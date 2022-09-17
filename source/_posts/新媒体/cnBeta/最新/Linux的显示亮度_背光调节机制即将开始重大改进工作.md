
---
title: 'Linux的显示亮度_背光调节机制即将开始重大改进工作'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0917/0a0c1dd0f64fac0.png'
author: cnBeta
comments: false
date: Sat, 17 Sep 2022 10:59:05 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0917/0a0c1dd0f64fac0.png'
---

<div>   
红帽公司的Hans de Goede多年来参与了许多重要的Linux台式机/笔记本电脑硬件改进工作，他最近一直关注的一项举措是用户界面当中的背光/亮度调节界面，这一直是Linux系统控制笔记本电脑硬件的一个短板。<br>
<p><a href="https://static.cnbetacdn.com/article/2022/0917/0a0c1dd0f64fac0.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0917/0a0c1dd0f64fac0.png" title alt="图片.png" referrerpolicy="no-referrer"></a><br></p><p>本周在Linux管道工（Linux Plumbers）会议上包含一个关于这个长期以来存在的需要改进的工作的演讲。<br></p><p>Hans de Goede一直致力于解决目前/sys/class/backlight用户空间API的局限性，并引入一个新的、设计更好的API。Hans最初在2014年就谈到了背光接口的问题，即一个显示器可以有多个背光设备未能被系统识别，背光亮度的值为0时系统未对其定义，没有办法将背光sysfs设备映射到给定的显示器等等。</p><p>为了解决当前的问题，正在酝酿中的计划是为DRM连接器对象添加新的"display_brightness"和"display_brightness_max"属性。现在，最大亮度的值为0将被定义为不支持亮度控制。</p><p>那些希望了解更多关于正在进行的改善Linux显示器背光亮度控制处理的工作的人，可以查看LPC 2022的Hans的幻灯片（PDF）：</p><p><a href="https://lpc.events/event/16/contributions/1390/attachments/990/1916/kernel-recipes-backlight-2022-16x9.pdf" _src="https://lpc.events/event/16/contributions/1390/attachments/990/1916/kernel-recipes-backlight-2022-16x9.pdf" target="_blank">https://lpc.events/event/16/contributions/1390/attachments/990/1916/kernel-recipes-backlight-2022-16x9.pdf</a><br></p><p>还有他一直在为解决这一混乱局面而进行的内核补丁：</p><p><a href="https://lore.kernel.org/all/20220825143726.269890-1-hdegoede@redhat.com/" _src="https://lore.kernel.org/all/20220825143726.269890-1-hdegoede@redhat.com/" target="_blank">https://lore.kernel.org/all/<span class="__cf_email__" data-cfemail="f7c5c7c5c5c7cfc5c2c6c3c4c0c5c1d9c5c1cecfcec7dac6da9f93929098929392b78592939f9683d994989a">[email protected]</span>/</a><br></p>   
</div>
            