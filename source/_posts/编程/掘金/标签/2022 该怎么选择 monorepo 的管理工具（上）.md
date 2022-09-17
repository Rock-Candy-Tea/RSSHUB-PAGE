
---
title: '2022 该怎么选择 monorepo 的管理工具（上）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56ec6b5322c64c76b456ea389c222684~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 18:54:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56ec6b5322c64c76b456ea389c222684~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>monorepo 的概念已经火了好几年，相关的工具也是层出不穷，前端 Engineer 该又要说<strong>学不动了，</strong> 最近我其实也有同感。</p>
<p>最近在做一个帮助团队同学快速创建一个符合团队规范、集成完善工作流的脚手架工具，为了方便管理和扩展，也是选择了 monorepo 的工程管理方式，所以也是花了些时间去调研业界内的一些工具。最后，结合我们的场景，选择一个合适的。</p>
<p>其实个人不纠结工具是否新旧问题，关键的点是满足我的需求（尽量集成 bump version、生成 changelog 等功能），使用也尽量简单，上手成本低，最好开销即用。</p>
<p>综合对比了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Flerna.js.org%2Fdocs%2Fgetting-started" target="_blank" rel="nofollow noopener noreferrer" title="https://lerna.js.org/docs/getting-started" ref="nofollow noopener noreferrer">lerna@5</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpnpm.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://pnpm.io/" ref="nofollow noopener noreferrer">pnpm</a> + <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchangesets%2Fchangesets" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/changesets/changesets" ref="nofollow noopener noreferrer">changeset</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnx.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nx.dev/" ref="nofollow noopener noreferrer">Nx</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fturborepo.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://turborepo.org/" ref="nofollow noopener noreferrer">Turborepo</a>，最后选了 <strong>lerna@5</strong>，本文结合我个人对以上几款工具的理解（确实有点学不动🐶），并总结下我最后为什么选择 lerna@5 的心路历程。</p>
<h2 data-id="heading-1">为什么需要 monorepo</h2>
<p><strong>一个新的工程管理方式的出现，代表它能解决特定的场景问题</strong>。我们有时候选择一些技术栈或者架构方案，不是为了盲目追求新技术，而是我们的使用场景确实需要，当然 monorepo 在 2022 也不算是一个新的概念了。</p>
<p>所以在你选择 monorepo 工程管理的方案时，你是否有问过自己，我真的需要 monorepo 吗？如果单个 NPM 包能解决问题，其实就没必要强行引入 monorepo，<strong>NPM 包本应该小而美</strong>。</p>
<p>我个人理解选择 monorepo 的方式有如下两个关键的理由：</p>
<ul>
<li><strong>多个项目需要共享相同的工作流并且这些项目正好又是归属同一个使用场景，或者组合起来是一个大的工程项目</strong>；例如我参与的开源项目 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwangeditor-team%2FwangEditor" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wangeditor-team/wangEditor" ref="nofollow noopener noreferrer">wangeEditor</a>，在 v5+ 版本已经使用 monorepo 方式管理，我们会把核心的编辑器功能和一些复杂的菜单功能拆分不同的包管理；</li>
<li><strong>项目之间有依赖关系</strong>；例如在一个 monorepo 中，项目 A、B 依赖了项目 C，如果跳出 monorepo ，我们升级了 C，需要手动升级 A、B，<strong>依赖关系越复杂，手动维护的成本越高</strong>。</li>
</ul>
<p>我们的 cli 工具在最初的设计中，我想要将 cli 的功能和核心的 command 功能分开维护，分为：cli 和 core 两个包，cli 依赖 core，后续 cli 功能丰富后，可能还会有更多的包，所以当时选择了 monorepo 的管理方式。虽然最后实现的时候有点差异，但是大差不差，核心的设计理念没有变化。</p>
<p>下面我们进入正题，具体分析以上提到的每个工具的特点。当然除此之外，社区还有很多的方案，例如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Frushstack.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rushstack.io/" ref="nofollow noopener noreferrer">Rush Stack</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fteambit%2Fbit" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/teambit/bit" ref="nofollow noopener noreferrer">Bit</a> 等，因为时间和精力有限，就没有一一研究了。</p>
<h2 data-id="heading-2">Turborepo</h2>
<p>如果你知道 Turborepo 是由大名鼎鼎的 Vercel 团队开源，你就知道这个工具不简单。先看它官方的介绍：</p>
<blockquote>
<p>Turborepo is a <strong>high-performance build system</strong> for JavaScript and TypeScript codebases.</p>
</blockquote>
<p>划重点：<strong>high-performance build system，</strong> 从这几个关键词中，我们能感受到它的定位是高性能的构建系统。</p>
<p>我们知道，将多个项目集中管理起来的一个很大的弊端就是：<strong>当我们的项目 codebase 越来越庞大，那么项目的工作流——lint、构建、单元测试、集成测试也会越来越慢。</strong> 而 Turborepo 这样的工具，就是专门针对这样的场景进行极致的性能优化。</p>
<p>那么 Turborepo 是怎么优化的了？核心的优化思路从两个方向：</p>
<ol>
<li><strong>Multiple Running Task，在执行 workspace 的 build 等 task 的时候，尽量做到并行，而且提供配置的方式让你可以声明 task 之间的依赖关系；</strong></li>
<li><strong>Cache 和 Remote Cache，软件性能优化离不开缓存；</strong></li>
</ol>
<p>我们展开聊聊。</p>
<h3 data-id="heading-3"><strong>Multiple</strong> Running Task</h3>
<p>假设我们现在有一个 monorepo 的项目，有以下几个 package：</p>
<ul>
<li>apps/web，依赖 shared</li>
<li>apps/docs，依赖 shared</li>
<li>package/shared，被 web 和 docs 依赖</li>
</ul>
<p>当我们使用正常的 yarn workspace 去管理 monorepo 的工作流任务时，例如执行以下命令：</p>
<pre><code class="hljs language-arduino copyable" lang="arduino">yarn workspaces run lint
yarn workspaces run test
yarn workspaces run build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后每个项目之间的任务执行进度就是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56ec6b5322c64c76b456ea389c222684~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这种运行工作流的方式在于，首先必须跑完所有的 lint task，然后再到 shared build task ，接着才是 web 和 docs 的 build task，最后运行完 test task 才算结束，这也是我们目前大多数项目在 CI 里面的 job 流水线的真实写照。<strong>随着项目 codebase 和数量膨胀，所有工作流也会越来越慢</strong>。</p>
<p>为了解决这个问题，Turborepo 做了如下优化。首先，它允许你在 <code>turbo.json</code>中声明 task 之间的依赖关系：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">&#123;
  <span class="hljs-string">"<span class="hljs-variable">$schema</span>"</span>: <span class="hljs-string">"https://turborepo.org/schema.json"</span>,
  <span class="hljs-string">"pipeline"</span>: &#123;
    <span class="hljs-string">"build"</span>: &#123;
      <span class="hljs-comment">// ^build means build must be run in dependencies</span>
      <span class="hljs-comment">// before it can be run in this workspace</span>
      <span class="hljs-string">"dependsOn"</span>: [<span class="hljs-string">"^build"</span>]
    &#125;,
    <span class="hljs-string">"test"</span>: &#123;
      <span class="hljs-string">"outputs"</span>: [],
    &#125;,
    <span class="hljs-string">"lint"</span>: &#123;
      <span class="hljs-string">"outputs"</span>: []
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 turbo（Turborepo 的 cli 工具） 执行 <code>script</code>：</p>
<pre><code class="hljs language-arduino copyable" lang="arduino">turbo run lint test build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后工作流任务运行的效果是：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39e7fceb78ba45cb90e8e6148a5429cd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>你会发现，所有的任务是以并行的方式运行，大大提高了效率。</p>
<p>当然，在很多场景下，项目之间的工作流是会有依赖关系的，例如一般 test 可能依赖 build，deploy 依赖 test 和 build，所以我们可以在 <code>turbo.json</code>中这样配置：\</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">&#123;
  <span class="hljs-string">"<span class="hljs-variable">$schema</span>"</span>: <span class="hljs-string">"https://turborepo.org/schema.json"</span>,
  <span class="hljs-string">"pipeline"</span>: &#123;
    <span class="hljs-comment">// Standard configuration</span>
    <span class="hljs-string">"build"</span>: &#123;
      <span class="hljs-string">"dependsOn"</span>: [<span class="hljs-string">"^build"</span>]
    &#125;,
    <span class="hljs-string">"test"</span>: &#123;
      <span class="hljs-string">"dependsOn"</span>: [<span class="hljs-string">"^build"</span>],
      <span class="hljs-string">"outputs"</span>: [],
    &#125;,
    <span class="hljs-string">"deploy"</span>: &#123;
      <span class="hljs-string">"dependsOn"</span>: [<span class="hljs-string">"test"</span>, <span class="hljs-string">"build"</span>],
      <span class="hljs-string">"outputs"</span>: []
    &#125;,
 
    <span class="hljs-comment">// Explicit workspace-task to workspace-task dependency</span>
    <span class="hljs-string">"frontend#deploy"</span>: &#123;
      <span class="hljs-string">"dependsOn"</span>: [<span class="hljs-string">"ui#test"</span>, <span class="hljs-string">"backend#deploy"</span>, <span class="hljs-string">"backend#health-check"</span>],
      <span class="hljs-string">"outputs"</span>: []
    &#125;,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总的来说，Turborepo 通过这种配置方式来声明 task 之间的关系，除了在运行性能有不错的提升之外，开发者也可以从配置中了解到工作流之间的依赖关系。</p>
<h3 data-id="heading-4">Cache 和 Remote Cache</h3>
<p>在每个项目的工作流任务中，一般都是由输入和输出的产物，Turborepo 就可以利用这一点进行 task 运行结果缓存：</p>
<ul>
<li>对于 build，source files 就是输入，构建的产物就是输出；</li>
<li>对于 lint 和 test，source files 就是输入，而输出的 log 可以看做是输出。</li>
</ul>
<p>当你执行 <code>trubo run build</code>，Turborepo 默认会生成缓存文件，第一次构建没有缓存的效果是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6785cc80a9704780b418be6a512d7e8c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第一次 build task 成功生成了 cache，存放在 <code>node_modules/.cache/turbo/*</code>目录下。当我们下一次再次运行 build 任务，如果命中缓存，并消费：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ed59f21c895461284a476939c4e6ae8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图所示，当前 build hash 如果在 turbo 缓存目录下存在，则表示缓存命中。</p>
<p>hash 是 Turborepo 综合项目的 source files、环境变量、工作区的 source file 等经过一些算法计算而来，想了解更多，可以点击：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fturborepo.org%2Fdocs%2Fcore-concepts%2Fcaching%23hashing" target="_blank" rel="nofollow noopener noreferrer" title="https://turborepo.org/docs/core-concepts/caching#hashing" ref="nofollow noopener noreferrer">hashing</a>。</p>
<p>当然，你可以通过配置告诉 Turborepo 缓存需要关注的输入和输出：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">&#123;
  <span class="hljs-string">"<span class="hljs-variable">$schema</span>"</span>: <span class="hljs-string">"https://turborepo.org/schema.json"</span>,
  <span class="hljs-string">"pipeline"</span>: &#123;
    <span class="hljs-string">"build"</span>: &#123;
      <span class="hljs-string">"outputs"</span>: [<span class="hljs-string">"dist/**"</span>, <span class="hljs-string">".next/**"</span>],
      <span class="hljs-string">"dependsOn"</span>: [<span class="hljs-string">"^build"</span>]
    &#125;,
    <span class="hljs-string">"test"</span>: &#123;
      <span class="hljs-string">"outputs"</span>: [], <span class="hljs-comment">// leave empty to only cache logs</span>
      <span class="hljs-string">"dependsOn"</span>: [<span class="hljs-string">"build"</span>],
      <span class="hljs-string">"inputs"</span>: [<span class="hljs-string">"src/**/*.tsx"</span>, <span class="hljs-string">"src/**/*.ts"</span>, <span class="hljs-string">"test/**/*.ts"</span>]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于本地开发和构建，Turborepo 的缓存已经非常强大。但是，如果把格局放大，如果你<strong>想要在 CI 中或者团队的人共享这份缓存了</strong>，所以这就是 Remote cache 的由来。</p>
<p>我们看一张图，在没有 Remote cache 之前：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90bb55f59af54fe8a3ace01dada77a6a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们发现，每个人本地去运行一些 task，那么这个缓存只有在开发者个人的电脑上才能享受到。</p>
<p>使用 Remote cache：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a66418ad89f247089204a8cd39ad0b72~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>很简单，把每次构建的缓存丢到云端，然后在下次构建的时候从云端拉取即可，这样就可保证每台机器都能享受到每次 task 运行产生的缓存，提高开发效率。</p>
<h3 data-id="heading-5">小结</h3>
<p>Vercel 团队的技术水平毋庸置疑，所以造出来的工具使用场景格局也是非常大。我个人感觉 Turborepo 的定位更像是服务企业级工程项目，这样的 monorepo 项目无论是包数量和 codebase 的量都是非常大，那么无不避免就会遇到运行 task 地效率低的问题。</p>
<p>而对于一般的 monorepo 项目，例如我最近开发的 cli 工具，<strong>痛点在工具的使用成本、工作流（bump version、生成 changelog 等）是否完善等</strong>。所以使用 Turborepo 对我来说有点杀鸡用牛刀的感觉，而且我还需要配合 Turborepo 定制一套自己的发版工作流，所以一看就不是我想要的菜。</p>
<h2 data-id="heading-6">Nx</h2>
<p>官方是这样介绍 Nx 的：</p>
<p>Nx is a smart, fast and extensible build system with first class monorepo support and powerful integrations.</p>
<p>Nx 是一个以支持 monorepo 优先，小巧、快速、可扩展的构建系统和强大的集成。</p>
<p>在我看完了它的文档后，我也不明白它哪里 small，功能非常的多，而且使用方式随着不同的技术栈或者 JS 运行环境都会不同。然后我看了差不多一个小时文档，才搞懂怎么去初始化一个 TypeScript 工程。那一刻，我就明白这肯定不是我想要的工具。吐槽归吐槽，我们还是客观地分析下它的优点。</p>
<p>它的卖点在于：</p>
<ul>
<li><strong>可扩展性强</strong>，通过插件的方式可以定制你自己的 code generator 和 task executor；</li>
<li><strong>Task Cache</strong> ，跟 Turborepo 差不多，也是可以缓存你每次运行 task 的结果；</li>
<li><strong>Distribute Task Execution，</strong> 支持通过分布式架构方式运行你的任务（格局打开）</li>
</ul>
<h3 data-id="heading-7">扩展性</h3>
<p>首先我们来了解下什么是 code generator，在 nx 的 cli 中，它支持一个命令，例如：</p>
<pre><code class="hljs language-ini copyable" lang="ini">nx generate @nrwl/react:component mycmp <span class="hljs-attr">--project</span>=myapp
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行这行命令会帮你创建一个以 myapp 命名地 monorepo 项目，下面还会帮你创建一个基于 <code>@nrwl/react:component</code>code generator 生成的 package：mycmp。</p>
<p>所以，通俗理解下 code generator 其实类似 create-react-app 中的模板。也就是，你可以在 Nx 中定制你自己的项目模板。</p>
<p>那么 task executor 又是什么？</p>
<p>回答该问题之前，我们先来看一份 <code>nx.json</code>配置：</p>
<pre><code class="hljs language-perl copyable" lang="perl">&#123;
  <span class="hljs-string">"root"</span>: <span class="hljs-string">"apps/cart"</span>,
  <span class="hljs-string">"sourceRoot"</span>: <span class="hljs-string">"apps/cart/src"</span>,
  <span class="hljs-string">"projectType"</span>: <span class="hljs-string">"application"</span>,
  <span class="hljs-string">"generators"</span>: &#123;&#125;,
  <span class="hljs-string">"targets"</span>: &#123;
    <span class="hljs-string">"build"</span>: &#123;
      <span class="hljs-string">"executor"</span>: <span class="hljs-string">"@nrwl/web:webpack"</span>,
      <span class="hljs-string">"options"</span>: &#123;
        <span class="hljs-string">"outputPath"</span>: <span class="hljs-string">"dist/apps/cart"</span>,
        ...
      &#125;,
      <span class="hljs-string">"configurations"</span>: &#123;
        <span class="hljs-string">"production"</span>: &#123;
          <span class="hljs-string">"sourceMap"</span>: false,
          ...
        &#125;
      &#125;
    &#125;,
    <span class="hljs-string">"test"</span>: &#123;
      <span class="hljs-string">"executor"</span>: <span class="hljs-string">"@nrwl/jest:jest"</span>,
      <span class="hljs-string">"options"</span>: &#123;
        ...
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在如上配置中，我们发现 <code>targets</code>中的 <code>build</code>和 <code>test</code>声明了不同的 <code>executor</code>，Nx 这里的 <code>targets</code>其实就相当于 Turborepo 中的 task ，而所谓的 <code>executor</code> 就是执行某个 task 用到的工具，在上面的配置中例如 build 使用的是 webpack，test 使用的是 jest。</p>
<p>Nx 允许你定制自己的 executor，确实非常灵活，<strong>但是灵活也带来学习和上手成本</strong>。</p>
<h3 data-id="heading-8">Task Cache</h3>
<p>Nx 也会在每次运行完 task 后，对产物进行缓存。通过如下配置，声明你需要缓存的 task：</p>
<pre><code class="hljs language-scss copyable" lang="scss">&#123;
  "tasksRunnerOptions": &#123;
    "default": &#123;
      "runner": <span class="hljs-string">"nx/tasks-runners/default"</span>,
      <span class="hljs-string">"options"</span>: &#123;
        "cacheableOperations": [<span class="hljs-string">"build"</span>, <span class="hljs-string">"test"</span>]
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Nx 默认开启本地缓存，然后一周后就会清除缓存。</p>
<p>Nx 缓存跟 Turborepo 类似，也是会根据 source files、配置、运行环境的Node 版本等计算出一个 hash，然后下次运行 task 时匹配 hash 来决定缓存是否命中，可以通过下面的图详细了解 Nx 缓存运作原理：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3df37f8127e34b5fa2ef2db2848d3b80~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Nx 的缓存非常强大，<strong>所以需要保证你需要缓存的 task 是没有副作用的</strong>。例如一些 e2e 测试，会依赖后端 API 服务，这是有副作用的，如果使用了缓存，可能会导致 e2e 的结果不符合预期。</p>
<h3 data-id="heading-9">Distribute Task Execution</h3>
<p>能在一个前端工具中看到分布式的概念，谁还敢嘲讽前端就是写写页面（🐶）。没错，这个分布式，就是计算机中的分布式概念，可能我们经常平时听到的有<strong>分布式数据库、分布式计算</strong>等，跟前端都没半毛钱关系。</p>
<p>Nx 支持你配置在多台机器上运行你的任务，你可以使用批处理或者分箱的方式手动设置，或者你可以直接用官方的 Nx Cloud。</p>
<p>使用分布式的方式在 CI 运行你的任务，分为两步：</p>
<p>第一，主任务流如下：</p>
<pre><code class="hljs language-ini copyable" lang="ini"><span class="hljs-comment"># Coordinate the agents to run the tasks</span>
- npx nx-cloud start-ci-run
<span class="hljs-comment"># Run any commands you want here</span>
- nx affected <span class="hljs-attr">--target</span>=lint
- nx affected <span class="hljs-attr">--target</span>=test
- nx affected <span class="hljs-attr">--target</span>=build
<span class="hljs-comment"># Stop any run away agents</span>
- npx nx-cloud stop-all-agents
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二，代理的任务流：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># Wait for tasks to execute</span>
- npx nx-cloud start-agent
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用一张图表示如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74c24e49ae9b45728ca581021144f4e7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>想要了解更多，可以访问以下博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.nrwl.io%2Fdistributing-ci-binning-and-distributed-task-execution-632fe31a8953" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.nrwl.io/distributing-ci-binning-and-distributed-task-execution-632fe31a8953" ref="nofollow noopener noreferrer">Distributing CI: Binning and Distributed Task Execution</a>。不得不说，在前端工具中引入分布式的概念还是非常超前的。</p>
<h3 data-id="heading-10">小结</h3>
<p>总体来说，Nx 的设计理念和背后的团队还是非常超前和强大的。但是个人感觉，对于一般的开发来说，上手成本有点高。其次，大多数卖点也不是我需要的，而且其扩展性和强大的分布式执行任务的功能感觉也更多是面向需要深度定制需求的场景。</p>
<p>这里引入一个小插曲，其实 Nx 团队就是接手和维护 lerna@5 的团队，他们也是在 lerna 的 task 运行中引入了 Nx，所以 lerna@5 运行 task 的效率还是有不错的提升。</p>
<h2 data-id="heading-11">为什么是 Build System</h2>
<p>上面我们详细介绍了 Turborepo 和 Nx 的一些优点以及背后的一些设计理念，对比之后我们可以发现它们有一些共同点：</p>
<ul>
<li><strong>定位都是 build system；</strong></li>
<li><strong>适用于管理 monorepo 项目，甚至以 monorepo 优先；</strong></li>
<li><strong>追求项目 task 运行的性能。</strong></li>
</ul>
<p>什么是 <strong>build system</strong>？在软件开发中，<strong>构建一般指的是将源码转换成能被机器认识的二进制可执行文件。</strong> 如果在单个项目中，例如一个使用 TypeScript 为语言开发的项目，如果不考虑其它的问题（静态资源优化、JS 代码混淆等），构建的过程只需要使用 tsc 编译器将 TypeSceipt 编译成 JavaScript 即可。</p>
<p>但是在一个 monorepo 工程中，需要考虑的是不只是简单的将一个项目的代码编译成可以在浏览器端或者其它 JavaScript 运行时工具中运行的代码，还需要面临的问题：</p>
<ul>
<li><strong>构建流程复杂问题</strong>，为了保证工程的质量，可能真正构建生产代码，还有一些前置步骤，例如 lint、单元测试、集成测试等；</li>
<li><strong>构建效率问题</strong>，当你的 monorepo 项目不断膨胀，codebase 越来越庞大，构建效率自然会下降；</li>
<li><strong>自动化问题</strong>，实际上在大公司的开发流程中，大多数构建任务不是开发人员手动触发，而是在 CI 流程中自动触发；</li>
<li><strong>构建环境的一致性问题</strong>，当越来越多的人投入到一个 monorepo 工程中进行开发，开发者个人电脑上的环境千差万别，怎么保证所有开发者在构建流程中的环境是一致的是一个需要重视的问题。</li>
</ul>
<p>这个时候，你就需要一个 <strong>build system</strong> 来解决以上问题。</p>
<p>个人理解在当前的前端生态里面，在现有的编程语言例如 TypeScript 、现有的框架例如 React等开发模式下，我们去开发一个 Web 应用到能够在浏览器端运行都离不开<strong>构建</strong>，当然其中还包括静态资源的优化、JS 代码混淆、JS 新语法的转换等等。所以，为了更好地解决 monorepo 下的 task 管理以及构建 task 的运行效率，这类的工具应运而生。</p>
<p>而 monorepo 的工程管理方式，越来越符合当前的一些大型开源项目和企业级应用的工程架构需要，所以随之也会有越来越多的轮子诞生。除了 Turborepo 和 Nx 实际上例如像 Facebook 也有 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbuckbuild.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://buckbuild.com/" ref="nofollow noopener noreferrer">Buck</a> 、Google 也有 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbazel.build%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://bazel.build/" ref="nofollow noopener noreferrer">Bazel</a> 这样的适用 monorepo 的 build system。</p>
<p>因为 monorepo 把项目集中管理的工程架构方案，无可避免会导致 task 运行所带来地性能问题，所以才需要有像 Turborepo 的 <strong>Multiple Running Task</strong> 和 <strong>Remote cache</strong> 以及 Nx 的 <strong>Distribute Task Execution</strong> 这样的功能来解决构建性能瓶颈问题。</p>
<h2 data-id="heading-12">预告</h2>
<p>因为篇幅问题，本文暂时先介绍了 Turborepo 和 Nx，后续的文章会继续介绍以下工具：</p>
<ul>
<li>lerna@5；</li>
<li>pnpm + changeset；</li>
</ul>
<p>最后总结，我到底应该选择了什么样的方案，以及对大家选择 monorepo 的工具有哪些启发。</p></div>  
</div>
            