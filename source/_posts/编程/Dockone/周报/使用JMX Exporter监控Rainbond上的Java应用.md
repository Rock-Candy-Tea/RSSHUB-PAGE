
---
title: '使用JMX Exporter监控Rainbond上的Java应用'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://static.goodrain.com/wechat/app-monitor/create_jmx.png'
author: Dockone
comments: false
date: 2022-02-13 12:11:19
thumbnail: 'https://static.goodrain.com/wechat/app-monitor/create_jmx.png'
---

<div>   
<br><h2>场景</h2>Prometheus 社区开发了 JMX Exporter 用于导出 JVM 的监控指标，以便使用 Prometheus 来采集监控数据。当您的 Java 应用部署在Rainbond上后<br>
<br>可通过本文了解部署在 Rainbond 上的 Java 应用如何使用  JMX Exporter 暴露 JVM 监控指标。<br>
<br><h2>JMX Exporter 简介</h2>Java Management Extensions，JMX 是管理 Java 的一种扩展框架，JMX Exporter 基于此框架读取 JVM 的运行时状态。JMX Exporter 利用 Java 的 JMX 机制来读取 JVM 运行时的监控数据，然后将其转换为 Prometheus 可辨识的 metrics 格式，让 Prometheus 对其进行监控采集。<br>
<br>JMX Exporter 提供 <code class="prettyprint">启动独立进程</code> 及 <code class="prettyprint">JVM 进程内启动（in-process)</code>两种方式暴露 JVM 监控指标：<br>
<br><strong>启动独立进程</strong><br>
<br>JVM 启动时指定参数，暴露 JMX 的 RMI 接口。JMX Exporter 调用 RMI 获取 JVM 运行时状态数据，转换为 Prometheus metrics 格式，并暴露端口让 Prometheus 采集。<br>
<br><strong>JVM 进程内启动（in-process)</strong><br>
<br>JVM 启动时指定参数，通过 javaagent 的形式运行 JMX Exporter 的 jar 包，进程内读取 JVM 运行时状态数据，转换为 Prometheus metrics 格式，并暴露端口让 Prometheus 采集。<br>
<br><blockquote><br>官方不建议使用 <code class="prettyprint">启动独立进程</code> 方式，该方式配置复杂且需单独的进程，进程本身的监控又引发了新的问题。本文以 <code class="prettyprint">JVM 进程内启动（in-process)</code>方式为例，在 Rainbond 中使用 JMX Exporter 暴露 JVM 监控指标。</blockquote><h2>在 Rainbond 上使用 JMX Exporter</h2>在Rainbond上对于构建类型不同的组件有不同的处理方式，如下<br>
<br><strong>通过源码构建的Java应用</strong><br>
<br>自V5.3版本后通过 Rainbond 源码构建的 JAVA 应用，默认都会将 <code class="prettyprint">JMX Exporter</code> 打包，用户使用时只需添加环境变量开启即可。<br>
<ol><li><br>为 JAVA 服务组件添加一个指定的环境变量 <code class="prettyprint">ES_ENABLE_JMX_EXPORTER = true</code> ，即可开启 <code class="prettyprint">jmx_exporter</code>。</li><li><br>在 JAVA 服务组件的端口管理处添加一个 <code class="prettyprint">5556</code> 端口，这是 jmx_exporter 默认监听的端口。</li></ol><br>
<br><strong>通过镜像构建的Java应用</strong><br>
<br>对于镜像或应用市场构建的应用，可以使用初始化类型的插件实现注入 <code class="prettyprint">jmx_agent</code>。<br>
<br>往期文章中详细讲解过其实现原理，可以参考：Rainbond通过插件整合SkyWalking，实现APM即插即用 <em>Agent插件实现原理部分</em>。<br>
<ul><li>构建 jmx_exporter 插件</li></ul><br>
<br>进入团队 -> 插件 -> 新建插件，创建初始化类型插件，源码地址：<a href="https://github.com/goodrain-apps/jmx_exporter.git" rel="nofollow" target="_blank">https://github.com/goodrain-apps/jmx_exporter.git</a><br>
<br><img src="https://static.goodrain.com/wechat/app-monitor/create_jmx.png" alt referrerpolicy="no-referrer"><br>
<br>插件构建成功后即可使用，为 JAVA 服务组件开通此插件即可。<br>
<ul><li>挂载存储</li></ul><br>
<br>为 JAVA 服务组件挂载存储 <code class="prettyprint">/tmp/agent</code>，使其可以与插件共享存储。<br>
<br>通过共享存储，初始化插件将所需的配置文件以及 <code class="prettyprint">Agent</code> 放在共享存储中供主服务使用，实现服务无侵入。<br>
<ul><li>添加环境变量</li></ul><br>
<br>为 JAVA 服务组件添加环境变量 <code class="prettyprint">JAVA_OPTS = -javaagent:/tmp/agent/jmx_prometheus_javaagent-0.16.1.jar=5556:/tmp/agent/prometheus-jmx-config.yaml</code><br>
<br>可挂载配置文件 <code class="prettyprint">/tmp/agent/prometheus-jmx-config.yaml</code> 替换现有的配置文件。<br>
<ul><li>添加端口</li></ul><br>
<br>在组件的端口管理处，添加新的端口 <code class="prettyprint">5556</code> <br>
<br>最后更新组件即可生效。<br>
<br><h2>添加应用监控点</h2>应用监控是基于 <code class="prettyprint">rbd-monitor</code> 实现，当我们添加了监控点后就相当于创建了一个 <code class="prettyprint">servicemonitor</code>。<br>
<br>进入组件内 -> 监控 -> 业务监控 -> 管理监控点，新增监控点，填写以下信息：<br>
<ul><li><br>配置名：自定义</li><li><br>收集任务名称：自定义</li><li><br>收集间隔时间：10秒</li><li><br>指标路径：/metrics</li><li><br>端口号：选择 <code class="prettyprint">jmx_exporter</code> 端口</li></ul><br>
<br>添加完后更新组件使其生效。<br>
<br><h2>添加监控图表</h2>接下来就可以添加一个监控图表，来展示 JAVA 服务组件中 JVM 的指标行：<br>
<br>点击业务监控面板上方的 <strong>添加图表</strong><br>
<br>输入新的标题，以及对应的查询条件 <code class="prettyprint">jvm_memory_bytes_used</code> 后，点击 <strong>查询</strong>。如果正常返回图表，则说明查询条件是正确的。标题的定义尽量清晰明了，并在有必要的情况下明确单位。<br>
<br>更多指标可参考 <a href="https://github.com/prometheus/jmx_exporter">官方文档</a><br>
<br><img src="https://static.goodrain.com/docs/5.3/practices/app-dev/java-exporter/java-exporter-2.png" alt referrerpolicy="no-referrer"><br>
<br><h2>扩展Grafana</h2>可通过<code class="prettyprint">grafana</code> 展示，以下简述操作步骤：<br>
<ol><li>获取 <code class="prettyprint">rbd-monitor</code> 服务 <code class="prettyprint">CLUSTER IP</code>。</li></ol><br>
<br><pre class="prettyprint">$ kubectl get svc -l name=rbd-monitor -n rbd-system<br>
<br>
NAME          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE<br>
rbd-monitor   ClusterIP   10.43.112.131   <none>        9999/TCP   13d<br>
</pre><br>
<ol><li>在平台上添加第三方服务，填写 <code class="prettyprint">rbd-monitor</code> 服务的 <code class="prettyprint">CLUSTER IP</code>。</li><li>从开源应用商店安装 <code class="prettyprint">Grafana</code>并添加依赖。</li><li>进入Grafana，Configuration -> Add Data Source -> URL为 <code class="prettyprint">http://127.0.0.1:9999</code> ，导入 <em>JVM dashboard ID 8878</em> ，通过Grafana面板展示应用监控信息。</li></ol><br>
<br><img src="https://static.goodrain.com/wechat/app-monitor/grafana-dashboard.png" alt referrerpolicy="no-referrer"><br>
<br><h2>References Link</h2><strong>jmx_export 插件Github</strong>  <a href="https://github.com/goodrain-apps/jmx_exporter.git" rel="nofollow" target="_blank">https://github.com/goodrain-apps/jmx_exporter.git</a><br>
<br><strong>jmx_export 官方</strong>  <a href="https://github.com/prometheus/jmx_exporter.git" rel="nofollow" target="_blank">https://github.com/prometheus/jmx_exporter.git</a><br>
<br><strong>jvm dashboard</strong>  <a href="https://grafana.com/grafana/dashboards/8878" rel="nofollow" target="_blank">https://grafana.com/grafana/dashboards/8878</a><br>
<br><h2>关于Rainbond</h2>Rainbond 是一个开源的云原生应用管理平台，使用简单，不需要懂容器和Kubernetes，支持管理多个Kubernetes集群，提供企业级应用的全生命周期管理，功能包括应用开发环境、应用市场、微服务架构、应用持续交付、应用运维、应用级多云管理等。
                                
                                                              
</div>
            