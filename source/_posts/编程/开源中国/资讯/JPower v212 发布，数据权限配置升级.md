
---
title: 'JPower v2.1.2 发布，数据权限配置升级'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/gdzWork/jpower-ui/raw/master/docs/image/logo.png'
author: 开源中国
comments: false
date: Tue, 10 May 2022 09:11:00 GMT
thumbnail: 'https://gitee.com/gdzWork/jpower-ui/raw/master/docs/image/logo.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img height="94" src="https://gitee.com/gdzWork/jpower-ui/raw/master/docs/image/logo.png" width="250" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:left"><a href="https://gitee.com/gdzWork/JPower">https://gitee.com/gdzWork/JPower</a></p> 
<h3 style="text-align:left">JPower只是刚起步，很多功能还在开发中敬请期待......</h3> 
<h2 style="text-align:left">简介</h2> 
<p style="color:#333333; text-align:left"><code>JPower</code><span style="background-color:#ffffff; color:#525252"><span> </span>是一款基于政府商业项目升级优化而来，采用前后端分离架构：SpringBoot2.x，AVue&Vue，Mybatis-plus，JWT。前端开源了一个框架：jpower-ui；项目分包明确，规范微服务的开发模式，使包与包之间的分工清晰；部署使用Docker或K8s + Jenkins；注册中心、配置中心选型Nacos，为工程瘦身的同时加强各模块之间的联动。</span><br> <code>JPower</code><span style="background-color:#ffffff; color:#525252"><span> </span>旨在解决大部分企业项目的基础功能，例如用户管理、权限管理、附件管理等。不再为项目开发进行重复工作；本项目可做为基础框架使用，降低前后分离的开发成本，减少了开发人员的工作量，让开发人员能够专注于业务开发。</span><br> <code>JPower宗旨是:</code><span style="background-color:#ffffff; color:#525252"><span> </span>解决项目开发中所有场景的基础、共有的功能，保证在此基础上只专注于自己的业务，不用再关注基础模块;</span></p> 
<h2 style="text-align:left">功能</h2> 
<ol> 
 <li>租户管理：超级用户角色管理所有的租户创建</li> 
 <li>组织管理：部门、用户数据维护、重置用户密码等</li> 
 <li>权限设置：数据权限、角色管理、给角色绑定用户、给角色授权菜单和资源</li> 
 <li>系统设置：菜单功能、附件管理、字典、行政地区、系统参数、应用管理等</li> 
 <li>网关管理：限流和阻止访问、注册中心</li> 
 <li>系统监控：接口文档、服务监控、SkyWalking监控等</li> 
</ol> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.1.2 发布特性：</h3> 
<ol> 
 <li>接口鉴权支持@PathVariable参数</li> 
 <li>优化日志输出</li> 
 <li>新增root用户拥有所有接口权限</li> 
 <li>文件管理上传文件名优化</li> 
 <li>jpower-boot模块独立成单体项目</li> 
 <li>字典注解@Dict的attributes属性改为必填项</li> 
 <li>数据权限新增注解方式</li> 
 <li>数据权限WEB配置优化</li> 
 <li>banner修改</li> 
 <li>一些其他BUG的修改</li> 
 <li>新增@NoSqlLog注解，可在开启SQL打印的情况下针对个别SQL不打印</li> 
</ol> 
<h2 style="text-align:left">文档</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fguodingzhi%2Fjpower" target="_blank"><strong>官方文档</strong></a></li> 
</ul> 
<h2 style="text-align:left">项目地址</h2> 
<p style="color:#333333; text-align:left">前往 Gitee 搜索 JPower或点击后面的链接即可访问项目主页：<a href="https://gitee.com/gdzWork/JPower">https://gitee.com/gdzWork/JPower</a></p> 
<h2 style="text-align:left">项目演示地址</h2> 
<ul> 
 <li>项目演示地址：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjpower.top%3A81%2F" target="_blank">http://jpower.top:81</a></li> 
 <li>超级用户登录（租户编码：000000）：</li> 
 <li>超级管理员： root/123456</li> 
 <li>租户用户登录（租户编码：LXD0DP）：</li> 
 <li>普通账号： admin/123456 </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            