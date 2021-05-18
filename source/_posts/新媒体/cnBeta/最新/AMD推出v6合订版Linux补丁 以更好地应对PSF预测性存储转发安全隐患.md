
---
title: 'AMD推出v6合订版Linux补丁 以更好地应对PSF预测性存储转发安全隐患'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0518/2a5d69e60243615.jpg'
author: cnBeta
comments: false
date: Tue, 18 May 2021 07:40:46 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0518/2a5d69e60243615.jpg'
---

<div>   
距离 AMD 发布有关 Zen 3“预测性存储转发”（简称 PSF）功能的安全性分析，已经过去一个半月。<strong>尽管从理论上来讲，该功能有助于有助于提升系统的整体性能。但与此同时，它也容易引发新的侧信道攻击。</strong>于是在安全白皮书发布后几天，AMD 就推出了允许选择性禁用 PSF 功能的 Linux 修补程序。不过 AMD 的相关工作仍在进行中，且尚未成为大多数人的选择。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/0518/2a5d69e60243615.jpg" alt="AMD CPU.jpg" referrerpolicy="no-referrer"></p><p>好消息是，截止本周一，我们已经迎来了六轮相关补丁程序，以便用户能够轻松控制 PSF 功能的开闭。</p><p>随着合并工作的顺利推进，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Zen 3 的 CPU PSF“缓解”（mitigation）补丁也正式更名为“控件”（control）。</p><blockquote><p>此外最新版 Linux 补丁修复了一些 MSR 寄存处的处理操作，简化了 PSF 应对操作，并将内核参数更改为具有可接受值的 predictive_store_fwd_disable = 。</p><p>如果选择了‘on’，则意味着引导将禁用 AMD Zen 3 处理器（包括锐龙 5000 / 霄龙 7003 系列）的预测性存储转发功能。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2021/0518/7b0b9b14dfc0c66.jpg" alt="AMD PSF.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：AMD | <a href="https://www.amd.com/system/files/documents/security-analysis-predictive-store-forwarding.pdf" target="_self">PDF</a>）</p><p>鉴于本次修补程序（<a href="https://lore.kernel.org/lkml/20210517220059.6452-1-rsaripal@amd.com/" target="_self">传送门</a>）的发布时间已经越过了 Linux 5.13 合并窗口，目前尚不清楚 AMD 是否会尝试在本周期中将之作为“安全修复程序”而向主流用户推送，还是等到下一个（Linux 5.14）合并窗口再完全整合进去。</p>   
</div>
            