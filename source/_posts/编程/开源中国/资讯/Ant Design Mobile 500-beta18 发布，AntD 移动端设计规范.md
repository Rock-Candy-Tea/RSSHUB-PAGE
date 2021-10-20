
---
title: 'Ant Design Mobile 5.0.0-beta.18 发布，AntD 移动端设计规范'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5337'
author: 开源中国
comments: false
date: Wed, 20 Oct 2021 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5337'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ant Design Mobile 5.0.0-beta.18 发布了。Ant Design Mobile 即 Ant Design 移动端设计规范，<code>antd-mobile</code> 是 Ant Design 的移动规范的 React 实现，服务于蚂蚁及口碑无线业务。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>更新内容如下：</strong></p> 
<ul> 
 <li>特性 
  <ul> 
   <li>Steps & Steps.Step 支持了<span> </span><code>className</code><span> </span>和<span> </span><code>style</code><span> </span>属性<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4185" target="_blank">#4185</a></li> 
   <li>Collapse.Panel 的<span> </span><code>title</code><span> </span>属性支持了<span> </span><code>ReactNode</code><span> </span>类型<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4197" target="_blank">#4197</a></li> 
   <li>Image 增加了<span> </span><code>lazy</code><span> </span>属性，支持懒加载<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4195" target="_blank">#4195</a></li> 
   <li>List.Item 增加了<span> </span><code>disabled</code><span> </span>属性<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4213" target="_blank">#4213</a></li> 
   <li>CheckList 支持了<span> </span><code>className</code><span> </span><code>style</code><span> </span><code>activeIcon</code><span> </span>属性<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4199" target="_blank">#4199</a></li> 
   <li>PullToRefresh 增加了<span> </span><code>renderText</code><span> </span>属性，支持完全自定义指示器的文案<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4220" target="_blank">#4220</a></li> 
  </ul> </li> 
 <li>优化 
  <ul> 
   <li>Mask Popup Toast Dialog Picker CascadePicker DatePicker NumberKeyboard 组件增加了<span> </span><code>stopPropagation</code><span> </span>属性，用来阻止事件的冒泡，并且默认是会阻止<span> </span><code>click</code><span> </span>事件的冒泡</li> 
   <li>ImageUploader 和 Picker 系列组件支持了国际化</li> 
  </ul> </li> 
 <li>修复 
  <ul> 
   <li>在 Form.Item 处于 disabled 状态时，不再会意外地触发<span> </span><code>onClick</code><span> </span>事件了<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4207" target="_blank">#4207</a></li> 
   <li>修复了在部分安卓设备下 Picker 滚轮无法拖动的问题</li> 
   <li>修复了 Swiper.Item 的点击事件无法触发的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4183" target="_blank">#4183</a></li> 
  </ul> </li> 
</ul> 
<hr> 
<p style="color:#24292f; text-align:start">迁移建议</p> 
<ul> 
 <li>Mask Popup Toast Dialog Picker CascadePicker DatePicker NumberKeyboard 现在会自动阻止<span> </span><code>click</code><span> </span>事件的冒泡了，这虽然是一个 break change，但是在绝大多数情况下都项目都不会有影响，而如果你之前在项目中有一些手动的<span> </span><code>stopPropagation</code><span> </span>处理，现在已经可以移除掉了</li> 
</ul> 
<p> 更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Freleases%2Ftag%2Fv5.0.0-beta.18" target="_blank">https://github.com/ant-design/ant-design-mobile/releases/tag/v5.0.0-beta.18</a></p>
                                        </div>
                                      
</div>
            