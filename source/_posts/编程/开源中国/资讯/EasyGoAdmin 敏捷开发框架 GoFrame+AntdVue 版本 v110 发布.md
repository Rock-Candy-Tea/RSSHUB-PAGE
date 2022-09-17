
---
title: 'EasyGoAdmin 敏捷开发框架 GoFrame+AntdVue 版本 v1.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2127'
author: 开源中国
comments: false
date: Sat, 17 Sep 2022 08:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2127'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">v1.1.0 更新内容：</span><br> <span style="background-color:#ffffff; color:#333333">1、升级文件上传功能，解决上传图片跨域的问题，后端服务器跨域处理中间件 Header 头加入：X-Requested-With；</span><br> <span style="background-color:#ffffff; color:#333333">2、架构优化和升级以及性能优化；</span><br> <span style="background-color:#ffffff; color:#333333">3、修复近期用户反馈的 BUG</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">一款 Go 语言基于 GoFrame、Vue、AntDesign、MySQL 等框架精心打造的一款模块化、插件化、高性能的前后端分离架构敏捷开发框架，可快速搭建前后端分离后台管理系统，本着简化开发、提升开发效率的初衷，框架自研了一套个性化的组件，实现了可插拔的组件式开发方式，同时为了敏捷快速开发，框架特地集成了代码生成器，完全自主研发了自定义 GO 后端服务模板和前端 Vue 自定义模板，可以根据已建好的表结构，可以快速的一键生成整个模块的所有代码和增删改查等等功能业务，真正实现了低代码开发方式，极大的节省了人力成本的同时提高了开发效率，缩短了研发周期，是一款真正意义上实现组件化、可插拔式的敏捷开发框架。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目特点</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>模块化、松耦合</li> 
 <li>模块丰富、开箱即用</li> 
 <li>简洁易用、快速接入</li> 
 <li>文档详尽、易于维护</li> 
 <li>自顶向下、体系化设计</li> 
 <li>统一框架、统一组件、降低选择成本</li> 
 <li>开发规范、设计模式、代码分层模型</li> 
 <li>强大便捷的开发工具链</li> 
 <li>完善的本地中文化支持</li> 
 <li>设计为团队及企业使用</li> 
</ul> 
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
 <li>代码生成：一键生成模块 CRUD 的功能，包括后端 Go 和前端 Vue 等相关代码。</li> 
 <li>案例演示：常规代码生成器一键生成后的演示案例。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">软件信息</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>软件名称：EasyGoAdmin 敏捷开发框架 GoFrame+AntdVue 版本</li> 
 <li>官网网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.easygoadmin.vip" target="_blank">http://www.easygoadmin.vip</a></li> 
 <li>文档网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.goframe.antdvue.easygoadmin.vip" target="_blank">http://docs.goframe.antdvue.easygoadmin.vip</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">系统演示</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.goframe.antdvue.easygoadmin.vip" target="_blank">http://manage.goframe.antdvue.easygoadmin.vip</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">版本说明</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>版本名称</th> 
   <th>版本说明</th> 
   <th>版本地址</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">GoFrame+Layui 混编版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 GoFrame、Layui 等框架研发</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_Layui</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Beego+Layui 混编版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 Beego、Layui 等框架研发</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Beego_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_Beego_Layui</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Gin+Layui 混编版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 Gin、Layui 等框架研发</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Gin_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_Gin_Layui</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Iris+Layui 混编版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 Iris、Layui 等框架研发</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Iris_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_Iris_Layui</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">GoFrame+EleVue 前后端分离版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 GoFrame、Vue、ElementUI 等框架研发前后端分离版本</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_EleVue</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Beego+EleVue 前后端分离版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 Beego、Vue、ElementUI 等框架研发前后端分离版本</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Beego_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_Beego_EleVue</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Gin+EleVue 前后端分离版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 Gin、Vue、ElementUI 等框架研发前后端分离版本</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Gin_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_Gin_EleVue</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Iris+EleVue 前后端分离版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 Iris、Vue、ElementUI 等框架研发前后端分离版本</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Iris_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_Iris_EleVue</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">GoFrame+AntdVue 前后端分离版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 GoFrame、Vue、AntDesign 等框架研发前后端分离版本</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_AntdVue</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Beego+AntdVue 前后端分离版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 Beego、Vue、AntDesign 等框架研发前后端分离版本</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Beego_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_Beego_AntdVue</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Gin+AntdVue 前后端分离版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 Gin、Vue、AntDesign 等框架研发前后端分离版本</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Gin_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_Gin_AntdVue</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Iris+AntdVue 前后端分离版</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">采用 Iris、Vue、AntDesign 等框架研发前后端分离版本</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Iris_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_Iris_AntdVue</a></td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目结构</h2> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span>├── app             <span style="color:#6a737d">// 应用目录</span></span>
<span>│   ├── controller  <span style="color:#6a737d">// 控制器</span></span>
<span>│   ├── dao         <span style="color:#6a737d">// DAO层</span></span>
<span>│   ├── model       <span style="color:#6a737d">// 模型层</span></span>
<span>│   └── service     <span style="color:#6a737d">// 服务层</span></span>
<span>│   └── utils       <span style="color:#6a737d">// 系统工具</span></span>
<span>├── boot</span>
<span>├── config          <span style="color:#6a737d">// 系统配置</span></span>
<span>├── docker</span>
<span>├── <span>document</span>        <span style="color:#6a737d">// 文档目录</span></span>
<span>├── i18n            <span style="color:#6a737d">// 国际化</span></span>
<span>├── library         <span style="color:#6a737d">// 类库</span></span>
<span>├── packed</span>
<span>├── <span style="color:#d73a49">public</span>          <span style="color:#6a737d">// 资源目录</span></span>
<span>├── router          <span style="color:#6a737d">// 路由</span></span>
<span>├── template        <span style="color:#6a737d">// 自定义模板</span></span>
<span>├── Dockerfile</span>
<span>├── go.mod</span>
<span>└── main.go</span></pre> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">特别鸣谢</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">感谢<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2F%23all-updates" target="_blank">GoFrame</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcn.vuejs.org" target="_blank">Vue</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2F2x.antdv.com%2Fdocs%2Fvue%2Fintroduce-cn" target="_blank">AntDesign</a>等优秀开源项目。</p>
                                        </div>
                                      
</div>
            