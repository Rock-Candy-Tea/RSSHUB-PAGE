
---
title: '深入 lerna 发包机制 —— lerna publish'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35ebc9954e0245df943711a7d8517d6c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 02 Apr 2021 02:32:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35ebc9954e0245df943711a7d8517d6c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>前言：<code>lerna</code> 作为一个风靡的前端 <code>monorepo</code> 管理工具，在许许多多的大型项目中都得到的实践，现在笔者在公司中开发的 monorepo 工具中，monorepo 中子项目的发包能力就是基于 lerna 来完成，因此本篇文章将讲解发包中最关键的命令即 <code>lerna publish</code>。</p>
</blockquote>
<p>在上一篇文章中介绍完了 <code>lerna version</code> 的运行机制后，那么在本篇文章中我将继续介绍一下 lerna 发包机制中最关键的一个 command 即 <code>lerna publish</code>。</p>
<p>现在我们来继续介绍 <code>lerna publish</code> 运行机制，作为发包机制中的最后决定性的一个指令，lerna publish 的做的工作其实很简单，就是将 monorepo 需要发布的包，发布到 npm registry 上面去。</p>
<p>同样 lerna publish 也分为几种不同的场景去运行:</p>
<pre><code class="hljs language-bash copyable" lang="bash">lerna publish  
<span class="hljs-comment"># lerna version + lerna publish from-git</span>
lerna publish from-git 
<span class="hljs-comment"># 发布当前 commit 中打上 annoted tag version 的包</span>
lerna publish from-packages 
<span class="hljs-comment"># 发布 package 中 pkg.json 上的 version 在 registry(高于 latest version)不存在的包</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>官方文档，<code>lerna publish</code> 一共有这样几种执行表现形式:</p>
<blockquote>
<p>lerna publish 永远不会发布 package.json 中 private 设置为 true 的包</p>
</blockquote>
<ul>
<li>发布自上次发布来有更新的包(这里的上次发布也是基于上次执行<code>lerna publish</code> 而言)</li>
<li>发布在当前 commit 上打上了 annotated tag 的包(即 <code>lerna publish from-git</code>)</li>
<li>发布在最近 commit 中修改了 package.json 中的 version (且该 version 在 registry 中没有发布过)的包(即 <code>lerna publish from-package</code>)</li>
<li>发布在上一次提交中更新了的 unversioned 的测试版本的包(以及依赖了的包)</li>
</ul>
<p><code>lerna publish</code> 本身提供了不少的 options，例如支持发布测试版本的包即 (<code>lerna version --canary</code>)。</p>
<p>在上文 lerna version 源码解析中，我们按照 <code>configureProperties -> initialize -> execute</code> 的顺序讲解了 lerna version 的执行顺序，其实在 lerna 中，几乎所有子命令源码的执行顺序都是按照这样一个结构在进行，lerna 本身作为一个 monorepo，主要是使用 core 核心中的执行机制来去分发命令给各个子项目去执行，因此套路都是一样的。</p>
<p>在开始阅读之前，我先提供一个整体的思维导图，可以让读者在开始阅读前有个大致的结构，也便于在阅读过程可以借此来进行回顾：</p>
<img alt="image-20210402004932449" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35ebc9954e0245df943711a7d8517d6c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<h2 data-id="heading-0">设置属性(configureProperties)</h2>
<p>相比较于 lerna version，<code>lerna publish</code> 的这一步就简单许多，大致就是根据 cli 的 options 对一些参数进行了初始化：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">configureProperties</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123;
      exact,
      gitHead,
      gitReset,
      tagVersionPrefix = <span class="hljs-string">"v"</span>,
      verifyAccess,
    &#125; = <span class="hljs-built_in">this</span>.options;

   <span class="hljs-comment">// 这里的 requiresGit 指的是除了 from-package 的其它发包方式</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.requiresGit && gitHead) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> ValidationError(<span class="hljs-string">"EGITHEAD"</span>, <span class="hljs-string">"--git-head is only allowed with 'from-package' positional"</span>);
    &#125;

  <span class="hljs-comment">// --exact 会指定一个具体的 version 版本，而不会加上 npm 那边的版本兼容前缀</span>
    <span class="hljs-built_in">this</span>.savePrefix = exact ? <span class="hljs-string">""</span> : <span class="hljs-string">"^"</span>;

    <span class="hljs-comment">// 用于用户自定义包的版本 tag 前缀，而不是使用默认的 v</span>
    <span class="hljs-built_in">this</span>.tagPrefix = tagVersionPrefix;

    <span class="hljs-comment">// --no-git-reset 用于避免 lerna publish 将暂存区的未提交的代码都 push 到 git 上</span>
    <span class="hljs-built_in">this</span>.gitReset = gitReset !== <span class="hljs-literal">false</span>;
  
    <span class="hljs-comment">// lerna 发包会默认检查用户 npm 权限 </span>
    <span class="hljs-comment">// 设置 --no-verify-access 跳过检查 </span>
    <span class="hljs-built_in">this</span>.verifyAccess = verifyAccess !== <span class="hljs-literal">false</span>;

  <span class="hljs-comment">// npm 发包相关配置</span>
    <span class="hljs-built_in">this</span>.npmSession = crypto.randomBytes(<span class="hljs-number">8</span>).toString(<span class="hljs-string">"hex"</span>);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过注释就可以比较清晰的看到一些 options 以及相关参数的初始化，这里就不详细介绍。</p>
<h2 data-id="heading-1">初始化(initialize)</h2>
<p>下面直接进来初始化的流程中来，因为涉及到发包相关的流程，这一步的前面过程涉及到的就是一些关于 npm 相关的 config 初始化，之后再根据不同的发包情况去进行对应的事件注册，这一步的事件注册以及执行方式都和 <code>lerna version</code> 源码解析时比较类似，主要过程可以分为三个步骤:</p>
<ol>
<li>初始化 npm config 参数</li>
<li>根据不同的发包情况执行不同的方法</li>
<li>处理上一步返回的结果</li>
</ol>
<p>这里不同的发包情况指的即是在文章开头介绍的 lerna publish 的几种执行方式，这里大致梳理一下以下的步骤：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">initialize</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// --skip-npm 相当于直接执行 lerna version </span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.options.skipNpm) &#123;
      <span class="hljs-comment">// 该 api 会在下个 major 被弃用</span>
      <span class="hljs-built_in">this</span>.logger.warn(<span class="hljs-string">"deprecated"</span>, <span class="hljs-string">"Instead of --skip-npm, call `lerna version` directly"</span>);
     <span class="hljs-comment">// 这里我们可以看到 lerna 中某个 command 调用其他 command 都是通过这种链式调用的方式</span>
      <span class="hljs-keyword">return</span> versionCommand(<span class="hljs-built_in">this</span>.argv).then(<span class="hljs-function">() =></span> <span class="hljs-literal">false</span>);
    &#125;
    
    <span class="hljs-comment">// 1. 初始化 npm config 参数</span>

    <span class="hljs-comment">// session 和 userAgent 都是 npm 发包需要验证的参数</span>
    <span class="hljs-built_in">this</span>.logger.verbose(<span class="hljs-string">"session"</span>, <span class="hljs-built_in">this</span>.npmSession);
    <span class="hljs-built_in">this</span>.logger.verbose(<span class="hljs-string">"user-agent"</span>, <span class="hljs-built_in">this</span>.userAgent);

    <span class="hljs-comment">// npm config 相关, 存一些 npm config 相关值</span>
    <span class="hljs-built_in">this</span>.conf = npmConf(&#123;
      <span class="hljs-attr">lernaCommand</span>: <span class="hljs-string">"publish"</span>,
      <span class="hljs-attr">_auth</span>: <span class="hljs-built_in">this</span>.options.legacyAuth,
      <span class="hljs-attr">npmSession</span>: <span class="hljs-built_in">this</span>.npmSession,
      <span class="hljs-attr">npmVersion</span>: <span class="hljs-built_in">this</span>.userAgent,
      <span class="hljs-attr">otp</span>: <span class="hljs-built_in">this</span>.options.otp,
      <span class="hljs-attr">registry</span>: <span class="hljs-built_in">this</span>.options.registry,
      <span class="hljs-string">"ignore-prepublish"</span>: <span class="hljs-built_in">this</span>.options.ignorePrepublish,
      <span class="hljs-string">"ignore-scripts"</span>: <span class="hljs-built_in">this</span>.options.ignoreScripts,
    &#125;);
  
    <span class="hljs-comment">// --dist-tag 用于 设置发包时候自定义 tag</span>
    <span class="hljs-comment">// 一般默认 tag 是 latest</span>
    <span class="hljs-comment">// lerna 中如果没指定 --dist-tag, 正式包的 tag 会用 latest, --canary 的测试包会用 canary</span>
    <span class="hljs-keyword">const</span> distTag = <span class="hljs-built_in">this</span>.getDistTag();

    <span class="hljs-comment">// 如果该参数存在 会被注入进 npm conf 中</span>
    <span class="hljs-keyword">if</span> (distTag) &#123;
      <span class="hljs-built_in">this</span>.conf.set(<span class="hljs-string">"tag"</span>, distTag.trim(), <span class="hljs-string">"cli"</span>);
    &#125;

    <span class="hljs-comment">// 注册运行 lerna.json 里面的 script 的 runner </span>
    <span class="hljs-built_in">this</span>.runPackageLifecycle = createRunner(<span class="hljs-built_in">this</span>.options);

    <span class="hljs-comment">// 如果 lerna 子 package 里面的 pkg.json 里面有 pre|post publish 这样的 script </span>
    <span class="hljs-comment">// 会跳过 lifecycle script 的执行过程，否则会去递归执行</span>
    <span class="hljs-built_in">this</span>.runRootLifecycle = <span class="hljs-regexp">/^(pre|post)?publish$/</span>.test(process.env.npm_lifecycle_event)
      ? <span class="hljs-function"><span class="hljs-params">stage</span> =></span> &#123;
          <span class="hljs-built_in">this</span>.logger.warn(<span class="hljs-string">"lifecycle"</span>, <span class="hljs-string">"Skipping root %j because it has already been called"</span>, stage);
        &#125;
      : <span class="hljs-function"><span class="hljs-params">stage</span> =></span> <span class="hljs-built_in">this</span>.runPackageLifecycle(<span class="hljs-built_in">this</span>.project.manifest, stage);

    
    <span class="hljs-comment">// 2. 根据不同的发包情况执行不同的方法</span>
    
    <span class="hljs-comment">// 通过 promise 构建一个执行链， lerna version 里面讲过</span>
    <span class="hljs-keyword">let</span> chain = <span class="hljs-built_in">Promise</span>.resolve();

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.options.bump === <span class="hljs-string">"from-git"</span>) &#123;
      chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.detectFromGit());
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.options.bump === <span class="hljs-string">"from-package"</span>) &#123;
      chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.detectFromPackage());
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.options.canary) &#123;
      chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.detectCanaryVersions());
    &#125; <span class="hljs-keyword">else</span> &#123;
      chain = chain.then(<span class="hljs-function">() =></span> versionCommand(<span class="hljs-built_in">this</span>.argv));
    &#125;

    <span class="hljs-comment">// 3. 对方法返回的结果做一个处理</span>
    
    <span class="hljs-keyword">return</span> chain.then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
      <span class="hljs-comment">// 如果上一步是走了 lerna version 的 bump version 过程</span>
      <span class="hljs-keyword">if</span> (!result) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
      &#125;

      <span class="hljs-comment">// lerna version 返回的结果数组里面没有需要更新的 package</span>
      <span class="hljs-keyword">if</span> (!result.updates.length) &#123;
        <span class="hljs-built_in">this</span>.logger.success(<span class="hljs-string">"No changed packages to publish"</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
      &#125;

      <span class="hljs-comment">// publish 的时候把 pkg.json 里面设置private 为 false 的包忽略掉 </span>
      <span class="hljs-built_in">this</span>.updates = result.updates.filter(<span class="hljs-function"><span class="hljs-params">node</span> =></span> !node.pkg.private);
      <span class="hljs-comment">// 需要更新的包以及对应更新到的version </span>
      <span class="hljs-built_in">this</span>.updatesVersions = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(result.updatesVersions);

      <span class="hljs-comment">// 再筛选一下需要发包的 packages,根据是否存在 pkg.json</span>
      <span class="hljs-built_in">this</span>.packagesToPublish = <span class="hljs-built_in">this</span>.updates.map(<span class="hljs-function"><span class="hljs-params">node</span> =></span> node.pkg);

      <span class="hljs-comment">// 用于发布 lerna 管理的 packages 的一些子目录例如 dist</span>
      <span class="hljs-comment">// 参考 --contents 这个 options</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.options.contents) &#123;
        <span class="hljs-comment">// 把这些目录写进需要发包的 pkg.json 中</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> pkg <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.packagesToPublish) &#123;
          pkg.contents = <span class="hljs-built_in">this</span>.options.contents;
        &#125;
      &#125;

      <span class="hljs-comment">// 用于确认上面除了 versioncommand 的其他三种执行情况</span>
      <span class="hljs-comment">// 例如 versionCommand 有自己的 confirm 过程</span>
      <span class="hljs-keyword">if</span> (result.needsConfirmation) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.confirmPublish();
      &#125;

      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>initialize</code> 前面有介绍主要分为三个步骤来执行，因此 1、3 两个步骤根据注释来理解过程还是比较清晰的，这里主要介绍一下第二步即 根据不同的发包情况来执行不用的方法，具体代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.options.bump === <span class="hljs-string">"from-git"</span>) &#123;
  chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.detectFromGit());
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.options.bump === <span class="hljs-string">"from-package"</span>) &#123;
  chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.detectFromPackage());
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.options.canary) &#123;
  chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.detectCanaryVersions());
&#125; <span class="hljs-keyword">else</span> &#123;
  chain = chain.then(<span class="hljs-function">() =></span> versionCommand(<span class="hljs-built_in">this</span>.argv));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先根据上面代码中以及文章开头介绍，可以很清晰的知道具体分为这几种情况：</p>
<ul>
<li><code>from-git</code> 即根据 <code>git commit</code> 上的 <code>annotaed tag</code> 进行发包</li>
<li><code>from-package</code> 即根据 lerna 下的 package 里面的 pkg.json 的 version 变动来发包</li>
<li><code>--canary</code> 发测试版本的包</li>
<li>剩下不带参数的情况就直接走一个 bump version(即执行 lerna version)</li>
</ul>
<p>下面从这几种情况做个介绍：</p>
<h3 data-id="heading-2"><code>from-git</code></h3>
<p>这一步的执行入口函数是 <code>detectFromGit</code> ，我们直接看这个函数的执行过程：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">detectFromGit</span>(<span class="hljs-params"></span>)</span> &#123;
    
    <span class="hljs-keyword">const</span> matchingPattern = <span class="hljs-built_in">this</span>.project.isIndependent() ? <span class="hljs-string">"*@*"</span> : <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.tagPrefix&#125;</span>*.*.*`</span>;

    <span class="hljs-keyword">let</span> chain = <span class="hljs-built_in">Promise</span>.resolve();

    <span class="hljs-comment">// 1. 验证当前的 git 工作区域是否干净 通过 git describe 来找</span>
    chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.verifyWorkingTreeClean());

    <span class="hljs-comment">// 2. 拿到当前 commit 上面的 tag</span>
    chain = chain.then(<span class="hljs-function">() =></span> getCurrentTags(<span class="hljs-built_in">this</span>.execOpts, matchingPattern));
  
    <span class="hljs-comment">// 3. 通过上一步的 tag 拿到需要更新的 pkg 的数组</span>
    chain = chain.then(<span class="hljs-function"><span class="hljs-params">taggedPackageNames</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (!taggedPackageNames.length) &#123;
        <span class="hljs-built_in">this</span>.logger.notice(<span class="hljs-string">"from-git"</span>, <span class="hljs-string">"No tagged release found"</span>);

        <span class="hljs-keyword">return</span> [];
      &#125;
      <span class="hljs-comment">// 独立发包模式就拿到所有包的数组</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.project.isIndependent()) &#123;
        <span class="hljs-keyword">return</span> taggedPackageNames.map(<span class="hljs-function"><span class="hljs-params">name</span> =></span> <span class="hljs-built_in">this</span>.packageGraph.get(name));
      &#125;
      
      <span class="hljs-comment">// 固定模式只用拿到一个版本，所有的包都用一个版本</span>
      <span class="hljs-keyword">return</span> getTaggedPackages(<span class="hljs-built_in">this</span>.packageGraph, <span class="hljs-built_in">this</span>.project.rootPath, <span class="hljs-built_in">this</span>.execOpts);
    &#125;);

    <span class="hljs-comment">// 4. 清除掉更新 packages 里面 pkg.json 中设置了 private 为 false 的包</span>
    chain = chain.then(<span class="hljs-function"><span class="hljs-params">updates</span> =></span> updates.filter(<span class="hljs-function"><span class="hljs-params">node</span> =></span> !node.pkg.private));

    <span class="hljs-comment">// 5. updateVersions 存需要发布的包名以及发布的版本</span>
    <span class="hljs-keyword">return</span> chain.then(<span class="hljs-function"><span class="hljs-params">updates</span> =></span> &#123;
      <span class="hljs-keyword">const</span> updatesVersions = updates.map(<span class="hljs-function"><span class="hljs-params">node</span> =></span> [node.name, node.version]);

      <span class="hljs-keyword">return</span> &#123;
        updates,
        updatesVersions,
        <span class="hljs-attr">needsConfirmation</span>: <span class="hljs-literal">true</span>,
      &#125;;
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这一步函数的执行过程还是比较简单明了的，在上面注释中根据不同的方法执行过程分为了 5 个步骤。主要就是根据当前 commit 拿到 tags 里面的 packages 然后返回这些 packages 以及其版本信息。</p>
<h3 data-id="heading-3"><code>from-package</code></h3>
<p>这一步执行的入口函数是 <code>detectFromPackage</code> ，直接看执行过程：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">detectFromPackage</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> chain = <span class="hljs-built_in">Promise</span>.resolve();

    <span class="hljs-comment">// 1. 验证当前 git 工作区是否干净，步骤同上</span>
    chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.verifyWorkingTreeClean());

    <span class="hljs-comment">// 2. 通过 getUnpublishedPackages 筛除 private 为 true 的 package && 拿到需要发布的pkg</span>
    <span class="hljs-comment">// 这一步用了 npm config 里面的快照来做对比</span>
    chain = chain.then(<span class="hljs-function">() =></span> getUnpublishedPackages(<span class="hljs-built_in">this</span>.packageGraph, <span class="hljs-built_in">this</span>.conf.snapshot));
    
    <span class="hljs-comment">// 3. 验证结果符合预期否</span>
    chain = chain.then(<span class="hljs-function"><span class="hljs-params">unpublished</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (!unpublished.length) &#123;
        <span class="hljs-built_in">this</span>.logger.notice(<span class="hljs-string">"from-package"</span>, <span class="hljs-string">"No unpublished release found"</span>);
      &#125;

      <span class="hljs-keyword">return</span> unpublished;
    &#125;);

    <span class="hljs-comment">// 4. updateVersions 存需要发布的包名以及发布的版本，返回结果</span>
    <span class="hljs-keyword">return</span> chain.then(<span class="hljs-function"><span class="hljs-params">updates</span> =></span> &#123;
      <span class="hljs-keyword">const</span> updatesVersions = updates.map(<span class="hljs-function"><span class="hljs-params">node</span> =></span> [node.name, node.version]);

      <span class="hljs-keyword">return</span> &#123;
        updates,
        updatesVersions,
        <span class="hljs-attr">needsConfirmation</span>: <span class="hljs-literal">true</span>,
      &#125;;
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一步主要是在 <code>getUnpublishedPackages</code> 这一步筛选出需要更新的 packages，这里 lerna 作者使用了自己封装的 pacote 库来去做一些关于版本的比对，从而得到需要更新的 packages，这里有想了解的可以自行去阅读一下，不做过多赘述。</p>
<h3 data-id="heading-4"><code>--canary</code></h3>
<p>这一步执行的入口函数是 <code>detectCanaryVersions</code> ，直接看执行过程：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">detectCanaryVersions</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-comment">// 初始化处理参数</span>
    <span class="hljs-keyword">const</span> &#123; cwd &#125; = <span class="hljs-built_in">this</span>.execOpts;
    <span class="hljs-keyword">const</span> &#123;
      bump = <span class="hljs-string">"prepatch"</span>,
      preid = <span class="hljs-string">"alpha"</span>,
      ignoreChanges,
      forcePublish,
      includeMergedTags,
    &#125; = <span class="hljs-built_in">this</span>.options;
    <span class="hljs-keyword">const</span> release = bump.startsWith(<span class="hljs-string">"pre"</span>) ? bump.replace(<span class="hljs-string">"release"</span>, <span class="hljs-string">"patch"</span>) : <span class="hljs-string">`pre<span class="hljs-subst">$&#123;bump&#125;</span>`</span>;

    <span class="hljs-keyword">let</span> chain = <span class="hljs-built_in">Promise</span>.resolve();

    <span class="hljs-comment">// 1. 验证当前 git 区是否干净</span>
    chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.verifyWorkingTreeClean());

    <span class="hljs-comment">// 2. 找到自上次来修改过的 packages 同时筛掉 private 为 false 的 pkg</span>
    chain = chain.then(<span class="hljs-function">() =></span>
      collectUpdates(<span class="hljs-built_in">this</span>.packageGraph.rawPackageList, <span class="hljs-built_in">this</span>.packageGraph, <span class="hljs-built_in">this</span>.execOpts, &#123;
        <span class="hljs-attr">bump</span>: <span class="hljs-string">"prerelease"</span>,
        <span class="hljs-attr">canary</span>: <span class="hljs-literal">true</span>,
        ignoreChanges,
        forcePublish,
        includeMergedTags,
      &#125;).filter(<span class="hljs-function"><span class="hljs-params">node</span> =></span> !node.pkg.private)
    );

    <span class="hljs-keyword">const</span> makeVersion = <span class="hljs-function"><span class="hljs-params">fallback</span> =></span> <span class="hljs-function">(<span class="hljs-params">&#123; lastVersion = fallback, refCount, sha &#125;</span>) =></span> &#123;
      <span class="hljs-comment">// --canary 会通过上一次的 version 来计算出这次的 version </span>
      <span class="hljs-keyword">const</span> nextVersion = semver.inc(lastVersion.replace(<span class="hljs-built_in">this</span>.tagPrefix, <span class="hljs-string">""</span>), release.replace(<span class="hljs-string">"pre"</span>, <span class="hljs-string">""</span>));
      <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;nextVersion&#125;</span>-<span class="hljs-subst">$&#123;preid&#125;</span>.<span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.max(<span class="hljs-number">0</span>, refCount - <span class="hljs-number">1</span>)&#125;</span>+<span class="hljs-subst">$&#123;sha&#125;</span>`</span>;
    &#125;;

    <span class="hljs-comment">// 3. 根据不同的 mode 计算出包及版本相关参数</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.project.isIndependent()) &#123;
      <span class="hljs-comment">// 独立发包模式</span>
      chain = chain.then(<span class="hljs-function"><span class="hljs-params">updates</span> =></span>
        <span class="hljs-comment">// pMap 是个链式执行过程，上一步的结果会给到下一步</span>
        pMap(updates, <span class="hljs-function"><span class="hljs-params">node</span> =></span>
          <span class="hljs-comment">// 根据 tag 匹配出需要发布的包</span>
          describeRef(
            &#123;
              <span class="hljs-attr">match</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;node.name&#125;</span>@*`</span>,
              cwd,
            &#125;,
            includeMergedTags
          )
             <span class="hljs-comment">// 通过上面的 makeVersion 方法来计算发布的 canary 版本</span>
            .then(makeVersion(node.version))
             <span class="hljs-comment">// 返回出去,这里实际上就是个 updateVerions 数组</span>
            .then(<span class="hljs-function"><span class="hljs-params">version</span> =></span> [node.name, version])
        ).then(<span class="hljs-function"><span class="hljs-params">updatesVersions</span> =></span> (&#123;
          updates,
          updatesVersions,
        &#125;))
      );
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 固定的模式，那么所有的包都会使用一个版本(lerna.json 里面的版本)</span>
      chain = chain.then(<span class="hljs-function"><span class="hljs-params">updates</span> =></span>
        describeRef(
          &#123;
            <span class="hljs-attr">match</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.tagPrefix&#125;</span>*.*.*`</span>,
            cwd,
          &#125;,
          includeMergedTags
        )
          <span class="hljs-comment">// 只用一个 version 去进行计算</span>
          .then(makeVersion(<span class="hljs-built_in">this</span>.project.version))
          .then(<span class="hljs-function"><span class="hljs-params">version</span> =></span> updates.map(<span class="hljs-function"><span class="hljs-params">node</span> =></span> [node.name, version]))
          .then(<span class="hljs-function"><span class="hljs-params">updatesVersions</span> =></span> (&#123;
            updates,
            updatesVersions,
          &#125;))
      );
    &#125;

  <span class="hljs-comment">// 4. 返回结果</span>
    <span class="hljs-keyword">return</span> chain.then(<span class="hljs-function">(<span class="hljs-params">&#123; updates, updatesVersions &#125;</span>) =></span> (&#123;
      updates,
      updatesVersions,
      <span class="hljs-attr">needsConfirmation</span>: <span class="hljs-literal">true</span>,
    &#125;));
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相比较于上面两步， <code>--canary</code> 的处理过程或许看上去要复杂一些，其实不然，根据上面代码注释中的内容可以比较清晰的看到整个执行流程，不过多了几种特殊情况需要去做一些判断，其中比较复杂的第三步，是需要通过 tag 得到一些相关的信息，需要更新的包，然后针对这些包现有的版本去做一些计算，可以参考上面的 <code>makeVersion</code> 方法，这里就根据 lerna 的 mode 分为了两种情况。</p>
<p>其中这里第二步还用到了在 lerna version 中收集变更的包的方法：<code>collectUpdates</code>。具体的执行机制可以参考我的上一篇关于 lerna version 的文章。</p>
<h3 data-id="heading-5">bump version</h3>
<p>如果不带参数的话，那么这一步就会直接执行一个 lerna version 的过程，一般 lerna publish 的预期行为是这样：</p>
<pre><code class="hljs language-js copyable" lang="js">chain = chain.then(<span class="hljs-function">() =></span> versionCommand(<span class="hljs-built_in">this</span>.argv));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>lerna version 的具体执行机制可以参考我的上一篇文章。</p>
<p>看完这几种情况之后再回到开头，再回顾一下 initialize 这一步最后对结果的一个处理过程，大致 initialize 的一个流程就这样结束了。</p>
<p>最后总结一下 lerna publish 的初始化过程，主要就是根据不同的发包情况，然后计算出需要发布的包的信息，例如包名称和更新版本。用于下一步发包的 execute 做准备。</p>
<h2 data-id="heading-6">执行(execute)</h2>
<p><code>lerna publish</code> 的最后一步即发包的过程就是在这里完成，代码结构为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">execute</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> chain = <span class="hljs-built_in">Promise</span>.resolve();

    <span class="hljs-comment">// 1. 验证 npm 源、权限，项目的 License 之内</span>
    chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.prepareRegistryActions());
    chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.prepareLicenseActions());

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.options.canary) &#123;
      <span class="hljs-comment">// 如果是测试包，更新到测试包的 version</span>
      chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.updateCanaryVersions());
    &#125;

    <span class="hljs-comment">// 2. 更新本地依赖包版本 && gitHead</span>
    chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.resolveLocalDependencyLinks());
    chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.annotateGitHead());
 
    <span class="hljs-comment">// 3. 更新写入本地</span>
    chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.serializeChanges());
 
    <span class="hljs-comment">// 4. 对 package pack</span>
    chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.packUpdated());
  
    <span class="hljs-comment">// 5. 发布包</span>
    chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.publishPacked());

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.gitReset) &#123;
      <span class="hljs-comment">// 设置了 --no-git-reset 会把 working tree 的版本修改重置</span>
      <span class="hljs-comment">// lerna 每次发包都会把更新的 package.json 的 version 的修改提交到 git 上去</span>
      <span class="hljs-comment">// 如果发测试包，这可能是没必要，因此可以用这个选项把修改 reset 掉</span>
      chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.resetChanges());
    &#125;

   <span class="hljs-comment">// 做后续的处理</span>
    <span class="hljs-keyword">return</span> chain.then(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 发布包的数量</span>
      <span class="hljs-keyword">const</span> count = <span class="hljs-built_in">this</span>.packagesToPublish.length;
      <span class="hljs-comment">// 发布包的名称以及版本，用于输出展示</span>
      <span class="hljs-keyword">const</span> message = <span class="hljs-built_in">this</span>.packagesToPublish.map(<span class="hljs-function"><span class="hljs-params">pkg</span> =></span> <span class="hljs-string">` - <span class="hljs-subst">$&#123;pkg.name&#125;</span>@<span class="hljs-subst">$&#123;pkg.version&#125;</span>`</span>);

      output(<span class="hljs-string">"Successfully published:"</span>);
      output(message.join(os.EOL));

      <span class="hljs-built_in">this</span>.logger.success(<span class="hljs-string">"published"</span>, <span class="hljs-string">"%d %s"</span>, count, count === <span class="hljs-number">1</span> ? <span class="hljs-string">"package"</span> : <span class="hljs-string">"packages"</span>);
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>execute</code> 是  <code>lerna publish</code> 的主要部分了，这一步的相对而言信息量比较巨大，我接下来会将上面的步骤拆一拆，一步一步来讲解 <code>execute</code> 这一步是怎么完成 lerna 发包的整个过程的。</p>
<p>首先可以看到上面代码中，我通过注释将这个步骤分成了六步：</p>
<h4 data-id="heading-7">1. 验证 npm && 项目license</h4>
<p>首先上面可以看到，这一步分为两个方法，一步是做 npm 相关的验证：<code>prepareRegistryActions</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">prepareRegistryActions</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> chain = <span class="hljs-built_in">Promise</span>.resolve();
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.conf.get(<span class="hljs-string">"registry"</span>) !== <span class="hljs-string">"https://registry.npmjs.org/"</span>) &#123;
      <span class="hljs-comment">// 这里的 registry 如果 url 是三方的例如公司的源，这里会跳过后面的检查</span>
      <span class="hljs-keyword">return</span> chain;
    &#125;

      <span class="hljs-comment">// --no-verify-access 停止校验，默认会校验</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.verifyAccess) &#123;
      <span class="hljs-comment">// 拿用户的 npm username，拿不到在 getNpmUsername 会抛错</span>
      chain = chain.then(<span class="hljs-function">() =></span> getNpmUsername(<span class="hljs-built_in">this</span>.conf.snapshot));
      <span class="hljs-comment">// 根据 username 对要发布的包做个鉴权</span>
      chain = chain.then(<span class="hljs-function"><span class="hljs-params">username</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (username) &#123;
          <span class="hljs-keyword">return</span> verifyNpmPackageAccess(<span class="hljs-built_in">this</span>.packagesToPublish, username, <span class="hljs-built_in">this</span>.conf.snapshot);
        &#125;
      &#125;);

      <span class="hljs-comment">// 校验用户是否需进行 2fa 的验证 -- 安全验证相关</span>
      chain = chain.then(<span class="hljs-function">() =></span> getTwoFactorAuthRequired(<span class="hljs-built_in">this</span>.conf.snapshot));
      chain = chain.then(<span class="hljs-function"><span class="hljs-params">isRequired</span> =></span> &#123;
        <span class="hljs-comment">// 记录一下</span>
        <span class="hljs-built_in">this</span>.twoFactorAuthRequired = isRequired;
      &#125;);
    &#125;

    <span class="hljs-keyword">return</span> chain;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>prepareRegistryActions</code> 执行时会先去校验 registry，如果是第三方的 registry，会停止校验，用户在发包设置了 <code>no-verify-access</code> 就不进行后面校验，默认会校验。</p>
<p>校验过程是首先通过 <code>getNpmUsername</code> 去拿到用户的 username，这里是通过 npm 提供的相关接口来获取，具体流程可以自行参考。拿到 username 之后根据 username 以及本次 publish 中需要发布的包的信息去做一个鉴权，判断用户是否用该包的读写发包权限，没有就会抛错，最后一步是个 2fa 的验证，一般 npm 包都不会开启，主要是为了安全作用做二次验证使用，这里不做具体讲解。</p>
<p>下面在看 license 的校验过程，方法是 <code>prepareLicenseActions</code> ：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">prepareLicenseActions</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve()
      <span class="hljs-comment">// 通过 glob 的方式去找到待发布的包中没有 licenses 的</span>
      .then(<span class="hljs-function">() =></span> getPackagesWithoutLicense(<span class="hljs-built_in">this</span>.project, <span class="hljs-built_in">this</span>.packagesToPublish))
      .then(<span class="hljs-function"><span class="hljs-params">packagesWithoutLicense</span> =></span> &#123;
      <span class="hljs-comment">// 对于没有 liecense 的包会打个 warnning 出来</span>
        <span class="hljs-keyword">if</span> (packagesWithoutLicense.length && !<span class="hljs-built_in">this</span>.project.licensePath) &#123;
          <span class="hljs-built_in">this</span>.packagesToBeLicensed = [];

          <span class="hljs-keyword">const</span> names = packagesWithoutLicense.map(<span class="hljs-function"><span class="hljs-params">pkg</span> =></span> pkg.name);
          <span class="hljs-keyword">const</span> noun = names.length > <span class="hljs-number">1</span> ? <span class="hljs-string">"Packages"</span> : <span class="hljs-string">"Package"</span>;
          <span class="hljs-keyword">const</span> verb = names.length > <span class="hljs-number">1</span> ? <span class="hljs-string">"are"</span> : <span class="hljs-string">"is"</span>;
          <span class="hljs-keyword">const</span> list =
            names.length > <span class="hljs-number">1</span>
              ? <span class="hljs-string">`<span class="hljs-subst">$&#123;names.slice(<span class="hljs-number">0</span>, -<span class="hljs-number">1</span>).join(<span class="hljs-string">", "</span>)&#125;</span><span class="hljs-subst">$&#123;names.length > <span class="hljs-number">2</span> ? <span class="hljs-string">","</span> : <span class="hljs-string">""</span>&#125;</span> and <span class="hljs-subst">$&#123;
                  names[names.length - <span class="hljs-number">1</span>] <span class="hljs-regexp">/* oxford commas _are_ that important */</span>
                &#125;</span>`</span>
              : names[<span class="hljs-number">0</span>];
          <span class="hljs-built_in">this</span>.logger.warn(
            <span class="hljs-string">"ENOLICENSE"</span>,
            <span class="hljs-string">"%s %s %s missing a license.\n%s\n%s"</span>,
            noun,
            list,
            verb,
            <span class="hljs-string">"One way to fix this is to add a LICENSE.md file to the root of this repository."</span>,
            <span class="hljs-string">"See https://choosealicense.com for additional guidance."</span>
          );
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// 记录一下</span>
          <span class="hljs-built_in">this</span>.packagesToBeLicensed = packagesWithoutLicense;
        &#125;
      &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一步并不会对主要流程有什么影响，主要就是找目前待发布的包中没有 license 的，然后给个 warnning 提示，这里找的方式使用过 lerna 自己构造的 project graph 去筛待发布包中不存在 liecense 文件的路径，想了解具体过程参考 <code>getPackagesWithoutLicense</code>。</p>
<h4 data-id="heading-8">2. 更新本地依赖版本 && 待发布包 gitHead</h4>
<p>可以你会对更新本地依赖版本这一步可能会有些迷惑，这里举个例子来解释一下，在 lerna 中，如果 workspaces 之前存在依赖的话，在这次发包中，例如 A 这个包依赖了 B，B 在这次发包中版本升级了，那么这里 A 里面依赖的 B 也要更新到对应的版本。</p>
<p>来看一下这一步：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">resolveLocalDependencyLinks</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 先找到依赖过本地包的包</span>
    <span class="hljs-comment">// lerna 中 A, B 都是 workspace， A 依赖 B 引入的时候是通过 symlink 引入的</span>
    <span class="hljs-comment">// 因此这里找 B 的依赖包只用判断 A 这里 resolved 的是不是个目录就行</span>
    <span class="hljs-keyword">const</span> updatesWithLocalLinks = <span class="hljs-built_in">this</span>.updates.filter(<span class="hljs-function"><span class="hljs-params">node</span> =></span>
      <span class="hljs-built_in">Array</span>.from(node.localDependencies.values()).some(<span class="hljs-function"><span class="hljs-params">resolved</span> =></span> resolved.type === <span class="hljs-string">"directory"</span>)
    );

    <span class="hljs-comment">// 拿到上一步结果之后，就把对应的更新写入 A</span>
    <span class="hljs-keyword">return</span> pMap(updatesWithLocalLinks, <span class="hljs-function"><span class="hljs-params">node</span> =></span> &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [depName, resolved] <span class="hljs-keyword">of</span> node.localDependencies) &#123;
        <span class="hljs-comment">// 注意这里 lerna 是不会处理 B: ../../file/xxx 这种引入情况的</span>
        <span class="hljs-keyword">const</span> depVersion = <span class="hljs-built_in">this</span>.updatesVersions.get(depName) || <span class="hljs-built_in">this</span>.packageGraph.get(depName).pkg.version;
        <span class="hljs-comment">// 以 A 为例子，这里 A 的 pkg.json 中的B 就要更新到发包的版本</span>
        node.pkg.updateLocalDependency(resolved, depVersion, <span class="hljs-built_in">this</span>.savePrefix);
      &#125;
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里涉及到的一些操作方法，都是来自于 lerna 构建的 project graph，这部分可以去参考一下 lerna core 中源码。</p>
<p>这里的 gitHead 是一个 hash 值，用户可以通过 --git-head 来自行指定，如果不指定的话，lerna 这里会默认帮你取当前 commit 的 hash 值，即通过 <code>git rev-parse HEAD</code> 来获取，一般 gitHead 结合 <code>from-package</code> 来使用，先看看代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">annotateGitHead</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// 用户如果没有默认指定就使用最近的 commit hash 值</span>
      <span class="hljs-comment">// getCurrentSHA 就是执行了一次 git rev-parse HEAD</span>
      <span class="hljs-keyword">const</span> gitHead = <span class="hljs-built_in">this</span>.options.gitHead || getCurrentSHA(<span class="hljs-built_in">this</span>.execOpts);
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> pkg <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.packagesToPublish) &#123;
        <span class="hljs-comment">// gitHead 是用来关联 package 和 git 记录</span>
        <span class="hljs-comment">// npm publish 正常情况下需要该字段</span>
        pkg.set(<span class="hljs-string">"gitHead"</span>, gitHead);
      &#125;
    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    &#125;
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用 <code>from-package</code> 的方式进行发包的时候，会把这个 githead 字段写在 <code>package.json</code> 里面。</p>
<h4 data-id="heading-9">3.  更新写入本地</h4>
<p>这一步就是将第二步的一些更新直接写到 lerna 中对应项目里面去，即写到磁盘里面，主要的方法为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">serializeChanges</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-keyword">return</span> pMap(<span class="hljs-built_in">this</span>.packagesToPublish, <span class="hljs-function"><span class="hljs-params">pkg</span> =></span> pkg.serialize());
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 <code>pkg.serialize()</code> 方法，是可以在 lerna 的 core 中找到的，主要作用就是将相关的更新写入本地磁盘：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">serialize</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-comment">// 这里的 writePkg 封装了 write-package-json 这个方法</span>
  <span class="hljs-keyword">return</span> writePkg(<span class="hljs-built_in">this</span>.manifestLocation, <span class="hljs-built_in">this</span>[PKG]).then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">4. package pack</h4>
<p>在讲解之前，我们得先知道 <code>npm pack</code> 这个操作是干什么的，它会打包当前的文件夹内容打包成一个 tar 包，我们在执行 npm publish 的时候会经常看到这个操作：</p>
<img alt="image-20210401234911209" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ddfbb9e8ee943fea0042069883c3707~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>不过 npm publish 帮我们封装了这个过程，lerna publish 中也会有这个过程，这已经是发包前的最后一个操作了，具体可参考代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">packUpdated</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> chain = <span class="hljs-built_in">Promise</span>.resolve();
  
    <span class="hljs-comment">// ... </span>
    <span class="hljs-keyword">const</span> opts = <span class="hljs-built_in">this</span>.conf.snapshot;
    <span class="hljs-keyword">const</span> mapper = pPipe(
      [
        <span class="hljs-comment">// packDirectory 会给对应 pkg 的文件夹打个 tar 包出来</span>
        <span class="hljs-comment">// 类似于上面的 npm pack</span>
        <span class="hljs-function"><span class="hljs-params">pkg</span> =></span>
          pulseTillDone(packDirectory(pkg, pkg.location, opts)).then(<span class="hljs-function"><span class="hljs-params">packed</span> =></span> &#123;
            pkg.packed = packed;
            <span class="hljs-keyword">return</span> pkg.refresh();
          &#125;),
      ].filter(<span class="hljs-built_in">Boolean</span>)
    );

   <span class="hljs-comment">// 这里会按照拓扑序列去对要发布的包进行 pack</span>
    chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.topoMapPackages(mapper));

    <span class="hljs-keyword">return</span> pFinally(chain, <span class="hljs-function">() =></span> tracker.finish());
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一步首先可以参考 <code>topoMapPackages</code> 这个方法，他会按照拓扑顺序去对需要更新的包进行 pack，这里 publish 因为涉及到包之间的一些依赖关系，因此只能按照拓扑的顺序去执行，<code>this.packagesToPublish</code> 里面存的是待发布的包：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">topoMapPackages</span>(<span class="hljs-params">mapper</span>)</span> &#123;
    <span class="hljs-comment">// 这里是作者的一个注释：</span>
    <span class="hljs-comment">// we don't respect --no-sort here, sorry</span>
    <span class="hljs-keyword">return</span> runTopologically(<span class="hljs-built_in">this</span>.packagesToPublish, mapper, &#123;
      <span class="hljs-attr">concurrency</span>: <span class="hljs-built_in">this</span>.concurrency,
      <span class="hljs-attr">rejectCycles</span>: <span class="hljs-built_in">this</span>.options.rejectCycles,
      <span class="hljs-attr">graphType</span>: <span class="hljs-built_in">this</span>.options.graphType === <span class="hljs-string">"all"</span> ? <span class="hljs-string">"allDependencies"</span> : <span class="hljs-string">"dependencies"</span>,
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此这里会按照拓扑顺序去对要发布的包进行打包成 tar 包的操作，具体执行方法是 <code>packDirectory</code> 这个方法，这个方法我只贴一下打包的那一段逻辑，还有一些其他的预处理逻辑做了一下删除：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> tar = <span class="hljs-built_in">require</span>(<span class="hljs-string">"tar"</span>);
<span class="hljs-keyword">const</span> packlist = <span class="hljs-built_in">require</span>(<span class="hljs-string">"npm-packlist"</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">packDirectory</span>(<span class="hljs-params">_pkg, dir, _opts</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">let</span> chain = <span class="hljs-built_in">Promise</span>.resolve();
  <span class="hljs-comment">// 拿到待发布 pkg 的 目录信息</span>
  chain = chain.then(<span class="hljs-function">() =></span> packlist(&#123; <span class="hljs-attr">path</span>: pkg.contents &#125;));
  <span class="hljs-comment">// 对目录下面的一些文件夹打包</span>
  chain = chain.then(<span class="hljs-function"><span class="hljs-params">files</span> =></span>
    <span class="hljs-comment">// 具体参数去参考 tar 这个 npm 包</span>
    tar.create(
      &#123;
        <span class="hljs-attr">cwd</span>: pkg.contents,
        <span class="hljs-attr">prefix</span>: <span class="hljs-string">"package/"</span>,
        <span class="hljs-attr">portable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">mtime</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-string">"1985-10-26T08:15:00.000Z"</span>),
        <span class="hljs-attr">gzip</span>: <span class="hljs-literal">true</span>,
      &#125;,
      files.map(<span class="hljs-function"><span class="hljs-params">f</span> =></span> <span class="hljs-string">`./<span class="hljs-subst">$&#123;f&#125;</span>`</span>)
    )
  );
  <span class="hljs-comment">// 将文件处理成 stream 形式写到一个临时目录下面</span>
  <span class="hljs-comment">// 发布完了会删除</span>
  chain = chain.then(<span class="hljs-function"><span class="hljs-params">stream</span> =></span> tempWrite(stream, getTarballName(pkg)));
  chain = chain.then(<span class="hljs-function"><span class="hljs-params">tarFilePath</span> =></span>
    getPacked(pkg, tarFilePath).then(<span class="hljs-function"><span class="hljs-params">packed</span> =></span>
      <span class="hljs-built_in">Promise</span>.resolve()
        .then(<span class="hljs-function">() =></span> runLifecycle(pkg, <span class="hljs-string">"postpack"</span>, opts))
        .then(<span class="hljs-function">() =></span> packed)
    )
  );
  <span class="hljs-keyword">return</span> chain;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">5. Package publish</h4>
<p>在上一步完成了待发布包的打包操作之后，这一步就是 lerna publish 整个流程的最后一步了！</p>
<p>这一步会将上一次打包的内容直接发布出去，先来看一下代码：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">publishPacked</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> chain = <span class="hljs-built_in">Promise</span>.resolve();

    <span class="hljs-comment">// 前面说过的 2fa 2次验证，这里会验证一下</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.twoFactorAuthRequired) &#123;
      chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.requestOneTimePassword());
    &#125;

    <span class="hljs-keyword">const</span> opts = <span class="hljs-built_in">Object</span>.assign(<span class="hljs-built_in">this</span>.conf.snapshot, &#123;
      <span class="hljs-comment">// 设置了 tempTag 就先用 lerna-temp</span>
      <span class="hljs-attr">tag</span>: <span class="hljs-built_in">this</span>.options.tempTag ? <span class="hljs-string">"lerna-temp"</span> : <span class="hljs-built_in">this</span>.conf.get(<span class="hljs-string">"tag"</span>),
    &#125;);

    <span class="hljs-keyword">const</span> mapper = pPipe(
      [
        <span class="hljs-function"><span class="hljs-params">pkg</span> =></span> &#123;
          <span class="hljs-comment">// 拿到 pkg 上一次发布的 tag，通过 semver.prerelease 进行判断</span>
          <span class="hljs-keyword">const</span> preDistTag = <span class="hljs-built_in">this</span>.getPreDistTag(pkg);
          <span class="hljs-comment">// 取一下 tag，一般这里会取 opts.tag，针对于每个包的情况不同</span>
          <span class="hljs-keyword">const</span> tag = !<span class="hljs-built_in">this</span>.options.tempTag && preDistTag ? preDistTag : opts.tag;
          <span class="hljs-comment">// 这里 rewrite 一下 tag</span>
          <span class="hljs-keyword">const</span> pkgOpts = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, opts, &#123; tag &#125;);

          <span class="hljs-comment">// 发布包这个操作通过 npmPublish 这个过程来完成</span>
          <span class="hljs-keyword">return</span> pulseTillDone(npmPublish(pkg, pkg.packed.tarFilePath, pkgOpts, <span class="hljs-built_in">this</span>.otpCache)).then(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">return</span> pkg;
          &#125;);
        &#125;
      ].filter(<span class="hljs-built_in">Boolean</span>)
    );

    <span class="hljs-comment">// 这里和上一步 pack 一样，按照拓扑执行</span>
    chain = chain.then(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.topoMapPackages(mapper));

    <span class="hljs-keyword">return</span> pFinally(chain, <span class="hljs-function">() =></span> tracker.finish());
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上一步讲了 <code>topoMapPackages</code> 这个方法，这里同样的，它会按照拓扑顺序去发布待发布的 pkg。</p>
<p>在 <code>npmPublish</code> 这个方法中，会将前面打包的 pkg 的 tar 包 publish 到 npm 上面去，这里用的是 lerna 作者自己的一个包，感兴趣的可以去 npm 上搜一下：<code>@evocateur/libnpmpublish</code></p>
<p>这个包可以不用担心 tarball 打包自于哪个 pkg，只要你有个 tarball 它会帮你直接上传到 npm 上面去来完成一次发布，具体的内容可以在 npm 中找到。</p>
<p>这里因为引入了一些外部包加上这里有太多的边界条件处理，这里就不具体去看 <code>npmPublish</code> 这个方法了，贴上发布的那部分代码，可以参考一下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; publish &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"@evocateur/libnpmpublish"</span>);

<span class="hljs-keyword">return</span> otplease(<span class="hljs-function"><span class="hljs-params">innerOpts</span> =></span> publish(manifest, tarData, innerOpts), opts, otpCache).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-comment">// re-throw to break chain upstream</span>
  <span class="hljs-keyword">throw</span> err;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么再走到这一步结束之后，基本上整个 lerna 的发包流程都走完了。</p>
<p>后续的一些收尾工作的处理，可以再拉回 执行(execute) 这一节开头的代码分析那里。</p>
<h3 data-id="heading-12">总结</h3>
<p>本文从源码角度剖析了一下 lerna publish 的执行机制，对于一些边界的 corner case 有些删减，按照主线讲解了 lerna publish 是怎么完成 lerna monorepo 中的整个发包流程操作的。希望本系列的文章能对你有所帮助。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            