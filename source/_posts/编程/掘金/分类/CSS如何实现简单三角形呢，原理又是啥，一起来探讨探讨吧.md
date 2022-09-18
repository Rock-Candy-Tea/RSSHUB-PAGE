
---
title: 'CSS如何实现简单三角形呢，原理又是啥，一起来探讨探讨吧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65cf048beb194784b6ce102bc58ba2e4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Sun, 18 Sep 2022 05:49:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65cf048beb194784b6ce102bc58ba2e4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>在前端开发的时候，我们有时候会需要用到一个三角形的形状，比如地址选择或者播放器里面播放按钮</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65cf048beb194784b6ce102bc58ba2e4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通常情况下，我们会使用图片或者<code>svg</code>去完成三角形效果图，但如果单纯使用<code>css</code>如何完成一个三角形呢？</p>
<p>实现过程似乎也并不困难，通过边框就可完成</p>
<h2 data-id="heading-1">二、实现过程</h2>
<p>在以前也讲过盒子模型，默认情况下是一个矩形，实现也很简单</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.border</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
        <span class="hljs-attribute">border</span>: <span class="hljs-number">2px</span> solid;
        <span class="hljs-attribute">border-color</span>: <span class="hljs-number">#96ceb4</span> <span class="hljs-number">#ffeead</span> <span class="hljs-number">#d9534f</span> <span class="hljs-number">#ffad60</span>;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"border"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c48474db08b84f60a3ff884c904792cf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>将<code>border</code>设置<code>50px</code>，效果图如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d8e265f6f06441c8f8e59502cb7126d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>白色区域则为<code>width</code>、<code>height</code>，这时候只需要你将白色区域部分宽高逐渐变小，最终变为0，则变成如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd0f6721a80744f29056da2ce57682a3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候就已经能够看到4个不同颜色的三角形，如果需要下方三角形，只需要将上、左、右边框设置为0就可以得到下方的红色三角形</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4daa9b94d4dd43ada0e358859e4b1d40~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但这种方式，虽然视觉上是实现了三角形，但实际上，隐藏的部分任然占据部分高度，需要将上方的宽度去掉</p>
<p>最终实现代码如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.border</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">border-style</span>:solid;
    <span class="hljs-attribute">border-width</span>: <span class="hljs-number">0</span> <span class="hljs-number">50px</span> <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">border-color</span>: transparent transparent <span class="hljs-number">#d9534f</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想要实现一个只有边框是空心的三角形，由于这里不能再使用<code>border</code>属性，所以最直接的方法是利用伪类新建一个小一点的三角形定位上去</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.border</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">border-style</span>:solid;
    <span class="hljs-attribute">border-width</span>: <span class="hljs-number">0</span> <span class="hljs-number">50px</span> <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">border-color</span>: transparent transparent <span class="hljs-number">#d9534f</span>;
    <span class="hljs-attribute">position</span>: relative;
&#125;
<span class="hljs-selector-class">.border</span><span class="hljs-selector-pseudo">:after</span>&#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">border-style</span>:solid;
    <span class="hljs-attribute">border-width</span>: <span class="hljs-number">0</span> <span class="hljs-number">40px</span> <span class="hljs-number">40px</span>;
    <span class="hljs-attribute">border-color</span>: transparent transparent <span class="hljs-number">#96ceb4</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8376c43f388470c9dab657961c441f1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="i" loading="lazy" referrerpolicy="no-referrer"></p>
<p>伪类元素定位参照对象的内容区域宽高都为0，则内容区域即可以理解成中心一点，所以伪元素相对中心这点定位</p>
<p>将元素定位进行微调以及改变颜色，就能够完成下方效果图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d882e6ce2b24204a0b284cf7ddd0c0c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最终代码如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.border</span><span class="hljs-selector-pseudo">:after</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">border-style</span>: solid;
    <span class="hljs-attribute">border-width</span>: <span class="hljs-number">0</span> <span class="hljs-number">40px</span> <span class="hljs-number">40px</span>;
    <span class="hljs-attribute">border-color</span>: transparent transparent <span class="hljs-number">#96ceb4</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">6px</span>;
    <span class="hljs-attribute">left</span>: -<span class="hljs-number">40px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">三、原理分析</h2>
<p>可以看到，边框是实现三角形的部分，边框实际上并不是一个直线，如果我们将四条边设置不同的颜色，将边框逐渐放大，可以得到每条边框都是一个梯形</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28555ab010d54c16b503b7d63d2eaa19~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当分别取消边框的时候，发现下面几种情况：</p>
<ul>
<li>取消一条边的时候，与这条边相邻的两条边的接触部分会变成直的</li>
<li>当仅有邻边时， 两个边会变成对分的三角</li>
<li>当保留边没有其他接触时，极限情况所有东西都会消失</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d306a72f73c45a4b7234616a1b36583~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上图的变化规则，利用旋转、隐藏，以及设置内容宽高等属性，就能够实现其他类型的三角形</p>
<p>如设置直角三角形，如上图倒数第三行实现过程，我们就能知道整个实现原理</p>
<p>实现代码如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
    <span class="hljs-comment">/* 内部大小 */</span>
    <span class="hljs-attribute">width</span>: <span class="hljs-number">0px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">0px</span>;
    <span class="hljs-comment">/* 边框大小 只设置两条边*/</span>
    <span class="hljs-attribute">border-top</span>: <span class="hljs-number">#4285f4</span> solid;
    <span class="hljs-attribute">border-right</span>: transparent solid;
    <span class="hljs-attribute">border-width</span>: <span class="hljs-number">85px</span>; 
    <span class="hljs-comment">/* 其他设置 */</span>
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">50px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            