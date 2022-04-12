
---
title: '腾讯企业级设计体系 TDesign 发布 2022.4 第二周更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=923'
author: 开源中国
comments: false
date: Tue, 12 Apr 2022 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=923'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px">TDesign 是一款诞生于腾讯内部、拥有完整的设计价值观和视觉风格指南的企业级设计体系，同时提供了丰富的设计资源，在设计体系基础上产出基于 Vue、React、小程序等业界主流技术栈的组件库解决方案，适合用于构建设计统一/多端覆盖/跨技术栈的企业级前端应用。</p> 
<p style="margin-left:0px">目前，TDesign 发布了 2022 年 4 月的第二周更新，带来如下变更：</p> 
<h2 style="margin-left:0px"><strong>组件库</strong></h2> 
<h2><strong>Vue2 for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Fblob%2Fv.2022.4.10%2Fhttps%25EF%25BC%259A%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.40.2" target="_blank"><strong>0.40.2 版</strong></a></h2> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>Form</code>：修复 <code>FormItem slot label</code> 未正常占位的问题</li> 
 <li><code>Slider</code>： 修复设置 <code>inputnumberProps</code> 属性无效的问题</li> 
 <li><code>Upload</code>： 
  <ul> 
   <li>修复 <code>remove</code>、<code>selectChange</code> 时间回调异常的问题</li> 
   <li>修复取消上传逻辑异常</li> 
  </ul> </li> 
</ul> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li><code>Popup</code>： <code>content</code> 尺寸变化后自动更新位置</li> 
 <li><code>Slider</code>： <code>label</code> 为 <code>function</code> 时新增 <code>value</code> 和 <code>position</code> 参数</li> 
 <li><code>Upload</code>： 
  <ul> 
   <li>支持自定义上传文件列表</li> 
   <li>列表型上传支持展示 <code>errorMessage</code></li> 
  </ul> </li> 
 <li><code>Checkbox</code>： <code>onChange</code> 事件新增参数 <code>option</code> 表示当前操作对象，<code>current</code> 表示当前操作对象的 <code>value</code></li> 
 <li><code>Table</code>： 
  <ul> 
   <li>表格拖拽排序支持完全受控用法</li> 
   <li>列配置功能，<code>onColumnChange</code> 事件新增参数 <code>e</code> 和 <code>currentColumn</code></li> 
   <li>列配置功能，新增 <code>buttonProps</code>，用于支持完全自定义「列配置按钮」风格和内容</li> 
   <li>列配置功能，新增 <code>placement</code>，用于控制「列配置按钮 」相对于表格组件的位置，可选值：左上角、右上角、左下角、右下角</li> 
   <li>列配置功能，新增控制列配置弹窗显示或隐藏属性 <code>columnControllerVisible</code> 和 <code>onColumnControllerVisibleChange</code>，将主要应用于完全需要自定义列配置按钮的业务场景</li> 
   <li><code>BaseTable</code>/<code>Primary</code>/<code>Table</code>/<code>EnhancedTable</code> 新增 <code>bottomContent</code>，用于设置表格底部内容</li> 
   <li>修复当数据量过少时，过滤浮层被隐藏的问题，修复 Safari 浏览器无法显示省略浮层问题</li> 
   <li>树形结构中，新增 <code>toggleExpandData</code>，用于控制行展开</li> 
   <li>树形结构中，无法获取到正确的 <code>rowKey</code> 时，抛出错误，提醒用户修改</li> 
   <li><code>table-layout</code>： <code>fixed</code> 模式，且内容超出时，设置默认列宽为 <code>100</code>，避免出现列宽为 <code>0</code> 消失的情况</li> 
   <li>即使没有行选中列，依然支持 <code>selectedRowKeys</code> 添加类名</li> 
   <li>行选中和行类名透传，同时存在时，自定义行类名透传失效问题</li> 
   <li>修复 <code>tfoot>tr</code> 类名透传失效问题</li> 
  </ul> </li> 
</ul> 
<p>详情见：https：//github.com/Tencent/tdesign-vue/releases/tag/0.40.2</p> 
<h2><strong>Vue3 for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Fblob%2Fv.2022.4.10%2Fhttps%25EF%25BC%259A%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Freleases%2Ftag%2F0.12.0" target="_blank"><strong>0.12.0 版</strong></a></h2> 
<h3><strong>⚠️BREAKING CHANGES</strong></h3> 
<ul> 
 <li>重构 <code>Table </code>为 <code>Composition API</code>，存在不兼容更新 
  <ul> 
   <li><code>BaseTable HTML</code> 结构变更，写过 <code>CSS</code> 样式覆盖的同学需注意更新样式。由之前的两个 <code>table</code> 分别渲染 <code>thead</code> 和 <code>tbody</code>，更为一个 <code>table</code></li> 
   <li>行拖拽排序功能，使用方法有调整，从 <code>sortOnRowDraggable</code> 更为 <code>dragSort='col'</code></li> 
   <li>表头更为使用 th 标签，之前为 td，不符合语义</li> 
   <li>事件 <code>row-db-click</code> 更为 <code>row-dblclick</code> ，<code>onRowDbClick</code> 更为 <code>rowDblclick</code></li> 
   <li>事件 <code>row-hover</code> 更为 <code>row-mouseover</code>, <code>onRowHover</code> 更为 <code>onRowMouseover</code></li> 
   <li><code>CSS</code> 类名 <code>t-table__row-first-full-row</code> 更为 <code>t-table__first-full-row</code>，<code>t-table__row-last-full-row</code> 更为 <code>t-table__last-full-row</code></li> 
  </ul> </li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li>修复 <code>configProvider</code> 警告 和 <code>globalConfig</code> 数据响应式问题</li> 
 <li>修复 <code>Input type=password</code> 时 <code>autocomplete</code> 警告 以及 <code>toggle password</code> 问题</li> 
 <li>修复 <code>Checkbox Group</code> 插槽形式 <code>disabled</code> 属性没有生效</li> 
 <li>修复 <code>Upload</code> 中 <code>triggerUpload</code> 方法未正确导出 和 自定义拖拽上传 demo 中 “点击上传” 按钮无效 修复 <code>Slider inputNumberProps</code> 未正常透传</li> 
 <li>修复 <code>Affix onFixedChange</code> 触发时机，在固定状态发生变化时才会触发该事件（改动之前为：滚动一直触发）</li> 
 <li>修复 <code>Table</code> 的 若干 Bug</li> 
</ul> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li>新增 <code>Collapse</code> 组件，使用 <code>Composition api</code></li> 
 <li>新增 <code>Message</code> 的 <code>fadeIn</code> and <code>fadeOut animation</code></li> 
 <li>新增 <code>color-picker</code> 渐变预览，改进最近使用色交互</li> 
 <li>新增 <code>Table</code> 特性 
  <ul> 
   <li>排序交互变更：排序方式支持点击直接排序</li> 
   <li>优化表格最后一列 <code>ellipsis</code> 浮层位置底部右对齐</li> 
   <li>新增超出省略功能， <code>ellipsis</code> 支持透传 <code>Popup</code> 组件全部属性</li> 
   <li>新增表尾合计行，支持固定在底部，支持多行合计，支持完全自定义内容</li> 
   <li>新增 <code>loadingProps</code> 透传加载组件全部特性</li> 
   <li>新增固定行（冻结行）</li> 
   <li>新增排序图标自定义，插槽 <code>(slot='filterIcon')</code> 和渲染函数 <code>(props.filterIcon)</code> 均可</li> 
   <li>新增全局配置：过滤图标、空元素、异步加载文本配置、排序按钮文本配置</li> 
   <li>新增 <code>scroll</code> 滚动事件</li> 
   <li>新增表头吸顶功能</li> 
   <li>新增综合功能：多级表头 + 固定表头 + 固定列 + 表头吸顶 + 虚拟滚动 + 自定义列配置</li> 
   <li>过滤功能，条件为真时，高亮筛选图标</li> 
   <li>新增列拖拽排序功能，通过拖拽手柄调整表格排序</li> 
  </ul> </li> 
</ul> 
<p> </p> 
<h2><strong>React for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Fblob%2Fv.2022.4.10%2Fhttps%25EF%25BC%259A%2Fgithub.com%2FTencent%2Ftdesign-react%2Freleases%2Ftag%2F0.30.2" target="_blank"><strong>0.30.2 版</strong></a></h2> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>Cascader</code>： 修复定制数据字段别名 <code>label</code> 不展示问题</li> 
 <li><code>Form</code>： 兼容 <code>FormItem</code> 单独使用报错问题</li> 
 <li><code>Table</code>： 
  <ul> 
   <li>修复 <code>table</code> 高度问题</li> 
   <li>修复 <code>table className ts</code> 类型丢失</li> 
  </ul> </li> 
 <li><code>Upload</code>： 修复多图片上传时 <code>defaultFiles</code> 造成上传进度错误</li> 
 <li><code>Slider</code>： 兼容不传 <code>value</code> 场景</li> 
</ul> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li><code>Breadcrumb</code>： 增加自定义 <code>children</code> 时对 <code>separator</code> 的支持</li> 
 <li><code>Popconfirm</code>： 调整组件导出命名</li> 
</ul> 
<p> </p> 
<h2><strong>Miniprogram for WeChat 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Fblob%2Fv.2022.4.10%2Fhttps%25EF%25BC%259A%2Fgithub.com%2FTencent%2Ftdesign-miniprogram%2Freleases%2Ftag%2F0.7.3" target="_blank"><strong>0.7.3 版</strong></a></h2> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>Cell</code>： 修复传入 <code>String</code> 类型的 <code>right-icon</code> 不生效的问题</li> 
 <li><code>Tabs</code>： 属性 <code>label </code>支持 <code>slot</code></li> 
 <li><code>Dialog</code>： 完善 <code>close</code> 事件返回的参数</li> 
 <li>受控优化：支持不传值时默认为非受控用法</li> 
</ul> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li>新增组件： 
  <ul> 
   <li><code>Collapse </code>折叠面板</li> 
   <li><code>Progress </code>进度条</li> 
  </ul> </li> 
 <li><code>Picker</code>： 新增属性 <code>header</code> 以及 <code>header</code> 和 <code>footer</code> 的插槽</li> 
 <li><code>DateTimePicker</code>： 新增属性 <code>header</code> 以及 <code>header</code> 和 <code>footer</code> 的插槽</li> 
</ul> 
<p> </p> 
<h2><strong>Vue3 for Mobile 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Fblob%2Fv.2022.4.10%2Fhttps%25EF%25BC%259A%2Fgithub.com%2FTencent%2Ftdesign-mobile-vue%2Freleases%2Ftag%2F0.8.2" target="_blank"><strong>0.8.2 版</strong></a></h2> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>tabs</code>： <code>label</code> 支持动态修改，以及新增支持 <code>slot</code> 的方式</li> 
 <li><code>popup</code>： 修复 <code>teleport</code> 失效问题</li> 
</ul> 
<p> </p> 
<h2 style="margin-left:0px"><strong>解决方案及周边</strong></h2> 
<h2><strong>TDesign Vue Starter 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Fblob%2Fv.2022.4.10%2Fhttps%25EF%25BC%259A%2Fgithub.com%2FTencent%2Ftdesign-vue-starter%2Freleases%2Ftag%2F0.1.5" target="_blank"><strong>0.1.5 版</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li>多标签 <code>Tab</code> 页增加持久化功能</li> 
 <li>内置全局配置组件，支持全局多语言及属性的配置</li> 
</ul> 
<p> </p> 
<h2><strong>TDesign Vue Next Starter 发布</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Fblob%2Fv.2022.4.10%2Fhttps%25EF%25BC%259A%2Fgithub.com%2FTencent%2Ftdesign-vue-next-starter%2Freleases%2Ftag%2F0.2.2" target="_blank"><strong> 0.2.2 版</strong></a></h2> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li>修复图表文字颜色异常</li> 
 <li>修复 <code>mock roles</code> 模块错误</li> 
</ul> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li>支持多标签页支持持久化</li> 
 <li>升级组件库依赖 tdesign-vue-next 至 0.11 版本</li> 
</ul> 
<p> </p> 
<h2><strong>TDesign React Starter 发布</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Fblob%2Fv.2022.4.10%2Fhttps%25EF%25BC%259A%2Fgithub.com%2FTencent%2Ftdesign-react-starter%2Freleases%2Ftag%2F0.1.2" target="_blank"><strong> 0.1.2 版</strong></a></h2> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li>修复构建产物丢失 <code>CSS Token</code> 的问题</li> 
 <li>修复图表文字重叠的问题</li> 
</ul> 
<p> </p> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Freleases%2Ftag%2Fv.2022.4.10" target="_blank">https://github.com/Tencent/tdesign/releases/tag/v.2022.4.10</a></p>
                                        </div>
                                      
</div>
            