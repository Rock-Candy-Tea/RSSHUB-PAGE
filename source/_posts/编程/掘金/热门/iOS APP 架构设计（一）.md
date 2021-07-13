
---
title: 'iOS APP 架构设计（一）'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22b15ce01bb64e3dbc37709c20586202~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 22:41:38 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22b15ce01bb64e3dbc37709c20586202~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">iOS APP 架构设计</h2>
<p>一，APP架构概述</p>
<p>1. 应用架构</p>
<p>2.Model 和 View</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2F3.App" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=http%3A//3.App" ref="nofollow noopener noreferrer">3</a>. App 的本质是反馈回路</p>
<p>4.架构技术</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2F5.App" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=http%3A//5.App" ref="nofollow noopener noreferrer">5.App</a> 任务</p>
<p>6.iOS 架构的5中模式：</p>
<p>二，APP设计常用的5种模式概览</p>
<p>1. Model-View-Controller</p>
<p>2. Model-View-ViewModel+协调器</p>
<p>3. Model-View-Controller+ViewState</p>
<p>4. Model 适配器-View 绑定器 (MAVB)</p>
<p>5. Elm 架构 (TEA)</p>
<p>三，其他APP架构模式</p>
<p>1. Model-View-Presenter</p>
<p>2. VIPER，Riblets，和其他 “Clean” 架构</p>
<p>3. 基于组件的架构 (React Native)</p>
<h2 data-id="heading-1">一，APP架构概述</h2>
<p><strong>1. 应用架构</strong></p>
<p>App 架构是软件设计的一个分支，它关心如何设计一个 app 的结构。具体来说，它关注于两个 方面:如何将 app 分解为不同的接口和概念层次部件，以及这些部件之间和自身的不同操作中 所使用的控制流和数据流路径。</p>
<p>我们通常使用简单的框图来解释 app 的架构。比如，Apple 的 MVC 模式可以通过 model、 view 和 controller 三层结构来描述。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22b15ce01bb64e3dbc37709c20586202~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面框图中的模块展示了这个模式中不同名字的三个层次。在一个 MVC 项目中，绝大部分的代 码都会落到其中某个层上。箭头表示了这些层进行连接的方式。</p>
<p>但是，这种简单的框图几乎无法解释在实践中模式的操作方式。这是因为在实际的 app 架构中， 部件的构建有非常多的可能性。事件流在层中穿梭的方式是什么?部件之间是否应该在编译期 间或者运行时持有对方?要怎么读取和修改不同部件中的数据?以及状态的变更应该以哪条路 径在 app 中穿行?</p>
<p><strong>2.Model 和 View</strong></p>
<p>在最高的层级上，app 架构其实就是一套分类，app 中不同的部件会被归纳到某个类型中去。 在本书中，我们将这些不同的种类叫做层次:一个层次指的是，遵循一些基本规则并负责特定 功能的接口和其他代码的集合。</p>
<p>Model 层和 View 层是这些分类中最为常⻅的两个。</p>
<p>Model 层是 app 的内容，它不依赖于 (像 UIKit 那样的) 任何 app 框架。也就是说，程序员对 model 层有完全的控制。Model 层通常包括 model 对象 (在录音 app 中的例子是文件夹和录音对象) 和协调对象 (比如我们的 app 例子中的负责在磁盘上存储数据的 Store 类型)。被存储在 磁盘上的那部分 model 我们称之为文档 model (documentation model)。</p>
<p>View 层是依赖于 app 框架的部分，它使 model 层可⻅，并允许用戶进行交互，从而将 model 层转变为一个 app。当创建 iOS 应用时，view 层几乎总是直接使用 UIKit。不过，我们也会看 到在有些架构中，会使用 UIKit 的封装来实现不同的 view 层。另外，对一些其他的像是游戏这 样的自定义应用，view 层可以不是 UIKit 或者 AppKit，它可能是 SceneKit 或者 OpenGL 的某 种封装。</p>
<p>有时候，我们选择使用结构体或者枚举来表示 model 或者 view 的实例，而不使用类的对象。 在实践中，类型之间的区别非常重要，但是当我们在 model 层中谈到对象、结构体和枚举时， 我们会将三者统一地称为 model 对象。类似地，我们也会把 view 层的实例叫做 view 对象，实 际上它们也可能是对象、结构体或者枚举。</p>
<p>View 对象通常会构成一个单一的 view 层级，在这个层级中，所有的 view 对象通过树结构的方 式连接起来。在树的根部是整个屏幕，屏幕中存在若干窗口，接下来在树的分支和叶子上是更 多的小 view。类似地，view controller 也通常会形成 view controller 层级。不过，model 对 象却不需要有明确的层级关系，在程序中它们可以是互不关联的独立 model。</p>
<p>当我们提到 view 时，通常指的是像一个按钮或者一个文本 label 这样的单一 view 对象。当我 们提到 model 时，我们通常指的也是像一个 Recording 实例或者 Folder 实例这样的单个 model 对象。在该话题的大多数文献中，“model” 在不同上下文中指的可能是不同的事情。它 可以指代一个 model 层，model 层中的具体的若干对象，文档 model，或者是 model 层中不 关联的文档。虽然可能会显得啰嗦，我们还是会尝试在本书中尽量明确地区分这些不同含义。</p>
<p><strong>为什么 Model 和 View 的分类会被认为是基础中的基础</strong></p>
<p>当然啦，就算不区分 model 层和 view 层，写出一个 app 也是绝对可能的。比如说，在一个简 单的对话框中，通常就没有独立的 model 数据。在用戶点击 OK 按钮的时候，我们可以直接从 用戶界面元素中读取状态。不过通常情况下，model 层的缺失，会让程序的行为缺乏对于清晰 规则的依据，这会使得代码难以维护。</p>
<p>定义一个 model 层的最重要的理由是，它为我们的程序提供一个表述事实的单一来源，这会让 逻辑清晰，行为正确。这样一来，我们的程序便不会被应用框架中的实现细节所支配。</p>
<p>应用框架为我们提供了构建 app 所需要的基础设施。在本书中，我们使用 Cocoa - 或者更精确 说，根据目标平台，使用 UIKit，AppKit 或者 WatchKit - 来作为应用框架。</p>
<p>如果 model 层能做到和应用框架分离，我们就可以完全在 app 的范围之外使用它。我们可以很 容易地在另外的测试套件中运行它，或者用一个完全不同的应用框架重写新的 view 层。这个 model 层将能够用于 Android，macOS 或者 Windows 版本的 app 中。</p>
<h3 data-id="heading-2">3.App 的本质是反馈回路</h3>
<p>View 层和 model 层需要交流。所以，两者之间需要存在连接。假设 view 层和 model 层是被清<br>
晰地分开，而且不存在无法解耦的联结的话，两者之间的通讯就需要一些形式的翻译:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16c64db20cd54d76b76f056a2772770d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从根本上说，用戶界面是一个同时负责展示和输入功能的反馈设备，所以毫无疑问，这导致的 结果就是一个反馈回路。每个 app 设计模式所面临的挑战是如何处理这张图表中箭头所包含的 交流，依赖和变换。</p>
<p>在 model 层和 view 层之间不同的路径拥有不同的名字。用戶发起的事件会导致 view 的响应， 我们把由此引起的代码路径称为 view action，像是点击按钮或者选中 table view 中的某一行 就属于 view action。当一个 view action 被送到 model 层时，它会被转变为 model action (或 者说，让 model 对象执行一个 action 或者进行更新的命令)。这种命令也被叫做一个消息 (特别 在当 model 是被 reducer 改变时，我们会这么称呼它)。将 view action 转变为 model action 的操作，以及路径上的其他逻辑被叫做交互逻辑。</p>
<p>一个或者多个 model 对象上状态的改变叫做 model 变更。Model 的变更通常会触发一个</p>
<p>model 通知，比如说从 model 层发出一个可观测的通知，它描述 model 层中什么内容发生了 改变。当 view 依赖于 model 数据时，通知会触发一个 view 变更，来更改 view 层中的内容。 这些通知可以以多种形式存在:Foundation 中的 Noti?cation，代理，回调，或者是其他机制， 都是可以的。将 model 通知和数据转变为 view 更改的操作，以及路径上的其他逻辑被叫做表 现逻辑。</p>
<p>根据 app 模式的不同，有些状态可能是在文档 model 之外进行维护的，这样一来，更新这些状 态的行为就不会追随文档 model 的路径。在很多模式中的导航状态就这种行为的一个常⻅例 子，在 view 层级中的某个部分 (或者按照 Cocoa Storyboard 中使用的术语，将它称为 scene) 可能会被换出或者换入层级中。</p>
<p>在 app 中非文档 model 的状态被叫做 view state。在 Cocoa 里，大部分 view 对象都管理着它 们自己的 view state，controller 对象则管理剩余的 view state。在 Cocoa view state 的框图 中，通常会有加在反馈回路上的捷径，或者单个层自身进行循环。在有一些架构中，view state 不属于 controller 层，而是属于 model 层的部分 (不过，根据定义，view controller 并不是文 档 model 的一部分)。</p>
<p>当所有的状态都在 model 层中被维护，而且所有的变更都通过完整的反馈回路路径进行传递 时，我们就将它称为单向数据流。当任意的 view 对象或者中间层对象只能够通过 model 发出 的通知来进行创建和更新 (换句话说，view 或者中间层不能通过捷径来更新自身或者其他的 view) 时，这个模式通常就是单向的。</p>
<p><strong>4.架构技术</strong></p>
<p>Apple 平台的标准 Cocoa 框架提供了一些架构工具。Noti?cation 将值从单一源广播给若干个 收听者。键值观察 (KVO) 可以将某个对象上属性的改变报告给另一个对象。然而，Cocoa 中的 架构工具十分有限，我们将会使用到一些额外的框架。</p>
<p>本书中使用到的第三方技术中包含了响应式编程。响应式编程也是一种用来交流变更的工具， 不过和通知或者 KVO 不同的是，它专注于在源和目标之间进行变形，让逻辑可以在部件之间传 输信息的同时得以表达。</p>
<p>我们可以使用像是响应式编程或者 KVO 这样的技术创建属性绑定。绑定接受一个源和一个目 标，无论何时，只要源发生了变化，目标也将被更新。这和手动进行观察在语法上有着不同， 我们不再需要写观察的逻辑，而只需要指定源和目标，接下来框架将会为我们处理其余部分的 工作。</p>
<p>macOS 上的 Cocoa 包含有 Cocoa 绑定技术，它是一种双向绑定，所有的可观察对象同时也是 观察者，在一个方向上建立绑定连接，会在反方向也创建一个连接。不论是 (在MVVM-C 的章</p>
<p>节中用到的) RxCocoa，还是 (MAVB 章节 中用到的) CwlViews，都不是双向绑定的。所以，在</p>
<p>本书中，所有关于绑定的讨论都只涉及到单向绑定。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2F5.App" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=http%3A//5.App" ref="nofollow noopener noreferrer"><strong>5.App</strong></a> <strong>任务</strong></p>
<p>要让程序正常工作，view 必须依赖于 model 数据来生成和存在，我们配置 view，让它可以对</p>
<p>model 进行更改，并且能在 model 更新时也得到更新。 所以，我们需要决定在 app 中如何执行下列任务:</p>
<p>1.构建—谁负责构建model和view，以及将两者连接起来?</p>
<p>2.更新model—如何处理viewaction?</p>
<p>3.改变view—如何将model的数据应用到view上去?</p>
<p>4.viewstate—如何处理导航和其他一些modelstate以外的状态?</p>
<p>5.测试—为了达到一定程度的测试覆盖，要采取怎样的测试策略?</p>
<ol start="6">
<li></li>
</ol>
<p>对于上面五个问题的回答，是构成 app 设计模式的基础要件。在本书中，我们会逐一研究这些 设计模式。</p>
<h3 data-id="heading-3">6.IOS 架构的5中模式：</h3>
<p><strong>IOS 架构的5中模式：</strong></p>
<ul>
<li>
<p>标准的CocoaModel-View-Controller(MVC)是Apple在示例项目中所采用的设计模 式。它是 Cocoa app 中最为常⻅的架构，同时也是在 Cocoa 中讨论架构时所采用的基 准线。</p>
</li>
<li>
<p>Model-View-ViewModel+协调器(MVVM-C)是MVC的变种，它拥有单独的 “view-model” (视图模型) 和一个用来管理 view controller 的协调器。MVVM 使用数据 绑定 (通常会和响应式编程一起使用) 来建立 view-model 层和 view 层之间的连接。</p>
</li>
<li>
<p>Model-View-Controller+ViewState(MVC+VS)这种模式将所有的viewstate集中到 一个地方，而不是让它们散落在 view 和 view controller 中。这和 model 层所遵循的规 则相同。</p>
</li>
<li>
<p>Model适配器-View绑定器(ModelAdapter-ViewBinder,MAVB)是本书的一位作者所 使用的实验性质的架构。MAVB 专注于构建声明式的 view，并且抛弃 controller，采用 绑定的方式来在 model 和 view 之间进行通讯。</p>
</li>
<li>
<p>Elm架构(TEA)与MVC或者MVVM这样的常⻅架构完全背道而驰。它使用虚拟view 层级来构建 view，并使用 reducer 来在 model 和 view 之间进行交互。</p>
</li>
</ul>
<h2 data-id="heading-4">二，APP设计常用的5种模式概览</h2>
<p><strong>1. Model-View-Controller</strong></p>
<p>在 Cocoa MVC 中，一小部分 controller 对象负责处理 model 或者 view 层范畴之外的所有任 务。</p>
<p>这意味着，controller 层接收所有的 view action，处理所有的交互逻辑，发送所有的 model action，接收所有的 model 通知，对所有用来展示的数据进行准备，最后再将它们应用到 view 的变更上去。如果我们去看一下介绍一章中的 app 反馈回路的图，会发现在 model 和 view 之</p>
<p>间的箭头上，几乎每个标签都是 controller。而且要知道，在这幅图中，构建和导航任务并没有 标注出来，它们也会由 controller 来处理。</p>
<p>下面是 MVC 模式的框图，它展示了一个 MVC app 的主要通讯路径:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c40450efd238431eaf5d194756c4f866~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图中的虚线部分代表运行时的引用，view 层和 model 层都不会直接在代码中引用 controller。 实线部分代表编译期间的引用，controller 实例知道自己所连接的 view 和 model 对象的接口。</p>
<p>如果我们在这个图标外部描上边界的话，就得到了一个 MVC 版本的 app 反馈回路。注意在图 表中其他的路径并不参与整个反馈回路的路径 (也就是 view 层和 controller 层上那些指向自身 的箭头)。</p>
<p><strong>1.构建</strong></p>
<p>App 对象负责创建最顶层的 view controller，这个 view controller 将加载 view，并且知道应 该从 model 中获取哪些数据，然后把它们显示出来。Controller 要么显式地创建和持有 model 层，要么通过一个延迟创建的 model 单例来获取 model。在多文档配置中，model 层由更低层 的像是 UIDocument 或 NSDocument 所拥有。那些和 view 相关的单个 model 对象，通常会 被 controller 所引用并缓存下来。</p>
<p><strong>2.更改 Model</strong></p>
<p>在 MVC 中，controller 主要通过 target/action 机制和 (由 storyboard 或者代码进行设置的) delegate 来接收 view 事件。Controller 知道自己所连接的 view，但是 view 在编译期间却没有 关于 controller 接口的信息。当一个 view 事件到达时，controller 有能力改变自身的内部状态， 更改 model，或者直接改变 view 层级。</p>
<p><strong>3.更改 View</strong></p>
<p>在我们所理解的 MVC 中，当一个更改 model 的 view action 发生时，controller 不应该直接去 操作 view 层级。正确的做法是，controller 去订阅 model 通知，并且在当通知到达时再更改 view 层级。这样一来，数据流就可以单向进行:view action 被转变为 model 变更，然后 model 发送通知，这个通知最后被转为 view 变更。</p>
<p><strong>4.View State</strong></p>
<p>View state 可以按需要被 store 在 view 或者 controller 的属性中。相对于影响 model 的 view action，那些只影响 view 或 controller 状态的 action 则不需要通过 model 进行传递。对于 view state 的存储，可以结合使用 storyboard 和 UIStateRestoring 来进行实现，storyboard 负责记录活跃的 controller 层级，而 UIStateRestoring 负责从 controller 和 view 中读取数据。</p>
<p><strong>5.测试</strong></p>
<p>在 MVC 中，view controller 与 app 的其他部件紧密相连。边界的缺失使得为 controller 编写 单元测试和接口测试十分困难，集成测试是余下的为数不多的可行测试手段之一。在集成测试 中，我们构建相连接的 view、model 和 controller 层，然后操作 model 或者 view，来测试是 否能得到我们想要的结果。</p>
<p>集成测试的书写非常复杂，而且它涵盖的范围太广了。它不仅仅测试逻辑，也测试部件是如何 连接的 (虽然在一些情况下和 UI 测试的⻆度并不相同)。不过，在 MVC 中通过集成测试，通常 达到 80% 左右的测试覆盖率是有可能的。</p>
<ul>
<li>MVC 的重要性</li>
</ul>
<p>因为 Apple 在所有的实例项目中都使用了这种模式，加上 Cocoa 本身就是针对这种模式设计 的，所以 Cocoa MVC 成为了 iOS，macOS，tvOS 和 watchOS 上官方认证的 app 架构模式。</p>
<ul>
<li>历史</li>
</ul>
<p>MVC 这个名字第一次被提出是在 1979 年，Trygve Reenskaug 用它来描述 Smalltalk-76 上已 经存在的 “template pattern” 应用。在他和 Adele Goldberg 讨论了术语方面的问题后，MVC 的名字被确定下来 (之前的名字包括 Model-View-Editor 和 Model-View-Tool-Editor 等)。</p>
<p>在原本的构想中，view 是直接 “附着” 在 model 层上，并观察所有 model 变化的。Controller 存在的目的仅仅是捕捉用戶事件，并把它们转发给 model。这两个特性都是 Smalltalk 运行方 式的产物，它们并不是为了现代的 app 框架所设计的，所以今天这种 MVC 的原始构想已经几 乎绝迹了。</p>
<p>Cocoa 中的 MVC 实现可以追溯到大约 1997 年的 NeXTSTEP 4 的年代。在那之前，所有现在 controller 所担当的⻆色，通常都由一个 (像是 NSWindow 那样的) 高层 view 类来扮演。之后， 从原始的 Smalltalk 的 MVC 实现中所发展出的理念是分离展示部分，也就是 view 层和 model 层应该被完全隔离开，这带来了一个强烈的需求，那就是要引入一个支持对象来辅助两者之间 的通讯。NeXTSTEP 中 controller 的概念和 Taligent 稍早的 Model-View-Presenter 中的 presenter (展示器) 很相似。不过，在现在 Model-View-Presenter 这个名字通常被用来指代那 些通过协议从 controller 中将 view 抽象出来的类似 MVC 的模式。</p>
<p><strong>2. Model-View-ViewModel+协调器</strong></p>
<p>MVVM 和 MVC 类似，也是通过基于场景 (scene，view 层级中可能会在导航发生改变时切入或者换出的子树) 进行的架构。相较于 MVC，MVVM 在每个场景中使用 view-model 来描述场景中的表现逻辑和交互逻辑。</p>
<p>View-model 在编译期间不包含对 view 或者 controller 的引用。它暴露出一系列属性，用来描 述每个 view 在显示时应有的值。把一系列变换运用到底层的 model 对象后，就能得到这些最 终可以直接设置到 view 上的值。实际将这些值设置到 view 上的工作，则由预先建立的绑定来 完成，绑定会保证当这些显示值发生变化时，把它设定到对应的 view 上去。响应式编程是用来 表达这类声明和变换关系的很好的工具，所以它天生就适合 (虽说不是严格必要) 被用来处理</p>
<p>view-model。在很多时候，整个 view-model 都可以用响应式编程绑定的方式，以声明式的形 式进行表达。</p>
<p>在理论上，因为 view-model 不包含对 view 层的引用，所以它是独立于 app 框架的，这让对于 view-model 的测试也可以独立于 app 框架。</p>
<p>由于 view-model 是和场景耦合的，我们还需要一个能够在场景间切换时提供逻辑的对象。在 MVVM-C 中，这个对象叫做协调器 (coordinator)。协调器持有对 model 层的引用，并且了解 view controller 树的结构，这样，它能够为每个场景的 view-model 提供所需要的 model 对象。</p>
<p>和 MVC 不同，MVVM-C 中的 view controller 从来都不会直接引用其他的 view controller (所 以，也不会引用其他的 view-model)。View controller 通过 delegate 的机制，将 view action 的信息告诉协调器。协调器据此显示新的 view controller 并设置它们的 model 数据。换句话 说，view controller 的层级是由协调器进行管理的，而不是由 view controller 来决定的。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa79a64c620f42748aaee425d721d860~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果我们忽略掉协调器，那么这张图表就很像 MVC 了，只不过在 view controller 和 model 之 间加入了一个阶段。MVVM 将之前在 view controller 中的大部分工作转移到了 view-model 中，但是要注意，view-model 并不会在编译时拥有对 view controller 的引用。</p>
<p>View-model 可以从 view controller 和 view 中独立出来，也可以被单独测试。同样，view controller 也不再拥有内部的 view state，这些状态也被移动到了 view-model 中。在 MVC 中 view controller 的双重⻆色 (既作为 view 层级的一部分，又负责协调 view 和 model 之间的交 互)，减少到了单一⻆色 (view controller 仅仅只是 view 层级的一部分)。</p>
<p>协调器模式的加入进一步减少了 view controller 所负责的部分:现在它不需要关心如何展示其 他的 view controller 了。因此，这实际上是以添加了一层 controller 接口为代价，降低了 view controller 之间的耦合。</p>
<p><strong>1.构建</strong></p>
<p>对于 model 的创建和 MVC 中的保持不变，通常它是一个顶层 controller 的职责。不过，单独</p>
<p>的 model 对象现在属于 view-model，而不属于 view controller。</p>
<p>初始的 view 层级的创建和 MVC 中的一样，通过 storyboard 或者代码来完成。和 MVC 不同的 是，view controller 不再直接为每个 view 获取和准备数据，它会把这项工作交给 view-model。 View controller 在创建的时候会一并创建 view-model，并且将每个 view 绑定到 view-model 所暴露出的相应属性上去。</p>
<p><strong>2.更改 Model</strong></p>
<p>在 MVVM 中，view controller 接收 view 事件的方式和 MVC 中一样 (在 view 和 view controller 之间建立连接的方式也相同)。不过，当一个 view 事件到达时，view controller 不会 去改变自身的内部状态、view state、或者是 model。相对地，它立即调用 view-model 上的方 法，再由 view-model 改变内部状态或者 model。</p>
<p><strong>3.更改 View</strong></p>
<p>和 MVC 不同，view controller 不监听 model。View-model 将负责观察 model，并将 model 的通知转变为 view controller 可以理解的形式。View controller 订阅 view-model 的变更，这 通常通过一个响应式编程框架来完成，但也可以使用任意其他的观察机制。当一个 view-model 事件来到时，由 view controller 去更改 view 层级。</p>
<p>为了实现单向数据流，view-model 总是应该将变更 model 的 view action 发送给 model，并 且仅仅在 model 变化实际发生之后再通知相关的观察者。</p>
<p><strong>4.View State</strong></p>
<p>View state 要么存在于 view 自身之中，要么存在于 view-model 里。和 MVC 不同，view controller 中不存在任何 view state。View-model 中的 view state 的变更，会被 controller 观 察到，不过 controller 无法区分 model 的通知和 view state 变更的通知。当使用协调器时， view controller 层级将由协调器进行管理。</p>
<p><strong>5.测试</strong></p>
<p>因为 view-model 和 view 层与 controller 层是解耦合的，所以可以使用接口测试来测试 view-model，而不需要像 MVC 里那样使用集成测试。接口测试要比集成测试简单得多，因为 不需要为它们建立完整的组件层次结构。</p>
<p>为了让接口测试尽可能覆盖更多的范围，view controller 应当尽可能简单，但是那些没有被移 出 view controller 的部分仍然需要单独进行测试。在我们的实现中，这部分内容包括与协调器 的交互，以及初始时负责创建工作的代码。</p>
<ul>
<li>MVVM 的重要性</li>
</ul>
<p>MVVM 是 iOS 上最流行的 MVC 的非直接变形的 app 设计模式。换言之，它和 MVC 相比，并没有非常大的不同;两者都是围绕 view controller 场景构建的，而且所使用的机制也大都相同。</p>
<p>最大的区别可能在于 view-model 中对响应式编程的使用了，它被用来描述一系列的转换和依 赖关系。通过使用响应式编程来清晰地描述 model 对象与显示值之间的关系，为我们从总体上 理解应用中的依赖关系提供了重要的指导。</p>
<p>iOS 中的协调器是一种很有用的模式，因为管理 view controller 层级是一件非常重要的事情。 协调器在本质上并没有和 MVVM 绑定，它也能被使用在 MVC 或者其他模式上。</p>
<ul>
<li>历史</li>
</ul>
<p>MVVM 由 Ken Cooper 和 Ted Peters 提出，他们当时在微软工作，负责后来变成 Windows Presentation Foundation (WPF) 的项目，<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2F%2525E8%2525BF%252599%2525E6%252598%2525AF%2525E5%2525BE%2525AE%2525E8%2525BD%2525AF.NET" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=http%3A//%25E8%25BF%2599%25E6%2598%25AF%25E5%25BE%25AE%25E8%25BD%25AF.NET" ref="nofollow noopener noreferrer">这是微软.NET</a> 的 app 框架，并于 2005 年正式发布。</p>
<p>WPF 使用一种基于 XML，被称为 XAML 的描述性语言来描述 view 所绑定的某个 view-model 上的属性。在 Cocoa 中，没有 XAML，我们必须使用像是 RxSwift 这样的框架和一些 (通常存 在于 controller 中的) 代码来完成 view-model 和 view 的绑定。</p>
<p>MVVM 和我们在 MVC 历史中提到的 MVP 模式非常类似. 不过，在 Cooper 和 Peters 的论述中， MVVM 中 view 和 view-model 的绑定需要明确的框架支持，但 presenter 是通过传统的手动 方式来传递变化。</p>
<p>iOS 中的协调器则是最近才 (重新) 流行起来的，Soroush Khanlou 在 2015 年时在他的网站上描述了这个想法。协调器基于 app controller 这样的更古老的模式，而它们在 Cocoa 和其他平台上已经存在了有数十年之久。</p>
<p><strong>3. Model-View-Controller+ViewState</strong></p>
<p>MVC+VS 是为标准的 MVC 带来单向数据流方式的一种尝试。在标准的 Cocoa MVC 中，view state 可以由两到三种不同的路径进行操作，MVC+VS 则试图避免这点，让 view state 的处理 更加易于管理。在 MVC+VS 中，我们明确地在一个新的 model 对象中，对所有的 view state 进行定义和表达，我们把这个对象叫做 view state model。</p>
<p>在 MVC+VS 中，我们不会忽略任何一次导航变更，列表选择，文本框编辑，开关变更，model 展示或者滚动位置变更 (或者其他任意的 view state 变化)。我们将这些变更发送给 view state model。每个 view controller 负责监听 view state model，这样变更的通讯会非常直接。在表现或者交互逻辑部分，我们不从 view 中去读取 view state ，而是从 view state model 中去获 取它们:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e9df6a959424b04a5b38a2762cc8f78~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>结果所得到的图表和 MVC 类似，但 controller 的内部反馈回路的部分 (被用来更新 view state) 有所不同，现在它和 model 的回路类似，形成了一个独立的 view state 回路。</p>
<p><strong>1.构建</strong></p>
<p>和传统的 MVC 一样，将文档 model 数据应用到 view 上的工作依然是 view controller 的责任， view controller 还会使用和订阅 view state 。因为 view state model 和文档 model 都需要观 察，所以相比于典型的 MVC 来说，我们需要多得多的通过通知进行观察的函数。</p>
<p><strong>2.更改 Model</strong></p>
<p>当 view action 发生时，view controller 去变更文档 model (这和 MVC 保持不变) 或者变更 model state。我们不会去直接改变 view 层级，所有的 view 变更都要通过文档 model 和 view state model 的通知来进行。</p>
<p><strong>3.更改 View</strong></p>
<p>Controller 同时对文档 model 和 view state model 进行观察，并且只在变更发生的时候更新 view 层级。</p>
<p>View State</p>
<p>View State 被明确地从 view controller 中提取出来。处理的方法和 model 是一样的: controller 观察 view state model，并且对应地更改 view 层级。</p>
<p><strong>4.测试</strong></p>
<p>在 MVC+VS 中，我们使用和 MVC 里类似的集成测试，但是测试本身会非常不同。所有的测试 都从一个空的根 view controller 开始，然后通过设定文档 model 和 view state model，这个 根 view controller 可以构建出整个 view 层级和 view controller 层级。MVC 的集成测试中最困 难的部分 (设定所有的部件) 在 MVC+VS 中可以被自动完成。要测试另一个 view state 时，我 们可以重新设置全局 view state，所有的 view controller 都会调整自身。</p>
<p>一旦 view 层级被构建，我们可以编写两种测试。第一种测试负责检查 view 层级是不是按照我 们的期望被建立起来，第二种测试检查 view action 有没有正确地改变 view state。</p>
<ul>
<li><strong>MVC+VS 的重要性</strong></li>
</ul>
<p>MVC+VS 主要是用来对 view state 进行教学的工具。</p>
<p>在一个非标准 MVC 的 app 中，添加一个 view state model，并且在每个 view controller 中 (在已经对 model 进行观察的基础上) 观察这些 view state model，提供了不少优点:任意的状 态恢复 (这种恢复不依赖于 storyboard 或者 UIStateRestoration)，完整的用戶界面日志，以及 为了调试目的，在不同的 view state 间进行跳转的能力。</p>
<ul>
<li><strong>历史</strong></li>
</ul>
<p>这种特定的体系是 Matt Gallagher 在 2017 年开发的教学工具，它被用来展示单向数据流和用 戶界面的时间旅行等概念。这个模式的目标是，在传统的 Cocoa MVC app 上通过最小的改动， 实现对 view 的状态在每个 action 发生时都可以进行快照。</p>
<p><strong>4. Model 适配器-View 绑定器 (MAVB)</strong></p>
<p>MAVB 是一种以绑定为中心的实验模式。在这个模式中，有三个重要的概念:view 绑定器， model 适配器，以及绑定。</p>
<p>View 绑定器是 view (或者 view controller) 的封装类:它构建 view，并且为它暴露出一个绑定 列表。一些绑定为 view 提供数据 (比如，一个标签的文本)，另一些从 view 中发出事件 (比如， 按钮点击或者导航变更)。</p>
<p>虽然 view 绑定器可以含有动态绑定，但是 view 绑定器本身是不可变的。这让 MAVB 也成为了 一种声明式的模式:你声明 view 绑定器和它们的 action，而不是随着时间去改变 view 绑定器。</p>
<p>Model 适配器是可变状态的封装，它是由所谓的 reducer 进行实现的。Model 适配器提供了一 个 (用于发送事件的) 输入绑定，以及一个 (用于接收更新的) 输出绑定。</p>
<p>在 MAVB 中，你不会去直接创建 view;相对地，你只会去创建 view 绑定器。同样地，你也从 来不会去处理 model 适配器以外的可变状态。在 view 绑定器和 model 适配器之间的 (两个方 向上的) 变换，是通过 (使用标准的响应式编程技术) 来对绑定进行变形而完成的。</p>
<p>MAVB 移除了对 controller 层的需求。创建逻辑通过 view 绑定器来表达，变换逻辑通过绑定来 表达，而状态变更则通过 model 适配器来表达。结果得到的框图如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/629f0fa354944ac49beea465e5bc380b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.构建</strong></p>
<p>Model 适配器 (用来封装主 model ) 和 view state 适配器 (封装顶层的 view state) 通常是在</p>
<p>main.swift 文件中进行创建的，这早于任何的 view。</p>
<p>View 绑定器使用普通的函数进行构建，这些函数接受必要的 model 适配器作为参数。实际的</p>
<p>Cocoa view 则由框架负责进行创建。 2. 更改 Model</p>
<p>当一个 view (或者 view controller) 可以发出 action 时，对应的 view 绑定允许我们指定一个 action 绑定。在这里，数据从 view 流向 action 绑定的输出端。典型情况下，输出端会与一个 model 适配器相连接，view 事件会通过绑定进行变形，成为 model 适配器可以理解的一条消 息。这条消息随后被 model 适配器的 reducer 使用，并改变状态。</p>
<p><strong>2.更改 View</strong></p>
<p>当 model 适配器的状态发生改变时，它会通过输出信号产生通知。在 view 绑定器中，我们可 以将 model 适配器的输出信号进行变形，并将它绑定到一个 view 属性上去。这样一来，view 属性就会在一个通知被发送时自动进行变更了。</p>
<p><strong>3.View State</strong></p>
<p>View state 被认为是 model 层的一部分。View state action 以及 view state 通知和 model action 以及 model 通知享有同样的路径。</p>
<p><strong>4.测试</strong></p>
<p>在 MAVB 中，我们通过测试 view 绑定器来测试代码。由于 view 绑定器是一组绑定的列表，我 们可以验证绑定包含了我们所期望的条目，而且它们的配置正确无误。我们可以和使用绑定来 测试初始构建以及发生变化时的情况。</p>
<p>在 MAVB 中进行的测试，与在 MVVM 中的测试很相似。不过，在 MVVM 中，view controller 有可能会包含逻辑，这导致在 view-model 和 view 之间有可能会存在没有测试到的代码。而 MAVB 中不存在 view controller，绑定代码是 model 适配器和 view 绑定器之间的唯一的代码， 这样一来，保证完整的测试覆盖要简单得多。</p>
<ul>
<li><strong>MAVB 的重要性</strong></li>
</ul>
<p>在我们所讨论的主要模式之中，MAVB 没有遵循某个直接的先例，它既不是从其他平台移植过 来的模式，也不是其他模式的变种。它自成一派，用于试验目的，而且一些奇怪。我们在这儿 介绍它的意义在于，它展示了一些很不一样的东西。不过，这并不是说这个模式没有从其他模 式中借鉴经验教训:像是绑定、响应式编程、领域专用语言以及 reducer 都是已经被熟知的想 法了。</p>
<ul>
<li><strong>历史</strong></li>
</ul>
<p>MAVB 是 Matt Gallagher 在 Cocoa with Love 网站上首先提出的。这个模式参照了 Cocoa 绑 定、函数式响应动画、ComponentKit、XAML、Redux 以及成千上万行的使用 Cocoa view controller 的经验。</p>
<p>本书中的实现使用了 CwlViews 框架来处理 view 构建、绑定器和适配器的实现等工作。</p>
<p><strong>5. Elm 架构 (TEA)</strong></p>
<p>TEA 和 MVC 有着根本上的不同。在 TEA 中，model 和所有的 view state 被集成为一个单个状 态对象，所有 app 中的变化都通过向状态对象发送消息来发生，一个叫做 reducer 的状态更新 函数负责处理这些消息。</p>
<p>在 TEA 中，每个状态的改变会生成一个新的虚拟 view 层级，它由轻量级的结构体组成，描述 了 view 层级应该看上去的形式。虚拟 view 层级让我们能够使用纯函数的方式来写 view 部分 的代码;虚拟 view 层级总是直接从状态进行计算，中间不会有任何副作用。当状态发生改变 时，我们使用同样的函数重新计算 view 层级，而不是直接去改变 view 层级。</p>
<p>Driver 类型 (这是 TEA 框架中的一部分，它负责持有对 TEA 中其他层的引用) 将对虚拟 view 层 级和 UIView 层级进行比较，并且对它进行必要的更改，让 view 和它们的虚拟版本相符合。这 个 TEA 框架中的 driver (驱动) 部件是随着我们 app 的启动而被初始化的，它自身并不知道要对 应哪个特定的 app。我们要在它的初始化方法中传入这些信息:包括 app 的初始状态，一个通 过消息更新状态的函数，一个根据给定状态渲染虚拟 view 层级的函数，以及一个根据给定状态 计算通知订阅的函数 (比如，我们可以订阅某个 model store 更改时所发出的通知)。</p>
<p>从框架的使用者的视⻆来看，TEA 的关于更改部分的框图是这样的:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac3333fb2cf742fc9c1ca88ae11e09dc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果我们追踪这张图表的上面两层，我们会发现在 view 和 model 之间存在我们在本章开头是 就说过的反馈回路;这是一个从 view 到状态，然后再返回 view 的回路 (通过 TEA 框架进行协 调)。</p>
<p>下面的回路代表的是 TEA中处理副作用的方式 (比如将数据写入磁盘中):当在状态更新方法中 处理消息时，我们可以返回一个命令，这些命令会被 driver 所执行。在我们的例子中，最重要 的命令是更改 store 中的内容，store 反过来又被 driver 所持有的订阅者监听。这些订阅者可 以触发消息来改变状态，状态最终触发 view 的重新渲染作为响应。</p>
<p>这些事件回路的结构让 TEA 成为了遵守单向数据流原则的设计模式的另一个例子。</p>
<p><strong>1.构建</strong></p>
<p>状态在启动时被构建，并传递给运行时系统 (也就是 driver)。运行时系统拥有状态，store 是一 个单例。</p>
<p>初始的 view 层级和之后更新时的 view 层级是通过同样的路径构建的:通过当前的状态，计算 出虚拟 view 层级，运行时系统负责更新真实的 view 层级，让它与虚拟 view 层级相匹配。</p>
<p><strong>2.更改 Model</strong></p>
<p>虚拟 view 拥有与它们所关联的消息，这些消息在一个 view 事件发生时会被发送。Driver 可以 接收这些消息，并使用更新方法来改变状态。更新方法可以返回一个命令 (副作用)，比如我们</p>
<p>想在 store 中进行的改动。Driver 会截获该命令并执行它。TEA 让 view 不可能直接对状态或者 store 进行更改。</p>
<p><strong>3.更改 View</strong></p>
<p>运行时系统负责这件事。改变 view 的唯一方式是改变状态。所以，初始化创建 view 层级和更</p>
<p>新 view 层级之间没有区别。 4. View State</p>
<p>View state 是包含在整体的状态之中的。由于 view 是直接从状态中计算出来的，导航和交互状 态也同样会被自动更新。</p>
<p><strong>4.测试</strong></p>
<p>在大多数架构中，让测试部件彼此相连往往要花费大量努力。在 TEA 中，我们不需要对此进行 测试，因为 driver 会自动处理这部分内容。类似地，我们不需要测试当状态变化时 view 会正确 随之变化。我们所需要测试的仅仅是对于给定的状态，虚拟 view 层级可以被正确计算。</p>
<p>要测试状态的变更，我们可以创建一个给定的状态，然后使用 update 方法和对应的消息来改 变状态。然后通过对比之前和之后的状态，我们就可以验证 update 是否对给定的状态和消息 返回了所期望的结果。在 TEA 中，我们还可以测试对应给定状态的订阅是不是正确。和 view 层级一样，update 函数和订阅也都是纯函数。</p>
<p>因为所有的部件 (计算虚拟 view 层级，更新函数和订阅) 都是纯函数，我们可以对它们进行完 全隔离的测试。任何框架部件的初始化都是不需要的，我们只用将参数传递进去，然后验证结 果就行了。我们 TEA 实现中的大多数测试都非常直截了当。</p>
<ul>
<li><strong>Elm 架构的重要性</strong></li>
</ul>
<p>TEA 最早是在 Elm 这⻔函数式语言中被实现的。所以 TEA 是一种如何用函数式的方法表达 GUI 编程的尝试。TEA 同时也是最为古老的单向数据流架构。</p>
<ul>
<li><strong>历史</strong></li>
</ul>
<p>Elm 是 Evan Czaplicki 所设计的函数式编程语言，它最初的目的是为了构建前端 web app。 TEA 是归功于 Elm 社区的一个模式，它的出现是语言约束和目标环境相互作用的自然结果。它 背后的思想影响了很多其他的基于 web 的框架，其中包括 React、Redux 和 Flux 等。在 Swift 中，还没有 TEA 的权威实现，不过我们可以找到不少研究型的项目。在本书中，我们使用 Swift 按我们自己的理解实现了这个模式。主要的工作由 Chris Eidhof 于 2017 年完成。虽然我 们的这个实现还并不是 “产品级” 的，但是许多想法是可以用在生产代码中的。</p>
<h2 data-id="heading-5">三，其他APP架构模式</h2>
<p><strong>1. Model-View-Presenter</strong></p>
<p>Model-View-Presenter (MVP) 是一种在 Android 上很流行的模式，在 iOS 中，也有相应的实 现。在总体结构和使用的技术上，它粗略来说是一种位于标准 MVC 和 MVVM 之间的模式。</p>
<p>MVP 使用单独的 presenter 对象，它和 MVVM 中 view-model 所扮演的⻆色一样。相对 view-model 而言，presenter 去除了响应式编程的部分，而是把要展示的值暴露为接口上的属 性。不过，每当这些值需要变更的时候，presenter 会立即将它们推送到下面的 view 中去 (view 将自己作为协议暴露给 presenter)。</p>
<p>从抽象的观点来看，MVP 和 MVC 很像。Cocoa 的 MVC，除了名字以外，就是一个 MVP - 它是 从上世纪九十年代 Taligent 的原始的 MVP 实现中派生出来的。View，状态和关联的逻辑在两 个模式中都是一样的。不同之处在于，现代的 MVP 中有一个分离的 presenter 实体，它使用协 议来在 presenter 和 view controller 之间进行界定，Cocoa 的 MVC 让 controller 能够直接引 用 view，而 MVP 中的 presenter 只能知道 view 的协议。</p>
<p>有些开发者认为协议的分离对于测试是必要的。当我们在讨论测试时，我们会看到标准的 MVC 在没有任何分离的情况下，也可以被完整测试。所以，我们感觉 MVP 并没有太大不同。如果我 们对测试一个完全解耦的展示层有强烈需求的话，我们认为 MVVM 的方式更简单一些:让 view controller 通过观察去从 view-model 中拉取值，而不是让 presenter 将值推送到一个协 议中去。</p>
<p><strong>2. VIPER，Riblets，和其他 “Clean” 架构</strong></p>
<p>VIPER，Riblets 和其他类似的模式尝试将 Robert Martin 的 “Clean Architecture” 从 web app 带到 iOS 开发中，它们主要把 controller 的职责分散到三到四个不同的类中，并用严格的顺序 将它们排列起来。在序列中的每个类都不允许直接引用序列中前面的类。</p>
<p>为了强制单方向的引用这一规则，这些模式需要非常多的协议，类，以及在不同层中传递数据 的方式。由于这个原因，很多使用这些模式的开发者会去使用代码生成器。我们的感觉是，这 些代码生成器，以及任何的繁杂到需要生成器的模式，都产生了一些误导。将 “Clean” 架构带 到 Cocoa 的尝试通常都宣称它们可以管理 view controller 的 “肥大化” 问题，但是让人啼笑皆 非的是，这么做往往让代码库变得更大。</p>
<p>虽然将接口分解是控制代码尺寸的一种有效手段，但是我们认为这应该按需进行，而不是教条 式地对每个 view controller 都这么操作。分解接口需要我们对数据以及所涉及到的任务有清楚 的认识，只有这样，我们才能达到最优的抽象，并在最大程度上降低代码的复杂度。</p>
<p><strong>3. 基于组件的架构 (React Native)</strong></p>
<p>如果你选择使用 JavaScript 而不是 Swift 编程，或者你的 app 重度依赖于 web API 的交互， JavaScript 会是更好的选择，这时你可能会考虑 React Native。不过，本书是专注于 Swift 和 Cocoa 的，所以我们将探索模式的界限定在了这些领域内。</p>
<p>如果你想要找一些类似 React Native，但是是基于 Swift 的东西的话，可以看看我们对 TEA 的 探索。MAVB 的实现也从 ComponentKit 中获得了一些启发，而 ComponentKit 本身又从 React 中获取灵感:它使用类 DSL 的语法来进行声明式和可变形的 view 构建，这和 React 中 Component 的 render 方法及其相似。</p>
<p>**由于文章篇幅有限，只能点到即止地介绍当前一些工作成果和思考，各个 Topic 还有一些新的方向在探索，如果你对 iOS 底层原理、架构设计、构建系统、如何面试有兴趣了解，**你也可以私信我及时获取最新资料以及面试相关资料。如果你有什么意见和建议欢迎给我留言！</p>
<p><strong>喜欢iOS的小伙伴可以关注我，一起学习交流！！！</strong></p>
<p>原文链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93621672" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=https%3A//blog.csdn.net/kyl282889543/article/details/93621672" ref="nofollow noopener noreferrer">IOS APP 架构设计（一）_kyl282889543的博客-CSDN博客_ios 架构</a></p></div>  
</div>
            