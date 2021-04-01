
---
title: 'Redisson 3.15.3 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6136'
author: 开源中国
comments: false
date: Thu, 01 Apr 2021 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6136'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Redisson 3.15.3 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Fclients">官方推荐</a>。</p> 
<p>此版本主要更新内容：</p> 
<ul> 
 <li>Feature - 增加 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Fwiki%2F2.-Configuration%23connectionlistener" target="_blank">connectionListener</a> setting</li> 
 <li>Fixed - RRateLimiter object 的 tryAcquire() 和 availablePermits() method 抛出太多结果而导致解包错误。</li> 
 <li>Fixed - <code>RRateLimiter</code>object 引发 LUA 脚本错误</li> 
 <li>Fixed - Topology Manager 中 Replicated Redis 配置的连接泄漏</li> 
 <li>Fixed - <code>ConnectionListener.onConnect()</code>method 在 Redisson 启动时没有被触发</li> 
 <li>Fixed -  RDeque object 的 addLastIfExists() 和 addLastIfExists() methods 不起作用</li> 
 <li>Fixed - 如果 Redis master 变更不成功，会抛出 ArrayIndexOutOfBoundsException</li> 
 <li>Fixed - 如果定义了多 worker，RScheduledExecutorService.scheduleAtFixedRate() 会启动同一个任务的多个实例</li> 
 <li>Fixed - 通过 RScheduledExecutorService.scheduleAtFixedRate() method 安排的任务在一段时间后没有被执行</li> 
</ul> 
<p>更新说明： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.15.3" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.15.3</a></p>
                                        </div>
                                      
</div>
            