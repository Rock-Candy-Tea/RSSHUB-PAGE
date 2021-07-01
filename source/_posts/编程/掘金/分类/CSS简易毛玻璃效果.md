
---
title: 'CSS简易毛玻璃效果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1448aa074df4970ab86655f3f365dc3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 22:35:49 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1448aa074df4970ab86655f3f365dc3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">CSS 毛玻璃效果</h2>
<h3 data-id="heading-1">一、什么是毛玻璃效果？</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1448aa074df4970ab86655f3f365dc3~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<ul>
<li>背景模糊的磨砂玻璃效果</li>
</ul>
</blockquote>
<blockquote>
<ul>
<li>空间物体漂浮多层次</li>
</ul>
</blockquote>
<blockquote>
<ul>
<li>鲜艳的色彩突出模糊的透明度</li>
</ul>
</blockquote>
<blockquote>
<ul>
<li>半透明物体上有一个细微的光线边界</li>
</ul>
</blockquote>
<h3 data-id="heading-2">二、如何实现？</h3>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.example</span>&#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0.2</span>);
    -webkit-backdrop-<span class="hljs-attribute">filter</span>: <span class="hljs-built_in">blur</span>(<span class="hljs-number">8px</span>);
    backdrop-<span class="hljs-attribute">filter</span>: <span class="hljs-built_in">blur</span>(<span class="hljs-number">8px</span>);
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">25px</span>;
    <span class="hljs-attribute">box-shadow</span>:inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">6px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">0.2</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">三、兼容问题？</h3>
<blockquote>
<p>1、如果只是简单的背景，可以使用 <code>background-attachment: fixed</code> 配合 <code>filter: blur()</code> 进行模拟；<br></p>
</blockquote>
<blockquote>
<p>2、对于fireFox浏览器，可以使用 <code>moz-element()</code> 配合 <code>filter: blur()</code> 实现复杂背景毛玻璃效果；<br></p>
</blockquote>
<blockquote>
<p>3、如不兼容上述效果，可以通过设置 <code>background: rgba(255, 255, 255, 0.5)</code> 来回到半透明效果。</p>
</blockquote></div>  
</div>
            