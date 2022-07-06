
---
title: '腾讯企业级设计体系 TDesign 发布 2022.7 第一周更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4665'
author: 开源中国
comments: false
date: Wed, 06 Jul 2022 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4665'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">TDesign 是一款诞生于腾讯内部、拥有完整的设计价值观和视觉风格指南的企业级设计体系，同时提供了丰富的设计资源，在设计体系基础上产出基于 Vue、React、小程序等业界主流技术栈的组件库解决方案，适合用于构建设计统一 / 多端覆盖 / 跨技术栈的企业级前端应用。</p> 
<p style="margin-left:0px">目前，TDesign 发布了 2022 年 7 月的第一周更新，带来如下变更：</p> 
<h2 style="margin-left:0px"><strong>组件库</strong></h2> 
<h2><strong>Vue2 for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.43.2" target="_blank"><strong>0.43.2</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li><code>Form</code>: 
  <ul> 
   <li>添加内置校验方法 whitespace</li> 
   <li>新增校验触发方式 <code>trigger: 'blur' </code>- 现在<code>FormItem.label</code>为 <code>string</code> 类型时， <code>Form.errorMessage </code>模板中的<code> $&#123;name&#125;</code> 会被替换为 <code>FormItem.label </code>属性；当 <code>label</code> 属性为 <code>slot/function</code> 时，<code>$&#123;name&#125;</code> 会被替换为 <code>FormItem.name </code>属性</li> 
  </ul> </li> 
 <li>Table: 
  <ul> 
   <li>可编辑单元格，支持编辑组件联动</li> 
   <li>树形结构行选中支持半选状态</li> 
   <li>树形结构，缩进 <code>indent</code> 支持 <code>0</code></li> 
  </ul> </li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>Dialog/Drawer</code>: 修复 <code>closeOnOverlayClick</code> <code>closeOnEscKeydown</code> 默认值导致的无法设置的问题</li> 
 <li><code>Drawer</code>: 修复 <code>header</code> 默认值为 <code>undefined</code> 的问题</li> 
 <li><code>Dialog</code>: 修复 dialog 滚动失效问题</li> 
 <li><code>Form</code>: 修复 <code>number</code> 规则校验不生效的问题</li> 
 <li><code>Table</code>: 
  <ul> 
   <li>动态数据合并单元格，删除行数据时，未更新合并单元格状态</li> 
   <li>修复自定义筛选组件不显示问题</li> 
  </ul> </li> 
 <li><code>ColorPicker</code>: 修复颜色选择器样式异常</li> 
 <li><code>ConfigProvider</code>: 修复 config-provider 同时存在 provide 和 setup#provide 导致卡顿的性能问题</li> 
 <li><code>DatePicker</code>: 修复suffixIcon、clear事件问题</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.43.2" target="_blank">https://github.com/Tencent/tdesign-vue/releases/tag/0.43.2</a></p> 
<h2><strong>Vue3 for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Freleases%2Ftag%2F0.17.3" target="_blank"><strong>0.17.3</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li><code>Form</code>: 添加内置校验方法 whitespace</li> 
 <li><code>table</code>: 可编辑单元格，支持编辑组件联动</li> 
 <li><code>Table</code>: 树形结构支持半选状态</li> 
 <li><code>Jumper</code>: 新增 <code>jumper</code> 组件</li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>Table</code>: 表头吸顶显示问题</li> 
 <li><code>Table</code>: <code>paginationAffixedBottom</code> 支持配置 Affix 组件全部特性</li> 
 <li><code>DatePicker</code>: 修复 <code>Jumper</code> 组件类名错误</li> 
 <li><code>Upload</code>: 在每次上传前将错误提示数据重置</li> 
 <li><code>RadioGroup</code>: 修复 <code>RadioGroup</code> 多次赋予不存在的值时文字不能正常显示</li> 
 <li><code>Dialog</code>: 修复 <code>closeOnOverlayClick</code> <code>closeOnEscKeydown</code> 默认值导致的无法设置的问题</li> 
 <li><code>Drawer</code>: 修复 <code>closeOnOverlayClick</code> <code>closeOnEscKeydown</code> 默认值导致的无法设置的问题</li> 
 <li><code>DatePicker</code>: 修复日期选择器在表单禁用后还能点击的问题</li> 
 <li><code>Tree</code>: <code>getRightData</code> 方法兼容 <code>value</code> 的 <code>alias</code></li> 
 <li><code>Form</code>: 修复不传 <code>form.onSubmit</code> 回调函数导致的 <code>scrollToFirstError</code> 参数失效的问题</li> 
 <li><code>DatePicker</code>: 修复 <code>clearble</code> 响应式问题</li> 
 <li><code>Dialog</code>: 修复滚动失效问题</li> 
 <li><code>Table</code>: 修复动态数据合并元格问题</li> 
 <li><code>Table</code>: 修复树形结构设置 <code>indent = 0</code> 无效问题</li> 
 <li><code>Slider</code>: 使用 <code>InputNumber</code> 时在使用 <code>range</code> 属性情况下传入 <code>min</code> 或 <code>max</code> 会导致手动输入显示 NaN 问题</li> 
 <li><code>Select</code>: 修复多选下换行提前占满一行的问题</li> 
 <li><code>Select</code>: 修复 input 高度 <code>height 100% </code>导致换行高度异常的问题</li> 
 <li><code>Pagination</code>: 修复如果页面总数变更后当前页数不变的问题</li> 
 <li><code>RangeInput</code>: 修复 <code>rangeinput</code> 样式问题</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Freleases%2Ftag%2F0.17.3" target="_blank">https://github.com/Tencent/tdesign-vue-next/releases/tag/0.17.3</a></p> 
<h2><strong>React for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react%2Freleases%2Ftag%2F0.36.2" target="_blank"><strong>0.36.2</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li><code>Form</code>: 添加内置校验方法 whitespace</li> 
 <li><code>Table</code>: 新增 <code>indeterminateSelectedRowKeys</code> ，用于控制选中行半选状态</li> 
 <li><code>Table</code>: 可编辑单元格，支持编辑组件联动</li> 
 <li><code>Table</code>: 树形结构行选中，支持中层节点半选状态</li> 
 <li><code>Table</code>: EnhancedTable 新增对外实例对象 <code>treeDataMap</code></li> 
 <li><code>Cascader</code>: 增加 <code>popupVisible, readonly, selectInputProps, onPopupVisibleChange</code> 属性，具体描述查看文档</li> 
 <li><code>Jumper</code>: 新增 jumper 组件</li> 
 <li><code>Space</code>: 优化空元素渲染</li> 
 <li><code>Cascader</code>: 基于 <code>select-input</code> 重构, 文本过长省略使用原生 title 展示全文本，不再使用 <code>tooltip</code> 组件</li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>table</code>: 表头吸顶显示问题</li> 
 <li><code>table</code>: <code>paginationAffixedBottom</code> 支持配置 Affix 组件全部特性</li> 
 <li><code>treeselect</code>: 默认lazy异步加载开启，与api保持一致</li> 
 <li><code>DatePicker</code>: 修复 presetsPlacement 不生效的问题</li> 
 <li><code>colorpicker</code>: 修复最近使用颜色的功能</li> 
 <li><code>Table</code>: 树形结构行选中，没有配置 <code>tree</code>，则当作普通表格行选中处理</li> 
 <li><code>Table</code>: 修复树形数据表格，选中子节点时，会导致父节点自动折叠问题</li> 
 <li><code>Table</code>: 修复合并单元格，动态数据显示异常问题、</li> 
 <li><code>Table</code>: 可编辑功能，数据更新不及时问题</li> 
 <li><code>Cascader</code>: 修复数据中 <code>value</code> 的数据类型为 <code>number</code> 时，<code>clearable</code> 失效</li> 
 <li><code>Dialog</code>: 修复滚动失效问题</li> 
 <li><code>select</code>: 修复多选下换行提前占满一行的问题</li> 
 <li><code>Upload</code>: 修复 disabled 依然可删除问题</li> 
 <li><code>colorPicker</code>: 修复在 <code>ColorTrigger</code> 输入色值时，自动<code>format</code>输入值并回填的问题</li> 
 <li><code>table</code>: 兼容树状表格未传入 <code>tree</code> 属性的场景</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react%2Freleases%2Ftag%2F0.36.2" target="_blank">https://github.com/Tencent/tdesign-react/releases/tag/0.36.2</a></p> 
<h2><strong>Miniprogram for WeChat 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-miniprogram%2Freleases%2Ftag%2F0.14.0" target="_blank"><strong>0.14.0</strong></a></h2> 
<h3><strong>❗ Breaking Changes</strong></h3> 
<ul> 
 <li><code>TextArea</code>: 移除不生效的外部样式类 <code>t-class-placeholder</code>, 建议使用类名 <code>t-textarea__placeholder</code> 进行样式覆盖，存在不兼容更新</li> 
</ul> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li><code>ActionSheet</code>: 新增 <code>t-class-content</code>、<code>t-class-cancel </code>外部样式类</li> 
 <li><code>Progress</code>: 新增<code>t-class-bar</code>外部样式类</li> 
 <li><code>Picker</code>: 
  <ul> 
   <li>新增 <code>confirm</code> 事件，返回参数和 <code>change</code> 一致</li> 
   <li><code>confirm</code>、<code>change</code>、<code>pick</code> 事件均返回 <code>label</code> 参数</li> 
  </ul> </li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>Tabbar</code>: 修复具名插槽无法使用的问题</li> 
 <li>修复默认层级问题 
  <ul> 
   <li>Dialog</li> 
   <li>DropdownMenu</li> 
   <li>Drawer</li> 
   <li>Message</li> 
   <li>Popup</li> 
  </ul> </li> 
 <li><code>Fab</code>: 修复 <code>text</code> 属性不生效的问题</li> 
 <li><code>NoticeBar</code>: 修复公告不滚动问题</li> 
 <li><code>Dialog</code>: 修复点击遮罩层不会触发 <code>close</code> 事件的问题</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-miniprogram%2Freleases%2Ftag%2F0.14.0" target="_blank">https://github.com/Tencent/tdesign-miniprogram/releases/tag/0.14.0</a></p> 
<h2><strong>Vue3 for Mobile 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-mobile-vue%2Freleases%2Ftag%2F0.9.0" target="_blank"><strong>0.9.0</strong></a></h2> 
<h3><strong>❗ Breaking Changes</strong></h3> 
<ul> 
 <li><code>Progress</code>: 移除 <code>size</code> 和 <code>theme</code> 属性，存在不兼容更新</li> 
 <li><code>Picker</code>:重构<code>Picker</code>组件 ，存在不兼容更新 
  <ul> 
   <li>移除子组件<code><picker-item/></code>，新增基于Picker开发的级联选择组件<code><cascade /></code></li> 
   <li>新增<code>columns</code>，代表配置每一列的选项；新增<code>renderLabel</code>，用于自定义渲染<code>label</code>；新增<code>onPick</code>，选中任何一列时均会触发</li> 
   <li>修改<code>onChange</code>，<code>onConfirm</code>的回调参数</li> 
   <li><code>DateTimePicker</code>:重构<code>DateTimePicker</code>组件</li> 
   <li>移除<code>disableDate</code>、<code>showWeek</code></li> 
   <li>新增<code>start</code>，用于设置最小可选时间；新增<code>end</code>，用于设置最大可选时间</li> 
   <li>将<code>onColumnChange</code>改名为<code>onPick</code>，修改回调参数</li> 
   <li>修改<code>onChange</code>，<code>onConfirm</code>的回调参数</li> 
  </ul> </li> 
 <li><code>Search</code>: 存在不兼容更新 
  <ul> 
   <li>移除 <code>iconColor</code> 属性</li> 
   <li><code>autofocus</code> 更名为 <code>focus</code></li> 
   <li><code>cancelButtonText</code> 更名为 <code>action</code></li> 
   <li>新增 <code>leftIcon</code> 支持左侧图标定制</li> 
   <li>新增 <code>value</code> 和 <code>default-value</code> 控制输入框的值</li> 
   <li><code>cancel</code> 事件更名为 <code>action-click</code></li> 
   <li>新增 <code>blur</code> 和 <code>focus</code> 事件</li> 
  </ul> </li> 
 <li><code>Collapse</code>:存在不兼容更新 
  <ul> 
   <li><code>accordion</code> 更名为 <code>expandMutex</code></li> 
   <li>移除 <code>title</code>、<code>labelWidth</code> 属性</li> 
   <li>新增 <code>disabled</code>、<code>expandIcon</code>、<code>onChange</code> 属性无效的问题</li> 
  </ul> </li> 
 <li><code>CollapsePanel</code>: 存在不兼容更新 
  <ul> 
   <li><code>name</code> 更为为 <code>value</code></li> 
   <li><code>title</code> 更名为 <code>header</code></li> 
   <li><code>extra</code> 更名为 <code>headerRightContent</code></li> 
   <li>移除 <code>labelWidth</code>、<code>headerClickable</code> 属性</li> 
   <li>新增 <code>default</code>、<code>expandIcon</code> 属性</li> 
   <li>移除 <code>click</code> 事件</li> 
  </ul> </li> 
 <li><code>Drawer</code>: 存在不兼容更新 
  <ul> 
   <li>移除 <code>slider</code> 属性</li> 
   <li>新增 <code>items</code>、<code>placement</code>、<code>showOverlay</code>、<code>zIndex</code> 等属性</li> 
   <li>新增 <code>close</code>、<code>item-click</code>、<code>overlay-click </code>等事件</li> 
  </ul> </li> 
</ul> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li><code>Indexes</code>: 新增 <code>Indexes</code> 组件</li> 
 <li><code>Input</code>: 新增支持 <code>size</code> 属性</li> 
 <li><code>Fab</code>: 新增支持 <code>buttonProps</code> 和 <code>style</code> 属性</li> 
 <li><code>Cell</code>: 新增支持 <code>image</code> 插槽</li> 
 <li><code>Rate</code>: 新增支持 <code>gap</code> 属性</li> 
 <li><code>Loading</code>: 新增支持 <code>duration</code>、<code>inheritColor</code>、<code>pause</code>、<code>reverse</code> 属性</li> 
 <li><code>Dialog</code>: 
  <ul> 
   <li>增支持 <code>actions</code> 和 <code>preventScrollThrough</code> 属性</li> 
   <li>新增支持 支持 <code>confirmBtn</code> 和 <code>cancelBtn</code> 的插槽</li> 
  </ul> </li> 
 <li><code>Checkbox</code>: 新增支持 <code>maxContentRow</code> 和 <code>maxLabelRow</code> 属性</li> 
 <li><code>CheckboxGroup</code>: 新增支持 <code>max</code> 属性</li> 
 <li><code>Swiper</code>: 新增支持 <code>minShowNum</code> 属性</li> 
 <li><code>Upload</code>: 
  <ul> 
   <li>新增 <code>select-change </code>事件</li> 
   <li>新增支持 <code>allowUploadDuplicateFile</code> 属性</li> 
  </ul> </li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>Badge</code>: 修复 <code>showZero</code> 属性无效的问题</li> 
 <li><code>Badge</code>: 修复 <code>maxCount</code> 属性无效的问题</li> 
 <li><code>DropdownMenu</code>: 修复单选 <code>update:value</code> 失效的问题</li> 
 <li><code>Radio</code>: 修复非受控用法错误的问题</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-mobile-vue%2Freleases%2Ftag%2F0.9.0" target="_blank">https://github.com/Tencent/tdesign-mobile-vue/releases/tag/0.9.0</a></p> 
<h2><strong>React for Mobile 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftdesign.tencent.com%2Fmobile-react%2Fgetting-started" target="_blank"><strong>0.1.0</strong></a></h2> 
<ul> 
 <li>适配移动端交互</li> 
 <li>基于 React 16.x（全部基于 React Hooks 的 Functional Component）</li> 
 <li>与其他框架/库（Vue / Angular）版本 UI 保持一致</li> 
 <li>支持按需加载</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftdesign.tencent.com%2Fmobile-react%2Fgetting-started" target="_blank">https://tdesign.tencent.com/mobile-react/getting-started</a></p> 
<h2 style="margin-left:0px"><strong>解决方案</strong></h2> 
<h2><strong>TDesign Vue Starter 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-starter%2Freleases%2Ftag%2F0.3.0" target="_blank"><strong>0.3.0</strong></a></h2> 
<h3><strong>Refactor</strong></h3> 
<ul> 
 <li>全面替换<code>less</code> <code>vars</code>颜色方案为CSS Token方案 与其他页面模板保持一致</li> 
 <li>移除<code>vue-color</code>，使用组件库的<code>color-picker-panel</code>组件</li> 
</ul> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li>升级组件库依赖至0.43+ <code>datepicker</code> 使用方式有调整</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-starter%2Freleases%2Ftag%2F0.3.0" target="_blank">https://github.com/Tencent/tdesign-vue-starter/releases/tag/0.3.0</a> </p> 
<p> </p> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Freleases%2Ftag%2Fv2022.7.5" target="_blank">https://github.com/Tencent/tdesign/releases/tag/v2022.7.5</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            