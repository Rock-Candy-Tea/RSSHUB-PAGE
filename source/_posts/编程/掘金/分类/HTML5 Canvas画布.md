
---
title: 'HTML5 Canvas画布'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7e240393a3f4e00b56ed2fcb57821c8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 23:43:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7e240393a3f4e00b56ed2fcb57821c8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>canvas元素用于在网页上绘制图形。</p>
<h2 data-id="heading-0">什么是canvas?</h2>
<p>HTML5元素用于图形的绘制，通过脚本(通常是JavaScript)来完成.</p>
<p>标签只是图形容器，您必须使用脚本来绘制图形。</p>
<p>你可以通过多种方法使用canvas绘制路径,盒、圆、字符以及添加图像。</p>
<h2 data-id="heading-1">浏览器支持</h2>
<p>表格中的数字表示支持元素的第一个浏览器版本号。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7e240393a3f4e00b56ed2fcb57821c8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">创建一个画布（Canvas）</h2>
<p>一个画布在网页中是一个矩形框，通过元素来绘制.</p>
<p>注意:默认情况下元素没有边框和内容。</p>
<p>简单实例如下:</p>
<pre><code class="copyable"><canvas id="myCanvas" width="200" height="100"></canvas>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意: 标签通常需要指定一个id属性 (脚本中经常引用), width 和 height 属性定义的画布的大小.</p>
<p>提示:你可以在HTML页面中使用多个  元素.</p>
<p>使用 style 属性来添加边框:</p>
<pre><code class="copyable">canvas id="myCanvas" width="200" height="100"
style="border:1px solid #000000;">
</canvas></pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果展示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c954c529b724631bcbd00bf1f05526c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">使用JavaScript来绘制图像</h2>
<p>canvas元素本身是没有绘图能力的。所有的绘制工作必须在JavaScript内部完成：</p>
<p>HTML代码：</p>
<pre><code class="copyable"><canvas id="myCanvas" width="200" height="100" style="border:1px solid #c3c3c3;">
您的浏览器不支持 HTML5 canvas 标签。
</canvas></pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>javascript代码：</p>
<pre><code class="copyable">var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
ctx.fillStyle="#FF0000";
ctx.fillRect(0,0,150,75);</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果展示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d181b36671d44bf5845e7194c2b6c5fc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>实例解析:</strong></p>
<p>首先，找到  元素:</p>
<p><code>var c=document.getElementById("myCanvas");</code></p>
<p>然后，创建 context 对象：</p>
<p><code>var ctx=c.getContext("2d");</code></p>
<p>getContext(“2d”) 对象是内建的 HTML5 对象，拥有多种绘制路径、矩形、圆形、字符以及添加图像的方法。</p>
<p>下面的两行代码绘制一个红色的矩形：</p>
<pre><code class="copyable">ctx.fillStyle="#FF0000";
ctx.fillRect(0,0,150,75);</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置fillStyle属性可以是CSS颜色，渐变，或图案。fillStyle 默认设置是#000000（黑色）。</p>
<p>fillRect(x,y,width,height) 方法定义了矩形当前的填充方式。</p>
<h2 data-id="heading-4">Canvas 坐标</h2>
<p>canvas 是一个二维网格。</p>
<p>canvas 的左上角坐标为 (0,0)</p>
<p>上面的 fillRect 方法拥有参数 (0,0,150,75)。</p>
<p>意思是：在画布上绘制 150×75 的矩形，从左上角开始 (0,0)。</p>
<p>坐标实例</p>
<p>如下图所示，画布的 X 和 Y 坐标用于在画布上对绘画进行定位。鼠标移动的矩形框上，显示定位坐标。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19ef5ec371ad40fca47efddd8051acc3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">Canvas 路径</h2>
<p>在Canvas上画线，我们将使用以下两种方法：</p>
<ul>
<li>moveTo(x,y)定义线条开始坐标</li>
<li>lineTo(x,y)定义线条结束坐标</li>
</ul>
<p>绘制线条我们必须使用到”ink”的方法，就像stroke().</p>
<p><strong>举例：</strong></p>
<p>定义开始坐标(0,0), 和结束坐标 (200,100)。然后使用 stroke() 方法来绘制线条:</p>
<p>HTML代码：</p>
<p><code><canvas id="myCanvas" width="200" height="100" style="border:1px solid #d3d3d3;">您的浏览器不支持 HTML5 canvas 标签。</canvas></pre></code></p>
<p>javascript代码:</p>
<pre><code class="copyable">var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
ctx.moveTo(0,0);
ctx.lineTo(200,100);
ctx.stroke();</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果展示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74214b79a7e244dcbdb018cfc299175e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在canvas中绘制圆形, 我们将使用以下javascript方法:</p>
<p><code>context.arc(<i>x</i>,<i>y</i>,<i>r</i>,<i>sAngle</i>,<i>eAngle</i>,<i>counterclockwise</i>);</code></p>
<p><strong>参数值</strong>
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48c58a4f74234e8bb7f3a6ecbd42f3a2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>定义和用法</strong></p>
<p>arc()方法创建弧/曲线（用于创建圆或部分圆）。</p>
<p>提示：如需通过arc()来创建圆，请把起始角设置为0，结束角设置为2*Math.PI。</p>
<p>提示：请使用stroke()或fill()方法在画布上绘制实际的弧。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/819f5bab203140e68dd341b782f9dca4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>中心：arc(100,75,50,0<em>Math.PI,1.5</em>Math.PI)</li>
<li>起始角：arc(100,75,50,0,1.5*Math.PI)</li>
<li>结束角：arc(100,75,50,0<em>Math.PI,1.5</em>Math.PI)</li>
</ul>
<p>实际上我们在绘制圆形时使用了 “ink” 的方法, 比如 stroke() 或者 fill().</p>
<p><strong>实例</strong></p>
<p>使用arc()方法绘制一个圆:</p>
<p>HTML代码：</p>
<pre><code class="copyable"><canvas id="myCanvas" width="200" height="100" style="border:1px solid #d3d3d3;">
您的浏览器不支持 HTML5 canvas 标签。</canvas></pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>javascript代码：</p>
<pre><code class="copyable">var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
ctx.beginPath();
ctx.arc(95,50,40,0,2*Math.PI);
ctx.stroke();</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果展示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b4a16be84fb498fb641535413ff8697~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">Canvas-文本</h2>
<p>使用canvas绘制文本，重要的属性和方法如下：</p>
<p>font-定义字体</p>
<p>fillText(<em>text,x,y,maxWidth</em>)-在canvas上绘制实心的文本</p>
<p>strokeText(<em>text,x,y,maxWidth</em>)-在canvas上绘制空心的文本</p>
<p><strong>参数值</strong></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd96bbca14bb43c1b1d0ec61ce29a02b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>使用fillText():</strong></p>
<p>实例</p>
<p>使用”Arial”字体在画布上绘制一个高30px的文字（实心）：</p>
<p>HTML代码：</p>
<pre><code class="copyable"><canvas id="myCanvas" width="200" height="100" style="border:1px solid #d3d3d3;">
您的浏览器不支持 HTML5 canvas 标签。</canvas></pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>javascript代码：</p>
<pre><code class="copyable">var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
ctx.font="30px Arial";
ctx.fillText("Hello World",10,50);</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果展示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e5fefefc06d433fba4d743c0f4367c3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>使用strokeText():</strong></p>
<p>实例</p>
<p>使用”Arial”字体在画布上绘制一个高30px的文字（空心）：</p>
<p>HTML代码：</p>
<pre><code class="copyable"><canvas id="myCanvas" width="200" height="100" style="border:1px solid #d3d3d3;">
您的浏览器不支持 HTML5 canvas 标签。</canvas></pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>javascript代码：</p>
<pre><code class="copyable">var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
ctx.font="30px Arial";
ctx.strokeText("Hello World",10,50);</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果展示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d6cf535ed1841109dfa102bc07cf1cf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">Canvas-渐变</h2>
<p>渐变可以填充在矩形,圆形,线条,文本等等,各种形状可以自己定义不同的颜色。</p>
<p>以下有两种不同的方式来设置Canvas渐变：</p>
<p>createLinearGradient()方法创建线性的渐变对象。</p>
<p>提示：请使用 addColorStop() 方法规定不同的颜色，以及在 gradient 对象中的何处定位颜色。</p>
<pre><code class="copyable">addColorStop()方法规定渐变对象中的颜色和位置。

addColorStop()方法与createLinearGradient()或createRadialGradient()一起使用。

注意：您可以多次调用addColorStop()方法来改变渐变。如果您不对渐变对象使用该方法，那么渐变将不可见。为了获得可见的渐变，您需要创建至少一个色标。

JavaScript语法：gradient.addColorStop(stop,color);

stop 介于0.0与1.0之间的值，表示渐变中开始与结束之间的位置。

color 在stop位置显示的CSS颜色值。</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>javascript语法</p>
<p><code>createLinearGradient(x,y,x1,y1)</pre></code></p>
<p><strong>参数值</strong></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95ae09f8e8d2466b8980248ead9b0abe~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>createLinearGradient() 方法创建放射状/圆形渐变对象。</p>
<p>JavaScript 语法：</p>
<p><code>createRadialGradient(x0,y0,r0,x1,y1,r1);</pre> </code></p>
<p><strong>参数值</strong></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3b4b9db568943b6b043c3eaaa4bebce~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>实例</p>
<p>使用createLinearGradient()创建一个线性渐变。使用渐变填充矩形:</p>
<p>javascript代码：</p>
<pre><code class="copyable">var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");

// Create gradient
var grd=ctx.createLinearGradient(0,0,200,0);
grd.addColorStop(0,"red");
grd.addColorStop(1,"white");

// Fill with gradient
ctx.fillStyle=grd;
ctx.fillRect(10,10,150,80);</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果展示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4369af080d564e398a8ae4bf81dbd9ac~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>实例</p>
<p>使用createRadialGradient()创建一个径向/圆渐变。使用渐变填充矩形：</p>
<p>javascript代码：</p>
<pre><code class="copyable">var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");

// Create gradient
var grd=ctx.createRadialGradient(75,50,5,90,60,100);
grd.addColorStop(0,"red");
grd.addColorStop(1,"white");

// Fill with gradient
ctx.fillStyle=grd;
ctx.fillRect(10,10,150,80);</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果展示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/543a1b587fec4a749e768baafd53a444~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">Canvas 图像</h2>
<p>把一幅图像放置到画布上, 使用以下方法:</p>
<p><code>drawImage(image,x,y)</pre> </code></p>
<p>HTML代码：</p>
<pre><code class="copyable"><p>Image to use:</p>
<img id="scream" src="img_the_scream.jpg" alt="The Scream" width="220" height="277">
<p>Canvas:</p>
<canvas id="myCanvas" width="250" height="300" style="border:1px solid #d3d3d3;">
您的浏览器不支持 HTML5 canvas 标签。
</canvas></pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>javascript代码：</p>
<pre><code class="copyable">var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
var img=document.getElementById("scream");

img.onload = function() &#123;
   ctx.drawImage(img,10,10);
&#125;</pre>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果展示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d239f75386ea4be8a81b754af6ff6d4e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d92db32794624aa39bf9cfdce5b9b5dd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            