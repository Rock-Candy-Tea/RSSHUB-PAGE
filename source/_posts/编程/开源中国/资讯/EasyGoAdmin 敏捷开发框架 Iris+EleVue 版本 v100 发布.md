
---
title: 'EasyGoAdmin 敏捷开发框架 Iris+EleVue 版本 v1.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-623fa3ecb11068d3e03c57c967269e287b3.png'
author: 开源中国
comments: false
date: Fri, 13 May 2022 09:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-623fa3ecb11068d3e03c57c967269e287b3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>v1.0.0 更新内容：<br> 1、设计、规划和研发基础RBAC权限架构；<br> 2、对系统模板进行架构设计及模板继承相关设计；<br> 3、研发框架基础模块，如字典、配置、行政区划管理等等常规基础模块；<br> 4、设计并研发代码生成器，根据表结构动态解析并生成模块文件和增删改查功能；<br> 5、设计并研发一系列其他配套功能很常规使用函数；</p> 
<h2>项目介绍</h2> 
<p>一款 Go 语言基于Iris、Vue、ElementUI、MySQL等框架精心打造的一款模块化、插件化、高性能的前后端分离架构敏捷开发框架，可快速搭建前后端分离后台管理系统，本着简化开发、提升开发效率的初衷，框架自研了一套个性化的组件，实现了可插拔的组件式开发方式，同时为了敏捷快速开发，框架特地集成了代码生成器，完全自主研发了自定义GO后端服务模板和前端Vue自定义模板，可以根据已建好的表结构，可以快速的一键生成整个模块的所有代码和增删改查等等功能业务，真正实现了低代码开发方式，极大的节省了人力成本的同时提高了开发效率，缩短了研发周期，是一款真正意义上实现组件化、可插拔式的敏捷开发框架。</p> 
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
 <li>职级管理：主要管理用户的职级。</li> 
 <li>岗位管理：主要管理用户担任职务。</li> 
 <li>部门管理：配置系统组织机构（公司、部门、小组），树结构展现支持数据权限。</li> 
 <li>字典管理：对系统中常用的较为固定的数据进行统一维护。</li> 
 <li>配置管理：对系统的常规配置信息进行维护，网站配置管理功能进行统一维护。</li> 
 <li>通知公告：系统通知公告信息发布维护。</li> 
 <li>操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。</li> 
 <li>登录日志：系统登录日志记录查询包含登录异常。</li> 
 <li>代码生成：一键生成模块CRUD的功能，包括后端Go和前端HTML、JS等相关代码。</li> 
 <li>案例演示：常规代码生成器一键生成后的演示案例。</li> 
</ul> 
<h2>软件信息</h2> 
<ul> 
 <li>软件名称：EasyGoAdmin敏捷开发框架Iris+EleVue版本</li> 
 <li>软件作者：@半城风雨 团队荣誉出品</li> 
 <li>软件出处：深圳EasyGoAdmin研发中心</li> 
 <li>软件协议：LGPL-3.0</li> 
 <li>官网网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.easygoadmin.vip" target="_blank">官网地址</a></li> 
 <li>文档网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.iris.elevue.easygoadmin.vip" target="_blank">文档地址</a></li> 
</ul> 
<h2>系统演示</h2> 
<ul> 
 <li>演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.iris.elevue.easygoadmin.vip" target="_blank">点击查看演示地址</a></li> 
</ul> 
<table> 
 <thead> 
  <tr> 
   <th>账号</th> 
   <th>密码</th> 
   <th>操作权限</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>admin</td> 
   <td>123456</td> 
   <td>演示环境无法进行修改删除操作</td> 
  </tr> 
 </tbody> 
</table> 
<h2>版本说明</h2> 
<table> 
 <thead> 
  <tr> 
   <th>版本名称</th> 
   <th>版本说明</th> 
   <th>版本地址</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>GoFrame+Layui混编版</td> 
   <td>采用GoFrame、Layui等框架研发</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_Layui</a></td> 
  </tr> 
  <tr> 
   <td>Beego+Layui混编版</td> 
   <td>采用Beego、Layui等框架研发</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Beego_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_Beego_Layui</a></td> 
  </tr> 
  <tr> 
   <td>Gin+Layui混编版</td> 
   <td>采用Gin、Layui等框架研发</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Gin_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_Gin_Layui</a></td> 
  </tr> 
  <tr> 
   <td>Iris+Layui混编版</td> 
   <td>采用Iris、Layui等框架研发</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Iris_Layui">https://gitee.com/easygoadmin/EasyGoAdmin_Iris_Layui</a></td> 
  </tr> 
  <tr> 
   <td>GoFrame+EleVue前后端分离版</td> 
   <td>采用GoFrame、Vue、ElementUI等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_EleVue</a></td> 
  </tr> 
  <tr> 
   <td>Beego+EleVue前后端分离版</td> 
   <td>采用Beego、Vue、ElementUI等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Beego_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_Beego_EleVue</a></td> 
  </tr> 
  <tr> 
   <td>Gin+EleVue前后端分离版</td> 
   <td>采用Gin、Vue、ElementUI等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Gin_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_Gin_EleVue</a></td> 
  </tr> 
  <tr> 
   <td>Iris+EleVue前后端分离版</td> 
   <td>采用Iris、Vue、ElementUI等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Iris_EleVue">https://gitee.com/easygoadmin/EasyGoAdmin_Iris_EleVue</a></td> 
  </tr> 
  <tr> 
   <td>GoFrame+AntdVue前后端分离版</td> 
   <td>采用GoFrame、Vue、AntDesign等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_GoFrame_AntdVue</a></td> 
  </tr> 
  <tr> 
   <td>Beego+AntdVue前后端分离版</td> 
   <td>采用Beego、Vue、AntDesign等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Beego_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_Beego_AntdVue</a></td> 
  </tr> 
  <tr> 
   <td>Gin+AntdVue前后端分离版</td> 
   <td>采用Gin、Vue、AntDesign等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Gin_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_Gin_AntdVue</a></td> 
  </tr> 
  <tr> 
   <td>Iris+AntdVue前后端分离版</td> 
   <td>采用Iris、Vue、AntDesign等框架研发前后端分离版本</td> 
   <td><a href="https://gitee.com/easygoadmin/EasyGoAdmin_Iris_AntdVue">https://gitee.com/easygoadmin/EasyGoAdmin_Iris_AntdVue</a></td> 
  </tr> 
 </tbody> 
</table> 
<h2>项目结构</h2> 
<div> 
 <div> 
  <pre><span>easygoadmin</span>
<span>|-- conf</span>
<span>|   `-- app.conf</span>
<span>|-- controllers</span>
<span>|   `-- default.go</span>
<span>|-- main.go</span>
<span>|-- models</span>
<span>|-- routers</span>
<span>|   `-- router.go</span>
<span>|-- static</span>
<span>|   |-- css</span>
<span>|   |-- img</span>
<span>|   `-- js</span>
<span>|-- tests</span>
<span>|   `-- default_test.go</span>
<span>`-- views</span>
<span>    `-- index.tpl</span></pre> 
 </div> 
</div> 
<h2>模块展示</h2> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-623fa3ecb11068d3e03c57c967269e287b3.png" width="1920" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            