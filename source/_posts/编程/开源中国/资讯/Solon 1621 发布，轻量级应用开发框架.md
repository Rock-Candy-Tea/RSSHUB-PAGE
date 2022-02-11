
---
title: 'Solon 1.6.21 发布，轻量级应用开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6831'
author: 开源中国
comments: false
date: Fri, 11 Feb 2022 11:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6831'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:start">关于官网</h3> 
<p style="color:#24292e; text-align:start">千呼万唤始出来：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsolon.noear.org%2F" target="_blank">https://solon.noear.org</a><span> </span>。整了一个月多了。。。还得不断接着整！</p> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="color:#24292e; text-align:start">Solon 是一个轻量级应用开发框架。支持 Web、Data、Job、Remoting、Cloud 等任何开发场景。短小而精悍！</p> 
<ul> 
 <li>强调，<strong>克制 + 简洁 + 开放的原则</strong></li> 
 <li>力求，<strong>更小、更快、更自由的体验</strong></li> 
</ul> 
<p style="color:#24292e; text-align:start">目前已有近130个生态插件，含盖了日常开发的各种需求。</p> 
<h3 style="text-align:start">关于 Solon Cloud</h3> 
<p style="color:#24292e; text-align:start">Solon Cloud 定义了一系列分布式开发的接口标准和配置规范，相当于DDD模式里的防腐层概念。是 Solon 的微服务架构模式开发解决方案。</p> 
<h3 style="text-align:start">本次主要更新</h3> 
<ul> 
 <li>拆分 BeanProxy 为 BeanProxy 和 AspectUtil</li> 
 <li>增加 接口 AspectUtil.attach(T,handler)；可以强制为一个类绑上代理</li> 
 <li>增加 接口 AspectUtil.attachByScan(basePackage,handler)；可以强制为一批类绑上代理</li> 
 <li>调整 接口动态代理的实现逻辑，以适应jdk9之后的权限处理</li> 
 <li>调整 启动参数的处理时机</li> 
 <li>修复 当未设定server.port时，启动参数将无法指定的问题</li> 
 <li>增加 server.request.maxRequestSize 支持配置： -1(不限)</li> 
 <li>插件 solon.extend.staticfiles，增加更多默认mime，及支持jdk自带的 "mime" 表；并优化性能</li> 
 <li>插件 solon.boot.jetty，调整 "org.eclipse.jetty.server.Request.maxFormContentSize" 配置的同步方式</li> 
</ul> 
<h3 style="text-align:start">快速了解 Solon</h3> 
<ul> 
 <li><a href="https://my.oschina.net/noear/blog/4980834">《想法与架构笔记》</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/4863844">《与 Spring Boot 的区别？》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/5039169">《与 Spring Cloud 的区别？》</a></li> 
</ul> 
<h3 style="text-align:start">项目地址</h3> 
<ul> 
 <li>gitee：<a href="https://gitee.com/noear/solon">https://gitee.com/noear/solon</a></li> 
 <li>github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnoear%2Fsolon" target="_blank">https://github.com/noear/solon</a></li> 
</ul>
                                        </div>
                                      
</div>
            