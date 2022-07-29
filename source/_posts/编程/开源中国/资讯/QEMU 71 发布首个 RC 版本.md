
---
title: 'QEMU 7.1 发布首个 RC 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3008'
author: 开源中国
comments: false
date: Fri, 29 Jul 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3008'
---

<div>   
<div class="content">
                                                                                            <p>QEMU 7.1 首个 RC 版本已发布，稳定版计划在几周后推出。RC 意味着已进入“功能冻结”阶段，即不会增加或删减功能。按照发布计划，在 8 月底推出稳定版之前，每周都会发布 RC 更新。</p> 
<p>QEMU 7.1 带来了对 LoongArch 的支持、大量新的 RISC-V 扩展，以及多项功能增强。</p> 
<p><strong>主要变化</strong></p> 
<ul> 
 <li>支持模拟更多 Arm CPU 指令集特性。在 Arm 前端，还支持模拟 Cortex-A76 和 Neoverse-N1 target。</li> 
 <li>初步支持龙芯 3A5000 系列 SoC 的 LoongArch 64 位 CPU 架构。</li> 
 <li>支持 RISC-V 特权规范 (privileged spec) 1.12 版本、改进 PMU 实现、支持 Zmmul 扩展，以及改进多项 RISC-V 架构，和启用其他新的扩展。</li> 
 <li>x86 上的 QEMU 7.1 现在增加了对 KVM VM 上的架构 LBR 的支持。</li> 
 <li>对于 QEMU 迁移场景，现在支持在 Linux 上进行零复制发送 (zero-copy-send)，以降低源主机上的 CPU 使用率。</li> 
 <li>在 QEMU 守护程序 (guest agent) 代码中改进对 Solaris 的支持。</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.qemu.org%2FChangeLog%2F7.1" target="_blank">详情</a>。</p>
                                        </div>
                                      
</div>
            