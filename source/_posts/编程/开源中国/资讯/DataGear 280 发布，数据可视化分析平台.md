
---
title: 'DataGear 2.8.0 发布，数据可视化分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png'
author: 开源中国
comments: false
date: Wed, 08 Sep 2021 09:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-636247d933d5080918b10b4014fbc7a2151.png'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">DataGear</a> 2.8.0 发布，新增大幅提升系统性能的缓存支持 ，增强图表JS对象API ，具体更新内容如下：</p> 
<ul> 
 <li>移除：移除管理员专有的数据源模式匹配授权功能，简化系统数据权限设计；</li> 
 <li>新增：新增数据源防护功能，使管理员可控制是否允许用户创建指定URL的数据源；</li> 
 <li>新增：图表、看板JS对象新增originalInfo函数，用于获取/设置图表展示数据的原始信息；</li> 
 <li>新增：图表JS对象新增registerEventHandlerDelegation、removeEventHandlerDelegation函数，用于为图表事件处理提供支持；</li> 
 <li>新增：图表JS对象新增callEventHandler、echartsOffEventHandler函数，用于为图表事件处理提供支持；</li> 
 <li>新增：图表JS对象新增resultData函数，用于获取/设置图表数据集结果数据；</li> 
 <li>新增：图表JS对象新增resultDataElement函数，用于获取图表数据集结果数据指定索引的元素；</li> 
 <li>新增：图表JS对象新增gradualColor函数，用于为图表配色提供支持；</li> 
 <li>新增：看板JS对象新增mapURLs函数，为自定义地图URL映射提供API；</li> 
 <li>修复：修复参数化数据集对于大数值参数可能出现精度丢失的BUG；</li> 
 <li>修复：修复数据管理列表/编辑页面、SQL工作台查询结果对于大数值会出现精度丢失的BUG；</li> 
 <li>修复：修复在已登录状态下打开/login地址会死循环的BUG；</li> 
 <li>改进：用户关联角色功能改为在用户编辑页面而非角色管理页面；</li> 
 <li>改进：系统添加缓存支持，大幅提升系统性能；</li> 
 <li>改进：标签卡图表添加横排配置项"inline"，配置项label.name简化为name，label.value简化为value；</li> 
 <li>改进：图表JS对象弃用eventBindHandlerDelegation、eventUnbindHandlerDelegation函数；</li> 
 <li>改进：看板编辑页面插入图表对话框改为悬浮面板，便于多次插入图表操作；</li> 
 <li>改进：登录页、注册页、重置密码页添加右上角系统菜单；</li> 
 <li>改进：程序发布包配置文件中添加DataGearWorkspace配置项模板；</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.datagear.tech%2F" target="_blank">DataGear</a>是一款数据可视化分析平台，可自由制作任何您想要的数据可视化看板，支持SQL、CSV、Excel、HTTP接口、JSON等多种数据源。</p> 
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
            