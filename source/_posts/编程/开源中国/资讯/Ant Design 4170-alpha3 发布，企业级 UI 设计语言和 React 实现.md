
---
title: 'Ant Design 4.17.0-alpha.3 发布，企业级 UI 设计语言和 React 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0915/062039_GA36_2744687.png'
author: 开源中国
comments: false
date: Wed, 15 Sep 2021 06:21:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0915/062039_GA36_2744687.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.17.0-alpha.3" target="_blank">Ant Design 4.17.0-alpha.3 </a>现<span style="color:#333333">已发布，主要变化如下：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f">Pagination</span><span> </span>支持定制 <code>selectComponentClass</code>。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32132" target="_blank">#32132</a></li> 
 <li>Tree 与 TreeSelect 支持 <code>placement</code> 属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32143" target="_blank">#32143</a></li> 
 <li>修复 Cascader 中 <code>popupClassName</code> 与 <code>popupPlacement</code> 属性无效问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32143" target="_blank">#32143</a></li> 
 <li>修复调用 <code>message.useMessage</code> 时未使用 ConfigProvider 中的 <code>getPopupContainer</code> 返回元素作为容器的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31939" target="_blank">#31939</a></li> 
 <li>修复 Table 中 <code>pagination.className</code> 不生效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32131" target="_blank">#32131</a></li> 
 <li>修复 RangePicker 的 <code>defaultPickerValue</code> 不生效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32107" target="_blank">#32107</a></li> 
 <li>修复 antd 编译产物缺失 <code>/style/default.css</code> 文件的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32116" target="_blank">#32116</a></li> 
 <li>修复 Tree 连接线在浏览器放大时一像素位置偏差的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32075" target="_blank">#32075</a></li> 
 <li>优化 Image 在小尺寸下省略预览文本。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F29900" target="_blank">#29900</a></li> 
 <li>添加格鲁吉亚语言环境。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32106" target="_blank">#32106</a></li> 
 <li>TypeScript 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复 Button 的 <code>type</code> 的 TS 类型定义。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32004" target="_blank">#32004</a> </li> 
   <li>完备 Pagination 的 <code>locale</code> TS 类型定义。[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F32128" target="_blank">#32128</a></li> 
   <li>完善并导出 DropdownButton 的 <code>DropdownButtonType</code> TS 类型定义。 [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F31957" target="_blank">#31957</a> </li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ant Design 是一套企业级 UI 设计语言和 React 组件库。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><img alt height="331" src="https://static.oschina.net/uploads/space/2021/0915/062039_GA36_2744687.png" width="960" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>特性</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>提炼自企业级中后台产品的交互语言和视觉风格。</li> 
 <li>开箱即用的高质量 React 组件。</li> 
 <li>使用 TypeScript 开发，提供完整的类型定义文件。</li> 
 <li>全链路开发和设计工具体系。</li> 
 <li>数十个国际化语言支持。</li> 
 <li>深入每个细节的主题定制能力。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>兼容环境</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>现代浏览器和 IE11（需要 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fant.design%2Fdocs%2Freact%2Fgetting-started-cn%23%25E5%2585%25BC%25E5%25AE%25B9%25E6%2580%25A7">polyfills</a>）。</li> 
 <li>支持服务端渲染。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.electronjs.org%2F">Electron</a></li> 
</ul>
                                        </div>
                                      
</div>
            