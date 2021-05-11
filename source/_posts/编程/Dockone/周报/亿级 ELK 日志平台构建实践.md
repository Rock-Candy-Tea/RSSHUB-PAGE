
---
title: '亿级 ELK 日志平台构建实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210510/60e33a72d81f8efc86ff3b11c8b3d530.png'
author: Dockone
comments: false
date: 2021-05-11 08:02:30
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210510/60e33a72d81f8efc86ff3b11c8b3d530.png'
---

<div>   
<br>本篇主要讲工作中的真实经历，我们怎么打造亿级日志平台，同时手把手教大家建立起这样一套亿级 ELK 系统。<br>
<br>废话不多说，老司机们座好了，我们准备发车了~~~<br>
<h3>整体架构</h3>整体架构主要分为 4 个模块，分别提供不同的功能。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210510/60e33a72d81f8efc86ff3b11c8b3d530.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210510/60e33a72d81f8efc86ff3b11c8b3d530.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>Filebeat</strong>：轻量级数据收集引擎。基于原先 Logstash-fowarder 的源码改造出来。换句话说：Filebeat就是新版的 Logstash-fowarder，也会是 ELK Stack 在 Agent 的第一选择。<br>
<br><strong>Kafka</strong>：数据缓冲队列。作为消息队列解耦了处理过程，同时提高了可扩展性。具有峰值处理能力，使用消息队列能够使关键组件顶住突发的访问压力，而不会因为突发的超负荷的请求而完全崩溃。<br>
<br><strong>Logstash</strong>：数据收集处理引擎。支持动态的从各种数据源搜集数据，并对数据进行过滤、分析、丰富、统一格式等操作，然后存储以供后续使用。<br>
<br><strong>Elasticsearch</strong>：分布式搜索引擎。具有高可伸缩、高可靠、易管理等特点。可以用于全文检索、结构化检索和分析，并能将这三者结合起来。Elasticsearch 基于 Lucene 开发，现在使用最广的开源搜索引擎之一，Wikipedia 、StackOverflow、Github 等都基于它来构建自己的搜索引擎。<br>
<br><strong>Kibana</strong>：可视化化平台。它能够搜索、展示存储在 Elasticsearch 中索引数据。使用它可以很方便的用图表、表格、地图展示和分析数据。<br>
<br><h3>版本说明</h3>Filebeat：6.2.4<br>
<br>Kafka：2.11-1<br>
<br>Logstash：6.2.4<br>
<br>Elasticsearch：6.2.4<br>
<br>Kibana：6.2.4<br>
<br>相应的版本最好下载对应的插件。<br>
<h3>具体实践</h3>我们就以比较常见的 Nginx 日志来举例说明下，日志内容是 JSON 格式。<br>
<pre class="prettyprint">&#123;"@timestamp":"2017-12-27T16:38:17+08:00","host":"192.168.56.11","clientip":"192.168.56.11","size":26,"responsetime":0.000,"upstreamtime":"-","upstreamhost":"-","http_host":"192.168.56.11","url":"/nginxweb/index.html","domain":"192.168.56.11","xff":"-","referer":"-","status":"200"&#125;<br>
&#123;"@timestamp":"2017-12-27T16:38:17+08:00","host":"192.168.56.11","clientip":"192.168.56.11","size":26,"responsetime":0.000,"upstreamtime":"-","upstreamhost":"-","http_host":"192.168.56.11","url":"/nginxweb/index.html","domain":"192.168.56.11","xff":"-","referer":"-","status":"200"&#125;<br>
&#123;"@timestamp":"2017-12-27T16:38:17+08:00","host":"192.168.56.11","clientip":"192.168.56.11","size":26,"responsetime":0.000,"upstreamtime":"-","upstreamhost":"-","http_host":"192.168.56.11","url":"/nginxweb/index.html","domain":"192.168.56.11","xff":"-","referer":"-","status":"200"&#125;<br>
&#123;"@timestamp":"2017-12-27T16:38:17+08:00","host":"192.168.56.11","clientip":"192.168.56.11","size":26,"responsetime":0.000,"upstreamtime":"-","upstreamhost":"-","http_host":"192.168.56.11","url":"/nginxweb/index.html","domain":"192.168.56.11","xff":"-","referer":"-","status":"200"&#125;<br>
&#123;"@timestamp":"2017-12-27T16:38:17+08:00","host":"192.168.56.11","clientip":"192.168.56.11","size":26,"responsetime":0.000,"upstreamtime":"-","upstreamhost":"-","http_host":"192.168.56.11","url":"/nginxweb/index.html","domain":"192.168.56.11","xff":"-","referer":"-","status":"200"&#125; <br>
</pre><br>
<h4>Filebeat</h4>为什么用 Filebeat ，而不用原来的 Logstash 呢？<br>
<br>原因很简单，资源消耗比较大。<br>
<br>由于 Logstash 是跑在 JVM 上面，资源消耗比较大，后来作者用 GO 写了一个功能较少但是资源消耗也小的轻量级的 Agent 叫 Logstash-forwarder。<br>
<br>后来作者加入 elastic.co 公司， Logstash-forwarder 的开发工作给公司内部 GO 团队来搞，最后命名为 Filebeat。<br>
<br>Filebeat 需要部署在每台应用服务器上，可以通过 Salt 来推送并安装配置。<br>
<br>下载：<br>
<pre class="prettyprint">$ wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.2.4-darwin-x86_64.tar.gz<br>
</pre><br>
解压：<br>
<pre class="prettyprint">tar -zxvf filebeat-6.2.4-darwin-x86_64.tar.gz<br>
mv filebeat-6.2.4-darwin-x86_64 filebeat<br>
cd filebeat<br>
</pre><br>
修改配置：<br>
<br>修改 Filebeat 配置，支持收集本地目录日志，并输出日志到 Kafka 集群中。<br>
<pre class="prettyprint">$ vim fileat.yml<br>
filebeat.prospectors:<br>
- input_type: log<br>
paths:<br>
-  /opt/logs/server/nginx.log<br>
json.keys_under_root: true<br>
json.add_error_key: true<br>
json.message_key: log<br>
<br>
output.kafka:   <br>
hosts: ["192.168.0.1:9092，192.168.0.2:9092，192.168.0.3:9092"]<br>
topic: 'nginx'<br>
</pre><br>
Filebeat 6.0 之后一些配置参数变动比较大，比如 document_type 就不支持，需要用 fields 来代替等等。<br>
<br>启动：<br>
<pre class="prettyprint">$ ./filebeat -e -c filebeat.yml<br>
</pre><br>
<h4>Kafka</h4>生产环境中 Kafka 集群中节点数量建议为（2N + 1 ）个，这边就以 3 个节点举例。<br>
<br>下载：<br>
<br>直接到官网下载 Kafka。<br>
<pre class="prettyprint">$ wget http://mirror.bit.edu.cn/apache/kafka/1.0.0/kafka_2.11-1.0.0.tgz<br>
</pre><br>
解压：<br>
<pre class="prettyprint">tar -zxvf kafka_2.11-1.0.0.tgz<br>
mv kafka_2.11-1.0.0 kafka<br>
cd kafka<br>
</pre><br>
修改 ZooKeeper 配置：<br>
<br>修改 ZooKeeper 配置，搭建 ZooKeeper 集群，数量 ( 2N + 1 ) 个。<br>
<br>ZooKeeper 集群建议采用 Kafka 自带，减少网络相关的因素干扰。<br>
<pre class="prettyprint">$ vim zookeeper.properties<br>
<br>
tickTime=2000<br>
dataDir=/opt/zookeeper<br>
clientPort=2181<br>
maxClientCnxns=50<br>
initLimit=10<br>
syncLimit=5<br>
<br>
server.1=192.168.0.1:2888:3888<br>
server.2=192.168.0.2:2888:3888<br>
server.3=192.168.0.3:2888:3888<br>
</pre><br>
ZooKeeper data 目录下面添加 myid 文件，内容为代表 ZooeKeeper 节点 id （1，2，3），并保证不重复。<br>
<pre class="prettyprint">$ vim /opt/zookeeper/myid<br>
1<br>
</pre><br>
启动 ZooKeeper 节点：<br>
<br>分别启动 3 台 ZooKeeper 节点，保证集群的高可用。<br>
<pre class="prettyprint">$ ./zookeeper-server-start.sh -daemon ./config/zookeeper.properties<br>
</pre><br>
修改 Kafka 配置：<br>
<br>Kafka 集群这边搭建为 3 台，可以逐个修改 Kafka 配置，需要注意其中 broker.id 分别 （1，2，3）。<br>
<pre class="prettyprint">$ vim ./config/server.properties<br>
broker.id=1<br>
port=9092<br>
host.name=192.168.0.1<br>
num.replica.fetchers=1<br>
log.dirs=/opt/kafka_logs<br>
num.partitions=3<br>
zookeeper.connect=192.168.0.1: 192.168.0.2: 192.168.0.3:2181<br>
zookeeper.connection.timeout.ms=6000<br>
zookeeper.sync.time.ms=2000<br>
num.io.threads=8<br>
num.network.threads=8<br>
queued.max.requests=16<br>
fetch.purgatory.purge.interval.requests=100<br>
producer.purgatory.purge.interval.requests=100<br>
delete.topic.enable=true<br>
</pre><br>
启动 Kafka 集群：<br>
<br>分别启动 3 台 Kafka 节点，保证集群的高可用。<br>
<pre class="prettyprint">$ ./bin/kafka-server-start.sh -daemon ./config/server.properties<br>
</pre><br>
查看 topic 是否创建成功。<br>
<pre class="prettyprint">$ bin/kafka-topics.sh --list --zookeeper localhost:2181<br>
<br>
nginx<br>
</pre><br>
监控 Kafka Manager：<br>
<br>Kafka-manager 是 Yahoo 公司开源的集群管理工具。<br>
<br>可以在 Github 上下载安装：<a href="https://github.com/yahoo/kafka-manager" rel="nofollow" target="_blank">https://github.com/yahoo/kafka-manager</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210510/b948f7c974b8b74c115a1f34655cc8ca.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210510/b948f7c974b8b74c115a1f34655cc8ca.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如果遇到 Kafka 消费不及时的话，可以通过到具体 cluster 页面上，增加 partition。Kafka 通过 partition 分区来提高并发消费速度。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210510/e785475b2eef698cecf6589d4bbd45dc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210510/e785475b2eef698cecf6589d4bbd45dc.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Logstash</h4>Logstash 提供三大功能：<br>
<ul><li>INPUT 进入</li><li>FILTER 过滤功能</li><li>OUTPUT 出去</li></ul><br>
<br>如果使用 Filter 功能的话，强烈推荐大家使用 <a href="https://grokdebug.herokuapp.com/">Grok debugger</a> 来预先解析日志格式。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210510/e99a67da30ad211458f85d8d744bb437.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210510/e99a67da30ad211458f85d8d744bb437.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
下载：<br>
<pre class="prettyprint">$ wget https://artifacts.elastic.co/downloads/logstash/logstash-6.2.4.tar.gz<br>
</pre><br>
解压重命名：<br>
<pre class="prettyprint">$ tar -zxvf logstash-6.2.4.tar.gz<br>
$ mv logstash-6.2.4 logstash<br>
</pre><br>
修改 Logstash 配置：<br>
<br>修改 Logstash 配置，使之提供 indexer 的功能，将数据插入到 Elasticsearch 集群中。<br>
<pre class="prettyprint">$ vim nginx.conf<br>
<br>
input &#123;<br>
kafka &#123;<br>
type => "kafka"<br>
bootstrap_servers => "192.168.0.1:2181,192.168.0.2:2181,192.168.0.3:2181"<br>
topics => "nginx"<br>
group_id => "logstash"<br>
consumer_threads => 2<br>
&#125;<br>
&#125;<br>
<br>
output &#123;<br>
elasticsearch &#123;<br>
host => ["192.168.0.1","192.168.0.2"，"192.168.0.3"]<br>
port => "9300"<br>
index => "nginx-%&#123;+YYYY.MM.dd&#125;"<br>
&#125;<br>
&#125; <br>
</pre><br>
启动 Logstash：<br>
<pre class="prettyprint">$ ./bin/logstash -f nginx.conf<br>
</pre><br>
<h4>Elasticsearch</h4>下载：<br>
<pre class="prettyprint">$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.4.tar.gz<br>
</pre><br>
解压：<br>
<pre class="prettyprint">$ tar -zxvf elasticsearch-6.2.4.tar.gz<br>
$ mv elasticsearch-6.2.4.tar.gz elasticsearch<br>
</pre><br>
修改配置：<br>
<pre class="prettyprint">$ vim config/elasticsearch.yml<br>
<br>
cluster.name: es <br>
node.name: es-node1<br>
network.host: 192.168.0.1<br>
discovery.zen.ping.unicast.hosts: ["192.168.0.1"]<br>
discovery.zen.minimum_master_nodes: 1<br>
</pre><br>
启动：<br>
<br>通过 -d 来后台启动。<br>
<pre class="prettyprint">$ ./bin/elasticsearch -d<br>
</pre><br>
打开网页 <a href="http://192.168.0.1:9200/" rel="nofollow" target="_blank">http://192.168.0.1:9200/</a>，如果出现下面信息说明配置成功。<br>
<pre class="prettyprint">&#123;<br>
name: "es-node1",<br>
cluster_name: "es",<br>
cluster_uuid: "XvoyA_NYTSSV8pJg0Xb23A",<br>
version: &#123;<br>
    number: "6.2.4",<br>
    build_hash: "ccec39f",<br>
    build_date: "2018-04-12T20:37:28.497551Z",<br>
    build_snapshot: false,<br>
    lucene_version: "7.2.1",<br>
    minimum_wire_compatibility_version: "5.6.0",<br>
    minimum_index_compatibility_version: "5.0.0"<br>
&#125;,<br>
tagline: "You Know, for Search"<br>
&#125; <br>
</pre><br>
控制台：<br>
<br>Cerebro 这个名字大家可能觉得很陌生，其实过去它的名字叫 kopf ！因为 Elasticsearch 5.0 不再支持 site plugin，所以 kopf 作者放弃了原项目，另起炉灶搞了 cerebro，以独立的单页应用形式，继续支持新版本下 Elasticsearch 的管理工作。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210510/577e9b9234170fe5bf252fc7732247dc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210510/577e9b9234170fe5bf252fc7732247dc.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
注意点：<br>
<ol><li>Master 与 Data 节点分离，当 Data 节点大于 3 个的时候，建议责任分离，减轻压力</li><li>Data Node 内存不超过 32G ，建议设置成 31 G ，具体原因可以看：<a href="https://blog.51cto.com/13527416/2051506" rel="nofollow" target="_blank">https://blog.51cto.com/13527416/2051506</a></li><li>discovery.zen.minimum_master_nodes 设置成（total / 2 + 1），避免脑裂情况</li><li>最重要的一点，不要将 ES 暴露在公网中，建议都安装 X-PACK ，来加强其安全性</li></ol><br>
<br><h4>kibana</h4>下载：<br>
<pre class="prettyprint">$ wget https://artifacts.elastic.co/downloads/kibana/kibana-6.2.4-darwin-x86_64.tar.gz<br>
</pre><br>
解压：<br>
<pre class="prettyprint">$ tar -zxvf kibana-6.2.4-darwin-x86_64.tar.gz<br>
$ mv kibana-6.2.4-darwin-x86_64.tar.gz kibana<br>
</pre><br>
修改配置：<br>
<pre class="prettyprint">$ vim config/kibana.yml<br>
<br>
server.port: 5601<br>
server.host: "192.168.0.1"<br>
elasticsearch.url: "http://192.168.0.1:9200"<br>
</pre><br>
启动 Kibana：<br>
<pre class="prettyprint">$ nohup ./bin/kibana &<br>
</pre><br>
界面展示：<br>
<br>创建索引页面需要到 <strong>Management -> Index Patterns</strong> 中通过前缀来指定。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210510/e2e58872c448ab813030bded981fcb1c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210510/e2e58872c448ab813030bded981fcb1c.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
最终效果展示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210510/a1c408072a9f3cd4a4f3713337b0edae.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210510/a1c408072a9f3cd4a4f3713337b0edae.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>总结</h3>综上，通过上面部署命令来实现 ELK 的整套组件，包含了日志收集、过滤、索引和可视化的全部流程，基于这套系统实现分析日志功能。同时，通过水平扩展 Kafka、Elasticsearch 集群，可以实现日均亿级的日志实时处理。<br>
<br>原文链接：<a href="https://blog.51cto.com/u_13527416/2117141" rel="nofollow" target="_blank">https://blog.51cto.com/u_13527416/2117141</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            