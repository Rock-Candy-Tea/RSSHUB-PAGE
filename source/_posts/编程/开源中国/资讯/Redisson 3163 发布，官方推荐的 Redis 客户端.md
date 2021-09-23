
---
title: 'Redisson 3.16.3 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8891'
author: 开源中国
comments: false
date: Thu, 23 Sep 2021 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8891'
---

<div>   
<div class="content">
                                                                                            <p>Redisson 3.16.3 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的官方推荐。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#000000">Improvement</span></strong></p> 
<ul> 
 <li><code>RBuckets.get()</code>方法在 Redis Cluster 模式下应按槽对键进行分组</li> 
 <li><code>RBatch</code>结果解码优化</li> 
</ul> 
<p style="color:#333333; margin-left:0px; margin-right:0px; text-align:left"><strong>Fixed</strong></p> 
<ul> 
 <li>如果用于任务池的连接被中断，<code>RExecutorService</code>、<code>RRemoteService</code>执行可能会挂起</li> 
 <li>带有<code>skipResult()</code>选项的 RBatch 会影响其他命令的结果（自 3.16.1 以来的回归）</li> 
 <li><span style="background-color:#ffffff; color:#24292f">连接泄漏</span>（自 3.16.1 以来的回归）</li> 
 <li><code>getBuckets().set()</code>方法抛出 CROSSSLOT 错误</li> 
 <li><code>RedissonMapCache.addListener()</code>方法抛出 NPE</li> 
 <li>在 Sentinel 模式下，从属节点的 master-host 没有解析</li> 
 <li>中断的<code>RLock.tryLock()</code>方法无限期地 renewing lock</li> 
 <li><span style="background-color:#ffffff; color:#24292f">如果正在使用，则不要 ping 连接</span></li> 
 <li><code>natMapper</code>不适用于已解析的 Sentinel 和 Cluster 主机</li> 
</ul> 
<p style="color:#333333; margin-left:0px; margin-right:0px; text-align:left">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.16.3" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.16.3</a></p>
                                        </div>
                                      
</div>
            