
---
title: '谷歌从 Android 移除大量 Fuchsia 相关代码，Starnix 项目新进展曝光'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/7/aeab7141-2d3a-45df-8d94-250ada5dc025.jpg@s_2,w_820,h_410'
author: IT 之家
comments: false
date: Sat, 16 Jul 2022 05:39:10 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/7/aeab7141-2d3a-45df-8d94-250ada5dc025.jpg@s_2,w_820,h_410'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1385139" rel="nofollow">Coje_He</a> 的线索投递！</div>
            <p data-vmark="f19b"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 7 月 16 日消息，本周，谷歌从 <a class="s_tag" href="https://android.ithome.com/" target="_blank">Android</a> 开源项目 (AOSP) 中移除了大量关于 Fuchsia 的代码，但目前 Android 和 Fuchsia 依然有着紧密的联系。</p><p data-vmark="741f">谷歌内部操作系统 Fuchsia 目前仅支持该公司的两款智能显示屏 Nest Hub 和 Nest Hub Max，但谷歌野心不止于此。</p><p data-vmark="489a">谷歌希望让一些 Fuchsia 设备能够运行<a class="s_tag" href="https://android.ithome.com/" target="_blank">安卓</a>和 Linux 等其他操作系统的 App。当然，这在理论上是可以做到的。</p><p data-vmark="5acd">有几种方法可以实现这一目标，谷歌最早的尝试之一是在虚拟机中运行 Android 操作系统的完整实例，也正因此 Chrome OS 和 PC 版谷歌 Play Games 可以支持 Android 应用，但这种方案也存在一些潜在的性能缺陷。</p><p data-vmark="c5e4">此外，谷歌还探索了另一条路径，即 Fuchsia 与 Android Runtime 之间建立一种直接的联系。正如在 2019 年有媒体发现谷歌在 AOSP 代码中创建了一个项目，该项目将创建专为 Fuchsia 设备设计的 Android Runtime 的进程。</p><p data-vmark="bf30">IT之家了解到，这个名为“device /Google/ Fuchsia”的 Android 项目的已经在 2021 年 2 月停止支持，但至今都没有公开事情进展如何。</p><p data-vmark="8d11">本周，谷歌将所有“device /Google/ Fuchsia”的代码从 Android 中删除，这也标志着这条特殊路径的终结。</p><p data-vmark="8944">在移除之后，该项目只留下简单的“TODO”信息，表明 Google 正考虑去走出一条新的路径。负责这项更改的开发者正在开发 Fuchsia 的“Starnix”项目。</p><p data-vmark="c7a1">值得一提的是，该项目最早于 2021 年被曝光，Starnix 项目设计初衷就是让 Fuchsia 能够“原生”运行为 Linux / Android 开发的应用和库。为了实现这个目标，Starnix 还把底层内核指令从 Linux 转换成了 Fuchsia 的 Zircon 内核。</p><p data-vmark="fa3d">Starnix 的提议被接受并开始工作已经一年多了。在此期间，Fuchsia 团队在开发能够在 Fuchsia 设备上运行的 Linux 程序方面取得了重大进展。</p><p data-vmark="cca0">Fuchsia 项目团队正希望能够在 Fuchsia 设备上运行 Linux 程序。事实上，官方还提供了一个专用的 Starnix  Shell，可以帮助开发者和发烧友玩转 Fuchsia 工作站。</p><p data-vmark="0acb">值得注意的是，这个 shell 不是简单的 Linux 设计，而是一个“包含在系统中的小型 Android 发行版”。最近，这一功能还被替换成了通过 adb 命令访问 Fuchsia 和 Starnix 的 Android 功能，可以说就像访问任何其他 Android 设备一样简单。</p><p data-vmark="bfaa">展望未来，谷歌似乎准备将 Fuchsia 的 Starnix 团队去打造一种可以稳定与 Android 及其应用程序兼容的方案，而 Fuchsia 的路线图中也要求它可以更好地处理 Android 的“init”进程。</p><p data-vmark="768e">6 月份的时候，有另一个路线图项目指出谷歌希望在 Fuchsia 正确“启动和运行时钟应用”，这可能是指谷歌时钟或 AOSP 的开源“桌面时钟”。当然，这个特殊的项目在公布不久就对公众隐藏了，只有下面的截图得以流传。</p><p data-vmark="9bb1" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/7/aeab7141-2d3a-45df-8d94-250ada5dc025.jpg@s_2,w_820,h_410" w="1130" h="565" alt="t7amujmo.webp" title="谷歌从 Android 移除大量 Fuchsia 相关代码，Starnix 项目新进展曝光" srcset="https://img.ithome.com/newsuploadfiles/2022/7/aeab7141-2d3a-45df-8d94-250ada5dc025.jpg 2x" width="1130" height="410" referrerpolicy="no-referrer"></p><p data-vmark="5bbe">总而言之，谷歌 Fuchsia 团队似乎仍有在考虑打造智能家居之外的产品，例如将 Fuchsia 打造成一款类似安卓的通用操作系统，并兼容大量的 Android 应用。但目前还没有更多消息，谷歌打算将这些高端设计应用在什么样的设备上仍有待观察。</p>
          
</div>
            