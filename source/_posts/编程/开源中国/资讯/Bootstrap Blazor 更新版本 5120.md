
---
title: 'Bootstrap Blazor 更新版本 5.12.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2929'
author: 开源中国
comments: false
date: Thu, 23 Sep 2021 09:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2929'
---

<div>   
<div class="content">
                                                                                            <h4 style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置近 100 个组件，欢迎大家尝试使用。</span></h4> 
<p><strong style="color:#333333">发布时间 2021-9-23 V5.12.0</strong></p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">破坏性更新</h4> 
<ul> 
 <li>!1875 feat(#I4B5EO): 接口<span> </span><code>IEditorItem</code><span> </span>属性<span> </span><code>Data</code><span> </span>变更为<span> </span><code>Items</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1875">#I4B2A3</a></li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start"><code>IEditorItem</code><span> </span>接口由原来的<span> </span><code>Data</code><span> </span>更改为<span> </span><code>Items</code><span> </span>统一参数名称方便理解</p> 
<ul> 
 <li>!1868 feat(#I4AET9): 组件<span> </span><code>PrintButton</code><span> </span>更改参数名称支持弹窗打印与整页面打印<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1862">#I4A2IT</a></li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">组件<span> </span><code>DialogOption</code><span> </span><code>ModalDialog</code><span> </span>参数变化如下：</p> 
<pre style="text-align:start"><code><span style="color:#008080">1</span>. `ShowPrintView` 变更为 `ShowPrintButton`
<span style="color:#008080">2</span>. `PrintViewButtonText` 变更为 `PrintButtonText`
<span style="color:#008080">3</span>. 新增参数 `ShowPrintButtonInHeader`
</code></pre> 
<h4 style="margin-left:0; margin-right:0; text-align:start">增加功能</h4> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">!1888 feat(#I4BEXP): 全局配置<span> </span><code>BootstrapBlazorOption</code><span> </span>增加参数<span> </span><code>DefaultCultureInfo</code><span> </span>方便设置在未启用多语言时设置默认文化<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1885">#I4BAQS</a></p> 
  <ol style="list-style-type:lower-roman"> 
   <li>项目配置文件<span> </span><code>appsettings.json</code><span> </span>文件中配置如下：</li> 
  </ol> </li> 
</ul> 
<pre style="text-align:start"><code><span style="color:#dd1144">"WebsiteOptions"</span>: &#123;
    <span style="color:#dd1144">"DefaultCultureInfo"</span>: <span style="color:#dd1144">"zh"</span>
&#125;
</code></pre> 
<pre style="text-align:start"><code><span>2. </span>代码中设置  
</code></pre> 
<pre style="text-align:start"><code><strong style="color:#333333">public</strong> <strong style="color:#333333">void</strong> ConfigureServices(IServiceCollection services)
&#123;
    services.AddBootstrapBlazor(<strong style="color:#333333">options</strong> =>
    &#123;
        <em>// 设置默认文化为中文</em>
        <strong style="color:#333333">options</strong>.DefaultCultureInfo = <span style="color:#dd1144">"zh"</span>;
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>!1885 feat(#I4BAQS): 组件<span> </span><code>Checkbox</code><span> </span>增加标签最大宽度防止溢出<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1885">#I4BAQS</a></li> 
 <li>!1882 feat(#I4BAMI): 组件<span> </span><code>MultiSelect</code><span> </span>增加最大高度默认样式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1882">#I4BAMI</a></li> 
 <li>!1880 feat(#I4B7W5): 组件<span> </span><code>Table</code><span> </span>渲染<span> </span><code>bool</code><span> </span>数据类型时默认使用<span> </span><code>Switch</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1880">#I4B7W5</a></li> 
 <li>!1878 feat(#I4B642): 组件<span> </span><code>Table</code><span> </span><code>Excel</code><span> </span>模式下支持<span> </span><code>OnSaveAsync</code><span> </span>更新模型<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1878">#I4B642</a></li> 
 <li>!1876 feat(#I4B5NZ): 组件<span> </span><code>Table</code><span> </span><code>Excel</code><span> </span>模式下支持<span> </span><code>OnQueryAsync</code><span> </span>获取数据集<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1876">#I4B5NZ</a></li> 
 <li>!1873 feat(#I4B2A3): 组件<span> </span><code>Table</code><span> </span><code>Excel</code><span> </span>模式下内置<span> </span><code>enum</code><span> </span>类型渲染成<span> </span><code>Select</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1873">#I4B2A3</a></li> 
 <li>!1872 feat(#I4B23E): 组件<span> </span><code>Table</code><span> </span><code>Excel</code><span> </span>模式下内置<span> </span><code>bool</code><span> </span>类型渲染成<span> </span><code>Switch</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1872">#I4B23E</a></li> 
 <li>!1871 feat(#I4B1YM): 组件<span> </span><code>Table</code><span> </span>增加<span> </span><code>Excel</code><span> </span>模式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1869">#I4B1YM</a></li> 
 <li>!1869 feat(#I4AIEI): 组件<span> </span><code>PrintButton</code><span> </span>移除背景遮罩增强用户体验完善文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1869">#I4AIEI</a></li> 
 <li>!1868 feat(#I4AET9): 组件<span> </span><code>PrintButton</code><span> </span>增加智能分析打印的内容支持<span> </span><code>ModalHeader</code><span> </span><code>ModalFooter</code><span> </span><code>Page</code><span> </span>中使用<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1862">#I4A2IT</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">问题修复</h4> 
<ul> 
 <li>!1889 fix(#I4BEZN): 修复组件<span> </span><code>DateTimeRange</code><span> </span>首次加载时未设置时间范围问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1889">#I4BEZN</a></li> 
 <li>!1887 fix(#I4BEXB): 修复组件<span> </span><code>TreeItem</code><span> </span>由于<span> </span><code>Text</code><span> </span>太长导致折行问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1887">#I4BEXB</a></li> 
 <li>!1886 fix(#I49905): 修复组件<span> </span><code>Menu</code><span> </span>二级菜单展开后<span> </span><code>wasm</code><span> </span>模式报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1886">#I49905</a></li> 
 <li>!1874 fix(#I4ASEJ): 修复组件<span> </span><code>Table</code><span> </span>开启<span> </span><code>AutoGenerateColumns</code><span> </span>后不触发<span> </span><code>OnCellRender</code><span> </span>回调问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1874">#I4ASEJ</a></li> 
 <li>!1870 fix(#I4AEMR): 修复组件<span> </span><code>Transfer</code><span> </span>开启搜索后内容高度不正确问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1870">#I4AEMR</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">提升性能</h4> 
<h4 style="margin-left:0; margin-right:0; text-align:start">更新示例</h4> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">!1881 doc(#I4B7W9): 组件<span> </span><code>Table</code><span> </span>更新多表头合并排序与过滤示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1881">#I4B7W9</a></p> 
<h4 style="margin-left:0px; margin-right:0px; text-align:left">项目地址</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Gitee：<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor">https://gitee.com/LongbowEnterprise/BootstrapBlazor</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor" target="_blank">https://github.com/dotnetcore/BootstrapBlazor</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FBootstrapBlazor%2F%23" target="_blank">https://www.nuget.org/packages/BootstrapBlazor</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">BootstrapBlazor 遵循 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/blob/master/LICENSE">Apache-2.0</a> 开源协议，欢迎大家提交 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls">PR</a> 或 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/issues/new">Issue</a>。喜欢可以给个 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/stargazers">Star</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            