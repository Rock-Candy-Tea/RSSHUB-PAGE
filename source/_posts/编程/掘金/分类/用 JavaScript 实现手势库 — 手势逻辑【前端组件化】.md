
---
title: '用 JavaScript 实现手势库 — 手势逻辑【前端组件化】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfe75f61c9da4b9697296336755ccf2b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 04 May 2021 08:01:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfe75f61c9da4b9697296336755ccf2b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前端组件化系列目录</h2>
<ul>
<li>「一」<a href="https://juejin.cn/post/6915319815041187848" target="_blank">用 JSX 建立组件 Parser（解析器）</a></li>
<li>「二」<a href="https://juejin.cn/post/6918276702061723655" target="_blank">使用 JSX 建立 Markup 组件风格</a></li>
<li>「三」<a href="https://juejin.cn/post/6925698689704919053" target="_blank">用 JSX 实现 Carousel 轮播组件</a></li>
<li>「四」<a href="https://juejin.cn/post/6947519943332069390" target="_blank">用 JavaScript 实现时间轴与动画</a></li>
<li>「五」<a href="https://juejin.cn/post/6955075376674504712" target="_blank">用 JavaScript 实现手势库 - 实现监听逻辑</a></li>
<li>「六」用 JavaScript 实现手势库 — 手势逻辑  《 本期 》</li>
<li>... 待续 ...</li>
</ul>
<hr>
<p>上一期《<a href="https://juejin.cn/post/6955075376674504712" target="_blank">实现监听逻辑</a>》中我们一起实现了<strong>基础的手势监听逻辑</strong>。有了这些手势的监听后，我们就可以开始实现每一个手势的逻辑。最终我们可以把这些手势应用到我们的《<a href="https://juejin.cn/post/6925698689704919053" target="_blank">轮播图组件</a>》当中。</p>
<p>接下来我们就开始实现 gesture 的逻辑。</p>
<hr>
<h2 data-id="heading-1">Start 事件</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfe75f61c9da4b9697296336755ccf2b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先我们会触发一个 start 事件，也就是当我们手指触摸到屏幕时第一个触发的事件。这时会有三种情况：</p>
<ul>
<li><strong>手指松开</strong>
<ul>
<li>会触发 end 事件，这样就构成一个 <code>tap</code> 点击的行为</li>
<li>通过监听 end 事件来实现即可</li>
</ul>
</li>
<li><strong>手指拖动超过 10 px</strong>
<ul>
<li>这种就是 <code>pan start</code> 拖动的行为</li>
<li>我们可以在 move 事件判断当前与上一个触点的距离</li>
</ul>
</li>
<li><strong>手指停留在当前位置超过 0.5s</strong>
<ul>
<li>这种就是 <code>press start</code> 按压的行为</li>
<li>我们可以添加一个 setTimeout 来实现</li>
</ul>
</li>
</ul>
<hr>
<h2 data-id="heading-2">Press 事件</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c784ccb913b4a6ab360290d77a0e44c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以我们第一步就是在 <code>start</code> 函数中加入一个 <code>setTimout</code> 的 handler 处理程序。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> handler;

<span class="hljs-keyword">let</span> start = <span class="hljs-function"><span class="hljs-params">point</span> =></span> &#123;
  handler = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'presss '</span>);
  &#125;, <span class="hljs-number">500</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般来说 <code>press</code> 是我们比较常见的一个行为。但是实际上这里是 press start 事件，后面还会跟随着一个 press end 的事件。我们也可以统称这个为 <code>press</code> 事件，然后这个手势库的使用者只需要监听这个 <code>press</code> 事件即可，极少的情况下是需要监听 <code>press end</code> 事件的。</p>
<p>这里我们需要注意的是，当我们触发其他的事件的时候，这个 500 毫秒的 setTimout 是有可能会被取消掉的。所以我们需要给这段逻辑一个 <code>handler</code>，并且放在全局作用域中，让其他事件可以获取到这个变量，并且可使用它取消掉这个处理逻辑。</p>
<hr>
<h2 data-id="heading-3">Pan 事件</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e23256695c8347bbbdda2035d8768b48~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们就去监听移动 10px 的 <code>pan</code> 事件，这里就需要我们记录一开始用户触摸屏幕时的 x 和 y 坐标，当用户移动手指的时候，持续计算新移动到的位置与初始位置的距离。如果这个距离超过了 10px 就可以触发我们的 <code>pan start</code> 的事件了。</p>
<p>所以首先我们需要在 start 函数中加入 <code>startX</code> 和 <code>startY</code> 的坐标记录，这里要注意的是，因为这两个值都是会在多个地方被使用的，所以也是需要在全局作用域中声明。</p>
<p>然后在 <code>move</code>  函数中计算当前触点与起点的直径距离。这里我们需要用到数学中的直径运算公式 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><msup><mi>z</mi><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">x^2 + y^2 = z^2</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.897438em;vertical-align:-0.08333em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:1.008548em;vertical-align:-0.19444em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.04398em;">z</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span></span>，而这里面的 x 是 <code>当前触点的 x 坐标</code> - <code>起点的 x 坐标</code> 的 x 轴的距离， y 就是 <code>当前出点的 y 坐标</code> - <code>起点的 y 坐标</code> 运算出来的 y 轴的距离。<strong>最终两个距离二次幂相加就是直径距离的二次幂</strong>。</p>
<p>在代码中我们一般都会尽量避免使用根号运算，因为根号运算会对性能有一定的影响。我们知道最终要判断的是直径距离是否是大于一个固定的 10px。那就是说 z = 10，而 z 的二次幂就是 100，所以我们直接判断这个直径距离是否大于 100 即可。</p>
<blockquote>
<p>这里还有一个需要注意的，就是当我们手指移动超过 10px 之后，如果我们手指没有离开屏幕而是往回移动了，这样的话我们距离起点已经不够 10px了。但是这个其实也是算 pan 事件，因为我们确实有移动超过 10px 距离，超过这个距离之后所有的移动都是属于 pan 事件。</p>
</blockquote>
<p>所以我们需要一个 <code>isPan</code> 的状态，第一次移动超出 10px 的时候，就会触发 <code>pan-start</code> 事件，并且把 <code>isPan</code> 置为 true，而后面的所有移动都会触发 <code>pan</code> 事件。</p>
<p>根据我们上面讲到的 <code>press</code> 事件，如果我们按下手指后 0.5 秒内出现了移动，那么 <code>press</code> 事件就会被取消。所以这里我们就需要 <code>clearTimeout</code> 把 <code>pressstart</code> 的 <code>handler</code> 给清楚掉。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> handler;
<span class="hljs-keyword">let</span> startX, startY;
<span class="hljs-keyword">let</span> isPan = <span class="hljs-literal">false</span>;

<span class="hljs-keyword">let</span> start = <span class="hljs-function"><span class="hljs-params">point</span> =></span> &#123;
  (startX = point.clientX), (startY = point.clientY);

  isPan = <span class="hljs-literal">false</span>;

  handler = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'pressstart'</span>);
  &#125;, <span class="hljs-number">500</span>);
&#125;;

<span class="hljs-keyword">let</span> move = <span class="hljs-function"><span class="hljs-params">point</span> =></span> &#123;
  <span class="hljs-keyword">let</span> dx = point.clientX - startX,
    dy = point.clientY - startY;

  <span class="hljs-keyword">let</span> d = dx ** <span class="hljs-number">2</span> + dy ** <span class="hljs-number">2</span>;

  <span class="hljs-keyword">if</span> (!isPan && d > <span class="hljs-number">100</span>) &#123;
    isPan = <span class="hljs-literal">true</span>;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'pan-start'</span>);
    <span class="hljs-built_in">clearTimeout</span>(handler);
  &#125;

  <span class="hljs-keyword">if</span> (isPan) &#123;
    <span class="hljs-built_in">console</span>.log(dx, dy);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'pan'</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-4">Tap 事件</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84e2ae5cf93f413ca86f62100918f183~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Tap 的这个逻辑我们可以在 end 事件里面去检查。首先我们默认有一个 <code>isTap</code> 等于 true 的状态，如果我们触发了 pan 事件的话，那就不会去触发 tap 的逻辑了，所以 tap 和 pan 是互斥的关系。但是为了不让它们变得很耦合，所以我们不使用原有的 isPan 作为判断状态，而是另外声明一个 <code>isTap</code> 的状态来记录。</p>
<p>这里我们 tap 和 pan 都有单独的状态，那么我们 press 也不例外，所以也给 press 加上一个 <code>isPress</code> 的状态，它的默认值是 false。如果我们 0.5 秒的定时器被触发了，<code>isPress</code> 也就会变成 true。</p>
<p>既然我们给每个事件都加入了状态，那么这里我们就给每一个事件触发的时候设置好这些状态的值。</p>
<ul>
<li><strong>press 时</strong>
<ul>
<li>isTap = false</li>
<li>isPan = false</li>
<li>isPress = true</li>
</ul>
</li>
<li><strong>pan 时</strong>
<ul>
<li>isTap = false</li>
<li>isPan = true</li>
<li>isPress = false</li>
</ul>
</li>
<li><strong>tap 时</strong>
<ul>
<li>isTap = true</li>
<li>isPan = false</li>
<li>isPress = false</li>
</ul>
</li>
</ul>
<p>如果我们发现用户没有移动，也没有按住触屏超过 0.5 秒，当用户离开屏幕时就会调用 end 函数，这个时候我们就可以认定用户的操作就是 tap。这里我们要注意的是，我们 press 的 0.5 秒定时器是没有被关闭的，所以我们在 isTap 的逻辑中需要 <code>clearTimeout(handler)</code>。</p>
<p>说到取消 press 定时器，其实我们 handler 的回调函数中，也需要做一个保护代码逻辑，在触发了 press-start 之后，我们需要保证每次点击屏幕只会触发一次，所以在 setTimout 的回调函数中的最后，我们需要加上 <code>handler = null</code>。这样只要 press-start 触发了，就不会再被触发。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> handler;
<span class="hljs-keyword">let</span> startX, startY;
<span class="hljs-keyword">let</span> isPan = <span class="hljs-literal">false</span>,
  isPress = <span class="hljs-literal">false</span>,
  isTap = <span class="hljs-literal">false</span>;

<span class="hljs-keyword">let</span> start = <span class="hljs-function"><span class="hljs-params">point</span> =></span> &#123;
  (startX = point.clientX), (startY = point.clientY);

  isPan = <span class="hljs-literal">false</span>;
  isTap = <span class="hljs-literal">true</span>;
  isPress = <span class="hljs-literal">false</span>;

  handler = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    isPan = <span class="hljs-literal">false</span>;
    isTap = <span class="hljs-literal">false</span>;
    isPress = <span class="hljs-literal">true</span>;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'press-start'</span>);
    handler = <span class="hljs-literal">null</span>;
  &#125;, <span class="hljs-number">500</span>);
&#125;;

<span class="hljs-keyword">let</span> move = <span class="hljs-function"><span class="hljs-params">point</span> =></span> &#123;
  <span class="hljs-keyword">let</span> dx = point.clientX - startX,
    dy = point.clientY - startY;

  <span class="hljs-keyword">let</span> d = dx ** <span class="hljs-number">2</span> + dy ** <span class="hljs-number">2</span>;

  <span class="hljs-keyword">if</span> (!isPan && d > <span class="hljs-number">100</span>) &#123;
    isPan = <span class="hljs-literal">true</span>;
    isTap = <span class="hljs-literal">false</span>;
    isPress = <span class="hljs-literal">false</span>;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'pan-start'</span>);
    <span class="hljs-built_in">clearTimeout</span>(handler);
  &#125;

  <span class="hljs-keyword">if</span> (isPan) &#123;
    <span class="hljs-built_in">console</span>.log(dx, dy);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'pan'</span>);
  &#125;
&#125;;

<span class="hljs-keyword">let</span> end = <span class="hljs-function"><span class="hljs-params">point</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (isTap) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'tap'</span>);
    <span class="hljs-built_in">clearTimeout</span>(handler);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-5">End 事件</h2>
<p>到了最后这里我们要处理的就是所有的结束时间，包括 <code>press-end</code> 和 <code>pan-end</code>。</p>
<p>这两个 end 事件都会在 end 函数中判断所得，如果在用户操作的过程中触发了 <code>pan-start</code> 或者 <code>press-start</code> 事件，到了 end 函数这里，对应的状态就会是 true。</p>
<p>所以我们对 end 函数做了以下改造：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> end = <span class="hljs-function"><span class="hljs-params">point</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (isTap) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'tap'</span>);
    <span class="hljs-built_in">clearTimeout</span>(handler);
  &#125;

  <span class="hljs-keyword">if</span> (isPan) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'pan-end'</span>);
  &#125;

  <span class="hljs-keyword">if</span> (isPress) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'press-end'</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们需要在 cancel 事件触发的时候，清楚掉 press 事件的 setTimeout。既然我们的操作被打断了，那也不可能会触发我们的长按事件了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 加入 cancel</span>
<span class="hljs-keyword">let</span> cancel = <span class="hljs-function"><span class="hljs-params">point</span> =></span> &#123;
  <span class="hljs-built_in">clearTimeout</span>(handler);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'cancel'</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>我们除了 <code>flick</code> 的逻辑，我们已经完成所有手势库里面的事件了。并且也能正确的区分这几种手势操作了。</p>
</blockquote>
<hr>
<p>这期我们就先到这里啦，下期我们就来一起完整这个手势库的逻辑，并且重新整理一次这里面的状态！～ 敬请期待，记得持续关注<strong>三哥</strong>哦～</p>
<blockquote>
<p>我是来自《<strong>技术银河</strong>》的<strong>三钻</strong>，一位正在重塑知识的技术人。下期再见。</p>
</blockquote>
<hr>
<h2 data-id="heading-6">⭐️ 三哥推荐</h2>
<h3 data-id="heading-7">开源项目推荐</h3>
<h4 data-id="heading-8">Hexo Theme Aurora</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c8b17bc9f4248c4991a242c1375db68~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d44d92571d548278a5952aa97283d6b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>在最近更新到版本 1.5.0，包含以下内容：</p>
<p>》<a href="https://tridiamond.tech/" target="_blank" rel="nofollow noopener noreferrer">预览</a>《</p>
</blockquote>
<p>:sparkles: 新增</p>
<ul>
<li>自适应 “推荐文章” 布局 (增加了一个新的 “<code>置顶文章布局</code>” !!)
<ul>
<li>能够在“推荐文章”和“置顶文章”模式之间自由切换</li>
<li>如果总文章少于 3 篇，将自动切换到“置顶文章”模式</li>
<li>在文章卡上添加了“置顶”和“推荐”标签</li>
<li><a href="https://aurora.tridiamond.tech/zh/guide/theme.html#%E6%8E%A8%E8%8D%90%E5%B8%83%E5%B1%80%E6%A8%A1%E5%BC%8F" target="_blank" rel="nofollow noopener noreferrer">:book: 文档</a></li>
</ul>
</li>
<li>增加了与 VuePress 一样的自定义容器 <a href="https://github.com/auroral-ui/hexo-theme-aurora/issues/77" target="_blank" rel="nofollow noopener noreferrer">#77</a>
<ul>
<li><code>Info</code> 容器</li>
<li><code>Warning</code> 容器</li>
<li><code>Danger</code> 容器</li>
<li><code>Detail</code> 容器</li>
<li><a href="https://tridiamond.tech/post/aurora%2Fcustom-quotes" target="_blank" rel="nofollow noopener noreferrer">预览</a></li>
</ul>
</li>
<li>支持了更多的 SEO meta 数据 <a href="https://github.com/auroral-ui/hexo-theme-aurora/issues/76" target="_blank" rel="nofollow noopener noreferrer">#76</a>
<ul>
<li>添加了 <code>description</code></li>
<li>添加了 <code>keywords</code></li>
<li>添加了 <code>author</code></li>
<li><a href="https://aurora.tridiamond.tech/zh/guide/site-meta.html#seo-meta" target="_blank" rel="nofollow noopener noreferrer">:book: 文档</a></li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0da1cb0eae74a7bb2a12cb556a99f88~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最近博主在全面投入开发一个可以 “<strong>迈向未来的</strong>” Hexo 主题，以极光为主题的博客主题。</p>
<p>如果你是一个开发者，做一个个人博客也是你简历上的一个亮光点。而如果你有一个超级炫酷的博客，那就更加是亮上加亮了，简直就闪闪发光。</p>
<p>如果喜欢这个主题，可以在 Github 上给我点个 🌟 让彼此都发光吧～</p>
<blockquote>
<p>主题 Github 地址：<a href="https://github.com/auroral-ui/hexo-theme-aurora" target="_blank" rel="nofollow noopener noreferrer">github.com/auroral-ui/…</a>
主题使用文档：<a href="https://aurora.tridiamond.tech/zh/" target="_blank" rel="nofollow noopener noreferrer">aurora.tridiamond.tech/zh/</a></p>
</blockquote>
<hr>
<h4 data-id="heading-9">VSCode Aurora Future</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad7e1249a2e7497d9df682620fa8a420~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
对，博主还做了一个 Aurora 的 VSCode 主题。用了Hexo Theme Aurora 相对应的颜色色系。这个主题的重点特性的就只用了 3 个颜色，减少在写代码的时候被多色多彩的颜色所转移了你的注意力，让你更集中在写代码之中。</p>
<p>喜欢的大家可以支持一下哦！ <strong>直接在 VSCode 的插件搜索中输入 “Aurora Future” 即可找到这个主题哦！～</strong></p>
<blockquote>
<p>主题 Github 地址：<a href="https://github.com/auroral-ui/aurora-future-vscode-theme" target="_blank" rel="nofollow noopener noreferrer">github.com/auroral-ui/…</a>
主题插件地址：<a href="https://marketplace.visualstudio.com/items?itemName=auroral-ui.aurora-future" target="_blank" rel="nofollow noopener noreferrer">marketplace.visualstudio.com/items?itemN…</a></p>
</blockquote>
<hr>
<h4 data-id="heading-10">Firefox Aurora Future</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c795f9193c764378aa219d3d1d9650d3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">我不知道大家，但是最近我在用火狐浏览器来做开发了。个人觉得火狐还真的是不错的。推荐大家尝试一下。</p>
<p>当然我这里想给大家介绍的是我在火狐也做了一个 Aurora 主题。对的！用的是同一套的颜色体系。喜欢的小伙伴可以试一下哦！</p>
<blockquote>
<p>主题地址：<a href="https://addons.mozilla.org/en-US/firefox/addon/aurora-future/" target="_blank" rel="nofollow noopener noreferrer">addons.mozilla.org/en-US/firef…</a></p>
</blockquote></div>  
</div>
            