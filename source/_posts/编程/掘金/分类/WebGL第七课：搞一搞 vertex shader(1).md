
---
title: 'WebGL第七课：搞一搞 vertex shader(1)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2ec6b9c86934cefb6906cbf265b150f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 00:52:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2ec6b9c86934cefb6906cbf265b150f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><pre><code class="copyable">本文标题：WebGL第七课：搞一搞 vertex shader(1)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在接下来的几次课里，我们将通过几个实例，来熟悉 <code>vertex shader</code> 的各种用法。</p>
<ol>
<li>我们将用 1000 个点，来绘制我们的图形。</li>
<li>我们的代码模板给出如下：</li>
</ol>
<pre><code class="copyable">
<!doctype html>
<html>

<head>
    <style>
        canvas &#123;
            border: 1px solid #000000;
        &#125;
    </style>

</head>

<body>
    <input id="slider" type="range" min="0" max="100" value="50" step="1" οnchange="sliderfunc()" />

    <canvas id="point" style="width:300px; height:300px">
    </canvas>
    <script id="vertex_shader" type="myshader">
        // Vertex Shader
        precision mediump int;
        precision mediump float;
        
        uniform float u_x_offset;
        attribute vec2 a_PointVertex;
        
        void main() &#123;
          gl_Position = vec4(a_PointVertex, 0.0, 1.0);
          gl_Position.y = sin(gl_Position.x * 3.14);
          if ( fract(gl_Position.x * 100.0) < 0.5)
          &#123;
            gl_Position.y = gl_Position.x;
          &#125;
          gl_Position.x = gl_Position.x + u_x_offset;
          gl_PointSize = 3.0;
        &#125;
    </script>
    <script id="fragment_shader" type="myshader">
        // Fragment shader
        precision mediump int;
        precision mediump float;
        
        void main() &#123;
          gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);
        &#125;
        
    </script>
    <script type="text/javascript">
        var pointCanvas = document.getElementById('point'); // 我们的纸
        var gl = pointCanvas.getContext('webgl', &#123; preserveDrawingBuffer: true &#125;); // 我们的笔
        var pointCount = 0;
        var pointData = [];
        for (var idx = -500; idx <= 500; idx++) &#123;
            pointCount++;
            pointData.push(idx / 500);
            pointData.push(0);
        &#125;
        //
        var pointArray = new Float32Array(pointData);
        var buffer_id;
        buffer_id = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, buffer_id);
        gl.bufferData(gl.ARRAY_BUFFER, pointArray, gl.STATIC_DRAW);
        //
        var vertex_shader_code = document.getElementById('vertex_shader').textContent;
        console.log(vertex_shader_code);
        var vertex_shader = gl.createShader(gl.VERTEX_SHADER);
        gl.shaderSource(vertex_shader, vertex_shader_code);
        gl.compileShader(vertex_shader);
        //
        var fragment_shader_code = document.getElementById('fragment_shader').textContent;
        var fragment_shader = gl.createShader(gl.FRAGMENT_SHADER);
        gl.shaderSource(fragment_shader, fragment_shader_code);
        gl.compileShader(fragment_shader);
        //
        var program = gl.createProgram();
        gl.attachShader(program, vertex_shader);
        gl.attachShader(program, fragment_shader);
        gl.linkProgram(program);
        gl.useProgram(program);
        //
        var a_PointVertex = gl.getAttribLocation(program, 'a_PointVertex');
        gl.vertexAttribPointer(a_PointVertex, 2, gl.FLOAT, false, 0, 0);
        gl.enableVertexAttribArray(a_PointVertex);
        //
        // gl.drawArrays(gl.POINTS, 0, pointCount);
    </script>
    <script>
        var u_x_offset_loc = gl.getUniformLocation(program, "u_x_offset");

        var sliderDom = document.getElementById("slider");
        function sliderfunc() &#123;
            console.log("___________________", u_x_offset_loc, typeof sliderDom.value, sliderDom.value);
            gl.uniform1f(u_x_offset_loc, parseFloat(sliderDom.value) / 100);
            gl.clearColor(0, 0, 0, 0);
            gl.clear(gl.COLOR_BUFFER_BIT);
            gl.drawArrays(gl.POINTS, 0, pointCount);
        &#125;
        sliderDom.addEventListener("change", sliderfunc);
    </script>
    </script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>我们的重点在上述代码的 这一部分, 也就是 <code>vertex shader</code> 部分 ：</li>
</ol>
<pre><code class="copyable">    <script id="vertex_shader" type="myshader">
        // Vertex Shader
        precision mediump int;
        precision mediump float;
        
        attribute vec2 a_PointVertex;
        
        void main() &#123;
          gl_Position = vec4(a_PointVertex, 0.0, 1.0);
          gl_PointSize = 3.0;
        &#125;
    </script>

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-0">第一个例子: 绘制 sin 正弦图像</h5>
<ul>
<li>我们准备的数据点有1000个，这些点的横坐标，从 -1 到 1</li>
<li>纵坐标都是0</li>
</ul>
<p>那么按到里讲，绘制的东西是一根横的直线，在屏幕中间<br>
我们在浏览器里打开这个页面，结果也确实如此：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2ec6b9c86934cefb6906cbf265b150f~tplv-k3u1fbpfcp-watermark.image" alt="7-1.png" loading="lazy" referrerpolicy="no-referrer"><br>
根据 正弦函数式子：<br>
<code>y = sin (x)</code></p>
<p>我们改动我们的 <code>vertex shader</code>, 如下:</p>
<pre><code class="copyable">    <script id="vertex_shader" type="myshader">
        // Vertex Shader
        precision mediump int;
        precision mediump float;
        
        attribute vec2 a_PointVertex;
        
        void main() &#123;
          gl_Position = vec4(a_PointVertex, 0.0, 1.0);
          gl_Position.y = sin(gl_Position.x);
          gl_PointSize = 3.0;
        &#125;
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>刷新一下页面，结果如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3888b8d608d344569391b8d9fd5604cf~tplv-k3u1fbpfcp-watermark.image" alt="7-2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们发现上图不怎么完美，因为并没有完整显示一个周期之内的正弦<br>
原因就是因为我们的 x 的范围是 -1---1 之间，这不够一个周期的<br>
一个周期应该是 -π --- +π 之间。<br>
那这样来变一下代码：</p>
<pre><code class="copyable">    <script id="vertex_shader" type="myshader">
        // Vertex Shader
        precision mediump int;
        precision mediump float;
        
        attribute vec2 a_PointVertex;
        
        void main() &#123;
          gl_Position = vec4(a_PointVertex, 0.0, 1.0);
          gl_Position.y = sin(gl_Position.x * 3.14);
          gl_PointSize = 3.0;
        &#125;
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>刷新一下页面，结果如下，这样就好看多了:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3da13f96b9c743f6ba542a041e4cfb8a~tplv-k3u1fbpfcp-watermark.image" alt="7-3.png" loading="lazy" referrerpolicy="no-referrer"><br>
太棒了，我们可以用<code>webgl</code>来绘制函数图形了，多好玩啊~</p>
<p>我要画两个周期的 sin 图像：</p>
<pre><code class="copyable">    <script id="vertex_shader" type="myshader">
        // Vertex Shader
        precision mediump int;
        precision mediump float;
        
        attribute vec2 a_PointVertex;
        
        void main() &#123;
          gl_Position = vec4(a_PointVertex, 0.0, 1.0);
          gl_Position.y = sin(gl_Position.x * 3.14 * 2.0);
          gl_PointSize = 3.0;
        &#125;
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是的，我们成功了：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a78c6f8dd91d4b7c9b1ebb177e887c39~tplv-k3u1fbpfcp-watermark.image" alt="7-4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们来搞一些奇怪的东西，比如说，我们的代码怎么改动，能绘制下面的图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cdb74457247447698643e12d76722ed~tplv-k3u1fbpfcp-watermark.image" alt="7-6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们发现，在图的左半边，好像图形往中间压缩了一半。<br>
线索：</p>
<ol>
<li>图的左半边：(<code>x<0</code>)</li>
<li>压缩一半 ：( <code>y = y * 0.5</code>)</li>
</ol>
<p>我们将上面的线索，更换成相应的代码如下：</p>
<pre><code class="copyable"><script id="vertex_shader" type="myshader">
      // Vertex Shader
      precision mediump int;
      precision mediump float;
      
      attribute vec2 a_PointVertex;
      
      void main() &#123;
        gl_Position = vec4(a_PointVertex, 0.0, 1.0);
        gl_Position.y = sin(gl_Position.x * 3.14 * 2.0);
        if (gl_Position.x < 0.0)
        &#123;
          gl_Position.y = gl_Position.y * 0.5;
        &#125;
        gl_PointSize = 3.0;
      &#125;
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还是两个周期的图像，不过，代码里写了，如果 <code>x<0</code> , <code>y</code> 就变成一半，很容易理解！</p>
<h5 data-id="heading-1">第二个例子: 同时绘制 <code>一条直线</code> 和 <code>sin</code> 图像</h5>
<p>就像下图这样：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55d2452ab5464fbeacfb16ef821f3a71~tplv-k3u1fbpfcp-watermark.image" alt="7-7.png" loading="lazy" referrerpolicy="no-referrer"><br>
有读者脑子里就在想了，简单：<br>
我在外面绘制两次，就是用 <code>gl.drawArrays</code>,绘制两次图像，事先准备好两个 <code>vertex shader</code>。<br>
结果是：行，你这么搞是可以的，我不会说任何反对的话，但是我再加一个限制，</p>
<ol>
<li>
<p>只准有一个<code>vertex shader</code>,</p>
</li>
<li>
<p>只准用一次<code>gl.drawArrays</code>。</p>
</li>
<li>
<p>而且不准改外面的生成数据的代码，我们只能改 <code>vertex shader</code> 代码！！！</p>
</li>
</ol>
<p>思路：
我们有<code>1000</code>个点，我们交叉绘制上面两个图形不就行了吗！！！<br>
比如说，奇数下标的绘制<code>sin</code>图像，偶数下标的绘制<code>直线</code>。</p>
<p>问题来了，我们能在vertex shader 里获取下标吗？？？？？
<code>显然不能。</code><br>
我们只能在<code>x</code>本身上下手，我们列一下最左边的几个<code>x</code>:<br>
-1.000, -0.998, -0.996, -0.994, -0.992, -0.990 ……<br>
我们将上面的数全部乘以 100就会得到下面的数：<br>
-100.0, -99.8, -99.6, -99.4, -99.2, -99<br>
我们再把小数部分保留，去掉整数部分：<br>
0,       0.8,    0.6,  0.4,    0.2 , 0<br>
我们发现，除了0之外，两个<code>小于0.5</code>的，两个<code>大于0.5</code>的<br>
那我们就按照这个来交叉，代码如下：</p>
<pre><code class="copyable"><script id="vertex_shader" type="myshader">
        // Vertex Shader
        precision mediump int;
        precision mediump float;
        
        attribute vec2 a_PointVertex;
        
        void main() &#123;
          gl_Position = vec4(a_PointVertex, 0.0, 1.0);
          gl_Position.y = sin(gl_Position.x * 3.14);
          if ( fract(gl_Position.x * 100.0) < 0.5)
          &#123;
            gl_Position.y = gl_Position.x;
          &#125;
          gl_PointSize = 3.0;
        &#125;
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>刷新页面，图像出来了！！成功！！</p>
<hr>
<hr>
<hr>
<pre><code class="copyable">正文结束，下面是答疑
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">小瓜瓜说：天真热，瓜真好吃，不过图形也是真好看。。。。。。</h5></div>  
</div>
            