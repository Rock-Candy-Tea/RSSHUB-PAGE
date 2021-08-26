
---
title: 'JumpServer 堡垒机 v2.13.0 发布，支持飞书认证和消息通知，新增会话录像水印功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-56aaeccaf653b57f968eb4c524fd162d09f.png'
author: 开源中国
comments: false
date: Thu, 26 Aug 2021 06:15:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-56aaeccaf653b57f968eb4c524fd162d09f.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://oscimg.oschina.net/oscnet/up-56aaeccaf653b57f968eb4c524fd162d09f.png" referrerpolicy="no-referrer"></p> 
<p>8月23日，JumpServer开源堡垒机正式发布v2.13.0版本。在这一版本中，JumpServer服务数据库（即JumpServer后台所使用的数据库）支持使用MySQL 8.0版本。用户登录认证方面，JumpServer除了支持OpenID、CAS、LDAP、Radius、企业微信和钉钉等第三方认证外，新增支持接入飞书认证；在消息订阅方面，也支持消息通知到飞书。</p> 
<p>在v2.13.0版本中，JumpServer新增支持录像会话水印功能。另外，在这一版本中，管理员可以对数据库会话进行主动终断，阻止用户继续操作数据库。X-Pack增强包方面，批量改密计划不仅支持批量修改资产用户密码，同时也支持了批量修改资产用户密钥，并在修改密钥的时候支持多种修改策略，例如追加、删除并追加和更新。</p> 
<h2>新增功能</h2> 
<p><strong>1. 支持飞书认证实现用户登录、消息通知</strong></p> 
<p>在JumpServer v2.13.0版本中，管理员可以进入“系统设置”→ “飞书”页面，输入APP ID和APP Secret，并启用飞书认证来进行配置。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-67a968cba509f654d6c3f95c0e2a9055a92.png" referrerpolicy="no-referrer"></p> 
<p>▲图1 在“系统设置”→“飞书”中开启飞书认证功能</p> 
<p>管理员将飞书认证配置完成后，用户打开登录页面，就可以看到飞书认证链接已在更多登录方式中出现，用户只需要点击“飞书”链接，扫码登录即可。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f6d4522704159bdd08fe9d08dab892d8b26.png" referrerpolicy="no-referrer"></p> 
<p>▲图2 打开登录页面，点击“飞书”链接进行授权登录认证</p> 
<p>在消息订阅方面，管理员进入“系统设置”→“系统消息订阅”页面，在“飞书”列中勾选对应的消息内容，当有新的消息发出时，已绑定飞书的用户便可以在飞书应用中直接查收消息。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cd5d78407897b0702896cee21c523b079b3.png" referrerpolicy="no-referrer"></p> 
<p>▲图3 在“系统设置”→“系统消息订阅”页面中开启飞书消息通知</p> 
<p><strong>2. 新增会话录像水印功能</strong></p> 
<p>在JumpServer v2.13.0版本中，管理员可以进入“系统设置”→“安全设置”选择开启录像会话水印功能。这样一来，用户在连接会话时，以及管理员在查看会话录像时，便可以看到相关的水印信息。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-126002525d677e39b295c493e5b4f9bbab1.png" referrerpolicy="no-referrer"></p> 
<p>▲图4 在“系统设置”→“安全设置”页面中开启录像水印功能</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f07d0f92e716393515bcbeae2a6be142220.png" referrerpolicy="no-referrer"></p> 
<p>▲图5 在Web Terminal中连接资产即可看到会话水印</p> 
<p><strong>3. 支持管理员主动终断数据库协议会话</strong></p> 
<p>在JumpServerv2.13.0版本中，管理员可以主动终断数据库协议的会话，以此来阻止用户继续操作。管理员进入在线会话列表页面点击“终断”按钮，用户在Web Terminal页面就会看到会话已被终断。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-7df7804ac08493f20f877d6e222bb96da32.png" referrerpolicy="no-referrer"></p> 
<p>▲图6 用户在Web Terminal页面看到会话已被终断</p> 
<p><strong>4. 支持通过SSH协议登录已开启MFA二次认证的资产</strong></p> 
<p>随着入侵和密码泄露事件的增多，很多企业资产已经安装并加入了MFA二次认证机制。在JumpServer v2.13.0版本中，支持通过SSH协议登录已开启MFA二次认证的资产。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9a1f5ed58e75994afb1025f79092279bbbc.png" referrerpolicy="no-referrer"></p> 
<p>▲图7 资产开启MFA二次认证后，登录资产时会提示用户输入验证码</p> 
<p><strong>5. 批量改密支持批量修改资产密钥（X-Pack增强包内）</strong></p> 
<p>在JumpServer v2.13.0版本中，支持批量修改资产密钥。密钥策略方面，支持密钥追加、清空所有密钥再追加新密钥、清空当前账号密钥再追加新密钥，尽可能地满足不同用户对于资产密钥的管理方案。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-125149651d560ec809757192cba6ccba043.png" referrerpolicy="no-referrer"></p> 
<p>▲图8 创建改密任务，管理员可以同时设置修改密码、密钥</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-2b1a59b7fa8bc9c11788a96bf18f96f0c28.png" referrerpolicy="no-referrer"></p> 
<p>▲图9 改密任务执行日志</p> 
<h2>功能优化</h2> 
<p>■ 支持对rz、sz命令上传/下载文件的控制和日志审计功能；</p> 
<p>■ 支持云管中心同步任务设置同步IP网段和协议组；</p> 
<p>■ 支持云管中心同步任务设置Unix特权用户和Windows特权用户；</p> 
<p>■ 支持MariaDB数据库连接（命令行方式）；</p> 
<p>■ 将Core、Celery纳入终端列表、系统监控；</p> 
<p>■ 支持通过拉起本地客户端建立XRDP会话（X-Pack增强包内）；</p> 
<p>■ 改密任务执行支持显示触发字段，包含手动触发和定时触发（X-Pack增强包内）。</p> 
<h2>Bug修复</h2> 
<p>■ 修复/api/docs/访问异常的问题；</p> 
<p>■ 修复es命令存储搜索不准确的问题；</p> 
<p>■ 修复配置消息订阅时所选用户为当前组织用户的问题；</p> 
<p>■ 修复微信、钉钉多次测试报错的问题；</p> 
<p>■ 修复收集Windows资产用户时未收集到全部用户的问题（X-Pack增强包内）；</p> 
<p>■ 修复通过OmniDB连接包含“-”字符的数据库时失败的问题（X-Pack增强包内）；</p> 
<p>■ 修复云管中心同步资产时重复创建的问题（X-Pack增强包内）。</p>
                                        </div>
                                      
</div>
            