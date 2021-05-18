
---
title: 'Android Studio 4.2 现已发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://devrel.andfun.cn/devrel/posts/2021/05/8dg20I.png'
author: 开源中国
comments: false
date: Tue, 18 May 2021 17:10:00 GMT
thumbnail: 'https://devrel.andfun.cn/devrel/posts/2021/05/8dg20I.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>我们高兴地宣布，Android Studio 4.2 现已发布，并可以从稳定版发布渠道中下载。此版本的重心在于推出经过升级的 IntelliJ 平台以及一些新功能，这些新功能旨在提高 Android 应用开发者的工作效率。</p> 
<p>我们知道，有时将应用项目升级到最新版本并非易事。为了解决这一问题，我们在 Android Studio 4.2 中提供了全新的应用项目升级助手，此助手更易于项目迁移并使用最新的 Android Gradle 插件 API。此外，我们还向现有功能 (如 Database Inspector [数据库检查器]、System Trace、SafeArgs 支持、Apply Changes、新项目向导等) 做出了一系列优化。如果您在使用这些功能并正在寻找下一个稳定版本的 Android Studio，那么您可以立即下载 Android Studio 4.2！</p> 
<p>请 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F05%2FiRu5fv.mp4" target="_blank">点击这里</a> 查看按照主要开发者流程依次介绍 Android Studio 4.2 中新功能的视频。</p> 
<h2><strong>开发</strong></h2> 
<ul> 
 <li> <p><strong>IntelliJ 平台更新</strong> - Android Studio 4.2 包含 IntelliJ IDEA Community Edition 2020.2 中的所有主要功能和更新，其中包括新版 GitHub PR 界面以及全新的集中式问题反馈窗口等。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2020%2F07%2Fintellij-idea-2020-2-is-released%2F" target="_blank">点击这里</a> 了解更多详情。</p> </li> 
 <li> <p><strong>Safe Args 支持</strong> - 如果您希望在使用 Jetpack 导航组件时在应用中的两个目标位置之间传递数据，建议使用 Safe Args 来确保数据封装。通过使用 Android Studio 4.2，您现在可以自动补全 Directions Args 的代码，并实现从源到 XML 的代码导航。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fguide%2Fnavigation%2Fnavigation-pass-data" target="_blank">点击这里</a> 了解更多详情。</p> </li> 
</ul> 
<p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/05/8dg20I.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>△ Safe Args 支持</p> 
</blockquote> 
<ul> 
 <li><strong>新项目向导和模块向导更新</strong> - 在此版本中，为了更易于发现 Android 设备类型，我们对新项目向导的视觉效果做出新的设计，同时还向每个模板添加了 ViewBinding。此外，我们对新模块向导的视觉效果也有更新，让您更轻松地了解可以添加到应用的各种模块类型。</li> 
</ul> 
<p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/05/kXnSsA.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>△ 新项目向导和新模块向导</p> 
</blockquote> 
<h2><strong>调试</strong></h2> 
<ul> 
 <li><strong>Database Inspector (数据库检查器) 改进</strong> - 通过 Database Inspector，您可以更轻松地管理和监控您的应用内数据库。在此版本中，我们做出了一些新的优化。新增了离线模式，这样您在进程中断后仍可以保持对应用数据库的检查，更易于在应用崩溃后对其做出诊断。同时我们也添加了一项便捷的查询历史记录选项。</li> 
</ul> 
<p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/05/KEtmrY.gif" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>△ 使用 Database Inspector 查询历史记录</p> 
</blockquote> 
<ul> 
 <li><strong>Retrace 命令行工具</strong> - 作为应用编译流程的一部分，R8 会混淆 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fbuild%2Fshrink-code%23decode-stack-trace" target="_blank">Kotlin 和 Java 编程语言</a> 代码。为了减少应用的内存占用量，其混淆并缩短了类型和方法名称，使得堆栈轨迹无法解码。Retrace 命令行工具会对这些名称做去混淆处理并使用 mapping.txt 文件恢复内联框架，以再次使得堆栈轨迹易于理解。您可前往 ./sdk/cmdline-tools/latest/bin/retrace，找到这个新的独立工具。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fcommand-line%2Fretrace" target="_blank">点击这里</a> 了解更多详情。</li> 
</ul> 
<h2><strong>构建</strong></h2> 
<ul> 
 <li><strong>AGP 升级助手</strong> - 将项目迁移到最新版本的 Android Gradle 插件 (AGP) 有时候比较棘手，在使用已弃用的 API 时更是如此。为了解决此问题并为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroid-developers.googleblog.com%2F2020%2F12%2Fannouncing-android-gradle-plugin.html" target="_blank">过渡到 Android Gradle 插件 7.0</a> 做出更好的准备，我们开发了一款新的升级助手。借助此助手，您可以切换针对项目执行的命令以升级至更高版本的 AGP、预览将受到 AGP 升级影响的文件并最终对已弃用的配置进行全局更新。</li> 
</ul> 
<p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/05/8hJ3AV.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>△ AGP 升级助手</p> 
</blockquote> 
<ul> 
 <li> <p><strong>Apply Changes 增强</strong> - 您可通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Frun%23apply-changes" target="_blank">Apply Changes</a>，将代码和资源更改推送至正在运行的应用，且无需重新启动应用。在 Android Studio 4.2 中，我们扩展了与 Apply Changes 相兼容的大量更改，当在 Android 11 以上版本的设备或模拟器上运行时，我们可添加资源 (占需要完全重启的更改的 23%) 和添加静态的最终字段 (如常量)。</p> </li> 
 <li> <p><strong>Android Gradle 插件 4.2</strong> - 我们借助 AGP 4.2 做出了不少显著的更改。首先，我们实施了一个全新的资源编译器，用以提高构建性能，尤其是 Windows 设备上的构建性能。其次，我们已将默认的 Java 编程语言更新为版本 8。最后，我们为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsource.android.google.cn%2Fsecurity%2Fapksigning%2Fv3" target="_blank">APK v3</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsource.android.google.cn%2Fsecurity%2Fapksigning%2Fv4" target="_blank">APK v4</a> 签名格式添加了支持。您可以查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases%2Fgradle-plugin" target="_blank">相关文档</a> 详细了解其他 AGP 更新。</p> </li> 
</ul> 
<pre><code>// build.gradle.kts

android &#123;
   ...
   signingConfigs &#123;
      config &#123;
          ...
          enableV3Signing(true)
          enableV4Signing(true)
      &#125;
   &#125;
&#125;

</code></pre> 
<blockquote> 
 <p>△ APK v3 和 APK v4 签名支持</p> 
</blockquote> 
<h2><strong>测试</strong></h2> 
<ul> 
 <li><strong>多设备部署</strong> - 在开发和测试应用时，多设备部署有时可以帮助您将应用部署到多个设备上来查看结果。此功能是早期 Android Studio 版本中的一项功能，现在我们再次引入了它并将其直接集成到 Android Studio 4.2 中的设备选择菜单中。需要注意的是，如果您向多个设备部署测试，系统可能会提示您启用此行为。</li> 
</ul> 
<p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/05/7ofMEX.gif" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>△ 多设备部署</p> 
</blockquote> 
<h2><strong>性能剖析</strong></h2> 
<ul> 
 <li><strong>System Trace 改进</strong> - 为了解应用的详细性能特性，可以借助此改进 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F347876061" target="_blank">在 Android Studio 性能剖析器内部使用 System Trace 功能</a>。在此版本的 Android Studio 中，我们现在为 system trace 推出了一个全新的事件表。通过这个全新的表格视图，您可在一个紧凑的用户界面中，一站式查看 BufferQueue、RSS 内存计数器和 CPU 核心频率。</li> 
</ul> 
<p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/05/NdSdt8.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>△ 使用新 System Trace 事件表的性能剖析器</p> 
</blockquote> 
<p>简要回顾，Android Studio 4.2 包括以下新增优化和功能:</p> 
<p><strong>开发</strong></p> 
<ul> 
 <li>IntelliJ 2020.2.3 平台更新</li> 
 <li>Safe Args 支持</li> 
 <li>新项目向导和模块向导更新</li> 
</ul> 
<p><strong>调试</strong></p> 
<ul> 
 <li>Database Inspector (数据库检查器) 改进</li> 
 <li>Retrace 命令行工具</li> 
</ul> 
<p><strong>构建</strong></p> 
<ul> 
 <li>AGP 升级助手</li> 
 <li>Apply Changes 优化</li> 
 <li>Android Gradle 插件 4.2</li> 
</ul> 
<p><strong>测试</strong></p> 
<ul> 
 <li>多设备部署</li> 
</ul> 
<p><strong>性能剖析</strong></p> 
<ul> 
 <li>System Trace 改进</li> 
</ul> 
<p>想了解更多详细信息，您可以参阅 Android Studio <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases%2F%233-3-0" target="_blank">版本说明</a>、Android Gradle <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases%2Fgradle-plugin" target="_blank">插件版本说明</a> 以及 Android 模拟器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases%2Femulator" target="_blank">版本说明</a>。</p> 
<h2><strong>快速上手</strong></h2> 
<p>您可以前往 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2F" target="_blank">下载</a> 最新版本的 Android Studio 4.2。如果您使用的是之前版本的 Android Studio，则只需更新到最新版本的 Android Studio 即可。如果您想保留稳定版本的 Android Studio，则可以同时运行 Android Studio Arctic Fox 稳定版和 Canary 版本。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fpreview%2Finstall-preview" target="_blank">点击这里</a> 了解更多详情。</p> 
<p>欢迎大家提供反馈，分享您喜欢的内容、您发现的问题或希望看到的功能的相应想法。如果有任何错误或问题，欢迎随时向我们 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsource.android.google.cn%2Fsource%2Freport-bugs%23developer-tools" target="_blank">提交问题</a>。也欢迎您持续关注我们，及时了解最新动态。</p> 
<p><em>Java 是 Oracle 和/或其附属公司的注册商标。</em></p>
                                        </div>
                                      
</div>
            