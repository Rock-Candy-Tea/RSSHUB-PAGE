
---
title: '云图三维 _ Three.js 基础入门介绍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9349284332b5435aa5c723978b3cb59d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 23:28:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9349284332b5435aa5c723978b3cb59d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>图片来源: <a href="https://unsplash.com/photos/d2w-_1LJioQ" target="_blank" rel="nofollow noopener noreferrer">unsplash.com/photos/d2w-…</a></p>
<blockquote>
<p><a href="https://www.yuntucad.com/" target="_blank" rel="nofollow noopener noreferrer">云图三维 连接你·创造的世界</a>  致力于打造国内第一家集查看、建模、装配和渲染于一体的“云端CAD”协作设计平台。</p>
</blockquote>
<h2 data-id="heading-0">正文</h2>
<p><a href="http://threejs.org/" target="_blank" rel="nofollow noopener noreferrer">Three.js</a> 是一个尽可能简化在网页端操作 3D 内容的js库。与其容易混淆的还有WebGL，事实上Three.js是对WebGL 封装， WebGL 是一个只能画点、线和三角形的非常底层的系统。想要用 WebGL 来做一些实用的东西通常需要大量的代码， Three.js对其封装之后，会大大减少代码量，提高编码效率。<strong>Three.js封装了诸如场景、灯光、阴影、材质、贴图、空间运算等一系列功能，让你不必要再从底层 WebGL 开始写起</strong>。</p>
<h2 data-id="heading-1">项目结构</h2>
<p>首先了解一下Three.js项目的整体结构。一个Three.js项目需要创建非常多的对象，包括Scene、Renderer、Camera、Mesh、Object3D、Group、Light、Geometry、Material、Texture等。下图是这些对象之间一些关系展示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9349284332b5435aa5c723978b3cb59d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">重点对象介绍</h2>
<p>在进入编码前，对上面提到的对象重点解释一下，有助于从整体上把握思路。</p>
<ul>
<li>
<p>首先有一个<a href="https://threejs.org/docs/#api/zh/constants/Renderer" target="_blank" rel="nofollow noopener noreferrer">渲染器 (<code>Renderer</code>)</a>。这可以说是 three.js 的主要对象。传入一个<a href="https://threejs.org/docs/#api/zh/scenes/Scene" target="_blank" rel="nofollow noopener noreferrer">场景 (<code>Scene</code>)</a> 和一个<a href="https://threejs.org/docs/#api/zh/cameras/Camera" target="_blank" rel="nofollow noopener noreferrer">摄像机 (<code>Camera</code>)</a> 到<a href="https://threejs.org/docs/#api/zh/constants/Renderer" target="_blank" rel="nofollow noopener noreferrer">渲染器 (<code>Renderer</code>)</a> 中，然后它会将摄像机视椎体中的三维场景渲染成一个二维图片显示在画布上。</p>
</li>
<li>
<p>其次有一个<a href="https://threejsfundamentals.org/threejs/lessons/zh_cn/threejs-scenegraph.html" target="_blank" rel="nofollow noopener noreferrer">场景图</a> 它是一个树状结构，由很多对象组成，比如图中包含了一个<a href="https://threejs.org/docs/#api/zh/scenes/Scene" target="_blank" rel="nofollow noopener noreferrer">场景 (<code>Scene</code>)</a> 对象 ，多个<a href="https://threejs.org/docs/#api/zh/objects/Mesh" target="_blank" rel="nofollow noopener noreferrer">网格 (<code>Mesh</code>)</a> 对象，<a href="https://threejs.org/docs/#api/zh/lights/Light" target="_blank" rel="nofollow noopener noreferrer">光源 (<code>Light</code>)</a> 对象，<a href="https://threejs.org/docs/#api/zh/objects/Group" target="_blank" rel="nofollow noopener noreferrer">群组 (<code>Group</code>)</a>，<a href="https://threejs.org/docs/#api/zh/core/Object3D" target="_blank" rel="nofollow noopener noreferrer">三维物体 (<code>Object3D</code>)</a>，和<a href="https://threejs.org/docs/#api/zh/cameras/Camera" target="_blank" rel="nofollow noopener noreferrer">摄像机 (<code>Camera</code>)</a> 对象。一个<a href="https://threejs.org/docs/#api/zh/scenes/Scene" target="_blank" rel="nofollow noopener noreferrer">场景 (<code>Scene</code>)</a> 对象定义了场景图最基本的要素，并包了含背景色和雾等属性。这些对象通过一个层级关系与明确的树状结构来展示出各自的位置和方向。子对象的位置和方向总是相对于父对象而言的。比如说汽车的轮子是汽车的子对象，这样移动和定位汽车时就会自动移动轮子。</p>
<p>注意图中<a href="https://threejs.org/docs/#api/zh/cameras/Camera" target="_blank" rel="nofollow noopener noreferrer">摄像机 (<code>Camera</code>)</a> 是一半在场景图中，一半在场景图外的。这表示在 three.js 中，<a href="https://threejs.org/docs/#api/zh/cameras/Camera" target="_blank" rel="nofollow noopener noreferrer">摄像机 (<code>Camera</code>)</a> 和其他对象不同的是，它不一定要在场景图中才能起作用。相同的是，<a href="https://threejs.org/docs/#api/zh/cameras/Camera" target="_blank" rel="nofollow noopener noreferrer">摄像机 (<code>Camera</code>)</a> 作为其他对象的子对象，同样会继承它父对象的位置和朝向。</p>
</li>
<li>
<p><a href="https://threejs.org/docs/#api/zh/objects/Mesh" target="_blank" rel="nofollow noopener noreferrer">网格 (<code>Mesh</code>)</a> 对象可以理解为用一种特定的<a href="https://threejs.org/docs/#api/zh/materials/Material" target="_blank" rel="nofollow noopener noreferrer">材质 (<code>Material</code>)</a> 来绘制的一个特定的<a href="https://threejsfundamentals.org/threejs/lessons/zh_cn/Geometry" target="_blank" rel="nofollow noopener noreferrer">几何体 (<code>Geometry</code>)</a>。<a href="https://threejs.org/docs/#api/zh/materials/Material" target="_blank" rel="nofollow noopener noreferrer">材质 (<code>Material</code>)</a> 和<a href="https://threejsfundamentals.org/threejs/lessons/zh_cn/Geometry" target="_blank" rel="nofollow noopener noreferrer">几何体 (<code>Geometry</code>)</a> 可以被多个<a href="https://threejs.org/docs/#api/zh/objects/Mesh" target="_blank" rel="nofollow noopener noreferrer">网格 (<code>Mesh</code>)</a> 对象使用。比如在不同的位置画两个蓝色立方体，需要两个<a href="https://threejs.org/docs/#api/zh/objects/Mesh" target="_blank" rel="nofollow noopener noreferrer">网格 (<code>Mesh</code>)</a> 对象来代表每一个立方体的位置和方向。但只需一个<a href="https://threejsfundamentals.org/threejs/lessons/zh_cn/Geometry" target="_blank" rel="nofollow noopener noreferrer">几何体 (<code>Geometry</code>)</a> 来存放立方体的顶点数据，和一种<a href="https://threejs.org/docs/#api/zh/materials/Material" target="_blank" rel="nofollow noopener noreferrer">材质 (<code>Material</code>)</a> 来定义立方体的颜色为蓝色就可以了。两个<a href="https://threejs.org/docs/#api/zh/objects/Mesh" target="_blank" rel="nofollow noopener noreferrer">网格 (<code>Mesh</code>)</a> 对象都引用了相同的<a href="https://threejsfundamentals.org/threejs/lessons/zh_cn/Geometry" target="_blank" rel="nofollow noopener noreferrer">几何体 (<code>Geometry</code>)</a> 和<a href="https://threejs.org/docs/#api/zh/materials/Material" target="_blank" rel="nofollow noopener noreferrer">材质 (<code>Material</code>)</a>。</p>
</li>
<li>
<p><a href="https://threejsfundamentals.org/threejs/lessons/zh_cn/Geometry" target="_blank" rel="nofollow noopener noreferrer">几何体 (<code>Geometry</code>)</a> 对象顾名思义代表一些几何体，如球体、立方体、平面、狗、猫、人、树、建筑等物体的<strong>顶点信息</strong>。Three.js 内置了许多<a href="https://threejsfundamentals.org/threejs/lessons/zh_cn/threejs-primitives.html" target="_blank" rel="nofollow noopener noreferrer">基本几何体</a> 。你也可以<a href="https://threejsfundamentals.org/threejs/lessons/zh_cn/threejs-custom-buffergeometry.html" target="_blank" rel="nofollow noopener noreferrer">创建自定义几何体</a>或<a href="https://threejsfundamentals.org/threejs/lessons/zh_cn/threejs-load-obj.html" target="_blank" rel="nofollow noopener noreferrer">从文件中加载几何体</a>。</p>
</li>
<li>
<p><a href="https://threejs.org/docs/#api/zh/materials/Material" target="_blank" rel="nofollow noopener noreferrer">材质 (<code>Material</code>)</a> 对象代表<a href="https://threejsfundamentals.org/threejs/lessons/zh_cn/threejs-materials.html" target="_blank" rel="nofollow noopener noreferrer">绘制几何体的表面属性</a>，包括使用的颜色，和光亮程度。一个<a href="https://threejs.org/docs/#api/zh/materials/Material" target="_blank" rel="nofollow noopener noreferrer">材质 (<code>Material</code>)</a> 可以引用一个或多个<a href="https://threejs.org/docs/#api/zh/textures/Texture" target="_blank" rel="nofollow noopener noreferrer">纹理 (<code>Texture</code>)</a>，这些纹理可以用来，打个比方，将图像包裹到几何体的表面。</p>
</li>
<li>
<p><a href="https://threejs.org/docs/#api/zh/textures/Texture" target="_blank" rel="nofollow noopener noreferrer">纹理 (<code>Texture</code>)</a> 对象通常表示一幅要[从文件中加载，要么在画布上生成，要么由另一个场景渲染出的图像。</p>
</li>
<li>
<p><a href="https://threejs.org/docs/#api/zh/lights/Light" target="_blank" rel="nofollow noopener noreferrer">光源 (<code>Light</code>)</a> 对象代表不同种类的光。</p>
</li>
</ul>
<h2 data-id="heading-3">正方体</h2>
<p>有了以上基本概念，接下来就用Three.js画个正方体 。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/add5739d96114ff1bf076b3ecc7edf7a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先是加载 three.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script type=<span class="hljs-string">"module"</span>>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> THREE <span class="hljs-keyword">from</span> <span class="hljs-string">'pathxxx/three.module.js'</span>;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把<code>type="module"</code>放到 script 标签中很重要。这可以让我们使用<code>import</code>关键字加载 three.js。还有其他的方法可以加载 three.js，但是自 r106 开始，使用模块是最推荐的方式。模块的优点是可以很方便地导入需要的其他模块。这样我们就不用再手动引入它们所依赖的其他文件了。</p>
<p>下一步我们需要一个<code><canvas></code>标签。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><body>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">canvas</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span></span>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Three.js 需要使用这个 canvas 标签来绘制，所以我们要先获取它然后传给 three.js。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script type=<span class="hljs-string">"module"</span>>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> THREE <span class="hljs-keyword">from</span> <span class="hljs-string">'pathxxx/three.module.js'</span>;
 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#c'</span>);
  <span class="hljs-keyword">const</span> renderer = <span class="hljs-keyword">new</span> THREE.WebGLRenderer(&#123;canvas&#125;);
  ...
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拿到 canvas 后我们需要创建一个 <a href="https://threejs.org/docs/#api/zh/renderers/WebGLRenderer" target="_blank" rel="nofollow noopener noreferrer">WebGL 渲染器 (<code>WebGLRenderer</code>)</a>。渲染器负责将你提供的所有数据渲染绘制到 canvas 上。之前还有其他渲染器，比如 CSS 渲染器 (<code>CSSRenderer</code>)、Canvas 渲染器 (<code>CanvasRenderer</code>)。将来也可能会有 WebGL2 渲染器 (<code>WebGL2Renderer</code>) 或 WebGPU 渲染器 (<code>WebGPURenderer</code>)。目前的话是 <a href="https://threejs.org/docs/#api/zh/renderers/WebGLRenderer" target="_blank" rel="nofollow noopener noreferrer">WebGL 渲染器 (<code>WebGLRenderer</code>)</a>，它通过 WebGL 将三维空间渲染到 canvas 上。</p>
<p>注意这里有一些细节。如果你没有给 three.js 传 canvas，three.js 会自己创建一个 ，但是你必须手动把它添加到文档中。</p>
<p>接下来我们需要一个<a href="https://threejs.org/docs/#api/zh/cameras/PerspectiveCamera" target="_blank" rel="nofollow noopener noreferrer">透视摄像机 (<code>PerspectiveCamera</code>)</a>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fov = <span class="hljs-number">75</span>;
<span class="hljs-keyword">const</span> aspect = <span class="hljs-number">2</span>;  <span class="hljs-comment">// 相机默认值</span>
<span class="hljs-keyword">const</span> near = <span class="hljs-number">0.1</span>;
<span class="hljs-keyword">const</span> far = <span class="hljs-number">5</span>;
<span class="hljs-keyword">const</span> camera = <span class="hljs-keyword">new</span> THREE.PerspectiveCamera(fov, aspect, near, far);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>fov</code>是视野范围 (field of view) 的缩写。上述代码中是指垂直方向为 75 度。 注意 three.js 中大多数的角用弧度表示，但是因为某些原因透视摄像机使用角度表示。</p>
<p><code>aspect</code>指画布的宽高比。我们将在别的文章详细讨论，在默认情况下 画布是 300x150 像素，所以宽高比为 300/150 或者说 2。</p>
<p><code>near</code>和<code>far</code>代表近平面和远平面，它们限制了摄像机面朝方向的可绘区域。 任何距离小于或超过这个范围的物体都将被裁剪掉 (不绘制)。</p>
<p>这四个参数定义了一个 <em>"视椎 (frustum)"</em>。 <em>视椎 (frustum)</em> 是指一个像被削去顶部的金字塔形状。换句话说，可以把 "视椎 (frustum)" 想象成其他三维形状如球体、立方体、棱柱体、截椎体。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7d3379e30284c3ebbfe76b6639fbe05~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>近平面和远平面的高度由视野范围决定，宽度由视野范围和宽高比决定。</p>
<p>视椎体内部的物体将被绘制，视椎体外的东西将不会被绘制。</p>
<p>摄像机默认指向 Z 轴负方向，上方向朝向 Y 轴正方向。我们将会把立方体放置在坐标原点，所以我们需要往后移一下摄像机才能显示出物体。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">camera.position.z = <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f5fe2409df04e80a3fd01d57522b64d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们能看到摄像机的位置在<code>z = 2</code>。它朝向 Z 轴负方向。我们的视椎体范围从摄像机前方 0.1 到 5。因为这张图是俯视图，视野范围会受到宽高比的影响。画布的宽度是高度的两倍，所以水平视角会比我们设置的垂直视角 75 度要大。</p>
<p>然后我们创建一个<a href="https://threejs.org/docs/#api/zh/scenes/Scene" target="_blank" rel="nofollow noopener noreferrer">场景 (<code>Scene</code>)</a>。<a href="https://threejs.org/docs/#api/zh/scenes/Scene" target="_blank" rel="nofollow noopener noreferrer">场景 (<code>Scene</code>)</a> 是 three.js 的基本的组成部分。需要 three.js 绘制的东西都需要加入到 scene 中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> scene = <span class="hljs-keyword">new</span> THREE.Scene();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后创建一个包含盒子信息的<a href="https://threejs.org/docs/#api/zh/geometries/BoxGeometry" target="_blank" rel="nofollow noopener noreferrer">立方几何体 (<code>BoxGeometry</code>)</a>。几乎所有希望在 three.js 中显示的物体都需要一个包含了组成三维物体的顶点信息的几何体。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> boxWidth = <span class="hljs-number">1</span>;
<span class="hljs-keyword">const</span> boxHeight = <span class="hljs-number">1</span>;
<span class="hljs-keyword">const</span> boxDepth = <span class="hljs-number">1</span>;
<span class="hljs-keyword">const</span> geometry = <span class="hljs-keyword">new</span> THREE.BoxGeometry(boxWidth, boxHeight, boxDepth);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后创建一个基本的材质并设置它的颜色. 颜色的值可以用 css 方式和十六进制来表示。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> material = <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial(&#123;<span class="hljs-attr">color</span>: <span class="hljs-number">0x44aa88</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再创建一个<a href="https://threejs.org/docs/#api/zh/objects/Mesh" target="_blank" rel="nofollow noopener noreferrer">网格 (<code>Mesh</code>)</a> 对象，它包含了：</p>
<ol>
<li><a href="https://threejsfundamentals.org/threejs/lessons/zh_cn/Geometry" target="_blank" rel="nofollow noopener noreferrer">几何体 (<code>Geometry</code>)</a>(物体的形状)</li>
<li><a href="https://threejs.org/docs/#api/zh/materials/Material" target="_blank" rel="nofollow noopener noreferrer">材质 (<code>Material</code>)</a>(如何绘制物体，光滑还是平整，什么颜色，什么贴图等等)</li>
<li>对象在场景中相对于他父对象的位置、朝向、和缩放。下面的代码中父对象即为场景对象。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> cube = <span class="hljs-keyword">new</span> THREE.Mesh(geometry, material);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们将网格添加到场景中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">scene.add(cube);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后将场景和摄像机传递给渲染器来渲染出整个场景。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">renderer.render(scene, camera);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/290bee1a11fc45bfa792bf7294b0a738~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>很难看出来这是一个三维的立方体，因为我们直视 Z 轴的负方向并且立方体和坐标轴是对齐的，所以我们只能看到一个面。</p>
<h2 data-id="heading-4">运动的正方体</h2>
<p>我们来让立方体旋转起来，以便更好的在三维环境中显示。为了让它动起来我们需要用到一个渲染循环函数 <a href="https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame" target="_blank" rel="nofollow noopener noreferrer"><code>requestAnimationFrame</code></a>.</p>
<p>代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">time</span>) </span>&#123;
  time *= <span class="hljs-number">0.001</span>;  <span class="hljs-comment">// 将时间单位变为秒</span>
 
  cube.rotation.x = time;
  cube.rotation.y = time;
 
  renderer.render(scene, camera);
 
  requestAnimationFrame(render);
&#125;
requestAnimationFrame(render);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>requestAnimationFrame</code>函数会告诉浏览器你需要显示动画。传入一个函数作为回调函数。本例中的函数是<code>render</code>函数。如果你更新了跟页面显示有关的任何东西，浏览器会调用你传入的函数来重新渲染页面。我们这里是调用 three.js 的<code>renderer.render</code>函数来绘制我们的场景。</p>
<p><code>requestAnimationFrame</code>会将页面开始加载到函数运行所经历的时间当作入参传给回调函数，单位是毫秒数</p>
<p>然后我们把立方体的 X 轴和 Y 轴方向的旋转角度设置成这个时间。这些旋转角度是弧度制。一圈的弧度为 2Π所以我们的立方体在每个方向旋转一周的时间为 6.28 秒。</p>
<p>最后渲染我们的场景并调用另一个帧动画函数来继续我们的循环。</p>
<p>回调函数之外在主进程中我们调用一次<code>requestAnimationFrame</code>来开始整个渲染循环。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7aa176ba29694607b16c2274823ee34d~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-11-14-51-54.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">添加灯光效果</h2>
<p>效果好了一些但还是很难看出是三维的。我们来添加些光照效果。three.js 中有很多种类型的灯光，现在我们先创建一盏平行光。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-keyword">const</span> color = <span class="hljs-number">0xFFFFFF</span>;
  <span class="hljs-keyword">const</span> intensity = <span class="hljs-number">1</span>;
  <span class="hljs-keyword">const</span> light = <span class="hljs-keyword">new</span> THREE.DirectionalLight(color, intensity);
  light.position.set(-<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">4</span>);
  scene.add(light);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>平行光有一个位置和目标点。默认值都为 (0, 0, 0)。我们这里 将灯光的位置设为 (-1, 2, 4)，让它位于摄像机前面稍微左上方一点的地方。目标点还是 (0, 0, 0)，让它朝向坐标原点方向。</p>
<p>我们还需要改变下立方体的材质。<a href="https://threejs.org/docs/#api/zh/materials/MeshBasicMaterial" target="_blank" rel="nofollow noopener noreferrer"><code>MeshBasicMaterial</code></a>材质不会受到灯光的影响。我们将他改成会受灯光影响的 <a href="https://threejs.org/docs/#api/zh/materials/MeshPhongMaterial" target="_blank" rel="nofollow noopener noreferrer"><code>MeshPhongMaterial</code></a>材质。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> material = <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial(&#123;<span class="hljs-attr">color</span>: <span class="hljs-number">0x44aa88</span>&#125;);  <span class="hljs-comment">// 绿蓝色</span>
<span class="hljs-keyword">const</span> material = <span class="hljs-keyword">new</span> THREE.MeshPhongMaterial(&#123;<span class="hljs-attr">color</span>: <span class="hljs-number">0x44aa88</span>&#125;);  <span class="hljs-comment">// 绿蓝色</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是我们新的项目结构</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a966bac64a05409ea4a98e91721a82b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>效果</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d582f6f6f86c4711b11d47d8a0c08cb9~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-11-14-53-24.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在应该可以很清楚的看出是三维立方体了。</p>
<h2 data-id="heading-6">让场景更为复杂</h2>
<p>我们再添加两个立方体使场景更加复杂。</p>
<p>每个立方体会引用同一个几何体和不同的材质，这样每个立方体将会是不同的颜色。</p>
<p>首先我们创建一个根据指定的颜色生成新材质的函数。它会根据指定的几何体生成对应网格，然后将网格添加进场景并设置其 X 轴的位置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeInstance</span>(<span class="hljs-params">geometry, color, x</span>) </span>&#123;
  <span class="hljs-keyword">const</span> material = <span class="hljs-keyword">new</span> THREE.MeshPhongMaterial(&#123;color&#125;);
 
  <span class="hljs-keyword">const</span> cube = <span class="hljs-keyword">new</span> THREE.Mesh(geometry, material);
  scene.add(cube);
 
  cube.position.x = x;
 
  <span class="hljs-keyword">return</span> cube;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们将用三种不同的颜色和 X 轴位置调用三次函数，将生成的网格实例存在一个数组中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> cubes = [
  makeInstance(geometry, <span class="hljs-number">0x44aa88</span>,  <span class="hljs-number">0</span>),
  makeInstance(geometry, <span class="hljs-number">0x8844aa</span>, -<span class="hljs-number">2</span>),
  makeInstance(geometry, <span class="hljs-number">0xaa8844</span>,  <span class="hljs-number">2</span>),
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们将在渲染函数中旋转三个立方体。我们给每个立方体设置了稍微不同的旋转角度。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">time</span>) </span>&#123;
  time *= <span class="hljs-number">0.001</span>;  <span class="hljs-comment">// 将时间单位变为秒</span>
 
  cubes.forEach(<span class="hljs-function">(<span class="hljs-params">cube, ndx</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> speed = <span class="hljs-number">1</span> + ndx * <span class="hljs-number">.1</span>;
    <span class="hljs-keyword">const</span> rot = time * speed;
    cube.rotation.x = rot;
    cube.rotation.y = rot;
  &#125;);
 
  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里是结果。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf218a8d823f41f899412347b9e26786~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-11-14-54-34.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果你对比上面的示意图可以看到此效果符合我们的预想。位置为 X = -2 和 X = +2 的立方体有一部分在我们的视椎体外面。他们大部分是被包裹的，因为水平方向的视角非常大。</p>
<h2 data-id="heading-7">现在的项目结构</h2>
<p>我们的项目现在有了这样的结构</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b50a9cfcf194138822032b3aad865af~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们有三个<a href="https://threejs.org/docs/#api/zh/objects/Mesh" target="_blank" rel="nofollow noopener noreferrer">网格 (<code>Mesh</code>)</a> 引用了相同的<a href="https://threejs.org/docs/#api/zh/geometries/BoxGeometry" target="_blank" rel="nofollow noopener noreferrer">立方几何体 (<code>BoxGeometry</code>)</a>。每个<a href="https://threejs.org/docs/#api/zh/objects/Mesh" target="_blank" rel="nofollow noopener noreferrer">网格 (<code>Mesh</code>)</a> 引用了一个单独的 <a href="https://threejs.org/docs/#api/zh/materials/MeshPhongMaterial" target="_blank" rel="nofollow noopener noreferrer"><code>MeshPhongMaterial</code></a>材质来显示不同的颜色。</p>
<h2 data-id="heading-8">写在最后</h2>
<p>本文介绍了Three.js的基本概念，并通过了一个简单的实例从零到一搭建了一个三维场景。麻雀虽小五脏俱全，希望对大家有所帮助。</p>
<blockquote>
<p>本文发布自 云图三维大前端团队，文章未经授权禁止任何形式的转载。</p>
</blockquote></div>  
</div>
            