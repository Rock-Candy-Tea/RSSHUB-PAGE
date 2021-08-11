
---
title: 'DataGear 2.7.0 发布，数据可视化分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png'
author: 开源中国
comments: false
date: Wed, 11 Aug 2021 00:59:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">DataGear</a> 2.7.0 发布，新增箱形图内置图表插件，改进图表JS对象API，具体更新内容如下：</p> 
<ul> 
 <li>新增：新增箱形图内置图表插件；</li> 
 <li>新增：新增数据集、图表、看板的复制功能；</li> 
 <li>新增：看板编辑页面新增看板和图表JS对象函数自动补全功能；</li> 
 <li>新增：图表JS对象新增inflateRenderOptions、inflateUpdateOptions、renderOptions函数，弃用optionsUpdate函数；</li> 
 <li>新增：图表JS对象新增internal函数，替换已弃用的echartsInstance函数；</li> 
 <li>新增：图表JS对象新增loadMap函数，用于为加载通用图表地图提供支持；</li> 
 <li>新增：图表JS对象新增resultValueObjects、resultDatasFirst函数；</li> 
 <li>新增：图表JS对象新增dataSetParamValueFirst、dataSetParamValuesFirst函数；</li> 
 <li>修复：修复在图表监听器里调用另一图表的refreshData函数有时不起作用的BUG；</li> 
 <li>修复：修复看板、图表展示地址末尾不带'/'会导致网页未找到的BUG；</li> 
 <li>修复：修复横向柱状图的配置项中xAxis和yAxis配置效果颠倒的BUG；</li> 
 <li>修复：修复内置图表对于某些series配置项不起作用的BUG；</li> 
 <li>修复：修复自定义图表设置异步渲染、异步更新无效的BUG；</li> 
 <li>修复：修复K线图未显示坐标轴刻度标签的BUG；</li> 
 <li>改进：弃用看板JS对象的isWaitForRender、isWaitForUpdate函数，它们不应作为开放API；</li> 
 <li>改进：图表元素的地图配置dg-chart-map、chart.echartsLoadMap函数支持SVG格式的地图；</li> 
 <li>改进：图表JS对象的dataSetParamValuesFirst、dataSetParamValues函数支持设置数组类型的参数值；</li> 
 <li>改进：简化数据集、图表、看板访问地址，移除"/analysis"地址前缀；</li> 
 <li>改进：完善各内置图表组件对于日期类数据的坐标轴类型支持；</li> 
 <li>改进：SQL、CSV、JSON数据集添加防注入和自动转义参数值支持；</li> 
 <li>改进：看板展示页面标题中的"DataGear"标识由前缀改为后缀，且默认显示看板名称；</li> 
 <li>改进：图表编辑页面支持悬浮提示选中图表类型的描述信息；</li> 
 <li>改进：图表插件临时目录改为应用配置的临时目录，而非操作系统临时目录；</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">DataGear</a>是一款数据可视化分析平台，使用Java语言开发，采用浏览器/服务器架构，支持SQL、CSV、Excel、HTTP接口、JSON等多种数据源，主要功能包括数据管理、SQL工作台、数据导入/导出、数据集管理、图表管理、看板管理等。</p> 
<p>官网地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">http://www.datagear.tech</a></p> 
<p>源码地址：</p> 
<p>Gitee：<a href="https://gitee.com/datagear/datagear">https://gitee.com/datagear/datagear</a></p> 
<p>Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdatageartech%2Fdatagear" target="_blank">https://github.com/datageartech/datagear</a></p> 
<p>大屏模板地址：<a href="https://gitee.com/datagear/DataGearDashboardTemplate">https://gitee.com/datagear/DataGearDashboardTemplate</a></p> 
<p>系统部分功能效果图：</p> 
<p><a href="https://my.oschina.net/u/4035217/blog/3168893">制作看板</a></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-ab30dacd8a3c860f4763518896b1c2ff30d.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://my.oschina.net/u/4035217/blog/4529151">数据钻取</a></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-bf1c73948e5912b4411d41bf6a629155efa.gif" referrerpolicy="no-referrer"></p> 
<p><a href="https://my.oschina.net/u/4035217/blog/4443596">地图联动</a></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a790a37949b40c068fe78819a480666bd4e.gif" referrerpolicy="no-referrer"></p> 
<p><a href="https://my.oschina.net/u/4035217/blog/4458378">看板表单</a></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-58bd41cca88a11ea834ba35d3b55f0af375.gif" referrerpolicy="no-referrer"></p> 
<p><a href="https://my.oschina.net/u/4035217/blog/4670538">表格轮播</a></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-203072677d00faa4aee066ebf069188a667.gif" referrerpolicy="no-referrer"></p> 
<p><a href="https://my.oschina.net/u/4035217/blog/4504599">时序图表</a></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e584867aad88a046d1a7003b0231c61587d.gif" referrerpolicy="no-referrer"></p> 
<p><a href="https://my.oschina.net/u/4035217/blog/4666146">异步加载</a></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1a7c11e1536023dbb1f279eeb66fcbafdf4.gif" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            