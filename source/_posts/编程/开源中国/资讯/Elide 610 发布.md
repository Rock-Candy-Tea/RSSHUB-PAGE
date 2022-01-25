
---
title: 'Elide 6.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=609'
author: 开源中国
comments: false
date: Tue, 25 Jan 2022 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=609'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Elide 是一个互联网和移动端应用数据 API 搭建平台，只需要一个简单的 JPA 注释模型就能帮你轻松搭建 GraphQL 和 JSON API web 服务。具有标准完善的数据安全保障、移动端性能优化 API、任何数据写入都可以保证原子性（Atomicity）、支持自定义数据持久化机制、数据模型一览无余和配置轻松自由等特性。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Elide 6.1.0 已正式发布，更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">特性</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>重构 spring 控制器和 Elide bean<span> </span><code>@RefreshScope</code>，以便当基于 spring boot 的 Elide 服务刷新时，它们将自动重新加载。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[maven-release-plugin] 为下一次开发迭代做准备</li> 
 <li>当涉及别名时，让 getColumnProjection() 方法对不同来源的列 Id 使用不同的名字</li> 
 <li>将 h2 从 2.0.202 升级到 2.0.206</li> 
 <li>将 micrometer-core 从 1.8.1 升级到 1.8.2</li> 
 <li>将 spring-core 从 5.3.14 升级到 5.3.15</li> 
 <li>将 spring-websocket 从 5.3.14 升级到 5.3.15</li> 
 <li>将 slf4j-api 从 1.7.32 升级到 1.7.33</li> 
 <li>将 log4j-over-slf4j 从 1.7.32 升至 1.7.33</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fblob%2Fmaster%2Fchangelog.md%23610" target="_blank">https://github.com/yahoo/elide/blob/master/changelog.md#610</a></p>
                                        </div>
                                      
</div>
            