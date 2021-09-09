
---
title: 'Flutter 2.5 发布，大版本更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5074a1975c21c32abbf21b0d62bf10c56d2.png'
author: 开源中国
comments: false
date: Thu, 09 Sep 2021 08:33:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5074a1975c21c32abbf21b0d62bf10c56d2.png'
---

<div>   
<div class="content">
                                                                                            <p>Flutter 2.5 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fflutter%2Fwhats-new-in-flutter-2-5-6f080c3f3dc" target="_blank">发布</a>。这是一个大版本更新，开发团队称此版本在 Flutter 版本历史上排名第二：关闭了 4600 个问题，从 252 个贡献者和 216 个审阅者合并了 3932 个 PR。 回顾过去一年，共有 1337 位贡献者创建了 21072 个 PR，其中有 15172 个被合并。</p> 
<p>此版本延续了一些重要的性能和工具改进，以追踪你自己应用中的性能问题。同时还有一些新功能，包括对 Android 的全屏支持、更多 Material You（也称为 v3）支持、更新的文本编辑以支持可切换的键盘快捷键、在 Widget Inspector 中更详细地查看你的小部件、在 Visual Studio Code 项目中添加依赖关系的新支持、从 IntelliJ/Android Studio 的测试运行中获取覆盖信息的新支持；以及一个全新的应用程序模板，为你的 real-world Flutter 应用程序提供更好的基础。</p> 
<p><strong>Performance：iOS 着色器预热、异步任务、GC & message passing</strong></p> 
<p>此版本带来了多项性能改进。此列表中的第一个 PR 用于从离线训练运行 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fengine%2Fpull%2F25644" target="_blank">#25644</a> ) 中连接 Metal 着色器预编译，它（如基准测试所示）将最坏情况的帧光栅化时间减少了 2/3 秒，将第 99 个百分位帧减少了一半。还在本版本中对 UI isolate 的事件循环的调度策略（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fengine%2Fpull%2F25789" target="_blank">#25789</a>）进行了改进，现在帧处理优先于其他异步事件的处理，从而在测试中消除了此源的卡顿。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5074a1975c21c32abbf21b0d62bf10c56d2.png" referrerpolicy="no-referrer"></p> 
<p>另一个导致卡顿的原因是 GC 暂停 UI 线程以回收内存。在这个版本中，未使用的图像的内存被快速回收（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fengine%2Fpull%2F26219" target="_blank">#26219</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fpull%2F82883" target="_blank">#82883</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fpull%2F84740" target="_blank">#84740</a>），大大减少了 GC。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-2f7bd28d1895814a9ff51a4e28eb5131375.png" referrerpolicy="no-referrer"></p> 
<p>测试结果表明，播放 20 秒动画 GIF 从需要 400 多次 GC 变为只需要 4 次。更少的主要 GC 意味着涉及图像出现和消失的动画将减少卡顿，并消耗更少的 CPU 和功率。</p> 
<p>Flutter 2.5 的另一个性能改进是在 Dart 和 Objective-C/Swift (iOS) 或 Dart 和 Java/Kotlin (Android) 之间发送消息时的延迟。通常作为 tuning-up message channels 的一部分，从消息编解码器中删除不必要的副本可将延迟减少多达 50%，具体取决于消息大小和设备（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fengine%2Fpull%2F25988" target="_blank">#25988</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fengine%2Fpull%2F26331" target="_blank">#26331</a>）。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-94d0e9abf226e613a9148434930eb0d2adc.png" referrerpolicy="no-referrer"></p> 
<p>对于 iOS 用户而言的一项性能更新为：在此版本中，在 Apple Silicon M1 Mac 上构建的 Flutter 应用程序可以在 ARM iOS 模拟器 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fpull%2F85642" target="_blank">#pull/85642</a> ) 上原生运行。这意味着 Intel x86_64 指令和 ARM 之间没有 Rosetta 转换，从而提高你的 iOS 应用程序测试期间的性能，并允许你避免一些微妙的 Rosetta 问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fissues%2F74970%23issuecomment-858170914" target="_blank">#74970</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fissues%2F79641" target="_blank">#79641</a>）。这是全面支持 Flutter for Apple Silicon 的又一步。</p> 
<p><strong>Dart 2.14：格式、语言特性、pub &  linting 开箱即用 </strong></p> 
<p>此版本的 Flutter 随 Dart 2.14 一起发布。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2F%40mit.mit%2Fannouncing-dart-2-14-b48b9bb2fb67" target="_blank">新版本的 Dart</a> 带有新的格式，使<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdart.dev%2Fguides%2Flanguage%2Flanguage-tour%23cascade-notation" target="_blank">级联</a>更加清晰；新的 pub 支持 ignoring files，以及新的语言功能，包括三重移位运算符的回归。此外，该版本还创建了一组新的在 Dart 和 Flutter 项目之间共享的标准 lints，开箱即用。 </p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-c0ce19dddf07ba191ef6a3fc0a80fb11a5f.png" referrerpolicy="no-referrer"></p> 
<p>此外，Flutter 2.5 版本包括许多涉及全屏模式及其功能的修复。例如，应用程序现在可以监听其他模式下 fullscreen changes 的使用情况；以便当系统 UI 返回时，开发人员现在可以编写代码以适当地返回全屏模式或执行其他操作。</p> 
<p>还继续构建了 Material You 规范支持。包括对 Floating Action Button  大小和主题的更新，以及新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflutter%2Fflutter%2Fpull%2F79999" target="_blank">MaterialState.scrolledUnder</a> 状态。</p> 
<p>Flutter DevTools 也通过利用引擎更新获得了一些关注。其中一组更新使 Flutter 能够将跟踪事件与特定 frames 相关联，帮助开发人员确定 frame 可能超出预算的原因。因此，开发人员可以更轻松地诊断应用程序中的低质量着色器编译。</p> 
<p>此版本的 DevTools 还附带了对 Widget Inspector 的更新，允许开发人员评估对象、查看属性、 Widget 状态等。当一个 Widget 被选中时，它会自动填充一个新的 Widget Inspector Console，可以在其中探索 Widget 属性。</p> 
<p>更多详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fflutter%2Fwhats-new-in-flutter-2-5-6f080c3f3dc" target="_blank">官方公告</a>。</p>
                                        </div>
                                      
</div>
            