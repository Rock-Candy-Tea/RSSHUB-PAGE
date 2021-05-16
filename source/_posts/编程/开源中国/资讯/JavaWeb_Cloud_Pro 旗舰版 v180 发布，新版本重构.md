
---
title: 'JavaWeb_Cloud_Pro 旗舰版 v1.8.0 发布，新版本重构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ea1aa0d5e7e71ec39f2cfa7a59872c2f9cd.png'
author: 开源中国
comments: false
date: Sat, 15 May 2021 17:16:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ea1aa0d5e7e71ec39f2cfa7a59872c2f9cd.png'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <div> 
  <div> 
   <div> 
    <p>v1.8.0更新内容：<br> 1、完善用户管理模块，新增省市区、详细地址、部门选择、用户昵称等等基础字段维护；<br> 2、系统用户表sys_user字段做了调整，province_id调整为province_code，city_id调整为city_code，district_id调整为district_code；<br> 3、会员表ums_member字段做了调整，province_id调整为province_code，city_id调整为city_code，district_id调整为district_code，新增详细地址字段address;<br> 4、会员管理模块做了完善，新增详细地址输入框，解决前期城市选择和日期无法存储和展示的问题；<br> 5、修复菜单管理模块添加菜单是上级菜单无法选择的问题；<br> 6、新增多环境配置文件application-local.yml，目前整体框架分四种环境，分别是：本地环境(local)、开发环境(dev)、测试环境(test)、线上环境(prod)<br> 7、前端部分扩展多环境部署支持，目前新增三种环境变量，开发环境.env.development，测试环境.env.test，线上环境.env.production，可以配套jenkins自动化部署工具做多环境自动化发布；<br> 8、解决字典管理模块右侧内容区页面加载时无法加载的问题；字典管理模块表做了优化，sys_dict表改成sys_dict_data表，原sys_dict_type表改成sys_dict表；同时相关前端和后端代码已全部同步更新；<br> 9、解决配置管理模块右侧内容区页面加载时无法加载的问题；配置管理模块表做了优化，sys_config表改成sys_config_data表，原sys_config_group表改成sys_config表；同时相关前端和后端代码已全部同步更新；<br> 10、升级代码生成器，同步一键生成前端Vue文件及菜单的功能；<br> 11、配置本地图片虚拟域名指向uploads目录，可以正常的显示图片和上传存储图片；</p> 
    <h3>项目介绍</h3> 
    <p>JavaWeb_Cloud_Pro 是基于 SpringCloud+Vue+ElementUI+MybatisPlus 研发的权限(RBAC)及内容管理系统，致力于做更简洁的后台管理框架，包含系统管理、代码生成、权限管理、站点、广告、布局、字段、配置等一系列常用的模块，整套系统一键生成所有模块（包括前端UI），一键实现CRUD，简化了传统手动抒写重复性代码的工作。 同时，框架提供长大量常规组件，如上传单图、上传多图、上传文件、下拉选择、复选框按钮、单选按钮，城市选择、富文本编辑器、权限颗粒度控制等高频使用的组件，代码简介，使用方便，节省了大量重复性的劳动，降低了开发成本，提高了整体开发效率，整体开发效率提交80%以上，框架专注于为中小企业提供最佳的行业基础后台框架解决方案，执行效率、扩展性、稳定性值得信赖，操作体验流畅，欢迎大家使用及进行二次开发。</p> 
    <ul> 
     <li>台、物流管理系统、快递管理系统、教务管理系统等各类管理软件。</li> 
    </ul> 
    <h3>功能特性</h3> 
    <ul> 
     <li><strong>严谨规范：</strong> 提供一套有利于团队协作的结构设计、编码、数据等规范。</li> 
     <li><strong>高效灵活：</strong> 清晰的分层设计、钩子行为扩展机制，解耦设计更能灵活应对需求变更。</li> 
     <li><strong>严谨安全：</strong> 清晰的系统执行流程，严谨的异常检测和安全机制，详细的日志统计，为系统保驾护航。</li> 
     <li><strong>组件化：</strong> 完善的组件化设计，丰富的表单组件，让开发列表和表单更得心应手。无需前端开发，省时省力。</li> 
     <li><strong>简单上手快：</strong> 结构清晰、代码规范、在开发快速的同时还兼顾性能的极致追求。</li> 
     <li><strong>自身特色：</strong> 权限管理、组件丰富、第三方应用多、分层解耦化设计和先进的设计思想。</li> 
    </ul> 
    <h2>后台演示（用户名:admin 密码:123456）</h2> 
    <ul> 
     <li>演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.cloud.pro.javaweb.vip" target="_blank">http://manage.cloud.pro.javaweb.vip</a></li> 
     <li>登录账号：admin</li> 
     <li>登录密码：123456</li> 
     <li>验证码：520</li> 
    </ul> 
    <p><strong>效果图</strong></p> 
    <p><img height="911" src="https://oscimg.oschina.net/oscnet/up-ea1aa0d5e7e71ec39f2cfa7a59872c2f9cd.png" width="1920" referrerpolicy="no-referrer"></p> 
    <p> </p> 
    <p><img height="910" src="https://oscimg.oschina.net/oscnet/up-b851638bb5e7e0614eda85ddd79836ea9ae.png" width="1919" referrerpolicy="no-referrer"><br>  </p> 
    <p><img height="905" src="https://oscimg.oschina.net/oscnet/up-6b5af525f84ffbca4a0408d381d5c44938a.png" width="1918" referrerpolicy="no-referrer"></p> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            