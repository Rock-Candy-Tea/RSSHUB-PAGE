
---
title: '【iOS】App 架构 - （二）App 设计模式概览'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d0c25ff686f41509ec8afc4117b3c44~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 04:07:32 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d0c25ff686f41509ec8afc4117b3c44~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>文章来自对 <a href="https://objccn.io/" target="_blank" rel="nofollow noopener noreferrer">objccn.io/</a> 相关书籍的整理笔记。“感谢 objc.io 及其撰稿作者们无私地将他们的知识分享给全世界”。</p>
</blockquote>
<p>使用下面的设计模式为录音 app 完成五种不同的实现。</p>
<p>两种模式在 iOS 中有着广泛的应用:</p>
<ul>
<li>
<p>标准的CocoaModel-View-Controller(MVC)是Apple在示例项目中所采用的设计模式。它是 Cocoa app 中最为常⻅的架构，同时也是在 Cocoa 中讨论架构时所采用的基准线。</p>
</li>
<li>
<p>Model-View-ViewModel+协调器 (MVVM-C) 是 MVC 的变种，它拥有单独的 “view-model” (视图模型) 和一个用来管理 view controller 的协调器。MVVM 使用数据绑定 (通常会和响应式编程一起使用) 来建立 view-model 层和 view 层之间的连接。</p>
</li>
</ul>
<p>将讨论的另外三种模式在 Cocoa 中并不常⻅，是还处于实验阶段的架构。这些架构为构建 app 提供了有用的⻅解，即使不选择将整个架构应用到项目中，也对改进代码会有所帮助:</p>
<ul>
<li>Model-View-Controller+ViewState (MVC+VS) 这种模式将所有的 view state 集中到一个地方，而不是让它们散落在 view 和 view controller 中。这和 model 层所遵循的规则相同，</li>
<li>Model适配器-View绑定器(ModelAdapter-ViewBinder,MAVB)是 App 架构 的一位作者所使用的实验性质的架构。MAVB 专注于构建声明式的 view，并且抛弃 controller，采用绑定的方式来在 model 和 view 之间进行通讯。</li>
<li>Elm 架构 (TEA) 与 MVC 或者 MVVM 这样的常⻅架构完全背道而驰。它使用虚拟 view 层级来构建 view，并使用 reducer 来在 model 和 view 之间进行交互。</li>
</ul>
<h1 data-id="heading-0">Model-View-Controller</h1>
<p>在 Cocoa MVC 中，一小部分 controller 对象负责处理 model 或者 view 层范畴之外的所有任务。</p>
<p>这意味着，controller 层接收所有的 view action，处理所有的交互逻辑，发送所有的 model action，接收所有的 model 通知，对所有用来展示的数据进行准备，最后再将它们应用到 view 的变更上去。看一下 app 反馈回路的图，会发现在 model 和 view 之间的箭头上，几乎每个标签都是 controller。构建和导航任务并没有标注出来，它们也会由 controller 来处理。</p>
<p>下面是 MVC 模式的框图，它展示了一个 MVC app 的主要通讯路径:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d0c25ff686f41509ec8afc4117b3c44~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图中的虚线部分代表运行时的引用，view 层和 model 层都不会直接在代码中引用 controller。
实线部分代表编译期间的引用，controller 实例知道自己所连接的 view 和 model 对象的接口。</p>
<h3 data-id="heading-1">1. 构建</h3>
<p>App 对象负责创建最顶层的 view controller，这个 view controller 将加载 view，并且知道应该从 model 中获取哪些数据，然后把它们显示出来。Controller 要么显式地创建和持有 model 层，要么通过一个延迟创建的 model 单例来获取 model。在多文档配置中，model 层由更低层的像是 UIDocument 或 NSDocument 所拥有。那些和 view 相关的单个 model 对象，通常会被 controller 所引用并缓存下来。</p>
<h3 data-id="heading-2">2. 更改 Model</h3>
<p>在 MVC 中，controller 主要通过 target/action 机制和 (由 storyboard 或者代码进行设置的) delegate 来接收 view 事件。Controller 知道自己所连接的 view，但是 view 在编译期间却没有关于 controller 接口的信息。当一个 view 事件到达时，controller 有能力改变自身的内部状态，更改 model，或者直接改变 view 层级。</p>
<h3 data-id="heading-3">3. 更改 View</h3>
<p>MVC 中，当一个更改 model 的 view action 发生时，controller 不应该直接去操作 view 层级。正确的做法是，controller 去订阅 model 通知，并且在当通知到达时再更改 view 层级。这样一来，数据流就可以单向进行:view action 被转变为 model 变更，然后 model 发送通知，这个通知最后被转为 view 变更。</p>
<h3 data-id="heading-4">4. View State</h3>
<p>View state 可以按需要被 store 在 view 或者 controller 的属性中。相对于影响 model 的 view action，那些只影响 view 或 controller 状态的 action 则不需要通过 model 进行传递。对于 view state 的存储，可以结合使用 storyboard 和 UIStateRestoring 来进行实现，storyboard 负责记录活跃的 controller 层级，而 UIStateRestoring 负责从 controller 和 view 中读取数据。</p>
<h3 data-id="heading-5">5. 测试</h3>
<p>在 MVC 中，view controller 与 app 的其他部件紧密相连。边界的缺失使得为 controller 编写单元测试和接口测试十分困难，集成测试是余下的为数不多的可行测试手段之一。在集成测试中，构建相连接的 view、model 和 controller 层，然后操作 model 或者 view，来测试是否能得到想要的结果。</p>
<p>集成测试的书写非常复杂，而且它涵盖的范围太广了。它不仅仅测试逻辑，也测试部件是如何连接的 (虽然在一些情况下和 UI 测试的⻆度并不相同)。不过，在 MVC 中通过集成测试，通常达到 80% 左右的测试覆盖率是有可能的。</p>
<h2 data-id="heading-6">MVC 的重要性</h2>
<p>因为 Apple 在所有的实例项目中都使用了这种模式，加上 Cocoa 本身就是针对这种模式设计的，所以 Cocoa MVC 成为了 iOS，macOS，tvOS 和 watchOS 上官方认证的 app 架构模式。</p>
<p>MVC 的自由度允许在使用时引入非常多的变种:很多来源于其他模式的思想，它们都可以被集成到整个 app 中的某个小部分中去。</p>
<h3 data-id="heading-7">历史</h3>
<p>MVC 这个名字第一次被提出是在 1979 年，Trygve Reenskaug 用它来描述 Smalltalk-76 上已 经存在的 “template pattern” 应用。Cocoa 中的 MVC 实现可以追溯到大约 1997 年的 NeXTSTEP 4 的年代。在那之前，所有现在 controller 所担当的⻆色，通常都由一个 (像是 NSWindow 那样的) 高层 view 类来扮演。之后， 从原始的 Smalltalk 的 MVC 实现中所发展出的理念是分离展示部分，也就是 view 层和 model 层应该被完全隔离开，这带来了一个强烈的需求，那就是要引入一个支持对象来辅助两者之间的通讯。</p>
<h1 data-id="heading-8">Model-View-ViewModel+协调器</h1>
<p>MVVM 和 MVC 类似，也是通过基于场景 (scene，view 层级中可能会在导航发生改变时切入或者换出的子树) 进行的架构。</p>
<p>相较于 MVC，MVVM 在每个场景中使用 view-model 来描述场景中的表现逻辑和交互逻辑。</p>
<p>View-model 在编译期间不包含对 view 或者 controller 的引用。它暴露出一系列属性，用来描述每个 view 在显示时应有的值。把一系列变换运用到底层的 model 对象后，就能得到这些最终可以直接设置到 view 上的值。实际将这些值设置到 view 上的工作，则由预先建立的绑定来完成，绑定会保证当这些显示值发生变化时，把它设定到对应的 view 上去。响应式编程是用来表达这类声明和变换关系的很好的工具，所以它天生就适合 (虽说不是严格必要) 被用来处理 view-model。在很多时候，整个 view-model 都可以用响应式编程绑定的方式，以声明式的形式进行表达。</p>
<p>在理论上，因为 view-model 不包含对 view 层的引用，所以它是独立于 app 框架的，这让对于 view-model 的测试也可以独立于 app 框架。</p>
<p>由于 view-model 是和场景耦合的，我们还需要一个能够在场景间切换时提供逻辑的对象。在 MVVM-C 中，这个对象叫做协调器 (coordinator)。协调器持有对 model 层的引用，并且了解 view controller 树的结构，这样，它能够为每个场景的 view-model 提供所需要的 model 对象。</p>
<p>和 MVC 不同，MVVM-C 中的 view controller 从来都不会直接引用其他的 view controller (所以，也不会引用其他的 view-model)。View controller 通过 delegate 的机制，将 view action 的信息告诉协调器。协调器据此显示新的 view controller 并设置它们的 model 数据。换句话 说，view controller 的层级是由协调器进行管理的，而不是由 view controller 来决定的。</p>
<p>这些特性所形成的架构的总体结构如下图所示:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39ed865d2f8143e8b01c0b105544914c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果忽略掉协调器，那么这张图表就很像 MVC 了，只不过在 view controller 和 model 之间加入了一个阶段。MVVM 将之前在 view controller 中的大部分工作转移到了 view-model 中，但是要注意，view-model 并不会在编译时拥有对 view controller 的引用。</p>
<p>View-model 可以从 view controller 和 view 中独立出来，也可以被单独测试。同样，view controller 也不再拥有内部的 view state，这些状态也被移动到了 view-model 中。在 MVC 中 view controller 的双重⻆色 (既作为 view 层级的一部分，又负责协调 view 和 model 之间的交互)，减少到了单一⻆色 (view controller 仅仅只是 view 层级的一部分)。</p>
<p>协调器模式的加入进一步减少了 view controller 所负责的部分:现在它不需要关心如何展示其他的 view controller 了。因此，这实际上是以添加了一层 controller 接口为代价，降低了 view controller 之间的耦合。</p>
<blockquote>
<p>View-model 虽然名字里既有 view 又有 model，但是它所扮演的其实是类似 controller 的⻆色。将严格区分 view controller 和 controller，前者只是后者的一个子集，view controller 仅仅是负责控制 view 的那部分 controller 类型。</p>
</blockquote>
<h3 data-id="heading-9">1. 构建</h3>
<p>对于 model 的创建和 MVC 中的保持不变，通常它是一个顶层 controller 的职责。不过，单独的 model 对象现在属于 view-model，而不属于 view controller。</p>
<p>初始的 view 层级的创建和 MVC 中的一样，通过 storyboard 或者代码来完成。和 MVC 不同的是，view controller 不再直接为每个 view 获取和准备数据，它会把这项工作交给 view-model。 View controller 在创建的时候会一并创建 view-model，并且将每个 view 绑定到 view-model 所暴露出的相应属性上去。</p>
<h3 data-id="heading-10">2. 更改 Model</h3>
<p>在 MVVM 中，view controller 接收 view 事件的方式和 MVC 中一样 (在 view 和 view controller 之间建立连接的方式也相同)。不过，当一个 view 事件到达时，view controller 不会去改变自身的内部状态、view state、或者是 model。相对地，它立即调用 view-model 上的方法，再由 view-model 改变内部状态或者 model。</p>
<h3 data-id="heading-11">3. 更改 View</h3>
<p>和 MVC 不同，view controller 不监听 model。View-model 将负责观察 model，并将 model 的通知转变为 view controller 可以理解的形式。View controller 订阅 view-model 的变更，这通常通过一个响应式编程框架来完成，但也可以使用任意其他的观察机制。当一个 view-model 事件来到时，由 view controller 去更改 view 层级。</p>
<p>为了实现单向数据流，view-model 总是应该将变更 model 的 view action 发送给 model，并且仅仅在 model 变化实际发生之后再通知相关的观察者。</p>
<h3 data-id="heading-12">4. View State</h3>
<p>View state 要么存在于 view 自身之中，要么存在于 view-model 里。和 MVC 不同，view controller 中不存在任何 view state。View-model 中的 view state 的变更，会被 controller 观察到，不过 controller 无法区分 model 的通知和 view state 变更的通知。当使用协调器时， view controller 层级将由协调器进行管理。</p>
<h3 data-id="heading-13">5. 测试</h3>
<p>因为 view-model 和 view 层与 controller 层是解耦合的，所以可以使用接口测试来测试 view-model，而不需要像 MVC 里那样使用集成测试。接口测试要比集成测试简单得多，因为不需要为它们建立完整的组件层次结构。</p>
<p>为了让接口测试尽可能覆盖更多的范围，view controller 应当尽可能简单，但是那些没有被移出 view controller 的部分仍然需要单独进行测试。这部分内容包括与协调器的交互，以及初始时负责创建工作的代码。</p>
<h2 data-id="heading-14">MVVM 的重要性</h2>
<p>MVVM 是 iOS 上最流行的 MVC 的非直接变形的 app 设计模式。它和 MVC 相比，并没有非常大的不同；两者都是围绕 view controller 场景构建的，而且所使用的机制也大都相同。</p>
<p>最大的区别可能在于 view-model 中对响应式编程的使用了，它被用来描述一系列的转换和依赖关系。通过使用响应式编程来清晰地描述 model 对象与显示值之间的关系，为从总体上理解应用中的依赖关系提供了重要的指导。</p>
<h3 data-id="heading-15">历史</h3>
<p>MVVM 由 Ken Cooper 和 Ted Peters 提出，他们当时在微软工作，负责后来变成 Windows Presentation Foundation (WPF) 的项目，这是微软 .NET 的 app 框架，并于 2005 年正式发布。</p>
<p>iOS 中的协调器则是最近才 (重新) 流行起来的，Soroush Khanlou 在 2015 年时在他的网站 上描述了这个想法。协调器基于 app controller 这样的更古老的模式，而它们在 Cocoa 和其他平台上已经存在了有数十年之久。</p>
<h1 data-id="heading-16">Model-View-Controller+ViewState</h1>
<p>MVC+VS 是为标准的 MVC 带来单向数据流方式的一种尝试。在标准的 Cocoa MVC 中，view state 可以由两到三种不同的路径进行操作，MVC+VS 则试图避免这点，让 view state 的处理更加易于管理。在 MVC+VS 中，明确地在一个新的 model 对象中，对所有的 view state 进行定义和表达，把这个对象叫做 view state model。</p>
<p>在 MVC+VS 中，不会忽略任何一次导航变更，列表选择，文本框编辑，开关变更，model 展示或者滚动位置变更 (或者其他任意的 view state 变化)。将这些变更发送给 view state model。每个 view controller 负责监听 view state model，这样变更的通讯会非常直接。在表现或者交互逻辑部分，不从 view 中去读取 view state ，而是从 view state model 中去获取它们:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbc5770ea9fa461db9b47fb8a7762632~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结果所得到的图表和 MVC 类似，但 controller 的内部反馈回路的部分 (被用来更新 view state) 有所不同，现在它和 model 的回路类似，形成了一个独立的 view state 回路。</p>
<h3 data-id="heading-17">1. 构建</h3>
<p>和传统的 MVC 一样，将文档 model 数据应用到 view 上的工作依然是 view controller 的责任， view controller 还会使用和订阅 view state 。因为 view state model 和文档 model 都需要观察，所以相比于典型的 MVC 来说，需要多得多的通过通知进行观察的函数。</p>
<h3 data-id="heading-18">2. 更改 Model</h3>
<p>当 view action 发生时，view controller 去变更文档 model (这和 MVC 保持不变) 或者变更 model state。不会去直接改变 view 层级，所有的 view 变更都要通过文档 model 和 view state model 的通知来进行。</p>
<h3 data-id="heading-19">3. 更改 View</h3>
<p>Controller 同时对文档 model 和 view state model 进行观察，并且只在变更发生的时候更新 view 层级。</p>
<h3 data-id="heading-20">4. View State</h3>
<p>View State 被明确地从 view controller 中提取出来。处理的方法和 model 是一样的: controller 观察 view state model，并且对应地更改 view 层级。</p>
<h3 data-id="heading-21">5. 测试</h3>
<p>在 MVC+VS 中，使用和 MVC 里类似的集成测试，但是测试本身会非常不同。所有的测试都从一个空的根 view controller 开始，然后通过设定文档 model 和 view state model，这个根 view controller 可以构建出整个 view 层级和 view controller 层级。MVC 的集成测试中最困难的部分 (设定所有的部件) 在 MVC+VS 中可以被自动完成。要测试另一个 view state 时，可以重新设置全局 view state，所有的 view controller 都会调整自身。</p>
<p>一旦 view 层级被构建，可以编写两种测试。第一种测试负责检查 view 层级是不是按照我期望被建立起来，第二种测试检查 view action 有没有正确地改变 view state。</p>
<h2 data-id="heading-22">MVC+VS 的重要性</h2>
<p>MVC+VS 主要是用来对 view state 进行教学的工具。</p>
<p>在一个非标准 MVC 的 app 中，添加一个 view state model，并且在每个 view controller 中 (在已经对 model 进行观察的基础上) 观察这些 view state model，提供了不少优点:任意的状 态恢复 (这种恢复不依赖于 storyboard 或者 UIStateRestoration)，完整的用户界面日志，以及 为了调试目的，在不同的 view state 间进行跳转的能力。</p>
<h3 data-id="heading-23">历史</h3>
<p>这种特定的体系
是 Matt Gallagher 在 2017 年开发的教学工具，它被用来展示单向数据流和用户界面的时间旅行等概念。这个模式的目标是，在传统的 Cocoa MVC app 上通过最小的改动， 实现对 view 的状态在每个 action 发生时都可以进行快照。</p>
<h1 data-id="heading-24">Model 适配器-View 绑定器 (MAVB)</h1>
<p>MAVB 是一种以绑定为中心的实验模式。在这个模式中，有三个重要的概念:view 绑定器，model 适配器，以及绑定。</p>
<p>View 绑定器是 view (或者 view controller) 的封装类:它构建 view，并且为它暴露出一个绑定 列表。一些绑定为 view 提供数据 (比如，一个标签的文本)，另一些从 view 中发出事件 (比如，按钮点击或者导航变更)。</p>
<p>虽然 view 绑定器可以含有动态绑定，但是 view 绑定器本身是不可变的。这让 MAVB 也成为了一种声明式的模式:声明 view 绑定器和它们的 action，而不是随着时间去改变 view 绑定器。</p>
<p>Model 适配器是可变状态的封装，它是由所谓的 reducer 进行实现的。Model 适配器提供了一个 (用于发送事件的) 输入绑定，以及一个 (用于接收更新的) 输出绑定。</p>
<p>在 MAVB 中，不会去直接创建 view;相对地，只会去创建 view 绑定器。同样地，也从来不会去处理 model 适配器以外的可变状态。在 view 绑定器和 model 适配器之间的 (两个方向上的) 变换，是通过 (使用标准的响应式编程技术) 来对绑定进行变形而完成的。</p>
<p>MAVB 移除了对 controller 层的需求。创建逻辑通过 view 绑定器来表达，变换逻辑通过绑定来表达，而状态变更则通过 model 适配器来表达。结果得到的框图如下:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b17997e4aef94e4a97faed89d2524412~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-25">1. 构建</h3>
<p>Model 适配器 (用来封装主 model ) 和 view state 适配器 (封装顶层的 view state) 通常是在 main.swift 文件中进行创建的，这早于任何的 view。</p>
<p>View 绑定器使用普通的函数进行构建，这些函数接受必要的 model 适配器作为参数。实际的
Cocoa view 则由框架负责进行创建。</p>
<h3 data-id="heading-26">2. 更改 Model</h3>
<p>当一个 view (或者 view controller) 可以发出 action 时，对应的 view 绑定允许指定一个 action 绑定。在这里，数据从 view 流向 action 绑定的输出端。典型情况下，输出端会与一个 model 适配器相连接，view 事件会通过绑定进行变形，成为 model 适配器可以理解的一条消息。这条消息随后被 model 适配器的 reducer 使用，并改变状态。</p>
<h3 data-id="heading-27">3. 更改 View</h3>
<p>当 model 适配器的状态发生改变时，它会通过输出信号产生通知。在 view 绑定器中，可以将 model 适配器的输出信号进行变形，并将它绑定到一个 view 属性上去。这样一来，view 属性就会在一个通知被发送时自动进行变更了。</p>
<h3 data-id="heading-28">4. View State</h3>
<p>View state 被认为是 model 层的一部分。View state action 以及 view state 通知和 model action 以及 model 通知享有同样的路径。</p>
<h3 data-id="heading-29">5. 测试</h3>
<p>在 MAVB 中，通过测试 view 绑定器来测试代码。由于 view 绑定器是一组绑定的列表，可以验证绑定包含了所期望的条目，而且它们的配置正确无误。可以和使用绑定来测试初始构建以及发生变化时的情况。</p>
<p>在 MAVB 中进行的测试，与在 MVVM 中的测试很相似。不过，在 MVVM 中，view controller 有可能会包含逻辑，这导致在 view-model 和 view 之间有可能会存在没有测试到的代码。而 MAVB 中不存在 view controller，绑定代码是 model 适配器和 view 绑定器之间的唯一的代码，这样一来，保证完整的测试覆盖要简单得多。</p>
<h2 data-id="heading-30">MAVB 的重要性</h2>
<p>MAVB 没有遵循某个直接的先例，它既不是从其他平台移植过来的模式，也不是其他模式的变种。它自成一派，用于试验目的，而且有一些奇怪，它展示了一些很不一样的东西。不过，这并不是说这个模式没有从其他模式中借鉴经验教训:像是绑定、响应式编程、领域专用语言以及 reducer 都是已经被熟知的想法了。</p>
<h3 data-id="heading-31">历史</h3>
<p>MAVB 是 Matt Gallagher 在 Cocoa with Love 网站上首先提出的。这个模式参照了 Cocoa 绑 定、函数式响应动画、ComponentKit、XAML、Redux 以及成千上万行的使用 Cocoa view controller 的经验。例子的实现使用了 CwlViews 框架来处理 view 构建、绑定器和适配器的实现等工作。</p>
<h1 data-id="heading-32">Elm 架构 (TEA)</h1>
<p>TEA 和 MVC 有着根本上的不同。在 TEA 中，model 和所有的 view state 被集成为一个单个状态对象，所有 app 中的变化都通过向状态对象发送消息来发生，一个叫做 reducer 的状态更新函数负责处理这些消息。</p>
<p>在 TEA 中，每个状态的改变会生成一个新的虚拟 view 层级，它由轻量级的结构体组成，描述了 view 层级应该看上去的形式。虚拟 view 层级让使用纯函数的方式来写 view 部分的代码;虚拟 view 层级总是直接从状态进行计算，中间不会有任何副作用。当状态发生改变时，我们使用同样的函数重新计算 view 层级，而不是直接去改变 view 层级。</p>
<p>Driver 类型 (这是 TEA 框架中的一部分，它负责持有对 TEA 中其他层的引用) 将对虚拟 view 层 级和 UIView 层级进行比较，并且对它进行必要的更改，让 view 和它们的虚拟版本相符合。这个 TEA 框架中的 driver (驱动) 部件是随着 app 的启动而被初始化的，它自身并不知道要对应哪个特定的 app。在它的初始化方法中传入这些信息:包括 app 的初始状态，一个通过消息更新状态的函数，一个根据给定状态渲染虚拟 view 层级的函数，以及一个根据给定状态计算通知订阅的函数 (比如，可以订阅某个 model store 更改时所发出的通知)。</p>
<p>从框架的使用者的视⻆来看，TEA 的关于更改部分的框图是这样的:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7f35ace039b4f078ba2d59030945e7d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>追踪这张图表的上面两层，会发现在 view 和 model 之间存在反馈回路;这是一个从 view 到状态，然后再返回 view 的回路 (通过 TEA 框架进行协调)。</p>
<p>下面的回路代表的是 TEA 中处理副作用的方式 (比如将数据写入磁盘中):当在状态更新方法中处理消息时，可以返回一个命令，这些命令会被 driver 所执行。最重要的命令是更改 store 中的内容，store 反过来又被 driver 所持有的订阅者监听。这些订阅者可以触发消息来改变状态，状态最终触发 view 的重新渲染作为响应。</p>
<p>这些事件回路的结构让 TEA 成为了遵守单向数据流原则的设计模式的另一个例子。</p>
<h3 data-id="heading-33">1. 构建</h3>
<p>状态在启动时被构建，并传递给运行时系统 (也就是 driver)。运行时系统拥有状态，store 是一个单例。</p>
<p>初始的 view 层级和之后更新时的 view 层级是通过同样的路径构建的:通过当前的状态，计算出虚拟 view 层级，运行时系统负责更新真实的 view 层级，让它与虚拟 view 层级相匹配。</p>
<h3 data-id="heading-34">2. 更改 Model</h3>
<p>虚拟 view 拥有与它们所关联的消息，这些消息在一个 view 事件发生时会被发送。Driver 可以接收这些消息，并使用更新方法来改变状态。更新方法可以返回一个命令 (副作用)，比如想在 store 中进行的改动。Driver 会截获该命令并执行它。TEA 让 view 不可能直接对状态或者 store 进行更改。</p>
<h3 data-id="heading-35">3. 更改 View</h3>
<p>运行时系统负责这件事。改变 view 的唯一方式是改变状态。所以，初始化创建 view 层级和更新 view 层级之间没有区别。</p>
<h3 data-id="heading-36">4. View State</h3>
<p>View state 是包含在整体的状态之中的。由于 view 是直接从状态中计算出来的，导航和交互状 态也同样会被自动更新。</p>
<h3 data-id="heading-37">5. 测试</h3>
<p>在大多数架构中，让测试部件彼此相连往往要花费大量努力。在 TEA 中，不需要对此进行测试，因为 driver 会自动处理这部分内容。类似地，不需要测试当状态变化时 view 会正确随之变化。所需要测试的仅仅是对于给定的状态，虚拟 view 层级可以被正确计算。</p>
<p>要测试状态的变更，可以创建一个给定的状态，然后使用 update 方法和对应的消息来改变状态。然后通过对比之前和之后的状态，就可以验证 update 是否对给定的状态和消息返回了所期望的结果。在 TEA 中，还可以测试对应给定状态的订阅是不是正确。和 view 层级一样，update 函数和订阅也都是纯函数。</p>
<p>因为所有的部件 (计算虚拟 view 层级，更新函数和订阅) 都是纯函数，可以对它们进行完全隔离的测试。任何框架部件的初始化都是不需要的，只用将参数传递进去，然后验证结果就行了。TEA 实现中的大多数测试都非常直截了当。</p>
<h1 data-id="heading-38">Elm 架构的重要性</h1>
<p>TEA 最早是在 Elm 这⻔函数式语言中被实现的。所以 TEA 是一种如何用函数式的方法表达 GUI 编程的尝试。TEA 同时也是最为古老的单向数据流架构。</p>
<h3 data-id="heading-39">历史</h3>
<p>Elm 是 Evan Czaplicki 所设计的函数式编程语言，它最初的目的是为了构建前端 web app。 TEA 是归功于 Elm 社区的一个模式，它的出现是语言约束和目标环境相互作用的自然结果。在 Swift 中，还没有 TEA 的权威实现，不过我们可以找到不少研究型的项目。</p>
<h1 data-id="heading-40">网络</h1>
<p>使用 MVC 版本的 app 来展示了两种不同的添加网络层的方法。在第一种方法中，controller 拥有网络，将 model 层用一个网络服务取代。在第二种方法中，model 拥有网络，我们在 model 层的上方添加了网络功能。</p>
<p>从研究 controller 拥有的网络开始会简单一些:每个 view controller 在需要的时候执行请求， 并将结果缓存在本地。不过，一旦当数据需要在不同的 view controller 之间共享的时候，这种模式就变得难以操作了。此时，一种通常更简单的做法是换成 model 拥有的网络。通过将网络作为 model 层的扩展，可以建立一套共享数据和变更通讯的机制。</p>
<h1 data-id="heading-41">没有提到的模式</h1>
<h2 data-id="heading-42">Model-View-Presenter</h2>
<p>Model-View-Presenter (MVP) 是一种在 Android 上很流行的模式，在 iOS 中，也有相应的实现。在总体结构和使用的技术上，它粗略来说是一种位于标准 MVC 和 MVVM 之间的模式。</p>
<p>MVP 使用单独的 presenter 对象，它和 MVVM 中 view-model 所扮演的⻆色一样。相对 view-model 而言，presenter 去除了响应式编程的部分，而是把要展示的值暴露为接口上的属性。不过，每当这些值需要变更的时候，presenter 会立即将它们推送到下面的 view 中去 (view 将自己作为协议暴露给 presenter)。</p>
<p>从抽象的观点来看，MVP 和 MVC 很像。Cocoa 的 MVC，除了名字以外，就是一个 MVP - 它是从上世纪九十年代 Taligent 的原始的 MVP 实现中派生出来的。View，状态和关联的逻辑在两个模式中都是一样的。不同之处在于，现代的 MVP 中有一个分离的 presenter 实体，它使用协议来在 presenter 和 view controller 之间进行界定，Cocoa 的 MVC 让 controller 能够直接引用 view，而 MVP 中的 presenter 只能知道 view 的协议。</p>
<p>有些开发者认为协议的分离对于测试是必要的。当在讨论测试时，会看到标准的 MVC 在没有任何分离的情况下，也可以被完整测试。所以 MVP 并没有太大不同。如果对测试一个完全解耦的展示层有强烈需求的话， MVVM 的方式更简单一些:让 view controller 通过观察去从 view-model 中拉取值，而不是让 presenter 将值推送到一个协议中去。</p>
<h2 data-id="heading-43">VIPER，Riblets，和其他 “Clean” 架构</h2>
<p>VIPER，Riblets 和其他类似的模式尝试将 Robert Martin 的 “Clean Architecture” 从 web app 带到 iOS 开发中，它们主要把 controller 的职责分散到三到四个不同的类中，并用严格的顺序 将它们排列起来。在序列中的每个类都不允许直接引用序列中前面的类。</p>
<p>为了强制单方向的引用这一规则，这些模式需要非常多的协议，类，以及在不同层中传递数据的方式。由于这个原因，很多使用这些模式的开发者会去使用代码生成器。这些代码生成器，以及任何的繁杂到需要生成器的模式，都产生了一些误导。将 “Clean” 架构带 到 Cocoa 的尝试通常都宣称它们可以管理 view controller 的 “肥大化” 问题，往往让代码库变得更大。</p>
<p>虽然将接口分解是控制代码尺寸的一种有效手段，但是这应该按需进行，而不是教条式地对每个 view controller 都这么操作。分解接口需要对数据以及所涉及到的任务有清楚的认识，只有这样才能达到最优的抽象，并在最大程度上降低代码的复杂度。</p>
<h2 data-id="heading-44">基于组件的架构 (React Native)</h2>
<p>如果选择使用 JavaScript 而不是 Swift 编程，或 app 重度依赖于 web API 的交互， JavaScript 会是更好的选择，这时可能会考虑 React Native。</p>
<p>如果你想要找一些类似 React Native，但是是基于 Swift 的东西的话，可以看对 TEA 的探索。MAVB 的实现也从 ComponentKit 中获得了一些启发，而 ComponentKit 本身又从 React 中获取灵感:它使用类 DSL 的语法来进行声明式和可变形的 view 构建，这和 React 中 Component 的 render 方法及其相似。</p></div>  
</div>
            