
---
title: '使用 Echarts 实现热力图 & 迁徙图'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c4ca77fa21e469fa46a562d80b8fbeb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 06:40:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c4ca77fa21e469fa46a562d80b8fbeb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>迁徙图一般用于表示数据流向的信息，比如某个位置的数据流入或流出情况。热力图则表示数据的密集程度。最近在工作中的需求也涉及了 2 种图的实现，也踩了一些小坑。本文对这 2 种图的实现做了一个大体的梳理，作为后续相关需求实现的一个参考。</p>
<h2 data-id="heading-1">基础地图显示</h2>
<h3 data-id="heading-2">中国地图数据获取</h3>
<p>从 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdatav.aliyun.com%2Ftools%2Fatlas%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://datav.aliyun.com/tools/atlas/index.html" ref="nofollow noopener noreferrer">datav-地图选择器</a> 获取中国地图数据，存放在一个 js 文件中。</p>
<h3 data-id="heading-3">echarts 依赖安装以及全局引入</h3>
<p>echarts 版本为 4.7.0, 本文实现思路不适用于 5.x 版本。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> echarts <span class="hljs-keyword">from</span> <span class="hljs-string">"echarts"</span>;
Vue.prototype.$echarts = echarts;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">地图初始化</h3>
<h4 data-id="heading-5">模板及样式设置</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"cmap"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cmap"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-id">#cmap</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">地图设置</h4>
<p>设计稿地图外层会有一个绿色荧光效果，为了实现这个效果，我们初始设置时需要 2 个图层，一个是底图图层，用于显示外框荧光效果。一个是深色图层，用于凸显底图边框。最后通过图层叠加的方式来实现我们的想要的效果。<strong>PS: 底图可以使用不包含子区域的中国地图</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c4ca77fa21e469fa46a562d80b8fbeb~tplv-k3u1fbpfcp-watermark.image" alt="地图图层叠加方式" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不明白图层叠加方式的可以看上图。<strong>通过图层叠加方式会引入另外一个问题：当我们进行缩放时，各个图层缩放是不会同步的，导致图层显示错位。</strong></p>
<h3 data-id="heading-7">主要代码</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">getBaseOption</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    ..
    <span class="hljs-comment">// 底图</span>
    <span class="hljs-attr">geo</span>: &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">map</span>: <span class="hljs-string">"china"</span>,
      <span class="hljs-attr">zoom</span>: <span class="hljs-number">1.1</span>,
      ...
      <span class="hljs-attr">roam</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">itemStyle</span>: &#123;
        <span class="hljs-attr">normal</span>: &#123;
          <span class="hljs-attr">areaColor</span>: <span class="hljs-string">"rgba(0, 0, 0, 0)"</span>,
          <span class="hljs-attr">borderWidth</span>: <span class="hljs-number">8</span>, <span class="hljs-comment">//设置外层边框</span>
          <span class="hljs-attr">borderColor</span>: <span class="hljs-string">"#00FFD7"</span>,
          <span class="hljs-attr">shadowColor</span>: <span class="hljs-string">"rgba(63, 236, 209, 1)"</span>,
          <span class="hljs-attr">shadowBlur</span>: <span class="hljs-number">40</span>, <span class="hljs-comment">//地图外层光晕</span>
        &#125;,
      &#125;,
    &#125;,
    <span class="hljs-attr">series</span>: [
    <span class="hljs-comment">// 深色背景图层</span>
      &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">"map"</span>,
        <span class="hljs-attr">map</span>: <span class="hljs-string">"china"</span>,
        <span class="hljs-attr">zoom</span>: <span class="hljs-number">1.1</span>,
        <span class="hljs-attr">geoIndex</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">aspectScale</span>: <span class="hljs-number">0.75</span>, <span class="hljs-comment">// 长宽比, 默认值 0.75</span>
        <span class="hljs-attr">showLegendSymbol</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 存在legend时显示</span>
        ...
        <span class="hljs-attr">roam</span>: <span class="hljs-literal">true</span>,
        ...
    ],
  &#125;;
&#125;
    
<span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">option = <span class="hljs-literal">null</span></span>)</span> &#123;
  <span class="hljs-keyword">if</span> (!option) &#123;
    <span class="hljs-keyword">return</span>;
  &#125;

  <span class="hljs-keyword">const</span> _option = option;
  <span class="hljs-comment">//   registerMap 需要再 echarts init 之前执行</span>
  <span class="hljs-built_in">this</span>.$echarts.registerMap(<span class="hljs-string">"china"</span>, chinaNoIslands);
  <span class="hljs-built_in">this</span>.chart = echarts.init(<span class="hljs-built_in">this</span>.$refs.cmap);
  <span class="hljs-built_in">this</span>.chart.setOption(_option, <span class="hljs-literal">true</span>);

  <span class="hljs-built_in">this</span>.chart.off(<span class="hljs-string">"click"</span>);
  <span class="hljs-built_in">this</span>.chart.on(<span class="hljs-string">"click"</span>, <span class="hljs-function">(<span class="hljs-params">params</span>) =></span> &#123;&#125;);
&#125;

<span class="hljs-comment">// 结合 Vue 生命周期对地图进行处理</span>
<span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">this</span>.init(<span class="hljs-built_in">this</span>.getBaseOption());
&#125;,
<span class="hljs-function"><span class="hljs-title">beforeDestroy</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">this</span>.chart && <span class="hljs-built_in">this</span>.chart.dispose();
<span class="hljs-built_in">this</span>.chart = <span class="hljs-literal">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">热力图</h2>
<p>热力图实质上也是由若干不同大小(半径不同)的点组合而成的，所以格式比较简单，只需要落点的经纬度和数值即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> heatmapData = [
  &#123;
    <span class="hljs-attr">value</span>: [<span class="hljs-number">107.38</span>, <span class="hljs-number">23.19</span>, <span class="hljs-number">120</span>]
  &#125;,
  &#123;
    <span class="hljs-attr">value</span>: [<span class="hljs-number">111</span>, <span class="hljs-number">37.86</span>, <span class="hljs-number">40</span>]
  &#125;
  ...
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加一个 type 为 heatmap 类型的 series 即可，使用上并不复杂。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">getHeatmapOption</span>(<span class="hljs-params">heatmapData = []</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (heatmapData.length === <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span>;
  &#125;

  <span class="hljs-keyword">const</span> _option = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-built_in">this</span>.getBaseOption()));
  <span class="hljs-comment">//   添加热力图 series 数据</span>
  _option.series.push(&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"热力图"</span>,
    <span class="hljs-attr">type</span>: <span class="hljs-string">"heatmap"</span>,
    <span class="hljs-attr">coordinateSystem</span>: <span class="hljs-string">"geo"</span>,
    <span class="hljs-attr">data</span>: heatmapData,
  &#125;);

  _option.visualMap = [
    &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">left</span>: <span class="hljs-string">"10%"</span>,
      <span class="hljs-attr">bottom</span>: <span class="hljs-string">"5%"</span>,
      <span class="hljs-attr">max</span>: <span class="hljs-number">20</span>,
      <span class="hljs-attr">min</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">z</span>: <span class="hljs-number">999</span>,
      <span class="hljs-attr">calculable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">text</span>: [<span class="hljs-string">"高"</span>, <span class="hljs-string">"低"</span>],
      <span class="hljs-attr">inRange</span>: &#123;
        <span class="hljs-attr">color</span>: [<span class="hljs-string">"#0033FF"</span>, <span class="hljs-string">"#FFFF00"</span>, <span class="hljs-string">"#FF3333"</span>],
      &#125;,
      <span class="hljs-attr">textStyle</span>: &#123;
        <span class="hljs-attr">color</span>: <span class="hljs-string">"#fff"</span>,
      &#125;,
      <span class="hljs-attr">seriesIndex</span>: <span class="hljs-number">1</span>,
    &#125;,
  ];
  <span class="hljs-keyword">return</span> _option;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>visualMap 的 calculable 属性值设置为 true 时，可以通过进度条过滤某些范围内的热力点。效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1cb0bd73dd846e98bd4cc646cc6ac46~tplv-k3u1fbpfcp-watermark.image" alt="热力图" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">迁徙图</h2>
<h3 data-id="heading-10">数据格式</h3>
<p>我们需要一个城市经纬度的映射 Map，用于获取城市的经纬度。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> geoCoordMap = &#123;
    上海: [<span class="hljs-number">121.4648</span>, <span class="hljs-number">31.2891</span>],
    东莞: [<span class="hljs-number">113.8953</span>, <span class="hljs-number">22.901</span>],
    东营: [<span class="hljs-number">118.7073</span>, <span class="hljs-number">37.5513</span>],
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">流向状态</h3>
<p>迁徙图通常只有以下 2 种状态。</p>
<ol>
<li>流出状态，A 位置流向 B、C、D... 位置。格式如下：</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> inSZCityData = [
  [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"福州"</span> &#125;, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"深圳"</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">195</span> &#125;],
  [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"太原"</span> &#125;, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"深圳"</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">90</span> &#125;],
  [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"长春"</span> &#125;, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"深圳"</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">40</span> &#125;],
  ...
];
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>流入状态，B、C、D 等位置流向 A 位置。格式如下：</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> outSZCityData = [
  [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"深圳"</span> &#125;, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"福州"</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">95</span> &#125;],
  [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"深圳"</span> &#125;, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"太原"</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">90</span> &#125;],
  [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"深圳"</span> &#125;, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"长春"</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">80</span> &#125;],
  ...
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">数据处理</h3>
<p>根据指向数据中的城市名。匹配出经纬度，生成地图飞线可用的数据：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">const</span> _convertLinesData = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> _dataWithCoord = [];
    data.forEach(<span class="hljs-function">(<span class="hljs-params">direction</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> _fromCoord = geoCoordMap[direction[<span class="hljs-number">0</span>].name];
      <span class="hljs-keyword">const</span> _toCoord = geoCoordMap[direction[<span class="hljs-number">1</span>].name];

      <span class="hljs-keyword">if</span> (_fromCoord && _toCoord) &#123;
        _dataWithCoord.push([
          &#123;
            <span class="hljs-attr">coord</span>: _fromCoord,
          &#125;,
          &#123;
            <span class="hljs-attr">coord</span>: _toCoord,
            <span class="hljs-attr">value</span>: direction[<span class="hljs-number">1</span>].value,
          &#125;,
        ]);
      &#125;
    &#125;);
    <span class="hljs-keyword">return</span> _dataWithCoord;
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>散点图数据处理，根据流向状态生成数据，格式为 [经度. 纬度，数值]。效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f443866c1bec40118320cbd5e5097b7f~tplv-k3u1fbpfcp-watermark.image" alt="迁徙图.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">代码示例</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fembed%2Fecharts-relituliuxiangtu-d62g7%3Ffontsize%3D14%26hidenavigation%3D1%26theme%3Ddark%26view%3Dpreview" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/embed/echarts-relituliuxiangtu-d62g7?fontsize=14&hidenavigation=1&theme=dark&view=preview" ref="nofollow noopener noreferrer">echarts-热力图&迁徙图</a></p>
<h2 data-id="heading-14">参考</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fa805814077%2Farticle%2Fdetails%2F109748719" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/a805814077/article/details/109748719" ref="nofollow noopener noreferrer">Echarts 迁徙图与地图上绘制散点</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2FPY0312%2Farticle%2Fdetails%2F104585293" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/PY0312/article/details/104585293" ref="nofollow noopener noreferrer">Echarts 开发静态数据模拟实现迁徙图步骤详解</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.makeapie.com%2Fexplore.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.makeapie.com/explore.html" ref="nofollow noopener noreferrer">Echarts 示例网站</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fwebin%2Fpen%2FXWJeavR" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/webin/pen/XWJeavR" ref="nofollow noopener noreferrer">echarts-codepen-迁徙图示例</a></li>
</ul></div>  
</div>
            