
---
title: 'RuoYi-Vue 3.8.0 发布，支持 Vue3'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/cd1f90be5f2684f4560c9519c0f2a232ee8.jpg'
author: 开源中国
comments: false
date: Wed, 01 Dec 2021 08:38:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/cd1f90be5f2684f4560c9519c0f2a232ee8.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">若依前后端分离版本<span style="background-color:#ffffff; color:#333333"> v3.8.0 已发布，更新日志：</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>新增配套并同步的Vue3前端版本</li> 
 <li>新增通用方法简化模态/缓存/下载/权限/页签使用</li> 
 <li>优化导出数据/使用通用下载方法</li> 
 <li>Excel注解支持自定义数据处理器</li> 
 <li>Excel注解支持导入导出标题信息</li> 
 <li>Excel导入支持@Excels注解</li> 
 <li>新增组件data-dict，简化数据字典使用</li> 
 <li>新增Jaxb依赖，防止jdk8以上出现的兼容错误</li> 
 <li>生产环境使用路由懒加载提升页面响应速度</li> 
 <li>修复五级以上菜单出现的404问题</li> 
 <li>防重提交注解支持配置间隔时间/提示消息</li> 
 <li>日志注解新增是否保存响应参数</li> 
 <li>任务屏蔽违规字符&参数忽略双引号中的逗号</li> 
 <li>升级SpringBoot到最新版本2.5.6</li> 
 <li>升级pagehelper到最新版1.4.0</li> 
 <li>升级spring-boot-mybatis到最新版2.2.0</li> 
 <li>升级oshi到最新版本v5.8.2</li> 
 <li>升级druid到最新版1.2.8</li> 
 <li>升级velocity到最新版本2.3</li> 
 <li>升级fastjson到最新版1.2.78</li> 
 <li>升级axios到最新版本0.24.0</li> 
 <li>升级dart-sass到版本1.32.13</li> 
 <li>升级core-js到最新版本3.19.1</li> 
 <li>升级jsencrypt到最新版本3.2.1</li> 
 <li>升级js-cookie到最新版本3.0.1</li> 
 <li>升级file-saver到最新版本2.0.5</li> 
 <li>升级sass-loader到最新版本10.1.1</li> 
 <li>升级element-ui到最新版本2.15.6</li> 
 <li>新增sendGet无参请求方法</li> 
 <li>禁用el-tag组件的渐变动画</li> 
 <li>代码生成点击预览重置激活tab</li> 
 <li>AjaxResult重写put方法，以方便链式调用</li> 
 <li>优化登录/验证码请求headers不设置token</li> 
 <li>优化用户个人信息接口防止修改用户名</li> 
 <li>优化Cron表达式生成器关闭时销毁避免缓存</li> 
 <li>优化注册成功提示消息类型success</li> 
 <li>优化aop语法，使用spring自动注入注解</li> 
 <li>优化记录登录信息，移除不必要的修改</li> 
 <li>优化mybatis全局默认的执行器</li> 
 <li>优化Excel导入图片可能出现的异常</li> 
 <li>修复代码生成模板主子表删除缺少事务</li> 
 <li>修复日志记录可能出现的转换异常</li> 
 <li>修复代码生成复选框字典遗漏问题</li> 
 <li>修复关闭xss功能导致可重复读RepeatableFilter失效</li> 
 <li>修复字符串无法被反转义问题</li> 
 <li>修复后端主子表代码模板方法名生成错误问题</li> 
 <li>修复xss过滤后格式出现的异常</li> 
 <li>修复swagger没有指定dataTypeClass导致启动出现warn日志</li> 
 <li>其他细节优化</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">若依是一套全部开源的快速开发平台，毫无保留给个人及企业免费使用。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>前端采用Vue、Element UI。</li> 
 <li>后端采用Spring Boot、Spring Security、Redis & Jwt。</li> 
 <li>权限认证使用Jwt，支持多终端认证系统。</li> 
 <li>支持加载动态权限菜单，多方式轻松权限控制。</li> 
 <li>高效率开发，使用代码生成器可以一键生成前后端代码。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下载地址<a href="https://gitee.com/y_project/RuoYi-Vue">RuoYi-Vue</a></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">如需不分离应用，请移步 <a href="https://gitee.com/y_project/RuoYi">RuoYi</a> <code>(保持同步更新)</code>，如需其他版本，请移步 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.ruoyi.vip%2Fruoyi%2Fdocument%2Fxmkz.html" target="_blank">项目扩展</a> <code>(不定时更新)</code></p> 
</blockquote> 
<h2 style="margin-left:0; margin-right:0; text-align:left">内置功能</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>用户管理：用户是系统操作者，该功能主要完成系统用户配置。</li> 
 <li>部门管理：配置系统组织机构（公司、部门、小组），树结构展现支持数据权限。</li> 
 <li>岗位管理：配置系统用户所属担任职务。</li> 
 <li>菜单管理：配置系统菜单，操作权限，按钮权限标识等。</li> 
 <li>角色管理：角色菜单权限分配、设置角色按机构进行数据范围权限划分。</li> 
 <li>字典管理：对系统中经常使用的一些较为固定的数据进行维护。</li> 
 <li>参数管理：对系统动态配置常用参数。</li> 
 <li>通知公告：系统通知公告信息发布维护。</li> 
 <li>操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。</li> 
 <li>登录日志：系统登录日志记录查询包含登录异常。</li> 
 <li>在线用户：当前系统中活跃用户状态监控。</li> 
 <li>定时任务：在线（添加、修改、删除)任务调度包含执行结果日志。</li> 
 <li>代码生成：前后端代码的生成（java、html、xml、sql）支持CRUD下载 。</li> 
 <li>系统接口：根据业务代码自动生成相关的api接口文档。</li> 
 <li>服务监控：监视当前系统CPU、内存、磁盘、堆栈等相关信息。</li> 
 <li>缓存监控：对系统的缓存信息查询，命令统计等。</li> 
 <li>在线构建器：拖动表单元素生成相应的HTML代码。</li> 
 <li>连接池监视：监视当前系统数据库连接池状态，可进行分析SQL找出系统性能瓶颈。</li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:left">在线体验</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue.ruoyi.vip%2F" target="_blank">http://vue.ruoyi.vip</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">文档地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.ruoyi.vip%2F" target="_blank">http://doc.ruoyi.vip</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">演示图</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-indent:0px; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/cd1f90be5f2684f4560c9519c0f2a232ee8.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/1cbcf0e6f257c7d3a063c0e3f2ff989e4b3.jpg" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-8074972883b5ba0622e13246738ebba237a.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-9f88719cdfca9af2e58b352a20e23d43b12.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-39bf2584ec3a529b0d5a3b70d15c9b37646.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-936ec82d1f4872e1bc980927654b6007307.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-b2d62ceb95d2dd9b3fbe157bb70d26001e9.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-d67451d308b7a79ad6819723396f7c3d77a.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/5e8c387724954459291aafd5eb52b456f53.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/644e78da53c2e92a95dfda4f76e6d117c4b.jpg" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-8370a0d02977eebf6dbf854c8450293c937.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-49003ed83f60f633e7153609a53a2b644f7.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-d4fe726319ece268d4746602c39cffc0621.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-c195234bbcd30be6927f037a6755e6ab69c.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<p> </p>
                                        </div>
                                      
</div>
            