
---
title: 'Ant Design Mobile 5.0.0-rc.2 发布，AntD 移动端设计规范'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=999'
author: 开源中国
comments: false
date: Sun, 05 Dec 2021 07:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=999'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ant Design Mobile 5.0.0-rc.2 发布了。Ant Design Mobile 即 Ant Design 移动端设计规范，<code>antd-mobile</code> 是 Ant Design 的移动规范的 React 实现，服务于蚂蚁及口碑无线业务。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>更新内容如下：</strong></p> 
<ul> 
 <li>特性 
  <ul> 
   <li>新增了 Cascader 和 CascaderView 组件<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4470" target="_blank">#4470</a></li> 
   <li>VirtualInput 新增了<span> </span><code>clearable</code><span> </span>属性<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4483" target="_blank">#4483</a></li> 
   <li>类型<span> </span><code>FileItem</code><span> </span>现在调整叫做<span> </span><code>ImageUploadItem</code><span> </span>了，并且支持了用户手动置顶<span> </span><code>key</code><span> </span>属性和<span> </span><code>thumbnailUrl</code><span> </span>属性</li> 
   <li>ActionSheet<span> </span><code>Action</code><span> </span>类型中<span> </span><code>text</code><span> </span>和<span> </span><code>description</code><span> </span>属性支持了 ReactNode<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4492" target="_blank">#4492</a></li> 
   <li>List 支持了<span> </span><code>--padding-left</code><span> </span>CSS 变量</li> 
  </ul> </li> 
 <li>优化 
  <ul> 
   <li>NumberKeyboard 退格键支持长按连续删除<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4477" target="_blank">#4477</a></li> 
   <li>一些动画相关的组件（Mask & Dialog & Popup）避免在组件卸载后触发状态更新<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4479" target="_blank">#4479</a></li> 
   <li>调整了 Dialog 的内容文字大小</li> 
   <li>调整了 Toast 的一些样式</li> 
   <li>Form 的必填星号移动到了左侧</li> 
   <li>Swiper 的<span> </span><code>loop</code><span> </span>属性的默认值调整成了<span> </span><code>false</code>，<code>stuckAtBoundary</code><span> </span>属性的默认值调整成了<span> </span><code>true</code></li> 
  </ul> </li> 
 <li>修复 
  <ul> 
   <li>修复了 VirtualInput 在内容过长是不会自动滚动至光标所在位置的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4483" target="_blank">#4483</a></li> 
   <li>修复了 Swiper 在同时开启了<span> </span><code>vertical</code><span> </span><code>loop</code><span> </span>模式时，内容无法正确渲染的问题</li> 
   <li>修复了 Tag 当内容出现中文时，高度会意外变化的问题</li> 
   <li>修复了 ImageUploader 当图片出现重复时，删除图片行为可能异常的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4494" target="_blank">#4494</a></li> 
   <li>修复了 SearchBar 文字和图片没有对齐的问题</li> 
  </ul> </li> 
</ul> 
<hr> 
<p style="color:#000000; text-align:start">迁移建议</p> 
<ul> 
 <li>Swiper 的<span> </span><code>loop</code><span> </span>属性的默认值调整成了<span> </span><code>false</code>，<code>stuckAtBoundary</code><span> </span>属性的默认值调整成了<span> </span><code>true</code>，所以需要检查一下项目中 Swiper 组件对应的这两个属性是否配置正常</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Freleases%2Ftag%2Fv5.0.0-rc.2" target="_blank">https://github.com/ant-design/ant-design-mobile/releases/tag/v5.0.0-rc.2</a></p>
                                        </div>
                                      
</div>
            