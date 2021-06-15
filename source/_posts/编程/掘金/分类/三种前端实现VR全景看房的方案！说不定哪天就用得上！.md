
---
title: '三种前端实现VR全景看房的方案！说不定哪天就用得上！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6aaf2a7187bc4b5eaf8f0346a2be0ec8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 19:59:50 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6aaf2a7187bc4b5eaf8f0346a2be0ec8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>事情是这样的，前几天我接到一个<code>外包工头</code>的新需求，某品牌要搭建一个在线VR展厅，用户可以在手机上通过陀螺仪或者拖动来360度全景参观展厅，这个VR展厅里会有一些信息点，点击之后可以呈现更多信息（视频，图文等）...</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6aaf2a7187bc4b5eaf8f0346a2be0ec8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我第一反应是用3D引擎，因为我不久前刚用<code>three.js</code>做过一个<code>BMW</code>的在线展厅，基本把<code>three.js</code>摸熟了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7386325890664c4e9cd36315067feef9~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-03 11_01_41.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>会另写一篇文章教大家用threejs做这个[BMW在线DIY]，感兴趣的小伙伴请关注我吧~</p>
</blockquote>
<h1 data-id="heading-1">方案一：WebGL3D引擎</h1>
<p>使用3D引擎先搭一个基本的3D场景，下面的演示使用<a href="https://github.com/mrdoob/three.js/" target="_blank" rel="nofollow noopener noreferrer">three.js</a>，同类的3D引擎我还调研过<a href="https://github.com/BabylonJS/Babylon.js" target="_blank" rel="nofollow noopener noreferrer">babylon.js</a>，<a href="https://playcanvas.com/" target="_blank" rel="nofollow noopener noreferrer">playcanvas</a>，使用都差不太多，学会一个基本都通的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> scene, camera, renderer;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initThree</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">//场景</span>
    scene = <span class="hljs-keyword">new</span> THREE.Scene();
    <span class="hljs-comment">//镜头</span>
    camera = <span class="hljs-keyword">new</span> THREE.PerspectiveCamera(<span class="hljs-number">90</span>, <span class="hljs-built_in">document</span>.body.clientWidth / <span class="hljs-built_in">document</span>.body.clientHeight, <span class="hljs-number">0.1</span>, <span class="hljs-number">100</span>);
    camera.position.set(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.01</span>);
    <span class="hljs-comment">//渲染器</span>
    renderer = <span class="hljs-keyword">new</span> THREE.WebGLRenderer();
    renderer.setSize(<span class="hljs-built_in">document</span>.body.clientWidth, <span class="hljs-built_in">document</span>.body.clientHeight);
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"container"</span>).appendChild(renderer.domElement);
    <span class="hljs-comment">//镜头控制器</span>
    <span class="hljs-keyword">var</span> controls = <span class="hljs-keyword">new</span> THREE.OrbitControls(camera, renderer.domElement);
    
    <span class="hljs-comment">//一会儿在这里添加3D物体</span>

    loop();
&#125;

<span class="hljs-comment">//帧同步重绘</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loop</span>(<span class="hljs-params"></span>) </span>&#123;
    requestAnimationFrame(loop);
    renderer.render(scene, camera);
&#125;

<span class="hljs-built_in">window</span>.onload = initThree;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们能看到一个黑乎乎的世界，因为现在<code>scene</code>里什么都没有，接着我们要把三维物体放进去了，使用3D引擎的实现方式无非都是以下几种</p>
<h2 data-id="heading-2">使用立方体（box）实现</h2>
<blockquote>
<p>这种方式最容易理解，我们在一个房间里，看向天花板，地面，正面，左右两面，背面共计六面。我们把所有六个视角拍成照片就得到下面六张图</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de9a7837404741528d39b13f516f58a4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在我们直接使用立方体（box）搭出这样一个房间</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> materials = [];
<span class="hljs-comment">//根据左右上下前后的顺序构建六个面的材质集</span>
<span class="hljs-keyword">var</span> texture_left = <span class="hljs-keyword">new</span> THREE.TextureLoader().load( <span class="hljs-string">'./images/scene_left.jpeg'</span> );
materials.push( <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial( &#123; <span class="hljs-attr">map</span>: texture_left&#125; ) );

<span class="hljs-keyword">var</span> texture_right = <span class="hljs-keyword">new</span> THREE.TextureLoader().load( <span class="hljs-string">'./images/scene_right.jpeg'</span> );
materials.push( <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial( &#123; <span class="hljs-attr">map</span>: texture_right&#125; ) );

<span class="hljs-keyword">var</span> texture_top = <span class="hljs-keyword">new</span> THREE.TextureLoader().load( <span class="hljs-string">'./images/scene_top.jpeg'</span> );
materials.push( <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial( &#123; <span class="hljs-attr">map</span>: texture_top&#125; ) );

<span class="hljs-keyword">var</span> texture_bottom = <span class="hljs-keyword">new</span> THREE.TextureLoader().load( <span class="hljs-string">'./images/scene_bottom.jpeg'</span> );
materials.push( <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial( &#123; <span class="hljs-attr">map</span>: texture_bottom&#125; ) );

<span class="hljs-keyword">var</span> texture_front = <span class="hljs-keyword">new</span> THREE.TextureLoader().load( <span class="hljs-string">'./images/scene_front.jpeg'</span> );
materials.push( <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial( &#123; <span class="hljs-attr">map</span>: texture_front&#125; ) );

<span class="hljs-keyword">var</span> texture_back = <span class="hljs-keyword">new</span> THREE.TextureLoader().load( <span class="hljs-string">'./images/scene_back.jpeg'</span> );
materials.push( <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial( &#123; <span class="hljs-attr">map</span>: texture_back&#125; ) );

<span class="hljs-keyword">var</span> box = <span class="hljs-keyword">new</span> THREE.Mesh( <span class="hljs-keyword">new</span> THREE.BoxGeometry( <span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span> ), materials );
scene.add(box);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f10e5ddca004406a63e77d9504c3dc4~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-14 19_51_17.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好，现在我们把镜头camera（也就是人的视角），放到box内，并且让所有贴图向内翻转后，VR全景就实现了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">box.geometry.scale( <span class="hljs-number">1</span>, <span class="hljs-number">1</span>, -<span class="hljs-number">1</span> );
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>现在我们进入了这个盒子！！</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28cd30c5469e43379e3a41ab4edae83d~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-14 19_41_37.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://github.com/mrdoob/three.js/blob/master/examples/webgl_panorama_cube.html" target="_blank" rel="nofollow noopener noreferrer">threejs官方立方体全景示例</a></p>
<h2 data-id="heading-3">使用球体（sphere）实现</h2>
<blockquote>
<p>我们将房间360度球形范围内所有的光捕捉到一个图片上，再将这张图片展开为矩形，就能得到这样一张全景图片</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27becc372074417a9ce02ca06f579eb2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> sphereGeometry = <span class="hljs-keyword">new</span> THREE.SphereGeometry(<span class="hljs-comment">/*半径*/</span><span class="hljs-number">1</span>, <span class="hljs-comment">/*垂直节点数量*/</span><span class="hljs-number">50</span>, <span class="hljs-comment">/*水平节点数量*/</span><span class="hljs-number">50</span>);<span class="hljs-comment">//节点数量越大，需要计算的三角形就越多，影响性能</span>

<span class="hljs-keyword">var</span> sphere = <span class="hljs-keyword">new</span> THREE.Mesh(sphereGeometry);
sphere.material.wireframe  = <span class="hljs-literal">true</span>;<span class="hljs-comment">//用线框模式大家可以看得清楚是个球体而不是圆形</span>
scene.add(sphere);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20e437117a654ba2b51ce1d47696de5b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在我们把这个全景图片贴到这个球体上</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> texture = <span class="hljs-keyword">new</span> THREE.TextureLoader().load(<span class="hljs-string">'./images/scene.jpeg'</span>);
<span class="hljs-keyword">var</span> sphereMaterial = <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial(&#123;<span class="hljs-attr">map</span>: texture&#125;);

<span class="hljs-keyword">var</span> sphere = <span class="hljs-keyword">new</span> THREE.Mesh(sphereGeometry,sphereMaterial);
<span class="hljs-comment">// sphere.material.wireframe  = true;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5083e0cc881549d883d788c97fddf3d8~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-14 14_54_38.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>和之前一样，我们把镜头camera（也就是人的视角），放到球体内，并且让所有贴图向内翻转后，VR全景就实现了</p>
<p><strong>现在我们进入了这个球体！！</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> sphereGeometry = <span class="hljs-keyword">new</span> THREE.SphereGeometry(<span class="hljs-comment">/*半径*/</span><span class="hljs-number">1</span>, <span class="hljs-number">50</span>, <span class="hljs-number">50</span>);
sphereGeometry.scale(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, -<span class="hljs-number">1</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1875fc36e0ef40a9a0c4c12fb9512ce5~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-14 15_15_28.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://github.com/mrdoob/three.js/blob/master/examples/webgl_panorama_equirectangular.html" target="_blank" rel="nofollow noopener noreferrer">threejs官方球体全景示例</a></p>
<h2 data-id="heading-4">添加信息点</h2>
<blockquote>
<p>在VR全景中，我们需要放置一些信息点，用户点击之后做一些动作。</p>
</blockquote>
<p>现在我们建立这样一个点的数组</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> hotPoints=[
    &#123;
        <span class="hljs-attr">position</span>:&#123;
            <span class="hljs-attr">x</span>:<span class="hljs-number">0</span>,
            <span class="hljs-attr">y</span>:<span class="hljs-number">0</span>,
            <span class="hljs-attr">z</span>:-<span class="hljs-number">0.2</span>
        &#125;,
        <span class="hljs-attr">detail</span>:&#123;
            <span class="hljs-string">"title"</span>:<span class="hljs-string">"信息点1"</span>
        &#125;
    &#125;,
    &#123;
        <span class="hljs-attr">position</span>:&#123;
            <span class="hljs-attr">x</span>:-<span class="hljs-number">0.2</span>,
            <span class="hljs-attr">y</span>:-<span class="hljs-number">0.05</span>,
            <span class="hljs-attr">z</span>:<span class="hljs-number">0.2</span>
        &#125;,
        <span class="hljs-attr">detail</span>:&#123;
            <span class="hljs-string">"title"</span>:<span class="hljs-string">"信息点2"</span>
        &#125;
    &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遍历这个数组，并将信息点的指示图添加到3D场景中</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> pointTexture = <span class="hljs-keyword">new</span> THREE.TextureLoader().load(<span class="hljs-string">'images/hot.png'</span>);
<span class="hljs-keyword">var</span> material = <span class="hljs-keyword">new</span> THREE.SpriteMaterial( &#123; <span class="hljs-attr">map</span>: pointTexture&#125; );

<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>;i<hotPoints.length;i++)&#123;
    <span class="hljs-keyword">var</span> sprite = <span class="hljs-keyword">new</span> THREE.Sprite( material );
    sprite.scale.set( <span class="hljs-number">0.1</span>, <span class="hljs-number">0.1</span>, <span class="hljs-number">0.1</span> );
    sprite.position.set( hotPoints[i].position.x, hotPoints[i].position.y, hotPoints[i].position.z );

   scene.add( sprite );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>看到HOT指示图了吗？</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b83bc4c6ef9247a5afefc82b0a6fa4b7~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-14 20_22_12.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>添加点击事件，首先将全部的sprite放到一个数组里</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">sprite.detail = hotPoints[i].detail;
poiObjects.push(sprite);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们通过射线检测（raycast），就像是镜头中心向鼠标所点击的方向发射出一颗子弹，去检查这个子弹最终会打中哪些物体。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdad02da56f94068bfda680fdd44cf73~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-15 01_35_14.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#container"</span>).addEventListener(<span class="hljs-string">"click"</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
    event.preventDefault();

    <span class="hljs-keyword">var</span> raycaster = <span class="hljs-keyword">new</span> THREE.Raycaster();
    <span class="hljs-keyword">var</span> mouse = <span class="hljs-keyword">new</span> THREE.Vector2();

    mouse.x = ( event.clientX / <span class="hljs-built_in">document</span>.body.clientWidth ) * <span class="hljs-number">2</span> - <span class="hljs-number">1</span>;
    mouse.y = - ( event.clientY / <span class="hljs-built_in">document</span>.body.clientHeight ) * <span class="hljs-number">2</span> + <span class="hljs-number">1</span>;

    raycaster.setFromCamera( mouse, camera );

    <span class="hljs-keyword">var</span> intersects = raycaster.intersectObjects( poiObjects );
    <span class="hljs-keyword">if</span>(intersects.length><span class="hljs-number">0</span>)&#123;
        alert(<span class="hljs-string">"点击了热点"</span>+intersects[<span class="hljs-number">0</span>].object.detail.title);
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">方案二：CSS3D</h1>
<p><code>threejs</code>等3d引擎太强大了，这些引擎的代码量都有大几百K，在今天的网速下显得无所谓，但在几年前我接到需求时仍然是重要的考量因素。既然我们只用到3D引擎的一点点功能，那么能否找到一个更加轻量的3D引擎呢。</p>
<p>有！<a href="https://github.com/shrekshrek/css3d-engine" target="_blank" rel="nofollow noopener noreferrer">css3d-engine</a>，这个3d引擎只有<code>14kb</code>，并且在多个大牌商业项目中应用</p>
<ul>
<li>淘宝造物节 <a href="https://shrek.imdevsh.com/show/zwj/" target="_blank" rel="nofollow noopener noreferrer">shrek.imdevsh.com/show/zwj/</a></li>
<li>adidas绝不凋谢 <a href="https://shrek.imdevsh.com/show/drose/" target="_blank" rel="nofollow noopener noreferrer">shrek.imdevsh.com/show/drose/</a></li>
<li>adidas胜势全开 <a href="https://shrek.imdevsh.com/show/bbcny/" target="_blank" rel="nofollow noopener noreferrer">shrek.imdevsh.com/show/bbcny/</a></li>
<li>adidas绝不跟随 <a href="https://shrek.imdevsh.com/show/crazylight/" target="_blank" rel="nofollow noopener noreferrer">shrek.imdevsh.com/show/crazyl…</a></li>
</ul>
<h2 data-id="heading-6">使用skybox实现</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.onload=initCSS3D;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initCSS3D</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> s = <span class="hljs-keyword">new</span> C3D.Stage();
    s.size(<span class="hljs-built_in">window</span>.innerWidth, <span class="hljs-built_in">window</span>.innerHeight).update();
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'container'</span>).appendChild(s.el);

    <span class="hljs-keyword">var</span> box = <span class="hljs-keyword">new</span> C3D.Skybox();
    box.size(<span class="hljs-number">954</span>).position(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>).material(&#123;
        <span class="hljs-attr">front</span>: &#123;<span class="hljs-attr">image</span>: <span class="hljs-string">"images/scene_front.jpeg"</span>&#125;,
        <span class="hljs-attr">back</span>: &#123;<span class="hljs-attr">image</span>: <span class="hljs-string">"images/scene_back.jpeg"</span>&#125;,
        <span class="hljs-attr">left</span>: &#123;<span class="hljs-attr">image</span>: <span class="hljs-string">"images/scene_right.jpeg"</span>&#125;,
        <span class="hljs-attr">right</span>: &#123;<span class="hljs-attr">image</span>: <span class="hljs-string">"images/scene_left.jpeg"</span>&#125;,
        <span class="hljs-attr">up</span>: &#123;<span class="hljs-attr">image</span>: <span class="hljs-string">"images/scene_top.jpeg"</span>&#125;,
        <span class="hljs-attr">down</span>: &#123;<span class="hljs-attr">image</span>: <span class="hljs-string">"images/scene_bottom.jpeg"</span>&#125;,

    &#125;).update();
    s.addChild(box);

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loop</span>(<span class="hljs-params"></span>) </span>&#123;
        angleX += (curMouseX - lastMouseX + lastAngleX - angleX) * <span class="hljs-number">0.3</span>;
        angleY += (curMouseY - lastMouseY + lastAngleY - angleY) * <span class="hljs-number">0.3</span>;

        s.camera.rotation(angleY, -angleX, <span class="hljs-number">0</span>).updateT();
        requestAnimationFrame(loop);
    &#125;

    loop();

    <span class="hljs-keyword">var</span> lastMouseX = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">var</span> lastMouseY = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">var</span> curMouseX = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">var</span> curMouseY = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">var</span> lastAngleX = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">var</span> lastAngleY = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">var</span> angleX = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">var</span> angleY = <span class="hljs-number">0</span>;

    <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">"mousedown"</span>, mouseDownHandler);
    <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">"mouseup"</span>, mouseUpHandler);

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mouseDownHandler</span>(<span class="hljs-params">evt</span>) </span>&#123;
        lastMouseX = curMouseX = evt.pageX;
        lastMouseY = curMouseY = evt.pageY;
        lastAngleX = angleX;
        lastAngleY = angleY;

        <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">"mousemove"</span>, mouseMoveHandler);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mouseMoveHandler</span>(<span class="hljs-params">evt</span>) </span>&#123;
        curMouseX = evt.pageX;
        curMouseY = evt.pageY;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mouseUpHandler</span>(<span class="hljs-params">evt</span>) </span>&#123;
        curMouseX = evt.pageX;
        curMouseY = evt.pageY;

        <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">"mousemove"</span>, mouseMoveHandler);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方案二的好处除了库很小以外，还是div+css来搭建三维场景的。但这个库的作者几乎不维护，遇到问题必须得自己想办法解决，比如使用在电脑上会看到明显的面片边缘</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0550ab3eae6f48399dab58334f3d85ed~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是在手机上浏览的话表现还是相当完美的</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b89d376ff6b4fac8149d9c91c6a775c~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-14 22_20_26.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">添加信息点</h2>
<p>我们继续为它添加可交互的信息点</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> hotPoints=[
    &#123;
        <span class="hljs-attr">position</span>:&#123;
            <span class="hljs-attr">x</span>:<span class="hljs-number">0</span>,
            <span class="hljs-attr">y</span>:<span class="hljs-number">0</span>,
            <span class="hljs-attr">z</span>:-<span class="hljs-number">476</span>
        &#125;,
        <span class="hljs-attr">detail</span>:&#123;
            <span class="hljs-string">"title"</span>:<span class="hljs-string">"信息点1"</span>
        &#125;
    &#125;,
    &#123;
        <span class="hljs-attr">position</span>:&#123;
            <span class="hljs-attr">x</span>:<span class="hljs-number">0</span>,
            <span class="hljs-attr">y</span>:<span class="hljs-number">0</span>,
            <span class="hljs-attr">z</span>:<span class="hljs-number">476</span>
        &#125;,
        <span class="hljs-attr">detail</span>:&#123;
            <span class="hljs-string">"title"</span>:<span class="hljs-string">"信息点2"</span>
        &#125;
    &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initPoints</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> poiObjects = [];
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>;i<hotPoints.length;i++)&#123;
        <span class="hljs-keyword">var</span> _p = <span class="hljs-keyword">new</span> C3D.Plane();

        _p.size(<span class="hljs-number">207</span>, <span class="hljs-number">162</span>).position(hotPoints[i].position.x,hotPoints[i].position.y,hotPoints[i].position.z).material(&#123;
            <span class="hljs-attr">image</span>: <span class="hljs-string">"images/hot.png"</span>,
            <span class="hljs-attr">repeat</span>: <span class="hljs-string">'no-repeat'</span>,
            <span class="hljs-attr">bothsides</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">//注意这个两面贴图的属性</span>
        &#125;).update();
        s.addChild(_p);

        _p.el.detail = hotPoints[i].detail;

        _p.on(<span class="hljs-string">"click"</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(e.target.detail.title);
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以显示信息点了，并且由于是div，我们非常容易添加鼠标点击交互等效果</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/322d2694cc0a4fccade31d54c19d749a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不过，<code>bothsides</code>属性为true时，背面的信息点图片是反的。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56c751dda5054eb697f86ee960d049d9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以我们这里要做一点处理，根据其与相机的夹角重置一下信息点的旋转角度。（<code>如果是那种怎么旋转都无所谓的图片，比如圆点则无需处理</code>）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> r = <span class="hljs-built_in">Math</span>.atan2(hotPoints[i].position.z-<span class="hljs-number">0</span>,<span class="hljs-number">0</span>-<span class="hljs-number">0</span>) * <span class="hljs-number">180</span> / <span class="hljs-built_in">Math</span>.PI+<span class="hljs-number">90</span>;
_p.size(<span class="hljs-number">207</span>, <span class="hljs-number">162</span>).position(hotPoints[i].position.x,hotPoints[i].position.y,hotPoints[i].position.z).material(&#123;
            <span class="hljs-attr">image</span>: <span class="hljs-string">"images/hot.png"</span>,
            <span class="hljs-attr">repeat</span>: <span class="hljs-string">'no-repeat'</span>,
            <span class="hljs-attr">bothsides</span>: <span class="hljs-literal">false</span>,
        &#125;).update();
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">需求升级了！</h1>
<p>以上两个方案，我以为可以给客户交差了。但客户又提出了一些想法</p>
<ul>
<li>
<p><strong>全景图质量需要更高，但加载速度不允许更慢</strong></p>
</li>
<li>
<p><strong>每个场景的信息点挺多的，坐标编辑太麻烦了</strong></p>
</li>
</ul>
<p>当时我心里想，总共才收你万把块钱，难不成还得给你定制个引擎，再做个可视化编辑器？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/447ed6e19cc04dc1aa00499729d12eeb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>直到客户发过来一个参考链接，我看完<code>惊呆了</code>，全景图非常清晰，但首次加载速度极快，像百度地图一样，是一块块从模糊到清晰被加载出来的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5afe3486f7584d8a8e14a5111b91f082~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-14 23_31_28.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过检查参考链接网页的代码，发现了方案三</p>
<h1 data-id="heading-9">方案三：pano2vr</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ea232a0cb834c9f9aaab05007a0dff0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>pano2vr是一款所见即所得的全景VR制作软件（正版149欧元），功能挺强大的，可以直接输出成HTML5静态网页，体验非常不错。</p>
<p>而其核心库<code>pano2vr_player.js</code>代码量也只有<code>238kb</code>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e88bcbbb4da84e26b9c6d62da2a9e48c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以直接使用这个软件来可视化的添加信息点，输出成HTML5后，除了静态图片以外，所有配置信息都在这个<code>pano.xml</code>文件里</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efad4f180a204623b4796d2194e165d3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">修改信息点图片</h2>
<p>整体的交互体验都非常好，但默认的信息点样式不喜欢，我们可以通过下面的代码来修改信息点图片</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">pano.readConfigUrlAsync(<span class="hljs-string">"pano.xml"</span>,<span class="hljs-function">()=></span>&#123;
    <span class="hljs-keyword">var</span> pois=pano.getPointHotspotIds();

    <span class="hljs-keyword">var</span> hotScale = <span class="hljs-number">0.2</span>;

    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>;i<pois.length;i++)&#123;
            <span class="hljs-keyword">var</span> ids=pois[i];
            <span class="hljs-keyword">var</span> hotsopt=pano.getHotspot(ids);
            hotsopt.div.firstChild.src=<span class="hljs-string">"images/hot.png"</span>;
            hotsopt.div.firstChild.style.width = <span class="hljs-number">207</span>*hotScale+<span class="hljs-string">"px"</span>;
            hotsopt.div.firstChild.style.height = <span class="hljs-number">162</span>*hotScale+<span class="hljs-string">"px"</span>;
            hotsopt.div.onmouseover = <span class="hljs-literal">null</span>;
            hotsopt.div.setAttribute(<span class="hljs-string">"ids"</span>,ids);
            hotsopt.div.onclick=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
                   <span class="hljs-comment">//在这里可以响应信息点的点击事件啦</span>
                   <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.getAttribute(<span class="hljs-string">"ids"</span>));
            &#125;;
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>哈哈，没想到最终的方案不仅极其简单的就实现了体验良好的VR全景，还附送了非常方便的信息点编辑。除去第一次开发的耗时，以后再制作新的VR场景也就是花个10分钟即可搞定。</p>
<p>但想到<code>外包工头</code>经常<em>压榨我的报价，压缩我的工期，无理变更需求</em></p>
<p>收到工程款的时候他请我去K歌，坐在KTV的包间里我没有告诉他使用pano2vr的事，而是对他说</p>
<p><strong>每个VR场景的信息点都要花1天时间编辑</strong></p>
<p><strong>每制作一个新的VR场景，你收品牌方8k</strong></p>
<p><strong>我每个场景收你3k，你躺赚5k</strong></p>
<p><strong>毕竟咱们老朋友了，我够意思吧</strong></p>
<p>他豪爽的干掉手中的啤酒说：“好兄弟，我给你唱一首！”</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01636d045c7b4c0c9995faa21ad7c5e1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>本故事纯属虚构，文末配图如有侵权，请联系我跟老板大哥喝一杯</p>
<p><a href="https://www.bilibili.com/video/BV1bf4y1t7QE/" target="_blank" rel="nofollow noopener noreferrer">查看本文配套视频教程</a></p>
<h1 data-id="heading-11">源码</h1>
<p>微信搜索并关注“<code>大帅老猿</code>”，回复“<code>webvr</code>”获得本文中三种方案的实现源码</p>
<blockquote>
<p>如果觉得我是个有趣的程序员，请关注我；如果觉得本文还不错，记得点赞收藏哦，说不定哪天就用得上！</p>
</blockquote></div>  
</div>
            