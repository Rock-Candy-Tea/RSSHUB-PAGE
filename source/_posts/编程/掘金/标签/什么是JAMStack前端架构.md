
---
title: '什么是JAMStack前端架构'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71b52feaec1942c2b1aab480b029f20f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 23:39:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71b52feaec1942c2b1aab480b029f20f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>node.js的出现，让JS全栈开发的越来越被公司所接受。目前，最火的大前端概念当属——JAMStack</p>
<h2 data-id="heading-0">定义</h2>
<p>JAM 其实是 Javascript、APIs、Markup 三个术语的首字母组合。通俗来说，JAMStack 就是使用 SSG（Static Site Generators）技术，并且不依赖 Web 服务的前端技术栈。</p>
<blockquote>
<p>"A modern web development architecture based on client-side JavaScript, reusable APIs, and prebuilt Markup"</p>
<p>— Mathias Biilmann (CEO & Co-founder of Netlify).</p>
</blockquote>
<ul>
<li>Javascript：网页渲染工具；JAMStack 并没有限制使用何种框架或是库</li>
<li>APIs：一系列服务端行为的抽象，主要通过 https 与 Javascript 交互。可以是第三方提供的服务，也可以是自己搭建的 function</li>
<li>Markup：网站是托管在 CDN 上的静态资源，Markup 就是生成这些资源的源文件。刚提出 Markup 概念的时候，大家都看好 Markdown 作为 Markup 语言，但是这些年更常用的是 Vue 或是 JSX 文件</li>
</ul>
<h2 data-id="heading-1">架构</h2>
<p>OK，仅仅列出 JAM 定义，其实跟没说一样，我们还是看看他与传统网站架构的比较：</p>
<h3 data-id="heading-2">相比于传统动态网站</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71b52feaec1942c2b1aab480b029f20f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Traditional vs. JAMStack</p>
<p>看架构图就很直观了，传统的 web 架构会有一个很厚重的后端服务器；而 JAMStack 更接近纯静态网站——它甚至通过 SSG 把数据和 html 一起托管到 CDN 上。</p>
<p>为什么会有 JAMStack 这么奇怪的架构呢？我们还是要看应用场景，以及它要解决的问题。对于一些新闻、企业官网、小型电商，这类 CMS（Content Management System）网站，它的内容更新非常缓慢。传统的网站架构无论如何都需要一个实时的在线服务，它在处理这些不怎么变动的内容时，很鸡肋：计算量很小，但是依旧需要大量后端和运维人员维护网站的安全性、稳定性、可伸缩性……</p>
<p>JAMStack 在这些场景下给出了新的解决方案：直接使用 CDN 分发静态页面以及数据；这些 CMS 就成了一个纯静态网站，上述运维难题也自然而然地规避了。据说，特朗普政府将白宫官网的 CMS 从 Drupal （PHP架构）改成了 WordPress （JAMStack 架构），每年能为美国纳税人节省 300 万美元。</p>
<h3 data-id="heading-3">相比于纯静态网站</h3>
<p>既然是 all in CDN，那为什么不用纯静态网站呢？我们再分析一下 JAMStack 与纯静态网站的区别。纯静态网站也是把所有内容分发到 CDN 上，但是它对承载动态内容并不是很友好。举个例子，某公司要想改其静态首页的公告；传统的做法是：运维人员（非开发）手动修改页面，然后更新部署。但是这种解决方案一看就很前现代——编辑页面就很麻烦的，还要自己操作一系列手动部署流程。</p>
<p>JAMStack 就给出了一个更动态的方案：事实上，JAMStack 是有后端的——一个叫 Headless CMS（无头内容管理系统）的后台系统。所谓的“无头”，就是用户端的 UI 展现和后台服务进行解耦，后台系统不负责定制用户端的 UI——也就是去“头”——只负责数据管理。它的大致流程是这样的：</p>
<ol>
<li>运维人员在无头 CMS 系统里输入数据</li>
<li>无头 CMS 系统将数据写入 DB，并触发 SSG 部署流程</li>
<li>SSG 拉取 git 代码和 DB 内的相关数据，并生成静态资源</li>
<li>SSG 再将静态资源部署到 CDN 上，并清理相关缓存</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f049c8b2b69140a79c773ed895e14cef~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Headless CMS</p>
<p>当然，实际项目中大概率还会是操作 admin 页面，然后调取无头 CMS 的 API 的。JAMStack 的整个运行平台是由服务商提供，页面更友好，也更具自动化，从而减少了非技术人员的出错的可能。</p>
<h3 data-id="heading-4">进阶版 JAMStack</h3>
<p>上面提到的 JAMStack 是五六年前提出这个概念时的理论模型，但是我看了一些号称 JAMStack 落地的网站，他们的实现其实并没那么“教条”：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0364906412e147fbac8592ffdc798cc6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Advanced JAMStack</p>
<p>现在的 JAMStack 还是会从客户端发送 API 请求数据的，只是 API 服务器很轻量，通常是 Lambda 这类 serverless 方法。有些 CMS 网站还集成了 auth 服务、搜索服务、支付服务等等，但是通常也是在前端直接集成三方服务的 JS 库。</p>
<h2 data-id="heading-5">优缺点</h2>
<p>OK，我们简单介绍了一下 JAMStack 的架构，稍微复盘一下。JAMStack 的优点有：</p>
<ul>
<li>高性能：几乎是纯静态的网页，网络请求基本流向了 CDN，很少有额外的数据请求</li>
<li>安全性高：不用太担心服务器和数据库的安全问题</li>
<li>成本低：静态资源托管的费用非常廉价</li>
<li>更好的开发体验：前端单独开发、单独部署、单独测试，完全解耦后端架构</li>
</ul>
<p>当然 JAMStack 的缺点也很明显，业务场景非常狭小，只能用于内容更新不大频繁的 CMS 站点。国外也有无头电商（Headless Commerce）的商业实践，但是前景并不明朗。</p>
<h2 data-id="heading-6">工具 & 最佳实践</h2>
<p>JAMStack 的工具链基本和传统 web app 前端相同，区别主要是 SSG 方案的选择：通常来说就是前端三大件（React、Angular、Vue）的 SSR 框架的抉择——Next、Scully、Nuxt 等等。不过我最近发现了一些 JAMStack 的全栈解决方案：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fgithub.com%252Fredwoodjs%252Fredwood" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fredwoodjs%2Fredwood" ref="nofollow noopener noreferrer">redwood.js</a>：react + graphql + prisma 的 serverless 框架</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fgithub.com%252Fblitz-js%252Fblitz" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fblitz-js%2Fblitz" ref="nofollow noopener noreferrer">blitz.js</a>：Typescript + Next + prisma + Auth 的 Node 框架，开箱即用</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fgithub.com%252Fmidwayjs%252Fmidway" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fmidwayjs%2Fmidway" ref="nofollow noopener noreferrer">midway.js</a>：React/Vue + egg/midway + typeorm 的 serverless OOP 框架</li>
</ul>
<p>这些方案本质上就是 Node 全栈的 Monorepo 模版，开箱即用，并且高度适配主流的 serverless 服务。不过，真正用到生成环境，可能还得再等等。</p>
<p>此外，这些年 JAMStack 也总结了一套最佳实践，主要有：</p>
<ul>
<li>原子化部署：每一次部署都应该是一个完整的站点 snapshot，不能有脏页面</li>
<li>Cache：一旦更新了静态资源，就应该立马清楚 CDN 缓存，保证上线的站点资源唯一</li>
<li>Git：构建工作流要强依赖于 Git hook。Markup 的变更要快速响应，也要方便地追踪</li>
<li>DevOps：能围绕不同的开发阶段、不同的运维需求快速地部构建、部署出一套新的环境，方便开发、测试、验收……</li>
</ul>
<h2 data-id="heading-7">小结</h2>
<p>从技术上讲，JAMStack 本质上就是一种增强版的静态网站，不算太大的创新，只能算是 serverless 兴起后的一种衍生品。不过，传统 Web 开发那一套“前端-api-后端-DB”的技术链确实过于繁琐了，JAMStack 是一种改进方向，至少在某些场景下是行之有效的方案。</p></div>  
</div>
            