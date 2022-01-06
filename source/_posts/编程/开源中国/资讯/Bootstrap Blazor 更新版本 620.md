
---
title: 'Bootstrap Blazor 更新版本 6.2.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2137'
author: 开源中国
comments: false
date: Thu, 06 Jan 2022 11:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2137'
---

<div>   
<div class="content">
                                                                                            <h4 style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置近 100 个组件，欢迎大家尝试使用。</span></h4> 
<h4 style="margin-left:0; margin-right:0; text-align:start">破坏性更新</h4> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">refactor(#I4P0MT): 表单内组件前置标签由原来的默认四个汉字宽度更改为六个汉字宽度<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2280">#I4P0MT</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">refactor(#I4OZ32): 组件<span> </span><code>Tab</code><span> </span>与<span> </span><code>Layout</code><span> </span>移除<span> </span><code>TabItemTextDictionary</code><span> </span>参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2271">#I4OZ32</a><br> 改用页面级标签<span> </span><code>TabItemOptionAttribute</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4OTDY): 移除<span> </span><code>NavigateTo</code><span> </span>扩展方法<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2267">#I4OTDY</a><br> 由于用此扩展方法生成的<span> </span><code>TabItem</code><span> </span>无法保持标签页状态（丢失<span> </span><code>Text</code>）等属性，改用页面内使用<span> </span><code>TabItemOptionAttribute</code><span> </span>属性替换</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4NAQ4): 组件<span> </span><code>BootstrapDynamicComponent</code><span> </span>参数集合更改为<span> </span><code>IDictionary<string, object?></code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2231">#I4NAN8</a><br> 方便使用者赋值避免触发不可为空检查绿色波浪线</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4NAN8): 组件<span> </span><code>ModalDialog</code><span> </span>内置一个保存按钮默认不显示回调方法为<span> </span><code>OnSaveAsync</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2230">#I4NAN8</a><br> 原<span> </span><code>EditDialog</code><span> </span>组件保存按钮回调方法<span> </span><code>OnSaveAsync</code><span> </span>更改为<span> </span><code>OnEditAsync</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4MSIJ): 组件<span> </span><code>BootstrapInput</code><span> </span>移除对标<span> </span><code>IsGroup</code><span> </span>参数改用<span> </span><code>BootstrapInputGroup</code><span> </span>实现<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2217">#I4MSIJ</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4MP2F): 重新设计<span> </span><code>RowButtonTemplate</code><span> </span>模板内置支持点击按钮后可自动选中本行<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2215">#I4MP2F</a><br> 由原来可任意设置子组件更改为必须为<span> </span><code>ButtonBase</code><span> </span>基类 内置两个类型可供使用<span> </span><code>TableCellButton</code><span> </span>和<span> </span><code>TableCellPopconfirmButton</code><span> </span>稍后可根据需求继续扩充<br> <code>TableCellButton</code><span> </span>增加<span> </span><code>AutoSelectedRowWhenClick</code><span> </span>参数默认为<span> </span><code>True</code><span> </span>点击按钮后自动选中本行，如需要不选中时请设置值为<span> </span><code>false</code><br> 原回调方法<span> </span><code>OnClickCallback</code><span> </span>移除请使用<span> </span><code>OnClick</code><span> </span>或者<span> </span><code>OnClickWithoutRender</code><span> </span>均可以</p> </li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">增加功能</h4> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4PBOF): 组件<span> </span><code>Table</code><span> </span>查询方法参数增加<span> </span><code>AdvanceSearchs</code><span> </span>内部已拼装并且关系的<span> </span><code>SearchModel</code><span> </span>条件集合<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2286">#I4PBOF</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4P9YK): 增加<span> </span><code>EFCore</code><span> </span>多列排序扩展方法<span> </span><code>Sort<TModel></code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2285">#I4P9YK</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4P8MS): 组件<span> </span><code>Table</code><span> </span>增加<span> </span><code>SortList</code><span> </span>参数用于设置多列默认排序<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2284">#I4P8MS</a><br> 例子<span> </span><code>new List<string> &#123; "Name", "Address desc" &#125;</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4P0X5): 新增<span> </span><code>LogoutLink</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2282">#I4P0X5</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4P0U6): 组件<span> </span><code>Table</code><span> </span>增加<span> </span><code>EmptyImage</code><span> </span>参数用户设置无数据时显示的图片<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2281">#I4P0U6</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4P0H1): 组件<span> </span><code>Table</code><span> </span>骨架屏支持<span> </span><code>ShowToolbar</code><span> </span>参数联动<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2277">#I4P0H1</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4P03T): 组件<span> </span><code>Table</code><span> </span>增加<span> </span><code>SearchDialogSize</code><span> </span><code>EditDialogSize</code><span> </span>参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2275">#I4P03T</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4OXMZ): 组件<span> </span><code>Card</code><span> </span>增加<span> </span><code>IsShadow</code><span> </span>参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2270">#I4OXMZ</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4OROX): 组件<span> </span><code>TableCellButton</code><span> </span>增加<span> </span><code>IsShow</code><span> </span>参数用于判断是否显示<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2266">#I4OROX</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4OQMH): 组件<span> </span><code>Pagination</code><span> </span>增加标签自定义参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2265">#I4OQMH</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4OJT2): 组件<span> </span><code>Dropdown</code><span> </span>增加阴影效果<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2264">#I4OJT2</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4O3RX): 组件<span> </span><code>BootstrapInput</code><span> </span>增加<span> </span><code>Readonly</code><span> </span>参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2255">#I4O3RX</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4O3RS): 组件<span> </span><code>Card</code><span> </span>增加<span> </span><code>IsCollapsible</code><span> </span>参数用于开始展开/收缩功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2254">#I4NYAZ</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4O30L): 组件<span> </span><code>Display</code><span> </span>内置到<span> </span><code>ValidateForm</code><span> </span>时双向绑定自动显示标签<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2252">#I4NYAZ</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4NYAZ): 组件<span> </span><code>Table</code><span> </span>列设置<span> </span><code>Lookup</code><span> </span>属性后编辑模板自动使用其作为数据源展示为<span> </span><code>Select</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2251">#I4NYAZ</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4NY9A): 双向绑定组件支持模型私有属性<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2250">#I4NY9A</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4NMID): 新增<span> </span><code>Logout</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2242">#I4NMID</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4NK5N): 组件<span> </span><code>TreeItem</code><span> </span>模板增加默认 flex 布局样式方便二开<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2240">#I4NK5N</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4NK5M): 组件<span> </span><code>Dialog</code><span> </span><code>ShowSaveDialog</code><span> </span>方法增加配置回调委托参数用于设置弹窗参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2239">#I4NK5M</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4NK18): 组件<span> </span><code>Tree</code><span> </span>增加<span> </span><code>OnTreeItemChecked</code><span> </span>回调方法传出当前组件选中的所有节点集合<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2238">#I4NK18</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4NK0F): 组件<span> </span><code>Table</code><span> </span>增加<span> </span><code>Lookup</code><span> </span>类型过滤器<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2236">#I4NK0F</a><br> 当<span> </span><code>TableColumn</code><span> </span>设置<span> </span><code>Lookup</code><span> </span>参数后列头过滤自动取其值作为过滤器候选项</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4NHCY): 组件<span> </span><code>Table</code><span> </span>增加<span> </span><code>TreeIcon</code><span> </span>参数用于更改行小箭头图标<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2235">#I4NBWG</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4NBWG): 组件<span> </span><code>BootstrapDynamicComponent</code><span> </span>静态方法参数可为空方便无参数组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2234">#I4NBWG</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4NBUK): 组件<span> </span><code>Dialog</code><span> </span>新增<span> </span><code>ShowSaveDialog</code><span> </span>泛型方法<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2233">#I4NBUK</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4MZDX): 新增<span> </span><code>SwitchButton</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2222">#I4MZDX</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4MZCQ): 新增<span> </span><code>Redirect</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2221">#I4MZCQ</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4MZCE): 新增<span> </span><code>LinkButton</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2220">#I4MZCE</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4MYK6): 组件<span> </span><code>Divider</code><span> </span>内部增加<span> </span><code>wrap</code><span> </span>节点使自身更加稳定防止被上下节点样式干扰位置<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2219">#I4MYK6</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4MWDG): 组件<span> </span><code>Layout</code><span> </span>增加<span> </span><code>OnAuthorizing</code><span> </span>回调方法用于权限认证框架使用<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2218">#I4MWDG</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4MSIJ): 新增<span> </span><code>BootstrapInputGroup</code><span> </span>组件对标<span> </span><code>input-group</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2217">#I4MSIJ</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4MSHK): 组件<span> </span><code>Block</code><span> </span>增加<span> </span><code>Condition</code><span> </span>参数用于接收变量值作为<span> </span><code>OnQueryCondition</code><span> </span>回调的精简版使用更方便 parameter<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2216">#I4MSHK</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4MMZ2): 组件<span> </span><code>Table</code><span> </span>工具栏按钮增加<span> </span><code>IsEnableWhenSelectedOneRow</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2214">#I4MMZ2</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4MLL7): 组件<span> </span><code>Tab</code><span> </span>关闭全部下拉框增加<span> </span><code>Shadown</code><span> </span>阴影效果<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2213">#I4MLL7</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4M8V8): 组件<span> </span><code>Tree</code><span> </span>支持设置<span> </span><code>IsActive</code><span> </span>默认选中效果<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2210">#I4M8V8</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4M8X7): 组件<span> </span><code>BootstrapBlazorRoot</code><span> </span>内部弹窗组件布局位置重新调整方便自定义弹窗层次关系<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2209">#I4M8X7</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4M8W5): 内置<span> </span><code>Lambda</code><span> </span>表达式解析支持枚举属性与字符串相等搜索查询<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2208">#I4M8W5</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4M7KC): 组件<span> </span><code>Layout</code><span> </span>内置<span> </span><code>ErrorLogger</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2207">#I4M7KC</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4M345): 增加<span> </span><code>IQueryableExtensions</code><span> </span>扩展类方便<span> </span><code>EFCore</code><span> </span>框架<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2204">#I4M345</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4M1SI): 类<span> </span><code>MenuItem</code><span> </span>增加<span> </span><code>Id/ParentId</code><span> </span>属性方便配合数据库使用<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2203">#I4M1SI</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4M1SL): 组件<span> </span><code>Table</code><span> </span>参数<span> </span><code>PageItemSource</code><span> </span>增加默认值<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2202">#I4M1SL</a></p> </li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">问题修复</h4> 
<ul> 
 <li>fix(#I4P1LQ): 修复<span> </span><code>Table</code><span> </span>组件未开启选中行时点击扩展按钮导致行选中问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2283">#I4P1LQ</a></li> 
 <li>fix(#I4OZWN): 组件<span> </span><code>ErrorLogger</code><span> </span>内部处理异常两次问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2274">#I4O26C</a></li> 
 <li>fix(#I4O26C): 修复<span> </span><code>Table</code><span> </span>组件<span> </span><code>OnCellRender</code><span> </span>回调移动端不生效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2258">#I4O26C</a></li> 
 <li>fix(#I4O30Z): 组件<span> </span><code>CardUpload</code><span> </span>设置<span> </span><code>IsSingle</code><span> </span>为<span> </span><code>True</code><span> </span>时移除右侧与底部间隙<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2253">#I4O30Z</a></li> 
 <li>fix(#I3HWSW): 修复<span> </span><code>Utility</code><span> </span>辅助类<span> </span><code>Lambda</code><span> </span>表达式生成属性报二义性错误<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2248">#I3HWSW</a><br> 由于子类使用<span> </span><code>new</code><span> </span>关键字重写父类属性导致</li> 
 <li>fix(#I4N9U1): 修复组件<span> </span><code>Button</code><span> </span>设置<span> </span><code>IsAsync</code><span> </span>为真时回调方法内异常后状态未恢复问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2246">#I4N9U1</a></li> 
 <li>fix(#I4NMI4): 修复组件<span> </span><code>BootstrapInputNumber</code><span> </span>未回调<span> </span><code>OnIncrement/OnDecrement</code><span> </span>方法问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2241">#I4NMI4</a></li> 
 <li>fix(#I4NK0M): 修复组件<span> </span><code>Table</code><span> </span>开启树形结构时过滤器失效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2237">#I4NK0M</a></li> 
 <li>fix(#I4M57S): 修复组件<span> </span><code>Layout</code><span> </span>未级联<span> </span><code>ErrorLogger</code><span> </span>传参问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2206">#I4M57S</a></li> 
 <li>fix(#I4M353): 更新<span> </span><code>Layout</code><span> </span>组件中侧边栏内菜单组件样式防止鼠标悬浮时菜单抖动问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2205">#I4M353</a></li> 
 <li>fix(#I4LVVG): 修复组件<span> </span><code>Table</code><span> </span>显示在编辑弹窗中时<span> </span><code>SearchText</code><span> </span>输入框显示<span> </span><code>Label</code><span> </span>问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2200">#I4LVVF</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">更新文档</h4> 
<ul> 
 <li>doc(#I4OWJT): 解决方案文档使用命名空间新语法 [#I4OWJT] (<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2269">https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2269</a>)</li> 
 <li>doc(#I4OBAA): 更新<span> </span><code>ErrorLooger</code><span> </span>示例文档增加配合<span> </span><code>Layout</code><span> </span>组件使用说明 [#I4NTRJ (https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2259)</li> 
 <li>doc(#I4NTRJ): 更新<span> </span><code>SkeletonTable</code><span> </span>示例文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2245">#I4NTRJ</a></li> 
 <li>doc(#I4NNK5): 更新<span> </span><code>Logout</code><span> </span>示例文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2243">#I4NNK5</a></li> 
 <li>doc(#I4N6JR): 更新<span> </span><code>IDispatchService</code><span> </span>示例文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2229">#I4N6JR</a></li> 
 <li>doc(#I4N6H2): 增加<span> </span><code>LinkButton</code><span> </span>示例文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2227">#I4N6H2</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">单元测试</h4> 
<ul> 
 <li>test(#I4PJME): 增加<span> </span><code>DateTimeRange</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2287">#I4PJME</a></li> 
 <li>test(#I4ODUT): 增加<span> </span><code>Toast</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2261">#I4ODUT</a></li> 
 <li>test(#I4NWBH): 增加<span> </span><code>AmbiguousMatchException</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2249">#I4NWBH</a></li> 
 <li>test(#I4NW9R): 增加<span> </span><code>TitleService</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2247">#I4NW9R</a></li> 
 <li>test(#I4NNYJ): 增加<span> </span><code>Logout</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2244">#I4NNYJ</a></li> 
 <li>test(#I4NATF): 增加<span> </span><code>ModalDialog</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2232">#I4NATF</a></li> 
 <li>test(#I4N6IB): 增加<span> </span><code>LinkButton</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2228">#I4N6IB</a></li> 
 <li>test(#I4N5N6): 增加<span> </span><code>Block</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2223">#I4N5N6</a></li> 
 <li>test(#I4LVVL): 增加<span> </span><code>Drawer</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2201">#I4LVVL</a></li> 
 <li>test(#I4LVVF): 增加<span> </span><code>Utility</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2199">#I4LVVF</a></li> 
 <li>test(#I4LVV7): 增加<span> </span><code>Switch</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2198">#I4LVV7</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">项目地址</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Gitee：<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor">https://gitee.com/LongbowEnterprise/BootstrapBlazor</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnetcore%2FBootstrapBlazor" target="_blank">https://github.com/dotnetcore/BootstrapBlazor</a></li> 
 <li>Nuget：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FBootstrapBlazor%2F%23" target="_blank">https://www.nuget.org/packages/BootstrapBlazor</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">BootstrapBlazor 遵循 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/blob/master/LICENSE">Apache-2.0</a> 开源协议，欢迎大家提交 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls">PR</a> 或 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/issues/new">Issue</a>。喜欢可以给个 <a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/stargazers">Star</a>。</p>
                                        </div>
                                      
</div>
            