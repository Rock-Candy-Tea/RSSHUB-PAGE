
---
title: '英特尔正为Linux 5.17准备PFRUT：升级系统固件无需重启'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1230/e0598afbf6e19ba.webp'
author: cnBeta
comments: false
date: Thu, 30 Dec 2021 01:55:29 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1230/e0598afbf6e19ba.webp'
---

<div>   
<strong>援引科技媒体 Phoronix 报道，英特尔为 Linux Kernel 5.17 准备的一项新开源项目，允许操作系统像主板上的 UEFI/BIOS 一样升级固件，而不需要重新启动系统。</strong>该项目叫做 Platform Firmware Runtime and Telemetry 驱动，简称 PFRUT。作为广泛使用的 ACPI 规范的一部分，这意味着我们可以看到同样的方法将来会出现在 Windows 和台式电脑上。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1230/e0598afbf6e19ba.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">PFRUT 给系统带来的好处是，当你更新 BIOS 时不需要重新启动系统。这项功能在服务器部署中非常有用，因为停机时间可能会阻碍业务运营。没有重启的要求，服务器可以自由地更新系统 BIOS，同时确保关键的工作负载在整个过程中保持运行。</p><p style="text-align: left;">目前，Phoronix 注意到这是一个服务器专属的功能，没有消息表明它是否会出现在Linux操作系统的消费者领域。PFRUT 的工作方式与你通常通过 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 或 Linux 更新 BIOS 的方式非常相似，更新过程是通过操作系统完成的，而不是直接通过系统 BIOS 完成。但在 PFRUT 中，操作系统将负责执行整个更新过程。而在正常的 BIOS 更新中，Windows 或 Linux 将只负责上传 BIOS，并在重新启动和将新的 BIOS 交给主板更新之前进行准备。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1230/178cf4488448bda.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">我们不确定是否有支持 PFRUT 的必要硬件要求。你可能需要一块支持它的主板，或者不需要硬件支持，只需要 PFRUT 驱动程序。目前，发展一直很稳定，有两个新的驱动程序更新，本周还为PFRUT开发了一个新工具，允许用户与BIOS更新器对接。<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>还将这些驱动程序添加到 Linux 的“Linux-next”分支中，计划在下一个 Linux 内核更新（即Linux 5.17）中使用。</p><p style="text-align: left;">这种功能是否会出现在台式电脑或Windows中，还有待观察。然而，由于它是基于无处不在的ACPI规范，应该有可能为消费者个人电脑采用同样的方法。</p>   
</div>
            