
---
title: 'echarts修改tooltip默认样式（使用formatter函数拼接加工）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d5f3af792a24b339edcb246edf28116~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 20:57:05 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d5f3af792a24b339edcb246edf28116~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>echarts给到的默认样式略为有点朴素，本文记录一下修改tooltip默认样式，忘了的时候来查查看一下</p>
</blockquote>
<h2 data-id="heading-0">默认tooltip样式图</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d5f3af792a24b339edcb246edf28116~tplv-k3u1fbpfcp-watermark.image" alt="echarts1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">修改过后的tooltip样式图</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb43b3702ae14756b393de0ae2bc2678~tplv-k3u1fbpfcp-watermark.image" alt="echarts2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">代码如下</h2>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"echartsBox"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"main"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">xData</span>: [<span class="hljs-string">"孙悟空"</span>, <span class="hljs-string">"猪八戒"</span>, <span class="hljs-string">"沙和尚"</span>, <span class="hljs-string">"唐僧"</span>, <span class="hljs-string">"白龙马"</span>, <span class="hljs-string">"白骨精"</span>, <span class="hljs-string">"狐狸精"</span>],
      <span class="hljs-attr">yData1</span>: [<span class="hljs-number">115</span>, <span class="hljs-number">198</span>, <span class="hljs-number">88</span>, <span class="hljs-number">77</span>, <span class="hljs-number">99</span>, <span class="hljs-number">123</span>, <span class="hljs-number">36</span>],
      <span class="hljs-attr">yData2</span>: [<span class="hljs-number">88</span>, <span class="hljs-number">89</span>, <span class="hljs-number">77</span>, <span class="hljs-number">66</span>, <span class="hljs-number">100</span>, <span class="hljs-number">145</span>, <span class="hljs-number">53</span>],
      <span class="hljs-attr">yData3</span>: [<span class="hljs-number">18</span>, <span class="hljs-number">55</span>, <span class="hljs-number">42</span>, <span class="hljs-number">63</span>, <span class="hljs-number">77</span>, <span class="hljs-number">85</span>, <span class="hljs-number">58</span>],
      <span class="hljs-attr">grid</span>: &#123;
        <span class="hljs-comment">// 网格线配置</span>
        <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">lineStyle</span>: &#123;
          <span class="hljs-attr">color</span>: [<span class="hljs-string">"#e9e9e9"</span>],
          <span class="hljs-attr">width</span>: <span class="hljs-number">1</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">"solid"</span>,
        &#125;,
      &#125;,
    &#125;;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 在通过mounted调用让echarts渲染</span>
    <span class="hljs-built_in">this</span>.echartsInit();
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">echartsInit</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">let</span> main = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"main"</span>); <span class="hljs-comment">// 获取dom元素作为eacharts的容器</span>
      <span class="hljs-built_in">this</span>.$echarts.init(main).setOption(&#123;
        <span class="hljs-attr">xAxis</span>: [
          &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">"category"</span>, <span class="hljs-comment">// 类别</span>
            <span class="hljs-attr">data</span>: <span class="hljs-built_in">this</span>.xData, <span class="hljs-comment">// x轴类别对应的值</span>
            <span class="hljs-attr">splitLine</span>: <span class="hljs-built_in">this</span>.grid, <span class="hljs-comment">// 给x轴加上网格线</span>
          &#125;,
        ],
        <span class="hljs-attr">yAxis</span>: &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">"value"</span>,
          <span class="hljs-attr">splitLine</span>: <span class="hljs-built_in">this</span>.grid, <span class="hljs-comment">// 给y轴加上网格线</span>
          <span class="hljs-attr">axisLabel</span>: &#123;
            <span class="hljs-attr">formatter</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value, index</span>) </span>&#123;
              <span class="hljs-keyword">return</span> value + <span class="hljs-string">"分"</span>;
            &#125;,
          &#125;,
        &#125;,
        <span class="hljs-attr">tooltip</span>: &#123;
          <span class="hljs-attr">trigger</span>: <span class="hljs-string">"axis"</span>, <span class="hljs-comment">// 鼠标移入到柱子里面就会有一个提示，默认是item方式，如果有多个柱状图，堆在一块item就不太好了，个人喜欢axis方式的</span>
          <span class="hljs-attr">triggerOn</span>: <span class="hljs-string">"mousemove"</span>, <span class="hljs-comment">// 什么时候触发提示小图标，点击click的时候，或者鼠标滑过的时候，默认是mousemove鼠标滑过</span>
          <span class="hljs-comment">/* formatter可以以字符串模板方式写，也可以用回调函数写，不过字符串模板略有限制，我们使用回调函数会灵活点 */</span>
          <span class="hljs-attr">formatter</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">params</span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"--x轴类目对应的参数数组--"</span>, params); <span class="hljs-comment">// 比如当鼠标hover到孙悟空同学这一列的时候，这个params数组存放的每一项数据分别是语数外三门成绩的具体信息</span>
            <span class="hljs-keyword">var</span> res = <span class="hljs-comment">// 字符串形式的html标签会被echarts转换渲染成数据，这个res主要是画的tooltip里的上部分的标题部分</span>
              <span class="hljs-string">"<div style='margin-bottom:5px;padding:0 12px;width:100%;height:24px;line-height:24px;background:pink;border-radius:3px;'><p>"</span> +
              params[<span class="hljs-number">0</span>].name +
              <span class="hljs-string">" </p></div>"</span>;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < params.length; i++) &#123;
              <span class="hljs-comment">//因为是个数组，所以要遍历拿到里面的数据，并加入到tooltip的数据内容部分里面去</span>
              res += <span class="hljs-string">`<div style="color: #fff;font-size: 14px; padding:0 12px;line-height: 24px">
                  <span style="display:inline-block;margin-right:5px;border-radius:2px;width:10px;height:10px;background-color:<span class="hljs-subst">$&#123;[
                    params[i].color, <span class="hljs-regexp">//</span> 默认是小圆点，我们将其修改成有圆角的正方形，这里用的是模板字符串。并拿到对应颜色、名字、数据
                  ]&#125;</span>;"></span>
                  <span class="hljs-subst">$&#123;params[i].seriesName&#125;</span>
                  <span class="hljs-subst">$&#123;params[i].data&#125;</span>分
                </div>`</span>;
            &#125;
            <span class="hljs-keyword">return</span> res; <span class="hljs-comment">// 经过这么一加工，最终返回出去并渲染，最终就出现了我们所看的效果</span>
          &#125;,
        &#125;,
        <span class="hljs-attr">legend</span>: &#123;
          <span class="hljs-comment">// legend 是对series进行筛选，所以data中每一项就是series中的每一项的标识，所以就是以name为标识</span>
          <span class="hljs-attr">data</span>: [<span class="hljs-string">"语文成绩"</span>, <span class="hljs-string">"数学成绩"</span>, <span class="hljs-string">"英语成绩"</span>],
        &#125;,
        <span class="hljs-attr">series</span>: [
          &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"语文成绩"</span>,
            <span class="hljs-attr">data</span>: <span class="hljs-built_in">this</span>.yData1,
            <span class="hljs-attr">type</span>: <span class="hljs-string">"bar"</span>, <span class="hljs-comment">// 类型为柱状图</span>
            <span class="hljs-attr">barWidth</span>: <span class="hljs-number">40</span>, <span class="hljs-comment">// 柱状图的宽度</span>
            <span class="hljs-attr">label</span>: &#123;
              <span class="hljs-comment">// 展示具体柱状图的数值</span>
              <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
            &#125;,
            <span class="hljs-attr">barGap</span>: <span class="hljs-string">"0"</span>,
            <span class="hljs-comment">/*
              注意，如果想要把数据堆在一块，堆叠放置，只需要在series数组中的每个对象中都加入stack属性，stack英文单词的释义是：
              一叠，一摞，一堆的意思，设置stack的属性值是什么倒无所谓，但是要让其stack的属性值保持一致，保持一致，才会堆叠到一块。
            */</span>
            <span class="hljs-attr">stack</span>: <span class="hljs-string">"值无所谓，但要保持一致"</span>,
          &#125;,
          &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"数学成绩"</span>,
            <span class="hljs-attr">data</span>: <span class="hljs-built_in">this</span>.yData2,
            <span class="hljs-attr">type</span>: <span class="hljs-string">"bar"</span>, <span class="hljs-comment">// 类型为柱状图</span>
            <span class="hljs-attr">barWidth</span>: <span class="hljs-number">40</span>, <span class="hljs-comment">// 柱状图的宽度</span>
            <span class="hljs-attr">label</span>: &#123;
              <span class="hljs-comment">// 展示具体柱状图的数值</span>
              <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
            &#125;,
            <span class="hljs-comment">/*
              注意，如果想要把数据堆在一块，堆叠放置，只需要在series数组中的每个对象中都加入stack属性，stack英文单词的释义是：
              一叠，一摞，一堆的意思，设置stack的属性值是什么倒无所谓，但是要让其stack的属性值保持一致，保持一致，才会堆叠到一块。
            */</span>
            <span class="hljs-attr">stack</span>: <span class="hljs-string">"值无所谓，但要保持一致"</span>,
          &#125;,
          &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"英语成绩"</span>,
            <span class="hljs-attr">data</span>: <span class="hljs-built_in">this</span>.yData3,
            <span class="hljs-attr">type</span>: <span class="hljs-string">"bar"</span>, <span class="hljs-comment">// 类型为柱状图</span>
            <span class="hljs-attr">barWidth</span>: <span class="hljs-number">40</span>, <span class="hljs-comment">// 柱状图的宽度</span>
            <span class="hljs-attr">label</span>: &#123;
              <span class="hljs-comment">// 展示具体柱状图的数值</span>
              <span class="hljs-attr">show</span>: <span class="hljs-literal">true</span>,
            &#125;,
            <span class="hljs-comment">/*
              注意，如果想要把数据堆在一块，堆叠放置，只需要在series数组中的每个对象中都加入stack属性，stack英文单词的释义是：
              一叠，一摞，一堆的意思，设置stack的属性值是什么倒无所谓，但是要让其stack的属性值保持一致，保持一致，才会堆叠到一块。
            */</span>
            <span class="hljs-attr">stack</span>: <span class="hljs-string">"值无所谓，但要保持一致"</span>,
          &#125;,
        ],
      &#125;);
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.echartsBox</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">900px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">500px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>就不写步骤了，直接看注释方便些</p>
</blockquote></div>  
</div>
            