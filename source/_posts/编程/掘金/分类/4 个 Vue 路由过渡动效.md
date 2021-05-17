
---
title: '4 个 Vue 路由过渡动效'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb49ed61051b40faa44fe30f59f17dcd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 02:39:26 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb49ed61051b40faa44fe30f59f17dcd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Vue 路由过渡是对 Vue 程序一种快速简便的增加个性化效果的的方法。 可以让你在程序的不同页面之间增加平滑的动画和过渡。如果使用得当，可以使你的程序显得更加专业，从而增强用户体验。</p>
<p>本文中会先介绍使用 Vue 路由过渡的基础知识，然后在举几个例子，为你一些灵感。下面是其中的一个案例：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb49ed61051b40faa44fe30f59f17dcd~tplv-k3u1fbpfcp-watermark.image" alt="image1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">在 Vue 程序中添加路由</h2>
<p>一般 Vue 路由设置如下所示：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">router-view</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在旧版本的 Vue 路由中，我们可以简单地用 <code><transition></code> 组件包装 <code><router-view></code>。</p>
<p>但是，在较新版本的 Vue 路由中则必须用 <code>v-slot</code> 来解构 props 并将它们传递到我们的内部 slot 中。 这将包含一个动态组件，该组件被过渡组件包围。</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; Component &#125;"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">transition</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"Component"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">为路由添加过渡</h2>
<p>默认情况下，用 <code><transition></code> 包裹 <code><component></code> 会在你应用的每个路由上添加相同的过渡。</p>
<p>可以通过两种方式为每个路由自定义转场效果。</p>
<h3 data-id="heading-2">将过渡移到每个组件中</h3>
<p>首先，不用把我们的动态组件与过渡组件包装在一起，可以将 <code><transition></code> 移动到每个单独的组件中。 像这样：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">transition</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrapper"</span>></span>
      <span class="hljs-comment"><!-- --></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>依此类推，对要进行过渡的每条路由进行处理。 这样就可以通过修改过渡名称来自定义每条路由。</p>
<h3 data-id="heading-3">用 v-bind 进行动态过渡</h3>
<p>另一个方法是将过渡的名称绑定到变量。 然后就可以根据自己的路有动态地修改这个变量。</p>
<p>这是 Vue 路由文档中的例子。在当前路由上用观察模式来动态设置 <code>transitionName</code> 变量。</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">:name</span>=<span class="hljs-string">"transitionName"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"Component"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">transition</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css">watch: &#123;
  <span class="hljs-string">'$route'</span> (to, from) &#123;
    const toDepth = to.path.<span class="hljs-built_in">split</span>(<span class="hljs-string">'/'</span>).length
    const fromDepth = from.path.<span class="hljs-built_in">split</span>(<span class="hljs-string">'/'</span>).length
    this.transitionName = toDepth < fromDepth ? <span class="hljs-string">'slide-right'</span> : <span class="hljs-string">'slide-left'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们了解了 Vue 路由过渡的基础知识，下面让来看一些例子。</p>
<h2 data-id="heading-4">#1 – 渐变过渡</h2>
<p>渐变页面过渡应该是最直接的一种动效。可以通过修改元素的透明度来实现。</p>
<p>首先，创建一个名为 fade 过渡。需要注意的是过渡模式设置为 <code>out-in</code>。</p>
<p>总共有 3 种过渡模式：</p>
<ol>
<li>default：淡入和淡出过渡同时发生</li>
<li>in-out：新元素首先淡入。 然后当前元素淡出。</li>
<li>out-in：当前元素先淡出。 然后新元素开始淡入。</li>
</ol>
<p>为了使新元素顺利淡入，我们需要在开始新过渡之前将当前元素删除。所以必须用 <code>mode = "out-in"</code>。</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; Component &#125;"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"fade"</span> <span class="hljs-attr">mode</span>=<span class="hljs-string">"out-in"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"Component"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code><transition></code> 为提供了几个 CSS 类，它们能够在动画周期中被动态添加或删除。</p>
<p>有 6。个不同的过渡类（3 个用于淡入，3 个用于淡出）。</p>
<ul>
<li><code>v-enter-from</code> / <code>v-leave-from</code>: 过渡的初始状态，过度开始后将其删除</li>
<li><code>v-enter-active</code> / <code>v-leave-active</code>: 过渡的激活状态</li>
<li><code>v-enter-to</code> / <code>v-leave-to</code>: 过渡的结束状态</li>
</ul>
<p>我们的淡入淡出过渡有一个名为 <code>fade-enter-from</code> 的类。</p>
<p>我们希望淡入和淡出状态的透明度为 0。然后当过渡处于活动状态时，希望对透明度进行动画处理。</p>
<p>我们甚至不必将透明度设置为1，因为在动画制作过程中会删除  <code>fade-enter-from</code> 和 <code>fade-leave-to</code> 类。 这会使元素自己单独设置为默认透明度为 1 的动画。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.fade-enter-active</span>,
<span class="hljs-selector-class">.fade-leave-active</span> &#123;
  <span class="hljs-attribute">transition</span>: opacity <span class="hljs-number">0.5s</span> ease;
&#125;

<span class="hljs-selector-class">.fade-enter-from</span>,
<span class="hljs-selector-class">.fade-leave-to</span> &#123;
  <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配合一些虚拟组件，这就是最终过渡效果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b7a2676694b478493d1f86ba24b86f5~tplv-k3u1fbpfcp-watermark.image" alt="image4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">#2 – 幻灯片过渡</h2>
<p>下一个是页面幻灯片过渡。</p>
<p>模板将如下。 由于希望淡入和淡出过渡同时发生，所以我们不想为过渡设置特殊的模式。</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; Component &#125;"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"slide"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"Component"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了使例子更容易理解，我把每个组件的宽度都设为100％，并占用至少 1 vh，还分别设置了背景色。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.wrapper</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100vh</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后过渡样式将为要滑动组件的绝对位置设置动画。如果需要不同的滑动方向，只需更改要设置的CSS属性（ <code>top</code>, <code>bottom</code>, <code>left</code>, <code>right</code>）。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.slide-enter-active</span>,
<span class="hljs-selector-class">.slide-leave-active</span> &#123;
  <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.75s</span> ease-out;
&#125;


<span class="hljs-selector-class">.slide-enter-to</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
&#125;


<span class="hljs-selector-class">.slide-enter-from</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">right</span>: -<span class="hljs-number">100%</span>;
&#125;


<span class="hljs-selector-class">.slide-leave-to</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">left</span>: -<span class="hljs-number">100%</span>;
&#125;


<span class="hljs-selector-class">.slide-leave-from</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是最终效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ef9c5c4dc644c0a8b8c09c4265d6b88~tplv-k3u1fbpfcp-watermark.image" alt="image1-20210517182239065.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">#3 – 缩放过渡</h2>
<p>缩放过渡与渐变过渡非常相似。同样需要把模式设置为 <code>out-in</code>，这样可以确保动画的正确顺序。</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; Component &#125;"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"scale"</span> <span class="hljs-attr">mode</span>=<span class="hljs-string">"out-in"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"Component"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后用样式改变元素的透明度和 <code>transform: scale</code>。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.scale-enter-active</span>,
<span class="hljs-selector-class">.scale-leave-active</span> &#123;
  <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.5s</span> ease;
&#125;


<span class="hljs-selector-class">.scale-enter-from</span>,
<span class="hljs-selector-class">.scale-leave-to</span> &#123;
  <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0.9</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了使这个过渡看上去更干净，可以把整个网页的背景色设置为黑色。</p>
<p>这是最终效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/815a9d2c432b4781b6008a398f4254d4~tplv-k3u1fbpfcp-watermark.image" alt="Jan-20-2021-13-58-14.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">#4 – 组合过渡</h2>
<p>过渡的效果有很多很多，常用的做法是把一些基础的过渡结合在一起，例如把幻灯片和缩放合并为一个过渡。</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; Component &#125;"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"scale-slide"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"Component"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.scale-slide-enter-active</span>,
<span class="hljs-selector-class">.scale-slide-leave-active</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.85s</span> ease;
&#125;

<span class="hljs-selector-class">.scale-slide-enter-from</span> &#123;
  <span class="hljs-attribute">left</span>: -<span class="hljs-number">100%</span>;
&#125;

<span class="hljs-selector-class">.scale-slide-enter-to</span> &#123;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0%</span>;
&#125;

<span class="hljs-selector-class">.scale-slide-leave-from</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1</span>);
&#125;

<span class="hljs-selector-class">.scale-slide-leave-to</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0.8</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是最终效果</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1345b2093f443eb947a8840a75a9f55~tplv-k3u1fbpfcp-watermark.image" alt="Jan-20-2021-13-57-43.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看上去还不错吧。</p>
<h2 data-id="heading-8">#5 – 写在最后</h2>
<p>近期在提升 Vue 的过程中，发现一个高逼格的 Vue3+TS 教程。
无偿分享给掘仔们，<a href="https://www.bilibili.com/video/BV1gf4y1W783" target="_blank" rel="nofollow noopener noreferrer">戳我看教程</a></p></div>  
</div>
            