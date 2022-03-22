
---
title: 'Redisson 3.17.0 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=648'
author: 开源中国
comments: false
date: Tue, 22 Mar 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=648'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Redisson 3.17.0 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的官方推荐。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#24292f">Feature</span></strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">添加了 RFunction 对象（需要 </span>Redis 7.0+<span style="background-color:#ffffff; color:#24292f">）。</span></li> 
 <li>为 RScoredSortedSet <span style="background-color:#ffffff; color:#24292f">对象</span>添加了 pollLastEntriesFromAny() 和 pollFirstEntriesFromAny() 方法（需要 Redis 7.0+）。</li> 
 <li>在 RExpirable 接口中添加了 expireIfSet()、expireIfNotSet()、expireIfGreater() 和 expireIfLess() 方法（需要 Redis 7.0+）。</li> 
 <li>增加了 checkLockSyncedSlaves 设置</li> 
 <li>为 RBucket <span style="background-color:#ffffff; color:#24292f">对象</span>添加 getAndExpire 和 getAndClearExpire() 方法（需要 Redis 6.2.0+）。</li> 
 <li>在 RScoredSortedSet 对象中添加了带超时和计数的 pollFirstFromAny() 和 pollLastFromAny() 方法（需要 Redis 7.0+）。</li> 
 <li>在 RScoredSortedSet 对象中添加了带超时和计数的 pollFirst() 和 pollLast() 方法（需要 Redis 7.0+）。</li> 
 <li>RScoredSortedSet 对象中添加了 addAllIfLess()、addAllIfGreater()、addAllIfExist()、addAllIfAbsent() 方法。</li> 
 <li>添加了 RExpirable.expire(Duration) 方法。</li> 
 <li>添加了 RExpirable.expireTime() 方法（需要 Redis 7.0+）。</li> 
 <li>RTimeSeries 对象增加了 range(), rangeReversed(), entryRange(), entryRangeReversed() 方法，并增加了限制参数。</li> 
 <li>增加了 TransactionalOperation.syncSlaves 设置。</li> 
 <li>在 RBlockingQueue 对象中添加了 pollFirstFromAny() 和 pollLastFromAny() 方法（需要 Redis 7.0+）。</li> 
</ul> 
<p><strong>Improvement </strong></p> 
<ul> 
 <li>只读缓存的脚本应该在从属节点上执行（需要 Redis 7.0+）。</li> 
 <li>SORT_RO 命令用于从属节点</li> 
 <li><span style="background-color:#ffffff; color:#24292f">通过 RPermitExpirableSemaphore 减少分配数据的大小</span></li> 
</ul> 
<p><strong>Fixed</strong></p> 
<ul> 
 <li>RedissonLocalCachedMap.clearLocalCache() 方法抛出 IllegalArgumentException</li> 
 <li>RedissonMultiLock 与 RedissonSpinLock 不能正常工作。</li> 
 <li><span style="background-color:#ffffff; color:#24292f">在集群模式下，SlaveConnectionPool 没有可用的 Redis 条目错误</span></li> 
 <li>RKeys.deleteByPattern() 方法并不总是正确删除 keys</li> 
 <li>RExpirableReactive 和 RExpirableRx 接口的 expireAt(Instant) 方法不起作用</li> 
 <li>在 Redis 集群模式下，错误地检测了添加和删除的 slots</li> 
 <li><span style="background-color:#ffffff; color:#24292f">多模式下的 Spring 数据连接会导致线程卡住（自3.16.7以来的回归）</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">未应用 Sentinel username setting</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">RTimeSeries 不能处理不同时间戳的相同值</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">Quarkus 环境变量未正确解析</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">在 RPermitExpirableSemaphore 中检查 expiration</span></li> 
 <li>RedisTimeoutException：Command execution timeout </li> 
 <li>RedissonMultiLock lock method 中错误的等待时间计算导致死锁</li> 
 <li>AsyncRemoteProxy 抛出 Redisson 被关闭的异常</li> 
 <li><span style="background-color:#ffffff; color:#24292f">RedisClusterNode.clusterSlots() 方法抛出异常</span></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292f">更新说明：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.17.0" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.17.0</a></p>
                                        </div>
                                      
</div>
            