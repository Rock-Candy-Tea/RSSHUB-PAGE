
---
title: 'Astro 1.0 正式发布，现代化静态站点生成器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0810/173749_DtmA_2720166.png'
author: 开源中国
comments: false
date: Thu, 11 Aug 2022 07:17:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0810/173749_DtmA_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>Astro 是一款现代化的轻量级静态站点生成器，具有出众的开发者体验 (Developer Experience)。据介绍，虽然 Astro 从诞生到今天只有 16 个月，但其仓库的 star 数已超过 13000，并且在全球拥有超过 30000 名用户。目前，Astro 文档已被翻译成 6 种不同的语言——包括<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.astro.build%2Fzh-cn%2Fgetting-started%2F" target="_blank">中文</a>。</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0810/173749_DtmA_2720166.png" referrerpolicy="no-referrer"></p> 
<p>近日，Astro <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fastro.build%2Fblog%2Fastro-1%2F" target="_blank">发布</a>了 1.0 正式版。团队称 1.0 意味着 API 已达到稳定状态，并可用于生产环境。部分新特性：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.astro.build%2Fen%2Fguides%2Fintegrations-guide%2Fimage%2F" target="_blank">图像优化</a>：引入新的<code><Image /></code>和<code><Picture /></code>组件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.astro.build%2Fen%2Fguides%2Fintegrations-guide%2Fmdx%2F" target="_blank">支持 MDX</a>：在 Markdown 中混合编写 UI 组件的标准语法</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.astro.build%2Fen%2Fguides%2Fserver-side-rendering%2F" target="_blank">支持 SSR</a>：SSR 现已达到稳定状态，可用于生产环境</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvitejs.dev%2Fblog%2Fannouncing-vite3.html%23dev-improvements" target="_blank">Vite 3.0</a>：升级 Astro 使用的构建引擎 Vite</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1c2ed843160415d51d37f482243504e832d.png" referrerpolicy="no-referrer"></p> 
<p>Astro 采用了独特的<strong> Island 组件架构</strong>，团队称这是一种用于构建更快网站的新型 Web 架构。与单页应用程序不同，Astro 的组件不会被捆绑到一个 JavaScript 包中。相反，每个组件都被视为一个独立的小型应用程序，与所有其他组件隔离存在。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-7e6c695058258ff5ebf6d3db1aae405ce53.png" referrerpolicy="no-referrer"></p> 
<p>Astro 其他特性：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>自带组件框架：Astro 为 React、Vue、Svelte 和 Tailwind CSS 等前端工具提供一级支持。通过<span> </span><code>astro add</code><span> </span>命令即可添加使用<br> <img src="https://static.oschina.net/uploads/space/2022/0810/152615_hTKT_2720166.png" referrerpolicy="no-referrer"></li> 
 <li>支持静态页面生成 (SSG) 和服务器端渲染 (SSR)，可以按需渲染内容</li> 
 <li>开发者体验出众：Astro 支持所有喜爱的开发者工具和功能，如 TypeScript、NPM 包、Scoped CSS、CSS Modules、Sass、Tailwind、Markdown、MDX</li> 
 <li>按需组件：Astro 支持通过水化组件按需加载 JavaScript。因此，如果该特定组件不可见，它不会加载相关的 JavaScript</li> 
 <li>100% 静态 HTML，无 JavaScript 运行时环境：当构建 Astro 时，它将删除所有 JavaScript，并将整个页面渲染为静态 HTML 页面</li> 
 <li>SEO 友好：使用 Astro，可以启用自动网站地图、RSS 订阅、分页和收藏</li> 
 <li>基于文件的路由：就像 Next.js 一样，Astro 有一个基于文件的路由机制，所有在 /pages 中的东西 Astro 都会将目录转化为路由</li> 
</ul> 
<p>借发布 1.0 的机会，开发团队还对官网 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fastro.build%2F" target="_blank">astro.build</a> 进行了重新设计：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-d030192cee1af3abbc20dcd1d35a27c67f0.png" referrerpolicy="no-referrer"></p> 
<p>最后团队表示，Astro 从首次推出到现在发布 1.0 正式版，已经发生了许多变化。它不仅仅只是静态站点生成器，开发者可以在任何流行的托管平台上将 Astro 构建为动态的、支持 SSR 的服务器。</p>
                                        </div>
                                      
</div>
            