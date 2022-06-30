
---
title: 'Fresh 1.0 稳定版发布，Deno 全栈 Web 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0630/065626_wj73_2720166.png'
author: 开源中国
comments: false
date: Thu, 30 Jun 2022 07:09:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0630/065626_wj73_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px; margin-right:0px; text-align:start">Fresh 是 Deno 的全新全栈 Web 框架。默认情况下，使用 Fresh 构建的网页不会向客户端发送 JavaScript。该框架没有构建步骤，可以将部署时间缩短一个数量级。近日，Fresh <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Ffresh-is-stable" target="_blank">发布</a>了第一个稳定版本。</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0630/065626_wj73_2720166.png" referrerpolicy="no-referrer"></p> 
<p>Fresh 使用了一种不同的模型：默认情况下，开发者会将 0 KB 的 JS 发送给客户端。因为大多数渲染在服务器上完成，客户端只负责重新渲染交互性的小模块。这是一个开发者明确选择客户端渲染特定组件的模型。早在 2020 年，Jason Miller 在他的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjasonformat.com%2Fislands-architecture" target="_blank">Islands Architecture 博客文章</a>中就描述了这个模型。</p> 
<p><span style="background-color:#ffffff; color:#333333">Fresh 核心是</span><strong style="color:#333333">路由框架和模板引擎的组合</strong><span style="background-color:#ffffff; color:#333333">，支持在服务器上按需渲染页面。除了在服务器中提供的即时 (JIT) 渲染之外，Fresh 还提供了一个接口，用于在客户端上无缝渲染某些组件，以实现最大的交互性。该框架使用 Preact 和 JSX</span>（或 TSX）在服务器和客户端上进行渲染和模板化。客户端渲染在每个组件级别上是完全可选的，因此许多应用程序根本不会向客户端发送任何 JavaScript。</p> 
<p><span style="background-color:#ffffff; color:#333333">由于 Fresh 没有构建步骤，因此开发者编写的代码直接就是在服务器和客户端上运行的代码。将 TypeScript 或 JSX 转换为纯 JavaScript 的任何必要转换都是在需要时即时完成的。这允许通过即时部署实现非常快速的迭代循环。</span></p> 
<p>Fresh 不仅仅是一个前端框架，而是一个用于编写网站的完全集成系统。开发者可以任意处理任何类型的请求、返回自定义响应、发出数据库请求等等。此路由返回纯文本 HTTP 响应而不是 HTML 页面，例如：</p> 
<pre><code class="language-javascript">// routes/api/joke.ts

const JOKES = [/** jokes here */];

export const handler = (_req: Request): Response => &#123;
  const randomIndex = Math.floor(Math.random() * JOKES.length);
  const body = JOKES[randomIndex];
  return new Response(body);
&#125;;</code></pre> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>这也可以用于为路由进行异步数据获取。下面是从磁盘上的文件加载博客文章的路由：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<pre><code class="language-javascript">// routes/blog/[id].tsx

import &#123; HandlerContext, PageProps &#125; from "$fresh/server.ts";

export const handler = async (_req: Request, ctx: HandlerContext): Response => &#123;
  const body = await Deno.readTextFile(`./posts/$&#123;ctx.params.id&#125;.md`);
  return ctx.render(&#123; body &#125;);
&#125;;

export default function BlogPostPage(props: PageProps) &#123;
  const &#123; body &#125; = props.data;
  // ...
&#125;</code></pre> 
<div style="text-align:start"> 
 <p>因为 Fresh 非常依赖动态服务器端渲染，所以速度必须快。Fresh 非常适合在 Deno Deploy、Netlify Edge Functions 或 Supabase Edge Functions 等边缘 runtime 场景运行。由于渲染过程在物理上非常靠近用户，从而可以最大限度地减少网络延迟。</p> 
 <p>Fresh 亮点特性</p> 
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
<p>Fresh 1.0 是一个稳定版本，支持在生产环境使用。<span style="background-color:#ffffff; color:#333333">通过 Deno，Fresh 项目可以手动部署到任何平台，但部署到像 Deno Deploy 这样的边缘运行时可获得最佳体验。</span></p>
                                        </div>
                                      
</div>
            