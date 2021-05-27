
---
title: '前端也要懂图形化： 浅谈 WebGL 技术'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13d4fd78045a490a8881150aed3cdc27~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 26 May 2021 05:06:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13d4fd78045a490a8881150aed3cdc27~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">WebGL概述</h1>
<p>WebGL是一项结合了HTML5和JavaScript，用来在网页上绘制和渲染复杂三维图形的技术。WebGL通过JavaScript操作OpenGL接口的标准，把三维空间图像显示在二维的屏幕上。</p>
<h2 data-id="heading-1">WebGL与OpenGL</h2>
<p>OpenGL本身是一套规范，不是API，通过OpenGL来统一各个显卡厂家实现操作图形、图像的实现标准。WebGL的技术规范继承自<strong>OpenGL ES</strong>，从<strong>2.0</strong>版本开始，OpenGL支持可编程着色器方法，这个支持可以让我们通过着色器语言编写着色器程序，代表我们可以精确控制每个像素的位置和颜色。在OpenGL2.0规范中，GPU可以执行着色器程序，根据着色器程序生成像素数据，最终显示在屏幕上。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13d4fd78045a490a8881150aed3cdc27~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">WebGL程序的结构</h2>
<p>相对于传统网页，支持WebGL的浏览器底层接入了OpenGL/OpenGL ES标准，WebGL通过实现标准支持着色器语言编程语言<strong>GLSL ES</strong>，在我们实际开发过程中，GLSL ES通常是以字符串的形式存在JavaScript中，我们可以通过JavaScript修改GLSL ES字符串来改变着色器程序。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5abd68f18e64346ae84563d3ebf4c0c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">着色器</h1>
<p>着色器是WebGL依赖的实现图像渲染的一种绘图机制。WebGL在GPU中运行，因此需要使用能够在GPU上运行的代码，这样的代码需要提供成对的方法，他们分别是<strong>顶点着色器</strong>和<strong>片元着色器</strong>。</p>
<h2 data-id="heading-4">顶点着色器</h2>
<p>顶点着色器的作用是计算顶点的位置，根据计算出的一系列顶点位置，WebGL可以对点， 线和三角形在内的一些图元进行光栅化处理。WebGL中显示的物体由一系列顶点组成，每个顶点都有位置和颜色等信息，在默认的情况下，所有像素的颜色都由线性插值计算得来，自动形成平滑渐变。</p>
<p>下面是顶点着色器的示例代码，顶点着色器通过<code>a_Position</code>、<code>a_PointSize</code>分别接收并设置顶点的位置和大小，通过<code>a_Color</code>从程序获取颜色并通过<code>v_Color</code>传递给片元着色器。其中，<strong>gl_Position</strong>和<strong>gl_PointSize</strong>是着色器的内置变量，分别代表顶点的位置和大小，因此这段代码的作用是设置顶点的位置和大小，同时接收程序传入的颜色<code>a_Color</code>并把它传递给片元着色器。</p>
<p>在着色器内，一般命名以<code>gl_</code>开头的变量是着色器的内置变量，除此之外<code>webgl_</code>和<code>_webgl</code>还是着色器保留字，自定义变量不能以<code>webgl_</code>或<code>_webgl</code>开头。变量声明一般包含<<em>存储限定符</em>><数据<em>类型</em>><<em>变量名称</em>>，以<code>attribute vec4 a_Position</code>为例，<code>attribute</code>表示存储限定符，<code>vec</code>是数据类型，<code>a_Position</code>为变量名称。</p>
<pre><code class="copyable">const vs_source = `

    attribute vec4 a_Position;

    attribute float a_PointSize;

    attribute vec4 a_Color;

    varying vec4 v_Color;

    void main() &#123;

        gl_Position = a_Position;

        gl_PointSize = a_PointSize;

        v_Color = a_Color;

    &#125;

`;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">片元着色器</h2>
<p>片元着色器的作用是计算出当前绘制图元中每个像素的颜色值，逐片元控制片元的颜色和纹理等渲染。关于片元，片元包含颜色、深度和纹理等信息，片元相对像素多出许多信息，从直观表现上看两者都是像素点。关于图元，图元是指WebGL中可以直接绘制7种基本图形，它们分别是：</p>
<ul>
<li>孤立点：<code>gl.POINTS</code></li>
<li>孤立线段：<code>gl.LINES</code></li>
<li>连续线段：<code>gl.LINE_STRIP</code></li>
<li>连续线圈：<code>gl.LINE_LOOP</code></li>
<li>孤立三角形：<code>gl.TRIANGLES</code></li>
<li>三角带：<code>gl.TRIANGLE_STRIP</code></li>
<li>三角扇：<code>gl.TRIANGLE_FAN</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61a08bbed837454fb834400f890f44f7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20a958fc25ab424a86678ff3c70bb049~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/097a985ea86b45afbd7ef5170fd0a94e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d36c7a457674b819be7a62594e328e2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a7dfeb62a1447e39933abc3fb26513b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbf0e83a28a94df8a3dd5bd4975f5c7e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59bf345871ae4b7283b1928ad55de29d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面是片元着色器的示例代码，首先设置了<code>float</code>为中等精度，然后通过<code>v_Color</code>接收来自顶点着色器的颜色并将其设置给内置变量<strong>gl_FragColor</strong>，其中通过内置变量<strong>gl_FragColor</strong>来确定顶点像素颜色。</p>
<p>关于精度可以详见<a href="https://blog.csdn.net/u014291990/article/details/103173077" target="_blank" rel="nofollow noopener noreferrer">WebGL着色器精度设置</a>。</p>
<pre><code class="copyable">const fs_source = `

    precision mediump float;

    varying vec4 v_Color;

    void main() &#123;

        gl_FragColor = v_Color;

    &#125;

`;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">存储限定符</h1>
<p>在上面例子中，我们在声明变量时，除了指定变量类型外，还使用了存储限定符。在GLSL中，应该根据变量用途使用存储限定符修饰。一般常用到三种存储限定符：</p>
<h2 data-id="heading-7">attribute 属性</h2>
<p>attribute只能用于顶点着色器，用来存储顶点着色器中每个顶点的输入，包括顶点位置坐标、纹理坐标和颜色等信息。</p>
<p>通常情况下我们会使用缓冲，缓冲是程序发送给GPU的数据，attribute用来从缓冲中获取所需数据，并将它提供给顶点着色器。程序可以指定每次顶点着色器运行时读取缓冲的规则。</p>
<h3 data-id="heading-8">使用缓冲设置顶点信息</h3>
<p>生成缓冲代码</p>
<pre><code class="copyable">// 创建缓冲对象

const vertexBuffer = gl.createBuffer();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将数据写入缓冲</p>
<pre><code class="copyable">// 缓冲数据

const vertices = new Float32Array([

 -0.5, 0.5, 10.0, 1.0, 0.0, 0.0, 1.0,

 -0.5, -0.5, 20.0, 0.0, 1.0, 0.0, 1.0,

 0.5, 0.5, 30.0, 0.0, 0.0, 1.0, 1.0

]);

// 绑定缓冲对象

gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);

// 将缓冲数据填充缓冲对象

gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置缓冲读取规则和启用缓冲对象</p>
<pre><code class="copyable"> // 调用顶点缓冲，将缓冲数据中一组7个数据中的前2个数据传给a_Position

 gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, SIZE * 7, 0);

 // 调用顶点缓冲，将缓冲数据中一组7个数据中的第3（偏移2个数据取1一个）个数据传给a_PointSize

 gl.vertexAttribPointer(a_PointSize, 1, gl.FLOAT, false, SIZE * 7, SIZE * 2);

 // 调用顶点缓冲，将缓冲数据中一组7个数据中的第4-7（偏移3个数据取4个）个数据传给a_Color

 gl.vertexAttribPointer(a_Color, 4, gl.FLOAT, false, SIZE * 7, SIZE * 3);

 // 激活a_Position使用缓冲数组，下同

 gl.enableVertexAttribArray(a_Position);

 gl.enableVertexAttribArray(a_PointSize);

 gl.enableVertexAttribArray(a_Color);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">uniform 全局变量</h2>
<p>uniform可以存在顶点着色器和片元着色器，用来存储图元处理过程中保持不变的值，例如颜色。值得一提的是，顶点着色器和片元着色器共享了 uniform 变量的命名空间，如果在顶点着色器和片段着色器中都声明了同名 uniform 变量，二者声明的类型和着色器的精度必须一致。</p>
<h2 data-id="heading-10">varying 可变量</h2>
<p>varying一般同时存在顶点着色器和片元着色器中，它的作用是从顶点着色器向片元着色器传输数据，在图元装配后，WegGL会对图元光栅化，在光栅化过程中，varying声明的变量的值会进行内插，使varying变量的值线性（默认）变化。</p>
<h1 data-id="heading-11">一个简单的例子：彩色三角形</h1>
<p>在这段代码中，指定三角形的三个点，分别位于画布的左上角、左下角和右上角，他们的颜色分别为红色、绿色和蓝色，大家可以运行示例代码查看效果。</p>
<pre><code class="copyable">// 顶点着色器

const vs_source = `

  attribute vec4 a_Position;

  attribute float a_PointSize;

  attribute vec4 a_Color;

  varying vec4 v_Color;

  void main() &#123;

    gl_Position = a_Position;

    gl_PointSize = a_PointSize;

    v_Color = a_Color;

  &#125;

`;

 

// 片元着色器

const fs_source = `

  precision mediump float;

  varying vec4 v_Color;

  void main() &#123;

    gl_FragColor = v_Color;

  &#125;

`;

 const canvas = document.getElementById('app');

 const gl = canvas.getContext('webgl');

 

 function initShader() &#123;

   // 创建shader

   const vs_shader = gl.createShader(gl.VERTEX_SHADER);

   gl.shaderSource(vs_shader, vs_source);

   gl.compileShader(vs_shader);

   if (!gl.getShaderParameter(vs_shader, gl.COMPILE_STATUS)) &#123;

     const error = gl.getShaderInfoLog(vs_shader);

     console.log('Failed to compile vs_shader:' + error);

     gl.deleteShader(vs_shader);

     return;

   &#125;

   const fs_shader = gl.createShader(gl.FRAGMENT_SHADER);

   gl.shaderSource(fs_shader, fs_source);

   gl.compileShader(fs_shader);

   if (!gl.getShaderParameter(fs_shader, gl.COMPILE_STATUS)) &#123;

     const error = gl.getShaderInfoLog(fs_shader);

     console.log('Failed to compile fs_shader:' + error);

     gl.deleteShader(fs_shader);

     return;

   &#125;

   // 创建program

   const program = gl.createProgram();

   gl.attachShader(program, vs_shader);

   gl.attachShader(program, fs_shader);

   gl.linkProgram(program);

   if (!gl.getProgramParameter(program, gl.LINK_STATUS)) &#123;

     const error = gl.getProgramInfoLog(program);

     console.log('无法链接程序对象：' + error);

     gl.deleteProgram(program);

     gl.deleteShader(fs_shader);

     gl.deleteShader(vs_shader);

     return;

   &#125;

   gl.useProgram(program);

   gl.program = program;

   // 获取着色器变量位置和赋值

   const a_Position = gl.getAttribLocation(gl.program, 'a_Position');

   if (a_Position < 0) &#123;

     console.log('Failed to get the storage location of a_Position');

     return;

   &#125;

   const a_Color = gl.getAttribLocation(gl.program, 'a_Color');

   if (a_Color < 0) &#123;

     console.log('Failed to get the storage location of a_Color');

     return;

   &#125;

   // 使用缓冲区表示多个值

  const vertices = new Float32Array([

    -0.5, 0.5, 1.0, 0.0, 0.0, 1.0,

    -0.5, -0.5, 0.0, 1.0, 0.0, 1.0,

    0.5, 0.5, 0.0, 0.0, 1.0, 1.0

  ])

  const SIZE = vertices.BYTES_PER_ELEMENT;

   const vertexBuffer = gl.createBuffer();

   gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);

   gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

   gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, SIZE * 6, 0);

   gl.vertexAttribPointer(a_Color, 4, gl.FLOAT, false, SIZE * 6, SIZE * 2);

   gl.enableVertexAttribArray(a_Position);

   gl.enableVertexAttribArray(a_Color);

 &#125;

 initShader();

 

 gl.clearColor(0.0, 0.0, 0.0, 1.0);

 gl.clear(gl.COLOR_BUFFER_BIT);

 

 gl.drawArrays(gl.TRIANGLES, 0, 3);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们分别只设置了三个点的颜色，但是渲染出来的图形却是彩色的三角形，造成这样的结果的原因是因为<code>v_Color</code>在传递的过程中经过了内插。以左上角点和右上角点对比，代表<code>rgb</code>颜色三个值线性向目标值变化，内插过程将颜色分配给光栅化后每个片元（像素）颜色，造成了颜色渐变。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25ed7899eb03423d9a698d70c199c200~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/437825c048044d0ea020f33f11993d8c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-12">WebGL渲染过程</h1>
<p>以上面例子为例，三角形的有3个点，需要执行3次顶点着色器，把3个点位置存储在图形装配区域。顶点着色器执行完毕后，三个点的坐标都已经处在图形装配区，开始装配图形，由于我们设置的是<code>gl.TRIANGLES</code>，图形装配出一个三角形。随后会进行光栅化，将装配好的图像转化成片元组合，也就是像素点，varying变量的插值也在这一过程中进行。光栅化后，程序调用片元着色器，假定光栅化后有10个片元，那么片元着色器将执行10次，每次调用处理一个片元，片元着色器计算该片元的颜色并写入颜色缓冲区，当最后一个片元被处理完成，浏览器就会显示出最终的结果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cd6459fce1c4024ab0ad0e99ab8be50~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-13">图片渲染</h1>
<p>通过顶点信息绘制像素点功能很强大，但对于复杂图形不够好用，通常我们需要渲染图片，这样就需要纹理映射了，这就是为什么在WebGL中，我们更倾向把图片描述为纹理的原因。</p>
<h2 data-id="heading-14">纹理映射</h2>
<p>纹理映射原理很简单，就是将一张图片映射到一个几何图形的表面。由于在WebGL中，WebGL能直接绘制的图形只有点、线和三角形，因此在纹理映射中，图片被映射到由两个三角形组成的矩形。</p>
<p>纹理映射具体步骤：</p>
<ol>
<li>准备映射的纹理图图像，纹理图像应该满足2的幂次方</li>
</ol>
<p>图片分辨率为非2的幂次方（104 * 104），图片不能被渲染，并提示图片分辨率可能不是2的幂次方</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/059f8fd6d44643f2b07c7126620f0f1c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图片分辨率为2的幂次方（256 * 256），正常显示</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47f9a76d84954d1ca0d0cdb939cf6585~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>为几何图形配置映射方式，顶点坐标和纹理坐标对应，需要注意，构建顺序与新增顶点的奇偶性相关。（假设v0代表第一个顶点</li>
</ol>
<ul>
<li>如果新增顶点时奇数，顶点排列顺序为：T = [n-1 n-2 n]；</li>
<li>如果新增顶点为偶数，顶点排列顺序为：T = [n-2 n-1 n]；</li>
</ul>
<p>下面顶点组成的三角形分别为：T1 = [v0, v1, v2]，T2 = [v2, v1, v3]</p>
<pre><code class="copyable">  // 顶点坐标、纹理坐标，绘制顺序：左上->左下->右上->右下

  const vertices = new Float32Array([

    -0.5, 0.5, 0.0, 1.0,   // v0

    -0.5, -0.5, 0.0, 0.0,  // v1

    0.5, 0.5, 1.0, 1.0,    // v2

    0.5, -0.5, 1.0, 0.0,   // v3

  ]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当把第一个坐标和第二个坐标互换时，绘制</p>
<pre><code class="copyable">  // 顶点坐标、纹理坐标，绘制顺序：左下->左上->右上->右下

  const vertices = new Float32Array([

    -0.5, -0.5, 0.0, 0.0,  // v0

    -0.5, 0.5, 0.0, 1.0,   // v1

    0.5, 0.5, 1.0, 1.0,    // v2

    0.5, -0.5, 1.0, 0.0,   // v3

  ]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c868499331d476d85be06ac2262f493~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>
<p>加载纹理图像，对其进行一些配置，以在WebGL中使用，分别有如下操作</p>
<ol>
<li>创建纹理对象</li>
<li>图片Y轴反转，因为图片坐标系y轴垂直向下，而纹理坐标系（st坐标系）t轴垂直向上，在我们的例子中，顶点坐标和纹理坐标是相反的，所以在纹理存储像素中需要对y轴翻转</li>
</ol>
</li>
</ol>
<p>假如未未进行y轴反转</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba5c1cb10e1a46469e2442a6b6b50b07~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>
<p>激活指定纹理单元</p>
</li>
<li>
<p>绑定纹理对象到纹理单元</p>
</li>
<li>
<p>设置纹理过滤，纹理过滤是指，当绘制范围（顶点坐标组成的矩形区域）与纹理本身大小不匹配时，如何获取纹理颜色。需要注意的是，设置错误的过滤可能会导致渲染失败</p>
<ol>
<li><code>gl.TEXTURE_MAP_FILTER</code>放大方法，纹理撑满至绘制范围</li>
<li><code>gl.TEXTURE_MIN_FILTER</code>缩小方法，纹理缩小至绘制范围</li>
<li><code>gl.TEXTURE_WRAP_S</code>水平填充，纹理大小不变，左右填充</li>
<li><code>gl.TEXTURE_WRAP_T</code>垂直填充，纹理大小不变，上下填充</li>
</ol>
</li>
</ol>
<p>过滤设置错误，假如画布大小400 * 400，顶点坐标范围-0.5～0.5对应大小200 * 200，图片大小256 * 256，纹理比绘制范围大，但是过滤仅设置了<code>gl.TEXTURE_MAG_FILTER</code>，获取纹理颜色失败，控制台又输出了熟悉的错误：图片不能被渲染，是否未设置合适纹理过滤</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5c3a59d87334c2b80d5b2494b5b4a8e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15ffaa7c47c44205a12934f73148ea06~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="6">
<li>将图像绑定到纹理</li>
<li>将纹理单元传递给着色器中的采样器</li>
</ol>

<ol start="4">
<li>在片元着色器中将相应的像素从纹理中抽取出来，并将像素的颜色赋给片元</li>
</ol>
<p>以上操作相关的代码片段如下</p>
<pre><code class="copyable">// 顶点着色器

 const vs_source = `

   attribute vec4 a_Position;

   attribute vec2 a_TexCoord;

   varying vec2 v_TexCoord;

   void main() &#123;

    gl_Position = a_Position;

    v_TexCoord = a_TexCoord;

   &#125;

`;

 

 // 片元着色器

const fs_source = `

  precision mediump float;

  uniform sampler2D u_Sampler;

  varying vec2 v_TexCoord;

  void main() &#123;

    gl_FragColor = texture2D(u_Sampler, v_TexCoord);

  &#125;

`;



...



function initShader() &#123;

  ...

  

  // 顶点坐标和纹理坐标

  const vertices = new Float32Array([

    -0.5, 0.5, 0.0, 1.0,

    -0.5, -0.5, 0.0, 0.0,

    0.5, 0.5, 1.0, 1.0,

    0.5, -0.5, 1.0, 0.0,

  ]);

   

  ...

&#125;



const texture = gl.createTexture();

const u_Sample = gl.getUniformLocation(gl.program, 'u_Sample');

 

const img = new Image();

img.onload = function () &#123;

  // 加载纹理图像，对其进行一些配置，以在WebGL中使用

  // 纹理像素存储y轴反转

  gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, 1);

  // 激活纹理单元0

  gl.activeTexture(gl.TEXTURE0);

  // 绑定纹理

  gl.bindTexture(gl.TEXTURE_2D, texture);

  // 设置过滤的过滤方式，这里仅设置了gl.TEXTURE_MIN_FILTER，也可以设置多种过滤

  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);

  // 生成纹理

  gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, gl.RGB, gl.UNSIGNED_BYTE, img);

  // 将纹理单元0传递给采样器

  gl.uniform1i(u_Sample, 0);

 

  gl.clearColor(0.0, 1.0, 0.0, 1.0);

  gl.clear(gl.COLOR_BUFFER_BIT);

  

  // 绘图顺序跟点有关

  gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);

&#125;

img.src = 'power-of-2-image';
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">❤️ 谢谢支持</h2>
<p>以上便是本次分享的全部内容，希望对你有所帮助^_^</p>
<p>喜欢的话别忘了 <strong>分享、点赞、收藏</strong> 三连哦~。</p>
<p>欢迎关注公众号 <strong>ELab团队</strong> 收货大厂一手好文章~</p>
<blockquote>
<p>我们来自字节跳动，是旗下大力教育前端部门，负责字节跳动教育全线产品前端开发工作。</p>
<p>我们围绕产品品质提升、开发效率、创意与前沿技术等方向沉淀与传播专业知识及案例，为业界贡献经验价值。包括但不限于性能监控、组件库、多端技术、Serverless、可视化搭建、音视频、人工智能、产品设计与营销等内容。</p>
<p>欢迎感兴趣的同学在评论区拍砖 🤪</p>
</blockquote></div>  
</div>
            