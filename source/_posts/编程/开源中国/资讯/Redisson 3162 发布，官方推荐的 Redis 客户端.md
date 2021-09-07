
---
title: 'Redisson 3.16.2 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2185'
author: 开源中国
comments: false
date: Tue, 07 Sep 2021 07:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2185'
---

<div>   
<div class="content">
                                                                                            <p>Redisson 3.16.2 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的官方推荐。</p> 
<p>此版本更新内容如下：</p> 
<p><strong>Feature </strong></p> 
<ul> 
 <li>Micronaut 3.0 集成</li> 
 <li>在<code>RLiveObjectService</code>接口中添加了 batched<code>merge()</code>方法</li> 
 <li>在 Redis Cluster 拓扑结构中使用主机名解析</li> 
 <li>在 Redis Sentinel 拓扑结构中使用主机名解析</li> 
 <li>在 RDeque、RdequeRx 和 RdequeReactive 接口中添加了批处理的 addLast() 和 addFirst() 方法。</li> 
 <li>为 RSet、RSetRx 和 RSetReactive 接口添加了 addAllCounted() 和 removeAllCounted() 方法。</li> 
</ul> 
<p><strong>Fixed </strong></p> 
<ul> 
 <li>不完全支持带有 MINID 策略的 Redis Stream trim 命令</li> 
 <li>Quarkus 在本机图像执行期间需要<code>AutowiredAnnotationBeanPostProcessor</code>类</li> 
 <li>Quarkus Netty 依赖项的问题</li> 
 <li>在 Redis Cluster 中检测到的<code>MOVED redirection loop detected</code>错误</li> 
 <li>处理 Redis Cluster 拓扑中带有空插槽的主节点</li> 
 <li>SentinelConnectionManager 应该对 IPv6 使用统一压缩格式</li> 
 <li><code>RLocalCachedMap.readAllValues()</code>方法使用 key decoder 而不是 value</li> 
 <li>传递给<code>RKeys.delete()</code>方法的空数组导致线程阻塞</li> 
 <li>没有地址的集群分区导致 NPE</li> 
 <li>等待<code>RSemaphore</code>许可获取的 reads 在许可添加时无法获取。</li> 
 <li><code>RRateLimiter</code>允许 limit overcome</li> 
 <li><code>RMapCacheReactive</code>和<code>RMapCacheRx</code>接口缺少定义驱逐算法的方法</li> 
 <li>在 Redisson<code>shutdown()</code>方法调用后，writ-behind 任务没有被刷新。</li> 
 <li>带有索引字段的 LiveObjects 不能使用批处理持久化方法进行存储</li> 
 <li>在 Redis Cluster 拓扑扫描中不应该跳过失败的主站</li> 
 <li>带过滤器的<code>RListReactive</code>迭代器返回不确定结果</li> 
 <li>如果使用主机名定义的节点，<code>replicatedServers</code>模式应该使用 ip 地址</li> 
 <li><code>replicatedServers</code>模式的多个 masters check 被移除</li> 
 <li><code>MapWriter</code>应该与 writeBehind 设置一起定义</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.16.2" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.16.2</a></p>
                                        </div>
                                      
</div>
            