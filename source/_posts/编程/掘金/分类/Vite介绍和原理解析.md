
---
title: 'Vite介绍和原理解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9301bff8140046ddaa3221a42d8ee2bf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 05:51:36 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9301bff8140046ddaa3221a42d8ee2bf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Vite号称是 <strong>下一代的前端开发和构建工具</strong> ，目前已经在前端社区里逐步开始流行起来了。它采用了全新的unbundle思想来提升整体的前端开发体验。比起传统的webpack构建，在性能速度上都有了质的提高。
那么接下来这篇文章，将主要介绍其使用方法和工作原理。</p>
<h1 data-id="heading-0">是什么</h1>
<p>Vite名字来源于法语, 意思为rapid，quickly。正好反映了其核心卖点—— <strong>"快速"</strong> 。在整体功能上实现了类似于预配置的webpack加dev server的功能， 用于提高前端项目的整体构建速度。
根据测试，服务器启动速度和HMR基本上都可以达到毫秒级别。</p>
<h1 data-id="heading-1">使用方法</h1>
<p>vite的使用方式十分简单，目前官方提供了脚手架来快速启动一个新项目:</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm init @vitejs/app

// yarn
yarn create @vitejs/app
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着就会进入交互式模式，让你选择对应的模板，输入项目名等操作。
如果需要手动指定模板和项目名，可以使用如下命令:</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm init @vitejs/app my-vite-demo --template react
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里指定的所有相关项目模板都可以在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fawesome-vite%23templates" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/awesome-vite#templates" ref="nofollow noopener noreferrer">github.com/vitejs/awes…</a> 仓库中找到。
项目启动后，就可以直接使用如下命令进行启动和预览了</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装依赖</span>
yarn install

<span class="hljs-comment"># 开发环境下使用</span>
yarn dev

<span class="hljs-comment"># 打包</span>
yarn run build
<span class="hljs-comment"># 用来预览打包后的效果</span>
yarn run serve
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">插件机制</h1>
<p>vite主要使用插件进行扩展功能，可以看到上述最简单的初始化项目启动后，在其配置文件 <code>vite.config.ts</code> 文件下，有如下代码：</p>
<pre><code class="hljs language-coffeescript copyable" lang="coffeescript"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> reactRefresh <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-react-refresh'</span>

<span class="hljs-regexp">//</span> [https:](https:<span class="hljs-regexp">//vitejs.dev/config/</span>)[<span class="hljs-regexp">//vitejs.dev/config/</span>](https:<span class="hljs-regexp">//vitejs.dev/config/</span>)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  plugins: [reactRefresh()]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这里引用了一个名为 <code>reactRefresh</code> 的插件, 这个插件可以在修改react组件的时候，不丢失其状态。
同样的，如果有需要实现其他额外的功能，都可以借助vite的插件机制进行扩展。这些第三方插件模块可以通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fawesome-vite%23plugins" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/awesome-vite#plugins" ref="nofollow noopener noreferrer">github.com/vitejs/awes…</a> 这个仓库找到。
同时，由于vite插件扩展了rollup的接口，所以要实现一个自己的vite插件跟写rollup插件是类似的。此处，可以参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2Fguide%2Fapi-plugin.html" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/guide/api-plugin.html" ref="nofollow noopener noreferrer">插件 API | Vite 官方中文文档</a> 。</p>
<h1 data-id="heading-3">工作原理</h1>
<p>上面介绍了这么多，那么Vite是如何实现超快速的开发体验的呢？
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Ftree%2Fmain%2Fpackages" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/tree/main/packages" ref="nofollow noopener noreferrer">github.com/vitejs/vite…</a>
我们都知道，传统打包构建工具，在服务器启动之前，需要从入口文件完整解析构建整个应用。因此，有大量的时间都花在了依赖生成，构建编译上。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9301bff8140046ddaa3221a42d8ee2bf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而vite主要遵循的是使用ESM(Es modules模块)的规范来执行代码，由于现代浏览器基本上都支持了ESM规范，所以在开发阶段并不需要将代码打包编译成es5模块即可在浏览器上运行。我们只需要从入口文件出发， 在遇到对应的 <code>import</code> 语句时，将对应的模块加载到浏览器中就可以了。因此，这种不需要打包的特性，也是vite的速度能够如此快速的原因。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdd41182ac21413dae16800f1e24cdda~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时ts/jsx等文件的转译工作也会借助了esbuild来提升速度。
Vite在内部实现上，会启动一个dev server， 并接受独立模块的HTTP请求，并让浏览器自身去解析和处理模块加载。
下面以官方提供的demo为例，可以看到运行后，在访问对应页面的时候，不是加载一整个的bundle.js文件，而是按模块去加载。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4164f6569154e5d9bda666b900f9d46~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从代码实现上，在允许 <code>yarn dev</code> 命令后，Vite就会启动一个dev server，然后加载各种中间件，进而监听对应的前端访问请求。
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fcli.ts%23L80" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/main/packages/vite/src/node/cli.ts#L80" ref="nofollow noopener noreferrer">github.com/vitejs/vite…</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; createServer &#125; = <span class="hljs-keyword">await</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./server'</span>)
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
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，会在开发环境中注入Vite自身的client客户端代码，用于监听HMR等处理。 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fserver%2Fmiddlewares%2FindexHtml.ts%23L141" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/main/packages/vite/src/node/server/middlewares/indexHtml.ts#L141" ref="nofollow noopener noreferrer">github.com/vitejs/vite…</a></p>
<h2 data-id="heading-4">裸模块重写</h2>
<p>由于目前ESM不支持类似 <code>import vue from "vue"</code> 这样的裸模块加载（import maps 提案 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FWICG%2Fimport-maps" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/WICG/import-maps" ref="nofollow noopener noreferrer">github.com/WICG/import…</a> 可解决这个问题，但还未实现），所以需要对模块加载地址进行重写操作。将其转换成类似于 <code>import vue from "/</code> <code>@modules/vue"</code> 这种形式。
实现原理上主要通过 <code>es-module-lexer</code> 和 <code>magic-string</code> 两个包进行替换，比起AST语义解析和转换，在性能上更有优势。
下面介绍一下这两个包：</p>
<h2 data-id="heading-5">Es-module-lexer</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fguybedford%2Fes-module-lexer" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/guybedford/es-module-lexer" ref="nofollow noopener noreferrer">github.com/guybedford/…</a>
虽然js代码的词法分析通常都使用babel, acorn等工具，但是针对ESM文件来说，使用es-module-lexer库在性能上能够有很大的提升，其压缩后的体积只有4kb，而且根据官方给出的例子720kb的Angular1库经过acorn解析要超过100ms，而使用es-module-lexer库只需要5ms, 在性能上提升了将近20倍。</p>
<h3 data-id="heading-6">Magic-string</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frich-harris%2Fmagic-string%23readme" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rich-harris/magic-string#readme" ref="nofollow noopener noreferrer">github.com/rich-harris…</a>
vite中使用了大量这个库做一些字符串的替换工作，从而避免操作AST。具体代码可以参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fplugins%2FimportAnalysis.ts%23L155" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/main/packages/vite/src/node/plugins/importAnalysis.ts#L155" ref="nofollow noopener noreferrer">github.com/vitejs/vite…</a>
整体思路大概类似于下面代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; init, parse <span class="hljs-keyword">as</span> parseImports, ImportSpecifier &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'es-module-lexer'</span>

<span class="hljs-comment">// 借助es-module-lexer来分析import语句</span>
imports = parseImports(source)[<span class="hljs-number">0</span>]

<span class="hljs-comment">// 接着在依赖分析及路径重写过程中利用magic-string来替换源码。</span>
<span class="hljs-keyword">let</span> s: MagicString | <span class="hljs-literal">undefined</span>
<span class="hljs-keyword">const</span> str = <span class="hljs-function">() =></span> s || (s = <span class="hljs-keyword">new</span> MagicString(source))

<span class="hljs-comment">// 省略部分代码</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; index < imports.length; index++) &#123;
        <span class="hljs-keyword">const</span> &#123;
          <span class="hljs-attr">s</span>: start,
          <span class="hljs-attr">e</span>: end,
          <span class="hljs-attr">ss</span>: expStart,
          <span class="hljs-attr">se</span>: expEnd,
          <span class="hljs-attr">d</span>: dynamicIndex,
          <span class="hljs-attr">n</span>: specifier
        &#125; = imports[index]

<span class="hljs-comment">// 省略部分代码</span>

<span class="hljs-comment">// 解析代码</span>
 <span class="hljs-keyword">const</span> &#123; imports, importsString, exp, endIndex, base, pattern &#125; =
              <span class="hljs-keyword">await</span> transformImportGlob(
                source,
                start,
                importer,
                index,
                root,
                normalizeUrl
              )
            str().prepend(importsString)
            str().overwrite(expStart, endIndex, exp)
            imports.forEach(<span class="hljs-function">(<span class="hljs-params">url</span>) =></span> importedUrls.add(url.replace(base, <span class="hljs-string">'/'</span>)))
            <span class="hljs-keyword">if</span> (!(importerModule.file! <span class="hljs-keyword">in</span> server._globImporters)) &#123;
              server._globImporters[importerModule.file!] = &#123;
                <span class="hljs-attr">module</span>: importerModule,
                <span class="hljs-attr">importGlobs</span>: []
              &#125;
            &#125;
            server._globImporters[importerModule.file!].importGlobs.push(&#123;
              base,
              pattern
            &#125;)
&#125;

<span class="hljs-comment">// 最终返回处理过的代码 </span>
<span class="hljs-keyword">if</span> (s) &#123;
  <span class="hljs-keyword">return</span> s.toString()
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-keyword">return</span> source
&#125;       
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">自定义区块处理</h3>
<p>这个功能是通过在模块后面链接 <code>?type=</code> 的参数来区分不同区块。然后针对每个区块单独进行处理。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a55ddb29acf411b842c24477a2e6048~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据不同的区块类型，在transform的时候会使用不同的插件进行编译。
下面以json文件为例，在处理 <code>xxx.json</code> 为结尾的文件的时候，首先json插件会匹配模块的id名是否是json。接着再进行转译工作。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">
<span class="hljs-comment">// Custom json filter for vite</span>
<span class="hljs-keyword">const</span> jsonExtRE = <span class="hljs-regexp">/\.json($|\?)(?!commonjs-proxy)/</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jsonPlugin</span>(<span class="hljs-params">
  options: JsonOptions = &#123;&#125;,
  isBuild: <span class="hljs-built_in">boolean</span>
</span>): <span class="hljs-title">Plugin</span> </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'vite:json'</span>,

    <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params">json, id</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!jsonExtRE.test(id)) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
      <span class="hljs-keyword">if</span> (SPECIAL_QUERY_RE.test(id)) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>

      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">if</span> (options.stringify) &#123;
          <span class="hljs-keyword">if</span> (isBuild) &#123;
            <span class="hljs-keyword">return</span> &#123;
              <span class="hljs-attr">code</span>: <span class="hljs-string">`export default JSON.parse(<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(
                <span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-built_in">JSON</span>.parse(json))
              )&#125;</span>)`</span>,
              <span class="hljs-attr">map</span>: &#123; <span class="hljs-attr">mappings</span>: <span class="hljs-string">''</span> &#125;
            &#125;
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">`export default JSON.parse(<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(json)&#125;</span>)`</span>
          &#125;
        &#125;

        <span class="hljs-keyword">const</span> parsed = <span class="hljs-built_in">JSON</span>.parse(json)
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">code</span>: dataToEsm(parsed, &#123;
            <span class="hljs-attr">preferConst</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">namedExports</span>: options.namedExports
          &#125;),
          <span class="hljs-attr">map</span>: &#123; <span class="hljs-attr">mappings</span>: <span class="hljs-string">''</span> &#125;
        &#125;
      &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        <span class="hljs-keyword">const</span> errorMessageList = <span class="hljs-regexp">/[\d]+/</span>.exec(e.message)
        <span class="hljs-keyword">const</span> position = errorMessageList && <span class="hljs-built_in">parseInt</span>(errorMessageList[<span class="hljs-number">0</span>], <span class="hljs-number">10</span>)
        <span class="hljs-keyword">const</span> msg = position
          ? <span class="hljs-string">`, invalid JSON syntax found at line <span class="hljs-subst">$&#123;position&#125;</span>`</span>
          : <span class="hljs-string">`.`</span>
        <span class="hljs-built_in">this</span>.error(<span class="hljs-string">`Failed to parse JSON file`</span> + msg, e.idx)
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">HMR</h2>
<p>热更新是前端开发体验中很重要的一环，那么Vite中主要依赖以下几个步骤来实现HMR的功能：</p>
<ol>
<li>在重写模块地址的时候，记录模块依赖链 <code>importMaps</code> 。 这样在后续更新的时候，可以知道哪些文件需要被热更新。</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c2759cf7e1a45f186c3be7d95fd2f07~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>代码中可以使用 <code>import.meta.hot</code> 接口来标记"HMR Boundary"。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbbd2e04a2b2442ea1fd260161b2355f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>接着，当文件更新的时候，会沿着之前记录下 <code>imoprtMaps</code> 链式结构找到对应的"HMR Boundary"， 再从此处重新加载对应更新的模块。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6da18cf30024c85a81fec400569d99c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80431aef5d454423aa494c2022d8ea65~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>如果没有遇到对应的boundary, 则整个应用重新刷新。</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df73c540bd9c4143ae4e7ec3f64333cf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用方法如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> foo <span class="hljs-keyword">from</span> <span class="hljs-string">'./foo.js'</span>

foo()

<span class="hljs-keyword">if</span> (<span class="hljs-keyword">import</span>.meta.hot) &#123;
    <span class="hljs-keyword">import</span>.meta.hot.accept(<span class="hljs-string">'./foo.js'</span>, <span class="hljs-function">(<span class="hljs-params">newFoo</span>) =></span> &#123;
        newFoo.foo()
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面将以具体代码进行介绍其原理。
客户端逻辑：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fplugins%2FimportAnalysis.ts%23L399" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/main/packages/vite/src/node/plugins/importAnalysis.ts#L399" ref="nofollow noopener noreferrer">github.com/vitejs/vite…</a></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// record for HMR import chain analysis</span>
<span class="hljs-comment">// make sure to normalize away base</span>
importedUrls.add(url.replace(base, <span class="hljs-string">'/'</span>))

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">if</span> (hasHMR && !ssr) &#123;
  debugHmr(
    <span class="hljs-string">`<span class="hljs-subst">$&#123;
      isSelfAccepting
        ? <span class="hljs-string">`[self-accepts]`</span>
        : acceptedUrls.size
        ? <span class="hljs-string">`[accepts-deps]`</span>
        : <span class="hljs-string">`[detected api usage]`</span>
    &#125;</span> <span class="hljs-subst">$&#123;prettyImporter&#125;</span>`</span>
  )
  <span class="hljs-comment">// 在用户业务代码中注入Vite客户端代码</span>
  str().prepend(
    <span class="hljs-string">`import &#123; createHotContext as __vite__createHotContext &#125; from "<span class="hljs-subst">$&#123;clientPublicPath&#125;</span>";`</span> +
      <span class="hljs-string">`import.meta.hot = __vite__createHotContext(<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(
        importerModule.url
      )&#125;</span>);`</span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2Fsrc%2Fclient%2Fclient.ts%23L70" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/main/packages/vite/src/client/client.ts#L70" ref="nofollow noopener noreferrer">github.com/vitejs/vite…</a></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">case</span> <span class="hljs-string">'update'</span>:
     notifyListeners(<span class="hljs-string">'vite:beforeUpdate'</span>, payload)
      <span class="hljs-comment">// 发生错误的时候，重新加载整个页面</span>
      <span class="hljs-keyword">if</span> (isFirstUpdate && hasErrorOverlay()) &#123;
        <span class="hljs-built_in">window</span>.location.reload()
        <span class="hljs-keyword">return</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        clearErrorOverlay()
        isFirstUpdate = <span class="hljs-literal">false</span>
      &#125;
      
      payload.updates.forEach(<span class="hljs-function">(<span class="hljs-params">update</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (update.type === <span class="hljs-string">'js-update'</span>) &#123;
          <span class="hljs-comment">// js更新逻辑， 会进入一个缓存队列，批量更新，从而保证更新顺序</span>
          queueUpdate(fetchUpdate(update))
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// css更新逻辑， 检测到更新的时候，直接替换对应模块的链接，重新发起请求</span>
          <span class="hljs-keyword">let</span> &#123; path, timestamp &#125; = update
          path = path.replace(<span class="hljs-regexp">/\?.*/</span>, <span class="hljs-string">''</span>)

          <span class="hljs-keyword">const</span> el = (
            [].slice.call(
              <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">`link`</span>)
            ) <span class="hljs-keyword">as</span> HTMLLinkElement[]
          ).find(<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> e.href.includes(path))
          <span class="hljs-keyword">if</span> (el) &#123;
            <span class="hljs-keyword">const</span> newPath = <span class="hljs-string">`<span class="hljs-subst">$&#123;path&#125;</span><span class="hljs-subst">$&#123;
              path.includes(<span class="hljs-string">'?'</span>) ? <span class="hljs-string">'&'</span> : <span class="hljs-string">'?'</span>
            &#125;</span>t=<span class="hljs-subst">$&#123;timestamp&#125;</span>`</span>
            el.href = <span class="hljs-keyword">new</span> URL(newPath, el.href).href
          &#125;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`[vite] css hot updated: <span class="hljs-subst">$&#123;path&#125;</span>`</span>)
        &#125;
      &#125;)
      <span class="hljs-keyword">break</span>
<span class="hljs-keyword">break</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>服务端处理HMR模块更新逻辑: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fserver%2Fhmr.ts%23L42" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/main/packages/vite/src/node/server/hmr.ts#L42" ref="nofollow noopener noreferrer">github.com/vitejs/vite…</a></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleHMRUpdate</span>(<span class="hljs-params">
  file: <span class="hljs-built_in">string</span>,
  server: ViteDevServer
</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">any</span>> </span>&#123;
  <span class="hljs-keyword">const</span> &#123; ws, config, moduleGraph &#125; = server
  <span class="hljs-keyword">const</span> shortFile = getShortName(file, config.root)

  <span class="hljs-keyword">const</span> isConfig = file === config.configFile
  <span class="hljs-keyword">const</span> isConfigDependency = config.configFileDependencies.some(
    <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> file === path.resolve(name)
  )
  <span class="hljs-keyword">const</span> isEnv = config.inlineConfig.envFile !== <span class="hljs-literal">false</span> && file.endsWith(<span class="hljs-string">'.env'</span>)
  <span class="hljs-keyword">if</span> (isConfig || isConfigDependency || isEnv) &#123;
    <span class="hljs-comment">// 重启server</span>
    <span class="hljs-keyword">await</span> restartServer(server)
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-comment">// (dev only) the client itself cannot be hot updated.</span>
  <span class="hljs-keyword">if</span> (file.startsWith(normalizedClientDir)) &#123;
    ws.send(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'full-reload'</span>,
      <span class="hljs-attr">path</span>: <span class="hljs-string">'*'</span>
    &#125;)
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-keyword">const</span> mods = moduleGraph.getModulesByFile(file)

  <span class="hljs-comment">// check if any plugin wants to perform custom HMR handling</span>
  <span class="hljs-keyword">const</span> timestamp = <span class="hljs-built_in">Date</span>.now()
  <span class="hljs-keyword">const</span> hmrContext: HmrContext = &#123;
    file,
    timestamp,
    <span class="hljs-attr">modules</span>: mods ? [...mods] : [],
    <span class="hljs-attr">read</span>: <span class="hljs-function">() =></span> readModifiedFile(file),
    server
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> plugin <span class="hljs-keyword">of</span> config.plugins) &#123;
    <span class="hljs-keyword">if</span> (plugin.handleHotUpdate) &#123;
      <span class="hljs-keyword">const</span> filteredModules = <span class="hljs-keyword">await</span> plugin.handleHotUpdate(hmrContext)
      <span class="hljs-keyword">if</span> (filteredModules) &#123;
        hmrContext.modules = filteredModules
      &#125;
    &#125;
  &#125;

  <span class="hljs-keyword">if</span> (!hmrContext.modules.length) &#123;
    <span class="hljs-comment">// html file cannot be hot updated</span>
    <span class="hljs-keyword">if</span> (file.endsWith(<span class="hljs-string">'.html'</span>)) &#123;
      [config.logger.info](http:<span class="hljs-comment">//config.logger.info/)(chalk.green(`page reload `) + chalk.dim(shortFile), &#123;</span>
        clear: <span class="hljs-literal">true</span>,
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
    <span class="hljs-keyword">return</span>
  &#125;

  updateModules(shortFile, hmrContext.modules, timestamp, server)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateModules</span>(<span class="hljs-params">
  file: <span class="hljs-built_in">string</span>,
  modules: ModuleNode[],
  timestamp: <span class="hljs-built_in">number</span>,
  &#123; config, ws &#125;: ViteDevServer
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> updates: Update[] = []
  <span class="hljs-keyword">const</span> invalidatedModules = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span><ModuleNode>()
  <span class="hljs-keyword">let</span> needFullReload = <span class="hljs-literal">false</span>

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> mod <span class="hljs-keyword">of</span> modules) &#123;
    invalidate(mod, timestamp, invalidatedModules)
    <span class="hljs-keyword">if</span> (needFullReload) &#123;
      <span class="hljs-keyword">continue</span>
    &#125;

    <span class="hljs-keyword">const</span> boundaries = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span><&#123;
      <span class="hljs-attr">boundary</span>: ModuleNode
      <span class="hljs-attr">acceptedVia</span>: ModuleNode
    &#125;>()
    
    <span class="hljs-comment">// 向上传递更新，直到遇到边界</span>
    <span class="hljs-keyword">const</span> hasDeadEnd = propagateUpdate(mod, timestamp, boundaries)
    <span class="hljs-keyword">if</span> (hasDeadEnd) &#123;
      needFullReload = <span class="hljs-literal">true</span>
      <span class="hljs-keyword">continue</span>
    &#125;

    updates.push(
      ...[...boundaries].map(<span class="hljs-function">(<span class="hljs-params">&#123; boundary, acceptedVia &#125;</span>) =></span> (&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;boundary.<span class="hljs-keyword">type</span>&#125;</span>-update`</span> <span class="hljs-keyword">as</span> Update[<span class="hljs-string">'type'</span>],
        timestamp,
        <span class="hljs-attr">path</span>: boundary.url,
        <span class="hljs-attr">acceptedPath</span>: acceptedVia.url
      &#125;))
    )
  &#125;

  <span class="hljs-keyword">if</span> (needFullReload) &#123;
    <span class="hljs-comment">// 重刷页面</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
   <span class="hljs-comment">// 相ws客户端发送更新事件， Websocket 监听模块更新, 并且做对应的处理。</span>
    ws.send(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'update'</span>,
      updates
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb12aee7b333442dbde7a9315c39e236~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">优化策略</h2>
<p>由于vite打包是让浏览器一个个模块去加载的，因此，就很容易存在http请求的瀑布流问题（浏览器并发一次最多6个请求）。此次，vite内部为了解决这个问题，主要采取了3个方案。</p>
<ol>
<li>
<p>预打包，确保每个依赖只对应一个请求/文件。比如lodash。此处可以参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2Fsrc%2Fnode%2Foptimizer%2FesbuildDepPlugin.ts%23L73" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/main/packages/vite/src/node/optimizer/esbuildDepPlugin.ts#L73" ref="nofollow noopener noreferrer">github.com/vitejs/vite…</a></p>
</li>
<li>
<p>代码分割code split。可以借助rollup内置的 <code>manualChunks</code> 来实现。</p>
</li>
<li>
<p>Etag 304状态码，让浏览器在重复加载的时候直接使用浏览器缓存。</p>
</li>
</ol>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fserver%2Fmiddlewares%2Ftransform.ts%23L155" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/main/packages/vite/src/node/server/middlewares/transform.ts#L155" ref="nofollow noopener noreferrer">github.com/vitejs/vite…</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// check if we can return 304 early</span>
<span class="hljs-keyword">const</span> ifNoneMatch = req.headers[<span class="hljs-string">'if-none-match'</span>]
<span class="hljs-keyword">if</span> (
  ifNoneMatch &&
  (<span class="hljs-keyword">await</span> moduleGraph.getModuleByUrl(url))?.transformResult?.etag ===
    ifNoneMatch
) &#123;
  isDebug && debugCache(<span class="hljs-string">`[304] <span class="hljs-subst">$&#123;prettifyUrl(url, root)&#125;</span>`</span>)
  res.statusCode = <span class="hljs-number">304</span>
  <span class="hljs-keyword">return</span> res.end()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">esbuild的使用</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2Fmain%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fplugins%2Fesbuild.ts%23L82" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/main/packages/vite/src/node/plugins/esbuild.ts#L82" ref="nofollow noopener noreferrer">github.com/vitejs/vite…</a>
利用esbuild来转换ts/jsx文件，从而更快地提升编译速度。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformWithEsbuild</span>(<span class="hljs-params">
  code: <span class="hljs-built_in">string</span>,
  filename: <span class="hljs-built_in">string</span>,
  options?: TransformOptions,
  inMap?: <span class="hljs-built_in">object</span>
</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">ESBuildTransformResult</span>> </span>&#123;
  <span class="hljs-comment">// if the id ends with a valid ext, use it (e.g. vue blocks)</span>
  <span class="hljs-comment">// otherwise, cleanup the query before checking the ext</span>
  <span class="hljs-keyword">const</span> ext = path.extname(
    <span class="hljs-regexp">/\.\w+$/</span>.test(filename) ? filename : cleanUrl(filename)
  )

  <span class="hljs-keyword">let</span> loader = ext.slice(<span class="hljs-number">1</span>)
  <span class="hljs-keyword">if</span> (loader === <span class="hljs-string">'cjs'</span> || loader === <span class="hljs-string">'mjs'</span>) &#123;
    loader = <span class="hljs-string">'js'</span>
  &#125;

  <span class="hljs-keyword">const</span> resolvedOptions = &#123;
    <span class="hljs-attr">loader</span>: loader <span class="hljs-keyword">as</span> Loader,
    <span class="hljs-attr">sourcemap</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// ensure source file name contains full query</span>
    <span class="hljs-attr">sourcefile</span>: filename,
    ...options
  &#125; <span class="hljs-keyword">as</span> ESBuildOptions

  <span class="hljs-keyword">delete</span> resolvedOptions.include
  <span class="hljs-keyword">delete</span> resolvedOptions.exclude
  <span class="hljs-keyword">delete</span> resolvedOptions.jsxInject

  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> transform(code, resolvedOptions)
    <span class="hljs-keyword">if</span> (inMap) &#123;
      <span class="hljs-keyword">const</span> nextMap = <span class="hljs-built_in">JSON</span>.parse(result.map)
      nextMap.sourcesContent = []
      <span class="hljs-keyword">return</span> &#123;
        ...result,
        <span class="hljs-attr">map</span>: combineSourcemaps(filename, [
          nextMap <span class="hljs-keyword">as</span> RawSourceMap,
          inMap <span class="hljs-keyword">as</span> RawSourceMap
        ]) <span class="hljs-keyword">as</span> SourceMap
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        ...result,
        <span class="hljs-attr">map</span>: <span class="hljs-built_in">JSON</span>.parse(result.map)
      &#125;
    &#125;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    debug(<span class="hljs-string">`esbuild error with options used: `</span>, resolvedOptions)
    <span class="hljs-comment">// patch error information</span>
    <span class="hljs-keyword">if</span> (e.errors) &#123;
      e.frame = <span class="hljs-string">''</span>
      e.errors.forEach(<span class="hljs-function">(<span class="hljs-params">m: Message</span>) =></span> &#123;
        e.frame += <span class="hljs-string">`\n`</span> + prettifyMessage(m, code)
      &#125;)
      e.loc = e.errors[<span class="hljs-number">0</span>].location
    &#125;
    <span class="hljs-keyword">throw</span> e
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">总结</h1>
<p>总体来说，Vite在前端构建工具领域上开辟了一条和webpack完全不同的道路，很好地解决了前端开发阶段构建速度慢的问题。预计将会使前端开发体验上更上一层楼。同时，vite.js的源码也在不停迭代过程中，如果有想要更加了解其具体的实现细节，还是希望能够亲自去阅读其源码。本文主要希望能够起到抛砖引玉的作用。</p>
<h1 data-id="heading-12">参考文档</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2Fguide%2F%23overview" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/guide/#overview" ref="nofollow noopener noreferrer">cn.vitejs.dev/guide/#over…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DxXrhg26VCSc" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/watch?v=xXrhg26VCSc" ref="nofollow noopener noreferrer">www.youtube.com/watch?v=xXr…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DfgwSJ-xXUTY" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/watch?v=fgwSJ-xXUTY" ref="nofollow noopener noreferrer">www.youtube.com/watch?v=fgw…</a></p></div>  
</div>
            