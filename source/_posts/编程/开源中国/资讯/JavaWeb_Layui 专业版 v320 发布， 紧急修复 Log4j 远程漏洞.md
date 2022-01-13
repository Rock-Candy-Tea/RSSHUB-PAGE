
---
title: 'JavaWeb_Layui 专业版 v3.2.0 发布， 紧急修复 Log4j 远程漏洞'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-eaf447c46aaa335666ccd1e5253e77b7b70.png'
author: 开源中国
comments: false
date: Thu, 13 Jan 2022 11:08:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-eaf447c46aaa335666ccd1e5253e77b7b70.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <p>v3.2.0 更新如下：<br> 1、紧急修复Log4j远程漏洞，目前已升级最新版本v2.17.1;<br> 2、修复近期客户反馈的BUG；<br> 3、优化和升级用户操作体验；</p> 
  <h2>📚 项目介绍</h2> 
  <p>一款 Java 语言基于 SpringBoot2.x、Layui、Thymeleaf、MybatisPlus、Shiro、MySQL等框架精心打造的一款模块化、插件化、高性能的前后端分离架构敏捷开发框架，可用于快速搭建后台管理系统，本着简化开发、提升开发效率的初衷，框架自研了一套个性化的组件，实现了可插拔的组件式开发方式：单图上传、多图上传、下拉选择、开关按钮、单选按钮、多选按钮、图片裁剪、富文本编辑器等等一系列个性化、轻量级的组件，是一款真正意义上实现组件化开发的敏捷开发框架，框架已集成了完整的RBAC权限架构和常规基础模块，同时支持多主题切换，可以根据自己喜欢的风格选择想一个的主题，实现了个性化呈现的需求；</p> 
  <p>为了敏捷快速开发，提升研发效率，框架内置了一键CRUD代码生成器，自定义了模块生成模板，可以根据已建好的表结构(字段注释需规范)快速的一键生成整个模块的所有代码和增删改查等等功能业务，真正实现了低代码开发，极大的节省了人力成本的同时提高了开发效率，缩短了研发周期，是一款真正意义上实现组件化、低代码敏捷开发框架。</p> 
  <h2>🍪 内置模块</h2> 
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
   <li>代码生成：一键生成模块CRUD的功能，包括后端和前端Vue等相关代码。</li> 
   <li>案例演示：常规代码生成器一键生成后的演示案例。</li> 
  </ul> 
  <h2>👷 开发者信息</h2> 
  <ul> 
   <li>系统名称：JavaWeb混编专业版</li> 
   <li>软件作者：@鲲鹏</li> 
   <li>软件出处：上海JavaWeb研发中心</li> 
   <li>官网网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.javaweb.vip" target="_blank">http://www.javaweb.vip</a></li> 
   <li>文档网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.javaweb.vip" target="_blank">http://docs.javaweb.vip</a></li> 
   <li>开源协议：LGPL-3.0</li> 
  </ul> 
  <h2>🎨 系统演示</h2> 
  <p>演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.javaweb.vip" target="_blank">http://manage.javaweb.vip</a></p> 
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
  <p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-eaf447c46aaa335666ccd1e5253e77b7b70.png" width="1920" referrerpolicy="no-referrer"></p> 
  <p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-2aa68261412090adf56db020d42e51a1f4b.png" width="1920" referrerpolicy="no-referrer"></p> 
  <p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-b92c740bc63c7e7b438ca9e6603a170fbfe.png" width="1920" referrerpolicy="no-referrer"></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            