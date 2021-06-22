
---
title: 'Mapbox GL JS简析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e86b135e8ef24d358fa69d69e87f0757~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 19:32:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e86b135e8ef24d358fa69d69e87f0757~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">MapboxGLJS 简介</h2>
<p>Mapbox 公司成立于 2010 年，创立目标是为 Google Map 提供一个替代方案。在当时，Google Map 地图几乎垄断了所有线上地图业务，但是在 Google Map 中，几乎没有定制化的可能，也没有任何工具可以让制图者按照他们的设想来创建地图。Mapbox 的成立旨在改变这种状况，为制图人员和开发人员提供工具来创建他们想要的地图。值得一提的是，目前 Mapbox 提供的制图工具几乎都是开源的。Mapbox 目前主要提供地理数据、渲染客户端和其他与地图相关的服务。Mapbox GL JS 是他们的一个开源客户端库，用于渲染 Web 端的可交互地图。作为 Mapbox 生态系统的一部分，它通常与 Mapbox 提供的其他服务集成在一起，统一对外使用。目前 Mapbox 公司的主营业务除了地图相关产品，还包括 LBS(Location Based Services)服务、自动驾驶、自有数据(Boundaries, Traffic Data, Movement)以及车机服务。Mapbox GL JS 是一个 JavaScript 库，它使用 WebGL 技术，以<a href="https://www.mapbox.com/help/define-vector-tiles" target="_blank" rel="nofollow noopener noreferrer">vector tiles</a>方式数据组织，以<a href="https://www.mapbox.cn/mapbox-gl-js/style-spec" target="_blank" rel="nofollow noopener noreferrer">Mapbox styles</a>来配置地图样式规则，最终渲染得到交互式地图。Mapbox GL 生态系统的另一部分是<a href="https://www.mapbox.com/mobile/" target="_blank" rel="nofollow noopener noreferrer">Mapbox Mobile</a>，它是一个用 C++ 编写的兼容桌面和移动平台的渲染引擎。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e86b135e8ef24d358fa69d69e87f0757~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">Mapbox GL JS 作为地图引擎的优势</h2>
<h3 data-id="heading-2">相比于 Leaflet, OpenStreetMap 等 2D 栅格图地图引擎</h3>
<ul>
<li>Mapbox GL JS 使用矢量数据渲染地图（可以使用栅格数据），矢量数据易于更改要素样式，图层顺序，也可以在数据版本迭代时快速同步更新。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1b6e55bee874330a38c80a3aa6c0182~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1e49ba3e8fb4072b7da73c7bd0bec0c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>矢量数据相比于栅格图片，具有更多种数据压缩的可能性；因此在相同场景中，矢量数据的数据量要比栅格数据要小（矢量数据需要组织得当）。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68783c597574464eaf0ce5be616e3d08~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Mapbox GL JS 采用 WebGL 方案，相比于 Canvas 和 SVG 方案，可以支持更多的三维地图效果。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1429fb6048df40fd8a0e5fdcf2b95275~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">相比于 Cesium 等三维地图引擎</h3>
<ul>
<li>Mapbox GL JS 的渲染场景实际为 2.5D，并不是完全的 3D 场景（控制可视角度），这使得地图可视范围的可控，数据可以使用二维金字塔模型组织，提升了场景内数据筛选性能，也控制了同屏展示的数据量。</li>
<li>Mapbox GL JS 的体量相对较小，模块结构较为清晰，易于进行改造及二次开发。</li>
</ul>
<h3 data-id="heading-4">相比于 Google Map, AB Map（Mapbox GL JS versions 1.x）</h3>
<ul>
<li>Mapbox GL JS 为开源软件，社区生态丰富，同样易于改造及二次开发。</li>
<li>Mapbox GL JS 的开源协议为 BSD-3-Clause license，可以合法进行商业化使用。</li>
<li>Mapbox GL 体系提供的地图方案，支持地图数据服务内网部署，可以做到内外网隔离。</li>
<li><code>2.x版本已更换协议</code><a href="https://wptavern.com/mapbox-gl-js-is-no-longer-open-source" target="_blank" rel="nofollow noopener noreferrer">参考新闻</a></li>
</ul>
<blockquote>
<p>Mapbox GL JS v2 has a completely different, proprietary license.<em>It is not free and not truly open anymore.</em></p>
</blockquote>
<h2 data-id="heading-5">如何创建一张地图</h2>
<h3 data-id="heading-6">1. 准备工作</h3>
<ul>
<li>
<p>申请 access_tokenaccess_token 是 Mapbox 的一种鉴权手段，通过 access token 可以将 API requests 和用户账号关联起来；在开发中，调用地图数据，使用相应的 API 或 SDK 都需要开发者的 access_token 有相应的权限。</p>
</li>
<li>
<p>准备 Mapbox Style url 或 Mapbox Style 对象 Mapbox Style 是定义地图的视觉外观的文档：绘制什么数据、以什么顺序绘制以及绘制数据时如何设置数据样式；Mapbox Style 对象是具有特定根级别和嵌套属性的 JSON 对象，内容包括有关数据源、图层样式、雪碧图、文字字体、元数据等的信息；</p>
</li>
</ul>
<p>Style 通常有三种来源：</p>
<ol>
<li>使用 Mapbox 官网提供的标准样式</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09e300da25fd4972a2fb215dd22b0e32~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>使用 Mapbox 提供的<a href="https://docs.mapbox.com/help/glossary/mapbox-studio/" target="_blank" rel="nofollow noopener noreferrer">Mapbox Studio</a>工作台，配置自定义地图样式</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be030e098721404cbfdf9b6363ee0afe~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>
<pre><code class="copyable"> 手动编写样式JSON对象
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"version"</span>: <span class="hljs-number">8</span>,
    <span class="hljs-string">"name"</span>: <span class="hljs-string">"Void"</span>,
    <span class="hljs-string">"metadata"</span>: &#123;&#125;,
    <span class="hljs-string">"sources"</span>: &#123;&#125;,
    <span class="hljs-string">"sprite"</span>: <span class="hljs-string">"mapbox://sprites/mapbox/basic-v9"</span>,
    <span class="hljs-string">"glyphs"</span>: <span class="hljs-string">"mapbox://fonts/&#123;fontstack&#125;/&#123;range&#125;.pbf"</span>,
    <span class="hljs-string">"layers"</span>: []
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2. 创建地图</h3>
<ul>
<li>使用 Mapbox CDN</li>
</ul>
<p>在 HTML 文件的中引入 Mapbox GL JS 提供的 js 和 css 文件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script src=<span class="hljs-string">'https://api.mapbox.com/mapbox-gl-js/v2.2.0/mapbox-gl.js'</span>></script>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">'https://api.mapbox.com/mapbox-gl-js/v2.2.0/mapbox-gl.css'</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">'stylesheet'</span> /></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 HTML 文件的中加入地图容器 DOM 和相应 script 代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><div id=<span class="hljs-string">'map'</span> style=<span class="hljs-string">'width: 400px; height: 300px;'</span>></div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
mapboxgl.accessToken = <span class="hljs-string">'<your access token here>'</span>;
<span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> mapboxgl.Map(&#123;
    <span class="hljs-attr">container</span>: <span class="hljs-string">'map'</span>, <span class="hljs-comment">// 容器DOM id</span>
    <span class="hljs-attr">style</span>: <span class="hljs-string">'mapbox://styles/mapbox/streets-v11'</span>, <span class="hljs-comment">// style URL</span>
    <span class="hljs-attr">center</span>: [-<span class="hljs-number">74.5</span>, <span class="hljs-number">40</span>], <span class="hljs-comment">// 地图初始中心点 [lng, lat]</span>
    <span class="hljs-attr">zoom</span>: <span class="hljs-number">9</span> <span class="hljs-comment">// 地图初始zoom</span>
&#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用包引入</li>
</ul>
<p>安装 npm 包</p>
<pre><code class="copyable">npm install --save mapbox-gl
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以在 HTML 文件的中引入 Mapbox GL JS 提供的 js 和 css 文件</p>
<pre><code class="copyable"><link href='https://api.mapbox.com/mapbox-gl-js/v2.2.0/mapbox-gl.css' rel='stylesheet' />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以使用 CSS loader 在 js 文件中直接引入</p>
<pre><code class="copyable">import 'mapbox-gl/dist/mapbox-gl.css';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目中创建地图</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> mapboxgl <span class="hljs-keyword">from</span> <span class="hljs-string">'mapbox-gl'</span>; <span class="hljs-comment">// or "const mapboxgl = require('mapbox-gl');"</span>

mapboxgl.accessToken = <span class="hljs-string">'<your access token here>'</span>;
<span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> mapboxgl.Map(&#123;
    <span class="hljs-attr">container</span>: <span class="hljs-string">'map'</span>, <span class="hljs-comment">// 容器DOM id</span>
    <span class="hljs-attr">style</span>: <span class="hljs-string">'mapbox://styles/mapbox/streets-v11'</span>, <span class="hljs-comment">// style URL</span>
    <span class="hljs-attr">center</span>: [-<span class="hljs-number">74.5</span>, <span class="hljs-number">40</span>], <span class="hljs-comment">// 地图初始中心点 [lng, lat]</span>
    <span class="hljs-attr">zoom</span>: <span class="hljs-number">9</span> <span class="hljs-comment">// 地图初始zoom</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">Mapbox GL JS 架构</h2>
<h3 data-id="heading-9">数据组织</h3>
<p>Mapbox GL JS 采用 Web 墨卡托投影，这使得世界在地图中是一个正方形；同样所有的数据按照比例尺，均匀分布在每一个不同分辨率的相同尺寸的正方形网格中。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/835012deea9a49b18dddf30a6935c94d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7b204f0c3bf48de810f285a6ecfaa17~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>墨卡托投影，是正轴等角圆柱投影。由荷兰地图学家墨卡托(G.Mercator)于 1569 年创立。假想一个与地轴方向一致的圆柱切或割于地球，按等角条件，将经纬网投影到圆柱面上，将圆柱面展为平面后，即得本投影。墨卡托投影在切圆柱投影与割圆柱投影中，最早也是最常用的是切圆柱投影。!<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b33cc9351a8f4069abe19d6ec1ab38c3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>这种数据组织方式(tileset)，它可以快速定位当前所需数据，按需下载，并且易于存储与缓存。Mapbox 提供了可以将数据处理为 tileset 的工具，其所有的库和 SDK，都需要 tileset 来组织数据。</p>
<h3 data-id="heading-10">代码架构</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c36422269be4f1d96c571fe87f824bb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>Interface 层位于顶层，其中包含与地图用户交互的所有类。Map 和 Camera 控制地图状态（缩放，视角，位置等），Marker 和 Popup 是在地图上添加的标记，Control 是一系列地图上的小工具（放大缩小按钮，指南针等），Event Handler 处理地图的各种事件（move, click, zoom......）。</p>
</li>
<li>
<p>Style 层包含了表现和处理 Mapbox Style 的所有类。Layer 为地图中的图层，表示地图中的不同图形要素（道路-Line，区划面-Fill。。。），与 Mapbox Style 中的 layer 一一对应，主要存储图层对渲染要素的一系列配置；Source 表示地图所需要的数据，同样与与 Mapbox Style 中的 source 一一对应；Style 层还有 Light 等地图全局使用的公共样式类。</p>
</li>
<li>
<p>Render 层含使用 WebGL 在屏幕上渲染地图要素的所有类。Paint 是一个全局的渲染调度器，所有的渲染指令都由 Painter 下发；不同的图形要素（Fill, Line, Symbol......）有着不同的 Draw Function，用来执行不同的渲染逻辑；不同的要素也有不同的 Shader，来进行着色器渲染。</p>
</li>
<li>
<p>Map Data 层为地图渲染所需要的数据，它们按照数据源的不同，分为不同的 Source 类。Source 中包含数据的请求，处理，主子线程的通信方法。每一个 Source 在子线程有一个对应的 Worker Source，用于在子线程实际执行网络请求和数据处理等逻辑。</p>
</li>
<li>
<p>Tile Data 是层是数据在被请求到后，处理为渲染（WebGL）所需要的格式所用到的所有类。不同的图形要素需要不同的数据规格，因此在数据处理时，Source 会按照使用该 Source 的不同 Layer 进行不同的数据处理和组织，完成后以 Bucket 的形式存储，等待渲染时被调用。</p>
</li>
<li>
<p>Util 层为整个地图运行流程中，使用到的一些工具类。</p>
</li>
<li>
<p><strong>Source, Tile, Bucket, Layer 的关系</strong>Source 按照数据源区分，里面存储着不同的 Tile 网格；每个 Source 可以被多个 Layer 使用，针对调用的不同的 Layer，每个 Tile 会存储不同的 Bucket，为不同的渲染方式提供数据。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3b7fd343cb84fad96a9309e03506f27~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">从代码到地图</h2>
<h3 data-id="heading-12">1. 实例化 Map</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8c7482eab5a45fe87e1b342244919ae~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>实例化 Map 对象以后，主要的工作在 Style 解析传入的 Mapbox Style：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/ui/map.js</span>

<span class="hljs-built_in">this</span>.setStyle(options.style, &#123;<span class="hljs-attr">localFontFamily</span>: <span class="hljs-built_in">this</span>._localFontFamily, <span class="hljs-attr">localIdeographFontFamily</span>: <span class="hljs-built_in">this</span>._localIdeographFontFamily&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Style 中，主要工作分为两部分，添加 source 和 layer</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/style/style.js</span>

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> id <span class="hljs-keyword">in</span> json.sources) &#123;
    <span class="hljs-built_in">this</span>.addSource(id, json.sources[id], &#123;<span class="hljs-attr">validate</span>: <span class="hljs-literal">false</span>&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/style/style.js</span>

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> layer <span class="hljs-keyword">of</span> layers) &#123;
    layer = createStyleLayer(layer);
    layer.setEventedParent(<span class="hljs-built_in">this</span>, &#123;<span class="hljs-attr">layer</span>: &#123;<span class="hljs-attr">id</span>: layer.id&#125;&#125;);
    <span class="hljs-built_in">this</span>._layers[layer.id] = layer;
    <span class="hljs-built_in">this</span>._serializedLayers[layer.id] = layer.serialize();
    <span class="hljs-built_in">this</span>._updateLayerCount(layer, <span class="hljs-literal">true</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加 source 时，会创建用于数据处理的 Source 对象和用于存储数据的 SourceCache 对象；添加 layer 时，会创建相应的 Layer 对象，并在初始化时解析 layer 的相关配置(layout, paint)。至此，实例化 Map 对象的工作结束。</p>
<h3 data-id="heading-13">2. 开始渲染一帧画面</h3>
<p>每一次地图可视范围发生变化（移动中心点、缩放等操作），或者有数据处理完毕，都会引起地图开始更新。如果有动态效果，地图会定期（60fps）触发更新。</p>
<h4 data-id="heading-14">1. 更新数据</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcb8b42582b9499b8a24cb40f3ff98be~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
地图的更新从 Map 的_update 方法开始，首先会判断在当前可视范围下，是否需要更新数据：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/ui/map.js</span>

<span class="hljs-built_in">this</span>.style._updateSources(<span class="hljs-built_in">this</span>.transform);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Style 中，会判断每个 SourceCache 在当前可视范围下，能否提供完整的数据：</p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-comment">// src/style/style.js</span>

<span class="hljs-built_in">this</span>._sourceCaches[id].update(transform);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 SourceCache 中，如果发现当前可视范围需要但是无法提供的数据，Source 会请求该数据，同时会使用该瓦块的父/子瓦块占位，避免空白：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/source/source_cache.js</span>

<span class="hljs-keyword">const</span> tile = <span class="hljs-built_in">this</span>._addTile(tileID);

<span class="hljs-comment">// ..</span>
<span class="hljs-keyword">const</span> parentId = tileID.scaledTo(overscaledZ);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Source 中，通知 worker 请求该数据：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/source/vector_tile_source.js</span>

tile.request = tile.actor.send(<span class="hljs-string">'loadTile'</span>, params, done.bind(<span class="hljs-built_in">this</span>), <span class="hljs-literal">undefined</span>, <span class="hljs-literal">true</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 worker 中，发起数据请求，接收到数据后，处理成为所需要的 Bucket，返回给主线程中的 Source，Source 会将数据存储在 SourceCache 中，供下次渲染调用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/source/vector_tile_worker_source.js</span>

tile.loadVectorData(data, <span class="hljs-built_in">this</span>.map.painter);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">2. 渲染画面</h4>
<p>在更新数据后，开始渲染地图画面：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/ui/map.js</span>

<span class="hljs-comment">// Actually draw</span>
<span class="hljs-built_in">this</span>.painter.render(<span class="hljs-built_in">this</span>.style, &#123;
    <span class="hljs-attr">showTileBoundaries</span>: <span class="hljs-built_in">this</span>.showTileBoundaries,
    <span class="hljs-attr">showTerrainWireframe</span>: <span class="hljs-built_in">this</span>.showTerrainWireframe,
    <span class="hljs-attr">showOverdrawInspector</span>: <span class="hljs-built_in">this</span>._showOverdrawInspector,
    <span class="hljs-attr">showQueryGeometry</span>: !!<span class="hljs-built_in">this</span>._showQueryGeometry,
    <span class="hljs-attr">rotating</span>: <span class="hljs-built_in">this</span>.isRotating(),
    <span class="hljs-attr">zooming</span>: <span class="hljs-built_in">this</span>.isZooming(),
    <span class="hljs-attr">moving</span>: <span class="hljs-built_in">this</span>.isMoving(),
    fadeDuration,
    <span class="hljs-attr">isInitialLoad</span>: <span class="hljs-built_in">this</span>._isInitialLoad,
    <span class="hljs-attr">showPadding</span>: <span class="hljs-built_in">this</span>.showPadding,
    <span class="hljs-attr">gpuTiming</span>: !!<span class="hljs-built_in">this</span>.listens(<span class="hljs-string">'gpu-timing-layer'</span>),
    <span class="hljs-attr">speedIndexTiming</span>: <span class="hljs-built_in">this</span>.speedIndexTiming,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>地图的渲染由 Painter 执行，首先将每个 SourceCache 中需要用到的数据进行预处理：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77e271884fdb4690ac4bfb4e334ee999~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/render/painter.js</span>

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> id <span class="hljs-keyword">in</span> sourceCaches) &#123;
    <span class="hljs-keyword">const</span> sourceCache = sourceCaches[id];
    <span class="hljs-keyword">if</span> (sourceCache.used) &#123;
        sourceCache.prepare(<span class="hljs-built_in">this</span>.context);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SourceCache 会将本次渲染需要用到的 Tile 进行预处理</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/source/source_cache.js</span>

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">this</span>._tiles) &#123;
    <span class="hljs-keyword">const</span> tile = <span class="hljs-built_in">this</span>._tiles[i];
    tile.upload(context);
    tile.prepare(<span class="hljs-built_in">this</span>.map.style.imageManager);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Tile 会将存储的 Bucket 进行预处理，并处理所需要的的图片和文字的纹理：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/source/tile.js</span>

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> id <span class="hljs-keyword">in</span> <span class="hljs-built_in">this</span>.buckets) &#123;
    <span class="hljs-keyword">const</span> bucket = <span class="hljs-built_in">this</span>.buckets[id];
    <span class="hljs-keyword">if</span> (bucket.uploadPending()) &#123;
        bucket.upload(context);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Bucket 中，会将所需要的数据，处理为 WebGL 所需要的 Buffer：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/data/bucket/fill_bucket.js</span>

<span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.uploaded) &#123;
    <span class="hljs-built_in">this</span>.layoutVertexBuffer = context.createVertexBuffer(<span class="hljs-built_in">this</span>.layoutVertexArray, layoutAttributes);
    <span class="hljs-built_in">this</span>.indexBuffer = context.createIndexBuffer(<span class="hljs-built_in">this</span>.indexArray);
    <span class="hljs-built_in">this</span>.indexBuffer2 = context.createIndexBuffer(<span class="hljs-built_in">this</span>.indexArray2);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，数据预处理完成，开始执行 WebGL 绘制。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22f6f575b8094a63b0f74f0fb4d12082~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
绘制工作主要是逐 Layer 的三轮绘制。绘制开始时，首先进行一轮离屏渲染，将需要在 Frameuffer 上绘制的内容进行逐一绘制（例如热力图的密度纹理）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Offscreen pass ===============================================</span>
<span class="hljs-comment">// We first do all rendering that requires rendering to a separate</span>
<span class="hljs-comment">// framebuffer, and then save those for rendering back to the map</span>
<span class="hljs-comment">// later: in doing this we avoid doing expensive framebuffer restores.</span>
<span class="hljs-built_in">this</span>.renderPass = <span class="hljs-string">'offscreen'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开始主画布绘制，首先重置 WebGL 参数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/render/painter.js</span>

<span class="hljs-comment">// Rebind the main framebuffer now that all offscreen layers have been rendered:</span>
<span class="hljs-built_in">this</span>.context.bindFramebuffer.set(<span class="hljs-literal">null</span>);
<span class="hljs-built_in">this</span>.context.viewport.set([<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">this</span>.width, <span class="hljs-built_in">this</span>.height]);

<span class="hljs-comment">// Clear buffers in preparation for drawing to the main framebuffer</span>
<span class="hljs-built_in">this</span>.context.clear(&#123;<span class="hljs-attr">color</span>: options.showOverdrawInspector ? Color.black : Color.transparent, <span class="hljs-attr">depth</span>: <span class="hljs-number">1</span>&#125;);
<span class="hljs-built_in">this</span>.clearStencil();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开始两轮绘制，第一轮绘制无透明图层，第二轮绘制有透明度的图层。拆分的一个重要原因是图层是否有透明度，对于颜色混合和深度测试的处理方式都有不同：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/render/painter.js</span>

<span class="hljs-comment">// Opaque pass ===============================================</span>
<span class="hljs-comment">// Draw opaque layers top-to-bottom first.</span>
<span class="hljs-built_in">this</span>.renderPass = <span class="hljs-string">'opaque'</span>;
<span class="hljs-comment">// ...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/render/painter.js</span>

<span class="hljs-comment">// Translucent pass ===============================================</span>
<span class="hljs-comment">// Draw all other layers bottom-to-top.</span>
<span class="hljs-built_in">this</span>.renderPass = <span class="hljs-string">'translucent'</span>;
<span class="hljs-comment">// ...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在每一轮绘制中，需要遍历所有 Layer，下面对一个 Layer 的绘制进行简单介绍。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e2530b58751483c849a0999e8f9a44a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">首先准备模板测试中每个 Tile 的模板，这时由于在数据处理中，每个 Tile 中所记录的数据，实际范围是要比 Tile 的范围稍大，需要在绘制时进行模板测试，防止重叠：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/render/painter.js</span>

<span class="hljs-built_in">this</span>._renderTileClippingMasks(layer, sourceCache, coords);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开始绘制图形：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/render/painter.js</span>

<span class="hljs-built_in">this</span>.renderLayer(<span class="hljs-built_in">this</span>, sourceCache, layer, coords);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>绘制图形是由不同 Layer 类型对应的 Draw Function 完成，以 Fill 为例，在判断当前绘制轮次需要绘制时，会对当前可视范围的 Tile 逐一绘制：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/render/draw_fill.js</span>

drawFillTiles(painter, sourceCache, layer, coords, depthMode, colorMode, <span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先加载需要用到的 WebGL Program：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/render/draw_fill.js</span>

<span class="hljs-keyword">const</span> program = painter.useProgram(programName, programConfiguration);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置部分相关的 Uniform 配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/render/draw_fill.js</span>

fillUniformValues(tileMatrix);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用绘制命令：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/render/draw_fill.js</span>

program.draw(painter.context, drawMode, depthMode,
painter.stencilModeForClipping(coord), colorMode, CullFaceMode.disabled, uniformValues,
layer.id, bucket.layoutVertexBuffer, indexBuffer, segments,
layer.paint, painter.transform.zoom, programConfiguration);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Program 中会绑定其余的 Uniform 配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/render/program.js</span>

<span class="hljs-keyword">if</span> (configuration) &#123;
    configuration.setUniforms(context, <span class="hljs-built_in">this</span>.binderUniforms, currentProperties, &#123;<span class="hljs-attr">zoom</span>: (zoom: any)&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>绑定渲染所用到的 Vao：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/render/program.js</span>

vao.bind(
    context,
    <span class="hljs-built_in">this</span>,
    layoutVertexBuffer,
    configuration ? configuration.getPaintVertexBuffers() : [],
    indexBuffer,
    segment.vertexOffset,
    dynamicLayoutBuffer,
    dynamicLayoutBuffer2
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后调用绘制命令：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/render/program.js</span>

gl.drawElements(
    drawMode,
    segment.primitiveLength * primitiveSize,
    gl.UNSIGNED_SHORT,
    segment.primitiveOffset * primitiveSize * <span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">至此一个 Layer 的绘制就完成了。</h2>
<p>字节跳动数据平台前端团队，在公司内负责大数据相关产品的研发。我们在前端技术上保持着非常强的热情，除了数据产品相关的研发外，在数据可视化、海量数据处理优化、web excel、WebIDE、私有化部署、工程工具都方面都有很多的探索和积累。</p>
<p>欢迎关注「 字节前端 ByteFE 」
简历投递联系邮箱「<a href="mailto:tech@bytedance.com">tech@bytedance.com</a>」</p></div>  
</div>
            