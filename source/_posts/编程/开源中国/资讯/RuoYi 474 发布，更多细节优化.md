
---
title: 'RuoYi 4.7.4 发布，更多细节优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-42e518aa72a24d228427a1261cb3679f395.png'
author: 开源中国
comments: false
date: Wed, 01 Jun 2022 07:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-42e518aa72a24d228427a1261cb3679f395.png'
---

<div>   
<div class="content">
                                                                                            <p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left"><span data-darkreader-inline-bgcolor data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-color:#c8c3bc; background-color:#ffffff; color:#333333">若依管理系统 v4.7.4 已发布，更新日志：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>用户头像上传图片格式限制</li> 
 <li>Excel注解支持color属性设置字体颜色</li> 
 <li>设置分页参数默认值</li> 
 <li>主子表操作列新增单个删除</li> 
 <li>定时任务检查Bean包名是否为白名单配置</li> 
 <li>升级spring-boot到最新版本2.5.14</li> 
 <li>升级shiro到最新版本1.9.0</li> 
 <li>升级oshi到最新版本6.1.6</li> 
 <li>升级fastjson到最新版1.2.83 安全修复版本</li> 
 <li>文件上传兼容Weblogic环境</li> 
 <li>新增清理分页的线程变量方法</li> 
 <li>新增获取不带后缀文件名称方法</li> 
 <li>用户缓存信息添加部门ancestors祖级列表</li> 
 <li>自定义ShiroFilterFactoryBean防止中文请求被拦截</li> 
 <li>字典类型必须以字母开头，且只能为（小写字母，数字，下滑线）</li> 
 <li>优化IP地址获取到多个的问题</li> 
 <li>优化表格冻结列阴影效果显示</li> 
 <li>优化菜单侧边栏滚动条尺寸及颜色</li> 
 <li>优化显示顺序orderNum类型为整型</li> 
 <li>优化接口使用泛型使其看到响应属性字段</li> 
 <li>优化导出数据LocalDateTime类型无数据问题</li> 
 <li>修复导入Excel时字典字段类型为Long转义为空问题</li> 
 <li>优化导出excel单元格验证,包含变更为开头.防止正常内容被替换</li> 
 <li>修复URL类型回退键被禁止问题</li> 
 <li>修复表格客户端分页序号显示错误问题</li> 
 <li>修复代码生成拖拽多次出现的排序不正确问题</li> 
 <li>修复表格打印组件不识别多层对象属性值问题</li> 
 <li>修复操作日志查询类型条件为0时会查到所有数据</li> 
 <li>修复Excel注解prompt/combo同时使用不生效问题</li> 
 <li>修复初始化多表格处理回调函数时获取的表格配置不一致问题</li> 
 <li>其他细节优化</li> 
</ul> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left">若依是一套全部开源的快速开发平台，毫无保留给个人及企业免费使用（免费商用无需授权）。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left">下载地址<span> </span><a href="https://gitee.com/y_project/RuoYi">RuoYi</a></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">如需分离版本，请移步 <a href="https://gitee.com/y_project/RuoYi-Vue">RuoYi-Vue</a> ，如需微服务版本，请移步 <a href="https://gitee.com/y_project/RuoYi-Cloud" target="_blank">RuoYi-Cloud</a> </p> 
</blockquote> 
<h4 style="margin-left:0; margin-right:0; text-align:left">内置功能</h4> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left">1.  用户管理：用户是系统操作者，该功能主要完成系统用户配置。<br> 2.  部门管理：配置系统组织机构（公司、部门、小组），树结构展现支持权限。<br> 3.  岗位管理：配置系统用户所属担任职务。<br> 4.  菜单管理：配置系统菜单，操作权限，按钮权限标识等。<br> 5.  角色管理：角色菜单权限分配、设置角色按机构进行数据范围权限划分。<br> 6.  字典管理：对系统中经常使用的一些较为固定的数据进行维护。<br> 7.  参数管理：对系统动态配置常用参数。<br> 8.  通知公告：系统通知公告信息发布维护。<br> 9.  操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。<br> 10.  登录日志：系统登录日志记录查询包含登录异常。<br> 11. 在线用户：当前系统中活跃用户状态监控。<br> 12. 定时任务：在线（添加、修改、删除) 任务调度包含执行结果日志。<br> 13. 代码生成：前后端代码的生成（java、html、xml、sql) 支持 CRUD 下载 。<br> 14. 系统接口：根据业务代码自动生成相关的 api 接口文档。<br> 15. 服务监控：监视当前系统 CPU、内存、磁盘、堆栈等相关信息。<br> 16. 缓存监控：对系统的缓存查询，删除、清空等操作。<br> 17. 在线构建器：拖动表单元素生成相应的 HTML 代码。<br> 18. 连接池监视：监视当前系统数据库连接池状态，可进行分析 SQL 找出系统性能瓶颈。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">系统演示  <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.ruoyi.vip%2F" target="_blank">http://www.ruoyi.vip</a></h3> 
<table cellspacing="0" data-darkreader-inline-bgcolor data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-border-bottom:currentcolor; --darkreader-inline-border-left:currentcolor; --darkreader-inline-border-right:currentcolor; --darkreader-inline-border-top:currentcolor; --darkreader-inline-color:#bdb7af; -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:medium none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px; max-width:100%; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-indent:0px; text-transform:none; white-space:normal; width:776px; word-break:keep-all; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-42e518aa72a24d228427a1261cb3679f395.png" referrerpolicy="no-referrer"></td> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-7f20dd0edba25e5187c5c4dd3ec7d3d9797.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-2dae3d87f6a8ca05057db059cd9a411d51d.png" referrerpolicy="no-referrer"></td> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-ea4d98423471e55fba784694e45d12bd4bb.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-7f6c6e9f5873efca09bd2870ee8468b8fce.png" referrerpolicy="no-referrer"></td> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-c708b65f2c382a03f69fe1efa8d341e6cff.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-9ab586c47dd5c7b92bca0d727962c90e3b8.png" referrerpolicy="no-referrer"></td> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-ef954122a2080e02013112db21754b955c6.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-088edb4d531e122415a1e2342bccb1a9691.png" referrerpolicy="no-referrer"></td> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-f886fe19bd820c0efae82f680223cac196c.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-c7a2eb71fa65d6e660294b4bccca613d638.png" referrerpolicy="no-referrer"></td> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-e60137fb0787defe613bd83331dc4755a70.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-7c51c1b5758f0a0f92ed3c60469b7526f9f.png" referrerpolicy="no-referrer"></td> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-15181aed45bb2461aa97b594cbf2f86ea5f.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-83326ad52ea63f67233d126226738054d98.png" referrerpolicy="no-referrer"></td> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-3bd6d31e913b70df00107db51d64ef81df7.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-70a2225836bc82042a6785edf6299e2586a.png" referrerpolicy="no-referrer"></td> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-0184d6ab01fdc6667a14327fcaf8b46345d.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-64d8086dc2c02c8f71170290482f7640098.png" referrerpolicy="no-referrer"></td> 
   <td data-darkreader-inline-border-bottom data-darkreader-inline-border-left data-darkreader-inline-border-right data-darkreader-inline-border-top style="--darkreader-inline-border-bottom:#3a3e41; --darkreader-inline-border-left:#3a3e41; --darkreader-inline-border-right:#3a3e41; --darkreader-inline-border-top:#3a3e41; border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-5e4daac0bb59612c5038448acbcef235e3a.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<p> </p>
                                        </div>
                                      
</div>
            