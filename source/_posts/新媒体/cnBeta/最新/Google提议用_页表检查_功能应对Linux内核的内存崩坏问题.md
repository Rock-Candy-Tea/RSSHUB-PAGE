
---
title: 'Google提议用_页表检查_功能应对Linux内核的内存崩坏问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1117/a5362288006d0b7.png'
author: cnBeta
comments: false
date: Wed, 17 Nov 2021 09:36:39 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1117/a5362288006d0b7.png'
---

<div>   
<strong>上周，Google 工程师发现了一个引用数据下溢（reference count underflow）问题，且一路可追溯到 2017 年的 Linux 4.14 内核。</strong>这个偶然发现的问题，会导致内存从一个进程泄露到另一个进程。为化解此类内存缺陷，Google 提出了一个全新的“页表检查”（Page Table Check）解决方案。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1117/a5362288006d0b7.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">问题从 Linux 4.14 延续到 Linux 5.16（来自：<a href="https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?id=4716023a8f6a0f4a28047f14dd7ebdc319606b84" target="_self">Kernel.org</a>）</p><p>除了 Google，近期还有不少合并提交修复了其它引用计数问题。但若“页表检查”功能推广开来，Linux 内核就会在页表条目插入 / 删除时，检查是否存在非法共享。</p><p>若检测到内存遭到破坏，内核也会以崩溃作为回应。此外需要注意的是，额外检查会导致一些性能影响、以及额外的内存资源开销。</p><p>基于此，“页表检查”功能不会在默认情况下开启。有需要的用户，需在手动激活 PAGE_TABLE_CHECK 的情况下进行构建。</p><p>然后在运行时，还要动用 page_table_check=on 这个内核启动参数。感兴趣的朋友，可移步至内核邮件公告列表（<a href="https://lore.kernel.org/all/20211116220038.116484-1-pasha.tatashin@soleen.com/" target="_self">LKML</a>）获取更多细节。</p><p>最后，作为单独补丁系列的一部分，我们还于本周二迎来了一组页面强化（<a href="https://lore.kernel.org/lkml/20211117012059.141450-1-pasha.tatashin@soleen.com/" target="_self">hardening page _refcoount</a>）。</p><p>参与其中的 Google 工程师，希望改进围绕引用计数代码的调试、并减少内存破坏等相关问题。</p>   
</div>
            