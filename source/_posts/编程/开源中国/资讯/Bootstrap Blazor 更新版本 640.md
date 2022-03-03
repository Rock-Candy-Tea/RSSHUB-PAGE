
---
title: 'Bootstrap Blazor 更新版本 6.4.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=576'
author: 开源中国
comments: false
date: Thu, 03 Mar 2022 08:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=576'
---

<div>   
<div class="content">
                                                                                            <p><strong style="color:#333333"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置 100多 个组件，欢迎大家尝试使用。</span></strong></p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">破坏性更新</h4> 
<ul> 
 <li>feat(#I4V64R): 组件<span> </span><code>Pagination</code><span> </span><code>ListView</code><span> </span>参数<span> </span><code>TotalCount</code><span> </span>由原来<span> </span><code>long</code><span> </span>更改为<span> </span><code>int</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2457">#I4V64R</a><br> 与<span> </span><code>Table</code><span> </span>等组件保持一致，减少数据类型转化代码</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">新增功能</h4> 
<ul> 
 <li>feat(#I4VIHR): 组件<span> </span><code>Button</code><span> </span>增加<span> </span><code>virtual</code><span> </span>关键字到<span> </span><code>HandleClick</code><span> </span>方法方便子类更改点击按钮逻辑<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2466">#I4VIHR</a></li> 
 <li>feat(#I4VEUV): 增加<span> </span><code>BootstrapBlazor.FontAwesome</code><span> </span>包用于封装组件需要的<span> </span><code>Icon</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2464">#I4VEUV</a></li> 
 <li>feat(#I4V7NE): 组件<span> </span><code>CardUpload</code><span> </span>预览地址<span> </span><code>PrevUrl</code><span> </span>支持<span> </span><code>base64</code><span> </span>格式内容字符串<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2461">#I4V7NE</a></li> 
 <li>feat(#I4V8Q9): 组件<span> </span><code>Table</code><span> </span>增加<span> </span><code>ShowMultiFilterHeader</code><span> </span>参数用于控制多级表头时是否显示过滤行默认<span> </span><code>false</code><span> </span>不显示<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2460">#I4V8Q9</a></li> 
 <li>feat(#I4UZ8Y): 组件<span> </span><code>Table</code><span> </span>工具栏按钮与行内编辑删除按钮可分开控制<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2454">#I4UZ8Y</a><br> 工具栏按钮使用<span> </span><code>ShowEditButton</code><span> </span><code>ShowDeleteButton</code><span> </span>控制，行内按钮使用<span> </span><code>ShowEditButtonCallback</code><span> </span><code>ShowDeleteButtonCallback</code><span> </span>控制</li> 
 <li>feat(#I4U8G2): 组件<span> </span><code>Markdown</code><span> </span>支持语法高亮<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2442">#I4U8G2</a></li> 
 <li>feat(#I4TPWE): 组件<span> </span><code>DownloadService</code><span> </span>增加打包文件夹下载重载方法<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2425">#I4TPWE</a></li> 
 <li>feat(#I4TPVY): 组件<span> </span><code>DownloadService</code><span> </span>增加物理文件路径重载方法<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2424">#I4TPVY</a></li> 
 <li>feat(#I4TLGT): 组件<span> </span><code>CardUpload</code><span> </span>增加<span> </span><code>OnZoomAsync</code><span> </span>回调方法<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2422">#I4TLGT</a></li> 
 <li>feat(#I4TERI): 组件<span> </span><code>Table</code><span> </span>编辑/搜索弹窗同时支持垂直居中与拖拽功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2415">#I4TER4</a></li> 
 <li>feat(#I4TERH): 组件<span> </span><code>Dialog</code><span> </span>增加<span> </span><code>ShowMaximizeButton</code><span> </span>参数支持弹窗最大化<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2414">#I4TERH</a></li> 
 <li>feat(#I4TER4): 组件<span> </span><code>ModalDialog</code><span> </span>增加<span> </span><code>ShowMaximizeButton</code><span> </span>参数用于弹窗全屏最大化<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2413">#I4TER4</a></li> 
 <li>feat(#I4T74I): 组件<span> </span><code>Table</code><span> </span>编辑/搜索弹窗支持拖拽功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2412">#I4T74I</a><span> </span>已发布<span> </span><code>6.3.1-beta05</code></li> 
 <li>feat(#I4T5JG): 组件<span> </span><code>Select</code><span> </span>增加<span> </span><code>AutoClearSearchText</code><span> </span>参数用于选中选项后自动清空搜索栏中内容<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2410">#I4T5JG</a><span> </span>已发布<span> </span><code>6.3.1-beta03</code></li> 
 <li>feat(#I4T7ZG): 增加<span> </span><code>BrowserNotification</code><span> </span>组件用于浏览器通知功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2408">#I4T7ZG</a><span> </span>已发布<span> </span><code>6.3.1-beta02</code></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">问题修复</h4> 
<ul> 
 <li>fix(#I4VUTF): 修复<span> </span><code>Table</code><span> </span>组件行内编辑/删除按钮显示逻辑，优先判断<span> </span><code>ShowEditButtonCallback</code><span> </span>回调，未设置时使用<span> </span><code>ShowDefaultButtons</code><span> </span>配合<span> </span><code>ShowEditButton/ShowDeleteButton</code><span> </span>判断是否显示<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2473">#I4VUTF</a></li> 
 <li>fix(#I4V5MJ): 修复<span> </span><code>Table</code><span> </span>组件动态类型时<span> </span><code>DataTableDynamicContext</code><span> </span>参数<span> </span><code>hiddenColumns</code><span> </span>未生效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2456">#I4V5MJ</a><br> <code>hiddenColumns</code><span> </span>中列表格默认不显示<span> </span><code>ColumnList</code><span> </span>中可自行勾选显示</li> 
 <li>fix(#I4U22I): 修复<span> </span><code>Modal</code><span> </span>组件多级弹窗层次结构不正确问题(6.3.0版本导致)<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2444">#I4U22I</a></li> 
 <li>fix(#I4U963): 修复<span> </span><code>Table</code><span> </span>组件高级搜索文本框<span> </span><code>string.Empty</code><span> </span>参与过滤条件问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2439">#I4TNP5</a></li> 
 <li>fix(#I4TNP5): 修复<span> </span><code>InputUpload</code><span> </span>组件双向绑定时未初始化值问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2423">#I4TNP5</a></li> 
 <li>fix(#I4TG7T): 修复<span> </span><code>Modal</code><span> </span>弹窗最大化偶尔失效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2417">#I4TG7T</a></li> 
 <li>fix(#I4TG7O): 修复<span> </span><code>Table</code><span> </span>组件编辑/搜索弹窗中按钮文字丢失问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2416">#I4TG7O</a></li> 
 <li>fix(#I4TBEY): 修复<span> </span><code>Table</code><span> </span>组件页面二次渲染后分页信息错误问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2411">#I4TBEY</a><span> </span>已发布<span> </span><code>6.3.1-beta04</code></li> 
 <li>fix(#I4SSN2): 修复<span> </span><code>Table</code><span> </span>组件使用动态类型时双向绑定<span> </span><code>SelectedRows</code><span> </span>失效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2409">#I4T460</a><span> </span>已发布<span> </span><code>6.3.1-beta01</code></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">更新文档</h4> 
<ul> 
 <li>doc(#I4U882): 更新<span> </span><code>Markdown</code><span> </span>文档描述错误<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2437">#I4U882</a></li> 
 <li>doc(#I4T460): 网页<span> </span><code>Home</code><span> </span>页脚增加运行时长动态更新功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2406">#I4T460</a></li> 
 <li>doc(#I4R77K): 更新<span> </span><code>InputGroup</code><span> </span>示例文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2405">#I4R77K</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">单元测试</h4> 
<ul> 
 <li>test(#I4VXYM): 增加<span> </span><code>BootstrapInputNumber</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2475">#I4VXYM</a></li> 
 <li>test(#I4VUOL): 增加<span> </span><code>PopConfirmButton</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2472">#I4VUOL</a></li> 
 <li>test(#I4VUGM): 增加<span> </span><code>SwitchButton</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2470">#I4VUGM</a></li> 
 <li>test(#I4V6DH): 增加<span> </span><code>Pagination</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2458">#I4V6DH</a></li> 
 <li>test(#I4TPYW): 增加<span> </span><code>DateTimePicker</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2455">#I4TPYW</a></li> 
 <li>test(#I4UQ4S): 提高<span> </span><code>Tree</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2453">#I4UQ4S</a></li> 
 <li>test(#I4UPLE): 增加<span> </span><code>Radio</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2451">#I4UPLE</a></li> 
 <li>test(#I4UMS2): 增加<span> </span><code>CardUpload</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2448">#I4UMS2</a></li> 
 <li>test(#I4UFDK): 增加<span> </span><code>ButtonUpload</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2447">#I4UFDK</a></li> 
 <li>test(#I4UF4J): 增加<span> </span><code>AvatarUpload</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2446">#I4UF4J</a></li> 
 <li>test(#I4UF29): 增加<span> </span><code>InputUpload</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2445">#I4UF29</a></li> 
 <li>test(#I4UDO7): 增加<span> </span><code>TransferPanel</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2443">#I4UDO7</a></li> 
 <li>test(#I4TWJ6): 增加<span> </span><code>Transfer</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2441">#I4TWJ6</a></li> 
 <li>test(#I4TPZ2): 增加<span> </span><code>Tree</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2440">#I4TPZ2</a></li> 
 <li>test(#I4U8Z3): 增加<span> </span><code>LookupFilter</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2438">#I4U8Z3</a></li> 
 <li>test(#I4U4QS): 增加<span> </span><code>Carousel</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2436">#I4U4QS</a></li> 
 <li>test(#I4U4GB): 增加<span> </span><code>EnumFilter</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2435">#I4U4GB</a></li> 
 <li>test(#I4TYXD): 增加<span> </span><code>Console</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2432">#I4TYXD</a></li> 
 <li>test(#I4TWCR): 增加<span> </span><code>StringFilter</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2430">#I4TWCR</a></li> 
 <li>test(#I4TW9L): 增加<span> </span><code>NumberFilter</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2429">#I4TW9L</a></li> 
 <li>test(#I4TW5C): 增加<span> </span><code>DateTimeFilter</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2428">#I4TV55</a></li> 
 <li>test(#I4TV55): 增加<span> </span><code>BoolFilter</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2427">#I4TV55</a></li> 
 <li>test(#I4TUVC): 增加<span> </span><code>TableFilter</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2426">#I4TJ11</a></li> 
 <li>test(#I4TJ11): 增加<span> </span><code>Timeline</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2420">#I4TJ11</a></li> 
 <li>test(#I4TIMF): 增加<span> </span><code>Calendar</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2419">#I4TIMF</a></li> 
 <li>test(#I4TJQM): 增加<span> </span><code>Transition</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2418">#I4TJQM</a></li> 
 <li>test(#I4T736): 增加<span> </span><code>SweetAlert</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2407">#I4T2TK</a></li> 
 <li>test(#I4T2TK): 增加<span> </span><code>Scroll</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2404">#I4T2TK</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">项目地址</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Gitee：<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor">https://gitee.com/LongbowEnterprise/BootstrapBlazor</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor" target="_blank">https://github.com/dotnetcore/BootstrapBlazor</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FBootstrapBlazor%2F%23" target="_blank">https://www.nuget.org/packages/BootstrapBlazor</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">BootstrapBlazor 遵循 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/blob/master/LICENSE">Apache-2.0</a> 开源协议，欢迎大家提交 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls">PR</a> 或 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/issues/new">Issue</a>。喜欢可以给个 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/stargazers">Star</a>。</p>
                                        </div>
                                      
</div>
            