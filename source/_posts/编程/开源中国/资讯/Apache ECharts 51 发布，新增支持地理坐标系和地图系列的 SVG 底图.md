
---
title: 'Apache ECharts 5.1 发布，新增支持地理坐标系和地图系列的 SVG 底图'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f677cd918bc896a5c0e252c060e64667a22.gif'
author: 开源中国
comments: false
date: Wed, 12 May 2021 07:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f677cd918bc896a5c0e252c060e64667a22.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>在最近发布的 Apache ECharts 5.1 版本中，新增支持了地理坐标系和地图系列的 <strong>SVG 底图</strong>，可以用来灵活地创造出非常酷的可视化作品；<strong>图例组件</strong>全面更新，默认更接近数据的样式，让数据与图例之间产生更符合直观的关联。</p> 
<p>除此之外，我们还在这个版本中改进了非常多的功能，让我们一起来了解一下吧！</p> 
<h2>地理坐标系和地图系列的 SVG 底图</h2> 
<p>在此之前，Apache ECharts 的只支持 geoJSON 格式的地图。在本次发布的 v5.1 版本中，地理坐标系组件（geo）和地图系列（map series）的底图支持了 SVG 格式，并且在 Canvas 和 SVG 两种渲染模式中得到渲染表现一致的效果。</p> 
<p><img alt height="322" src="https://oscimg.oschina.net/oscnet/up-f677cd918bc896a5c0e252c060e64667a22.gif" width="400" referrerpolicy="no-referrer"></p> 
<p>除此之外，SVG 底图也和 geoJSON 一样，默认支持了平移、缩放等操作，提供相似的用户体验。</p> 
<p><img alt height="285" src="https://oscimg.oschina.net/oscnet/up-2ac02b0c91a3a3626e969fa877707382d20.gif" width="400" referrerpolicy="no-referrer"></p> 
<p>SVG 地图支持了对指定区域“高亮（emphasis）”、“聚焦（focus）”、“淡出（blur）”、“显示标签（label）”、“提示框（tooltip）”等能力，通过 ECharts 配置项就可以方便地启用。他们能够让用户清晰地看到数据、信息和图像的关联。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-bbd828ae5fc9828aad9e363441934d451ef.gif" referrerpolicy="no-referrer"></p> 
<p>有了 SVG 底图后，开发者可以在地图系列（map series）上做出更丰富的数据可视化表达。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e3c9be08fc95602ff022c30a22c58d9c527.gif" referrerpolicy="no-referrer"></p> 
<p>结合 Apache ECharts v5 开始支持的“选中（select）”能力，能做出一些像飞机、影院选座功能性的应用。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-ad77434d733e1e188d32b91aa7da1a9f91d.gif" referrerpolicy="no-referrer"></p> 
<p>同 geoJSON 底图一样，SVG 底图上也可以绘制其他图表系列，如散点图（scatter series）、路径图（lines series）、关系图（graph series）等等。下面是绘制路径图系列（lines series）的例子。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-50891569ca1ea920a5a794f1f0492e00380.gif" referrerpolicy="no-referrer"></p> 
<p><img height="0" src="https://oscimg.oschina.net/oscnet/up-e22aa8e7d16bafc62e505e2a2afbd22ba30.png" width="0" referrerpolicy="no-referrer"></p> 
<p>SVG 底图大大加强了 ECharts 能创造出的图表的表现力，欢迎在官网下载最新版尝试使用！</p> 
<h2>全面升级的图例</h2> 
<p>图例通常位于图表的一个角落，用以表示数据样式以及其所代表的含义。Apache ECharts 也在很早的版本就支持了图例。</p> 
<p>在这个版本中，我们对图例进行了全面的升级，让图例的默认样式与数据的样式更加接近，包括图形颜色、形状、描边等信息。这样，用户在直观上就更能对数据产生关联。</p> 
<p><img height="0" src="https://oscimg.oschina.net/oscnet/up-c4ec4b8f906ecf5f2aab5d1c43388b1feed.png" width="0" referrerpolicy="no-referrer"></p> 
<p>许多 <code>legend</code> 中的样式支持设置为 <code>'inherit'</code>，这意味着其值将会从系列的对应值中继承，从而方便地在图例中使用与系列中相同的值。</p> 
<p>此外，我们还扩展了 <code>legend</code> 配置项的接口，使得开发者可以将图例的样式自定义成不同于系列的样式，以满足特殊场景下的需求。</p> 
<h2>完整的版本记录</h2> 
<h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts-doc%2Fblob%2Fmaster%2Fzh%2Fchangelog.md%23v510" target="_blank">v5.1.0</a></h3> 
<p>[Feature] [geo] [map] 地理坐标系和地图系列支持使用 SVG 数据作为地图源。#14571 (100pah)<br> [Feature] [legend] 默认使用了更直观的图例设计，图例的样式更符合系列样式。#14497 (Ovilia)<br> [Feature] [i18n] 新增捷克语翻译。#14468 (JiriBalcar)<br> [Feature] [animation] 为resize方法添加animation的动画过渡配置。#14553 (pissang)<br> [Feature] [effectScatter] effectScatter系列添加clip配置。#14574 (susiwen8)<br> [Fix] [debug] 优化组件缺失时候的错误提示。#14568 (pissang)<br> [Fix] [tooltip] 优化tooltip的性能。#14246 (plainheart)<br> [Fix] [label] 修复标签可能会显示在图形下面的错误。#14542 (plainheart) #14417 (susiwen8)<br> [Fix] [pattern] 修复CanvasPatttern#setTransform方法可能会不存在报错的问题 #738 (pissang)<br> [Fix] [tooltip] 修复tooltip中对时间轴的格式化错误 #14471 (Ovilia)<br> [Fix] [symbol] 所有使用symbol的组件都添加了symbolOffset的支持。#14375 (plainheart)<br> [Fix] [markArea] 修复markArea背景色可能不显示的问题。Close #13647 #14343 (Nick22nd)<br> [Fix] [markLine] 修复markLine中字符串格式的数据可能无法使用的问题。Close #14300 #14314 (Ovilia)<br> [Fix] [select] 修复可能存在null值访问的问题。Close #14293 #14413 (leosxie)<br> [Fix] [dataZoom] 修复dataZoom中的标签高宽设置不生效的问题。#14388 (wf123537200)<br> [Fix] [animation] 修复存在NaN值的动画可能会错误的问题。#730 (Nick22nd)<br> [Fix] [visualMap] 修复itemSymbol配置不生效的问题。Close #5719 #14243 (Ovilia)<br> [Fix] [loading] 修复标签被其它图形覆盖的问题。#14191 (yufeng04)<br> [Fix] [custom] 修复自定义系列标签颜色可能不对的问题。Close #14092 #14254 (Nick22nd)<br> [Fix] [map] 修复使用labelLayout的时候地图标签可能不会随着拖动更新。#14578 (pissang)<br> [Fix] [calendar] 修复日标签位置偏移的问题。Close #11508 #13902 (Nick22nd)<br> [Fix] [lines] 修复折线图动画可能错乱的问题。#13638 (vially)<br> [Fix] [type] 暴露更多的类型方便插件生成类型文件 #14289 (pissang)<br> [Fix] [type] 添加LegendComponentOption.icon类型 #14263 (thesiti92)<br> [Fix] 去除一些遗留代码的使用 #14357 (pissang)</p> 
<h3><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgithub.com%2Fapache%2Fecharts-doc%2Fblob%2Fmaster%2Fzh%2Fchangelog.md%23v511" target="_blank">v5.1.1</a></h3> 
<p>[Fix] [geo] 修复 5.1.0 引入的geo组件上tooltip无法显示的问题。#14767 (pissang)<br> [Fix] [tooltip] 修复 5.1.0 引入的 tooltip 在开启 appendToBody 后位置不对的问题。#14713 (plainheart)<br> [Fix] [map] 修复 5.1.0 引入的地图上的tooltip可能会报错的问题。#14704 (plainheart)<br> [Fix] [pie] 修复饼图上标签引导线labelLine从outside修改为inside之后高亮依然可能显示的问题。#14702 (villebro)<br> [Fix] [type] 修复 5.1.0 引入的老版本 TypeScript 可能出现类型错误的问题。Close #14716 #14739<br> [Fix] [type] 修复 symbolOffset 非可选的类型错误。#14693 (villebro)</p>
                                        </div>
                                      
</div>
            