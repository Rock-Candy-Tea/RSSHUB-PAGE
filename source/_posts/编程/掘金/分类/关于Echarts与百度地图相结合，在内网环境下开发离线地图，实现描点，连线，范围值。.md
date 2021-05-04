
---
title: '关于Echarts与百度地图相结合，在内网环境下开发离线地图，实现描点，连线，范围值。'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79ca286a498045bbbbee54e2e4defcab~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 03 May 2021 20:02:27 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79ca286a498045bbbbee54e2e4defcab~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79ca286a498045bbbbee54e2e4defcab~tplv-k3u1fbpfcp-watermark.image" alt="离线地图引入3要素.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">引言</h2>
<p>前端er必备技能之一：地图开发。也不能说是开发，只是拿百度地图大牛们开发好的插件，做一个简单使用。建议阅读本文前，先尝试一下在线地图的开发，如：<a href="http://lbsyun.baidu.com/index.php?title=%E9%A6%96%E9%A1%B5" target="_blank" rel="nofollow noopener noreferrer">申请AK码</a>，<a href="http://lbsyun.baidu.com/cms/jsapi/reference/jsapi_webgl_1_0.html#a0b0" target="_blank" rel="nofollow noopener noreferrer">了解百度地图相关api</a>，<a href="https://echarts.apache.org/zh/option.html#series-map" target="_blank" rel="nofollow noopener noreferrer">Echarts中地图模块</a>。</p>
<h2 data-id="heading-1">效果预览</h2>
<p>去年在JS中做的离线版，为了兼容IE，使用的老版本Echarts:
<a href="https://info.swufe.edu.cn/netinfo/echarts/doc/example.html" target="_blank" rel="nofollow noopener noreferrer">需要兼容ie的可以使用这个版本的Echarts</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b07bd3e36f641bb9188f7dd2ba8e42e~tplv-k3u1fbpfcp-watermark.image" alt="map_js.gif" loading="lazy" referrerpolicy="no-referrer">
这是最近做的vue版:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6118447d77f3421982707d231315a2e1~tplv-k3u1fbpfcp-watermark.image" alt="map_vue.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">实现方式</h2>
<h3 data-id="heading-3">1.引入文件</h3>
<p>我的实现方式是需要4样东西：echarts，apiv1.3.min.js，modules_ditu.js，瓦片图。</p>
<p>地图开发最关键的一步就是：如何引入百度地图的api文件。
在线地图中的引用很简单，只需要script引入一个url即可，即可引入相关API的文件。<code><script type="text/javascript" src="http://api.map.baidu.com/api?v=2.0&ak=你的AK码"></script></code></p>
<p>那么离线地图也是一样的思路，我们只需要引入api相关的JS文件即可。引入文件步骤（以需要的apiv1.3.min为例）。<a href="https://blog.csdn.net/Jason_nuc/article/details/51175523?t=1495448114844" target="_blank" rel="nofollow noopener noreferrer">我之前是学习的这位博主的博客</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce65433026da417e9caad74617963fa3~tplv-k3u1fbpfcp-watermark.image" alt="地图文件获取.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在离线地图中，我们需要引入的JS文件只有2个JS，文中说的那个CSS可以不引，无影响。</p>
<p>最后就是我们的核心=>瓦片图的获取。离线地图就是靠JS中动态拼接路径，来调取瓦片图，以此来实现的可视化地图。我们用的瓦片图只有5个层级，但是图片数量也已经有2W多张了，</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55a63f27b2aa42e98e12bd63ee5019a5~tplv-k3u1fbpfcp-watermark.image" alt="瓦片图.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">2.文件中路径改动</h3>
<p>文件引入之后呢，我们还需要根据我们的文件存放位置，来调整一下两个JS中的路径。以我的这一版api--.js为例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/699f6399ae5c425d8f3d25b5563fdf60~tplv-k3u1fbpfcp-watermark.image" alt="瓦片图文件路径.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20fe0bedf65d42c2ad1f4156a08251d7~tplv-k3u1fbpfcp-watermark.image" alt="2.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">3.引入文件出现的bug</h3>
<h4 data-id="heading-6">文本无法选中</h4>
<p>在引入地图相关文件的该页面中，会出现文本无法选中，使得用户无法复制。这个是因为modules_ditu.js引起的，因为有的modules--.js版本中，会加<code>onselectstart = fasle 禁止选中文字</code>。然后呢，我试着在源码中，改变其值，反正是木得效果，没起作用。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6207347cfccb4e9785e8307b24671fbf~tplv-k3u1fbpfcp-watermark.image" alt="3.jpg" loading="lazy" referrerpolicy="no-referrer">
最后的解决方法，百度的是，重新找几个老版本的modules--.js文件替上去即可。</p>
<h2 data-id="heading-7">vue中的代码实现</h2>
<h3 data-id="heading-8">1.相关代码</h3>
<p>index.html中引入</p>
<p>注：脚手架创建的项目中，因为webpack中打包静态文件路径默认是在static中，所以我们的静态文件也要放在static下。</p>
<pre><code class="hljs language-js copyable" lang="js"><script type=<span class="hljs-string">"text/javascript"</span> src=<span class="hljs-string">"./static/map/js/apiv1.3.min.js"</span>></script>
modules_ditu不用在这引入，因为该JS是在api---.js中有引入，无需重复引入。
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"ip_query query clearfix"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"map"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">geo_data</span>: &#123;
        <span class="hljs-attr">city</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">coord</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">radius</span>: <span class="hljs-literal">null</span>
      &#125;
    &#125;;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> this_ = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">let</span> ipLocation = &#123;
      <span class="hljs-attr">city</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">coord</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">radius</span>: <span class="hljs-number">600</span>
    &#125;;
    <span class="hljs-comment">// 赋值</span>
    <span class="hljs-built_in">this</span>.geo_data = &#123;
      <span class="hljs-attr">city</span>: ipLocation.city ? ipLocation.city : <span class="hljs-string">"北京"</span>,
      <span class="hljs-attr">coord</span>: [
        ipLocation.lngwgs ? ipLocation.lngwgs : <span class="hljs-number">116.397469</span>,
        ipLocation.latwgs ? ipLocation.latwgs : <span class="hljs-number">39.908821</span>
      ],
      <span class="hljs-attr">radius</span>: ipLocation.radius
    &#125;;
    <span class="hljs-comment">// 绘制地图</span>
    <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> IpMap_ec = <span class="hljs-built_in">this</span>.echarts.init(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"map"</span>));
      <span class="hljs-keyword">let</span> map_render = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">params, api</span>) </span>&#123;
        <span class="hljs-keyword">let</span> x_y = api.coord(this_.geo_data.coord);
        <span class="hljs-keyword">let</span> r = api.size([<span class="hljs-number">0</span>, <span class="hljs-number">1</span>])[<span class="hljs-number">1</span>] * (this_.geo_data.radius / <span class="hljs-number">80</span>);
        <span class="hljs-keyword">let</span> color = <span class="hljs-string">"#A7C2DF"</span>;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">"circle"</span>,
          <span class="hljs-attr">shape</span>: &#123;
            <span class="hljs-attr">cx</span>: x_y[<span class="hljs-number">0</span>],
            <span class="hljs-attr">cy</span>: x_y[<span class="hljs-number">1</span>],
            <span class="hljs-attr">r</span>: r
          &#125;,
          <span class="hljs-attr">style</span>: api.style(&#123;
            <span class="hljs-attr">fill</span>: color,
            <span class="hljs-attr">stroke</span>: this_.echarts.color.lift(color)
          &#125;)
        &#125;;
      &#125;;
      IpMap_ec.setOption(
        &#123;
          <span class="hljs-attr">bmap</span>: &#123;
            <span class="hljs-attr">center</span>: <span class="hljs-built_in">this</span>.geo_data.coord,
            <span class="hljs-attr">zoom</span>: <span class="hljs-number">5</span>,
            <span class="hljs-attr">roam</span>: <span class="hljs-string">"scale"</span>
          &#125;,
          <span class="hljs-attr">series</span>: [
            &#123;
              <span class="hljs-attr">type</span>: <span class="hljs-string">"scatter"</span>,
              <span class="hljs-attr">coordinateSystem</span>: <span class="hljs-string">"bmap"</span>,
              <span class="hljs-attr">symbol</span>: <span class="hljs-string">"circle"</span>,
              <span class="hljs-attr">symbolSize</span>: <span class="hljs-number">30</span>,
              <span class="hljs-attr">data</span>: [
                &#123;
                  <span class="hljs-attr">name</span>: <span class="hljs-built_in">this</span>.geo_data.city,
                  <span class="hljs-attr">value</span>: <span class="hljs-built_in">this</span>.geo_data.coord
                &#125;
              ]
            &#125;,
            &#123;
              <span class="hljs-attr">type</span>: <span class="hljs-string">"custom"</span>,
              <span class="hljs-attr">coordinateSystem</span>: <span class="hljs-string">"bmap"</span>,
              <span class="hljs-attr">renderItem</span>: map_render,
              <span class="hljs-attr">itemStyle</span>: &#123;
                <span class="hljs-attr">opacity</span>: <span class="hljs-number">0.5</span>
              &#125;,
              <span class="hljs-attr">animation</span>: <span class="hljs-literal">false</span>,
              <span class="hljs-attr">silent</span>: <span class="hljs-literal">true</span>,
              <span class="hljs-attr">data</span>: [<span class="hljs-number">0</span>],
              <span class="hljs-attr">z</span>: -<span class="hljs-number">10</span>
            &#125;
          ]
        &#125;,
        <span class="hljs-literal">true</span>
      );
      <span class="hljs-comment">// map API事件相关</span>
      <span class="hljs-keyword">let</span> bmap = IpMap_ec.getModel()
        .getComponent(<span class="hljs-string">"bmap"</span>)
        .getBMap();
      bmap.setMinZoom(<span class="hljs-number">3</span>);
      bmap.setMaxZoom(<span class="hljs-number">7</span>);
      <span class="hljs-comment">// 解决滚动触发2次zoomstart时的情形</span>
      <span class="hljs-keyword">let</span> zoom_arr = [];
      bmap.addEventListener(<span class="hljs-string">"zoomstart"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> zoom_level = bmap.getZoom();
        zoom_arr.push(zoom_level);
      &#125;);
      <span class="hljs-keyword">let</span> zoom_map = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> point = <span class="hljs-keyword">new</span> BMap.Point(
          this_.geo_data.coord[<span class="hljs-number">0</span>],
          this_.geo_data.coord[<span class="hljs-number">1</span>]
        );
        <span class="hljs-keyword">if</span> (zoom_arr.length > <span class="hljs-number">1</span>) &#123;
          <span class="hljs-keyword">let</span> end_level = bmap.getZoom();
          <span class="hljs-keyword">let</span> differ = end_level - zoom_arr[<span class="hljs-number">0</span>];
          <span class="hljs-keyword">let</span> res_level = differ > <span class="hljs-number">0</span> ? zoom_arr[<span class="hljs-number">0</span>] + differ - <span class="hljs-number">1</span> : zoom_arr[<span class="hljs-number">0</span>] + differ + <span class="hljs-number">1</span>;
          zoom_arr = [];
          bmap.centerAndZoom(point, res_level);
        &#125; <span class="hljs-keyword">else</span> &#123;
          bmap.centerAndZoom(point, bmap.getZoom());
          zoom_arr = [];
        &#125;
      &#125;;
      <span class="hljs-comment">// 缩扩固定中心点</span>
      bmap.addEventListener(<span class="hljs-string">"zoomend"</span>, zoom_map);
    &#125;);
  &#125;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"stylus"</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.ip_query</span> &#123;
  <span class="hljs-selector-id">#map</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">900px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">600px</span>;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">30px</span> auto;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef0373a2ed1049478caa82a42189fe73~tplv-k3u1fbpfcp-watermark.image" alt="地图_test.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">2.相关bug或优化点</h3>
<h4 data-id="heading-10">1.如果2次或多次实例化echarts，滑轮滚动一次，缩扩2个级别</h4>
<p>因为我做的这一版地图主要是运用到IP查询中，可能会出现查询失败，查询时的input框及查询内容的动态过渡效果的实现，然后我这里是简单粗暴的多次实例化echarts来达到效果。这样会出现一个问题，就是多次搜索IP，地图中缩扩时会出现<strong>滑轮滚动一次，缩扩2个级别</strong>，然后做了个判断，来手动让他恢复缩放正常情况下。</p>
<pre><code class="copyable">      // 解决滚动触发2次zoomstart时的情形
      let zoom_arr = [];
      bmap.addEventListener("zoomstart", function() &#123;
        let zoom_level = bmap.getZoom();
        zoom_arr.push(zoom_level);
      &#125;);
      let zoom_map = function() &#123;
        let point = new BMap.Point(
          this_.geo_data.coord[0],
          this_.geo_data.coord[1]
        );
        if (zoom_arr.length > 1) &#123;
          let end_level = bmap.getZoom();
          let differ = end_level - zoom_arr[0];
          let res_level;
          if (differ > 0) &#123;
            res_level = zoom_arr[0] + differ - 1;
          &#125; else &#123;
            res_level = zoom_arr[0] + differ + 1;
          &#125;
          zoom_arr = [];
          bmap.centerAndZoom(point, res_level);
        &#125; else &#123;
          bmap.centerAndZoom(point, bmap.getZoom());
          zoom_arr = [];
        &#125;
      &#125;;
      // 缩扩固定中心点
      bmap.addEventListener("zoomend", zoom_map);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">2.拖拽出边界时的优化</h4>
<p>地图实质上就是瓦片图的拼接，但是离线地图受制于瓦片图的完善度，拖拽出边界后，我们实质上是没有图片可以引了。所以，会出现灰边（咋们的背景色），体验不好。</p>
<p>最好的效果就是：用户拖拽至边界时，禁用拖拽。往回拖时，再启用拖拽。或者 是做成球形的效果，拖拽至左侧边界时，出现右侧边界，但难度较大。我这里完成的是类似第一种效果，也并不完美。</p>
<p>去年在做的时候，本意是想在每次拖拽开始时（dragstart）先判断当前是否在边界处，在边界处就继续禁用拖拽，dragging中判断滑动至边界时，直接禁用拖拽<code>map.disableDragging();</code>，然后dragend中再启用拖拽。但是，实际中禁用拖拽后，比如dragging中禁用拖拽，他就不走dragend了，直接在dragging这一状态便停止了，然后其他的回调情况也是类似这种，我没有找到完善的触发这套流程的回调，所以就没能实现。</p>
<p>因为离线地图的资料比较少，百度地图的API中也并不完善，没有相关的回调，我又没能力自己封装，所以就采用的是下边这种。
这里的思路就是：</p>
<p>因为我们只有4个缩放层级，然后通过百度地图的相关API手动测出临界值时所对应的中心点经纬度，在拖拽出边界时，给他拖回当前临界值对应的中心点。<strong>然后呢，这里的问题就是</strong>：当你拖拽出边界时，再拖回边界所对应的中心点时，实际上是有一个过程的，会有一定的时间来完成这个流程。然后这种情况呢，就会触发多次拖拽回当前中心点，用户的体验就是下图中：拖拽出左边界时，会下滑一定距离。只会回到当前左边界中心点对应的x处，y是会下滑一些的。<strong>关于这个问题的解决</strong>，我在后来学习了防抖节流之后，可以用<strong>节流的思路</strong>去完善一下。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73a857798ccb4d6c845aab3375193939~tplv-k3u1fbpfcp-watermark.image" alt="map_js_bb.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"> let x = 0;
 let y = 0;
 map.addEventListener('dragging', function () &#123;
                console.log(map.getBounds().getCenter());
                //移动后的可视区域
                var movew = map.getBounds().getSouthWest();   //可视区域左下角
                var movee = map.getBounds().getNorthEast();   //可视区域右上角

                var moveL = movew.lng;//可视区域左边界的经度
                var moveR = movee.lng;//可视区域右边界的经度
                var moveB = movew.lat;//可视区域下边界的纬度
                var moveT = movee.lat;//可视区域上边界的纬度

                var boundaryleftlng;//左边界临界值经度
                var boundaryrightlng;//右边界临界值经度
                var boundarytoplat;//上边界临界值纬度
                var boundarydownlat;//下边界临界值纬度

                if (zoom == 4) &#123;
                    boundaryleftlng = -179.204242;
                    boundarydownlat = -82.202266;
                    boundaryrightlng = 180.910992
                    boundarytoplat = 84.602547;
                    if (moveR > boundaryrightlng) &#123;
                        x = 60;
                    &#125; else if (moveL < boundaryleftlng) &#123;
                        x = -58;
                    &#125; else &#123;
                        x = map.getBounds().getCenter().lng;
                    &#125;
                    if (moveT > boundarytoplat) &#123;
                        y = 65;
                    &#125; else if (moveB < boundarydownlat) &#123;
                        y = -55;
                    &#125; else &#123;
                        y = map.getBounds().getCenter().lat;
                    &#125;
                &#125; else if (zoom == 5) &#123;
                    boundaryleftlng = -179.940134;
                    boundarydownlat = -81.533889;
                    boundaryrightlng = 179.690224;
                    boundarytoplat = 84.602547;
                    if (moveR > boundaryrightlng) &#123;
                        x = 120;
                    &#125; else if (moveL < boundaryleftlng) &#123;
                        x = -120;
                    &#125; else &#123;
                        x = map.getBounds().getCenter().lng;
                    &#125;
                    if (moveT > boundarytoplat) &#123;
                        y = 79;
                    &#125; else if (moveB < boundarydownlat) &#123;
                        y = -55;
                    &#125; else &#123;
                        y = map.getBounds().getCenter().lat;
                    &#125;
                &#125; else if (zoom == 6) &#123;
                    boundaryleftlng = -179.976929;
                    boundarydownlat = -81.133421;
                    boundaryrightlng = 179.984581;
                    boundarytoplat = 84.581712;
                    if (moveR > boundaryrightlng) &#123;
                        x = 150;
                    &#125; else if (moveL < boundaryleftlng) &#123;
                        x = -150;
                    &#125; else &#123;
                        x = map.getBounds().getCenter().lng;
                    &#125;
                    if (moveT > boundarytoplat) &#123;
                        y = 82;
                    &#125; else if (moveB < boundarydownlat) &#123;
                        y = -73;
                    &#125; else &#123;
                        y = map.getBounds().getCenter().lat;
                    &#125;
                &#125; else if (zoom == 7) &#123;
                    boundaryleftlng = -179.811353;
                    boundarydownlat = -80.952417;
                    boundaryrightlng = 179.910992;
                    boundarytoplat = 84.607743;
                    if (moveR > boundaryrightlng) &#123;
                        x = 164;
                    &#125; else if (moveL < boundaryleftlng) &#123;
                        x = -164;
                    &#125; else &#123;
                        x = map.getBounds().getCenter().lng;
                    &#125;
                    if (moveT > boundarytoplat) &#123;
                        y = 83;
                    &#125; else if (moveB < boundarydownlat) &#123;
                        y = -78;
                    &#125; else &#123;
                        y = map.getBounds().getCenter().lat;
                    &#125;
                &#125;

                if(moveR > boundaryrightlng || moveL < boundaryleftlng || moveT > boundarytoplat || moveB < boundarydownlat)&#123;
                    // map.disableDragging();
                    var point = new BMap.Point(x,y);
                    map.centerAndZoom(point, map.getZoom());
                &#125;
            &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">3.mousemove事件耗时久使得拖拽体验不好（未解决）</h4>
<p>vue版的代码中我禁止了拖拽，因为我用的两个JS文件和上面的JS版的是一样的，但是用最新版的echarts加vue引入后，拖拽时会报这个警告，会很卡顿，正好我们的需求也不用拖拽，我就禁了给。如果你需要拖拽的话可以试试多找几个版本的api--.js和module--.js替上去试试看能否解决。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b588a58b2ac4d3dabe9e4464c87afc6~tplv-k3u1fbpfcp-watermark.image" alt="warn.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">尾言</h2>
<p>感谢您能看到这里，如果觉得有些许收获的话，请动动你发财的小手，给小编点个赞吧~ ！</p>
<p>因为目前是五一假期，瓦片图那个文件太大了，我就没拷，之后我会把我这一版地图的相关文件，上传到百度云，后续会放个链接，大家感兴趣的可以下载一下，试试看。</p></div>  
</div>
            