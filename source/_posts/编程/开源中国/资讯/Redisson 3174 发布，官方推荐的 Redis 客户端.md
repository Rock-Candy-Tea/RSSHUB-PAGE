
---
title: 'Redisson 3.17.4 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7018'
author: 开源中国
comments: false
date: Sat, 18 Jun 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7018'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0">Redisson 3.17.4 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的官方推荐。</p> 
<p style="margin-left:0">此版本更新内容如下：</p> 
<p style="margin-left:0"><span style="color:#24292f"><strong>Feature</strong></span></p> 
<ul> 
 <li><span style="color:#24292f">为支持 JSON.* 命令添加了 RJsonBucket 对象</span></li> 
 <li><span style="color:#24292f">在 RBatch 中添加了 RFunction 和 RShardedTopic 对象</span></li> 
</ul> 
<p style="margin-left:0"><span style="color:#24292f"><strong>Fixed</strong></span></p> 
<ul> 
 <li><span style="color:#24292f">在 Sentinel 模式下连续出现"Unable to unfreeze entry"错误</span></li> 
 <li><span style="color:#24292f">nameMapper 设置不适用于 RExecutorService 和 RScheduledExecutorService</span></li> 
 <li><span style="color:#24292f">通道写入异常可能导致错误的命令顺序</span></li> 
 <li><span style="color:#24292f">如果 SENTINEL SENTINELS 命令的结果中不包括 DNS 解析的 sentinel，则不连接到它</span></li> 
 <li>RScript.load() 方法不应该使用失败的 Redis 节点</li> 
 <li>RPermitExpirableSemaphore.acquisitionAsync() 方法会挂起，直到 leaseTimeout 发生。(自 3.16.8 以来的回归)</li> 
 <li>对 RRemoteService 的响应使用 60 秒的轮询，而不是采取命令</li> 
 <li>Spring Data Redis ReactiveScriptingCommands 对象的 eval() 和 evalSha() 方法会抛出 IndexOutOfBoundsException</li> 
 <li>过期的 entries eviction process 被限制为每次调用 5000 条</li> 
 <li>在通道重新连接后，sharded 主题没有被重新订阅</li> 
 <li>执行 blpop 命令会导致重新连接</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.17.4" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.17.4</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            