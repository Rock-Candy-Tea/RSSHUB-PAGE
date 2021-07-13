
---
title: 'Linux 5.15有望合并Memory Folios方案 内核构建速度可提升7%'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Tue, 13 Jul 2021 11:33:04 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
<strong>甲骨文公司的长期内核开发人员Matthew Wilcox已经研究了“内存对开区”概念相当长的一段时间，这可以改善Linux的内存管理，使其具有更大的效率。</strong>例如，使用内存对开的基准测试表明，内核的构建速度可以提高7%。现在看来，人们希望看到至少有一些这样的对开代码在Linux 5.15中得到应用。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p>Memory Folios为Linux内核提供了一个新的结构类型，以更好地管理内存，之前的补丁系列对现状和新的 "Folios"方法的问题进行了更详细的说明。</p><p>struct folio是一个新的抽象概念，取代了古老的struct page。一个函数如果接受了一个struct folio的参数，就声明它将对整个（可能是复合）页面进行操作，而不仅仅是PAGE_SIZE参数约定的数字。作为回报，调用者保证它所传递的指针不会指向一个尾部页面。</p><p>在Linux内核中使用这个新结构意味着要打几十个补丁，如果算上调整XFS文件系统以使用它和其他内核代码的工作，总共要打200多个补丁。</p><p>红帽公司的David Howells现在正在寻求至少核心的folios补丁可以在Linux 5.15中出现。鉴于Howells在Linux的网络文件系统支持库和本地文件系统缓存方面所做的大量工作，他希望能在下一个内核周期看到内存页对开特性的引入。</p>   
</div>
            