
---
title: '云图三维 _ Three.js Sprite精灵'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf91ed16ee044c579e57d17703910414~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 17 Jul 2021 01:55:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf91ed16ee044c579e57d17703910414~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>图片来源： <a href="https://link.juejin.cn/?target=https%3A%2F%2Funsplash.com%2Fphotos%2FxyhRYPQ0DqU" target="_blank" rel="nofollow noopener noreferrer" title="https://unsplash.com/photos/xyhRYPQ0DqU" ref="nofollow noopener noreferrer">unsplash.com/photos/xyhR…</a></p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuntucad.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuntucad.com/" ref="nofollow noopener noreferrer">云图三维 连接你·创造的世界</a> 致力于打造国内第一家集查看、建模、装配和渲染于一体的“云端CAD”协作设计平台。</p>
</blockquote>
<p>Three.js的精灵模型对象Sprite是一个<strong>永远面向相机的平面</strong>，没有z轴的概念，通常用来加载纹理、用作标签使用，注意Sprite没有背面，<strong>它永远会正对着你</strong>。所以我们可以用它来显示一些标签，当改变观看角度，标签也会随之改变角度。并且，sprite不接受阴影，计算机图形学中，精灵指包含于场景中的二维图像或动画，基类都是<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.yanhuangxueyuan.com%2Fthreejs%2Fdocs%2Findex.html%23api%2Fzh%2Fcore%2FObject3D" target="_blank" rel="nofollow noopener noreferrer" title="http://www.yanhuangxueyuan.com/threejs/docs/index.html#api/zh/core/Object3D" ref="nofollow noopener noreferrer">Object3D</a>,关于精灵模型对象Sprite的方法和属性除了可以查看文档<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.yanhuangxueyuan.com%2Fthreejs%2Fdocs%2Findex.html%23api%2Fzh%2Fobjects%2FSprite" target="_blank" rel="nofollow noopener noreferrer" title="http://www.yanhuangxueyuan.com/threejs/docs/index.html#api/zh/objects/Sprite" ref="nofollow noopener noreferrer">Sprite</a>，也可以查看基类Object3D。</p>
<h2 data-id="heading-0">创建基本的组件</h2>
<p>之前提过，一个Three.js场景中必须包含一些必要的组件。比如场景、相机、渲染器等等。下面代码初始化一些基本组件，便于复用</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initScence</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">var</span> scene = <span class="hljs-keyword">new</span> THREE.Scene();
            <span class="hljs-comment">//直线光</span>
            <span class="hljs-keyword">var</span> directionalLight = <span class="hljs-keyword">new</span> THREE.DirectionalLight(<span class="hljs-number">0xffffff</span>, <span class="hljs-number">0.7</span>);
            directionalLight.position.set(-<span class="hljs-number">20</span>, <span class="hljs-number">40</span>, <span class="hljs-number">60</span>);
            scene.add(directionalLight);
            <span class="hljs-comment">//环境光</span>
            <span class="hljs-keyword">var</span> ambientLight = <span class="hljs-keyword">new</span> THREE.AmbientLight(<span class="hljs-number">0x292929</span>);
            scene.add(ambientLight);
            <span class="hljs-keyword">return</span> scene
        &#125;

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initCamera</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">var</span> camera = <span class="hljs-keyword">new</span> THREE.PerspectiveCamera(<span class="hljs-number">45</span>, <span class="hljs-built_in">window</span>.innerWidth / <span class="hljs-built_in">window</span>.innerHeight, <span class="hljs-number">0.1</span>, <span class="hljs-number">1000</span>);
            camera.position.x = <span class="hljs-number">120</span>;
            camera.position.y = <span class="hljs-number">60</span>;
            camera.position.z = <span class="hljs-number">180</span>;
            <span class="hljs-keyword">return</span> camera
        &#125;

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initRender</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">var</span> renderer = <span class="hljs-keyword">new</span> THREE.WebGLRenderer();
            renderer.setClearColor(<span class="hljs-keyword">new</span> THREE.Color(<span class="hljs-number">0xEEEEEE</span>, <span class="hljs-number">1.0</span>));
            renderer.setSize(<span class="hljs-built_in">window</span>.innerWidth, <span class="hljs-built_in">window</span>.innerHeight);
            <span class="hljs-keyword">return</span> renderer
        &#125;
        
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params"></span>) </span>&#123;
      
            <span class="hljs-keyword">var</span> scene = initScence();
            <span class="hljs-keyword">var</span> camera = initCamera();
            <span class="hljs-keyword">var</span> renderer = initRender()
            camera.lookAt(scene.position);

            <span class="hljs-comment">// 添加场景中的元素 TODO</span>

           
            <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"WebGL-output"</span>).appendChild(renderer.domElement);
            render();
            <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
                requestAnimationFrame(render);
                renderer.render(scene, camera);
            &#125;
        &#125;
        <span class="hljs-built_in">window</span>.onload = init
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">使用Sprite创建2D形状</h2>
<p>通过Sprite创建精灵模型不需要几何体，只需要给构造函数Sprite的参数设置为一个精灵材质<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.yanhuangxueyuan.com%2Fthreejs%2Fdocs%2Findex.html%23api%2Fzh%2Fmaterials%2FSpriteMaterial" target="_blank" rel="nofollow noopener noreferrer" title="http://www.yanhuangxueyuan.com/threejs/docs/index.html#api/zh/materials/SpriteMaterial" ref="nofollow noopener noreferrer">SpriteMaterial</a>即可。</p>
<p>精灵材质对象SpriteMaterial和普通的网格材质一样可以设置颜色(.color)、颜色贴图(.map)、开启透明(.transparent)、透明度(.opacity)等属性，精灵材质对象SpriteMaterial的基类是材质Material。</p>
<p>精灵材质SpriteMaterial的属性除了和网格材质类似的属性和方法外，还有一些自己独特的方法和属性，比如<code>.rotation</code>旋转精灵模型，更多相关属性和方法可以查看Threejs文档关于SpriteMaterial的介绍。</p>
<p>在Threejs中，可以使用Sprite加载图像纹理，当然也包括用canvas创建的纹理，因此，canvas能创建什么图像，Sprite就能创建什么形状。下面的例子使用Sprite创建了一个圆：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createSpriteShape</span>(<span class="hljs-params"></span>)</span>&#123;
       <span class="hljs-comment">/*1、创建一个画布，记得设置画布的宽高，否则将使用默认宽高，有可能会导致图像显示变形*/</span>
        <span class="hljs-keyword">let</span> canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"canvas"</span>);
        canvas.width = <span class="hljs-number">120</span>;
        canvas.height = <span class="hljs-number">120</span>;
        <span class="hljs-comment">/*2、创建图形，这部分可以去看w3c canvas教程*/</span>
        <span class="hljs-keyword">let</span> ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);
        ctx.fillStyle = <span class="hljs-string">"#ff0000"</span>;
        ctx.arc(<span class="hljs-number">50</span>,<span class="hljs-number">50</span>,<span class="hljs-number">50</span>,<span class="hljs-number">0</span>,<span class="hljs-number">2</span>*<span class="hljs-built_in">Math</span>.PI);
        ctx.fill();
        <span class="hljs-comment">/*3、将canvas作为纹理，创建Sprite*/</span>
        <span class="hljs-keyword">let</span> texture = <span class="hljs-keyword">new</span> THREE.Texture(canvas);
        texture.needsUpdate = <span class="hljs-literal">true</span>; <span class="hljs-comment">//注意这句不能少</span>
        <span class="hljs-keyword">let</span> material =  <span class="hljs-keyword">new</span> THREE.SpriteMaterial(&#123;
          <span class="hljs-attr">color</span>:<span class="hljs-number">0xff00ff</span>,<span class="hljs-comment">//设置精灵矩形区域颜色</span>
          <span class="hljs-attr">rotation</span>:<span class="hljs-built_in">Math</span>.PI/<span class="hljs-number">4</span>,<span class="hljs-comment">//旋转精灵对象45度，弧度值</span>
          <span class="hljs-attr">map</span>: texture,<span class="hljs-comment">//设置精灵纹理贴图</span>
        &#125;);
        <span class="hljs-keyword">let</span> mesh = <span class="hljs-keyword">new</span> THREE.Sprite(material);
        <span class="hljs-comment">/*4、放大图片，每个精灵有自己的大小，默认情况下都是很小的，如果你不放大，基本是看不到的*/</span>
        <span class="hljs-comment">//mesh.scale.set(100,100,1);</span>
        <span class="hljs-keyword">return</span> mesh;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后把mesh添加到scence中就能刚看到效果</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">var</span> scene = initScence();
            <span class="hljs-keyword">var</span> camera = initCamera();
            <span class="hljs-keyword">var</span> renderer = initRender()
            camera.lookAt(scene.position);
            scene.add(createSpriteShape())
            
            <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"WebGL-output"</span>).appendChild(renderer.domElement);
            render();
            <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
                requestAnimationFrame(render);
                renderer.render(scene, camera);
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf91ed16ee044c579e57d17703910414~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">.scale和.position</h3>
<p>精灵模型对象和网格模型Mesh对一样基类都是Object3D，自然精灵模型也有缩放属性<code>.scale</code>和位置属性<code>.position</code>，一般设置精灵模型的大小是通过<code>.scale</code>属性实现，而精灵模型的位置通过属性<code>.position</code>实现，精灵模型和普通模型一样，可以改变它在三维场景中的位置，区别在于精灵模型的正面一直平行于canvas画布。</p>
<p>在使用透视投影相机对象的时候，精灵模型对象显示的大小和网格模型一样受距离相机的距离影响，也就是距离越远，显示效果越小。</p>
<h2 data-id="heading-3">使用Sprite创建文字</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createSpriteText</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">//先用画布将文字画出</span>
        <span class="hljs-keyword">let</span> canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"canvas"</span>);
        <span class="hljs-keyword">let</span> ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);
        ctx.fillStyle = <span class="hljs-string">"#ffff00"</span>;
        ctx.font = <span class="hljs-string">"Bold 100px Arial"</span>;
        ctx.lineWidth = <span class="hljs-number">4</span>;
        ctx.fillText(<span class="hljs-string">"Hello World"</span>,<span class="hljs-number">4</span>,<span class="hljs-number">104</span>);
        <span class="hljs-keyword">let</span> texture = <span class="hljs-keyword">new</span> THREE.Texture(canvas);
        texture.needsUpdate = <span class="hljs-literal">true</span>;
        
        <span class="hljs-comment">//使用Sprite显示文字</span>
        <span class="hljs-keyword">let</span> material = <span class="hljs-keyword">new</span> THREE.SpriteMaterial(&#123;<span class="hljs-attr">map</span>:texture&#125;);
        <span class="hljs-keyword">let</span> textObj = <span class="hljs-keyword">new</span> THREE.Sprite(material);
        textObj.scale.set(<span class="hljs-number">0.5</span> * <span class="hljs-number">100</span>, <span class="hljs-number">0.25</span> * <span class="hljs-number">100</span>, <span class="hljs-number">0.75</span> * <span class="hljs-number">100</span>);
        textObj.position.set(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">98</span>);
        <span class="hljs-keyword">return</span> textObj;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后把textObj添加到scence中就能刚看到效果</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// once everything is loaded, we run our Three.js stuff.</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">var</span> stats = initStats();
            <span class="hljs-keyword">var</span> scene = initScence();
            <span class="hljs-keyword">var</span> camera = initCamera();
            <span class="hljs-keyword">var</span> renderer = initRender()
            camera.lookAt(scene.position);

            <span class="hljs-comment">// scene.add(createSpriteShape())</span>
            scene.add(createSpriteText())
            <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"WebGL-output"</span>).appendChild(renderer.domElement);
            render();
            <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
                stats.update();
                requestAnimationFrame(render);
                renderer.render(scene, camera);
            &#125;
        &#125;
        <span class="hljs-built_in">window</span>.onload = init

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c659105a0c04ce6aaa4e7b1b4d2df48~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">写在最后</h2>
<p>本文介绍了Three.js的Sprite相关的内容，包含了使用Sprite创建2D形状和创建文字，希望对你有帮助。</p>
<blockquote>
<p>本文发布自 云图三维大前端团队，文章未经授权禁止任何形式的转载。</p>
</blockquote></div>  
</div>
            