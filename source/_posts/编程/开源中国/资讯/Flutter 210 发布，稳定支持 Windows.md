
---
title: 'Flutter 2.10 发布，稳定支持 Windows'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0204/085519_8USU_4937141.png'
author: 开源中国
comments: false
date: Fri, 04 Feb 2022 08:57:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0204/085519_8USU_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>Flutter 2.10 正式发布，该版本距离上个版本的发布还不到两个月时间，但即使在这么短的时间内，Flutter 已经关闭了 1843 个问题，合并了 1525 个 PR。</p> 
<h3>稳定支持 Windows</h3> 
<p><img alt height="394" src="https://static.oschina.net/uploads/space/2022/0204/085519_8USU_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>Flutter 已支持 Linux，针对 Windows 和 macOS 的测试版也已推出一段时间了，如今 Windows 版本正式结束测试，达到稳定状态。</p> 
<p>Flutter 2.10 除了带来了对 Windows 的稳定支持以外，这个版本还包括对文本处理、键盘处理和键盘快捷键的大量改进，以及直接集成到 Windows 的新功能，支持命令行参数、全局化文本输入和可访问性。</p> 
<h3>性能改进</h3> 
<p><img alt height="351" src="https://static.oschina.net/uploads/space/2022/0204/085507_wJ8W_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>这个版本的 Flutter 包括由 Flutter 社区成员 knopp 提供的对 <strong>dirty region management</strong> 的初步支持。他启用了 iOS/Metal 上单个 <strong>dirty region</strong> 的部分重绘。这一变化将一些基准上的光栅化时间降低了一个数量级，并将这些基准上的 GPU 利用率从 90% 以上降低到 10% 以下。</p> 
<p>这个版本还包括一个更快的类型流分析的实现。在官方的基准测试中，Flutter 应用程序的总体构建时间下降了~10%。</p> 
<h3>iOS 更新</h3> 
<p>除了性能改进，Flutter 2.10 还增加了一些特定平台的功能和改进。一个新的增强功能是在 iOS 中提供更流畅的键盘动画，这将自动提供给你的应用程序，开发者不需要做任何事情。</p> 
<p>该版本还改善了 iOS 的相机插件稳定性，修复了一些情况下产生的崩溃问题。最后，64 位 iOS 架构得到了一个新的功能，以减少内存的使用：<strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fengine%2Fpull%2F30077" target="_blank">compressed</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fengine%2Fpull%2F30333" target="_blank">pointers</a></strong>。</p> 
<h3>Android 更新</h3> 
<p>这个版本也包含了一些针对 Android 的改进。默认情况下，当创建一个新的应用程序时，Flutter 默认支持最新的 Android 版本，即 Android 12。此外在这个版本中，已经自动启用了 multidex 支持。</p> 
<p>Flutter 工具现在会对常见的问题给出解决步骤。例如，如果你在你的应用程序中添加了一个插件，需要你升级支持的 Android SDK 版本，那么现在会在日志中看到一个 "Flutter Fix" 的建议。</p> 
<h3>VS Code 改进</h3> 
<p>Flutter 的 Visual Studio Code 扩展也得到了一些改进，新版本中，你可以在代码的更多地方进行颜色预览，以及一个可以为你更新代码的颜色选择器。</p> 
<p><img alt height="264" src="https://static.oschina.net/uploads/space/2022/0204/085453_lry6_4937141.gif" width="700" referrerpolicy="no-referrer"></p> 
<p>此外，如果你想成为 VS Code 的 Dart 和 Flutter 扩展的预发布版本的测试者，你可以在你的扩展设置中切换到预发布版本。</p> 
<h3>不再支持 iOS 9/10</h3> 
<p>由于使用量的减少和维护目标设备的难度增加，因此在 2022 年第三季度的稳定版中，将从 Flutter 稳定版中放弃对 32 位 iOS 设备和 iOS 9 和 10 版本的支持。这意味着在那之后，根据稳定的 Flutter SDK 构建的应用程序将不再适用于 32 位 iOS 设备，Flutter 支持的最小 iOS 版本将更新到 iOS 11。</p> 
<p>……</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fflutter%2Fwhats-new-in-flutter-2-10-5aafb0314b12" target="_blank">https://medium.com/flutter/whats-new-in-flutter-2-10-5aafb0314b12</a></p>
                                        </div>
                                      
</div>
            