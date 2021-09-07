
---
title: 'Genode 21.08 正式发布，开源操作系统框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3841'
author: 开源中国
comments: false
date: Tue, 07 Sep 2021 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3841'
---

<div>   
<div class="content">
                                                                                            <p>Genode 21.08 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgenode.org%2Fnews%2Fgenode-os-framework-release-21.08" target="_blank">发布</a>。</p> 
<blockquote> 
 <p>Genode 操作系统框架是一个用于构建高度安全的专用操作系统的工具包。它可以从只有 4MB 内存的嵌入式系统扩展到高度动态的通用工作负载。</p> 
 <p>Genode 基于递归系统结构。每个程序都在专门的沙箱中运行，并且仅授予其特定用途所需的访问权限和资源。程序可以利用自己的资源创建和管理子沙箱，从而形成可以在每个级别应用策略的层次结构。该框架提供了让程序相互通信和交换资源的机制，但只能以严格定义的方式进行。由于这种严格的制度，与当代操作系统相比，安全关键功能的攻击面可以减少几个数量级。</p> 
 <p>该框架将 L4 的构建原则与 Unix 哲学保持一致。根据 Unix 哲学，Genode 是一组小型构建块的集合，从中可以组成复杂的系统。但与 Unix 不同的是，这些构建块不仅包括应用程序，还包括所有经典的操作系统功能，例如内核、设备驱动程序、文件系统和协议栈。</p> 
 <p>特性</p> 
 <ul> 
  <li> <p>CPU 架构：x86（32 和 64 位）、ARM（32 和 64 位）、RISC-V</p> </li> 
  <li> <p>内核：L4 家族的大多数成员（<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fhypervisor.org%2F" target="_blank">NOVA</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsel4.systems%2F" target="_blank">seL4</a>、 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fos.inf.tu-dresden.de%2Ffiasco%2F" target="_blank">Fiasco.OC</a>、 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fokl4.org%2F" target="_blank">OKL4 v2.1</a>、 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.l4ka.org%2F65.php" target="_blank">L4ka::Pistachio</a>、 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fos.inf.tu-dresden.de%2Ffiasco%2Fprev%2F" target="_blank">L4/Fiasco</a>）、Linux 和自定义内核。</p> </li> 
  <li> <p>虚拟化：VirtualBox（基于 NOVA）、ARM 的自定义虚拟机监视器和 Unix 软件的自定义运行时</p> </li> 
  <li> <p>超过 100 个随时可用的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgenode.org%2Fdocumentation%2Fcomponents" target="_blank">组件</a></p> </li> 
 </ul> 
</blockquote> 
<p>更新亮点：</p> 
<ul> 
 <li>改进对 CPU 的支持</li> 
 <li>改进 VirtualBox</li> 
 <li>支持原生 Web 浏览器中的媒体播放</li> 
 <li>支持 Sculpt OS 中的 LTE 连接</li> 
 <li>简化移植方法</li> 
 <li>改进对英特尔 GPU 的支持</li> 
</ul> 
<p><strong>简化移植方法</strong></p> 
<p>Genode 21.08 引入精简的移植方法能够大大减少成本，创造更广泛的硬件支持。新移植方式的第一个成功案例是为 Pinephone 和 MNT-Reform 笔记本电脑增加了图形驱动，为 Pine-A64-LTS 板增加了网络驱动，为 MNT-Reform 增加了 SD 卡驱动。</p> 
<p>Genode 21.08 的第二个更新亮点是对英特尔 GPU 的支持进行了大幅度的修改。跟过去与 GPU 相关的实验性工作相比，新版本找到了一种方法，可以将 GPU 支持干净地整合到复杂的 Genode 系统的 GUI 架构中（如 Sculpt OS）。</p> 
<p>除了上述的变化，Genode 还在改进其缓存维护 (cache-maintenance) 接口，改进 Genode/Linux 上的主机文件系统访问，改进 libuvc 的网络摄像头支持。另外，QEMU 的 RAM 帧缓冲器驱动程序现在可用于测试，以及开始逐步淘汰废弃的组件。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgenode.org%2Fnews%2Fgenode-os-framework-release-21.08" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            