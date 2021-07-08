
---
title: 'Bootstrap Blazor 更新版本 5.0.38'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5742'
author: 开源中国
comments: false
date: Thu, 08 Jul 2021 10:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5742'
---

<div>   
<div class="content">
                                                                    
                                                        <h4 style="text-align:start"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置近 90 个组件，欢迎大家尝试使用。</span></h4> 
<p style="text-align:start">发布时间 2021-07-08</p> 
<h4 style="text-align:start">增加功能</h4> 
<ul> 
 <li>!1556 feat(#I3ZLCL): 组件 <code>Table</code> 固定列功能兼容 <code>Light</code> <code>Dark</code> 模式表头背景色 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1556">#I3ZLCL</a></li> 
 <li>!1554 feat(#I3ZKQU): 组件 <code>Table</code> 开始多表头时保持原始表头 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1554">#I3ZKQU</a></li> 
 <li>!1552 feat(#I3ZJVJ): 组件 <code>Table</code> 表头排序 <code>Tooltip</code> 增加本地化功能 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1545">#I3ZJVJ</a></li> 
 <li>!1545 feat(#I3Z3FZ): 组件 <code>Table</code> 增加 <code>ShowSearchText</code> 参数用于控制是否显示搜索文本框默认 true <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1545">#I3Z3FZ</a></li> 
 <li>!1543 feat(#I3Z2ZB): <code>DynamicObjectContextExtensions</code> 增加常用标签扩展方法 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1543">#I3Z2ZB</a></li> 
 <li>!1542 feat(#I3Z2TU): 扩展方法 <code>GetDisplayName</code> 增加动态程序集检查方式报错 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1542">#I3Z2TU</a></li> 
 <li>!1540 feat(#I3Z00I): 组件 <code>Table</code> 支持使用 <code>DataTable</code> 作为数据源时 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1540">#I3Z00I</a></li> 
 <li>!1539 feat(#I3Z008): <code>EmitHelper</code> 生成动态类时支持属性上增加自定义标签功能 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1539">#I3Z008</a></li> 
 <li>!1535 feat(#I3VXUH): 组件 <code>Table</code> 支持更新 <code>Items</code> 参数后自动刷新 <code>UI</code> <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1535">#I3VXUH</a></li> 
 <li>!1534 feat(#I3VXUA): 组件 <code>DateTimePicker</code> 值为 <code>DateTime.MinValue</code> 时转化为 <code>DateTime.Now</code> <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1530">#I3YTWL</a></li> 
 <li>!1530 feat(#I3YTWL): 组件 <code>ValidateForm</code> 增加动态程序集判断防止报错 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1530">#I3YTWL</a></li> 
 <li>!1529 feat(#I3YTVC): <code>Utility</code> 扩展方法支持动态程序集防止报错 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1529">#I3YTVC</a></li> 
</ul> 
<h4 style="text-align:start">问题修复</h4> 
<ul> 
 <li>!1548 fix(#I3Z9DJ): 修复 <code>Table</code> 组件显示动态类型列开启过滤功能时过滤弹窗显示位置不正确问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1548">#I3Z9DJ</a></li> 
 <li>!1544 fix(#I3Z3BD): 修复 <code>CreateCallback</code> 方法内部缓存键值错误导致多表格编辑时报错问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1544">#I3Z3BD</a></li> 
 <li>!1541 fix(#I3Z2NH): 修复 <code>AutoGenerateColumnAttribute</code> 设置 <code>ComponentType</code> 时未生效问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1541">#I3Z2NH</a></li> 
 <li>!1533 fix(#I3YX2M): 修复 <code>CardUpload</code> 组件删除按钮不工作问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1533">#I3YX2M</a></li> 
 <li>!1532 fix(#I3Y4XW): 修复 <code>CardUpload</code> 组件设置单选并给定默认值时仍显示上传按钮问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1532">#I3Y4XW</a></li> 
</ul> 
<h4 style="text-align:start">示例更新</h4> 
<ul> 
 <li>!1558 doc(#I3ZLCU): 更新 <code>AutoComplete</code> 组件参数说明文档 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1558">#I3ZLCU</a></li> 
 <li>!1557 doc(#I3ZLCR): 更新 <code>Table</code> 组件固定列文档适配表头 <code>Light</code> <code>Dark</code> 模式下背景色 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1557">#I3ZLCR</a></li> 
 <li>!1546 doc(#I3Z3HQ): 更新 <code>Table</code> 组件仅显示高级搜索按钮示例 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1546">#I3Z3HQ</a></li> 
 <li>!1536 doc(#I3YZMG): 增加 <code>Table</code> 组件更新 <code>Items</code> 数据源后自动更新 <code>UI</code> 示例 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1528">#I3YTTE</a></li> 
 <li>!1528 doc(#I3YTTE): 更新 <code>Tab</code> 组件 <code>IsOnlyRenderActiveTab</code> 示例代码 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1528">#I3YTTE</a></li> 
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
            