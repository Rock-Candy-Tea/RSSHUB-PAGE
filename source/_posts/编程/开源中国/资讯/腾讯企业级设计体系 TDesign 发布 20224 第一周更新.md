
---
title: '腾讯企业级设计体系 TDesign 发布 2022.4 第一周更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7490'
author: 开源中国
comments: false
date: Fri, 08 Apr 2022 06:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7490'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">TDesign 是一款诞生于腾讯内部、拥有完整的设计价值观和视觉风格指南的企业级设计体系，同时提供了丰富的设计资源，在设计体系基础上产出基于 Vue、React、小程序等业界主流技术栈的组件库解决方案，适合用于构建设计统一/多端覆盖/跨技术栈的企业级前端应用。</p> 
<p style="margin-left:0px">目前，TDesign 发布了 2022 年 4 月的第一周更新，带来如下变更：</p> 
<h2><strong>组件库</strong></h2> 
<h2><strong>Vue2 for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.40.1" target="_blank"><strong>0.40.1 版</strong></a></h2> 
<h3><strong>Bug Fixes</strong></h3> 
<ul> 
 <li><code>Table</code>: 修复本地数据排序，异步加载数据时分页失效的问题</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.40.1" target="_blank">https://github.com/Tencent/tdesign-vue/releases/tag/0.40.1</a></p> 
<h2><strong>Vue2 for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.40.0" target="_blank"><strong>0.40.0 版</strong></a></h2> 
<h3><strong>⚠️BREAKING CHANGES</strong></h3> 
<ul> 
 <li><code>Table</code>: 表格行列拖拽排序功能重构，新用法请参考官网 demo</li> 
 <li><code>Form</code>: <code>label</code> 为空时不再默认渲染宽度占位，需要手动设置样式保持表单对齐</li> 
</ul> 
<h3><strong>Bug Fixes</strong></h3> 
<ul> 
 <li><code>Popconfirm</code>: 修复确认框中按钮默认大小</li> 
 <li><code>Upload</code>: 修复上传中状态文案</li> 
 <li><code>Popup</code>: 修复 <code>hideEmptyPopup</code> 在动态改变内容时不生效的问题</li> 
 <li><code>Table</code>: 修复合并单元格边框样式问题</li> 
 <li><code>Datepicker</code>: 修复区间时间选择时，月份/年份选择面板样式异常的问题</li> 
 <li>修复 <code>Table</code>/<code>SelectInput</code>/<code>TagInput</code> 按需引入时出现 <code>composition-api</code> 相关报错的问题</li> 
</ul> 
<h3><strong>Features</strong></h3> 
<ul> 
 <li><code>Table</code>: 支持外部设置当前显示列，新增 API <code>displayColumns defaultDisplayColumns onDisplayColumnsChange</code></li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.40.0" target="_blank">https://github.com/Tencent/tdesign-vue/releases/tag/0.40.0</a></p> 
<h2><strong>Vue2 for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.39.1" target="_blank"><strong>0.39.1 版</strong></a></h2> 
<h3><strong>Bug Fixes</strong></h3> 
<ul> 
 <li><code>Upload</code>: 
  <ul> 
   <li>修复 <code>success</code> 事件先于 <code>progress</code> 事件触发时，上传文件 <code>loadingFile</code> 值不正确的问题</li> 
   <li>修复最大数量限制 <code>max</code> 在多次文件选择中判断不正确的问题</li> 
  </ul> </li> 
 <li><code>Pagination</code>: 修复跳转页输入框展示了额外 <code>placeholder</code> 默认内容的问题</li> 
 <li><code>TreeSelect</code>: 
  <ul> 
   <li>修复 <code>treeProps</code> 中同时传入 <code>key</code>、<code>load</code> 时选中项显示的问题</li> 
   <li>修正 <code>TreeSelect</code> 的交互行为，与 <code>Select</code> 保持一致</li> 
   <li>修复 <code>filter</code> 状态下，树无法折叠的问题；修复 <code>lazy</code> 状态下，无法正确展示 <code>label</code> 的问题</li> 
  </ul> </li> 
 <li><code>Table</code>: 
  <ul> 
   <li>修复虚拟滚动 <code>threshold</code> 引起的报错</li> 
  </ul> </li> 
 <li>修复 <code>TS</code> 定义报错问题，非 <code>Typescript</code> 或 <code>SSR</code> 项目请尽快由 0.39.0 版本升级</li> 
</ul> 
<h3><strong>Features</strong></h3> 
<ul> 
 <li><code>ConfigProvider</code>: 完善语言配置能力</li> 
 <li><code>Table</code>: 
  <ul> 
   <li>表格超出省略浮层父元素更为表头 <code>thead</code>，避免挂载到全局 body</li> 
   <li>过滤功能浮层元素默认挂载到 <code>t-table</code>，不再挂载到全局</li> 
  </ul> </li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.39.1" target="_blank">https://github.com/Tencent/tdesign-vue/releases/tag/0.39.1</a></p> 
<h2><strong>Vue2 for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.39.0" target="_blank"><strong>0.39.0 版</strong></a></h2> 
<h3><strong>⚠️BREAKING CHANGES</strong></h3> 
<ul> 
 <li><code>Table</code> 组件使用 <code>composition-api</code> 重构 
  <ul> 
   <li><code>BaseTable HTML</code> 结构变更，写过 <code>CSS </code>样式覆盖的同学需注意更新样式</li> 
   <li>表头更为使用 <code>th </code>标签，之前为 <code>td</code>，不符合语义</li> 
   <li>事件 <code>row-db-click</code> 更为 <code>row-dblclick</code> ，<code>onRowDbClick</code> 更为 <code>rowDblclick</code></li> 
   <li>事件 <code>row-hover</code> 更为 <code>row-mouseover</code>, <code>onRowHover </code>更为 <code>onRowMouseover</code>（本没有 <code>rowHover </code>事件）</li> 
   <li><code>CSS </code>类名 <code>t-table__row-first-full-row</code> 更为 <code>t-table__first-full-row</code>，<code>t-table__row-last-full-row</code> 更为 <code>t-table__last-full-row</code></li> 
  </ul> </li> 
</ul> 
<h3><strong>Bug Fixes</strong></h3> 
<ul> 
 <li><code>Affix</code>: 修复 <code>onFixedChange</code> 触发时机，在固定状态发生变化时才会触发该事件（改动之前为：滚动一直触发）</li> 
 <li><code>Table</code>: 
  <ul> 
   <li>自定义列配置功能：多级表头和列显示配置同时存在时，无法进行正确的列配置的问题，列配置仅显示了第一层表头</li> 
   <li><code>verticalAlign </code>不生效问题</li> 
   <li>右上角出现文字穿透问题</li> 
   <li>固定表头和固定列，全部使用 <code>CSS sticky</code> 输出样式，组件仅渲染一个表格，表头和表内容 不再分开渲染输出。不仅支持 <code>table-layout: fixed</code> 模式，同时也支持 <code>table-layout: auto</code> 模式</li> 
   <li>设置 <code>tableLayout</code> : <code>auto</code> ，<code>maxHeight </code>显示异常</li> 
   <li><code>Table</code> 组件 <code>BaseTableCol </code>配置项 <code>fixed </code>和 <code>ellipsis(true)</code> 属性共存导致fix阴影无法显示</li> 
   <li>多级表头的表格 改变 <code>children</code> 的宽度无效</li> 
   <li>table 组件使用 <code>PrimaryTable </code>控制台报错 <code>t-primary-table</code> 未注册</li> 
   <li>表格组件设置 <code>height </code>或 <code>maxHeight </code>后未出现滚动条的时候竖线不对齐</li> 
   <li>修复，排序图标和过滤图标同时存在时，样式异常问题</li> 
  </ul> </li> 
</ul> 
<h3><strong>Features</strong></h3> 
<ul> 
 <li><code>Table</code>: 
  <ul> 
   <li>新增超出省略功能， <code>ellipsis </code>支持透传 <code>Popup</code> 组件全部属性</li> 
   <li>新增表尾合计行，支持固定在底部，支持多行合计，支持完全自定义内容</li> 
   <li>新增 <code>loadingProps</code> 透传加载组件全部特性</li> 
   <li>新增固定行（冻结行）</li> 
   <li>支持虚拟滚动</li> 
   <li>新增排序图标自定义，插槽 <code>(slot='filterIcon')</code> 和渲染函数 <code>(props.filterIcon)</code> 均可</li> 
   <li>新增全局配置：过滤图标、空元素、异步加载文本配置、排序按钮文本配置</li> 
   <li>新增 <code>scroll </code>滚动事件</li> 
   <li>新增表头吸顶功能</li> 
   <li>新增综合功能：多级表头 + 固定表头 + 固定列 + 表头吸顶 + 虚拟滚动 + 自定义列配置</li> 
  </ul> </li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.39.0" target="_blank">https://github.com/Tencent/tdesign-vue/releases/tag/0.39.0</a></p> 
<h2><strong>Vue3 for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Freleases%2Ftag%2F0.11.1" target="_blank"><strong>0.11.1 版</strong></a></h2> 
<h3><strong>Bug Fixes</strong></h3> 
<ul> 
 <li>重构 <code>Tabs</code> 为 <code>Composition-api</code></li> 
 <li>修复 <code>Upload triggerupload</code> 方法未导出</li> 
 <li>修复 <code>InputNumber</code> 未注册 <code>input</code> 组件</li> 
 <li>修复 <code>CheckboxGroup disabled</code> 属性无效</li> 
 <li>修复 <code>Input</code> 的 <code>type</code> 传入无效</li> 
 <li>修复 <code>SelectInput</code> Demo 样式</li> 
 <li>修复 <code>Pagination</code> 跳转页输入框展示了额外 <code>placeholder</code> 默认内容</li> 
</ul> 
<h3><strong>Features</strong></h3> 
<ul> 
 <li>重构 <code>TreeSelect</code> 为 <code>Composition-api</code></li> 
 <li>重构 日历组件 为 <code>Composition-api</code></li> 
 <li>国际化配置迁移至 <code>common</code></li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Freleases%2Ftag%2F0.11.1" target="_blank">https://github.com/Tencent/tdesign-vue-next/releases/tag/0.11.1</a></p> 
<h2><strong>React for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react%2Freleases%2Ftag%2F0.30.1" target="_blank"><strong>0.30.1 版</strong></a></h2> 
<h3><strong>⚠️BREAKING CHANGES</strong></h3> 
<ul> 
 <li><code>Form</code>: <code>label</code> 为空时不再默认渲染宽度占位，需要手动设置样式保持表单对齐</li> 
</ul> 
<h3><strong>Bug Fixes</strong></h3> 
<ul> 
 <li><code>Pagination</code>: 修复输入框宽显示问题</li> 
 <li><code>Datepicker</code>: 修复区间选择时间，月份/年份选择时间类型异常的问题</li> 
 <li><code>InputNumber</code>: 修复不能输入小数点问题</li> 
 <li><code>Popconfirm</code>: 修复按需加载样式丢失问题</li> 
 <li><code>Select</code>: 修复首次  <code>focus</code> 自动搜索问题</li> 
</ul> 
<h3><strong>Features</strong></h3> 
<ul> 
 <li>标签：优化组件内部逻辑</li> 
 <li><code>FormItem</code>: 支持自定义嵌套模式 & <code>label</code> 为空时不再处理占位对齐问题</li> 
 <li><code>SelectInput</code>:  <code>borderless</code> 和 <code>autowidth</code> 作为独立属性分开</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react%2Freleases%2Ftag%2F0.30.1" target="_blank">https://github.com/Tencent/tdesign-react/releases/tag/0.30.1</a></p> 
<h2><strong>Miniprogram for WeChat 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-miniprogram%2Freleases%2Ftag%2F0.7.2" target="_blank"><strong>0.7.2 版</strong></a></h2> 
<h3><strong>Bug Fixes</strong></h3> 
<ul> 
 <li><code>Search</code>: 修复 <code>submit</code> 事件返回参数错误的问题</li> 
 <li><code>Toast</code>: 修复最大宽度和文案没对齐的问题</li> 
 <li><code>Input</code>: 修复设置 <code>clearable</code>，点击不清除内容的问题</li> 
 <li><code>Dialog</code>: 修复 1px 边框在 iOS 上消失的问题</li> 
 <li><code>Swiper</code>: 修复延迟设置地址时，显示不正常的问题</li> 
 <li><code>Button</code>: 修复文案没有垂直居中的问题</li> 
</ul> 
<h3><strong>Feature</strong></h3> 
<ul> 
 <li><code>Fab</code>: 新增支持悬浮按钮</li> 
 <li><code>Drawer</code>: 新增支持抽屉</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-miniprogram%2Freleases%2Ftag%2F0.7.2" target="_blank">https://github.com/Tencent/tdesign-miniprogram/releases/tag/0.7.2</a></p> 
<h2><strong>Vue3 for Mobile 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-mobile-vue%2Freleases%2Ftag%2F0.8.1" target="_blank"><strong>0.8.1 版</strong></a></h2> 
<h3><strong>Bug Fixes</strong></h3> 
<ul> 
 <li><code>count-down</code>: 单位样式 bug 修复、倒计时加入 <code>fps</code> 获取</li> 
 <li><code>swiper</code>: 快速滑动导致卡住问题</li> 
 <li><code>picker</code>: 组件 demo 修复</li> 
 <li><code>swipe-cell</code>: 修改组件示例，和 demo 保持一致</li> 
</ul> 
<h3><strong>Feature</strong></h3> 
<ul> 
 <li>支持历史版本跳转</li> 
 <li><code>dropdown-menu</code>: 更新组件的模板类型处理</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-mobile-vue%2Freleases%2Ftag%2F0.8.1" target="_blank">https://github.com/Tencent/tdesign-mobile-vue/releases/tag/0.8.1</a> </p> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Freleases%2Ftag%2Fv.2022.4.3" target="_blank">https://github.com/Tencent/tdesign/releases/tag/v.2022.4.3</a></p>
                                        </div>
                                      
</div>
            