
---
title: 'Svelte教程翻译（八、补间动画）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5308'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 04:03:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=5308'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">运动</h2>
<p>设置值和观察DOM自动更新是很酷的。知道什么更酷吗？这些值之间的差异。Svelte包括一些工具，可以帮助您构建流畅的用户界面，使用动画来传达更改。</p>
<p>我们先将<code>progress</code>存储更改为tweened值：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
<span class="hljs-keyword">import</span> &#123; tweened &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/motion'</span>;

<span class="hljs-keyword">const</span> progress = tweened(<span class="hljs-number">0</span>);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>单击按钮将使进度条变化到新值。不过，这有点机械化，令人不满意。我们需要增加一个缓慢结束的功能：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; tweened &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/motion'</span>;
<span class="hljs-keyword">import</span> &#123; cubicOut &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/easing'</span>;

<span class="hljs-keyword">const</span> progress = tweened(<span class="hljs-number">0</span>, &#123;
<span class="hljs-attr">duration</span>: <span class="hljs-number">400</span>,
<span class="hljs-attr">easing</span>: cubicOut
&#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>svelte/easing模块包含Penner-easing函数，或者您可以提供自己的<code>p=>t</code>函数，其中p和t都是介于0和1之间的值。</p>
</blockquote>
<p>Tween提供的选项：</p>
<ul>
<li>delay：在tween开始之前的毫秒数</li>
<li>duration：以毫秒为单位的tween的持续时间，或者<code>(from, to) => milliseconds</code>，允许您自定义变化。</li>
<li>easing：一个 <code>p => t</code> 函数</li>
<li>interpolate：<code>(from, to) => t => value</code>用于在任意值之间插值的自定义函数。默认情况下，Svelte将在数字、日期以及形式相同的数组和对象之间进行插值（只要它们仅包含数字和日期或其他有效数组和对象）。如果要插值（例如）颜色字符串或变换矩阵，请提供自定义插值器</li>
</ul>
<p>您还可以将这些选项作为第二个参数传递给<code>progress.set</code>和<code>progress.update</code>，在这种情况下，它们将覆盖默认值。set和update方法都返回一个在tween完成时解析的promise。</p>
<p>完整的代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; tweened &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/motion'</span>;
<span class="hljs-keyword">import</span> &#123; cubicOut &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/easing'</span>;

<span class="hljs-keyword">const</span> progress = tweened(<span class="hljs-number">0</span>, &#123;
<span class="hljs-attr">duration</span>: <span class="hljs-number">400</span>,
<span class="hljs-attr">easing</span>: cubicOut
&#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">progress</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;$progress&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">progress</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">"&#123;() => progress.set(0)&#125;"</span>></span>
0%
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">"&#123;() => progress.set(0.25)&#125;"</span>></span>
25%
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">"&#123;() => progress.set(0.5)&#125;"</span>></span>
50%
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">"&#123;() => progress.set(0.75)&#125;"</span>></span>
75%
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">"&#123;() => progress.set(1)&#125;"</span>></span>
100%
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
progress &#123;
<span class="hljs-attribute">display</span>: block;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">回弹</h2>
<p>回弹函数是tweend函数的一种替代方法，它通常对频繁变化的值更有效。</p>
<p>在本例中，我们有两个存储—一个表示圆的坐标，另一个表示圆的大小。让我们将它们转换为spring：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; spring &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/motion'</span>;

<span class="hljs-keyword">let</span> coords = spring(&#123; <span class="hljs-attr">x</span>: <span class="hljs-number">50</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">50</span> &#125;);
<span class="hljs-keyword">let</span> size = spring(<span class="hljs-number">10</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两个springs都有默认的stiffness和damping，它们控制着回弹的弹性。我们可以指定自己的初始值：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> coords = spring(&#123; <span class="hljs-attr">x</span>: <span class="hljs-number">50</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">50</span> &#125;, &#123;
<span class="hljs-attr">stiffness</span>: <span class="hljs-number">0.1</span>,
<span class="hljs-attr">damping</span>: <span class="hljs-number">0.25</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>晃动鼠标，并尝试拖动滑块，以了解它们如何影响回弹的行为。请注意，可以在回弹仍处于运动状态时调整这些值。</p>
<p>完整代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; spring &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/motion'</span>;

<span class="hljs-keyword">let</span> coords = spring(&#123; <span class="hljs-attr">x</span>: <span class="hljs-number">50</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">50</span> &#125;, &#123;
<span class="hljs-attr">stiffness</span>: <span class="hljs-number">0.1</span>,
<span class="hljs-attr">damping</span>: <span class="hljs-number">0.25</span>
&#125;);

<span class="hljs-keyword">let</span> size = spring(<span class="hljs-number">10</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"position: absolute; right: 1em;"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">label</span>></span>
<span class="hljs-tag"><<span class="hljs-name">h3</span>></span>stiffness (&#123;coords.stiffness&#125;)<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">bind:value</span>=<span class="hljs-string">&#123;coords.stiffness&#125;</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"range"</span> <span class="hljs-attr">min</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">max</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">step</span>=<span class="hljs-string">"0.01"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">label</span>></span>

<span class="hljs-tag"><<span class="hljs-name">label</span>></span>
<span class="hljs-tag"><<span class="hljs-name">h3</span>></span>damping (&#123;coords.damping&#125;)<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">bind:value</span>=<span class="hljs-string">&#123;coords.damping&#125;</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"range"</span> <span class="hljs-attr">min</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">max</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">step</span>=<span class="hljs-string">"0.01"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">svg</span>
<span class="hljs-attr">on:mousemove</span>=<span class="hljs-string">"&#123;e => coords.set(&#123; x: e.clientX, y: e.clientY &#125;)&#125;"</span>
<span class="hljs-attr">on:mousedown</span>=<span class="hljs-string">"&#123;() => size.set(30)&#125;"</span>
<span class="hljs-attr">on:mouseup</span>=<span class="hljs-string">"&#123;() => size.set(10)&#125;"</span>
></span>
<span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">&#123;$coords.x&#125;</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">&#123;$coords.y&#125;</span> <span class="hljs-attr">r</span>=<span class="hljs-string">&#123;$size&#125;/</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
svg &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;
circle &#123;
fill: <span class="hljs-number">#ff3e00</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这节是动画效果，强烈推荐去官网体验一下。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsvelte.dev%2Ftutorial%2Ftweened" target="_blank" rel="nofollow noopener noreferrer" title="https://svelte.dev/tutorial/tweened" ref="nofollow noopener noreferrer">补间动画</a></p></div>  
</div>
            