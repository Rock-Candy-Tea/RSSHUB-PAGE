
---
title: '纯 html + css 实现毛毛虫'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19facdb6bb22413a8f4af2f2dfd4493e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 23:53:58 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19facdb6bb22413a8f4af2f2dfd4493e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">毛毛虫</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19facdb6bb22413a8f4af2f2dfd4493e~tplv-k3u1fbpfcp-watermark.image" alt="ZtvEiHCiQ4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">分析</h3>
<ol>
<li>毛毛虫是由一个个的圆从里到外组成。</li>
<li>最里面的圆距离中心位置最近，最外层的圆距离中心位置最远。</li>
<li>圆的旋转速度是一样的，只是开始旋转的时间（或者位置）不一样。</li>
</ol>
<p>初始时</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/804afd2d959d456989e40fe6d87d18ed~tplv-k3u1fbpfcp-watermark.image" alt="WXWorkCapture_16267658011830.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后从左到右依次开始绕着圆心旋转</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddc5966ccbb84b32a66d1d9de8045111~tplv-k3u1fbpfcp-watermark.image" alt="WXWorkCapture_16267662815039.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9466f4e65e04d00ab76a9d8591687d2~tplv-k3u1fbpfcp-watermark.image" alt="WXWorkCapture_16267662762275.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">代码 - 以两个圆为例</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"rect"</span>></span>
        <span class="hljs-comment"><!-- 第一个圆 --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"circle"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"rect"</span>></span>
        <span class="hljs-comment"><!-- 第二个圆 --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"circle"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@keyframes</span> rotate &#123;
    <span class="hljs-number">0%</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">1turn</span>);
    &#125;
&#125;
<span class="hljs-selector-class">.rect</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">500px</span>;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">justify-content</span>: center;
    <span class="hljs-attribute">align-items</span>: center;
    <span class="hljs-attribute">position</span>: absolute;
&#125;
<span class="hljs-selector-class">.circle</span> &#123;
    <span class="hljs-comment">/* 圆的默认样式 */</span>
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">2px</span> <span class="hljs-number">2px</span> <span class="hljs-number">5px</span> <span class="hljs-number">5px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.1</span>);
&#125;
<span class="hljs-comment">/* 调整第一个圆旋转的开始时间和初始位置 */</span>
<span class="hljs-selector-class">.rect</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">1</span>) &#123;
    <span class="hljs-comment">/* 旋转延迟 0 */</span>
    <span class="hljs-attribute">animation</span>: rotate <span class="hljs-number">3s</span> <span class="hljs-number">0s</span> linear infinite;
&#125;
<span class="hljs-selector-class">.rect</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">1</span>) <span class="hljs-selector-class">.circle</span> &#123;
    <span class="hljs-comment">/* 相对于圆心的偏移量 10px */</span>
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(<span class="hljs-number">10px</span>);
    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">43deg</span>, <span class="hljs-number">#4158D0</span> <span class="hljs-number">0%</span>, <span class="hljs-number">#C850C0</span> <span class="hljs-number">46%</span>, <span class="hljs-number">#FFCC70</span> <span class="hljs-number">100%</span>);
&#125;

<span class="hljs-comment">/* 调整第二个圆旋转的开始时间和初始位置 */</span>
<span class="hljs-selector-class">.rect</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
    <span class="hljs-comment">/* 旋转延迟 250ms */</span>
    <span class="hljs-attribute">animation</span>: rotate <span class="hljs-number">3s</span> <span class="hljs-number">250ms</span> linear infinite;
&#125;
<span class="hljs-selector-class">.rect</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) <span class="hljs-selector-class">.circle</span> &#123;
    <span class="hljs-comment">/* 相对圆心偏移 20px */</span>
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(<span class="hljs-number">20px</span>);
    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">160deg</span>, <span class="hljs-number">#0093E9</span> <span class="hljs-number">0%</span>, <span class="hljs-number">#80D0C7</span> <span class="hljs-number">100%</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两个圆时的情况</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de7b066146a04e8fae7b6d1a90313d4b~tplv-k3u1fbpfcp-watermark.image" alt="M6Lotr7Gtc.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来只要照着上面的规则加圆（越往外层的圆偏移量越大, 动画开始时间越晚），就可以达到毛毛虫的效果。</p>
<h3 data-id="heading-3">完整代码</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjsbin.com%2Fxanalug%2Fedit%3Fhtml%2Ccss%2Coutput" target="_blank" rel="nofollow noopener noreferrer" title="https://jsbin.com/xanalug/edit?html,css,output" ref="nofollow noopener noreferrer">jsbin.com/xanalug/edi…</a></p></div>  
</div>
            