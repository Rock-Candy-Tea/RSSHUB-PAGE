
---
title: 'Ant Design Mobile 5.0.0-beta.16 发布，AntD 移动端设计规范'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9667'
author: 开源中国
comments: false
date: Fri, 15 Oct 2021 06:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9667'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ant Design Mobile 5.0.0-beta.16 发布了。Ant Design Mobile 即 Ant Design 移动端设计规范，<code>antd-mobile</code> 是 Ant Design 的移动规范的 React 实现，服务于蚂蚁及口碑无线业务。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>更新内容如下：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>特性 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Collapse.Panel 增加了 <code>destroyOnClose</code> 属性</li> 
   <li>Collapse.Panel 增加了 <code>onClick</code> 属性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4134" target="_blank">#4134</a></li> 
   <li>Selector 的 <code>onChange</code> 属性增加了额外的 <code>items</code> 参数</li> 
   <li>Image 增加了 <code>onClick</code> 属性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4162" target="_blank">#4162</a></li> 
   <li>TextArea 的 <code>showCount</code> 属性支持了 render props <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4165" target="_blank">#4165</a></li> 
   <li>优化了 Checkbox 和 Radio 的图标样式，并且增加了一些 CSS 变量</li> 
   <li>Space 移除了 <code>size</code> 属性，改为通过 CSS 变量 <code>--gap</code> <code>--vertical-gap</code> <code>--horizontal-gap</code> 调整间距大小</li> 
  </ul> </li> 
 <li>优化 
  <ul style="margin-left:0; margin-right:0"> 
   <li>避免 Picker 和 PickerView 组件的 <code>onSelect</code> 事件被过度频繁地触发的问题</li> 
  </ul> </li> 
 <li>修复 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复了 Popup Collapse.Panel Mask 组件的 <code>forceRender</code> 和 <code>destroyOnClose</code> 属性未生效的问题</li> 
   <li>修复了 Picker 组件在关闭时额外地触发了 <code>onSelect</code> 属性的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4143" target="_blank">#4143</a></li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">迁移建议</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>检查是否有用到 <code>Space</code> 的 <code>size</code> 属性，需要调整为通过 CSS 变量的形式进行设置</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Freleases%2Ftag%2Fv5.0.0-beta.16" target="_blank">https://github.com/ant-design/ant-design-mobile/releases/tag/v5.0.0-beta.16</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            