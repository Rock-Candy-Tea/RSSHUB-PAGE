
---
title: 'Blitz.js 一体化开发 (1.2)：与 Next.js 进行权衡'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9797'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 02:20:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=9797'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Next.js 是什么？</h2>
<p>Blitz 是基于 Next.js 的，因此几乎支持 Next.js 的所有功能。有关差异的更多信息，请参见此处：<a href="https://blitzjs.com/docs/why-blitz" target="_blank" rel="nofollow noopener noreferrer">为什么是 Blitz 而非 Next.js</a>。</p>
<p><a href="https://nextjs.org/" target="_blank" rel="nofollow noopener noreferrer"><strong>Next.js</strong></a> 是一个流行的 React 框架，其中有很多内置功能，例如：</p>
<ul>
<li>预渲染，每页支持静态生成 (SSG) 和服务端渲染 (SSR)。</li>
<li>自动代码拆分，可更快地加载页面。</li>
<li>客户端路由具有优化的预加载功能。</li>
<li>开发环境支持热更新。</li>
<li>完全可拓展。</li>
</ul>
<h2 data-id="heading-1">为什么是 Blitz 而非 Next.js？</h2>
<h3 data-id="heading-2">1. 全栈而非前端</h3>
<p>Next.js 主要是一个前端框架。它是为构建连接到其它 API 的前端而设计的。Nex.js 并不是一个真正的、开箱即用的全栈框架。</p>
<p>Blitz 中添加了所有缺少的功能，这些功能使 Next 变成了真正的全栈框架。这些关键功能包括直接访问数据库，中间件和身份验证。</p>
<h3 data-id="heading-3">2. 数据层</h3>
<p>Blitz 的数据层是一种新颖的技术，可以再保留客户端渲染的同时消除 API。在 Blitz 应用中，你可以将服务器代码直接导入前端，因此无需构建 API 并从前端进行数据提取工作。在构建时，Blitz 自动插入一个 API 调用，该 API 调用在服务器上运行服务端代码。本质上，Blitz 将你的 API 抽象为一个编译步骤。</p>
<p>这是 React 应用程序开发的游戏规则改变者，因为它消除了传统 React 应用程序体系结构的整个部分。这意味着更容易学习、更快开发，并且构建事务更有趣！</p>
<p>也就是说，你可以像往常一样继续通过 REST 或 GraphQL 进行数据获取。Blitz 对此没有任何限制。</p>
<h3 data-id="heading-4">3. 内置身份验证</h3>
<p>Blitz 具有可与任何身份验证商一起使用的内置会话管理服务，包括自托管的电子邮件/密码和第三方服务。身份验证是一项复杂且难以正确实施的事情。将其内置到 Blitz 中可以为你节省大量时间和潜在的安全漏洞。</p>
<p>在 Next.js 中使用 auth 构建令人敬畏的 UX 会非常地棘手和乏味，但是 Blitz 免费为你提供了一流的 DX。</p>
<h3 data-id="heading-5">4. 约定</h3>
<p>除了基于文件系统的路由外，Next.js 没有任何约定。此时，每个开发人员都可以为每个项目重新发明轮子。</p>
<p>Blitz 带来了许多约定，例如如何组织文件以及如何构造路由。这意味着你不会浪费任何时间为每个项目弄清楚这一点。这也极大地造福了社区。通用的项目结构和架构模式可让你从 Blitz 应用程序迁移到 Blitz 应用程序，并立即感到宾至如归。</p>
<h3 data-id="heading-6">5. 代码脚手架</h3>
<p>有两种主要方法可以减少你必须手工编写的代码量：</p>
<ol>
<li>代码生成</li>
<li>代码脚手架</li>
</ol>
<p><strong>Code 生成</strong> 意味着让库来为你生成代码。例如，可以通过 GraphQL 查询生成代码的 graphql-code-generator 和可以从你的数据库架构中生成整个 GraphQL API 的 Hasura。通常，codegen 无法完全自定义生成的代码。你需要通过库来支持。同时你也会常遇到 codegen 无法解决的极端情况。而且你无法修复它，因为你不拥有该代码。</p>
<p><strong>Code 脚手架</strong> 意味着初始代码将注入到你的项目之中。从那时起，你对所有代码拥有着完全的所有权，并可以根据需要进行自定义。代码脚手架的缺点是你不会像从第三方库生成的代码那也获得自动更新。但巨大的好处在于其可以确保你永远不会受到别人无法改变的设计选择的限制。</p>
<p>Blitz 是代码脚手架的忠实拥护者。我们有大量的 <a href="https://www.yuque.com/ningo/blitzjs/cli-generate" target="_blank" rel="nofollow noopener noreferrer"><code>blitz generate</code></a> 命令，可将代码脚手架插入你的项目中。我们的代码脚手架还处于初期阶段——我们仍然需要添加许多强大的功能，包括添加自己的自定义脚手架模板的功能。</p>
<h3 data-id="heading-7">6. 配方</h3>
<p>Recipes 是用于将代码从 npm 或 git 存储库上的 MDX 配方放入你的项目中的单行命令。</p>
<p>例如：</p>
<ul>
<li><code>blitz install tailwind</code>——一行命令安装和配置 tailwind</li>
<li><code>blitz install chakra-ui</code>——一行命令安装和配置 chakra</li>
<li><code>blitz install material-ui</code>——一行命令安装和配置 material-ui</li>
</ul>
<p>Recipes 超级强大，它们几乎可以更改项目中的任何内容，包括添加依赖项、更改代码、添加代码等。它们是通过 MDX 编写的，可以像 React 一样组成。</p>
<h3 data-id="heading-8">7. 全新的开发环境</h3>
<p>一个新的 Next.js 应用是完全恐怖的。因此，每次你启动 Next.js 项目，你必须花费数小时来建立 eslint、petterier、husky git hooks 等的所有基础知识。</p>
<p>一个新的 Blitz 应用可以为你节省大量时间，因为所有这些都是为你预先配置的！当然，你以后始终可以对其进行自定义，但是拥有一个可行的起点真的很棒。</p>
<h3 data-id="heading-9">8. 放宽限制</h3>
<p>Next.js 要求你所有的 React 页面都放在一个 <code>pages/</code> 文件夹中。Blitz 通过允许你拥有无限数量的 <code>pages/</code>文件夹来放宽此限制。</p>
<p>对于大型项目，这是一个巨大的好处，因为你可以按任意方式分离和组织页面。</p>
<p>例如：</p>
<ul>
<li><code>app/pages/</code> 可以包含“首页”和“关于”之类的页面</li>
<li><code>app/products/pages/</code> 可以包含于产品相关的所有页面</li>
<li><code>app/admin/pages/</code> 可以包含与后端 admin 部分相关的所有页面</li>
</ul>
<h2 data-id="heading-10">权衡</h2>
<p>你应该会知道，一切都需要被权衡。那么 Blitz 需要权衡的是什么？</p>
<h3 data-id="heading-11">框架限制</h3>
<p>每个框架都有一定程度的限制。如果你使用 React 构建应用，那么就很容易被 React 限制。</p>
<p>Blitz 的限制级别比 Next.js 高一个级别。Blitz 代码库与 Next.js 代码库没有 <em>太多</em> 不同。但这已经够不同了，以至于“弹出”到普通的 Next.js 并不简单。例如，你可能将使用 Blitz 所特有的 Blitz 身份验证。但切换到 Next AUth 将为你提供与 Next.js 相当的体验。</p>
<p>Blitz 零 API 数据层是 Blitz 独有的。因此，如果此时切换到 Next.js，则必须管理自己的 API 代码（而如果从 Next.js 开始，则必须这么做，因此不会丢失任何内容）。但是，你所有的后端 query 和 mutation 逻辑都可以直接移植。</p>
<h3 data-id="heading-12">升级 Next.js</h3>
<p>如果你想站在 Next.js 版本的最前沿，请知道 Blitz 会稍微落后但不会太远。通常，我们会在新的 Next.js 版本发布后不到一周的时间内更新 Blitz。</p>
<p>但如果你使用 yarn，则可以先使用 package.json 中的 <code>resolutions</code> 字段来升级 next.js。</p>
<h3 data-id="heading-13">多客户端 API</h3>
<p>有人会说，“迟早你会需要 GraphQL，所以你应该从它开始”。虽然我们认为绝大多数应用程序的增长不会足够大以至于不能保证 GraphQL，但是提供多个客户端的 API 的问题是一个很好的要点。</p>
<p>我们完全承认，许多 Web 应用程序迟早都需要移动应用程序。我们希望这种集成尽可能的简单！</p>
<p>也就是说，你可以为其他客户端将 GraphQL 服务器添加到 Blitz 应用中，这可能是一个很好的选择，有些人已经开始这样做了。</p>
<p><strong>目前，截至 2021 年 2 月 17 日：</strong></p>
<ul>
<li>你可以直接访问自动生成的 API 接口，并且可以在任何移动应用中使用它们（我们目前有几个人在建设中）；</li>
<li>你可以通过 <a href="https://www.yuque.com/ningo/blitzjs/cli-routes" target="_blank" rel="nofollow noopener noreferrer"><code>blitz routes</code></a> 来查看应用程序中生成的 API；</li>
<li>你可以在此处查看 API 接口的 RPC 规范：<a href="https://www.yuque.com/ningo/blitzjs/rpc-specification" target="_blank" rel="nofollow noopener noreferrer">RPC Specification</a>。</li>
</ul>
<p><strong>我们计划今后要做的事：</strong></p>
<ol>
<li>第一步，添加文档和工具，以使手动使用生成的 API 接口变得更加容易，访问：<a href="https://github.com/blitz-js/blitz/discussions/1907" target="_blank" rel="nofollow noopener noreferrer">github.com/blitz-js/bl…</a> 和 <a href="https://github.com/blitz-js/blitz/issues/745" target="_blank" rel="nofollow noopener noreferrer">github.com/blitz-js/bl…</a>；</li>
<li>接下来，添加生成一个 JS/TS 客户端库的功能，作为使用从应用生成接口的好方</li>
</ol>
<p>法；</p>
<ol>
<li>还有，添加某种一流的 react-native 支持，你可以再其中将 Blitz queries/mutations 直接导入到你的 react-native 代码中，并使它神奇地工作，就像今天在你的 Web 应用程序中一样。在 1.0 版本后，这将是 Brandon 在这一年中的主要工作重点。</li>
</ol>
<h3 data-id="heading-14">高阶后端架构</h3>
<p>目前，Blitz 在后端架构上的功能还很少，尤其是与 Nest.js 或 AdonisJS 之类的
东西相比。但是，这并不意味着你不能在 Blitz 中使用这些模式，但你需要自己进
行设置。实际上，如果需要，你可以在 Blitz 应用中直接使用 Nest.js。</p>
<p>但是我们非常有兴趣通过默认支持或简单的植入来加入更先进的后端体系架构到
Blitz 中。我们有一个<a href="https://github.com/blitz-js/blitz/discussions/1841" target="_blank" rel="nofollow noopener noreferrer">正在进行的讨论</a>，如果你有想法，我们希望你能加入。</p>
<h3 data-id="heading-15">当不部署到 Serverless 时的单线程</h3>
<p>具体来说，这是 Next.js 的折衷方案。Next.js 是单线程的，这意味着如果你在进行繁重的后端处理时，你可能会发现所有的 Web 请求都开始受到影响。解决方案是让后端处理来生成其他进程。</p>
<p>运行多个后台进程并不是很困难，但是我们希望添加文档和 API，以使其尽可能简单。</p>
<h2 data-id="heading-16">译者结语</h2>
<p>本文内容属于 <a href="https://blitzjs.com/docs" target="_blank" rel="nofollow noopener noreferrer">Blitz.js 官方文档</a> - 简介章节的后半部分。总共十四个章节（简介、社区、基础、页面、路由、权限、数据库、Queries 和 Mutations、后端架构、部署、配方、配置、CLI 和模板）。未来不定期翻译其余章节，也可能会原创一些文章。</p>
<p>《<a href="https://github.com/hylerrix/blitzjs-tutorial" target="_blank" rel="nofollow noopener noreferrer">React 全栈开发手册</a>》系列专注探索 Blitz.js + React 全栈应用开发，原文翻译内容会同步更新到 <a href="https://github.com/blitz-js/zh-hans.blitzjs.com" target="_blank" rel="nofollow noopener noreferrer">Blitz.js 中文仓库</a> 上。欢迎 Star、Watch 或关注公众号 (@ningowood) 来及时接收消息。</p>
<blockquote>
<p>2021 © <a href="https://github.com/hylerrix/blitzjs-tutorial" target="_blank" rel="nofollow noopener noreferrer">github.com/hylerrix/bl…</a></p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            