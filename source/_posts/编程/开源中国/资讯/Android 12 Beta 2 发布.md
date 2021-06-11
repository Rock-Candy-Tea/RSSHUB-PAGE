
---
title: 'Android 12 Beta 2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://devrel.andfun.cn/devrel/posts/2021/06/cmgC2B.gif'
author: 开源中国
comments: false
date: Fri, 11 Jun 2021 08:09:00 GMT
thumbnail: 'https://devrel.andfun.cn/devrel/posts/2021/06/cmgC2B.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p><em>作者 / Dave Burke, VP of Engineering</em></p> 
<p>几周前在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fevents.google.com%2Fio%2F" target="_blank">Google I/O</a> 上，我们发布了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fmp%2Fappmsgalbum%3F__biz%3DMzk0NDIwMTExNw%3D%3D%26action%3Dgetalbum%26album_id%3D1836606184309506051%23wechat_redirect" target="_blank">Android 12</a> 的第一个 Beta 版，带来了能展现您的个性、契合您的需求的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaterial.io%2Fblog%2Fannouncing-material-you" target="_blank">全新 UI</a>，提升了性能表现，并依旧将隐私和安全置于核心。Android 12 也给开发者们带来了更好的工具，用于打造令人愉悦的体验，无论用户使用的是手机、笔记本电脑、平板电脑、可穿戴设备还是汽车。</p> 
<p>今天我们带来了 Android 12 的第二个 Beta 版供大家体验。Beta 2 加入了新的隐私功能，如隐私仪表板 (Privacy Dashboard)，并继续朝着最终版本稳步前进。</p> 
<p>Android 12 中值得开发者们体验的内容还有很多: 全新设计的 UI、桌面小部件 (widget)、丰富的震动效果、改进的视频和图像质量，全新的隐私特性 (比如近似位置)，等等。请查看本文 "Google I/O 上的 Android 12" 一节了解值得关注的演讲和内容。</p> 
<p>今天您就可以在 Pixel 设备上通过 OTA 更新 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.google.com%2Fandroid%2Fbeta" target="_blank">开始体验</a> Android 12 Beta 2，如果您之前参加过 Beta 1 测试，会自动获得更新。您还可以在我们合作伙伴的若干指定设备上体验 Android 12 Beta，具体请查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fdevices" target="_blank">官网文档</a>。</p> 
<p>有关 Android 12 的详细信息以及如何开始开发，请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12" target="_blank">Android 12 开发者网站</a>。</p> 
<h2><strong>Beta 2 更新一览</strong></h2> 
<p>Beta 2 中包含我们在 Google I/O 中提及的一些隐私特性和许多功能更新，以改进功能、稳定性和性能表现。下面介绍其中一些亮点:</p> 
<p><strong>隐私仪表板 (Privacy Dashboard)</strong> - 为了让用户更好地了解应用正在访问的数据，我们加入了隐私仪表板功能。仪表板提供了一个简单而清晰的时间线视图，显示过去 24 小时内所有应用对麦克风、摄像头，以及位置的访问情况。用户还可以向应用查询为什么访问了敏感数据，只需开发者通过一个新的系统 intent <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fandroid%2Fcontent%2FIntent.html%23ACTION_VIEW_PERMISSION_USAGE_FOR_PERIOD" target="_blank">ACTION_VIEW_PERMISSION_USAGE_FOR_PERIOD</a> 使用一个 Activity 向用户提供此信息。我们建议应用尽可能利用这个 intent 主动帮助用户了解指定时间段内的数据访问情况。为了帮助您了解自己的代码以及第三方库使用隐私数据的情况，请使用 Data Auditing API。请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fabout%2Fversions%2F12%2Ffeatures%23show-rationale-privacy-dashboard" target="_blank">官方文档</a> 了解详细信息:</p> 
<p><img alt="△ 隐私仪表板: 过去 24 小时内的位置访问时间线" src="https://devrel.andfun.cn/devrel/posts/2021/06/cmgC2B.gif" referrerpolicy="no-referrer"></p> 
<p>△ 隐私仪表板: 过去 24 小时内的位置访问时间线</p> 
<p><strong>麦克风和摄像头指示器</strong> - 我们在状态栏加入了指示器，帮助用户知晓应用正在使用设备的摄像头和麦克风。用户可以前往快速设置 (Quick Settings) 查看正在使用摄像头和麦克风的应用，并在需要时轻松管理其使用权限。我们建议开发者查看自己应用对麦克风和摄像头的使用情况，移除用户不希望使用这些传感器的用例。请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fabout%2Fversions%2F12%2Fbehavior-changes-all%23mic-camera-indicators" target="_blank">官方文档</a> 了解详细信息。</p> 
<p><strong>麦克风和摄像头开关</strong> - 我们在快速设置 (Quick Settings) 里增加了全局开关，让用户可以快速禁用应用访问麦克风和摄像头 (仅限支持的设备)。当开关被关闭时，访问相应传感器的应用会收到空白的视频和音频流，系统也会提示用户打开传感器以使用应用的功能。开发者可以使用新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fandroid%2Fhardware%2FSensorPrivacyManager.html" target="_blank"><code>SensorPrivacyManager</code></a> API 来了解设备对这个开关功能的支持情况。麦克风和摄像头开关控制对所有的应用均生效，无论其目标平台版本如何。请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fabout%2Fversions%2F12%2Fbehavior-changes-all%23mic-camera-toggles" target="_blank">官方文档</a> 了解详细信息。</p> 
<p><strong>剪贴板读取通知</strong> - 为了让用户更清楚地知晓应用何时在读取剪贴板，Android 12 会在每次应用调用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fandroid%2Fcontent%2FClipboardManager%23getPrimaryClip%28%29" target="_blank">getPrimaryClip()</a> 时在屏幕底部显示一条 Toast 提示信息。如果剪贴板数据来自同一个应用，则不会出现提示信息。我们建议您减少应用对剪贴板的访问，并确保只在符合用户预期的情况下才读取剪贴板。请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fabout%2Fversions%2F12%2Fbehavior-changes-all%23clipboard-access-notifications" target="_blank">官方文档</a> 了解详细信息。</p> 
<p><strong>更直观的连接体验</strong> - 为了让用户更好地了解和管理他们的网络连接，我们在状态栏 (Status Bar)、快速设置 (Quick Settings) 以及设置 (Settings) 中提供了更简明、更直观的连接体验。全新的网络面板 (Internet Panel) 让用户可以轻松切换互联网提供商，以及更轻松地排除网络连接问题。请和我们分享您的使用反馈！</p> 
<p><img alt="△ 快速设置里新增的互联网连接控件" src="https://devrel.andfun.cn/devrel/posts/2021/06/sU7HV1.png" referrerpolicy="no-referrer"></p> 
<p>△ 快速设置里新增的互联网连接控件</p> 
<p>请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2F" target="_blank">Android 12 开发者网站</a> 详细了解 Android 12 的新特性。</p> 
<h2><strong>Google I/O 上的 Android 12</strong></h2> 
<p>在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fmp%2Fappmsgalbum%3F__biz%3DMzk0NDIwMTExNw%3D%3D%26action%3Dgetalbum%26album_id%3D1816170362913538051%23wechat_redirect" target="_blank">Google I/O</a> 上，我们为开发者们尽述了 Android 的更新内容，从 Android 12 到 Modern Android Development (现代 Android 开发) 工具，从新的设备型式，比如 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F375932966" target="_blank">Wear</a> 以及 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F375666877" target="_blank">可折叠设备</a>，到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F374392605" target="_blank">Google Play</a>。观看 Google I/O 上关于 <a href="ttps://devrel.andfun.cn/devrel/posts/2021/06/Ttogea.mp4">Android 12 最关键的 3 大要点</a> 视频了解更多详情。</p> 
<p><strong>#1 Android 的新 UI</strong> - Android 12 带来了 Android 有史以来最大的设计变更。我们重新思考了整套体验，包括颜色、形状、光照和动效，使得 Android 12 更具表现力、更鲜活、更个性化，并整体统一在同一种设计语言下，命名为 Material You。</p> 
<ul> 
 <li> <p>观看《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV13V41177zj%2F" target="_blank">Material Design 更新一览</a>》演讲了解更多信息。另外也请阅读《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaterial.io%2Fblog%2Fannouncing-material-you" target="_blank">介绍 Material You</a>》一文，了解设计师和开发者需要了解的设计指南概览。</p> </li> 
 <li> <p>如果您的应用提供 widget，请观看《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F06%2FhwxwhZ.mp4" target="_blank">重塑 widget</a>》演讲了解 Android 12 带来的新特性。您也可以通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Ffeatures%2Fwidgets" target="_blank">官方文档</a>，以及我们的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fandroid%2Fuser-interface-samples%2Ftree%2Fmain%2FAppWidget" target="_blank">AppWidget</a> 示例代码了解详情。</p> </li> 
</ul> 
<p><strong>#2 性能表现</strong> - 在 Android 12 中，我们对性能表现进行了重大且深入的资源投入: 从提升基础系统性能，延长电池使用时间，到前台服务变更和提升媒体质量以及性能，还提供了新的工具来优化应用。</p> 
<ul> 
 <li> <p>观看《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F06%2FntmoQs.mp4" target="_blank">打造高效 Android 后台任务</a>》演讲，了解 Android 12 中的前台服务，以及如何管理后台工作。也请阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fforeground-services" target="_blank">官方文档</a> 了解详情。</p> </li> 
 <li> <p>观看《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F06%2F49HCVL.mp4" target="_blank">Android Media 更新一览</a>》演讲，了解媒体性能和质量新特性，包括视频质量和转码，性能等级，ExoPlayer 更新，以及实时音频。</p> </li> 
 <li> <p>观看《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F06%2FtSMjHT.mp4" target="_blank">用 Macrobenchmark 测量卡顿和启动速度</a>》演讲，了解最新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fprofile%2Fmacrobenchmark-intro" target="_blank">Macrobenmark</a> 库，以及如何改善应用性能。</p> </li> 
</ul> 
<p><strong>#3 隐私和安全</strong> - 在 Android 12 中，我们继续为用户提供更多的透明度和控制权，同时保证设备和数据安全。</p> 
<ul> 
 <li> <p>观看《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F06%2FghPf3z.mp4" target="_blank">Android 隐私更新一览</a>》演讲，或阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F375445782" target="_blank">这篇文章</a> 了解最新的隐私特性，以及如何在应用中支持它们。也请通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fcodelabs%2Fapproximate-location%230" target="_blank">近似位置 codelab</a> 了解这个 Android 12 中新增的隐私权选项。</p> </li> 
 <li> <p>观看《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F06%2FcgQexz.mp4" target="_blank">Android 安全更新</a>》演讲，了解安全方面的更新情况，以及我们与安全社区工作的进展。</p> </li> 
</ul> 
<p>别忘了观看《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1PU4y1b7jv%2F" target="_blank">Android 更新一览</a>》了解 Android 12 的诸多更新，以及《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F06%2FLdGXcC.mp4" target="_blank">为 Android 12 做好准备的 12 个技巧</a>》，了解在进行兼容性测试时需要关注的领域。Google I/O 中的 Android 完整内容清单在这里: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fevents.google.com%2Fio%2Fprogram%2Fcontent%3F4%3Dtopic_android%264%3Dtopic_googleplay" target="_blank">https://events.google.com/io/program/content?4=topic_android&4=topic_googleplay</a></p> 
<h2><strong>应用兼容性</strong></h2> 
<p>我们已经开放 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fdevices" target="_blank">Pixel 和其他设备</a> 上的早期体验用户和开发者体验 Android 12 Beta，现在是时候让您的应用就绪了！</p> 
<p>要进行兼容性测试，请在运行 Android 12 Beta 的设备或模拟器上，通过 Google Play 或其他渠道安装您的正式版应用。请测试应用的所有流程，找出功能或 UI 上暴露的问题。请通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fbehavior-changes-all" target="_blank">行为变更清单</a> 来确定测试重点。现在无需升级应用的 <code>targetSdkVersion</code>，在解决所有发现的问题后，请尽快为您的 Android 12 Beta 用户发布应用的更新版本。</p> 
<p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/06/PUHop0.png" referrerpolicy="no-referrer"></p> 
<p>随着 Beta 2 的发布，Android 12 越来越接近 2021 年 8 月的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Foverview%23platform_stability" target="_blank">平台稳定性里程碑</a>。届时，面向应用的系统行为、SDK/NDK API 和非 SDK 列表都将最终确定。您将可以完成最后的兼容性测试，并发布完全兼容的应用、SDK 或开发库。发布时间表详见: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fpreview%2Foverview" target="_blank">https://developer.android.google.cn/preview/overview</a></p> 
<h2><strong>即刻开始体验 Android 12</strong></h2> 
<p>不论您是想体验 Android 12 的功能、测试应用还是 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Ffeedback" target="_blank">提交反馈</a>，都可以从这次的 Beta 版开始。只需使用受支持的 Pixel 设备 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.google.com%2Fandroid%2Fbeta" target="_blank">注册参加测试</a>，即可通过无线 (OTA) 方式获得更新。要开始进行开发，请先安装并 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fsetup-sdk" target="_blank">设置 Android 12 SDK</a>。</p> 
<p>您也可以在参与 Android 12 开发者预览计划的顶级设备制造商合作伙伴的设备上体验 Android 12 Beta 2。请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fdevices" target="_blank">developer.android.google.cn/about/versions/12/devices</a> 查看合作伙伴的完整列表。为了在更多设备上进行更广泛的测试，请通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fgsi-release-notes" target="_blank">Android GSI 映像</a> 来安装和体验 Android 12 Beta。如果您没有合适的设备，也可以在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fabout%2Fversions%2F12%2Fget%23on_emulator" target="_blank">Android 模拟器</a> 上进行测试。</p> 
<p>Beta 2 也适用于 Android TV，您可以查看最新的功能，测试自己的应用，并尝试全新的 Google TV 体验。请前往 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Ftv" target="_blank">Android TV 开发者网站</a> 了解更多信息并使用 ADT-3 开发者工具包上手开发。</p> 
<p>请访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2F12" target="_blank">Android 12 开发者网站</a> 了解 Beta 版的详细信息。</p> 
<p>您对产品的反馈及问题对我们非常重要，欢迎通过下方二维码向我们 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fservices.google.cn%2Ffb%2Fforms%2Fandroiddevswechat%2F" target="_blank">提交反馈</a>。您的问题有可能出现在下一期的 FAQ 中并获得解答。感谢您的支持！</p> 
<p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/06/IYtelg.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            