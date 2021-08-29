
---
title: 'Kubernetes故障检测和自愈工具NPD'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/315b3965009050efcf97f106a17b8c35.jpg'
author: Dockone
comments: false
date: 2021-08-29 14:07:01
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/315b3965009050efcf97f106a17b8c35.jpg'
---

<div>   
<br>节点问题检测器（Node Problem Detector）是一个守护程序，用于监视和报告节点的健康状况（包括内核死锁、OOM、系统线程数压力、系统文件描述符压力等指标）。 你可以将节点问题探测器以 DaemonSet 或独立守护程序运行。 节点问题检测器从各种守护进程收集节点问题，并以<a href="https://kubernetes.io/zh/docs/concepts/architecture/nodes/#condition">NodeCondition</a>和<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#event-v1-core">Event</a>的形式报告给API Server。  <br>
<br>您可以通过检测相应的指标，提前预知节点的资源压力，可以在节点开始驱逐Pod之前手动释放或扩容节点资源压力，防止Kubernetes进行资源回收或节点不可用可能带来的损失。<br>
<br>Git仓库地址：<a href="https://github.com/kubernetes/node-problem-detector" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... ector</a><br>
<h3>Kubernetes 目前问题</h3><ul><li>基础架构守护程序问题：NTP服务关闭</li><li>硬件问题：CPU，内存或磁盘损坏</li><li>内核问题：内核死锁，文件系统损坏</li><li>容器运行时问题：运行时守护程序无响应</li><li>……</li></ul><br>
<br>当Kubernetes中节点发生上述问题，在整个集群中，Kubernetes服务组件并不会感知以上问题，就会导致Pod仍会调度至问题节点。<br>
<br>为了解决这个问题，我们引入了这个新的守护进程node-problem-detector，从各个守护进程收集节点问题，并使它们对上游层可见。一旦上游层面发现了这些问题，我们就可以讨论补救措施。<br>
<h3>NPD使用</h3><h4>构建</h4>NPD使用Go modules管理依赖，因此构建它需要Go SDK 1.11+：<br>
<pre class="prettyprint">cd $GOPATH/src/k8s.io<br>
go get k8s.io/node-problem-detector<br>
cd node-problem-detector<br>
<br>
export GO111MODULE=on <br>
go mod vendor<br>
<br>
# 设置构建标记<br>
export BUILD_TAGS="disable_custom_plugin_monitor disable_system_stats_monitor"<br>
<br>
# 在Ubuntu 14.04上需要安装<br>
sudo apt install libsystemd-journal-dev<br>
make all<br>
</pre><br>
<h4>安装</h4><pre class="prettyprint"># add repo<br>
helm repo add feisky https://feisky.xyz/kubernetes-charts<br>
helm update<br>
<br>
# install packages<br>
helm install feisky/node-problem-detector --namespace kube-system --name npd<br>
</pre><br>
<h4>启动参数</h4><ul><li>--version：在控制台打印NPD的版本号</li><li>--hostname-override：供NPD使用的自定义的节点名称，NPD会优先获取该参数设置的节点名称，其次是从NODE_NAME环境变量中获取，最后从os.Hostname()方法获取。</li></ul><br>
<br><strong>system-log-monitor相关参数</strong><br>
<ul><li>--config.system-log-monitor: system log monitor配置文件路径，多个文件用逗号分隔，如<a href="https://github.com/kubernetes/node-problem-detector/blob/master/config/system-stats-monitor.json">config/kernel-monitor.json</a>，NPD会为每一个配置文件生成单独的log monitor。你可以使用不同的log monitors来监控不同的系统日志。</li></ul><br>
<br><strong>system-stats-monitor相关参数</strong><br>
<ul><li>--config.system-stats-monitor: system status monitor配置文件路径，多个文件用逗号分隔，如<a href="https://github.com/kubernetes/node-problem-detector/blob/master/config/custom-plugin-monitor.json">config/system-stats-monitor.json</a>，NPD会为每一个配置文件生成单独的status monitor。你可以使用不同的status monitors来监控系统的不同状态。</li></ul><br>
<br><strong>custom-plugin-monitor相关参数</strong><br>
<ul><li>--config.custom-plugin-monitor：用户自定义插件配置文件路径，多个文件用逗号分隔，如<a href="https://github.com/kubernetes/node-problem-detector/blob/master/config/custom-plugin-monitor.json">config/custom-plugin-monitor.json</a>，NPD会为每一个配置文件生成单独的自定义插件监视器。你可以使用不同的自定义插件监视器来监控不同的系统问题。</li></ul><br>
<br><strong>Kubernetes exporter相关参数</strong><br>
<ul><li>--enable-k8s-exporter：是否开启上报信息到API Server，默认为true</li><li><br>--apiserver-override：一个URI参数，用于自定义node-problem-detector连接apiserver的地址。如果--enable-k8s-exporter为false，则忽略此内容。格式与Heapster的源标志相同。例如，要在没有身份验证的情况下运行，请使用以下配置：<a href="http://APISERVER_IP:APISERVER_PORT?inClusterConfig=false" rel="nofollow" target="_blank">http://APISERVER_IP:APISERVER_ ... false</a><br>
<br>请参阅<a href="https://github.com/kubernetes-retired/heapster/blob/master/docs/source-configuration.md#kubernetes">heapster</a>文档以获取可用选项的完整列表。</li><li><br>--address：绑定NPD服务器的地址。</li><li>--port：NPD服务端口，如果为0，表示禁用NPD服务。</li></ul><br>
<br><strong>Prometheus exporter相关参数</strong><br>
<ul><li>--prometheus-address：绑定Prometheus抓取端点的地址，默认为127.0.0.1</li><li>--prometheus-port：绑定Prometheus抓取端点的端口，默认为20257，使用0禁用</li></ul><br>
<br><strong>Stackdriver exporter相关参数</strong><br>
<ul><li>--exporter.stackdriver：Stackdriver exporter程序配置文件的路径，例如：<a href="https://github.com/kubernetes/node-problem-detector/blob/master/config/exporter/stackdriver-exporter.json">config/exporter/stackdriver-exporter.json</a>，默认为空字符串。 设置为空字符串以禁用。</li></ul><br>
<br><strong>过期参数</strong><br>
<ul><li>--system-log-monitors：system log monitor配置文件路径，多个文件用逗号分隔。该选项已过期，被--config.system-log-monitor取代，即将被移除。如果在启动NPD时同时设置了--system-log-monitors和--config.system-log-monitor，会引发panic。</li><li>--custom-plugin-monitors：用户自定义插件配置文件路径，多个文件用逗号分隔。该选项已过期，被--config.custom-plugin-monitor取代，即将被移除。如果在启动NPD时同时设置了--custom-plugin-monitors和--config.custom-plugin-monitor，会引发panic。</li></ul><br>
<br><h4>覆盖配置文件</h4>构建节点问题检测器的Docker镜像时，会嵌入<a href="https://github.com/kubernetes/node-problem-detector/tree/v0.1/config">默认配置</a>。<br>
<br>不过，你可以像下面这样使用ConfigMap将其覆盖：<br>
<br>1、更改 config/ 中的配置文件<br>
<br>2、创建ConfigMap node-strick-detector-config：<br>
<pre class="prettyprint">kubectl create configmap node-problem-detector-config --from-file=config/<br>
</pre><br>
3、更改node-problem-detector.yaml以使用ConfigMap：<br>
<pre class="prettyprint">apiVersion: apps/v1<br>
kind: DaemonSet<br>
metadata:<br>
name: node-problem-detector-v0.1<br>
namespace: kube-system<br>
labels:<br>
k8s-app: node-problem-detector<br>
version: v0.1<br>
kubernetes.io/cluster-service: "true"<br>
spec:<br>
selector:<br>
matchLabels:<br>
  k8s-app: node-problem-detector  <br>
  version: v0.1<br>
  kubernetes.io/cluster-service: "true"<br>
template:<br>
metadata:<br>
  labels:<br>
    k8s-app: node-problem-detector<br>
    version: v0.1<br>
    kubernetes.io/cluster-service: "true"<br>
spec:<br>
  hostNetwork: true<br>
  containers:<br>
  - name: node-problem-detector<br>
    image: k8s.gcr.io/node-problem-detector:v0.1<br>
    securityContext:<br>
      privileged: true<br>
    resources:<br>
      limits:<br>
        cpu: "200m"<br>
        memory: "100Mi"<br>
      requests:<br>
        cpu: "20m"<br>
        memory: "20Mi"<br>
    volumeMounts:<br>
    - name: log<br>
      mountPath: /log<br>
      readOnly: true<br>
    - name: config # Overwrite the config/ directory with ConfigMap volume<br>
      mountPath: /config<br>
      readOnly: true<br>
  volumes:<br>
  - name: log<br>
    hostPath:<br>
      path: /var/log/<br>
  - name: config # Define ConfigMap volume<br>
    configMap:<br>
      name: node-problem-detector-config<br>
</pre><br>
4、使用新的配置文件重新创建节点问题检测器：<br>
<br><strong>说明</strong>：此方法仅适用于通过kubectl启动的节点问题检测器。<br>
<br>如果节点问题检测器作为集群插件运行，则不支持覆盖配置。 插件管理器不支持ConfigMap。<br>
<h4>如何验证NPD捕获信息</h4>通常这些错误是比较难真实测试，只能通过发送消息到Journal来模拟。<br>
<br>1、发送一个kernel deadlock类型的condition：在对应的Node节点上执行以下操作<br>
<pre class="prettyprint">echo "task docker:7 blocked for more than 300 seconds." |systemd-cat -t kernel<br>
</pre><br>
然后通过Kubernetes控制台，你可以看到对应的信息：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210827/315b3965009050efcf97f106a17b8c35.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/315b3965009050efcf97f106a17b8c35.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
2、发送一个event<br>
<pre class="prettyprint">echo "Error trying v2 registry: failed to register layer: rename /var/lib/docker/image/test /var/lib/docker/image/ddd: directory not empty.*" |systemd-cat -t docker<br>
</pre><br>
然后通过以下命令来对应的event<br>
<pre class="prettyprint">kubectl describe node/xxxx<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210827/9816615f2a153e0d65239227e4acd3dd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/9816615f2a153e0d65239227e4acd3dd.png" class="img-polaroid" title="1.1_.png" alt="1.1_.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>实现原理</h3><h4>核心组件</h4><strong>Problem Daemon（Monitor）</strong><br>
<br>Problem Daemon是监控任务子守护进程，NPD会为每一个Problem Daemon配置文件创建一个守护进程，这些配置文件通过--config.custom-plugin-monitor、--config.system-log-monitor、--config.system-stats-monitor参数指定。每个Problem Daemon监控一个特定类型的节点故障，并报告给NPD。目前Problem Daemon以Goroutine的形式运行在NPD中，未来会支持在独立进程（容器）中运行并编排为一个Pod。在编译期间，可以通过相应的标记禁用每一类Problem Daemon。<br>
<ul><li>custom-plugin-monitor：用户自定义的Problem Daemon</li><li>system-log-monitor：系统日志监控</li><li>system-stats-monitor：系统状态监控</li></ul><br>
<br><strong>ProblemDaemonHandler</strong><br>
<br>ProblemDaemonHandler定义了Problem Daemon的初始化方法。<br>
<pre class="prettyprint">type ProblemDaemonHandler struct &#123;<br>
// 初始化 Problem Daemon实例，如果初始化过程中出错，则抛出 panic<br>
CreateProblemDaemonOrDie func(string) Monitor<br>
// 说明了从命令行参数配置 Problem Daemon 的方式<br>
CmdOptionDescription string<br>
&#125; <br>
</pre><br>
在NPD启动时，init()方法中完成了ProblemDaemonHandler的注册：<br>
<pre class="prettyprint">var (<br>
// 在NPD启动过程中，通过init()方法注册<br>
handlers = make(map[types.ProblemDaemonType]types.ProblemDaemonHandler)<br>
)<br>
<br>
// 注册Problem Daemon工厂方法，将会用于创建Problem Daemon<br>
func Register(problemDaemonType types.ProblemDaemonType, handler types.ProblemDaemonHandler) &#123;<br>
handlers[problemDaemonType] = handler<br>
&#125; <br>
</pre><br>
<strong>Exporter</strong><br>
<br>Exporter用于上报节点健康信息到某种控制面。在NPD启动时，会根据需求初始化并启动各种Exporter。Exporter分为三类：<br>
<ul><li>Kubernetes Exporter：会将节点健康信息上报到API Server。</li><li>Prometheus Exporter：负责上报节点指标信息到Prometheus。</li><li>Plugable Exporters：可插拔的Exporter（如Stackdriver Exporter），我们也可以自定义Exporter，并在init()方法中注册，这样在NPD启动时就会自动初始化并启动。</li></ul><br>
<br>详见：<a href="https://km.sankuai.com/page/1072724542" rel="nofollow" target="_blank">https://km.sankuai.com/page/1072724542</a><br>
<br><strong>ExporterHandler</strong><br>
<br>ExporterHandler和ProblemDaemonHandler功能类似，其定义了Exporter的初始化方法。也是在NPD启动时，init()方法中完成了ExporterHandler的注册。<br>
<pre class="prettyprint">type ExporterHandler struct &#123;<br>
// CreateExporterOrDie initializes an exporter, panic if error occurs.<br>
CreateExporterOrDie func(CommandLineOptions) Exporter<br>
// CmdOptionDescription explains how to configure the exporter from command line arguments.<br>
Options CommandLineOptions<br>
&#125; <br>
</pre><br>
<strong>Condition Manager</strong><br>
<br>Kubernetes Exporter获取到的异常Condition信息会上报给Condition Manager，Condition Manager每秒检查Condition的变化，并同步到API Server的Node对象中。<br>
<br><strong>Problem Client</strong><br>
<br>Problem Client负责与API Server交互，并将巡检过程中生成的Events和Conditions上报给API Server。<br>
<pre class="prettyprint">type Client interface &#123;<br>
// 从API Server获取当前节点所有指定类型的Conditions<br>
GetConditions(conditionTypes []v1.NodeConditionType) ([]*v1.NodeCondition, error)<br>
// 调用API Server接口更新当前节点的Condition列表<br>
SetConditions(conditions []v1.NodeCondition) error<br>
// 上报Event信息到API Server<br>
Eventf(eventType string, source, reason, messageFmt string, args ...interface&#123;&#125;)<br>
// 从API Server获取当前node-problem-detector实例所在的节点信息<br>
GetNode() (*v1.Node, error)<br>
&#125; <br>
</pre><br>
<strong>Problem Detector</strong><br>
<br>Problem Detector是NPD的核心对象，它负责启动所有的<a href="https://km.sankuai.com/page/1072601362">Problem Daemon</a>（也可以叫做 Monitor），并利用channel收集Problem Daemon中发现的异常信息，然后将异常信息提交给<a href="https://km.sankuai.com/page/1072724542">Exporter</a>，Exporter负责将这些异常信息上报到指定的控制面（如API Server、Prometheus、<a href="https://www.infoq.cn/article/2018/05/stackdriver-kubernetes">Stackdriver</a>等）。<br>
<br>详见：<a href="https://km.sankuai.com/page/1074277220" rel="nofollow" target="_blank">https://km.sankuai.com/page/1074277220</a><br>
<br><strong>Status</strong><br>
<br>Status是Problem Daemon向Exporter上报的异常信息对象。<br>
<pre class="prettyprint">type Status struct &#123;<br>
// problem daemon 的名称<br>
Source string `json:"source"`<br>
// 临时的节点问题 —— 事件对象，如果此Status用于Condition更新则此字段可以为空<br>
// 从老到新排列在数组中<br>
Events []Event `json:"events"`<br>
// 永久的节点问题 —— NodeCondition。PD必须总是在此字段报告最新的Condition<br>
Conditions []Condition `json:"conditions"`<br>
&#125; <br>
</pre><br>
<strong>Tomb</strong><br>
<br>用于从外部控制协程的生命周期， 它的逻辑很简单，准备结束生命周期时：<br>
<ol><li>外部协作者发起一个通知</li><li>协作线程接收到通知，进行清理</li><li>清理完成后，协程反向通知外部协作者</li><li>外部协作者退出阻塞</li></ol><br>
<br><h4>启动过程</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210827/d97b345b660bf31d7b902b3598a7ce43.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/d97b345b660bf31d7b902b3598a7ce43.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>NPD启动过程</em><br>
<br>NPD启动过程完成的工作有：<br>
<ol><li>打印NPD版本号</li><li>设置节点名称，优先使用命令行中设置的节点名称，其次是环境变量NODE_NAME中的节点名称，最次是os.Hostname()</li><li>校验命令行参数的合法性</li><li>初始化Problem Daemons</li><li>初始化默认Exporters（包含Kubernetes Exporter、Prometheus Exporter）和可插拔Exporters（如Stackdriver Exporter）</li><li>使用Problem Daemons和Exporters构建Problem Detector，并启动</li></ol><br>
<br><h4>检测流程</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210827/4b3c9a63cdc94df38a372947bfd10ca6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/4b3c9a63cdc94df38a372947bfd10ca6.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>NPD检测流程</em><br>
<h4>节点自愈</h4>采集节点的健康状态是为了能够在业务Pod不可用之前提前发现节点异常，从而运维或开发人员可以对Docker、Kubelet或节点进行修复。在NPDPlus中，为了减轻运维人员的负担，提供了根据采集到的节点状态从而进行不同自愈动作的能力。集群管理员可以根据节点不同的状态配置相应的自愈能力，如重启Docker、重启Kubelet或重启CVM节点等。同时为了防止集群中的节点雪崩，在执行自愈动作之前做了严格的限流，防止节点大规模重启。同时为了防止集群中的节点雪崩，在执行自愈动作之前做了严格的限流。具体策略为：<br>
<ul><li>在同一时刻只允许集群中的一个节点进行自愈行为，并且两个自愈行为之间至少间隔1分钟。</li><li>当有新节点添加到集群中时，会给节点2分钟的容忍时间，防止由于节点刚刚添加到集群的不稳定性导致错误自愈。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210827/f94f05716d6268d14c97dbe7f8d20bef.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/f94f05716d6268d14c97dbe7f8d20bef.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>custom-plugin-monitor</h3>此Problem Daemon为NPD提供了一种插件化机制，允许基于任何语言来编写监控脚本，只需要这些脚本遵循NPD关于退出码和标准输出的规范。通过调用用户配置的脚本来检测各种节点问题。<br>
<br>脚本退出码：<br>
<ul><li>0：对于Evnet来说表示Normal，对于NodeCondition表示False</li><li>1：对于Evnet来说表示Warning，对于NodeCondition表示True</li></ul><br>
<br>脚本输出应该小于80字节，避免给etcd的存储造成压力。<br>
<br>使用标记禁用：disable_custom_plugin_monitor<br>
<h4>示例</h4><pre class="prettyprint">&#123;<br>
"plugin": "custom",  // 插件类型<br>
"pluginConfig": &#123; // 插件配置<br>
"invoke_interval": "10s", // 执行时间间隔<br>
"timeout": "3m", // 健康检查超时时间<br>
"max_output_length": 80,<br>
"concurrency": 1 // 并行度<br>
&#125;,<br>
"source": "health-checker", // 事件源<br>
"metricsReporting": true,  // 是否上报指标信息<br>
"conditions": [ // 发现异常后在Node中设置的Condition信息<br>
&#123;<br>
  "type": "KubeletUnhealthy",<br>
  "reason": "KubeletIsHealthy",<br>
  "message": "kubelet on the node is functioning properly"<br>
&#125;<br>
],<br>
"rules": [ // 巡检规则<br>
&#123;<br>
  "type": "permanent",<br>
  "condition": "KubeletUnhealthy",<br>
  "reason": "KubeletUnhealthy",<br>
  "path": "/home/kubernetes/bin/health-checker", // 二进制文件路径<br>
  "args": [ // 二进制文件启动参数<br>
    "--component=kubelet",<br>
    "--enable-repair=true",// 是否启用自愈，自愈会尝试重启组件<br>
    "--cooldown-time=1m", // 冷却时间，组件启动后的一段时间为冷却时间，冷却时间能如果发现异常，不会尝试自愈<br>
    "--loopback-time=0",// 要回溯的Journal日志的时间，如果为0，则从组件启动时间开始回溯<br>
    "--health-check-timeout=10s" // 健康检查超时时间<br>
  ],<br>
  "timeout": "3m" // 巡检超时时间<br>
&#125;<br>
]<br>
&#125; <br>
</pre><br>
<h4>Plugin</h4>Plugin是NPD或用户自定义的一些异常检查程序，可以用任意语言编写。custom-plugin-monitor在执行过程中会执行这些异常检测程序，并根据返回结果来判断是否存在异常。NPD提供了三个Plugin，分别是：<br>
<ul><li>health-check：检查kubelet、Docker、kube-proxy、CRI等进程是否健康。</li><li>log-counter：依赖的插件是journald，其作用是统计指定的Journal日志中近一段时间满足正则匹配的历史日志条数。</li><li>network_problem.sh：检查<a href="http://arthurchiao.art/blog/conntrack-design-and-implementation-zh/">conntrack table</a>的使用率是否超过90%。</li></ul><br>
<br><strong>health-checker</strong><br>
<br>命令行参数：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210827/f229813008ec7af7a04f58da5d05691a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/f229813008ec7af7a04f58da5d05691a.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
结构定义：<br>
<pre class="prettyprint">type healthChecker struct &#123;<br>
component       string // 要进行健康检查的组件名称，支持kubelet、docker、kube-proxy和CRI<br>
service         string // 组件的服务名称，需要通过Service读取Journal日志，并检查日志是否存在异常<br>
enableRepair    bool // 是否启动自动修复，如果启动自动修复，当发现异常时会调用repairFunc尝试自动修复<br>
healthCheckFunc func() (bool, error) // 组件健康检查方法<br>
repairFunc         func() // 组件自愈方法，这是一种“best-effort”形式的自愈，会尝试 kill 掉组件的进程，但可能失败<br>
uptimeFunc         func() (time.Duration, error)  // 获取组件的启动时间（启动后经过的时间）<br>
crictlPath         string // crictl二进制文件路径，用于对CRI（Container Runtime Interface）组件执行健康检查<br>
healthCheckTimeout time.Duration // 健康检查超时时间<br>
coolDownTime       time.Duration // 服务启动后，在冷却时间内如果发现异常，不会尝试自动修复。超出冷却时间后才会尝试自动修复<br>
loopBackTime       time.Duration // 待检Journal查日志的起始时间间隔，如果该值为0，则从组件启动的日志开始检查<br>
logPatternsToCheck map[string]int // 要检查的Journal日志的正则表达式<br>
&#125; <br>
</pre><br>
执行流程：<br>
<br>health-checker的执行流程可以分为三个步骤：<br>
<ol><li>调用 healthCheckFunc()方法判断组件进程是否健康</li><li>获取组件近一段时间的Journal日志，判断异常日志数量是否达到上限</li><li>如果前两步检查都未发现异常，则返回 true。否则，如果启动了自动修复机制，则调用repairFunc()尝试自愈</li></ol><br>
<br>健康检查：<br>
<pre class="prettyprint">func getHealthCheckFunc(hco *options.HealthCheckerOptions) func() (bool, error) &#123;<br>
switch hco.Component &#123;<br>
case types.KubeletComponent:<br>
  // 访问 http://127.0.0.1:10248/healthz，判断kubelet是否健康<br>
    return healthCheckEndpointOKFunc(types.KubeletHealthCheckEndpoint, hco.HealthCheckTimeout)<br>
case types.KubeProxyComponent:<br>
  // 访问http://127.0.0.1:10256/healthz，判断kube-proxy是否健康<br>
    return healthCheckEndpointOKFunc(types.KubeProxyHealthCheckEndpoint, hco.HealthCheckTimeout)<br>
case types.DockerComponent:<br>
    return func() (bool, error) &#123; // 执行docker ps命令判断Docker是否健康<br>
        if _, err := execCommand(hco.HealthCheckTimeout, getDockerPath(), "ps"); err != nil &#123;<br>
            return false, nil<br>
        &#125;<br>
        return true, nil<br>
    &#125;<br>
case types.CRIComponent:<br>
    return func() (bool, error) &#123;// 执行circtl --runtime-endpoint=unix:///var/run/containerd/containerd.sock --image-endpoint=unix:///var/run/containerd/containerd.sock<br>
        if _, err := execCommand(hco.HealthCheckTimeout, hco.CriCtlPath, "--runtime-endpoint="+hco.CriSocketPath, "--image-endpoint="+hco.CriSocketPath, "pods"); err != nil &#123;<br>
            return false, nil<br>
        &#125;<br>
        return true, nil<br>
    &#125;<br>
default:<br>
    glog.Warningf("Unsupported component: %v", hco.Component)<br>
&#125;<br>
<br>
return nil<br>
&#125; <br>
</pre><br>
组件自愈：<br>
<pre class="prettyprint">func getRepairFunc(hco *options.HealthCheckerOptions) func() &#123;<br>
switch hco.Component &#123;<br>
case types.DockerComponent:<br>
    // Use "docker ps" for docker health check. Not using crictl for docker to remove<br>
    // dependency on the kubelet.<br>
    return func() &#123;<br>
        execCommand(types.CmdTimeout, "pkill", "-SIGUSR1", "dockerd")<br>
        execCommand(types.CmdTimeout, "systemctl", "kill", "--kill-who=main", hco.Service)<br>
    &#125;<br>
default:<br>
    // Just kill the service for all other components<br>
    return func() &#123;<br>
        execCommand(types.CmdTimeout, "systemctl", "kill", "--kill-who=main", hco.Service)<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
<strong>log-counter</strong><br>
<br>依赖的插件是journald，其作用是统计指定的Journal日志中近一段时间满足正则匹配的历史日志条数。<br>
<br>命令行参数：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210827/3d9880ba0f04a043bd4ce72c7668e335.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/3d9880ba0f04a043bd4ce72c7668e335.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
执行流程：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210827/d471f18a3f001c4265dea6bb78e76a7d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/d471f18a3f001c4265dea6bb78e76a7d.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>log-counter执行流程</em><br>
<br>Count()：<br>
<pre class="prettyprint">func (e *logCounter) Count() (count int, err error) &#123;<br>
start := e.clock.Now()<br>
for &#123;<br>
    select &#123;<br>
    case log, ok := <-e.logCh:<br>
        if !ok &#123;<br>
            err = fmt.Errorf("log channel closed unexpectedly")<br>
            return<br>
        &#125;<br>
        // 只统计logCounter启动之前的日志<br>
        if start.Before(log.Timestamp) &#123;<br>
            return<br>
        &#125;<br>
        e.buffer.Push(log)<br>
        if len(e.buffer.Match(e.pattern)) != 0 &#123;<br>
            count++<br>
        &#125;<br>
    case <-e.clock.After(timeout):<br>
        // 如果超过一定时间没有新日志生成，则退出<br>
        return<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
Journal日志检查：<br>
<pre class="prettyprint">func checkForPattern(service, logStartTime, logPattern string, logCountThreshold int) (bool, error) &#123;<br>
// 从Journal日志中匹配符合规则的错误日志<br>
out, err := execCommand(types.CmdTimeout, "/bin/sh", "-c",<br>
    // Query service logs since the logStartTime<br>
    `journalctl --unit "`+service+`" --since "`+logStartTime+<br>
        // 正则匹配<br>
        `" | grep -i "`+logPattern+<br>
        // 计算错误发生次数<br>
        `" | wc -l`)<br>
if err != nil &#123;<br>
    return true, err<br>
&#125;<br>
occurrences, err := strconv.Atoi(out)<br>
if err != nil &#123;<br>
    return true, err<br>
&#125;<br>
// 如果错误日志数量超过阈值，则返回false<br>
if occurrences >= logCountThreshold &#123;<br>
    glog.Infof("%s failed log pattern check, %s occurrences: %v", service, logPattern, occurrences)<br>
    return false, nil<br>
&#125;<br>
return true, nil<br>
&#125; <br>
</pre><br>
<strong>network_problem.sh</strong><br>
<br>检查<a href="http://arthurchiao.art/blog/conntrack-design-and-implementation-zh/">conntrack table</a>的使用率是否超过90%。<br>
<pre class="prettyprint">#!/bin/bash<br>
<br>
# This plugin checks for common network issues.<br>
# Currently only checks if conntrack table is more than 90% used.<br>
<br>
readonly OK=0<br>
readonly NONOK=1<br>
readonly UNKNOWN=2<br>
<br>
# "nf_conntrack" replaces "ip_conntrack" - support both<br>
readonly NF_CT_COUNT_PATH='/proc/sys/net/netfilter/nf_conntrack_count'<br>
readonly NF_CT_MAX_PATH='/proc/sys/net/netfilter/nf_conntrack_max'<br>
readonly IP_CT_COUNT_PATH='/proc/sys/net/ipv4/netfilter/ip_conntrack_count'<br>
readonly IP_CT_MAX_PATH='/proc/sys/net/ipv4/netfilter/ip_conntrack_max'<br>
<br>
if [[ -f $NF_CT_COUNT_PATH ]] && [[ -f $NF_CT_MAX_PATH ]]; then<br>
readonly CT_COUNT_PATH=$NF_CT_COUNT_PATH<br>
readonly CT_MAX_PATH=$NF_CT_MAX_PATH<br>
elif [[ -f $IP_CT_COUNT_PATH ]] && [[ -f $IP_CT_MAX_PATH ]]; then<br>
readonly CT_COUNT_PATH=$IP_CT_COUNT_PATH<br>
readonly CT_MAX_PATH=$IP_CT_MAX_PATH<br>
else<br>
exit $UNKNOWN<br>
fi<br>
<br>
readonly conntrack_count=$(< $CT_COUNT_PATH) || exit $UNKNOWN<br>
readonly conntrack_max=$(< $CT_MAX_PATH) || exit $UNKNOWN<br>
readonly conntrack_usage_msg="$&#123;conntrack_count&#125; out of $&#123;conntrack_max&#125;"<br>
<br>
if (( conntrack_count > conntrack_max * 9 /10 )); then<br>
echo "Conntrack table usage over 90%: $&#123;conntrack_usage_msg&#125;"<br>
exit $NONOK<br>
else<br>
echo "Conntrack table usage: $&#123;conntrack_usage_msg&#125;"<br>
exit $OK<br>
fi <br>
</pre><br>
<h3>system-log-monitor</h3>system-log-monitor用于监控系统和内核日志，根据预定义规则来报告问题、指标。它支持基于文件的日志、journald、kmsg。要监控其它日志，需要实现LogWatcher接口。<br>
<h4>LogMonitor</h4><pre class="prettyprint">type logMonitor struct &#123;<br>
// 配置文件路径<br>
configPath string<br>
// 读取日志的逻辑委托给LogWatcher，这里解耦的目的是支持多种类型的日志<br>
watcher    watchertypes.LogWatcher<br>
// 日志缓冲，读取的日志在此等待处理<br>
buffer     LogBuffer<br>
// 对应配置文件中的字段<br>
config     MonitorConfig<br>
// 对应配置文件中的conditions字段<br>
conditions []types.Condition<br>
// 输入日志条目的通道<br>
logCh      <-chan *logtypes.Log<br>
// 输出状态的通道<br>
output     chan *types.Status<br>
// 用于控制此Monitor的生命周期<br>
tomb       *tomb.Tomb<br>
&#125; <br>
</pre><br>
<h4>LogWatcher</h4>LogWatcher的主要作用的监听文件更新，并将追加的文件内容写入LogBuffer中供LogMonitor处理。NPD中提供了三种LogWatcher的实现：<br>
<ul><li>filelog：监听任意文本类型日志。</li><li>journald：监听journald日志。</li><li>kmsg：监听内核日志设备，如/dev/kmsg。</li></ul><br>
<br>LogWatcher也需要在init()方法中完成注册。<br>
<pre class="prettyprint">type LogWatcher interface &#123;<br>
// 开始监控日志，并通过通道输出日志<br>
Watch() (<-chan *types.Log, error)<br>
// 停止，注意释放打开的资源<br>
Stop()<br>
&#125; <br>
</pre><br>
<strong>FileLog</strong><br>
<br>FileLog通过监控指定的文件更新，并对日志内容进行正则匹配，以发现异常日志，从而判断组件是否正常。<br>
<pre class="prettyprint">&#123;<br>
"plugin": "filelog",<br>
"pluginConfig": &#123;<br>
    "timestamp": "^time=\"(\\S*)\"",// 时间戳解析表达式<br>
    "message": "msg=\"([^\n]*)\"",  // 日志解析表达式<br>
    "timestampFormat": "2006-01-02T15:04:05.999999999-07:00" // 时间戳格式<br>
&#125;,<br>
"logPath": "/var/log/docker.log", // 日志路径<br>
"lookback": "5m", // 日志回溯时长<br>
"bufferSize": 10, // 缓冲大小（日志条数）<br>
"source": "docker-monitor",<br>
"conditions": [],<br>
"rules": [ // 健康检查规则<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "CorruptDockerImage",<br>
        "pattern": "Error trying v2 registry: failed to register layer: rename /var/lib/docker/image/(.+) /var/lib/docker/image/(.+): directory not empty.*"<br>
    &#125;<br>
]<br>
&#125; <br>
</pre><br>
<strong>journald</strong><br>
<br>journald底层依赖sdjournal包，监控系统日志的更新，并且可以从指定的历史时间点开始读取。如果未指定Journal日志路径，则从系统默认路径读取。读取到的日志会转换成logtypes.Log对象，并写入logCh通道中。Journal通过监控Journal文件更新，并对日志内容进行正则匹配，以发现异常日志，从而判断组件是否正常。<br>
<pre class="prettyprint">&#123;<br>
"plugin": "journald",<br>
"pluginConfig": &#123;<br>
    "source": "abrt-notification"<br>
&#125;,<br>
"logPath": "/var/log/journal", // Journal日志路径<br>
"lookback": "5m", // 日志回溯时长<br>
"bufferSize": 10, // log缓存大小（日志条数）<br>
"source": "abrt-adaptor",<br>
"conditions": [],<br>
"rules": [ // 健康检查规则<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "CCPPCrash",<br>
        "pattern": "Process \\d+ \\(\\S+\\) crashed in .*"<br>
    &#125;,<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "UncaughtException",<br>
        "pattern": "Process \\d+ \\(\\S+\\) of user \\d+ encountered an uncaught \\S+ exception"<br>
    &#125;,<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "XorgCrash",<br>
        "pattern": "Display server \\S+ crash in \\S+"<br>
    &#125;,<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "VMcore",<br>
        "pattern": "System encountered a fatal error in \\S+"<br>
    &#125;,<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "Kerneloops",<br>
        "pattern": "System encountered a non-fatal error in \\S+"<br>
    &#125;<br>
]<br>
&#125; <br>
</pre><br>
<strong>kmsg</strong><br>
<br>kmsg和journald的实现原理类似，它底层依赖kmsgparser包，实现内核日志的监控更新和回溯。默认的文件路径是/dev/kmsg。kmsg通过监控系统日志文件更新，并对日志内容进行正则匹配，以发现异常日志，从而判断组件是否正常。<br>
<pre class="prettyprint">&#123;<br>
"plugin": "kmsg",<br>
"logPath": "/dev/kmsg", // 内核日志路径<br>
"lookback": "5m",  // 日志回溯时长<br>
"bufferSize": 10,  // 缓存大小（日志条数）<br>
"source": "kernel-monitor",<br>
"metricsReporting": true,<br>
"conditions": [<br>
    &#123;<br>
        "type": "KernelDeadlock",<br>
        "reason": "KernelHasNoDeadlock",<br>
        "message": "kernel has no deadlock"<br>
    &#125;,<br>
    &#123;<br>
        "type": "ReadonlyFilesystem",<br>
        "reason": "FilesystemIsNotReadOnly",<br>
        "message": "Filesystem is not read-only"<br>
    &#125;<br>
],<br>
"rules": [<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "OOMKilling",<br>
        "pattern": "Killed process \\d+ (.+) total-vm:\\d+kB, anon-rss:\\d+kB, file-rss:\\d+kB.*"<br>
    &#125;,<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "TaskHung",<br>
        "pattern": "task [\\S ]+:\\w+ blocked for more than \\w+ seconds\\."<br>
    &#125;,<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "UnregisterNetDevice",<br>
        "pattern": "unregister_netdevice: waiting for \\w+ to become free. Usage count = \\d+"<br>
    &#125;,<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "KernelOops",<br>
        "pattern": "BUG: unable to handle kernel NULL pointer dereference at .*"<br>
    &#125;,<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "KernelOops",<br>
        "pattern": "divide error: 0000 \\[#\\d+\\] SMP"<br>
    &#125;,<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "Ext4Error",<br>
        "pattern": "EXT4-fs error .*"<br>
    &#125;,<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "Ext4Warning",<br>
        "pattern": "EXT4-fs warning .*"<br>
    &#125;,<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "IOError",<br>
        "pattern": "Buffer I/O error .*"<br>
    &#125;,<br>
    &#123;<br>
        "type": "temporary",<br>
        "reason": "MemoryReadError",<br>
        "pattern": "CE memory read error .*"<br>
    &#125;,<br>
    &#123;<br>
        "type": "permanent",<br>
        "condition": "KernelDeadlock",<br>
        "reason": "AUFSUmountHung",<br>
        "pattern": "task umount\\.aufs:\\w+ blocked for more than \\w+ seconds\\."<br>
    &#125;,<br>
    &#123;<br>
        "type": "permanent",<br>
        "condition": "KernelDeadlock",<br>
        "reason": "DockerHung",<br>
        "pattern": "task docker:\\w+ blocked for more than \\w+ seconds\\."<br>
    &#125;,<br>
    &#123;<br>
        "type": "permanent",<br>
        "condition": "ReadonlyFilesystem",<br>
        "reason": "FilesystemIsReadOnly",<br>
        "pattern": "Remounting filesystem read-only"<br>
    &#125;<br>
]<br>
&#125; <br>
</pre><br>
<h4>LogBuffer</h4>LogBuffer是一个可循环写入的日志队列，max字段控制可记录日志的最大条数，当日志条数超过max时，就会从头覆盖写入。LogBuffer也支持正则匹配buffer中的日志内容。<br>
<pre class="prettyprint">type LogBuffer interface &#123;<br>
// 把日志写入 log buffer 中<br>
Push(*types.Log)<br>
// 对 buffer 中的日志进行正则匹配<br>
Match(string) []*types.Log<br>
// 把 log buffer 中的日志按时间由远到近连接成一个字符串<br>
String() string<br>
&#125; <br>
</pre><br>
<h4>实现原理</h4><strong>启动过程</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210827/d7ec31378868d195bc3346502b1728e5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/d7ec31378868d195bc3346502b1728e5.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>执行过程</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210827/85cbf4d5d153aa16ee9ba79acc67dece.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/85cbf4d5d153aa16ee9ba79acc67dece.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>system-stats-monitor</h3>将各种健康相关的统计信息报告为Metrics。<br>
<br>目前支持的组件仅仅有主机信息、磁盘：<br>
<ul><li>disk/io_time设备队列非空时间，毫秒</li><li>disk/weighted_io设备队列非空时间加权，毫秒</li><li>disk/avg_queue_len上次调用插件以来，平均排队请求数</li></ul><br>
<br>使用标记禁用：disable_system_stats_monitor<br>
<ul><li>cpuCollector：采集CPU相关指标信息。</li><li>diskCollector：采集磁盘相关指标信息。</li><li>hostCollector：采集宿主机相关指标信息。</li><li>memoryCollector：采集内存相关指标信息。</li><li>osFeatureCollector：采集系统属性相关指标。</li><li>netCollector：采集网络相关指标信息。</li></ul><br>
<br><h3>检查规则</h3><h4>自定义插件规则</h4><strong>CustomRule</strong><br>
<pre class="prettyprint">// 自定义规则（插件），描述CPM如何调用插件，分析调用结果<br>
type CustomRule struct &#123;<br>
// 报告永久还是临时问题<br>
Type types.Type `json:"type"`<br>
// 此问题触发哪种NodeCondition，仅当永久问题才设置此字段<br>
Condition string `json:"condition"`<br>
// 问题的简短原因，对于永久问题，通常描述NodeCondition的一个子类型<br>
Reason string `json:"reason"`<br>
// 自定义插件（脚本）的文件路径<br>
Path string `json:"path"`<br>
// 传递给自定义插件的参数<br>
Args []string `json:"args"`<br>
// 自定义插件执行超时<br>
TimeoutString *string `json:"timeout"`<br>
Timeout *time.Duration `json:"-"`<br>
&#125; <br>
</pre><br>
示例：<a href="https://github.com/kubernetes/node-problem-detector/blob/master/config/health-checker-kubelet.json" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... .json</a><br>
<h4>系统日志监控规则</h4><strong>systemlogtypes.Rule</strong><br>
<pre class="prettyprint">type Rule struct &#123;<br>
// 报告永久还是临时问题<br>
Type types.Type `json:"type"`<br>
// 此问题触发哪种NodeCondition，仅当永久问题才设置此字段<br>
Condition string `json:"condition"`<br>
// 问题的简短原因，对于永久问题，通常描述NodeCondition的一个子类型<br>
Reason string `json:"reason"`<br>
// Pattern is the regular expression to match the problem in log.<br>
// Notice that the pattern must match to the end of the line.<br>
Pattern string `json:"pattern"`<br>
&#125; <br>
</pre><br>
示例：<a href="https://github.com/kubernetes/node-problem-detector/blob/master/config/kernel-monitor.json" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... .json</a><br>
<h3>异常上报</h3>node-problem-detector使用Event和NodeCondition将问题报告给apiserver。<br>
<ul><li>NodeCondition：导致节点无法处理于Pod生命周期的的永久性问题应报告为NodeCondition。</li><li>Event：对Pod影响有限的临时问题应作为event报告。</li></ul><br>
<br><h4>异常类型</h4><ul><li>temporary：致节点无法处理于Pod生命周期的的永久性问题</li><li>permanent：对Pod影响有限的临时问题</li></ul><br>
<br><h3>指标上报</h3>通过配置metricsReporting可以选择是否开启System Log Monitor的指标上报功能。该字段默认为true。<br>
<br>临时异常只会上报counter指标，如下：<br>
<pre class="prettyprint"># HELP problem_counter Number of times a specific type of problem have occurred.<br>
# TYPE problem_counter counter<br>
problem_counter&#123;reason="TaskHung"&#125; 2<br>
</pre><br>
永久异常会上报gauge指标和counter指标，如下：<br>
<pre class="prettyprint"># HELP problem_counter Number of times a specific type of problem have occurred.<br>
# TYPE problem_counter counter<br>
problem_counter&#123;reason="DockerHung"&#125; 1<br>
# HELP problem_gauge Whether a specific type of problem is affecting the node or not.<br>
# TYPE problem_gauge gauge<br>
problem_gauge&#123;condition="KernelDeadlock",reason="DockerHung"&#125; 1<br>
</pre><br>
Counter是一个累计类型的数据指标，它代表单调递增的计数器。<br>
<br>Gauge是可以任意上下波动数值的指标类型。<br>
<br><strong>指标</strong><br>
<br>NPD对指标这一概念也进行了封装，它依赖OpenCensus而不是Prometheus这样具体的实现的API。<br>
<br>所有指标如下：<br>
<pre class="prettyprint">const (<br>
CPURunnableTaskCountID  MetricID = "cpu/runnable_task_count"<br>
CPUUsageTimeID          MetricID = "cpu/usage_time"<br>
CPULoad1m               MetricID = "cpu/load_1m"<br>
CPULoad5m               MetricID = "cpu/load_5m"<br>
CPULoad15m              MetricID = "cpu/load_15m"<br>
ProblemCounterID        MetricID = "problem_counter"<br>
ProblemGaugeID          MetricID = "problem_gauge"<br>
DiskIOTimeID            MetricID = "disk/io_time"<br>
DiskWeightedIOID        MetricID = "disk/weighted_io"<br>
DiskAvgQueueLenID       MetricID = "disk/avg_queue_len"<br>
DiskOpsCountID          MetricID = "disk/operation_count"<br>
DiskMergedOpsCountID    MetricID = "disk/merged_operation_count"<br>
DiskOpsBytesID          MetricID = "disk/operation_bytes_count"<br>
DiskOpsTimeID           MetricID = "disk/operation_time"<br>
DiskBytesUsedID         MetricID = "disk/bytes_used"<br>
HostUptimeID            MetricID = "host/uptime"<br>
MemoryBytesUsedID       MetricID = "memory/bytes_used"<br>
MemoryAnonymousUsedID   MetricID = "memory/anonymous_used"<br>
MemoryPageCacheUsedID   MetricID = "memory/page_cache_used"<br>
MemoryUnevictableUsedID MetricID = "memory/unevictable_used"<br>
MemoryDirtyUsedID       MetricID = "memory/dirty_used"<br>
OSFeatureID             MetricID = "system/os_feature"<br>
SystemProcessesTotal    MetricID = "system/processes_total"<br>
SystemProcsRunning      MetricID = "system/procs_running"<br>
SystemProcsBlocked      MetricID = "system/procs_blocked"<br>
SystemInterruptsTotal   MetricID = "system/interrupts_total"<br>
SystemCPUStat           MetricID = "system/cpu_stat"<br>
NetDevRxBytes           MetricID = "net/rx_bytes"<br>
NetDevRxPackets         MetricID = "net/rx_packets"<br>
NetDevRxErrors          MetricID = "net/rx_errors"<br>
NetDevRxDropped         MetricID = "net/rx_dropped"<br>
NetDevRxFifo            MetricID = "net/rx_fifo"<br>
NetDevRxFrame           MetricID = "net/rx_frame"<br>
NetDevRxCompressed      MetricID = "net/rx_compressed"<br>
NetDevRxMulticast       MetricID = "net/rx_multicast"<br>
NetDevTxBytes           MetricID = "net/tx_bytes"<br>
NetDevTxPackets         MetricID = "net/tx_packets"<br>
NetDevTxErrors          MetricID = "net/tx_errors"<br>
NetDevTxDropped         MetricID = "net/tx_dropped"<br>
NetDevTxFifo            MetricID = "net/tx_fifo"<br>
NetDevTxCollisions      MetricID = "net/tx_collisions"<br>
NetDevTxCarrier         MetricID = "net/tx_carrier"<br>
NetDevTxCompressed      MetricID = "net/tx_compressed"<br>
)<br>
</pre><br>
其中ProblemCounterID和ProblemGaugeID是针对所有Problem的Counter/Gauge，其他都是SystemStatsMonitor暴露的指标。<br>
<h3>治愈系统</h3>在NPD的术语中，治愈系统（Remedy System）是一个或一组进程，负责分析NPD检测出的问题，并且采取补救措施，让Kubernetes集群恢复健康状态。<br>
<br>目前官方提及的治愈系统有只有Draino。NPD项目并没有提供对Draino的集成，你需要手工部署和配置Draino。<br>
<h4>Draino</h4><a href="https://github.com/planetlabs/draino">Draino</a>是Planet开源的小项目，最初在Planet用于解决GCE上运行的Kubernetes集群的持久卷相关进程（mkfs.ext4、mount等）永久卡死在不可中断睡眠状态的问题。Draino的工作方式简单粗暴，只是检测到NodeCondition并Cordon、Drain节点。<br>
<br>基于Label和NodeCondition自动的Drain掉故障Kubernetes节点：<br>
<ol><li>具有匹配标签的的Kubernetes节点，只要进入指定的NodeCondition之一，立即禁止调度（Cordoned）</li><li>在禁止调度之后一段时间，节点被Drain掉</li></ol><br>
<br>Draino可以联用Cluster Autoscaler，自动的终结掉Drained的节点。<br>
<br>在Descheduler项目成熟以后，可以代替Draino。<br>
<br>原文链接：<a href="https://www.jianshu.com/p/eeba98425307" rel="nofollow" target="_blank">https://www.jianshu.com/p/eeba98425307</a>，作者：王勇1024
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            