
---
title: '微软发布ARM64EC 17.3：Windows 11 on ARM迎来全面支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0810/9492f32750422fc.png'
author: cnBeta
comments: false
date: Wed, 10 Aug 2022 07:23:36 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0810/9492f32750422fc.png'
---

<div>   
早在 2021 年 6 月，微软就宣布了适用于 Windows 11 的 ARM64EC 。<strong>官方称之为一种使现有 x64 应用程序在 ARM 平台上获得近乎原生性能的新方法 —— 即便你调用了尚不支持该脚骨的插件和依赖项。</strong>转眼一年过去，ARM64EC 终于迎来了面向 Windows 11 的更完整支持。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0810/9492f32750422fc.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：C++ <a href="https://devblogs.microsoft.com/cppblog/official-support-for-arm64ec-is-here/" target="_self">Team Blogs</a>）</p><p>据悉，ARM64EC 的“EC”，是“仿真兼容”（Emulation Compatible）的缩写。</p><blockquote><p>其设想是提供一个二进制接口（ABI），以便开发者使用 x64 和 ARM 代码构建应用程序。</p><p>这意味着 ARM 代码可在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 设备上原生运行，而其它特定于 x64 的代码则会通过仿真方式运行。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0810/1b7931105c83a76.png" alt="2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：Windows <a href="https://blogs.windows.com/windowsdeveloper/2021/06/28/announcing-arm64ec-building-native-and-interoperable-apps-for-windows-11-on-arm/" target="_self">Blogs</a>）</p><p>作为 Windows on ARM 项目的一个重要里程碑，<strong>ARM64EC ABI 与 ARM64 ABI 之间的差异，主要体现在如下方面：</strong></p><blockquote><p>ARN64EC ABI 具有与 x64 代码的二进制兼容特性，且遵循着既有的 x64 软件约定。</p><p>其中包括调用约定（calling convention）、堆栈使用（stack usage），以及数据对齐（data alignment）。</p><p>这使得 ARM64EC 和 x64 代码具有可互操作的特性，基于前者构建的应用程序可能包含 x64 代码，但也不都如此。</p><p>因为 ARM64EC 本身有一套完整、一流的的视窗二进制接口（Windows ABI）。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0810/d79dca204cbab81.png" alt="3.png" referrerpolicy="no-referrer"></p><p>经过一年多的开发，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>现认为 ABI 已足够稳定，能够从实验阶段过渡到通用发布（<a href="https://docs.microsoft.com/en-us/windows/arm/arm64ec-build" target="_self">GA</a>）。</p><blockquote><p>随着 ARM64EC 17.3 版本的推出，其能够为开发者带来诸多益处。</p><p>比如开发者能够逐步更新他们的代码，让 x64 和 ARM 功能同时运行，而无需费心确保他们的整个代码库都具有与 ARM 平台的兼容性。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0810/e82a8249442dbb9.png" alt="arm64ec-vs-new-platform.png" referrerpolicy="no-referrer"></p><p>当然，在 Windows on ARM 设备上，还是原生 ARM 代码的性能要略胜一筹。</p><p>不过微软的想法，是通过持续不断的代码库更新来提升 ARM 性能，但又不至于在此过程中丢失任何功能特性。</p>   
</div>
            