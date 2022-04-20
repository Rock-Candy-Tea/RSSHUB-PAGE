
---
title: 'Bootstrap Blazor 更新版本 6.5.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2618'
author: 开源中国
comments: false
date: Wed, 20 Apr 2022 15:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2618'
---

<div>   
<div class="content">
                                                                                            <h4 style="margin-left:0; margin-right:0; text-align:start"><strong style="color:#333333"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置 100多 个组件，欢迎大家尝试使用。</span></strong></h4> 
<p>破坏性更新</p> 
<ul> 
 <li>feat(#I50GIB): 组件<span> </span><code>Table</code><span> </span>参数<span> </span><code>SearchDialogShowMaximizeButton</code><span> </span><code>EditDialogShowMaximizeButton</code><span> </span>默认值更改为<span> </span><code>true</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2599">#I50GIB</a><br> 组件<span> </span><code>Table</code><span> </span>编辑/搜索 弹窗默认显示最大化按钮</li> 
 <li>refactor(#I502E4): 组件<span> </span><code>DateTimePicker</code><span> </span>使用视图参数<span> </span><code>DatePickerViewModel</code><span> </span>更改为<span> </span><code>DatePickerViewMode</code><span> </span><code>TimePickerCellViewModel</code><span> </span>更改为<span> </span><code>TimePickerCellViewMode</code><span> </span><code>CalendarViewModel</code><span> </span>更改为<span> </span><code>CalendarViewMode</code><span> </span>更正单次拼写错误<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2592">#I502E4</a></li> 
 <li>refactor(#I4ZSNF): 服务<span> </span><code>DialogService</code><span> </span>扩展方法<span> </span><code>ShowSaveDialog</code><span> </span>原参数<span> </span><code>Dictionary<string, object?>? parameters = null</code><span> </span>更改为<span> </span><code>Action<Dictionary<string, object?>>? parametersFactory = null</code><span> </span>回调方式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2584">#I4ZSNF</a></li> 
 <li>refactor(#I4YRMU): 类<span> </span><code>Utility</code><span> </span>扩展方法<span> </span><code>CreateComponentByFieldType</code><span> </span><code>CreateDisplayByFieldType</code><span> </span>移除<span> </span><code>LookupService</code><span> </span>参数精简调用方代码<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2553">#I4YRMU</a></li> 
 <li>refactor(#I4YRI0): 类<span> </span><code>Utility</code><span> </span>扩展方法<span> </span><code>CreateComponentByFieldType</code><span> </span><code>CreateDisplayByFieldType</code><span> </span>移除<span> </span><code>ShowLabel</code><span> </span>参数精简调用方代码<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2552">#I4YRI0</a></li> 
 <li>feat(#I4Y0FS): 所有弹窗由原来的默认<span> </span><code>Large</code><span> </span>更改为<span> </span><code>ExtraExtraLarge</code><span> </span>超超大支持带鱼屏<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2535">#I4Y0FS</a></li> 
 <li>refactor(#I4WVAB): 类<span> </span><code>TableTreeNode</code><span> </span>移除参数<span> </span><code>HasKey</code><span> </span>属性<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2499">#I4WVAB</a></li> 
 <li>refactor(#I4WLN7): 组件<span> </span><code>DynamicElement</code><span> </span>移除参数<span> </span><code>GenerateElement</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2493">#I4WLN7</a></li> 
 <li>refactor(#I4WI7I): 弹窗服务<span> </span><code>SwalService</code><span> </span>参数<span> </span><code>SwalOption</code><span> </span>移除<span> </span><code>IsConfirm</code><span> </span>参数减少使用者代码量<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2490">#I4WI7I</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">新增功能</h4> 
<ul> 
 <li>feat(#I51EOA): 增加<span> </span><code>Speech</code><span> </span>语音识别组件将语音转化为文字<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2620">#I51EOA</a></li> 
 <li>feat(#I5153N): 组件<span> </span><code>CardUpload</code><span> </span>增加图片预览功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2618">#I5153N</a></li> 
 <li>feat(#I514V4): 组件<span> </span><code>Image</code><span> </span>增加<span> </span><code>PrevList</code><span> </span>大图预览功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2617">#I514V4</a></li> 
 <li>feat(#I512OY): 组件<span> </span><code>Image</code><span> </span>增加<span> </span><code>HandleError</code><span> </span>功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2616">#I512OY</a></li> 
 <li>feat(#I512OS): 组件<span> </span><code>Image</code><span> </span>增加<span> </span><code>PlaceHolderTemplate</code><span> </span>模板功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2615">#I512OS</a></li> 
 <li>feat(#I512B7): 增加<span> </span><code>Image</code><span> </span>组件用于显示图片<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2614">#I512B7</a></li> 
 <li>feat(#I50XD6): 组件<span> </span><code>Tree</code><span> </span>增加<span> </span><code>GetCheckedItems</code><span> </span>实例方法方便获取当前<span> </span><code>Tree</code><span> </span>所有选中的节点<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2608">#I50XD6</a></li> 
 <li>feat(#I50UHM): 组件<span> </span><code>Editor</code><span> </span>增加<span> </span><code>DoMethodAsync</code><span> </span>实例方法<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2607">#I50UHM</a></li> 
 <li>feat(#I4Y0EB): 组件<span> </span><code>Table</code><span> </span>编辑/搜索弹窗 设置<span> </span><code>ScrollingDialogContent</code><span> </span>固定弹窗<span> </span><code>Footer</code><span> </span>功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2594">#I4Y0EB</a></li> 
 <li>feat(#I4Z2SE): 增加<span> </span><code>FAIconList</code><span> </span>组件提供<span> </span><code>FontAwesome</code><span> </span>图标选择功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2585">#I4ZSNO</a></li> 
 <li>feat(#I4ZSNF): 服务<span> </span><code>DialogService</code><span> </span>增加<span> </span><code>ShowCloseDialog</code><span> </span>扩展方法<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2584">#I4ZSNF</a></li> 
 <li>feat(#I4ZSLV): 组件<span> </span><code>ButtonBase</code><span> </span>增加<span> </span><code>ShowTooltip/RemoveTooltip</code><span> </span>实例方法方便使用者调用提示栏功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2583">#I4ZSLV</a></li> 
 <li>feat(#I4ZS5O): 移除内置样式<span> </span><code>table-modal-footer</code><span> </span>复用<span> </span><code>modal-footer</code><span> </span>减少弹窗使用者样式代码<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2582">#I4YW36</a></li> 
 <li>feat(##I4ZN9E): 组件<span> </span><code>BootstrapInput</code><span> </span>增加<span> </span><code>IsSelectAllTextOnEnter</code><span> </span>参数用于回车选中所有文字<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2580">#I4YW36</a></li> 
 <li>feat(#I4YW36): 特性<span> </span><code>AutoGenerateColumn</code><span> </span>支持<span> </span><code>ShowLabelTooltip</code><span> </span>参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2557">#I4YW36</a></li> 
 <li>feat(#I4YVGQ): 组件<span> </span><code>Dialog</code><span> </span>增加<span> </span><code>ShowValidateFormDialog</code><span> </span>扩展方法方便弹出<span> </span><code>ValidateForm</code><span> </span>表单的弹窗<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2556">#I4YVGQ</a></li> 
 <li>feat(#I4YNCG): 表单组件以及<span> </span><code>TableColumn</code><span> </span><code>EditorItem</code><span> </span>增加<span> </span><code>ShowLabelTooltip</code><span> </span>参数 用于显示标签太长时被裁剪后鼠标悬浮时显示<span> </span><code>Tooltip</code><span> </span>提示栏<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2554">#I4YNCG</a></li> 
 <li>feat(#I4YMFK): 组件<span> </span><code>ValidateForm</code><span> </span>显示标签增加<span> </span><code>title</code><span> </span>标签支持鼠标悬停提示<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2550">#I4YMFK</a></li> 
 <li>feat(#I4YL4D): 组件<span> </span><code>MessageOption</code><span> </span>增加参数<span> </span><code>OnDismiss</code><span> </span>回调委托用于<span> </span><code>MesssageItem</code><span> </span>关闭回调<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2547">#I4YEXU</a></li> 
 <li>feat(#I4YEXU): 组件<span> </span><code>Layout</code><span> </span>增加手风琴效果参数<span> </span><code>IsAccordion</code><span> </span>设定<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2545">#I4YEXU</a></li> 
 <li>feat(#I4Y6OH): 组件<span> </span><code>GeoLocation</code><span> </span>增加持续定位功能可用于导航开发<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2541">#I4Y6OH</a></li> 
 <li>feat(#I4Y3QG): 组件<span> </span><code>Dialog</code><span> </span>全屏弹窗支持<span> </span><code>ExtraExtraLarge</code><span> </span>样式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2540">#I4Y3QG</a></li> 
 <li>feat(#I4Y2KZ): 组件<span> </span><code>Dropdown</code><span> </span>支持<span> </span><code>ExtraExtraLarge</code><span> </span>样式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2539">#I4Y2KZ</a></li> 
 <li>feat(#I4Y2JH): 组件<span> </span><code>Button</code><span> </span>支持<span> </span><code>ExtraExtraLarge</code><span> </span>样式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2538">#I4Y24F</a></li> 
 <li>feat(#I4Y2BM): 组件<span> </span><code>Checkbox</code><span> </span>支持<span> </span><code>ExtraExtraLarge</code><span> </span>样式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2537">#I4Y24F</a></li> 
 <li>feat(#I4Y24F): 组件<span> </span><code>Avatar</code><span> </span>支持<span> </span><code>ExtraExtraLarge</code><span> </span>样式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2536">#I4Y24F</a></li> 
 <li>feat(#I4Y0FS): 增加<span> </span><code>ExtraExtraLarge</code><span> </span>超超大样式支持带鱼屏<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2535">#I4Y0FS</a></li> 
 <li>feat(#I4XOJE): 增加<span> </span><code>ILookUpService</code><span> </span>数据服务用于关联外键数据<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2527">#I4XOJE</a></li> 
 <li>feat(#I4XHT5): 组件<span> </span><code>InputGroup</code><span> </span>兼容<span> </span><code>Select</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2519">#I4XHT5</a></li> 
 <li>feat(#I4U3DX): 组件<span> </span><code>Select</code><span> </span>下拉框内容过多时自动滚动到选项值<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2517">#I4XGLY</a></li> 
 <li>feat(#I4XGLY): 组件<span> </span><code>BootstrapInputGroupLabel</code><span> </span>适配<span> </span><code>ValidateForm</code><span> </span>组件内置判断是<span> </span><code>input-group</code><span> </span>内部标签还是属性标签<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2515">#I4XGLY</a></li> 
 <li>feat(#I4XDLI): 增加<span> </span><code>SkeletonTree</code><span> </span>骨架屏组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2513">#I4XDLI</a></li> 
 <li>feat(#I4XBU1): 组件<span> </span><code>WebClient</code><span> </span>属性<span> </span><code>Device</code><span> </span>更改为<span> </span><code>WebClientDeviceType</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2512">#I4XBU1</a></li> 
 <li>feat(#I4X736): 扩展方法<span> </span><code>GenerateValueChanged</code><span> </span>公开方便项目中动态创建回调<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2507">#I4X736</a></li> 
 <li>feat(#I4X3SG): 组件<span> </span><code>Tab</code><span> </span>增加<span> </span><code>ButtonTemplate</code><span> </span>提供扩展按钮功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2506">#I4X3SG</a></li> 
 <li>feat(#I4X067): 组件<span> </span><code>Table</code><span> </span>绑定复杂属性时支持过滤与排序功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2502">#I4X067</a></li> 
 <li>feat(#I4WV52): 工具类<span> </span><code>Utility</code><span> </span>增加<span> </span><code>GetKeyValue</code><span> </span>方法用于获取<span> </span><code>[KeyAttribute]</code><span> </span>标记属性值<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2497">#I4WV52</a></li> 
 <li>feat(#I4WM94): 组件<span> </span><code>PopConfirmButton</code><span> </span>增加<span> </span><code>IsLink</code><span> </span>参数使用<span> </span><code>A</code><span> </span>标签进行组件渲染<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2494">#I4W9YF</a></li> 
 <li>feat(#I4WEZR): 组件<span> </span><code>TableColumn</code><span> </span>支持复杂类型属性<span> </span><code>bind-Field="context.Foo.Dummy.Cat.Name"</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2479">#I4W9YF</a></li> 
 <li>feat(#I4W9YF): 组件<span> </span><code>Camera</code>增加<span> </span><code>videoWidth</code><span> </span><code>videoHeight</code><span> </span>参数用于设置视频窗口大小<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2478">#I4W9YF</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">问题修复</h4> 
<ul> 
 <li>fix(#I51EP5): 组件<span> </span><code>Transfer</code><span> </span>右侧数据移动到左侧时<span> </span><code>Value</code><span> </span>不正确问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2611">#I511VH</a></li> 
 <li>fix(#I511VH): 组件<span> </span><code>Table</code><span> </span>使用动态<span> </span><code>DataTable</code><span> </span>作为数据源时无法使用删除操作超过两次<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2611">#I511VH</a></li> 
 <li>fix(#I50NJX): 组件<span> </span><code>RadioList</code><span> </span>内部增加<span> </span><code>FormatValueAsString</code><span> </span>修复绑定<span> </span><code>SelectedItem</code><span> </span>时内部处理不正确问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2604">#I50NJX</a></li> 
 <li>fix(#I506W3): 组件<span> </span><code>MultiSelect</code><span> </span>设置<span> </span><code>Min/Max</code><span> </span>验证失效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2595">#I506W3</a></li> 
 <li>fix(#I500DE): 组件<span> </span><code>DateTimeRange</code><span> </span>未设置<span> </span><code>Value</code><span> </span>参数时报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2593">#I500DE</a></li> 
 <li>fix(#I5021K): 组件<span> </span><code>InputUpload</code><span> </span>浏览与删除按钮样式重复问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2591">#I5021K</a></li> 
 <li>fix(#I4Y6AR): 组件<span> </span><code>Table</code><span> </span>组件在<span> </span><code>InCell</code><span> </span>模式下编辑单元格后数据恢复问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2577">#I4Y6AR</a></li> 
 <li>fix(#I4ZBA2): 组件<span> </span><code>MultiSelect</code><span> </span>组件搜索结果选中状态显示不正确问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2575">#I4ZBA2</a></li> 
 <li>fix(#I4YDWI): 组件<span> </span><code>Table</code><span> </span><code>Excel</code><span> </span>动态模式抛异常问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2544">#I4YDWI</a></li> 
 <li>fix(#I4XZDD): 组件<span> </span><code>Switch</code><span> </span>设置<span> </span><code>IsReadonlyWhenEdit</code><span> </span>丢失显示文本问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2534">#I4XZDD</a></li> 
 <li>fix(#I4XVKU): 组件<span> </span><code>Light</code><span> </span>未支持自定义<span> </span><code>class</code><span> </span>样式问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2531">#I4XVKU</a></li> 
 <li>fix(#I4XPYY): 组件<span> </span><code>Input</code><span> </span>在弹窗内无法自动获得焦点问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2530">#I4XPYY</a></li> 
 <li>fix(#I4XJ5M): 组件<span> </span><code>Table</code><span> </span>行内<span> </span><code>TableCellButton</code><span> </span>属性<span> </span><code>IsDisabled</code><span> </span>未生效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2520">#I4XJ5M</a></li> 
 <li>fix(#I4U9JM): 组件<span> </span><code>Tree</code><span> </span>增加骨架屏用于异步加载大数据<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2514">#I4U9JM</a></li> 
 <li>fix(#I4X9JC): 组件<span> </span><code>DateTimePicker</code><span> </span>增加时间溢出检查<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2510">#I4X9JC</a></li> 
 <li>fix(#I4WV6R): 组件<span> </span><code>Table</code><span> </span>工具栏编辑等按钮在未选择行时仍然可用问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2498">#I4WV6R</a></li> 
 <li>fix(#I4WSEI): 组件<span> </span><code>Select</code><span> </span>数据项<span> </span><code>Items</code><span> </span>中无当前选项值时<span> </span><code>Value</code><span> </span>值不正确问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2495">#I4WG4N</a></li> 
 <li>fix(#I4WG4N): 组件<span> </span><code>InputUpload</code><span> </span>绑定<span> </span><code>string</code><span> </span>类型是不显示文件名问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2488">#I4WG4N</a></li> 
 <li>fix(#I4WFYV): 组件<span> </span><code>PopConfirmButton</code><span> </span>移除<span> </span><code>sealed</code><span> </span>关键字允许集成扩展本组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2487">#I4WAHK</a></li> 
 <li>fix(#I4WAHK): 组件<span> </span><code>Camera</code><span> </span>移除<span> </span><code>Fill</code><span> </span>填充方式使用者可以使用样式自定义填充方式<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2482">#I4WAHK</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">更新文档</h4> 
<ul> 
 <li>doc(#I4UCAK): 更新<span> </span><code>Card</code><span> </span>示例文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2600">#I4UCAK</a></li> 
 <li>doc(#I4ZXNM): 更新<span> </span><code>Tree</code><span> </span>组件<span> </span><code>IsCollapsed</code><span> </span>参数说明与示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2587">#I4WAFR</a></li> 
 <li>doc(#I4YUTT): 更新<span> </span><code>IpAddress</code><span> </span>组件到表单组件分类内<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2555">#I4WAFR</a></li> 
 <li>doc(#I4WAFR): 更新<span> </span><code>Camera</code><span> </span>组件示例文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2481">#I4WAFR</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">单元测试</h4> 
<ul> 
 <li>test(#I50NJ3): 增加<span> </span><code>Validator</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2603">#I50NJ3</a></li> 
 <li>test(#I501DL): 增加<span> </span><code>TimePicker</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2590">#I501DL</a></li> 
 <li>test(#I500N7): 增加<span> </span><code>ClipboardService</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2589">#I500N7</a></li> 
 <li>test(#I500MQ): 增加<span> </span><code>FAIconList</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2588">#I500MQ</a></li> 
 <li>test(#I4ZRIP): 增加<span> </span><code>Table</code><span> </span><code>Search</code><span> </span>功能单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2581">#I4ZRIP</a></li> 
 <li>test(#I4ZMWB): 增加<span> </span><code>BootstrapBlazorAuthorizeView</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2578">#I4ZMWB</a></li> 
 <li>test(#I4ZHTE): 增加<span> </span><code>Geolocation</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2576">#I4ZHTE</a></li> 
 <li>test(#I4ZA0N): 增加<span> </span><code>Input</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2573">#I4ZA0N</a></li> 
 <li>test(#I4ZA05): 增加<span> </span><code>DropdownWidget</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2572">#I4ZA05</a></li> 
 <li>test(#I4Z9ZV): 增加<span> </span><code>FullScreen</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2571">#I4Z9ZV</a></li> 
 <li>test(#I4Z9XQ): 增加<span> </span><code>Toast</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2570">#I4Z2WF</a></li> 
 <li>test(#I4Z9W7): 增加<span> </span><code>Slider</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2569">#I4Z2WF</a></li> 
 <li>test(#I4Z2WT): 增加<span> </span><code>Nav</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2568">#I4Z2WF</a></li> 
 <li>test(#I4Z2WF): 增加<span> </span><code>Skeleton</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2567">#I4Z2WF</a></li> 
 <li>test(#I4Z2W6): 增加<span> </span><code>HandWritten</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2566">#I4Z2W6</a></li> 
 <li>test(#I4Z2VY): 增加<span> </span><code>IpLocator</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2565">#I4Z2VY</a></li> 
 <li>test(#I4Z2U3): 增加<span> </span><code>Rate</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2564">#I4Z2U3</a></li> 
 <li>test(#I4Z2UI): 增加<span> </span><code>LogoutLink</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2563">#I4Z2UI</a></li> 
 <li>test(#I4Z2TQ): 增加<span> </span><code>Search</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2561">#I4YYRX</a></li> 
 <li>test(#I4Z2SM): 增加<span> </span><code>TextArea</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2560">#I4YYRX</a></li> 
 <li>test(#I4YYRX): 增加<span> </span><code>Collapse</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2558">#I4YYRX</a></li> 
 <li>test(#I4YN9P): 增加<span> </span><code>IpAddress</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2551">#I4YN9P</a></li> 
 <li>test(#I4YLKC): 增加<span> </span><code>ListView</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2549">#I4YLKC</a></li> 
 <li>test(#I4YL54): 增加<span> </span><code>Message</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2548">#I4YL54</a></li> 
 <li>test(#I4YJLL): 增加<span> </span><code>Download</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2546">#I4YJLL</a></li> 
 <li>test(#I4YD5R): 增加<span> </span><code>Editor</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2542">#I4YD5R</a></li> 
 <li>test(#I4XYP2): 增加<span> </span><code>Cascader</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2532">#I4XYP2</a></li> 
 <li>test(#I4XPYV): 增加<span> </span><code>EditorForm</code><span> </span>只读属性渲染成<span> </span><code>Display</code><span> </span>组件单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2529">#I4XOJ0</a></li> 
 <li>test(#I4XOJ0): 增加<span> </span><code>Captcha</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2528">#I4XOJ0</a></li> 
 <li>test(#I4XKX7): 增加<span> </span><code>Camera</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2522">#I4XKX7</a></li> 
 <li>test(#I4X05H): 增加<span> </span><code>Dropdown</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2503">#I4X05H</a></li> 
 <li>test(#I4WF7Y): 增加<span> </span><code>Breadcrumb</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2485">#I4WF7Y</a></li> 
 <li>test(#I4WF7U): 增加<span> </span><code>Split</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2484">#I4WF7U</a></li> 
 <li>test(#I4W9WY): 增加<span> </span><code>ValidateForm</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2480">#I4VXYM</a></li> 
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
            