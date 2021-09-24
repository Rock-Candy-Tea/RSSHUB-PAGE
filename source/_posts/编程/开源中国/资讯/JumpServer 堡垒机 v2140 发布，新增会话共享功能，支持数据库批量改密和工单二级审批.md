
---
title: 'JumpServer 堡垒机 v2.14.0 发布，新增会话共享功能，支持数据库批量改密和工单二级审批'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c59b656180f27f3475ca0a4ac7cb9423adf.png'
author: 开源中国
comments: false
date: Fri, 24 Sep 2021 14:37:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c59b656180f27f3475ca0a4ac7cb9423adf.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="324" src="https://oscimg.oschina.net/oscnet/up-c59b656180f27f3475ca0a4ac7cb9423adf.png" width="1012" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>9月22日，JumpServer开源堡垒机正式发布v2.14.0版本。在该版本中，JumpServer新增了会话共享功能，支持多用户进行协同操作，以满足运维人员在不同场景中的运维需求，同时对加入会话的用户活动进行记录。需要注意的是，JumpServer目前仅支持通过Web Terminal连接的SSH/Telnet协议会话进行共享，另外，还支持用户在Web Terminal中设置终端主题。在用户个人信息页面中，用户可以针对JumpServer内部的消息选择性地开启消息接受方式，例如企业微信、钉钉等。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>X-Pack增强包方面，改密计划不仅支持对资产进行批量改密，同时也支持对数据库应用进行批量改密，满足用户对数据库密码的相关安全策略要求。目前已支持的数据库类型包括：MySQL、Oracle、PostgreSQL和MariaDB。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>在v2.14.0版本中，JumpServer新增工单系统二级审批功能，管理员可以针对不同类型的工单设置一级或二级审批流程。</span><span>在新版本中，MFA多因子认证方式不仅支持基于时间的一次性算法（即TOTP）认证，同时也支持通过短信（SMS）验证码的方式进行认证。另外，在这一版本中，云管中心支持对Google Cloud Platform（谷歌云）的资产进行同步。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">新增功能</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c"><strong><span>1. Web Terminal支持会话共享和多用户协同操作</span></strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>在JumpServer v2.14.0版本中，用户通过Web Terminal连接SSH/Telnet资产成功后，可以在页面中创建分享链接，并将分享链接和验证码发送给其他用户。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-a4575e59e8ec77ffc7c04d5a2e1cf9c8584.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图1 在Web Terminal中成功连接资产后，点击创建共享链接</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2076" src="https://oscimg.oschina.net/oscnet/up-3b127d91a4afe3f93983ce1eba6969cb726.png" width="3576" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图2 复制分享链接</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>其他用户访问链接并输入验证码，验证通过后即可加入到同一会话中，并进行操作。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2078" src="https://oscimg.oschina.net/oscnet/up-7584e607c94b7762dbaecd38b5e82a15883.png" width="3578" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图3 用户访问链接并输入验证码</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>加入成功后，用户可以在Web Terminal会话页面看到所有会话中的在线用户。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2078" src="https://oscimg.oschina.net/oscnet/up-3ea4212572e2c002aca112c14436e678bdc.png" width="3582" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图4 在会话页面中查看在线用户</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>对于共享会话加入者的活动记录，管理员可以进入“会话管理”菜单中的“活动”页面进行查看，并开展相关的审计操作。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2080" src="https://oscimg.oschina.net/oscnet/up-448a2fca08da8e05631f115b6840991c38a.png" width="3576" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图5 在“会话管理”菜单中点击“活动”页面，对共享会话加入者的活动记录进行审计</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c"><strong><span>2. Web Terminal支持用户自定义主题方案</span></strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>在JumpServer v2.14.0版本中，用户通过Web Terminal连接SSH/Telnet资产成功后，可以在页面中点击“设置”图标修改终端主题风格，从而提升用户的使用体验。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2080" src="https://oscimg.oschina.net/oscnet/up-6d3a622c455fe71c025d5acbcf3c2aaff68.png" width="3578" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图6 在会话页面中设置终端主题</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c"><strong><span>3. 改密计划支持对数据库应用进行批量改密（X-Pack增强包内）</span></strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>在JumpServer v2.14.0版本中，改密计划不仅可以对资产进行批量改密，同时也支持对数据库应用进行批量改密。目前已经支持的数据库类型包括MySQL、Oracle、PostgreSQL和MariaDB，创建应用改密计划时提供了三种密码策略供管理员进行选择。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2080" src="https://oscimg.oschina.net/oscnet/up-e0984c8f1985c5349b488736a9f8497a433.png" width="3582" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图7 创建应用改密计划</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>改密计划创建成功后，管理员可以查看所有应用改密计划、执行列表和改密任务。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2076" src="https://oscimg.oschina.net/oscnet/up-8ea79aff3df44ef5c9670d46b36c6dfa93f.png" width="3574" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图8 应用改密计划列表</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2078" src="https://oscimg.oschina.net/oscnet/up-6d78c86276d62089383571f5974c7806c44.png" width="3578" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图9 应用改密计划执行列表</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2076" src="https://oscimg.oschina.net/oscnet/up-fbbe75560c8dfa70911f23b280152def753.png" width="3576" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图10 应用改密任务列表</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#28937c">4.<span> </span></span></strong><span style="color:#28937c"><strong>工单系统支持设置一级、二级审批流程（X-Pack增强包内）</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>在JumpServer v2.14.0版本中，工单系统支持一级、二级审批流程，管理员可以针对不同的工单类型进行单独设置。而审批流程中的每一级都有四种审批人策略供管理员选择，其中包括超级管理员、组织管理员、超级管理员+组织管理员，以及自定义用户。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2078" src="https://oscimg.oschina.net/oscnet/up-41a64786ab12e48c53a2d866679a359003e.png" width="3582" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图11 设置申请资产工单的审批流程</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>用户创建申请资产工单。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2080" src="https://oscimg.oschina.net/oscnet/up-b011692073332110fd8434ccaff828eb7bf.png" width="3582" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图12 创建申请资产工单</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>工单创建成功后会自动流转至一级审批，这时所有的一级审批人员均可对工单进行审批操作。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2078" src="https://oscimg.oschina.net/oscnet/up-afdb1cb946aa77bf1fb37676671bfe8fc2f.png" width="3578" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图13 一级审批人审批工单</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>一级审批人审批工单通过后，会自动流转到下一级审批流程中。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1766" src="https://oscimg.oschina.net/oscnet/up-9c7f00dd59d8ceb952b3ce38c4c3ebd64f3.png" width="2400" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图14 二级审批人审批工单</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c"><strong><span>5. MFA多因子支持通过短信（SMS）验证码方式进行二次认证（X-Pack增强包内）</span></strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>在JumpServer v2.14.0版本中，用户登录支持通过短信验证码的方式进行MFA二次认证。首先，管理员需要在“系统设置”→“信息”中配置并开启短信服务，目前支持阿里云、腾讯云的短信服务平台。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2076" src="https://oscimg.oschina.net/oscnet/up-eed79702db35e713d544830cd3fd83d5e76.png" width="3574" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图15 管理员在“系统设置”→“信息”中配置短信服务</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>开启MFA认证的用户在登录JumpServer时可以选择短信验证码作为二次认证方式。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2078" src="https://oscimg.oschina.net/oscnet/up-30214fb1d9d0f9393cebc7cc015e78fcc1e.png" width="3580" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图16 用户登录选择短信验证码进行二次认证</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c"><strong><span>6. 云管中心支持对Google Cloud Platform（谷歌云）的资产进行同步（X-Pack增强包内）</span></strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>在JumpServer v2.14.0版本中，已支持对Google Cloud Platform（谷歌云）资产的同步功能。管理员在创建谷歌云账号时，需要上传一个Service Accounts Key文件（仅支持JSON格式）。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="2076" src="https://oscimg.oschina.net/oscnet/up-52e9177ffa991e0c43a07a0cecef277f375.png" width="3578" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图17 创建谷歌云账号</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>账号创建完成后，管理员创建同步实例任务，执行方式支持定时、定期执行和手动执行。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="1692" src="https://oscimg.oschina.net/oscnet/up-c54be9be870cef7cb2bad78e02b92b0496e.png" width="2990" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>▲图18 创建谷歌云同步任务</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">功能优化</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>针对项目配置参数，管理员可以直接在系统设置中进行修改，修改完成后立即生效，不再需要修改配置文件和重启服务；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>支持Windows会话在移动端进行操作，同时增加快捷键“Shift+Alt+Ctrl”来快速呼出右侧栏；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>对于第三方认证的用户，在登录JumpServer时支持进行MFA二次认证。同时也支持使用企业微信、钉钉进行扫码登录；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>在授权列表中显示资产/应用授权规则的创建方式，例如手动创建、工单创建，以便管理员对授权进行区分和快速查找；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>创建资产授权规则，当授权动作选择上传、下载、复制、粘贴中的任意一项或几项时，由于连接动作是前置条件，所以禁止用户取消；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>修改新注册终端的名称（包含宿主机的主机名标识），以便管理员在多节点部署架构中区分终端所属节点；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>连接Windows会话时，在用户名、密码以及连接方式的对话框中增加“下次自动登录”选项来记住用户的连接方式。当用户连接资产时不需要每次都进行选择，从而提高用户的使用体验；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>增加配置项来开启或关闭Windows会话的XRDP连接方式（X-Pack增强包内）；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>支持对通过XRDP方式连接的Windows会话进行全屏操作和本地磁盘挂载（X-Pack增强包内）；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>增加JumpServerClient和MicrosoftRemoteDesktop应用下载页面，便于纯内网环境的用户使用XRDP方式连接Windows（X-Pack增强包内）。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Bug修复</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>修复应用账号不能通过用户名进行过滤的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>修复WebSocket服务引起的Redis连接数量持续增加的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>修复删除已关联资产的特权用户偶尔失败的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>修复当资产和特权用户关系发生变化时，资产特权用户未及时更新的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■<span> </span></span><span>修复当部署服务器的磁盘、内存达到阈值时，偶尔未发送告警消息的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>修复当设置未分组节点下显示单独授权的资产配置项时，用户授权树未及时更新的问题；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>修复批量更新组织失败的问题（X-Pack增强包内）；</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#28937c">■</span><span><span> </span>修复终断通过XRDP方式连接的Windows会话偶尔失败的问题（X-Pack增强包内）。</span></p>
                                        </div>
                                      
</div>
            