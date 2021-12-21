
---
title: 'Jedis 4.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7532'
author: 开源中国
comments: false
date: Tue, 21 Dec 2021 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7532'
---

<div>   
<div class="content">
                                                                                            <p>Jedis 是 Redis 的一个 Java 客户端库，旨在提高性能和易用性。Jedis 与 redis 2.8.x、3.xx 及更高版本完全兼容。</p> 
<h3>新功能</h3> 
<ul> 
 <li>引入 JedisPooled 
  <ul> 
   <li>JedisPool 的替代品，实现了与 JedisCluster 相同的接口，允许在 JedisCluster 和 JedisPooled 之间轻松切换。</li> 
  </ul> </li> 
 <li>引入 JedisSharding</li> 
 <li>引入 ClusterPipeline 和 ShardedPipeline</li> 
 <li>引入 ReliableTransaction</li> 
 <li>引入 UnifiedJedis</li> 
 <li>引入 ConnectionProvider 接口和一些实现</li> 
 <li>引入 CommandExecutor 接口和一些实现</li> 
 <li>增加了 RedisJSON 和 RedisJSON 2 命令</li> 
 <li>增加了 RediSearch 命令</li> 
 <li>……</li> 
</ul> 
<h3>变化</h3> 
<ul> 
 <li>具有 <code>GenericObjectPoolConfig<Jedis></code> 的 JedisCluster 构造函数现在接受 <code>GenericObjectPoolConfig<Connection></code></li> 
 <li>大多数 SortedSet 方法改为返回 Java <code>List</code> 而不是 <code>Set</code></li> 
 <li>许多方法现在返回原始值（long/boolean/double，而不是 Long/Boolean/Double）</li> 
 <li>ShardedJedisPool、Sharded、ShardedJedis、BinaryShardedJedis、ShardInfo、JedisShardInfo 类被移除</li> 
 <li>BinaryJedis 和 BinaryJedisCluster 类已被删除，这些类的方法可以分别在 Jedis 和 JedisCluster 类中使用</li> 
 <li>删除了 Client 和 BinaryClient 类</li> 
 <li><code>redis.client.jedis.commands</code> 包被重新实现，意味着 Commands 接口被重组</li> 
 <li>删除了 Sentinel 类</li> 
</ul> 
<h3>维护</h3> 
<ul> 
 <li>将依赖性 <code>org.slf4j:slf4j-api</code> 升级到 <code>1.7.32</code> 版本</li> 
 <li>添加了依赖性 <code>org.json:json</code> 版本 <code>20211205</code></li> 
 <li>添加了依赖性 <code>com.google.code.gson:gson</code> 版本 <code>2.8.9</code></li> 
</ul> 
<h3>更改列表</h3> 
<ul> 
 <li>通过替换无效的 JedisDataException 抛出 IllegalStateException</li> 
 <li>支持带有 TLS 的 Sentinel</li> 
 <li>删除 EVAL 和 EVALSHA 命令中无限超时的用法</li> 
 <li>避免 SetFromList 类的 NullPointException</li> 
 <li>JedisNoReachableClusterNodeException 应扩展 JedisClusterOperationException</li> 
 <li>从 Transaction 中移除 WATCH</li> 
 <li>JedisDataException 不应该被包裹在 Pool 操作中</li> 
 <li>删除 SYNC 命令</li> 
 <li>删除 ShardedJedisPipeline 类</li> 
 <li>删除 JedisPoolAbstract 类并隐藏 Pool.initPool() 方法</li> 
 <li>限制 Jedis 中 setDataSource 的访问</li> 
 <li>升级依赖关系</li> 
 <li>移除被保留的废弃内容</li> 
 <li>解决 XADD 冲突</li> 
 <li>使用 slf4j-simple 来替换 log4j 的实现</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Freleases%2Ftag%2Fv4.0.0" target="_blank">https://github.com/redis/jedis/releases/tag/v4.0.0</a></p>
                                        </div>
                                      
</div>
            