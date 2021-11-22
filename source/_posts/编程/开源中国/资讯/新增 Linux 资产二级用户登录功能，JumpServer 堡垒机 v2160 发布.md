
---
title: '新增 Linux 资产二级用户登录功能，JumpServer 堡垒机 v2.16.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-550bf9a0d327d245bfd0cad4aa27217f22d.png'
author: 开源中国
comments: false
date: Mon, 22 Nov 2021 17:04:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-550bf9a0d327d245bfd0cad4aa27217f22d.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt height="334" src="https://oscimg.oschina.net/oscnet/up-550bf9a0d327d245bfd0cad4aa27217f22d.png" width="922" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0">11 月 22 日，JumpServer 开源堡垒机正式发布 v2.16.0 版本。这一版本有如下改动：</p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;">JumpServer 新增 Linux 资产二级用户登录功能，支持用户登录资产后自动切换为其他用户；</li> 
 <li style="margin-left: 0px; margin-right: 0px;">该版本还支持将资产连接过程中产生的会话录像存储在华为云对象存储服务 OBS 中；</li> 
 <li style="margin-left: 0px; margin-right: 0px;">用户登录方面，支持管理员开启或关闭异地登录保护功能。</li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>X-Pack 增强包方面，支持管理员自定义配置导航栏中的文档、技术支持链接地址。</span></li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px">新增功能</h2> 
<p style="margin-left:0px; margin-right:0px"><span style="color:#28937c"><strong>1. 新增Linux资产二级用户登录功能</strong></span></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.16.0版本中，新增Linux资产二级用户登录功能。管理员在创建、更新系统用户时启用“用户切换”选项，并指定“切换自”系统用户（仅支持配置自动登录SSH协议系统用户）。这样一来，用户在登录资产时，会首先使用“切换自”系统用户登录资产，登录成功后会自动切换至当前系统用户。同时，管理员可以在“系统用户详情”标签中的“Su用户”页面查看当前系统用户支持切换到的所有系统用户。</p> 
<p><img alt height="1359" src="https://oscimg.oschina.net/oscnet/up-05d1d5f4b10ea952c9d87a17375d2216624.png" width="2558" referrerpolicy="no-referrer"></p> 
<p><span>                                  ▲图1 在“系统用户”页面中指定“切换自”系统用户</span></p> 
<p style="margin-left:0; margin-right:0"><img alt height="1360" src="https://oscimg.oschina.net/oscnet/up-6ad97f97f237fc0c441ea70cab2f1110fce.png" width="2558" referrerpolicy="no-referrer"></p> 
<p><span>               ▲图2 在“系统用户详情”→“Su用户”页面中查看可以切换到的所有系统用户</span></p> 
<p style="margin-left:0px; margin-right:0px"><span><strong><span style="color:#28937c">2. 会话录像支持存储在华为云OBS</span></strong></span></p> 
<p style="margin-left:0; margin-right:0"><span>在JumpServer v2.16.0版本中，会话录像存储支持配置并使用华为云对象存储服务OBS。目前，JumpServer已支持的存储服务包括AWS S3、Ceph、Swift、阿里云OSS、Azure和华为云OBS。</span></p> 
<p><img alt height="1360" src="https://oscimg.oschina.net/oscnet/up-363dad5fc63f532fb80e1232d832252a13c.png" width="2558" referrerpolicy="no-referrer"></p> 
<p>                                ▲图3 在“会话管理”→“存储配置”中选择“OBS”选项</p> 
<p style="margin-left:0; margin-right:0"><img alt height="1360" src="https://oscimg.oschina.net/oscnet/up-3f1839ed521ef5cb837ec5dcdac409bf2f5.png" width="2558" referrerpolicy="no-referrer"></p> 
<p><span>                                               ▲图4 创建华为云OBS录像存储</span></p> 
<p style="margin-left:0px; margin-right:0px"><img alt height="1360" src="https://oscimg.oschina.net/oscnet/up-64787332e7be1e279498d576dabf9719c7a.png" width="2557" referrerpolicy="no-referrer"></p> 
<p><span>                                                     ▲图5 更新终端录像存储</span></p> 
<p><strong><span style="color:#28937c">3. 支持管理员开启或关闭异地登录保护功能</span></strong></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.16.0版本中，管理员可以自定义开启或关闭异地登录保护功能，满足了用户在不同场景下对于账号安全性的需求。</p> 
<p><img alt height="1360" src="https://oscimg.oschina.net/oscnet/up-5727e0932f53db7437219413d6ebd71ee19.png" width="2557" referrerpolicy="no-referrer"></p> 
<p><span>                    ▲图6 在“系统设置”→“安全设置”中开启或关闭异地登录保护功能</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#28937c">4. 支持自定义配置导航栏中的文档、技术支持链接地址（X-Pack增强包内）</span></strong></p> 
<p style="margin-left:0; margin-right:0">在JumpServer v2.16.0版本中，管理员可以自定义配置导航栏中的文档、技术支持链接地址。</p> 
<p><img alt height="1360" src="https://oscimg.oschina.net/oscnet/up-5c77167d8e5f9a33773f7a514e20bf8fdb1.png" width="2558" referrerpolicy="no-referrer"></p> 
<p><span>                      ▲图7 在“系统设置”→“其他设置”中配置文档、技术支持链接地址</span></p> 
<h2 style="margin-left:0px; margin-right:0px">功能优化</h2> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>优化MFA认证、绑定流程；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>优化支持管理员手动修改资产硬件信息；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化登录页面MFA认证失败的错误提示信息；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>移动“会话设置保留时间”至“定期清理设置”页面；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 新增ESC和F11快捷键，通过Web Terminal连接Windows资产时进行使用；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 新增内置资产平台列表Windows-RDP、Windows-TLS，并设置Windows2016为外置平台；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化异地登录提醒不再对局域网地址进行检测；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化重置公钥成功的消息格式；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>优化创建用户邮件信息，支持部分标签定义；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化终端列表指标数值保留至一位小数；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>优化通过rz命令下载多文件时的显示问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化更新页面密码输入框的风格；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 优化数据库改密支持MySQL v5.6版本，Oracle密码支持设置特殊字符（X-Pack增强包内）。</p> 
<h2 style="margin-left:0px; margin-right:0px">Bug修复</h2> 
<p style="margin-left:0px; margin-right:0px"><span style="color:#28937c">■</span> 修复执行Ansible任务的日志输出中包含非UTF-8字符报错的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复开启使用RADIUS OTP配置后，用户登录没有跳转至MFA认证页面的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>修复终端删除后录像存储不能删除的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复LDAP设置多个OU（组织单元）时，包含空白字符测试连接会失败的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复因光标移动造成命令拦截失败的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复应用授权详情中用户组不能删除的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复首次打开管理页面获取不到默认语言的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复数据库连接没有关闭的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复创建、更新表单下拉列表选项较多导致文字溢出的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复进行MFA登录验证时没有自动选中输入框的问题；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■ </span>修复工单流程更新后不生效的问题（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复数据库改密成功后无法连接的问题（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■</span> 修复通过XRDP连接资产时网关限制只能使用22端口的问题（X-Pack增强包内）；</p> 
<p style="margin-left:0; margin-right:0"><span style="color:#28937c">■<span> </span></span>修复通过XRDP连接Windows资产时偶尔报错的问题（X-Pack增强包内）。</p>
                                        </div>
                                      
</div>
            