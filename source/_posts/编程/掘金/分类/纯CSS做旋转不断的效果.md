
---
title: '纯CSS做旋转不断的效果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35eaf42fcd984d6cbb0fe8b8b4ccaed3~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 00:30:12 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35eaf42fcd984d6cbb0fe8b8b4ccaed3~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<p>昨天学习了CSS的<code>animation</code>动画特性，做了一个简单的放大字体效果。</p>
<p>文章链接如下：<a href="https://juejin.cn/post/6992503829367357448" target="_blank" title="https://juejin.cn/post/6992503829367357448">juejin.cn/post/699250…</a></p>
<p>今天学习一个不太熟悉的CSS属性：transform。</p>
<p>MDN官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Ftransform" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/transform" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
<blockquote>
<p><code>transform</code>属性允许你旋转，缩放，倾斜或平移给定元素。这是通过修改CSS视觉格式化模型的坐标空间来实现的。</p>
</blockquote>
<p>其中可选得转换样式被称为<code>transform-functions</code>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2Ftransform-function" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/transform-function" ref="nofollow noopener noreferrer">MDN文档</a>中关于<code>transform-functions</code>，列举了包括<code>matrix</code>, <code>matrix3d</code>, <code>perspective</code>, <code>rotate</code>等多个函数。</p>
<p>本文会用到上一篇文章中介绍的<code>animation</code>以及transform中的rotate函数。</p>
<p>其中有几个关键点值得注意</p>
<ol>
<li>animation属性值中的速度设置为linear。表示动画变化是匀速的。</li>
</ol>
<p>如果是默认的ease，即默认逐渐变慢的速度时，可以看到动画在转换为25%，50%，75%时会有比较明显的卡顿效果。<strong>这也帮助我们理解了animation中的速度函数，是针对@keyframes中的每一段的，而不是从开始到结束的</strong>，若采用<code>ease</code>默认值，效果如下所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35eaf42fcd984d6cbb0fe8b8b4ccaed3~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt="35e414a4-a38d-46e1-834f-9b60dd2ae3e7.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>animation属性中的定义播放次数为：infinate，表示无限次数播放，从而可以使动画一直循环播放。</li>
</ol>
<p>最终的播放效果如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c2fcf5619d54163aa1dfc70093c1572~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt="808c465f-8ff0-4697-a941-684e72aa5c72.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"border"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"rotate"</span>></span>
        中国加油！奥运健儿加油！
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.border</span> &#123;
        <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid black;
    &#125;
    <span class="hljs-selector-tag">body</span> &#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">flex-direction</span>: row;
        <span class="hljs-attribute">align-items</span>: center;
        <span class="hljs-attribute">justify-content</span>: center;
    &#125;

    <span class="hljs-selector-class">.rotate</span> &#123;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">align-items</span>: center;
        <span class="hljs-attribute">justify-content</span>: center;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">color</span>: red;
        <span class="hljs-attribute">animation</span>: rotate <span class="hljs-number">10s</span> linear infinite;
        -webkit-<span class="hljs-attribute">animation</span>: rotate <span class="hljs-number">10s</span> linear infinite;
        
    &#125;

    <span class="hljs-keyword">@keyframes</span> rotate &#123;
        <span class="hljs-number">0%</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
        &#125;

        <span class="hljs-number">25%</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">90deg</span>);
        &#125;

        <span class="hljs-number">50%</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">180deg</span>);
        &#125;

        <span class="hljs-number">75%</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">270deg</span>);
        &#125;

        <span class="hljs-number">100%</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">360deg</span>);
        &#125;
    &#125;

    <span class="hljs-keyword">@-webkit-keyframes</span> rotate &#123;
        <span class="hljs-number">0%</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
        &#125;

        <span class="hljs-number">25%</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">90deg</span>);
        &#125;

        <span class="hljs-number">50%</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">180deg</span>);
        &#125;

        <span class="hljs-number">75%</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">270deg</span>);
        &#125;

        <span class="hljs-number">100%</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">360deg</span>);
        &#125;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>PS: 制作动画所用软件为ScreenToGif。</p></div>  
</div>
            