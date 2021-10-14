
---
title: 'JetLinks 1.11 发布，开源物联网基础平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-47ce3bf43e228df5e931111ed40bde09b0a.png'
author: 开源中国
comments: false
date: Thu, 14 Oct 2021 10:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-47ce3bf43e228df5e931111ed40bde09b0a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="text-align:start">JetLinks 开源物联网平台</h1> 
<p style="color:#2c3e50; text-align:start">JetLinks 基于Java8、Spring Boot 2.x、WebFlux、Netty、Vert.x、Reactor 等开发，是一个开源的企业级物联网基础开发平台，实现了物联网相关以及相关业务开发的众多基础功能，能帮助你快速建立物联网相关业务系统。</p> 
<p style="color:#2c3e50; text-align:start">在线演示地址：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.jetlinks.cn%2F" target="_blank">http://demo.jetlinks.cn<span><span> </span></span></a>用户名:<code>test</code><span> </span>密码:<span> </span><code>test123456</code></p> 
<p>测试用户未开放全部权限，建议本地运行社区版体验或者联系商务试用企业版。</p> 
<h2 style="text-align:start">核心特性</h2> 
<p style="color:#2c3e50; text-align:start"><strong>开放源代码</strong></p> 
<p style="color:#2c3e50; text-align:start">全部源代码开放，可自由拓展功能，不再受制于人。前后端分离，接口全开放。</p> 
<p style="color:#2c3e50; text-align:start"><strong>统一设备接入,海量设备管理</strong></p> 
<p style="color:#2c3e50; text-align:start">TCP/UDP/MQTT/HTTP、TLS/DTLS、不同厂商、不同设备、不同报文、统一接入，统一管理。</p> 
<p style="color:#2c3e50; text-align:start"><strong>规则引擎</strong></p> 
<p style="color:#2c3e50; text-align:start">灵活的规则模型配置，支持多种规则模型以及<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jetlinks.cn%2Fdev-guide%2Frule-engine.html" target="_blank">自定义规则模型</a>。设备告警，场景联动，均由统一的规则引擎管理。</p> 
<p style="color:#2c3e50; text-align:start"><strong>强大的可视化规则设计器</strong></p> 
<p><img height="979" src="https://oscimg.oschina.net/oscnet/up-47ce3bf43e228df5e931111ed40bde09b0a.png" width="1911" referrerpolicy="no-referrer"></p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <p><strong>说明</strong></p> 
 <p>可视化规则设计器基于 node-red，后端使用纯 Java 实现.</p> 
</div> 
<p style="color:#2c3e50; text-align:start"><strong>数据权限控制</strong></p> 
<p style="color:#2c3e50; text-align:start">灵活的非侵入<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jetlinks.cn%2Fdev-guide%2Fassets.html" target="_blank">数据权限控制</a>，可实现不同机构、不同用户共享数据，可控制单条数据的操作权限。支持自定义维度(公司,部门...)</p> 
<p style="color:#2c3e50; text-align:start"><strong>多种数据存储策略</strong></p> 
<p style="color:#2c3e50; text-align:start">支持灵活的设备<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jetlinks.cn%2Fbest-practices%2Fstart.html%23%25E5%25AD%2598%25E5%2582%25A8%25E7%25AD%2596%25E7%2595%25A5%25E9%2580%2589%25E6%258B%25A9" target="_blank">数据存储策略</a>，可将不同类型的设备数据存储到不同的地方。</p> 
<h2 style="text-align:start">技术栈</h2> 
<ol> 
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
<h2 style="text-align:start">架构</h2> 
<p><img height="886" src="https://oscimg.oschina.net/oscnet/up-66c52c602080fa89a2e30a53c81e9253d35.png" width="1030" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">1.11-RELEASE</h2> 
<p style="color:#2c3e50; text-align:start">更新时间： 2021-10-13</p> 
<p style="color:#2c3e50; text-align:start">代码分支：<span> </span><code>1.11</code></p> 
<p style="color:#2c3e50; text-align:start">主要优化：</p> 
<ol> 
 <li>租户成员可指定授予租户内全部数据权限（Pro）</li> 
 <li>增加数据权限功能，可将数据绑定到任意维度(角色,机构)中，实现数据权限控制。支持对单条数据的操作级别控制 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jetlinks.cn%2Fdev-guide%2Fassets.html" target="_blank">查看说明</a> （Pro）</li> 
 <li>设备协议<code>CompositeProtocolSupport.onBeforeDeviceCreate</code>增加自定义设备信息,在创建设备时,可自定义生成设备的相关配置</li> 
 <li>视频模块 GB28181 查看录像、快进、暂停、跳转播放 (Pro选配模块)</li> 
 <li>完善单元测试（Pro）</li> 
 <li>优化实体事件，增加<code>EntityBeforeXXX</code>,<code>EntityPrepareXXX</code>事件</li> 
 <li>增加相关资产数据级联操作：绑定设备时自动绑定产品，绑定产品时自动绑定产品分类等 (Pro)</li> 
 <li>拓展<code>spring.r2dbc.pool</code>相关配置，支持配置连接有效期</li> 
 <li>邮件通知模版中表达式增加对html的处理，解决部分富文本编辑器会把表达式转为html</li> 
 <li>增加对<code>Elasticsearch</code>数据权限控制的查询条件支持(Pro)</li> 
 <li>设备消息统计支持数据权限控制 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jetlinks.cn%2Fdev-guide%2Fmicrometer.html%23%25E8%25AE%25BE%25E5%25A4%2587%25E7%25BB%259F%25E8%25AE%25A1" target="_blank">查看说明</a> (Pro)</li> 
 <li>优化菜单管理,可根据菜单进行赋权(前端暂未实现)</li> 
 <li>优化物模型转换时的精度处理</li> 
 <li>规则引擎事件中的数据增加：<code>modelType(模型类型)</code>，<code>jobExecutor(节点执行器)</code>，<code>ruleConf(规则的其他配置信息)</code>配置，可在直接从事件数据中获取进行处理</li> 
 <li>在关联子设备时增加循环依赖检查</li> 
 <li>云云对接-Dueros 支持场景了，可通过小度音响控制场景规则 ( Pro 选配模块)</li> 
</ol> 
<p style="color:#2c3e50; text-align:start"><strong>BUG修复</strong></p> 
<ol> 
 <li>修复 GB28181 可能导致内存泄漏问题(未应答无法一些无法处理的指令)</li> 
 <li>修复 GB28181 级联点播时，sdp为空时无法点播的问题</li> 
 <li>修复使用 pgsql 进行大量 insert 操作时，pgsql 占用内存过高问题</li> 
 <li>修复存在同类名协议包会出现冲突的问题</li> 
 <li>修复通知模版表达式中，表达式内容超过 128 引起数组下标越界问题</li> 
 <li>修复设备分组和设备网关会查询出没有权限的设备问题</li> 
 <li>修复规则引擎无法捕获全部节点事件的问题</li> 
</ol> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <p style="color:#b29400"><strong>更新说明</strong></p> 
 <p>此版本重构了租户功能,并增加数据权限控制相关功能.</p> 
 <p>升级可能需要替换部分 API 包名，如:</p> 
 <ol> 
  <li>使用<code>org.jetlinks.pro.assets.Asset</code>替换<code>org.jetlinks.pro.tenant.TenantAsset</code></li> 
  <li>使用<code>org.jetlinks.pro.assets.AssetType</code>替换<code>org.jetlinks.pro.tenant.AssetType</code></li> 
  <li>使用<code>AssetsHolderCrudController</code>替换<code>TenantAccessCrudController</code></li> 
  <li>使用<code>CorrelatesAssetsHolderCrudController</code>替换<code>TenantCorrelatesAccessCrudController</code></li> 
  <li>使用<code>CorrelatesAssetsHolderQueryController</code>替换<code>CorrelatesAssetsHolderQueryController</code></li> 
  <li>使用注解<code>AssetsController</code>替换<code>TenantAssets</code></li> 
 </ol> 
 <p><code>AssetsHolder</code>：针对租户以及其他自定义的数据权限相关操作</p> 
 <p><code>TenantMember</code>：只针对租户进行数据权限相关操作</p> 
</div>
                                        </div>
                                      
</div>
            