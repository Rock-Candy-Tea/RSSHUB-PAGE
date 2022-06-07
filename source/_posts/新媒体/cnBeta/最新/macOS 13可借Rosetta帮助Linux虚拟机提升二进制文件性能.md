
---
title: 'macOS 13可借Rosetta帮助Linux虚拟机提升二进制文件性能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0607/07b444b4b3fca91.jpg'
author: cnBeta
comments: false
date: Tue, 07 Jun 2022 09:32:37 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0607/07b444b4b3fca91.jpg'
---

<div>   
苹果在 WWDC 2022 主题演讲期间介绍了 macOS 13“Ventura”，<strong>而新系统的一项有趣变化，就是能够利用 Rosetta 来快速执行在 ARM Linux 虚拟机上运行的 x86_64 二进制文件。</strong>此前，我们已经见识过该软件在 Apple Silicon Mac 设备上的出色性能表现。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0607/07b444b4b3fca91.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0607/07b444b4b3fca91.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（来自：Apple Developer <a href="https://developer.apple.com/videos/play/wwdc2022/10002/" target="_self">门户</a>）</p><p>通过两年时间，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>已在 Intel（x86_64）平台的二进制文件转译工作上取得了长足进步。</p><p>而在 macOS 13 中，苹果又宣布运行 ARM Linux 虚拟机的 Apple Silicon 系统，现已能够借助 Rosetta 来翻译 x86_64 的 Linux 二进制文件。</p><p>换言之，在 Apple Silicon（ARM）平台上运行的 Linux 虚拟机，将获得对 Linux x86_64 的良好支持。</p><p><img src="https://static.cnbetacdn.com/article/2022/0607/d3a11db4c588af6.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">这项 Rosetta 调用是基于 macOS 虚拟化框架实现的（来自：Apple <a href="https://developer.apple.com/videos/play/wwdc2022/10002/" target="_self">文档</a>）</p><p>鉴于苹果未向第三方公开 Apple Silicon Mac 的 Linux x86_64 发行版安装渠道（第三方移植工作距离可用仍属奢谈），经由虚拟机的用户空间应用程序二进制支持，就显得尤为重要。</p><p>此外由于这套 Rosetta 调用机制取决于 macOS 虚拟化框架和其它集成，我们也不奢望它能够在 macOS 之外套用（比如非 Apple ARM Linux 服务器、或 Asahi Linux 移植）。</p><p>展望未来，我们很是期待这项技术与竞争方案的性能 / 可靠性对比、及其是否适用于图形应用程序等场景 —— 比如让 Apple Silicon Mac 通过 Linux 虚拟机来运行 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 版 Steam 游戏。</p>   
</div>
            