
---
title: 'Elide 6.0.4 发布，雅虎开源的应用数据 API 搭建平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2254'
author: 开源中国
comments: false
date: Mon, 20 Dec 2021 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2254'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Elide 6.0.4 现已发布。Elide 是一个互联网和移动端应用数据 API 搭建平台，只需要一个简单的 JPA 注释模型就能帮你轻松搭建 GraphQL 和 JSON API web 服务。具有标准完善的数据安全保障、移动端性能优化 API、任何数据写入都可以保证原子性（Atomicity）、支持自定义数据持久化机制、数据模型一览无余和配置轻松自由等特性。更新内容如下：</span></p> 
<h2>Bug 修复</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fcommit%2F5e9c1d7ff097ec3143de5ab7b20d5bafcf4ff0b0" target="_blank">view commit</a> 修复 #137 (#2433)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fcommit%2Fde351f391f51d0d8a7586e9384c9f2657743a66f" target="_blank">view commit</a><span> </span>修复 #2263，<span style="background-color:#ffffff; color:#2e3033">json - api json 处理错误现在将返回一个 400 </span>(#2434)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fcommit%2Fac520d61915aa77253fd69cee3c5713da85ede77" target="_blank">view commit</a><span> </span>将 caffeine 从 3.0.4 升级到 3.0.5 (#2435)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fcommit%2F1cce9a9c4d9d29ab29638e7297000a604954eabb" target="_blank">view commit</a><span> 将</span> jetty-webapp 从 9.4.43.v20210629 升级到 9.4.44.v20210927 (#2436)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fcommit%2F35ba78e82f7e230b5c8d3818ab67df7606e65f29" target="_blank">view commit</a><span> </span>修复 #2438 (#2441)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fcommit%2Fa4f89601fb6acc03e6a3a0e0b29d8412e733eb77" target="_blank">view commit</a><span> </span>将 metrics.version 从 4.2.4 t 升级到 4.2.5 (#2442)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fcommit%2Fbd16677ae47419004707f5a7356aa952315c2746" target="_blank">view commit</a><span> </span>将 classgraph 从 4.8.137 升级到 4.8.138 (#2445)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fcommit%2F469fe23e1bc9c8c6639c8df083472f437a69d1ae" target="_blank">view commit</a><span> 问题 </span>608 (#2446)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fcommit%2F8e1563b2e4abde911563b69a6b5a37ca6361d3a5" target="_blank">view commit</a><span> 将</span> micrometer-core 从 1.8.0 升级到 1.8.1 (#2444)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fcommit%2Fcc7b13da0aa6f276c034325be51793f6d6b866c0" target="_blank">view commit</a><span> 将</span> httpcore 从 4.4.14 升级到 4.4.15 (#2443)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fcommit%2F9e2ff4727fbb11947d55536f59409b2e80766290" target="_blank">view commit</a><span> </span>解决 #2447 (#2448)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fcommit%2F2ad81220c9eecb5c009653d72b3204706200d03a" target="_blank">view commit</a><span> </span><span style="background-color:#ffffff; color:#24292f">AsyncQueryOperation：修复空列表的索引越界错误 (#2449)</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fcommit%2F0f2187a533022c3847f2bc744d4e1bd6f03e2595" target="_blank">view commit</a><span> </span><span style="background-color:#ffffff; color:#2e3033">物理列名称中的空格</span>(#2450)</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Fblob%2Fmaster%2Fchangelog.md%23604" target="_blank">https://github.com/yahoo/elide/blob/master/changelog.md#604</a></p>
                                        </div>
                                      
</div>
            