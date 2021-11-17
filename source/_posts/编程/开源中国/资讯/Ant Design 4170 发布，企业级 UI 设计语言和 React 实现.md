
---
title: 'Ant Design 4.17.0 发布，企业级 UI 设计语言和 React 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9279'
author: 开源中国
comments: false
date: Wed, 17 Nov 2021 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9279'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ant Design 4.17.0 现已发布，主要变化如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>动态主题 
  <ul style="margin-left:0; margin-right:0"> 
   <li>ConfigProvider 支持动态配置主题色，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fblob%2F4.17.0%2Fdocs%2Freact%2Fcustomize-theme-variable" target="_blank">详细文档</a>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31496" target="_blank">#31496</a></li> 
   <li>移动部分 <code>mixins</code> less 文件到 <code>themes</code> 文件下，因为它们依赖于主题相关变量。我们不推荐直接引用底层 less 文件，但是如果你使用了请注意这部分变更。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32763" target="_blank">#32763</a></li> 
   <li>修复 <code>antd.variable.less</code> 编译时会混入默认主题配置的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32279" target="_blank">#32279</a></li> 
   <li>修复 antd 编译产物缺失 <code>/style/default.css</code> 文件的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32116" target="_blank">#32116</a></li> 
   <li>修复 less 编译 <code>antd.xxx.less</code> 会抛出 <code>Maximum call stack size exceeded error</code> 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32063" target="_blank">#32063</a></li> 
  </ul> </li> 
 <li>Input 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复 <code>Input.Search</code> 组件在有 <code>allowClear</code> 和 <code>addonBefore</code> 属性时，输入框 <code>border-left-radius</code> 值错误的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32812" target="_blank">#32812</a></li> 
   <li>修复 Input 设置 <code>disabled</code> 时仍然保留聚焦样式的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32739" target="_blank">#32739</a></li> 
   <li>修复 Input <code>placeholder</code> 在 Chrome 上能被选择的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32639" target="_blank">#32639</a></li> 
   <li>Input.TextArea <code>maxLength</code> 属性现在会传给原生 textarea 标签。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32448" target="_blank">#32448</a></li> 
   <li>修复 Input 聚焦时点击清除图标无效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31931" target="_blank">#31931</a></li> 
  </ul> </li> 
 <li>Cascader 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Cascader 支持 <code>multiple</code> 模式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31936" target="_blank">#31936</a></li> 
   <li>在 <code>Cascader</code> 组件中，默认给选中值的文本添加 <code>title</code> 属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31237" target="_blank">#31237</a></li> 
   <li>修复 Cascader 中 <code>popupClassName</code> 与 <code>popupPlacement</code> 属性无效问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32143" target="_blank">#32143</a></li> 
  </ul> </li> 
 <li>Select 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Select 支持 <code>placement</code> 属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32143" target="_blank">#32143</a></li> 
   <li>Select 支持 <code>fieldNames</code> 自定义字段名称。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31925" target="_blank">#31925</a></li> 
   <li>Select 支持 mac 的 <code>ctrl + n/p</code> 快捷键组合。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Freact-component%2Fselect%2Fpull%2F650" target="_blank">#650</a></li> 
   <li>Select 在 <code>multiple</code> 模式下，tag 添加 <code>title</code> 属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Freact-component%2Fselect%2Fpull%2F637" target="_blank">#637</a></li> 
   <li>优化 Select 中选项文字粗细。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32486" target="_blank">#32486</a></li> 
  </ul> </li> 
 <li>TreeSelect 
  <ul style="margin-left:0; margin-right:0"> 
   <li>TreeSelect 支持 <code>placement</code> 属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32143" target="_blank">#32143</a></li> 
   <li>TreeSelect 支持 <code>fieldNames</code> 自定义字段名称。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31925" target="_blank">#31925</a></li> 
  </ul> </li> 
 <li>Tree 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Tree <code>draggable</code> 添加拖拽图标以提示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32306" target="_blank">#32306</a></li> 
   <li>Tree 添加 <code>fieldNames</code> 属性以支持自定义节点字段名称。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31395" target="_blank">#31395</a></li> 
   <li>Tree 虚拟滚动也支持 <code>onScroll</code> 事件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Freact-component%2Ftree%2Fpull%2F474" target="_blank">#474</a></li> 
   <li>修复 Tree 一个图标文字对齐问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32822" target="_blank">#32822</a></li> 
   <li>修复 Tree.DirectoryTree 键盘操作时抛出 <code>TypeError:nativeEvent is undefined</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32551" target="_blank">#32551</a></li> 
   <li>修复 Tree 拖拽到外部时没有清空指示器的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Freact-component%2Ftree%2Fpull%2F478" target="_blank">#478</a></li> 
   <li>修复 Tree 连接线在浏览器放大时一像素位置偏差的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32075" target="_blank">#32075</a></li> 
  </ul> </li> 
 <li>PageHeader 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复 PageHeader <code>breadcrumbRender</code> 返回<code>false</code>，仍然展示 dom 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32738" target="_blank">#32738</a></li> 
  </ul> </li> 
 <li>Form 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Form <code>rule</code> 支持 <code>warningOnly</code> 实现非阻塞校验。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30829" target="_blank">#30829</a></li> 
   <li>Form.ErrorList 支持自定义 <code>className</code> 属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30887" target="_blank">#30887</a></li> 
   <li>修复 Form 下 Select 内容太长导致布局换行的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32778" target="_blank">#32778</a></li> 
   <li>修复 Mentions 在 Form 下错误样式丢失的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32385" target="_blank">#32385</a></li> 
  </ul> </li> 
 <li>Drawer 
  <ul style="margin-left:0; margin-right:0"> 
   <li>调整 Drawer 关闭按钮位置和默认宽度，新增 <code>extra</code> 操作区域和 <code>size</code> 大小属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30908" target="_blank">#30908</a></li> 
   <li>Drawer 支持 <code>autoFocus</code> 属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Freact-component%2Fdrawer%2Fpull%2F181" target="_blank">#181</a></li> 
   <li>修复底部 Drawer 组件没有动画的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32761" target="_blank">#32761</a></li> 
   <li>优化 Drawer 弹出动画。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32342" target="_blank">#32342</a></li> 
  </ul> </li> 
 <li>Steps 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复 Steps 垂直 <code>progressDot</code> 的对齐样式问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32742" target="_blank">#32742</a></li> 
   <li>修复 Steps 默认响应式不生效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31965" target="_blank">#31965</a></li> 
  </ul> </li> 
 <li>Typography 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复 Typography 在单行折叠时展开后不换行。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32735" target="_blank">#32735</a></li> 
   <li>修复 Typography 设置 <code>ellipsis</code> 后在缩放下的文本溢出。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32496" target="_blank">#32496</a></li> 
   <li>修复 Typography <code>ellipsis</code> 在 Chrome 下屏幕缩小时溢出的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32447" target="_blank">#32447</a></li> 
  </ul> </li> 
 <li>Table 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Table 新增 <code>column.filterMode</code> 以支持配置树形筛选菜单，可选值为 <code>'menu' | 'tree'</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31809" target="_blank">#31809</a></li> 
   <li>Table 新增 <code>column.filterSearch</code> 以支持开启筛选列搜索功能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31809" target="_blank">#31809</a></li> 
   <li>Table 鼠标悬浮 <code>rowSpan</code> 行时会高亮所有相关行。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32557" target="_blank">#32557</a></li> 
   <li>修复 Table 选择框下拉箭头被固定列遮挡的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32276" target="_blank">#32276</a></li> 
   <li>修复 Table 设置 <code>sticky</code> 的时候 <code>loading</code> 样式跳动的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32703" target="_blank">#32703</a></li> 
   <li>修复 Table 不支持 <code>ref</code> 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32136" target="_blank">#32136</a></li> 
   <li>Table 移除 IE11 下 <code>sticky</code> 的相关样式以解决布局问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32177" target="_blank">#32177</a></li> 
   <li>优化 Table 排序图标边距问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32172" target="_blank">#32172</a></li> 
   <li>修复 Table 中 <code>pagination.className</code> 不生效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32131" target="_blank">#32131</a></li> 
   <li>修复 Table.SELECT_XXX 会无视 <code>getCheckboxProps</code> 提供的 <code>disabled</code> 状态问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32027" target="_blank">#32027</a></li> 
   <li>Table 筛选菜单重置按钮现在不再关闭菜单和生效。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31809" target="_blank">#31809</a></li> 
   <li>回滚 Table sticky <code>z-index</code> 样式的 less 计算到 <code>calc</code>，以防止 <code>auto</code> 样式计算错误问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31874" target="_blank">#31874</a></li> 
   <li>修复 Table 在数据变更后滚动条展示问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Freact-component%2Ftable%2Fpull%2F647" target="_blank">#647</a></li> 
  </ul> </li> 
 <li>Transfer 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Transfer 新增自定义左右 <code>footer</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31108" target="_blank">#31108</a></li> 
   <li>Transfer 支持 <code>locale.notFoundContent</code> 传入数组。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31088" target="_blank">#31088</a></li> 
   <li>修复 Transfer 打开选择菜单时抛出 <code>MenuItem should not leave undefined key</code> 警告。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32578" target="_blank">#32578</a></li> 
   <li>调整 Transfer 筛选搜索框图标位置，使其和表格筛选搜索框统一。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31809" target="_blank">#31809</a></li> 
  </ul> </li> 
 <li>Collapse 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复 Collapse 设置 <code>expandIconPosition</code> 为 <code>right</code> 后的样式问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32648" target="_blank">#32648</a></li> 
   <li>调整 Collapse 标题栏样式使标题折行时不侵占箭头空间。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32492" target="_blank">#32492</a></li> 
  </ul> </li> 
 <li>Button 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复 Button 有 <code>icon</code> 和 <code>href</code> 时的对齐问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32373" target="_blank">#32373</a></li> 
   <li>修复 Button <code>ghost</code> 鼠标悬停样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32289" target="_blank">#32289</a></li> 
   <li>修复 Button 配置 <code>loading</code> 时，无法触发 Tooltip 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32158" target="_blank">#32158</a></li> 
  </ul> </li> 
 <li>Pagination 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Pagination 支持定制 <code>selectComponentClass</code>。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32132" target="_blank">#32132</a></li> 
   <li>Pagination <code>simple</code> 属性下中翻页 input 增加 box-shadow。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32528" target="_blank">#32528</a></li> 
  </ul> </li> 
 <li>Upload 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复 Upload <code>listStyle="picture"</code> 下加载中样式错位的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32664" target="_blank">#32664</a></li> 
   <li>修复 Upload 错误背景颜色。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32051" target="_blank">#32051</a></li> 
  </ul> </li> 
 <li>InputNumber 
  <ul style="margin-left:0; margin-right:0"> 
   <li>InputNumber 增加 <code>addonBefore</code> 和 <code>addonAfter</code> 属性支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31432" target="_blank">#31432</a></li> 
   <li>InputNumber 新增 <code>controls</code> 属性用于控制是否显示加减按钮。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31548" target="_blank">#31548</a></li> 
   <li>InputNumber <code>formatter</code> 支持额外参数用以检测当前变更是否为用户输入。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31030" target="_blank">#31030</a></li> 
   <li>修复 InputNumber 操作杆箭头未居中对齐的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32409" target="_blank">#32409</a></li> 
   <li>聚焦 InputNumber 时将始终显示加减操作区。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31911" target="_blank">#31911</a></li> 
  </ul> </li> 
 <li>DatePicker 
  <ul style="margin-left:0; margin-right:0"> 
   <li><code>DatePicker</code> 和 <code>RangePicker</code> 现在支持 <code>nextIcon</code>、<code>prevIcon</code>、<code>superNextIcon</code> 和 <code>superPrevIcon</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31703" target="_blank">#31703</a></li> 
   <li>修复 RangePicker 的 <code>defaultPickerValue</code> 不生效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32107" target="_blank">#32107</a></li> 
  </ul> </li> 
 <li>Notification 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Notification 支持 <code>maxCount</code> 属性以限制最大显示数。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31807" target="_blank">#31807</a></li> 
   <li>修复多次调用 Notification 时 <code>closeIcon</code> 配置无法覆盖的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32359" target="_blank">#32359</a></li> 
  </ul> </li> 
 <li>增加 Menu.Divider 的 <code>dashed</code> 属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31379" target="_blank">#31379</a></li> 
 <li>Skeleton.Button 添加 <code>block</code> 属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30902" target="_blank">#30902</a></li> 
 <li>Popconfirm 组件的 <code>onConfirm</code> 允许返回一个 Promise。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30871" target="_blank">#30871</a></li> 
 <li>修复 Card 设置 <code>tabs</code> 后当 <code>tabPosition: 'left'</code> 时的样式问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32695" target="_blank">#32695</a></li> 
 <li>修复 Radio <code>type</code> 属性被覆盖导致无法点击的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32463" target="_blank">#32463</a></li> 
 <li>修复英文国际化文案 <code>Ok</code> 为 <code>OK</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32259" target="_blank">#32259</a></li> 
 <li>修复 Switch <code>loading</code> 按钮位置不正确的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32216" target="_blank">#32216</a></li> 
 <li>修复 Grid Col <code>flex</code> 在内容过长的时候缩放失效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32160" target="_blank">#32160</a></li> 
 <li>修复调用 <code>message.useMessage</code> 时未使用 ConfigProvider 中的 <code>getPopupContainer</code> 返回元素作为容器的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31939" target="_blank">#31939</a></li> 
 <li>优化 Image 在小尺寸下省略预览文本。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F29900" target="_blank">#29900</a></li> 
 <li>修复 Alert <code>message</code> 为空时 dom 节点还在的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32057" target="_blank">#32057</a></li> 
 <li>修复 Anchor 组件包含空格时 <code>targetOffset</code> 属性不生效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31952" target="_blank">#31952</a></li> 
 <li>新增 Less 变量 <code>@checkbox-border-radius</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31360" target="_blank">#31360</a></li> 
 <li>Avatar 增加 <code>crossOrigin</code> 参数以解决跨域问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31273" target="_blank">#31273</a></li> 
 <li>RTL 
  <ul style="margin-left:0; margin-right:0"> 
   <li>优化 Alert 关闭按钮在 RTL 模式下的显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32286" target="_blank">#32286</a></li> 
   <li>优化 Table 表头操作按钮在 RTL 模式下显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32283" target="_blank">#32283</a></li> 
   <li>优化 Collapse 按钮在 RTL 模式下位置显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32282" target="_blank">#32282</a></li> 
   <li>优化 Badge 数字在 RTL 模式下显示和动画。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32281" target="_blank">#32281</a></li> 
   <li>优化 InputNumber 操作栏 RTL 模式下边框样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32272" target="_blank">#32272</a></li> 
   <li>优化 Dropdown RTL 模式下 icon 显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32271" target="_blank">#32271</a></li> 
   <li>修复 Transfer 列表在 RTL 模式下 <code>direction</code> 取值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31903" target="_blank">#31903</a></li> 
  </ul> </li> 
 <li>国际化 
  <ul style="margin-left:0; margin-right:0"> 
   <li>添加格鲁吉亚语言环境。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32106" target="_blank">#32106</a></li> 
   <li>补充 de_DE 中 Image 字段。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32001" target="_blank">#32001</a></li> 
   <li>添加马拉雅拉姆语 (ml_IN) 语言环境。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31521" target="_blank">#31521</a></li> 
   <li>添加乌尔都语 (ur_PK) 语言环境。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31346" target="_blank">#31346</a></li> 
   <li>添加孟加拉语 (bn_BD) 语言环境。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31257" target="_blank">#31257</a></li> 
  </ul> </li> 
 <li>TypeScript 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修改 Spin <code>tip</code> 的类型为 ReactNode。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32733" target="_blank">#32733</a></li> 
   <li>修复 Message duration 类型定义。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32524" target="_blank">#32524</a></li> 
   <li>修复 ConfigProvider 中 <code>getPopupContainer</code> 的参数类型。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32406" target="_blank">#32406</a></li> 
   <li>修复 Table 丢失泛型定义。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32358" target="_blank">#32358</a></li> 
   <li>修复 Switch <code>id</code> 属性定义。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32237" target="_blank">#32237</a></li> 
   <li>修复 Button 的 <code>type</code> 的 TS 类型定义。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32004" target="_blank">#32004</a></li> 
   <li>完备 Pagination 的 <code>locale</code> TS 类型定义。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32128" target="_blank">#32128</a></li> 
   <li>完善并导出 DropdownButton 的 <code>DropdownButtonType</code> TS 类型定义。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31957" target="_blank">#31957</a></li> 
   <li>调整 List 组件 <code>rowKey</code> 类型为 React.key。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32033" target="_blank">#32033</a></li> 
   <li>修复 DatePicker <code>ref</code> 类型。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31993" target="_blank">#31993</a></li> 
   <li>更新 Drawer 中 <code>levelMove</code> 类型定义。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30714" target="_blank">#30714</a></li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.17.0" target="_blank">https://github.com/ant-design/ant-design/releases/tag/4.17.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            