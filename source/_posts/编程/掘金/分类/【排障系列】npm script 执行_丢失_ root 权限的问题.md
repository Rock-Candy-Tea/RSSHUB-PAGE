
---
title: '【排障系列】npm script 执行_丢失_ root 权限的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ef62d2ad79b4707b62813dd3a5a7b61~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 01 May 2021 07:39:47 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ef62d2ad79b4707b62813dd3a5a7b61~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1、问题背景</h2>
<p>近期，在线上运行服务时遇到了一个诡异的 Linux 权限问题：root 用户在操作本该有权限的资源时，却报了权限错误。</p>
<p>报错如下：</p>
<pre><code class="hljs language-text copyable" lang="text">Error: EACCES: permission denied, mkdir '/root/.pm2/logs'
    at Object.mkdirSync (fs.js:921:3)
    at mkdirpNativeSync (/home/web_server/project/node_modules/pm2/node_modules/mkdirp/lib/mkdirp-native.js:29:10)
    at Function.mkdirpSync [as sync] (/home/web_server/project/node_modules/pm2/node_modules/mkdirp/index.js:21:7)
    at module.exports.Client.initFileStructure (/home/web_server/project/node_modules/pm2/lib/Client.js:133:25)
    at new module.exports (/home/web_server/project/node_modules/pm2/lib/Client.js:38:8)
    at new API (/home/web_server/project/node_modules/pm2/lib/API.js:108:19)
    at Object.<anonymous> (/home/web_server/、project/node_modules/pm2/lib/binaries/CLI.js:22:11)
    at Module._compile (internal/modules/cjs/loader.js:1137:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:1157:10)
    at Module.load (internal/modules/cjs/loader.js:985:32)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个错误非常直观，就是用户想要创建 <code>/root/.pm2/logs</code> 文件夹，但是没有权限。该服务使用 pm2 做多进程管理。pm2 默认会将其日志信息、进程信息等写入到 <code>$HOME/.pm2</code> 下。因为是 root 后用户所以写到了 <code>/root/.pm2</code> 里。</p>
<p>但这个问题的奇怪之处在于，服务是通过 root 用户启动的，对 <code>/root</code> 目录是具有写入权限的。但这里却报了名优权限的错我。</p>
<p>那么是什么导致 root 用户操作 <code>/root</code> 目录的权限“丢失”了呢？</p>
<h2 data-id="heading-1">2、初步排查</h2>
<p>项目是容器化部署，使用 npm script 启动，代码文件位于 <code>/home/web_server/project</code> 下。执行 <code>npm start</code> 即可启动。</p>
<p>这是我们使用的一套标准的构建与部署「模版」，已经在上百个服务上应用，且一直都正常。知道近期的一次上线出现了上面这个问题。</p>
<p>这次突然出现的这个问题让我充满了疑惑 —— 基于对 Linux 系统用户、用户组权限控制的理解，不可能出现这个错误。难道是我理解有误？</p>
<p>在疑惑的同时，我尝试不使用 npm script，直接通过 pm2 命令行 <code>pm2 start ecosystem.config.js</code> 启动，发现服务正常启动了！莫非是 npm 导致的？</p>
<p>而在这次上线的时候，确实更新了基础镜像，升级了 npm cli。之前是 v6.x，这次更新到了 v7.x。而当我将 npm 版本回退到 v6.x 后，问题小时。看来是 v7.x 的改动导致了这个问题。</p>
<h2 data-id="heading-2">3、问题定位</h2>
<p>先说结论：npm v6.x 使用 npm script 执行命令时默认会使用 unsafe 模式，将子执行命令的子进程设置为 root 用户/用户组，该行为可以通过 <code>unafe-pem</code> 配置来控制。而在 v7.x 中，如果通过 root 用户执行 npm script，则会基于当前目录（cwd）所属用户来设置。</p>
<p>下面通过代码来一起看下。</p>
<h3 data-id="heading-3">3.1、v7.x 中 npm script 的实现</h3>
<blockquote>
<p>以下代码来自 <a href="https://github.com/npm/cli/tree/v7.11.1" target="_blank" rel="nofollow noopener noreferrer">npm/cli v7.11.1</a></p>
</blockquote>
<p>npm script 的执行逻辑可以从 <a href="https://github.com/npm/cli/blob/v7.11.1/lib/exec.js#L88" target="_blank" rel="nofollow noopener noreferrer"><code>lib/exec.js</code></a> 中查看：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Exec</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">BaseCommand</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">async</span> _exec (_args, &#123; locationMsg, path, runPath &#125;) &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-keyword">if</span> (call && _args.length)
      <span class="hljs-keyword">throw</span> <span class="hljs-built_in">this</span>.usage

    <span class="hljs-keyword">return</span> libexec(&#123;
      ...flatOptions,
      args,
      <span class="hljs-comment">// ...</span>
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>省略无关代码，可以看到执行 npm script 时会调用 <code>libexec</code> 方法，<a href="https://github.com/npm/cli/blob/v7.11.1/node_modules/libnpmexec/lib/index.js#L50" target="_blank" rel="nofollow noopener noreferrer"><code>libexec</code> 方法</a>内部会调用 <a href="https://github.com/npm/cli/blob/v7.11.1/node_modules/libnpmexec/lib/index.js#L50" target="_blank" rel="nofollow noopener noreferrer"><code>runScript</code> 方法</a>来执行命令。</p>
<blockquote>
<p>因为调用链比较长，我把中间代码省略了，只贴出关键的代码，感兴趣的朋友可以点击文中链接跳转查看。</p>
</blockquote>
<p>通过<a href="https://github.com/npm/cli/blob/v7.11.1/node_modules/%40npmcli/run-script/lib/run-script.js#L9" target="_blank" rel="nofollow noopener noreferrer">一系列</a>曲折的调用，代码最后会调用到 <a href="https://github.com/npm/cli/blob/v7.11.1/node_modules/%40npmcli/run-script/lib/run-script-pkg.js#L54" target="_blank" rel="nofollow noopener noreferrer"><code>promiseSpawn</code> 方法</a>。这个方法最终会使用 child_process 内置模块里提的 <code>spawn</code> 方法来启动子进程执行命令，其<a href="https://github.com/npm/cli/blob/v7.11.1/node_modules/%40npmcli/promise-spawn/index.js#L13-L20" target="_blank" rel="nofollow noopener noreferrer">相关代码</a>如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promiseSpawn = <span class="hljs-function">(<span class="hljs-params">cmd, args, opts, extra = &#123;&#125;</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> cwd = opts.cwd || process.cwd()
  <span class="hljs-keyword">const</span> isRoot = process.getuid && process.getuid() === <span class="hljs-number">0</span>
  <span class="hljs-keyword">const</span> &#123; uid, gid &#125; = isRoot ? inferOwner.sync(cwd) : &#123;&#125;
  <span class="hljs-keyword">return</span> promiseSpawnUid(cmd, args, &#123;
    ...opts,
    cwd,
    uid,
    gid
  &#125;, extra)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的实现中，有一行非常重要：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; uid, gid &#125; = isRoot ? inferOwner.sync(cwd) : &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，如果当前进程的用户是 root，则会使用 <code>inferOwner</code> 方法来设置启动的子进程的 uid 和 gid（也就是用户 id 和用户组 id）。</p>
<p>那么 <code>inferOwner</code> 是做什么的呢？它其实就是<a href="https://github.com/npm/cli/blob/v7.11.1/node_modules/%40npmcli/promise-spawn/index.js#L13-L20" target="_blank" rel="nofollow noopener noreferrer">用来获取某个文件所属的用户与用户组</a>的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> inferOwnerSync = <span class="hljs-function"><span class="hljs-params">path</span> =></span> &#123;
  path = resolve(path)
  <span class="hljs-keyword">if</span> (cache.has(path))
    <span class="hljs-keyword">return</span> cache.get(path)

  <span class="hljs-keyword">const</span> parent = dirname(path)

  <span class="hljs-keyword">let</span> threw = <span class="hljs-literal">true</span>
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">const</span> st = fs.lstatSync(path)
    threw = <span class="hljs-literal">false</span>
    <span class="hljs-keyword">const</span> &#123; uid, gid &#125; = st
    cache.set(path, &#123; uid, gid &#125;)
    <span class="hljs-keyword">return</span> &#123; uid, gid &#125;
  &#125; <span class="hljs-keyword">finally</span> &#123;
    <span class="hljs-keyword">if</span> (threw && parent !== path) &#123;
      <span class="hljs-keyword">const</span> owner = inferOwnerSync(parent)
      cache.set(path, owner)
      <span class="hljs-keyword">return</span> owner <span class="hljs-comment">// eslint-disable-line no-unsafe-finally</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中最重要的代码是这几行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> st = fs.lstatSync(path)
<span class="hljs-comment">// ...</span>
<span class="hljs-keyword">const</span> &#123; uid, gid &#125; = st
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://nodejs.org/dist/latest-v14.x/docs/api/fs.html#fs_fs_lstatsync_path_options" target="_blank" rel="nofollow noopener noreferrer"><code>fs.lstatSync</code> 方法</a> 会使用 <a href="https://man7.org/linux/man-pages/man2/lstat.2.html" target="_blank" rel="nofollow noopener noreferrer"><code>fstat</code></a> 这个系统调用来获取文件的 uid 和 gid。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ef62d2ad79b4707b62813dd3a5a7b61~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>promiseSpawn</code> 中会将 cwd 传入来获取 uid 和 gid。而在我们线上服务的容器里，我们是在 <code>/home/web_server/project</code> 下执行 <code>npm start</code>，该目录所属用户是 <code>web_server</code>，用户组是 <code>web_server</code>。所以 npm 在启动子进程时“切换”了用户。</p>
<p>所以实际情况是，<code>pm2 start ecosystemt.config.js</code> 相当于是被 web_server 用户启动的，但是环境变量 <code>$HOME</code> 仍然是 <code>/root</code>。所以在 <code>/root</code> 中创建文件夹，自然就没有权限。</p>
<h3 data-id="heading-4">3.2、v6.x 中 npm script 实现方式的区别</h3>
<blockquote>
<p>以下代码来自 <a href="https://github.com/npm/cli/tree/v6.14.8" target="_blank" rel="nofollow noopener noreferrer">npm/cli v6.14.8</a></p>
</blockquote>
<p>v7.x 为了权限安全，做了上述操作，那么 v6.x 如何呢？</p>
<p>v6.x 的 npm script 入口是 <a href="https://github.com/npm/cli/blob/v6.14.8/lib/run-script.js#L173" target="_blank" rel="nofollow noopener noreferrer"><code>lib/run-script.js</code> 文件</a>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span> (<span class="hljs-params">pkg, wd, cmd, args, cb</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  chain(cmds.map(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">c</span>) </span>&#123;
    <span class="hljs-comment">// pass cli arguments after -- to script.</span>
    <span class="hljs-keyword">if</span> (pkg.scripts[c] && c === cmd) &#123;
      pkg.scripts[c] = pkg.scripts[c] + joinArgs(args)
    &#125;

    <span class="hljs-comment">// when running scripts explicitly, assume that they're trusted.</span>
    <span class="hljs-keyword">return</span> [lifecycle, pkg, c, wd, &#123; <span class="hljs-attr">unsafePerm</span>: <span class="hljs-literal">true</span> &#125;]
  &#125;), cb)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而其实际执行则需要从 <code>lifecycle</code> 方法中来找。上面这段代码的最后一行还有一个非常重要的参数 <code>&#123; unsafePerm: true &#125;</code>，之后会用到。</p>
<p><a href="https://github.com/npm/cli/blob/v6.14.8/lib/utils/lifecycle.js#L13" target="_blank" rel="nofollow noopener noreferrer">lifecycle</a> 本身代码并不复杂，主要就是参数调整，然后调用实际函数。和 uid、gid 实际的设置代码是在 <a href="https://github.com/npm/cli/blob/v6.14.8/node_modules/npm-lifecycle/index.js#L264-L276" target="_blank" rel="nofollow noopener noreferrer"><code>npm-lifecycle/index.js</code> 中的 <code>runCmd</code></a> 里：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runCmd</span> (<span class="hljs-params">note, cmd, pkg, env, stage, wd, opts, cb</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">var</span> unsafe = opts.unsafePerm
  <span class="hljs-keyword">var</span> user = unsafe ? <span class="hljs-literal">null</span> : opts.user
  <span class="hljs-keyword">var</span> group = unsafe ? <span class="hljs-literal">null</span> : opts.group
  
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">if</span> (unsafe) &#123;
    runCmd_(cmd, pkg, env, wd, opts, stage, unsafe, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, cb)
  &#125; <span class="hljs-keyword">else</span> &#123;
    uidNumber(user, group, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">er, uid, gid</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (er) &#123;
        er.code = <span class="hljs-string">'EUIDLOOKUP'</span>
        opts.log.resume()
        process.nextTick(dequeue)
        <span class="hljs-keyword">return</span> cb(er)
      &#125;
      runCmd_(cmd, pkg, env, wd, opts, stage, unsafe, uid, gid, cb)
    &#125;)
  &#125;
&#125;

<span class="hljs-comment">// ...</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runCmd_</span> (<span class="hljs-params">cmd, pkg, env, wd, opts, stage, unsafe, uid, gid, cb_</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">var</span> proc = spawn(sh, args, conf, opts.log)
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>runCmd</code> 里会通过传入的 <code>opt.unsafePem</code> 参数（就是上面设置的那个 <code>&#123; unsafePerm: true &#125;</code>）来判断是否是 <code>unsafe</code> 的。如果是 <code>unsafe</code>，则会在调用 <code>runCmd_</code> 时将 uid、gid 设置为 0。0 就代表 root 用户和 root 用户组。</p>
<p>而最终在 <code>runCmd_</code> 中的 <a href="https://github.com/npm/cli/blob/v6.14.8/node_modules/npm-lifecycle/lib/spawn.js#L36" target="_blank" rel="nofollow noopener noreferrer"><code>spawn</code></a> 就是 <code>child_process</code> 中的 <code>spawn</code> 方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> _spawn = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>).spawn
<span class="hljs-comment">// ...</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">spawn</span> (<span class="hljs-params">cmd, args, options, log</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">const</span> raw = _spawn(cmd, args, options)
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>到这里我们就定位到了该问题：</p>
<ul>
<li>在 v6.x 中，只要没有设置 <code>unsafe-pem</code> 这个 npm config，npm script 就会在启动子进程时默认设置为 root。</li>
<li>而在 v7.x 中，如果运行时是 root 用户，则会根据 cwd 所属的用户/用户组，来设置启动子进程的 uid 和 gid。</li>
</ul>
<p>目前从代码实现来看，似乎没有特别好的处理方式，比较简答的两种就是：</p>
<ul>
<li>如果用 v7.x，在我们这个场景下，可以把 <code>/home/web_server/project</code> 所属用户/用户组改为 root。但权限的改动可能会引发其他问题。</li>
<li>先暂时回退到 v6.x，使环境和保持一致。</li>
</ul>
<h3 data-id="heading-5">3.3、npm cli 的变更日志</h3>
<p>其实，这个变更在 npm <a href="https://github.com/npm/cli/blob/v7.11.1/CHANGELOG.md#all-lifecycle-scripts" target="_blank" rel="nofollow noopener noreferrer">v7.0.0-beta.0 发布时的 CHANGELOG</a> 里是有提到的。不过只有寥寥一行：</p>
<blockquote>
<p>The user, group, uid, gid, and unsafe-perms configurations are no longer relevant. When npm is run as root, scripts are always run with the effective uid and gid of the working directory owner.</p>
</blockquote>
<p>大致说的就是咱们上面从代码分析的结论：如果是 root 运行 npm，则在脚本执行时切换到当前工作目录的 owner。</p>
<p>然后如果你跟着代码看下来，也会发现 v6.x 中的 <code>unsafe-pem</code> 配置，在 v7.0.0 开始就被废弃了。不过 npm cli 文档更新的较慢，直到 v7.0.0 正式版发布后的一个月后，才在 <a href="https://github.com/npm/cli/blob/v7.11.1/CHANGELOG.md#documentation-16" target="_blank" rel="nofollow noopener noreferrer">v7.0.15 的 Release</a> 里把 <code>unsafe-pem</code> 从文档中移除。</p>
<h3 data-id="heading-6">3.4、其他可能出现的问题</h3>
<p>这个功能实现的变更，除了会导致一些文件操作时的权限问题，还会有一些其他场景的权限错误。例如在如果你用 npm script 启动一个 nodejs server，要绑定 443 端口，这个时候可能就会报错。因为会需要 root 权限来执行这个端口绑定。在 <a href="https://github.com/npm/cli/issues/3110" target="_blank" rel="nofollow noopener noreferrer">issue 里就有人提到了这个情况</a>。</p>
<hr>
<h2 data-id="heading-7">4、加餐：child_process#spawn 是如何设置 user 和 group 的？</h2>
<p>通过上面的分析，问题已经被解决了。沿着这个问题，可以具体看了下 Nodejs 中，child_process 模块的 <code>spawn</code> 方法是如何设置 user 和 group 的。</p>
<blockquote>
<p>以下代码基于 <a href="https://github.com/nodejs/node/tree/v14.16.1" target="_blank" rel="nofollow noopener noreferrer">Nodejs v14.16.1</a>。只关注 unix 实现。</p>
</blockquote>
<p>Nodejs 中，我们在上层引入的模块，是直接放在 <code>lib</code> 下面的，而其一般会在调用 <code>lib/internal</code> 下的对应模块，这部分会直接使用 internalBinding 来调用 C++ 对象和方法。child_process 也不例外，你会在 <a href="https://github.com/nodejs/node/blob/v14.16.1/lib/internal/child_process.js#L378" target="_blank" rel="nofollow noopener noreferrer"><code>lib/internal/child_process.js</code></a> 中看到如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js">ChildProcess.prototype.spawn = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">const</span> err = <span class="hljs-built_in">this</span>._handle.spawn(options);
  <span class="hljs-comment">// ...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为比较简答，所以这里省去了 <code>lib/child_process.js</code> 中的方法。只要知道，我们在 JavaScript 层使用 <code>spawn</code> 方法时，最后会调用到 ChildProcess 实例的 <code>spawn</code> 方法即可。可以看到最后是调用了 <code>this._handle.spawn</code>。那么 <code>this._handle</code> 是什么呢？</p>
<p>它其实就是<a href="https://github.com/nodejs/node/blob/v14.16.1/lib/internal/child_process.js#L250" target="_blank" rel="nofollow noopener noreferrer">通过 binding 创建的 Process 对象</a>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; Process &#125; = internalBinding(<span class="hljs-string">'process_wrap'</span>);

<span class="hljs-comment">// ...</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ChildProcess</span>(<span class="hljs-params"></span>) </span>&#123;
  EventEmitter.call(<span class="hljs-built_in">this</span>);

  <span class="hljs-comment">// ...</span>
  <span class="hljs-built_in">this</span>._handle = <span class="hljs-keyword">new</span> Process();
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 binding 的设置在 <a href="https://github.com/nodejs/node/blob/v14.16.1/src/process_wrap.cc#L157-L174" target="_blank" rel="nofollow noopener noreferrer"><code>src/process_wrap.cc</code></a> 中，</p>
<pre><code class="hljs language-c++ copyable" lang="c++">  <span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Spawn</span><span class="hljs-params">(<span class="hljs-keyword">const</span> FunctionCallbackInfo<Value>& args)</span> </span>&#123;
    <span class="hljs-comment">// ...</span>

    <span class="hljs-comment">// options.uid</span>
    Local<Value> uid_v =
        js_options-><span class="hljs-built_in">Get</span>(context, env-><span class="hljs-built_in">uid_string</span>()).<span class="hljs-built_in">ToLocalChecked</span>();
    <span class="hljs-keyword">if</span> (!uid_v-><span class="hljs-built_in">IsUndefined</span>() && !uid_v-><span class="hljs-built_in">IsNull</span>()) &#123;
      <span class="hljs-built_in">CHECK</span>(uid_v-><span class="hljs-built_in">IsInt32</span>());
      <span class="hljs-keyword">const</span> <span class="hljs-keyword">int32_t</span> uid = uid_v.As<Int32>()-><span class="hljs-built_in">Value</span>();
      options.flags |= UV_PROCESS_SETUID;
      options.uid = <span class="hljs-keyword">static_cast</span><<span class="hljs-keyword">uv_uid_t</span>>(uid);
    &#125;

    <span class="hljs-comment">// options.gid</span>
    Local<Value> gid_v =
        js_options-><span class="hljs-built_in">Get</span>(context, env-><span class="hljs-built_in">gid_string</span>()).<span class="hljs-built_in">ToLocalChecked</span>();
    <span class="hljs-keyword">if</span> (!gid_v-><span class="hljs-built_in">IsUndefined</span>() && !gid_v-><span class="hljs-built_in">IsNull</span>()) &#123;
      <span class="hljs-built_in">CHECK</span>(gid_v-><span class="hljs-built_in">IsInt32</span>());
      <span class="hljs-keyword">const</span> <span class="hljs-keyword">int32_t</span> gid = gid_v.As<Int32>()-><span class="hljs-built_in">Value</span>();
      options.flags |= UV_PROCESS_SETGID;
      options.gid = <span class="hljs-keyword">static_cast</span><<span class="hljs-keyword">uv_gid_t</span>>(gid);
    &#125;
    
    <span class="hljs-keyword">int</span> err = <span class="hljs-built_in">uv_spawn</span>(env-><span class="hljs-built_in">event_loop</span>(), &wrap->process_, &options);
    wrap-><span class="hljs-built_in">MarkAsInitialized</span>();
    
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，它把从 JavaScript 层设置的 uid 和 gid 设置到 options 上，然后调用了 <a href="https://docs.libuv.org/en/latest/process.html?highlight=uv_spawn#c.uv_spawn" target="_blank" rel="nofollow noopener noreferrer"><code>uv_spawn</code></a> 函数创建子进程。在 <code>uv_spawn</code> 中对于创建的子进程会通过 <a href="https://github.com/nodejs/node/blob/v14.16.1/deps/uv/src/unix/process.c#L408" target="_blank" rel="nofollow noopener noreferrer"><code>uv__process_child_init</code> 来做初始化设置</a>：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_spawn</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop,
             <span class="hljs-keyword">uv_process_t</span>* process,
             <span class="hljs-keyword">const</span> <span class="hljs-keyword">uv_process_options_t</span>* options)</span> </span>&#123;

    <span class="hljs-comment">// ...</span>
    <span class="hljs-keyword">if</span> (pid == <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">uv__process_child_init</span>(options, stdio_count, pipes, signal_pipe[<span class="hljs-number">1</span>]);
        <span class="hljs-built_in">abort</span>();
    &#125;
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后则是在 <a href="https://github.com/nodejs/node/blob/v14.16.1/deps/uv/src/unix/process.c#L346-L365" target="_blank" rel="nofollow noopener noreferrer"><code>uv__process_child_init</code></a> 里通过 <a href="https://man7.org/linux/man-pages/man2/setuid.2.html" target="_blank" rel="nofollow noopener noreferrer"><code>setuid</code></a> 和 <a href="https://man7.org/linux/man-pages/man2/setgid.2.html" target="_blank" rel="nofollow noopener noreferrer"><code>setgid</code></a> 这两个系统调用来实现的：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">uv__process_child_init</span><span class="hljs-params">(<span class="hljs-keyword">const</span> <span class="hljs-keyword">uv_process_options_t</span>* options,
                                   <span class="hljs-keyword">int</span> stdio_count,
                                   <span class="hljs-keyword">int</span> (*pipes)[<span class="hljs-number">2</span>],
                                   <span class="hljs-keyword">int</span> error_fd)</span> </span>&#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-keyword">if</span> ((options->flags & UV_PROCESS_SETGID) && <span class="hljs-built_in">setgid</span>(options->gid)) &#123;
        <span class="hljs-built_in">uv__write_int</span>(error_fd, <span class="hljs-built_in">UV__ERR</span>(errno));
        _exit(<span class="hljs-number">127</span>);
    &#125;

    <span class="hljs-keyword">if</span> ((options->flags & UV_PROCESS_SETUID) && <span class="hljs-built_in">setuid</span>(options->uid)) &#123;
        <span class="hljs-built_in">uv__write_int</span>(error_fd, <span class="hljs-built_in">UV__ERR</span>(errno));
        _exit(<span class="hljs-number">127</span>);
    &#125;
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Nodejs 官方文档中也有介绍。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/379f96ae2540423d876d468513e72241~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们通过阅读代码也印证了这一点。</p>
<p>完。</p>
<blockquote>
<p>往期【排障系列】文章：</p>
<ul>
<li><a href="https://juejin.cn/post/6949823818097492005" target="_blank">记一次 Node gRPC 静态生成文件引发的问题</a></li>
</ul>
</blockquote></div>  
</div>
            