
---
title: '时隔多年 Android 13终于原生支持exFAT驱动器'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0620/4144cdc055767c4.jpg'
author: cnBeta
comments: false
date: Mon, 20 Jun 2022 07:29:14 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0620/4144cdc055767c4.jpg'
---

<div>   
<strong>随着 Android 13 的到来，Google Pixel 系列移动设备用户，也终于能够原生处理 exFAT 磁盘上大于 4GB 的单个文件了。</strong>Esper 科技编辑 Mishaal Rahman 偶然间发现，在将手头的 Pixel 6 Pro 智能机从 Android 12L 升级到 Android 13 之后，系统终于迎来了对可扩展文件分配表（exFAT）的支持。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0620/4144cdc055767c4.jpg" alt="Android 13 exFAT.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：esper <a href="https://blog.esper.io/android-dessert-bites-27-exfat-on-pixel-532176849/" target="_self">blog</a>）</p><p>Android Police 补充道：变化发生在 Linux 5.10+ 内核上运行的 Android 版本，即从 Android 12L（5.10.81-android12-9）到 5.10.107-android13-4 期间。</p><p>如果曾尝试在一台 Google Android 设备上使用过 exFAT 驱动器，应该不会对此感到陌生。</p><p>事实上，自<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>于 2006 年推出以来，许多 OEM 硬件厂商都在默默为此付费 —— 比如<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://samsung.jd.com/" target="_blank">三星</a>就开发了一个 back-pocket exFAT 驱动程序。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0620/2edfd049269b6fd.webp" alt="2.webp" referrerpolicy="no-referrer"></p><p>好消息是，随着微软于 2019 年公开鼓励将 exFAT 支持集成到 Linux 中，内核社区就开始了积极地拥抱它。而三星的 exFAT 驱动，也最终被改头换面、并融入了 Linux 5.7 。</p><p>遗憾的是，期间 Android 内核与下游开发人员并没有想要那么快地跳转版本，而是更愿意对特定版本提供长期支持、以确保平台体验的稳定。</p><p>自那时起，Google 维护的 Android Common Kernel 长时间都基于 Linux 5.4 —— 直到 5.10 才形成了一个新的分支。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0620/f7e7210b5cff7dd.webp" alt="3.webp" referrerpolicy="no-referrer"></p><p>既然基于 Linux 5.10 内核的 Android 12 设备在技术层面上已支持挂载 / 卸载 exFAT 分区，那为何运行 Android 12L 的 Pixel 6 Pro 又被拦着无法读取 exFAT 驱动器呢？</p><p>原因在于，exFAT 的挂载服务（vold / 卷守护进程）会检查它是否可以访问几个特定的“帮助”二进制文件。如果它们不存在，则挂载服务就无法通过检查并正常工作。</p><p><img src="https://static.cnbetacdn.com/article/2022/0620/ea7343a89560c87.webp" alt="4.webp" referrerpolicy="no-referrer"></p><p>不管怎样，我们现在至少已确认这样的调用存在于 Android 13 大版本中 —— 更确切地说，至少一个自定义内核开发者已能够修补 exFAT 驱动程序的二进制检查，因而理论上可将至向后移至到较旧的 Android 版本中。</p><p>最后，一旦 Google 在 Android 13 上正式完成了部署，其它 OEM 厂商也将能够直接受益于 Android 开源项目（AOSP）的 esFAT 支持。</p>   
</div>
            