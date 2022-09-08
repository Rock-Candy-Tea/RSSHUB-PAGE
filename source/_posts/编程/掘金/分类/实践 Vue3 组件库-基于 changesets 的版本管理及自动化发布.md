
---
title: '实践 Vue3 组件库-基于 changesets 的版本管理及自动化发布'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/372c0ced7b3249399220aeb788a69903~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 06:09:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/372c0ced7b3249399220aeb788a69903~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第1文章，点击查看活动详情”</p>
<p>本系列已接近尾声，本篇是主要部分的最后一篇。再有其它也都是扩展性的内容。接下来看如何发布组件库和管理更新日志。本篇新增的完整代码可查看单独的分支 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbfehub%2Fvlib-starter%2Ftree%2F9-publish" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/bfehub/vlib-starter/tree/9-publish" ref="nofollow noopener noreferrer">9-publish</a>。</p>
<blockquote>
<p>如果你还不了解这个系列要做什么，那你可以先阅读 <a href="https://juejin.cn/post/7136467262826872868" target="_blank" title="https://juejin.cn/post/7136467262826872868">【实践 Vue3 组件库-介绍一下这个系列】</a> 的介绍，以便你对整个系列有清晰的认识。</p>
</blockquote>
<h2 data-id="heading-0">使用流程及概念</h2>
<p>什么是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchangesets%2Fchangesets" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/changesets/changesets" ref="nofollow noopener noreferrer">changesets</a>？根据官网的介绍 changesets 是用于管理版本及变更日志的工具，专注多包管理。</p>
<h3 data-id="heading-1">安装及初始化(init)</h3>
<p>现在先安装它到项目中。</p>
<pre><code class="hljs language-sh copyable" lang="sh">pnpm add @changesets/cli -w -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>pnpm changeset init</code> 初始化，会看到项目中生成了一个 <code>.changeset</code> 的文件夹，里面会生成 <code>config.json</code> 文件。生成的是默认配置一般不用做过多更改，你可以查看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchangesets%2Fchangesets%2Fblob%2Fmain%2Fdocs%2Fconfig-file-options.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/changesets/changesets/blob/main/docs/config-file-options.md" ref="nofollow noopener noreferrer">config-file-options</a> 的具体描述。</p>
<pre><code class="hljs language-sh copyable" lang="sh">pnpm changeset init
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/372c0ced7b3249399220aeb788a69903~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">生成 changeset 文件(add)</h3>
<p>什么是 changeset 文件(带疑问)？执行 <code>pnpm changeset add</code> 命令(add 可省略)，会弹出一些询问窗口。</p>
<pre><code class="hljs language-sh copyable" lang="sh">pnpm changeset add
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>
<p>哪些包是需要发布的？(有修改的和未修改的包会分开列出)</p>
</li>
<li>
<p>发布包的版本是什么？(遵循 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsemver.org%2Flang%2Fzh-CN%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://semver.org/lang/zh-CN/" ref="nofollow noopener noreferrer">semver</a> 规范)。</p>
</li>
<li>
<p>以及此次变更的描述？(后续根据它生成 changelog 内容)。</p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac8ee260fbde4924abd80b2c826e2382~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>全部选择完毕后会在 <code>.changeset</code> 目录下生成一个文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5586915c06b842469c333124936a0dfd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个文件就是 <code>changeset</code> 文件，可以看到里面的内容，就是我们刚才选择的。所以 <code>changeset</code> 文件是什么呢，就是记录此次更新的信息(包名称、包版本更新级别、CHANGELOG 信息) 的文件。</p>
<p>如果想把这些变更攒一攒，现在就可以把 changeset 文件提交了。每当开发了一个新功能或修复了一个问题并且想要记录在 changelog 中都需要生成一个 changeset 文件。</p>
<h3 data-id="heading-3">消耗 changeset 文件(version)</h3>
<p>现在已经有了一些 changeset 文件，那么如何使用它。执行 <code>pnpm changeset version</code> 命令来消耗 changeset 文件并且修改对应包版本以及依赖该包的包版本，同时会根据之前 changeset 文件里面的信息来生成对应的 CHANGELOG 信息。</p>
<pre><code class="hljs language-sh copyable" lang="sh">pnpm changeset version
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14cf2bfab95d4804b87ba5e1e6c88476~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">完善 changelog 信息(changelog-github)</h3>
<p>现在生成的 changelog 有点简单，我们可能想加一些哪次提交的、提交人是谁、关联 PR 等。</p>
<pre><code class="hljs language-sh copyable" lang="sh">pnpm add @changesets/changelog-github -w -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>config.json</code> 文件的 <code>changelog</code> 配置。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// .changeset/config.json</span>
<span class="hljs-punctuation">&#123;</span>
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">"changelog"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
    <span class="hljs-string">"@changesets/changelog-github"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-punctuation">&#123;</span>
      <span class="hljs-comment">// 这个是 github 上的包路径</span>
      <span class="hljs-attr">"repo"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"bfehub/vlib-starter"</span>
    <span class="hljs-punctuation">&#125;</span>
  <span class="hljs-punctuation">]</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看名称就知道它是从 github 上获取信息的，所以我们还需要做两步：</p>
<ol>
<li>
<p>把 changeset 文件提交到 github 上。</p>
</li>
<li>
<p>生成 github 的 <code>Access Token</code> 用于调用 github 的 api 接口。</p>
</li>
</ol>
<p>点击此地址 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsettings%2Ftokens%2Fnew" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/settings/tokens/new" ref="nofollow noopener noreferrer">github.com/settings/to…</a> 生成 token，起个名字选择时间就可以了，其他可以不用选。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2845e1ec747343988a4357e5aab23c03~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后把它设置为临时环境变量，后续自动化发布会自动鉴权不需要这个。如果你想手动发布就写入的系统的环境变量里。</p>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-comment"># win</span>
<span class="hljs-built_in">set</span> GITHUB_TOKEN=Your Yoken

<span class="hljs-comment"># mac</span>
<span class="hljs-built_in">export</span> GITHUB_TOKEN=Your Yoken
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时执行 <code>pnpm changeset version</code> 消耗 changeset 文件，可以看到内容变详细了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9532353352c44f3d966b931b11eb0c1c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">发布包版本(publish)</h3>
<p>终于到了激动人心的时刻，把组件库发布出去。在这之前修改下 <code>package.json</code> 中的必要字段内容，更多字段可以阅读 <a href="https://juejin.cn/post/7023539063424548872" target="_blank" title="https://juejin.cn/post/7023539063424548872">这篇文章</a> 了解更多。</p>
<p>只发布打包的产物文件。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// packages/vlib-ui/package.json</span>
<span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"files"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"es"</span><span class="hljs-punctuation">,</span> <span class="hljs-string">"lib"</span><span class="hljs-punctuation">,</span> <span class="hljs-string">"dist"</span><span class="hljs-punctuation">,</span> <span class="hljs-string">"global.d.ts"</span><span class="hljs-punctuation">]</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>命名空间的包必须指定 public 才能发布公开包。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// packages/vlib-ui/package.json</span>
<span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"publishConfig"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"access"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"public"</span>
  <span class="hljs-punctuation">&#125;</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在发包之前需要保证测试、打包完成，这里可以合并成一个命令。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// package.json</span>
<span class="hljs-comment">// --recursive 执行所有的子包中的命令</span>
<span class="hljs-comment">// --stream 输出中添加包的目录前缀</span>
<span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"release"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"pnpm --recursive --stream build && changeset publish"</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>pnpm release</code> 发布。前提是你得登录 npm 的账号，没登录过的请自行搜索。</p>
<blockquote>
<p>如果你是测试的，发布之后没用可以立即删除掉，维护生态环境人人有责。</p>
</blockquote>
<pre><code class="hljs language-sh copyable" lang="sh">pnpm release
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef7de93bcffd4c8ca6b75de65c63ad77~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/679fc7df479b4325b105df26e70a6365~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">工作流程示意</h3>
<p>上面的流程我简单的画了个图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00af468e07534bb18fffeecd3f681758~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="8.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">实现自动化发布</h2>
<p>我们利用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.github.com%2Fen%2Factions" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.github.com/en/actions" ref="nofollow noopener noreferrer">GitHub Actions</a> 来实现自动化发布。如果你完全不知道这个是什么，你可以阅读<a href="https://juejin.cn/post/7113562222852309023" target="_blank" title="https://juejin.cn/post/7113562222852309023">这篇文章</a>的基础部分。</p>
<p>自动化发布流程是由 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchangesets%2Faction" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/changesets/action" ref="nofollow noopener noreferrer">changesets/action</a> 实现，先了解下它的工作方式是什么。</p>
<ol>
<li>
<p>如果我们有新的 changeset 文件提交，它会自动执行 <code>changeset version</code> 命令。</p>
</li>
<li>
<p>如果有变更会创建一个发布用的 PR，每当 changeset 文件有变更都会更新这个 PR 的内容。</p>
</li>
<li>
<p>当我们合并这个 PR 时，此时包版本和 Npm 上的包版本不一致就会执行 <code>publish</code> 配置。</p>
</li>
</ol>
<h3 data-id="heading-8">编写发布流程</h3>
<p>在项目下 <code>.github/workflows</code> 文件中新建 <code>release.yml</code> 文件，当符合条件时 Actions 会自动运行它。</p>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-comment"># https://docs.github.com/en/actions/using-workflows/about-workflows</span>
<span class="hljs-comment"># 整个工作流的名称</span>
<span class="hljs-attr">name:</span> <span class="hljs-string">Release</span>

<span class="hljs-comment"># 监听 main 分支的 push 事件(有更新时)</span>
<span class="hljs-attr">on:</span>
  <span class="hljs-attr">push:</span>
    <span class="hljs-attr">branches:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">main</span>

<span class="hljs-comment"># 所有的 jobs</span>
<span class="hljs-attr">jobs:</span>
  <span class="hljs-comment"># 定义一个名为 release 的 job</span>
  <span class="hljs-attr">release:</span>
    <span class="hljs-comment"># 运行环境</span>
    <span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-latest</span>
    <span class="hljs-comment"># 定义步骤</span>
    <span class="hljs-attr">steps:</span>
      <span class="hljs-comment"># https://github.com/actions/checkout</span>
      <span class="hljs-comment"># 拉取代码</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Checkout</span> <span class="hljs-string">Repo</span>
        <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/checkout@v2</span>

      <span class="hljs-comment"># https://github.com/actions/setup-node</span>
      <span class="hljs-comment"># 安装 node</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Setup</span> <span class="hljs-string">Node.js</span>
        <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/setup-node@v3</span>
        <span class="hljs-attr">with:</span>
          <span class="hljs-attr">node-version:</span> <span class="hljs-number">16.</span><span class="hljs-string">x</span>

      <span class="hljs-comment"># https://github.com/pnpm/action-setup</span>
      <span class="hljs-comment"># 安装 pnpm</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Setup</span> <span class="hljs-string">Pnpm</span>
        <span class="hljs-attr">uses:</span> <span class="hljs-string">pnpm/action-setup@v2</span>
        <span class="hljs-attr">with:</span>
          <span class="hljs-attr">version:</span> <span class="hljs-number">7.</span><span class="hljs-string">x</span>

      <span class="hljs-comment"># https://pnpm.io/zh/cli/install#--frozen-lockfile</span>
      <span class="hljs-comment"># 下载依赖</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Install</span> <span class="hljs-string">Dependencies</span>
        <span class="hljs-attr">run:</span> <span class="hljs-string">pnpm</span> <span class="hljs-string">install</span> <span class="hljs-string">--frozen-lockfile</span>

      <span class="hljs-comment"># https://github.com/changesets/action</span>
      <span class="hljs-comment"># 自动创建发布 PR 或 发布 npm</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Create</span> <span class="hljs-string">Release</span> <span class="hljs-string">Pull</span> <span class="hljs-string">Request</span> <span class="hljs-string">or</span> <span class="hljs-string">Publish</span> <span class="hljs-string">to</span> <span class="hljs-string">npm</span>
        <span class="hljs-attr">uses:</span> <span class="hljs-string">changesets/action@v1</span>
        <span class="hljs-comment"># 参数配置</span>
        <span class="hljs-attr">with:</span>
          <span class="hljs-comment"># 发布时执行什么命令</span>
          <span class="hljs-attr">publish:</span> <span class="hljs-string">pnpm</span> <span class="hljs-string">release</span>
          <span class="hljs-comment"># 消耗 changeset 文件的命令；不需要自定义可不填</span>
          <span class="hljs-attr">version:</span> <span class="hljs-string">pnpm</span> <span class="hljs-string">changeset</span> <span class="hljs-string">version</span>
          <span class="hljs-comment"># 提交的信息是什么；如果有 commitlint 验证，需要更改。</span>
          <span class="hljs-attr">commit:</span> <span class="hljs-string">"chore: version packages"</span>
        <span class="hljs-comment"># 此步骤的环境变量，下一步讲解</span>
        <span class="hljs-attr">env:</span>
          <span class="hljs-attr">NPM_TOKEN:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.NPM_TOKEN</span> <span class="hljs-string">&#125;&#125;</span>
          <span class="hljs-attr">GITHUB_TOKEN:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.GITHUB_TOKEN</span> <span class="hljs-string">&#125;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">获取发布权限</h3>
<p>在上面的配置中有两个 <code>NPM_TOKEN</code> 和 <code>GITHUB_TOKEN</code> 变量看怎么去获取。</p>
<p>其中 <code>GITHUB_TOKEN</code> 不用配置，这使用的 Actions 内置的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.github.com%2Fcn%2Factions%2Fsecurity-guides%2Fautomatic-token-authentication" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.github.com/cn/actions/security-guides/automatic-token-authentication" ref="nofollow noopener noreferrer">自动身份令牌认证</a>。</p>
<p>其中 <code>NPM_TOKEN</code> 需要从 Npm 账户中生成 <code>Access Token</code>，并配置到 Actions 中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07ce0ec7047c4f5989336361b6443b21~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择 <code>Automation</code> 类型，专门用于 <code>CI/CD</code> 的跳过 2FA 的验证(保存好只展现一次)。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0886a274f8a48c0ab7fb3784b40b8fe~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>添加到 <code>GitHub Actions secrets</code> 中，这里存放一些私密的变量什么的，可以在 Actions 中获取到。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed33a29482f449e794498cb92f869b0b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c583a1bbe8641d48afec5ffcb098c44~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">触发自动发布</h3>
<p>如果现在提交后，会发现不会自动创建 PR，这是因为没有新的 changeset 文件，现在创建一个新的。和之前步骤一样，使用 <code>pnpm changeset</code> 创建一个 changeset 文件并提交。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a25eca9b84f644bf8a6529cf9c417a7b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时再去看 Actions 中构建步骤的日志会触发 PR 请求。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4caa9165ed58462ca599292e4bd8d94b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>并且在 Pull Requests 中会多一个 PR 请求，并且描述了发布的包版本和变更日志，如果你一直不合并会一直更新。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/885898cd1b0846709aef59551db81666~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="15.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在去合并这个 PR 到 main 分支。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ab510ea093b4718abd8d8bd32373f49~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="16.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>合并完成后在看 Actions 中构建步骤的日志，已经执行了打包和发布。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8eefa78042c3473c95fcef1aaf2abe95~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在已经发布到 Npm 上了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05d3fef934754fd0a079b97a8581221b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，到此就自动化发布完成了。</p>
<h2 data-id="heading-11">你可以...</h2>
<ul>
<li>
<p>你可以根据本章内容自己实现一遍完善我们的组件库。</p>
</li>
<li>
<p>如果对你有帮助可以点个 <strong>赞</strong> 和 <strong>关注</strong> 以示鼓励。</p>
</li>
</ul></div>  
</div>
            