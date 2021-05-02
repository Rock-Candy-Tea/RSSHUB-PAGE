
---
title: 'QEMU 6.0.0 稳定版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/b7a67e57c782dcad6fb936c37a9a3ee38d9.jpg'
author: 开源中国
comments: false
date: Sun, 02 May 2021 07:22:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/b7a67e57c782dcad6fb936c37a9a3ee38d9.jpg'
---

<div>   
<div class="content">
                                                                                            <p>QEMU 6.0.0 已正式 GA。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qemu.org%2F2021%2F04%2F30%2Fqemu-6-0-0%2F" target="_blank">发布公告显示</a>，共有 268 名贡献者为此版本提交了 3300+ commits。</p> 
<p>更新亮点：</p> 
<ul> 
 <li>68k: 基于 virtio 设备的新“虚拟”机器类型</li> 
 <li>ARM: 支持 ARMv8.1-M ‘Helium’ 架构和 Cortex-M55 CPU</li> 
 <li>ARM: 支持 ARMv8.4 TTST, SEL2 和 DIT 扩展</li> 
 <li>ARM: 系统和用户模式模拟支持 ARMv8.5 MemTag 扩展</li> 
 <li>ARM: 支持新的 mps3-an524, mps3-an547 板型号</li> 
 <li>ARM: 对 xlnx-zynqmp, xlnx-versal, sbsa-ref, npcm7xx 和 sabrelite 电路板模型的附加设备仿真支持</li> 
 <li>Hexagon: 高通六角 DSP 单元的新仿真支持</li> 
 <li>MIPS: 支持龙芯 3‘virt’机器类型</li> 
 <li>PowerPC: 对 PowerNV 机器类型的外部 BMC 支持</li> 
 <li>PowerPC: pseries 计算机现在会将内存拔出故障反馈给管理工具，并重试不成功的 CPU 拔出请求</li> 
 <li>RISC-V: Microchip PolarFire 板现在支持 QSPI NOR 闪存</li> 
 <li>Tricore: 支持新的模拟 Infineon TC27x SoC 的 TriBoard 电路板模型</li> 
 <li>x86: AMD SEV-ES 支持以安全的 CPU 寄存器状态运行 guest</li> 
 <li> <p>x86: protection keys (PKS) 的 TCG 仿真支持</p> </li> 
 <li>ACPI: 支持将 NIC 分配给 guest OS 中的已知名称，而与 PCI 插槽的位置无关</li> 
 <li>NVMe: 对 v1.4 规范的新仿真支持，具有许多新功能，包括对分区命名空间 (Zoned Namespaces) 的实验性支持、多路径 I/O 和端到端数据保护</li> 
 <li>virtiofs: 使用新的 USE_KILLPRIV_V2 guest 虚拟机功能提升性能</li> 
 <li>VNC: virtio-vga 支持基于客户端窗口大小的缩放方案</li> 
 <li> <p>QMP: 备份作业现在支持并行的多个异步请求</p> </li> 
 <li> <p>……</p> </li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.qemu.org%2FChangeLog%2F6.0" target="_blank">点此查看完整 Changelog</a>。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qemu.org%2Fdownload%2F%23source" target="_blank">https://www.qemu.org/download/#source</a></p> 
<p>QEMU 由 Fabrice Bellard 创建，是一个纯软件实现的通用模拟器和虚拟机，它有三种模式，几乎可以模拟任何硬件设备：</p> 
<ul> 
 <li>Full-system emulation：可在任何支持的硬件架构上运行任何操作系统</li> 
 <li>User-mode emulation：运行另一个 Linux/BSD 程序</li> 
 <li>Virtualization：接近本机性能运行 KVM 和 Xen 虚拟机</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/b7a67e57c782dcad6fb936c37a9a3ee38d9.jpg" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/27d5b7fb500c62e490f99c23e23a5801218.jpg" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/4972b8dc1f9eec22d147812997d550743b0.jpg" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            