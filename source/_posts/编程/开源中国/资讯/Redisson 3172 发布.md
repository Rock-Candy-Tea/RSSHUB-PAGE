
---
title: 'Redisson 3.17.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7800'
author: 开源中国
comments: false
date: Wed, 25 May 2022 07:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7800'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Redisson 3.17.2 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的官方推荐。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#24292f">Feature</span></strong></p> 
<ul> 
 <li><span style="color:#24292f">添加了 </span><span style="color:#24292f">RScoredSortedSet.replace() 方法</span></li> 
 <li><span style="color:#24292f">添加了 Spring Data Redis 2.7.0 模块</span></li> 
 <li><span style="color:#24292f">添加了 RPatternTopic.removeAllListenersAsync() 方法</span></li> 
 <li><span style="color:#24292f">添加了 RShardedTopic 对象（需要Redis 7.0+）</span></li> 
 <li>允许在 Redis connection url 中指定用户名和密码</li> 
 <li>支持本地缓存的 JCache 数据分区</li> 
</ul> 
<p><strong><span style="background-color:#ffffff; color:#24292f">Fixed</span></strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">在集群模式下失败后出现"Can't add slave"的异常</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">连接中断后"Unable to acquire subscription"的错误</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">当使用 useScriptCache=true 从缓存中获取值时，JCache 永远挂起</span></li> 
 <li>如果指定了 MapLoader，RMap.merge() 方法会挂起</li> 
 <li>FairLock 线程计数器应该从 1 开始</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.17.2" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.17.2</a></p>
                                        </div>
                                      
</div>
            