
---
title: '京东到家Loki日志系统实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/d71e9f6e5e0f53a3631ba3702349d7c6.png'
author: Dockone
comments: false
date: 2021-09-22 13:16:54
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/d71e9f6e5e0f53a3631ba3702349d7c6.png'
---

<div>   
<br><h3>背景</h3>随着业务的高速发展，目前基于ELK架构的日志系统无法满足京东到家的日志存储和查询需求。这是因为ELK架构中要用全文索引来支撑搜索服务，需要为日志的原文建立反向索引，这会导致最终存储数据相较原始内容成倍增长，产生较高的存储成本。不管数据将来是否会被搜索，都会在写入时因为索引操作而占用大量的计算资源，这对于日志这种写多读少的服务也是一种计算资源的浪费。另外日志采集无法自动化，新的日志需要运维手动加入。针对这些痛点，我们调研了当前流行的日志系统，最终选择了Loki这个新兴日志系统作为ELK架构日志系统的替代。<br>
<br>以下是根据ELK与Loki优缺点进行对比。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210917/d71e9f6e5e0f53a3631ba3702349d7c6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/d71e9f6e5e0f53a3631ba3702349d7c6.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Loki日志系统</h3>Loki是Grafana Labs团队最新的开源项目，是一个水平可扩展，高可用性，多租户的日志聚合系统。设计经济高效且易于操作，它不会为日志内容编制索引，而是为每个日志流编制一组标签。<br>
<br>Loki日志系统由以下3个部分组成：<br>
<ul><li>Loki是主服务器，负责存储日志和处理查询。</li><li>Promtail是专为Loki定制的客户端，负责收集日志并将其发送Loki。</li><li>Grafana用于UI展示（可以自己开发前端页面来替代）。</li></ul><br>
<br><h4>Loki架构</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210917/7a0eaecead870c03d62423e43117017a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/7a0eaecead870c03d62423e43117017a.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>Promtail开源客户端负责采集并上报日志；</li><li>Distributor：日志写入入口，将数据转发到Ingester；</li><li>Ingester：日志的写入服务，缓存并写入日志内容和索引到底层存储；</li><li>Querier：日志读取服务，执行搜索请求。</li></ul><br>
<br><strong>Distributor</strong><br>
<br>Promtail收集日志并将其发送给Loki，Distributor就是第一个接收日志的组件。由于日志的写入量可能很大，所以不能在它们传入时就将它们写入存储中，需要批处理和压缩数据。Loki通过构建压缩数据块来实现这一点，方法是在日志进入时对其进行gzip操作，组件ingester是一个有状态的组件，负责构建和刷新chunck，当chunk达到一定的数量或者时间后，刷新到存储中去。每个流的日志对应一个ingester，当日志到达Distributor后，根据元数据和hash算法计算出应该到哪个ingester上面。<br>
<br><strong>Ingester</strong><br>
<br>接收到日志并开始构建chunk，基本上就是将日志进行压缩并附加到chunk上面。一旦chunk“填满”（数据达到一定数量或者过了一定期限），ingester将其刷新到数据库。对块和索引使用单独的数据库，因为它们存储的数据类型不同。<br>
<br>刷新一个chunk之后，ingester然后创建一个新的空chunk并将新条目添加到该chunk中。<br>
<br><strong>Querier</strong><br>
<br>读取就非常简单了，由Querier负责给定一个时间范围和标签选择器，Querier查看索引以确定哪些块匹配，并通过greps将结果显示出来。它还从Ingester获取尚未刷新的最新数据。<br>
<br>对于每个查询，一个查询器将为您显示所有相关日志。实现了查询并行化，提供分布式grep，使即使是大型查询也是足够的。<br>
<h4>Loki读写组件</h4><strong>写数据</strong><br>
<br>日志数据的写主要依托的是Distributor和Ingester两个组件，整体流程如下：<br>
<ol><li>Distributor收到HTTP请求，用于存储流数据</li><li>通过hash环对数据流进行hash</li><li>Distributor将数据流发送到对应的Ingester及其副本上</li><li>Ingester新建Chunk或将数据追加到已有Chunk上</li><li>Distributor通过HTTP连接发送响应信息</li></ol><br>
<br><strong>读数据</strong><br>
<ol><li>Querier收到HTTP请求（来自Granfana或者自己开发的前端）</li><li>Querier将请求发送至Ingester用以获取内存数据</li><li>Ingester收到请求后返回符合条件的数据</li><li>如果没有Ingester返回数据，Querier从后端存储加载数据并执行查询</li><li>Querier遍历所有数据并进行去重处理，通过HTTP连接返回最终结果</li></ol><br>
<br><h4>Loki查询语法</h4><strong>选择器</strong><br>
<br>对于查询表达式的标签部分，将放在&#123;&#125;中，多个标签表达式用逗号分隔：<br>
<br>&#123;app="mysql",name="mysql-backup"&#125;<br>
<br>支持的符号有：<br>
<ul><li>=  完全相同。</li><li>!=  不平等。</li><li>=~  正则表达式匹配。</li><li>!~  不要正则表达式匹配</li></ul><br>
<br><strong>过滤表达式</strong><br>
<br>编写日志流选择器后，您可以通过编写搜索表达式进一步过滤结果。搜索表达式可以文本或正则表达式。<br>
<br>如：&#123;job=“mysql”&#125; |= “error”<br>
<br>支持多个过滤：&#123;job=“mysql”&#125; |= “error” !=“timeout”<br>
<br>目前支持的操作符：<br>
<ul><li>|= line包含字符串。</li><li>!= line不包含字符串。</li><li>|~ line匹配正则表达式。</li><li>!~ line与正则表达式不匹配</li></ul><br>
<br><h3>京东到家应用日志系统</h3>到家运维部基于loki日志系统，开发出到家应用日志分析平台。具体的技术方案如下：<br>
<ul><li>前端UI  ：官方是使用Grafana进行前端展示，我们使用python/flask开发前端页面，整合到运维管理平台中。</li><li>后端存储选择Cassandra分布式存储系统，可以横向扩容。</li><li>研发在页面自定义要收集的日志文件，利用Promtail文件发现机制自动进行日志收集。</li><li>支持实时展示日志内容，以及对历史日志文件进行自定义搜索。</li></ul><br>
<br><h4>架构图</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210917/baba3fb7ec0c69c1dffd08204e8c979a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/baba3fb7ec0c69c1dffd08204e8c979a.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>日志接入</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210917/77b51d29e2237c2499655b921cce9425.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/77b51d29e2237c2499655b921cce9425.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>选择应用、主机，输入自定义的日志文件。</li><li>调用应用服务器上的SaltStack管理客户端，将待采集日志文件路径写入主机Promtail日志采集客户端对应文件中</li><li>利用PPromtail文件自动发现机制，发现新加入的日志，将日志采集发送到Loki server</li></ul><br>
<br><h4>实时日志</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210917/5f197eae378cf72f667306dfe154eaff.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/5f197eae378cf72f667306dfe154eaff.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
调用Loki API通过WebSocket实时展示日志内容。<br>
<h4>历史日志</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210917/49d015d3a090d2e872daa75321c5fd03.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/49d015d3a090d2e872daa75321c5fd03.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
选择应用，主机及日志，输入多个关键字进行内容过滤，多个关键字中间使用空格间隔。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210917/de51fdd6002dc0c33220307a5bc527d1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/de51fdd6002dc0c33220307a5bc527d1.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在实际生产环境中（1台48核/256G内存/12*6T sata硬盘的存储型物理机）对10T数据进行多关键字、多日志文件进行查询，5s内返回查询结果。<br>
<h4>技术难点</h4><ul><li>日志路径采用文件监听技术，配置日志路径更加灵活，不需要重新启动客户端。</li><li>采用分布式数据存储Cassandra，可以横向扩容。</li><li>实时日志采用WebSocket技术实现。</li><li>在所有服务器部署Promtail客户端工作量比较大，我们采用将客户端打包到操作系统镜像中，这样新的机器无需再安装客户端。</li></ul><br>
<br><h4>配置文件示例</h4>下面是到家的Loki相关配置文件，供大家参考。<br>
<pre class="prettyprint">LokiServer配置：<br>
auth_enabled: false  #关闭认证，对数据来源客户端不做认证<br>
server:<br>
http_listen_port: 3101  #loki http端口 <br>
ingester:<br>
lifecycler:<br>
address: 127.0.0.1   #ingester地址，默认为本机127.0.0.1，如果有多台server也可以写多个<br>
ring:<br>
  kvstore:<br>
    store: inmemory  #使用内存做为ingester存储<br>
  replication_factor: 1<br>
     final_sleep: 0s<br>
chunk_idle_period: 5m #在没有更新之前chunk在内存中的时间<br>
chunk_retain_period: 30s  #刷新后应在内存中保留多长时间  <br>
storage_config:#存储配置<br>
cassandra:#使用Cassandra<br>
addresses: x.x.x.x #cassandra的IP<br>
keyspace: lokiindex  #cassandra的keyspace<br>
auth: false    #关闭Cassandra认证 <br>
schema_config:<br>
configs:<br>
- from: 2020-07-01<br>
 store: cassandra   #数据存储方式为Cassandra   <br>
 object_store: cassandra<br>
 schema: v11<br>
 index:<br>
   prefix: index_  #index表的前缀<br>
   period: 168h   #index每张表的时间范围7天<br>
 chunks:<br>
   prefix: chunk_  #chunks表的前缀<br>
   period: 168h  #chunks每张表的时间范围7天 <br>
limits_config:<br>
ingestion_rate_mb: 50 #每个用户每秒的采样率限制<br>
enforce_metric_name: false<br>
reject_old_samples: true<br>
reject_old_samples_max_age:168h <br>
chunk_store_config:<br>
# 最大可查询历史日期 7天<br>
max_look_back_period: 168h <br>
# 表的保留期7天<br>
table_manager:<br>
retention_deletes_enabled: true  #超过retention_period时间历史数据可以删除<br>
retention_period: 168h<br>
<h1>Promtail客户端:</h1>server:<br>
http_listen_port: 0 #http端口，为0表示端口随机<br>
grpc_listen_port: 0 #grpc端口，为0表示端口随机  <br>
# Positions<br>
positions:<br>
filename:/export/servers/promtail/tmp/positions.yaml #记录采集的文件路径与日志采集位置 <br>
# Loki服务器的地址<br>
clients:<br>
- url:http://xx.xx.xxx/loki/api/v1/push <br>
scrape_configs:<br>
- job_name: daojia #job_name 用于标识抓取配置<br>
file_sd_configs:#用于文件发现<br>
   - files:<br>
        -'/export/servers/promtail/logpath.yaml'#具体文件<br>
     refresh_interval: 10s #文件检测间隔，当有新日志加入会自动发现并自动采集日志，无须客户端重启 <br>
- targets:<br>
- localhost  #收集的主机<br>
labels:<br>
host: 1.1.1.1 #给收集主机打标签host:1.1.1.1<br>
log: gw           #给收集主机打标签log: gw<br>
__path__:/export/servers/nginx/logs/gw.o2o.jd.local/gw.o2o.jd.local_access.log          #要收集的日志路径<br>
</pre><br>
<h3>总结及规划</h3>目前已经有1000多台应用服务器的日志收集到了基于Loki的到家日志系统中，每天的日志量占用空间才1.4T，原来在ES中，这么多的日志量需要近30T的存储空间，极大节省了硬件成本。而且根据前端研发提交过来的日志名称，可以自动化日志收集，减少了运维日志相关的手工操作，提高了运维的工作效率。<br>
<br>整个日志平台只使用了1台48核/256G内存/12*6T sata硬盘的存储型物理机，Loki server和Cassandra存储都部署在这台机器上。后续日志客户端接入量增加后，  Loki server可以通过增加节点进行扩容，提高日志接收能力。后端存储Cassandra也可以通过增加Cassandra集群节点来横向扩容。另外前端展示方面，后续要针对搜索结果进一步分析处理和展示。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/-IvWfhXbm3WXFIBtbrhX-A" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/-IvWfhXbm3WXFIBtbrhX-A</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            