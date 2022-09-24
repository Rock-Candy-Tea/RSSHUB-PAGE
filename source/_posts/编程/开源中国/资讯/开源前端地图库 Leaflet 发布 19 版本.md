
---
title: '开源前端地图库 Leaflet 发布 1.9 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2228'
author: 开源中国
comments: false
date: Fri, 23 Sep 2022 21:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2228'
---

<div>   
<div class="content">
                                                                    
                                                        <p>v1.9的发布为Leaflet自2016年以来的首次重大版本升级奠定了基础！从那时起，很多事情都发生了变化，是时候让Leaflet与网络平台一起成长了。</p> 
<p>在这个版本之后，我们将把1.x的代码分支化，并将其置于维护模式中——<strong>只</strong>保留潜在的1.x版本用于关键的错误修复。尽管<strong>2.0版本</strong>还很遥远，需要一些时间才能成形，但我们计划做以下改变。</p> 
<ul> 
 <li><strong>放弃对Internet Explorer的支持。</strong>这已经是一个漫长的过程，但现在Internet Explorer已经<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.windows.com%2Fwindowsexperience%2F2022%2F06%2F15%2Finternet-explorer-11-has-retired-and-is-officially-out-of-support-what-you-need-to-know%2F" target="_blank">正式报废</a>，是时候说再见了。今后，Leaflet将转向一个常青的策略，针对Firefox、Chrome、Edge和Safari等浏览器。</li> 
 <li><strong>拥抱现代JavaScript。</strong>为了保持向后兼容，Leaflet完全是用ES5编写的，这是传统浏览器所支持的JavaScript版本。因此，我们无法利用许多伟大的JavaScript功能（例如，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses" target="_blank">标准化的类</a>，而不得不依赖我们<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fleafletjs.com%2Freference.html%23class" target="_blank">自己的实现</a>）。通过采用更现代的ECMAScript标准，我们可以开始努力使Leaflet与现代JavaScript库所期望的相一致。</li> 
 <li><strong>标准化的模块。</strong>当我们发布Leaflet v1时，JavaScript世界的格局非常不同，充满了竞争性的模块标准，如CommonJS、AMD和UMD。今天，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FModules" target="_blank">ECMAScript模块</a>已经成为将JavaScript生态系统统一在一个旗帜下的明确的发展方向。今后，Leaflet将只在一个标准化的模块系统中发布，大大降低了我们分布式代码的复杂性。</li> 
 <li><strong>移除Leaflet全局变量。</strong>作为一个使用Leaflet的开发者，你可能对大写字母L非常熟悉。这是Leaflet全局变量，Leaflet的所有功能都在这里。为了让编译器工具能够通过一个叫做<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FGlossary%2FTree_shaking" target="_blank">tree-shaking</a>的过程更好地消除死代码，我们正在删除这个全局变量。为了保持与旧插件的向后兼容性，我们将提供一个可以手动导入的垫片，以恢复这一功能。</li> 
</ul> 
<p>点击这里查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLeaflet%2FLeaflet%2Freleases%2Ftag%2Fv1.9.0" target="_blank">完整的更新日志</a>。</p> 
<p>补充说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLeaflet%2FLeaflet%2Freleases%2Ftag%2Fv1.9.1" target="_blank">v1.9.1补丁</a>已经发布，以解决与<em>Leaflet.markercluster</em>插件的兼容性。</p>
                                        </div>
                                      
</div>
            