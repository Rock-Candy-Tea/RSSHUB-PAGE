
---
title: 'ECharts的多图表联动'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d423118813744c782b47ee35348d06d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 05:41:25 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d423118813744c782b47ee35348d06d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>当需要展示的数据比较多时，放在一个图表进行展示的效果并不佳，此时，可以考虑使用两个图表进行联动展示。
ECharts提供了多图表联动（connect）的功能，连接的多个图表可以共享组件事件并实现保存图片时的自动拼接。多图表联动支持直角系下tooltip的联动</p>
<p>实现EChart中的多图表联动，可以使用以下两种方法。
（1）分别设置每个ECharts对象为相同的group值，并通过在调用ECharts对象的connect方法时，传入group值，从而使用多个ECharts对象建立联动关系，格式如下。
myChart1.group = 'group1';  //给第1个ECharts对象设置一个group值
myChart2.group = 'group1';  //给第2个ECharts对象设置一个相同的group值
echarts.connect('group1');  //调用ECharts对象的connect方法时，传入group值</p>
<p>（2）直接调用ECharts的connect方法，参数为一个由多个需要联动的ECharts对象所组成的数组，格式如下。
echarts.connect([myChart1,myChart2]);
若想要解除已有的多图表联动，则可以调用disConnect方法，格式如下。
echarts.disConnect('group1');</p>
<p>利用某学院2019年和2020年的专业招生情况绘制柱状图联动图表，如图所示。
由图可知，共有上下两个柱状图，分别表示2019、2020两个年度的招生情况汇总。由于建立了多图表联动，所以当鼠标滑过2019年或2020年的人工智能专业柱体上时，系统会同时在2019年、2020年的人工智能专业上自动弹出相应的详情提示框（tooltip）。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d423118813744c782b47ee35348d06d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html>

<head>
<meta charset="utf-8">
<script type="text/javascript" src='js/echarts.js'></script>
</head>

<body>
<div id="main1" style="width: 600px; height:400px"></div>
<div id="main2" style="width: 600px; height:400px"></div>
<script type="text/javascript">
//基于准备好的dom，初始化ECharts图表
var myChart1 = echarts.init(document.getElementById("main1"));
var option1 = &#123;  //指定第1个图表的配置项和数据
color: ['LimeGreen', 'DarkGreen', 'red', 'blue', 'Purple'],
backgroundColor: 'rgba(128, 128, 128, 0.1)',  //rgba设置透明度0.1
title: &#123; text: '某学院2019年专业招生情况汇总表', left: 40, top: 5 &#125;,
tooltip: &#123; tooltip: &#123; show: true &#125;, &#125;,
legend: &#123; data: ['2019年招生'], left: 422, top: 8 &#125;,
xAxis: [&#123;
data: ["大数据", "云计算", "Oracle", "ERP", "人工智能",
"软件开发", "移动开发", "网络技术"],axisLabel:&#123;interval: 0&#125;
&#125;],
yAxis: [&#123; type: 'value', &#125;],
series: [&#123;  //配置第1个图表的数据系列
name: '2019年招生',
type: 'bar', barWidth: 40,  //设置柱状图中每个柱子的宽度
data: [125, 62, 45, 56, 123, 205, 108, 128],
&#125;]
&#125;;
//基于准备好的dom,初始化ECharts图表
var myChart2 = echarts.init(document.getElementById("main2"));
var option2 = &#123;  //指定第2个图表的配置项和数据
color: ['blue', 'LimeGreen', 'DarkGreen', 'red', 'Purple'],
backgroundColor: 'rgba(128, 128, 128, 0.1)',  //rgba设置透明度0.1
title: &#123; text: '某学院2020年专业招生情况汇总表', left: 40, top: 8 &#125;,
tooltip: &#123; show: true &#125;,
legend: &#123; data: ['2020年招生'], left: 422, top: 8 &#125;,
xAxis: [&#123;
data: ["大数据", "云计算", "Oracle", "ERP", "人工智能",
"软件开发", "移动开发", "网络技术"],axisLabel:&#123;interval: 0&#125;
&#125;],
yAxis: [&#123; type: 'value', &#125;],
series: [&#123;  //配置第2个图表的数据系列
name: '2020年招生',
type: 'bar', barWidth: 40,  //设置柱状图中每个柱子的宽度
data: [325, 98, 53, 48, 222, 256, 123, 111],
&#125;]
&#125;;
myChart1.setOption(option1);  //为myChart1对象加载数据
myChart2.setOption(option2);  //为myChart2对象加载数据
//多图表联动配置方法1：分别设置每个echarts对象的group值
myChart1.group = 'group1';
myChart2.group = 'group1';
echarts.connect('group1');
//多图表联动配置方法2：直接传入需要联动的echarts对象myChart1，myChart2
//echarts.connect([myChart1,myChart2]);
</script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用某大学各专业2016－2020年的招生情况绘制饼图与柱状图的联动图表，如图所示。
由图可知，上方的饼图和下方的柱状图（柱状图也可以通过工具箱转为折线图）。当鼠标滑过饼图的某个扇区时，饼图出现的详情提示框显示相应扇区所对应年份的招生人数及其所占各年总招生人数的比例，同时柱状图（或折线图）也会相应地出现详情提示框，显示对应年份各个专业的招生人数的详细数据。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e48fe18caafd415fa3c28edb7d54d07b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>源代码如下：</p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html>

<head>
<meta charset="utf-8">
<script type="text/javascript" src='js/echarts.js'></script>
</head>

<body>
<div id="main1" style="width: 600px; height:400px"></div>
<div id="main2" style="width: 600px; height:400px"></div>
<script type="text/javascript">
//基于准备好的dom，初始化ECharts图表
var myChart1 = echarts.init(document.getElementById("main1"));
var option1 = &#123;  //指定第1个图表option1的配置项和数据
color: ['red', 'Lime', 'blue', 'DarkGreen', 'DarkOrchid', 'Navy'],
backgroundColor: 'rgba(128, 128, 128, 0.1)',  //配置背景色，rgba设置透明度0.1
title: &#123; text: '某大学各专业历年招生情况分析', x: 'center', y: 12 &#125;,
tooltip: &#123; trigger: "item", formatter: "&#123;a&#125;<br/>&#123;b&#125;:&#123;c&#125;(&#123;d&#125;%)" &#125;,
legend: &#123;
orient: 'vertical', x: 15, y: 15,
data: ['2016', '2017', '2018', '2019', '2020']
&#125;,
series: [&#123;  //配置第1个图表的数据系列
name: '总人数:', type: 'pie',
radius: '70%', center: ['50%', 190],
data: [
&#123; value: 1695, name: '2016' &#125;, &#123; value: 1790, name: '2017' &#125;,
&#123; value: 2250, name: '2018' &#125;, &#123; value: 2550, name: '2019' &#125;,
&#123; value: 2570, name: '2020' &#125;]
&#125;]
&#125;;
myChart1.setOption(option1);  //使用指定的配置项和数据显示饼图
//基于准备好的dom，初始化ECharts图表
var myChart2 = echarts.init(document.getElementById("main2"));
var option2 = &#123;  //指定第2个图表的配置项和数据
color: ['red', 'Lime', 'blue', 'DarkGreen', 'DarkOrchid', 'Navy'],
backgroundColor: 'rgba(128, 128, 128, 0.1)',  //配置背景色，rgba设置透明度0.1
tooltip: &#123; trigger: 'axis', axisPointer: &#123; type: 'shadow' &#125; &#125;,  //配置提示框组件
legend: &#123;  //配置图例组件
left: 42, top: 25,
data: ['大数据', 'Oracle', '云计算', '人工智能', '软件工程']
&#125;,
toolbox: &#123;  //配置第2个图表的工具箱组件
show: true, orient: 'vertical', left: 550, top: 'center',
feature: &#123;
mark: &#123; show: true &#125;, restore: &#123; show: true &#125;, saveAsImage: &#123; show: true &#125;,
magicType: &#123; show: true, type: ['line', 'bar', 'stack', 'tiled'] &#125;
&#125;
&#125;,
xAxis: [&#123;
type: 'category',
data: ['2016', '2017', '2018', '2019', '2020']
&#125;],  //配置第2个图表的x轴坐标系
yAxis: [&#123; type: 'value', splitArea: &#123; show: true &#125; &#125;],  //配置第2个图表的y轴坐标系
series: [  //配置第2个图表的数据系列
&#123;
name: '大数据', type: 'bar', stack: '总量',
data: [301, 334, 390, 330, 320], barWidth: 45,
&#125;,
&#123; name: 'Oracle', type: 'bar', stack: '总量', data: [101, 134, 90, 230, 210] &#125;,
&#123; name: '云计算', type: 'bar', stack: '总量', data: [191, 234, 290, 330, 310] &#125;,
&#123; name: '人工智能', type: 'bar', stack: '总量', data: [201, 154, 190, 330, 410] &#125;,
&#123; name: '软件工程', type: 'bar', stack: '总量', data: [901, 934, 1290, 1330, 1320] &#125;
]
&#125;;
myChart2.setOption(option2);  //使用指定的配置项和数据显示堆叠柱状图
//多图表联动配置方法1：分别设置每个echarts对象的group值
myChart1.group = 'group1';
myChart2.group = 'group1';
echarts.connect('group1');
     //多图表联动配置方法2：直接传入需要联动的echarts对象myChart1，myChart2
    //echarts.connect([myChart1,myChart2]);
</script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            