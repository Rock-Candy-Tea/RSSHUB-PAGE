
---
title: 'CSS实战笔记(十二) 图片等比例缩放'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eaada3f2a59c4aeeaab885b2adb3b459~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 01 May 2021 18:56:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eaada3f2a59c4aeeaab885b2adb3b459~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0"><a href="https://juejin.cn/post/6957521363326205982"></a>1、背景</h3>
<p>在网页展示图片是一个很常见的需求，大多数情况下，展示区域的大小是固定的，原图片的大小也是固定的</p>
<p>如果展示区域的宽高和原图片的宽高不等比例，那么在默认情况下很可能会压缩或拉伸图片以适应区域大小</p>
<blockquote>
<p>下面我们用两张图片做一个对比实验，假设展示区域的宽高都是 300px</p>
<p>横向图片的宽高分别是 722px 和 88px，纵向图片的宽高分别是 80px 和 525px</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-class">.image</span> &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"image"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"test.png"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eaada3f2a59c4aeeaab885b2adb3b459~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c73f6c25ed8489a80ab5862d16874e4~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1"><a href="https://juejin.cn/post/6957521363326205982"></a>2、设置 CSS</h3>
<p>很显然，这并不是我们想要的，因为它会导致图片变形压缩，我们需要找到一种办法，能让图片等比例缩放</p>
<p>最简单的方法莫过于设置 CSS，使得图片可以自动适应展示区域的大小，代码非常简单</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-class">.image-box</span> &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
        &#125;
        <span class="hljs-selector-class">.image</span> &#123;
            <span class="hljs-attribute">width</span>: auto;
            <span class="hljs-attribute">height</span>: auto;
            <span class="hljs-attribute">max-width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">max-height</span>: <span class="hljs-number">100%</span>;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"image-box"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"image"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"test.png"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a4927740e4c4f95bd13e956c35fd7ea~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6dcf106853141b9a7761f458ab8b3f7~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2"><a href="https://juejin.cn/post/6957521363326205982"></a>3、使用 canvas</h3>
<p>设置 CSS 样式之后，图片会按照最小边进行等比例缩放，这种解决办法已经可以满足大多数的使用场景</p>
<p>但有时候我们会希望展示区域被占满，鱼和熊掌不可兼得，这时我们不得不裁剪图片能够等比例缩放的最大区域</p>
<p>实际上就是用一个与展示区域等比例的矩形截取图片，并要求截取出来的图片尽可能大且位于原图片的中心位置</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ef28706d37b4c3bbc9cbc83485714a7~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/632acc0eda8e4217ac07339859d683fe~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-built_in">window</span>.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">let</span> cvs = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#image'</span>)
            <span class="hljs-keyword">let</span> ctx = cvs.getContext(<span class="hljs-string">'2d'</span>)
            <span class="hljs-keyword">let</span> img = <span class="hljs-keyword">new</span> Image()
            img.src = <span class="hljs-string">'test.png'</span>
            img.onload = <span class="hljs-function">() =></span> &#123;
                <span class="hljs-keyword">let</span> adaptedImage = adaptImage(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, img.width, img.height, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, cvs.width, cvs.height)
                ctx.drawImage(img, ...adaptedImage)
            &#125;
        &#125;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">adaptImage</span>(<span class="hljs-params">imgX, imgY, imgW, imgH, cvsX, cvsY, cvsW, cvsH</span>) </span>&#123;
            <span class="hljs-keyword">let</span> idealW = imgW
            <span class="hljs-keyword">let</span> idealH = cvsH + (imgW - cvsW) * (cvsH / cvsW)
            <span class="hljs-keyword">if</span> (idealH <= imgH) &#123;
                <span class="hljs-keyword">return</span> [<span class="hljs-number">0</span>, imgH / <span class="hljs-number">2</span> - idealH / <span class="hljs-number">2</span>, idealW, idealH, cvsX, cvsY, cvsW, cvsH]
            &#125; <span class="hljs-keyword">else</span> &#123;
                idealH = imgH
                idealW = cvsW + (imgH - cvsH) * (cvsW / cvsH)
                <span class="hljs-keyword">return</span> [imgW / <span class="hljs-number">2</span> - idealW / <span class="hljs-number">2</span>, <span class="hljs-number">0</span>, idealW, idealH, cvsX, cvsY, cvsW, cvsH]
            &#125;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"image"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"300"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/842db3260b7c4a05a27fa31022f7b95c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99ee909c08184eff95d397393274cb79~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            