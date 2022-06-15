
---
title: 'Apache ECharts 5.3.3 发布，交互式图表可视化库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2568'
author: 开源中国
comments: false
date: Wed, 15 Jun 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2568'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0"><span style="color:#333333">Apache ECharts 是一个使用 JavaScript 实现的开源可视化库，可以流畅的运行在 PC 和移动设备上，兼容当前绝大部分浏览器（IE8/9/10/11，Chrome，Firefox，Safari 等），底层依赖矢量图形库 ZRender，提供直观，交互丰富，可高度个性化定制的数据可视化图表。</span></p> 
<p style="margin-left:0"><span style="color:#333333">Apache ECharts 5.3.3 现已发布，具体更新内容如下：</span></p> 
<ul> 
 <li>[Feature] [bar] 添加新的 stacking strategies。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F17086" target="_blank">#17086</a></li> 
 <li>[Feature] [tree] tree focus 支持<code>relative</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F17009" target="_blank">#17009</a></li> 
 <li>[Feature] [visualMap]<code>selectedMode</code>支持<code>boolean</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F16972" target="_blank">#16972</a></li> 
 <li>[Fix] [line] 修复从折线图切换到阶梯折线图时，在<code>notMerge: true</code>情况下多边形不更新的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F16772" target="_blank">#16772</a></li> 
 <li>[Fix] [tree] 修复 edgeShape 为 polyline 时意外展开的子节点。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F16548" target="_blank">#16548</a></li> 
 <li>[Fix] [graph] 修复<code>autoCurveness</code>类型。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F16897" target="_blank">#16897</a></li> 
 <li>[Fix] [radar] 修复分支合并带来的回归 bug。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F16764" target="_blank">#16764</a></li> 
 <li>[Fix] [geo] 修复 linesGL 系列不渲染的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F17150" target="_blank">#17150</a></li> 
 <li>[Fix] [pictorialBar] 改进 PictorialBarSeriesOption 类型定义。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F17155" target="_blank">#17155</a></li> 
 <li>[Fix] [tooltip] 修复 triggerOn 设置为 click 时内容随轴范围变化的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F16939" target="_blank">#16939</a></li> 
 <li>[Fix] [dataZoom] 修复<code>borderColor</code>在某些捆绑环境中可能不起作用。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F16854" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLing310" target="_blank">16854</a></li> 
 <li>[Fix] [markLine] 修复 markLine 标签显示错误的 tooltip content 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F16971" target="_blank">#16971</a></li> 
 <li>[Fix] [markArea] 修复 markArea 可能被意外过滤的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F16861" target="_blank">#16861</a></li> 
 <li>[Fix] [axis] 修复<code>&#123;yy&#125;</code>没有被填充到 2 digits。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F17064" target="_blank">#17064</a></li> 
 <li>[Fix] [axis] 修复了应该将一年分成 4 个季度而不是 3 个季度的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F17073" target="_blank">#17073</a></li> 
 <li>[Fix] [axis]] 修复自定义系列不适用于 singleAxis 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F16850" target="_blank">#16850</a></li> 
 <li>[Fix] [graphic] 修复某些选项可能在更新时被意外重置。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F17007" target="_blank">#17007</a></li> 
 <li>[Fix] [decal] 修复设置<code>legend.itemStyle.decal</code>为<code>'none'</code>后图案不变化。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F16922" target="_blank">#16922</a></li> 
 <li>[Fix] [radialGradient] 为 radial gradient 添加安全防护。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fecomfe%2Fzrender%2Fissues%2F898" target="_blank">#898</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fecomfe%2Fzrender%2Fissues%2F919" target="_blank">#919</a></li> 
 <li>[Fix] [types] 修复<code>DataStore</code>中的拼写错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Fissues%2F16824" target="_blank">#16824</a> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Freleases%2Ftag%2F5.3.3" target="_blank">https://github.com/apache/echarts/releases/tag/5.3.3</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            