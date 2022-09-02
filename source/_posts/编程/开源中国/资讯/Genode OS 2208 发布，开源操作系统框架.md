
---
title: 'Genode OS 22.08 发布，开源操作系统框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8a843aa099de9b92190bc8df4bafa45fcc8.png'
author: 开源中国
comments: false
date: Thu, 01 Sep 2022 23:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8a843aa099de9b92190bc8df4bafa45fcc8.png'
---

<div>   
<div class="content">
                                                                                            <p>Genode OS 22.08 已正式发布。</p> 
<blockquote> 
 <p>Genode 操作系统框架是一个用于构建高度安全的专用操作系统的工具包。它可以从只有 4MB 内存的嵌入式系统扩展到高度动态的通用工作负载。</p> 
 <p>Genode 基于递归系统结构。每个程序都在专门的沙箱中运行，并且仅授予其特定用途所需的访问权限和资源。程序可以利用自己的资源创建和管理子沙箱，从而形成可以在每个级别应用策略的层次结构。该框架提供了让程序相互通信和交换资源的机制，但只能以严格定义的方式进行。由于这种严格的制度，与当代操作系统相比，安全关键功能的攻击面可以减少几个数量级。</p> 
 <p>该框架将 L4 的构建原则与 Unix 哲学保持一致。根据 Unix 哲学，Genode 是一组小型构建块的集合，从中可以组成复杂的系统。但与 Unix 不同的是，这些构建块不仅包括应用程序，还包括所有经典的操作系统功能，例如内核、设备驱动程序、文件系统和协议栈。</p> 
 <p><strong>特性</strong></p> 
 <ul> 
  <li> <p>CPU 架构：x86（32 和 64 位）、ARM（32 和 64 位）、RISC-V</p> </li> 
  <li> <p>内核：L4 家族的大多数成员（<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fhypervisor.org%2F">NOVA</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsel4.systems%2F">seL4</a>、 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fos.inf.tu-dresden.de%2Ffiasco%2F">Fiasco.OC</a>、 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fokl4.org%2F">OKL4 v2.1</a>、 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.l4ka.org%2F65.php">L4ka::Pistachio</a>、 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fos.inf.tu-dresden.de%2Ffiasco%2Fprev%2F">L4/Fiasco</a>）、Linux 和自定义内核。</p> </li> 
  <li> <p>虚拟化：VirtualBox（基于 NOVA）、ARM 的自定义虚拟机监视器和 Unix 软件的自定义运行时</p> </li> 
  <li> <p>超过 100 个随时可用的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgenode.org%2Fdocumentation%2Fcomponents">组件</a></p> </li> 
 </ul> 
</blockquote> 
<p>本次更新的一大重点是<strong>使 Genode OS 作为一个智能手机操作系统更加实用</strong>。</p> 
<p>附带 SculptOS 通用操作系统的 Genode OS 将目光投向了作为手机操作系统运行。特别是，迄今为止的大部分工作都集中在让 Genode OS/Sculpt 在 PinePhone 上运行良好。</p> 
<p>团队在发布公告中<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgenode.org%2Fnews%2Fgenode-os-framework-release-22.08" target="_blank">写道</a>：</p> 
<blockquote> 
 <p>自从我们为 PC 创建 Sculpt OS 以来，基于 Genode 的智能手机的愿景无疑是我们最雄心勃勃的事业。在过去的两年里，我们在瞄准 PinePhone 硬件的同时，不懈地追求这一愿景。工作范围从系统控制处理器的定制固件，到内核开发、种类繁多的设备驱动程序，再到用户界面和应用程序级别。在 Genode 22.08 中，这些努力最终形成了第一个完整的系统——Sculpt OS 的手机变体。</p> 
</blockquote> 
<p>Genode OS 及其 Sculpt OS 在移动设备方面的工作一直是使用语音通话功能、使用 Morph 进行移动互联网浏览等。他们一直致力于改进在 PinePhone 上运行的各种底层硬件支持，以及改进堆栈以确保应用程序可以工作。</p> 
<p>作为硬件工作的一部分，他们还将 Lima 开源 Arm Mali 400 驱动程序从 Linux 移植到了 Genode。他们已经使用 GPU 加速运行了基本的 GLMark2 测试用例，他们的 Lima 驱动程序支持将改善他们的 Morph Web 浏览器体验。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-8a843aa099de9b92190bc8df4bafa45fcc8.png" referrerpolicy="no-referrer"></p> 
<p><span><span><span><span><span><span><span><span><span><span><span><span style="color:#121212"><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><em>Genode OS 展示了移植 Ubuntu Touch UI 以在 Genode 上运行。</em></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgenode.org%2Fdocumentation%2Frelease-notes%2F22.08" target="_blank">Release Note</a></p>
                                        </div>
                                      
</div>
            