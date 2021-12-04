
---
title: 'Linux 5.17将修复在读取损坏软盘时强制弹出导致的挂起问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1204/437baf870325a27.jpg'
author: cnBeta
comments: false
date: Sat, 04 Dec 2021 04:43:45 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1204/437baf870325a27.jpg'
---

<div>   
随着日历即将翻向 2022 年的新篇章，许多人或许早已忘记“保存”图标所指代的软盘驱动器。即使是较为年长的计算机用户，上一次接触软盘的时间，或许都可以追溯到大约 20 年前。<strong>事实上，如今仍有许多普通人看不到的隐秘角落，仍依赖于软盘驱动器的应用。与此同时，Linux 内核也在不时发布针对软驱的驱动更新和修复补丁。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1204/437baf870325a27.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">资料图（来自：IBM）</p><p>尴尬的是，今年早些时候发布的一批软驱补丁，可能导致 Linux 内核在意外状况下挂起。</p><p>问题可追溯到 2012 年的代码修改，之后我们不时见到看门狗代码（watchdog code）引起的相对一致的触发。</p><p>具体说来是，若用户尝试读取损坏的软盘，并在 I/O 仍在重复尝试时强制手动弹出，则行为变更可能导致可重现的挂起。</p><p>如果你仍在使用软盘、并运行着基于现代内核的此类系统，还请耐心等待计划于 Linux 5.17 中引入的 bug 修复。</p><p><img src="https://static.cnbetacdn.com/article/2021/1204/1708d56a4160130.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：<a href="https://lore.kernel.org/lkml/045df549-6805-0a02-a634-81aca7d98db5@linux.com/T/#u" target="_self">LKML</a>）</p><p>据悉，Linux 5.17 内核驱动程序会在软盘弹出时撤销操作，而无需等待 watchdog code 返回 / 完成，以避免在软盘损坏等情况下挂起。</p><p>如果一切顺利，Linux 5.17 有望于 2022 年的前几个月内发布，但各大 Linux 发行版的更新推送可能要多等待一段时间。</p><p>至于软盘驱动程序会在 Linux 主线内核中保留多长的时间，目前暂不得而知。毕竟在某些无需频繁迭代的工业设备中，软盘仍得到相当广泛的使用。</p>   
</div>
            