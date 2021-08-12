
---
title: 'three.js 使用总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7893'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 18:21:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=7893'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第1天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h2 data-id="heading-0">three.js 基础</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Faotu.io%2Fnotes%2F2017%2F08%2F28%2Fgetting-started-with-threejs%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://aotu.io/notes/2017/08/28/getting-started-with-threejs/index.html" ref="nofollow noopener noreferrer">Three.js 现学现卖</a> 这篇文章会让你对 Three.js 有全面的了解。</p>
<h2 data-id="heading-1">实战经验</h2>
<h3 data-id="heading-2">实时绘制</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">animate</span>(<span class="hljs-params"></span>) </span>&#123;
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <code>requestAnimationFrame</code> 实现了 <code>Three.js</code> 的渲染帧，只要我们改变场景类物体的属性，渲染帧就能实时绘制出属性变化后的物体。</p>
<h3 data-id="heading-3">几何体 <code>Geometry</code></h3>
<h3 data-id="heading-4">尺寸和位置</h3>
<p>几何体 <code>Geometry</code> 提供了 <code>.scale ( x, y, z )</code> 和 <code>.scale.x = xxx</code> 来实现尺寸的缩放，他们的区别主要在缩放的参照物。</p>
<p>一般来说，<strong>调用方法</strong>的都是基于<strong>几何体的当前的属性</strong>，直接更改属性值的基于几何体创建时的原始属性：</p>
<ol>
<li><code>.scale()</code> 缩放基于当前已缩放过的尺寸</li>
<li><code>.scale.x = xxx</code> 缩放基于原始的尺寸</li>
</ol>
<p>使用 <code>.translate(x, y, z)</code> 和 <code>.translate.x === xxx</code> 移动以及``.rotateX()<code>和</code>.rotate.x` 旋转时也遵循这个规律。</p>
<h3 data-id="heading-5">计算尺寸</h3>
<p>一旦进行了缩放，物体的尺寸就发生了变化，我们可以通过以下方式获取最新的尺寸信息：</p>
<pre><code class="hljs language-js copyable" lang="js">geometry.computeBoundingBox() <span class="hljs-comment">// 获取几何体的包围盒 </span>
<span class="hljs-keyword">let</span> &#123; <span class="hljs-attr">y</span>: height, <span class="hljs-attr">x</span>: width, <span class="hljs-attr">z</span>: depth &#125; = geometry.boundingBox.getSize()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">材质 Material</h3>
<h4 data-id="heading-7">更改材质颜色</h4>
<p>Material 的 color 属性都是 <code>THREE.Color</code> 的实例，它拥有多种改变颜色的方法，推荐如下方式：</p>
<pre><code class="hljs language-js copyable" lang="js">material.color.setStyle(newColor)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>newColor 可以是： <code>"rgb(250, 0,0)"</code>, <code>"rgb(100%, 0%, 0%)"</code>, <code>"hsl(0, 100%, 50%)"</code>, <code>"#ff0000"</code>, <code>"#f00"</code>, or <code>"red"</code></p>
<p><strong>注意：不支持 rgba</strong></p>
<h4 data-id="heading-8">透明颜色</h4>
<p>首先，Three.js 不支持透明颜色（<em>存疑，待验证</em>）。目前使用的是透明材质+颜色的方式：</p>
<pre><code class="hljs language-js copyable" lang="js">material = <span class="hljs-keyword">new</span> <span class="hljs-built_in">this</span>.THREE.MeshLambertMaterial(&#123;
  <span class="hljs-attr">color</span>: <span class="hljs-number">0xff3c60</span>, 
  <span class="hljs-attr">transparent</span>: <span class="hljs-literal">true</span>
&#125;);
material.color.setStyle(color)
material.opacity = opacity
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">替换材质</h4>
<p>其实更简单就是, 更改 Mesh 的 Material 属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> cube = <span class="hljs-keyword">new</span> THREE.Mesh(geometry, material)
cube = newMaterial <span class="hljs-comment">// 更改为新的材质</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">立方体贴图</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> materials = [ 
  rightMaterial, <span class="hljs-comment">// right</span>
  leftMaterial, <span class="hljs-comment">// left</span>
  topMaterial, <span class="hljs-comment">// top</span>
  bottomMaterial, <span class="hljs-comment">// bottom </span>
  frontMaterial, <span class="hljs-comment">// front </span>
  backMaterial, <span class="hljs-comment">// back</span>
]
<span class="hljs-keyword">let</span> cube = <span class="hljs-keyword">new</span> THREE.Mesh(geometry, material)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">场景等比缩放</h3>
<p>一般调整窗口大小时我们用下文的 resize 方法实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建渲染器</span>
<span class="hljs-keyword">let</span> renderer = <span class="hljs-keyword">new</span> THREE.WebGLRenderer();
<span class="hljs-keyword">let</span> camera = <span class="hljs-keyword">new</span> THREE.PerspectiveCamera(<span class="hljs-number">75</span>, width / height, <span class="hljs-number">1</span>, <span class="hljs-number">800</span>)

<span class="hljs-comment">// 调整大小</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resize</span> (<span class="hljs-params">width, height</span>) </span>&#123;
  camera.aspect = width / height
  renderer.setSize(width, height);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要想做到物体在场景内占有的比率一定，我们可以使用如下方式:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 以下为伪代码</span>
<span class="hljs-keyword">const</span> designW = W
<span class="hljs-keyword">const</span> designH = H
<span class="hljs-keyword">const</span> trueW = W1
<span class="hljs-keyword">const</span> trueH = W2

<span class="hljs-keyword">let</span> renderer = <span class="hljs-keyword">new</span> THREE.WebGLRenderer();
<span class="hljs-keyword">let</span> camera = <span class="hljs-keyword">new</span> THREE.PerspectiveCamera(<span class="hljs-number">75</span>, designW / designH, <span class="hljs-number">1</span>, <span class="hljs-number">800</span>)

<span class="hljs-comment">// 绘制物体按照 designW 下对应的尺寸绘制</span>

<span class="hljs-comment">// 适配到当前场景宽高</span>
camera.aspect = trueW / trueH
renderer.setSize(trueW, trueH);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">动画</h3>
<h4 data-id="heading-13">简单动画</h4>
<p>在渲染帧内改变物体的属性就可以形成动画</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">animate</span>(<span class="hljs-params"></span>) </span>&#123;
  requestAnimationFrame(animate);

  <span class="hljs-comment">// 改变物体的属性</span>
  boxMesh.rotateY(speed)

  renderer.render(scene, camera);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">Tween.JS 动画</h4>
<p>利用 Tween.JS 我们可以轻松实现许多动画，详情参见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftweenjs%2Ftween.js%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tweenjs/tween.js/" ref="nofollow noopener noreferrer">Tween.JS 文档</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> ani = <span class="hljs-keyword">new</span> TWEEN.Tween(&#123; <span class="hljs-attr">rotation</span>: totalRotation1 &#125;)
  .to(&#123; <span class="hljs-attr">rotation</span>: totalRotation2 &#125;, <span class="hljs-number">1000</span>)
  .onUpdate(<span class="hljs-function">(<span class="hljs-params">&#123;rotation&#125;</span>) =></span> &#123;
    boxMesh.rotation.y = rotation
  &#125;)
  .onComplete(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ani complete'</span>)
  &#125;)
  .start()


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">animate</span>(<span class="hljs-params"></span>) </span>&#123;
  requestAnimationFrame(animate);

  <span class="hljs-comment">// 改变物体的属性</span>
  ani.update()

  renderer.render(scene, camera);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">光源种类</h3>
<h4 data-id="heading-16">光源和阴影</h4>
<p>不能产生投影的光源有：环境光（AmbientLight）、半球光（HemisphereLight）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 渲染器启用阴影</span>
renderer.shadowMap.enabled = <span class="hljs-literal">true</span>

<span class="hljs-comment">// 指定哪个光源能产生阴影</span>
spotLight.castShadow = <span class="hljs-literal">true</span>

<span class="hljs-comment">// 指定哪个物体能投射阴影，哪个物体能接受阴影</span>
plane.receiveShadow = <span class="hljs-literal">true</span>
cube.receiveShadow = <span class="hljs-literal">true</span>

<span class="hljs-comment">// 更改阴影质量</span>

<span class="hljs-comment">// 更改渲染器的投影类型，默认值是 THREE.PCFShadowMap</span>
renderer.shadowMap.type = THREE.PCFSoftShadowMap

<span class="hljs-comment">// 更改光源的阴影质量，默认值是 512</span>
spotLight.shadow.mapSize.width = <span class="hljs-number">1024</span> 
spotLight.shadow.mapSize.height = <span class="hljs-number">1024</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">canvas 纹理</h3>
<h4 data-id="heading-18">精灵文字</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 绘制canvas</span>
<span class="hljs-keyword">let</span> &#123; fontSize, fontFamily, fontBold, color &#125; = style
<span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>);
<span class="hljs-keyword">let</span> ctx = canvas.getContext(<span class="hljs-string">'2d'</span>);
  
<span class="hljs-keyword">const</span> fontStyle = <span class="hljs-string">`<span class="hljs-subst">$&#123;fontBold ? <span class="hljs-string">'bold'</span> : <span class="hljs-string">'normal'</span>&#125;</span> <span class="hljs-subst">$&#123;fontSize&#125;</span>px `</span> + fontFamily
ctx.font = fontStyle

<span class="hljs-keyword">const</span> &#123; width &#125; = ctx.measureText(text)

canvas.width = width
canvas.height = fontSize

ctx.font = fontStyle
ctx.fillStyle = color;
ctx.fillText(text, <span class="hljs-number">0</span>, fontSize);

<span class="hljs-comment">// canvas 材质</span>
<span class="hljs-keyword">let</span> texture = <span class="hljs-keyword">new</span> THREE.CanvasTexture(canvas)

<span class="hljs-comment">// 生成纹理</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">渐变色的实现</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> context = canvas.getContext( <span class="hljs-string">'2d'</span> );

<span class="hljs-keyword">let</span> gradient = context.createLinearGradient( <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, canvas.height);
gradient.addColorStop( <span class="hljs-number">0</span>, c1 );
gradient.addColorStop( <span class="hljs-number">1</span>, c2 );

context.fillStyle = gradient;

context.fillRect( <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, canvas.width, canvas.height );

<span class="hljs-keyword">let</span> canvasTexture = <span class="hljs-keyword">new</span> <span class="hljs-built_in">this</span>.THREE.CanvasTexture( canvas );

<span class="hljs-keyword">let</span> canvasMaterial = <span class="hljs-keyword">new</span> <span class="hljs-built_in">this</span>.THREE.MeshLambertMaterial( &#123; <span class="hljs-attr">map</span>: canvasTexture &#125; );
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">3D 模型</h3>
<h4 data-id="heading-21">加载 3D 模型</h4>
<p>默认内置的模型都是 json 形式的，如果要加载其它格式的，需要自行按照官方示例引入对应的 Loader。</p>
<h4 data-id="heading-22">模型中心点</h4>
<p>模型的中心点可能不在其几何中心，通过如下方式，可以重置中心点并将模型移动到三维坐标 <code>(0,0,0)</code> 处：</p>
<pre><code class="hljs language-js copyable" lang="js">geometry.center()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若模型为 <code>Three.Group</code> 则要进行复杂的计算。</p>
<h4 data-id="heading-23">模型加载后纹理为纯黑色的处理</h4>
<pre><code class="copyable">loader.load( 'xxx.obj', function ( object ) &#123;
  //需要添加的部分
  object.scene.traverse(function ( child ) &#123;
    if ( child.isMesh ) &#123;
      child.material.emissive = child.material.color;
      child.material.emissiveMap = child.material.map ;
    &#125;
  &#125;);
  scene.add( gltf.scene );
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>相关资料：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fljason1993%2Farticle%2Fdetails%2F90767066" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/ljason1993/article/details/90767066" ref="nofollow noopener noreferrer">关于 threejs 加载fbx 材质是黑色 没有贴图 的问题</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_35377699%2Farticle%2Fdetails%2F83539581" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_35377699/article/details/83539581" ref="nofollow noopener noreferrer">three.js gltf模型加载后为黑色</a></li>
</ul>
<h3 data-id="heading-24">点击物体</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> raycaster = <span class="hljs-keyword">new</span> THREE.Raycaster()
<span class="hljs-keyword">let</span> mouse = <span class="hljs-keyword">new</span> THREE.Vector2()


onClick = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
  <span class="hljs-comment">// x, y 为左上点坐标</span>
  <span class="hljs-built_in">this</span>.mouse.x = ((event.clientX - x) / width) * <span class="hljs-number">2</span> - <span class="hljs-number">1</span>;
  <span class="hljs-built_in">this</span>.mouse.y = -((event.clientY - y) / height) * <span class="hljs-number">2</span> + <span class="hljs-number">1</span>;

  <span class="hljs-comment">// update the picking ray with the camera and mouse position</span>
  <span class="hljs-built_in">this</span>.raycaster.setFromCamera( <span class="hljs-built_in">this</span>.mouse, <span class="hljs-built_in">this</span>.camera.camera );

  <span class="hljs-comment">// calculate objects intersecting the picking ray</span>
  <span class="hljs-keyword">let</span> intersects = <span class="hljs-built_in">this</span>.raycaster.intersectObjects(<span class="hljs-built_in">this</span>.boxGroup.children );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考资料：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000010490845" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000010490845" ref="nofollow noopener noreferrer">ThreeJS中的点击与交互——Raycaster的用法</a></p>
<h2 data-id="heading-25">其他细节</h2>
<ol>
<li>在同一位置绘制多个平行平面时，会出现交错失真现象，可以调整数值，使平面在它的法线方向错开位置。</li>
</ol>
<h2 data-id="heading-26">参考资料</h2>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Faotu.io%2Fnotes%2F2017%2F08%2F28%2Fgetting-started-with-threejs%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://aotu.io/notes/2017/08/28/getting-started-with-threejs/index.html" ref="nofollow noopener noreferrer">Three.js 现学现卖</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fread.douban.com%2Freader%2Febook%2F7412854%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://read.douban.com/reader/ebook/7412854/" ref="nofollow noopener noreferrer">Three.js入门指南（张雯莉） - 豆瓣阅读</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fthreejs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://threejs.org/" ref="nofollow noopener noreferrer">Three.js 官网</a></p>
</li>
<li>
<p>Three.js 开发指南</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fre.jd.com%2Fcps%2Fitem%2F12113317.html" target="_blank" rel="nofollow noopener noreferrer" title="https://re.jd.com/cps/item/12113317.html" ref="nofollow noopener noreferrer">购买链接</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjosdirksen%2Flearning-threejs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/josdirksen/learning-threejs" ref="nofollow noopener noreferrer">示例代码仓库</a></li>
</ul>
</li>
</ul></div>  
</div>
            