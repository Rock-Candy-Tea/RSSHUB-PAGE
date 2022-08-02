
---
title: '开发者提议清理Linux内核中长期过时的DECnet网络代码'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0802/69ac70f31e873cc.png'
author: cnBeta
comments: false
date: Tue, 02 Aug 2022 06:24:51 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0802/69ac70f31e873cc.png'
---

<div>   
作为 Digital Equipment Corporation 的一组网络协议，DECnet 可追溯到 1975 年。<strong>但是这个早已过时的协议，还是在 Linux 内核中留存了十多年的时间。</strong>与主线内核相比，它更像是该丢进历史博物馆的代码。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0802/69ac70f31e873cc.png" referrerpolicy="no-referrer"></p><p><a href="https://www.phoronix.com/news/Linux-DECnet-2022-Removal" target="_self">Phoronix</a> 指出，DEC 为实现数字网络架构的软硬件网络产品而开发了 DECnet 。</p><p>作为 80 年代的早期点对点网络架构之一，内置于 DEC 的 VMS 中的它，在那个时代有其历史积极意义。</p><p>然而自 90 年代初以来，它就已经显得过时且鸡肋。然而为了照顾极少数的使用需求，DECnet 代码还是长期滞留于 Linux 内核之中。</p><p><img src="https://static.cnbetacdn.com/article/2022/0802/a57482784bc0e29.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：<a href="https://lore.kernel.org/lkml/20220731190646.97039-1-stephen@networkplumber.org/" target="_self">LKML</a>）</p><p>好消息是，Stephen Hemminger 在 7 月底提交了一份“意见征求稿”，希望大家能够支持从 Linux 内核中移除死而不僵的 DECnet 代码。</p><blockquote><p>DECnet 是一项过时的网络协议，但比之普通用户，内核管理人员对它的关注度要更高。</p><p>它本就该被丢进计算机协议的历史博物馆，而不是在 Linux 内核中苟延残喘。</p><p>由 Sourceforge 上的文档链接可知，自 2010 年以来，其在内核中就一直处于被孤立的状态。</p>在编译用户空间程序时，还请将该 UAPI 扔到一边吧！</blockquote><p>此外 Linux 开发者 David Laight 补充道：“Linux 起初受到了让人惊叹的支持，但当我在 1990 年代初编写以太网驱动程序时，DECnet 它早就已经过时了！”</p><p>最后，目前这份建议文档（<a href="https://lore.kernel.org/lkml/20220731190646.97039-1-stephen@networkplumber.org/#r" target="_self">RFC</a>）仍在邮件列表中浮动。若最终顺利清理掉，Linux 内核将可精简掉大约一万二千行代码。</p>   
</div>
            