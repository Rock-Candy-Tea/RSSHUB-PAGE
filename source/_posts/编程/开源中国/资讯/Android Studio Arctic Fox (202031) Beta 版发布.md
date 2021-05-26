
---
title: 'Android Studio Arctic Fox (2020.3.1) Beta 版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://devrel.andfun.cn/devrel/posts/2021/05/TQYdaK.png'
author: 开源中国
comments: false
date: Wed, 26 May 2021 13:45:00 GMT
thumbnail: 'https://devrel.andfun.cn/devrel/posts/2021/05/TQYdaK.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt="△ Android Studio Arctic Fox 启动画面" src="https://devrel.andfun.cn/devrel/posts/2021/05/TQYdaK.png" referrerpolicy="no-referrer"></p> 
<p>Android Studio Arctic Fox 启动画面</p> 
<p><em>作者 / Paris Hsu, Product & Design, Android</em></p> 
<p><em>注: 正如我们 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F336006084" target="_blank">去年年底宣布</a> 的那样，我们已经改变了版本编号方案，以配合 Android Studio 所基于的 IntelliJ IDE 编号，即 2020.3，再加上我们自己的补丁编号，以及一个便于记忆和使用的代号。我们将按字母顺序安排代号，第一个便是 Arctic Fox，它现在处于 Beta 版；下一个代号是 Bumblebee，现在则还在 Canary 渠道中。</em></p> 
<p>现在，我们很高兴向大家公布 Android Studio Arctic Fox (2020.3.1) Beta: 官方 Android IDE 的最新版本，专注于设计、设备和开发者生产力。您现在就可以在 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fpreview" target="_blank">Beta 版渠道</a> 下载，以尝试在 Google I/O 2021 期间发布的所有新功能:</p> 
<p>世界各地的开发者社区尽管在过去的一年里不得不适应各种挑战，但仍在继续创造令人惊叹的创新应用。得益于社区的反馈，我们为大家提供并更新了这套工具，旨在赋能三大主题:</p> 
<ul> 
 <li> <p><strong>快速 UI 设计</strong> - 使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fjetpack%2Fcompose" target="_blank">Jetpack Compose</a>，创建现代 UI 从未如此简单。我们提供各种工具以帮助您完成设计之旅: 在不同的配置中创建预览，用 Compose Preview 导航您的代码，用 Deploy Preview to Device 进行单独测试，用 Layout Inspector 检查整个应用。在整个迭代过程中，您可以快速编辑字符串和数字，并看到即时更新。此外，通过 Layout Editor 中的 Accessibility Scanner，您可以查看基于 View 的布局是否存在无障碍问题。</p> </li> 
 <li> <p><strong>覆盖新设备，无论大小</strong> - 将您的应用扩展到更广阔的舞台，不仅仅限于手机。无论是 Wear OS、Google TV 还是 Android Auto，我们都准备了新的模拟器和系统映像，甚至还有针对不同测试场景的真实模拟: 用 Wear OS Pairing 配对您的手表和手机模拟器，用 Wear OS 心率传感器进行一场虚拟的跑步，用 Google TV Remote Control 远程控制切换频道，用 Automotive OS Sensor Replay 进行驾驶。</p> </li> 
 <li> <p><strong>提升开发者生产力</strong> - 我们希望确保您的工作空间和环境为最新的系统做好准备，并优化速度和质量。现在，您可以享受 Intellij 2020.3 重大更新带来的一大批新功能和改进，在应用中测试 Android 12 所带来的新功能，用 Memory Profiler 的新 UI 提升应用性能，用 WorkManager Inspector 捋清后台任务关系，并使用 Non-Transitive R 类 IDE Refactoring 来提高构建速度。</p> </li> 
</ul> 
<p>简而言之，这是一次不容错过的升级！围绕这些主题，Beta 版中还有很多功能和改进供您体验，请继续阅读本文或观看下面的演讲，以了解更多亮点。您也可以先跳过阅读，直接去 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fpreview" target="_blank">Beta 渠道</a> 下载 Android Studio Arctic Fox (2020.3.1) Beta，现在就上手尝试一下最新的功能吧！请向我们提交反馈，帮助我们在下一个版本的 Android Studio 中继续聚焦您最关心的领域。</p> 
<h2><strong>Android Studio Arctic Fox (2020.3.1) Beta 特性一览</strong></h2> 
<p>下面是 Android Studio Arctic Fox (2020.3.1) Beta 中新功能的完整列表，按三大主题组织:</p> 
<p><strong>设计</strong></p> 
<ul> 
 <li><strong>Compose Preview</strong> - 用 Compose Preview 创建 Compose UI 的预览！通过使用 @Preview 注释，Compose Preview 可以在不同的配置 (即主题、设备) 下一次可视化多个组件，并为您创建一个心理地图来导航您的代码。</li> 
</ul> 
<p><img alt="△ Compose Preview" src="https://devrel.andfun.cn/devrel/posts/2021/05/Ng2pMe.gif" referrerpolicy="no-referrer"></p> 
<p>Compose Preview</p> 
<ul> 
 <li><strong>Compose Layout Inspector</strong> - 您现在可以用 Layout Inspector 检查用 Compose 编写的布局。无论您的应用是完全用 Compose 编写的布局，还是混合使用了 Compose 和 View，Layout Inspector 都能帮助您了解布局如何在设备或模拟器上呈现，获得丰富的细节 (如传递给每个 Composable 的参数和修饰符)，并调试可能出现的问题。当您与应用互动时，您现在还可以选择启用<strong>实时更新 (Live Updates)</strong>，以不断地从您的设备上串流数据，或者禁用实时更新而只在需要时使用<strong>刷新 (Refresh)</strong> 动作来减少对设备的性能影响。</li> 
</ul> 
<p><img alt="△ Compose Layout Inspector" src="https://devrel.andfun.cn/devrel/posts/2021/05/i9nMFB.gif" referrerpolicy="no-referrer"></p> 
<p>Compose Layout Inspector</p> 
<ul> 
 <li><strong>部署预览到设备</strong> - 使用此功能将 UI 片段部署到设备或模拟器上，从而在设备中测试您的一小部分代码，而无需启动完整应用。您的预览将获得和应用相同的运行环境 (权限、资源)。只需点击部署到设备 (Deploy to device) 图标，其位于 Compose 预览顶部或者代码编辑器 gutter 条的 @Preview 注释旁边，Android Studio 将把该 @Preview 部署到连接的设备或模拟器中。</li> 
</ul> 
<p><img alt="△ 注意预览和编辑器 gutter 条中的部署到设备按钮" src="https://devrel.andfun.cn/devrel/posts/2021/05/4wjMge.gif" referrerpolicy="no-referrer"></p> 
<p>注意预览和编辑器 gutter 条中的部署到设备按钮</p> 
<ul> 
 <li><strong>字元实时编辑</strong> - 字元的实时编辑功能让使用 Compose 的开发者可以快速编辑代码中的字元 (字符串、数字、布尔运算)，并立即看到结果，无需等待编译。该功能通过让代码的变化在预览、模拟器或实体设备中近乎即时地体现，从而提高您的生产力。</li> 
</ul> 
<p><img alt="△ 编辑数字和字符串，并即刻在预览和设备上看到结果" src="https://devrel.andfun.cn/devrel/posts/2021/05/Y3nJk0.gif" referrerpolicy="no-referrer"></p> 
<p>编辑数字和字符串，并即刻在预览和设备上看到结果</p> 
<ul> 
 <li><strong>Layout Editor 中的 Accessibility Scanner</strong> - Android Studio 现在与 Android Accessibility Test Framework 集成，以帮助您发现布局中的无障碍问题。在使用 Layout Editor 时，点击错误报告按钮来查看本面板。Accessibility Scanner (无障碍扫描器) 将报告与无障碍相关的问题，并为一些常见的问题 (如缺少内容描述，或对比度过低等) 推荐修复方法。</li> 
</ul> 
<p><img alt="△ Layout Editor 中的 Accessibility Test Framework Scanner" src="https://devrel.andfun.cn/devrel/posts/2021/05/ughLgA.gif" referrerpolicy="no-referrer"></p> 
<p>Layout Editor 中的 Accessibility Test Framework Scanner</p> 
<p><strong>设备</strong></p> 
<ul> 
 <li><strong>Wear OS 配对</strong> - 我们创建了一个新的 Wear OS 配对助手，以指导开发者一步一步在 Android Studio 中直接将 Wear OS 模拟器与实体或虚拟手机进行配对。您可以通过 "设备" 下拉菜单 > Wear OS 模拟器配对助手 (<strong>Wear OS emulator pairing assistant</strong>) 使用此功能。请注意，目前只支持与 Wear OS 2 伴侣配对，对 Wear OS 3 的支持将很快推出。请阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Ftraining%2Fwearables%2Fget-started%2Fcreating%23pairing-assistant" target="_blank">官方文档</a> 了解详情.</li> 
</ul> 
<p><img alt="△ Wear OS 模拟器配对助手对话框" src="https://devrel.andfun.cn/devrel/posts/2021/05/0fLhTH.png" referrerpolicy="no-referrer"></p> 
<p>Wear OS 模拟器配对助手对话框</p> 
<p><img alt="△ 手机 + 手表模拟器配对成功状态" src="https://devrel.andfun.cn/devrel/posts/2021/05/aPZBQL.png" referrerpolicy="no-referrer"></p> 
<p>手机 + 手表模拟器配对成功状态</p> 
<ul> 
 <li><strong>新的 Wear OS 系统映像</strong> - Wear OS 3 开发者预览版系统映像现已推出，让您玩转 Wear OS 的最新版本！</li> 
</ul> 
<p><img alt="△ Wear OS 系统映像" src="https://devrel.andfun.cn/devrel/posts/2021/05/ahkoR4.jpg" referrerpolicy="no-referrer"></p> 
<p>Wear OS 系统映像</p> 
<ul> 
 <li><strong>适用于 Wear OS 模拟器的心率传感器</strong> - 为了帮助您测试 Wear OS 应用，Android 模拟器现在支持在运行 Wear OS 模拟器的时候使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Fandroid%2Fhardware%2FSensor%23TYPE_HEART_RATE" target="_blank">心率传感器 API</a>。请通过 Android Studio SDK 管理器下载 Android 模拟器 v30.4.5，这是支持本功能的最低版本。</li> 
</ul> 
<p><img alt="△ Wear OS 模拟器中的心率传感器" src="https://devrel.andfun.cn/devrel/posts/2021/05/eeoq6k.gif" referrerpolicy="no-referrer"></p> 
<p>Wear OS 模拟器中的心率传感器</p> 
<ul> 
 <li><strong>Google TV 遥控</strong> - 在支持运行新的 Google TV 界面之外，我们还提供了更新的遥控面板，支持 Google TV 新增的遥控功能，包括用户档案和设置。</li> 
</ul> 
<p><img alt="△ Google TV 遥控" src="https://devrel.andfun.cn/devrel/posts/2021/05/Gt9zQo.gif" referrerpolicy="no-referrer"></p> 
<p>Google TV 遥控</p> 
<ul> 
 <li><strong>新的 Google TV 系统映像</strong> - 我们更新了系统映像，让您自由探索新的 Google TV 体验。</li> 
</ul> 
<p><img alt="△ Google TV 系统映像" src="https://devrel.andfun.cn/devrel/posts/2021/05/TFqaHL.png" referrerpolicy="no-referrer"></p> 
<p>Google TV 系统映像</p> 
<ul> 
 <li><strong>Automotive OS 传感器回放</strong> - 您现在可以使用 Android Automotive 模拟器来模拟驾驶场景，能够回放汽车传感器数据 (如速度、档位)，以完成您的开发和测试工作流程。</li> 
</ul> 
<p><img alt="△ Android Automotive OS 传感器回放" src="https://devrel.andfun.cn/devrel/posts/2021/05/acCTX3.png" referrerpolicy="no-referrer"></p> 
<p>Android Automotive OS 传感器回放</p> 
<p><strong>开发者生产力</strong></p> 
<ul> 
 <li> <p><strong>IntelliJ 平台更新</strong> - Android Studio Arctic Fox (2020.3.1) Beta 包括 IntelliJ 2020.3 平台版本，其中有许多新功能，如调试器互动提示，新的欢迎屏幕，以及大量新的代码编辑器增强功能，可以加快您的工作流程。请阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2020%2F12%2Fintellij-idea-2020-3%2F" target="_blank">官方文档</a> 了解详情。</p> </li> 
 <li> <p><strong>Android 12 lint 检查</strong> - 我们增加了针对为 Android 12 构建应用的 lint 检查，以便您可以在具体上下文中获得指导。仅举几例: 针对启动屏幕的自定义声明、精细位置使用的近似位置权限、媒体格式，以及传感器高采样率权限。</p> </li> 
 <li> <p><strong>非传递性 R 类重构</strong> - 在 Android Gradle 插件中使用非传递性 (non-transitive) R 类，可以为具有多个模块的应用带来更快的构建速度。它通过确保每个模块只包含对其自身资源的引用，而不从依赖关系中提取引用来防止资源的重复。您可以通过<strong>重构 (Refactor) > 迁移到非传递性 R 类 (Migrate to Non-transitive R Classes)</strong> 来使用此功能。</p> </li> 
 <li> <p><strong>Apple Silicon 支持预览</strong> - 对于那些在 Apple Silicon (arm64) 硬件上使用 MacOS 的用户，Android Studio Arctic Fox 提供了对这种新架构的预览支持。arm64 平台支持仍在积极开发中，但我们想为您提供起点，以获得您的反馈。由于这是一个针对 arm64 架构的预览版，您需要在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Farchive" target="_blank">Android Studio 下载存档页</a> 中寻找 Mac (Apple Silicon) 并单独下载该版本。</p> </li> 
 <li> <p><strong>模拟器工具窗口中的扩展控制</strong> - 当模拟器在工具窗口中打开时，开发者可以访问模拟器的所有扩展控件。这些扩展控件将为开发者提供强大的工具来在 Android studio 中测试应用，如导航回放、虚拟传感器和快照。要在 Android Studio 中启动模拟器，请进入 Android Studio 内的<strong>设置 > 工具 > 模拟器 (Preferences > Tools > Emulator)</strong>，然后选择 "在工具窗口中启动"。</p> </li> 
</ul> 
<p><img alt="△ 模拟器工具窗口中的扩展控制" src="https://devrel.andfun.cn/devrel/posts/2021/05/WQfVZ7.gif" referrerpolicy="no-referrer"></p> 
<p>模拟器工具窗口中的扩展控制</p> 
<ul> 
 <li><strong>Background Task Inspector</strong> - 现在，当使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fjetpack%2Fandroidx%2Freleases%2Fwork" target="_blank">WorkManager 库</a> 2.5.0 或更高版本时，您可以用 Background Task Inspector 来可视化、监控和调试应用的后台工作器。您可以通过菜单栏的<strong>视图 > 工具窗口 > 应用检查器 (View > Tool Windows > App Inspection)</strong> 来使用此功能。当您在 API 级别 26 及以上的设备上部署应用时，就能在 Background Task Inspector 标签页中看到工作器的活动情况，如下图所示。请阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fr%2Fstudio-ui%2Fbackground-task-inspector-help" target="_blank">官方文档</a> 了解详情。</li> 
</ul> 
<p><img alt="△ Background Task Inspector" src="https://devrel.andfun.cn/devrel/posts/2021/05/SYFtmv.gif" referrerpolicy="no-referrer"></p> 
<p>Background Task Inspector</p> 
<ul> 
 <li><strong>用 Test Matrix 进行并行设备测试</strong> - 插桩测试现在可以在多个设备上并行，并通过专门的插桩测试结果面板进行查看。该面板名为 Test Matrix，可以实时串流测试结果。请阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fpreview%2Ffeatures%23instrumentation-testing" target="_blank">官方文档</a> 了解详情。</li> 
</ul> 
<p><img alt="△ Test Matrix 在多个设备上并行运行测试" src="https://devrel.andfun.cn/devrel/posts/2021/05/xVF2EC.png" referrerpolicy="no-referrer"></p> 
<p>Test Matrix 在多个设备上并行运行测试</p> 
<ul> 
 <li><strong>Memory Profiler 的新录制界面</strong> - 我们为不同的录制活动整合了 Memory Profiler 界面，如捕获堆转储以及记录 Java、Kotlin 和原生内存分配。</li> 
</ul> 
<p><img alt="△ Memory Profiler: Java/Kotlin 分配记录" src="https://devrel.andfun.cn/devrel/posts/2021/05/RFaPqS.gif" referrerpolicy="no-referrer"></p> 
<p>Memory Profiler: Java/Kotlin 分配记录</p> 
<ul> 
 <li><strong>更新系统需求</strong> - 为了确保我们为 Android 开发者提供最佳体验，我们更新了使用 Android Studio 的系统需求。这些需求也代表了我们用来彻底测试 Android Studio 以确保高质量和高性能的配置，我们计划在未来更频繁地更新这些需求。虽然您仍然能够使用低于配置需求的系统，但我们不能保证这样做时的兼容性或支持。请前往官方 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%23Requirements" target="_blank">开发者网站</a> 查看更新的系统需求。</li> 
</ul> 
<p>最后总结一下 Android Studio Arctic Fox (2020.3.1) 测试版中包括的新增和改进功能:</p> 
<p><strong>设计</strong></p> 
<ul> 
 <li>Compose Preview</li> 
 <li>Compose Layout Inspector</li> 
 <li>部署预览到设备</li> 
 <li>字元实时编辑</li> 
 <li>Layout Editor 中的 Accessibility Scanner</li> 
</ul> 
<p><strong>设备</strong></p> 
<ul> 
 <li>Wear OS 配对</li> 
 <li>心率传感器</li> 
 <li>新的 Wear OS 系统映像</li> 
 <li>Google TV 遥控</li> 
 <li>Google TV 系统映像</li> 
 <li>Automotive OS 传感器回放</li> 
</ul> 
<p><strong>生产力</strong></p> 
<ul> 
 <li>Intellij 2020.3.1</li> 
 <li>Android 12 lint 检查</li> 
 <li>非传递性 R 类重构</li> 
 <li>Apple Silicon 支持预览</li> 
 <li>Android 模拟器扩展控件</li> 
 <li>Background Task Inspector</li> 
 <li>Test Matrix</li> 
 <li>Memory Profiler 新的录制界面</li> 
</ul> 
<p>您可能还在 I/O 大会上看到了其他的新功能，这些功能没有包含在上面的列表中，而是被安排在了 Android Studio (2021.1.1) Bumblebee Canary 中，还没有完全准备好在 Beta 渠道发布:</p> 
<p><strong>设计</strong></p> 
<ul> 
 <li>Interactive Compose 预览</li> 
 <li>Compose Animation 预览</li> 
 <li>Preview Configuration Picker</li> 
 <li>动画矢量 Drawable 预览</li> 
 <li>Compose Blueprint Mode</li> 
 <li>ConstraintLayout 的 Compose Constraints Preview</li> 
</ul> 
<p><strong>设备</strong></p> 
<ul> 
 <li>Automotive OS USB Passthrough - 即将推出</li> 
 <li>Automotive OS Rotary Controls - 即将推出</li> 
</ul> 
<p><strong>生产力</strong></p> 
<ul> 
 <li>Kotlin 协程调试器</li> 
 <li>Device Manager</li> 
 <li>在 Android Studio 中集成 Gradle Instrumented Test Runner</li> 
 <li>Gradle 托管设备</li> 
</ul> 
<h2><strong>别错过 Google I/O 2021 上的演讲</strong></h2> 
<p>随着这一激动人心版本的发布，Android Studio 团队还发布了一系列关于 Android Studio 的演讲。观看以下演讲视频以了解最新功能，并获得有关如何使用 Android Studio 的技巧和心得:</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F05%2FvpXHfE.mp4" target="_blank">Android 开发工具更新一览</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F05%2FYiKgSl.mp4" target="_blank">Android Kotlin 最新状态</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F05%2F3qq3Fg.mp4" target="_blank">设计工具更新一览</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F05%2FCi3ULZ.mp4" target="_blank">Android Gradle 插件更新一览</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F05%2F3qq3Fg.mp4" target="_blank">Android 测试工具更新一览</a></li> 
</ul> 
<h2><strong>即刻上手使用</strong></h2> 
<p>Android Studio Arctic Fox (2020.3.1) 是一个重要的版本，现在正是 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fpreview" target="_blank">下载</a> 并体验 Beta 版的好时机，以便及时将新功能融入您的工作流程。Beta 版虽已接近稳定版的品质，但与任何 Beta 版一样，错误可能仍然存在。所以，如果您确实发现了问题，请告知我们，我们会努力进行修复。如果您已经在使用 Android Studio，可以通过导航菜单查看 Beta 渠道的更新 (<strong>Help > Check for Update [Windows/Linux] , Android Studio > Check for Updates [OS X]</strong>)。更新到 Beta 版后即可使用新版本的 Android Studio 和 Android 模拟器。</p> 
<p>一如既往，希望大家多多提交反馈，告诉我们您喜欢哪些功能，看到了哪些问题。如果您发现了错误或 bug，请尽快提交给我们。</p> 
<p>您对产品的反馈及问题对我们非常重要，欢迎通过下方二维码向我们提交反馈。您的问题有可能出现在下一期的 FAQ 中并获得解答。感谢您的支持！</p> 
<p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/05/JzCYxp.jpg" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            