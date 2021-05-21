
---
title: 'BudWk 7.0.0 发布，微服务网关 + 组件化 + API 接口化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/budwk/budwk/raw/v7.x/main.png'
author: 开源中国
comments: false
date: Fri, 21 May 2021 11:32:00 GMT
thumbnail: 'https://gitee.com/budwk/budwk/raw/v7.x/main.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">BudWk V7 进行了大量重构，与之前版本结构大不相同，增加网关中心、认证中心、控制中心等，并且完全组件化、配置化，大大减轻开发工作量，提升开发效率的同时为产品升级迭代提供了极大便利。</p> 
<p style="text-align:left">BudWk 原名 NutzWk ，是基于国产框架 nutz 及 nutzboot 开发的开源Web基础项目，集权限体系、系统参数、数据字典、站内消息、定时任务、CMS、微信等最常用功能，不庞杂、不面面俱到，使其具有上手容易、开发便捷、扩展灵活等特性，特别适合各类大中小型定制化项目需求。</p> 
<p style="text-align:left">自2012年开源至今，以“在力所能及的情况下，最大限度的提高Web开发人员的生产力”为宗旨，紧跟时代技术发展，发布V1-V7多个版本，也尝试在开源和持续发展的道路上求索。</p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbudwk.com%2F" target="_blank">https://budwk.com</a> 官网</p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.budwk.com%2F" target="_blank">https://demo.budwk.com</a> V7演示地址</p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnutzwk.wizzer.cn%2F" target="_blank">https://nutzwk.wizzer.cn</a> V5演示地址</p> 
<h1 style="text-align:left">本版说明(BudWk v7.x)</h1> 
<h2 style="text-align:left">运行环境</h2> 
<ul> 
 <li>JDK 11 + 或 OpenJDK 11 +</li> 
 <li>Redis 4.0.8 +</li> 
 <li>MySql 5.7 + 或 MariaDB、Oracle、SqlServer、达梦等</li> 
 <li>Nacos 2.0.0 +</li> 
</ul> 
<h2 style="text-align:left">开发工具</h2> 
<ul> 
 <li>IntelliJ IDEA</li> 
 <li>Visual Studio Code</li> 
 <li>Node 12.13.0 +</li> 
 <li>Maven 3.5.3 +</li> 
 <li>Git</li> 
</ul> 
<h2 style="text-align:left">架构图</h2> 
<p style="text-align:left"><img alt="BUDWK架构" src="https://gitee.com/budwk/budwk/raw/v7.x/main.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">目录结构</h2> 
<div style="text-align:left"> 
 <div> 
  <pre>budwk                               <span style="color:#888888">-- 根目录</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter                     <span style="color:#888888">-- 组件中心</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter-common           <span style="color:#888888">-- 通用类组件</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter-database         <span style="color:#888888">-- 数据库组件</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter-dependencies     <span style="color:#888888">-- 所有依赖</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter-dubbo            <span style="color:#888888">-- Dubbo组件</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter-email            <span style="color:#888888">-- Email组件</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter-gateway          <span style="color:#888888">-- 网关组件</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter-job              <span style="color:#888888">-- 简易定时任务组件</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter-log              <span style="color:#888888">-- 日志及SLog组件</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter-openapi          <span style="color:#888888">-- 接口文档生成组件</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter-security         <span style="color:#888888">-- 权限验证组件</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter-sms              <span style="color:#888888">-- 短信发送组件</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter-storage          <span style="color:#888888">-- 文件存储组件</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-starter-web              <span style="color:#888888">-- WEB拦截跨越表单验证组件</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-gateway                     <span style="color:#888888">-- 网关中心</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-platform                    <span style="color:#888888">-- 控制中心</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-platform-common          <span style="color:#888888">-- 通用类供其他模块调用</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-platform-server          <span style="color:#888888">-- 服务类提供API服务</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-ucenter                     <span style="color:#888888">-- 认证中心</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-cms                         <span style="color:#888888">-- 简易CMS</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-cms-common               <span style="color:#888888">-- 通用类供其他模块调用</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-cms-server               <span style="color:#888888">-- 服务类提供API服务</span>
<span style="background-color:#ffadad; color:#a61717">│</span>  <span style="background-color:#ffadad; color:#a61717">├─</span>wk-vue-admin                   <span style="color:#888888">-- Vue前端代码</span></pre> 
 </div> 
</div> 
<h2 style="text-align:left">技术选型</h2> 
<h3 style="text-align:left">后端技术</h3> 
<table cellspacing="0" style="width:634px"> 
 <thead> 
  <tr> 
   <th>技术</th> 
   <th>名称</th> 
   <th>官网</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">Nutz</td> 
   <td style="border-color:#dfe2e5">JavaEE应用框架</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnutzam.com%2F" target="_blank">https://nutzam.com</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">NutzBoot</td> 
   <td style="border-color:#dfe2e5">微服务框架</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnutzam%2Fnutzboot" target="_blank">https://github.com/nutzam/nutzboot</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">SaToken</td> 
   <td style="border-color:#dfe2e5">权限框架</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsa-token.dev33.cn%2F" target="_blank">http://sa-token.dev33.cn</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Druid</td> 
   <td style="border-color:#dfe2e5">数据库连接池</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fdruid" target="_blank">https://github.com/alibaba/druid</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Nacos</td> 
   <td style="border-color:#dfe2e5">配置及注册中心</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnacos.io%2F" target="_blank">https://nacos.io</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Dubbo</td> 
   <td style="border-color:#dfe2e5">分布式服务框架</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdubbo.apache.org%2F" target="_blank">https://dubbo.apache.org</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Redis</td> 
   <td style="border-color:#dfe2e5">分布式缓存数据库</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2F" target="_blank">https://redis.io</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Quartz</td> 
   <td style="border-color:#dfe2e5">作业调度框架</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.quartz-scheduler.org%2F" target="_blank">https://www.quartz-scheduler.org</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">IdGenerator</td> 
   <td style="border-color:#dfe2e5">雪花主键生成</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyitter%2FIdGenerator" target="_blank">https://github.com/yitter/IdGenerator</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Hutool</td> 
   <td style="border-color:#dfe2e5">工具集合</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhutool.cn%2F" target="_blank">https://hutool.cn</a></td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="text-align:left">前端技术</h3> 
<table cellspacing="0" style="width:634px"> 
 <thead> 
  <tr> 
   <th>技术</th> 
   <th>名称</th> 
   <th>官网</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">Vue.js</td> 
   <td style="border-color:#dfe2e5">MVVM框架</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvuejs.org%2F" target="_blank">https://vuejs.org</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Nuxt.js</td> 
   <td style="border-color:#dfe2e5">Vue通用应用框架</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnuxtjs.org%2F" target="_blank">https://nuxtjs.org</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Element</td> 
   <td style="border-color:#dfe2e5">基于Vue的UI框架</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Felement.eleme.io%2F" target="_blank">https://element.eleme.io</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Font-awesome</td> 
   <td style="border-color:#dfe2e5">字体图标</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffontawesome.com%2F" target="_blank">https://fontawesome.com</a></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            