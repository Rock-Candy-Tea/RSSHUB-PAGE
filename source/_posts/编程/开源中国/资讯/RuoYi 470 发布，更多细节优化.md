
---
title: 'RuoYi 4.7.0 发布，更多细节优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-42e518aa72a24d228427a1261cb3679f395.png'
author: 开源中国
comments: false
date: Wed, 01 Sep 2021 08:02:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-42e518aa72a24d228427a1261cb3679f395.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">若依管理系统 v4.7.0 已发布，更新日志：</span></p> 
<ul> 
 <li>优化弹出层显示在顶层窗口</li> 
 <li>定时任务支持在线生成cron表达式</li> 
 <li>Excel注解支持Image图片导入</li> 
 <li>支持配置是否开启记住我功能</li> 
 <li>修改时检查用户数据权限范围</li> 
 <li>表单重置开始/结束时间控件</li> 
 <li>新增多图上传示例</li> 
 <li>启用父部门状态排除顶级节点</li> 
 <li>富文本默认dialogsInBody属性</li> 
 <li>去除默认分页合理化参数</li> 
 <li>顶部菜单跳转添加绝对路径</li> 
 <li>升级oshi到最新版本v5.8.0</li> 
 <li>升级shiro到最新版本v1.8.0</li> 
 <li>升级commons.io到最新版本v2.11.0</li> 
 <li>升级jquery到最新版v3.6.0</li> 
 <li>升级icheck到最新版v1.0.3</li> 
 <li>升级layer到最新版本v3.5.1</li> 
 <li>升级layui到最新版本v2.6.8</li> 
 <li>升级laydate到最新版本v5.3.1</li> 
 <li>升级select2到最新版v4.0.13</li> 
 <li>升级cropper到最新版本v1.5.12</li> 
 <li>升级summernote到最新版本v0.8.18</li> 
 <li>升级duallistbox到最新版本v3.0.9</li> 
 <li>升级jquery.validate到最新版本v1.19.3</li> 
 <li>升级bootstrap-suggest到最新版本v0.1.29</li> 
 <li>升级bootstrap-select到最新版本v1.13.18</li> 
 <li>升级bootstrap-fileinput到最新版本v5.2.3</li> 
 <li>查询表格指定列值增加是否去重属性</li> 
 <li>删除sourceMappingURL源映射</li> 
 <li>去除多余的favicon.ico引入</li> 
 <li>优化代码生成模板</li> 
 <li>优化XSS跨站脚本过滤</li> 
 <li>补充定时任务表字段注释</li> 
 <li>定时任务屏蔽ldap远程调用</li> 
 <li>定时任务屏蔽http(s)远程调用</li> 
 <li>定时任务对检查异常进行事务回滚</li> 
 <li>调度日志详细页添加关闭按钮</li> 
 <li>优化异常打印输出信息</li> 
 <li>优化移动端进入首页样式</li> 
 <li>优化用户操作不能删除自己</li> 
 <li>默认开始/结束时间绑定控件选择类型</li> 
 <li>其他细节优化</li> 
</ul> 
<p style="text-align:left">若依是一套全部开源的快速开发平台，毫无保留给个人及企业免费使用（免费商用无需授权）。</p> 
<p style="text-align:left">下载地址<a href="https://gitee.com/y_project/RuoYi">RuoYi</a></p> 
<blockquote> 
 <p>如需分离版本，请移步 <a href="https://gitee.com/y_project/RuoYi-Vue">RuoYi-Vue</a> <code>(保持同步更新)</code>，如需其他版本，请移步 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.ruoyi.vip%2Fruoyi%2Fdocument%2Fxmkz.html" target="_blank">项目扩展</a> <code>(不定时更新)</code></p> 
</blockquote> 
<h4 style="text-align:left">内置功能</h4> 
<p style="text-align:left">1.  用户管理：用户是系统操作者，该功能主要完成系统用户配置。<br> 2.  部门管理：配置系统组织机构（公司、部门、小组），树结构展现支持权限。<br> 3.  岗位管理：配置系统用户所属担任职务。<br> 4.  菜单管理：配置系统菜单，操作权限，按钮权限标识等。<br> 5.  角色管理：角色菜单权限分配、设置角色按机构进行数据范围权限划分。<br> 6.  字典管理：对系统中经常使用的一些较为固定的数据进行维护。<br> 7.  参数管理：对系统动态配置常用参数。<br> 8.  通知公告：系统通知公告信息发布维护。<br> 9.  操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。<br> 10.  登录日志：系统登录日志记录查询包含登录异常。<br> 11. 在线用户：当前系统中活跃用户状态监控。<br> 12. 定时任务：在线（添加、修改、删除)任务调度包含执行结果日志。<br> 13. 代码生成：前后端代码的生成（java、html、xml、sql)支持CRUD下载 。<br> 14. 系统接口：根据业务代码自动生成相关的api接口文档。<br> 15. 服务监控：监视当前系统 CPU、内存、磁盘、堆栈等相关信息。<br> 16. 缓存监控：对系统的缓存查询，删除、清空等操作。<br> 17. 在线构建器：拖动表单元素生成相应的HTML代码。<br> 18. 连接池监视：监视当前系统数据库连接池状态，可进行分析SQL找出系统性能瓶颈。</p> 
<h3 style="text-align:left">系统演示  <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.ruoyi.vip%2F" target="_blank">http://www.ruoyi.vip</a></h3> 
<table cellspacing="0" style="width:776px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-42e518aa72a24d228427a1261cb3679f395.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-7f20dd0edba25e5187c5c4dd3ec7d3d9797.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-2dae3d87f6a8ca05057db059cd9a411d51d.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-ea4d98423471e55fba784694e45d12bd4bb.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-7f6c6e9f5873efca09bd2870ee8468b8fce.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-c708b65f2c382a03f69fe1efa8d341e6cff.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-9ab586c47dd5c7b92bca0d727962c90e3b8.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-ef954122a2080e02013112db21754b955c6.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-088edb4d531e122415a1e2342bccb1a9691.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-f886fe19bd820c0efae82f680223cac196c.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-c7a2eb71fa65d6e660294b4bccca613d638.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-e60137fb0787defe613bd83331dc4755a70.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-7c51c1b5758f0a0f92ed3c60469b7526f9f.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-15181aed45bb2461aa97b594cbf2f86ea5f.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-83326ad52ea63f67233d126226738054d98.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-3bd6d31e913b70df00107db51d64ef81df7.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-70a2225836bc82042a6785edf6299e2586a.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-0184d6ab01fdc6667a14327fcaf8b46345d.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-64d8086dc2c02c8f71170290482f7640098.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-5e4daac0bb59612c5038448acbcef235e3a.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            