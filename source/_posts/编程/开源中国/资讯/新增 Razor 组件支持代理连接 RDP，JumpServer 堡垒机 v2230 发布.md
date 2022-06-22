
---
title: '新增 Razor 组件支持代理连接 RDP，JumpServer 堡垒机 v2.23.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/366beb6dd8494440adbf4994a8252591?from=pc'
author: 开源中国
comments: false
date: Wed, 22 Jun 2022 06:27:00 GMT
thumbnail: 'https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/366beb6dd8494440adbf4994a8252591?from=pc'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0; text-align:start"> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <p><img alt="新增Razor组件支持代理连接RDP，JumpServer堡垒机v2.23.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/366beb6dd8494440adbf4994a8252591?from=pc" referrerpolicy="no-referrer"></p> 
   <p><span style="color:#000000">2022年6月20日，JumpServer开源堡垒机正式发布v2.23.0版本。这一版本的JumpServer在X-Pack增强包中新增了Razor组件。该组件支持代理连接RDP协议资产，替代了JumpServer原有的XRDP组件，为用户提供更加流畅的连接体验。</span></p> 
  </div> 
  <div style="margin-left:0; margin-right:0"> 
   <p><img alt="新增Razor组件支持代理连接RDP，JumpServer堡垒机v2.23.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/7718c88ec9a8457fbc621cdda78b757c?from=pc" referrerpolicy="no-referrer"></p> 
   <p><span style="color:#000000">在原有XRDP功能的基础上，Razor组件实现了单向控制上传/下载、复制/粘贴功能；外接显示屏时，Razor组件能够直接拉起RemoteApp远程应用；在连接资产或应用，以及播放录像方面体验，Razor组件所提供的连接体验更加丝滑流畅。</span></p> 
  </div> 
  <p style="margin-left:0; margin-right:0"><span style="color:#000000">在v2.23.0版本中，JumpServer还支持对数据库命令进行复核（通过CLI和Web CLI方式连接的数据库）。同时，在Web Terminal页面中，新增支持按组织显示授权资源。</span></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#000000">另外，在开源版本中，JumpServer新增支持OpenID认证设置用户属性映射字段，用户可以自定义设置用户属性字段。</span></p> 
  <h1 style="margin-left:0; margin-right:0">新增功能</h1> 
  <p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">1. 新增Razor组件支持代理连接RDP（X-Pack增强包内）</span></strong></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#000000">在JumpServer v2.23.0版本中，新增的Razor组件。该组件支持代理连接RDP协议资产，替代了JumpServer原有的XRDP组件，原生RDP连接体验全面升级。</span></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#000000">在原有XRDP组件功能的基础上，Razor组件在权限控制方面，实现了单向控制上传/下载、复制/粘贴功能；同时，外接显示屏时，可直接拉起RemoteApp远程应用，解决了旧版本因外接显示屏，无法拉起RemoteApp远程应用的问题。另外，在连接拉起资产或应用，以及播放录像等体验方面，借助Razor组件，用户能够获得更加丝滑流畅的使用体验。</span></p> 
  <div style="margin-left:0; margin-right:0">
   <img alt="新增Razor组件支持代理连接RDP，JumpServer堡垒机v2.23.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/b6714dcc5b304d1d82ea57426a6b3926?from=pc" referrerpolicy="no-referrer">
  </div> 
  <div style="margin-left:0; margin-right:0">
   <span style="color:#999999">▲ 图1 外接显示屏时，Razor组件能够直接拉起RDP客户端连接RemoteApp应用，例如MySQL WorkBench应用</span>
  </div> 
  <div style="margin-left:0; margin-right:0">
   <img alt="新增Razor组件支持代理连接RDP，JumpServer堡垒机v2.23.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/a8610f0fedfe424bb63b93ea5c8b6912?from=pc" referrerpolicy="no-referrer">
  </div> 
  <div style="margin-left:0; margin-right:0">
   <span style="color:#999999">▲ 图2 单向开启下载文件权限，Razor拉起资产或应用时，只能下载文件，无法上传文件</span>
  </div> 
  <div style="margin-left:0; margin-right:0">
    
  </div> 
  <p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">2. 支持对数据库命令进行复核（X-Pack增强包内）</span></strong></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#000000">在JumpServer v2.23.0版本中，新增支持对数据库命令进行复核（通过CLI和Web CLI方式连接的数据库）。</span></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#000000">管理员选择“资产管理”→“命令过滤”，即可创建数据库命令复核的规则，并设置审批人。授权的用户连接数据库（使用CLI或Web CLI连接方式）后，输入该命令复核规则中的命令，会提示该命令需要工单审批信息。审批人同意该工单，则该命令执行成功；反之，审批人拒绝该工单，该命令执行失败。</span></p> 
  <div style="margin-left:0; margin-right:0">
   <img alt="新增Razor组件支持代理连接RDP，JumpServer堡垒机v2.23.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/72951c5bd5d04c1a96b591f2aeb697b0?from=pc" referrerpolicy="no-referrer">
  </div> 
  <div style="margin-left:0; margin-right:0">
   <span style="color:#999999">                                  ▲ 图3 创建数据库命令复核规则</span>
  </div> 
  <div style="margin-left:0; margin-right:0">
   <img alt="新增Razor组件支持代理连接RDP，JumpServer堡垒机v2.23.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/7b36407a06a84f2cb93b120172b70341?from=pc" referrerpolicy="no-referrer">
  </div> 
  <div style="margin-left:0; margin-right:0">
   <span style="color:#999999">       ▲ 图4 用户执行命令复核规则中的命令，提示需要工单审批等信息</span>
  </div> 
  <div style="margin-left:0; margin-right:0">
   <img alt="新增Razor组件支持代理连接RDP，JumpServer堡垒机v2.23.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/ebb74079e75f4d9cb6f20d8fcf80208a?from=pc" referrerpolicy="no-referrer">
  </div> 
  <div style="margin-left:0; margin-right:0">
   <span style="color:#999999">        ▲ 图5 审批人拒绝该工单，则用户执行该命令是被禁止的</span>
  </div> 
  <p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">3. Web Terminal页面支持按组织显示授权资源（X-Pack增强包内）</span></strong></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#000000">在JumpServer v2.23.0版本中，Web Terminal页面新增支持按组织显示授权资源。当用户在多组织下都有授权资源时，在Web Terminal页面中，可切换组织获取该组织的授权资源。</span></p> 
  <div style="margin-left:0; margin-right:0">
   <img alt="新增Razor组件支持代理连接RDP，JumpServer堡垒机v2.23.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/0c21151f07fc48099c352d4b6675ce25?from=pc" referrerpolicy="no-referrer">
  </div> 
  <div style="margin-left:0; margin-right:0">
   <span style="color:#999999">   ▲ 图6 在Web Terminal页面中，可以切换组织获取该组织的授权资源</span>
  </div> 
  <p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">4. 新增支持OpenID认证设置用户属性映射字段</span></strong></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#000000">在JumpServer v2.23.0版本中，新增支持OpenID认证设置用户属性映射字段。管理员选择“系统设置”→“认证设置”→“OIDC”，即可自定义用户属性映射字段，实现将OpenID中用户属性映射到JumpServer用户上的操作。</span></p> 
  <p style="margin-left:0; margin-right:0"><em><span style="color:#000000">注：如果用户所填写的属性不存在，则会使用OpenID中用户的ID作为属性进行映射。</span></em></p> 
  <div style="margin-left:0; margin-right:0">
   <img alt="新增Razor组件支持代理连接RDP，JumpServer堡垒机v2.23.0发布" src="https://p26.toutiaoimg.com/origin/tos-cn-i-qvj2lq49k0/f537cd86f1854c5f88d6974a34eaf997?from=pc" referrerpolicy="no-referrer">
  </div> 
  <div style="margin-left:0; margin-right:0">
   <span style="color:#999999">   ▲ 图7 管理员在OIDC设置页面上，可以自定义用户属性映射字段</span>
  </div> 
  <h1 style="margin-left:0; margin-right:0">功能优化</h1> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>优化Luna页⾯访问资产显⽰Loading的动画；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>优化克隆角⾊权限时包含权限位；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> </span>增加配置项<br> <em><span>CONNECTION_TOKEN_EXPIRATION</span></em>控制连接Token的过期时间，默认⾄少5分钟；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> </span>优化RBAC模块的数据库迁移逻辑，提升升级速度；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>优化JumpServer Client版本v1.1.6，⽀持ARM架构；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> </span>优化授权规则过期通知⽂案；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> </span>优化系统⽤户、改密任务密码字段，不⽀持输⼊单双引号；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>优化命令过滤器详情页⾯，增加快速选择⽤户、⽤户组、应⽤等资源；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> </span>优化管理页⾯中技术⽀持菜单，提供“⼯具下载”链接；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> </span>优化OpenID⽤户登录时默认邮件后缀使⽤配置项；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>优化⽂件上传成功的提⽰信息（Lion组件）；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> </span>优化命令记录中⽂字符记录乱码的问题（Lion组件）；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>优化Web终端显⽰最⼤滚动⾏数，从1000行提升至5000⾏（KoKo组件）；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>优化⽀持MySQL 8.0版本数据库（Magnus组件）；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> </span>优化会话记录的登录IP地址问题，去掉记录端口号（Magnus组件）；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>优化⽀持PostgreSQL SCRAM认证（Magnus组件）（X-Pack增强包内）。</p> 
  <h1 style="margin-left:0; margin-right:0">Bug 修复</h1> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>修复⽤户重置密码地址不正确的问题；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>修复获取登录IP城市时不准确的问题；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> </span>修复公告设置内容不显⽰的问题；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>修复LDAP⽤户属性映射配置了⽤户组字段后导致⽤户登录失败的问题；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> </span>修复推送动态⽤户时Comment中包含空格导致推送失败的问题；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>修复命令列表模糊搜索时报错的问题；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>修复列表⾃定义搜索时再次返回页⾯显⽰True的问题；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>修复⽤户⾸次登录页⾯提交后，会取消第三⽅绑定账号的问题；</p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>修复OmniDB组件占⽤CPU资源过⾼的问题，有效提升用户的连接和使用性能（X-Pack增强包内）；</p> 
  <p style="margin-left:0px; margin-right:0px"><span style="color:#28937c">■</span><span> </span>修复⼿动登录的系统⽤户连接RemoteApp应⽤时获取不到认证信息导致登录失败的问题（X-Pack增强包内）。</p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            