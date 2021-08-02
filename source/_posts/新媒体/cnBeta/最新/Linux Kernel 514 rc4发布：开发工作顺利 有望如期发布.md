
---
title: 'Linux Kernel 5.14 rc4发布：开发工作顺利 有望如期发布'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Mon, 02 Aug 2021 03:14:20 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
<strong>Linux Kernel 5.14 的第 4 个候选版本于今天正式发布。</strong>该分支更新的开发工作相当顺利，进程中并没有出现太多令人担心的东西。但本次更新的幅度依然不小，没有什么让 Linux 创造者 Linus Torvalds 感到沮丧的东西。<br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在 Linux 5.14-rc4 公告中写道：“没什么需要重点关注的，rc4 开发进度一切正常。它主要是一个非常好的、平坦的diffstat--如此小的分散的变化--除了在selftests和xfs修复中的几个小点。大部分是驱动，一些arch更新，网络，加上工具和selftests。没有什么特别突出的地方”。</p><p style="text-align: left;">本周引起我们注意的是，Linux 5.14-rc4 确实改变了一些管道行为，此前 Linux 内核在 2019 年破坏了一些 Android 应用程序。一个有趣的情况是，恢复内核行为以恢复与旧内核的二进制兼容性，即使是在用户空间滥用接口的情况下。但无论如何，整体影响应该不大。</p><p style="text-align: left;">Linux 5.14-rc4也放弃了一个DEC Alpha特定的x86二进制加载器，本周还有 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 的 PMC 更新，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> Alder Lake HID 支持，以及更多通过 platform-drivers-x86 实现的更新。总的来说，这是一个相当令人愉快的一周，也是结束7月的好方法，没有什么真正可怕的事情发生，但我们将看看接下来的几周如何发展，看看这是否会是一个准时的内核发布。</p>   
</div>
            