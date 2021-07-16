
---
title: 'Loki生产环境集群方案'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/1831948ceb77e31a7e142dff6364a852.png'
author: Dockone
comments: false
date: 2021-07-16 15:07:47
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/1831948ceb77e31a7e142dff6364a852.png'
---

<div>   
<br>很多新入坑Loki的小伙伴当看到distributor、ingester、querier以及各种依赖的三方存储时，往往都比较懵逼，不知道从哪儿入手。此外再加上官方的文档里面对于集群部署的粗浅描述，更是让新手们大呼部署太难。其实，除了官方的helm外，藏在Loki仓库的production目录里面有一篇生产环境的集群部署模式。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/1831948ceb77e31a7e142dff6364a852.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/1831948ceb77e31a7e142dff6364a852.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
原文里面，社区采用的是docker-compose的方式来快速拉起一套Loki集群。虽然我们正式在生产环境中实施时，不会傻到用docker-compose部署在一个node上（显然这里我们强行不考虑docker-swarm）。不过里面关于Loki的架构和配置文件却值得我们学习。<br>
<br>那么，与纯分布式的Loki集群相比，这套方案有什么特别的呢？首先我们先来看看下面这张图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/e6cfde429965e188d3a01945e2bba631.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/e6cfde429965e188d3a01945e2bba631.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到，最明显的有三大不同点：<br><br>
<ol><li>Loki核心服务distributor、ingester、querier没有分离，而是启动在一个实例当中；</li><li>抛弃了Consul和etcd外部的KV存储，而是直接用memberlist在内存中维护集群状态；</li><li>使用boltdb-shipper替代其他日志索引方案</li></ol><br>
<br>这样看起来，Loki集群的整体架构就比较清晰，且更少的依赖外部系统。简单总结了下，除了用于存储chunks和index而绕不开的S3存储外，还需要一个缓存服务用于加速日志查询和写入。<br>
<br><blockquote><br>Loki2.0版本之后，对于使用boltdb存储索引部分做了较大的重构，采用新的boltdb-shipper模式，可以让Loki的索引存储在S3上，而彻底摆脱Cassandra或者谷歌的BigTable。此后服务的横向扩展将变得更加容易。关于bolt-shipper的更多细节，可以参考：<a href="https://grafana.com/docs/loki/latest/operations/storage/boltdb-shipper/" rel="nofollow" target="_blank">https://grafana.com/docs/loki/ ... pper/</a></blockquote>说得这么玄乎，那我们来看看这套方案的配置有哪些不一样呢？<br>
<h3>原生部分</h3><h4>memberlist</h4><pre class="prettyprint">memberlist:  <br>
join_members: ["loki-1", "loki-2", "loki-3"]  <br>
dead_node_reclaim_time: 30s  <br>
gossip_to_dead_nodes_time: 15s  <br>
left_ingesters_timeout: 30s  <br>
bind_addr: ['0.0.0.0']  <br>
bind_port: 7946  <br>
</pre><br>
Loki的memberlist使用的是gossip协议来让集群内的所有节点达到最终一致性的。此部分的配置几乎都是协议频率和超时的控制，保持默认的就好<br>
<h4>ingester</h4><pre class="prettyprint">ingester:  <br>
lifecycler:  <br>
join_after: 60s  <br>
observe_period: 5s  <br>
ring:  <br>
  replication_factor: 2  <br>
  kvstore:  <br>
    store: memberlist  <br>
final_sleep: 0s <br>
</pre><br>
ingester的状态通过gossip协议同步到集群的所有member当中，同时让ingester的复制因子为2。即一个日志流同时写入到两个ingster服务当中以保证数据的冗余。<br>
<h3>扩展部分</h3>社区的集群模式配置原生部分仍然显得不太够意思，除了memberlist的配置稍显诚意外，其它部分仍然不够我们对生产环境的要求。这里小白简单改造了一下，分享给大家。<br>
<h4>storage</h4>将index和chunks的存储统一让S3对象存储纳管，让Loki彻底摆脱三方依赖。<br>
<pre class="prettyprint">schema_config:  <br>
configs:  <br>
- from: 2021-04-25  <br>
store: boltdb-shipper  <br>
object_store: aws  <br>
schema: v11  <br>
index:  <br>
  prefix: index_  <br>
  period: 24h  <br>
<br>
storage_config:  <br>
boltdb_shipper:  <br>
shared_store: aws  <br>
active_index_directory: /loki/index  <br>
cache_location: /loki/boltdb-cache  <br>
aws:  <br>
s3: s3://<S3_ACCESS_KEY>:<S3_SECRET_KEY>@<S3_URL>/<S3__BUCKET>    <br>
s3forcepathstyle: true  <br>
insecure: true<br>
</pre><br>
这里值得说明的就是用于存储日志流索引的是bolt_shipper，它是可以通过共享存储方式写到s3当中的。那么<code class="prettyprint">active_index_directory</code>就是S3上的Bucket路径，<code class="prettyprint">cache_location</code>则为Loki本地bolt索引的缓存数据。<br>
<br><blockquote><br>事实上ingester上传到s3的index路径为<code class="prettyprint">&lt;S3__BUCKET>/index/</code></blockquote><h4>Redis</h4>原生的方案里并不提供缓存，这里我们引入Redis来做查询和写入的缓存。对于很多小伙伴纠结的是一个Redis共用还是多个Redis单独使用，这个看你集群规模，不大的情况下，一个Redis实例足以满足需求。<br>
<pre class="prettyprint">query_range:  <br>
results_cache:  <br>
cache:  <br>
  redis:  <br>
    endpoint: redis:6379  <br>
    expiration: 1h  <br>
cache_results: true  <br>
<br>
index_queries_cache_config:  <br>
redis:  <br>
endpoint: redis:6379  <br>
expiration: 1h  <br>
<br>
chunk_store_config:  <br>
chunk_cache_config:  <br>
redis:  <br>
  endpoint: redis:6379  <br>
  expiration: 1h      <br>
write_dedupe_cache_config:  <br>
redis:  <br>
  endpoint: redis:6379  <br>
  expiration: 1h  <br>
</pre><br>
<h4>ruler</h4>既然Loki以及做了集群化部署，当然ruler这个服务也得跟在切分。难以接受的是，社区这部分的配置竟然是缺失的。所以我们得自己补充完整。我们知道日志的ruler可以写在S3对象存储上，同时每个ruler实例也是通过一致性哈希环来分配自己的rules。所以这部分配置，我们可以如下参考：<br>
<pre class="prettyprint">ruler:  <br>
storage:  <br>
type: s3  <br>
s3:  <br>
  s3: s3://<S3_ACCESS_KEY>:<S3_SECRET_KEY>@<S3_URL>/<S3_RULES_BUCKET>  <br>
  s3forcepathstyle: true  <br>
  insecure: true  <br>
  http_config:  <br>
    insecure_skip_verify: true  <br>
enable_api: true  <br>
enable_alertmanager_v2: true  <br>
alertmanager_url: "http://<alertmanager>"  <br>
ring:  <br>
  kvstore:  <br>
  store: memberlist<br>
</pre><br>
<h4>支持Kubernetes</h4>最后，最最最重要的是要让官方的Loki集群方案支持在Kubernetes中部署，否则一切都是瞎扯。由于篇幅的限制，我将manifest提交到GitHub上，大家直接clone到本地部署。<br>
<br>GitHub地址：<a href="https://github.com/CloudXiaobai/loki-cluster-deploy/tree/master/production/loki-system" rel="nofollow" target="_blank">https://github.com/CloudXiaoba ... ystem</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210716/7cae39f0c0d4886e457035dcba50d81a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210716/7cae39f0c0d4886e457035dcba50d81a.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这个manifest只依赖一个S3对象存储，所以你在部署到生产环境时，请务必预先准备好对象存储的AccessKey和SecretKey。将他们配置到installation.sh当中后，直接执行脚本就可以开始安装了。<br>
<br><blockquote><br>文件中的ServiceMonitor是为Loki做的Prometheus Operator的Metrics服务发现，你可以自己选择是否部署。</blockquote><h3>总结</h3>本文介绍了官方提供的一种Loki生产环境下的集群部署方案，并在此基础上加入了一些诸如缓存、S3对象存储的扩展配置，并将官方的docker-compose部署方式适配到Kubernetes当中。官方提供的方案有效的精简了Loki分布式部署下复杂的结构，值得我们学习。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/qnt7JUzHLUU6Qs_tv5V0Hw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/qnt7JUzHLUU6Qs_tv5V0Hw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            