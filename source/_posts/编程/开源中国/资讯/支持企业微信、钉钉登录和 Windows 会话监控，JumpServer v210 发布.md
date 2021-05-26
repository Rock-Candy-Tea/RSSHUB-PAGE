
---
title: '支持企业微信、钉钉登录和 Windows 会话监控，JumpServer v2.10 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d37bdef47c39c6fd2b0c516103da0e4ba0c.png'
author: 开源中国
comments: false
date: Wed, 26 May 2021 07:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d37bdef47c39c6fd2b0c516103da0e4ba0c.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><img alt height="342" src="https://oscimg.oschina.net/oscnet/up-d37bdef47c39c6fd2b0c516103da0e4ba0c.png" width="824" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">5月24日，JumpServer开源堡垒机正式发布v2.10.0版本。在该版本中，JumpServer支持用户通过企业微信、钉钉进行登录，满足了更多企业用户的实际需求。</p> 
<p style="text-align:left">这一版本的JumpServer还新增了Lion图形化连接组件，该组件主要是使用Golang和Vue.js重构了JumpServer的Guacamole组件。Lion图形化连接组件极大地优化了对系统资源的占用，增强了JumpServer对RDP/VNC协议会话的管理与控制，完善了原有的连接、终断、上传/下载、录像上传、文件上传/下载审计等功能，并且新增了Windows会话监控的功能。</p> 
<p style="text-align:left">JumpServer企业版附含的X-Pack增强包新增命令复核功能，针对风险命令，审批人可审批该命令是否可以执行。</p> 
<h2 style="text-align:left">新增功能</h2> 
<p style="text-align:left"><strong>1. 支持用户通过企业微信、钉钉登录到JumpServer</strong></p> 
<p style="text-align:left">在JumpServer v2.10.0版本中，支持用户通过企业微信、钉钉进行登录，以满足更多企业的实际需求。管理员只需在“系统设置”→“企业微信”或者“钉钉”配置好相应的信息，用户在个人信息中点击绑定企业微信或钉钉，按要求进行扫码即可绑定成功。在登录页面点击“企业微信”或“钉钉”，扫码后即可成功登录到JumpServer。</p> 
<p style="text-align:left">支持企业微信、钉钉登录和Windows会话监控，JumpServer v2.10发布<br> <img alt height="943" src="https://oscimg.oschina.net/oscnet/up-7b047fdae1428535019ac293d2e26377411.png" width="1919" referrerpolicy="no-referrer"><br> 图1 企业微信认证配置</p> 
<p style="text-align:left">支持企业微信、钉钉登录和Windows会话监控，JumpServer v2.10发布<br> <img alt height="944" src="https://oscimg.oschina.net/oscnet/up-d80b7410d6a958bede420bec3e67bfb64d2.png" width="1919" referrerpolicy="no-referrer"><br> 图2 钉钉认证配置</p> 
<p style="text-align:left">支持企业微信、钉钉登录和Windows会话监控，JumpServer v2.10发布<br> <img alt height="941" src="https://oscimg.oschina.net/oscnet/up-0749c2f83f289df2cc19fb741943820494b.png" width="1919" referrerpolicy="no-referrer"><br> 图3 在用户个人信息页面绑定企业微信或者钉钉</p> 
<p style="text-align:left">支持企业微信、钉钉登录和Windows会话监控，JumpServer v2.10发布<br> <img alt height="946" src="https://oscimg.oschina.net/oscnet/up-e9ecda08dbdad201d1ab8c150c6ab58ef75.png" width="1919" referrerpolicy="no-referrer"><br> 图4 登录JumpServer欢迎界面，点击“企业微信”或者“钉钉”扫码登录</p> 
<p style="text-align:left"><strong>2. 新增Lion图形化连接组件，支持RDP/VNC协议的会话监控</strong></p> 
<p style="text-align:left">在JumpServer v2.10.0版本中，新增Lion图形化连接组件。该组件主要是使用Golang和Vue.js重构了JumpServer的Guacamole组件。Lion图形化连接组件极大地优化了对系统资源的占用，增强了JumpServer对RDP/VNC协议会话的管理与控制，完善了原有的连接、终断、上传/下载、录像上传、文件上传/下载审计等功能，并且新增了Windows会话监控的功能。</p> 
<p style="text-align:left">支持企业微信、钉钉登录和Windows会话监控，JumpServer v2.10发布<br> <img alt height="944" src="https://oscimg.oschina.net/oscnet/up-248a9ed246be95abfa0fef6e324fd73bb2e.png" width="1919" referrerpolicy="no-referrer"><br> 图5 连接RDP/VNC资产，右侧新增快捷键、剪贴板、文件管理功能</p> 
<p style="text-align:left">支持企业微信、钉钉登录和Windows会话监控，JumpServer v2.10发布<br> <img alt height="952" src="https://oscimg.oschina.net/oscnet/up-83f1f8366db9eff4bb73f20546b891cd7a1.png" width="1919" referrerpolicy="no-referrer"><br> 图6 支持监控RDP/VNC协议会话</p> 
<p style="text-align:left"><strong>3. 新增命令复核功能（X-Pack增强包内)</strong></p> 
<p style="text-align:left">JumpServer v2.10.0版本的X-Pack增强包新增了命令复核功能。管理员选择“命令过滤”→“命令过滤规则”，即可创建一个命令过滤复核动作的规则。管理员可以根据需要设定规则，对规则类型、规则内容、审批人等信息进行设置。然后，将该命令过滤规则设置给某个系统用户，当用户使用该系统用户登录资产时，输入该规则中的命令，即会发送命令复核工单给审批人。待审批人同意后，该命令才可执行。</p> 
<p style="text-align:left">支持企业微信、钉钉登录和Windows会话监控，JumpServer v2.10发布<br> <img alt height="944" src="https://oscimg.oschina.net/oscnet/up-7b1e9c4c24d49e94a8e88010086cda7b7ac.png" width="1909" referrerpolicy="no-referrer"><br> 图7 创建命令复核规则</p> 
<p style="text-align:left">支持企业微信、钉钉登录和Windows会话监控，JumpServer v2.10发布<br> <img alt height="944" src="https://oscimg.oschina.net/oscnet/up-e7126d72aa6908e599b40a2813f0087e811.png" width="1919" referrerpolicy="no-referrer"><br> 图8 将该规则指定给某些系统用户</p> 
<p style="text-align:left">支持企业微信、钉钉登录和Windows会话监控，JumpServer v2.10发布<br> <img alt height="944" src="https://oscimg.oschina.net/oscnet/up-eb9b16a48fc4e60214a468ff9daed721a2d.png" width="1917" referrerpolicy="no-referrer"><br> 图9 系统用户执行该规则中的命令，需要等待审批人同意后，方可执行</p> 
<p style="text-align:left">支持企业微信、钉钉登录和Windows会话监控，JumpServer v2.10发布<br> <img alt height="944" src="https://oscimg.oschina.net/oscnet/up-45dde50cebfa20ea2ac7c32a84d823d7b3d.png" width="1919" referrerpolicy="no-referrer"><br> 图10 审批人同意该命令执行，则命令执行成功</p> 
<p style="text-align:left">支持企业微信、钉钉登录和Windows会话监控，JumpServer v2.10发布<br> <img alt height="946" src="https://oscimg.oschina.net/oscnet/up-db30c6eec14efafe0a9c53f174b55c66a92.png" width="1919" referrerpolicy="no-referrer"><br> 图11 审批人拒绝该命令执行，则命令执行失败</p> 
<h2 style="text-align:left"> 功能优化</h2> 
<p style="text-align:left">■ 优化过期用户可以立即退出登录；</p> 
<p style="text-align:left">■ 优化资产授权过期时在线会话自动断开；</p> 
<p style="text-align:left">■ 优化创建ElasticSearch命令存储时可设置是否忽略SSL证书；</p> 
<p style="text-align:left">■ 优化用户公钥设置功能，管理员可配置是否允许用户设置公钥；</p> 
<p style="text-align:left">■ 优化管理员可以设置用户下次登录前是否需要修改密码；</p> 
<p style="text-align:left">■ 优化授权导入功能，支持使用用户名、资产名、IP、节点路径、系统用户名称进行导入；</p> 
<p style="text-align:left">■ 优化管理员可设置历史密码不可重复次数；</p> 
<p style="text-align:left">■ 优化节点删除设计，在删除节点时可以同时删除不包含子孙资产的子孙节点。</p> 
<h2 style="text-align:left">Bug修复</h2> 
<p style="text-align:left">■ 修复创建资产时Protocols字段默认值有误的问题；</p> 
<p style="text-align:left">■ 修复创建资产不传Nodes报错的问题；</p> 
<p style="text-align:left">■ 修复上传XSLX文件中包含数字类型数据时报错的问题；</p> 
<p style="text-align:left">■ 修复上传超大文件超时问题；</p> 
<p style="text-align:left">■ 优化管理员可以设置用户下次登录前是否需要修改密码；</p> 
<p style="text-align:left">■ 修复数据库组件网关不传递密码报错的问题（X-Pack增强包内）；</p> 
<p style="text-align:left">■ 修复改密计划页面更新资产、节点报错的问题（X-Pack增强包内）；</p> 
<p style="text-align:left">■ 修复收集用户任务创建不填写周期执行报错的问题（X-Pack增强包内）。</p>
                                        </div>
                                      
</div>
            