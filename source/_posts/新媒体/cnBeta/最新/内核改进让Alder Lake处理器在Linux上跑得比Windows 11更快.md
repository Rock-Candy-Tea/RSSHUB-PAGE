
---
title: '内核改进让Alder Lake处理器在Linux上跑得比Windows 11更快'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0211/9b71e78c628647f.jpg'
author: cnBeta
comments: false
date: Fri, 11 Feb 2022 05:58:29 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0211/9b71e78c628647f.jpg'
---

<div>   
当英特尔于去年 11 月推出 12 代 Alder Lake 酷睿处理器时，Phoronix 就已经开展过跨平台的基准测试。<strong>不过随着 Linux 5.16 及后续带来的内核改进，Windows 11 的性能优势已大不如前。</strong>在基于酷睿 i9-12900K 旗舰桌面处理器的硬件测试平台上，Phoronix 还同时比对了多个版本的 Linux 操作系统。<br><br>
<p><img src="https://static.cnbetacdn.com/article/2022/0211/9b71e78c628647f.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://www.phoronix.com/scan.php?page=article&item=adl-linux516-windows&num=1" target="_self">Phoronix</a>）</p><p>除了基于 Linux 5.16 / 5.17-rc3 的 Ubuntu 22.02，还有<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>自用的 Clear Linux 参考平台。</p><p>发布初期，<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 确实赋予了 Alder Lake 更好的性能优化。但随着围绕混合核心架构的修复、以及其它内核改进的引入，Linux 5.16+ 又重新取得了领先地位。</p><p><a href="https://static.cnbetacdn.com/article/2022/0211/96570b8340c5423.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0211/96570b8340c5423.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p>与前述测试一样，本轮硬件测试采用了 i9-12900K 处理器、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://asus.jd.com/" target="_blank">华硕</a> ROG STRIX Z690-E GAMING WiFi
主板（使用测试时的最新版固件），以及 2×32GB DDR5-4400 双通道内存。</p><p>图形部分仅采用集成的 Gen12 ADL-S GT1 核显，Windows 11（x64 专业版）操作系统打上了 2 月初的所有可用稳定更新 + 驱动程序。</p><p><img src="https://static.cnbetacdn.com/article/2022/0211/cded2b6d29799ab.jpg" alt="3.jpg" referrerpolicy="no-referrer"></p><p>Linux 系统则使用了 2 月 7 日的 Ubuntu 22.04 LTS 每日构建版（选择了 i915.force_probe 启动项，以启用 i9-12900K 图形加速功能），以及基于 Linux 5.16 内核的 Clear Linux 35810 滚动发行版。</p><p><img src="https://static.cnbetacdn.com/article/2022/0211/5cf00e7be1f728b.png" alt="4.png" referrerpolicy="no-referrer"></p><p>简单来说，在视频和图像编码编码测试项目中，Alder Lake 处理器可受益于 Linux 5.16+ 内核改进、且 Clear Linux 还有额外的性能加成。</p><p><img src="https://static.cnbetacdn.com/article/2022/0211/b3473325f720ce1.png" alt="5.png" referrerpolicy="no-referrer"></p><p>在总计 104 轮对比测试中，Windows 11 只能在 13% 的情况下领先于 Linux 。至于总是垫底的 Ubuntu 22.04，必须指出的是，它目前仍处于 Linux 5.15 的开箱即用状态。</p><p><img src="https://static.cnbetacdn.com/article/2022/0211/76f63a5ff56e2b8.png" alt="6.png" referrerpolicy="no-referrer"></p><p>感兴趣的朋友，可移步至 <a href="https://www.phoronix.com/scan.php?page=article&item=adl-linux516-windows&num=6" target="_self">Phoronix</a>，以查看完整的测试结果。</p>   
</div>
            