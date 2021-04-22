
---
title: 'Redisson 3.15.4 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2861'
author: 开源中国
comments: false
date: Thu, 22 Apr 2021 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2861'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Redisson 3.15.4 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Fclients">官方推荐</a>。</p> 
<p>此版本主要更新内容：</p> 
<ul> 
 <li>Feature - 添加了 sslProtocols setting</li> 
 <li>Feature - 添加了 nameMapper setting</li> 
 <li>Feature - <code>getSigned()</code>, <code>setSigned()</code>, <code>incrementAndGetSigned()</code>, <code>getUnsigned()</code>, <code>setUnsigned()</code>, <code>incrementAndGetUnsigned()</code> 方法添加到<code>RBitSet</code> 对象</li> 
 <li>Feature - <code>updateEntryExpiration()</code>, <code>getWithTTLOnly()</code> 方法添加到 <code>RMapCache</code> 对象</li> 
 <li>Improvement - 如果没有指定 idleTime 和缓存大小，Spring Cache、MyBatis Cache、Hibernate Cache 实现应该从 Redis slave 读取数据</li> 
 <li>Fixed - <code>ClusterConnectionManager.upDownSlaves()</code>方法抛出<code>ConcurrentModificationException</code></li> 
 <li>Fixed - <code>ClusterConnectionManager.checkMasterNodesChange()</code>方法抛出 NPE</li> 
 <li>Fixed - <code>JCache</code> <code>CacheEntryUpdatedListener</code> 不能获得已更改的条目的旧值</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.15.4" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.15.4</a> </p>
                                        </div>
                                      
</div>
            