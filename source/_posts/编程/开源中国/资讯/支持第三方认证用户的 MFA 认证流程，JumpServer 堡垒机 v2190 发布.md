
---
title: '支持第三方认证用户的 MFA 认证流程，JumpServer 堡垒机 v2.19.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0c1bf3e7aeb3f8f95fa291e4aa013c7f2b4.png'
author: 开源中国
comments: false
date: Mon, 21 Feb 2022 13:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0c1bf3e7aeb3f8f95fa291e4aa013c7f2b4.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="344" src="https://oscimg.oschina.net/oscnet/up-0c1bf3e7aeb3f8f95fa291e4aa013c7f2b4.png" width="1084" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span>2022年2月21日，JumpServer开源堡垒机正式发布v2.19.0版本。在这一版本中，JumpServer新增支持第三方认证用户开启MFA认证流程，满足了更多用户对于账号安全性的需求。同时，支持命令过滤规则忽略大小写匹配策略，并且在Web终端页面连接资产时，新增支持自动保存上次使用的系统用户，进一步提升用户的使用体验。</span></p> 
<p style="margin-left:0; margin-right:0"><span>另外，在列表搜索方面，支持多级自定义模糊搜索。在大规模资产的场景下，用户可以通过多级自定义搜索功能，更加精确地搜索出结果。</span></p> 
<p style="margin-left:0; margin-right:0">X-Pack增强包方面，JumpServer新增支持工单申请Redis数据库应用，用户可以通过工单授权申请Redis数据库应用。同时，支持通过XRDP连接远程应用时的复制/粘贴、上传/下载（磁盘挂载）权限控制。</p> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">1. 支持第三方认证用户开启MFA认证流程</span></strong></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.19.0版本中，新增支持第三方认证用户的MFA认证流程，满足了更多用户对于账号安全性的需求。其中，第三方登录方式包括OIDC、CAS，以及SAML 2.0。</p> 
<p style="margin-left:0; margin-right:0">管理员可以在“系统设置”→ “安全设置”中，开启“第三方登录用户进行MFA认证”选项。第三方认证的用户可以通过JumpServer的“个人信息”页面，开启并绑定MFA。绑定成功，且该用户成功通过第三方登录认证后，还需要进行MFA多因子认证，才能够成功登录JumpServer系统。</p> 
<p><img alt height="1526" src="https://oscimg.oschina.net/oscnet/up-1c4fe0f5a58a6dac28f827eb6507759e715.png" width="2706" referrerpolicy="no-referrer"></p> 
<p>              ▲ 图1 在“系统设置”→“安全设置”页面启用“第三方登录用户进行MFA认证”选项</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1526" src="https://oscimg.oschina.net/oscnet/up-1eace4226726e89b9b50a12616254db820a.png" width="2706" referrerpolicy="no-referrer"></p> 
<p>                ▲ 图2 用户在“个人信息”→“基本信息”→“设置多因子认证”页面启用MFA，并进行绑定</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1528" src="https://oscimg.oschina.net/oscnet/up-42472954ae32b6e9a1d989f3e4362875fc5.png" width="2712" referrerpolicy="no-referrer"></p> 
<p>                                              ▲ 图3 使用第三方OIDC用户登录</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1526" src="https://oscimg.oschina.net/oscnet/up-7db3d59346e472a67be990204d6d6a8e6e2.png" width="2708" referrerpolicy="no-referrer"></p> 
<p><span>                              ▲ 图4 用户通过第三方认证成功后，进行MFA多因子认证</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">2. 新增命令过滤规则忽略大小写匹配策略</span></strong></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.19.0版本中，新增命令过滤规则忽略大小写匹配策略。管理员可以在“创建命令过滤器规则”页面中，勾选“忽略大小写”选项。这样一来，用户在使用高危命令时，输入大写或小写命令，都会被拦截。</p> 
<p><img alt height="1530" src="https://oscimg.oschina.net/oscnet/up-a6ef0a08b369d98aeb4329c8191044fe21c.png" width="2708" referrerpolicy="no-referrer"></p> 
<p>                         ▲ 图5 管理员在“创建命令过滤器规则”页面中勾选“忽略大小写”选项</p> 
<p style="margin-left:0; margin-right:0"><img alt height="657" src="https://oscimg.oschina.net/oscnet/up-0e4f52fc5f719abdd28b465ccf5e0c2e5e3.png" width="1075" referrerpolicy="no-referrer"></p> 
<p><span>                                    ▲ 图6 用户输入高危命令时，输入大小写都会被拦截</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c"><strong>3. Web终端连接资产时，新增自动保存上次使用的系统用户</strong></span></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.19.0版本中，支持Web终端连接资产时，自动保存上次使用的系统用户，进一步提升了用户的使用便捷性。</p> 
<p><img alt height="1524" src="https://oscimg.oschina.net/oscnet/up-6527a38eef6220ad383892781f8bad9c477.png" width="2704" referrerpolicy="no-referrer"></p> 
<p><span>                                 ▲ 图7 Web终端连接资产时，自动保存上次使用的系统用户</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">4. 支持多级自定义模糊搜索</span></strong></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.19.0版本中，在列表搜索方面，支持多级自定义模糊搜索。这样一来，在大规模资产的场景下，用户可以通过多级自定义搜索，更加精确地搜索出结果。</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1528" src="https://oscimg.oschina.net/oscnet/up-323acde9511e1db21a57a25183157d2742a.png" width="2708" referrerpolicy="no-referrer"></p> 
<p><span>                                         ▲ 图8 列表搜索支持多级自定义模糊搜索</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c"><strong>5. 支持工单申请Redis数据库应用（X-Pack增强包内）</strong></span></p> 
<p style="margin-left:0; margin-right:0">JumpServer v2.19.0版本支持工单授权申请Redis数据库应用。目前，工单申请数据库应用除了支持Oracle、MySQL、PostgreSQL、MairaDB、SQL Server以外，还支持了Redis数据库。</p> 
<p style="margin-left:0; margin-right:0">用户可以在“工单”→“申请应用授权”中，选择“Redis”数据库应用类型。工单创建完成且审批人员通过后，用户即有权限使用该Redis数据库应用。</p> 
<p><img alt height="1526" src="https://oscimg.oschina.net/oscnet/up-05c7357b146747a3b5d3f760c0fabc533d5.png" width="2704" referrerpolicy="no-referrer"></p> 
<p>                                              ▲ 图9 用户申请Redis数据库应用工单</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1526" src="https://oscimg.oschina.net/oscnet/up-bd798c075986db06896f36bfc334ef17de4.png" width="2706" referrerpolicy="no-referrer"></p> 
<p><span>                     ▲ 图10 审批人员同意工单申请后，用户有权限连接Redis数据库应用</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">6. 支持通过XRDP连接远程应用时的复制/粘贴、上传/下载（磁盘挂载）权限控制（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.19.0版本中，新增支持通过XRDP连接远程应用时的复制/粘贴、上传/下载（磁盘挂载）权限控制，即授权远程应用时，开启上传/下载（挂载磁盘）、复制/粘贴的权限。</p> 
<p style="margin-left:0; margin-right:0">复制/粘贴权限是指用户连接该远程应用时，可以从外部计算机复制信息，并且粘贴到该远程应用；或者从该远程应用复制信息，粘贴到外部计算机。通过上传/下载功能，用户只需在打开的远程应用中单击右键，在打开的菜单中选择“另存为”选项。然后在打开的文件夹中找到挂载磁盘，即可向磁盘中拖拽文件，进行上传/下载操作。</p> 
<p><img alt height="1754" src="https://oscimg.oschina.net/oscnet/up-b74063533e8b01fd6261b80921b09c91f4d.png" width="2740" referrerpolicy="no-referrer"></p> 
<p>                                                     ▲ 图11 远程应用复制/粘贴功能</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1276" src="https://oscimg.oschina.net/oscnet/up-646b1c9f040c088ebef7854bc6ff4d0860f.png" width="2118" referrerpolicy="no-referrer"></p> 
<p><span>                                    ▲ 图12 远程应用向挂载磁盘中拖拽文件，实现上传/下载功能</span></p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>优化账号备份的性能问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化会话录像回放窗口的自适应问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化用户授权树右击Kubernetes节点时，不自动展开的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化表单提交时，自动滚动到校验报错字段位置的问题。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复获取SAML 2.0协议的用户属性偶尔为空的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复测试资产可连接性失败的问题（在资产关联了多个系统用户的情况下）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复站内信功能导致Redis数据库连接数量持续增加的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>修复Syslog记录的日志不显示命令记录中远端地址的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复会话录像文件未被定时清除的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复资产账号列表数据重复的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复通过SSH连接资产时的复用问题（当资产IP修改后，不再复用已有连接）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复资产账号导出条数不准确的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复通过XRDP连接资产时，会生成用户登录日志的问题（X-Pack增强包内）。</p>
                                        </div>
                                      
</div>
            