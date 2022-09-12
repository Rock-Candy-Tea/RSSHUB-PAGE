
---
title: 'Fresh 1.1 正式发布，Deno 全栈 Web 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-842de3268d50d201025a2d720daf839ebd1.png'
author: 开源中国
comments: false
date: Mon, 12 Sep 2022 07:30:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-842de3268d50d201025a2d720daf839ebd1.png'
---

<div>   
<div class="content">
                                                                                            <p>Fresh 1.1 稳定版已发布，新版本包含许多重要的改进，使 Fresh 更易于使用、更快，并且更实用。</p> 
<p><span style="background-color:#ffffff; color:#333333">Fresh 是 Deno 的全新全栈 Web 框架。默认情况下，使用 Fresh 构建的网页不会向客户端发送 JavaScript。该框架没有构建步骤，可以将部署时间缩短一个数量级。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Fresh 使用了一种不同的模型：默认情况下，开发者会将 0 KB 的 JS 发送给客户端。因为大多数渲染在服务器上完成，客户端只负责重新渲染交互性的小模块。这是一个开发者明确选择客户端渲染特定组件的模型。早在 2020 年，Jason Miller 在他的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjasonformat.com%2Fislands-architecture" target="_blank">Islands Architecture 博客文章</a>中就描述了这个模型。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Fresh 核心是</span><strong style="color:#333333">路由框架和模板引擎的组合</strong><span style="background-color:#ffffff; color:#333333">，支持在服务器上按需渲染页面。除了在服务器中提供的即时 (JIT) 渲染之外，Fresh 还提供了一个接口，用于在客户端上无缝渲染某些组件，以实现最大的交互性。该框架使用 Preact 和 JSX</span>（或 TSX）在服务器和客户端上进行渲染和模板化。客户端渲染在每个组件级别上是完全可选的，因此许多应用程序根本不会向客户端发送任何 JavaScript。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">由于 Fresh 没有构建步骤，因此开发者编写的代码直接就是在服务器和客户端上运行的代码。将 TypeScript 或 JSX 转换为纯 JavaScript 的任何必要转换都是在需要时即时完成的。这允许通过即时部署实现非常快速的迭代循环。</span></p> 
<div style="text-align:start"> 
 <p style="margin-left:0; margin-right:0">因为 Fresh 非常依赖动态服务器端渲染，所以速度必须快。Fresh 非常适合在 Deno Deploy、Netlify Edge Functions 或 Supabase Edge Functions 等边缘 runtime 场景运行。由于渲染过程在物理上非常靠近用户，从而可以最大限度地减少网络延迟。</p> 
 <p style="margin-left:0; margin-right:0"><strong>Fresh 亮点特性</strong></p> 
</div> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>无构建步骤</li> 
 <li>零配置</li> 
 <li>边缘 JIT 渲染</li> 
 <li>轻量且快速（框架不需要客户端 JS）</li> 
 <li>单个组件支持可选的客户端<span> </span><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FHydration_%28web_development%29" target="_blank">Hydration</a></strong></li> 
 <li>由于采用渐进式增强和使用原生浏览器功能而具有很强的适应性</li> 
 <li>开箱即用的 TypeScript</li> 
 <li>文件系统路由采用 Next.js</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-842de3268d50d201025a2d720daf839ebd1.png" referrerpolicy="no-referrer"></p> 
<p><strong>Fresh 1.1 更新亮点：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Ffresh-1.1%23automatic-jsx" target="_blank">支持自动默认使用 JSX 模式</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Ffresh-1.1%23plugins" target="_blank">插件</a> 
  <ul style="margin-left:0; margin-right:0"> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Ffresh-1.1%23official-twind-plugin" target="_blank">增加官方<code>twind</code><span>插件</span></a></li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Ffresh-1.1%23preact-signals-support" target="_blank">支持 Preact Signals</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Ffresh-1.1%23preact-devtools-support" target="_blank">支持 Preact DevTools</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Ffresh-1.1%23explicit-rendering-of-404-pages" target="_blank">显式渲染 404 页面</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Ffresh-1.1%23stacked-middleware" target="_blank">支持叠加中间件</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Ffresh-1.1%23experimental-denoserve-support" target="_blank">实验性支持<span> </span><code>Deno.serve</code></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Ffresh-1.1%23showcase--made-with-fresh-badges" target="_blank">增加 Showcase & "Made with Fresh" 徽章</a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Ffresh-1.1" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            