
---
title: 'echarts 仪表盘渐变问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: '/static/aaa.png'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 01:57:10 GMT
thumbnail: '/static/aaa.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">问题：</h1>
<p>echarts仪表盘下半圆隐约存在</p>
<h1 data-id="heading-1">原因：</h1>
<p>目前设置的axisLine.lineStyle.color，不是只是分段颜色设置，为了渐变衔接的效果，有一部分点是叠加了两层颜色设置。</p>
<p>先全长度铺了一层绿色，从左往右透明度降低；再从0.8的位置到结束，铺了一层黄色，从左往右透明度升高。</p>
<p>大致的axisLine.lineStyle.color数组设置如下：</p>
<pre><code class="copyable">axisLine.lineStyle.color =
[
[
0,
"rgba(255,255,255,0.2)"
],
......
[
0.9975,
"rgba(0, 255, 0,0.005)"
],
[
0.8,
"rgba(255, 255, 0,0.01)"
],
......
[
0.998,
"rgba(255, 255, 0,1)"
],
[
1,
"rgb(255,0,0)"
]
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样可以做出自然的过度，但是仔细查看，echarts仪表盘下半圆隐约存在。</p>
<h1 data-id="heading-2">解决办法：</h1>
<p><strong>PS：可直接跳到最后，看第6个解决方案：“6、完美的echarts仪表盘渐变设置方案”</strong></p>
<h2 data-id="heading-3">1、对color数组排序</h2>
<pre><code class="copyable">axisLine.lineStyle.color =
[
[
0,
"rgba(255,255,255,0.2)"
],
......
[
0.8,
"rgba(255, 255, 0,0.01)"
],
......
[
0.9975,
"rgba(0, 255, 0,0.005)"
],
......
[
0.998,
"rgba(255, 255, 0,1)"
],
[
1,
"rgb(255,0,0)"
]
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>现象：</strong></p>
<p>echarts仪表盘下半圆消失，但是过度明显不自然，出现条纹。</p>
<h2 data-id="heading-4">2、排序后去重</h2>
<p><strong>原因：</strong></p>
<p>因为有像0.96这类点有两个颜色设置，去重操作，留下第一个或者第二个。</p>
<p><strong>现象：</strong></p>
<p>echarts仪表盘下半圆消失，但是过度明显不自然，仍然出现条纹。
于是想到第三个方法，重复点不能直接去掉而是取中间值。</p>
<h2 data-id="heading-5">3、重复点取颜色中间值</h2>
<pre><code class="copyable">const uniqueArr = (oldArr) => &#123;
  let newArray = []
  for (let i = 0; i < oldArr.length; i++) &#123;
    if (i > 0) &#123;
      if (oldArr[i][0] !== oldArr[i - 1][0]) &#123;
        newArray.push(oldArr[i])
      &#125; else &#123;
        let co1 = newArray[newArray.length - 1][1]
        let co2 = oldArr[i][1]
        let aaa = co1.split(',')[3].replace(')', '')
        let bbb = co2.split(',')[3].replace(')', '')
        let opacity = (parseFloat(aaa) + parseFloat(bbb)) / 2
        newArray[newArray.length - 1][1] = 'rgba(128, 255, 0, ' + opacity + ')'
      &#125;
    &#125;
  &#125;
  return newArray
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>现象：</strong></p>
<p>echarts仪表盘下半圆消失，但是过度明显不自然，仍然出现条纹。</p>
<h2 data-id="heading-6">4、不进行颜色叠加</h2>
<p><strong>现象：</strong></p>
<p>echarts仪表盘下半圆消失，但是过度明显不自然。</p>
<h2 data-id="heading-7">5、用axisTick.lineStyle.color.image属性设置渐变刻度。</h2>
<p>此方法用刻度当调图，无法再设置坐标轴线样式axisLine.lineStyle.color，因为已被覆盖。</p>
<pre><code class="copyable"><img src="/static/aaa.png" id="bg_img" style="display:none"/>
注意：确保img节点已挂载
axisTick: &#123;
show: true,
length: 30,
splitNumber: 100,
lineStyle: &#123;
  color: &#123;
image: document.getElementById('bg_img'),
repeat: 'no-repeat'
  &#125;,
  width: 3
&#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>现象：</strong></p>
<p>echarts仪表盘下半圆消失，过度很自然，但是无法再设置坐标轴线样式，无法动态置灰某段值，且指针不能随当前坐标轴点颜色改变而改变。</p>
<h2 data-id="heading-8">6、完美的echarts仪表盘渐变设置方案</h2>
<p>使用series即可！！！</p>
<p>每个series的样式一模一样，值也一样，能不显示就不显示，但是颜色axisLine.lineStyle.color必须设置不一样，每一个series设置一个单独的从头到尾的渐变即可。</p>
<p><strong>注意：</strong></p>
<p>虽然多个series只是为了叠加颜色，但是必须充填数据项和值，不然提示框组件tooltip、指针显示不同步，打不到叠加颜色的指针效果。</p></div>  
</div>
            