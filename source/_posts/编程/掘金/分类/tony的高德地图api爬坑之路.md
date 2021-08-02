
---
title: 'tony的高德地图api爬坑之路...'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d568d6d03034815a19988c13fdfe5df~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 23:06:04 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d568d6d03034815a19988c13fdfe5df~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>由于项目里面涉及到高德地图web端相关业务需求，自己也是从不会到看文档慢慢学会，诚惶诚恐，这篇文章说与其是技术分享，其实是给没接触过高德地图jsapi的前端开发者分享一些小小的建议以及自己的一些经验之谈，说的有不对的地方欢迎大家指正~</p>
<p>接下来我会从【新手怎么看文档】【怎么根据业务需求合理使用api】【怎么封装业务组件】【那些年Tony爬过的坑】这几个方面来具体聊一聊</p>
<h2 data-id="heading-1">1.新手怎么看文档</h2>
<p>个人认为高德地图api文档相对百度地图、bing地图而言更加清晰明了，对新手比较友好，我拿到需求如果不熟悉也要先看一下文档，只需要看web端jsapi即可，主要看这几个板块:</p>
<ol>
<li>示例中心(这里有一些前人写好的demo，拿来稍微改动一下就可以变成业务代码)</li>
<li>参考手册(如果示例中心还不能满足需求，或者对某个类某个方法不熟悉，可以移步到这里定位到相关类或者方法仔细观察一下)</li>
<li>AMapUi组件(这个是高德自己封装好的一些组件，可以实现一些复杂业务，比如用巡航器结合el-slider组件实现带进度条的轨迹回放效果)</li>
</ol>
<h2 data-id="heading-2">2.怎么根据业务需求合理使用api</h2>
<h3 data-id="heading-3">2.1.地图</h3>
<h4 data-id="heading-4">2.2.1.创建地图</h4>
<blockquote>
<p>我一般使用vue-amap插件引入高德地图，首先安装插件npm i vue-amap -S</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">main.js
<span class="hljs-comment">// 引入vue-amap</span>
<span class="hljs-keyword">import</span> VueAMap <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-amap'</span>;
Vue.use(VueAMap);
<span class="hljs-comment">// 初始化vue-amap</span>
VueAMap.initAMapApiLoader(&#123;
  <span class="hljs-comment">// 高德的key</span>
  <span class="hljs-attr">key</span>: <span class="hljs-string">'你申请的key'</span>,
  <span class="hljs-comment">// 插件集合</span>
  <span class="hljs-attr">plugin</span>: [<span class="hljs-string">'Autocomplete'</span>, <span class="hljs-string">'PlaceSearch'</span>, <span class="hljs-string">'Scale'</span>, <span class="hljs-string">'HawkEye'</span>, <span class="hljs-string">'ToolBar'</span>, <span class="hljs-string">'ControlBar'</span>, <span class="hljs-string">'MapType'</span>, <span class="hljs-string">'PolyEditor'</span>, <span class="hljs-string">'AMap.CircleEditor'</span>, <span class="hljs-string">'AMap.MarkerClusterer'</span>, <span class="hljs-string">'AMap.Geocoder'</span>],
  <span class="hljs-comment">// api版本</span>
  <span class="hljs-attr">v</span>: <span class="hljs-string">'2.0'</span>,
  <span class="hljs-comment">// AMapUi组件库版本</span>
  <span class="hljs-attr">uiVersion</span>: <span class="hljs-string">'1.1.1'</span>
&#125;);

单文件组件内使用
<span class="hljs-keyword">import</span> &#123; lazyAMapApiLoaderInstance &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-amap'</span>

initMap () &#123;
      lazyAMapApiLoaderInstance.load().then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.map = <span class="hljs-keyword">new</span> AMap.Map(<span class="hljs-string">'map'</span>, &#123;
          <span class="hljs-attr">viewMode</span>: <span class="hljs-string">'2D'</span>,
          <span class="hljs-attr">center</span>: <span class="hljs-built_in">this</span>.center,
          <span class="hljs-attr">zoom</span>: <span class="hljs-built_in">this</span>.zoom
        &#125;)
        <span class="hljs-keyword">let</span> toolBar = <span class="hljs-keyword">new</span> AMap.ToolBar(&#123;
          <span class="hljs-attr">position</span>: &#123;
            <span class="hljs-attr">top</span>: <span class="hljs-string">'110px'</span>,
            <span class="hljs-attr">left</span>: <span class="hljs-string">'40px'</span>
          &#125;
        &#125;)
        <span class="hljs-keyword">let</span> controlBar = <span class="hljs-keyword">new</span> AMap.ControlBar(&#123;
          <span class="hljs-attr">position</span>: &#123;
            <span class="hljs-attr">top</span>: <span class="hljs-string">'10px'</span>,
            <span class="hljs-attr">left</span>: <span class="hljs-string">'10px'</span>
          &#125;
        &#125;)
        <span class="hljs-keyword">let</span> scale = <span class="hljs-keyword">new</span> AMap.Scale()
        <span class="hljs-built_in">this</span>.map.addControl(toolBar)
        <span class="hljs-built_in">this</span>.map.addControl(controlBar)
        <span class="hljs-built_in">this</span>.map.addControl(scale)
      &#125;)
    &#125;  <span class="hljs-comment">// 这个是2.0版本写法，1.x版本写法稍微有所不同</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.2.点标记</h3>
<h4 data-id="heading-6">2.2.1.创建点标记</h4>
<blockquote>
<p>点击按钮给地图绑定点击事件--->根据事件对象获取点击位置经纬度--->将经纬度传入<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.amap.com%2Fapi%2Fjavascript-api%2Freference%2Foverlay%23marker" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.amap.com/api/javascript-api/reference/overlay#marker" ref="nofollow noopener noreferrer">AMap.Marker</a>构造函数--->
new实例化<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.amap.com%2Fapi%2Fjavascript-api%2Freference%2Foverlay%23marker" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.amap.com/api/javascript-api/reference/overlay#marker" ref="nofollow noopener noreferrer">AMap.Marker</a>构造函数--->调用map的add方法将生成的实例渲染到地图上</p>
</blockquote>
<p>或者</p>
<blockquote>
<p>直接使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.amap.com%2Fapi%2Fjavascript-api%2Freference%2Fplugin%23AMap.MouseTool" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.amap.com/api/javascript-api/reference/plugin#AMap.MouseTool" ref="nofollow noopener noreferrer">AMap.MouseTool</a>鼠标绘制工具类</p>
</blockquote>
<p>建议使用第二种方法，用户体验比较好</p>
<h4 data-id="heading-7">2.2.2.点标记添加弹跳动画</h4>
<blockquote>
<p>需要注意的是如果使用1.4.15版本api直接调用相关方法即可，如果使用2.0版本ap好像需要自己实现，实现代码如下：</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">/deep/.bounce-marker &#123;
          <span class="hljs-attr">animation</span>: bounce <span class="hljs-number">0.</span>5s cubic-bezier(<span class="hljs-number">0.1</span>, <span class="hljs-number">0.25</span>, <span class="hljs-number">0.1</span>, <span class="hljs-number">1</span>) 0s infinite
            alternate both;
        &#125;
        @keyframes bounce &#123;
          <span class="hljs-keyword">from</span> &#123;
            <span class="hljs-attr">transform</span>: translateY(0px);
          &#125;
          to &#123;
            <span class="hljs-attr">transform</span>: translateY(-40px);
          &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">2.2.3.点标记轨迹回放</h4>
<blockquote>
<p>这个参考文档即可，2.0版本写法和1.x版本有所不同</p>
</blockquote>
<h4 data-id="heading-9">2.2.4.点标记聚合显示</h4>
<blockquote>
<p>这个参考文档即可，2.0版本写法和1.x版本有所不同</p>
</blockquote>
<h3 data-id="heading-10">2.3.折线</h3>
<p>使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.amap.com%2Fapi%2Fjavascript-api%2Freference%2Foverlay%23polyline" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.amap.com/api/javascript-api/reference/overlay#polyline" ref="nofollow noopener noreferrer">AMap.Polyline</a>构建函数创建实例--->调用map的add方法将实例添加到地图上</p>
<h3 data-id="heading-11">2.4.多边形</h3>
<h4 data-id="heading-12">2.4.1创建多边形</h4>
<blockquote>
<p>在地图上点击按钮给地图绑定点击事件--->根据事件对象获取点标记的经纬度--->组成一个数组传入<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.amap.com%2Fapi%2Fjavascript-api%2Freference%2Foverlay%23polygon" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.amap.com/api/javascript-api/reference/overlay#polygon" ref="nofollow noopener noreferrer">AMap.Polygon</a>构造函数--->调用add方法将生成的实例渲染到地图上</p>
</blockquote>
<p>或者</p>
<blockquote>
<p>直接使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.amap.com%2Fapi%2Fjavascript-api%2Freference%2Fplugin%23AMap.MouseTool" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.amap.com/api/javascript-api/reference/plugin#AMap.MouseTool" ref="nofollow noopener noreferrer">AMap.MouseTool</a>鼠标绘制工具类</p>
</blockquote>
<p>建议使用第二种方法，用户体验比较好</p>
<h3 data-id="heading-13">2.5.圆</h3>
<h4 data-id="heading-14">2.5.1.创建圆</h4>
<p>使用AMap.Circle(opt:<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.amap.com%2Fapi%2Fjavascript-api%2Freference%2Foverlay%23CircleOptions" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.amap.com/api/javascript-api/reference/overlay#CircleOptions" ref="nofollow noopener noreferrer">CircleOptions</a>)构建函数创建实例--->调用map的add方法将实例添加到地图上</p>
<h4 data-id="heading-15">2.5.2.编辑圆</h4>
<p>首先根据后端返回的圆心经纬度和半径回显圆--->然后使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.amap.com%2Fapi%2Fjavascript-api%2Freference%2Fplugin%23AMap.CircleEditor" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.amap.com/api/javascript-api/reference/plugin#AMap.CircleEditor" ref="nofollow noopener noreferrer">AMap.CircleEditor(Map,Circle)</a>创建实例--->调用open方法开启编辑--->监听move、adjust事件</p>
<h4 data-id="heading-16">2.5.3.根据id唯一标识查看(放大)圆</h4>
<p>遍历后端返回的圆形覆盖物列表数据(array)，将唯一标识id绑定到<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.amap.com%2Fapi%2Fjavascript-api%2Freference%2Foverlay%23circle" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.amap.com/api/javascript-api/reference/overlay#circle" ref="nofollow noopener noreferrer">AMap.Circle</a>的extData参数上面，这样点击表格数据的每一行就可以根据这个唯一标识结合Circle类的getExtData()方法找到这个圆形覆盖物，然后调用map.setFitView()方法将该圆形覆盖物放大到合适的视野级别</p>
<h4 data-id="heading-17">2.5.4.判断圆和圆的位置关系</h4>
<p>这个高德好像没有提供相关方法，自己实现，思路也很简单，大致思路就是判断圆心距离和半径之和的大小关系。怎么计算圆心距离可以参考api文档里面的【参考手册 数学计算库】</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-title">doesCircleIntersect</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> circlesData = <span class="hljs-built_in">this</span>.allCircleData.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.type !== <span class="hljs-number">3</span>)
      <span class="hljs-keyword">if</span> (!circlesData.length) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-keyword">const</span> isIntersect = circlesData.some(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
        <span class="hljs-keyword">const</span> marker1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.AMap.LngLat(item.lon, item.lat)
        <span class="hljs-keyword">const</span> marker2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.AMap.LngLat(<span class="hljs-built_in">this</span>.circleOptions.lon, <span class="hljs-built_in">this</span>.circleOptions.lat)
        <span class="hljs-keyword">const</span> circleCenterDistance = marker1.distance(marker2)
        <span class="hljs-keyword">const</span> circleRadiusSum = item.radius + <span class="hljs-built_in">this</span>.circleOptions.radius
        <span class="hljs-keyword">return</span> circleCenterDistance < circleRadiusSum
      &#125;)
      <span class="hljs-keyword">return</span> isIntersect
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">2.5.5.判断圆和点标记的位置关系</h4>
<p>直接调用Circle类的contains(point:LngLat)方法，这个方法返回一个boolean，用于判断圆形覆盖物是否包含点标记</p>
<h3 data-id="heading-19">2.6.信息窗体</h3>
<h4 data-id="heading-20">2.6.1.打开信息窗体</h4>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 方法一:html字符串拼接思路实现</span>
    <span class="hljs-comment">// 打开信息窗体</span>
    <span class="hljs-function"><span class="hljs-title">openInfoWindow</span>(<span class="hljs-params">info</span>)</span> &#123;
      <span class="hljs-keyword">var</span> infoList = [<span class="hljs-string">'<div class="info-container">'</span>]
      infoList.push(<span class="hljs-string">`<div class="info-container__header">飞手信息</div>`</span>)
      infoList.push(<span class="hljs-string">`<div class="info-container__body">`</span>)
      infoList.push(<span class="hljs-string">`<div>飞手姓名：<span class="hljs-subst">$&#123;info.pilotName&#125;</span></div>`</span>)
      infoList.push(<span class="hljs-string">`<div>身份证号：<span class="hljs-subst">$&#123;info.identityCard&#125;</span></div>`</span>)
      infoList.push(<span class="hljs-string">`<div>飞行时长：<span class="hljs-subst">$&#123;info.duration&#125;</span>h</div>`</span>)
      infoList.push(<span class="hljs-string">`<div>地址：<span class="hljs-subst">$&#123;info.address&#125;</span></div>`</span>)
      infoList.push(<span class="hljs-string">`<div>经度：<span class="hljs-subst">$&#123;info.pilotLon&#125;</span> 纬度：<span class="hljs-subst">$&#123;info.pilotLat&#125;</span></div>`</span>)
      infoList.push(<span class="hljs-string">`</div></div>`</span>)
      <span class="hljs-built_in">this</span>.infoWindow = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.AMap.InfoWindow(&#123;
        <span class="hljs-attr">content</span>: infoList.join(<span class="hljs-string">''</span>), <span class="hljs-comment">// 使用默认信息窗体框样式，显示信息内容</span>
        <span class="hljs-attr">offset</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.AMap.Pixel(-<span class="hljs-number">5</span>, -<span class="hljs-number">35</span>)
      &#125;)
      <span class="hljs-built_in">this</span>.infoWindow.open(
        <span class="hljs-built_in">this</span>.map,
        <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.AMap.LngLat(info.pilotLon, info.pilotLat)
      )
    &#125;
    
    <span class="hljs-comment">// 方法二：使用组件的思路去实现，设置isCustom属性为true就可以随心所欲的去用组件去实现一个自定义的信息窗体</span>
    <span class="hljs-comment">// 打开信息窗体</span>
    <span class="hljs-function"><span class="hljs-title">openInfoWindow</span>(<span class="hljs-params">info</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.showInfoWindow = <span class="hljs-literal">true</span>
      <span class="hljs-built_in">this</span>.infoWindowContent = info
      <span class="hljs-keyword">const</span> infoWindow = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.AMap.InfoWindow(&#123;
        <span class="hljs-attr">isCustom</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// isCustom设置true 自定义信息窗体</span>
        <span class="hljs-attr">content</span>: <span class="hljs-built_in">this</span>.$refs.infoWindowRef.$el, <span class="hljs-comment">// 指向自定义信息窗体dom元素</span>
        <span class="hljs-attr">offset</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.AMap.Pixel(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
      &#125;)
      <span class="hljs-built_in">this</span>.infoWindow = infoWindow
      <span class="hljs-built_in">this</span>.infoWindow.open(<span class="hljs-built_in">this</span>.map, <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.AMap.LngLat(info.lon, info.lat))
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>以上两种方法都可以实现，方法一适用于展示内容比较简单的信息窗体，方法二相对而言更加灵活可扩展，写起来也很爽，也好维护，后期迭代只需要改动子组件即可</p>
</blockquote>
<h3 data-id="heading-21">2.7.覆盖物群组</h3>
<blockquote>
<p>如果需要一次性给地图添加很多覆盖物，其中包括点标记、圆形、多边形等等，可以考虑使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.amap.com%2Fapi%2Fjavascript-api%2Freference%2Foverlay%23overlaygroup" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.amap.com/api/javascript-api/reference/overlay#overlaygroup" ref="nofollow noopener noreferrer">AMap.OverlayGroup</a>，比较简单粗暴</p>
</blockquote>
<h3 data-id="heading-22">2.8.LBS服务</h3>
<h4 data-id="heading-23">2.8.1.地理编码(地址->经纬度)</h4>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">/**
     * 根据关键词查询经纬度
     */</span>
    <span class="hljs-function"><span class="hljs-title">getLngLatByKeywords</span>(<span class="hljs-params">keywords</span>)</span> &#123;
      <span class="hljs-keyword">const</span> geocoder = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.AMap.Geocoder()
      geocoder.getLocation(keywords, <span class="hljs-function">(<span class="hljs-params">status, result</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (status === <span class="hljs-string">'complete'</span> && result.geocodes.length) &#123;
          <span class="hljs-keyword">const</span> center = result.geocodes[<span class="hljs-number">0</span>].location
          <span class="hljs-built_in">this</span>.map.setCenter(center)
          <span class="hljs-built_in">this</span>.map.setZoom(<span class="hljs-number">18</span>)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">this</span>.$message.info(<span class="hljs-string">'根据地址查询位置失败，请输入详细地址搜索'</span>)
        &#125;
      &#125;)
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">2.8.2.逆地理编码(经纬度->地址)</h4>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">/**
     * 根据经纬度查询位置
     */</span>
    <span class="hljs-function"><span class="hljs-title">getAddressByLngLat</span>(<span class="hljs-params">lnglat</span>)</span> &#123;
      <span class="hljs-keyword">const</span> geocoder = <span class="hljs-keyword">new</span> <span class="hljs-built_in">window</span>.AMap.Geocoder(&#123;
        <span class="hljs-attr">city</span>: <span class="hljs-string">'全国'</span>
      &#125;)
      geocoder.getAddress(lnglat, <span class="hljs-function">(<span class="hljs-params">status, result</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (status === <span class="hljs-string">'complete'</span> && result.regeocode) &#123;
          <span class="hljs-keyword">const</span> address = result.regeocode.formattedAddress
          <span class="hljs-built_in">this</span>.form.remarks = <span class="hljs-string">`以<span class="hljs-subst">$&#123;address&#125;</span>为中心，以<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.circleOptions.radius&#125;</span>米为半径的圆形区域`</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">this</span>.$message.info(<span class="hljs-string">'根据经纬度查询地址失败'</span>)
        &#125;
      &#125;)
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">2.8.3.行政区划查询</h4>
<blockquote>
<p>这里就不详细说，分两种，行政区边界查询和下属行政区查询，一般会结合el-cascader级联选择器做一些行政区划查询的业务需求。</p>
</blockquote>
<h2 data-id="heading-26">3.怎么封装业务组件</h2>
<blockquote>
<p>封装组价也很简单，不外乎组件通信，slot，mixins这些东西，当然，想要封装一个高可用、低耦合的组件还是比较考验人的功底，我一般是首先实现业务需求，然后再将很多页面复用的data、methods单独抽离出来，放到mixins里面，前提是这些data、methods具备单独抽离出来的条件，这个条件怎么界定的其实也没有一个标准，就看到底是在页面写还是在mixins里面写比较优雅。当然也可以直接封装一个单独的业务组件，比如信息窗体自定义组件，电子围栏组件等等</p>
</blockquote>
<h2 data-id="heading-27">4.那些年Tony爬过的坑</h2>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d568d6d03034815a19988c13fdfe5df~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<p>什么...Tony???没错，不要怀疑，我以前不是理发的，只是英语不好所以取了这个简单又好记的名字，我很喜欢，毕竟已经伴随我好几年的职业生涯了</p>
<h3 data-id="heading-28">4.1.绘制多边形使用第一种方法点标记不按套路出牌，不按顺时针连接，也不按逆时针连接，却是交叉连接。这么说可能还是有些懵逼，我手绘几张图对比看一下就明白了</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/134fc08d1825444bb904941fe8bd345a~tplv-k3u1fbpfcp-watermark.image" alt="26eff89fd312073ea1898221bd3fdd7.png" loading="lazy" referrerpolicy="no-referrer">
期望的连接顺序是1-2-3-4-1 或者 1-4-3-2-1 然而 他偏偏不给面子逆天而行 1-2-4-3-1 或者 1-3-4-2-1</p>
<blockquote>
<p>解决办法：先将经纬度坐标转换成平面坐标，根据平面坐标对点标记按照一定的规则排序，排好序再创建多边形，规则如下</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// start表示中心点  end表示多边形顶点</span>
    getAngle (start, end) &#123;
      <span class="hljs-comment">// 首先将经纬度坐标转换为平面坐标</span>
      <span class="hljs-keyword">const</span> p_start = <span class="hljs-built_in">this</span>.map.lngLatToContainer(start)
      <span class="hljs-keyword">const</span> p_end = <span class="hljs-built_in">this</span>.map.lngLatToContainer(end)
      <span class="hljs-keyword">const</span> diff_x = p_end.x - p_start.x
      <span class="hljs-keyword">const</span> diff_y = p_end.y - p_start.y
      <span class="hljs-keyword">return</span> (<span class="hljs-number">360</span> * <span class="hljs-built_in">Math</span>.atan2(diff_y, diff_x)) / (<span class="hljs-number">2</span> * <span class="hljs-built_in">Math</span>.PI) + <span class="hljs-number">180</span>
    &#125;
    
    <span class="hljs-comment">// 遍历顶点集合，调用getAngle方法获取每个顶点和中心点成的角度(<90°),根据角度对顶点进行排序，排好序再绘制多边形即可，后续代码省略</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">4.2.列表页新增圆形(多边形)覆盖物成功之后，立即点击编辑这条新增记录，打开el-dialog对话框，对话框里面的地图会出现首次渲染失败的神奇bug</h3>
<blockquote>
<p>解决办法：新增页面和编辑页面地图容器id名取名区别开</p>
</blockquote>
<h2 data-id="heading-30"><span>结语</span></h2>
行文至此，想聊的基本都聊了，可能还有一些高级用法，不常见的bug我还没接触过，算不上干货满满，也算不上废话连篇，只能说是给新人一点小小的指引，希望看了我的文章可以少走一点弯路，有什么想法也可以留言相互交流。</div>  
</div>
            