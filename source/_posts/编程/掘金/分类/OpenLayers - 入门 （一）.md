
---
title: 'OpenLayers - 入门 （一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85e07c27cfb94c059a98abf84f96a7a5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 21:18:45 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85e07c27cfb94c059a98abf84f96a7a5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与 8 月更文挑战的第 11 天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8 月更文挑战</a></strong></p>
<h2 data-id="heading-0">简介</h2>
<p>在地图项目的开发中，有时候也需要不依赖于任何公司来开发项目。那么前端地图展示，图层控制就需要一个开源的框架来开发，我一下就相中了<code>OpenLayers</code>（其实是公司要求）。</p>
<h2 data-id="heading-1">什么是 OpenLayers</h2>
<ul>
<li>这里使用的是 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fopenlayers.org%2Fdownload%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://openlayers.org/download/" ref="nofollow noopener noreferrer">OpenLayers v6.6.1</a></strong></li>
</ul>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fopenlayers.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://openlayers.org/" ref="nofollow noopener noreferrer"><code>OpenLayers</code></a> 是一个开源的<code>JavaScript类库</code>，主要是用于开发<code>Web GIS</code>客户端。要想完整的开发一个地图项目，还需要后端提供地图瓦片的服务，如可以使用<code>geoserver</code>等。</li>
<li>它可以轻松地在任何网页中放置动态地图。且能支持移动设备。</li>
<li>它可以显示从任何来源加载的地图图块、矢量数据和标记。</li>
<li>它易于定制和扩展，能通过简单的 CSS 设置地图控件的样式。使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fopenlayers.org%2F3rd-party%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://openlayers.org/3rd-party/" ref="nofollow noopener noreferrer">第三方库</a>来自定义和扩展功能。</li>
</ol>
<h2 data-id="heading-2">基础概念</h2>
<p>一个新的框架，详细了解基础概念，有助于我们快速开发。</p>
<h3 data-id="heading-3">Map</h3>
<p><code>OpenLayers</code>的核心组件是<code>map (ol/Map)</code>，<code>Map</code>就是地图。它被呈现到目标容器中（例如，<code>div</code>元素）。可以在构造时配置所有映射属性，也可以使用<code>setTarget()</code>来设置。<code>Layer</code>、<code>View</code>都是定义在<code>ol/Map</code>下。</p>
<h3 data-id="heading-4">View</h3>
<p>因为地图不对地图的中心、缩放级别和投影等内容负责。 所以这些功能都是有<code>View</code>来实现的。它的定义在<code>ol/View</code>下。<br>
<code>View</code>有一个<code>projection</code>(投影)。投影确定中心的坐标系和地图分辨率计算的单位，默认使用墨卡托投影<code>EPSG:3857</code>。<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.pianshen.com%2Farticle%2F7987865406%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.pianshen.com/article/7987865406/" ref="nofollow noopener noreferrer">坐标系、投影、EPSG:4326、EPSG:3857</a></p>
<h3 data-id="heading-5">Source</h3>
<p><code>Source</code> 就是图层数据的来源，数据格式可以是 XYZ、WMS 或 WMTS 等 OGC 源以及 GeoJSON 或 KML 等格式的矢量数据。它的定义在<code>ol/source</code>下。</p>
<h3 data-id="heading-6">Layer</h3>
<p><code>Layer</code>表示一个图层。在项目的开发中我们的操作都是在一个个图层上绘制，然后<code>OpenLayers</code>根据层级把图层一层层的绘制上去。
它定义在<code>ol/layer</code>下，有四种基本类型的层。</p>
<ul>
<li><code>ol/layer/Tile</code> - 渲染在网格中提供平铺图像的源，这些网格按特定分辨率的缩放级别组织。栅格图层。</li>
<li><code>ol/layer/Image</code> - 渲染以任意范围和分辨率提供地图图像的源。栅格图层。</li>
<li><code>ol/layer/Vector</code> - 在客户端呈现矢量数据。矢量图层。</li>
<li><code>ol/layer/VectorTile</code> - 渲染作为矢量切片提供的数据。矢量图层。</li>
</ul>
<h3 data-id="heading-7">control</h3>
<p><code>control</code>表示控件，使用按钮来控制地图。
在<code>ol/control</code>下，定义了一些内置的控件。如全屏、旋转、缩放、小地图等。<br>
在内置控件不满足需求时也需要我们自定义控件。</p>
<h3 data-id="heading-8">interaction</h3>
<p><code>interaction</code>交互事件，添加地图和用户的交互事件。<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fopenlayers.org%2Fen%2Flatest%2Fapidoc%2Fmodule-ol_interaction.html" target="_blank" rel="nofollow noopener noreferrer" title="https://openlayers.org/en/latest/apidoc/module-ol_interaction.html" ref="nofollow noopener noreferrer">api 文档</a></p>
<h2 data-id="heading-9">开始使用</h2>
<ul>
<li>引入<code>OpenLayers</code></li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.6.1/css/ol.css"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.6.1/build/ol.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>设置元素</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.map</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">500px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"map"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"map"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>创建地图</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> ol.Map(&#123;
  <span class="hljs-attr">target</span>: <span class="hljs-string">'map'</span>,
  <span class="hljs-attr">layers</span>: [
    <span class="hljs-keyword">new</span> ol.layer.Tile(&#123;
      <span class="hljs-comment">// 使用高度瓦片图</span>
      <span class="hljs-attr">source</span>: <span class="hljs-keyword">new</span> ol.source.XYZ(&#123;
            <span class="hljs-attr">url</span>: <span class="hljs-string">'https://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x=&#123;x&#125;&y=&#123;y&#125;&z=&#123;z&#125;'</span>
          &#125;)
    &#125;)
  ],
  <span class="hljs-attr">view</span>: <span class="hljs-keyword">new</span> ol.View(&#123;
    <span class="hljs-attr">center</span>: ol.proj.fromLonLat([<span class="hljs-number">37.41</span>, <span class="hljs-number">8.82</span>]),
    <span class="hljs-attr">zoom</span>: <span class="hljs-number">4</span>
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>通过<code>new ol.Map(&#123; ... &#125;);</code>加载地图对象，通过<code>target</code>参数绑定元素节点。</li>
<li>通过<code>layers</code>参数定义地图中可用的图层列表。后面图层覆盖前面的图层。</li>
<li>通过<code>View</code>参数指定地图的中心、分辨率和旋转。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85e07c27cfb94c059a98abf84f96a7a5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>OpenLayers</code>开发可以简单的理解为，把整个地图看作一个容器 <code>Map</code>。把根据<code>Layer</code>规则生成的图层加入地图中。在这基础上使用 <code>View、Control、Interaction</code>控制地图。</li>
</ul></div>  
</div>
            