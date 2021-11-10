
---
title: 'RuoYi 4.7.1 发布，更多细节优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-42e518aa72a24d228427a1261cb3679f395.png'
author: 开源中国
comments: false
date: Wed, 10 Nov 2021 08:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-42e518aa72a24d228427a1261cb3679f395.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">若依管理系统 v4.7.1 已发布，更新日志：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>新增是否开启页签功能</li> 
 <li>代码生成的模块增加创建表功能</li> 
 <li>Excel导入支持@Excels注解</li> 
 <li>Excel注解支持导入导出标题信息</li> 
 <li>Excel注解支持自定义数据处理器</li> 
 <li>日志注解新增是否保存响应参数</li> 
 <li>防重提交注解支持配置间隔时间/提示消息</li> 
 <li>网页部分操作禁止使用后退键（Backspace）</li> 
 <li>实例演示中增加多层窗口获取值</li> 
 <li>弹出层openOptions增加动画属性</li> 
 <li>升级spring-boot到最新版本2.5.6</li> 
 <li>升级spring-boot-mybatis到最新版2.2.0</li> 
 <li>升级pagehelper到最新版1.4.0</li> 
 <li>升级oshi到最新版本v5.8.2</li> 
 <li>升级druid到最新版1.2.8</li> 
 <li>升级fastjson到最新版1.2.78</li> 
 <li>升级thymeleaf-extras-shiro到最新版本v2.1.0</li> 
 <li>升级bootstrap-fileinput到最新版本v5.2.4</li> 
 <li>修改阿里云maven仓库地址为新版地址</li> 
 <li>定时任务屏蔽违规字符</li> 
 <li>增加sendGet无参请求方法</li> 
 <li>代码生成去掉多余的排序字段</li> 
 <li>优化启动脚本参数优化</li> 
 <li>优化页签关闭右侧清除iframe元素</li> 
 <li>优化多表格切换表单查询参数</li> 
 <li>优化表格实例切换event不能为空</li> 
 <li>优化mybatis全局默认的执行器</li> 
 <li>优化导入Excel数据关闭时清理file</li> 
 <li>优化Excel导入图片可能出现的异常</li> 
 <li>优化记录登录信息，防止不必要的修改</li> 
 <li>优化aop语法，使用spring自动注入注解</li> 
 <li>修复无法被反转义问题</li> 
 <li>修复拖拽行数据错位问题</li> 
 <li>修复新窗口打开页面关闭弹窗报错</li> 
 <li>修复富文本回退键被禁止&控制台报错问题</li> 
 <li>修复自定义弹出层全屏参数无效问题</li> 
 <li>修复树表代码生成短字段无法识别问题</li> 
 <li>修复apple/webkit浏览器时间无法格式化</li> 
 <li>修复后端主子表代码模板方法名生成错误问题</li> 
 <li>修复swagger没有指定dataTypeClass导致启动出现warn日志</li> 
 <li>其他细节优化</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">若依是一套全部开源的快速开发平台，毫无保留给个人及企业免费使用（免费商用无需授权）。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下载地址<a href="https://gitee.com/y_project/RuoYi">RuoYi</a></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">如需分离版本，请移步 <a href="https://gitee.com/y_project/RuoYi-Vue">RuoYi-Vue</a> <code>(保持同步更新)</code>，如需其他版本，请移步 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.ruoyi.vip%2Fruoyi%2Fdocument%2Fxmkz.html" target="_blank">项目扩展</a> <code>(不定时更新)</code></p> 
</blockquote> 
<h4 style="margin-left:0; margin-right:0; text-align:left">内置功能</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.  用户管理：用户是系统操作者，该功能主要完成系统用户配置。<br> 2.  部门管理：配置系统组织机构（公司、部门、小组），树结构展现支持权限。<br> 3.  岗位管理：配置系统用户所属担任职务。<br> 4.  菜单管理：配置系统菜单，操作权限，按钮权限标识等。<br> 5.  角色管理：角色菜单权限分配、设置角色按机构进行数据范围权限划分。<br> 6.  字典管理：对系统中经常使用的一些较为固定的数据进行维护。<br> 7.  参数管理：对系统动态配置常用参数。<br> 8.  通知公告：系统通知公告信息发布维护。<br> 9.  操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。<br> 10.  登录日志：系统登录日志记录查询包含登录异常。<br> 11. 在线用户：当前系统中活跃用户状态监控。<br> 12. 定时任务：在线（添加、修改、删除)任务调度包含执行结果日志。<br> 13. 代码生成：前后端代码的生成（java、html、xml、sql)支持CRUD下载 。<br> 14. 系统接口：根据业务代码自动生成相关的api接口文档。<br> 15. 服务监控：监视当前系统 CPU、内存、磁盘、堆栈等相关信息。<br> 16. 缓存监控：对系统的缓存查询，删除、清空等操作。<br> 17. 在线构建器：拖动表单元素生成相应的HTML代码。<br> 18. 连接池监视：监视当前系统数据库连接池状态，可进行分析SQL找出系统性能瓶颈。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">系统演示  <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.ruoyi.vip%2F" target="_blank">http://www.ruoyi.vip</a></h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-indent:0px; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-42e518aa72a24d228427a1261cb3679f395.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-7f20dd0edba25e5187c5c4dd3ec7d3d9797.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-2dae3d87f6a8ca05057db059cd9a411d51d.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-ea4d98423471e55fba784694e45d12bd4bb.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-7f6c6e9f5873efca09bd2870ee8468b8fce.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-c708b65f2c382a03f69fe1efa8d341e6cff.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-9ab586c47dd5c7b92bca0d727962c90e3b8.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-ef954122a2080e02013112db21754b955c6.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-088edb4d531e122415a1e2342bccb1a9691.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-f886fe19bd820c0efae82f680223cac196c.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-c7a2eb71fa65d6e660294b4bccca613d638.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-e60137fb0787defe613bd83331dc4755a70.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-7c51c1b5758f0a0f92ed3c60469b7526f9f.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-15181aed45bb2461aa97b594cbf2f86ea5f.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-83326ad52ea63f67233d126226738054d98.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-3bd6d31e913b70df00107db51d64ef81df7.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-70a2225836bc82042a6785edf6299e2586a.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-0184d6ab01fdc6667a14327fcaf8b46345d.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-64d8086dc2c02c8f71170290482f7640098.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-5e4daac0bb59612c5038448acbcef235e3a.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            