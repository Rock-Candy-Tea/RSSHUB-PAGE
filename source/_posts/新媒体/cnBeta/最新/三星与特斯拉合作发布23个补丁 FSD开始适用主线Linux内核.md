
---
title: '三星与特斯拉合作发布23个补丁 FSD开始适用主线Linux内核'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0113/7dfb273b358b41c.jpg'
author: cnBeta
comments: false
date: Thu, 13 Jan 2022 13:13:21 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0113/7dfb273b358b41c.jpg'
---

<div>   
<strong>三星与特斯拉合作发布了一组23个补丁，用于使特斯拉的完全自动驾驶（FSD）SoC适用于主线Linux内核。</strong>这23个补丁使特斯拉的完全自动驾驶SoC能够从上游Linux内核启动，而目前使用的是下游内核构建。<br>
 <p>特斯拉不仅利用Coreboot支持开源的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> GPU Linux驱动，甚至支持将其添加到主线Linux内核中。Tesla FSD SoC支持包括设备树的添加和对内核的各种修改，以提供这种基本支持，该技术主要是建立在现有的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://samsung.jd.com/" target="_blank">三星</a>Exynos SoC驱动路径上。由于利用了内核中现有的三星驱动代码，特斯拉FSD SoC的支持只新增大约3.7万行的新代码。</p><p><a href="https://static.cnbetacdn.com/article/2022/0113/7dfb273b358b41c.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0113/7dfb273b358b41c.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></a></p><p>特斯拉的FSD SoC是在2019年初推出的14纳米SoC，除了12个Cortex-A72内核外，还有一个Mali G71 GPU，两个神经处理单元，以及其他额外的IP块。</p><p>特斯拉FSD SoC对Linux内核的支持目前正在LKML上进行审查，以便可能被纳入未来的主线内核版本。</p><p><strong>了解更多：</strong></p><p><a href="https://lore.kernel.org/lkml/20220113121143.22280-1-alim.akhtar@samsung.com/" _src="https://lore.kernel.org/lkml/20220113121143.22280-1-alim.akhtar@samsung.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="1426242626242525272526252520273a2626262c2439253975787d793a757f7c6075665467757967617a733a777b">[email protected]</span>m/</a><br></p>   
</div>
            