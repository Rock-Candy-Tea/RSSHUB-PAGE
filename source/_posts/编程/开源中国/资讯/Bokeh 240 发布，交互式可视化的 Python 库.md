
---
title: 'Bokeh 2.4.0 发布，交互式可视化的 Python 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3937'
author: 开源中国
comments: false
date: Sat, 18 Sep 2021 06:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3937'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>Bokeh 是一个用于现代 Web 浏览器的交互式可视化库。它提供了优雅、简洁的多功能图形结构，并在大型或流式数据集提供了高性能的交互性。Bokeh 可以帮助任何想要快速轻松地制作交互式绘图、仪表板和数据应用程序的人。</p> 
 <p>Bokeh 2.4.0 发布，该版本的更新内容包括：</p> 
 <ul> 
  <li>文档的修复和改进 
   <ul> 
    <li>更新了贡献者指南 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11513" target="_blank">#11513</a></li> 
    <li>添加<code>pre-commit</code> hooks <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11442" target="_blank">#11442</a></li> 
    <li>参考指南改进 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F9961" target="_blank">#9961</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11445" target="_blank">#11445</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11563" target="_blank">#11563</a></li> 
    <li>添加了 Sampledata 和 gallery 示例数据 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F9329" target="_blank">#9329</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11489" target="_blank">#11489</a></li> 
   </ul> </li> 
  <li>WebGL 修复和改进 
   <ul> 
    <li>使用 ReGL 重写了 WebGL 后端 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F10861" target="_blank">#10861</a></li> 
    <li>修复虚线样式（Dashed line） <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F10876" target="_blank">#10876</a></li> 
    <li>支持填充图案 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11159" target="_blank">#11159</a></li> 
    <li>实现了所有标记类型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11098" target="_blank">#11098</a></li> 
   </ul> </li> 
  <li>SVG 修正和改进 
   <ul> 
    <li>修复了虚线的偏移和填充图案 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11058" target="_blank">#11058</a></li> 
    <li>添加了缺少的椭圆字形 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11404" target="_blank">#11404</a></li> 
    <li>剪切区域问题已修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11551" target="_blank">#11551</a></li> 
   </ul> </li> 
  <li>其他修正和改进 
   <ul> 
    <li>标签现在可以是多行的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F7317" target="_blank">#7317</a></li> 
    <li>可以隐藏单个图例项和表格列 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F9261" target="_blank">#9261</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11423" target="_blank">#11423</a></li> 
    <li>标签面板可以被设置为禁用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F10898" target="_blank">#10898</a></li> 
    <li>工具栏按钮遵循标签排序 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11266" target="_blank">#11266</a></li> 
    <li>单选按钮组支持垂直方向 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11374" target="_blank">#11374</a></li> 
    <li>新增合并的 RangesUpdate 事件 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11095" target="_blank">#11095</a></li> 
    <li>来自 json_items 的输出包括 Bokeh 版本 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbokeh%2Fbokeh%2Fissues%2F11146" target="_blank">#11146</a></li> 
   </ul> </li> 
 </ul> 
 <p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.bokeh.org%2Fen%2Flatest%2Fdocs%2Freleases.html" target="_blank">https://docs.bokeh.org/en/latest/docs/releases.html</a></p> 
</div>
                                        </div>
                                      
</div>
            