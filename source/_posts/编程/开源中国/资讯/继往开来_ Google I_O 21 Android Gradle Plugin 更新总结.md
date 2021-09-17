
---
title: '继往开来_ Google I_O 21 Android Gradle Plugin 更新总结'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-09461079702d0c6fa5625c0941283f4d9f5.png'
author: 开源中国
comments: false
date: Fri, 17 Sep 2021 17:11:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-09461079702d0c6fa5625c0941283f4d9f5.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>距离 Google I/O 2021 已经过去了一段时间，捋了捋关于 Android Gradle Plugin (AGP) 方面的东西，主要集中在 “What’s new in Android Gradle plugin” 这个 session。不过由于 2020 年没有 Google I/O，线下的活动也因为疫情全部暂停，所以这个 session 短短 11 分钟，信息量却相当大，几乎可当作是这两年更新的重点浓缩 (前后看了三遍)。也因此，这篇文章里我会放出很多额外的参考资料，挖了下最近一两年大家可能忽略了的 talks/posts/repos。文章整体脉络仍按这个 session 的 agenda 来。</p> 
 <h4><strong>性能提升</strong></h4> 
 <p><strong>Configuration Cache</strong></p> 
 <p>Gradle 的生命周期分为大的三个部分: 初始化阶段 (Initialization Phase)，配置阶段 (Configuration Phase)，执行阶段 (Execution Phase)。其中任务执行的部分只要处理恰当，已经能够很好的进行缓存和重用——重用已有的缓存是加快编译速度十分关键的一环，如果把这个机制运用到其他阶段当然也能带来一些收益。仅次于执行阶段耗时的一般是配置阶段，而今年 AGP 给我们带来的 Gradle Configuration Cache 的支持，一项自 Gradle 6.6 起开始孵化的新功能。它使得配置阶段的主要产出物——Task Graph 可以被重用，在示例的项目中这个优化可以带来 8s 左右的不必要等待 (如果 Gradle 脚本配置并没有改变)。</p> 
 <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3dce0de9-5102-4e92-bc51-2fe848ea9f80/912301e0-d18b-465a-9df7-1735b0204a98.png" height="394" src="https://oscimg.oschina.net/oscnet/up-09461079702d0c6fa5625c0941283f4d9f5.png" width="700" referrerpolicy="no-referrer"></p> 
 <ul> 
  <li>Configuration Cache <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2Fcurrent%2Fuserguide%2Fconfiguration_cache.html%23config_cache%3Arequirements" target="_blank">https://docs.gradle.org/current/userguide/configuration_cache.html#config_cache:requirements</a></li> 
  <li>Gradle 6.6 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.gradle.org%2Fintroducing-configuration-caching" target="_blank">https://blog.gradle.org/introducing-configuration-caching</a></li> 
 </ul> 
 <p>想体验这项优化只需要在执行 Gradle 命令时加入 –configuration-cache，例如 ./gradlew –configuration-cache help。由于 Configuration Cache 现在还未完全稳定，如果您想一直开启 (包括享受 IDE Sync 时的优化)，需要使用如下 properties:</p> 
 <pre><code>org.gradle.unsafe.configuration-cache=true

</code></pre> 
 <p>第一次使用时会看到计算 Task Graph 的提示:</p> 
 <pre><code>Calculating task graph as no configuration cache is available for tasks: :test-app:assembleDebug

</code></pre> 
 <p>成功后会在 Build 结束时提示:</p> 
 <pre><code>Configuration cache entry stored.

</code></pre> 
 <p>之后 Cache 就可以被下一次构建复用 (如果没有构建脚本修改):</p> 
 <pre><code>Reusing configuration cache.
...
51 actionable tasks: 2 executed, 49 up-to-date
Configuration cache entry reused.

</code></pre> 
 <p>作为插件使用者，发现常用插件出现不支持的情况，可先搜索是否有相同的问题已经出现，例如下面这个 Kotlin 1.4.32 插件和 Gradle 7.0 配合时出现的问题:</p> 
 <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/707aa14e-e321-4b2c-80cd-eb7074ecf265/d9565415-3e79-4295-b414-a356183fe49d.png" height="326" src="https://oscimg.oschina.net/oscnet/up-eb12093f993b63b283c693181a57ed30316.png" width="700" referrerpolicy="no-referrer"></p> 
 <p>在这个 YouTrack issue 下我们可以简单看到通过升级 Kotlin 插件版本至 1.5.0 以上即可解决。</p> 
 <ul> 
  <li>issue <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FKT-43605" target="_blank">https://youtrack.jetbrains.com/issue/KT-43605</a></li> 
 </ul> 
 <p>事实上 AGP/Kotlin/Gradle 核心的几个插件 (主要是背后的 Tasks) 在最近的版本都已经支持 Configuration Cache，通过这几篇文档 / issue 可以了解大概:</p> 
 <ul> 
  <li> <p>Help community Gradle plugins adopt the configuration cache #13490 - Gradle Github Issues</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fgradle%2Fissues%2F13490" target="_blank">https://github.com/gradle/gradle/issues/13490</a></p> </li> 
  <li> <p>Gradle Properties Change - Android Gradle Plugin 4.2 Release Note</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio%2Freleases%2Fgradle-plugin%234.2-gradle-properties" target="_blank">https://developer.android.google.cn/studio/releases/gradle-plugin#4.2-gradle-properties</a></p> </li> 
  <li> <p>Gradle Configuration Cache Support - Kotlin Doc</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkotlinlang.org%2Fdocs%2Fgradle.html%23gradle-configuration-cache-support" target="_blank">https://kotlinlang.org/docs/gradle.html#gradle-configuration-cache-support</a></p> </li> 
 </ul> 
 <p>而作为插件开发者，则还要关心 Configuration Cache 的适配工作。其重点在于: Task 的参数和内部实现需要避开直接传入 / 使用 Gradle 的几个 Context 及一些无法序列化的类。以我维护的 Seal 插件为例，它是一个解决 AndroidManifest.xml 冲突的小插件，我们执行 /gradlew –configuration-cache :test-app:assembleDebug 会发现有两个问题待修复:</p> 
 <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/868b0b3f-6c2e-4e61-aaee-297ff7b1c440/07c22133-7c30-4c65-940e-289171338692.png" height="225" src="https://oscimg.oschina.net/oscnet/up-5105767ae396340087095c91ff85f853102.png" width="700" referrerpolicy="no-referrer"></p> 
 <ul> 
  <li>Seal <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F2BAB%2FSeal" target="_blank">https://github.com/2BAB/Seal</a></li> 
 </ul> 
 <p>通过构建结束时输出的 Configuration Cache HTML Report 我们可以查看到详细的堆栈:</p> 
 <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4605576b-072f-434f-99b4-041e784a2c4a/a5df7d16-bbe9-4dd8-a0b8-a611b9401deb.png" height="793" src="https://oscimg.oschina.net/oscnet/up-cb92ddae444da7af4ebd0a245ff6067f092.png" width="700" referrerpolicy="no-referrer"></p> 
 <p>针对这个错误，其实仅仅需要把 project.logger 改成 this.logger 的引用即可:</p> 
 <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f1c05727-d11d-4e83-8be6-88564a679f53/580998b9-44bd-4f82-820d-07f3bfdd35f2.png" height="187" src="https://oscimg.oschina.net/oscnet/up-22aed666cf5edb8efc5703740ce9eb0236a.png" width="700" referrerpolicy="no-referrer"></p> 
 <p>对于更复杂的规则和用例，可以参考 Gradle 的文档以及 AGP 兼容 Configuration Cache 的心路历程 (修复了 400 多个 issues):</p> 
 <ul> 
  <li> <p>Configuration Cache</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2Fcurrent%2Fuserguide%2Fconfiguration_cache.html%23config_cache%3Arequirements" target="_blank">https://docs.gradle.org/current/userguide/configuration_cache.html#config_cache:requirements</a></p> </li> 
  <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzAwODY4OTk2Mg%3D%3D%26mid%3D2652068924%26idx%3D2%26sn%3D9a8b980cb4f6cf5eb998293fd10a98d9%26scene%3D21%23wechat_redirect" target="_blank">深入探索 Android Gradle 插件的缓存配置</a></p> </li> 
 </ul> 
 <p>最后，有个 Gradle 官方维护的 android-cache-fix-gradle-plugin，一些 AGP build cache、configuration cache 的特殊问题，可以在此处查阅下，说不定正好是您项目碰到的。</p> 
 <ul> 
  <li>android-cache-fix-gradle-plugin <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgradle%2Fandroid-cache-fix-gradle-plugin" target="_blank">https://github.com/gradle/android-cache-fix-gradle-plugin</a></li> 
 </ul> 
 <p><strong>Non-transitive R-classes</strong></p> 
 <p>事实上 R 文件的这类特性已经发展了很多年，可以参考这篇按时间顺序整理的文章。但是最新的 nonTransitiveAppRClass 特性需要 AGP 7.0 及以上，目前资料较少，在 Android Studio Arctic Fox 版本发布说明中有部分提及:</p> 
 <blockquote> 
  <p>非传递性 R 类重构: 在 Android Gradle 插件中使用非传递性 (non-transitive) R 类，可以为具有多个模块的应用带来更快的构建速度。它通过确保每个模块只包含对其自身资源的引用，而不从依赖关系中提取引用来防止资源的重复。您可以通过重构 (Refactor) > 迁移到非传递性 R 类 (Migrate to Non-transitive R Classes) 来使用此功能。</p> 
 </blockquote> 
 <ul> 
  <li>文章 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mobileit.cz%2FBlog%2FPages%2Fr-class.aspx" target="_blank">https://www.mobileit.cz/Blog/Pages/r-class.aspx</a></li> 
 </ul> 
 <p>开启方式如下:</p> 
 <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cab61dd1-71a2-4ef9-b17c-8b2c46f9c757/7187a830-b15f-4aa8-a22a-5addbf2066c9.png" height="1176" src="https://oscimg.oschina.net/oscnet/up-3aef4ab73dfdcdfa5dedb3f6c17078a4de5.png" width="700" referrerpolicy="no-referrer"></p> 
 <p>这个操作帮助您自动添加两行特性开启的代码到 gradle.properties，并重新 build project:</p> 
 <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a6006acc-95eb-4fbb-bedd-56fdfe30f4bc/c0e57b54-ba38-4507-a1f8-babae6a875e0.png" height="205" src="https://oscimg.oschina.net/oscnet/up-197fdf7ad19e3e4a2d30c62d66411cb75c3.png" width="700" referrerpolicy="no-referrer"></p> 
 <p><strong>Cacheable Lint Task</strong></p> 
 <p>Lint 的运行一直是耗时大户，在 AGP 7.0 后 (最早计划是 3.5，见这篇文档)，终于正式成为可缓存的 Task。</p> 
 <ul> 
  <li>文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2Fcurrent%2Fuserguide%2Fcaching_android_projects.html%23lint" target="_blank">https://docs.gradle.org/current/userguide/caching_android_projects.html#lint</a></li> 
 </ul> 
 <p><strong>其他</strong></p> 
 <p>另外 AS + AGP 自 4.x 以来还有一些提升的点:</p> 
 <ul> 
  <li> <p>Gradle Kotlin DSL 体验和性能提升，可以看到 Google I/O Android App 项目已经全部改成 *.gradle.kts 脚本；</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoogle%2Fiosched" target="_blank">https://github.com/google/iosched</a></p> </li> 
  <li> <p>AAPT2 的性能提升；</p> </li> 
  <li> <p>JDK 11 引入的性能提升；</p> </li> 
  <li> <p>…</p> </li> 
 </ul> 
 <p>可以在 AGP/AS 的 Release Notes 里找到这些信息。</p> 
 <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cd07b817-6b4c-44d2-a1c6-7d5570a7ef21/0e1e659d-602a-44b0-8fb1-89885e85ee88.png" height="455" src="https://oscimg.oschina.net/oscnet/up-45199236ad3596d875fb393700c82735066.png" width="700" referrerpolicy="no-referrer"></p> 
 <h4><strong>新的 DSL</strong></h4> 
 <p><strong>DSL Doc 迁移至 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fandroid.google.cn" target="_blank">android.google.cn</a></strong></p> 
 <p>旧的 AGP DSL 文档 从 3.4 之后就不再更新了。新的文档迁移至 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fandroid.google.cn" target="_blank">android.google.cn</a>，更加统一。依旧可按版本查看:</p> 
 <ul> 
  <li>当前版本 (Current Release): 即稳定版本 4.2；</li> 
  <li>预览版本 (Preview Releases): 即 beta 7.0 和 alpha 7.1 测试版；</li> 
  <li>之前的版本 (Past Releases): 即之前所有的老版本，但由于中间的更迭 / 切换，所以其实 3.5 -> 4.0 版本的文档都没有；</li> 
  <li>文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoogle.github.io%2Fandroid-gradle-dsl%2F" target="_blank">https://google.github.io/android-gradle-dsl/</a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fandroid.google.cn" target="_blank">android.google.cn</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Ftools%2Fgradle-api" target="_blank">https://developer.android.google.cn/reference/tools/gradle-api</a></li> 
 </ul> 
 <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b983d1b3-9390-40a5-a1c8-5e6ab26e1a15/e1ef1cc0-e9d0-4b0f-9d98-97f043d7bf18.png" height="516" src="https://oscimg.oschina.net/oscnet/up-b4ef4da2b949296d16e11ff07a70707fd40.png" width="700" referrerpolicy="no-referrer"></p> 
 <p>这个变化也反映在了 google source 的 tag 上，对于 AGP 源码来说 gradle-x.y.z 的 tag 自 3.4.0 之后就没有了，目前您可以使用 studio-x.y.z 例如 studio-4.2.0 来反向定位 AGP 的版本。</p> 
 <ul> 
  <li>google source <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroid.googlesource.com%2Fplatform%2Fmanifest%2F%2Brefs" target="_blank">https://android.googlesource.com/platform/manifest/+refs</a></li> 
 </ul> 
 <p><strong>Android Studio 提供的 AGP 升级助手</strong></p> 
 <p>为了让开发者便捷流畅地升级 AGP，AGP 配合 AS 推出了升级助手功能。这个新特性已经迭代了几个版本，目前对 Gradle Groovy DSL 脚本的升级十分有用，当您看到升级提示时 (一般发生在刚打开一个工程时):</p> 
 <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3008da64-b794-471e-986c-3eba8521b711/a5cf25d1-a089-42d5-8aae-7e0d9c6e1710.png" src="https://oscimg.oschina.net/oscnet/up-ef41b4d38361034b33e5fd4fade7530e1a6.png" width="700" referrerpolicy="no-referrer"></p> 
 <p>点击 Upgrade 还会有预览功能 (截图自 session 的 slide):</p> 
 <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4ee410eb-b721-4e22-a923-5fe25d844b22/e1df68e8-aa05-4f84-b644-f8ac2c1aac7b.png" height="394" src="https://oscimg.oschina.net/oscnet/up-ab4b55caaeb0546544f377b63f59a23d0fb.png" width="700" referrerpolicy="no-referrer"></p> 
 <p>不过对于 Gradle Kotlin DSL 的支持还有待补齐，例如基础的 compileSdkVersion 等废弃 DSL 的迁移也未支持:</p> 
 <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1493801f-4ee6-4b5f-912b-250328415d33/d0c18e1c-3452-4af1-98f9-f31780f97c39.png" height="438" src="https://oscimg.oschina.net/oscnet/up-55661b53cb3134ab5c149cfac4212553243.png" width="700" referrerpolicy="no-referrer"></p> 
 <p>当然，复杂的对象引用也无法帮您直接修改，例如 classpath(Deps.agp)，这已经超过该工具能做的范围。您可以把其当成类似 Java 转 Kotlin 的辅助工具，先用它快速升级和整理基础的 DSL，然后再手动对照 DSL 文档修改出错的小部分。</p> 
 <h4><strong>新的 Variant API</strong></h4> 
 <p>Variant API 是这两年 Android 与插件开发相关的最重要更新，如果之前没有针对 AGP 生态开发过协同插件的朋友可以通过下面这张图 “了解什么是 Variant”？</p> 
 <p><img alt="https://s3-us-west-2.amazonaws.com/secure.notion-static.com/391ba312-96d0-45ac-ba19-1984dce12fbf/cb35371f-4997-436f-88c9-f17aef97afcd.png" height="394" src="https://oscimg.oschina.net/oscnet/up-ffe7b6ad4b51b08ec6ad6e5327ae5216d40.png" width="700" referrerpolicy="no-referrer"></p> 
 <p>Variant API 的更新可以概括: 为了使协同插件的开发者依赖于更稳定的 API，将原来的 com.android.tools.build:gradle 包拆分成 gradle 和 gradle-api 两个包，做到接口和实现的隔离。实战角度来看我们可以关注两部分: Variant 遍历入口变更和部分自定义 Task 的简化。</p> 
 <p><strong>Variant 遍历入口变更</strong></p> 
 <p>大部分 AGP 生态的协同插件都需要注册 Variant aware 的 Task，即遍历 Variant 注册与其对应的自定义 Task，例如上面提到的 Seal 插件的 postUpdateDebugManifest postUpdateReleaseManifest。您一定看到过这样的代码 (Groovy):</p> 
 <pre><code>def android = project.extensions.android
android.applicationVariants.all &#123; variant ->
    def variantName = variant.name.capitalize()
    createTask(project, variantName)
&#125;

</code></pre> 
 <p>或者 Kotlin 的版本:</p> 
 <pre><code>val androidExtension = project.extensions.findByType(AppExtension::class.java)!!
androidExtension.applicationVariants.all &#123; variant ->
    val variantName = variant.name.capitalize()
    createTask(project, variantName)
&#125;

</code></pre> 
 <p>如果是适用于 library 的插件则需要 LibraryExtension 和 libraryVariants。</p> 
 <p>这类 API 现在改成了 gradle-api 内的新 API 调用:</p> 
 <pre><code>val androidExtension = project.extensions.getByType<ApplicationAndroidComponentsExtension>()
androidExtension.onVariants &#123; variant ->
    ...
&#125;

</code></pre> 
 <p>这里获取到的 Variant 是 com.android.build.api.variant.ApplicationVariant，Extension 则来自于 com.android.build.api.extension.ApplicationAndroidComponentsExtension。另外一个可能会用到的接口是 beforeVariants(…)，用来控制 Variant 的构建，例如全局修改一些 Variant 的属性等。从这段 Snippet 我们可能看不出来 Variant 具体的变化，但这变化背后包含了规范的 Variant 状态流转，公开的 API 等。</p> 
 <ul> 
  <li>com.android.build.api.variant.ApplicationVariant <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Ftools%2Fgradle-api%2F7.1%2Fcom%2Fandroid%2Fbuild%2Fapi%2Fvariant%2FApplicationVariant" target="_blank">https://developer.android.google.cn/reference/tools/gradle-api/7.1/com/android/build/api/variant/ApplicationVariant</a></li> 
  <li>com.android.build.api.extension.ApplicationAndroidComponentsExtension <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Ftools%2Fgradle-api%2F4.2%2Fcom%2Fandroid%2Fbuild%2Fapi%2Fextension%2FApplicationAndroidComponentsExtension" target="_blank">https://developer.android.google.cn/reference/tools/gradle-api/4.2/com/android/build/api/extension/ApplicationAndroidComponentsExtension</a></li> 
 </ul> 
 <p><strong>部分自定义 Task 的简化</strong></p> 
 <p>这类简化指 Task 插入点和 Task 参数获取 (注入) 的简化，提供这类特性的 API 也称之为 Artifact APIs。在比较经典的模式里: 对于插入点，一般我们会手动找到 Task 的前后依赖关系，使用 Gradle API 进行依赖关系重新梳理 (甚至可能要自定义一些新的生命周期锚点 Task 辅助)；对于 Task 的参数，就使出各种奇技淫巧，从已有 Task 里的参数 / 中间产物 / 私有对象等找到我们需要的数据，再注入到自定义的 Task 中。而现在 Artifact APIs 规范了一套标准操作，使得我们可以简易地和已有的数据、中间产物进行交互，实战角度来看我们可以分为两种模式:</p> 
 <p>复杂的 Transform/Append/Create 操作: 插入 Task 到特定节点和 Task 参数注入一条龙服务，一般适用于需要定义某个具体的插入点；</p> 
 <pre><code>androidComponents &#123;
    val gitVersionProvider = tasks.register<GitVersionTask>("gitVersionProvider") &#123;
        gitVersionOutputFile.set(
            File(project.buildDir, "intermediates/gitVersionProvider/output"))
        outputs.upToDateWhen &#123; false &#125;
    &#125;
    onVariants &#123; variant ->
        val manifestProducer = tasks.register<ManifestProducerTask>("$&#123;variant.name&#125;ManifestProducer") &#123;
            gitInfoFile.set(gitVersionProvider.flatMap(GitVersionTask::gitVersionOutputFile))
        &#125;
        variant.artifacts.use(manifestProducer)
            .wiredWith(ManifestProducerTask::outputManifest)
            .toCreate(SingleArtifact.MERGED_MANIFEST)
    &#125;
&#125;

</code></pre> 
 <p>纯粹的 Get: 主动获取 intermediates，一般适用于较为独立的 Task，没有严苛的插入位置要求 (但是藉由 Provider 的传递会有隐式的 Task 依赖)，没有需要替换等操作:</p> 
 <pre><code>androidComponents &#123;
    onVariants &#123; variant ->
        project.tasks.register<DisplayApksTask>("$&#123;variant.name&#125;DisplayApks") &#123;
            apkFolder.set(variant.artifacts.get(SingleArtifact.APK))
            builtArtifactsLoader.set(variant.artifacts.getBuiltArtifactsLoader())
        &#125;
    &#125;
&#125;

</code></pre> 
 <p><strong>更多</strong></p> 
 <p>从实用的角度来说，新的 Variant 接口、Extension 接口公开的 API 比之前少了，但更加规范。Artifacts 作为手动获取 Task input/output 的补充，目前的公开 API 也还比较少，希望插件开发者们在遇到合理的需要公开的 API 但目前还没有时，给 AGP team 多提点 issue :)。</p> 
 <p>另外，限于篇幅我无法在这里介绍全部的 Variant API 更新，包括新的 Provider API 引入 (Lazy Configuration)，Variant 状态流转，更多种的 Artifacts API 的使用，如何借鉴它的设计来自己动手解决那些还没有被封装、公开的接口等等。您可以从下面几份资料中获得更多的灵感:</p> 
 <ul> 
  <li> <p>From Gradle properties to AGP APIs - Android Dev Summit ’19: 讲解了 Variant API 的基石—— Provider API 及其衍生的多个子类，Variant 状态流转及其 API 的多种使用姿势等；</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DOTANozHzgPc" target="_blank">https://www.youtube.com/watch?v=OTANozHzgPc</a></p> </li> 
  <li> <p>New APIs in the Android Gradle Plugin - Android Developers Blog: 介绍了 Variant API 想法设计的由来，新 API 的使用；</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmedium.com%2Fandroiddevelopers%2Fnew-apis-in-the-android-gradle-plugin-f5325742e614" target="_blank">https://medium.com/androiddevelopers/new-apis-in-the-android-gradle-plugin-f5325742e614</a></p> </li> 
  <li> <p>android/gradle-recipes: 分别提供了 Groovy/Kotlin DSL 下 Variant API 常用的示例代码；</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fandroid%2Fgradle-recipes%2Ftree%2Fagp-7.1" target="_blank">https://github.com/android/gradle-recipes/tree/agp-7.1</a></p> </li> 
  <li> <p>Android Gradle Plugin DSL/API migration timeline: 未来三年 New DSL 和 Variant API 相关的 milestone；</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2Freleases%2Fgradle-plugin-roadmap" target="_blank">https://developer.android.com/studio/releases/gradle-plugin-roadmap</a></p> </li> 
  <li> <p>Lazy Configuration: Task 配置延迟获取，Provider 及其各种子类，Task 隐式依赖等。</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gradle.org%2Fcurrent%2Fuserguide%2Flazy_configuration.html" target="_blank">https://docs.gradle.org/current/userguide/lazy_configuration.html</a></p> </li> 
 </ul> 
 <h4><strong>ASM API</strong></h4> 
 <p>ASM API 是之前 Transform API 的替代品，旨在更低成本地提供一个 Class -> Dex 之间的插入点用以修改字节码。它没有了之前 Transform API 的灵活性，比如目前看起来它和 ASM 字节码工具是绑定的，不支持 Javassist 或者 Aspect 等。但同时，它拥有更好的性能，更低的使用成本 (指实现 transform 本身，因为 ASM 实际上是相对 Javasssist Aspect 更底层的 API，更灵活、学习成本也更高)，以及更容易适配 Gradle 的新特性。目前刚刚开始孵化，从 API Doc 来看还不推荐开发者使用它来构建一个生产环境的插件。</p> 
 <pre><code>abstract class ExamplePlugin : Plugin<Project> &#123;
    override fun apply(project: Project) &#123;
        val androidComponents = project.extensions.getByType(AndroidComponentsExtension::class.java)
        androidComponents.onVariants &#123; variant ->
            variant.transformClassesWith(ExampleClassVisitorFactory::class.java,
                                 InstrumentationScope.ALL) &#123;
                it.writeToStdout.set(true)
            &#125;
            variant.setAsmFramesComputationMode(FramesComputationMode.COPY_FRAMES)
        &#125;
    &#125;
    interface ExampleParams : InstrumentationParameters &#123;
        @get:Input
        val writeToStdout: Property<Boolean>
    &#125;
    abstract class ExampleClassVisitorFactory :
        AsmClassVisitorFactory<ExampleParams> &#123;
        override fun createClassVisitor(
            classContext: ClassContext,
            nextClassVisitor: ClassVisitor
        ): ClassVisitor &#123;
            return if (parameters.get().writeToStdout.get()) &#123;
                TraceClassVisitor(nextClassVisitor, PrintWriter(System.out))
            &#125; else &#123;
                TraceClassVisitor(nextClassVisitor, PrintWriter(File("trace_out")))
            &#125;
        &#125;
        override fun isInstrumentable(classData: ClassData): Boolean &#123;
            return classData.className.startsWith("com.example")
        &#125;
    &#125;
&#125;

</code></pre> 
 <p>上面代码用到的 API 可以参考如下说明:</p> 
 <ul> 
  <li> <p>Component#transformClassesWith(…)</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Ftools%2Fgradle-api%2F7.1%2Fcom%2Fandroid%2Fbuild%2Fapi%2Fcomponent%2FComponent.html%23transformClassesWith%28java.lang.Class%2C%2520com.android.build.api.instrumentation.InstrumentationScope%2C%2520kotlin.Function1%29" target="_blank">https://developer.android.google.cn/reference/tools/gradle-api/7.1/com/android/build/api/component/Component.html#transformClassesWith(java.lang.Class, com.android.build.api.instrumentation.InstrumentationScope, kotlin.Function1)</a></p> </li> 
  <li> <p>InstrumentationParameters</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Freference%2Ftools%2Fgradle-api%2F7.1%2Fcom%2Fandroid%2Fbuild%2Fapi%2Finstrumentation%2FInstrumentationParameters" target="_blank">https://developer.android.google.cn/reference/tools/gradle-api/7.1/com/android/build/api/instrumentation/InstrumentationParameters</a></p> </li> 
 </ul> 
 <p>对经典的 Transform 不熟悉的朋友可以看下几个知名的 Transform 库封装 (挺巧都是中国公司的开源项目):</p> 
 <ul> 
  <li> <p>ByteX (活跃)</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbytedance%2FByteX" target="_blank">https://github.com/bytedance/ByteX</a></p> </li> 
  <li> <p>Booster (活跃，部分功能使用)</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdidi%2Fbooster" target="_blank">https://github.com/didi/booster</a></p> </li> 
  <li> <p>Lancet (不活跃)</p> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feleme%2Flancet" target="_blank">https://github.com/eleme/lancet</a></p> </li> 
 </ul> 
 <h4><strong>总结</strong></h4> 
 <p>从开发者的角度来看，Android 工具团队在 AGP & AS 上更加注重 Engineering Experience 的东西了。在解决了很多历史遗留问题的同时，这次的 Session 还透露出对 AGP 周边生态建设的长远计划，希望明年可以看到这些东西真的被更多 Android 开发者接受，到时候我也一定再写一篇 22 年版的总结和前瞻。</p> 
</div>
                                        </div>
                                      
</div>
            