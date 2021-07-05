
---
title: 'OpeningO-spring-boot-x 新版 4.3.1 出炉，强大的分布式 id 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3466'
author: 开源中国
comments: false
date: Mon, 05 Jul 2021 10:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3466'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">OpeningO-spring-boot-x是spring boot应用的扩展。</span></p> 
<p><strong>特性清单</strong></p> 
<ul> 
 <li> <p>手动事务管理 [2021.6.29更新]</p> </li> 
 <li> <p>分布式id生成器gedid，DidLoader [ 2021.6.25更新 ]</p> </li> 
 <li> <p>Safety工具 [ 2021.6.25更新 ]</p> </li> 
 <li> <p>请求日志，包括请求源、请求目标、请求参数、处理时间、错误异常等信息；</p> </li> 
 <li> <p>请求响应参数的自动装配（映射）；</p> </li> 
 <li> <p>跨域的配置；</p> </li> 
 <li> <p>嵌入<code>SpringBoot</code>的异常处理机制，可以将原来的错误信息中插入其他信息、或将其解析或转换为其他信息；</p> </li> 
 <li> <p>如<code>SpringBoot</code>之<code>starter</code>动态装配或在<code>yml</code>中配置相关特性；</p> </li> 
 <li> <p>简化的<code>Redis</code>操作；</p> </li> 
 <li> <p>提炼<code>Elasticsearch</code>之<code>HighlevelClient</code>常用操作saveOrUpdate,deleteById(s),findById(s),search等；</p> </li> 
 <li> <p><code>feign</code>的请求头参数的处理：合并上下游的请求头参数，并发场景的数据处理策略；</p> </li> 
 <li> <p>基于<code>Druid</code>和<code>Hikari</code>的动态路由<code>RoutingDataSource</code>；</p> </li> 
 <li> <p><code>SpringBoot</code>应用的配置信息的自动拷贝；</p> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">此次重点更新分布式Id支持</span></p> 
<p><strong><span style="background-color:#ffffff; color:#333333">支持多种ID生成引擎</span></strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333">EtcdIdEngine</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">SnowflakeIdEngine</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">RedisIdEngine</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">ZookeeperIdEngine</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">UuidEngine</span></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">还可以根据自己的需要封装适合自己的IdEngine。这里有管理分布式Id</span>——GeDid的详细介绍：<a href="https://my.oschina.net/brucezcq/blog/5120369">https://my.oschina.net/brucezcq/blog/5120369</a></p> 
<p>同步支持了，WebSocket、一些工具组件：Safety、手动事务管理器ManualTransactionManager。</p>
                                        </div>
                                      
</div>
            