
---
title: 'WebStorm 2021.2.1 发布，大幅改进对 Vue 的支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6229'
author: 开源中国
comments: false
date: Thu, 26 Aug 2021 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6229'
---

<div>   
<div class="content">
                                                                    
                                                        <p>WebStorm 2021.2.1 是 WebStorm 2021.2 的第一个错误修复更新，此次更新包含了对 Vue 的修复和改进，尤其是对 <code><script setup></code> 的支持。</p> 
<h3>对 Vue 的改进</h3> 
<p>WebStorm 2021.2.1 包括几个期待已久的对 Vue 支持的改进。IDE 现在支持 <code><script setup></code> RFC 的最终版本。</p> 
<p><img alt height="350" src="https://static.oschina.net/uploads/space/2021/0826/072726_lCSa_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>去年，WebStorm 增加了对 <code>script setup</code> 实验性版本的支持，从那时起，RFC 已经出现了不少的变化。随着 Vue 3.2 中 <code>script setup</code> 的稳定发布，我们重新设计了对这一功能的支持，因此从现在起你可以在项目中使用它而不会有任何问题。</p> 
<h3>这个版本中对 Vue 的其他改进包括：</h3> 
<ul> 
 <li>现在支持 Vue 3 样式选择器，如 <code>:deep</code> 和 <code>:slotted</code> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-52145" target="_blank">WEB-52145</a>).</li> 
 <li>当父元素是一个未知标签时，代码补全不会中断 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-42754" target="_blank">WEB-42754</a>).</li> 
 <li>解决了 Composition API 的几个问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-50510" target="_blank">WEB-50510</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-48792" target="_blank">WEB-48792</a>).</li> 
 <li>修正了当一个 prop 具有所需属性时，推断出的 prop 类型错误的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-50190" target="_blank">WEB-50190</a>).</li> 
 <li>TypeScript 服务不应该再在你的 Vue 项目中停止工作 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-47248" target="_blank">WEB-47248</a>).</li> 
 <li>修复了 Pug 支持中的各种回归问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-52050" target="_blank">WEB-52050</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-51988" target="_blank">WEB-51988</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-51614" target="_blank">WEB-51614</a>).</li> 
</ul> 
<h3>其他值得关注的修复：</h3> 
<ul> 
 <li>添加了选择是否要在代码补全时插入大括号的功能 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-31404" target="_blank">WEB-31404</a>)</li> 
 <li>解决了从 WSL 2 打开项目时导致 IDE 冻结的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-273398" target="_blank">IDEA-273398</a>)</li> 
 <li>添加了对 Angular 模板中的 shorthand 属性的支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-51572" target="_blank">WEB-51572</a>)</li> 
 <li>重新设计了对 Tailwind CSS 的支持，使其可以使用 JIT 模式 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-50318" target="_blank">WEB-50318</a>)</li> 
 <li>内置终端中使用的 Ctrl+箭头键现在应该可以正常工作 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-271542" target="_blank">IDEA-271542</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconfluence.jetbrains.com%2Fdisplay%2FWI%2FWebStorm%2B2021.2.1%2BRelease%2BNotes" target="_blank">https://confluence.jetbrains.com/display/WI/WebStorm+2021.2.1+Release+Notes</a></p>
                                        </div>
                                      
</div>
            