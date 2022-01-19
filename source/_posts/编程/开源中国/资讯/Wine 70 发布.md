
---
title: 'Wine 7.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9547'
author: 开源中国
comments: false
date: Wed, 19 Jan 2022 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9547'
---

<div>   
<div class="content">
                                                                                            <p>Wine（Wine Is Not an Emulator）是一个能够在多种兼容 POSIX 接口的操作系统（诸如 Linux、macOS 与 BSD 等）上运行 Windows 应用的兼容层。它不是像虚拟机或者模拟器一样模仿内部的 Windows 逻辑，而是将 Windows API 调用翻译成为动态的 POSIX 调用，免除了性能和其它一些行为的内存占用，让你能够干净地整合 Windows 应用到桌面。</p> 
<p>Wine 7.0 已经正式发布，该版本中值得关注的更新内容包括：</p> 
<h3>PE 模块</h3> 
<ul> 
 <li>除了少数例外，所有模块都可以用 PE 格式构建。</li> 
 <li>对于有关联的 Unix 库的 PE 模块，PE 部分和 Unix 部分之间的接口是通过标准的 NT 系统调用。</li> 
 <li>内置的 dlls 只有在磁盘上有相应的PE文件时才被加载。</li> 
</ul> 
<h3>WoW64</h3> 
<ul> 
 <li>实现了 64 位 Windows-on-Windows（WoW64）架构，并且支持在 64 位 Unix 主机进程中运行 32 位 Windows 应用程序。</li> 
 <li>大多数 Unix 库都实现了 WoW64 thunks，使 32 位 PE 模块可以调用 64 位的 Unix 库。</li> 
</ul> 
<h3>主题</h3> 
<ul> 
 <li>Wine 中包含了一个 "Light" 主题，有 "Blue" 和 "Classic Blue" 两个颜色变体。</li> 
 <li>所有的 Common Controls 都支持主题化，并在主题改变时自动刷新。</li> 
 <li>所有内置的应用程序都支持主题化，以及高 DPI 渲染。</li> 
</ul> 
<h3>图形</h3> 
<ul> 
 <li>有一个新的 Win32u 库实现了内核方面的图形和窗口管理支持。</li> 
 <li>Vulkan 驱动支持升级到 Vulkan 规范的 1.2.201 版本。</li> 
 <li>对 Direct2D 效果的一些初步支持已经实现。</li> 
 <li>Direct2D API 支持 ID2D1MultiThread 接口。</li> 
 <li>WindowsCodecs 支持对 WMP（Windows Media Photo）格式的图像进行解码，以及将图像编码为 DDS（DirectDraw Surface）格式。</li> 
 <li>WindowsCodecs 不再支持将图像编码为 macOS ICNS 格式。</li> 
</ul> 
<h3>Direct3D</h3> 
<ul> 
 <li>对 Wine Direct3D 实现的 Vulkan 渲染器进行了各种改进。</li> 
 <li>Direct3D 12 支持 1.1 版本的根签名。</li> 
 <li>下列额外的显卡会被 Direct3D 显卡数据库所识别： 
  <ul> 
   <li>AMD Radeon RX 5500M</li> 
   <li>AMD Radeon RX 6800/6800 XT/6900 XT</li> 
   <li>AMD Van Gogh</li> 
   <li>英特尔 UHD Graphics 630</li> 
   <li>Nvidia GT 1030</li> 
  </ul> </li> 
 <li>……</li> 
</ul> 
<h3>D3DX</h3> 
<ul> 
 <li>对 D3DX 效果框架的第 10 版的支持有了很大的改进。</li> 
 <li>D3DX 10 支持 Windows Media Photo（JPEG XR）图像文件格式。</li> 
 <li>各种 D3DX10 纹理创建函数（ <code>D3DX10CreateTextureFromMemory()</code>及其变体）被实现。</li> 
 <li>增加了 ID3DX10Sprite 接口的部分实现。</li> 
 <li>增加了 ID3DX10Font 接口的部分实现。</li> 
</ul> 
<h3>音频/视频</h3> 
<ul> 
 <li>DirectShow 和 Media Foundation GStreamer 被统一到一个单一的后端，使其更容易实现新的媒体解码 API。</li> 
 <li>Windows Media 的异步和同步阅读器对象是基于 WineGStreamer 后端实现的。</li> 
 <li>Media Foundation 的支持更加完整</li> 
 <li>QuickTime 解码器库（wineqtdecoder）被移除，GStreamer 是 macOS 上所有内置多媒体编解码器所需的。</li> 
</ul> 
<h3>文本和字体</h3> 
<ul> 
 <li>Font Set 对象是在 DirectWrite 中实现的。</li> 
 <li>TextHost 接口已在 RichEdit 中正确实现。</li> 
</ul> 
<h3>国际化</h3> 
<ul> 
 <li>统一码字符表是基于 14.0.0 版本。</li> 
 <li>时区数据被更新，基于来自 Olson 和 Unicode CLDR 数据库的信息。</li> 
 <li>720（阿拉伯语、波斯语和乌尔都语）和 20949（韩文）代码段得到支持。</li> 
 <li>支持 sr-Latn-RS 区划。</li> 
</ul> 
<p>……</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.winehq.org%2Fannounce%2F7.0" target="_blank">https://www.winehq.org/announce/7.0</a></p>
                                        </div>
                                      
</div>
            