
---
title: 'RuoYi-Vue 3.7.0 发布，更多细节优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/cd1f90be5f2684f4560c9519c0f2a232ee8.jpg'
author: 开源中国
comments: false
date: Mon, 13 Sep 2021 08:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/cd1f90be5f2684f4560c9519c0f2a232ee8.jpg'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">若依前后端分离版本<span style="box-sizing: inherit; background-color: rgb(255, 255, 255); color: rgb(51, 51, 51);"> v3.7.0 已发布，更新日志：</span></p> 
 <ol style="box-sizing: inherit; margin: 0px 0px 20px; list-style-type: decimal; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;"> 
  <li>参数管理支持配置验证码开关</li> 
  <li>新增是否开启用户注册功能</li> 
  <li>定时任务支持在线生成cron表达式</li> 
  <li>菜单管理支持配置路由参数</li> 
  <li>支持自定义注解实现接口限流</li> 
  <li>Excel注解支持Image图片导入</li> 
  <li>自定义弹层溢出滚动样式</li> 
  <li>自定义可拖动弹窗宽度指令</li> 
  <li>自定义可拖动弹窗高度指令</li> 
  <li>修复任意账户越权问题</li> 
  <li>修改时检查用户数据权限范围</li> 
  <li>修复保存配置主题颜色失效问题</li> 
  <li>新增暗色菜单风格主题</li> 
  <li>菜单&部门新增展开/折叠功能</li> 
  <li>页签新增关闭左侧&添加图标</li> 
  <li>顶部菜单排除隐藏的默认路由</li> 
  <li>顶部菜单同步系统主题样式</li> 
  <li>跳转路由高亮相对应的菜单栏</li> 
  <li>代码生成主子表多选行数据</li> 
  <li>日期范围支持添加多组</li> 
  <li>升级element-ui到最新版本2.15.5</li> 
  <li>升级oshi到最新版本v5.8.0</li> 
  <li>升级commons.io到最新版本v2.11.0</li> 
  <li>定时任务屏蔽ldap远程调用</li> 
  <li>定时任务屏蔽http(s)远程调用</li> 
  <li>补充定时任务表字段注释</li> 
  <li>定时任务对检查异常进行事务回滚</li> 
  <li>启用父部门状态排除顶级节点</li> 
  <li>富文本新增上传文件大小限制</li> 
  <li>默认首页使用keep-alive缓存</li> 
  <li>修改代码生成字典回显样式</li> 
  <li>自定义分页合理化传入参数</li> 
  <li>修复字典组件值为整形不显示问题</li> 
  <li>修复定时任务日志执行状态显示</li> 
  <li>角色&菜单新增字段属性提示信息</li> 
  <li>修复角色分配用户页面参数类型错误提醒</li> 
  <li>优化布局设置动画特效</li> 
  <li>优化异常处理信息</li> 
  <li>优化错误token导致的解析异常</li> 
  <li>密码框新增显示切换密码图标</li> 
  <li>定时任务新增更多操作</li> 
  <li>更多操作按钮添加权限控制</li> 
  <li>导入用户样式优化</li> 
  <li>提取通用方法到基类控制器</li> 
  <li>优化使用权限工具获取用户信息</li> 
  <li>优化用户不能删除自己</li> 
  <li>优化XSS跨站脚本过滤</li> 
  <li>优化代码生成模板</li> 
  <li>验证码默认20s超时</li> 
  <li>BLOB下载时清除URL对象引用</li> 
  <li>代码生成导入表按创建时间排序</li> 
  <li>修复代码生成页面数据编辑保存之后总是跳转第一页的问题</li> 
  <li>修复带safari浏览器无法格式化utc日期格式yyyy-MM-dd'T'HH🇲🇲ss.SSS问题</li> 
  <li>多图上传组件移除多余的api地址&验证失败导致图片删除问题&无法删除相应图片修复</li> 
  <li>其他细节优化</li> 
 </ol> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">若依是一套全部开源的快速开发平台，毫无保留给个人及企业免费使用。</p> 
 <ul style="box-sizing: inherit; margin: 0px 0px 20px; list-style-type: disc; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;"> 
  <li style="box-sizing: inherit; line-height: 1.875em; margin-top: 0px;">前端采用Vue、Element UI。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">后端采用Spring Boot、Spring Security、Redis & Jwt。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">权限认证使用Jwt，支持多终端认证系统。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">支持加载动态权限菜单，多方式轻松权限控制。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em; margin-bottom: 0px;">高效率开发，使用代码生成器可以一键生成前后端代码。</li> 
 </ul> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">下载地址<a href="https://gitee.com/y_project/RuoYi-Vue" style="box-sizing: inherit; background-color: transparent; color: rgb(52, 111, 182); text-decoration: none;">RuoYi-Vue</a></p> 
 <blockquote style="box-sizing: inherit; position: relative; margin: 0px 0px 20px; padding: 20px; background-color: rgb(246, 246, 246); border-left: 6px solid rgb(230, 230, 230); font-style: normal; font-weight: 400; word-break: break-word; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-style: initial; text-decoration-color: initial;"> 
  <p style="box-sizing: inherit; margin: 0px; line-height: inherit;">如需不分离应用，请移步 <a href="https://gitee.com/y_project/RuoYi" style="box-sizing: inherit; background-color: transparent; color: rgb(52, 111, 182); text-decoration: none;">RuoYi</a> <code style="box-sizing: inherit; font-family: Consolas, Monaco, "Andale Mono", "Ubuntu Mono", monospace; font-size: 13px; margin: 0px 3px; padding: 3px 4px; border: none; border-radius: 4px; background: rgb(238, 238, 238); color: rgb(51, 51, 51);">(保持同步更新)</code>，如需其他版本，请移步 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.ruoyi.vip%2Fruoyi%2Fdocument%2Fxmkz.html" style="box-sizing: inherit; background-color: transparent; color: rgb(52, 111, 182); text-decoration: none;" target="_blank">项目扩展</a> <code style="box-sizing: inherit; font-family: Consolas, Monaco, "Andale Mono", "Ubuntu Mono", monospace; font-size: 13px; margin: 0px 3px; padding: 3px 4px; border: none; border-radius: 4px; background: rgb(238, 238, 238); color: rgb(51, 51, 51);">(不定时更新)</code></p> 
 </blockquote> 
 <h2 style="box-sizing: inherit; font-family: "PingFang SC", "Helvetica Neue", "Microsoft YaHei UI", "Microsoft YaHei", "Noto Sans CJK SC", Sathu, EucrosiaUPC, Arial, Helvetica, sans-serif; line-height: 1.8; margin: 22px 0px 16px; font-weight: 600; padding: 0px; font-size: 24px; border: none; color: rgb(51, 51, 51); font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">内置功能</h2> 
 <ol style="box-sizing: inherit; margin: 0px 0px 20px; list-style-type: decimal; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;"> 
  <li style="box-sizing: inherit; line-height: 1.875em; margin-top: 0px;">用户管理：用户是系统操作者，该功能主要完成系统用户配置。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">部门管理：配置系统组织机构（公司、部门、小组），树结构展现支持数据权限。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">岗位管理：配置系统用户所属担任职务。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">菜单管理：配置系统菜单，操作权限，按钮权限标识等。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">角色管理：角色菜单权限分配、设置角色按机构进行数据范围权限划分。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">字典管理：对系统中经常使用的一些较为固定的数据进行维护。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">参数管理：对系统动态配置常用参数。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">通知公告：系统通知公告信息发布维护。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">登录日志：系统登录日志记录查询包含登录异常。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">在线用户：当前系统中活跃用户状态监控。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">定时任务：在线（添加、修改、删除)任务调度包含执行结果日志。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">代码生成：前后端代码的生成（java、html、xml、sql）支持CRUD下载 。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">系统接口：根据业务代码自动生成相关的api接口文档。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">服务监控：监视当前系统CPU、内存、磁盘、堆栈等相关信息。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">缓存监控：对系统的缓存信息查询，命令统计等。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">在线构建器：拖动表单元素生成相应的HTML代码。</li> 
  <li style="box-sizing: inherit; line-height: 1.875em; margin-bottom: 0px;">连接池监视：监视当前系统数据库连接池状态，可进行分析SQL找出系统性能瓶颈。</li> 
 </ol> 
 <h2 style="box-sizing: inherit; font-family: "PingFang SC", "Helvetica Neue", "Microsoft YaHei UI", "Microsoft YaHei", "Noto Sans CJK SC", Sathu, EucrosiaUPC, Arial, Helvetica, sans-serif; line-height: 1.8; margin: 22px 0px 16px; font-weight: 600; padding: 0px; font-size: 24px; border: none; color: rgb(51, 51, 51); font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">在线体验</h2> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue.ruoyi.vip%2F" style="box-sizing: inherit; background-color: transparent; color: rgb(52, 111, 182); text-decoration: none;" target="_blank">http://vue.ruoyi.vip</a></p> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">文档地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.ruoyi.vip%2F" style="box-sizing: inherit; background-color: transparent; color: rgb(52, 111, 182); text-decoration: none;" target="_blank">http://doc.ruoyi.vip</a></p> 
 <h2 style="box-sizing: inherit; font-family: "PingFang SC", "Helvetica Neue", "Microsoft YaHei UI", "Microsoft YaHei", "Noto Sans CJK SC", Sathu, EucrosiaUPC, Arial, Helvetica, sans-serif; line-height: 1.8; margin: 22px 0px 16px; font-weight: 600; padding: 0px; font-size: 24px; border: none; color: rgb(51, 51, 51); font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;">演示图</h2> 
 <table cellspacing="0" style="box-sizing: border-box; display: block; border-collapse: collapse; border-spacing: 1px; font-size: 14px; color: rgb(68, 68, 68); overflow: auto; width: 776px; border: none; line-height: inherit; word-break: keep-all; margin: 0px; max-width: 100%; font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;"> 
  <tbody style="box-sizing: inherit;"> 
   <tr style="box-sizing: inherit; background-color: rgb(255, 255, 255);"> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/cd1f90be5f2684f4560c9519c0f2a232ee8.jpg" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/1cbcf0e6f257c7d3a063c0e3f2ff989e4b3.jpg" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
   </tr> 
   <tr style="box-sizing: inherit; background-color: rgb(248, 248, 248);"> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/up-8074972883b5ba0622e13246738ebba237a.png" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/up-9f88719cdfca9af2e58b352a20e23d43b12.png" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
   </tr> 
   <tr style="box-sizing: inherit; background-color: rgb(255, 255, 255);"> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/up-39bf2584ec3a529b0d5a3b70d15c9b37646.png" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/up-936ec82d1f4872e1bc980927654b6007307.png" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
   </tr> 
   <tr style="box-sizing: inherit; background-color: rgb(248, 248, 248);"> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/up-b2d62ceb95d2dd9b3fbe157bb70d26001e9.png" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/up-d67451d308b7a79ad6819723396f7c3d77a.png" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
   </tr> 
   <tr style="box-sizing: inherit; background-color: rgb(255, 255, 255);"> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/5e8c387724954459291aafd5eb52b456f53.jpg" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/644e78da53c2e92a95dfda4f76e6d117c4b.jpg" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
   </tr> 
   <tr style="box-sizing: inherit; background-color: rgb(248, 248, 248);"> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/up-8370a0d02977eebf6dbf854c8450293c937.png" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/up-49003ed83f60f633e7153609a53a2b644f7.png" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
   </tr> 
   <tr style="box-sizing: inherit; background-color: rgb(255, 255, 255);"> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/up-d4fe726319ece268d4746602c39cffc0621.png" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
    <td style="box-sizing: inherit; padding: 4px 8px; border: 1px solid rgb(221, 221, 221);"><img class="zoom-in-cursor" src="https://oscimg.oschina.net/oscnet/up-c195234bbcd30be6927f037a6755e6ab69c.png" style="box-sizing: border-box; border: 0px; margin: 0px auto; max-width: 80%; height: auto; vertical-align: middle; cursor: zoom-in;" referrerpolicy="no-referrer"></td> 
   </tr> 
  </tbody> 
 </table> 
</div>
                                        </div>
                                      
</div>
            