
---
title: 'EasyGoAdmin_Gin_EleVue 版 v1.2.0，新增自定义模板和功能实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-57a34c69bb51f413200e4e906eb834fb7c6.png'
author: 开源中国
comments: false
date: Thu, 17 Mar 2022 08:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-57a34c69bb51f413200e4e906eb834fb7c6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>v1.2.0 更新内容：<br> 1、升级代码生成器，生成模块时自动创建菜单和权限节点；<br> 2、性能优化和底层架构调优；</p> 
<h2>项目介绍</h2> 
<p>一款 Go 语言基于Gin、Xorm、Vue、ElementUI、MySQL等框架精心打造的一款模块化、插件化、高性能的前后端分离架构敏捷开发框架，可快速搭建前后端分离后台管理系统，本着简化开发、提升开发效率的初衷，框架自研了一套个性化的组件，实现了可插拔的组件式开发方式，同时为了敏捷快速开发，框架特地集成了代码生成器，完全自主研发了自定义GO后端服务模板和前端Vue自定义模板，可以根据已建好的表结构，可以快速的一键生成整个模块的所有代码和增删改查等等功能业务，真正实现了低代码开发方式，极大的节省了人力成本的同时提高了开发效率，缩短了研发周期，是一款真正意义上实现组件化、可插拔式的敏捷开发框架。</p> 
<h2>项目特点</h2> 
<ul> 
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
<h2>内置模块</h2> 
<ul> 
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
 <li>代码生成：一键生成模块CRUD的功能，包括后端Go和前端Vue等相关代码。</li> 
 <li>案例演示：常规代码生成器一键生成后的演示案例。</li> 
</ul> 
<h2>开发者信息</h2> 
<ul> 
 <li>系统名称：EasyGoAdmin敏捷开发框架Gin+EleVue版本</li> 
 <li>软件作者：@半城风雨</li> 
 <li>官网网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.easygoadmin.vip" target="_blank">官网地址</a></li> 
 <li>文档网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.gin.ele.easygoadmin.vip%2F" target="_blank">文档地址</a></li> 
</ul> 
<h2>系统演示</h2> 
<table> 
 <thead> 
  <tr> 
   <th>演示地址</th> 
   <th>账号</th> 
   <th>密码</th> 
   <th>操作权限</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.gin.elevue.easygoadmin.vip" target="_blank">点击查看演示地址</a></td> 
   <td>admin</td> 
   <td>123456</td> 
   <td>演示环境无法进行修改删除操作</td> 
  </tr> 
 </tbody> 
</table> 
<h2>项目结构</h2> 
<div> 
 <div> 
  <pre><span>├── app             <span><span>// 应用目录</span></span></span>
<span>│   ├── controller  <span><span>// 控制器</span></span></span>
<span>│   ├── dto         <span><span>// DTO层</span></span></span>
<span>│   ├── middleware  <span><span>// 中间件层</span></span></span>
<span>│   ├── model       <span><span>// 模型层</span></span></span>
<span>│   └── service     <span><span>// 服务层</span></span></span>
<span>│   └── vo          <span><span>// VO视图层</span></span></span>
<span>├── boot</span>
<span>├── config          <span><span>// 系统配置</span></span></span>
<span>├── <span><span>document</span></span>        <span><span>// 文档目录</span></span></span>
<span>├── i18n            <span><span>// 国际化</span></span></span>
<span>├── library         <span><span>// 类库</span></span></span>
<span>├── packed</span>
<span>├── <span><span>public</span></span>          <span><span>// 资源目录</span></span></span>
<span>├── router          <span><span>// 路由</span></span></span>
<span>├── templates       <span><span>// 自定义模板</span></span></span>
<span>├── utils           <span><span>// 工具类库</span></span></span>
<span>├── Dockerfile</span>
<span>├── go.mod</span>
<span>└── main.go</span></pre> 
 </div> 
</div> 
<h2>模块展示</h2> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-57a34c69bb51f413200e4e906eb834fb7c6.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-1c0fe8d41016b5ff0e41dfbc6064e682335.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-46d4bcf5ee1f721d0dc6c3787638959f145.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-8cfecc2652b4105d3c94563a9a0a4bae720.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-59c1d755e6de58089ab2cc6129a7bd1fe9e.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-4a0d29aadd5e93d4c0f411718ad9a68308b.png" referrerpolicy="no-referrer"></p> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-cfa5011ad1cd4597225de542a5670215fd3.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-816bba0292c709d2ca283f690bb4da66503.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            