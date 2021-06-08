
---
title: 'Prisma：适用于Node.js和TypeScript的完整ORM'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d397a20478f468799f73bd94c4cd658~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 04:54:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d397a20478f468799f73bd94c4cd658~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://www.prisma.io/" target="_blank" rel="nofollow noopener noreferrer">Prisma</a>是Node.js和TypeScript的下一代ORM。经过两年多的开发，我们很高兴分享所有Prisma工具已准备好投入生产！</p>
<h2 data-id="heading-0">对象关系映射的新范例</h2>
<p>Prisma是适用于Node.js和TypeScript的下一代<a href="https://www.github.com/prisma/prisma" target="_blank" rel="nofollow noopener noreferrer">开源</a>ORM。它包含以下工具：</p>
<ul>
<li><a href="https://www.prisma.io/client" target="_blank" rel="nofollow noopener noreferrer"><strong>Prisma Client</strong></a>——自动生成且类型安全的数据库客户端</li>
<li><a href="https://www.prisma.io/migrate" target="_blank" rel="nofollow noopener noreferrer"><strong>Prisma Migrate</strong></a>——声明式数据建模和可自定义的迁移</li>
<li><a href="https://www.prisma.io/studio" target="_blank" rel="nofollow noopener noreferrer"><strong>Prisma Studio</strong></a>——现代化的用户界面，可查看和编辑数据</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d397a20478f468799f73bd94c4cd658~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这些工具可以在任何Node.js或TypeScript项目中一起或单独采用。Prisma当前支持PostgreSQL，MySQL，SQLite，SQL Server（预览版）。 MongoDB的连接器正在开发中，请在<a href="https://www.notion.so/prismaio/Support-MongoDB-9f115ebf4a754069a7d7eaae94dc4651" target="_blank" rel="nofollow noopener noreferrer">此处注册Early Access程序</a>。</p>
<h3 data-id="heading-1">数据库是很难的</h3>
<p>使用数据库是应用程序开发中最具挑战性的领域之一。数据建模，模式迁移和编写数据库查询是应用程序开发人员每天处理的常见任务。</p>
<p>在Prisma，我们发现Node.js生态系统虽然在构建数据库支持的应用程序中越来越流行，但并未为应用程序开发人员提供处理这些任务的现代工具。</p>
<blockquote>
<p>应用程序开发人员应该关心数据，而不是SQL</p>
</blockquote>
<p>随着工具变得更加专业化，应用程序开发人员应该能够专注于为组织实现增值功能，而不必花费时间通过编写胶合代码来遍历应用程序的各个层。</p>
<h3 data-id="heading-2">Prisma-Node.js和TypeScript的完整ORM</h3>
<p>尽管Prisma解决了与传统ORM相似的问题，但是其对这些问题的处理方式却根本不同。</p>
<p><strong>Prisma模式中的数据建模</strong></p>
<p>使用Prisma时，您可以在Prisma模式中定义数据模型。以下是Prisma模型的样例：</p>
<pre><code class="hljs language-js copyable" lang="js">model Post &#123;
  id        Int     @id @<span class="hljs-keyword">default</span>(autoincrement())
  title     <span class="hljs-built_in">String</span>
  content   <span class="hljs-built_in">String</span>?
  published <span class="hljs-built_in">Boolean</span> @<span class="hljs-keyword">default</span>(<span class="hljs-literal">false</span>)
  author    User?   @relation(fields: [authorId], <span class="hljs-attr">references</span>: [id])
  authorId  Int?
&#125;

model User &#123;
  id    Int     @id @<span class="hljs-keyword">default</span>(autoincrement())
  email <span class="hljs-built_in">String</span>  @unique
  name  <span class="hljs-built_in">String</span>?
  posts Post[]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些模型中的每一个都映射到基础数据库中的表，并充当Prisma Client提供的生成的数据访问API的基础。Prisma的<a href="https://marketplace.visualstudio.com/items?itemName=Prisma.prisma" target="_blank" rel="nofollow noopener noreferrer">VS Code扩展</a>提供语法高亮显示，自动补全，快速修复和许多其他功能，使数据建模具有神奇而令人愉悦的体验。</p>
<p><strong>使用Prisma Migrate进行数据库迁移</strong></p>
<p>Prisma Migrate将Prisma模式转换为所需的SQL，以创建和更改数据库中的表。可以通过<a href="https://www.prisma.io/docs/concepts/components/prisma-cli" target="_blank" rel="nofollow noopener noreferrer">Prisma CLI</a>提供的 <code>prisma migration</code> 命令使用它。</p>
<p>PostgreSQL:</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">TABLE</span> "Post" (
    "id" SERIAL <span class="hljs-keyword">NOT</span> <span class="hljs-keyword">NULL</span>,
    "title" TEXT <span class="hljs-keyword">NOT</span> <span class="hljs-keyword">NULL</span>,
    "content" TEXT,
    "published" <span class="hljs-type">BOOLEAN</span> <span class="hljs-keyword">NOT</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">DEFAULT</span> <span class="hljs-literal">false</span>,
    "authorId" <span class="hljs-type">INTEGER</span>,

    <span class="hljs-keyword">PRIMARY</span> KEY ("id")
);

<span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">TABLE</span> "User" (
    "id" SERIAL <span class="hljs-keyword">NOT</span> <span class="hljs-keyword">NULL</span>,
    "email" TEXT <span class="hljs-keyword">NOT</span> <span class="hljs-keyword">NULL</span>,
    "name" TEXT,

    <span class="hljs-keyword">PRIMARY</span> KEY ("id")
);

<span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">UNIQUE</span> INDEX "User.email_unique" <span class="hljs-keyword">ON</span> "User"("email");

<span class="hljs-keyword">ALTER</span> <span class="hljs-keyword">TABLE</span> "Post" <span class="hljs-keyword">ADD</span> <span class="hljs-keyword">FOREIGN</span> KEY ("authorId") <span class="hljs-keyword">REFERENCES</span> "User"("id") <span class="hljs-keyword">ON</span> <span class="hljs-keyword">DELETE</span> <span class="hljs-keyword">SET</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">ON</span> UPDATE CASCADE;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在基于Prisma模式自动生成SQL的同时，您可以轻松地根据自己的特定需求对其进行自定义。通过这种方法，Prisma Migrate在生产率和控制力之间取得了很好的平衡。</p>
<p><strong>使用Prisma Client进行直观且类型安全的数据库访问</strong></p>
<p>与Prisma Client一起使用的主要好处是，它使开发人员可以在对象中进行思考，因此提供了一种熟悉且自然的方式来推理其数据。</p>
<p>Prisma Client没有模型实例的概念。相反，它有助于制定始终返回纯JavaScript对象的数据库查询。多亏了生成的类型，您也为这些查询获得了自动补全功能。</p>
<p>另外，作为对TypeScript开发者的一种奖励。Prisma Client查询的所有结果都是完全类型化的。事实上，Prisma提供了任何TypeScript ORM中最强大的类型安全保证（你可以在这里阅读与TypeORM的类型安全比较）。</p>
<p><strong>Prisma Studio的现代管理界面</strong></p>
<p>Prisma还为你的数据库提供了一个现代化的管理界面--想想看phpMyAdmin，但在2021年。😉</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05872cf881d0496184a85357d868c2f8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">Prisma适合任何技术栈</h2>
<p>Prisma与你构建的应用程序无关，并将很好地补充你的技术栈，无论你喜欢的技术是什么。你可以在这里找到更多关于Prisma如何与你喜欢的框架或库一起工作的信息。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7e4e0d9c757443dbad00ecf2530f026~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">为任务关键型应用程序的生产做好准备</h2>
<p>Prisma在过去三年中发展了很多，我们非常高兴与开发人员社区分享结果。</p>
<h3 data-id="heading-5">从GraphQL到数据库</h3>
<p>自从我们开始构建开发人员工具以来，作为一家公司，在过去的几年中，我们经历了许多主要的产品迭代和发展过程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bed1f2d2a3a4da084ac8a645f9ae3d2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Prisma是我们从成为GraphQL生态系统的早期创新者中学到的经验教训以及我们从小型创业公司到大型企业的各种规模的数据层获得的见解的结果。</p>
<p>自三年前首次发布以来，Prisma已被成千上万的公司使用，Prisma经过了实战测试，并准备用于关键任务应用程序。</p>
<h3 data-id="heading-6">我们关心开发人员</h3>
<p>Prisma是开放开发的。我们的产品和工程团队正在监控GitHub的问题，通常在问题打开后24小时内做出响应。</p>
<p>新版本每两周发布一次，包含新特性、bug修复和大量改进。每次发布后，我们都会在Youtube上直播新功能，并从社区获得反馈。</p>
<p>我们还会尝试通过专门的社区支持团队，在开发人员提出关于Prisma的任何问题时，无论是在Slack，GitHub讨论区还是Stackoverflow上，都可以为他们提供帮助。</p>
<p>这是我们的社区数量：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7280fa39dc74f328fe0dd79ad5d8416~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">公司在生产中使用Prisma</h3>
<p>我们很高兴看到Prisma如何帮助各种规模的公司提高生产力并更快地交付产品。</p>
<p>在我们的旅程中，阿迪达斯、HyreCar、Agora Systems、Labelbox等公司为我们提供了关于如何发展产品的宝贵意见。我们有幸与一些最具创新性和独创性的技术领导者合作。</p>
<p>如果您想了解Prisma如何帮助这些公司提高生产力，请查看以下资源：</p>
<ul>
<li>
<p>Rapha</p>
<ul>
<li>blog——<a href="https://www.prisma.io/blog/helping-rapha-access-data-across-platforms-n3jfhtyu6rgn" target="_blank" rel="nofollow noopener noreferrer">Prisma如何帮助Rapha管理其移动应用程序数据</a></li>
<li>Talk——<a href="https://www.youtube.com/watch?v=A617FvOZdFE&ab_channel=Prisma" target="_blank" rel="nofollow noopener noreferrer">Prisma在Rapha</a></li>
</ul>
</li>
<li>
<p>iopool</p>
<ul>
<li>blog——<a href="https://www.prisma.io/blog/iopool-customer-success-story-uLsCWvaqzXoa" target="_blank" rel="nofollow noopener noreferrer">iopool如何使用Prisma在不到6个月的时间内重构其应用程序</a></li>
<li>Talk——<a href="https://www.youtube.com/watch?v=mWvroX_lkZI&ab_channel=Prisma" target="_blank" rel="nofollow noopener noreferrer">Prisma在ipool</a></li>
</ul>
</li>
</ul>
<h3 data-id="heading-8">从原型到开发再到生产</h3>
<p>最好的开发者工具是那些不走寻常路的工具，并能轻松地适应项目的日益复杂化。这正是我们设计Prisma的方式。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f02506ccbad1484f9ab94da5586d252f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Prisma有内置的工作流程，适用于开发生命周期的所有阶段，从原型设计到开发，到部署，到CI/CD，到测试等等。</p>
<h3 data-id="heading-9">下一代Web框架基于Prisma构建</h3>
<p>我们特别感到谦虚，许多框架和库作者选择Prisma作为其工具的默认ORM。以下是一些使用Prisma的高级框架的选择：</p>
<ul>
<li><a href="https://redwoodjs.com/" target="_blank" rel="nofollow noopener noreferrer">RedwoodJS</a>——基于React和GraphQL的全栈框架</li>
<li><a href="https://blitzjs.com/" target="_blank" rel="nofollow noopener noreferrer">Blitz</a>——基于Next.js的全栈框架</li>
<li><a href="https://next.keystonejs.com/" target="_blank" rel="nofollow noopener noreferrer">KeystoneJS</a>——无头CMS</li>
<li><a href="https://wasp-lang.dev/" target="_blank" rel="nofollow noopener noreferrer">Wasp</a>——用于基于React开发全栈Web应用程序的DSL</li>
<li><a href="http://amplication.com/" target="_blank" rel="nofollow noopener noreferrer">Amplication</a>——用于基于React和NestJS构建全栈应用程序的工具集</li>
</ul>
<h2 data-id="heading-10">开源及其他</h2>
<p>我们是一家由VC资助的公司，其团队热衷于改善应用程序开发人员的生活。当我们通过构建开源工具开始我们的旅程时，我们对Prisma的长期愿景远比构建“仅” ORM更大。</p>
<p>在我们最近的企业活动和Prisma聚会中，我们开始分享这一愿景，我们称之为<strong>应用程序数据平台</strong>。</p>
<blockquote>
<p>Prisma的愿景是使Facebook、Twitter和Airbnb等公司使用的定制数据访问层民主化，并使其适用于所有规模的开发团队和组织。</p>
</blockquote>
<p>这个想法主要是受到Facebook、Twitter和Airbnb等公司的启发，这些公司在其数据库和其他数据源的基础上建立了定制的数据访问层，使应用程序开发人员更容易以安全和高效的方式访问他们需要的数据。</p>
<p>Prisma的目标是使这种自定义数据访问层的思想民主化，并使其可用于任何规模的开发团队和组织。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/228353a6bcbd4b5ba650df0c5bc6007f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>翻译自<a href="https://www.prisma.io/blog/prisma-the-complete-orm-inw24qjeawmb" target="_blank" rel="nofollow noopener noreferrer">www.prisma.io/blog/prisma…</a></p></div>  
</div>
            