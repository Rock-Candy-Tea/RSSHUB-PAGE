
---
title: 'Echarts---图例组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b398f254af76495c8655c0ee912df3b6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 05:05:06 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b398f254af76495c8655c0ee912df3b6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>图例（legend）组件是ECharts中较为常用的组件，它用于以不同的颜色区别系列标记的名字，表述了数据与图形的关联。用户在操作时，可以通过单击图例控制哪些数据系列显示或不显示。
在ECharts 3.x/ECharts 4.x中，单个ECharts实例可以存在多个图例组件，方便多个图例的布局。当图例数量过多时，可以使用滚动翻页。</p>
<p>在ECharts中，图例组件的属性如表所示</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b398f254af76495c8655c0ee912df3b6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d206d4cbf944337a3d81a1c4caaea93~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/448728e246304ccc983acd3fa88b2850~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图例组件属性示意图如图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4b2173fca5b4c1693dabfb68070bdfd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>利用某一年的蒸发量、降水量、最低气温和最高气温数据绘制折柱混搭图，并为图表配置图例组件。
当图例数量过多或图例长度过长时，可以使用垂直滚动图例或水平滚动图例，参见属性legend.type。此时，设置type属性的值为“scroll”，表示图例只显示在一行，多余的部分会自动呈现为滚动效果，如图所示。
由图可知，右上方的 滑动 图标即图例的滚动图标，可以将图例呈现为滚动效果。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e7348228a4440a7815fe67d49408b2a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图例的源代码如下;</p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html>

<head>
    <meta charset="utf-8">
    <!--引入ECharts脚本-->
    <script src="js/echarts.js"></script>
</head>

<body>
    <!---为ECharts准备一个具备大小（宽高）的DOM-->
    <div id="main" style="width: 600px; height: 600px"></div>
    <script type="text/javascript">
        //基于准备好的DOM，初始化ECharts图表
        var myChart = echarts.init(document.getElementById("main"));
        //指定图表的配置项和数据
        var option = &#123;
            color: ["red", 'green', 'blue', 'grey'],  //使用自己预定义的颜色
            legend: &#123;
                orient: 'horizontal',  //'vertical'
                x: 'right',  //'center'|'left'|&#123;number&#125;,
                y: 'top',  //'center'|'bottom'|&#123;number&#125;
                backgroundColor: '#eee',
                borderColor: 'rgba(178,34,34,0.8)',
                borderWidth: 4,
                padding: 10,
                itemGap: 20, textStyle: &#123; color: 'red' &#125;,
            &#125;,
            xAxis: &#123;  //配置x轴坐标系
                data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
            &#125;,
            yAxis: [  //配置y轴坐标系
                &#123;   //设置第1条y轴
                    type: 'value',
                    axisLabel: &#123; formatter: '&#123;value&#125; ml' &#125;
                &#125;,
                &#123;   //设置第2条y轴
                    type: 'value',
                    axisLabel: &#123; formatter: '&#123;value&#125; °C' &#125;,
                    splitLine: &#123; show: false &#125;
                &#125;
            ],
            series: [  //配置数据系列
                &#123;   //设置数据系列1
                    name: '某一年的蒸发量', type: 'bar',
                    data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6]
                &#125;,
                &#123;   //设置数据系列2
                    name: '某一年的降水量', smooth: true,
                    type: 'line', yAxisIndex: 1, data: [11, 11, 15, 13, 12, 13, 10]
                &#125;,
                &#123;   //设置数据系列3
                    name: '某一年的最高气温', type: 'bar',
                    data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6]
                &#125;,
                &#123;   //设置数据系列4
                    name: '某一年的最低气温', smooth: true,
                    type: 'line', yAxisIndex: 1, data: [-2, 1, 2, 5, 3, 2, 0]
                &#125;
            ]
        &#125;;
        //使用刚指定的配置项和数据显示图表
        myChart.setOption(option); 
    </script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            