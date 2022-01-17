
---
title: 'JetLinks 1.12 发布，开源物联网基础平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-66c52c602080fa89a2e30a53c81e9253d35.png'
author: 开源中国
comments: false
date: Mon, 17 Jan 2022 10:30:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-66c52c602080fa89a2e30a53c81e9253d35.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:start">JetLinks 开源物联网平台</h1> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">JetLinks 基于Java8、Spring Boot 2.x、WebFlux、Netty、Vert.x、Reactor 等开发，是一个开源的企业级物联网基础开发平台，实现了物联网相关以及相关业务开发的众多基础功能，能帮助你快速建立物联网相关业务系统。</p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">在线完整功能演示地址：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.jetlinks.cn%2F" target="_blank">http://demo.jetlinks.cn<span><span> </span></span></a>用户名:<code>test</code><span> </span>密码:<span> </span><code>test123456</code></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">测试用户未开放全部权限，建议本地运行社区版体验或者联系商务试用企业版。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">核心特性</h2> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start"><strong>开放源代码</strong></p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">全部源代码开放，可自由拓展功能，不再受制于人。前后端分离，接口全开放。</p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start"><strong>统一设备接入,海量设备管理</strong></p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">TCP/UDP/MQTT/HTTP、TLS/DTLS、不同厂商、不同设备、不同报文、统一接入，统一管理。</p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start"><strong>规则引擎</strong></p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">灵活的规则模型配置，支持多种规则模型以及<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jetlinks.cn%2Fdev-guide%2Frule-engine.html" target="_blank">自定义规则模型</a>。设备告警，场景联动，均由统一的规则引擎管理。</p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">超轻量级基于SQL的<a href="https://gitee.com/jetlinks/reactor-ql">实时处理引擎</a>,让数据处理更简单. </p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start"><strong>多种数据存储策略</strong></p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">支持灵活的设备<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jetlinks.cn%2Fbest-practices%2Fstart.html%23%25E5%25AD%2598%25E5%2582%25A8%25E7%25AD%2596%25E7%2595%25A5%25E9%2580%2589%25E6%258B%25A9" target="_blank">数据存储策略</a>，可将不同类型的设备数据存储到不同的地方。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">技术栈</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-boot" target="_blank">Spring Boot 2.3.x</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2F" target="_blank">Spring WebFlux</a> 响应式Web支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fr2dbc.io%2F" target="_blank">R2DBC<span><span> </span></span></a>响应式关系型数据库驱动</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fprojectreactor.io%2F" target="_blank">Project Reactor<span><span> </span></span></a>响应式编程框架</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2F" target="_blank">Netty<span><span> </span></span></a>,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvertx.io%2F" target="_blank">Vert.x<span><span> </span></span></a>高性能网络编程框架</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fcn%2Fproducts%2Fenterprise-search" target="_blank">ElasticSearch<span><span> </span></span></a>全文检索，日志，时序数据存储</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2F" target="_blank">Redis</a> 设备配置，状态管理，缓存</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2F" target="_blank">PostgreSQL<span><span> </span></span></a>业务功能数据管理</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhs-web" target="_blank">hsweb framework 4</a> 业务功能基础框架</li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:start">架构</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="886" src="https://oscimg.oschina.net/oscnet/up-66c52c602080fa89a2e30a53c81e9253d35.png" width="1030" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">1.12-RELEASE</h2> 
<p style="color:#2c3e50; text-align:start">更新时间: 2022-01-10</p> 
<p style="color:#2c3e50; text-align:start">代码分支:<span> </span><code>1.12</code></p> 
<p style="color:#2c3e50; text-align:start">主要优化:</p> 
<ol> 
 <li>增加物连接器功能,属性,功能,事件可以引用其他设备进行操作.(Pro)</li> 
 <li>视频模块增加固定视频流地址支持.(Pro)</li> 
 <li>调整虚拟属性逻辑,未设置窗口的规则,直接合并到原始属性消息中.(Pro)</li> 
 <li>性能优化.</li> 
 <li>增加根据告警记录查询设备相关数据查询条件:<span> </span><code>where id dev-alarm 'state not xxx'</code>.</li> 
 <li>修复批量<code>save</code>时,可能导致部分数据字段被设置为null.</li> 
 <li>修复<code>OpenAPI</code>可能导致堆外内存泄漏的问题.(Pro)</li> 
 <li><code>@Subscribe</code>注解可以使用表达式来引用配置值，如:<span> </span><code>@Subscribe("/device/$&#123;a.b.c:default&#125;")</code></li> 
 <li>修复默认存储策略聚合查询:相同属性不同聚合方式时，聚合值可能不对的问题.</li> 
 <li>修复边缘网关配置<code>max-message-size</code>无效的问题.(Pro)</li> 
 <li>钉钉增加机器人Webhook群通知.(Pro)</li> 
 <li>视频模块增加代理播放API,可使用平台接口直接播放直播和设备本地回放录像(播放地址固定).(Pro付费模块)</li> 
 <li>修复同一个设备告警配置多个触发条件时，可能某些条件无法触发问题.</li> 
 <li>升级log4j为<code>2.17.1</code>,升级logback为<code>1.2.9</code>.(平台未直接使用log4j,而是使用<code>log4j-to-slf4j</code>,最终使用logback).</li> 
 <li>修复最新设备数据存储中如果属性使用array类型,可能导致查询数据报错问题.(Pro)</li> 
 <li>设备重复注册时，自动更新配置等相关信息到数据库中.</li> 
</ol>
                                        </div>
                                      
</div>
            