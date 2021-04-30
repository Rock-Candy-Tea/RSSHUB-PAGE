
---
title: '【译】未来的APP：声明式UI+Kotlin跨平台（D-KMP）（上）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5061b7e63504e72b067c86cb097d48b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Apr 2021 00:50:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5061b7e63504e72b067c86cb097d48b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>The future of apps:Declarative UIs with Kotlin MultiPlatform (D-KMP) — Part 1/3 <br>
作者：Sahil Sharma <br>
译者：不想翻身的鱼</p>
</blockquote>
<p><a href="https://danielebaroncelli.medium.com/the-future-of-apps-declarative-uis-with-kotlin-multiplatform-d-kmp-part-1-3-c0e1530a5343" target="_blank" rel="nofollow noopener noreferrer">原文链接</a></p>
<p>基于声明式UI，Kotlin跨平台和MVI模式，分三篇文章来讲述新的D-KMP架构。</p>
<p><strong>第一篇：D-KMP架构和声明式UI</strong></p>
<p><a href="https://juejin.cn/post/6956511926457696293" target="_blank">第二篇：Kotlin跨平台和MVI模式</a></p>
<p>第三篇：D-KMP的分层和团队组织</p>
<p><code>最近更新：2021年4月8日</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5061b7e63504e72b067c86cb097d48b~tplv-k3u1fbpfcp-watermark.image" alt="1_MIRW_odYriJChVdQbqjd2Q.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99dba4d926154d28aaaf1e8d1140408d~tplv-k3u1fbpfcp-watermark.image" alt="1_YXeYR0SiDXOYtHbY70j-hA.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2020年不仅是疫情肆虐的一年，也是APP开发的过去和未来的分水岭。</p>
<p>2021 APP的未来已经开始，那就是声明式UI和跨平台，它们将永远改变APP的架构模式和实现。去创建一个多平台的有85%的共享代码的原生的UI的APP将会变得很正常。开发的生产力将大幅度提高，同时也能提高APP的质量。</p>
<p>本文将介绍主要的概念，以及它们是怎么优雅的组合到一起的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aecebf454e0242148deb25189e671db1~tplv-k3u1fbpfcp-watermark.image" alt="1_9EOoAhmiabR4S4Xqwxxb7g.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1eb6a11f02db43f186788f69a3551adb~tplv-k3u1fbpfcp-watermark.image" alt="1_P2ow0SLwIK0GQF0w5ogTEg.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">过去</h3>
<p>这里的过去说的是APP一直以来的开发方式：大部分公司都是各自平台开发应用（Android，iOS，Web），在客户端侧没有做代码共享。</p>
<p>为了控制在每个平台侧编写重复的带，大部分应用倾向于“轻客户端”，将大部分的业务逻辑和数据处理放在唯一可以共享的服务端。</p>
<p>这种方式，服务端会变得“面向UI”。架构会被设计成这样：大部分点击都会触发一个API的调用，接口会返回下一个页面要展示的详细信息，这样一个非常有限的客户端逻辑。</p>
<p>其他的客户端逻辑都需要在每个平台维护一套相同的代码，通常会避免这种情况，除非这些逻辑能带来比较有意义的客户体验。</p>
<p>对于客户端侧的共享代码，这些年已经有一些公司在尝试一些方法，但是对于大部分来说都是一次失败的历史，最终还是会把代码还原到只有原生或者平台特性的开发。被大家熟知的案例比如<code>DropBox</code>（通过共享C++代码），<code>AirBnB</code>（通过RN共享）。换句话说，还没有一个合适的技术可以让这些公司可以实现一个长期安全的投入到共享代码。</p>
<h3 data-id="heading-1">未来</h3>
<p>2020年，我们经历了两个重要范例增长，两个几乎是并行的：声明式UI和Kotlin跨平台。这会带来前所未有的机会，会让跨平台和客户端侧的代码共享变成APP开发的更倾向的选择。</p>
<p>声明式UI非常适合跨平台的架构，因为它们是无状态的而且可以做到跟业务逻辑完全解耦。通过把声明式UI和Kotlin跨平台组合到一起，我们可以安全的搭建一个有大量客户端侧共享代码的APP（高达85%），并且在各自原生平台有很高的性能。同时我们还能拥有各自平台原生的UI。</p>
<p>应用现在可以做到“富客户端”，因为客户端侧的逻辑成本不像以前那么高了，因为不再需要每个平台维护同一套逻辑了。应用会变得非常的灵活并且带来很多会给用户体验带来改善，减少用户在点完一个东西需要等待场景。</p>
<p>服务端可以变得完全是“UI无关的”并且集中精力在提供通用数据，删除所有的冗余逻辑，因为数据处理和格式化在客户端层就可以完成。这个同时也能很大程度提高数据吞吐量。</p>
<p>让我们一个个来看一下。首先让我们定义一下这个即将到来的APP开发新纪元的几个核心概念。</p>
<h3 data-id="heading-2">未来应用的3个核心概念</h3>
<ul>
<li><strong>声明式UI</strong>（Android的Jetpack Compose，iOS的Swift UI）</li>
<li><strong>KMP</strong>（Kotlin 跨平台）</li>
<li><strong>MVI模式</strong>（Model-View-Intent）</li>
</ul>
<p>我们称其为D-KMP架构，表示声明式UI和Kotlin跨平台。MVI模式是为了让两者配合起来更完美。</p>
<h3 data-id="heading-3">D-KMP架构</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66cb2ee953ca495280a1c37ee0b3a317~tplv-k3u1fbpfcp-watermark.image" alt="1_u0-oVjYhj5KK7J8naWf8rg.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有一点很重套必需要说明下，现在展示的D-KMP架构是针对全新的项目。</p>
<p>我们讨论的不是往一个现有项目里面逐渐的引入声明式UI和Kotlin 跨平台。</p>
<p>我们的目标是<strong>简洁的</strong>，<strong>健壮的</strong>，<strong>不会过时的</strong>的架构，而不会向过去妥协并且是基于创新的技术和范例来构建的。</p>
<p>还有一点需要强调的是D-KMP不是一个lib库，而是一个架构，完全依赖官方的framework。</p>
<p>让我们详细的了解下这个架构三个核心的细节，首先看下声明式UI。</p>
<h3 data-id="heading-4">声明式UI已经开始在Android和iOS上发展了</h3>
<p>差不多经过10多年，我们开始经历移动框架的非常重要的革命。Android和iOS都开始了各自新的UI工具集，并且都是声明式的，受到React和Flutter它俩的影响。它们将完全取代现有的各自系统定义视图的方式。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e20b083b78594191a520ea4269d9ead0~tplv-k3u1fbpfcp-watermark.image" alt="1_8FqQC_aYHbR8Rx3VMBFhWg.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Google在2019年的Google I/O 大会上发布了<strong>Jetpack Compose</strong>。2020年8月进入Alpha阶段，2021年春季进入beta阶段，预计2021年底能发布1.0版本。</p>
<p><strong>Jetpack Compose会支持Android 5以及以上的版本</strong>（target API 21）。这就意味着所有新的Jetpack Compose的API都是向后兼容的，而且不需要新的Android版本。这是因为在低版本上Jetpack Compose是直接在画布上进行绘制额。</p>
<p>Apple在2019年的WWDC上个发布了Swift UI，随着iOS 13一起发布。今年随着iOS 14的发布已经做了很多改进。
跟Jetpack Compose不同的是，Swift UI的更新是跟iOS系统绑定在一起的。新的Swift UIAPI不会向后兼容。但是考虑到所有支持iOS 13的设备现在也支持iOS 14（与往常不同，苹果今年没有弃用任何设备），可以很安全的在target 是iOS14的应用使用Swift UI。</p>
<h3 data-id="heading-5">为什么是声明式UI</h3>
<p>Jetpack Compose和Swift UI都是声明式UI的框架，它们只是用来表示不同状态下UI应该怎么样展示，而不是直接的管理状态。声明式UI变得越来越流行，也正是因为React.js和Flutter这来你给个框架，它俩让人们看到了跟无状态的组件交互是一件多么简单的事情。也正是它俩的成功，让Android和iOS加入到了声明式UI的世界。</p>
<p>使用Jetpack Compose你可以忘记Android笨重的视图系统和可怕的<code>Fragments</code>。使用Swift UI你可以忘记VC这个UI Kit和不怎么灵活的StoryBoard。<strong>这是一个全新的开始。这就是未来!</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cee0834dfa0437297b00e2636576d82~tplv-k3u1fbpfcp-watermark.image" alt="1_mpauYGRLOdtXnVMLMGKBvA.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2944ef820b44125af9a2be83be8a7cb~tplv-k3u1fbpfcp-watermark.image" alt="1_TrmNwY-zbSN1gpqgP6cGlw.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>声明式UI可以让UI布局和ViewModel进行一个彻底的分离，因为不再需要其他层额外的代码（使用findViewById和@IBOutlet）去把两者联系起来。关于这个主题，Google的Leland Richardson写了一篇非常有意思的文章（这篇文章我正好翻译过，这里贴上我翻译文章<a href="https://juejin.cn/post/6940133772880773128" target="_blank">Jetpack Compose底层实现原理</a>）。</p>
<p>Jetpack Compose和Swift UI非常的相似。有一些琐碎的语法的（Jetpack Compose用的是Kotlin，Swift UI用的是Swift）以及导航模式不同，但是背后带理念都是一样的。尤其是数据是传递到这些无状态UI框架的方式完全是一样的。也正是因为这一点，ViewModel跟平台无关才显得有意义。后面我们会进一步聊下这方面具体的细节。</p>
<h3 data-id="heading-6">Web端的声明式UI</h3>
<p>Web端最有名的声明式UI就是React.js（by Facebook），也是真正把声明式UI带向成功的框架。这是一个工业级改变的框架，如果没有React.js的成功，我们现在也可能在Android和iOS上用不了声明式UI。</p>
<p>Kotlin提供了对React.js非常方便的封装，我们可以使用Kotlin/React作为Web的声明式UI。它可以以插件的形式引入到我们的D-KMP架构，就跟Android上的Jetpack Compose和iOS上的Swift UI一样。</p>
<p>在Kotlin/React里面你可以引用所有已有的React.js的组件，可以用到Kotlin语言的相对于JS的有点。你也可以完全用Kotlin创建自定义的组件。可以到<a href="https://kotlinlang.org/docs/js-get-started.html" target="_blank" rel="nofollow noopener noreferrer">Kotlin/React</a>文档了解详细的信息。</p>
<p>除了Kotlin/React以外，更有意思的可能就是<strong>Compose for Web</strong>，也就是Jetpack Compose的Web版本，目前JetBrains（Kotlin的创建者）正在开发。如果说用Kotlin/React 来实现UI还需要额外15%的工作量（相对于85%的KMP的共享代码），Compose for Web会使这块工作量少很多，因为它跟Android的Jetpack Compose非常像。因此我们非常期待它发布的那一天。</p>
<h3 data-id="heading-7">桌面端的声明式UI</h3>
<p>在我们等待web版本的同时，JetBrains已经发布了桌面版的Compose，可以用来开发Windows，macOS和Linux的桌面应用。</p>
<p>关于桌面端，值的注意的是Swift UI已经支持macOS了。用Swift UI编写的UI在iOS，macOS，tvOS和watchOS 6之间是无缝适配的。我们也期望Jetpack Compose早日实现多平台的无缝适配（Android，桌面和Web）。</p>
<p>可以想象一下，在不久的将来只要你会Jetpack Compose和Swift UI就能开发处各个平台非常优秀的应用。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46a413a466ce42eaabcdf36691e44455~tplv-k3u1fbpfcp-watermark.image" alt="1_qM_9WtxGBR18Lqvve63TSA.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">为什么不是一套UI框架可以适配所有平台呢？</h3>
<p>你可能在想会不会只有这么一套声明式UI框架可以适配所有的平台。</p>
<p>换句话说，Jetpack Compose会不会最终适配所有苹果的系统（iOS，macOS，tvOS，watchOS），或者说Swift UI最终会不会适配非苹果的设备？</p>
<p>就目前而言，如果这个会发生的话，那也不会是苹果或者谷歌来做，可能是社区或者第三方来做的。我们已经看到Jetpack Compose已经被引入到桌面端和Web端，不是谷歌而是JetBrains。</p>
<p>谷歌和苹果还是会集中精力到各自的系统上面。其实这样对UI的未来是非常健康的。这样就一直有两套独立强大的工具集相互竞争，不断创新。</p>
<p>现在让我们再看下<strong>Kotlin 跨平台：</strong>
开始第二篇文章。</p></div>  
</div>
            