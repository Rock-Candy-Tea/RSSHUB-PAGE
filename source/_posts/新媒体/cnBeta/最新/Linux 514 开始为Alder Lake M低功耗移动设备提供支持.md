
---
title: 'Linux 5.14 开始为Alder Lake M低功耗移动设备提供支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Mon, 31 May 2021 12:17:03 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
最近几个月，已经有很多Linux内核补丁用于提升Alder Lake S和Alder Lake
P的支持度和性能表现，<strong>而最近开始，英特尔的开发人员已经在为Alder Lake M低功耗移动设备提供支持补丁。对Alder Lake
M的Linux支持一直落后于ADL-S和ADL-P，但差距不大，在大多数情况下，ADL-M相当于增加了额外的PCI ID。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p>到目前为止，在Linux 5.13的主线Linux内核中，有intel_th PCI和USB DWC3驱动程序对Alder Lake M的支持，但随着今年夏天Linux 5.14周期的到来，看起来会有更多的初始支持。</p><p>现在在各种"-next"树和邮件列表中排队的Alder Lake M补丁包括Alder Lake M对PCH-DMIC或SoundWire编解码器以及传统的声音支持、Pinctrl支持、MFD Intel-LPSS，以及其他需要新PCI ID的领域。而在为Alder Lake已经引入的新代码路径上，这些待定的补丁没有太多引人注目的惊喜。</p><p>看起来Linux 5.14可能会首次成为支持Alder Lake M的基准版本，但我们会看到一些悬而未决的补丁预计在一个月后的下一个合并窗口启动。通常情况下，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>会提前为新硬件提供Linux内核支持，这次仍然是预留了几个月，但不是我们习惯于看到的那种幅度，但对于Alder Lake而言是一个很大的进步，英特尔的Linux工程师也在继续完成对Xeon Sapphire Rapids的支持。</p><p>Alder Lake是英特尔的第12代酷睿处理器，最引人注目的是Gold Code和Gracemont低功耗内核的混合架构。Alder Lake还引入了对DDR5/LPDDR5的支持，改进了英特尔Gen12 Xe图形，以及其他改进。当下一代处理器在今年晚些时候开始出货时，看看Alder Lake对Linux的支持和性能如何提升将是很有趣的。</p><p><a href="https://static.cnbetacdn.com/article/2021/05/d9c14eb0dd69d77.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/05/d9c14eb0dd69d77.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            