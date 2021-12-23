
---
title: 'GIMP 2.10.30 发布，更好地支持 Adobe PSD'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3846'
author: 开源中国
comments: false
date: Thu, 23 Dec 2021 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3846'
---

<div>   
<div class="content">
                                                                                            <p>GIMP 图像编辑器发布了当前 2.10 稳定系列的一个新的错误修复版本。GIMP 2.10.30 改进了几种文件格式的支持。PSD 支持得到了各种类型的改进，AVIF 格式导出现在倾向于使用 AOM 编码器。</p> 
<p>在 Linux 和其他可能使用 Freedesktop 的操作系统上，现在使用 Freedesktop API 实现了显示器上的颜色选择（Colors dockable），并保留了旧的实现作为后备选择。截图插件现在也优先使用 Freedesktop API，而不是特定的 KDE 或 GNOME API。</p> 
<p>GIMP 2.10.30 中的变化包括：</p> 
<ul> 
 <li>对 Adobe Photoshop (PSD) 文件处理的改进</li> 
 <li>从 GIMP 导出 AVIF 现在倾向于使用 AOM AV1 编码器</li> 
 <li>在文本层渲染时不再遵循系统设置中的子像素字体渲染选择</li> 
 <li>重写核心选择绘制逻辑，使其能在 macOS Big Sur 及以上系统中使用</li> 
 <li>在 Windows上，从 <code>GetICMProfile()</code> 转移到 <code>WcsGetDefaultColorProfile()</code> API，因为前者在 Windows 11 中被损坏</li> 
 <li>扩展名 <code>.avif</code> 现在能与 GIMP 相关联</li> 
 <li>对元数据支持的各种改进</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.gimp.org%2Fnews%2F2021%2F12%2F21%2Fgimp-2-10-30-released%2F" target="_blank">https://www.gimp.org/news/2021/12/21/gimp-2-10-30-released/</a></p>
                                        </div>
                                      
</div>
            