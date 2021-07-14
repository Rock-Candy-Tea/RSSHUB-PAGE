
---
title: '菜鸟也要学ThreeJs（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7950ff1ae014b62ba9ed1db1e783b0d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 04:01:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7950ff1ae014b62ba9ed1db1e783b0d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作为前端开发者，谁不喜欢这样的所见即所得的快乐呢？</p>
<p>构建场景 物理引擎 塑造模型</p>
<p>说起来酷炫，但是实际学起来实在是头大，WegGl的管道着色器基本上写起来和学一门新的语言一样，ThreeJs的话 教程又没那么多，实在是费力。</p>
<p>最近发现了国外大佬的课，分享一下自己的ThreeJs学习路程～</p>
<p>在文章中用到的代码 都会在附在附录上～</p>
<p>接下来就是干货时间：</p>
<p>首先建立HTML文件</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>03 - Basic Scene<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"webgl"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./three.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./script.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JS文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// // Canvas</span>
<span class="hljs-comment">// const canvas = document.querySelector('canvas.webgl')</span>

<span class="hljs-comment">// // Sizes</span>
<span class="hljs-comment">// const sizes = &#123;</span>
<span class="hljs-comment">//     width: 800,</span>
<span class="hljs-comment">//     height: 600</span>
<span class="hljs-comment">// &#125;</span>

<span class="hljs-comment">// // Scene</span>
<span class="hljs-comment">// const scene = new THREE.Scene()</span>

<span class="hljs-comment">// // Object</span>
<span class="hljs-comment">// const cubeGeometry = new THREE.BoxGeometry(1, 1, 1)</span>
<span class="hljs-comment">// const cubeMaterial = new THREE.MeshBasicMaterial(&#123;</span>
<span class="hljs-comment">//     color: '#ff0000'</span>
<span class="hljs-comment">// &#125;)</span>
<span class="hljs-comment">// const cubeMesh = new THREE.Mesh(cubeGeometry, cubeMaterial)</span>
<span class="hljs-comment">// scene.add(cubeMesh)</span>

<span class="hljs-comment">// // Camera</span>
<span class="hljs-comment">// const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height)</span>
<span class="hljs-comment">// camera.position.z = 3</span>
<span class="hljs-comment">// scene.add(camera)</span>

<span class="hljs-comment">// // Renderer</span>
<span class="hljs-comment">// const renderer = new THREE.WebGLRenderer(&#123;</span>
<span class="hljs-comment">//     canvas: canvas</span>
<span class="hljs-comment">// &#125;)</span>
<span class="hljs-comment">// renderer.setSize(sizes.width, sizes.height)</span>
<span class="hljs-comment">// renderer.render(scene, camera)</span>


<span class="hljs-keyword">const</span> scene = <span class="hljs-keyword">new</span> THREE.Scene()

<span class="hljs-keyword">const</span> geometry = <span class="hljs-keyword">new</span> THREE.BoxGeometry(<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>)
<span class="hljs-keyword">const</span> material = <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial(&#123; <span class="hljs-attr">color</span>: <span class="hljs-number">0xff0000</span> &#125;)

<span class="hljs-keyword">const</span> mesh = <span class="hljs-keyword">new</span> THREE.Mesh(geometry,material)
scene.add(mesh)

<span class="hljs-keyword">const</span> sizes = &#123;
  <span class="hljs-attr">width</span>: <span class="hljs-number">800</span>,
  <span class="hljs-attr">height</span>: <span class="hljs-number">600</span>
&#125;
<span class="hljs-keyword">const</span> camera = <span class="hljs-keyword">new</span> THREE.PerspectiveCamera(<span class="hljs-number">75</span>,sizes.width/sizes.height)
camera.position.z = <span class="hljs-number">3</span>
scene.add(camera)

<span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.webgl'</span>)

<span class="hljs-keyword">const</span> render = <span class="hljs-keyword">new</span> THREE.WebGLRenderer(&#123;
<span class="hljs-attr">canvas</span>:canvas
&#125;)

render.setSize(sizes.width,sizes.height)

render.render(scene,camera)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后记得再去下载THREEJS文件 并且引入就可以啦！</p>
<p>Three Js 四大要素</p>
<blockquote>
<p>1.包含一些对象的场景 Scene</p>
<p>2.一些对象 Object</p>
<p>3.摄像机  Camera</p>
<p>4.渲染器  Render</p>
</blockquote>
<h1 data-id="heading-0">Scene</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> scene = <span class="hljs-keyword">new</span> THREE.Scene()
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">Object</h1>
<p>创建对象，我们需要先创建一个Mesh</p>
<h2 data-id="heading-2">Mesh</h2>
<p>一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fthreejs.org%2Fdocs%2F%23api%2Fen%2Fobjects%2FMesh" target="_blank" rel="nofollow noopener noreferrer" title="https://threejs.org/docs/#api/en/objects/Mesh" ref="nofollow noopener noreferrer">Mesh</a> 是几何（形状）和材料（外观）的组合。</p>
<p>那么我们创建Mesh 对应就需要先创建几何Geomotry ，以及材料Material</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> geometry = <span class="hljs-keyword">new</span> THREE.BoxGeometry(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>)
<span class="hljs-keyword">const</span> material = <span class="hljs-keyword">new</span> THREE.MeshBasicMaterial(&#123; <span class="hljs-attr">color</span>: <span class="hljs-number">0xff0000</span> &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>小Tips：</p>
<p>颜色16进制表示  分别表示 R G B 即 红 绿 蓝 ，颜色深度分别从0 到 f</p>
<p># ff0000</p>
<p>表示为红色</p>
<p>ff  => 红色满格</p>
<p>00 => 不要绿色</p>
<p>00 => 不要蓝色</p>
<p>所以如上ff0000就表示纯红色了</p>
</blockquote>
<p>创建好<code>geometry</code>和<code>material</code>就可以通过<code>THREE.Mesh()</code>来合并生成一个Mesh对象了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mesh = <span class="hljs-keyword">new</span> THREE.Mesh(geometry,material)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">添加对象</h2>
<p>创建Mesh 之后 一定记得像Scen中进行添加，不然Camera是看不到它的</p>
<pre><code class="hljs language-js copyable" lang="js">scene.add(mesh)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">Camera</h1>
<p>1.相机不可见</p>
<p>2.可以设置多个相机，但是render的时候 只能有一个</p>
<p>常规的 我们创建<code>PerspectiveCamera</code>透视相机，可以实现使近处的物体看起来比远处的物体更突出的效果。</p>
<p>设置相机需要像个参数</p>
<h2 data-id="heading-5">View 视角</h2>
<p>视野是你的视角有多大。如果您使用非常大的角度，您将能够同时看到各个方向，但失真很大，因为结果将绘制在一个小矩形上。如果您使用小角度，则事物看起来会放大。视野（或 <code>fov</code>）以度数表示，对应于垂直视角。在本练习中，我们将使用 <code>75</code> 度角。</p>
<p>小视角：</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7950ff1ae014b62ba9ed1db1e783b0d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210608134351009" loading="lazy" referrerpolicy="no-referrer">
<p>大视角：</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d98a8a8952c42ec9d5a771484721bc1~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210608134417756" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-6">Size 纵横比</h2>
<p>在大多数情况下，纵横比是画布的宽度除以其高度。我们暂时没有指定任何宽度或高度，但我们稍后需要。同时，我们将创建一个具有临时值的对象，我们可以重用它。</p>
<p>不要忘记将相机添加到场景中。一切都应该可以在不将相机添加到场景中的情况下工作，但稍后可能会导致错误</p>
<h2 data-id="heading-7">相机位置</h2>
<p>一定记得设置camera的position 或者 rotation 或者scale</p>
<p>否则 摄像机会处于 整个物体的内部，无法看到任何东西</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> camera = <span class="hljs-keyword">new</span> THREE.PerspectiveCamera(<span class="hljs-number">75</span>,sizes.width/sizes.height)
camera.position.z = <span class="hljs-number">3</span>
scene.add(camera)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">Object</h1>
<p>操作ThreeJS 中的 对象 可以帮助我们在后续实现一些动画的效果</p>
<p>之前我们试过<code>position</code>来移动camera的位置，达到不同的视角</p>
<p>后续 我们可以一共有 4 个属性可以转换场景中的对象</p>
<ul>
<li>
<p><code>position</code> （移动物体）</p>
</li>
<li>
<p><code>scale</code> （调整对象大小）</p>
</li>
<li>
<p><code>rotation</code> （旋转对象）</p>
</li>
<li>
<p><code>quaternion</code> （类似旋转对象）</p>
<p>注意我们改变object的位置，一定要在render.renderer 函数调用之前，否则就不会生效了。</p>
</li>
</ul>
<h1 data-id="heading-9">Position</h1>
<p>x 是向右的，y轴是向上的，z轴是向后的（forward to camera）</p>
<p>我们可以通过操作Mesh来 变换</p>
<blockquote>
<p>因为Mesh 即成雨Object.3D 且 代表着一个具体的模块，即由形状和材质两部分组成。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">mesh.position.x = <span class="hljs-number">0.7</span>
mesh.position.y = - <span class="hljs-number">0.6</span>
mesh.position.z = <span class="hljs-number">1</span>

<span class="hljs-comment">//或者</span>

mesh.position.set(<span class="hljs-number">0.7</span>, - <span class="hljs-number">0.6</span>, <span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">Length</h2>
<p>Position 设置后 是一个Vector3[3维向量]，因此我们可以求的具体的值</p>
<pre><code class="hljs language-js copyable" lang="js">mesh.position.length()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样可以得到一个具体的向量的长度。</p>
<p>同时，如果我们对两个Vectore3 需要知道他们的距离，可以使用<code>distanceTo</code>函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//当前mesh与相机向量的距离</span>
mesh.position.distanceTo(camera.position)

<span class="hljs-comment">//与向量(0,1,2)的距离</span>
mesh.positon.distanceTo(<span class="hljs-keyword">new</span> THREE.Vector3(<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">归一化【标准化】</h2>
<p>相当于 将当前向量归一化为标准向量，只需要使用<code>normalize</code>函数即可。</p>
<pre><code class="hljs language-js copyable" lang="js">mesh.position.distanceTo(camera.position)
<span class="hljs-comment">//此时 mesh的length是1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">辅助线</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * Axes Helper
 */</span>
<span class="hljs-keyword">const</span> axesHelper = <span class="hljs-keyword">new</span> THREE.AxesHelper(<span class="hljs-number">2</span>)
scene.add(axesHelper)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>AxesHelper</code>的参数表示辅助线的长度</p>
<p>绿色 - y轴</p>
<p>红色 - x轴</p>
<p>蓝色 - z轴</p>
<p>默认情况下，Camera是对准z轴的，也就是如果我们不移动camera的x ， y 那么会看到如下的画面</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43bb9e8fdd6b4f75a2eff743162fd6eb~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210609233638336" loading="lazy" referrerpolicy="no-referrer">
<h1 data-id="heading-13"></h1>
<h1 data-id="heading-14">Scale</h1>
<p>按某个方向 缩放</p>
<pre><code class="hljs language-js copyable" lang="js">mesh.scale.x = <span class="hljs-number">2</span>
mesh.scale.y = <span class="hljs-number">0.25</span>
mesh.scale.z = <span class="hljs-number">0.5</span> 

mesh.scale.set(<span class="hljs-number">2</span>,<span class="hljs-number">0.5</span>,<span class="hljs-number">0.5</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">Rotation</h2>
<p>1.旋转</p>
<p>旋转以当前的轴为中心 旋转度数</p>
<ul>
<li>如果你在 <code>y</code> 轴上旋转，你可以把它想象成一个旋转木马。</li>
<li>如果你在 <code>x</code> 轴上旋转，你可以想象你正在旋转你将要乘坐的汽车的轮子。</li>
<li>如果你在 <code>z</code> 轴上旋转，你可以想象你正在旋转你将要乘坐的飞机前面的螺旋桨。</li>
</ul>
<p>默认2PI 为一个圆周</p>
<pre><code class="hljs language-js copyable" lang="js">mesh.rotation.x = <span class="hljs-built_in">Math</span>.PI * <span class="hljs-number">0.25</span>
mesh.rotation.y = <span class="hljs-built_in">Math</span>.PI * <span class="hljs-number">0.25</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是注意了，在普通的旋转中，无论我们在js中 rotation的顺序如何，都是按照 先x 再y 再z 进行旋转的，然而当我们执行x轴的旋转操作后，此时再执行y轴 就已经和初始的y轴不一致了，因此 我们需要通过加锁来进行设置</p>
<pre><code class="hljs language-js copyable" lang="js">object.rotation.reorder(<span class="hljs-string">'YXZ'</span>)
<span class="hljs-comment">//1.此处XYZ为字符串 2.一定要大写</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置后即表示，按照 先y轴 再x轴 再z轴的顺讯进行旋转。</p>
<h3 data-id="heading-16">Look At</h3>
<p><code>Camera.lookat(Vector3)</code>表示 将摄像机指向目标的向量</p>
<pre><code class="hljs language-js copyable" lang="js">camera.lookAt(<span class="hljs-keyword">new</span> THREE.Vector3(<span class="hljs-number">0</span>, - <span class="hljs-number">1</span>, <span class="hljs-number">0</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即表示将摄像机指向 0 -1 0 的向量位置</p>
<p>当然，我们也可以使用<code>camera.lookAt(mesh.position)</code>，此时我们的mesh就会出现在屏幕的正中央。</p>
<h3 data-id="heading-17">Group</h3>
<p>需要对一个<code>object</code>进行多次变换操作的时候，我们可以通过创建一个<code>group</code>然后，直接移动group即可。</p></div>  
</div>
            