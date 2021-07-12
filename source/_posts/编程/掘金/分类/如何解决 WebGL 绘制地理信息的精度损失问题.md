
---
title: '如何解决 WebGL 绘制地理信息的精度损失问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb0939127f5b4d6e94a778d41f9120b1~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 19:55:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb0939127f5b4d6e94a778d41f9120b1~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">引言：热力图为什么在抖动呢？</h2>
<p>Deck.GL 是 Uber 开源的地理数据渲染框架，在使用 Deck.GL 绘制热力图的时候，发现不断放大地图时，地图层明显地抖动，且热力的聚合结果也有问题。下面的 demo 展示了这个现象，黄色图层是热力图图层，黑点代表原始数据，显然不断放大地图时，热力图的点并没有和原始数据点对应，且在不断抖动。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb0939127f5b4d6e94a778d41f9120b1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Ftimeless15%2Fembed%2FYzNpgNO" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/timeless15/embed/YzNpgNO" ref="nofollow noopener noreferrer">代码地址</a></strong></p>
<p>但官方的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeck.gl%2Fdocs%2Fapi-reference%2Faggregation-layers%2Fheatmap-layer" target="_blank" rel="nofollow noopener noreferrer" title="https://deck.gl/docs/api-reference/aggregation-layers/heatmap-layer" ref="nofollow noopener noreferrer">demo</a> 却并没有出现这个现象，那么问题出在了哪里呢？</p>
<p>如果非要说两个 demo 之间有何不同，就是数据不一样。测试 demo 的地图数据是室内地图级别的，而官方 demo 数据是在城市级别的。室内地图数据到小数点后五六位才出现不同，城市级别的数据在小数点后一两位，那么很有可能是数据精度损失导致的。</p>
<p>基于这个猜想，上网一搜确实有不少文章介绍由于 WebGL 的精度损失带来的问题，看来是个共性的问题，那么是如何解决的呢？我们先从数据开始分析，了解不同地理渲染框架是如何解决这个问题的。</p>
<h2 data-id="heading-1">前置背景</h2>
<h3 data-id="heading-2">Web 墨卡托投影</h3>
<p>因为地球是圆的，要将地图展示在平面上，需要通过一定的投影变换绘制到平面上。墨卡托投影又称“等角正轴圆柱投影”，其等角的特性可以保证对象形状不变性，也可以保证方向和相互位置的正确性。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FWeb_Mercator_projection" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Web_Mercator_projection" ref="nofollow noopener noreferrer">具体的原理</a>不在此赘述，有兴趣的可以自行了解。Web 墨卡托投影则将地球的椭圆球体简化为原型球体，坐标转换的公式如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7392bca5b662482482f122d681200e6a~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/139943f79b324727981249e7c7c4f488~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从公式可以看出，纬度坐标到 Y 轴坐标的转换是非线性的，计算不仅依赖于三角函数和对数运算，且必须在每一帧的渲染中对每个坐标都进行计算，显然会带来大量的计算开销。</p>
<h3 data-id="heading-3">精度损失</h3>
<p>地理渲染框架中都需要将元素的经纬度坐标转换为屏幕的像素坐标，随着地图不断放大，经纬度坐标转换到像素坐标的变换矩阵的位移值越来越大，即像素坐标值越来越大。因为 JS 数据是 64 位双精度浮点数，而着色器程序 GLSL 的数据只能是  32 位双精度浮点数，因此从 JS 往着色器内部传数据时，必然会出现精度丢失现象。如果不对精度丢失问题做处理，那么当放大到一定程度以后，移动地图时就会发现这些元素出现抖动现象。</p>
<p><code>Math.fround</code> 方法可以将数据从 64 位转换到 32 位：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Math</span>.fround(-<span class="hljs-number">122.4000588</span>); <span class="hljs-comment">// -122.40006256103516</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假设坐标是 <code>[-122.4000588, 37.7900699]</code> ，将其转换为 32 位浮点数是 <code>[-122.40006256103516, 37.790069580078125]</code>，这两个点之间的距离在真实世界的差值有 0.3325 米。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9343b1962b5945d7a1eeaba58de8c325~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么不同的地理渲染框架是如何处理大量计算和精度损失的问题呢？</p>
<h2 data-id="heading-4">Mapbox 的做法</h2>
<p>Mapbox 采用了瓦片坐标系。地理信息的展示要素通常是静止的，因此可以预先将地图分成若干瓦片，每个瓦片包含了实际的地理信息要素。这样每次相机发生变化时，只需要以视口内的瓦片为单位渲染数据就行了。瓦片坐标系也很好理解，下图是缩放等级 z 为 2 下的瓦片坐标系：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f897b528c9c4493ebc3724ddbdcb4d33~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Mapbox 所有的过程都是在平面坐标系下进行，因此首先通过墨卡托投影将要素的经纬度坐标投影至平面坐标，在每次渲染过程中都重新实时计算瓦片相对中心点的偏移矩阵，将数据变换到瓦片坐标系中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pixelsToTileUnits</span>(<span class="hljs-params">tile: &#123;tileID: OverscaledTileID, tileSize: number&#125;,
 pixelValue: number, z: number</span>): <span class="hljs-title">number</span> </span>&#123;
    <span class="hljs-keyword">return</span> pixelValue * (EXTENT / (tile.tileSize * <span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">2</span>,
 z - tile.tileID.overscaledZ)));
&#125;

<span class="hljs-keyword">const</span> translation = [
  inViewportPixelUnitsUnits ? translate[<span class="hljs-number">0</span>] : pixelsToTileUnits(tile, translate[<span class="hljs-number">0</span>], <span class="hljs-built_in">this</span>.transform.zoom),
  inViewportPixelUnitsUnits ? translate[<span class="hljs-number">1</span>] : pixelsToTileUnits(tile, translate[<span class="hljs-number">1</span>], <span class="hljs-built_in">this</span>.transform.zoom),
  <span class="hljs-number">0</span>
];

<span class="hljs-keyword">const</span> translatedMatrix = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Float32Array</span>(<span class="hljs-number">16</span>);
mat4.translate(translatedMatrix, matrix, translation);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在得到平面坐标后，为了减少数据量，Mapbox 对某些要素进行简化，并根据瓦片信息剪裁要素，再获取当前视口内包含的瓦片，最后以瓦片为单位，渲染其包含的要素。具体的过程可以参考 Mapbox 的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.mapbox.com%2Frendering-big-geodata-on-the-fly-with-geojson-vt-4e4d2a5dd1f2" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.mapbox.com/rendering-big-geodata-on-the-fly-with-geojson-vt-4e4d2a5dd1f2" ref="nofollow noopener noreferrer">文章</a>。</p>
<p>在渲染的这一步，每个瓦片的要素传入着色器中的坐标不是经纬度，也不是墨卡托的绝对坐标，而是相对于当前瓦片的坐标：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 墨卡托坐标 -> 相对瓦片坐标 [0, 8192]</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformPoint</span>(<span class="hljs-params">x, y, extent, z2, tx, ty</span>) </span>&#123;
  <span class="hljs-keyword">return</span> [
    <span class="hljs-built_in">Math</span>.round(extent * (x * z2 - tx)),
    <span class="hljs-built_in">Math</span>.round(extent * (y * z2 - ty))];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于使用的是相对瓦片坐标，GLSL 的 32 位精度足够用，因此精度问题也就不存在了。但是相应的，每次相机投影矩阵发生变化时，每个瓦片的投影矩阵也都需要重新计算。</p>
<p>一般缩放等级到 18 级以后，比如室内地图一般在 22 级，网格非常小，会导致切分时间非常长。考虑到用户体验，面对一组待渲染瓦片，Mapbox 按照距离屏幕中心的距离进行了排序，优先渲染中心瓦片：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 屏幕中点坐标</span>
<span class="hljs-keyword">const</span> centerCoord = MercatorCoordinate.fromLngLat(<span class="hljs-built_in">this</span>.center);
<span class="hljs-keyword">const</span> centerPoint = <span class="hljs-keyword">new</span> Point(numTiles * centerCoord.x - <span class="hljs-number">0.5</span>, numTiles * centerCoord.y - <span class="hljs-number">0.5</span>);

<span class="hljs-comment">// 覆盖瓦片数组按屏幕中心距离排序</span>
tiles.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> centerPoint.dist(a.canonical) - centerPoint.dist(b.canonical));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>概括而言，Mapbox 将墨卡托投影计算放在 CPU 中，传入着色器程序中的坐标是相对瓦片坐标，避免了 GLSL 的精度损失，并且通过要素简化、分片剪裁等操作大幅减少数据，有效控制了在 CPU 中的运算量。</p>
<h2 data-id="heading-5">Deck.GL 的做法</h2>
<p>Deck.GL 本身的定位是处理百万级别频繁变化的数据点，在 CPU 上进行墨卡托投影会严重影响性能。Deck.GL 将经纬度坐标直接传递给 GPU，在顶点着色器中进行转换。这样，必然会带来 JS 往 GLSL 中传数据时的精度损失问题。这些误差可能在地图范围大时还无法感知，在高缩放等级下就会造成肉眼可见的偏移，即“抖动”现象，并且随着缩放等级提升，误差将越来越大。</p>
<p>Deck.GL 曾测试过不同缩放等级在不同纬度下 Y 轴像素误差：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/209c2177820a47b3a57528efc65e560a~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">数据拆分为高位和低位</h3>
<p>为了解决这个问题，Deck.GL v3 版本中，引入了一种在 GLSL 中模拟 64 位双精度浮点数的方法，将数据拆分为高位和低位，每个数字的高位和低位都将在 GPU 中计算：</p>
<ul>
<li><code>highPart = Math.fround(x)</code></li>
<li><code>lowPart = x - highPart</code></li>
</ul>
<p>然后通过使用 32 位浮点数的级联运算来模拟 64 位的浮点运算。显然代价是巨大的 GPU 消耗。例如一个 64 位除法运算需要映射到 11 个 32 位运算，64 位的矩阵运算 (mat4 to vec4) 需要 1952 个 32 位运算。</p>
<p>使用这种方案的确实解决了精度损失引起的抖动问题，但模拟 64 位矩阵运算严重影响了着色器编译和解析的性能，同时也会增加 CPU 向 GPU 传递的数据带宽。一些性能低的显卡驱动程序无法兼容，就算兼容可能也要几秒钟的时间来编译它，导致显示卡顿。</p>
<h3 data-id="heading-7">偏移坐标系</h3>
<p>既想要保留高精度，又想避免过高的计算性能，在 v6.2 版本以后，Deck.GL 使用了一种以屏幕中心作为动态坐标原点的 <strong>"Offset Coords"</strong> 方案，解决了这个问题。</p>
<p>偏移坐标系的基本想法是，相近的两个坐标之差正好可以将高位抹去，只需要使用 32 位来存储差值，精度就完全足够了。因此我们需要选取一个固定点，用来计算差值。固定点选择视口中心点，计算偏移部分的过程应该在着色器中完成。因为每一帧的视口中心点的经纬度坐标都可能在改变，如果在 CPU 中每帧都重复进行偏移部分的矩阵运算，性能无法支撑。</p>
<p>下面的代码是根据当前坐标系，选择是进行处理正常经纬度还是处理经纬度的差值。</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-comment">// deck.gl/shaders/project.glsl</span>
<span class="hljs-function">vec4 <span class="hljs-title">project_position</span><span class="hljs-params">(vec4 position)</span> </span>&#123;
  <span class="hljs-comment">// 处理经纬度 offset</span>
  <span class="hljs-keyword">if</span> (project_uCoordinateSystem == COORDINATE_SYSTEM_LNGLAT_AUTO_OFFSET) &#123;
    <span class="hljs-comment">// 与视口中心点的偏移，在经纬度坐标下保留低位，32 位足够用</span>
    <span class="hljs-keyword">float</span> X = position.x - project_coordinate_origin.x;
    <span class="hljs-keyword">float</span> Y = position.y - project_coordinate_origin.y;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">project_offset_</span>(<span class="hljs-built_in">vec4</span>(X, Y, position.z, position.w));
  &#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 省略正常处理经纬度 -> 世界坐标</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">vec4</span>(
      <span class="hljs-built_in">project_mercator</span>(position.xy) * WORLD_SCALE * u_project_scale,
      <span class="hljs-built_in">project_scale</span>(position.z),
      position.w
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么怎么确定采用哪种计算方式呢？Deck.GL 设定了缩放等级的阈值，在正常和 Offset 两种坐标系之间切换，如果缩放等级大于 12，则需要计算出视口中心在经纬度坐标系下的坐标：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> LNGLAT_AUTO_OFFSET_ZOOM_THRESHOLD = <span class="hljs-number">12</span>;
<span class="hljs-keyword">if</span> (coordinateZoom < LNGLAT_AUTO_OFFSET_ZOOM_THRESHOLD) &#123;
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 使用 Offset 坐标，传入经纬度坐标系下的视口中心点</span>
  <span class="hljs-keyword">const</span> lng = <span class="hljs-built_in">Math</span>.fround(viewport.longitude);
  <span class="hljs-keyword">const</span> lat = <span class="hljs-built_in">Math</span>.fround(viewport.latitude);
  shaderCoordinateOrigin = [lng, lat];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此在顶点着色器中，最终像素空间坐标的计算结果可以拆分为两部分：世界坐标系偏移部分的矩阵运算和视口中心的投影结果：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-comment">// 处理 offset 和正常经纬度到世界坐标系转换</span>
vec4 project_pos = <span class="hljs-built_in">project_position</span>(<span class="hljs-built_in">vec4</span>(a_pos, <span class="hljs-number">0.0</span>, <span class="hljs-number">1.0</span>));
gl_Position = u_mvp_matrix * project_pos + u_viewport_center_projection;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>视口中心点的投影结果可以在 CPU 中的每一渲染帧中计算，偏移部分的矩阵运算则在着色器中完成，因此每一帧的计算只需要更新少量的 uniform，几乎可以在 CPU 或 GPU 上以零成本完成。</p>
<p>测试结果如下图，新的混合坐标系（黄色）具有与 64 位模式（红色）相当的精度，即使只使用了 32 位，而原先 32 位模式（蓝色）在相同缩放级别下出现了抖动。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c72db63127c44eb68283554add52a090~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">计算差值 —— 泰勒展开</h4>
<p>上述计算过程中，还有一个细节值得注意。如何根据世界坐标系下（经纬度）的差值，来估计墨卡托投影坐标系下的差值呢？在偏移坐标系场景下，<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f84b495f35b44157a3cb119cebf47d61~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"> 是动态的屏幕中心坐标，其他点与中心点的差值是 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e17f13fe2c3441068f25fcc8bede34b8~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">， <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef763f919b0e4441a40a3e968fcd71cd~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"> 函数是世界坐标系到偏移坐标系的转换函数。泰勒展开做的就是根据 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d87448da72d74846a59dd57354919b9f~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"> 处的值，结合 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3126a5744ee4e43aacb2fe296ed3e8c~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"> 函数的导数，可以对 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b7884ea9b8f4a9eac6c316182859281~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"> 函数任意点的值进行估计。泰勒展开的级数越多，代表模拟值的误差越小。</p>
<p>Web 墨卡托投影公式：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8943388c23c74ca1835c89e0f3a51a74~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6658d8f872774ebdadb16f59d14c62b8~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于 X 轴方向是线性的，可以使用线性估计：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e9969709fa14572a818f394126b3c92~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Y 轴方向是非线性的，可以使用泰勒二级展开：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30d76c360e6e42f4b8f010dd62544ad6~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 GLSL 中使用向量运算可以快速实现上述转换公式：其中 <code>u_pixels_per_degree</code> 对应 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62b6e341dcec483f821d3bbabfa12420~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">，而 <code>u_pixels_per_degree2</code> 对应 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f50edcf9e60e4412a68a86f03f7c87bc~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer">，<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eda18edeff704d16a7e4c8df316cfa81~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"> 的值通过 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0b111219f2940f894fda1f5e426928d~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"> 导数得到。</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-comment">// offset:[delta lng, delta lat]</span>
<span class="hljs-function">vec4 <span class="hljs-title">project_offset</span><span class="hljs-params">(vec4 offset)</span> </span>&#123;
    <span class="hljs-keyword">float</span> dy = offset.y;
    dy = <span class="hljs-built_in">clamp</span>(dy, <span class="hljs-number">-1.</span>, <span class="hljs-number">1.</span>);
    vec3 pixels_per_unit = u_pixels_per_degree + u_pixels_per_degree2 * dy;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">vec4</span>(offset.xyz * pixels_per_unit, offset.w);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">总结</h2>
<p>那么回到本文最开始的问题，去看热力图的源码就会发现原因。Deck.GL 的热力图模块在传递坐标时没有转换，传入着色器中的坐标精度出现了损失。通过上一节可以知道，Deck.GL  在不同版本中对精度损失问题有不同的策略，所以可能是在策略迁移过程中没有测试覆盖，导致了热力图模块仍存在问题。所以我主动提了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvisgl%2Fdeck.gl%2Fpull%2F5621%3Fw%3D1" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/visgl/deck.gl/pull/5621?w=1" ref="nofollow noopener noreferrer">issue</a>，并很快得到了解决。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3ca58043d0345b8a4edb1bbe3af00b7~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e5639db83594072aa6db8bb461d3c01~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用新版本的热力图之后，问题得到了解决：</p>
<p><img src="https://img.alicdn.com/imgextra/i1/O1CN01rvYURm1yqabiIdF30_!!6000000006630-1-tps-1774-1316.gif" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Ftimeless15%2Fembed%2FKKWbaGE" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/timeless15/embed/KKWbaGE" ref="nofollow noopener noreferrer">代码地址</a></strong></p>
<p>总结一下，WebGL 渲染高缩放等级下地理信息的抖动问题，有以下几个解决方法：</p>
<ul>
<li>
<p>使用相对于瓦片的坐标系，可以有效解决精度问题。但是当缩放程度越来越大时，瓦片分割的时间越来越长，而且如果要解决非瓦片数据的精度问题，还需要将其换算到相应的瓦片中。</p>
</li>
<li>
<p>将数据拆分为高位和低位，将一个 Float64Array 拆分为两个 Float32Array，虽然可以解决精度问题，但是代价是显著增加了内存开销和 GPU 计算。</p>
</li>
<li>
<p>偏移坐标系，相近的两个坐标之差正好可以将高位抹去，只需要使用 32 位来存储差值，精度就完全足够了。</p>
</li>
</ul>
<p>除了数据抖动之外，由于 WebGL 精度损失带来的现象还有 z-fighting，Z 缓冲区精度丢失问题，本文就不再赘述，有兴趣可以网上搜索相关资料了解。</p>
<h2 data-id="heading-10">参考资料</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2Fvis-gl%2Fhow-sometimes-assuming-the-earth-is-flat-helps-speed-up-rendering-in-deck-gl-c43b72fd6db4" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/vis-gl/how-sometimes-assuming-the-earth-is-flat-helps-speed-up-rendering-in-deck-gl-c43b72fd6db4" ref="nofollow noopener noreferrer">How (sometimes) assuming the Earth is "flat" helps speed up rendering in deck.gl</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.mapbox.com%2Frendering-big-geodata-on-the-fly-with-geojson-vt-4e4d2a5dd1f2" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.mapbox.com/rendering-big-geodata-on-the-fly-with-geojson-vt-4e4d2a5dd1f2" ref="nofollow noopener noreferrer">Rendering big geodata on the fly with GeoJSON-VT</a></li>
</ul>
<blockquote>
<p>作者：作者：ES2049 | timeless</p>
</blockquote>
<blockquote>
<p>文章可随意转载，但请保留此原文链接。</p>
<p>非常欢迎有激情的你加入 ES2049 Studio，简历请发送至 <a href="https://link.juejin.cn/?target=mailto%3Acaijun.hcj%40alibaba-inc.com" target="_blank" title="mailto:caijun.hcj@alibaba-inc.com" ref="nofollow noopener noreferrer">caijun.hcj@alibaba-inc.com</a> 。</p>
</blockquote></div>  
</div>
            