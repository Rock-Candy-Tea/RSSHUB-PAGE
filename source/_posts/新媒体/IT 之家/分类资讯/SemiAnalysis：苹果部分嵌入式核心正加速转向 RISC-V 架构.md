
---
title: 'SemiAnalysis：苹果部分嵌入式核心正加速转向 RISC-V 架构'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/9/4509bba3-e5d0-4b3e-9912-fd9f996fe7e0.jpg@s_2,w_820,h_546'
author: IT 之家
comments: false
date: Sat, 17 Sep 2022 07:42:13 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/9/4509bba3-e5d0-4b3e-9912-fd9f996fe7e0.jpg@s_2,w_820,h_546'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D2056699" rel="nofollow">OC_Formula</a> 的线索投递！</div>
            <p data-vmark="6c22"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 9 月 17 日消息，半导体产业分析机构 SemiAnalysis 分析师 Dylan Patel 表示，苹果正将其嵌入式芯片核心指令集从 ARM 架构的转向 RISC-V 架构，谷歌也将在 TPU 上应用来自 SiFive X280 核心的部分设计。</p><p data-vmark="072a">例如现有 Apple A15 仿生芯片就有十几个基于 Arm 的 CPU 内核分布在芯片上，用于各种不会直接面向用户的功能。SemiAnalysis 可以确认这些内核在未来几代硬件中积极转向 RISC-V 架构。</p><p data-vmark="b74e">还有人指出，RISC-V 作为一款在 BSD 开源的硬件架构，按照苹果一贯的行事风格来看，他们一定不会直接用 RISC-V，而且经过魔改后闭源（或许会命名为 Apple ISA）再搭配自家闭源系统进行整体营销，类似 A10 之后 CPU 中的指令集模式。</p><p data-vmark="fd61">在 Apple Silicon 设计中，核心是相当重要的一部分，例如在 M1 中就有 30 多个内核负责与系统无关的各种工作负载，如 WiFi / 蓝牙、接口重定时、触摸板控制、NAND 芯片的内核等，它们都拥有自己的固件，并为 SoC 外围功能电路提供支持。</p><p data-vmark="06b5">目前看来，这些核心大多基于 Arm M 系列或低端的 A 系列 IP，而苹果目前正想办法用 RISC-V 来取代这些核心。</p><p data-vmark="0270">鉴于很大一部分软件依赖于主 big.LITTLE 运行，其他次要的 SoC 任务迁移到异构 ISA 只需进行少量的固件调整即可。更重要的是，苹果可以藉此节省巨额授权费用，按库克的思路来考虑苹果根本没理由不干。</p><p data-vmark="fa30"><img src="https://img.ithome.com/newsuploadfiles/2022/9/4509bba3-e5d0-4b3e-9912-fd9f996fe7e0.jpg@s_2,w_820,h_546" w="820" h="546" title="SemiAnalysis：苹果部分嵌入式核心正加速转向 RISC-V 架构" width="820" height="546" referrerpolicy="no-referrer"></p><p data-vmark="a256">IT之家了解到，近期苹果发布了 <a class="s_tag" href="https://iphone.ithome.com/" target="_blank">iPhone 14</a> 系列新款手机，包括 <a class="s_tag" href="https://iphone.ithome.com/" target="_blank">iPhone</a> 14、<a class="s_tag" href="https://iphone.ithome.com/" target="_blank">iPhone 14 Plus</a>、<a class="s_tag" href="https://iphone.ithome.com/" target="_blank">iPhone 14 Pro</a>、<a class="s_tag" href="https://iphone.ithome.com/" target="_blank">iPhone 14 Pro Max</a>，5999 元起。</p><p data-vmark="da6e">在预售方面，大部分人可能更倾向于 iPhone 14 Pro、iPhone 14 Pro Max（搭载 A16 芯片），并且已延迟到 10 月发货，而 iPhone 14、iPhone 14 Plus （搭载 A15 芯片）仍可以在首发日购买到。</p><p data-vmark="e829">据苹果官方介绍，<span class="accentTextColor">A16 仿生芯片由两颗高性能核心和 4 颗高能效核心组成的 6 核中央处理器带来的速度提升至高可达 40%</span>（和 A13 相比），采用经加速的 5 核图像处理器，内存带宽提升多达 50%，极为适合运行图形密集型游戏和 App，而全新 16 核神经网络引擎的处理能力高达每秒 17 万亿次运算，这枚芯片可在耗电量极低的情况下提供更高的性能，并且实现全天候电池续航。</p><p data-vmark="1900">不过，A16 Bionic 的 GPU、神经引擎核心与去年的 A15 Bionic 完全相同，得益于台积电 N4（第三代 5nm，约 6% 密度提升）工艺的提升，最终 CPU 方面实现了“近 160 亿个晶体管”，较 150 亿的 A15 略有提升，此外功耗方面应该会有所提升。</p>
          
</div>
            