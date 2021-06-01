
---
title: '用 CSS 找回童年的快乐，哆啦A梦伴你同行'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/329bc7093e484ff882bd2d854afa2f6c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 31 May 2021 16:29:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/329bc7093e484ff882bd2d854afa2f6c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>小时候我就想，如果能有一个像哆啦A梦一样的朋友陪伴我们成长该有多好？悲伤时有人安慰；想放弃的时候，有人鼓励；快乐的时候，有人分享。最关键的是他拥有无所不能的神奇口袋。而如今长大了，反过来我希望能像哆啦A梦一样，陪伴着孩子成长。于是作为给我们的儿童节礼物，接下来通过 CSS 画一个《哆啦A梦，伴你同行》的海报，一起找回童年的回忆吧。</p>
<h1 data-id="heading-1">相关知识点</h1>
<p>CSS 中能画图的大多数人第一时间想到的就是 <code>canvas</code>，但是还有一个 API 不能小看。那就是可以用来画曲线的 <code>border-radius</code>。接下来我们先来了解一下相关知识点的基本用法吧。</p>
<h2 data-id="heading-2">border-radius</h2>
<blockquote>
<p><code>border-radius</code> 允许你设置元素的外边框圆角。当使用一个半径时确定一个圆形，当使用两个半径时确定一个椭圆。这个(椭)圆与边框的交集形成圆角效果。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/329bc7093e484ff882bd2d854afa2f6c~tplv-k3u1fbpfcp-zoom-1.image" alt="border-radius-sh.png" loading="lazy" referrerpolicy="no-referrer">
我们开发过程中经常只用一个属性值，例如 <code>border-radius: 10px;</code> 对这个属性了解的同学应该知道，这其实是一个简写，类似 <code>padding: 10px;</code> 他实际上会有**两个维度的半径，一个是水平维度，一个是垂直维度。**他的全写是 <code>border-radius: 10px 10px 10px 10px / 10px 10px 10px 10px;</code> <code>/</code> 前的四个值是以左上角为首顺时针对应的四个角的水平半径，而后是垂直半径。
说了这么多，我们来实操一下，试着画一个哆啦A梦的眼眶。重点关注 <code>border-radius</code>，<code>html</code> 部分基本是 <code>div</code>就不一一展示了。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.eye</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">38px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">136px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">136px</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">100px</span> <span class="hljs-number">60px</span> <span class="hljs-number">100px</span> <span class="hljs-number">70px</span> / <span class="hljs-number">100px</span> <span class="hljs-number">60px</span> <span class="hljs-number">100px</span> <span class="hljs-number">70px</span>;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">2px</span> solid <span class="hljs-number">#7f888f</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#fff</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给四个角分别设置对应的水平和垂直半径，最终效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05be9c834a0b4c81ac7757615f015ae6~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外哆啦A梦的脸比较特殊，我这边用了两个半圆叠加在一起，把多余的部分遮挡，最终呈现出了这样的效果。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'doraemon'</span>></span>
  <span class="hljs-comment"><!-- 脸部 --></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'header'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'face'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.doraemon</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">350px</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.header</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>);
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#5087b8</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">700px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">350px</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">350px</span> <span class="hljs-number">350px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> / <span class="hljs-number">350px</span> <span class="hljs-number">350px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.face</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">600px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">250px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">300px</span> <span class="hljs-number">300px</span> <span class="hljs-number">0</span> / <span class="hljs-number">225px</span> <span class="hljs-number">225px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b9022faa3f94974a19dc3fcfa0ad300~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">rotate()</h2>
<blockquote>
<p><code>rotate()</code>函数定义了一种将元素围绕一个定点（由 <code>transform-origin</code> 属性指定，默认为元素的中心）旋转而不变形的转换。指定的角度定义了旋转的量度。若角度为正，则顺时针方向旋转，否则逆时针方向旋转。旋转180°也被称为点反射。</p>
</blockquote>
<p>顾名思义，就是作一个旋转角度用的，其中还分为 <code>rotateY()</code>、<code>rotateX()</code> 作用是让一个元素围绕纵坐标(垂直轴、水平轴)旋转，而不会对其进行变形。
​</p>
<p>因为哆啦A梦的脸比较对称，就是一个蓝的、圆的、大胖子脸，我们可以通过这个 API 轻而易举的画出另一边眼眶（懒人偷懒的办法多）。同样的，还可以画出他的猫胡子。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'eye eye-left'</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'pupil'</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'pupil-mask'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'pupil-middle'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'pupil-small'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'tear-top'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'tear-bottom'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'eye eye-right mirror'</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'pupil mirror'</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'pupil-mask'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'pupil-middle'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'pupil-small'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'tear-top'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'tear-bottom'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.eye</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">38px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">136px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">136px</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">100px</span> <span class="hljs-number">60px</span> <span class="hljs-number">100px</span> <span class="hljs-number">70px</span> / <span class="hljs-number">100px</span> <span class="hljs-number">60px</span> <span class="hljs-number">100px</span> <span class="hljs-number">70px</span>;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">2px</span> solid <span class="hljs-number">#7f888f</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#fff</span>;
&#125;

<span class="hljs-selector-class">.eye</span><span class="hljs-selector-class">.eye-left</span> &#123;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">104px</span>;
&#125;

<span class="hljs-selector-class">.eye</span><span class="hljs-selector-class">.eye-right</span> &#123;
    <span class="hljs-attribute">right</span>: <span class="hljs-number">104px</span>;
&#125;

<span class="hljs-selector-class">.mirror</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">180deg</span>);     // 水平翻转
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3aba539e508245d8b457d0f2467f240f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">box-shadow</h2>
<blockquote>
<p><code>box-shadow</code>** <strong>属性用于在元素的框架上添加阴影效果。你可以在同一个元素上设置多个阴影效果，并用逗号将他们分隔开。该属性可设置的值包括</strong>阴影的X轴偏移量、Y轴偏移量、模糊半径、扩散半径和颜色**。</p>
</blockquote>
<p>海报上的哆啦A梦的鼻子做出了立体的效果，这时候就该 <code>box-shadow</code> 出场了，其实只要知道对应的值代表什么，问题就迎刃而解了，我们来看下简单的使用例子。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 依次对应的值为 x偏移量 | y偏移量 | 阴影模糊半径 | 阴影扩散半径 | 阴影颜色 */</span>
<span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">2px</span> <span class="hljs-number">2px</span> <span class="hljs-number">2px</span> <span class="hljs-number">1px</span> <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>嗯，看着非常简单，一目了然，接着我们开始画他的鼻子吧。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'nose'</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'blink'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.nose</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">127px</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">80px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">80px</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#ae3537</span>;
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">2px</span> <span class="hljs-number">30px</span> <span class="hljs-number">18px</span> -<span class="hljs-number">8px</span> <span class="hljs-built_in">rgb</span>(<span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> / <span class="hljs-number">33%</span>);
&#125;

<span class="hljs-comment">/* 鼻子上的光 */</span>
<span class="hljs-selector-class">.nose</span> <span class="hljs-selector-class">.blink</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">5px</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">36px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">22px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#bf5d5c</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">80px</span> <span class="hljs-number">30px</span> <span class="hljs-number">44px</span> <span class="hljs-number">20px</span> / <span class="hljs-number">60px</span> <span class="hljs-number">30px</span> <span class="hljs-number">60px</span> <span class="hljs-number">20px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/637b736bd2484516a2b50ff9e4d97abe~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">召唤哆啦A梦</h1>
<p>终于到了最关键的时刻了，把所有的零部件拼接在一起吧。决定就是你了，出来吧，哆啦A梦（串了串了）。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d18efe3fc5d94cbaa88ec74bc9a04e67~tplv-k3u1fbpfcp-zoom-1.image" alt="doraemon.gif" loading="lazy" referrerpolicy="no-referrer">
完整的代码我放在 <a href="https://codepen.io/guyon/pen/poepbxB" target="_blank" rel="nofollow noopener noreferrer">Code Pen</a> 上了，有感兴趣的同学可以看看。</p>
<h1 data-id="heading-6">结束语</h1>
<p>大雄和静香最终在一起了，你为什么还是一个人（我指的是哆啦A梦, 哈哈哈）？现实生活中其实有很多哆啦A梦，疼爱你的家人，帮助你的朋友，开导你的老师，引导你的上司都是我们人生中的哆啦A梦。最后，祝所有人儿童节快乐！</p></div>  
</div>
            