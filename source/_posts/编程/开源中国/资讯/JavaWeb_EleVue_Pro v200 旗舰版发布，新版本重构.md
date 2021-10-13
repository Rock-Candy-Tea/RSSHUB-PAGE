
---
title: 'JavaWeb_EleVue_Pro v2.0.0 旗舰版发布，新版本重构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-28f6f400d7d0e59c9b7b762029de3f6b356.png'
author: 开源中国
comments: false
date: Wed, 13 Oct 2021 09:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-28f6f400d7d0e59c9b7b762029de3f6b356.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>v2.0.0 更新内容：<br> 1、前端UI架构全新升级，整体框架了做了重构和优化；<br> 2、模块Vue文件做列表页和编辑表单也分层设计，增强可维护性降低维护成本；<br> 3、优化用户管理模块，列表新增部门名称列；<br> 4、优化升级字典管理模块和配置管理模块；<br> 5、优化升级登录日志和操作日志；<br> 6、友链管理模块新增使用平台和友链类型筛选条件，表结构新增备注note字段；<br> 7、增强菜单管理模块，新增是否隐藏菜单hide字段;<br> 8、重构个人中心页面，去掉之前Base64头像上传方式，统一采用自研上传图片组件，服务器直接处理图片链接即可；<br> 9、站点模块列表㛑新增站点名称展示列itemName字段，后端服务新增ItemCateListVo文件；<br> 10、优化会员管理模块，新增性别查询条件；<br> 11、重构代码生成器，重写自定义生成器模板；<br> 12、解决代码生成器读取数据表字段重复的问题；<br> 13、重构菜单管理模块，调整菜单节点创建业务逻辑，采用全部删除重新创建的方式；<br> 14、新增CMS管理模块，包括单图上传和多图上传；<br> 15、职级管理新增导入Excel、导出Excel的功能；<br> 16、系统核心模块新增Excel操作类ExcelUtil文件；<br> 17、新增API模块，涉及到客户端(包括微信、小程序)等等功能都可以放入API模块中；<br> 18、核心模块新增JWT工具类和ZipUtils压缩文件工具类；<br> 19、基类文件做了调整，统一放入common核心模块中；</p> 
<h3>项目介绍</h3> 
<p>JavaWeb_Vue_Pro 是基于 SpringBoot2+Vue+ElementUI+Shiro+MybatisPlus 研发的权限(RBAC)及内容管理系统，致力于做更简洁的后台管理框架，包含系统管理、代码生成、权限管理、站点、广告、布局、字段、配置等一系列常用的模块，整套系统一键生成所有模块（包括前端UI），一键实现CRUD，简化了传统手动抒写重复性代码的工作。 同时，框架提供长大量常规组件，如上传单图、上传多图、上传文件、下拉选择、复选框按钮、单选按钮，城市选择、富文本编辑器、权限颗粒度控制等高频使用的组件，代码简介，使用方便，节省了大量重复性的劳动，降低了开发成本，提高了整体开发效率，整体开发效率提交80%以上，JavaWeb框架专注于为中小企业提供最佳的行业基础后台框架解决方案，执行效率、扩展性、稳定性值得信赖，操作体验流畅，使用非常优化，欢迎大家使用及进行二次开发。</p> 
<h2>后台演示（用户名:admin 密码:123456）</h2> 
<ul> 
 <li>演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.vue.pro.javaweb.vip" target="_blank">http://manage.vue.pro.javaweb.vip</a></li> 
 <li>登录账号：admin</li> 
 <li>登录密码：123456</li> 
 <li>验证码：520</li> 
</ul> 
<h2>效果图展示</h2> 
<p><img height="768" src="https://oscimg.oschina.net/oscnet/up-28f6f400d7d0e59c9b7b762029de3f6b356.png" width="1366" referrerpolicy="no-referrer"></p> 
<p><img height="768" src="https://oscimg.oschina.net/oscnet/up-ef21723c30bbae07914b6c13fa71ad70076.png" width="1366" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            