
---
title: 'Bootstrap Blazor 更新版本 6.0.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=329'
author: 开源中国
comments: false
date: Thu, 11 Nov 2021 08:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=329'
---

<div>   
<div class="content">
                                                                                            <h4 style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置近 100 个组件，欢迎大家尝试使用。</span></h4> 
<h4 style="margin-left:0; margin-right:0; text-align:start">破坏性更新</h4> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">!2033 feat(#I4H52A): 组件<span> </span><code>AutoFill</code><span> </span>原参数<span> </span><code>CustomFiler</code><span> </span>更改为<span> </span><code>OnCustomFilter</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2033">#I4H52A</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">!2061 feat(#I4HOAT): 重构<span> </span><code>ServiceProviderFactory</code><span> </span>静态类<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2061">#I4HOAT</a></p> </li> 
</ul> 
<pre style="text-align:start"><code><span><strong style="color:#333333">public</strong> <strong style="color:#333333">void</strong> <strong style="color:#990000">Configure</strong><span>(IApplicationBuilder app, IWebHostEnvironment env)</span>
</span>&#123;
    <em>// 使用扩展方法</em>
    app.ApplicationServices.RegisterProvider();
    
    <em>// 或者使用静态方法</em>
    <em>// BootstrapBlazor.Components.ServiceProviderFactory.RegisterProvider(app.ApplicationServices);</em>
&#125;
</code></pre> 
<h4 style="margin-left:0; margin-right:0; text-align:start">增加功能</h4> 
<ul> 
 <li>!2066 feat(#I427JH) 组件<span> </span><code>BootstrapInputBase</code><span> </span>增加<span> </span><code>IsTrim</code><span> </span>参数用于自动去除尾部空格默认值<span> </span><code>false</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2065">#I427JH</a></li> 
 <li>!2065 feat(#I4HR59): 组件<span> </span><code>Alert</code><span> </span>组件增加关闭功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2065">#I4HR59</a></li> 
 <li>!2060 feat(#I4HNZ4): 重构组件<span> </span><code>Tab</code><span> </span>内部标签页显示逻辑<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2060">#I4HNZ4</a></li> 
 <li>!2053 feat(#I4HK6D): 新增组件<span> </span><code>BootstrapBlazorRoot</code><span> </span>用于统一服务组件<span> </span><code>Dialog</code><span> </span><code>Message</code><span> </span><code>Toast</code><span> </span>等<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2053">#I4HK6D</a></li> 
 <li>!2047 feat(#I4HEOM): 组件<span> </span><code>Block</code><span> </span>集成授权框架支持<span> </span><code>Users</code><span> </span><code>Roles</code><span> </span>授权模式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2047">#I4HEOM</a></li> 
 <li>!2045 feat(#I4HCGX): 项目框架增加<span> </span><code>net6.0</code><span> </span>支持<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2045">#I4HCGX</a></li> 
 <li>!2044 feat(#I4HCF3): 组件<span> </span><code>Block</code><span> </span>增加<span> </span><code>Authorized</code><span> </span><code>NotAuthorized</code><span> </span>模板方便使用<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2044">#I4HCF3</a></li> 
 <li>!2042 feat(#I4HAJH): 新增<span> </span><code>Block</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2042">#I4HAJH</a></li> 
 <li>!2035 feat(#I4H5IQ): 底层<span> </span><code>JSInvoke</code><span> </span>增加异步等待<span> </span><code>await</code><span> </span>关键字防止弹窗服务<span> </span><code>DialogService.ShowModal</code><span> </span>方法后跟<span> </span><code>Show</code><span> </span>方法时导致第二次弹窗无法弹出问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2035">#I4H5IQ</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">问题修复</h4> 
<ul> 
 <li>!2068 fix(#I4HS25): 修复<span> </span><code>BootstrapInputBase</code><span> </span>子组件开启<span> </span><code>IsTrim</code><span> </span>后端得到的数据仍有空格问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2068">#I4HS25</a></li> 
 <li>!2064 fix(#I4HQPN): 修复点击<span> </span><code>Menu</code><span> </span>组件<span> </span><code>Tab</code><span> </span>组件首次加载是渲染<span> </span><code>Text</code><span> </span>不正确问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2064">#I4HQPN</a></li> 
 <li>!2055 fix(#I4HL1T): 修复<span> </span><code>TooltipComponentBase</code><span> </span>子类未初始化弹窗即销毁时底层报警问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2055">#I4HL1T</a></li> 
 <li>!2054 fix(#I4HKKA): 修复<span> </span><code>CacheManager</code><span> </span>在不同命名空间下有相同类名的类时导致异常问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2054">#I4HKKA</a></li> 
 <li>!2046 fix(#I4HCWJ): 修复组件<span> </span><code>IpAddress</code><span> </span>客户端脚本报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2046">#I4HCWJ</a></li> 
 <li>!2039 fix(#I4H5L2): 修复组件<span> </span><code>AutoFill</code><span> </span>使用鼠标点击候选项时组件显示文字未更新问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2039">#I4H5L2</a></li> 
 <li>!2029 fix(#I4GVEC): 修复本地化逻辑未搜索当前程序集问题<span> </span><code>v5.17.3</code><span> </span>版本导致 [#I4GVEC] (<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2029">https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2029</a>)</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">更新文档</h4> 
<ul> 
 <li>!2067 doc(#I4HRK4): 更新后台模拟器菜单显示文本<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2067">#I4HRK4</a></li> 
 <li>!2059 doc(#I4HMJU): 更新示例文档目录结构减少层次方便查找<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2059">#I4HMJU</a></li> 
 <li>!2050 doc(#I4HHMQ): 更新文档移除<span> </span><code>!</code><span> </span>可为空断言符号<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2050">#I4HHMQ</a></li> 
 <li>!2038 doc(#I4H5KW): 更新示例<span> </span><code>BootstrapInput</code><span> </span>组件以及子组件设置<span> </span><code>IsSelectAllTextOnFocus</code><span> </span>参数后开启获得焦点自动全选示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2038">#I4H5KW</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">单元测试</h4> 
<ul> 
 <li>!2048 test(#I4HEV0): <code>Block</code><span> </span>组件单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2048">#I4HEV0</a></li> 
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
            