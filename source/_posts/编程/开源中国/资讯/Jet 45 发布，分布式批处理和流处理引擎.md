
---
title: 'Jet 4.5 发布，分布式批处理和流处理引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2382'
author: 开源中国
comments: false
date: Fri, 23 Apr 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2382'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Jet 是一个开源的、内存中的、分布式批处理和流处理引擎。你可以用它来处理大量的实时事件或大批量的静态数据集。为了给人一种规模感，Jet 的一个节点已经被证明可以每秒聚集1000万个事件，延迟低于10毫秒。</p> 
<h4>新功能：</h4> 
<ul> 
 <li>[sql] 动态 <code>ClassDefinition</code> 消除了在 IMap 中使用新的记录类型时重新启动集群的需要；</li> 
</ul> 
<h4>增强：</h4> 
<ul> 
 <li>[jdbc] 添加了一个选项，用于配置 JDBC Sink 的批处理大小；</li> 
 <li>[sql] 优化了 SQL 聚合的内存占用；</li> 
 <li>[sql] 现在你可以在 SQL 生成器函数中使用表达式了；</li> 
 <li>[核心]从 IMap/ICache 中提取数据可能会由于同时创建过多的分区迭代器而导致 OOME；</li> 
 <li>[核心] 删除了因工作被取消而发生的错误的误导性记录；</li> 
 <li>[pipeline-api] 大大提高了滑动窗口中 <code>pickAny</code> 聚合操作的性能；</li> 
</ul> 
<h4>修复：</h4> 
<ul> 
 <li>[core]Jet 与 Java Logging Framework 的集成导致它无意中从关机 hook 中关闭了 <code>System.out</code>，这将破坏其他关机 hook；</li> 
 <li>[core] 修复了 <code>DAG.toDotString()</code>，以显示正确的队列大小；</li> 
 <li>[sql] <code>CREATE MAPPING</code> 语法有一个漏洞，你可以在同一语句中同时使用 <code>OR REPLACE</code> 和 <code>IF NOT EXISTS</code> ；</li> 
 <li>[cdc]在 CDC 源中实施已处理的偏移反馈；</li> 
 <li>[extensions] 更新 AWS SDK 版本至 1.11.976；</li> 
 <li>[extensions] 更新 Guava 版本至 30.1；</li> 
 <li>[extensions] 更新 Parquet 版本到 1.12.0；</li> 
 <li>[extensions] 更新 Avro 到 1.10.2；</li> 
 <li>[extensions] 更新 Jetty 版本至 9.4.38.v20210224；</li> 
 <li>[extensions] 更新 wildfly-openssl 到 1；</li> 
 <li>[extensions] 更新 ElasticSearch-6 到 6.8.14；</li> 
 <li>[extensions] 更新 ElasticSearch-7 至 7.10.0；</li> 
 <li>[extensions] 更新 Kafka 版本到 2.2.2；</li> 
 <li>[extensions] 更新 MySql Connector 至 8.0.20；</li> 
 <li>[extensions] 更新 Apache Http Client 至 4.5.13；</li> 
 <li>[extensions] 更新 Netty 至 4.1.61.Final；</li> 
 <li>[extensions] 更新 Snakeyaml 版本至 1.26 [SEC-71]；</li> 
</ul> 
<h4>重大变化：</h4> 
<ul> 
 <li><code>DAG.toDotString(int defaultParallelism)</code> 方法签名现在为 <code>DAG.toDotString(int defaultLocalParallelism, int defaultQueueSize)</code>。调用者现在必须提供队列大小，如果不在边缘上重写，则将被显示。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhazelcast%2Fhazelcast-jet%2Freleases%2Ftag%2Fv4.5" target="_blank">https://github.com/hazelcast/hazelcast-jet/releases/tag/v4.5</a></p>
                                        </div>
                                      
</div>
            