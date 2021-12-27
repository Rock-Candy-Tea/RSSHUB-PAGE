
---
title: 'Linux 5.16-rc7正式发布 圣诞假期令其改进较小'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Sun, 26 Dec 2021 23:19:42 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
Linus Torvalds今天发布了Linux 5.16-rc7，作为最新的每周测试候选版本，而正式的Linux
5.16稳定版应该在两周内发布。由于是圣诞假期期间发布的版本，Linux 5.16-rc7很小，没有大的惊喜。Linus
Torvalds在5.16-rc7公告中指出：<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p>"没有人会感到惊讶，这个rc7的变化是相当小的。统计数字看起来也不出意外：大约四分之三是驱动程序（网络、输入、声音、TEE、HWMON、RDMA...）。有点不寻常的是，我们中间有人修复了一个PC键盘控制器（不是USB，而是旧的传统类型），这意味着最早支持的硬件之一仍然存在，并且仍然得到一些罕见硬件的支持变动。其余的主要是一些kvm和网络的修复，以及其他地方的一些随机零散区域的改进。"</p><p>Linux 5.16还没有围绕x86集群感知调度进行任何修改，以避免5.16中引入的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>Alder Lake性能下降，因此使用新款酷睿处理器的用户要么是通过独立引入补丁，要么是在5.16中直接禁用Alder Lake，或者选择在5.16中将x86集群感知调度默认为完全关闭。</p><p>有许多令人兴奋的Linux 5.16内核功能还暗自持续到来，当这个下一个版本在假期后的1月首次亮相时我们可以看到。</p><p><strong>访问发布公告：</strong></p><p><a href="https://lore.kernel.org/lkml/CAHk-=wgV_v+Enop3TwRFtJY74UjQtw=kfOzGXTQscLx2syW6Eg@mail.gmail.com/T/#u" _src="https://lore.kernel.org/lkml/CAHk-=wgV_v+Enop3TwRFtJY74UjQtw=kfOzGXTQscLx2syW6Eg@mail.gmail.com/T/#u" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="286b69604305155f4f7e775e036d4647581b7c5f7a6e5c62711f1c7d42795c5f15434e67526f707c795b4b64501a5b517f1e6d4f6845494144064f45494144064b">[email protected]</span>om/T/#u</a><br></p>   
</div>
            