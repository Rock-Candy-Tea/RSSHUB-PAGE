
---
title: 'SpringBlade 3.2.0 发布，新增灵活数据权限特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/201905/05103447_GA1q.png'
author: 开源中国
comments: false
date: Fri, 05 Nov 2021 09:57:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/201905/05103447_GA1q.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0; text-align:left"><strong>简介：</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">SpringBlade 是由一个商业级项目升级优化而来的 SpringCloud 微服务架构，采用 Java8 API 重构了业务代码，完全遵循阿里巴巴编码规范。采用 Spring Boot 2.5 、Spring Cloud 2020 、Mybatis 等核心技术，用于快速搭建企业级的 SaaS 微服务系统平台。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">SpringBlade 同时提供 SpringBoot 单体架构版本，为中小型项目保驾护航，可与两套分别基于 React 和 Vue 的前端框架无缝对接。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">SpringBlade 致力于创造新颖的开发模式，将开发中遇到的痛点、生产中所踩的坑整理归纳，并将解决方案都融合到框架中。</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>版本更新信息：</strong></h3> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>升级 SpringBoot 至 2.5.6</li> 
 <li>升级 SpringBootAdmin 至 2.5.3</li> 
 <li>升级 SpringCloud 至 2020.0.4</li> 
 <li>升级 Nacos 至 2.0.3</li> 
 <li>升级 Knife4j 至 2.0.9</li> 
 <li>升级 Mybatis-Plus 至 3.4.3.4</li> 
 <li>新增注解配置数据权限特性</li> 
 <li>新增Web在线配置数据权限特性</li> 
 <li>新增自定义Sql配置数据权限特性</li> 
 <li>新增懒加载表格树特性</li> 
 <li>新增部门管理祖级节点字段</li> 
 <li>新增CacheUtil工具类</li> 
 <li>优化部门管理新增逻辑</li> 
 <li>优化租户拦截器初始化逻辑</li> 
 <li>优化适配各新版本API变动</li> 
</ol> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>SpringBlade 系列项目地址：</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">前端 UI 项目地址(基于 React)：<a href="https://gitee.com/smallc/Sword">Sword</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">前端 UI 项目地址(基于 Vue)：<a href="https://gitee.com/smallc/Saber">Saber</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">核心框架项目地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchillzhuang%2Fblade-tool.git" target="_blank">BladeTool</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">后端框架项目地址：<a href="https://gitee.com/smallc/SpringBlade">SpringBlade</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">后端 SpringBoot 版本地址：<a href="https://gitee.com/smallc/SpringBlade/tree/2.0-boot/">BladeBoot</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">发行版地址：<a href="https://gitee.com/smallc/SpringBlade/releases">https://gitee.com/smallc/SpringBlade/releases</a></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>官网演示地址：</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">Blade 官网地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbladex.vip%2F" target="_blank">Blade</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Sword 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsword.bladex.vip%2F" target="_blank">Sword 演示</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Saber 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsaber.bladex.vip%2F" target="_blank">Saber 演示</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Archer 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Farcher.bladex.vip%2F" target="_blank">Archer 演示</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Caster 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdata.avuejs.com%2F" target="_blank">Caster 演示</a></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>系统界面一览</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt height="339" src="https://static.oschina.net/uploads/img/201905/05103447_GA1q.png" width="700" referrerpolicy="no-referrer"><img alt height="336" src="https://static.oschina.net/uploads/img/201905/05103447_OUvJ.png" width="700" referrerpolicy="no-referrer"><img alt height="388" src="https://static.oschina.net/uploads/img/201905/05103447_jQls.png" width="700" referrerpolicy="no-referrer"></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="389" src="https://static.oschina.net/uploads/img/201905/05103447_Kg7V.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="422" src="https://static.oschina.net/uploads/img/201905/05103448_AXa8.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt height="354" src="https://static.oschina.net/uploads/img/201905/05103448_2Btr.png" width="700" referrerpolicy="no-referrer"></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt height="380" src="https://static.oschina.net/uploads/img/201905/05103448_EyDG.png" width="700" referrerpolicy="no-referrer"></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt height="381" src="https://static.oschina.net/uploads/img/201905/05103449_HAor.png" width="700" referrerpolicy="no-referrer"></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="378" src="https://static.oschina.net/uploads/img/201905/05103451_DnCK.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt height="347" src="https://static.oschina.net/uploads/img/201905/05103452_NVS3.png" width="700" referrerpolicy="no-referrer"><img alt height="349" src="https://static.oschina.net/uploads/img/201905/05103453_wskj.png" width="700" referrerpolicy="no-referrer"><img alt height="348" src="https://static.oschina.net/uploads/img/201905/05103453_pbHV.png" width="700" referrerpolicy="no-referrer"><img alt height="348" src="https://static.oschina.net/uploads/img/201905/05103454_JmSJ.png" width="700" referrerpolicy="no-referrer"></strong></p> 
<p> </p>
                                        </div>
                                      
</div>
            