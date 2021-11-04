
---
title: 'Bootstrap Blazor 更新版本 5.18.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6018'
author: 开源中国
comments: false
date: Thu, 04 Nov 2021 02:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6018'
---

<div>   
<div class="content">
                                                                                            <h4 style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置近 100 个组件，欢迎大家尝试使用。</span></h4> 
<h4 style="margin-left:0; margin-right:0; text-align:start">增加功能</h4> 
<ul> 
 <li>!2026 feat(#I4GSP6): 组件<span> </span><code>ValidateForm</code><span> </span>增加实例属性<span> </span><code>ValueChangedFields</code><span> </span>用户获取表单内更改值的字段用于优化更新逻辑<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2026">#I4GSP6</a></li> 
 <li>!2025 feat(#I4GSNV): 组件<span> </span><code>AutoFill</code><span> </span>移除泛型类约束<span> </span><code>ISelectedItem</code><span> </span>更加通用<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2025">#I4GSNV</a></li> 
 <li>!2018 feat(#I4GKU8): 组件<span> </span><code>Layout</code><span> </span>增加<span> </span><code>IsOnlyRenderActiveTab</code><span> </span>用于更改<span> </span><code>Tab</code><span> </span>组件渲染方式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2018">#I4GKU8</a></li> 
 <li>!2017 feat(#I4GHFS): 新增<span> </span><code>PrintService</code><span> </span>打印服务组件随时随地打印想要的内容<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2017">#I4GHFS</a></li> 
 <li>!2015 feat(#I4GF5X): 重新设计<span> </span><code>CacheManager</code><span> </span>内部类优化组件性能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2015">#I4GF5X</a></li> 
 <li>!2008 feat(#I4FY7A): 组件<span> </span><code>Layout</code><span> </span>增加<span> </span><code>IsCollapsed</code><span> </span>参数用于控制首次加载时是否收缩侧边栏 默认值<span> </span><code>false</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2008">#I4FY7A</a></li> 
 <li>!1997 feat(#I4FPF4): 组件<span> </span><code>Table</code><span> </span>设置虚拟滚动时移除内部对<span> </span><code>Height</code><span> </span>设置的默认值便于外部使用样式设置高度<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1997">#I4FPF4</a></li> 
 <li>!1996 feat(#I4FOSV): 组件<span> </span><code>TreeItem</code><span> </span>增加<span> </span><code>CssClass</code><span> </span>参数用于设置自定义样式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1996">#I4FOSV</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">问题修复</h4> 
<ul> 
 <li>!2024 fix(#I4GSLY): 修复组件<span> </span><code>TableColumn</code><span> </span>内联设置<span> </span><code>Editable</code><span> </span>时无法覆盖<span> </span><code>AutoGenerateClassAttribute</code><span> </span>标签设置值<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2024">#I4GSLY</a></li> 
 <li>!2007 fix(#I4G5B9): 修复组件<span> </span><code>Table</code><span> </span>设置<span> </span><code>SearchTemplate</code><span> </span>再高级搜索中失效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2007">#I4G5B9</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">更新文档</h4> 
<ul> 
 <li>!2027 doc(#I4GST8): 文档后台生成器更新<span> </span><code>Footer</code><span> </span>样式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2027">#I4GST8</a></li> 
 <li>!1999 doc(#I4FVPT): 文档下方增加<span> </span><code>razor</code><span> </span>代码片段<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1999">#I4FVPT</a></li> 
 <li>!2010 doc(#I4G814): 文档系统全面增加多语言即时翻译功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2010">#I4G814</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">单元测试</h4> 
<ul> 
 <li>!2028 test(#I4GSU1): 增加单元测试框架集成<span> </span><code>xUnit</code><span> </span><code>bUnit</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2028">#I4GSU1</a></li> 
</ul> 
<p>项目地址</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Gitee：<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor">https://gitee.com/LongbowEnterprise/BootstrapBlazor</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor" target="_blank">https://github.com/dotnetcore/BootstrapBlazor</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FBootstrapBlazor%2F%23" target="_blank">https://www.nuget.org/packages/BootstrapBlazor</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">BootstrapBlazor 遵循 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/blob/master/LICENSE">Apache-2.0</a> 开源协议，欢迎大家提交 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls">PR</a> 或 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/issues/new">Issue</a>。喜欢可以给个 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/stargazers">Star</a>。</p>
                                        </div>
                                      
</div>
            