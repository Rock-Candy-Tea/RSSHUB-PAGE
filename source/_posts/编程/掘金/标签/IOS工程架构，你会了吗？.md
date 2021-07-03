
---
title: 'IOS工程架构，你会了吗？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e604ae2703d84bc19ba693539efa1f6a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 22:36:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e604ae2703d84bc19ba693539efa1f6a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、框架模式的选择</h1>
<h2 data-id="heading-1">1. MVC模式</h2>
<p>MVC全名是Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写，一种软件设计典范，用一种业务逻辑、数据、界面显示分离的方法组织代码，将业务逻辑聚集到一个部件里面，在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑。MVC被独特的发展起来用于映射传统的输入、处理和输出功能在一个逻辑的图形化用户界面的结构中。</p>
<h3 data-id="heading-2">1.1 MVC 编程模式</h3>
<p>MVC 是一种使用 MVC（Model View Controller 模型-视图-控制器）设计应用程序的模式</p>
<ul>
<li>
<p><strong>视图</strong>（View）：负责数据展示、监听用户触摸等工作</p>
</li>
<li>
<p><strong>控制器</strong>（Controller）：负责业务逻辑、事件响应、数据加工等工作</p>
</li>
<li>
<p><strong>模型</strong>（Controller）：负责封装数据、存储和处理数据运算等工作</p>
</li>
</ul>
<h3 data-id="heading-3">1.2 MVC通信特点</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e604ae2703d84bc19ba693539efa1f6a~tplv-k3u1fbpfcp-watermark.image" alt="2021051517090759.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>Model和View永远不能相互通信，只能通过Controller传递。</p>
</li>
<li>
<p>Controller可以直接与Model通信（读写调用Model），Model通过Notification和KVO机制与Controller间接通信。</p>
</li>
<li>
<p>Controller与View通过Target/Action，delegate和datasource三种模式进行通信。</p>
</li>
</ol>
<p>通过这三种模式，View就可以向Controller通信，Action/Target 模式来让Controller 监听View 触发的事件。View又通过Data source和delegate进行数据获取和某些通信操作。</p>
<h3 data-id="heading-4">1.3 MVC优缺点</h3>
<p><strong>1. 易用性</strong>：与其他几种模式相比最小的代码量，维护起来也较为容易。</p>
<p><strong>2. 可测性</strong>：由于糟糕的分散性，只能对Model进行测试。</p>
<p><strong>3. 均衡性</strong>：厚重的ViewController、无处安放的网络逻辑与数据逻辑。</p>
<h2 data-id="heading-5">2.MVCS模式</h2>
<p>苹果自身就采用的是这种架构思路，从名字也能看出，也是基于MVC衍生出来的一套架构。从概念上来说，它拆分的部分是Model部分，拆出来一个Store。这个Store专门负责数据存取。</p>
<p>从实际操作的角度上讲，它拆开的是Controller。因为Controller做了数据存储的事情，就会变得非常庞大，那么就把Controller专门负责存取数据的那部分抽离出来，交给另一个对象去做，这个对象就是Store。这么调整之后，整个结构也就变成了真正意义上的MVCS。</p>
<ul>
<li>
<p>视图（View）：用户界面</p>
</li>
<li>
<p>控制器（Controller）：业务逻辑及处理</p>
</li>
<li>
<p>模型（Model）：数据存储</p>
</li>
<li>
<p>存储器（Store）：数据处理逻辑</p>
</li>
</ul>
<p>MVCS是基于瘦Model的一种架构思路，把原本Model要做的很多事情中的其中一部分关于数据存储的代码抽象成了Store，在一定程度上降低了Controller的压力。</p>
<h2 data-id="heading-6">3. MVP模式</h2>
<p>MVP（Model-View-Presenter）是从经典的模式MVC演变而来，它们的基本思想有相通的地方Controller/Presenter负责逻辑的处理，Model提供数据，View负责显示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da78ce27e3ba4dc99b819a9ded9c760d~tplv-k3u1fbpfcp-watermark.image" alt="0af902ea9926b6ed803a1f521c59bb3f.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">3.1 MVP模式的优缺点</h3>
<ol>
<li>
<p>模型与视图完全分离，我们可以修改视图而不影响模型。</p>
</li>
<li>
<p>可以更高效地使用模型，因为所有的交互都发生在Presenter内部。</p>
</li>
<li>
<p>可以将一个Presenter用于多个视图，而不需要改变Presenter的逻辑。</p>
</li>
<li>
<p>如果我们把逻辑放在Presenter中，那么我们就可以脱离用户接口来测试这些逻辑。</p>
</li>
<li>
<p>由于对视图的渲染放在了Presenter中，视图和Presenter的交互会过于频繁，一旦视图需要变更，Presenter也需要变更了。</p>
</li>
</ol>
<h3 data-id="heading-8">3.2 MVP与MVC区别：</h3>
<ol>
<li>
<p>在MVP中View并不直接使用Model，它们之间的通信是通过Presenter (MVC中的Controller)来进行的，所有的交互都发生在Presenter内部，而在MVC中View会直接从Model中读取数据而不是通过 Controller。</p>
</li>
<li>
<p>在MVP中view 引用Presenter ，Presenter不引用View；Presenter 引用Model，Model不引用Presenter。</p>
</li>
<li>
<p>在MVC里，View是可以直接访问Model的。View里会包含Model信息，不可避免的还要包括一些业务逻辑。 在MVC模型里，Model不依赖于View，但是View是依赖于Model的。因为有一些业务逻辑在View里实现了，导致View的可重用性降低。</p>
</li>
<li>
<p>在MVC里，不建议在 View 中依赖 Model，而是尽可能把业务逻辑都放在 Controller 中处理，使View 只和 Controller 交互。</p>
</li>
</ol>
<h2 data-id="heading-9">4.MVVM模式</h2>
<p>MVVM是Model-View-ViewModel的简写。它本质上就是MVC 的改进版。MVVM 就是将其中的View 的状态和行为抽象化，让我们将视图 UI 和业务逻辑分开。当然这些事 ViewModel 已经帮我们做了，它可以取出 Model 的数据同时帮忙处理 View 中由于需要展示内容而涉及的业务逻辑。</p>
<p>MVVM（Model-View-ViewModel）框架的由来便是MVP（Model-View-Presenter）模式与WPF结合的应用方式时发展演变过来的一种新型架构框架。它立足于原有MVP框架并且把WPF的新特性糅合进去，以应对客户日益复杂的需求变化。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25e12530ef2148a8b66e3a1f32dd47e1~tplv-k3u1fbpfcp-watermark.image" alt="20210515171017267.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">4.1 MVVM模式的组成部分</h3>
<ul>
<li>
<p>模型：模型是指代表真实状态内容的领域模型（面向对象），或指代表内容的数据访问层（以数据为中心）。</p>
</li>
<li>
<p>视图：就像在MVC和MVP模式中一样，视图是用户在屏幕上看到的结构、布局和外观（UI）。</p>
</li>
<li>
<p>视图模型：视图模型是暴露公共属性和命令的视图的抽象。在视图模型中，绑定器在视图和数据绑定器之间进行通信。</p>
</li>
</ul>
<p>引用特点：view 引用viewModel ，viewModel不引用view（即不要在viewModel中引入#import UIKit.h，任何视图本身的引用都不应该放在viewModel中）；viewModel 引用model，model不引用viewModel。</p>
<h3 data-id="heading-11">3.2 MVVM优点</h3>
<ul>
<li>
<p><strong>低耦合</strong>：View可以独立于Model变化和修改，一个ViewModel可以绑定到不同的View上，当View变化的时候Model可以不变，当Model变化的时候View也可以不变。</p>
</li>
<li>
<p><strong>可重用性</strong>：你可以把一些视图逻辑放在一个ViewModel里面，让很多view重用这段视图逻辑。</p>
</li>
<li>
<p><strong>独立开发</strong>：开发人员可以专注于业务逻辑和数据的开发（ViewModel），设计人员可以专注于页面设计。</p>
</li>
<li>
<p><strong>可测试</strong>：界面素来是比较难于测试的，而现在测试可以针对ViewModel来写。</p>
</li>
</ul>
<h3 data-id="heading-12">3.2 MVVM与MVP区别：</h3>
<p>mvvm模式将Presener改名为View Model，基本上与MVP模式完全一致，唯一的区别是，MVVM可以结合RAC（MVVM+RAC）实现view与ViewModel的双向绑定，这样开发者就不用处理接收事件和View更新的工作。</p>
<h1 data-id="heading-13">二、通用基础库与cocoaPod应用</h1>
<h2 data-id="heading-14">1. 通用基础库的目录分布</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5782582a65394e279ba1eba9ab3e19fb~tplv-k3u1fbpfcp-watermark.image" alt="20210518160007185.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>【Service】业务服务层，存放公共业务逻辑与通用服务，如公共接口、基础组件配置、用户信息、共享数据、页面路由配置等。</p>
<p>【BaseKit】基础层，存放着通用的基础库，应用于各个业务模块。</p>
<p><strong>CommonLib</strong>：通用功能组件，具体功能的实现和应用，如APM、数据上报、页面路由、OCR等。</p>
<p><strong>Views</strong>：通用视图组件，如BannerView、AlertView、pageControl、loadingView等。</p>
<p><strong>Kernal</strong>：基础服务组件，提供基础服务能力，如Network、Log、dataBase、webImage等。</p>
<p><strong>Basic</strong>：基础类，又分为MVC三个子目录，封装存放Basic类。</p>
<p><strong>Marco</strong>：通用声明，宏定义-define、常量声明-extern。</p>
<p><strong>Utils</strong>：工具类集合，如Tools、Authoritys、Encrypt、NetworkAccessible等 。</p>
<p><strong>Categorys</strong>：公共类别扩展，可按照类属性的不同分为不同的子目录，如View、Datas、Image等。</p>
<p>备注：自上而下的依赖关系</p>
<h2 data-id="heading-15">2. cocoaPod应用</h2>
<p>cocoaPod应用IOS开发者应该都比较熟悉，主要是用关联第三方库与私有组件库，方便版本迭代管理。</p>
<h3 data-id="heading-16">2.1 GitHub第三方库</h3>
<p>CocoaPods详解之-使用篇：<a href="https://blog.csdn.net/meegomeego/article/details/24005567" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/meegomeego/…</a></p>
<h3 data-id="heading-17">2.2 GitLab私有库</h3>
<p>CocoaPod-spec私有库配置：<a href="https://blog.csdn.net/z119901214/article/details/90241251" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/z119901214/…</a></p>
<h1 data-id="heading-18">三、业务组件&组件通讯</h1>
<h2 data-id="heading-19">1. 业务组件</h2>
<p>业务组件主要是指作为一个大的业务模块，单独分离成一个组件的形式，如电商模块、聊天模块、博客等。业务组件之间不存在耦合代码，由组件通讯中间层实现彼此的通讯。</p>
<h3 data-id="heading-20">1.1 组价分层方式</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/472338540c824d50b2b38167feb13eb4~tplv-k3u1fbpfcp-watermark.image" alt="20210224000103415.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过xcworkspace的方式分层，A为主工程，B、C为两个业务模块
目录分层：在主业务目录下，按照不同的业务组件创建不同的目录，业务模块独立，组件之间不直接调用API。</p>
<p>xcworkspace分层：通过xcworkspace的方式，不同的业务模块创建各自的project工程，业务project工程run成功后，将framework引入主工程中。</p>
<p>pod组件分层：以pod-specs的方式引入业务组件，各个业务模块都独立成一个工程，具体可以参考github组件化项目-iOS-Component-Pro</p>
<h3 data-id="heading-21">1.2 组件分层方式的特点</h3>
<ul>
<li>
<p><strong>目录分层</strong>：目录分层比较简单，没有实现真正的代码分割，所以目录与目录直接的类是可以引用的，这样就很依赖于团队开发的规范性。</p>
</li>
<li>
<p><strong>xcworkspace分层</strong>：xcworkspace分层实现了不同业务组件代码的分割，作为framework的形式引入。动态编译的形式引入会影响到编译打包的效率；打包成静态framework的形式引入更新迭代成本比较高，而且不利于cocoaPod的使用。</p>
</li>
<li>
<p><strong>pod组件分层</strong>：实现了不同业务组件代码的分割，又解决了xcworkspace分层影响编译效率与不利于cocoaPod使用的问题，业务组件与基础组件统一使用cocoaPod管理。</p>
</li>
</ul>
<h5 data-id="heading-22">版权声明：本文为CSDN博主「い红尘ぅ秋枫」的原创文章。原文链接<a href="https://blog.csdn.net/z119901214/article/details/109048724" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/z119901214/…</a></h5></div>  
</div>
            