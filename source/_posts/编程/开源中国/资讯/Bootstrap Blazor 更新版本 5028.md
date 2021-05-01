
---
title: 'Bootstrap Blazor 更新版本 5.0.28'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7598'
author: 开源中国
comments: false
date: Fri, 30 Apr 2021 16:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7598'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <h4 style="text-align:start"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置近 80 个组件，欢迎大家尝试使用。</span></h4> 
   <h4 style="text-align:start">增加功能</h4> 
   <ul> 
    <li>!1363 feat(#I3OT83): 组件内所有获取属性相关代码均支持子类使用 <code>new</code> 关键字覆盖父类属性 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1363">#I3OT83</a></li> 
    <li>!1362 feat(#I29FLZ): 重新设计 <code>Menu</code> 组件内置 <code>SideMenu</code> <code>TopMenu</code> <code>MenuLink</code> 等组件，支持 <code>手风琴</code> <code>收缩/折叠</code> 效果 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1362">#I29FLZ</a></li> 
    <li>!1358 feat(#I3OAUQ): <code>Select</code> 组件支持通过 <code>PlaceHolder</code> 设置可为空默认选项 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1358">#I3OAUQ</a></li> 
    <li>!1357 feat(#I3O7QY): 新增字符串扩展方法 <code>TryConvertTo</code> 可将任意字符串转化为任意类型 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1357">#I3O7QY</a></li> 
    <li>!1356 feat(#I3O56M): <code>CheckboxList</code> 和 <code>MultiSelect</code> 组件支持 <code>List<Guid></code>数据类型 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1356">#I3O56M</a></li> 
    <li>!1348 feat(#I3NM1W): 重新设计 <code>Transfer</code> 组件为泛型组件支持客户端验证 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1348">#I3NM1W</a></li> 
    <li>!1327 feat(#I3JCAS): 增加 <code>Download</code> 组件 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1327">#I3JCAS</a></li> 
    <li>!1326 feat(#I3J9XZ): <code>MultSelect</code> 组件数据源 <code>Items</code> 支持双向绑定 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1326">#I3J9XZ</a></li> 
    <li>!1323 feat(#I3J5C9): <code>Transfer</code> 组件重新设计支持双向绑定 <code>bind-Items</code> 特性 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1323">#I3J5C9</a></li> 
    <li>!1321 feat(#I3J1VX): <code>Display</code> 组件支持可为空布尔类型与空值类型 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1321">#I3J1VX</a></li> 
   </ul> 
   <h4 style="text-align:start">问题修复</h4> 
   <ul> 
    <li>!1366 fix(#I3OVJC): 修复 <code>ValidateForm</code> 组件开启 <code>ValidateAllProperties</code> 属性后 <code>CheckboxList</code> 组件客户端数据有效性检查失效问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1366">#I3OVJC</a></li> 
    <li>!1365 fix(#I3OUQZ): <code>ValidateForm</code> 组件支持复杂类型字段进行客户端数据有效性检查 [#I3OUQZ] (<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1365">https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1365</a>)</li> 
    <li>!1352 fix(#I3O3QP): <code>Tree</code> 组件 <code>ShowCheckbox=true</code> 时复选框左右标签不应该显示 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1352">#I3O3QP</a></li> 
    <li>!1351 fix(#I3MJKW): 修复 <code>InputUpload</code> 组件无法工作问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1351">#I3MJKW</a></li> 
    <li>!1345 fix(#I3NF8X): <code>InputNumber</code> 组件在 <code>Centos</code> 服务器上 <code>wasm</code> 模式下报错问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1345">#I3NF8X</a></li> 
    <li>!1340 fix(#I3IA28): 修复部分客户端切换带 <code>Dialog</code> 组件页面时报错问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1340">#I3IA28</a></li> 
    <li>!1339 fix(#I3MZ03): 修复 <code>Transfer</code> 组件内置到 <code>ValidateForm</code> 组件内时 <code>Checkbox</code> 组件出现 <code>Label</code> 问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1339">#I3MZ03</a></li> 
    <li>!1337 fix(#I3MNBI): 修复 <code>TableCellButton</code> 组件内部触发两次 <code>OnClickWithoutRender</code> 回调方法问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1337">#I3MNBI</a></li> 
    <li>!1325 fix(#I3J8UD): 修复 <code>ValidateForm</code> 表单验证时 <code>ValidationAttribute</code> 派生子类不生效问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1325">#I3J8UD</a></li> 
    <li>!1319 fix(#I3IXZW): 修复 <code>Button</code> 按钮组件在 <code>ValidateForm</code> 中异步提交图标不正确问题 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/1319">#I3IXZW</a> 
     <ol> 
      <li><code>5.0.26</code> 版本导致新 bug</li> 
     </ol> </li> 
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
</div> 
<div id="gtx-trans" style="position: absolute; left: 8px; top: 1308.3px;"> 
 <div class="gtx-trans-icon">
   
 </div> 
</div>
                                        </div>
                                      
</div>
            