
---
title: 'Bootstrap Blazor 更新版本 5.0.26'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2552'
author: 开源中国
comments: false
date: Fri, 16 Apr 2021 16:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2552'
---

<div>   
<div class="content">
                                                                                            <h4 style="text-align:start"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置近 80 个组件，欢迎大家尝试使用。</span></h4> 
<h4 style="text-align:start">增加功能</h4> 
<ul> 
 <li> <p>!1313 feat(#I3IQKI): <code>Collapse</code> 组件增加 <code>TitleColor</code> 参数 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1313">#I3IQKI</a></p> </li> 
 <li> <p>!1311 feat(#I3IQ1A): <code>MultiSelect</code> 组件支持重置数据源后一并设置已选项 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1311">#I3IQ1A</a></p> </li> 
 <li> <p>!1310 feat(#I3IOAD): <code>Avatar</code> 组件 <code>GetUrlAsync</code> 方法移动到 <code>OnParameterSetAsync</code> 中 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1310">#I3IOAD</a></p> 
  <ol> 
   <li>此改动稍微损失一点性能但是支持表格内动态设置行内 <code>Avatar</code> 组件数据源</li> 
  </ol> </li> 
 <li> <p>!1307 feat(#I3ILXS): <code>EnumExtensions</code> 类增加一个公开方法 <code>ToEnumDisplayName<TEnum></code> 方便代码调用 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1307">#I3ILXS</a></p> </li> 
 <li> <p>!1290 feat(#I3I010): <code>Table</code> 组件 <code>ShowLoading</code> 逻辑重新设计 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1290">#I3I010</a></p> 
  <ol> 
   <li>涵盖  <strong>新建</strong>  <strong>编辑</strong>  <strong>删除</strong>  <strong>搜索</strong>  <strong>刷新</strong>  <strong>过滤</strong>  <strong>翻页</strong> 按钮</li> 
  </ol> </li> 
</ul> 
<h4 style="text-align:start">问题修复</h4> 
<ul> 
 <li>!1317 fix(#I3IVZV): Avatar GetUrlAsync not working after render <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1317">#I3IVZV</a></li> 
 <li>!1316 fix(#I3IVUS): 修复 <code>Display</code> 组件提供 <code>Data</code> 数据源后仍然显示 <code>Value</code> 值问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1316">#I3IVUS</a></li> 
 <li>!1315 fix(#I3ITV3): 修复 <code>CloseOtherTabs</code> <code>CloseAllTabs</code> 两个方法未渲染 UI 问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1315">#I3ITV3</a></li> 
 <li>!1312 fix(#I3IR9J): 修复 <code>Button</code> 组件上一个版本增加 <code>IsAsync</code> 导致图标不能代码更改问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1312">#I3IR9J</a></li> 
 <li>!1304 fix(#I3IGA9): 修复 <code>TitleService</code> 偶尔抛出异常问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1304">#I3IGA9</a></li> 
 <li>!1303 fix(#I3IG3A): 修复 <code>Layout</code> 组件切换页面是输出框报错问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1303">#I3IG3A</a></li> 
 <li>!1299 fix(#I3IA28): 修复重新加载时程序抛出 <code>InvalidOperationException</code> 异常问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1299">#I3IA28</a></li> 
 <li>!1292 fix(#I3I010): 修复 <code>CardUpload</code> 组件删除文件后 <code>UI</code> 未刷新问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1290">#I3I010</a></li> 
</ul> 
<p style="text-align:left">更新历史 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/wikis/v5.0.24?sort_id=3857954">传送门</a></p> 
<h2 style="text-align:left">项目地址</h2> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor">https://gitee.com/LongbowEnterprise/BootstrapBlazor</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor" target="_blank">https://github.com/dotnetcore/BootstrapBlazor</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FBootstrapBlazor%2F%23" target="_blank">https://www.nuget.org/packages/BootstrapBlazor</a></li> 
</ul> 
<p style="text-align:left">BootstrapBlazor 遵循 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/blob/master/LICENSE">Apache-2.0</a> 开源协议，欢迎大家提交 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls">PR</a> 或 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/issues/new">Issue</a>。喜欢可以给个 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/stargazers">Star</a>。</p>
                                        </div>
                                      
</div>
            