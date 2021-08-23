
---
title: 'vivo商城计价中心 - 从容应对复杂场景价格计算'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae1e424a3f2a4c369945935299138a15~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 19:20:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae1e424a3f2a4c369945935299138a15~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、背景</h1>
<p>随着vivo商城的业务架构不断升级，整个商城较为复杂多变的营销玩法被拆分到独立的促销系统中。</p>
<p>拆分后的促销系统初期只是负责了营销活动玩法的维护，促销中最为重要的计价业务仍然遗留在商城主站业务中，且由于历史建设问题，商城核心交易链路中商详页、购物车、下单这三块关于计价逻辑是分开独立维护的，没有统一，显然随着促销优惠的增加或者玩法的变动，商城侧业务重复开发量会显著加大。</p>
<p>促销系统的独立，计价相关业务能力从业务边界上也应由促销系统提供，因此促销侧需要从头开始设计促销计价相关能力。</p>
<h1 data-id="heading-1">二、原有计价业务</h1>
<h2 data-id="heading-2">2.1 计价业务场景</h2>
<p>商城原有涉及到计价业务的主要是商详页、购物车、确认下单、提交订单这几个业务场景。</p>
<p>如果将每一个影响最终售卖价的优惠叫做计价因子的话，那前述几种场景下对于售卖价有影响的计价因子归为三大类：</p>
<ul>
<li>
<p>优惠活动（单品优惠、订单优惠）</p>
</li>
<li>
<p>优惠券（优惠券、代金券）</p>
</li>
<li>
<p>虚拟抵扣（积分、换新鼓励金）</p>
</li>
</ul>
<p>对于每种计价场景与计价因子有如下关系：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae1e424a3f2a4c369945935299138a15~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">2.2 原有计价模型</h2>
<p>对于具体执行的计价业务中各计价因子间是有一定的先后优先级关系的，综合如下图所示，也在一定程度说明了原有计价业务模型：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3ca5e95469540daab30cced4845b7ec~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">三、促销计价模型</h1>
<h2 data-id="heading-5">3.1 分层模型</h2>
<p>促销系统从零搭建基础计价能力，对于系统的稳定性及扩展性必须有一定的保障，而这也就对于促销系统的计价模型提出了一定的要求，通用的基础计价模型最好是能有过一定的实践经历验证过的，因此我们采用了传统电商久经考验的计价模型：分层计价。</p>
<p>所谓的分层计价即传统电商中优惠涉及的三个层面：商品级、店铺级、平台级，正常情况下<strong>不同级别的优惠默认是可以叠加的，同一级别的优惠默认情况下是互斥的</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37ebf52d412d4c5c8a1c1046bffb3d13~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里需要说明的是，每一层级的优惠计算的时候，对于有些优惠的门槛条件是否满足需要依赖原价，<strong>默认情况下依赖于上一个层级的优惠计算后的价格</strong>，即商品级优惠计算依赖商品原价，店铺级优惠依赖于商品级优惠计算后的价格，平台级优惠依赖于店铺级优惠计算后的价格。</p>
<h4 data-id="heading-6">叠加规则特别说明：</h4>
<p>正常优惠叠加是指两个优惠可以同时享受，对于不同层级的优惠默认就是叠加的，对于同一层级的优惠默认是不叠加的，比如正常情况下，优惠券下的各种类型券是只能用一张的。</p>
<p>但某些场景下，业务上会指定同一层级的优惠可以叠加使用的，同时指定叠加使用的场景下还会分为普通叠加和并行叠加，举个例子：订单优惠和优惠券这两个类型的叠加就属于普通叠加（优惠券门槛是否满足的判断取决于订单优惠后的价格），优惠券和代金券的叠加属于并行叠加（优惠券和代金券的门槛是否满足的判断都取决于这两者的前序优惠后的价格）。</p>
<p>对于同一层级的优惠按不同维度分为：<strong>必选/勾选、可叠加(并行叠加/普通叠加)/不可叠加</strong> 。</p>
<h2 data-id="heading-7">3.2 新的计价模型</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3af762b0c8654b659193d71076f0442d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">3.3 核心计价流程</h2>
<h3 data-id="heading-9">3.3.1 主流程</h3>
<p>通过前述计价模型可以得知，在计算优惠价时的先后顺序是：商品级(CalcItem)、店铺级(CalcShop)、平台级(CalcGroup)，另外根据一些特殊业务场景，增加了可能的中断业务逻辑(CalcInterrupt)，因此可得到下图所示的最粗粒度的计价流程;</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82ef47eb94a143c2ba4a26c99bf7e629~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那这三个级别的计算优惠价内部又是如何实现的呢？经过业务抽象，这三个级别的计算可以变成一个通用的计算优惠逻辑，仅有优惠级别的区分。</p>
<h3 data-id="heading-10">3.3.2 通用流程</h3>
<p>经过业务抽象发现三个级别的优惠计算的通用逻辑：</p>
<ul>
<li>
<p>获取当前层级的优惠查询器（Get Current Level PromotionGetter）</p>
</li>
<li>
<p>过滤优惠查询器（Filter PromotionGetter）</p>
</li>
<li>
<p>查询优惠（Get Promotion）</p>
</li>
<li>
<p>过滤优惠（Filter Promotion）</p>
</li>
<li>
<p>通过计价引擎计算优惠（Calc Engine）</p>
</li>
<li>
<p>过滤计价结果（Filter CalcResult）</p>
</li>
</ul>
<p>因此我们得出如下的通用的计价流程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/455aa4a64ce94522a3224525578a1e4f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通用计价流程中的又有几个相对灵活的与业务相关过滤逻辑，从后面的细节流程中可以了解更多的实现。</p>
<h3 data-id="heading-11">3.3.3 细节流程</h3>
<p>之所以在通用计价流程中会有几个过滤节点，是因为在业务上会有一些特殊的过滤逻辑，比如商详页来源的时候，只能使用商品级优惠查询器，某个优惠只能特殊渠道去享受等等。</p>
<p>所以需要抽象出一个通用的可扩展的过滤机制来实现业务需求，因此会按照不同维度去定制一些链式过滤器，执行流程如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4091f63874349e8b548b84fb8bd9cea~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然图中所示的不同维度额过滤器只是目前业务中的一部分，比如还有按照终端、付款方式、外部业务方等等，这些在具体实现的时候可以非常灵活的支持。</p>
<p><strong>那上述过滤器是如何制定？以及与业务如何关联的？</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/962293281cad4b5ab350597c5be07a62~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中列出部分业务定制过滤序器，自定义过滤器后会自动注册到统一的优惠业务过滤器工厂中，在前述的计价流程中，需要用到相关过滤器时，只需带上相关上下文参数可以自动从过滤器工厂中获取匹配的过滤器。</p>
<h3 data-id="heading-12">3.3.4 完整全流程</h3>
<p>把前面这一系列流程中进行一个组合拼装，就可以得到计价的完整全流程图，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6607011b3d3a4db19dec2b3f429453fa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从这个完整流程图中，可以看到一个通用稳定的核心计价流程以及一个支持业务多变的定制过滤器，既保证了核心的稳定，又保留灵活的扩展。</p>
<h1 data-id="heading-13">四、系统核心设计</h1>
<p>在通用的计价执行流程中一个节点是「Calc Engine」，也就是计价引擎，这是整个计价逻辑中最核心底层的能力，由它来判定每个优惠是否能被用户享有。</p>
<h2 data-id="heading-14">4.1 统一优惠模型</h2>
<p>由于计价中心在建设的时候，已经存在了促销系统中的各个优惠活动、独立的优惠券及代金券、遗留在商城主站的未迁移的优惠，因此想用兼容这么多的优惠类型，必然需要建立一个统一的优惠模型，而在建设过程中需将现有的优惠模型进行适配转换至统一模型。</p>
<p>统一优惠模型中的一些关键信息有：优惠标识、优惠类型、优惠模板id、开始结束时间、优惠参数及一些扩展参数等。</p>
<h2 data-id="heading-15">4.2 优惠模板</h2>
<p>1）在进行促销计价时，每个具体的优惠都会对应一个唯一的优惠模板，每个优惠模板本质上是一个JSON字符串，只是这些JSON字符串是由遵循了一定特殊逻辑规则的元信息数据转化而成，而这些元信息在被计价引擎解释执行时，都是返回布尔类型标识是否通过。</p>
<p>2）基本的元信息数据有这几种：</p>
<p>**AndMeta(与）**对应逻辑关系中的“与”关系，表示该类型的元信息所包含的子元信息解释执行都返回真才为真；</p>
<p>**OrMeta(或）**对应逻辑关系中的“或“关系，表示该类型的元信息所包含的子元信息任一解释执行返回真就为真；</p>
<p>**NotMeta(非）**对应逻辑关系中的“非”关系，表示该类型中元信息所包含的子元信息解释为假当前元信息为真；</p>
<p>**ConditionalMeta(条件）**如果条件参数不存在或者从上下文获取参数指定的布尔值不为true，则当前元信息返回真，否则根据元信息中包含的子元信息解释执行的结果作为当前元信息执行结果；</p>
<p>**ComplexMeta(组合元信息）**该元信息作为所有模板的通用载体，该元信息中包含两个重要信息conditon、action，两者的关系是只有condition条件都满足后后，才会去执行后续的action，而condition和action都可能为前述中的各种元信息的复杂组合。</p>
<p>3）模板元信息关系：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c58750622c347ba9f62aa36a13e01bf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>4）优惠模板示例：</p>
<pre><code class="hljs language-java copyable" lang="java">&#123;
  <span class="hljs-string">"type"</span>: <span class="hljs-string">"COMPLEX"</span>,
  <span class="hljs-string">"condition"</span>: &#123;
    <span class="hljs-string">"type"</span>: <span class="hljs-string">"AND"</span>,
    <span class="hljs-string">"metas"</span>: [
      &#123;
        <span class="hljs-string">"type"</span>: <span class="hljs-string">"CONDITIONAL"</span>,
        <span class="hljs-string">"metas"</span>: [
          &#123;
            <span class="hljs-string">"type"</span>: <span class="hljs-string">"CONDITION"</span>,
            <span class="hljs-string">"metaCode"</span>: <span class="hljs-string">"terminalCheckCondition"</span>
          &#125;
        ],
        <span class="hljs-string">"param"</span>: <span class="hljs-string">"needTerminalCheck"</span>
      &#125;,
      &#123;
        <span class="hljs-string">"type"</span>: <span class="hljs-string">"CONDITION"</span>,
        <span class="hljs-string">"metaCode"</span>: <span class="hljs-string">"amountOverCondition"</span>
      &#125;
    ]
  &#125;,
  <span class="hljs-string">"action"</span>: &#123;
    <span class="hljs-string">"type"</span>: <span class="hljs-string">"AND"</span>,
    <span class="hljs-string">"metas"</span>: [
      &#123;
        <span class="hljs-string">"type"</span>: <span class="hljs-string">"ACTION"</span>,
        <span class="hljs-string">"metaCode"</span>: <span class="hljs-string">"cutPriceAction"</span>
      &#125;,
      &#123;
        <span class="hljs-string">"type"</span>: <span class="hljs-string">"ACTION"</span>,
        <span class="hljs-string">"metaCode"</span>: <span class="hljs-string">"freezeCouponAction"</span>
      &#125;
    ]
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">4.3 计价引擎</h2>
<p>计价引擎本质上就是对应优惠模板的解释执行，并配合相关上下文，进行优惠计算，关键代码如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">executeMeta</span><span class="hljs-params">(Meta meta, EngineContext context)</span> </span>&#123;
    <span class="hljs-keyword">if</span> (meta <span class="hljs-keyword">instanceof</span> AndMeta) &#123;
        <span class="hljs-keyword">return</span> executeAndMeta((AndMeta)meta, context);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (meta <span class="hljs-keyword">instanceof</span> OrMeta) &#123;
        <span class="hljs-keyword">return</span> executeOrMeta((OrMeta) meta, context);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (meta <span class="hljs-keyword">instanceof</span> NotMeta) &#123;
        <span class="hljs-keyword">return</span> executeNotMeta((NotMeta)meta, context);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (meta <span class="hljs-keyword">instanceof</span> ComplexMeta) &#123;
        <span class="hljs-keyword">return</span> executeComplexMeta((ComplexMeta)meta, context);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (meta <span class="hljs-keyword">instanceof</span> ConditionalMeta) &#123;
        <span class="hljs-keyword">return</span> executeConditionalMeta((ConditionalMeta)meta, context);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> executeIMeta(meta, context);
    &#125;
&#125;
 
......
 
<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">executeComplexMeta</span><span class="hljs-params">(ComplexMeta complexMeta, EngineContext context)</span> </span>&#123;
    Meta condition = complexMeta.getCondition();
    Meta action = complexMeta.getAction();
    <span class="hljs-keyword">return</span> executeMeta(condition, context) && executeMeta(action, context);
&#125;
 
<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">executeConditionalMeta</span><span class="hljs-params">(ConditionalMeta conditionalMeta, EngineContext context)</span> </span>&#123;
    PromotionContext promotionContext = context.getPromotionContext();
    <span class="hljs-keyword">if</span> (promotionContext == <span class="hljs-keyword">null</span> || promotionContext.getParameters() == <span class="hljs-keyword">null</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
    &#125;
 
    String conditionParam = conditionalMeta.getParameter();
    String sNeedProcess = promotionContext.getParameters().get(conditionParam);
    <span class="hljs-keyword">if</span> (sNeedProcess == <span class="hljs-keyword">null</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
    &#125;
 
    <span class="hljs-keyword">boolean</span> needProcess = Boolean.parseBoolean(sNeedProcess);
    <span class="hljs-keyword">if</span> (needProcess) &#123;
        <span class="hljs-keyword">return</span> executeMeta(conditionalMeta.getMetas().get(<span class="hljs-number">0</span>), context);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
    &#125;
&#125;
 
<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">executeIMeta</span><span class="hljs-params">(Meta meta, EngineContext context)</span> </span>&#123;
    IMeta iMeta = MetaFactory.get(meta.getMetaDef().getMetaCode());
    <span class="hljs-keyword">if</span> (iMeta == <span class="hljs-keyword">null</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> CalcException(<span class="hljs-string">"meta not found, metaCode="</span> + meta.getMetaDef().getMetaCode());
    &#125;
 
    <span class="hljs-keyword">return</span> iMeta.execute(context);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-17">五、小结</h1>
<p>通过前面几章内容的描述，我们基本把vivo商城促销系统建设计价中心的关键思路阐述完了。建设完计价中心后，整个促销系统的核心基础才立住，但这也只是个开始，整个商城围绕着促销计价中心仍然还有其他待建设的内容，比如整个商城的营销价格能力矩阵，价格监控，商城时光机等等，而这些内容我们后续有机会也会陆续输出相关文章，与大家一起交流学习。</p>
<blockquote>
<p>作者：vivo互联网服务器团队-Wei Fuping</p>
</blockquote></div>  
</div>
            