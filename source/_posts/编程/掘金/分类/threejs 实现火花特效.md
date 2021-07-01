
---
title: 'three.js 实现火花特效'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f50a053a9eb94d2889d73e6a334b66a3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 16:15:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f50a053a9eb94d2889d73e6a334b66a3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<h2 data-id="heading-0">前言</h2>
<p>大家好，这里是 CSS兼WebGL 魔法使——alphardex。</p>
<p>上周末刚在原神里抽到了“火花骑士”可莉，于是就心血来潮，想用three.js来实现一种火系的特效，不是炸弹的爆炸，而是炸弹爆炸后在草上留下的火花效果</p>
<p><a href="https://imgtu.com/i/RBvmVJ" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f50a053a9eb94d2889d73e6a334b66a3~tplv-k3u1fbpfcp-zoom-1.image" alt="RBvmVJ.jpg" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>游戏里的效果相对比较卡通化，而本文的效果将更加逼近现实一点</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fc099781b8946eea833150f9ce6d915~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>让我们开始吧！</p>

<h2 data-id="heading-1">准备工作</h2>
<p>在开始本项目之前，你首先要了解ray marching这个概念，如果不了解也没关系，笔者之前写过一篇介绍它的<a href="https://juejin.cn/post/6934461126977519629" target="_blank">入门文章</a>，或者通过<a href="http://jamie-wong.com/2016/07/15/ray-marching-signed-distance-functions/" target="_blank" rel="nofollow noopener noreferrer">这篇文章</a>也可以入门，掌握了基础概念后就可以开始了</p>
<p>本项目需要用到：</p>
<p>笔者的<a href="https://codepen.io/alphardex/pen/yLaQdOq" target="_blank" rel="nofollow noopener noreferrer">three.js模板</a>：点击右下角的fork即可复制一份</p>
<p>着色器模块化：<a href="https://github.com/glslify/glslify" target="_blank" rel="nofollow noopener noreferrer">glslify</a></p>
<p>着色器npm包：<code>glsl-noise</code>,<code>glsl-sdf-primitives</code>,<code>glsl-sdf-ops</code></p>
<h2 data-id="heading-2">正文</h2>
<h3 data-id="heading-3">场景搭建</h3>
<p>按之前的惯例，搭建一个场景，放一个铺满屏幕的平面，设定一些必要的参数（火花的速度与颜色）</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RayMarchingFire</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Base</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">sel: <span class="hljs-built_in">string</span>, debug: <span class="hljs-built_in">boolean</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>(sel, debug);
    <span class="hljs-built_in">this</span>.clock = <span class="hljs-keyword">new</span> THREE.Clock();
    <span class="hljs-built_in">this</span>.cameraPosition = <span class="hljs-keyword">new</span> THREE.Vector3(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>);
    <span class="hljs-built_in">this</span>.params = &#123;
      <span class="hljs-attr">velocity</span>: <span class="hljs-number">2</span>,
    &#125;;
    <span class="hljs-built_in">this</span>.colorParams = &#123;
      <span class="hljs-attr">color1</span>: <span class="hljs-string">"#ff801a"</span>,
      <span class="hljs-attr">color2</span>: <span class="hljs-string">"#ff5718"</span>,
    &#125;;
  &#125;
  <span class="hljs-comment">// 初始化</span>
  <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.createScene();
    <span class="hljs-built_in">this</span>.createOrthographicCamera();
    <span class="hljs-built_in">this</span>.createRenderer();
    <span class="hljs-built_in">this</span>.createRayMarchingFireMaterial();
    <span class="hljs-built_in">this</span>.createPlane();
    <span class="hljs-built_in">this</span>.createLight();
    <span class="hljs-built_in">this</span>.trackMousePos();
    <span class="hljs-built_in">this</span>.addListeners();
    <span class="hljs-built_in">this</span>.setLoop();
  &#125;
  <span class="hljs-comment">// 创建材质</span>
  <span class="hljs-function"><span class="hljs-title">createRayMarchingFireMaterial</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> rayMarchingFireMaterial = <span class="hljs-keyword">new</span> THREE.ShaderMaterial(&#123;
      <span class="hljs-attr">vertexShader</span>: rayMarchingFireVertexShader,
      <span class="hljs-attr">fragmentShader</span>: rayMarchingFireFragmentShader,
      <span class="hljs-attr">side</span>: THREE.DoubleSide,
      <span class="hljs-attr">uniforms</span>: &#123;
        <span class="hljs-attr">uTime</span>: &#123;
          <span class="hljs-attr">value</span>: <span class="hljs-number">0</span>,
        &#125;,
        <span class="hljs-attr">uMouse</span>: &#123;
          <span class="hljs-attr">value</span>: <span class="hljs-keyword">new</span> THREE.Vector2(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>),
        &#125;,
        <span class="hljs-attr">uResolution</span>: &#123;
          <span class="hljs-attr">value</span>: <span class="hljs-keyword">new</span> THREE.Vector2(<span class="hljs-built_in">window</span>.innerWidth, <span class="hljs-built_in">window</span>.innerHeight),
        &#125;,
        <span class="hljs-attr">uVelocity</span>: &#123;
          <span class="hljs-attr">value</span>: <span class="hljs-number">3</span>,
        &#125;,
        <span class="hljs-attr">uColor1</span>: &#123;
          <span class="hljs-attr">value</span>: <span class="hljs-keyword">new</span> THREE.Color(<span class="hljs-built_in">this</span>.colorParams.color1),
        &#125;,
        <span class="hljs-attr">uColor2</span>: &#123;
          <span class="hljs-attr">value</span>: <span class="hljs-keyword">new</span> THREE.Color(<span class="hljs-built_in">this</span>.colorParams.color2),
        &#125;,
      &#125;,
    &#125;);
    <span class="hljs-built_in">this</span>.rayMarchingFireMaterial = rayMarchingFireMaterial;
    <span class="hljs-built_in">this</span>.shaderMaterial = rayMarchingFireMaterial;
  &#125;
  <span class="hljs-comment">// 创建平面</span>
  <span class="hljs-function"><span class="hljs-title">createPlane</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> geometry = <span class="hljs-keyword">new</span> THREE.PlaneBufferGeometry(<span class="hljs-number">2</span>, <span class="hljs-number">2</span>, <span class="hljs-number">100</span>, <span class="hljs-number">100</span>);
    <span class="hljs-keyword">const</span> material = <span class="hljs-built_in">this</span>.rayMarchingFireMaterial;
    <span class="hljs-built_in">this</span>.createMesh(&#123;
      geometry,
      material,
    &#125;);
  &#125;
  <span class="hljs-comment">// 动画</span>
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> elapsedTime = <span class="hljs-built_in">this</span>.clock.getElapsedTime();
    <span class="hljs-keyword">const</span> mousePos = <span class="hljs-built_in">this</span>.mousePos;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.rayMarchingFireMaterial) &#123;
      <span class="hljs-built_in">this</span>.rayMarchingFireMaterial.uniforms.uTime.value = elapsedTime;
      <span class="hljs-built_in">this</span>.rayMarchingFireMaterial.uniforms.uMouse.value = mousePos;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来开始编写片元着色器</p>
<h3 data-id="heading-4">创建发光渐变椭圆</h3>
<p>仔细观察火花的形状你会发现其实它的大致形状像一个椭圆，而且还是发光的渐变椭圆，于是我们就要想办法来创建这种形状。
简要说下思路：ray marching获取的值改成光线位置pos和光线移动的进度strength，光线位置的y轴将用于设定火花的颜色；光线移动的进度strength用于设定火花的形状（这里就是椭圆）</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-meta">#pragma glslify:centerUv=require(../modules/centerUv)</span>
<span class="hljs-meta">#pragma glslify:getRayDirection=require(../modules/getRayDirection)</span>
<span class="hljs-meta">#pragma glslify:sdSphere=require(glsl-sdf-primitives/sdSphere)</span>
<span class="hljs-meta">#pragma glslify:opU=require(glsl-sdf-ops/union)</span>
<span class="hljs-meta">#pragma glslify:cnoise=require(glsl-noise/classic/3d)</span>

<span class="hljs-keyword">uniform</span> <span class="hljs-type">float</span> uTime;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">vec2</span> uMouse;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">vec2</span> uResolution;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">float</span> uVelocity;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">vec3</span> uColor1;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">vec3</span> uColor2;

<span class="hljs-keyword">varying</span> <span class="hljs-type">vec2</span> vUv;
<span class="hljs-keyword">varying</span> <span class="hljs-type">vec3</span> vPosition;

<span class="hljs-type">float</span> fire(<span class="hljs-type">vec3</span> p)&#123;
    <span class="hljs-type">vec3</span> p2=p*<span class="hljs-type">vec3</span>(<span class="hljs-number">1.</span>,<span class="hljs-number">.5</span>,<span class="hljs-number">1.</span>)+<span class="hljs-type">vec3</span>(<span class="hljs-number">0.</span>,<span class="hljs-number">1.</span>,<span class="hljs-number">0.</span>);
    <span class="hljs-type">float</span> geo=sdSphere(p2,<span class="hljs-number">1.</span>);
    <span class="hljs-type">float</span> result=geo;
    <span class="hljs-keyword">return</span> result;
&#125;

<span class="hljs-type">vec2</span> sdf(<span class="hljs-type">vec3</span> p)&#123;
    <span class="hljs-type">float</span> result=opU(<span class="hljs-built_in">abs</span>(fire(p)),-(<span class="hljs-built_in">length</span>(p)<span class="hljs-number">-100.</span>));
    <span class="hljs-type">float</span> objType=<span class="hljs-number">1.</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-type">vec2</span>(result,objType);
&#125;

<span class="hljs-type">vec4</span> rayMarch(<span class="hljs-type">vec3</span> eye,<span class="hljs-type">vec3</span> ray)&#123;
    <span class="hljs-type">float</span> depth=<span class="hljs-number">0.</span>;
    <span class="hljs-type">float</span> strength=<span class="hljs-number">0.</span>;
    <span class="hljs-type">float</span> eps=<span class="hljs-number">.02</span>;
    <span class="hljs-type">vec3</span> pos=eye;
    <span class="hljs-keyword">for</span>(<span class="hljs-type">int</span> i=<span class="hljs-number">0</span>;i<<span class="hljs-number">64</span>;i++)&#123;
        pos+=depth*ray;
        <span class="hljs-type">float</span> dist=sdf(pos).x;
        depth=dist+eps;
        <span class="hljs-keyword">if</span>(dist><span class="hljs-number">0.</span>)&#123;
            strength=<span class="hljs-type">float</span>(i)/<span class="hljs-number">64.</span>;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-type">vec4</span>(pos,strength);
&#125;

<span class="hljs-type">void</span> main()&#123;
    <span class="hljs-type">vec2</span> p=centerUv(vUv,uResolution);
    p=p*<span class="hljs-type">vec2</span>(<span class="hljs-number">1.6</span>,<span class="hljs-number">-1</span>);
    
    <span class="hljs-type">vec3</span> ro=<span class="hljs-type">vec3</span>(<span class="hljs-number">0.</span>,<span class="hljs-number">-2.</span>,<span class="hljs-number">4.</span>);
    <span class="hljs-type">vec3</span> ta=<span class="hljs-type">vec3</span>(<span class="hljs-number">0.</span>,<span class="hljs-number">-2.5</span>,<span class="hljs-number">-1.5</span>);
    <span class="hljs-type">float</span> fl=<span class="hljs-number">1.25</span>;
    <span class="hljs-type">vec3</span> rd=getRayDirection(p,ro,ta,fl);
    
    <span class="hljs-type">vec3</span> color=<span class="hljs-type">vec3</span>(<span class="hljs-number">0.</span>);
    
    <span class="hljs-type">vec4</span> result=rayMarch(ro,rd);
    
    <span class="hljs-type">float</span> strength=<span class="hljs-built_in">pow</span>(result.w*<span class="hljs-number">2.</span>,<span class="hljs-number">4.</span>);
    <span class="hljs-type">vec3</span> ellipse=<span class="hljs-type">vec3</span>(strength);
    color=ellipse;
    
    <span class="hljs-built_in">gl_FragColor</span>=<span class="hljs-type">vec4</span>(color,<span class="hljs-number">1.</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>centerUv.glsl</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-type">vec2</span> centerUv(<span class="hljs-type">vec2</span> uv,<span class="hljs-type">vec2</span> resolution)&#123;
    uv=<span class="hljs-number">2.</span>*uv<span class="hljs-number">-1.</span>;
    <span class="hljs-type">float</span> aspect=resolution.x/resolution.y;
    uv.x*=aspect;
    <span class="hljs-keyword">return</span> uv;
&#125;

<span class="hljs-meta">#pragma glslify:export(centerUv);</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>getRayDirection.glsl</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-meta">#pragma glslify:setCamera=require(./setCamera)</span>

<span class="hljs-type">vec3</span> getRayDirection(<span class="hljs-type">vec2</span> p,<span class="hljs-type">vec3</span> ro,<span class="hljs-type">vec3</span> ta,<span class="hljs-type">float</span> fl)&#123;
    <span class="hljs-type">mat3</span> ca=setCamera(ro,ta,<span class="hljs-number">0.</span>);
    <span class="hljs-type">vec3</span> rd=ca*<span class="hljs-built_in">normalize</span>(<span class="hljs-type">vec3</span>(p,fl));
    <span class="hljs-keyword">return</span> rd;
&#125;

<span class="hljs-meta">#pragma glslify:export(getRayDirection)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>setCamera.glsl</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-type">mat3</span> setCamera(<span class="hljs-keyword">in</span> <span class="hljs-type">vec3</span> ro,<span class="hljs-keyword">in</span> <span class="hljs-type">vec3</span> ta,<span class="hljs-type">float</span> cr)
&#123;
    <span class="hljs-type">vec3</span> <span class="hljs-keyword">cw</span>=<span class="hljs-built_in">normalize</span>(ta-ro);
    <span class="hljs-type">vec3</span> cp=<span class="hljs-type">vec3</span>(<span class="hljs-built_in">sin</span>(cr),<span class="hljs-built_in">cos</span>(cr),<span class="hljs-number">0.</span>);
    <span class="hljs-type">vec3</span> cu=<span class="hljs-built_in">normalize</span>(<span class="hljs-built_in">cross</span>(<span class="hljs-keyword">cw</span>,cp));
    <span class="hljs-type">vec3</span> cv=(<span class="hljs-built_in">cross</span>(cu,<span class="hljs-keyword">cw</span>));
    <span class="hljs-keyword">return</span> <span class="hljs-type">mat3</span>(cu,cv,<span class="hljs-keyword">cw</span>);
&#125;

<span class="hljs-meta">#pragma glslify:export(setCamera)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://imgtu.com/i/R0RM7Q" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0be1f5a6c8cd4bd0b0b07dfcfa085ed0~tplv-k3u1fbpfcp-zoom-1.image" alt="R0RM7Q.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h3 data-id="heading-5">用噪声生成火花</h3>
<p>接下来就对这个椭圆应用上噪声（这里选了传统噪声，为了更好看的外观，也可以选择其他的噪声）</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-type">float</span> fire(<span class="hljs-type">vec3</span> p)&#123;
    <span class="hljs-type">vec3</span> p2=p*<span class="hljs-type">vec3</span>(<span class="hljs-number">1.</span>,<span class="hljs-number">.5</span>,<span class="hljs-number">1.</span>)+<span class="hljs-type">vec3</span>(<span class="hljs-number">0.</span>,<span class="hljs-number">1.</span>,<span class="hljs-number">0.</span>);
    <span class="hljs-type">float</span> geo=sdSphere(p2,<span class="hljs-number">1.</span>);
    <span class="hljs-comment">// float result=geo;</span>
    <span class="hljs-type">float</span> displacement=uTime*uVelocity;
    <span class="hljs-type">vec3</span> displacementY=<span class="hljs-type">vec3</span>(<span class="hljs-number">.0</span>,displacement,<span class="hljs-number">.0</span>);
    <span class="hljs-type">float</span> noise=(cnoise(p+displacementY))*p.y*<span class="hljs-number">.4</span>;
    <span class="hljs-type">float</span> result=geo+noise;
    <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://imgtu.com/i/R0fRFH" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f92298b839124a849eed422016fbf51e~tplv-k3u1fbpfcp-zoom-1.image" alt="R0fRFH.gif" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>莫名感觉像黑魂3里的芙莉德修女的黑焰，尽管这样也很cool，我们还是给它加上颜色，让它更像现实中的火花</p>
<h3 data-id="heading-6">给火花加上颜色</h3>
<p>将颜色通过mix函数混合起来（强度是光线位置的y轴），和之前的颜色相乘即可</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-type">void</span> main()&#123;
    ...
    
    <span class="hljs-type">float</span> fireBody=result.y/<span class="hljs-number">64.</span>;
    <span class="hljs-type">vec3</span> mixColor=<span class="hljs-built_in">mix</span>(uColor1,uColor2,fireBody);
    color*=mixColor;
    
    <span class="hljs-built_in">gl_FragColor</span>=<span class="hljs-type">vec4</span>(color,<span class="hljs-number">1.</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fc099781b8946eea833150f9ce6d915~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">项目地址</h2>
<p><a href="https://codepen.io/alphardex/pen/OJmPpeJ" target="_blank" rel="nofollow noopener noreferrer">Ray Marching Fire</a></p></div>  
</div>
            