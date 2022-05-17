
---
title: '腾讯企业级设计体系 TDesign 发布 2022.5 第二周更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2977'
author: 开源中国
comments: false
date: Tue, 17 May 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2977'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">TDesign 是一款诞生于腾讯内部、拥有完整的设计价值观和视觉风格指南的企业级设计体系，同时提供了丰富的设计资源，在设计体系基础上产出基于 Vue、React、小程序等业界主流技术栈的组件库解决方案，适合用于构建设计统一 / 多端覆盖 / 跨技术栈的企业级前端应用。</p> 
<p style="margin-left:0px">目前，TDesign 发布了 2022 年 5 月的第二周更新，带来如下变更：</p> 
<h2 style="margin-left:0px"><strong>组件库</strong></h2> 
<h2><strong>Vue2 for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.41.3" target="_blank"><strong>0.41.3 版</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li><code>Icon</code>: 更新图标 新增 <code>file-icon</code> 图标 调整 <code>file-excel</code>、<code>file-pdf</code>、<code>file-powerpoint</code>、<code>file-unknown</code>、<code>file-word</code> 和 <code>star-filled</code> 图标的绘制路径</li> 
 <li><code>Dialog</code>: 支持<code>preventScrollThrough</code>API</li> 
 <li><code>Table</code>: 支持自定义树形结构图标 <code>treeExpandAndFoldIcon</code>，同时支持全局配置此图标</li> 
 <li><code>Table</code>: 支持隐藏排序文本提示 <code>hideSortTips</code>，同时支持全局配置是否隐藏排序文本提示</li> 
 <li><code>Steps</code>: 新增 <code>separator</code> 属性，用于控制步骤条分隔符类型</li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>Select</code>: 修复 <code>textarea</code> 作为 panelContent 时无法使用键盘事件的问题</li> 
 <li><code>Slider</code>: 修复 <code>InputProps</code> 属性传递布尔值时 ts 错误的问题</li> 
 <li><code>Table</code>: 固定列滚动阴影修复</li> 
 <li><code>Dropdown</code>: 插槽模式下 <code>maxHeight </code>失效的问题</li> 
 <li><code>Dropdown</code>: 透传 popup 事件问题</li> 
 <li><code>Dialog</code>: 修复 <code>normal</code> 下加入 lock 导致页面无法滚动的问题</li> 
 <li><code>Table</code>: 修正拖拽列款的边界条件判断</li> 
 <li><code>Progress</code>: 修复环形进度条显示比例不准确</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.41.3" target="_blank">https://github.com/Tencent/tdesign-vue/releases/tag/0.41.3</a></p> 
<h2><strong>Vue3 for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Freleases%2Ftag%2F0.14.2" target="_blank"><strong>0.14.2 版</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li><code>swiper</code>: 增加新组件 <code>swiper</code></li> 
 <li><code>Icon</code>: 更新图标 新增 <code>file-icon</code> 图标 调整 <code>file-excel</code>、<code>file-pdf</code>、<code>file-powerpoint</code>、<code>file-unknown</code>、<code>file-word</code> 和 <code>star-filled</code> 图标的绘制路径</li> 
 <li><code>popconfirm</code>: <code>visible</code> 属性支持 <code>v-model</code> 语法糖</li> 
 <li><code>notification</code>: 使用项目中已有的 js 动画方案，替换先前的 <code>transitionGroup</code> 方案，完善了组件出现和回收动画效果。其中涉及到 common 子仓库的修改，删除之前 transition 相关的类名，添加了一个 <code>&-list__showt</code> 类名。</li> 
 <li><code>notification</code>: 增加 <code>onMouseenter</code> 和 <code>onMouseleave</code> 事件，保证鼠标移入移出组件时，<code>duration</code> 时间的停止和重新计时。</li> 
 <li><code>Table</code>: 支持自定义树形结构图标 <code>treeExpandAndFoldIcon</code>，同时支持全局配置此图标</li> 
 <li><code>Table</code>: 支持隐藏排序文本提示 <code>hideSortTips</code>，同时支持全局配置是否隐藏排序文本提示</li> 
 <li><code>dropdown</code>: 使用 compositionAPI 重构 <code>dropdown</code> 组件</li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>InputNumber</code>: 修复 input-number 重构 hook 使用错误出现的问题</li> 
 <li><code>tooltip</code>: support set placement by mouse</li> 
 <li><code>ConfigProvider</code>: 修复 <code>animation</code> 属性 <code>exclude</code> 和 <code>include</code> 在 TS 中都必填的问题</li> 
 <li><code>Table</code>: <code>renderExpandedRow</code> 为非必填</li> 
 <li><code>ColorPicker</code>: - fix(ColorPicker): 遍历循环的时候无法监听 change 事件会报错</li> 
 <li><code>TimePicker</code>: time-range-picker suffix icon 丢失问题</li> 
 <li><code>message</code>: 修复插件式调用时，用户传入 <code>onCloseBtnClick</code> 事件时，无法触发回调</li> 
 <li><code>notification</code>: 修复插件式调用时，用户传入 <code>onCloseBtnClick</code> <code>onDurationEnd</code> 事件时，无法触发回调</li> 
 <li><code>menu</code>: 修复 <code>expandMutex </code>属性设置无效</li> 
 <li><code>slider</code>: 修复 <code>toolTipProps </code>属性设置无效, 拼写错误</li> 
 <li><code>popconfirm</code>: 修复箭头与 <code>trigger</code> 属性</li> 
 <li><code>dialog</code>: 修复初始化且为显示时的 <code>lock</code> 问题</li> 
 <li><code>breadcrumb</code>: 修复弹出 tooltip 异常</li> 
 <li><code>input</code>: 修复 <code>autowidth</code> 模式计算错误</li> 
 <li><code>form</code>: 修复当 modelValue 为外部传入的 undefined 时，双向绑定失效</li> 
 <li><code>form</code>: 修复 <code>attrs</code> 注入异常</li> 
 <li><code>timePicker</code>: 修复当 modelValue 为外部传入的 undefined 时，clearable 失效</li> 
 <li><code>Steps</code>: 支持 separator api & 修复响应式问题</li> 
 <li><code>progress</code>: 环形进度条显示比例不准确</li> 
 <li><code>Table</code>: 修复 多级表头 + 列配置 综合示例中，列数量超出一定限制时报错</li> 
 <li><code>tooltip</code>: support set placement by mouse</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Freleases%2Ftag%2F0.14.2" target="_blank">https://github.com/Tencent/tdesign-vue-next/releases/tag/0.14.2</a></p> 
<h2><strong>React for Web 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react%2Freleases%2Ftag%2F0.33.2" target="_blank"><strong>0.33.2 版</strong></a></h2> 
<h3><strong>❗ Breaking Changes</strong></h3> 
<ul> 
 <li>重构 <code>DatePicker</code>、<code>TimePicker </code>组件，样式结构有所调整，存在不兼容更新</li> 
</ul> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li><code>DatePicker</code>: 
  <ul> 
   <li>移除 <code>range</code>api，分别导出 <code>Datepicker</code> 与 <code>DateRangePicker</code> 组件</li> 
   <li>支持 <code>DatePickerPanel</code> 与 <code>DateRangePickerPanel</code> 单独使用</li> 
   <li>支持年份、月份区间选择</li> 
   <li>支持 <code>allowInput</code> api</li> 
  </ul> </li> 
 <li><code>TimePicker</code>： 
  <ul> 
   <li>重新调整样式、允许输入交互重新设计</li> 
   <li>调整交互为点击确认按钮保留改动 直接关闭弹窗不保留改动 恢复初始值</li> 
   <li><code>disableTime</code>、<code>onFocus</code>、<code>onBlur</code>、<code>onInput </code>等API存在 breaking change</li> 
   <li>新增 <code>TimePickerPanel</code> 组件 用于单独使用面板的场景</li> 
  </ul> </li> 
 <li><code>RangeInput</code>: 新增 <code>RangeInput</code> 组件</li> 
 <li><code>RangeInputPopup</code>： 新增 <code>RangeInputPopup</code> 组件</li> 
 <li><code>Jumper</code>：新增 <code>Jumper</code> 组件</li> 
 <li><code>Steps</code>: 支持 separator api & 完善反转逻辑</li> 
 <li><code>Form</code>: 支持整理嵌套数据</li> 
 <li><code>Affix</code>: 优化滚动逻辑</li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<p><code>Table</code>: 修复 多级表头 + 列配置 综合示例中，列数量超出一定限制时报错<br> <code>DatePicker</code>: 修复宽度计算问题<br> <code>Slider</code>: 修复 <code>inputNumberProps </code>类型问题</p> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react%2Freleases%2Ftag%2F0.33.2" target="_blank">https://github.com/Tencent/tdesign-react/releases/tag/0.33.2</a></p> 
<h2><strong>Miniprogram for WeChat 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-miniprogram%2Freleases%2Ftag%2F0.11.2" target="_blank"><strong>0.11.2 版</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li>完善 <code>Input</code> 原生属性 
  <ul> 
   <li>完善 <code>change</code> 事件，增加返回 <code>cursor</code> 和 <code>keyCode</code> 数据</li> 
   <li>增加 <code>keyboardheightchange</code> 事件，键盘高度发生变化的时候触发</li> 
   <li>增加占位符相关属性：<code>placehoderStyle</code> 和 <code>placeholderClass</code></li> 
   <li>增加光标相关属性：<code>cursor</code>、<code>selection-start</code>、<code>selection-end</code></li> 
   <li>增加 <code>hold-keyboard</code> 属性</li> 
   <li>增加安全键盘相关属性</li> 
  </ul> </li> 
 <li><code>Button</code>: 增加 <code>bindchooseavatar</code> 原生事件，用户选择头像</li> 
 <li><code>Input</code>: 支持 <code>borderless</code> 属性</li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li><code>Picker</code>: 修复在没有取消和确认按钮的时候，标题没居中对齐的问题</li> 
 <li><code>Sticky</code>: 修复在极端情况下报错的问题</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-miniprogram%2Freleases%2Ftag%2F0.11.2" target="_blank">https://github.com/Tencent/tdesign-miniprogram/releases/tag/0.11.2</a></p> 
<h2 style="margin-left:0px"><strong>解决方案及周边</strong></h2> 
<h2><strong>TDesign Starter CLI 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-starter-cli%2Freleases%2Ftag%2F0.2.2" target="_blank"><strong>0.2.2 版</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li>配合模板新增维护中页面升级</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-starter-cli%2Freleases%2Ftag%2F0.2.2" target="_blank">https://github.com/Tencent/tdesign-starter-cli/releases/tag/0.2.2</a></p> 
<h2><strong>TDesign Vue Starter 发布</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-starter%2Freleases%2Ftag%2F0.2.1" target="_blank"><strong> 0.2.1 版</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li>列表页增加吸顶展示</li> 
 <li>新增维护中页面</li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li>修复展示底部开关失效的问题</li> 
 <li>修复 mock roles 错误</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-starter%2Freleases%2Ftag%2F0.2.1" target="_blank">https://github.com/Tencent/tdesign-vue-starter/releases/tag/0.2.1</a></p> 
<h2><strong>TDesign Vue Next Starter 发布 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next-starter%2Freleases%2Ftag%2F0.3.1" target="_blank"><strong>0.3.1 版</strong></a></h2> 
<h3><strong>🌈 Features</strong></h3> 
<ul> 
 <li>lint新增 style scoped 提示</li> 
 <li>新增维护中页面</li> 
 <li>升级组件库依赖至 0.14+</li> 
</ul> 
<h3><strong>🐞 Bug Fixes</strong></h3> 
<ul> 
 <li>修复多标签 Tab 页关闭左侧，关闭其他可能导致主页标签被删除</li> 
 <li>修复多个滚动列表之间切换时页面不刷新导致的样式缺陷</li> 
</ul> 
<p>详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next-starter%2Freleases%2Ftag%2F0.3.1" target="_blank">https://github.com/Tencent/tdesign-vue-next-starter/releases/tag/0.3.1</a></p> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Freleases%2Ftag%2Fv2022.5.15" target="_blank">https://github.com/Tencent/tdesign/releases/tag/v2022.5.15</a></p>
                                        </div>
                                      
</div>
            