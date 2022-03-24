
---
title: 'QEMU 7.0 新特性预览：支持 Intel AMX、针对 ARM 架构的改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9584'
author: 开源中国
comments: false
date: Thu, 24 Mar 2022 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9584'
---

<div>   
<div class="content">
                                                                    
                                                        <p>QEMU 7.0 首个 RC 版本已发布，正式版计划于 4 月中旬推出。QEMU 7.0 特别增加了对 Intel AMX 的支持，此特性有助于 Linux KVM 对 Intel Advanced Matrix Extensions 的支持，目前已准备合并到主线。7.0 版本在 RISC-V 架构支持方面也完成了不少工作，此外还有多项其他变化。</p> 
<p><strong>主要新特性一览</strong></p> 
<ul> 
 <li>针对 ARM 架构的改进：引入新<span style="color:#121212">的 </span>mori-bmc board model、支持模拟其他功能<span style="color:#121212">以及改进 </span>virt board</li> 
 <li>OpenRISC 现在最多支持 4 个内核（此前 2 个内核已经是极限）。OpenRISC 代码现在还可以自动生成 DeviceTree 并将其传递给内核</li> 
 <li>放弃支持 PowerPC 401 / 403 / 601 / 602 CPU</li> 
 <li>QEMU Tiny Code Generator (TCG) 不再支持 ARMv4 和 ARMv5 主机</li> 
 <li>RISC-V 上的 QEMU 现在支持获批准的 Vector 1.0 扩展以及 Zve64f、Zve32f 等其他新扩展</li> 
 <li>近期在 Linux 内核主线中进入上游的 RISC-V KVM 支持现在由 QEMU 提供底层支持</li> 
 <li>改进 QEMU for RISC-V：默认启用管理程序扩展和对 128 位 CPU 的实验性支持</li> 
 <li>添加对 Intel AMX 的支持</li> 
 <li>9pfs 代码现在支持 macOS 主机</li> 
 <li>HPPA target 现在可以支持多达 16 个 vCPU</li> 
 <li>QEMU 7.0 添加了一个"-display dbus"选项，可使用基于 gtk4-rs Rust 的 GTK4 查看器导出外部进程的显示，此功能用于未来版本的 GNOME Boxes 和 virt-viewer</li> 
 <li>支持更灵活的 fleecing 备份</li> 
 <li>在"guest-get-osinfo"命令中支持 Microsoft Windows 11</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.qemu.org%2FChangeLog%2F7.0" target="_blank">详情点此查看</a>。</p>
                                        </div>
                                      
</div>
            