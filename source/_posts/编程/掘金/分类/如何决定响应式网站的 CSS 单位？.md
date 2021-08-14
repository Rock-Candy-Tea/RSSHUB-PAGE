
---
title: '如何决定响应式网站的 CSS 单位？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a5fe643ef55438abcb5954e3c74c889~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 17:42:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a5fe643ef55438abcb5954e3c74c889~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第14天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p><strong>很高兴又见面了！😊</strong></p>
<blockquote>
<p><strong>在我们创建适合各种设备的响应式网站时，了解正确的CSS 单位很重要。不过在深入研究决策之前，让我们先对它们进行分类以便了解它们的用途。</strong></p>
</blockquote>
<h1 data-id="heading-0">如何决定响应式网站的 CSS 单位？</h1>
<p><strong>1.绝对单位</strong></p>
<ul>
<li>px - 像素</li>
<li>pt - 点</li>
<li>pc - Picas</li>
<li>in - 英寸</li>
<li>cm - 厘米</li>
<li>mm - 毫米</li>
</ul>
<p><strong>2.百分比单位</strong></p>
<ul>
<li>百分比 % 单位</li>
</ul>
<p><strong>3.相对单位</strong></p>
<ul>
<li>
<p>相对于字体大小</p>
<ul>
<li>em</li>
<li>rem - 根 em</li>
</ul>
</li>
<li>
<p>相对于查看端口/文档</p>
<ul>
<li>vw</li>
<li>vh</li>
<li>vmax</li>
<li>vmin</li>
</ul>
</li>
</ul>
<p><strong>在这里学习最常见的单位 👇</strong></p>
<h2 data-id="heading-1">🚁 px 单位</h2>
<blockquote>
<p><strong>绝对像素单位仅用于屏幕（界面），其余单位用于打印。px 单位不是一个好的选择，实际上这不是用于缩放。无论您选择什么屏幕尺寸，px 单位的尺寸都是固定的。这就是为什么边框总是首选 px 单位的原因，因为边框在所有屏幕尺寸上也保持固定。</strong></p>
</blockquote>
<h2 data-id="heading-2">🎪 ％ 单位</h2>
<blockquote>
<p><strong>这用于设置元素的宽度，它总是相对于其直接父元素的大小。如果没有定义的父级，则默认情况下body被视为父级。</strong></p>
</blockquote>
<p><strong>考虑一个宽度为 500px 的盒子，里面有一个 h1 元素</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid crimson;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-tag">h1</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果👇</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a5fe643ef55438abcb5954e3c74c889~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>👉如果没有定义父级，那么 root 将被视为默认父级。</strong></p>
<h2 data-id="heading-3">⚓ em 单位</h2>
<blockquote>
<p><strong>em 单位总是相对于它的直接父级的字体大小。1em == <code>一个父字体大小</code>。如果未覆盖，默认字体大小为 16px，假设在父元素中字体大小为 48px，那么在子元素中为 1em == 48px。</strong></p>
</blockquote>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">h1</span>&#123; 
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1em</span>; <span class="hljs-comment">/* now 1em == 16px */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果👇</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab3dbaddc3904425bd3331742f2c0c2d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.container</span>&#123;
   <span class="hljs-attribute">font-size</span>: <span class="hljs-number">48px</span>; 
<span class="hljs-comment">/* 或 3em，因为默认字体大小是 16px
& 它的父元素是 body，所以 3*16px 就是 48px */</span>
&#125;
<span class="hljs-selector-tag">h1</span>&#123;
   <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1em</span>; <span class="hljs-comment">/* now 1em == 48px */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果👇</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a67ec5704d1b46fabd361af87aa89dfa~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<strong>我们可以将这个单位用于边距和填充，因为它可以让我们根据元素的字体大小在框周围使用灵活的间距。元素 font-size 会根据设备大小而变化，因此元素周围的间距也将分别发生变化。</strong></p>
<h2 data-id="heading-4">🛵 rem 单位</h2>
<blockquote>
<p><strong>r 代表 root  em，与 em 不同，它总是相对于根字体大小，无论它的下一个父元素具有什么字体大小。如果根已经重新定义了字体大小，如 60px 那么 1rem == 60px 。</strong></p>
</blockquote>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">html</span>&#123;
   <span class="hljs-attribute">font-size</span>: <span class="hljs-number">60px</span>;
&#125;
<span class="hljs-selector-class">.container</span>&#123;
   <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
&#125;
<span class="hljs-selector-tag">h1</span>&#123;
   <span class="hljs-attribute">font-size</span>: <span class="hljs-number">1rem</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果👇</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd391c2335fa478598a1eefb5f7fa554~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">🚋 vw 单位</h2>
<blockquote>
<p><strong>vw 代表 viewprot width（视口宽度），这意味着 vw 总是相对于根宽度的 1%，与父元素的宽度无关。所以，如果 <code>1vw == 1%</code> 那么 <code>100vw == 100%</code> 视口宽度。</strong></p>
</blockquote>
<p><strong>让我们考虑以下示例，其中一个子项的宽度相对于父项的大小，而另一个子项的宽度相对于根。</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.container</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">600px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">2px</span> solid black;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;
<span class="hljs-selector-class">.box1</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">background</span>: skyblue;
&#125;
<span class="hljs-selector-class">.box2</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">70vw</span>;
  <span class="hljs-attribute">background</span>: pink;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果👇</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2c9577e3c8947228e21aeeac30224e0~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">🛸 vh 单位</h2>
<blockquote>
<p><strong>vh 代表 viewprot height （视口高度），如 vw 它也相对于根/文档的 1% 高度。让我们考虑以下示例，其中一个子级的高度与父级大小有关，而另一个子级的高度与根相关。</strong></p>
</blockquote>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.container</span>&#123;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">2px</span> solid;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">40px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">800px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
&#125;
<span class="hljs-selector-class">.box1</span>&#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">background</span>: skyblue;
&#125;
<span class="hljs-selector-class">.box2</span>&#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">background</span>: pink;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">50%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果👇</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6a37ab74e8c4c8f815a35c6ae9ebefa~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">🛬 wuhu ! 起飞 !</h2>
<h3 data-id="heading-8">概括总结</h3>
<p>🌟 <strong>px单位常用于边框。<br>
🌟 % 单位相对于相对父级的宽度。<br>
🌟 em 单位相对于元素字体大小的边距和填充 。<br>
🌟 rem 单位相对于根的字体大小 。<br>
🌟 vw 和 vh 表示相对于根的宽度和高度。<br>
🌟 这些是 6 个 css 单元，它们最常用于使网站具有响应性。</strong></p>
<blockquote>
<p><strong>我已经写了很长一段时间的技术博客，并且主要通过CSDN发表，这是我的一篇 响应式网站的 CSS 单位教程。我喜欢通过文章分享技术与快乐。您可以访问我的博客： <a href="https://juejin.cn/user/2040341402229751/posts" target="_blank" title="https://juejin.cn/user/2040341402229751/posts">掘金-海拥</a>  以了解更多信息。希望你们会喜欢！</strong></p>
</blockquote>
<p><strong>💌 欢迎大家在评论区提出意见和建议！💌</strong></p>
<p><strong>如果你真的从这篇文章中学到了一些新东西，喜欢它，收藏它并与你的小伙伴分享。🤗最后，不要忘了❤或📑支持一下哦。</strong></p></div>  
</div>
            