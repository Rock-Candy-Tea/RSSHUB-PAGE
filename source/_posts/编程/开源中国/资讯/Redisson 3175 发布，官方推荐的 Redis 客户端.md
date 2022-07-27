
---
title: 'Redisson 3.17.5 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7364'
author: 开源中国
comments: false
date: Wed, 27 Jul 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7364'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <div> 
   <p style="margin-left:0">Redisson 3.17.5 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的官方推荐。</p> 
   <p style="margin-left:0">此版本更新内容如下：</p> 
   <p style="margin-left:0"><span style="color:#24292f"><strong>Feature</strong></span></p> 
   <ul> 
    <li><span style="color:#24292f">为事务性 RSetCache 和 RSet 对象实现了 touch()、unlink() 和 delete() 方法</span></li> 
    <li><span style="color:#24292f">事务性 RBucket、RMap、RMapCache、RSetCache、RSet 对象支持 expire()、expireAt() 和 clearExpire() 方法</span></li> 
    <li><span style="color:#24292f">添加了 ExecutorOptions.idGenerator() 设置</span></li> 
    <li><span style="color:#24292f">将任务 id 添加到 RExecutorService 接口的方法</span></li> 
   </ul> 
   <p style="margin-left:0"><span style="color:#24292f"><strong>Fixed</strong></span></p> 
   <ul> 
    <li><span style="color:#24292f">在 Spring Data Redis 2.7 中使用 RedisMessageListenerContainer 重复订阅</span></li> 
    <li><span style="color:#24292f">NameMapper 两次应用于事务性 RBucket</span></li> 
    <li><span style="color:#24292f">某些 Quarkus 环境变量会清除通过配置文件设置的所有 Redisson 属性</span></li> 
    <li><span style="color:#24292f">RJsonBucket.delete() 方法不起作用</span></li> 
    <li><span style="color:#24292f">RExecutorService.submitAsync(Callable, long, TimeUnit) 方法抛出 ClassCastException</span></li> 
    <li>锁定 synced slaves check</li> 
    <li>如果 result 是 list 的 list，反应式脚本命令会抛出ClassCastException</li> 
    <li>RBatch.getJsonBucket() 方法应返回 RJsonBucketAsync 接口</li> 
   </ul> 
   <p style="margin-left:0px">详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.17.5" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.17.5</a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            