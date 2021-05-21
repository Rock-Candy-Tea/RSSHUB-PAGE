
---
title: '学习 canvas （三） 常用的绘图技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1efa88d0fc8049a9aab1fd13514fc2a3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 20 May 2021 05:38:51 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1efa88d0fc8049a9aab1fd13514fc2a3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">图像填充</h1>
<p><code>canvas</code> 除了使用颜色填充形状，也可以通过定义图案来填充形状。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"500"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"500"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvas"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
      <span class="hljs-comment">// 获取元素DOM</span>
      <span class="hljs-keyword">var</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"canvas"</span>);
      <span class="hljs-comment">// 获取画布上下文</span>
      <span class="hljs-keyword">var</span> c = canvas.getContext(<span class="hljs-string">"2d"</span>);

      <span class="hljs-keyword">var</span> img = <span class="hljs-keyword">new</span> Image();
      img.addEventListener(<span class="hljs-string">"load"</span>, loadHandler);
      img.src = <span class="hljs-string">"./1.jpg"</span>;

      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadHandler</span>(<span class="hljs-params">e</span>) </span>&#123;
        <span class="hljs-comment">// createPattern() 在指定的方向上重复元图像</span>
        <span class="hljs-keyword">var</span> pat1 = c.createPattern(img, <span class="hljs-string">"repeat"</span>);
        c.fillStyle = pat1; <span class="hljs-comment">// 设置为背景</span>
        c.fillRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">300</span>, <span class="hljs-number">200</span>);
        <span class="hljs-keyword">var</span> pat2 = c.createPattern(img, <span class="hljs-string">"repeat-y"</span>);
        c.fillStyle = pat2;
        c.translate(<span class="hljs-number">0</span>, <span class="hljs-number">210</span>); <span class="hljs-comment">// 位移</span>
        c.fillRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">300</span>, <span class="hljs-number">200</span>);
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1efa88d0fc8049a9aab1fd13514fc2a3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>与渐变一样，都是相对于当前坐标系绘制图案。</li>
<li>根据<code>createPattern()</code>绘制图像。函数的第二个参数，设置图片重复方向。</li>
<li><code>translate(0, 210)</code> 将新的 (0,0) 位置设置为 (0,70)。再次绘制新的矩形。</li>
</ol>
<h1 data-id="heading-1">绘制组合图形 - 太极图</h1>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"500"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"500"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvas"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
      <span class="hljs-comment">// 获取元素DOM</span>
      <span class="hljs-keyword">var</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"canvas"</span>);
      <span class="hljs-comment">// 获取画布上下文</span>
      <span class="hljs-keyword">var</span> ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);

      ctx.fillStyle = <span class="hljs-string">"#00ff00"</span>;
      <span class="hljs-comment">// fillRect() 绘制有填充颜色的矩形</span>
      ctx.fillRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">500</span>, <span class="hljs-number">500</span>);

      <span class="hljs-comment">// 线</span>
      ctx.lineWidth = <span class="hljs-number">1</span>;

      <span class="hljs-comment">// 绘制 白色半圆</span>
      ctx.beginPath();
      ctx.fillStyle = <span class="hljs-string">"#fff"</span>;
      ctx.arc(<span class="hljs-number">250</span>, <span class="hljs-number">250</span>, <span class="hljs-number">100</span>, getRads(-<span class="hljs-number">90</span>), getRads(<span class="hljs-number">90</span>), <span class="hljs-literal">false</span>);
      ctx.fill();

      <span class="hljs-comment">// 绘制 黑色半圆</span>
      ctx.beginPath();
      ctx.fillStyle = <span class="hljs-string">"#000"</span>;
      ctx.arc(<span class="hljs-number">250</span>, <span class="hljs-number">250</span>, <span class="hljs-number">100</span>, getRads(<span class="hljs-number">90</span>), getRads(-<span class="hljs-number">90</span>), <span class="hljs-literal">false</span>);
      ctx.fill();

      <span class="hljs-comment">// 修改 绘制原点 绘制小球</span>
      <span class="hljs-comment">// 绘制 白色小圆</span>
      ctx.beginPath();
      ctx.fillStyle = <span class="hljs-string">"#fff"</span>;
      ctx.arc(<span class="hljs-number">250</span>, <span class="hljs-number">200</span>, <span class="hljs-number">50</span>, getRads(-<span class="hljs-number">90</span>), getRads(<span class="hljs-number">90</span>), <span class="hljs-literal">true</span>);
      ctx.fill();

      <span class="hljs-comment">// 绘制 黑色小圆</span>
      ctx.beginPath();
      ctx.fillStyle = <span class="hljs-string">"#000"</span>;
      ctx.arc(<span class="hljs-number">250</span>, <span class="hljs-number">300</span>, <span class="hljs-number">50</span>, getRads(-<span class="hljs-number">90</span>), getRads(<span class="hljs-number">90</span>), <span class="hljs-literal">false</span>);
      ctx.fill();

      <span class="hljs-comment">// 绘制 小黑点</span>
      ctx.beginPath();
      ctx.fillStyle = <span class="hljs-string">"#000"</span>;
      ctx.arc(<span class="hljs-number">250</span>, <span class="hljs-number">200</span>, <span class="hljs-number">10</span>, getRads(<span class="hljs-number">0</span>), getRads(<span class="hljs-number">360</span>), <span class="hljs-literal">false</span>);
      ctx.fill();

      <span class="hljs-comment">// 绘制 小白点</span>
      ctx.beginPath();
      ctx.fillStyle = <span class="hljs-string">"#fff"</span>;
      ctx.arc(<span class="hljs-number">250</span>, <span class="hljs-number">300</span>, <span class="hljs-number">10</span>, getRads(<span class="hljs-number">0</span>), getRads(<span class="hljs-number">360</span>), <span class="hljs-literal">false</span>);
      ctx.fill();

      <span class="hljs-comment">// 度 转换 弧度</span>
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRads</span>(<span class="hljs-params">degrees</span>) </span>&#123;
        <span class="hljs-keyword">return</span> (<span class="hljs-built_in">Math</span>.PI * degrees) / <span class="hljs-number">180</span>;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8e7a37f07de40619aabe11641d6a34b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li><code>(Math.PI * degrees) / 180</code> 弧度计算公式。</li>
<li><code>arc()</code> 绘制弧形图形。根据修改绘图位置，组合计算好的图形，形成一个新的图形。</li>
</ol>
<h1 data-id="heading-2">Transforms 修改绘制原点</h1>
<p>与许多2D API一样，<code>Canvas</code> 支持标准的平移，旋转和缩放转换。这使您可以在屏幕上绘制变换后的形状，而无需手动计算新点。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"500"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"500"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvas"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
      <span class="hljs-comment">// 获取元素DOM</span>
      <span class="hljs-keyword">var</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"canvas"</span>);
      <span class="hljs-comment">// 获取画布上下文</span>
      <span class="hljs-keyword">var</span> ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);

      <span class="hljs-keyword">var</span> data = [<span class="hljs-number">10</span>, <span class="hljs-number">60</span>, <span class="hljs-number">40</span>, <span class="hljs-number">50</span>];
      ctx.fillStyle = <span class="hljs-string">"black"</span>;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < data.length; i++) &#123;
        <span class="hljs-keyword">var</span> dp = data[i];
        ctx.translate(<span class="hljs-number">100</span>, <span class="hljs-number">0</span>);

        <span class="hljs-keyword">if</span> (i === <span class="hljs-number">2</span>) &#123;
          <span class="hljs-keyword">var</span> rads = (<span class="hljs-number">30</span> * <span class="hljs-built_in">Math</span>.PI * <span class="hljs-number">2.0</span>) / <span class="hljs-number">360.0</span>;
          ctx.rotate(rads);
        &#125;

        ctx.fillRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">50</span>, dp);
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87256e1f9fed40f896469d14d9c334c5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改绘制点后，下一次的绘制会继续在上一次的位置改变。不做特殊操作是永久性的。当然，随着时间的流逝，这可能会造成混乱。您可以像这样撤消转换：</p>
<pre><code class="hljs language-html copyable" lang="html">for (var i = 0; i < data.length; i++) &#123;
    ctx.save();
    var dp = data[i];
    ctx.translate(100, 0);
    if (i === 2) &#123;
      var rads = (30 * Math.PI * 2.0) / 360.0;
      ctx.rotate(rads);
    &#125;
    ctx.fillRect(0, 0, 50, dp);
    ctx.restore();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li><code>.save()</code> 保存上一次的修改位置。</li>
<li><code>.restore()</code> 恢复为之前的位置。</li>
</ol>
<h1 data-id="heading-3">不透明度</h1>
<p>通过Canvas API，使用<code>globalAlpha</code>属性控制任何绘图功能的不透明度。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
      <span class="hljs-comment">// 获取元素DOM</span>
      <span class="hljs-keyword">var</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"canvas"</span>);
      <span class="hljs-comment">// 获取画布上下文</span>
      <span class="hljs-keyword">var</span> ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);

      ctx.fillStyle = <span class="hljs-string">"red"</span>;
      ctx.fillRect(<span class="hljs-number">20</span>, <span class="hljs-number">20</span>, <span class="hljs-number">75</span>, <span class="hljs-number">50</span>);
      <span class="hljs-comment">// 调节透明度</span>
      ctx.globalAlpha = <span class="hljs-number">0.3</span>;
      ctx.fillStyle = <span class="hljs-string">"blue"</span>;
      ctx.fillRect(<span class="hljs-number">50</span>, <span class="hljs-number">50</span>, <span class="hljs-number">75</span>, <span class="hljs-number">50</span>);
      ctx.fillStyle = <span class="hljs-string">"green"</span>;
      ctx.fillRect(<span class="hljs-number">80</span>, <span class="hljs-number">80</span>, <span class="hljs-number">75</span>, <span class="hljs-number">50</span>);
      ctx.globalAlpha = <span class="hljs-number">1</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>此不透明度设置适用于所有绘图操作。</li>
<li>绘制完成后需要注意设置回来，以免影响后续操作。</li>
</ol>
<h1 data-id="heading-4">三次贝塞尔曲线</h1>
<p>示意图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5e5c2b7c467442f992116b54c985dfe~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用三次贝塞尔曲线，绘制线条时形成曲线的过程。</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
      <span class="hljs-comment">// 获取元素DOM</span>
      <span class="hljs-keyword">var</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"canvas"</span>);
      <span class="hljs-comment">// 获取画布上下文</span>
      <span class="hljs-keyword">var</span> ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);

      ctx.lineWidth = <span class="hljs-number">1</span>;

      ctx.beginPath();
      ctx.moveTo(<span class="hljs-number">75</span>, <span class="hljs-number">40</span>);
      ctx.bezierCurveTo(<span class="hljs-number">75</span>, <span class="hljs-number">38</span>, <span class="hljs-number">71</span>, <span class="hljs-number">26</span>, <span class="hljs-number">50</span>, <span class="hljs-number">26</span>);
      ctx.bezierCurveTo(<span class="hljs-number">20</span>, <span class="hljs-number">25</span>, <span class="hljs-number">20</span>, <span class="hljs-number">62.5</span>, <span class="hljs-number">21</span>, <span class="hljs-number">63</span>);
      ctx.bezierCurveTo(<span class="hljs-number">20</span>, <span class="hljs-number">80</span>, <span class="hljs-number">40</span>, <span class="hljs-number">102</span>, <span class="hljs-number">75</span>, <span class="hljs-number">120</span>);
      ctx.bezierCurveTo(<span class="hljs-number">110</span>, <span class="hljs-number">102</span>, <span class="hljs-number">130</span>, <span class="hljs-number">80</span>, <span class="hljs-number">130</span>, <span class="hljs-number">62.5</span>);
      ctx.bezierCurveTo(<span class="hljs-number">130</span>, <span class="hljs-number">62.5</span>, <span class="hljs-number">130</span>, <span class="hljs-number">25</span>, <span class="hljs-number">100</span>, <span class="hljs-number">26</span>);
      ctx.bezierCurveTo(<span class="hljs-number">85</span>, <span class="hljs-number">25</span>, <span class="hljs-number">75</span>, <span class="hljs-number">37</span>, <span class="hljs-number">75</span>, <span class="hljs-number">40</span>);
      ctx.stroke();
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb056a7ad90047e9ac6d76c0a01831d7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li><code>bezierCurveTo()</code> 绘制一条三次贝塞尔曲线，三次贝塞尔曲线需要三个点。前两个点是用于三次贝塞尔计算中的控制点，第三个点是曲线的结束点。曲线的开始点是当前路径中最后一个点。</li>
</ol>
<h1 data-id="heading-5">剪裁</h1>
<p><strong>剪切区域</strong>。它是Canvas之中由路径所定义的一块区域，这意味着任何绘图都只会在剪辑内部进行。简单来说就是根据<code>clip()</code>函数之前路径定义的图形来进行控制。</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
      <span class="hljs-comment">// 获取元素DOM</span>
      <span class="hljs-keyword">var</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"canvas"</span>);
      <span class="hljs-comment">// 获取画布上下文</span>
      <span class="hljs-keyword">var</span> ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);

      <span class="hljs-comment">// 绘制矩形</span>
      ctx.fillStyle = <span class="hljs-string">"red"</span>;
      ctx.fillRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">400</span>, <span class="hljs-number">100</span>);

      <span class="hljs-comment">// 创建三角形路径</span>
      ctx.beginPath();
      ctx.moveTo(<span class="hljs-number">200</span>, <span class="hljs-number">50</span>);
      ctx.lineTo(<span class="hljs-number">250</span>, <span class="hljs-number">150</span>);
      ctx.lineTo(<span class="hljs-number">150</span>, <span class="hljs-number">150</span>);
      ctx.closePath();

      <span class="hljs-comment">// 使用三角形作为剪辑</span>
      ctx.clip();

      ctx.fillStyle = <span class="hljs-string">"yellow"</span>;
      ctx.fillRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">400</span>, <span class="hljs-number">120</span>);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3cd2f9e83fd4ce2984d6b66b363bde9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://www.cnblogs.com/fangsmile/p/10180344.html" target="_blank" rel="nofollow noopener noreferrer">Canvas中的剪切clip()方法</a></p></div>  
</div>
            