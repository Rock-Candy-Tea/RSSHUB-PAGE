
---
title: 'Blitz.js 入门教程 (1.1)：基于 Next.js 的下一代 React 全栈框架'
categories: 
 - 编程
 - 掘金
 -  - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64f5d72ede37401bb4ebdac30a31ac12~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 22 Mar 2021 23:01:54 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64f5d72ede37401bb4ebdac30a31ac12~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">译者序</h2>
<p>苦 JS 生态久已。在 2020 年后，一直徘徊于该为自己构建怎样的技术栈，迟迟没有太多落地成果——库太多了，一个小场景就能有很多个解决方案；方向也太多了，哪怕大前端三个字，现今都能拆分为很多的细分领域。直到遇到了 Rome，看到社区已经开始尝试整合重构 Node 生态的前端工具链；又遇到了 Deno，直接摆脱 Node 的历史遗留问题来建设更贴近现代标准的 JavaScript/TypeScript 运行时；现在又遇到了 Blitz.js，一站式 React 全栈框架，在 Next.js 之上赋能更多的后端场景...于是自己的很多方向性问题都豁然开朗：通过建立不同的 Repo 来专攻不同的方向，且每个 Repo 都能有代表性的同时，覆盖更多的场景。于是——</p>
<ul>
<li><a href="https://github.com/hylerrix/deno-tutorial" target="_blank" rel="nofollow noopener noreferrer">Deno 钻研之术</a>：看未来，学标准。Node 也不落下。</li>
<li><a href="https://github.com/hylerrix/deno-algorithm" target="_blank" rel="nofollow noopener noreferrer">Deno 算法之旅</a>：刷算法，玩测试。</li>
<li><a href="https://github.com/hylerrix/es-interview" target="_blank" rel="nofollow noopener noreferrer">ECMAScript 面试宝典</a>：备面试，打基础；</li>
<li><a href="https://github.com/hylerrix/blitzjs-tutorial" target="_blank" rel="nofollow noopener noreferrer">Blitz.js + React 全栈开发手册</a>：搞工程，尝全栈。深入 React，实战 Next.js，掌握后端开发。</li>
<li>以及还有一切弃坑的 repo......</li>
</ul>
<p>当然，Blitz.js 还有很多吸引人的特性：</p>
<ul>
<li><strong>一体式全栈架构</strong>：在一个 Monorepo 里从数据库到用户端全搞定，也没用重复性代码。试想前后端分离的架构下，如果你喜欢 TypeScript 的话，很可能得写两套相同 TS...且这种一体式架构很容易让自己的项目灵感从头到尾地快速落地。</li>
<li><strong>API 不再必须</strong>：REST 和 GraphQL？或许都不需要，交给 Blitz.js 来在编译时构建。当需要提供 API 给更多端使用时，再结合相关库来生成 API。</li>
<li><strong>更轻松的开箱体验</strong>：脚手架初始化后直接提供登录注册甚至重置密码功能，直接支持最基本的后端环境，开箱即用的体验不能再好，同时甚至能通过强大的 blitz generate CLI 快速植入生态圈中的主流库到项目中。</li>
<li><strong>并不会“学不动了”</strong>：基于 Next.js，前端 React，后端 Prisma 等库，Blitz.js 构建于各种已经主流化的生态之上。</li>
<li><strong>拥抱未来</strong>：Blitz.js 预计将于下个月（2021 年 4 月）发布 v1.0 版本。</li>
</ul>
<p>本文属于《<a href="https://github.com/hylerrix/blitzjs-tutorial" target="_blank" rel="nofollow noopener noreferrer">Blitz.js + React 全栈开发手册</a>》系列，原文翻译内容会同步更新到 <a href="https://github.com/blitz-js/zh-hans.blitzjs.com" target="_blank" rel="nofollow noopener noreferrer">Blitz.js 中文仓库</a> 上。欢迎 Star 和 Watch：<a href="https://github.com/hylerrix/blitzjs-tutorial" target="_blank" rel="nofollow noopener noreferrer">github.com/hylerrix/bl…</a>。</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64f5d72ede37401bb4ebdac30a31ac12~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">快速入手</h2>
<h3 data-id="heading-2">配置你的环境</h3>
<p>你需要使用 Node 12 或者更新的版本。</p>
<h3 data-id="heading-3">安装 Blitz</h3>
<p>执行 <code>npm install -g blitz</code></p>
<h3 data-id="heading-4">创建一个新项目</h3>
<ol>
<li><code>blitz new myAppName</code></li>
<li><code>cd myAppName</code></li>
<li><code>blitz dev</code></li>
<li>访问你的新项目 <a href="http://localhost:3000/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000</a></li>
</ol>
<h3 data-id="heading-5">欢迎来到 Blitz 社区 👋</h3>
<p>Blitz 社区是个温暖、安全、多样化、包容也不失有趣的社区！ LGBTQ+、女生和少数派欢迎你们的到来。</p>
<p><a href="https://discord.blitzjs.com/" target="_blank" rel="nofollow noopener noreferrer">加入我们的 Discord 社区</a>，我们会在这里帮助每个人搭建 Blitz 应用。这里也是我们协作共建 Blitz 本身的重要场地。</p>
<p>对于提问以及会花费较长时间的讨论，<a href="https://github.com/blitz-js/blitz/discussions" target="_blank" rel="nofollow noopener noreferrer">可以发帖到我们的论坛中</a>。</p>
<p>有关完整的介绍，请阅读 社区是如何运作的。文中包括了如何获得帮助、如何报告错误以及如何提出新功能建议等的详细指导。</p>
<p><strong>欢迎你的帮助来使 Blitz 变得更好！ 🤝</strong></p>
<p>我们有一个很棒的社区正在共同努力让 Blitz 成为世界上一流的框架。</p>
<p>你该如何提供帮助：</p>
<ol>
<li>通过 <a href="https://github.com/blitz-js/blitz/issues/new/choose" target="_blank" rel="nofollow noopener noreferrer">在 GitHub 上提交 issue</a> 来反馈 Bug。</li>
<li>贡献代码： 阅读贡献指南，以了解如何开始。</li>
<li><a href="https://github.com/blitz-js/blitz#sponsors-and-donations" target="_blank" rel="nofollow noopener noreferrer">赞助 & 捐赠</a>，可以从 $5/月 开始。</li>
<li>以及你觉得可以的其它任何方式！我们非常感谢你的任何贡献（如文档、视频、博客等）。如果你遇到任何阻碍，欢迎来 Discord 上与我们交流！:)</li>
</ol>
<h3 data-id="heading-6">下一步</h3>
<h4 data-id="heading-7">教程</h4>
<p>教程篇 是有关 Blitz 所有基本内容的完整练习，其中包括将模型添加到数据库以及从前端读取和更新数据。</p>
<h4 data-id="heading-8">学习</h4>
<p>这里有你想要熟悉的 Blitz 的关键概念：</p>
<ul>
<li>如何 新建页面</li>
<li>如何 使用文件路由系统</li>
<li>如何设置并 使用数据库</li>
<li>如何使用 Blitz Queries 和 Mutations 来读写你的数据库。</li>
<li>如何通过 <code>blitz generate</code> 命令来用脚手架生成数据库模型</li>
</ul>
<p>的所有代码。</p>
<h2 data-id="heading-9">入门教程</h2>
<p>在本教程中，我们将会指导你创建一个简易的投票系统。</p>
<p>我们将假设你已经 安装了 Blitz。你可以通过在终端运行以下命令来确定 Blitz 是否已经安装或检查安装的版本号：</p>
<pre><code class="hljs language-bash copyable" lang="bash">blitz -v
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 Blitz 已经安装成功，你应该能看到安装的版本号。否则你会收到一条像这样的错误提示：“command not found: blitz”。</p>
<h3 data-id="heading-10">创建一个新应用</h3>
<p>在命令行中，<code>cd</code> 进入你想要创建应用的根目录文件夹后，执行以下命令：</p>
<pre><code class="hljs language-sh copyable" lang="sh">blitz new my-blitz-app
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Blitz 会在你当前的文件夹中创建一个 <code>my-blitz-app</code> 文件夹。你接着会收到一个选择表单库的提示。本教程中将选择其中推荐的 <code>React Final Form</code> 库。</p>
<p>让我们看看 <code>blitz new</code> 命令创建了什么：</p>
<pre><code class="hljs language-markdown copyable" lang="markdown">my-blitz-app
├── app/
│   ├── api/
│   ├── auth/
│   │   ├── components/
│   │   │   ├── LoginForm.tsx
│   │   │   └── SignupForm.tsx
│   │   ├── mutations/
│   │   │   ├── changePassword.ts
│   │   │   ├── forgotPassword.test.ts
│   │   │   ├── forgotPassword.ts
│   │   │   ├── login.ts
│   │   │   ├── logout.ts
│   │   │   ├── resetPassword.test.ts
│   │   │   ├── resetPassword.ts
│   │   │   └── signup.ts
│   │   ├── pages/
│   │   │   ├── forgot-password.tsx
│   │   │   ├── login.tsx
│   │   │   ├── reset-password.tsx
│   │   │   └── signup.tsx
│   │   └── validations.ts
│   ├── core/
│   │   ├── components/
│   │   │   ├── Form.tsx
│   │   │   └── LabeledTextField.tsx
│   │   ├── hooks/
│   │   │   └── useCurrentUser.ts
│   │   └── layouts/
│   │       └── Layout.tsx
│   ├── pages/
│   │   ├── 404.tsx
│   │   ├── <span class="hljs-emphasis">_app.tsx
│   │   ├── _</span>document.tsx
│   │   ├── index.test.tsx
│   │   └── index.tsx
│   └── users/
│       └── queries/
│           └── getCurrentUser.ts
├── db/
│   ├── index.ts
│   ├── schema.prisma
│   └── seeds.ts
├── integrations/
├── mailers/
│   └── forgotPasswordMailer.ts
├── public/
│   ├── favicon.ico<span class="hljs-emphasis">*
│   └── logo.png
├── test/
│   ├── setup.ts
│   └── utils.tsx
├── README.md
├── babel.config.js
├── blitz.config.js
├── jest.config.js
├── package.json
├── tsconfig.json
├── types.d.ts
├── types.ts
└── yarn.lock
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>上述文件有：</p>
<ul>
<li><code>app/</code> 文件夹是项目中绝大多数功能的容器。你可以在这里放置任何页面或 API 路由。</li>
<li><code>app/pages/</code> 文件夹是主要的页面文件夹。如果你使用过 Next.js 你将会立即注意到两者的不同。在 Blitz 中，你可以有许多 <code>pages</code> 文件夹，它们将在构建时合并在一起。</li>
<li><code>app/core/</code> 文件夹是放置整个应用中使用到的通用组件、Hooks 等的主要位置。</li>
<li><code>db/</code> 是数据库配置所在的位置。如果你正在编写模型或检查迁移情况，可以来这里。</li>
<li><code>public/</code> 文件夹可以让你放置任何静态资源。如果你有要在应用中使用的图像、文件或视频等，都可以放置在其中。</li>
<li><code>.babelrc.js</code>、<code>.env</code> 等（“dotfiles 文件”）是各种 JavaScript 工具需要用到的配置文件。</li>
<li><code>blitz.config.js</code> 用于 Blitz 的高级自定义配置，与 <code>next.config.js</code> 相同</li>
<li><code>tsconfig.json</code> 是我们推荐的 TypeScript 设置。</li>
</ul>
<h3 data-id="heading-11">开发环境服务器</h3>
<p>现在，如果你还没有在 <code>my-blitz-app</code> 文件夹下，确保切换到其中，并运行以下命令：</p>
<pre><code class="hljs language-sh copyable" lang="sh">blitz dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你将会在命令行中看到如下输出：</p>
<pre><code class="hljs language-sh copyable" lang="sh">✔ Compiled
Loaded env from /private/tmp/my-blitz-app/.env
warn  - You have enabled experimental feature(s).
warn  - Experimental features are not covered by semver, and may cause unexpected or broken application behavior. Use them at your own risk.

ready - started server on 0.0.0.0:3000, url: http://localhost:3000
info  - Using external babel configuration from /my-blitz-app/babel.config.js
event - compiled successfully
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在服务器已成功运行，浏览器中访问 <a href="http://localhost:3000/" target="_blank" rel="nofollow noopener noreferrer">localhost:3000</a>。你将会看到带有 Blitz logo 的欢迎页面。成功了！</p>
<h3 data-id="heading-12">以用户身份注册</h3>
<p>Bliz 应用让用户登录和注册开箱即用！现在让我们来尝试一下。点击 <strong>注册</strong> 按钮，输入任何电子邮件和密码，然后单击 <strong>创建账户</strong> 后，你将被重定向到用户主页，并在其中可以看到你的用户 <code>id</code> 和 <code>role</code>。</p>
<p>如果需要，你也可以尝试注销并重新登录。或在登录页面上单击 <strong>忘记密码</strong>，以尝试重置密码流程。</p>
<h3 data-id="heading-13">编写你的第一个页面</h3>
<p>接下来让我们创建你的第一个页面。</p>
<p>打开 <code>app/pages/index.tsx</code> 文件然后替换掉 <code>Home</code> 组件的所有内容为这段代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">//...</span>

<span class="hljs-keyword">const</span> Home: BlitzPage = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello, world!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">"Loading..."</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">UserInfo</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">Suspense</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;

<span class="hljs-comment">//...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>保存文件后你将会看到浏览器页面进行了更新。你可以如你所愿地添加需要的各种自
定义项，。准备就绪后，请转到下一节。</p>
<h3 data-id="heading-14">数据库配置</h3>
<p>好消息是，已经为你建立好了 SQLite 数据库！你可以在终端中运行 <code>blitz prisma studio</code> 来打开一个可以查看数据库数据的 Web 界面。</p>
<p>请注意，在开始第一个实际项目时，你可能希望使用可扩展性更高的数据库（如 PostgreSQL），以避免在将来切换数据库时产生的麻烦。有关更多信息，请参见 数据库概述 篇。目前，我们将继续使用默认的 SQLite 数据库。</p>
<h3 data-id="heading-15">模型的脚手架代码</h3>
<p>Blitz 提供了一个方便的 CLI 命令 <code>generate</code> 来构建样板代码。我们将使用 <code>generate</code> 来创建两个模型：<code>Question</code>（问题） 和 <code>Choice</code>（选择）。<code>Question</code> 包含问题内容和选择列表。<code>Choice</code> 包含选择内容、投票计数以及相关的问题。Blitz 将为这两个模型自动生成一个 id、一个创建时间戳以及一个最新更新的时间戳。</p>
<h4 data-id="heading-16">首先，我们将生成与 <code>Question</code> 模型有关的所有信息：</h4>
<pre><code class="hljs language-bash copyable" lang="bash">blitz generate all question text:string
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当出现提示框时，按 <strong>Enter</strong> 以运行 <code>prisma migrate</code>，这将使用新的模型来更新你的数据库架构。此时会要求一个名称，可以输入“add question”之类的值。</p>
<pre><code class="hljs language-bash copyable" lang="bash">CREATE    app/pages/questions/[questionId].tsx
CREATE    app/pages/questions/[questionId]/edit.tsx
CREATE    app/pages/questions/index.tsx
CREATE    app/pages/questions/new.tsx
CREATE    app/questions/components/QuestionForm.tsx
CREATE    app/questions/queries/getQuestion.ts
CREATE    app/questions/queries/getQuestions.ts
CREATE    app/questions/mutations/createQuestion.ts
CREATE    app/questions/mutations/deleteQuestion.ts
CREATE    app/questions/mutations/updateQuestion.ts

✔ Model <span class="hljs-keyword">for</span> <span class="hljs-string">'question'</span> created <span class="hljs-keyword">in</span> schema.prisma:

> model Question &#123;
>   id        Int      @default(autoincrement()) @id
>   createdAt DateTime @default(now())
>   updatedAt DateTime @updatedAt
>   text      String
> &#125;

? Run <span class="hljs-string">'prisma migrate dev'</span> to update your database? (Y/n) › <span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">Environment variables loaded from .env
Prisma schema loaded from db/schema.prisma
Datasource <span class="hljs-string">"db"</span>: SQLite database <span class="hljs-string">"db.sqlite"</span> at <span class="hljs-string">"file:./db.sqlite"</span>

✔ Name of migration … add question
The following migration(s) have been created and applied from new schema changes:

migrations/
  └─ 20210217035805_add_question/
    └─ migration.sql

✔ Generated Prisma Client (2.17.0) to ./node_modules/@prisma/client <span class="hljs-keyword">in</span> 103ms

Everything is now <span class="hljs-keyword">in</span> sync.
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>generate</code> 命令搭配 <code>all</code> 类型将生成相关的模型、queries、mutation 和页面文件。请参见 Blitz generate 页面查询更多可用的类型选项。</p>
<h4 data-id="heading-17">接下来，我们将生成带有相应 queries 和 mutations 的 <code>Choice</code> 模型。</h4>
<p>这次我们搭配 <code>resource</code> 类型，因为我们不需要为 <code>Choice</code> 模型生成页面：</p>
<pre><code class="hljs language-bash copyable" lang="bash">blitz generate resource choice text votes:int:default=0 belongsTo:question
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样，在系统提示你进行迁移时，按 <strong>Enter</strong> 后输入迁移的名称。</p>
<pre><code class="hljs language-bash copyable" lang="bash">CREATE    app/choices/queries/getChoice.ts
CREATE    app/choices/queries/getChoices.ts
CREATE    app/choices/mutations/createChoice.ts
CREATE    app/choices/mutations/deleteChoice.ts
CREATE    app/choices/mutations/updateChoice.ts

✔ Model <span class="hljs-keyword">for</span> <span class="hljs-string">'choice'</span> created <span class="hljs-keyword">in</span> schema.prisma:

> model Choice &#123;
>   id         Int      @default(autoincrement()) @id
>   createdAt  DateTime @default(now())
>   updatedAt  DateTime @updatedAt
>   text       String
>   votes      Int      @default(0)
>   question   Question @relation(fields: [questionId], references: [id])
>   questionId Int
> &#125;

? Run <span class="hljs-string">'prisma migrate dev'</span> to update your database? (Y/n) › <span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">最后，让我们更新 <code>Question</code> 模型以关联到 <code>Choice</code> 上。</h4>
<p>打开 <code>db/schema.prisma</code> 并在 <code>Question</code> 模型中添加 <code>choices Choice[]</code>。</p>
<pre><code class="hljs language-diff copyable" lang="diff">model Question &#123;
  id        Int      @id @default(autoincrement())
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  text      String
<span class="hljs-addition">+ choices   Choice[]</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后运行 <code>blitz prisma generate</code> 来更新 prisma 客户端以同步 schema 的更改。这里不涉及数据库迁移，因为数据库中没有实际字段添加到 <code>Question</code> 模型中。</p>
<h3 data-id="heading-19">访问 Prisma 数据库客户端</h3>
<p>现在，让我们跳进 Blitz 交互式 Shell 中，并使用 Blitz 为你提供的 Primsa 数据库客户端。要启动 Blitz 控制台，请使用以下命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash">blitz console
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一旦你进入控制台后，浏览数据库客户端：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># No questions are in the system yet.</span>
⚡ > await db.question.findMany()
[]

<span class="hljs-comment"># Create a new Question:</span>
⚡ > <span class="hljs-built_in">let</span> q = await db.question.create(&#123;data: &#123;text: <span class="hljs-string">"What's new?"</span>&#125;&#125;)
undefined

<span class="hljs-comment"># See the entire object:</span>
⚡ > q
&#123;
  id: 1,
  createdAt: 2020-06-15T15:06:14.959Z,
  updatedAt: 2020-06-15T15:06:14.959Z,
  text: <span class="hljs-string">"What's new?"</span>
&#125;

<span class="hljs-comment"># Or, access individual values on the object:</span>
⚡ > q.text
<span class="hljs-string">"What's new?"</span>

<span class="hljs-comment"># Change values by using the update function:</span>
⚡ > q = await db.question.update(&#123;<span class="hljs-built_in">where</span>: &#123;id: 1&#125;, data: &#123;text: <span class="hljs-string">"What's up?"</span>&#125;&#125;)
&#123;
  id: 1,
  createdAt: 2020-06-15T15:06:14.959Z,
  updatedAt: 2020-06-15T15:13:17.394Z,
  text: <span class="hljs-string">"What's up?"</span>
&#125;

<span class="hljs-comment"># db.question.findMany() now displays all the questions in the database:</span>
⚡ > await db.question.findMany()
[
  &#123;
    id: 1,
    createdAt: 2020-06-15T15:06:14.959Z,
    updatedAt: 2020-06-15T15:13:17.394Z,
    text: <span class="hljs-string">"What's up?"</span>
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">更新模型属性生成的代码</h3>
<blockquote>
<p>在再次运行该应用之前，我们需要自定义一些已生成的代码。最终这些修复过程将不再需要——但就目前而言，我们需要解决结果未解决的问题。</p>
</blockquote>
<p>自动生成的页面，当前并未使用你在生成过程中定义的实际模型的属性。以后会支持，但现在，需要我们手动修复生成的页面。</p>
<h4 data-id="heading-21">Question 页面</h4>
<p>进入 <code>app/pages/questions/index.tsx</code>. 请注意到一个 <code>QuestionsList</code> 组件已经为你生成了：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// app/pages/questions/index.tsx</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> QuestionsList = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> router = useRouter()
  <span class="hljs-keyword">const</span> page = <span class="hljs-built_in">Number</span>(router.query.page) || <span class="hljs-number">0</span>
  <span class="hljs-keyword">const</span> [&#123;questions, hasMore&#125;] = usePaginatedQuery(getQuestions, &#123;
    <span class="hljs-attr">orderBy</span>: &#123;<span class="hljs-attr">id</span>: <span class="hljs-string">"asc"</span>&#125;,
    <span class="hljs-attr">skip</span>: ITEMS_PER_PAGE * page,
    <span class="hljs-attr">take</span>: ITEMS_PER_PAGE,
  &#125;)

  <span class="hljs-keyword">const</span> goToPreviousPage = <span class="hljs-function">() =></span> router.push(&#123;<span class="hljs-attr">query</span>: &#123;<span class="hljs-attr">page</span>: page - <span class="hljs-number">1</span>&#125;&#125;)
  <span class="hljs-keyword">const</span> goToNextPage = <span class="hljs-function">() =></span> router.push(&#123;<span class="hljs-attr">query</span>: &#123;<span class="hljs-attr">page</span>: page + <span class="hljs-number">1</span>&#125;&#125;)

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        &#123;questions.map((question) => (
          <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;question.id&#125;</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">&#123;</span>`/<span class="hljs-attr">questions</span>/$&#123;<span class="hljs-attr">question.id</span>&#125;`&#125;></span>
              <span class="hljs-tag"><<span class="hljs-name">a</span>></span>&#123;question.name&#125;<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        ))&#125;
      <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">disabled</span>=<span class="hljs-string">&#123;page</span> === <span class="hljs-string">0&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;goToPreviousPage&#125;</span>></span>
        Previous
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">disabled</span>=<span class="hljs-string">&#123;!hasMore&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;goToNextPage&#125;</span>></span>
        Next
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过目前跑不通的！请记住我们创建的 <code>Question</code> 模型上面没有任何“name”字段。
要解决此问题，请替换 <code>question.name</code> 为 <code>question.text</code>。</p>
<pre><code class="hljs language-diff copyable" lang="diff">// app/pages/questions/index.tsx

export const QuestionsList = () => &#123;
  const router = useRouter()
  const page = Number(router.query.page) || 0
  const [&#123;questions, hasMore&#125;] = usePaginatedQuery(getQuestions, &#123;
    orderBy: &#123;id: "asc"&#125;,
    skip: ITEMS_PER_PAGE * page,
    take: ITEMS_PER_PAGE,
  &#125;)

  const goToPreviousPage = () => router.push(&#123;query: &#123;page: page - 1&#125;&#125;)
  const goToNextPage = () => router.push(&#123;query: &#123;page: page + 1&#125;&#125;)

  return (
    <div>
      <ul>
        &#123;questions.map((question) => (
          <li key=&#123;question.id&#125;>
            <Link href=&#123;`/questions/$&#123;question.id&#125;`&#125;>
<span class="hljs-deletion">-              <a>&#123;question.name&#125;</a></span>
<span class="hljs-addition">+              <a>&#123;question.text&#125;</a></span>
            </Link>
          </li>
        ))&#125;
      </ul>

      <button disabled=&#123;page <span class="hljs-comment">=== 0&#125; onClick=&#123;goToPreviousPage&#125;></span>
        Previous
      </button>
      <button disabled=&#123;!hasMore&#125; onClick=&#123;goToNextPage&#125;>
        Next
      </button>
    </div>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们将类似的修复方法应用于 <code>app/questions/components/QuestionForm.tsx</code> 中。在表单提交中，将 <code>LabeledTextField</code> 中 <code>name</code> 变为 <code>text</code>。</p>
<pre><code class="hljs language-diff copyable" lang="diff">export function QuestionForm<S extends z.ZodType<any, any>>(
  props: FormProps<S>,
) &#123;
  return (
    <Form<S> &#123;...props&#125;>
<span class="hljs-deletion">-     <LabeledTextField name="name" label="Name" placeholder="Name" /></span>
<span class="hljs-addition">+     <LabeledTextField name="text" label="Text" placeholder="Text" /></span>
    </Form>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22"><code>createQuestion</code> mutation</h4>
<p>在 <code>app/questions/mutations/createQuestion.ts</code> 中，我们需要更新 <code>CreateQuestion</code> zod 验证模式，使用 <code>text</code> 而不是 <code>name</code>。</p>
<pre><code class="hljs language-diff copyable" lang="diff">// app/questions/mutations/createQuestion.ts

const CreateQuestion = z
  .object(&#123;
<span class="hljs-deletion">-   name: z.string(),</span>
<span class="hljs-addition">+   text: z.string(),</span>
  &#125;)
  .nonstrict()
// ...
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23"><code>updateQuestion</code> mutation</h4>
<p>在 <code>app/questions/mutations/updateQuestion.ts</code> 中，我们需要更新 <code>UpdateQuestion</code> zod 验证模式，使用 <code>text</code> 而不是 <code>name</code>。</p>
<pre><code class="hljs language-diff copyable" lang="diff">// app/questions/mutations/updateQuestion.ts

const UpdateQuestion = z
  .object(&#123;
    id: z.number(),
<span class="hljs-deletion">-   name: z.string(),</span>
<span class="hljs-addition">+   text: z.string(),</span>
  &#125;)
  .nonstrict()
// ...
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24"><code>deleteQuestion</code> mutation</h4>
<p>Prisma 尚不支持“级联删除”。在本教程的上下文中，这意味着它在删除 <code>Question</code> 时不会删除相关的 <code>Choice</code>数据。我们需要临时改动生成的 <code>deleteQuestion</code> mutation，以便手动做这件事。在文本编辑框中打开 <code>app/questions/mutations/deleteQuestion.ts</code> 并将以下内容添加到函数主体的顶
部。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">await</span> db.choice.deleteMany(&#123;<span class="hljs-attr">where</span>: &#123;<span class="hljs-attr">questionId</span>: id&#125;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终的效果应该为：</p>
<pre><code class="hljs language-diff copyable" lang="diff">// app/questions/mutations/deleteQuestion.ts

export default resolver.pipe(
  resolver.zod(DeleteQuestion),
  resolver.authorize(),
  async (&#123;id&#125;) => &#123;
<span class="hljs-addition">+   await db.choice.deleteMany(&#123;where: &#123;questionId: id&#125;&#125;)</span>
    const question = await db.question.deleteMany(&#123;where: &#123;id&#125;&#125;)

    return question
  &#125;,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，此 mutation 将在删除问题本身之前，删除与问题相关的选择。</p>
<h4 data-id="heading-25">现在尝试创建、更新和删除问题</h4>
<p>太棒了！现在确保你的程序正常运行。否则在你的终端中执行 <code>blitz dev</code>，然后访问 <code>localhost:3000/questions</code>。尝试创建问题并编辑、删除它们。</p>
<h3 data-id="heading-26">在问题表格中添加选择项</h3>
<p>到目前为止，你做的很棒！我们要做的下一件事是在我们的问题中添加选择。在你的编辑器中打开 <code>app/questions/components/QuestionForm.tsx</code>。</p>
<p>添加另外三个 <code><LabeledTextField></code> 组件作为选择。</p>
<pre><code class="hljs language-diff copyable" lang="diff">export function QuestionForm<S extends z.ZodType<any, any>>(
  props: FormProps<S>,
) &#123;
  return (
    <Form<S> &#123;...props&#125;>
      <LabeledTextField name="text" label="Text" placeholder="Text" />
<span class="hljs-addition">+     <LabeledTextField name="choices.0.text" label="Choice 1" /></span>
<span class="hljs-addition">+     <LabeledTextField name="choices.1.text" label="Choice 2" /></span>
<span class="hljs-addition">+     <LabeledTextField name="choices.2.text" label="Choice 3" /></span>
    </Form>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在打开 <code>app/pages/questions/new.tsx</code> 并设置 <code>initialValues</code> 为如下：</p>
<pre><code class="hljs language-diff copyable" lang="diff">      <QuestionForm
        submitText="Create Question"
<span class="hljs-deletion">-       // initialValues=&#123;&#123; &#125;&#125;</span>
<span class="hljs-addition">+       initialValues=&#123;&#123;choices: []&#125;&#125;</span>
        onSubmit=&#123;async (values) => &#123;
          try &#123;
            const question = await createQuestionMutation(values)
            router.push(`/questions/$&#123;question.id&#125;`)
          &#125; catch (error) &#123;
            console.error(error)
            return &#123;
              [FORM_ERROR]: error.toString(),
            &#125;
          &#125;
        &#125;&#125;
      />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来打开 <code>app/questions/mutations/createQuestion.ts</code> 并更新 zod 模式，来让 mutation 接收 choice 数据。而且我们还需要更新 <code>db.question.create</code> 调用，以便 choice 也可以被创建。</p>
<pre><code class="hljs language-diff copyable" lang="diff">// app/questions/mutations/createQuestion.ts

const CreateQuestion = z
  .object(&#123;
    text: z.string(),
<span class="hljs-addition">+   choices: z.array(z.object(&#123;text: z.string()&#125;)),</span>
  &#125;)
  .nonstrict()

export default resolver.pipe(
  resolver.zod(CreateQuestion),
  resolver.authorize(),
  async (input) => &#123;
<span class="hljs-deletion">-   const question = await db.question.create(&#123;data: input&#125;)</span>
<span class="hljs-addition">+   const question = await db.question.create(&#123;</span>
<span class="hljs-addition">+     data: &#123;</span>
<span class="hljs-addition">+       ...input,</span>
<span class="hljs-addition">+       choices: &#123;create: input.choices&#125;,</span>
<span class="hljs-addition">+     &#125;,</span>
<span class="hljs-addition">+   &#125;)</span>

    return question
  &#125;,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">试试看</h4>
<p>现在你可以转到 <code>localhost:3000/questions/new</code> 并创建一个带有选择的新问题！</p>
<h3 data-id="heading-28">列出选择</h3>
<p>该轻松一下了。返回浏览器中的 <code>localhost:3000/questions</code> 并查看你创建的所有问题。让我们在这些问题下列出相关的选择如何？首先，我们需要自定义问题查询函数。在 Prisma 中，你需要手动让客户端知道你需要查询的嵌套关系，将你的 <code>getQuestion.ts</code> 和 <code>getQuestions.ts</code> 文件更改为如下所示：</p>
<pre><code class="hljs language-diff copyable" lang="diff">// app/questions/queries/getQuestion.ts

const GetQuestion = z.object(&#123;
  // This accepts type of undefined, but is required at runtime
  id: z.number().optional().refine(Boolean, "Required"),
&#125;)

export default resolver.pipe(
  resolver.zod(GetQuestion),
  resolver.authorize(),
  async (&#123;id&#125;) => &#123;
<span class="hljs-deletion">-   const question = await db.question.findFirst(&#123;where: &#123;id&#125;&#125;)</span>
<span class="hljs-addition">+   const question = await db.question.findFirst(&#123;</span>
<span class="hljs-addition">+     where: &#123;id&#125;,</span>
<span class="hljs-addition">+     include: &#123;choices: true&#125;,</span>
<span class="hljs-addition">+   &#125;)</span>

    if (!question) throw new NotFoundError()

    return question
  &#125;,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-diff copyable" lang="diff">// app/questions/queries/getQuestions.ts

interface GetQuestionsInput
  extends Pick<
    Prisma.QuestionFindManyArgs,
    "where" | "orderBy" | "skip" | "take"
  > &#123;&#125;

export default resolver.pipe(
  resolver.authorize(),
  async (&#123;where, orderBy, skip = 0, take = 100&#125;: GetQuestionsInput) => &#123;
    const &#123;items: questions, hasMore, nextPage, count&#125; = await paginate(&#123;
      skip,
      take,
      count: () => db.question.count(&#123;where&#125;),
      query: (paginateArgs) =>
        db.question.findMany(&#123;
          ...paginateArgs,
          where,
          orderBy,
<span class="hljs-addition">+         include: &#123;choices: true&#125;,</span>
        &#125;),
    &#125;)

    return &#123;
      questions,
      nextPage,
      hasMore,
      count,
    &#125;
  &#125;,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在在浏览器中跳回我们主要的 Question 页面 (<code>app/pages/questions/index.tsx</code>)，我们可以列出每个问题的选择。并将此代码添加到我们 <code>QuestionsList</code> 中的 <code>Link</code> 下：</p>
<pre><code class="hljs language-diff copyable" lang="diff">// app/pages/questions/index.tsx

// ...
&#123;
  questions.map((question) => (
    <li key=&#123;question.id&#125;>
      <Link href=&#123;`/questions/$&#123;question.id&#125;`&#125;>
        <a>&#123;question.text&#125;</a>
      </Link>
<span class="hljs-addition">+     <ul></span>
<span class="hljs-addition">+       &#123;question.choices.map((choice) => (</span>
<span class="hljs-addition">+         <li key=&#123;choice.id&#125;></span>
<span class="hljs-addition">+           &#123;choice.text&#125; - &#123;choice.votes&#125; votes</span>
<span class="hljs-addition">+         </li></span>
<span class="hljs-addition">+       ))&#125;</span>
<span class="hljs-addition">+     </ul></span>
    </li>
  ))
&#125;
// ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在在浏览器中访问 <code>/questions</code> 路由。<strong>神奇吧！</strong></p>
<h3 data-id="heading-29">让我们允许用户对这些问题投票！</h3>
<p>在浏览器中打开 <code>app/pages/questions/[questionId].tsx</code>。首先，我们将对该页面进行一些改造。</p>
<ol>
<li>替换 <code><h1>Question &#123;question.id&#125;</h1></code> 为 <code><h1>&#123;question.text&#125;</h1></code>.</li>
<li>删除 <code>pre</code> 元素，并将如下复制到之前写的选择列表中：</li>
</ol>
<pre><code class="hljs language-jsx copyable" lang="jsx"><ul>
  &#123;question.choices.map(<span class="hljs-function">(<span class="hljs-params">choice</span>) =></span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;choice.id&#125;</span>></span>
      &#123;choice.text&#125; - &#123;choice.votes&#125; votes
    <span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
  ))&#125;
</ul>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果返回浏览器，页面目前看起来像这样！</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b900c05f8a78403c833a511fc00382a6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-30">现在是时候来增加投票功能！</h3>
<p>首先我们需要打开 <code>app/choices/mutations/updateChoice.ts</code>，更新 zod 模式，添加新增投票功能。</p>
<pre><code class="hljs language-diff copyable" lang="diff">const UpdateChoice = z
  .object(&#123;
    id: z.number(),
<span class="hljs-deletion">-   name: z.string(),</span>
  &#125;)
  .nonstrict()

export default resolver.pipe(
  resolver.zod(UpdateChoice),
  resolver.authorize(),
  async (&#123;id, ...data&#125;) => &#123;
<span class="hljs-deletion">-   const choice = await db.choice.update(&#123;where: &#123;id&#125;, data&#125;)</span>
<span class="hljs-addition">+   const choice = await db.choice.update(&#123;</span>
<span class="hljs-addition">+     where: &#123;id&#125;,</span>
<span class="hljs-addition">+     data: &#123;votes: &#123;increment: 1&#125;&#125;,</span>
<span class="hljs-addition">+   &#125;)</span>

    return choice
  &#125;,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回到 <code>app/pages/questions/[questionId].tsx</code> 中进行如下更改：</p>
<p>在我们的 <code>li</code> 中，新增一个如下的 <code>button</code>：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><li key=&#123;choice.id&#125;>
  &#123;choice.text&#125; - &#123;choice.votes&#125; votes
  <button>Vote</button>
</li>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，导入我们更新的 <code>updateChoice</code> mutation，并在页面中创建 <code>handleVote</code> 函数。</p>
<pre><code class="hljs language-diff copyable" lang="diff">// app/pages/questions/[questionId].tsx
<span class="hljs-addition">+import updateChoice from "app/choices/mutations/updateChoice"</span>

//...

export const Question = () => &#123;
  const router = useRouter()
  const questionId = useParam("questionId", "number")
  const [deleteQuestionMutation] = useMutation(deleteQuestion)
  const [question] = useQuery(getQuestion, &#123;id: questionId&#125;)
<span class="hljs-addition">+ const [updateChoiceMutation] = useMutation(updateChoice)</span>
<span class="hljs-addition">+</span>
<span class="hljs-addition">+ const handleVote = async (id: number) => &#123;</span>
<span class="hljs-addition">+   try &#123;</span>
<span class="hljs-addition">+     await updateChoiceMutation(&#123;id&#125;)</span>
<span class="hljs-addition">+     refetch()</span>
<span class="hljs-addition">+   &#125; catch (error) &#123;</span>
<span class="hljs-addition">+     alert("Error updating choice " + JSON.stringify(error, null, 2))</span>
<span class="hljs-addition">+   &#125;</span>
<span class="hljs-addition">+ &#125;</span>

  return (
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们需要更新问题相关的 <code>useQuery</code> 调用以返回需要在 <code>handleVote</code> 内部使用的 <code>refetch</code> 函数。</p>
<pre><code class="hljs language-diff copyable" lang="diff">// app/pages/questions/[questionId].tsx

//...
<span class="hljs-deletion">- const [question] = useQuery(getQuestion, &#123;id: questionId&#125;)</span>
<span class="hljs-addition">+ const [question, &#123;refetch&#125;] = useQuery(getQuestion, &#123;id: questionId&#125;)</span>
//...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，我们将告诉新的 <code>button</code> 来条用该函数！</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><button onClick=&#123;<span class="hljs-function">() =></span> handleVote(choice.id)&#125;>Vote</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终的 <code>Question</code> 组件应该是这个样子：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Question = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> router = useRouter()
  <span class="hljs-keyword">const</span> questionId = useParam(<span class="hljs-string">"questionId"</span>, <span class="hljs-string">"number"</span>)
  <span class="hljs-keyword">const</span> [deleteQuestionMutation] = useMutation(deleteQuestion)
  <span class="hljs-keyword">const</span> [question, &#123;refetch&#125;] = useQuery(getQuestion, &#123;<span class="hljs-attr">id</span>: questionId&#125;)
  <span class="hljs-keyword">const</span> [updateChoiceMutation] = useMutation(updateChoice)

  <span class="hljs-keyword">const</span> handleVote = <span class="hljs-keyword">async</span> (id: number) => &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">await</span> updateChoiceMutation(&#123;id&#125;)
      refetch()
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      alert(<span class="hljs-string">"Error updating choice "</span> + <span class="hljs-built_in">JSON</span>.stringify(error, <span class="hljs-literal">null</span>, <span class="hljs-number">2</span>))
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">Head</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Question &#123;question.id&#125;<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Head</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;question.text&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
          &#123;question.choices.map((choice) => (
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;choice.id&#125;</span>></span>
              &#123;choice.text&#125; - &#123;choice.votes&#125; votes
              <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> handleVote(choice.id)&#125;>Vote<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
          ))&#125;
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">&#123;</span>`/<span class="hljs-attr">questions</span>/$&#123;<span class="hljs-attr">question.id</span>&#125;/<span class="hljs-attr">edit</span>`&#125;></span>
          <span class="hljs-tag"><<span class="hljs-name">a</span>></span>Edit<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">Link</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">button</span>
          <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span>
          <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;async</span> () =></span> &#123;
            if (window.confirm("This will be deleted")) &#123;
              await deleteQuestionMutation(&#123;id: question.id&#125;)
              router.push("/questions")
            &#125;
          &#125;&#125;
          style=&#123;&#123;marginLeft: "0.5rem"&#125;&#125;
        >
          Delete
        <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">最后，让我们支持编辑某问题下的一个选择</h3>
<p>如果单击现有问题之一上的“编辑”按钮，你将看到它使用与创建问题相同的形式。至
此，该部分已经完成！我们只需要更新我们的 mutation。</p>
<p>打开 <code>app/questions/mutations/updateQuestion.ts</code> 并进行如下改动：</p>
<pre><code class="hljs language-diff copyable" lang="diff">// app/questions/mutations/updateQuestion.ts
import &#123;resolver&#125; from "blitz"
import db from "db"
import * as z from "zod"

const UpdateQuestion = z
  .object(&#123;
    id: z.number(),
    text: z.string(),
<span class="hljs-addition">+   choices: z.array(</span>
<span class="hljs-addition">+     z.object(&#123;id: z.number().optional(), text: z.string()&#125;).nonstrict(),</span>
<span class="hljs-addition">+   ),</span>
  &#125;)
  .nonstrict()

export default resolver.pipe(
  resolver.zod(UpdateQuestion),
  resolver.authorize(),
  async (&#123;id, ...data&#125;) => &#123;
<span class="hljs-deletion">-   const question = await db.question.update(&#123;where: &#123;id&#125;, data&#125;)</span>
<span class="hljs-addition">+   const question = await db.question.update(&#123;</span>
<span class="hljs-addition">+     where: &#123;id&#125;,</span>
<span class="hljs-addition">+     data: &#123;</span>
<span class="hljs-addition">+       ...data,</span>
<span class="hljs-addition">+       choices: &#123;</span>
<span class="hljs-addition">+         upsert: data.choices.map((choice) => (&#123;</span>
<span class="hljs-addition">+           // Appears to be a prisma bug,</span>
<span class="hljs-addition">+           // because `|| 0` shouldn't be needed</span>
<span class="hljs-addition">+           where: &#123;id: choice.id || 0&#125;,</span>
<span class="hljs-addition">+           create: &#123;text: choice.text&#125;,</span>
<span class="hljs-addition">+           update: &#123;text: choice.text&#125;,</span>
<span class="hljs-addition">+         &#125;)),</span>
<span class="hljs-addition">+       &#125;,</span>
<span class="hljs-addition">+     &#125;,</span>
<span class="hljs-addition">+   &#125;)</span>

    return question
  &#125;,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>[upsert](https://www.prisma.io/docs/reference/api-reference/prisma-client-reference#upsert)</code> 是一种特殊的操作，表示“如果存在此项目，请对其进行更新。否则创建它”。这对于
当前情况是完美的，因为我们不需要用户在创建问题时同时添加三个选择。所以如果
用户通过编辑问题添加另一个选择，则将在此处创建它。</p>
<h3 data-id="heading-32">结尾</h3>
<p>🥳 恭喜！你创建了自己的 Blitz 应用！祝你玩得开心，也欢迎与你的朋友分享。现在，你已经完成了本教程，为什么不尝试使你的投票应用变得更好呢？你可以尝试：</p>
<ul>
<li>添加样式 (提示, 试试 <code>blitz install tailwind</code> 或 <code>blitz install chakra-ui</code>)</li>
<li>显示更多有关选票的统计信息</li>
<li>在 Render 或 Vercel 上实时部署。</li>
</ul>
<p>如果你想与全球 Blitz 社区分享你的项目，没有比 Discord 更好的地方了。</p>
<p>访问 <a href="https://discord.blitzjs.com/" target="_blank" rel="nofollow noopener noreferrer">discord.blitzjs.com</a>。然后，将连接发布到 <strong>#built-with-blitz</strong> 频道来与所有人共享！</p>
<h2 data-id="heading-33">译者结语</h2>
<p>本文内容属于 <a href="https://blitzjs.com/docs" target="_blank" rel="nofollow noopener noreferrer">Blitz.js 官方文档</a> - 简介章节的前半部分。总共十四个章节（简介、社区、基础、页面、路由、权限、数据库、Queries 和 Mutations、后端架构、部署、配方、配置、CLI 和模板）。未来不定期翻译其余章节，也可能会原创一些文章。</p>
<p>《<a href="https://github.com/hylerrix/blitzjs-tutorial" target="_blank" rel="nofollow noopener noreferrer">Blitz.js + React 全栈开发手册</a>》系列专注探索 Blitz.js + React 全栈应用开发，原文翻译内容会同步更新到 <a href="https://github.com/blitz-js/zh-hans.blitzjs.com" target="_blank" rel="nofollow noopener noreferrer">Blitz.js 中文仓库</a> 上。欢迎 Star、Watch 或关注公众号 (@ningowood) 来及时接收消息。</p>
<blockquote>
<p>2021 © <a href="https://github.com/hylerrix/blitzjs-tutorial" target="_blank" rel="nofollow noopener noreferrer">github.com/hylerrix/bl…</a></p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            