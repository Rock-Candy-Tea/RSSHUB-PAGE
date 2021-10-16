
---
title: 'Realtek 802.11ax Wi-Fi卡驱动"rtw89"正准备合并到Linux 5.16'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1016/38663fa06f9edd8.jpg'
author: cnBeta
comments: false
date: Sat, 16 Oct 2021 12:28:25 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1016/38663fa06f9edd8.jpg'
---

<div>   
本周到达wireless-drivers-next分支的是"rtw89"驱动，这是一个由Realtek贡献的开源802.11ax WiFi驱动。这个新的rtw89 Linux Wi-Fi驱动最初是为了支持Realtek 8852AE 802.11ax ASIC。<br>
 <p>Realtek方面选择开发一个新的驱动程序，而不是扩展现有的Realtek无线内核驱动程序，这是因为寄存器地址范围已经完全完善，新的格式，以及其他相比现有的Realtek无线芯片组的根本变化。</p><p><a href="https://static.cnbetacdn.com/article/2021/1016/38663fa06f9edd8.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1016/38663fa06f9edd8.jpg" title alt="Hac68213f001d43a79a1a8e20e96d53bcP.jpg" referrerpolicy="no-referrer"></a></p><p>Realtek rtw89的开发由该公司官方的工程师领导，也将用于支持他们新的802.11ax无线芯片组的后续型号。</p><p>rtw89 Wi-Fi驱动程序的初始形式是大约91000行新代码，但其中大约一半的行数是一个包含寄存器表的C文件。</p><p>到目前为止，Realtek 8852AE新卡已经出现在各种新的联想笔记本电脑中。</p><p>在下个月的Linux 5.16合并窗口之前，Realtek rtw89驱动目前位于wireless-drivers-next中，其他厂牌Wi-Fi驱动的变化也在不断增加。</p>   
</div>
            