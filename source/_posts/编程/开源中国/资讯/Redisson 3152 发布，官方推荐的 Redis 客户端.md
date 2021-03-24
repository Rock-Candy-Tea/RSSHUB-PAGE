
---
title: 'Redisson 3.15.2 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: '/images/404.gif'
author: 开源中国
comments: false
date: Tue, 23 Mar 2021 23:12:00 GMT
thumbnail: '/images/404.gif'
---

<div>   
<div class="content">
                                                                                            <p>Redisson 3.15.2 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Fclients" target="_blank">官方推荐</a>。</p> 
<p>此版本主要更新内容：</p> 
<ul> 
 <li>Feature - 为 RDeque 和 RBlockingDeque objects 添加了 move() 方法</li> 
 <li>Feature - 在 RStream.add() 方法中添加了 MINID trimming strategy 和 LIMIT 参数</li> 
 <li>Feature - 添加了新的 config <code>checkSlaveStatusWithSyncing</code> setting</li> 
 <li>Feature - 默认启用 tcpNoDelay 设置</li> 
 <li>Feature - 增加了 RedissonClient.reactive() 和 RedissonClient.rxJava() 方法</li> 
 <li>Feature - Spring Boot 自动配置应创建 Reactive 和 RxJava 实例</li> 
 <li>Improvement - RStream.read() 和 RStream.readGroup() 的简化 API</li> 
 <li>Fixed - 5.3 版本之前的 Hibernate 模块不支持 nextTimestamp() 方法的回退</li> 
 <li>Fixed - 如果在编码过程中出现异常，MarshallingCodec 不会释放分配的 ByteBuf 对象</li> 
 <li>Fixed - 如果 Redis 客户端没有发送响应，retryInterval 不用于下一次尝试</li> 
 <li>Fixed - 在 org.redisson.RedissonLock#tryLockInnerAsync 方法中以非安全的方式更新了 lease timeout</li> 
 <li>Fixed - 不支持 RxJava 对象中的引用</li> 
 <li>Fixed - Spring Data Redis 模块不支持 RedisStreamCommands.xReadGroup() 方法中的 StreamReadOptions.isNoack() 选项</li> 
 <li>Fixed - 试图在没有密码的情况下认证 sentinel 服务器</li> 
 <li>Fixed - RStream.getInfo() 方法不对条目进行解码</li> 
 <li>Fixed - 如果之前由于 failedSlaveCheckInterva l时间范围内的错误而被排除，Redisson不会重新连接 slave</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.15.2" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.15.2</a> </p>
                                        </div>
                                      
</div>
            