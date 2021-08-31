
---
title: 'Three.js初探'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e16dbf3669174690b8a11724bbb1e2e4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 01:46:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e16dbf3669174690b8a11724bbb1e2e4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Three.js 是一个3d的基础库，学习它可以帮助我们打开3d的大门。</p>
<h2 data-id="heading-0">说在前面的话</h2>
<p>由于学习图形学需要很深的数学基础，才能理解原生API的使用，这导致对于普通程序员来说学习成本太大。而Threejs 很友好的封装了原生API，通过对数据结构和设计模式的封装，以一个更利于理解的角度阐述了3D世界，所以我打算先从Threejs开始学习，由浅入深理解原理。</p>
<h2 data-id="heading-1">Three.js 的重要概念</h2>
<h3 data-id="heading-2">主要概念：</h3>
<ol>
<li>渲染器</li>
<li>相机</li>
</ol>

<ol start="3">
<li>几何体</li>
<li>光照</li>
</ol>
<h3 data-id="heading-3">辅助工具：</h3>
<ol>
<li>动画函数</li>
<li>用户界面操作库</li>
</ol>

<ol start="3">
<li>帧率监控库</li>
</ol>
<h2 data-id="heading-4">一道简单的开胃菜</h2>
<pre><code class="copyable"><html>
  <style>
       body &#123;
       /* set margin to 0 and overflow to hidden, to go fullscreen */
         margin: 0;
         overflow: hidden;
       &#125;
  </style>
<body>
  <div id='WebGL-output'></div>
  <script src="./src/index.ts"></script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import &#123; Scene,WebGL1Renderer,PerspectiveCamera, Color, AxesHelper&#125; from "three";

window.onload = init;

function init() &#123;
  const renderer = new WebGL1Renderer();
  const scene = new Scene();
  const camera = new PerspectiveCamera();
  // render the scene
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setClearColor(new Color(0xEEEEEE));
  camera.lookAt(scene.position);
  renderer.render(scene, camera);
  // add the output of the renderer to the html element
  document.getElementById("WebGL-output").appendChild(renderer.domElement);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码里面已经基本包含了Threejs的核心三要素；<strong>渲染器（WebGL1Renderer），照相机(PerspectiveCamera)，场景(Scene);</strong></p>
<p><strong>照相机：</strong> 是一个视角的概念，就是你看到的东西；camera.lookAt 表示你朝那个方向看。由于我们在一个3D世界，所以就算不站着不动，只要你原地旋转，看的东西也是不一样的。</p>
<p><strong>场景：</strong> 类似画布的概念，就是你想在画布上放些啥。</p>
<p><strong>渲染器：</strong> 渲染虚拟物体的载体。只有将场景和相机扔给渲染器渲染；显示器才能展示真实的物体。</p>
<p><strong>理解了上面的概念，运行上面的代码发现页面中并没有任何东西。那是因为我们没有往场景中添加东西。添加了东西我们就可以物体了。</strong></p>
<hr>
<h2 data-id="heading-5">理解坐标系</h2>
<p>在3D世界中，有一个三维坐标系的概念。坐标系就是代表物体在虚拟世界的位置。有了他，我们就很容易找到自己的位置，不容易迷失方向</p>
<p><strong>接着上面的例子，我们把辅助坐标系添加到场景中，并调整相机的视角，这样在页面中就可以看到坐标系了。</strong></p>
<pre><code class="copyable">import &#123; Scene,WebGL1Renderer,PerspectiveCamera, Color, AxesHelper&#125; from "three";

function init() &#123;
  const renderer = new WebGL1Renderer();
  const scene = new Scene();
  const camera = new PerspectiveCamera();
  // render the scene
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setClearColor(new Color(0xEEEEEE));
  // position and point the camera to the center of the scene
  camera.position.x = -40;// 红线是X轴
  camera.position.y = 30; // 蓝线是y轴
  camera.position.z = 30; // 绿线是Z轴

  // show axes in the screen
  const axes = new AxesHelper(10);
  scene.add(axes);
  console.log(scene.position);

  camera.lookAt(scene.position);
  renderer.render(scene, camera);

  // add the output of the renderer to the html element
  document.getElementById("WebGL-output").appendChild(renderer.domElement);
&#125;

 window.onload = init;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意点：调整相机的视角，就相当于调整眼睛看的方向。</strong></p>
<hr>
<p><strong>页面的效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e16dbf3669174690b8a11724bbb1e2e4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们分别看到了红线，蓝线，绿线，分别对应X轴，Y轴，Z轴。</p>
<ul>
<li>
<p><strong>红线是X轴</strong></p>
</li>
<li>
<p><strong>蓝线是y轴</strong></p>
</li>
<li>
<p><strong>绿线是Z轴</strong></p>
</li>
</ul>
<p><strong>源码：</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhpstream%2Fthree-demo%2Ftree%2Fmaster%2Fdemo%2Findex" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/hpstream/three-demo/tree/master/demo/index" ref="nofollow noopener noreferrer">github.com/hpstream/th…</a></p>
<p><strong>代码演示：</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fhpstream.github.io%2Fthree-demo%2Findex%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://hpstream.github.io/three-demo/index/index.html" ref="nofollow noopener noreferrer">hpstream.github.io/three-demo/…</a></p>
<h2 data-id="heading-6">了解几何体(Geometry)</h2>
<p>几何体是数学中的概念，如：球体，立方体，平面体。它本质上是一种对现实的抽象。像现实中的球，抽象成数学概念就是球体，<strong>那么球，和球体存在着什么联系呢？</strong></p>
<p><strong>个人理解：</strong></p>
<p><strong>球体(几何体) + 材料(材质) = 球(实体)</strong></p>
<hr>
<p>代码的展示形式：</p>
<pre><code class="copyable"> var shpereGeometry = new SphereGeometry(8,20,20)
 var shpereMeterial = new MeshBasicMaterial(&#123;color:0x7777ff,wireframe:true&#125;)
 var shpere = new Mesh(shpereGeometry,shpereMeterial)
 
 shpere.position.x = -10;
 shpere.position.y = 10;
 shpere.position.z = -10;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>通过</strong> SphereGeometry 创建几何体的骨架，MeshBasicMaterial 创建材质， 通过材质和骨架的组合，就可以创建一个球。通过调整位置，让球在我们创造的虚拟世界移动。</p>
<h2 data-id="heading-7">学会使用常见的几何体</h2>
<pre><code class="copyable">import &#123; Scene,WebGL1Renderer,PerspectiveCamera, Color, AxesHelper, PlaneGeometry, MeshBasicMaterial, Mesh, BoxGeometry, SphereGeometry&#125; from "three";

let renderer: WebGL1Renderer, scene: Scene, camera: PerspectiveCamera;

function paintGeometry() &#123;
   // 绘画一个灰色，平面几何体
   const planeGeometry = new PlaneGeometry(20, 20);
   const planeMaterial = new MeshBasicMaterial(&#123; color: 0xcccccc &#125;);
   var plane = new Mesh(planeGeometry, planeMaterial);
   plane.rotation.x = -0.5 * Math.PI;
   scene.add(plane);
   // 绘画一个立方体
   var cubeGeometry = new BoxGeometry(4,4,4)
   var cubeMaterial = new MeshBasicMaterial(&#123;color:0xff0000,wireframe:true&#125;)
   var cube = new Mesh(cubeGeometry,cubeMaterial)
   cube.position.x = 2;
   cube.position.y = 2;
   cube.position.z = 2;
   scene.add(cube)
   // 绘画一个球体
   var shpereGeometry = new SphereGeometry(8,20,20)
   var shpereMeterial = new MeshBasicMaterial(&#123;color:0x7777ff,wireframe:true&#125;)
   var shpere = new Mesh(shpereGeometry,shpereMeterial)
   shpere.position.x = -10;
   shpere.position.y = 10;
   shpere.position.z = -10;
   scene.add(shpere);
&#125;

function init() &#123;
  //... 
  //...
  paintGeometry();

 // ...
  document.getElementById("WebGL-output").appendChild(renderer.domElement);
&#125;

window.onload = init;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>scene.add(cube); 将立方体放进场景中</strong></p>
<p>案例图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5831bbbde6f94f16ba1ab5fb1e90fe29~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>源码：</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhpstream%2Fthree-demo%2Ftree%2Fmaster%2Fdemo%2Findex2" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/hpstream/three-demo/tree/master/demo/index2" ref="nofollow noopener noreferrer">github.com/hpstream/th…</a></p>
<p><strong>代码演示：</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fhpstream.github.io%2Fthree-demo%2Findex%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://hpstream.github.io/three-demo/index/index.html" ref="nofollow noopener noreferrer">hpstream.github.io/three-demo/…</a></p>
<hr>
<h2 data-id="heading-8">光照与反光材料</h2>
<p>光打在物体上，我们就能看到物体的反射的光，其实在3D的虚拟世界，也是一样可以看到的。只不过我们需要使用光源和特殊的反光材料才能实现。</p>
<pre><code class="copyable">const spotLight = new SpotLight(0xffffff);
spotLight.position.set(-40, 60, -10);
spotLight.castShadow = true;
scene.add(spotLight);


var cubeGeometry = new BoxGeometry(4, 4, 4);
// 反光材料
var cubeMaterial = new MeshLambertMaterial(&#123;
    color: 0xff0000,
   //  wireframe: true,
&#125;);
var cube = new Mesh(cubeGeometry, cubeMaterial);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SpotLight 创建一个点光源，放入场景中， 将立方体的材质换成可以反光的MeshLambertMaterial材质，就可以看到光照的效果了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aabb0abaa4f148f3807ab22955645bca~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>源码：</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhpstream%2Fthree-demo%2Ftree%2Fmaster%2Fdemo%2Findex3" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/hpstream/three-demo/tree/master/demo/index3" ref="nofollow noopener noreferrer">github.com/hpstream/th…</a></p>
<p><strong>代码演示：</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fhpstream.github.io%2Fthree-demo%2Findex%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://hpstream.github.io/three-demo/index/index.html" ref="nofollow noopener noreferrer">hpstream.github.io/three-demo/…</a></p>
<h2 data-id="heading-9">动画与辅助函数的使用</h2>
<p>requestAnimationFrame 是浏览器提供的一个动画函数，我们可以使用这个函数制动动画效果，其基本思路就是在每一帧改变物体的位置，这样子连续的看起来就是动画了。</p>
<pre><code class="copyable">function renderScene() &#123;
    cube.rotation.x += 0.2;
    cube.rotation.y += 0.2;
    cube.rotation.z += 0.2
    // render using requestAnimationFrame
    requestAnimationFrame(renderScene);
    renderer.render(scene, camera);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 requestAnimationFrame 不停的让几何体旋转起来。就可以看到动画了。</p>
<p>由于动画可能会影响页面帧率，导致页面卡顿，所以我们在最好有一个工具可能检测浏览器的刷新频率，我们<strong>使用stats.js来监听页面的帧率</strong></p>
<pre><code class="copyable">import Stats from "stats.js";


function initStats() &#123;
  stats = new Stats();
  stats.showPanel(2); // 0: fps, 1: ms
  stats.dom.style.position = "absolute";
  stats.dom.style.left = "0px";
  stats.dom.style.top = "0px";

  document.getElementById("Stats-output").appendChild(stats.dom);

  return stats;
&#125;

 function renderScene() &#123;
    stats.update();
    // ...
    // ...
    renderer.render(scene, camera);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在做动画时，可能经常需要调整几何体的位置参数。但是频繁改动代码显得非常麻烦，而<strong>dat.gui 这个库可以很友好的帮助我们在页面修改参数，看页面效果</strong>。</p>
<pre><code class="copyable">import * as dat from "dat.gui";
const gui = new dat.GUI();
var controls = new (function () &#123;
  this.rotationSpeed = 0.02;
  this.bouncingSpeed = 0.03;
&#125;)();
 gui.add(controls, "rotationSpeed", 0, 0.5);
 gui.add(controls, "bouncingSpeed", 0, 0.5);


function renderScene() &#123;
    stats.update();
    cube.rotation.x += controls.rotationSpeed;
    cube.rotation.y += controls.rotationSpeed;
    cube.rotation.z += controls.rotationSpeed;

    // bounce the sphere up and down
    step += controls.bouncingSpeed;
    sphere.position.x = 0 + 10 * Math.cos(step);
    sphere.position.y = 2 + 10 * Math.abs(Math.sin(step));
    // render using requestAnimationFrame
    requestAnimationFrame(renderScene);
    renderer.render(scene, camera);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>案例示意图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f0575860a554d109081bded042d32f4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>源码：</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhpstream%2Fthree-demo%2Ftree%2Fmaster%2Fdemo%2Findex4" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/hpstream/three-demo/tree/master/demo/index4" ref="nofollow noopener noreferrer">github.com/hpstream/th…</a></p>
<p><strong>代码演示：</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fhpstream.github.io%2Fthree-demo%2Findex%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://hpstream.github.io/three-demo/index/index.html" ref="nofollow noopener noreferrer">hpstream.github.io/three-demo/…</a></p>
<h2 data-id="heading-10">总结</h2>
<p>通过上面知识点的讲解，我们理解了3D世界的基本要素，和一些辅助工具。基本上算是打开了我们3D世界的大门。接下来我会对每一个要素展开讲解，尽情期待吧。</p></div>  
</div>
            