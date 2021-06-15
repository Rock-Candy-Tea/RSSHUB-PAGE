
---
title: '英特尔M.2 Modem驱动IOSM即将整合到Linux 5.14内核中'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0615/8f421e59b43f614.jpg'
author: cnBeta
comments: false
date: Tue, 15 Jun 2021 03:12:38 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0615/8f421e59b43f614.jpg'
---

<div>   
英特尔希望通过全新的 M.2 通讯模组来增强 EVO 笔记本和 Chromebook 的商用。<strong>在推进过程中英特尔的工程师一直在研究将“IOSM”作为 M.2 通讯模组的驱动程序，在经过数月的代码开发之后，该驱动将会在 Linux 5.14 内核中首次亮相。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0615/8f421e59b43f614.jpg" alt="4jhpbhxp.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">这个新的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> M.2 通讯模组驱动程序被称之为的 IOSM，全称是 IPC over Shared Memory。官方解释为 IOSM 驱动是一个 PCIe 主控驱动，可用于 Linux 或者 Chrome 平台。在主机平台和英特尔 M.2 通讯模组之间通过 PCIe 接口进行数据交换。该驱动提供符合 MBI M协议的接口。任何前端应用程序（如：调制解调器管理器）可以很容易地管理MBIM接口，以实现面向WWAN的数据通信。</p><p style="text-align: left;">IOSM已经看到了追溯到2020年底的补丁，这个驱动程序正在利用内核的新WWAN框架，用于无线WAN设备。从今天起，该驱动已被排入net-next，因此当Linux 5.14内核的合并窗口在几周内打开时，它就被摆在了桌面上。</p>   
</div>
            