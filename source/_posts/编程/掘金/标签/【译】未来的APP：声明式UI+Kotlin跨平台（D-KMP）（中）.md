
---
title: '【译】未来的APP：声明式UI+Kotlin跨平台（D-KMP）（中）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5061b7e63504e72b067c86cb097d48b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Apr 2021 01:40:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5061b7e63504e72b067c86cb097d48b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>The future of apps:Declarative UIs with Kotlin MultiPlatform (D-KMP) — Part 2/3 <br>
作者：Sahil Sharma <br>
译者：不想翻身的鱼</p>
</blockquote>
<p><a href="https://danielebaroncelli.medium.com/the-future-of-apps-declarative-uis-with-kotlin-multiplatform-d-kmp-part-2-3-1bbadaf19aef" target="_blank" rel="nofollow noopener noreferrer">原文链接</a></p>
<p>基于声明式UI，Kotlin跨平台和MVI模式，分三篇文章来讲述新的D-KMP架构。</p>
<p><a href="https://juejin.cn/post/6955015172343726111" target="_blank">第一篇：D-KMP架构和声明式UI</a></p>
<p><strong>第二篇：Kotlin跨平台和MVI模式</strong></p>
<p>第三篇：D-KMP的分层和团队组织</p>
<p><code>最近更新：2021年4月8日</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5061b7e63504e72b067c86cb097d48b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">1.4版本Kotlin跨平台真的来了</h3>
<p>随着2020年8月份Kotlin 1.4的发布，Kotlin跨平台已经不再是实验性阶段，已经是Alpha了。</p>
<p>现在，其实我们已经可以开始应用这项技术到我们的产品上了，虽然后面还会有一些改变和改进，但是目前的稳定性已经很好了。</p>
<p>如果目前还有什么会阻塞我们实现这个D-KMP项目的话，它们都来自UI部分（Jetpack Compose还处在密切开发中，但是随着Navigation组件的发布已经越来越好了）而不是KMP的部分。</p>
<p>由于Kotlin在JVM社区的成功，2017年谷歌宣布将Kotlin作为Android第一支持的语言。2019年谷歌将Kotlin指定为Android开发的首选语言（取代了Java）。</p>
<p>现在Kotlin已经演进为一个跨平台的语言，拥有将代码编译到3个不同的平台：</p>
<ul>
<li><strong>JVM</strong>（Android和服务端）</li>
<li><strong>Native</strong>（iOS、macOS，Window，Linux）</li>
<li><strong>JavaScript</strong>（Web，同时提供对React封装）</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56a767ad47984430b19b84764cf8f414~tplv-k3u1fbpfcp-watermark.image" alt="1_6SJzsygHSrdvdmShHrhi3Q.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>正是因为这个，我们现在可以用Kotlin开发共享代码直接运行到各个平台上。</p>
<p>目前有两个不同首字母用到跨平台上面：</p>
<ul>
<li><strong>KMM</strong> = Kotlin Multiplatform Mobile（只是Android和iOS）</li>
<li><strong>KMP</strong> = Kotlin Multiplatform（也包括桌面端和Web）</li>
</ul>
<p>自从Kotlin 1.4开始，已经有一个固定的KMM的门户入口，专门用来说明怎么在移动端开发开始跨平台。对于不熟悉Kotlin跨平台的人来说是非常好的材料。</p>
<p>JetBrains（不仅是Kotlin的作者还是Android Studio的作者）发布了一个KMM的AS插件，这个插件可以让开发者直接在AS里面运行iOS应用。这个其实也是非常有用的。</p>
<p>Kotlin并不是唯一实现跨平台的编程语言。同时也是一个非常有趣的编程语言，同时避免了很多的模板代码。它有很多你能想象的高级特性：协程，可计算属性，属性委托，扩展函数，高阶函数，lambda等等。</p>
<p>Kotlin很快的成为了一门主流的编程语言。用Kotlin写的代码肯定会持续数十年的。作为一个长期项目来用肯定是没问题的。</p>
<h3 data-id="heading-1">KMP vs Flutter vs ReactNative</h3>
<p>当说起跨平台，2个主流的框架大家听的最多的可能是Flutter和React Native，这两个框架都可以让你进行共享代码，</p>
<p>同时你也可能听到大家不喜欢这些框架，因为它们限制了大家定制各个平台的原生UI。</p>
<p>Kotlin跨平台的到来，同时提供了这两个优点：</p>
<ul>
<li>在所有平台共享代码</li>
<li>能自由的定制各个平台的UI</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65eede6b0bbe4302a599a01c5ab7af8b~tplv-k3u1fbpfcp-watermark.image" alt="1_-pMVyErQTkoesaI97jdiLw.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在<strong>KMP</strong>里面，共享的代码是用Kotlin写的，但是最终会编译成一个原生的库：Android上是一个jar包，iOS上是一个OC的framework，web上是一个js的库。因为这样，原生的UI层在各自的平台上可以很自然和共享代码进行交互。</p>
<p>在<strong>Flutter</strong>里面，代码是用Dart来写的，最总会编译成一个原生的库，在Android 上是通过NDK，iOS上是LLVM，Web上是JS。但是与KMP不同的是，Flutter需要开启一个自己的引擎，会对包体积的影响比较大。
Flutter不使用原生的UI，它使用的是自己的声明式UI widget是通过Skia的图像引擎一个像素一个像素画出来的。这两年有很多人在用Flutter，因为Flutter提供的声明式UI方式而不是传统的Android和iOS的View。但是现在声明式的UI已经在Android和iOS的原生端开始加速支持了，这样Flutter的主要优势已经不在了。Jetpack Compose和SwiftUI 可以让你全速的构建一个顶级的APP。</p>
<p>在<strong>React Native</strong>，代码是用javascript写的，只能通过运行JS代码的C/C++桥跟native 层进行通信。UI的组件是对Android和iOS原生组件的封装，开发者对于UI的控制非常有限。RN整个的架构也证明性能不是特别好，甚至Facebook自己也慢慢的要放弃RN了。2018年AirBnB就宣布<a href="https://medium.com/airbnb-engineering/sunsetting-react-native-1868ba28e30a" target="_blank" rel="nofollow noopener noreferrer">RN的时代结束了</a>。</p>
<h3 data-id="heading-2">语言很重要：Kotlin vs Dart vs JavaScript</h3>
<p>另外一个KMP相对于Flutter和RN的优势就是编程语言。与Dart和JS相比，Kotlin是下一代顶级语言，它具有可靠性和简洁的特点。在Kotlin很轻松的就能写出高质量的代码，因为她具备了非常智能的特性，比如协程，可计算属性，高阶函数等等。</p>
<h3 data-id="heading-3">D-KMP架构下平台特有的代码只有15%</h3>
<p>此时可能有人会认为<code>“好，我知道KMP很牛。我知道声明式UI最终会来到Android和iOS平台。但是这种方式我仍然还要给各自平台画UI，这也会造成很多重复工作！”</code></p>
<p>答案是“NO！并没有很多重复的工作”</p>
<p>在新的原生声明式UI平台下，UI层是非常轻的。在我们目前用D-KMP架构构建的APP里，从整个代码量来看UI层大约值占了15%的代码量。并且UI是所有的平台特有的代码，其他的全是KMP的共享代码。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84c54f2cdc4a4b3d95584183611d4a28~tplv-k3u1fbpfcp-watermark.image" alt="1_V4g54su84IaK84QdlHn7OA.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这额外的15%的代码是完全值得的，因为它可以让我们给各个平台自由定制，而不是像Flutter和RN有很多的限制。Android和iOS是两个不同的平台有很多的不同。一个顶级的APP需要保持各个平台真实的UI/UX模式的。</p>
<p>从我们的经验来看，一旦我们在Android端写了Jetpack Compose的UI，就可以直接到iOS上SwiftUI实现出来。代码的结构几乎是一样的。对于一个简单的APP，要不了一天时间。</p>
<p>在两个框架还有一些相同的组件，虽然名字不同。例如，你想要把多个文本水平放置在一个布局内，Android端Jetpack Compose是<code>Row</code>，iOS端SwiftUI是<code>HStack</code>，文本的组件在两个框架里面都是<code>Text</code>，只是语法有点不一样。一旦你熟悉了这些小小的不同点，完成一端的声明式UI后，你可以快速复制到另外一个上面。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a39da3cbcc834a27a7687a71e44fe2a3~tplv-k3u1fbpfcp-watermark.image" alt="1_aBwcUfVscWvZzCaboUualw.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有的数据都来自于页面的状态，由KMP共享的代码提供。在各自平台的声明式UI，只需要关心view，其实是一个很轻的工作。</p>
<p>重要的是声明式UI<strong>不需要处理数据</strong>。啥也不用管直接展示就好。这也会大量减少平台相关的bug。</p>
<p>一旦共享的代码不担心bug，在各自平台上所有的事情就会推进的很顺利。这也是为什么不需要过于在意在各自平台上开发一套UI。</p>
<h3 data-id="heading-4">MVI模式：D-KMP架构的第三个核心</h3>
<p>我们一开始就提到，MVI模式（代表Model-View-Intent）是这个结构的第三个核心部分。背后主要的概念是<strong>单项数据流</strong>，这也是它跟之前的MVC，MVP，MVVM不同的地方。MVI是响应式模式，让APP的行为更加的一致性和可预测性，你可以认为它是MVVM的演进。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a98689fe6ab41f293830ca48077671a~tplv-k3u1fbpfcp-watermark.image" alt="1_YsJtXWJi0_xD2Nv3zZWsUQ.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在MVI模式下，View的状态只有唯一的可信数据源。任何时候状态都是有可变的数据组成，并且只能被Model修改。所有的事情都是单向的。用户出发了一个事件/intent。Model做出相应并执行一些操作之后改变状态。然后新的状态被反映到View上面。</p>
<p>在我们的D-KMP架构下，我们在KMP的共享代码里面实现MVI的Model（可见下面的图）这个可以让我们<strong>在共享代码里面进行状态管理</strong>，这个非常重要！</p>
<p>也正是因为这样，我们平台特有的代码只是声明式UI的那一层，这一层是很轻的并且是无状态的，因为它完全把状态的管理委托给了KMP的ViewModel。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66cb2ee953ca495280a1c37ee0b3a317~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>让我们看一些代码：开始我们的第三篇文章吧！</p></div>  
</div>
            