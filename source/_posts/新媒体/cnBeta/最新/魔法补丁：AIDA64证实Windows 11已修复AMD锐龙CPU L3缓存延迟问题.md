
---
title: '魔法补丁：AIDA64证实Windows 11已修复AMD锐龙CPU L3缓存延迟问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1019/410d26e21b652fb.png'
author: cnBeta
comments: false
date: Tue, 19 Oct 2021 01:15:11 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1019/410d26e21b652fb.png'
---

<div>   
几天前，微软向 Beta 和 Release Preview 通道的 Insider 测试者们，推送了 Windows 11 操作系统的 22000.282 编译版本。<strong>可知其中包含了大量的更新改进，尤其是 AMD 锐龙 CPU 用户最为关心的 L3 缓存延迟问题。</strong>自 Windows 11 操作系统正式发布以来，这个问题导致 AMD CPU 的 L3 缓存出现了延迟的大涨，并于 Patch Tuesday 之后被进一步放大。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1019/410d26e21b652fb.png" alt="0.png" referrerpolicy="no-referrer"></p><p>AIDA64 指出，即使<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>已将 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Zen 3 架构正式列入 Windows 11 的支持列表，且在架构方面引入了重大升级。</p><p>但锐龙 R9-5900X 这样的最新款 Zen 3 处理器，仍会受到缓存延迟问题导致的严重性能损失。</p><p>此外 Windows 11 操作系统会在启用基于虚拟化的安全性（VBS）之后造成一定的性能损失，这是因为旧款 CPU 上缺少 MBEC 所导致。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1019/3a2dcc06fcea0e1.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">Windows 10 平台 L3 缓存截图</p><p>庆幸的是，微软已经随着 Build 22000.282（KB5006746）补丁的发布，正式修补了 Windows 11 在 AMD 锐龙 CPU 平台上的性能问题。</p><p>与此同时，AIDA64 官方也决定对新测试版本展开一番测试，以验证微软的说法，于是就有了本文看到的这三张截图。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1019/7e380f070f0dc06.png" alt="2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">Windows 11 平台 L3 缓存延迟截图（修补前）</p><p>测试分别在 Windows 10、以及修补前后的 Windows 11 操作系统平台上展开。</p><p>与上次不同的是，AIDA64 这次特地选用了基于 Zen 2 架构的锐龙 R9 PRO 3900 处理器、AORUS X570 主板、以及 DDR4-2667 双通道内存的硬件配置。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1019/f7a74f51ccd4f97.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">Windows 11 平台 L3 缓存延迟截图（修复后）</p><p>结果表明，KB5006746 补丁确实发挥了巨大的作用。本次更新后，AMD 锐龙 CPU 的 L3 缓存性能已经恢复到了其应有的水平。</p><p>基于此，AIDA64 强烈建议 Insider 测试者们在第一时间升级到最新版本。至于普通用户，还请耐心等待 Windows 11 的分批次稳步推进。</p>   
</div>
            