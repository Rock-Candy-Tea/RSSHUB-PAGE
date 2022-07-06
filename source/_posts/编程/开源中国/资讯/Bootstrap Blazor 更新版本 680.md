
---
title: 'Bootstrap Blazor 更新版本 6.8.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=607'
author: 开源中国
comments: false
date: Wed, 06 Jul 2022 11:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=607'
---

<div>   
<div class="content">
                                                                                            <h4 style="margin-left:0; margin-right:0; text-align:start"><strong style="color:#333333"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置 120 多 个组件，欢迎大家尝试使用。单元测试所有组件代码覆盖率达到了 100%</span></strong></h4> 
<h4 style="margin-left:0; margin-right:0; text-align:start">破坏性更新</h4> 
<ul> 
 <li>feat(#I5CHPN): 组件<span> </span><code>Tree</code><span> </span>移除内置不折行与截断样式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2906">#I5CHPN</a></li> 
 <li>feat(#206): 组件<span> </span><code>Table</code><span> </span>树状结构<span> </span><code>IsTree</code><span> </span>模式重写 文档参考<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.blazor.zone%2Ftables%2Ftree">https://www.blazor.zone/tables/tree</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">新增功能</h4> 
<ul> 
 <li>feat(#I5AK02): 组件<span> </span><code>Table</code><span> </span>增加一个实例属性<span> </span><code>Rows</code><span> </span>用于获得当前表格显示所有行数据集合<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2850">#I5AK02</a></li> 
 <li>feat(#I5AO8I): 组件<span> </span><code>LinkButton</code><span> </span>使用新的<span> </span><code>link-color</code><span> </span>样式代替<span> </span><code>text-color</code><span> </span>样式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2854">#I5AK02</a></li> 
 <li>feat(#I5AOA7): 组件<span> </span><code>Logout</code><span> </span>增加<span> </span><code>ShowUserName</code><span> </span>参数用于仅显示头像<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2856">#I5AOA7</a></li> 
 <li>feat(#I5APA6): 增加<span> </span><code>RibbonTab</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2857">#I5APA6</a></li> 
 <li>feat(#I5APAI): 组件<span> </span><code>Layout</code><span> </span>样式使用变量方便使用者更改样式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2858">#I5APAI</a></li> 
 <li>feat(#I5AY2S): 组件<span> </span><code>Table</code><span> </span>部分样式更改为<span> </span><code>css</code><span> </span>变量方便更改主题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2867">#I5AY2S</a></li> 
 <li>feat(#I5B6SL): 组件<span> </span><code>Table</code><span> </span>选中行<span> </span><code>SelectedRows</code><span> </span>功能支持无主键数据集内部使用对象相等原理判断保持选中状态<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2871">#I5B6SL</a></li> 
 <li>feat(#I5BGMO): 组件<span> </span><code>Layout</code><span> </span>增加<span> </span><code>ChildContent</code><span> </span>模板用于自定义显示内容<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2880">#I5BGMO</a></li> 
 <li>feat(#I5C315): 组件<span> </span><code>Pagination</code><span> </span>增加自定义<span> </span><code>HTML</code><span> </span>标签功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2897">#I5C315</a></li> 
 <li>feat(#I5CMCR): 增加<span> </span><code>ILocalizationResolve</code><span> </span>服务，本地化信息丢失时回调此服务方法，增加文化信息回落机制<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2908">#I5CMCR</a></li> 
 <li>feat(#I5CSHR): 组件<span> </span><code>Table</code><span> </span>增加<span> </span><code>ShowLoadingInFirstRender</code><span> </span>参数用于首次加载数据时是否显示加载动画<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2912">#I5CSHR</a></li> 
 <li>feat(#I5CWVZ): 组件<span> </span><code>Table</code><span> </span>增加<span> </span><code>InsertRowMode</code><span> </span>参数用于<span> </span><code>Incell</code><span> </span>模式下设置插入新行位置 默认插入到最后<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2915">#I5CSHR</a></li> 
 <li>feat(#I5DFVS): 接口<span> </span><code>IDynamicObjectContext</code><span> </span>增加<span> </span><code>OnSelectedRows</code><span> </span>回调委托用于<span> </span><code>Table</code><span> </span>组件动态类型时保持选中行功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2932">#I5DFVS</a></li> 
 <li>feat(#I5DUPB): 组件<span> </span><code>Card</code><span> </span>开启<span> </span><code>IsCollapsible</code><span> </span>后支持<span> </span><code>CardHeaderTemplate</code><span> </span>自定义模板<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2940">#I5DUPB</a></li> 
 <li>feat(#I5EASI): 组件<span> </span><code>Card</code><span> </span>开启<span> </span><code>IsCollapsible</code><span> </span>后支持默认为收缩状态<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2951">#I5EASI</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">问题修复</h4> 
<ul> 
 <li>fix(#I5AEHH): 组件<span> </span><code>LinkButton</code><span> </span>支持<span> </span><code>OnClickWithoutRender</code><span> </span>功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2847">#I5AEHH</a></li> 
 <li>fix(#I5AG3Z): 组件<span> </span><code>Redirect</code><span> </span>修复<span> </span><code>release</code><span> </span>版本报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2848">#I5AG3Z</a></li> 
 <li>fix(#I5AO8W): 组件<span> </span><code>Divider</code><span> </span>修复<span> </span><code>Vertical</code><span> </span>模式下浏览器改变大小时不显示问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2855">#I5AG3Z</a></li> 
 <li>fix(#I5AAUH): 修复组件<span> </span><code>PopConfirmButton</code><span> </span>设置<span> </span><code>IsAsync</code><span> </span>时支持<span> </span><code>OnConfirm</code><span> </span>不支持同步方法问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2861">#I5AAUH</a></li> 
 <li>fix(#I5AW0W): 修复<span> </span><code>EditForm</code><span> </span>自动渲染组件时设置渲染为<span> </span><code>Textarea</code><span> </span>并且只读时<span> </span><code>Rows</code><span> </span>参数未生效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2865">#I5AW0W</a></li> 
 <li>fix(#I5AXR3): 修复<span> </span><code>TabItemOptionAttribute</code><span> </span>设定值优先级比点击菜单设置值低问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2868">#I5AXR3</a></li> 
 <li>fix(#I5B9O3): 修复<span> </span><code>DateTimeRange</code><span> </span>组件在表单中正常布局未折行问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2873">#I5B9O3</a></li> 
 <li>fix(#I5BBE6): 修复<span> </span><code>RadioList</code><span> </span>组件双向绑定枚举类型时设置<span> </span><code>Items</code><span> </span>参数失效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2874">#I5BBE6</a></li> 
 <li>fix(#I5BBFM): 修复<span> </span><code>RowType</code><span> </span>设置为<span> </span><code>Inline</code><span> </span>模式下部分组件折行问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2875">#I5BBFM</a></li> 
 <li>fix(#I5BHF9): 修复<span> </span><code>AutoFill</code><span> </span>首次加载时不显示<span> </span><code>Value</code><span> </span>值问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2879">#I5BHF9</a></li> 
 <li>fix(#I5C0EQ): 修复<span> </span><code>PopconfirmButton</code><span> </span>开启<span> </span><code>IsAsync</code><span> </span>参数后在<span> </span><code>ValidateForm</code><span> </span>中使用时报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2895">#I5C0EQ</a></li> 
 <li>fix(#I5CWUD): 调整<span> </span><code>Radio</code><span> </span><code>Checkbox</code><span> </span>样式防止标签过长导致变形问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2914">#I5CWUD</a></li> 
 <li>fix(#I5D0X0): 更新<span> </span><code>Divider</code><span> </span>样式修复垂直分隔符<span> </span><code>is-left</code><span> </span><code>is-right</code><span> </span>样式不正确问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2925">#I5D0X0</a></li> 
 <li>fix(#I5D87T): 修复<span> </span><code>Editor</code><span> </span>组件切换路由时报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2927">#I5D87T</a></li> 
 <li>fix(#I5DIM6): 修复<span> </span><code>Table</code><span> </span>组件<span> </span><code>TableToolbar</code><span> </span>内自定义按钮设置<span> </span><code>Size</code><span> </span>参数无效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2935">#I5DIM6</a></li> 
 <li>fix(#I5DM0X): 修复<span> </span><code>Table</code><span> </span>组件使用动态类型模式下无法保持选中行问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2938">#I5DM0X</a></li> 
 <li>fix(#I5DRKS): 修复<span> </span><code>Dialog</code><span> </span>组件开启可拖动功能后无法关闭弹窗问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2939">#I5DRKS</a></li> 
 <li>fix(#I5DV57): 修复<span> </span><code>Table</code><span> </span>组件开启搜索框自适应高度计算错误问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2942">#I5DV57</a></li> 
 <li>fix(#I5CJDY): 修复<span> </span><code>Tab</code><span> </span>组件嵌套使用时<span> </span><strong>火柴棍</strong><span> </span>特效首次出现位置不正确问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2950">#I5CJDY</a></li> 
 <li>fix(#I5F09S): 修复<span> </span><code>Progress</code><span> </span>组件未支持自定义<span> </span><code>HTML</code><span> </span>标签问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2961">#I5F09S</a></li> 
 <li>fix(#I5F2P7): 修复<span> </span><code>Table</code><span> </span>组件开始树形结构后加载动画不显示问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2962">#I5F2P7</a></li> 
 <li>fix(#I5F5G2): 修复<span> </span><code>Table</code><span> </span>组件<span> </span><code>OnQueryAsync</code><span> </span>回调中未设置排序处理时内部逻辑未生效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2963">#I5F5G2</a></li> 
 <li>fix(#I5F6P8): 修复<span> </span><code>Table</code><span> </span>组件排序内部逻辑 支持使用<span> </span><code>Items</code><span> </span>与不分页时处理排序逻辑<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2965">#I5F6P8</a></li> 
 <li>fix(#I5FCP7): 修复<span> </span><code>Cascader</code><span> </span>组件数据验证失败后提示框背景色为黑色问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2967">#I5FCP7</a></li> 
 <li>fix(#I5FCQM): 修复<span> </span><code>Cascader</code><span> </span>组件数据验证失败后不会自动弹出提示框问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2968">#I5FCQM</a></li> 
 <li>fix(#I5FFLA): 修复<span> </span><code>Table</code><span> </span>行内自定义扩展按钮会重复增加问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2970">#I5FFLA</a></li> 
 <li>fix(#I5F9NL): 修复<span> </span><code>Table</code><span> </span>过滤/搜索列为可为空类型时报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2973">#I5F9NL</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">更新文档</h4> 
<ul> 
 <li>doc(#I5APG8): 增加<span> </span><code>RibbonTab</code><span> </span>组件示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2859">#I5APG8</a></li> 
 <li>doc(#I58OLE): 增加<span> </span><code>Timezone</code><span> </span>示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2862">#I58OLE</a></li> 
 <li>doc(#I5C328): 增加<span> </span><code>Table</code><span> </span>组件动态数据分页功能示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2898">#I5C328</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">单元测试</h4> 
<ul> 
 <li>test(#I5AN0Q): 增加<span> </span><code>LambdaExtensions</code><span> </span>扩展方法单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2851">#I5AN0Q</a></li> 
 <li>test(#I5APIV): 增加<span> </span><code>RibbonTab</code><span> </span>组件单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2860">#I5APIV</a></li> 
 <li>test(#I5ATRC): 增加<span> </span><code>ObjectExtensions</code><span> </span>组件单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2864">#I5APIV</a></li> 
 <li>test(#I5AXD9): 增加<span> </span><code>Utility</code><span> </span>扩展方法单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2866">#I5AXD9</a></li> 
 <li>test(#I5BPFP): 增加<span> </span><code>ITableColumnExtensions</code><span> </span>扩展方法<span> </span><code>ToSearchs</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2884">#I5AXD9</a></li> 
 <li>test(#I5CX7T): 增加<span> </span><code>InsertRowMode</code><span> </span>新参数单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2916">#I5CX7T</a></li> 
 <li>test(#I5E6JZ): 增加<span> </span><code>Footer</code><span> </span>组件单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2948">#I5E6JZ</a></li> 
 <li>test(#I5EN6E): 增加<span> </span><code>Redirect</code><span> </span>组件单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2953">#I5EN6E</a></li> 
 <li>test(#I5ETVU): 增加<span> </span><code>Row</code><span> </span>组件单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2958">#I5ETVU</a></li> 
 <li>test(#I5FD5Z): 增加<span> </span><code>Cascader</code><span> </span>组件单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2969">#I5FD5Z</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>项目地址</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Gitee：<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor">https://gitee.com/LongbowEnterprise/BootstrapBlazor</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor" target="_blank">https://github.com/dotnetcore/BootstrapBlazor</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FBootstrapBlazor%2F%23" target="_blank">https://www.nuget.org/packages/BootstrapBlazor</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">BootstrapBlazor 遵循 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/blob/master/LICENSE">Apache-2.0</a> 开源协议，欢迎大家提交 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls">PR</a> 或 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/issues/new">Issue</a>。喜欢可以给个 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/stargazers">Star</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            