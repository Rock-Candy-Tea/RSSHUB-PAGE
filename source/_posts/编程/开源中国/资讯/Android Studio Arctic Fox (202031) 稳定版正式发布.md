
---
title: 'Android Studio Arctic Fox (2020.3.1) 稳定版正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://devrel.andfun.cn/devrel/posts/2021/08/BWTera.png'
author: 开源中国
comments: false
date: Wed, 11 Aug 2021 14:27:00 GMT
thumbnail: 'https://devrel.andfun.cn/devrel/posts/2021/08/BWTera.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/08/BWTera.png" referrerpolicy="no-referrer"></p> 
<p><em>作者 / Amanda Alexander, Android 产品经理</em></p> 
<p>我们高兴地宣布，Android Studio Arctic Fox 现已正式进入稳定版发布渠道，欢迎大家下载。这个最新版本支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F394742195" target="_blank">Jetpack Compose 1.0</a>，用于构建原生界面的 Android 全新工具包。另外，此版本也强调对多设备类型的覆盖，包括 Wear OS 设备，并提供新版后台任务管理器等功能，帮助开发者提高工作效率。我们基于开发者的反馈打造出了这套全新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fmp%2Fappmsgalbum%3F__biz%3DMzk0NDIwMTExNw%3D%3D%26action%3Dgetalbum%26album_id%3D1873156382456135681%23wechat_redirect" target="_blank">Android Studio</a>，助力开发者社区更快地构建高质量、现代化的应用，且覆盖多样的设备！</p> 
<p>请注意: 去年，我们 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F336006084" target="_blank">宣布</a> 调整 Android Studio 的版本编号方案，以匹配 Android Studio 所基于的 IntelliJ IDEA 的年份和版本，并加入我们自己的补丁程序编号。我们将使用代号 (按字母顺序递增): 第一个是 Arctic Fox，第二个是 Bumblebee (目前处于 Canary 版)。Android Studio Arctic Fox (2020.3.1) 将 Android Studio 更新到了 IntelliJ 平台的 2020.3 版本，其中加入了大量新功能，包括调试程序交互提示、VCS 更新以及几项新的代码编辑器改进，以提升您的工作效率。请阅读 IntelliJ 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2020%2F12%2Fintellij-idea-2020-3%2F" target="_blank">版本说明</a> 了解详情。</p> 
<p>为让大家快速设计现代化 UI，我们针对 Jetpack Compose 添加了额外的功能。借助 Compose Preview，您可以为 Compose UI 的多个组件创建预览，以便在多个维度 (如主题、屏幕和字号大小等) 即时查看您的修改带来的变化。部署预览 (Deploy Preview) 至设备的功能让您可以直接将 Compose 代码片段部署到设备或模拟器中，以便快速测试一小段代码。我们在布局检查器 (Layout Inspector) 中添加了 Compose 支持，方便您在需要更深入了解布局时，能够轻松地理解布局的渲染方式。此外，我们还新增了字元实时编辑功能，这样您就可以在预览中以及在模拟器或实体设备运行应用时，即时查看 Compose 代码的变化结果，而无需再次进行编译。</p> 
<p>在强化设备支持方面，我们构建了新的 Wear OS 配对助手，以简化 Wear OS 模拟器与实体或虚拟手机的配对。您还可以立即通过 Wear OS 3 的开发者预览版系统映像来使用最新版本的 Wear OS。当您运行 Wear OS 模拟器时，您还会发现我们增加了对心率传感器 (Heart Rate Sensor) API 的支持。我们针对面向 Google TV 的应用加入了最新的 Google TV 遥控器功能，并更新了 Google TV 系统映像，让大家可以体验最新的界面设计。此外，我们完善了 Automotive OS 的开发和测试工作流，让开发者可以使用模拟器回放汽车传感器数据来模拟驾驶场景。对于面向平板电脑的应用，我们更新了所有的模板，使它们原生支持横屏。无论您是针对小屏还是大屏设备进行开发，我们都加入了新的功能来帮助您持续打造创新且出色的应用。</p> 
<p>最后，为提高开发者的工作效率，我们增加了一些能让您更高效工作的功能。例如，我们为 Android 12 添加了 lint 检查，从而帮助大家构建面向下一代 Android 的应用。为帮助您测试代码，我们在布局编辑器 (Layout Editor) 中增加了无障碍功能扫描器 (Accessibility Scanner)，以便您更轻松地识别布局中的无障碍问题，而新的测试矩阵 (Test Matrix) 让您可以实时跨多设备并行查看测试结果。此外，我们添加了对搭载 Apple 芯片 (arm64) 的硬件的预览支持，并扩展了模拟器控件，以扩大测试的覆盖面。最后，在调试方面，新的后台任务检查器 (Background Task Inspector) 可以帮助您分析应用的后台任务处理器 (worker)。</p> 
<p>Android Studio Arctic Fox 中的改进不胜枚举。要查看完整更新列表，请参阅 Android Studio Arctic Fox (2020.3.1) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F375208544" target="_blank">Beta 版发布文章</a> 和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases" target="_blank"> 版本说明</a>。 您也可以观看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevrel.andfun.cn%2Fdevrel%2Fposts%2F2021%2F08%2FH69M2R.mp4" target="_blank">视频</a> 了解不容错过的更新亮点。</p> 
<h2><strong>设计</strong></h2> 
<p>使用 @Preview 注释生成 Compose 代码的预览，并对多个组件的不同配置 (例如不同设备或主题) 进行可视化。Compose Preview 可以让您更轻松地针对代码中的 Composables 创建心理映射。</p> 
<p><img alt="△ Compose Preview" src="https://devrel.andfun.cn/devrel/posts/2021/08/iWI4Gt.gif" referrerpolicy="no-referrer"></p> 
<p>△ Compose Preview</p> 
<p><strong>Layout Inspector 支持 Compose</strong></p> 
<p>无论应用是完全通过 Compose 打造，还是结合使用了 Compose 和 Views，Layout Inspector 都能让您获取更多有关布局的详情，并进行问题排查。例如，您能够看到传递至各个 Composable 的参数和修饰符。在开发应用时，您还可以选择启用实时更新 (Live Updates)，以从设备串流数据。</p> 
<p><img alt="△ Compose Layout Inspector" src="https://devrel.andfun.cn/devrel/posts/2021/08/WHbIR0.gif" referrerpolicy="no-referrer"></p> 
<p>△ Compose Layout Inspector</p> 
<p><strong>字元实时编辑</strong></p> 
<p>您现在可以快速编辑代码中的字元 (字符串、数字、布尔运算等)，并立即在屏幕 (不论是预览、模拟器或实体设备) 上查看更改结果，而无需进行编译。</p> 
<p><img alt="△ 字元实时编辑: 编辑字符串，并在预览中实时查看改动结果" src="https://devrel.andfun.cn/devrel/posts/2021/08/4vxL8g.gif" referrerpolicy="no-referrer"></p> 
<p>△ 字元实时编辑: 编辑字符串，并在预览中实时查看改动结果</p> 
<h2><strong>设备</strong></h2> 
<p><strong>Wear OS 配对</strong></p> 
<p>全新 Wear OS 配对助手将帮助您完成配对，从而简化 Wear OS 模拟器与虚拟或实体手机的配对过程。请注意，此功能目前可用于和 Wear OS 2 配套设备的配对，对 Wear OS 3 的支持将在不久后推出。请阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Ftraining%2Fwearables%2Fapps%2Fcreating%23pairing-assistant" target="_blank">官方文档</a> 了解详情。</p> 
<p><img alt="△ Wear OS 模拟器配对助手对话框" src="https://devrel.andfun.cn/devrel/posts/2021/08/18MPbN.png" referrerpolicy="no-referrer"></p> 
<p>△ Wear OS 模拟器配对助手对话框</p> 
<p><img alt="△ 手机 + 手表模拟器配对成功状态" src="https://devrel.andfun.cn/devrel/posts/2021/08/WWrdhZ.png" referrerpolicy="no-referrer"></p> 
<p>△ 手机 + 手表模拟器配对成功状态</p> 
<h2><strong>开发者生产力</strong></h2> 
<p><strong>后台任务检查器 (Background Task Inspector)</strong></p> 
<p>当在运行级别 26 或更高级别 API 的设备上使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fjetpack%2Fandroidx%2Freleases%2Fwork" target="_blank">WorkManager 库</a> 2.5.0 或更高版本时，您可以使用全新的后台任务检查器 (Background Task Inspector) 来可视化、监控和调试应用的后台任务处理器。从菜单栏依次选择 <strong>View (视图) > Tool Windows (工具窗口) > App Inspection (应用检查)</strong>，即可访问此工具。请阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fr%2Fstudio-ui%2Fbackground-task-inspector-help" target="_blank">官方文档</a> 了解详情。</p> 
<p><img alt src="https://devrel.andfun.cn/devrel/posts/2021/08/EBeiCS.gif" referrerpolicy="no-referrer"></p> 
<p>下面简要总结一下 Android Studio Arctic Fox (2020.3.1) 稳定版新增的优化和功能:</p> 
<p><strong>设计</strong></p> 
<ul> 
 <li>Compose Preview</li> 
 <li>后台任务检查器 (Background Task Inspector)</li> 
 <li>部署预览到设备</li> 
 <li>字元实时编辑</li> 
</ul> 
<p><strong>设备</strong></p> 
<ul> 
 <li>Wear OS 配对</li> 
 <li>心率传感器</li> 
 <li>新版 Wear OS 系统映像</li> 
 <li>Google TV 遥控</li> 
 <li>Google TV 系统映像</li> 
 <li>Automotive OS 传感器回放</li> 
 <li>平板电脑模板支持</li> 
</ul> 
<p><strong>开发者生产力</strong></p> 
<ul> 
 <li>IntelliJ 2020.3.1</li> 
 <li>Android 12 lint 检查</li> 
 <li>非传递性 R 类重构</li> 
 <li>Apple 芯片支持预览</li> 
 <li>Android 模拟器扩展控件</li> 
 <li>后台任务检查器 (Background Task Inspector)</li> 
 <li>布局编辑器中的无障碍功能扫描器 (Accessibility Scanner)</li> 
 <li>测试矩阵 (Test Matrix)</li> 
 <li>内存分析器 (Memory Profiler) 的新录制界面</li> 
 <li>AGP 升级助手改进</li> 
 <li>C++ 编辑器: 在调试程序中设置执行点</li> 
</ul> 
<p>欲了解更多详细信息，请参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases%2F%233-3-0" target="_blank">Android Studio 版本说明</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases%2Fgradle-plugin" target="_blank">Android Gradle 插件版本说明</a> 以及 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases%2Femulator" target="_blank">Android 模拟器版本说明</a>。</p> 
<h2><strong>即刻开始使用</strong></h2> 
<p><strong>下载 Android Studio</strong></p> 
<p>您现在就可以 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2F" target="_blank">下载最新版本</a> 的 Android Studio Arctic Fox，或者 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%23downloads" target="_blank">下载 Apple 芯片预览版</a>。如果您使用的是之前版本的 Android Studio，则只需更新到最新版本的 Android Studio 即可。如果您想保留稳定版本的 Android Studio，则可以同时运行 Android Studio Arctic Fox 稳定版和 Canary 版本。请阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fpreview%2Finstall-preview" target="_blank">官方文档</a> 了解详情。</p> 
<p>我们期待着您的反馈，无论是您喜欢的内容、产品中的问题，以及希望加入的功能。如果您发现错误或问题，欢迎随时 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsource.android.google.cn%2Fsource%2Freport-bugs%23developer-tools" target="_blank">提交</a> 给我们。</p>
                                        </div>
                                      
</div>
            