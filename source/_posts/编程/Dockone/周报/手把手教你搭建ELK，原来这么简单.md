
---
title: '手把手教你搭建ELK，原来这么简单'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/b8b549601324100ac5163a82f7a1130a.png'
author: Dockone
comments: false
date: 2021-08-25 07:07:51
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/b8b549601324100ac5163a82f7a1130a.png'
---

<div>   
<br><h3>概述</h3>我们都知道，在生产环境中经常会遇到很多异常，报错信息，需要查看日志信息排查错误。现在的系统大多比较复杂，即使是一个服务背后也是一个集群的机器在运行，<strong>如果逐台机器去查看日志显然是很费力的，也不现实</strong>。<br>
<br>如果能把日志全部收集到一个平台，然后像百度，谷歌一样<strong>通过关键字搜索出相关的日志</strong>，岂不快哉。于是就有了<strong>集中式日志系统</strong>。ELK就是其中一款使用最多的开源产品。<br>
<h3>思维导图</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/b8b549601324100ac5163a82f7a1130a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/b8b549601324100ac5163a82f7a1130a.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>什么是ELK</h3>ELK其实是Elasticsearch，Logstash 和 Kibana三个产品的首字母缩写，这三款都是开源产品。<br>
<br><strong>ElasticSearch</strong>（简称ES），是一个实时的分布式搜索和分析引擎，它可以用于全文搜索，结构化搜索以及分析。<br>
<br><strong>Logstash</strong>，是一个数据收集引擎，主要用于进行数据收集、解析，并将数据发送给ES。支持的数据源包括本地文件、ElasticSearch、MySQL、Kafka等等。<br>
<br><strong>Kibana</strong>，为 Elasticsearch 提供了分析和 Web 可视化界面，并生成各种维度表格、图形。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/42522d7c8de227d21c9299037af6be78.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/42522d7c8de227d21c9299037af6be78.png" class="img-polaroid" title="01.png" alt="01.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>搭建ELK</h3>环境依赖：CentOS 7.5，JDK 1.8，ElasticSearch 7.9.3，Logstash 7.9.3，Kibana 7.9.3。<br>
<h4>安装ElasticSearch</h4>首先，到官网下载安装包，然后使用 <code class="prettyprint">tar -zxvf</code> 命令解压。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/3076fe1cf37575c228068b9e28cab0b9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/3076fe1cf37575c228068b9e28cab0b9.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
找到 config 目录下的 elasticsearch.yml 文件，修改配置：<br>
<pre class="prettyprint">cluster.name: es-application  <br>
node.name: node-1  <br>
#对所有 IP 开放  <br>
network.host: 0.0.0.0  <br>
#HTTP 端口号  <br>
http.port: 9200  <br>
#ElasticSearch 数据文件存放目录  <br>
path.data: /usr/elasticsearch-7.9.3/data  <br>
#ElasticSearch 日志文件存放目录  <br>
path.logs: /usr/elasticsearch-7.9.3/logs<br>
</pre><br>
配置完之后，因为 ElasticSearch 使用非 root 用户启动，所以创建一个用户。<br>
<pre class="prettyprint"># 创建用户  <br>
useradd yehongzhi  <br>
# 设置密码  <br>
passwd yehongzhi  <br>
# 赋予用户权限  <br>
chown -R yehongzhi:yehongzhi /usr/elasticsearch-7.9.3/<br>
</pre><br>
然后切换用户，启动：<br>
<pre class="prettyprint"># 切换用户  <br>
su yehongzhi  <br>
# 启动 -d 表示后台启动  <br>
./bin/elasticsearch -d<br>
</pre><br>
使用命令 <code class="prettyprint">netstat -nltp</code> 查看端口号：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/7198e7a690104d4c7d43ebae6f9b809d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/7198e7a690104d4c7d43ebae6f9b809d.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
访问 <a href="http://192.168.0.109:9200/" rel="nofollow" target="_blank">http://192.168.0.109:9200/</a> 可以看到如下信息，表示安装成功。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/91672d58cc1bfda7e52d7d87eb9ea2fd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/91672d58cc1bfda7e52d7d87eb9ea2fd.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>安装 Logstash</h4>首先在官网下载安装压缩包，然后解压，找到 /config 目录下的 logstash-sample.conf 文件，修改配置：<br>
<pre class="prettyprint">input &#123;  <br>
file&#123;  <br>
path => ['/usr/local/user/*.log']  <br>
type => 'user_log'  <br>
start_position => "beginning"  <br>
&#125;  <br>
&#125;  <br>
<br>
output &#123;  <br>
elasticsearch &#123;  <br>
hosts => ["http://192.168.0.109:9200"]  <br>
index => "user-%&#123;+YYYY.MM.dd&#125;"  <br>
&#125;  <br>
&#125; <br>
</pre><br>
input 表示输入源，output 表示输出，还可以配置 filter 过滤，架构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/7997d5a424cb8ee5c4aaf0f8e9b67f65.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/7997d5a424cb8ee5c4aaf0f8e9b67f65.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
配置完之后，要有数据源，也就是日志文件，准备一个 user.jar 应用程序，然后后台启动，并且输出到日志文件 user.log 中，命令如下：<br>
<pre class="prettyprint">nohup java -jar user.jar >/usr/local/user/user.log &<br>
</pre><br>
接着再后台启动 Logstash，命令如下：<br>
<pre class="prettyprint">nohup ./bin/logstash -f /usr/logstash-7.9.3/config/logstash-sample.conf &<br>
</pre><br>
启动完之后，使用 <code class="prettyprint">jps</code> 命令，可以看到两个进程在运行：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/6743bd29165ea261bd99c6ffe52da1c4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/6743bd29165ea261bd99c6ffe52da1c4.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>安装 Kibana</h4>首先还是到官网下载压缩包，然后解压，找到 /config 目录下的 kibana.yml 文件，修改配置：<br>
<pre class="prettyprint">server.port: 5601  <br>
server.host: "192.168.0.111"  <br>
elasticsearch.hosts: ["http://192.168.0.109:9200"]<br>
</pre><br>
和 ElasticSearch 一样，不能使用 root 用户启动，需要创建一个用户：<br>
<pre class="prettyprint"># 创建用户  <br>
useradd kibana<br>
# 设置密码<br>
passwd kibana<br>
# 赋予用户权限<br>
chown -R kibana:kibana /usr/kibana/<br>
</pre><br>
然后使用命令启动：<br>
<pre class="prettyprint">#切换用户<br>
su kibana<br>
#非后台启动，关闭 shell 窗口即退出<br>
./bin/kibana  <br>
#后台启动<br>
nohup ./bin/kibana &<br>
</pre><br>
启动后在浏览器打开 <a href="http://192.168.0.111:5601/" rel="nofollow" target="_blank">http://192.168.0.111:5601</a>，可以看到 Kibana 的 Web 交互界面：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/cad0ccc6bb3bbfa7f162e96fd44e6f2e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/cad0ccc6bb3bbfa7f162e96fd44e6f2e.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>效果展示</h4>全部启动成功后，整个过程应该是这样，我们看一下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/54385694e5dc2e7c4c929e5051298fbb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/54385694e5dc2e7c4c929e5051298fbb.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
浏览器打开 <a href="http://192.168.0.111:5601/" rel="nofollow" target="_blank">http://192.168.0.111:5601</a>，到管理界面，点击“Index Management”可以看到，有一个 <code class="prettyprint">user-2020.10.31</code> 的索引。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/5b2ac121850e4032bc808bf01dcf6e49.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/5b2ac121850e4032bc808bf01dcf6e49.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
点击 <code class="prettyprint">Index Patterns</code> 菜单栏，然后创建，命名为 user-* 。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/a6ffece4c59306286ce6ad4fe10616da.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/a6ffece4c59306286ce6ad4fe10616da.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
最后，就可以到 Discover 栏进行选择，选择 user-* 的 Index Pattern，然后搜索关键字，就找到相关的日志了！<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/212f43ef243fb59636e6b6e048133721.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/212f43ef243fb59636e6b6e048133721.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>改进优化</h3>上面只是用到了核心的三个组件简单搭建的 ELK，实际上是有缺陷的。如果 Logstash 需要添加插件，那就全部服务器的 Logstash 都要添加插件，扩展性差。所以就有了 <strong>FileBeat</strong>，占用资源少，只负责采集日志，不做其他的事情，这样就轻量级，把 Logstash 抽出来，做一些滤处理之类的工作。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/c254327b49f58a1619d2f8a63de3d481.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/c254327b49f58a1619d2f8a63de3d481.jpg" class="img-polaroid" title="13.jpg" alt="13.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
FileBeat 也是官方推荐用的日志采集器，首先下载 Linux 安装压缩包：<br>
<pre class="prettyprint">https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.9.3-linux-x86_64.tar.gz<br>
</pre><br>
下载完成后，解压。然后修改 filebeat.yml 配置文件：<br>
<pre class="prettyprint">#输入源  <br>
filebeat.inputs:  <br>
- type: log  <br>
enabled: true  <br>
paths:  <br>
- /usr/local/user/*.log  <br>
#输出，Logstash 的服务器地址  <br>
output.logstash:  <br>
hosts: ["192.168.0.110:5044"]  <br>
#输出，如果直接输出到 ElasticSearch 则填写这个  <br>
#output.elasticsearch:  <br>
#hosts: ["localhost:9200"]  <br>
#protocol: "https"<br>
</pre><br>
然后 Logstash 的配置文件 logstash-sample.conf，也要改一下：<br>
<pre class="prettyprint">#输入源改成 beats  <br>
input &#123;  <br>
beats &#123;  <br>
port => 5044  <br>
codec => "json"  <br>
&#125;  <br>
&#125; <br>
</pre><br>
然后启动 FileBeat：<br>
<pre class="prettyprint">#后台启动命令  <br>
nohup ./filebeat -e -c filebeat.yml >/dev/null 2>&1 & <br>
</pre> <br>
再启动 Logstash：<br>
<pre class="prettyprint">#后台启动命令  <br>
nohup ./bin/logstash -f /usr/logstash-7.9.3/config/logstash-sample.conf &<br>
</pre><br>
怎么判断启动成功呢，看 Logstash 应用的 /logs 目录下的 logstash-plain.log 日志文件：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210823/e22c26521d88584effc83f096231aee7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210823/e22c26521d88584effc83f096231aee7.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>写在最后</h3>目前，很多互联网公司都是采用ELK来做日志集中式系统，原因很简单：<strong>开源、插件多、易扩展、支持数据源多、社区活跃、开箱即用</strong>等等。我见过有一个公司在上面的架构中还会加多一个 Kafka 的集群，主要是基于日志数据量比较大的考虑。但是呢，基本的三大组件 ElasticSearch，Logstash，Kibana 是不能少的。<br>
<br>希望这篇文章能帮助大家对ELK有一些初步的认识，感谢大家的阅读。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/gwYJeEBVRgD6SkZWoP-skg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/gwYJeEBVRgD6SkZWoP-skg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            