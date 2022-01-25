
---
title: 'Linux Kernel 5.17为AMD硬件带来大量改进'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0125/39b0703a0b848ed.webp'
author: cnBeta
comments: false
date: Tue, 25 Jan 2022 03:22:11 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0125/39b0703a0b848ed.webp'
---

<div>   
伴随着 Linux 人才团队的扩建以及加速推进对下一代硬件的支持，正在开发的 Linux 5.17 内核上会有大量 AMD 功能获得重大改进，并将在 Linux 的 AMD 兼容性和处理方面迎来更新的进展<strong>。科技媒体 Phoronix 报道了关于 Linux 5.17 的功能概述，现在新功能的定稿已经提交并被标记为 Linux 5.17-rc1。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0125/39b0703a0b848ed.webp" alt="u9ge7sv8.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">现在，Linux Kernel 5.17 开始进入每周更新的候选版本阶段，预估会在今年 3 月下旬正式发布。Phoronix 提醒用户，Linux 5.17 不会是 Ubuntu 22.04 LTS 的默认内核，但 Fedora 36 以及众多春季 Linux 发行版会采用该内核版本。</p><p style="text-align: left;">以下是整合到 Linux 5.17 的主要 AMD 功能介绍</p><p style="text-align: left;">● 新版 AMD P-state 驱动已经正式准备好发布。这个驱动是 AMD 和 Valve 合作开发的，与标准的 ACPI CPUFreq 驱动相比，有助于提高 Linux 平台上的电源效率。</p><p style="text-align: left;">AMD 的 P-State 驱动依赖于 ACPI 协作处理器性能控制（CPCC），它在创建更精细的计算机处理器频率和性能状态信息可用性方面由平台揭示部分。通过 ACPI CPPC，只要启用CPPC，AMD的P状态就只能与Zen 2和未来的处理器兼容。</p><p style="text-align: left;">与 Scheutil 治理器相结合，AMD P-State 应该允许比目前利用 CPUFreq 与 Schedutil 的过程更多的性能。</p><p style="text-align: left;">● 在最新的 Zen 4 处理器技术方面，有许多发展，包括 EDAC 和 SMCA 的更新，包括识别注册 DDR5 和减载 DDR5 内存类别以便报告。K10 温度写入支持似乎比计划提前合并，在发布后有希望，就像过去通常看到的那样，特别是在 Zen 1到3系列。这种缺乏支持的情况对于访问准时的CPU支持温度监测显示得并不好。</p><p style="text-align: left;">● AMD Smart Trace Buffer（AMD STB），是一个循环数据缓冲器，记录系统执行信息，从内部分析故障。AMD STB 始终处于活动状态，当错误发生时可以擦除，而不需要进行任何额外的仪器测试或重新创建错误来寻找解决方案。AMD 智能跟踪缓冲器的支持已经正式完成，在利用较新的硬件时，CPU 和 Radeon dGPU 部分都将在 Linux 5.17 版本中准备就绪。</p><p style="text-align: left;">● 用于 AMD Renoir 的硬件现在已经支持其音频协处理器的 Sound Open Firmware。Linux 5.17将是第一个支持Sound Open Firmware的AMD平台，Sound Open Firmware传统上是作为一个<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>项目整合的，但已经失效了。</p><p style="text-align: left;">● 此外，在 AMD 的 Linux 笔记本电脑方面，修复了 AMD s2idle 故障，以及 AMD 的 S2idle/S0ix 相关 Linux 工作的最新集合。许多带有X570、B550、B450、X470芯片组的较新的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://asus.jd.com/" target="_blank">华硕</a>主板现在将包括对工作传感器的支持--这是Linux平台的第一次。Linux 5.17还提出了对Rembrandt SoC网络的支持。</p><p style="text-align: left;">● 对 Rembrandt APU 提供 GPU 恢复和 Van Gogh 的无缝启动，以及修复了其他几个错误，并将在未来更新为更加兼容。这次的 AMDGPU DRM 内核驱动方面并不像最近的一些内核发布那样令人兴奋。</p><p style="text-align: left;">● 最后，Linux 5.17 可以使用 AMD 3DNow。带有 Hudson D4 芯片组的 AMD Fusion APU 系统，预计可以改善启动时间。指令位于内核的代码内。</p>   
</div>
            