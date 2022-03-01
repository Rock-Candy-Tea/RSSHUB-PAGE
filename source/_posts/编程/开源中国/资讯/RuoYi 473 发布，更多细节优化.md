
---
title: 'RuoYi 4.7.3 发布，更多细节优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-42e518aa72a24d228427a1261cb3679f395.png'
author: 开源中国
comments: false
date: Tue, 01 Mar 2022 08:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-42e518aa72a24d228427a1261cb3679f395.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">若依管理系统 v4.7.3 已发布，更新日志：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>表格树支持分页/异步加载</li> 
 <li>代码生成预览支持复制内容</li> 
 <li>定时任务默认保存到内存中执行</li> 
 <li>代码生成同步保留必填/类型选项</li> 
 <li>页面若未匹配到字典标签则返回原字典值</li> 
 <li>用户访问控制时校验数据权限，防止越权</li> 
 <li>导出Excel时屏蔽公式，防止CSV注入风险</li> 
 <li>升级spring-boot到最新版本2.5.10</li> 
 <li>升级spring-boot-mybatis到最新版2.2.2</li> 
 <li>升级pagehelper到最新版1.4.1</li> 
 <li>升级oshi到最新版本6.1.2</li> 
 <li>升级bootstrap-table到最新版本1.19.1</li> 
 <li>服务监控新增运行参数信息显示</li> 
 <li>定时任务目标字符串验证包名白名单</li> 
 <li>文件上传接口新增原/新文件名返回参数</li> 
 <li>定时任务屏蔽违规的字符</li> 
 <li>分页数据新增分页参数合理化参数</li> 
 <li>表格父子视图添加点击事件打开示例</li> 
 <li>优化上传文件名称命名规则</li> 
 <li>优化加载字典缓存数据</li> 
 <li>优化任务队列满时任务拒绝策略</li> 
 <li>优化IE11上传预览不显示的问题</li> 
 <li>优化Excel格式化不同类型的日期对象</li> 
 <li>优化国际化配置多余的zh请求问题</li> 
 <li>优化新版Chrome浏览器回退出现的遮罩层</li> 
 <li>修复EMAIL类型回退键被禁止问题</li> 
 <li>修复Xss注解字段值为空时的异常问题</li> 
 <li>其他细节优化</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">若依是一套全部开源的快速开发平台，毫无保留给个人及企业免费使用（免费商用无需授权）。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下载地址<a href="https://gitee.com/y_project/RuoYi">RuoYi</a></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">如需分离版本，请移步 <a href="https://gitee.com/y_project/RuoYi-Vue">RuoYi-Vue</a> ，如需微服务版本，请移步 <a href="https://gitee.com/y_project/RuoYi-Cloud" target="_blank">RuoYi-Cloud</a> </p> 
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
<p> </p>
                                        </div>
                                      
</div>
            