
---
title: '运用logaX "优雅" 展现可视化图表极端数据🎨'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c707f676cd104cf3be54df7e11675e91~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 20:28:38 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c707f676cd104cf3be54df7e11675e91~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第13天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<p>可视化开发是前端开发的重要分支之一。日常的数据需求需要我们去熟练使用<code>Echarts</code>、<code>Antv</code>、<code>Highcharts</code>等开源可视化库。可能还有些定制化的需求，这就需要去深入了解<code>svg</code>、<code>canvas</code>更底层的东西。操作<code>svg</code>的有<code>D3</code>，<code>canvas</code>则有<code>Zrender</code>等。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c707f676cd104cf3be54df7e11675e91~tplv-k3u1fbpfcp-watermark.image" alt="src=http___img.mp.itc.cn_q_70,c_zoom,w_640_upload_20170629_925694caa5bb411ca71b5702c4739648.jpg&refer=http___img.mp.itc.jfif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文以<code>Echarts</code>为例，讲解如何运用基本初等函数中的<code>对数函数</code>去解决<code>极端</code>数据的业务场景。如果听懂了，其他图表库相信也能触类旁通地解决。</p>
<h2 data-id="heading-1">对数函数🎈</h2>
<p>对数函数是<code>6</code>种基本初等函数之一。如果<code>a^x=N（a>0，且a≠1）</code>，那么数<code>x</code>叫做以<code>a</code>为底<code>N</code>的对数，记作<code>x=logaN</code>，其中<code>a</code>叫做对数的底数，<code>N</code>叫做真数。</p>
<p>一般，函数<code>y=logax（a>0，且a≠1）</code>叫做对数函数。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b6b9f090f4e45baabb5fc128c766ef0~tplv-k3u1fbpfcp-watermark.image" alt="下载.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由图可看出，随着<code>x</code>增长，对数函数的增长趋势越来越平缓，本文的解决核心思想也就是利用对数函数增长缓慢的特性。</p>
<p>进入正题 ~</p>
<h2 data-id="heading-2">业务场景</h2>
<p>模拟下业务场景。<br>
<strong>产品经理</strong>：js
需要用折线图表展示这份数据。<br>
<strong>后端</strong>：返回的真实数据类似<code>[212, 0, 0.001, 9, 1, 133, 13200]</code></p>
<p>可以看出目前数据差异较大，拿<code>Echarts</code>配置如下所示。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9500283dba874984ba6e4c73b2d766a9~tplv-k3u1fbpfcp-watermark.image" alt="echarts (2).png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> option = &#123;
    <span class="hljs-attr">xAxis</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'category'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'x'</span>,
      <span class="hljs-attr">data</span>: [<span class="hljs-string">'Mon'</span>, <span class="hljs-string">'Tue'</span>, <span class="hljs-string">'Wed'</span>, <span class="hljs-string">'Thu'</span>, <span class="hljs-string">'Fri'</span>, <span class="hljs-string">'Sat'</span>, <span class="hljs-string">'Sun'</span>]
    &#125;,
    <span class="hljs-attr">toolbox</span>: &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">feature</span>: &#123;
        <span class="hljs-attr">saveAsImage</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'png'</span>
        &#125;
      &#125;
    &#125;,
    <span class="hljs-attr">tooltip</span>: &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">trigger</span>: <span class="hljs-string">'axis'</span>
    &#125;,
    <span class="hljs-attr">yAxis</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'value'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'y'</span>,
      <span class="hljs-attr">minorSplitLine</span>: &#123;
        <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;,
    <span class="hljs-attr">series</span>: [&#123;
      <span class="hljs-attr">data</span>: [<span class="hljs-number">212</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0.001</span>, <span class="hljs-number">9</span>, <span class="hljs-number">1</span>, <span class="hljs-number">133</span>, <span class="hljs-number">13200</span>],
      <span class="hljs-attr">type</span>: <span class="hljs-string">'line'</span>,
      <span class="hljs-attr">smooth</span>: <span class="hljs-literal">true</span>
    &#125;]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>产品经理</strong>：数据差异太大，这图感觉不太行，能不能优化下？<br>
<strong>前端</strong>：这... 真实数据是这样，能有什么办法？（推锅）给我点时间，我先想想吧。</p>
<p>翻阅Echarts文档，发现轴的<code>type</code>属性有<code>log</code>的概念，立马替换，结果如下，跟想像中的不太一样，好像报错了。😅
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/232b5805f770439091af7b8f9dad9d10~tplv-k3u1fbpfcp-watermark.image" alt="echarts (2).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>仔细排查 + 搜索引擎，发现是因为<code>0</code>的原因，毕竟对数<code>x</code>的定义域是大于0的。所以这里可以改成<code>null</code>。图是不是就好看很多了，兴奋地叫产品经理过来看效果。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2078055bb1c41a08d32d71f6394cf29~tplv-k3u1fbpfcp-watermark.image" alt="echarts (2).png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> option = &#123;
    <span class="hljs-attr">xAxis</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'category'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'x'</span>,
        <span class="hljs-attr">data</span>: [<span class="hljs-string">'Mon'</span>, <span class="hljs-string">'Tue'</span>, <span class="hljs-string">'Wed'</span>, <span class="hljs-string">'Thu'</span>, <span class="hljs-string">'Fri'</span>, <span class="hljs-string">'Sat'</span>, <span class="hljs-string">'Sun'</span>]
    &#125;,
    <span class="hljs-attr">toolbox</span>: &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">feature</span>: &#123;
        <span class="hljs-attr">saveAsImage</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'png'</span>
        &#125;
      &#125;
    &#125;,
    <span class="hljs-attr">tooltip</span>: &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">trigger</span>: <span class="hljs-string">'axis'</span>
    &#125;,
    <span class="hljs-attr">yAxis</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'log'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'y'</span>,
        <span class="hljs-attr">minorSplitLine</span>: &#123;
            <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>
        &#125;
    &#125;,
    <span class="hljs-attr">series</span>: [&#123;
        <span class="hljs-attr">data</span>: [<span class="hljs-number">212</span>, <span class="hljs-literal">null</span>, <span class="hljs-number">0.001</span>, <span class="hljs-number">9</span>, <span class="hljs-number">1</span>, <span class="hljs-number">133</span>, <span class="hljs-number">13200</span>],
        <span class="hljs-attr">type</span>: <span class="hljs-string">'line'</span>,
        <span class="hljs-attr">smooth</span>: <span class="hljs-literal">true</span>
    &#125;]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>产品经理</strong>：嗯嗯，好看多了，但怎么中间断开了？<br>
<strong>前端</strong>：因为数据是0，没有了啊。<br>
<strong>产品经理</strong>：需求是满足了，好想线是连一起的（得寸进尺💢）<br>
<strong>前端</strong>：...</p>
<p>虽然嘴上拒绝，但还是得快速地去想方案，毕竟得<code>优雅</code>处理。<code>Echarts</code>没有提供相关解决方案，重新换个库，再研究，有点浪费时间了。自己用<code>canvas</code>画，更不可能了。那怎么去延伸<code>对数</code>的思想呢？</p>
<p>在翻阅对数概念时，突然看到一句话:<code>指数函数是对数函数的反函数</code>，灵光乍现✨。</p>
<ol>
<li>先将原始数据用对数函数转换一下。</li>
<li>显示的时候再用指数函数转换回来。</li>
</ol>
<p>这里处理原数据的时候需要<code>+1</code>处理，显示的时候<code>-1</code>即可。因为对数在<code>(0,1)</code>范围内是负数，趋于<code>0</code>的时候又接近于负无穷。图表数据本身是正数的情况下，映射成负数，更容易误导。</p>
<p>改造成功，如下图所示，线也连一起了，骄傲地把产品经理叫过来。<br>
<strong>产品经理</strong>：👏。<br>
<strong>前端</strong>：小事小事~。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1165ccbd247545c88139f91c0fc66b5c~tplv-k3u1fbpfcp-watermark.image" alt="echarts (2).png" loading="lazy" referrerpolicy="no-referrer">
代码思路如下：</p>
<ol>
<li>转换数据用<code>Math.log10(d + 1)</code>即可。</li>
<li>显示数据的时候用<code>Math.pow(10, d) - 1</code>。图表方面利用<code>Echarts</code>提供的<code>formatter</code>格式化显示<code>y轴</code>和<code>tooltip</code>。</li>
</ol>
<p>具体代码如下，即插即用，拿去直接用！！！</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 转换原始数据</span>
<span class="hljs-keyword">let</span> transformToLog = <span class="hljs-function">(<span class="hljs-params">d</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.log10(d + <span class="hljs-number">1</span>)
&#125;
<span class="hljs-comment">// 对数转原始数据</span>
<span class="hljs-keyword">let</span> transformToOrigin = <span class="hljs-function">(<span class="hljs-params">d</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">10</span>, d) - <span class="hljs-number">1</span>
&#125;
<span class="hljs-keyword">let</span> orginData = [<span class="hljs-number">212</span>, <span class="hljs-literal">null</span>, <span class="hljs-number">0.001</span>, <span class="hljs-number">9</span>, <span class="hljs-number">1</span>, <span class="hljs-number">133</span>, <span class="hljs-number">13200</span>]

<span class="hljs-keyword">let</span> option = &#123;
    <span class="hljs-attr">xAxis</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'category'</span>,
      <span class="hljs-attr">data</span>: [<span class="hljs-string">'Mon'</span>, <span class="hljs-string">'Tue'</span>, <span class="hljs-string">'Wed'</span>, <span class="hljs-string">'Thu'</span>, <span class="hljs-string">'Fri'</span>, <span class="hljs-string">'Sat'</span>, <span class="hljs-string">'Sun'</span>]
    &#125;,
    <span class="hljs-attr">toolbox</span>: &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">feature</span>: &#123;
        <span class="hljs-attr">saveAsImage</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'png'</span>
        &#125;
      &#125;
    &#125;,
    <span class="hljs-attr">tooltip</span>: &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">trigger</span>: <span class="hljs-string">'axis'</span>,
      <span class="hljs-attr">formatter</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">params</span>) </span>&#123;
          <span class="hljs-keyword">return</span> params[<span class="hljs-number">0</span>].axisValue + <span class="hljs-string">'：'</span> + <span class="hljs-built_in">Number</span>(transformToOrigin(params[<span class="hljs-number">0</span>].value).toFixed(<span class="hljs-number">3</span>))
      &#125;
    &#125;,
    <span class="hljs-attr">yAxis</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'value'</span>,
      <span class="hljs-attr">axisLabel</span>: &#123;
        <span class="hljs-attr">formatter</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value, index</span>) </span>&#123;
            <span class="hljs-keyword">if</span>(value > <span class="hljs-number">0</span>) &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">10</span>, value)&#125;
            <span class="hljs-keyword">return</span> value
        &#125;  
      &#125;,
      <span class="hljs-attr">minorSplitLine</span>: &#123;
        <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;,
    <span class="hljs-attr">series</span>: [&#123;
      <span class="hljs-attr">data</span>: logData,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'line'</span>,
      <span class="hljs-attr">smooth</span>: <span class="hljs-literal">true</span>
    &#125;]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>产品需求满足了，但故事还没结束，毕竟标题还有<code>极端</code>两个字。</p>
<p>这算是自己的疑问吧，如果数据有<code>负数</code>怎么办，那这又不可行了？毕竟对数定义域是大于<code>0</code>。<br>
那怎么办？既然是负数，我们是不是可以想到<code>取绝对值</code>。</p>
<ol>
<li>若是负数，先取绝对值，再用对数，最后乘以<code>-1</code>。</li>
<li>显示的时候，再反向操作即可。</li>
</ol>
<p>首先原数据改为：<code>[212, null, 0.001, 9, 1, -133, 13200]</code>。先看结果图，<code>优雅</code>么？</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2f1895312d649089f55455aa3d719a5~tplv-k3u1fbpfcp-watermark.image" alt="echarts (2).png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 转换原始数据</span>
<span class="hljs-keyword">let</span> transformToLog = <span class="hljs-function">(<span class="hljs-params">d</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> operator = <span class="hljs-number">1</span>
    d < <span class="hljs-number">0</span> && (operator = -<span class="hljs-number">1</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.log10(<span class="hljs-built_in">Math</span>.abs(d) + <span class="hljs-number">1</span>) * operator
&#125;
<span class="hljs-comment">// 对数转原始数据</span>
<span class="hljs-keyword">let</span> transformToOrigin = <span class="hljs-function">(<span class="hljs-params">d</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> operator = <span class="hljs-number">1</span>
    d < <span class="hljs-number">0</span> && (operator = -<span class="hljs-number">1</span>)
    <span class="hljs-keyword">return</span> (<span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">10</span>, d * operator)) * operator - <span class="hljs-number">1</span> * operator
&#125;
<span class="hljs-keyword">let</span> orginData = [<span class="hljs-number">212</span>, <span class="hljs-literal">null</span>, <span class="hljs-number">0.001</span>, <span class="hljs-number">9</span>, <span class="hljs-number">1</span>, -<span class="hljs-number">133</span>, <span class="hljs-number">13200</span>]
<span class="hljs-keyword">let</span> logData = orginData.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> transformToLog(item))

<span class="hljs-keyword">let</span> option = &#123;
    <span class="hljs-attr">xAxis</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'category'</span>,
      <span class="hljs-attr">data</span>: [<span class="hljs-string">'Mon'</span>, <span class="hljs-string">'Tue'</span>, <span class="hljs-string">'Wed'</span>, <span class="hljs-string">'Thu'</span>, <span class="hljs-string">'Fri'</span>, <span class="hljs-string">'Sat'</span>, <span class="hljs-string">'Sun'</span>]
    &#125;,
    <span class="hljs-attr">toolbox</span>: &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">feature</span>: &#123;
        <span class="hljs-attr">saveAsImage</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'png'</span>
        &#125;
      &#125;
    &#125;,
    <span class="hljs-attr">tooltip</span>: &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">trigger</span>: <span class="hljs-string">'axis'</span>,
      <span class="hljs-attr">formatter</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">params</span>) </span>&#123;
          <span class="hljs-keyword">return</span> params[<span class="hljs-number">0</span>].axisValue + <span class="hljs-string">'：'</span> + <span class="hljs-built_in">Number</span>(transformToOrigin(params[<span class="hljs-number">0</span>].value).toFixed(<span class="hljs-number">3</span>))
      &#125;
    &#125;,
    <span class="hljs-attr">yAxis</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'value'</span>,
      <span class="hljs-attr">axisLabel</span>: &#123;
        <span class="hljs-attr">formatter</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value, index</span>) </span>&#123;
            <span class="hljs-keyword">let</span> operator = <span class="hljs-number">1</span>
            <span class="hljs-keyword">if</span>(value < <span class="hljs-number">0</span>) operator = -<span class="hljs-number">1</span>
            <span class="hljs-keyword">if</span>(value === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">10</span>, value * operator) * operator 
            
        &#125;  
      &#125;,
      <span class="hljs-attr">minorSplitLine</span>: &#123;
        <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;,
    <span class="hljs-attr">series</span>: [&#123;
      <span class="hljs-attr">data</span>: logData,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'line'</span>,
      <span class="hljs-attr">smooth</span>: <span class="hljs-literal">true</span>
    &#125;]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">总结</h2>
<p>💗 感谢8月掘金活动，让自己能坚持一个月，用文字记录基础知识点和一些小心得，也幸运地获取了一些点赞和关注，从<code>lv1</code>到<code>lv2</code>，切实感受写文章的快乐。</p>
<p>先前文章大多是<code>JS</code>基础，接下来，我会分享的更全面一点，比如<code>CSS</code>、<code>node</code>、<code>可视化</code>、<code>浏览器</code>等，也会继续分享自己的小心得（结合真实业务场景，绝对干货），比如这一篇，看大家兴趣（其实看点赞量了，哈哈哈哈）。</p>
<p>如果本篇文章帮到你了，记得毫不吝啬地三连<code>点赞</code>+<code>关注</code>+<code>收藏</code>啊！！！</p>
<p>当然，也欢迎各路大佬<code>评论</code>交流学习，批评指正。</p></div>  
</div>
            