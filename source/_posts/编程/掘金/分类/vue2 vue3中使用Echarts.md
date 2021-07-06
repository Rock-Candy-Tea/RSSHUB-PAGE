
---
title: 'vue2 vue3中使用Echarts'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47658c8999c0400d9f8652ea9a424fbb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 06:43:57 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47658c8999c0400d9f8652ea9a424fbb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">安装</h2>
<pre><code class="hljs language-js copyable" lang="js">npm install echarts --save
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">vue2中使用Echarts</h2>
<p><strong>在main.js文件中</strong></p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// 引入echarts</span>
<span class="hljs-keyword">import</span> echarts <span class="hljs-keyword">from</span> <span class="hljs-string">'echarts'</span>
Vue.prototype.$echarts = echarts 

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>给定一个容器</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"myChart"</span> :style=<span class="hljs-string">"&#123;width: '300px', height: '300px'&#125;"</span>></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>echarts初始化应在钩子函数mounted()中，这个钩子函数是在el 被新创建的 vm.$el 替换，并挂载到实例上去之后调用</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 引入基本模板</span>
<span class="hljs-keyword">let</span> echarts = <span class="hljs-built_in">require</span>(<span class="hljs-string">'echarts/lib/echarts'</span>)

<span class="hljs-comment">// 引入柱状图组件</span>
<span class="hljs-built_in">require</span>(<span class="hljs-string">'echarts/lib/chart/bar'</span>)

<span class="hljs-comment">// 引入提示框和title组件</span>
<span class="hljs-built_in">require</span>(<span class="hljs-string">'echarts/lib/component/tooltip'</span>)
<span class="hljs-built_in">require</span>(<span class="hljs-string">'echarts/lib/component/title'</span>)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'hello'</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'Welcome to Your Vue.js App'</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.drawLine();
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">drawLine</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 基于准备好的dom，初始化echarts实例</span>
      <span class="hljs-keyword">let</span> myChart = echarts.init(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'myChart'</span>))
      <span class="hljs-comment">// 绘制图表</span>
     <span class="hljs-attr">title</span>: &#123;
        <span class="hljs-attr">text</span>: <span class="hljs-string">'折线图堆叠'</span>
    &#125;,
    <span class="hljs-attr">tooltip</span>: &#123;
        <span class="hljs-attr">trigger</span>: <span class="hljs-string">'axis'</span>
    &#125;,
    <span class="hljs-attr">legend</span>: &#123;
        <span class="hljs-attr">data</span>: [<span class="hljs-string">'邮件营销'</span>, <span class="hljs-string">'联盟广告'</span>, <span class="hljs-string">'视频广告'</span>, <span class="hljs-string">'直接访问'</span>, <span class="hljs-string">'搜索引擎'</span>]
    &#125;,
    <span class="hljs-attr">grid</span>: &#123;
        <span class="hljs-attr">left</span>: <span class="hljs-string">'3%'</span>,
        <span class="hljs-attr">right</span>: <span class="hljs-string">'4%'</span>,
        <span class="hljs-attr">bottom</span>: <span class="hljs-string">'3%'</span>,
        <span class="hljs-attr">containLabel</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">toolbox</span>: &#123;
        <span class="hljs-attr">feature</span>: &#123;
            <span class="hljs-attr">saveAsImage</span>: &#123;&#125;
        &#125;
    &#125;,
    <span class="hljs-attr">xAxis</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'category'</span>,
        <span class="hljs-attr">boundaryGap</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">data</span>: [<span class="hljs-string">'周一'</span>, <span class="hljs-string">'周二'</span>, <span class="hljs-string">'周三'</span>, <span class="hljs-string">'周四'</span>, <span class="hljs-string">'周五'</span>, <span class="hljs-string">'周六'</span>, <span class="hljs-string">'周日'</span>]
    &#125;,
    <span class="hljs-attr">yAxis</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'value'</span>
    &#125;,
    <span class="hljs-attr">series</span>: [
        &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'邮件营销'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'line'</span>,
            <span class="hljs-attr">stack</span>: <span class="hljs-string">'总量'</span>,
            <span class="hljs-attr">data</span>: [<span class="hljs-number">120</span>, <span class="hljs-number">132</span>, <span class="hljs-number">101</span>, <span class="hljs-number">134</span>, <span class="hljs-number">90</span>, <span class="hljs-number">230</span>, <span class="hljs-number">210</span>]
        &#125;,
        &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'联盟广告'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'line'</span>,
            <span class="hljs-attr">stack</span>: <span class="hljs-string">'总量'</span>,
            <span class="hljs-attr">data</span>: [<span class="hljs-number">220</span>, <span class="hljs-number">182</span>, <span class="hljs-number">191</span>, <span class="hljs-number">234</span>, <span class="hljs-number">290</span>, <span class="hljs-number">330</span>, <span class="hljs-number">310</span>]
        &#125;,
        &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'视频广告'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'line'</span>,
            <span class="hljs-attr">stack</span>: <span class="hljs-string">'总量'</span>,
            <span class="hljs-attr">data</span>: [<span class="hljs-number">150</span>, <span class="hljs-number">232</span>, <span class="hljs-number">201</span>, <span class="hljs-number">154</span>, <span class="hljs-number">190</span>, <span class="hljs-number">330</span>, <span class="hljs-number">410</span>]
        &#125;,
        &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'直接访问'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'line'</span>,
            <span class="hljs-attr">stack</span>: <span class="hljs-string">'总量'</span>,
            <span class="hljs-attr">data</span>: [<span class="hljs-number">320</span>, <span class="hljs-number">332</span>, <span class="hljs-number">301</span>, <span class="hljs-number">334</span>, <span class="hljs-number">390</span>, <span class="hljs-number">330</span>, <span class="hljs-number">320</span>]
        &#125;,
        &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'搜索引擎'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'line'</span>,
            <span class="hljs-attr">stack</span>: <span class="hljs-string">'总量'</span>,
            <span class="hljs-attr">data</span>: [<span class="hljs-number">820</span>, <span class="hljs-number">932</span>, <span class="hljs-number">901</span>, <span class="hljs-number">934</span>, <span class="hljs-number">1290</span>, <span class="hljs-number">1330</span>, <span class="hljs-number">1320</span>]
        &#125;
    ]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">vue3中使用Echarts</h2>
<p><strong>因为setup中没有this,而且这时候还没有渲染,所以在setup中 ,可以使用provide/inject来把echart引入进来</strong></p>
<p><strong>在根组件里引入echart,一般是App.vue</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> echarts <span class="hljs-keyword">from</span> <span class="hljs-string">'echarts'</span>
<span class="hljs-keyword">import</span> &#123; provide &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
 
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span>&#123;
    provide(<span class="hljs-string">'echarts'</span>,echarts)               <span class="hljs-comment">//provide</span>
  &#125;,
  <span class="hljs-attr">components</span>: &#123;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意的是<code>import * as echarts from 'echarts'</code>, 不能 <code>import echarts from 'echarts'</code>,这样会报错,因为5,0版本的echarts的接口已经变成了下面这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> &#123; 
 EChartsFullOption <span class="hljs-keyword">as</span> EChartsOption, 
 connect, 
 disConnect, 
 dispose,
 getInstanceByDom, 
 getInstanceById, 
 getMap, 
 init,
 registerLocale, 
 registerMap, 
 registerTheme 
 &#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在需要使用的页面,定义div</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"home-page-traffic_chart"</span> style=<span class="hljs-string">"width: 600px; height: 280px"</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>然后在需要使用到Echarts的页面inject</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'data_page'</span>,
  setup () &#123;
    <span class="hljs-keyword">const</span> trafficData = ref(&#123;&#125;)
    <span class="hljs-keyword">const</span> echarts = inject(<span class="hljs-string">'echarts'</span>)
    onMounted(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> myChart = echarts.init(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'home-page-traffic_chart'</span>))
      <span class="hljs-comment">// 绘制图表</span>
      myChart.setOption(&#123;
        <span class="hljs-attr">title</span>: &#123;
          <span class="hljs-attr">text</span>: <span class="hljs-string">'今日话务统计'</span>
        &#125;,
        <span class="hljs-attr">tooltip</span>: &#123;
          <span class="hljs-attr">trigger</span>: <span class="hljs-string">'axis'</span>,
          <span class="hljs-attr">axisPointer</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'shadow'</span>
          &#125;
        &#125;,
        <span class="hljs-attr">grid</span>: &#123;
          <span class="hljs-attr">left</span>: <span class="hljs-string">'3%'</span>,
          <span class="hljs-attr">right</span>: <span class="hljs-string">'4%'</span>,
          <span class="hljs-attr">bottom</span>: <span class="hljs-string">'3%'</span>,
          <span class="hljs-attr">containLabel</span>: <span class="hljs-literal">true</span>
        &#125;,
        <span class="hljs-attr">xAxis</span>: [
          &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'category'</span>,
            <span class="hljs-attr">data</span>: [<span class="hljs-string">'Mon'</span>, <span class="hljs-string">'Tue'</span>, <span class="hljs-string">'Wed'</span>, <span class="hljs-string">'Thu'</span>, <span class="hljs-string">'Fri'</span>, <span class="hljs-string">'Sat'</span>, <span class="hljs-string">'Sun'</span>],
            <span class="hljs-attr">axisTick</span>: &#123;
              <span class="hljs-attr">alignWithLabel</span>: <span class="hljs-literal">true</span>
            &#125;
          &#125;
        ],
        <span class="hljs-attr">yAxis</span>: [
          &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'value'</span>
          &#125;
        ],
        <span class="hljs-attr">series</span>: [
          &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'直接访问'</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">'bar'</span>,
            <span class="hljs-attr">barWidth</span>: <span class="hljs-string">'60%'</span>,
            <span class="hljs-attr">data</span>: [<span class="hljs-number">10</span>, <span class="hljs-number">52</span>, <span class="hljs-number">200</span>, <span class="hljs-number">334</span>, <span class="hljs-number">390</span>, <span class="hljs-number">330</span>, <span class="hljs-number">220</span>]
          &#125;
        ]
      &#125;)
      <span class="hljs-built_in">window</span>.onresize = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        myChart.resize()
      &#125;
    &#125;)
    <span class="hljs-keyword">return</span> &#123;
    &#125;
  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果图</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47658c8999c0400d9f8652ea9a424fbb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            