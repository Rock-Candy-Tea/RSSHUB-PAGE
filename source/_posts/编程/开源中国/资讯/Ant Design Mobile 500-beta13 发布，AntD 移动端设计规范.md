
---
title: 'Ant Design Mobile 5.0.0-beta.13 发布，AntD 移动端设计规范'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8661'
author: 开源中国
comments: false
date: Tue, 28 Sep 2021 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8661'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ant Design Mobile 5.0.0-beta.13 发布了。Ant Design Mobile 即 Ant Design 移动端设计规范，<code>antd-mobile</code> 是 Ant Design 的移动规范的 React 实现，服务于蚂蚁及口碑无线业务。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>更新内容如下：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>特性 
  <ul style="margin-left:0; margin-right:0"> 
   <li>新增 PickerView 组件 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4039" target="_blank">#4039</a></li> 
   <li>Picker.Cascader 调整命名为独立的 CascadePicker 组件</li> 
   <li>Mask 增加了 <code>color</code> 属性，支持白色的遮罩</li> 
   <li>ImageUploader 支持了 <code>onDelete</code> 属性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4043" target="_blank">#4043</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4050" target="_blank">#4050</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4049" target="_blank">#4049</a></li> 
   <li>Form 支持了 <code>ref</code>，便于在类组件中使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4047" target="_blank">#4047</a></li> 
  </ul> </li> 
 <li>优化 
  <ul style="margin-left:0; margin-right:0"> 
   <li><code>SwipeAction.Action.onClick</code> 暴露出了点击事件</li> 
   <li>PullToRefresh 的 content 容器增加了 className <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4042" target="_blank">#4042</a></li> 
   <li>Mask <code>opacity</code> 属性的预设调整为了 <code>default</code> <code>thin</code> <code>thick</code> </li> 
   <li>Cascader 改名为 TreeSelect，同时移除了 Cascader.Multiple </li> 
   <li>优化了 ImageUploader <code>capture</code> 属性的类型定义</li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">迁移建议</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>检查是否有用到 <code>Picker.Cascader</code>，需要重命名为 <code>CascadePicker</code></li> 
 <li>检查是否有用到 <code>Cascader.Multiple</code>，现在已经不再支持</li> 
 <li>检查是否有给 Mask 组件设置 <code>opacity='dark'</code>，需要改为 <code>opacity='thick'</code></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Freleases%2Ftag%2Fv5.0.0-beta.13" target="_blank">https://github.com/ant-design/ant-design-mobile/releases/tag/v5.0.0-beta.13</a> </p>
                                        </div>
                                      
</div>
            