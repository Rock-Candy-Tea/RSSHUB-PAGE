
---
title: 'lerna 快速入门'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/539db50b35f94fdcba42d0188c4fb93d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 24 May 2021 17:55:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/539db50b35f94fdcba42d0188c4fb93d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">multiRepo Vs monoRepo</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/539db50b35f94fdcba42d0188c4fb93d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">lerna 简介</h2>
<blockquote>
<p>Lerna是一个用来优化托管在 git\npm 上的多 package 代码库的工作流的一个管理工具,可以让你在主项目下管理多个子项目，从而解决了多个包互相依赖，且发布时需要手动维护多个包的问题</p>
</blockquote>
<ul>
<li>多仓库管理</li>
<li>多包管理</li>
<li>自动管理包依赖</li>
</ul>
<h2 data-id="heading-2">lerna 常用命令</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 安装</span>
npm i -g lerna

<span class="hljs-comment">// 创建目录</span>
mkdir lerna-repo && code lerna-repo

<span class="hljs-comment">// 初始化</span>
lerna init  <span class="hljs-comment">// 默认fixed，包版本号统一管理</span>
lerna init -i  <span class="hljs-comment">// 独立模式，包版本单独管理</span>

<span class="hljs-comment">// 启动项目（如果项目是从git下载的，而不是第一次新建）</span>
lerna bootstrap  <span class="hljs-comment">// 安装所有packages的依赖项并且连接本地包的交叉依赖项</span>
lerna bootstrap --hoist <span class="hljs-comment">// 将各包中相同的依赖提取到根 node_modules, 最好先lerna clean删除各包依赖</span>

<span class="hljs-comment">// 创建package</span>
<span class="hljs-comment">// 也可以在packages目录下手动创建</span>
lerna create <packageName> -y <span class="hljs-comment">// 通过lerna 快速创建</span>

<span class="hljs-comment">// 安装依赖</span>
<span class="hljs-comment">// 将本地或者远程的包作为依赖项添加到当前的packages中，每次只能添加一个包</span>
lerna add axios <span class="hljs-comment">// 如果使用 Workspaces，各个包都安装一遍</span>
lerna add axios --scope=<package-name> <span class="hljs-comment">// 安装到指定的包中，--scope 指定需要安装的包名</span>

<span class="hljs-comment">// 删除所有包下面的node_modules目录，也可以删除指定包下面的node_modules。</span>
<span class="hljs-comment">// 注意： 不会删除package.json里面的依赖项定义，也不会删除root目录的node_modules</span>
lerna clean
lerna clean --scope=<package-name>

<span class="hljs-comment">// 列出所有公开的包（排除private=true的）</span>
lerna list
lerna list --json <span class="hljs-comment">// json形式</span>

<span class="hljs-comment">// 检查自上次发布以来有哪些包有更新</span>
lerna changed

<span class="hljs-comment">// 查看自上次发布以来的所有包或者指定包的git diff变化</span>
lerna diff

<span class="hljs-comment">// 在包含该脚本命令的每个package内部执行npm script脚本命令,也可以指定在某个package下执行</span>
lerna run
lerna run build --scope=feu-ui

<span class="hljs-comment">// 在每个包中执行任意命令，也可以指定在某个package下执行</span>
lerna exec
lerna exec -- npm view \$LERNA_PACKAGE_NAME

<span class="hljs-comment">// 将相互依赖的所有包Symlink链接在一起</span>
lerna link

<span class="hljs-comment">// 版本更新</span>
lerna version

<span class="hljs-comment">// 发布包</span>
<span class="hljs-comment">// 不会发布标记为私有（package.json中private=true）的包</span>
<span class="hljs-comment">// 代码必须先提交到 `git`</span>
<span class="hljs-comment">// 必须登录 `npm`</span>
lerna publish

<span class="hljs-comment">// 显示发布当前提交中标记的包，类似于先独立执行lerna version后，再执行此命令进行发布</span>
lerna publish <span class="hljs-keyword">from</span>-git

<span class="hljs-comment">//显示发布npm registry中不存在的最新版本的包</span>
lerna publish <span class="hljs-keyword">from</span>-package

<span class="hljs-comment">// 导入</span>
<span class="hljs-comment">// 将本地的包导入到指定目录</span>
lerna <span class="hljs-keyword">import</span> ~<span class="hljs-regexp">/Users/</span>desktop --dest=package-name 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">设置yarn useWorkspaces</h2>
<ul>
<li>默认是npm, 而且每个子package都有自己的<code>node_modules</code>，通过这样设置后，只有顶层有一个<code>node_modules</code></li>
<li>通过使用<code>workspace</code>，<code>yarn install</code>会自动的帮忙解决安装和link问题</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">yarn install <span class="hljs-comment"># 等价于 lerna bootstrap --npm-client yarn --use-workspaces</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>lerna.json</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"npmClient"</span>: <span class="hljs-string">"yarn"</span>,  <span class="hljs-comment">// 指定使用yarn，默认npm</span>
<span class="hljs-string">"useWorkspaces"</span>: <span class="hljs-literal">true</span>  <span class="hljs-comment">// 使用工作区域</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>package.json</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"workspaces"</span>: [
    <span class="hljs-string">"packages/*"</span>
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>lerna add axios</p>
<ul>
<li>axios 安装到根目录的 <code>node_modules</code></li>
<li>axios 依赖写入各包的 <code>package.json</code>中</li>
</ul>
<h2 data-id="heading-4">注意事项</h2>
<ul>
<li><code>lerna-repo</code> 根目录是管理包的并不需要发布，<code>lerna-repo、package.json</code> 设置 <code>"private": true</code></li>
<li><code>lerna-repo/packages</code> 目录下才是需要发布的包，不需要发布的也设置 <code>"private": true</code></li>
<li>通过使用workspace，yarn install会自动的帮忙解决安装和link问题</li>
<li>发布 <code>@scope</code> 包</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// 在需要发布的子包下设置，而不是根目录的 package.json</span>
&#123;
 <span class="hljs-attr">"name"</span>: <span class="hljs-string">"@vtian/package-name"</span>,
 <span class="hljs-attr">"publishConfig"</span>: &#123;
   <span class="hljs-attr">"access"</span>: <span class="hljs-string">"publish"</span> <span class="hljs-comment">// 如果该模块需要发布，对于scope模块，需要设置为publish，否则需要权限验证</span>
   <span class="hljs-comment">// "registry": "https://[registry-url]" // 不要在子包中设置发布地址，在根目录的package.json中设置。会导致发布失败</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果发布的是私仓，可能还需要配置</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// .npmrc文件</span>

egistry = https:<span class="hljs-comment">//[registry-url]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">lerna.json 完整配置文件</h2>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.1.3"</span>,
  <span class="hljs-attr">"npmClient"</span>: <span class="hljs-string">"npm"</span>,
  <span class="hljs-attr">"command"</span>: &#123;
    <span class="hljs-attr">"publish"</span>: &#123;
      <span class="hljs-attr">"ignoreChanges"</span>: [<span class="hljs-string">"ignored-file"</span>, <span class="hljs-string">"*.md"</span>],
      <span class="hljs-attr">"message"</span>: <span class="hljs-string">"chore(release): publish"</span>,
      <span class="hljs-attr">"registry"</span>: <span class="hljs-string">"https://npm.pkg.github.com"</span>
    &#125;,
    <span class="hljs-attr">"bootstrap"</span>: &#123;
      <span class="hljs-attr">"ignore"</span>: <span class="hljs-string">"component-*"</span>,
      <span class="hljs-attr">"npmClientArgs"</span>: [<span class="hljs-string">"--no-package-lock"</span>]
    &#125;
  &#125;,
  <span class="hljs-attr">"packages"</span>: [<span class="hljs-string">"packages/*"</span>]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数说明：</p>
<ul>
<li>version 当前库的版本号，独立模式下，此参数设置为independent</li>
<li>npmClient 允许指定命令使用的client， 默认是npm， 可以设置成yarn</li>
<li>command.publish.ignoreChanges 可以指定那些目录或者文件的变更不会被publish</li>
<li>command.publish.message 指定发布时提交的消息格式</li>
<li>command.publish.registry 设置npm包发布的注册地址</li>
<li>command.bootstrap.ignore 设置执行lerna bootstrap安装依赖时不受影响的包</li>
<li>command.bootstrap.npmClientArgs 指定在执行lerna bootstrap命令时传递给npm install的参数</li>
<li>command.bootstrap.scope 指定那些包会受 lerna bootstrap 命令影响</li>
<li>packages 指定包所在目录</li>
</ul>
<h2 data-id="heading-6">适用场景</h2>
<ul>
<li>工具包</li>
<li>公共ui组件库</li>
<li>前端微服务项目</li>
</ul>
<h2 data-id="heading-7">项目地址</h2>
<p><a href="https://github.com/tiandashu/lerna-repo.git" target="_blank" rel="nofollow noopener noreferrer">lerna-repo</a></p></div>  
</div>
            