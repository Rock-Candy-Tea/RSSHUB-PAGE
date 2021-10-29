
---
title: 'WebRTC M94 更新：MediaTrack 可插入流、支持 RFC 2198 冗余项'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-657f0700e7501e91a1f8a4d759622844cee.jpg'
author: 开源中国
comments: false
date: Fri, 29 Oct 2021 06:50:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-657f0700e7501e91a1f8a4d759622844cee.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><span> <img alt height="383" src="https://oscimg.oschina.net/oscnet/up-657f0700e7501e91a1f8a4d759622844cee.jpg" width="900" referrerpolicy="no-referrer"></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>WebRTC M94<span> </span></strong>目前已在 Chrome 测试版中发布，包含 1 个新特性以及超过 19 个 Bug 修复，功能增强，稳定性与性能等方面的改进。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">01.<strong>公共服务公告</strong></h1> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>1. MediaTrack 可插入流</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MediaStreamTrack 的可插入流 API 目前可以作为稳定 Web API 的形式获取了，不再需要源试用版！该 API 可用于直接访问和修改音频或视频流。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更多有关信息见：https://web.dev/mediastreamtrack-insertable-media-processing/</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>2. 非标准的 RTCConfiguration.offerExtmapAllowMixed 选项已从 Chrome 中移除</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">RTCPeerConnection 构造函数中的非标准 offerExtmapAllowMixed 已经从M94 中删除。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">另请参阅删除 https://groups.google.com/a/chromium.org/g/blink-dev/c/Plik-x6biZ0/m/eJ8P1iy0AQAJ 的意图，了解详细信息以及如何在需要调用 setRemoteDescription 之前进行 SDP 操作.</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">02. 功能及问题修复</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">可登陆：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.chromium.org%2Fp%2Fwebrtc%2Fissues%2Flist" target="_blank">Monorail - webrtc - Web-based real-time communication - Monorail<span> </span></a>输入问题 ID 即可查询 Bug 详情。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.1</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：1084702</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：Pixel 3 上的移动版 Chrome 在 WebRTC 通话中出现非 16 位对齐分辨率的视频损坏：硬件 VP8 编码器 Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Blink>WebRTC>Video,</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Internals>GPU>Video,</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Internals>Media>Capture</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.2</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Feature</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：1225701</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：为开发者构建默认启用 DCHECKS</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Build</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.3</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：1232358</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：在 WebRTC 中启用 AV1-SVC 时依赖项描述符 (DD) RTP 扩展故障</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Blink>WebRTC</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.4</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：1234779</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：remoteDescription 状态为 a=inactive 时，Peer Connection 仍然发送 RTP</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Blink>WebRTC>PeerConnection</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.5</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：1236202</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：合并请求：PeerConnection 假定所有新的 m= 部分都将进入第一个 BUNDLE 组</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Blink>WebRTC>PeerConnection</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.6</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：999886</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：代码库对比 clang r370594 添加 -Wfinal-dtor-non-final-class 编译选项</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Build,Tools>LLVM</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.7</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：11640</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：支持 RFC 2198 冗余项</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Audio</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.8</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：12470</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：带有序列号间隙的循环和空 RTP 数据包</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Network>RTP</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.9</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：12837</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：PC 端在重新协商时发出候选项</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：PeerConnection</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.10</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：12906</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：PeerConnection 假定所有新的 m= 部分都将进入第一个 BUNDLE 组</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：PeerConnection</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.11</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：12975</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：video_replay 的纵横比是硬编码的</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Tools</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.12</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：12980</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：视频的抖动统计数据远高于预期</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Stats</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.13</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：12988</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：WebRTC 准备为 Chromium 的 dcheck_always_on 默认值提供切换选项</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Build</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.14</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：12989</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：50-tile 会议通话时 NackModule2 可能会导致 2.5 kHz 频率的空闲唤醒</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Internals</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.15</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：12991</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：在 Chrome Windows 中打开硬件加速时出现 AVC 解析错误</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Video</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.16</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：12995</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：FrameEncryptorInterface 无法用于视频</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：PeerConnection</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.17</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：13037</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：每层的编码帧率统计数据不准确</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Stats,Video</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.18</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：13053</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：Mac ARM64 上的 iSAC 测试在chromium回滚后启动失败</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Audio,Build</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.19</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：4299</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：从生成的 offer 中删除 a=ice-options:google-ice 项</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：PeerConnection</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>No.20</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">类型：Bug</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">问题 ID：1231698</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">描述：display-capture（权限策略）</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">组件：Blink>GetDisplayMedia</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">原文链接：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">https://groups.google.com/g/discuss-webrtc/c/tFyWdqW2sQM/m/ebfZvC9VAgAJ</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">关于网易云信</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">网易云信是集网易 20 余年 IM 以及音视频技术打造的融合通信云服务专家，稳定易用的通信与视频 PaaS 平台。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">提供融合通信与视频的核心能力与组件，包含 IM 即时通讯、5G 消息平台、一键登录、信令、短信与号码隐私保护等通信服务，音视频通话、直播、点播、互动直播与互动白板等音视频服务，视频会议等组件服务。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">网易云信服务于网易云音乐、好未来、新东方、科大讯飞、南京银行等各行各业客户。</p>
                                        </div>
                                      
</div>
            