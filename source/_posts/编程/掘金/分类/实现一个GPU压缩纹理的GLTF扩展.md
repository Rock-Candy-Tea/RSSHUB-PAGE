
---
title: '实现一个GPU压缩纹理的GLTF扩展'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45fbf0072e8a4e4a82f995466b4918e0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 09:12:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45fbf0072e8a4e4a82f995466b4918e0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">缘由</h2>
<p>很早之前就听公司的WebGL同时调研过GPU压缩纹理，我之前也做过一些调研，发现有<a href="https://github.com/BinomialLLC/basis_universal" target="_blank" rel="nofollow noopener noreferrer">basis_universal</a>工具可以实现快速的uastc、etc1s快速transcode到对应平台所支持的压缩纹理格式，但是由于wasm体积和loader等js体积过大而没有使用。后面发现有更轻量的transcode实现，所以想利用起来。</p>
<h2 data-id="heading-1">探索</h2>
<p><a href="https://github.com/KhronosGroup/Basis-Universal-Transcoders/" target="_blank" rel="nofollow noopener noreferrer">Basis-Universal-Transcoders</a>是由KhronosGroup所使用<code>AssemblyScript</code>编写，相比于basis 220+kb的wasm，十分轻量，但是缺点是所支持的transcode的格式少，只有3种，还有开发不算太活跃。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45fbf0072e8a4e4a82f995466b4918e0~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19dcbf11f0874ce8a7c571f4af1becae~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>后面了解到LayaAir的压缩纹理使用方案则是相对简单粗暴，ios使用pvrtc, 安卓etc1, 其他则是png/jpg。加上之前实现过<a href="https://github.com/deepkolos/hdr-prefilter-texture" target="_blank" rel="nofollow noopener noreferrer">hdr-prefilter-texture</a>, 同样的思路也可硬应用到压缩纹理上面。</p>
<p><strong>各种需要runtime处理的均可以预处理，runtime只需要加载预处理后的产物即可</strong></p>
<p>所以就有这个这个GPU压缩纹理扩展，把basis transcode产出存储起来，runtime根据所支持的格式下载对应预处理后的格式。</p>
<h2 data-id="heading-2">前置知识</h2>
<h3 data-id="heading-3">GLTF结构</h3>
<p>既然目标是GLTF扩展，就需要了解GLTF格式。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5c1b955dfae4f829865b7b242c1e40d~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>asset: 描述GLTF格式版本信息<br>
extensionsUsed：告诉parser需要一下扩展，才能解析GLTF<br>
其他的和关系型数据库的表有点类似，不过使用下标来进行关联，比如：</p>
<blockquote>
<p>scene: 指向scenes[0]<br>
scenes[i].nodes[j]: 指向nodes[j]<br>
nodes[i].mesh: 指向meshes[i]<br>
meshes[i].primitives[j].material: 指向materials[i]<br>
materials[i].normalTexture: 指向textures[i]<br>
textures[i].source: 指向images[i]<br>
images[i].uri: 指向网络地址<br>
images[i].bufferView: 指向bufferViews[i]<br>
bufferViews[i].buffer: 指向buffers[i]<br>
buffers[i].uri: 指向网络地址</p>
</blockquote>
<h3 data-id="heading-4">GLTF扩展</h3>
<p>简单了解了GLTF的信息关联方式后，则可以着手了解GLTF扩展如何编写。需要实现GLTF扩展也可以理解为是一个降级扩展，和google所实现的<code>EXT_texture_webp</code>, 相当类似。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">GLTFTextureWebPExtension</span>(<span class="hljs-params">parser</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.parser = parser;
  <span class="hljs-built_in">this</span>.name = EXTENSIONS.EXT_TEXTURE_WEBP;
  <span class="hljs-built_in">this</span>.isSupported = <span class="hljs-literal">null</span>;
&#125;

GLTFTextureWebPExtension.prototype.loadTexture = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">textureIndex</span>) </span>&#123;
  <span class="hljs-keyword">var</span> name = <span class="hljs-built_in">this</span>.name;
  <span class="hljs-keyword">var</span> parser = <span class="hljs-built_in">this</span>.parser;
  <span class="hljs-keyword">var</span> json = parser.json;

  <span class="hljs-keyword">var</span> textureDef = json.textures[textureIndex];

  <span class="hljs-keyword">if</span> (!textureDef.extensions || !textureDef.extensions[name]) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
  &#125;

  <span class="hljs-keyword">var</span> extension = textureDef.extensions[name];
  <span class="hljs-keyword">var</span> source = json.images[extension.source];

  <span class="hljs-keyword">var</span> loader = parser.textureLoader;
  <span class="hljs-keyword">if</span> (source.uri) &#123;
    <span class="hljs-keyword">var</span> handler = parser.options.manager.getHandler(source.uri);
    <span class="hljs-keyword">if</span> (handler !== <span class="hljs-literal">null</span>) loader = handler;
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.detectSupport().then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">isSupported</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (isSupported) <span class="hljs-keyword">return</span> parser.loadTextureImage(textureIndex, source, loader);

    <span class="hljs-keyword">if</span> (json.extensionsRequired && json.extensionsRequired.indexOf(name) >= <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'THREE.GLTFLoader: WebP required by asset but unsupported.'</span>);
    &#125;

    <span class="hljs-comment">// Fall back to PNG or JPEG.</span>
    <span class="hljs-keyword">return</span> parser.loadTexture(textureIndex);
  &#125;);
&#125;;

GLTFTextureWebPExtension.prototype.detectSupport = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.isSupported) &#123;
    <span class="hljs-built_in">this</span>.isSupported = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve</span>) </span>&#123;
      <span class="hljs-keyword">var</span> image = <span class="hljs-keyword">new</span> Image();

      image.src = <span class="hljs-string">'data:image/webp;base64,UklGRiIAAABXRUJQVlA4IBYAAAAwAQCdASoBAAEADsD+JaQAA3AAAAAA'</span>;
      image.onload = image.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        resolve(image.height === <span class="hljs-number">1</span>);
      &#125;;
    &#125;);
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.isSupported;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到关键只有两个方法，一个是<code>detectSupport</code>，一个是<code>loadTexture</code>，逻辑均比较容易理解，其中<code>loadTexture</code>是由<code>GLTFLoader</code>触发。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/951c89cd02024b67bd7a813d35c3c77d~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以发现自定义GLTF扩展还是比较容易的，只需要在GLTFLoader里搜索this._invokeOne即可知道所支持的钩子函数有多少，目前有5个，分别是</p>
<ol start="0">
<li>loadMesh</li>
<li>loadBufferView</li>
<li>loadMaterial</li>
<li>loadTexture</li>
<li>getMaterialType</li>
</ol>
<h2 data-id="heading-5">实现</h2>
<p>先整理实现的大概思路。</p>
<p>GLTF扩展部分</p>
<ol start="0">
<li>定义扩展的scheme</li>
<li>detectSupport 通过获取gl读取扩展支持情况取得</li>
<li>loadTexture 按照scheme加载对应数据，生成CompressedTexture并返回</li>
</ol>
<p>工具部分</p>
<ol start="0">
<li>从GLTF/GLB加载，把里面包含的texture转换成basis, 然后decode成astc|bc7|dxt|pvrtc|etc1</li>
<li>按照scheme格式存储导出gltf。</li>
</ol>
<h3 data-id="heading-6">定义scheme</h3>
<p>参考EXT_texture_webp可知，扩展配置存放在extensions.EXT_texture_webp中，也就是只需要定义这部分格式即可。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d29da76e57cf450dace694020da09c51~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"textures"</span>: [
    &#123;
      <span class="hljs-attr">"source"</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">"extensions"</span>: &#123;
        <span class="hljs-attr">"EXT_GPU_COMPRESSED_TEXTURE"</span>: &#123;
          <span class="hljs-attr">"astc"</span>: <span class="hljs-number">1</span>,
          <span class="hljs-attr">"bc7"</span>: <span class="hljs-number">2</span>,
          <span class="hljs-attr">"dxt"</span>: <span class="hljs-number">3</span>,
          <span class="hljs-attr">"pvrtc"</span>: <span class="hljs-number">4</span>,
          <span class="hljs-attr">"etc1"</span>: <span class="hljs-number">5</span>,
          <span class="hljs-attr">"width"</span>: <span class="hljs-number">2048</span>,
          <span class="hljs-attr">"height"</span>: <span class="hljs-number">2048</span>,
          <span class="hljs-attr">"hasAlpha"</span>: <span class="hljs-number">0</span>,
          <span class="hljs-attr">"compress"</span>: <span class="hljs-number">1</span>
        &#125;
      &#125;
    &#125;
  ],
  <span class="hljs-attr">"buffers"</span>: [
    &#123; <span class="hljs-attr">"name"</span>: <span class="hljs-string">"buffer"</span>, <span class="hljs-attr">"byteLength"</span>: <span class="hljs-number">207816</span>, <span class="hljs-attr">"uri"</span>: <span class="hljs-string">"buffer.bin"</span> &#125;,
    &#123; <span class="hljs-attr">"name"</span>: <span class="hljs-string">"image3.astc"</span>, <span class="hljs-attr">"byteLength"</span>: <span class="hljs-number">48972</span>, <span class="hljs-attr">"uri"</span>: <span class="hljs-string">"image3.astc.bin"</span> &#125;,
    &#123; <span class="hljs-attr">"name"</span>: <span class="hljs-string">"image3.bc7"</span>, <span class="hljs-attr">"byteLength"</span>: <span class="hljs-number">50586</span>, <span class="hljs-attr">"uri"</span>: <span class="hljs-string">"image3.bc7.bin"</span> &#125;,
    &#123; <span class="hljs-attr">"name"</span>: <span class="hljs-string">"image3.dxt"</span>, <span class="hljs-attr">"byteLength"</span>: <span class="hljs-number">10686</span>, <span class="hljs-attr">"uri"</span>: <span class="hljs-string">"image3.dxt.bin"</span> &#125;,
    &#123; <span class="hljs-attr">"name"</span>: <span class="hljs-string">"image3.pvrtc"</span>, <span class="hljs-attr">"byteLength"</span>: <span class="hljs-number">21741</span>, <span class="hljs-attr">"uri"</span>: <span class="hljs-string">"image3.pvrtc.bin"</span> &#125;,
    &#123; <span class="hljs-attr">"name"</span>: <span class="hljs-string">"image3.etc1"</span>, <span class="hljs-attr">"byteLength"</span>: <span class="hljs-number">22360</span>, <span class="hljs-attr">"uri"</span>: <span class="hljs-string">"image3.etc1.bin"</span> &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>格式很简单，一看就明白，astc|bc7|dxt|pvrtc|etc1字段指向buffers[i]。</p>
<h3 data-id="heading-7">生成对应结构的GLTF</h3>
<p>这里一部分可以参考basis的<code>webgl/texture/index.html</code>，循环生成5种类型的压缩纹理产物保存到bin文件即可，然后手动编写GLTF文件即可。</p>
<p>至此，基础版已经可以编写出来了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GLTFGPUCompressedTexture</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">parser</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'EXT_GPU_COMPRESSED_TEXTURE'</span>;
    <span class="hljs-built_in">this</span>.parser = parser;
  &#125;

  <span class="hljs-function"><span class="hljs-title">detectSupport</span>(<span class="hljs-params">renderer</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.supportInfo = &#123;
      <span class="hljs-attr">astc</span>: renderer.extensions.has(<span class="hljs-string">'WEBGL_compressed_texture_astc'</span>),
      <span class="hljs-attr">bc7</span>: renderer.extensions.has(<span class="hljs-string">'EXT_texture_compression_bptc'</span>),
      <span class="hljs-attr">dxt</span>: renderer.extensions.has(<span class="hljs-string">'WEBGL_compressed_texture_s3tc'</span>),
      <span class="hljs-attr">etc1</span>: renderer.extensions.has(<span class="hljs-string">'WEBGL_compressed_texture_etc1'</span>),
      <span class="hljs-attr">etc2</span>: renderer.extensions.has(<span class="hljs-string">'WEBGL_compressed_texture_etc'</span>),
      <span class="hljs-attr">pvrtc</span>:
        renderer.extensions.has(<span class="hljs-string">'WEBGL_compressed_texture_pvrtc'</span>) ||
        renderer.extensions.has(<span class="hljs-string">'WEBKIT_WEBGL_compressed_texture_pvrtc'</span>),
    &#125;;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">loadTexture</span>(<span class="hljs-params">textureIndex</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; parser, name &#125; = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">const</span> json = parser.json;
    <span class="hljs-keyword">const</span> textureDef = json.textures[textureIndex];

    <span class="hljs-keyword">if</span> (!textureDef.extensions || !textureDef.extensions[name]) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    
    <span class="hljs-keyword">const</span> extensionDef = textureDef.extensions[name];
    <span class="hljs-keyword">const</span> &#123; width, height, hasAlpha &#125; = extensionDef;

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> name <span class="hljs-keyword">in</span> <span class="hljs-built_in">this</span>.supportInfo) &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.supportInfo[name] && extensionDef[name] !== <span class="hljs-literal">undefined</span>) &#123;
        <span class="hljs-keyword">return</span> parser
          .getDependency(<span class="hljs-string">'buffer'</span>, extensionDef[name])
          .then(<span class="hljs-function"><span class="hljs-params">buffer</span> =></span> &#123;
            <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> 支持带mipmap的压缩纹理</span>
            <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> zstd压缩</span>

            <span class="hljs-keyword">const</span> mipmaps = [
              &#123;
                <span class="hljs-attr">data</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(buffer),
                width,
                height,
              &#125;,
            ];


            <span class="hljs-comment">// 目前的buffer是直接可以传递到GPU的buffer</span>
            <span class="hljs-keyword">const</span> texture = <span class="hljs-keyword">new</span> CompressedTexture(
              mipmaps,
              width,
              height,
              typeFormatMap[name][hasAlpha],
              UnsignedByteType,
            );
            texture.minFilter =
              mipmaps.length === <span class="hljs-number">1</span> ? LinearFilter : LinearMipmapLinearFilter;
            texture.magFilter = LinearFilter;
            texture.generateMipmaps = <span class="hljs-literal">false</span>;
            texture.needsUpdate = <span class="hljs-literal">true</span>;

            <span class="hljs-keyword">return</span> texture;
          &#125;);
      &#125;
    &#125;

    <span class="hljs-comment">// Fall back to PNG or JPEG.</span>
    <span class="hljs-keyword">return</span> parser.loadTexture(textureIndex);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">丰富细节</h2>
<ol start="0">
<li>由于etc1s产出的basis，体积小，但是质量差，uastc质量高，但是体积大，所以需要使用无损压缩。</li>
<li>需要支持mipmap, GPU压缩纹理无法在GPU快速生成mipmap，需要实现mipmap加载</li>
<li>既然需要压缩，可能需要使用web worker加速，wasm加速，SIMD加速等</li>
<li>CLI转换工具支持多进程，批量处理，输出大小统计信息</li>
<li>编写性能测试用例，对比 KTX2+uastc 的压缩纹理方案，记录数据整理表格</li>
<li>PC端、手机浏览器对比，还有ImageBitmapLoader，纹理数量大小，分辨率大小等对比</li>
<li>少图片使用 UI 线程 decode, 多图片使用 worker decode</li>
<li>完善资源释放逻辑，dipose</li>
</ol>
<p>然后就有了相对完善的解决方案<a href="https://github.com/deepkolos/gltf-gpu-compressed-texture" target="_blank" rel="nofollow noopener noreferrer">gltf-gpu-compressed-texture</a></p>
<blockquote>
<p>一个用于 GPU 压缩纹理降级的 GLTF 扩展，以及批量 CLI 转换工具，适用于<code>THREE</code>的<code>GLTFLoader</code>，<a href="https://deepkolos.github.io/gltf-gpu-compressed-texture/examples/index.html" target="_blank" rel="nofollow noopener noreferrer">DEMO 地址</a>，<a href="https://github.com/deepkolos/glTF/tree/master/extensions/2.0/Vendor/EXT_GPU_COMPRESSED_TEXTURE" target="_blank" rel="nofollow noopener noreferrer">扩展定义</a></p>
</blockquote>
<h2 data-id="heading-9">性能数据</h2>
<p>运行环境 Chrome 93, CPU Intel I9 10900 ES 版，核显 HD630<br>
加载 <code>BC7</code> 格式，use ImageBitmapLoader，THREE r129，localhost，disable cache: true</p>

















































































































<table><thead><tr><th>模型</th><th>参数</th><th>load</th><th>render</th><th>总耗时</th><th>模型大小</th><th>依赖大小</th></tr></thead><tbody><tr><td>banzi_blue</td><td>gltf-tc zstd no-mimap no-worker</td><td>36.10ms</td><td>1.60ms</td><td>37.70ms</td><td>506kb</td><td>22.3kb</td></tr><tr><td>banzi_blue</td><td>gltf-tc no-zstd mimap no-worker</td><td>25.80ms</td><td>1.50ms</td><td>27.30ms</td><td>2.2mb</td><td>22.3kb</td></tr><tr><td>banzi_blue</td><td>gltf-tc zstd mimap no-worker</td><td>37.90ms</td><td>1.60ms</td><td>39.50ms</td><td>648kb</td><td>22.3kb</td></tr><tr><td>banzi_blue</td><td>gltf ktx2 uastc</td><td>534.70ms</td><td>1.70ms</td><td>536.40ms</td><td>684kb</td><td>249.3kb</td></tr><tr><td>banzi_blue</td><td>glb</td><td>32.80qms</td><td>6.00ms</td><td>38.80ms</td><td>443kb</td><td></td></tr><tr><td>banzi_blue</td><td>gltf</td><td>27.70ms</td><td>4.90ms</td><td>32.60ms</td><td>446kb</td><td></td></tr><tr><td>BoomBox</td><td>gltf-tc zstd mipmap worker</td><td>153.50ms</td><td>23.70ms</td><td>177.20ms</td><td>6.6mb</td><td>22.3kb</td></tr><tr><td>BoomBox</td><td>gltf-tc zstd mipmap no-worker</td><td>241.10ms</td><td>9.40ms</td><td>250.50ms</td><td>6.6mb</td><td>22.3kb</td></tr><tr><td>BoomBox</td><td>glb ktx2 uastc</td><td>506.10ms</td><td>9.30ms</td><td>515.40ms</td><td>7.1mb</td><td>249.3kb</td></tr><tr><td>BoomBox</td><td>glb</td><td>156.10ms</td><td>89.50ms</td><td>245.60ms</td><td>11.3mb</td><td></td></tr><tr><td>BoomBox</td><td>gltf</td><td>120.20ms</td><td>58.80ms</td><td>179.00ms</td><td>11.3mb</td><td></td></tr></tbody></table>
<blockquote>
<p>由于 banzi_blue 贴图小于 4 张，所以在 UI 线程 decode zstd，因为 worker 传数据也会有不少耗时
对比使用的 KTX2Loader 全部 zstd decode 是在 UI 线程，<a href="https://github.com/mrdoob/three.js/pull/21984" target="_blank" rel="nofollow noopener noreferrer">decode in Web Worker PR</a>已提交<br>
依赖大小 22.3kb 是从<a href="https://deepkolos.github.io/gltf-gpu-compressed-texture/examples/index.html" target="_blank" rel="nofollow noopener noreferrer">线上 DEMO</a> 取得，http-server --gzip 不太好使</p>
</blockquote>
<p>可以明显看到相比于 KTX2+uastc 的压缩纹理方案，从加载耗时和依赖大小，有<strong>大幅优势</strong>，模型大小也有不少优势<br>
同时也可以看到 BoomBox gltf-tc zstd mipmap worker load+render 耗时，与 gltf 耗时 相差不大，但是模型大小有大幅优势</p>
<p>MI 8 下的测试数据可以查看 <a href="https://github.com/deepkolos/gltf-gpu-compressed-texture/tree/main/screenshots" target="_blank" rel="nofollow noopener noreferrer">screenshots</a> 目录</p>
<p>微信 webview 下 BoomBox 均比 glb/gltf 快，属于异常，chrome 下表现正常，banzi_blue 则稍慢一些，KTX2 的方案依然很慢</p>
<h2 data-id="heading-10">命令行使用</h2>
<blockquote>
<p>使用之前请确保<a href="https://github.com/facebook/zstd/releases/" target="_blank" rel="nofollow noopener noreferrer">zstd</a>和<a href="https://github.com/BinomialLLC/basis_universal/releases/" target="_blank" rel="nofollow noopener noreferrer">basisu</a>已经在 PATH 里面</p>
</blockquote>
<pre><code class="hljs language-sh copyable" lang="sh">> npm i gltf-gpu-compressed-texture -S
<span class="hljs-comment"># 查看帮助</span>
> gltf-tc -h

  -h --<span class="hljs-built_in">help</span>                                              显示帮助
  -i --input [dir] [?outdir] [?compress] [?mipmap]       把gltf所使用纹理转换为GPU压缩纹理并支持fallback

Examples:
  gltf-tc -i ./examples/glb ./examples/zstd
  gltf-tc -i ./examples/glb ./examples/no-zstd 0
  gltf-tc -i ./examples/glb ./examples/no-mipmap 1 <span class="hljs-literal">false</span>
  gltf-tc -i ./examples/glb ./examples/no-zstd-no-mipmap 0 <span class="hljs-literal">false</span>

<span class="hljs-comment"># 执行</span>
> gltf-tc -i ./examples/glb ./examples/zstd

<span class="hljs-keyword">done</span>: 6417ms    image3.png      法线:<span class="hljs-literal">false</span>      sRGB: <span class="hljs-literal">true</span>
<span class="hljs-keyword">done</span>: 13746ms   image2.png      法线:<span class="hljs-literal">true</span>       sRGB: <span class="hljs-literal">false</span>
<span class="hljs-keyword">done</span>: 14245ms   image0.png      法线:<span class="hljs-literal">false</span>      sRGB: <span class="hljs-literal">true</span>
<span class="hljs-keyword">done</span>: 14491ms   image1.png      法线:<span class="hljs-literal">false</span>      sRGB: <span class="hljs-literal">false</span>
<span class="hljs-keyword">done</span>: 577ms     FINDI_TOUMING01_nomarl1.jpg     法线:<span class="hljs-literal">true</span>       sRGB: <span class="hljs-literal">false</span>
<span class="hljs-keyword">done</span>: 568ms     FINDI_TOUMING01_Basecoler.png   法线:<span class="hljs-literal">false</span>      sRGB: <span class="hljs-literal">true</span>
<span class="hljs-keyword">done</span>: 1267ms    lanse_banzi-1.jpg       法线:<span class="hljs-literal">false</span>      sRGB: <span class="hljs-literal">true</span>
<span class="hljs-keyword">done</span>: 577ms     FINDI_TOUMING01_Basecoler.png   法线:<span class="hljs-literal">false</span>      sRGB: <span class="hljs-literal">true</span>
<span class="hljs-keyword">done</span>: 604ms     FINDI_TOUMING01_nomarl1.jpg     法线:<span class="hljs-literal">true</span>       sRGB: <span class="hljs-literal">false</span>
<span class="hljs-keyword">done</span>: 1280ms    lvse_banzi-1.jpg        法线:<span class="hljs-literal">false</span>      sRGB: <span class="hljs-literal">true</span>

cost: 17.75s
compress: 1, summary:
  bitmap: 11.22MB
  astc  : 7.18MB
  etc1  : 1.85MB
  bc7   : 7.16MB
  dxt   : 3.04MB
  pvrtc : 2.28MB
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">NPM 包使用</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; GLTFLoader, CompressedTexture, WebGLRenderer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'three-platfromzie/examples/jsm/loaders/GLTFLoader'</span>;
<span class="hljs-keyword">import</span> GLTFGPUCompressedTexture <span class="hljs-keyword">from</span> <span class="hljs-string">'gltf-gpu-compressed-texture'</span>;

<span class="hljs-keyword">const</span> gltfLoader = <span class="hljs-keyword">new</span> GLTFLoader();
<span class="hljs-keyword">const</span> renderer = <span class="hljs-keyword">new</span> WebGLRenderer();
<span class="hljs-keyword">const</span> scene = <span class="hljs-keyword">new</span> Scene();

gltfLoader.register(<span class="hljs-function"><span class="hljs-params">parser</span> =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> GLTFGPUCompressedTexture(parser, renderer, &#123;
    <span class="hljs-attr">CompressedTexture</span>: THREE.CompressedTexture,
  &#125;);
&#125;);

gltfLoader.loadAsync(<span class="hljs-string">'./examples/zstd/BoomBox.gltf'</span>).then(<span class="hljs-function">(<span class="hljs-params">gltf</span>) =></span> &#123;
  scene.add(gltf.scene);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">折腾发现</h2>
<ol start="0">
<li>压缩纹理minFilter和magFilter支持有限</li>
<li>zstd比png decode速度快，所以有zpng格式出现</li>
<li>比zstd更好的是az64不过没开源，也不知道实际性能情况</li>
<li>ktx2Loader里使用的居然zstddec是在UI线程decode, 所以提个PR，实现worker pool decode</li>
<li>利用transferable传递buffer不能是经过Offset的TypeArray, 比如Uint8Array(buffer, dataOffset), 需要clone一下Uint8Array.from(new Uint8Array(buffer, dataOffset));</li>
<li>epic有类似basis transcode方案和压缩格式 <a href="http://www.radgametools.com/oodle.htm" target="_blank" rel="nofollow noopener noreferrer">oodle</a>, 闭源</li>
<li>zstd还可能可以使用到tf模型上面去，不过tf也有自己的<a href="https://github.com/tensorflow/compression" target="_blank" rel="nofollow noopener noreferrer">数据压缩</a></li>
<li>有实现在GPU decode Huffman, <a href="https://dl.acm.org/doi/10.1145/3225058.3225076" target="_blank" rel="nofollow noopener noreferrer">Massively Parallel Huffman Decoding on GPUs</a></li>
<li>最开始提到的Basis-Universal-Transcoders，<a href="https://github.com/BabylonJS/Babylon.js/blob/master/ktx2Decoder/src/Transcoders/liteTranscoder_UASTC_ASTC.ts" target="_blank" rel="nofollow noopener noreferrer">babylon</a>已经应用起来了, 只是还是标注实验性</li>
<li>zstd wasm应该是未使用SIMD版本，并且是上一年构建的，使用最新版本构建wasm，不过未能成功跑起来</li>
<li>IOS 上传纹理会卡GIF，使用了压缩纹理则不会</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbc051216c4a407eac7c740555afc470~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_20210615004511.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">最后</h2>
<p>欢迎大家使用<a href="https://github.com/deepkolos/gltf-gpu-compressed-texture" target="_blank" rel="nofollow noopener noreferrer">gltf-gpu-compressed-texture</a>，欢迎star</p></div>  
</div>
            