
---
title: '【VUE】引入使用G2图表'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4668'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 00:52:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=4668'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">关于G2图表介绍</h2>
<p>G2 是一套基于图形语法理论的可视化底层引擎，以数据驱动，提供图形语法与交互语法，具有高度的易用性和扩展性</p>
<p>使用 G2，可以无需关注图表各种繁琐的实现细节，一条语句即可使用 Canvas 或 SVG 构建出各种各样的可交互的统计图表</p>
<h2 data-id="heading-1">G2图表官网地址</h2>
<pre><code class="copyable">https://antv.gitee.io/zh
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">G2图标详细开发手册</h2>
<pre><code class="copyable">https://antv-g2.gitee.io/zh/docs/api/general/chart
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">使用</h2>
<h4 data-id="heading-4">第一步：安装G2依赖包</h4>
<pre><code class="copyable">npm instal @antv/g2
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">第二步：在绘图前需要为 G2 准备一个 DOM 容器</h4>
<pre><code class="copyable"><div id="webInfo"></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">第三步：引入</h4>
<pre><code class="copyable">import G2 from "@antv/g2";
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">第四步：在mounted中定义</h4>
<ol>
<li>可先在全局定义let chart = null;</li>
<li>const chart = new G2.Chart(&#123;&#125;)</li>
</ol>
<pre><code class="copyable">chart = new G2.Chart(&#123;       
        container: "webInfo",//指定图表容器       
        forceFit: true,//强制配合 
        width: 600, // 指定图表宽度       
        height: 306,//高度       
        padding: [20, 30, 30, 50],//内边距 
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">第五步：载入数据源</h4>
<pre><code class="copyable">/马上更新图表 / 
chart.changeData(chartData) 

/仅仅是更新数据，而不需要马上更新图表/ 
chart.source(chartData) 

/需要更新图表时调用 / 
chart.repaint()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">补充：扩展清除图形语法</h4>
<pre><code class="copyable">/清理所有/
chart.clear(); 
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            