
---
title: 'WebGL第二十六课：贴图代码实战｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e427ac7c8d847c4a8371df5dc4c5493~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 23:48:56 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e427ac7c8d847c4a8371df5dc4c5493~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<pre><code class="copyable">本文标题：WebGL第二十六课：贴图代码实战｜ 8月更文挑战
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-0">友情提示</h3>
<p>这篇文章是<a href="https://juejin.cn/column/6988039774393073694" target="_blank" title="https://juejin.cn/column/6988039774393073694">WebGL课程专栏</a>的第26篇，强烈建议从前面开始看起。因为花了大量的工夫来讲解向量的概念和矩阵运算。这些基础知识会影响你的思维。</p>
<h3 data-id="heading-1">本课代码直接跳转获取：<a href="https://juejin.cn/post/6999899791513780260/" target="_blank" title="https://juejin.cn/post/6999899791513780260/">二十六课代码</a></h3>
<h3 data-id="heading-2">引子</h3>
<p>我们需要预备的概念：</p>
<ul>
<li>我们传入WebGL的是一个一个的顶点信息， 包含(坐标， 颜色， UV，其他等等)</li>
<li>对于<code>画三角形模式</code>来说，WebGL每画三个点之后，就在这三个点内部，进行插值，计算出三个点内部的坐标，颜色，UV</li>
<li>然后根据计算出来的插值，对三个点内部进行填充颜色，或者根据UV进行图片采样</li>
</ul>
<p>上面的内容是在上一次课进行讲解的，不清楚的小伙伴先去上一次课了解一下更好。</p>
<h3 data-id="heading-3">创建一个目录</h3>
<p>我们本次要搞贴图，所以我们创建一个目录</p>
<pre><code class="copyable">images
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后把你需要的图片放到这个目录里面，我的图片名字叫 <code>funny-cat.jpeg</code>, 是一张猫的图片：</p>
<pre><code class="copyable">images/funny-cat.jpeg
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e427ac7c8d847c4a8371df5dc4c5493~tplv-k3u1fbpfcp-watermark.image" alt="funny-cat.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">前端js拉取图片</h3>
<p>这里不难，主要就注意一点，拉取图片是一个<code>异步过程</code>。</p>
<p>我们一定要在拉取图片完成之后，再把数据传入到<code>WebGL</code>，否则就出不来图片，并且会报错。</p>
<p>代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> image = <span class="hljs-keyword">new</span> Image();
image.src = <span class="hljs-string">"images/funny-cat.jpeg"</span>; <span class="hljs-comment">// 这里改成你自己的图片</span>
image.addEventListener(<span class="hljs-string">'load'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 加载完成之后，这个函数会被调用</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">将图片数据传入WebGL</h3>
<p>这里没什么可以讲的，基本过程：</p>
<ul>
<li>
<ol>
<li>在 WebGL 里创建一个 贴图存储区。</li>
</ol>
</li>
<li>
<ol start="2">
<li>将 WebGL 这个状态机切换到这个贴图存储区。</li>
</ol>
</li>
<li>
<ol start="3">
<li>将刚才拉取的图片数据，传给WebGL。</li>
</ol>
</li>
</ul>
<p>代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// 在 WebGL 里创建一个 texture</span>
    <span class="hljs-keyword">let</span> texture = gl.createTexture();
    <span class="hljs-comment">// 切换状态机到当前 texture</span>
    gl.bindTexture(gl.TEXTURE_2D, texture);
    <span class="hljs-comment">//</span>
    gl.texImage2D(gl.TEXTURE_2D, <span class="hljs-number">0</span>, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">综合上面两个过程</h3>
<p>由于拉取图片成功，是用异步回调函数的形式给出的，所以代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> images_loaing_progress = <span class="hljs-number">0</span>; <span class="hljs-comment">// 搞一个变量，用来记录图片是否已经加载完成</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CreateTextureAndLoadImage</span>(<span class="hljs-params">gl</span>) </span>&#123;
    <span class="hljs-comment">// 在 WebGL 里创建一个 texture</span>
    <span class="hljs-keyword">let</span> texture = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, texture);

    <span class="hljs-comment">// 异步加载一张图片，存进刚刚创建好的 texture 里</span>
    <span class="hljs-keyword">var</span> image = <span class="hljs-keyword">new</span> Image();
    image.src = <span class="hljs-string">"images/funny-cat.jpeg"</span>;
    image.addEventListener(<span class="hljs-string">'load'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        gl.bindTexture(gl.TEXTURE_2D, texture);
        gl.texImage2D(gl.TEXTURE_2D, <span class="hljs-number">0</span>, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
        images_loaing_progress = <span class="hljs-number">100</span>;
    &#125;);
    <span class="hljs-keyword">return</span> texture;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果这样写的话， 很有可能你到时候，图片不出来，还会报错。</p>
<p>为什么呢？</p>
<p>因为<code>WebGL</code>对图片的 <code>width</code> <code>height</code>有要求，那就是，最好都是 <code>2</code> 的整数次方。比如说2， 4， 8， 16，等等。</p>
<p>为了让所有的图片都可以好用，我们最终代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> images_loaing_progress = <span class="hljs-number">0</span>;

<span class="hljs-comment">// 判断是否是 2 的 整数次方</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isPowerOf2</span>(<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-keyword">return</span> (value & (value - <span class="hljs-number">1</span>)) === <span class="hljs-number">0</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CreateTextureAndLoadImage</span>(<span class="hljs-params">gl</span>) </span>&#123;
    <span class="hljs-comment">// 在 WebGL 里创建一个 texture</span>
    <span class="hljs-keyword">let</span> texture = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, texture);

    <span class="hljs-comment">// 异步加载一张图片，存进刚刚创建好的 texture 里</span>
    <span class="hljs-keyword">var</span> image = <span class="hljs-keyword">new</span> Image();
    image.src = <span class="hljs-string">"images/funny-cat.jpeg"</span>;
    image.addEventListener(<span class="hljs-string">'load'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        gl.bindTexture(gl.TEXTURE_2D, texture);
        gl.texImage2D(gl.TEXTURE_2D, <span class="hljs-number">0</span>, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
        <span class="hljs-keyword">if</span> (isPowerOf2(image.width) && isPowerOf2(image.height)) &#123;
            gl.generateMipmap(gl.TEXTURE_2D);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"非2的整数次方"</span>);
            gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
            gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
            gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
        &#125;
        images_loaing_progress = <span class="hljs-number">100</span>;
    &#125;);
    <span class="hljs-keyword">return</span> texture;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>好的，也许你发现了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">gl.generateMipmap(gl.TEXTURE_2D);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一句，是用来生成 <code>Mipmap</code> 的，什么叫 <code>Mipmap</code>，后面用一篇文章接着说。这里这么写就行。</p>
<h3 data-id="heading-7">生成顶点坐标和顶点UV</h3>
<p>不管是展示什么东西，我们必须有顶点，为了画三角形，我们至少准备三个顶点。</p>
<p>顶点的信息，这里有两个：</p>
<ul>
<li>
<ol>
<li>坐标</li>
</ol>
</li>
<li>
<ol start="2">
<li>UV</li>
</ol>
</li>
</ul>
<p>我们随意取三个点：</p>
<ul>
<li>
<p>A <code>坐标:</code>(-1, -1)      <code>UV:</code> (0, 0) 图片左下角</p>
</li>
<li>
<p>B <code>坐标:</code>(1, -1)       <code>UV:</code> (1, 0) 图片右下角</p>
</li>
<li>
<p>C <code>坐标:</code>(0, 1)       <code>UV:</code> (0.5, 1) 图片最上面中间</p>
</li>
</ul>
<p>我们将上面的数据，用一个平坦的数组表示出来：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> data = [-<span class="hljs-number">1</span>, -<span class="hljs-number">1</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>,
    <span class="hljs-number">1</span>, -<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">0</span>,
    <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">0.5</span>, <span class="hljs-number">1</span>
];
<span class="hljs-keyword">var</span> dataArr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>(data);
<span class="hljs-keyword">var</span> pointCount = <span class="hljs-number">3</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，三个点的坐标，一定要是逆时针。</p>
<h3 data-id="heading-8">vertex_shader 接收UV信息</h3>
<p>我们知道，vertex_shader 可以用来接收 buffer 中的信息。</p>
<p>顶点的坐标:</p>
<pre><code class="copyable">    attribute vec2 a_PointVertex; // 顶点坐标
<span class="copy-code-btn">复制代码</span></code></pre>
<p>UV信息同样：</p>
<pre><code class="copyable">    attribute vec2 a_PointUV; // 顶点UV
<span class="copy-code-btn">复制代码</span></code></pre>
<p>极其简单。</p>
<p>由于最终的颜色，和图片采用啥的，都是在<code>fragment_shader</code>中进行。所以UV信息需要传到 <code>fragment_shader</code>。</p>
<p>所以必须声明一个 varying 变量：</p>
<pre><code class="copyable">    varying vec2 uv;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终的 <code>vertex_shader</code>：</p>
<pre><code class="copyable"><script id="vertex_shader" type="myshader">
    // Vertex Shader
    precision mediump int;
    precision mediump float;
    
    uniform mat3 u_all; // 拉伸 旋转 位移

    attribute vec2 a_PointVertex; // 顶点坐标
    attribute vec2 a_PointUV;     // 顶点UV

    varying vec2 uv;


    void main() &#123;
      vec3 coord = u_all * vec3(a_PointVertex, 1.0);
      gl_Position = vec4(coord.x, coord.y, 0.0, 1.0);
      uv = a_PointUV;
    &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于我们用的一个buffer来存储 坐标和UV 两个信息，所以，我们必须告知 <code>vertex_shader</code>如何使用这个buffer：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> a_PointVertex = gl.getAttribLocation(program, <span class="hljs-string">'a_PointVertex'</span>);
<span class="hljs-keyword">var</span> a_PointUV = gl.getAttribLocation(program, <span class="hljs-string">'a_PointUV'</span>);
gl.vertexAttribPointer(a_PointVertex, <span class="hljs-number">2</span>, gl.FLOAT, <span class="hljs-literal">false</span>, <span class="hljs-number">16</span>, <span class="hljs-number">0</span>); <span class="hljs-comment">// 每个顶点 16 个字节, 坐标从第0个字节开始</span>
gl.enableVertexAttribArray(a_PointVertex);
gl.vertexAttribPointer(a_PointUV, <span class="hljs-number">2</span>, gl.FLOAT, <span class="hljs-literal">false</span>, <span class="hljs-number">16</span>, <span class="hljs-number">8</span>); <span class="hljs-comment">// 每个顶点 16 个字节， UV从第8个字节开始</span>
gl.enableVertexAttribArray(a_PointUV);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">fragment_shader 利用UV信息，对图片进行采样</h3>
<p>我们知道 <code>buffer</code> 信息，在<code>vertex_shader</code>可以用 <code>attribute</code>的形式接收。</p>
<p>那么Image信息，在<code>fragment_shader</code>中，怎么来取呢？</p>
<pre><code class="copyable">答案就是采样！
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-glsl copyable" lang="glsl">      <script id="fragment_shader" type="myshader">
       <span class="hljs-comment">// Fragment shader</span>
       <span class="hljs-keyword">precision</span> <span class="hljs-keyword">mediump</span> <span class="hljs-type">int</span>;
       <span class="hljs-keyword">precision</span> <span class="hljs-keyword">mediump</span> <span class="hljs-type">float</span>;

       <span class="hljs-keyword">uniform</span> <span class="hljs-type">sampler2D</span> u_funny_cat; <span class="hljs-comment">// 有趣的猫的图片</span>

       <span class="hljs-keyword">varying</span> <span class="hljs-type">vec2</span> uv;

       <span class="hljs-type">void</span> main() &#123;
         <span class="hljs-type">vec4</span> sample_color = <span class="hljs-built_in">texture2D</span>(u_funny_cat, uv);
         <span class="hljs-built_in">gl_FragColor</span> = <span class="hljs-type">vec4</span>(sample_color, <span class="hljs-number">1.0</span>);
       &#125;
   </script>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">还有一步</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> u_FunnyCatLocation = gl.getUniformLocation(program, <span class="hljs-string">"u_funny_cat"</span>);
gl.uniform1i(u_FunnyCatLocation, <span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面两句是干嘛的呢，我们看看刚才的<code>fragment_shader</code>，是不是有一个<code>uniform</code> 变量<code>u_funny_cat</code>。</p>
<p>这个变量代表的是我们存入WebGL中的图片的下标，我们只存了一个图，所以这个图的下标自然就是0。</p>
<h3 data-id="heading-11">看看效果</h3>
<p>注意，我们需要拖动一下网页上的滑竿，才能出来图像，是因为拖动的时候会调用画图的代码。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4659c17fabb479bb1bb6f91378e95a7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先，图片倒了，这个不是什么大问题。由于图片本身的坐标系，和UV所采用的坐标系不一样。</p>
<p>改法有很多种，这里我们直接改顶点的UV：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> data = [-<span class="hljs-number">1</span>, -<span class="hljs-number">1</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>,
            <span class="hljs-number">1</span>, -<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>,
            <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">0.5</span>, <span class="hljs-number">0</span>
        ];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么效果如下(还是需要先拖动一下滑竿)：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3483ad564924925910647483c3ef6a7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>哎呀，小猫咪显示的不完整啊。</p>
<h3 data-id="heading-12">通过更改顶点的UV，来显示完整的图片</h3>
<p>由于三个顶点的UV就代表了，这三个点锚定在图片的那个点上，中间的填充，是用插值自动来做的。</p>
<p>所以，要让小猫咪显示完整的话，我们把C点（最上面的点）变成-1试试：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> data = [-<span class="hljs-number">1</span>, -<span class="hljs-number">1</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>,
    <span class="hljs-number">1</span>, -<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>,
    <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">0.5</span>, -<span class="hljs-number">1</span>
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd941e460d25429abe77d42d1c8b5cbe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>仔细分析一下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0a595a543144c988ddc397fff5f901c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据三个点的UV，我们图中的红点处的UV根据插值，大概差不多就是 (0.5, 0)</p>
<p>而 (0.5, 0) 这个点，刚刚好就是原来的图片的 最上方中间位置。（注意，原图的Y是倒过来的， y = 0，就是最上方）。</p>
<p>那么其他的点，也是根据这个逻辑，来跟原图对应的，这就是所谓插值。</p>
<p>我们把</p>
<ul>
<li>左边的点UV往左拉一拉</li>
<li>右边的点UV往右拉一拉</li>
</ul>
<p>代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> data = [-<span class="hljs-number">1</span>, -<span class="hljs-number">1</span>, -<span class="hljs-number">0.5</span>, <span class="hljs-number">1</span>,
            <span class="hljs-number">1</span>, -<span class="hljs-number">1</span>, <span class="hljs-number">1.5</span>, <span class="hljs-number">1</span>,
            <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">0.5</span>, -<span class="hljs-number">1</span>
        ];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44625e84196540dd8a25c4a805841e2e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家根据插值，和三个点的UV，来计算一下这个方框的大概UV，看看是不是，差不多就是一个图形的四个角。</p>
<p>好了，这就是为什么，这个框框里面就能完整的显示一个小猫咪了。</p>
<h4 data-id="heading-13">UV的y轴反了，非常不爽</h4>
<p>由于这一点非常不爽，我们在外面构造UV信息的时候，经常不好想象。</p>
<p>所以我们不在外面构造的时候，进行这一步修正。</p>
<p>我们在<code>vertex_shader</code>里修正：</p>
<pre><code class="copyable">          uv = a_PointUV;
          uv.y = 1.0 - uv.y; // 就这一句。。。。。。

<span class="copy-code-btn">复制代码</span></code></pre>
<p>看效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e2f2f43ffed4e1bb48b41c7d77639be~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>小猫咪又倒过来了，是因为我们数据的UV刚才修正过一遍，我们用将一开始的数据找回来：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> data = [-<span class="hljs-number">1</span>, -<span class="hljs-number">1</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>,
    <span class="hljs-number">1</span>, -<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">0</span>,
    <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">0.5</span>, <span class="hljs-number">1</span>
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66a3200d79bc49ff8c9e302511b6e838~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>又显示不完整了，这里我就不给出怎么显示完整的代码了，小伙伴们自己搞一搞。</p>
<hr>
<hr>
<hr>
<pre><code class="copyable">  正文结束，下面是答疑
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">小瓜瓜说：我如果乱填UV信息，会发生什么呢?</h3>
<ul>
<li>答：不会发生什么，无非就是三个点的UV信息是乱的，然后中间插值也是乱的，显示的图片也是乱的：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> data = [-<span class="hljs-number">1</span>, -<span class="hljs-number">1</span>, <span class="hljs-built_in">Math</span>.random(), <span class="hljs-built_in">Math</span>.random(),
          <span class="hljs-number">1</span>, -<span class="hljs-number">1</span>, <span class="hljs-built_in">Math</span>.random(), <span class="hljs-built_in">Math</span>.random(),
          <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-built_in">Math</span>.random(), <span class="hljs-built_in">Math</span>.random()
      ];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以试试这样写UV。。。</p></div>  
</div>
            