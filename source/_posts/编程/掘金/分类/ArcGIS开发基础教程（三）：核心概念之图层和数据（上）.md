
---
title: 'ArcGIS开发基础教程（三）：核心概念之图层和数据（上）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bf0c490950945439c5e81ab1028ed77~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 01:33:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bf0c490950945439c5e81ab1028ed77~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">核心概念之图层和数据（上）</h1>
<p><strong>图层</strong>是可在Map中使用的数据集合。图层数据可以在前端创建，或者由 ArcGIS Online 和 ArcGIS Enterprise 发布，或由外部服务器托管。</p>
<h2 data-id="heading-1">要素集合</h2>
<p><em>要素（feature）</em></p>
<p>: 要素是对地理位置或实体的记录。每个要素都包含为一种几何类型（点、折线或多边形）定义的空间坐标和存储其他信息的属性字段。</p>
<p><strong>图层</strong>通常用来管理和显示大量的要素集合。要素集合又分为结构化和非结构化<sup id="user-content-fnref-1"><a href="https://juejin.cn/post/7003267134855839774#fn-1" class="footnote-ref" target="_blank" title="#fn-1">1</a></sup>。如果要显示要素集合时，一般的做法是：</p>
<ul>
<li>
<p>如果数据是结构化的，使用<code>FeatureLayer</code>来显示数据</p>
</li>
<li>
<p>如果是非结构化的，用<code>GraphicsLayer</code>来显示数据</p>
</li>
</ul>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bf0c490950945439c5e81ab1028ed77~tplv-k3u1fbpfcp-watermark.image" alt="image-20210902145834267" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Map作为数据的容器，存放着各种不同类型的图层，图层又是由要素集合组成，每个要素都要包含<code>attributes</code>、<code>geometry</code>、<code>symbol</code>属性才能正常显示，<code>popupTemplate</code>为可选属性，定义了要素弹出窗口的显示内容。</p>
</blockquote>
<h2 data-id="heading-2">常见图层类型</h2>
<p>ArcGIS API for JavaScript有许多图层类，可用于访问和显示图层数据。所有的图层类都继承于<code>Layer</code>。使用哪种图层类取决于数据的格式和数据的存储位置。每个图层类还带有不同的方法。</p>
<p>常用图层类型介绍如下：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-FeatureLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-FeatureLayer.html" ref="nofollow noopener noreferrer"><code>FeatureLayer</code></a>，存储在ArcGIS Enterprise中的地理数据，主要用于显示、查询、过滤和编辑大量的地理要素。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-GraphicsLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-GraphicsLayer.html" ref="nofollow noopener noreferrer"><code>GraphicsLayer</code></a>，临时存储在内存中的地理数据，主要用于在地图上以图形或文字的形式显示少数地理要素。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-CSVLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-CSVLayer.html" ref="nofollow noopener noreferrer"><code>CSVLayer</code></a>/<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-KMLLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-KMLLayer.html" ref="nofollow noopener noreferrer"><code>KMLLayer</code></a>/<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-GeoJSONLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-GeoJSONLayer.html" ref="nofollow noopener noreferrer"><code>GeoJSONLayer</code></a>，存储在可通过网络访问的外部文件中的地理数据，主要用于将外部文件存储的地理数据显示为一个图层。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-TileLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-TileLayer.html" ref="nofollow noopener noreferrer"><code>TileLayer</code></a>/<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-VectorTileLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-VectorTileLayer.html" ref="nofollow noopener noreferrer"><code>VectorTileLayer</code></a>，数据以切片方案存储，以实现快速渲染，主要用于在地理背景中显示底图和其他切片数据集。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-MapImageLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-MapImageLayer.html" ref="nofollow noopener noreferrer"><code>MapImageLayer</code></a>，存储在ArcGIS Enterprise中并动态生成图片展示相应地理数据。主要用于展示由ArcGIS Server服务动态渲染的图层。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-ImageryLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-ImageryLayer.html" ref="nofollow noopener noreferrer"><code>ImageryLayer</code></a>，存储在ArcGIS Enterprise中的地理相关影像。主要用于展示卫星或其他影像数据。</li>
</ul>
<h2 data-id="heading-3">FeatureLayer介绍</h2>
<p><code>FeatureLayer</code>的数据源可以是内存中由应用程序加载的数据，也可以是从ArcGIS Enterprise上托管的REST API服务中请求的数据。在ArcGIS Enterprise中发布服务数据是首选方法，尤其是在访问和显示大量地理数据时。图层在客户端和服务器上都得到了高度优化，可以快速显示，并支持一些其他功能。</p>
<h3 data-id="heading-4">服务端构建图层</h3>
<p><code>FeatureLayer</code>支持从REST API服务返回的要素集合生成图层。这是访问和显示大型数据集的最有效方式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> layer = <span class="hljs-keyword">new</span> FeatureLayer(&#123;
  <span class="hljs-attr">url</span>: <span class="hljs-string">"https://services3.arcgis.com/GVgbJbqm8hXASVYi/arcgis/rest/services/Trailheads/FeatureServer/0"</span>
&#125;);

map.layers.add(layer);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">客户端构建图层</h3>
<p>通常情况下，图层数据是从ArcGIS Enterprise上托管的REST API服务加载的，但也可以直接从内存中的要素集合中创建一个<code>FeatureLayer</code>。</p>
<p><em>示例JSON数据：</em></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"places"</span>: [
    &#123;
      <span class="hljs-attr">"id"</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">"address"</span>: <span class="hljs-string">"200 N Spring St, Los Angeles, CA 90012"</span>,
      <span class="hljs-attr">"longitude"</span>: <span class="hljs-number">-118.24354</span>,
      <span class="hljs-attr">"latitude"</span>: <span class="hljs-number">34.05389</span>
    &#125;,
    &#123;
      <span class="hljs-attr">"id"</span>: <span class="hljs-number">2</span>,
      <span class="hljs-attr">"address"</span>: <span class="hljs-string">"419 N Fairfax Ave, Los Angeles, CA 90036"</span>,
      <span class="hljs-attr">"longitude"</span>: <span class="hljs-number">-118.31966</span>,
      <span class="hljs-attr">"latitude"</span>: <span class="hljs-number">34.13375</span>
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从示例JSON数据中创建一个<code>FeatureLayer</code>需要以下步骤：</p>
<ol>
<li>
<p>将<code>places</code>数组每一项转化为一个具有属性和几何的<code>Graphic</code>对象。<code>Graphic</code>对象主要包含<code>attributes</code>和<code>geometry</code>属性，分别负责设置要素的图形和属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> graphics = places.map(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">place</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Graphic(&#123;
    <span class="hljs-attr">attributes</span>: &#123;
      <span class="hljs-attr">ObjectId</span>: place.id,
      <span class="hljs-attr">address</span>: place.address
    &#125;,
    <span class="hljs-attr">geometry</span>: &#123;
      <span class="hljs-attr">longitude</span>: place.longitude,
      <span class="hljs-attr">latitude</span>: place.latitude
    &#125;
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>创建一个<code>FeatureLayer</code>对象，并指定<code>objectIdField</code>, <code>fields</code>, <code>renderer</code>, and <code>source</code>属性。<code>objectIdField</code>用于标识该要素的唯一地段名，可理解为指定哪个字段为<code>id</code>字段，<code>field</code>属性是一个对象数组，用于指定要素含有哪些字段及值类型，<code>renderer</code>属性用于设置要素的渲染器，<code>source</code>属性指定创建FeatureLayer的图形对象的集合。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> featureLayer = <span class="hljs-keyword">new</span> FeatureLayer(&#123;
  <span class="hljs-attr">source</span>: graphics,
  <span class="hljs-attr">renderer</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"simple"</span>,                    <span class="hljs-comment">// autocasts as new SimpleRenderer()</span>
    <span class="hljs-attr">symbol</span>: &#123;                          <span class="hljs-comment">// autocasts as new SimpleMarkerSymbol()</span>
      <span class="hljs-attr">type</span>: <span class="hljs-string">"simple-marker"</span>,
      <span class="hljs-attr">color</span>: <span class="hljs-string">"#102A44"</span>,
      <span class="hljs-attr">outline</span>: &#123;                       <span class="hljs-comment">// autocasts as new SimpleLineSymbol()</span>
        <span class="hljs-attr">color</span>: <span class="hljs-string">"#598DD8"</span>,
        <span class="hljs-attr">width</span>: <span class="hljs-number">2</span>
      &#125;
    &#125;
  &#125;,
  <span class="hljs-attr">objectIdField</span>: <span class="hljs-string">"ObjectID"</span>,           <span class="hljs-comment">// This must be defined when creating a layer from `Graphic` objects</span>
  <span class="hljs-attr">fields</span>: [
    &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">"ObjectID"</span>,
      <span class="hljs-attr">alias</span>: <span class="hljs-string">"ObjectID"</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">"oid"</span>
    &#125;,
    &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">"address"</span>,
      <span class="hljs-attr">alias</span>: <span class="hljs-string">"address"</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">"string"</span>
    &#125;
  ]
&#125;);

map.layers.add(featureLayer);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-6">GraphicsLayer介绍</h2>
<p>Graphics 通常用于向地图临时添加文本、和具有不同类型的图形。创建graphics layer的最简单方法是将 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-Graphic.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-Graphic.html" ref="nofollow noopener noreferrer"><code>Graphic</code></a> 对象创建为一个数组，并将这个数组传递给一个新的 <code>GraphicsLayer</code> 对象的 <code>graphics</code> 属性。</p>
<blockquote>
<p>可以将graphic理解为单个要素，所以需要<code>attributes</code>、<code>geometry</code>、<code>symbol</code>属性才能正常显示。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> pointGraphic = <span class="hljs-keyword">new</span> Graphic(&#123;
  <span class="hljs-attr">attributes</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"LA City Hall"</span>,
    <span class="hljs-attr">address</span>: <span class="hljs-string">"200 N Spring St, Los Angeles, CA 90012"</span>
  &#125;,
  <span class="hljs-attr">geometry</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"point"</span>,                     <span class="hljs-comment">// autocasts as new Point()</span>
    <span class="hljs-attr">longitude</span>: -<span class="hljs-number">118.24354</span>,
    <span class="hljs-attr">latitude</span>: <span class="hljs-number">34.05389</span>
  &#125;,
  <span class="hljs-attr">symbol</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"simple-marker"</span>,             <span class="hljs-comment">// autocasts as new SimpleMarkerSymbol()</span>
    <span class="hljs-attr">color</span>: [ <span class="hljs-number">226</span>, <span class="hljs-number">119</span>, <span class="hljs-number">40</span> ],
    <span class="hljs-attr">outline</span>: &#123;                         <span class="hljs-comment">// autocasts as SimpleLineSymbol()</span>
      <span class="hljs-attr">color</span>: [ <span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span> ],
      <span class="hljs-attr">width</span>: <span class="hljs-number">2</span>
    &#125;
  &#125;
&#125;);

<span class="hljs-keyword">const</span> graphicsLayer = <span class="hljs-keyword">new</span> GraphicsLayer(&#123;
  <span class="hljs-attr">graphics</span>: [ pointGraphic ]
&#125;);

map.layers.add(graphicsLayer);
<span class="copy-code-btn">复制代码</span></code></pre>
<div class="footnotes">
<hr>
<ol>
<li id="user-content-fn-1">如果每个要素都有相同的几何类型和相同的属性名，则是结构化的。反之，则是非结构化的。<a href="https://juejin.cn/post/7003267134855839774#fnref-1" class="footnote-backref" target="_blank" title="#fnref-1">↩</a></li>
</ol>
</div></div>  
</div>
            