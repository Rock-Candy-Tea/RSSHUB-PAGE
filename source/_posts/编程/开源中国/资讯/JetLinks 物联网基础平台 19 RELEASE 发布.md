
---
title: 'JetLinks 物联网基础平台 1.9 RELEASE 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e8a05bd9e63731532755669da349d7a875d.png'
author: 开源中国
comments: false
date: Mon, 31 May 2021 10:30:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e8a05bd9e63731532755669da349d7a875d.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="text-align:start">JetLinks 开源物联网平台</h1> 
<p style="text-align:start">JetLinks 基于Java8,Spring Boot 2.x,WebFlux,Netty,Vert.x,Reactor等开发, 是一个开箱即用,可二次开发的企业级物联网基础平台。平台实现了物联网相关的众多基础功能, 能帮助你快速建立物联网相关业务系统。</p> 
<h2 style="text-align:start">核心特性</h2> 
<p style="text-align:start">完全开源(社区版免费),基于事件驱动,拓展性强.</p> 
<p style="text-align:start">支持统一物模型管理,多种设备,多种厂家,多种报文,统一管理。</p> 
<p style="text-align:start">统一设备连接管理,多协议适配(TCP,MQTT,UDP,CoAP,HTTP等),屏蔽网络编程复杂性,灵活接入不同厂家不同协议的设备。</p> 
<p style="text-align:start">灵活的规则引擎,设备告警,消息通知,数据转发,场景联动.</p> 
<p style="text-align:start">强大的<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jetlinks.cn%2Fdev-guide%2Freactor-ql.html" target="_blank">ReactorQL</a>引擎,使用SQL来处理实时数据.可拓展自定义函数.</p> 
<p style="text-align:start">地理位置:统一管理地理位置信息,支持区域搜索.</p> 
<p style="text-align:start">灵活的非侵入<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jetlinks.cn%2Fdev-guide%2Fmulti-tenant.html" target="_blank">多租户</a>数据权限控制.</p> 
<p style="text-align:start">在线演示地址: <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.jetlinks.cn%2F" target="_blank">http://demo.jetlinks.cn </a>用户名:<code>test</code> 密码: <code>test123456</code>.</p> 
<h2 style="text-align:start">技术栈</h2> 
<ol> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-boot" target="_blank">Spring Boot 2.3.x</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2F" target="_blank">Spring WebFlux </a>响应式Web支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fr2dbc.io%2F" target="_blank">R2DBC </a>响应式关系型数据库驱动</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fprojectreactor.io%2F" target="_blank">Project Reactor </a>响应式编程框架</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2F" target="_blank">Netty </a>,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvertx.io%2F" target="_blank">Vert.x </a>高性能网络编程框架</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fcn%2Fproducts%2Fenterprise-search" target="_blank">ElasticSearch </a>全文检索，日志，时序数据存储</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2F" target="_blank">Redis</a>,设备配置,状态管理,缓存.</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2F" target="_blank">PostgreSQL </a>业务功能数据管理</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhs-web" target="_blank">hsweb framework 4 </a>业务功能基础框架</li> 
</ol> 
<h2 style="text-align:start">架构</h2> 
<p style="text-align:start"><img height="886" src="https://oscimg.oschina.net/oscnet/up-e8a05bd9e63731532755669da349d7a875d.png" width="1030" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">设备接入流程</h2> 
<p style="text-align:start"><img height="771" src="https://oscimg.oschina.net/oscnet/up-6d6f85dc9dfcf843a1ce4d821075d702991.png" width="897" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">1.9-RELEASE</h2> 
<ol> 
 <li>增加设备独立物模型支持,可给单独的设备配置物模型.</li> 
 <li>基本实现GB28181国标视频设备接入,支持<code>直播</code>,<code>云台控制</code>,<code>级联操作</code>.(选配模块)</li> 
 <li>RabbitMQ增加<code>routeKey</code>配置,可在配置文件中指定<code>device.message.writer.rabbitmq.consumer-route-key</code>和<code>device.message.writer.rabbitmq.producer-route-key</code>.（Pro）</li> 
 <li>当设置了<code>device.message.writer.rabbitmq.consumer=false</code>时,不创建MQ消费者.(Pro)</li> 
 <li>设备支持独立物模型,可单独配置设备的物模型.</li> 
 <li>适配<code>tdengine 2.0.16.0</code>,优化sql长度策略. (pro)</li> 
 <li>优化规则引擎编辑器,实现组件模块化动态加载.（Pro）</li> 
 <li>修复启动服务时,如果某个产品物模型发布失败,导致后面的产品终止发布的问题.</li> 
 <li>增加<code>ignoreLatest</code>消息头,<code>message.addHeader("ignoreLatest",true)</code> 忽略记录最新数据到数据库.</li> 
 <li>修复租户下操作设备告警提示无权限.(Pro)</li> 
 <li>优化租户在解绑成员时,同时解绑成员的资产信息.(Pro)</li> 
 <li>优化子设备消息回复处理</li> 
 <li>物模型属性增加存储方式功能,可配置部分属性不存储.</li> 
 <li>增加虚拟属性功能,可通过规则来计算出虚拟属性值.(Pro)</li> 
 <li>增加租户成员绑定(<code>TenantMemberBindEvent</code>),解绑(<code>TenantMemberUnBindEvent</code>)事件.可通过<code>spring-event</code>订阅处理此事件.(Pro)</li> 
 <li>优化子设备状态检查，当检查子设备状态时，将会尝试发送<code>ChildDeviceMessage<DeviceStateCheckMessage></code>给网关，处理后返回<code>ChildDeviceMessageReply<DeviceStateCheckMessageReply></code>.</li> 
 <li>增加<code>ClickHouse</code>设备数据存储策略支持.(Pro)</li> 
 <li>增加权限过滤功能,可配置禁止赋予自己没有的权限给其他用户.<code>hsweb.permission.filter</code>相关配置</li> 
 <li>设备和产品的租户绑定逻辑优化: 绑定设备时，自动绑定产品.解绑产品时,自动解绑设备.(Pro)</li> 
 <li>用户管理增加租户权限控制.(Pro)</li> 
 <li>当向<code>keepOnline</code>当设备发送消息时,如果原始连接已断开,将返回<code>CONNECTION_LOST</code>错误.</li> 
 <li>设置<code>keepOnline</code>的会话将被持久化,重启服务后自动恢复.(Pro)</li> 
</ol>
                                        </div>
                                      
</div>
            