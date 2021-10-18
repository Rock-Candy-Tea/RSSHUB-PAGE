
---
title: '新Linux内核补丁能为Vortex86硬件提供适当的CPU检测'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1018/14423c1ed4b2b5b.jpg'
author: cnBeta
comments: false
date: Mon, 18 Oct 2021 02:05:12 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1018/14423c1ed4b2b5b.jpg'
---

<div>   
对于那些目前依然维护 32 位 x86 架构、且没有出现部分 Vortex86 核心并不支持 i686 级别功能的 Linux 发行版本，Vortex86 32-bit SoCs 依然可以正常运行。<strong>但现在终于有了一个待定的内核补丁，为 Vortex86 硬件提供适当的 CPU 检测。</strong><br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1018/14423c1ed4b2b5b.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1018/14423c1ed4b2b5b.jpg" alt="08bk8tgy.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">DM&P 电子公司的 Vortex86 SoC 与各种旧的 Linux 发行版配合得很好，与通用的 x86 32 位路径相比，不需要对这些 CPU 进行任何特殊处理。尽管在 2021 年底，对 DM&P Vortex 处理器的正式检测和支持正在进行，但其动机是 Spectre 和 Meltdown 缓解措施被错误地应用于它们。</p><p style="text-align: left;">Vortex86 CPU对Spectre和Meltdown并不脆弱，因为它们是一个内序设计，也缺乏CLFLUSH指令。但是，由于Linux内核没有适当地迎合Vortex86并正确地识别它们，对这些32位SoC的性能打击缓解措施被错误地应用，而这些32位SoC的速度已经够慢了，没有不必要的缓解措施。</p><p style="text-align: left;">因此，一个补丁正在等待中，以提供对正确识别DM&P电子Vortex86处理器的支持，从而使任何怪癖和调整能够正确应用。目前，唯一的调整/怪癖处理只是意味着在上述硬件上启动时，Spectre和Meltdown缓解措施将不再被应用。</p>   
</div>
            