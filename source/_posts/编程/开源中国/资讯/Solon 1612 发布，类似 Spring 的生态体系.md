
---
title: 'Solon 1.6.12 发布，类似 Spring 的生态体系'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3600'
author: 开源中国
comments: false
date: Tue, 04 Jan 2022 18:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3600'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:start">关于官网</h3> 
<p style="color:#24292e; text-align:start">千呼万唤始出来：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsolon.noear.org%2F" target="_blank">https://solon.noear.org</a><span> </span>。整了一个月多了，总体样子有了。。。还得不断接着整！</p> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="color:#24292e; text-align:start">Solon 是一个轻量级应用开发框架。支持 Web、Data、Job、Remoting、Cloud 等任何开发场景。短小而精悍！</p> 
<ul> 
 <li>强调，<strong>克制 + 简洁 + 开放的原则</strong></li> 
 <li>力求，<strong>更小、更快、更自由的体验</strong></li> 
</ul> 
<p style="color:#24292e; text-align:start">目前已有近130个生态插件，含盖了日常开发的各种需求。</p> 
<h3 style="text-align:start">关于 Solon Cloud</h3> 
<p style="color:#24292e; text-align:start">Solon Cloud 定义了一系列分布式开发的接口标准和配置规范，相当于DDD模式里的防腐层概念。是 Solon 的微服务架构模式开发解决方案。</p> 
<h3 style="text-align:start">关于本次更新</h3> 
<ul> 
 <li>修复 solon.boot.websocket 插件，带参数时无法正确路由的问题</li> 
 <li>修复 solon.serialization.jackson 插件，body 为空时，会出错的问题</li> 
 <li>插件 log4j2-solon-plugin，升级 log4j 为 2.17.1</li> 
 <li>插件 solon.serialization.snack3，升级 snack3 为 3.2.7 ，支持成员类反序列化</li> 
 <li>插件 solon.serialization.jackson，升级 jackson 为 2.13.1</li> 
 <li>插件 aws-s3-solon-plugin，升级 aws-java-sdk-s3 为 1.12.132</li> 
 <li>插件 solon.view.beetl，升级 beetl 为 3.9.3</li> 
 <li>插件 beetlsql-solon-plugin，升级 beetlsql 为 3.12.6</li> 
 <li>插件 logback-solon-plugin、log4j2-solon-plugin，调整为启动异常退出时可记录日志</li> 
 <li>调整 内部对 ctx.path() 的应用全改为 ctx.pathNew()，便于路径重定义</li> 
 <li>调整 yaml、json 配置的 的 null 值默认转为空字符串（与 properties 保持一至）</li> 
 <li>新增 配置文件 "占位符" 任意使用（之前只能出现一个占位符）</li> 
</ul> 
<h3 style="text-align:start">快速了解 Solon</h3> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/4980834">《想法与架构笔记》</a></p> 
<p style="color:#24292e; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></p> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/4863844">《与 Spring Boot 的区别？》</a></p> 
<p style="color:#24292e; text-align:start"><a href="https://my.oschina.net/noear/blog/5039169">《与 Spring Cloud 的区别？》</a></p>
                                        </div>
                                      
</div>
            