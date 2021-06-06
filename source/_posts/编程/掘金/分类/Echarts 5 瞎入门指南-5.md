
---
title: 'Echarts 5 瞎入门指南-5'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fb46a0a40c44b64b769436c4bbe89ac~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 18:19:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fb46a0a40c44b64b769436c4bbe89ac~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本章主题提示框（Tooltip）是一种最常用的可视化组件，可以帮助用户交互式地了解数据的详细信息。 郭宝坤惯例： 上来先看个demo</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"chart"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> echarts <span class="hljs-keyword">from</span> <span class="hljs-string">'echarts'</span>
    <span class="hljs-keyword">let</span> myChart = <span class="hljs-literal">null</span>,
    
    tooltip = &#123;
        <span class="hljs-comment">//刚开始什么都不写</span>
    &#125;,
    
    xAxis= &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'category'</span>,
        <span class="hljs-attr">data</span>: [<span class="hljs-string">'司理理'</span>, <span class="hljs-string">'林婉儿'</span>]
    &#125;,
    
    series = [
        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'魅力值'</span>,  <span class="hljs-attr">type</span>: <span class="hljs-string">'bar'</span>, <span class="hljs-attr">data</span>: [<span class="hljs-number">99</span>, <span class="hljs-number">95</span>] &#125;,
        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'武力值'</span>, <span class="hljs-attr">type</span>: <span class="hljs-string">'bar'</span>, <span class="hljs-attr">data</span>: [<span class="hljs-number">70</span>, <span class="hljs-number">20</span>] &#125;
    ];
    
    <span class="hljs-keyword">const</span> options = &#123;     
        tooltip,
        xAxis,
        <span class="hljs-attr">yAxis</span>: &#123;&#125;,
        series
    &#125;;
    
    ~<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params"></span>) </span>&#123;
        myChart = echarts.init(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'chart'</span>)); <span class="hljs-comment">//实际情况这里需要等dom加载完了</span>
        myChart.setOption(options)  
    &#125;() 
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fb46a0a40c44b64b769436c4bbe89ac~tplv-k3u1fbpfcp-watermark.image" alt="demo1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以明显的看出司理理姑娘比较优秀...  <img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9de4bd18752348d69f804ce94fff5305~tplv-k3u1fbpfcp-watermark.image" alt="hj1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">触发方式 ( item / axis / none )</h3>
<p>上面tooltip 只展示了其中一项（魅力值）， 因为tooltip 默认触发方式是 'item'    其实它有三种值可选，让我们看下其它两种</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// item: 数据项图形触发，主要在散点图，饼图等无类目轴的图表中使用。</span>
<span class="hljs-comment">// axis: 坐标轴触发，主要在柱状图，折线图等会使用 '类目轴' 的图表中使用。</span>
<span class="hljs-comment">// none: 什么都不触发， 这个跟show: false 有什么区别 ？？ （知道的小伙伴留个言）</span>
tooltip = &#123;
    <span class="hljs-attr">trigger</span>: <span class="hljs-string">'axis'</span>, 
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到 axis 显示了司理理的 "所有" 特性值</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf3f4d1e39b648599a72b5d086842a43~tplv-k3u1fbpfcp-watermark.image" alt="axis.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里解释下类目轴与非类目轴：<code>类目轴就是横坐标标签类型为类目（type: 'category'）的坐标轴 非类目轴 常见有 时间（time），数值（value），对数（log）3种</code>
比如上面我们 x轴 的 司理理 和 林婉儿 就是类目轴  那些比如2018~2021 就是非类目轴</p>
<h3 data-id="heading-1">优化样式</h3>
<p>接下来我们看下如何修改tootip 外观样式</p>
<pre><code class="hljs language-js copyable" lang="js">tooltip = &#123;
    ...
    <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">'rgba(50,50,50,0.7)'</span>,  <span class="hljs-comment">//背景色</span>
    <span class="hljs-attr">textStyle</span>: &#123;
        <span class="hljs-attr">color</span>: <span class="hljs-string">'#fff'</span>, <span class="hljs-comment">//文字颜色</span>
        <span class="hljs-attr">align</span>:<span class="hljs-string">'left'</span>, <span class="hljs-comment">//左对齐</span>
        <span class="hljs-comment">//overflow: 'truncate'  超出时显示...  （需要设置width）</span>
    &#125;
&#125;    

<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5606ac8d0ae47d4bc7baab9b951de77~tplv-k3u1fbpfcp-watermark.image" alt="yh.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">排序</h3>
<pre><code class="hljs language-js copyable" lang="js">tooltip = &#123;
    ...
    <span class="hljs-attr">order</span>: <span class="hljs-string">'valueAsc'</span>  <span class="hljs-comment">//根据数据值, 升序排列。</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1175740c06044e6a0f8cd4a29e459d3~tplv-k3u1fbpfcp-watermark.image" alt="px.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到比较小的武力值排在了上面， 默认是根据系列顺序排的</p>
<h3 data-id="heading-3">extraCssText</h3>
<p>官方翻译为：额外附加到浮层的 css 样式。 这个不起眼的属性可以设置很多东西！！</p>
<pre><code class="hljs language-js copyable" lang="js">tooltip = &#123;
     ...
     <span class="hljs-attr">extraCssText</span>: <span class="hljs-string">'width: 130px; height: 150px;'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0be7201b632347dc804860f960c87bb7~tplv-k3u1fbpfcp-watermark.image" alt="xss.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">formatter</h3>
<p>有时候可能会需要对后面数值加个特殊符号， 比如冒号、括号、连接线之类的，这时候需要用到formatter</p>
<pre><code class="hljs language-js copyable" lang="js">tooltip = &#123;
    ...
    <span class="hljs-attr">formatter</span>: <span class="hljs-string">'&#123;a0&#125; (&#123;c0&#125;)<br />&#123;a1&#125;: &#123;c1&#125;'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/198f42a9620948f690a8f8c6bec324c2~tplv-k3u1fbpfcp-watermark.image" alt="format.png" loading="lazy" referrerpolicy="no-referrer"> <br></p>
<p>上面的a0 c0... 叫做模板变量，echarts提供的模板变量有 &#123;a&#125;, &#123;b&#125;，&#123;c&#125;，&#123;d&#125;  <br>
不同图表类型下的 &#123;a&#125;，&#123;b&#125;，&#123;c&#125;，&#123;d&#125; 含义可能不一样， 大概意思如下</p>
<ul>
<li>a: 系列名称</li>
<li>b: 数据名称</li>
<li>c: 数值</li>
<li>d: 百分比 （饼图经常用到）</li>
</ul>
<p>而上面的a0 c0 代表的是下标0， 它与series的下标相对应， 如写成a1在前 a0在后， 那么tootip显示就是武力值在上， 魅力值在下， 这个根据需要可以用来排序</p>
<h3 data-id="heading-5">最后的轻语</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-string">`  <<<<<<<<<    飞上枝头的都风趣， 占了巢的都在窃喜    >>>>>>>>>   `</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            