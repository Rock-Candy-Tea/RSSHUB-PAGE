
---
title: 'DataGear 2.6.0 发布，数据可视化分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png'
author: 开源中国
comments: false
date: Wed, 07 Jul 2021 09:17:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">DataGear</a> 2.6.0 发布，修复严重BUG，ECharts升级至5.1.2版本，具体更新内容如下：</p> 
<ul> 
 <li>新增：看板JS对象新增serverDate函数，用于获取服务端当前日期；</li> 
 <li>新增：看板监听器新增updateChartError函数，图表监听器新增updateError函数，用于自定义图表更新数据出错处理逻辑；</li> 
 <li>新增：表格图表新增carousel.hideVerticalScrollbar配置项，用于控制轮播时是否隐藏纵向滚动条；</li> 
 <li>修复：修复定时刷新图表的dg-chart-link和refreshData()不起作用的BUG；</li> 
 <li>修复：修复隐藏轮播表格元素会导致页面卡死的BUG；</li> 
 <li>修复：修复定时刷新图表在更新数据出错后没有继续执行定时刷新的BUG；</li> 
 <li>修复：修复点击数据源列表条目打开数据源出错后无法再次重试的BUG；</li> 
 <li>改进：仪表盘图表支持添加多个数值列；</li> 
 <li>改进：图表元素上的dg-chart-listener改为继承<body>上的设置而非覆盖；</li> 
 <li>改进：调整系统查询框布局，将查询条件都聚合至搜索框内；</li> 
 <li>改进：看板里动态生成的内置CSS插入在用户定义CSS之前，确保用户CSS有更高优先级；</li> 
 <li>改进：系统配置项directory.root改为DataGearWorkspace，便于通过环境变量配置工作目录；</li> 
 <li>其他：ECharts版本由4.9.0升级至5.1.2；</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">DataGear</a><em> </em><span style="background-color:#ffffff; color:#333333">是一款数据可视化分析平台，使用Java语言开发，采用浏览器/服务器架构，支持SQL、CSV、Excel、HTTP接口、JSON等多种数据源，主要功能包括数据管理、SQL工作台、数据导入/导出、数据集管理、图表管理、看板管理等。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">官网地址：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">http://www.datagear.tech</a></p> 
<p>源码地址：</p> 
<p>Gitee：<a href="https://gitee.com/datagear/datagear" target="_blank">https://gitee.com/datagear/datagear</a></p> 
<p>Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdatageartech%2Fdatagear" target="_blank">https://github.com/datageartech/datagear</a></p> 
<p>大屏模板地址：<a href="https://gitee.com/datagear/DataGearDashboardTemplate" target="_blank">https://gitee.com/datagear/DataGearDashboardTemplate</a></p> 
<p>系统部分功能效果图：</p> 
<p><a href="https://my.oschina.net/u/4035217/blog/3168893" target="_blank">制作看板</a></p> 
<p><img alt height="630" src="https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png" width="1352" referrerpolicy="no-referrer"></p> 
<p><img alt height="632" src="https://oscimg.oschina.net/oscnet/up-ab30dacd8a3c860f4763518896b1c2ff30d.png" width="1360" referrerpolicy="no-referrer"></p> 
<p><a href="https://my.oschina.net/u/4035217/blog/4529151" target="_blank">数据钻取</a></p> 
<p><img alt height="630" src="https://oscimg.oschina.net/oscnet/up-bf1c73948e5912b4411d41bf6a629155efa.gif" width="1352" referrerpolicy="no-referrer"></p> 
<p><a href="https://my.oschina.net/u/4035217/blog/4443596" target="_blank">地图联动</a></p> 
<p><img alt height="630" src="https://oscimg.oschina.net/oscnet/up-a790a37949b40c068fe78819a480666bd4e.gif" width="1352" referrerpolicy="no-referrer"></p> 
<p><a href="https://my.oschina.net/u/4035217/blog/4458378" target="_blank">看板表单</a></p> 
<p><img alt height="630" src="https://oscimg.oschina.net/oscnet/up-58bd41cca88a11ea834ba35d3b55f0af375.gif" width="1352" referrerpolicy="no-referrer"></p> 
<p><a href="https://my.oschina.net/u/4035217/blog/4670538" target="_blank">表格轮播</a></p> 
<p><img alt height="630" src="https://oscimg.oschina.net/oscnet/up-203072677d00faa4aee066ebf069188a667.gif" width="1352" referrerpolicy="no-referrer"></p> 
<p><a href="https://my.oschina.net/u/4035217/blog/4504599" target="_blank">时序图表</a></p> 
<p><img alt height="630" src="https://oscimg.oschina.net/oscnet/up-e584867aad88a046d1a7003b0231c61587d.gif" width="1352" referrerpolicy="no-referrer"></p> 
<p><a href="https://my.oschina.net/u/4035217/blog/4666146" target="_blank">异步加载</a></p> 
<p><img alt height="630" src="https://oscimg.oschina.net/oscnet/up-1a7c11e1536023dbb1f279eeb66fcbafdf4.gif" width="1352" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"> </p>
                                        </div>
                                      
</div>
            