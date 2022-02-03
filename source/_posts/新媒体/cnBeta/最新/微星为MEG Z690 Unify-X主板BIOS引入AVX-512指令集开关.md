
---
title: '微星为MEG Z690 Unify-X主板BIOS引入AVX-512指令集开关'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0203/9394f1dfbdee0e0.png'
author: cnBeta
comments: false
date: Thu, 03 Feb 2022 04:18:17 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0203/9394f1dfbdee0e0.png'
---

<div>   
<strong>上月早些时候，有报道称英特尔将强制主板制造商禁用 Alder Lake 处理器的 AVX-512 指令集。</strong>虽然官方没有透露是否“意外启用了 AVX-512 支持”，但消费者似乎仍可通过禁用 Gracemont 节能核心（E 核）、让 Golden Cove 高性能核心（P 核）可以用上 AVX-512 指令集。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0203/9394f1dfbdee0e0.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">与标准的 AVX2 指令集相比，AVX-512 的性能与效率表现要略高一些。</p><p>虽然节能 E 核在多线程工作负载中具有一定的优势，但 AVX-512 支持仍有望使 12 代 Alder Lake 处理器成为入门级服务器 / 工作站的一个不错选择。</p><p>奇怪的是，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>似乎不希望这种情况发生，所以很快就敦促主板合作伙伴“最好从主板 BIOS 中剔除对 AVX-512 指令集的支持”。</p><p><img src="https://static.cnbetacdn.com/article/2022/0203/d00b5769a57884e.png" alt="2.png" referrerpolicy="no-referrer"></p><p>有趣的是，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">微星</a>（<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">MSI</a>）似乎仍在 MEG Z690 Unify-X 上保留了这项功能，允许用户通过微码选择，启用 Alder Lake 处理器上的 AVX-512 支持。</p><p><a href="https://www.igorslab.de/en/intel-deactivated-avx-512-on-alder-lake-but-fully-questionable-interpretation-of-efficiency-news-editorial/" target="_self">Igor's Lab</a> 的 Xaver Amberger，在最新的 A22 BIOS 版本中发现了新添加的代码。如上图所示，用户可选自动（Auto）、正常（Normal）和 AVX-512 尝试（Trail）三档设置。</p><p><a href="https://static.cnbetacdn.com/article/2022/0203/87564f49a4ce12a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0203/87564f49a4ce12a.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（via <a href="https://hwbot.org/submission/4915853_skullbringer_y_cruncher___pi_2.5b_core_i9_12900k_(8p)_55sec_271ms" target="_self">HWBOT</a>）</p><p>之所以仅在 MSI MEG Z690 Unify-X 这款主板上解锁这项体验，主要是因为它是一款主打发烧友的高端超频主板。</p><p>借助 AVX-512，英特尔 Alder Lake CPU 可在 Y-Cruncher 等极端超频基准测试中发挥更高的性能、效率也更高一些。</p><p>至于其它主板厂商是否会很快跟进推出新版 BIOS（或者保留未屏蔽 AVX-512 选项的旧版 BIOS），目前暂不得而知。</p>   
</div>
            