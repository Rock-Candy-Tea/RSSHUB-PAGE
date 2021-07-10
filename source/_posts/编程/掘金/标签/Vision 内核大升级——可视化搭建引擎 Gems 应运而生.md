
---
title: 'Vision 内核大升级——可视化搭建引擎 Gems 应运而生'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a18fb25711784b31bdff19ca606c9d79~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 03:05:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a18fb25711784b31bdff19ca606c9d79~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>近年来，前端领域逐渐掀起了一股低代码热潮，在经历前后数年的迭代演化后，低代码这一领域已是百花齐放，各家方案层出不穷，百家争鸣。在这样的缤纷繁杂的业态中，新一代低代码平台 Vision 及其核心搭建引擎 Gems 横空出世，加入到这场赛跑角逐之中。<br>
我们应该从什么样角度去审视和设计我们的低代码平台？我想可以从业务和技术两个方向来做探讨：<br>
在业务侧，以运营活动页为代表的 C 侧，以管理后台为代表的 B 侧，不同业务形态跨度之大，平台应该如何 cover 不同的业务场景？<br>
在技术侧，页面编辑、版本管理、权限控制、预览发布、业务逻辑等不同能力、不同技术栈的功能被打包在同一个平台，平台应该如何组织和拆分这几者的联系？<br>
本文将围绕 Vision 内核升级、Gems 的诞生，以及可视化搭建的一些典型场景进行阐述 ，对以上问题的解决方案进行探索和讨论，希望能给读者带来一些启发。<br>
本文也是 IMWeb 团队低代码系列的开篇。</p>
</blockquote>
<p>Vision，是在线教育已经打磨了两年多的一站式通用运营平台，旨在帮助产品运营同学高效地完成活动页面的搭建、发布等工作的同时，也帮助业务开发效率和体验的不断提升。Vision 跨过自己的一个个里程碑，截止到今日，除了在线教育的三大业务，也已经支持了部门外业务 18 个。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a18fb25711784b31bdff19ca606c9d79~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在近一年的开发迭代中，Vision 平台也针对活动页运营链路完善了一系列功能，诸如便捷的 AB 实验能力，开箱即用的线上数据透视能力等等。</p>
<p>而另一方面，更接近搭建核心能力的升级，像水平布局、容器无限嵌套、组件间数据访问 等能力却迟迟没有动工。背后的原因在哪？</p>
<h2 data-id="heading-0">一. 问题是什么？</h2>
<p><em><strong>"我们似乎不太知道该从何下手增加这些能力</strong></em> <strong>"</strong>，团队里负责一起维护 Vision 的小伙伴会发出这样的疑问。</p>
<p>作为一个运营提效工具，它提效的方式是提供给运营同学便捷地可视化地搭建落地页的能力，不难发现，Vision 的核心能力就是 <strong>可视化搭建</strong>。</p>
<p>然而，系统的设计是否能直观体现我们的核心能力？能力的边界又在哪？我们是否能清晰地辨析出新能力该在 Vision 的哪个子模块扩展，同时还保持着系统复杂度增长的平稳趋势？我心里也有着这些疑问，而答案几乎都是不明了的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66fc30cf9c374471b6a27f452114b36e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，我们的模块划分是一个常规 web 应用的方式，可视化搭建能力的核心并没有一个直观的形态，模块化的描述与可视化搭建领域的模型之间并没有建立合适的关联。</p>
<p>在这样的设计下，由于缺乏对领域的抽象和基础模块的设计，很多工作都变得困难起来。比如我们想增加渲染协议检查相关的逻辑，我们<strong>需要仔细地阅读大量现有系统的代码，才能找到一个相对合适的切入点</strong>，完成功能的实现。</p>
<p>更让人受阻的是，协议检查这个 <em>涉及渲染流程</em> 的能力落地，甚至<strong>需要同时发生在系统前端和后台的两个涉及渲染流程的模块中，编写类似的代码</strong>。这为系统代码的维护带来了额外的成本。</p>
<p>我们需要一种更理想的设计方式，将 Vision 的核心能力直观地描述出来，将 Vision 系统的软件复杂度的增长压缩在一个可控的速度，从而帮助我们更稳固、高效地进行后续系统的开发与维护。</p>
<h3 data-id="heading-1">来自团队另一类场景的诉求</h3>
<p>另一方面，团队内 B 侧需求量日渐庞大，持续有相当比例的人力投入到管理后台类系统开发中。</p>
<p>这部分系统的重复度很高，都是重表单场景，很多时候就是各类表单的排列组合。同时大部分这类系统是给内部使用，对页面的质量、性能各方面要求相对 C 侧页面还是要稍低一些。这样的重复性与开发要求，持续投入在其中的同学未免会觉得自己的技术成长受限，管理后台页面的开发就好像成了一件苦差，谁都不乐意接。</p>
<p>我们注意到，公司内其实已经存在用于解决管理后台场景的低代码方案，比如 XPage，但是它目前仅在微信支付内部使用。</p>
<p>我们很自然地考虑，是否能扩展 Vision 的系统能力，让其也能够支撑 B 侧场景。但几经推敲和讨论后我们放弃了这个思路。我们认为，运营场景与 B 侧场景在搭建页面的形态与搭建平台使用用户上存在着诸多差异，<strong>如果我们期望在一个搭建平台上解决两类问题，必然存在着一些折中的设计</strong>，为了同时满足两类场景的需求。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5601a1f396394cc4bbdf32f498f02a45~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最高效好用的工具一定是专注于某垂直领域提供深度解决方案的。因此，我们希望在上层建设另一个专注于管理后台系统搭建的平台，在新的平台上针对 B 侧场景提供最适合的产品设计；同时将 Vision 的核心搭建能力下沉，构建一个可视化搭建引擎，在其基础上，扩展更丰富的基础能力以支撑上层多样的应用场景。</p>
<p>Vision 遇到的问题，是软件工程的问题，是控制软件复杂度的问题；而来自团队的 B 侧需求，是产品能力复用的问题，是大框架下系统分层的问题。然而，它们似乎都指引着 Vision 往同一个目的地迈进......</p>
<h2 data-id="heading-2">二. 新的思路</h2>
<p>我们开始将 Vision 系统打碎，开始思考可视化搭建核心能力的边界在哪，可视化搭建核心的抽象可以是怎样的，换句话说，从 Vision 下沉的可视化搭建引擎的具体形态如何。</p>
<p>Vision 平台的产品视图，活动搭建、编辑页面，包含了活动页面编辑、保存、历史管理、权限控制、预览发布等等能力。这其中不少是更适合作为上层平台能力的，比如历史管理、活动发布等。这些都不是我们的引擎想要包含的内容。</p>
<p>如果尝试用一句话来描述核心的搭建能力，那么首先，我们组织页面的方式是基于素材的拼装，然后页面搭建的结果，其实就是对页面组成素材的协议化描述，而页面的渲染，则是对这份描述的解释与执行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b9de58a824b43b5b2cfeb39c119dc18~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们将上面这句话做一些拆解和抽象：</p>
<ul>
<li>我们需要提供对协议的解析与渲染的能力，我们把它叫做渲染器；</li>
<li>协议从哪来呢，我们需要提供可视化组装协议的能力，就叫做编辑器；</li>
<li>协议渲染过程所需对应的素材，那便是素材库；</li>
</ul>
<p><strong>渲染器、编辑器、素材库，三个相对独立的基础库组成了我们的可视化搭建引擎。</strong> 它将作为承载可视化搭建领域核心能力的微内核，成为 Vision 以及上层其它各类贴合业务场景的搭建平台的基石，Gems 应运而生。</p>
<p>除了大模块的拆分，每个模块内部也进行了相当的抽象和设计，下图是一个总览：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbdf48b556894600bb2a01b5f6248d80~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中值得一提的是，编辑器中所见即所得的操作画布（模拟器）所依赖的渲染逻辑，我们统一收敛到了 Renderer，然后<strong>通过编辑器中的 <em>EditableEnhancer</em> 为渲染组件提供编辑上下文特有的交互能力。</strong> 这带来了两个好处。</p>
<ol>
<li>降低了渲染相关逻辑改动的成本，即前面提到的涉及渲染逻辑的改动需要发生在多处的问题不复存在；</li>
<li>减少了模拟器预览效果与最终发布效果的差异，因为渲染代码就是同一份。</li>
</ol>
<p>其它子模块的设计细节这里暂时不展开，后续可能进行系列文章总结，有兴趣的同学可以保持关注。</p>
<h2 data-id="heading-3">三. 新架构下的能力扩展</h2>
<p>在新架构的基础上，我们如愿进行了众多核心能力的扩展。这里从几个具体的场景切入，来看一看 Gems 具体能力项的设计与实现。</p>
<h3 data-id="heading-4">栅格布局</h3>
<p>这里说的栅格布局，主要就是为了解决水平排列素材的场景，该场景在 PC 端页面中较为常见。</p>
<p>原有的能力中，我们拥有普通的容器能力，容器里面可以放子组件。而栅格布局实现的方式则是提供一个栅格布局容器。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bea5f1e814bd4b3494103881ff538268~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，栅格容器看起来就是比普通容器多了几个“坑”，在添加组件时可以选择往哪个坑添加。那么，结合我们的整体架构进行需求分析：</p>
<ul>
<li>Renderer 侧，从<strong>渲染协议</strong>开始看，本质上，栅格容器只需要 <em><strong>一个额外的信息来描述子组件属于哪一个“坑”</strong></em> ；</li>
<li>Materials 侧，从<strong>素材定义</strong>看，栅格容器则比普通容器需要多定义一个信息，那就是 <em><strong>容器需要有多少“坑”。</strong></em></li>
</ul>
<p>其实分析到这，围绕这个“坑”的设计，似乎已经不局限于栅格容器了。所有需要有多个“坑”的容器组件，都可以拥有类似的抽象，像 Tab 组件、Table 组件、模态窗等等。</p>
<p>我们进行了如下的抽象和设计：</p>
<ul>
<li>“坑” => <strong>插槽 => slot</strong>；</li>
<li>一个额外的信息来描述子组件属于哪一个“坑” => 渲染协议扩展，组件描述中增加 slot 字段；</li>
<li>容器需要有多少“坑” => 组件定义中增加 slots() 配置项；</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9dc8dff5df5d430e88498cc0d471eb1a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>到这，我们已经具备了渲染一个多插槽容器的基本条件，剩下的问题来到 Editor，<strong>如何为这种携带插槽的容器赋予编辑态特有的一些 UI 和交互动作</strong>了，也就是让容器里的插槽可以被选中，指定往某个插槽添加子组件等等。</p>
<p>得益于我们 Editor 与 Renderer 的架构设计，我们只需要在 EditableEnhancer 中扩展处理插槽的能力即可，具体的实现形式即为一个高阶组件，大致逻辑如下：</p>
<ul>
<li>将拥有插槽的容器的子组件按 slot 分组；</li>
<li>为分好组的子组件包裹插槽组件，为插槽提供相应的 UI 和交互。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> withSlots = <span class="hljs-function">(<span class="hljs-params">View</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">WithSlots</span>(<span class="hljs-params">&#123; instance, children, ...otherProps &#125;</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123; slots &#125; = instance;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">instance</span>=<span class="hljs-string">&#123;instance&#125;</span> &#123;<span class="hljs-attr">...otherProps</span>&#125; ></span>
        &#123;
          slots(instance).map((slot) => (
            <span class="hljs-tag"><<span class="hljs-name">SlotContainer</span>></span>
              &#123;children.filter((child) => slot === child.props.slot)&#125;
            <span class="hljs-tag"></<span class="hljs-name">SlotContainer</span>></span>
          ))
        &#125;
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
    );
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此我们已经具备了提供栅格布局能力的所有关键要素。</p>
<h3 data-id="heading-5">素材数据联动</h3>
<p>素材间的联动，其实 Vision 原有的设计里已经支持了，主要是借助事件系统实现的一套联动机制。这套联动模式在由明确 UI（事件） 驱动的场景下是很适合的，我们以点击按钮打开弹窗这个场景为例，简单回顾下 Vision 对此的描述方式：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f58e9c1077745fa8e80e54dc616ab1c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>视角转换到我们新面临的B侧场景，我们试一试使用这套模型对常见的表单场景进行描述。</p>
<p>我们假设有一个 Input 提供给用户输入，然后有另外一个 Table 依赖这个 Input 的值进行数据拉取，以及另一个 Text 需要展示 Input 的值。</p>
<p>那么按上述联动动作的思路来完成，我们需要以下几步：</p>
<ol>
<li>首先在 Input 组件上提供一种自定义事件触发，比如 <em>输入变化</em>，同时携带上改动的值；</li>
<li>在 Table 上实现自定义动作（事件监听），比如 <em>更新参数</em>，接收新的参数值并更新组件内部维护的数据；</li>
<li>类似 2，在 Text 上实现自定义动作，比如 <em>更新文本</em>，接收新的文本内容并重新渲染；</li>
<li>在 Input 上配置 <em>输入变化</em> 分别触发 Table 和 Text 的 <em>更新参数、更新文本</em> 动作。</li>
</ol>
<p>模型已经有些复杂了。这里的核心逻辑，Input 其实是作为一个数据的生产者，对应的， Table 和 Text 作为其数据的消费者。可以想象得到，我们需要为每一个拥有数据生产能力的素材，围绕其 UI 行为，实现类似上述步骤 1 的自定义事件触发，将数据发射出来；同时，为每一个拥有数据消费能力的素材（其实可以说是所有素材）实现类似上述步骤 2/3 的自定义动作。而且，当数据消费关系复杂时，上述步骤 4 的搭建配置，成本也是不容小觑的。</p>
<p>显然，联动动作设计背后事件驱动的方式在这个场景下变得不那么适用。我们需要一种数据驱动的模式，我们需要一种组件间能进行数据共享的能力。</p>
<p>我们为素材定义了新的接口能力 ——— <strong>开放数据接口。简单的说，开放数据接口就是一个素材声明的可以被外部（其它素材）访问引用的数据接口声明。</strong> 区别于素材自身的静态数据，该开放数据是一个运行时的动态数据，并不固化于渲染协议中，数据也并不是由页面编辑者在搭建页面时产生。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a25b90f952b4ab88c4959302a70ee47~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图，我们实现上面的表单场景就只需要简单的两步：</p>
<ol>
<li>在 Input 定义可供其它素材访问的数据项；</li>
<li>页面搭建时，在需要消费 Input 数据的地方（此例为 Table 和 Text 的数据配置）通过 Input 的组件 key（实例 id）进行数据引用。</li>
</ol>
<p>整个具体的实现将由三个核心模块的密切配合共同完成：</p>
<ul>
<li>Materials 提供数据接口的定义能力；</li>
<li>Editor 提供快捷配置数据变量及相关提示的组件配置表单能力；</li>
<li>Renderer 提供运行时数据对象的创建、数据分发及变量解析能力。</li>
</ul>
<p>每一个素材（包括组件、动作、插件）都可以定义自己拥有的可被其它素材访问的数据，同时素材数据的更新将会触发依赖侧的更新。最终的效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a05f542911a84149ab9d264ffc526a90~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">组件模板</h3>
<p>在某一些场景下，我们希望一个组件被添加到画布中时能携带一些默认的样式或行为，比如模态窗组件。</p>
<p>首先我们希望它能默认拥有比较常见的 Footer（取消、确定按钮），但我们同样也希望模态窗的 Footer 部分可以相对自由的被定制，那么将 Footer 固化在模态窗实现内不会是一个好的方式。</p>
<p>我们考虑将 Footer 部分作为模态窗的插槽之一，可以自由地置入子组件。所以现在就回到了最初的命题，我们需要一种能力，能够描述组件进入画布时的默认表现。</p>
<p>可以分析得到，这个能力是 Materials 和 Editor 需要关注的。Materials 提供素材默认表现的定义，而 Editor 则负责解析执行该定义，并赋予素材进入画布时以相应的行为。</p>
<p>我们在 Materials 侧为每个组件提供了一种定义 templates 的能力，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdfaa9411aa045719b7f37db61237422~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>针对模态窗的场景，通过 templates 配置，为其定义了两种模板，其中 弹窗（<em>带默认 Footer</em>） 的模板则自动携带了的“确认”、“取消”按钮。Editor 拿到这份组件配置时，则会在组件面板中给出相应的模板以供搭建用户选择。</p>
<p>组件的颗粒度与搭建灵活程度几乎是正相关的。组件颗粒度越细，那么搭建时可自由组合来支撑的页面多样性就越大。但与之而来的，是搭建成本的提高。反之组件粒度越粗，搭起来越简单，而灵活性又受限。</p>
<p>组件模板能力的设计，有效 <strong>缓解了搭建效率与搭建灵活性之间的矛盾</strong> ，在维持细粒度、高灵活性的原子组件的同时，通过预设模板对原子组件进行组合的方式，为高频搭建场景提高了不少搭建效率。</p>
<h2 data-id="heading-7">四. 成果及未来展望</h2>
<p>从 Vision 中诞生出的 Gems，现在<strong>已经成功替代了 Vision 原有的核心逻辑代码</strong>，也为 Vision 带来了新的栅格布局、数据联动等新能力。更重要的是，Gems 让 Vision 的软件复杂度得到了控制，为系统的开发维护工作带来了指引，让一切系统的变更更加有迹可循。</p>
<p>另一方面，基于 Gems，团队内 <strong>专注于管理后台类页面搭建的 Hulk 系统也成功问世并投入实际生产之中</strong>。截止笔者发文，团队内已经在开心鼠排课系统、课堂章鱼哥、课堂人社系统等多个管理系统的页面使用 Hulk 搭建，得到一众好评，节省了大量开发人力。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e91ceaeafef14ccd91d4e9c59b7390f0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
目前 Gems 仍在高速迭代与实践验证中，后续将开放给团队外使用，并逐步开源。届时欢迎大家前来使用、给予宝贵的意见！</p></div>  
</div>
            