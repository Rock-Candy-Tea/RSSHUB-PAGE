
---
title: '使用css制作圆弧形背景 _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f14a256bbaf4e0e9d29f5829fdde043~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 05:04:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f14a256bbaf4e0e9d29f5829fdde043~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">问题一</h1>
<p>使用background制作制作一个类似下图的圆弧形渐变背景图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f14a256bbaf4e0e9d29f5829fdde043~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">思路</h1>
<p>需要在当前的基础上制作一个更大的盒子, 如下图红框部分所示 (比如设置<code>width</code>为150%). 然后通过设置盒子的<code>border-bottom-left-radius</code> 和 <code>border-bottom-right-radius</code>来形成圆弧的效果.</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04fac3f6925d44339dacbdf53ade7e7f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>设置好<code>radius</code>以后需要把大盒子往左边拽回一部分距离 (比如往左移动25%), 使得视口部分在大盒子的正中央, 如下图所示. 可以通过<code>position</code>来设置背景大盒子的位置.</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43dd22d568d64e91922ab2a3f69fd40b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">代码 (流式布局)</h1>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 焦点图部分 --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"banner"</span>></span>
            <span class="hljs-comment"><!-- 利用一个标签的背景制作了大盒子的背景效果 --></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"banner-bg"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-comment"><!-- 下面是滑动焦点图部分 --></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.banner</span> &#123;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">187px</span>;
    <span class="hljs-attribute">overflow</span>: hidden;
&#125;

<span class="hljs-selector-class">.banner</span> <span class="hljs-selector-class">.banner-bg</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">left</span>: -<span class="hljs-number">25%</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">150%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">145px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#C82519</span>;
    <span class="hljs-attribute">border-bottom-left-radius</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">border-bottom-right-radius</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">0deg</span>, <span class="hljs-number">#f1503b</span>, <span class="hljs-number">#c82519</span> <span class="hljs-number">50%</span>);  <span class="hljs-comment">/* 渐变 */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">问题二</h1>
<p>使用图片制作一个如下的弧形背景图</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2223c14c4e94e089ae556ab310070df~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">思路</h2>
<p>与上面思路相同的一点是: 
都需要制作一个大盒子, 并且通过设置盒子的<code>border-bottom-left-radius</code> 和 <code>border-bottom-right-radius</code>来形成圆弧的效果.</p>
<p>不同点在于:
在下面的代码中, 没有直接设置一个宽度为150%的大盒子, 而是设置一个宽度为100%和盒子, 通过在左右两侧各<code>padding</code>一个25%的值来得到一个大盒子. 对于<code><a></code>和<code><img></code>标签来说, 就不需要进行额外的宽度设置了.</p>
<p>有一个值得注意的点是这次的<code>overflow: hidden</code> 直接设置给了父元素<code><div></code>, 通过隐藏超出部分而使子元素只能显示圆弧内的部分, 而不是直接在子元素上设置圆弧.</p>
<p>这时候图片距离左边是有一定距离的, 这是因为父元素设置了<code>padding</code>, 这个值为25%. 但这时不能直接将整个父元素表示出的大盒子向左移动25%, 这是因为这个25%是针对宽度100%而言的, 而加上左右两边的<code>padding</code>后整个大盒子的宽度为150%, 因此需要向左移动的距离为150%的25%, 也就是25%/150% = 1/6 = 16.666%. 所以正确的方法应该是向左移动16.666%, 而不是25%</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f715e2d97c04feab76faa2d462c9268~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">代码</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 焦点图部分 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"focus"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"images/banner.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 焦点图样式 */</span>
<span class="hljs-selector-class">.focus</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span> <span class="hljs-number">25%</span>;
  <span class="hljs-attribute">border-bottom-left-radius</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">border-bottom-right-radius</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(-<span class="hljs-number">16.666%</span>);
  <span class="hljs-attribute">overflow</span>: hidden;
&#125;
<span class="hljs-selector-class">.focus</span> <span class="hljs-selector-tag">a</span> &#123;
  <span class="hljs-attribute">display</span>: block;
&#125;
<span class="hljs-selector-class">.focus</span> <span class="hljs-selector-tag">a</span> <span class="hljs-selector-tag">img</span> &#123;
  <span class="hljs-attribute">display</span>: block;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            