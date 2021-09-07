
---
title: 'Linux 5.15改进系统内存调用 可更快释放垂死进程的资源'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0907/7b5fef87a668f3b.png'
author: cnBeta
comments: false
date: Tue, 07 Sep 2021 04:50:20 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0907/7b5fef87a668f3b.png'
---

<div>   
<strong>为解决 systemd-oomd 或 Android 的 LMKD 等内存问题，Linux 社区开发者一直提议引入更好的系统调用策略，以更快地释放垂死进程的内存。</strong>比如今夏早些时候，Phoronix 的 Michael Larabel，就提出了一个名叫“process_reap”的系统调用方案，特点是能够在压力下更快地回收内存资源。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0907/7b5fef87a668f3b.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=884a7e5964e06ed93c7771c0d7cf19c09a8946f1" target="_self">Kernel.org</a>）</p><p>最新消息是，这项工作已经演变成为了“process_mrelease”，且 Linux 5.15 也做好了迎接新版系统调用策略的准备。而使用新系统调用的最大优势，就在于能够更快、更可预测地回收垂死进程的内存资源。</p><p><a href="https://www.phoronix.com/scan.php?page=news_item&px=Linux-5.15-process-mrelease" target="_self">Phoronix</a> 指出，传统 Linux（尤其是桌面 Linux）无法很好地应对内存压力，但近年来 systemd-oomd、各种内核创新、以及现在的 process_mrelease，都已经取得了稳步的发展。</p><p>在该补丁合并到 Linux 5.15 之后，Andrew Morton 继续深入解释了 process_mrelease 的系统调用方式：</p><blockquote><p>对于此类系统组件来说，能够快速高效地释放内存资源，是非常重要的一点。</p><p>遗憾的是，进程在收到 SIGKILL 后释放内存所需的时间、可能因进程的状态（不间断睡眠）、正在运行的核心大小、以及 OPP 级别而异。</p><p>若能够找到以更可预测的方式来释放目标进程资源的机制，也将能够提升系统控制其内存压力的能力。</p><p>通过引入 process_mrelease 系统调用方案，系统就能够从调用方（caller）的上下文中释放垂死进程的内存。</p><p>基于此，内存能够以更可控的方式来释放，具有 CPU 亲和性和调用优先级，释放内存的工作量也会由调用方来承担，不过相关操作只允许针对垂死进程来执行。</p></blockquote>   
</div>
            