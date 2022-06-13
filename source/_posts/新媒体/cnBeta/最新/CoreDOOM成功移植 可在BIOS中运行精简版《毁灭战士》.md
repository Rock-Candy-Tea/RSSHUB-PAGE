
---
title: 'CoreDOOM成功移植 可在BIOS中运行精简版《毁灭战士》'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0613/b761462d48c448c.png'
author: cnBeta
comments: false
date: Mon, 13 Jun 2022 09:53:32 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0613/b761462d48c448c.png'
---

<div>   
作为一款在 PC 游戏史上占据重要地位的作品，我们已经在许多奇葩的场景中见到过 93 版《毁灭战士》（Doom）的运行，比如老式拨盘电话、Twitter 网页、甚至 100 磅发霉的土豆上。<strong>不过本文要为大家介绍的，则是一个能够在主板 BIOS 上运行的最新移植项目。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0613/b761462d48c448c.png" alt="2.png" referrerpolicy="no-referrer"></p><p><a href="https://www.pcgamer.com/doom-coreboot-coredoom/" target="_self">PCMag</a> 解释称：该版本通过 Coreboot 方案，以在主板固件平台上运行。</p><p>与出厂自带的主板 BIOS 软件相比，开源的 Coreboot 具有更加轻快灵活的特点。</p><p>最新消息是，移植者结合了 Dasharo 框架，在一块<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">微星</a> Z690 主板上玩出了新花样。</p><p><img src="https://static.cnbetacdn.com/article/2022/0613/c3e27c0f7200147.jpg" referrerpolicy="no-referrer"></p><p>作为完成硬件初始化工作后运行的实际软件，Coreboot 依赖于所谓的“有效负载”（payloads）来实现相关功能，涵盖了 Linux 启动、以及传统 x86 SeaBIOS 等形式。</p><p>然而出乎许多人意料的是，最近又有人倒腾出来了一个“coreDOOM”。<a href="https://www.phoronix.com/scan.php?page=news_item&px=Coreboot-4.17" target="_self">Phoronix</a> 指出，这是一个能够在 BIOS 中运行的《Doom》移植版。</p><p>其基于 Coreboot 4.17 的有效载荷打造，本质上可在启动时直接加载系统和游戏。不过受限于 ROM 芯片的存储空间，改造后的 PC 也只能拿来玩这款经典老游戏了。<br></p><p><img src="https://static.cnbetacdn.com/article/2022/0613/4c293ac070d25a7.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>其它尴尬的地方包括仅支持 PS/2 键盘，不支持音频或保存，且退出游戏时会让系统整体陷入冻结。</p><p>即便如此，作为 doomgeneric 的一个精简移植项目，CoreDOOM 还是较 93 原版要更加便携。</p><p>展望未来，我们大可期待 Coreboot 本身也将迎来更多现代化的特性加持。<br></p>   
</div>
            