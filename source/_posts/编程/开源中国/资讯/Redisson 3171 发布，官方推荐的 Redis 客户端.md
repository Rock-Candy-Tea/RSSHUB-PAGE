
---
title: 'Redisson 3.17.1 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6583'
author: 开源中国
comments: false
date: Wed, 27 Apr 2022 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6583'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Redisson 3.17.1 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的官方推荐。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#24292f">Feature</span></strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">对 LiveObjects 的 transient fields 支持，以避免数据序列化</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">在 RTopic object 中添加了 removeAllListenersAsync() 方法</span></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#24292f">Improvement</span></strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">并行创建的连接数量减少到 5，以获得更好的稳定性</span></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#24292f">Fixed</span></strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">RedissonReactiveClient.getMultilock() 方法应接受 RLockReactive objects</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">RedissonRxClient.getMultilock() 方法应接受 RLockRx objects</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">在拓扑扫描期间不要关闭错误响应的连接</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">SET 命令应该是一个 empotent 操作</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">如果 host 未知，MasterSlaveConnectionManager 会抛出 ClassCastException</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">如果 writeLock 在 readLock 之前 released，那么两者都 acquired，RReadWriteLock 的更新就不起作用了</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">Spring Data Redis 模块。在集群模式下扫描，其他节点不能被扫描到</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">RReliableTopic object 抛出"attempt to compare nil with number"的错误</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">如果剩余等待时间为负数，RedissonSpinLock.tryLock() 方法会返回 false 而不是 true</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">如果批量使用 RMap 的 merge()、compute()、computeIfAbsent() 和 computeIfPresent()，应该抛出一个错误</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">无法在 CronSchedule object 中指定时区</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">RMapCache.destroy() 方法抛出 NPE</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">RLock.tryLock() 方法抛出了 CancellationException</span></li> 
 <li>无法连接到 Redis 服务器的错误由于 NPE 而被抛出</li> 
 <li>RBlockingQueue.pollLastAndOfferFirstTo() 在结果为空时抛出 ClassCastException</li> 
 <li>internal AsyncSemaphore 不会跳过同一线程中被取消的任务</li> 
 <li>RLocalCachedMap.getAll() 方法不遵循 storeCacheMiss 设置</li> 
 <li>RMultiLock <span style="background-color:#ffffff; color:#24292f">object </span>不能正确处理 waitTime 和 leastTime 的 0 值</li> 
 <li>Spring Data Redis模块。RedissonConnection.execute() 方法不能正确调用重载方法</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.17.1" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.17.1</a></p>
                                        </div>
                                      
</div>
            