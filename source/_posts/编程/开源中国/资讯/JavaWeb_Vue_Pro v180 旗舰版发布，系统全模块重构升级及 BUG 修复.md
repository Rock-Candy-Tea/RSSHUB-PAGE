
---
title: 'JavaWeb_Vue_Pro v1.8.0 旗舰版发布，系统全模块重构升级及 BUG 修复'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-820c31dd6a23f9ac9057a4feaad237f6aab.png'
author: 开源中国
comments: false
date: Sat, 08 May 2021 16:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-820c31dd6a23f9ac9057a4feaad237f6aab.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>v1.8.0更新内容：<br> 1、完善用户管理模块，新增省市区、详细地址、部门选择、用户昵称等等基础字段维护；<br> 2、系统用户表sys_user字段做了调整，province_id调整为province_code，city_id调整为city_code，district_id调整为district_code；<br> 3、会员表ums_member字段做了调整，province_id调整为province_code，city_id调整为city_code，district_id调整为district_code，新增详细地址字段address;<br> 4、会员管理模块做了完善，新增详细地址输入框，解决前期城市选择和日期无法存储和展示的问题；<br> 5、修复菜单管理模块添加菜单是上级菜单无法选择的问题；<br> 6、新增多环境配置文件application-local.yml，目前整体框架分四种环境，分别是：本地环境(local)、开发环境(dev)、测试环境(test)、线上环境(prod)<br> 7、前端部分扩展多环境部署支持，目前新增三种环境变量，开发环境.env.development，测试环境.env.test，线上环境.env.production，可以配套jenkins自动化部署工具做多环境自动化发布；<br> 8、解决字典管理模块右侧内容区页面加载时无法加载的问题；字典管理模块表做了优化，sys_dict表改成sys_dict_data表，原sys_dict_type表改成sys_dict表；同时相关前端和后端代码已全部同步更新；<br> 9、解决配置管理模块右侧内容区页面加载时无法加载的问题；配置管理模块表做了优化，sys_config表改成sys_config_data表，原sys_config_group表改成sys_config表；同时相关前端和后端代码已全部同步更新；</p> 
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
<p><img height="726" src="https://oscimg.oschina.net/oscnet/up-820c31dd6a23f9ac9057a4feaad237f6aab.png" width="1362" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><img height="910" src="https://oscimg.oschina.net/oscnet/up-b5700358507e49e55450910abb68f3234b0.png" width="1920" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><img height="910" src="https://oscimg.oschina.net/oscnet/up-b4b1f6fc487221953d35eb87a4235737e02.png" width="1918" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><img height="909" src="https://oscimg.oschina.net/oscnet/up-176471b3a6b8a51a733cf9497ab7eaa4ee5.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            