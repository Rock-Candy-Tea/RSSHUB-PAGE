
---
title: 'Linux 5.13添加对亚马逊Luna游戏手柄的支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0507/df55d6993245b29.jpg'
author: cnBeta
comments: false
date: Fri, 07 May 2021 03:05:00 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0507/df55d6993245b29.jpg'
---

<div>   
<strong>Linux 5.13 内核今天整合了新的输入子系统更新，其中最值得关注的就是添加了对亚马逊（Luna）游戏手柄的支持。</strong>亚马逊的游戏手柄（Luna 手柄）主要服务于该公司的云游戏服务，但可以通过蓝牙、USB 接口在 Windows、Mac 和 Android 平台上使用。该手柄售价为 70 美元，还可以和 Fire TV 设备一起使用。<br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0507/df55d6993245b29.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0507/df55d6993245b29.jpg" alt="ors2de4h.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在 Linux 5.13 中，只需将亚马逊游戏手柄的 USB 设备 ID 添加到 XPad 驱动程序中，就可以获得支持。当这个 Luna 手柄通过 USB 连接时，它的行为类似于<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a> <a data-link="1" href="https://microsoft.pvxt.net/e4yLO" target="_blank">Xbox</a> 360 控制器。</p><p style="text-align: left;">因此，对于这个 Linux 5.13 的支持只是将 0x041a 设备 ID 和 0x1949 亚马逊供应商 ID 添加到XPad驱动中。Linux 的 XPad 驱动是用来支持 Xbox 游戏机控制器的--包括官方的和各种第三方的控制器。对 XPad 驱动的小补充是由谷歌 Chrome OS 工程师贡献的。</p><p style="text-align: left;">除了在 XPad 驱动中启用亚马逊游戏手柄，Linux 5.13 的输入子系统还整合了 3 个新的触控屏驱动。这些新的触摸屏驱动是 Hycon HY46XX、ILITEK Lego 系列和 MStar MSG2638。还有一个新的 Azoteq IQS626A 即将获得整合。</p>   
</div>
            