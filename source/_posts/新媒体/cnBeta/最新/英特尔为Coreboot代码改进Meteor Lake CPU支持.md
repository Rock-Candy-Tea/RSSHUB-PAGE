
---
title: '英特尔为Coreboot代码改进Meteor Lake CPU支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0609/6203f537a9367d3.webp'
author: cnBeta
comments: false
date: Thu, 09 Jun 2022 08:03:58 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0609/6203f537a9367d3.webp'
---

<div>   
过去几年，以 AMD、Intel、NVIDIA 为代表的芯片制造商，经常会在新品正式上市前几年，就于 Linux 内核代码中被扒出一些线索。<strong>最新消息是，Phoronix 刚刚在 Coreboot 代码工作中，看到了接替 13 代 Raptor Lake 处理器的 Raptor Lake CPU 的身影。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0609/6203f537a9367d3.webp" alt="1.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">英特尔 Fab 42 工厂里的测试芯片（图 via Cnet）</p><p>WCCFTech 指出：英特尔第 14 代酷睿处理器将采用 Intel 4 制程、并过渡到堆叠式平铺架构。</p><p>而在英特尔工程师为 Linux 带来的最新 Coreboot 补丁中，我们就看到了 Meteor Lake CPU 的身影。</p><blockquote><p>Coreboot 曾被叫做 LinuxBIOS，该应用程序项目致力于用‘轻量级固件’，替换大多数计算机系统中的专有固件（UEFI BIOS）。</p><p>该固件专为在现代 32 / 64-bit 操作系统上，加载和处理所必须的最少任务而开发。</p></blockquote><p>本周早些时候，英特尔 Coreboot 开源固件项目合并到了最初的 Meteor Lake SoC 支持代码中。</p><p>其实早在去年，我们就已经看到过几项“Meteor Lake”的补丁发生了变化。尤其是当前的 Linux 驱动程序，需要新的 ID 来支持 14 代酷睿。</p><p><img src="https://static.cnbetacdn.com/article/2022/0609/64bcd17ca2e3c92.png" alt="2.png" referrerpolicy="no-referrer"></p><p>本次更新的固件支持包（FSP），为 Linux 中现有的 Meteor Lake 支持又带来了一些补充。</p><p>此前一些未与该公司取得合作的开源开发者，曾提议英特尔通过修改 FSP 让软件开源（或允许其它形式的变更），以获得更多开放的兼容性与功能。</p><p>截至目前，这家芯片巨头尚未回应其它开发商的需求，但我们会持续关注这个故事的未来发展。</p><p>感兴趣的朋友，可移步至 GitHub 上的 Coreboot 专题页面（<a href="https://github.com/coreboot/coreboot/commit/b8224f48feb9c2967e22993b630ad1c6a835b241" target="_self">传送门</a>），以获知本次代码修订提交的更多细节。</p>   
</div>
            