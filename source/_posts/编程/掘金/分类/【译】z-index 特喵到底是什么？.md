
---
title: '【译】z-index 特喵到底是什么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00b2b42427eb40a9acd22cfb0bfa4609~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 22:34:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00b2b42427eb40a9acd22cfb0bfa4609~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原文地址：<a href="https://www.joshwcomeau.com/css/stacking-contexts/" target="_blank" rel="nofollow noopener noreferrer">www.joshwcomeau.com/css/stackin…</a></p>
<p>作者：Josh Comeau、 译者：林鸿鹄</p>
<p>未经授权禁止转载。</p>
<h1 data-id="heading-0">带你探索 CSS 层叠上下文， CSS 中头号误导人的机制。</h1>
<p>在 CSS 中，我们都明确的知道用 z-index 可以来控制 HTML 的层级顺序。元素有着越大的指数将会排在页面的最顶部：</p>
<pre><code class="copyable"><style>
  .box &#123;
    position: relative;
    width: 50px;
    height: 50px;
    border: 3px solid;
    background: silver;
  &#125;
  .first.box &#123;
    z-index: 2;
  &#125;
  .second.box &#123;
    z-index: 1;
    margin-top: -20px;
    margin-left: 20px;
  &#125;
</style>

<div class="first box"></div>
<div class="second box"></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00b2b42427eb40a9acd22cfb0bfa4609~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>因为 .first.box 比 .second.box 有着更大的 z-index 的数值，所有它展示在前面。假如我们把 z-index 的声明从代码中移除的话，那么 .first.box 将会被 .second.box 遮挡了。</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1de4a0a6f9d84e24aaa4e3955915b4ec~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>但事情往往不是这么简单。有时候大的 z-index 不是战无不胜的。让我们来看看小明同学写的这个代码到底发生了什么！</p>
<pre><code class="copyable"><style>
  header &#123;
    position: relative;
    z-index: 2;
  &#125;
  .tooltip &#123;
    position: absolute;
    z-index: 999999;
  &#125;
  main &#123;
    position: relative;
    z-index: 1;
  &#125;
</style>

<header>
  My Cool Site
</header>
<main>
  <div class="tooltip">
    A tooltip
  </div>
  <p>Some main content</p>
</main>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b1976424eae4cbc91c1fee802382358~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>小明明明声明了.tooltip 的 z-index：999999, 是大于 header 的 z-index：2 的。 可是为什么 header 还是展示在最上层呢？</p>
<p>在揭秘这个神秘面纱之前，我们需要去学习一个叫做 stacking contexts 的知识点。这个只是点虽然让人费解，但却是CSS最为基础的机制。在剩下的这片文章中，我们将会了解到他们是什么？他们是怎样运作的，以及我们怎么能在代码中用他们取得便利。</p>
<blockquote>
<p>本篇文章面向的读者：所有被 z-index 曾经支配过恐惧的前端开发。</p>
</blockquote>
<h2 data-id="heading-1">层（layers）和组（groups）</h2>
<p>如果你曾经用过类似 PS 或是 Figma 这种图文编辑软件，那么你应该熟悉层级的概念：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/612d5b028866446eb704b0ca05b17b7a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>下面这张图像千层饼一样有3层不同的画布。最低层的是一张小喵咪的照片。在照片之上的是2层傻傻的细节，最后合成后就是一张长胡子的天使小猫咪了！</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39368947a961443e85a8bfa43e665cfb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在PS里，我们可以组合这些层级：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5291cde66c3451e93b35cdd7d95d59f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>就像文件夹一样，一个组可以让我们组合一系列的层级。组合之间的层级不能被混合在一起。所有狗狗的层级都会盖在猫咪的层级之上。</p>
<p>当我们导出最终组合的时候，我们一点也看不到猫咪，因为全部的层级都已经被猫咪覆盖了：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5aafde568c1f46398177fd9a20939873~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>同样的，CSS层级的运作方式其实和 PS 差不多： 元素们都被组合成为 <strong>stacking contexts</strong>。当我们给元素一个z-index，那么这个值只会和在相同 context 下的其他元素竞争。z-index 不是全局的。</p>
<p>在默认的情况下， 一个简单的 HTML 文本只有一个上下文，它包括了所有的节点。 但是，我们可以添加更多的上下文！</p>
<p>创建上下文的方法有很多种， 但是最普遍的方法是通过结合两个声明，position 和 z-index :</p>
<pre><code class="copyable">.some-element &#123;
  position: relative;
  z-index: 1;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当两个声明在一起的时候，一个秘密的开关被打开了： 我们就这样创建了一个新的上下文，元素 .some-element 和它的子元素将会被划分成一个组。</p>
<p>让我们来重新回顾一下之前的那个例子：</p>
<pre><code class="copyable"><style>
  header &#123;
    position: relative;
    z-index: 2;
  &#125;
  .tooltip &#123;
    position: absolute;
    z-index: 999999;
  &#125;
  main &#123;
    position: relative;
    z-index: 1;
  &#125;
</style>
<header>
  My Cool Site
</header>
<main>
  <div class="tooltip">
    A tooltip
  </div>
  <p>Some main content</p>
</main>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以先画出这段代码的上下文结构：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b78ef1903144f2abd7e22f1ab387e35~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>虽然 .tooltip 元素的 z-index 是 999999，但是那个值只在 main 标签里才能生效。这个 z-index 只能控制 .tooltip 是展示在 p 标签的上方还是下方而已。</p>
<p>纵观根上下文，我们可以比较 header 标签和 main 标签所在的位置。 因为 main 标签的 z-index 比 header 小。<strong>所以 main 和它的子元素都展示在 header 的下方</strong>。</p>
<h2 data-id="heading-2">修改上面的例子</h2>
<p>所以我们该如何修改小明同学的代码来让 tooltip 展示在 header 的上方呢？其实非常的简单，我们完全不需要给 main 标签添加 z-index:</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a56dc7a24e0144a1a94a7fbc58213b55~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>没了 z-index 的 main 标签不会去创建上下文。
现在我们再去看代码的上下文结构将会是这样的：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b321be232af242b1b01df80cfff914f8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>现在，因为 header 和 tooltip 元素在相同的上下文中，他们的 z-index 变开始较量，最后决出胜利者！</p>
<p><strong>注意</strong>： 这里我们不是在讨论那些元素的父子关系。不管 tooltip 是多么复杂地被其他元素所嵌套，浏览器只关心层叠上下文。</p>
<blockquote>
<h3 data-id="heading-3">打破规则</h3>
<p>在上面更改代码的例子中，我们只是把 z-index 从 main 标签中移除了，因为刚刚 z-index 完全没有起什么作用。 但是如果 main 标签真的需要 z-index 来创建一个上下文呢？怎么样在不移除 z-index 的情况下来实现呢？</p>
<p>根据CSS的规则，很遗憾我们没有办法通过其他CSS方法达成我们要的效果：一个上下文里的元素永远都不能拿来和其他上下文比较。</p>
<p>幸运的是，我们还是可以通过其他方法来达成那样的效果，我们需要动一下小脑筋。</p>
<p>我们可以把 tooltip 移出 main 标签，挂在 body 标签下面，然后通过 CSS 定位来让 tooltip 看起来是 header 的子元素。</p>
</blockquote>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c813d564d0b34a139e77998c3e6fa098~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">更多创建层叠上下文的方法</h2>
<p>我们已经见到了如何通过结合 relative absolute 和 z-index 的方法来创建上下文，但是那不是唯一的方法！我们还可以通过这些法子：</p>
<ul>
<li>把透明度 opacity 设置成比 1 小的值</li>
<li>把 position 设置为 fixed 或者 sticky （这种情况无需提供 z-index)</li>
<li>把 mix-blend-mode 设置为 multiply、hard-light、difference（normal不行🙅）</li>
<li>把 z-index 添加到一个带有 display：flex 或者 display： grid 的容器里</li>
<li>使用 transform， filter， clip-path，或者 perpective</li>
<li>把 will-change 设置为 opacity 或者 transform</li>
<li>通过 isolation: isolation 直接创建上下文（很快就会讲到这个的使用！）</li>
<li>其他详见 <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context#the_stacking_context" target="_blank" rel="nofollow noopener noreferrer">MDN 实现清单</a></li>
</ul>
<p>下面这个例子中我们使用了 will-change 给 main 标签创建了一个上下文，所以我们依旧得到了之前的结果：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8d26123268e4b889988422a50daad09~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">z-index 的常见误知</h2>
<p>我们已经知道了为了让 z-index 生效，我们需要去给 position 设置成 relative 和 absolute 对吧？</p>
<p>其实不完全是这样的，再来看看下面这段代码：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23678c20684d46f7b258ec211638d82c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>第二个盒子被赋值了 z-index 被展示在其他盒子的上方。但是我们看不到哪里声明了 position 对吧！</p>
<p>大部分情况下，z-index 只能在拥有 position 的元素生效（relative/absolute）。但是在 flexbox 布局时，flex 子元素的 z-index 即使 position 为 static 也可以生效哦～</p>
<h2 data-id="heading-6">再让我们捋一捋。。</h2>
<p>有件奇怪的事我们可能需要再仔细琢磨一下。</p>
<p>在之前的PS比喻中，我们能很好的区分组的概念和层级的概念：所有可视的元素都是层级，组只是一个来帮助组合层级的容器而已。</p>
<p>在浏览器里，这个概念就有一些些模糊。所有使用了 z-index 的元素创建了上下文。</p>
<p>一般来说当我们决定使用 z-index 的时候，我们的目的仅仅是希望改变那个元素在当前父上下文的位置。我们并不希望在那个元素上创建一个上下文！我们需要在这个上面再好好考虑一下。</p>
<p>当一个上下文被创建了，它会把所有子元素给扁平化。所有子元素给安排的明明白白，我们本质上把他们都锁在了内部。</p>
<p>我们不应该把 z-index 只想象成改变元素顺序的工具，我们也应该把它当成包裹（组合）它子元素的方法。如果组没有生成的话 z-index 是不会生效的。</p>
<blockquote>
<p>我们已经见到了之前的例子，上下文有时候会造成细微的，难debug的情况。假如 z-index 能在全局进行比较会不会好一些呢？</p>
<p>我不觉得，这是一些我的理由：</p>
<ol>
<li>
<p>假如我们有一个很复杂的结构，我们需要给很多很多元素赋予 z-index，z-index 通货膨胀了解一下！</p>
</li>
<li>
<p>虽然我不是个浏览器工程师，我能想象现在的设计有助于浏览器的执行效率。没有现在的设计，浏览器需要和许多有 z-index 的元素进行比较，感觉上会有很多额外的工作要做！</p>
</li>
<li>
<p>当我们理解了上下文，我们可以借此去封印一些元素。在组件驱动的框架里这是个非常强大的模式，比如 React。</p>
</li>
</ol>
<p>最后一点是最有趣的点了，让我们多看看吧！</p>
</blockquote>
<h2 data-id="heading-7">用 isolation 实现全密封抽象</h2>
<p>现在我要和你们介绍我最喜欢的，也是最复杂的一个 CSS 属性： isolation 属性，隐藏在这个语言里的宝藏男孩。</p>
<p>你可以这样去使用它：</p>
<pre><code class="copyable">.wrapper &#123;
  isolation: isolate;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们使用这个来声明一个元素，它制作了一件事情：创建一个新的上下文。</p>
<p>为什么有这么多方法来创建一个上下文呢？哈哈，因为所有其他的方法都是隐式创建了上下文，其他的更改可能会改变其结果。 但是 isolation 可以用最纯粹简单方法创造上下文。</p>
<ul>
<li>不需要去规定 z-index</li>
<li><strong>可以在 static 定位的元素上使用！</strong></li>
<li>不会影响到子元素的渲染</li>
</ul>
<p><strong>再强调一次，因为这个实在是太棒了！isolation 可以在 static 定位的元素上使用！它可以让我们封印它的子元素！</strong></p>
<p>让我们再来看另外一个例子。最近我搭建了一个很赞的信封组件。</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05b93793a4384293a99991604428f4d4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当你把鼠标移到开口处，一封信会像这样划出来</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61456c67ddd14dd89002ee46ca0d0e92~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这个信封组件的结构分为四个部分（从左到右：信封后面的开口贴，信封后面，一封信，信的正面）</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0734d43973594632bcb3e0d9953c3306~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我把这个结构用 React 组件打包在一起，看起来是这个样子（为了让大家简单的看到，我使用了内敛样式）</p>
<pre><code class="copyable">function Envelope(&#123; children &#125;) &#123;
  return (
    <div>
      <BackPane style=&#123;&#123; zIndex: 1 &#125;&#125; /> 信的正面
      <Letter style=&#123;&#123; zIndex: 3 &#125;&#125;> 信
        &#123;children&#125;
      </Letter>
      <Shell style=&#123;&#123; zIndex: 4 &#125;&#125; /> 信封后面
      <Flap style=&#123;&#123; zIndex: isOpen ? 2 : 5 &#125;&#125; /> 开口贴
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（你可能好奇为什么开口贴的 z-index 是动态的， 因为它在打开时需要展示在信的后面）</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a59ffe9088f4ac7abc1b7bed4f9e73c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>一个好的 React 组件是到哪里都可以使用，是一个独立的封闭的，就像一件太空服。目前我们这个太空服很不幸漏气了。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcc0324f83b841979ff3edb3b798d318~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af13b8942d6f4028ad9a3f3bd0326b05~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当我把这个组件放在一个 z-index: 3 的 header 旁边时，如上图所示我们的层级和 header 被混淆在了一起。 因为我们的信封 Envelope 是由 div 包裹着四个层级，但它本身没有创建一个上下文。</p>
<p>但我们可以给 Envelope 组件外层的 div 添加 isolation: isolate 来保证组件能划成一个组。</p>
<pre><code class="copyable">function Envelope(&#123; children &#125;) &#123;
  return (
    <div style=&#123;&#123; isolation: 'isolate' &#125;&#125;>
      <BackPane style=&#123;&#123; zIndex: 1 &#125;&#125; />
      <Letter style=&#123;&#123; zIndex: 3 &#125;&#125;>
        &#123;children&#125;
      </Letter>
      <Shell style=&#123;&#123; zIndex: 4 &#125;&#125; />
      <Flap style=&#123;&#123; zIndex: isOpen ? 2 : 5 &#125;&#125; />
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么，为什么我们不用之前的方法 position: relative； z-index：1 来创建上下文呢？那是因为 React 组件是期望被重复使用的， z-index：1 不能保证在其他情况下是正确的。isolation 的魅力就是你可以保证这个组件永远是灵活的。</p>
<blockquote>
<p>浏览器支持
isolation 不是一个新的熟悉，他有很好的浏览器支持。它可以在除了 Internet Explorer 以外的任何浏览器上使用。</p>
<p>假如你想在 Internet Explorer 上支持，你可以考虑使用 transform：translate(0px)</p>
</blockquote>
<h2 data-id="heading-8">Debug 上下文</h2>
<p>很遗憾， 我没有找到很多能帮助 debug 上下文的工具。</p>
<p>Microsoft Edge 有一个很有趣的 <a href="https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/3d-view/" target="_blank" rel="nofollow noopener noreferrer">"3D视图"</a> 可以帮助显示上下文的结构。</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5886dade5554738a2fc120d8ff76bc4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>实际上讲，这个东西其实我感觉看起来很累，不能感觉他能帮助我去定位我 app 中的元素，也不能帮我去理解我 app 里的上下文关系。</p>
<p>其实我还有一个另外的小点子，那就是 offsetParent。</p>
<pre><code class="copyable">const element = document.querySelector('.tooltip');
console.log(element.offsetParent); // <main>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>offsetParent 会返回一个最近且带有非static值（relative, absolute, fixed）的position的祖先节点。</p>
<blockquote>
<p>注意：这不是一个最完美的解决方法。不是所有上下文都是用 position 来布局的，而且不是所有 position 定位的元素都会创建一个上下文！但这个方法至少是一个用来检测的起点。</p>
<p>假如你有新的方法，可以通过 Twitter 来联系我！：
<a href="https://twitter.com/JoshWComeau" target="_blank" rel="nofollow noopener noreferrer">twitter.com/JoshWComeau</a></p>
</blockquote>
<p><strong>更新1:</strong> Felix Becker 告诉我一个 <a href="https://marketplace.visualstudio.com/items?itemName=felixfbecker.css-stacking-contexts" target="_blank" rel="nofollow noopener noreferrer">VSCode 插件</a>可以用来高亮生成上下文的代码：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f4afc84435c447c8229394659458890~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>(这个插件能在 .css 和 .scss 文件使用）</p>
<p><strong>更新2:</strong> Giuseppe Gurgone 告诉我一个 谷歌浏览器插件可以在 devtools 添加新的 <a href="https://chrome.google.com/webstore/detail/z-context/jigamimbjojkdgnlldajknogfgncplbh" target="_blank" rel="nofollow noopener noreferrer">“z-index"</a></p>
<p><strong>更新3:</strong> Andrea Dragotta 发明了一个超赞的浏览器插件，它可以让我们看到一大堆超有用关于 z-index 和上下文的信息：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0a2b1b829624ef4b8516a11e2ae2735~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这个东西真的是超赞超牛，我最近一直在用这个插件。</p>
<p><a href="https://chrome.google.com/webstore/detail/css-stacking-context-insp/apjeljpachdcjkgnamgppgfkmddadcki" target="_blank" rel="nofollow noopener noreferrer">谷歌</a>
<a href="https://addons.mozilla.org/en-US/firefox/addon/css-stacking-context-inspector/" target="_blank" rel="nofollow noopener noreferrer">火狐</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            