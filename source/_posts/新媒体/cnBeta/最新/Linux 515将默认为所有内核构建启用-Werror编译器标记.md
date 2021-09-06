
---
title: 'Linux 5.15将默认为所有内核构建启用-Werror编译器标记'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0906/33ec0a70279cb16.png'
author: cnBeta
comments: false
date: Mon, 06 Sep 2021 03:22:59 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0906/33ec0a70279cb16.png'
---

<div>   
<strong>在近日的 Linux 5.15 内核合并中，Linus Torvalds 介绍了一项重要更改 —— 所有内核构建将默认启用“-Werror”编译器标记。</strong>据悉，该标记会将所有警告都视作编译错误，以迫使开发者提起重视并优先处理，否则将中断编译过程。此前已有许多软件项目默认采取了相同措施来加强质量控制，但它们大多没有精细到 Linux 内核这样的程度。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0906/33ec0a70279cb16.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=3fe617ccafd6f5bb33c2391d6f4eeb41c1fd0151" target="_self">Kernel.org</a>）</p><p>Linus Torvalds 评论道：“我们切实需要一个始终纯净的编译环境，并将按需禁用特定的过于急切的警告”。</p><p>遗憾的是，尽管 Linus 在自己的树中严格遵循强制执行，但某些编译器还是会忽视相关警告，因而他才下定决定让“-Werror”标记被默认启用。</p><p>与此同时，该补丁添加了将 WERROR 作为 Kconfig 开关的选项。若新版编译器引入了内核无法立即修复的新警告、或其它选择性问题，开发者还是被允许禁用该标记的的。</p><p>Linus Torvalds 补充道：“但愿这么做会让我们受到更少的查询请求，因为它们总是包含了我们现有的各种自动化流程中没有留意到的新警告”。</p>   
</div>
            