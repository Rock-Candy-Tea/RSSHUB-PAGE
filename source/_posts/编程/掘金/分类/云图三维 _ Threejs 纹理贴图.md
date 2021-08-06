
---
title: '云图三维 _ Three.js 纹理贴图'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35f9c74156a14be6bbc8b0a654c55fcd~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 23:45:03 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35f9c74156a14be6bbc8b0a654c55fcd~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>图片来源： <a href="https://link.juejin.cn/?target=https%3A%2F%2Funsplash.com%2Fphotos%2FUD5drKd4H6w" target="_blank" rel="nofollow noopener noreferrer" title="https://unsplash.com/photos/UD5drKd4H6w" ref="nofollow noopener noreferrer">unsplash.com/photos/UD5d…</a></p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuntucad.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuntucad.com/" ref="nofollow noopener noreferrer">云图三维 连接你·创造的世界</a> 致力于打造国内第一家集查看、建模、装配和渲染于一体的“云端CAD”协作设计平台。</p>
</blockquote>
<p>应读者的要求，希望我们成立一个专业的、面向成渝地区的前端开发人员的webgl、Threejs行业QQ交流群，便于大家讨论问题。群里有研究webgl、Threejs大佬哦，欢迎大家加入！——点击链接加入群聊【three.js/webgl重庆联盟群】：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjq.qq.com%2F%3F_wv%3D1027%26k%3DpX9BUnzn" target="_blank" rel="nofollow noopener noreferrer" title="https://jq.qq.com/?_wv=1027&k=pX9BUnzn" ref="nofollow noopener noreferrer">jq.qq.com/?_wv=1027&k…</a></p>
<h2 data-id="heading-0">一、前言</h2>
<p>今天这篇文章中，主要介绍下three.js中纹理贴图的模块，渲染一个 3D 物体时，网格 Mesh 决定了这个物体的形状态，如一个球，一辆车，一个人等。而纹理决定了这个物体的表面具体长什么样子。一个球包上一层篮球的花纹就是篮球了，而如果包上的是一层足球的花纹那可能就是足球了。</p>
<h2 data-id="heading-1">二、概述</h2>
<p>Three.Js 中为定义了多种多样的纹理，其类图如下。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35f9c74156a14be6bbc8b0a654c55fcd~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="0585M36@OQ2&#125;&#125;5DD(T_0M3E.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>纹理的基类是 Texture，一般我们都使用这个类，通过给其属性 Image 传入一个图片从而构造出一个纹理。纹理是材质的属性，材质和几何体 Gemotry 构成 Mesh ，然后被添加到 Scene 中进行渲染。<strong>纹理决定了物体的表面该是什么样子，而材质则决定了物体具备什么样的“气质”</strong>。</p>
<h2 data-id="heading-2">三、纹理介绍</h2>
<h3 data-id="heading-3">1、Texture</h3>
<p>纹理的属性很多，但在一般情况下，并不要需要一一来设置，而是取默认值即可。并且，我们一般都会通过 <code>TextureLoader </code>来为我们构造一个纹理，而不是直接构造。例子如下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> texture = <span class="hljs-keyword">new</span> THREE.TextureLoader().load( <span class="hljs-string">"textures/water.jpg"</span> ); 
texture.wrapS = THREE.RepeatWrapping; 
texture.wrapT = THREE.RepeatWrapping; 
texture.repeat.set( <span class="hljs-number">4</span>, <span class="hljs-number">4</span> );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般情况下，我们这么简单的设置下就可以了。但实际应用中，我们可能会碰到需要指定自己的纹理坐标的情况。那这个时候，我们就需要自己计算好纹理坐标，然后给 geometry 添加属性 “uv”，从而应用我们自己的纹理坐标。</p>
<pre><code class="hljs language-js copyable" lang="js">geom.addAttribute(<span class="hljs-string">'uv'</span>, <span class="hljs-keyword">new</span> THREE.BufferAttribute(uvArr, <span class="hljs-number">2</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过纹理贴图加载器<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.yanhuangxueyuan.com%2Fthreejs%2Fdocs%2Findex.html%23api%2Fzh%2Floaders%2FTextureLoader" target="_blank" rel="nofollow noopener noreferrer" title="http://www.yanhuangxueyuan.com/threejs/docs/index.html#api/zh/loaders/TextureLoader" ref="nofollow noopener noreferrer">TextureLoader</a>的<code>load()</code>方法加载一张图片可以返回一个纹理对象<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.yanhuangxueyuan.com%2Fthreejs%2Fdocs%2Findex.html%23api%2Fzh%2Ftextures%2FTexture" target="_blank" rel="nofollow noopener noreferrer" title="http://www.yanhuangxueyuan.com/threejs/docs/index.html#api/zh/textures/Texture" ref="nofollow noopener noreferrer">Texture</a>，纹理对象<code>Texture</code>可以作为模型材质颜色贴图<code>.map</code>属性的值。</p>
<p>材质的颜色贴图属性<code>.map</code>设置后，模型会从纹理贴图上采集像素值，这时候一般来说不需要再设置材质颜色<code>.color</code>。<code>.map</code>贴图之所以称之为颜色贴图就是因为网格模型会获得颜色贴图的颜色值RGB。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 纹理贴图映射到一个矩形平面上 </span>
<span class="hljs-keyword">var</span> geometry = <span class="hljs-keyword">new</span> THREE.PlaneGeometry(<span class="hljs-number">204</span>, <span class="hljs-number">102</span>); <span class="hljs-comment">//矩形平面 </span>
<span class="hljs-comment">// TextureLoader创建一个纹理加载器对象，可以加载图片作为几何体纹理 </span>
<span class="hljs-keyword">var</span> textureLoader = <span class="hljs-keyword">new</span> THREE.TextureLoader(); <span class="hljs-comment">// 执行load方法，加载纹理贴图成功后，返回一个纹理对象</span>
Texture textureLoader.load(<span class="hljs-string">'Earth.png'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">texture</span>) </span>&#123; 
<span class="hljs-keyword">var</span> material = <span class="hljs-keyword">new</span> THREE.MeshLambertMaterial(&#123; 
<span class="hljs-comment">// color: 0x0000ff, </span>
<span class="hljs-comment">// 设置颜色纹理贴图：Texture对象作为材质map属性的属性值 </span>
    <span class="hljs-attr">map</span>: texture,<span class="hljs-comment">//设置颜色贴图属性值 </span>
&#125;); 
<span class="hljs-comment">//材质对象</span>
Material <span class="hljs-keyword">var</span> mesh = <span class="hljs-keyword">new</span> THREE.Mesh(geometry, material); 
<span class="hljs-comment">//网格模型对象</span>
Mesh scene.add(mesh); 
<span class="hljs-comment">//网格模型添加到场景中 </span>
<span class="hljs-comment">//纹理贴图加载成功后，调用渲染函数执行渲染操作 </span>
<span class="hljs-comment">// render(); </span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2、CanvasTexture</h3>
<p>在Three.js中，肯定避免不了要设置实体的材质，比如说要给一个box加颜色、图片或者视频画面；
大家可以看以下代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> THREE.MeshBasicMaterial(&#123;<span class="hljs-attr">color</span>: <span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">0xffffff</span>&#125;); <span class="hljs-comment">// 颜色</span>
 
<span class="hljs-keyword">new</span> THREE.MeshBasicMaterial( &#123; <span class="hljs-attr">map</span>: THREE.ImageUtils.loadTexture(<span class="hljs-string">'./assets/plane.jpeg'</span>) &#125; ); <span class="hljs-comment">// 图片</span>
 
<span class="hljs-keyword">new</span> THREE.VideoTexture(<span class="hljs-built_in">document</span>.getElementId(<span class="hljs-string">'video'</span>)); <span class="hljs-comment">// 视频</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这些功能对我来说已经够用了，后来发现也可以用canvas的渲染作为材质，为了做demo方便自己包装了下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> createCanvas = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">w,h</span>) </span>&#123;
w = w || <span class="hljs-number">30</span>;
h = h || <span class="hljs-number">30</span>
<span class="hljs-keyword">var</span> cs = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>)
<span class="hljs-keyword">var</span> ctx = cs.getContext(<span class="hljs-string">'2d'</span>);
cs.width = w;
cs.height = h;
ctx.fillStyle =<span class="hljs-string">"#fff"</span>;
ctx.fillRect(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,w,h);
ctx.strokeStyle = <span class="hljs-string">"#c00"</span>;
ctx.shadowBlur = <span class="hljs-number">20</span>;
ctx.shadowColor = <span class="hljs-string">"#c99"</span>;
ctx.strokeWidth = <span class="hljs-number">30</span>;
ctx.beginPath();
ctx.moveTo(w/<span class="hljs-number">2</span>, <span class="hljs-number">0</span>);
ctx.lineTo(<span class="hljs-number">0</span>,h);
ctx.lineTo(w, h);
ctx.closePath()
ctx.stroke();
<span class="hljs-keyword">return</span> cs;
&#125;
 
<span class="hljs-keyword">var</span> texture = <span class="hljs-keyword">new</span> THREE.Texture(createCanvas(<span class="hljs-number">130</span>,<span class="hljs-number">130</span>)) 
<span class="hljs-keyword">var</span> material = <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial(&#123;
    <span class="hljs-attr">map</span>: texture
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>附上效果图</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24b7aeace2b74f7eb31c91bf4831abdf~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt=")XHJAY%NAZSX&#123;V%W_VTL$CV.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">3、DataTexture（数据纹理对象）</h3>
<p>three.js数据纹理对象<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.yanhuangxueyuan.com%2Fthreejs%2Fdocs%2Findex.html%23api%2Fzh%2Ftextures%2FDataTexture" target="_blank" rel="nofollow noopener noreferrer" title="http://www.yanhuangxueyuan.com/threejs/docs/index.html#api/zh/textures/DataTexture" ref="nofollow noopener noreferrer">DataTexture</a>简单地说就是通过程序创建纹理贴图的每一个像素值。</p>
<p>程序生成一张图片的RGB值</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81eaec418b094b4b8f4fe6ae1854aed5~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="A9%A3_I0~7&#125;@W$_@UUSS25A.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> geometry = <span class="hljs-keyword">new</span> THREE.PlaneGeometry(<span class="hljs-number">128</span>, <span class="hljs-number">128</span>); <span class="hljs-comment">//矩形平面 </span>
<span class="hljs-comment">/** * 创建纹理对象的像素数据 */</span> 
<span class="hljs-keyword">var</span> width = <span class="hljs-number">32</span>; <span class="hljs-comment">//纹理宽度 </span>
<span class="hljs-keyword">var</span> height = <span class="hljs-number">32</span>; <span class="hljs-comment">//纹理高度 </span>
<span class="hljs-keyword">var</span> size = width * height; <span class="hljs-comment">//像素大小 </span>
<span class="hljs-keyword">var</span> data = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(size * <span class="hljs-number">3</span>); <span class="hljs-comment">//size*3：像素在缓冲区占用空间 </span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < size * <span class="hljs-number">3</span>; i += <span class="hljs-number">3</span>) &#123; <span class="hljs-comment">// 随机设置RGB分量的值 </span>
data[i] = <span class="hljs-number">255</span> * <span class="hljs-built_in">Math</span>.random() 
data[i + <span class="hljs-number">1</span>] = <span class="hljs-number">255</span> * <span class="hljs-built_in">Math</span>.random() 
data[i + <span class="hljs-number">2</span>] = <span class="hljs-number">255</span> * <span class="hljs-built_in">Math</span>.random() 
&#125; 
<span class="hljs-comment">// 创建数据文理对象 RGB格式：THREE.RGBFormat </span>
<span class="hljs-keyword">var</span> texture = <span class="hljs-keyword">new</span> THREE.DataTexture(data, width, height, THREE.RGBFormat); 
texture.needsUpdate = <span class="hljs-literal">true</span>; 
<span class="hljs-comment">//纹理更新 </span>
<span class="hljs-comment">//打印纹理对象的image属性 </span>
<span class="hljs-comment">// console.log(texture.image); </span>
<span class="hljs-keyword">var</span> material = <span class="hljs-keyword">new</span> THREE.MeshPhongMaterial(&#123; 
<span class="hljs-attr">map</span>: texture, <span class="hljs-comment">// 设置纹理贴图 </span>
&#125;); 
<span class="hljs-comment">//材质对象Material </span>
<span class="hljs-keyword">var</span> mesh = <span class="hljs-keyword">new</span> THREE.Mesh(geometry, material);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">写在最后</h2>
<p>本文介绍了Three.js的纹理相关的内容，包含了使用Texture、CanvasTexture、DataTexture具体如何使用，希望对你有帮助。</p>
<blockquote>
<p>本文发布自 云图三维大前端团队，文章未经授权禁止任何形式的转载。</p>
</blockquote></div>  
</div>
            