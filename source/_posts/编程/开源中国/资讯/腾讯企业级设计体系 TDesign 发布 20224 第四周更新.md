
---
title: '腾讯企业级设计体系 TDesign 发布 2022.4 第四周更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2892'
author: 开源中国
comments: false
date: Tue, 26 Apr 2022 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2892'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">TDesign 是一款诞生于腾讯内部、拥有完整的设计价值观和视觉风格指南的企业级设计体系，同时提供了丰富的设计资源，在设计体系基础上产出基于 Vue、React、小程序等业界主流技术栈的组件库解决方案，适合用于构建设计统一/多端覆盖/跨技术栈的企业级前端应用。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前，TDesign 发布了 2022 年 4 月的第四周更新，带来如下变更：</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Vue2 for Web 发布<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.41.0" target="_blank"><strong>0.41.0 版</strong></a></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>⚠️BREAKING CHANGES</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Table: 拖拽排序修改为<span> </span><code>drag=sort</code><span> </span>表示列拖拽排序，<code>drag=row</code><span> </span>表示行拖拽排序，<code>drag=row-handler</code><span> </span>表示行手柄列拖拽排序。如果您使用了<code>drag="col"</code><span> </span>来实现行拖拽排序，请更为使用<span> </span><code>drag="row-handler"</code>。存在不兼容更新</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🐞 Bug Fixes</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Table</code>: 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复<span> </span><code>SSR</code><span> </span>场景下使用报错的问题</li> 
   <li>修复表头吸顶时不对齐的问题</li> 
   <li>按需引入<span> </span><code>Button</code><span> </span>组件，避免业务按需引入<span> </span><code>Table</code><span> </span>组件时出现组件不存在报错的问题</li> 
   <li>修复无法使用插槽自定义过滤图标的问题</li> 
   <li>解决<span> </span><code>TdBaseTableProps</code><span> </span>和<span> </span><code>TdPrimaryTableProps</code><span> </span>关于<span> </span><code>onCellClick</code><span> </span>的<span> </span><code>TS</code><span> </span>类型冲突</li> 
  </ul> </li> 
 <li><code>Alert</code>: 修复<span> </span><code>ts</code><span> </span>类型错误</li> 
 <li><code>Cascader</code>: 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复可过滤状态下的下拉面板拉起闪烁的问题</li> 
   <li>修复可过滤状态下的输入内容未被正常销毁的问题</li> 
  </ul> </li> 
 <li><code>Transfer</code>: 修复<span> </span><code>Transfer</code><span> </span>设置<span> </span><code>targetSort</code><span> </span>后未按预期展示的问题</li> 
 <li><code>ConfigProvider</code>: 修复<span> </span><code>ConfigProvider</code><span> </span>组件导出错误的问题</li> 
 <li><code>TreeSelect</code>: 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复<span> </span><code>value</code><span> </span>为数字<span> </span><code>0</code><span> </span>时，不渲染<span> </span><code>label</code><span> </span>的问题</li> 
   <li>修复<span> </span><code>onBlur</code><span> </span>和<span> </span><code>onClear</code><span> </span>触发时，不会清除<span> </span><code>filter function</code><span> </span>的问题</li> 
  </ul> </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🌈 Features</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Select</code>: 去掉选中和下拉项中的<span> </span><code>title</code><span> </span>属性</li> 
 <li><code>Table</code>: 支持树形结构展示，行展开或收起时触发<span> </span><code>onTreeExpandChange</code><span> </span>事件</li> 
 <li><code>Collapse</code>: 新增<span> </span><code>Collapse</code><span> </span>折叠面板组件，使用请参照 官网</li> 
 <li><code>Tree</code>: 
  <ul style="margin-left:0; margin-right:0"> 
   <li><code>Tree</code><span> </span>组件实现嵌套结构渲染能力</li> 
   <li>部分属性改为不让<span> </span><code>Vue</code><span> </span>监听，一定程度上提升组件性能，减少对外部组件交互性能的影响</li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue%2Freleases%2Ftag%2F0.41.0" target="_blank">https://github.com/Tencent/tdesign-vue/releases/tag/0.41.0</a></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Vue3 for Web 发布<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Freleases%2Ftag%2F0.12.2" target="_blank"><strong>0.12.2 版</strong></a></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🐞 Bug Fixes</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Transfer</code><span> </span>修复设置<span> </span><code>targetSort</code><span> </span>后未按预期展示的问题</li> 
 <li><code>Anchor</code>: 修复<span> </span><code>click</code><span> </span>事件参数不正确</li> 
 <li>修复<span> </span><code>slider</code><span> </span>引起的产物报错</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Freleases%2Ftag%2F0.12.2" target="_blank">https://github.com/Tencent/tdesign-vue-next/releases/tag/0.12.2</a></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Vue3 for Web 发布<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Freleases%2Ftag%2F0.13.0" target="_blank"><strong>0.13.0 版</strong></a></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>⚠️BREAKING CHANGES</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Table</code>: 拖拽排序，<code>drag=sort</code><span> </span>表示列拖拽排序，<code>drag=row</code><span> </span>表示行拖拽排序，<code>drag=row-handler</code><span> </span>表示行手柄列拖拽排序。如果您使用了<span> </span><code>drag="col"</code><span> </span>来实现行拖拽排序，请更为使用<span> </span><code>drag="row-handler"</code>。存在不兼容更新</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🐞 Bug Fixes</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Drawer</code>: 修复<span> </span><code>header</code><span> </span>属性无效问题</li> 
 <li><code>Textarea</code>: 修复在设置自动高度后，赋值后不高度不改变的问题</li> 
 <li><code>DatePicker</code>: 修复当传入值为非日期格式的情况页面卡死的问题</li> 
 <li><code>Transfer</code>: 修复设置<span> </span><code>targetSort</code><span> </span>后未按预期展示的问题</li> 
 <li><code>TreeSelect</code>: 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复<span> </span><code>value</code><span> </span>渲染异常问题</li> 
   <li>修复组件在多选时无<span> </span><code>v-model</code><span> </span>展示异常问题</li> 
  </ul> </li> 
 <li><code>Upload</code>: 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复上传失败状态流转问题</li> 
   <li>修复上传文件尺寸限制计算问题</li> 
  </ul> </li> 
 <li><code>Table</code>: 
  <ul style="margin-left:0; margin-right:0"> 
   <li>多级表头和列配置功能混合使用时，表格宽度渲染不正确问题</li> 
   <li>表头吸顶，不对齐问题</li> 
   <li>列配置功能，按需引入<span> </span><code>Button</code><span> </span>组件。避免业务按需引入<span> </span><code>Table</code><span> </span>组件时，出现组件不存在错误</li> 
   <li>无法使用插槽自定义过滤图标</li> 
   <li>修复<span> </span><code>TdBaseTableProps</code><span> </span>和<span> </span><code>TdPrimaryTableProps</code><span> </span>关于<span> </span><code>onCellClick</code><span> </span>的<span> </span><code>TS</code><span> </span>类型冲突</li> 
   <li>单选，报错<span> </span><code>e.stopPropagation is not a function</code></li> 
   <li>单选 和 多选触发了不应该触发的<span> </span><code>onChange</code><span> </span>事件</li> 
  </ul> </li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🌈 Features</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Table</code>: 
  <ul style="margin-left:0; margin-right:0"> 
   <li>支持简易列拖拽排序</li> 
   <li>树形结构，行展开或收起时，触发事件<span> </span><code>onTreeExpandChange</code></li> 
  </ul> </li> 
 <li><code>Checkbox</code>: 使用<span> </span><code>compositionAPI</code><span> </span>重构</li> 
 <li><code>Breadcrumb</code>: 使用<span> </span><code>compositionAPI</code><span> </span>重构</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-vue-next%2Freleases%2Ftag%2F0.13.0" target="_blank">https://github.com/Tencent/tdesign-vue-next/releases/tag/0.13.0</a></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>React for Web 发布<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react%2Freleases%2Ftag%2F0.32.0" target="_blank"><strong>0.32.0 版</strong></a></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>⚠️BREAKING CHANGES</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Table</code>: 重构<span> </span><code>table<span> </span></code>组件, 样式结构有所变动，存在不兼容更新</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🐞 Bug Fixes</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Select</code>: 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复多选+可搜索条件下输入问题</li> 
   <li>修复<span> </span><code>multiple</code><span> </span>模式删除问题</li> 
  </ul> </li> 
 <li><code>Progress</code>: 修复<span> </span><code>trackColor</code><span> </span>默认值导致背景色显示错误问题</li> 
 <li><code>Dialog</code>: 修复<span> </span><code>destroyOnClose</code><span> </span>为<span> </span><code>true</code><span> </span>时<span> </span><code>visible</code><span> </span>失效问题</li> 
 <li><code>Layout</code>: 修复<span> </span><code>ts</code><span> </span>类型警告</li> 
 <li><code>table</code>: 修复<span> </span><code>pagination</code><span> </span>数据同步问题</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🌈 Features</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Card</code>: 新增<span> </span><code>Card</code><span> </span>组件</li> 
 <li><code>ColorPicker</code>: 新增<span> </span><code>ColorPicker</code><span> </span>组件</li> 
 <li><code>Table</code>: 重构<span> </span><code>table</code><span> </span>组件, 修复众多问题</li> 
 <li><code>Divider</code>: 优化文本模式在竖型模式下样式问题</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-react%2Freleases%2Ftag%2F0.32.0" target="_blank">https://github.com/Tencent/tdesign-react/releases/tag/0.32.0</a></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Miniprogram for WeChat 发布<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-miniprogram%2Freleases%2Ftag%2F0.9.0" target="_blank"><strong>0.9.0 版</strong></a></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>⚠️BREAKING CHANGES</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Steps</code>: 子组件名称从<code><span> </span>t-step</code><span> </span>改成<span> </span><code>t-step-item</code></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🐞 Bug Fixes</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>Checkbox</code>: 优化渲染性能</li> 
 <li><code>Switch</code>: 修复无法选择的问题</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🌈 Features</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>ActionSheet</code>: 新增动作面板组件</li> 
 <li><code>NoticeBar</code>: 新增公告栏组件</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-miniprogram%2Freleases%2Ftag%2F0.9.0" target="_blank">https://github.com/Tencent/tdesign-miniprogram/releases/tag/0.9.0</a></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>解决方案及周边</strong></h2> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>TDesign Starter CLI 发布<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-starter-cli%2Freleases%2Ftag%2F0.2.1" target="_blank"><strong>0.2.1 版</strong></a></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>🌈 Features</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>支持<span> </span><code>React</code><span> </span>解决方案分页面功能下载</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详情见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign-starter-cli%2Freleases%2Ftag%2F0.2.1" target="_blank">https://github.com/Tencent/tdesign-starter-cli/releases/tag/0.2.1</a></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftdesign%2Freleases%2Ftag%2Fv.2022.4.24" target="_blank">https://github.com/Tencent/tdesign/releases/tag/v.2022.4.24</a></p>
                                        </div>
                                      
</div>
            