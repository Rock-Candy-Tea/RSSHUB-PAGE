
---
title: 'Solon 1.6.18 发布，轻量级应用开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7027'
author: 开源中国
comments: false
date: Sat, 22 Jan 2022 11:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7027'
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
 <li>插件 mybatis-solon-plugin，升级 mybatis 为 3.5.9</li> 
 <li>插件 mybatisplus-solon-plugin，升级 mybatis-plus 为 3.5.0</li> 
 <li>插件 mybatis-sqlhelper-solon-plugin，升级 sqlhelper-mybatis 为 3.6.9</li> 
 <li>插件 mybatis-pagehelper-solon-plugin，升级 pagehelper 为 5.3.0</li> 
 <li>增加 注入泛型推断支持</li> 
 <li>增加 国际化配置 支持 yml 格式</li> 
 <li>增加 泛型基类向容器注册机制</li> 
 <li>增加 泛型类基于 typeName 的自动注册和注入。</li> 
 <li>取消 @Inject 对函数的支持，以免让人误用</li> 
 <li>修复 启动参数值会丢失"-"的问题</li> 
 <li>修复 sessionstate.redis 不能反序列化对象的问题</li> 
 <li>修复 json post 空值时，不会触发实体验证机制</li> 
 <li>修复 @Inject 的初始化链当中，当自己注入自己时会异常的问题</li> 
 <li>调整 redis 单词拼写错误（maxTotaol -> maxTotal）</li> 
 <li>调整 Aop.get(Class<?>) 改为：Aop.get(Class)</li> 
 <li>调整 Aop.getOrNew(Class<?>) 改为：Aop.getOrNew(Class)</li> 
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
<p> </p>
                                        </div>
                                      
</div>
            