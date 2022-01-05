
---
title: '甲骨文CleanCache在被夸大宣传了十年后将从Linux内核中移除'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0105/9ca5ab950ab6c7c.jpg'
author: cnBeta
comments: false
date: Wed, 05 Jan 2022 11:28:19 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0105/9ca5ab950ab6c7c.jpg'
---

<div>   
<strong>十年前，CleanCache补丁系列被并入Linux内核主线，但现在它将退役。今天，作为Andrew
Morton补丁的一部分，合并到Linux-Next中的CleanCache被移除了。为什么？因为它已经没有用户了。</strong>自从2019年移除Xen
Transcendent Memory（TMEM）驱动代码后，CleanCache已经没有任何用户了，但代码仍然在内核中赋闲。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0105/9ca5ab950ab6c7c.jpg" title alt="transcendent-memory-not-just-for-virtualization-anymore-41-638.jpg" referrerpolicy="no-referrer"></p><p>CleanCache是由甲骨文的工程师开发的，在推出时，他们宣布它是"非常酷的东西，有巨大的潜力使运行的虚拟机大幅优化/性能/效率，是相当多的研究和实验的结果。"</p><p>它在内核的文档更保守地将其总结为："CleanCache是由VFS层提供的一个新的可选功能，它有可能为许多环境中的许多工作负载大大增加页面缓存的有效性，而成本可以忽略不计。CleanCache可以被认为是一个页面粒度的受害者缓存（Victim Cache），一个与直接匹配或低相联缓存并用的、容量很小的全相联缓存。用于存放内核的页框替换算法（PFRA）想要保留但由于没有足够的内存而无法保留的干净页面。因此，当PFRA"驱逐"一个页面时，它首先试图使用CleanCache代码将该页面中包含的数据放入内核不能直接访问或寻址的内存，其大小未知且可能随时间而变化。</p><p>但是，在被甲骨文公司吹嘘了十年后的今天，没有内核代码使用它，因此它将退役，随着它在Linux-Next中作为AKPM补丁的一部分被移除，它很可能在Linux 5.17中被主线移除。</p><p><strong>Linux内核网站文档：</strong></p><p><a href="https://www.kernel.org/doc/html/latest/vm/cleancache.html" _src="https://www.kernel.org/doc/html/latest/vm/cleancache.html" target="_blank">https://www.kernel.org/doc/html/latest/vm/cleancache.html</a><br></p><p><strong>甲骨文网站发布时的新闻稿：</strong></p><p><a href="https://blogs.oracle.com/wim/post/another-feature-hit-mainline-linux-cleancache-transcendent-memory" _src="https://blogs.oracle.com/wim/post/another-feature-hit-mainline-linux-cleancache-transcendent-memory" target="_blank">https://blogs.oracle.com/wim/post/another-feature-hit-mainline-linux-cleancache-transcendent-memory</a><br></p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1222045.htm" target="_blank">阿里巴巴为Linux内核调度器提出组平衡器（GB）概念</a></p></div>   
</div>
            