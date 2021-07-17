
---
title: '如何用Loki来分析Kubernetes事件'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/c85000e65761a21f370fc58681a66908.jpg'
author: Dockone
comments: false
date: 2021-07-17 13:12:10
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/c85000e65761a21f370fc58681a66908.jpg'
---

<div>   
<br>在Kubernetes API的众多对象中，Events算是最容易被我们忽视的类型之一。与其他对象相比，Event的活动量很大，不太可能长时间存储在etcd中，默认情况下，Event留存时间也只有1小时。当我们使用<code class="prettyprint">kubectl describe</code>获取一个对象时，可能因时间超限而无法获取它的历史事件，这对集群的使用者非常的不友好。除了能查看集群事件外，我们可能还有类似追踪一些特定的Warning事件（如Pod生命周期、副本集或worker节点状态）来进行相关告警的需求。那么在开启本期话题之前，我们先来理解下Kubernetes Events的结构，下述是官访问给出的几个重要字段解释：<br>
<ul><li><strong>Message</strong>：A human-readable description of the status of this operation</li><li><strong>Involved Object</strong>：The object that the event is about, like Pod, Deployment, Node, etc.</li><li><strong>Reason</strong>：Short, machine-understandable string – in other words, Enum</li><li><strong>Source</strong>：The component reporting this event; a short, machine-understandable string, i.e., kube-scheduler</li><li><strong>Type</strong>：Currently holds only Normal & Warning, but custom types can be given if desired.</li><li><strong>Count</strong>：The number of times the event has occurred</li></ul><br>
<br>对于这些事件，我们期望能有一个采集工具将信息输出到一个持久化的地方进行存储和分析。在以往，通常我们将Kubernetes的事件输出到Elasticsearch进行索引分析。<br>
<br>既然本文讨论的是以Loki来分析Kubernes的事件，那我们对于事件的处理基本按照如下流程：<br>
<pre class="prettyprint">kubernetes-api --> event-exporter --> fluentd --> loki --> grafana  <br>
</pre><br>
目前能够采集Kubernetes Events的开源组件主要以阿里云开源的Kube-eventer和Opsgenie开源的kubernetes-event-exporter为主（KubeSphere也有一个kube-events，不过需要配合其它组件的CRD使用，所以不在讨论范围之中）。<br>
<br>当事件进入到Loki后，就可以通过LogQL v2语句在Grafana上进行可视化查询，比如我们可以让Kubernetes中的事件按照等级、类型分类统计展示。通过Dashboard可以快速看到集群当前的的一些异常情况。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/c85000e65761a21f370fc58681a66908.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/c85000e65761a21f370fc58681a66908.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/d3206f3d9ba48cbd481f0d7f4eaf219b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/d3206f3d9ba48cbd481f0d7f4eaf219b.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>kubernetes-event-exporter</h3>首先需要部署kubernetes-event-exporter，它会将集群的事件打印到<code class="prettyprint">容器stdout当中</code>以方便日志采集。<br>
<pre class="prettyprint">apiVersion: v1  <br>
kind: ServiceAccount  <br>
metadata:  <br>
name: event-exporter  <br>
namespace: kube-system  <br>
---  <br>
apiVersion: rbac.authorization.k8s.io/v1  <br>
kind: ClusterRoleBinding  <br>
metadata:  <br>
name: event-exporter  <br>
roleRef:  <br>
apiGroup: rbac.authorization.k8s.io  <br>
kind: ClusterRole  <br>
name: view  <br>
subjects:  <br>
- kind: ServiceAccount  <br>
namespace: kube-system  <br>
name: event-exporter  <br>
---  <br>
apiVersion: v1  <br>
kind: ConfigMap  <br>
metadata:  <br>
name: event-exporter-cfg  <br>
namespace: kube-system  <br>
data:  <br>
config.yaml: |  <br>
logLevel: error  <br>
logFormat: json  <br>
route:  <br>
  routes:  <br>
    - match:  <br>
        - receiver: "dump"  <br>
receivers:  <br>
  - name: "dump"  <br>
    file:  <br>
      path: "/dev/stdout"  <br>
---  <br>
apiVersion: apps/v1  <br>
kind: Deployment  <br>
metadata:  <br>
name: event-exporter  <br>
namespace: kube-system  <br>
spec:  <br>
replicas: 1  <br>
template:  <br>
metadata:  <br>
  labels:  <br>
    app: event-exporter  <br>
    version: v1  <br>
spec:  <br>
  serviceAccountName: event-exporter  <br>
  containers:  <br>
    - name: event-exporter  <br>
      image: opsgenie/kubernetes-event-exporter:0.9  <br>
      imagePullPolicy: IfNotPresent  <br>
      args:  <br>
        - -conf=/data/config.yaml  <br>
      volumeMounts:  <br>
        - mountPath: /data  <br>
          name: cfg  <br>
  volumes:  <br>
    - name: cfg  <br>
      configMap:  <br>
        name: event-exporter-cfg  <br>
selector:  <br>
matchLabels:  <br>
  app: event-exporter  <br>
  version: v1  <br>
</pre><br>
当容器完全运行之后，通过kubectl logs可以看到event-exporter容器会以json格式打印的集群事件了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/57b21dd9c432e5fbc74a425595aed10b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/57b21dd9c432e5fbc74a425595aed10b.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
通常运行在Kubernetes之上Fluentd和FluentBit默认会采集容器的日志，我们需要做的是将这些内容发送给Loki。<br>
<br>最终我们可以在Dagger上查询Kubernetes事件的写入情况。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/9fd71bdcde3af6aa65a69e35f32cc33d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/9fd71bdcde3af6aa65a69e35f32cc33d.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>扩展Node Problem Detector</h3>Kubernetes中关于Node的事件不多，对于节点上更多偏向底层的状态（如内核死锁、容器运行时无响应等）并不能通过事件的方式通知出来。<strong>Node Problem Detector</strong>作为一个很好的补充，它可以将node上更细节的事件以<code class="prettyprint">NodeCondition</code>和<code class="prettyprint">Event</code>方式上报给Kubernetes。<br>
<br>安装<strong>Node Problem Detector</strong>非常简单，只需要通过helm的两条命令即可完成。<br>
<pre class="prettyprint">helm repo add deliveryhero https://charts.deliveryhero.io/  <br>
helm install deliveryhero/node-problem-detector  <br>
</pre><br>
<strong>Node Problem Detector</strong>支持用户运行自定义脚本来构造事件，本文中的Node Problem Detector除了默认的配置外，还有关于定义的网络监控脚步来做node节点上Conntrack的检查。<br>
<pre class="prettyprint">apiVersion: v1  <br>
kind: ConfigMap  <br>
metadata:  <br>
name: node-problem-detector-config  <br>
namespace: kube-system  <br>
data:  <br>
network_problem.sh: |  <br>
#!/bin/bash  <br>
readonly OK=0  <br>
readonly NONOK=1  <br>
readonly UNKNOWN=2  <br>
<br>
readonly NF_CT_COUNT_PATH='/proc/sys/net/netfilter/nf_conntrack_count'  <br>
readonly NF_CT_MAX_PATH='/proc/sys/net/netfilter/nf_conntrack_max'  <br>
readonly IP_CT_COUNT_PATH='/proc/sys/net/ipv4/netfilter/ip_conntrack_count'  <br>
readonly IP_CT_MAX_PATH='/proc/sys/net/ipv4/netfilter/ip_conntrack_max'  <br>
<br>
if [[ -f $NF_CT_COUNT_PATH ]] && [[ -f $NF_CT_MAX_PATH ]]; then  <br>
  readonly CT_COUNT_PATH=$NF_CT_COUNT_PATH  <br>
  readonly CT_MAX_PATH=$NF_CT_MAX_PATH  <br>
elif [[ -f $IP_CT_COUNT_PATH ]] && [[ -f $IP_CT_MAX_PATH ]]; then  <br>
  readonly CT_COUNT_PATH=$IP_CT_COUNT_PATH  <br>
  readonly CT_MAX_PATH=$IP_CT_MAX_PATH  <br>
else  <br>
  exit $UNKNOWN  <br>
fi  <br>
<br>
readonly conntrack_count=$(< $CT_COUNT_PATH) || exit $UNKNOWN  <br>
readonly conntrack_max=$(< $CT_MAX_PATH) || exit $UNKNOWN  <br>
readonly conntrack_usage_msg="$&#123;conntrack_count&#125; out of $&#123;conntrack_max&#125;"  <br>
<br>
if (( conntrack_count > conntrack_max * 9 /10 )); then  <br>
  echo "Conntrack table usage over 90%: $&#123;conntrack_usage_msg&#125;"  <br>
  exit $NONOK  <br>
else  <br>
  echo "Conntrack table usage: $&#123;conntrack_usage_msg&#125;"  <br>
  exit $OK  <br>
fi  <br>
network-problem-monitor.json: |  <br>
&#123;  <br>
    "plugin": "custom",  <br>
    "pluginConfig": &#123;  <br>
        "invoke_interval": "30s",  <br>
        "timeout": "5s",  <br>
        "max_output_length": 80,  <br>
        "concurrency": 3  <br>
    &#125;,  <br>
    "source": "network-plugin-monitor",  <br>
    "metricsReporting": true,  <br>
    "conditions": [],  <br>
    "rules": [  <br>
        &#123;  <br>
            "type": "temporary",  <br>
            "reason": "ConntrackFull",  <br>
            "path": "/config/network_problem.sh",  <br>
            "timeout": "5s"  <br>
        &#125;  <br>
    ]  <br>
&#125;  <br>
...  <br>
</pre><br>
再编辑node-problem-detector的DaemonSet文件，将如下的自定义的脚本和规则内容引入。<br>
<pre class="prettyprint">...  <br>
  containers:  <br>
  - name: node-problem-detector  <br>
    command:  <br>
    - /node-problem-detector  <br>
    - --logtostderr  <br>
    - --config.system-log-monitor=/config/kernel-monitor.json,/config/docker-monitor.json  <br>
    - --config.custom-plugin-monitor=/config/network-problem-monitor.json  <br>
    - --prometheus-address=0.0.0.0  <br>
    - --prometheus-port=20258  <br>
    - --k8s-exporter-heartbeat-period=5m0s  <br>
...  <br>
  volumes:  <br>
  - name: config  <br>
    configMap:  <br>
      defaultMode: 0777  <br>
      name: node-problem-detector-config  <br>
      items:  <br>
      - key: kernel-monitor.json  <br>
        path: kernel-monitor.json  <br>
      - key: docker-monitor.json  <br>
        path: docker-monitor.json  <br>
      - key: network-problem-monitor.json  <br>
        path: network-problem-monitor.json  <br>
      - key: network_problem.sh  <br>
        path: network_problem.sh  <br>
</pre><br>
<h3>Grafana分析面板</h3>小白已经将基于Loki的Kubernetes事件分析面板贡献在了Grafana Lab上面，我们可以访问如下网站下载Dashboard。<br>
<br><a href="https://grafana.com/grafana/dashboards/14003" rel="nofollow" target="_blank">https://grafana.com/grafana/dashboards/14003</a><br>
<br>当将面板导入到Grafana之后，我们需要修改Panel的log查询语句，将&#123;job="kubernetes-event-exporter"&#125;替换为自己exporter的标签。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/821f44fa84a0fbd1ef33652360ebfc10.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/821f44fa84a0fbd1ef33652360ebfc10.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
之后，我们就可以得到如下的分析面板<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/ae247efef448104812718e377abf9b6e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/ae247efef448104812718e377abf9b6e.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
怎么样，是不是心动的感觉。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/I92YtuKXpeGX3mAuJotrpg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/I92YtuKXpeGX3mAuJotrpg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            