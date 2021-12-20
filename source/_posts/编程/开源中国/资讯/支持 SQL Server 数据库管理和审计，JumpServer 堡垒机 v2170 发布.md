
---
title: '支持 SQL Server 数据库管理和审计，JumpServer 堡垒机 v2.17.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-12f4ff168992e38c258f56e0245afb6bb75.png'
author: 开源中国
comments: false
date: Mon, 20 Dec 2021 12:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-12f4ff168992e38c258f56e0245afb6bb75.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="358" src="https://oscimg.oschina.net/oscnet/up-12f4ff168992e38c258f56e0245afb6bb75.png" width="1276" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">12月20日，JumpServer开源堡垒机正式发布v2.17.0版本。在这一版本中，JumpServer支持基于SAML 2.0的联合身份验证，支持对Windows资产的键盘操作进行记录和审计，同时用户可以通过键盘操作快速定位Windows资产会话录像，并且支持对数据库操作的SQL语句进行过滤。</p> 
<p style="margin-left:0; margin-right:0">X-Pack增强包方面，JumpServer新增对微软SQL Server数据库的管理、连接、操作和审计功能，支持将改密计划执行结果用邮件的方式发送给指定接收人，支持通过XRDP方式连接Windows远程应用。另外，云管中心新增OpenStack私有云资产同步，同时支持对通过Web GUI方式连接的数据库进行SQL指令补全和过滤。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0; margin-right:0"><strong>1. 支持基于SAML 2.0的联合身份验证以实现单点登录</strong></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#3e3e3e">在JumpServer v2.17.0版本中，用户登录已支持基于SAML 2.0的联合身份验证。SAML 2.0 （安全断言标记语言2.0）是许多身份验证提供商（Identity Provider，简称为IdP）使用的一种开放标准，使身份提供商可以实现联合单点登录（Federated Single Sign-on），管理员可以授权经过联合身份验证通过的用户登录JumpServer的管理系统或用户系统。目前JumpServer已支持的用户登录认证方式包括但不限于CAS、OpenID、SAML 2.0、AD/LDAP、RADIUS、企业微信、钉钉和飞书。</span></p> 
<p><img alt height="896" src="https://oscimg.oschina.net/oscnet/up-9c309036f43d176343d90eff2e75b2168a6.png" width="1484" referrerpolicy="no-referrer"></p> 
<p>                                              ▲图1 JumpServer的用户登录页面</p> 
<p><img alt height="1068" src="https://oscimg.oschina.net/oscnet/up-f893f9a09a9869c14c10b26ffba3da9523d.png" width="1712" referrerpolicy="no-referrer"></p> 
<p><span>                                              ▲图2 SAML 2.0认证配置页面</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">2. 支持对数据库操作的SQL语句进行阻断（仅支持允许、拒绝操作，暂不支持复核）</span></strong></p> 
<p style="margin-left:0; margin-right:0">敏感SQL命令的阻断与拦截是安全审计的重要特性。这可以有效避免团队成员的违规操作、敏感操作、误操作等行为，避免为企业带来不必要的损失。在JumpServer v2.17.0版本中，管理员可以通过创建命令过滤器，并与命令过滤规则、用户、普通系统用户和数据库应用等进行关联，定义SQL命令过滤规则。这样一来，用户无论是通过CLI、Web CLI，还是Web GUI方式连接的数据库，都可以被实时阻断。</p> 
<p><img alt height="954" src="https://oscimg.oschina.net/oscnet/up-3b28416eb8ddf2f5a2cda78c60a7a43fd9f.png" width="1250" referrerpolicy="no-referrer"></p> 
<p>                      ▲图3 通过Web CLI方式连接数据库，执行SQL命令被阻断</p> 
<p style="margin-left:0; margin-right:0"><img alt height="955" src="https://oscimg.oschina.net/oscnet/up-5b03801b463827cce9077905417b75c59e5.png" width="1247" referrerpolicy="no-referrer"></p> 
<p><span>                             ▲图4 通过Web GUI方式连接数据库，执行SQL命令被阻断</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">3. 支持对Windows资产的键盘操作进行记录和审计（仅支持Web连接的方式）</span></strong></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.17.0版本中，对于通过Web方式连接的Windows资产，支持对用户的键盘操作进行记录和审计。同时，当管理员查看录像回放时，可以选择从某个键盘操作记录的指定位置开始回放。</p> 
<p><img alt height="957" src="https://oscimg.oschina.net/oscnet/up-0293ec80666e66991682c931dd5cd33ab33.png" width="1321" referrerpolicy="no-referrer"></p> 
<p>                                             ▲图5 通过Web方式连接Windows资产</p> 
<p style="margin-left:0; margin-right:0"><img alt height="926" src="https://oscimg.oschina.net/oscnet/up-6fadbe62e7401a46fac1d7a34fdb9420624.png" width="1333" referrerpolicy="no-referrer"></p> 
<p><span>                                     ▲图6 录像回放页面左侧显示键盘操作记录列表</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">4. 支持对SQL Server数据库进行管理、连接、操作和审计（仅支持CLI和Web CLI方式连接）（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0">Microsoft SQL Server是由美国微软公司推出的一种关系数据库解决方案，最新的版本为SQL Server 2019。根据DB-Engines对数据库管理系统的流行程度排名，SQL Server的市场份额排名第三。为了满足更多企业对于数据库多样化的管理需求，JumpServer在v2.17.0版本中，新增了对SQL Server数据库的管理、连接、操作和审计功能。</p> 
<p><img alt height="957" src="https://oscimg.oschina.net/oscnet/up-f988495448ff7afd392f0050accdac9e48a.png" width="1494" referrerpolicy="no-referrer"></p> 
<p>                             ▲图7 在JumpServer管理页面创建SQL Server数据库应用</p> 
<p style="margin-left:0; margin-right:0"><img alt height="958" src="https://oscimg.oschina.net/oscnet/up-b699015152048e619996505b25e7c10a3db.png" width="1495" referrerpolicy="no-referrer"></p> 
<p><span>                                            ▲图8 在Web UI页面连接SQL Server数据库</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">5. 支持通过XRDP方式连接Windows远程应用（需要使用最新的Jmservisor脚本）（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.17.0版本中，用户连接远程应用时可以选择通过Web GUI或者本地RDP客户端的方式进行连接。下图是一个通过RDP客户端（Remote Desktop Client）连接Windows远程应用Chrome浏览器，并打开JumpServer官方文档页面的示例。</p> 
<p><img alt height="1007" src="https://oscimg.oschina.net/oscnet/up-8d2cceb27103a4a58ef376c304c8c120826.png" width="1430" referrerpolicy="no-referrer"></p> 
<p><span>                               ▲图9 通过RDP连接Windows远程应用Chrome浏览器</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#279a81">6. 支持对OpenStack私有云资产进行同步（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.17.0版本中，云管中心支持对OpenStack私有云资产进行同步。目前，JumpServer支持的公有云、私有云资产同步对象包括阿里云、腾讯云、华为云、AWS（中国区域、国际）、Azure（中国区域、国际）、谷歌云、VMware、青云私有云、华为私有云、Nutanix和OpenStack等。</p> 
<p><img alt height="957" src="https://oscimg.oschina.net/oscnet/up-afd4352ba92f2c1b8a080ee5b3253a635e4.png" width="1496" referrerpolicy="no-referrer"></p> 
<p><span>                                                     ▲图10 创建OpenStack云管账号</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">7. 支持对通过Web GUI方式连接的数据库进行SQL补全（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.17.0版本中，对通过Web GUI方式连接的数据库应用，用户可以在操作页面中开启或关闭SQL语句命令补全功能（默认开启）。</p> 
<p><img alt height="958" src="https://oscimg.oschina.net/oscnet/up-28c764e102ee0e6cbf2434a802b491ba280.png" width="1495" referrerpolicy="no-referrer"></p> 
<p><span>                         ▲图11 通过Web GUI连接数据库并输入SQL语句，自动提示完整命令</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">8. 支持将改密计划执行结果发送给指定接收人（仅支持邮件方式）（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.17.0版本中，管理员创建改密计划时可以指定收件人。当改密计划执行完成后，系统会将本次改密计划的资产账号信息以加密文件的方式通过邮件发送给收件人。需要注意的是，为了确保资产账号信息的安全性，防止在传输过程中出现信息泄漏的问题，只有在个人信息页面配置了文件加密密码的用户才能够收到改密后的资产账号信息文件。</p> 
<p><img alt height="958" src="https://oscimg.oschina.net/oscnet/up-5b19acdf827ca0c999b48f04aa97fdf1ca5.png" width="1495" referrerpolicy="no-referrer"></p> 
<p>                                                   ▲图12 创建改密计划指定收件人</p> 
<p style="margin-left:0; margin-right:0"><img alt height="960" src="https://oscimg.oschina.net/oscnet/up-baaeb7f969c2775a0048b4c9cb756fbd115.png" width="1495" referrerpolicy="no-referrer"></p> 
<p><span>                                           ▲图13 在个人信息页面中配置文件加密密码</span></p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> </span>支持对命令过滤器进行多维度绑定；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>优化服务启动脚本的执行速度；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化终端性能指标对内存使用率兼容Docker Limit的设置；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>优化消息通知类型，支持Markdown格式；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化站内信文案和显示遮挡的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化JSON输入框，支持一键格式化；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> </span>优化申请资产工单，可以指定节点（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 移除远程应用右侧快捷键菜单栏（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化创建申请资产、应用工单时默认选中当前组织（X-Pack增强包内）。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span><span> </span>修复数据库连接未关闭的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复在Redis集群环境下使用Redis锁机制报错的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>修复openSUSE系统su切换用户失败的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复根据节点、资产查询授权时报错的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复用户使用CAS、OpenID登录时的跳转问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复根据资产IP查询资产显示不全的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复会话详情页命令列表排序功能失效的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复获取应用类型时系统用户认证信息失败的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>修复青云私有云同步资产网段地址固定的问题（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复将应用从某个授权中移除时会从所有授权中移除的问题（X-Pack增强包内）。</p>
                                        </div>
                                      
</div>
            