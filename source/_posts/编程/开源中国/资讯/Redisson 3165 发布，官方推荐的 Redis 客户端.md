
---
title: 'Redisson 3.16.5 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9728'
author: 开源中国
comments: false
date: Thu, 02 Dec 2021 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9728'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Redisson 3.16.5 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的官方推荐。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#24292f">Feature</span></strong></p> 
<ul> 
 <li>在 RSet 对象中添加了<code>countIntersection()</code>方法</li> 
 <li>为<code>RListMultimapCache</code>和<code>RSetMultimapCache</code>对象添加反应式接口</li> 
 <li>添加了<code>sentinelUsername</code>设置</li> 
 <li>添加了分布式迭代器</li> 
 <li>添加了对 Spring Data Redis 2.6.0 的支持</li> 
</ul> 
<p style="color:#333333; margin-left:0px; margin-right:0px; text-align:left"><strong>Fixed</strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">Spring Data Redis 的 RedissonConnectionFactory.getReactiveConnection() 方法与 Redis 集群模式不兼容</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">Mybatis RedissonCache 应该在根包中搜索 redisson.yaml 配置</span></li> 
 <li>在使用 master host 的新 IP 进行故障转移后，出现<code>Can't find host in slaves!</code>错误</li> 
 <li>在复制模式下，没有检测到 failed slaves</li> 
 <li>在<code>put</code>之前的<code>get</code>操作可能导致本地缓存状态不一致</li> 
 <li><code>RList.remove(object, count)</code>如果删除多个对象，则抛出异常</li> 
 <li><code>RLocalCachedMap.delete()</code>方法异步清除本地缓存</li> 
 <li>如果处于订阅状态，则<code>IdleConnectionWatcher</code>不应关闭<code>RedisPubSubConnection</code></li> 
 <li>Sentinel <span style="background-color:#ffffff; color:#24292f">master host </span>不使用 SSL 的问题</li> 
 <li>LocalCachedMap 对象的更新同步策略不应将更新值两次应用于更新源实例</li> 
 <li>JCache dependency 更新为 1.1.1</li> 
 <li><span style="background-color:#ffffff; color:#24292f">Sentinel master-host = ? 设置</span>在从属检查中没有得到正确处理</li> 
 <li><code>RBuckets.trySet()</code>方法引发 CROSSSLOT 错误</li> 
 <li>DNS 监视器在当前尝试未完成时重新尝试更改主服务器</li> 
</ul> 
<p style="color:#333333; margin-left:0px; margin-right:0px; text-align:left">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.16.5" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.16.5</a></p>
                                        </div>
                                      
</div>
            