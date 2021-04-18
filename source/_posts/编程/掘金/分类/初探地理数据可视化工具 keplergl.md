
---
title: '初探地理数据可视化工具 kepler.gl'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f642c5da825140ec8e725893a28963c1~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 17 Apr 2021 20:11:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f642c5da825140ec8e725893a28963c1~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">1. 写在前面</h2>
<p>最近在看 Ubur 的 <code>Deck.gl</code>，间接性接触到它们开源的一个地理数据分析可视化工具 <code>kepler.gl</code>，之前也有看到，没有怎么玩过，恰好最近有点时间，来玩一玩这个地理数据可视化工具。</p>
<p>下面就以探索的方式展开简单玩玩 <code>kepler.gl</code>。</p>
<h3 data-id="heading-1">1.1 开源可视化库</h3>
<blockquote>
<p>可能工作的原因可能比较熟悉地理相关库，这里就举例经常看到用到的一些开源可视化库与工具。</p>
</blockquote>
<h3 data-id="heading-2">1.1.1 简单分类</h3>
<h4 data-id="heading-3">图表库</h4>
<ul>
<li>
<p>基础图表</p>
<ul>
<li>
<p><a href="https://github.com/apache/echarts" target="_blank" rel="nofollow noopener noreferrer">ECharts</a></p>
</li>
<li>
<p><a href="https://github.com/chartjs/Chart.js" target="_blank" rel="nofollow noopener noreferrer">Chart.js</a></p>
</li>
<li>
<p><a href="https://github.com/antvis/" target="_blank" rel="nofollow noopener noreferrer">AntV-G2/F2</a></p>
</li>
<li>
<p><a href="https://github.com/vega/vega" target="_blank" rel="nofollow noopener noreferrer">Vega</a></p>
</li>
<li>
<p><a href="https://github.com/rough-stuff/rough" target="_blank" rel="nofollow noopener noreferrer">Rough.js</a></p>
</li>
<li>
<p>...more</p>
</li>
</ul>
</li>
<li>
<p>关系图和流程图</p>
<ul>
<li><a href="https://github.com/mermaid-js/mermaid" target="_blank" rel="nofollow noopener noreferrer">mermaid</a></li>
</ul>
</li>
<li>
<p><a href="https://github.com/jacomyal/sigma.js" target="_blank" rel="nofollow noopener noreferrer">sigma.js</a></p>
<ul>
<li><a href="https://github.com/antvis/" target="_blank" rel="nofollow noopener noreferrer">AntV-G6/X6</a></li>
</ul>
</li>
<li>
<p><a href="https://github.com/dagrejs/dagre" target="_blank" rel="nofollow noopener noreferrer">dagre</a></p>
<ul>
<li>...more</li>
</ul>
</li>
</ul>
<h4 data-id="heading-4">地理库</h4>
<ul>
<li>
<p>2D</p>
</li>
<li>
<p><a href="https://github.com/Leaflet/Leaflet" target="_blank" rel="nofollow noopener noreferrer">Leaflet</a></p>
</li>
<li>
<p><a href="https://github.com/openlayers/openlayers" target="_blank" rel="nofollow noopener noreferrer">OpenLayers</a></p>
</li>
<li>
<p><a href="https://github.com/huiyan-fe/mapv" target="_blank" rel="nofollow noopener noreferrer">Mapv</a></p>
</li>
<li>
<p><a href="https://github.com/antvis/L7" target="_blank" rel="nofollow noopener noreferrer">AntV-L7</a></p>
</li>
<li>
<p>3D</p>
<ul>
<li><a href="https://github.com/mapbox/mapbox-gl-js" target="_blank" rel="nofollow noopener noreferrer">Mapbox GL JS</a></li>
</ul>
</li>
<li>
<p><a href="https://github.com/CesiumGS/cesium" target="_blank" rel="nofollow noopener noreferrer">Cesium</a></p>
<ul>
<li><a href="https://github.com/visgl/deck.gl" target="_blank" rel="nofollow noopener noreferrer">Deck.gl</a></li>
</ul>
</li>
<li>
<p><a href="https://github.com/maptalks/maptalks.js" target="_blank" rel="nofollow noopener noreferrer">maptalks.js</a></p>
<ul>
<li>...more</li>
</ul>
</li>
</ul>
<h4 data-id="heading-5">数据驱动框架</h4>
<ul>
<li><a href="https://github.com/d3/d3" target="_blank" rel="nofollow noopener noreferrer">D3</a></li>
<li><a href="https://github.com/d3/d3-geo" target="_blank" rel="nofollow noopener noreferrer">d3-geo</a>
<ul>
<li>...more</li>
</ul>
</li>
</ul>
<h4 data-id="heading-6">渲染库</h4>
<ul>
<li>
<p>2D</p>
<ul>
<li>
<p><a href="https://github.com/adobe-webplatform/Snap.svg" target="_blank" rel="nofollow noopener noreferrer">Snap.svg</a></p>
</li>
<li>
<p><a href="https://github.com/fabricjs/fabric.js" target="_blank" rel="nofollow noopener noreferrer">Fabric.js</a></p>
</li>
<li>
<p><a href="https://github.com/pixijs/pixi.js" target="_blank" rel="nofollow noopener noreferrer">PixiJS</a></p>
</li>
<li>
<p>...more</p>
</li>
</ul>
</li>
<li>
<p>2/3D</p>
<ul>
<li>
<p><a href="https://github.com/processing/p5.js" target="_blank" rel="nofollow noopener noreferrer">p5.js</a></p>
</li>
<li>
<p><a href="https://github.com/spritejs/spritejs" target="_blank" rel="nofollow noopener noreferrer">Sprite.js</a></p>
</li>
</ul>
</li>
<li>
<p>3D</p>
<ul>
<li>
<p><a href="https://github.com/mrdoob/three.js" target="_blank" rel="nofollow noopener noreferrer">Three.js</a></p>
</li>
<li>
<p><a href="https://github.com/BabylonJS/Babylon.js" target="_blank" rel="nofollow noopener noreferrer">Babylon.js</a></p>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-7">1.1.2 简单关系图</h3>
<p><img alt="开源的数据可视化库" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f642c5da825140ec8e725893a28963c1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">1.2 kepler.gl 了解</h3>
<blockquote>
<p>kepler.gl 是 Uber 开源，面向大规模数据集的强大开源地理数据分析工具，基于 <a href="https://github.com/visgl/deck.gl" target="_blank" rel="nofollow noopener noreferrer">deck.gl</a> 构建的 React 组件，高性能，用于大规模地理数据集的可视化分析探索。</p>
<p>--- <a href="https://github.com/keplergl/kepler.gl" target="_blank" rel="nofollow noopener noreferrer">kepler.gl</a></p>
</blockquote>
<p>提到 <code>deck.gl</code> 就自然要了解一下地理空间可视化框架 <a href="https://vis.gl/" target="_blank" rel="nofollow noopener noreferrer">Vis.gl</a> 的<a href="https://vis.gl/frameworks/" target="_blank" rel="nofollow noopener noreferrer">生态</a>：</p>
<ul>
<li><a href="https://deck.gl/" target="_blank" rel="nofollow noopener noreferrer">deck.gl</a> - A high-performance WebGL 2 rendering framework for big data visualizations that integrates perfectly with reactive applications.</li>
<li><a href="https://visgl.github.io/react-map-gl/" target="_blank" rel="nofollow noopener noreferrer">react-map-gl</a> - A React wrapper around Mapbox GL which works seamlessly with deck.gl.</li>
<li><a href="https://github.com/uber/react-vis" target="_blank" rel="nofollow noopener noreferrer">React-vis</a>- A composable, deeply customizable charting library</li>
<li><a href="https://luma.gl/" target="_blank" rel="nofollow noopener noreferrer">luma.gl</a> - A comprehensive set of WebGL 2 components targeting high-performance rendering and GPGPU computing.</li>
<li><a href="https://loaders.gl/" target="_blank" rel="nofollow noopener noreferrer">loaders.gl</a> - a suite of framework-independent loaders for file formats focused on visualization of big data, including point clouds, 3D geometries, images, geospatial formats as well as tabular data.</li>
<li><a href="https://nebula.gl/" target="_blank" rel="nofollow noopener noreferrer">nebula.gl</a> - High-Performance, 3D-enabled GeoJSON editing deck.gl and React</li>
</ul>
<p><img alt="Catalog" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b56e756be63b47c58c972d0b5456062b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>了解大致关系情况后，就搭建 kepler.gl，来玩一玩看看。</p>
<h2 data-id="heading-9">2. 搭建 kepler.gl</h2>
<h4 data-id="heading-10">2.1 生成项目、安装依赖</h4>
<p>生成项目使用 <a href="https://github.com/facebook/create-react-app" target="_blank" rel="nofollow noopener noreferrer">create-react-app</a> 脚手架工具</p>
<pre><code class="hljs language-bash copyable" lang="bash">npx create-react-app kepler.gl-taste
<span class="hljs-built_in">cd</span> kepler.gl-taste
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装 <code>kepler.gl</code>相关依赖，<code>kepler.gl</code> 使用 <a href="https://redux.js.org/" target="_blank" rel="nofollow noopener noreferrer">Redux</a> 管理组件状态，这里需要安装 <code>redux, react-redux</code></p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install --save kepler.gl redux react-redux react-virtualized styled-components
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装 <code>react-virtualized</code> 需要使用到 <code>AutoSizer</code> 组件，方便自动调整适配屏幕</p>
<h4 data-id="heading-11">2.2 添加相关代码</h4>
<p>使用 Redux 创建状态管理 <code>store.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore, combineReducers, applyMiddleware, compose &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-keyword">import</span> keplerGlReducer <span class="hljs-keyword">from</span> <span class="hljs-string">"kepler.gl/reducers"</span>;
<span class="hljs-keyword">import</span> &#123; enhanceReduxMiddleware &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"kepler.gl/middleware"</span>;

<span class="hljs-keyword">const</span> initialState = &#123;&#125;;

<span class="hljs-keyword">const</span> customizedKeplerGlReducer = keplerGlReducer.initialState(&#123;
<span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> customize initial state</span>
&#125;);

<span class="hljs-keyword">const</span> reducers = combineReducers(&#123;
  <span class="hljs-attr">keplerGl</span>: customizedKeplerGlReducer,
<span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> app reducer</span>
  <span class="hljs-comment">// app: appReducer</span>
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> middlewares = enhanceReduxMiddleware([
  <span class="hljs-comment">// Add other middlewares here</span>
]);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> enhancers = [applyMiddleware(...middlewares)];

<span class="hljs-comment">// using createStore</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(reducers, initialState, compose(...enhancers));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>挂载 KeplerGl 组件 <code>app.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> AutoSizer <span class="hljs-keyword">from</span> <span class="hljs-string">"react-virtualized/dist/commonjs/AutoSizer"</span>;
<span class="hljs-keyword">import</span> KeplerGl <span class="hljs-keyword">from</span> <span class="hljs-string">"kepler.gl"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"./App.css"</span>;

<span class="hljs-keyword">const</span> MAPBOX_TOKEN = process.env.REACT_APP_MAPBOX_TOKEN; <span class="hljs-comment">// eslint-disable-line</span>
<span class="hljs-keyword">const</span> MAPBOX_API_URL = <span class="hljs-string">"https://api.mapbox.com"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">AutoSizer</span>></span>
        &#123;(&#123; height, width &#125;) => (
          <span class="hljs-tag"><<span class="hljs-name">KeplerGl</span>
            <span class="hljs-attr">mapboxApiAccessToken</span>=<span class="hljs-string">&#123;MAPBOX_TOKEN&#125;</span>
            <span class="hljs-attr">id</span>=<span class="hljs-string">"map"</span>
            <span class="hljs-attr">width</span>=<span class="hljs-string">&#123;width&#125;</span>
            <span class="hljs-attr">height</span>=<span class="hljs-string">&#123;height&#125;</span>
            <span class="hljs-attr">mapboxApiUrl</span>=<span class="hljs-string">&#123;MAPBOX_API_URL&#125;</span>
          /></span>
        )&#125;
      <span class="hljs-tag"></<span class="hljs-name">AutoSizer</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>挂载 APP 组件，注入 store，<code>index.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom"</span>;
<span class="hljs-keyword">import</span> &#123; Provider &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-redux"</span>;
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">"./store"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"./index.css"</span>;

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多相关代码查看 <a href="https://github.com/liuvigongzuoshi/kepler.gl-taste" target="_blank" rel="nofollow noopener noreferrer">kepler.gl-taste</a></p>
<h4 data-id="heading-12">2.3 部署</h4>
<p>之前一般选择 Vercel 与 travis-ci 来持续集成部署，现在 <code>Github Actions</code> 也比较好用了，这里就使用 <code>Github Actions</code> 来做持续集成。</p>
<p><img alt="Github Actions" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b976325cd384cc780fb7f86f5e166bd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>新建工作流，配置 Actions <a href="https://github.com/liuvigongzuoshi/kepler.gl-taste/blob/main/.github/workflows/deploy-gh-page.yml" target="_blank" rel="nofollow noopener noreferrer">deploy-gh-page.yml</a></p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">name:</span> <span class="hljs-string">deploy</span> <span class="hljs-string">gh-pag</span> <span class="hljs-string">CI</span>

<span class="hljs-attr">on:</span>
  <span class="hljs-attr">push:</span>
    <span class="hljs-attr">branches:</span> [ <span class="hljs-string">main</span> ]
  <span class="hljs-attr">pull_request:</span>
    <span class="hljs-attr">branches:</span> [ <span class="hljs-string">main</span> ]

<span class="hljs-attr">jobs:</span>
  <span class="hljs-attr">deploy:</span>

    <span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-latest</span>

    <span class="hljs-attr">strategy:</span>
      <span class="hljs-attr">matrix:</span>
        <span class="hljs-attr">node-version:</span> [<span class="hljs-number">14.</span><span class="hljs-string">x</span>]

    <span class="hljs-attr">steps:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/checkout@v2</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Use</span> <span class="hljs-string">Node.js</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">matrix.node-version</span> <span class="hljs-string">&#125;&#125;</span>
      <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/setup-node@v2</span>
      <span class="hljs-attr">with:</span>
        <span class="hljs-attr">node-version:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">matrix.node-version</span> <span class="hljs-string">&#125;&#125;</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">run:</span> <span class="hljs-string">npm</span> <span class="hljs-string">install</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">run:</span> <span class="hljs-string">npm</span> <span class="hljs-string">run</span> <span class="hljs-string">build</span>
    
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">deploy</span>
      <span class="hljs-attr">uses:</span> <span class="hljs-string">peaceiris/actions-gh-pages@v3</span>
      <span class="hljs-attr">with:</span>
        <span class="hljs-attr">github_token:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.ACCESS_TOKEN</span> <span class="hljs-string">&#125;&#125;</span>
        <span class="hljs-attr">publish_dir:</span> <span class="hljs-string">./build</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>部署完成之后，访问部署后的<a href="https://liuvigongzuoshi.github.io/kepler.gl-taste/" target="_blank" rel="nofollow noopener noreferrer">地址</a>，下就开始来玩玩 kepler.gl</p>
<p><img alt="demo" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e68ddd9a262b45a9ac3deffbfe99af51~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">3. 使用 kepler.gl</h2>
<h3 data-id="heading-14">3.1 拾取要分析的数据</h3>
<p>这里就以带地理信息的天气数据来玩玩 <code>kepler.gl</code> 看看效果，数据就使用<a href="https://data.cma.cn/" target="_blank" rel="nofollow noopener noreferrer">国家气象科学数据中心</a>收集的地面站点数据。不过使用数据之前需要注册帐号，审核通过之后就可以使用了。</p>
<p><img alt="国家气象科学数据中心" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3aae9acbe8f0403190fd189dc7571d92~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里就以四川地面气象站逐小时观测资料为演示数据，选取要观测要素，数据检索完成后，申请数据下载。</p>
<p><img alt="数据检索" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fc79494209048d29c12b090b4c1761e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>审核通过后下载数据，数据格式如下图所示：</p>
<p><img alt="逐小时观测资料" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e48a24144714818a2187d684d6eccb0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看到数据只要站点编号，缺少站点信息数据，再次下载站点数据，数据格式如下图所示：</p>
<p><img alt="站点数据" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/709d8fc3da7143c999dab7620860dd35~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>下面进行数据合并处理</p>
<h3 data-id="heading-15">3.2 处理数据</h3>
<p>编写 <code>JS</code> 脚本处理两个 <code>CSV</code> 数据格式，将只要站点编号的文件注入站点信息，为了方便处理这里导出为 Json 文件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>)

<span class="hljs-keyword">const</span> parseToJson = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
<span class="hljs-keyword">const</span> lines = data.trim().split(<span class="hljs-regexp">/[\r?\n]&#123;1,2&#125;/</span>)
<span class="hljs-keyword">const</span> rows = lines.map(<span class="hljs-function">(<span class="hljs-params">line</span>) =></span> line.trim().split(<span class="hljs-string">','</span>))
<span class="hljs-keyword">const</span> headRow = rows.slice(<span class="hljs-number">0</span>, <span class="hljs-number">1</span>)[<span class="hljs-number">0</span>]
  <span class="hljs-keyword">const</span> bodyRows = rows.slice(<span class="hljs-number">1</span>)

  <span class="hljs-keyword">const</span> headMap = headRow.reduce(<span class="hljs-function">(<span class="hljs-params">pre, cur, index</span>) =></span> &#123;
      pre.set(index, cur)
      <span class="hljs-keyword">return</span> pre
    &#125;, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>())

  <span class="hljs-keyword">const</span> records = bodyRows.map(<span class="hljs-function">(<span class="hljs-params">row</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> initialValue = &#123;&#125;
      <span class="hljs-keyword">const</span> record = row.reduce(<span class="hljs-function">(<span class="hljs-params">pre, cur, index</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> key = headMap.get(index)

        <span class="hljs-keyword">if</span> (key) &#123;
          <span class="hljs-keyword">const</span> vaule = <span class="hljs-built_in">Number</span>(cur)
          <span class="hljs-keyword">if</span> (cur === <span class="hljs-string">''</span> || <span class="hljs-built_in">Number</span>.isNaN(vaule)) &#123;
            pre[key] = cur
          &#125; <span class="hljs-keyword">else</span> &#123;
            pre[key] = vaule
          &#125;
        &#125;
        <span class="hljs-keyword">return</span> pre
      &#125;, initialValue)
      <span class="hljs-keyword">return</span> record
    &#125;)

  <span class="hljs-keyword">return</span> records
&#125;

<span class="hljs-keyword">const</span> Station_Id_C = fs.readFileSync(<span class="hljs-string">'./Station_Id_C.csv'</span>).toString();
<span class="hljs-keyword">const</span> SrouceData = fs.readFileSync(<span class="hljs-string">'./SrouceData.csv'</span>).toString();

<span class="hljs-keyword">const</span> srouceData = parseToJson(SrouceData)
<span class="hljs-keyword">const</span> stationJson = parseToJson(Station_Id_C)

<span class="hljs-keyword">const</span> stationMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()

<span class="hljs-keyword">for</span> (item <span class="hljs-keyword">of</span> stationJson) &#123;
stationMap.set(item.Station_Id_C, item)
&#125;

<span class="hljs-keyword">for</span> (item <span class="hljs-keyword">of</span> srouceData) &#123;
<span class="hljs-keyword">const</span> station = stationMap.get(item.Station_Id_C)
item.Lat = station.Lat
item.Lon = station.Lon
item.Alt = station.Alt
item.Name = station.Name
&#125;

fs.writeFileSync(<span class="hljs-string">'result.json'</span>, <span class="hljs-built_in">JSON</span>.stringify(srouceData))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">3.3 使用数据</h3>
<h4 data-id="heading-17">3.3.1 操作示例</h4>
<p><img alt="站点数据分布 gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a7b36dbb31d49ba8a96bb21f681d8ef~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">3.3.2 各气象站点海拔高度分布</h4>
<p><img alt="各气象站点海拔高度分布" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5edc22fd6f654ec295f2e65611e003e5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-19">3.3.3 各气象站点中午气温分布</h4>
<p><img alt="各气象站点中午气温分布" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3576f545fe6349d78ed63d0ddfaa5308~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-20">3.3.4 各气象站点中午气压热力图</h4>
<p><img alt="各气象站点中午气压热力图" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80ee55bf604247ffafa37842620d083f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-21">3.3.5 各气象站点聚合分布图</h4>
<p><img alt="各气象站点聚合分布图" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/932871ca5903421ba94a5afd9084224d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-22">3.3.6 各气象站点栅格化最大风速三维视图</h4>
<p><img alt="各气象站点栅格化最大风速三维视图" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/679b146e1ab341ba815067d7dfcaa741~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-23">3.3.7 各气象站点体感温度三维视图</h4>
<p><img alt="各气象站点体感温度三维视图" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fea660353b834d39aa4915a191804171~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-24">4. 写在后面</h2>
<p>上面主要利用气象站点的气象数据并结合带有的经纬度的地理数据进行简单数据可视化分析查看，因点数据的局限性，没有尝试 <code>kepler.gl</code> 还支持的线、弧线、面、三维模型等可视化功能。如果对上面的功能感觉兴趣，可在官网查看更多炫酷的<a href="https://kepler.gl/" target="_blank" rel="nofollow noopener noreferrer">案例</a>：</p>















<table><thead><tr><th><a href="https://kepler.gl/demo/sfcontour" target="_blank" rel="nofollow noopener noreferrer">Polygon</a> - 海拔等高线</th><th><a href="https://kepler.gl/demo/nyc_census" target="_blank" rel="nofollow noopener noreferrer">Polygon</a> - 区域人口</th><th><a href="https://kepler.gl/demo/ukcommute" target="_blank" rel="nofollow noopener noreferrer">Arc</a> - 通勤起终点</th></tr></thead><tbody><tr><td><img alt="海拔等高线" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c4f547c75f14d83b8c206166f6d274e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td><img alt="区域人口" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75ed35fb023f412aa1e4e256d48f9369~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td><img alt="通勤起终点" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b85c67d0ef349a5954121edb06066cb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td></tr></tbody></table>
<p>除此之外也有供比较详细的<a href="https://docs.kepler.gl/docs/user-guides/j-get-started" target="_blank" rel="nofollow noopener noreferrer">用户手册</a>，对无编码经验的同学也能快速上手制作一份地理数据可视化解决方案。</p>
<h3 data-id="heading-25">参考资料</h3>
<ul>
<li><a href="https://docs.kepler.gl/docs/api-reference" target="_blank" rel="nofollow noopener noreferrer">kepler.gl api-reference</a></li>
<li><a href="https://www.zoo.team/article/use-git-actions" target="_blank" rel="nofollow noopener noreferrer">Github Actions 部署前端项目</a></li>
<li><a href="https://github.com/uber-common/vis-academy/tree/master/src/demos/kepler.gl" target="_blank" rel="nofollow noopener noreferrer">vis-academy</a></li>
<li><a href="https://data.cma.cn/" target="_blank" rel="nofollow noopener noreferrer">中国气象科学数据中心</a></li>
</ul>
<p>文中链接较多建议<a href="https://github.com/liuvigongzuoshi/blog/blob/master/README.md#%E5%8F%AF%E8%A7%86%E5%8C%96%E7%9B%B8%E5%85%B3" target="_blank" rel="nofollow noopener noreferrer">原文地址</a>查阅。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            