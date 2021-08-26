
---
title: 'QEMU 6.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/b7a67e57c782dcad6fb936c37a9a3ee38d9.jpg'
author: 开源中国
comments: false
date: Thu, 26 Aug 2021 07:23:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/b7a67e57c782dcad6fb936c37a9a3ee38d9.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p>QEMU 6.1.0 已正式发布，总共有 221 名贡献者为此版本提交了 3000+ commit。</p> 
<p>更新亮点：</p> 
<ul> 
 <li>block：支持通过 ‘blockdev-reopen’ QMP 命令创建 block 后再变更 block 节点选项</li> 
 <li>Crypto：优化文档，以及提升后端建议的性能</li> 
 <li>I2C：支持模拟 I2C muxes (pca9546, pca9548) 和 PMBus</li> 
 <li>TCG Plugins：默认启用 TCG 插件，并提供了新的 execlog 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qemu.org%2F2021%2F08%2F19%2Ftcg-cache-modelling-plugin%2F" target="_blank">cache modelling</a> 插件</li> 
 <li>ARM：针对基于 Aspeed (rainier-bmc, quanta-q7l1), npcm7xx (quanta-gbs-bmc) 和 Cortex-M3 (stm32vldiscovery) 机器的新板卡支持</li> 
 <li>ARM：对哈希和加密引擎的 Aspeed 支持</li> 
 <li>ARM：支持模拟更多的 Arm CPU 功能，例如模拟 SVE2（包括 bfloat16）、整数矩阵乘法累加运算等</li> 
 <li>PowerPC: pseries：支持在较新的 guest 中检测热插拔故障</li> 
 <li>PowerPC: pseries：增加最大 CPU 数量</li> 
 <li>PowerPC: pseries：支持模拟部分 POWER10 前缀指令</li> 
 <li>PowerPC: new board support for Genesi/bPlan Pegasos II (pegasos2)</li> 
 <li>RISC-V：升级对 OpenTitan 平台的支持，包括 OpenTitan 定时器</li> 
 <li>RISC-V：支持 virtio-vga</li> 
 <li>RISC-V：优化文档，以及常规的代码清理和修复</li> 
 <li>s390：支持模拟矢量增强设施 (vector-enhancements facility)</li> 
 <li>s390：支持 gen16 CPU models</li> 
 <li>x86：新的英特尔 CPU model 版本支持 XSAVES 指令</li> 
 <li>x86：为 Q35 机器添加基于 ACPI 的 PCI 热插拔支持（现在是默认状态）</li> 
 <li>x86：改进对 AMD 虚拟化扩展的模拟</li> 
 <li>……</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.qemu.org%2FChangeLog%2F6.1" target="_blank">点此查看完整 Changelog</a>。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qemu.org%2Fdownload%2F" target="_blank">https://www.qemu.org/download/</a></p> 
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
            