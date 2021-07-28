
---
title: 'Redisson 3.16.1 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6217'
author: 开源中国
comments: false
date: Wed, 28 Jul 2021 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6217'
---

<div>   
<div class="content">
                                                                                            <p>Redisson 3.16.1 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的官方推荐。</p> 
<p>此版本更新内容如下：</p> 
<ul> 
 <li>改进 - 增加了 MarshallingCodec 和 JsonJacksonCodec 预热</li> 
 <li>改进 - 对连接数少的连接池的性能改进</li> 
 <li>修复 -  如果在 REDIS_WRITE_ATOMIC 模式下执行批处理，则命令错误后连接泄漏</li> 
 <li>修复 -  AsyncSemaphore race condition 问题</li> 
 <li>修复 -  Quarkus 本机远程服务调用失败</li> 
 <li>修复 - <code>nameMapper</code>设置不适用于<code>RTopic</code>对象</li> 
 <li>修复 -  REDIS_WRITE_ATOMIC 模式下的批处理不尊重批处理设置</li> 
 <li>修复 - 在执行<code>RLiveObjectService.get()</code>方法时缓存关闭时抛出<code>UndeclaredThrowableException</code></li> 
 <li>修复 -  反应式事务未解锁事务锁</li> 
 <li>修复 -  事务映射的 keySet() 方法抛出异常</li> 
 <li>修复 -  如果 owner 不存在，则应取消锁到期更新</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.16.1" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.16.1</a></p>
                                        </div>
                                      
</div>
            