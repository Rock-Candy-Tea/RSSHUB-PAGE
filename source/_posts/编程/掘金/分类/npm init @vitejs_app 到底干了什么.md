
---
title: 'npm init @vitejs_app 到底干了什么'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2556e2cab4c04aa194b2bdd0056bda3a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 16:19:33 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2556e2cab4c04aa194b2bdd0056bda3a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本篇文章来自团队小伙伴 <a href="https://juejin.cn/user/1926000099989709" target="_blank">@小明额额额</a> 的一次学习分享，希望跟大家分享与探讨。</p>
<p>求积硅步以致千里，勇于探享生活之美。</p>
</blockquote>
<p><img alt="npm init @vitejs/app 到底干了什么" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2556e2cab4c04aa194b2bdd0056bda3a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">背景</h3>
<p>最近在闲暇时间学习尤大大的新框架 ViteJs 的时候发现，创建一个新的基于 Vite 的项目时，使用的命令方式是：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm init @vitejs/app
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这跟我们熟悉的 CLI 创建 Vue 项目的命令完全不一样：</p>
<pre><code class="hljs language-shell copyable" lang="shell">vue create project-name
<span class="copy-code-btn">复制代码</span></code></pre>
<p>「在不安装脚手架工具的情况下，还能直接使用 npm 创建项目？」带着好奇心小小的探究了一下。</p>
<p>首先我们要知道这个命令 <code>npm init @vitejs/app</code> 是要做什么？</p>
<p>一番谷歌 + 官网文档，实际上这个命令就是要创建一个新的 Vite 项目，且基于某个模版，这个模版可以是 Vue / React 或其它。那么它到底是如何创建的？带着这个问题我们先来重温下 <code>npm init</code>。</p>
<h3 data-id="heading-1">复习 npm init</h3>
<p><code>npm init</code> 对于我们来说应该非常熟悉了，通常我们使用 <code>npm init</code> 初始化一个 package.json 文件来起手一个项目。大多数小伙伴只用到这，但是这个命令后面是可以携带参数的？这个参数能干什么呢？对于我这见惯大场面的 cv 程序员来说，翻手就是一个谷歌。谷歌大佬告诉我们 <a href="https://docs.npmjs.com/cli/v7/commands/npm-init" target="_blank" rel="nofollow noopener noreferrer">npm-init</a>：</p>
<blockquote>
<p><code>npm init <initializer></code> 通常被用于创建一个新的或者已经存在的 npm 包。</p>
</blockquote>
<p>initializer 在这里是一个名为 <code>create-<initializer></code> 的 npm 软件包，该软件包将由 npx 来安装，然后执行其 package.json 中 bin 属性对应的脚本，会创建或更新 package.json 并运行一些与初始化相关的操作。</p>
<p>官方说明也给出了命令相对应的一些示例：</p>





















<table><thead><tr><th>命令</th><th>等同</th></tr></thead><tbody><tr><td><code>npm init foo</code></td><td><code>npx create-foo</code></td></tr><tr><td><code>npm init @usr/foo</code></td><td><code>npx @usr/create-foo</code></td></tr><tr><td><code>npm init @usr</code></td><td><code>npx @usr/create</code></td></tr></tbody></table>
<p>文章开头的命令 <code>npm init @vitejs/app</code> 正好匹配到了第二条示例，对应起来应该是这样：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm init @vitejs/app -> npx @vitejs/create-app
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的解释可以看出，在命令行中运行 <code>npm init @vitejs/app</code>，实际上是通过了 npx 运行了名为 @vitejs/create-app 这个包，那么我们就去 Vite 官方仓库找一找有没有叫 create-app 的文件？</p>
<p>查看 <a href="https://github.com/vitejs/vite" target="_blank" rel="nofollow noopener noreferrer">ViteJs</a> 源码发现 packages 文件夹中确实存在一个 <a href="https://github.com/vitejs/vite/tree/main/packages/create-app" target="_blank" rel="nofollow noopener noreferrer">create-app</a> 目录，那我们就再深入的看看这个目录里面有什么？</p>
<p><img alt="create-app" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dda9a060026f4d56b720f93cb4322f34~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">@vitejs/create-app 项目做了什么?</h3>
<p>在 create-app 文件夹下的 package.json 中发现 bin 入口：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"@vitejs/create-app"</span>,
  <span class="hljs-comment">// ...没错了，就是这</span>
  <span class="hljs-attr">"bin"</span>: &#123;
    <span class="hljs-attr">"create-app"</span>: <span class="hljs-string">"index.js"</span>,
    <span class="hljs-attr">"cva"</span>: <span class="hljs-string">"index.js"</span>
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>bin 属性配置了 create-app 的执行入口文件 index.js ，那我们就去看看 index.js 中做了什么操作，源码过长，部分精简以便享用，感兴趣的小伙伴可深挖：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// https://github.com/vitejs/vite/blob/main/packages/create-app/index.js</span>

<span class="hljs-comment">// 省略非关键代码</span>
<span class="hljs-keyword">const</span> TEMPLATES = [
  yellow(<span class="hljs-string">'vanilla'</span>),
  green(<span class="hljs-string">'vue'</span>),
  green(<span class="hljs-string">'vue-ts'</span>),
  <span class="hljs-comment">//...</span>
]

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> targetDir = argv._[<span class="hljs-number">0</span>]
  <span class="hljs-keyword">if</span> (!targetDir) &#123;
    <span class="hljs-comment">// 第一步：确定用户录入的 Project name</span>
    <span class="hljs-keyword">const</span> &#123; name &#125; = <span class="hljs-keyword">await</span> prompt(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'name'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">`Project name:`</span>,
      <span class="hljs-attr">initial</span>: <span class="hljs-string">'vite-project'</span>
    &#125;)
    targetDir = name
  &#125;

  <span class="hljs-keyword">const</span> root = path.join(cwd, targetDir)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`\nScaffolding project in <span class="hljs-subst">$&#123;root&#125;</span>...`</span>)
  
  <span class="hljs-comment">// 第二步：检查是否存在同名目录且是否为空目录</span>
  <span class="hljs-keyword">if</span> (!fs.existsSync(root)) &#123;
    fs.mkdirSync(root, &#123; <span class="hljs-attr">recursive</span>: <span class="hljs-literal">true</span> &#125;)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">const</span> existing = fs.readdirSync(root)
    <span class="hljs-keyword">if</span> (existing.length) &#123;
        <span class="hljs-comment">//...</span>
    &#125;
  &#125;

  <span class="hljs-comment">// 第三步 校验并选择模版</span>
  <span class="hljs-keyword">let</span> template = argv.t || argv.template
  <span class="hljs-keyword">let</span> message = <span class="hljs-string">'Select a template:'</span>
  <span class="hljs-keyword">if</span> (!template || !isValidTemplate) &#123;
    <span class="hljs-keyword">const</span> &#123; t &#125; = <span class="hljs-keyword">await</span> prompt(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'select'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'t'</span>,
      message,
      <span class="hljs-attr">choices</span>: TEMPLATES
    &#125;)
    template = stripColors(t)
  &#125;

  <span class="hljs-keyword">const</span> templateDir = path.join(__dirname, <span class="hljs-string">`template-<span class="hljs-subst">$&#123;template&#125;</span>`</span>)

  <span class="hljs-keyword">const</span> write = <span class="hljs-function">(<span class="hljs-params">file, content</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> targetPath = renameFiles[file]
      ? path.join(root, renameFiles[file])
      : path.join(root, file)
    <span class="hljs-keyword">if</span> (content) &#123;
      fs.writeFileSync(targetPath, content)
    &#125; <span class="hljs-keyword">else</span> &#123;
      copy(path.join(templateDir, file), targetPath)
    &#125;
  &#125;
  <span class="hljs-comment">// 第四步：拷贝并写入文件</span>
  <span class="hljs-keyword">const</span> files = fs.readdirSync(templateDir)
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> file <span class="hljs-keyword">of</span> files.filter(<span class="hljs-function">(<span class="hljs-params">f</span>) =></span> f !== <span class="hljs-string">'package.json'</span>)) &#123;
    write(file)
  &#125;

  <span class="hljs-keyword">const</span> pkg = <span class="hljs-built_in">require</span>(path.join(templateDir, <span class="hljs-string">`package.json`</span>))

  <span class="hljs-comment">// 第五步：拷贝 package.json 提示安装运行</span>
  write(<span class="hljs-string">'package.json'</span>, <span class="hljs-built_in">JSON</span>.stringify(pkg, <span class="hljs-literal">null</span>, <span class="hljs-number">2</span>))
  <span class="hljs-comment">// ...提示 `npm install / npm run dev`</span>
&#125;

<span class="hljs-comment">// 省略功能函数...</span>
init().catch(<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.error(e)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码主要逻辑如下：</p>
<ul>
<li>第一步：确定 Project name ，用户输入或默认；</li>
<li>第二步：检查本地是否存在同名目录，并判断是否为空目录；</li>
<li>第三步：选择要创建的模板，vue、vue-ts、react 等；</li>
<li><strong>第四部（核心）：根据选择的模板匹配到项目下以 <code>template-</code> 开头的目录，将目录中的所有文件拷贝到本地项目目录中；</strong></li>
<li>第五步：拷贝修改完 name 的新 package.json 到新项目中，并提示安装依赖和运行；</li>
</ul>
<p>到此我们已经搞清楚 <code>npm init @vitejs/app</code> 背后是通过执行 create-app 中 bin 所指定的脚本文件。而这个脚本文件（这里是 index.js）所做的工作，就是根据一些配置和模版项目，利用 node 将所有模版文件拷贝到本地项目目录中，从而完成了一个根据模板创建项目的系列操作。</p>
<p>创建项目可用 CLI 脚手架，为何要如此大费周章呢？莫急且看。</p>
<h3 data-id="heading-3">npm init VS vue create</h3>
<p>我们使用 <code>vue create</code> 来创建项目时，背后是 Vue-CLI 给予我们的能力。所以我们得首先安装 Vue-Cli，然后才可以使用它来创建项目。而 <code>npm init</code> 则跳过了 CLI 这部分，它基于指定脚本来实现，所以与 <code>vue create</code> 对比，它的优点：</p>
<ul>
<li>项目即工具，更加简单直接；</li>
<li>不用安装额外的 CLI 工具，多一个工具就多一个使用成本；</li>
<li>更新方便，无需同时维护模板和 CLI 工具；</li>
</ul>
<p>所以，总的来说使用 <code>npm init</code> 创建项目更加简单和纯粹。</p>
<h3 data-id="heading-4">加深 package.json 认识</h3>
<p>不难发现，create-app 入口文件关键是 package.json 文件的 bin 属性，那么 bin 和 main 有什么区别呢？</p>













<table><thead><tr><th>main</th><th>bin</th></tr></thead><tbody><tr><td>属性是一个 module ID，是程序的主要的入口点，当然如果不设置，默认值就是 index.js</td><td>如果此 npm 包带有 bin 属性，那么此 npm 包的可执行文件就会被链接到当前项目的 ./node_modules/.bin 中，此后在命令行中就很方便的执行这个包，比如：node node_modules/.bin/myapp，更加详细的解释可参照 <a href="https://docs.npmjs.com/cli/v7/configuring-npm/package-json#bin" target="_blank" rel="nofollow noopener noreferrer">package.json bin</a></td></tr></tbody></table>
<p>不得不说，package.json 中每个属性都有它的用处，只有仔细的阅读和分析其的含义和用法，才会有创造轮子的那点灵光啊！</p>
<h3 data-id="heading-5">学完能做什么？</h3>
<p>公司新的项目层出不穷，目前项目还在做微前端的重构，微前端中的各个子模块都需要使用一个模板 <code>Ctrl + C</code> / <code>Ctrl + V</code> 来创建，虽然对于我们 cv 程序员来说是小 case，但是如果我们有了自己的 create-app，我们翻手一个 <code>npm init @company/app</code>，岂不更美哉？</p>
<p>不单如此，我们还可以建立公司内部或对外的模板库项目，将所有常用的模板项目维护到一个项目中，统一维护管理，岂不快哉？(坑已挖好，活已安排，下次一定）...</p>
<p>以上便是本次分享的全部内容，希望对你有所帮助 ^_^</p>
<p>喜欢的话别忘了动动手指，点赞、收藏、关注三连一波带走。</p>
<hr>
<h3 data-id="heading-6">关于我们</h3>
<p>我们是万拓科创前端团队，左手组件库，右手工具库，各种技术野蛮生长。</p>
<p>一个人跑得快，不如一群人跑得远。欢迎加入我们的小分队，牛年牛气轰轰往前冲。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            