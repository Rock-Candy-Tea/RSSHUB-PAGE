
---
title: '支持通过 VS Code 直连 Linux-SSH 协议资产，JumpServer v2.11.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p1-tt.byteimg.com/origin/pgc-image/4fe53837c1c545ebb6d6f97a22be10dd?from=pc'
author: 开源中国
comments: false
date: Tue, 22 Jun 2021 11:45:00 GMT
thumbnail: 'https://p1-tt.byteimg.com/origin/pgc-image/4fe53837c1c545ebb6d6f97a22be10dd?from=pc'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="text-align:left"> 
 <p>6月21日，JumpServer开源堡垒机正式发布v2.11.0版本。在该版本中，JumpServer新增站内信功能，可接收危险命令告警、监控告警等信息。同时，该版本还支持通过SSH工具直连资产，以及通过VS Code（即Visual Studio Code）的Remote-SSH插件直连JumpServer所纳管的Linux-SSH协议资产，从而进行远程开发。</p> 
 <p>X-Pack增强包功能方面，JumpServer新增XRDP组件，支持用户通过本地客户端直连RDP资产，建立图形会话界面。为了满足更多企业用户实际需求，我们还新增了账号管理，主要包括资产账号、应用账号、收集用户、以及改密计划等功能，以方便账号集中统一纳管。</p> 
 <h1>新增功能</h1> 
 <p><strong><span style="color:#28937c">1. 新增站内信功能</span></strong></p> 
 <p>在JumpServer v2.11.0版本中，新增站内信功能，支持订阅查看内部消息提示。目前JumpServer支持四种消息接收方式，即邮件、企业微信、钉钉和站内信。支持设置接收消息类型包括：危险命令告警以及监控告警。</p> 
 <p>管理员可点击“系统设置”→“系统消息订阅”，勾选具体的接收消息方式，并且设置消息接收人。如果危险命令告警勾选了全部消息接收方式，当用户执行了高危命令，接收人即可通过邮件、企业微信、钉钉、站内信方式收到告警信息。</p> 
 <div>
  <img alt="支持通过VS Code直连Linux-SSH协议资产，JumpServer v2.11.0发布" src="https://p1-tt.byteimg.com/origin/pgc-image/4fe53837c1c545ebb6d6f97a22be10dd?from=pc" referrerpolicy="no-referrer"> 
  <p style="text-align:center">图1 通过选择“系统设置”→“系统消息订阅”，设置消息接收方式和接收人</p> 
 </div> 
 <div>
  <img alt="支持通过VS Code直连Linux-SSH协议资产，JumpServer v2.11.0发布" src="https://p1-tt.byteimg.com/origin/pgc-image/7aad7364b9f545fbb5f5e070df42bbce?from=pc" referrerpolicy="no-referrer"> 
  <p style="text-align:center">图2 接收人在JumpServer界面右上角点击“站内信”图标，即可展示所收到的未读站内信</p> 
 </div> 
 <div>
  <img alt="支持通过VS Code直连Linux-SSH协议资产，JumpServer v2.11.0发布" src="https://p1-tt.byteimg.com/origin/pgc-image/da4968c0bfe24532a3d9a3743f0c6437?from=pc" referrerpolicy="no-referrer"> 
  <p style="text-align:center">图3 接收人可在企业微信接收到告警信息</p> 
 </div> 
 <p><strong><span style="color:#28937c">2. 支持通过SSH工具直连资产</span></strong></p> 
 <p>在JumpServer v2.11.0版本中，支持通过SSH工具直连资产。使用命令格式：s<em>sh jumpserverUsername@systemUsername@AssetIP@jumpserverHostIP -p2222</em>，如果能匹配到唯一资产、唯一系统用户名，则可直接登录该资产。如匹配到多个同IP资产，则用户可自主选择资产以及系统用户进行登录。</p> 
 <div>
  <img alt="支持通过VS Code直连Linux-SSH协议资产，JumpServer v2.11.0发布" src="https://p3-tt.byteimg.com/origin/pgc-image/aeb72e40dc064f41992a11c5c06f953d?from=pc" referrerpolicy="no-referrer"> 
  <p style="text-align:center">图4 通过SSH特殊命令格式，指定系统用户直连资产</p> 
 </div> 
 <p><strong><span style="color:#28937c">3. 支持通过VS Code的Remote-SSH插件直连JumpServer所纳管的Linux-SSH协议资产</span></strong></p> 
 <p>在JumpServer v2.11.0版本中，支持通过VS Code（即Visual Studio Code）的Remote-SSH插件直连JumpServer所纳管的Linux-SSH协议资产，从而进行远程开发。用户需要在VS Code插件库下载Remote-SSH。下载成功后，点击远程SSH连接工具，选择“Connect to Host”→“Add New SSH Host”。</p> 
 <p>输入命令格式：<em>ssh jumpserverUsername@systemUsername@AssetIP@jumpserverHostIP -p2222</em>，根据提示，可使用指定的系统用户连接指定的资产（即JumpServer所纳管的Linux-SSH协议资产）。目前我们仅支持自动登录的系统用户，且匹配的资产是唯一的。</p> 
 <div>
  <img alt="支持通过VS Code直连Linux-SSH协议资产，JumpServer v2.11.0发布" src="https://p6-tt.byteimg.com/origin/pgc-image/276a7aefa18b4a359c145430f55bf593?from=pc" referrerpolicy="no-referrer"> 
  <p style="text-align:center">图5 支持通过VS Code的Remote-SSH插件直连JumpServer所纳管的Linux-SSH协议资产</p> 
 </div> 
 <div>
  <img alt="支持通过VS Code直连Linux-SSH协议资产，JumpServer v2.11.0发布" src="https://p3-tt.byteimg.com/origin/pgc-image/17ad6c6a229f4a1f861f489a50cc2492?from=pc" referrerpolicy="no-referrer"> 
  <p style="text-align:center">图6 成功直连JumpServer所纳管的Linux-SSH协议资产</p> 
 </div> 
 <p><strong><span style="color:#28937c">4. 新增XRDP组件，支持用户通过本地客户端直连RDP资产（X-Pack增强包内）</span></strong></p> 
 <p>X-Pack增强功能方面，JumpServer v2.11.0版本新增XRDP组件，支持用户通过本地客户端直连RDP资产，建立图形会话界面。管理员选择“系统设置”→“终端设置”，填写好RDP地址。用户只需在Luna界面中，点击“WIndows资产”→“系统用户”→“连接方式”，选择“Microsoft RDP Client”选项，并点击“确定”按钮，即会自动下载一个RDP文件。用户通过本地自主安装的远程桌面客户端连接工具打开RDP文件，即可使用刚才选择的系统用户直连该资产，同时JumpServer还能够对其进行会话审计。</p> 
 <div>
  <img alt="支持通过VS Code直连Linux-SSH协议资产，JumpServer v2.11.0发布" src="https://p6-tt.byteimg.com/origin/pgc-image/8cc70ba7930443938db42fc6d0b2cfc5?from=pc" referrerpolicy="no-referrer"> 
  <p style="text-align:center">图7 用户下载RDP文件，点击“Windows资产”→ “系统用户”，选择Microsoft RDP Client连接方式</p> 
 </div> 
 <div>
  <img alt="支持通过VS Code直连Linux-SSH协议资产，JumpServer v2.11.0发布" src="https://p3-tt.byteimg.com/origin/pgc-image/9ee6362cc90e486980513f2e3f994ca4?from=pc" referrerpolicy="no-referrer"> 
  <p style="text-align:center">图8 使用本地Microsoft RDP Client打开该RDP文件，成功使用所选择的系统用户连接该资产</p> 
 </div> 
 <div>
  <img alt="支持通过VS Code直连Linux-SSH协议资产，JumpServer v2.11.0发布" src="https://p3-tt.byteimg.com/origin/pgc-image/20cbe402289f4f58bf5002d86eebb0f8?from=pc" referrerpolicy="no-referrer"> 
  <p style="text-align:center">图9 管理员可在“会话管理”界面审计该XRDP会话</p> 
 </div> 
 <p><strong><span style="color:#28937c">5. 新增账号管理功能模块（X-Pack增强包内）</span></strong></p> 
 <p>JumpServer v2.11.0版本还新增了账号管理功能模块（X-Pack增强包内）。主要包括资产账号、应用账号、收集用户、以及改密计划等功能，方便账号集中统一纳管。</p> 
 <p><strong>需要说明的是，这一版本的JumpServer取消了原有X-Pack模块中的密码匣子、收集用户、改密计划选项，将其功能合并至账号管理功能模块中。</strong>以资产账号为例，管理员点击资产账号左侧的资产树节点，即可获取该节点下所有资产列表信息；点击某条资产，右侧即可获取该资产的所有账号列表。用户还可对账号密码进行查询、更新、测试可连接性、导出资产账号密码等操作。</p> 
 <div>
  <img alt="支持通过VS Code直连Linux-SSH协议资产，JumpServer v2.11.0发布" src="https://p3-tt.byteimg.com/origin/pgc-image/16bc1da6a9294b7db1ea4e8e61a5c16e?from=pc" referrerpolicy="no-referrer"> 
  <p style="text-align:center">图10 获取资产的所有账号列表信息，并且可对账号密码进行查询、更新、测试可连接性、导出资产账号密码等操作</p> 
 </div> 
 <div>
  <img alt="支持通过VS Code直连Linux-SSH协议资产，JumpServer v2.11.0发布" src="https://p3-tt.byteimg.com/origin/pgc-image/ab530e878a424f549cd529da9396adeb?from=pc" referrerpolicy="no-referrer"> 
  <p style="text-align:center">图11 获取某应用的所有账号密码信息，并可进行查看密码、导出账号密码等操作</p> 
 </div> 
 <h1>功能优化</h1> 
 <p><span style="color:#28937c">■ </span>支持使用华为云对象存储服务（OBS)，可对会话录像进行存储；</p> 
 <p><span style="color:#28937c">■ </span>优化系统用户，支持用户设置临时密码；</p> 
 <p><span style="color:#28937c">■ </span>优化通过Luna页面登录资产时对系统用户的选择，提升用户使用体验；</p> 
 <p><span style="color:#28937c">■ </span>优化记录Token认证的登录日志；</p> 
 <p><span style="color:#28937c">■ </span>优化Koko组件的代码结构，并重构部分代码逻辑（Koko）；</p> 
 <p><span style="color:#28937c">■</span> 优化云同步的资产创建者字段为System（X-Pack增强包内）；</p> 
 <p><span style="color:#28937c">■ </span>优化云账号测试失败的提示信息（X-Pack增强包内）。</p> 
 <h1>Bug修复</h1> 
 <p><span style="color:#28937c">■ </span>修复Redis服务异常时（例如主从切换）用户Session立即过期的问题 ；</p> 
 <p><span style="color:#28937c">■</span> 修复导入模版生成的列表中没有显示整数类型所在列的问题；</p> 
 <p><span style="color:#28937c">■</span> 修改周期监测任务的配置参数；</p> 
 <p><span style="color:#28937c">■ </span>修复Azure云管账号创建必填字段提示信息（X-Pack增强包内）；</p> 
 <p><span style="color:#28937c">■</span> 修复组织批量删除的问题，禁止批量。</p> 
</div> 
<div style="text-align:left">
  
</div>
                                        </div>
                                      
</div>
            