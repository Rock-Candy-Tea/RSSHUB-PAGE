
---
title: 'Android 12 最后一个开发者预览版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0319/070233_7Hbi_2744687.png'
author: 开源中国
comments: false
date: Fri, 23 Apr 2021 23:49:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0319/070233_7Hbi_2744687.png'
---

<div>   
<div class="content">
                                                                                            <p>谷歌已经发布了 Android 12 的第三个<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroid-developers.googleblog.com%2F2021%2F04%2Fandroid-12-developer-preview-3.html" target="_blank">开发者预览版</a>，这也是最后一个以开发者为中心的构建版本。第一个 Android 12 测试版将在 5 月到来，第二个和第三个测试版构建则将在 6 月至 7 月之间向开发者开放。接着 8 月份，Android 12 的第一个稳定版将会发布。</p> 
<p><img alt height="180" src="https://static.oschina.net/uploads/space/2021/0319/070233_7Hbi_2744687.png" width="789" referrerpolicy="no-referrer"></p> 
<p>此版本一些亮点内容如下：</p> 
<ul> 
 <li><strong>改进的应用启动体验：</strong>添加了新的 SplashScreen API，为所有的应用程序提供了新的应用程序启动动画。包括启动时进入应用的动作，显示你的应用图标的闪屏，以及过渡到你的应用本身。新的体验为每个应用的启动带来了标准的设计元素，但它也是可定制的，开发者可以通过 XML 文件来进行自定义。</li> 
</ul> 
<p><img alt height="316" src="https://oscimg.oschina.net/oscnet/up-de3f87ccaa9bbafca521aa3025b115a4e26.png" width="300" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>新的呼叫通知模板：</strong>改进了呼叫通知，使其具有更多的可见性和可扫描性，并改善其与其他通知组件的一致性。用户可以使用该模板为来电、呼出和筛选的电话创建通知。每种类型都支持多种动作，包括默认动作和针对用户应用程序的自定义动作。用户还可以附加一个大的头像图片，提供文本，并设置按钮颜色提示。</li> 
 <li> <p><strong>Exact alarm permission：</strong>为了鼓励应用程序节约系统资源，以 Android 12 为目标的应用程序必须拥有 SCHEDULE_EXACT_ALARM 权限，以便设置exact alarms。如果你的应用程序试图使用设置 exact alarms 的 API，但没有被授予该权限，就会发生一个 SecurityException。</p> </li> 
 <li> <p><strong>改进的 Web 链接：</strong>Android 12 中进行一些改变，以帮助用户更快、更无缝地获得他们的内容。首先，改变了对未通过安卓应用链接验证或未由用户手动批准的链接的默认处理。现在，操作系统将直接在默认浏览器中打开它们，而不是显示一个选择器对话框。为了让用户更容易批准你的应用程序的链接，新版本已经添加了一个新的 Intent，将他们带到设置中的"Open by default"。如果你想确保只有你的应用程序可以处理来自你的域名的链接，你可以使用 App Links。好增加了新的 adb 命令来帮助你配置和测试你的链接。</p> </li> 
 <li> <p> </p> <p><strong>丰富的触觉体验</strong></p> </li> 
 <li> <p> </p> <p><strong>视频编码的改进</strong></p> </li> 
 <li> <p> </p> <p><strong>Camera2 vendor 扩展</strong></p> </li> 
 <li> <p> </p> <p><strong>Quad bayer 相机传感器支持</strong></p> </li> 
 <li> <p> </p> <p><strong>更快的机器学习：</strong>通过引入填充、栅格同步、执行对象重复利用等等机制进一步提高了 Neural Networks API 的执行效率。还通过 Google Play 服务，使 ML 加速器驱动程序可以在平台发布之外更新。这将使开发者更容易在任何兼容设备上利用最新的驱动程序，并确保 ML 性能改进和错误修复比以前更快地到达用户手中。</p> </li> 
 <li> <p> </p> <p><strong>标准化 GPU 计算：</strong>弃用 RenderScript APIs，以支持跨平台的 GPU 计算解决方案，如 Vulkan 和 OpenGL。</p> </li> 
 <li> <p> </p> <p><strong>更好地调试 native crashes</strong></p> </li> 
 <li> <p> </p> <p><strong>更加灵活的备份配置</strong></p> </li> 
</ul> 
<p>更多详细内容可查看官方博客：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroid-developers.googleblog.com%2F2021%2F04%2Fandroid-12-developer-preview-3.html" target="_blank">https://android-developers.googleblog.com/2021/04/android-12-developer-preview-3.html</a>  </p>
                                        </div>
                                      
</div>
            