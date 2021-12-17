
---
title: 'WebRTC M95 更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9872'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 13:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9872'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; text-align:left"><span><span><span>WebRTC M95</span><span>目前已在Chrome测试版中发布，包含4个新特性以及超过6个bug修复、功能增强、稳定性与性能等方面的改进。</span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>欢迎关注</span></span></span></span>网易云信账号<span><span><span><span>，我们将定期翻译 WebRTC 相关内容，帮助开发者获得最新资讯，走在行业前沿。</span></span></span></span></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span><span>01.</span></span><span><span>亮点功能</span></span></span></span></span></h1> 
<p style="color:#333333; text-align:left"><span><span><strong><span><span style="color:#434343">dcSCTP</span></span></strong></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span><span style="color:#434343">用于SCTP传输的DcSCTP库的推出开启了这一里程碑。详情见</span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgroups.google.com%2Fg%2Fdiscuss-webrtc%2Fc%2FYIMS2WdKeM0" target="_blank"><span><span><span style="color:#0366d6">公告</span></span></span></a><span><span><span style="color:#434343">。</span></span></span></span></span></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span><span>02.<span> </span></span></span><span><span>功能及问题修复</span></span></span></span></span></h1> 
<p style="color:#333333; text-align:left"><span><span><span><span>可登陆：</span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.chromium.org%2Fp%2Fwebrtc%2Fissues%2Flist" target="_blank"><span><span><span style="color:#1a84ee"><span><span>https://bugs.chromium.org/p/webrtc/issues/list</span></span></span></span></span></a><span> </span><span><span>输入问题 ID 即可查询 Bug 详情。</span></span></span></span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span>No.1</span></span></span></span></h4> 
<p style="color:#333333; text-align:left"><span><span><span><span>类型：</span></span><span><span><span style="color:#434343">Feature</span></span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>问题 ID：</span></span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcrbug.com%2F1146942" target="_blank"><span><span style="color:#003884"><span><span>1146942</span></span></span></span></a></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>描述：</span></span><span><span style="color:#202124">chromium/webrtc</span></span><span><span style="color:#202124">使用的pipewire 版本从 0.2 升级到 0.3</span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>组件：</span></span><span><span><span style="color:#434343">Internals>Media>ScreenCapture</span></span></span></span></span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span>No.2</span></span></span></span></h4> 
<p style="color:#333333; text-align:left"><span><span><span><span>类型：Feature</span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>问题 ID：</span></span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcrbug.com%2F1203442" target="_blank"><span><span style="color:#003884"><span><span>1203442</span></span></span></span></a></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>描述：</span></span><span><span><span style="color:#434343">删除3DES密码套件</span></span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>组件：</span></span><span><span><span style="color:#434343">Internals>Network>SSL</span></span></span></span></span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span>No.3</span></span></span></span></h4> 
<p style="color:#333333; text-align:left"><span><span><span><span>类型：Bug</span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>问题 ID：</span></span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcrbug.com%2F1241213" target="_blank"><span><span style="color:#003884"><span><span>1241213</span></span></span></span></a></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>描述：</span></span><span><span><span style="color:#434343">M93</span></span></span><span><span><span style="color:#434343">之后版本复用收发器来添加最近删除的视频轨道的功能不起作用</span></span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>组件：Blink>WebRTC</span></span></span></span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span>No.4</span></span></span></span></h4> 
<p style="color:#333333; text-align:left"><span><span><span><span>类型：Bug</span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>问题 ID：</span></span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcrbug.com%2F1247182" target="_blank"><span><span style="color:#003884"><span><span>1247182</span></span></span></span></a></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>描述：</span></span><span><span><span style="color:#434343">rtcp_receiver_fuzzer:  webrtc::RTCPReceiver::ParseCompoundPacket</span></span></span><span><span><span style="color:#434343">使用了未初始化的值</span></span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>组件：</span></span><span><span><span style="color:#434343">Blink>WebRTC>Network</span></span></span></span></span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span>No.5</span></span></span></span></h4> 
<p style="color:#333333; text-align:left"><span><span><span><span>类型：Bug</span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>问题 ID：</span></span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fbugs.webrtc.org%2F10812" target="_blank"><span><span style="color:#003884"><span><span>10812</span></span></span></span></a></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>描述：</span></span><span><span><span style="color:#434343">解决编码器封装和测试模块的非整数帧率问题</span></span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>组件：</span></span><span><span><span style="color:#434343">Video</span></span></span></span></span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span>No.6</span></span></span></span></h4> 
<p style="color:#333333; text-align:left"><span><span><span><span>类型：Bug</span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>问题 ID：</span></span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fbugs.webrtc.org%2F11640" target="_blank"><span><span style="color:#003884"><span><span>11640</span></span></span></span></a></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>描述：</span></span><span><span><span style="color:#434343">支持RFC 2198冗余</span></span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>组件：</span></span><span><span><span style="color:#434343">Audio</span></span></span></span></span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span>No.7</span></span></span></span></h4> 
<p style="color:#333333; text-align:left"><span><span><span><span>类型：Bug</span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>问题 ID：</span></span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fbugs.webrtc.org%2F12933" target="_blank"><span><span style="color:#003884"><span><span>12933</span></span></span></span></a></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>描述：</span></span><span><span><span style="color:#434343">Chrome</span></span></span><span><span><span style="color:#434343">不支持接收角色设置选项不为actpass的提议SDP</span></span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>组件：</span></span><span><span><span style="color:#434343">PeerConnection</span></span></span></span></span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span>No.8</span></span></span></span></h4> 
<p style="color:#333333; text-align:left"><span><span><span><span>类型：Feature</span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>问题 ID：</span></span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fbugs.webrtc.org%2F13077" target="_blank"><span><span style="color:#003884"><span><span>13077</span></span></span></span></a></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>描述：</span></span><span><span><span style="color:#434343">可插入流:公开有效载荷类型</span></span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>组件：</span></span><span><span><span style="color:#434343">PeerConnection</span></span></span></span></span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span>No.9</span></span></span></span></h4> 
<p style="color:#333333; text-align:left"><span><span><span><span>类型：Bug</span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>问题 ID：</span></span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fbugs.webrtc.org%2F13078" target="_blank"><span><span style="color:#003884"><span><span>13078</span></span></span></span></a></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>描述：</span></span><span><span><span style="color:#434343">WgcCaptureSource</span></span></span><span><span><span style="color:#434343">在尝试采集所有显示器时抛出异常</span></span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>组件：</span></span><span><span><span style="color:#434343">DesktopCapture</span></span></span></span></span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span>原文链接：</span></span></span></span></h3> 
<p style="color:#333333; text-align:left"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgroups.google.com%2Fg%2Fdiscuss-webrtc%2Fc%2FSfzpFc-dH-E%2Fm%2FJHlMpLO1AAAJ" target="_blank"><span><span style="color:#003884"><span><span>https://groups.google.com/g/discuss-webrtc/c/SfzpFc-dH-E/m/JHlMpLO1AAAJ</span></span></span></span></a></span></span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span><span><span><span><span>关于</span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetease.im%2F%3Ffrom%3Dzhihu%26utm_source%3Dzhihu%26utm_medium%3Darticle%26utm_content%3D1216" target="_blank"><span><span>网易云信</span></span></a></span></span></span></h2> 
<p style="color:#333333; text-align:left"><span><span><span><span>网易云信是集网易 20 余年 IM 以及音视频技术打造的融合通信云服务专家，稳定易用的通信与视频 PaaS 平台。</span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>提供融合通信与视频的核心能力与组件，包含 IM 即时通讯、5G 消息平台、一键登录、信令、短信与号码隐私保护等通信服务，音视频通话、直播、点播、互动直播与互动白板等音视频服务，视频会议等组件服务。</span></span></span></span></p> 
<p style="color:#333333; text-align:left"><span><span><span><span>网易云信服务于网易云音乐、好未来、新东方、科大讯飞、南京银行等各行各业客户。</span></span></span></span></p>
                                        </div>
                                      
</div>
            