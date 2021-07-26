
---
title: '纯 html + css 实现彩虹蝴蝶'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df24dc5491de4769aef0c0fe38a3e588~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 02:19:55 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df24dc5491de4769aef0c0fe38a3e588~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df24dc5491de4769aef0c0fe38a3e588~tplv-k3u1fbpfcp-watermark.image" alt="hsibVxFjLx.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">代码</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"500"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"500"</span> <span class="hljs-attr">viewBox</span>=<span class="hljs-string">"0 0 480 352"</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">mask</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"mask1"</span> <span class="hljs-attr">maskContentUnits</span>=<span class="hljs-string">"userSpaceOnUse"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"480"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"352"</span> <span class="hljs-attr">xlink:href</span>=<span class="hljs-string">"https://i.pinimg.com/originals/3d/cb/c2/3dcbc2ba6a3f6ded21c66f23b1b9b2cb.gif"</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">image</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">mask</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">linearGradient</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"lg1"</span> <span class="hljs-attr">x1</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">y1</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">x2</span>=<span class="hljs-string">"100%"</span> <span class="hljs-attr">y2</span>=<span class="hljs-string">"100%"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">stop</span> <span class="hljs-attr">offset</span>=<span class="hljs-string">"15%"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"sc sc1"</span>></span><span class="hljs-tag"></<span class="hljs-name">stop</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">stop</span> <span class="hljs-attr">offset</span>=<span class="hljs-string">"45%"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"sc sc2"</span>></span><span class="hljs-tag"></<span class="hljs-name">stop</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">stop</span> <span class="hljs-attr">offset</span>=<span class="hljs-string">"55%"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"sc sc2"</span>></span><span class="hljs-tag"></<span class="hljs-name">stop</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">stop</span> <span class="hljs-attr">offset</span>=<span class="hljs-string">"85%"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"sc sc3"</span>></span><span class="hljs-tag"></<span class="hljs-name">stop</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">linearGradient</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">defs</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"url(#lg1)"</span> <span class="hljs-attr">mask</span>=<span class="hljs-string">"url(#mask1)"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100%"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100%"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">rect</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.sc</span> &#123;
    <span class="hljs-attribute">animation</span>: rainbow <span class="hljs-number">3s</span> linear infinite alternate;
&#125;

<span class="hljs-comment">/* 添加延迟, 形成交错的彩虹效果 */</span>
<span class="hljs-selector-class">.sc2</span> &#123;
    <span class="hljs-attribute">animation-delay</span>: -<span class="hljs-number">1s</span>;
&#125;

<span class="hljs-selector-class">.sc3</span> &#123;
    <span class="hljs-attribute">animation-delay</span>: -<span class="hljs-number">2s</span>;
&#125;

<span class="hljs-keyword">@keyframes</span> rainbow &#123;
    <span class="hljs-number">0%</span> &#123;
        stop-<span class="hljs-attribute">color</span>: pink;
    &#125;
    <span class="hljs-number">35%</span> &#123;
        stop-<span class="hljs-attribute">color</span>: crimson;
    &#125;
    <span class="hljs-number">50%</span> &#123;
        stop-<span class="hljs-attribute">color</span>: purple;
    &#125;
    <span class="hljs-number">85%</span> &#123;
        stop-<span class="hljs-attribute">color</span>: yellow;
    &#125;
    <span class="hljs-number">100%</span> &#123;
        stop-<span class="hljs-attribute">color</span>: orange;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">解释</h3>
<p><code>mask</code> 可以看作一个遮罩，作用在其他元素上时，黑色的部分会被隐藏，白色的部分与元素原来的背景合成新的背景。</p>
<p>用渐变的背景填充 <code>rect</code>，然后使用一个背景为黑色，主体部分为白色的蝴蝶图像作为 <code>mask</code> 作用在 <code>rect</code> 上，那么渐变背景便只显示在蝴蝶上。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3933bbc2f3547e6bd4b71647045a880~tplv-k3u1fbpfcp-watermark.image" alt="3dcbc2ba6a3f6ded21c66f23b1b9b2cb.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5c4a7f10c08404a89e570d8e04e19d2~tplv-k3u1fbpfcp-watermark.image" alt="aDnU7gkLgj.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">在线代码</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjsbin.com%2Ffiyelof%2Fedit%3Fhtml%2Ccss%2Coutput" target="_blank" rel="nofollow noopener noreferrer" title="https://jsbin.com/fiyelof/edit?html,css,output" ref="nofollow noopener noreferrer">jsbin.com/fiyelof/edi…</a></p>
<h3 data-id="heading-3">参考</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fyoksel%2Fpen%2FMKgppV" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/yoksel/pen/MKgppV" ref="nofollow noopener noreferrer">codepen.io/yoksel/pen/…</a></p></div>  
</div>
            