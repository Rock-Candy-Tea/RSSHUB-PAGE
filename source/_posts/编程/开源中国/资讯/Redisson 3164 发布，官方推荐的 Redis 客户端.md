
---
title: 'Redisson 3.16.4 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4021'
author: 开源中国
comments: false
date: Tue, 02 Nov 2021 07:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4021'
---

<div>   
<div class="content">
                                                                                            <p>Redisson 3.16.4 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的官方推荐。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#24292f">Feature</span></strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">增加了 sentinelsDiscovery 设置</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">在 redisson-quarkus 模块中添加了 quarkus.redisson.file 设置，以定义外部 Redisson 配置文件。</span></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#000000">Improvement</span></strong></p> 
<ul> 
 <li>优化<code>ClusterConnectionManager.checkSlaveNodesChange()</code>和<code>ClusterConnectionManager.checkMasterNodesChange()</code>方法</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Fixed</strong></p> 
<ul> 
 <li>复制模式下的主控变化监控任务如果在 dns 变化前被调用就会停止执行</li> 
 <li><span style="background-color:#ffffff; color:#24292f">如果 requestId 为 null，则无法调用 RemoteService</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">编解码器不适用于非集群中的 RBuckets.set() 方法</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">不应在 Redis 集群模式下再次添加恢复的 slave</span></li> 
 <li><code>releaseConnection</code>方法可能导致 StackOverflowError</li> 
 <li><span style="background-color:#ffffff; color:#24292f">未正确处理带有主机名的 MOVED 响应</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">如果组中有一个没有数据的信息，RStream.readGroup() 方法会抛出 IndexOutOfBoundsException</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">CommandPubSubDecoder 中的 NPE</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">RExecutorService 可能会在同一时间执行同一个任务两次</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">测试的依赖项应该使用适当的范围</span></li> 
 <li><code>RPriorityQueue.add()</code>方法使用异步方法</li> 
 <li>不重试已经成功发送的 non-idempotent 操作</li> 
 <li><span style="background-color:#ffffff; color:#24292f">RMapCache.fastRemove 抛出 RedisException：解压的 results 太多</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">在高并发环境下，RRateLimiter 随着时间的推移而减少了限制</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">如果连接在使用中，不要 PING 连接</span></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">更新说明：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.16.4" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.16.4</a> </p>
                                        </div>
                                      
</div>
            