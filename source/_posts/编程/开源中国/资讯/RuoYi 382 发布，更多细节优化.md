
---
title: 'RuoYi 3.8.2 发布，更多细节优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/cd1f90be5f2684f4560c9519c0f2a232ee8.jpg'
author: 开源中国
comments: false
date: Fri, 01 Apr 2022 07:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/cd1f90be5f2684f4560c9519c0f2a232ee8.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">若依前后端分离版本<span style="background-color:#ffffff; color:#333333"> v3.8.1 已发布，更新日志：</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>前端支持设置是否需要防止数据重复提交</li> 
 <li>开启TopNav没有子菜单情况隐藏侧边栏</li> 
 <li>侧边栏菜单名称过长悬停显示标题</li> 
 <li>用户访问控制时校验数据权限，防止越权</li> 
 <li>导出Excel时屏蔽公式，防止CSV注入风险</li> 
 <li>组件ImagePreview支持多图预览显示</li> 
 <li>组件ImageUpload支持多图同时选择上传</li> 
 <li>组件FileUpload支持多文件同时选择上传</li> 
 <li>服务监控新增运行参数信息显示</li> 
 <li>定时任务目标字符串过滤特殊字符</li> 
 <li>定时任务目标字符串验证包名白名单</li> 
 <li>代码生成列表图片支持预览</li> 
 <li>代码生成编辑修改打开新页签</li> 
 <li>代码生成新增Java类型Boolean</li> 
 <li>代码生成子表支持日期/字典配置</li> 
 <li>代码生成同步保留必填/类型选项</li> 
 <li>升级oshi到最新版本6.1.2</li> 
 <li>升级fastjson到最新版1.2.80</li> 
 <li>升级pagehelper到最新版1.4.1</li> 
 <li>升级spring-boot到最新版本2.5.11</li> 
 <li>升级spring-boot-mybatis到最新版2.2.2</li> 
 <li>添加遗漏的分页参数合理化属性</li> 
 <li>修改npm即将过期的注册源地址</li> 
 <li>修复分页组件请求两次问题</li> 
 <li>修复通用文件下载接口跨域问题</li> 
 <li>修复Xss注解字段值为空时的异常问题</li> 
 <li>修复选项卡点击右键刷新丢失参数问题</li> 
 <li>修复表单清除元素位置未垂直居中问题</li> 
 <li>修复服务监控中运行参数显示条件错误</li> 
 <li>修复导入Excel时字典字段类型为Long转义为空问题</li> 
 <li>修复登录超时刷新页面跳转登录页面还提示重新登录问题</li> 
 <li>优化加载字典缓存数据</li> 
 <li>优化IP地址获取到多个的问题</li> 
 <li>优化任务队列满时任务拒绝策略</li> 
 <li>优化文件上传兼容Weblogic环境</li> 
 <li>优化定时任务默认保存到内存中执行</li> 
 <li>优化部门修改缩放后出现的错位问题</li> 
 <li>优化Excel格式化不同类型的日期对象</li> 
 <li>优化菜单表关键字导致的插件报错问题</li> 
 <li>优化Oracle用户头像列为空时不显示问题</li> 
 <li>优化页面若未匹配到字典标签则返回原字典值</li> 
 <li>优化修复登录失效后多次请求提示多次弹窗问题</li> 
 <li>其他细节优化</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">若依是一套全部开源的快速开发平台，毫无保留给个人及企业免费使用。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>前端采用Vue、Element UI。</li> 
 <li>后端采用Spring Boot、Spring Security、Redis & Jwt。</li> 
 <li>权限认证使用Jwt，支持多终端认证系统。</li> 
 <li>支持加载动态权限菜单，多方式轻松权限控制。</li> 
 <li>高效率开发，使用代码生成器可以一键生成前后端代码。</li> 
 <li>提供了技术栈（Vue3 Element Plus Vite）版本RuoYi-Vue3，保持同步更新。</li> 
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
                                        </div>
                                      
</div>
            