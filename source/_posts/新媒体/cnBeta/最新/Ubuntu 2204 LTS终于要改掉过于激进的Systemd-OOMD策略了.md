
---
title: 'Ubuntu 22.04 LTS终于要改掉过于激进的Systemd-OOMD策略了'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0701/c77690043a50054.jpg'
author: cnBeta
comments: false
date: Fri, 01 Jul 2022 06:22:00 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0701/c77690043a50054.jpg'
---

<div>   
在移动操作系统上，iOS / Android 智能机用户已经领教过疯狂“杀后台”的威力。<strong>然而在 Ubuntu 22.04 LTS 发行版上，Linux 用户也沮丧于 Systemd-OOMD 会在高内存 / 交换使用时干掉应用程序。</strong>于是过去一个月里，开发者们一直在尝试找出 Systemd-OOMD 的优化策略。尤其避免突然杀掉 VS Code 和 Firefox 等软件进程，而导致用户体验变得极其糟糕。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0701/c77690043a50054.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://www.phoronix.com/scan.php?page=news_item&px=Ubuntu-Drops-Swap-Kill" target="_self">Phoronix</a>）</p><p>Jammy 已经提出了针对 systemd 249.11-0ubuntu3.4 的修订建议，目前正在根切片（-.slice）上设置“ManagedOOMSwap=auto”，并将很快向稳定版本推送更新。</p><p>此前 Ubuntu 22.04 LTS 一直在默认使用“ManagedOOMSwap=kill”，结果导致系统总是误杀高资源占用的重要应用程序进程。</p><p><img src="https://static.cnbetacdn.com/article/2022/0701/aa745a5ed9cd30b.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>而在修改后，system-oomd 的默认策略将被局限于监测内存压力（memory pressure）、而不至于将手伸长到瞎管交换使用率（swap usage）。</p><p>在不终止大量 swap usage 或提议增加 swap size 的新策略下，用户将不再频繁看到应用程序被意外终止，此外 Ubuntu Linux 开发团队也在探索其它建议和想法。</p>   
</div>
            