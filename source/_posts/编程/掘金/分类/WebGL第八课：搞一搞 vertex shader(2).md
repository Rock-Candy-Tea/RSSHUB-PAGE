
---
title: 'WebGL第八课：搞一搞 vertex shader(2)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f3393c3ba3d4f19b5d6ef2957e27fc9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 01:47:09 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f3393c3ba3d4f19b5d6ef2957e27fc9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><pre><code class="copyable">本文标题：WebGL第八课：搞一搞 vertex shader(2)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上次课，我们一开始画了一个周期的sin函数，然后画了两个周期的sin函数。<br>
不过，我们是直接改的 <code>vertex shader</code> 代码。<br>
如果我们在网页里，能通过一个滑竿(slider)来拖动改变，然后反应到图形里就好了。</p>
<p>根据上面的需求，我们先在网页里加一个，slider input 控件，<br>
整个代码改动如下：</p>
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
        
        attribute vec2 a_PointVertex;
        
        void main() &#123;
          gl_Position = vec4(a_PointVertex, 0.0, 1.0);
          gl_Position.y = sin(gl_Position.x * 3.14);
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
        var sliderDom = document.getElementById("slider");
        function sliderfunc() &#123;
        &#125;
        sliderDom.addEventListener("change", sliderfunc);
    </script>
    </script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在前面，加了一个 slider input 控件，在最后将这个控件绑定了一个事件，也就是<br>
这个控件的值改变的时候，我们可以在 <code>sliderfunc</code> 函数中做一些事情。</p>
<pre><code class="copyable">var sliderDom = document.getElementById("slider");
function sliderfunc() &#123;
    // 应该在这里来改变图形的绘制
&#125;
sliderDom.addEventListener("change", sliderfunc);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-0">重点新概念：uniform 变量</h5>
<ul>
<li><code>uniform</code> 变量是可以写在 <code>vertex shader</code> 和 <code>fragment shader</code> 中的变量</li>
<li>随时都可以通过<code>gl</code>的<code>api</code>，改变<code>uniform</code>变量的值</li>
</ul>
<p>我们改动我们的 <code>vertex shader</code>, 如下:</p>
<pre><code class="copyable">    <script id="vertex_shader" type="myshader">
        // Vertex Shader
        precision mediump int;
        precision mediump float;
        uniform float u_x_offset;
        
        attribute vec2 a_PointVertex;
        
        void main() &#123;
          gl_Position = vec4(a_PointVertex, 0.0, 1.0);
          gl_Position.y = sin(gl_Position.x * 3.14 * u_x_offset);
          gl_PointSize = 3.0;
        &#125;
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>注意，声明了一个 <code>float</code> 类型的 <code>uniform</code> 变量 <code>u_x_offset</code>;</li>
<li>注意，sin 的传入参数，变成了 <code>gl_Position.x * 3.14 * u_x_offset</code></li>
<li>也就是说，我们可以把 <code>u_x_offset</code> 当做一个调节因子.</li>
</ul>
<p>光这些还没用，我们要在 sliderfunc 里写一些代码，来从外面改变 <code>vertex shader</code> 中的 <code>u_x_offset</code>变量。</p>
<p>最后的代码改动如下：</p>
<pre><code class="copyable">    <script>
        var u_x_offset_loc = gl.getUniformLocation(program, "u_x_offset");

        var sliderDom = document.getElementById("slider");
        function sliderfunc() &#123;
            gl.uniform1f(u_x_offset_loc, parseFloat(sliderDom.value) / 10);
            gl.clearColor(0, 0, 0, 0);
            gl.clear(gl.COLOR_BUFFER_BIT);
            gl.drawArrays(gl.POINTS, 0, pointCount);
        &#125;
        sliderDom.addEventListener("change", sliderfunc);
    </script>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>详解：</p>
<ul>
<li>gl.getUniformLocation ， 用于得到 <code>vertex shader</code> 中的 uniform 变量的位置</li>
<li>gl.uniform1f             改变 <code>vertex shader</code>中的 uniform变量的值</li>
<li>gl.clear(gl.COLOR_BUFFER_BIT) 清空整个图像 ，否则会重复绘制，越来越乱</li>
<li>gl.drawArrays(gl.POINTS, 0, pointCount) 重新绘制</li>
</ul>
<p>效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f3393c3ba3d4f19b5d6ef2957e27fc9~tplv-k3u1fbpfcp-watermark.image" alt="8-1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d25a24e501c94deaa4e304f0e526cf71~tplv-k3u1fbpfcp-watermark.image" alt="8-2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>随着我们拖动滑竿，不同周期的<code>sin</code>图像会被绘制到页面上。</p>
<hr>
<hr>
<hr>
<pre><code class="copyable">正文结束，下面是答疑
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-1">小鸭鸭说：既然可以在 js 代码改变 uniform 变量的值，那么我搞个定时器，是不是就是动画了？</h5>
<ul>
<li>答：完全正确✔️！！！！！下课~</li>
</ul></div>  
</div>
            