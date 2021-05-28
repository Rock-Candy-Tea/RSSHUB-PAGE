
---
title: 'GLSL着色器，来玩'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://img11.360buyimg.com/imagetools/jfs/t1/159690/37/16529/250457/60632138E30fd5df7/882e91ba77e3a9b6.jpg'
author: 掘金
comments: false
date: Thu, 27 May 2021 05:55:59 GMT
thumbnail: 'https://img11.360buyimg.com/imagetools/jfs/t1/159690/37/16529/250457/60632138E30fd5df7/882e91ba77e3a9b6.jpg'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>对实现动画的前端同学们来说，<code>canvas</code>可以说是最自由，最能全面控制的一个动画实现载体。不但能通过<code>javascript</code>控制点、线、面的绘制，使用图片资源填充；还能改变输入参数作出交互动画，完全控制动画过程中的动作轨迹、速度、弹性等要素。</p>
<p>但使用<code>canvas</code>开发过较复杂一点的动画的同学，可能会发现，完全使用<code>javascript</code>绘制、控制的动画，某些效果不太好实现（这篇文章只讨论2D），像模糊，光照，水滴等效果。虽然用逐像素处理的方法也可以实现，但<code>javascript</code>对这类型大量数据的计算并不擅长，实现出来每一帧绘制的时间十分感人，用他实现动画并不现实。</p>
<p>但<code>canvas</code>除了最常用的<code>javascript</code> API绘制方式（<code>getContext('2d')</code>），还有WebGL的方式（<code>getContext(webgl)</code>），对前面说到的大量数据计算的场景，可以说是最适合发挥的地方。WebGL对很多同学来说就是实现3D场景的，其实对2D绘图来说，也有很大的发挥场景。</p>
<h2 data-id="heading-0">为什么WebGL会比较厉害</h2>
<p>我们来看看<code>javascript</code> API绘制和webGL绘制原理上的不同之处：</p>
<p>如果使用<code>javascript</code>对画布的逐个像素进行处理，那这部分处理工作就需要在<code>javascript</code>的运行环境里进行，我们知道<code>javascript</code>的执行是单线程的，所以只能逐个逐个像素进行计算和绘制。就像一个细长的漏斗，一滴一滴水的往下漏。</p>
<p><img src="https://img11.360buyimg.com/imagetools/jfs/t1/159690/37/16529/250457/60632138E30fd5df7/882e91ba77e3a9b6.jpg" alt="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3d239848921472c89efaa691393259f~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而WebGL的处理方式，是用GPU驱动的，对每一个像素的处理，都是在GPU上执行，而GPU有许多渲染管道，这些处理可以在这些管道中并行执行，这就是WebGL擅长这种大量数据计算场景的原因。</p>
<p><img src="https://img12.360buyimg.com/imagetools/jfs/t1/163279/8/15220/308469/60632138E3bea6a6b/8b3372eeb42cc6bb.jpg" alt="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2eff6dcbdc094e6b9b2742900b9b302b~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">WebGL那么厉害，都用它绘图就好喇</h2>
<p>WebGL虽然有上面说的优点，但也有个致命的缺点：不好学，想要简单画根线也要费一番力气。</p>
<p>GPU并行管道之间是不知道另一个管道输出的是什么，只知道自己管道的输入和需要执行的程序；而且不保留状态，管道自己并不知道在这次任务之前执行过什么程序，有什么输入输出值，类似现在纯函数的概念。这些观念上的不同就提升了使用WebGL绘图的门槛。</p>
<p>另外这些跑在GPU里的程序不是<code>javascript</code>，是一种类C语言，这也需要前端同学们另外再学习。</p>
<h2 data-id="heading-2">Hello, world</h2>
<p>那门槛再高也总有需要跨过去的一天的，下面一步一步控制WebGL去<code>画</code>一点图案，大家也可以体会一下，适合在什么时候使用这一门技术。</p>
<h3 data-id="heading-3">基础环境——大荧幕</h3>
<p>为尽快进入GLSL着色器的阶段，这里基础WebGL环境搭建用了<code>Three.js</code>，大家可以研究下这个基础环境的搭建，不用第三方库其实也用不了多少代码量。</p>
<p>以下是基础环境的搭建:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params">canvas</span>) </span>&#123;
  <span class="hljs-keyword">const</span> renderer = <span class="hljs-keyword">new</span> THREE.WebGLRenderer(&#123;canvas&#125;);
  renderer.autoClearColor = <span class="hljs-literal">false</span>;
 
  <span class="hljs-keyword">const</span> camera = <span class="hljs-keyword">new</span> THREE.OrthographicCamera(
    -<span class="hljs-number">1</span>, <span class="hljs-comment">// left</span>
     <span class="hljs-number">1</span>, <span class="hljs-comment">// right</span>
     <span class="hljs-number">1</span>, <span class="hljs-comment">// top</span>
    -<span class="hljs-number">1</span>, <span class="hljs-comment">// bottom</span>
    -<span class="hljs-number">1</span>, <span class="hljs-comment">// near,</span>
     <span class="hljs-number">1</span>, <span class="hljs-comment">// far</span>
  );
  <span class="hljs-keyword">const</span> scene = <span class="hljs-keyword">new</span> THREE.Scene();
  <span class="hljs-keyword">const</span> plane = <span class="hljs-keyword">new</span> THREE.PlaneGeometry(<span class="hljs-number">2</span>, <span class="hljs-number">2</span>);

  <span class="hljs-keyword">const</span> fragmentShader = <span class="hljs-string">'............'</span>
  <span class="hljs-keyword">const</span> uniforms = &#123;
    <span class="hljs-attr">u_resolution</span>:  &#123; <span class="hljs-attr">value</span>: <span class="hljs-keyword">new</span> THREE.Vector2(canvas.width, canvas.height) &#125;,
    <span class="hljs-attr">u_time</span>: &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">0</span> &#125;
  &#125;;
  <span class="hljs-keyword">const</span> material = <span class="hljs-keyword">new</span> THREE.ShaderMaterial(&#123;
    fragmentShader,
    uniforms,
  &#125;);
  scene.add(<span class="hljs-keyword">new</span> THREE.Mesh(plane, material));
 
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
    material.uniforms.u_time.value++;
    renderer.render(scene, camera);
    requestAnimationFrame(render);
  &#125;

  render()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解释一下上面这段代码做了什么：创建了一个3D场景（说好的2D呢？），把一个矩形平面糊在摄像机前面，占满摄像机视觉范围，就像看IMAX坐最前排，你能看到的就只有面前的屏幕的感觉，屏幕上的画面就是你的整个世界。我们的绘图就在这个屏幕上。</p>
<p>再说明一下，着色器分为顶点着色器<code>VERTEX_SHADER</code>和片段着色器<code>FRAGMENT_SHADER</code>。</p>
<p>顶点着色器对3D场景里物体的每个顶点计算值，如颜色、法线向量等，在这里我们只讨论2D画面，顶点着色器的部分就由<code>Three.js</code>代劳了，实现的作用就是固定了场景中镜头和屏幕的位置。</p>
<p>而片段着色器的作用就是计算平面上每一个片段（在这里是屏幕上每一个像素）输出的颜色值，也是这篇文章研究的对象。</p>
<p>片段着色器入参有<code>varying</code>和<code>uniform</code>两种，<code>varying</code>简单说一下是由顶点着色器传入的，每个片段输入的值由相关的顶点线性插值得到，所以每个片段上的值不一样，本文先不讨论这部分（不然写不完了）。<code>uniform</code>是统一值，由着色器外部传入，每个片段得到的值是一样的，在这里就是我们从<code>javascript</code>输入变量的入口。上面的代码我们就为片段着色器传入了<code>u_resolution</code>，包含画布的宽高值。</p>
<h3 data-id="heading-4">第一个着色器</h3>
<p><code>fragmentShader</code>为着色器的程序代码，一般的构成为:</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-meta">#ifdef GL_ES</span>
<span class="hljs-keyword">precision</span> <span class="hljs-keyword">mediump</span> <span class="hljs-type">float</span>;
<span class="hljs-meta">#endif</span>

<span class="hljs-keyword">uniform</span> <span class="hljs-type">vec2</span> u_resolution;

<span class="hljs-type">void</span> main() &#123;
  <span class="hljs-built_in">gl_FragColor</span> = <span class="hljs-type">vec4</span>(<span class="hljs-number">1.0</span>, <span class="hljs-number">0.0</span>, <span class="hljs-number">0.0</span>, <span class="hljs-number">1.0</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在前3行检查了是否定义了<code>GL_ES</code>，这通常在移动端或浏览器下会定义，第2行指定了浮点数<code>float</code>的精度为中等，也可以指定为低精度<code>lowp</code>或高精度<code>highp</code>，精度越低执行速度越快，但质量会降低。值得一提的是，同样的设置在不同的执行环境下可能会表现不一样，例如某些移动端的浏览器环境，需要指定为高精度才能获得和PC端浏览器里中等精度一样的表现。</p>
<p>第5行指定了着色器可以接收哪些入参，这里就只有一个入参：类型为vec2的<code>u_resolution</code>。</p>
<p>最后3行描述了着色器的主程序，其中可以对入参和其他信息作处理，最后输出颜色到<code>gl_FragColor</code>，代表这个片段显示的颜色，其中4个数值代表<code>RGBA</code>（红、绿、蓝、透明度），数值范围为<code>0.0 ~ 1.0</code>。</p>
<p>为什么要写<code>0.0</code>而不是<code>0</code>呢，因为<code>GLSL</code>里不像<code>javascript</code>数字只有一个类型，而是分成整形(<code>int</code>)和浮点数(<code>float</code>)，而浮点数必须包含小数点，当小数点前是0的时候，写成<code>.0</code>也可以。</p>
<p>那大家看完这段解说，应该能猜到上面的着色器会输出什么吧，对，就是全屏的红色。</p>
<p>这就是最基础的片段着色器。</p>
<h3 data-id="heading-5">使用uniform</h3>
<p>大家应该注意到上面的例子没有用到传入的uniform值，下面来说一下这些值怎么用。</p>
<p>看之前搭建基础环境的<code>javascript</code>代码可以看到，<code>u_resolution</code>存储了画布的宽高，这个值在着色器有什么用呢？</p>
<p>这要说到片元着色器的另一个内建的值<code>gl_FragCoord</code>，这个值存储的是片段（像素）的座标<code>x</code>，<code>y</code>值，使用这两个值就可以知道当前着色器计算的是画布上哪个位置的颜色。举个例子：</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-meta">#ifdef GL_ES</span>
<span class="hljs-keyword">precision</span> <span class="hljs-keyword">mediump</span> <span class="hljs-type">float</span>;
<span class="hljs-meta">#endif</span>

<span class="hljs-keyword">uniform</span> <span class="hljs-type">vec2</span> u_resolution;

<span class="hljs-type">void</span> main() &#123;
  <span class="hljs-type">vec2</span> st = <span class="hljs-built_in">gl_FragCoord</span>.xy / u_resolution;
  <span class="hljs-built_in">gl_FragColor</span> = <span class="hljs-type">vec4</span>(st, <span class="hljs-number">0.0</span>, <span class="hljs-number">1.0</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这样的图像：</p>
<p><img src="https://img12.360buyimg.com/imagetools/jfs/t1/156235/37/18839/33609/6062ffeaE37643d53/3cb9bd3ca9299815.png" alt="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/deba900f59574066893b54e13ce62846~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面的着色器代码，使用归一化后的<code>x</code>、<code>y</code>座标输出到<code>gl_FragColor</code>的红、绿色部分。</p>
<p>从图中可以看出，<code>gl_FragCoord</code>的<code>(0, 0)</code>点在左下角，x轴和y轴方向分别为向右和向上。</p>
<p>另一个uniform值<code>u_time</code>就是一个随着时间不断增加的值，利用这个值可以使图像随时间变化，实现动画的效果。</p>
<p>上面的着色器再改写一下：</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-meta">#ifdef GL_ES</span>
<span class="hljs-keyword">precision</span> <span class="hljs-keyword">mediump</span> <span class="hljs-type">float</span>;
<span class="hljs-meta">#endif</span>

<span class="hljs-keyword">uniform</span> <span class="hljs-type">vec2</span> u_resolution;
<span class="hljs-keyword">uniform</span> <span class="hljs-type">float</span> u_time;

<span class="hljs-type">void</span> main() &#123;
  <span class="hljs-type">vec2</span> st = <span class="hljs-built_in">gl_FragCoord</span>.xy / u_resolution;
  <span class="hljs-built_in">gl_FragColor</span> = <span class="hljs-type">vec4</span>(st, <span class="hljs-built_in">sin</span>(u_time / <span class="hljs-number">100.0</span>), <span class="hljs-number">1.0</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到下图的效果：</p>
<p><a href="http://storage.360buyimg.com/element-video/QQ20210330-195823.mp4" target="_blank" rel="nofollow noopener noreferrer">storage.360buyimg.com/element-vid…</a></p>
<p>着色器中使用三角函数<code>sin</code>，在颜色输出的蓝色通道做一个从0到1的周期变化。</p>
<h2 data-id="heading-6">还能做什么？</h2>
<p>掌握基本的原理后，就是开始从大师的作品中学习了。<a href="https://www.shadertoy.com/" target="_blank" rel="nofollow noopener noreferrer">shadertoy</a>是一个类似codepen的着色器playgroud，上面的着色器都是利用上面的基本工具，还有一些造型函数，造出各种眼花缭乱的特效、动画。</p>
<p>上面就是GLSL着色器基本的开发工具，现在就可以开始开发你自己的着色器，剩下就是使用数学方面的技能了。</p></div>  
</div>
            