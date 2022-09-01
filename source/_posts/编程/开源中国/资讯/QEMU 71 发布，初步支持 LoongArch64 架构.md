
---
title: 'QEMU 7.1 发布，初步支持 LoongArch64 架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6683'
author: 开源中国
comments: false
date: Thu, 01 Sep 2022 07:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6683'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">QEMU 是一个免费开源的模拟器，它通过动态二进制翻译来模拟机器的处理器，并为机器提供一套不同的硬件和设备模型，使其能够运行各种客户操作系统。它可以与基于内核的虚拟机（KVM）互操作，以接近原生速度运行虚拟机。QEMU 还可以对用户级进程进行模拟，使为一种架构编译的应用程序能够在另一种架构上运行。</span></p> 
<p>QEMU 7.1 发布了，此版本的<span style="color:#333333">新特性</span>包括初始支持 64 位 LoongArch 作为新的 CPU 架构、支持多个新的 RISC-V 扩展、支持新的 Arm CPU 功能：</p> 
<ul> 
 <li>实时迁移：支持 Linux 上的零复制发送</li> 
 <li>QMP：通过“block-export-add”命令导出带有脏位图的 NBD 图像的新选项</li> 
 <li>QMP：新的“query-stats”和“query-stats-schema”命令，用于从各种 QEMU 子系统中检索统计信息</li> 
 <li>QEMU 来宾代理：改进了 Solaris 支持，新命令“guest-get-diskstats”/“guest-get-cpustats”，“guest-get-disks”现在报告 NVMe SMART 信息，“guest-get-fsinfo”现在报告 NVMe总线型</li> 
 <li>ARM：对新机器类型的仿真支持：Aspeed AST1030 SoC、Qaulcomm 和 fby35 (AST2600 / AST1030)</li> 
 <li>ARM：对 Cortex-A76 和 Neoverse-N1 CPU 的仿真支持</li> 
 <li>ARM：对可扩展矩阵扩展、缓存推测控制、RAS 和许多其他 CPU 扩展的仿真支持</li> 
 <li>ARM：“virt”板现在支持模拟 GICv4.0</li> 
 <li>HPPA：新的 SeaBIOS v6 固件，在使用 GTK UI 运行时支持启动菜单中的 PS/2 键盘、改进的串行端口仿真和额外的 STI 文本字体</li> 
 <li><strong>LoongArch：初步支持 LoongArch64 架构、龙芯 3A5000 多处理器 SoC 和龙芯 7A1000 主机桥</strong></li> 
 <li>MIPS：Nios2 板（-machine 10m50-ghrd）现在支持向量中断控制器、影子寄存器集和改进的异常处理</li> 
 <li>OpenRISC：“or1k-sim”机器现在支持 4 个 16550A UART 串​​行设备，而不是 1 个</li> 
 <li>RISC-V：支持特权规范版本 1.12.0 的新 ISA 扩展、对 MIP SEIP 的软件访问、Sdtrig 扩展、矢量扩展改进、本机调试、PMU 改进以及许多其他功能和杂项修复/改进</li> 
 <li>RISC-V：“virt”板现在支持 TPM</li> 
 <li>RISC-V：“OpenTitan”板现在支持 Ibex SPI</li> 
 <li>s390x：s390x Vector-Enhancements Facility 2 的仿真支持</li> 
 <li>s390x：s390-ccw BIOS 现在支持从非 512 扇区大小的驱动器启动</li> 
 <li>x86：架构 LBR 的虚拟化支持</li> 
 <li>Xtensa：支持 lx106 内核和缓存测试操作码</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qemu.org%2F2022%2F08%2F30%2Fqemu-7-1-0%2F" target="_blank">https://www.qemu.org/2022/08/30/qemu-7-1-0/</a></p>
                                        </div>
                                      
</div>
            