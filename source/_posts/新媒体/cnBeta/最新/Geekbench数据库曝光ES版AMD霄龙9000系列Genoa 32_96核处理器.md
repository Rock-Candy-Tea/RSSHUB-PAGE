
---
title: 'Geekbench数据库曝光ES版AMD霄龙9000系列Genoa 32_96核处理器'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0817/173ccf8e4c5d3b6.jpg'
author: cnBeta
comments: false
date: Wed, 17 Aug 2022 00:49:56 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0817/173ccf8e4c5d3b6.jpg'
---

<div>   
@Benchleaks 刚刚在 Twitter 上晒出了两款 ES 版 AMD 霄龙 9000 系列 Genoa 服务器处理器的 Geekbench 基准测试数据。<strong>尽管与正式版相比，两款 CPU 的主频相对较低，其单线程性能改进还是相当亮眼。</strong>其中 96 核心 / 192 线程的 EPYC 9000 Genoa 处理器的编号为“100-000000997-01”，而 32 核心 / 64 线程的那枚则是“100-000000897-03”。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0817/173ccf8e4c5d3b6.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0817/173ccf8e4c5d3b6.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（via <a href="https://wccftech.com/amd-epyc-9000-genoa-96-core-32-core-cpu-benchmarks-strong-single-threaded-performance/" target="_self">WCCFTech</a>）</p><p>96 / 32 核 EPYC 9000 Genoa 处理器的基础频率为 3.51 / 3.61 GHz，但实测似乎只能达到 3.5 GHz、且异常的全核频率似乎拖累了多线程性能（有待进一步分析验证）。</p><p>测试平台选用了双路 SP5 服务器主板（曙光 OEM），但分别为其配备了 768 / 640 GB 的 DDR5 内存。</p><p><img src="https://static.cnbetacdn.com/article/2022/0817/f0adb0e7d9c775b.png" alt="2-1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">双路 × 32 核心测试平台</p><p>需要注意的是，Zen 4 CPU 的每个 CCD 应该会搭配 32MB L3 高速缓存，这里 Geekbench 软件可能错误识别成 16MB（或者早期样本只启用了一半的 L3 Cache）。</p><p>最终 32 核 EPYC 9000 Genoa CPU 单核 / 多线程得分为 1444 / 35329 分，而 96 核 EPYC 9000 Genoa CPU 则是 1464 / 19834 分。</p><p><img src="https://static.cnbetacdn.com/article/2022/0817/9227fd2e20933f6.png" alt="2-2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">双路 × 96 核心测试平台</p><p>如此怪异的成绩，表明两枚 ES 版处理器的全核性能发挥严重拖了后腿。好消息是，至少它们的单核表现仍相当亮眼。</p><p>此外参考 @结城安穗-YuuKi_AnS 在社交媒体上分享的 96 核 EPYC 9654 @ 双路平台的基准测试成绩，早期芯片的利用率确实是个问题。<img src="https://static.cnbetacdn.com/article/2022/0817/922829ee70e4532.png" alt="3.png" referrerpolicy="no-referrer"></p><p>整个测试期间，只有不到一个处理器在那里发力。在搭配 22000 RPM 高转<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C738%2C751" target="_blank">风扇</a>的情况下，标称 360W TDP 的芯片温度，竟然只有 83℃ 。</p><p><img src="https://static.cnbetacdn.com/article/2022/0817/ea448137ab372b1.png" alt="4-1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">Geekbench 5 - 单核性能比较</p><p>全核频率更是低到 3.65 GHz，庆幸的是 CPU-Z 的 AVX-512 单核跑分还是能够达到不错的 687.1 分。</p><p><img src="https://static.cnbetacdn.com/article/2022/0817/d5c47934157c0ba.png" alt="4-2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">CPU-Z / AVX-512 单核性能比较</p><p>按照计划，EPYC 9000 Genoa GPU 或于未来几个月内投向服务器市场，届时我们将重新审视正式版 SKU 的实际性能表现。</p><p><img src="https://static.cnbetacdn.com/article/2022/0817/20f35793e12ba34.png" alt="5.png" referrerpolicy="no-referrer"></p>   
</div>
            