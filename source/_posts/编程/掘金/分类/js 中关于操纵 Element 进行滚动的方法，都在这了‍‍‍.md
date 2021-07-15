
---
title: 'js 中关于操纵 Element 进行滚动的方法，都在这了‍‍‍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b95ac84944742f89d76cb43cd05c40b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 19:04:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b95ac84944742f89d76cb43cd05c40b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>为了方便咱操作 html 中的元素滚动条进行上下左右的滚动，js 自带了N种（规范内）方法：</p>
<h4 data-id="heading-0">适用 ScrollToOptions 的方法</h4>
<blockquote>
<p>CSSOM View 规范的 <code>ScrollToOptions</code> 用于指定一个元素应该滚动到哪里，以及滚动是否应该平滑，它可以作为参数提供给以下方法：</p>
<ul>
<li>
<p>Window.scroll()</p>
</li>
<li>
<p>Window.scrollTo()</p>
</li>
<li>
<p>Window.scrollBy()</p>
</li>
<li>
<p>Element.scroll()</p>
</li>
<li>
<p>Element.scrollTo()</p>
</li>
<li>
<p>Element.scrollBy()</p>
</li>
<li>
<p>这么多方法我该怎么选，怎么用？<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b95ac84944742f89d76cb43cd05c40b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>使用方法：</p>
<pre><code class="hljs language-js copyable" lang="js">element.scrollTo(x-coord, y-coord)
<span class="hljs-comment">// or</span>
element.scrollTo(options)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数</p>
<ul>
<li>x-coord(必填): 是期望滚动到位置水平轴上距元素左上角的像素，例如：element.scrollTo(100, 0)。</li>
<li>y-coord(必填): 是期望滚动到位置竖直轴上距元素左上角的像素，例如：element.scrollTo(0, 100)。</li>
</ul>
<p>或者</p>
<ul>
<li>options: 遵循 CSSOM View 规范的 ScrollToOptions 对象。</li>
</ul>
<p><code>两种方案适用于以上全部方法，需要注意：scrollBy 方法回滚时需要填写负数数值~</code></p>
</blockquote>
<p>诶，划重点，遵循 CSSOM View 规范的 <code>ScrollToOptions</code>，以上罗列的方法都遵循 CSSOM View 的规范，所以它们的使用方法可以说是完全一致，只是名儿不一样，<code>ohhhhhhh CSSOM View yyds！</code>
MDN文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FScrollToOptions" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/ScrollToOptions" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
<p>接下来再看看 ScrollToOptions 怎么耍：</p>
<blockquote>
<p>ScrollToOptions 共接受三个参数：</p>
<ul>
<li>top (Number): 指定 window 或元素 Y 轴方向滚动的像素数。`</li>
<li>left (Number): 指定 window 或元素 X 轴方向滚动的像素数。</li>
<li>behavior (smooth | instant | auto) : 默认值 auto(效果等同 instant)，指定滚动是否应该(smooth)平滑进行，还是立即跳到(instant)指定位置。该属性实际上定义在 ScrollOptions 上，它通过 ScrollToOptions 实现。</li>
</ul>
</blockquote>
<h4 data-id="heading-1">通过配置 ScrollToOptions 进行滚动：</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> options = &#123;
<span class="hljs-attr">left</span>: <span class="hljs-number">100</span>,
<span class="hljs-attr">top</span>: <span class="hljs-number">100</span>,
<span class="hljs-attr">behavior</span>: <span class="hljs-string">'smooth'</span>
&#125;;
<span class="hljs-built_in">window</span>.scrollTo.scroll(options);


<span class="hljs-comment">// window.scrollTo</span>
<span class="hljs-keyword">const</span> checked = <span class="hljs-literal">true</span>;
<span class="hljs-keyword">const</span> scrollOptions = &#123;
<span class="hljs-attr">left</span>: <span class="hljs-number">100</span>,
<span class="hljs-attr">top</span>: <span class="hljs-number">100</span>,
<span class="hljs-attr">behavior</span>: checked ? <span class="hljs-string">'smooth'</span> : <span class="hljs-string">'auto'</span>
&#125;;

<span class="hljs-built_in">window</span>.scrollTo(scrollOptions);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">以上各种方法控制（上下左右）滚动代码：</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> scroller = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'scroller'</span>);

<span class="hljs-comment">// scroll 与 scrollTo (两种方法使用方式完全一致，所以只写出 scrollTo)</span>
<span class="hljs-comment">/* 向上滚动 */</span>
scroller.scrollTo(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
<span class="hljs-comment">// or </span>
scroller.scrollTo(&#123; <span class="hljs-attr">top</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">behavior</span>: <span class="hljs-string">'smooth'</span> &#125;);


<span class="hljs-comment">/* 向下滚动 */</span>
scroller.scrollTo(<span class="hljs-number">0</span>, scroller.scrollHeight);
<span class="hljs-comment">// or</span>
scroller.scrollTo(&#123; <span class="hljs-attr">top</span>: scroller.scrollHeight, <span class="hljs-attr">behavior</span>: <span class="hljs-string">'smooth'</span>&#125;)


<span class="hljs-comment">/* 向左滚动 */</span>
scroller.scrollTo(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
<span class="hljs-comment">// or</span>
scroller.scrollTo(&#123; <span class="hljs-attr">left</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">behavior</span>: <span class="hljs-string">'smooth'</span>&#125;)


<span class="hljs-comment">/* 向右滚动 */</span>
scroller.scrollTo(scroller.scrollWidth);
<span class="hljs-comment">// or</span>
scroller.scrollTo(&#123; <span class="hljs-attr">left</span>: scroller.scrollWidth, <span class="hljs-attr">behavior</span>: <span class="hljs-string">'smooth'</span>&#125;)

<span class="hljs-comment">// ----------------- scrollBy (回滚滚动条需要写负数，其它一致) -----------------</span>
<span class="hljs-comment">/* 向上滚动 */</span>
scroller.scrollBy(<span class="hljs-number">0</span>, -scroller.scrollHeight);
<span class="hljs-comment">// or </span>
scroller.scrollTo(&#123; <span class="hljs-attr">top</span>: -scroller.scrollHeight, <span class="hljs-attr">behavior</span>: <span class="hljs-string">'smooth'</span> &#125;);

<span class="hljs-comment">/* 向左滚动 */</span>
scroller.scrollBy(-scroller.scrollWidth, <span class="hljs-number">0</span>);
<span class="hljs-comment">// or </span>
scroller.scrollTo(&#123; <span class="hljs-attr">left</span>: -scroller.scrollWidth, <span class="hljs-attr">behavior</span>: <span class="hljs-string">'smooth'</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ul>
<li>scrollWidth: 是元素全部内容的<code>宽度</code>，包括由于overflow溢出而在屏幕上不可见的内容</li>
<li>scrollHeight: 是元素全部内容的<code>高度</code>，包括由于overflow溢出而在屏幕上不可见的内容</li>
<li>scrollTop: 横向滚动条距离元素最顶部的距离</li>
<li>scrollLeft: 横向滚动条距离元素最左侧的距离</li>
</ul>
</blockquote>
<p>以上直接使用 x,y 坐标轴方式滚动，写法简便，但是如果想要单独设置x, y轴时比较麻烦，因为两个参数都是必填的，相反 ScrollToOptions 配置方式则相对灵活，并且可以配置平滑滚动，坐标轴方式则不支持。所以，该用哪个你懂我意思吗？</p>
<h4 data-id="heading-3">同胞兄弟 Element.scrollIntoView()</h4>
<blockquote>
<p>Element 接口的 scrollIntoView() 方法会滚动元素的父容器，使被调用 scrollIntoView() 的元素对用户可见。</p>
<pre><code class="hljs language-js copyable" lang="js">element.scrollIntoView(); <span class="hljs-comment">// 等同于element.scrollIntoView(true)</span>
element.scrollIntoView(alignToTop); <span class="hljs-comment">// Boolean型参数</span>
element.scrollIntoView(scrollIntoViewOptions); <span class="hljs-comment">// Object型参数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>使用方法：</code>
alignToTop（Boolean 可选）</p>
<ul>
<li>true：元素的顶端将和其所在滚动区的可视区域的顶端对齐。相应的 scrollIntoViewOptions: &#123; block: "start", inline: "nearest" &#125;。这是这个参数的默认值。</li>
<li>false：元素的底端将和其所在滚动区的可视区域的底端对齐。相应的scrollIntoViewOptions: &#123; block: "end", inline: "nearest" &#125;。</li>
</ul>
<p><code>or</code>
scrollIntoViewOptions （<code>CSSOM View</code> 规范的一个包含下列属性的对象：可选，）</p>
<ul>
<li>behavior (可选)：定义动画过渡效果， （smooth | instant | auto） 之一。默认为 "auto"。</li>
<li>block (可选)：定义垂直方向的对齐， "start", "center", "end", 或 "nearest"之一，默认为 "start"，start，center，end 分别对应上中下，nearest 表示滚动到距离最近的点。</li>
<li>inline (可选)：定义水平方向的对齐， "start", "center", "end", 或 "nearest"之一，默认为 "nearest"，start，center，end 分别对应左中右，nearest 表示滚动到距离最近的点。</li>
</ul>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> element = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"box"</span>);

<span class="hljs-comment">/* 滚动到顶部 */</span>
element.scrollIntoView();
<span class="hljs-comment">// or</span>
element.scrollIntoView(&#123; <span class="hljs-attr">behavior</span>: <span class="hljs-string">"smooth"</span>, <span class="hljs-attr">block</span>: <span class="hljs-string">"start"</span> &#125;);

<span class="hljs-comment">/* 滚动到底部 */</span>
element.scrollIntoView(<span class="hljs-literal">false</span>);
<span class="hljs-comment">// or</span>
element.scrollIntoView(&#123; <span class="hljs-attr">behavior</span>: <span class="hljs-string">"smooth"</span>, <span class="hljs-attr">block</span>: <span class="hljs-string">"end"</span> &#125;);

<span class="hljs-comment">/* 滚动到最左侧 */</span>
element.scrollIntoView(&#123; <span class="hljs-attr">behavior</span>: <span class="hljs-string">"smooth"</span>, <span class="hljs-attr">inline</span>: <span class="hljs-string">"start"</span> &#125;);

<span class="hljs-comment">/* 滚动到最右侧 */</span>
element.scrollIntoView(&#123; <span class="hljs-attr">behavior</span>: <span class="hljs-string">"smooth"</span>, <span class="hljs-attr">inline</span>: <span class="hljs-string">"end"</span> &#125;);

<span class="hljs-comment">/* 滚动到中间位置 */</span>
element.scrollIntoView(&#123; <span class="hljs-attr">behavior</span>: <span class="hljs-string">"smooth"</span>, <span class="hljs-attr">block</span>: <span class="hljs-string">'center'</span>, <span class="hljs-attr">inline</span>: <span class="hljs-string">"center"</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">简单案例，欢迎来踩：</h5>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2F_DreamMaker7%2Fpen%2FPomWQMK" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/_DreamMaker7/pen/PomWQMK" ref="nofollow noopener noreferrer">codepen.io/_DreamMaker…</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/790faa915caf44778047299f47f31d04~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
关于 Element 滚动就讲到这里，如果文中有错误或者可以改进的地方请立即在评论区公开处刑，觉得写的不错的话，来个小小的点赞，你的鼓励是我坚持的动力，谢谢😀~</p></div>  
</div>
            