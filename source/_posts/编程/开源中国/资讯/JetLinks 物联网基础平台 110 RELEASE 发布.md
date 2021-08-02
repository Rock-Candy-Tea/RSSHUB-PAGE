
---
title: 'JetLinks 物联网基础平台 1.10 RELEASE 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e8a05bd9e63731532755669da349d7a875d.png'
author: 开源中国
comments: false
date: Mon, 02 Aug 2021 05:33:00 GMT
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
<h2 style="text-align:start">1.10-RELEASE</h2> 
<p style="text-align:start">更新时间: 2021-08-02</p> 
<p style="text-align:start">代码分支: <code>1.10</code></p> 
<ol> 
 <li>增加批量下发设备指令功能,支持查看下发记录,自动重试等(Pro)</li> 
 <li>上报属性和读取属性回复增加<code>属性源时间</code>和<code>属性状态</code>;行式存储时,会使用源时间当作时间戳进行存储.</li> 
 <li>GB28181视频接入支持预置位、看守位指令。(Pro)</li> 
 <li>ClickHouse增加指定存储策略,支持集群轮询写,分布式读。(Pro)</li> 
 <li>HTTP消息增加文件上传支持<code>HttpExchangeMessage.multiPart()</code>。(Pro)</li> 
 <li>JetLinks后端接口国际化支持(jsr303,枚举(<code>I18nEnumDict</code>),异常(<code>I18nSupportException</code>))。<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jetlinks.cn%2Fdev-guide%2Fi18n.html" target="_blank">查看说明</a></li> 
 <li>提供对游标分页查询支持,部分数据库可能不支持offset方式分页,当分页结果中<code>scoll</code>为<code>true</code>时,表示游标分页,此时不支持使用<code>pageIndex</code>进行分页,下一页查询时需要在动态查询条件中指定上一页返回的<code>scrollId</code>:<code>"context":&#123;"scrollId":"上一页的ID"&#125;</code>,并且查询条件变化后,需要重置页码以及<code>scrollId</code>.</li> 
 <li>设备数据存储策略增加<code>cassandra</code>支持,可将设备数据写入到<code>cassandra</code>中(Pro).</li> 
 <li>增加数据源管理,统一管理各种数据源(RabbitMQ,Kafka)等(Pro).</li> 
 <li>增加RabbitMQ数据源实现,支持<code>创建生产者,消费者</code>,<code>RabbitMQ管理功能(添加用户,权限等)</code>(Pro).</li> 
 <li>规则引擎中增加RabbitMQ,Kafka转发节点(Pro).</li> 
 <li>规则引擎节点增加权限控制支持,可通过<code>rule.engine.executor-filter</code>进行相关配置(Pro).</li> 
 <li>规则引擎<code>ReactorQL</code>节点支持租户权限控制,<code>rule.engine.task-executor.reactor-ql.enable-tenant=true</code>开启.(Pro)</li> 
 <li>规则引擎设备指令节点发送指令发生异常时,将返回转为消息回复,而不是抛出异常.</li> 
 <li>规则引擎在启动时，自动启动全部规则中符合调度策略的任务，实现添加新的集群节点自动启动任务.(Pro)</li> 
 <li>子设备自动注册时,同时绑定设备资产到网关所在到租户用户下(Pro).</li> 
 <li>优化设备会话状态,如果同一个设备在不同的集群节点连接,以最后连接的为准,之前的会断开(Pro).</li> 
 <li><code>MQTT Broker</code>方式接入设备支持设置QoS.</li> 
 <li>增加<code>FileQueue</code>工具类,可将队列数据持久化到本地文件.</li> 
 <li>增加<code>ParallelIntervalHelper</code>工具类,可对并行操作进行延迟来实现并行转串行的效果.</li> 
 <li><code>DeviceDataManager</code>接口增加<code>getTags</code>方法,可在协议包中通过此方式来获取设备标签.</li> 
 <li>在TCP网络组件中的粘拆包处理方式脚本中增加<code>parser.newBuffer()</code>方法,<a href="https://gitee.com/jetlinks/jetlinks-community/blob/master/jetlinks-components/network-component/tcp-component/src/test/java/org/jetlinks/community/network/tcp/parser/strateies/ScriptPayloadParserBuilderTest.java#L63-73" target="_blank">使用方法</a>.</li> 
</ol> 
<p style="text-align:start">Bug修复:</p> 
<ol> 
 <li>修复关闭权限验证时，可能无法使用<code>POST</code>动态查询问题</li> 
 <li>修复CoAP停止后无法重启的问题</li> 
 <li>修复部分网络组件未配置线程数则无法启动的问题</li> 
 <li>修复集群下,设备历史在线统计可能不准确的问题</li> 
</ol>
                                        </div>
                                      
</div>
            