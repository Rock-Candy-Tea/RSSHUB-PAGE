
---
title: 'Rainbond通过插件整合ELK_EFK，实现日志收集'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/wechat/EFK/es_architecture.png'
author: Dockone
comments: false
date: 2022-01-01 15:07:45
thumbnail: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/wechat/EFK/es_architecture.png'
---

<div>   
<br><h3>前言</h3>ELK 是三个开源项目的首字母缩写：Elasticsearch、Logstash 和 Kibana。但后来出现的 FileBeat 可以完全替代 Logstash的数据收集功能，也比较轻量级。本文将介绍 <strong>EFK:</strong> Elasticsearch、Filebeat 和 Kibana<br>
<br>Elasticsearch：分布式搜索和分析引擎，具有高可伸缩、高可靠和易管理等特点。基于 Apache Lucene 构建，能对大容量的数据进行接近实时的存储、搜索和分析操作。通常被用作某些应用的基础搜索引擎，使其具有复杂的搜索功能；<br>
<br>Kibana：数据分析和可视化平台。与 Elasticsearch 配合使用，对其中数据进行搜索、分析和以统计图表的方式展示；<br>
<br>Filebeat：Filebeat 是一个轻量级的传送器，用于转发和集中日志数据。Filebeat 作为代理安装在您的服务器上，监控您指定的日志文件或位置，收集日志事件，并将它们转发到 Elasticsearch 或 Logstash 以进行索引。<br>
<br>通过本文了解如何将运行在 Rainbond 上的应用，通过开启 FileBeat 插件的方式收集应用日志并发送到 Elasticsearch 中。<br>
<br><h3>整合架构</h3>在收集日志时，需要在应用中启用 FileBeat 插件进行收集，FileBeat收集日志有三种方式：<br>
<ol><li>指定日志路径</li><li>收集所有容器日志</li><li>指定 Label 自动发现</li></ol><br>
<br>本文使用 指定日志路径进行收集，这种方式我们可以自定义收集日志的规则等。<br>
<br>我们将 FileBeat 制作成 Rainbond 的 <a href="https://www.rainbond.com/docs/get-start/concept/plugin?channel=dockone">一般类型插件</a> ，在应用启动之后，插件也随之启动并自动收集日志发送至 Elasticsearch,整个过程对应用容器无侵入，且拓展性强。对接其他日志收集也可以用类似方式，用户通过替换插件实现对接不同的日志收集工具。<br>
<br>下图展示了在Rainbond使用FileBeat插件收集应用日志并发送到 Elasticsearch 的结构。<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/wechat/EFK/es_architecture.png" alt="image-20211223162213573" referrerpolicy="no-referrer"><br>
<br><h3>插件实现原理解析</h3>Rainbond插件体系是相对于Rainbond应用模型的一部分，插件主要用来实现应用容器扩展运维能力。由于运维工具的实现有较大的共性，因此插件本身可以被复用。插件必须绑定到应用容器时才具有运行时状态，用以实现一种运维能力，比如性能分析插件、网络治理插件、初始化类型插件。<br>
<br>具有运行时的插件的运行环境与所绑定的组件从以下几个方面保持一致：<br>
<ul><li><strong>网络空间</strong> 这个一个至关重要的特性，网络空间一致使插件可以对组件网络流量进行旁路监听和拦截，设置组件本地域名解析等。</li><li><strong>存储持久化空间</strong> 这个特性使得插件与组件之间可以通过持久化目录进行文件交换。</li><li><strong>环境变量</strong> 这个特性使得插件可以读取组件的环境变量。</li></ul><br>
<br>在制作 FileBeat 插件的过程中，使用到了 <strong>一般类型插件</strong>，可以理解为一个POD启动两个 Container，Kubernetes原生支持一个POD中启动多个 Container，但配置起来相对复杂，在Rainbond中通过插件实现使用户操作简单。<br>
<br><h3>通过Rainbond 应用商店一键安装 EK</h3>我们已将 elasticsearch + Kibana 制作为应用并发布至应用市场，用户可基于开源应用商店一键安装。<br>
<ol><li>安装 Rainbond</li><li>在开源应用商店搜索 elasticsearch，点击安装即可一键安装；</li></ol><br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/wechat/EFK/es_store.png" alt="image-20211223163856435" referrerpolicy="no-referrer"><br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/wechat/EFK/es_topology.png" alt="image-20211223164246240" referrerpolicy="no-referrer"><br>
<ol><li><code class="prettyprint">elasticsearch</code> 默认启用了 xpack 安全模块来保护我们的集群，所以我们需要一个初始化的密码。我们进入 <code class="prettyprint">elasticsearch</code> Web终端执行如下所示的命令，Web终端内运行 <code class="prettyprint">bin/elasticsearch-setup-passwords</code> 命令来生成默认的用户名和密码：</li></ol><br>
<br><code class="prettyprint">shell<br>
bin/elasticsearch-setup-passwords 参数<br>
auto 自动生成<br>
interactive 手动填写</code><br>
<ol><li>进入 <code class="prettyprint">Kibana</code> 组件的环境变量中，修改默认连接 <code class="prettyprint">elasticsearch</code>的环境变量 <code class="prettyprint">ELASTICSEARCH_PASSWORD</code>。</li></ol><br>
<br><h3>收集应用日志</h3>使用 Nginx 作为本文的演示应用，在Rainbond上使用镜像创建组件，<br>
<ul><li>镜像地址：<code class="prettyprint">nginx:latest</code></li><li>挂载存储：<code class="prettyprint">/var/log/nginx</code>，将Nginx日志持久化，Filebeat插件可读取到该日志文件。</li></ul><br>
<br><strong>制作 FileBeat 插件</strong><br>
<br>在Rainbond团队界面点击插件后进入插件界面，点击新建插件，创建一般类型插件。<br>
<ul><li>镜像地址：docker.elastic.co/beats/filebeat:7.15.2</li><li>其他自定义即可。</li></ul><br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/wechat/EFK/create_plugin.png" alt="image-20211223165325136" referrerpolicy="no-referrer"><br>
<br>创建插件并构建，构建成功后我们在 Nginx组件的插件中开通 FileBeat 插件。<br>
<br>在Nginx组件的环境配置中，添加 FileBeat 配置文件 如下，更多配置可参考 <a href="https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-reference-yml.html">官方文档</a><br>
<ul><li>配置文件挂载路径：/usr/share/filebeat/filebeat.yml</li><li>配置文件权限：644</li></ul><br>
<br><code class="prettyprint">yaml<br>
filebeat.inputs:<br>
- type: log<br>
  paths:<br>
    - /var/log/nginx/*.log<br>
output.elasticsearch:<br>
  hosts: '127.0.0.1:9200'<br>
  username: &quot;elastic&quot;<br>
  password: &quot;elastic&quot;</code><br>
<br><strong>建立依赖关系</strong><br>
<br>将 Nginx 与 elasticsearch 建立依赖关系，使其能通过 <code class="prettyprint">127.0.0.1</code>地址与 <code class="prettyprint">elasticsearch</code> 通信，更新Nginx组件使依赖生效。<br>
<br><strong>访问Kibana</strong><br>
<br><blockquote><br>Kibana默认已汉化<br>
  <ol><li><br>点击 <code class="prettyprint">Stack Management</code> > 索引管理，可看到我们的 <code class="prettyprint">filebeat</code> 索引已存在。</li><li><br><code class="prettyprint">Stack Management</code> > 索引模式，创建 <code class="prettyprint">filebeat</code> 索引模式。</li><li><br><code class="prettyprint">Discover</code> 页面即可看到日志信息。</li></ol></blockquote><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/wechat/EFK/discover.png" alt="image-20211223180227267" referrerpolicy="no-referrer"><br>
<br><h3>总结</h3>基于Rainbond的插件机制与 EFK 结合，使用户可以快速的通过<code class="prettyprint">EFK</code>收集应用日志进行分析，并且可灵活的将插件 <code class="prettyprint">FileBeat</code> 替换为 <code class="prettyprint">Logstash</code>。<br>
<br>除此之外，Rainbond的插件机制具有开放性，通过插件机制对应用治理功能进行扩展，例如网络治理类、数据备份类插件，在对原应用逻辑无侵入的情况下，能够通过网络治理类插件对服务的性能进行分析，对接ELK等日志收集系统；对于数据库等组件而言，使用备份插件对数据进行备份。<br>
<br><h3>关于Rainbond</h3>Rainbond 是一个开源的云原生应用管理平台，使用简单，不需要懂容器和Kubernetes，支持管理多个Kubernetes集群，提供企业级应用的全生命周期管理，功能包括应用开发环境、应用市场、微服务架构、应用持续交付、应用运维、应用级多云管理等。<br>
<br>Github：<a href="https://github.com/goodrain/rainbond" rel="nofollow" target="_blank">https://github.com/goodrain/rainbond</a><br>
<br>官网：<a href="https://www.rainbond.com/" rel="nofollow" target="_blank">https://www.rainbond.com</a><br>
<br>微信群：请搜索添加群助手微信号 <code class="prettyprint">wylhzmyj</code><br>
<br>钉钉群：请搜索钉钉群号 <code class="prettyprint">31096419</code>
                                
                                                              
</div>
            