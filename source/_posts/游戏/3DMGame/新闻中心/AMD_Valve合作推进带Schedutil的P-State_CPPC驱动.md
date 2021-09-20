
---
title: 'AMD_Valve合作推进带Schedutil的P-State_CPPC驱动'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20210919/1632065586_160852.jpg'
author: 3DMGame
comments: false
date: Sun, 19 Sep 2021 15:33:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20210919/1632065586_160852.jpg'
---

<div>   
<p style="text-indent:2em;">
以 Steam Deck 为主要推动力，AMD 和 Valve 一直在努力合作改善 Linux CPU 的性能/频率。正如今年 8 月报道所猜测的，他们的工作可能围绕着 Zen 2 CPU 和新版 ACPI CPPC 推进。例如上周发布适用于 Linux 的 AMD P-State 驱动，确实利用了 CPCC 信息。在昨天召开的 XDC2021 大会上，AMD 正式展示了这个新驱动。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210919/1632065586_160852.jpg" alt="AMD/Valve合作推进带Schedutil的P-State/CPPC驱动" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
AMD 正在开发这个新的“AMD
P-State”驱动程序，以利用 ACPI 协作处理器性能控制（CPPC），做出更明智的 CPU 频率缩放/性能状态决策。虽然 CPCC 初期仅限于 Zen 3 的一个子集，但经过适当的审查现已经支持 Zen 2 和更新版本 AMD CPU。
</p>
<p style="text-indent:2em;">
此外，AMD 和 Valve 正专注于利用 Schedutil 治理器，该治理器利用内核的调度器利用率数据，试图做出更准确的决定。当不使用英特尔的 P-State 驱动时，Schedutil已经是许多Linux发行版内核上的ACPI CPUFreq的默认值，并且总体上处于良好状态。上游公司也一直在推动 AMD 接受 Schedutil，这可以追溯到他们最初在 2019 年为 Zen 2 涉足
ACPI CPPC 支持时。
</p>
<p style="text-indent:2em;">
AMD的Ray Huang周五在X.Org开发者大会（XDC2021）上围绕他们的工作发表了演讲。下面是感兴趣的人的发言，但长话短说，众所周知，ACPI CPUFreq 不太理想，AMD P-State 正在努力改善 AMD 较新 CPU 的情况，类似于英特尔的 P-State 驱动。
</p>
<p style="text-indent:2em;">
AMD的数据显示，新的P-State驱动在不同的工作负载下比CPUFreq有可衡量的性能/效率改进。AMD的P-State驱动仍在开发中，还没有被主流化，所以最早也要到Linux 5.16才会出现。
</p>          
</div>
            