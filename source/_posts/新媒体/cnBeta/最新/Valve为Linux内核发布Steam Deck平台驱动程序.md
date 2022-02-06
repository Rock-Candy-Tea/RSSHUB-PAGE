
---
title: 'Valve为Linux内核发布Steam Deck平台驱动程序'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0206/bbf51d1fe5e755c.jpg'
author: cnBeta
comments: false
date: Sun, 06 Feb 2022 10:43:23 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0206/bbf51d1fe5e755c.jpg'
---

<div>   
Valve今天发布了一个Linux内核驱动，用于为即将推出的Steam
Deck提供平台控制支持。该平台驱动用于支持由嵌入式控制器（EC）固件提供的Steam
Deck特定"VLV0100"设备。最终用于CPU/设备风扇控制、访问DDIC寄存器、电池温度测量、显示相关设置和USB
Type-C事件通知等功能。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0206/bbf51d1fe5e755c.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>这个驱动程序是由Valve工程师开发的，x86"ste<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>eck"平台的驱动程序只有500多行新代码，现在正在努力合并入主线内核。这并不是能够在Steam甲板上使用其他Linux发行版的关键功能，但它肯定是很好的。</p><p>考虑到补丁的推出时间，预计要到3月下旬启动的Linux 5.18周期才会被合并。Valve的基于Arch Linux的SteamOS预计至少在最初会依赖一个打了补丁的内核，所以对于Steam Deck的玩家来说，所有的功能都应该是正常的，但是这个驱动对于那些有时间想在这个便携式手持游戏系统上运行其他Linux发行版的人来说才是有用的。</p><p><strong>了解更多：</strong></p><p><a href="https://lore.kernel.org/lkml/20220206022023.376142-1-andrew.smirnov@gmail.com/" _src="https://lore.kernel.org/lkml/20220206022023.376142-1-andrew.smirnov@gmail.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="cffdfffdfdfffdfff9fffdfdfffdfce1fcf8f9fefbfde2fee2aea1abbdaab8e1bca2a6bda1a0b98fa8a2aea6a3e1aca0a2">[email protected]</span>/</a><br></p>   
</div>
            