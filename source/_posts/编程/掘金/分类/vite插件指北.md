
---
title: 'vite插件指北'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e229d9ff7880440bafcc5f188486defc~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 01:37:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e229d9ff7880440bafcc5f188486defc~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">vite插件机制</h3>
<h4 data-id="heading-1">命名约定</h4>
<p>如果插件不使用 Vite 特有的钩子，可以实现为 <a href="https://cn.vitejs.dev/guide/api-plugin.html#Rollup-%E6%8F%92%E4%BB%B6%E5%85%BC%E5%AE%B9%E6%80%A7" target="_blank" rel="nofollow noopener noreferrer">兼容的 Rollup 插件</a>，推荐使用 <a href="https://rollupjs.org/guide/en/#conventions" target="_blank" rel="nofollow noopener noreferrer">Rollup 插件名称约定</a>。</p>
<ul>
<li>Rollup 插件应该有一个带 <code>rollup-plugin-</code> 前缀、语义清晰的名称。</li>
<li>在 package.json 中包含 <code>rollup-plugin</code> 和 <code>vite-plugin</code> 关键字。</li>
</ul>
<p>这样，插件也可以用于纯 Rollup 或基于 WMR 的项目。</p>
<p>对于 Vite 专属的插件：</p>
<ul>
<li>Vite 插件应该有一个带 <code>vite-plugin-</code> 前缀、语义清晰的名称。</li>
<li>在 package.json 中包含 <code>vite-plugin</code> 关键字。</li>
<li>在插件文档增加一部分关于为什么本插件是一个 Vite 专属插件的详细说明（如，本插件使用了 Vite 特有的插件钩子）。</li>
</ul>
<p>如果你的插件只适用于特定的框架，它的名字应该遵循以下前缀格式：</p>
<ul>
<li><code>vite-plugin-vue-</code> 前缀作为 Vue 插件</li>
<li><code>vite-plugin-react-</code> 前缀作为 React 插件</li>
<li><code>vite-plugin-svelte-</code> 前缀作为 Svelte 插件</li>
</ul>
<h4 data-id="heading-2">插件配置</h4>
<p>用户会将插件添加到项目的 <code>devDependencies</code> 中并使用数组形式的 <code>plugins</code> 选项配置它们。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> vitePlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-feature'</span>
<span class="hljs-keyword">import</span> rollupPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-feature'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">plugins</span>: [vitePlugin(), rollupPlugin()]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假值的插件将被忽略，可以用来轻松地启用或停用插件。</p>
<p><code>plugins</code> 也可以接受将多个插件作为单个元素的预设。这对于使用多个插件实现的复杂特性（如框架集成）很有用。该数组将在内部被扁平化（flatten）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 框架插件</span>
<span class="hljs-keyword">import</span> frameworkRefresh <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-framework-refresh'</span>
<span class="hljs-keyword">import</span> frameworkDevtools <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-framework-devtools'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">framework</span>(<span class="hljs-params">config</span>) </span>&#123;
  <span class="hljs-keyword">return</span> [frameworkRefresh(config), frameworkDevTools(config)]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vite.config.js</span>
<span class="hljs-keyword">import</span> framework <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-framework'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">plugins</span>: [framework()]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">简单示例</h4>
<h6 data-id="heading-4">引入一个虚拟文件</h6>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myPlugin</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> virtualFileId = <span class="hljs-string">'@my-virtual-file'</span>
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'my-plugin'</span>, <span class="hljs-comment">// 必须的，将会显示在 warning 和 error 中</span>
    <span class="hljs-function"><span class="hljs-title">resolveId</span>(<span class="hljs-params">id</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (id === virtualFileId) &#123;
        <span class="hljs-keyword">return</span> virtualFileId
      &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">load</span>(<span class="hljs-params">id</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (id === virtualFileId) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`export const msg = "from virtual file"`</span> <span class="hljs-comment">// 替换文件内容</span>
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这使得可以在 JavaScript 中引入这些文件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; msg &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@my-virtual-file'</span>
<span class="hljs-built_in">console</span>.log(msg) <span class="hljs-comment">//  from virtual file</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-5">转换自定义文件类型</h6>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fileRegex = <span class="hljs-regexp">/\.(my-file-ext)$/</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myPlugin</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'transform-file'</span>,
    <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params">src, id</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (fileRegex.test(id)) &#123;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">code</span>: compileFileToJS(src), <span class="hljs-comment">// 文件类型转换</span>
          <span class="hljs-attr">map</span>: <span class="hljs-literal">null</span> <span class="hljs-comment">// 如果可行将提供 source map</span>
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">通用钩子</h4>
<p>在开发中，Vite 开发服务器会创建一个插件容器来调用 <a href="https://rollupjs.org/guide/en/#build-hooks" target="_blank" rel="nofollow noopener noreferrer">Rollup 构建钩子</a>，与 Rollup 如出一辙。</p>
<h5 data-id="heading-7">以下钩子在服务器启动时被调用</h5>
<ul>
<li><code>options</code></li>
<li><code>buildStart</code></li>
</ul>
<h6 data-id="heading-8">options</h6>
<ul>
<li>Type: ( inputOptions ) => options</li>
</ul>
<p>rollup打包的第一个钩子，在rollup完全配置完成之前，用来替换或者操作rollup的配置，返回null，表示不做任何操作，如果简单的只是为了读rollup的配置文件，那么可以在<code>buildStart</code>这个钩子里面去获取；同时，它是rollup所有钩子里唯一一个无法获取 <a href="https://rollupjs.org/guide/en/#plugin-context" target="_blank" rel="nofollow noopener noreferrer">plugin context</a> 的钩子，这个钩子应该一般很少用到。</p>
<h6 data-id="heading-9">buildStart</h6>
<ul>
<li>Type: <code>(options: InputOptions) => void</code></li>
<li>Previous Hook: <a href="https://rollupjs.org/guide/en/#options" target="_blank" rel="nofollow noopener noreferrer"><code>options</code></a></li>
<li>Next Hook: <a href="https://rollupjs.org/guide/en/#resolveid" target="_blank" rel="nofollow noopener noreferrer"><code>resolveId</code></a></li>
</ul>
<p>跟在options钩子后面，在rollup构建时候触发，主要用来获取rollup的配置</p>
<h5 data-id="heading-10">以下钩子会在每个模块请求时调用</h5>
<h6 data-id="heading-11">resolveId</h6>
<ul>
<li>Type: <code>(importee, importer) => (id|Promise)</code></li>
<li>Previous Hook: <a href="https://rollupjs.org/guide/en/#buildstart" target="_blank" rel="nofollow noopener noreferrer"><code>buildStart</code></a>、<a href="https://rollupjs.org/guide/en/#moduleparsed" target="_blank" rel="nofollow noopener noreferrer"><code>moduleParsed</code></a>、<a href="https://rollupjs.org/guide/en/#resolvedynamicimport" target="_blank" rel="nofollow noopener noreferrer"><code>resolveDynamicImport</code></a>.</li>
<li>Next Hook: <a href="https://rollupjs.org/guide/en/#load" target="_blank" rel="nofollow noopener noreferrer"><code>load</code></a></li>
</ul>
<p>如果配置了<a href="https://rollupjs.org/guide/en/#buildstart" target="_blank" rel="nofollow noopener noreferrer"><code>buildStart</code></a>、<a href="https://rollupjs.org/guide/en/#moduleparsed" target="_blank" rel="nofollow noopener noreferrer"><code>moduleParsed</code></a>、<a href="https://rollupjs.org/guide/en/#resolvedynamicimport" target="_blank" rel="nofollow noopener noreferrer"><code>resolveDynamicImport</code></a>、那么resolveId钩子会跟在前面三个钩子后面依次触发；需要说明一下，<a href="https://rollupjs.org/guide/en/#moduleparsed" target="_blank" rel="nofollow noopener noreferrer"><code>moduleParsed</code></a>和<a href="https://rollupjs.org/guide/en/#resolvedynamicimport" target="_blank" rel="nofollow noopener noreferrer"><code>resolveDynamicImport</code></a>这两个钩子在rollup的serve(开发模式)下并不会用到。在某个插件触发<a href="https://rollupjs.org/guide/en/#thisemitfileemittedfile-emittedchunk--emittedasset--string" target="_blank" rel="nofollow noopener noreferrer"><code>this.emitFile</code></a>或者<a href="https://rollupjs.org/guide/en/#thisresolvesource-string-importer-string-options-skipself-boolean-custom-plugin-string-any--promiseid-string-external-boolean--absolute-modulesideeffects-boolean--no-treeshake-syntheticnamedexports-boolean--string-meta-plugin-string-any--null" target="_blank" rel="nofollow noopener noreferrer"><code>this.resolve</code></a> 手动resolve一个id的时候，就会触发resolveId钩子；返回null，表示采用默认的解析方式；返回false，表示importee被作为外部模块，不会打包进bundle。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">resolveId</span>(<span class="hljs-params">importee,importer</span>)</span> &#123;
  <span class="hljs-comment">// importee表示的是chunk本身，importer表示引入importee的chunk</span>
  <span class="hljs-comment">// 例如我在App.tsx里面引入了上面虚拟文件的内容，则importee = @my-virtual-file，importer = App.tsx的绝对路径</span>
  <span class="hljs-keyword">if</span> (!importer) &#123;
    <span class="hljs-comment">// We need to skip this plugin to avoid an infinite loop</span>
    <span class="hljs-keyword">const</span> resolution = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.resolve(importee, <span class="hljs-literal">undefined</span>, &#123; <span class="hljs-attr">skipSelf</span>: <span class="hljs-literal">true</span> &#125;);
    <span class="hljs-comment">// If it cannot be resolved, return `null` so that Rollup displays an error</span>
    <span class="hljs-keyword">if</span> (!resolution) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;resolution.id&#125;</span>?entry-proxy`</span>;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
&#125;,
<span class="hljs-function"><span class="hljs-title">load</span>(<span class="hljs-params">id</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (id.endsWith(<span class="hljs-string">'?entry-proxy'</span>)) &#123;
    <span class="hljs-comment">// get resolution.id</span>
    <span class="hljs-keyword">const</span> importee = id.slice(<span class="hljs-number">0</span>, -<span class="hljs-string">'?entry-proxy'</span>.length);
    <span class="hljs-comment">// Note that this will throw if there is no default export</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">`export &#123;default&#125; from '<span class="hljs-subst">$&#123;importee&#125;</span>';`</span>;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-12">load</h6>
<ul>
<li>Type: <code>(id: string) => string | null | &#123;code: string, map?: string | SourceMap, ast? : ESTree.Program, moduleSideEffects?: boolean | "no-treeshake" | null, syntheticNamedExports?: boolean | string | null, meta?: &#123;[plugin: string]: any&#125; | null&#125;</code></li>
<li>Previous Hook: <a href="https://rollupjs.org/guide/en/#resolveid" target="_blank" rel="nofollow noopener noreferrer"><code>resolveId</code></a> or <a href="https://rollupjs.org/guide/en/#resolvedynamicimport" target="_blank" rel="nofollow noopener noreferrer"><code>resolveDynamicImport</code></a></li>
<li>Next Hook: <a href="https://rollupjs.org/guide/en/#transform" target="_blank" rel="nofollow noopener noreferrer"><code>transform</code></a></li>
</ul>
<p>自定义一个loader，去返回自定义的文件内容；如果返回null，那么返回的就是系统解析这个chunk的默认内容，load可返回的内容类型太多，包括sourceMap, ast等，具体的参见<a href="https://rollupjs.org/guide/en/#load" target="_blank" rel="nofollow noopener noreferrer"><code>load</code></a></p>
<h6 data-id="heading-13">transform</h6>
<ul>
<li>Type: <code>(code: string, id: string) => string | null | &#123;code?: string, map?: string | SourceMap, ast? : ESTree.Program, moduleSideEffects?: boolean | "no-treeshake" | null, syntheticNamedExports?: boolean | string | null, meta?: &#123;[plugin: string]: any&#125; | null&#125;</code></li>
<li>Previous Hook: <a href="https://rollupjs.org/guide/en/#load" target="_blank" rel="nofollow noopener noreferrer"><code>load</code></a></li>
<li>NextHook: <a href="https://rollupjs.org/guide/en/#moduleparsed" target="_blank" rel="nofollow noopener noreferrer"><code>moduleParsed</code></a> once the file has been processed and parsed.</li>
</ul>
<p>用来针对load之后的chunk做转换，避免额外的编译开销</p>
<h5 data-id="heading-14">以下钩子在服务器关闭时被调用</h5>
<ul>
<li><a href="https://rollupjs.org/guide/en/#buildend" target="_blank" rel="nofollow noopener noreferrer"><code>buildEnd</code></a></li>
<li><a href="https://rollupjs.org/guide/en/#closebundle" target="_blank" rel="nofollow noopener noreferrer"><code>closeBundle</code></a></li>
</ul>
<h6 data-id="heading-15">buildEnd</h6>
<ul>
<li>Type: <code>(error?: Error) => void</code></li>
<li>Previous Hook: <a href="https://rollupjs.org/guide/en/#moduleparsed" target="_blank" rel="nofollow noopener noreferrer"><code>moduleParsed</code></a>, <a href="https://rollupjs.org/guide/en/#resolveid" target="_blank" rel="nofollow noopener noreferrer"><code>resolveId</code></a> or <a href="https://rollupjs.org/guide/en/#resolvedynamicimport" target="_blank" rel="nofollow noopener noreferrer"><code>resolveDynamicImport</code></a>.</li>
<li>Next Hook: <a href="https://rollupjs.org/guide/en/#outputoptions" target="_blank" rel="nofollow noopener noreferrer"><code>outputOptions</code></a> in the output generation phase as this is the last hook of the build phase.</li>
</ul>
<p>在bunding finished的时候、写文件之前触发，也可以返回Promise；如果在build过程中报错，也会触发这个钩子</p>
<h4 data-id="heading-16">vite独有的钩子</h4>
<h6 data-id="heading-17">config</h6>
<ul>
<li>Type: <code>(config: UserConfig, env: &#123; mode: string, command: string &#125;) => UserConfig | null | void</code></li>
</ul>
<p>在解析 Vite 配置前调用。钩子接收原始用户配置（命令行选项指定的会与配置文件合并）和一个描述配置环境的变量，包含正在使用的 <code>mode</code> 和 <code>command</code>。它可以返回一个将被深度合并到现有配置中的部分配置对象，或者直接改变配置（如果默认的合并不能达到预期的结果）。在config钩子内调用任何其他的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 返回部分配置（推荐）</span>
<span class="hljs-keyword">const</span> partialConfigPlugin = <span class="hljs-function">() =></span> (&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'return-partial'</span>,
  <span class="hljs-attr">config</span>: <span class="hljs-function">() =></span> (&#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-attr">foo</span>: <span class="hljs-string">'bar'</span>
    &#125;
  &#125;)
&#125;)
<span class="hljs-comment">// 直接改变配置（应仅在合并不起作用时使用）</span>
<span class="hljs-keyword">const</span> mutateConfigPlugin = <span class="hljs-function">() =></span> (&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'mutate-config'</span>,
  <span class="hljs-function"><span class="hljs-title">config</span>(<span class="hljs-params">config, &#123; command &#125;</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (command === <span class="hljs-string">'build'</span>) &#123;
      config.root = __dirname
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-18">configResolved</h6>
<ul>
<li>Type: <code>(config: ResolvedConfig) => void | Promise<void></code></li>
</ul>
<p>在解析 Vite 配置后调用。使用这个钩子读取和存储最终解析的配置。当插件需要根据运行的命令做一些不同的事情时，它也很有用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> exmaplePlugin = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">let</span> config
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'read-config'</span>,
    <span class="hljs-function"><span class="hljs-title">configResolved</span>(<span class="hljs-params">resolvedConfig</span>)</span> &#123;
      <span class="hljs-comment">// 存储最终解析的配置</span>
      config = resolvedConfig
    &#125;,
    <span class="hljs-comment">// 使用其他钩子存储的配置</span>
    <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params">code, id</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (config.command === <span class="hljs-string">'serve'</span>) &#123;
        <span class="hljs-comment">// serve: 用于启动开发服务器的插件</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// build: 调用 Rollup 的插件</span>
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-19">configureServer</h6>
<ul>
<li>Type: <code>(server: ViteDevServer) => (() => void) | void | Promise<(() => void) | void></code></li>
<li>ViteDevServer接口：<a href="https://cn.vitejs.dev/guide/api-javascript.html#vitedevserver" target="_blank" rel="nofollow noopener noreferrer">ViteDevServer</a></li>
</ul>
<p>是用于配置开发服务器的钩子。最常见的用例是在内部 <a href="https://github.com/senchalabs/connect" target="_blank" rel="nofollow noopener noreferrer">connect</a> 应用程序中添加自定义中间件:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> myPlugin = <span class="hljs-function">() =></span> (&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'configure-server'</span>,
  <span class="hljs-function"><span class="hljs-title">configureServer</span>(<span class="hljs-params">server</span>)</span> &#123;
    server.middlewares.use(<span class="hljs-function">(<span class="hljs-params">req, res, next</span>) =></span> &#123;
      <span class="hljs-comment">// 自定义请求处理...</span>
    &#125;)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注入后置中间件</p>
<p><code>configureServer</code> 钩子将在内部中间件被安装前调用，所以自定义的中间件将会默认会比内部中间件早运行。如果你想注入一个在内部中间件 <strong>之后</strong> 运行的中间件，你可以从 <code>configureServer</code> 返回一个函数，将会在内部中间件安装后被调用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> myPlugin = <span class="hljs-function">() =></span> (&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'configure-server'</span>,
  <span class="hljs-function"><span class="hljs-title">configureServer</span>(<span class="hljs-params">server</span>)</span> &#123;
    <span class="hljs-comment">// 返回一个在内部中间件安装后</span>
    <span class="hljs-comment">// 被调用的后置钩子</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      server.middlewares.use(<span class="hljs-function">(<span class="hljs-params">req, res, next</span>) =></span> &#123;
        <span class="hljs-comment">// 自定义请求处理...</span>
      &#125;)
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意 <code>configureServer</code> 在运行生产版本时不会被调用，所以其他钩子需要注意防止它的缺失。</p>
<h6 data-id="heading-20">transformIndexHtml</h6>
<ul>
<li>Type:  <code>IndexHtmlTransformHook | &#123; enforce?: 'pre' | 'post' transform: IndexHtmlTransformHook &#125;</code></li>
</ul>
<p>转换 <code>index.html</code> 的专用钩子。钩子接收当前的 HTML 字符串和转换上下文。上下文在开发期间暴露<a href="https://cn.vitejs.dev/guide/api-javascript.html#ViteDevServer" target="_blank" rel="nofollow noopener noreferrer"><code>ViteDevServer</code></a>实例，在构建期间暴露 Rollup 输出的包。</p>
<p>这个钩子可以是异步的，并且可以返回以下其中之一:</p>
<ul>
<li>经过转换的 HTML 字符串</li>
<li>注入到现有 HTML 中的标签描述符对象数组（<code>&#123; tag, attrs, children &#125;</code>）。每个标签也可以指定它应该被注入到哪里（默认是在 <code><head></code> 之前）</li>
<li>一个包含 <code>&#123; html, tags &#125;</code> 的对象</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> htmlPlugin = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'html-transform'</span>,
    <span class="hljs-function"><span class="hljs-title">transformIndexHtml</span>(<span class="hljs-params">html</span>)</span> &#123;
      <span class="hljs-keyword">return</span> html.replace(
        <span class="hljs-regexp">/<title>(.*?)<\/title>/</span>,
        <span class="hljs-string">`<title>Title replaced!</title>`</span>
      )
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-21">handleHotUpdate</h6>
<ul>
<li>Type: <code>(ctx: HmrContext) => Array<ModuleNode> | void | Promise<Array<ModuleNode> | void></code></li>
</ul>
<pre><code class="copyable">interface HmrContext &#123;
  file: string
  timestamp: number
  modules: Array<ModuleNode>
  read: () => string | Promise<string>
  server: ViteDevServer
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>modules</code> 是受更改文件影响的模块数组。它是一个数组，因为单个文件可能映射到多个服务模块（例如 Vue 单文件组件）。</li>
<li><code>read</code> 这是一个异步读函数，它返回文件的内容。之所以这样做，是因为在某些系统上，文件更改的回调函数可能会在编辑器完成文件更新之前过快地触发，并 <code>fs.readFile</code> 直接会返回空内容。传入的 <code>read</code> 函数规范了这种行为。</li>
</ul>
<p>钩子可以选择:</p>
<ul>
<li>过滤和缩小受影响的模块列表，使 HMR 更准确。</li>
<li>返回一个空数组，并通过向客户端发送自定义事件来执行完整的自定义 HMR 处理:</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">handleHotUpdate</span>(<span class="hljs-params">&#123; server &#125;</span>)</span> &#123;
  server.ws.send(&#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'custom'</span>,
    <span class="hljs-attr">event</span>: <span class="hljs-string">'special-update'</span>,
    <span class="hljs-attr">data</span>: &#123;&#125;
  &#125;)
  <span class="hljs-keyword">return</span> []
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>客户端代码应该使用 <a href="https://cn.vitejs.dev/guide/api-hmr.html" target="_blank" rel="nofollow noopener noreferrer">HMR API</a> 注册相应的处理器（这应该被相同插件的 <code>transform</code> 钩子注入）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (<span class="hljs-keyword">import</span>.meta.hot) &#123;
  <span class="hljs-keyword">import</span>.meta.hot.on(<span class="hljs-string">'special-update'</span>, <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-comment">// 执行自定义更新</span>
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">钩子执行顺序总结</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myExample</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 返回的是插件对象</span>
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'hooks-order'</span>, 
        <span class="hljs-comment">// 初始化hooks，只走一次</span>
        <span class="hljs-function"><span class="hljs-title">options</span>(<span class="hljs-params">opts</span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'options'</span>);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">buildStart</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'buildStart'</span>);
        &#125;,
        <span class="hljs-comment">// vite特有钩子</span>
        <span class="hljs-function"><span class="hljs-title">config</span>(<span class="hljs-params">config</span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'config'</span>);
            <span class="hljs-keyword">return</span> &#123;&#125;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">configResolved</span>(<span class="hljs-params">resolvedCofnig</span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'configResolved'</span>);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">configureServer</span>(<span class="hljs-params">server</span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'configureServer'</span>);
            <span class="hljs-comment">// server.app.use((req, res, next) => &#123;</span>
            <span class="hljs-comment">//   // custom handle request...</span>
            <span class="hljs-comment">// &#125;)</span>
        &#125;,
        <span class="hljs-function"><span class="hljs-title">transformIndexHtml</span>(<span class="hljs-params">html</span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'transformIndexHtml'</span>);
            <span class="hljs-keyword">return</span> html
            <span class="hljs-comment">// return html.replace(</span>
            <span class="hljs-comment">//   /<title>(.*?)<\/title>/,</span>
            <span class="hljs-comment">//   `<title>Title replaced!</title>`</span>
            <span class="hljs-comment">// )</span>
        &#125;,
        <span class="hljs-comment">// 通用钩子</span>
        <span class="hljs-function"><span class="hljs-title">resolveId</span>(<span class="hljs-params">source</span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(resolveId)
            <span class="hljs-keyword">if</span> (source === <span class="hljs-string">'virtual-module'</span>) &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'resolvedId'</span>);
                <span class="hljs-keyword">return</span> source; 
            &#125;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>; 
        &#125;,
        <span class="hljs-function"><span class="hljs-title">load</span>(<span class="hljs-params">id</span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'load'</span>);
                
            <span class="hljs-keyword">if</span> (id === <span class="hljs-string">'virtual-module'</span>) &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-string">'export default "This is virtual!"'</span>;
            &#125;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params">code, id</span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'transform'</span>);
            <span class="hljs-keyword">if</span> (id === <span class="hljs-string">'virtual-module'</span>) &#123;
            &#125;
            <span class="hljs-keyword">return</span> code
        &#125;,
    &#125;;
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果</p>
<pre><code class="copyable">config
configResolved
options
configureServer
buildStart
transformIndexHtml
load
load
transform
transform
<span class="copy-code-btn">复制代码</span></code></pre>
<p>钩子执行顺序</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e229d9ff7880440bafcc5f188486defc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-23">插件执行顺序</h4>
<p>和webpack有点类似，也是通过enforce字段控制</p>
<ul>
<li>别名处理Alias</li>
<li>用户插件设置<code>enforce: 'pre'</code></li>
<li>Vite核心插件</li>
<li>用户插件未设置<code>enforce</code></li>
<li>Vite构建插件</li>
<li>用户插件设置<code>enforce: 'post'</code></li>
<li>Vite构建后置插件(minify, manifest, reporting)</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf65b1e604df4ff6903081128ee4e591~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于公司后续架构升级会用到vue3+vite，考虑到vite暂时可能还有些轮子不够健全，不排除后续工作需要自己写vite插件，所以在此稍做总结，不对的地方还望指正。</p>
<p>参考链接：</p>
<p><a href="https://juejin.cn/post/6950217775663513608" target="_blank">juejin.cn/post/695021…</a></p>
<p><a href="https://cn.vitejs.dev/guide/api-plugin.html" target="_blank" rel="nofollow noopener noreferrer">cn.vitejs.dev/guide/api-p…</a></p>
<p><a href="https://rollupjs.org/guide/en/#plugin-development" target="_blank" rel="nofollow noopener noreferrer">rollupjs.org/guide/en/#p…</a></p></div>  
</div>
            