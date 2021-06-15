
---
title: 'WebGL基本图形三角形的绘制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3f70648d09c4daeba07531a8834b1a9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 06:23:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3f70648d09c4daeba07531a8834b1a9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>三角形的绘制比点的绘制多对多一个步骤。那就是三角形需要创建缓冲区。有以下几种绘制三角形的方法。
三种绘制方式的代码几乎是一样的。只是在进行渲染时<code>drawArrays(type,start,count)</code>中的<code>type</code>不一样。</p>
<p>以下例子主要用到以下<code>GLSL</code>知识。</p>
<pre><code class="hljs language-js copyable" lang="js">gl.createBuffer：创建buffer。
gl.bindBuffer：绑定某个缓冲区对象为当前缓冲区。
gl.bufferData：往缓冲区中复制数据。
gl.enableVertexAttribArray：启用顶点属性。
gl.vertexAttribPointer：设置顶点属性从缓冲区中读取数据的方式。
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>顶点着色器代码</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><script id=<span class="hljs-string">"vertexShader"</span> type=<span class="hljs-string">"x-shader/x-vertex"</span>>
  <span class="hljs-comment">//attribute声明vec4类型变量apos</span>
  attribute vec4 apos;
  <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">//顶点坐标apos赋值给内置变量gl_Position</span>
    <span class="hljs-comment">//逐顶点处理数据</span>
    gl_Position = apos;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>片元着色器代码</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><script id=<span class="hljs-string">"fragmentShader"</span> type=<span class="hljs-string">"x-shader/x-fragment"</span>>
  <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 逐片元处理数据，所有片元(像素)设置为红色</span>
    gl_FragColor = vec4(<span class="hljs-number">1.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">1.0</span>);
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>javascript代码,主要由以下4部分代码构成
<ul>
<li>获取<code>WebGL</code>上下文</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//通过getElementById()方法获取canvas画布</span>
<span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'webgl'</span>);
<span class="hljs-comment">//通过方法getContext()获取WebGL上下文</span>
<span class="hljs-keyword">const</span> gl = canvas.getContext(<span class="hljs-string">'webgl'</span>);
<span class="hljs-comment">//初始化着色器</span>
<span class="hljs-keyword">const</span> program = initShader(gl);
<span class="hljs-comment">//初始化缓存区</span>
<span class="hljs-keyword">const</span> count = initBuffer(gl);
render(gl, program, count);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>声明初始化着色器函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//声明初始化着色器函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initShader</span>(<span class="hljs-params">gl</span>) </span>&#123;
    <span class="hljs-comment">//顶点着色器源码</span>
    <span class="hljs-keyword">const</span> vertexShaderSource = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'vertexShader'</span>).innerText;
    <span class="hljs-comment">//片元着色器源码</span>
    <span class="hljs-keyword">const</span> fragmentShaderSource = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'fragmentShader'</span>).innerText;
    <span class="hljs-keyword">const</span> vertexShader = gl.createShader(gl.VERTEX_SHADER);
    <span class="hljs-keyword">const</span> fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
    gl.shaderSource(vertexShader, vertexShaderSource);
    gl.shaderSource(fragmentShader, fragmentShaderSource);
    gl.compileShader(vertexShader);
    gl.compileShader(fragmentShader);
    <span class="hljs-keyword">const</span> program = gl.createProgram();
    gl.attachShader(program, vertexShader);
    gl.attachShader(program, fragmentShader);
    gl.linkProgram(program);
    gl.useProgram(program);
    <span class="hljs-keyword">return</span> program;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>初始化缓冲数据</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//初始化缓冲数据</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initBuffer</span>(<span class="hljs-params">gl</span>) </span>&#123;
    <span class="hljs-comment">//类型数组构造函数Float32Array创建顶点数组</span>
    <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>([
    -<span class="hljs-number">0.5</span>, <span class="hljs-number">0.5</span>,
    -<span class="hljs-number">0.5</span>, -<span class="hljs-number">0.5</span>,
    <span class="hljs-number">0.5</span>, <span class="hljs-number">0.5</span>,
    ]);

    <span class="hljs-comment">//创建缓冲区对象</span>
    <span class="hljs-keyword">var</span> buffer = gl.createBuffer();
    <span class="hljs-comment">//绑定缓冲区对象,激活buffer</span>
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    <span class="hljs-comment">//顶点数组data数据传入缓冲区</span>
    gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW);
    <span class="hljs-keyword">return</span> data.length;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>渲染</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">gl, program, count</span>) </span>&#123;
    <span class="hljs-comment">//获取顶点着色器的位置变量apos，即aposLocation指向apos变量。</span>
    <span class="hljs-keyword">const</span> aposLocation = gl.getAttribLocation(program, <span class="hljs-string">'apos'</span>);

    <span class="hljs-comment">//缓冲区中的数据按照一定的规律传递给位置变量apos</span>
    gl.vertexAttribPointer(aposLocation, <span class="hljs-number">2</span>, gl.FLOAT, <span class="hljs-literal">false</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
    <span class="hljs-comment">//允许数据传递</span>
    gl.enableVertexAttribArray(aposLocation);
    <span class="hljs-comment">//设置清屏颜色为黑色。</span>
    gl.clearColor(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1.0</span>);
    <span class="hljs-comment">//清屏</span>
    gl.clear(gl.COLOR_BUFFER_BIT);
    <span class="hljs-comment">//开始绘制图形</span>
    gl.drawArrays(gl.TRIANGLES, <span class="hljs-number">0</span>, count);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-0">1、常规方式</h4>
<pre><code class="hljs language-js copyable" lang="js">gl.drawArrays(gl.TRIANGLES, <span class="hljs-number">0</span>, <span class="hljs-number">3</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2、三角形带</h4>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3f70648d09c4daeba07531a8834b1a9~tplv-k3u1fbpfcp-watermark.image" width="300" loading="lazy" referrerpolicy="no-referrer">
<p>绘制三角形的数量 = 顶点数 - 2</p>
<pre><code class="hljs language-js copyable" lang="js"> gl.drawArrays(gl.TRIANGLE_STRIP, <span class="hljs-number">0</span>, <span class="hljs-number">3</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3、三角形扇</h4>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61893ad7bf684f8a95393ba1547ec844~tplv-k3u1fbpfcp-watermark.image" width="300" loading="lazy" referrerpolicy="no-referrer">
<p>绘制三角形的数量 = 顶点数 - 2</p>
<pre><code class="hljs language-js copyable" lang="js"> gl.drawArrays(gl.TRIANGLE_FAN, <span class="hljs-number">0</span>, <span class="hljs-number">3</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">4、动态绘制三角形</h4>
<p>着色器中的代码跟动态绘制点的代码几乎是一样的。只是多了一个颜色插值的处理。</p>
<ul>
<li>顶点着色器代码</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><script type=<span class="hljs-string">"shader-source"</span> id=<span class="hljs-string">"vertexShader"</span>>
    <span class="hljs-comment">//浮点数设置为中等精度</span>
    precision mediump float;
    <span class="hljs-comment">//接收 JavaScript 传递过来的点的坐标（X, Y）</span>
    attribute vec2 a_Position;
    attribute vec4 a_Color;
    varying vec4 v_Color;
    <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 最终的顶点坐标。</span>
        gl_Position = vec4(a_Position, <span class="hljs-number">0.0</span>, <span class="hljs-number">1.0</span>);
        <span class="hljs-comment">//进行颜色插值计算</span>
        v_Color = a_Color;
    &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>片元着色器代码</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><script type=<span class="hljs-string">"shader-source"</span> id=<span class="hljs-string">"fragmentShader"</span>>
    <span class="hljs-comment">//浮点数设置为中等精度</span>
    precision mediump float;
    <span class="hljs-comment">// 用来接收顶点着色器插值后的颜色。</span>
    varying vec4 v_Color;
    <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 点的最终颜色。</span>
        gl_FragColor =  v_Color;
    &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>javascript代码
<ul>
<li><code>WebGL</code>上下文的获取</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//通过getElementById()方法获取canvas画布</span>
<span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'webgl'</span>);
<span class="hljs-comment">//设置canvas尺寸为满屏</span>
<span class="hljs-comment">//注意设置canvas的尺寸必须在获取WebGL上下文之前调用</span>
resizeCanvas(canvas);
<span class="hljs-comment">//通过方法getContext()获取WebGL上下文</span>
<span class="hljs-keyword">const</span> gl = canvas.getContext(<span class="hljs-string">'webgl'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>canvas</code>的尺寸动态设置</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//设置canvas的大小</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resizeCanvas</span>(<span class="hljs-params">canvas, width, height</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (canvas.width !== width) &#123;
        canvas.width = width ? width : <span class="hljs-built_in">window</span>.innerWidth;
    &#125;
    <span class="hljs-keyword">if</span> (canvas.height !== height) &#123;
        canvas.height = height ? height : <span class="hljs-built_in">window</span>.innerHeight;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>着色器中的变量赋值处理</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">assignValue</span>(<span class="hljs-params">gl,program</span>)</span>&#123;
    <span class="hljs-keyword">let</span> a_Position = gl.getAttribLocation(program, <span class="hljs-string">'a_Position'</span>);
    <span class="hljs-keyword">let</span> a_Color = gl.getAttribLocation(program, <span class="hljs-string">'a_Color'</span>);
    gl.enableVertexAttribArray(a_Position);
    gl.enableVertexAttribArray(a_Color);
    <span class="hljs-keyword">let</span> buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    <span class="hljs-comment">//将缓冲区中的数据按照一定规律传递给a_Position,表示从缓存区中获取两个浮点型数据(浮点型数据，4个字节)，缓存区一行为4*6个字节，偏移量为0</span>
    gl.vertexAttribPointer(a_Position, <span class="hljs-number">2</span>, gl.FLOAT, <span class="hljs-literal">false</span>, <span class="hljs-number">4</span>*<span class="hljs-number">6</span>, <span class="hljs-number">0</span>);
    gl.vertexAttribPointer(a_Color, <span class="hljs-number">4</span>, gl.FLOAT, <span class="hljs-literal">false</span>,<span class="hljs-number">4</span>*<span class="hljs-number">6</span>, <span class="hljs-number">8</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>点击事件监听</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> positions = [];
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initClick</span>(<span class="hljs-params"></span>) </span>&#123;  
    canvas.addEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
        <span class="hljs-keyword">const</span> color = randomColor();
        <span class="hljs-keyword">const</span> position = coordTransform(e.pageX, e.pageY)
        positions.push(...position, ...Object.values(color));
        <span class="hljs-comment">// 顶点信息为 18 的整数倍即3个顶点时执行绘制操作，因为三角形由三个顶点组成，每个顶点由六个元素组成。</span>
        <span class="hljs-keyword">if</span> (positions.length % <span class="hljs-number">18</span> == <span class="hljs-number">0</span>) &#123;
            <span class="hljs-comment">// gl.bindBuffer(gl.ARRAY_BUFFER, buffer);</span>
            gl.bufferData(gl.ARRAY_BUFFER, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>(positions), gl.STATIC_DRAW);
            render(gl);
        &#125;
    &#125;)
&#125;
<span class="hljs-comment">//颜色值的随机生成</span>
<span class="hljs-keyword">const</span> random = <span class="hljs-built_in">Math</span>.random;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">randomColor</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">r</span>: random(),
        <span class="hljs-attr">g</span>: random(),
        <span class="hljs-attr">b</span>: random(),
        <span class="hljs-attr">a</span>: random()
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>声明初始化着色器函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//声明初始化着色器函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initShader</span>(<span class="hljs-params">gl</span>) </span>&#123;
    <span class="hljs-comment">//顶点着色器源码</span>
    <span class="hljs-keyword">const</span> vertexShaderSource = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'vertexShader'</span>).innerText;
    <span class="hljs-comment">//片元着色器源码</span>
    <span class="hljs-keyword">const</span> fragmentShaderSource = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'fragmentShader'</span>).innerText;
    <span class="hljs-keyword">const</span> vertexShader = gl.createShader(gl.VERTEX_SHADER);
    <span class="hljs-keyword">const</span> fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
    gl.shaderSource(vertexShader, vertexShaderSource);
    gl.shaderSource(fragmentShader, fragmentShaderSource);
    gl.compileShader(vertexShader);
    gl.compileShader(fragmentShader);
    <span class="hljs-keyword">const</span> program = gl.createProgram();
    gl.attachShader(program, vertexShader);
    gl.attachShader(program, fragmentShader);
    gl.linkProgram(program);
    gl.useProgram(program);
    <span class="hljs-keyword">return</span> program;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>屏幕坐标换算成裁剪坐标系(顶点着色器)的坐标</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//屏幕坐标换算成裁剪坐标系的坐标(在着色器中的坐标)</span>
<span class="hljs-keyword">const</span> &#123; width, height &#125; = canvas;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">coordTransform</span>(<span class="hljs-params">x, y</span>) </span>&#123;
    <span class="hljs-comment">// 将 canvas 的坐标值 转换为 [-1.0, 1.0]的范围。</span>
    <span class="hljs-keyword">const</span> posisionX = <span class="hljs-number">2</span> * x / width - <span class="hljs-number">1</span>;
    <span class="hljs-comment">// canvas的 Y 轴坐标方向和 裁剪坐标系的相反。</span>
    <span class="hljs-keyword">const</span> positionY = -(<span class="hljs-number">2</span> * y / height - <span class="hljs-number">1</span>);
    <span class="hljs-keyword">return</span> [posisionX, positionY];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>WebGL</code>渲染</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">gl</span>) </span>&#123;
    <span class="hljs-comment">//设置清屏颜色为黑色。</span>
    gl.clearColor(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>);
    gl.clear(gl.COLOR_BUFFER_BIT);
    <span class="hljs-keyword">if</span> (positions.length > <span class="hljs-number">0</span>) &#123;
        gl.drawArrays(gl.TRIANGLES, <span class="hljs-number">0</span>, positions.length / <span class="hljs-number">6</span>);
    &#125;
&#125;
<span class="hljs-comment">//创建着色器程序</span>
<span class="hljs-keyword">const</span> program = initShader(gl);
constassignValue(gl,program)
initClick();
render(gl);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><strong>参考</strong></p>
<p><a href="http://www.yanhuangxueyuan.com/WebGL/" target="_blank" rel="nofollow noopener noreferrer">WebGL零基础入门教程(郭隆邦)</a>;<br>
<a href="https://juejin.cn/book/6844733755580481543/section/6844733755916025869" target="_blank">WebGL 入门与实践</a><br>
<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/WebGLRenderingContext/vertexAttribPointer" target="_blank" rel="nofollow noopener noreferrer">WebGL官方文档</a></p></div>  
</div>
            