
---
title: 'Chrome安全团队希望将指针错误消灭在编译阶段'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0924/4bb5fc92436fd49.png'
author: cnBeta
comments: false
date: Fri, 24 Sep 2021 09:48:33 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0924/4bb5fc92436fd49.png'
---

<div>   
在计算机安全领域，攻击者的手段也在不断创新。为了构筑坚实的浏览器安全防线，谷歌已经为 Chrome 打造了基于沙箱和站点隔离的多进程架构。<strong>不过在近日发布的一篇博客文章中，Chrome 安全团队进一步介绍了他们在内存安全性方面的最新努力。</strong><br>
<p><img src="https://static.cnbetacdn.com/article/2021/0924/4bb5fc92436fd49.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：Google <a href="https://security.googleblog.com/2021/09/an-update-on-memory-safety-in-chrome.html" target="_self">Security Blog</a>）</p><p>Chrome 安全团队称，尽管他们在努力坚守上述主要的安全防线，但模糊测试的结果表明，这些措施的防护效果已达到极限，意味着浏览器开发商无法再单纯依靠单纯的策略来抵御野外攻击。</p><p>数据表明，去年的时候，有超过 70% 的严重安全漏洞都与内存相关，尤其是 C / C++ 编程语言中的指针 bug 会导致内存误解。在浏览器应用之外，内存安全也是一个需要全球软件工程社区认真对待的问题。</p><p>与此同时，Chrome 安全团队认为这也是一个机遇，毕竟许多 bug 都具有类似的根本原因，意味着我们能够一次搞定大部分问题。为此，Chrome 安全团队提出了三个着力点：</p><blockquote><p>（1）在编译时检查指针是否正确；</p><p>（2）在运行时检查指针是否正确；</p><p>（3）调查现有代码库部分内存安全语言的使用。</p></blockquote><p>“编译时检查”意味着在 Chrome 构建过程中确保安全，甚至早于向用户设备推送更新之前。</p><p>“运行时检查”意味着 Chrome 浏览器会在终端设备上运行软件时进行检查。当然，这么做也会有一定的性能成本开销。</p><blockquote><p>考虑到有数百万计的指针，即使每个指针的影响都极其细微，数十亿的用户量级，累加起来还是相当可观的，尤其许多用户仍在使用资源相对受限的低功耗移动设备。</p><p>在理想情况下，Chrome 安全团队倾向于优先选择第（1）套方案。遗憾的是，C++ 编程语言在设计之初并没有考虑到这一点。</p><p>权衡利弊之后，我们最终只剩下了让 C++ 更安全（但也更慢）的第（2）和第（3）种选项，或尝试开始使用其它编程语言。</p></blockquote><p>换言之，Chrome 安全团队将在 C++ 安全解决方案上倾注大量的心力，例如 MiraclePtr 和 ABSL / STL 强化模式。</p><p>在每种情况下，我们都希望消除相当一部分可被利用的安全漏洞，但预计也会造成一些性能损失。</p><blockquote><p>比如借助 MiraclePtr 隔离潜在会被引用的内存，以预防释放后的隐患。而在内存资源更加宝贵的大部分移动设备上，我们很难专门腾出一块专门的隔离区。</p><p>即便如此，MiraclePtr 仍有望消除浏览器进程中超过 50% 的释放后错误使用 —— 对于当前的 Chrome 安全性来说，这已经算得上是一个相当瞩目的成就。</p></blockquote><p>同时，Chrome 安全团队将探索未来是否能够把 Chrome 的某些部分用“内存安全语言”进行重构 —— 比如当前被寄予厚望的 Rust（由 Mozilla 雇员 Graydon Hoare 创立）。</p><p>由于 Rust 编程语言保障了编译时的安全性，所以编译器能够早在代码抵达用户设备前排除指针错误，从而避免进一步的性能损失。至于 C++ 能否与 Rust 良好配合，仍有待时间去检验。</p>   
</div>
            