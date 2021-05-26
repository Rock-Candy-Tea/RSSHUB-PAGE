
---
title: 'Ant Design 4.16.0 发布，企业级 UI 设计语言和 React 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9676'
author: 开源中国
comments: false
date: Wed, 26 May 2021 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9676'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ant Design 4.16.0 发布了。Ant Design 是一套企业级的 UI 设计语言和 React 实现，使用 TypeScript 构建，提供完整的类型定义文件，自带提炼自企业级中后台产品的交互语言和视觉风格、开箱即用的高质量 React 组件与全链路开发和设计工具体系。</p> 
<p>此版本更新内容如下：</p> 
<ul> 
 <li>重构 Menu，支持键盘操作以及无障碍体验优化。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30382" target="_blank">#30382</a></li> 
 <li>重新设计 Table 筛选和排序按钮的位置，使其归属列更明确。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30651" target="_blank">#30651</a></li> 
 <li>Table 
  <ul> 
   <li>Table.Summary 支持  <code>sticky</code>  模式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30631" target="_blank">#30631</a></li> 
   <li>修复有固定列的 Table 内嵌 Table 的额外边距丢失的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30587" target="_blank">#30587</a></li> 
   <li>Table 新增  <code>expandable.fixed</code>  属性用于设置扩展图标固定。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F29959" target="_blank">#29959</a></li> 
  </ul> </li> 
 <li>Upload 
  <ul> 
   <li>Upload 组件  <code>itemRender</code>  添加  <code>actions</code>  调用参数。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30236" target="_blank">#30236</a></li> 
   <li>Upload 从拖动事件中删除  <code>stopPropagation</code> ，并添加 <code>onDrop</code>  回调。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30319" target="_blank">#30319</a></li> 
  </ul> </li> 
 <li>Typography 
  <ul> 
   <li>Typography 增加斜体字支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30458" target="_blank">#30458</a></li> 
   <li>修复 Typography 配置  <code>ellipsis=&#123;&#123; suffix: 'xxx' &#125;&#125;</code>  时换行闪动问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30582" target="_blank">#30582</a></li> 
  </ul> </li> 
 <li>Collapse 
  <ul> 
   <li>修复 Collapse 不指定  <code>header</code>  时箭头错位的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30586" target="_blank">#30586</a></li> 
   <li>修复 Collapse 隐藏时设置  <code>activeKey</code>  时内容会消失的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30555" target="_blank">#30555</a></li> 
  </ul> </li> 
 <li>修复 Menu.SubMenu 的  <code>icon</code>  设置为第三方 icon 库时的样式问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30642" target="_blank">@#30642</a></li> 
 <li>修复 Descriptions 单独引入样式丢失的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30602" target="_blank">@#30602</a></li> 
 <li>Radio.Group 支持  <code>data-*</code>  和  <code>aria-*</code>  属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30507" target="_blank">#30507</a></li> 
 <li>Statistic.CountDown 组件增加  <code>onChange</code>  事件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30265" target="_blank">#30265</a></li> 
 <li>PageHeader 的  <code>breadcrumb</code>  中允许设置为组件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30019" target="_blank">#30019</a></li> 
 <li>ConfigProvider 支持动态设置  <code>prefixCls</code> 。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30625" target="_blank">#30625</a></li> 
 <li>修复 Anchor 指定  <code>getCurrentAnchor</code>  后无法触发  <code>onChange</code>  的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30601" target="_blank">#30601</a></li> 
 <li>修复 Notification  <code>useNotification</code>  生成的通知框  <code>className</code>  作用范围不一致的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30588" target="_blank">#30588</a></li> 
 <li>修复 Tabs  <code>tabBarGutter</code>  属性失效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30545" target="_blank">#30545</a></li> 
 <li>改写 Space 使用  <code>flexGap</code>  以代替  <code>margin</code>  样式以处理某些边界情况下的布局问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30023" target="_blank">#30023</a></li> 
 <li>修复 Form 校验错误状态下 Input.Group 和 Cascader 边框颜色错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30640" target="_blank">#30640</a></li> 
 <li>国际化 
  <ul> 
   <li>补充罗马尼亚语国际化。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30419" target="_blank">#30419</a></li> 
   <li>补充荷兰语（荷兰 NL）及荷兰语（比利时 BE）国际化。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30389" target="_blank">#30389</a></li> 
  </ul> </li> 
 <li>TypeScript 
  <ul> 
   <li>Space TypeScript 定义支持 HTMLAttribute 属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F30590" target="_blank">#30590</a></li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.16.0" target="_blank">https://github.com/ant-design/ant-design/releases/tag/4.16.0</a></p>
                                        </div>
                                      
</div>
            