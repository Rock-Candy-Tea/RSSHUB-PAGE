
---
title: 'DataGear 2.9.0 发布，数据可视化分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png'
author: 开源中国
comments: false
date: Wed, 13 Oct 2021 09:18:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">DataGear</a> 2.9.0发布，新增内置图表，扩充看板 API，具体更新内容如下：</p> 
<ul> 
 <li>新增：内置图表新增嵌套饼图、单选下拉框、多选下拉框；</li> 
 <li>新增：内置标签卡图表新增 flex 配置项，用于配置弹性布局；</li> 
 <li>新增：图表 JS 对象新增 themeStyleName、themeStyleSheet 函数，用于为定义图表 CSS 样式提供支持；</li> 
 <li>新增：图表 JS 对象新增 elementStyle、styleString函数，用于为定义图表 CSS 样式提供支持；</li> 
 <li>修复：修复数据集（CSV、JSON 等）修改内容后必须刷新看板页面才能更新数据的 BUG ；</li> 
 <li>修复：修复当登录超时后点击查询页面的查询按钮无响应的 BUG ；</li> 
 <li>改进：重构内置表格图表配置项，支持细粒度配置表格样式；</li> 
 <li>改进：重构内置标签卡图表配置项，支持细粒度配置标签样式；</li> 
 <li>改进：改进表格图表滚动条样式，使其与图表主题匹配（仅支持 webkit 内核浏览器）；</li> 
 <li>改进：看板内图表元素的内置 CSS 样式改为通过样式类实现，避免用户定义样式不起作用；</li> 
 <li>改进：数据集预览即使执行出错也返回解析后的内容，便于排查拼写错误；</li> 
 <li>改进：数据集参数、属性、数据格式修改时也须重新执行预览；</li> 
 <li>改进：删除用户操作改为必须选择数据迁移目标用户后才能删除；</li> 
 <li>其他：ECharts 版本由 5.1.2 升级至 5.2.0 ；</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">DataGear</a> <span style="background-color:#ffffff; color:#333333">是一款开源免费的数据可视化分析平台，可自由制作任何您想要的数据可视化看板，支持接入 SQL、CSV、Excel、HTTP 接口、JSON 等多种数据源。</span></p> 
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
            