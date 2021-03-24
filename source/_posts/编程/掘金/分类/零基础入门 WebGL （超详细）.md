
---
title: '零基础入门 WebGL （超详细）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/846c536e71a44891b7e984dd49061b06~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 19:12:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/846c536e71a44891b7e984dd49061b06~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>只要理解了 WebGL 背后的概念，学习 WebGL 并没有那么难。很多 WebGL 入门文章并没有介绍这些重要的概念，直接使用 WebGL 复杂的 API 开始渲染图形，很轻松就把入坑文变成了劝退文。这篇文章将会着重讲解这些概念，并一步步探究 WebGL 是如何渲染图片到屏幕的，理解这些重要的概念，将会大大降低学习曲线。</p>
<h2 data-id="heading-0">什么是 WebGL？</h2>
<p>WebGL 可以用来在网页上绘制和渲染复杂的图形或者进行大量计算，它完全集成到浏览器的所有网页标准中，无需安装任何插件即可使用。由非营利 Khronos Group 设计和维护。WebGL 除了应用在图形渲染，如游戏、数据可视化、地图、AR/VR等等，还能应用在深度学习等需要大量计算的场景。</p>
<p>我们知道在网页中可以用 <code>canvas</code> 来画一些 2d 图形。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>)
<span class="hljs-keyword">const</span> ctx = canvas.getContext(<span class="hljs-string">'2d'</span>) <span class="hljs-comment">// 建立一个二维渲染上下文</span>
<span class="hljs-comment">// 现在我们就可以用 ctx 来画图形</span>
ctx.fillRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">100</span>, <span class="hljs-number">100</span>) <span class="hljs-comment">// 画一个方块</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看见上方获取上下文的参数传的是 <code>2d</code>。所以一般都会认为它只能用来在网页上画 2D 图形，而 WebGL 才能画 3D 图形。其实真实情况是，我们完全可以用 <code>2d</code> 来画 3D 图形，甚至是在终端上使用字符来渲染 3D 图形，这背后都是数学的功劳。WebGl 其实只是一个光栅化引擎，它非常底层，我们只能用它来画点，线和三角形。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>)
<span class="hljs-keyword">const</span> gl = canvas.getContext(<span class="hljs-string">'webgl'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里将 <code>2d</code> 换成 <code>webgl</code> 就可以获取到三维渲染上下文。目前大部分浏览器都支持了 WebGL，不过有的浏览器需要传入 <code>experimental-webgl</code>，比如 IE11。</p>
<p>后面我们会编写在 GPU 中运行的代码（着色器），并且会把数据从 CPU 传递给 GPU。</p>
<p>CPU 和 GPU 设计目标的不同，它们分别针对了两种不同的应用场景。GPU 最初的目的是为了计算机图形和视频游戏。一般我们会在 CPU 中管理整个系统的任务，将一些计算量大，但没什么技术含量，而且要重复很多次的任务交给 GPU 来完成。GPU 拥有数千的内核，可以并发完成大量计算，计算这些任务会比 CPU 快得多。这就是为什么 WebGL 要用到 GPU 的能力，GPU 可以极大提升渲染图片的速度。</p>
<h3 data-id="heading-1">OpenGL 介绍</h3>
<p>WebGL 基于 OpenGL。OpenGL(Open Graphics Library) 是用于渲染2D、3D矢量图形的跨语言、跨平台的应用程序编程接口，常用于CAD、虚拟现实、科学可视化程序和电子游戏开发。实际的 OpenGL 库通常是显卡生产商根据规范进行开发的。</p>
<p>OpenGL 前身是 SGI 的 IRIS GL API 它在当时被认为是最先进的科技并成为事实上的行业标准，后由 SGI 转变为一项开放标准 OpenGL。1992年 SGI 创建 OpenGL架构审查委员会，2006年将 OpenGL API 标准的控制权交给 Khronos Group。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/846c536e71a44891b7e984dd49061b06~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>OpenGL 是跨平台的，在移动设备上一般使用 OpenGL ES(OpenGL for Embedded Systems) 它是 OpenGL 的子集，上图展示了 OpenGL 和 OpenGL ES 的时间线。</p>
<p>WebGL 基于 OpenGL ES 2.0，它是 OpenGL ES 2.0 的子集。WebGL 2.0 基于 OpenGL ES 3.0。大多数现代浏览器都支持了 WebGL 2.0，但是苹果到目前为止还没有支持 WebGL 2.0！所以现在还是大部分应用还是基于 WebGL 1.0 开发。</p>
<h2 data-id="heading-2">坐标系</h2>
<p>我们知道 2D canvas 中原点在左上角，Y 轴正值向下。</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9487fcc26a6e40a28043729c4dc3fff8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>OpenGL 中的坐标系似乎更符合我们的直觉。</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c31f1e1b8ba4ec5a4cf493bbcea53a0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>原点在中间，Y 正轴向上，X 正轴向右。</p>
<p>注意 OpenGL 中的 X 轴， Y 轴和 Z 轴最大值是 1，最小值是 -1。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> canvasWidth = <span class="hljs-number">500</span>
<span class="hljs-keyword">const</span> x = <span class="hljs-number">100</span>

<span class="hljs-keyword">const</span> two = x / canvasWidth * <span class="hljs-number">2</span> <span class="hljs-comment">// 变为 0 -> 2</span>
<span class="hljs-keyword">const</span> clipX = two - <span class="hljs-number">1</span> <span class="hljs-comment">// 0 -> 2 变为 -1 -> +1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面将点的 X 坐标处理到 -1 到 +1 之间，三个点的坐标都处理到这 -1 和 +1 之间，我们就称为<strong>标准化设备坐标(Normalized Device Coordinates, NDC)</strong>，标准化设备坐标是一个 x、y 和 z 值在 -1 到 1 的一小段空间。任何落在范围外的坐标都会被丢弃/裁剪，不会显示在你的屏幕上。</p>
<h3 data-id="heading-3">左右手坐标系</h3>
<p>我们上面没有展示 OpenGL 中的 Z 轴张啥样，因为 Z 轴有两种形式，一种是指向屏幕外（正值在屏幕外），另一种是指向屏幕（正值在屏幕内）。</p>
<p>当 Z 轴指向屏幕外时，我们称此坐标系为右手坐标系，当 Z 轴指向屏幕内我们称为左手坐标系。</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be87bdf8cfb843ffaab7b094632ed4da~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们可以伸出左右手来比划下，其中中指指向的就是正 Z 轴。</p>
<h4 data-id="heading-4">旋转正方向</h4>
<p>左右手坐标系对旋转的正方向正好相反，同样伸出我们的左右手。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d05a74624454215ab8b7c5ae0126dcb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>左手坐标系用左手，右手坐标系用右手。大拇指朝向轴的正方向，剩下 4 根手指弯曲方向就是旋转正方向。如果我们从轴的正端来看，右手坐标系的正方向是逆时针旋转，左手坐标系的正方向是顺时针旋转。</p>
<h3 data-id="heading-5">OpenGL 是哪个坐标系？</h3>
<p>那么 OpenGL 是左手坐标系，还是右手坐标系？答案是 <strong>都不是</strong>。</p>
<p>比如我们现在有两个点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> point1  = [<span class="hljs-number">0.5</span>, <span class="hljs-number">0.5</span>, <span class="hljs-number">0.1</span>] <span class="hljs-comment">// 分别是 X，Y，Z 的值</span>
<span class="hljs-keyword">const</span> point2 = [<span class="hljs-number">0.5</span>, <span class="hljs-number">0.5</span>, -<span class="hljs-number">0.2</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们在 OpenGL 中画出上面两点，哪个点在前哪个点在后？</p>
<p>这取决于我们渲染两个点的顺序，如果后渲染 <code>point1</code> 则 <code>point1</code> 覆盖 <code>point2</code>，如果后渲染 <code>point2</code> 则 <code>point2</code> 覆盖 <code>point1</code>。</p>
<h3 data-id="heading-6">深度缓存映射</h3>
<p>如果我们开启 OpenGL 的深度测试。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>)
<span class="hljs-keyword">const</span> gl = canvas.getContext(<span class="hljs-string">'webgl'</span>)
gl.enable(gl.DEPTH_TEST) <span class="hljs-comment">// 激活深度测试</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>深度测试就是将图形的 Z 值<strong>映射存储</strong>到深度缓存区中，这样在我们在 OpenGL 中画各种图形时，我们就知道这个图形离我们近还是远，离我们越近的点会覆盖离我们远的点，如果这个点比缓存中的点远时，则抛弃。</p>
<p>当我们开启了深度测试，无论 <code>point1</code> 和 <code>point2</code> 渲染顺序如何，<code>point2</code> 始终会覆盖 <code>point1</code>。也就是 Z 值小的点会覆盖 Z 值大的点，也就是说 OpenGL 是<strong>左手坐标系</strong>。</p>
<p>OpenGL 中还有个 <code>depthRange</code> 函数，它接收两个参数 <code>depthRange(zNear, zFar)</code> 两个参数都是数字，都必须是 <code>0</code> 到 <code>1</code> 之间的数字。默认情况下为 <code>depthRange(0, 1)</code>，这个函数用来设置深度缓存的范围。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>)
<span class="hljs-keyword">const</span> gl = canvas.getContext(<span class="hljs-string">'webgl'</span>)
gl.depthRange(<span class="hljs-number">1</span>, <span class="hljs-number">0</span>) <span class="hljs-comment">// 反转了默认值</span>
gl.enable(gl.DEPTH_TEST)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们按照上方设置了深度缓存范围，再来渲染 <code>point1</code> 和 <code>point2</code> 我们就发现，无论顺序如何 <code>point1</code> 始终会覆盖 <code>point2</code> 了，OpenGL 变成了<strong>右手坐标系</strong>。</p>
<p>默认情况下深度缓存的范围是 0 到 1。下面我们来看下 OpenGL 是如何将 Z 值([-1, +1]) 变为深度缓存的([0, 1])。</p>
<pre><code class="hljs language-c copyable" lang="c">depth = n + (f - n) * (z + <span class="hljs-number">1</span>) / <span class="hljs-number">2</span> 
<span class="hljs-comment">// n 和 f 是 depthRange 函数设置的。n 是 near，f 是 far。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面展示了如何将 Z 值变成了深度缓存。</p>
<h3 data-id="heading-7">但是</h3>
<p><strong>如果真的在 WebGL 中设置 <code>depthRange(1, 0)</code> 你会发现没有任何效果。</strong> 这是 WebGL 和 OpenGL 的差异之处，根据 WebGL 1.0 的规范</p>
<p><a href="https://www.khronos.org/registry/webgl/specs/1.0/#VIEWPORT_DEPTH_RANGE" target="_blank" rel="nofollow noopener noreferrer">www.khronos.org/registry/we…</a></p>
<blockquote>
<p><strong>6.12 Viewport Depth Range</strong></p>
<p>The WebGL API does not support depth ranges with where the near plane is mapped to a value greater than that of the far plane. A call to depthRange will generate an INVALID_OPERATION error if zNear is greater than zFar.</p>
</blockquote>
<p>也就是在 WebGL 中 <code>depthRange</code> 的 <code>zNear</code> 不允许小于 <code>zFar</code>。</p>
<p>要把 WebGL 变成右手坐标系，还有另外一种方法。</p>
<pre><code class="hljs language-js copyable" lang="js">gl.clearDepth(<span class="hljs-number">0</span>)
gl.depthFunc(gl.GREATER)
gl.clear(gl.DEPTH_BUFFER_BIT)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里将深度缓存设置成 <code>0</code>（默认值是 <code>1</code>）并用 <code>clear</code> 重置深度缓存。然后设置深度比较函数为大于（默认值是小于），这样就可以让 <code>z</code> 值大的顶点覆盖小的顶点了。</p>
<h3 data-id="heading-8">常用坐标系</h3>
<p>一般情况下我们也不会使用 <code>depthRange</code>，<code>clearDepth</code> 这些函数。也就是说默认的话 OpenGL 应该是左手坐标系。这里就是让大家非常混乱的地方，实际上开发中都是使用的<strong>右手坐标系</strong>。</p>
<p>当然并不是右手坐标系比左手坐标系好，而是右手坐标系是 OpenGL 的惯例。例如微软的 DirectX 中惯用的是左手坐标系。</p>
<h2 data-id="heading-9">Hello World</h2>
<p>现在来用 WebGL 来画一个三角形吧。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>)
canvas.width = <span class="hljs-number">300</span>
canvas.height = <span class="hljs-number">300</span>
<span class="hljs-built_in">document</span>.body.append(canvas) <span class="hljs-comment">// 创建和将 canvas 加入页面</span>

<span class="hljs-keyword">const</span> gl = canvas.getContext(<span class="hljs-string">'webgl'</span>)
gl.viewport(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, gl.canvas.width, gl.canvas.height)
<span class="hljs-comment">// 告诉 webgl 如何将 0 到 1 坐标 变为屏幕上的坐标</span>

<span class="hljs-keyword">const</span> vertexShader = gl.createShader(gl.VERTEX_SHADER) 
<span class="hljs-comment">// 创建一个顶点着色器</span>
gl.shaderSource(vertexShader, <span class="hljs-string">`
  attribute vec4 a_position;

  void main() &#123;
    gl_Position = a_position; // 设置顶点位置
  &#125;
`</span>) <span class="hljs-comment">// 编写顶点着色器代码</span>
gl.compileShader(vertexShader) <span class="hljs-comment">// 编译着色器代码</span>

<span class="hljs-keyword">const</span> fragmentShader = gl.createShader(gl.FRAGMENT_SHADER) 
<span class="hljs-comment">// 创建一个片元着色器</span>
gl.shaderSource(fragmentShader, <span class="hljs-string">`
  precision mediump float;
  uniform vec4 u_color;

  void main() &#123;
    gl_FragColor = u_color; // 设置片元颜色
  &#125;
`</span>) <span class="hljs-comment">// 编写片元着色器代码</span>
gl.compileShader(fragmentShader) <span class="hljs-comment">// 编译着色器代码</span>

<span class="hljs-keyword">const</span> program = gl.createProgram() <span class="hljs-comment">// 创建一个程序</span>
gl.attachShader(program, vertexShader) <span class="hljs-comment">// 添加顶点着色器</span>
gl.attachShader(program, fragmentShader) <span class="hljs-comment">// 添加片元着色器</span>
gl.linkProgram(program) <span class="hljs-comment">// 连接 program 中的着色器</span>

gl.useProgram(program) <span class="hljs-comment">// 告诉 webgl 用这个 program 进行渲染</span>

<span class="hljs-keyword">const</span> colorLocation = gl.getUniformLocation(program, <span class="hljs-string">'u_color'</span>) 
<span class="hljs-comment">// 获取 u_color 变量位置</span>
gl.uniform4f(colorLocation, <span class="hljs-number">0.93</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.56</span>, <span class="hljs-number">1</span>) <span class="hljs-comment">// 设置它的值</span>

<span class="hljs-keyword">const</span> positionLocation = gl.getAttribLocation(program, <span class="hljs-string">'a_position'</span>) 
<span class="hljs-comment">// 获取 a_position 位置</span>
<span class="hljs-keyword">const</span> positionBuffer = gl.createBuffer() 
<span class="hljs-comment">// 创建一个顶点缓冲对象，返回其 ID，用来放三角形顶点数据，</span>
gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer) 
<span class="hljs-comment">// 将这个顶点缓冲对象绑定到 gl.ARRAY_BUFFER</span>
<span class="hljs-comment">// 后续对 gl.ARRAY_BUFFER 的操作都会映射到这个缓存</span>
gl.bufferData(gl.ARRAY_BUFFER, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>([
    <span class="hljs-number">0</span>, <span class="hljs-number">0.5</span>,
    <span class="hljs-number">0.5</span>, <span class="hljs-number">0</span>,
    -<span class="hljs-number">0.5</span>, -<span class="hljs-number">0.5</span>
]),  <span class="hljs-comment">// 三角形的三个顶点</span>
     <span class="hljs-comment">// 因为会将数据发送到 GPU，为了省去数据解析，这里使用 Float32Array 直接传送数据</span>
gl.STATIC_DRAW <span class="hljs-comment">// 表示缓冲区的内容不会经常更改</span>
)
<span class="hljs-comment">// 将顶点数据加入的刚刚创建的缓存对象</span>

gl.vertexAttribPointer( <span class="hljs-comment">// 告诉 OpenGL 如何从 Buffer 中获取数据</span>
    positionLocation, <span class="hljs-comment">// 顶点属性的索引</span>
    <span class="hljs-number">2</span>, <span class="hljs-comment">// 组成数量，必须是1，2，3或4。我们只提供了 x 和 y</span>
    gl.FLOAT, <span class="hljs-comment">// 每个元素的数据类型</span>
    <span class="hljs-literal">false</span>, <span class="hljs-comment">// 是否归一化到特定的范围，对 FLOAT 类型数据设置无效</span>
    <span class="hljs-number">0</span>, <span class="hljs-comment">// stride 步长 数组中一行长度，0 表示数据是紧密的没有空隙，让OpenGL决定具体步长</span>
    <span class="hljs-number">0</span> <span class="hljs-comment">// offset 字节偏移量，必须是类型的字节长度的倍数。</span>
)
gl.enableVertexAttribArray(positionLocation);
<span class="hljs-comment">// 开启 attribute 变量额，使顶点着色器能够访问缓冲区数据</span>

gl.clearColor(<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>) <span class="hljs-comment">// 设置清空颜色缓冲时的颜色值</span>
gl.clear(gl.COLOR_BUFFER_BIT) <span class="hljs-comment">// 清空颜色缓冲区，也就是清空画布</span>

gl.drawArrays( <span class="hljs-comment">// 从数组中绘制图元</span>
    gl.TRIANGLES, <span class="hljs-comment">// 画三角形</span>
    <span class="hljs-number">0</span>,  <span class="hljs-comment">// 从哪个点开始画</span>
    <span class="hljs-number">3</span> <span class="hljs-comment">// 需要用到多少个点</span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57a2d9a6992d4052bbcf98105c694aa4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>用 WebGL 画了个三角形，代码多的确实有点夸张。下面来一点点解释上面这一坨代码到底怎么画出这个三角形的。</p>
<h3 data-id="heading-10">顶点和片元着色器</h3>
<p>上面代码的注释基本解释了各个步骤是干啥的，不过一些概念还需要详细介绍下。</p>
<p>WebGL 的重点是顶点和片元着色器，也就是上面 <code>gl.shaderSource</code> 第二个参数。</p>
<p>OpenGL 的着色器使用 <strong>GLSL(OpenGL Shading Language)</strong> 语言进行编写，它有点像 C 语言。</p>
<p>顶点着色器主要是用来确定顶点的位置的，告诉 OpenGL 这个顶点在 NDC(标准化设备坐标) 中的坐标，也就是设置 <code>gl_Position</code>（内置变量） 变量。</p>
<p>片元作色器也叫片段着色器，大家可以理解为像素着色器，一个片元就当成一个像素。片元作色器主要是用来确认这个像素的颜色的，也就是设置给 <code>gl_FragColor</code>（内置变量） 变量。</p>
<p>我们使用 OpenGL 的目的是在屏幕上渲染一张图片。图片是由一个个像素组成的，首先我们定义了一堆顶点给 OpenGL，然后 OpenGL 把每个顶点都传给顶点坐标系，顶点坐标系返回顶点在 NDC 中的位置，然后 OpenGL 将这些坐标进行图形装配（上面我们设置装配成三角形）。然后将图形变成一个个片元（像素），这一步叫做光栅化。然后将这些片元传递给片元着色器，然后片元着色器用来输出这个像素的颜色。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> vertex = [[<span class="hljs-number">50</span>, <span class="hljs-number">0</span>], [<span class="hljs-number">0</span>, <span class="hljs-number">50</span>], [-<span class="hljs-number">50</span>, -<span class="hljs-number">50</span>]] <span class="hljs-comment">// 定义顶点</span>
vertex = vertex.map(<span class="hljs-function"><span class="hljs-params">v</span> =></span> vertexShader(v)) <span class="hljs-comment">// 然会 NDC 中的顶点位置（-1 到 +1）</span>
<span class="hljs-keyword">const</span> fragment = rasterization(vertex) <span class="hljs-comment">// 将这些顶点组成的图形变成一个个片元</span>
<span class="hljs-keyword">const</span> colors = fragment.map(<span class="hljs-function"><span class="hljs-params">f</span> =></span> fragmentShader(f)) <span class="hljs-comment">// 将这些片元给片元着色器，确定它的颜色</span>
colors.forEach(<span class="hljs-function"><span class="hljs-params">color</span> =></span> writePixelToScreen(color)) <span class="hljs-comment">// 然后渲染到屏幕</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面是简单描述这个过程的伪 js 代码。</p>
<p><img alt="又从网上偷了张图" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70006aedc062444ea6f1430eeac23af9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上面图片很好的展示了这个过程，可以忽略几何着色器，WebGL 中只有顶点和片元着色器。</p>
<p>我们从这幅图也可以看出来，片元着色器调用的测试比顶点着色器多得多。所以一些计算能放到顶点着色器就放入到顶点着色器。</p>
<h3 data-id="heading-11">向着色器传递数据</h3>
<p>着色器是使用 GLSL 写的，那么我们如何在 JS 将数据传入到着色器中呢？</p>
<p>上面 GLSL 代码中有如下两个变量，这代表是从外部传进来的。</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-comment">// vertex</span>
<span class="hljs-keyword">attribute</span> <span class="hljs-type">vec4</span> a_position;
<span class="hljs-comment">// frag</span>
<span class="hljs-keyword">uniform</span> <span class="hljs-type">vec4</span> u_color;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两个变量的类型都是 <code>vec4</code>，可以理解为有 4 个浮点数的数组或 4 个自由度的矢量。大家可以先忽略为什么顶点是 <code>vec4</code> 而不是 <code>vec3</code>。</p>
<p>能够从外部传入数据，关键就在 <code>attribute</code> 和 <code>uniform</code> 存储限定字，这两种类型的变量必须要定义在函数外部，并且它们都不能在着色器中被重新赋值。</p>
<h4 data-id="heading-12">uniform</h4>
<p>我们先来看 <code>uniform</code>。它可以在顶点和片元着色器中使用，它是全局的，在着色器程序中是独一无二的。它有点像 <code>window.u_color</code>，我们在<strong>外部JS</strong>给它赋值，在顶点和片元着色器中都可以使用，我们也可以在<strong>外部JS</strong>修改它的值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> colorLocation = gl.getUniformLocation(program, <span class="hljs-string">'u_color'</span>)
gl.uniform4f(colorLocation, <span class="hljs-number">0.93</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.56</span>, <span class="hljs-number">1</span>)
<span class="hljs-comment">// 类似于 program.window.u_color = [0.93, 0.0, 0.56, 1.0];</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们首先获取 <code>u_color</code> 在着色器中的位置，然后使用 <code>uniform4f</code> 传递数据，<code>4f</code> 代表是 4 个浮点数，也就是 <code>rgba</code>，需要注意 OpenGL 中颜色值的范围不是 0 到 255，而是 0 到 1。</p>
<h4 data-id="heading-13">attribute</h4>
<p><code>attribute</code> 只能用在顶点着色器，被用来表示逐顶点信息，上面例子中，我们定义了三个顶点传递给 <code>a_position</code> 变量，顶点着色器不是一次性获取到这些顶点，而是一个个的获取。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> points = [p1, p2, p3]
points.forEach(<span class="hljs-function"><span class="hljs-params">p</span> =></span> vertexShader(p))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类似上面这种执行顶点着色器，当然在显卡中会并发的执行顶点着色器。我们使用 JS 传递 <code>attribute</code> 比较麻烦一点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> positionLocation = gl.getAttribLocation(program, <span class="hljs-string">'a_position'</span>) 
<span class="hljs-keyword">const</span> positionBuffer = gl.createBuffer() 
gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer) 
gl.bufferData(gl.ARRAY_BUFFER, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>([
    <span class="hljs-number">0</span>, <span class="hljs-number">0.5</span>,
    <span class="hljs-number">0.5</span>, <span class="hljs-number">0</span>,
    -<span class="hljs-number">0.5</span>, -<span class="hljs-number">0.5</span>
]), gl.STATIC_DRAW)
gl.vertexAttribPointer(positionLocation, <span class="hljs-number">2</span>, gl.FLOAT, <span class="hljs-literal">false</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
gl.enableVertexAttribArray(positionLocation);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和 <code>uniform</code> 一样我们首先获取变量的地址，然后创建一个顶点缓冲来存储顶点数据，顶点缓冲对象的缓冲类型是 <code>gl.ARRAY_BUFFER</code>，需要将 buffer 绑定到 <code>gl.ARRAY_BUFFER</code>，后续对 <code>gl.ARRAY_BUFFER</code> 操作就相当于对这个 buffer 进行操作。然后我们使用 <code>bufferData</code> 方法将数据存入缓存中，加入缓存区后，我们还需要使用 <code>vertexAttribPointer</code> 告诉 OpenGL 如何获取数据，最后使用 <code>enableVertexAttribArray</code> 启用顶点属性就行了。</p>
<h3 data-id="heading-14">代码解析</h3>
<p>了解了顶点和片元着色器，基本上上面的代码就理解的差不多了，现在让我们再过一边上面的代码。</p>
<p>要使用 WebGL 渲染，首先需要获取渲染上下文，这里只需要将平时用的 <code>2d</code> 参数改为 <code>webgl</code> 就行，然后设置 WebGL viewport，这样 OpenGL 就可以根据它将 NDC 坐标变成屏幕上的坐标。</p>
<p>接着我们创建了顶点和片元着色器，然后编译着色器代码。创建一个着色器程序，将顶点和片元着色器加入到这个着色器程序并连接着色器，然后告诉 webgl 使用这个着色器程序。</p>
<p>接着就是上面说过的向着色器中传递数据，接下来我们设置了 WebGL 的默认颜色缓冲区颜色值，然后清空颜色缓冲区，也就是使用我们设置的颜色清除画布。</p>
<p>最后一步我们使用 <code>gl.drawArrays</code> 开始渲染了，我们选择渲染三角形，当然还可以把类型变成线段，最后就是三条线的三角形，而不是填充的三角形，我们有顶点缓冲区中有三个顶点，所以这里设置了渲染 3 次。</p>
<p>OpenGL 本身就是一个状态机，我们使用 API 设置它的状态，来告诉它如何运行，OpenGL 的状态通常被称为 OpenGL 上下文。</p>
<h2 data-id="heading-15">GLSL ES 入门</h2>
<p>可能大家对 GLSL 比较陌生，下面将详细介绍下这个 OpenGL 着色器语言。在 OpenGL ES 和 WebGL 中使用的是 GLSL ES，可能大家已经猜到了，WebGL 中使用是基于 GLSL 1.2 也是 GLSL ES 2.0 版本，WebGL2 中使用的是基于 3.30 的版本，也是 GLSL ES 的 3.0 版本。</p>
<p>它是强类型语言，每一句都需要有分号。它注释语法和 JS 一样，变量名规则也和 JS 一样，不能使用关键字，保留字，不能以 <code>gl_</code>、<code>webgl_</code> 或 <code>_webgl_</code> 开头。</p>
<p>GLSL 中主要有三种数据值类型，浮点数、整数和布尔。注意浮点数必须要带小数点。类型转换可以直接使用 <code>float</code>、<code>int</code> 和 <code>bool</code> 函数。</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-type">float</span> f = <span class="hljs-type">float</span>(<span class="hljs-number">1</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它的运算符基本也和 JS 一样，<code>++</code> <code>--</code> <code>+=</code> <code>&&</code> <code>||</code> 还有三元运算符都支持。</p>
<h3 data-id="heading-16">矩阵和矢量</h3>
<p>因为是用来画图的，所以对矩阵和矢量也有支持。</p>
<p><code>vec2</code>、<code>vec3</code> 和 <code>vec3</code> 代表 2、3 和 4 个浮点数的矢量。</p>
<p><code>ivec2</code>、<code>ivec3</code> 和 <code>ivec3</code> 整数版本。</p>
<p><code>bvec2</code>、<code>bvec3</code> 和 <code>bvec3</code> 布尔版本。</p>
<p><code>mat2</code>、<code>mat3</code> 和 <code>mat4</code> 2x2、3x3 和 4x4 的矩阵。</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-type">vec3</span> color = <span class="hljs-type">vec3</span>(<span class="hljs-number">1.</span>, <span class="hljs-number">1.</span>, <span class="hljs-number">1.</span>); <span class="hljs-comment">// 白色</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>GLSL 对矢量的赋值、获取和构造也十分强大。</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-type">vec4</span> v4 = <span class="hljs-type">vec4</span>(<span class="hljs-number">1.</span>,<span class="hljs-number">2.</span>,<span class="hljs-number">3.</span>,<span class="hljs-number">4.</span>);
<span class="hljs-type">vec3</span> color = v4.rgb; <span class="hljs-comment">// 可是用 rgba 获取，相当于 vec3(1., 2., 3.)</span>
<span class="hljs-type">vec3</span> position = v4.xyz; <span class="hljs-comment">// 也可以用 xyzw 获取</span>
<span class="hljs-type">vec3</span> <span class="hljs-built_in">texture</span> = v4.stp; <span class="hljs-comment">// 也可以使用 stpq 获取</span>

<span class="hljs-type">vec2</span> v2 = <span class="hljs-type">vec2</span>(v4); <span class="hljs-comment">// 使用 v4 的前两个元素构造</span>
<span class="hljs-type">vec4</span> v41 = <span class="hljs-type">vec4</span>(v2, v4.yw); <span class="hljs-comment">// 使用 v2 和 v4 的后两个元素构造</span>
<span class="hljs-type">vec4</span> v42 = <span class="hljs-type">vec4</span>(<span class="hljs-number">1.</span>); <span class="hljs-comment">// 4 个元素都设成 1.</span>
v42.g = <span class="hljs-number">2.</span>;
v42[<span class="hljs-number">1</span>] = <span class="hljs-number">3.</span>; <span class="hljs-comment">// 也可以使用 [] 获取</span>

<span class="hljs-type">mat2</span> m2 = <span class="hljs-type">mat2</span>(<span class="hljs-number">1.</span>, <span class="hljs-number">2.</span>, <span class="hljs-number">3.</span>, <span class="hljs-number">4.</span>);
<span class="hljs-type">vec2</span> v21 = m2[<span class="hljs-number">0</span>]; <span class="hljs-comment">// [1., 2.]</span>
<span class="hljs-type">float</span> f = v21[<span class="hljs-number">0</span>].x <span class="hljs-comment">// 混合使用都行</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">分支和循环</h3>
<p>分支和循环也和 JS 一样。</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-keyword">if</span> (<span class="hljs-literal">true</span>) &#123;&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-literal">true</span>) &#123;&#125; <span class="hljs-keyword">else</span> &#123;&#125;
<span class="hljs-keyword">for</span> (<span class="hljs-type">int</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3</span>; i++) &#123;
<span class="hljs-keyword">continue</span>; <span class="hljs-comment">// 或 break</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">函数</h3>
<p>每个着色器中都必须有个 <code>main</code> 函数，它会被自动执行，函数的返回值写在函数名前，没返回值就为 <code>void</code>。</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-type">float</span> add(<span class="hljs-type">float</span> a, <span class="hljs-type">float</span> b) &#123;
<span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果函数定义在调用之后则需要先声明该函数。</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-type">float</span> add(<span class="hljs-type">float</span> a, <span class="hljs-type">float</span> b); <span class="hljs-comment">// 声明</span>
<span class="hljs-type">void</span> main() &#123;
<span class="hljs-type">float</span> c = add(<span class="hljs-number">1.</span>, <span class="hljs-number">1.</span>);
&#125;
<span class="hljs-type">float</span> add(<span class="hljs-type">float</span> a, <span class="hljs-type">float</span> b) &#123;
<span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外函数参数还有限定词。</p>
<p><code>in</code> 默认，表示像函数传入参数。</p>
<p><code>const in</code> 和 <code>in</code> 一样，但是不能修改。</p>
<p><code>out</code> 在函数中被赋值，并被传出。</p>
<p><code>inout</code> 传入参数，在函数中被赋值，并被传出。</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-type">void</span> add(<span class="hljs-keyword">in</span> <span class="hljs-type">float</span> a, <span class="hljs-keyword">in</span> <span class="hljs-type">float</span> b, <span class="hljs-keyword">out</span> <span class="hljs-type">float</span> answer) &#123;
answer = a + b; <span class="hljs-comment">// 不使用 return 而用 out</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>GLSL 中还有一些内置函数，例如 <code>sin</code>, <code>cos</code>, <code>pow</code>, <code>abs</code> 等等。</p>
<h3 data-id="heading-19">精度限定字</h3>
<p>精度限定字用来控制数值的精度，越高的精度也就意味着更慢的性能，所以我们要合理的控制程序的精度。GLSL 中分为三种精度 <code>highp</code>、<code>mediump</code> 和 <code>lowp</code>，分别是高、中和低精度。</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-keyword">mediump</span> <span class="hljs-type">float</span> size; <span class="hljs-comment">// 声明一个中精度浮点数</span>
<span class="hljs-keyword">highp</span> <span class="hljs-type">int</span> len; <span class="hljs-comment">// 声明一个高精度整数</span>
<span class="hljs-keyword">lowp</span> <span class="hljs-type">vec4</span> v; <span class="hljs-comment">// 低精度矢量</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一个一个变量的声明，非常麻烦，我们还可以一次性声明这些精度。</p>
<pre><code class="hljs language-glsl copyable" lang="glsl"><span class="hljs-keyword">precision</span> <span class="hljs-keyword">mediump</span> <span class="hljs-type">float</span>; <span class="hljs-comment">// 浮点数全部使用中精度</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>GLSL 已经帮我们设置了默认变量精度。</p>
<p>在顶点着色器中 <code>int</code> 和 <code>float</code> 都是 <code>highp</code>。</p>
<p>在片元着色器中 <code>int</code> 是 <code>mediump</code>，<code>float</code> 没有定义。</p>
<p>这也就是为什么上面片元着色器中第一行代码是 <code>precision mediump float;</code> 了，因为 OpenGL 没有设置默认值，所以必须得我们自己设置。</p>
<p><em>另外在顶点和片元着色器 <code>sampler2D</code> 和 <code>samplerCube</code> 都是 <code>lowp</code>（它们主要用来渲染图片，后面会详细讲解）。</em></p>
<p>更多关于 GLSL 内容，可以查看 <a href="http://www.khronos.org/opengles/sdk/docs/man/" target="_blank" rel="nofollow noopener noreferrer">OpenGL ES Reference Pages</a>。</p>
<h2 data-id="heading-20">立方体</h2>
<p>我们现在来研究下如何渲染一个立方体吧。如前所述，WebGL 是很底层的 API，它只能用来画点、线和三角形，那么我们如何来画正方形呢？</p>
<p>其实大家看到的那些精美的 3D 模型，其实都是一个个非常小的三角形组成的。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb7400fb7f31480cb52caf2b7284d1c1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>比如这个冰箱就是由 3 万多个三角形组成。为什么选择三角形呢？这是因为任何多边形都可以最终分解为多个三角形，也就是说三角形是多边形的基本单位，并且三角形一定在一个平面上。</p>
<p>可以使用两个三角形组合来表示一个正方形，立方体有 6 个面，也就需要 12 个三角形，每个三角形需要 3 个顶点，那么最终我们就需要 36 个顶点！</p>
<p>但是立方体比较特殊，它其实只有 8 个顶点，一个顶点被三个面共用。那么有什么方法让我们只用定义 8 个顶点呢？OpenGL 还可以通过我们定义的顶点索引来渲染三角形，比如我们发送 8 个顶点和一个顶点索引数组到 GPU，然后 OpenGL 就可以使用索引数组的顺序来渲染三角形了。</p>
<p>比如索引数组 <code>[1,2,3,3,2,0]</code> 并且我们是画三角形的话，这就表示使用顶点数组下标为 <code>1</code>、<code>2</code> 和 <code>3</code> 的顶点来渲染一个三角形，然后用 <code>3</code>、<code>2</code> 和 <code>0</code> 下标渲染另一个三角形。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>)
canvas.width = canvas.height = <span class="hljs-number">300</span>
<span class="hljs-built_in">document</span>.body.appendChild(canvas)
<span class="hljs-keyword">const</span> gl = canvas.getContext(<span class="hljs-string">'webgl'</span>)
gl.viewport(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, gl.canvas.width, gl.canvas.height)

<span class="hljs-keyword">const</span> program = createProgramFromSource(gl, <span class="hljs-string">`
attribute vec4 aPos;
attribute vec4 aColor;
varying vec4 vColor;

void main() &#123;
  gl_Position = aPos;
  vColor = aColor;
&#125;
`</span>, <span class="hljs-string">`
precision mediump float;
varying vec4 vColor;

void main() &#123;
  gl_FragColor = vColor;
&#125;
`</span>)

<span class="hljs-keyword">const</span> points = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>([
  -<span class="hljs-number">0.5</span>,<span class="hljs-number">0.5</span>,-<span class="hljs-number">0.5</span>, <span class="hljs-number">0.5</span>,<span class="hljs-number">0.5</span>,-<span class="hljs-number">0.5</span>, <span class="hljs-number">0.5</span>,-<span class="hljs-number">0.5</span>,-<span class="hljs-number">0.5</span>, -<span class="hljs-number">0.5</span>,-<span class="hljs-number">0.5</span>,-<span class="hljs-number">0.5</span>,
  <span class="hljs-number">0.5</span>,<span class="hljs-number">0.5</span>,<span class="hljs-number">0.5</span>, -<span class="hljs-number">0.5</span>,<span class="hljs-number">0.5</span>,<span class="hljs-number">0.5</span>, -<span class="hljs-number">0.5</span>,-<span class="hljs-number">0.5</span>,<span class="hljs-number">0.5</span>, <span class="hljs-number">0.5</span>,-<span class="hljs-number">0.5</span>,<span class="hljs-number">0.5</span>
])
<span class="hljs-keyword">const</span> colors = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>([
  <span class="hljs-number">1</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>, <span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">0</span>, <span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">1</span>, <span class="hljs-number">1</span>,<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,
  <span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>, <span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>, <span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>, <span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>
])
<span class="hljs-keyword">const</span> indices = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>([
  <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">0</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-comment">// 前</span>
  <span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">7</span>, <span class="hljs-number">2</span>, <span class="hljs-comment">// 右</span>
  <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">4</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-comment">// 后</span>
  <span class="hljs-number">5</span>, <span class="hljs-number">3</span>, <span class="hljs-number">6</span>, <span class="hljs-number">5</span>, <span class="hljs-number">0</span>, <span class="hljs-number">3</span>, <span class="hljs-comment">// 左</span>
  <span class="hljs-number">0</span>, <span class="hljs-number">5</span>, <span class="hljs-number">4</span>, <span class="hljs-number">0</span>, <span class="hljs-number">4</span>, <span class="hljs-number">1</span>, <span class="hljs-comment">// 上</span>
  <span class="hljs-number">7</span>, <span class="hljs-number">6</span>, <span class="hljs-number">3</span>, <span class="hljs-number">7</span>, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>  <span class="hljs-comment">// 下</span>
])

<span class="hljs-keyword">const</span> [posLoc, posBuffer] = createAttrBuffer(gl, program, <span class="hljs-string">'aPos'</span>, points)
<span class="hljs-keyword">const</span> [colorLoc, colorBuffer] = createAttrBuffer(gl, program, <span class="hljs-string">'aColor'</span>, colors)
<span class="hljs-keyword">const</span> indexBuffer = gl.createBuffer()
gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer)
gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, gl.STATIC_DRAW)

gl.bindBuffer(gl.ARRAY_BUFFER, posBuffer)
gl.vertexAttribPointer(posLoc, <span class="hljs-number">3</span>, gl.FLOAT, <span class="hljs-literal">false</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
gl.enableVertexAttribArray(posLoc)

gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer)
gl.vertexAttribPointer(colorLoc, <span class="hljs-number">3</span>, gl.FLOAT, <span class="hljs-literal">false</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
gl.enableVertexAttribArray(colorLoc)

gl.enable(gl.DEPTH_TEST)
gl.clearColor(<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">1</span>)
gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT)

gl.drawElements(
  gl.TRIANGLES, <span class="hljs-comment">// 要渲染的图元类型</span>
  indices.length, <span class="hljs-comment">// 要渲染的元素数量</span>
  gl.UNSIGNED_BYTE, <span class="hljs-comment">// 元素数组缓冲区中的值的类型</span>
  <span class="hljs-number">0</span> <span class="hljs-comment">// 元素数组缓冲区中的偏移量, 字节单位</span>
)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createShader</span>(<span class="hljs-params">gl, type, source</span>) </span>&#123;
  <span class="hljs-keyword">const</span> shader = gl.createShader(type)
  gl.shaderSource(shader, source)
  gl.compileShader(shader)
  <span class="hljs-keyword">return</span> shader;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createProgramFromSource</span>(<span class="hljs-params">gl, vertex, fragment</span>) </span>&#123;
  <span class="hljs-keyword">const</span> vertexShader = createShader(gl, gl.VERTEX_SHADER,vertex)
  <span class="hljs-keyword">const</span> fragmentShader = createShader(gl, gl.FRAGMENT_SHADER, fragment)
  <span class="hljs-keyword">const</span> program = gl.createProgram()
  gl.attachShader(program, vertexShader)
  gl.attachShader(program, fragmentShader)
  gl.linkProgram(program)
  gl.useProgram(program)
  <span class="hljs-keyword">return</span> program
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createAttrBuffer</span>(<span class="hljs-params">gl, program, attr, data</span>) </span>&#123;
  <span class="hljs-keyword">const</span> location = gl.getAttribLocation(program, attr)
  <span class="hljs-keyword">const</span> buffer = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buffer)
  gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW)
  <span class="hljs-keyword">return</span> [location, buffer]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码画了一个边长是 <code>1</code> 的立方体，立方体的正中心就在坐标轴原点。</p>
<p>我们除了定义每个顶点的坐标，还定义了每个顶点的颜色，靠近屏幕外的 4 个顶点设置成彩色，后 4 个顶点设置成黑色。</p>
<p>然后使用 <code>Uint8Array</code> 定义了顶点索引（如果又索引值大于 256 就应该使用 <code>Uint16Array</code>）。</p>
<p>颜色数据和坐标一样，创建一个缓存然后，告诉 WebGL 如何获取获取。但是顶点索引数据有一点点不同，它的绑定点不是 <code>gl.ARRAY_BUFFER</code> 而是 <code>gl.ELEMENT_ARRAY_BUFFER</code> 它是用于元素索引的 Buffer。</p>
<p>这里还开启了深度测试，这样后画的三角形就不会覆盖先画的，而是根据它们的 Z 值判断。另外清理的时候不用调用两次 <code>clear</code> 函数，而是使用 <code>|</code> 运算符，<code>gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT</code>。</p>
<p>最后一步将 <code>drawArrays</code> 换成 <code>drawElements</code>，表示我们用索引来渲染图形。</p>
<h3 data-id="heading-21">存储限定字 varying</h3>
<p>存储限定字其实一共有三个 <code>attribute</code>、<code>uniform</code> 和 <code>varying</code>。上面已经介绍了前两个，它们都是从外部 JS 获取数据。</p>
<p><code>varying</code> 是顶点着色器向片元着色器传送数据。上面例子中我们将 <code>aColor</code> 赋值给 <code>vColor</code>，然后在片元着色器中就可以使用 <code>vColor</code> 了。</p>
<p>叫 <code>varying</code> 也是有原因的，我们可以先来看看上面代码最终渲染成什么样子。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3d0d16d43a64872952442cf68d864ce~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们设置前面 4 个顶点颜色分别是红、绿、蓝和粉色，怎么渲染出来的是一种渐变色？</p>
<p>前面将过，片段着色器执行的次数一般比顶点着色器执行次数多得多。这是因为在片元着色器之前会执行光栅化，会将图元离散化，变成一个个像素，然后每个像素都会执行片元着色器，来确定这个像素的颜色。</p>
<p><code>varying</code> 变量从顶点着色器向片元着色器传递时会被 OpenGL 插值，也就是我们定义了三角形 3 个顶点的颜色，三角形内部的像素都是根据这 3 个顶点颜色插值出来的。比如一个线段一个端点是红色，另一个是绿色，那么这个线段中间就是 50% 的红色和 50% 的绿色。</p>
<h3 data-id="heading-22">旋转和透视</h3>
<p>我们渲染的是一个立方体，为什么显示出来确实一个正方形？</p>
<p>因为这个立方体的正面正对着我们，我们就只能看见它的正面，如果我们将这个立方体稍微旋转一下，就可以看出来这个是立方体了。</p>
<p>现实生活中，我们看物体会有近大远小的效果，也就是有透视效果。在 3D 图形中也应该也有类似的效果，现在我们渲染的这个立方体是没有透视效果的，也就是前面那个面会和后面那个面一样大。</p>
<p>如何让图形旋转，让它看起来有透视效果需要将在下篇文章中介绍。</p>
<h2 data-id="heading-23">总结</h2>
<p>这篇文章讲了 WebGL 基础知识和一些重要概念。WebGL 的 X、Y 和 Z 轴坐标范围是 -1 到 +1，任何超出这个范围的顶点都会被裁切，这个坐标我们称为<strong>标准化设备坐标(NDC)</strong>。WebGL 默认是左手坐标系，但是我们也可以将它变成右手坐标系。一般我们会选择一个坐标系就不会再改变，WebGL 的惯例是右手坐标系。渲染图形时先对每个顶点执行顶点着色器，然后再进行光栅化，其中 <code>varying</code> 变量会被插值，然后执行片元着色器，返回各个像素的颜色。最后我们渲染一个立方体看起来像个正方形，因为我们看的是它的正对面，我们需要旋转它才能看见其他的面，WebGL 中并没有 API 让我们调用一下，立方体就旋转了，我们需要用数学公式来旋转，通常是使用旋转矩阵来完成，下篇文章将详细旋转、缩放等变换。</p>
<h2 data-id="heading-24">参考</h2>
<ul>
<li>《WebGL 编程指南》</li>
<li><a href="https://webglfundamentals.org/" target="_blank" rel="nofollow noopener noreferrer">webglfundamentals.org/</a></li>
<li><a href="https://learnopengl-cn.github.io/" target="_blank" rel="nofollow noopener noreferrer">learnopengl-cn.github.io/</a></li>
<li><a href="https://zh.wikipedia.org/wiki/OpenGL" target="_blank" rel="nofollow noopener noreferrer">zh.wikipedia.org/wiki/OpenGL</a></li>
<li><a href="https://zh.wikipedia.org/wiki/WebGL" target="_blank" rel="nofollow noopener noreferrer">zh.wikipedia.org/wiki/WebGL</a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/WebGL_API" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></li>
<li><a href="https://www.khronos.org/registry/webgl/specs/1.0/" target="_blank" rel="nofollow noopener noreferrer">www.khronos.org/registry/we…</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            