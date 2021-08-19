
---
title: '因微软未在限定90天内修复 Google Project Zero团队披露权限提升漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0819/d2f1e0f2fbfa64a.jpg'
author: cnBeta
comments: false
date: Thu, 19 Aug 2021 08:57:30 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0819/d2f1e0f2fbfa64a.jpg'
---

<div>   
<strong>由于微软并没有在限定的 90 天时间内修复漏洞，<a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2207&can=2&q=&colspec=ID%20Type%20Status%20Priority%20Milestone%20Owner%20Summary&cells=ids" target="_blank">Google 的 Project Zero 团队近日披露了存在于 Windows 系统中的权限提升（EoP）漏洞</a>。</strong>这个漏洞是因为 Windows 过滤平台（WFP）的默认规则允许可执行文件连接到 AppContainers 中的 TCP 套接字，这导致了 EoP。基本上，WFP中定义的一些规则可以被恶意行为者匹配，以连接到 AppContainer 并注入恶意代码。<br>
  <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0819/d2f1e0f2fbfa64a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0819/d2f1e0f2fbfa64a.jpg" alt="j82gcmum.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">Project Zero 团队运行机制是这样的：发现漏洞后报告给厂商，并给予 90 天的时间进行修复。如果厂商没有在限期内进行修复，那么团队就会公开披露。自然，根据所需修复的复杂性，团队有时还会以宽限期的形式提供额外的时间。</p><p style="text-align: left;">报告该漏洞的安全研究员James Forshaw接着说。</p><blockquote style="text-align: left;"><p style="text-align: left;">这当然是一个普遍的问题，如果任何应用程序添加了许可规则，可以通过 AppContainer 到达，那么这些规则可以在阻止规则之前被匹配。当然，这无疑是设计上的问题，但这里的问题是这些规则在我测试过的所有系统中都是默认存在的，因此任何系统都会有漏洞。请注意，这并不允许访问 localhost，因为这在 ACCEPT/RECV 层是失败的，它提前阻止了 AppContainer 的 localhost 连接。</p><p style="text-align: left;">从修复的角度看，也许这些默认规则不应该与AC进程相匹配（所以要添加FWPM_CONDITION_ALE_PACKAGE_ID的检查），或者它们应该在AC阻止规则之后排序。也可能是它们太灵活了，即使限制在一个特定的端口，至少也能减少攻击面。我不确定是否有解决这个问题的一般方法，但由于AC进程不能列举当前的规则（AFAIK），那么AC进程将永远不知道是否有非默认的规则被添加，他们可以滥用。</p></blockquote>   
</div>
            