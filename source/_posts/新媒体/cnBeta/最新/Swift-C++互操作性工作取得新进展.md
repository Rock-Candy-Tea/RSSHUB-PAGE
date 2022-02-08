
---
title: 'Swift-C++互操作性工作取得新进展'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0208/379d126743536a4.png'
author: cnBeta
comments: false
date: Tue, 08 Feb 2022 07:40:44 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0208/379d126743536a4.png'
---

<div>   
<strong>作为 Swift 项目的一部分，新成立的 Swift-C++ 互操作性工作组，将负责开发设计 C++ 和苹果 Swift 之间的互操作性模型。</strong>1 月 31 日的公告指出，开发者们对两种语言的双向互操作性，产生了相当浓厚的兴趣。具体说来是，该工作组将为 Swift 编译器增加“导入和使用某些 C++ API 的能力”。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0208/379d126743536a4.png" alt="1.png" referrerpolicy="no-referrer"></p><p>立项初期，Swift-C++ 工作组将致力于快速迭代、并完善两种语言之间的互操作层的目标设计，以及讨论对 Swift 编译器的相关更改，从而构建互操作性的支持框架。</p><p>公告补充道，Swift 编译器现可导入并使用某些 C++ API，包括 C++ 标准库类型 std:string 和 std::vector 。</p><p><img src="https://static.cnbetacdn.com/article/2022/0208/7d8cdf4d1133bef.png" alt="2.png" referrerpolicy="no-referrer"></p><p>此外 Swift <a href="https://forums.swift.org/t/swift-and-c-interoperability-workgroup-announcement/54998" target="_self">GitHub</a> 页面上发布的《C++ 互操作性宣言》，还描述了两种语言之间的双向 API 互操作性的设计目标。</p><p>至于广大开发者提议的更改，必须符合 Swift 的目标和理念，毕竟工作组不希望让 Swift 语言或标准库产生分叉。</p><p>所以主要的工作，还是聚焦在 C++ 代码、工具链、标准库实现、以及运行时环境的有限更改上。</p>   
</div>
            