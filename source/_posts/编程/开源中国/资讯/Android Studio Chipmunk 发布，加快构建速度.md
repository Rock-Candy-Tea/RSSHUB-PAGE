
---
title: 'Android Studio Chipmunk 发布，加快构建速度'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b652fe2e8c3e31bd6308752c1c30105e81c.png'
author: 开源中国
comments: false
date: Tue, 10 May 2022 23:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b652fe2e8c3e31bd6308752c1c30105e81c.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Android Studio 是 Android 开发的官方 IDE，包括构建 Android 应用程序所需的一切。近日 Android 团队正式发布了 Android Studio Chipmunk 的稳定版本。这个版本是一个较小的功能版本，但包含了最新的 IntelliJ 更新，并在质量和稳定性方面做出了改善，仅在这个版本中就解决了超过 175 个质量问题。</p> 
<p><img alt height="438" src="https://oscimg.oschina.net/oscnet/up-b652fe2e8c3e31bd6308752c1c30105e81c.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>Compose Animation 预览</h3> 
<p>这个之前的实验性功能现在可以让 Jetpack Compose 的开发者检查和调试他们用 Compose 构建的动画。如果一个动画在可合成的预览中被描述，你可以检查每个动画值在特定时间的准确值，暂停动画、循环、快进或放慢。这对于逐帧比较动画与它们的设计规格特别有用。</p> 
<p>Compose Animation Preview 目前支持AnimatedVisibility 和 updateTransition。它将在未来支持更多的动画类型。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-4c1251ab75c195429687a9a7696f3981bee.gif" width="700" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h3>CPU Profiler</h3> 
<p>Android Studio Chipmunk 现在显示更新的 jank 信息，包括 jank 类型以及预期和实际期限，帮助你发现 jank 的实际原因。当你使用 Android Emulator 或 API 级别为 31 或更高的设备时（Android 12 或以上），该 jank 信息可用。</p> 
<p><img alt height="102" src="https://oscimg.oschina.net/oscnet/up-c5b88e3104b1b741e10094dfafecbc528f4.png" width="700" referrerpolicy="no-referrer"></p> 
<p>在 CPU 分析器中显示 Jank 信息</p> 
<p><img alt height="129" src="https://oscimg.oschina.net/oscnet/up-20bfa963412847ec661a224fea1364446c2.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>Build Analyzer：检查 Jetifier</h3> 
<p>在 Chipmunk 中为 Build Analyzer 中引入了一个新的 Jetifier 检查，它将通知你是否可以删除 Jetifier 标志以提高构建过程中的性能。</p> 
<p>Jetifier 标志是为了自动迁移第三方库以使用 AndroidX 而设计的，绝大多数 Android Studio 项目仍然启用了它。然而库的生态已经大部分转移到了对 AndroidX 的原生支持，现在有这个标志通常会增加不必要的构建开销，关闭它通常会节省 5-10% 的构建时间。</p> 
<p><img alt height="225" src="https://oscimg.oschina.net/oscnet/up-c77dc41cc623f6acb39259be3f04a5557ca.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>IntelliJ 平台更新</h3> 
<p>虽然 Android Studio Chipmunk 的 Android 特定功能数量不多，但它包括了 IntelliJ 2021.2 平台的主要版本，其中有许多新功能。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroid-developers.googleblog.com%2F2022%2F05%2Fandroid-studio-chipmunk.html" target="_blank">https://android-developers.googleblog.com/2022/05/android-studio-chipmunk.html</a></p>
                                        </div>
                                      
</div>
            