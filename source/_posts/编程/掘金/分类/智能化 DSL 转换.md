
---
title: '智能化 DSL 转换'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07c38925380647bb9964a75f1bf446e9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 19:11:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07c38925380647bb9964a75f1bf446e9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>文/ 阿里云流量产品团队 - 虚俞</p>
</blockquote>
<p>智能化技术在不断的前进，随着训练算法的不断迭代，模型的识别准确率也在稳步提升，但是以当前智能化的进程来看，识别的准确率是无法到达100%的，而且部分场景的因为在表现形式上过于接近，导致在识别是差异不大。并且识别产生的数据是一个扁平化的数组，这样的数据在下游是无法直接使用的，无论是画布引擎的渲染，还是代码的生成，都是需要有一个立体的数据，即DSL。 本文会介绍Dumbo在这方面的设计思路及实现。</p>
<h1 data-id="heading-0">背景</h1>
<p>Dumbo 是一个利用图像识别算法，一键生成前端代码的智能开发平台。目前已经落地于多个阿里云控制台及中后台项目。</p>
<div align="middle"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07c38925380647bb9964a75f1bf446e9~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<p>首先，Dumbo 的基本链路为通过一张图片，利用智能化技术识别图片中各种信息数据，在通过DSL引擎转化为符合约定规范的 JSON 描述（即 Schema ），再通过可视化搭建平台进行人工微调修正，最后生成 React 模块代码。</p>
<p>无论在可视化搭建平台，还是直接利用Schema生成React模块代码，中间都需要先把利用图像识别算法得到的数据，转换为可被搭建平台/代码生成模块所认识的Schema，这部分就是本文所需要阐述内容。</p>
<h1 data-id="heading-1">解决方案</h1>
<p>考虑到Dumbo有开放的模型训练能力，但是模型训练及识别之后的数据及DSL转化可能在不同团队之间是独立，基础组件库也不同，前期我们做了内部的Adapter转化引擎，主要是对Fusion/Antd的一些转换，但是有很多团队会有自己的一些组件库及业务组件，这部分可以在模型训练的时候添加标注，但是我们默认的DSL是不支持这类识别的，所以需要有一个特定的模块来处理这部分数据，并能够很好的支持后续的扩展。所以把DSL转化这层独立出来，作为一个单独的项目，目标成为一个能够通过简单配置就能够实现业务自定义DSL，快速的搭建一个完善的Adapter服务。</p>
<p>我们在实现DSL转化引擎之前，我们需要知道输入是什么？目标及输出是什么？这是转换的前提条件，我们弄清楚输入是怎么样的一个结构，然后才能根据相应的结构对输入进行处理。
首先，看下我们的输入结构：</p>
<pre><code class="copyable">[
    &#123;
        "name": "Message",
        "props": &#123;
        &#125;,
        "probability": 1,
        "position": &#123;
        &#125;,
        "id": "534df201-bdcb-11eb-8e5e-8fd6c9c0318c"
    &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输入结构整体是一个扁平式的，所以我们Adapter的输入就是一组识别的大数组，那输出是什么，看如下数据：</p>
<pre><code class="copyable">&#123;
    "version": "1.0.0",
    "componentsMap": [
        &#123;
            "componentName": "Page",
            "exportName": "Page",
            "package": "@alifd/fusion",
            "version": "2.19.0",
            "destructuring": true
        &#125;
    ],
    "componentsTree": [
        &#123;
            "componentName": "Page",
            "children": [],
            "props": &#123;&#125;
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是一个立体化的结构，能够被搭建平台直接使用的Sechma及其相关的依赖关系。
所以基于以上的输入/输出特性，我们定义了Adapter引擎，整体的设计如下：</p>
<div align="middle"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a107ad524ab4f41ac31613ba431f9c3~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<h2 data-id="heading-2">实现</h2>
<p>下面我们分别对每个模块进行展开，简要阐述下具体的实现过程。</p>
<p><strong>Node 节点的预处理工作</strong>
首先预处理部分，原始Node节点是一个扁平的数据数组，但是我们最终的目标是一个结构化、立体的数据，所以我们需要对数据进行一些前置处理，这样才能在后续的流程中更准确的来判断位置，识别特性等。我们此处以Table为例子，它所需要经历的预处理Plugins如下几种：</p>
<div align="middle"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff1cde70b5c84b0e8074756c51c79a2f~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<p>首先我们对文字进行了处理，包括但不仅限于文字的非正常拆分、特定无效文字的过滤等。机器识别的文字可能存在无效字符、断句拆分异常的问题，这可能会影响后续位置信息的判断，所以我们在文字预处理里面，会对整体文字进行合并，通过算法把一些合并度高的文字进行合并及过滤。
并会进行一些去重相关处理，这块去重则主要是部分特定的组件，在内部是不存在children，所以需要我们根据特定的场景，来去除该部分的一些无效文案，比如说一些Icon Button被文字识别成的特殊或者数字字符。这就需要有去重着一步来完成。
接下来是关系处理，我们会通过节点深度，来处理节点与节点间的关系，子节点是否包含子节点等，通过位置、重叠度、相似度算法，来初步处理子节点与父节点之间的关系，得到一个立体型的数据。</p>
<p><strong>Adapter处理</strong>
Adapter处理就涉及到了每个组件的特性处理及细分内部具体属性信息，大致内部会做以下几种操作，功能因组件复杂程度来决定。
我们还是以Table为例子</p>
<div align="middle"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e82c29c160a4f4aa34463ce930d60fd~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<p>首先我们会在子节点中找到Column Title相关的节点数据，并会对Column Title进行重组，变成Table.Column节点，作为Table的每一列，并会提取相关的子Text节点内部的英文文案作为Key值来进行后续的数据匹配。Table.Column查找会依据第一个行高度及整体识别的宽度信息，等综合进行判断，判断出Table.Column的存在，并封装为一个单独的节点数据。接下来表格存在多种属性，以我们集团的Fusion组件为例子，Table包含了一系列排序，筛选，选择字段。这部分需要通过对Icon的分析，来确定Table是否包含此类属性。我们也会处理表格内数据，生成一份识别类型的dataSource，供下游进行数据渲染，这里也会做一些我们项目中平时对于Table的基础属性的补全工作。</p>
<p><strong>Node 节点的后处理</strong>
前面基本已经把一些节点的特殊属性，节点的缺失的一些属性做了补全，接下就是对组件库的适配，及最后依赖提取等，以Table为例，我们的流程节点包含如下：</p>
<div align="middle"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39c2f4b2d3a04cf39323c81da40bbe0f~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></div><br> 
<p>在执行的时候我们会确定需要输出时依赖的底层组件库，会从相应库中找到对应字段，部分属性需要根据组件库进行转换，把内部的一些属性名称转为对应的组件库的属性。我们会维护一张大的组件Map表，会标注组件所支持的属性，及对应的标识符，以此来确定最终Sechma所需要的属性。最后是依赖的提取，也是根据用户所选择的基础组件库，获取到用户所用到的组件信息，自动生成符合集团规范的DSL依赖描述。
还有就是最终DSL的整体格式，也是通过这部分后处理来实现的，之后用户的自定义DSL也会在这里做实现，达到用户能够自定义输出DSL的能力。</p>
<h2 data-id="heading-3">细节</h2>
<p>DSL转化我们做了很多次的优化，中间我们持续发现了一些bad case，内部会有很多处理这部分的逻辑，没办法以一种统一的方式来处理。</p>
<p><strong>Button处理</strong>
我们在Button最开始的处理的时候，最开始的时候我们按照设计规范来定义Button内部的children，一般内部有Icon的则表示是一个Icon Button，有文字的则表示普通的Button，但是我们在具体实现的时候，发现Icon的是识别可能会把"刂"错识别成为排序的Icon，因为比较接近。这块导致Button从普通的变成了Icon Button，这种现象显然是我们没有预料到的。所以我们进行细化处理，区分children长度及特殊字符串、位置信息来进行预判Button是否是Icon Button，最终达到转换效果和设计稿一致的目标。</p>
<p><strong>详情列表的label位置判断</strong>
详情列表在我们组件中存在垂直、水平2种label的呈现方式，因为该模型的特殊性相对于不是很明显，所以在模型识别之后整体呈现的效果并不佳，部分Item并没有准确的识别到, 这时我们就需要在已有识别的Item基础上，再根据位置信息来判断未被识别的Item是否存在，label的位置是如何的？我们这边进行了系列处理，来尽最大程度的实现label位置的查找。
1、这边会分2个分支处理，第一分支按行进行分组，判断行内是否有Item，如果有，则根据Item的label位置进行未识别位置判断，并且记录Item的个数。以位置基础为基准，根据左右/上下节点来判断出label。
2、继续处理其他行的数据，一般我们的交互规范不会出现垂直、水平2种都出现的情况。所以我们以多数Item的label位置作为所有的label位置，再2次进行查找未包含Item的行，最终达到优化识别的效果。</p>
<p>还有其他细节就不一一举例，当然这也是很小的点，后续有很多算法需要优化。</p>
<h2 data-id="heading-4">展望</h2>
<p>以上我们介绍了现有我们DSL引擎支持的能力和解决方案的实现，后续我们会持续优化我们的DSL引擎，会根据我们的场景及组件特征，对一套组件的特性进行多算法的处理，结算处整体的有效性。在今年也会计划把整个DSL作为智能识别的一环服务，对我们集团内部做一些自定化的功能，接入方可以有效的复用我们的特性算法，也可以自定义组件特性算法，后续考虑把这个作为一个智能化DSL转化市场来做，甚至让用户在可视化的界面内就能够自由组合对应Plugin和Adapter，实现在线自定义DSL的场景。当然目前我们的项目还在高速迭代中，DSL引擎也有很多考虑不周的地方，有较多优化的空间，也有很多想法待实现，欢迎有想法的同学加入我们，可联系<a href="mailto:yaoli.pt@alibaba-inc.com">yaoli.pt@alibaba-inc.com</a>，期待你与我们一路通行，一路探索。</p>
  <br>
  <hr>
  <div align="middle"><a href="https://weibo.com/7513068590/profile?topnav=1&wvr=6&is_all=1" target="_blank" rel="nofollow noopener noreferrer"> 淘系前端-F-x-Team 开通微博</a> 啦！（微博登录后可见）</div>
  <div align="middle">除文章外还有更多的团队内容等你解锁🔓</div>
  <div align="middle">
    <a href="https://weibo.com/7513068590/profile?topnav=1&wvr=6&is_all=1" target="_blank" rel="nofollow noopener noreferrer"> 
      <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5d0f4abfd194076b20313ca0f56d983~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
    </a>
  </div>
  <br></div>  
</div>
            