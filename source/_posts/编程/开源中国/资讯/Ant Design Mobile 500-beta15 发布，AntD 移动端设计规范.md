
---
title: 'Ant Design Mobile 5.0.0-beta.15 发布，AntD 移动端设计规范'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2213'
author: 开源中国
comments: false
date: Mon, 11 Oct 2021 07:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2213'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ant Design Mobile 5.0.0-beta.15 发布了。Ant Design Mobile 即 Ant Design 移动端设计规范，<code>antd-mobile</code> 是 Ant Design 的移动规范的 React 实现，服务于蚂蚁及口碑无线业务。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>更新内容如下：</strong></p> 
<ul> 
 <li>特性 
  <ul> 
   <li>DatePicker 支持了<span> </span><code>title</code><span> </span>属性<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4084" target="_blank">#4084</a></li> 
   <li>PageIndicator 增加了一些 CSS 变量，原有的 CSS 变量也进行了调整<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4088" target="_blank">#4088</a></li> 
   <li>新增了 SideBar 组件<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4092" target="_blank">#4092</a></li> 
   <li>Dialog 的<span> </span><code>Action</code><span> </span>配置支持了传入<span> </span><code>style</code><span> </span>和<span> </span><code>className</code><span> </span>等 native props<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4121" target="_blank">#4121</a></li> 
   <li>Form.Item 增加了<span> </span><code>hidden</code><span> </span>属性<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4133" target="_blank">#4133</a></li> 
  </ul> </li> 
 <li>优化 
  <ul> 
   <li>优化了 Ellipsis 的计算逻辑<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4087" target="_blank">#4087</a></li> 
   <li>ImageUploader 在上传图片失败时增加了错误信息的打印<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4111" target="_blank">#4111</a></li> 
   <li>调整了 Form 的字段必填样式<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4131" target="_blank">#4131</a></li> 
   <li>Dropdown 的<span> </span><code>forceRender</code><span> </span>从 Dropdown 移至了 Dropdown.Item</li> 
   <li>优化了 Swiper 在部分内容较少的情况下的动画效果</li> 
  </ul> </li> 
 <li>修复 
  <ul> 
   <li>修复了 Dialog 最后一个按钮右侧边框未去除的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4115" target="_blank">#4115</a></li> 
   <li>修复了在部分情况下 rem 布局的 px 换算计算精度较低导致的位置偏移问题</li> 
   <li>修复了 Picker 的<span> </span><code>onSelect</code><span> </span>属性没有触发的问题</li> 
   <li>修复了 Picker、CascadePicker 在部分情况下在执行<span> </span><code>props.children(...)</code><span> </span>时传入了错误的<span> </span><code>items</code><span> </span>数据的问题</li> 
   <li>修复了 ImageUploader 在连续选择两张相同图片时未能正确触发上传事件的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4137" target="_blank">#4137</a></li> 
  </ul> </li> 
</ul> 
<hr> 
<p style="color:#24292f; text-align:start">迁移建议</p> 
<ul> 
 <li>PageIndicator 的 CSS 变量进行了调整，所以需要把原来的<span> </span><code>--active-color</code><span> </span>改为<span> </span><code>--active-dot-color</code>，<code>--non-active-color</code><span> </span>改为<span> </span><code>--dot-color</code></li> 
 <li>如果有用到 Dropdown 的<span> </span><code>forceRender</code><span> </span>属性，需要调整到 Dropdown.Item 上</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Freleases%2Ftag%2Fv5.0.0-beta.15" target="_blank">https://github.com/ant-design/ant-design-mobile/releases/tag/v5.0.0-beta.15</a></p>
                                        </div>
                                      
</div>
            