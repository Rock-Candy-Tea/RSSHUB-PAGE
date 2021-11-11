
---
title: 'Linux 5.16为内核驱动程序引入断电侦测硬件功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1111/9690af6445fff12.png'
author: cnBeta
comments: false
date: Thu, 11 Nov 2021 10:24:18 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1111/9690af6445fff12.png'
---

<div>   
上周，开发者向 Linux 5.16 提交了主要的 ACPI 和电源管理功能变更。但在周三的合并中，我们又迎来了第二批功能变更。<strong>其中值得一提的，莫过于允许 Linux 驱动程序在断电时依然能够“侦测”硬件的新特性。</strong>据悉，英特尔对 Linux 内核所做的这项改进，旨在允许内核模块探测某些设备、而不改变它们的现有电源状态。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1111/9690af6445fff12.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="http://lkml.iu.edu/hypermail/linux/kernel/2111.0/02281.html" target="_self">LKML</a>）</p><p>虽然不适用于所有硬件 / 驱动程序（取决于必要的 ACPI 支持），但该功能至少可以帮助正确探测硬件并加载驱动程序。在无需初始化的情况下，确保相关组件能够成功电量和工作。</p><p>有趣的是，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>这么做的动机，主要还是围绕笔记本网络摄像头等硬件而产生的。毕竟某些网络摄像头会在启用时点亮隐私提醒 LED 灯，但出于安全的考量，该功能通常又是交给 OS 软件来控制的。</p><p>为了避免对用户体验造成打扰，或在系统启动时误以为 Linux / 其它东西正在监视他们，英特尔才提出了希望能够“在断电状态下侦测设备”的 ACPI 驱动程序新功能。</p><p><img src="https://static.cnbetacdn.com/article/2021/1111/9cc7d8ba4c2084b.jpg" referrerpolicy="no-referrer"></p><p>新改进可免除在加载内核驱动程序时必须开启摄像头的麻烦，不过这项解决方案也不是 100% 完美，比如在尝试使用驱动程序 / 摄像头之前，我们无法知晓硬件是否存在问题。</p><p>参考英特尔在最新补丁中提到的描述，这项改动主要针对 imx319 和 at24 驱动程序。至于其它 Linux 内核驱动程序，亦可在具有必要的 ACPI 特性的情况下启用该功能。</p><p>具体说来是，相关代码通过 ACPI 树引入，因其在电源管理中引入了“_DSC”对象，以指示该设备能够处于评估其配置的深度睡眠状态。</p><p>由今年早些时候提出的 <a href="https://lore.kernel.org/linux-acpi/CAJZ5v0gwDEjC9T7wfCqDr7R0q_ptz2nVU52_8i8noXHPEign1g@mail.gmail.com/T/" target="_self">ACPI 规范草案</a>可知：支持该 _DSC ACPI 对象的设备，可以让 Linux 内核知晓特定硬件能够在驱动程序侦测过程中保持 D3cold 或类似状态、而无需完全开启对应的设备。</p>   
</div>
            