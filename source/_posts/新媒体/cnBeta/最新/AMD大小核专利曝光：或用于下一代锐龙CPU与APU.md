
---
title: 'AMD大小核专利曝光：或用于下一代锐龙CPU与APU'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0616/a6c5ded913dca6e.jpg'
author: cnBeta
comments: false
date: Wed, 16 Jun 2021 03:32:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0616/a6c5ded913dca6e.jpg'
---

<div>   
<strong>WCCFTech 刚刚曝光了 AMD 新获的一项有趣专利，因为它预示了下一代锐龙 CPU / APU 产品线可能采用类似移动设备平台的“大小核”设计理念。</strong>此前多年，智能机 SoC 厂商已经对 big.LITTLE 架构展开了充分的验证，而英特尔也计划在 12 代 Alder Lake-S 桌面产品线上试水 16C / 24T 的大小核设计。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0616/a6c5ded913dca6e.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p>此前有传闻称，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 会在下一代芯片设计中过渡至混合架构，而新曝光的“任务转换”（Task Transition）专利，也或多或少地证实了这一点。</p><p><img src="https://static.cnbetacdn.com/article/2021/0616/f4591c5c3018c90.png" alt="1.png" referrerpolicy="no-referrer"></p><p>熟悉 ARM SoC 架构的朋友，应该不难理解 big.LITTLE 可结合不同的核心 IP、以实现性能和能效方面的更优均衡。</p><p><img src="https://static.cnbetacdn.com/article/2021/0616/29e4a0ecdcd7dba.png" alt="2.png" referrerpolicy="no-referrer"></p><p>而<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>的 12 代 x86 处理器（Lakefield SoC），也设法将高性能的酷睿 Cove 核心、与低功耗的凌动 Gracemont 核心结合到了一起。</p><p><img src="https://static.cnbetacdn.com/article/2021/0616/3a2675ffca48806.png" alt="4.png" referrerpolicy="no-referrer"></p><p>虽未得到广泛的采用，但随着英特尔与 AMD 在下一代芯片设计上引领转型，系统和软件开发商也将很快跟进早期测试。</p><p><img src="https://static.cnbetacdn.com/article/2021/0616/d5fbbd0638bbdfd.png" alt="5.png" referrerpolicy="no-referrer"></p><p>言归正传，AMD 于 2019 年 12 月提交了这项有趣的异构设计专利，且该公司早就在 APU 产品线上实现了“在同一封装中融汇两套不同的芯片 IP”的目标。</p><p>由新专利的文档资料可知，AMD 描述了一种独特的方法、系统和装置，能够将性能度量与相关联的阈值进行比较、或通过其它指标来确定多个任务是否该从某组 CPU 核心转移到另一组。</p><p><img src="https://static.cnbetacdn.com/article/2021/0616/bfdd78f88ed5521.png" alt="7.png" referrerpolicy="no-referrer"></p><p>在工作负载的迁移过程中，显然还需要对两组 CPU 的相关任务进行特定的调整。比如在暂停源 CPU 核心任务的同时、还需要参考目标 CPU 核心的状态信息，以便其做好承接转移负载的准备。</p><p>众所周知，异构架构倾向于将大核心用于高性能工作负载、而小核心则更适合于效率优化的多线程任务。</p><p>新专利表明，AMD 将通过同一个互连小芯片来沟通两组 CPU 核心、同时给予内部互相通信的权限，以分享核心利用率、内存使用 / 访问、空闲 / 负载状态下的能耗等信息。</p><p><img src="https://static.cnbetacdn.com/article/2021/0616/77cb4e07cbb53f3.png" alt="8.png" referrerpolicy="no-referrer"></p><p>最后，有传闻称 AMD 会在 Strix Point APU 芯片上使用 Zen 5 大核心 + Zen 4D 小核心的设计，但它们要等到 2024 年才会与大家见面。</p><p>同时随着英特尔 Alder Lake 芯片在今年晚些时候的亮相，预计最新版本的 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 操作系统也将为其落实大量更新，以支持混合架构和新的调度优化程序。</p><p>至于异构架构能否在 x86 主流平台上交出让广大消费者感到满意的答卷，仍有待时间去检验。</p>   
</div>
            