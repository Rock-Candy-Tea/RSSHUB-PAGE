
---
title: 'CSS 动画实现星球环绕效果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67b07d5edd9f4d009a601783885f4610~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 08:16:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67b07d5edd9f4d009a601783885f4610~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好，我是97年的前端小鲜肉绿生，日常对接设计师“奇怪”的想法🤔。今天为大家带来一个实用的前端小技巧。在做某 H5 活动页时，设计师山田出了一个行星环绕运动 🪐 的效果图 ，五颗球需要围绕倾斜的轨道进行旋转运动。JavaScript 可以画很多复杂的动画，各种星球类的实现网上有很多，那么如何用 CSS 实现这个效果呢？</p>
<p>CSS 实现效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67b07d5edd9f4d009a601783885f4610~tplv-k3u1fbpfcp-watermark.image" alt="1616045664764-f8401335-1219-43c2-96e5-35fab4e8011f.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fembed%2Fyong-css-shixianxingqiuhuanraoxiaoguo-m95e2%3Ffontsize%3D14%26hidenavigation%3D1%26theme%3Ddark" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/embed/yong-css-shixianxingqiuhuanraoxiaoguo-m95e2?fontsize=14&hidenavigation=1&theme=dark" ref="nofollow noopener noreferrer">在线 Demo 链接</a></p>
<h2 data-id="heading-0">再认识 CSS Transform</h2>
<p>在开始之前，先回顾一些 CSS Transform 的知识点～</p>
<h3 data-id="heading-1">Transform</h3>
<h4 data-id="heading-2">坐标系</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f3fc87e90464016b8a0dc098ab80685~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>X 轴：屏幕左上角为原点，水平方向为 X 轴</p>
<p>Y 轴：屏幕左上角为原点，垂直方向为 Y 轴</p>
<p>Z 轴：屏幕左上角为原点，垂直电脑的轴为 Z 轴，可以理解为指向我们的轴</p>
<h4 data-id="heading-3">transform 参数的执行顺序</h4>
<p>transform 中传入的效果是有<strong>先后执行顺序</strong>的（效果上看，可以理解为<strong>后传入</strong>的<strong>先执行</strong>，但实际计算是以<strong>矩阵</strong>：<strong>matrix</strong> 的方式去算的），且转换会改变坐标轴。</p>
<p>如下图，skew、scale、rotate... 本质上都是用 matrix 实现的，只不过 rotate 这种形式更容易让人上手。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31728e1e13194d8b9c917824930cc033~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>matrix 方法有两种：<br>
1、matrix()     3x3 矩阵<br>
2、matrix3d() 4x4 矩阵</p>
</blockquote>
<p>举个例子：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">30deg</span>);

// matrix(cos30°,sin30°,-sin30°,cos30°,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>);
<span class="hljs-attribute">transform</span>: <span class="hljs-built_in">matrix</span>(<span class="hljs-number">0.866025</span>,<span class="hljs-number">0.500000</span>,-<span class="hljs-number">0.500000</span>,<span class="hljs-number">0.866025</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两种方式的表现结果是一致的，但如果要用纯 matrix 实现 rotate，你需要手动计算各种 sin，cos 值。</p>
<p>再举两个简单的例子，帮助快速理解 transform 的计算（执行）顺序：</p>
<ol>
<li>先执行 scaleX(0.5) 把正方形变成了长方形，再执行 rotateZ(45deg) 把元素顺时针旋转 45 度，得到的是一个倾斜的长方形：</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.test_transform</span> &#123;
  <span class="hljs-attribute">width</span>:<span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>:<span class="hljs-number">100px</span>;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#c685d9</span>;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">45deg</span>) <span class="hljs-built_in">scaleX</span>(<span class="hljs-number">0.5</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59e0d7632ce9474296246d8dd4fb6c58~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>先执行顺时针旋转 45 度，再压缩 X 轴，得到了一个菱形：</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.test_transform_2</span> &#123;
  ...
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scaleX</span>(<span class="hljs-number">0.5</span>) <span class="hljs-built_in">rotate</span>(<span class="hljs-number">45deg</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6a9bf136db74efabab5cac77bf059b8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">rotate</h3>
<p>简单的旋转，rotate(45deg) 其实就是 rotateZ(45deg)。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9d18e69881b41018a1418442cb166d8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">scale</h3>
<p>缩放，如 scaleY(0.6)</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcd561ac5ff343e79692a9156cbf8201~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>scale() 仅适用于在欧几里德平面（二维平面）上的变换。如果需要进行空间中的缩放，必须使用 scale3D() 。</p>
</blockquote>
<p>下面介绍如何用 CSS 实现一个简单的单球环绕效果：</p>
<h2 data-id="heading-6">实现单球环绕效果</h2>
<h3 data-id="heading-7">Step1 - 基础样式</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c603fb0812a4c6481f1861a54c01007~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><div className=<span class="hljs-string">'wrap'</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'planet'</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'ball'</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.wrap</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">180deg</span>, <span class="hljs-number">#020205</span> <span class="hljs-number">0%</span>, <span class="hljs-number">#170f39</span> <span class="hljs-number">51%</span>, <span class="hljs-number">#35247a</span> <span class="hljs-number">95%</span>);
  <span class="hljs-attribute">width</span>: <span class="hljs-number">600px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">600px</span>;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">justify-content</span>: center;
&#125;

<span class="hljs-selector-class">.planet</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">2px</span> solid <span class="hljs-number">#fff</span>;
  <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
&#125;

<span class="hljs-selector-class">.ball</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">background-color</span>: yellowgreen;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Step2 - 让圆形穿过轨道</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a28c936ed09142ed8ad9025e5c25748f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.ball</span> &#123;
  // ...
  <span class="hljs-attribute">left</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-number">50%</span> - <span class="hljs-number">25px</span>);
  <span class="hljs-attribute">top</span>: -<span class="hljs-number">25px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么需要这一步？假使给这个方形加上 border-radius: 50% 转为一个圆形，目前图中所处的点才是串在圆形轨道上的，正方形四个角的点对应的半径会大于圆形的半径。</p>
<h3 data-id="heading-9">Step3 - 旋转轨道</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77a5aefa280f47ae85f7311bac3f9fd8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.planet</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateZ</span>(<span class="hljs-number">45deg</span>);
&#125;

<span class="hljs-selector-class">.ball</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateZ</span>(-<span class="hljs-number">45deg</span>); // 中和轨道的旋转
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Step4 - 压缩轨道 Y 轴，形成 3D 效果</h3>
<p>注意先后顺序，需要先旋转再压缩，否则会变成一个倾斜的长方形</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c719e3e797dd498db9f3eeebe4562c60~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.planet</span> &#123;
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scaleY</span>(<span class="hljs-number">0.5</span>) <span class="hljs-built_in">rotateZ</span>(<span class="hljs-number">45deg</span>);
&#125;

<span class="hljs-selector-class">.ball</span> &#123;
  // 中和轨道的 scaleY 压缩，<span class="hljs-number">2</span> * <span class="hljs-number">0.5</span> = <span class="hljs-number">1</span> 恢复原状，注意传入顺序，和 <span class="hljs-selector-class">.planet</span> 的 <span class="hljs-attribute">transform</span> 是相反的，就像连续上了几个不同的锁，打开时要用和上锁相反的顺序去解
  <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateZ</span>(-<span class="hljs-number">45deg</span>) <span class="hljs-built_in">scaleY</span>(<span class="hljs-number">2</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">Step5 - 把轨道变成椭圆形</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fe7d67aacaa45b2a39643bec14de98a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.planet</span> &#123;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">Step6 - 让轨道转起来</h3>
<p>上面的步骤已经把原来的图形变成了一个类似轨道和星球的图形了，只要遵循上述关于 rotateZ 和 scaleY 的中和规律，就能让轨道转起来，且保持球体的样式不被压缩：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afc476cdbe1f43c39dab3002464bb93e~tplv-k3u1fbpfcp-watermark.image" alt="1616053387270-7ecf4769-40b5-4cb0-8461-1f79bd99586e.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css">// 公转动画
<span class="hljs-keyword">@keyframes</span> planet-rotate &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">transform</span>:  <span class="hljs-built_in">scaleY</span>(<span class="hljs-number">0.5</span>) <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
  &#125;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>:  <span class="hljs-built_in">scaleY</span>(<span class="hljs-number">0.5</span>) <span class="hljs-built_in">rotate</span>(<span class="hljs-number">360deg</span>);
  &#125;
&#125;

// 自转动画
<span class="hljs-keyword">@keyframes</span> self-rotate &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>) <span class="hljs-built_in">scaleY</span>(<span class="hljs-number">2</span>);
  &#125;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">360deg</span>) <span class="hljs-built_in">scaleY</span>(<span class="hljs-number">2</span>);
  &#125;
&#125;

<span class="hljs-selector-class">.planet</span> &#123;
  <span class="hljs-attribute">animation</span>: planet-rotate <span class="hljs-number">20s</span> linear infinite;
&#125;

<span class="hljs-selector-class">.ball</span> &#123;
  <span class="hljs-attribute">animation</span>: self-rotate <span class="hljs-number">20s</span> linear infinite;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">Step7 - 让轨道产生倾斜角度</h3>
<p>依旧利用 transform 的执行顺序，只要在最后再执行一个 rotate(Z)，就能让整个平面产生倾斜感</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00950a8399744c3e9a95579cf15a60dd~tplv-k3u1fbpfcp-watermark.image" alt="1616053594414-87104715-d988-458a-9918-5fd759f88f42.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@keyframes</span> planet-rotate &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">transform</span>:  <span class="hljs-built_in">rotate</span>(<span class="hljs-number">45deg</span>) <span class="hljs-built_in">scaleY</span>(<span class="hljs-number">0.5</span>) <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
  &#125;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>:  <span class="hljs-built_in">rotate</span>(<span class="hljs-number">45deg</span>) <span class="hljs-built_in">scaleY</span>(<span class="hljs-number">0.5</span>) <span class="hljs-built_in">rotate</span>(<span class="hljs-number">360deg</span>);
  &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> self-rotate &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>) <span class="hljs-built_in">scaleY</span>(<span class="hljs-number">2</span>) <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">45deg</span>);
  &#125;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">360deg</span>) <span class="hljs-built_in">scaleY</span>(<span class="hljs-number">2</span>) <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">45deg</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">实现多球环绕效果</h2>
<p>因为一个轨道容器最多只能保证四个球是在圆形轨道上运动的，如果要实现大于 4 个球的运动，其实只要重叠多个轨道 + 球的平面，但只展示一个轨道（border）即可。</p>
<h3 data-id="heading-15">运动模型</h3>
<p><strong>独立运动个体</strong> = 单球体 + 单球体所在轨道（父元素）<br><strong>多球环绕</strong> = 独立运动个体 * N 重叠在同一位置，并仅展示最底层球体所在轨道，其余轨道隐藏，最后对每个独立运动个体进行初始旋转位置的偏移<br></p>
<h3 data-id="heading-16">实现步骤</h3>
<p>下面以 <strong>5</strong> 个球的场景为例，介绍如何实现多球环绕的效果，为了编写方便使用了 React + Sass：<br></p>
<h4 data-id="heading-17">1. 编写基本 DOM 结构与样式</h4>
<p><strong>Jsx</strong></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 传入数据</span>
<span class="hljs-keyword">const</span> dataSource = [
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'山田'</span>,
  &#125;,
  <span class="hljs-comment">// ...</span>
];

<span class="hljs-comment">// 渲染一个球 + 名字的 DOM</span>
<span class="hljs-keyword">const</span> renderCircleBoxItem = <span class="hljs-function">(<span class="hljs-params">name: string</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.circleBoxItem&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.ball&#125;</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.name&#125;</span>></span>&#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;;

<span class="hljs-comment">// 根据 dataSource 的数量来渲染多个旋转体</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.circleBoxWrap&#125;</span>></span>
  &#123;
    dataSource.map((item, key) => (
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;key&#125;</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.circleBox&#125;</span>></span>&#123;renderCircleBoxItem(item.name)&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    ))
  &#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Sass</strong></p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-comment">// 轨道层 keyframes</span>
<span class="hljs-keyword">@function</span> getPlanetRotate(<span class="hljs-variable">$rotateValue</span>) &#123;
  <span class="hljs-keyword">@return</span> rotate(<span class="hljs-number">45deg</span>) scaleY(<span class="hljs-number">0.5</span>) rotate(#&#123;<span class="hljs-variable">$rotateValue</span>&#125;);
&#125;

<span class="hljs-keyword">@keyframes</span> planet-rotate &#123;
  0% &#123;
    <span class="hljs-attribute">transform</span>: getPlanetRotate(<span class="hljs-number">0deg</span>);
  &#125;
  100% &#123;
    <span class="hljs-attribute">transform</span>: getPlanetRotate(<span class="hljs-number">360deg</span>);
  &#125;
&#125;

<span class="hljs-comment">// 自转球体 keyframes</span>
<span class="hljs-keyword">@function</span> getSelfRotate(<span class="hljs-variable">$rotateValue</span>) &#123;
  <span class="hljs-keyword">@return</span> rotate(#&#123;<span class="hljs-variable">$rotateValue</span>&#125;) scaleY(<span class="hljs-number">2</span>) rotate(-<span class="hljs-number">45deg</span>) scale(<span class="hljs-number">1</span>)) translateX(<span class="hljs-number">50px</span>);
  <span class="hljs-comment">// 这里 translateX 是为了修正球的位置，使之尽量保持在轨道上运动</span>
&#125;

<span class="hljs-keyword">@keyframes</span> self-rotate &#123;
  0% &#123;
    <span class="hljs-attribute">transform</span>: getSelfRotate(<span class="hljs-number">0deg</span>);
  &#125;
  100% &#123;
    <span class="hljs-attribute">transform</span>: getSelfRotate(-<span class="hljs-number">360deg</span>);
  &#125;
&#125;

<span class="hljs-comment">// 轨道元素，内含一个球体</span>
<span class="hljs-selector-class">.circleBox</span> &#123;
  <span class="hljs-comment">// 统一转动速度</span>
  <span class="hljs-variable">$planet-rotate-speed</span>: <span class="hljs-number">30s</span>;
  
  <span class="hljs-comment">// 随便定个轨道大小</span>
  <span class="hljs-attribute">width</span>: <span class="hljs-number">648px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">648px</span>;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
  
  <span class="hljs-comment">// 让轨道呈圆形</span>
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;

  <span class="hljs-comment">// 球体元素（球 + 文字 label）</span>
  <span class="hljs-selector-class">.circleBoxItem</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">flex-direction</span>: row;
    <span class="hljs-attribute">align-items</span>: center;
      
    <span class="hljs-comment">// 位置修正，要让球 + 文字的单元处于父元素（不加 border-radius 时是一个正方形）的一边的中心位置</span>
    <span class="hljs-comment">//，这样才能在形成椭圆轨道时，始终贴合轨道运动</span>
    <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>; <span class="hljs-comment">// 球 + 文字定宽，方便计算位置修正</span>
    <span class="hljs-attribute">top</span>: -<span class="hljs-number">30px</span>; <span class="hljs-comment">// 球的直径是 60px，向上偏移一半</span>
    <span class="hljs-attribute">left</span>: calc(<span class="hljs-number">50%</span> - #&#123;p2r(<span class="hljs-number">100</span>)&#125;); <span class="hljs-comment">// 横向居中</span>
      
    <span class="hljs-selector-class">.ball</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">60px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">60px</span>;
      <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
      <span class="hljs-attribute">overflow</span>: hidden;
      <span class="hljs-attribute">border</span>: <span class="hljs-number">6px</span> solid <span class="hljs-number">#fff</span>;
      <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#6d45ca</span>;
      <span class="hljs-attribute">margin-right</span>: p2r(<span class="hljs-number">20</span>);
    &#125;
  
    <span class="hljs-selector-class">.name</span> &#123;
      <span class="hljs-comment">// 文字相关的样式...</span>
    &#125;
  &#125;

  &<span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">1</span>) &#123;
    <span class="hljs-attribute">border</span>: p2r(<span class="hljs-number">2</span>) solid <span class="hljs-number">#fff</span>;
    
    <span class="hljs-attribute">animation</span>: planet-rotate <span class="hljs-variable">$planet-ratate-speed</span> linear infinite;
    <span class="hljs-selector-class">.circleBoxItem</span> &#123;
      <span class="hljs-attribute">animation</span>: self-rotate <span class="hljs-variable">$planet-ratate-speed</span> linear infinite;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">2. 处理轨道偏移</h4>
<p>为了让球体们产生偏移，需要对每个 <strong>独立运动个体</strong> 的初始旋转位置产生偏移计算，对轨道的 keyframes 进行改写：</p>
<p><strong>Sass</strong></p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-comment">// 使用 css 变量控制步长（即偏移距离）</span>
<span class="hljs-selector-pseudo">:root</span> &#123;
  --planet-rotate-step: <span class="hljs-number">72deg</span>; <span class="hljs-comment">// 72 = 360 / 5</span>
&#125;

<span class="hljs-keyword">@function</span> getPlanetRotate(<span class="hljs-variable">$rotateValue</span>) &#123;
  <span class="hljs-keyword">@return</span> rotate(<span class="hljs-number">45deg</span>) scaleY(<span class="hljs-number">0.5</span>) rotate(#&#123;<span class="hljs-variable">$rotateValue</span>&#125;);
&#125;

<span class="hljs-keyword">@keyframes</span> planet-rotate-<span class="hljs-number">1</span> &#123;
  0% &#123;
    <span class="hljs-attribute">transform</span>: getPlanetRotate(<span class="hljs-number">0deg</span>);
  &#125;
  100% &#123;
    <span class="hljs-attribute">transform</span>: getPlanetRotate(<span class="hljs-number">360deg</span>);
  &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> planet-rotate-<span class="hljs-number">2</span> &#123;
  0% &#123;
    <span class="hljs-attribute">transform</span>: getPlanetRotate(calc(<span class="hljs-number">0deg</span> + var(--planet-rotate-step) * <span class="hljs-number">1</span>));
  &#125;
  100% &#123;
    <span class="hljs-attribute">transform</span>: getPlanetRotate(calc(<span class="hljs-number">360deg</span> + var(--planet-rotate-step) * <span class="hljs-number">1</span>));
  &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> planet-rotate-<span class="hljs-number">3</span> &#123;
  0% &#123;
    <span class="hljs-attribute">transform</span>: getPlanetRotate(calc(<span class="hljs-number">0deg</span> + var(--planet-rotate-step) * <span class="hljs-number">2</span>));
  &#125;
  100% &#123;
    <span class="hljs-attribute">transform</span>: getPlanetRotate(calc(<span class="hljs-number">360deg</span> + var(--planet-rotate-step) * <span class="hljs-number">2</span>));
  &#125;
&#125;

<span class="hljs-comment">// ...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">3. 处理球体运动</h4>
<p>球体需要针对轨道的旋转路径进行位置修正，编写球体的 keyframes：</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-keyword">@function</span> getSelfRotate(<span class="hljs-variable">$rotateValue</span>) &#123;
  <span class="hljs-keyword">@return</span> rotate(#&#123;<span class="hljs-variable">$rotateValue</span>&#125;) scaleY(<span class="hljs-number">2</span>) rotate(-<span class="hljs-number">45deg</span>) scale(<span class="hljs-number">1</span>) translateX(<span class="hljs-number">50px</span>);
&#125;

<span class="hljs-keyword">@keyframes</span> self-rotate-<span class="hljs-number">1</span> &#123;
  0% &#123;
    <span class="hljs-attribute">transform</span>: getSelfRotate(<span class="hljs-number">0deg</span>);
  &#125;
  100% &#123;
    <span class="hljs-attribute">transform</span>: getSelfRotate(-<span class="hljs-number">360deg</span>);
  &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> self-rotate-<span class="hljs-number">2</span> &#123;
  0% &#123;
    <span class="hljs-attribute">transform</span>: getSelfRotate(calc(<span class="hljs-number">0deg</span> - var(--planet-rotate-step) * <span class="hljs-number">1</span>));
  &#125;
  100% &#123;
    <span class="hljs-attribute">transform</span>: getSelfRotate(calc(-<span class="hljs-number">360deg</span> - var(--planet-rotate-step) * <span class="hljs-number">1</span>));
  &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> self-rotate-<span class="hljs-number">3</span> &#123;
  0% &#123;
    <span class="hljs-attribute">transform</span>: getSelfRotate(calc(<span class="hljs-number">0deg</span> - var(--planet-rotate-step) * <span class="hljs-number">2</span>));
  &#125;
  100% &#123;
    <span class="hljs-attribute">transform</span>: getSelfRotate(calc(-<span class="hljs-number">360deg</span> - var(--planet-rotate-step) * <span class="hljs-number">2</span>));
  &#125;
&#125;

<span class="hljs-comment">// ...</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">4. Animations 语句编写</h4>
<p>调整元素的 animation：</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-class">.circleBox</span> &#123;
  &<span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">1</span>) &#123;
    <span class="hljs-comment">// 仅显示第一个轨道</span>
    <span class="hljs-attribute">border</span>: p2r(<span class="hljs-number">2</span>) solid <span class="hljs-number">#fff</span>;

    <span class="hljs-attribute">animation</span>: planet-rotate-<span class="hljs-number">1</span> <span class="hljs-variable">$planet-rotate-speed</span> linear infinite;
    <span class="hljs-selector-class">.circleBoxItem</span> &#123;
      <span class="hljs-attribute">animation</span>: self-rotate-<span class="hljs-number">1</span> <span class="hljs-variable">$planet-rotate-speed</span> linear infinite;
    &#125;
  &#125;

  &<span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>) &#123;
    <span class="hljs-attribute">animation</span>: planet-rotate-<span class="hljs-number">2</span> <span class="hljs-variable">$planet-rotate-speed</span> linear infinite;
    <span class="hljs-selector-class">.circleBoxItem</span> &#123;
      <span class="hljs-attribute">animation</span>: self-rotate-<span class="hljs-number">2</span> <span class="hljs-variable">$planet-rotate-speed</span> linear infinite;
    &#125;
  &#125;

  &<span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>) &#123;
    <span class="hljs-attribute">animation</span>: planet-rotate-<span class="hljs-number">3</span> <span class="hljs-variable">$planet-rotate-speed</span> linear infinite;
    <span class="hljs-selector-class">.circleBoxItem</span> &#123;
      <span class="hljs-attribute">animation</span>: self-rotate-<span class="hljs-number">3</span> <span class="hljs-variable">$planet-rotate-speed</span> linear infinite;
    &#125;
  &#125;
  
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">5. 搭配 CSS 变量自动计算球的间距</h4>
<p>真实场景需要根据传入的数据个数自动处理球的间距（偏移距离），这时可以用 JS 动态计算并修改刚才的 CSS 变量来完美解决：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> number = dataSource.length;
<span class="hljs-keyword">const</span> step = <span class="hljs-number">360</span> / number;

<span class="hljs-built_in">document</span>.documentElement.style.setProperty(<span class="hljs-string">'--planet-rotate-step'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;step&#125;</span>deg`</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67b07d5edd9f4d009a601783885f4610~tplv-k3u1fbpfcp-watermark.image" alt="1616045664764-f8401335-1219-43c2-96e5-35fab4e8011f.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一个星球环绕的 CSS 动画就完成啦，感谢大家观看，我们下期再会～</p>
<hr>
<p>2021年校招（面向2022年毕业的同学们）正式开始啦！联系我们请注明来源掘金，看下图👇 了解更多信息～</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f10fcc2974b64241b37a087f82702d2e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            