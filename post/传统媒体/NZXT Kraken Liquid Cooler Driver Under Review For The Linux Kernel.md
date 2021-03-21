
---
title: NZXT Kraken Liquid Cooler Driver Under Review For The Linux Kernel
categories: 
    - 传统媒体
    - Phoronix - 新闻与评测
author: Phoronix - 新闻与评测
comments: false
date: Fri, 19 Mar 2021 07:40:00 GMT
thumbnail: https://www.phoronix.com/assets/categories/hardware.jpg
---

<div>   
<div style="float: left; padding: 0 10px 10px;"><img alt="HARDWARE -- " src="https://www.phoronix.com/assets/categories/hardware.jpg" width="100" height="100" referrerpolicy="no-referrer"></div>
While NZXT does not provide any official Linux software support for their products like their all-in-one liquid coolers, the open-source community for years has worked to fill that void thanks to reverse-engineering. The latest work when it comes to the NZXT Kraken AIO liquid coolers is a proposed HWMON driver for the mainline kernel.
<br>
<br>For years there has been various user-space solutions for monitoring and controlling NZXT Kraken liquid cooling loops with the likes of <a href="https://www.phoronix.com/scan.php?page=news_item&px=GKraken-NZXT-Linux-Water-Cool">the GKraken software</a> and Liquidctl. That's been in user-space for interfacing with these USB-based devices while now a kernel driver for mainline has been proposed that allows various NZXT Kraken products to be supported while jiving with the hardware monitoring "HWMON" subsystem.
<br><p align="center"><img src="https://www.phoronix.net/image.php?id=2019&image=kraken_linux_7_med" referrerpolicy="no-referrer"></p>
<br>The proposed "nzxt-kraken2" kernel driver is under review and exposes the Kraken's fan and pump speed as well as coolant temperature through the HWMON interfaces for easy monitoring via sysfs. Kraken does support fan and pump control but is not currently exposed by this driver. Similarly, LED controls are not supported by this kernel driver either. The kernel driver is making the assumption that the existing user-space tools like GKraken are better suited for handling these controls than the kernel driver
<br>
<br>Jonas Malaco of the Liquidctl project is the developer who worked on this kernel driver and sent it out for review and discussion on the mailing list. The nzxt-kraken2 kernel driver is currently verified against the NZXT Kraken X42, X52, X62, and X72 AIO coolers.
<br>
<br>The nzxt-kraken2 driver under review in its current form can be found on the <a href="https://lore.kernel.org/lkml/20210318164824.21374-1-jonas@protocubo.io/">kernel mailing list</a>.  
</div>
            