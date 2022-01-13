
---
title: 'React Suite 5.5.0 版本更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8761'
author: 开源中国
comments: false
date: Thu, 13 Jan 2022 18:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8761'
---

<div>   
<div class="content">
                                                                                            <p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left">React Suite 一套 React 的 UI 组件库，贴心的 UI 设计，友好的开发体验。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">文档: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frsuitejs.com%2F" target="_blank">https://rsuitejs.com</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">设计: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frsuitejs.com%2Fdesign%2Fdefault%2F" target="_blank">https://rsuitejs.com/design/default/</a></p> </li> 
</ul> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0px; margin-right:0px; text-align:left">V5.5.0 版本发布，更新内容如下：</p> 
<h3 style="text-align:start">Bug 修复</h3> 
<ul> 
 <li><strong>Dropdown:</strong><span> </span>推断出 toggleAs 组件的 props (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fissues%2F2299" target="_blank">#2299</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fcommit%2F84611cc6f88e1d9cd712bc3f08be559d0a146ba0" target="_blank">84611cc</a>)</li> 
 <li><strong>InputNumber:</strong><span> 继承</span> html input 属性 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fissues%2F2298" target="_blank">#2298</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fcommit%2Fd7622eed72b36ed15e91f606027d2e540391bdc7" target="_blank">d7622ee</a>)</li> 
 <li><strong>MultiCascader:</strong><span> </span>修复不渲染所选值的计数 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fissues%2F2289" target="_blank">#2289</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fcommit%2F324e90c8499adf58cb25083fd5c99fe98eb9ecba" target="_blank">324e90c</a>)</li> 
 <li><strong>Tree:</strong><span> 修复拖拽时出现循环依赖对象</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fissues%2F2281" target="_blank">#2281</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fcommit%2F26cbaf2fd92ab562174e19cf55388c01fe22143a" target="_blank">26cbaf2</a>), closes<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fissues%2F2268" target="_blank">#2268</a></li> 
</ul> 
<h3 style="text-align:start">新特性</h3> 
<ul> 
 <li><strong>InputNumber:</strong><span> </span>支持键盘交互 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fissues%2F2294" target="_blank">#2294</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fcommit%2F46993e235ca3d3ee8b6faa16a5fa11a8ed544e3b" target="_blank">46993e2</a>)</li> 
 <li><strong>RangeSlider:</strong><span> </span>支持<span> </span><code>constraint</code><span> </span>prop (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fissues%2F2291" target="_blank">#2291</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fcommit%2Fa2d38a8efe4f85c28ce1f4ee79a89eda1e1cf7b0" target="_blank">a2d38a8</a>)</li> 
</ul> 
<h3 style="text-align:start">性能改进</h3> 
<ul> 
 <li><strong>styles:</strong><span> </span>简化 4 层的 CSS 复合选择器 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fissues%2F2282" target="_blank">#2282</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frsuite%2Frsuite%2Fcommit%2F304e8da0c2057d148bbad36674aba33382439949" target="_blank">304e8da</a>)</li> 
</ul>
                                        </div>
                                      
</div>
            