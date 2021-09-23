
---
title: 'Google提出_上游优先_理念 目标消除Android碎片化痛点'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0923/ea777de44e2711b.jpg'
author: cnBeta
comments: false
date: Wed, 22 Sep 2021 23:55:24 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0923/ea777de44e2711b.jpg'
---

<div>   
Android 操作系统一直以来被人所诟病的一点就是，由移动运营商把持的所有下游补丁以及各种供应商/设备控制的内核树。<strong>为进一步减少碎片化，近年来越来越多的代码开始上游化，而且 Google 正努力让所有新产品的内核都基于 Android Generic Kernel Image (GKI) 。</strong><br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0923/ea777de44e2711b.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0923/ea777de44e2711b.jpg" alt="iq50jgpz.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">展望未来，Google现在正在谈论一种“上游优先”（upstream first）的方法来推送新的内核功能。在今天召开的 Linux Plumbers 大会（LPC2021）上，Google 的 Todd Kjos 围绕着 GKI 计划进行了演讲。</p><p style="text-align: left;">在 Android 12 和基于 Linux 5.10 的 GKI 镜像，Google 已经进一步减少了碎片化，以至做到了“几乎消除”。在 Android 12 的 GKI 中，大部分供应商/OEM 的内核功能现在要么被上游到 Linux 内核中，要么被隔离到供应商模块/钩子中，要么被合并到 Android Common Kernel 中。</p><p style="text-align: left;">Google 在 GKI 方面取得了良好的进展，同时也确保供应商适应新的方法，以减少内核的混乱。但最令人兴奋的可能是他们对 2023 至 2024 年进一步减少技术债务的展望。他们将追求“新功能的上游开发模式”，确保新代码首先进入 Linux 内核 Mainline，而不是直接在 Android 源码树中寻找宿主。</p><p style="text-align: left;">Google 还承诺“努力将 Android Common Kernels 中的所有树外补丁上游化”。</p>   
</div>
            