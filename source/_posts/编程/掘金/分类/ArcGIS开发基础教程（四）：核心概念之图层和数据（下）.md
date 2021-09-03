
---
title: 'ArcGIS开发基础教程（四）：核心概念之图层和数据（下）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6112'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 19:31:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=6112'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">核心概念之图层和数据（下）</h1>
<h2 data-id="heading-1">外部数据源图层介绍</h2>
<p>外部数据源的数据和文件是由<code>Layer</code>类的不同子类支持的。包括用于处理外部文件（如<code>CSV</code>或<code>GeoJSON</code>文件）或加载外部地图（如GeoQ，高德，Bing Maps）的特定类型的层。</p>
<p>常见的外部数据源图层有以下几种：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-CSVLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-CSVLayer.html" ref="nofollow noopener noreferrer"><code>CSVLayer</code></a>，数据来源为CSV文件，数据类型为点的矢量图形，支持的特性包括客户端地理处理、弹出窗口、支持2D和3D符号渲染。限制主要是可能根据要素个数，需要下载大量数据、</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-GeoJSONLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-GeoJSONLayer.html" ref="nofollow noopener noreferrer"><code>GeoJSONLayer</code></a>，数据来源为GeoJSON文件，数据类型为点、折线和多边形的矢量图形，主要用于从 GeoJSON 文件创建图层。限制是每个GeoJSON图层只能接受一个单一的几何体类型。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-OGCFeatureLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-OGCFeatureLayer.html" ref="nofollow noopener noreferrer"><code>OGCFeatureLayer</code></a>，数据类型包括点、线和多边形，支持渲染器、标签和弹出窗口等。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-WFSLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-WFSLayer.html" ref="nofollow noopener noreferrer"><code>WFSLayer</code></a>，数据来源为WFS 服务，数据类型支持点、多点、线和多边形，支持渲染器、标签、弹出窗口，但是限制数据必须是GeoJSON格式，只支持2.0.0版本。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-WMSLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-WMSLayer.html" ref="nofollow noopener noreferrer"><code>WMSLayer</code></a>，数据来源为WMS 服务，数据类型支持栅格数据导出的单个图像，支持OGC规范。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-WMTSLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-WMTSLayer.html" ref="nofollow noopener noreferrer"><code>WMTSLayer</code></a>，数据来源为WMTS切片服务，数据类型为切片图像，支持OGC规范。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-OpenStreetMapLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-OpenStreetMapLayer.html" ref="nofollow noopener noreferrer"><code>OpenStreetMapLayer</code></a>，数据来源为OSM切片服务，数据类型为切片图像，用来展示OpenStreetMap的切片地图。</li>
</ul>
<p>以上每个图层在初始化的时候都需要不同的属性，请参考每个图层类型文档了解更多。</p>
<p><em>创建CSVLayer的示例：</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> earthquakesLayer = <span class="hljs-keyword">new</span> CSVLayer(&#123;
  <span class="hljs-attr">url</span>: <span class="hljs-string">"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.csv"</span>,
  <span class="hljs-attr">copyright</span>: <span class="hljs-string">"USGS Earthquakes"</span>,
  <span class="hljs-attr">latitudeField</span>: <span class="hljs-string">"latitude"</span>, <span class="hljs-comment">// Defaults to "latitude"</span>
  <span class="hljs-attr">longitudeField</span>: <span class="hljs-string">"longitude"</span> <span class="hljs-comment">// Defaults to "longitude"</span>
&#125;);

map.layers.add(earthquakesLayer)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">底图介绍</h2>
<p>底图为地图提供地理背景。底图通常以切片地图的形式提供，以加快渲染。栅格底图要预先对底图切片。矢量底图以压缩的二进制格式提供数据，并在客户端上进行渲染。ArcGIS自带了一系列底图<sup id="user-content-fnref-1"><a href="https://juejin.cn/post/7003544745070821389#fn-1" class="footnote-ref" target="_blank" title="#fn-1">1</a></sup>。</p>
<p>自定义地图数据也可以通过ArcGIS Enterprise发布成矢量或栅格切片底图。</p>
<p>一个特定的<code>Map</code>对象的底图可以用<code>basemap</code>属性来控制，这个属性可以是一个字符串或一个<code>Basemap</code>对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> <span class="hljs-built_in">Map</span> = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(&#123;
  <span class="hljs-attr">basemap</span>: <span class="hljs-string">"streets-navigation-vector"</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">ArcGIS Server服务介绍</h2>
<p><code>MapImageLayer</code>用于显示ArcGIS Enterprise发布的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Frest%2Fservices-reference%2Fenterprise%2Fmap-service.htm" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/rest/services-reference/enterprise/map-service.htm" ref="nofollow noopener noreferrer">Map Service</a>。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Frest%2Fservices-reference%2Fenterprise%2Fmap-service.htm" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/rest/services-reference/enterprise/map-service.htm" ref="nofollow noopener noreferrer">Map Service</a>通常包含多个子图层和复杂的制图。地图服务将数据渲染成服务器端的图像，并在客户端显示。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> layer = <span class="hljs-keyword">new</span> MapImageLayer(&#123;
<span class="hljs-attr">url</span>: <span class="hljs-string">"https://sampleserver6.arcgisonline.com/arcgis/rest/services/USA/MapServer"</span>,
  <span class="hljs-attr">sublayers</span>: [
    &#123;
     <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
     <span class="hljs-attr">visible</span>: <span class="hljs-literal">true</span>
   &#125;, &#123;
     <span class="hljs-attr">id</span>: <span class="hljs-number">0</span>,
     <span class="hljs-attr">visible</span>: <span class="hljs-literal">true</span>,
     <span class="hljs-attr">definitionExpression</span>: <span class="hljs-string">"pop2000 > 100000"</span>
   &#125;
 ]
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Fjavascript%2Flatest%2Fapi-reference%2Fesri-layers-ImageryLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/javascript/latest/api-reference/esri-layers-ImageryLayer.html" ref="nofollow noopener noreferrer"><code>ImageryLayer</code></a>用于显示ArcGIS Enterprise发布的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com%2Frest%2Fservices-reference%2Fenterprise%2Fimage-service.htm" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com/rest/services-reference/enterprise/image-service.htm" ref="nofollow noopener noreferrer">Image Service</a> 的图像或其他栅格数据。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> layer = <span class="hljs-keyword">new</span> ImageryLayer(&#123;
  <span class="hljs-comment">// URL to the imagery service</span>
  <span class="hljs-attr">url</span>: <span class="hljs-string">"https://landsat2.arcgis.com/arcgis/rest/services/Landsat8_Views/ImageServer"</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<div class="footnotes">
<hr>
<ol>
<li id="user-content-fn-1">一些ArcGIS底图需要<code>API key</code>调用，另一部分则无需配置，直接调用，具体请查阅<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.arcgis.com" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.arcgis.com" ref="nofollow noopener noreferrer">ArcGIS开发者网站</a>。<a href="https://juejin.cn/post/7003544745070821389#fnref-1" class="footnote-backref" target="_blank" title="#fnref-1">↩</a></li>
</ol>
</div></div>  
</div>
            