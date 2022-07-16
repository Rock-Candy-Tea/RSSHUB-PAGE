
---
title: 'Android移除大量Fuchsia相关代码 Starnix项目新进展曝光'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0716/ff23c3ce110fc54.webp'
author: cnBeta
comments: false
date: Sat, 16 Jul 2022 03:17:11 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0716/ff23c3ce110fc54.webp'
---

<div>   
<strong>本周，Google 从 Android Open Source Project (AOSP) 中移除了大量关于 Fuchsia 的代码</strong>，但 Android 和 Fuchisia 依然有着紧密的联系。<br>
 <p style="text-align:center"><<img src="https://static.cnbetacdn.com/article/2022/0716/ff23c3ce110fc54.webp" alt="t7amujmo.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在目前官方提供的公开信息上，Fuchsia 系统目前仅适用于 Nest Hub 和 Nest Hubs Max 两款 Google 自家的智能屏幕设备。不过从过去几年的开发情况来看，Google 对 Fuchsia 有更高的期望。</p><p style="text-align: left;">在 Google 的设想中，Fuchsia 设备可以运行来自 Android 和 Linux 等其他系统的应用程序。而这在理论上可以让 Fuchsia 设备无缝替代 Chromebook 或者 Android <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>，让旧款应用也能顺畅运行。</p><p style="text-align: left;">想要达成这个目标有多种途径，其中一种也是 Google 最早尝试的是，在一个虚拟主机上运行完整的 Android 系统实例。虽然这种方式可以让 Chrome OS 和 Google Play Games for PC 引入对 Android 应用的支持，但是存在一些潜在的性能问题。</p><p style="text-align: left;">另一种方式就是增强 Fuchsia 和 Android Runtime 的直接关系。最早在 2019 年被发现，Google 基于公开 Android 代码（AOSP）创建了一个项目，能够为 Fuchsia 设备创建了 Android Runtime 版本。</p><p style="text-align: left;">在 2021 年 2 月启动的“device/google/fuchsia”，在 Android 设备中启动 Fuchsia 项目，只是目前并没有公开的进度指标。</p><p style="text-align: left;">而本周，“device/google/fuchsia”的代码已经从 Android 上移除，正式标志着这条特殊途径的结束。</p><p style="text-align: left;">在移除之后只留下简单的“TODO”信息，表明 Google 正计划创建新的东西。负责这项更改的开发者正在开发 Fuchsia 的“Starnix”项目。</p><p style="text-align: left;">该项目最早于 2021 年被曝光，Starnix 项目设计初衷就是让 Fuchsia 能够“原生”运行为 Linux/Android 开发的应用和库。为了实现这个目标，Starnix 项目将会扮演着翻译来自 Linux 的底层内核架构到 Fuchsia 的 Zircon 内核。</p><p style="text-align: left;">Fuchsia 项目团队正希望能够在 Fuchsia 设备上运行 Linux 程序。事实上专用的 Starnix  Shell 已经开放下载，用于测试 Fuchsia 的“工作站”，能够让开发者和忠实用户玩这款系统。</p>   
</div>
            