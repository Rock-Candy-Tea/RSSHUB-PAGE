
---
title: 'Android 13 开发者预览版 2 发布，重视用户隐私和安全'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0318/073534_hSj5_5430600.png'
author: 开源中国
comments: false
date: Fri, 18 Mar 2022 07:46:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0318/073534_hSj5_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">Android 13 Developer Preview 2  发布了，该版本仍然围绕着 Android 13 的<strong>隐私和安全、开发者生产力以及平板电脑和大屏幕支持等核心主题构建。</strong></p> 
<h3 style="margin-left:0px">隐私和用户信任</h3> 
<ul> 
 <li><strong>通知权限 ，</strong>Android 13 引入了一个用于从应用发送通知的新<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fguide%2Ftopics%2Fpermissions%2Foverview%23runtime" target="_blank">运行时权限： </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fandroid%2FManifest.permission%23POST_NOTIFICATIONS" target="_blank">POST_NOTIFICATIONS</a>。</li> 
</ul> 
<p style="margin-left:0px">面向 Android 13 的应用需要在发布通知之前向用户<strong>请求通知权限</strong>，对于面向 Android 12 或更低版本的应用，系统将自动处理升级流程，为用户提供更多上下文和控制权，关于该通知权限的更多内容可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fabout%2Fversions%2F13%2Fchanges%2Fnotification-permission" target="_blank">点此查看</a>。</p> 
<p><img alt height="355" src="https://static.oschina.net/uploads/space/2022/0318/073534_hSj5_5430600.png" width="400" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>开发人员可降级应用权限</strong> <strong>-</strong>某些应用程序可能不再需要用户之前授予的某些权限来启用特定功能，或保留旧 Android 版本的敏感权限。Android 13 提供了一个<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fandroid%2Fcontent%2FContext.html%23revokeOwnPermissionsOnKill%28java.util.Collection%253Cjava.lang.String%253E%29" target="_blank">新 API</a>，通过降级应用之前授予的运行时权限，来保护用户隐私。</li> 
 <li style="margin-left: 0px;"><strong>更安全地导出上下文注册的接收器 -</strong>在 Android 12 要求开发人员声明清单声明的 Intent 接收器的可导出性。在 Android 13 要求开发者对上下文注册的接收器也执行相同的操作，方法是在为非系统源注册接收器时添加<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fandroid%2Fcontent%2FContext.html%23RECEIVER_EXPORTED" target="_blank">RECEIVER_EXPORTED</a> 或 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fandroid%2Fcontent%2FContext.html%23RECEIVER_NOT_EXPORTED" target="_blank">RECEIVER_NOT_EXPORTED标志，</a>此举有助于确保接收器不可用于其他应用程序发送广播。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">开发人员生产力</h2> 
<ul> 
 <li><strong style="color:rgba(0, 0, 0, 0.67)">改进的日文文本换行</strong> <strong style="color:rgba(0, 0, 0, 0.67)">-</strong> TextViews 现在可以通过文集（听起来自然的最小单词单位）或短语（而不是字符）来换行文本，以获得更优美和可读的日文应用程序。下图是启用短语样式（底部文字）和未启用（顶部文字）的日语文本换行：</li> 
</ul> 
<p><img alt height="483" src="https://static.oschina.net/uploads/space/2022/0318/074203_GTyE_5430600.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>改进了非拉丁脚本（non-latin scripts）的行高 -</strong> Android 13 通过使用适合每种语言的行高来改进非拉丁脚本（例如泰米尔语、缅甸语、泰卢固语和藏语）的显示，新的行高可防止剪裁并改善字符的定位。</li> 
</ul> 
<p><img alt height="370" src="https://static.oschina.net/uploads/space/2022/0318/074528_tYeW_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong style="color:rgba(0, 0, 0, 0.67)">颜色矢量字体</strong> <strong style="color:rgba(0, 0, 0, 0.67)">- Android 13 增加了对 COLR 版本 1（</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Ftypography%2Fopentype%2Fspec%2Fcolr" target="_blank">规范</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DBmqYm5Wwz8M" target="_blank">介绍视频</a>）字体的渲染支持，并将系统表情符号更新为 COLRv1 格式。COLRv1 是一种新的、高度紧凑的字体格式，可以在任何大小下快速清晰地呈现。</li> 
 <li><strong style="color:rgba(0, 0, 0, 0.67)">蓝牙 LE 音频</strong> <strong style="color:rgba(0, 0, 0, 0.67)">-</strong>低功耗 (LE) 音频是下一代无线音频，旨在取代经典蓝牙并支持新的用例和连接拓扑。</li> 
 <li><strong style="color:rgba(0, 0, 0, 0.67)">MIDI 2.0 </strong><strong style="color:rgba(0, 0, 0, 0.67)">-</strong> Android 13 增加了对新 MIDI 2.0 标准的支持，包括通过 USB 连接 MIDI 2.0 硬件的能力。</li> 
</ul> 
<p> </p> 
<p>此版本该包含一些应用兼容性的介绍，更多内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroid-developers.googleblog.com%2F2022%2F03%2Fsecond-preview-android-13.html" target="_blank">发行公告</a>。</p>
                                        </div>
                                      
</div>
            