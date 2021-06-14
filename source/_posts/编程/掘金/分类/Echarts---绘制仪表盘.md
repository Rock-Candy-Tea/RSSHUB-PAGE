
---
title: 'Echarts---绘制仪表盘'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a59df655d5c41dbab29aea45ea67bcc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 23:28:39 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a59df655d5c41dbab29aea45ea67bcc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>仪表盘（Gauge）也被称为拨号图表或速度表图，用于显示类似于速度计上的读数的数据，是一种拟物化的展示形式。
仪表盘是常用的商业智能（BI）类的图表之一，可以轻松展示用户的数据，并能清晰地看出某个指标值所在的范围。
为了更直观地查看项目的实际完成率数据，以及汽车的速度、发动机的转速、油表和水表的现状，需要在ECharts中绘制单仪表盘和多仪表盘进行展示。</p>
<p>ECharts的主要创始者林峰曾经说过，他在一次漫长的拥堵当中，有机会观察和思考仪表盘的问题，突然间意识到仪表盘不仅是在传达数据，而且能传达出一种易于记忆的状态，并且影响人的情绪，这种正面或负面的情绪影响对决策运营有一定的帮助。
在仪表盘中，仪表盘的颜色可以用于划分指示值的类别，而刻度标示、指针指示维度、指针角度则可用于表示数值。
仪表盘只需分配最小值和最大值，并定义一个颜色范围，指针将显示出关键指标的数据或当前进度。仪表盘可应用于诸如速度、体积、温度、进度、完成率、满意度等。</p>
<p>1 绘制单仪表盘</p>
<p>利用项目实际完成率数据观察项目的完成情况，如图所示。
由图可知，使用3种不同的灰度表示项目的实际完成情况。其中，左下角区域提示项目实际完成率过低，而变动的指针与下方随之变动的数字同时指示出当前的实际完成率。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a59df655d5c41dbab29aea45ea67bcc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图例的源代码如下：</p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html>

<head>
    <meta charset="utf-8">
    <!-- 引入 ECharts 文件 -->
    <script src="js/echarts.js"></script>

</head>

<body>
    <!---为ECharts准备一个具备大小（宽高）的DOM--->
    <div id="main" style="width: 800px; height: 600px"></div>
    <script type="text/javascript">
        //基于准备好的DOM，初始化ECharts图表
        var myChart = echarts.init(document.getElementById("main"));
        //指定图表的配置项和数据
        var color1 = [[0.2, "rgba(255,0,0,1)"], [0.8, "rgba(0,255,255,1)"], [1, "rgba(0,255,0,1)"]];
        var data1 = [&#123;
            name: "完成率(%)",
            value: 50,
        &#125;];
        var option = &#123;  //指定图表的配置项和数据
            backgroundColor: 'rgba(128, 128, 128, 0.1)',  //rgba设置透明度0.1
            tooltip: &#123;  //配置提示框组件
                show: true,
                formatter: "&#123;b&#125;：&#123;c&#125;%",
                backgroundColor: "rgba(255,0,0,0.8)",  //设置提示框浮层的背景颜色
                borderColor: "#333",  //设置提示框浮层的边框颜色
                borderWidth: 0,  //设置提示框浮层的边框宽
                padding: 5,  //设置提示框浮层内边距，单位px，默认各方向内边距为5
                textStyle: &#123;  //设置提示框浮层的文本样式
                    //color,fontStyle,fontWeight,fontFamily,fontSize,lineHeight
                &#125;,
            &#125;,
            title: &#123;  //配置标题组件
                text: '项目实际完成率(%)',
                x: 'center', y: 25,
                show: true,  //设置是否显示标题，默认true
                //设置相对于仪表盘中心的偏移位置
                //数组第一项是水平方向的偏移，第二项是垂直方向的偏移
                offsetCenter: [50, "20%"],
                textStyle: &#123;
                    fontFamily: "黑体",  //设置字体名称，默认宋体
                    color: "blue",  //设置字体颜色，默认#333
                    fontSize: 20,  //设置字体大小，默认15
                &#125;
            &#125;,
            series: [
                &#123;
                    name: "单仪表盘示例",  //设置系列名称，用于tooltip的显示，legend的图例筛选
                    type: "gauge",  //设置系列类型
                    radius: "80%",  //设置参数：number，string，仪表盘半径，默认75% 
                    center: ["50%", "55%"],  //设置仪表盘位置(圆心坐标)
                    startAngle: 225,  //设置仪表盘起始角度，默认225
                    endAngle: -45,  //设置仪表盘结束角度，默认-45
                    clockwise: true,  //设置仪表盘刻度是否是顺时针增长，默认true
                    min: 0,  //设置最小的数据值，默认0，映射到minAngle
                    max: 100,  //设置最大的数据值，默认100，映射到maxAngle
                    splitNumber: 10,  //设置仪表盘刻度的分割段数，默认10
                    axisLine: &#123;  //设置仪表盘轴线(轮廓线)相关配置
                        show: true,  //设置是否显示仪表盘轴线(轮廓线)，默认true
                        lineStyle: &#123;  //设置仪表盘轴线样式
                            color: color1,  //设置仪表盘的轴线可以被分成不同颜色的多段
                            opacity: 1,  //设置图形透明度，支持从0到1的数字，为0时不绘制该图形
                            width: 30,  //设置轴线宽度，默认30
                            shadowBlur: 20,  //设置(发光效果)图形阴影的模糊大小
                            shadowColor: "#fff",  //设置阴影颜色，支持的格式同color
                        &#125;
                    &#125;,
                    splitLine: &#123;  //设置分隔线样式
                        show: true,  //设置是否显示分隔线，默认true
                        length: 30,  //设置分隔线线长，支持相对半径的百分比，默认30
                        lineStyle: &#123;  //设置分隔线样式
                            color: "#eee",  //设置线的颜色，默认#eee
                            //设置图形透明度，支持从0到1的数字，为0时不绘制该图形
                            opacity: 1,
                            width: 2,  //设置线度，默认2
                            type: "solid",  //设置线的类型，默认solid，此外还有dashed，dotted
                            shadowBlur: 10,  //设置(发光效果)图形阴影的模糊大小
                            shadowColor: "#fff",  //设置阴影颜色，支持的格式同color
                        &#125;
                    &#125;,
                    axisTick: &#123;  //设置刻度(线)样式
                        show: true,  //设置是否显示刻度(线)，默认true
                        splitNumber: 5,  //设置分隔线之间分割的刻度数，默认5
                        length: 8,  //设置刻度线长.支持相对半径的百分比，默认8
                        lineStyle: &#123;  //设置刻度线样式
                            color: "#eee",  //设置线的颜色，默认#eee
                            //设置图形透明度.支持从0到1的数字，为0时不绘制该图形
                            opacity: 1,
                            width: 1,  //设置线度，默认 1
                            type: "solid",  //设置线的类型，默认solid，此外还有dashed，dotted
                            shadowBlur: 10,  //设置(发光效果)图形阴影的模糊大小
                            shadowColor: "#fff",  //设置阴影颜色，支持的格式同color
                        &#125;,
                    &#125;,
                    axisLabel: &#123;  //设置刻度标签
                        show: true,  //设置是否显示标签，默认true
                        distance: 25,  //设置标签与刻度线的距离，默认5
                        color: "blue",  //设置文字的颜色
                        fontSize: 32,  //设置文字的字体大小，默认5
                        //设置刻度标签的内容格式器，支持字符串模板和回调函数两种形式
                        formatter: "&#123;value&#125;",
                    &#125;,
                    pointer: &#123;  //设置仪表盘指针
                        show: true,  //设置是否显示指针，默认true
                        //设置指针长度,可以是绝对值，也可是相对于半径的百分比，默认80%
                        length: "70%",
                        width: 9,  //设置指针宽度，默认8
                    &#125;,
                    itemStyle: &#123;  //设置仪表盘指针样式
                        color: "auto",  //设置指针颜色，默认(auto)取数值所在的区间的颜色
                        opacity: 1,  //设置图形透明度，支持从0到1的数字，为0时不绘制该图形
                        borderWidth: 0,  //设置描边线宽,默认0，为0时无描边
                        //设置柱条的描边类型,默认为实线，支持'solid'，'dashed'，'dotted'
                        borderType: "solid",
                        borderColor: "#000",  //设置图形的描边颜色，默认"#000"，不支持回调函数
                        shadowBlur: 10,  //设置(发光效果)图形阴影的模糊大小
                        shadowColor: "#fff",  //设置阴影颜色，支持的格式同color
                    &#125;,
                    emphasis: &#123;  //设置高亮的仪表盘指针样式
                        itemStyle: &#123;
                            //高亮和正常,两者具有同样的配置项，只是在不同状态下配置项的值不同
                        &#125;
                    &#125;,
                    detail: &#123;  //设置仪表盘详情，用于显示数据
                        show: true,  //设置是否显示详情，默认true
                        offsetCenter: [0, "50%"],  //设置相对于仪表盘中心的偏移位置
                        color: "auto",  //设置文字的颜色，默认auto
                        fontSize: 30,  //设置文字的字体大小，默认15
                        formatter: "&#123;value&#125;%",  //格式化函数或者字符串
                    &#125;,
                    data: data1
                &#125;
            ]
        &#125;;
        setInterval(function () &#123;
            option.series[0].data[0].value = (Math.random() * 100).toFixed(2);
            myChart.setOption(option, true);  //使用指定的配置项和数据显示图表
        &#125;, 2000);  //每2秒重新渲染一次，以实现动态效果
    </script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2 绘制多仪表盘</p>
<p>前面介绍的单仪表盘，相对比较简单，只能表示一类事物的范围情况。
如果需要同时表现几类不同事物的范围情况，那么应该使用多仪表盘进行展示。利用汽车的速度、发动机的转速、油表和水表的数据展示汽车的现状，如图所示。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33d6408565954ee099bf33c6c9c2ad0b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图例的源代码如下：</p>
<pre><code class="hljs language-<!DOCTYPE copyable" lang="<!DOCTYPE"><html>

<head>
<meta charset="utf-8">
<!-- 引入 ECharts 文件 -->
<script src="js/echarts.js"></script>

</head>

<body>
<!---为ECharts准备一个具备大小（宽高）的DOM--->
<div id="main" style="width: 800px; height: 600px"></div>
<script type="text/javascript">
//基于准备好的DOM，初始化ECharts图表
var myChart = echarts.init(document.getElementById("main"));
//指定图表的配置项和数据
var option = &#123;  //指定图表的配置项和数据
backgroundColor: 'rgba(128, 128, 128, 0.1)',  //rgba设置透明度0.1
title: &#123;  //配置标题组件
text: '多仪表盘实例 (共四个仪表盘)',
x: 'center', y: 100,
show: true,  //设置是否显示标题，默认true
offsetCenter: [50, "20%"],  //设置相对于仪表盘中心的偏移
textStyle: &#123;
fontFamily: "黑体",  //设置字体名称，默认宋体
color: "blue",  //设置字体颜色，默认#333
fontSize: 20,  //设置字体大小，默认15
&#125;
&#125;,
tooltip: &#123; formatter: "&#123;a&#125; <br/>&#123;c&#125; &#123;b&#125;" &#125;,  //配置提示框组件
series: [  //配置数据系列，共有4个仪表盘
&#123;   //设置数据系列之1：速度
name: '速度', type: 'gauge', z: 3,
min: 0,  //设置速度仪表盘的最小值
max: 220,  //设置速度仪表盘的最大值
splitNumber: 22,  //设置速度仪表盘的分隔数目为22
radius: '50%',  //设置速度仪表盘的大小
axisLine: &#123; lineStyle: &#123; width: 10 &#125; &#125;,
axisTick: &#123;  //设置坐标轴小标记
length: 15,  //设置属性length控制线长
splitNumber: 5,  //设置坐标轴小标记的分隔数目为5
lineStyle: &#123;  //设置属性lineStyle控制线条样式
color: 'auto'
&#125;
&#125;,
splitLine: &#123; length: 20, lineStyle: &#123; color: 'auto' &#125; &#125;,
title: &#123; textStyle: &#123; fontWeight: 'bolder', fontSize: 20, fontStyle: 'italic' &#125; &#125;,
detail: &#123; textStyle: &#123; fontWeight: 'bolder' &#125; &#125;,
data: [&#123; value: 40, name: '车速(km/h)' &#125;]
&#125;,
&#123;   //设置数据系列之2：转速
name: '转速', type: 'gauge',
center: ['20%', '55%'],  //设置转速仪表盘中心点的位置，默认全局居中
radius: '35%',  //设置转速油表仪表盘的大小
min: 0,  //设置转速仪表盘的最小值
max: 7,  //设置转速仪表盘的最大值
endAngle: 45,
splitNumber: 7,  //设置转速仪表盘的分隔数目为7
axisLine: &#123; lineStyle: &#123; width: 8 &#125; &#125;,  //设置属性lineStyle控制线条样式
axisTick: &#123;  //设置坐标轴小标记
length: 12,  //设置属性length控制线长
splitNumber: 5,  //设置坐标轴小标记的分隔数目为5
lineStyle: &#123;  //设置属性lineStyle控制线条样式
color: 'auto'
&#125;
&#125;,
splitLine: &#123;  //设置分隔线
length: 20,  //设置属性length控制线长
lineStyle: &#123;  //设置属性lineStyle（详见lineStyle）控制线条样式
color: 'auto'
&#125;
&#125;,
pointer: &#123; width: 5 &#125;,
title: &#123; offsetCenter: [0, '-30%'], &#125;,
detail: &#123; textStyle: &#123; fontWeight: 'bolder' &#125; &#125;,
data: [&#123; value: 1.5, name: '转速(x1000 r/min)' &#125;]
&#125;,
&#123;   //设置数据系列之3：油表
name: '油表', type: 'gauge',
center: ['77%', '50%'],  //设置油表仪表盘中心点的位置，默认全局居中
radius: '25%',  //设置油表仪表盘的大小
min: 0,  //设置油表仪表盘的最小值
max: 2,  //设置油表仪表盘的最小值
startAngle: 135, endAngle: 45,
splitNumber: 2,  //设置油表的分隔数目为2
axisLine: &#123; lineStyle: &#123; width: 8 &#125; &#125;,  //设置属性lineStyle控制线条样式
axisTick: &#123;  //设置坐标轴小标记
splitNumber: 5,  //设置小标记分隔数目为5
length: 10,  //设置属性length控制线长
lineStyle: &#123;  //设置属性lineStyle控制线条样式
color: 'auto'
&#125;
&#125;,
axisLabel: &#123;
formatter: function (v) &#123;
switch (v + '') &#123;
case '0': return 'E';
case '1': return '油表';
case '2': return 'F';
&#125;
&#125;
&#125;,
splitLine: &#123;  //设置分隔线
length: 15,  //设置属性length控制线长
lineStyle: &#123;  //设置属性lineStyle（详见lineStyle）控制线条样式
color: 'auto'
&#125;
&#125;,
pointer: &#123; width: 4 &#125;,  //设置油表的指针宽度为4
title: &#123; show: false &#125;,
detail: &#123; show: false &#125;,
data: [&#123; value: 0.5, name: 'gas' &#125;]
&#125;,
&#123;   //设置数据系列之4：水表
name: '水表', type: 'gauge',
center: ['77%', '50%'],  //设置水表仪表盘中心点的位置，默认全局居中
radius: '25%',  //设置水表仪表盘的大小
min: 0,  //设置水表的最小值
max: 2,  //设置水表的最大值
startAngle: 315, endAngle: 225,
splitNumber: 2,  //设置分隔数目
axisLine: &#123;  //设置坐标轴线
lineStyle: &#123;  //设置属性lineStyle控制线条样式
width: 8  //设置线条宽度
&#125;
&#125;,
axisTick: &#123; show: false &#125;,  //设置不显示坐标轴小标记
axisLabel: &#123;
formatter: function (v) &#123;
switch (v + '') &#123;
case '0': return 'H';
case '1': return '水表';
case '2': return 'C';
&#125;
&#125;
&#125;,
splitLine: &#123;  //设置分隔线
length: 15,  //设置属性length控制线长
lineStyle: &#123;  //设置属性lineStyle（详见lineStyle）控制线条样式
color: 'auto'
&#125;
&#125;,
pointer: &#123; width: 2 &#125;,  //设置水表的指针宽度为2
title: &#123; show: false &#125;,
detail: &#123; show: false &#125;,
data: [&#123; value: 0.5, name: 'gas' &#125;]
&#125;
]
&#125;;
setInterval(function () &#123;
option.series[0].data[0].value = (Math.random() * 100).toFixed(2) - 0;
option.series[1].data[0].value = (Math.random() * 7).toFixed(2) - 0;
option.series[2].data[0].value = (Math.random() * 2).toFixed(2) - 0;
option.series[3].data[0].value = (Math.random() * 2).toFixed(2) - 0;
myChart.setOption(option, true);
&#125;, 2000);  //每间2秒重新渲染一次，以实现动态效果
</script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            