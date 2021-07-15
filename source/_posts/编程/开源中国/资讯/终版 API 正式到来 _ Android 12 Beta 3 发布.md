
---
title: '终版 API 正式到来 _ Android 12 Beta 3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://devrel.andfun.cn/devrel/posts/2021/07/N8Kn3C.png'
author: 开源中国
comments: false
date: Thu, 15 Jul 2021 14:21:00 GMT
thumbnail: 'https://devrel.andfun.cn/devrel/posts/2021/07/N8Kn3C.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>每个月，我们都在努力让 Android 12 更接近其最终形态，包括创新功能、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaterial.io%2Fblog%2Fannouncing-material-you" target="_blank">更适合用户的新版 UI</a>、性能提升、隐私增强、安全改进等等。许多人已经通过我们的 Beta 计划在 Android 12 上进行开发和测试，再次感谢大家一直以来分享的反馈！</p> 
<p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/07/N8Kn3C.png" referrerpolicy="no-referrer"></p> 
<p>不过现在离这个版本的正式发布还有很多事情要做。今天我们带来 Android 12 的第三个 Beta 版供大家体验。除了滚屏截图、隐私指示器 API 和增强的自动旋转等更新之外，Beta 3 还包含了最终版本的 Android 12 API 和官方 SDK。有了这些，您就可以在平台稳定性里程碑 (会在 Beta 4 时达成) 到来之前测试应用并进行更新。现在就让您的应用做好准备吧！</p> 
<p>今天您就可以在 Pixel 设备上通过 OTA 更新 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.google.com%2Fandroid%2Fbeta" target="_blank">开始体验 Android 12 Beta 3</a>，如果您之前参加过 Beta 测试，会自动获得更新。您还可以在我们的设备制造商合作伙伴 (如夏普和 TCL) 的若干 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fdevices" target="_blank">指定设备</a> 上体验 Android 12 Beta 3。</p> 
<p>有关 Android 12 的详细信息以及如何开始开发，请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12" target="_blank">Android 12 开发者网站</a>。</p> 
<h3><strong>Beta 3 更新一览</strong></h3> 
<p>Beta 3 包含许多改善功能、用户体验和性能的更新。下面介绍其中几个亮点。</p> 
<p><strong>滚屏截图</strong> - 为了让大家更容易保存和分享滚屏内容，我们增加了滚屏截图功能。从 Beta 3 开始，当用户对可滚动的内容进行截图时，会看到一个 "截取更多" 的按钮，点击即可将截图范围扩展到全部内容，还可以调整裁切范围。</p> 
<p><img alt="△ 在设置 (Settings) 中进行滚屏截图" src="https://devrel.andfun.cn/devrel/posts/2021/07/WWFmkt.png" referrerpolicy="no-referrer"></p> 
<p>△ 在设置 (Settings) 中进行滚屏截图</p> 
<p>滚屏截图对大多数应用来说都是开箱即用的: 如果您的应用使用标准的基于视图 (View-based) 的界面，则无需任何更改。对于不基于视图的或高度定制的应用界面以及 UI 工具包，我们将提供一个新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fandroid%2Fview%2FScrollCaptureCallback" target="_blank">ScrollCapture API</a> 来支持滚屏截图。系统会通过这个 API 告知应用滚屏截图的请求，并提供一个 Surface，以供您在其中绘制 UI。我们将继续对滚屏截图进行迭代，在 Beta 4 中，您将看到更多默认支持此功能的场景，包括对 ListView 的支持。我们也在努力为更多的内容 (如网页内容) 提供支持。请务必和我们分享您的使用感想！</p> 
<p><strong>设备端搜索</strong> - 我们在 Beta 3 进一步强化了对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fandroid%2Fapp%2Fappsearch%2Fpackage-summary" target="_blank">AppSearch</a> 的平台支持，AppSearch 是一个全新的高性能设备端搜索引擎。通过 AppSearch，应用可以对结构化数据进行索引，并通过内置的全文搜索功能进行搜索，还可以使用高效索引和检索、多语言支持和相关性排序等原生功能。</p> 
<p>AppSearch 有两种使用方式: 一种是通过新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fjetpack%2Fandroidx%2Freleases%2Fappsearch" target="_blank">AppSearch Jetpack 库</a> 提供本地索引供您的应用使用，且向前兼容；另一种则是针对整个系统进行维护的中央索引，支持 Android 12 及以后的版本。当您采用中央索引方式时，系统 UI 可以显示您的应用的数据，除非您选择不使用此功能。此外，您可以与其他应用安全地共享数据，允许他们同时搜索自己的和您的应用的数据。请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fguide%2Ftopics%2Fsearch%2Fappsearch" target="_blank">官方文档</a> 了解详细信息。</p> 
<p><strong>WindowInsets 中的隐私指示器 API</strong> - 在 Beta 2 中，我们在状态栏里增加了隐私指示器，显示应用何时使用设备的摄像头或麦克风。由于指示器会在应用处于沉浸式模式时显示，并有可能覆盖控件或内容，因此应用需要知道指示器可以在哪里绘制，并做出必要的调整，以避免有用的内容被指示器覆盖。在 Beta 3 中，我们为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fandroid%2Fview%2FWindowInsets" target="_blank">WindowInsets</a> 添加了新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fandroid%2Fview%2FWindowInsets%23getPrivacyIndicatorBounds%28%29" target="_blank">隐私指示器 (privacy indicator) API</a>，让您知晓指示器的最大呈现范围以及它们在屏幕上的相对位置，且兼顾当前的屏幕方向和语言设置。请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fbehavior-changes-all%3Fhl%3Den%23mic-camera-indicators" target="_blank">官方文档 (英文)</a> 了解详细信息:</p> 
<p><strong>企业可配置的摄像头和麦克风开关</strong> - 在 Beta 2 中，我们引入了新的开关，让用户能够立即关闭所有应用对设备麦克风和摄像头的访问。我们现在让企业管理员可以访问该功能，他们可以在其全权管理的设备上限制对这些传感器的使用。请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fandroid%2Fos%2FUserManager.html%23DISALLOW_CAMERA_TOGGLE" target="_blank">官方文档</a> 了解详细信息。</p> 
<p><strong>为与 CDM 配对的应用启动前台服务提供新的权限</strong> - 为了更好地支持设备配套应用执行核心功能，同时向系统提供透明度，与 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fguide%2Ftopics%2Fconnectivity%2Fcompanion-device-pairing" target="_blank">配套设备管理器 (Companion Device Manager, CDM)</a> 配对的应用可以通过声明一个新的普通权限，从后台启动前台服务。请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fguide%2Ftopics%2Fconnectivity%2Fcompanion-device-pairing" target="_blank">官方文档</a> 了解详细信息。</p> 
<p><strong>更好用、更快速的自动旋转</strong> - 我们增强了 Android 的自动旋转功能，通过使用前置摄像头来更准确地识别何时旋转屏幕。让您躺在沙发上或床上使用设备时获得更好的体验。对于开发者来说，这意味着自动旋转将为用户提供更好的体验，只需用户在系统设置中打开此功能即可。增强的自动旋转功能由我们最近公布的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.google%2Ftechnology%2Fsafety-security%2Four-work-keep-you-safe%2F" target="_blank">Private Compute Core</a> 提供支持，因此图像永远不会被存储到设备中，也不会被发送出设备。在 Beta 3 中，这项功能适用于 Pixel 4 及更新的 Pixel 设备。</p> 
<p>为了使屏幕旋转的速度在所有设备上尽可能地快，我们还优化了动画和重绘，并增加了一个机器学习驱动的手势检测算法。通过这些优化，基础自动旋转功能的延迟已经减少了 25%，而加入人脸检测功能的旋转则建立在这些改进之上。欢迎大家亲身体验改进过的自动旋转功能，并和我们分享使用体验。</p> 
<p><strong>Android 12 的游戏支持</strong> - 通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fgames%2Fgamemode" target="_blank">游戏模式 (Game Mode) API</a>，您可以在玩家为游戏选择不同的性能配置时做出反应: 比如在漫长的通勤过程中节省电池消耗，或者通过性能模式获得最高的帧率。这些 API 将与即将推出的游戏仪表板整合，该仪表板提供了一层额外的控件，让玩家可以在游戏过程中快速进行关键实用功能的设置。游戏仪表板将于今年晚些时候在指定的若干设备上推出。</p> 
<p><img alt="△ Touchgrind BMX 在 Android 12 上的 "边玩边下" 体验" src="https://devrel.andfun.cn/devrel/posts/2021/07/RbC4rV.gif" referrerpolicy="no-referrer"></p> 
<p>△ Touchgrind BMX 在 Android 12 上的 "边玩边下" 体验</p> 
<p>另外，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fgames%2Fdistribute%2Fplay-as-you-download" target="_blank">边玩边下 (play as you download)</a> 功能将允许游戏在安装过程中从后台下载游戏资源，从而让玩家更快地进入游戏:</p> 
<p>请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12" target="_blank">Android 12 开发者网站</a> 详细了解 Android 12 的新特性</p> 
<h2><strong>终版 API 和 SDK</strong></h2> 
<p>我们在过去数个月内一直致力于完成 Android 12 的 API。今天随着 Beta 3 的发布，这套 API 也正式来到大家面前，同时发布的还有正式版的 API 等级 31 的 SDK。我们计划在 Beta 4 时全面抵达平台稳定性里程碑，届时不仅是 API 接口，所有面向应用的系统行为、非 SDK 接口列表都将最终确定。</p> 
<p>如果您是针对 Android 12 API 编译应用，我们建议使用今天发布的版本更新您的开发环境，并使用正式版 SDK 和最新的工具重新编译您的应用。</p> 
<h2><strong>应用兼容性</strong></h2> 
<p>许多早期体验用户和开发者已经在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fdevices" target="_blank">Pixel 和其他设备</a> 上开始体验 Android 12 Beta，现在是时候确保您的应用兼容，以让他们尽情使用了！</p> 
<p>要在 Beta 3 上进行应用兼容性测试，请在运行 Android 12 Beta 的设备或模拟器上，通过 Google Play 或其他渠道安装您的正式版应用。请测试应用的所有流程，找出功能或 UI 上暴露的问题。请通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fbehavior-changes-all" target="_blank">行为变更清单</a> 来找出可能影响应用的潜在变更，从而确定测试重点。现在您无需升级应用的 targetSdkVersion，在解决所有发现的问题后，请尽快为您的 Android 12 Beta 用户发布应用的更新版本。</p> 
<p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/07/t8pOp5.png" referrerpolicy="no-referrer"></p> 
<p>正如之前提到的，随着下一个版本，即 Beta 4 的发布，Android 12 将抵达 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Foverview%23platform_stability" target="_blank">平台稳定性里程碑</a>。届时，面向应用的系统行为、SDK/NDK API 和非 SDK 列表都将最终确定。您将可以进行最后的兼容性测试，并发布完全兼容的应用、SDK 或开发库。发布时间表详见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fpreview%2Foverview" target="_blank">这里</a>。</p> 
<h2><strong>即刻开始体验 Android 12</strong></h2> 
<p>不论您是想体验 Android 12 的功能、测试应用还是 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Ffeedback" target="_blank">提交反馈</a>，都可以从这次的 Beta 版开始。只需使用受支持的 Pixel 设备注册 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.google.com%2Fandroid%2Fbeta" target="_blank">参加测试</a>，即可通过无线 (OTA) 方式获得更新。要开始进行开发，请先安装并 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fsetup-sdk" target="_blank">设置 Android 12 SDK</a>。</p> 
<p>您也可以在参与 Android 12 开发者预览计划的顶级设备制造商合作伙伴 (如夏普和 TCL) 的设备上体验 Android 12 Beta 3。请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fdevices" target="_blank">developer.android.google.cn/about/versions/12/devices</a> 查看合作伙伴的完整列表。为了在更多设备上进行更广泛的测试，请通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fgsi-release-notes%3Fhl%3Den" target="_blank">Android GSI 映像 (英语)</a> 来安装和体验 Android 12 Beta。如果您没有合适的设备，也可以在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fget%23on_emulator" target="_blank">Android 模拟器</a> 上进行测试。</p> 
<p>Beta 3 也适用于 Android TV，您可以查看最新的功能，测试自己的应用，并尝试全新的 Google TV 体验。请前往 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Ftv" target="_blank">Android TV 开发者网站</a> 了解更多信息并使用 ADT-3 开发者工具包上手开发。</p> 
<p>请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2F12" target="_blank">Android 12 开发者网站</a> 了解 Beta 版的详细信息。</p>
                                        </div>
                                      
</div>
            