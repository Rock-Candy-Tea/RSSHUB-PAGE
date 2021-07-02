
---
title: 'Vite 特性和部分源码解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 15:00:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eb6a01e6564840817b127265b07edd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是第 105 篇不掺水的原创，想获取更多原创好文，请搜索公众号关注我们吧~ 本文首发于政采云前端博客：<a href="https://zoo.team/article/about-vite" target="_blank" rel="nofollow noopener noreferrer">Vite 特性和部分源码解析</a></p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d49f2992684343948565c0d9fa97ca7a~tplv-k3u1fbpfcp-watermark.image" alt="清音.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">Vite 的特性</h3>
<p>Vite 的主要特性就是 Bundleless。基于浏览器开始原生的支持 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Modules?fileGuid=DDr3GGh6QRvQgWQC" target="_blank" rel="nofollow noopener noreferrer">JavaScript 模块功能</a>，JavaScript 模块依赖于  <code>import</code> 和 <code>export</code> 的特性，目前主流浏览器基本都支持；</p>
<p>想要查看具体支持的版本可以<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Modules?fileGuid=DDr3GGh6QRvQgWQC" target="_blank" rel="nofollow noopener noreferrer">点击这里</a>；</p>
<p>那这有什么优势呢？</p>
<h4 data-id="heading-1">去掉打包步骤</h4>
<p>打包是开发者利用打包工具将应用各个模块集合在一起形成 bundle，以一定规则读取模块的代码，以便在不支持模块化的浏览器里使用，并且可以减少 http 请求的数量。但其实在本地开发过程中打包反而增加了我们排查问题的难度，增加了响应时长，Vite 在本地开发命令中去除了打包步骤，从而缩短构建时长。</p>
<h4 data-id="heading-2">按需加载</h4>
<p>为了减少 bundle 大小，一般会想要按需加载，主要有两种方式：</p>
<ol>
<li>使用动态引入 <code>import()</code> 的方式异步的加载模块，被引入模块依然需要提前编译打包；</li>
<li>使用 tree shaking 等方式尽力的去掉未引用的模块；</li>
</ol>
<p>而 Vite 的方式更为直接，它只在某个模块被 import 的时候动态的加载它，实现了真正的按需加载，减少了加载文件的体积，缩短了时长；</p>
<h4 data-id="heading-3">Vite开发环境主体流程</h4>
<p>下图是 Vite 在开发环境运行时加载文件的主体流程。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6922f9b694324cb193acdbb482babadb~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-4">Vite  部分源码解析</h3>
<h4 data-id="heading-5">总体目录结构</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">|-CHANGELOG.md
|-LICENSE.md
|-README.md
|-bin
|  |-openChrome.applescript
|  |-vite.js
|-client.d.ts
|-package.json
|-rollup.config.js #打包配置文件
|-scripts
|  |-patchTypes.js
|-src
|  |-client #客户端
|  |  |-client.ts
|  |  |-env.ts
|  |  |-overlay.ts
|  |  |-tsconfig.json
|  |-node #服务端
|  |  |-build.ts
|  |  |-cli.ts #命令入口文件
|  |  |-config.ts
|  |  |-constants.ts #常量
|  |  |-importGlob.ts
|  |  |-index.ts
|  |  |-logger.ts
|  |  |-optimizer
|  |  |  |-esbuildDepPlugin.ts
|  |  |  |-index.ts
|  |  |  |-registerMissing.ts
|  |  |  |-scan.ts
|  |  |-plugin.ts #rollup 插件
|  |  |-plugins   #插件相关文件
|  |  |  |-asset.ts
|  |  |  |-clientInjections.ts
|  |  |  |-css.ts
|  |  |  |-esbuild.ts
|  |  |  |-html.ts
|  |  |  |-index.ts 
|  |  |  |-...
|  |  |-preview.ts
|  |  |-server
|  |  |  |-hmr.ts #热更新
|  |  |  |-http.ts
|  |  |  |-index.ts
|  |  |  |-middlewares #中间件
|  |  |  |  |-...
|  |  |  |-moduleGraph.ts #模块间关系组装(树形)
|  |  |  |-openBrowser.ts #打开浏览器
|  |  |  |-pluginContainer.ts
|  |  |  |-send.ts
|  |  |  |-sourcemap.ts
|  |  |  |-transformRequest.ts
|  |  |  |-ws.ts
|  |  |-ssr
|  |  |  |-__tests__
|  |  |  |  |-ssrTransform.spec.ts
|  |  |  |-ssrExternal.ts
|  |  |  |-ssrManifestPlugin.ts
|  |  |  |-ssrModuleLoader.ts
|  |  |  |-ssrStacktrace.ts
|  |  |  |-ssrTransform.ts
|  |  |-tsconfig.json
|  |  |-utils.ts
|-tsconfig.base.json
|-types
|  |-...                  
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">server 核心方法</h4>
<p>从入口文件 cli.ts，可以看到三个命令对应了 3 个核心的文件&方法；</p>
<ol>
<li>dev 命令</li>
</ol>
<p>文件路径：./server/index.ts；</p>
<p>主要方法：createServer；</p>
<p>主要功能：项目的本地开发命令，基于 httpServer 启动服务，Vite 通过对请求路径的劫持获取资源的内容返回给浏览器，服务端将文件路径进行了重写。例如：</p>
<p>项目源码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./index.vue'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经服务端重写后，node_modules 文件夹下的三方包代码路径也会被拼接完整。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> __vite__cjsImport0_vue <span class="hljs-keyword">from</span> <span class="hljs-string">"/node_modules/.vite/vue.js?v=ed69bae0"</span>; 
<span class="hljs-keyword">const</span> createApp = __vite__cjsImport0_vue[<span class="hljs-string">"createApp"</span>];
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'/src/pages/back-sky/index.vue'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.build 命令
文件路径：./build.ts ；</p>
<p>主要方法：build；</p>
<p>主要功能：使用 rollup 打包编译</p>
<p>3.optimize 命令</p>
<p>文件路径：./optimizer/index.ts；</p>
<p>主要方法：optimizeDeps；</p>
<p>主要功能：主要针对第三方包，Vite 在执行 runOptimize 的时候中会使用 rollup 对三方包重新编译，将编译成符合 esm 模块规范的新的包放入 node_modules 下的 .vite 中，然后配合 resolver 对三方包的导入进行处理：使用编译后的包内容代替原来包的内容，这样就解决了 Vite 中不能使用 cjs 包的问题。</p>
<p>下面是 .vite 文件夹中的 _metadata.json 文件，它在预编译的过程中生成，罗列了所有被预编译完成的文件及其路径。例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-string">"hash"</span>: <span class="hljs-string">"31d458ff"</span>,
  <span class="hljs-string">"browserHash"</span>: <span class="hljs-string">"ed69bae0"</span>,
  <span class="hljs-string">"optimized"</span>: &#123;
    <span class="hljs-string">"element-plus/lib/utils/dom"</span>: &#123;
      <span class="hljs-string">"file"</span>: <span class="hljs-string">"/Users/zcy/Documents/workspace/back-sky-front/node_modules/.vite/element-plus_lib_utils_dom.js"</span>,
      <span class="hljs-string">"src"</span>: <span class="hljs-string">"/Users/zcy/Documents/workspace/back-sky-front/node_modules/element-plus/lib/utils/dom.js"</span>,
      <span class="hljs-string">"needsInterop"</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-string">"element-plus"</span>: &#123;
      <span class="hljs-string">"file"</span>: <span class="hljs-string">"/Users/zcy/Documents/workspace/back-sky-front/node_modules/.vite/element-plus.js"</span>,
      <span class="hljs-string">"src"</span>: <span class="hljs-string">"/Users/zcy/Documents/workspace/back-sky-front/node_modules/element-plus/lib/index.esm.js"</span>,
      <span class="hljs-string">"needsInterop"</span>: <span class="hljs-literal">false</span>
    &#125;,
    <span class="hljs-string">"vue"</span>: &#123;
      <span class="hljs-string">"file"</span>: <span class="hljs-string">"/Users/zcy/Documents/workspace/back-sky-front/node_modules/.vite/vue.js"</span>,
      <span class="hljs-string">"src"</span>: <span class="hljs-string">"/Users/zcy/Documents/workspace/back-sky-front/node_modules/vue/dist/vue.runtime.esm-bundler.js"</span>,
      <span class="hljs-string">"needsInterop"</span>: <span class="hljs-literal">true</span>
    &#125;,
    ......
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">模块解析</h4>
<p><a href="https://cn.vitejs.dev/guide/dep-pre-bundling.html?fileGuid=DDr3GGh6QRvQgWQC" target="_blank" rel="nofollow noopener noreferrer">预构建</a>是用来提升页面重载速度，它将 CommonJS、UMD 等转换为 ESM 格式。预构建这一步由 <a href="http://esbuild.github.io/?fileGuid=DDr3GGh6QRvQgWQC" target="_blank" rel="nofollow noopener noreferrer">esbuild</a> 执行，这使得 Vite 的冷启动时间比任何基于 JavaScript 的打包程序都要快得多。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a3322c3c6c647b0b642eb6dd7c9c1e3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>为什么 ESbuild 会更快？</p>
<ol>
<li>使用 Go 语言</li>
<li>重度并行，使用 CPU</li>
<li>高效使用内存</li>
<li>Scratch 编写，减少使用三方库，避免导致性能不可控</li>
</ol>
<p>重写导入为合法的 URL，例如 <code>/node_modules/.vite/my-dep.js?v=f3sf2ebd</code> 以便浏览器能够正确导入它们</p>
<h4 data-id="heading-8">热更新</h4>
<p>热更新主体流程如下：</p>
<ol>
<li>服务端基于 watcher 监听文件改动，根据类型判断更新方式，并编译资源</li>
<li>客户端通过 WebSocket 监听到一些更新的消息类型</li>
<li>客户端收到资源信息，根据消息类型执行热更新逻辑</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baaa3b74a60046ca9d0817102b9e60e5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面是服务端热更新的核心 hmr.ts 中的部分判断逻辑；</p>
<p>如果配置文件或者环境文件发生修改时，会触发服务重启，才能让配置生效。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (file === config.configFile || file.endsWith(<span class="hljs-string">'.env'</span>)) &#123;
  <span class="hljs-comment">// auto restart server 配置&环境文件修改则自动重启服务</span>
  debugHmr(<span class="hljs-string">`[config change] <span class="hljs-subst">$&#123;chalk.dim(shortFile)&#125;</span>`</span>)
  config.logger.info(
    chalk.green(<span class="hljs-string">'config or .env file changed, restarting server...'</span>),
    &#123; <span class="hljs-attr">clear</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">timestamp</span>: <span class="hljs-literal">true</span> &#125;
  )
  <span class="hljs-keyword">await</span> restartServer(server)
  <span class="hljs-keyword">return</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>html 文件更新时，将会触发页面的重新加载。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (file.endsWith(<span class="hljs-string">'.html'</span>)) &#123; <span class="hljs-comment">// html 文件更新</span>
  config.logger.info(chalk.green(<span class="hljs-string">`page reload `</span>) +         chalk.dim(shortFile), &#123;
    <span class="hljs-attr">clear</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">timestamp</span>: <span class="hljs-literal">true</span>
  &#125;)
  ws.send(&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'full-reload'</span>,
    <span class="hljs-attr">path</span>: config.server.middlewareMode
    ? <span class="hljs-string">'*'</span>
    : <span class="hljs-string">'/'</span> + normalizePath(path.relative(config.root, file))
  &#125;)
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// loaded but not in the module graph, probably not js</span>
  debugHmr(<span class="hljs-string">`[no modules matched] <span class="hljs-subst">$&#123;chalk.dim(shortFile)&#125;</span>`</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vue 等文件更新时，都会进入 <code>updateModules</code> 方法，正常情况下只会触发 update，实现热更新，热替换；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateModules</span>(<span class="hljs-params">
  file: string,
  modules: ModuleNode[],
  timestamp: number,
  &#123; config, ws &#125;: ViteDevServer
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> updates: Update[] = []
  <span class="hljs-keyword">const</span> invalidatedModules = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span><ModuleNode>()
<span class="hljs-comment">// 遍历插件数组，关联下面的片段</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> mod <span class="hljs-keyword">of</span> modules) &#123;
    <span class="hljs-keyword">const</span> boundaries = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span><&#123;
      <span class="hljs-attr">boundary</span>: ModuleNode
      <span class="hljs-attr">acceptedVia</span>: ModuleNode
    &#125;>()
    <span class="hljs-comment">// 设置时间戳</span>
    invalidate(mod, timestamp, invalidatedModules)
    <span class="hljs-comment">// 查找引用模块，判断是否需要重载页面</span>
    <span class="hljs-keyword">const</span> hasDeadEnd = propagateUpdate(mod, timestamp, boundaries)
    <span class="hljs-comment">// 找不到引用者则会发起刷新</span>
    <span class="hljs-keyword">if</span> (hasDeadEnd) &#123;
      config.logger.info(chalk.green(<span class="hljs-string">`page reload `</span>) + chalk.dim(file), &#123;
        <span class="hljs-attr">clear</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">timestamp</span>: <span class="hljs-literal">true</span>
      &#125;)
      ws.send(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'full-reload'</span>
      &#125;)
      <span class="hljs-keyword">return</span>
    &#125;
    updates.push(
      ...[...boundaries].map(<span class="hljs-function">(<span class="hljs-params">&#123; boundary, acceptedVia &#125;</span>) =></span> (&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;boundary.type&#125;</span>-update`</span> <span class="hljs-keyword">as</span> Update[<span class="hljs-string">'type'</span>],
        timestamp,
        <span class="hljs-attr">path</span>: boundary.url,
        <span class="hljs-attr">acceptedPath</span>: acceptedVia.url
      &#125;))
    )
  &#125;
  <span class="hljs-comment">// 日志输出</span>
  config.logger.info(
    updates
      .map(<span class="hljs-function">(<span class="hljs-params">&#123; path &#125;</span>) =></span> chalk.green(<span class="hljs-string">`hmr update `</span>) + chalk.dim(path))
      .join(<span class="hljs-string">'\n'</span>),
    &#123; <span class="hljs-attr">clear</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">timestamp</span>: <span class="hljs-literal">true</span> &#125;
  )
  <span class="hljs-comment">// 向客户端发送消息，进行热更新操作</span>
  ws.send(&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'update'</span>,
    updates
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中的 modules 是热更新时需要执行的各个插件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> plugin <span class="hljs-keyword">of</span> config.plugins) &#123;
  <span class="hljs-keyword">if</span> (plugin.handleHotUpdate) &#123;
    <span class="hljs-keyword">const</span> filteredModules = <span class="hljs-keyword">await</span> plugin.handleHotUpdate(hmrContext)
    <span class="hljs-keyword">if</span> (filteredModules) &#123;
      hmrContext.modules = filteredModules
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vite 会把模块的依赖关系组合成 moduleGraph，它的结构类似树形，热更新中判断哪些文件需要更新也会依赖  moduleGraph；它的文件内容大致如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// moduleGraph 返回的 ModuleNode 大致结构</span>
 ModuleNode &#123;
  <span class="hljs-attr">id</span>: <span class="hljs-string">'/Users/zcy/Documents/workspace/back-sky-front/src/pages/back-sky/index.js'</span>,
  <span class="hljs-attr">file</span>: <span class="hljs-string">'/Users/zcy/Documents/workspace/back-sky-front/src/pages/back-sky/index.js'</span>,
  <span class="hljs-attr">importers</span>: <span class="hljs-built_in">Set</span> &#123;&#125;,
  <span class="hljs-attr">importedModules</span>: <span class="hljs-built_in">Set</span> &#123;
    ModuleNode &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-string">'/Users/zcy/Documents/workspace/back-sky-front/node_modules/.vite/vue.js?v=32cfd30c'</span>,
      <span class="hljs-attr">file</span>: <span class="hljs-string">'/Users/zcy/Documents/workspace/back-sky-front/node_modules/.vite/vue.js'</span>,
      ......
      <span class="hljs-attr">lastHMRTimestamp</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">url</span>: <span class="hljs-string">'/node_modules/.vite/vue.js?v=32cfd30c'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'js'</span>
    &#125;,
    ModuleNode &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-string">'/Users/zcy/Documents/workspace/back-sky-front/src/pages/back-sky/index.vue'</span>,
      <span class="hljs-attr">file</span>: <span class="hljs-string">'/Users/zcy/Documents/workspace/back-sky-front/src/pages/back-sky/index.vue'</span>,
      ......
      <span class="hljs-attr">url</span>: <span class="hljs-string">'/src/pages/back-sky/index.vue'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'js'</span>
    &#125;,
    ModuleNode &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-string">'/Users/zcy/Documents/workspace/back-sky-front/node_modules/element-plus/lib/theme-chalk/index.css'</span>,
      <span class="hljs-attr">file</span>: <span class="hljs-string">'/Users/zcy/Documents/workspace/back-sky-front/node_modules/element-plus/lib/theme-chalk/index.css'</span>,
      <span class="hljs-attr">importers</span>: [<span class="hljs-built_in">Set</span>],
      <span class="hljs-attr">importedModules</span>: <span class="hljs-built_in">Set</span> &#123;&#125;,
      <span class="hljs-attr">acceptedHmrDeps</span>: <span class="hljs-built_in">Set</span> &#123;&#125;,
      <span class="hljs-attr">isSelfAccepting</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">transformResult</span>: [<span class="hljs-built_in">Object</span>],
      <span class="hljs-attr">ssrTransformResult</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">ssrModule</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">lastHMRTimestamp</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">url</span>: <span class="hljs-string">'/node_modules/element-plus/lib/theme-chalk/index.css'</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'js'</span>
    &#125;,
    ......
  &#125;,
  <span class="hljs-attr">acceptedHmrDeps</span>: <span class="hljs-built_in">Set</span> &#123;&#125;,
  <span class="hljs-attr">isSelfAccepting</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">transformResult</span>: &#123;
    <span class="hljs-attr">code</span>: <span class="hljs-string">'import __vite__cjsImport0_vue from '</span> +
      <span class="hljs-string">'"/node_modules/.vite/vue.js?v=32cfd30c"; const createApp = '</span> +
      <span class="hljs-string">'__vite__cjsImport0_vue["createApp"];\nimport App from '</span> +
      <span class="hljs-string">"'/src/pages/back-sky/index.vue';\nimport "</span> +
      <span class="hljs-string">"'/node_modules/element-plus/lib/theme-chalk/index.css';\n\nconst app = "</span> +
      <span class="hljs-string">'createApp(App);\n\nimport &#123; addHistoryMethod &#125; from '</span> +
      <span class="hljs-string">"'/src/pages/back-sky/api/index.js';\nimport &#123;\n  ElButton,\n  ElDropdown,\n  "</span> +
      <span class="hljs-string">'ElDropdownMenu,\n  ElDropdownItem,\n  ElMenu,\n  ElSubmenu,\n  ElMenuItem,\n  '</span> +
      <span class="hljs-string">'ElMenuItemGroup,\n  ElPopover,\n  ElDialog,\n  ElRow,\n  ElInput,\n  '</span> +
      <span class="hljs-string">"ElLoading,\n&#125; from '/node_modules/.vite/element-plus.js?v=32cfd30c';\n\n"</span> +
      <span class="hljs-string">'app.use(ElButton);\napp.use(ElLoading);\napp.use(ElDropdown);\n'</span> +
      <span class="hljs-string">'app.use(ElDropdownMenu);\napp.use(ElDropdownItem);\napp.use(ElMenu);\n'</span> +
      <span class="hljs-string">'app.use(ElSubmenu);\napp.use(ElMenuItem);\napp.use(ElMenuItemGroup);\n'</span> +
      <span class="hljs-string">'app.use(ElPopover);\napp.use(ElDialog);\napp.use(ElRow);\napp.use(ElInput);\n'</span> +
      <span class="hljs-string">"\nconst f = ()=>&#123;\n  return app.mount('#app');\n&#125;;\n\nconst $backsky = "</span> +
      <span class="hljs-string">"document.getElementById('back-sky');\nif($backsky) &#123;\n  $backsky.innerHTML "</span> +
      <span class="hljs-string">"= '';\n  $backsky.appendChild(f().$el);\n&#125; else &#123;\n  window.onload = "</span> +
      <span class="hljs-string">"function()&#123;\n    document.getElementById('back-sky') && "</span> +
      <span class="hljs-string">"document.getElementById('back-sky').appendChild(f().$el);\n  &#125;;\n&#125;\n\n"</span> +
      <span class="hljs-string">"window.addHistoryListener = addHistoryMethod('historychange');\n"</span> +
      <span class="hljs-string">"history.pushState =  addHistoryMethod('pushState');\nhistory.replaceState "</span> +
      <span class="hljs-string">"=  addHistoryMethod('replaceState');\n\n// 监听hash路由变化，不与onhashchange互相覆盖\n"</span> +
      <span class="hljs-string">'addHashChange(()=>&#123;\n  setTimeout(() => &#123;\n    const $backsky = '</span> +
      <span class="hljs-string">"document.getElementById('back-sky');\n    if($backsky && "</span> +
      <span class="hljs-string">"$backsky.innerHTML === '') &#123;\n      $backsky.appendChild(f().$el);\n    &#125;\n "</span> +
      <span class="hljs-string">" &#125;,0);\n&#125;);\n\nfunction addHashChange(callback) &#123;\n  if('onhashchange' in "</span> +
      <span class="hljs-string">'window === false)&#123;//浏览器不支持\n    return false;\n  &#125;\n  '</span> +
      <span class="hljs-string">'if(window.addEventListener) &#123;\n    '</span> +
      <span class="hljs-string">"window.addEventListener('hashchange',function(e) &#123;\n      callback && "</span> +
      <span class="hljs-string">'callback(e);\n    &#125;,false);\n  &#125;else if(window.attachEvent) &#123;//IE 8 及更早 IE '</span> +
      <span class="hljs-string">"版本浏览器\n    window.attachEvent('onhashchange',function(e) &#123;\n      callback "</span> +
      <span class="hljs-string">'&& callback(e);\n    &#125;);\n  &#125;\n  '</span> +
      <span class="hljs-string">"window.addHistoryListener('history',function(e)&#123;\n    callback && "</span> +
      <span class="hljs-string">'callback(e);\n  &#125;);\n&#125;\n\n\n'</span>,
    <span class="hljs-attr">map</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">etag</span>: <span class="hljs-string">'W/"846-Qa424gJKl3YCqHDWXXsM1mFHRqg"'</span>
  &#125;,
  <span class="hljs-attr">ssrTransformResult</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">ssrModule</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">lastHMRTimestamp</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">url</span>: <span class="hljs-string">'/src/pages/back-sky/index.js'</span>,
  <span class="hljs-attr">type</span>: <span class="hljs-string">'js'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">原有项目切换</h3>
<p>最后我们来看下如何使用 Vite 去打包一个旧的 Vue 项目；</p>
<p>首先我们需要升级 Vue3</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install vue@next
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并为项目添加 vite 配置文件，在根目录下创建 vite.config.js，并为它添加一些基础的配置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vite.config.js</span>
<span class="hljs-comment">// vite2.1.5</span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">import</span> vue <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-vue'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// 配置选项</span>
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'@utils'</span>: path.resolve(__dirname, <span class="hljs-string">'./src/utils'</span>)
    &#125;,
  &#125;,
  <span class="hljs-attr">plugins</span>: [vue()],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引用的第三方组件库可能也会需要升级，例如：升 element-ui 至 element-plus</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install element-plus
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vue3 在 import 时，需使用 <code>createApp</code> 方法进行初始化</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./index.vue'</span>;
<span class="hljs-keyword">const</span> app = createApp(App);
<span class="hljs-keyword">import</span> &#123;
  ElInput,
  ElLoading,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-plus'</span>;

app.use(ElButton);
app.use(ElLoading);
......
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里就可以将项目运行起来了。
注意：Vite 官方不允许省略 .vue 后缀，否则就会报错；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[plugin:vite:<span class="hljs-keyword">import</span>-analysis] Failed to resolve <span class="hljs-keyword">import</span> <span class="hljs-string">"./todoList"</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"src/pages/back-sky/components/header/index.vue"</span>. Does the file exist?
<span class="hljs-regexp">/components/</span>header/index.vue:<span class="hljs-number">2</span>:<span class="hljs-number">23</span>
<span class="hljs-number">1</span>  |  
<span class="hljs-number">2</span>  |  <span class="hljs-keyword">import</span> todoList <span class="hljs-keyword">from</span> <span class="hljs-string">'./todoList'</span>;
<span class="hljs-keyword">import</span> todoList <span class="hljs-keyword">from</span> <span class="hljs-string">'./todoList.vue'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们来对比一下该项目两种构建方式时间的对比；</p>
<p>Webpack 冷启动，耗时 7513ms：</p>
<pre><code class="hljs language-bash copyable" lang="bash">⚠ ｢wdm｣: Hash: 1ad1dd54289cfad8ecbe
Version: webpack 4.46.0
Time: 7513ms
Built at: 2021-05-24 13:59:35
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相同项目 Vite 冷启动，耗时 924ms：</p>
<pre><code class="hljs language-bash copyable" lang="bash">> vite
Pre-bundling dependencies:
  vue
  element-plus
  @zcy/zcy-request
  element-plus/lib/utils/dom
(this will be run only when your dependencies or config have changed)
  vite v2.3.3 dev server running at:
  > Local: http://localhost:3000/
  > Network: use `--host` to expose
  ready <span class="hljs-keyword">in</span> 924ms.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>二次启动（预编译的依赖已存在），耗时 407ms；</p>
<pre><code class="hljs language-bash copyable" lang="bash">> vite
  vite v2.3.3 dev server running at:
  > Local: http://localhost:3000/
  > Network: use `--host` to expose
  ready <span class="hljs-keyword">in</span> 407ms.
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">总结</h3>
<p>使用 Vite 进行本地服务启动和热更新都会有明显的提效，至于编译打包环节的差异点有哪些？效果如何？你们还踩过哪些坑？留言告诉我吧。</p>
<p>推荐阅读：</p>
<p><a href="https://dev.to/iggredible/what-the-heck-are-cjs-amd-umd-and-esm-ikm?fileGuid=DDr3GGh6QRvQgWQC" target="_blank" rel="nofollow noopener noreferrer">What are CJS, AMD, UMD, and ESM in Javascript?</a></p>
<h2 data-id="heading-11">推荐阅读</h2>
<p><a href="https://juejin.cn/post/6974184935804534815" target="_blank">我在工作中是如何使用 git 的</a></p>
<p><a href="https://juejin.cn/post/6976798974757830687" target="_blank">15 分钟学会 Immutable</a></p>
<h2 data-id="heading-12">开源作品</h2>
<ul>
<li>政采云前端小报</li>
</ul>
<p><strong>开源地址 <a href="https://www.zoo.team/openweekly/" target="_blank" rel="nofollow noopener noreferrer">www.zoo.team/openweekly/</a></strong> (小报官网首页有微信交流群)</p>
<h2 data-id="heading-13">招贤纳士</h2>
<p>政采云前端团队（ZooTeam），一个年轻富有激情和创造力的前端团队，隶属于政采云产品研发部，Base 在风景如画的杭州。团队现有 40 余个前端小伙伴，平均年龄 27 岁，近 3 成是全栈工程师，妥妥的青年风暴团。成员构成既有来自于阿里、网易的“老”兵，也有浙大、中科大、杭电等校的应届新人。团队在日常的业务对接之外，还在物料体系、工程平台、搭建平台、性能体验、云端应用、数据分析及可视化等方向进行技术探索和实战，推动并落地了一系列的内部技术产品，持续探索前端技术体系的新边界。</p>
<p>如果你想改变一直被事折腾，希望开始能折腾事；如果你想改变一直被告诫需要多些想法，却无从破局；如果你想改变你有能力去做成那个结果，却不需要你；如果你想改变你想做成的事需要一个团队去支撑，但没你带人的位置；如果你想改变既定的节奏，将会是“5 年工作时间 3 年工作经验”；如果你想改变本来悟性不错，但总是有那一层窗户纸的模糊… 如果你相信相信的力量，相信平凡人能成就非凡事，相信能遇到更好的自己。如果你希望参与到随着业务腾飞的过程，亲手推动一个有着深入的业务理解、完善的技术体系、技术创造价值、影响力外溢的前端团队的成长历程，我觉得我们该聊聊。任何时间，等着你写点什么，发给 <code>ZooTeam@cai-inc.com</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d3aa3d1f8646a8bcda8cfd9e335a4b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            