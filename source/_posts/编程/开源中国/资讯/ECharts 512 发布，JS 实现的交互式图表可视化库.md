
---
title: 'ECharts 5.1.2 发布，JS 实现的交互式图表可视化库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6323'
author: 开源中国
comments: false
date: Fri, 11 Jun 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6323'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ECharts 是一个使用 JavaScript 实现的开源可视化库，可以流畅的运行在 PC 和移动设备上，兼容当前绝大部分浏览器（IE8/9/10/11，Chrome，Firefox，Safari等），底层依赖矢量图形库 ZRender，提供直观，交互丰富，可高度个性化定制的数据可视化图表。</p> 
<p>ECharts 5.1.2 正式发布，本次更新内容如下：</p> 
<ul> 
 <li>[Feature] [geo/map] 在变换和 svg 解析器中支持倾斜 skew；</li> 
 <li>[Feature] [tree] 在工具提示回调的参数中添加 treeAncestors 属性；</li> 
 <li>[Feature] [i18n] 增加斯洛文尼亚语翻译</li> 
 <li>[Fix] [canvas] 当 dirty rect 被启用时，修复额外的 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fctx.save%2F" target="_blank">ctx.save</a> 调用；</li> 
 <li>[Fix] [path] 在优化 line segments 时，修复小的子路径可能被忽略；</li> 
 <li>[Fix] [tooltip] 当组件 tooltip.formatter 没有指定时，使用特定的默认 formatter，而不是使用全局 tooltip.formatter 作为默认；</li> 
 <li>[Fix] [resize] 修复了在使用 lazyUpdate: true 调用 setOption 之后在调用 resize 时会抛出错误的问题；</li> 
 <li>[Fix] [treemap] 使用差异数据运行 setOption 两次时出错；</li> 
 <li>[Fix] [tree] 使用差异数据运行 setOption 两次时出错；</li> 
 <li>[Fix] [option] 在合并主题之前检查缺少的组件；</li> 
 <li>[Fix] [text] 修复渐变文字背景导致渲染错误的问题；</li> 
 <li>[Fix] [clip] 当 clip 设置为 false 时，线形图会出现错误；</li> 
 <li>[Fix] [legend] 移除意外的语法以确保更好的兼容性；</li> 
 <li>[Fix] [dataZoom] startValue 和 endValue 的类型修复；</li> 
 <li>[Fix] [label] 确保临时符号的标签在线条和区域多边形的前面；</li> 
 <li>[Fix] [dataZoom] 当 toolbox.feature.dataZoom 未声明时，不应该有 dataZoom 过滤；</li> 
 <li>[Fix] [line] 避免 linearMap util 中的无限值；</li> 
 <li>[Fix] [timeline] 当播放到结束时触发 <code>timelineplaychange</code> 事件；</li> 
 <li>[Fix] [custom] 修复自定义系列中的渐进式渲染；</li> 
 <li>[Fix] [label] 修复标签不在顶部的错误；</li> 
 <li>[Fix] [toolbox] 自定义工具箱按钮的 show 选项不起作用；</li> 
 <li>[Fix] [type] 将 LineEndLabelOption.valueAnimation 更改为可选；</li> 
 <li>[Fix] [type] 导出 cbs 及其参数类型；</li> 
 <li>[Fix] [type] 修复位置回调的返回类型；</li> 
 <li>[Fix] [type] 从 PatternObject 中删除非必须的属性，并修正一些类型问题；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fecharts%2Freleases%2Ftag%2F5.1.2" target="_blank">https://github.com/apache/echarts/releases/tag/5.1.2</a></p>
                                        </div>
                                      
</div>
            