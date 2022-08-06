
---
title: '上游合并在即：开发者大幅精简Rust for Linux v9补丁体量'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0806/12445aa2a2b68f7.jpg'
author: cnBeta
comments: false
date: Sat, 06 Aug 2022 02:45:32 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0806/12445aa2a2b68f7.jpg'
---

<div>   
本周早些时候发布的 Rust for Linux v8 补丁，引入了诸多抽象、并将 Rust 编程语言集成扩展到了内核中的更多部分。Phoronix 指出：<strong>v8 补丁的代码总行数达到了 43.6k，而今日新发布的“Rust for Linux v9”，仅引入了 12.5k 的新代码行。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0806/12445aa2a2b68f7.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">Rust 有望作为 C 语言的补充，作为支持 Linux 内核驱动程序开发的新语言。</p><p>由于删除了许多额外的功能和集成，Rust for Linux v9 较之前的补丁要小得多。通过坚持更初始的“最小化路线”，其有望为主线内核带来更积极的变化。</p><p>除了增强集成与构建事务，它还允许对各种抽象和子系统的特定补丁，引来更多人参与代码的审核与反馈工作。<strong>首席开发者 Miguel Ojeda 评论道：</strong></p><blockquote><p>作为 v8 补丁的‘精简版’，v9 为编译一个最小的 Rust 内核模块提供了足够的支持 —— 以期率先得到‘核心’支持，并开始逐步将其余部分‘上游化’。</p><p>内核模块能够创建一个‘向量’，作为一种连续、可增长的数组类型，其能够推送一些数字、并在卸下时使用‘pr_info!’宏将之打印到内核日志。</p></blockquote><p><strong>新补丁系列还可通过移除其中部分内容而变得更小，目前看来其取得了不错的平衡。</strong></p><blockquote>最终得来 3% 的 kernel crate 留存（减少到了 500 行），60% 的 alloc 和 adapt alloc 提交（100 行），总体量从 40k 精简到了 13k 行。<p>虽然大多数代码已在 linux-next 中存在数月，但我们还是不得不为减少一些内容而做微小的改动，最后欢迎大家积极反馈这一选项是否符合你的预期。</p></blockquote><p><a href="https://www.phoronix.com/news/Rust-For-Linux-v9-Patches" target="_self">Phoronix</a> 指出，随着 v9 补丁量的显著瘦身，其有望较之前更容易获得主线许可。</p><p>Linus Torvalds 一直希望尽快完成合并（下周的 Linux 6.0 合并窗口），后续将观察相关工作是否已经足够良好。</p>   
</div>
            