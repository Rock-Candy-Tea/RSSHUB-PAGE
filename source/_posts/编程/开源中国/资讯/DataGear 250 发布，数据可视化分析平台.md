
---
title: 'DataGear 2.5.0 发布，数据可视化分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png'
author: 开源中国
comments: false
date: Wed, 09 Jun 2021 09:09:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">DataGear</a> 2.5.0 发布，图表支持自定义数据格式，具体更新内容如下：</p> 
<ul> 
 <li>新增：图表编辑页面新增自定义日期类数据格式的功能；</li> 
 <li>新增：数据集编辑页面新增自定义数据源格式的功能；</li> 
 <li>新增：看板JS对象新增resultDataFormat函数，用于获取/设置看板级的结果数据格式；</li> 
 <li>新增：图表JS对象新增resultDataFormat函数，用于获取/设置图表级的结果数据格式；</li> 
 <li>新增：图表JS对象新增updateResults函数、替换已弃用的getUpdateResults函数；</li> 
 <li>新增：图表JS对象的chartDataSets元素新增query属性，替换已弃用的paramValues属性；</li> 
 <li>修复：修复数据管理功能不支持Oracle同义词的BUG；</li> 
 <li>修复：修复内置Oracle驱动缺少orai18n.jar导致无法访问某些版本数据库的BUG；</li> 
 <li>修复：修复数据集未正确处理24小时制日期和时间的BUG；</li> 
 <li>修复：修复列表页面关键字查询未重置页码的BUG；</li> 
 <li>修复：修复列表页分页组件未设置英语语言的BUG；</li> 
 <li>改进：数据集预览时可自动合并页面端编辑的属性；</li> 
 <li>其他：SpringBoot版本由2.3.6升级至2.4.6；</li> 
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
            