
---
title: 'Echarts Bar横向柱状图'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1edc686b9374ed79f5115abe87aac5e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 23:55:24 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1edc686b9374ed79f5115abe87aac5e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>接上一篇<a href="https://juejin.cn/post/6999630442362044447" target="_blank" title="https://juejin.cn/post/6999630442362044447"># Echart Bar柱状图样式详解</a>续写，可以先看看上一篇，不看的话，影响也不是特别大。</p>
<h2 data-id="heading-0">横向柱状图</h2>
<h3 data-id="heading-1">动态更新数据和样式</h3>
<p>实现数据<code>按月统计</code>和<code>按日统计</code>的动态切换。按月统计时，每个月数据都会展示，x 轴显示 12 个标签；按日统计时，x 轴不完全显示所有标签，间隔显示，而且<code>柱状体的宽度</code>也会变化。主要是采用的是<code>setOption</code>方法。</p>
<p>官方文档[setOption]：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fecharts.apache.org%2Fzh%2Fapi.html%23echartsInstance.setOption" target="_blank" rel="nofollow noopener noreferrer" title="https://echarts.apache.org/zh/api.html#echartsInstance.setOption" ref="nofollow noopener noreferrer">echarts.apache.org/zh/api.html…</a></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> R <span class="hljs-keyword">from</span> <span class="hljs-string">"ramda"</span>;

  <span class="hljs-keyword">const</span> source1 = [
    [<span class="hljs-string">"1月"</span>, <span class="hljs-number">1330</span>, <span class="hljs-number">666</span>, <span class="hljs-number">560</span>],
    [<span class="hljs-string">"2月"</span>, <span class="hljs-number">820</span>, <span class="hljs-number">760</span>, <span class="hljs-number">660</span>],
    ......
    [<span class="hljs-string">"11月"</span>, <span class="hljs-number">901</span>, <span class="hljs-number">880</span>, <span class="hljs-number">360</span>],
    [<span class="hljs-string">"12月"</span>, <span class="hljs-number">934</span>, <span class="hljs-number">600</span>, <span class="hljs-number">700</span>],
  ];
  <span class="hljs-keyword">const</span> source2 = [
    [<span class="hljs-string">"1日"</span>, <span class="hljs-number">1330</span>, <span class="hljs-number">666</span>, <span class="hljs-number">560</span>],
    [<span class="hljs-string">"2日"</span>, <span class="hljs-number">820</span>, <span class="hljs-number">760</span>, <span class="hljs-number">660</span>],
    ......
    [<span class="hljs-string">"29日"</span>, <span class="hljs-number">934</span>, <span class="hljs-number">600</span>, <span class="hljs-number">700</span>],
    [<span class="hljs-string">"30日"</span>, <span class="hljs-number">1330</span>, <span class="hljs-number">666</span>, <span class="hljs-number">560</span>],
  ];

  <span class="hljs-comment">// 具体配置如之前所示，详细省略，只做基本示例展示</span>
  <span class="hljs-keyword">const</span> initOption = &#123;
    ...
    <span class="hljs-attr">dataset</span>: &#123; <span class="hljs-attr">source</span>: source1 &#125;,
  &#125;;

  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">charts</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">isDaily</span>: <span class="hljs-literal">false</span>,
      &#125;;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.charts = <span class="hljs-built_in">this</span>.$echarts.init(
        <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"barCharts"</span>),
        <span class="hljs-literal">null</span>,
        &#123;
          <span class="hljs-attr">renderer</span>: <span class="hljs-string">"svg"</span>,
        &#125;
      );
      <span class="hljs-built_in">this</span>.charts.setOption(R.clone(initOption));
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">handleSource</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.isDaily = !<span class="hljs-built_in">this</span>.isDaily;
        <span class="hljs-built_in">this</span>.charts.setOption(
          R.mergeDeepRight(initOption, &#123;
            <span class="hljs-comment">// 动态更新数据源</span>
            <span class="hljs-attr">dataset</span>: &#123;
              <span class="hljs-attr">source</span>: <span class="hljs-built_in">this</span>.isDaily ? source2 : source1,
            &#125;,
            <span class="hljs-attr">xAxis</span>: &#123;
              <span class="hljs-comment">// 动态更新标签间隔</span>
              <span class="hljs-attr">axisLabel</span>: &#123;
                <span class="hljs-attr">interval</span>: <span class="hljs-built_in">this</span>.isDaily ? <span class="hljs-number">4</span> : <span class="hljs-string">"auto"</span>,
              &#125;,
            &#125;,
            <span class="hljs-attr">series</span>: R.map(
              <span class="hljs-comment">// 动态更新柱体宽度</span>
              <span class="hljs-function">(<span class="hljs-params">o</span>) =></span> ((o.barWidth = <span class="hljs-built_in">this</span>.isDaily ? <span class="hljs-number">12</span> : <span class="hljs-number">24</span>), o),
              initOption.series
            ),
          &#125;),
          <span class="hljs-literal">true</span>
        );
        <span class="hljs-built_in">this</span>.charts.resize();
      &#125;,
    &#125;,
  &#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1edc686b9374ed79f5115abe87aac5e~tplv-k3u1fbpfcp-watermark.image" alt="ic_bar_8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">解决 echarts 宽高自适应问题</h3>
<p>在 web 项目中做图表时，图表的宽高不是固定的，需要随着浏览器<code>宽度高度自适应</code>，使用的方法就是<code>resize</code>。如果有多个图表，需要同时进行<code>resize</code>处理。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"resize"</span>, <span class="hljs-built_in">this</span>.handleResize, <span class="hljs-literal">false</span>);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">"resize"</span>, <span class="hljs-built_in">this</span>.handleResize);
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">handleResize</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> _this = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">const</span> timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          _this.lineCharts.resize();
          _this.barCharts.resize();
        &#125;, <span class="hljs-number">500</span>);
        <span class="hljs-comment">// 清除定时器</span>
        <span class="hljs-built_in">this</span>.$once(<span class="hljs-string">"hook:beforeDestroy"</span>, <span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(timer);
        &#125;);
      &#125;,
    &#125;,
  &#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">纵向柱状图</h2>
<h3 data-id="heading-4">纵向柱状图实现</h3>
<p>本质和横向是一样的，就是将 x，y 轴值更换一下；x 轴为<code>value</code>，y 轴为<code>category</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> option = &#123;
  <span class="hljs-attr">xAxis</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"value"</span>,
  &#125;,
  <span class="hljs-attr">yAxis</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"category"</span>,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">坐标指示器背景渐变色</h3>
<p>其实原理和横向的一样，就是渐变色处理的地方 <code>x</code>，<code>y</code> 值更换一下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> horizontalColor = &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">"linear"</span>,
  <span class="hljs-attr">x</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 更换</span>
  <span class="hljs-attr">y</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">x2</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">y2</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 更换</span>
  <span class="hljs-attr">colorStops</span>: [
    &#123; <span class="hljs-attr">offset</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"rgba(234,244,255,1)"</span> &#125;,
    &#123; <span class="hljs-attr">offset</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">color</span>: <span class="hljs-string">"rgba(234,244,255,0.3)"</span> &#125;,
  ],
  <span class="hljs-attr">global</span>: <span class="hljs-literal">false</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">柱体设置不同颜色</h3>
<p>柱体的属性设置<code>series</code>中<code>color</code>可以是一个函数，在函数中处理。核心代码为<code>colorList[params.dataIndex]</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> colorList = [
  <span class="hljs-string">"#1890ff"</span>,
  <span class="hljs-string">"#52c41a"</span>,
  <span class="hljs-string">"#faad14"</span>,
  <span class="hljs-string">"#f5222d"</span>,
  <span class="hljs-string">"#1DA57A"</span>,
  <span class="hljs-string">"#d9d9d9"</span>,
];
<span class="hljs-keyword">let</span> series = [
  &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"bar"</span>,
    <span class="hljs-attr">barWidth</span>: <span class="hljs-number">16</span>,
    <span class="hljs-attr">itemStyle</span>: &#123;
      <span class="hljs-comment">// 定制显示（按顺序）,实现不同颜色的柱体</span>
      <span class="hljs-attr">color</span>: <span class="hljs-function">(<span class="hljs-params">params</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> colorList[params.dataIndex];
      &#125;,
    &#125;,
    <span class="hljs-attr">dimensions</span>: [<span class="hljs-string">"类型"</span>, <span class="hljs-string">"销售数量"</span>],
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">柱状图上方显示数值</h3>
<p>柱体的属性设置<code>series</code>中<code>label</code>可以是一个函数，在函数中处理。可以设置位置，字体颜色和大小等。核心代码为<code>params.value[params.encode.x[0]]</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> series = [
  &#123;
    <span class="hljs-comment">// ......</span>
    <span class="hljs-attr">type</span>: <span class="hljs-string">"bar"</span>,
    <span class="hljs-attr">label</span>: &#123;
      <span class="hljs-comment">// 柱图头部显示值</span>
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">position</span>: <span class="hljs-string">"right"</span>,
      <span class="hljs-attr">color</span>: <span class="hljs-string">"#333"</span>,
      <span class="hljs-attr">fontSize</span>: <span class="hljs-string">"12px"</span>,
      <span class="hljs-attr">formatter</span>: <span class="hljs-function">(<span class="hljs-params">params</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> params.value[params.encode.x[<span class="hljs-number">0</span>]];
      &#125;,
    &#125;,
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">tooltip 提示框自定义</h3>
<p>和横向的一样，就是要注意取值<code>params[0].axisValue</code>, <code>item.seriesName</code>, <code>item.value[item.encode.x[0]]</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> tooltip = R.merge(tooltip, &#123;
  <span class="hljs-attr">formatter</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">params</span>) </span>&#123;
    <span class="hljs-keyword">let</span> html = <span class="hljs-string">`<div style="height:auto;width:163px;">
          <div style="font-size:14px;font-weight:bold;color:#333;margin-bottom:16px;line-height:1;">
            <span class="hljs-subst">$&#123;params[<span class="hljs-number">0</span>].axisValue&#125;</span>
          </div>
          <span class="hljs-subst">$&#123;params
            .map(
              (
                item
              ) => <span class="hljs-string">`<div style="font-size:12px;color:#808080;margin-bottom:8px;display:flex;align-items:center;line-height:1;">
                <span style="display:inline-block;margin-right:8px;border-radius:6px;width:6px;height:6px;background-color:<span class="hljs-subst">$&#123;
                  item.color
                &#125;</span>;"></span>
                <span class="hljs-subst">$&#123;item.seriesName&#125;</span>
                <span style="flex:1;text-align:right;"><span class="hljs-subst">$&#123;
                  item.value[item.encode.x[<span class="hljs-number">0</span>]]
                &#125;</span></span>
              </div>`</span>
            )
            .join(<span class="hljs-string">""</span>)&#125;</span>
        </div>`</span>;
    <span class="hljs-keyword">return</span> html;
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">总体实现</h3>
<pre><code class="hljs language-js copyable" lang="js">charts.setOption(&#123;
  <span class="hljs-attr">title</span>: &#123;
    <span class="hljs-attr">text</span>: <span class="hljs-string">"销售数量分布"</span>,
  &#125;,
  <span class="hljs-attr">dataset</span>: &#123;
    <span class="hljs-attr">source</span>: [
      [<span class="hljs-string">"苹果"</span>, <span class="hljs-number">200</span>],
      [<span class="hljs-string">"桃子"</span>, <span class="hljs-number">180</span>],
      [<span class="hljs-string">"葡萄"</span>, <span class="hljs-number">340</span>],
      [<span class="hljs-string">"香蕉"</span>, <span class="hljs-number">250</span>],
      [<span class="hljs-string">"芒果"</span>, <span class="hljs-number">166</span>],
      [<span class="hljs-string">"榴莲"</span>, <span class="hljs-number">185</span>],
    ],
  &#125;,
  <span class="hljs-attr">xAxis</span>: R.merge(yAxis, &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"value"</span>,
  &#125;),
  <span class="hljs-attr">yAxis</span>: R.mergeDeepRight(xAxis, &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"category"</span>,
    <span class="hljs-attr">axisPointer</span>: &#123;
      <span class="hljs-attr">shadowStyle</span>: &#123;
        <span class="hljs-attr">color</span>: horizontalColor,
      &#125;,
    &#125;,
  &#125;),
  series,
  tooltip,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e92a2e243ca34a4cb6e756bbf0225457~tplv-k3u1fbpfcp-watermark.image" alt="ic_bar_9.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            