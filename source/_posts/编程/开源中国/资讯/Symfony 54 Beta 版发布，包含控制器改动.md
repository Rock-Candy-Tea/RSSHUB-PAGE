
---
title: 'Symfony 5.4 Beta 版发布，包含控制器改动'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1109/061115_DYos_2744687.png'
author: 开源中国
comments: false
date: Tue, 09 Nov 2021 06:12:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1109/061115_DYos_2744687.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Symfony 是一款基于 MVC 架构的 PHP 框架，致力于减少重复代码的编写，以加速 Web 应用的开发和维护。Symfony 与许多关系型数据库集成的也非常好，成本也较小。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Symfony 致力于在企业背景下创建健壮的应用，同时也给予了开发者强大的配置功能：从文件结构到外部目录，几乎所有的东西都可以自定义。Symfony 也捆绑了一些诸如测试、调试、文档生成等工具来满足企业的开发过程。</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">Symfony 5.4 主要对控制器做了一些更改：</h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">弃用 Request::get() 方法</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">Symfony 请求对象是 HTTP 请求消息的面向对象表示。这个对象提供了几个方法，以从传入的请求中获取信息:</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img alt height="334" src="https://static.oschina.net/uploads/space/2021/1109/061115_DYos_2744687.png" width="858" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">除了这些特定的方法，还有一个通用的<span> </span><code>get()</code><span> </span>方法，在 path(路由占位符或自定义属性)、<code>$_GET</code><span> </span>和<span> </span><code>$_POST<span> </span></code>中查找信息，并返回找到的第一个值:</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img alt height="125" src="https://static.oschina.net/uploads/space/2021/1109/061131_V3pB_2744687.png" width="960" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">这种方法的灵活性在某些边缘情况下可能很有用，但通常情况下最好明确说明数据来自何处，因此 Symfony 一直不建议使用这个方式，</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">在 Symfony 5.4中，<span> </span><code>get()</code><span> </span>方法被标记为私有。使用它将看到弃用消息。</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#2e3033">快捷方式变更</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">早期的 Symfony 版本可以使用<span> </span><code>get()</code><span> </span>和<span> </span><code>has()</code><span> </span>方法从控制器访问所有应用程序服务，Symfony 5.4 完全弃用了<span> </span><code>get()</code><span> </span>和<span> </span><code>has()</code><span> </span>方法，用这种方式访问​​整个服务容器被认为是一种反面模式<span style="color:#18171b">（</span><span> </span><span style="color:#18171b">anti-pattern </span>），<code>get()</code><span> </span>方法只允许访问与控制器相关的非常有限的一组服务，在控制器中获取服务应该使用构造函数或方法注入。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此外，控制器为最常见的操作提供了一系列快捷方式。例如，要重定向到某个路由，不需要注入<span> </span><code>UrlGeneratorInterface</code><span> </span>类来获取 URL 生成器服务，可以选择使用<span> </span><code>redirectToRoute()</code><span> </span>快捷方式：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img alt height="227" src="https://static.oschina.net/uploads/space/2021/1109/061145_nQGQ_2744687.png" width="960" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">弃用以下控制器快捷方式，它们与 HTTP 操作没有直接关系：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>dispatchMessage()</code></li> 
 <li><code>getDoctrine()</code></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">不要使用这些快捷方式，而是在构造函数或控制器方法中注入相关服务。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">除了以上对 Symfony 控制器的改动，5.4  BETA 版本还有其他更新项，具体可查看更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsymfony%2Fsymfony%2Freleases%2Ftag%2Fv5.4.0-BETA1" target="_blank">https://github.com/symfony/symfony/releases/tag/v5.4.0-BETA</a></p>
                                        </div>
                                      
</div>
            