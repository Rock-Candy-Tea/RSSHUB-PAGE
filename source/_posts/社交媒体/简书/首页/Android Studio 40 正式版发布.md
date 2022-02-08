
---
title: 'Android Studio 4.0 正式版发布'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/7095626-06518a4cee73ddee.jpg'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/7095626-06518a4cee73ddee.jpg'
---

<div>   
<p><em>作者 / Adarsh Fernando, Product Manager</em><br>
即便在如今这个变幻莫测的时势里，我们依然看到来自世界各地开发者们的佳作——那就是 Android 上一个又一个精彩的应用。不论您是在厨房里用一台笔记本工作，还是在家中有更好的办公环境，您都需要更好的、与时俱进的趁手工具: Android Studio 4.0。更高效的代码编写、更快捷的编译速度，让您尽情地为用户们设计最棒的应用，即刻<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio" target="_blank">下载正式版</a>开始使用吧！<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="219" data-height="209"><img data-original-src="//upload-images.jianshu.io/upload_images/7095626-06518a4cee73ddee.jpg" data-original-width="219" data-original-height="209" data-original-format="image/png" data-original-filesize="25624" src="https://upload-images.jianshu.io/upload_images/7095626-06518a4cee73ddee.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><br>
Android Studio 4.0 的亮点众多，这里列出几项: 全新的 Motion Editor，可助您轻松打造应用动效；Build Analyzer 可以帮您找到导致编译速度缓慢的症结；您还可以尽情使用 Java 8 API，无需考虑您应用的最低 API 级别。另外，我们还根据大家的反馈调整了 CPU Profiler 界面，使得工作流更加直观，而且还提供了并排显示功能帮助您更轻松地分析线程活动。Layout Inspector 现在会如实显示应用 UI 中的真实数据，方便您更好地调试设备上显示的内容。<p></p>
<p>Android Studio 4.0 正式版的发布，离不开预览版用户们早期给出的宝贵反馈。请继续阅读本文，或者观看下方视频来详细了解 4.0 正式版的亮点和新功能。如果您已经迫不及待想要上手一试，请移步我们的官方网站<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio" target="_blank">下载 Android Studio 4.0 正式版</a>。</p>
<ul>
<li>
<strong>腾讯视频链接</strong><br>
<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fv.qq.com%2Fx%2Fpage%2Fq097904jf85.html" target="_blank">https://v.qq.com/x/page/q097904jf85.html</a>
</li>
<li>
<strong>Bilibili 视频链接</strong><br>
<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1cv411679P%2F" target="_blank">https://www.bilibili.com/video/BV1cv411679P/</a>
</li>
</ul>
<h2>设计</h2>
<p><strong>Motion Editor</strong><br>
<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdeveloper.android.google.cn%2Ftraining%2Fconstraint-layout%2Fmotionlayout" target="_blank">MotionLayout API</a> 进一步拓展了 ConstraintLayout 的丰富功能，使得 Android 开发者能在应用中管理复杂的动效和 widget 动画。Android Studio 4.0 中新加入的 Motion Editor 让开发者能在其界面中创建、编辑和预览 MotionLayout 动画，从而更轻松地驾驭这个 API。从创建文件，到编辑约束设置、转场动画、关键帧以及视图属性，Motion Editor 都会为您代劳，再也无需手动创建和编辑复杂的 XML 文件——当然如果您的确需要查看的话，也只需要轻点一下鼠标即可。我们提供的便捷体验还不止于此: 如果您已经在使用 ConstraintLayout，可以通过 IDE 轻松将其转换成 MotionLayout。前往<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fwrite%2Fmotion-editor" target="_blank">开发者官网</a>了解更多。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="600" data-height="477"><img data-original-src="//upload-images.jianshu.io/upload_images/7095626-d2cf75a547fb4fb2" data-original-width="600" data-original-height="477" data-original-format="image/gif" data-original-filesize="1042127" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">△ 在 Motion Editor 中创建、编辑和预览动画</div>
</div>
<p><strong>Layout Inspector 全新升级</strong><br>
想要搞清楚某个属性的取值从何而来？或者想通过实时的 3D 画面轻松查看视图的嵌套层级？全新的 Layout Inspector 就可以帮您轻松做到。它提供的数据会与正在运行的应用完全同步，更会让您对各个资源在应用中如何排布和计算一览无余，使得 UI 调试变得更加简单直观。</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="624"><img data-original-src="//upload-images.jianshu.io/upload_images/7095626-33ef7fb4da6959ac" data-original-width="1080" data-original-height="624" data-original-format="image/png" data-original-filesize="331458" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">△ 通过 Layout Inspector 实时调试应用 UI</div>
</div><p></p>
<p>在主菜单中依次选择 <strong>View > Tool Windows > Layout Inspector</strong> 来使用 Layout Inspector。如果您的应用是部署到 API 等级 29 或以上的设备，则可以使用到更丰富的功能，比如随着视图变化动态更新的布局层次结构、帮助您更好了解资源取值解析的详细视图属性信息、以及可以展示运行时 UI 结构的实时 3D 模型。您可以尽情在应用中导航、触发动画和视图转场，在这同时依然能精确调试 UI，让每一个像素都尽如人意。前往《<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzAwODY4OTk2Mg%3D%3D%26mid%3D2652055231%26idx%3D1%26sn%3D74d5b79c47b9b10481a3759c046932fd%26scene%3D21%23wechat_redirect" target="_blank">Android Studio 4.0+ 中新的 UI 层次结构调试工具</a>》了解更多。</p>
<p><strong>Layout Validation</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="719"><img data-original-src="//upload-images.jianshu.io/upload_images/7095626-b88b26973386fac5" data-original-width="1080" data-original-height="719" data-original-format="image/png" data-original-filesize="147229" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">△ 使用 Layout Validation 在多个屏幕中对比 UI
</div>
</div>
<p>在为多种硬件配置、屏幕尺寸和分辨率开发应用时，您需要确保在 UI 中做出的每一处修改都能在各个屏幕上完美展现。通过 Layout Validation 窗口，您可以同时预览 UI 在不同屏幕、不同配置中的呈现结果，从而轻松让应用适配好这些设备。只需点击 IDE 右上角的 <strong>Layout Validation</strong> 标签即可打开本窗口。</p>
<h2>开发与分析</h2>
<p><strong>CPU Profiler 界面升级</strong><br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="694"><img data-original-src="//upload-images.jianshu.io/upload_images/7095626-ba81fb6e57c34774" data-original-width="1080" data-original-height="694" data-original-format="image/png" data-original-filesize="179686" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">△ 升级后的 CPU Profiler 界面</div>
</div><p></p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fprofile%2Fcpu-profiler" target="_blank">CPU Profiler</a> 的设计目的是为您呈现应用中线程活动以及跟踪数据的丰富信息。开发者们在反馈中希望我们让这个工具的 UI 导航起来更为直观，以及让其中的数据更易于解读，于是我们在这个版本中带来了新的界面来回应大家的需求。在 Android Studio 4.0 中，CPU 活动记录从分析器的主时间轴中分离出来，并成组展现，以便于分析。您可以上下移动分组，也可以通过拖放操作重新排列组内的项目，从而打造更定制化的呈现布局。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="546"><img data-original-src="//upload-images.jianshu.io/upload_images/7095626-0e2745b19b639aa2" data-original-width="1080" data-original-height="546" data-original-format="image/png" data-original-filesize="342101" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">△ 并排显示使得分析线程活动更加轻松</div>
</div>
<p>并排显示使得分析更加轻松，您现在可以在 Thread Activity 时间轴中查看所有线程活动 (包括方法、函数和事件)，以及使用新加入的导航快捷键在数据间移动——如使用 W/A/S/D 四键进行精细的缩放和平移。我们还重新设计了 System Trace 界面，用不同的颜色来区分显示事件，从而在视觉上更加醒目。在线程排序方面，更繁忙的线程会优先展示，帮助您专注于所选线程中的数据。最后，在我们投入资源改善 CPU Profiler 的质量后，我们发现自 Android Studio 3.6 以来用户报告的记录错误率有了明显下降。本次更新还带来了更多值得尝试的改进，前往<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases%23cpu-profiler-upgrades" target="_blank">开发者官网</a>了解更多。</p>
<p><strong>编写代码缩减规则时的智能编辑器功能</strong><br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="632" data-height="244"><img data-original-src="//upload-images.jianshu.io/upload_images/7095626-e36d694c991473b9" data-original-width="632" data-original-height="244" data-original-format="image/png" data-original-filesize="55554" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">△ 编写 R8 代码规则时的智能编辑器功能</div>
</div><p></p>
<p>我们在 Android Gradle 插件 3.4.0 中引入了 R8，使得字节码转换 (desugaring)、缩减、混淆和 dex 处理能一步到位，这让构建性能得到了显著的提升。在创建 R8 的规则文件时，Android Studio 现在提供了智能编辑器功能，包括语法高亮、补全以及错误检查等。编辑器还与您的 Android 项目集成，为所有的类、方法和字段提供完整的符号补全，并提供快速导航和重构功能。</p>
<p><strong>IntelliJ IDEA 2019.3 平台更新</strong></p>
<p>Android Studio IDE 核心已经整合了 IntelliJ IDEA <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2019%2F11%2Fintellij-idea-2019-3-better-performance-and-quality%2F" target="_blank">2019.3</a> 和 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2020%2F02%2Fintellij-idea-2019-3-3-is-out%2F" target="_blank">2019.3.3</a> 版本的更新。这些更新主要用于提升 IDE 整体的质量和性能。</p>
<p><strong>Kotlin Android 实时模板</strong></p>
<p>实时模板 (Live Template) 是 IntelliJ 中一个很方便的功能: 您只需输入简单的关键词即可将常见的构造插入自己的代码中。Android Studio 现在为您的 Kotlin 代码提供了 Android 专用的实时模板。例如，您现在只需输入 toast 并按下 Tab 键即可快速插入一个 Toast 消息框。如需查看可用实时模板的完整列表，请打开 Settings (或 Preferences) 对话框，并依次选择 Editor > Live Templates。</p>
<p><strong>为 C++ 提供 Clangd 支持</strong></p>
<p>对使用 C++ 语言的开发者，我们现在改用 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fclangd.llvm.org%2F" target="_blank">clangd</a> 作为主要的语言分析引擎，用于代码导航、补全、检查、以及显示代码错误和警告。我们现在还将 clang-tidy 绑定在 Android Studio 中。想要配置 clangd 或 Clang-Tidy 的行为逻辑，请打开 IDE 的 Settings (或 Preferences) 对话框，并依次选择 Languages & Frameworks > C/C++ > Clangd (或 Clang-Tidy)，然后设置相应的选项。</p>
<h2>构建</h2>
<p>Android Gradle 插件 4.0.0 通过使用 Java 8 API (无需考虑您应用的最低 API 级别) 为 Android Studio 带来了 Build Analyzer 功能，并支持在动态功能模块之间创造功能对功能的依赖性。完整的更新列表请查看 <a href="https://links.jianshu.com/go?to=http%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases%2Fgradle-plugin%234-0-0" target="_blank">Android Gradle 插件 4.0.0 版本说明</a>。</p>
<p><strong>Build Analyzer</strong><br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="430"><img data-original-src="//upload-images.jianshu.io/upload_images/7095626-51aef7ec4391b602" data-original-width="1080" data-original-height="430" data-original-format="image/png" data-original-filesize="225459" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">△ 使用 Build Analyzer 发现构建性能瓶颈</div>
</div><p></p>
<p>Android 开发者会使用多种 Gradle 插件以及自定义构建逻辑来为自己的应用定制构建系统。然而，过时或错误配置的任务会延长构建时间，从而拖累开发效率，并导致开发人员心情沮丧、效率下降。Build Analyzer 可以帮助开发者找到构建中的瓶颈，那些显著拖累构建时间的插件和任务会被高亮显示，并同时给出缓解速度回退的操作建议。前往<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fbuild%2Fbuild-analyzer" target="_blank">开发者官网</a>了解更多。</p>
<p><strong>Java 8 语言库在 D8 和 R8 中的字节码转换 (desugaring)</strong></p>
<p>上一个版本的 Android Gradle 插件通过字节码转换操作，在所有 API 等级中支持了大量 Java 8 的语言功能，比如 lambda 表达式和方法引用。在 Android Studio 4.0 中字节码转换引擎得到了扩展，现在不管您应用的 minSdkVersion 是多少，都可以使用 Java 8 API (比如 java.util.stream、java.util.function 和 java.time)。前往<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Fwrite%2Fjava8-support" target="_blank">开发者官网</a>了解更多。</p>
<p><strong>功能模块层级的依赖关系</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="354"><img data-original-src="//upload-images.jianshu.io/upload_images/7095626-1e742b08e3a6c07c" data-original-width="1080" data-original-height="354" data-original-format="image/png" data-original-filesize="33532" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">△ 功能对功能的依赖性</div>
</div>
<p>在使用 Android Gradle 插件 4.0.0 及以上版本时，您可以指定一个动态功能模块依赖于另一个功能模块。这种依赖关系使得您的应用可以获得所需的模块来解锁更丰富的功能，从而减少下载需求，也使得应用更易于模块化。比如，一个 :video 功能可以依赖 :camera 功能。如果用户需要使用录制视频的功能，您的应用会在请求 :video 时自动下载所需的 :camera 模块。前往<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases%234-0-0-feature-plugin" target="_blank">开发者官网</a>了解更多。</p>
<p><strong>新的构建功能开关选项</strong></p>
<p>Android Gradle 插件内置了对现代代码库 (如数据绑定和视图绑定) 和构建功能 (如自动生成 BuildConfig 类) 的支持。但您可能不是每个项目都需要用到这些库和功能。在插件的 4.0.0 版本中，您可以单独关闭某个构建选项 (如下所示)，从而优化大型项目的构建性能。关于 DSL 和您可以操作的完整功能列表，请参阅<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases%2Fgradle-plugin%234-0-0" target="_blank">版本说明</a>。</p>
<pre><code>
android &#123;
    // The default value for each feature is shown below.
    // You can change the value to override the default behavior.
    buildFeatures &#123;
        // Determines whether to support View Binding.
        // Note that the viewBinding.enabled property is now deprecated.
        viewBinding = false
        // Determines whether to support Data Binding.
        // Note that the dataBinding.enabled property is now deprecated.
        dataBinding = false
        ...
    &#125;
&#125;
</code></pre>
<p>△ 用于启用/禁用构建功能的 Android Gradle 插件 DSL</p>
<p><strong>对 Kotlin DSL 脚本文件的基础支持</strong><br>
Android Studio 4.0 现在已经内置了对 Kotlin DSL 构建脚本文件 (*.kts) 的支持，这意味着 Kotlin 构建脚本有了完整的快速修复功能，并且能在 Project Structure 窗口中进行操作。虽然我们对使用 Kotlin 来配置构建有很高的期待，但接下来的一年中我们依然会继续完善 Android Gradle 插件的 DSL API，这可能会给 Kotlin 脚本用户带来 API 的重大变更 (breaking change)。从长远来看，这些改善终将使得 DSL 对 Kotlin 脚本用户来说更简单易用。</p>
<p><strong>依赖元数据</strong></p>
<p>在使用 Android Gradle 插件 4.0.0 及以上版本构建应用时，插件中会包含描述编译到您的应用中的库依赖关系的元数据。在上传应用时，Play Console 会检查这些元数据，并告知您哪些 SDK 以及应用中的依赖存在问题，在某些时候还会给出如何解决的反馈。</p>
<p>这些数据会被压缩，通过 Google Play 的签名密钥进行加密，并存储在发布的应用的签名模块中。如果您不愿意分享这些信息，可以在模块的 build.gradle 文件中加入以下内容:</p>
<pre><code>android &#123;
    dependenciesInfo &#123;
        // Disables dependency metadata when building APKs.
        includeInApk = false
        // Disables dependency metadata when building Android App Bundles.
        includeInBundle = false
    &#125;
&#125;
</code></pre>
<p>△ 禁用 APK 或 App Bundle 中的依赖元数据</p>
<p>现在让我们回顾一下 Android Studio 4.0 带来的改进以及新功能:</p>
<p><strong>设计:</strong></p>
<ul>
<li>Motion Editor: 轻松创建、编辑和预览 MotionLayout 动画</li>
<li>Layout Inspector 全新升级: 更加直观的实时调试体验</li>
<li>Layout Validation: 在多个屏幕上同时对比 UI</li>
</ul>
<p><strong>开发与分析:</strong></p>
<ul>
<li>CPU Profiler 更新: UI 更直观、更易于浏览，数据更易解读</li>
<li>R8 规则更新: 编写代码缩减规则的智能编辑器功能，如语法高亮、补全和错误检查</li>
<li>IntelliJ IDEA 2019.3 平台更新: 性能和质量得到提升</li>
<li>实时模板更新: 为 Kotlin 提供 Android 专用实时模板</li>
<li>Clangd 支持: 默认启用 Clangd 和 Clang-Tidy</li>
</ul>
<p><strong>构建:</strong></p>
<ul>
<li>Build Analyzer: 了解和找到构建时的性能瓶颈</li>
<li>Java 8 语言支持更新: Java 8 API 现在均可使用，与应用最低 API 等级无关</li>
<li>功能对功能的依赖性: 定义两个动态功能模块之间的依赖</li>
<li>buildFeatures DSL: 逐个启用/禁用构建功能，如数据绑定</li>
<li>Kotlin DSL: 对 Kotlin DSL 脚本文件的基础支持</li>
</ul>
<p>请参<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases%234-0-0" target="_blank">阅版本说明</a>，了解本次发布的完整信息。</p>
<h2>即刻开始使用</h2>
<p>请前往下载页面获取<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio" target="_blank"> Android Studio 4.0</a>。如果您使用的是旧版 Android Studio，可以直接更新到最新版本。</p>
<p>我们一如既往地期待着大家的反馈，如果您喜欢某个功能，或者发现了问题，请随时告诉我们。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="836" data-height="345"><img data-original-src="//upload-images.jianshu.io/upload_images/7095626-8d549d607d19b83a.jpg" data-original-width="836" data-original-height="345" data-original-format="image/png" data-original-filesize="19070" src="https://upload-images.jianshu.io/upload_images/7095626-8d549d607d19b83a.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
  
</div>
            