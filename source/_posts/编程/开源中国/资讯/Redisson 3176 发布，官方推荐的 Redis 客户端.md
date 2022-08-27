
---
title: 'Redisson 3.17.6 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=739'
author: 开源中国
comments: false
date: Sat, 27 Aug 2022 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=739'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Redisson 3.17.6 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的官方推荐。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Feature</strong></p> 
<ul> 
 <li>Helidon 3.0 支持</li> 
 <li>能够在 MapOptions 对象中指定 MapWriterAsync 和 MapLoaderAsync</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#24292f">Improvement</span></strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">日志输出字符串默认扩展为1000 个字符</span></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Fixed</strong></p> 
<ul> 
 <li><code>RBuckets</code>方法不使用<code>nameMapper</code></li> 
 <li>PingConnectionHandler 应在 RedisLoadingException、RedisTryAgainException、RedisClusterDownException、RedisBusyException 上关闭通道</li> 
 <li>调用超时不适用于<code>RTopic.removeListenerAsync()</code>方法</li> 
 <li><code>RMap.destroy()</code>方法调用后，WriteBehind task 不会停止</li> 
 <li>如果在池中创建了新连接，连接 ping 工作不正确</li> 
 <li>“SlaveConnectionPool no available Redis entries”错误在集群中发生，原因是提前将主节点从节点中排除以进行读取</li> 
 <li>永久阻塞调用线程</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.17.6" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.17.6</a></p>
                                        </div>
                                      
</div>
            