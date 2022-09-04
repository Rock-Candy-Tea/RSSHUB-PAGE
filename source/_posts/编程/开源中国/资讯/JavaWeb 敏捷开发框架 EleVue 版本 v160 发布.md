
---
title: 'JavaWeb 敏捷开发框架 EleVue 版本 v1.6.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=281'
author: 开源中国
comments: false
date: Sun, 04 Sep 2022 08:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=281'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <div> 
   <div> 
    <p>v1.6.0更新内容：<br> 1、后端新增权限节点颗粒度控制，集成Shiro,使用方法：@RequiresPermissions("sys:city:edit")<br> 2、前端Vue端新增按钮权限节点控制，没有节点权限则按钮不显示，使用方式如：v-if="permission.includes('sys:level:delete')"<br> 3、新增配合Jenkins多环境发布的功能与POM配置；<br> 4、新增ExcelUtils导出工具类，并在职级管理模块写了导出Excel数据案例；<br> 5、职级管理、岗位管理、登录日志集成导出Excel功能；<br> 6、完善个人中心头像上传功能，完善Base64Utils转换工具类；<br> 7、重新设计登录界面背景图片；<br> 8、解决切换账号之前打开的Tab页依然存在的问题；</p> 
    <h2>项目介绍</h2> 
    <p>一款 Java 语言基于 SpringBoot2.x、MybatisPlus、Vue、ElementUI、MySQL 等框架精心打造的一款前后端分离框架，致力于实现模块化、组件化、可插拔的前后端分离架构敏捷开发框架，可用于快速搭建前后端分离后台管理系统，本着简化开发、提升开发效率的初衷，目前框架已集成了完整的 RBAC 权限架构和常规基础模块，前端 Vue 端支持多主题切换，可以根据自己喜欢的风格选择想一个的主题，实现了个性化呈现的需求；</p> 
    <p>为了敏捷快速开发，提升研发效率，框架内置了一键 CRUD 代码生成器，自定义了模块生成模板，可以根据已建好的表结构 (字段注释需规范) 快速的一键生成整个模块的所有代码和增删改查等等功能业务，真正实现了低代码开发，极大的节省了人力成本的同时提高了开发效率，缩短了研发周期，是一款真正意义上实现组件化、低代码敏捷开发框架。</p> 
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
     <li>代码生成：一键生成模块 CRUD 的功能，包括后端和前端 Vue 等相关代码。</li> 
     <li>案例演示：常规代码生成器一键生成后的演示案例。</li> 
    </ul> 
    <h2>开发者信息</h2> 
    <ul> 
     <li>软件名称：JavaWeb 敏捷开发框架 EleVue 版本</li> 
     <li>官网网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.javaweb.vip" target="_blank">http://www.javaweb.vip</a></li> 
     <li>文档网址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.vue.pro.javaweb.vip" target="_blank">http://docs.vue.pro.javaweb.vip</a></li> 
    </ul> 
    <h2>系统演示</h2> 
    <p>演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.vue.pro.javaweb.vip" target="_blank">http://manage.vue.pro.javaweb.vip</a></p> 
    <h2>版本说明</h2> 
    <table> 
     <thead> 
      <tr> 
       <th>版本名称</th> 
       <th>说明</th> 
       <th>地址</th> 
      </tr> 
     </thead> 
     <tbody> 
      <tr> 
       <td>JavaWeb 混编专业版</td> 
       <td>采用 SpringBoot2+Thymeleaf+layui</td> 
       <td><a href="https://gitee.com/javaweb520/JavaWeb">https://gitee.com/javaweb520/JavaWeb</a></td> 
      </tr> 
      <tr> 
       <td>JavaWeb_Pro 混编旗舰版</td> 
       <td>采用 SpringBoot2+Thymeleaf+layui</td> 
       <td><a href="https://gitee.com/javaweb520/JavaWeb_Pro">https://gitee.com/javaweb520/JavaWeb_Pro</a></td> 
      </tr> 
      <tr> 
       <td>JavaWeb_Vue 专业版</td> 
       <td>前后端分离版，采用 SpringBoot2+Vue+ElementUI</td> 
       <td><a href="https://gitee.com/javaweb520/JavaWeb_Vue">https://gitee.com/javaweb520/JavaWeb_Vue</a></td> 
      </tr> 
      <tr> 
       <td>JavaWeb_Vue_Pro 旗舰版</td> 
       <td>采用 SpringBoot2+Vue+ElementUI</td> 
       <td><a href="https://gitee.com/javaweb520/JavaWeb_Vue_Pro">https://gitee.com/javaweb520/JavaWeb_Vue_Pro</a></td> 
      </tr> 
      <tr> 
       <td>JavaWeb_Ant_Pro 旗舰版</td> 
       <td>采用 SpringBoot2+Vue+AntDesign</td> 
       <td><a href="https://gitee.com/javaweb520/JavaWeb_Ant_Pro">https://gitee.com/javaweb520/JavaWeb_Ant_Pro</a></td> 
      </tr> 
      <tr> 
       <td>JavaWeb_Cloud 微服务专业版</td> 
       <td>采用 SpringCloud+Vue+ElementUI</td> 
       <td><a href="https://gitee.com/javaweb520/JavaWeb_Cloud">https://gitee.com/javaweb520/JavaWeb_Cloud</a></td> 
      </tr> 
      <tr> 
       <td>JavaWeb_Cloud_Pro 微服务旗舰版</td> 
       <td>采用 SpringCloud+Vue+ElementUI</td> 
       <td><a href="https://gitee.com/javaweb520/JavaWeb_Cloud_Pro">https://gitee.com/javaweb520/JavaWeb_Cloud_Pro</a></td> 
      </tr> 
      <tr> 
       <td>JavaWeb_Cloud_Ant 微服务旗舰版</td> 
       <td>采用 SpringCloud+Vue+AntDesign</td> 
       <td><a href="https://gitee.com/javaweb520/JavaWeb_Cloud_Ant">https://gitee.com/javaweb520/JavaWeb_Cloud_Ant</a></td> 
      </tr> 
     </tbody> 
    </table> 
    <h2>特别鸣谢</h2> 
    <p>感谢 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.baomidou.com%2F" target="_blank">MybatisPlus</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcn.vuejs.org" target="_blank">Vue</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN" target="_blank">ElementUI</a> 等优秀开源项目。</p> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            