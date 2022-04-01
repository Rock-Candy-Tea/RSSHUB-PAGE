
---
title: 'Vite 2.9 发布，全新的前端构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0401/071712_FLeV_4252687.png'
author: 开源中国
comments: false
date: Fri, 01 Apr 2022 07:17:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0401/071712_FLeV_4252687.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Vite 2.9 已发布。</p> 
<p style="margin-left:0">主要更新内容：</p> 
<ul> 
 <li>提升冷启动速度</li> 
 <li>支持 CSS Sourcemaps</li> 
 <li>增强 Web Workers</li> 
 <li>面向插件和框架作者的新工具</li> 
</ul> 
<p><strong>提升冷启动速度</strong></p> 
<p>在 2.9 之前，Vite 首次在项目上运行 dev 需要执行扫描阶段以发现依赖关系，然后在启动服务器之前预先捆绑它们。在 2.9 中，扫描和预捆绑依赖项现在都是<strong>非阻塞</strong>的，因此服务器在冷启动期间会立即启动。</p> 
<p>此外，现在还支持请求在管道中流动，从而提高初始冷启动加载速度，并在重新处理和让 Vite 填充模块图和浏览器处理文件时，增加了发现新的缺失依赖的机会。在许多情况下，当发现新的依赖关系时，也不需要完全重新加载页面。</p> 
<p><strong>实验性支持 CSS Sourcemaps</strong></p> 
<p>此功能目前处于实验性阶段，默认情况下禁用，以避免对不需要它的用户造成性能损失。若需启用，将<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvitejs.dev%2Fconfig%2F%23css-devsourcemap" target="_blank">css.devSourcemap</a><span style="color:#24292f"> 设置为 </span><code>true</code><span style="color:#24292f">。</span></p> 
<p><strong>增强 Web Workers</strong></p> 
<p><span style="color:#24292f">Web Workers 现在支持生成 source map，此外稳健性也有所提升，并修复了旧版本中的多个问题。</span></p> 
<p><strong>面向插件和框架作者的新工具</strong></p> 
<ul> 
 <li>Client Server Communication API</li> 
 <li><code>importedCss</code> and <code>importedAssets</code> to RenderedChunk type</li> 
 <li>Optimize Custom Extensions (experimental)</li> 
</ul> 
<p style="margin-left:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2FCHANGELOG.md%23290-2022-03-30ub.com%252Fvitejs%252Fvite%252Fblob%252Fmain%252Fpackages%252Fvite%252FCHANGELOG.md%2523280-2022-02-09" target="_blank">详细内容查看 Changelog</a>。</p> 
<hr> 
<p style="margin-left:0">Vite（法语意思是 “快”，发音为 /vit/，类似 veet）是一种全新的前端构建工具。你可以把它理解为一个开箱即用的开发服务器 + 打包工具的组合，但是更轻更快。Vite 利用浏览器原生的 ES 模块支持和用编译到原生的语言开发的工具（如 esbuild）来提供一个快速且现代的开发体验。</p> 
<p style="margin-left:0"><img height="281" src="https://static.oschina.net/uploads/space/2022/0401/071712_FLeV_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0">Vite 有多快？在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepl.it%2F">Repl.it</a> 上从零启动一个基于 Vite 的 React 应用，浏览器页面加载完毕的时候，CRA（create-react-app）甚至还没有装完依赖。</p> 
<p style="margin-left:0">如果你还没听说过 Vite 到底是什么，可以到<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcn.vitejs.dev%2Fguide%2Fwhy.html">这里</a>了解一下项目的设计初衷。如果你想要了解 Vite 跟其它一些类似的工具有什么区别，可以参考这里的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcn.vitejs.dev%2Fguide%2Fcomparisons.html">对比</a>。</p>
                                        </div>
                                      
</div>
            