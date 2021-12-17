
---
title: 'QEMU 6.2 正式发布，支持 Apple Silicon 和更多 RISC-V 指令'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8168'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 07:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8168'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">QEMU 是一个免费开源的管理程序。它通过动态二进制转换来模拟机器的处理器，并为机器提供一套不同的硬件和设备模型，使其能够运行各种客户操作系统。它可以与基于内核的虚拟机（KVM）互操作，以接近原生速度运行虚拟机。QEMU 还可以对用户级进程进行模拟，使得为一种架构编译的应用程序能够在另一种架构上运行。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">QEMU 6.2 带来的变化和改进包括：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>针对 "powernv" 机器改进了 POWER10 的支持</li> 
 <li>增加了对 POWER10 DD2.0 CPU 的初步支持</li> 
 <li>PowerPC 的维护者由 David Gibson 和 Greg Kurz 变更为 Cédric le Goater 和 Daniel Henrique Barboza</li> 
 <li>结合功能强大的 KVM，现在在虚拟机中支持 Intel SGX（软件保护扩展）</li> 
 <li>在配备 Apple Silicon SoC 的 macOS 机器上，QEMU 现在支持 HVF 加速器，用于运行 AArch64 客户机</li> 
 <li>QEMU 的微型代码生成器 TCG 现在支持富士通 A64FX 高性能 ARM 处理器</li> 
 <li>支持更多 RISC-V 指令、支持 SiFive PWM，以及处理此开源处理器 ISA 的其他改进</li> 
 <li>改进 IBM POWER10 支持</li> 
 <li>添加了 Intel Snow Ridge v4 CPU 模型</li> 
 <li>已弃用的机器名称 'raspi2' 和 'raspi3' 已被删除；使用 'raspi2b' 和 'raspi3b' 代替</li> 
 <li>'virt' 机器现在支持模拟的 ITS</li> 
 <li>pl011 UART 模型现在支持发送 "break"</li> 
 <li>xlnx-zcu102 和 xlnx-versal-virt 机器现在支持 BBRAM 和 eFUSE 设备</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.qemu.org%2FChangeLog%2F6.2" target="_blank">https://wiki.qemu.org/ChangeLog/6.2</a></p>
                                        </div>
                                      
</div>
            