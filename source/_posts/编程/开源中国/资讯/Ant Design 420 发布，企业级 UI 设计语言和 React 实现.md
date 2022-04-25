
---
title: 'Ant Design 4.20 发布，企业级 UI 设计语言和 React 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6347'
author: 开源中国
comments: false
date: Mon, 25 Apr 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6347'
---

<div>   
<div class="content">
                                                                                            <p>Ant Design 4.20 现已发布，主要变化如下：</p> 
<ul> 
 <li>支持 React 18 以及严格模式。 
  <ul> 
   <li>修复 Form 在 React 18 的 StrictMode 下，错误信息无法更新的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35096" target="_blank">#35096</a></li> 
   <li>修复 Notification 和 Message 在 React 18 下抛出使用 <code>createRoot</code> 的警告信息。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35030" target="_blank">#35030</a></li> 
   <li>修复 BackTop 组件在严格模式下不能正常工作的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34858" target="_blank">#34858</a></li> 
  </ul> </li> 
 <li>新增 Segmented 分段控制器组件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34319" target="_blank">#34319</a> 
  <ul> 
   <li>4.20.0 正式版后，Segemented 的 <code>onChange</code> 回调函数的参数从 <code>ChangeEvent</code> 调整为 <code>value</code>。如果你使用了 <code>4.20.0-alpha.0</code> <code>4.20.0-alpha.1</code>，请注意这个变化。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35187" target="_blank">#35187</a></li> 
  </ul> </li> 
 <li>Form 
  <ul> 
   <li>Form 添加 <code>useWatch</code> 支持获取当前字段值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35036" target="_blank">#35036</a></li> 
   <li>Form 支持 <code>useFormInstance</code> 以获取当前上下文中的 Form 实例。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35039" target="_blank">#35039</a></li> 
   <li>修复 Form <code>labelCol=&#123;&#123; sm: 24 &#125;&#125;</code> 和 <code>wrapperCol=&#123;&#123; sm: 24 &#125;&#125;</code> 时样式错乱的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34907" target="_blank">#34907</a></li> 
  </ul> </li> 
 <li>Menu 添加 <code>items</code> 数据化菜单项支持以为将来性能提升做准备，并且 <code>children</code> 将会在下个大版本中废弃。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34559" target="_blank">#34559</a></li> 
 <li>Image PreviewGroup 支持顶部进度渲染。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35038" target="_blank">#35038</a></li> 
 <li>Upload 
  <ul> 
   <li>Upload <code>picture-card</code> 模式支持配置图片的 <code>crossOrigin</code> 属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34981" target="_blank">#34981</a></li> 
   <li>修复 Upload <code>prefixCls</code> 对列表不生效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34944" target="_blank">#34944</a></li> 
   <li>优化 Upload 操作按钮的样式细节。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35052" target="_blank">#35052</a></li> 
  </ul> </li> 
 <li>Table 
  <ul> 
   <li>Table 列筛选条件重置时，支持重置为默认值而非空值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34355" target="_blank">#34355</a></li> 
   <li>修复 Table <code>size="small"</code> 时列头背景色和选择列宽度的样式问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34963" target="_blank">#34963</a></li> 
   <li>补全 Table 的德语国际化文案。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34836" target="_blank">#34836</a></li> 
   <li>优化 Table 过滤列表的计算性能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35064" target="_blank">#35064</a></li> 
   <li>优化 Table <code>size="small"</code> 和 <code>size="middle"</code> 时选择下拉菜单的边距样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35173" target="_blank">#35173</a></li> 
  </ul> </li> 
 <li>Tree 
  <ul> 
   <li>Tree 组件的 <code>switcherIcon</code> 属性支持 render-prop。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34470" target="_blank">#34470</a></li> 
   <li>Tree 支持 <code>rootClassName</code> and <code>rootStyle</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34578" target="_blank">#34578</a></li> 
  </ul> </li> 
 <li>Breadcrumb 
  <ul> 
   <li>修复 Breadcrumb 抛出 <code>placement</code> 废弃警告的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35162" target="_blank">#35162</a></li> 
   <li>修复 Breadcrumb 展示非预期的数字符号的样式问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35123" target="_blank">#35123</a></li> 
   <li>为 Breadcrumb 层次结构增加可访问性支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34082" target="_blank">#34082</a></li> 
  </ul> </li> 
 <li>Anchor 
  <ul> 
   <li>Anchor <code>getCurrentAnchor</code> 参数中返回默认高亮项。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34799" target="_blank">#34799</a></li> 
   <li>重构 Anchor 为函数组件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35073" target="_blank">#35073</a></li> 
  </ul> </li> 
 <li>Cascader 
  <ul> 
   <li>Cascader 添加 <code>showCheckedStrategy</code> 用于配置回填方式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34568" target="_blank">#34568</a></li> 
   <li>修复 Cascader 的搜索结果未占满整个面板的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35019" target="_blank">#35019</a></li> 
  </ul> </li> 
 <li>Typography 的 <code>onCopy</code> 方法支持获取点击事件对象。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34655" target="_blank">#34655</a></li> 
 <li>Grid 支持 <code>justify="space-evenly"</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34606" target="_blank">#34606</a></li> 
 <li>Dialog 及 Image 支持 <code>rootClassName</code> 属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34574" target="_blank">#34574</a></li> 
 <li>修复 Skeleton 在没有 <code>children</code> 并设置 <code>loading</code> 为 false 时提示 <code>Nothing was returned from render</code> 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34872" target="_blank">#34872</a></li> 
 <li>优化 Switch 禁用色以更好适应非白底背景。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35103" target="_blank">#35103</a></li> 
 <li>移除 Tabs <code>overflow: hidden</code> 样式以修复 Select 和 sticky Table 在 Tabs 中的展现问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35195" target="_blank">#35195</a></li> 
 <li>修正 Steps 在 RTL 模式下样式问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35088" target="_blank">#35088</a></li> 
 <li>修复 Badge 在 RTL 模式下、独立使用时的动画效果。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34899" target="_blank">#34899</a></li> 
 <li>优化 Modal id 生成逻辑，以优化无障碍体验。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35072" target="_blank">#35072</a></li> 
 <li>修复 Select 和 AutoComplete 使用键盘向下滚动时行为异常的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35025" target="_blank">#35025</a></li> 
 <li>Spin 
  <ul> 
   <li>修复 Spin 动画样式在 Parcel 解析异常的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35005" target="_blank">#35005</a></li> 
   <li>Spin 添加 <code>aria</code> 属性以提升可访问性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34408" target="_blank">#34408</a></li> 
  </ul> </li> 
 <li>Dropdown 支持方向键切换选项。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34738" target="_blank">#34738</a></li> 
 <li>修复 Title、Text、Paragraph 组件不支持 <code>ref</code> 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34847" target="_blank">#34847</a></li> 
 <li>Input 
  <ul> 
   <li>Input.Group 对子组件屏蔽 Form.Item 的样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34764" target="_blank">#34764</a></li> 
   <li>调整 Form 下 TextArea 的样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34714" target="_blank">#34714</a></li> 
  </ul> </li> 
 <li>修复 Checkbox 缺少 <code>aria-checked</code> 属性导致屏幕阅读器识别错误的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34862" target="_blank">#34862</a></li> 
 <li>Less 
  <ul> 
   <li>替换 less 中的 html 选择器为对应变量。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35186" target="_blank">#35186</a></li> 
   <li>修改 less 中 <code>danger</code> 值从函数改为变量。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35113" target="_blank">#35113</a></li> 
   <li>箭头圆角使用固定值 2px 变量。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35086" target="_blank">#35086</a></li> 
  </ul> </li> 
 <li>TypeScript 
  <ul> 
   <li>修正 Upload 组件中 <code>UploadChangeParam<T></code> 内部 <code>fileList</code> 不使用泛型问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35158" target="_blank">#35158</a></li> 
   <li>更新 TypeScript 定义以兼容 <code>@types/react@18</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35075" target="_blank">#35075</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F35076" target="_blank">#35076</a></li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.20.0" target="_blank">https://github.com/ant-design/ant-design/releases/tag/4.20.0</a></p>
                                        </div>
                                      
</div>
            