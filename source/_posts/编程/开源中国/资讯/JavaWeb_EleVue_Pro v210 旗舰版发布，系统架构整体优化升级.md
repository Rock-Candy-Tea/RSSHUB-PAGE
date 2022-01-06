
---
title: 'JavaWeb_EleVue_Pro v2.1.0 旗舰版发布，系统架构整体优化升级'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/javaweb520/JavaWeb_Vue_Pro/raw/master/uploads/demo/1.png'
author: 开源中国
comments: false
date: Thu, 06 Jan 2022 09:14:00 GMT
thumbnail: 'https://gitee.com/javaweb520/JavaWeb_Vue_Pro/raw/master/uploads/demo/1.png'
---

<div>   
<div class="content">
                                                                                            <p>v2.1.0 更新内容：<br> 1、前端UI架构全新升级，整体框架了做了重构和优化；<br> 2、模块Vue文件做列表页和编辑表单也分层设计，增强可维护性降低维护成本；<br> 3、优化用户管理模块，列表新增部门名称列；<br> 4、优化升级字典管理模块和配置管理模块；<br> 5、优化升级登录日志和操作日志；<br> 6、友链管理模块新增使用平台和友链类型筛选条件，表结构新增备注note字段；<br> 7、增强菜单管理模块，新增是否隐藏菜单hide字段;<br> 8、重构个人中心页面，去掉之前Base64头像上传方式，统一采用自研上传图片组件，服务器直接处理图片链接即可；<br> 9、站点模块列表㛑新增站点名称展示列itemName字段，后端服务新增ItemCateListVo文件；<br> 10、优化会员管理模块，新增性别查询条件；<br> 11、重构代码生成器，重写自定义生成器模板；<br> 12、解决代码生成器读取数据表字段重复的问题；<br> 13、重构菜单管理模块，调整菜单节点创建业务逻辑，采用全部删除重新创建的方式；<br> 14、新增CMS管理模块，包括单图上传和多图上传；<br> 15、职级管理新增导入Excel、导出Excel的功能；<br> 16、系统核心模块新增Excel操作类ExcelUtil文件；<br> 17、新增API模块，涉及到客户端(包括微信、小程序)等等功能都可以放入API模块中；<br> 18、核心模块新增JWT工具类和ZipUtils压缩文件工具类；<br> 19、基类文件做了调整，统一放入common核心模块中；<br> 20、优化系统架构，完善一些细节问题；</p> 
<p> </p> 
<h2>📚 项目介绍</h2> 
<p>一款 Java 语言基于 SpringBoot2.x、MybatisPlus、Vue、ElementUI、MySQL等框架精心打造的一款前后端分离框架，致力于实现模块化、组件化、可插拔的前后端分离架构敏捷开发框架，可用于快速搭建前后端分离后台管理系统，本着简化开发、提升开发效率的初衷，目前框架已集成了完整的RBAC权限架构和常规基础模块，前端Vue端支持多主题切换，可以根据自己喜欢的风格选择想一个的主题，实现了个性化呈现的需求；</p> 
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
 <li>系统名称：JavaWeb_Vue_Pro前后端分离框架旗舰版</li> 
 <li>软件作者：@鲲鹏</li> 
 <li>软件出处：上海JavaWeb研发中心</li> 
 <li>官网网址：<a href="https://gitee.com/link?target=http%3A%2F%2Fwww.javaweb.vip">http://www.javaweb.vip</a></li> 
 <li>文档网址：<a href="https://gitee.com/link?target=http%3A%2F%2Fdocs.vue.pro.javaweb.vip">http://docs.vue.pro.javaweb.vip</a></li> 
 <li>开源协议：LGPL-3.0</li> 
</ul> 
<h2>🎨 系统演示</h2> 
<p>演示地址：<a href="https://gitee.com/link?target=http%3A%2F%2Fmanage.vue.pro.javaweb.vip">http://manage.vue.pro.javaweb.vip</a></p> 
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
<h2>🔧 模块展示</h2> 
<p><img alt="效果图1" src="https://gitee.com/javaweb520/JavaWeb_Vue_Pro/raw/master/uploads/demo/1.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图3" src="https://gitee.com/javaweb520/JavaWeb_Vue_Pro/raw/master/uploads/demo/3.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图4" src="https://gitee.com/javaweb520/JavaWeb_Vue_Pro/raw/master/uploads/demo/4.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图5" src="https://gitee.com/javaweb520/JavaWeb_Vue_Pro/raw/master/uploads/demo/5.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图5" src="https://gitee.com/javaweb520/JavaWeb_Vue_Pro/raw/master/uploads/demo/6.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图20" src="https://gitee.com/javaweb520/JavaWeb_Vue_Pro/raw/master/uploads/demo/20.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图21" src="https://gitee.com/javaweb520/JavaWeb_Vue_Pro/raw/master/uploads/demo/21.png" referrerpolicy="no-referrer"></p> 
<p><img alt="效果图22" src="https://gitee.com/javaweb520/JavaWeb_Vue_Pro/raw/master/uploads/demo/22.png" referrerpolicy="no-referrer"></p> 
<h2>🍻 贡献者名单</h2> 
<p>@鲲鹏</p> 
<h2>🍻 安全&缺陷</h2> 
<p>如果你发现了一个安全漏洞或缺陷，请发送邮件到 <a href="https://www.oschina.net/action/GoToLink?url=mailto%3Ajavaweb520%40gmail.com" target="_blank">javaweb520@gmail.com</a>,所有的安全漏洞都将及时得到解决。</p> 
<h2>✨ 特别鸣谢</h2> 
<p>感谢<a href="https://gitee.com/link?target=https%3A%2F%2Fmp.baomidou.com%2F">MybatisPlus</a>、<a href="https://gitee.com/link?target=https%3A%2F%2Fcn.vuejs.org%2F">VueJs</a>、<a href="https://gitee.com/link?target=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN">ElementUI</a>等优秀开源项目。</p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            