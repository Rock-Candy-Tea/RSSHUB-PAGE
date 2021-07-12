
---
title: 'RuoYi-Vue 3.6.0 发布，更多细节优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/cd1f90be5f2684f4560c9519c0f2a232ee8.jpg'
author: 开源中国
comments: false
date: Mon, 12 Jul 2021 08:29:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/cd1f90be5f2684f4560c9519c0f2a232ee8.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">若依前后端分离版本<span style="background-color:#ffffff; color:#333333"> v3.6.0 已发布，更新日志：</span></p> 
<ol> 
 <li>角色管理新增分配用户功能</li> 
 <li>用户管理新增分配角色功能</li> 
 <li>日志列表支持排序操作</li> 
 <li>优化参数&字典缓存操作</li> 
 <li>系统布局配置支持动态标题开关</li> 
 <li>菜单路由配置支持内链访问</li> 
 <li>默认访问后端首页新增提示语</li> 
 <li>富文本默认上传返回url类型</li> 
 <li>新增自定义弹窗拖拽指令</li> 
 <li>全局注册常用通用组件</li> 
 <li>全局挂载字典标签组件</li> 
 <li>ImageUpload组件支持多图片上传</li> 
 <li>FileUpload组件支持多文件上传</li> 
 <li>文件上传组件添加数量限制属性</li> 
 <li>富文本编辑组件添加类型属性</li> 
 <li>富文本组件工具栏配置视频</li> 
 <li>封装通用iframe组件</li> 
 <li>限制超级管理员不允许操作</li> 
 <li>用户信息长度校验限制</li> 
 <li>分页组件新增pagerCount属性</li> 
 <li>添加bat脚本执行应用</li> 
 <li>升级oshi到最新版本v5.7.4</li> 
 <li>升级element-ui到最新版本2.15.2</li> 
 <li>升级pagehelper到最新版1.3.1</li> 
 <li>升级commons.io到最新版本v2.10.0</li> 
 <li>升级commons.fileupload到最新版本v1.4</li> 
 <li>升级swagger到最新版本v3.0.0</li> 
 <li>修复关闭confirm提示框控制台报错问题</li> 
 <li>修复存在的SQL注入漏洞问题</li> 
 <li>定时任务屏蔽rmi远程调用</li> 
 <li>修复用户搜索分页变量错误</li> 
 <li>修复导出角色数据范围翻译缺少仅本人</li> 
 <li>修复表单构建选择下拉选择控制台报错问题</li> 
 <li>优化图片工具类读取文件</li> 
 <li>其他细节优化</li> 
</ol> 
<p style="text-align:left">若依是一套全部开源的快速开发平台，毫无保留给个人及企业免费使用。</p> 
<ul> 
 <li>前端采用Vue、Element UI。</li> 
 <li>后端采用Spring Boot、Spring Security、Redis & Jwt。</li> 
 <li>权限认证使用Jwt，支持多终端认证系统。</li> 
 <li>支持加载动态权限菜单，多方式轻松权限控制。</li> 
 <li>高效率开发，使用代码生成器可以一键生成前后端代码。</li> 
</ul> 
<p style="text-align:left">下载地址<a href="https://gitee.com/y_project/RuoYi-Vue">RuoYi-Vue</a></p> 
<blockquote> 
 <p>如需不分离应用，请移步 <a href="https://gitee.com/y_project/RuoYi">RuoYi</a> <code>(保持同步更新)</code>，如需其他版本，请移步 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.ruoyi.vip%2Fruoyi%2Fdocument%2Fxmkz.html" target="_blank">项目扩展</a> <code>(不定时更新)</code></p> 
</blockquote> 
<h2 style="text-align:left">内置功能</h2> 
<ol> 
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
<h2 style="text-align:left">在线体验</h2> 
<p style="text-align:left">演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue.ruoyi.vip%2F" target="_blank">http://vue.ruoyi.vip</a></p> 
<p style="text-align:left">文档地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.ruoyi.vip%2F" target="_blank">http://doc.ruoyi.vip</a></p> 
<h2 style="text-align:left">演示图</h2> 
<table cellspacing="0" style="width:776px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/cd1f90be5f2684f4560c9519c0f2a232ee8.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/1cbcf0e6f257c7d3a063c0e3f2ff989e4b3.jpg" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-8074972883b5ba0622e13246738ebba237a.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-9f88719cdfca9af2e58b352a20e23d43b12.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-39bf2584ec3a529b0d5a3b70d15c9b37646.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-936ec82d1f4872e1bc980927654b6007307.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-b2d62ceb95d2dd9b3fbe157bb70d26001e9.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-d67451d308b7a79ad6819723396f7c3d77a.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/5e8c387724954459291aafd5eb52b456f53.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/644e78da53c2e92a95dfda4f76e6d117c4b.jpg" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-8370a0d02977eebf6dbf854c8450293c937.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-49003ed83f60f633e7153609a53a2b644f7.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-d4fe726319ece268d4746602c39cffc0621.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-c195234bbcd30be6927f037a6755e6ab69c.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            