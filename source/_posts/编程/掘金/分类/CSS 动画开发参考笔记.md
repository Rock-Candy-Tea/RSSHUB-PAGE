
---
title: 'CSS 动画开发参考笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://user-gold-cdn.xitu.io/2019/7/25/16c278758a151f14?imageView2/2/w/1956/q/85/interlace/1'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 04:37:27 GMT
thumbnail: 'https://user-gold-cdn.xitu.io/2019/7/25/16c278758a151f14?imageView2/2/w/1956/q/85/interlace/1'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">CSS 动画开发参考笔记</h1>
<h2 data-id="heading-1">过渡 transition</h2>
<p><strong>过渡可以为一个元素在不同状态之间切换的时候定义不同的过渡效果</strong>。比如在不同的伪元素之间切换，像是 :hover，:active 或者通过 JavaScript 实现的状态变化。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">transition</span>: property duration timing-function delay;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">transition 常用属性</h3>






























<table><thead><tr><th>属性</th><th>意义</th><th>值</th></tr></thead><tbody><tr><td>transition-property</td><td>规定设置过渡效果的 CSS 属性的名称</td><td><code><property></code></td></tr><tr><td>transition-duration</td><td>规定完成过渡效果需要多少秒或毫秒</td><td><code><time></code></td></tr><tr><td>transition-timing-function</td><td>规定速度效果的速度曲线</td><td><code><timing-function></code></td></tr><tr><td>transition-delay</td><td>定义过渡效果何时开始</td><td><code><time></code></td></tr></tbody></table>
<h3 data-id="heading-3">css 速度曲线</h3>













































<table><thead><tr><th>选项</th><th>意义</th></tr></thead><tbody><tr><td>cubic-bezier(x1, y1, x2, y2)</td><td>定义了一条连续的立方贝塞尔曲线，也被称为缓动函数</td></tr><tr><td>steps(steps, direction)</td><td>等距步骤划分输出值域的步进函数</td></tr><tr><td>ease</td><td>cubic-bezier(0.25, 0.1, 0.25, 1.0)，开始加速，中段减速</td></tr><tr><td>ease-in</td><td>cubic-bezier(0.42, 0.0, 1.0, 1.0)，开始缓慢，中段逐渐上升</td></tr><tr><td>ease-out</td><td>cubic-bezier(0.0, 0.0, 0.58, 1.0)，开始快速,在接近结束减速</td></tr><tr><td>ease-in-out</td><td>cubic-bezier(0.42, 0.0, 0.58, 1.0)，开始结束缓慢，中段加速</td></tr><tr><td>linear</td><td>cubic-bezier(0.0, 0.0, 1.0, 1.0)，以恒定速度前进</td></tr><tr><td>step-start</td><td>steps(1, start)，动画立即跳转到结束状态并保持在该位置直到动画结束。</td></tr><tr><td>step-end</td><td>steps(1, end)，动画将保持其初始状态，直到结束，直接跳转到其最终位置。</td></tr></tbody></table>
<h2 data-id="heading-4">动画 animation</h2>
<p>animation 属性用来指定一组或多组动画，每组之间用逗号相隔。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">animation</span>: name duration timing-function 
delay iteration-count direction play-state fill-mode;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">animation 常用属性</h3>


















































<table><thead><tr><th>属性</th><th>意义</th><th>值</th></tr></thead><tbody><tr><td>animation-name</td><td>用来调用@keyframes定义好的动画</td><td><code><keyframes-name></code></td></tr><tr><td>animation-duration</td><td>指定元素播放动画所持续的时间</td><td><code><time></code></td></tr><tr><td>animation-timing-function</td><td>规定速度效果的速度曲线</td><td><code><timing-function></code></td></tr><tr><td>animation-delay</td><td>定义在浏览器开始执行动画之前等待的时间</td><td><code><time></code></td></tr><tr><td>animation-iteration-count</td><td>定义动画的播放次数</td><td>`infinite</td></tr><tr><td>animation-direction</td><td>定义动画的播放次数</td><td>`normal</td></tr><tr><td>animation-play-state</td><td>控制元素动画的播放状态</td><td>`running</td></tr><tr><td>animation-fill-mode</td><td>控制动画结束后的样式</td><td>`none</td></tr></tbody></table>
<h3 data-id="heading-6">keyframes</h3>
<p>@keyframes 通过沿动画序列定义关键帧（或路标点）的样式来控制CSS动画序列中的中间步骤。与transition相比，可以更好地控制动画序列的中间步骤。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*语法规范*/</span>
<span class="hljs-keyword">@keyframes</span> slidein &#123;
  <span class="hljs-selector-tag">from</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300%</span>;
  &#125;
  <span class="hljs-selector-tag">to</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  &#125;
&#125;
<span class="hljs-keyword">@keyframes</span> slidein &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300%</span>;
  &#125;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">transform 变形</h2>
<p>transform属性允许你旋转，缩放，倾斜或平移给定元素。</p>
<h3 data-id="heading-8">3d坐标轴</h3>
<p>z轴垂直电脑屏幕指向你，y轴在电脑屏幕垂直👇，x轴在电脑屏幕水平👉。</p>
<p><img src="https://user-gold-cdn.xitu.io/2019/7/25/16c278758a151f14?imageView2/2/w/1956/q/85/interlace/1" alt="3d坐标轴" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">transform 常用属性</h3>


































































































































<table><thead><tr><th>属性</th><th>意义</th><th>值</th></tr></thead><tbody><tr><td>perspective</td><td>视角可以设置在父元素跟子元素上应用，应用效果不一样</td><td><code><length></code></td></tr><tr><td>backface-visibility</td><td>是否透视</td><td>`visible</td></tr><tr><td>perspective-origin</td><td>指定观察者的位置，用作 perspective 属性的消失点</td><td>`</td></tr><tr><td>transform-style</td><td>变形效果</td><td>`flat(水平)</td></tr><tr><td>translateX(x)</td><td>沿着 X 轴旋转 x</td><td>`</td></tr><tr><td>translateY(y)</td><td>沿着 Y 轴旋转 y</td><td>`</td></tr><tr><td>translateZ(z)</td><td>沿着 Z 轴旋转 z</td><td><code><length></code></td></tr><tr><td>translate(tx, ty)</td><td>移动元素在平面上的位置</td><td>`</td></tr><tr><td>translate3d(tx, ty, tz)</td><td>移动元素在3D空间中的位置</td><td>`</td></tr><tr><td>scaleX(x)</td><td>沿着 X 轴上缩放 x</td><td><code><number></code></td></tr><tr><td>scaleY(y)</td><td>沿着 Y 轴上缩放 y</td><td><code><number></code></td></tr><tr><td>scaleZ(z)</td><td>沿着 Z 轴上缩放 z</td><td><code><number></code></td></tr><tr><td>scale(sx, sy)</td><td>改变元素的大小,增大或减小元素的大小，并且缩放量由矢量定义</td><td><code><number></code></td></tr><tr><td>scale3d(sx, sy, sz)</td><td>改变元素的3D空间大小</td><td><code><number></code></td></tr><tr><td>rotateX(a)</td><td>围绕 X 轴旋转 a</td><td><code><angle></code></td></tr><tr><td>rotateY(a)</td><td>围绕 Y 轴旋转 a</td><td><code><angle></code></td></tr><tr><td>rotateZ(a)</td><td>围绕 Z 轴旋转 a</td><td><code><angle></code></td></tr><tr><td>rotate(a)</td><td>旋转 a</td><td><code><angle></code></td></tr><tr><td>rotate3d(x, y, z, a)</td><td>旋转元素在3D空间中的位置</td><td><code>x,y,z:<number>, a:<angle></code></td></tr><tr><td>skewX(a)</td><td>沿着 X 轴扭曲 a 角度</td><td><code><angle></code></td></tr><tr><td>skewY(a)</td><td>沿着 Y 轴扭曲 a 角度</td><td><code><angle></code></td></tr><tr><td>skew(xa, ya)</td><td>每个方向上元素上的每个点以一定角度扭曲</td><td><code><angle></code></td></tr><tr><td>matrix(a,b,c,d,e,f)</td><td>根据矩阵参数对元素进行变换</td><td><code><number> a,b,c,d: 线性变换, e,f:变换的量</code></td></tr><tr><td>matrix3d(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3, a4, b4, c4, d4)</td><td>根据矩阵参数对元素进行3D变换</td><td><code><number> a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3,d4:线性变换, a4,b4c4:变换的量</code></td></tr></tbody></table>
<pre><code class="hljs language-text copyable" lang="text">矩阵计算
[a, c, e]   [x]   [ax + by + e]
[b, d, f] * [y] = [cx + dy + f]
[0, 0, 1]   [1]   [ 0 +  0 + 1]
matrix(0, 0, 0, 0, tx, ty) = translate(tx, ty)
matrix(sx, 0, 0, sy, 0, 0) = scale(sx, sy)
matrix(cosθ,sinθ,-sinθ,cosθ,0,0) = rotate(θ)
matrix(1,tan(θy),tan(θx),1,0,0) = skew(θ, θ)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">transform 坑点</h3>
<ol>
<li>会隐性改变层叠上下文</li>
<li>父元素设置 transform 限制 子元素 position:fixed 直接降级变成 position:absolute</li>
<li>transform 改变 overflow 对 absolute 元素的限制</li>
<li>transform 限制 absolute 的 100% 宽度大小</li>
</ol>
<h2 data-id="heading-11">一些常用的改变时会触发回流(重布局)的属性</h2>
<h3 data-id="heading-12">盒子模型相关属性</h3>
<ul>
<li>width, height, padding, margin, display,</li>
<li>border-width, border, min-height, max-height, min-width, max-width</li>
</ul>
<h3 data-id="heading-13">定位属性及浮动</h3>
<ul>
<li>top ,bottom ,left ,right ,position ,float ,clear</li>
</ul>
<h3 data-id="heading-14">改变节点内部文字结构</h3>
<ul>
<li>text-align, overflow-y, font-weight, overflow,</li>
<li>font-family, line-height, vertival-align, white-space, font-size</li>
</ul>
<h2 data-id="heading-15">修改时只触发重绘的属性</h2>
<ul>
<li>color, border-style, border-radius, visibility, text-decoration,</li>
<li>background, background-image, background-position, background-repeat,</li>
<li>background-size, outline-color, outline, outline-style, outline-width, box-shadow</li>
</ul>
<h3 data-id="heading-16">建议使用属性</h3>
<ul>
<li>opacity</li>
<li>transform</li>
<li>translate</li>
<li>rotate</li>
<li>scale</li>
</ul></div>  
</div>
            