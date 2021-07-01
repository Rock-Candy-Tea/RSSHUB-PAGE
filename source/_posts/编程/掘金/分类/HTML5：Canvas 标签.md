
---
title: 'HTML5：Canvas 标签'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8db3406a60634d429b8105258f6a5e57~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 06:30:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8db3406a60634d429b8105258f6a5e57~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>什么是 canvas？
H5 <code><canvas></code> 元素用于图形的绘制，通过脚本 (通常是JavaScript)来完成。<code><canvas></code> 标签只是图形容器，必须使用脚本来绘制图形。</p>
<blockquote>
<p><strong>创建一个画布（Canvas）</strong></p>
</blockquote>
<p>一个画布在网页中是一个矩形框，通过 <code><canvas></code> 元素来绘制。默认情况下 <code><canvas></code> 元素没有边框和内容。</p>
<p>例：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"myCanvas"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>标签通常需要指定一个 id 属性 (脚本中经常引用)</li>
<li>width 和 height 属性定义的画布的大小</li>
</ul>
<p><strong>使用 style 属性来添加边框</strong>:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"myCanvas"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"border:1px solid #000000;"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>使用 JavaScript 来绘制图像</strong></p>
</blockquote>
<p>canvas 元素本身是没有绘图能力的。所有的绘制工作必须在 JavaScript 内部完成：
示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> c=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myCanvas"</span>);
<span class="hljs-keyword">var</span> ctx=c.getContext(<span class="hljs-string">"2d"</span>);
ctx.fillStyle=<span class="hljs-string">"#FF0000"</span>;
ctx.fillRect(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">150</span>,<span class="hljs-number">75</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>Canvas 坐标</strong></p>
</blockquote>
<ul>
<li>canvas 是一个二维网格</li>
<li>canvas 的左上角坐标为 (0,0)</li>
<li>上面的 fillRect 方法拥有参数 (0,0,150,75)。</li>
</ul>
<p>示例：
如下图所示，画布的 X 和 Y 坐标用于在画布上对绘画进行定位。鼠标移动的矩形框上，显示定位坐标。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8db3406a60634d429b8105258f6a5e57~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>Canvas 路径</strong></p>
</blockquote>

























































<table><thead><tr><th>方法</th><th>描述</th></tr></thead><tbody><tr><td>fill()</td><td>填充当前绘图（路径）</td></tr><tr><td>stroke()</td><td>绘制已定义的路径</td></tr><tr><td>beginPath()</td><td>起始一条路径，或重置当前路径</td></tr><tr><td>moveTo()</td><td>把路径移动到画布中的指定点，不创建线条</td></tr><tr><td>closePath()</td><td>创建从当前点回到起始点的路径</td></tr><tr><td>lineTo()</td><td>添加一个新点，然后在画布中创建从该点到最后指定点的线条</td></tr><tr><td>clip()</td><td>从原始画布剪切任意形状和尺寸的区域</td></tr><tr><td>quadraticCurveTo()</td><td>创建二次贝塞尔曲线</td></tr><tr><td>bezierCurveTo()</td><td>创建三次方贝塞尔曲线</td></tr><tr><td>arc()</td><td>创建弧/曲线（用于创建圆形或部分圆）</td></tr><tr><td>arcTo()</td><td>创建两切线之间的弧/曲线</td></tr><tr><td>isPointInPath()</td><td>如果指定的点位于当前路径中，则返回 true，否则返回 false</td></tr></tbody></table>
<p>示例：
定义开始坐标(0,0), 和结束坐标 (200,100)。然后使用 stroke() 方法来绘制线条:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> c=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myCanvas"</span>);
<span class="hljs-keyword">var</span> ctx=c.getContext(<span class="hljs-string">"2d"</span>);
ctx.moveTo(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>);
ctx.lineTo(<span class="hljs-number">200</span>,<span class="hljs-number">100</span>);
ctx.stroke();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在 canvas 中绘制圆形</strong></p>
<pre><code class="copyable">arc(x,y,r,start,stop)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：
使用 arc() 方法 绘制一个圆:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> c=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myCanvas"</span>);
<span class="hljs-keyword">var</span> ctx=c.getContext(<span class="hljs-string">"2d"</span>);
ctx.beginPath();
ctx.arc(<span class="hljs-number">95</span>,<span class="hljs-number">50</span>,<span class="hljs-number">40</span>,<span class="hljs-number">0</span>,<span class="hljs-number">2</span>*<span class="hljs-built_in">Math</span>.PI);
ctx.stroke();
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>Canvas 文本</strong></p>
</blockquote>





















<table><thead><tr><th>属性</th><th>描述</th></tr></thead><tbody><tr><td>font</td><td>定义字体</td></tr><tr><td>fillText(text,x,y)</td><td>在 canvas 上绘制实心的文本</td></tr><tr><td>strokeText(text,x,y)</td><td>在 canvas 上绘制空心的文本</td></tr></tbody></table>
<p>示例1：
使用 "Arial" 字体在画布上绘制一个高 30px 的文字（实心）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> c=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myCanvas"</span>);
<span class="hljs-keyword">var</span> ctx=c.getContext(<span class="hljs-string">"2d"</span>);
ctx.font=<span class="hljs-string">"30px Arial"</span>;
ctx.fillText(<span class="hljs-string">"Hello World"</span>,<span class="hljs-number">10</span>,<span class="hljs-number">50</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例2：
使用 "Arial" 字体在画布上绘制一个高 30px 的文字（空心）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> c=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myCanvas"</span>);
<span class="hljs-keyword">var</span> ctx=c.getContext(<span class="hljs-string">"2d"</span>);
ctx.font=<span class="hljs-string">"30px Arial"</span>;
ctx.strokeText(<span class="hljs-string">"Hello World"</span>,<span class="hljs-number">10</span>,<span class="hljs-number">50</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>Canvas  渐变</strong></p>
</blockquote>
<p>渐变可以填充在矩形, 圆形, 线条, 文本等等, 各种形状可以自己定义不同的颜色。</p>

























<table><thead><tr><th>方法</th><th>描述</th></tr></thead><tbody><tr><td>createLinearGradient()</td><td>创建线性渐变</td></tr><tr><td>createRadialGradient()</td><td>创建放射状/环形的渐变</td></tr><tr><td>createPattern()</td><td>在指定的方向上重复指定的元素</td></tr><tr><td>addColorStop()</td><td>规定渐变对象中的颜色和停止位置</td></tr></tbody></table>
<p>示例1:
创建一个线性渐变。使用渐变填充矩形:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> c=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myCanvas"</span>);
<span class="hljs-keyword">var</span> ctx=c.getContext(<span class="hljs-string">"2d"</span>);
 
<span class="hljs-comment">// 创建渐变</span>
<span class="hljs-keyword">var</span> grd=ctx.createLinearGradient(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">200</span>,<span class="hljs-number">0</span>);
grd.addColorStop(<span class="hljs-number">0</span>,<span class="hljs-string">"red"</span>);
grd.addColorStop(<span class="hljs-number">1</span>,<span class="hljs-string">"white"</span>);
 
<span class="hljs-comment">// 填充渐变</span>
ctx.fillStyle=grd;
ctx.fillRect(<span class="hljs-number">10</span>,<span class="hljs-number">10</span>,<span class="hljs-number">150</span>,<span class="hljs-number">80</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例2:
创建一个径向/圆渐变。使用渐变填充矩形：</p>
<pre><code class="copyable">var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
 
// 创建渐变
var grd=ctx.createRadialGradient(75,50,5,90,60,100);
grd.addColorStop(0,"red");
grd.addColorStop(1,"white");
 
// 填充渐变
ctx.fillStyle=grd;
ctx.fillRect(10,10,150,80);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            