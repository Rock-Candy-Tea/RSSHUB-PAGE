
---
title: 'JavaWeb 敏捷开发框架 EleVue 版本 v1.7.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3571'
author: 开源中国
comments: false
date: Sat, 17 Sep 2022 08:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3571'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">v1.7.0更新内容：<br> 1、升级优化菜单管理模块，采用异步加载的方式加载菜单，解决前期加载耗时的问题；<br> 2、自定义代码生成器模板，新增前端自定义模板Index.vue.ftl;<br> 3、完善代码生成器工具类CodeGenerateUtils;<br> 4、菜单权限管理新增权限节点穿梭组件自定义选择节点权限的功能，一键快捷创建菜单节点；<br> 5、完善代码生成器功能，一键生成整个模块的所有后端文件和业务代码；<br> 6、前端代码生成器升级，可以同步生成前端模块的完整模块代码，同时创建节点，赋予权限编译后即可运行；<br> 7、解决前期用户使用过程中反馈的BUG；</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">一款 Java 语言基于 SpringBoot2.x、MybatisPlus、Vue、ElementUI、MySQL 等框架精心打造的一款前后端分离框架，致力于实现模块化、组件化、可插拔的前后端分离架构敏捷开发框架，可用于快速搭建前后端分离后台管理系统，本着简化开发、提升开发效率的初衷，目前框架已集成了完整的 RBAC 权限架构和常规基础模块，前端 Vue 端支持多主题切换，可以根据自己喜欢的风格选择想一个的主题，实现了个性化呈现的需求；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">为了敏捷快速开发，提升研发效率，框架内置了一键 CRUD 代码生成器，自定义了模块生成模板，可以根据已建好的表结构 (字段注释需规范) 快速的一键生成整个模块的所有代码和增删改查等等功能业务，真正实现了低代码开发，极大的节省了人力成本的同时提高了开发效率，缩短了研发周期，是一款真正意义上实现组件化、低代码敏捷开发框架。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">内置模块</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>用户管理：用于维护管理系统的用户，常规信息的维护与账号设置。</li> 
 <li>角色管理：角色菜单管理与权限分配、设置角色所拥有的菜单权限。</li> 
 <li>菜单管理：配置系统菜单，操作权限，按钮权限标识等。</li> 
 <li>职级管理：主要管理用户担任的职级。</li> 
 <li>岗位管理：主要管理用户担任的岗位。</li> 
 <li>部门管理：主要管理系统组织架构，对组织架构进行统一管理维护。</li> 
 <li>操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。</li> 
 <li>登录日志：系统登录日志记录查询包含登录异常。</li> 
 <li>字典管理：对系统中常用的较为固定的数据进行统一维护。</li> 
 <li>配置管理：对系统的常规配置信息进行维护，网站配置管理功能进行统一维护。</li> 
 <li>城市管理：统一对全国行政区划进行维护，对其他模块提供行政区划数据支撑。</li> 
 <li>友链管理：对系统友情链接、合作伙伴等相关外链进行集成维护管理的模块。</li> 
 <li>个人中心：主要是对当前登录用户的个人信息进行便捷修改的功能。</li> 
 <li>广告管理：主要对各终端的广告数据进行管理维护。</li> 
 <li>站点栏目：主要对大型系统网站等栏目进行划分和维护的模块。</li> 
 <li>会员管理：对各终端注册的会员进行统一的查询与管理的模块。</li> 
 <li>网站配置：对配置管理模块的数据源动态解析与统一维护管理的模块。</li> 
 <li>通知公告：系统通知公告信息发布维护。</li> 
 <li>代码生成：一键生成模块 CRUD 的功能，包括后端和前端 Vue 等相关代码。</li> 
 <li>案例演示：常规代码生成器一键生成后的演示案例。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">开发者信息</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>软件名称：JavaWeb 敏捷开发框架 EleVue 版本</li> 
 <li>官网网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.javaweb.vip" target="_blank">http://www.javaweb.vip</a></li> 
 <li>文档网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.vue.pro.javaweb.vip" target="_blank">http://docs.vue.pro.javaweb.vip</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">系统演示</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.vue.pro.javaweb.vip" target="_blank">http://manage.vue.pro.javaweb.vip</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">版本说明</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>版本名称</th> 
   <th>说明</th> 
   <th>地址</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">JavaWeb 混编专业版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 SpringBoot2+Thymeleaf+layui</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/javaweb520/JavaWeb">https://gitee.com/javaweb520/JavaWeb</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">JavaWeb_Pro 混编旗舰版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 SpringBoot2+Thymeleaf+layui</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/javaweb520/JavaWeb_Pro">https://gitee.com/javaweb520/JavaWeb_Pro</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">JavaWeb_Vue 专业版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">前后端分离版，采用 SpringBoot2+Vue+ElementUI</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/javaweb520/JavaWeb_Vue">https://gitee.com/javaweb520/JavaWeb_Vue</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">JavaWeb_Vue_Pro 旗舰版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 SpringBoot2+Vue+ElementUI</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/javaweb520/JavaWeb_Vue_Pro">https://gitee.com/javaweb520/JavaWeb_Vue_Pro</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">JavaWeb_Ant_Pro 旗舰版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 SpringBoot2+Vue+AntDesign</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/javaweb520/JavaWeb_Ant_Pro">https://gitee.com/javaweb520/JavaWeb_Ant_Pro</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">JavaWeb_Cloud 微服务专业版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 SpringCloud+Vue+ElementUI</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/javaweb520/JavaWeb_Cloud">https://gitee.com/javaweb520/JavaWeb_Cloud</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">JavaWeb_Cloud_Pro 微服务旗舰版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 SpringCloud+Vue+ElementUI</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/javaweb520/JavaWeb_Cloud_Pro">https://gitee.com/javaweb520/JavaWeb_Cloud_Pro</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">JavaWeb_Cloud_Ant 微服务旗舰版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 SpringCloud+Vue+AntDesign</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/javaweb520/JavaWeb_Cloud_Ant">https://gitee.com/javaweb520/JavaWeb_Cloud_Ant</a></td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">特别鸣谢</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">感谢<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.baomidou.com%2F" target="_blank">MybatisPlus</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcn.vuejs.org" target="_blank">Vue</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN" target="_blank">ElementUI</a><span> </span>等优秀开源项目。</p>
                                        </div>
                                      
</div>
            