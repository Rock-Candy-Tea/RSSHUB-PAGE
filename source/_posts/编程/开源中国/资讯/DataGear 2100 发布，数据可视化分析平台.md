
---
title: 'DataGear 2.10.0 发布，数据可视化分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png'
author: 开源中国
comments: false
date: Wed, 17 Nov 2021 09:22:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">DataGear</a> 2.10.0发布，新增7种内置图表，扩充看板API，具体更新内容如下：</p> 
<ul> 
 <li>新增：内置图表新增涟漪气泡图、涟漪坐标散点图、涟漪地图散点图；</li> 
 <li>新增：内置图表新增地图路径图、地图飞线图、平行坐标系图、阶梯折线图；</li> 
 <li>新增：图表编辑页面新增数据集属性别名功能，用于设置图表展示时对应数据系列名称；</li> 
 <li>新增：图表编辑页面新增数据集属性排序功能，用于设置图表展示时对应数据系列顺序；</li> 
 <li>新增：图表JS对象新增dataSetProperties()、dataSetProperty()函数，用于获取数据集属性；</li> 
 <li>新增：图表JS对象新增dataSetPropertyOrder()函数，用于获取/设置数据集属性排序；</li> 
 <li>新增：图表JS对象新增dataSetPropertyAlias()函数，用于获取/设置数据集属性排序，同时弃用的dataSetPropertyLabel()函数；</li> 
 <li>新增：图表JS对象新增dataSetParams()、dataSetParam()，用于获取数据集参数；</li> 
 <li>新增：图表JS对象新增hasDataSetParam()函数，替换已弃用的hasParamDataSet()函数；</li> 
 <li>新增：图表JS对象新增dataSetAlias()函数，用于获取/设置数据集别名，同时弃用chartDataSetName()函数；</li> 
 <li>新增：图表JS对象新增resultMapObjects()函数，用于获取数据集结果数据经属性映射后的对象数组；</li> 
 <li>新增：看板JS对象新增user()函数，用于获取当前浏览用户信息；</li> 
 <li>新增：数据集添加DG_USER、DG_ROLE_NAMES内置参数，用于在后台查询时获取当前用户和角色信息；</li> 
 <li>修复：看板导入功能添加压缩包编码设置项，修复导入含有中文名的压缩包有时会报错的BUG；</li> 
 <li>修复：修复坐标散点图在刷新数据后横坐标没有同步更新的BUG；</li> 
 <li>修复：修复表格图表误将标题文本设置为标题元素样式的BUG；</li> 
 <li>修复：修复看板编辑页面图表列表有时会出现表格列宽混乱的BUG；</li> 
 <li>改进：内置图表改名：[基本散点图]改为[气泡图]，[散点值地图]改为[地图散点图]，[关系地图]改为[地图关系图]；</li> 
 <li>改进：图表编辑页面调整数据集顺序操作由拖拽方式改为更方便的上移/下移按钮方式；</li> 
 <li>改进：图表保存时忽略空数据标记，避免存储长度溢出；</li> 
 <li>改进：修改系统滚动条样式与主题匹配（仅支持webkit浏览器）；</li> 
 <li>改进：简化看板部分支持库文件名，移除"datagear-"前缀；</li> 
 <li>改进：改进内置图表校验加载策略，只有修改时才校验加载，以减少系统启动时间；</li> 
 <li>其他：看板支持库ECharts版本由5.2.0升级至5.2.2；</li> 
 <li>其他：看板支持库jQuery版本由1.12.4升级至3.6.0；</li> 
 <li>其他：表格图表支持库DataTables版本由1.10.18升级至1.11.3，并移除打印、导出等非必要的组件；</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">DataGear</a>是一款开源免费的数据可视化分析平台，可自由制作任何您想要的数据可视化看板，支持接入SQL、CSV、Excel、HTTP接口、JSON等多种数据源。</p> 
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
            