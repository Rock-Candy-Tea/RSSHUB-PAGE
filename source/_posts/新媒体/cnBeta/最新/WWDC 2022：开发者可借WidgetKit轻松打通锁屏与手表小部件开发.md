
---
title: 'WWDC 2022：开发者可借WidgetKit轻松打通锁屏与手表小部件开发'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0607/19103fbf31246d4.jpg'
author: cnBeta
comments: false
date: Tue, 07 Jun 2022 05:13:53 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0607/19103fbf31246d4.jpg'
---

<div>   
在北京时间今日凌晨 1 点的 WWDC 2022 主题演讲后，苹果在开发者简报会上介绍了 iOS 16 和 watchOS 9 的诸多新功能和体验改进。<strong>其中最让我们关注的，莫过于开发者们可借助 WidgetKit 小部件开发工具，在手机锁屏界面和 Apple Watch 表盘上复用相关代码。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0607/19103fbf31246d4.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>这家库比蒂诺科技巨头，详细介绍了开发者现可为 iOS 16 锁屏构建不同类型的小部件。</p><p>而受 Apple Watch 复杂性的启发，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>还宣称这些新的小部件可帮助开发者利用其应用程序中的关键信息，并将其显示在用户能够一目了然的地方。</p><p><strong>更棒的是，所有这些锁屏小部件，现也能够同时在 iOS 和 watchOS 平台上运行</strong> —— 因为从 watchOS 9 开始，复杂功能也将基于 WidgetKit 来提供支持。</p><blockquote><p>这意味着开发者们能够在两套平台上使用相同的代码，而苹果官方开发工具会在期间自动搞定相关差异。</p><p>默认情况下，小部件将使用适当的系统字体来创建。此外为了增强可读性，锁屏小部件将带有着色。</p></blockquote><p><strong>发布初期，苹果向开发者提供了三套预设方案，</strong>分别是圆形（circular）、矩形（rectangular）、以及内联式（inline）。</p><blockquote><p>● 首先，圆形小部件非常适合显示小图像、页面或仅有几个字符的文本，比如方便用户了解当日的活跃度、是否该去跑步健身（刷满各个项目的圆圈）。</p><p>● 其次，矩形小部件设计能够提供更大的画布显示区域，苹果解释称这更适用于显示天气预报等内容。</p><p>● 另外，内联小部件提供了一种通过少量文本的 SF 符号来传达信息的方式 —— 当前官方图标库中已包含 4000+ 不同的符号。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0607/8dfcbd512d6b934.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">WidgetKit 更新将今秋随 iOS 16 一起正式到来</p><p>这些内联小部件将显示在锁屏时钟 / 系统日期字符串的旁边，比如“某月 6 号 / 周一”。</p><blockquote><p>在 WWDC 2022 会议安排的示例中，苹果展示了这个小部件将如何在时钟界面的基础上显示天气信息。</p><p>比如在此例中，日期后面紧跟的太阳符号就代表了天气、且后方紧跟着显示着用户所在的城市信息。</p></blockquote><p>事实上，WidgetKit 小部件开发工具包覆盖了苹果旗下的 iOS、<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fipad%2F" target="_blank">iPad</a>OS 和 macOS 等平台。</p><blockquote><p>随着今年晚些时候的正式到来，开发者们还有望带来更多丰富、新颖的小部件，以及面向 watchOS 平台的复杂功能体验。</p><p>如果你喜欢 Brass、Widgetsmith 之类的个性化体验，届时大可为主屏、锁屏和手表统一设置匹配的小部件，并以相同的方式在所有设备上进行自定义。</p></blockquote><p>另一项新功能则允许小部件显示实时信息，开发者将能够创建使用 Swift UI 构建的实时活动（Live Activities），以便在锁屏界面上提供最新信息。</p><p>与小部件一样，这些实时活动组件也基于 WidgetKit 构建。而它与标准小部件之间的最大区别，就是开发者能够实时更新 Live Activities 的呈现状态。</p>   
</div>
            