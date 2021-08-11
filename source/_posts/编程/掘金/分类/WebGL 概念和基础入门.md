
---
title: 'WebGL 概念和基础入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 15:08:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是第 110 篇不掺水的原创，想获取更多原创好文，请搜索公众号关注我们吧~ 本文首发于政采云前端博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzoo.team%2Farticle%2Fwebglabout" target="_blank" rel="nofollow noopener noreferrer" title="https://zoo.team/article/webglabout" ref="nofollow noopener noreferrer"> WebGL 概念和基础入门</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/037d120ded4b4ffbabbd15a0bf9336ba~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">WebGL 是什么</h2>
<p>对于 WebGL 百度百科给出的解释是 WebGL 是一种 3D 绘图协议，而对此维基百科给出的解释却是一种 JavaScript API。由于 WebGL 技术旨在帮助我们在不使用插件的情况下在任何兼容的网页浏览器中开发交互式 2D 和 3D 网页效果，我们可以将其理解为一种帮助我们开发 3D 网页的绘图技术，当然底层还是 JavaScript API。</p>
<h2 data-id="heading-1">WebGL 发展史</h2>
<p>WebGL 的发展最早要追溯到 2006 年，WebGL 起源于 Mozilla 员工弗拉基米尔·弗基西维奇的一项 Canvas 3D 实验项目，并于 2006 年首次展示了 Canvas 3D 的原型。这一技术在 2007 年底在 FireFox 和 Opera 浏览器中实现。2009 年初 Khronos Group 联盟创建了 WebGL 的工作组最初的工作成员包括 Apple、Google、Mozilla、Opera 等。 2011 年 3 月 WebGL 1.0 规范发布，WebGL 2 规范的发展始于 2013 年，并于 2017 年 1 月最终完成，WebGL 2 的规范，首度在 Firefox 51、Chrome 56 和 Opera 43 中被支持。</p>
<h2 data-id="heading-2">WebGL 中的基本概念</h2>
<p>WebGL 运行在电脑的 GPU 中，因此需要使用能在 GPU 上运行的代码，这样的代码需要提供成对的方法，每对方法中的一个叫顶点着色器而另外一个叫做片元着色器，并且使用 GLSL 语言。将顶点着色器和片元着色器连接起来的方法叫做着色程序。</p>
<ul>
<li>顶点着色器</li>
</ul>
<p>顶点着色器的作用是计算顶点的位置，即提供顶点在裁剪空间中的坐标值
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/927e60379ad6434b95ff81c0e7196d86~tplv-k3u1fbpfcp-watermark.image" alt="顶点着色器工作原理" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>片元着色器</li>
</ul>
<p>片元着色器的作用是计算图元的颜色值，我们可以将片元着色器大致理解成网页中的像素</p>
<ul>
<li>数据获取方式
在前面我们提到了顶点着色器和片元着色器的概念，而顶点着色器和片元着色器这两个方法的运行都需要有对应的数据，接下来我们一起来了解一下着色器获取数据的四种方式：
<ul>
<li>属性和缓冲</li>
</ul>
缓冲是发送到 GPU 的一些二进制数据序列，通常情况下缓冲数据包括位置、方向、纹理坐标、顶点颜色值等。 当然你可以根据自己的需要存储任何你想要的数据。
属性用于说明如何从缓冲中获取所需数据并将它提供给顶点着色器。
<ul>
<li>全局变量</li>
</ul>
全局变量在着色程序运行前赋值，在运行过程中全局有效。全局变量在一次绘制过程中传递给着色器的值都一样。
<ul>
<li>纹理</li>
</ul>
纹理是一个数据序列，可以在着色程序运行中随意读取其中的数据。一般情况下我们在纹理中存储的大都是图像数据，但你也可以根据自己喜欢存放除了颜色数据以外的其它数据
<ul>
<li>可变量</li>
</ul>
可变量是一种顶点着色器给片元着色器传值的方式</li>
</ul>
<h3 data-id="heading-3">小结</h3>
<p>WebGL 只关心两件事：裁剪空间中的坐标值和颜色值。使用 WebGL 只需要给它提供这两个东西。 因此我们通过提供两个着色器来做这两件事，一个顶点着色器提供裁剪空间坐标值，一个片元着色器提供颜色值。</p>
<h2 data-id="heading-4">WebGL 工作原理</h2>
<p>了解完 WebGL 的一些基本概念，我们可以一起来看看 WebGL 在 GPU 上的工作都做了些什么。正如我们之前了解到的 WebGL 在 GPU 上的工作主要分为两个部分，即顶点着色器所做的工作（将顶点转换为裁剪空间坐标）和片元着色器所做的工作（基于顶点着色器的计算结果绘制像素点）。假如我们需要绘制一个三角形，此时 GPU 上进行的工作便是先调用三次顶点着色器计算出三角形的 3 个顶点在裁剪空间坐标系中的对应位置，并通过变量 gl_Position 保存在 GPU 中，然后调用片元着色器完成每个顶点颜色值的计算，并通过变量 gl_FragColor 将对应的颜色值存储在 GPU 中。完成这些工作后我们已经得到了绘制三角形所需的像素点，最后便是光栅化三角形了。</p>
<h2 data-id="heading-5">原生 WebGL API 绘制三角形</h2>
<p>前面我们已经学习了 WebGL 的发展史、基本概念和工作原理等内容，接下来我们就该实践出真知了，所以我们来看看如何通过 WebGL 在网页中绘制一个简单的三角形。我们知道 WebGL 作为一种 3D 绘图技术本身就是依托于 HTML5 中的 canvas 元素而存在的，所以再正式开始绘制之前我们需要进行一系列的准备工作：</p>
<ul>
<li>
<p>首先我们需要创建一个 canvas 元素作为绘制三角形所需的画布，并完成浏览器对 canvas 元素兼容性的测试。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">webglInit</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> canvasEl = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>); <span class="hljs-comment">// canvas 元素创建</span>
  canvasEl.width = <span class="hljs-built_in">document</span>.body.clientWidth; <span class="hljs-comment">// 设置 canvas 画布的宽度</span>
  canvasEl.height = <span class="hljs-built_in">document</span>.body.clientHeight; <span class="hljs-comment">// 设置 canvas 画布的高度</span>
  <span class="hljs-built_in">document</span>.body.append(canvasEl); <span class="hljs-comment">// 将创建好的 canvas 画布添加至页面中的 body 元素下</span>
  <span class="hljs-comment">// 接下来我们需要判断浏览器对于 WebGL 的兼容性，如果浏览器不支持 WebGL 那么我们就不需要再进行下去了</span>
  <span class="hljs-keyword">if</span>(!canvasEl.getContext(<span class="hljs-string">"webgl"</span>) && !canvasEl.getContext(<span class="hljs-string">"experimental-webgl "</span>)) &#123;
    alert(<span class="hljs-string">"Your Browser Doesn't Support WebGL"</span>);
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-comment">// 如果浏览器支持 WebGL，那么我们就获取 WebGL 的上下文对象并复制给变量 gl</span>
  <span class="hljs-keyword">const</span> context = (canvasEl.getContext(<span class="hljs-string">"webgl"</span>))
  ? canvasEl.getContext(<span class="hljs-string">"webgl"</span>) 
  : getContext(<span class="hljs-string">"experimental-webgl"</span>);
  <span class="hljs-comment">/* 
    设置视口 context.viewport(x, y, width, height);
    x: 用来设定视口的左下角水平坐标。默认值：0
    y: 用来设定视口的左下角垂直坐标。默认值：0
    width: 用来设定视口的宽度。默认值：canvas 的宽度
    height: 用来设定视口的高度。默认值：canvas 的高度
    当你第一次创建 WebGL 上下文的时候，视口的大小和 canvas 的大小是匹配的。然而，如果你重新改变了canvas的大小，你需要告诉 WebGL 上下文设定新的视口，因此这里作为初次创建这行代码可以省略
  */</span>
  context.viewport(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, context.canvas.width, context.canvas.height);
  <span class="hljs-keyword">return</span> context;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>准备好了 canvas 画布下一步就可以开始画三角形了，正如我们平常画画一般，我们需要准备画三角形所需的顶点即顶点着色器，以及三角形对应的填充色即片元着色器</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> gl =  webglInit();
<span class="hljs-comment">// 创建顶点着色器 语法 gl.createShader(type) 此处 type 为枚举型值为 gl.VERTEX_SHADER 或 gl.FRAGMENT_SHADER 两者中的一个</span>
<span class="hljs-keyword">const</span> vShader = gl.createShader(gl.VERTEX_SHADER) 
<span class="hljs-comment">// 编写顶点着色器的 GLSL 代码 语法 gl.shaderSource(shader, source); shader - 用于设置程序代码的 webglShader（着色器对象) source - 包含 GLSL 程序代码的字符串</span>
gl.shaderSource(vShader, <span class="hljs-string">`
  attribute vec4 v_position;

  void main() &#123;
    gl_Position = v_position; // 设置顶点位置
  &#125;
`</span>)
gl.compileShader(vShader) <span class="hljs-comment">// 编译着色器代码</span>

<span class="hljs-keyword">const</span> fShader = gl.createShader(gl.FRAGMENT_SHADER) 
gl.shaderSource(fShader, <span class="hljs-string">`
  precision mediump float;
  uniform vec4 f_color;
  void main() &#123;
    gl_FragColor = f_color; // 设置片元颜色
  &#125;
`</span>) <span class="hljs-comment">// 编写片元着色器代码 </span>
gl.compileShader(fShader) <span class="hljs-comment">// 编译着色器代码</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>前面我们已经完成了顶点着色器和片元着色器的配置，做好了一切绘制前的准备工作接下来，接下来我们就需要创建一个程序用来连接我们的顶点着色器和片元着色器完成最终的三角形绘制工作。</p>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建一个程序用于连接顶点着色器和片元着色器</span>
<span class="hljs-keyword">const</span> program = gl.createProgram() 
gl.attachShader(program, vShader) <span class="hljs-comment">// 添加顶点着色器</span>
gl.attachShader(program, fShader) <span class="hljs-comment">// 添加片元着色器</span>
gl.linkProgram(program) <span class="hljs-comment">// 连接 program 中的着色器</span>

gl.useProgram(program) <span class="hljs-comment">// 告诉 WebGL 用这个 program 进行渲染</span>

<span class="hljs-keyword">const</span> color = gl.getUniformLocation(program, <span class="hljs-string">'f_color'</span>) 
<span class="hljs-comment">// 获取 f_color 变量位置</span>
gl.uniform4f(color, <span class="hljs-number">0.93</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.56</span>, <span class="hljs-number">1</span>) <span class="hljs-comment">// 设置它的值</span>

<span class="hljs-keyword">const</span> position = gl.getAttribLocation(program, <span class="hljs-string">'v_position'</span>) 
<span class="hljs-comment">// 获取 v_position 位置</span>
<span class="hljs-keyword">const</span> pBuffer = gl.createBuffer() 
<span class="hljs-comment">// 创建一个顶点缓冲对象，返回其 id，用来放三角形顶点数据，</span>
gl.bindBuffer(gl.ARRAY_BUFFER, pBuffer) 
<span class="hljs-comment">// 将这个顶点缓冲对象绑定到 gl.ARRAY_BUFFER</span>
<span class="hljs-comment">// 后续对 gl.ARRAY_BUFFER 的操作都会映射到这个缓存</span>
gl.bufferData(gl.ARRAY_BUFFER, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>([
    <span class="hljs-number">0</span>, <span class="hljs-number">0.5</span>,
    <span class="hljs-number">0.5</span>, <span class="hljs-number">0</span>,
    -<span class="hljs-number">0.5</span>, -<span class="hljs-number">0.5</span>
]),  <span class="hljs-comment">// 三角形的三个顶点</span>
     <span class="hljs-comment">// 因为会将数据发送到 GPU，为了省去数据解析，这里使用 Float32Array 直接传送数据</span>
gl.STATIC_DRAW <span class="hljs-comment">// 表示缓冲区的内容不会经常更改</span>
)
<span class="hljs-comment">// 将顶点数据加入的刚刚创建的缓存对象</span>

gl.vertexAttribPointer( <span class="hljs-comment">// 告诉 OpenGL 如何从 Buffer 中获取数据</span>
    position, <span class="hljs-comment">// 顶点属性的索引</span>
    <span class="hljs-number">2</span>, <span class="hljs-comment">// 组成数量，必须是 1，2，3 或 4。我们只提供了 x 和 y</span>
    gl.FLOAT, <span class="hljs-comment">// 每个元素的数据类型</span>
    <span class="hljs-literal">false</span>, <span class="hljs-comment">// 是否归一化到特定的范围，对 FLOAT 类型数据设置无效</span>
    <span class="hljs-number">0</span>, <span class="hljs-comment">// stride 步长 数组中一行长度，0 表示数据是紧密的没有空隙，让 OpenGL 决定具体步长</span>
    <span class="hljs-number">0</span> <span class="hljs-comment">// offset 字节偏移量，必须是类型的字节长度的倍数。</span>
)
gl.enableVertexAttribArray(position);
<span class="hljs-comment">// 开启 attribute 变量额，使顶点着色器能够访问缓冲区数据</span>

gl.clearColor(<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>) <span class="hljs-comment">// 设置清空颜色缓冲时的颜色值</span>
gl.clear(gl.COLOR_BUFFER_BIT) <span class="hljs-comment">// 清空颜色缓冲区，也就是清空画布</span>
<span class="hljs-comment">// 语法 gl.drawArrays(mode, first, count); mode - 指定绘制图元的方式 first - 指定从哪个点开始绘制 count - 指定绘制需要使用到多少个点</span>
gl.drawArrays( gl.TRIANGLES, <span class="hljs-number">0</span>, <span class="hljs-number">3</span> )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配合 HTML 文件运行上述代码后我们可以在网页中看到如图所示的三角形，且三角形大小根据浏览器窗口大小自适应。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c675c63bd8e4667a8d9e2799d05f120~tplv-k3u1fbpfcp-watermark.image" alt="webgl triangle" loading="lazy" referrerpolicy="no-referrer">
可以看到仅仅是绘制一个简单的三角形我们就已经写了一大长串的 JS 代码，如果真的用原生 WebGL  API 编写一个动态的 3D 交互式网页，那么开发成本可见是极其昂贵的。</p>
<h2 data-id="heading-6">WebGL 原生 API 开发的不足</h2>
<p>上面原生 WebGL API 绘制三角形的例子，充分向我们展示了使用原生 WebGL API 开发 3D 交互式网页存在的问题。尽管从功能上而言原生 WebGL API 可以满足我们任意场景的开发需要但是，其开发和学习的成本极其昂贵。对于 WebGL 的初学者而言是极度不友好的，我们需要配置顶点着色器用于计算绘制顶点所在的位置，而这对于开发者而言需要一定的数学基础熟悉矩阵的运算，同时也要有空间几何的概念熟悉 3D 物体的空间分布。而场景的光照，纹理等的设计也都需要对颜色的配置有自己的见解。所以为了给初学者降低难度，下面我将介绍一些 WebGL 开发的常用框架。</p>
<h2 data-id="heading-7">几种 WebGL 开发的框架</h2>
<ul>
<li>Three.js
<ul>
<li>Three.js 是 WebGL 的综合库，其应用范围比较广泛，美中不足的一点是，Three.js 库没有比较全面详细的官方文档，对于使用者而言不是特别友好</li>
</ul>
</li>
<li>Cesium.js
<ul>
<li>Cesium.js 是专用于 3D 地图开发的 WebGL 库，其拥有较为全面的 3D 地图开发 API，对于需要开发 3D 地图的开发者而言是一个不错的选择，但针对其他场景的应用开发覆盖的就不是很全面了</li>
</ul>
</li>
<li>Babylon.js
<ul>
<li>Babylon.js 是一款国外应用较广泛的 WebGL 库，感兴趣的小伙伴可以自己去了解一下，这里就不做详细介绍了</li>
</ul>
</li>
</ul>
<p>Three.js 是一款运行在浏览器中的 3D 引擎，你可以用它创建各种三维场景，同时 Three.js 也是一个综合性的 WebGL 库。如果你需要进行 3D 地图网页的开发那就可以用到 Cesium.js 了，Cesium.js 是一款专用于地图开发的 WebGL 库。而 Babylon.js 则是国外较火的 WebGL 库。</p>
<h2 data-id="heading-8">基于 Three.js 绘制旋转立方体</h2>
<ul>
<li>
<p>运用 Three.js 绘制旋转立方体的第一步同原生 WebGl 一样，首先便是要准备 Three.js 运行所需的环境。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建 renderer 变量用于存储渲染器对象</span>
<span class="hljs-keyword">var</span> renderer;
<span class="hljs-comment">// initThree 函数用来初始化 Three.js 运行所需的环境</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initThree</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 同原生 WebGL 环境搭建过程一样，Three.js 也需要先设置画布 canvas 元素的大小</span>
  width = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'canvas-frame'</span>).clientWidth; <span class="hljs-comment">// 设置宽度属性为浏览器窗口宽度</span>
  height = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'canvas-frame'</span>).clientHeight; <span class="hljs-comment">// 设置高度属性为浏览器窗口高度</span>
  <span class="hljs-comment">// 新建一个 WebGL 渲染器并赋值给 renderer 变量</span>
  renderer = <span class="hljs-keyword">new</span> THREE.WebGLRenderer(&#123;
    <span class="hljs-attr">antialias</span>: <span class="hljs-literal">true</span>
  &#125;);
  <span class="hljs-comment">// 设置画布大小为浏览器窗口大小</span>
  renderer.setSize(width, height);
  <span class="hljs-comment">// 将画布元素挂载到页面</span>
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'canvas-frame'</span>).appendChild(renderer.domElement);
  <span class="hljs-comment">// 设置清空画布的颜色为白色</span>
  renderer.setClearColor(<span class="hljs-number">0xFFFFFF</span>, <span class="hljs-number">1.0</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>接下来不同于原生 WebGL 需要准备顶点着色器和片元着色器，Three.js 需要准备的是相机。Three.js 绘制 3D 网页所需的 3 大基本要素便是 相机、场景和物体，当然如果有需要设置明暗效果我们还需要加入第 4 要素光源，光源并不一定需要设置，但是相机、场景和物体是一定有的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建 camera 变量用于存储相机对象</span>
<span class="hljs-keyword">var</span> camera;
<span class="hljs-comment">// 初始化相机函数 Three.js 中相机的类型有好几种可以根据具体需要进行选择这里我们要创建的是一个旋转的立方体所以采用的是透视相机，而如果需要创建 3D 阴影效果的场景则需要使用正交相机</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initCamera</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">/* 
    创建透一个视相机的实例语法 PerspectiveCamera( fov : Number, aspect : Number, near : Number, far : Number ) 
    fov - 视角
    aspect - 物体的长宽比
    near - 相机近点截图
    far - 相机远点截图
  */</span>
  camera = <span class="hljs-keyword">new</span> THREE.PerspectiveCamera(<span class="hljs-number">45</span>, width / height, <span class="hljs-number">1</span>, <span class="hljs-number">10000</span>);
  camera.position.x = <span class="hljs-number">0</span>; <span class="hljs-comment">// 设置相机在三维空间坐标中 x 轴的位置</span>
  camera.position.y = <span class="hljs-number">10</span>; <span class="hljs-comment">// 设置相机在三维空间坐标中 y 轴的位置</span>
  camera.position.z = <span class="hljs-number">5</span>; <span class="hljs-comment">// 设置相机在三维空间坐标中 z 轴的位置</span>
  camera.up.x = <span class="hljs-number">0</span>;
  camera.up.y = <span class="hljs-number">0</span>;
  camera.up.z = <span class="hljs-number">1</span>;
  camera.lookAt(<span class="hljs-keyword">new</span> THREE.Vector3(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>));<span class="hljs-comment">// 设置相机的观察点</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>上一步我们完成了相机的设置，下面我们来准备 Three.js 绘制 3D 网页所需的第二要素场景。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建 scene 变量用于存储场景对象</span>
<span class="hljs-keyword">var</span> scene;
<span class="hljs-comment">// initScene 函数创建一个场景并赋值给 scene 变量</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initScene</span>(<span class="hljs-params"></span>) </span>&#123;
  scene = <span class="hljs-keyword">new</span> THREE.Scene();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>准备好了相机和场景下面我们就需要设置拍摄的物体了，完成物体的绘制后将其添加到场景中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建一个 cube 变量用于存放几何立方体</span>
<span class="hljs-keyword">var</span> cube;

<span class="hljs-comment">// initObject 函数就是我们创建场景的核心了</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initObject</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 首先创建一个一个几何类的实例并赋值给 geometry 变量</span>
  <span class="hljs-keyword">var</span> geometry = <span class="hljs-keyword">new</span> THREE.BoxGeometry(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>); 
  <span class="hljs-comment">// 然后创建一种材质的实例 MeshBasicMaterial 材质的构造函数能够创建一种简单的不受场景灯光效果影响的材质</span>
  <span class="hljs-keyword">var</span> material = <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial( &#123; <span class="hljs-attr">color</span>: <span class="hljs-number">0x00ff00</span> &#125; );
  <span class="hljs-comment">// Mesh 是一种三角形网格基本单元的构造函数，类似于我们原生 WebGL 中的片元着色器它用于连接几何体和材质</span>
  cube = <span class="hljs-keyword">new</span> THREE.Mesh( geometry, material );
  <span class="hljs-comment">// 最后将创建好的几何立方体添加到场景中</span>
  scene.add(cube);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>到这里我们已经完成了 Three.js 绘制 3D 网页所需的基本配置，当然如果有需要对 3D 网页的明暗效果，灯光颜色做处理的我们还可以在场景中加入灯光的配置，这里由于我们的旋转立方体对于灯光并未有什么特殊的要求，所以我们便直接进入最后一步场景的渲染。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// render 函数提供了浏览器的循环渲染功能</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
  cube.rotation.x += <span class="hljs-number">0.01</span>;
cube.rotation.y += <span class="hljs-number">0.01</span>;
renderer.render(scene, camera);
requestAnimationFrame(render);
&#125;
<span class="hljs-comment">// 最后将 Threee.js 环境初始化，场景创建，相机创建渲染器创建以及渲染初始化等函数合成到一起执行我们就完成了一个旋转立方体的绘制</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">threeStart</span>(<span class="hljs-params"></span>) </span>&#123;
initThree();
initCamera();
initScene();
initObject();
render();
&#125;
<span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'DOMContentLoaded'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  threeStart();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Three.js 的旋转立方体的绘制还需要配合 HTML 文件使用才能看到效果</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../utils/three.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
    <span class="hljs-selector-tag">div</span><span class="hljs-selector-id">#canvas-frame</span> &#123;
      <span class="hljs-attribute">border</span>: none;
      <span class="hljs-attribute">cursor</span>: pointer;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">600px</span>;
      <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#EEEEEE</span>;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvas-frame"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配合 HTML 文件运行上述代码后我们可以在网页中看到，一个旋转的绿色立方体</p>
</li>
</ul>
<h3 data-id="heading-9"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/604b225d1cea41f08853eccc853fa158~tplv-k3u1fbpfcp-watermark.image" alt="cube" loading="lazy" referrerpolicy="no-referrer"></h3>
<h3 data-id="heading-10">小结</h3>
<p>通过对比我们发现尽管我们通过 Three.js 创建了更为复杂的场景，但是代码量相对 WebGL 原生 API 绘制三角形时反而要少了。由此可见对于初学者而言，直接使用 WebGL 原生 API 进行 3D 网页的开发，显然是不合适的。这时候我们就可以借助像 Three.js 这样的 WebGL 封装库进行开发。相较之原生 API 的开发，这类第三方封装好的 WebGL 库大大降低了我们的开发成本，同时也能帮助我们开发出更加炫酷的页面效果。当然也不是说原生 API 不好，毕竟如果有能力学透 WebGL 原生 API 的开发还是能够帮助我们在开发 3D 网页的时候实现更加随心所欲的功能，且 Three.js 本身的文档并不是特别完善所以想要顺利的使用同样需要摸透 WebGL 原生 API。</p>
<h2 data-id="heading-11">总结</h2>
<p>WebGL 技术出现的时间并不算短，然而尽管能够开发出拥有炫酷效果的 3D 网页却一直未能大火，现今应用的最多的也不过是 3D 网页游戏的开发。这其中很大一部分的原因便是受到网速发展的制约，在当今这个快节奏的社会中人们对于网页加载速度的忍耐度是极低的，一个 WebGL 开发的 3D 网页动辄需要三四秒的打开时间对用户而言无疑是极度不友好的。但是相信随着 5G 通信技术的发展，网络通信技术飞速发展下，WebGL 技术的明天可能会迎来新的发展契机。</p>
<h2 data-id="heading-12">推荐阅读</h2>
<p><a href="https://juejin.cn/post/6984547134062198791" target="_blank" title="https://juejin.cn/post/6984547134062198791">最熟悉的陌生人rc-form</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzoo.team%2Farticle%2Fabout-vite" target="_blank" rel="nofollow noopener noreferrer" title="https://zoo.team/article/about-vite" ref="nofollow noopener noreferrer">Vite 特性和部分源码解析</a></p>
<p><a href="https://juejin.cn/post/6974184935804534815" target="_blank" title="https://juejin.cn/post/6974184935804534815">我在工作中是如何使用 git 的</a></p>
<p><a href="https://juejin.cn/post/6987140782595506189" target="_blank" title="https://juejin.cn/post/6987140782595506189">如何搭建适合自己团队的构建部署平台</a></p>
<h2 data-id="heading-13">开源作品</h2>
<ul>
<li>政采云前端小报</li>
</ul>
<p><strong>开源地址 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zoo.team%2Fopenweekly%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zoo.team/openweekly/" ref="nofollow noopener noreferrer">www.zoo.team/openweekly/</a></strong> (小报官网首页有微信交流群)</p>
<h2 data-id="heading-14">招贤纳士</h2>
<p>政采云前端团队（ZooTeam），一个年轻富有激情和创造力的前端团队，隶属于政采云产品研发部，Base 在风景如画的杭州。团队现有 40 余个前端小伙伴，平均年龄 27 岁，近 3 成是全栈工程师，妥妥的青年风暴团。成员构成既有来自于阿里、网易的“老”兵，也有浙大、中科大、杭电等校的应届新人。团队在日常的业务对接之外，还在物料体系、工程平台、搭建平台、性能体验、云端应用、数据分析及可视化等方向进行技术探索和实战，推动并落地了一系列的内部技术产品，持续探索前端技术体系的新边界。</p>
<p>如果你想改变一直被事折腾，希望开始能折腾事；如果你想改变一直被告诫需要多些想法，却无从破局；如果你想改变你有能力去做成那个结果，却不需要你；如果你想改变你想做成的事需要一个团队去支撑，但没你带人的位置；如果你想改变既定的节奏，将会是“5 年工作时间 3 年工作经验”；如果你想改变本来悟性不错，但总是有那一层窗户纸的模糊… 如果你相信相信的力量，相信平凡人能成就非凡事，相信能遇到更好的自己。如果你希望参与到随着业务腾飞的过程，亲手推动一个有着深入的业务理解、完善的技术体系、技术创造价值、影响力外溢的前端团队的成长历程，我觉得我们该聊聊。任何时间，等着你写点什么，发给 <code>ZooTeam@cai-inc.com</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d3aa3d1f8646a8bcda8cfd9e335a4b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            