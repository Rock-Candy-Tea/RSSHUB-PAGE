
---
title: 'Docusaurus 2.0 正式发布，Facebook 开源的静态网站生成器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-effd4994a788e4f9bab74f97689180f14a5.png'
author: 开源中国
comments: false
date: Tue, 02 Aug 2022 11:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-effd4994a788e4f9bab74f97689180f14a5.png'
---

<div>   
<div class="content">
                                                                                            <p>Docusaurus 2.0 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocusaurus.io%2Fblog%2F2022%2F08%2F01%2Fannouncing-docusaurus-2.0" target="_blank">发布</a>。</p> 
<blockquote> 
 <p>Docusaurus 是 Facebook（现更名为 Meta）开源的静态网站生成器。它将你的网站构建成一个单页面应用程序 (single-page application)，具有快速的客户端导航功能并充分利用了 React 的强大能力，为网站赋予更好地交互性。虽然 Docusaurus 是为文档功能而生的，但是也可以用来构建任何类型的网站（个人站点、产品介绍、博客、营销页面等）。</p> 
</blockquote> 
<p>发布公告称，新一代的 Docusaurus 历经 4 年的开发，期间发布了 75 个 alpha 和 22 个 beta 版本。未来将会遵循语义化版本管理 (Semantic Versioning)，并更快地发布重大更新版本。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-effd4994a788e4f9bab74f97689180f14a5.png" referrerpolicy="no-referrer"></p> 
<p><strong>Docusaurus 2.0 主要变化</strong></p> 
<ul> 
 <li>React 既支持服务器端也支持客户端，可实现现代单页应用程序导航</li> 
 <li>提供深色主题、更好的 UI 和 UX</li> 
 <li>支持插件，插件使社区能够以第三方软件包的形式提供有用的功能</li> 
 <li>通过<code>themeConfig</code><span style="background-color:#ffffff; color:#262626"><span> 配置</span>项可灵活</span>更换主题</li> 
 <li>文档版本控制基于快照，并提供灵活的插件选项，以适应开发者工作流程</li> 
 <li>TypeScript 支持配置文件、插件、自定义页面和主题作者</li> 
 <li>Markdown 支持数学方程式、实时代码块</li> 
 <li>支持 PWA</li> 
</ul> 
<p>在 Docusaurus 2 中，现在支持通过 MDX 在 Markdown 中插入 React 组件，轻松构建交互式文档。</p> 
<p>示例：</p> 
<p><span style="background-color:#ffffff; color:#262626">docs/my-document.mdx</span></p> 
<pre><code class="language-markdown">### Give it a try: press that button!

import ColorModeToggle from '@theme/ColorModeToggle';

<ColorModeToggle/></code></pre> 
<p>虽然 Docusaurus 2 现在才正式发布，但它早已处于稳定状态，并被广泛使用，因此 Docusaurus 2 在 npm 的下载量很快就超过了 Docusaurus 1：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-aee1e73f4e72f11a3e2919238e8c325f2a6.png" referrerpolicy="no-referrer"></p> 
<p><strong>使用案例</strong></p> 
<ul> 
 <li>redocusaurus：与 OpenAPI 和 Redoc 无缝集成</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-8a41332cb8db137d198b1d2b95c3f729a27.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a227660dea1409b4006ec6b1bd7b1596162.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            