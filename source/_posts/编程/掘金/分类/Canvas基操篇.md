
---
title: 'Canvas基操篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e1906459b494b658ba24406200fbde9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 06:29:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e1906459b494b658ba24406200fbde9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第28天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">👝1.初级阶段——师傅领进门~</h1>
<h2 data-id="heading-1">🎣（1）canvas是什么？</h2>
<blockquote>
我们翻译一下这个单词，会发现它有「 画布 」的意思。
画布画布不就是绘制图形的么？不过不同的是canvas元素是在网页上绘制图形！
<p> </p>
<p>  其实canvas 元素就是使用 JavaScript 在网页上绘制图像。而绘制的画布区域是一个矩形区域，我们可以控制其中每一像素，以达到想画啥就画啥的效果。canvas 拥有多种绘制路径、矩形、圆形、字符以及添加图像的方法。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e1906459b494b658ba24406200fbde9~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<h2 data-id="heading-2">🍶（2）如何使用？</h2>
<blockquote>
<p>上面说canvas 元素就是使用 JavaScript 在网页上绘制图像！所以关于canvas的使用也分为两步：
 </p>
<h2 data-id="heading-3">  第一步：在HTML5页面创建canvas元素；</h2>
<h2 data-id="heading-4">  第二步：通过JavaScript来绘制。</h2>
</blockquote>
<h3 data-id="heading-5">1️⃣创建 Canvas 元素：</h3>
<blockquote>
<p>向 HTML5 页面添加 canvas 元素!</p>
</blockquote>
<p>规定此canvas元素的 id、宽度和高度（宽度和高度即指定画布的大小！）：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--canvas默认大小：宽300px，高150px--></span>
<span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"myCanvas"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2️⃣通过 JavaScript 来绘制：</h3>
<blockquote>
<p>canvas 元素本身是没有绘图能力的。所有的绘制工作必须在 JavaScript 内完成：</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
<span class="hljs-comment">//第一步，匹配到canvas对象。</span>
<span class="hljs-keyword">var</span> c=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myCanvas"</span>);
<span class="hljs-comment">//第二步，获取canvas的上下文环境 </span>
<span class="hljs-keyword">var</span> cxt=c.getContext(<span class="hljs-string">"2d"</span>);    <span class="hljs-comment">//getContext("2d") 对象是内建的 HTML5 对象，拥有多种绘制路径、矩形、圆形、字符以及添加图像的方法。</span>

<span class="hljs-comment">// 绘制一个红色的矩形：</span>
cxt.fillStyle=<span class="hljs-string">"red"</span>;
<span class="hljs-comment">// fillRect方法是绘制矩形    参数：绘制矩形的左上角x坐标，y坐标，x方向长度，y方向长度</span>
cxt.fillRect(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">150</span>,<span class="hljs-number">75</span>);<span class="hljs-comment">// 在画布上绘制 150x75 的矩形，从左上角开始 (0,0)。</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">3️⃣实现效果：</h3>
<blockquote>
<p>需要注意的是：canvas的画布区域，左上角为坐标原点(0,0)，分别向右为x轴，向下为y轴。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd7189c0a34b42b3be490daf813bf9e8~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-8">🚧2.中级阶段——绘制一些常见的基本图形~</h1>
<ul>
<li>要知道，再复杂的图形也都是由各种基本图形组合而成。</li>
<li>所以，先来看看如何绘制各种常见的基本图形。</li>
<li>这样，进行一些需要使用canvas的项目设计时才会手到擒来！</li>
</ul>
<h2 data-id="heading-9">🚓（1）绘制一条直线</h2>
<blockquote>
<ol>
<li>指定起始(x,y)坐标；</li>
<li>指定粗细；</li>
<li>指定颜色。</li>
</ol>
<p> </p>
<p>注意：通过CSS定位到canvas元素，并为其设置一个显眼的border样式，方便下面观察！</p>
</blockquote>
<h3 data-id="heading-10">1️⃣上代码：</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
  <span class="hljs-comment">/*设置canvas画布样式——画布边框粗细1px；实线；红色*/</span>
<span class="hljs-selector-id">#myCanvas</span>&#123;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid red;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"myCanvas"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"250"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
<span class="hljs-keyword">var</span> c=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myCanvas"</span>);
<span class="hljs-keyword">var</span> ctx=c.getContext(<span class="hljs-string">"2d"</span>);

<span class="hljs-comment">// 1.首先，将画笔定位到起点坐标处；</span>
ctx.moveTo(<span class="hljs-number">50</span>,<span class="hljs-number">50</span>);
<span class="hljs-comment">// 2.然后，从当前位置连一条线到终点坐标处（注意：此时并没有真正的画线！)</span>
ctx.lineTo(<span class="hljs-number">100</span>,<span class="hljs-number">50</span>);
ctx.strokeStyle = <span class="hljs-string">"blue"</span>;    <span class="hljs-comment">// 线条的颜色</span>
ctx.lineWidth = <span class="hljs-string">"5"</span>;     <span class="hljs-comment">// 线条的粗细</span>
<span class="hljs-comment">// 3.最后，画线条，作用是描边————这句才是真正的画线！</span>
ctx.stroke();        <span class="hljs-comment">// 认真学习的同学可以将本行注释再看看效果哦！</span>

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">2️⃣实现效果：</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e161eaf9c9445e3a5e4f4a609db5dd7~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">🚑（2）绘制一条折线</h2>
<blockquote>
<ol>
<li>指定折点处的形状；</li>
<li>指定线端点的形状。</li>
</ol>
</blockquote>
<h3 data-id="heading-13">1️⃣上代码：</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-selector-id">#myCanvas</span>&#123;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid red;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"myCanvas"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"250"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
<span class="hljs-keyword">var</span> c=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myCanvas"</span>);
<span class="hljs-keyword">var</span> ctx=c.getContext(<span class="hljs-string">"2d"</span>);

<span class="hljs-comment">// 1.首先，将画笔定位到起点坐标处</span>
ctx.moveTo(<span class="hljs-number">50</span>,<span class="hljs-number">50</span>);
<span class="hljs-comment">// 2.然后，从当前位置连一条线到重点坐标处【因为现在画的是折线，所以拐两拐】（注意：并不是真画线！)</span>
ctx.lineTo(<span class="hljs-number">100</span>,<span class="hljs-number">50</span>);
ctx.lineTo(<span class="hljs-number">60</span>,<span class="hljs-number">80</span>);

<span class="hljs-comment">// 3.指定线段端点形状  ———— round:圆形；square:正方形；butt:默认</span>
ctx.lineCap = <span class="hljs-string">"round"</span>;  
  
<span class="hljs-comment">// 4.指定线交点（折线点）的形状 ———— round:圆形；miter：默认；bevel:截取一部分；</span>
ctx.lineJoin = <span class="hljs-string">"round"</span>;   

ctx.strokeStyle = <span class="hljs-string">"blue"</span>;  <span class="hljs-comment">// 线条的颜色</span>
ctx.lineWidth = <span class="hljs-string">"5"</span>;   <span class="hljs-comment">// 线条的粗细</span>

<span class="hljs-comment">// 5.最后，画线条，作用是描边————这句才是真正的画线！</span>
ctx.stroke();  

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>认真学习的小伙伴们可以尝试将lineCap和lineJoin的值多次更改，看看各种值的真实实现效果哦！</p>
</blockquote>
<h3 data-id="heading-14">2️⃣实现效果：</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80621d05db8e4737953e630f748b60c4~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">🚔（3）画矩形和圆</h2>
<blockquote>
<p>分别尝试画实心和空心！</p>
</blockquote>
<table><tbody><tr><td>同一张画图上绘制多个图形小知识点：<table><tbody><tr><td>
在同一个canvas上，即同一张画布上画图时，画笔的位置为画笔画完上一个图的结束点！<table><tbody><tr><td>
问题就是重新定位画笔过于麻烦！</td></tr></tbody></table>解决方法——所以在一个图画完后使用.stroke()方法绘制出此图；
并使用方法.beginPath()新开辟一次画图，重新定位画笔即可！
<h3 data-id="heading-16">1️⃣上代码：</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>画方，画圆<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-selector-id">#c1</span>&#123;
<span class="hljs-attribute">border</span>:<span class="hljs-number">1px</span> solid blue;            
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c1"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"1300"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"700"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
<span class="hljs-keyword">var</span> c = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"c1"</span>);
<span class="hljs-keyword">var</span> ctx = c.getContext(<span class="hljs-string">"2d"</span>);

<span class="hljs-comment">//1.绘制空心矩形</span>
ctx.strokeStyle = <span class="hljs-string">"blue"</span>;
ctx.lineWidth = <span class="hljs-number">5</span>;<span class="hljs-comment">//线条粗细</span>
ctx.strokeRect(<span class="hljs-number">50</span>,<span class="hljs-number">50</span>,<span class="hljs-number">250</span>,<span class="hljs-number">250</span>);<span class="hljs-comment">//参数：左上角x,y坐标，x,y方向长度</span>


<span class="hljs-comment">//2.绘制实心矩形</span>
ctx.fillStyle = <span class="hljs-string">"#DFFF4A"</span>;     <span class="hljs-comment">// 指定填充颜色</span>
ctx.fillRect(<span class="hljs-number">350</span>,<span class="hljs-number">50</span>,<span class="hljs-number">100</span>,<span class="hljs-number">100</span>);


<span class="hljs-comment">//3.画一个既描边又填充的矩形</span>
<span class="hljs-comment">//第一种方法：先画一个空心矩形，然后在其内部画一个实心矩形</span>
ctx.lineWidth = <span class="hljs-number">20</span>;
ctx.strokeRect(<span class="hljs-number">500</span>,<span class="hljs-number">50</span>,<span class="hljs-number">100</span>,<span class="hljs-number">100</span>);
ctx.fillRect(<span class="hljs-number">500</span>,<span class="hljs-number">50</span>,<span class="hljs-number">100</span>,<span class="hljs-number">100</span>);

<span class="hljs-comment">//第二种方法：.rect()方法先画一个空心矩形，然后.fill()填充</span>
ctx.rect(<span class="hljs-number">650</span>,<span class="hljs-number">50</span>,<span class="hljs-number">100</span>,<span class="hljs-number">100</span>);
ctx.stroke();
ctx.fill()


<span class="hljs-comment">//4.绘制填充的圆</span>
ctx.beginPath();
ctx.lineWidth = <span class="hljs-number">3</span>;
<span class="hljs-comment">//参数：150,500是圆心，80是半径，0是弧的起始角度，  Math.PI/2是弧的结束角度， true是逆时针;false是顺时针。</span>
ctx.arc(<span class="hljs-number">150</span>,<span class="hljs-number">500</span>,<span class="hljs-number">80</span>,<span class="hljs-number">0</span>,<span class="hljs-built_in">Math</span>.PI*<span class="hljs-number">2</span>,<span class="hljs-literal">true</span>);
ctx.stroke();
ctx.fill();<span class="hljs-comment">// 注意：使用的填充样式都是上面设置过的！</span>


<span class="hljs-comment">// 5.绘制空心的圆</span>
ctx.beginPath();
ctx.lineWidth = <span class="hljs-number">3</span>;
ctx.arc(<span class="hljs-number">400</span>,<span class="hljs-number">500</span>,<span class="hljs-number">80</span>,<span class="hljs-number">0</span>,<span class="hljs-built_in">Math</span>.PI*<span class="hljs-number">2</span>,<span class="hljs-literal">true</span>);
ctx.stroke();

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">2️⃣实现效果：</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6d646876dca4b8aabffc906a5c356fd~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">🚐（4）颜色渐变之线性渐变和发散渐变</h2>
<table><tbody><tr><td>渐变可以填充在矩形, 圆形, 线条, 文本等各种形状中，主要作用是：可以自己定义不同的颜色。</td></tr></tbody></table>
<h3 data-id="heading-19">1️⃣上代码：</h3>
<blockquote>
<p>当我们使用渐变对象，必须使用两种或两种以上的停止颜色。</p>
</blockquote>
<p>addColorStop()方法指定颜色停止，参数使用坐标来描述，可以是0至1。
使用渐变，设置fillStyle或strokeStyle的值为渐变，然后绘制形状，如矩形，文本，或一条线。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>线性渐变和发散渐变<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-selector-id">#c1</span>&#123;
<span class="hljs-attribute">border</span>: <span class="hljs-number">3px</span> solid red;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c1"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"1000"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"700"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
<span class="hljs-comment">//第一步，找到canvas对象。</span>
<span class="hljs-keyword">var</span> c = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"c1"</span>);
<span class="hljs-comment">//第二步，获取canvas的上下文环境</span>
<span class="hljs-keyword">var</span> ctx = c.getContext(<span class="hljs-string">"2d"</span>);

<span class="hljs-comment">//然后就可以通过ctx进行绘制了</span>
ctx.beginPath();

<span class="hljs-comment">// 线性渐变的实现</span>
<span class="hljs-comment">//第一种： 竖着渐变，从指定的左上角坐标到右上角坐标竖着范围内进行颜色渐变</span>
<span class="hljs-keyword">var</span> jianbian = ctx.createLinearGradient(<span class="hljs-number">100</span>,<span class="hljs-number">100</span>,<span class="hljs-number">300</span>,<span class="hljs-number">100</span>);  <span class="hljs-comment">// 左上角x,y坐标，右上角x,y坐标</span>
jianbian.addColorStop(<span class="hljs-number">0</span>,<span class="hljs-string">"red"</span>);
jianbian.addColorStop(<span class="hljs-number">0.5</span>,<span class="hljs-string">"blue"</span>);
jianbian.addColorStop(<span class="hljs-number">1</span>,<span class="hljs-string">"yellow"</span>);
ctx.strokeStyle = jianbian;
ctx.lineWidth = <span class="hljs-number">10</span>;
ctx.moveTo(<span class="hljs-number">100</span>,<span class="hljs-number">100</span>);
ctx.lineTo(<span class="hljs-number">300</span>,<span class="hljs-number">100</span>);
ctx.stroke();

<span class="hljs-comment">//第二种： 斜着渐变，从指定的左上角坐标到右下角坐标斜着范围内进行颜色渐变</span>
ctx.beginPath();
<span class="hljs-keyword">var</span> jianbian2 = ctx.createLinearGradient(<span class="hljs-number">400</span>,<span class="hljs-number">300</span>,<span class="hljs-number">600</span>,<span class="hljs-number">500</span>);
jianbian2.addColorStop(<span class="hljs-number">0</span>,<span class="hljs-string">"cyan"</span>);
jianbian2.addColorStop(<span class="hljs-number">0.3</span>,<span class="hljs-string">"green"</span>);
jianbian2.addColorStop(<span class="hljs-number">0.7</span>,<span class="hljs-string">"purple"</span>);
jianbian2.addColorStop(<span class="hljs-number">1</span>,<span class="hljs-string">"blue"</span>);
ctx.fillStyle = jianbian2;
ctx.moveTo(<span class="hljs-number">400</span>,<span class="hljs-number">300</span>);
ctx.lineTo(<span class="hljs-number">600</span>,<span class="hljs-number">300</span>);
ctx.lineTo(<span class="hljs-number">600</span>,<span class="hljs-number">500</span>);
ctx.lineTo(<span class="hljs-number">400</span>,<span class="hljs-number">500</span>);
ctx.closePath();<span class="hljs-comment">//使用.closePath()方法即可自动封闭图形，封闭终点坐标到起点坐标！</span>
ctx.stroke();
ctx.fill();


<span class="hljs-comment">// 发散渐变的实现</span>
<span class="hljs-comment">//指定两个圆所形成的圆环内发散向四周渐变</span>
ctx.beginPath();
<span class="hljs-keyword">var</span> jianbian3 = ctx.createRadialGradient(<span class="hljs-number">150</span>,<span class="hljs-number">400</span>,<span class="hljs-number">50</span>,<span class="hljs-number">150</span>,<span class="hljs-number">400</span>,<span class="hljs-number">200</span>);  <span class="hljs-comment">// 参数：第一个圆的圆心+半径，第二个圆的圆心+半径</span>
jianbian3.addColorStop(<span class="hljs-number">0</span>,<span class="hljs-string">"red"</span>);
jianbian3.addColorStop(<span class="hljs-number">0.3</span>,<span class="hljs-string">"blue"</span>);
jianbian3.addColorStop(<span class="hljs-number">0.7</span>,<span class="hljs-string">"yellow"</span>);
jianbian3.addColorStop(<span class="hljs-number">1</span>,<span class="hljs-string">"green"</span>);
ctx.fillStyle = jianbian3;
ctx.moveTo(<span class="hljs-number">10</span>,<span class="hljs-number">300</span>);
ctx.lineTo(<span class="hljs-number">310</span>,<span class="hljs-number">300</span>);
ctx.lineTo(<span class="hljs-number">310</span>,<span class="hljs-number">500</span>);
ctx.lineTo(<span class="hljs-number">10</span>,<span class="hljs-number">500</span>);
ctx.closePath();
ctx.stroke();
ctx.fill();

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">2️⃣实现效果：</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5db59ed4ce9482a953c7aafce1cb19d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-21">🚉拓展——几种复杂图形的绘制</h2>
<ul>
<li>题目就是下面所列的五个，请小伙伴们发挥你们的小脑袋瓜，自己先动手绘制哦🙄！</li>
<li>所用的操作在上面都已详细讲解，没有一道题超纲哦（实践是检验真理的唯一标准🤩）</li>
<li>做完的小伙伴们可以看看下面我的代码和实现的效果，说不定你们做的比我的还要好😂！</li>
</ul>
<blockquote>
<ol>
<li>使用红色填充的五角星；</li>
<li>使用渐变色填充的六边形；</li>
<li>机器人头部（使用线性渐变&&发散渐变）；</li>
<li>空心的五角星；</li>
<li>绘制一个四肢健全的小人。</li>
</ol>
</blockquote>
<h3 data-id="heading-22">1️⃣上代码：</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>五道题<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-selector-id">#canvas_first</span>&#123;
<span class="hljs-attribute">border</span>: <span class="hljs-number">5px</span> solid red;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvas_first"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"1500"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"700"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
<span class="hljs-comment">// 想要在canvas上画东西，第一步要先找到canvas控件</span>
<span class="hljs-keyword">var</span> c = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"canvas_first"</span>);
<span class="hljs-comment">//获取绘制的上下文环境,简单理解为画笔（实际上不是画笔）</span>
<span class="hljs-keyword">var</span> ctx = c.getContext(<span class="hljs-string">"2d"</span>);<span class="hljs-comment">//此对象是内建的 HTML5 对象，拥有多种绘制路径、矩形、圆形、字符以及添加图像的方法。</span>

<span class="hljs-comment">// 1.五角星</span>
ctx.moveTo(<span class="hljs-number">100</span>,<span class="hljs-number">0</span>);  <span class="hljs-comment">// 将画笔移动到指定的位置</span>
ctx.fillStyle = <span class="hljs-string">"red"</span>;        <span class="hljs-comment">// 封闭图形填充的颜色   配合.fill()使用</span>
ctx.lineTo(<span class="hljs-number">159</span>,<span class="hljs-number">181</span>);      <span class="hljs-comment">//从当前位置连一条线到指定位置（并不是真画线)</span>
ctx.lineTo(<span class="hljs-number">5</span>,<span class="hljs-number">69</span>);
ctx.lineTo(<span class="hljs-number">195</span>,<span class="hljs-number">69</span>);
ctx.lineTo(<span class="hljs-number">41</span>,<span class="hljs-number">181</span>);
ctx.closePath();
ctx.strokeStyle = <span class="hljs-string">"red"</span>;  <span class="hljs-comment">// 线条的颜色</span>
ctx.stroke();  <span class="hljs-comment">//画线条，作用是描边。</span>
ctx.fill();      <span class="hljs-comment">//填充封闭区域，使用指定的填充样式来填充</span>


<span class="hljs-comment">// 2.六边形</span>
ctx.beginPath();
<span class="hljs-keyword">var</span> jianbian2 = ctx.createLinearGradient(<span class="hljs-number">250</span>,<span class="hljs-number">20</span>,<span class="hljs-number">450</span>,<span class="hljs-number">220</span>);   <span class="hljs-comment">// 线性渐变————左上角到右下角渐变</span>
jianbian2.addColorStop(<span class="hljs-number">0</span>,<span class="hljs-string">"cyan"</span>);
jianbian2.addColorStop(<span class="hljs-number">0.3</span>,<span class="hljs-string">"green"</span>);
jianbian2.addColorStop(<span class="hljs-number">0.7</span>,<span class="hljs-string">"purple"</span>);
jianbian2.addColorStop(<span class="hljs-number">1</span>,<span class="hljs-string">"blue"</span>);
ctx.fillStyle = jianbian2;
ctx.moveTo(<span class="hljs-number">300</span>, <span class="hljs-number">20</span>);
ctx.lineTo(<span class="hljs-number">400</span>,<span class="hljs-number">20</span>);
ctx.lineTo(<span class="hljs-number">450</span>, <span class="hljs-number">120</span>);
ctx.lineTo(<span class="hljs-number">400</span>,<span class="hljs-number">220</span>);
ctx.lineTo(<span class="hljs-number">300</span>,<span class="hljs-number">220</span>);
ctx.lineTo(<span class="hljs-number">250</span>,<span class="hljs-number">120</span>);
ctx.closePath();
ctx.strokeStyle = <span class="hljs-string">"black"</span>;
ctx.lineWidth = <span class="hljs-string">"3"</span>;<span class="hljs-comment">// 设置线条的粗细</span>
ctx.stroke();
ctx.fill();


<span class="hljs-comment">// 3.机器人头</span>
ctx.beginPath();<span class="hljs-comment">// 开启新的路径</span>
<span class="hljs-comment">// 头轮廓</span>
ctx.strokeRect(<span class="hljs-number">500</span>,<span class="hljs-number">20</span>,<span class="hljs-number">250</span>,<span class="hljs-number">250</span>);
<span class="hljs-comment">//左眼</span>
<span class="hljs-keyword">var</span> jianbian3 = ctx.createRadialGradient(<span class="hljs-number">560</span>,<span class="hljs-number">80</span>,<span class="hljs-number">5</span>,<span class="hljs-number">560</span>,<span class="hljs-number">80</span>,<span class="hljs-number">35</span>);    <span class="hljs-comment">// 发散渐变——————指定两组圆心+半径：环内渐变</span>
jianbian3.addColorStop(<span class="hljs-number">0</span>,<span class="hljs-string">"red"</span>);
jianbian3.addColorStop(<span class="hljs-number">0.3</span>,<span class="hljs-string">"blue"</span>);
jianbian3.addColorStop(<span class="hljs-number">0.7</span>,<span class="hljs-string">"yellow"</span>);
jianbian3.addColorStop(<span class="hljs-number">1</span>,<span class="hljs-string">"green"</span>);
ctx.fillStyle = jianbian3;
ctx.arc(<span class="hljs-number">560</span>,<span class="hljs-number">80</span>,<span class="hljs-number">35</span>,<span class="hljs-number">0</span>,<span class="hljs-built_in">Math</span>.PI*<span class="hljs-number">2</span>,<span class="hljs-literal">true</span>);    <span class="hljs-comment">// 150,500是圆心，   80是半径，  0是弧的起始角度，  Math.PI/2是弧的结束角度， true是逆时针;false是顺时针.</span>
<span class="hljs-comment">//右眼</span>
ctx.strokeRect(<span class="hljs-number">653</span>,<span class="hljs-number">46</span>,<span class="hljs-number">70</span>,<span class="hljs-number">70</span>);
<span class="hljs-comment">//鼻子</span>
ctx.moveTo(<span class="hljs-number">620</span>,<span class="hljs-number">145</span>);
ctx.lineTo(<span class="hljs-number">640</span>,<span class="hljs-number">160</span>);
ctx.lineTo(<span class="hljs-number">602</span>,<span class="hljs-number">160</span>);
ctx.closePath();<span class="hljs-comment">//从当前位置连接一条线，到起始位置，形成一个封闭路径</span>
ctx.lineJoin = <span class="hljs-string">"round"</span>; <span class="hljs-comment">//线交点图形</span>
ctx.stroke();
ctx.fill();
<span class="hljs-comment">//嘴巴</span>
ctx.beginPath();
<span class="hljs-keyword">var</span> jianbian = ctx.createLinearGradient(<span class="hljs-number">568</span>,<span class="hljs-number">220</span>,<span class="hljs-number">683</span>,<span class="hljs-number">220</span>);    <span class="hljs-comment">// 线性渐变——————如果是一条直线，直接起点到终点渐变即可（注意：）</span>
jianbian.addColorStop(<span class="hljs-number">0</span>,<span class="hljs-string">"red"</span>);
jianbian.addColorStop(<span class="hljs-number">0.5</span>,<span class="hljs-string">"blue"</span>);
jianbian.addColorStop(<span class="hljs-number">1</span>,<span class="hljs-string">"yellow"</span>);
ctx.strokeStyle = jianbian;
ctx.lineWidth = <span class="hljs-number">20</span>;
ctx.moveTo(<span class="hljs-number">568</span>,<span class="hljs-number">220</span>);
ctx.lineTo(<span class="hljs-number">683</span>,<span class="hljs-number">220</span>);
ctx.lineCap = <span class="hljs-string">"round"</span>;<span class="hljs-comment">//线端点的显示效果</span>
ctx.stroke();


<span class="hljs-comment">// 4.空心五角形</span>
ctx.beginPath();
ctx.lineWidth = <span class="hljs-number">3</span>;
ctx.strokeStyle = <span class="hljs-string">"black"</span>;
ctx.moveTo(<span class="hljs-number">750</span>,<span class="hljs-number">300</span>);
ctx.lineTo(<span class="hljs-number">790</span>,<span class="hljs-number">380</span>);
ctx.lineTo(<span class="hljs-number">870</span>,<span class="hljs-number">380</span>);
ctx.lineTo(<span class="hljs-number">800</span>,<span class="hljs-number">430</span>);
ctx.lineTo(<span class="hljs-number">840</span>,<span class="hljs-number">520</span>);
ctx.lineTo(<span class="hljs-number">750</span>,<span class="hljs-number">460</span>);
ctx.lineTo(<span class="hljs-number">670</span>,<span class="hljs-number">520</span>);
ctx.lineTo(<span class="hljs-number">700</span>,<span class="hljs-number">430</span>);
ctx.lineTo(<span class="hljs-number">630</span>,<span class="hljs-number">380</span>);
ctx.lineTo(<span class="hljs-number">710</span>,<span class="hljs-number">380</span>)
ctx.closePath();
ctx.stroke()


<span class="hljs-comment">// 5.一个四肢健全的小人</span>
ctx.beginPath();
<span class="hljs-comment">// 脑袋</span>
ctx.arc(<span class="hljs-number">1150</span>,<span class="hljs-number">150</span>,<span class="hljs-number">80</span>,<span class="hljs-number">0</span>,<span class="hljs-built_in">Math</span>.PI*<span class="hljs-number">2</span>,<span class="hljs-literal">true</span>);
<span class="hljs-comment">// 身体</span>
ctx.strokeRect(<span class="hljs-number">1070</span>,<span class="hljs-number">230</span>,<span class="hljs-number">160</span>,<span class="hljs-number">250</span>);
<span class="hljs-comment">// 身体的纽扣</span>
ctx.strokeRect(<span class="hljs-number">1143</span>,<span class="hljs-number">290</span>,<span class="hljs-number">10</span>,<span class="hljs-number">20</span>);
ctx.strokeRect(<span class="hljs-number">1143</span>,<span class="hljs-number">350</span>,<span class="hljs-number">10</span>,<span class="hljs-number">20</span>);
ctx.strokeRect(<span class="hljs-number">1143</span>,<span class="hljs-number">410</span>,<span class="hljs-number">10</span>,<span class="hljs-number">20</span>);
<span class="hljs-comment">// 腿</span>
ctx.strokeRect(<span class="hljs-number">1165</span>,<span class="hljs-number">480</span>,<span class="hljs-number">45</span>,<span class="hljs-number">120</span>);
ctx.strokeRect(<span class="hljs-number">1090</span>,<span class="hljs-number">480</span>,<span class="hljs-number">45</span>,<span class="hljs-number">120</span>);
<span class="hljs-comment">// 脚</span>
ctx.strokeRect(<span class="hljs-number">1158</span>,<span class="hljs-number">600</span>,<span class="hljs-number">60</span>,<span class="hljs-number">25</span>);
ctx.strokeRect(<span class="hljs-number">1082</span>,<span class="hljs-number">600</span>,<span class="hljs-number">60</span>,<span class="hljs-number">25</span>);
<span class="hljs-comment">// 右胳膊+手</span>
ctx.strokeRect(<span class="hljs-number">1230</span>,<span class="hljs-number">290</span>,<span class="hljs-number">110</span>,<span class="hljs-number">35</span>);
ctx.strokeRect(<span class="hljs-number">1310</span>,<span class="hljs-number">325</span>,<span class="hljs-number">30</span>,<span class="hljs-number">78</span>);
<span class="hljs-comment">// 左胳膊+手</span>
ctx.strokeRect(<span class="hljs-number">960</span>,<span class="hljs-number">290</span>,<span class="hljs-number">110</span>,<span class="hljs-number">35</span>);
ctx.strokeRect(<span class="hljs-number">960</span>,<span class="hljs-number">325</span>,<span class="hljs-number">30</span>,<span class="hljs-number">78</span>);
ctx.stroke();
<span class="hljs-comment">// 小脸</span>
ctx.beginPath();
<span class="hljs-comment">// 左眼</span>
ctx.arc(<span class="hljs-number">1115</span>,<span class="hljs-number">125</span>,<span class="hljs-number">20</span>,<span class="hljs-number">0</span>,<span class="hljs-built_in">Math</span>.PI,<span class="hljs-literal">true</span>);
<span class="hljs-comment">// 右眼</span>
ctx.moveTo(<span class="hljs-number">1200</span>,<span class="hljs-number">125</span>);
ctx.arc(<span class="hljs-number">1180</span>,<span class="hljs-number">125</span>,<span class="hljs-number">20</span>,<span class="hljs-number">0</span>,<span class="hljs-built_in">Math</span>.PI,<span class="hljs-literal">true</span>);
<span class="hljs-comment">// 嘴巴</span>
ctx.moveTo(<span class="hljs-number">1180</span>,<span class="hljs-number">170</span>);
ctx.arc(<span class="hljs-number">1150</span>,<span class="hljs-number">170</span>,<span class="hljs-number">30</span>,<span class="hljs-number">0</span>,<span class="hljs-built_in">Math</span>.PI,<span class="hljs-literal">false</span>);
ctx.stroke();

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">2️⃣实现效果：</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb1ef3ad82b74c03895a8c003a7fbd8b~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>🌻🌻如果你从本文中学到了知识，喜欢它，那么我很荣幸。希望你可以将本文分享给你的小伙伴，点个赞&&收藏本文，并且，欢迎广大读者在评论区探讨技术，或是提出你们真诚的意见。🌻🌻</p>
<blockquote>
<p>🌹本文到此结束，很高兴遇见你——我是【孤寒者】，一个喜欢计算机的男孩子！🌹</p>
</blockquote></td></tr></tbody></table></td></tr></tbody></table></div>  
</div>
            