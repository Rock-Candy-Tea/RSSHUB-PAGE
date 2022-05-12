
---
title: '谷歌发布 Flutter 3'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5713f20bf8c6f4b639a5ef41edc4ae684d6.png'
author: 开源中国
comments: false
date: Thu, 12 May 2022 07:45:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5713f20bf8c6f4b639a5ef41edc4ae684d6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>谷歌宣布推出 Flutter 3。Flutter 3 完成了谷歌从以移动为中心到多平台框架的路线图，提供了 macOS 和 Linux 桌面应用程序支持，以及对 Firebase 集成的改进、新的生产力和性能特性，并支持 Apple Silicon。</p> 
<p><img alt height="281" src="https://oscimg.oschina.net/oscnet/up-5713f20bf8c6f4b639a5ef41edc4ae684d6.png" width="500" referrerpolicy="no-referrer"></p> 
<p>公告指出，Flutter 3 是谷歌完善 Flutter 所支持的平台的旅程的高潮部分；Flutter 3 中增加了对 macOS 和 Linux 应用程序的稳定支持，目前其已完成对 6 个主要平台的稳定支持。现在，<strong>Flutter 可用于构建跨 Android、iOS、Web（桌面）、Linux、Windows 桌面和 macOS 的生产级应用程序。</strong></p> 
<p>添加平台支持需要的不仅仅是渲染像素：它包括新的输入和交互模型、编译和构建支持、可访问性和国际化以及特定于平台的集成。谷歌方面表示，其目标是让用户能够灵活地充分利用底层操作系统，同时根据自己的选择共享尽可能多的 UI 和逻辑。</p> 
<p><span style="background-color:#ffffff"><span style="color:#000000">在 macOS 上，Flutter 原生支持 Intel 和 Apple Silicon。</span></span><span style="background-color:#ffffff"><span style="color:#292929">在 Linux 上，Canonical 和 Google 合作提供了一个高度集成的、同类最佳的开发选项。Flutter 3 还包含了一些性能改进、Material You 支持和生产力更新。</span></span></p> 
<p><span style="background-color:#ffffff"><span style="color:#292929">“</span></span>在这个版本中，Flutter 完全原生于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsupport.apple.com%2Fen-us%2FHT211814" target="_blank">Apple 芯片</a>上进行开发。虽然 Flutter 自发布以来一直与基于 M1 的 Apple 设备兼容，但 Flutter 现在充分利用了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fdartlang%2Fannouncing-dart-2-14-b48b9bb2fb67" target="_blank">Dart 对  Apple 芯片的支持</a>，从而能够在基于 M1 的设备上更快地编译并支持 macOS 应用程序的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fapple-silicon%2Fbuilding-a-universal-macos-binary" target="_blank">通用二进制文件。</a><span style="background-color:#ffffff"><span style="color:#292929">”</span></span></p> 
<p>有关 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fm3.material.io%2F" target="_blank">Material Design 3</a> 的工作在此版本中基本完成，允许开发人员利用可提供动态配色方案和更新的视觉组件的适应性强的跨平台设计系统：</p> 
<p><img alt height="260" src="https://oscimg.oschina.net/oscnet/up-779e046abc22021a47157652d1de6a092f6.png" width="500" referrerpolicy="no-referrer"></p> 
<p>谷歌在该周期中对 Dart 的工作包括减少 <span style="background-color:#ffffff"><span style="color:#292929">boilerplate </span></span>和提高可读性的新语言功能、实验性 RISC-V 支持、升级的 linter 和新文档。有关 Dart 2.17 中所有新改进的更多详细信息，可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fdartlang" target="_blank">博客</a>。</p> 
<p><span style="background-color:#ffffff"><span style="color:#000000">Flutter 现在提供<strong>与 Firebase 的一流集成。</strong>“今天，我们</span></span>宣布 Flutter/Firebase 的集成将成为 Firebase 产品的一个完全支持的核心部分。我们正在将源代码和文档转移到主要的 Firebase 存储库和站点中，你可以期望我们与 Android 和 iOS 同步发展 Firebase 对 Flutter 的支持。<span style="background-color:#ffffff"><span style="color:#000000">”</span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#292929"><span style="background-color:#ffffff">此外，还进行了重大改进，以支持使用 Firebase 流行的实时崩溃报告服务 Crashlytics 的 Flutter 应用程序。</span></span>通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffirebase.google.com%2Fdocs%2Fcrashlytics" target="_blank">Flutter Crashlytics 插件</a>的更新，你可以实时跟踪致命错误，为你提供与其他 iOS 和 Android 开发人员相同的功能集。<span style="color:#292929"><span style="background-color:#ffffff">并简化了插件设置过程，因此只需几个步骤即可从你的 Dart 代码中启动和运行 Crashlytics。</span></span></p> 
<p>为了让休闲游戏开发者更容易使用 Flutter 及其硬件加速图形支持来制作游戏，谷歌现在还提供了一个 <strong>Flutter 休闲游戏工具包</strong>，它提供了一个模板和最佳实践的入门工具包以及广告和云服务的积分，并<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fashehwkdkdjruejdnensjsjdne.web.app%2F%23%2F" target="_blank">使用 Flutter 和 Firebase 创建了一个基于网络的弹球游戏</a>。</p> 
<p><img alt height="281" src="https://oscimg.oschina.net/oscnet/up-fa0496fbeb2bf9422a3bb5b141779b83aa6.png" width="500" referrerpolicy="no-referrer"></p> 
<p>谷歌方面表示，其<span style="color:#292929"><span style="background-color:#ffffff">创建 Flutter 是为了彻底改变应用程序开发：将 Web 的迭代开发模型与以前游戏保留的硬件加速图形渲染和像素级控制相结合。自 Flutter 1.0 beta 发布以来的过去四年里，他们逐渐在这些基础上进行构建，添加了新的框架功能和新的小部件，与底层平台更深入地集成，丰富的包库以及许多性能和工具改进。</span></span></p> 
<p><span style="background-color:#ffffff"><span style="color:#292929"><img alt height="147" src="https://oscimg.oschina.net/oscnet/up-2a7c70eae5019fc2761fe7e1c64cd15ef6e.png" width="700" referrerpolicy="no-referrer"></span></span></p> 
<p>目前，<span style="background-color:#ffffff"><span style="color:#292929">使用 Flutter 构建的应用程序已超过 500,000 个。客户领域涵盖：</span></span>从微信等社交应用到 Betterment 和 Nubank 等金融和银行应用；从 SHEIN 和 trip.com 等商务应用到 Fastic 和 Tabcorp 等生活方式应用；从 My BMW 等配套应用程序到巴西政府等公共机构。</p> 
<p><span style="color:#292929">更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fflutter%2Fintroducing-flutter-3-5eb69151622f" target="_blank">查看官方公告</a>。</span></p>
                                        </div>
                                      
</div>
            