
---
title: 'iPadOS 16代码揭示_内部模式_旧款iPad亦可启用Stage Manager'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0614/c3033d28ed3c94f.webp'
author: cnBeta
comments: false
date: Thu, 16 Jun 2022 03:36:13 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0614/c3033d28ed3c94f.webp'
---

<div>   
早些时候，苹果软件工程主管 Craig Federighi 曾解释为何这项功能仅限于 M1 iPad 。但是本周，我们又看到了与 Stage Manager 相关的另一篇文章。<strong>可知 iPadOS 16 代码中提到的一种“内部模式”，可让非 M1 iPad 也获得这一多任务处理 / 叠放式窗口体验。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0614/c3033d28ed3c94f.webp" referrerpolicy="no-referrer"></p><p><a href="https://9to5mac.com/2022/06/15/ipados-16-internal-stage-manager-older-ipads/" target="_self">9to5Mac</a> 发现，这些代码引用了一项被称作“Legacy Devices”的内部设置，能够为旧设备启用“Chamois”功能（Stage Manager 的代号）。</p><p>遗憾的是，根据 Craig Federighi 的说法 —— <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>在推出 Stage Manager 前，曾于更多型号的 <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fipad%2F" target="_blank">iPad</a> 上开展过测试，最终确定只有 M1 iPad 才能确保带来理想的使用体验。</p><p>即便如此，感兴趣的开发者们，还是可以尝试于 iPadOS 16 的首个 Dev 测试版本中打开这个隐藏选项（可能遇到卡顿等意外问题）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0614/d87dbe1f9e7408c.webp" referrerpolicy="no-referrer"></p><p>此外 Craig Federighi 有在早前接受采访时称，虚拟内存交换对于 Stage Manager 的体验构建至关重要 —— 因为该功能最多支持同时打开八个应用程序窗口（主屏 4 个 + 外接显示器 4 个）。</p><p>矛盾的是，我们后来发现位于支持列表中的 64GB 入门款 iPad Air 5，本身又是缺乏 memory swap 的（via <a href="https://9to5mac.com/2022/06/14/ipad-air-5-lacks-memory-swap-stage-manager/" target="_self">9to5Mac</a>）。</p><p>该高管还指出，Stage Manager 具有流畅的动画和漂亮的阴影，所以对硬件要求也较高。但是这一说法同样存在争议，毕竟可升级 macOS Ventura 的 2017 Intel Mac 也支持它。</p><p><img src="https://static.cnbetacdn.com/article/2022/0614/d2a56d1e2667808.webp" referrerpolicy="no-referrer"></p><p>当目前尚不清楚苹果是否会为 iPadOS 16 / Stage Manager 重新划定标线。</p><p>不过去年一度仅限 M1 Mac 的 macOS Monterey / Live Text 功能，最终也在广大用户的口诛笔伐下被投放到了 Intel Mac 上。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1280523.htm" target="_blank">苹果软件工程主管强调为何Stage Manager功能仅限M1 iPad</a></p></div>   
</div>
            