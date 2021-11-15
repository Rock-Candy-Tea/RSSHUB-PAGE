
---
title: 'MKVToolNix v63.0.0 发布，MKV 视频编辑工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3972'
author: 开源中国
comments: false
date: Mon, 15 Nov 2021 07:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3972'
---

<div>   
<div class="content">
                                                                    
                                                        <p>MKVToolNix 63.0.0 发布了。MKVToolNix 是一套功能强大的 mkv(Matroska)格式制作和处理的工具，支持将多种视频、音频、字幕等格式封装成 mkv 格式。</p> 
<h3>新功能和改进</h3> 
<ul> 
 <li>mkvmerge: AC-3 解析器：BSID 值大于 10 且小于 15 的 E-AC-3 现在也可以被识别；</li> 
 <li>mkvmerge: 当使用语言代码来选择音轨时（例如 <code>-a und,en</code>），所有没有语言属性的音轨将被视为它们有一个被设置为 <code>und</code>的语言属性；</li> 
 <li>MKVToolNix GUI：仅在 Windows 上：当用 Qt ≥ 5.14 和 < 6 编译时，如果 Windows 设置为 125%、150% 或 175%，GUI 将被适当地缩放；</li> 
 <li>MKVToolNix GUI：当目前没有任务在运行时，右下角的 Spinner 现在会被隐藏；</li> 
 <li>MKVToolNix GUI：header 编辑器：在树状视图中添加了一个新列，显示 "track enabled" 标志的状态，该信息也显示在右侧的轨道概览页面上；</li> 
 <li>MKVToolNix GUI：header 编辑器：用户现在可以通过拖放来重新排列轨道；</li> 
</ul> 
<h3>错误修正</h3> 
<ul> 
 <li>mkvmerge: AVI 阅读器：修复了读取包含 <code>vprp</code> 视频属性 header 块的 AVI 文件，避免读取过早中止;</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bunkus.org%2Fblog%2F2021%2F11%2Fmkvtoolnix-v63-0-0-released%2F" target="_blank">https://www.bunkus.org/blog/2021/11/mkvtoolnix-v63-0-0-released/</a></p>
                                        </div>
                                      
</div>
            