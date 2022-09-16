
---
title: 'Android 官方模块化方案解读'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b020c08af564fcba8a366dc66c96486~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
author: 掘金
comments: false
date: Tue, 13 Sep 2022 07:24:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b020c08af564fcba8a366dc66c96486~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Android 官方模块化方案解读</h1>
<h2 data-id="heading-1">前言</h2>
<p>前不久整理下 Now In Android 项目是如何做模块化的（<a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI5NjE4NDkxNQ%3D%3D%26mid%3D2247483826%26idx%3D1%26sn%3D707aff2a896ade824344565373da6c78%26chksm%3Dec497c8edb3ef59827804d74e92ac11b4fef456ba7ca658ad114a3ca7bb12e5ff771efb6f921%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=MzI5NjE4NDkxNQ==&mid=2247483826&idx=1&sn=707aff2a896ade824344565373da6c78&chksm=ec497c8edb3ef59827804d74e92ac11b4fef456ba7ca658ad114a3ca7bb12e5ff771efb6f921&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">Android 官方项目是怎么做模块化的？快来学习下</a>），没想到官方不久前也在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.com%2Ftopic%2Fmodularization" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.com/topic/modularization" ref="nofollow noopener noreferrer">官方文档</a>中更新了模块化相关的章节，下面就一起看一下官方文档中是如何描述 Android App 模块化的。</p>
<h2 data-id="heading-2">概述</h2>
<p>首先思考下，为什么要做模块化或者说如果不做模块化会有什么问题？</p>
<h3 data-id="heading-3">模块化解决了什么问题？</h3>
<p>随着项目以及业务的不断迭代，整个项目中代码数量会不断的增长，在这个过程中代码的可扩展性、可读性都会随着时间的推移而下降。</p>
<p>解决这个问题方式大致有两种，一种是定期 Review 代码架构并做一些防劣化措施，从而保证项目的质量不会随着项目的增长而下降。但是这种方式在需求快速迭代的团队中由于工期及人力投入的原因是很难被执行的。另外就是需要团队中有能够敏锐发现代码劣化倾向的人，从而发起 Review，这个角色通常由技术专家或者是架构师承担。这种方式可操作性并不高。</p>
<p>另外一种解决思路就是将复杂问题拆解成多个小的、简单问题，而对简单问题的处理通常并不需要特别依赖高级人才。这种方式就是分而治之，将大型、复杂问题拆解成一个个小的、简单问题，从而可以做到各个击破。这种方式对应的工程手段之一就是<strong>模块化</strong>。</p>
<h3 data-id="heading-4">什么是模块化？</h3>
<p>模块化简单讲就是把多功能、高耦合的代码逻辑拆散成多个功能单一、职责明确的模块（module）。一个项目模块化后的整体架构大致如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b020c08af564fcba8a366dc66c96486~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注：<code>:app:phone</code> 是模块名，app表示是子目录的形式，具体可以参考我给 Now In Android 提交的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fandroid%2Fnowinandroid%2Fpull%2F241" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/android/nowinandroid/pull/241" ref="nofollow noopener noreferrer">PR 241</a>。</p>
</blockquote>
<h3 data-id="heading-5">模块化有哪些好处？</h3>
<p>模块化的好处有很多，主要集中表现在提高代码库的可维护性和整体质量上。下表总结了主要优势。</p>





















<table><thead><tr><th><strong>优点</strong></th><th><strong>概括</strong></th></tr></thead><tbody><tr><td>多 App复用</td><td>模块化是在多 App 开发中复用代码逻辑的基础。每个模块都是一个独立有效的构建单元。</td></tr><tr><td>严格的访问权限</td><td>模块可以很好做控制代码的可访问性，模块内部私有的逻辑添加 <code>internal</code> 或者 <code>private</code> 修饰。防止代码被其他模块引用而导致的过度耦合。</td></tr><tr><td>可定制的交付</td><td>可以使用动态下发（ <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.com%2Fguide%2Fplaycore%2Ffeature-delivery" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.com/guide/playcore/feature-delivery" ref="nofollow noopener noreferrer">Play Feature Delivery</a> ）功能（注：国内应用商店基本不可用） 。</td></tr></tbody></table>
<p>上述好处只能通过模块化才能实现。以下是不使用模块化也能实现的好处，但模块化可以更好地实现。</p>





























<table><thead><tr><th><strong>优点</strong></th><th><strong>概括</strong></th></tr></thead><tbody><tr><td>可扩展性</td><td>在代码紧密耦合的代码仓库中，一个微小的更改都有可能导致牵一发动全身。一个好的模块化的项目会做到代码解耦（关注点分离原则），从而规避了上述问题。</td></tr><tr><td>负责人</td><td>一个模块可以有一个专门的负责人，负责维护代码、修复错误、添加测试和 CodeReview 。方便代码与人员的双重管理。</td></tr><tr><td>封装</td><td>封装意味着代码的每一部分都应该对其他部分有尽可能少的了解（最少知道原则）。孤立的代码更容易阅读和理解。</td></tr><tr><td>可测试性</td><td>可测试性描述了测试代码的难易程度。可测试代码是可以轻松独立测试组件的代码。小类总比大型类容易测试，依赖少的类总比依赖多的类容易测试。</td></tr><tr><td>构建时间</td><td>模块化可以提升编译速度，例如增量构建、构建缓存或并行构建。</td></tr></tbody></table>
<h3 data-id="heading-6">模块化常见的误区</h3>
<p>任何一项技术都有好坏，模块化也是如此。对模块化使用不当，可能也会引入一些问题。一些常见的问题如下：</p>
<ul>
<li>
<p><strong>太细粒度</strong>：太细粒度就意味着项目中会有很多模块，而多模块又会导致编译耗时以及多模块配置同步的问题；</p>
</li>
<li>
<p><strong>太粗粒度</strong>：太粗粒度就意味着项目中会有很少模块，基本不能完全发挥出模块化的好处；当做这是一个循序渐进的过程，太粗粒度可以是一个开始不应该是一个结束；</p>
</li>
<li>
<p><strong>太复杂</strong>：将项目模块化并不总是有意义的。如果在可预见的未来项目的增长并不明确，保持现状也是一种不错的选择。</p>
</li>
</ul>
<h3 data-id="heading-7">高内聚低耦合原则</h3>
<p>没有适合所有项目的模块化方案。下面讲下模块化开发过程中可以采用的一些一般规则和常见模式。</p>
<p>高内聚低耦合是模块化项目的一种属性。耦合衡量模块相互依赖的程度，内聚衡量单个模块的元素在功能上的相关性。应该争取低耦合和高内聚：</p>
<ul>
<li>
<p><strong>低耦合模块不应该了解其他模块的内部工作原理</strong>，这意味着模块应该尽可能地相互独立，以便对一个模块的更改对其他模块的影响为零或最小。</p>
</li>
<li>
<p><strong>高内聚</strong>意味着模块应该仅包含相关性的代码。在一个示例电子书应用程序，将书籍和支付的代码混合在同一个模块中可能是不合适的，因为它们是两个不同的功能领域。</p>
</li>
</ul>
<p>如果两个模块严重依赖彼此，那么它们实际上应该作为一个系统运行。相反，如果一个模块的两个部分不经常交互，它们可能应该是单独的模块。</p>
<h3 data-id="heading-8">小结</h3>
<p>模块化就是一种将复杂问题拆解成多个简单问题的工程化方案。所以如果你觉得项目还没有那么复杂，引入模块化的收益将没有那么明显。这里的复杂性包括多 App 复用、严格的代码可见性以及 Google Paly 的动态下发（<code>Play Feature Delivery</code>）。当然，如果希望在可扩展性、所有权、封装或构建时间中受益，那么模块化是值得考虑的事情。</p>
<h2 data-id="heading-9">模块的类型</h2>
<h3 data-id="heading-10">App 模块</h3>
<p>应用程序模块是应用程序的入口点。它们依赖于特性（feature）模块，通常提供导航能力。使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2Fbuild%2Fbuild-variants%3Fhl%3Dzh-cn" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.com/studio/build/build-variants?hl=zh-cn" ref="nofollow noopener noreferrer">多渠道打包</a>方案，单个应用程序模块可以编译为许多不同的二进制文件。</p>
<p>如，根据使用用途可以分为正式版本 App、 测试 Demo App，其中正式版本 App 根据其发布平台又可以分为 智能手机、汽车、电视、可穿戴设备等，其依赖关系大致如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5b47e63e954491faca55f7b6e53ce06~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">特性（Feature）模块</h3>
<p>特性是 App 中功能相对独立的部分，通常对包含一个页面或一系列密切相关的页面，例如注册或结帐流程。如果您的应用具有底部栏导航，则很可能每个目的地都是一项功能。</p>
<p>特性模块中一般会包含页面或路由（destinations）。因此，在模块内部需求处理 UI Layer 中相关的内容。特性模块中不必局限于单个页面或导航目的地，可以包含多个页面。<strong>特性模块依赖于数据模块。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b76e18a9fa524978859a822fb09d5583~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">数据（Data）模块</h3>
<p>数据模块通常包含 <strong>Repository</strong>、<strong>DataSource</strong> 和实体类。数据模块主要有三个职责：</p>
<ol>
<li><strong>封装某个领域的所有数据和业务逻辑</strong>：每个数据模块应该负责处理代表某个领域的数据。它可以处理多种相关类型的数据。</li>
</ol>

<ol start="2">
<li><strong>将 Repository 公开为外部</strong> <strong>API</strong>：数据模块的公共 API 应该是 Repository，因为它们负责将数据公开给 App 的其余部分。</li>
</ol>

<ol start="3">
<li><strong>对外隐藏所有实现细节和 DataSource</strong>：DataSource 只能由同一模块的 Repository 访问，对外是隐藏的状态。可以通过使用 Kotlin 的 <code>private</code> 或者 <code>internal</code> 关键字来强制执行此操作。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e80462ff4cf9491184853ca4f3d28b24~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">公共（Common）模块</h3>
<p>公共模块，也称为核心模块或者基础模块，包含其他模块经常使用的代码。以下是常用模块的示例：</p>
<ul>
<li><strong>基础</strong> <strong>UI</strong> <strong>模块</strong>：如果 App 中使用自定义 View 和样式（style），应该考虑将他们统一封装到一个模块中，以便可以复用。也就是大家通常所说的 UI 规范库，这可以使 UI 在不同特性模块之间保持一致。</li>
<li><strong>打点统计模块</strong>：打点统计模块，一般是使用市面上现有的 SDK，当然也有自研的。取决于项目需要。</li>
<li><strong>网络模块</strong>：网络库模块，通常是对三方网络库（如 OhHttp）的封装，简化自定义配置时，减少不必要的重复代码。</li>
<li><strong>工具模块</strong>：工具类，也称为帮助类，通常是在应用程序中重用的小段代码。如文件读写、电子邮件验证器或自定义运算符等。</li>
</ul>
<p>App 模块化整体汇总形式大致如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd567603d9d945949cd26a7aa2ac9c46~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>\</p>
<h2 data-id="heading-14"><strong>模块间通信</strong></h2>
<blockquote>
<p>注：此部分结合自身经验以及官方文档整合而得，请批判性观看。</p>
</blockquote>
<p>项目虽然采用了模块化方式进行开发，减少了代码之间的耦合，但是模块间的通信仍是不可避免的事情。模块间相互依赖的方式在工程上并不可行，Android 项目并不允许模块间的相互依赖。通常的做法就是引入第三个中介模块，模块间通过中介模块来进行通信。</p>
<p>中介模块在依赖形式上有可以分为两种，一种是向下抽象，抽离出两个模块共有的数据层逻辑，模块通过回调或者是数据流的方式监听逻辑的变化；另一种形式是抽象，在宿主 App 模块中组合拼装两个模块的逻辑。前者是下沉逻辑，后者是控制反转。</p>
<p>下面我以一个简单的业务场景举例：在购书籍列表页面，选择特定的一本书并下单购买。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0342957da272418195285ecbe6b6c4fa~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">抽离基础模块</h3>
<p>大致流程如下：</p>
<ol>
<li>分别在 <code>:feature:home</code> 与 <code>:feature:checkout</code> 设置对基础依赖模块的初始化操作，如接口实现、回调监听等；</li>
</ol>

<ol start="2">
<li>在 <code>:feature:home</code> 模块内通过依赖的 <code>:data:books</code>模块，调用其 <code>navigate()</code> 方法跳转至 <code>:feature:checkout</code> 模块；</li>
</ol>

<ol start="3">
<li>在 <code>:feature:books</code> 模块内将跳转事件通过 <code>onNavigationBook</code> 分发出去，由 <code>:feature:checkout</code>模块模块实现；</li>
<li><code>:feature:home</code> 模块通过 <code>:data:books</code>模块提供的 <code>onPaymentCanceled()</code> 回调来监听对应的结果；</li>
</ol>

<p>这种通讯方式随着业务的迭代，底层通用的数据模块会不断膨胀，耦合也会越加严重，所以并不建议使用此方式。官方文档中示例方式则是交由调用者处理，各自模块也相对内聚。</p>
<h3 data-id="heading-16">依赖调用者模块</h3>
<p>这种方式一般是依赖 app 模块来组装各个业务模块的业务逻辑，也就是一样意义上的胶水代码。大致方式如下：</p>
<ol>
<li><code>:app</code> 模块调用 <code>:feature:home</code>提供的 navigate 函数跳转至 <code>home</code> 页面，并通过 onCheckout 函数将对应的结果回调出去；</li>
<li><code>:app</code> 模块监听到 <code>onCheckout()</code> 回调后，调用 <code>:feature:checkout</code>模块提供 navigate 函数进行跳转，并通过 <code>onPaymentCanceled()</code> 回调将结果抛出；</li>
</ol>

<p>此种方式使得各业务模块的逻辑更加内聚，虽然这种方式的结果及事件也能很好的暴露出去。但是如果这种方式在大型项目中使用时会导致产生大量的胶水代码（频繁的初始化以及 Callback 设置），不利于项目中后续迭代。为了解决胶水代码问题，可以在项目中引入依赖管理的框架。</p>
<h3 data-id="heading-17">依赖管理框架</h3>
<p>依赖管理不仅可以很好地解决对象繁琐的初始化逻辑，还可以很好的实施控制反转的编码思想。目前主流的依赖管理的方案有两种，分别为依赖注入与服务查找：</p>
<ol>
<li>
<p><strong>依赖注入</strong>：依赖注入使类能够定义其依赖项而不构造它们。在运行时，另一个类负责提供这些依赖项。一般是使用注解方式，适合大中型项目，如 <strong>Hilt</strong>；</p>
</li>
<li>
<p><strong>服务查找</strong>：服务查找的方式一般是维护一个注册表，所需的依赖都可以在这个注册表中查找；一般是使用相对简单，适合中小型项目，如 <strong>koin</strong>；</p>
</li>
</ol>
<p>官方推荐使用 <code>Hilt</code> 来进行依赖管理，如果你的项目中在使用其他的依赖管理方式，并且没有遇到问题的话，那么继续使用当前的框架即可。</p>
<p>依赖管理的方式不仅可以使用模块间通信，在模块内部通信也是一种很好的解耦与复用的手段，只是在模块间通信会流程变得更加复杂，也更能突出依赖管理的重要性。整个依赖管理在模块化整体架构大致如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f19725f041e48cd9b8209a035bc9449~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以服务查找方式实现，其大致流程（忽略模块内通讯）如下：</p>
<ol>
<li>数据层可以将对应的数据注入到 DI 容器中；</li>
<li>在特性模块中可以获取到数据层提供的数据，同时也可以将自身的数据注入到 DI 中；</li>
<li>在 app 模块获取所需的数据或特性功能；</li>
</ol>
<h3 data-id="heading-18">小结</h3>
<p>其实整个模块间的通信可以按照其行为方式分为两大类，一种是不同模块间页面直接的跳转，另一种则是不同模块间的数据交互。</p>
<p>对于前者有各种路由框架，Android 官方也提供了 Navigation 库；对于后者也有不少框架，如 Dagger2、Koin，Android 官方也提供了 hilt 库；当然社区中也有两者都能满足的库，如阿里的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2FARouter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/ARouter" ref="nofollow noopener noreferrer">ARouter</a>。</p>
<p>官方文档中只是提到了比较原始的方式，也是对初学者比较友好的方式。大家可以根据自己项目中的现状选择适合自己的即可。</p>
<h2 data-id="heading-19">最佳实践</h2>
<p>虽然开发模块化 App 没有唯一正确的方式，但是以下的一些建议仍可以使代码更具可读性、可维护性和可测试性。</p>
<h3 data-id="heading-20">保持配置一致</h3>
<p>每个模块都会引入配置开销。当模块数量达到某个阈值，则管理一致的配置将成为一项挑战。下面的配置可以减少这部分的工作量：</p>
<ul>
<li>使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.gradle.org%2Fcurrent%2Fuserguide%2Fplatforms.html%23sub%3Aversion-catalog" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.gradle.org/current/userguide/platforms.html#sub:version-catalog" ref="nofollow noopener noreferrer">version catalog</a> 来来统一各模块中依赖的版本号；</li>
</ul>

<ul>
<li>使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.gradle.org%2Fcurrent%2Fsamples%2Fsample_convention_plugins.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.gradle.org/current/samples/sample_convention_plugins.html" ref="nofollow noopener noreferrer">约定插件</a> 在模块之间共享 <code>build.gradle</code> 中的构建逻辑。</li>
</ul>
<h3 data-id="heading-21">尽量少暴露</h3>
<p>模块的公共接口应该是最小的，并且仅仅只公开必需公开的。它不应该在外面暴露任何实现细节。尽可能的缩小外部调用者的可访问范围，使用 Kotlin 的<code>private</code>或<code>internal</code> 可以很好的做到这一点。在模块中声明依赖项时推荐使用<code>implementation</code>，而非<code>api</code>。<code>implementation</code>不会透传依赖，从而可以做到缩短构建时间。</p>
<h3 data-id="heading-22">尽量使用 Kotlin 和 Java 模块</h3>
<p>Android Studio 支持三种基本类型的模块：</p>
<ul>
<li><strong>应用程序模块</strong><code>AndroidManifest.xml</code>是您的应用程序的入口点。它们可以包含源代码、资源、资产和. 应用模块的输出是一个 Android App Bundle (AAB) 或一个 Android 应用程序包 (APK)。</li>
</ul>

<ul>
<li><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2Fprojects%2Fandroid-library%3Fhl%3Dzh-cn" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.com/studio/projects/android-library?hl=zh-cn" ref="nofollow noopener noreferrer">库模块</a></strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.com%2Fstudio%2Fbuild%2Fdependencies%3Fhl%3Dzh-cn" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.com/studio/build/dependencies?hl=zh-cn" ref="nofollow noopener noreferrer">依赖项</a>与应用程序模块具有相同的内容。它们被其他 Android 模块用作依赖项。库模块的输出是一个 Android Archive (AAR)，在结构上与应用程序模块相同，但它们被编译为一个 Android Archive (AAR) 文件，以后可以被其他模块用作。库模块可以在许多应用程序模块中封装和重用相同的逻辑和资源。</li>
</ul>

<ul>
<li><strong>Kotlin 和 Java 库</strong>不包含任何 Android 资源、资产或清单文件。</li>
</ul>
<p>由于 Android 模块会带来开销，因此您最好尽可能使用 Kotlin 或 Java 类型。</p>
<h2 data-id="heading-23">总结</h2>
<p>以上内容是根据官方文档整理而得，对部分内容做了结构调整、重新绘制了 UML 图以及添加了些自己的经验感悟。对原文整理会存在疏忽遗漏的部分，请大家到官方文档中查看，做到“交叉验证”。</p>
<p>如果你想快速搭建一个全新的 Android 模块化项目，可以到 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmadroidmaq%2Farchitecture-templates" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/madroidmaq/architecture-templates" ref="nofollow noopener noreferrer">architecture-templates</a></strong> 仓库中 clone，可以说是非常便捷了。</p>
<p>虽然模块化技术在国内并算不上什么新技术了，但是我仍然看到了一些积极的影响：</p>
<ul>
<li>对于初学者而言，有一套相对详细指导文档并且完整示例的项目（Now in Android）可以参考，从而可以快速搭建模块化的项目；</li>
<li> 对于已经实践过模块化项目团队，我相信仍能从官方文章中学习到一些新思路及方法，以复盘的视角审视自己团队中的模块化方案的优劣；</li>
</ul>
<p>当然，模块化本身并不是终点。模块化之后还有组件化，组件化之后还有壳工程和动态化。每个技术阶段对应到团队发展的阶段，那些适合目前团队现状的技术才是”好“技术。</p></div>  
</div>
            