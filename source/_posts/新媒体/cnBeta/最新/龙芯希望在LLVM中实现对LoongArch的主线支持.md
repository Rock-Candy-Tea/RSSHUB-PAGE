
---
title: '龙芯希望在LLVM中实现对LoongArch的主线支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1129/6d870affc28ebdf.webp'
author: cnBeta
comments: false
date: Fri, 17 Dec 2021 09:56:59 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1129/6d870affc28ebdf.webp'
---

<div>   
近日有消息称，<strong>龙芯不仅致力于为 GCC 编译器和相关 GNU 工具链组件提供 LoongArch 指令级架构（IS）支持，还制定了要为 LoongArch 实现 LLVM 主线支持的计划。</strong>回顾 2021 年，该公司一直忙于推出新的 MIPS CPU 架构，同时致力于 Linux 内核移植（以及开源代码编译器 / 相关组件）。若进展顺利，国产高性能处理器也将能够迎来更好的发挥。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1129/6d870affc28ebdf.webp" referrerpolicy="no-referrer"></p><p><a href="https://www.phoronix.com/scan.php?page=news_item&px=LoongArch-LLVM-Plans" target="_self">Phoronix</a> 报道称，当前基于 LoongArch 的龙芯 3A5000 CPU，其基准测试尚未给大家留下深刻的印象。</p><p>但是观察基于 MIPS 的新架构会如何发展，本身也是一件相当有趣的事情。比如周三的时候，龙芯工程师就介绍了他们最新的 LLVM 计划。</p><p>自去年以来，他们一直致力于 LLVM 支持。虽然初始目标仅与旧版本挂钩，但在那之后，团队一直在有针对性地开展 LoongArch 的移植重构（<a href="https://lists.llvm.org/pipermail/llvm-dev/2021-December/154371.html" target="_self">LLVM Git</a>）。</p><p><img src="https://static.cnbetacdn.com/article/2021/1217/69f7684289c445d.png" referrerpolicy="no-referrer"></p><p>期间他们还改进了测试的覆盖率和代码规范，以期在步入上游 LLVM 存储库后持续改进相关代码。</p><p>过去数月，我们已经见到了与 LoongArch 相关的大量公开工作，但内部开发的工作量也不该忽略。</p><p>即使短时间内无法与 Intel / <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 等芯片行业巨头相匹敌，LoongArch 能够像俄罗斯 Elbrus CPU 一样成为国产佳品，也是具有相当重要的意义的。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1208409.htm" target="_blank">龙芯中科发布补丁系列 以在GCC中启用对LoongArch处理器的支持</a></p></div>   
</div>
            