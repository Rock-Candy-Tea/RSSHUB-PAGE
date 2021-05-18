
---
title: 'Loki生产环境集群方案'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51dc87b179304ac784a8f7914ff5659e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 18:33:56 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51dc87b179304ac784a8f7914ff5659e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>很多新入坑Loki的小伙伴当看到distributor、ingester、querier以及各种依赖的三方存储时，往往都比较懵逼，不知道从哪儿入手。此外再加上官方的文档里面对于集群部署的粗浅描述，更是让新手们大呼部署太难。其实，除了官方的helm外，藏在Loki仓库的production目录里面有一篇生产环境的集群部署模式。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51dc87b179304ac784a8f7914ff5659e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
原文里面，社区采用的是docker-compose的方式来快速拉起一套Loki集群。虽然我们正式在生产环境中实施时，不会傻到用docker-compose部署在一个node上（显然这里我们强行不考虑docker-swarm）。不过里面关于Loki的架构和配置文件却值得我们学习。</p>
<p>那么，与纯分布式的Loki集群相比，这套方案有什么特别的呢？首先我们先来看看下面这张图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af733930a05c43608a20215f452b47ca~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，最明显的有三大不同点：</p>
<ol>
<li>loki核心服务distributor、ingester、querier没有分离，而是启动在一个实例当中；</li>
<li>抛弃了consul和etcd外部的kv存储，而是直接用memberlist在内存中维护集群状态；</li>
<li>使用boltdb-shipper替代其他日志索引方案</li>
</ol>
<p>这样看起来，Loki集群的整体架构就比较清晰，且更少的依赖外部系统。简单总结了下，除了用于存储chunks和index而绕不开的S3存储外，还需要一个缓存服务用于加速日志查询和写入。</p>
<blockquote>
<p>Loki2.0版本之后，对于使用boltdb存储索引部分做了较大的重构，采用新的boltdb-shipper模式，可以让Loki的索引存储在S3上，而彻底摆脱Cassandra或者谷歌的BigTable。此后服务的横向扩展将变得更加容易。关于bolt-shipper的更多细节，可以参考：<a href="https://grafana.com/docs/loki/latest/operations/storage/boltdb-shipper/" target="_blank" rel="nofollow noopener noreferrer">grafana.com/docs/loki/l…</a></p>
</blockquote>
<p>说得这么玄乎，那我们来看看这套方案的配置有哪些不一样呢？</p>
<h2 data-id="heading-0">原生部分</h2>
<h4 data-id="heading-1">memberlist</h4>
<pre><code class="copyable">memberlist:
  join_members: ["loki-1", "loki-2", "loki-3"]
  dead_node_reclaim_time: 30s
  gossip_to_dead_nodes_time: 15s
  left_ingesters_timeout: 30s
  bind_addr: ['0.0.0.0']
  bind_port: 7946
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Loki的memberlist使用的是gossip协议来让集群内的所有节点达到最终一致性的。此部分的配置几乎都是协议频率和超时的控制，保持默认的就好</p>
<h4 data-id="heading-2">ingester</h4>
<pre><code class="copyable">ingester:
  lifecycler:
    join_after: 60s
    observe_period: 5s
    ring:
      replication_factor: 2
      kvstore:
        store: memberlist
    final_sleep: 0s
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ingester的状态通过gossip协议同步到集群的所有member当中，同时让ingester的复制因子为2。即一个日志流同时写入到两个ingster服务当中以保证数据的冗余。</p>
<h2 data-id="heading-3">扩展部分</h2>
<p>社区的集群模式配置原生部分仍然显得不太够意思，除了memberlist的配置稍显诚意外，其它部分仍然不够我们对生产环境的要求。这里小白简单改造了一下，分享给大家。</p>
<h4 data-id="heading-4">storage</h4>
<p>将index和chunks的存储统一让S3对象存储纳管，让Loki彻底摆脱三方依赖。</p>
<pre><code class="copyable">schema_config:
  configs:
  - from: 2021-04-25
    store: boltdb-shipper
    object_store: aws
    schema: v11
    index:
      prefix: index_
      period: 24h
    
storage_config:
  boltdb_shipper:
    shared_store: aws
    active_index_directory: /loki/index
    cache_location: /loki/boltdb-cache
  aws:
    s3: s3://<S3_ACCESS_KEY>:<S3_SECRET_KEY>@<S3_URL>/<S3__BUCKET>  
    s3forcepathstyle: true
    insecure: true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里值得说明的就是用于存储日志流索引的是bolt_shipper，它是可以通过共享存储方式写到s3当中的。那么<code>active_index_directory</code>就是S3上的Bucket路径，<code>cache_location</code>则为Loki本地bolt索引的缓存数据。</p>
<blockquote>
<p>事实上ingester上传到s3的index路径为<code><S3__BUCKET>/index/</code></p>
</blockquote>
<h4 data-id="heading-5">redis</h4>
<p>原生的方案里并不提供缓存，这里我们引入redis来做查询和写入的缓存。对于很多小伙伴纠结的是一个redis共用还是多个redis单独使用，这个看你集群规模，不大的情况下，一个redis实例足以满足需求。</p>
<pre><code class="copyable">query_range:
  results_cache:
    cache:
      redis:
        endpoint: redis:6379
        expiration: 1h
  cache_results: true

index_queries_cache_config:
  redis:
    endpoint: redis:6379
    expiration: 1h
    
chunk_store_config:
  chunk_cache_config:
    redis:
      endpoint: redis:6379
      expiration: 1h    
  write_dedupe_cache_config:
    redis:
      endpoint: redis:6379
      expiration: 1h
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">ruler</h4>
<p>既然Loki以及做了集群化部署，当然ruler这个服务也得跟在切分。难以接受的是，社区这部分的配置竟然是缺失的。所以我们得自己补充完整。我们知道日志的ruler可以写在S3对象存储上，同时每个ruler实例也是通过一致性哈希环来分配自己的rules。所以这部分配置，我们可以如下参考：</p>
<pre><code class="copyable">ruler:
  storage:
    type: s3
    s3:
      s3: s3://<S3_ACCESS_KEY>:<S3_SECRET_KEY>@<S3_URL>/<S3_RULES_BUCKET>
      s3forcepathstyle: true
      insecure: true
      http_config:
        insecure_skip_verify: true
    enable_api: true
    enable_alertmanager_v2: true
    alertmanager_url: "http://<alertmanager>"
    ring:
      kvstore:
      store: memberlist
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">支持kubernetes</h4>
<p>最后，最最最重要的是要让官方的Loki集群方案支持在Kubernetes中部署，否则一切都是瞎扯。由于篇幅的限制，我将manifest提交到github上，大家直接clone到本地部署。</p>
<p>GitHub地址： <a href="https://github.com/CloudXiaobai/loki-cluster-deploy/tree/master/production/loki-system" target="_blank" rel="nofollow noopener noreferrer">github.com/CloudXiaoba…</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91756b4ef070402ab7404fc2f72d94a9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个manifest只依赖一个S3对象存储，所以你在部署到生产环境时，请务必预先准备好对象存储的AccessKey和SecretKey。将他们配置到installation.sh当中后，直接执行脚本就可以开始安装了。</p>
<blockquote>
<p>文件中的ServiceMonitor是为Loki做的Prometheus Operator的Metrics服务发现，你可以自己选择是否部署</p>
</blockquote>
<h2 data-id="heading-8">总结</h2>
<p>本文介绍了官方提供的一种Loki生产环境下的集群部署方案，并在此基础上加入了一些诸如缓存、S3对象存储的扩展配置，并将官方的docker-compose部署方式适配到Kubernetes当中。官方提供的方案有效的精简了Loki分布式部署下复杂的结构，值得我们学习。</p>
<hr>
<p>「云原生小白」</p></div>  
</div>
            