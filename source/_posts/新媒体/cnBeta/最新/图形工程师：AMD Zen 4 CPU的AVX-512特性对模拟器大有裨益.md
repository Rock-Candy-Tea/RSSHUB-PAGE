
---
title: '图形工程师：AMD Zen 4 CPU的AVX-512特性对模拟器大有裨益'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0905/eac1e1b75085089.png'
author: cnBeta
comments: false
date: Mon, 05 Sep 2022 12:27:28 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0905/eac1e1b75085089.png'
---

<div>   
<strong>Riot Games 图形工程师 Joey（@Wunkolo）刚刚在 Twitter 上透露，AMD Zen 4 CPU 引入的 AVX-512 特性，可为 Yuzu 等模拟器带来巨大的优势。</strong>Wunkolo 表示，自己多年来一直尝试为模拟器测试 AVX-512 加速功能。而他的最新工作，正好可以极大地受益于 AMD 即将推出的锐龙 7000 系列 AM5 台式处理器。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0905/eac1e1b75085089.png" alt="1.png" referrerpolicy="no-referrer"></p><p>具体说来是，包括 <a href="https://yuzu-emu.org/" target="_self">Yuzu</a>（<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.jd.com/pinpai/14671.html" target="_blank">任天堂</a> Switch）、<a href="https://citra-emu.org/" target="_self">Gitra</a>（任天堂 3DS）、<a href="https://vita3k.org/" target="_self">Vita3K</a>（索尼 PS Vita）、以及 <a href="https://xenia.jp/" target="_self">Xenia</a>（<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a> <a data-link="1" href="https://microsoft.pvxt.net/e4yLO" target="_blank">Xbox</a> 360）在内的模拟器，都可获益于消费级 CPU 的 AVX-512 指令集。</p><p>此前<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>曾尝试在 12 代 Alder Lake CPU 中添加 AVX-512 加速特性，但后来又出于功耗等方面的考虑，而通过主板 CPU 微码更新来锁死（至强 / Xeon 芯片仍可用）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0905/8ea38d6f3689124.png" alt="3.png" referrerpolicy="no-referrer"></p><p>数据方面，与标准的 AVX2 指令集相比，AVX-512 可为 RPCS3（索尼 PS3）等模拟器带来高达 30% 的性能提升。</p><p>有趣的是，在 Intel 在消费级 CPU 市场放弃 AVX-512 的同时，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 这边又为 Zen 4 锐龙 7000 系列 AM5 台式处理器带来了 AVX-512 支持。</p><p><a href="https://static.cnbetacdn.com/article/2022/0905/858493be67f843d.jpeg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0905/858493be67f843d.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></a></p><p>该公司称，其 Zen 4 CPU 可通过 AVX-512（VNNI）将 FP32 推理性能提升 30%、且 INT8 推理性能可达 2.5 倍。</p><p>值得一提的是，Wunkolo 表示这些成绩还是在没有使用任何 256 位 ymm、或 512 位 zmm 寄存器的情况下完成的。</p><p><img src="https://static.cnbetacdn.com/article/2022/0905/3dba4f313847be8.png" alt="4.png" referrerpolicy="no-referrer"></p><p>WCCFTech 指出，寄存器位宽能够显著扩展新指令级架构在特定项目上的表现。虽然在这段长篇大论中，Wunkolo 并未给出细致的个人工作说明，但确实也分享了一些文档链接。</p><p>对于喜欢玩模拟器、或者需要在特定场景下使用 AVX-512 指令集的朋友，大可期待锐龙 7000 和 13 代酷睿正式上市后的市场反响。</p>   
</div>
            