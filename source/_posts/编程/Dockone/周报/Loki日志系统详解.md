
---
title: 'Loki日志系统详解'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/b59447b7c5afda68d1008b966fcb5fe3.jpeg'
author: Dockone
comments: false
date: 2021-08-11 09:07:51
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/b59447b7c5afda68d1008b966fcb5fe3.jpeg'
---

<div>   
<br><h3>背景</h3>最近，在对公司容器云的日志方案进行设计的时候，发现主流的ELK或者EFK比较重，再加上现阶段对于ES复杂的搜索功能很多都用不上最终选择了Grafana开源的Loki日志系统，下面介绍下Loki的背景。<br>
<h4>背景和动机</h4>当我们的容器云运行的应用或者某个节点出现问题了，解决思路应该如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210809/b59447b7c5afda68d1008b966fcb5fe3.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/b59447b7c5afda68d1008b966fcb5fe3.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
我们的监控使用的是基于Prometheus体系进行改造的，Prometheus中比较重要的是Metric和Alert，Metric是来说明当前或者历史达到了某个值，Alert设置Metric达到某个特定的基数触发了告警，但是这些信息明显是不够的。我们都知道，Kubernetes的基本单位是Pod，Pod把日志输出到stdout和stderr，平时有什么问题我们通常在界面或者通过命令查看相关的日志，举个例子：当我们的某个Pod的内存变得很大，触发了我们的Alert，这个时候管理员，去页面查询确认是哪个Pod有问题，然后要确认Pod内存变大的原因，我们还需要去查询Pod的日志，如果没有日志系统，那么我们就需要到页面或者使用命令进行查询了：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210809/ef7738dc0b9c685d1dbe6ddb6cf36179.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/ef7738dc0b9c685d1dbe6ddb6cf36179.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如果，这个时候应用突然挂了，这个时候我们就无法查到相关的日志了，所以需要引入日志系统，统一收集日志，而使用ELK的话，就需要在Kibana和Grafana之间切换，影响用户体验。所以 ，loki的第一目的就是最小化度量和日志的切换成本，有助于减少异常事件的响应时间和提高用户的体验。<br>
<h4>ELK存在的问题</h4>现有的很多日志采集的方案都是采用全文检索对日志进行索引（如ELK方案），优点是功能丰富，允许复杂的操作。但是，这些方案往往规模复杂，资源占用高，操作苦难。很多功能往往用不上，大多数查询只关注一定时间范围和一些简单的参数（如host、service等），使用这些解决方案就有点杀鸡用牛刀的感觉了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210809/2cb3931fda8bc5a80687949f9fcaf8ca.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/2cb3931fda8bc5a80687949f9fcaf8ca.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
因此，Loki的第二个目的是，在查询语言的易操作性和复杂性之间可以达到一个权衡。<br>
<h4>成本</h4>全文检索的方案也带来成本问题，简单的说就是全文搜索（如ES）的倒排索引的切分和共享的成本较高。后来出现了其他不同的设计方案如：<br>
<br><a href="https://github.com/oklog/oklog">OKlog</a>，采用最终一致的、基于网格的分布策略。这两个设计决策提供了大量的成本降低和非常简单的操作，但是查询不够方便。因此，Loki的第三个目的是，提高一个更具成本效益的解决方案。<br>
<h3>架构</h3><h4>整体架构</h4>Loki的架构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210809/6d8dcd103bf426f9905be1525a9123ab.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/6d8dcd103bf426f9905be1525a9123ab.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
不难看出，Loki的架构非常简单，使用了和Prometheus一样的标签来作为索引，也就是说，你通过这些标签既可以查询日志的内容也可以查询到监控的数据，不但减少了两种查询之间的切换成本，也极大地降低了日志索引的存储。Loki将使用与Prometheus相同的服务发现和标签重新标记库，编写了pormtail，在Kubernetes中promtail以DaemonSet方式运行在每个节点中，通过Kubernetes API等到日志的正确元数据，并将它们发送到Loki。下面是日志的存储架构：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210809/0b24bd94e155d9fe5181526a71562af7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/0b24bd94e155d9fe5181526a71562af7.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>读写</h4>日志数据的写主要依托的是Distributor和Ingester两个组件，整体的流程如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210809/6b8c63b9edbbc04d4d303051d853140a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/6b8c63b9edbbc04d4d303051d853140a.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>Distributor</strong><br>
<br>一旦promtail收集日志并将其发送给loki，Distributor就是第一个接收日志的组件。由于日志的写入量可能很大，所以不能在它们传入时将它们写入数据库。这会毁掉数据库。我们需要批处理和压缩数据。<br>
<br>Loki通过构建压缩数据块来实现这一点，方法是在日志进入时对其进行gzip操作，组件ingester是一个有状态的组件，负责构建和刷新chunck，当chunk达到一定的数量或者时间后，刷新到存储中去。每个流的日志对应一个ingester，当日志到达Distributor后，根据元数据和hash算法计算出应该到哪个ingester上面。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210809/02de0cb7ecb8803c5276027853e1c110.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/02de0cb7ecb8803c5276027853e1c110.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
此外，为了冗余和弹性，我们将其复制n（默认情况下为3）次。<br>
<br><strong>Ingester</strong><br>
<br>Ingester接收到日志并开始构建chunk：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210809/33f6f5416dbbf6044447318a01bb5380.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/33f6f5416dbbf6044447318a01bb5380.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
基本上就是将日志进行压缩并附加到chunk上面。一旦chunk“填满”（数据达到一定数量或者过了一定期限），ingester将其刷新到数据库。我们对块和索引使用单独的数据库，因为它们存储的数据类型不同。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210809/aa0737b5d90a678f021308b5bdd7763e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/aa0737b5d90a678f021308b5bdd7763e.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
刷新一个chunk之后，ingester然后创建一个新的空chunk并将新条目添加到该chunk中。<br>
<br><strong>Querier</strong><br>
<br>读取就非常简单了，由Querier负责给定一个时间范围和标签选择器，Querier查看索引以确定哪些块匹配，并通过greps将结果显示出来。它还从Ingester获取尚未刷新的最新数据。<br>
<br>对于每个查询，一个查询器将为您显示所有相关日志。实现了查询并行化，提供分布式grep，使即使是大型查询也是足够的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210809/eeb4d9fa5982cc43c979362d1af2bea5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210809/eeb4d9fa5982cc43c979362d1af2bea5.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>可扩展性</h4>Loki的索引存储可以是cassandra/bigtable/dynamodb，而chuncks可以是各种对象存储，Querier和Distributor都是无状态的组件。对于ingester他虽然是有状态的但是，当新的节点加入或者减少，整节点间的chunk会重新分配，已适应新的散列环。而Loki底层存储的实现Cortex已经 在实际的生产中投入使用多年了。有了这句话，我可以放心的在环境中实验一把了。<br>
<h3>部署</h3>Loki的安装非常简单。<br>
<h4>创建namespace</h4><pre class="prettyprint">oc new-project loki<br>
</pre><br>
<h4>权限设置</h4> <pre class="prettyprint">oc adm policy add-scc-to-user anyuid -z default -n loki<br>
oc adm policy add-cluster-role-to-user cluster-admin system:serviceaccount:loki:default<br>
</pre><br>
<h4>安装Loki</h4>安装命令：<br>
<pre class="prettyprint">oc create -f statefulset.json -n loki<br>
</pre><br>
statefulset.json如下：<br>
<pre class="prettyprint">&#123;<br>
"apiVersion": "apps/v1",<br>
"kind": "StatefulSet",<br>
"metadata": &#123;<br>
    "name": "loki"<br>
&#125;,<br>
"spec": &#123;<br>
    "podManagementPolicy": "OrderedReady",<br>
    "replicas": 1,<br>
    "revisionHistoryLimit": 10,<br>
    "selector": &#123;<br>
        "matchLabels": &#123;<br>
            "app": "loki"<br>
        &#125;<br>
    &#125;,<br>
    "serviceName": "womping-stoat-loki-headless",<br>
    "template": &#123;<br>
        "metadata": &#123;<br>
            "annotations": &#123;<br>
                "checksum/config": "da297d66ee53e0ce68b58e12be7ec5df4a91538c0b476cfe0ed79666343df72b",<br>
                "prometheus.io/port": "http-metrics",<br>
                "prometheus.io/scrape": "true"<br>
            &#125;,<br>
            "creationTimestamp": null,<br>
            "labels": &#123;<br>
                "app": "loki",<br>
                "name": "loki"<br>
            &#125;<br>
        &#125;,<br>
        "spec": &#123;<br>
            "affinity": &#123;&#125;,<br>
            "containers": [<br>
                &#123;<br>
                    "args": [<br>
                        "-config.file=/etc/loki/local-config.yaml"<br>
                    ],<br>
                    "image": "grafana/loki:latest",<br>
                    "imagePullPolicy": "IfNotPresent",<br>
                    "livenessProbe": &#123;<br>
                        "failureThreshold": 3,<br>
                        "httpGet": &#123;<br>
                            "path": "/ready",<br>
                            "port": "http-metrics",<br>
                            "scheme": "HTTP"<br>
                        &#125;,<br>
                        "initialDelaySeconds": 45,<br>
                        "periodSeconds": 10,<br>
                        "successThreshold": 1,<br>
                        "timeoutSeconds": 1<br>
                    &#125;,<br>
                    "name": "loki",<br>
                    "ports": [<br>
                        &#123;<br>
                            "containerPort": 3100,<br>
                            "name": "http-metrics",<br>
                            "protocol": "TCP"<br>
                        &#125;<br>
                    ],<br>
                    "readinessProbe": &#123;<br>
                        "failureThreshold": 3,<br>
                        "httpGet": &#123;<br>
                            "path": "/ready",<br>
                            "port": "http-metrics",<br>
                            "scheme": "HTTP"<br>
                        &#125;,<br>
                        "initialDelaySeconds": 45,<br>
                        "periodSeconds": 10,<br>
                        "successThreshold": 1,<br>
                        "timeoutSeconds": 1<br>
                    &#125;,<br>
                    "resources": &#123;&#125;,<br>
                    "terminationMessagePath": "/dev/termination-log",<br>
                    "terminationMessagePolicy": "File",<br>
                    "volumeMounts": [<br>
                        &#123;<br>
                            "mountPath": "/tmp/loki",<br>
                            "name": "storage"<br>
                        &#125;<br>
                    ]<br>
                &#125;<br>
            ],<br>
            "dnsPolicy": "ClusterFirst",<br>
            "restartPolicy": "Always",<br>
            "schedulerName": "default-scheduler",<br>
            "terminationGracePeriodSeconds": 30,<br>
            "volumes": [<br>
                &#123;<br>
                    "emptyDir": &#123;&#125;,<br>
                    "name": "storage"<br>
                &#125;<br>
            ]<br>
        &#125;<br>
    &#125;,<br>
    "updateStrategy": &#123;<br>
        "type": "RollingUpdate"<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
<h4>安装Promtail</h4>安装命令：<br>
<pre class="prettyprint">oc create -f configmap.json -n loki<br>
</pre><br>
configmap.json如下：<br>
<pre class="prettyprint">&#123;<br>
"apiVersion": "v1",<br>
"data": &#123;<br>
    "promtail.yaml": "client:\n  backoff_config:\n    maxbackoff: 5s\n    maxretries: 5\n    minbackoff: 100ms\n  batchsize: 102400\n  batchwait: 1s\n  external_labels: &#123;&#125;\n  timeout: 10s\npositions:\n  filename: /run/promtail/positions.yaml\nserver:\n  http_listen_port: 3101\ntarget_config:\n  sync_period: 10s\n\nscrape_configs:\n- job_name: kubernetes-pods-name\n  pipeline_stages:\n    - docker: &#123;&#125;\n    \n  kubernetes_sd_configs:\n  - role: pod\n  relabel_configs:\n  - source_labels:\n    - __meta_kubernetes_pod_label_name\n    target_label: __service__\n  - source_labels:\n    - __meta_kubernetes_pod_node_name\n    target_label: __host__\n  - action: drop\n    regex: ^$\n    source_labels:\n    - __service__\n  - action: labelmap\n    regex: __meta_kubernetes_pod_label_(.+)\n  - action: replace\n    replacement: $1\n    separator: /\n    source_labels:\n    - __meta_kubernetes_namespace\n    - __service__\n    target_label: job\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_namespace\n    target_label: namespace\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_pod_name\n    target_label: instance\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_pod_container_name\n    target_label: container_name\n  - replacement: /var/log/pods/*$1/*.log\n    separator: /\n    source_labels:\n    - __meta_kubernetes_pod_uid\n    - __meta_kubernetes_pod_container_name\n    target_label: __path__\n- job_name: kubernetes-pods-app\n  pipeline_stages:\n    - docker: &#123;&#125;\n    \n  kubernetes_sd_configs:\n  - role: pod\n  relabel_configs:\n  - action: drop\n    regex: .+\n    source_labels:\n    - __meta_kubernetes_pod_label_name\n  - source_labels:\n    - __meta_kubernetes_pod_label_app\n    target_label: __service__\n  - source_labels:\n    - __meta_kubernetes_pod_node_name\n    target_label: __host__\n  - action: drop\n    regex: ^$\n    source_labels:\n    - __service__\n  - action: labelmap\n    regex: __meta_kubernetes_pod_label_(.+)\n  - action: replace\n    replacement: $1\n    separator: /\n    source_labels:\n    - __meta_kubernetes_namespace\n    - __service__\n    target_label: job\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_namespace\n    target_label: namespace\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_pod_name\n    target_label: instance\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_pod_container_name\n    target_label: container_name\n  - replacement: /var/log/pods/*$1/*.log\n    separator: /\n    source_labels:\n    - __meta_kubernetes_pod_uid\n    - __meta_kubernetes_pod_container_name\n    target_label: __path__\n- job_name: kubernetes-pods-direct-controllers\n  pipeline_stages:\n    - docker: &#123;&#125;\n    \n  kubernetes_sd_configs:\n  - role: pod\n  relabel_configs:\n  - action: drop\n    regex: .+\n    separator: ''\n    source_labels:\n    - __meta_kubernetes_pod_label_name\n    - __meta_kubernetes_pod_label_app\n  - action: drop\n    regex: ^([0-9a-z-.]+)(-[0-9a-f]&#123;8,10&#125;)$\n    source_labels:\n    - __meta_kubernetes_pod_controller_name\n  - source_labels:\n    - __meta_kubernetes_pod_controller_name\n    target_label: __service__\n  - source_labels:\n    - __meta_kubernetes_pod_node_name\n    target_label: __host__\n  - action: drop\n    regex: ^$\n    source_labels:\n    - __service__\n  - action: labelmap\n    regex: __meta_kubernetes_pod_label_(.+)\n  - action: replace\n    replacement: $1\n    separator: /\n    source_labels:\n    - __meta_kubernetes_namespace\n    - __service__\n    target_label: job\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_namespace\n    target_label: namespace\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_pod_name\n    target_label: instance\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_pod_container_name\n    target_label: container_name\n  - replacement: /var/log/pods/*$1/*.log\n    separator: /\n    source_labels:\n    - __meta_kubernetes_pod_uid\n    - __meta_kubernetes_pod_container_name\n    target_label: __path__\n- job_name: kubernetes-pods-indirect-controller\n  pipeline_stages:\n    - docker: &#123;&#125;\n    \n  kubernetes_sd_configs:\n  - role: pod\n  relabel_configs:\n  - action: drop\n    regex: .+\n    separator: ''\n    source_labels:\n    - __meta_kubernetes_pod_label_name\n    - __meta_kubernetes_pod_label_app\n  - action: keep\n    regex: ^([0-9a-z-.]+)(-[0-9a-f]&#123;8,10&#125;)$\n    source_labels:\n    - __meta_kubernetes_pod_controller_name\n  - action: replace\n    regex: ^([0-9a-z-.]+)(-[0-9a-f]&#123;8,10&#125;)$\n    source_labels:\n    - __meta_kubernetes_pod_controller_name\n    target_label: __service__\n  - source_labels:\n    - __meta_kubernetes_pod_node_name\n    target_label: __host__\n  - action: drop\n    regex: ^$\n    source_labels:\n    - __service__\n  - action: labelmap\n    regex: __meta_kubernetes_pod_label_(.+)\n  - action: replace\n    replacement: $1\n    separator: /\n    source_labels:\n    - __meta_kubernetes_namespace\n    - __service__\n    target_label: job\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_namespace\n    target_label: namespace\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_pod_name\n    target_label: instance\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_pod_container_name\n    target_label: container_name\n  - replacement: /var/log/pods/*$1/*.log\n    separator: /\n    source_labels:\n    - __meta_kubernetes_pod_uid\n    - __meta_kubernetes_pod_container_name\n    target_label: __path__\n- job_name: kubernetes-pods-static\n  pipeline_stages:\n    - docker: &#123;&#125;\n    \n  kubernetes_sd_configs:\n  - role: pod\n  relabel_configs:\n  - action: drop\n    regex: ^$\n    source_labels:\n    - __meta_kubernetes_pod_annotation_kubernetes_io_config_mirror\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_pod_label_component\n    target_label: __service__\n  - source_labels:\n    - __meta_kubernetes_pod_node_name\n    target_label: __host__\n  - action: drop\n    regex: ^$\n    source_labels:\n    - __service__\n  - action: labelmap\n    regex: __meta_kubernetes_pod_label_(.+)\n  - action: replace\n    replacement: $1\n    separator: /\n    source_labels:\n    - __meta_kubernetes_namespace\n    - __service__\n    target_label: job\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_namespace\n    target_label: namespace\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_pod_name\n    target_label: instance\n  - action: replace\n    source_labels:\n    - __meta_kubernetes_pod_container_name\n    target_label: container_name\n  - replacement: /var/log/pods/*$1/*.log\n    separator: /\n    source_labels:\n    - __meta_kubernetes_pod_annotation_kubernetes_io_config_mirror\n    - __meta_kubernetes_pod_container_name\n    target_label: __path__\n"<br>
&#125;,<br>
"kind": "ConfigMap",<br>
"metadata": &#123;<br>
    "creationTimestamp": "2019-09-05T01:05:03Z",<br>
    "labels": &#123;<br>
        "app": "promtail",<br>
        "chart": "promtail-0.12.0",<br>
        "heritage": "Tiller",<br>
        "release": "lame-zorse"<br>
    &#125;,<br>
    "name": "lame-zorse-promtail",<br>
    "namespace": "loki",<br>
    "resourceVersion": "17921611",<br>
    "selfLink": "/api/v1/namespaces/loki/configmaps/lame-zorse-promtail",<br>
    "uid": "30fcb896-cf79-11e9-b58e-e4a8b6cc47d2"<br>
&#125;<br>
&#125;<br>
<br>
<br>
<br>
<br>
oc create -f daemonset.json -n loki<br>
</pre><br>
daemonset.json如下：<br>
<pre class="prettyprint">&#123;<br>
        "apiVersion": "apps/v1",<br>
        "kind": "DaemonSet",<br>
        "metadata": &#123;<br>
            "annotations": &#123;<br>
                "deployment.kubernetes.io/revision": "2"<br>
            &#125;,<br>
            "creationTimestamp": "2019-09-05T01:16:37Z",<br>
            "generation": 2,<br>
            "labels": &#123;<br>
                "app": "promtail",<br>
                "chart": "promtail-0.12.0",<br>
                "heritage": "Tiller",<br>
                "release": "lame-zorse"<br>
            &#125;,<br>
            "name": "lame-zorse-promtail",<br>
            "namespace": "loki"<br>
        &#125;,<br>
        "spec": &#123;<br>
            "progressDeadlineSeconds": 600,<br>
            "replicas": 1,<br>
            "revisionHistoryLimit": 10,<br>
            "selector": &#123;<br>
                "matchLabels": &#123;<br>
                    "app": "promtail",<br>
                    "release": "lame-zorse"<br>
                &#125;<br>
            &#125;,<br>
            "strategy": &#123;<br>
                "rollingUpdate": &#123;<br>
                    "maxSurge": 1,<br>
                    "maxUnavailable": 1<br>
                &#125;,<br>
                "type": "RollingUpdate"<br>
            &#125;,<br>
            "template": &#123;<br>
                "metadata": &#123;<br>
                    "annotations": &#123;<br>
                        "checksum/config": "75a25ee4f2869f54d394bf879549a9c89c343981a648f8d878f69bad65dba809",<br>
                        "prometheus.io/port": "http-metrics",<br>
                        "prometheus.io/scrape": "true"<br>
                    &#125;,<br>
                    "creationTimestamp": null,<br>
                    "labels": &#123;<br>
                        "app": "promtail",<br>
                        "release": "lame-zorse"<br>
                    &#125;<br>
                &#125;,<br>
                "spec": &#123;<br>
                    "affinity": &#123;&#125;,<br>
                    "containers": [<br>
                        &#123;<br>
                            "args": [<br>
                                "-config.file=/etc/promtail/promtail.yaml",<br>
                                "-client.url=http://loki.loki.svc:3100/api/prom/push"<br>
                            ],<br>
                            "env": [<br>
                                &#123;<br>
                                    "name": "HOSTNAME",<br>
                                    "valueFrom": &#123;<br>
                                        "fieldRef": &#123;<br>
                                            "apiVersion": "v1",<br>
                                            "fieldPath": "spec.nodeName"<br>
                                        &#125;<br>
                                    &#125;<br>
                                &#125;<br>
                            ],<br>
                            "image": "grafana/promtail:v0.3.0",<br>
                            "imagePullPolicy": "IfNotPresent",<br>
                            "name": "promtail",<br>
                            "ports": [<br>
                                &#123;<br>
                                    "containerPort": 3101,<br>
                                    "name": "http-metrics",<br>
                                    "protocol": "TCP"<br>
                                &#125;<br>
                            ],<br>
                            "readinessProbe": &#123;<br>
                                "failureThreshold": 5,<br>
                                "httpGet": &#123;<br>
                                    "path": "/ready",<br>
                                    "port": "http-metrics",<br>
                                    "scheme": "HTTP"<br>
                                &#125;,<br>
                                "initialDelaySeconds": 10,<br>
                                "periodSeconds": 10,<br>
                                "successThreshold": 1,<br>
                                "timeoutSeconds": 1<br>
                            &#125;,<br>
                            "resources": &#123;&#125;,<br>
                            "securityContext": &#123;<br>
                                "readOnlyRootFilesystem": true,<br>
                                "runAsUser": 0<br>
                            &#125;,<br>
                            "terminationMessagePath": "/dev/termination-log",<br>
                            "terminationMessagePolicy": "File",<br>
                            "volumeMounts": [<br>
                                &#123;<br>
                                    "mountPath": "/etc/promtail",<br>
                                    "name": "config"<br>
                                &#125;,<br>
                                &#123;<br>
                                    "mountPath": "/run/promtail",<br>
                                    "name": "run"<br>
                                &#125;,<br>
                                &#123;<br>
                                    "mountPath": "/var/lib/docker/containers",<br>
                                    "name": "docker",<br>
                                    "readOnly": true<br>
                                &#125;,<br>
                                &#123;<br>
                                    "mountPath": "/var/log/pods",<br>
                                    "name": "pods",<br>
                                    "readOnly": true<br>
                                &#125;<br>
                            ]<br>
                        &#125;<br>
                    ],<br>
                    "dnsPolicy": "ClusterFirst",<br>
                    "restartPolicy": "Always",<br>
                    "schedulerName": "default-scheduler",<br>
                    "securityContext": &#123;&#125;,<br>
                    "terminationGracePeriodSeconds": 30,<br>
                    "volumes": [<br>
                        &#123;<br>
                            "configMap": &#123;<br>
                                "defaultMode": 420,<br>
                                "name": "lame-zorse-promtail"<br>
                            &#125;,<br>
                            "name": "config"<br>
                        &#125;,<br>
                        &#123;<br>
                            "hostPath": &#123;<br>
                                "path": "/run/promtail",<br>
                                "type": ""<br>
                            &#125;,<br>
                            "name": "run"<br>
                        &#125;,<br>
                        &#123;<br>
                            "hostPath": &#123;<br>
                                "path": "/var/lib/docker/containers",<br>
                                "type": ""<br>
                            &#125;,<br>
                            "name": "docker"<br>
                        &#125;,<br>
                        &#123;<br>
                            "hostPath": &#123;<br>
                                "path": "/var/log/pods",<br>
                                "type": ""<br>
                            &#125;,<br>
                            "name": "pods"<br>
                        &#125;<br>
                    ]<br>
                &#125;<br>
            &#125;<br>
        &#125;<br>
    &#125; <br>
</pre><br>
<h4>安装服务</h4><pre class="prettyprint">oc create -f service.json -n loki<br>
</pre><br>
service.json的内容如下：<br>
<pre class="prettyprint">&#123;<br>
"apiVersion": "v1",<br>
"kind": "Service",<br>
"metadata": &#123;<br>
    "creationTimestamp": "2019-09-04T09:37:49Z",<br>
    "name": "loki",<br>
    "namespace": "loki",<br>
    "resourceVersion": "17800188",<br>
    "selfLink": "/api/v1/namespaces/loki/services/loki",<br>
    "uid": "a87fe237-cef7-11e9-b58e-e4a8b6cc47d2"<br>
&#125;,<br>
"spec": &#123;<br>
    "externalTrafficPolicy": "Cluster",<br>
    "ports": [<br>
        &#123;<br>
            "name": "lokiport",<br>
            "port": 3100,<br>
            "protocol": "TCP",<br>
            "targetPort": 3100<br>
        &#125;<br>
    ],<br>
    "selector": &#123;<br>
        "app": "loki"<br>
    &#125;,<br>
    "sessionAffinity": "None",<br>
    "type": "NodePort"<br>
&#125;,<br>
"status": &#123;<br>
    "loadBalancer": &#123;&#125;<br>
&#125; <br>
</pre><br>
<h3>语法</h3>Loki提供了HTTP接口，我们这里就不详解了，大家可以看：<a href="https://github.com/grafana/loki/blob/master/docs/api.md" rel="nofollow" target="_blank">https://github.com/grafana/lok ... pi.md</a><br>
<br>我们这里说下查询的接口如何使用。<br>
<br>第一步，获取当前Loki的元数据类型：<br>
<pre class="prettyprint">curl http://192.168.25.30:30972/api/prom/label<br>
&#123;<br>
"values": ["alertmanager", "app", "component", "container_name", "controller_revision_hash", "deployment", "deploymentconfig", "docker_registry", "draft", "filename", "instance", "job", "logging_infra", "metrics_infra", "name", "namespace", "openshift_io_component", "pod_template_generation", "pod_template_hash", "project", "projectname", "prometheus", "provider", "release", "router", "servicename", "statefulset_kubernetes_io_pod_name", "stream", "tekton_dev_pipeline", "tekton_dev_pipelineRun", "tekton_dev_pipelineTask", "tekton_dev_task", "tekton_dev_taskRun", "type", "webconsole"]<br>
&#125; <br>
</pre><br>
第二步，获取某个元数据类型的值：<br>
<pre class="prettyprint">curl http://192.168.25.30:30972/api/prom/label/namespace/values<br>
&#123;"values":["cicd","default","gitlab","grafanaserver","jenkins","jx-staging","kube-system","loki","mysql-exporter","new2","openshift-console","openshift-infra","openshift-logging","openshift-monitoring","openshift-node","openshift-sdn","openshift-web-console","tekton-pipelines","test111"]&#125; <br>
</pre><br>
第三步，根据label进行查询，例如：<br>
<pre class="prettyprint">http://192.168.25.30:30972/api/prom/query?direction=BACKWARD&limit=1000&regexp=&query=&#123;namespace="cicd"&#125;&start=1567644457221000000&end=1567730857221000000&refId=A<br>
</pre><br>
参数解析：<br>
<ul><li>query：一种查询语法详细见下面章节，&#123;name=~“mysql.+”&#125; or &#123;namespace=“cicd”&#125; |= "error"表示查询，namespace为CI/CD的日志中，有error字样的信息。</li><li>limit：返回日志的数量</li><li>`start：开始时间，Unix时间表示方法 默认为，一小时前时间</li><li>end：结束时间，默认为当前时间</li><li>direction：forward或者backward，指定limit时候有用，默认为 backward</li><li>regexp：对结果进行regex过滤</li></ul><br>
<br><h4>LogQL语法</h4><strong>选择器</strong><br>
<br>对于查询表达式的标签部分，将放在&#123;&#125;中，多个标签表达式用逗号分隔：<br>
<pre class="prettyprint">&#123;app="mysql",name="mysql-backup"&#125; <br>
</pre><br>
支持的符号有：<br>
<ul><li>=：完全相同。</li><li>!=：不平等。</li><li>=~：正则表达式匹配。</li><li>!~：不要正则表达式匹配。</li></ul><br>
<br><strong>过滤表达式</strong><br>
<br>编写日志流选择器后，您可以通过编写搜索表达式进一步过滤结果。搜索表达式可以文本或正则表达式。<br>
<br>如：<br>
<ul><li>&#123;job=“mysql”&#125; |= “error”</li><li>&#123;name=“kafka”&#125; |~ “tsdb-ops.*io:2003”</li><li>&#123;instance=~“kafka-[23]”,name=“kafka”&#125; != kafka.server:type=ReplicaManager</li></ul><br>
<br>支持多个过滤：<br>
<ul><li>&#123;job=“mysql”&#125; |= “error” != “timeout”</li></ul><br>
<br>目前支持的操作符：<br>
<ul><li>|= line包含字符串。</li><li>!= line不包含字符串。</li><li>|~ line匹配正则表达式。</li><li>!~ line与正则表达式不匹配。</li></ul><br>
<br>表达式遵循<a href="https://github.com/google/re2/wiki/Syntax" rel="nofollow" target="_blank">https://github.com/google/re2/wiki/Syntax</a>语法。<br>
<br>原文链接：<br>
<ul><li><a href="https://blog.csdn.net/Linkthaha/article/details/100575278" rel="nofollow" target="_blank">https://blog.csdn.net/Linkthah ... 75278</a></li><li><a href="http://blog.csdn.net/Linkthaha/article/details/100575651" rel="nofollow" target="_blank">http://blog.csdn.net/Linkthaha ... 75651</a></li><li><a href="https://blog.csdn.net/Linkthaha/article/details/100582422" rel="nofollow" target="_blank">https://blog.csdn.net/Linkthah ... 82422</a></li><li><a href="https://blog.csdn.net/Linkthaha/article/details/100582587" rel="nofollow" target="_blank">https://blog.csdn.net/Linkthah ... 82587</a></li></ul><br>
<br>作者：linkt1234
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            