
---
title: 'webgl变换：深入图形平移'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/Users/bytedance/writing_script/%E7%9F%A5%E4%B9%8E%E5%86%99%E4%BD%9C/webgl/img/webgl%E5%8F%98%E6%8D%A2%EF%BC%9A%E6%B7%B1%E5%85%A5%E5%9B%BE%E5%BD%A2%E5%B9%B3%E7%A7%BB/%E5%9B%BE%E8%A7%A3.png'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 01:46:18 GMT
thumbnail: 'https://juejin.cn/Users/bytedance/writing_script/%E7%9F%A5%E4%B9%8E%E5%86%99%E4%BD%9C/webgl/img/webgl%E5%8F%98%E6%8D%A2%EF%BC%9A%E6%B7%B1%E5%85%A5%E5%9B%BE%E5%BD%A2%E5%B9%B3%E7%A7%BB/%E5%9B%BE%E8%A7%A3.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在以前的文章里，不管是绘制图形，绘制点亦或者是改变色值，所有的内容都是静态的。</p>
<p>在 <code>webgl</code> 里，图形的运动分为 <code>平移、旋转、缩放</code> 三种类型。</p>
<p>接下来，我们会从零基础开始，一点一点来深入了解图形如何进行运动。</p>
<p>首先来从零开始了解下图形的平移</p>
<h2 data-id="heading-0">1. 图形平移</h2>
<p>首先我们来看如何实现图形的平移操作。</p>
<p>平移的操作就是将<strong>图形的原始坐标</strong>加上对应的移动距离。首先来看下平移的实现</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vertexShaderSource = <span class="hljs-string">""</span> +
      <span class="hljs-string">"attribute vec4 apos;"</span> + <span class="hljs-comment">// 定义一个坐标</span>
      <span class="hljs-string">"uniform float x;"</span> + <span class="hljs-comment">// 处理 x 轴移动</span>
      <span class="hljs-string">"uniform float y;"</span> + <span class="hljs-comment">// 处理 y 轴移动</span>
      <span class="hljs-string">"void main()&#123;"</span> +
      <span class="hljs-string">" gl_Position.x = apos.x + x;"</span> +
      <span class="hljs-string">" gl_Position.y = apos.y + y;"</span> +
      <span class="hljs-string">" gl_Position.z = 0.0;"</span> + <span class="hljs-comment">// z轴固定</span>
      <span class="hljs-string">" gl_Position.w = 1.0;"</span> +
      <span class="hljs-string">"&#125;"</span>;
<span class="hljs-keyword">const</span> fragmentShaderSource = <span class="hljs-string">""</span> +
      <span class="hljs-string">"void main()&#123;"</span> +
      <span class="hljs-string">" gl_FragColor = vec4(1.0,0.0,0.0,1.0);"</span> +
      <span class="hljs-string">"&#125;"</span>;

<span class="hljs-comment">// initShader已经实现了很多次，本次就不再赘述了</span>
<span class="hljs-keyword">const</span> program = initShader(gl,vertexShaderSource,fragmentShaderSource);

<span class="hljs-keyword">const</span> buffer = gl.createBuffer();
<span class="hljs-keyword">const</span> data = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>([
  <span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,
  -<span class="hljs-number">0.5</span>,-<span class="hljs-number">0.5</span>,
  <span class="hljs-number">0.5</span>,-<span class="hljs-number">0.5</span>,
]);

gl.bindBuffer(gl.ARRAY_BUFFER,buffer);
gl.bufferData(gl.ARRAY_BUFFER,data,gl.STATIC_DRAW);

<span class="hljs-keyword">const</span> aposlocation = gl.getAttribLocation(program,<span class="hljs-string">'apos'</span>);
<span class="hljs-keyword">const</span> xlocation = gl.getUniformLocation(program,<span class="hljs-string">'x'</span>);
<span class="hljs-keyword">const</span> ylocation = gl.getUniformLocation(program,<span class="hljs-string">'y'</span>);

gl.vertexAttribPointer(aposlocation,<span class="hljs-number">2</span>,gl.FLOAT,<span class="hljs-literal">false</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>);
gl.enableVertexAttribArray(aposlocation);

<span class="hljs-keyword">let</span> x = <span class="hljs-number">0.0</span>;
<span class="hljs-keyword">let</span> y = <span class="hljs-number">0.0</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span> (<span class="hljs-params"></span>) </span>&#123;
  gl.uniform1f(xlocation,x += <span class="hljs-number">0.01</span>);
  gl.uniform1f(ylocation,y += <span class="hljs-number">0.01</span>);

  gl.drawArrays(gl.TRIANGLES,<span class="hljs-number">0</span>,<span class="hljs-number">3</span>);
  <span class="hljs-comment">// 使用此方法实现一个动画</span>
  requestAnimationFrame(run)
&#125;
run()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解释：</p>
<ul>
<li>首先声明一个变量 <code>x</code> 和变量 <code>y</code>  ，用来处理 x轴 和 y轴 的坐标。<strong>这里使用的是 <code>uniform</code></strong> 变量，因为平移的操作对于图形上的所有顶点都有影响。</li>
<li>通过 <code>gl_Position.[xyzw]</code> 来分别设置 <code>x、y、z、w</code> 的值。用于改变图形位置。</li>
<li>使用 <code>gl.uniform1f</code> 来为 x 和 y 赋值</li>
<li>使用 <code>requestAnimationFrame</code> 实现一个缓动动画。方便观察效果。</li>
<li>其他的操作，缓冲区，绘制，赋值，激活，</li>
</ul>
<p>可以看到，这样处理图形移动的话很好理解，但是因为一个移动，我们声明了两个 <code>uniform</code> 变量来实现。并且分开设置的 <code>xyz</code> 坐标，非常的不方便。</p>
<p>所以，在处理<code>webgl</code>变换（平移、缩放、旋转）的时候，通常使用<strong>矩阵</strong>来实现。接下来就来看看，如何使用矩阵实现图形的平移。</p>
<h2 data-id="heading-1">2. 平移矩阵</h2>
<p>推导平移矩阵的步骤：</p>
<ul>
<li>获取平移前后的图形坐标（三维）</li>
<li>计算平移前后的差值</li>
<li>带入到平移矩阵</li>
<li>处理图形顶点</li>
<li>获得平移后的图形</li>
</ul>
<h3 data-id="heading-2">2.1 平移矩阵的推导</h3>
<p>首先让我们来看一幅图片。</p>
<p><img src="https://juejin.cn/Users/bytedance/writing_script/%E7%9F%A5%E4%B9%8E%E5%86%99%E4%BD%9C/webgl/img/webgl%E5%8F%98%E6%8D%A2%EF%BC%9A%E6%B7%B1%E5%85%A5%E5%9B%BE%E5%BD%A2%E5%B9%B3%E7%A7%BB/%E5%9B%BE%E8%A7%A3.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这幅图片的意义就是我们将<strong>橙色的三角形</strong>移动到<strong>蓝色虚线三角形</strong>处。</p>
<p>移动之后的<strong>蓝色虚线三角形</strong>的三个坐标分别为</p>
<ul>
<li><code>x’ = x + x1</code></li>
<li><code>y' = y + y1</code></li>
<li><code>z' = z + z1</code></li>
<li><code>w=1</code> 齐次坐标为1</li>
</ul>
<h3 data-id="heading-3">2.2 获得平移矩阵</h3>
<p>在 <code>webgl</code> 中，通常使用<strong>矩阵</strong>来实现图形变换。下面我们来看看矩阵如何表示。</p>
<p><img src="https://juejin.cn/Users/bytedance/writing_script/%E5%86%99%E4%BD%9C%E6%96%87%E7%AB%A0/webgl/img/webgl%E5%8F%98%E6%8D%A2%EF%BC%9A%E6%B7%B1%E5%85%A5%E5%9B%BE%E5%BD%A2%E5%B9%B3%E7%A7%BB/%E5%B9%B3%E7%A7%BB%E7%9F%A9%E9%98%B5.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>左侧是平移之前的原始坐标，中间的是一个平移矩阵，经过两者相乘，可以得到一个平移之后的坐标。</p>
<p>现在我们来看下<strong>平移矩阵</strong>如何计算得出</p>
<p>首先通过上述图片中的矩阵我们来得到几个方程式。用左侧的列分别乘矩阵的行，可以得到一下公式</p>
<ul>
<li><code>ax + by + cz + w = x'</code></li>
<li><code>ex + fy + gz + h = y'</code></li>
<li><code>ix + jy + kz + l = z'</code></li>
<li><code>mx + ny + oz + p = w'</code></li>
</ul>
<p>公式合并：</p>
<p>将<strong>第一节</strong> 里的四个方程式和<strong>第二节</strong>里的四个方程式合并，可以得到如下结果：</p>
<ul>
<li><code>ax + by + cz + w = x + x1'</code>：只有当 <code>a = 1，b = c = 0, w = x1</code> 的时候，等式左右两边成立</li>
<li><code>ex + fy + gz + h = y + y1'</code>：只有当 <code>f = 1, e = g = 0, h = y1</code> 的时候，等式左右两边成立</li>
<li><code>ix + jy + kz + l = z + z1'</code>：只有当 <code>k = 1,i = j = 0, l = z1</code> 的时候，等式左右两边成立</li>
<li><code>mx + ny + oz + p = 1'</code>：只有当 <code>m = n = o = 0, p = 1</code> 的时候，等式左右两边成立</li>
</ul>
<p>经过上述方程式，可以得到一个平移的矩阵：</p>
<blockquote>
<p>| 1 0 0 x |</p>
<p>| 0 1 0 y |</p>
<p>| 0 0 1 z |</p>
<p>| 0 0 0 1 |</p>
</blockquote>
<p>之后将平移矩阵和原始坐标相乘，就可以得到平移之后的坐标。</p>
<h2 data-id="heading-4">3. 矩阵实战</h2>
<p>来看看使用矩阵如何处理图形的平移。</p>
<h5 data-id="heading-5">第一步，创建着色器源代码</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vertexShaderSource = <span class="hljs-string">""</span> +
      <span class="hljs-string">"attribute vec4 apos;"</span> +
      <span class="hljs-string">"uniform mat4 mat;"</span> + <span class="hljs-comment">// 创建一个 uniform 变量，代表平移矩阵</span>
      <span class="hljs-string">"void main()&#123;"</span> +
      <span class="hljs-string">" gl_Position = mat * apos;"</span> + <span class="hljs-comment">// 矩阵与原始坐标相乘</span>
      <span class="hljs-string">"&#125;"</span>;
<span class="hljs-keyword">const</span> fragmentShaderSource = <span class="hljs-string">""</span> +
      <span class="hljs-string">"void main()&#123;"</span> +
      <span class="hljs-string">" gl_FragColor = vec4(1.0,0.0,0.0,1.0);"</span> +
      <span class="hljs-string">"&#125;"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">第二步，创建平移矩阵</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> Tx = <span class="hljs-number">0.1</span>;    <span class="hljs-comment">//x坐标的位置</span>
<span class="hljs-keyword">let</span> Ty = <span class="hljs-number">0.1</span>;    <span class="hljs-comment">//y坐标的位置</span>
<span class="hljs-keyword">let</span> Tz = <span class="hljs-number">0.0</span>;    <span class="hljs-comment">//z坐标的位置</span>
<span class="hljs-keyword">let</span> Tw = <span class="hljs-number">1.0</span>;    <span class="hljs-comment">//差值</span>
<span class="hljs-keyword">const</span> mat = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>([
  <span class="hljs-number">1.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,
  <span class="hljs-number">0.0</span>,<span class="hljs-number">1.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,
  <span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">1.0</span>,<span class="hljs-number">0.0</span>,
  Tx,Ty,Tz,Tw,
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里可以看到，使用的矩阵和我们推导出来的矩阵不太一样，推导的平移矩阵里 <code>xyzw</code> 位于矩阵的右侧，现在是位于矩阵的底部，这是为什么呢？</p>
<p>这是因为在 <code>webgl</code> 中，矩阵的使用需要按照 <strong>左上右下</strong> 的对角线做一次翻转。所以使用的矩阵，<code>xyzw</code> 位于底部</p>
<h5 data-id="heading-7">第三步，绘制一个三角形</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> program = initShader(gl,vertexShaderSource,fragmentShaderSource);
<span class="hljs-keyword">const</span> aposlocation = gl.getAttribLocation(program,<span class="hljs-string">'apos'</span>);
<span class="hljs-keyword">const</span> data =  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>([
  <span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,
  -<span class="hljs-number">.3</span>,-<span class="hljs-number">.3</span>,
  <span class="hljs-number">.3</span>,-<span class="hljs-number">.3</span>
]);

<span class="hljs-keyword">const</span> buffer = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER,buffer);
gl.bufferData(gl.ARRAY_BUFFER,data,gl.STATIC_DRAW);

gl.vertexAttribPointer(aposlocation,<span class="hljs-number">2</span>,gl.FLOAT,<span class="hljs-literal">false</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>);
gl.enableVertexAttribArray(aposlocation);

gl.drawArrays(gl.TRIANGLES,<span class="hljs-number">0</span>,<span class="hljs-number">3</span>); <span class="hljs-comment">// 第五步的时候会重写</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">第四步，获取矩阵变量，给矩阵赋值</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> matlocation = gl.getUniformLocation(program,<span class="hljs-string">'mat'</span>);
gl.uniformMatrix4fv(matlocation,<span class="hljs-literal">false</span>,mat);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里使用 <code>gl.uniformMatrix4fv</code> 来给矩阵赋值。</p>
<h5 data-id="heading-9">第五步，添加缓动动画</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span> (<span class="hljs-params"></span>) </span>&#123;
  Tx += <span class="hljs-number">0.01</span>
  Ty += <span class="hljs-number">0.01</span>
  <span class="hljs-keyword">const</span> mat = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>([
    <span class="hljs-number">1.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,
    <span class="hljs-number">0.0</span>,<span class="hljs-number">1.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,
    <span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">1.0</span>,<span class="hljs-number">0.0</span>,
    Tx,Ty,Tz,Tw,
  ]);
  gl.uniformMatrix4fv(matlocation,<span class="hljs-literal">false</span>,mat);
  gl.drawArrays(gl.TRIANGLES,<span class="hljs-number">0</span>,<span class="hljs-number">3</span>);

  <span class="hljs-comment">// 使用此方法实现一个动画</span>
  requestAnimationFrame(run)
&#125;
run()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">4. 完整代码</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"webgl"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"500"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"500"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> gl = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'webgl'</span>).getContext(<span class="hljs-string">'webgl'</span>);
  <span class="hljs-keyword">const</span> vertexShaderSource = <span class="hljs-string">""</span> +
    <span class="hljs-string">"attribute vec4 apos;"</span> +
    <span class="hljs-string">"uniform mat4 mat;"</span> +
    <span class="hljs-string">"void main()&#123;"</span> +
    <span class="hljs-string">" gl_Position = mat * apos;"</span> +
    <span class="hljs-string">"&#125;"</span>;
  <span class="hljs-keyword">const</span> fragmentShaderSource = <span class="hljs-string">""</span> +
    <span class="hljs-string">"void main()&#123;"</span> +
    <span class="hljs-string">" gl_FragColor = vec4(1.0,0.0,0.0,1.0);"</span> +
    <span class="hljs-string">"&#125;"</span>;

  <span class="hljs-keyword">const</span> program = initShader(gl,vertexShaderSource,fragmentShaderSource);
  <span class="hljs-keyword">const</span> aposlocation = gl.getAttribLocation(program,<span class="hljs-string">'apos'</span>);
  <span class="hljs-keyword">const</span> matlocation = gl.getUniformLocation(program,<span class="hljs-string">'mat'</span>);

  <span class="hljs-keyword">const</span> data =  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>([
    <span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,
    -<span class="hljs-number">.3</span>,-<span class="hljs-number">.3</span>,
    <span class="hljs-number">.3</span>,-<span class="hljs-number">.3</span>
  ]);
  <span class="hljs-keyword">const</span> buffer = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER,buffer);
  gl.bufferData(gl.ARRAY_BUFFER,data,gl.STATIC_DRAW);

  gl.vertexAttribPointer(aposlocation,<span class="hljs-number">2</span>,gl.FLOAT,<span class="hljs-literal">false</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>);
  gl.enableVertexAttribArray(aposlocation);

  <span class="hljs-keyword">let</span> Tx = <span class="hljs-number">0.1</span>;    <span class="hljs-comment">//x坐标的位置</span>
  <span class="hljs-keyword">let</span> Ty = <span class="hljs-number">0.1</span>;    <span class="hljs-comment">//y坐标的位置</span>
  <span class="hljs-keyword">let</span> Tz = <span class="hljs-number">0.0</span>;    <span class="hljs-comment">//z坐标的位置</span>
  <span class="hljs-keyword">let</span> Tw = <span class="hljs-number">1.0</span>;    <span class="hljs-comment">//差值</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span> (<span class="hljs-params"></span>) </span>&#123;
    Tx += <span class="hljs-number">0.01</span>
    Ty += <span class="hljs-number">0.01</span>
    <span class="hljs-keyword">const</span> mat = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>([
      <span class="hljs-number">1.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,
      <span class="hljs-number">0.0</span>,<span class="hljs-number">1.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,
      <span class="hljs-number">0.0</span>,<span class="hljs-number">0.0</span>,<span class="hljs-number">1.0</span>,<span class="hljs-number">0.0</span>,
      Tx,Ty,Tz,Tw,
    ]);
    gl.uniformMatrix4fv(matlocation,<span class="hljs-literal">false</span>,mat);
    gl.drawArrays(gl.TRIANGLES,<span class="hljs-number">0</span>,<span class="hljs-number">3</span>);

    <span class="hljs-comment">// 使用此方法实现一个动画</span>
    requestAnimationFrame(run)
  &#125;
  run()
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initShader</span>(<span class="hljs-params">gl,vertexShaderSource,fragmentShaderSource</span>)</span>&#123;
    <span class="hljs-keyword">const</span> vertexShader = gl.createShader(gl.VERTEX_SHADER);
    <span class="hljs-keyword">const</span> fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);

    gl.shaderSource(vertexShader,vertexShaderSource);
    gl.shaderSource(fragmentShader,fragmentShaderSource);

    gl.compileShader(vertexShader);
    gl.compileShader(fragmentShader);

    <span class="hljs-keyword">const</span> program = gl.createProgram();

    gl.attachShader(program,vertexShader);
    gl.attachShader(program,fragmentShader)

    gl.linkProgram(program);
    gl.useProgram(program);
    <span class="hljs-keyword">return</span> program;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，通过矩阵控制图形移动就全部实现完成了。</p>
<p>今天的分享就到这儿了，</p>
<p>Bye~</p>
<hr>
<p>数据平台前端团队，在公司内负责多款大数据相关产品的研发。我们在前端技术上保持着非常强的热情，除了数据产品相关的研发外，在数据可视化、海量数据处理优化、web excel、WebIDE、私有化部署、工程工具都方面都有很多的探索和积累，欢迎投递简历！</p></div>  
</div>
            