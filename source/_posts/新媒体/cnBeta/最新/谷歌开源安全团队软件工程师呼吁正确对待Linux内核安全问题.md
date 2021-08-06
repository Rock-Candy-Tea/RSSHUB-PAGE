
---
title: '谷歌开源安全团队软件工程师呼吁正确对待Linux内核安全问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0806/6b18f13b0f9f466.png'
author: cnBeta
comments: false
date: Fri, 06 Aug 2021 10:57:35 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0806/6b18f13b0f9f466.png'
---

<div>   
尽管即将迎来 30 周年，基于开源的 Linux，仍是计算机历史上最大的协作开发项目。围绕 Linux 的庞大社区，已让它能够顺利完成许多惊人的工作。与此同时，开发者们似乎缺乏对安全缺陷的注意力。<strong>谷歌开源安全团队软件工程师 Kees Cook 在一篇博客文章中指出：代码的健壮性与安全性之间有很强的联系。鉴于 Bug 已经很难查找，安全缺陷就更难显露出来。</strong><br>
<p><img src="https://static.cnbetacdn.com/article/2021/0806/6b18f13b0f9f466.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">谷歌呼吁正确面对 Linux 内核的安全性问题（来自：Google <a href="https://security.googleblog.com/2021/08/linux-kernel-security-done-right.html" target="_self">Security Blog</a>）</p><p>对于开发者来说，显然不该止步于此。当缺陷确实显现时，对其展开有效处理也是很有必要的。</p><p>通过先行一步，不仅能够一次修补一个 bug，还可阻止因其引发的不良影响。使用 C 语言编写的 Linux，显然也将长期面临这方面的问题。</p><blockquote><p>Kees Cook 指出，Linux 必须采取更加主动的安全措施，以保护自身免受相关风险的影响。</p><p>举个例子，汽车之所以强制配备安全带，并不是我们有意要撞车，而是因为危险随时可能降临。</p></blockquote><p>即使每个人都希望在他们的计算机、移动设备、或交通工具上运行一个安全的内核，也不是每个人都有能力做些什么。</p><blockquote><p>上游内核开发人员能够修复 bug，但无法控制下游供应商选择将哪些内容整合到他们的产品之中。</p><p>最终用户可以选择他们需要的产品，但通常也无法控制修复了哪些 bug、或使用了哪些内核（有时内核本身也是个问题）。</p></blockquote><p>综上所述，最佳的办法，就是让供应商对其产品的内核安全负起责任来。</p><p><img src="https://static.cnbetacdn.com/article/2021/0806/180a203ca992e2a.png" referrerpolicy="no-referrer"></p><p>尽管许多供应商都在受到恶意软件、僵尸网络、以及针对有缺陷软件的攻击时选择做一只鸵鸟，但 Kees Cook 还是希望他们能支棱起来。</p><p>通常情况下，这些厂商会将自家设备视作一款物理产品，而不是需要定期更新的“混合服务”产品。</p><p>除了鼓励厂商尽可能早地修复所有 Bug，谷歌安全团队还希望让更多工程师能参与到代码审查、安全测试、工具链开发、以及基础设施改进等工作中来。</p><p>根据他们最保守的估计，当前的百余名工程师，仍不足以充分支撑 Linux 内核及其工具链的相关开发工作。</p><p>但这种“上游优先”的产品内核开发与测试方法，其实已被证明相当有效。比如在 Chrome OS 和 Android 的开发项目上，谷歌就已经落实了有一段时间了。</p>   
</div>
            