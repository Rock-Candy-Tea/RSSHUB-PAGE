
---
title: 'LLVM_Clang添加了对ARMv9.3-A的支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0104/37cef41e69d7482.webp'
author: cnBeta
comments: false
date: Tue, 04 Jan 2022 02:53:50 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0104/37cef41e69d7482.webp'
---

<div>   
作为十年前推出的 ARMv8 的继任者，ARM 在去年宣布了 ARMv9 指令集。自发布时起，ARM 一直在努力将 ARMv9 支持添加到 GCC 和 LLVM/Clang 等开源编译器中。在几个月前，这些开源编译器已经初步支持 ARMv9，<strong>今天的 LLVM/Clang 上，它获得了对 ARMv9.3-A 的支持。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0104/37cef41e69d7482.webp" alt="f23yxui2.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">去年 9 月，ARM 概述了他们 2021 年的架构发展，包括优化的 memcpy 函数、不可屏蔽的中断、指针认证更新、PMU 更新和其他变化。这些2021年的更新被卷进 ARMv8.8-A 的形式，然后在 ARMv9世界中被称为ARMv9.3-A。</p><p style="text-align: left;">开源编译器已经解决了对ARMv8.8-A的支持，而今天进入主线LLVM的mono仓库的是ARMv9.3-A支持。LLVM补丁和Clang补丁重申，这是编译器已经支持的ARMv8.8-A扩展，但适用于ARMv9架构。考虑到已经有的v8.8-A支持，ARMv9.3-A的增加是相当小的。</p>   
</div>
            