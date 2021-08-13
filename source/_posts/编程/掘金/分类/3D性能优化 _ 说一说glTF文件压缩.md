
---
title: '3D性能优化 _ 说一说glTF文件压缩'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e89e03c05a24466b8126c6cec252344~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 02:14:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e89e03c05a24466b8126c6cec252344~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">引言</h1>
<p>最近做T级互动，需要使用到3D模型。相信大家和我一样，在开始着手的时候，一定会有这么些问题：</p>
<ul>
<li>1.如何选择3D模型的导出格式</li>
<li>2.如何对模型文件进行优化</li>
<li>3.在大流量的项目中兼容性怎么样</li>
</ul>
<p>让我们通过这篇文章，进行细致的探索、调研与沉淀。</p>
<br>
<h1 data-id="heading-1">一、什么是 glTF 文件</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF-Tutorials%2Fblob%2Fmaster%2FgltfTutorial%2FgltfTutorial_002_BasicGltfStructure.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_002_BasicGltfStructure.md" ref="nofollow noopener noreferrer">glTF</a> 全称 <code>Graphics Language Transmission Format</code>，是三维场景和模型的标准文件格式。</p>
<p>glTF 核心是 JSON 文件，描述了 3D 场景的整个内容。它由场景结构本身的描述组成，其由定义场景图的节点的层次提供。</p>
<p>场景中出现的 3D 对象是使用连接到节点的 meshes(网格)定义的。Materials(材料)定义对象的外观。Animations(动画)描述 3D 对象如何随着时间的推移转换 3D 对象，并且 Skins(蒙皮)定义了对物体的几何形状的方式基于骨架姿势变形。Cameras(相机)描述了渲染器的视图配置。</p>
<p>除此以外，它还包括了带有二进制数据和图像文件的链接，如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e89e03c05a24466b8126c6cec252344~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<h1 data-id="heading-2">二、.gltf 与.glb</h1>
<p>从 blender 文件导出中可以看出：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91dced1c665d4e0ab5adba3d2f294838~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>glTF 文件有两种拓展形式，.gltf（JSON / ASCII）或.glb（二进制）。.gltf 文件可能是自包含的，也可能引用外部二进制和纹理资源，而 .glb 文件则是完全自包含的（但使用外部工具可以将其缓冲区/纹理保存为嵌入或单独的文件，后面会提到）。</p>
<h2 data-id="heading-3">2.1 .glb文件产生原因</h2>
<p>glTF 提供了两个也可以一起使用的交付选项：</p>
<ul>
<li>glTF JSON 指向外部二进制数据（几何、关键帧、皮肤）和图像。</li>
<li>glTF JSON 嵌入 base64 编码的二进制数据，并使用数据 URI 内联图像。</li>
</ul>
<p>对于这些资源，由于 base64 编码，glTF 需要单独的请求或额外的空间。Base64 编码需要额外的处理来解码并增加文件大小（编码资源增加约 33%）。虽然 gzip 减轻了文件大小的增加，但解压缩和解码仍然会增加大量的加载时间。</p>
<p>为了解决这个问题，引入了一种容器格式 Binary glTF。在二进制 glTF 中，glTF 资产（JSON、.bin 和图像）可以存储在二进制 blob 中，就是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF%2Fblob%2Fmaster%2Fspecification%2F2.0%2FREADME.md%23glb-file-format-specification" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF/blob/master/specification/2.0/README.md#glb-file-format-specification" ref="nofollow noopener noreferrer">.glb 文件</a>。</p>
<h2 data-id="heading-4">2.2 文件对比</h2>
<h3 data-id="heading-5">2.2.1 同一个glTF文件，.glb格式要比.gltf小</h3>
<ul>
<li>自包含的：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fddb964fb62e479b8c7b90505027bab2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>引用外部二进制和纹理资源的：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67f2eb7571df4802951b6ff4bc2dc0fc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">2.2.2 .gltf文件预览：</h3>
<ul>
<li>自包含的：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4e1429fc67140f5bbe232d68731d8b2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>引用外部二进制和纹理资源：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11bdddb15e544011a8ab9ca4718352bd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">2.2.3 glb文件预览：</h3>
<ul>
<li>自包含的：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/add031cb379c40d0913569a2c2e65025~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>引用外部二进制和纹理资源：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a6c2a43fa8f4c31ac0b7b7ebb45e402~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中可以看到，当非自包含型的时候，请求glTF文件时，会一同请求图片文件。</p>
<p>那么，我们就可以利用这个特性，就可以实现一些性能优化，让我们往下继续。</p>
<br>
<h1 data-id="heading-8">三、glTF 文件拆分</h1>
<p>上文提到，glTF文件可以拆分为.gltf/.glb文件+二进制文件+纹理图片，那么，我们就可以<strong>将其拆分出来，并对纹理图片进行单独的压缩</strong>，来进行性能的优化。</p>
<p>可以使用<code>gltf pipeLine</code> ，其具有以下功能：</p>
<ul>
<li>glTF 与 glb 的相互转换</li>
<li>将缓冲区/纹理保存为嵌入或单独的文件</li>
<li>将 glTF 1.0 模型转换为 glTF 2.0(使用<code>KHR_techniques_webgl</code>和<code>KHR_blend</code>)</li>
<li>使用 Draco 进行网格压缩</li>
</ul>
<p>在这里，我们是要使用“将缓冲区/纹理保存为嵌入或单独的文件”这个功能。</p>
<p>让我们来看看拆分出来的文件
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7536bb2480645f999024a18f7b6d624~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>再回顾一下，.glb文件是这么引入外部单独的纹理与二进制文件的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c92699a7d3264922bea7bdf9fbac537c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，只要将拆分出来的这几个文件，<strong>放入同一个路径中</strong>，然后像之前那样引入就好了。</p>
<ul>
<li>压缩方式</li>
</ul>
<pre><code class="copyable">gltf-pipeline -i male.glb -o male-processed.glb -s
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用方式（在 Three.js 中）</li>
</ul>
<p>普普通通地用就好了，和不拆分的没什么区别</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; GLTFLoader &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three/examples/jsm/loaders/GLTFLoader'</span>

<span class="hljs-keyword">const</span> loader = <span class="hljs-keyword">new</span> GLTFLoader()
loader.load(MODEL_FILE_PATH, <span class="hljs-function">(<span class="hljs-params">gltf</span>) =></span> &#123;
 <span class="hljs-comment">// ....</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>性能对比</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c6ebf86018b4702a94a0e6aaf4feea6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<h1 data-id="heading-9">四、glTF 文件压缩</h1>
<p>如上面介绍，glTF 文件包括.gltf/.glb 文件、.bin 文件以及纹理资源。glTF2.0 相关的插件主要有以下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03daf73190e049469aece78167d21ae5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么我们从中取一些来分析一下。</p>
<br>
<h2 data-id="heading-10">4.1 网格压缩</h2>
<h3 data-id="heading-11">4.1.1 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF%2Fblob%2Fmaster%2Fextensions%2F2.0%2FKhronos%2FKHR_draco_mesh_compression%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF/blob/master/extensions/2.0/Khronos/KHR_draco_mesh_compression/README.md" ref="nofollow noopener noreferrer">KHR_draco_mesh_compression</a></h3>
<p>最<strong>常见</strong>的一种网格压缩方式，采用开源的Draco算法，用于压缩和解压缩3D 网格和点云，并且可能会改变网格中顶点的顺序和数量。压缩的使文件小得多，但是在客户端设备上需要<strong>额外的解码时间</strong>。</p>
<ul>
<li>压缩方式</li>
</ul>
<p>可以使用<code>gltf-pipeline</code>gltf 文件优化工具进行压缩</p>
<pre><code class="copyable">gltf-pipeline -i male.glb -o male-processed.glb -d
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用方式（在 Three.js 中）</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; GLTFLoader &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three/examples/jsm/loaders/GLTFLoader'</span>
<span class="hljs-keyword">import</span> &#123; DRACOLoader &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three/examples/jsm/loaders/DRACOLoader'</span>

<span class="hljs-keyword">const</span> loader = <span class="hljs-keyword">new</span> GLTFLoader()

<span class="hljs-comment">// 创建解码器实例</span>
<span class="hljs-keyword">const</span> dracoLoader = <span class="hljs-keyword">new</span> DRACOLoader()
<span class="hljs-comment">// 设置解压库文件路径</span>
dracoLoader.setDecoderPath(DECODER_PATH)
<span class="hljs-comment">// 加载解码器实例</span>
loader.setDRACOLoader(dracoLoader)

loader.load(MODEL_FILE_PATH, <span class="hljs-function">(<span class="hljs-params">gltf</span>) =></span> &#123;
 <span class="hljs-comment">// ....</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>性能分析对比</li>
</ul>
<p>这个 glb 文件原大小为 3.2M，draco 压缩后为 1.8M，约为原文件的<strong>56%</strong>。</p>
<p>从上面的代码中可以看出，创建解码器实例需要引入额外的库来进行解码，<code>setDecoderPath</code>会自动请求 wasm 文件来进行解密操作。而这两个 wasm 文件同时也增加了请求时间和请求数量，那么加上这两个文件，真实的压缩率约为<strong>62.5%</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce3e30f2f8e145c8a7d16d0eeb4bae8a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，如果一个项目需要加载多个 glTF 文件，那么可以创建一个 DRACOLoader 实例并重复使用它。但如果项目只需要加载一个 glTF 文件，那么使用 draco 算法是否具有“性价比”就值得考量了。</p>
<p>用 demo 进行一下性能对比：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c12955880ed41f3bca1fd82d3af2960~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可见 draco 算法首次加载和解密时间，要大于原文件。而在<strong>实际</strong>项目中，这个差距更加明显，并且<strong>偶尔会出现解密堵塞的情况</strong>，需要重新进入页面才能恢复功能。</p>
<p>除此以外，还有一个很直观的问题，模型画质的损失是肉眼可观的。</p>
<p>如图，分别是在 iPhone 12 和小米 MIX2 中的样子：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52503fe7878f4fffaf87e664c69529ae~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>总而言之，如果要将 draco 压缩算法运用到大规模项目中，需要结合实际项目进行以下对比：</p>
<ul>
<li>(1) 请求两个文件+解密耗时，与本身 glb 文件压缩后的体积大小相比，真实性能对比；</li>
<li>(2) 画质是否会出现设计师无法接受的损失。</li>
</ul>
<br>
<h3 data-id="heading-12">4.1.2 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF%2Fblob%2Fmaster%2Fextensions%2F2.0%2FKhronos%2FKHR_mesh_quantization%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF/blob/master/extensions/2.0/Khronos/KHR_mesh_quantization/README.md" ref="nofollow noopener noreferrer">KHR_mesh_quantization</a></h3>
<p>顶点属性通常使用<code>FLOAT</code>类型存储，将原始始浮点值转换为16位或8位存储以适应统一的3D或2D网格，也就是我们所说的quantization向量化，该插件主要就是将其向量化。</p>
<p>例如，静态 PBR-ready 网格通常需要每个顶点<code>POSITION</code>（12 字节）、<code>TEXCOORD</code>（8 字节）、<code>NORMAL</code>（12 字节）和<code>TANGENT</code>（16 字节），总共 48 字节。通过此扩展，可以用于<code>SHORT</code>存储位置和纹理坐标数据（分别为 8 和 4 字节）以及<code>BYTE</code>存储法线和切线数据（各 4 字节），每个顶点总共 20 字节。</p>
<ul>
<li>压缩方式</li>
</ul>
<p>可以使用<code>gltfpack</code>工具进行压缩</p>
<pre><code class="copyable">gltfpack -i male.glb -o male-processed.glb
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用方式（在 Three.js 中）</li>
</ul>
<p>普普通通地用就好了，和不压缩的没什么区别</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; GLTFLoader &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three/examples/jsm/loaders/GLTFLoader'</span>

<span class="hljs-keyword">const</span> loader = <span class="hljs-keyword">new</span> GLTFLoader()
loader.load(MODEL_FILE_PATH, <span class="hljs-function">(<span class="hljs-params">gltf</span>) =></span> &#123;
 <span class="hljs-comment">// ....</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>性能对比</li>
</ul>
<p>原文件3.2M，压缩后1.9M，为原文件的59.3%，比原模型加载速度也快上不少。
放到实际项目中，没有画质损失和加载时间过长的问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8e46f33468340308314bd3543a127b6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">4.1.3 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF%2Fblob%2Fmaster%2Fextensions%2F2.0%2FVendor%2FEXT_meshopt_compression%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF/blob/master/extensions/2.0/Vendor/EXT_meshopt_compression/README.md" ref="nofollow noopener noreferrer">EXT_meshopt_compression</a></h3>
<p>此插件假定缓冲区视图数据针对 GPU 效率进行了优化——使用量化并使用最佳数据顺序进行 GPU 渲染——并在 bufferView 数据之上提供一个压缩层。每个 bufferView 都是独立压缩的，这允许加载器最大程度地将数据直接解压缩到 GPU 存储中。</p>
<p>除了优化压缩率之外，压缩格式还具有两个特性——非常快速的解码（使用 WebAssembly SIMD，解码器在现代桌面硬件上以约 1 GB/秒的速度运行），以及与通用压缩兼容的字节存储。也就是说，不是尽可能地减少编码大小，而是以通用压缩器可以进一步压缩它的方式构建比特流。</p>
<ul>
<li>压缩方式</li>
</ul>
<p>可以使用<code>gltfpack</code>工具进行压缩</p>
<pre><code class="copyable">gltfpack -i male.glb -o male-processed.glb -cc
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用方式（在 Three.js 中）</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; GLTFLoader &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three/examples/jsm/loaders/GLTFLoader'</span>
<span class="hljs-keyword">import</span> &#123; MeshoptDecoder &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three/examples/jsm/libs/meshopt_decoder.module.js'</span>

<span class="hljs-keyword">const</span> loader = <span class="hljs-keyword">new</span> GLTFLoader()
loader.setMeshoptDecoder(MeshoptDecoder)
loader.load(MODEL_FILE_PATH, <span class="hljs-function">(<span class="hljs-params">gltf</span>) =></span> &#123;
 <span class="hljs-comment">// ....</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>性能分析对比</li>
</ul>
<p>原文件3.2M，压缩后1.1M，为原文件的<strong>65.6%</strong>，首次加载时间比原模型快上不少。
放到实际项目中，没有画质损失和加载时间过长的问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a20c9b0d19142288f5cfe02f17a9670~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-14">五、多个机型设备与优化对比结果</h1>
<p>为了避免上文提到的“draco”压缩使得模型受损的情况，找了几台iPhone、安卓的手机来进行了一下性能与兼容的测试，让我们看一下结果。
PS：公司网络在不同时间段内网速不同（如上午和下午），可能会对数字产生小部分影响，但不影响文件优化横向对比。</p>
<h2 data-id="heading-15">iPhone 12（iOS 14.4，自用）</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d85bb1ad813e40279cf7b269db07ff7c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">Huawei Mate 40 pro （HarmonyOS，自用）</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60676b8d66f1445a937cc9d63027eb68~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">Xiaomi Mix2（Android 8.0，测试机）</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/027c9fc6aaa24bcfba16e81d98a7b544~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">iPhone 6sp （iOS 13.7，自用机）</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbf0ebcbcb8e4fb9b74386907b9fbec6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">5.1 总结</h2>
<p>可见，对于小部分需要使用模型的，并且只需要加载一个模型的业务，采用<code>KHR_mesh_quantization</code>或<code>EXT_meshopt_compression</code>进行网格压缩，再使用<code>gltf-pipeline</code>进行模块区分并对纹理图片压缩，是目前找到的较好的优化方案。</p>
<br>
<h1 data-id="heading-20">六、其他</h1>
<p>其实还有很多性能优化的插件，目前正在进行调试和调查，等后续迭代或有什么新进展，会继续更新：</p>
<p>网格优化的：</p>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF%2Fblob%2Fmaster%2Fextensions%2F2.0%2FVendor%2FEXT_mesh_gpu_instancing%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF/blob/master/extensions/2.0/Vendor/EXT_mesh_gpu_instancing/README.md" ref="nofollow noopener noreferrer">EXT_mesh_gpu_instancing</a></p>
<p>现 Three.js 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmrdoob%2Fthree.js%2Fissues%2F21937" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mrdoob/three.js/issues/21937" ref="nofollow noopener noreferrer">GLTFLoader</a> 尚未支持，Babylon.js 的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdoc.babylonjs.com%2Ftypedoc%2Fclasses%2Fbabylon.gltf2.loader.extensions.khr_mesh_quantization" target="_blank" rel="nofollow noopener noreferrer" title="https://doc.babylonjs.com/typedoc/classes/babylon.gltf2.loader.extensions.khr_mesh_quantization" ref="nofollow noopener noreferrer">BABYLON.GLTF2.Loader.Extensions</a> 支持</p>
</li>
</ul>
<p>还有一些纹理优化的插件：</p>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF%2Fblob%2Fmaster%2Fextensions%2F2.0%2FKhronos%2FKHR_texture_basisu%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF/blob/master/extensions/2.0/Khronos/KHR_texture_basisu/README.md" ref="nofollow noopener noreferrer">KHR_texture_basisu</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF%2Fblob%2Fmaster%2Fextensions%2F2.0%2FVendor%2FEXT_texture_webp%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF/blob/master/extensions/2.0/Vendor/EXT_texture_webp/README.md" ref="nofollow noopener noreferrer">EXT_texture_webp</a></p>
</li>
</ul>
<h1 data-id="heading-21">七、参考资料</h1>
<ol>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF-Tutorials%2Fblob%2Fmaster%2FgltfTutorial%2FgltfTutorial_002_BasicGltfStructure.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_002_BasicGltfStructure.md" ref="nofollow noopener noreferrer">The Basic Structure of glTF</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF%2Fblob%2Fmaster%2Fspecification%2F2.0%2FREADME.md%23glb-file-format-specification" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF/blob/master/specification/2.0/README.md#glb-file-format-specification" ref="nofollow noopener noreferrer">GLB File Format Specification</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF%2Ftree%2Fmaster%2Fextensions%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF/tree/master/extensions/" ref="nofollow noopener noreferrer">Extensions for glTF 2.0</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF%2Fblob%2Fmaster%2Fextensions%2F2.0%2FKhronos%2FKHR_draco_mesh_compression%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF/blob/master/extensions/2.0/Khronos/KHR_draco_mesh_compression/README.md" ref="nofollow noopener noreferrer">KHR_draco_mesh_compression</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fthreejs.org%2Fdocs%2F%23examples%2Fen%2Floaders%2FDRACOLoader" target="_blank" rel="nofollow noopener noreferrer" title="https://threejs.org/docs/#examples/en/loaders/DRACOLoader" ref="nofollow noopener noreferrer">DRACOLoader – three.js docs</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FCesiumGS%2Fgltf-pipeline" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/CesiumGS/gltf-pipeline" ref="nofollow noopener noreferrer">CesiumGS/gltf-pipeline: Content pipeline tools for optimizing glTF assets.</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF%2Fblob%2Fmaster%2Fextensions%2F2.0%2FKhronos%2FKHR_mesh_quantization%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF/blob/master/extensions/2.0/Khronos/KHR_mesh_quantization/README.md" ref="nofollow noopener noreferrer">KHR_mesh_quantization</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmeshoptimizer.org%2Fgltf%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://meshoptimizer.org/gltf/" ref="nofollow noopener noreferrer">📦 gltfpack | meshoptimizer</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fthreejs.org%2Fdocs%2F%3Fq%3DGLTFLoader%23examples%2Fen%2Floaders%2FGLTFLoader" target="_blank" rel="nofollow noopener noreferrer" title="https://threejs.org/docs/?q=GLTFLoader#examples/en/loaders/GLTFLoader" ref="nofollow noopener noreferrer">GLTFLoader</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKhronosGroup%2FglTF%2Fblob%2Fmaster%2Fextensions%2F2.0%2FVendor%2FEXT_meshopt_compression%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KhronosGroup/glTF/blob/master/extensions/2.0/Vendor/EXT_meshopt_compression/README.md" ref="nofollow noopener noreferrer">EXT_meshopt_compression</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6931954784018628621" target="_blank" title="https://juejin.cn/post/6931954784018628621">【网格压缩测评】MeshQuan、MeshOpt、Draco</a></p>
</li>
</ol></div>  
</div>
            