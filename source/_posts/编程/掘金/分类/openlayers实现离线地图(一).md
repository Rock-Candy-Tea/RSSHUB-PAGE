
---
title: 'openlayers实现离线地图(一)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57405350ac0b4dd9b5b12a4acedddd56~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 07:14:48 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57405350ac0b4dd9b5b12a4acedddd56~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第1天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<p>基于内网的限制，所以需要实现一个离线版的地图。说到离线地图就要先说说在线的，平时使用的高德，腾讯等地图可以在很多软件中看到它的身影，像是打车软件内，一般会展示用户定位，路线，点位点功能。相关的Api也很完善，像是高德地图提供了很多的功能，但是在内网中就无法使用在线服务了，而openlayers是一个开源的js库用于在web浏览器展示地图。</p>
<h5 data-id="heading-1">离线地图实现原理</h5>
<p>从下图中其实可以看出，地图在缩放的时候其实是展示对应层级地点的图,所以要展示离线地图，首先需要获取到相应的地图资源，通常使用下载器下载对应格式的瓦片图。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57405350ac0b4dd9b5b12a4acedddd56~tplv-k3u1fbpfcp-watermark.image" alt="`(0B1D21YG@ZR&#125;B(WXIEM&#123;S.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>瓦片地图一般这几种类型：1.谷歌瓦片 2.原始瓦片 3.标准TMS瓦片 4.cGISServer瓦片 5.world wind 瓦片 6.水经注瓦片。</p>
<h5 data-id="heading-2">vue中使用openlayers</h5>
<p>官网提供了很多的案例，不过没有中文版的文档。</p>
<pre><code class="hljs language-js copyable" lang="js">    npm install ol
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化地图</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> tileLayer = <span class="hljs-keyword">new</span> TileLayer(&#123; <span class="hljs-attr">source</span>: <span class="hljs-keyword">new</span> XYZ(&#123; <span class="hljs-attr">url</span>: <span class="hljs-string">`tiles/&#123;z&#125;/&#123;x&#125;/&#123;y&#125;.png`</span> &#125;) &#125;) 指定瓦片图获取的路径
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(&#123;
        <span class="hljs-attr">layers</span>: [地图资源]
        <span class="hljs-attr">view</span>: <span class="hljs-keyword">new</span> View(&#123;
          <span class="hljs-attr">center</span>: fromLonLat([xxx,xxx],<span class="hljs-comment">// 地图中心点</span>
          <span class="hljs-attr">zoom</span>: <span class="hljs-number">14</span>, <span class="hljs-comment">// 缩放级别</span>
          <span class="hljs-attr">minZoom</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 最小缩放级别</span>
          <span class="hljs-attr">maxZoom</span>: <span class="hljs-number">18</span>, <span class="hljs-comment">// 最大缩放级别</span>
          <span class="hljs-attr">constrainResolution</span>: <span class="hljs-literal">true</span>
        &#125;),
        <span class="hljs-attr">target</span>: <span class="hljs-built_in">this</span>.$refs.olMap<span class="hljs-comment">// DOM容器</span>
      &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们可以初步得到一个地图实例，在使用中只需要提前下好相关的地图资源，并且传入对于的中心点经纬度就可以看到相应的地图，层级越大地图资源的体积越大，所以需要将地图资源存放在服务器上。</p></div>  
</div>
            