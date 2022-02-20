
---
title: 'go-charts 1.0 版本发布：支持更多的图表样例及主题'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.shields.io/badge/license-MIT-blue.svg'
author: 开源中国
comments: false
date: Sun, 20 Feb 2022 17:58:00 GMT
thumbnail: 'https://img.shields.io/badge/license-MIT-blue.svg'
---

<div>   
<div class="content">
                                                                                            <h1>go-charts</h1> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvicanso%2Fgo-charts%2Fblob%2Fmaster%2FLICENSE" target="_blank"><img alt="license" src="https://img.shields.io/badge/license-MIT-blue.svg" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvicanso%2Fgo-charts%2Factions" target="_blank"><img alt="Build Status" src="https://github.com/vicanso/go-charts/workflows/Test/badge.svg" referrerpolicy="no-referrer"></a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvicanso%2Fgo-charts" target="_blank">go-charts</a>基于go-chart，提供更简单方便的形式生成数据图表，支持<code>svg</code>与<code>png</code>两种方式的输出，支持三种主题<code>light</code>, <code>dark</code>以及<code>grafana</code>。</p> 
<p><code>Apache ECharts</code>在前端开发中得到众多开发者的认可，因此<code>go-charts</code>提供了兼容<code>Apache ECharts</code>的配置参数，简单快捷的生成相似的图表(<code>svg</code>或<code>png</code>)，方便插入至Email或分享使用。下面为常用的图表截图(主题为light与grafana)：</p> 
<p><img alt height="1907" src="https://oscimg.oschina.net/oscnet/up-f825d75bceddd6e3065f1f87b7e2a6547f9.png" width="810" referrerpolicy="no-referrer"></p> 
<h2>支持图表类型</h2> 
<p>暂仅支持三种的图表类型：<code>line</code>, <code>bar</code> 以及 <code>pie</code></p> 
<h2>示例</h2> 
<p>下面的示例为<code>go-charts</code>两种方式的参数配置：golang的参数配置、echarts的JSON配置，输出相同的折线图。 更多的示例参考：<code>./examples/</code>目录</p> 
<pre><code class="language-go">package main

import (
    "os"
    "path/filepath"

    charts "github.com/vicanso/go-charts"
)

func writeFile(file string, buf []byte) error &#123;
    tmpPath := "./tmp"
    err := os.MkdirAll(tmpPath, 0700)
    if err != nil &#123;
        return err
    &#125;

    file = filepath.Join(tmpPath, file)
    err = os.WriteFile(file, buf, 0600)
    if err != nil &#123;
        return err
    &#125;
    return nil
&#125;

func chartsRender() ([]byte, error) &#123;
    d, err := charts.Render(charts.ChartOption&#123;
        Type: charts.ChartOutputPNG,
        Title: charts.TitleOption&#123;
            Text: "Line",
        &#125;,
        XAxis: charts.NewXAxisOption([]string&#123;
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun",
        &#125;),
        SeriesList: charts.SeriesList&#123;
            charts.NewSeriesFromValues([]float64&#123;
                150,
                230,
                224,
                218,
                135,
                147,
                260,
            &#125;),
        &#125;,
    &#125;)
    if err != nil &#123;
        return nil, err
    &#125;
    return d.Bytes()
&#125;

func echartsRender() ([]byte, error) &#123;
    return charts.RenderEChartsToPNG(`&#123;
        "title": &#123;
            "text": "Line"
        &#125;,
        "xAxis": &#123;
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        &#125;,
        "series": [
            &#123;
                "data": [150, 230, 224, 218, 135, 147, 260]
            &#125;
        ]
    &#125;`)
&#125;

type Render func() ([]byte, error)

func main() &#123;
    m := map[string]Render&#123;
        "charts-line.png":  chartsRender,
        "echarts-line.png": echartsRender,
    &#125;
    for name, fn := range m &#123;
        buf, err := fn()
        if err != nil &#123;
            panic(err)
        &#125;
        err = writeFile(name, buf)
        if err != nil &#123;
            panic(err)
        &#125;
    &#125;
&#125;
</code></pre> 
<h2>ECharts参数说明</h2> 
<p>名称有[]的参数非echarts的原有参数，为<code>go-charts</code>的新增参数，可根据实际使用场景添加。</p> 
<ul> 
 <li><code>[type]</code> 画布类型，支持<code>svg</code>与<code>png</code>，默认为<code>svg</code></li> 
 <li><code>[theme]</code> 颜色主题，支持<code>dark</code>、<code>light</code>以及<code>grafana</code>模式，默认为<code>light</code></li> 
 <li><code>[fontFamily]</code> 字体，全局的字体设置</li> 
 <li><code>[padding]</code> 图表的内边距，单位px。支持以下几种模式的设置 
  <ul> 
   <li><code>padding: 5</code> 设置内边距为5</li> 
   <li><code>padding: [5, 10]</code> 设置上下的内边距为 5，左右的内边距为 10</li> 
   <li><code>padding:[5, 10, 5, 10]</code> 分别设置<code>上右下左</code>边距</li> 
  </ul> </li> 
 <li><code>[box]</code> 图表的区域，以&#123;"left": Int, "right": Int, "top": Int, "bottom": Int&#125;的形式配置</li> 
 <li><code>[width]</code> 画布宽度，默认为600</li> 
 <li><code>[height]</code> 画布高度，默认为400</li> 
 <li><code>title</code> 图表标题，包括标题内容、高度、颜色等 
  <ul> 
   <li><code>title.text</code> 标题文本，支持以<code>\\n</code>的形式换行</li> 
   <li><code>title.subtext</code> 副标题文本，支持以<code>\\n</code>的形式换行</li> 
   <li><code>title.left</code> 标题与容器左侧的距离，可设置为<code>left</code>, <code>right</code>, <code>center</code>, <code>20%</code> 以及 <code>20</code> 这样的具体数值</li> 
   <li><code>title.top</code> 标题与容器顶部的距离，暂仅支持具体数值，如<code>20</code></li> 
   <li><code>title.textStyle.color</code> 标题文字颜色</li> 
   <li><code>title.textStyle.fontSize</code> 标题文字字体大小</li> 
   <li><code>title.textStyle.fontFamily</code> 标题文字的字体系列，需要注意此配置是会影响整个图表的字体</li> 
  </ul> </li> 
 <li><code>xAxis</code> 直角坐标系grid中的x轴，由于go-charts仅支持单一个x轴，因此若参数为数组多个x轴，只使用第一个配置 
  <ul> 
   <li><code>xAxis.boundaryGap</code> 坐标轴两边留白策略，仅支持三种设置方式<code>null</code>, <code>true</code>或者<code>false</code>。<code>null</code>或<code>true</code>时则数据点展示在两个刻度中间</li> 
   <li><code>xAxis.splitNumber</code> 坐标轴的分割段数，需要注意的是这个分割段数只是个预估值，最后实际显示的段数会在这个基础上根据分割后坐标轴刻度显示的易读程度作调整</li> 
   <li><code>xAxis.data</code> x轴的展示文案，暂只支持字符串数组，如["Mon", "Tue"]，其数量需要与展示点一致</li> 
  </ul> </li> 
 <li><code>yAxis</code> 直角坐标系grid中的y轴，最多支持两个y轴 
  <ul> 
   <li><code>yAxis.min</code> 坐标轴刻度最小值，若不设置则自动计算</li> 
   <li><code>yAxis.max</code> 坐标轴刻度最大值，若不设置则自动计算</li> 
   <li><code>yAxis.axisLabel.formatter</code> 刻度标签的内容格式器，如<code>"formatter": "&#123;value&#125; kg"</code></li> 
   <li><code>yAxis.axisLine.lineStyle.color</code> 坐标轴颜色</li> 
  </ul> </li> 
 <li><code>legend</code> 图表中不同系列的标记 
  <ul> 
   <li><code>legend.show</code> 图例是否显示，如果不需要展示需要设置为<code>false</code></li> 
   <li><code>legend.data</code> 图例的数据数组，为字符串数组，如["Email", "Video Ads"]</li> 
   <li><code>legend.align</code> 图例标记和文本的对齐，可设置为<code>left</code>或者<code>right</code>，默认为标记靠左<code>left</code></li> 
   <li><code>legend.padding</code> legend的padding，配置方式与图表的<code>padding</code>一致</li> 
   <li><code>legend.left</code> legend离容器左侧的距离，其值可以为具体的像素值(20)或百分比(20%)、<code>left</code>或者<code>right</code></li> 
   <li><code>legend.top</code> legend离容器顶部的距离，暂仅支持数值形式</li> 
  </ul> </li> 
 <li><code>series</code> 图表的数据项列表 
  <ul> 
   <li><code>series.name</code> 图表的名称，与<code>legend.data</code>对应，两者只只设置其一</li> 
   <li><code>series.type</code> 图表的展示类型，暂支持<code>line</code>, <code>bar</code>以及<code>pie</code>，需要注意<code>pie</code>只能单独使用</li> 
   <li><code>series.radius</code> 饼图的半径值，如<code>50%</code>，默认为<code>40%</code></li> 
   <li><code>series.yAxisIndex</code> 该数据项使用的y轴，默认为0，对yAxis的配置对应</li> 
   <li><code>series.label.show</code> 是否显示文本标签(默认为对应的值)</li> 
   <li><code>series.label.distance</code> 距离图形元素的距离</li> 
   <li><code>series.label.color</code> 文本标签的颜色</li> 
   <li><code>series.itemStyle.color</code> 该数据项展示时使用的颜色</li> 
   <li><code>series.markPoint</code> 图表的标注配置</li> 
   <li><code>series.markPoint.symbolSize</code> 标注的大小，默认为30</li> 
   <li><code>series.markPoint.data</code> 标注类型，仅支持数组形式，其类型只支持<code>max</code>与<code>min</code>，如：`[&#123;"type": "max"&#125;, &#123;"type": "min"&#125;]</li> 
   <li><code>series.markLine</code> 图表的标线配置</li> 
   <li><code>series.markPoint.data</code> 标线类型，仅支持数组形式，其类型只支持<code>max</code>、<code>min</code>以及<code>average</code>，如：`[&#123;"type": "max"&#125;, &#123;"type": "min"&#125;, &#123;"type": "average"&#125;]</li> 
   <li><code>series.data</code> 数据项对应的数据数组，支持以下形式的数据： 
    <ul> 
     <li><code>数值</code> 常用形式，数组数据为浮点数组，如[1.1, 2,3, 5.2]</li> 
     <li><code>结构体</code> pie图表或bar图表中指定样式使用，如[&#123;"value": 1048, "name": "Search Engine"&#125;,&#123;"value": 735,"name": "Direct"&#125;]</li> 
    </ul> </li> 
  </ul> </li> 
 <li><code>[children]</code> 嵌套的子图表参数列表，图表支持嵌套的形式=</li> 
</ul> 
<h2>性能</h2> 
<p>简单的图表生成PNG在20ms左右，而SVG的性能则更快，性能上比起使用<code>chrome headless</code>加载<code>echarts</code>图表展示页面再截图生成的方式大幅度提升，满足简单的图表生成需求。</p> 
<pre><code class="language-bash">BenchmarkMultiChartPNGRender-8                78          15216336 ns/op         2298308 B/op       1148 allocs/op
BenchmarkMultiChartSVGRender-8               367           3356325 ns/op        20597282 B/op       3088 allocs/op
</code></pre> 
<h2>中文字符</h2> 
<p>默认使用的字符为<code>roboto</code>为英文字体库，因此如果需要显示中文字符需要增加中文字体库，<code>InstallFont</code>函数可添加对应的字体库，成功添加之后则指定<code>title.textStyle.fontFamily</code>即可。 在浏览器中使用<code>svg</code>时，如果指定的<code>fontFamily</code>不支持中文字符，展示的中文并不会乱码，但是会导致在计算字符宽度等错误。</p>
                                        </div>
                                      
</div>
            