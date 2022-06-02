
---
title: '开源操作系统框架 Genode OS 发布 22.05 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0602/070517_16zz_4937141.png'
author: 开源中国
comments: false
date: Thu, 02 Jun 2022 07:05:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0602/070517_16zz_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>Genode 操作系统框架是一个用于构建高度安全的专用操作系统的工具包，从嵌入式设备扩展到动态通用计算。</p> 
<p>Genode 基于递归系统结构。每个程序都在专门的沙箱中运行，并且仅授予其特定用途所需的访问权限和资源。该框架提供了让程序相互通信和交换资源的机制，但只能以严格定义的方式进行。由于这种严格的制度，与当代操作系统相比，Genode 在安全关键功能的攻击面可以减少几个数量级。</p> 
<p>目前 Genode OS 发布了 v22.05 版本，该版本引入了一个基于 WireGuard 协议的派生 VPN 组件，这足以让 Sculpt OS 支持 WireGuard，此举实现了他们在 WireGuard 虚拟专用网络支持方便的路线图之一。</p> 
<p><img height="556" src="https://static.oschina.net/uploads/space/2022/0602/070517_16zz_4937141.png" width="750" referrerpolicy="no-referrer"></p> 
<p>另一方面，Genode OS 继续利用 Linux 设备驱动程序，在这个原始操作系统下扩展 PC 硬件支持，该版本引入了围绕 WiFi、Intel 显示/图形驱动程序和其他源自 Linux 5.14.21 内核的组件。</p> 
<p>该版本还有 PCI 改进、改进的触摸事件支持、对 Genode 的 PinePhone 端口的初始电话支持，以及各种其他改进。具体内容可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgenode.org%2Fdocumentation%2Frelease-notes%2F22.05" target="_blank">发布公告</a>中查看。</p> 
<p> </p>
                                        </div>
                                      
</div>
            