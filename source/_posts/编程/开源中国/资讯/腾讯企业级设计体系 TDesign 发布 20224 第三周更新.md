
---
title: '腾讯企业级设计体系 TDesign 发布 2022.4 第三周更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7379'
author: 开源中国
comments: false
date: Tue, 19 Apr 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7379'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">TDesign 是一款诞生于腾讯内部、拥有完整的设计价值观和视觉风格指南的企业级设计体系，同时提供了丰富的设计资源，在设计体系基础上产出基于 Vue、React、小程序等业界主流技术栈的组件库解决方案，适合用于构建设计统一/多端覆盖/跨技术栈的企业级前端应用。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前，TDesign 发布了 2022 年 4 月的第三周更新，带来如下变更：</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>组件库</strong></h2> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Vue2 for Web 发布<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.40.3" target="_blank"><strong>0.40.3 版</strong></a></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🐞 Bug Fixes</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Timepicker</code>： 修复手动清空<span> </span><code>value</code><span> </span>时异常的问题</li> 
 <li><code>Textarea</code>： 修复输入数字零时显示异常的问题</li> 
 <li><code>Menu</code>： 修复局部注册组件时报错的问题</li> 
 <li><code>Select</code>： 修复可过滤的选择器提前换行的问题</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🌈 Features</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Form</code>： 默认渲染<span> </span><code>extra DOM</code><span> </span>节点</li> 
 <li><code>Dialog</code>： 新增<span> </span><code>showInAttachedElement API</code><span> </span>用于控制是否仅在挂载元素中显示弹窗</li> 
 <li><code>Card</code>： 新增卡片组件</li> 
 <li><code>Swiper</code>： 新增轮播框组件</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.40.3" target="_blank">https://github.com/Tencent/tdesign-vue/releases/tag/0.40.3</a></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>React for Web 发布<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react%2Freleases%2Ftag%2F0.31.0" target="_blank"><strong>0.31.0 版</strong></a></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>⚠️BREAKING CHANGES</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>FormItem<span> </span></code>样式调整，默认渲染<span> </span><code>extra</code><span> </span>文本节点占位，<code>FormItem</code><span> </span>上下<span> </span><code>margin</code><span> </span>有所调整 ，存在不兼容更新</li> 
 <li><code>Popconfirm</code>： 移除<span> </span><code>PopConfirm</code><span> </span>组件导出，请更改为<span> </span><code>Popconfirm</code></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🐞 Bug Fixes</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Cascader</code>： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复<span> </span><code>filterable</code><span> </span>模式下展示异常</li> 
   <li>修复多选与筛选时文本过长的展示异常</li> 
  </ul> </li> 
 <li><code>Popup</code>： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复初始化翻转逻辑判断错误</li> 
   <li>修复嵌套浮层<span> </span><code>click</code><span> </span>时关闭异常</li> 
   <li>修复<span> </span><code>trigger</code><span> </span>元素变化后展示异常</li> 
  </ul> </li> 
 <li><code>Slider</code>： 修复<span> </span><code>max</code><span> </span>数值过大浏览器崩溃问题</li> 
 <li><code>Breadcrumb</code>： 修复面包屑初始样式被覆盖问题</li> 
 <li><code>GlobalConfig</code>： 修复<span> </span><code>ts</code><span> </span>类型问题</li> 
 <li><code>Menu</code>： 修复<span> </span><code>MenuGroup</code><span> </span>嵌套时样式问题</li> 
 <li><code>Select</code>： 修复输入事件异常</li> 
 <li><code>Dialog</code>： 修复<span> </span><code>destory</code><span> </span>函数未真正销毁组件问题</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🌈 Features</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Form</code>： 新增动态表单能力，可使用<span> </span><code>FormList</code><span> </span>组件管理表单项</li> 
 <li><code>Popconfirm</code>： 移除<span> </span><code>PopConfirm</code><span> </span>组件导出，请更改为<span> </span><code>Popconfirm</code></li> 
 <li><code>Popup</code>： 支持<span> </span><code>attach</code><span> </span>函数传入<span> </span><code>triggerNode</code></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react%2Freleases%2Ftag%2F0.31.0" target="_blank">https://github.com/Tencent/tdesign-react/releases/tag/0.31.0</a></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Miniprogram for WeChat 发布<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-miniprogram%2Freleases%2Ftag%2F0.8.0" target="_blank"><strong>0.8.0 版</strong></a></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>⚠️BREAKING CHANGES</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>CheckboxGroup</code>：<span> </span><code>change</code><span> </span>事件返回的<span> </span><code>value</code><span> </span>将会过滤非<span> </span><code>checkbox</code><span> </span>的值，存在不兼容更新</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🐞 Bug Fixes</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Steps</code>： 修复子步骤条不支持<span> </span><code>status</code><span> </span>的问题</li> 
 <li><code>Picker</code>： 修复出现空白的取消和确认按钮</li> 
 <li><code>Swiper</code>： 修复点击误触发翻页问题</li> 
 <li><code>Radio</code>： 修复<span> </span><code>label</code><span> </span>错误的渲染位置</li> 
 <li><code>Checkbox</code>： 修复<span> </span><code>label</code><span> </span>错误的渲染位置</li> 
 <li><code>Textarea</code>： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复缺失的<span> </span><code>label</code><span> </span>插槽</li> 
   <li>修复传入<span> </span><code>adjust-position</code><span> </span>不生效的问题</li> 
  </ul> </li> 
 <li><code>Transition</code>： 修复动画过程中触发<span> </span><code>leave</code><span> </span>会导致界面卡死的问题</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🌈 Features</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>DropdownMenu</code>： 新增下拉菜单组件</li> 
 <li><code>Radio</code>： 新增<span> </span><code>borderless</code><span> </span>属性</li> 
 <li><code>Checkbox</code>： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>新增<span> </span><code>borderless</code><span> </span>属性</li> 
   <li>新增<span> </span><code>theme<span> </span></code>属性，添加<span> </span><code>tag</code><span> </span>类型，默认值为<span> </span><code>default</code></li> 
  </ul> </li> 
 <li><code>CheckboxGroup</code>： 新增<span> </span><code>customStyle</code><span> </span>属性，透传<span> </span><code>style</code><span> </span>至根元素</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-miniprogram%2Freleases%2Ftag%2F0.8.0" target="_blank">https://github.com/Tencent/tdesign-miniprogram/releases/tag/0.8.0</a></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Vue3 for Mobile 发布<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-mobile-vue%2Freleases%2Ftag%2F0.8.4" target="_blank"><strong>0.8.4 版</strong></a></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🐞 Bug Fixes</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Swiper</code>： 修复动态绑定时出错问题</li> 
 <li><code>List</code>： 修复组件 demo 代码运行出错的问题</li> 
 <li><code>Input</code>：<span> </span><code>compositionend</code><span> </span>优化</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🌈 Features</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Tabs</code>： 新增<span> </span><code>stickyProps</code>，支持滚动到顶部时自动吸顶</li> 
 <li><code>PullDownRefresh</code>：<span> </span><code>loadingBarHeight</code><span> </span>属性支持<span> </span><code>string</code><span> </span>类型，代码优化</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-mobile-vue%2Freleases%2Ftag%2F0.8.4" target="_blank">https://github.com/Tencent/tdesign-mobile-vue/releases/tag/0.8.4</a></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>设计资源</strong></h2> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Figma for Starter 发布<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.figma.com%2Fcommunity%2Ffile%2F1096715990751064502" target="_blank"><strong>1.0.1 版</strong></a></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🔥 TDesign Starter 基础版已发布</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>提供适用于中后台多种场景的<span> </span><code>Figma</code><span> </span>页面模板设计文件</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.figma.com%2Fcommunity%2Ffile%2F1096715990751064502" target="_blank">https://www.figma.com/community/file/1096715990751064502</a> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Freleases%2Ftag%2Fv2022.4.17" target="_blank">https://github.com/Tencent/tdesign/releases/tag/v2022.4.17</a></p>
                                        </div>
                                      
</div>
            