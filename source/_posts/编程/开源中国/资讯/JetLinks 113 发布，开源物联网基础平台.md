
---
title: 'JetLinks 1.13 发布，开源物联网基础平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-66c52c602080fa89a2e30a53c81e9253d35.png'
author: 开源中国
comments: false
date: Mon, 27 Jun 2022 11:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-66c52c602080fa89a2e30a53c81e9253d35.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:start">JetLinks 开源物联网平台</h1> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">JetLinks 基于 Java8、Spring Boot 2.x、WebFlux、Netty、Vert.x、Reactor 等开发，是一个开源的企业级物联网基础开发平台，实现了物联网相关以及相关业务开发的众多基础功能，能帮助你快速建立物联网相关业务系统。</p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">在线完整功能演示地址：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.jetlinks.cn%2F" target="_blank">http://demo.jetlinks.cn<span><span> </span></span></a>用户名:<code>test</code><span> </span>密码:<span> </span><code>test123456</code></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">测试用户未开放全部权限，建议本地运行社区版体验或者联系商务试用企业版。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">核心特性</h2> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start"><strong>开放源代码</strong></p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">全部源代码开放，可自由拓展功能，不再受制于人。前后端分离，接口全开放。</p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start"><strong>统一设备接入，海量设备管理</strong></p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">TCP/UDP/MQTT/HTTP、TLS/DTLS、不同厂商、不同设备、不同报文、统一接入，统一管理。</p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start"><strong>规则引擎</strong></p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">灵活的规则模型配置，支持多种规则模型以及<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jetlinks.cn%2Fdev-guide%2Frule-engine.html" target="_blank">自定义规则模型</a>。设备告警，场景联动，均由统一的规则引擎管理。</p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">超轻量级基于 SQL 的<a href="https://gitee.com/jetlinks/reactor-ql">实时处理引擎</a><span> </span>, 让数据处理更简单. </p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start"><strong>多种数据存储策略</strong></p> 
<p style="color:#2c3e50; margin-left:0; margin-right:0; text-align:start">支持灵活的设备<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jetlinks.cn%2Fbest-practices%2Fstart.html%23%25E5%25AD%2598%25E5%2582%25A8%25E7%25AD%2596%25E7%2595%25A5%25E9%2580%2589%25E6%258B%25A9" target="_blank">数据存储策略</a>，可将不同类型的设备数据存储到不同的地方。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">技术栈</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-boot" target="_blank">Spring Boot 2.3.x</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2F" target="_blank">Spring WebFlux</a> 响应式 Web 支持</li> 
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
<h2 style="margin-left:0; margin-right:0; text-align:start">1.13-RELEASE</h2> 
<p style="color:#2c3e50; text-align:start">发布时间: 2022-06-25</p> 
<p style="color:#2c3e50; text-align:start">代码分支:<span> </span><code>1.13</code></p> 
<p style="color:#2c3e50; text-align:start">主要优化:</p> 
<ol> 
 <li>升级<code>netty 4.1.73.Final</code>以及<code>vertx 4.2.3</code>版本,支持<code>mqtt5</code>.</li> 
 <li>修复网关子设备通过直连接入到平台时,状态可能不一致问题.</li> 
 <li>修复解绑租户成员不会触发资产解绑事件问题.(Pro)</li> 
 <li>优化设备租户信息同步逻辑(事务提交后再执行同步).(Pro)</li> 
 <li>增加在ReactorQL函数中获取设备配置信息<code>select device.config(deviceId,'password') pwd from ...</code>.</li> 
 <li>优化视频录像逻辑,优化历史录像文件信息解析性能.(Pro付费模块)</li> 
 <li>修复国标视频点播时,ssrc对应的流ID可能错误问题.(Pro付费模块)</li> 
 <li>访问日志增加只能查看自己的日志功能.(Pro)</li> 
 <li>修复标签使用object或者array类型时,可能导致无法解析问题.</li> 
 <li>完善表字段说明以及单元测试.(Pro)</li> 
 <li>增加统一的文件管理功能<code>FileManager</code>,来统一管理相对敏感的文件上传以及访问.</li> 
</ol>
                                        </div>
                                      
</div>
            