
---
title: 'BziChart子弹图BulletChart业务组件封装'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d5954c5f48e4c09abb9c0d65d78274f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 04:33:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d5954c5f48e4c09abb9c0d65d78274f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">需求背景：</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d5954c5f48e4c09abb9c0d65d78274f~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">图表库选型</h1>
<p>老的项目中使用G2配置实现，配置零散，后期不好维护，在新的需求中，考虑重构</p>
<p>于是，调研了一波图表库，目前主流的图表库有echarts、highcharts、D3js、antv(G2, G6, F2)基于D3封装的react图表库rechart； 还有基于G2封装的react图表库viser、Bizcharts等等。还有关系图展示使用的Cytoscapejs；时序图常用工具库visjs等等 那么如何选择呢？</p>
<p>由于项目是react框架，所以考虑用react封装的图表库，大概去看了一遍BizCharts图表库，文档什么的感觉还是很完善的，并且GitHub上也一直在维护。素以决定了BizCharts，该图表库新的版本是V4.X</p>
<p><a href="https://bizcharts.net/product/BizCharts4/category/77/page/142#demo" target="_blank" rel="nofollow noopener noreferrer">bizcharts.net/product/Biz…</a></p>
<h1 data-id="heading-2">问题</h1>
<p>开始根据需求进行相关组件demo实现，柱状图、折线图、直方图、环状图都相对比较简单，根据文档基本都能实现，但是在实现子弹图的时候，文档上的demo都是有问题的；怎么办呢？</p>
<p>第一想到了去GitHub上找源代码去看，文档上的配置属性很多都已经废弃</p>
<p><a href="https://github.com/alibaba/BizCharts/blob/25de7baa650904507a53e9fdd50e9c6374ea1c06/src/plots/BulletChart.tsx" target="_blank" rel="nofollow noopener noreferrer">github.com/alibaba/Biz…</a></p>
<p>后来去antv上找到了子弹图
<a href="https://g2plot.antv.vision/zh/docs/api/plots/bullet#xfield%EF%BC%8C%E8%BF%99%E9%87%8C%E6%89%8D%E6%98%AF%E6%9C%80%E6%96%B0%E7%9A%84%E6%96%87%E6%A1%A3%EF%BC%8C%E7%84%B6%E5%90%8E%E6%A0%B9%E6%8D%AE%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E4%B8%80%E7%82%B9%E7%82%B9%E5%AE%9E%E7%8E%B0%EF%BC%8C%E6%95%88%E6%9E%9C%E5%9B%BE%E5%A6%82%E4%B8%8B%EF%BC%9A" target="_blank" rel="nofollow noopener noreferrer">g2plot.antv.vision/zh/docs/api…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0f20c3e1e254634af89fdbbdd0e75b6~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>献上经过近一天的探索，实现的demo代码</p>
<pre><code class="copyable">import React from 'react';
import ReactDOM from 'react-dom';
import &#123; BulletChart &#125; from 'bizcharts';

// 数据源
const mockData = [
  &#123;
    title: "满意度",
    measures: [83],
    target: [80],
    ranges: [0, 10, 40, 75, 100],
  &#125;,
];

function Demo() &#123;
  return (
    <BulletChart
      data=&#123;mockData&#125;
      xField="title"
      yField="ranges"
      height=&#123;90&#125;
      measureField="measures"
      rangeField="ranges"
      targetField="target"
      size=&#123;&#123;
        measure: 10,
        range: 28,
        target: 25,
      &#125;&#125;
      color=&#123;&#123;
        measure: ["#43467c"],
        target: ["#000000"],
        range: ["#b4ebbf", "#ffb1ac", "#ffdba1", "#abc9f0"],
      &#125;&#125;
      bulletStyle=&#123;&#123;
        target: &#123;
          width: 15,
          fill: "#000000",
        &#125;,
      &#125;&#125;
      yAxis=&#123;&#123;
        tickCount: 11,
        top: true,
      &#125;&#125;
      legend=&#123;&#123;
custom: "true",
position: "top",
offsetX: 8,
items: [
   &#123;
name: "班平均分",
marker: &#123;
symbol: "circle",
style: &#123;
fill: "#43467c",
&#125;,
&#125;,
&#125;,
&#123;
name: "校平均",
marker: &#123;
symbol: "line",
style: &#123;
stroke: "#000000",
&#125;,
&#125;,
&#125;,
&#123;
name: "不及格",
marker: &#123;
symbol: "circle",
style: &#123;
fill: "#ffb1ac",
&#125;,
&#125;,
&#125;,
&#123;
name: "及格",
marker: &#123;
symbol: "circle",
style: &#123;
fill: "#ffdba1",
&#125;,
&#125;,
&#125;,
&#123;
name: "良好",
marker: &#123;
symbol: "circle",
style: &#123;
fill: "#abc9f0",
&#125;,
&#125;,
&#125;,
&#123;
name: "优秀",
marker: &#123;
symbol: "circle",
style: &#123;
fill: "#b4ebbf",
&#125;,
&#125;,
&#125;,
],
&#125;&#125;
    />
  );
&#125;

ReactDOM.render(<Demo />, mountNode);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            