
---
title: 'Bootstrap Blazor 更新版本 5.6.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1492'
author: 开源中国
comments: false
date: Thu, 12 Aug 2021 12:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1492'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置近 90 个组件，欢迎大家尝试使用。本次更新全面升级支持 Bootstrap V5.6，内置 `Bootstrap` 样式框架也升级到了最新版 `v5.1`</span></p> 
<p style="text-align:start"><strong>发布时间 2021-8-12 V5.6.0</strong></p> 
<h4 style="text-align:start">增加功能</h4> 
<ul> 
 <li>!1709 feat(#I450PE): 'Tab' 组件增加指定索引 <code>ActiveTab</code> 重载方法 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1709">#I450PE</a></li> 
 <li>!1708 feat(#I451B7): <code>Switch</code> 组件内置 <code>Table</code> 单元格内时支持对齐参数 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1708">#I451B7</a></li> 
 <li>!1704 chore(#I44WDE): 升级项目底层 <code>dotnet</code> 框架到 <code>5.0.9</code> <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1704">#I44WDE</a></li> 
 <li>!1701 feat(#I44TYN): 增加 <code>NullSwitch</code> 组件支持 Nullable <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1701">#I44TYN</a></li> 
 <li>!1700 feat:(#I44QUY): <code>Table</code> 组件内置到 <code>ValidateForm</code> 中后行内显示与编辑不显示前置标签 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1694">#I44GIG</a></li> 
 <li>!1694 feat(#I44GIG): <code>Table</code> 组件过滤功能新增支持 <code>int</code> <code>double</code> <code>decimal</code> 三种数据类型 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1694">#I44GIG</a></li> 
 <li>!1691 feat(#I44F4H): <code>Table</code> 组件 <code>EditForm</code> <code>EditInCell</code> 模式下支持 <code>Readonly</code> 参数 编辑时只读 新建时可输入 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1691">#I44F4H</a></li> 
 <li>!1690 feat(#I44CUD): <code>Table</code> 组件增加 <code>OnAfterSaveAsync</code> 回调方法用于保存后执行此回调 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1690">#I44CUD</a></li> 
 <li>!1687 feat(#I444LV): <code>Search</code> 组件点击搜索按钮后自动获得焦点 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1687">#I444LV</a></li> 
 <li>!1686 feat(#I4421V): <code>Table</code> 组件 <code>SearchDialog</code> 支持 <code>Inline</code> 模式布局与标签对齐功能 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1686">#I4421V</a></li> 
</ul> 
<h4 style="text-align:start">问题修复</h4> 
<ul> 
 <li>!1712 fix(#I453H8): 修复 <code>EditDialog</code> 组件设置 <code>Editable</code> 未生效问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1712">#I453H8</a></li> 
 <li>!1705 fix(#I44WS2): 修复 <code>PopconfirmButon</code> 点击弹窗内按钮后再此点击时无法弹出问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1704">#I44WS2</a></li> 
 <li>!1703 fix(#I44W1K): 修复 <code>PopconfirmButon</code> 二次点击闪烁问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1703">#I44W1K</a></li> 
 <li>!1699 fix(#I44N03): 修复 <code>Table</code> 组件复选框状态点击新建按钮后未清除问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1699">#I44N03</a></li> 
 <li>!1698 fix(#I44MZ9): 修复 <code>Table</code> 组件点击删除按钮后无法点击新建与编辑按钮问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1698">#I44MZ9</a></li> 
 <li>!1697 fix(#I44MZ1): 修复 <code>Table</code> 组件浮点数值列设置 <code>Step</code> 编辑模式下报错问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1693">#I44I8C</a></li> 
 <li>!1693 fix(#I44I8C): 修复 <code>MultiSelect</code> 组件向上弹出下拉框时指示小箭头错位问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1693">#I44I8C</a></li> 
 <li>!1692 fix(#I44I7S): 移除 <code>dropdown-menu</code> 高度限制样式保持 <code>bootstrap</code> 原生样式 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1692">#I44I7S</a></li> 
</ul> 
<p style="text-align:left">项目地址</p> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor">https://gitee.com/LongbowEnterprise/BootstrapBlazor</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor" target="_blank">https://github.com/dotnetcore/BootstrapBlazor</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FBootstrapBlazor%2F%23" target="_blank">https://www.nuget.org/packages/BootstrapBlazor</a></li> 
</ul> 
<p style="text-align:left">BootstrapBlazor 遵循 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/blob/master/LICENSE">Apache-2.0</a> 开源协议，欢迎大家提交 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls">PR</a> 或 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/issues/new">Issue</a>。喜欢可以给个 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/stargazers">Star</a>。</p>
                                        </div>
                                      
</div>
            