
---
title: 'HTML+CSS利用3D转换translate_rotate 实现旋转木马_翻转盒子_3D导航栏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ffca588d85e4e9a9bd085e5487054eb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 20:40:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ffca588d85e4e9a9bd085e5487054eb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第28天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>上一篇文章中我们学习了一些CSS 3D特效的一些理论知识，下面我们就来实战一下，实现一个3D导航栏，翻转盒子和旋转木马的特效</p>
</blockquote>
<h3 data-id="heading-0"> 案例一 实现两个翻转的盒子</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>3d demo<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">body</span>&#123;
            <span class="hljs-attribute">perspective</span>: <span class="hljs-number">350px</span>;
        &#125;
        <span class="hljs-selector-class">.box</span> &#123;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">100px</span> auto;
            <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
            <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.4s</span>;
        &#125;

        <span class="hljs-selector-class">.box</span> <span class="hljs-selector-tag">div</span> &#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">text-align</span>: center;
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
        &#125;

        <span class="hljs-selector-class">.box</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:first</span>-child &#123;
            <span class="hljs-attribute">background-color</span>: pink;
            <span class="hljs-attribute">z-index</span>: <span class="hljs-number">1</span>;
        &#125;

        <span class="hljs-selector-class">.box</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:last-child</span> &#123;
            <span class="hljs-attribute">background-color</span>: green;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">180deg</span>);
        &#125;

        <span class="hljs-selector-class">.box</span><span class="hljs-selector-pseudo">:hover</span>&#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">180deg</span>);
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>Hello<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>world<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ffca588d85e4e9a9bd085e5487054eb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">案例二 3D导航栏</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>3d demo<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-class">.box</span> &#123;
            <span class="hljs-attribute">position</span>: relative;           
            <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
            <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.4s</span>;
        &#125;

        <span class="hljs-selector-class">.box</span> <span class="hljs-selector-tag">div</span> &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">text-align</span>: center;
            <span class="hljs-attribute">background-color</span>:pink;
        &#125;

        <span class="hljs-selector-class">.box</span> <span class="hljs-selector-class">.shn</span> &#123;
            <span class="hljs-attribute">background-color</span>: green;
           <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(-<span class="hljs-number">25px</span>) <span class="hljs-built_in">translateZ</span>(-<span class="hljs-number">25px</span>) <span class="hljs-built_in">rotateX</span>(-<span class="hljs-number">90deg</span>)
        &#125;

        <span class="hljs-selector-class">.box</span><span class="hljs-selector-pseudo">:hover</span>&#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(-<span class="hljs-number">50px</span>) <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">90deg</span>);
        &#125;

        <span class="hljs-selector-tag">li</span>&#123;
            <span class="hljs-attribute">float</span>: left;
            <span class="hljs-attribute">list-style</span>: none;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>导航一<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"shn"</span>></span>导航一<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>导航二<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"shn"</span>></span>导航二<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>导航三<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"shn"</span>></span>导航三<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6bbef85cbf44d7f830c7d0b3395c160~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">案例三 旋转木马</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>旋转木马<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">body</span> &#123;
            <span class="hljs-attribute">perspective</span>: <span class="hljs-number">1000px</span>;
        &#125;

        <span class="hljs-selector-tag">section</span> &#123;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">200px</span> auto;
            <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
            <span class="hljs-attribute">animation</span>: rotate <span class="hljs-number">10s</span> linear infinite;
            <span class="hljs-attribute">background</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">caoyaolu.jpg</span>) no-repeat center;
        &#125;

        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span> &#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">background</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">timg.jfif</span>) no-repeat;
        &#125;

        <span class="hljs-selector-tag">section</span><span class="hljs-selector-pseudo">:hover</span> &#123;
            <span class="hljs-attribute">animation-play-state</span>: paused;
        &#125;

        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:first</span>-child &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">400px</span>);
        &#125;

        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">60deg</span>) <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">400px</span>);
        &#125;

        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>) &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">120deg</span>) <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">400px</span>);
        &#125;

        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">4</span>) &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">180deg</span>) <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">400px</span>);
        &#125;

        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">5</span>) &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">240deg</span>) <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">400px</span>);
        &#125;

        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">6</span>) &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">300deg</span>) <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">400px</span>);
        &#125;

        <span class="hljs-keyword">@keyframes</span> rotate &#123;
            <span class="hljs-number">0%</span> &#123;
                <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">0deg</span>);
            &#125;

            <span class="hljs-number">100%</span> &#123;
                <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">100deg</span>);
            &#125;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">section</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8b60779690445dc8ad11cdb2c3b042a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            