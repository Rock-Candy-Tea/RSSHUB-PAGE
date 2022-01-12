
---
title: 'HandBrake 1.5.1 发布，多功能视频转码工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5015'
author: 开源中国
comments: false
date: Wed, 12 Jan 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5015'
---

<div>   
<div class="content">
                                                                                            <p>HandBrake 是一款适用于 Linux、Mac 和 Windows 的开源视频转码器。在更新之前，请确保队列中没有待处理的编码。也请对你的任何自定义预设和应用程序首选项进行备份，因为它们可能与新版本不兼容。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Handbrake 1.5.1 现已发布，更新内容如下：</p> 
<h4><strong>Upgrade Notice</strong></h4> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在更新 HandBrake 之前，请确保队列中没有待处理的编码，并确保备份你拥有的任何自定义预设和应用首选项，因为它们可能与新版本不兼容。Windows 用户，请确保安装 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdotnet.microsoft.com%2Fen-us%2Fdownload%2Fdotnet%2F6.0" target="_blank">Microsoft .NET Desktop Runtime 6.0.0 或更高版本</a>。仔细阅读：你需要 <strong>DESKTOP </strong>runtime。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h4><strong>HandBrake 1.5.1</strong></h4> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>这是对 HandBrake 1.5.0 的 rebuild，没有任何功能变化。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Build system</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>修复了源码压缩包的一个问题，它破坏了 Flathub Builds。</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Windows</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>Windows UI 现在仅适用于 .NET 6.0。（不再需要 .NET 5.0）</li> 
</ul> 
<h4><strong>HandBrake 1.5.0</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>所有平台</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Video</p> 
<ul> 
 <li>修复了旧 Intel CPU 上导致 CLI 无法初始化的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F3924" target="_blank">#3924</a> )</li> 
 <li>更新了视频引擎以保留色度样本位置信息</li> 
 <li>更新了英特尔快速同步以使用英特尔 oneAPI 视频处理库 (oneVPL)</li> 
</ul> 
<p style="text-align:start">Audio</p> 
<ul> 
 <li>修复了 MP2 音频源在禁用直通时不使用 fallback encoder 的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F3863" target="_blank">#3863</a> )</li> 
 <li>修复了 FFmpeg AAC 音频编码器质量模式缩放范围 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F1295" target="_blank">#1295</a> )</li> 
</ul> 
<p style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>字幕</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>修复了一个关于字幕通过时长的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F3764" target="_blank">#3764</a> )</li> 
</ul> 
<p style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>构建系统</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>修复了 Flatpak 构建过程中的多个潜在 race conditions</li> 
 <li>更新了 mac-toolchain-build 脚本，增加了新的工具版本</li> 
</ul> 
<p style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>第三方库</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>更新的库 
  <ul> 
   <li>FFmpeg 4.4.1（解码和过滤器）</li> 
   <li>FreeType 2.11.1（字幕）</li> 
   <li>Fribidi 1.0.11（字幕）</li> 
   <li>HarfBuzz 3.1.2（字幕）</li> 
   <li>Jansson 2.14（JSON 架构）</li> 
   <li>libass 0.15.2（字幕）</li> 
   <li>libdav1d 0.9.2（AV1 解码）</li> 
   <li>libjpeg-turbo 2.1.2（预览图像压缩）</li> 
   <li>libogg 1.3.5（Xiph 编解码器支持）</li> 
   <li>libvpx 1.11.0（VP8/VP9 视频编码）</li> 
   <li>zimg 3.0.3（颜色转换）</li> 
  </ul> </li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Freleases%2Ftag%2F1.5.1" target="_blank">https://github.com/HandBrake/HandBrake/releases/tag/1.5.1</a></p>
                                        </div>
                                      
</div>
            