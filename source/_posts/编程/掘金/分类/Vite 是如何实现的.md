
---
title: 'Vite 是如何实现的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79df687efb934e2e9fb8ed8d8ef6895d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 22:59:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79df687efb934e2e9fb8ed8d8ef6895d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<p>Vite 是由 Vue 作者尤雨溪开发的 Web 开发工具，尤雨溪在微博上推广时对 Vite 做了简短介绍：</p>
<blockquote>
<p>Vite，一个基于浏览器原生 ES imports 的开发服务器。利用浏览器去解析 imports，在服务器端按需编译返回，完全跳过了打包这个概念，服务器随起随用。同时不仅有 Vue 文件支持，还搞定了热更新，而且热更新的速度不会随着模块增多而变慢。针对生产环境则可以把同一份代码用 Rollup 打包。虽然现在还比较粗糙，但这个方向我觉得是有潜力的，做得好可以彻底解决改一行代码等半天热更新的问题。</p>
</blockquote>
<p>我们可以从这段话中提取一些关键信息</p>
<ul>
<li>Vite 基于 ESM，因此实现了快速启动和即时模块热更新能力；</li>
<li>Vite 在服务端实现了按需编译。</li>
</ul>
<p>所以可以直白一些来讲：<strong>Vite 在开发环境下并没有打包和构建过程。</strong></p>
<p>开发者在代码中写到的 ESM 导入语法会直接发送给服务器，而服务器也直接将 ESM 模块内容运行处理后，下发给浏览器。接着，现代浏览器通过解析 script module，对每一个 import 到的模块进行 HTTP 请求，服务器继续对这些 HTTP 请求进行处理并响应。</p>
<h2 data-id="heading-0">Vite 实现原理解读</h2>
<h3 data-id="heading-1">环境搭建</h3>
<p>Vite 思想比较容易理解，实现起来也并不复杂。接下来，我们来对 Vite 源码进行分析</p>
<p>首先，我们打造一个学习环境，创建一个基于 Vite 的应用，并启动：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> yarn global add vite</span>
<span class="hljs-meta">$</span><span class="bash"> npm init vite-app vite-app</span>
<span class="hljs-meta">
$</span><span class="bash"> <span class="hljs-built_in">cd</span> vite-app</span>
<span class="hljs-meta">
$</span><span class="bash"> yarn</span>
<span class="hljs-meta">
$</span><span class="bash"> yarn dev</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>会得到如下图所示的目录结构：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79df687efb934e2e9fb8ed8d8ef6895d~tplv-k3u1fbpfcp-zoom-1.image" alt="目录结构" loading="lazy" referrerpolicy="no-referrer"></p>
<p>启动项目：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> yarn dev</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中浏览器请求：**<a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A3000%2F**%25EF%25BC%258C%25E5%25BE%2597%25E5%2588%25B0%25E7%259A%2584%25E5%2586%2585%25E5%25AE%25B9%25E5%258D%25B3%25E6%2598%25AF%25E6%2588%2591%25E4%25BB%25AC%25E5%25BA%2594%25E7%2594%25A8%25E9%25A1%25B9%25E7%259B%25AE%25E4%25B8%25AD%25E7%259A%2584" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:3000/**%EF%BC%8C%E5%BE%97%E5%88%B0%E7%9A%84%E5%86%85%E5%AE%B9%E5%8D%B3%E6%98%AF%E6%88%91%E4%BB%AC%E5%BA%94%E7%94%A8%E9%A1%B9%E7%9B%AE%E4%B8%AD%E7%9A%84" ref="nofollow noopener noreferrer">http://localhost:3000/**，得到的内容即是我们应用项目中的</a> index.html 内容。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a28292f70054a0bb9e1e1d159c46111~tplv-k3u1fbpfcp-zoom-1.image" alt="浏览器效果" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">入口源码</h3>
<p>拉取<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite" ref="nofollow noopener noreferrer">源码</a>，在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2F73344a9560323008cc0b5ef6994019e2a0354141%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fcli.ts%23L80" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/73344a9560323008cc0b5ef6994019e2a0354141/packages/vite/src/node/cli.ts#L80" ref="nofollow noopener noreferrer">开命令行实现部分</a>，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cli
  .command(<span class="hljs-string">'[root]'</span>) <span class="hljs-comment">// default command</span>
  .alias(<span class="hljs-string">'serve'</span>)
  .option(<span class="hljs-string">'--host [host]'</span>, <span class="hljs-string">`[string] specify hostname`</span>)
  .option(<span class="hljs-string">'--port <port>'</span>, <span class="hljs-string">`[number] specify port`</span>)
  .option(<span class="hljs-string">'--https'</span>, <span class="hljs-string">`[boolean] use TLS + HTTP/2`</span>)
  .option(<span class="hljs-string">'--open [path]'</span>, <span class="hljs-string">`[boolean | string] open browser on startup`</span>)
  .option(<span class="hljs-string">'--cors'</span>, <span class="hljs-string">`[boolean] enable CORS`</span>)
  .option(<span class="hljs-string">'--strictPort'</span>, <span class="hljs-string">`[boolean] exit if specified port is already in use`</span>)
  .option(<span class="hljs-string">'-m, --mode <mode>'</span>, <span class="hljs-string">`[string] set env mode`</span>)
  .option(
    <span class="hljs-string">'--force'</span>,
    <span class="hljs-string">`[boolean] force the optimizer to ignore the cache and re-bundle`</span>
  )
  .action(<span class="hljs-keyword">async</span> (root: string, <span class="hljs-attr">options</span>: ServerOptions & GlobalCLIOptions) => &#123;
    <span class="hljs-comment">// output structure is preserved even after bundling so require()</span>
    <span class="hljs-comment">// is ok here</span>
    <span class="hljs-keyword">const</span> &#123; createServer &#125; = <span class="hljs-keyword">await</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./server'</span>)
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> server = <span class="hljs-keyword">await</span> createServer(&#123;
        root,
        <span class="hljs-attr">base</span>: options.base,
        <span class="hljs-attr">mode</span>: options.mode,
        <span class="hljs-attr">configFile</span>: options.config,
        <span class="hljs-attr">logLevel</span>: options.logLevel,
        <span class="hljs-attr">clearScreen</span>: options.clearScreen,
        <span class="hljs-attr">server</span>: cleanOptions(options) <span class="hljs-keyword">as</span> ServerOptions
      &#125;)
      <span class="hljs-keyword">await</span> server.listen()
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      createLogger(options.logLevel).error(
        chalk.red(<span class="hljs-string">`error when starting dev server:\n<span class="hljs-subst">$&#123;e.stack&#125;</span>`</span>)
      )
      process.exit(<span class="hljs-number">1</span>)
    &#125;
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <strong>createServer</strong> 来启动一个 http 服务，来实现对浏览器请求的响应。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; createServer &#125; = <span class="hljs-keyword">await</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./server'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fserver%2Findex.ts%23L302" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/main/packages/vite/src/node/server/index.ts#L302" ref="nofollow noopener noreferrer">createServer</a>方法的实现，代码如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createServer</span>(<span class="hljs-params">inlineConfig</span>) </span>&#123;
    <span class="hljs-comment">// 配置文件处理</span>
    <span class="hljs-keyword">const</span> config = <span class="hljs-keyword">await</span> resolveConfig(inlineConfig, <span class="hljs-string">'serve'</span>, <span class="hljs-string">'development'</span>)
    <span class="hljs-keyword">const</span> root = config.root
    <span class="hljs-keyword">const</span> serverConfig = config.server
    <span class="hljs-keyword">const</span> httpsOptions = <span class="hljs-keyword">await</span> resolveHttpsConfig(config)
    <span class="hljs-keyword">let</span> &#123; middlewareMode &#125; = serverConfig
    <span class="hljs-comment">// 以中间件模式创建 vite 服务器，不使用 vite 创建的服务器</span>
    <span class="hljs-keyword">if</span> (middlewareMode === <span class="hljs-literal">true</span>) &#123;
      middlewareMode = <span class="hljs-string">'ssr'</span>
    &#125;
  
    <span class="hljs-keyword">const</span> middlewares = connect()
    <span class="hljs-comment">// 创建一个 http 实例，注意，这里如果 middlewareMode = 'ssr' 则使用中间件来创建服务器</span>
    <span class="hljs-keyword">const</span> httpServer = middlewareMode
      ? <span class="hljs-literal">null</span>
        : <span class="hljs-keyword">await</span> resolveHttpServer(serverConfig, middlewares, httpsOptions)
    <span class="hljs-comment">// HMR 连接</span>
    <span class="hljs-keyword">const</span> ws = createWebSocketServer(httpServer, config, httpsOptions)
  
    <span class="hljs-keyword">const</span> &#123; ignored = [], ...watchOptions &#125; = serverConfig.watch || &#123;&#125;
    <span class="hljs-comment">// 文件监听</span>
    <span class="hljs-keyword">const</span> watcher = chokidar.watch(path.resolve(root), &#123;
      <span class="hljs-attr">ignored</span>: [<span class="hljs-string">'**/node_modules/**'</span>, <span class="hljs-string">'**/.git/**'</span>, ...ignored],
      <span class="hljs-attr">ignoreInitial</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">ignorePermissionErrors</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">disableGlobbing</span>: <span class="hljs-literal">true</span>,
      ...watchOptions
    &#125;) 
  
    <span class="hljs-keyword">const</span> plugins = config.plugins
    <span class="hljs-keyword">const</span> container = <span class="hljs-keyword">await</span> createPluginContainer(config, watcher)
    <span class="hljs-keyword">const</span> moduleGraph = <span class="hljs-keyword">new</span> ModuleGraph(container)
    <span class="hljs-keyword">const</span> closeHttpServer = createServerCloseFn(httpServer)
  
    <span class="hljs-comment">// eslint-disable-next-line prefer-const</span>
    <span class="hljs-keyword">let</span> exitProcess
  
    <span class="hljs-keyword">const</span> server = &#123;
      <span class="hljs-attr">config</span>: config,
      middlewares,
      <span class="hljs-keyword">get</span> <span class="hljs-title">app</span>() &#123;
        config.logger.warn(
          <span class="hljs-string">`ViteDevServer.app is deprecated. Use ViteDevServer.middlewares instead.`</span>
        )
        <span class="hljs-keyword">return</span> middlewares
      &#125;,
      httpServer,
      watcher,
      <span class="hljs-attr">pluginContainer</span>: container,
      ws,
      moduleGraph,
      transformWithEsbuild,
      <span class="hljs-function"><span class="hljs-title">transformRequest</span>(<span class="hljs-params">url, options</span>)</span> &#123;
        <span class="hljs-keyword">return</span> transformRequest(url, server, options)
      &#125;,
      <span class="hljs-attr">transformIndexHtml</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-function"><span class="hljs-title">ssrLoadModule</span>(<span class="hljs-params">url</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (!server._ssrExternals) &#123;
          server._ssrExternals = resolveSSRExternal(
            config,
            server._optimizeDepsMetadata
              ? <span class="hljs-built_in">Object</span>.keys(server._optimizeDepsMetadata.optimized)
              : []
          )
        &#125;
        <span class="hljs-keyword">return</span> ssrLoadModule(url, server)
      &#125;,
      <span class="hljs-function"><span class="hljs-title">ssrFixStacktrace</span>(<span class="hljs-params">e</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (e.stack) &#123;
          e.stack = ssrRewriteStacktrace(e.stack, moduleGraph)
        &#125;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">listen</span>(<span class="hljs-params">port, isRestart</span>)</span> &#123;
        <span class="hljs-keyword">return</span> startServer(server, port, isRestart)
      &#125;,
      <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">close</span>(<span class="hljs-params"></span>)</span> &#123;
        process.off(<span class="hljs-string">'SIGTERM'</span>, exitProcess)
  
        <span class="hljs-keyword">if</span> (!middlewareMode && process.env.CI !== <span class="hljs-string">'true'</span>) &#123;
          process.stdin.off(<span class="hljs-string">'end'</span>, exitProcess)
        &#125;
  
        <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all([
          watcher.close(),
          ws.close(),
          container.close(),
          closeHttpServer()
        ])
      &#125;,
      <span class="hljs-attr">_optimizeDepsMetadata</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">_ssrExternals</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">_globImporters</span>: &#123;&#125;,
      <span class="hljs-attr">_isRunningOptimizer</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">_registerMissingImport</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">_pendingReload</span>: <span class="hljs-literal">null</span>
    &#125;
  
    server.transformIndexHtml = createDevHtmlTransformFn(server)
  
    exitProcess = <span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">await</span> server.close()
      &#125; <span class="hljs-keyword">finally</span> &#123;
        process.exit(<span class="hljs-number">0</span>)
      &#125;
    &#125;
  
    <span class="hljs-comment">// 如果收到终止信号句柄，停止服务</span>
    process.once(<span class="hljs-string">'SIGTERM'</span>, exitProcess)
  
    <span class="hljs-keyword">if</span> (!middlewareMode && process.env.CI !== <span class="hljs-string">'true'</span>) &#123;
      process.stdin.on(<span class="hljs-string">'end'</span>, exitProcess)
    &#125;
  
    watcher.on(<span class="hljs-string">'change'</span>, <span class="hljs-keyword">async</span> (file) => &#123;
      file = normalizePath(file)
      <span class="hljs-comment">// invalidate module graph cache on file change</span>
      moduleGraph.onFileChange(file)
      <span class="hljs-keyword">if</span> (serverConfig.hmr !== <span class="hljs-literal">false</span>) &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">await</span> handleHMRUpdate(file, server)
        &#125; <span class="hljs-keyword">catch</span> (err) &#123;
          ws.send(&#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'error'</span>,
            <span class="hljs-attr">err</span>: prepareError(err)
          &#125;)
        &#125;
      &#125;
    &#125;)
  
    watcher.on(<span class="hljs-string">'add'</span>, <span class="hljs-function">(<span class="hljs-params">file</span>) =></span> &#123;
      handleFileAddUnlink(normalizePath(file), server)
    &#125;)
  
    watcher.on(<span class="hljs-string">'unlink'</span>, <span class="hljs-function">(<span class="hljs-params">file</span>) =></span> &#123;
      handleFileAddUnlink(normalizePath(file), server, <span class="hljs-literal">true</span>)
    &#125;)
  
    <span class="hljs-comment">// 插件处理</span>
    <span class="hljs-comment">// apply server configuration hooks from plugins</span>
    <span class="hljs-keyword">const</span> postHooks = []
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> plugin <span class="hljs-keyword">of</span> plugins) &#123;
      <span class="hljs-keyword">if</span> (plugin.configureServer) &#123;
        postHooks.push(<span class="hljs-keyword">await</span> plugin.configureServer(server))
      &#125;
    &#125;
  
    <span class="hljs-comment">// 下面是一些中间件的处理</span>
    <span class="hljs-comment">// Internal middlewares ------------------------------------------------------</span>
  
    <span class="hljs-comment">// request timer</span>
    <span class="hljs-comment">// 请求时间调试</span>
    <span class="hljs-keyword">if</span> (process.env.DEBUG) &#123;
      middlewares.use(timeMiddleware(root))
    &#125;
  
    <span class="hljs-comment">// cors (enabled by default)</span>
    <span class="hljs-keyword">const</span> &#123; cors &#125; = serverConfig
    <span class="hljs-keyword">if</span> (cors !== <span class="hljs-literal">false</span>) &#123;
      middlewares.use(corsMiddleware(<span class="hljs-keyword">typeof</span> cors === <span class="hljs-string">'boolean'</span> ? &#123;&#125; : cors))
    &#125;
  
    <span class="hljs-comment">// proxy</span>
    <span class="hljs-keyword">const</span> &#123; proxy &#125; = serverConfig
    <span class="hljs-keyword">if</span> (proxy) &#123;
      middlewares.use(proxyMiddleware(httpServer, config))
    &#125;
  
    <span class="hljs-comment">// base</span>
    <span class="hljs-keyword">if</span> (config.base !== <span class="hljs-string">'/'</span>) &#123;
      middlewares.use(baseMiddleware(server))
    &#125;
  
    <span class="hljs-comment">// open in editor support</span>
    middlewares.use(<span class="hljs-string">'/__open-in-editor'</span>, launchEditorMiddleware())
  
    <span class="hljs-comment">// hmr reconnect ping</span>
    <span class="hljs-comment">// Keep the named function. The name is visible in debug logs via `DEBUG=connect:dispatcher ...`</span>
    middlewares.use(<span class="hljs-string">'/__vite_ping'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">viteHMRPingMiddleware</span>(<span class="hljs-params">_, res</span>) </span>&#123;
      res.end(<span class="hljs-string">'pong'</span>)
    &#125;)
  
    <span class="hljs-comment">//decode request url</span>
    middlewares.use(decodeURIMiddleware())
  
    <span class="hljs-comment">// serve static files under /public</span>
    <span class="hljs-comment">// this applies before the transform middleware so that these files are served</span>
    <span class="hljs-comment">// as-is without transforms.</span>
    <span class="hljs-keyword">if</span> (config.publicDir) &#123;
      middlewares.use(servePublicMiddleware(config.publicDir))
    &#125;
  
    <span class="hljs-comment">// main transform middleware</span>
    middlewares.use(transformMiddleware(server))
  
    <span class="hljs-comment">// serve static files</span>
    middlewares.use(serveRawFsMiddleware(server))
    middlewares.use(serveStaticMiddleware(root, config))
  
    <span class="hljs-comment">// spa fallback</span>
    <span class="hljs-keyword">if</span> (!middlewareMode || middlewareMode === <span class="hljs-string">'html'</span>) &#123;
      middlewares.use(
        history(&#123;
          <span class="hljs-attr">logger</span>: createDebugger(<span class="hljs-string">'vite:spa-fallback'</span>),
          <span class="hljs-comment">// support /dir/ without explicit index.html</span>
          <span class="hljs-attr">rewrites</span>: [
            &#123;
              <span class="hljs-attr">from</span>: <span class="hljs-regexp">/\/$/</span>,
              <span class="hljs-function"><span class="hljs-title">to</span>(<span class="hljs-params">&#123; parsedUrl &#125;</span>)</span> &#123;
                <span class="hljs-keyword">const</span> rewritten = parsedUrl.pathname + <span class="hljs-string">'index.html'</span>
                <span class="hljs-keyword">if</span> (fs.existsSync(path.join(root, rewritten))) &#123;
                  <span class="hljs-keyword">return</span> rewritten
                &#125; <span class="hljs-keyword">else</span> &#123;
                  <span class="hljs-keyword">return</span> <span class="hljs-string">`/index.html`</span>
                &#125;
              &#125;
            &#125;
          ]
        &#125;)
      )
    &#125;
  
    <span class="hljs-comment">// run post config hooks</span>
    <span class="hljs-comment">// This is applied before the html middleware so that user middleware can</span>
    <span class="hljs-comment">// serve custom content instead of index.html.</span>
    postHooks.forEach(<span class="hljs-function">(<span class="hljs-params">fn</span>) =></span> fn && fn())
  
    <span class="hljs-keyword">if</span> (!middlewareMode || middlewareMode === <span class="hljs-string">'html'</span>) &#123;
      <span class="hljs-comment">// transform index.html</span>
      middlewares.use(indexHtmlMiddleware(server))
      <span class="hljs-comment">// handle 404s</span>
      <span class="hljs-comment">// Keep the named function. The name is visible in debug logs via `DEBUG=connect:dispatcher ...`</span>
      middlewares.use(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">vite404Middleware</span>(<span class="hljs-params">_, res</span>) </span>&#123;
        res.statusCode = <span class="hljs-number">404</span>
        res.end()
      &#125;)
    &#125;
  
    <span class="hljs-comment">// error handler</span>
    middlewares.use(errorMiddleware(server, !!middlewareMode))
  
    <span class="hljs-keyword">const</span> runOptimize = <span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">if</span> (config.cacheDir) &#123;
        server._isRunningOptimizer = <span class="hljs-literal">true</span>
        <span class="hljs-keyword">try</span> &#123;
          server._optimizeDepsMetadata = <span class="hljs-keyword">await</span> optimizeDeps(config)
        &#125; <span class="hljs-keyword">finally</span> &#123;
          server._isRunningOptimizer = <span class="hljs-literal">false</span>
        &#125;
        server._registerMissingImport = createMissingImporterRegisterFn(server)
      &#125;
    &#125;
  
    <span class="hljs-keyword">if</span> (!middlewareMode && httpServer) &#123;
      <span class="hljs-comment">// overwrite listen to run optimizer before server start</span>
      <span class="hljs-keyword">const</span> listen = httpServer.listen.bind(httpServer)
      httpServer.listen = (<span class="hljs-keyword">async</span> (port, ...args) => &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">await</span> container.buildStart(&#123;&#125;)
          <span class="hljs-keyword">await</span> runOptimize()
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          httpServer.emit(<span class="hljs-string">'error'</span>, e)
          <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-keyword">return</span> listen(port, ...args)
      &#125;) 
  
      httpServer.once(<span class="hljs-string">'listening'</span>, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// update actual port since this may be different from initial value</span>
        serverConfig.port = (httpServer.address()).port
      &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">await</span> container.buildStart(&#123;&#125;)
      <span class="hljs-keyword">await</span> runOptimize()
    &#125;
  
    <span class="hljs-keyword">return</span> server
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码很长，简单来说做了这几件事：</p>
<ul>
<li>创建一个服务器，用于作为一个静态服务器，响应应用的请求</li>
<li>创建一个 webSocket，提供 HMR</li>
<li>使用 chokidar 启用文件监听，并对文件修改进行处理</li>
<li>插件处理</li>
<li>监听句柄，如遇到停止信号则停止服务</li>
</ul>
<h3 data-id="heading-3">启动服务器的作用</h3>
<p>浏览器在访问在访问了 <strong><a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A3000%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:3000/" ref="nofollow noopener noreferrer">http://localhost:3000/</a></strong> 后，得到了下面的内容：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">di</span> <span class="hljs-attr">v</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"/src/main.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>依据 ESM 规范在浏览器 script 标签中的实现，对于 <code><script type="module" src="./bar.js"></script></code>  内容：当出现 <code>script</code> 标签 <code>type</code> 属性为 <code>module</code> 时，浏览器会发出 HTTP 请求模块相应内容。经过 Vite Server 处理。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b89c844091f24de08ea2a06328179974~tplv-k3u1fbpfcp-zoom-1.image" alt="经过处理的 main.js" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到，经过 Vite Server 处理 <strong><a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A3000%2Fsrc%2Fmain.js" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:3000/src/main.js" ref="nofollow noopener noreferrer">http://localhost:3000/src/main.js</a></strong> 请求后，最终返回了上面图片的内容。不过这个内容和我们项目中的
<code>./src/main.js</code> 有差别</p>
<p>源代码是这样</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.css'</span>

createApp(App).mount(<span class="hljs-string">'#app'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过 Vite 后变成这样了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'/@modules/vue.js'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'/src/App.vue'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'/src/index.css?import'</span>

createApp(App).mount(<span class="hljs-string">'#app'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们拆成两部分来看。</p>
<p>其中 <code>import &#123; createApp &#125; from 'vue'</code> 改为 <code>import &#123; createApp &#125; from '/@modules/vue.js'</code>，原因很明显：<code>import</code> 对应的路径只支持 <code>"/""./"</code>或者 <code>"../"</code> 开头的内容，直接使用模块名 <code>import</code>，会立即报错。</p>
<p>所以在 Vite Server 处理请求时，通过 resolve 这个插件来给 <code>import from 'A' 的 A</code> 添加 <code>/@module/</code> 前缀为 <code>from '/@modules/A'</code>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fplugins%2Fresolve.ts%23L66" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/main/packages/vite/src/node/plugins/resolve.ts#L66" ref="nofollow noopener noreferrer">源码部分对应</a>。</p>
<h4 data-id="heading-4">整个过程和调用链路较长，我对 Vite 处理 import 方法做一个简单总结：</h4>
<ul>
<li>
<p>在 createServer 里获取请求 path 对应的 body 内容；</p>
</li>
<li>
<p>通过 es-module-lexer 解析资源 AST，并拿到 import 的内容；</p>
</li>
<li>
<p>如果判断 import 的资源是绝对路径，即可认为该资源为 npm 模块，并返回处理后的资源路径。比如上述代码中，<code>vue → /@modules/vue</code>。</p>
</li>
</ul>
<p>对于形如：<code>import App from './App.vue'</code>和 <code>import './index.css'</code> 的处理，与上述情况类似：</p>
<ul>
<li>
<p>在 createSercer 里获取请求 path 对应的 body 内容；</p>
</li>
<li>
<p>通过 es-module-lexer 解析资源 AST，并拿到 import 的内容；</p>
</li>
<li>
<p>如果判断 import 的资源是相对路径，即可认为该资源为项目应用中资源，并返回处理后的资源路径。比如上述代码中，<code>./App.vue → /src/App.vue</code>。</p>
</li>
</ul>
<p>接下来浏览器根据 main.js 的内容，分别请求：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">/@modules/vue.js
/src/App.vue
/src/index.css?<span class="hljs-keyword">import</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 <code>/@module/</code> 类请求较为容易，我们只需要完成下面三步：</p>
<ul>
<li>
<p>在 createServer 中间件里获取请求 path 对应的 body 内容；</p>
</li>
<li>
<p>判断路径是否以 /@module/ 开头，如果是，取出包名（这里为 vue.js）；</p>
</li>
<li>
<p>去 node_modules 文件中找到对应的 npm 库，并返回内容。</p>
</li>
</ul>
<p>上述步骤在 Vite 中使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fplugins%2Fresolve.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/main/packages/vite/src/node/plugins/resolve.ts" ref="nofollow noopener noreferrer">resolve</a> 中间件实现。</p>
<p>接着，就是对 <code>/src/App.vue</code> 类请求进行处理，这就涉及 Vite 服务器的编译能力了。</p>
<p>我们先看结果，对比项目中的 App.vue，浏览器请求得到的结果显然出现了大变样：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/989f8ccd46cb4a03ba859e83ea40906f~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实际上，<code>App.vue</code> 这样的单文件组件对应 <code>script、style</code> 和 <code>template</code>，在经过 Vite Server 处理时，服务端对 <code>script、style 和 template</code> 三部分分别处理，对应中间件为 <strong><code>@vitejs/plugin-vue</code></strong>。这个插件的实现很简单，即对 <code>.vue</code> 文件请求进行处理，通过 parseSFC 方法解析单文件组件，并通过 <code>compileSFCMain</code> 方法将单文件组件拆分为形如上图内容，对应中间件关键内容可在源码 vuePlugin 中找到。源码中，涉及 <code>parseSFC</code> 具体所做的事情，是调用 <code>@vue/compiler-sfc</code> 进行单文件组件解析。精简为我自己的逻辑，帮助你理解：</p>
<p>总的来说，每一个 <code>.vue</code> 单文件组件都被拆分成多个请求。比如对应上面场景，浏览器接收到 App.vue 对应的实际内容后，发出 <code>HelloWorld.vue</code> 以及 <code>App.vue?type=template</code> 的请求（通过 type 这个 query 来表示是 template 还是 style）。<code>createServer</code> 进行分别处理并返回，这些请求依然分别被上面提到的 <code>@vitejs/plugin-vue</code> 插件处理：对于 <code>template</code> 的请求，服务使用 <code>@vue/compiler-dom</code> 进行编译 <code>template</code> 并返回内容。</p>
<p>对于上面提到的 <code>http://localhost:3000/src/index.css?import</code> 请求稍微特殊，在 <code>css</code> 插件中， 通过 <code>cssPostPlugin</code> 对象的 <code>transform</code> 来实现解析：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params">css, id, ssr</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!cssLangRE.test(id) || commonjsProxyRE.test(id)) &#123;
        <span class="hljs-keyword">return</span>
      &#125;

      <span class="hljs-keyword">const</span> modules = cssModulesCache.get(config)!.get(id)
      <span class="hljs-keyword">const</span> modulesCode =
        modules && dataToEsm(modules, &#123; <span class="hljs-attr">namedExports</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">preferConst</span>: <span class="hljs-literal">true</span> &#125;)

      <span class="hljs-keyword">if</span> (config.command === <span class="hljs-string">'serve'</span>) &#123;
        <span class="hljs-keyword">if</span> (isDirectCSSRequest(id)) &#123;
          <span class="hljs-keyword">return</span> css
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// server only</span>
          <span class="hljs-keyword">if</span> (ssr) &#123;
            <span class="hljs-keyword">return</span> modulesCode || <span class="hljs-string">`export default <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(css)&#125;</span>`</span>
          &#125;
          <span class="hljs-keyword">return</span> [
            <span class="hljs-string">`import &#123; updateStyle, removeStyle &#125; from <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(
              path.posix.join(config.base, CLIENT_PUBLIC_PATH)
            )&#125;</span>`</span>,
            <span class="hljs-string">`const id = <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(id)&#125;</span>`</span>,
            <span class="hljs-string">`const css = <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(css)&#125;</span>`</span>,
            <span class="hljs-string">`updateStyle(id, css)`</span>,
            <span class="hljs-comment">// css modules exports change on edit so it can't self accept</span>
            <span class="hljs-string">`<span class="hljs-subst">$&#123;modulesCode || <span class="hljs-string">`import.meta.hot.accept()\nexport default css`</span>&#125;</span>`</span>,
            <span class="hljs-string">`import.meta.hot.prune(() => removeStyle(id))`</span>
          ].join(<span class="hljs-string">'\n'</span>)
        &#125;
      &#125;

      <span class="hljs-comment">// build CSS handling ----------------------------------------------------</span>

      <span class="hljs-comment">// record css</span>
      styles.set(id, css)

      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">code</span>: modulesCode || <span class="hljs-string">`export default <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(css)&#125;</span>`</span>,
        <span class="hljs-attr">map</span>: &#123; <span class="hljs-attr">mappings</span>: <span class="hljs-string">''</span> &#125;,
        <span class="hljs-comment">// avoid the css module from being tree-shaken so that we can retrieve</span>
        <span class="hljs-comment">// it in renderChunk()</span>
        <span class="hljs-attr">moduleSideEffects</span>: <span class="hljs-string">'no-treeshake'</span>
      &#125;
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用 <code>cssPostPlugin</code> 中的 <code>transform</code> 方法：</p>
<p>该方法会在浏览器中执行 <code>updateStyle</code> 方法，就像是 <code>http://localhost:3000/src/index.css?import</code> 的源码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createHotContext <span class="hljs-keyword">as</span> __vite__createHotContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"/@vite/client"</span>;<span class="hljs-keyword">import</span>.meta.hot = __vite__createHotContext(<span class="hljs-string">"/src/components/HelloWorld.vue?vue&type=style&index=0&scoped=true&lang.css"</span>);<span class="hljs-keyword">import</span> &#123; updateStyle, removeStyle &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"/@vite/client"</span>
<span class="hljs-keyword">const</span> id = <span class="hljs-string">"/Users/study/vite-app/src/components/HelloWorld.vue?vue&type=style&index=0&scoped=true&lang.css"</span>
<span class="hljs-keyword">const</span> css = <span class="hljs-string">"\nh1[data-v-469af010] &#123;\n   font-size:18px;\n&#125;\n"</span>
updateStyle(id, css)
<span class="hljs-keyword">import</span>.meta.hot.accept()
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> css
<span class="hljs-keyword">import</span>.meta.hot.prune(<span class="hljs-function">() =></span> removeStyle(id))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终完成在浏览器中插入样式。</p>
<p>至此，我们解析并列举了较多源码内容。以上内容需要跟着思路，一步步梳理，也强烈建议你打开 Vite 源码自己动手剖析。如果看到这里你仍然也有些“云里雾里”，不要心急，结合我下面这个图示，再次进行阅读，相信会更有收获。</p>
<h3 data-id="heading-5">和 webpack 对比</h3>
<h4 data-id="heading-6">webpack bundleless 的思路</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e13fd887ae634b499b58b8c7ea2a6ada~tplv-k3u1fbpfcp-zoom-1.image" alt="webpack 思路" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d85735a75a8b413984a00ee03a07ef10~tplv-k3u1fbpfcp-zoom-1.image" alt="打包思路" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">Vite bundleless 的思路：</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c73b2bf2470b4728b4afcceced734113~tplv-k3u1fbpfcp-zoom-1.image" alt="Vite 的 思路" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0cefb57cac8455ca10bceac95770db4~tplv-k3u1fbpfcp-zoom-1.image" alt="打包思路" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">总结</h4>
<ul>
<li>
<p>Vite 利用浏览器原生支持 ESM 这一特性，省略了对模块的打包，也就不需要生成 bundle，因此初次启动更快，HMR 特性友好。</p>
</li>
<li>
<p>Vite 开发模式下，通过启动 Node 服务器，在服务端完成模块的改写（比如单文件的解析编译等）和请求处理，实现真正的按需编译。</p>
</li>
<li>
<p>Vite Server 所有逻辑基本都依赖中间件实现。这些中间件，拦截请求之后，完成了如下内容：</p>
<ul>
<li>
<p>处理 ESM 语法，比如将业务代码中的 import 第三方依赖路径转为浏览器可识别的依赖路径；</p>
</li>
<li>
<p>对 .ts、.vue 等文件进行即时编译；</p>
</li>
<li>
<p>对 Sass/Less 的需要预编译的模块进行编译；</p>
</li>
<li>
<p>和浏览器端建立 socket 连接，实现 HMR。</p>
</li>
</ul>
</li>
</ul></div>  
</div>
            