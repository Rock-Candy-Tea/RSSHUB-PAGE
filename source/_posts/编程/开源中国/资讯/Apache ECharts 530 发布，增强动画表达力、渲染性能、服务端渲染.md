
---
title: 'Apache ECharts 5.3.0 发布，增强动画表达力、渲染性能、服务端渲染'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e2474a2cd836a6facceacabfc5631497cff.gif'
author: 开源中国
comments: false
date: Thu, 27 Jan 2022 03:47:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e2474a2cd836a6facceacabfc5631497cff.gif'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px; margin-right:0px; text-align:left">Apache ECharts 5.3.0 在动画表达力、渲染性能、服务端渲染上做了大幅度的增强，同时也新增了多坐标轴刻度自动对齐、tooltip 数值格式化、地图投影等社区中期盼已久的特性。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">接下来就让我们一起来看一下这些酷炫又实用的功能吧！</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>关键帧动画</span></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">在之前 ECharts 的动画集中在图形添加、更新以及移除的过渡动画上，过渡动画往往只有开始状态和结束状态。为了表达更复杂的动画效果，我们 5.3.0 中为自定义系列和图形组件引入了全新的关键帧动画。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">下面是一个简单的通过关键帧动画实现的呼吸动画的效果。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><img alt height="260" src="https://oscimg.oschina.net/oscnet/up-e2474a2cd836a6facceacabfc5631497cff.gif" width="288" referrerpolicy="no-referrer"></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#005cc5">keyframeAnimation</span>: [
  &#123;
    <span style="color:#d19a66"><span style="color:#005cc5">duration</span></span>: <span style="color:#d19a66"><span>3000</span></span>,
    <span style="color:#d19a66"><span style="color:#005cc5">loop</span></span>: <span style="color:#56b6c2">true</span>,
    <span style="color:#d19a66"><span style="color:#005cc5">keyframes</span></span>: [
      &#123;
        <span style="color:#d19a66"><span style="color:#005cc5">percent</span></span>: <span style="color:#d19a66"><span>0.5</span></span>,
        <span style="color:#d19a66"><span style="color:#005cc5">easing</span></span>: <span style="color:#98c379"><span style="color:#032f62">'sinusoidalInOut'</span></span>,
        <span style="color:#d19a66"><span style="color:#005cc5">scaleX</span></span>: <span style="color:#d19a66"><span>0.1</span></span>,
        <span style="color:#d19a66"><span style="color:#005cc5">scaleY</span></span>: <span style="color:#d19a66"><span>0.1</span></span>
      &#125;,
      &#123;
        <span style="color:#d19a66"><span style="color:#005cc5">percent</span></span>: <span style="color:#d19a66"><span>1</span></span>,
        <span style="color:#d19a66"><span style="color:#005cc5">easing</span></span>: <span style="color:#98c379"><span style="color:#032f62">'sinusoidalInOut'</span></span>,
        <span style="color:#d19a66"><span style="color:#005cc5">scaleX</span></span>: <span style="color:#d19a66"><span>1</span></span>,
        <span style="color:#d19a66"><span style="color:#005cc5">scaleY</span></span>: <span style="color:#d19a66"><span>1</span></span>
      &#125;
    ]
  &#125;
]
</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">在关键帧动画中，你可以配置动画时长、缓动、是否循环、每个关键帧的位置、缓动以及图形属性等。而且每个图形可以同时设置多个不同配置的关键帧动画。灵活的配置让我们可以实现非常复杂的动画效果，下面列举几个可以应用关键帧动画的场景。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>自定义加载动画</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">ECharts 默认内置了一个加载动画，可以调用<code>showLoading</code>显示。开发者经常会提需求需要更多的加载动画效果。现在有了关键帧动画后，我们可以通过图形（graphic）组件配合关键帧动画实现任何想要的加载动画效果，比如文本描边动画或者柱状图形状的加载动画。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><img alt height="146" src="https://oscimg.oschina.net/oscnet/up-a669a1f4a33d52893e6eb318c6e3604a098.gif" width="372" referrerpolicy="no-referrer"><img alt height="146" src="https://oscimg.oschina.net/oscnet/up-2e149c932703284541396dc0678dd29febc.gif" width="372" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>扩展更丰富的散点图动画特效</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">带有特效动画的散点图一直以来是 ECharts 的特色功能。开发者可以使用 effectScatter 系列来实现带有涟漪特效的动态散点图，这种特效动画除了让作品更有趣，也起到了高亮提示用户的效果。跟加载动画一样，开发者也常常提出需要更多动画效果的需求。现在我们可以在自定义系列中通过使用关键帧动画来实现更复杂的特效。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">比如下面例子在 SVG 地图上给自定义系列绘制的图钉加上了跳动的动画效果，同时配上了涟漪动画。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><img alt height="386" src="https://oscimg.oschina.net/oscnet/up-81a925811442631870211aeca5c4c64a6b7.gif" width="480" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>加载 Lottie 动画</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">为了充分发掘出新的关键帧动画的能力，ECharts 团队的沈毅写了一个<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpissang%2Flottie-parser" target="_blank">Lottie 动画的解析库</a>，可以将 Lottie 动画文件解析成 ECharts 的图形格式进行渲染。结合 Lottie 的表达力我们可以进一步的在我们的项目中绘制出细腻的动画:</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-5dcdb859274e4d526789b1d5d6d952a698c.gif" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>图形组件过渡动画</span></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">我们在 5.0 里为自定义系列中返回的图形提供了更灵活的过渡动画配置。可以通过<code>transition</code>,<span> </span><code>enterFrom</code>,<span> </span><code>leaveTo</code>三个配置项来配置每个图形哪些属性会拥有过渡动画，当图形创建和被移除的时候该执行怎么样的动画。例如：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span><span style="color:#c678dd"><span style="color:#d73a49">function</span></span> <span style="color:#61aeee"><span style="color:#d73a49">renderItem</span></span>() </span>&#123;
  <em><span style="color:#6a737d">//...</span></em>
  <span style="color:#c678dd"><span style="color:#d73a49">return</span></span> &#123;
    <em><span style="color:#6a737d">//...</span></em>
    <span style="color:#d19a66"><span style="color:#005cc5">x</span></span>: <span style="color:#d19a66"><span>100</span></span>,
    <em><span style="color:#6a737d">// 'style', 'x', 'y' 会被动画</span></em>
    <span style="color:#d19a66"><span style="color:#005cc5">transition</span></span>: [<span style="color:#98c379"><span style="color:#032f62">'style'</span></span>, <span style="color:#98c379"><span style="color:#032f62">'x'</span></span>, <span style="color:#98c379"><span style="color:#032f62">'y'</span></span>],
    <span style="color:#d19a66"><span style="color:#005cc5">enterFrom</span></span>: &#123;
      <span style="color:#d19a66"><span style="color:#005cc5">style</span></span>: &#123;
        <em><span style="color:#6a737d">// 淡入</span></em>
        <span style="color:#d19a66"><span style="color:#005cc5">opacity</span></span>: <span style="color:#d19a66"><span>0</span></span>
      &#125;,
      <em><span style="color:#6a737d">//从左侧飞入</span></em>
      <span style="color:#d19a66"><span style="color:#005cc5">x</span></span>: <span style="color:#d19a66"><span>0</span></span>
    &#125;,
    <span style="color:#d19a66"><span style="color:#005cc5">leaveTo</span></span>: &#123;
      <em><span style="color:#6a737d">// 淡出</span></em>
      <span style="color:#d19a66"><span style="color:#005cc5">opacity</span></span>: <span style="color:#d19a66"><span>0</span></span>
    &#125;,
    <em><span style="color:#6a737d">// 向右侧飞出</span></em>
    <span style="color:#d19a66"><span style="color:#005cc5">x</span></span>: <span style="color:#d19a66"><span>200</span></span>
  &#125;;
&#125;
</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">在 5.3.0 中我们把这些过渡动画的配置扩展到了图形（graphic）组件中，并且做了更多的增强：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">如果你不想一一写出每个要动画的属性，现在你可以直接配置<code>transition: 'all'</code>为所有属性都加上动画过渡。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">与此同时我们还新增了<code>enterAnimation</code>、<code>updateAnimation</code>、<code>leaveAnimation</code>分别配置每个图形入场、更新、出场动画的时长（duration）、延迟（delay）和缓动（easing）。除此之外，渐变色现在也支持动画了。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>全新的 SVG 渲染器</span></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">在 5.3.0 中我们重构了我们的 SVG 渲染器，新的 SVG 渲染器能够带来 2x ~ 10x 的性能提升，在某些特殊场景中甚至能有数十倍的提升。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">之前的 SVG 渲染器我们直接从渲染队列更新到 DOM。但是因为 zrender 的图形属性跟 DOM 并不是一一对应的，因此中间需要实现非常复杂的 Diff 逻辑，容易出错而且在某些场景下性能并不能做到最好。在这个版本我们重构成先全量渲染到 VDOM，然后再将 VDOM patch 到 DOM 完成渲染。全量渲染可以避免复杂的 Diff 逻辑带来的潜在 Bug。而 VDOM 和 DOM 的一一对应可以保证在 patch 的时候保证更新是最少的，从而带来巨大的性能提升。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fecharts.apache.org%2Fexamples%2Fzh%2Feditor.html%3Fc%3Dgeo-svg-scatter-simple%26renderer%3Dsvg" target="_blank">这个例子</a><span> </span>可以给大家带来比较直观的性能提升的感受。新的版本在 SVG 模式下拖动的交互上比之前版本流畅非常多。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-520acaebaf1248edfec140513d2b62f5a99.gif" width="640" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">除了性能的提升，我们还可以使用中间全量渲染得到的 VDom 做更多的事情，比如下面会介绍的服务端渲染。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>零依赖的服务端渲染</span></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">在之前的版本 ECharts 也可以实现服务端的渲染，但是必须得依赖<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fnode-canvas" target="_blank">node-canvas</a>，如果是使用 SVG 模式则需要依赖<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjsdom%2Fjsdom" target="_blank">JSDOM</a><span> </span>来模拟 DOM 环境。这些依赖一是带来了额外的体积和使用要求，二是也会有更多的性能损耗。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">这次新的 SVG 渲染器可以让我们从中间的 VDOM 渲染得到字符串，带来了完全零依赖的服务端渲染，输出更精简并且带有 CSS 动画的 SVG 字符串。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><em><span style="color:#6a737d">// 在 SSR 模式下第一个参数不需要再传入 DOM 对象</span></em>
<span style="color:#c678dd"><span style="color:#d73a49">const</span></span> chart = echarts.<span style="color:#d73a49">init</span>(<span style="color:#56b6c2"><span style="color:#005cc5">null</span></span>, <span style="color:#56b6c2"><span style="color:#005cc5">null</span></span>, &#123;
  renderer: <span style="color:#98c379"><span style="color:#032f62">'svg'</span></span>, <em><span style="color:#6a737d">// 必须使用 SVG 模式</span></em>
  ssr: <span style="color:#56b6c2"><span style="color:#005cc5">true</span></span>, <em><span style="color:#6a737d">// 开启 SSR</span></em>
  width: <span style="color:#d19a66"><span>400</span></span>, <em><span style="color:#6a737d">// 需要指明高和宽</span></em>
  height: <span style="color:#d19a66"><span>300</span></span>
&#125;);

<em><span style="color:#6a737d">// 像正常使用一样 setOption</span></em>
chart.setOption(...);

<em><span style="color:#6a737d">// 输出字符串</span></em>
<span style="color:#c678dd"><span style="color:#d73a49">const</span></span> svgStr = chart.renderToSVGString();
</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">我们在 CodeSandbox 中搭建一个最简单的 NodeJS 服务器然后使用 ECharts 服务端渲染的效果：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><img alt height="450" src="https://oscimg.oschina.net/oscnet/up-790196a18429e34e7cd4e82176018019db0.gif" width="762" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">在此基础上，我们优化了输出的 SVG 字符串，使其在诸如 PowerPoint 等更多的平台上有更好的显示效果。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>自定义地图投影</span></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">地图一直是 ECharts 中使用非常广泛的组件。一般地图组件会使用存储了经纬度的 GeoJSON 格式的数据。而 ECharts 则计算出合适的显示区域然后把经纬度线性映射到这个区域。这是一种最简单的地图投影方式。但是简单的线性投影并无法满足某些复杂的地图场景，例如使用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FAlbers_projection" target="_blank">Albers</a><span> </span>投影解决线性投影中面积失真的问题，或者在世界地图中让太平洋显示在中间等等。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">因此在 5.3.0 里中我们引入了自定义的地图投影，可以通过<code>project</code>和<code>unproject</code>两个方法告诉 ECharts 如何投影坐标，以及如何根据投影后坐标计算经纬度。下面是简单的使用墨卡托投影的例子：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>series = &#123;
  <span style="color:#c678dd"><span style="color:#d73a49">type</span></span>: <span style="color:#98c379"><span style="color:#032f62">'map'</span></span>,
  projection: &#123;
    project: <span><span><span><span>point</span></span></span><span> =></span></span> [
      (point[<span style="color:#d19a66"><span>0</span></span>] / <span style="color:#d19a66"><span>180</span></span>) * <span style="color:#e6c07b"><span>Math</span></span>.PI,
      -<span style="color:#e6c07b"><span>Math</span></span>.log(<span style="color:#e6c07b"><span>Math</span></span>.tan((<span style="color:#e6c07b"><span>Math</span></span>.PI / <span style="color:#d19a66"><span>2</span></span> + (point[<span style="color:#d19a66"><span>1</span></span>] / <span style="color:#d19a66"><span>180</span></span>) * <span style="color:#e6c07b"><span>Math</span></span>.PI) / <span style="color:#d19a66"><span>2</span></span>))
    ],
    unproject: <span><span><span><span>point</span></span></span><span> =></span></span> [
      (point[<span style="color:#d19a66"><span>0</span></span>] * <span style="color:#d19a66"><span>180</span></span>) / <span style="color:#e6c07b"><span>Math</span></span>.PI,
      ((<span style="color:#d19a66"><span>2</span></span> * <span style="color:#d19a66"><span>180</span></span>) / <span style="color:#e6c07b"><span>Math</span></span>.PI) * <span style="color:#e6c07b"><span>Math</span></span>.atan(<span style="color:#e6c07b"><span>Math</span></span>.exp(point[<span style="color:#d19a66"><span>1</span></span>])) - <span style="color:#d19a66"><span>90</span></span>
    ]
  &#125;
&#125;;
</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">除了我们自己实现投影公式，我们也可以使用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fd3%2Fd3-geo" target="_blank">d3-geo</a><span> </span>等第三方库提供的现成的投影实现：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#c678dd"><span style="color:#d73a49">const</span></span> projection = d3.geoConicEqualArea();
<em><span style="color:#6a737d">// ...</span></em>
series = &#123;
  <span style="color:#c678dd"><span style="color:#d73a49">type</span></span>: <span style="color:#98c379"><span style="color:#032f62">'map'</span></span>,
  projection: &#123;
    project: <span><span><span><span>point</span></span></span><span> =></span></span> projection(point),
    unproject: <span><span><span><span>point</span></span></span><span> =></span></span> projection.invert(point)
  &#125;
&#125;;
</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">配合在 5.2 里新增的全局过渡动画特性，我们可以实现不同投影效果之间的动画过渡：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-9a9c30aa03a37d623c5cf7a2bf0bbfea32c.gif" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">除了地图的投影之外，我们在这个版本对于地图还做了下面两个增强：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">对 GeoJSON 数据提供了<code>'LineString'</code>和<code>'MultiLineString'</code>的支持。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">将默认标签位置的计算从包围盒中心改为最大区域的重心坐标，计算结果更加准确。</p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>多坐标轴的刻度对齐</span></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">多坐标轴的刻度对齐是社区中提了很久的一个需求，我们在网上也可以看到很多开发者写的如何在 ECharts 中实现坐标轴对齐的文章，通常都会比较麻烦而且会有比较多的局限性。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">在 5.3.0 中我们终于引入了数值轴坐标轴刻度对齐的功能。可以在需要对齐刻度的坐标轴中配置<code>alignTicks: true</code>。该坐标轴就会根据第一个坐标轴的刻度划分去调整自己的刻度，实现自动对齐。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><img alt height="266" src="https://oscimg.oschina.net/oscnet/up-7983bc27d020174e218cd7d1a9e2bf793a5.png" width="553" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>支持高亮和选中状态的关闭</span></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">ECharts 中高亮状态可以在鼠标移到图形上的时候给用户提供反馈，但是在图表中有海量图形的时候，高亮的动画也可能带来交互上的性能问题。特别在 tooltip 或者图例组件联动触发的高亮会同时高亮多个图形。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">因此在这个版本中我们新增了<code>emphasis.disabled</code>配置项。如果不需要高亮的反馈，又对交互性能非常在意的话，可以通过这个配置项来关闭高亮状态。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">与此同时，对于选中状态，我们也新增了<code>select.disabled</code>。该配置项可以用于细粒度配置部分数据不可选。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>支持整个系列的选中</span></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">在 5.3.0 中我们支持将<code>selectedMode</code>配置为<code>'series'</code>以实现系列所有数据的选中。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>tooltip 中的数值格式化</span></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">tooltip 可以在用户移到图形上的时候通过提示框显示更详细的相关信息，ECharts 也提供了<code>formatter</code>回调函数可以让开发者更灵活的自定义提示框的内容。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">但是我们发现大部分时候开发者只是需要格式化提示框中的数字部分，例如固定精度，加上<code>$</code>前缀等等，而之前为了格式化数字开发者只能通过<code>formatter</code>重写整个提示框的内容。特别是在 5.0 后 ECharts 的提示框结构更复杂，样式更美观了，重写变得成本很大而且很难达到默认的效果。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">因此在这个版本我们为 tooltip 新增了<code>valueFormatter</code>配置项用于数值部分的格式化。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">还是刚才那个坐标轴对齐的例子，我们可以为提示框中的数值部分加上 °C 和 ml 的后缀。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#d73a49">tooltip</span>: &#123;
  <span style="color:#d19a66"><span style="color:#005cc5">valueFormatter</span></span>: <span><span>value</span> =></span> value + <span style="color:#98c379"><span style="color:#032f62">' ml'</span></span> <em>// or <span style="color:#032f62">' °C'</span></em>
&#125;
</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">每个系列都可以根据自己的数值格式配置自己的<code>valueFormatter</code>。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>更灵活的扇区圆角</span></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">在 5.0 中我们为扇区新增了圆角的配置，可以让饼图，旭日图变得更有趣。之前圆角的配置只支持内半径和外半径分开配置，这次我们更进一步，支持扇区的四个角都配置成不同的圆角大小，带来更灵活的呈现。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><img alt height="341" src="https://oscimg.oschina.net/oscnet/up-8def3f8b8aba23cab8a8cfe82015692c862.png" width="472" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>饼图的复杂标签优化</span></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">饼图一直是 ECharts 中标签呈现最复杂的图表之一，我们从 5.0 开始就一直在饼图的标签布局、显示上做了很多的优化。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">这次我们针对使用了换行，背景色，富文本等格式比较复杂的饼图标签做了深度的优化。在宽度的自适应、超出容器、引导线的计算上比之前有了更好的效果：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><img alt height="358" src="https://oscimg.oschina.net/oscnet/up-d937c56a57136ef7a11f0931a3a4d918dfb.png" width="964" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>柱状图 large 模式优化</span></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">在数据量很多（> 2k）的时候，我们支持柱状图通过开启 large 模式来加速渲染，提升交互性能，但是之前 large 模式下对柱状图布局比较简单，不支持多系列堆叠后的布局。在 5.3.0 中我们对 large 模式的布局进行了优化，跟普通模式保持了一致性。我们可以在更多的场景中通过开启 large 来优化柱状图的性能。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">除此之外，优化后的柱状图布局也修复了在对数轴这样的非线性轴上堆叠效果不正确的 bug。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>非兼容改动</span></h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>registerMap 和 getMap 方法需要在引入地图组件后才能使用</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">为了减少最小打包的体积，我们从核心模块中移除了地图数据管理的方法<code>getMap</code>和<code>registerMap</code>。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">如果你是<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fecharts.apache.org%2Fhandbook%2Fzh%2Fbasics%2Fimport%2F%23%25E6%258C%2589%25E9%259C%2580%25E5%25BC%2595%25E5%2585%25A5-echarts-%25E5%259B%25BE%25E8%25A1%25A8%25E5%2592%258C%25E7%25BB%2584%25E4%25BB%25B6" target="_blank">按需引入</a><span> </span>ECharts 组件的话，需要保证先引入了<code>GeoComponent</code>或者<code>MapChart</code>之后，才能使用<code>registerMap</code>注册地图数据。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#c678dd"><span style="color:#d73a49">import</span></span> * <span style="color:#c678dd"><span style="color:#d73a49">as</span></span> echarts <span style="color:#c678dd"><span style="color:#d73a49">from</span></span> <span style="color:#98c379"><span style="color:#032f62">'echarts/core'</span></span>;
<span style="color:#c678dd"><span style="color:#d73a49">import</span></span> &#123; MapChart &#125; <span style="color:#c678dd"><span style="color:#d73a49">from</span></span> <span style="color:#98c379"><span style="color:#032f62">'echarts/charts'</span></span>;

echarts.use([MapChart]);

<em><span style="color:#6a737d">// 必须在使用 use 方法注册了 MapChart 后才能使用 registerMap 注册地图</span></em>
echarts.registerMap(<span style="color:#98c379"><span style="color:#032f62">'world'</span></span>, worldJSON);
</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">如果你是使用<code>import * as echarts from 'echarts'</code>全量引入，这次改动不会对你产生任何影响。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>折线图移除默认高亮加粗的效果</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">我们在 5.0 里对折线图引入了默认高亮加粗的效果，但是社区反馈这个在很多场景效果并不好，所以在这个版本我们将这个效果从默认开启改为默认关闭，如果需要使用高亮加粗，则可以显示配置：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>series = &#123;
  <span style="color:#c678dd"><span style="color:#d73a49">type</span></span>: <span style="color:#98c379"><span style="color:#032f62">'line'</span></span>,
  <em><span style="color:#6a737d">//...</span></em>
  emphasis: &#123;
    lineStyle: &#123;
      width: <span style="color:#98c379"><span style="color:#032f62">'bolder'</span></span>
    &#125;
  &#125;
&#125;;</code></pre>
                                        </div>
                                      
</div>
            