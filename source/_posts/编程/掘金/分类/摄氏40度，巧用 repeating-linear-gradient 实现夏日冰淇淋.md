
---
title: '摄氏40度，巧用 repeating-linear-gradient 实现夏日冰淇淋'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dea0e6d614914f5d98b7903c74f1108c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 16:53:30 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dea0e6d614914f5d98b7903c74f1108c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“这是我参与更文挑战的第21天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>”</p>
<p>热到冒烟的天气，温度已经变得毫无道理。</p>
<p>思聪童鞋按耐不住夏日的炎热，『芳心』蠢蠢欲动。</p>
<p>但结局成为街头小巷的谈资，终于马失前蹄，喜闻乐道的被反杀了。</p>
<p>假若思聪童鞋会说冰淇淋情话：</p>
<ul>
<li>思聪： 你吃冰淇淋的时候不能笑哦</li>
<li>一宁： 为啥？</li>
<li>思聪： 你一笑它就融化了。</li>
</ul>
<p>结局还会一样吗？</p>
<p>whatever，虽然没有思聪的少爷命， 但不妨碍我们自己用 css 做一个冰淇淋，<del>关键时刻说不定真能取悦对象</del></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dea0e6d614914f5d98b7903c74f1108c~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">冰淇淋主体结构</h3>
<p>基础 html 结构：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"icecream"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cream"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"texture"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"stick"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基础 css 样式：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span>, <span class="hljs-selector-tag">html</span> &#123; <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>; &#125;

<span class="hljs-comment">/* 背景容器 */</span>
<span class="hljs-selector-class">.container</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#33485F</span>;
&#125;

<span class="hljs-comment">/* 奶油 */</span>
<span class="hljs-selector-class">.cream</span> &#123;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">190px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">260px</span>;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">80px</span> <span class="hljs-number">80px</span> <span class="hljs-number">10px</span> <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">overflow</span>: hidden;  
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#efc531</span>;  
&#125;

<span class="hljs-comment">/* 奶油左侧点缀 */</span>
<span class="hljs-selector-class">.cream</span>:after &#123;
    content: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">21px</span>;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">170px</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0.5</span>); 
&#125;

<span class="hljs-comment">/* 木棍 */</span>
<span class="hljs-selector-class">.stick</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">57px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">86px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#E09C5F</span>;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">25px</span> <span class="hljs-number">25px</span>;
  <span class="hljs-attribute">display</span>: block;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
&#125;

<span class="hljs-comment">/* 木棍点缀 */</span>
<span class="hljs-selector-class">.stick</span>:before &#123;
  display: block;
  <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">24px</span>;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#8D613B</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e773d1147b004e48b1b7a20c25a11e7c~tplv-k3u1fbpfcp-watermark.image" alt="body.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">冰淇淋纹路</h3>
<p>新增 css 纹路效果，主要是利用 <code>repeating-linear-gradient</code>。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 纹路 */</span>
<span class="hljs-selector-class">.texture</span> &#123;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">0%</span>;
  <span class="hljs-attribute">left</span>: -<span class="hljs-number">40%</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">180%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">120%</span>;
  
  <span class="hljs-attribute">background-image</span>: 
    <span class="hljs-built_in">repeating-linear-gradient</span>(
      <span class="hljs-number">#30dcf6</span> <span class="hljs-number">0%</span>,
      <span class="hljs-number">#30dcf6</span> <span class="hljs-number">25%</span>,
      <span class="hljs-number">#f2d200</span> <span class="hljs-number">25%</span>,
      <span class="hljs-number">#f2d200</span> <span class="hljs-number">50%</span>
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS函数 repeating-linear-gradient() 创建一个由重复线性渐变组成的 <code><image></code>， 这是一个类似 <code>linear-gradient</code> 的函数，并且采用相同的参数，但是它会在所有方向上重复渐变以覆盖其整个容器. 这个函数的结果是一个 <code><gradient></code> 数据类型的对象, 这是一个特殊的<code><image></code>类型。</p>
<p>repeating-linear-gradient 可以通过 <a href="https://interactive-examples.mdn.mozilla.net/pages/css/function-repeating-linear-gradient.html" target="_blank" rel="nofollow noopener noreferrer">repeating-linear-gradient</a> 这个链接在线尝试效果。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a59a3d6462a419dbbd41bd21657bdb6~tplv-k3u1fbpfcp-watermark.image" alt="texture.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本例子当中，默认沿着竖直方向重复渐变，一个 <code><image></code> 渐变图像占竖直高度的50%（意味着可以重复2次） ，内部每个色块（#30dcf6，#f2d200）各占 25%。所以如果没有 <code>.cream</code> 这个父元素 <code>over-flow: hidden</code> 这行 css 的话，预览效果是这样的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7b5e6ae21674c4b8be0e08d44b40909~tplv-k3u1fbpfcp-watermark.image" alt="tmp.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">冰淇淋动画</h3>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 纹路 */</span>
<span class="hljs-selector-class">.texture</span> &#123;
  <span class="hljs-comment">/* 略 */</span>
  <span class="hljs-attribute">animation</span>: flavours <span class="hljs-number">100s</span> linear infinite;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">155deg</span>);
&#125;

<span class="hljs-keyword">@keyframes</span> flavours &#123;
  <span class="hljs-selector-tag">to</span> &#123;
    <span class="hljs-attribute">background-position</span>: <span class="hljs-number">0</span> -<span class="hljs-number">1000vh</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，主要原理是将纹路旋转，再通过改变背景位置，开启无限循环。效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23fa0e22823a4be7945b84714bd1e8a3~tplv-k3u1fbpfcp-watermark.image" alt="icestream.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>附 codepen 源码， <a href="https://codepen.io/SunLn/pen/poeQjxz" target="_blank" rel="nofollow noopener noreferrer">css icecream, css 冰淇淋</a></p>
<h3 data-id="heading-3">最后</h3>
<p>写文不易，欢迎点赞、收藏、关注。其他可能你有兴趣的文章。</p>
<ul>
<li><a href="https://juejin.cn/post/6974230882618097677" target="_blank">前端40k高薪岗位有多少，又分布在哪里？</a></li>
<li><a href="https://juejin.cn/post/6972337061042847751" target="_blank">前端面试官问『你会造火箭吗』，我答『会的』，结果…</a></li>
<li><a href="https://juejin.cn/post/6970893008778559495" target="_blank">了解学习 Proxy 的好朋友 - Reflect，为什么需要 Reflect</a></li>
</ul>
<p>欢迎关注同名公众号【对马弹琴】。</p></div>  
</div>
            