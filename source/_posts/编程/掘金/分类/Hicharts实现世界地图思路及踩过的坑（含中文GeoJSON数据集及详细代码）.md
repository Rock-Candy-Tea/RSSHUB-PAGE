
---
title: 'Hicharts实现世界地图思路及踩过的坑（含中文GeoJSON数据集及详细代码）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/423dab3b517848508d4fd47d6a8aabdb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 02:34:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/423dab3b517848508d4fd47d6a8aabdb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>目录</strong></p>
<p><a href="https://juejin.cn/post/6984728685106429965#%E4%B8%80%E3%80%81%E5%9B%BE%E8%A1%A8%E5%BA%93%E7%9A%84%E6%AF%94%E8%BE%83" target="_blank" title="#%E4%B8%80%E3%80%81%E5%9B%BE%E8%A1%A8%E5%BA%93%E7%9A%84%E6%AF%94%E8%BE%83">一、图表库的比较</a></p>
<p><a href="https://juejin.cn/post/6984728685106429965#%E4%BA%8C%E3%80%81Geojson%E4%B8%96%E7%95%8C%E5%9C%B0%E5%9B%BE%E6%95%B0%E6%8D%AE%E9%9B%86%E5%8F%8A%E4%B8%AD%E6%96%87%E7%BF%BB%E8%AF%91" target="_blank" title="#%E4%BA%8C%E3%80%81Geojson%E4%B8%96%E7%95%8C%E5%9C%B0%E5%9B%BE%E6%95%B0%E6%8D%AE%E9%9B%86%E5%8F%8A%E4%B8%AD%E6%96%87%E7%BF%BB%E8%AF%91">二、Geojson世界地图数据集及中文翻译</a></p>
<p><a href="https://juejin.cn/post/6984728685106429965#%E4%B8%89%E3%80%81Highcharts%E5%AE%9E%E7%8E%B0%E4%B8%96%E7%95%8C%E5%9C%B0%E5%9B%BE%EF%BC%88%E5%90%AB%E8%AF%A6%E7%BB%86%E4%BB%A3%E7%A0%81%EF%BC%89" target="_blank" title="#%E4%B8%89%E3%80%81Highcharts%E5%AE%9E%E7%8E%B0%E4%B8%96%E7%95%8C%E5%9C%B0%E5%9B%BE%EF%BC%88%E5%90%AB%E8%AF%A6%E7%BB%86%E4%BB%A3%E7%A0%81%EF%BC%89">三、Highcharts实现世界地图（含详细代码）</a></p>
<p><a href="https://juejin.cn/post/6984728685106429965#%E5%9B%9B%E3%80%81%E5%AE%9E%E7%8E%B0%E8%BF%87%E7%A8%8B%E4%B8%AD%E8%B8%A9%E8%BF%87%E7%9A%84%E5%9D%91" target="_blank" title="#%E5%9B%9B%E3%80%81%E5%AE%9E%E7%8E%B0%E8%BF%87%E7%A8%8B%E4%B8%AD%E8%B8%A9%E8%BF%87%E7%9A%84%E5%9D%91">四、实现过程中踩过的坑</a></p>
<p><a href="https://juejin.cn/post/6984728685106429965#%E4%BA%94%E3%80%81%E5%9B%BE%E4%BE%8B%E7%82%B9%E5%87%BB%E5%90%8E%E5%AF%B9%E5%BA%94%E5%9B%BE%E8%A1%A8%E4%B8%8D%E5%8F%98%E5%8C%96%C2%A0" target="_blank" title="#%E4%BA%94%E3%80%81%E5%9B%BE%E4%BE%8B%E7%82%B9%E5%87%BB%E5%90%8E%E5%AF%B9%E5%BA%94%E5%9B%BE%E8%A1%A8%E4%B8%8D%E5%8F%98%E5%8C%96%C2%A0">五、Highcharts legend图例禁止点击事件的探索及解决</a></p>
<hr>
<p>项目开发过程中，遇到一个需求，在世界地图相应国家中，标注相应参数。最后做出的效果如下图所示，这是符合需求的。接下来我会写一下实现思路以及在实现到发布过程中，遇到的问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/423dab3b517848508d4fd47d6a8aabdb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">一、图表库的比较</h3>
<p>提到世界地图，我们应该很快想到几个图表库。</p>
<p>（1）<strong>Echarts</strong>：这个库我们并不陌生，官方给出的介绍是：ECharts，一个使用 JavaScript 实现的开源可视化库，可以流畅的运行在 PC 和移动设备上，兼容当前绝大部分浏览器（IE8/9/10/11，Chrome，Firefox，Safari等），底层依赖矢量图形库 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fecomfe%2Fzrender" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ecomfe/zrender" ref="nofollow noopener noreferrer">ZRender</a>，提供直观，交互丰富，可高度个性化定制的数据可视化图表。</p>
<p>具体的特性及相关介绍可查看官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fecharts.apache.org%2Fzh%2Ffeature.html" target="_blank" rel="nofollow noopener noreferrer" title="https://echarts.apache.org/zh/feature.html" ref="nofollow noopener noreferrer">echarts.apache.org/zh/feature.…</a>，介绍的很详细。</p>
<p>（2）<strong>Highcharts</strong>：Highcharts 是一个用纯 JavaScript 编写的一个图表库， 能够很简单便捷的在 Web 网站或是 Web 应用程序添加有交互性的图表。本次来写地图相关的内容，我才知道Highcharts 系列软件包含 <strong>Highcharts JS，Highstock JS，Highmaps JS</strong> 共三款软件，均为纯 JavaScript 编写的 HTML5 图表库。</p>
<p>非常牛非常好用, 但是它部分功能是要收费的, 使用之前要让公司帮你买好相应的功能才能用于商用。</p>
<p>同样，具体的内容可查看官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.highcharts.com.cn%2Fdocs%2Fstart-introduction" target="_blank" rel="nofollow noopener noreferrer" title="https://www.highcharts.com.cn/docs/start-introduction" ref="nofollow noopener noreferrer">www.highcharts.com.cn/docs/start-…</a></p>
<p>（3）<strong>G2</strong>：G2 是一套基于可视化编码的图形语法，以数据驱动，具有高度的易用性和扩展性，用户无需关注各种繁琐的实现细节，一条语句即可构建出各种各样的可交互的统计图表。</p>
<p>具体的内容可查看官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fantv%2Fg2-docs%2Fget-started" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/antv/g2-docs/get-started" ref="nofollow noopener noreferrer">www.yuque.com/antv/g2-doc…</a></p>
<p>（4）<strong>D3</strong>：<strong>D3.js</strong>是一个基于数据操作文档的 JavaScript 库。<strong>D3</strong>帮助您使用 HTML、SVG 和 CSS 使数据栩栩如生。D3 对 Web 标准的强调为您提供现代浏览器的全部功能，而无需将自己束缚在专有框架中，结合了强大的可视化组件和数据驱动的 DOM 操作方法。</p>
<p>具体的内容可查看官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fd3js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://d3js.org/" ref="nofollow noopener noreferrer">d3js.org/</a></p>
<p><strong>图表库的比较：</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fduole%2Fp%2F11050784.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/duole/p/11050784.html" ref="nofollow noopener noreferrer">www.cnblogs.com/duole/p/110…</a>这篇文章总结了近20个图表库</p>





















































<table><thead><tr><th></th><th>DataV</th><th>AntV</th><th>Echarts</th><th>Highcharts</th><th>D3js</th></tr></thead><tbody><tr><td>特性</td><td>（1）DataV是一个基于Vue的数据可视化组件库（当然也有React版本）（2）提供用于提升页面视觉效果的SVG边框和装饰（3）提供常用的图表如折线图等</td><td>（1）AntV 是蚂蚁金服全新一代数据可视化解决方案，致力于提供一套简单方便、专业可靠、无限可能的数据可视化最佳实践。（2）G2本身是一门图形语法，简易性和灵活性是在于你学习了这么语法之后，你能够所思即所得，用图形去表达。而他的难点是在于简易性和灵活性建立在学习了语法之后，G2的定位不是一门开箱即用的框架。</td><td>ECharts，一个纯 Javascript 的图表库，可以流畅的运行在 PC 和移动设备上，兼容当前绝大部分浏览器（IE8/9/10/11，Chrome，Firefox，Safari等），底层依赖轻量级的 Canvas 类库 ZRender，提供直观，生动，可交互，可高度个性化定制的数据可视化图表。</td><td>让数据可视化更简单 兼容 IE6+、完美支持移动端、图表类型丰富、方便快捷的 HTML5 交互性图表库</td><td>D3js 是一个可以基于数据来操作文档的 JavaScript 库。可以帮助你使用 HTML, CSS, SVG 以及 Canvas 来展示数据。D3 遵循现有的 Web 标准，可以不需要其他任何框架独立运行在现代浏览器中，它结合强大的可视化组件来驱动 DOM 操作。D3.js 是一个免费的JavaScript库，可以帮助您使用数据创建图像。该工具使您能够将任意数据连接到文档对象模型（DOM），然后将数据驱动的转换应用于文档。通过DOM编程API，程序员可以将文档作为对象访问。</td></tr><tr><td>官方地址</td><td><a href="https://link.juejin.cn/?target=http%3A%2F%2Fdatav.jiaminghi.com%2Fguide%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://datav.jiaminghi.com/guide/" ref="nofollow noopener noreferrer">datav.jiaminghi.com/guide/</a></td><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fantv.vision%2Fzh" target="_blank" rel="nofollow noopener noreferrer" title="https://antv.vision/zh" ref="nofollow noopener noreferrer">antv.vision/zh</a></td><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fecharts.apache.org%2Fzh%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://echarts.apache.org/zh/index.html" ref="nofollow noopener noreferrer">echarts.apache.org/zh/index.ht…</a></td><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.highcharts.com.cn%2Fdocs%2Fhow-to-create-plugins" target="_blank" rel="nofollow noopener noreferrer" title="https://www.highcharts.com.cn/docs/how-to-create-plugins" ref="nofollow noopener noreferrer">www.highcharts.com.cn/docs/how-to…</a></td><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fd3js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://d3js.org/" ref="nofollow noopener noreferrer">d3js.org/</a></td></tr><tr><td>收费情况</td><td>阿里免费</td><td>阿里系免费</td><td>百度开源免费</td><td>美国商用的话需要付费</td><td>免费</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>
<h3 data-id="heading-1">二、Geojson世界地图数据集及中文翻译</h3>
<p>Highcharts官方提供的数据集地址为：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fimg.hcharts.cn%2Fmapdata%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://img.hcharts.cn/mapdata/" ref="nofollow noopener noreferrer">img.hcharts.cn/mapdata/</a></p>
<p>如何使用数据集及数据集字段解析？<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.highcharts.com.cn%2Fdocs%2Fmapdata%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.highcharts.com.cn/docs/mapdata/" ref="nofollow noopener noreferrer">www.highcharts.com.cn/docs/mapdat…</a></p>
<p>上述提到了，Highcharts 系列软件包含 <strong>Highcharts JS，Highstock JS，Highmaps JS</strong> 共三款软件。在实现地图的时候，要使用Highmaps，Highmaps 是继承自 Highcharts 的专门用于地图的图表插件。Highmaps 除了根据值展示地理区域色块外，还支持线段（可以表示公路，河流等）、点（城市，兴趣点等）等其他地理元素。</p>
<p>使用Highmaps：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.highcharts.com.cn%2Fdocs%2Fhighmaps-started" target="_blank" rel="nofollow noopener noreferrer" title="https://www.highcharts.com.cn/docs/highmaps-started" ref="nofollow noopener noreferrer">www.highcharts.com.cn/docs/highma…</a></p>
<p>引入Highcharts的方案：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.highcharts.com.cn%2Fdocs%2Finstall-from-npm" target="_blank" rel="nofollow noopener noreferrer" title="https://www.highcharts.com.cn/docs/install-from-npm" ref="nofollow noopener noreferrer">www.highcharts.com.cn/docs/instal…</a></p>
<p>（1）Geojson数据是什么？（介绍来源于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FgBkQi1dV3OvEgcVol6knsQ" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/gBkQi1dV3OvEgcVol6knsQ" ref="nofollow noopener noreferrer">mp.weixin.qq.com/s/gBkQi1dV3…</a>，这篇文章讲解很详细，可以直接跳转到该文章查看相关内容）</p>
<ol>
<li>geojson是用json的语法表达和存储地理数据，可以说是json的子集，它不是专门js使用的这点要清楚。</li>
<li>地图上有山川, 河流, 海洋等等的地理信息, ，那么如何描述一条河? 这个时候就要使用geojson格式的文件来描绘。</li>
<li>并不是必须用geojson, geojson只是一套规范, 各大解析器用这套规范来解析生成对应的景色, 我们完全可以制定自己的规范来实现这些, 无非是兼容性不好需要自己写绘制的解析器。</li>
</ol>
<p>（2）Geojson详细介绍？</p>
<p><strong>1. 基本结构</strong></p>
<pre><code class="copyable">&#123; // 可以包括点线面, 一个大的集合
  "type": "FeatureCollection", // 定义这个是个geojson文件, 这里还可以是其他值下面会说
  "features": [] // 这里放要绘制的数据
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以后我们看到<code>"type": "FeatureCollection"</code>这样一行就说明这个文件是geojson规范的文件</p>
<p><strong>2. 描述一个点(Feature)</strong><br>
地图上的打点数据</p>
<pre><code class="copyable">&#123;
  "type": "FeatureCollection",
  "features": [
    &#123;
      "type": "Feature",  // 表示这个对象是一个要素
      "properties": &#123;&#125;, // 这里放样式, 后面会专门说
      "geometry": &#123; // 这里面放具体的数据
        "type": "Point",  // 专指画点
        "coordinates": [105.380859375, 31.57853542647338] // 默认是经度与纬度, 三维的话就是xyz三个值, 当然这里也不一定是经纬度(不同的坐标体系)中会讲为什么
      &#125;
    &#125;,
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3. 描述多个点(FeatureCollection)</strong><br>
**优点</p>
<ol>
<li>写法简洁</li>
<li>这些点样式可以共用</li>
</ol>
<pre><code class="copyable">&#123;
  "type": "FeatureCollection",
  "features": [
    &#123;
      "type": "Feature",
      "properties": &#123;&#125;,
      "geometry": &#123;
        "type": "MultiPoint", // 多点, 也就是连续画多个同样的点
        "coordinates": [[105.380859375, 31.57853542647338],
        [105.580859375, 31.52853542647338]
        ]
      &#125;
    &#125;,
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4. 描述一条线(LineString)</strong></p>
<ol>
<li>这里还是描绘每一个点, 但这些点会连接在一起形成线</li>
<li>地图上的连线数据</li>
</ol>
<pre><code class="copyable">&#123;
  "type": "FeatureCollection",
  "features": [
    &#123;
      "type": "Feature",
      "properties": &#123;&#125;,
      "geometry": &#123;
        "type": "LineString", // 这里所有的点会连接在一起形成线
        "coordinates": [[105.6005859375, 30.65681556429287],
        [107.95166015624999, 31.98944183792288],
        [109.3798828125, 30.031055426540206],
        [107.7978515625, 29.935895213372444]]
      &#125;
    &#125;,
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>5. 描述多条线(MultiLineString)</strong></p>
<ol>
<li>这里第二组与第一组的线, 可以分隔开不会首尾相连.</li>
</ol>
<pre><code class="copyable">&#123;
  "type": "FeatureCollection",
  "features": [
    &#123;
      "type": "Feature",
      "properties": &#123;&#125;,
      "geometry": &#123;
        "type": "MultiLineString",
        "coordinates":
          [
            [
              [105.6005859375, 30.65681556429287],
              [107.95166015624999, 31.98944183792288],
              [109.3798828125, 30.031055426540206],
              [107.7978515625, 29.935895213372444]
            ],
            [
              [109.3798828125, 30.031055426540206],
              [107.1978515625, 31.235895213372444]
            ]
          ]
      &#125;
    &#125;,
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6. 描述一个面(Polygon, 也叫多边形)</strong></p>
<ol>
<li>第一个点与最后一个点要相同, 这样才能完成闭环!!</li>
<li>三维数组的格式需要注意</li>
</ol>
<pre><code class="copyable">&#123;
  "type": "FeatureCollection",
  "features": [
    &#123;
      "type": "Feature",
      "properties": &#123;&#125;,
      "geometry": &#123;
        "type": "Polygon", // 注意这里是三维数组
        "coordinates": [
          [
            [106.10595703125, 33.33970700424026],
            [106.32568359375, 32.41706632846282],
            [108.03955078125, 32.2313896627376],
            [108.25927734375, 33.15594830078649],
            [106.10595703125, 33.33970700424026]
          ]
        ]
      &#125;
    &#125;,
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>7. 一个面里面有多个面(Polygon)</strong></p>
<ol>
<li>这种单一的'Polygon'里面出现多个形状, 会出现中空的情况, 类似布尔运算, 这样就可以在地图中描述那种圈型的国家</li>
</ol>
<pre><code class="copyable">&#123;
  "type": "FeatureCollection",
  "features": [
    &#123;
      "type": "Feature",
      "properties": &#123;&#125;,
      "geometry": &#123;
        "type": "Polygon",
        "coordinates": [
          [
            [
              -39.7265625,
              -3.162455530237848
            ],
            [
              127.96875,
              -3.162455530237848
            ],
            [
              127.96875,
              74.1160468394894
            ],
            [
              -39.7265625,
              74.1160468394894
            ],
            [
              -39.7265625,
              -3.162455530237848
            ]
          ],
          [
            [
              -22.5,
              15.961329081596647
            ],
            [
              110.74218749999999,
              15.961329081596647
            ],
            [
              110.74218749999999,
              70.8446726342528
            ],
            [
              -22.5,
              70.8446726342528
            ],
            [
              -22.5,
              15.961329081596647
            ]
          ]
        ]
      &#125;
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下:<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afac9151cd8c499780b14fe4f9a2d186~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>8. 描述多个面(MultiPolygon)</strong><br>
优势:</p>
<ol>
<li>写法简洁</li>
<li>这些点样式可以共用</li>
</ol>
<pre><code class="copyable">&#123;
  "type": "FeatureCollection",
  "features": [
    &#123;
      "type": "Feature",
      "properties": &#123;&#125;,
      "geometry": &#123;
        "type": "MultiPolygon",
        "coordinates": [
          [
          [
            [
              -39.7265625,
              -3.162455530237848
            ],
            [
              127.96875,
              -3.162455530237848
            ],
            [
              127.96875,
              74.1160468394894
            ],
            [
              -39.7265625,
              74.1160468394894
            ],
            [
              -39.7265625,
              -3.162455530237848
            ]
          ]
        ],
        [
          [
            [
              -22.5,
              15.961329081596647
            ],
            [
              110.74218749999999,
              15.961329081596647
            ],
            [
              110.74218749999999,
              70.8446726342528
            ],
            [
              -22.5,
              70.8446726342528
            ],
            [
              -22.5,
              15.961329081596647
            ]
          ]
        ]
        ]
      &#125;
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里如果重叠了就是颜色的叠加了如图所示:<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47739fcec6e348f78b7d073fb356f554~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>9. 描述一个组(geometries)</strong></p>
<ol>
<li>比如我们为了表示一种特定的地貌那么我们可以把这个地貌数据独立起来</li>
</ol>
<pre><code class="copyable">&#123;
  "type": "FeatureCollection",
  "features": [
    &#123; // 可以包括点线面, 一个独立的集合
      "type": "GeometryCollection",
      "geometries": [
        &#123;
          "type": "Point",
          "coordinates": [108.62, 31.02819]
        &#125;, &#123;
          "type": "LineString",
          "coordinates": [[108.896484375, 30.1071178870],
          [108.2184375, 30.91717870],
          [109.5184375, 31.2175780]]
        &#125;
      ]
    &#125;
  ]
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>10. 不同的样式(properties)</strong></p>
<pre><code class="copyable">&#123;
  "type": "FeatureCollection",
  "features": [
     &#123;
      "type": "Feature",
      "properties": &#123; // 专门放属性
        "stroke": "#fa9661", // 外边颜色
        "stroke-width": 4.1, // 外边宽
        "stroke-opacity": 0.7, // 外边透明度
        "fill": "#9e290c",  // 填充色
        "fill-opacity": 0.7 // 填充色透明度
      &#125;,
      "geometry": &#123;
        "type": "Point",  // 画点
        "coordinates": [105.380859375, 31.57853542647338]
      &#125;
    &#125;,
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">三、Highcharts实现世界地图（含详细代码）</h3>
<p>ECharts实现地图Demo：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fwangcunhuazi%2Farticle%2Fdetails%2F41621911" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/wangcunhuazi/article/details/41621911" ref="nofollow noopener noreferrer">blog.csdn.net/wangcunhuaz…</a></p>
<p>别人的实现Demo（记录使用Highmaps创建世界地图）：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_42282789%2Farticle%2Fdetails%2F106368763" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_42282789/article/details/106368763" ref="nofollow noopener noreferrer">blog.csdn.net/qq_42282789…</a></p>
<p>别人的实现Demo（关于在echarts中使用geo.json渲染地图的方法）：<a href="https://juejin.cn/post/6971239249135796237" target="_blank" title="https://juejin.cn/post/6971239249135796237">juejin.cn/post/697123…</a></p>
<p>在Vue中使用Highcharts：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.jianshukeji.com%2Fhighcharts%2Fuse-highcharts-with-vue.html" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.jianshukeji.com/highcharts/use-highcharts-with-vue.html" ref="nofollow noopener noreferrer">blog.jianshukeji.com/highcharts/…</a></p>
<p>highcharts-Highmaps 动态传入城市名称：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bbsmax.com%2FA%2FA2dmZGABze%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bbsmax.com/A/A2dmZGABze/" ref="nofollow noopener noreferrer">www.bbsmax.com/A/A2dmZGABz…</a></p>
<p>Highcharts实现世界地图官方DEMO：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjshare.com.cn%2Fmapdata%2FCN4fQa%3Fmap%3Dcustom%2Fworld-palestine-highres" target="_blank" rel="nofollow noopener noreferrer" title="https://jshare.com.cn/mapdata/CN4fQa?map=custom/world-palestine-highres" ref="nofollow noopener noreferrer">jshare.com.cn/mapdata/CN4…</a></p>
<p><strong>Highcharts提供的Geojson世界地图数据集的国家名称中文翻译</strong></p>
<p>其中，我需要展示的国家名称是中文，但是找了好多数据集全是英文，因此对国家名称进行了统一的翻译，主要是根据**提供的语言翻译包来进行对比处理的。有需要该文档的同学可以联系我。</p>
<p>翻译资源如图：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44250c0cfe424bf387cf684ff9c4f647~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>世界地图具体实现代码：</p>
<p>html代码：</p>
<pre><code class="copyable"><!-- 地图数据信息，用于地图数据地址与名字的映射 -->
<div id="container">加载地图数据中</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>js代码： </p>
<pre><code class="copyable">import template from './template.html'
import './style.less'
// 数据集，翻译之后的，保存到本地了
import &#123; WORLDDATA &#125; from './world'
import Highmaps from 'highcharts/modules/map'
Highmaps(window.Highcharts)

let WorldMapComponent = &#123;
  name: 'worldmap',
  props: &#123;
    worldMapData: &#123;
      type: Array,
      default: function () &#123;
        return &#123;&#125;
      &#125;
    &#125;
  &#125;,
  data () &#123;
    return &#123;
      worldData: WORLDDATA
    &#125;
  &#125;,
  watch: &#123;
    worldMapData (data) &#123;
      this.initMapData(data)
    &#125;
  &#125;,
  methods: &#123;
    initMapData (resData) &#123;
      var mapdata = this.worldData
      var data = []
      resData.length && resData.forEach(element => &#123;
        mapdata.features.length && mapdata.features.forEach(md => &#123;
          if (mapdata.features) &#123;
            if (element.geo.includes(md.properties['name'])) &#123;
              let color = ''
              switch (element.level) &#123;
                case 'a':
                  color = '#67cc02'
                  break
                case 'b':
                  color = '#ffe100'
                  break
                case 'c':
                  color = '#fab011'
                  break
                case 'd':
                  color = '#ff523f'
                  break
              &#125;
              data.push(&#123;
                'hc-key': md.properties['hc-key'],
                value: element.counts,
                color: color
              &#125;)
            &#125;
          &#125;
        &#125;)
      &#125;)
      // 初始化图表
      window.$('#container').highcharts('Map', &#123;
        mapNavigation: &#123;
          enabled: true,
          buttonOptions: &#123;
            verticalAlign: 'bottom'
          &#125;
        &#125;,
        // 控制图例
        colorAxis: &#123;
          // 下面的图例是长条渐变色
          // min: 0,
          // stops: [
          //   [0, window.Highcharts.getOptions().colors[5]],
          //   [0.5, window.Highcharts.getOptions().colors[4]],
          //   [0.75, window.Highcharts.getOptions().colors[3]],
          //   [1, window.Highcharts.getOptions().colors[13]]
          // ]
          dataClasses: [&#123;
            from: -1,
            to: 0,
            color: '#67cc02',
            name: 'a'
          &#125;, &#123;
            from: 0,
            to: 1,
            color: '#ffe100',
            name: 'b'
          &#125;, &#123;
            from: 2,
            to: 3,
            name: 'c',
            color: '#fab011'
          &#125;, &#123;
            from: 3,
            to: 4,
            name: 'd,
            color: '#ff523f'
          &#125;]
        &#125;,
        tooltip: &#123;
          formatter: function () &#123;
            let str = ''
            this.point.colorArr.forEach((item, index) => &#123;
              console.log(item)
              // eslint-disable-next-line
              str += `<span style="color: $&#123;item&#125;">●</span>攻击次数: <b>$&#123;this.point.valueArr[index]&#125;</b><br>`
            &#125;)
            // eslint-disable-next-line
            return `位置: <b>$&#123;this.point.name&#125;</b><br>$&#123;str&#125;`
          &#125;
        &#125;,
        // 不显示标题
        title: &#123;
          text: null
        &#125;,
        // 去掉highcharts的水印
        credits: &#123;
          enabled: false
        &#125;,
        series: [&#123;
          data: data,
          mapData: mapdata,
          joinBy: 'hc-key',
          name: 'abcd',
          states: &#123;
            hover: &#123;
              color: '#a4edba'
            &#125;
          &#125;,
          dataLabels: &#123;
            enabled: false,
            format: '&#123;point.name&#125;'
          &#125;
        &#125;]
      &#125;)
    &#125;
  &#125;,
  template
&#125;
WorldMapComponent.install = function (Vue) &#123;
  Vue.component(this.name, WorldMapComponent)
&#125;
export default WorldMapComponent
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">四、实现过程中踩过的坑</h3>
<p>（1）报错：Uncaught Error: Highcharts error #16 </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62b268a627824188ac9f806effaafe35~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决方案参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fw926498%2Farticle%2Fdetails%2F80536829" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/w926498/article/details/80536829" ref="nofollow noopener noreferrer">blog.csdn.net/w926498/art…</a></p>
<p>（2）报错：Uncaught TypeError: (intermediate value)(intermediate value)(...) is not a funtion：解决方案参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fxubuhui%2Farticle%2Fdetails%2F103321990" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/xubuhui/article/details/103321990" ref="nofollow noopener noreferrer">blog.csdn.net/xubuhui/art…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53707fb0ad5e4ffb83f5bbd8e0ccddfa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（3）世界地图实现后，本地运行没有任何问题，但是部署到线上的时候，报错：</p>
<pre><code class="copyable">Uncaught TypeError: Array.prototype.forEach called on null or undefined at highcharts.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当时但从报错来看，以为没有处理空数据的情况，因此把所有涉及数组的地方都处理了一遍，重新部署，结果还是报同样的错。 </p>
<p>最后发现是highcharts版本的问题，本地用的是6.2.0，但是部署后线上用的是6.0.7，将线上的版本替换，问题解决。</p>
<p>（4）legend由长条形改为圆形</p>
<pre><code class="copyable">// 控制图例
        colorAxis: &#123;
          // 下面的图例是长条渐变色
          // min: 0,
          // stops: [
          //   [0, window.Highcharts.getOptions().colors[5]],
          //   [0.5, window.Highcharts.getOptions().colors[4]],
          //   [0.75, window.Highcharts.getOptions().colors[3]],
          //   [1, window.Highcharts.getOptions().colors[13]]
          // ]
          dataClasses: [&#123;
            from: -1,
            to: 0,
            color: '#67cc02',
            name: '低危'
          &#125;, &#123;
            from: 0,
            to: 1,
            color: '#ffe100',
            name: '中危'
          &#125;, &#123;
            from: 2,
            to: 3,
            name: '高危',
            color: '#fab011'
          &#125;, &#123;
            from: 3,
            to: 4,
            name: '危急',
            color: '#ff523f'
          &#125;]
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（5）不显示highcharts的水印：</p>
<pre><code class="copyable">// 去掉highcharts的水印
credits: &#123;
    enabled: false
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">五、Highcharts legend图例禁止点击事件的探索及解决</h3>
<p>这个问题我之前没有注意到，测试提了一个bug。确实，这样处理之后，点击下面的图例，只有对应点击的图例会置灰，但是图标上没有任何变化，这肯定是不行的。</p>
<p>这个问题如何解决，我探索了好久。最初的方向是，点击之后，如何才能关联到图表中的数据，做出相应的改变，所以我从官网看了好多demo。</p>
<p>比如这个：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.highcharts.com.cn%2Fdemo%2Fhighmaps%2Fdata-class-two-ranges" target="_blank" rel="nofollow noopener noreferrer" title="https://www.highcharts.com.cn/demo/highmaps/data-class-two-ranges" ref="nofollow noopener noreferrer">www.highcharts.com.cn/demo/highma…</a>，人家的demo命名没有做特殊处理，点击小圆圈就会改变UI的。</p>
<p>还有这个：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjshare.com.cn%2Fhighmaps%2Fhhhhva" target="_blank" rel="nofollow noopener noreferrer" title="https://jshare.com.cn/highmaps/hhhhva" ref="nofollow noopener noreferrer">jshare.com.cn/highmaps/hh…</a></p>
<p>还有这个：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjshare.com.cn%2Fhighmaps%2FI4p8zm" target="_blank" rel="nofollow noopener noreferrer" title="https://jshare.com.cn/highmaps/I4p8zm" ref="nofollow noopener noreferrer">jshare.com.cn/highmaps/I4…</a></p>
<p>我发现他们都没有做单独特殊的处理，那我在这儿应该也不用做处理才对。但是我的并没有生效。</p>
<p>后来我懂了，我这个图和上述几个demo的性质是不一样的。我这个图是用世界地图改造而来的。</p>
<p>我这个图的原型是这样子：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.highcharts.com.cn%2Fdemo%2Fhighmaps%2Fall-maps" target="_blank" rel="nofollow noopener noreferrer" title="https://www.highcharts.com.cn/demo/highmaps/all-maps" ref="nofollow noopener noreferrer">www.highcharts.com.cn/demo/highma…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16b92f8d76e749dc8776422e67de0e8b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> 图例很明显，跟我现在用的不一样，并且上图中，点击图例之后，世界地图并没有任何改变。而我现在是加了下述代码之后实现的圆点的图例。目前为止，我觉得是这个原因。</p>
<pre><code class="copyable">        // 控制图例
        colorAxis: &#123;
          dataClasses: [&#123;
            name: '危急',
            color: '#ff523f'
          &#125;, &#123;
            name: '高危',
            color: '#fab011'
          &#125;, &#123;
            color: '#ffe100',
            name: '中危'
          &#125;, &#123;
            color: '#67cc02',
            name: '低危'
          &#125;]
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候我改变了方向，能否控制图例，不能触发点击事件。确实，对应这个问题是有相应API的，就是这个legendItemClick，无论是官网还是很多人的介绍，都是用它，但是我加上之后并没有效果。</p>
<p>大家几乎都是这样来处理的，但是我的并没有效果。</p>
<pre><code class="copyable">       plotOptions: &#123;
          series: &#123;
            events: &#123;
              //控制图标的图例legend不允许切换
             legendItemClick: function (even)&#123;                                    
                return false  //return  true 则表示允许切换
              &#125;
            &#125;
          &#125;
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实针对colorAxis，官方也提供了相应的legendItemClick事件，但是同样。我处理的时候并没有生效。官方介绍：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fapi.highcharts.com%2Fhighcharts%2FcolorAxis.events.legendItemClick" target="_blank" rel="nofollow noopener noreferrer" title="https://api.highcharts.com/highcharts/colorAxis.events.legendItemClick" ref="nofollow noopener noreferrer">api.highcharts.com/highcharts/…</a></p>
<p>现在这个问题终于解决了，是看到有同学自定义了方法，给了我启发，同学的介绍如链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_43860703%2Farticle%2Fdetails%2F111520257" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_43860703/article/details/111520257" ref="nofollow noopener noreferrer">blog.csdn.net/weixin_4386…</a></p>
<p>我用上之后，生效了，阻止了事件的触发。</p>
<pre><code class="copyable">      // 自定义图例事件
      window.Highcharts.wrap(window.Highcharts.Legend.prototype, 'renderItem', 
        function(proceed, item) &#123;
        proceed.call(this, item)
        var element = item.legendGroup.element
        // 图例点击事件
        element.onclick = function() &#123;
          return false
        &#125;
      &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看了下官网，原来这是提供的二次扩展的一个API。</p>
<p><strong>通过 prototype 重新函数</strong></p>
<p>JavaScript 在动态更改脚本行为方面表现的非常强大。在 Highcharts 内部，我们创建了一个工具函数 <code>wrap</code>，该函数可以在现有原型函数执行之前或之后添加自己的业务代码，其构造及参数说明如下：</p>
<p><code>Highcharts.wrap(object obj, String methodName, function callback)</code></p>
<ul>
<li>obj：需要封装的函数的父级对象</li>
<li>methodName: 函数名</li>
<li>callback: 回调函数</li>
</ul>
<p>其中原始函数以第一个参数传递给封装函数，原始函数的其他参数在第一个参数后传递给封装函数，下面是示例代码：</p>
<pre><code class="copyable">H.wrap(H.Series.prototype, 'drawGraph', function(proceed) &#123;

  // 原始函数执行之前编写的逻辑代码
  console.log("We are about to draw the graph: ", this.graph);

  // 执行原始函数（proceed）, arguments 为原始函数参数（第一个参数是原始函数）
  proceed.apply(this, Array.prototype.slice.call(arguments, 1));

  // 原始函数执行之后的逻辑代码
  console.log("We just finished drawing the graph: ", this.graph);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            