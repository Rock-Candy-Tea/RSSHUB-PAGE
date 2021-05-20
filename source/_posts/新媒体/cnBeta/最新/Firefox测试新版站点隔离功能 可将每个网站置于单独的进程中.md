
---
title: 'Firefox测试新版站点隔离功能 可将每个网站置于单独的进程中'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0520/5deec93af306de0.jpg'
author: cnBeta
comments: false
date: Thu, 20 May 2021 07:32:18 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0520/5deec93af306de0.jpg'
---

<div>   
<strong>Mozilla 当前正在 Firefox 每夜构建版（Nightly Build）和 Beta 通道测试一项全新的安全体系架构，特点是能够将每个站点都置于单独的操作系统进程中。</strong>由官方描述可知，当前在 Firefox 启动时，浏览器将启动一个具有特权的父进程、八个 Web 内容进程、最多两个附加的半特权 Web 内容进程，以及四个用于 Web 扩展、GPU 操作、联网和媒体解码的实用程序进程。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0520/5deec93af306de0.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0520/5deec93af306de0.jpg" alt="mozilla-site-isolation.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">Firefox 站点隔离功能示意（来自：Mozilla <a href="https://hacks.mozilla.org/2021/05/introducing-firefox-new-site-isolation-security-architecture/" target="_self">官网</a>）</p><p>不过在设置了一定数量的进程之后，后续很可能将恶意站点放入另一个站点已在使用的同一进程中，并赋予其访问共享进程内存的权限。</p><p>在利用 Spectre 漏洞攻击的情况下，恶意站点很可能借此取得同一进程中其它站点的数据。</p><p>此外现有方案意味着任何广告、或嵌入页面和子帧的内容，都将与父页面置于相同的进程中，而不会区分它们是否来自同一站点。</p><p>庆幸的是，在实施了“站点隔离”政策之后，不属于同一站点的每个嵌入式元素都将具有各自的进程，然后客户端操作系统将为浏览器提供内存防护和安全性保证。</p><blockquote><p>Mozilla 高级平台工程师 Anny Gakhokidze 在博客中写道：在更危险的情况下，恶意站点可能将合法站点嵌入子帧，并试图诱骗受害者输入敏感信息。</p><p>在成功执行类似 Spectre 攻击的情况下，顶级站点可能会从其嵌入的子帧访问其不应访问的敏感信息（反之亦然）。</p><p>而新版 Firefox 浏览器引入的站点隔离安全架构，将有效地提升恶意站点执行此类攻击的难度。</p><p>此外 Firefox 会将同一网站的 http 和 https 版本都视作不同的站点，意味着两者也将置于单独的进程中。</p></blockquote><p>ZDNet 指出，该功能将充分利用由社区维护的有效顶级域名列表，其中包括了 github.io 和 blogger.com 等在内站点。</p><p>这些网站拥有许多子域名节点，所以 Firefox 也会将各个子版块都视作单独的站点来实施隔离。</p><p>Anny Gakhokidze 补充道，新架构也在其它方面改善了 Firefox 的体验：</p><blockquote><p>比如一个站点消耗的计算资源（或垃圾收集）不该导致其它页面的响应能力降级、或者在页面崩溃的时候波及其它进程中的网页。</p><p>更棒的是，通过使用更多进程来加载网站，将使得我们能够把工作分配到许多 CPU 核心，从而更高效地利用底层硬件。</p></blockquote><p>据悉，Firefox 早在 2019 年初就首次带来了名为“Project Fission”的站点隔离功能，而竞争对手谷歌为 Chrome 实施的站点隔离方案也有一段时间了。</p><p>感兴趣的朋友，可尝试在 Firefox Nightly 中导航至 about:preferences#experimental，然后启用 Fission 复选框并重启浏览器。</p><p>至于 Firefox 正式版 / Beta 通道的用户，亦可导航至 about:config 页面，然后将 fission.autostart 设定为启用，并重启浏览器。</p><p>最后，Linux 平台的 Firefox 用户请注意，Project Fission <a href="https://wiki.mozilla.org/Project_Fission" target="_self">Wiki 页面</a>上的许多已知问题表明，你们可能遭遇内存使用量过多、以及 X11 连接器耗尽资源等 Bug 。</p>   
</div>
            