
---
title: 'WebRTC M90 更新：功能增强、改进稳定性与性能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3655'
author: 开源中国
comments: false
date: Fri, 21 May 2021 03:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3655'
---

<div>   
<div class="content">
                                                                    
                                                        <p>WebRTC M90 目前已在 Chrome 测试版中发布，包含 2 个新特性和超过 29 个 bug 修复，以及功能增强、稳定性与性能等方面的改进。</p> 
<p><strong>欢迎关注本账号，我们将定期翻译 WebRTC 相关内容，帮助开发者获得最新资讯，走在行业前沿。</strong></p> 
<h2>01. 公共服务公告</h2> 
<p>Plan B SDP 弃用</p> 
<p>提醒：Plan B SDP 已被弃用，将来会被彻底删除。</p> 
<p>时间线见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgroups.google.com%2Fg%2Fdiscuss-w" target="_blank">https://groups.google.com/g/discuss-w</a></p> 
<h2>02.功能</h2> 
<h3>MediaStreamTrack Insertable Streams 源试用版</h3> 
<p>该 API 是 MediaStream 和 WebCodecs API 的扩展，允许应用程序：</p> 
<ul> 
 <li>访问 MediaStreamTrack 中的原始数据；</li> 
 <li>定义新的自定义 MediaStreamTracks。</li> 
</ul> 
<p>这两个功能可以组合使用，例如创建媒体特效（比如:"funny hats"）。</p> 
<p>该 API 依赖于 WebCodecs raw media interfaces 以及 WHATWG Streams API。该特性是 WebCodecs 源试用版的一部分。</p> 
<h3>getCurrentBrowsingContextMedia 源试用版</h3> 
<p>这是一个用于获取当前 Tab 内容的新的试验性 API，目前正在开发中。第一次实现可以作为试用版使用，更多信息见： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.google.com%2Fdocument%2Fd%2F1CIQH2ygvw7eTGO__Pcds_D46Gcn-iPAqESQqOsHHfkI%2Fedit" target="_blank">https://docs.google.com/document/d/1CIQH2ygvw7eTGO__Pcds_D46Gcn-iPAqESQqOsHHfkI/edit</a></p> 
<h2>03.功能及问题修复</h2> 
<p>可登陆：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.chromium.org%2Fp%2Fwebrtc%2Fissues%2Flist" target="_blank">https://bugs.chromium.org/p/webrtc/issues/list</a> 输入问题 ID 即可查询 bug 详情。 </p> 
<h3>No.1 </h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：1138888    </li> 
 <li>描述：WebRTC 低延迟渲染器  </li> 
 <li>组件：Blink>WebRTC>Video</li> 
</ul> 
<h3>No.2</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：1155477</li> 
 <li>描述：AEC3：线性滤波器会在长时间通话中逐渐发散 </li> 
 <li>组件：Blink>WebRTC>Audio</li> 
</ul> 
<h3>No.3</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：1170699</li> 
 <li>描述：WebRTC 的 AV1 编码初始化失败</li> 
 <li>组件：Blink>WebRTC</li> 
</ul> 
<h3>No.4</h3> 
<ul> 
 <li>类型：Feature</li> 
 <li>问题 ID：516700</li> 
 <li>描述：WebRTC Chromium 时钟差</li> 
 <li>组件：Blink>WebRTC</li> 
</ul> 
<h3>No.5</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：10675</li> 
 <li>描述：支持以 text2pcap 格式记录原始 rtp</li> 
 <li>组件：Network>RTP</li> 
</ul> 
<h3>No.6</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：11031</li> 
 <li>描述：MID 协商完成后，重传可能会失败 [Unified Plan]</li> 
 <li>组件：Network>RTP</li> 
</ul> 
<h3>No.7</h3> 
<ul> 
 <li>类型：Feature</li> 
 <li>问题 ID：11989</li> 
 <li>描述：为VoIP APIs提供VoipStatistics接口用于媒体统计</li> 
 <li>组件：Audio</li> 
</ul> 
<h3>No.8</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12265</li> 
 <li>描述：AEC3: 线性滤波器会在长时间通话中逐渐发散</li> 
 <li>组件：Audio</li> 
</ul> 
<h3>No.9</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12279</li> 
 <li>描述：(network.cc:908): 每 2 秒出现 10051 连接失败</li> 
 <li>组件：PeerConnection,Tools</li> 
</ul> 
<h3>No.10</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12380</li> 
 <li>描述：当接收 Opus 流时，每次刷新 DTX 包舒适噪音会突然改变能量值</li> 
 <li>组件：Audio</li> 
</ul> 
<h3>No.11</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12383</li> 
 <li>描述：收集 bundle 使用的统计信息 </li> 
</ul> 
<h3>No.12</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12384</li> 
 <li>描述：Windows 客户端上每次音频通话 Registry-Key-MMDevices-Audio-Handles 都会增加</li> 
 <li>组件：Audio</li> 
</ul> 
<h3>No.13</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12398</li> 
 <li>描述：使用svc并且宽/高的值为奇数时，AV1编码器出现seg错误</li> 
 <li>组件：Video  </li> 
</ul> 
<h3>No.14</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12407</li> 
 <li>描述：SEA 为静止图层创建并初始化编码器</li> 
 <li>组件：Video</li> 
</ul> 
<h3>No.15</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12426</li> 
 <li>描述：多线程访问 JsepTransport::jsep_transports_by_name_时未作保护</li> 
</ul> 
<h3>No.16</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12427</li> 
 <li>描述：PeerConnetion 不同线程之间编排 JsepTransportController 事件</li> 
</ul> 
<h3>No.17</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12430</li> 
 <li>描述：RtpBitrateConfigurator 的 TSAN 上报</li> 
</ul> 
<h3>No.18</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12431</li> 
 <li>描述：RTC 事件日志可视化在 Python3 环境下不生效</li> 
 <li>组件：Tools</li> 
</ul> 
<h3>No.19</h3> 
<ul> 
 <li>类型：Feature</li> 
 <li>问题 ID：12432</li> 
 <li>描述：在 RTC 事件日志中可视化 RTCP BYE 消息</li> 
 <li>组件：Tools</li> 
</ul> 
<h3>No.20</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12439</li> 
 <li>描述：如果系统时间回退，传统 getStats 将停止工作</li> 
 <li>组件：Stats</li> 
</ul> 
<h3>No.21</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12445</li> 
 <li>描述： JsepTransportController::mid_to_transport_未作保护</li> 
</ul> 
<h3>No.22</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12448</li> 
 <li>描述：ULPFEC:到达顺序异常以及到达延迟过久</li> 
 <li>组件：Video</li> 
</ul> 
<h3>No.23</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12455</li> 
 <li>描述：  webrtc::AudioSendStream::Config::ToString() 在 M90 版本调用失败</li> 
 <li>组件：Audio</li> 
</ul> 
<h3>No.24</h3> 
<ul> 
 <li>类型：Feature</li> 
 <li>问题 ID：12459</li> 
 <li>描述：限制最大图层数时，允许裁剪分辨率</li> 
 <li>组件：Video</li> 
</ul> 
<h3>No.25</h3> 
<ul> 
 <li>类型：Bug</li> 
 <li>问题 ID：12487</li> 
 <li>描述：实现视频 RTP 流的抖动数据统计</li> 
</ul> 
<p><strong>原文链接：</strong> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgroups.google.com%2Fg%2Fdiscuss-webrtc%2Fc%2F8VgEFxD_S80%2Fm%2FC6e_utBTAAAJ" target="_blank">https://groups.google.com/g/discuss-webrtc/c/8VgEFxD_S80/m/C6e_utBTAAAJ</a></p>
                                        </div>
                                      
</div>
            