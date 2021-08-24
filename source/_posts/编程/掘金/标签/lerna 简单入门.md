
---
title: 'lerna 简单入门'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/367a4f983a60471eaea111788c8f42bc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 06:45:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/367a4f983a60471eaea111788c8f42bc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Multirepo模式</h2>
<p>单体仓库，即每一个<code>package</code>都单独用一个仓库来进行管理。如果不同<code>package</code>之间相互依赖，会越来越难以维护。</p>
<h2 data-id="heading-1">Monorepo</h2>
<p>所有相关的<code>package</code>都放在一个仓库里进行管理。</p>
<h2 data-id="heading-2">lerna是什么？</h2>
<blockquote>
<p>A tool for managing JavaScript projects with multiple packages. 一个用于管理，具有多个<code>package</code>，项目的工具。</p>
</blockquote>
<p>一个由lerna管理的项目，通常的结构如下：</p>
<pre><code class="hljs language-shell copyable" lang="shell">- 📃 lerna.json
- 📃 package.json
- 📁 packages
  - 📁 packageA
    - 📃 package.json  
  - 📁 packageB
    - 📃 package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">lerna Fixed/Locked 模式 (默认模式)</h2>
<p>默认的模式，<code>lerna init</code> 创建默认模式的项目。固定模式使用 <code>lerna.json</code> 对所有的 <code>package</code> 进行统一的版本管理。多项目中任何一个 <code>package</code> 修改都会导致所有 <code>package</code> 的版本号变动。</p>
<h2 data-id="heading-4">lerna Independent 模式</h2>
<p>独立模式，<code>lerna init --independent</code> 创建独立模式的项目。独立模式允许每一个 <code>package</code> 单独修改版本号。在 <code>lerna publish</code> 时, 只会更新有变化的 <code>package</code> 的版本号。</p>
<h2 data-id="heading-5">lerna.json</h2>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"1.1.3"</span>, <span class="hljs-comment">// 版本号，Independent模式下设置为independent</span>
  <span class="hljs-string">"npmClient"</span>: <span class="hljs-string">"npm"</span>, <span class="hljs-comment">// 指定运行命令的客户端</span>
  <span class="hljs-string">"command"</span>: &#123;
    <span class="hljs-string">"publish"</span>: &#123;
      <span class="hljs-string">"ignoreChanges"</span>: [<span class="hljs-string">"ignored-file"</span>, <span class="hljs-string">"*.md"</span>], <span class="hljs-comment">// 指定那些目录或者文件的变更不会被publish</span>
      <span class="hljs-string">"message"</span>: <span class="hljs-string">"chore(release): publish"</span>, <span class="hljs-comment">// 执行发布版本更新时的自定义提交消息</span>
      <span class="hljs-string">"registry"</span>: <span class="hljs-string">"https://npm.pkg.github.com"</span> <span class="hljs-comment">// 设置npm包发布的注册地址</span>
    &#125;,
  &#125;,
  <span class="hljs-string">"packages"</span>: [<span class="hljs-string">"packages/*"</span>] <span class="hljs-comment">// 指定包所在的目录</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">使用lerna</h2>
<h3 data-id="heading-7">安装lerna</h3>
<pre><code class="hljs language-shell copyable" lang="shell">npm install --global lerna
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">初始化lerna (使用默认模式)</h3>
<pre><code class="hljs language-shell copyable" lang="shell">lerna init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>项目目录结构如下：</p>
<pre><code class="hljs language-shell copyable" lang="shell">- 📁 packages3
- 📃 package.json
- 📃 lerna.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目目录中创建三个项目</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/367a4f983a60471eaea111788c8f42bc~tplv-k3u1fbpfcp-watermark.image" alt="lerna-app.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>app 依赖 ui, utils</li>
<li>ui 依赖 utils</li>
<li>utils 不依赖任何库，需要发布到 npm 上</li>
</ul>
<pre><code class="hljs language-shell copyable" lang="shell">lerna create app && lerna create ui && lerna create utils
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时项目的文件夹结构，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0d4d9cc4677443cb3c12bb323f90759~tplv-k3u1fbpfcp-watermark.image" alt="项目目录.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">处理 utils package</h4>
<p>在 <code>utils.js</code> 中简单添加一些示例代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>;

<span class="hljs-built_in">module</span>.exports = &#123; add &#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">...args</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'使用 utils 库的的 add 方法'</span>)
    <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < args.length; i += <span class="hljs-number">1</span>) &#123;
        sum += args[i]
    &#125;
    <span class="hljs-keyword">return</span> sum
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">处理 ui package</h4>
<ol>
<li>在 ui package 中的 package.json 文件中设置 <code>private: true</code>, npm 不会发布这个包。</li>
<li>将 utils 添加到 ui package 中。<code>lerna add utils --scope=ui</code></li>
</ol>
<p>在 ui.js 中使用 utlis</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>;

<span class="hljs-keyword">const</span> &#123; add &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'utils'</span>);

<span class="hljs-built_in">module</span>.exports = ui;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ui</span>(<span class="hljs-params">...args</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'调用 ui 函数'</span>, ...args);
  add(...args)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">处理 app package</h4>
<ol>
<li>在 app package 中的 package.json 文件中设置 <code>private: true</code>, npm 不会发布这个包。</li>
<li>将 ui 和 utils 添加到app中。 <code>lerna add ui --scope=app</code>, <code>lerna add utils --scope=app</code></li>
</ol>
<p>在 app.js 中 使用 ui 和 utlis</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>;

<span class="hljs-keyword">const</span> &#123; add &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'utils'</span>);
<span class="hljs-keyword">const</span> ui = <span class="hljs-built_in">require</span>(<span class="hljs-string">'ui'</span>);

<span class="hljs-built_in">module</span>.exports = app;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">app</span>(<span class="hljs-params"></span>) </span>&#123;
    add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>)
    ui(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>)
&#125;

app()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行 app, <code>node app.js</code>。得到，如下的log</p>
<pre><code class="hljs language-shell copyable" lang="shell">使用 utils 库的的 add 方法
调用 ui 函数 1 2 3
使用 utils 库的的 add 方法
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">npm发布</h2>
<p>我们需要把 utils 发布到 npm 上。如果项目需要 build。需要提前使用 build 命令对项目进行打包。</p>
<p>接下来调用 lerna publish 发布项目，由于使用的 Fixed/Locked 模式，所有项目的版本号，会根据 lerna.json 中的版本号更新。</p>
<p><img src="https://i.loli.net/2021/08/23/ChesGxrzptjwYDT.png" alt="发布1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择版本后，可以看到终端页面如下：</p>
<p><img src="https://i.loli.net/2021/08/23/PKQc2N8yGz1LHrd.png" alt="发布2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>三个 package 的版本号都统一为0.0.1，而且 app 和 ui 为 private，不会被发布到 npm。</p>
<h2 data-id="heading-13">lerna的命令</h2>
<h3 data-id="heading-14">lerna init</h3>
<p>初始化 lerna 项目</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">
#</span><span class="bash"> 固定模式</span>
lerna init
<span class="hljs-meta">
#</span><span class="bash"> 独立模式</span>
lerna init ----independent
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">lerna bootstrap</h3>
<p>安装所有 package 的依赖。并且连接本地包的交叉依赖。</p>
<h3 data-id="heading-16">lerna create</h3>
<p>创建一个在 lerna 管理项目中的包。</p>
<h3 data-id="heading-17">lerna import</h3>
<h3 data-id="heading-18">lerna add</h3>
<p>将本地或者远程的包作为依赖项添加到 package 中。</p>
<p><code>lerna add react --scope=app</code>, 在 app 项目中添加 react</p>
<h3 data-id="heading-19">lerna clean</h3>
<p>删除所有 package 的 node_modules 目录。也可以指定删除具体包下面的 node_modules。</p>
<p><code>lerna clean --scope=ui</code>, 删除 ui 下的 node_modules 目录。</p>
<h3 data-id="heading-20">lerna ls</h3>
<p>列出所有公开的包（private: true的除外）</p>
<h3 data-id="heading-21">lerna changed</h3>
<p>检查自上次发布以来，有那些包发生了更新。</p>
<h3 data-id="heading-22">lerna run</h3>
<p>在包含该命令的每个 package 中执行命令, 也可以指定在某个 package 下执行。</p>
<p><code>lerna run build --scope=app</code>, 在 app 中执行build命令。</p>
<h3 data-id="heading-23">lerna publish</h3>
<p>发布需要发布的包</p>
<h2 data-id="heading-24">参考</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.npmjs.com%2Fcli%2Fv7%2Fconfiguring-npm%2Fpackage-json" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.npmjs.com/cli/v7/configuring-npm/package-json" ref="nofollow noopener noreferrer">package.json</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flerna%2Flerna%23readme" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lerna/lerna#readme" ref="nofollow noopener noreferrer">lerna</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Flerna.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://lerna.js.org/" ref="nofollow noopener noreferrer">lerna</a></li>
<li><a href="https://juejin.cn/post/6844904194999058440#heading-22" target="_blank" title="https://juejin.cn/post/6844904194999058440#heading-22">lerna多包管理实践</a></li>
</ul></div>  
</div>
            