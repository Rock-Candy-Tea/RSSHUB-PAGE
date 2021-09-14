
---
title: 'Linux Kernel 5.15将GCC版本要求提高到5.1'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Tue, 14 Sep 2021 07:43:22 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
<strong>上周日发布的 Linux Kernel 5.15 首个候选版本更新引入了诸多变化，不过在本周一引入的一项新变化中，提高了创建 Linux 内核的 GCC 版本门槛。</strong>目前，Linux Kernel 是基于 GCC 4.9 内核上构建的，现在它已经被提升到 GCC 5.1。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">AArch64 已经至少需要 GCC 5.1，而这次升级影响到所有其他架构。不过，除了那些试图在非常老的企业级 Linux 发行版上构建的人之外，其影响最终应该是非常小的。GCC 5.1 可以追溯到 2015 年的 GNU Compiler Collection 版本。所以基本上你需要一个过去六年内的编译器来构建 Linux 的 mainline 内核。</p><p style="text-align: left;">通过放弃 GCC5 之前的编译器支持，他们能够避免 GCC 4.9 的一些编译器警告，并放弃其他针对 GCC4 的变通方法。事实上，放弃 GCC5.1 之前的支持意味着删除了大约 350 行代码，并降低了围绕验证旧编译器支持的维护负担。</p><p style="text-align: left;">除了删除旧的兼容性残余和处理编译器的烦扰之外，这次迁移到GCC 5.1的最低版本确实意味着Linux内核有可能在未来的代码中从使用 C89（GNU89 同源语）切换到 C11（GNU11 同源语），但目前这个变化还没有在 mainline 上进行。</p>   
</div>
            