
---
title: 'QEMU 6.1 首个 RC 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6679'
author: 开源中国
comments: false
date: Tue, 27 Jul 2021 23:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6679'
---

<div>   
<div class="content">
                                                                                            <p>QEMU 6.1 迎来了首个 RC 版本，为 8 月底前的稳定版亮相做好了准备。</p> 
<p>QEMU 6.1 是在 4 月底发布的<a href="https://www.oschina.net/news/139895/qemu-6-0-0-released"> QEMU 6.0 </a>基础上的又一个重要功能版本。随着 RC 版本的到来，目前 QEMU 6.1 处于硬功能冻结 (hard feature freeze) 状态。</p> 
<p>官方表示在正式发布之前，每周都会有候选版本的更新，预计 QEMU 6.1. 将于 8 月中下旬完成。</p> 
<p>QEMU 6.1 的变化包括：</p> 
<ul> 
 <li>在 PowerPC 上大幅增加最大 CPU 数量的支持，用户有可能在受到 QEMU 的限制之前遇到其他的系统限制</li> 
 <li>QEMU 上的 RISC-V 有围绕 OpenTitan 平台支持的更新，对 VirtIO VGA 的支持，以及其他多种架构的改进</li> 
 <li>在 Tiny Code Generator (TCG) 内为 POWER10 的支持进行了许多工作</li> 
 <li>对更多 Arm CPU 特性的仿真支持，包括 SVE2 和 BFloat16 等</li> 
 <li>x86 上的 QEMU 6.1 增加了启用 XSAVES 的新 CPU 模型版本、允许 guest 帐户对总线锁定进行速率限制的新机器选项以及其他更改</li> 
 <li>QEMU 的 virtio-mem 现在可以与 VFIO 搭配使用</li> 
 <li>弃用旧的 CPU target，包括 Moxie、lm32 和 unicore32</li> 
</ul> 
<p>更多细节查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.nongnu.org%2Farchive%2Fhtml%2Fqemu-devel%2F2021-07%2Fmsg05754.html" target="_blank">发布公告</a>和 QEMU Wiki 上的临时<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.qemu.org%2FChangeLog%2F6.1" target="_blank"> Changelog</a>。</p>
                                        </div>
                                      
</div>
            