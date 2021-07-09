
---
title: 'Svelte教程翻译（九、过渡）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6283'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 04:04:55 GMT
thumbnail: 'https://picsum.photos/400/300?random=6283'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">过渡</h2>
<p>我们可以通过优雅地将元素显示到DOM中或从DOM中移除，来创建更具吸引力的用户界面。使用transition指令，在Svelte中这变得非常容易。</p>
<p>首先，从svelte/transition导入淡入淡出功能：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; fade &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/transition'</span>;
<span class="hljs-keyword">let</span> visible = <span class="hljs-literal">true</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后将其添加到<code><p></code>元素：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">transition:fade</span>></span>Fades in and out<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; fade &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/transition'</span>;
<span class="hljs-keyword">let</span> visible = <span class="hljs-literal">true</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">label</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">bind:checked</span>=<span class="hljs-string">&#123;visible&#125;</span>></span>
visible
<span class="hljs-tag"></<span class="hljs-name">label</span>></span>

&#123;#if visible&#125;
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">transition:fade</span>></span>
Fades in and out
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
&#123;/if&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">添加参数</h2>
<p>过渡函数可以接受参数。用<code>fly</code>替换<code>fade</code>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; fly &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/transition'</span>;
<span class="hljs-keyword">let</span> visible = <span class="hljs-literal">true</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并将其应用于<code><p></code>以及一些选项：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">transition:fly</span>=<span class="hljs-string">"&#123;&#123; y: 200, duration: 2000 &#125;&#125;"</span>></span>
Flies in and out
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请注意，过渡是可逆的。如果您在过渡进行时切换复选框，它将从当前点过渡，而不是从开始或结束点。</p>
<p>完整代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; fly &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/transition'</span>;
<span class="hljs-keyword">let</span> visible = <span class="hljs-literal">true</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">label</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">bind:checked</span>=<span class="hljs-string">&#123;visible&#125;</span>></span>
visible
<span class="hljs-tag"></<span class="hljs-name">label</span>></span>

&#123;#if visible&#125;
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">transition:fly</span>=<span class="hljs-string">"&#123;&#123; y: 200, duration: 2000 &#125;&#125;"</span>></span>
Flies in and out
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
&#123;/if&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">淡入淡出</h2>
<p>一个元素可以有一个in或out指令，或者两者都有，而不是transition指令。导入<code>fade</code>和<code>fly</code>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; fade, fly &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/transition'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后将过渡指令替换为单独的输入和输出指令：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">in:fly</span>=<span class="hljs-string">"&#123;&#123; y: 200, duration: 2000 &#125;&#125;"</span> <span class="hljs-attr">out:fade</span>></span>
Flies in, fades out
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这种情况下，过渡不会反转。</p>
<h2 data-id="heading-3">自定义CSS过渡</h2>
<p>svelte/transition模块有一些内置的过渡，但很容易创建自己的过渡。举例来说，这是fade过渡的源代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fade</span>(<span class="hljs-params">node, &#123;
delay = <span class="hljs-number">0</span>,
duration = <span class="hljs-number">400</span>
&#125;</span>) </span>&#123;
<span class="hljs-keyword">const</span> o = +getComputedStyle(node).opacity;

<span class="hljs-keyword">return</span> &#123;
delay,
duration,
<span class="hljs-attr">css</span>: <span class="hljs-function"><span class="hljs-params">t</span> =></span> <span class="hljs-string">`opacity: <span class="hljs-subst">$&#123;t * o&#125;</span>`</span>
&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该函数接受两个参数：应用过渡的节点和传入的参数对象，并返回具有以下属性的对象：</p>
<ul>
<li>
<p>delay：过渡开始前的毫秒数</p>
</li>
<li>
<p>duration：过渡的时长（毫秒）</p>
</li>
<li>
<p>easing：一个<code>p=>t</code>函数</p>
</li>
<li>
<p>css：一个<code>(t,u)=>css</code>函数，其中<code>u===1-t</code></p>
</li>
<li>
<p>tick：一个 <code>(t, u) => &#123;...&#125;</code>函数，对节点有一定影响</p>
</li>
</ul>
<p>t=0时，从头开始播放动画，t=1时，反转动画。</p>
<p>大多数情况下，您应该返回css属性而不是tick属性，因为css动画会从主线程运行。Svelte“模拟”过渡并构造一个CSS动画，然后让它运行。</p>
<p>例如，“淡入淡出”（fade）过渡生成类似以下内容的CSS动画：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-number">0%</span> &#123; <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span> &#125;
<span class="hljs-number">10%</span> &#123; <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.1</span> &#125;
<span class="hljs-number">20%</span> &#123; <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.2</span> &#125;
<span class="hljs-comment">/* ... */</span>
<span class="hljs-number">100%</span> &#123; <span class="hljs-attribute">opacity</span>: <span class="hljs-number">1</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过，我们可以变得更有创意：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; fade &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/transition'</span>;
<span class="hljs-keyword">import</span> &#123; elasticOut &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/easing'</span>;

<span class="hljs-keyword">let</span> visible = <span class="hljs-literal">true</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">spin</span>(<span class="hljs-params">node, &#123; duration &#125;</span>) </span>&#123;
<span class="hljs-keyword">return</span> &#123;
duration,
<span class="hljs-attr">css</span>: <span class="hljs-function"><span class="hljs-params">t</span> =></span> &#123;
<span class="hljs-keyword">const</span> eased = elasticOut(t);

<span class="hljs-keyword">return</span> <span class="hljs-string">`
transform: scale(<span class="hljs-subst">$&#123;eased&#125;</span>) rotate(<span class="hljs-subst">$&#123;eased * <span class="hljs-number">1080</span>&#125;</span>deg);
color: hsl(
<span class="hljs-subst">$&#123;~~(t * <span class="hljs-number">360</span>)&#125;</span>,
<span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.min(<span class="hljs-number">100</span>, <span class="hljs-number">1000</span> - <span class="hljs-number">1000</span> * t)&#125;</span>%,
<span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.min(<span class="hljs-number">50</span>, <span class="hljs-number">500</span> - <span class="hljs-number">500</span> * t)&#125;</span>%
);`</span>
&#125;
&#125;;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>记住：强大的力量带来巨大的责任。</p>
<p>完整代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; fade &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/transition'</span>;
<span class="hljs-keyword">import</span> &#123; elasticOut &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/easing'</span>;

<span class="hljs-keyword">let</span> visible = <span class="hljs-literal">true</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">spin</span>(<span class="hljs-params">node, &#123; duration &#125;</span>) </span>&#123;
<span class="hljs-keyword">return</span> &#123;
duration,
<span class="hljs-attr">css</span>: <span class="hljs-function"><span class="hljs-params">t</span> =></span> &#123;
<span class="hljs-keyword">const</span> eased = elasticOut(t);

<span class="hljs-keyword">return</span> <span class="hljs-string">`
transform: scale(<span class="hljs-subst">$&#123;eased&#125;</span>) rotate(<span class="hljs-subst">$&#123;eased * <span class="hljs-number">1080</span>&#125;</span>deg);
color: hsl(
<span class="hljs-subst">$&#123;~~(t * <span class="hljs-number">360</span>)&#125;</span>,
<span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.min(<span class="hljs-number">100</span>, <span class="hljs-number">1000</span> - <span class="hljs-number">1000</span> * t)&#125;</span>%,
<span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.min(<span class="hljs-number">50</span>, <span class="hljs-number">500</span> - <span class="hljs-number">500</span> * t)&#125;</span>%
);`</span>
&#125;
&#125;;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">label</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">bind:checked</span>=<span class="hljs-string">&#123;visible&#125;</span>></span>
visible
<span class="hljs-tag"></<span class="hljs-name">label</span>></span>

&#123;#if visible&#125;
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"centered"</span> <span class="hljs-attr">in:spin</span>=<span class="hljs-string">"&#123;&#123;duration: 8000&#125;&#125;"</span> <span class="hljs-attr">out:fade</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span>></span>transitions!<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
&#123;/if&#125;

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-class">.centered</span> &#123;
<span class="hljs-attribute">position</span>: absolute;
<span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
<span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
<span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>,-<span class="hljs-number">50%</span>);
&#125;

<span class="hljs-selector-tag">span</span> &#123;
<span class="hljs-attribute">position</span>: absolute;
<span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>,-<span class="hljs-number">50%</span>);
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">4em</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">自定义JS过渡</h2>
<p>虽然您通常应该尽可能多地使用CSS进行过渡，但有一些效果是没有JavaScript无法实现的，例如打字机效果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">typewriter</span>(<span class="hljs-params">node, &#123; speed = <span class="hljs-number">50</span> &#125;</span>) </span>&#123;
<span class="hljs-keyword">const</span> valid = (
node.childNodes.length === <span class="hljs-number">1</span> &&
node.childNodes[<span class="hljs-number">0</span>].nodeType === Node.TEXT_NODE
);

<span class="hljs-keyword">if</span> (!valid) &#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`This transition only works on elements with a single text node child`</span>);
&#125;

<span class="hljs-keyword">const</span> text = node.textContent;
<span class="hljs-keyword">const</span> duration = text.length * speed;

<span class="hljs-keyword">return</span> &#123;
duration,
<span class="hljs-attr">tick</span>: <span class="hljs-function"><span class="hljs-params">t</span> =></span> &#123;
<span class="hljs-keyword">const</span> i = ~~(text.length * t);
node.textContent = text.slice(<span class="hljs-number">0</span>, i);
&#125;
&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">let</span> visible = <span class="hljs-literal">false</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">typewriter</span>(<span class="hljs-params">node, &#123; speed = <span class="hljs-number">50</span> &#125;</span>) </span>&#123;
<span class="hljs-keyword">const</span> valid = (
node.childNodes.length === <span class="hljs-number">1</span> &&
node.childNodes[<span class="hljs-number">0</span>].nodeType === Node.TEXT_NODE
);

<span class="hljs-keyword">if</span> (!valid) &#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`This transition only works on elements with a single text node child`</span>);
&#125;

<span class="hljs-keyword">const</span> text = node.textContent;
<span class="hljs-keyword">const</span> duration = text.length * speed;

<span class="hljs-keyword">return</span> &#123;
duration,
<span class="hljs-attr">tick</span>: <span class="hljs-function"><span class="hljs-params">t</span> =></span> &#123;
<span class="hljs-keyword">const</span> i = ~~(text.length * t);
node.textContent = text.slice(<span class="hljs-number">0</span>, i);
&#125;
&#125;;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">label</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">bind:checked</span>=<span class="hljs-string">&#123;visible&#125;</span>></span>
visible
<span class="hljs-tag"></<span class="hljs-name">label</span>></span>

&#123;#if visible&#125;
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">in:typewriter</span>></span>
The quick brown fox jumps over the lazy dog
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
&#123;/if&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">过渡事件</h2>
<p>知道过渡的开始和结束时间可能很有用。与任何其他DOM事件一样，Svelte可以监听过渡事件：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span>
<span class="hljs-attr">transition:fly</span>=<span class="hljs-string">"&#123;&#123; y: 200, duration: 2000 &#125;&#125;"</span>
<span class="hljs-attr">on:introstart</span>=<span class="hljs-string">"&#123;() => status = 'intro started'&#125;"</span>
<span class="hljs-attr">on:outrostart</span>=<span class="hljs-string">"&#123;() => status = 'outro started'&#125;"</span>
<span class="hljs-attr">on:introend</span>=<span class="hljs-string">"&#123;() => status = 'intro ended'&#125;"</span>
<span class="hljs-attr">on:outroend</span>=<span class="hljs-string">"&#123;() => status = 'outro ended'&#125;"</span>
></span>
Flies in and out
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; fly &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/transition'</span>;

<span class="hljs-keyword">let</span> visible = <span class="hljs-literal">true</span>;
<span class="hljs-keyword">let</span> status = <span class="hljs-string">'waiting...'</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>status: &#123;status&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"><<span class="hljs-name">label</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">bind:checked</span>=<span class="hljs-string">&#123;visible&#125;</span>></span>
visible
<span class="hljs-tag"></<span class="hljs-name">label</span>></span>

&#123;#if visible&#125;
<span class="hljs-tag"><<span class="hljs-name">p</span>
<span class="hljs-attr">transition:fly</span>=<span class="hljs-string">"&#123;&#123; y: 200, duration: 2000 &#125;&#125;"</span>
<span class="hljs-attr">on:introstart</span>=<span class="hljs-string">"&#123;() => status = 'intro started'&#125;"</span>
<span class="hljs-attr">on:outrostart</span>=<span class="hljs-string">"&#123;() => status = 'outro started'&#125;"</span>
<span class="hljs-attr">on:introend</span>=<span class="hljs-string">"&#123;() => status = 'intro ended'&#125;"</span>
<span class="hljs-attr">on:outroend</span>=<span class="hljs-string">"&#123;() => status = 'outro ended'&#125;"</span>
></span>
Flies in and out
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
&#123;/if&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">局部过渡</h2>
<p>通常，当添加或销毁任何容器块时，过渡将在元素上起作用。在这里的示例中，切换整个列表的可见性也会将过渡应用于各个列表元素。</p>
<p>相反，我们希望仅在添加和删除单个项目时播放过渡。</p>
<p>我们可以通过局部转换来实现这一点，该转换仅在添加或删除当前节点时播放：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">transition:slide</span>|<span class="hljs-attr">local</span>></span>
&#123;item&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; slide &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/transition'</span>;

<span class="hljs-keyword">let</span> showItems = <span class="hljs-literal">true</span>;
<span class="hljs-keyword">let</span> i = <span class="hljs-number">5</span>;
<span class="hljs-keyword">let</span> items = [<span class="hljs-string">'one'</span>, <span class="hljs-string">'two'</span>, <span class="hljs-string">'three'</span>, <span class="hljs-string">'four'</span>, <span class="hljs-string">'five'</span>, <span class="hljs-string">'six'</span>, <span class="hljs-string">'seven'</span>, <span class="hljs-string">'eight'</span>, <span class="hljs-string">'nine'</span>, <span class="hljs-string">'ten'</span>];
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">label</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">bind:checked</span>=<span class="hljs-string">&#123;showItems&#125;</span>></span>
show list
<span class="hljs-tag"></<span class="hljs-name">label</span>></span>

<span class="hljs-tag"><<span class="hljs-name">label</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"range"</span> <span class="hljs-attr">bind:value</span>=<span class="hljs-string">&#123;i&#125;</span> <span class="hljs-attr">max</span>=<span class="hljs-string">10</span>></span>

<span class="hljs-tag"></<span class="hljs-name">label</span>></span>

&#123;#if showItems&#125;
&#123;#each items.slice(0, i) as item&#125;
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">transition:slide</span>|<span class="hljs-attr">local</span>></span>
&#123;item&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
&#123;/each&#125;
&#123;/if&#125;

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-tag">div</span> &#123;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0.5em</span> <span class="hljs-number">0</span>;
<span class="hljs-attribute">border-top</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#eee</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">延迟过渡</h2>
<p>Svelte的过渡引擎的一个特别强大的功能是延迟过渡的能力，这样它们就可以在多个元素之间进行协调。</p>
<p>以这对todo列表为例，在其中切换todo会将其发送到相反的列表。在现实世界中，物体的行为不是这样的，它们通过一系列中间位置移动，而不是在另一个地方消失和重新出现。使用motion可以帮助用户理解应用程序中发生的事情。</p>
<p>我们可以使用crossfade函数来实现这个效果，它创建了一对名为send和receive的过渡。当一个元素被“发送”时，它会寻找一个对应的元素“接收”，并生成一个过渡，将该元素过渡到对应的位置并淡出。当一个元素被“接收”时，情况正好相反。如果没有对应项，则使用回退过渡。</p>
<p>完整代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; quintOut &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/easing'</span>;
<span class="hljs-keyword">import</span> &#123; crossfade &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'svelte/transition'</span>;

<span class="hljs-keyword">const</span> [send, receive] = crossfade(&#123;
<span class="hljs-attr">duration</span>: <span class="hljs-function"><span class="hljs-params">d</span> =></span> <span class="hljs-built_in">Math</span>.sqrt(d * <span class="hljs-number">200</span>),

<span class="hljs-function"><span class="hljs-title">fallback</span>(<span class="hljs-params">node, params</span>)</span> &#123;
<span class="hljs-keyword">const</span> style = getComputedStyle(node);
<span class="hljs-keyword">const</span> transform = style.transform === <span class="hljs-string">'none'</span> ? <span class="hljs-string">''</span> : style.transform;

<span class="hljs-keyword">return</span> &#123;
<span class="hljs-attr">duration</span>: <span class="hljs-number">600</span>,
<span class="hljs-attr">easing</span>: quintOut,
<span class="hljs-attr">css</span>: <span class="hljs-function"><span class="hljs-params">t</span> =></span> <span class="hljs-string">`
transform: <span class="hljs-subst">$&#123;transform&#125;</span> scale(<span class="hljs-subst">$&#123;t&#125;</span>);
opacity: <span class="hljs-subst">$&#123;t&#125;</span>
`</span>
&#125;;
&#125;
&#125;);

<span class="hljs-keyword">let</span> uid = <span class="hljs-number">1</span>;

<span class="hljs-keyword">let</span> todos = [
&#123; <span class="hljs-attr">id</span>: uid++, done: <span class="hljs-literal">false</span>, <span class="hljs-attr">description</span>: <span class="hljs-string">'write some docs'</span> &#125;,
&#123; <span class="hljs-attr">id</span>: uid++, done: <span class="hljs-literal">false</span>, <span class="hljs-attr">description</span>: <span class="hljs-string">'start writing blog post'</span> &#125;,
&#123; <span class="hljs-attr">id</span>: uid++, done: <span class="hljs-literal">true</span>,  <span class="hljs-attr">description</span>: <span class="hljs-string">'buy some milk'</span> &#125;,
&#123; <span class="hljs-attr">id</span>: uid++, done: <span class="hljs-literal">false</span>, <span class="hljs-attr">description</span>: <span class="hljs-string">'mow the lawn'</span> &#125;,
&#123; <span class="hljs-attr">id</span>: uid++, done: <span class="hljs-literal">false</span>, <span class="hljs-attr">description</span>: <span class="hljs-string">'feed the turtle'</span> &#125;,
&#123; <span class="hljs-attr">id</span>: uid++, done: <span class="hljs-literal">false</span>, <span class="hljs-attr">description</span>: <span class="hljs-string">'fix some bugs'</span> &#125;,
];

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">input</span>) </span>&#123;
<span class="hljs-keyword">const</span> todo = &#123;
<span class="hljs-attr">id</span>: uid++,
done: <span class="hljs-literal">false</span>,
<span class="hljs-attr">description</span>: input.value
&#125;;

todos = [todo, ...todos];
input.value = <span class="hljs-string">''</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">remove</span>(<span class="hljs-params">todo</span>) </span>&#123;
todos = todos.filter(<span class="hljs-function"><span class="hljs-params">t</span> =></span> t !== todo);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mark</span>(<span class="hljs-params">todo, done</span>) </span>&#123;
todo.done = done;
remove(todo);
todos = todos.concat(todo);
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'board'</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span>
<span class="hljs-attr">placeholder</span>=<span class="hljs-string">"what needs to be done?"</span>
<span class="hljs-attr">on:keydown</span>=<span class="hljs-string">&#123;e</span> =></span> e.key === 'Enter' && add(e.target)&#125;
>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'left'</span>></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>todo<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
&#123;#each todos.filter(t => !t.done) as todo (todo.id)&#125;
<span class="hljs-tag"><<span class="hljs-name">label</span>
<span class="hljs-attr">in:receive</span>=<span class="hljs-string">"&#123;&#123;key: todo.id&#125;&#125;"</span>
<span class="hljs-attr">out:send</span>=<span class="hljs-string">"&#123;&#123;key: todo.id&#125;&#125;"</span>
></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">checkbox</span> <span class="hljs-attr">on:change</span>=<span class="hljs-string">&#123;()</span> =></span> mark(todo, true)&#125;>
&#123;todo.description&#125;
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">"&#123;() => remove(todo)&#125;"</span>></span>remove<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
&#123;/each&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'right'</span>></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>done<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
&#123;#each todos.filter(t => t.done) as todo (todo.id)&#125;
<span class="hljs-tag"><<span class="hljs-name">label</span>
<span class="hljs-attr">class</span>=<span class="hljs-string">"done"</span>
<span class="hljs-attr">in:receive</span>=<span class="hljs-string">"&#123;&#123;key: todo.id&#125;&#125;"</span>
<span class="hljs-attr">out:send</span>=<span class="hljs-string">"&#123;&#123;key: todo.id&#125;&#125;"</span>
></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">checkbox</span> <span class="hljs-attr">checked</span> <span class="hljs-attr">on:change</span>=<span class="hljs-string">&#123;()</span> =></span> mark(todo, false)&#125;>
&#123;todo.description&#125;
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">"&#123;() => remove(todo)&#125;"</span>></span>remove<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
&#123;/each&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-class">.board</span> &#123;
<span class="hljs-attribute">display</span>: grid;
grid-template-<span class="hljs-attribute">columns</span>: <span class="hljs-number">1</span>fr <span class="hljs-number">1</span>fr;
grid-gap: <span class="hljs-number">1em</span>;
<span class="hljs-attribute">max-width</span>: <span class="hljs-number">36em</span>;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
&#125;

<span class="hljs-selector-class">.board</span> > <span class="hljs-selector-tag">input</span> &#123;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">1.4em</span>;
grid-column: <span class="hljs-number">1</span>/<span class="hljs-number">3</span>;
&#125;

<span class="hljs-selector-tag">h2</span> &#123;
<span class="hljs-attribute">font-size</span>: <span class="hljs-number">2em</span>;
<span class="hljs-attribute">font-weight</span>: <span class="hljs-number">200</span>;
user-select: none;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0.5em</span> <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-tag">label</span> &#123;
<span class="hljs-attribute">position</span>: relative;
<span class="hljs-attribute">line-height</span>: <span class="hljs-number">1.2</span>;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0.5em</span> <span class="hljs-number">2.5em</span> <span class="hljs-number">0.5em</span> <span class="hljs-number">2em</span>;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0.5em</span> <span class="hljs-number">0</span>;
<span class="hljs-attribute">border-radius</span>: <span class="hljs-number">2px</span>;
user-select: none;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-built_in">hsl</span>(<span class="hljs-number">240</span>, <span class="hljs-number">8%</span>, <span class="hljs-number">70%</span>);
<span class="hljs-attribute">background-color</span>:<span class="hljs-built_in">hsl</span>(<span class="hljs-number">240</span>, <span class="hljs-number">8%</span>, <span class="hljs-number">93%</span>);
<span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;
&#125;

<span class="hljs-selector-tag">input</span><span class="hljs-selector-attr">[type=<span class="hljs-string">"checkbox"</span>]</span> &#123;
<span class="hljs-attribute">position</span>: absolute;
<span class="hljs-attribute">left</span>: <span class="hljs-number">0.5em</span>;
<span class="hljs-attribute">top</span>: <span class="hljs-number">0.6em</span>;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.done</span> &#123;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-built_in">hsl</span>(<span class="hljs-number">240</span>, <span class="hljs-number">8%</span>, <span class="hljs-number">90%</span>);
<span class="hljs-attribute">background-color</span>:<span class="hljs-built_in">hsl</span>(<span class="hljs-number">240</span>, <span class="hljs-number">8%</span>, <span class="hljs-number">98%</span>);
&#125;

<span class="hljs-selector-tag">button</span> &#123;
<span class="hljs-attribute">position</span>: absolute;
<span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
<span class="hljs-attribute">right</span>: <span class="hljs-number">0.2em</span>;
<span class="hljs-attribute">width</span>: <span class="hljs-number">2em</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
<span class="hljs-attribute">background</span>: no-repeat <span class="hljs-number">50%</span> <span class="hljs-number">50%</span> <span class="hljs-built_in">url</span>(<span class="hljs-string">"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23676778' d='M12,2C17.53,2 22,6.47 22,12C22,17.53 17.53,22 12,22C6.47,22 2,17.53 2,12C2,6.47 6.47,2 12,2M17,7H14.5L13.5,6H10.5L9.5,7H7V9H17V7M9,18H15A1,1 0 0,0 16,17V10H8V17A1,1 0 0,0 9,18Z'%3E%3C/path%3E%3C/svg%3E"</span>);
<span class="hljs-attribute">background-size</span>: <span class="hljs-number">1.4em</span> <span class="hljs-number">1.4em</span>;
<span class="hljs-attribute">border</span>: none;
<span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>;
<span class="hljs-attribute">transition</span>: opacity <span class="hljs-number">0.2s</span>;
<span class="hljs-attribute">text-indent</span>: -<span class="hljs-number">9999px</span>;
<span class="hljs-attribute">cursor</span>: pointer;
&#125;

<span class="hljs-selector-tag">label</span><span class="hljs-selector-pseudo">:hover</span> <span class="hljs-selector-tag">button</span> &#123;
<span class="hljs-attribute">opacity</span>: <span class="hljs-number">1</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>过渡动画的教程示例很精彩，推荐到官网查看。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsvelte.dev%2Ftutorial%2Ftransition" target="_blank" rel="nofollow noopener noreferrer" title="https://svelte.dev/tutorial/transition" ref="nofollow noopener noreferrer">过渡</a></p></div>  
</div>
            