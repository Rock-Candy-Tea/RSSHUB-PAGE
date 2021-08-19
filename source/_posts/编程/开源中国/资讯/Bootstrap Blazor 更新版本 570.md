
---
title: 'Bootstrap Blazor 更新版本 5.7.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8061'
author: 开源中国
comments: false
date: Thu, 19 Aug 2021 09:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8061'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置近 100 个组件，欢迎大家尝试使用。</span></p> 
<p style="text-align:start"><strong>发布时间 2021-8-17 V5.7.0</strong></p> 
<h4 style="text-align:start">增加功能</h4> 
<ul> 
 <li>!1738 feat(#I4699U): <code>Display</code> 组件增加内置于表单中时增加默认背景色功能 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1738">#I4697U</a></li> 
 <li>!1737 feat(#I4697U): <code>Table</code> 组件 <code>Toolbar</code> 工具栏内按钮未设置图标时在移动端模式下显示汉字 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1737">#I4697U</a></li> 
 <li>!1734 feat(#I461UK): <code>Table</code> 组件增加 <code>SearchMode</code> 参数用于控制搜索栏渲染方式 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1734">#I461UK</a></li> 
 <li>!1733 feat(#I45YF4): <code>EditorForm</code> 组件增加 <code>Items</code> 参数用于接收指定列进行渲染 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1732">#I45YF4</a></li> 
 <li>!1732 feat(#I45X3W): <code>Table</code> 组件增加 <code>ShowCardView</code> 参数用于手工切换视图模式 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1732">#I45X3W</a></li> 
 <li>!1731 refactor(#I45WXS): <code>Table</code> 组件 <code>RenderTableModel</code> 参数名更改为 <code>RenderTableMode</code> <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1731">#I45WXS</a></li> 
 <li>!1728 fix(#I45VC8): popup window when set enable then disable</li> 
 <li>!1721 feat(#I45IO4): <code>Select</code> 组件自动创建时支持开为空枚举类型 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1721">#I45IO4</a></li> 
 <li>!1717 feat(#I45DE4): <code>Table</code> 组件增加 <code>IsTracking</code> 参数用于父子表录入场景需求 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1717">#I45DE4</a></li> 
 <li>!1715 feat(#I458DK): <code>DynamicDataTableContext</code> 内置对 <code>DBNull</code> 数据类型处理防止报错 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1715">#I458DK</a></li> 
 <li>!1713 feat(#I4567F): <code>Dialog</code> 增加 <code>HeaderTemplate</code> 自定义模板 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1713">#I4567F</a></li> 
</ul> 
<h4 style="text-align:start">问题修复</h4> 
<ul> 
 <li>!1730 fix(#I45VIZ): 修复 <code>DateTimePicker</code> 组件设置禁用后再开启时无法弹出日历框问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1730">#I45VIZ</a></li> 
 <li>!1729 fix(#I45VCK): 修复 <code>DateTimePicker</code> 组件动态更新 <code>IsDisabled</code> 后仍然弹出日历框问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1729">#I45VCK</a></li> 
 <li>!1728 fix(#I45VC8): 修复 <code>DateTimeRange</code> 组件动态更新 <code>IsDisabled</code> 后仍然弹出日历框问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1728">#I45VC8</a></li> 
 <li>!1723 feat(#I45L4I): <code>Table</code> 组件自动生成编辑模板时支持可为空枚举类型 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1723">#I45L4I</a></li> 
 <li>!1727 fix(#I45QNP): 修复 <code>PopConfirmButton</code> <code>OnBeforeClick</code> 逻辑错误问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1727">#I45QNP</a></li> 
 <li>!1726 fix(#I45N52): 修复本地化 <code>GetAllStrings</code> 方法报错问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1726">#I45N52</a></li> 
 <li>!1724 fix(#I44MWD): 移除 <code>Tree</code> 组件 <code>Items</code> 只读显示 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1724">#I44MWD</a></li> 
 <li>!1719 fix(#I45H57): 修复本地化功能在 <code>CentOS</code> <code>WSL</code> 环境中资源文件加载失败问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1719">#I45H57</a></li> 
 <li>!1712 fix(#I453H8): 修复 <code>EditDialog</code> 组件设置 <code>Editable</code> 未生效问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1712">#I453H8</a></li> 
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
            