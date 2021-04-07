
---
title: '基于 RocketMQ Prometheus Exporter 打造定制化 DevOps 平台'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/ba47b820c7814e67bf9c956785c68d27.png'
author: Dockone
comments: false
date: 2021-04-07 12:10:50
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/ba47b820c7814e67bf9c956785c68d27.png'
---

<div>   
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/ba47b820c7814e67bf9c956785c68d27.png" alt="头图.png" referrerpolicy="no-referrer"><br>
<br>作者 | 陈厚道  冯庆<br>
来源 | <a href="https://mp.weixin.qq.com/s/gbSG3VUT7u7ipP0HgH-ACQ">阿里巴巴云原生公众号</a><br>
<br><blockquote><br><strong>导读</strong>：本文将对 RocketMQ-Exporter 的设计实现做一个简单的介绍，读者可通过本文了解到 RocketMQ-Exporter 的实现过程，以及通过 RocketMQ-Exporter 来搭建自己的 RocketMQ 监控系统。RocketMQ 在线可交互教程现已登录知行动手实验室，PC 端登录 start.aliyun.com 即可直达。</blockquote>RocketMQ 云原生系列文章：<br>
<ul><li><a href="http://mp.weixin.qq.com/s?__biz=MzUzNzYxNjAzMg==&mid=2247503524&idx=1&sn=925c6bbb7f3a42a3e8ee1cca047849e7&chksm=fae6c56bcd914c7db520178be25fe7487f3701282cf50c425ac6d612cc04f0aefba66fa25b54&scene=21#wechat_redirect">阿里的 RocketMQ 如何让双十一峰值之下 0 故障</a></li><li><a href="https://mp.weixin.qq.com/s/i-0rmFPAZ9rR-A1NeXUMjQ">当 RocketMQ 遇上 Serverless，会碰撞出怎样的火花？</a></li><li><a href="http://mp.weixin.qq.com/s?__biz=MzUzNzYxNjAzMg==&mid=2247493788&idx=1&sn=28415e847c8a61962477be283d99d6f4&chksm=fae6e353cd916a458f3d836c435a73fba46b22b125f5149449056fa09f138dcb46e094c25461&scene=21#wechat_redirect">云原生时代 RocketMQ 运维管控的利器 - RocketMQ Operator</a></li><li><a href="https://mp.weixin.qq.com/s/b3YGm8uMuOZNRhZdA7egSQ">云原生时代消息中间件的演进路线</a></li><li><a href="https://mp.weixin.qq.com/s/gbSG3VUT7u7ipP0HgH-ACQ">基于 RocketMQ Prometheus Exporter 打造定制化 DevOps 平台</a>（本文）</li></ul><br>
<br><strong>RocketMQ-Exporter 项目的 GitHub 地址：</strong><br>
<a href="https://github.com/apache/rocketmq-exporter"><strong>_</strong></a><strong><a href="https://github.com/apache/rocketmq-exporter_" rel="nofollow" target="_blank">https://github.com/apache/rocketmq-exporter_</a></strong><br>
<br>文章主要内容包含以下几个方面：<br>
<ol><li>RocketMQ 介绍</li><li>Prometheus 简介</li><li>RocketMQ-Exporter 的具体实现</li><li>RocketMQ-Exporter 的监控指标和告警指标</li><li>RocketMQ-Exporter 使用示例</li></ol><br>
<br><h1>RocketMQ 介绍</h1>RocketMQ 是一个分布式消息和流数据平台，具有低延迟、高性能、高可靠性、万亿级容量和灵活的可扩展性。简单的来说，它由 Broker 服务器和客户端两部分组成，其中客户端一个是消息发布者客户端(Producer)，它负责向 Broker 服务器发送消息；另外一个是消息的消费者客户端(Consumer)，多个消费者可以组成一个消费组，来订阅和拉取消费 Broker 服务器上存储的消息。<br>
<br>正由于它具有高性能、高可靠性和高实时性的特点，与其他协议组件在 MQTT 等各种消息场景中的结合也越来越多，应用越来越广泛。而对于这样一个强大的消息中间件平台，在实际使用的时候还缺少一个监控管理平台。<br>
<br>当前在开源界，使用最广泛监控解决方案的就是 Prometheus。与其它传统监控系统相比较，Prometheus 具有易于管理，监控服务的内部运行状态，强大的数据模型，强大的查询语言 PromQL，高效的数据处理，可扩展，易于集成，可视化，开放性等优点。并且借助于 Prometheus 可以很快速的构建出一个能够监控 RocketMQ 的监控平台。<br>
<br><h1>Prometheus 简介</h1>下图展示了 Prometheus 的基本架构：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/a741ca02d3d36fc171a693a713747974.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/a741ca02d3d36fc171a693a713747974.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>1. Prometheus Server</h2>Prometheus Server 是 Prometheus 组件中的核心部分，负责实现对监控数据的获取，存储以及查询。Prometheus Server 可以通过静态配置管理监控目标，也可以配合使用 Service Discovery 的方式动态管理监控目标，并从这些监控目标中获取数据。其次 Prometheus Server 需要对采集到的监控数据进行存储，Prometheus Server 本身就是一个时序数据库，将采集到的监控数据按照时间序列的方式存储在本地磁盘当中。最后 Prometheus Server 对外提供了自定义的 PromQL 语言，实现对数据的查询以及分析。<br>
<br><h2>2. Exporters</h2>Exporter 将监控数据采集的端点通过 HTTP 服务的形式暴露给 Prometheus Server，Prometheus Server 通过访问该 Exporter 提供的 Endpoint 端点，即可获取到需要采集的监控数据。RocketMQ-Exporter 就是这样一个 Exporter，它首先从 RocketMQ 集群采集数据，然后借助 Prometheus 提供的第三方客户端库将采集的数据规范化成符合 Prometheus 系统要求的数据，Prometheus 定时去从 Exporter 拉取数据即可。<br>
<br>当前 RocketMQ Exporter 已被 Prometheus 官方收录，其地址为：<a href="https://github.com/apache/rocketmq-exporter">_</a><a href="https://github.com/apache/rocketmq-exporter_" rel="nofollow" target="_blank">https://github.com/apache/rocketmq-exporter_</a>。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/6a62cf6e4f569ada18524df1d129148c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/6a62cf6e4f569ada18524df1d129148c.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h1>RocketMQ-Exporter 的具体实现</h1>当前在 Exporter 当中，实现原理如下图所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/b019cc10beb83dd00f32b46ffd20da19.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/b019cc10beb83dd00f32b46ffd20da19.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>整个系统基于 spring boot 框架来实现。由于 MQ 内部本身提供了比较全面的数据统计信息，所以对于 Exporter 而言，只需要将 MQ 集群提供的统计信息取出然后进行加工而已。所以 RocketMQ-Exporter 的基本逻辑是内部启动多个定时任务周期性的从 MQ 集群拉取数据，然后将数据规范化后通过端点暴露给 Prometheus 即可。其中主要包含如下主要的三个功能部分：<br>
<ul><li>MQAdminExt 模块通过封装 MQ 系统客户端提供的接口来获取 MQ 集群内部的统计信息。</li><li>MetricService 负责将 MQ 集群返回的结果数据进行加工，使其符合 Prometheus 要求的格式化数据。</li><li>Collect 模块负责存储规范化后的数据，最后当 Prometheus 定时从 Exporter 拉取数据的时候，Exporter 就将 Collector 收集的数据通过 HTTP 的形式在/metrics 端点进行暴露。</li></ul><br>
<br><h1>RocketMQ-Exporter 的监控指标和告警指标</h1>RocketMQ-Exporter 主要是配合 Prometheus 来做监控，下面来看看当前在 Expoter 中定义了哪些监控指标和告警指标。<br>
<ul><li>监控指标</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/56131e37b6019a89578a1d7ac088b8f7.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/56131e37b6019a89578a1d7ac088b8f7.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>rocketmq_message_accumulation 是一个聚合指标，需要根据其它上报指标聚合生成。<br>
<ul><li>告警指标</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/2efe58cd8c0d6922c8db6f4ba13394c5.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/2efe58cd8c0d6922c8db6f4ba13394c5.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>消费者堆积告警指标也是一个聚合指标，它根据消费堆积的聚合指标生成，value 这个阈值对每个消费者是不固定的，当前是根据过去 5 分钟生产者生产的消息数量来定，用户也可以根据实际情况自行设定该阈值。告警指标设置的值只是个阈值只是象征性的值，用户可根据在实际使用 RocketMQ 的情况下自行设定。这里重点介绍一下消费者堆积告警指标，在以往的监控系统中，由于没有像 Prometheus 那样有强大的 PromQL 语言，在处理消费者告警问题时势必需要为每个消费者设置告警，那这样就需要 RocketMQ 系统的维护人员为每个消费者添加，要么在系统后台检测到有新的消费者创建时自动添加。在 Prometheus 中，这可以通过一条如下的语句来实现：<br>
<br><code class="prettyprint">(sum(rocketmq_producer_offset) by (topic) - on(topic)  group_right  sum(rocketmq_consumer_offset) by (group,topic)) <br>
- ignoring(group) group_left sum (avg_over_time(rocketmq_producer_tps[5m])) by (topic)*5*60 > 0</code><br>
<br>借助 PromQL 这一条语句不仅可以实现为任意一个消费者创建消费告警堆积告警，而且还可以使消费堆积的阈值取一个跟生产者发送速度相关的阈值。这样大大增加了消费堆积告警的准确性。<br>
<br><h1>RocketMQ-Exporter 使用示例</h1><h2>1. 启动 NameServer 和 Broker</h2>要验证 RocketMQ 的 Spring-Boot 客户端，首先要确保 RocketMQ 服务正确的下载并启动。可以参考 RocketMQ 主站的快速开始来进行操作。确保启动 NameServer 和 Broker 已经正确启动。<br>
<br><h2>2. 编译 RocketMQ-Exporter</h2>用户当前使用，需要自行下载 git 源码编译：<br>
<br><code class="prettyprint">git clone https://github.com/apache/rocketmq-exporter<br>
cd rocketmq-exporter<br>
mvn clean install</code><br>
<br><h2>3. 配置和运行</h2>RocketMQ-Exporter 有如下的运行选项：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/c04f1754627cc0caddd4660d95a4f471.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/c04f1754627cc0caddd4660d95a4f471.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>以上的运行选项既可以在下载代码后在配置文件中更改，也可以通过命令行来设置。<br>
<br>编译出来的 jar 包就叫 rocketmq-exporter-0.0.1-SNAPSHOT.jar，可以通过如下的方式来运行。<br>
<br><code class="prettyprint">java -jar rocketmq-exporter-0.0.1-SNAPSHOT.jar [--rocketmq.config.namesrvAddr=&quot;127.0.0.1:9876&quot; ...]</code><br>
<br><h2>4. 安装 Prometheus</h2>首先到 Prometheus<a href="https://prometheus.io/download/"> 官方下载地址</a>去下载 Prometheus 安装包，当前以 linux 系统安装为例，选择的安装包为 prometheus-2.7.0-rc.1.linux-amd64.tar.gz，经过如下的操作步骤就可以启动 prometheus 进程。<br>
<br><code class="prettyprint">tar -xzf prometheus-2.7.0-rc.1.linux-amd64.tar.gzcd prometheus-2.7.0-rc.1.linux-amd64/./prometheus --config.file=prometheus.yml --web.listen-address=:5555</code><br>
<br>Prometheus 默认监听端口号为 9090，为了不与系统上的其它进程监听端口冲突，我们在启动参数里面重新设置了监听端口号为 5555。然后通过浏览器访问 <a href="http://</" rel="nofollow" target="_blank">http://<</a>服务器 IP 地址>:5555,就可以验证 Prometheus 是否已成功安装，显示界面如下：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/a7ca90aa6e5e2c5fd988d04d630e92c8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/a7ca90aa6e5e2c5fd988d04d630e92c8.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>由于 RocketMQ-Exporter 进程已启动，这个时候可以通过 Prometheus 来抓取 RocketMQ-Exporter 的数据，这个时候只需要更改 Prometheus 启动的配置文件即可。<br>
<br>整体配置文件如下：<br>
<br>```<br>
<h1>my global config</h1>global:<br>
   scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.<br>
   evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.<br>
   # scrape_timeout is set to the global default (10s).<br>
<br> # Load rules once and periodically evaluate them according to the global 'evaluation_interval'.<br>
 rule_files:<br>
   # - "first_rules.yml"<br>
   # - "second_rules.yml"<br>
<br> scrape_configs:<br>
   - job_name: 'prometheus'<br>
     static_configs:<br>
     - targets: ['localhost:5555']<br>
<ul><li>job_name: 'exporter'<br>
 static_configs:<br>
<ul> - targets: ['localhost:5557']<br>
```</ul></li></ul><br>
<br>更改配置文件后，重启服务即可。重启后就可以在 Prometheus 界面查询 RocketMQ-Exporter 上报的指标，例如查询 rocketmq_broker_tps 指标，其结果如下：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/4f0176cec132bb9fa72c0ffc95c98799.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/4f0176cec132bb9fa72c0ffc95c98799.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>5. 告警规则添加</h2>在 Prometheus 可以展示 RocketMQ-Exporter 的指标后，就可以在 Prometheus 中配置 RocketMQ 的告警指标了。在 Prometheus 的配置文件中添加如下的告警配置项，*.rules 表示可以匹配多个后缀为 rules 的文件。<br>
<br><code class="prettyprint">rule_files:<br>
  # - &quot;first_rules.yml&quot;<br>
  # - &quot;second_rules.yml&quot; <br>
  - /home/prometheus/prometheus-2.7.0-rc.1.linux-amd64/rules/*.rules</code><br>
<br>当前设置的告警配置文件为 warn.rules，其文件具体内容如下所示。其中的阈值只起一个示例的作用，具体的阈值还需用户根据实际使用情况来自行设定。<br>
<br><code class="prettyprint"><h2>#</h2><h1>Sample prometheus rules/alerts for rocketmq.</h1>#<br>
<h2>#</h2><h1>Galera Alerts</h1>groups:<br>
- name: GaleraAlerts<br>
  rules:<br>
  - alert: RocketMQClusterProduceHigh<br>
    expr: sum(rocketmq_producer_tps) by (cluster) >= 10<br>
    for: 3m<br>
    labels:<br>
      severity: warning<br>
    annotations:<br>
      description: '&#123;&#123;$labels.cluster&#125;&#125; Sending tps too high.'<br>
      summary: cluster send tps too high<br>
  - alert: RocketMQClusterProduceLow<br>
    expr: sum(rocketmq_producer_tps) by (cluster) &lt; 1<br>
    for: 3m<br>
    labels:<br>
      severity: warning<br>
    annotations:<br>
      description: '&#123;&#123;$labels.cluster&#125;&#125; Sending tps too low.'<br>
      summary: cluster send tps too low<br>
  - alert: RocketMQClusterConsumeHigh<br>
    expr: sum(rocketmq_consumer_tps) by (cluster) >= 10<br>
    for: 3m<br>
    labels:<br>
      severity: warning<br>
    annotations:<br>
      description: '&#123;&#123;$labels.cluster&#125;&#125; consuming tps too high.'<br>
      summary: cluster consume tps too high<br>
  - alert: RocketMQClusterConsumeLow<br>
    expr: sum(rocketmq_consumer_tps) by (cluster) &lt; 1<br>
    for: 3m<br>
    labels:<br>
      severity: warning<br>
    annotations:<br>
      description: '&#123;&#123;$labels.cluster&#125;&#125; consuming tps too low.'<br>
      summary: cluster consume tps too low<br>
  - alert: ConsumerFallingBehind<br>
    expr: (sum(rocketmq_producer_offset) by (topic) - on(topic)  group_right  sum(rocketmq_consumer_offset) by (group,topic)) - ignoring(group) group_left sum (avg_over_time(rocketmq_producer_tps[5m])) by (topic)*5*60 > 0<br>
    for: 3m<br>
    labels:<br>
      severity: warning<br>
    annotations:<br>
      description: 'consumer &#123;&#123;$labels.group&#125;&#125; on &#123;&#123;$labels.topic&#125;&#125; lag behind<br>
        and is falling behind (behind value &#123;&#123;$value&#125;&#125;).'<br>
      summary: consumer lag behind<br>
  - alert: GroupGetLatencyByStoretime<br>
    expr: rocketmq_group_get_latency_by_storetime > 1000<br>
    for: 3m<br>
    labels:<br>
      severity: warning<br>
    annotations:<br>
      description: 'consumer &#123;&#123;$labels.group&#125;&#125; on &#123;&#123;$labels.broker&#125;&#125;, &#123;&#123;$labels.topic&#125;&#125; consume time lag behind message store time<br>
        and (behind value is &#123;&#123;$value&#125;&#125;).'<br>
      summary: message consumes time lag behind message store time too much</code><br>
<br>最终，可以在 Prometheus 的看一下告警展示效果，红色表示当前处于告警状态的项，绿色表示正常状态。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/f44841c151c5aec19fb1361cc06b35c4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/f44841c151c5aec19fb1361cc06b35c4.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>6. Grafana dashboard for RocketMQ</h2>Prometheus 自身的指标展示平台没有当前流行的展示平台 Grafana 好， 为了更好的展示 RocketMQ 的指标，可以使用 Grafana 来展示 Prometheus 获取的指标。<br>
<br>首先到官网去下载：<a href="https://grafana.com/grafana/download">_</a><a href="https://grafana.com/grafana/download_" rel="nofollow" target="_blank">https://grafana.com/grafana/download_</a>，这里仍以二进制文件安装为例进行介绍。<br>
<br><code class="prettyprint">wget https://dl.grafana.com/oss/release/grafana-6.2.5.linux-amd64.tar.gz <br>
tar -zxvf grafana-6.2.5.linux-amd64.tar.gz<br>
cd grafana-5.4.3/</code><br>
<br>同样为了不与其它进程的使用端口冲突，可以修改 conf 目录下的 defaults.ini 文件的监听端口，当前将 grafana 的监听端口改为 55555，然后使用如下的命令启动即可：<br>
<br><code class="prettyprint">./bin/grafana-server web</code><br>
然后通过浏览器访问 <a href="http://</" rel="nofollow" target="_blank">http://<</a>服务器 IP 地址>:55555,就可以验证 grafana 是否已成功安装。系统默认用户名和密码为 admin/admin，第一次登陆系统会要求修改密码，修改密码后登陆，界面显示如下：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/de3e55d1d21f9868686acb54f5e23d2d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/de3e55d1d21f9868686acb54f5e23d2d.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>点击 Add data source 按钮，会要求选择数据源。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/57208547bbaf286e813fe92baf4bbaf3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/57208547bbaf286e813fe92baf4bbaf3.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>选择数据源为 Prometheus，设置数据源的地址为前面步骤启动的 Prometheus 的地址。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/49141e2a4a300b60da687c16e580c38e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/49141e2a4a300b60da687c16e580c38e.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>回到主界面会要求创建新的 Dashboard。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/1ca112064d64a6ebb949dac8342ee67f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/1ca112064d64a6ebb949dac8342ee67f.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>点击创建 dashboard，创建 dashboard 可以自己手动创建，也可以以配置文件导入的方式创建，当前已将 RocketMQ 的 dashboard 配置文件上传到 Grafana 的官网，这里以配置文件导入的方式进行创建。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/677d3bc49c549e695d84974201ebe183.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/677d3bc49c549e695d84974201ebe183.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>点击 New dashboard 下拉按钮。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/60105d2d276e9dd6c89561b3f8a21ea1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/60105d2d276e9dd6c89561b3f8a21ea1.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>选择 import dashboard。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/53d38dea0459d30ee99b60b6d9711d27.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/53d38dea0459d30ee99b60b6d9711d27.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>这个时候可以到 Grafana 官网去下载当前已为 RocketMQ 创建好的配置文件，地址为：<a href="https://grafana.com/dashboards/10477/revisions">_</a><a href="https://grafana.com/dashboards/10477/revisions_" rel="nofollow" target="_blank">https://grafana.com/dashboards/10477/revisions_</a>，如下图所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/9ef7b5acf27fe12988e1c7431feddda5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/9ef7b5acf27fe12988e1c7431feddda5.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>点击 download 就可以下载配置文件，下载配置文件然后，复制配置文件中的内容粘贴到上图的粘贴内容处。<br>
<br>最后按上述方式就将配置文件导入到 Grafana 了。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/8d2fe2d118f18047184642f973154c96.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/8d2fe2d118f18047184642f973154c96.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>最终的效果如下所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/ad4a11d3996b866d2eee5e1ea2e6524f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/ad4a11d3996b866d2eee5e1ea2e6524f.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>作者简介</h2><strong>陈厚道</strong>，曾就职于腾讯、盛大、斗鱼等互联网公司。目前就职于尚德机构，在尚德机构负责基础架构方面的设计和开发工作。对分布式消息队列、微服务架构和落地、DevOps 和监控平台有比较深入的研究。<br>
<br><strong>冯庆</strong>，曾就职于华为。目前就职于尚德机构，在尚德机构基础架构团队负责基础组件的开发工作。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210407/1748099b45017eab046a01509600f42f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210407/1748099b45017eab046a01509600f42f.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>在 PC 端登录 **<a href="https://start.aliyun.com/"><strong>start.aliyun.com</strong></a></strong> 知行动手实验室，沉浸式体验在线交互教程**。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            