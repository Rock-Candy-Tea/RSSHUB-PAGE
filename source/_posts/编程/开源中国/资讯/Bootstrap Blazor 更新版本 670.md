
---
title: 'Bootstrap Blazor 更新版本 6.7.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7557'
author: 开源中国
comments: false
date: Wed, 01 Jun 2022 11:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7557'
---

<div>   
<div class="content">
                                                                                            <h4 style="margin-left:0; margin-right:0; text-align:start"><strong style="color:#333333"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置 120 多 个组件，欢迎大家尝试使用。本次更新增加了工业组件与语音识别与语音合成组件。重点完成了单元测试所有组件代码覆盖率达到了 100%</span></strong></h4> 
<h4 style="margin-left:0; margin-right:0; text-align:start">破坏性更新</h4> 
<ul> 
 <li>feat(#I56OQP):<span> </span><code>BootstrapBlazor</code><span> </span>移除内置<span> </span><code>Editor</code><span> </span>组件移动到<span> </span><code>BootstrapBlazor.SummerNote</code><span> </span>包内<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2765">#I56OQP</a></li> 
 <li>refactor(#I58S7N): 组件内<span> </span><code>ILookUpService</code><span> </span>更改为<span> </span><code>ILookupService</code><span> </span>更改单词拼写<span> </span><code>LookUp</code><span> </span>更改为<span> </span><code>Lookup</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2811">#I58S7N</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">新增功能</h4> 
<ul> 
 <li>feat(#I55NIO): 组件<span> </span><code>ReconnectorOutlet</code><span> </span>增加<span> </span><code>AutoReconnect</code><span> </span>参数用于控制是否开启自动重连机制<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2748">#I55NIO</a></li> 
 <li>feat(#I56GPF): 语音识别组件<span> </span><code>RecognizerOption</code><span> </span>增加<span> </span><code>AutoRecoginzerElapsedMilliseconds</code><span> </span>参数配置默认自动识别时长 默认<span> </span><code>5000</code><span> </span>毫秒<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2762">#I56GPF</a></li> 
 <li>feat(#I56GYE): 语音识别组件<span> </span><code>Callback</code><span> </span>增加状态参数方法使用者控制 UI<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2763">#I56GYE</a></li> 
 <li>feat(#I56JGP): 语音识别组件<span> </span><code>Callback</code><span> </span>更改为可选参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2764">#I56JGP</a></li> 
 <li>feat(#I56Q9E): 新增<span> </span><code>BootstrapBlazor.SummerNote</code><span> </span>组件包提供原<span> </span><code>Editor</code><span> </span>组件所有功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2766">#I56Q9E</a></li> 
 <li>feat(#I56W9J): 语音识别组件增加<span> </span><code>Logger</code><span> </span>输出信息方便定位问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2768">#I56Q9E</a></li> 
 <li>feat(#I575PZ): 组件<span> </span><code>MultiSelect</code><span> </span>增加<span> </span><code>ItemTemplate</code><span> </span>可自定义下拉框选项<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2775">#I575PZ</a></li> 
 <li>feat(#I578CU): 组件<span> </span><code>MultiSelect</code><span> </span>支持通过设置<span> </span><code>GroupName</code><span> </span>进行分组显示<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2777">#I578CU</a></li> 
 <li>feat(#I57PKH): 组件<span> </span><code>Markdonw</code><span> </span>支持内置<span> </span><code>ValidateForm</code><span> </span>进行数据合规性检查<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2788">#I57PKH</a></li> 
 <li>feat(#I57RYM): 组件<span> </span><code>Display</code><span> </span>支持显式设定渲染组件为<span> </span><code>Textarea</code><span> </span>并且自动设置其为只读<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2794">#I57RYM</a></li> 
 <li>feat(#I58J2U): 新增<span> </span><code>Bootstrap.Topology</code><span> </span>组件用户绘制<span> </span><code>HMI</code><span> </span>人机交互图<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2800">#I58J2U</a></li> 
 <li>feat(#I58KV7): 组件<span> </span><code>Topology</code><span> </span>增加<span> </span><code>OnBeforePushData</code><span> </span>回调方法<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2801">#I58KV7</a></li> 
 <li>feat(#I58M7G): 组件<span> </span><code>TopologyItem</code><span> </span>增加<span> </span><code>Title</code><span> </span>参数用于客户端图形显示<span> </span><code>tooltip</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2803">#I58M7G</a></li> 
 <li>feat(#I57D36): 组件<span> </span><code>ImageViewer</code><span> </span>增加<span> </span><code>IsAsync</code><span> </span>参数用于异步加载图片<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2804">#I57D36</a></li> 
 <li>feat(#I58MPF): 组件<span> </span><code>Markdown</code><span> </span>内部更新缓存键值防止冲突被覆盖<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2807">#I58MPF</a></li> 
 <li>feat(#I58SMD): 组件<span> </span><code>RadioList</code><span> </span>支持<span> </span><code>IsButton</code><span> </span>参与渲染成互斥按钮状态<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2812">#I58SMD</a></li> 
 <li>feat(#I5948R): 组件<span> </span><code>Table</code><span> </span>虚拟滚动模式支持手动调用<span> </span><code>QueryAsync</code><span> </span>重新设置数据源<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2816">#I5948R</a></li> 
 <li>feat(#I5969C): 组件<span> </span><code>Topology</code><span> </span>增加<span> </span><code>PushData</code><span> </span>实例方法用于订阅模式使用<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2817">#I5969C</a></li> 
 <li>feat(#I59O45): 新增<span> </span><code>Cherry-Markdown</code><span> </span>腾讯富文本组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2829">#I59O45</a></li> 
 <li>feat(#I5A1R5): 组件<span> </span><code>LinkButton</code><span> </span>基类更改为<span> </span><code>ButtonBase</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2838">#I5A1R5</a></li> 
 <li>feat(#I5A1Z0): 组件<span> </span><code>Divider</code><span> </span>减少一个节点优化渲染大小<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2839">#I5A1Z0</a></li> 
 <li>feat(#I5A59D): 组件<span> </span><code>LinkButton</code><span> </span>更新图片与文字位置<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2840">#I5A59D</a></li> 
 <li>feat(#I5AAU1): 组件<span> </span><code>ButtonBase</code><span> </span>增加<span> </span><code>aria-disabled</code><span> </span>参数符合规范<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2844">#I5AAU1</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">问题修复</h4> 
<ul> 
 <li>fix(#I51TKP): 修复组件<span> </span><code>EditorItem</code><span> </span>使用<span> </span><code>Lookup</code><span> </span>不生效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2629">#I51TKP</a></li> 
 <li>fix(#I55PJ9): 修复组件<span> </span><code>AutoComplete</code><span> </span>组件设置参数<span> </span><code>IsDisabled</code><span> </span>不生效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2753">#I55PJ9</a></li> 
 <li>fix(#I55NBU): 组件<span> </span><code>DatetimePicker</code><span> </span>适配<span> </span><code>InputGroup</code><span> </span>可以内置到组合组件内使用<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2758">#I55NBU</a></li> 
 <li>fix(#I56CL9): 组件<span> </span><code>Table</code><span> </span>搜索功能<span> </span><code>SearchText</code><span> </span>支持全类型自动匹配<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2761">#I56CL9</a></li> 
 <li>fix(#I56TZX ): 组件<span> </span><code>Dialog</code><span> </span><code>ShowModal</code><span> </span>方法更正<span> </span><code>OnClosing</code><span> </span>返回<span> </span><code>false</code><span> </span>导致结果为<span> </span><code>Yes</code><span> </span>问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2767">#I56TZX</a></li> 
 <li>fix(#I55EA6): 组件<span> </span><code>Markdown</code><span> </span>移除<span> </span><code>Value</code><span> </span><code>Html</code><span> </span>双向绑定机制采用<span> </span><code>OnValueChanged</code><span> </span><code>OnHtmlChanged</code><span> </span>修复光标闪烁问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2772">#I55EA6</a></li> 
 <li>fix(#I576DA): 修复组件<span> </span><code>Editor</code><span> </span>脚本报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2776">#I576DA</a></li> 
 <li>fix(#I57AGS): 更新<span> </span><code>Speech</code><span> </span>语音服务优化卡顿问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2780">#I57AGS</a></li> 
 <li>fix(#I58A3O): 修复组件<span> </span><code>DateTimePicker</code><span> </span>组件设置<span> </span><code>ViewMode</code><span> </span>值为<span> </span><code>DateTime</code><span> </span>后无法切换日视图问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2797">#I58A3O</a></li> 
 <li>fix(#I58G2R): 修复弹窗打印按钮表单内容丢失问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2802">#I58G2R</a></li> 
 <li>fix(#I591ZL): 修复组件<span> </span><code>Table</code><span> </span>使用动态<span> </span><code>DynamicObject</code><span> </span>时无法选中行问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2814">#I591ZL</a></li> 
 <li>fix(#I59G4E): 修复组件<span> </span><code>Tab</code><span> </span>在<span> </span><code>Razor</code><span> </span>文件中更改内部<span> </span><code>TabItem</code><span> </span>参数时无法更新<span> </span><code>UI</code><span> </span>问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2826">#I59G4E</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">更新文档</h4> 
<ul> 
 <li>doc(#I568JH): 更新组件使用步骤文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2759">#I568JH</a></li> 
 <li>doc(#I58DIS): 增加<span> </span><code>TabItem</code><span> </span>实例方法<span> </span><code>SetText</code><span> </span>示例代码<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2799">#I58DIS</a></li> 
 <li>doc(#I592BU): 更新<span> </span><code>Topology</code><span> </span>HMI 组件视频教程链接<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2815">#I592BU</a></li> 
 <li>doc(#I596MB): 增加<span> </span><code>Topology</code><span> </span>实战示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2818">#I596MB</a></li> 
 <li>doc(#I59UJE): 增加<span> </span><code>Light</code><span> </span>组件变色与提示框示例代码<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2837">#I59UJE</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">单元测试</h4> 
<ul> 
 <li>test(#I55NYC): 增加<span> </span><code>Table</code><span> </span>组件分页功能单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2750">#I55NYC</a></li> 
 <li>test(#I55SHE): 增加<span> </span><code>Table</code><span> </span>组件工具栏单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2754">#I55SHE</a></li> 
 <li>test(#I55Y6V): 增加<span> </span><code>Table</code><span> </span>组件<span> </span><code>TableColumn</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2757">#I55Y6V</a></li> 
 <li>test(#I56WPV): 增加<span> </span><code>Editor</code><span> </span>组件单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2769">#I56WPV</a></li> 
 <li>test(#I59CHX): 增加<span> </span><code>Table</code><span> </span>组件<span> </span><code>IsTree</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2825">#I59CHX</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">项目地址</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Gitee：<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor">https://gitee.com/LongbowEnterprise/BootstrapBlazor</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor" target="_blank">https://github.com/dotnetcore/BootstrapBlazor</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FBootstrapBlazor%2F%23" target="_blank">https://www.nuget.org/packages/BootstrapBlazor</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">BootstrapBlazor 遵循 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/blob/master/LICENSE">Apache-2.0</a> 开源协议，欢迎大家提交 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls">PR</a> 或 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/issues/new">Issue</a>。喜欢可以给个 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/stargazers">Star</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            