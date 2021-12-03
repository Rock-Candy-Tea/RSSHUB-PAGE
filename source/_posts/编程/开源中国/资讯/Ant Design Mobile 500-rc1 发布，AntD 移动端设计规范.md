
---
title: 'Ant Design Mobile 5.0.0-rc.1 发布，AntD 移动端设计规范'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3821'
author: 开源中国
comments: false
date: Fri, 03 Dec 2021 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3821'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ant Design Mobile 5.0.0-rc.1 发布了。Ant Design Mobile 即 Ant Design 移动端设计规范，<code>antd-mobile</code> 是 Ant Design 的移动规范的 React 实现，服务于蚂蚁及口碑无线业务。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>更新内容如下：</strong></p> 
<ul> 
 <li>特性 
  <ul> 
   <li>DatePicker 支持了两种新的精度：<code>week</code><span> </span>和<span> </span><code>week-day</code><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4415" target="_blank">#4415</a></li> 
   <li>List 支持了自定义边框样式<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4444" target="_blank">#4444</a></li> 
   <li>Tag 增加了一些 CSS 变量<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4468" target="_blank">#4468</a></li> 
   <li>Tabs 增加了<span> </span><code>--content-padding</code><span> </span>CSS 变量<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4459" target="_blank">#4459</a></li> 
   <li>Space 增加了<span> </span><code>onClick</code><span> </span>属性<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4471" target="_blank">#4471</a></li> 
   <li>FloatingBubble 增加了<span> </span><code>--border-radius</code><span> </span>CSS 变量<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4473" target="_blank">#4473</a></li> 
   <li>CheckList 支持了 List 全部的 CSS 变量<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4457" target="_blank">#4457</a></li> 
  </ul> </li> 
 <li>优化 
  <ul> 
   <li>避免了 Picker 系列组件意外地触发<span> </span><code>onChange</code><span> </span>事件<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4442" target="_blank">#4442</a></li> 
   <li>Form.Item 的<span> </span><code>label</code><span> </span>和<span> </span><code>help</code><span> </span>属性支持了<span> </span><code>ReactNode</code><span> </span>类型<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4421" target="_blank">#4421</a></li> 
   <li>Dialog 在关闭动画进行时现在会自动禁止用户进行点击操作<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4441" target="_blank">#4441</a></li> 
   <li>SearchBar 在弹出虚拟键盘时，回车键的文字调整为“搜索”了<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4455" target="_blank">#4455</a></li> 
   <li>优化了 Picker 系列组件的性能</li> 
  </ul> </li> 
 <li>修复 
  <ul> 
   <li>修复了 Ellipsis 在新版 Chrome 中无法正常渲染的问题</li> 
   <li>修复了 Tabs 在内容高度动态变化时，高亮线条的动画会缺失的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4449" target="_blank">#4449</a></li> 
   <li>修复了 IndexBar 在 Panel 列表动态变化时，显示顺序错乱的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4443" target="_blank">#4443</a></li> 
   <li>修复了 IndexBar 手指划过边栏的文字时，无法触发选中操作的问题</li> 
   <li>修复了 Stepper 当按钮大小被调整之后，图标没有居中的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4460" target="_blank">#4460</a></li> 
   <li>修复了 Input 组件导致的关于<span> </span><code>enterKeyHint</code><span> </span>的 warning</li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Freleases%2Ftag%2Fv5.0.0-rc.1" target="_blank">https://github.com/ant-design/ant-design-mobile/releases/tag/v5.0.0-rc.1</a></p>
                                        </div>
                                      
</div>
            