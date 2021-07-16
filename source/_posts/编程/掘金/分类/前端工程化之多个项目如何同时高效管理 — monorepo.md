
---
title: '前端工程化之多个项目如何同时高效管理 — monorepo'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18867ca9d91746e586210b798592a977~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 17:54:43 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18867ca9d91746e586210b798592a977~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>monorepo 不仅限于前端，但此篇博文只谈前端。</p>
</blockquote>
<h2 data-id="heading-0">是什么</h2>
<blockquote>
<p>wikipedia: In <a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FVersion_control" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Version_control" ref="nofollow noopener noreferrer">version control systems</a>, a <strong>monorepo</strong> ("<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wiktionary.org%2Fwiki%2Fmono-%23English" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wiktionary.org/wiki/mono-#English" ref="nofollow noopener noreferrer">mono</a>" meaning 'single' and "repo" being short for '<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FRepository_(version_control)" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Repository_(version_control)" ref="nofollow noopener noreferrer">repository</a>') is a software development strategy where code for many projects is stored in the same repository.</p>
</blockquote>
<p>翻译过来就是：在版本控制系统中，<strong>monorepo</strong> 是一种软件开发策略，其中许多项目的代码存储在同一存储库中。</p>
<h2 data-id="heading-1">为什么</h2>
<p>在公司内，如果项目较多，每一个项目都会有一个Git仓库，就会导致新来的员工每一次更改项目的时候都需要从 Git 仓库上面拉一份代码下来比较麻烦。</p>
<p>那如果将所有的项目放在一个仓库一起管理呢？这就是 monorepo。</p>
<h3 data-id="heading-2">优点</h3>
<ol>
<li>对依赖统一进行管理。</li>
<li>可以抽取逻辑维护公共库。</li>
<li>所有项目统一配置相同的工程配置。</li>
</ol>
<h3 data-id="heading-3">缺点</h3>
<ol>
<li>需要有比较严格的 CR 规范。</li>
<li>Git 权限管理难以控制。</li>
<li>版本控制比较麻烦</li>
</ol>
<blockquote>
<p>项目都需要规范的流程。</p>
</blockquote>
<h2 data-id="heading-4">怎么做</h2>
<p>目前来说，前端算是有两种比较常见的对 monorepo 的方案：</p>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Flerna.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://lerna.js.org/" ref="nofollow noopener noreferrer">lerna.js</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fclassic.yarnpkg.com%2Fen%2Fdocs%2Fworkspaces%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://classic.yarnpkg.com/en/docs/workspaces/" ref="nofollow noopener noreferrer">yarn workspace</a></li>
</ol>
<blockquote>
<p>当然，它们也可以同时使用。</p>
</blockquote>
<h3 data-id="heading-5">yarn workspaces</h3>
<p>它允许设置多个包，即只需运行一次 yarn 安装即可一次性安装所有包。</p>
<p>在<code>package.json</code>文件中添加以下内容</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"private"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">"workspaces"</span>: [<span class="hljs-string">"workspace-a"</span>, <span class="hljs-string">"workspace-b"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">禁止使用</h4>
<p>在 <code>.yarnrc</code> 文件中添加：</p>
<pre><code class="hljs language-bash copyable" lang="bash">workspaces-experimental <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">learn.js</h3>
<blockquote>
<p>Github 仓库在：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flerna%2Flerna" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lerna/lerna" ref="nofollow noopener noreferrer">github.com/lerna/lerna</a></p>
</blockquote>
<p>Lerna is a tool that optimizes the workflow around managing multi-package repositories with git and npm.</p>
<p>Lerna 是一个使用 git 和 npm 优化管理多包存储库的工作流程的工具。</p>
<p>需要注意的是：lerna 只是一个优化工作流程的工具，并不是一个部署工具。</p>
<h4 data-id="heading-8">安装</h4>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 新建一个项目</span>
mkdir lerna-demo && <span class="hljs-built_in">cd</span> lerna-demo

<span class="hljs-comment"># 初始化项目</span>
npm init -y

<span class="hljs-comment"># 安装 lerna</span>
yarn add lerna -D

<span class="hljs-comment"># 初始化 lerna 的项目</span>
npx lerna init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时一个最基本的 lerna 项目算是完成了。</p>
<p>(记得添加 .gitignore )</p>
<h4 data-id="heading-9">使用</h4>
<p>上述的命令完成之后，现在项目的文件目录：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18867ca9d91746e586210b798592a977~tplv-k3u1fbpfcp-watermark.image" alt="CleanShot 2021-06-26 at 15.26.21@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>更改一下 <code>package.json</code> 在其中加一个字段：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"private"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于我们管理的是子项目，一般不对父项目进行发布处理，所以将 <code>private</code> 设置为 <code>true</code>。</p>
<p>然后在 <code>packages</code> 目录中新建项目即可。</p>
<p>lerna 会自动检测到 packages 里面的项目进行管理。</p>
<blockquote>
<p><code>packages</code> 目录中的项目需要注意一件事情：</p>
<ul>
<li><code>package.json</code> 的 name 字段需要和文件夹的名称相同。</li>
</ul>
</blockquote>
<h4 data-id="heading-10">命令</h4>
<ul>
<li>lerna init: 初始化</li>
<li>learn list: 列出现在管理的项目</li>
<li>lerna diff: 列出最近一次 release 的区别</li>
<li>lerna change: 更改了哪些 package</li>
<li>lerna bootstrap: 安装依赖并且链接任何交叉依赖项</li>
<li>lerna clean: 清理所有依赖项</li>
<li>lerna exec: 在每个 package 执行命令</li>
<li>lerna run: 在包含 npm script 中的每个 package 执行 npm script</li>
<li>lerna import: 将 package 导入到具有提交历史记录的 monorepo 中</li>
<li>lerna link: 将相互依赖的所有 package 符号链接在一起</li>
</ul>
<h3 data-id="heading-11">同时使用</h3>
<p><code>lerna</code> 和 <code>yarn workspace</code> 可以同时使用</p>
<p>在 <code>lerna.json</code> 添加：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"packages"</span>: [
    <span class="hljs-string">"packages/*"</span>
  ],
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.0.0"</span>,
  <span class="hljs-attr">"npmClient"</span>: <span class="hljs-string">"yarn"</span>,
  <span class="hljs-attr">"useWorkspaces"</span>: <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 <code>package.json</code> 添加：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">"private"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">"workspaces"</span>: [
    <span class="hljs-string">"packages/*"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">区别</h4>
<p>在 <code>yarn workspace</code> 中有这么一段：</p>
<blockquote>
<p>Yarn’s workspaces are the low-level primitives that tools like Lerna can (and <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flerna%2Flerna%2Fpull%2F899" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lerna/lerna/pull/899" ref="nofollow noopener noreferrer">do</a>!) use. They will never try to support the high-level feature that Lerna offers, but by implementing the core logic of the resolution and linking steps inside Yarn itself we hope to enable new usages and improve performance.</p>
</blockquote>
<p>这个就是区别</p>
<h2 data-id="heading-13">参考</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMonorepo" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Monorepo" ref="nofollow noopener noreferrer">wikipedia Monorepo</a>: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMonorepo" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Monorepo" ref="nofollow noopener noreferrer">en.wikipedia.org/wiki/Monore…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fclassic.yarnpkg.com%2Fen%2Fdocs%2Fworkspaces%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://classic.yarnpkg.com/en/docs/workspaces/" ref="nofollow noopener noreferrer">yarn workspace</a>: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fclassic.yarnpkg.com%2Fen%2Fdocs%2Fworkspaces" target="_blank" rel="nofollow noopener noreferrer" title="https://classic.yarnpkg.com/en/docs/workspaces" ref="nofollow noopener noreferrer">classic.yarnpkg.com/en/docs/wor…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flerna%2Flerna" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lerna/lerna" ref="nofollow noopener noreferrer">lerna github</a>: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flerna%2Flerna" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lerna/lerna" ref="nofollow noopener noreferrer">github.com/lerna/lerna</a></p>
<br>
<br>
<p><em><strong>PS:大家看了后觉得对自己有帮助可以三连留言,欢迎提出宝贵意见，也欢迎各位对相关技术有兴趣的开发者（由团队开发人员微信号x118422邀请）入群，在线解答讨论数据可视化、优化图表性能等方面的技术问题~</strong></em></p></div>  
</div>
            