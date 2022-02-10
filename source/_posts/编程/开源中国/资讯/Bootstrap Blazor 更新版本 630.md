
---
title: 'Bootstrap Blazor 更新版本 6.3.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8166'
author: 开源中国
comments: false
date: Thu, 10 Feb 2022 09:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8166'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span style="background-color:#ffffff; color:#333333">Bootstrap Blazor 是一款基于 Bootstrap 的 企业级 Blazor UI 组件库，目前内置 100多 个组件，欢迎大家尝试使用。</span></strong></p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">破坏性更新</h4> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4RFA1): 重新设计地理位置查询服务<span> </span><code>IIPLocatorProvider</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2333">#I4RFA1</a><br> <code>Locate</code><span> </span>方法返回可为空<span> </span><code>string</code><span> </span>内部增加注入配置参数<span> </span><code>IPLocatorOption</code><span> </span>接口<span> </span><code>IIPLocator</code><span> </span>增加<span> </span><code>Url</code><span> </span>参数<span> </span><code>6.2.8</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4QXK9): 服务<span> </span><code>WebClientService</code><span> </span>逻辑重构增加<span> </span><code>ClientInfo</code><span> </span>实体类方便用于<span> </span><code>MVVM</code><span> </span>数据绑定<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2316">#I4QXK9</a><br> 服务原有方法<span> </span><code>RetrieveRemoteInfo</code><span> </span>更改为<span> </span><code>GetClientInfo</code>，原服务属性全部移动到<span> </span><code>ClientInfo</code><span> </span>实体类中方便进行数据绑定</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4PZBR): 组件<span> </span><code>Table</code><span> </span>移除参数<span> </span><code>UseInjectDataService</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2297">#I4PZBR</a><br> 组件内部采用就近原则智能推算如查询方法 OnQueryAsync DataService InjectDataService 减少使用者代码量，而且可以自定义局部方法，如只提供 OnQueryAsync 其余方法仍然使用注入数据服务的通用方法 版本<span> </span><code>6.2.4</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(#I4Q0MF): 组件<span> </span><code>Pagination</code><span> </span>每页显示数量下拉框更改为默认居中<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2303">#I4Q0MF</a><span> </span>版本<span> </span><code>6.2.7-beta02</code><br> 原组件默认系统设置居左</p> </li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">增加功能</h4> 
<ul> 
 <li>feat(#I4SYY1): 组件<span> </span><code>ValidateForm</code><span> </span>增加<span> </span><code>OnFieldValueChanged</code><span> </span>回调方法<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2396">#I4SYY1</a></li> 
 <li>feat(#I4SQKN): 增加<span> </span><code>GeolocationService</code><span> </span>服务可用于地理位置定位功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2396">#I4SQKN</a></li> 
 <li>feat(#I4SNXQ): 增加<span> </span><code>DragDrop</code><span> </span>组件<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2393">#I4SNXQ</a></li> 
 <li>feat(#I4SLOR): 组件<span> </span><code>BarcodeReader</code><span> </span>增加<span> </span><code>OnDeviceChanged</code><span> </span>回调方法<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2383">#I4SLG7</a></li> 
 <li>feat(#I4SL49): 组件<span> </span><code>Display</code><span> </span>增加<span> </span><code>TypeResolver</code><span> </span>参数用于解析内部类等实际应用场景<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2378">#I4SL49</a></li> 
 <li>feat(#I4SFT5): 组件<span> </span><code>Table</code><span> </span>内置支持<span> </span><code>CheckboxList<string></code><span> </span>渲染<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2364">#I4SFT5</a></li> 
 <li>refactor(#I4SD6E): 组件<span> </span><code>Layout</code><span> </span>参数<span> </span><code>OnUpdate</code><span> </span>更改为<span> </span><code>OnUpdateAsync</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2361">#I4SD6E</a></li> 
 <li>feat(#I4RYFY): 增加注册服务扩展方法提高<span> </span><code>AddBootstrapBlazor</code><span> </span>代码可读性<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2355">#I4RYFY</a></li> 
 <li>feat(#I4RUA6): 组件<span> </span><code>DropdownWidgetItem</code><span> </span>增加<span> </span><code>Title</code><span> </span>参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2342">#I4RUA6</a></li> 
 <li>feat(#I4RQG7): 组件<span> </span><code>Table</code><span> </span>增加<span> </span><code>SortString</code><span> </span>参数用于多列排序移除<span> </span><code>SortList</code><span> </span>参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2343">#I4RQG7</a><br> <code>SortList</code><span> </span>参数为<span> </span><code>List<string></code><span> </span>使用者需要额外的较多代码实现，<code>SortString</code><span> </span>参数为<span> </span><code>string</code><span> </span>类型使用更方便</li> 
 <li>feat(#I4RKR2): 组件<span> </span><code>Table</code><span> </span>工具栏按钮<span> </span><code>TableToolbarButton</code><span> </span>增加<span> </span><code>IsShow</code><span> </span>参数用于控制是否显示<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2338">#I4RKR2</a></li> 
 <li>feat(#I4RGER): 组件<span> </span><code>TabItem</code><span> </span>增加<span> </span><code>IsShow</code><span> </span>参数<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2337">#I4RGER</a></li> 
 <li>feat(#I4RG4D): 内置百度地理位置定位服务<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2336">#I4RG4D</a><span> </span><code>6.2.8</code></li> 
 <li>feat(#I4RFNP): 组件<span> </span><code>IPLocatorProvider</code><span> </span>配置类<span> </span><code>IPLocatorOption</code><span> </span>参数<span> </span><code>LocatorFactory</code><span> </span>增加<span> </span><code>IServiceProvider</code><span> </span>参数方便使用者获取容器内的服务<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2335">#I4RFNP</a><span> </span><code>6.2.8</code></li> 
 <li>feat(#I4RER0): 增加<span> </span><code>Ajax</code><span> </span>组件用于<span> </span><code>SSR</code><span> </span>模式登录等特殊用途<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2330">#I4RER0</a></li> 
 <li>feat(#I4REU4): 组件<span> </span><code>TreeItem</code><span> </span>增加<span> </span><code>ActiveItem</code><span> </span>参数用于设置当前组件选中的节点<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2332">#I4REU4</a></li> 
 <li>feat(#I4RCYE): 组件<span> </span><code>Table</code><span> </span>增加<span> </span><code>CloseButtonText</code><span> </span>参数用于更改弹窗关闭按钮显示文本<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2329">#I4RCYE</a></li> 
 <li>feat(#I4QYFE): 组件<span> </span><code>Dialog</code><span> </span>增加<span> </span><code>FullScreenSize</code><span> </span>支持全屏弹窗<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2318">#I4QYFE</a></li> 
 <li>feat(#I4QXVD): 组件<span> </span><code>Modal</code><span> </span>增加<span> </span><code>FullScreenSize</code><span> </span>支持全屏弹窗<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2317">#I4QXVD</a></li> 
 <li>feat(#14QWY9): 组件<span> </span><code>Table</code><span> </span>增加对<span> </span><code>ColorPicker</code><span> </span>支持<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2315">#14QWY9</a></li> 
 <li>feat(#I4PQG5): 组件<span> </span><code>Upload</code><span> </span>增加<span> </span><code>Reset</code><span> </span>方法用于清除已上传的文件列表<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2310">#I4PQG5</a></li> 
 <li>feat(#I4QMF1): 增加<span> </span><code>AutoRedirect</code><span> </span>组件可用于实现自动锁屏功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2309">#I4QH0N</a><span> </span>版本<span> </span><code>6.2.7-beta05</code></li> 
 <li>feat(#I4QH0N): 组件<span> </span><code>Dropdown</code><span> </span>内置表单组件时自动显示前置标签<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2308">#I4QH0N</a><span> </span>版本<span> </span><code>6.2.7-beta03</code></li> 
 <li>feat(#I4Q0IK): 页面未提供<span> </span><code>TabItemOptionAttribute</code><span> </span>时使用路由信息作为标签页显示文本防止出现空白标签页<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2302">#I4Q0IK</a><span> </span>版本<span> </span><code>6.2.7-beta02</code></li> 
 <li>feat(#I4Q0CM): 恢复<span> </span><code>NavigateTo</code><span> </span>扩展方法支持同一个页面显示不同名称标签页应用场景<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2301">#I4Q03I</a><span> </span>版本<span> </span><code>6.2.7-beta01</code></li> 
 <li>feat(#I4Q03I): 组件<span> </span><code>Table</code><span> </span>增加<span> </span><code>OnSort</code><span> </span>回调委托参数用于动态设置多列排序功能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2298">#I4Q03I</a><span> </span>版本<span> </span><code>6.2.5</code></li> 
 <li>chore(#I4PXI0): CI&CD docker 镜像增加中文文化设置<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2295">#I4PXI0</a></li> 
 <li>feat(#I4PPQ2): 组件<span> </span><code>Table</code><span> </span>增加<span> </span><code>IsHideFooterWhenNoData</code><span> </span>用于控制无数据时是否显示<span> </span><code>Footer</code><span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2289">#I4PPQ2</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">问题修复</h4> 
<ul> 
 <li>fix(#I4SYD6): 组件<span> </span><code>Select</code><span> </span>支持<span> </span><code>Null</code><span> </span>数据源减少使用者代码量<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2402">#I4SYD6</a></li> 
 <li>refactor(#I4SODP): 组件<span> </span><code>MultiSelect</code><span> </span>优化更新销毁机制<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2394">#I4RER0</a></li> 
 <li>fix(#I4RER0): 修复<span> </span><code>Ajax</code><span> </span>对<span> </span><code>Null</code><span> </span>处理成空字符串问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2382">#I4RER0</a></li> 
 <li>fix(#I4SHOA): 修复<span> </span><code>TableColumn</code><span> </span>设置参数 ｀Rows｀ 渲染成<span> </span><code>Textarea</code><span> </span>组件后布局错位问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2370">#I4SHOA</a></li> 
 <li>fix(#I4SK0X): 修复由支持<span> </span><code>CheckboxList</code><span> </span>更改<span> </span><code>Utility</code><span> </span>类中<span> </span><code>IsCheckboxList</code><span> </span>方法报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2367">#I4SK0X</a><span> </span><code>6.2.9-beta10</code></li> 
 <li>fix(#I4SICI): 修复组件<span> </span><code>CheckboxList</code><span> </span>值为<span> </span><code>string</code><span> </span>类型并且未设置<span> </span><code>Items</code><span> </span>属性时报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2365">#I4SICI</a><span> </span><code>6.2.9-beta09</code></li> 
 <li>fix(#I4RYFC): 修复组件<span> </span><code>DateTimeRange</code><span> </span>在表单内未适配问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2354">#I4RYFC</a></li> 
 <li>fix(#I4RW6K): 修复组件<span> </span><code>Table</code><span> </span>编辑/删除按钮在<span> </span><code>CardView</code><span> </span>模式下始终显示问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2352">#I4RW6K</a><span> </span><code>6.2.9-beta-04</code></li> 
 <li>fix(#I4RW5K): 修复组件<span> </span><code>Skeleton</code><span> </span>骨架屏圆角被遮挡问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2351">#I4RW5K</a></li> 
 <li>fix(#I4RVX7): 修复组件<span> </span><code>Table</code><span> </span>搜索模板中搜索按钮与重置按钮顺序颠倒问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2350">#I4RVX7</a></li> 
 <li>fix(#I4RVWZ): 修复组件<span> </span><code>Card</code><span> </span>未设置<span> </span><code>CardHeader</code><span> </span>模板与<span> </span><code>HeaderText</code><span> </span>时仍显示<span> </span><code>CardHeader</code><span> </span>问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2349">#I4RVWZ</a></li> 
 <li>fix(#I4RVGM): 修复<span> </span><code>Enumerable<TItem></code><span> </span>扩展方法<span> </span><code>Sort</code><span> </span>多列排序不正确问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2348">#I4RVGM</a></li> 
 <li>fix(#I4RV9J): 修复组件<span> </span><code>Table</code><span> </span>通过<span> </span><code>ShowEdit/DeleteCallback</code><span> </span>回调禁用掉行内编辑/删除按钮后工具栏按钮仍然可用问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2346">#I4RV9J</a><br> 禁用掉行内编辑/删除按钮后无法禁用工具栏按钮，点击工具栏按钮后给予相对应的提示不可编辑或者删除选中行</li> 
 <li>fix(#I4RULJ): 组件<span> </span><code>DropdownWidget</code><span> </span>弹出框向右微调<span> </span><code>2px</code><span> </span>保证居中对齐<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2345">#I4RUJ5</a></li> 
 <li>fix(#I4RUJ5): 修复组件<span> </span><code>Tab</code><span> </span>内容越界后被裁剪问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2344">#I4RUJ5</a></li> 
 <li>fix(#I4RQEX): 修复组件<span> </span><code>Table</code><span> </span>在卡片模式下设置固定表头时丢失滚动条问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2341">#I4RQEX</a><span> </span><code>6.2.9-beta02</code></li> 
 <li>fix(#I4RET5): 修复组件<span> </span><code>Table</code><span> </span>固定表头计算高度脚本移除 16px 间隙<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2331">#I4RET5</a></li> 
 <li>fix(#I4R70W): 修复组件<span> </span><code>AutoComplete</code><span> </span>客户端报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2326">#I4QT7M</a></li> 
 <li>fix(#I4QT7M): 修复组件<span> </span><code>Pagination</code><span> </span>每页条目数显示下拉框未居中问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2313">#I4QT7M</a></li> 
 <li>fix(#I4QP5C): 修复组件<span> </span><code>Table</code><span> </span>双击单元格回调报错问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2312">#I4QP5C</a></li> 
 <li>fix(#I4QHL7): 修复组件<span> </span><code>Table</code><span> </span>保存失败后无提示信息问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2311">#I4QHL7</a></li> 
 <li>fix(#I4PVTO): 修复组件<span> </span><code>Table</code><span> </span>设置<span> </span><code>SearchMode.Top</code><span> </span>时自适应高度不正确问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2307">#I4PVTO</a></li> 
 <li>fix(#I4Q0DK): 组件<span> </span><code>Table</code><span> </span>使用<span> </span><code>Items</code><span> </span>作为数据源时报错<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2300">#I4PKOC</a></li> 
 <li>fix(#I4PKOC): 修复组件<span> </span><code>Modal</code><span> </span>导致切换页面时报错问题（手欠移除代码导致）<a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2296">#I4PKOC</a></li> 
 <li>fix(#I4PWKC): 修复组件<span> </span><code>Table</code><span> </span>点击表头过滤时多于一个条件时过滤结果不正确问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2294">#I4PSJO</a></li> 
 <li>fix(#I4PSJO): 修复组件<span> </span><code>Table</code><span> </span>搜索模型中包含枚举类型时及时设置<span> </span><code>CustomerSearchModel</code><span> </span>高级搜索过滤条件不正确问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2293">#I4PSJO</a></li> 
 <li>fix(#I4PM8I): 修复组件<span> </span><code>Table</code><span> </span>设置<span> </span><code>DynamicContext</code><span> </span>时<span> </span><code>DeleteAsync</code><span> </span>回调方法未生效问题<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2292">#I4PM8I</a></li> 
 <li>fix(#I4PPY4): 修复组件<span> </span><code>Table</code><span> </span>当数据集为空集合时<span> </span><code>Footer</code><span> </span>内置聚合函数用于数据合计功能报错<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2291">#I4PPQ2</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">提升性能</h4> 
<ul> 
 <li>perf(#I4QWXW): 重新设计<span> </span><code>Table</code><span> </span>组件明细行展开逻辑减少请流量提搞性能<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2314">#I4QWXW</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">更新文档</h4> 
<ul> 
 <li>doc(#I4T0ZJ): 更新<span> </span><code>IPLocator</code><span> </span>示例文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2403">#I4T0ZJ</a></li> 
 <li>doc(#I4SLTQ): 更新<span> </span><code>Ajax</code><span> </span>组件文档增加<span> </span><code>Goto</code><span> </span>用法<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2386">#I4SLTQ</a></li> 
 <li>doc(#I4SKWJ): 更新<span> </span><code>AutoFill</code><span> </span>组件示例文档增加<span> </span><code>SkipEnter/SkipEsc</code><span> </span>参数说明<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2376">#I4SKWJ</a></li> 
 <li>doc(#I4SKWG): 更新<span> </span><code>AutoComplete</code><span> </span>组件示例文档增加<span> </span><code>SkipEnter/SkipEsc</code><span> </span>参数说明<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2375">#I4SKWG</a></li> 
 <li>doc(#I4SK3J): 更新<span> </span><code>EditorForm</code><span> </span>移除<span> </span><code>IEnumerable<string></code><span> </span>数据类型使用模板渲染<span> </span><code>CheckboxList</code><span> </span>示例已内置无需使用模板<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2368">#I4SK3J</a></li> 
 <li>doc(#I4S1KP): 更新<span> </span><code>BootstrapInput</code><span> </span>组件示例文档增加<span> </span><code>ValidateRules</code><span> </span>介绍<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2356">#I4S1KP</a></li> 
 <li>doc(#I4RQ7S): 更新<span> </span><code>Ajax</code><span> </span>组件示例文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2340">#I4RQ7S</a></li> 
 <li>doc(#I4RFGM): 更新<span> </span><code>IPLocator</code><span> </span>示例文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2334">#I4RFGM</a></li> 
 <li>doc(#I4RCRW): 更新<span> </span><code>Dialog</code><span> </span>组件<span> </span><code>ShowEdit/Search/SaveDialog</code><span> </span>示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2328">#I4RCRW</a></li> 
 <li>doc(#I4R6SO): 更新<span> </span><code>Table</code><span> </span>树状列表示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2325">#I4R6SO</a></li> 
 <li>doc(#I4QZ6Z): 更新<span> </span><code>Table</code><span> </span>组件<span> </span><code>RowButtonTemplate</code><span> </span><code>IsShow</code><span> </span>参数用法<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2322">#I4QZ6Z</a></li> 
 <li>doc(#I4Q910): 更新项目介绍文档<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2306">#I4Q910</a></li> 
 <li>doc(#I4Q8H7): 更新<span> </span><code>Block</code><span> </span>组件登录认证示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2305">#I4Q8H7</a></li> 
 <li>feat(#I4Q8P3): 官网页脚增加系统运行时长信息<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2304">#I4Q8P3</a></li> 
 <li>doc(#I4Q071): 更新<span> </span><code>Table</code><span> </span>组件动态多列排序示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2299">#I4Q071</a></li> 
 <li>doc(#I4PPRR): 更新<span> </span><code>Table</code><span> </span>组件<span> </span><code>Footer</code><span> </span>合计功能示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2290">#I4PPRR</a></li> 
 <li>doc(#I4PNVD): 更新<span> </span><code>Table</code><span> </span>自定义<span> </span><code>SearchModel</code><span> </span>搜索示例<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2288">#I4PNVD</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">单元测试</h4> 
<ul> 
 <li>test(#I4SWEF): 增加<span> </span><code>Timer</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2400">#I4SWEF</a></li> 
 <li>test(#I4SWEE): 增加<span> </span><code>Circle</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2399">#I4SWEE</a></li> 
 <li>test(#I4SOE4): 增加<span> </span><code>MultiSelect</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2395">#I4SMH1</a></li> 
 <li>test(#I4SMS6): 补充<span> </span><code>Select</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2391">#I4SMS6</a></li> 
 <li>test(#I4SMH6): 补充<span> </span><code>Dialog</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2390">#I4SMH1</a></li> 
 <li>test(#I4SMH1): 增加<span> </span><code>TabLink</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2389">#I4SMH1</a></li> 
 <li>test(#I4SLZY): 增加<span> </span><code>Tab</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2388">#I4SLZY</a></li> 
 <li>test(#I4SLZQ): 增加<span> </span><code>Layout</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2387">#I4SLOS</a></li> 
 <li>test(#I4SLOT): 增加<span> </span><code>Card</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2385">#I4SLOS</a></li> 
 <li>test(#I4SLOS): 增加<span> </span><code>BarcodeReader</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2384">#I4SLOS</a></li> 
 <li>test(#I4SL47): 增加<span> </span><code>Display</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2377">#I4SL47</a></li> 
 <li>test(#I4SKW7): 增加<span> </span><code>AutoFill</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2374">#I4SKW7</a></li> 
 <li>test(#I4SKQP): 增加<span> </span><code>AutoComplete</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2372">#I4SKQP</a></li> 
 <li>test(#I4SKQA): 增加<span> </span><code>RadioList</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2371">#I4SKQA</a></li> 
 <li>test(#I4SKPA): 增加<span> </span><code>CheckboxList</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2369">#I4SKPA</a></li> 
 <li>test(#I4SAKJ): 增加<span> </span><code>Ajax</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2360">#I4SAKJ</a></li> 
 <li>test(#I4QZC6): 增加<span> </span><code>AutoRedirect</code><span> </span>单元测试<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2323">#I4QZC6</a></li> 
 <li>test(#I4QZ67): 更新<span> </span><code>Dialog</code><span> </span>组件单元测试提高代码覆盖率<span> </span><a href="https://gitee.com/LongbowEnterprise/BootstrapBlazor/pulls/2321">#I4QZ67</a></li> 
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
            