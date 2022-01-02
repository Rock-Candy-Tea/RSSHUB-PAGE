
---
title: 'go-charts 0.0. 3版本发布，兼容更多的 echarts 配置'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c59f70784f9be3947a3a4614d1099b5f104.png'
author: 开源中国
comments: false
date: Sun, 02 Jan 2022 10:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c59f70784f9be3947a3a4614d1099b5f104.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#c9d1d9; text-align:start"><span style="color:#000000"><code>go-charts</code>基于</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwcharczuk%2Fgo-chart" target="_blank"><span style="color:#000000">go-chart</span></a><span style="color:#000000">生成数据图表，无其它模块的依赖纯golang的实现，支持<code>svg</code>与<code>png</code>的输出，<code>Apache ECharts</code>在前端开发中得到众多开发者的认可，<code>go-charts</code>兼容<code>Apache ECharts</code>的配置参数，简单快捷的生成相似的图表(<code>svg</code>或<code>png</code>)，方便插入至Email或分享使用。下面为常用的几种图表截图(两种模式)：</span></p> 
<p style="color:#c9d1d9; text-align:center"><img alt src="https://oscimg.oschina.net/oscnet/up-c59f70784f9be3947a3a4614d1099b5f104.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">支持图表类型</h2> 
<p>暂仅支持三种的图表类型：<code>line</code>,<span> </span><code>bar</code><span> </span>以及<span> </span><code>pie</code></p> 
<p> </p> 
<h2 style="text-align:start">示例</h2> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#000000"><code>go-charts</code>兼容了<code>echarts</code>的参数配置，可简单的使用json形式的配置字符串则可快速生成图表。</span></p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"os"</span>

charts <span style="color:var(--color-prettylights-syntax-string)">"github.com/vicanso/go-charts"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
<span>buf</span>, <span>err</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span>charts</span>.<span style="color:var(--color-prettylights-syntax-entity)">RenderEChartsToPNG</span>(<span style="color:var(--color-prettylights-syntax-string)">`&#123;</span>
<span style="color:var(--color-prettylights-syntax-string)">"title": &#123;</span>
<span style="color:var(--color-prettylights-syntax-string)">"text": "Line"</span>
<span style="color:var(--color-prettylights-syntax-string)">&#125;,</span>
<span style="color:var(--color-prettylights-syntax-string)">"xAxis": &#123;</span>
<span style="color:var(--color-prettylights-syntax-string)">"type": "category",</span>
<span style="color:var(--color-prettylights-syntax-string)">"data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]</span>
<span style="color:var(--color-prettylights-syntax-string)">&#125;,</span>
<span style="color:var(--color-prettylights-syntax-string)">"series": [</span>
<span style="color:var(--color-prettylights-syntax-string)">&#123;</span>
<span style="color:var(--color-prettylights-syntax-string)">"data": [150, 230, 224, 218, 135, 147, 260]</span>
<span style="color:var(--color-prettylights-syntax-string)">&#125;</span>
<span style="color:var(--color-prettylights-syntax-string)">]</span>
<span style="color:var(--color-prettylights-syntax-string)">&#125;`</span>)
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> <span>err</span> <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
<span style="color:var(--color-prettylights-syntax-entity)">panic</span>(<span>err</span>)
&#125;
<span>os</span>.<span style="color:var(--color-prettylights-syntax-entity)">WriteFile</span>(<span style="color:var(--color-prettylights-syntax-string)">"output.png"</span>, <span>buf</span>, <span style="color:var(--color-prettylights-syntax-constant)">0600</span>)
&#125;</pre> 
</div> 
<h2 style="text-align:start">参数说明</h2> 
<ul> 
 <li><code>theme</code><span> </span>颜色主题，支持<code>dark</code>与<code>light</code>模式，默认为<code>light</code></li> 
 <li><code>padding</code><span> </span>图表的内边距，单位px。支持以下几种模式的设置 
  <ul> 
   <li><code>padding: 5</code><span> </span>设置内边距为5</li> 
   <li><code>padding: [5, 10]</code><span> </span>设置上下的内边距为 5，左右的内边距为 10</li> 
   <li><code>padding:[5, 10, 5, 10]</code><span> </span>分别设置<code>上右下左</code>边距</li> 
  </ul> </li> 
 <li><code>title</code><span> </span>图表标题，包括标题内容、高度、颜色等 
  <ul> 
   <li><code>title.text</code><span> </span>标题内容</li> 
   <li><code>title.left</code><span> </span>标题与容器左侧的距离，可设置为<code>left</code>,<span> </span><code>right</code>,<span> </span><code>center</code>,<span> </span><code>20%</code><span> </span>以及<span> </span><code>20</code><span> </span>这样的具体数值</li> 
   <li><code>title.top</code><span> </span>标题与容器顶部的距离，暂仅支持具体数值，如<code>20</code></li> 
   <li><code>title.textStyle.color</code><span> </span>标题文字颜色</li> 
   <li><code>title.textStyle.fontSize</code><span> </span>标题文字字体大小</li> 
   <li><code>title.textStyle.height</code><span> </span>标题高度</li> 
   <li><code>title.textStyle.fontFamily</code><span> </span>标题文字的字体系列，需要注意此配置是会影响整个图表的字体</li> 
  </ul> </li> 
 <li><code>xAxis</code><span> </span>直角坐标系grid中的x轴，由于go-charts仅支持单一个x轴，因此若参数为数组多个x轴，只使用第一个配置 
  <ul> 
   <li><code>xAxis.boundaryGap</code><span> </span>坐标轴两边留白策略，仅支持三种设置方式<code>null</code>,<span> </span><code>true</code>或者<code>false</code>。<code>null</code>或<code>true</code>时则数据点展示在两个刻度中间</li> 
   <li><code>xAxis.splitNumber</code><span> </span>坐标轴的分割段数，需要注意的是这个分割段数只是个预估值，最后实际显示的段数会在这个基础上根据分割后坐标轴刻度显示的易读程度作调整</li> 
   <li><code>xAxis.data</code><span> </span>x轴的展示文案，暂只支持字符串数组，如["Mon", "Tue"]，其数量需要与展示点一致</li> 
  </ul> </li> 
 <li><code>yAxis</code><span> </span>直角坐标系grid中的y轴，最多支持两个y轴 
  <ul> 
   <li><code>yAxis.min</code><span> </span>坐标轴刻度最小值，若不设置则自动计算</li> 
   <li><code>yAxis.max</code><span> </span>坐标轴刻度最大值，若不设置则自动计算</li> 
   <li><code>yAxis.axisLabel.formatter</code><span> </span>刻度标签的内容格式器，如<code>"formatter": "&#123;value&#125; kg"</code></li> 
  </ul> </li> 
 <li><code>legend</code><span> </span>图表中不同系列的标记 
  <ul> 
   <li><code>legend.data</code><span> </span>图例的数据数组，为字符串数组，如["Email", "Video Ads"]</li> 
   <li><code>legend.align</code><span> </span>图例标记和文本的对齐，默认为标记靠左<code>left</code></li> 
   <li><code>legend.padding</code><span> </span>legend的padding，配置方式与图表的<code>padding</code>一致</li> 
   <li><code>legend.left</code><span> </span>legend离容器左侧的距离，其值可以为具体的像素值(20)或百分比(20%)</li> 
   <li><code>legend.right</code><span> </span>legend离容器右侧的距离，其值可以为具体的像素值(20)或百分比(20%)</li> 
  </ul> </li> 
 <li><code>series</code><span> </span>图表的数据项列表 
  <ul> 
   <li><code>series.type</code><span> </span>图表的展示类型，暂支持<code>line</code>,<span> </span><code>bar</code>以及<code>pie</code>，需要注意<code>pie</code>只能单独使用</li> 
   <li><code>series.yAxisIndex</code><span> </span>该数据项使用的y轴，默认为0，对yAxis的配置对应</li> 
   <li><code>series.itemStyle.color</code><span> </span>该数据项展示时使用的颜色</li> 
   <li><code>series.data</code><span> </span>数据项对应的数据数组，支持以下形式的数据： 
    <ul> 
     <li><code>数值</code><span> </span>常用形式，数组数据为浮点数组，如[1.1, 2,3, 5.2]</li> 
     <li><code>结构体</code><span> </span>pie图表或bar图表中指定样式使用，如[&#123;"value": 1048, "name": "Search Engine"&#125;,&#123;"value": 735,"name": "Direct"&#125;]</li> 
    </ul> </li> 
  </ul> </li> 
</ul> 
<h2 style="text-align:start">性能</h2> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#000000">简单的图表生成PNG在20ms左右，而SVG的性能则更快，性能上比起使用<code>chrome headless</code>加载<code>echarts</code>图表展示页面再截图生成的方式大幅度提升，满足简单的图表生成需求。</span></p> 
<div style="text-align:start"> 
 <pre>goos: darwin
goarch: amd64
pkg: github.com/vicanso/go-charts
cpu: Intel(R) Core(TM) i5-8257U CPU @ 1.40GHz
BenchmarkEChartsRenderPNG-8           60          17765045 ns/op         2492854 B/op       1007 allocs/op
BenchmarkEChartsRenderSVG-8          282           4303042 ns/op        32622688 B/op       2983 allocs/op</pre> 
</div> 
<h2 style="text-align:start">中文字符</h2> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#000000">默认使用的字符为<code>Roboto</code>为英文字体库，因此如果需要显示中文字符需要增加中文字体库，<code>InstallFont</code>函数可添加对应的字体库，成功添加之后则指定<code>title.textStyle.fontFamily</code>即可。 在浏览器中使用<code>svg</code>时，如果指定的<code>fontFamily</code>不支持中文字符，展示的中文并不会乱码，但是会导致在计算字符宽度等错误。</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            