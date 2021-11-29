
---
title: 'Jedis 4.0.0 beta 4 发布，Redis Java 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1139'
author: 开源中国
comments: false
date: Mon, 29 Nov 2021 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1139'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Jedis 是 Redis 的一个 Java 客户端库，Jedis 4.0.0 beta 4 发布，更新内容如下：</p> 
<h3>新功能</h3> 
<ul> 
 <li>引入 JedisPooled 实现了与 JedisCluster 相同的接口，允许在 JedisCluster 和 JedisPooled 之间轻松切换。</li> 
 <li>实现了 RediJSON 2 命令</li> 
 <li>恢复了 Jedis 3 类/方法： 
  <ul> 
   <li>JedisSentinelPool 类</li> 
   <li>JedisPubSub 抽象类</li> 
   <li>BinaryJedisPubSub 抽象类</li> 
   <li>JedisMonitor 抽象类</li> 
   <li>Pipeline.syncAndReturnAll() 方法</li> 
  </ul> </li> 
 <li>添加/更改了 ACL 命令： 
  <ul> 
   <li>添加了 ACL DELUSER 命令</li> 
   <li>添加了带 bits 选项的 ACL GENPASS 命令</li> 
   <li>添加了 aclLogReset() 方法，支持 ACL LOG RESET 子命令，以取代 aclLog(options) 方法。</li> 
  </ul> </li> 
 <li>错误修复 
  <ul> 
   <li>修复了 ClusterPipeline 中的 NullPointerException。</li> 
   <li>修复了 ClusterConnectionProvider 中的资源泄漏。</li> 
  </ul> </li> 
 <li>维护 
  <ul> 
   <li>重写了 Document.toString() 方法 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fissues%2F2692" target="_blank">#2692</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2696" target="_blank">#2696</a>)</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Freleases%2Ftag%2Fv4.0.0-beta4" target="_blank">https://github.com/redis/jedis/releases/tag/v4.0.0-beta4</a></p> 
<p> </p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            