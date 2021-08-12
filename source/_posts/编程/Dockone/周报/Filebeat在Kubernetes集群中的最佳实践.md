
---
title: 'Filebeat在Kubernetes集群中的最佳实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210810/619ff7659bce28f92d2830a147f4dc8b.png'
author: Dockone
comments: false
date: 2021-08-12 09:07:54
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210810/619ff7659bce28f92d2830a147f4dc8b.png'
---

<div>   
<br><h3>背景</h3>在Kubernetes还未兴起的时代，业务部署几乎所有应用都采用单机部署，当压力增大时，IDC架构只能横向拓展服务器集群，增加算力，云计算兴起后，可以动态的调整已有服务器的配置，来分担压力，或者可以通过弹性伸缩来实现根据业务量大小、集群负载、监控等情况，动态的横向调整后端服务器的数量。日志作为应用系统的一部分，通常在系统异常时，用来排查故障，寻找原因，传统的日志处理方式通常结合<code class="prettyprint">grep</code>和<code class="prettyprint">Linux</code>常见的文本命令工具进行分析。<br>
<br>为了支持更快的开发、迭代效率，近年来开始了容器化改造，并开始了拥抱Kubernetes生态、业务全量上云等工作。在这阶段，日志无论从规模、种类都呈现爆炸式的增长，对日志进行数字化、智能化分析的需求也越来越高，因此统一的日志平台应运而生。<br>
<h3>Kubernetes日志系统收集难点</h3>单纯日志系统的解决方案非常多，相对也比较成熟，这里就不再去赘述，我们此次只针对Kubernetes上的日志系统建设而论。Kubernetes上的日志方案相比我们之前基于物理机、虚拟机场景的日志方案有很大不同，例如：<br>
<ul><li>日志的形式变得更加复杂，不仅有物理机/虚拟机上的日志，还有容器的标准输出、容器内的文件、容器事件、Kubernetes事件等等信息需要采集；</li><li>环境的动态性变强，在Kubernetes中，机器的宕机、下线、上线、Pod销毁、扩容/缩容等都是常态，这种情况下日志的存在是瞬时的（例如如果Pod销毁后该Pod日志就不可见了），所以日志数据必须实时采集到服务端。同时还需要保证日志的采集能够适应这种动态性极强的场景；</li><li>日志的种类变多，上图是一个典型的Kubernetes架构，一个请求从客户端需要经过CDN、Ingress、Service Mesh、Pod等多个组件，涉及多种基础设施，其中的日志种类增加了很多，例如Kubernetes各种系统组件日志、审计日志、ServiceMesh日志、Ingress等。</li></ul><br>
<br><h3>Kubernetes日志文件说明</h3>关于<code class="prettyprint">Kubenetes</code>的日志采集，部署方式是采用<code class="prettyprint">DaemonSet</code>的方式，采集时按照Kubernetes集群的<code class="prettyprint">namespace</code>进行分类，然后根据<code class="prettyprint">namespace</code>的名称创建不同的<code class="prettyprint">topic</code>到Kafka中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210810/619ff7659bce28f92d2830a147f4dc8b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210810/619ff7659bce28f92d2830a147f4dc8b.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
一般情况下，Kubernetes默认会在<code class="prettyprint">/var/log/containers</code>和<code class="prettyprint">/var/log/pods</code>目录中会生成这些日志文件的软连接，如下所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210810/423cdbfed5ca47a6912b3fa1f760762a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210810/423cdbfed5ca47a6912b3fa1f760762a.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
然后，会看到这个目录下存在了此宿主机上的所有容器日志，文件的命名方式为：<br>
<pre class="prettyprint">[podName]_[nameSpace]_[depoymentName]-[containerId].log<br>
</pre><br>
上面这个是<code class="prettyprint">deployment</code>的命名方式，其他的会有些不同，例如：<code class="prettyprint">DaemonSet</code>，<code class="prettyprint">StatefulSet</code>等，不过所有的都有一个共同点，就是：<br>
<pre class="prettyprint">*_[nameSpace]_*.log<br>
</pre><br>
到这里，知道这个特性，就可以往下来看<code class="prettyprint">Filebeat</code>的部署和配置了。<br>
<h3>Filebeat</h3><h4>部署</h4>部署采用的<code class="prettyprint">DaemonSet</code>方式进行：<br>
<pre class="prettyprint">---<br>
apiVersion: v1<br>
kind: ConfigMap<br>
metadata:<br>
name: filebeat-config<br>
namespace: log<br>
data:<br>
filebeat.yml: |-<br>
filebeat.inputs:<br>
- type: container<br>
  enabled: true<br>
  paths:<br>
  - /var/log/containers/*_default_*.log<br>
  fields:<br>
    namespace: default<br>
    env: dev<br>
    k8s: cluster-dev<br>
- type: container<br>
  enabled: true<br>
  paths:<br>
  - /var/log/containers/*_kube-system_*.log<br>
  fields:<br>
    namespace: kube-system<br>
    env: dev<br>
    k8s: cluster-dev<br>
filebeat.config.modules:<br>
  path: $&#123;path.config&#125;/modules.d/*.yml<br>
  reload.enabled: false<br>
output.kafka:<br>
  hosts: ["175.27.159.78:9092","175.27.159.78:9093","175.27.159.78:9094"]<br>
  topic: '%&#123;[fields.k8s]&#125;-%&#123;[fields.namespace]&#125;'<br>
  partition.round_robin:<br>
    reachable_only: true<br>
---<br>
apiVersion: apps/v1<br>
kind: DaemonSet<br>
metadata:<br>
name: filebeat<br>
namespace: log <br>
labels:<br>
k8s-app: filebeat<br>
spec:<br>
selector:<br>
matchLabels:<br>
  k8s-app: filebeat<br>
template:<br>
metadata:<br>
  labels:<br>
    k8s-app: filebeat<br>
spec:<br>
  serviceAccountName: filebeat<br>
  terminationGracePeriodSeconds: 30<br>
  hostNetwork: true<br>
  dnsPolicy: ClusterFirstWithHostNet<br>
  containers:<br>
  - name: filebeat<br>
    image: docker.elastic.co/beats/filebeat:7.12.0<br>
    args: [<br>
      "-c", "/etc/filebeat.yml",<br>
      "-e",<br>
    ]<br>
    env:<br>
    - name: NODE_NAME<br>
      valueFrom:<br>
        fieldRef:<br>
          fieldPath: spec.nodeName<br>
    securityContext:<br>
      runAsUser: 0<br>
      # If using Red Hat OpenShift uncomment this:<br>
      #privileged: true<br>
    resources:<br>
      limits:<br>
        memory: 200Mi<br>
      requests:<br>
        cpu: 100m<br>
        memory: 100Mi<br>
    volumeMounts:<br>
    - name: config<br>
      mountPath: /etc/filebeat.yml<br>
      readOnly: true<br>
      subPath: filebeat.yml<br>
    - name: data<br>
      mountPath: /usr/share/filebeat/data<br>
    - name: varlibdockercontainers<br>
      mountPath: /data/docker/containers<br>
      readOnly: true<br>
    - name: varlog<br>
      mountPath: /var/log<br>
      readOnly: true<br>
  volumes:<br>
  - name: config<br>
    configMap:<br>
      defaultMode: 0640<br>
      name: filebeat-config<br>
  - name: varlog<br>
    hostPath:<br>
      path: /var/log<br>
  - name: varlibdockercontainers<br>
    hostPath:<br>
      path: /data/docker/containers<br>
  # data folder stores a registry of read status for all files, so we don't send everything again on a Filebeat pod restart<br>
  - name: data<br>
    hostPath:<br>
      # When filebeat runs as non-root user, this directory needs to be writable by group (g+w).<br>
      path: /var/lib/filebeat-data<br>
      type: DirectoryOrCreate<br>
---<br>
apiVersion: rbac.authorization.k8s.io/v1<br>
kind: ClusterRoleBinding<br>
metadata:<br>
name: filebeat<br>
subjects:<br>
- kind: ServiceAccount<br>
name: filebeat<br>
namespace: log<br>
roleRef:<br>
kind: ClusterRole<br>
name: filebeat<br>
<h2>  apiGroup: rbac.authorization.k8s.io</h2>apiVersion: rbac.authorization.k8s.io/v1<br>
kind: ClusterRole<br>
metadata:<br>
name: filebeat<br>
labels:<br>
k8s-app: filebeat<br>
rules:<br>
- apiGroups: [""] # "" indicates the core API group<br>
resources:<br>
- namespaces<br>
- pods<br>
- nodes<br>
verbs:<br>
- get<br>
- watch<br>
- list<br>
- apiGroups: ["apps"]<br>
resources:<br>
- replicasets<br>
<h2>  verbs: ["get", "list", "watch"]</h2>apiVersion: v1<br>
kind: ServiceAccount<br>
metadata:<br>
name: filebeat<br>
namespace: log <br>
labels:<br>
k8s-app: filebeat<br>
</pre><br>
<pre class="prettyprint">[root@master filebeat]# kubectl apply -f filebeat-daemonset.yaml <br>
configmap/filebeat-daemonset-config-test created<br>
daemonset.apps/filebeat created<br>
clusterrolebinding.rbac.authorization.k8s.io/filebeat created<br>
clusterrole.rbac.authorization.k8s.io/filebeat created<br>
serviceaccount/filebeat created<br>
</pre><br>
<h4>Filebeat配置文件介绍</h4>这里先简单介绍下<code class="prettyprint">Filebeat</code>的配置结构：<br>
<pre class="prettyprint">filebeat.inputs:<br>
<br>
filebeat.config.modules:<br>
<br>
processors:<br>
<br>
output.xxxxx:<br>
</pre><br>
结构大概是这么个结构，完整的数据流向简单来说就是下面这个图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210810/c18916880b98228ec10cce4414022a3c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210810/c18916880b98228ec10cce4414022a3c.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>inputs</h4>根据命名空间做分类，每一个命名空间就是一个topic，如果要收集多个集群，同样也是使用命名空间做分类，只不过topic的命名就需要加个Kubernetes的集群名，这样方便去区分了，那既然是通过命名空间来获取日志，那么在配置<code class="prettyprint">inputs</code>的时候就需要通过写正则将指定命名空间下的日志文件取出，然后读取，例如：<br>
<pre class="prettyprint">filebeat.inputs:<br>
- type: container<br>
enabled: true<br>
paths:<br>
- /var/log/containers/*_default_*.log<br>
fields:<br>
namespace: default<br>
env: dev<br>
k8s: cluster-dev<br>
</pre><br>
这里是写了一个命名空间，如果有多个，就排开写就行了，如下所示：<br>
<pre class="prettyprint">filebeat.inputs:<br>
- type: container<br>
enabled: true<br>
paths:<br>
- /var/log/containers/*_default_*.log<br>
fields:<br>
namespace: default<br>
env: dev<br>
k8s: cluster-dev<br>
- type: container<br>
enabled: true<br>
paths:<br>
- /var/log/containers/*_kube-system_*.log<br>
fields:<br>
namespace: kube-system<br>
env: dev<br>
k8s: cluster-dev<br>
</pre><br>
上面说了通过命名空间创建<code class="prettyprint">topic</code>，我这里加了一个自定义的字段<code class="prettyprint">namespace</code>，就是后面的<code class="prettyprint">topic</code>的名称，但是这里有很多的命名空间，那在输出的时候，如何动态去创建呢？<br>
<pre class="prettyprint">output.kafka:<br>
hosts: ["10.0.105.74:9092","10.0.105.76:9092","10.0.105.96:9092"]<br>
topic: '%&#123;[fields.namespace]&#125;'<br>
partition.round_robin:<br>
reachable_only: true<br>
</pre><br>
那么目前，完整的配置文件如下：<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: ConfigMap<br>
metadata:<br>
name: filebeat-config<br>
namespace: log<br>
data:<br>
filebeat.yml: |-<br>
filebeat.inputs:<br>
- type: container<br>
  enabled: true<br>
  paths:<br>
  - /var/log/containers/*_default_*.log<br>
  fields:<br>
    namespace: default<br>
    env: dev<br>
    k8s: cluster-dev<br>
- type: container<br>
  enabled: true<br>
  paths:<br>
  - /var/log/containers/*_kube-system_*.log<br>
  fields:<br>
    namespace: kube-system<br>
    env: dev<br>
    k8s: cluster-dev<br>
filebeat.config.modules:<br>
  path: $&#123;path.config&#125;/modules.d/*.yml<br>
  reload.enabled: false<br>
output.kafka:<br>
  hosts: ["175.27.159.78:9092","175.27.159.78:9093","175.27.159.78:9094"]<br>
  topic: '%&#123;[fields.k8s]&#125;-%&#123;[fields.namespace]&#125;'<br>
  partition.round_robin:<br>
    reachable_only: true<br>
</pre><br>
<h4>processors</h4>如果是不对日志做任何处理，到这里就结束了，但是这样又视乎在查看日志的时候少了点什么？ 到这里仅仅知道日志内容，和该日志来自于哪个命名空间，但是你不知道该日志属于哪个服务，哪个Pod，甚至说想查看该服务的镜像地址等，但是这些信息在我们上面的配置方式中是没有的，所以需要进一步的添砖加瓦。<br>
<br>这个时候就用到了一个配置项，叫做： <code class="prettyprint">processors</code>。<br>
<br><strong>添加Kubernetes的基本信息</strong><br>
<br>在采集Kubernetes的日志时，如果按照上面那种配置方式，是没有关于Pod的一些信息的，例如：<br>
<ul><li>Pod Name</li><li>Pod UID</li><li>Namespace</li><li>Labels</li></ul><br>
<br>添加前日志示例：<br>
<pre class="prettyprint">&#123;<br>
"@timestamp": "2021-05-06T02:47:09.256Z",<br>
"@metadata": &#123;<br>
"beat": "filebeat",<br>
"type": "_doc",<br>
"version": "7.12.0"<br>
&#125;,<br>
"log": &#123;<br>
"file": &#123;<br>
  "path": "/var/log/containers/metrics-server-5549c7694f-7vb66_kube-system_metrics-server-9108765e17c7e325abd665fb0f53c8f4b3077c698cb88392099dfbafb0475709.log"<br>
&#125;,<br>
"offset": 15842<br>
&#125;,<br>
"stream": "stderr",<br>
"message": "E0506 02:47:09.254911       1 reststorage.go:160] unable to fetch pod metrics for pod log/filebeat-s67ds: no metrics known for pod",<br>
"input": &#123;<br>
"type": "container"<br>
&#125;,<br>
"fields": &#123;<br>
"env": "dev",<br>
"k8s": "cluster-dev",<br>
"namespace": "kube-system"<br>
&#125;,<br>
"ecs": &#123;<br>
"version": "1.8.0"<br>
&#125;,<br>
"host": &#123;<br>
"name": "node-03"<br>
&#125;,<br>
"agent": &#123;<br>
"hostname": "node-03",<br>
"ephemeral_id": "1c87559a-cfca-4708-8f28-e4fc6441943c",<br>
"id": "f9cf0cd4-eccf-4d8b-bd24-2bff25b4083b",<br>
"name": "node-03",<br>
"type": "filebeat",<br>
"version": "7.12.0"<br>
&#125;<br>
&#125; <br>
</pre><br>
那么如果想添加这些信息，就要使用<code class="prettyprint">processors</code>中的一个工具，叫做：<code class="prettyprint">add_kubernetes_metadata</code>，字面意思就是添加Kubernetes的一些元数据信息，使用方法可以先来看一段示例：<br>
<pre class="prettyprint">processors:<br>
- add_kubernetes_metadata:<br>
  host: $&#123;NODE_NAME&#125;<br>
  matchers:<br>
  - logs_path:<br>
      logs_path: "/var/log/containers/"<br>
</pre><br>
<ul><li><code class="prettyprint">host</code>：指定要对Filebeat起作用的节点，防止无法准确检测到它，比如在主机网络模式下运行Filebeat</li><li><code class="prettyprint">matchers</code>：匹配器用于构造与索引创建的标识符相匹配的查找键</li><li><code class="prettyprint">logs_path</code>：容器日志的基本路径，如果未指定，则使用Filebeat运行的平台的默认日志路径</li></ul><br>
<br>加上这个Kubernetes的元数据信息之后，就可以在日志里面看到Kubernetes的信息了，看一下添加Kubernetes信息后的日志格式：<br>
<pre class="prettyprint">&#123;<br>
"@timestamp": "2021-05-06T03:01:58.512Z",<br>
"@metadata": &#123;<br>
"beat": "filebeat",<br>
"type": "_doc",<br>
"version": "7.12.0"<br>
&#125;,<br>
"agent": &#123;<br>
"hostname": "node-03",<br>
"ephemeral_id": "c0f94fc0-b128-4eb9-b9a3-387f4cae44b7",<br>
"id": "f9cf0cd4-eccf-4d8b-bd24-2bff25b4083b",<br>
"name": "node-03",<br>
"type": "filebeat",<br>
"version": "7.12.0"<br>
&#125;,<br>
"ecs": &#123;<br>
"version": "1.8.0"<br>
&#125;,<br>
"stream": "stdout",<br>
"input": &#123;<br>
"type": "container"<br>
&#125;,<br>
"host": &#123;<br>
"name": "node-03"<br>
&#125;,<br>
"container": &#123;<br>
"id": "6791d22d210507becd7306ead1eeda9a4c558b5ca0630ed5af4f8b1b220fb4a7",<br>
"runtime": "docker",<br>
"image": &#123;<br>
  "name": "nginx:1.10"<br>
&#125;<br>
&#125;,<br>
"kubernetes": &#123;<br>
"namespace": "default",<br>
"replicaset": &#123;<br>
  "name": "nginx-5b946576d4"<br>
&#125;,<br>
"labels": &#123;<br>
  "app": "nginx",<br>
  "pod-template-hash": "5b946576d4"<br>
&#125;,<br>
"container": &#123;<br>
  "name": "nginx",<br>
  "image": "nginx:1.10"<br>
&#125;,<br>
"deployment": &#123;<br>
  "name": "nginx"<br>
&#125;,<br>
"node": &#123;<br>
  "name": "node-03",<br>
  "uid": "4340750b-1bb4-4d61-a9aa-4715c7326988",<br>
  "labels": &#123;<br>
    "kubernetes_io/arch": "amd64",<br>
    "kubernetes_io/hostname": "node-03",<br>
    "kubernetes_io/os": "linux",<br>
    "beta_kubernetes_io/arch": "amd64",<br>
    "beta_kubernetes_io/os": "linux"<br>
  &#125;,<br>
  "hostname": "node-03"<br>
&#125;,<br>
"namespace_uid": "8d1dad4b-bea0-469d-9858-51147822de79",<br>
"pod": &#123;<br>
  "name": "nginx-5b946576d4-6kftk",<br>
  "uid": "cc8c943a-919c-4e15-9cde-05358b8588c1"<br>
&#125;<br>
&#125;,<br>
"log": &#123;<br>
"offset": 2039,<br>
"file": &#123;<br>
  "path": "/var/log/containers/nginx-5b946576d4-6kftk_default_nginx-6791d22d210507becd7306ead1eeda9a4c558b5ca0630ed5af4f8b1b220fb4a7.log"<br>
&#125;<br>
&#125;,<br>
"message": "2021-05-06 11:01:58 10.234.2.11 - - \"GET / HTTP/1.1\" 200 612 \"-\" \"curl/7.29.0\" \"-\"",<br>
"fields": &#123;<br>
"k8s": "cluster-dev",<br>
"namespace": "default",<br>
"env": "dev"<br>
&#125;<br>
&#125; <br>
</pre><br>
可以看到Kubernetes这个key的value有关于Pod的信息，还有Node的一些信息，还有namespace信息等，基本上关于Kubernetes的一些关键信息都包含了，非常的多和全。<br>
<br>但是，问题又来了，这一条日志信息有点太多了，有一半多不是我们想要的信息，所以，我们需要去掉一些对于我们没有用的字段。<br>
<br><strong>删除不必要的字段</strong><br>
<pre class="prettyprint">processors:<br>
- drop_fields:<br>
  #删除的多余字段<br>
  fields:<br>
    - host<br>
    - ecs<br>
    - log<br>
    - agent<br>
    - input<br>
    - stream<br>
    - container<br>
  ignore_missing: true<br>
</pre><br>
<strong>添加日志时间</strong><br>
<br>通过上面的日志信息，可以看到是没有单独的一个关于日志时间的字段的，虽然里面有一个<code class="prettyprint">@timestamp</code>，但不是北京时间，而我们要的是日志的时间，<code class="prettyprint">message</code>里面倒是有时间，但是怎么能把它取到并单独添加一个字段呢，这个时候就需要用到<code class="prettyprint">script</code>了，需要写一个js脚本来替换。<br>
<pre class="prettyprint">processors:<br>
- script:<br>
  lang: javascript<br>
  id: format_time<br>
  tag: enable<br>
  source: ><br>
    function process(event) &#123;<br>
        var str=event.Get("message");<br>
        var time=str.split(" ").slice(0, 2).join(" ");<br>
        event.Put("time", time);<br>
    &#125;<br>
- timestamp:<br>
  field: time<br>
  timezone: Asia/Shanghai<br>
  layouts:<br>
    - '2006-01-02 15:04:05'<br>
    - '2006-01-02 15:04:05.999'<br>
  test:<br>
    - '2019-06-22 16:33:51'<br>
</pre><br>
添加完成后，会多一个<code class="prettyprint">time</code>的字段，在后面使用的时候，就可以使用这个字段了。<br>
<pre class="prettyprint">&#123;<br>
"@timestamp": "2021-05-06T04:32:10.560Z",<br>
"@metadata": &#123;<br>
"beat": "filebeat",<br>
"type": "_doc",<br>
"version": "7.12.0"<br>
&#125;,<br>
"message": "2021-05-06 11:32:10 10.234.2.11 - - \"GET / HTTP/1.1\" 200 612 \"-\" \"curl/7.29.0\" \"-\"",<br>
"fields": &#123;<br>
"k8s": "cluster-dev",<br>
"namespace": "default",<br>
"env": "dev"<br>
&#125;,<br>
"time": "2021-05-06 11:32:10",<br>
"kubernetes": &#123;<br>
"replicaset": &#123;<br>
  "name": "nginx-deployment-6c4b886b"<br>
&#125;,<br>
"labels": &#123;<br>
  "app": "nginx-deployment",<br>
  "pod-template-hash": "6c4b886b"<br>
&#125;,<br>
"container": &#123;<br>
  "name": "nginx",<br>
  "image": "nginx:1.19.5"<br>
&#125;,<br>
"deployment": &#123;<br>
  "name": "nginx-deployment"<br>
&#125;,<br>
"node": &#123;<br>
  "uid": "07d8a1a4-e10f-4331-adf0-2fd7d5817c2d",<br>
  "labels": &#123;<br>
    "beta_kubernetes_io/os": "linux",<br>
    "kubernetes_io/arch": "amd64",<br>
    "kubernetes_io/hostname": "node-02",<br>
    "kubernetes_io/os": "linux",<br>
    "beta_kubernetes_io/arch": "amd64"<br>
  &#125;,<br>
  "hostname": "node-02",<br>
  "name": "node-02"<br>
&#125;,<br>
"namespace_uid": "8d1dad4b-bea0-469d-9858-51147822de79",<br>
"pod": &#123;<br>
  "name": "nginx-deployment-6c4b886b-6rbhw",<br>
  "uid": "78a28548-3d34-4df6-9a76-c651b39ff934"<br>
&#125;,<br>
"namespace": "default"<br>
&#125;<br>
&#125; <br>
</pre><br>
<strong>优化Kubernetes数据信息结构</strong><br>
<br>这里单独创建了一个字段<code class="prettyprint">k8s</code>，字段里包含：<code class="prettyprint">podName</code>，<code class="prettyprint">nameSpace</code>，<code class="prettyprint">imageAddr</code>，<code class="prettyprint">hostName</code>等关键信息，最后再把<code class="prettyprint">Kubernetes</code>这个字段drop掉就可以了。最终结果如下：<br>
<pre class="prettyprint">processors:<br>
- script:<br>
  lang: javascript<br>
  id: format_k8s<br>
  tag: enable<br>
  source: ><br>
    function process(event) &#123;<br>
        var k8s=event.Get("kubernetes");<br>
        var newK8s = &#123;<br>
            podName: k8s.pod.name,<br>
            nameSpace: k8s.namespace,<br>
            imageAddr: k8s.container.name,<br>
            hostName: k8s.node.hostname<br>
        &#125;<br>
        event.Put("k8s", newK8s);<br>
    &#125; <br>
</pre><br>
日志：<br>
<pre class="prettyprint">&#123;<br>
"@timestamp": "2021-05-06T05:33:25.351Z",<br>
"@metadata": &#123;<br>
"beat": "filebeat",<br>
"type": "_doc",<br>
"version": "7.12.0"<br>
&#125;,<br>
"fields": &#123;<br>
"k8s": "cluster-dev",<br>
"namespace": "default",<br>
"env": "dev"<br>
&#125;,<br>
"k8s": &#123;<br>
"hostName": "node-02",<br>
"podName": "nginx-deployment-6c4b886b-6rbhw",<br>
"nameSpace": "default",<br>
"imageAddr": "nginx"<br>
&#125;,<br>
"message": "06/May/2021:05:33:25 +0000 10.234.2.11 - - \"GET / HTTP/1.1\" 200 612 \"-\" \"curl/7.29.0\" \"-\""<br>
&#125; <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210810/1518571e2e1f90acb71a9570f8908731.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210810/1518571e2e1f90acb71a9570f8908731.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
原文链接：<a href="https://juejin.cn/post/6974581299881181220" rel="nofollow" target="_blank">https://juejin.cn/post/6974581299881181220</a>，作者：王骁
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            