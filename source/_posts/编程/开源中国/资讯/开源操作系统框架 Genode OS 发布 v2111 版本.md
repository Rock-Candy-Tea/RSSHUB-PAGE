
---
title: '开源操作系统框架 Genode OS 发布 v21.11 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5351'
author: 开源中国
comments: false
date: Sun, 05 Dec 2021 08:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5351'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff">开源操作系统框架 Genode OS 本周发布了 v21.11 版本，</span>Genode 操作系统框架是一个用于构建高度安全的专用操作系统的工具包，它可以从只有 4MB 内存的嵌入式系统扩展到高度动态的通用工作负载。</p> 
<p>Genode 基于递归系统结构。每个程序都在专门的沙箱中运行，并且仅授予其特定用途所需的访问权限和资源。程序可以利用自己的资源创建和管理子沙箱，从而形成可以在每个级别应用策略的层次结构。该框架提供了让程序相互通信和交换资源的机制，但只能以严格定义的方式进行。由于这种严格的制度，与当代操作系统相比，安全关键功能的攻击面可以减少几个数量级。</p> 
<p><span style="background-color:#ffffff">v21.11 提供了许多硬件改进和其他功能：</span></p> 
<ul> 
 <li>- 供对 Allwinner A64 SoC 的支持，尤其是对 PinePhone 的支持（触摸屏支持和其他功能）。</li> 
 <li>- Genode 的 Intel 图形支持<strong>允许 Skylake/Gen9 和更新版本的图形</strong>。以前 Genode 的开发人员主要绑定从 Linux 移植的代码的 Gen8/Broadwell 图形，现在 Gen9+ 也可以正常工作。（此 Genode 版本使用 Mesa 21.0 和 Intel Iris Gallium3D）</li> 
 <li>- 各种其他 Linux 设备驱动程序处理改进。</li> 
 <li>- 完全支持 VirtaulBox 6。</li> 
 <li>- 继续致力于支持各种 SoC，包括 NXP i.MX。</li> 
 <li>- 除了 x86/x86_64 之外，Sculpt OS 作为 Genode 的通用操作系统，还支持 64 位 ARM。</li> 
 <li>- Genode 的 SDL2 库支持使用 OSS 和 OpenGL 图形支持的音频支持。</li> 
</ul> 
<p>可以在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgenode.org%2Fnews%2Fgenode-os-framework-release-21.11" target="_blank">Genode.org</a> 找到有关 Genode 21.11 版本的更多详细信息。</p>
                                        </div>
                                      
</div>
            