
---
title: 'OBS Studio 28.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1340'
author: 开源中国
comments: false
date: Fri, 02 Sep 2022 07:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1340'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">OBS Studio 28 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fobsproject%2Fobs-studio%2Freleases%2Ftag%2F28.0.0" target="_blank">发布</a>，</span><span style="background-color:#ffffff; color:#24292f">此版本标志着 OBS 成立 10 周年。</span><span style="background-color:#ffffff; color:#333333">这是一个重大更新版本，新增了许多重要功能和其他升级。其中包括：</span></p> 
<ul> 
 <li>10-bit 和 HDR 编码支持 
  <ul> 
   <li>目前只能使用 AV1 和 HEVC 编码器对 HDR 和 10-bit 色彩进行编码。10-bit HEVC 编码需要 NVIDIA 10 系列、AMD 5000 系列或更新的 GPU。尚不支持 Intel QuickSync 和 Apple VT。</li> 
   <li>HDR 的推荐设置是 <span style="background-color:#ffffff; color:#24292f">Color Format P010 & Color Space Rec. 2100 PQ</span></li> 
   <li>如果希望对 10-bit SDR 进行编码，用户可以使用包含 SDR 颜色空间的 Color Format P010（例如 Rec. 709, Rec. 601）。不过仍然需要 AV1 或 HEVC</li> 
   <li>目前仅支持使用 YouTube 的 HLS 服务通过 HEVC 编码器支持 HDR 流式传输</li> 
   <li>在 SDR 中进行合成时，以 HDR 运行的游戏现在可以正确地映射到 SDR</li> 
   <li>如果设备支持，视频捕获设备可用于捕获和流式传输 HDR（例如 EVGA XR1 Pro, Elgato 4K60 Pro Mk.2, AverMedia Live Gamer 4K）</li> 
   <li>如果 source 使用 HDR 进行渲染，某些 filters 将不起作用：应用 LUT、色度键、颜色键、图像蒙版/混合、亮度键、锐度</li> 
   <li>Mac/Linux 支持有限。HDR 预览不起作用，几个输入/编码器仍需要更新。</li> 
  </ul> </li> 
 <li>将 UI 框架升级到 Qt6（所有平台） 
  <ul> 
   <li>由于 Qt 6 已不再支持 Windows 7 和 8、macOS 10.13 和 10.14、Ubuntu 18.04 和所有 32 位操作系统。因此，OBS Studio 不再支持以下操作系统平台： 
    <ul> 
     <li>Windows 7 & 8</li> 
     <li>macOS 10.13 & 10.14</li> 
     <li>Ubuntu 18.04</li> 
     <li>所有 32 位操作系统</li> 
    </ul> </li> 
   <li>此外，许多依赖 Qt5 组件的第三方插件在没有升级到 Qt6 之前可能无法正常运行</li> 
  </ul> </li> 
 <li>原生支持 Apple Silicon (macOS) 
  <ul> 
   <li>请注意，许多第三方插件需要发布其插件的 Apple Silicon 版本才能在支持 Apple Silicon 的 OBS 上运行</li> 
  </ul> </li> 
 <li><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新功能和添加：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> 
  <ul> 
   <li>原生集成 obs-websocket 5.0 插件（所有平台），<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fobsproject.com%2Fblog%2Fobs-studio-and-obs-websocket-join-forces" target="_blank">点此查看详情</a></li> 
   <li>升级 AMD 编码器实现 (Windows)</li> 
   <li>在 macOS 12.5+ 上支持 ScreenCaptureKit，显著提升截图性能</li> 
   <li>对 Apple VT 编码器的重大改进 (macOS)</li> 
   <li>特定于应用程序的音频捕获 (Windows)</li> 
   <li>集成 NVIDIA 移除背景功能 (Windows)</li> 
   <li>支持按时间或文件大小自动切割录音（所有平台）</li> 
   <li>增加新的默认主题 Yami（所有平台）</li> 
  </ul> </li> 
</ul> 
<p>……</p> 
<p>更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fobsproject%2Fobs-studio%2Freleases%2Ftag%2F28.0.0" target="_blank">查看发布说明</a>。</p>
                                        </div>
                                      
</div>
            