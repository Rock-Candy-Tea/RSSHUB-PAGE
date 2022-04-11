
---
title: '携程配置管理平台 Apollo 发布 2.0.0 RC1，支持 Java 17'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-dddbdd40e6281614f3ae6325914610bff39.png'
author: 开源中国
comments: false
date: Mon, 11 Apr 2022 18:39:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-dddbdd40e6281614f3ae6325914610bff39.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apollo 2.0.0-RC1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Forrn6UpAME7Zq5bB450s4A" target="_blank">已发布</a>，此次发布是 Apollo 自 1.0.0 以来的又一次大版本更新，包含了诸如 Java 17 支持、Java 1.7 不再支持、唯一键索引、Spring Boot 版本升级等重大更新。GA 版本预计一个月后发布。</p> 
<hr> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>Java 17 支持</strong></p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">Apollo 客户端和服务端均已支持 Java 8、11 和 17 版本。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>公共 Namespace 列表页</strong></p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">Apollo 主页新增了公共 Namespace 列表视图，用户可以在此页面上查看和搜索公共 Namespace。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-dddbdd40e6281614f3ae6325914610bff39.png" referrerpolicy="no-referrer"></p> 
<p><strong>灰度发布支持标签</strong></p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">灰度规则支持通过标签来标识灰度的实例列表，适用于 IP 不固定的场景如 Kubernetes。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1d096ce0d0a64f2c220963dd227b2716af7.png" referrerpolicy="no-referrer"></p> 
<p><strong>配置导入导出功能增强</strong></p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">批量配置导入导出功能进行了重新设计并增强。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a28ebda27472aa44e87799e3d39fa56d27f.png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#24292f">每个 Namespace 下现也已支持单独导入和导出。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-3339e83836193c3a7c622f3dc7465ef6451.png" referrerpolicy="no-referrer"></p> 
<p><strong>唯一键索引</strong></p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">由于软删除的设计，Apollo 之前版本的数据库除主键外没有唯一键约束，在一些并发的情况下可能会遇到重复数据的问题。基于 2.0.0 版本新增的 DeletedAt 列，我们为大多数表都增加了唯一索引。</p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start"><strong>Spring Boot 和 Spring Cloud 版本升级</strong></p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">Apollo 服务端的 Spring Boot 和 Spring Cloud 分别升级到了 2.6.6 和 2021.0.1 版本。</p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start"><strong>不兼容更新 </strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">apollo-client 从 2.0.0 版本开始<strong>不再支持 Java 1.7 版本</strong>，最低的 Java 运行时环境是 1.8。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapolloconfig%2Fapollo%2Freleases%2Ftag%2Fv2.0.0-RC1" target="_blank">详情查看 release note</a>。</p> 
<hr> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>关于 Apollo</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Apollo 项目于 2016 年在携程框架研发部诞生，初衷是为了解决公司内部配置管理尤其是中间件公共配置的管理难题，秉持着开源开放的精神，项目从第一行代码开始就在 GitHub 上开源，可以说是一个完全开放的项目。经过多年的发展，Apollo 以其功能丰富、简单易用等特性，得到了社区开发者的欢迎，也已在数百家公司中得到广泛使用。</p>
                                        </div>
                                      
</div>
            