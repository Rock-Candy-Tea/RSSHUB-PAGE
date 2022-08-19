
---
title: 'Android Studio 2021.3.1 RC1 发布，代号_海豚_(Dolphin)'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0818/105356_YOUC_2720166.gif'
author: 开源中国
comments: false
date: Fri, 19 Aug 2022 07:16:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0818/105356_YOUC_2720166.gif'
---

<div>   
<div class="content">
                                                                                            <p>Android Studio Dolphin（版本号为 2021.3.1）首个 RC <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroidstudio.googleblog.com%2F2022%2F08%2Fandroid-studio-dolphin-rc1-now-available.html" target="_blank">已发布</a>。</p> 
<p><strong><span style="background-color:#ffffff; color:#333333">已达到稳定版状态的新特性</span></strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>Jetpack Compose</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Compose 动画组合</li> 
 <li>Compose 多重预览注解</li> 
 <li>布局检查器中的 Compose 重新组合计数</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>Wear OS</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Wear OS 模拟器配对助手</li> 
 <li>Wear OS 模拟器侧边工具栏</li> 
 <li>直接启动 Wear OS 界面</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>开发工具</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Logcat V2</li> 
 <li>由 Gradle 管理的设备</li> 
</ul> 
<hr> 
<p><strong>主要变化</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>Jetpack Compose</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><strong>Compose Animation Coordination</strong><span> </span>(Compose 动画组合) - 您可以在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fjetpack%2Fcompose%2Ftooling%23animations" target="_blank">Animation Preview<span> </span></a>(动画预览) 中查看您的全部动画并且自由搭配。您也可以锁定某个特定的动画。</p> <p style="margin-left:0; margin-right:0"><img src="https://static.oschina.net/uploads/space/2022/0818/105356_YOUC_2720166.gif" referrerpolicy="no-referrer"></p> <p>△ Compose Animation 组合</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>Compose Multipreview Annotations</strong><span> </span>(Compose 多重预览注解) - 定义注解类，在其中包含多个预览的定义，并且使用该注解一次性生成这些预览。该注解可以同时预览多个设备、字体及主题，而无需重复定义每个单独的可组合项。</p> <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-84f9eb3ab7fbe2f622090a675c51d9db1fe.png" referrerpolicy="no-referrer"></p> <p>△ 多重预览注解</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>布局检查器中的 Compose 重新组合计数</strong><span> </span>- 在布局检查器中查看 Compose 应用的重新组合计数。重新组合计数和跳过计数可配置显示在组件树和属性窗格中。如需了解更多信息，请参阅<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fpreview%2Ffeatures%23li-compose-counter" target="_blank">Android 开发者文档</a>。</p> <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-d287d5bca44b338f1b67f8a6908408da5b8.png" referrerpolicy="no-referrer"></p> <p>△ Compose 重新组合计数</p> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>Wear OS</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><strong>Wear OS Emulator Pairing Assistant (Wear OS 模拟器配对助手)</strong><span> </span>- 使用 Wear OS 模拟器配对助手，您可以在设备管理器中看到 Wear 设备，并且使用单台手机配对多个手表模拟器。您也无需再像以前一样经常重新配对设备，因为 Android Studio 在关闭时会存储配对记录。</p> <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-0abb0a32b1007197d08b65b97d37881612b.png" referrerpolicy="no-referrer"></p> <p>△ Wear OS 模拟器配对助手</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>Wear OS Emulator Side Toolbar (Wear OS 模拟器侧边工具栏)</strong><span> </span>- 使用 Wear 特制的模拟器按钮，其中整合了模拟的物理按键，包括主按钮、手掌按钮、倾斜按钮。</p> <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-266bd9005183526c3417ac4f3b7d06fec7f.png" referrerpolicy="no-referrer"></p> <p>△ Wear OS 模拟器侧边工具栏</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>Wear OS Direct Surface Launch (直接启动 Wear OS 界面)</strong><span> </span>- 为 Wear OS 卡片、表盘以及表盘复杂功能创建 Run/Debug 配置，并且从 Android Studio 直接启动。</p> <p style="margin-left:0; margin-right:0"><img src="https://static.oschina.net/uploads/space/2022/0818/105628_stNb_2720166.gif" referrerpolicy="no-referrer"></p> <p>△ 新的 Wear OS Run/Debug 配置类型</p> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>开发工具</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><strong>Logcat V2</strong><span> </span>- 从底层重构的全新 Logcat 可以更便捷地解析、查询和追踪日志。Logcat V2 包括新的格式，使其可以更轻松地检索所需的信息，新的分离视图可以帮助您同时追踪多个记录，并且包含全新且功能强大的日志筛选语法。如需了解更多信息，请参阅<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fpreview%2Ffeatures%23logcat" target="_blank">Android 开发者文档</a>。</p> <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-ea757d012613acb96c64651b1ee8dd5c7c0.png" referrerpolicy="no-referrer"></p> <p>△ Logcat V2</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>由 Gradle 管理的设备</strong><span> </span>- 为自动化测试描述您所需的虚拟设备，并将其作为构建的一部分，同时让 Gradle 来完成剩余的工作。从 SDK 的下载到设备授权以及设置，再到测试执行以及卸载，Gradle 在插桩测试中会管理您虚拟设备的整个生命周期。Gradle 也会采取一些智能功能，比如快照管理，缓存测试，以及碎片测试来保障您的测试能够高效、快速、连续地运行。Gradle 所管理的设备还引入了一个全新类型的设备，叫做<span> </span><strong>自动化测试设备</strong>，它会针对自动化测试优化设备，从而在测试执行过程中有效降低 CPU 和内存的占用。如需了解更多信息，请参阅<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fpreview%2Ffeatures%23gmd" target="_blank">Android 开发者文档</a>。</p> <p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-c345ce056152afaed6d0e8b5dbbbc0a57ca.png" referrerpolicy="no-referrer"></p> <p>△ 由 Gradle 管理的设备</p> </li> 
</ul> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2Fpreview" target="_blank">https://developer.android.com/studio/preview</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            