
---
title: 'QEMU 7.0 发布，正式支持 Intel AMX、大幅改进 RISC-V'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1037'
author: 开源中国
comments: false
date: Fri, 22 Apr 2022 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1037'
---

<div>   
<div class="content">
                                                                                            <p>QEMU 是一个免费开源的模拟器，它通过动态二进制翻译来模拟机器的处理器，并为机器提供一套不同的硬件和设备模型，使其能够运行各种客户操作系统。它可以与基于内核的虚拟机（KVM）互操作，以接近原生速度运行虚拟机。QEMU 还可以对用户级进程进行模拟，使为一种架构编译的应用程序能够在另一种架构上运行。</p> 
<p>QEMU 7.0 版本正式推出，这个版本包含了来自 225 位贡献者共 2500 多次提交。</p> 
<p>更新内容包括：</p> 
<ul> 
 <li>ACPI：支持通过 ACPI ERST 接口记录访客事件</li> 
 <li>virtiofs：改进的安全标签支持</li> 
 <li>ARM：'virt' board 支持 virtio-mem-pci、指定访客 CPU 拓扑结构，以及在使用 KVM/hvf 时启用 PAuth</li> 
 <li>ARM："xlnx-versal-virt" board 支持 PMC SLCR 和模拟 OSPI 闪存控制器</li> 
 <li>HPPA：支持多达 16 个 vCPU、为 HP-UX VDE/CDE 环境改进图形驱动、设置 SCSI 启动顺序，以及其他一些新功能</li> 
 <li>OpenRISC：'sim' board 支持多达 4 个核心，加载外部 initrd 映像，并为启动内核自动生成一个 DeviceTree</li> 
 <li>PowerPC：为 XIVE 和 PHB 3/4 改进了 "powernv "模拟，以及对 XIVE2 和 PHB5 的新支持</li> 
 <li>RISC-V：对 KVM 的支持</li> 
 <li>RISC-V：支持批准的 1.0 Vector 扩展，以及 Zve64f、Zve32f、Zfhmin、Zfh、zfinx、zdinx 和 zhinx&#123;min&#125; 扩展</li> 
 <li>RISC-V：'spike' 机器支持 OpenSBI 二进制加载</li> 
 <li>RISC-V：'virt' 机器支持 32 个核心，并支持 AIA</li> 
 <li>s390x：支持 "Miscellaneous-Instruction-Extensions Facility 3"</li> 
 <li>x86: 对英特尔 AMX 的支持</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qemu.org%2F2022%2F04%2F19%2Fqemu-7-0-0%2F" target="_blank">https://www.qemu.org/2022/04/19/qemu-7-0-0/</a></p>
                                        </div>
                                      
</div>
            