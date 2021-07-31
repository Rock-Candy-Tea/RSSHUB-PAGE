
---
title: 'Oasis 2D 之 SpriteMask'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc3fe62285ed431388d4af919d13b7f5~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 06:22:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc3fe62285ed431388d4af919d13b7f5~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者 - <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsinglecoder" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/singlecoder" ref="nofollow noopener noreferrer">Oasis 团队 - 诚空</a>
<a name="user-content-BvxGJ" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h1 data-id="heading-0">前言</h1>
<p>过去大家对 Oasis 的认知一直停留在 3D 领域，过去我们支撑了很多 3D 互动项目的落地，随着我们服务的业务数量越来越多，复杂度越来越高，仅仅提供 3D 的能力已经不能完全满足业务需求了，所以今年我们开始扩展 2D 能力。2D 中最基础的就是 SpriteRenderer 和 SpriteMask，在引擎版本 0.3 中，我们已经完成了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Foasisengine.cn%2F0.4%2Fdocs%2Fsprite-renderer-cn" target="_blank" rel="nofollow noopener noreferrer" title="https://oasisengine.cn/0.4/docs/sprite-renderer-cn" ref="nofollow noopener noreferrer">SpriteRenderer</a> 的重构，而本篇文章主要分享下 <a href="https://link.juejin.cn/?target=https%3A%2F%2Foasisengine.cn%2F0.4%2Fdocs%2Fsprite-mask-cn" target="_blank" rel="nofollow noopener noreferrer" title="https://oasisengine.cn/0.4/docs/sprite-mask-cn" ref="nofollow noopener noreferrer">SpriteMask</a> 的研发历程，最终的效果如下（左图为内遮罩 <strong>VisibleInsideMask</strong>，右图为外遮罩 <strong>VisibleOutsideMask</strong>）：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc3fe62285ed431388d4af919d13b7f5~tplv-k3u1fbpfcp-zoom-1.image" alt="mask.gif" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-vOTtq" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h1 data-id="heading-1">调研</h1>
<p>SpriteMask 的主要作用就是和 SpriteRenderer 协作，实现精灵遮罩的效果。在进入正式开发前，我们先从两方面进行调研：开发者使用层面业界一些引擎是如何使用遮罩的、底层实现层面遮罩实现都有哪些技术方案。
<a name="user-content-yN3hF" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-2">使用方式</h2>
<p>从开发者使用层面来看，行业内遮罩的使用方式大致分为 2 种：基于节点树层次结构和基于渲染顺序。
<a name="user-content-gz0Ao" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-3">基于节点树层次结构</h3>
<p>基于节点树层次结构的使用方式大致如下图：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2cf766376d7f4715844d98317988cc0c~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>mask 会对其子节点中所有的渲染组件生效，这种使用方式，比较依赖节点树的层次结构，当一个 sprite 需要多个遮罩的时候，就需要嵌套多层 mask 了，而且一旦某个遮罩需要动态改变，整个节点树的结构可能也需要跟着一起调整。
<a name="user-content-ent0E" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-4">基于渲染顺序</h3>
<p>基于渲染顺序的使用方式，mask 会通过一些参数设置最后得到两个遮罩影响的渲染范围 [front, back)，结合 sprite 的渲染顺序来看 (以屏幕往外作为 <strong>Z</strong> 的正方向来说，当两个精灵有重叠的时候，Z 更大的会渲染在更上面，也就是会覆盖 Z 更小的)，大致如下：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd70fe74c0a2486eadb25f4f1d9ca7f0~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>可以看出，mask 和渲染顺序比较强相关，实现起来会比较自然，就是不够灵活，比如上图中，我们希望 mask 对 Z 为 0 的 sprite 遮罩生效，其他保持不变就无法做到了。
<a name="user-content-B44KB" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-5">Oasis：基于遮罩层</h3>
<p>无论是基于节点树层次结构或基于渲染顺序，都不够灵活，SpriteMask 对 SpriteRenderer 的遮罩都会受到一些外部因素影响，如节点树层次结构或者渲染顺序等，我们希望 SpriteMask 可以快速和 SpriteRenderer 进行匹配 (<strong>匹配：一个 SpriteMask 可以对 SpriteRenderer 产生遮罩称为匹配</strong>)，并且不受外部因素的影响，为此我们在使用方式上设计了<a href="https://link.juejin.cn/?target=https%3A%2F%2Foasisengine.cn%2F0.4%2Fdocs%2Fsprite-mask-cn%23%25E9%2581%25AE%25E7%25BD%25A9%25E5%25B1%2582-spritemasklayer" target="_blank" rel="nofollow noopener noreferrer" title="https://oasisengine.cn/0.4/docs/sprite-mask-cn#%E9%81%AE%E7%BD%A9%E5%B1%82-spritemasklayer" ref="nofollow noopener noreferrer">遮罩层</a>的概念，当 SpriteMask 影响的遮罩层和 SpriteRenderer 所处的遮罩层有交集的时候即可匹配，如下：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afcbf3155c8443d3bbea0d509404c5f1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-IkZ3n" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-6">技术选型</h2>
<p>业界实现的遮罩能力主要有：矩形遮罩、矩形旋转遮罩、图片遮罩、几何多边形遮罩、内外遮罩。而 Oasis 是移动优先的 web 图形引擎，所以我们可以基于 webgl 来实现各种遮罩效果，主要有以下几种方案：stencil、framebuffer、scissor、shader。接下来我们从功能完备和性能两方面来进行考虑。
<a name="user-content-oGtg9" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-7">功能完备</h3>
<p>从功能完备的角度来进行分析对比，如下表：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a3322d3884f4c54852a47a0de070819~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-jMcEc" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-8">性能</h3>
<p>从功能完备的角度分析，可以排除 scissor、shader 方案，接下来我们需要从性能角度来对比下 stencil 和 framebuffer。我们使用 webgl 分别实现 stencil 和 framebuffer 方案，不断增加遮罩数量，计算 100 帧平均每帧时间 (单位：ms)，结果如下：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f617f96c71249cca64e65ade733cb9e~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>测试环境
设备：MacBook Pro
处理器：2.4 GHz 四核 Intel Core i5
浏览器：Chrome 90.0.4430.212</p>
</blockquote>
<p><strong>测试示例详见：</strong><br>stencil：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fchengkong%2Fpen%2FpoPerVy%3Feditors%3D1011" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/chengkong/pen/poPerVy?editors=1011" ref="nofollow noopener noreferrer">codepen.io/chengkong/p…</a><br>framebuffer：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fchengkong%2Fpen%2FxxdYNro" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/chengkong/pen/xxdYNro" ref="nofollow noopener noreferrer">codepen.io/chengkong/p…</a>
<a name="user-content-oIegJ" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-9">结论</h3>
<p>通过两个维度的对比分析，从功能完备的角度来看，我们可以排出其他方案了，只剩下 stencil 和 framebuffer。再从性能角度来看，framebuffer 方案的性能比 stencil 的性能慢差不多 <strong>10</strong> 倍的数量级，因此我们最终决定采用 stencil 的方案来实现遮罩。
<a name="user-content-qcS6u" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h1 data-id="heading-10">关键设计与实现</h1>
<p>调研完成后，使用方式与技术方案已经明确，接下来就是核心类的设计了。这里先简单介绍下需要了解的几个核心概念：遮罩层、遮罩区域、遮罩类型。<br>​</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Foasisengine.cn%2F0.4%2Fdocs%2Fsprite-mask-cn%23%25E9%2581%25AE%25E7%25BD%25A9%25E5%25B1%2582-spritemasklayer" target="_blank" rel="nofollow noopener noreferrer" title="https://oasisengine.cn/0.4/docs/sprite-mask-cn#%E9%81%AE%E7%BD%A9%E5%B1%82-spritemasklayer" ref="nofollow noopener noreferrer">遮罩层</a>是我们抽象出来的概念，作为 SpriteMask 和 SpriteRenderer 如何匹配的纽带，<strong>遮罩区域</strong>表示的是我们对一个特定区域要进行遮罩处理，<strong>遮罩类型</strong>表示的是遮罩处理的方案(内遮罩，外遮罩)。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5d598255a0b4f37bafe70b66a6b7901~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-eFciW" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-11">设计</h2>
<p>最终开发者使用的方式如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> sprEntity = rootEntity.createChild(<span class="hljs-string">"Sprite"</span>);
<span class="hljs-comment">// 1.1 添加一个 SpriteRenderer</span>
<span class="hljs-keyword">const</span> renderer = sprEntity.addComponent(SpriteRenderer);
renderer.sprite = sprite;
<span class="hljs-comment">// 1.2 设置遮罩类型</span>
renderer.maskInteraction = SpriteMaskInteraction.VisibleInsideMask;
<span class="hljs-comment">// 1.3 设置精灵所属遮罩层</span>
renderer.maskLayer =  SpriteMaskLayer.Layer0;

<span class="hljs-keyword">const</span> maskEntity = rootEntity.createChild(<span class="hljs-string">"Mask"</span>);
<span class="hljs-comment">// 2.1 添加一个 SpriteMask</span>
<span class="hljs-keyword">const</span> mask = maskEntity.addComponent(SpriteMask);
<span class="hljs-comment">// 2.2 设置遮罩区域</span>
mask.sprite = maskSprite;
<span class="hljs-comment">// 2.3 设置影响的遮罩层，和精灵所属遮罩层进行匹配用</span>
mask.influenceLayers = SpriteMaskLayer.Layer0;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相关类的关系图如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89d9abd2c2484118bd8d18b1d9767798~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">遮罩层</h3>
<p>遮罩层决定着 SpriteMask 和 SpriteRenderer 如何进行快速匹配，我们先来定义所有的遮罩层，如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * Sprite mask layer.
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-built_in">enum</span> SpriteMaskLayer &#123;
    <span class="hljs-comment">/** Mask layer 0. */</span>
  Layer0 = <span class="hljs-number">0x1</span>,
  <span class="hljs-comment">/** Mask layer 1. */</span>
  Layer1 = <span class="hljs-number">0x2</span>,
  .
  .
  .
  <span class="hljs-comment">/** Mask layer 31. */</span>
  Layer31 = <span class="hljs-number">0x80000000</span>,
  <span class="hljs-comment">/** All mask layers. */</span>
  Everything = <span class="hljs-number">0xffffffff</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遮罩层一共 32 个，<strong>why ???</strong> 主要是 Number 类型虽然是 64 位，但是所有按位运算都是在 32 位二进制数上执行的，每位可以代表一层，这样我们在做匹配的时候可以通过位运算快速筛选，并且一个场景中预留 32 个遮罩层应该是可以满足所有需求了 (反正我是没遇到过啥项目里面同时使用这么多遮罩的 ^-^)。接下来就是给 SpriteRenderer 和 SpriteMask 添加遮罩层相关属性，如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SpriteRenderer</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Renderer</span> </span>&#123;
  <span class="hljs-comment">/**
   * The mask layer the sprite renderer belongs to.
   */</span>
  <span class="hljs-keyword">get</span> <span class="hljs-title">maskLayer</span>(): <span class="hljs-title">number</span>;
  <span class="hljs-title">set</span> <span class="hljs-title">maskLayer</span>(<span class="hljs-params">value: <span class="hljs-built_in">number</span></span>);
&#125;

<span class="hljs-title">class</span> <span class="hljs-title">SpriteMask</span> <span class="hljs-title">extends</span> <span class="hljs-title">Renderer</span> &#123;
  <span class="hljs-comment">/** The mask layers the sprite mask influence to. */</span>
  <span class="hljs-attr">influenceLayers</span>: <span class="hljs-built_in">number</span> = SpriteMaskLayer.Everything;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-sVfFv" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-13">遮罩区域</h3>
<p>当前版本我们计划先实现图片遮罩，也就是遮罩的区域由遮罩设置的图片来决定，所以在 SpriteMask 添加一个属性来设置遮罩图片，如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SpriteMask</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Renderer</span> </span>&#123;
  <span class="hljs-comment">/** The mask layers the sprite mask influence to. */</span>
  <span class="hljs-attr">influenceLayers</span>: <span class="hljs-built_in">number</span> = SpriteMaskLayer.Everything;
  
  <span class="hljs-comment">/**
   * The Sprite used to define the mask.
   */</span>
  <span class="hljs-keyword">get</span> <span class="hljs-title">sprite</span>(): <span class="hljs-title">Sprite</span>;
  <span class="hljs-title">set</span> <span class="hljs-title">sprite</span>(<span class="hljs-params">value: Sprite</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-Fdsb7" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-14">遮罩类型</h3>
<p>遮罩层设计完后，明确了 SpriteMask 和 SpriteRenderer 如何进行快速匹配，接下来一个比较重要的设计就是被遮罩的精灵，是显示遮罩区域内还是区域外的内容呢？首先我们定义遮罩类型的枚举，如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/**
 * Sprite mask interaction.
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-built_in">enum</span> SpriteMaskInteraction &#123;
  <span class="hljs-comment">/** The sprite will not interact with the masking system. */</span>
  None,
  <span class="hljs-comment">/** The sprite will be visible only in areas where a mask is present. */</span>
  VisibleInsideMask,
  <span class="hljs-comment">/** The sprite will be visible only in areas where no mask is present. */</span>
  VisibleOutsideMask
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遮罩类型的选择应该由 SpriteRenderer 来决定，所以我们在 SpriteRenderer 里添加一个属性来标记，如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SpriteRenderer</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Renderer</span> </span>&#123;  
  <span class="hljs-comment">/**
   * Interacts with the masks.
   */</span>
  <span class="hljs-keyword">get</span> <span class="hljs-title">maskInteraction</span>(): <span class="hljs-title">SpriteMaskInteraction</span>;
  <span class="hljs-title">set</span> <span class="hljs-title">maskInteraction</span>(<span class="hljs-params">value: SpriteMaskInteraction</span>);
  
  /**
   * <span class="hljs-title">The</span> <span class="hljs-title">mask</span> <span class="hljs-title">layer</span> <span class="hljs-title">the</span> <span class="hljs-title">sprite</span> <span class="hljs-title">renderer</span> <span class="hljs-title">belongs</span> <span class="hljs-title">to</span>.
   */
  <span class="hljs-title">get</span> <span class="hljs-title">maskLayer</span>(): <span class="hljs-title">number</span>;
  <span class="hljs-title">set</span> <span class="hljs-title">maskLayer</span>(<span class="hljs-params">value: <span class="hljs-built_in">number</span></span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-ep8ea" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-15">实现</h2>
<p>我们先来看看最终实现在整个渲染管线中的流程图如下：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844be17a1a8949f18f0f8a52fb9879e1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-YeQbY" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-16">遮罩层匹配</h3>
<p><a name="user-content-nmpaa" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-17">基本原理</h4>
<p>虽然 SpriteMask 继承于 Renderer，但是在每帧调用到 _render 的时候，我们并不是直接把 SpriteMask 送入渲染队列，而是在渲染管线中缓存住，如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SpriteMask</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Renderer</span> </span>&#123;
  _render(camera: Camera): <span class="hljs-built_in">void</span> &#123;
    <span class="hljs-comment">// ...</span>
    
    <span class="hljs-comment">// 如果是 SpriteMask 渲染组件，直接在渲染管线中缓存</span>
    camera._renderPipeline._allSpriteMasks.add(<span class="hljs-built_in">this</span>);
    
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么要这么设计呢，解答这个问题之前，我们需要先了解一下 Oasis 现在是如何把需要渲染的内容送入最终渲染的，如下：<br>一般情况，渲染组件将自己丢入渲染队列之后，对于整个渲染管线来说，只是一堆渲染元素，渲染队列排好序之后，会逐个渲染 (流程图中的绿色部分)。至此，我们还是无法解释上述的疑问，不急，再来看看如何使用 stencil 实现遮罩的流程，我们始终设置模版测试的参考值为 1 ，如下：</p>
<ol>
<li>把对精灵有影响的 SpriteMask 全部送入 GPU 进行模版测试，并更新模版缓冲的值</li>
<li>渲染精灵的时候，根据遮罩类型选择比较函数 (gl.stencilFunc)</li>
<li>通过 stencil test 的像素即可渲染出来</li>
</ol>
<p>是不是发现问题了呢？第一步需要把有影响的 SpriteMask 全部送入 GPU，假设有一个 SpriteMask 对两个不同的精灵都有影响，那么必然需要送入 2 次，按照现有的渲染流程，显然无法做到，所以我们需要把 SpriteMask 单独缓存 (流程图中的蓝色部分)，当渲染到某个精灵的时候，把所有匹配的 SpriteMask 找出来进行模版缓冲区的更新。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3388289612a74bb3818454063dedafc2~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-IWudM" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-18">优化技巧</h4>
<p>这里有一个问题需要思考，假设我们连续渲染两个精灵，但是两个精灵匹配的 SpriteMask 只相差一个，那么这个时候模版缓冲区完全没必要一个个更新，只需要两个精灵所属遮罩层之间做个 diff 就好了，这样可以有效的减少和 GPU 的交互，基于此，我们添加 <code>SpriteMaskManager</code> 来专门处理这部分逻辑，核心思想就是记录上一个精灵 (称为 preSprite) 的遮罩层，当渲染新的精灵 (称为 curSprite) 时，找出两个精灵遮罩层的差异，分为 3 种情况：commonLayer、addLayer、reduceLayer。commonLayer 是两个精灵重叠的层，addLayer 是 curSprite 比 preSprite 多的层，reduceLayer 是 curSprite 比 preSprite 少的层，关系如下：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65af1096b0704447b5be85752b92af96~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>找出遮罩层差异的核心代码如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> commonLayer = preMaskLayer & curMaskLayer;
<span class="hljs-keyword">const</span> addLayer = curMaskLayer & ~preMaskLayer;
<span class="hljs-keyword">const</span> reduceLayer = preMaskLayer & ~curMaskLayer;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，需要通过遮罩层差异，找出对应的 SpriteMask，然后进行相应的操作，SpriteMask 是通过 influenceLayers 来标识自己会影响哪些遮罩层，因此只需要和上面的 3 个层做简单位运算即可，核心代码如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// Traverse masks.</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, n = allMasks.length; i < n; i++) &#123;
  <span class="hljs-keyword">const</span> mask = allMaskElements[i];
  <span class="hljs-keyword">const</span> influenceLayers = mask.influenceLayers;

  <span class="hljs-comment">// Do nothing for commonLayer.</span>
  <span class="hljs-keyword">if</span> (influenceLayers & commonLayer) &#123;
    <span class="hljs-keyword">continue</span>;
  &#125;

  <span class="hljs-comment">// Stencil value +1 for mask influence to addLayer.</span>
  <span class="hljs-keyword">if</span> (influenceLayers & addLayer) &#123;
    <span class="hljs-keyword">const</span> maskRenderElement = mask._maskElement;
    maskRenderElement.isAdd = <span class="hljs-literal">true</span>;
    <span class="hljs-built_in">this</span>._batcher.drawElement(maskRenderElement);
    <span class="hljs-keyword">continue</span>;
  &#125;

  <span class="hljs-comment">// Stencil value +1 for mask influence to reduceLayer.</span>
  <span class="hljs-keyword">if</span> (influenceLayers & reduceLayer) &#123;
    <span class="hljs-keyword">const</span> maskRenderElement = mask._maskElement;
    maskRenderElement.isAdd = <span class="hljs-literal">false</span>; 
    <span class="hljs-built_in">this</span>._batcher.drawElement(maskRenderElement);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-XKv2e" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-19">遮罩区域</h3>
<p>当一个 SpriteMask 匹配后，就需要去更新 stencil 缓冲区，对于 addLayer 的我们需要给缓冲区中对应的位置 +1，对于 reduceLayer 的我们需要给缓冲区中对应的位置 -1，核心代码如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// Set the op that the stencil test passed.</span>
<span class="hljs-keyword">const</span> stencilState = material.renderState.stencilState;
<span class="hljs-keyword">const</span> op = spriteMaskElement.isAdd ? StencilOperation.IncrementSaturate : StencilOperation.DecrementSaturate;
stencilState.passOperationFront = op;
stencilState.passOperationBack = op;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-X04Is" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-20">遮罩类型</h3>
<p>当通过遮罩层的匹配找出所有 SpriteMask 并将 stencil 缓冲区数据更新后，我们就需要根据设置的遮罩类型来设置模版测试函数，核心代码如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">if</span> (maskInteraction === SpriteMaskInteraction.None) &#123;
  <span class="hljs-comment">// When the mask is not needed, the stencil test always passed.</span>
  stencilState.enabled = <span class="hljs-literal">false</span>;
  stencilState.writeMask = <span class="hljs-number">0xff</span>;
  stencilState.referenceValue = <span class="hljs-number">0</span>;
  stencilState.compareFunctionFront = stencilState.compareFunctionBack = CompareFunction.Always;
&#125; <span class="hljs-keyword">else</span> &#123;
  stencilState.enabled = <span class="hljs-literal">true</span>;
  stencilState.writeMask = <span class="hljs-number">0x00</span>;
  <span class="hljs-comment">// When a mask is needed, set ref to 1, inside mask ref <= stencil, outside mask ref> stencil.</span>
  stencilState.referenceValue = <span class="hljs-number">1</span>;
  <span class="hljs-keyword">const</span> compare =
        maskInteraction === SpriteMaskInteraction.VisibleInsideMask
  ? CompareFunction.LessEqual
  : CompareFunction.Greater;
  stencilState.compareFunctionFront = compare;
  stencilState.compareFunctionBack = compare;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-YcZLA" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h1 data-id="heading-21">总结</h1>
<p>最终我们实现了 SpriteMask 的基础版本 (支持图片遮罩)，详见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Foasisengine.cn%2F0.4%2Fdocs%2Fsprite-mask-cn" target="_blank" rel="nofollow noopener noreferrer" title="https://oasisengine.cn/0.4/docs/sprite-mask-cn" ref="nofollow noopener noreferrer">oasisengine.cn/0.4/docs/sp…</a>。<br>并且可以通过我们的示例查看详细用法，详见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Foasisengine.cn%2F0.4%2Fexamples%23sprite-mask" target="_blank" rel="nofollow noopener noreferrer" title="https://oasisengine.cn/0.4/examples#sprite-mask" ref="nofollow noopener noreferrer">oasisengine.cn/0.4/example…</a>。<br>​</p>
<p>目前我们的 SpriteMask 只实现了图片遮罩的能力，已经能够满足大部分的需求了，后续也会根据开发者的实际需求，考虑是否支持矩形遮罩、椭圆遮罩、自定义图形遮罩等。并且之后遮罩会支持整个 2D 的生态，而不仅仅局限于 SpriteRenderer。
<a name="user-content-XwE64" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h1 data-id="heading-22">最后</h1>
<p>欢迎大家 star 我们的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Foasis-engine%2Fengine" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/oasis-engine/engine" ref="nofollow noopener noreferrer">github 仓库</a>，也可以随时关注我们后续 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Foasis-engine%2Fengine%2Fmilestone%2F3" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/oasis-engine/engine/milestone/3" ref="nofollow noopener noreferrer">v0.5</a> 的规划，也可以在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Foasis-engine%2Fengine%2Fissues" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/oasis-engine/engine/issues" ref="nofollow noopener noreferrer">issues</a> 里给我们提需求和问题。开发者可以加入到我们的钉钉群里来跟我们吐槽和探讨一些问题，钉钉搜索 31360432</p>
<p>无论你是渲染、TA 、Web 前端或是游戏方向，只要你和我们一样，渴望实现心中的绿洲，欢迎投递简历到 <a href="https://link.juejin.cn/?target=mailto%3Achenmo.gl%40antgroup.com" target="_blank" title="mailto:chenmo.gl@antgroup.com" ref="nofollow noopener noreferrer">chenmo.gl@antgroup.com</a>。岗位描述详见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Foasis-engine%2Fannouncement%2Fkdlpxt" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/oasis-engine/announcement/kdlpxt" ref="nofollow noopener noreferrer">www.yuque.com/oasis-engin…</a>。</p></div>  
</div>
            