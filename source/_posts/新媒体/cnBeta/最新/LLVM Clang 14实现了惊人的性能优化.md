
---
title: 'LLVM Clang 14实现了惊人的性能优化'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1207/dacd8f12b313703.png'
author: cnBeta
comments: false
date: Tue, 07 Dec 2021 03:25:59 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1207/dacd8f12b313703.png'
---

<div>   
多年以来，LLVM / Clang 的性能已经迎来了相当大的提升。此外在 x86_64 和 AArch64 应用上，它也能够与 GCC 编译器并驾齐驱。即便如此，激烈的竞争并未就此止步。<strong>由最近一次提交的内容可知，即将于 2022 年初发布的 LLVM / Clang 14.0，将迎来更多性能方面的优化。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1207/dacd8f12b313703.png" alt="1.png" referrerpolicy="no-referrer"></p><p>早些时候，LLVM 开发者 Djordje Todorovic 为 LLVM 的 Loop Invariant Code Motion（LICM）Pass 引入了相关改进，以便能够在没有 STORE 的情况下提升 LOAD 。</p><blockquote><p>补丁描述称，在 LICM 中开展加载 / 存储更新时，若不能证明下沉存储是安全的，LLVM 就不会提升加载，即使我们能够证明它可被取消引用并移出循环。</p><p>该补丁通过在循环中插入适当的 PHI，并将其移动到循环前置器中以实现负载改善，而 STORE 将在循环中保持原样。</p><p>通过这么做，我们可避免在每次迭代中、于内存位置进行加载。此外这项针对 Pass 的改进，还有助于修复此前一个 <a href="https://bugs.llvm.org/show_bug.cgi?id=51193" target="_self">bug 报告</a>中提到的错过 register promotion 的问题。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2021/1207/f795872bd60fd2e.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1207/f795872bd60fd2e.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>对于不了解编译器内部原理、仅对净收益感兴趣的用户，Todorovic 也分享了一些基准测试结果。</p><blockquote><p>在我们的 PostgreSQL 基准测试中，我们发现这一 LOAD 补丁的性能增益在 12% 左右。</p><p>此外从 XZ 压缩、C-Ray 到 MrBayes 等各种其它工作负载的性能，通常也有几个百分点的性能改进。</p></blockquote><p>最后，这项加载性能改进补丁将和其它内容一道，成为明年 3 月正式发布的 LLVM Clang 14.0 稳定版的一部分。</p>   
</div>
            