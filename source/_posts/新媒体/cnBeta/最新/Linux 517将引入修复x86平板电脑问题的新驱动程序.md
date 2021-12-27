
---
title: 'Linux 5.17将引入修复x86平板电脑问题的新驱动程序'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1227/921cf5830684494.png'
author: cnBeta
comments: false
date: Mon, 27 Dec 2021 08:23:22 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1227/921cf5830684494.png'
---

<div>   
在下一轮 Linux 5.17 内核更新周期中，<strong>开发团队计划引入一个名为“x86-android-tablets”的驱动程序，以解决与平板电脑有关的一些问题和无法正常运行的缺陷。</strong>近年来，红帽长期开发者 Hans de Goede 一直在负责这方面的事务，以及其它与桌面相关的改进。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1227/921cf5830684494.png" referrerpolicy="no-referrer"></p><p>他表示，作为 ACPI 差分系统描述表（DSDT）的一部分，许多 x86 平板电脑仅存在无效条目和其它问题。但当尝试在所述硬件上运行主线 Linux 时，仍会导致遇到一些问题。</p><p>好消息是，Hans de Goede 现已将自己编写的 x86-android-tablets 驱动程序排入 x86 平台的驱动程序树，以缓和 x86（主要是 Android）平板电脑的混乱局面。</p><p>他解释称，作为目前在 platform-drivers-x86 “for-next” 分支中<a href="https://git.kernel.org/pub/scm/linux/kernel/git/pdx86/platform-drivers-x86.git/commit/?h=for-next&id=55fa3c9665bfcf32b21af8ecdeb48d5c5177d8d7" target="_self">提交</a>的一部分，x86 Android 平板电脑的出厂镜像往往存在各种问题。</p><p>通常预装内核会被放到这些设备中带有硬编码的设备地址和 GPIO，而不是在 DSDT 中指定。差分系统描述表中包含了随机的设备集合，但它们可能存在或不存在。</p><p>好消息是，即将到来的新驱动程序，仅在基于 DMI 匹配的受影响机型上加载，以期修复电池监控、触摸板、加速度计不工作等问题。</p><p>如此一来，在作为模块构建时，我们也无需向主内核映像（vmlinuz）添加任何额外的代码 —— 比如驰为 Hi8 这款<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> x86 平板电脑。</p>   
</div>
            