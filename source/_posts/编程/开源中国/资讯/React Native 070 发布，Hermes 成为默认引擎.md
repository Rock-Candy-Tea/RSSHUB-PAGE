
---
title: 'React Native 0.70 发布，Hermes 成为默认引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9759'
author: 开源中国
comments: false
date: Tue, 06 Sep 2022 07:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9759'
---

<div>   
<div class="content">
                                                                                            <p>React Native 0.70 版本正式发布，这个版本有几项改进，比如 Codegen 的新的统一配置、Hermes 作为默认引擎、对 Android 构建的完整 CMake 支持，还有对新架构文档的更新。</p> 
<p>具体更新内容如下：</p> 
<h3>New Architecture 的新文档</h3> 
<p>在过去的几个月里，Meta 一直在努力为文档中的 New Architecture 部分增加更多的内容。在新的部分，你可以找到迁移指南、例子和教程，让你尽快掌握。</p> 
<p>同时你还可以找到新的文档，深入了解为什么要有一个 New Architecture 和它的各个部分。这能帮助你更好地理解新 API 背后的原理。</p> 
<h3>Hermes 作为默认引擎</h3> 
<p>React Native 0.70 是第一个默认启用 Hermes 的版本。</p> 
<p>这是 Hermes 团队和 React Native 团队合作的结果，Meta 将努力改进和微调 Hermes，使其性能更强，并提供社区高度要求的功能。</p> 
<h3>Codegen 的新的统一配置</h3> 
<p>在 0.70 版本中，引入了一个统一的方式来定义 iOS 和 Android 的 Codegen 规格。以前你必须把 Android 的配置放在一个单独的 build.gradle 文件中。</p> 
<p>现在，你可以直接在 package.json 中定义它：</p> 
<pre><code class="language-json">  "codegenConfig": &#123;
    "name": "CustomAnimationView",
    "type": "components",
    "jsSrcsDir": "./src",
    "android": &#123;
      "javaPackageName": "com.custom.animation"
    &#125;
  &#125;

</code></pre> 
<p>这一改进为库维护者在将其代码库迁移到 New Architecture 时提供了更一致的体验。</p> 
<h3>New Architecture 库的 Android Autolinking</h3> 
<p>在 0.70 版本中，New Architecture 的用户能够自动链接库，而不需要在他们的 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2FAndroid.mk" target="_blank">Android.mk</a> 或 CMake 文件上做任何额外的配置。</p> 
<p>自动链接（Autolinking）React Native 开发体验的一个重要部分。它允许你用 <code>yarn add</code> 命令包含外部库，而无需处理 CocoaPods 或 Gradle 设置。</p> 
<p>虽然自动链接功能在 iOS 上的 New Architecture 库运行良好，但在 Android 上却并非如此。在 0.70 版本中缩小了这一差距，现在你可以继续在你的项目中加入带有 <code>yarn add</code> 的库：它们会在任何架构上被正确链接。</p> 
<h3>对 Android 构建的全面 CMake 支持</h3> 
<p>从 0.70 开始，用户现在可以使用 CMake 来配置他们的 Native 构建了。虽然不希望应用程序的用户直接编写 C++ 代码，但你仍然需要一个本地编译的入口。</p> 
<p>从现在开始，你可以使用 <code>CMakeLists.txt</code> 文件而不是 <code>Android.mk</code> 文件来处理你项目中任何与 Android/Native 相关的东西。</p> 
<h3>依赖升级</h3> 
<ul> 
 <li>将 RN CLI 升级到 9.0.0 版本</li> 
 <li>将 Android Gradle Plugin 升级到 7.2.1</li> 
 <li>将 Gradle 升级到 7.5.1</li> 
 <li>将 RCT-Folly 升级到 2021-07-22</li> 
 <li>将 Metro 升级到 0.72</li> 
 <li>将 SoLoader 升级到 0.10.4</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactnative.dev%2Fblog%2F2022%2F09%2F05%2Fversion-070" target="_blank">https://reactnative.dev/blog/2022/09/05/version-070</a></p>
                                        </div>
                                      
</div>
            