
---
title: 'JavaWeb_Cloud_AntdVue_Pro 旗舰版 v2.0.0 发布，年度新版本重构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-443b4961ae3b9d30f84d19a32799a5e74a2.png'
author: 开源中国
comments: false
date: Fri, 11 Feb 2022 09:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-443b4961ae3b9d30f84d19a32799a5e74a2.png'
---

<div>   
<div class="content">
                                                                                            <p>v2.0.0 更新内容：<br> 1、前端UI架构全新升级，整体框架了做了重构和优化；<br> 2、模块Vue文件做列表页和编辑表单也分层设计，增强可维护性降低维护成本；<br> 3、优化用户管理模块，列表新增部门名称列；<br> 4、优化升级字典管理模块和配置管理模块；<br> 5、优化升级登录日志和操作日志；<br> 6、友链管理模块新增使用平台和友链类型筛选条件，表结构新增备注note字段；<br> 7、增强菜单管理模块，新增是否隐藏菜单hide字段;<br> 8、重构个人中心页面，去掉之前Base64头像上传方式，统一采用自研上传图片组件，服务器直接处理图片链接即可；<br> 9、站点模块列表㛑新增站点名称展示列itemName字段，后端服务新增ItemCateListVo文件；<br> 10、优化会员管理模块，新增性别查询条件；<br> 11、重构代码生成器，重写自定义生成器模板；<br> 12、解决代码生成器读取数据表字段重复的问题；<br> 13、重构菜单管理模块，调整菜单节点创建业务逻辑，采用全部删除重新创建的方式；<br> 14、新增CMS管理模块，包括单图上传和多图上传；<br> 15、职级管理新增导入Excel、导出Excel的功能；<br> 16、系统核心模块新增Excel操作类ExcelUtil文件；<br> 17、新增API模块，涉及到客户端(包括微信、小程序)等等功能都可以放入API模块中；<br> 18、核心模块新增JWT工具类和ZipUtils压缩文件工具类；<br> 19、基类文件做了调整，统一放入common核心模块中；<br> 20、优化系统架构，完善一些细节问题；<br> 21、紧急修复Log4j远程漏洞，目前已升级最新版本v2.17.1;<br> 22、修复近期客户反馈的BUG，优化和升级用户操作体验；<br> 23、升级配置管理功能，单图和多图可以在列表和编辑表单中直接显示图片，便于预览，提高使用体验；<br> 24、前端系统用户管理和会员管理表单编辑页新增城市省市区验证；城市选择做了优化升级，提供了可用性；<br> 25、升级优化配置管理模块，列表可以直接显示图片信息；</p> 
<h2>📚 项目介绍</h2> 
<p>一款 Java 语言基于 SpringCloud、Vue、AntDesign、MySQL等框架精心打造的一款前后端分离框架，致力于实现模块化、组件化、可插拔的前后端分离架构敏捷开发框架，可用于快速搭建前后端分离后台管理系统，本着简化开发、提升开发效率的初衷，目前框架已集成了完整的RBAC权限架构和常规基础模块，前端Vue端支持多主题切换，可以根据自己喜欢的风格选择想一个的主题，实现了个性化呈现的需求；</p> 
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
 <li>系统名称：JavaWeb_Cloud_AntdVue_Pro前后端分离框架旗舰版</li> 
 <li>软件作者：@鲲鹏</li> 
 <li>软件出处：上海JavaWeb研发中心</li> 
 <li>软件咨询：<a href="https://gitee.com/link?target=http%3A%2F%2Fwpa.qq.com%2Fmsgrd%3Fv%3D3%26uin%3D1451478873%26site%3Dqq%26menu%3Dyes">1451478873</a></li> 
 <li>官网网址：<a href="https://gitee.com/link?target=https%3A%2F%2Fwww.javaweb.vip">https://www.javaweb.vip</a></li> 
 <li>文档网址：<a href="https://gitee.com/link?target=http%3A%2F%2Fdocs.cloud.ant.javaweb.vip">http://docs.cloud.ant.javaweb.vip</a></li> 
 <li>开源协议：LGPL-3.0</li> 
</ul> 
<h2>🎨 系统演示</h2> 
<p>演示地址：<a href="https://gitee.com/link?target=http%3A%2F%2Fmanage.cloud.ant.javaweb.vip">http://manage.cloud.ant.javaweb.vip</a></p> 
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
<p><img height="768" src="https://oscimg.oschina.net/oscnet/up-443b4961ae3b9d30f84d19a32799a5e74a2.png" width="1366" referrerpolicy="no-referrer"></p> 
<p><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-7666b4ed9f51c588a5e9dcabbdcbf9db77b.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-52c0f234e8b0970ded9f332130cc4a3f22a.png" referrerpolicy="no-referrer"><img alt height="1080" src="https://oscimg.oschina.net/oscnet/up-25187285c08e11526c406c6d814a1f68361.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            