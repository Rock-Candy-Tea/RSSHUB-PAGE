
---
title: '周末在家学Echarts'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c886820c113403290378574519cba81~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 22:22:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c886820c113403290378574519cba81~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>周末在家没事，做了两个数据可视化的echarts图表，学到了很多有关echarts的知识点。现在总结一下，供各位同学一起学习，成长。</p>
<h3 data-id="heading-0">需求</h3>
<p>图表的练习
一、深入学习echarts5，并总结
二、做一个练习
1、使用dataset
2、总结一下公共的配置
3、react技术栈，ts语言
4、组件使用antd
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c886820c113403290378574519cba81~tplv-k3u1fbpfcp-zoom-1.image" alt="以上为图1-1" loading="lazy" referrerpolicy="no-referrer">
图1-1</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a008bc87b4c244b8b33af1ce5a07bce0~tplv-k3u1fbpfcp-zoom-1.image" alt="以上为土1-2" loading="lazy" referrerpolicy="no-referrer">
以上为图1-2</p>
<h3 data-id="heading-1">效果图</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d21a63f9233a406689df8b674387ad6b~tplv-k3u1fbpfcp-zoom-1.image" alt="图2-1" loading="lazy" referrerpolicy="no-referrer">
以上为 图2-1</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc227337cad54e1f950e2984a9bc599f~tplv-k3u1fbpfcp-zoom-1.image" alt="图2-2" loading="lazy" referrerpolicy="no-referrer">
图2-2</p>
<h3 data-id="heading-2">思路</h3>
<h4 data-id="heading-3">分析需求图1-1</h4>
<p>首先是需求图1-1. 是一个典型的双y轴，柱形图加折线图。可以使用这个案例来改造。
<a href="https://echarts.apache.org/examples/zh/editor.html?c=mix-line-bar" target="_blank" rel="nofollow noopener noreferrer">折柱混合</a>
双y轴的话 主要是使用下面代码配置</p>
<pre><code class="hljs language-js copyable" lang="js">yAxis: [
    &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'value'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'水量'</span>,
        <span class="hljs-attr">min</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">max</span>: <span class="hljs-number">250</span>,
        <span class="hljs-attr">interval</span>: <span class="hljs-number">50</span>,
        <span class="hljs-attr">axisLabel</span>: &#123;
            <span class="hljs-attr">formatter</span>: <span class="hljs-string">'&#123;value&#125; ml'</span>
        &#125;
    &#125;,
    &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'value'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'温度'</span>,
        <span class="hljs-attr">min</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">max</span>: <span class="hljs-number">25</span>,
        <span class="hljs-attr">interval</span>: <span class="hljs-number">5</span>,
        <span class="hljs-attr">axisLabel</span>: &#123;
            <span class="hljs-attr">formatter</span>: <span class="hljs-string">'&#123;value&#125; °C'</span>
        &#125;
    &#125;
],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于图表中一些自定义的元素，如，右上角的二个元素，如下图3-1
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fafca7474f340de915d33b5d52ac161~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
这两个元素可以使用 echarts中的 <code>graphic</code> 的 <code>elements</code> 属性。
如下图 3-2时对<code>graphic</code> 属性的简短解释。可以使用这个属性将一些图片，文本，圆，线，多面图，矩形，线，元素群组，添加到图表的指定位置。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2ad1776dcc64f5797fb5906d683999d~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
此外由于该图表有二个产品，一个全部。所以使用的是dataset的数据源来存储图表的数据。</p>
<p>如下是<code>全部产品</code>的数据</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> dataseSource = [
      [<span class="hljs-string">'product'</span>, <span class="hljs-string">'已交付'</span>, <span class="hljs-string">'累计百分比'</span>],
      [<span class="hljs-string">'批次1'</span>, <span class="hljs-number">850</span>, <span class="hljs-number">21</span>],
      [<span class="hljs-string">'批次2'</span>, <span class="hljs-number">1500</span>, <span class="hljs-number">36</span>],
      [<span class="hljs-string">'批次3'</span>, <span class="hljs-number">1800</span>, <span class="hljs-number">43</span>],
      [<span class="hljs-string">'批次4'</span>, <span class="hljs-number">2700</span>, <span class="hljs-number">65</span>],
      [<span class="hljs-string">'批次5'</span>, <span class="hljs-number">2600</span>, <span class="hljs-number">72</span>],
      [<span class="hljs-string">'批次6'</span>, <span class="hljs-number">2700</span>, <span class="hljs-number">85</span>],
      [<span class="hljs-string">'下一批次'</span>, <span class="hljs-number">3220</span>, <span class="hljs-number">80</span>],
    ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击产品D，或产品E ，只要修改数据源，重新设置图表options就可以了。</p>
<p>此外还有一点，就是折线图的label属性是个动态值，大于50，字体变红，并增加一个警告图标。
此方案是这样实现的,主要是用 label中的<code>rich</code> 属性与 <code>formatter</code>属性.
rich 用于设置样式，就像为css中的class增加样式。
而 formatter 则可为不同的折线点，设置不用的样式。使用这种写法 <code>&#123;b| value&#125;</code> b为样式的名称，value为要显示的文本，或值。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'累计百分比'</span>,
  <span class="hljs-attr">type</span>: <span class="hljs-string">'line'</span>,
  <span class="hljs-attr">label</span>: &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">distance</span>: <span class="hljs-number">5</span>,
      <span class="hljs-attr">rich</span>:&#123;
          <span class="hljs-attr">red</span>:&#123;<span class="hljs-attr">color</span>:<span class="hljs-string">'red'</span>,<span class="hljs-attr">fontSize</span>:<span class="hljs-number">14</span>&#125;,
          <span class="hljs-attr">b</span>: &#123;
              <span class="hljs-attr">backgroundColor</span>: &#123;
                <span class="hljs-attr">image</span>: <span class="hljs-string">'https://img-blog.csdnimg.cn/2021070312161116.png'</span>
              &#125;,
              <span class="hljs-attr">height</span>: <span class="hljs-number">30</span>,
            &#125;,
      &#125;,
      <span class="hljs-attr">formatter</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">params</span>) </span>&#123;
          <span class="hljs-keyword">const</span> &#123; data &#125; = params;
          <span class="hljs-keyword">const</span> value = data[<span class="hljs-number">2</span>]
        <span class="hljs-keyword">if</span> (value > <span class="hljs-number">50</span>) &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-string">"&#123;red|"</span> + value + <span class="hljs-string">"%&#125;&#123;b| &#125;"</span>
        &#125;
        <span class="hljs-keyword">return</span> value+<span class="hljs-string">"%"</span>
      &#125;
  &#125;,
  <span class="hljs-attr">yAxisIndex</span>: <span class="hljs-number">1</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">分析需求图1-2</h4>
<p>需求图1-2 难点是在贴图的处理上。
由于是一个类目累加的柱状图，又称堆叠柱状图。因此可以基于该图例改造实现。
<a href="https://echarts.apache.org/examples/zh/editor.html?c=bar-stack" target="_blank" rel="nofollow noopener noreferrer">堆叠柱状图</a>
堆叠柱状体 主要是在 <code>series</code> 中设置该属<code>stack: 'total',</code> 及可将同样设置<code>stack: 'total'</code> 的series 。堆积起来。
此外，该图例需要开始 贴图。不开启，设置了贴图是不会显示的。</p>
<pre><code class="hljs language-js copyable" lang="js">aria: &#123;
    <span class="hljs-attr">enabled</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">decal</span>: &#123;
        <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置蓝色的 已用产能 贴图。</p>
<pre><code class="hljs language-js copyable" lang="js">itemStyle:&#123;
    <span class="hljs-attr">decal</span>:&#123;
        <span class="hljs-attr">symbol</span>: <span class="hljs-string">'rect'</span>,
        <span class="hljs-attr">symbolSize</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">maxTileWidth</span>:<span class="hljs-number">512</span>,
        <span class="hljs-attr">maxTileHeight</span>:<span class="hljs-number">512</span>,
        <span class="hljs-attr">symbolKeepAspect</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">dashArrayX</span>: [<span class="hljs-number">1</span>,<span class="hljs-number">0</span>],
        <span class="hljs-attr">dashArrayY</span>: [<span class="hljs-number">2</span>,<span class="hljs-number">2</span>],
        <span class="hljs-attr">color</span>: <span class="hljs-string">'#5470c6'</span>,
        <span class="hljs-comment">// rotation: 0.5235987755982988</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有关 属性<code>decal</code> 的更多解释 请看。
<a href="https://echarts.apache.org/zh/option.html#series-line.itemStyle.decal" target="_blank" rel="nofollow noopener noreferrer">decal详细解释</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8d0c45b4f994c9cb6634a62f7cac555~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">代码</h3>
<h4 data-id="heading-6">图1-1的核心代码</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> allData = []
<span class="hljs-comment">//[21,36,43,65,72,85,92]</span>
<span class="hljs-comment">// [850,1500,1800,2700,2600,2700,3220]</span>
<span class="hljs-keyword">const</span> proD = []
<span class="hljs-keyword">const</span> proE = []
<span class="hljs-keyword">const</span> dataseSource = [
      [<span class="hljs-string">'product'</span>, <span class="hljs-string">'已交付'</span>, <span class="hljs-string">'累计百分比'</span>],
      [<span class="hljs-string">'批次1'</span>, <span class="hljs-number">850</span>, <span class="hljs-number">21</span>],
      [<span class="hljs-string">'批次2'</span>, <span class="hljs-number">1500</span>, <span class="hljs-number">36</span>],
      [<span class="hljs-string">'批次3'</span>, <span class="hljs-number">1800</span>, <span class="hljs-number">43</span>],
      [<span class="hljs-string">'批次4'</span>, <span class="hljs-number">2700</span>, <span class="hljs-number">65</span>],
      [<span class="hljs-string">'批次5'</span>, <span class="hljs-number">2600</span>, <span class="hljs-number">72</span>],
      [<span class="hljs-string">'批次6'</span>, <span class="hljs-number">2700</span>, <span class="hljs-number">85</span>],
      [<span class="hljs-string">'下一批次'</span>, <span class="hljs-number">3220</span>, <span class="hljs-number">80</span>],
    ]

option = &#123;
    <span class="hljs-attr">color</span>: [<span class="hljs-string">'#53f3f3'</span>, <span class="hljs-string">'#fff85f'</span>, <span class="hljs-string">'#EE6666'</span>],
    <span class="hljs-attr">textStyle</span>: &#123;<span class="hljs-attr">color</span>: <span class="hljs-string">'#fff'</span>&#125;,
    <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">'#020403'</span>,<span class="hljs-comment">//背景色</span>
    <span class="hljs-attr">dataset</span>: &#123;
      <span class="hljs-attr">source</span>: dataseSource,
    &#125;,
    <span class="hljs-attr">graphic</span>: &#123;
      <span class="hljs-attr">elements</span>: [
        &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">'rect'</span>,
          <span class="hljs-attr">x</span>: <span class="hljs-number">120</span>,
          <span class="hljs-attr">y</span>: <span class="hljs-number">10</span>,
          <span class="hljs-attr">shape</span>: &#123;
            <span class="hljs-attr">width</span>: <span class="hljs-number">150</span>,
            <span class="hljs-attr">height</span>: <span class="hljs-number">50</span>
          &#125;,
          <span class="hljs-attr">style</span>: &#123;
            <span class="hljs-attr">fill</span>: <span class="hljs-string">'rgba(255,255,255,.6)'</span>
          &#125;
        &#125;,
        &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">'rect'</span>,
          <span class="hljs-attr">x</span>: <span class="hljs-number">320</span>,
          <span class="hljs-attr">y</span>: <span class="hljs-number">10</span>,
          <span class="hljs-attr">shape</span>: &#123;
            <span class="hljs-attr">width</span>: <span class="hljs-number">150</span>,
            <span class="hljs-attr">height</span>: <span class="hljs-number">50</span>
          &#125;,
          <span class="hljs-attr">style</span>: &#123;
            <span class="hljs-attr">fill</span>: <span class="hljs-string">'rgba(255,255,255,.5)'</span>
          &#125;
        &#125;,
        &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">'image'</span>,
          <span class="hljs-attr">style</span>: &#123;
            <span class="hljs-attr">image</span>: <span class="hljs-string">'data:i yf8A/9k='</span>,
            <span class="hljs-attr">x</span>: <span class="hljs-number">325</span>,
            <span class="hljs-attr">y</span>: <span class="hljs-number">15</span>,
            <span class="hljs-attr">width</span>: <span class="hljs-number">40</span>,
            <span class="hljs-attr">height</span>: <span class="hljs-number">40</span>
          &#125;,
          <span class="hljs-attr">onclick</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(data)
          &#125;
        &#125;,
        &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">'text'</span>,
          <span class="hljs-attr">x</span>: <span class="hljs-number">180</span>,
          <span class="hljs-attr">y</span>: <span class="hljs-number">20</span>,
          <span class="hljs-attr">style</span>: &#123;
            <span class="hljs-attr">fill</span>: <span class="hljs-string">'#000'</span>,
            <span class="hljs-attr">text</span>: <span class="hljs-string">'9999'</span>,
            <span class="hljs-attr">font</span>: <span class="hljs-string">'bold 34px Microsoft YaHei'</span>,
          &#125;,
          <span class="hljs-attr">onclick</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(data)
            <span class="hljs-built_in">console</span>.log( <span class="hljs-built_in">arguments</span>)
            <span class="hljs-keyword">const</span> &#123; target&#125; = data;
            target.style.text = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random()*<span class="hljs-number">1000</span>)+<span class="hljs-string">""</span>;
          &#125;
        &#125;,
        &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">'text'</span>,
          <span class="hljs-attr">x</span>: <span class="hljs-number">380</span>,
          <span class="hljs-attr">y</span>: <span class="hljs-number">20</span>,
          <span class="hljs-attr">style</span>: &#123;
            <span class="hljs-attr">fill</span>: <span class="hljs-string">'#000'</span>,
            <span class="hljs-attr">text</span>: <span class="hljs-string">'12H'</span>,
            <span class="hljs-attr">font</span>: <span class="hljs-string">'bold 34px Microsoft YaHei'</span>,
          &#125;
        &#125;,
        &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">'image'</span>,
          <span class="hljs-attr">style</span>: &#123;
            <span class="hljs-attr">image</span>: <span class="hljs-string">'data:image/png; /9k='</span>,
            <span class="hljs-attr">x</span>: <span class="hljs-number">125</span>,
            <span class="hljs-attr">y</span>: <span class="hljs-number">15</span>,
            <span class="hljs-attr">width</span>: <span class="hljs-number">40</span>,
            <span class="hljs-attr">height</span>: <span class="hljs-number">40</span>
          &#125;
        &#125;,
        
        &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'group'</span>,
            <span class="hljs-attr">bottom</span>: <span class="hljs-number">20</span>,
            <span class="hljs-attr">children</span>: [
                &#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'image'</span>,<span class="hljs-attr">style</span>:&#123;<span class="hljs-attr">image</span>:<span class="hljs-string">'dat A/9k'</span>&#125; &#125;,
                &#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'text'</span>, <span class="hljs-attr">left</span>:<span class="hljs-number">10</span>, <span class="hljs-attr">style</span>: &#123;
                    <span class="hljs-attr">fill</span>: <span class="hljs-string">'#fff85f'</span>,
                <span class="hljs-attr">text</span>: <span class="hljs-string">'全部'</span>,
                <span class="hljs-attr">font</span>: <span class="hljs-string">'bold 34px Microsoft YaHei'</span>,&#125;&#125;
            ],
            <span class="hljs-attr">onclick</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(data)
          &#125;
         
        &#125;,
        &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'group'</span>,
            <span class="hljs-attr">bottom</span>: <span class="hljs-number">20</span>,
            <span class="hljs-attr">left</span>: <span class="hljs-number">120</span>,
            <span class="hljs-attr">children</span>: [
                &#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'image'</span>,<span class="hljs-attr">style</span>:&#123;<span class="hljs-attr">image</span>:<span class="hljs-string">'d  9k'</span>&#125; &#125;,
                &#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'text'</span>, <span class="hljs-attr">style</span>: &#123;
                    <span class="hljs-attr">fill</span>: <span class="hljs-string">'#fff'</span>,
            <span class="hljs-attr">text</span>: <span class="hljs-string">'产品D'</span>,
            <span class="hljs-attr">font</span>: <span class="hljs-string">'bold 34px Microsoft YaHei'</span>,&#125;&#125;
            ],
            <span class="hljs-attr">onclick</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(data)
          &#125;
         
        &#125;,
        &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'group'</span>,
            <span class="hljs-attr">bottom</span>: <span class="hljs-number">20</span>,
            <span class="hljs-attr">left</span>: <span class="hljs-number">240</span>,
            <span class="hljs-attr">children</span>: [
                &#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'image'</span>,<span class="hljs-attr">style</span>:&#123;<span class="hljs-attr">image</span>:<span class="hljs-string">' 9k'</span>&#125; &#125;,
                &#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'text'</span>, <span class="hljs-attr">style</span>: &#123;
                    <span class="hljs-attr">fill</span>: <span class="hljs-string">'#fff'</span>,
            <span class="hljs-attr">text</span>: <span class="hljs-string">'产品E'</span>,
            <span class="hljs-attr">font</span>: <span class="hljs-string">'bold 34px Microsoft YaHei'</span>,&#125;&#125;
            ],
            <span class="hljs-attr">onclick</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(data)
          &#125;
         
        &#125;,
        
      ]
    &#125;,
    <span class="hljs-attr">tooltip</span>: &#123;
        <span class="hljs-attr">trigger</span>: <span class="hljs-string">'axis'</span>,
        <span class="hljs-attr">axisPointer</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'cross'</span>,
            <span class="hljs-attr">crossStyle</span>: &#123;
                <span class="hljs-attr">color</span>: <span class="hljs-string">'#999'</span>
            &#125;
        &#125;
    &#125;,
    <span class="hljs-attr">legend</span>: &#123;
        <span class="hljs-attr">bottom</span>: <span class="hljs-number">20</span>,
        <span class="hljs-attr">right</span>:<span class="hljs-number">20</span>,
        <span class="hljs-attr">textStyle</span>:&#123;<span class="hljs-attr">color</span>:<span class="hljs-string">'#fff'</span>&#125;,
        <span class="hljs-attr">data</span>: [
            &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'已交付'</span>,<span class="hljs-attr">icon</span>: <span class="hljs-string">'circle'</span>&#125;,  
            &#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'累计百分比'</span>,<span class="hljs-attr">icon</span>:<span class="hljs-string">'circle'</span>&#125;]
    &#125;,
    <span class="hljs-attr">xAxis</span>: [
        &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'category'</span>,
            <span class="hljs-attr">axisPointer</span>: &#123;
                <span class="hljs-attr">type</span>: <span class="hljs-string">'shadow'</span>
            &#125;
        &#125;
    ],
    <span class="hljs-attr">yAxis</span>: [
        &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'value'</span>,
            <span class="hljs-attr">show</span>:<span class="hljs-literal">true</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'件'</span>,
            <span class="hljs-attr">min</span>: <span class="hljs-number">0</span>,
            <span class="hljs-attr">max</span>: <span class="hljs-number">5000</span>,
            <span class="hljs-attr">axisLine</span>:&#123;
                <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">lineStyle</span>:&#123;
                    <span class="hljs-attr">color</span>: <span class="hljs-string">'#02180b'</span>
                &#125;
            &#125;,
            <span class="hljs-attr">splitLine</span>: &#123;
                <span class="hljs-attr">lineStyle</span>: &#123;
                    <span class="hljs-attr">type</span>: <span class="hljs-string">'dashed'</span>,
                    <span class="hljs-attr">color</span>: <span class="hljs-string">'#02180b'</span>,
                &#125;
            &#125;
        &#125;,
        &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'value'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
            <span class="hljs-attr">min</span>: <span class="hljs-number">0</span>,
            <span class="hljs-attr">max</span>: <span class="hljs-number">100</span>,
            <span class="hljs-attr">axisLabel</span>: &#123;
                <span class="hljs-attr">formatter</span>: <span class="hljs-string">'&#123;value&#125;.00 %'</span>
            &#125;,
            <span class="hljs-attr">axisLine</span>:&#123;
                <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">lineStyle</span>:&#123;
                    <span class="hljs-attr">color</span>: <span class="hljs-string">'#02180b'</span>
                &#125;
            &#125;,
            <span class="hljs-attr">splitLine</span>: &#123;
                <span class="hljs-attr">lineStyle</span>: &#123;
                    <span class="hljs-attr">type</span>: <span class="hljs-string">'dashed'</span>,
                    <span class="hljs-attr">color</span>: <span class="hljs-string">'#02180b'</span>,
                &#125;
            &#125;
        &#125;
    ],
    <span class="hljs-attr">series</span>: [
        &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'已交付'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'bar'</span>,
            <span class="hljs-attr">barWidth</span>: <span class="hljs-number">20</span>,
            <span class="hljs-attr">label</span>: &#123;
                <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">position</span>: <span class="hljs-string">'top'</span>,
                <span class="hljs-attr">valueAnimation</span>: <span class="hljs-literal">true</span>,
            &#125;
        &#125;,
        &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'累计百分比'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'line'</span>,
            <span class="hljs-attr">label</span>: &#123;
                <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">distance</span>: <span class="hljs-number">5</span>,
                <span class="hljs-attr">rich</span>:&#123;
                    <span class="hljs-attr">red</span>:&#123;<span class="hljs-attr">color</span>:<span class="hljs-string">'red'</span>,<span class="hljs-attr">fontSize</span>:<span class="hljs-number">14</span>&#125;,
                    <span class="hljs-attr">b</span>: &#123;
                        <span class="hljs-attr">backgroundColor</span>: &#123;
                          <span class="hljs-attr">image</span>: <span class="hljs-string">'https://img-blog.csdnimg.cn/2021070312161116.png'</span>
                        &#125;,
                        <span class="hljs-attr">height</span>: <span class="hljs-number">30</span>,
                      &#125;,
                &#125;,
                <span class="hljs-attr">formatter</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">params</span>) </span>&#123;
                    <span class="hljs-keyword">const</span> &#123; data &#125; = params;
                    <span class="hljs-keyword">const</span> value = data[<span class="hljs-number">2</span>]
                  <span class="hljs-keyword">if</span> (value > <span class="hljs-number">50</span>) &#123;
                    <span class="hljs-keyword">return</span> <span class="hljs-string">"&#123;red|"</span> + value + <span class="hljs-string">"%&#125;&#123;b| &#125;"</span>
                  &#125;
                  <span class="hljs-keyword">return</span> value+<span class="hljs-string">"%"</span>
                &#125;
            &#125;,
            <span class="hljs-attr">yAxisIndex</span>: <span class="hljs-number">1</span>,
        &#125;
    ]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">图1-2的核心代码</h4>
<pre><code class="hljs language-js copyable" lang="js">option = &#123;
    <span class="hljs-comment">// color: ['#5470c6', '#fac858'],</span>
    <span class="hljs-attr">color</span>: [<span class="hljs-string">'#fff'</span>, <span class="hljs-string">'#fff'</span>],
    <span class="hljs-attr">legend</span>: &#123;
        <span class="hljs-attr">data</span>: [<span class="hljs-string">'已用产能'</span>, <span class="hljs-string">'剩余产能'</span>]
    &#125;,
    <span class="hljs-attr">xAxis</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'category'</span>,
        <span class="hljs-attr">data</span>: [<span class="hljs-string">"制芯"</span>,<span class="hljs-string">"组芯"</span>,<span class="hljs-string">"熔炼"</span>,<span class="hljs-string">"浇注"</span>,<span class="hljs-string">"冷却"</span>,<span class="hljs-string">"落砂"</span>,<span class="hljs-string">"切割"</span>,<span class="hljs-string">"抛丸"</span>,<span class="hljs-string">"打磨"</span>,<span class="hljs-string">"检测"</span>]
    &#125;,
    <span class="hljs-attr">yAxis</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'value'</span>,
        <span class="hljs-attr">axisLabel</span>:&#123;
          <span class="hljs-attr">formatter</span>: <span class="hljs-string">'&#123;value&#125;%'</span>
        &#125;
    &#125;,
    <span class="hljs-attr">series</span>: [
        &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'已用产能'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'bar'</span>,
            <span class="hljs-attr">stack</span>: <span class="hljs-string">'total'</span>,
            <span class="hljs-attr">label</span>: &#123;
                <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">formatter</span>:<span class="hljs-string">'&#123;c&#125;%'</span>
            &#125;,
            <span class="hljs-attr">emphasis</span>: &#123;
                <span class="hljs-attr">focus</span>: <span class="hljs-string">'series'</span>
            &#125;,
            <span class="hljs-attr">data</span>: [<span class="hljs-number">76</span>,<span class="hljs-number">54</span>,<span class="hljs-number">62</span>,<span class="hljs-number">59</span>,<span class="hljs-number">67</span>,<span class="hljs-number">81</span>,<span class="hljs-number">84</span>,<span class="hljs-number">92</span>,<span class="hljs-number">96</span>,<span class="hljs-number">83</span>],
            <span class="hljs-attr">itemStyle</span>:&#123;
                ....
            &#125;
        &#125;,
        &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'剩余产能'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'bar'</span>,
            <span class="hljs-attr">stack</span>: <span class="hljs-string">'total'</span>,
            <span class="hljs-attr">label</span>: &#123;
                <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">formatter</span>:<span class="hljs-string">'&#123;c&#125;%'</span>
            &#125;,
            <span class="hljs-attr">emphasis</span>: &#123;
                <span class="hljs-attr">focus</span>: <span class="hljs-string">'series'</span>
            &#125;,
            <span class="hljs-attr">data</span>: [<span class="hljs-number">24</span>,<span class="hljs-number">46</span>,<span class="hljs-number">38</span>,<span class="hljs-number">41</span>,<span class="hljs-number">33</span>,<span class="hljs-number">19</span>,<span class="hljs-number">16</span>,<span class="hljs-number">8</span>,<span class="hljs-number">4</span>,<span class="hljs-number">17</span>],
            <span class="hljs-attr">itemStyle</span>:&#123;
                <span class="hljs-attr">decal</span>:&#123;
                   ....
                &#125;
            &#125;
        &#125;,
    ],
    <span class="hljs-attr">aria</span>: &#123;
        <span class="hljs-attr">enabled</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">decal</span>: &#123;
            <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
        &#125;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将代码复制到 echarts的编辑器里就可以实时预览效果了。
<a href="https://echarts.apache.org/examples/zh/editor.html?c=line-simple" target="_blank" rel="nofollow noopener noreferrer">echarts.apache.org/examples/zh…</a></p>
<p>后续的我会给大家详细讲解echarts中的贴花。 这是一个非常具有表现力，并且可以玩出花的特性。
大家敬请期待。</p></div>  
</div>
            