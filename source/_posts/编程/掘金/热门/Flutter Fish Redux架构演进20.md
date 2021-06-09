
---
title: 'Flutter Fish Redux架构演进2.0'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/357524e10f2145fd94786f2403197f2b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 22:43:55 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/357524e10f2145fd94786f2403197f2b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：闲鱼技术——啊丘</p>
<p>Fish-Redux开源以来，已经在闲鱼核心链路上做了大量验证。从初期的宝贝详情页，发布页面开始，Fish-Redux在闲鱼的使用程度逐渐提高。Fish-Redux框架的使用极大提升了复杂页面场景下的开发效率。特别是通过框架提供的组件复用和状态管理能力，我们大幅降低了代码冗余也简化了页面复杂度。​</p>
<p>然而随着页面复杂度的不断提升，现有能力已无法支撑新业务场景的述求。特别是对</p>
<p>•页面编排•动态AB•灵活性不足</p>
<p>于是我们基于Fish-Redux现有框架做了新一轮架构演进。通过对现有适配器能力的升级，进一步提高了架构的灵活性。Fish-Redux的2.0版本正式诞生！​</p>
<p>​</p>
<h2 data-id="heading-0">闲鱼Fish-Redux现状</h2>
<p>Fish-Redux已经在闲鱼核心链路大量落地。Fish-Redux核心收益如下：​</p>
<p>1.组件复用</p>
<p>以闲鱼的商品详情页开发为例。以核心的服务类型商品和交易类型商品为基础。借助Fish-Redux框架，我们衍生出了普通宝贝，租赁宝贝，玩家号宝贝等10多个宝贝详情页面。这些不同类型的详情页面，不仅有自己独立的业务模块，也最大可能的复用了共同的组件模块。</p>
<p>2.状态管理</p>
<p>在发布这种强交互场景开发中，我们使用Fish-Redux高效管理了大量的页面事件，极大提升了组件通信的效率。繁多的业务场景下也保证得了逻辑组件化。</p>
<p>3.代码结构管理</p>
<p>Fish-Redux为我们提供了很好的文件代码规范。这保证我们在开发的时候，无论是代码风格还是项目结构，都有着高度一致性。发布链路我们多人参与开发，负责对应的模块，针对对应的组件部分进行开发。特别是人员流转以后，可以快速上手，这极大的提高了多人协同开发的效率。</p>
<p>​</p>
<h2 data-id="heading-1">Fish-Redux面临的挑战</h2>
<p>​</p>
<p>需要保持Fish-Redux的特性前提下暴露出动态编排能力的Adpater，满足上诉能力才能支撑为未来所需要的业务场景。​</p>
<p>简单介绍下目前adapter所存在的一些短板和不足：​</p>
<h3 data-id="heading-2">已有静态编排：StaticFlowAdapter</h3>
<pre><code class="copyable">StaticFlowAdapter(&#123;
    @required List<Dependent<T>> slots,
    Reducer<T> reducer,
    Effect<T> effect,
    ReducerFilter<T> filter,
  &#125;)

  （Dependent = connector + component）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>FlowAdapter由Dependent数组决定页面展现顺序。 页面的展示顺序直接取决于 solts，并且能直接控制各个自组件之间的数据流转，利用这一点优势去编写复杂页面，各种数据分治的逻辑，很大程度的提高来代码的可维护性。 这种形式也存在某些弊端，我们无法对slots动态的进行修改，缺失动态编排能力。​</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/357524e10f2145fd94786f2403197f2b~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="null" loading="lazy" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-3">已有动态编排：DynamicFlowAdapter</h3>
<pre><code class="copyable">    final Map<String, AbstractLogic<Object>> pool;
  final AbstractConnector<T, List<ItemBean>> connector;

  DynamicFlowAdapter(&#123;
    @required this.pool,
    @required this.connector,
    ReducerFilter<T> filter,
    Reducer<T> reducer,
    Effect<T> effect,
    @deprecated Object Function(T) key,
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>DynamicFlowAdapter提供的核心入参是“pool”，“connector”。pool 提供的adapter的组件池，connector提供组件key，state。从列表组件静态展示转变为数据源动态控制页面列表UI。多组件，重复展示的列表提供来便利。​</p>
<p>DynamicFlowAdapter也存在一些不便的地方，所有的组件数据处理都归一到了一个connector之中，Fish-Redux数据分治的亮点就难以得到体现。对于我们去编写复杂动态页面列表也不是很方便。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33eecedebae540d8af96aa35e8862509~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<p>无论是StaticFlowAdapter还是DynamicFlowAdapter都无法同时满足动态编排加上数据分治的特性，我们对Fish-Redux做了进一步的演进。​</p>
<h2 data-id="heading-4">Fish-Redux演进：</h2>
<p>​</p>
<p>第一个版本是基于Fish-Redux的能力我们做了一层脚手架 effective_redux，针对我们上诉的需求对于DynamicFlowAdapter进行包装（组件注册+数据源处理）完成了data映射component逻辑，实现了对应的动态编排能力。</p>
<p>1.脚手架中内置了一些了通用基础模版，动态模版，列表模版等，来支持一些紧急的业务需求。2.对fish redux做了ListAdapter功能增强，提出了Section的概念。来满足对数据不同数据集合类型展示的需求</p>
<p>但是做完第一个版本后引发了一些思考：​</p>
<p>1.动态编排能力是否使用fish redux的用户也需要2.针对页面改动修改了页面框架的外观是否增加学习成本，开发人员的不习惯3.技术带动业务发展，业务需求是否能反补技术框架能力等</p>
<p>第二个版本我们决定将部分能力反补至fish redux中。经过一些思考和目前存在的Adapter一些功能实现对比，总结了目前我们能反补到fish redux的能力部分。并且统一化了FlowAdapter，同时提供了动态编排的能力。</p>
<h3 data-id="heading-5">改进后的编排：FlowAdapter</h3>
<p>Dependent = connector(数据描述)+component(UI描述配置)</p>
<p>重新思考了Adapter的核心思想：Dependent集合的中转站，处理集合内的数据流转，组件的刷新逻辑。同时将处理后的集合转换成UI界面特定数据。​</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dafd4d4f94e3410eb3f66e8d1e7f5522~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="null" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>动态编排实现： FlowAdapater不再以静态的形式获取组合的Dependent列表，由静态参数List 转变为 FlowDependencies 获取的动态回调。 我们可以在FlowDependencies中做一系列扩展，例如页面展示动态编排，组件的AB功能等等。​</p>
<p>分治数据特性： 动态获取的List为connector+component的数据集合，不再是单一的做数据映射UI的逻辑处理，将真正的数据处理过程交回到各个connector中，保持了adapter内组件的数据处理分治特性。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df187f1988024644a93cc8a3fff696de~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="null" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eeafcb14695349fe9b897a28cc4e98cd~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然我们也做了adapter的规整。上诉介绍的两种adapter其实我们会发现内部的实现逻辑是保持不一致的，static adapter， dynamic adapter真正去处理组件集合的拉平逻辑是不同的。​</p>
<p>针对这种我们把StaticFlowAdapter，DynamicFlowAdapter功能实现迁移至我们的新版FlowAdapter中。保证Adapter能力实现一致，外观保持一致，降低学习成本，也能统一做一些性能上的优化。​</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d5dc8c976c243d580bdf1586a384fda~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="null" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/979ae699553741eaa7334d378b4aa9a4~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">效果展示：</h2>
<p>fish redux完成架构升级后，我们的详情&发布链路做了对应的代码修改。​</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8c45770ef6246849dfaf52f1cf19439~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="null" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c62f40bc003d44b3b8b56fdda5fc5e25~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<p>内置模版注册，根据服务端下发的配置信息决定页面的编排顺序。基于框架提供出对应的动态编排能力，我们能做到我们提出的一些业务可能性。​</p>
<p>【动态编排能力】我们的编排顺序，展示数据是由服务端返回的配置信息数据决定的。也就是说页面的展示是有服务端确定的。我们后续对模块之间的顺序调整不再依赖于客户端本地修改后进行发包修改。同时我们也做了对应数据一场的兜底方案，标准的页面展示顺序。​</p>
<p>【组件AB能力】组件AB的能力可以交付到服务端前置处理，同时也可以本地代码中增加动态替换的代码，根据不同的配置分桶做一些定制化的处理​</p>
<p>【动态模版】动态模版的增加为了满足产品快速验证某个业务模块是否可行，直接线上做测试校验，不需要客户端发版本。</p>
<p>​</p>
<p>详情的效果展示：基于价格模块的位置调整，上下架进行了一些尝试。我们能很快的进行一些线上调整动作。​</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0be8c5f21b38496289ef2db62d66711e~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="null" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>​</p>
<p>​</p>
<h2 data-id="heading-7">展望：</h2>
<p>这次我们针对fish redux的adapter做规整，对于编排数据获取的思路转变，更加明确了adapter的功能职责。在根本之处对adapter做了优化处理，更加适应业务场景。此次的优化修改后续会合并至fish redux release之中，为大家带来更多的使用便捷之处。</p>
<p>基于这次框架的演进，为我们带来了fish redux针对不同容器下更多的思考，我们不单单只满足于普通列表的adapter适配，fish redux针对不同容器展示，我们也在着手准备。对于瀑布流场景或者其他的容器内也能有很好的落地。也会在fish redux层面做出一些对PowerScrollView的适配。</p>
<p>对于一些业务的解决方案，动态模版，AB能力我也期望输出到fish redux的扩展包中，不单单解决框架层面的一些问题，最终是一个框架平台的形式让使用者更加简易。对fish redux的能力扩展也是我们后续的一个重要命题。​</p>
<p>最后，欢迎大家积极尝试fish redux，并在社区中发出声音，提出问题或者改进建议，以及贡献代码。我们相信未来fish redux会在更多的场景，能力上使用出现在屏幕上，让大家感受到fish redux的美妙之处。</p></div>  
</div>
            