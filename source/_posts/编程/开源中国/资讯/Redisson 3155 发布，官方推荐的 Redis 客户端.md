
---
title: 'Redisson 3.15.5 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1532'
author: 开源中国
comments: false
date: Fri, 14 May 2021 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1532'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Redisson 3.15.5 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的官方推荐。</p> 
<ul> 
 <li>Feature - 在 RBatch 对象中添加了 discard() 方法；</li> 
 <li>Feature - 在 Tomcat 会话管理器中添加了 broadcastSessionUpdates 设置；</li> 
 <li>修复 - 如果 jcache 的 yaml 格式配置有误，则不会出错；</li> 
 <li>修复 - 频繁的 Redis master 故障转移（failover）导致 IdleConnectionWatcher 的内存泄漏；</li> 
 <li>修复 - Spring Data 模块中的 RedisStreamCommands.xGroupDelConsumer() 方法使用了错误的 Redis 命令；</li> 
 <li>修复 - 如果 pubsub 连接达到上限，RLock 就不能再被获取；</li> 
 <li>修复 - PubSub Lock 条目在获取 Lock 的过程中内存泄漏；</li> 
 <li>修复 - dns 监控器不应该使用 IP 地址作为主机名；</li> 
 <li>修复 - 如果 Redis 集群节点返回空的拓扑结构，故障转移处理将停止工作；</li> 
 <li>修复 - Spring Data RedissonConnection 对象的 mGet() 和 mSet() 方法引发 CROSSSLOT 错误；</li> 
 <li>修复 - Spring Data ReactiveKeyCommands 接口的 touch()、mDel()、mUnlink()、expire()、pExpire()、expireAt()、pExpireAt()、persist() 方法应作为写入操作执行；</li> 
 <li>修复 - Rmap.computeIfPresent() 不会更新可变的对象；</li> 
 <li>修复 - 如果 ExecutorService 节点宕机，MapReduce 超时不被应用；</li> 
 <li>修复 - Redisson 尝试重新连接被拓扑管理器标记为关闭的 Redis 节点；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.15.5" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.15.5</a></p>
                                        </div>
                                      
</div>
            