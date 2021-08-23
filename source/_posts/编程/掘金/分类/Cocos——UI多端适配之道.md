
---
title: 'Cocos——UI多端适配之道'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70178af91c924deea9de56e133f2a086~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 04:16:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70178af91c924deea9de56e133f2a086~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>前端同学通常都用媒体查询或 rem 做多端适配，但是在 Cocos 上 CSS 不复存在。那你知道在 Cocos 上如何做到多端适配吗？本文从需求背景出发，带你领略 Cocos 的多端适配之道～</p>
</blockquote>
<h2 data-id="heading-0">背景</h2>
<p>某一天接到了新需求，自己看了设计同学给的设计稿后瞬间感觉头大，分析了下主要有以下难点：</p>
<ol>
<li>题目背景需为同一张背景图，在不同端上要显示背景图的不同区域</li>
<li>标题栏上的倒计时、题干与最小化按钮的贴边距离在各端各不相同</li>
<li>选项背景图需根据选项长度自动拉伸，同时保证两侧圆角不被拉伸</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70178af91c924deea9de56e133f2a086~tplv-k3u1fbpfcp-watermark.image" alt="多端设计稿图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果这种适配方案采用CSS实现的话，肯定少不了一大堆的媒体查询，作为前端同学来说 CSS 实现肯定更为熟悉，但这也会导致样式代码冗长繁琐，对开发者来说是一种折磨。业务中这几年引进了 Cocos 游戏引擎来实现新题型，曾经我们那样熟悉的CSS在Cocos中将不复存在，这时在Cocos上我们要如何实现这种多端适配呢？</p>
<h2 data-id="heading-1">分析</h2>
<p>针对这个需求，我们将适配的过程拆分成以下几点：</p>
<ol>
<li>多端适配背景图</li>
<li>多端适配贴边节点</li>
<li>选项背景图九宫格切割</li>
</ol>
<h2 data-id="heading-2">多端适配背景图</h2>
<ol>
<li>
<p>什么是设计分辨率和屏幕分辨率？</p>
<p>​在Cocos上做多端适配需要先了解什么是设计分辨率和屏幕分辨率。根据 Cocos 官方文档的介绍，<strong>设计分辨率</strong> 是内容生产者在制作场景时使用的分辨率蓝本，而 <strong>屏幕分辨率</strong> 是游戏在设备上运行时的实际屏幕显示分辨率。在实际开发中，设计分辨率其实就是<strong>设计同学在设计稿中使用最多的尺寸</strong>，一般来说都是 iPhone 6 的 667*375，几乎所有的设计稿都以这个尺寸来出图，然后才会针对不同端（ PC 、iPad、iPhoneX等）来单独出适配的设计稿图。所以我们在 Cocos 中 canvas 的大小通常就设置成宽为 667，高为 375 的设计分辨率，在此分辨率上完成基本的功能开发。</p>
</li>
<li>
<p>设计分辨率和屏幕分辨率的关系？</p>
<p>​假设我们的设计分辨率与屏幕分辨率同为 667 x 375，这时候 canvas 不用缩放就可以完美适配屏幕；假设我们的设计分辨率为 667 x 375，而实际屏幕分辨率为1334 x 750，这个时候 canvas 就需要放大两倍才能够完美适配屏幕。<strong>canvas 进行缩放时，场景下所有的节点都能够享受到基于设计分辨率的智能缩放</strong>。</p>
</li>
<li>
<p>Fit Height 和 Fit Width</p>
<p>​上一点举出的例子中，当设计分辨率为 667 x 375 且屏幕分辨率为 1334 x 750 时，场景需要放大两倍才能够完美适配屏幕，但这个的前提是设计分辨率和屏幕分辨率的宽高比一致。假设设计分辨率的宽高比与屏幕分辨率的宽高比不一致（这是在多端适配下常见的问题），这个时候该怎么办呢？canvas 组件提供了 Fit Height 与 Fit Width 两种适配模式来帮助我们解决。该怎么理解这两种适配模式？</p>
<p>我们以下面这个场景作为基础场景，紫色框为我们的设计分辨率，蓝色框为实际场景：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f857ba2f36a0466a99db36539fd14d0d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>先看看<strong>屏幕分辨率宽高比小于设计分辨率宽高比</strong>的情况（iPad情况）。</p>
<p>​我们先设置为 Fit Height 模式看看效果，会发现设计分辨率的高度会自动撑满屏幕的高度，而由于屏幕分辨率宽高比比设计分辨率小，所以屏幕两边也会被裁掉一部分背景图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b5735d056904cedbf08ea95af1fee25~tplv-k3u1fbpfcp-watermark.image" alt="image-20210720161814021" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​我们再设置为 Fit Width 模式看看效果，会发现设计分辨率的宽度会自动撑满屏幕的宽度，而由于屏幕分辨率宽高比比设计分辨率小，所以屏幕上下会多显示一部分背景图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6c956f06408415694bd7c30d928acc9~tplv-k3u1fbpfcp-watermark.image" alt="image-20210720162951727" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再看看<strong>屏幕分辨率宽高比大于设计分辨率宽高比</strong>的情况（iPhoneX 情况）</p>
<p>​我们先设置为 Fit Height 模式看看效果，会发现设计分辨率的高度会自动撑满屏幕的高度，而由于屏幕分辨率宽高比比设计分辨率大，所以屏幕两边也会多显示一部分背景图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16c1e64754404ea7b38a70fd47965736~tplv-k3u1fbpfcp-watermark.image" alt="image-20210720163452244" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​我们再设置为 Fit Width 模式看看效果，会发现设计分辨率的宽度会自动撑满屏幕的宽度，而由于屏幕分辨率宽高比比设计分辨率大，所以屏幕上下会被裁掉一部分背景图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7f817e2f80d4bba9035ce821469887b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210720163637108" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>背景多端适配用什么模式？</p>
<p>​经过上面 Fit Height 与 Fit Width 两种模式的解释，现在你能确定本文第一张图中每个端使用哪种模式进行适配吗？在屏幕分辨率宽高比小于设计分辨率宽高比（iPad 情况）时，我们希望在宽度一致的情况下在上下两侧展示更多的背景区域，这个时候就需要使用 Fit Width；在屏幕分辨率宽高比大于设计分辨率宽高比（iPhoneX 情况）时，我们希望在高度一致的情况下在左右两侧展示更多的背景区域，这个时候就需要使用 Fit Height。</p>
<p>​在代码中我们可以通过获取当前视图大小来得到实际屏幕分辨率的宽高比，根据宽高比来决定是使用 Fit Height 模式还是 Fit Width 模式。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setCanvasScaleMode</span>(<span class="hljs-params">canvas: cc.Canvas</span>) </span>&#123;
  <span class="hljs-keyword">const</span> standardRadio = <span class="hljs-number">16</span> / <span class="hljs-number">9</span>; <span class="hljs-comment">// 标准宽高比，差不多就是iPhone6的宽高比（横屏），一般设计稿以此为标准</span>
  <span class="hljs-keyword">const</span> screenSize = cc.view.getFrameSize();
  <span class="hljs-keyword">const</span> currentRadio = screenSize.width / screenSize.height; <span class="hljs-comment">// 宽高比</span>
  <span class="hljs-keyword">if</span> (currentRadio <= standardRadio) &#123;
    <span class="hljs-comment">// 偏方形的屏幕，代表是iPad之类的。</span>
    canvas.fitHeight = <span class="hljs-literal">false</span>;
    canvas.fitWidth = <span class="hljs-literal">true</span>;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 偏长的屏幕，代表是ipx。太长了，高度显得小，所以优先适配高度</span>
    canvas.fitWidth = <span class="hljs-literal">false</span>;
    canvas.fitHeight = <span class="hljs-literal">true</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​确定了模式之后我们还需要确保背景不会出现黑边，因为当在 iPad 情况下使用 Fit Width 模式时，上下两侧会展示更多的背景区域，如果背景图片没有那么高的话上下两侧就会出现黑边；同理当在 iPhoneX 情况下使用 Fit Height 模式时，左右两侧会展示更多的背景区域，如果背景图片没有那么宽的话左右两侧也会出现黑边。这时我们需要设计同学提供的背景图片时能够覆盖 iPad 的高度与 iPhoneX 的宽度，背景图片应大于设计分辨率，并在上下左右四个方向都预留一定的长度来保证背景适配时不会出现黑边。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c65fa9c9e7e54144b7ed51048c0a6c58~tplv-k3u1fbpfcp-watermark.image" alt="image-20210720165444137" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>特殊情况</p>
<p>​细心的同学可能已经发现了， PC 端与 iPhone7 端的宽高比其实是一样的，按照我们上面的想法这两端应该显示一样的背景区域，同时由于 PC 端的宽高比 iPhone7 的宽高要大，而<strong>场景中的所有节点都能享受到基于设计分辨率的智能缩放</strong>，所以 PC 端的节点应该比 iPhone7 的节点大。但是在第一张设计稿图中，设计同学要求 PC 端要占据更多的背景区域，同时其中节点的大小也与 iPhone7 中节点的大小保持相同，以保证 PC 端题目显示的美观，这个时候我们就需要单独对 PC 端的情况做适配，将背景图与节点都做下缩放。</p>
</li>
</ol>
<h2 data-id="heading-3">多端适配贴边节点</h2>
<ol>
<li>
<p>Widget 组件为何物？</p>
<p>​Widget 组件为 Cocos 中的一个 UI 布局组件，用于将当前节点对齐到父节点的任意位置，我们通过设置 Widget 组件的各种数值可以让节点对齐上边界、对齐下边界、对齐左边界、对齐右边界、水平方向居中和竖直方向居中。当场景中有节点需要贴边时 Widget 组件是不二的选择。</p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3aed6b178bcd449999b09c75bf141af4~tplv-k3u1fbpfcp-watermark.image" alt="image-20210720172226061" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>
<p>哪个节点作为贴边节点对齐的父节点？</p>
<p>​当有节点需要贴边时，我们希望的是无论屏幕分辨率如何改变，节点总是能在屏幕的固定位置出现。比如第一张设计稿图中的倒计时节点，我们希望在不同屏幕分辨率的情况下它都能够固定在屏幕左上角，不会出现随着屏幕分辨率的改变而移到右上角的情况。所以贴边节点指定的父节点大小要跟屏幕的大小一致，哪个节点最合适呢？</p>
<p>​没错，答案就是 canvas 节点！在我们使用 Fit Height 和 Fit Width 模式时，canvas 节点会占据屏幕的大小，这时需要贴边的节点相对于 canvas 节点设置贴边距离实际上就是相对屏幕设置贴边距离。</p>
</li>
<li>
<p>多端贴边距离设置</p>
<p>​根据设计同学的要求，贴边节点（例如倒计时节点）在 PC 端、iPad 端、iPhoneX 端和 iPhone7 端贴边的距离都是不一样的，这个时候我们如何根据不同端分别设置贴边距离呢？</p>
<p>​首先明确，设置多端节点的贴边距离实际上就是更改节点 Widget 组件在各个方向上对齐的数值，例如倒计时组件，我们先判断当前是哪一个端，然后再根据该端来改变其 Widget 组件的top与left数值。</p>
<p>​由于Widget的设置逻辑不仅需要在不同贴边节点执行，还需要在每个贴边节点的不同端情况下执行，使用场景众多，所以我们可以把这段逻辑抽出来作为一个通用脚本组件，再分别添加到需要的节点上。以下是我们抽出来的一个UIAdaptor脚本组件：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-meta">@ccclass</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UIAdaptor</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">cc</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-meta">@property</span>(&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
    <span class="hljs-attr">tooltip</span>: <span class="hljs-string">`app: <span class="hljs-subst">$&#123;PlatformTypes.APP&#125;</span>, iPad: <span class="hljs-subst">$&#123;PlatformTypes.iPad&#125;</span>,  PC : <span class="hljs-subst">$&#123;PlatformTypes. PC &#125;</span>, iPhoneX: <span class="hljs-subst">$&#123;PlatformTypes.iPhoneX&#125;</span>, AndroidiPad: <span class="hljs-subst">$&#123;PlatformTypes.AndroidiPad&#125;</span>`</span>,
  &#125;)
  <span class="hljs-attr">platform</span>: PlatformTypes = -<span class="hljs-number">1</span>;

  <span class="hljs-meta">@property</span>(&#123;
    <span class="hljs-attr">type</span>: [<span class="hljs-built_in">Number</span>],
    <span class="hljs-attr">tooltip</span>: <span class="hljs-string">'left, top, right, bottom, horizontalCenter, verticalCenter'</span>,
  &#125;)
  <span class="hljs-attr">widgetOptions</span>: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>> = [
    <span class="hljs-built_in">Number</span>.MAX_SAFE_INTEGER, <span class="hljs-built_in">Number</span>.MAX_SAFE_INTEGER, <span class="hljs-built_in">Number</span>.MAX_SAFE_INTEGER, <span class="hljs-built_in">Number</span>.MAX_SAFE_INTEGER,
    <span class="hljs-built_in">Number</span>.MAX_SAFE_INTEGER, <span class="hljs-built_in">Number</span>.MAX_SAFE_INTEGER,
  ];

  <span class="hljs-meta">@property</span>(&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
    <span class="hljs-attr">tooltip</span>: <span class="hljs-string">`ONCE: <span class="hljs-subst">$&#123;WidgetAlignModes.ONCE&#125;</span>, ON_WINDOW_RESIZE: <span class="hljs-subst">$&#123;WidgetAlignModes.ON_WINDOW_RESIZE&#125;</span>
      ALWAYS: <span class="hljs-subst">$&#123;WidgetAlignModes.ALWAYS&#125;</span>
    `</span>,
  &#125;)
  widgetAlignModes = WidgetAlignModes.ON_WINDOW_RESIZE;

  <span class="hljs-meta">@property</span>(&#123;
    <span class="hljs-attr">type</span>: [<span class="hljs-built_in">Number</span>],
    <span class="hljs-attr">tooltip</span>: <span class="hljs-string">'width, height'</span>,
  &#125;)
  <span class="hljs-attr">size</span>: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>> = [];

  <span class="hljs-meta">@property</span>(&#123;
    <span class="hljs-attr">type</span>: [<span class="hljs-built_in">Number</span>],
    <span class="hljs-attr">tooltip</span>: <span class="hljs-string">'x, y'</span>,
  &#125;)
  <span class="hljs-attr">scale</span>: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">number</span>> = [];

  <span class="hljs-meta">@property</span>(&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
  &#125;)
  fontSize = -<span class="hljs-number">1</span>;
<span class="hljs-comment">// 对节点的 Widget 组件做适配</span>
  <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">fitWidget</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> widget = <span class="hljs-built_in">this</span>.getComponent(cc.Widget);
    <span class="hljs-keyword">if</span> (!widget) &#123;
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-built_in">enum</span> WidgetOptions &#123;
      left,
      top,
      right,
      bottom,
      horizontalCenter,
      verticalCenter,
    &#125;
    <span class="hljs-built_in">this</span>.widgetOptions.forEach(<span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">number</span>, index: <span class="hljs-built_in">number</span></span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> value !== <span class="hljs-string">'number'</span> || value >= <span class="hljs-built_in">Number</span>.MAX_SAFE_INTEGER - <span class="hljs-number">1</span>) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;
      <span class="hljs-keyword">const</span> optionType = WidgetOptions[index];
      widget[optionType] = value;
      widget[<span class="hljs-string">`isAlign<span class="hljs-subst">$&#123;optionType.replace(optionType[<span class="hljs-number">0</span>], optionType[<span class="hljs-number">0</span>].toUpperCase())&#125;</span>`</span>] = <span class="hljs-literal">true</span>;
    &#125;);

    widget.alignMode = <span class="hljs-built_in">this</span>.widgetAlignModes;
  &#125;
<span class="hljs-comment">// 对节点的大小做适配</span>
  <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">fitSize</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> [width, height] = <span class="hljs-built_in">this</span>.size;
    <span class="hljs-built_in">this</span>.node.setContentSize(
      width,
      height
    );
  &#125;
<span class="hljs-comment">// 对节点的字体大小做适配</span>
  <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">fitFontSize</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> label = <span class="hljs-built_in">this</span>.getComponent(cc.Label);
    label.fontSize = <span class="hljs-built_in">this</span>.fontSize;
  &#125;
<span class="hljs-comment">// 对节点的缩放做适配</span>
  <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">fitScale</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">scaleX</span>: originalScaleX, <span class="hljs-attr">scaleY</span>: originalScaleY &#125; = <span class="hljs-built_in">this</span>.node;
    <span class="hljs-keyword">const</span> [x, y = x] = <span class="hljs-built_in">this</span>.scale;
    <span class="hljs-built_in">this</span>.node.setScale(originalScaleX * x, originalScaleY * y);
  &#125;

  <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">fit</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.size.length) &#123;
      <span class="hljs-built_in">this</span>.fitSize();
    &#125;

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.fontSize >= <span class="hljs-number">0</span>) &#123;
      <span class="hljs-built_in">this</span>.fitFontSize();
    &#125;

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.scale.length) &#123;
      <span class="hljs-built_in">this</span>.fitScale();
    &#125;

    <span class="hljs-built_in">this</span>.fitWidget();


    <span class="hljs-keyword">const</span> widget = <span class="hljs-built_in">this</span>.getComponent(cc.Widget);
    <span class="hljs-keyword">if</span> (widget) &#123;
      widget.updateAlignment();
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">start</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 获取当前场景所在的端</span>
    <span class="hljs-keyword">const</span> platform = getPlatformType();
    <span class="hljs-keyword">if</span> (platform === <span class="hljs-built_in">this</span>.platform) &#123;
      <span class="hljs-built_in">this</span>.fit();
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>​可以看到这个脚本组件不仅可以设置节点的 Widget 组件，还可以设置节点的 size、scale、fontSize 等，使用这一个脚本组件就可以实现多端下节点贴边距离、大小、缩放等的设置。我们还是看回刚才说到的倒计时节点，使用 UIAdaptor 脚本组件后会是什么样子？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13b58a78ffaa4436893752217c70460c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210720211558909" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​由于每个端上倒计时节点的贴边距离都不相同，所以我们针对每个端都在倒计时节点上添加一个 UIAdaptor 脚本组件，填写不同的Platform（ PC 、iPhoneX、iPad、Android iPad）与 Widget options（left、top、right、bottom、horizontalCenter、verticalCenter），当场景加载执行到这些脚本时会逐个去判断当前场景所在的端是不是与 UIAdaptor 选择的端一致，如果不是则跳过，如果是则根据填写的数值进行设置。通过这种方式我们可以<strong>无代码</strong>实现贴边节点的多端适配。</p>
</li>
</ol>
<h2 data-id="heading-4">选项背景图九宫格切割</h2>
<ol>
<li>
<p>为什么要对背景图做处理？</p>
<p>设计同学会给出第一张设计稿图中选项的切图，切图长下面这个样子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da1ecfa2946b4cbe8eb9a47a6a0ee823~tplv-k3u1fbpfcp-watermark.image" alt="image-20210721104946811" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果我们不对图片做任何处理，直接将它扔进选项，让它根据选项长度自动拉伸，会有什么状况发生呢？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23d14444f72743c7aac1fb492b8815cc~tplv-k3u1fbpfcp-watermark.image" alt="image-20210721105313047" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，在选项长度较大的情况下，选项的背景图展现出了一个很诡异的形状，四个圆角被拉伸地很不协调，如果被设计同学看到又少不了一通吐槽...我们希望的是无论选项有多长，四个圆角都能够保持原始状态，不被选项长度所影响，而这种未经处理的图片显然不符合我们的需求。</p>
</li>
<li>
<p>何为九宫格切割？</p>
<p>为了让开发者能够制作可任意拉伸的UI图像，Cocos Creator 中提供了针对图像资源的九宫格切割方式。我们在 Cocos Creator 中选中图像资源进行编辑，会出现一个编辑图像的弹窗：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ea06f30eee046a797d07f669229de99~tplv-k3u1fbpfcp-watermark.image" alt="image-20210721110533098" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这里我们可以移动绿色线条将图片资源切割成九部分，每个部分的拉伸规则如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec8415f9a1ad42d3aa1990ead36232ff~tplv-k3u1fbpfcp-watermark.image" alt="image-20210721110718219" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们将选项按钮的四个圆角切割到九宫格的四个角落，这样无论选项如何拉伸，四个圆角始终能够保持原始状态，不会因为选项长度的变化而缩放拉伸。来看看对图像资源进行九宫格切割后的效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c99db5c845514d27a39e04569776c71d~tplv-k3u1fbpfcp-watermark.image" alt="image-20210721111032269" loading="lazy" referrerpolicy="no-referrer"></p>
<p>怎么样，选项看起来是不是比刚才协调了很多？</p>
</li>
<li>
<p>九宫格切割注意事项</p>
<p>通常来说设计同学提供切图时会提供切图的一倍图、二倍图和三倍图，选择选项按钮切图的时候最好选择跟设计分辨率下按钮大小相近的倍图。假设按钮切图的一倍图高度为 44，二倍图高度为 88，三倍图高度为 132，而在设计分辨率下按钮的高度为 88，这个时候我们就要选择按钮切图的二倍图。</p>
<p>如果选择一倍图做九宫格切割，由于一倍图的尺寸过小，四个圆角也会变得很小，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4052ddffa5cf4392bcf91f855125e1c1~tplv-k3u1fbpfcp-watermark.image" alt="image-20210721113758845" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果选择三倍图做九宫格切割，由于三倍图尺寸过大，四个圆角也会变得很大，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efd7e9f731184982bbdeae630edc7ae1~tplv-k3u1fbpfcp-watermark.image" alt="image-20210721113910838" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ol>
<h2 data-id="heading-5">参考文章</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cocos.com%2Fcreator%2Fmanual%2Fzh%2Fui%2Fmulti-resolution.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cocos.com/creator/manual/zh/ui/multi-resolution.html" ref="nofollow noopener noreferrer">多分辨率适配方案</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cocos.com%2Fcreator%2Fmanual%2Fzh%2Fui%2Fsliced-sprite.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cocos.com/creator/manual/zh/ui/sliced-sprite.html" ref="nofollow noopener noreferrer">制作可任意拉伸的UI图像</a></li>
</ol>
<p><br><br></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1474641c84da4d22838159d50571e9f5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            