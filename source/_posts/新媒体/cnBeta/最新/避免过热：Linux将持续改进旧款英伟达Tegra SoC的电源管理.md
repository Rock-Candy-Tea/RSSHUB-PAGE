
---
title: '避免过热：Linux将持续改进旧款英伟达Tegra SoC的电源管理'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1026/0a11115c0bf2fce.jpg'
author: cnBeta
comments: false
date: Tue, 26 Oct 2021 07:44:32 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1026/0a11115c0bf2fce.jpg'
---

<div>   
Phoronix 指出：<strong>尽管 Tegra 2 和 Tegra 3 SoC 问世已有十年，但 Linux 主线内核仍在帮助英伟达善后，以解决相关平台设备过热的尴尬。</strong>近段时间，我们已见到热控制代码等工作改进。最新消息是，社区已对 Tegra 电源管理补丁实施第 14 次修订，且正努力让它们被 Linux 5.17 给收录（而不是 Linux 5.16）。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1026/0a11115c0bf2fce.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">Tegra 3“Cardhu”参考平板</p><p>用于明年 Linux 内核的 39 个补丁集，为 Tegra 驱动程序提供了运行时电源管理，且支持在 Tegra20（Tegra 2）和 Tegra30（Tegra 3）SoC 上实现内核电压优化。</p><p>显然，这些补丁的诞生，旨在彻底解决困扰各款 Tegra 设备的过热问题。既然硬件方面难以下手，社区开发者们就普遍选择了通过软件优化来提供“售后”。</p><p>据悉，该<a href="https://lore.kernel.org/lkml/20211025224032.21012-1-digetx@gmail.com/T/#m39fa3f160e7f06c1b07a2e8809c32950457cbb7f" target="_self">系列补丁</a>涉及重新编写的四千多行代码，以按顺序提供对 Tegra 2 和 Tegra 3 运行时的电源管理 / 核心电压优化支持。</p>   
</div>
            