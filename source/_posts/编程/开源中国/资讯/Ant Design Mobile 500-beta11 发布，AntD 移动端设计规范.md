
---
title: 'Ant Design Mobile 5.0.0-beta.11 发布，AntD 移动端设计规范'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4152'
author: 开源中国
comments: false
date: Sun, 26 Sep 2021 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4152'
---

<div>   
<div class="content">
                                                                                            <p>Ant Design Mobile 5.0.0-beta.11 发布了。Ant Design Mobile 即 Ant Design 移动端设计规范，<code>antd-mobile</code> 是 Ant Design 的移动规范的 React 实现，服务于蚂蚁及口碑无线业务。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>更新内容如下：</strong></p> 
<ul> 
 <li>特性 
  <ul> 
   <li>增加了配套的图标库<span> </span><code>antd-mobile-icons</code>，其他组件中用到的图标也进行了替换</li> 
   <li>Ellipsis 支持了中间省略<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4015" target="_blank">#4015</a></li> 
   <li>Mask 组件试验性地增加了对无障碍的支持</li> 
   <li>Mask 增加了<span> </span><code>afterShow</code><span> </span>属性</li> 
  </ul> </li> 
 <li>优化 
  <ul> 
   <li>Loading 组件进行了重构，改为基于 svg 实现，同时移除了<span> </span><code>size</code><span> </span>属性<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4012" target="_blank">#4012</a></li> 
   <li>Mask 和 Popup 的动画改为基于 react-spring 实现，更加自然细腻</li> 
   <li>调整了 Dialog 的<span> </span><code>getContainer</code><span> </span>属性类型定义<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4028" target="_blank">#4028</a></li> 
   <li>调整了 Popover 的<span> </span><code>trigger</code><span> </span><code>placement</code><span> </span>属性类型定义<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4032" target="_blank">#4032</a></li> 
   <li>Popover.Menu 的<span> </span><code>onSelect</code><span> </span>属性改名为<span> </span><code>onAction</code>，和其他组件保持一致<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4032" target="_blank">#4032</a></li> 
  </ul> </li> 
 <li>修复 
  <ul> 
   <li>修复了 NavBar 返回图标自定义设置失效的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F3999" target="_blank">#3999</a></li> 
   <li>修复了<span> </span><code>Toast.show</code><span> </span>中<span> </span><code>afterClose</code><span> </span>事件重复触发的问题</li> 
   <li>修复了 Stepper 在外部<span> </span><code>value</code><span> </span>变化时，可能不会同步到输入框的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fpull%2F4021" target="_blank">#4021</a></li> 
  </ul> </li> 
</ul> 
<hr> 
<p style="color:#24292f; text-align:start">迁移建议</p> 
<ul> 
 <li>检查是否有对 Loading 组件的使用，现在的 Loading 已经不再支持设置<span> </span><code>size</code><span> </span>属性了，它会自动根据当前的字号调整大小</li> 
 <li>检查是否用到了 Popover.Menu 的<span> </span><code>onSelect</code><span> </span>属性，需要同步把命名改为<span> </span><code>onAction</code></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Freleases%2Ftag%2Fv5.0.0-beta.11" target="_blank">https://github.com/ant-design/ant-design-mobile/releases/tag/v5.0.0-beta.11</a></p>
                                        </div>
                                      
</div>
            