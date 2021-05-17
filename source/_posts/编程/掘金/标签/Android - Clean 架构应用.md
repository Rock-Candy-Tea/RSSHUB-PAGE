
---
title: 'Android - Clean 架构应用'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/933ab4b0491b44a4a7e569abe4455653~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 02:57:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/933ab4b0491b44a4a7e569abe4455653~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">参考</h3>
<p><a href="https://www.jianshu.com/p/66e749e19f0d" target="_blank" rel="nofollow noopener noreferrer">Clean架构探讨</a></p>
<p><a href="https://www.cnblogs.com/wanpengcoder/p/3479322.html" target="_blank" rel="nofollow noopener noreferrer">The Clean Architecture--一篇很不错的关于架构的文章</a></p>
<p><a href="https://fernandocejas.com/blog/engineering/2014-09-03-architecting-android-the-clean-way/" target="_blank" rel="nofollow noopener noreferrer">Architecting Android...The clean way?</a></p>
<h3 data-id="heading-1">架构的一般特征</h3>
<p>在 <code>Uncle Bob</code> 的文章中总结了架构所应具有的特征：</p>
<ul>
<li><code>框架独立</code>：架构不依赖于一些满载功能的软件库。这可以让你像使用工具一样使用这样的框架，而不是把系统塞到他们有限的约束之中。</li>
<li><code>可测试性</code>：业务规则可以在没有UI，数据库，Web服务器，或者其他外部元素的情况下完成测试。</li>
<li><code>UI独立</code>：在不改变系统其余部分的情况下完成UI的简易修改。如，Web UI可以在不改变业务规则的基础之上替换成控制台UI。</li>
<li><code>数据库独立</code>：业务规则不绑定的数据库中，这样你可以更换Oracle or SQL Server, for Mongo, BigTable, CouchDB，或者其他数据库。</li>
<li><code>外部机制独立</code>：事实上业务规则根本不知道外层的事情。</li>
</ul>
<p>基于以上特点 <code>Bob</code> 提出了 <code>Clean 架构</code> 思想。</p>
<p><code>Clean</code> 的核心思想在于面向对象编程，通过分层和依赖倒置原则对项目解耦。</p>
<h3 data-id="heading-2">Clean 架构分层</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/933ab4b0491b44a4a7e569abe4455653~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>Clean</code> 架构大致可以将一个项目分为四层，如上图中洋葱图所示：</p>
<ul>
<li><code>Entities</code>：实体</li>
<li><code>Use Cases</code>：用例</li>
<li><code>Interface Adapters</code>：接口适配器</li>
<li><code>Frameworks and Drivers</code>：框架和驱动</li>
</ul>
<h4 data-id="heading-3">entity 实体</h4>
<p>实体是可以在 <code>企业范围</code> 内多个不同应用间公用的核心对象。实体的具体形式是什么其实并不重要，它可以是包含有方法的对象或者一系列的数据结构和函数。但其内包含的一定是最通用和最高等级的规则。实体层外的任何变动都不能影响到实体。</p>
<h4 data-id="heading-4">Use Cases 用例</h4>
<p>用例包含了 <code>应用范围</code> 内的特定业务规则。用例层整合并且实现了应用中需要的所有用例。这些用例协调着来往于实体之间的数据流，并且指引实体使用它们企业范围内的业务规则实现用例的目标。</p>
<p>同样用例层的代码也不应受到其外层变动的影响。比如数据库框架、UI框架或其他通用框架的替换都不应影响用例层代码。</p>
<p>只有在应用的业务逻辑发生变动时才能对用例层的相关代码进行调整。</p>
<h4 data-id="heading-5">Interface Adapters 接口适配器</h4>
<p>本层是通过一系列适配器，将用例层和实体层方便使用的数据格式转换成最外层数据库和Web等框架方便使用的数据格式。</p>
<p>本层相当于分割内层与外层的分界线。本层以里为具体的业务逻辑以及里层所操作的数据结构，本层以外是项目所使用的库、框架等以及外层所操作的数据。这样就将业务逻辑与UI、技术的使用分割开来，再通过适配器的作用使内层和外层互相连接在一起。</p>
<p>接口适配器的存在让项目可以里层外层同时开发。</p>
<h4 data-id="heading-6">Frameworks and Drivers 框架和驱动</h4>
<p>这一层是项目的最外层，一般包括项目中所使用到的框架和工具，如数据库、Web框架等。最外层所用到的所有框架和工具要做到可以用最小的代价随时替换。</p>
<h4 data-id="heading-7">跨层调用</h4>
<p>按照 <code>Clean</code> 架构思想内层是不应该持有外层对象的。外层访问内层可以直接通过内层对象进行访问，那内层如何访问外层呢？这可以通过 <code>依赖倒置原则</code> 来解决。依赖倒置简单理解就是依赖于抽象而不依赖于具体。可以将外层某个逻辑抽象出一个接口，内层通过接口调用外层接口的具体实现以达到访问外层的目的。</p>
<h3 data-id="heading-8">Clean 架构在 Android 项目中的应用</h3>
<p>介绍完 <code>Clean</code> 架构之后，我们来看如何将 <code>Clean</code> 架构的思想运用到 <code>Android</code> 项目中。
我主要是通过下面两个项目来学习 <code>Clean</code> 架构思想是如何应用于 <code>Android</code> 项目的。</p>
<ul>
<li><a href="https://github.com/android10/Android-CleanArchitecture" target="_blank" rel="nofollow noopener noreferrer">Android-CleanArchitecture</a></li>
<li><a href="https://github.com/android/architecture-samples/tree/todo-mvp-clean" target="_blank" rel="nofollow noopener noreferrer">architecture-samples</a></li>
</ul>
<p>上面两个项目虽然都是 <code>MVP - Clean</code> 两种架构结合的开发方式。但其侧重点不同：</p>
<ul>
<li><code>Android-CleanArchitecture</code>：此项目是 <code>Clean</code> 架构思想在 <code>Android</code> 项目中的完整体现。非常适合 <code>Android</code> 开发者学习 <code>Clean</code> 架构思想。</li>
<li><code>architecture-samples</code>：此项目展示了如何使用不同架构开发 <code>Android</code> 项目。其 <code>todo-mvp-clean</code> 分支更多的是使用 <code>Clean</code> 架构的用例层思想来对 <code>P</code> 层复杂的业务逻辑进行简化。</li>
</ul>
<p>本篇主要是为了学习 <code>Clean</code> 思想那我们主要来介绍 <code>Android-CleanArchitecture</code> 项目。但是强烈建议也学习 <code>architecture-samples</code> 项目。</p>
<h4 data-id="heading-9">Android 项目分层</h4>
<p><code>Android-CleanArchitecture</code> 项目作者将 <code>MVP</code> 架构按 <code>Clean</code> 思想绘制成洋葱图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e0544399d7b4d8893119ed9113a3751~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到这张图你可能会有疑惑 <code>UI</code> 和 <code>Presenters</code> 层都理解，那 <code>M</code> 层去哪了。其实就是本项目中的 <code>UserModel</code>，是 <code>UI</code> 和 <code>Presenters</code> 层操作的数据模型。</p>
<h4 data-id="heading-10">项目模块和层级间对应关系</h4>
<p>作者将项目划分为了三个模块，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa0ff9d0a8b04c2ba1e50c86f74b9536~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>三个模块各自功能以及分别对应于洋葱图中的哪层，如下：</p>
<p><code>Presentation Layer</code>，本模块对应于 <code>UI</code>、<code>Presenters</code> 两层。负责处理与视图相关的所有逻辑。刚才也介绍过了 <code>M</code> 是<code>UI</code>、<code>Presenters</code> 两层处理的数据结构，所以其实 <code>MVP</code> 都存在于本模块的。但功能和以往有所不同，<code>V</code> 依然表示是视图，<code>P</code> 不再处理业务逻辑而是通过适配器连接表示层和用例层进行数据交换，<code>M</code> 就是单纯的数据结构，对应于项目中的 <code>UserModel</code>。</p>
<p><code>Domain Layer</code>，本模块对应于 <code>Use Cases</code> 层。负责实现项目中所有的业务逻辑用例。并定义了 <code>UserRepository</code> 接口供用例调用。</p>
<p><code>Data Layer</code>，本模块对应于 <code>Entities</code>、<code>UI</code> 两层。这里可能就有些难以理解了，<code>Entities</code> 层好理解，这里有 <code>UI</code> 层什么事。请注意区分 <code>Android</code> 项目的模块依赖和 <code>Clean</code> 架构层级依赖之间的不同。我们再来回顾一下 <code>Clean</code> 架构思想，最外层除了 <code>UI</code> 还有什么，是不是还有数据库、工具库等。本模块中使用 <code>Repository</code> 模式处理实体数据，包括线上数据、本地数据的处理，其中线上数据可能会用到 <code>Retrofit</code>、<code>Okhttp</code> 等具体实现，本地数据可能会用到 <code>SQLite</code>、<code>Room</code> 等，它们是不是都应该是在 <code>Clean</code> 架构的最外层。</p>
<p>这也可以理解为什么作者会把 <code>UserRepository</code> 接口定义在 <code>Domain Layer</code> 中了。</p>
<h4 data-id="heading-11">数据传递</h4>
<p>介绍完项目模块的划分以及如此划分的原因，我们最后再来看项目中数据是如何传递的。如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9367cd288a6f4878bf029c1925d02c7b~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到项目中的数据是通过观察者模式传递的。</p>
<p>结合项目本身可以看到作者为每个模块都定义了一个数据结构（<code>UserEntity、User、UserModel</code>）并有对应的转换器 <code>Mapper</code>。这样做的好处就是各个模块之间可以最大程度的解耦。但是对于一些非常简单的业务项目来说每个模块都定义一个数据模型实在是没有必要的，太繁琐了。事实上对于一些小项目来说项目中某业务中仅存一个数据结构已经是常态了。</p>
<p>个人理解如果将视图开发和业务开发分离的话仅需要 <code>XxxModel</code>、<code>XxxEntity</code> 两种数据结构就可以了即解耦又减少了些繁琐。在 <a href="https://www.jianshu.com/p/66e749e19f0d" target="_blank" rel="nofollow noopener noreferrer">Clean架构探讨</a> 中作者给出了不同的意见。还是那句话 <code>只有最合适的架构没有最好的架构</code>。</p>
<p>感觉有用的话点赞哟 <code>^_^</code>。</p></div>  
</div>
            