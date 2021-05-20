
---
title: '使用 pnpm 构建 Monorepo 项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/073737cd43d149998f87d2d391456d82~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 20 May 2021 03:13:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/073737cd43d149998f87d2d391456d82~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">monorepo 是什么</h2>
<p>monorepo 是把多个项目的所有代码放到一个 git 仓库中进行管理，多个项目中会有共享的代码则可以分包引用。整个项目就是有 root 管理的 dependencies 加上多个 packages，每个 package 也可以在自己的作用域引入自己的 dependencies。</p>
<p>项目结构如下：</p>
<pre><code class="copyable">.
├── node_modules
├── package.json
├── packages
│   ├── ui
│   ├── utils
│   └── web
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
├── readme.md
└── tsconfig.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>packages 文件夹中的就是原本每个独立的项目(下文称之为 package )了，现在放在一起用 workspace 去管理。最外层路径称之为 root。在 root package.json 中的 deps 是所有子 package 共用的。</p>
<h2 data-id="heading-1">pnpm 是什么</h2>
<blockquote>
<p>Fast, disk space efficient package manager</p>
</blockquote>
<p>pnpm 是新一代 node 包管理器。它由 npm/yarn 衍生而来，但却解决了 npm/yarn 内部潜在的 bug，并且极大了地优化了性能，扩展了使用场景。<sup id="user-content-fnref-1"><a href="https://juejin.cn/post/6964328103447363614#fn-1" class="footnote-ref">1</a></sup></p>
<p>pnpm 相比 yarn，npm，yarn PnP 安装包更快速，对包的依赖管理更偏平，对磁盘占用也有优势。</p>
<p>具体可以参考这篇文章：<a href="https://jishuin.proginn.com/p/763bfbd3bcff" target="_blank" rel="nofollow noopener noreferrer">为什么现在我更推荐 pnpm 而不是 npm/yarn?</a></p>
<h2 data-id="heading-2">为什么要使用 monorepo</h2>
<p>使用 monorepo 可以把原本一个项目的多个模块拆分成多个 packages，在 packages 之间相互引用，也可以单独发布成包，极大地解决了项目之间代码无法重用的痛点。在项目打包或者编译操作时也可重用一套配置，通吃所有 packages。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/073737cd43d149998f87d2d391456d82~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">开始</h2>
<p>首先需要安装 pnpm，就不用多说了。然后 init 一个项目。</p>
<p>在 root 目录新建 <code>pnpm-workspace.yaml</code>，内容如下</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">packages:</span>
  <span class="hljs-comment"># all packages in subdirs of packages/ and components/</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">'packages/**'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们所有的 packages 都放在 <code>packages</code> 目录下。</p>
<p>用 pnpm 安装全局共用的包，比如 react, react-dom。</p>
<pre><code class="hljs language-sh copyable" lang="sh">pnpm install react react-dom -w
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意这里使用 <code>-w</code> 表示把包安装在 root 下，该包会放置在 <code><root>/node_modules</code> 下。当然也可以把把安装在所有 packages 中，使用 <code>-r</code> 代替 <code>-w</code>。你必须使用其中一个参数。例如把 dayjs 装入 packages/web 下，packages/web 中的 package.json name 为 <code>@test/web</code>。需要执行：</p>
<pre><code class="hljs language-sh copyable" lang="sh">pnpm i dayjs -r --filter @<span class="hljs-built_in">test</span>/web
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>--filter</code> 后面接子 package 的 name 表示只把安装的新包装入这个 package 中。</p>
<hr>
<p>接下来，我们在 packages 中新建以下几个目录。</p>
<pre><code class="copyable">├── packages
│   ├── ui
│   ├── utils
│   └── web
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后每个都执行 <code>npm init</code> ，假设每个 package 的 name 依次为 <code>@test/ui</code> <code>@test/utils</code> <code>@test/web</code>。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// packages/utils</span>
&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"@test/utils"</span>, <span class="hljs-comment">// <-----</span>
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.ts"</span>,
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">"Innei"</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"MIT"</span>,
  <span class="hljs-attr">"dependencies"</span>: &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以 utils 为例，入口文件为 index.ts，首先建立这个文件。写入如下内容。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">number</span>, b: <span class="hljs-built_in">number</span></span>) =></span> a + b
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，执行</p>
<pre><code class="copyable">pnpm i @test/utils -r --filter @test/ui
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后，打开 <code>packages/ui/package.json</code> 发现 dependencies 中多了一行。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"@test/ui"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"./index.tsx"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;&#125;,
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">"Innei"</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"MIT"</span>,
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"@test/utils"</span>: <span class="hljs-string">"workspace:^1.0.0"</span> <span class="hljs-comment">// <--------</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于是 workspace 管理的，所有有一个前缀 workspace。接下来则可以从 package/ui 中直接引入这个包了。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123;add&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@test/utils'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，如果用 vscode ts server 提供的 auto import 会使用 relative path 引用。如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123;add&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../utils'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实只要用 vscode 打开这个文件夹，当成一个项目来写就行了。这也就暂时剥离 monorepo 这个概念了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/018a49b2e697447fadedba72537d5ea5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么接下来的 package/web 就是整个项目的整体了。放置原来项目中的所有 src 下的代码。而一些原本通用的代码就从 src 下提取成包放在了 packages 下了。这样就好理解了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/770913387a0c471aae5bbe3ea34ed3b0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Template: <a href="https://github.com/Innei" target="_blank" rel="nofollow noopener noreferrer">Innei</a>/<strong><a href="https://github.com/Innei/pnpm-workspace-monorepo" target="_blank" rel="nofollow noopener noreferrer">pnpm-workspace-monorepo</a></strong></p>
<div class="footnotes">
<hr>
<ol>
<li id="user-content-fn-1"><a href="https://jishuin.proginn.com/p/763bfbd3bcff" target="_blank" rel="nofollow noopener noreferrer">为什么现在我更推荐 pnpm 而不是 npm/yarn?</a><a href="https://juejin.cn/post/6964328103447363614#fnref-1" class="footnote-backref">↩</a></li>
</ol>
</div></div>  
</div>
            