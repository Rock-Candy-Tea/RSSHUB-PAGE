
---
title: 'Linux 5.19中Framework Laptop获得ChromeOS EC驱动支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0530/109a1ac2f2c50f6.webp'
author: cnBeta
comments: false
date: Mon, 30 May 2022 02:32:14 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0530/109a1ac2f2c50f6.webp'
---

<div>   
在 Linux 5.19 内核的 Chrome 平台更新中，在带来大量修复之外还引入了全新的 Chrome OS ACPI
设备驱动，但现阶段大部分都是比较基础的。<strong>一个值得注意的补充是 Framework Laptop 现在得到了 cros_ec_lpcs
的支持</strong>，该模块化 Linux 笔记本电脑使用了Google的 ChromeOS 嵌入式控制器。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0530/109a1ac2f2c50f6.webp" alt="9b41exg7.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">Framework Laptop 是少数使用 ChromeOS EC，但不是 Chromebook/ChromeOS 设备之一。由于使用了 Google 开发的 EC，Framework Laptop 的嵌入式控制器软件是开源固件。在 Linux 5.19 中，在 cros_ec_lpcs 驱动程序中添加了 DMI 匹配，因此它可以正确绑定到框架笔记本电脑上。</p><p style="text-align: left;">同时这套针对 Linux 5.19 的 Chrome 平台更新还增加了新的 ChromeOS ACPI 设备驱动程序。此驱动程序将 ACPI 报告的值导出到 sysfs 目录，因为在通过常见 ACPI 工具读取时，传统 ACPI 表中不存在数据。 ChromeOS 用户空间直接使用这个新驱动程序通过 sysfs 公开的数据。</p>   
</div>
            