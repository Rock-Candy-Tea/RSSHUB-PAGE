
---
title: '在 Threejs 中自己实现一套阴影'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eefbe497befd4d8bbd4576b56716ae8c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Apr 2021 22:59:59 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eefbe497befd4d8bbd4576b56716ae8c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一. 背景</h2>
<p>  Threejs 给我们封装的阴影虽然简单易用，但太过上层，不够灵活。
  之前在预研厘米秀新形象时，需要把 Unity 中的着色器代码“翻译”到 Threejs 的自定义材质中。我们发现新形象在 Unity 中定义的第一个 PASS 依赖于阴影，也就是说我们需要必须先拿到阴影数据，才能再对后续的 PASS 进行“翻译”。但是 Threejs 并不会给我们提供阴影信息。另外，就算真的可以通过各种操作拿到 Threejs 生成的阴影纹理，我们也还是需要在自定义材质中通过着色器来理解以及消费它。
  综上，干脆在 Threejs 上自己实现一套阴影，足够灵活，也能自己把握细节。</p>
<h2 data-id="heading-1">二. 阴影是如何产生的</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eefbe497befd4d8bbd4576b56716ae8c~tplv-k3u1fbpfcp-watermark.image" alt="1619512717_62_w564_h438.png" loading="lazy" referrerpolicy="no-referrer"><br>
在自然界中，一个不自发光的物体要被看见，是需要光源照射的。由于光是沿直线传播的，当光线被某些物体(图中橘色物体)遮挡后，那些本来有颜色的区域(点C)因为没有照射而变回黑色，这些区域就是阴影。</p>
<h2 data-id="heading-2">三. 如何用 ShadowMap 生成阴影</h2>
<p>  理论上，在绘制点的颜色时，只要判断该点有没有被“遮挡”，就知道是否要绘制成阴影。而判断“遮挡”的方案有很多，最常用的就是 ShadowMap。
  我们只要知道该点与光源的连线上，有没有比它离光源更近的点存在。其中点与光源的距离，在 ShadowMap 中就是深度。具体的做法是：</p>
<ul>
<li>(1) 生成深度纹理图：所谓深度纹理图，就是每个位置的最小深度。我们站在光源的位置，按照光线传播的视角，观察场景，计算场景中的物体距离光源的距离(也就是该视角下的深度)，并记录各个位置上的最小值，从而获得一张深度纹理。</li>
<li>(2) 使用深度纹理图：对于世界中的某个点 p，我们要先得到它在光源视角下的深度，再和深度纹理图中对应的深度进行比较，就可以判定它是否在阴影中了。</li>
</ul>
<p>  ps: 更多关于 ShadowMap 生成阴影的原理以及阴影质量的逐步优化可以看我的另一篇文章<a href="https://juejin.cn/post/6940078211967483911" target="_blank">《3D世界中的阴影—ShadowMap原理解析》</a> </p>
<h2 data-id="heading-3">四. 落地代码</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75d8a207dad64bb6ae72756a4a66284b~tplv-k3u1fbpfcp-watermark.image" alt="1619513368_50_w593_h567.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>  下面的 demo 代码，都是用来实现以上这个场景的阴影效果。其中蓝青色的正方体代表光源位置。</p>
<h3 data-id="heading-4">1. 每一帧的渲染流程</h3>
<p>  我们在设备上看到的图像，都是一帧一帧绘制出来的。在这个 demo 中每一帧的渲染，包括以下两个部分：</p>
<ul>
<li>(1) 离屏渲染：将相机移动到光源处，渲染场景到缓冲区，拿到 shadow map。</li>
<li>(2) 切换渲染目标，将场景渲染到屏幕上。其中场景中的正方体和地板，都要配上自定义材质来使用 shadow map。</li>
</ul>
<p>  下面是渲染流程的相关代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; OrbitControls &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./assets/orbitcontrols.js"</span>;

<span class="hljs-keyword">let</span> renderer, stats, camera, camera4SM;
<span class="hljs-keyword">let</span> scene, bufferScene, bufferTexture;

<span class="hljs-keyword">const</span> domElement = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"canvas-frame"</span>);

<span class="hljs-comment">// 帧数检测</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initStatus</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// ... &#125;</span>

<span class="hljs-comment">// 初始化 render</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initThree</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// ... &#125;</span>

<span class="hljs-comment">// 初始化场景</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initScene</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 需要绘制到屏幕的场景</span>
  scene = <span class="hljs-keyword">new</span> THREE.Scene();
  <span class="hljs-keyword">const</span> axisHelper = <span class="hljs-keyword">new</span> THREE.AxesHelper(<span class="hljs-number">100</span>);
  scene.add(axisHelper);
  <span class="hljs-comment">// 离屏缓冲区</span>
  bufferScene = <span class="hljs-keyword">new</span> THREE.Scene();
  bufferTexture = <span class="hljs-keyword">new</span> THREE.WebGLRenderTarget(
    domElement.clientWidth,
    domElement.clientHeight
  );
  bufferTexture.depthBuffer = <span class="hljs-literal">true</span>;
  bufferTexture.depthTexture = <span class="hljs-keyword">new</span> THREE.DepthTexture();
&#125;

<span class="hljs-comment">// 初始化相机</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initCamera</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> width = domElement.clientWidth;
  <span class="hljs-keyword">const</span> height = domElement.clientHeight;

  camera = <span class="hljs-keyword">new</span> THREE.PerspectiveCamera(<span class="hljs-number">45</span>, width / height, <span class="hljs-number">1</span>, <span class="hljs-number">10000</span>);
  camera.position.set(<span class="hljs-number">50</span>, <span class="hljs-number">50</span>, <span class="hljs-number">200</span>);
  camera.lookAt(scene.position);
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  scene.add(camera);
  <span class="hljs-comment">// 光源处的相机，用于生成 shadow map</span>
  camera4SM = <span class="hljs-keyword">new</span> THREE.OrthographicCamera(-<span class="hljs-number">100</span>, <span class="hljs-number">100</span>, <span class="hljs-number">100</span>, -<span class="hljs-number">100</span>, <span class="hljs-number">1</span>, <span class="hljs-number">70</span>);
  camera4SM.position.set(<span class="hljs-number">20</span>, <span class="hljs-number">50</span>, <span class="hljs-number">0</span>);
  camera4SM.lookAt(bufferScene.position);
  camera4SM.aspect = width / height;
  camera4SM.updateProjectionMatrix();
  bufferScene.add(camera4SM);

&#125;

<span class="hljs-comment">// 初始化光源</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initLight</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// ...&#125;</span>

<span class="hljs-comment">// 每一帧调用的渲染函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 渲染到目标缓冲区</span>
  renderer.setClearColor(<span class="hljs-string">"rgb(255,255,255)"</span>, <span class="hljs-number">1.0</span>);
  renderer.setRenderTarget(bufferTexture);
  renderer.render(bufferScene, camera4SM);

  <span class="hljs-comment">// 渲染到屏幕</span>
  renderer.setClearColor(<span class="hljs-string">"rgb(150,150,150)"</span>, <span class="hljs-number">1.0</span>);
  renderer.setRenderTarget(<span class="hljs-literal">null</span>);
  renderer.render(scene, camera);

  stats.update();
  requestAnimationFrame(render);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">start</span>(<span class="hljs-params"></span>) </span>&#123;
  initStatus();
  initThree();
  initScene();
  initCamera();
  initLight();
  initObject();

  render();
&#125;

start();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2. 生成深度纹理图 - shadow map</h3>
<p>  使用离屏渲染，将深度图这一帧缓存起来。<br>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/008c7bbe2200454ca47b5c86fc2606ae~tplv-k3u1fbpfcp-watermark.image" alt="1619514934_21_w300_h296.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">(1) 新加一个自定义材质，用来记录深度</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initObject</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// add object in buffer scene</span>
  <span class="hljs-keyword">const</span> getSMMaterial = <span class="hljs-keyword">new</span> THREE.ShaderMaterial(&#123;
    <span class="hljs-attr">uniforms</span>: &#123;
      <span class="hljs-attr">projectionMatrixSM</span>: &#123; <span class="hljs-attr">value</span>: camera4SM.projectionMatrix &#125;,
    &#125;,
    <span class="hljs-attr">vertexShader</span>: <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"vertexShaderSM"</span>).textContent,
    <span class="hljs-attr">fragmentShader</span>: <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"fragmentShaderSM"</span>).textContent,
  &#125;);
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  相关的着色器代码：
  具体的做法就是把投影之后的片元深度值，写到 rgb 中的 r 值。这就是为啥我们的 shadow map 是偏红色的～</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"vertexShaderSM"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"x-shader/x-vertex"</span>></span><span class="javascript">
    uniform mat4 projectionMatrixSM;
    <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span>&#123;
      gl_Position = projectionMatrixSM * modelViewMatrix * vec4( position, <span class="hljs-number">1.0</span> );
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"fragmentShaderSM"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"x-shader/x-fragment"</span>></span><span class="javascript">
    <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
      gl_FragColor = vec4(gl_FragCoord.z, <span class="hljs-number">0.0</span>, <span class="hljs-number">0.0</span>, <span class="hljs-number">0.0</span>); <span class="hljs-comment">// 将片元的深度值写入r值</span>
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">(2) 把使用该材质的正方体和地板放到离屏渲染的场景里</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initObject</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">const</span> groundGeo = <span class="hljs-keyword">new</span> THREE.BoxGeometry(<span class="hljs-number">40</span>, <span class="hljs-number">40</span>, <span class="hljs-number">1</span>);
  <span class="hljs-keyword">const</span> groundInBuffer = <span class="hljs-keyword">new</span> THREE.Mesh(groundGeo, getSMMaterial);
  groundInBuffer.rotation.x = <span class="hljs-built_in">Math</span>.PI / <span class="hljs-number">2</span>;
  groundInBuffer.name = <span class="hljs-string">"groundPlane"</span>;
  bufferScene.add(groundInBuffer);
  
  <span class="hljs-keyword">const</span> cubeGeo = <span class="hljs-keyword">new</span> THREE.BoxGeometry(<span class="hljs-number">20</span>, <span class="hljs-number">20</span>, <span class="hljs-number">20</span>);
  <span class="hljs-keyword">const</span> cubeInBuffer = <span class="hljs-keyword">new</span> THREE.Mesh(cubeGeo, getSMMaterial);
  cubeInBuffer.position.y += <span class="hljs-number">10</span>;
  cubeInBuffer.name = <span class="hljs-string">"cubeInBuffer"</span>;
  bufferScene.add(cubeInBuffer);
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">(3) 用光源处的相机渲染场景到缓存里</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 渲染到目标缓冲区</span>
  renderer.setClearColor(<span class="hljs-string">"rgb(255,255,255)"</span>, <span class="hljs-number">1.0</span>);
  renderer.setRenderTarget(bufferTexture);
  renderer.render(bufferScene, camera4SM);
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3. 使用深度纹理图生成阴影</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c5f4fa539554c5bb1618615a096c352~tplv-k3u1fbpfcp-watermark.image" alt="1619515049_66_w1132_h604.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">(1) 新加一个自定义材质，用来使用深度图生成阴影</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initObject</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// add object in buffer scene</span>
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// add object in screen scene</span>
  <span class="hljs-keyword">const</span> useSM4CubeMat = <span class="hljs-keyword">new</span> THREE.ShaderMaterial(&#123;
    <span class="hljs-comment">// attributes 居然传不进去</span>
    <span class="hljs-attr">uniforms</span>: &#123;
      <span class="hljs-attr">modelViewMatrixSM</span>: &#123; <span class="hljs-attr">value</span>: cubeInBuffer.modelViewMatrix &#125;,
      <span class="hljs-attr">projectionMatrixSM</span>: &#123; <span class="hljs-attr">value</span>: camera4SM.projectionMatrix &#125;,
      <span class="hljs-attr">depthTexture</span>: &#123; <span class="hljs-attr">value</span>: bufferTexture.texture &#125;,
      <span class="hljs-attr">color</span>: &#123; <span class="hljs-attr">value</span>: <span class="hljs-keyword">new</span> THREE.Vector3(<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">0</span>) &#125;,
    &#125;,
    <span class="hljs-attr">vertexShader</span>: <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"vertexShader"</span>).textContent,
    <span class="hljs-attr">fragmentShader</span>: <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"fragmentShader"</span>).textContent,
  &#125;);
  
    <span class="hljs-keyword">const</span> useSM4GroundMat = <span class="hljs-keyword">new</span> THREE.ShaderMaterial(&#123;
    <span class="hljs-attr">uniforms</span>: &#123;
      <span class="hljs-attr">modelViewMatrixSM</span>: &#123; <span class="hljs-attr">value</span>: groundInBuffer.modelViewMatrix &#125;,
      <span class="hljs-attr">projectionMatrixSM</span>: &#123; <span class="hljs-attr">value</span>: camera4SM.projectionMatrix &#125;,
      <span class="hljs-attr">depthTexture</span>: &#123; <span class="hljs-attr">value</span>: bufferTexture.texture &#125;,
      <span class="hljs-attr">color</span>: &#123; <span class="hljs-attr">value</span>: <span class="hljs-keyword">new</span> THREE.Vector3(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>) &#125;,
    &#125;,
    <span class="hljs-attr">vertexShader</span>: <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"vertexShader"</span>).textContent,
    <span class="hljs-attr">fragmentShader</span>: <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"fragmentShader"</span>).textContent,
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  相关的着色器代码：</p>
<ul>
<li>先做归一化：mvp 矩阵处理完的坐标还会被自动转化成裁剪空间的坐标，范围在 [0, 1] 区间，所以这里也要做归一化。</li>
<li>获取深度：拿到深度纹理中对应坐标存储的数据。</li>
<li>判断片元属否在阴影中：如果该片元的深度大于shadow map 存储的对应深度，则表示相同位置下，有比该点距离光源更近的点存在，被遮挡了。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"vertexShader"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"x-shader/x-vertex"</span>></span><span class="javascript">
    uniform mat4 modelViewMatrixSM;
    uniform mat4 projectionMatrixSM;
    varying vec4 result;
    <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span>&#123;
      gl_Position = projectionMatrix * modelViewMatrix * vec4( position, <span class="hljs-number">1.0</span> );
      result = projectionMatrixSM * modelViewMatrixSM * vec4( position, <span class="hljs-number">1.0</span> );
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"fragmentShader"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"x-shader/x-fragment"</span>></span><span class="javascript">
    uniform sampler2D depthTexture;
    uniform vec3 color;
    varying vec4 result;
    <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
      vec3 shadowCoord = (result.xyz / result.w) / <span class="hljs-number">2.0</span> + <span class="hljs-number">0.5</span>; <span class="hljs-comment">// 归一化</span>
      vec4 rgbaDepth = texture2D(depthTexture, shadowCoord.xy); 
      float depth = rgbaDepth.r; <span class="hljs-comment">// 拿到深度纹理中对应坐标存储的深度</span>

      float visibility = (shadowCoord.z > depth + <span class="hljs-number">0.3</span>) ? <span class="hljs-number">0.0</span> : <span class="hljs-number">1.0</span>; <span class="hljs-comment">// 判断片元是否在阴影中</span>
      vec4 v_Color = vec4(color, <span class="hljs-number">1.0</span>);
      gl_FragColor = vec4(v_Color.rgb * visibility, v_Color.a);
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">(2) 把使用该材质的正方体和地板放到屏幕渲染的场景里</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initObject</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-comment">// ...</span>
<span class="hljs-keyword">const</span> cubeBufGeo = <span class="hljs-keyword">new</span> THREE.BufferGeometry();
  cubeBufGeo.fromGeometry(cubeGeo);
  <span class="hljs-keyword">const</span> cubeInScreen = <span class="hljs-keyword">new</span> THREE.Mesh(cubeBufGeo, useSM4CubeMat);
  cubeInScreen.position.y += <span class="hljs-number">10</span>;
  cubeInScreen.name = <span class="hljs-string">"cubeInScreen"</span>;
  scene.add(cubeInScreen);
    
<span class="hljs-keyword">const</span> planeInScreen = <span class="hljs-keyword">new</span> THREE.Mesh(groundGeo, useSM4GroundMat);
  planeInScreen.rotation.x = <span class="hljs-built_in">Math</span>.PI / <span class="hljs-number">2</span>;
  planeInScreen.name = <span class="hljs-string">"planeInScreen"</span>;
  scene.add(planeInScreen);
  
  <span class="hljs-comment">// 展示 shadow map</span>
  <span class="hljs-comment">//...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">(3) 渲染场景到屏幕上</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 每一帧调用的渲染函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 渲染到目标缓冲区</span>
  <span class="hljs-comment">// ...</span>

  <span class="hljs-comment">// 渲染到屏幕</span>
  renderer.setClearColor(<span class="hljs-string">"rgb(150,150,150)"</span>, <span class="hljs-number">1.0</span>);
  renderer.setRenderTarget(<span class="hljs-literal">null</span>);
  renderer.render(scene, camera);

  stats.update();
  requestAnimationFrame(render);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">五. 最终效果</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbdfca1a4c97420f9e47a86d456f26c8~tplv-k3u1fbpfcp-watermark.image" alt="1619593417_70_w1914_h750.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">六. 附录</h2>
<ul>
<li>相关代码：<a href="https://github.com/Zack921/visual-demo/tree/main/threejs/diyShadow" target="_blank" rel="nofollow noopener noreferrer">github.com/Zack921/vis…</a></li>
<li>3D世界中的阴影—ShadowMap原理解析: <a href="https://juejin.cn/post/6940078211967483911" target="_blank">juejin.cn/post/694007…</a></li>
</ul></div>  
</div>
            