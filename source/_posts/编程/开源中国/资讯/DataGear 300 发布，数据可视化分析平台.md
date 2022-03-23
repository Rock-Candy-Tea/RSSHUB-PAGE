
---
title: 'DataGear 3.0.0 发布，数据可视化分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f091935a79918e45ceb03d22d546b95abfd.gif'
author: 开源中国
comments: false
date: Wed, 23 Mar 2022 08:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f091935a79918e45ceb03d22d546b95abfd.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">DataGear</a> 3.0.0发布，新增看板分享密码功能和可变模型数据集特性，具体更新内容如下：</p> 
<ul> 
 <li>不兼容：整理合并系统数据库脚本datagear.sql，不支持低于2.13.0版本自动升级；</li> 
 <li>新增：分享看板新增设置密码功能，设置后访问看板需进行密码确认；</li> 
 <li>新增：看板可视编辑模式新增编辑图片/超链接/视频/文本标签元素属性功能;</li> 
 <li>新增：看板可视编辑模式新增插入文本标签功能；</li> 
 <li>新增：看板图表主题新增titleTheme、legendTheme属性，新增用于设置字体大小的fontSize属性；</li> 
 <li>新增：数据集新增【可变模型】特性，移除数据集属性必填规则，用于支持数据结构不固定的数据集；</li> 
 <li>修复：修复未授权用户仍能打开看板展示链接的BUG；</li> 
 <li>修复：修复Excel数据集有空值单元格时，会出现值串列的BUG；</li> 
 <li>修复：修复看板可视编辑模式刷新操作后切换至源码模式未同步源码的BUG；</li> 
 <li>修复：修复看板可视编辑模式删除元素后未重置元素节点路径信息的BUG；</li> 
 <li>修复：修复SQL数据集未选择数据源时SQL自动补全报错的BUG；</li> 
 <li>修复：修复数据源导入/导出数据页面表格宽度未填满的BUG；</li> 
 <li>修复：修复新建看板全局资源存储路径包含新目录时保存报错的BUG；</li> 
 <li>改进：看板可视编辑模式添加快捷执行按钮，点击可直接执行上次操作；</li> 
 <li>改进：看板可视编辑模式删除元素/解绑图表操作改为需确认执行；</li> 
 <li>改进：看板可视编辑模式图表选项编辑文本域改为格式化的文本编辑器；</li> 
 <li>改进：看板可视编辑模式图表选项支持设置为图表选项JS变量名；</li> 
 <li>改进：看板可视编辑模式刷新页面后保持元素边线状态；</li> 
 <li>改进：看板源码编辑模式支持代码折叠；</li> 
 <li>改进：看板编辑页面的图表列表面板改为可拖动；</li> 
 <li>改进：自定义图表默认渲染为数据JSON字符串列表而非表格，避免无法显示完整数据的问题；</li> 
 <li>改进：系统图表支持库ECharts版本由5.2.2升级至5.3.1；</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">DataGear</a>是一款开源免费的数据可视化分析平台，支持自由制作任何您想要的数据可视化看板。</p> 
<p>官网地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">http://www.datagear.tech</a></p> 
<p>源码地址：</p> 
<p>Gitee：<a href="https://gitee.com/datagear/datagear">https://gitee.com/datagear/datagear</a></p> 
<p>Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdatageartech%2Fdatagear" target="_blank">https://github.com/datageartech/datagear</a></p> 
<p>大屏模板地址：<a href="https://gitee.com/datagear/DataGearDashboardTemplate">https://gitee.com/datagear/DataGearDashboardTemplate</a></p> 
<p>系统部分功能效果图：</p> 
<p>看板可视编辑模式</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f091935a79918e45ceb03d22d546b95abfd.gif" referrerpolicy="no-referrer"></p> 
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
            