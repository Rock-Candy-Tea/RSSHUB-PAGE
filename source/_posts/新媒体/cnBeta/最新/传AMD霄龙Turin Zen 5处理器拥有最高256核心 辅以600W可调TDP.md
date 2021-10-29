
---
title: '传AMD霄龙Turin Zen 5处理器拥有最高256核心 辅以600W可调TDP'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1029/4da8d5ea449b57d.jpg'
author: cnBeta
comments: false
date: Fri, 29 Oct 2021 07:46:31 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1029/4da8d5ea449b57d.jpg'
---

<div>   
<strong>@ExecutableFix 和 @Greymon55，刚刚在 Twitter 上分享了与 AMD 下一代 Zen 5 霄龙（EPYC）Turin 处理器有关的一些有趣细节。</strong>据说作为 Genoa 系列的继任者，EPYC Turin 将沿用 SP5 平台，辅以前所未见的封装设计。今年晚些时候，我们有望率先在 EPYC Milan-X 上见到堆叠式 3D 小芯片设计的演变。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1029/4da8d5ea449b57d.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1029/4da8d5ea449b57d.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p>当 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 霄龙 Turin 处理器在数年后正式亮相时，可推测该系列芯片将在一块基板上整合多个 CCD 与缓存堆栈。</p><p>相比之下，Genoa CPU 最高拥有 96 个核心，而 Bergamo 算是在同一 Zen 4 架构上的演进版本，据说拥有最高 128 个核心。</p><p><a href="https://static.cnbetacdn.com/article/2021/1029/21dcc2899ea33bd.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1029/21dcc2899ea33bd.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>除了 CPU 与缓存设计，传闻还称 Turing 还有望迎来 256 个核心、且搭配 PCIe 6.0 。若 AMD 有意采用堆叠式 X3D 小芯片方案，甚至可以推到更高。</p><p>至于如何在相同的 SP5 平台上容纳两倍于 Genoa / Bergamo 的核心数量，我们对传说中的 192C / 384T 和 256C / 512T 的 EPYC Turin CPU 还是充满了好奇。</p><p><img src="https://static.cnbetacdn.com/article/2021/1029/6b2c25aea1695f7.png" alt="3.png" referrerpolicy="no-referrer"></p><p>预计为了实现这一目标，AMD 有两条技术路线可选。其一是让每个 CCD 的核心数翻倍，目前 Zen 3 / Zen 4 的单 CCD 可容纳 8 个核心。</p><p>若翻倍到单 CCD / 16 个核心，最终 EPYC 服务器处理器有望通过堆叠 12 / 16 个 CCD，达成 192 / 256 个核心的目的。</p><p><a href="https://static.cnbetacdn.com/article/2021/1029/8107d25473e4467.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1029/8107d25473e4467.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a></p><p>在早前的传闻中，MLID 了一种全新的封装布局，即在 SP5 平台上可支持多达 16 组 CCD 。不过 AMD 还有另一条可能性较低的技术路线，那就是在 CCD 之上继续堆叠 CCD 。</p><p>如此以来，即便每组 CCD 维持 8 个核心不变，总体设计还是可以达成多芯片 / 16 组 CCD 。</p><p><a href="https://static.cnbetacdn.com/article/2021/1029/8fabcab0d65c359.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1029/8fabcab0d65c359.png" alt="5.png" referrerpolicy="no-referrer"></a></p><p>至于芯片的热设计功耗（TDP），即使 EPYC Turin 用上台积电最先进的 3nm 工艺制程，双倍核心的功率需求也是相当夸张的。</p><p>即将推出的 96 核 EPYC Genoa CPU，其可调 cTDP 已经高达 400W 。若 EPCY Turin 的 cTDP 最高冲击到了 600W，SP5 插槽（LGA 6096）似乎也可承受 700W 的峰值功耗（虽然只能持续 1ms）。</p><p><a href="https://static.cnbetacdn.com/article/2021/1029/af0b3403a1998eb.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1029/af0b3403a1998eb.png" alt="6.png" referrerpolicy="no-referrer"></a></p><p>Gigabyte 的泄露资料已证实有关下一代平台的各种信息，可知 SP5 针脚数量比当前的 LGA 4094 还多了 2002 个触点。</p><p>如果将持续时间放宽到 10ms，那 SP5 平台的峰值功率将落到 440W（OCC 峰值 600W）。在超过 cTDP 之后，EPYC 芯片将在 30ms 内恢复限制。</p><p>最后，泄露的 AMD 演示文稿还证实了 EPYC Genoa 继任者的 SoC 将支持更高的 DDR5-6000 到 6400 内存（或指代 Bergamo / Turin）。</p><p>如果一切顺利，AMD 或于 2024 - 2025 年左右推出 EPYC Turin，并将与<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>的 Diamond Rapids Xeon 平台展开更直接的竞争。</p>   
</div>
            