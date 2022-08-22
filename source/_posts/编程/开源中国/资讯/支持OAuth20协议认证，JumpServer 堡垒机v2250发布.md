
---
title: '支持OAuth2.0协议认证，JumpServer 堡垒机v2.25.0发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://blog.fit2cloud.com/wp-content/uploads/2022/08/%E8%A1%A8%E6%A0%BC-1024x273.png'
author: 开源中国
comments: false
date: Mon, 22 Aug 2022 15:21:00 GMT
thumbnail: 'https://blog.fit2cloud.com/wp-content/uploads/2022/08/%E8%A1%A8%E6%A0%BC-1024x273.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://blog.fit2cloud.com/wp-content/uploads/2022/08/%E8%A1%A8%E6%A0%BC-1024x273.png" referrerpolicy="no-referrer"></p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">2022年8月22日，JumpServer开源堡垒机正式发布v2.25.0版本。在这一版本中，用户登录支持OAuth2.0协议认证方式，管理员配置OAuth2相关的认证信息，用户在登录时即可通过OAuth2认证方式进行认证登录。同时，系统设置新增系统⼯具Ping和Telnet，更方便用户检测网络的连通情况和分析网络速度。另外，客户端拉起支持Deepin（深度）国产操作系统。</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">X-Pack增强包方面，针对短信服务，JumpServer除了支持腾讯云和阿里云的短信服务外，在这一版本新增支持CMPP v2.0协议短信网关。</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">另外，在“云同步”模块中，JumpServer新增支持局域网同步。目前，JumpServe所支持的云平台除了阿里云、腾讯云、华为云、百度云、京东云、AWS（中国）、AWS（国际）、Azure（中国）、Azure（国际）、谷歌云、VMware、青云私有云、华为私有云、OpenStack、Nutanix、华为Fusion Compute以外，还支持局域网同步，满足了企业在多云资产纳管方面的实际需求，协助用户实现对私有云、公有云资产的统一纳管。</p> 
<h2 style="margin-left:.5407911001em; margin-right:auto; text-align:start">新增功能</h2> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start"><strong>1. 用户登录支持OAuth2.0协议认证方式</strong></p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">在JumpServer v2.25.0版本中，用户登录支持OAuth2.0协议认证方式。管理员可以选择“系统设置”→“认证设置”→“OAuth2”，配置相关的认证信息，并开启该认证。这样一来，用户登录页面后就可以选择OAuth2认证方式进行认证登录。</p> 
<p><img alt src="https://blog.fit2cloud.com/wp-content/uploads/2022/08/%E5%9B%BE1-2-1024x696.png" referrerpolicy="no-referrer"></p> 
<p>▲ 图1 选择“系统设置”→“认证设置”→“OAuth2”：以新浪微博为例，配置OAuth2认证</p> 
<p><img alt src="https://blog.fit2cloud.com/wp-content/uploads/2022/08/%E5%9B%BE2-3-1024x600.png" referrerpolicy="no-referrer"></p> 
<p>               ▲ 图2 登录页面：用户可以点击weibo认证进行认证登录</p> 
<p><img alt src="https://blog.fit2cloud.com/wp-content/uploads/2022/08/%E5%9B%BE3-3-1024x569.png" referrerpolicy="no-referrer"></p> 
<p>                                 ▲ 图3 用户扫描二维码进行认证登录</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start"><strong>2. 系统设置新增系统⼯具Ping和Telnet</strong></p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">在JumpServer v2.25.0版本中，系统设置新增系统⼯具Ping和Telnet。管理员选择“系统设置”→“系统工具”，即可使用Ping或者Telnet系统工具，用户能够更加方便地检测网络的连通情况和分析网络速度。</p> 
<p><img alt src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/859b943ea8b84bc5ae1b9d2ba10789bc~noop.image?_iz=58558&from=article.pc_detail&x-expires=1661755517&x-signature=Ej78AjJDtv28bHWTFSFHIhuo7B4%3D" referrerpolicy="no-referrer"></p> 
<p>                             ▲ 图4 使用Ping和Telnet检测网络的连通情况</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start"><strong>3. 客户端拉起支持Deepin（深度）国产操作系统</strong></p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">在JumpServer v2.25.0版本中，客户端拉起新增支持Deepin（深度）国产操作系统。用户使用Deepin操作系统，登录JumpServer连接资产时，选择SSH Client或RDP客户端连接方式，即可直接拉起本地相应的SSH客户端或RDP客户端。</p> 
<p><img alt src="https://blog.fit2cloud.com/wp-content/uploads/2022/08/%E5%9B%BE5-2-1024x718.png" referrerpolicy="no-referrer"></p> 
<p>                    ▲ 图5 Deepin（深度）操作系统拉起本地RDP客户端</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start"><strong>4. 短信服务支持CMPP v2.0协议（X-Pack增强包内）</strong></p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">在JumpServer v2.25.0版本中，短信服务在腾讯云和阿里云短信服务的基础上新增对CMPP v2.0协议短信网关的支持。</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">管理员在“系统设置”→”短信设置“中，选择“CMPP v2.0”选项进行配置，并且启用SMS。用户在“个人信息”页面中，开启多因子（MFA）认证，同时启用短信认证。此后，用户在登录二次认证时，即可使用该CMPP短信服务进行短信验证码认证。</p> 
<p><img alt src="https://blog.fit2cloud.com/wp-content/uploads/2022/08/%E5%9B%BE6-2-1024x640.png" referrerpolicy="no-referrer"></p> 
<p>                     ▲ 图6 CMPP v2.0短信服务配置（X-Pack增强包内）</p> 
<p><img alt src="https://blog.fit2cloud.com/wp-content/uploads/2022/08/%E5%9B%BE7-1024x428.jpeg" referrerpolicy="no-referrer"></p> 
<p>▲ 图7 用户在登录二次认证时，即可使用该CMPP短信服务进行短信验证码认证</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start"><strong>5. 云同步支持局域网同步（X-Pack增强包内）</strong></p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">在JumpServer v2.25.0版本中，在“云同步”模块新增支持局域网同步。</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">目前，JumpServe支持的云平台除了阿里云、腾讯云、华为云、百度云、京东云、AWS（中国）、AWS（国际）、Azure（中国）、Azure（国际）、谷歌云、VMware、青云私有云、华为私有云、OpenStack、Nutanix、华为Fusion Compute以外，还支持局域网同步，满足了企业在多云资产纳管方面的实际需求，协助用户实现对私有云、公有云资产的统一纳管。</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">管理员选择”资产列表“→”云同步“，创建局域网账号，并且创建局域网同步任务，即可将符合规则的局域网IP同步到JumpServer进行统一纳管。</p> 
<p><img alt src="https://blog.fit2cloud.com/wp-content/uploads/2022/08/%E5%9B%BE8-2-1024x536.png" referrerpolicy="no-referrer"></p> 
<p>                                                  ▲ 图8 创建局域网账号</p> 
<p><img alt src="https://blog.fit2cloud.com/wp-content/uploads/2022/08/%E5%9B%BE9-2-1024x674.png" referrerpolicy="no-referrer"></p> 
<p>                                            ▲ 图9 创建局域网同步任务</p> 
<h2 style="margin-left:.5407911001em; margin-right:auto; text-align:start">功能优化</h2> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ 优化配置⽂件⽀持对敏感信息进⾏加密后填写；</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ 优化资产树显⽰，⽀持搜索节点；</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ 优化⽤户登录规则，根据优先级进⾏匹配；</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ 优化第三⽅⽤户登录也验证⽤户登录规则；</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ 优化登录失败⽇志中的原因信息；</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ 通过Luna页⾯连接远程应⽤时，隐藏右侧快捷键弹窗；</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ 优化下载RDP⽂件名，解决⽂件名中包含“/”时不能正常拉起客户端的问题；</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ ⽀持PostgreSQL、MySQL数据库的预处理SQL记录并审计，取消记录Select语句的执⾏结果。</p> 
<h2 style="margin-left:.5407911001em; margin-right:auto; text-align:start">Bug修复</h2> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ 修复PostgreSQL通过KoKo连接时不⾛⽹关的问题；</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ 修复通过Xshell⼯具使⽤rz下载⽂件时后续录像没有记录的问题；</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ 修复Luna组件左侧树布局折叠展⽰和组织选择问题；</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ 修复⽤户登录每隔⼀⼩时⾃动退出的问题；</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ 修复系统平台不能导⼊的问题；</p> 
<p style="color:#686868; margin-left:auto; margin-right:auto; text-align:start">■ 修复更新资产账号密码不成功的问题（当资产账号密码结尾是“:”的情况时）。</p> 
<p> </p>
                                        </div>
                                      
</div>
            