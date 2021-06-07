
---
title: '【iOS】App 架构 - （一）介绍'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfe8b0af387942b2b090d6922f12ed73~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 06:11:55 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfe8b0af387942b2b090d6922f12ed73~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>文章来自对 <a href="https://objccn.io/" target="_blank" rel="nofollow noopener noreferrer">objccn.io/</a>  相关书籍的整理笔记。“感谢 objc.io 及其撰稿作者们无私地将他们的知识分享给全世界”。</p>
</blockquote>
<h1 data-id="heading-0">前言</h1>
<h2 data-id="heading-1">App 设计模式</h2>
<p>将一组被重复使用的设计规则称为设计模式。将会展示如何使用五种最主要的 App 设计模式来完整实现一个 App。所挑选的模式中，有的已经经过广泛的验证，有的还处于实验阶段，分别是:</p>
<ul>
<li>Model-View-Controller (MVC)</li>
<li>Model-View-ViewModel+Coordinator (MVVM-C)</li>
<li>Model-View-Controller+ViewState (MVC+VS)</li>
<li>ModelAdapter-ViewBinder (MAVB)</li>
<li>Elm 架构 (The Elm Architecture, TEA)</li>
</ul>
<h2 data-id="heading-2">架构技术和经验教训</h2>
<p>展示每一种实现方式之后，会讨论这种模式在解决问题时的优势，以及使用类似策略在其他任意模式中解决问题的方式。研究这些技术在它们各自的模式中的使用方式之后，还会继续讨论它们的核心思想，看看这些思想是如何跨越不同的模式来解决问题的。</p>
<h2 data-id="heading-3">关于录音 App</h2>
<p>会展示同一个录音 app 的五种不同实现。所有实现的完整源码都公开在该链接中。
<a href="https://github.com/objcio/app-architecture" target="_blank" rel="nofollow noopener noreferrer">github.com/objcio/app-…</a></p>
<h1 data-id="heading-4">应用架构</h1>
<p>App 架构是软件设计的一个分支，关心如何设计一个 App 的结构。关注两个方面：如何将 App 分解为不同的接口和概念层次部件，以及这些部件之间和自身的不同操作中所使用的控制流和数据流路径。</p>
<p>通常使用简单的框图来解释 App 的架构。比如，Apple 的 MVC 模式可以通过 model、 view 和 controller 三层结构来描述。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfe8b0af387942b2b090d6922f12ed73~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面框图中的模块展示了这个模式中不同名字的三个层次。在一个 MVC 项目中，绝大部分的代码都会落到其中某个层上。箭头表示了这些层进行连接的方式。但是，这种简单的框图几乎无法解释在实践中模式的操作方式。这是因为在实际的 App 架构中，部件的构建有非常多的可能性。</p>
<h1 data-id="heading-5">Model 和 View</h1>
<p>在最高的层级上，App 架构就是一套分类，App 中不同的部件会被归纳到某个类型中去。将这些不同的种类叫做层次：一个层次指的是，遵循一些基本规则并负责特定功能的接口和其他代码的集合。</p>
<p>Model 层和 View 层是这些分类中最为常⻅的两个。</p>
<p><strong>Model 层</strong>是 App 的内容，它不依赖于 (像 UIKit 那样的) 任何 App 框架。也就是说，程序员对 Model 层有完全的控制。Model 层通常包括 Model 对象 (在录音 App 中的例子是文件夹和录音对象) 和协调对象 (比如 App 例子中的负责在磁盘上存储数据的 Store 类型)。被存储在磁盘上的那部分 Model 我们称之为文档 Model (Documentation Model)。</p>
<p><strong>View 层</strong>是依赖于 App 框架的部分，它使 Model 层可⻅，并允许用户进行交互，从而将 model 层转变为一个 App。当创建 iOS 应用时，view 层几乎总是直接使用 UIKit。不过，有些架构中会使用 UIKit 的封装来实现不同的 view 层。另外，对一些其他的像是游戏这样的自定义应用，view 层可以不是 UIKit 或者 AppKit，它可能是 SceneKit 或者 OpenGL 的某种封装。</p>
<p>有时候，选择使用结构体或者枚举来表示 model 或者 view 的实例，而不使用类的对象。在实践中，类型之间的区别非常重要，但是在 model 层中谈到对象、结构体和枚举时，会将三者统一地称为 model 对象。类似地会把 view 层的实例叫做 view 对象，实际上它们也可能是对象、结构体或者枚举。</p>
<p>View 对象通常会构成一个单一的 view 层级，在这个层级中，所有的 view 对象通过树结构的方式连接起来。在树的根部是整个屏幕，屏幕中存在若干窗口，接下来在树的分支和叶子上是更多的小 view。类似地，view controller 也通常会形成 view controller 层级。不过，model 对象却不需要有明确的层级关系，在程序中它们可以是互不关联的独立 model。</p>
<p>当提到 view 时，通常指的是像一个按钮或者一个文本 label 这样的单一 view 对象。提到 model 时，通常指的也是像一个 Recording 实例或者 Folder 实例这样的单个 model 对象。在该话题的大多数文献中，“model” 在不同上下文中指的可能是不同的事情。</p>
<h2 data-id="heading-6">为什么 Model 和 View 的分类会被认为是基础</h2>
<p>就算不区分 model 层和 view 层，写出一个 app 也是可以的。不过通常情况下，model 层的缺失，会让程序的行为缺乏对于清晰规则的依据，这会使得代码难以维护。</p>
<p>定义一个 model 层的最重要的理由是它为程序提供一个表述事实的单一来源，逻辑清晰，行为正确。这样一来，程序便不会被应用框架中的实现细节所支配。</p>
<p>应用框架提供了构建 app 所需要的基础设施。根据目标平台，使用 UIKit，AppKit 或者 WatchKit 来作为应用框架。如果 model 层能做到和应用框架分离，就可以完全在 App 的范围之外使用它。可以很容易地在另外的测试套件中运行它，或者用一个完全不同的应用框架重写新的 view 层。这个 model 层将能够用于 Android，macOS 或者 Windows 版本的 App 中。</p>
<h1 data-id="heading-7">App 的本质是反馈回路</h1>
<p>View 层和 model 层需要交流。所以两者之间需要存在连接。假设 view 层和 model 层是被清晰地分开，且不存在无法解耦的联结的话，两者之间的通讯就需要一些形式的翻译:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1cf4900977147ae80c94468069461b0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从根本上说，用户界面是一个同时负责展示和输入功能的反馈设备，这导致的结果就是一个反馈回路。每个 app 设计模式所面临的挑战是如何处理这张图表中箭头所包含的交流，依赖和变换。</p>
<p>在 model 层和 view 层之间不同的路径拥有不同的名字。用户发起的事件会导致 view 的响应，把由此引起的代码路径称为 <strong>view action</strong>。当一个 view action 被送到 model 层时，它会被转变为 <strong>model action</strong> (或者说，让 model 对象执行一个 action 或者进行更新的命令)。这种命令也被叫做一个消息 (特别在当 model 是被 reducer 改变时会这么称呼它)。将 view action 转变为 model action 的操作，以及路径上的其他逻辑被叫做<strong>交互逻辑</strong>。</p>
<blockquote>
<p>reducer 这个名字来自于函数式编程的 reduce 操作，它指的是对一系列的值进行操作，把它们按照一定逻辑 “减少” (合并) 到一个值中。一般来说，架构中的 reducer 所负责的事情是，将一系列未来到来的变化 (或者说消息)，与当前的状态进 行 “合并”，并推导出新的状态。</p>
</blockquote>
<p>一个或者多个 model 对象上状态的改变叫做 <strong>model 变更</strong>。Model 的变更通常会触发一个
model 通知，比如说从 model 层发出一个可观测的通知，它描述 model 层中什么内容发生了改变。当 view 依赖于 model 数据时，通知会触发一个 view 变更，来更改 view 层中的内容。这些通知可以以多种形式存在：Foundation 中的 Notification、代理、回调，或者是其他机制都是可以的。将 model 通知和数据转变为 view 更改的操作，以及路径上的其他逻辑被叫做<strong>表现逻辑</strong>。</p>
<p>根据 app 模式的不同，有些状态可能是在文档 model 之外进行维护的，这样一来，更新这些状态的行为就不会追随文档 model 的路径。在很多模式中的导航状态就是这种行为的一个常⻅例子，在 view 层级中的某个部分 (或者按照 Cocoa Storyboard 中使用的术语，将它称为 scene) 可能会被换出或者换入层级中。</p>
<p>在 app 中非文档 model 的状态被叫做 <strong>view state</strong>。在 Cocoa 里，大部分 view 对象都管理着自己的 view state，controller 对象则管理剩余的 view state。在 Cocoa view state 的框图中，通常会有加在反馈回路上的捷径，或者单个层自身进行循环。在有一些架构中，view state 不属于 controller 层，而是属于 model 层的部分 (不过根据定义，view controller 并不是文 档 model 的一部分)。</p>
<p>当所有的状态都在 model 层中被维护，而且所有的变更都通过完整的反馈回路路径进行传递时，就将它称为单向数据流。当任意的 view 对象或者中间层对象只能够通过 model 发出的通知来进行创建和更新 (换句话说，view 或者中间层不能通过捷径来更新自身或者其他的 view) 时，这个模式通常就是单向的。</p>
<h1 data-id="heading-8">架构技术</h1>
<p>Apple 平台的标准 Cocoa 框架提供了一些架构工具。Notification 将值从单一源广播给若干个收听者。键值观察 (KVO) 可以将某个对象上属性的改变报告给另一个对象。然而，Cocoa 中的架构工具十分有限，将会使用到一些额外的框架。</p>
<p>使用到的第三方技术中包含了响应式编程。响应式编程也是一种用来交流变更的工具，不过和通知或者 KVO 不同的是，它专注于在源和目标之间进行变形，让逻辑可以在部件之间传输信息的同时得以表达。</p>
<p>可以使用像是响应式编程或者 KVO 这样的技术创建属性绑定。绑定接受一个源和一个目标，无论何时，只要源发生了变化，目标也将被更新。这和手动进行观察在语法上有着不同，不再需要写观察的逻辑，而只需要指定源和目标，接下来框架将会为我们处理其余部分的工作。</p>
<p>macOS 上的 Cocoa 包含有 Cocoa 绑定技术，它是一种双向绑定，所有的可观察对象同时也是观察者，在一个方向上建立绑定连接，会在反方向也创建一个连接。不论是 RxCocoa，还是 CwlViews，都不是双向绑定的。本次所有关于绑定的讨论都只涉及到单向绑定。</p>
<h1 data-id="heading-9">App 任务</h1>
<p>要让程序正常工作，view 必须依赖于 model 数据来生成和存在，配置 view，让它可以对
model 进行更改，并且能在 model 更新时也得到更新。 所以，需要决定在 app 中如何执行下列任务:</p>
<ol>
<li>构建 — 谁负责构建 model 和 view，以及将两者连接起来?</li>
<li>更新 model — 如何处理 view action?</li>
<li>改变 view — 如何将 model 的数据应用到 view 上去?</li>
<li>view state — 如何处理导航和其他一些 model state 以外的状态?</li>
<li>测试 — 为了达到一定程度的测试覆盖，要采取怎样的测试策略?</li>
</ol>
<p>对于上面五个问题的回答，是构成 app 设计模式的基础要件。会逐一研究这些设计模式。</p></div>  
</div>
            