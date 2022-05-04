
---
title: 'Bootstrap Blazor 更新版本 6.6.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=380'
author: 开源中国
comments: false
date: Wed, 04 May 2022 10:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=380'
---

<div>   
<div class="content">
                                                                                            <h4 style="margin-left:0; margin-right:0; text-align:start"><strong style="color:#333333"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置 120多 个组件，欢迎大家尝试使用。</span></strong></h4> 
<div style="margin-right:-15px; text-align:start"> 
 <div> 
  <div> 
   <h4 style="margin-left:0; margin-right:0">破坏性更新</h4> 
   <ul> 
    <li>feat(#I534U3): 组件<span> </span><code>Markdown</code><span> </span>改为动态加载资源 引用组件后无需手动添加<span> </span><code>css</code><span> </span><code>js</code><span> </span>等资源链接<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2670">#I534U3</a></li> 
   </ul> 
   <h4 style="margin-left:0; margin-right:0">新增功能</h4> 
   <ul> 
    <li>feat(#I51EQX): 增加组件<span> </span><code>SignaturePad</code><span> </span>用于手写签名<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2622">#I51EQX</a></li> 
    <li>feat(#I51M4O): 增加组件<span> </span><code>SpeechWave</code><span> </span>用于语音识别显示波形图<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2625">#I51M4O</a></li> 
    <li>feat(#I51TLZ): 增加组件<span> </span><code>Synthesizer</code><span> </span>用于语音合成<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2630">#I51TLZ</a></li> 
    <li>feat(#I51LEH): 更新组件<span> </span><code>ImageViewer</code><span> </span>增加鼠标拖动功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2642">#I51LEH</a></li> 
    <li>feat(#I51TFF): 更新组件<span> </span><code>TabItem</code><span> </span>增加实例方法<span> </span><code>SetText</code><span> </span>用于动态更新<span> </span><code>Text</code><span> </span><code>Icon</code><span> </span><code>Closable</code><span> </span>参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2644">#I51LEH</a></li> 
    <li>feat(#I525HA): 增加服务<span> </span><code>ResizeNotificationService</code><span> </span>与组件<span> </span><code>Responsive</code><span> </span>用于网页尺寸变化时触发<span> </span><code>Bootstrap</code><span> </span>断点阀值通知<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2649">#I525HA</a></li> 
    <li>feat(#I52FDR): 增加组件<span> </span><code>BaiduSpeech</code><span> </span>语音服务增加百度语音支持<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2652">#I52FDR</a></li> 
    <li>feat(#175): 更新组件<span> </span><code>Table</code><span> </span>过滤框<span> </span><code>TableFilter</code><span> </span>增加<span> </span><code>ResetAllColumnsFilter</code><span> </span>方法<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor%2Fpull%2F175">#175</a><span> </span>感谢 @wettstein-guebau</li> 
    <li>feat(#I52L17): 更新组件<span> </span><code>Upload</code><span> </span>支持鼠标拖拽<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2662">#I52L17</a></li> 
    <li>feat(#I52PW1): 更新组件<span> </span><code>ImageViewer</code><span> </span>支持手势放大缩小<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2664">#I52PW1</a></li> 
    <li>feat(#I533TP): 更新组件<span> </span><code>IEditor</code><span> </span>接口增加<span> </span><code>LookupStringCompare</code><span> </span>参数用于设置文本比较规则默认<span> </span><code>OrdinalIgnoreCase</code><span> </span>大小写不明感<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2665">#I533TP</a></li> 
    <li>feat(#I537X5): 更新组件<span> </span><code>BarcodeReader</code><span> </span>依赖脚本更改为动态加载<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2671">#I537X5</a></li> 
    <li>feat(#I537YS): 更新组件<span> </span><code>QRCode</code><span> </span>依赖脚本更改为动态加载<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2673">#I537YS</a></li> 
    <li>feat(#I5338U): 更新组件<span> </span><code>EditorForm</code><span> </span>增加参数<span> </span><code>GroupName</code><span> </span><code>GroupOrder</code><span> </span>用于编辑项分组<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2682">#I5338U</a></li> 
    <li>feat(#I53H0O): 更新组件<span> </span><code>Table</code><span> </span>增加参数<span> </span><code>ShowExtendEditButton</code><span> </span><code>ShowExtendDeleteButton</code><span> </span>用于单独控制行内<span> </span><strong>编辑</strong><span> </span>与<span> </span><strong>删除</strong><span> </span>按钮是否显示 默认为<span> </span><strong>true</strong><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2685">#I53H0O</a></li> 
    <li>feat(#I53KLK): 更新组件<span> </span><code>EditorForm</code><span> </span>增加参数<span> </span><code>ShowUnsetGroupItemsOnTop</code><span> </span>用于控制未分组项目是否在头部渲染 默认 false<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2688">#I53H0O</a></li> 
    <li>feat(#I53LM6): 更新组件<span> </span><code>AutoComplete</code><span> </span>增加<span> </span><code>OnSelectedItemChanged</code><span> </span>回调方法仅鼠标点击下拉选项或者回车时触发<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2690">#I53LM6</a></li> 
    <li>feat(#I538WS): 更新组件<span> </span><code>Table</code><span> </span>增加参数<span> </span><code>CollapsedTopSearch</code><span> </span>用于控制顶端搜索栏默认是否收缩 默认 false<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2691">#I538WS</a></li> 
    <li>feat(#I54GH3): 增加扩展方法<span> </span><code>CascadingMenu</code><span> </span>用于将菜单集合进行层次化<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2705">#I54GH3</a></li> 
    <li>feat(#I53ZDH ): 更新组件<span> </span><code>Table</code><span> </span>内置支持<span> </span><code>bool?</code><span> </span>数据类型 可渲染成<span> </span><code>Select<bool></code><span> </span>或者<span> </span><code>NullSwitch</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2709">#I53ZDH</a></li> 
    <li>feat(#I54V9B): 组件支持<span> </span><code>Mac</code><span> </span><code>Ubuntu</code><span> </span>等无<span> </span><code>CultureInfo</code><span> </span>设置系统 默认使用<span> </span><code>en</code><span> </span>文化 可通过配置文件设置<span> </span><code>DefaultCultureInfo</code><span> </span>参数更改默认文化信息<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2712">#I53ZDH</a></li> 
    <li>feat(#I550IB): 组件<span> </span><code>Speech</code><span> </span>配置类<span> </span><code>Options</code><span> </span>支持热更新更改配置文件后无需重启应用刷新即可生效<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2715">#I53ZDH</a></li> 
    <li>feat(#I51YC0): 增加屏幕键盘<span> </span><code>OnScreenKeyboard</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2717">#I51YC0</a></li> 
    <li>feat(#I5544K): 组件内部多语言处理模块<span> </span><code>JsonStringLocalizerFactory</code><span> </span>支持<span> </span><code>BootstrapBlazorOptions</code><span> </span>配置变化时热更新<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2719">#I5544K</a></li> 
    <li>feat(#I5587C): 组件<span> </span><code>AutoFill</code><span> </span>增加<span> </span><code>Debounce</code><span> </span>防抖参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2725">#I5544K</a></li> 
    <li>feat(#I55J3N): 组件<span> </span><code>Card</code><span> </span>增加<span> </span><code>Collapsed</code><span> </span>参数用于设置<span> </span><code>CardHeader</code><span> </span>默认是否收起<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2736">#I55J3N</a></li> 
    <li>feat(#I55KQD): 组件<span> </span><code>Button</code><span> </span>增加<span> </span><code>IsAutoFocus</code><span> </span>自动获得焦点参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2740">#I55KQD</a></li> 
   </ul> 
   <h4 style="margin-left:0; margin-right:0">问题修复</h4> 
   <ul> 
    <li>fix(#I51TKP): 修复组件<span> </span><code>EditorItem</code><span> </span>使用<span> </span><code>Lookup</code><span> </span>不生效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2629">#I51TKP</a></li> 
    <li>fix(#I51WA2): 修复组件<span> </span><code>Markdown</code><span> </span>使用<span> </span><code>bind-Value</code><span> </span>后无法插入内容问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2637">#I51WA2</a></li> 
    <li>fix(#I50WN8): 修复组件<span> </span><code>Table</code><span> </span>模型中有<span> </span><code>[Key]</code><span> </span>标签导致选中行显示不正确问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2643">#I50WN8</a></li> 
    <li>fix(#I521CL): 修复组件<span> </span><code>AutoComplete</code><span> </span>组件验证失败后无法弹出提示框问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2647">#I521CL</a></li> 
    <li>fix(#I52427): 修复组件<span> </span><code>PopConfirmButton</code><span> </span>参数<span> </span><code>Color</code><span> </span>不生效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2648">#I52427</a></li> 
    <li>fix(#174): 修复组件<span> </span><code>Table</code><span> </span>过滤框<span> </span><code>TableFilter</code><span> </span>生成两次问题<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor%2Fpull%2F174">#174</a><span> </span>感谢 @wettstein-guebau</li> 
    <li>fix(#I533H3): 修复组件<span> </span><code>ImageViewer</code><span> </span>鼠标滚动导致图片反转问题<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor%2Fpull%2F2663">#I533H3</a></li> 
    <li>fix(#I5340E): 修复组件<span> </span><code>Upload</code><span> </span><code>ButtonUpload</code><span> </span><code>CardUpload</code><span> </span>粘贴拖拽上传失效问题<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor%2Fpull%2F2666">#I5340E</a></li> 
    <li>fix(#I534TZ): 修复扩展方法<span> </span><code>addLink</code><span> </span>报错问题<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor%2Fpull%2F2669">#I534TZ</a></li> 
    <li>fix(#I546YJ): 修复<span> </span><code>Table</code><span> </span>组件<span> </span><code>ShowTips</code><span> </span>参数翻页后内容不变问题<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor%2Fpull%2F2700">#I546YJ</a></li> 
    <li>fix(#I54VOU): 修复<span> </span><code>Download</code><span> </span>官网报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2714">#I53ZDH</a></li> 
    <li>fix(#I552KB): 修复<span> </span><code>Table</code><span> </span>组件提供<span> </span><code>OnEditAsync</code><span> </span>回调后 保存失败或者取消后 原始数据被更改问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2718">#I552KB</a></li> 
    <li>fix(#I54O4J): 修复<span> </span><code>Markdown</code><span> </span>组件脚本报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2721">#I54O4J</a></li> 
    <li>fix(#I55BRE): 修复<span> </span><code>Tree</code><span> </span>组件点击节点不能改变前置<span> </span><code>Radiobox</code><span> </span><code>Checkbox</code><span> </span>状态问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2726">#I55BRE</a></li> 
    <li>fix(#I55HX9): 修复<span> </span><code>AutoComplete</code><span> </span>组件首次不匹配时不显示<span> </span><code>NoData</code><span> </span>显示问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2734">#I55BRE</a></li> 
    <li>fix(#I55KOT): 修复<span> </span><code>IpAddress</code><span> </span>组件在某些显示上显示不全问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2741">#I55KOT</a></li> 
    <li>fix(#I55L3J): 修复<span> </span><code>AutoComplete</code><span> </span>组件触发两次<span> </span><code>Enter</code><span> </span>回车案件问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2743">#I55L3J</a></li> 
    <li>fix(#I55MCP): 修复<span> </span><code>Table</code><span> </span>组件<span> </span><code>Footer</code><span> </span>内置聚合统计在移动端显示错位问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2745">#I55MCP</a></li> 
   </ul> 
   <h4 style="margin-left:0; margin-right:0">更新文档</h4> 
   <ul> 
    <li>refactor(#I51UCV): 微调<span> </span><code>wasm</code><span> </span>项目模板与<span> </span><code>net6</code><span> </span>默认模板保持一致<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2634">#I51UCV</a></li> 
    <li>doc(#I51WB7): 网站增加语音识别与合成实战示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2638">#I51WB7</a></li> 
    <li>doc(#I52Y49): 更新<span> </span><code>Font Awesome</code><span> </span>图标文档增加样式语句直接复制功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2657">#I52Y49</a></li> 
    <li>doc(#I539ON): 更新<span> </span><code>AutoComplete</code><span> </span>参数说明<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2675">#I539ON</a></li> 
    <li>doc(#I53DQR): 更新<span> </span><code>TableColumn</code><span> </span>参数说明<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2683">#I53DQR</a></li> 
    <li>doc(#I53LUB): 更新<span> </span><code>Table</code><span> </span>参数说明<span> </span><code>ShowAdvancedSearch</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2689">#I53DQR</a></li> 
    <li>doc(#I54780): 更新<span> </span><code>BootsrapInput</code><span> </span>示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2699">#I53DQR</a></li> 
    <li>doc(#I54CVB): 更新<span> </span><code>Speech</code><span> </span>与<span> </span><code>Reconnector</code><span> </span>组件视频教程链接地址<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2703">#I54CVB</a></li> 
    <li>doc(#I54J8T): 更新<span> </span><code>BootstrapBlazorOptions</code><span> </span><code>WebSiteOptions</code><span> </span>支持热更新<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2706">#I54J8T</a></li> 
    <li>doc(#I553ZC): 更新<span> </span><code>Responsive</code><span> </span>组件描述<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2716">#I553ZC</a></li> 
    <li>doc(#I55C6D): 更新弹窗类组件文档增加使用步骤描述<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2727">#I55C6D</a></li> 
    <li>doc(#I54GGV): 更新<span> </span><code>Menu</code><span> </span>组件<span> </span><code>Bottom</code><span> </span>底部布局示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2739">#I54GGV</a></li> 
    <li>doc(#I55LOR): 更新<span> </span><code>Breakpoints</code><span> </span>断点阈值文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2744">#I55LOR</a></li> 
   </ul> 
   <h4 style="margin-left:0; margin-right:0">单元测试</h4> 
   <ul> 
    <li>test(#I51PW6): 增加<span> </span><code>Speech</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2627">#I51PW6</a></li> 
    <li>test(#I51QQC): 增加<span> </span><code>SpeechWave</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2628">#I51QQC</a></li> 
    <li>test(#I51U5H): 增加<span> </span><code>Captcha</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2632">#I51U5H</a></li> 
    <li>test(#I51U7I): 提高<span> </span><code>BootstrapLabel</code><span> </span>单元测试代码覆盖率<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2633">#I51U7I</a></li> 
    <li>test(#I51UDD): 提高<span> </span><code>BootstrapBlazorRoot</code><span> </span>单元测试代码覆盖率<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2635">#I51UDD</a></li> 
    <li>test(#I51UGB): 提高<span> </span><code>Block</code><span> </span>单元测试代码覆盖率<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2636">#I51UGB</a></li> 
    <li>test(#I52Q5P): 更新<span> </span><code>Speech</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2655">#I51UGB</a></li> 
    <li>test(#I531D6): 更新<span> </span><code>TableFilter</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2659">#I531D6</a></li> 
    <li>test(#I531EA): 更新<span> </span><code>Responsive</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2660">#I531EA</a></li> 
    <li>test(#I531V5): 增加<span> </span><code>ShowColumnList</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2661">#I531EA</a></li> 
    <li>test(#I53YFE): 增加<span> </span><code>BrowserNotification</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2694">#I53YFE</a></li> 
    <li>test(#I54A03): 增加<span> </span><code>Reconnector</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2701">#I54A03</a></li> 
    <li>test(#I54N0G): 增加<span> </span><code>WebClientService</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2707">#I54N0G</a></li> 
    <li>test(#I558OR): 增加<span> </span><code>Dragdrop</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2733">#I558OR</a></li> 
    <li>test(#I55MCV): 增加<span> </span><code>Table</code><span> </span>组件<span> </span><code>Footer</code><span> </span>聚合统计单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2746">#I558OR</a></li> 
    <li>test(#I55N6S): 增加<span> </span><code>Table</code><span> </span>组件<span> </span><code>Checkbox</code><span> </span>复选框逻辑单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2747">#I55N6S</a></li> 
   </ul> 
  </div> 
 </div> 
</div> 
<div style="text-align:start"> 
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
                                      
</div>
            