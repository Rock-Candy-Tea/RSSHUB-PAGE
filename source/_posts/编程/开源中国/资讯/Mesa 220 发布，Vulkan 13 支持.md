
---
title: 'Mesa 22.0 发布，Vulkan 1.3 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8872'
author: 开源中国
comments: false
date: Fri, 11 Mar 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8872'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000"><span style="background-color:#ffffff">Mesa 22.0 已经发布。像往常一样，大部分开源的 3D GPU 驱动活动都是围绕着英特尔和 AMD 的 Radeon graphics drivers </span><span style="background-color:#ffffff">—— </span><span style="background-color:#ffffff">英特尔的 Iris Gallium3D、最近推出的英特尔 Crocus Gallium3D 驱动、英特尔 ANV Vulkan、RadeonSI Gallium3D 和 Radeon RADV 驱动。但是，Zink OpenGL-on-Vulkan 实现、Freedreno、Panfrost和其他各种小型驱动程序工作也在持续推进中；在 Nouveau 开源的 NVIDIA 驱动程序方面则没有什么值得关注的。</span></span></p> 
<p><span style="color:#000000"><span style="background-color:#ffffff">Mesa 22.0 的一些亮点</span></span><span style="background-color:#ffffff; color:#121212"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.phoronix.com%2Fscan.php%3Fpage%3Dnews_item%26px%3DMesa-22.0-Released" target="_blank">包括</a>：</span></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#121212">Vulkan 1.3 适用于 Radeon "RADV" 和 Intel "ANV" Vulkan 驱动程序。Vulkan 1.3 所需的各种扩展在本周期早期添加，包括动态渲染（KHR_dynamic_rendering）和其他功能。</span></li> 
 <li>英特尔 Alder Lake N 支持与 starting Raptor Lake一起到位。还有新的但已禁用的 DG2/Alchemist 代码。</li> 
 <li>适用于英特尔 OpenGL 和 Vulkan 驱动程序的 Adaptive-Sync/VRR。</li> 
 <li>用于 RADV 和英特尔 ANV 的 DG2/Alchemist 实验性网格着色器。</li> 
 <li>继续进行 RADV 光线的工作。</li> 
 <li>更好的 Radeon VCE 视频编码性能。</li> 
 <li>RadeonSI 稀疏纹理支持。</li> 
 <li>对 RADV 的模拟 ETC2 支持。</li> 
 <li>用于 Navi 1x 消费级 GPU 的 RadeonSI NGG 着色器剔除。</li> 
 <li>Mesa 的 classic drivers 退役。同样，英特尔的 OpenSWR 驱动程序已移至 Mesa 的“Amber”分支。</li> 
 <li>RadeonSI 和 Zink 现在支持 OpenGL ARB_sparse_texture 扩展。</li> 
 <li>Microsoft 的 D3D12 代码现在支持 OpenGL ES 3.1 和其他正在努力实现 GL 4.x 支持的功能，例如计算着色器。</li> 
 <li>使用 Linux 5.17+ 和即将推出的 VMware 虚拟化软件时，VMware SVGA OpenGL 4.3 支持。</li> 
 <li>Zink OpenGL-on-Vulkan 代码继续变得更加高性能和更好地支持各种 OpenGL 功能。</li> 
 <li>Raspberry Pi V3DV Vulkan 驱动程序现在可以在 Android 上运行。</li> 
 <li>Freedreno 对 Clover OpenCL 有基本的支持。</li> 
 <li>Mesa 的 EGL 代码中的 DMA-BUF 反馈支持。</li> 
 <li>各种性能优化，包括更多 RadeonSI 优化。</li> 
</ul> 
<p>详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.freedesktop.org%2Farchives%2Fmesa-announce%2F2022-March%2F000665.html" target="_blank">查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            