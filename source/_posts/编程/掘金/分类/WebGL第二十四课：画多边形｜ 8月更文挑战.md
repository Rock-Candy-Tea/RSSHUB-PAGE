
---
title: 'WebGL第二十四课：画多边形｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35be829c0e32460cb78444c5b386e38c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 23:36:24 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35be829c0e32460cb78444c5b386e38c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第10天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<pre><code class="copyable">本文标题：WebGL第二十四课：画多边形｜ 8月更文挑战
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-0">本文的最后代码，用一篇单独的文章给出，需要的小伙伴直接跳：<a href="https://juejin.cn/post/6998041392303833101/" target="_blank" title="https://juejin.cn/post/6998041392303833101/">二十四课代码</a></h1>
<h3 data-id="heading-1">引子</h3>
<p>上一次课，我们用三个点，画出了一个三角形。并且中间填充了黑色（其实是WebGL自行插值的）。</p>
<p>那么这一次课，我们扩展一下，画一个N边形，并且这个N可以通过页面上的一个滑竿来控制，即时生效。</p>
<p>最终的效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35be829c0e32460cb78444c5b386e38c~tplv-k3u1fbpfcp-watermark.image" alt="24-1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们通过上面的动图可以看出，当N边形的边数越来越多，我们画出的图形就越趋向于一个圆。</p>
<p>这正是<code>WebGL</code>如何模拟一些复杂的曲线、曲面的，就是<code>不断的逼近</code>。(要考虑效果和性能，不能把数据点搞太多)</p>
<h3 data-id="heading-2">准备坐标点</h3>
<p>我们用四边形，也就是正方形，来作为例子。</p>
<p>我们先观察一下正方形：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ae274a27d774dc5ad71ad4e5f25ec03~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>正方形有四个顶点，我们通过划分区域，将这个正方形划分成四个小三角形。</p>
<p>而每一个三角形有三个顶点，也就是说，我们需要事先准备 12 个坐标点。</p>
<p>我们先人工的把这十二个点描述出来，如下：</p>
<p>第一个三角形的三个点：OAB</p>
<p>第二个三角形的三个点：OBC</p>
<p>第三个三角形的三个点：OCD</p>
<p>第四个三角形的三个点：ODA</p>
<p>注意，我上面严格遵守了，一定要逆时针这个原则。</p>
<p>后面写代码的时候，也是按照这个顺序来写。</p>
<h3 data-id="heading-3">编写生成N边形坐标点的函数</h3>
<p>我们先写出函数头：</p>
<pre><code class="copyable">function GetPolyN(center, R, N) &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>center</code> ：中心</p>
<p><code>R</code> : 中心到顶点的距离</p>
<p><code>N</code> : 多边形的边数</p>
<p>我们的思维模式就是:</p>
<ul>
<li>
<ol>
<li>将一个圆周 N 等分，找出这N等分的坐标点。</li>
</ol>
</li>
<li>
<ol start="2">
<li>再将这N等分的坐标点，两两一组，与中心点组合，正好就是三个点一组。</li>
</ol>
</li>
<li>
<ol start="3">
<li>将上面的所有坐标点，平坦化</li>
</ol>
</li>
</ul>
<p>根据上面的思路，得出下面的代码：</p>
<pre><code class="copyable">// GetTri 函数在上次课已经讲解过了
function GetTri(A, B, C) &#123;
    return [A[0], A[1], B[0], B[1], C[0], C[1]];
&#125;

// 获得N边形
function GetPolyN(center, R, N) &#123;
    // 1. 先在圆周上，均匀获取 N 个点
    let idx = 0;
    let x = 0;
    let y = 0;
    let rad = 0;
    let pointArr = [];
    for (; idx != N; idx++) &#123;
        rad = ((2 * Math.PI) / N) * idx;
        x = R * Math.cos(rad) + center[0]; // 考虑 中心到顶点的长度  中心
        y = R * Math.sin(rad) + center[1]; // 考虑 中心到顶点的长度  中心
        pointArr.push([x, y]);
    &#125;
    // 2. 将这N个点，每两个一组，与中心，正好是三个点，组成N个三角形
    let res = []; // 平坦化数组
    for (idx = 0; idx != N; idx++) &#123;
        res.push(...GetTri(pointArr[idx], pointArr[(idx + 1) % N], center)); // 注意这里是逆时针排布的
    &#125;
    return res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">页面上加一个滑竿来控制N</h3>
<p>这个属于html的知识，我们只写列出代码如下：</p>
<pre><code class="copyable">    <p>
        <b>N边形:</b>
        <input id="N" type="range" min="3" max="100" value="3" step="1" oninput="updatefunc()" />
        <b id="Nvalue">0</b>
    </p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值得注意的是，我们设置了 min 是3，也就是最小画的就是三角形。最大是100，我们最后会发现100，足以模拟一个圆了。</p>
<h3 data-id="heading-5">buffer 的删除与新建</h3>
<p>这一次课有一点不一样的过程， 那就是当<code>N</code>变化的时候，我们需要重新生成数据点，然后重新在<code>WebGL</code>里生成一个<code>buffer</code>，为了不造成内存泄露，我们还需要将前面的<code>buffer</code>删掉。</p>
<p>也就是说，我们需要将<code>生成buffer，传入数据</code>的代码，挪到<code>updatefunc</code>函数里。</p>
<p>最终的<code>updatefunc</code>如下：</p>
<pre><code class="copyable">        function updatefunc() &#123;
            
            // 这里判断一下，如果以前有buffer，就删掉
            if (buffer_id) &#123;
                gl.deleteBuffer(buffer_id);
            &#125;
            // 生成N边形
            data = GetPolyN([0, 0], 0.5, NDom.value);
            dataArr = new Float32Array(data);
            pointCount = data.length / 2;
            // 重新创建WebGL的buffer，并且将多边形的点传入
            buffer_id = gl.createBuffer();
            gl.bindBuffer(gl.ARRAY_BUFFER, buffer_id);
            gl.bufferData(gl.ARRAY_BUFFER, dataArr, gl.STATIC_DRAW);
            // 指定 data 的格式
            gl.vertexAttribPointer(a_PointVertex, 2, gl.FLOAT, false, 0, 0);
            gl.enableVertexAttribArray(a_PointVertex);

            /*
            ...
            ...
            没有变化的代码
            ...
            ...
            */
            
            gl.clearColor(0, 0, 0, 0);
            gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
            gl.drawArrays(gl.TRIANGLES, 0, pointCount);
        &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">整点花活</h3>
<p>上面确实可以画出多边形了，但是我们还是不确认，是不是由一个一个小三角形组成的。</p>
<p>那不妨这样。我们把小三角形的颜色区分开，一个一个的，用不同的颜色。那就一目了然了。</p>
<h4 data-id="heading-7">思路：</h4>
<p>既然要不同的点，用不同的颜色。那么就必须要把颜色也传入到<code>WebGL</code>的<code>buffer</code>里去了。</p>
<p>这里有两种途径：</p>
<ul>
<li>
<ol>
<li>利用老的buffer，如下</li>
</ol>
</li>
</ul>
<p>[数据点1坐标][数据点1颜色][数据点2坐标][数据点2颜色][数据点3坐标][数据点3颜色]………………</p>
<ul>
<li>
<ol start="2">
<li>新开一个buffer</li>
</ol>
</li>
</ul>
<p>buffer_point(老的buffer):</p>
<p>[数据点1坐标][数据点2坐标][数据点3坐标]………………</p>
<p>buffer_color:</p>
<p>[数据点1颜色][数据点2颜色][数据点3颜色]………………</p>
<p>上面两种办法都行啊，这里我选择第二种办法，也就是不动原有的buffer，而新建一个buffer_color。</p>
<p>我们知道一个数据点，就要对应一个颜色，而一个颜色由RGB三个字段组成。</p>
<p>所以我们在shader里接收的时候，要使用vec3。</p>
<p>这里对比坐标，坐标是xy，只需要vec2。</p>
<h4 data-id="heading-8">vertex_shader 的改动</h4>
<p>在 <code>vertex_shader</code> 中要加一个 <code>attribute</code> 变量 <code>a_PointColor</code>:</p>
<pre><code class="copyable">    attribute vec3 a_PointColor;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了将这个 <code>a_PointColor</code> 传给 <code>fragment_shader</code> ，我们必须再加一个 <code>varying</code> 变量：</p>
<pre><code class="copyable">    attribute vec3 a_PointColor;
    varying vec3 color;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么最终的<code>vertex_shader</code></p>
<pre><code class="copyable">    <script id="vertex_shader" type="myshader">
        // Vertex Shader
        precision mediump int;
        precision mediump float;
        
        uniform mat3 u_all;

        attribute vec2 a_PointVertex;

        attribute vec3 a_PointColor;

        varying vec3 color;

        void main() &#123;
          vec3 coord = u_all * vec3(a_PointVertex, 1.0);
          gl_Position = vec4(coord.x, coord.y, 0.0, 1.0);
          color = a_PointColor;
        &#125;
    </script>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">fragment_shader 的改动</h4>
<p>这个就很简单了，加一个 varying 同名变量 , 然后用这个变量当做颜色就行了：</p>
<pre><code class="copyable">    <script id="fragment_shader" type="myshader">
        // Fragment shader
        precision mediump int;
        precision mediump float;

        varying vec3 color;

        void main() &#123;
        
          gl_FragColor = vec4(color, 1.0);
        &#125;
        
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">针对坐标点数组，生成一个颜色数组</h4>
<p>我们只需要记住，每个坐标点，对应一个颜色，而一个颜色有三个分量RGB就行了：</p>
<pre><code class="copyable">function GetRandomColor(pointCount) &#123;
    let res = [];
    let idx = 0;
    for (; idx != pointCount; idx++) &#123;
        res.push(Math.random());//R
        res.push(Math.random());//G
        res.push(Math.random());//B
    &#125;
    return res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，我们上面的颜色是随机生成的，这样看起来更 <code>花活</code> 一点。</p>
<h4 data-id="heading-11">最终效果</h4>
<p>这里不给出最终的代码，从文章开头的链接，可以直接拿到最终代码。</p>
<p>其实只要将上面所说的，稍微攒一攒，就行了。</p>
<p>最后的花活效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9691d2a50a2d4ad6ba44c797515ed64f~tplv-k3u1fbpfcp-watermark.image" alt="24-2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<hr>
<hr>
<pre><code class="copyable">  正文结束，下面是答疑
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">小丫丫说：我终于看见五颜六色的东西了！</h3>
<ul>
<li>答：花里胡哨的东西！</li>
</ul></div>  
</div>
            