
---
title: '项目echarts图表问题点总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/445fdd5d9e9248b7addc703affed4c06~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 00:56:15 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/445fdd5d9e9248b7addc703affed4c06~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在UI提供的效果图中，总有些平常开发遇到很少的图表展示情况。本篇文章就是总结了几个实际开发中遇到的两个地方来说一下。</p>
<h2 data-id="heading-0">饼图的展示问题</h2>
<p>当 radius 设置为一个值时，在 echarts v4 版本和 v5 版本的不一样的展示问题。</p>
<pre><code class="copyable">&#123;
    type: 'pie',
    radius: ['55%'],
    center: ['50%', '50%'],
    data: [
        &#123;
            name: "1",
            value: "3720"
        &#125;,
        &#123;
            name: "2",
            value: "2920"
        &#125;,
        &#123;
            name: "3",
            value: "2200"
        &#125;,
        &#123;
            name: "4",
            value: "1420"
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面是饼图设置中 series 的配置，radius 是设置饼图的半径。</p>
<p>这里数组的第一项是内半径，第二项是外半径，而有时我们实现一些非数据展示的圆环内边线和外边线之类的，就可能数组中只设置一个值，在这个情况下，我们会发现 v4 和 v5 版本会有不同的展示问题，在 v4 中 tooltip 是不显示的，这个是我们要的，因为特殊线只是展示效果，但在 v5 中就会有 tooltip 的提示。</p>
<p>这个问题就让我们探究一下到底是什么原因导致的。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/445fdd5d9e9248b7addc703affed4c06~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个图就是在 v4 版本下面的效果，相当于 radius 中只设置了外半径，内半径不存在，这个圆环的环宽是没有的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0550484374904acb8724ebce0e760497~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个则是v5版本下面的效果，radius 设置的值是为外半径，内半径则被认为是 0，此时环宽就是这个外半径，展示出的效果就是一个圆。</p>
<p>现在，我们应该就清楚为什么两个版本的 tooltip 一个显示，一个不显示的问题所在了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a289b26729045c0976beac9b8b3a541~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">3d 柱状图</h2>
<h3 data-id="heading-2">v3 版本实现</h3>
<p>因为 UI 提供了一个 3d 柱状图的效果图，所以就去查了一下 echarts 里面有什么方法可以实现。</p>
<p>在百度查找中，找到一个可以实现的 demo。</p>
<p>引入 echarts-bar3d 插件后，其他配置和平常柱状图没有区别，效果也算可以。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/988ac02575c7497db3c5a55b6fcf998f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">series: [
    &#123;
        type: 'bar3d',
        zlevel: 1,
        data: [400, 400, 400, 400, 400, 400, 400],
        itemStyle: &#123;
            normal: &#123;
                color: new echarts.graphic.LinearGradient(
                    0, 0, 0, 1,
                    [
                        &#123; offset: 0, color: '#17404d' &#125;,
                        &#123; offset: 1, color: '#051a2e' &#125;
                    ]
                ),
                opacity: 0.8
            &#125;
        &#125;
    &#125;,
    &#123;
        type: 'bar3d',
        zlevel: 2,
        barGap: '-100%',
        data: [300, 120, 175, 20, 230, 350, 400],
        itemStyle: &#123;
            normal: &#123;
                color: new echarts.graphic.LinearGradient(
                    0, 0, 0, 1,
                    [
                        &#123; offset: 0, color: '#ffcd98' &#125;,
                        &#123; offset: 1, color: '#e19709' &#125;
                    ]
                ),
                opacity: 0.8
            &#125;
        &#125;
    &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到和我们正常的 bar 图表配置没有区别，只是这个 y 轴的分隔线加上效果就不太一样了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a710a161a5424f8296a6cebce4ddc872~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以明显看到这个 3d 效果会让分隔线也有个 3d 效果，但是这个问题可以和 UI 商量，还是在接受范围内，可最后去使用，才发现，这个 echarts 版本也是完全不一样，这个是在 v3.7 版本中实现的，现在都已经到 v5 版本，现在的 3d 效果已经完全不是这个样子，在项目中也不可能再引入一个 v3 的版本。所以需要再去换个方向了。</p>
<h3 data-id="heading-3">gl 配置 3d 展示</h3>
<p>在 echarts 的 GL 配置中找到 bar3D，可以发现已经和原先柱状图的配置有一些差别了，先是坐标轴多出一个 z 轴，而且配置也都相应的变成 xAxis3D，yAxis3D 等，但基本上的配置都还是和原先无差，需要特别注意的就是 data 的数据是一个数组表示一个数据在 x，y，z 三个坐标轴下的位置。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d409764f916a4d6da9a77fa1e7f96369~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是实现效果还是和我们想要的差很多，这个完全 3d 的效果完全不是我们想要的，我们需要的只是一个伪 3d 的展示即可。</p>
<h3 data-id="heading-4">伪 3d 展示柱状图</h3>
<p>去 echarts 图表平台的示例库中可以找到一些参考。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03e63434c3ad43448b0b15f8992cfed9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>简单的就是这种，只需要 series 中再多加入两个 pictorialBar 配置。这个是<strong>象形柱图</strong>配置，就是设置各种具象图形元素（如图片、<a href="http://www.w3.org/TR/SVG/paths.html#PathData" target="_blank" rel="nofollow noopener noreferrer">SVG PathData</a> 等）的柱状图，这里我们只需要简单的图形类型即可，这个 demo 使用的就是 rect。</p>
<p>但是这个效果跟我们想要的也差的有点太多，所以又找到另外一种的图表设置。</p>
<h3 data-id="heading-5">自定义图表</h3>
<p>echarts还有一个自定义图表功能， <strong><a href="http://echarts.baidu.com/option.html#series-custom" target="_blank" rel="nofollow noopener noreferrer">custom series</a></strong> 自定义系列能让用户定制渲染逻辑。</p>
<p>我们可以用此方法写出一个伪3d柱状图图表。</p>
<pre><code class="copyable">const CubeLeft = echarts.graphic.extendShape(&#123;
    shape: &#123;
        x: 0,
        y: 0
    &#125;,
    buildPath: function(ctx, shape) &#123;
        const xAxisPoint = shape.xAxisPoint
        const c0 = [shape.x + 8, shape.y]
        const c1 = [shape.x - 8, shape.y]
        const c2 = [xAxisPoint[0] - 8, xAxisPoint[1]]
        const c3 = [xAxisPoint[0] + 8, xAxisPoint[1]]
        ctx.moveTo(c0[0], c0[1]).lineTo(c1[0], c1[1]).lineTo(c2[0], c2[1]).lineTo(c3[0], c3[1]).closePath()
    &#125;
&#125;)
const CubeRight = echarts.graphic.extendShape(&#123;
    shape: &#123;
        x: 0,
        y: 0
    &#125;,
    buildPath: function(ctx, shape) &#123;
        const xAxisPoint = shape.xAxisPoint
        const c1 = [shape.x + 8, shape.y]
        const c2 = [xAxisPoint[0] + 8, xAxisPoint[1]]
        const c3 = [xAxisPoint[0] + 13, xAxisPoint[1] - 3]
        const c4 = [shape.x + 13, shape.y - 3]
        ctx.moveTo(c1[0], c1[1]).lineTo(c2[0], c2[1]).lineTo(c3[0], c3[1]).lineTo(c4[0], c4[1]).closePath()
    &#125;
&#125;)
const CubeTop = echarts.graphic.extendShape(&#123;
    shape: &#123;
        x: 0,
        y: 0
    &#125;,
    buildPath: function(ctx, shape) &#123;
        const c1 = [shape.x - 8, shape.y]
        const c2 = [shape.x + 8, shape.y]
        const c3 = [shape.x + 13, shape.y - 3]
        const c4 = [shape.x - 3, shape.y - 3]
        ctx.moveTo(c1[0], c1[1]).lineTo(c2[0], c2[1]).lineTo(c3[0], c3[1]).lineTo(c4[0], c4[1]).closePath()
    &#125;
&#125;)
echarts.graphic.registerShape('CubeLeft', CubeLeft)
echarts.graphic.registerShape('CubeRight', CubeRight)
echarts.graphic.registerShape('CubeTop', CubeTop)
option = &#123;
    series: [&#123;
        type: 'custom',
        renderItem: (params, api) => &#123;
            // 对于 data 中的每个 dataItem，都会调用这个 renderItem 函数。
            // （但是注意，并不一定是按照 data 的顺序调用）
            const location = api.coord([api.value(0), api.value(1)])
            return &#123;
                type: 'group',
                children: [&#123;
                    type: 'CubeLeft',
                    shape: &#123;
                        api,
                        xValue: api.value(0),
                        yValue: api.value(1),
                        x: location[0],
                        y: location[1],
                        xAxisPoint: api.coord([api.value(0), 0])
                    &#125;,
                    style: &#123;
                        fill: new echarts.graphic.LinearGradient(0, 0, 0, 1, [&#123;
                                offset: 0,
                                color: '#02ffff'
                            &#125;,
                            &#123;
                                offset: 1,
                                color: '#069095'
                            &#125;
                        ])
                    &#125;
                &#125;, &#123;
                    type: 'CubeRight',
                    shape: &#123;
                        api,
                        xValue: api.value(0),
                        yValue: api.value(1),
                        x: location[0],
                        y: location[1],
                        xAxisPoint: api.coord([api.value(0), 0])
                    &#125;,
                    style: &#123;
                        fill: new echarts.graphic.LinearGradient(0, 0, 0, 1, [&#123;
                                offset: 0,
                                color: '#199d9d'
                            &#125;,
                            &#123;
                                offset: 1,
                                color: '#0b6c70'
                            &#125;
                        ])
                    &#125;
                &#125;, &#123;
                    type: 'CubeTop',
                    shape: &#123;
                        api,
                        xValue: api.value(0),
                        yValue: api.value(1),
                        x: location[0],
                        y: location[1],
                        xAxisPoint: api.coord([api.value(0), 0])
                    &#125;,
                    style: &#123;
                        fill: new echarts.graphic.LinearGradient(0, 0, 0, 1, [&#123;
                                offset: 0,
                                color: '#397b92'
                            &#125;,
                            &#123;
                                offset: 1,
                                color: '#55b6ce'
                            &#125;
                        ])
                    &#125;
                &#125;]
            &#125;
        &#125;,
        data: [2012, 1230, 3790, 2349, 1654]
    &#125;]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个实现明显复杂很多，相当于所有位置都是我们自己去定义。</p>
<p>可以看到我们这里是用了 type: 'group' ，这个 type 是有多种选择的。</p>
<p>group：group 是唯一的可以有子节点的容器。group 可以用来整体定位一组图形元素。</p>
<p>path：可使用 <a href="http://www.w3.org/TR/SVG/paths.html#PathData" target="_blank" rel="nofollow noopener noreferrer">SVG PathData</a> 做路径。 可以用来画图标，或者其他各种图形，因为可以很便捷得缩放以适应给定尺寸。</p>
<p>image：图形。</p>
<p>text：文本块。</p>
<p>rect：矩形。</p>
<p>circle：圆。</p>
<p>ring：圆环。</p>
<p>sector：扇形。</p>
<p>arc：圆弧。</p>
<p>polygon：多边形。</p>
<p>polyline：折线。</p>
<p>line：直线。</p>
<p>bezierCurve：二次或三次贝塞尔曲线。</p>
<p>我们可以用一个最简单的自定义图表来看一下这个 custom 实现：</p>
<pre><code class="copyable">// 单独一个矩形
&#123;
    type: 'rect',
    shape: &#123;
        x: x, y: y, width: width, height: height
    &#125;,
    style: api.style()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出结构还是比较简单的，类型，形状，样式这个三个配置就可以实现一个自定义图表。</p>
<pre><code class="copyable">// 一组图形元素
&#123;
    type: 'group',
    // 如果 diffChildrenByName 设为 true，则会使用 child.name 进行 diff，
    // 从而能有更好的过度动画，但是降低性能。缺省为 false。
    // diffChildrenByName: true,
    children: [&#123;
        type: 'circle',
        shape: &#123;
            cx: cx, cy: cy, r: r
        &#125;,
        style: api.style()
    &#125;, &#123;
        type: 'line',
        shape: &#123;
            x1: x1, y1: y1, x2: x2, y2: y2
        &#125;,
        style: api.style()
    &#125;]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>进而可以用多个简单的自定义图表来形成一组元素。</p>
<p>这个整体结构我们明白了，接下来就要看下用到 graphic 方法都是做什么的。</p>
<p>graphic：图形相关帮助方法。</p>
<p>官方 graphic 下的五种具体方法。</p>
<p>extendShape：创建一个新的 shape class。</p>
<p>registerShape：注册一个开发者定义的 shape class。</p>
<p>getShapeClass：得到一个 <a href="https://echarts.apache.org/zh/api.html#echarts.graphic.registerShape" target="_blank" rel="nofollow noopener noreferrer">注册</a> 好的 class。</p>
<p>clipPointsByRect：输入一组点，和一个矩形，返回被矩形截取过的点。</p>
<p>clipRectByRect：输入两个矩形，返回第二个矩形截取第一个矩形的结果。</p>
<p>我们这里就用到了 extendShape 和 registerShape，一个是去创建我们想要的图形，一个是引入我们创建的图形。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3625dd0169cc4f10944b8d50daaf3e92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到这个跟我们想要的 UI 就已经差不多了，接着去改样式就行了。</p>
<p>本篇文章到此结束，希望有帮助到看这篇文章的小伙伴。</p>
<p>浙江大华技术股份有限公司-软研-智慧城市产品研发部招聘高级前端！！！！！ 欢迎大家来聊，有意向可发送简历到 chen_<a href="mailto:zhen@dahuatech.com">zhen@dahuatech.com</a>，加入我们，可以一起进步，一起聚餐，一起旅游，让我们从世界村的小伙伴变成大华村的小伙伴。</p></div>  
</div>
            