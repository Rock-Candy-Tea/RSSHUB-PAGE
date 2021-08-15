
---
title: 'vite预构建源码梳理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc320098901141548e2ef47be32a755a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 01:48:11 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc320098901141548e2ef47be32a755a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>对于<code>“为什么要进行依赖预构建?"</code>这个问题<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvitejs.cn%2Fguide%2Fdep-pre-bundling.html%23%25E4%25BE%259D%25E8%25B5%2596%25E9%25A2%2584%25E6%259E%2584%25E5%25BB%25BA" target="_blank" rel="nofollow noopener noreferrer" title="https://vitejs.cn/guide/dep-pre-bundling.html#%E4%BE%9D%E8%B5%96%E9%A2%84%E6%9E%84%E5%BB%BA" ref="nofollow noopener noreferrer">vite文档</a>已经解释的很清楚了，那么预构建大概的流程是什么样的呢？</p>
<h2 data-id="heading-0">启动预构建</h2>
<p>从文档中我们知道在服务启动前会进行预构建，对应源码位置在<code>src/node/server/index.ts</code>,预构建的函数名是<code>optimizeDeps</code></p>
<pre><code class="copyable">...
const runOptimize = async () => &#123;
    if (config.cacheDir) &#123;
      server._isRunningOptimizer = true;
      try &#123;
        server._optimizeDepsMetadata = await optimizeDeps(config);
      &#125; finally &#123;
        server._isRunningOptimizer = false;
      &#125;
      server._registerMissingImport = createMissingImporterRegisterFn(server);
    &#125;
  &#125;;
  
...
await runOptimize();
...
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">开始预构建</h2>
<p>函数<code>optimizeDeps</code>定义在<code>src/node/optimizer/index.ts</code>，其主要流程可分为以下几步：</p>
<ol>
<li>判断是否需要预构建，如果之前预构建的内容还可以用，那么直接<code>return</code>，反之继续往下执行。需要说明的是判断预构建的内容是否可用的依据是<code>package.lock.json</code>和部分vite配置的内容，具体实现在<code>getDepHash</code>函数中。</li>
</ol>
<pre><code class="copyable">
  if (!force) &#123;
    let prevData;
    try &#123;
      prevData = JSON.parse(fs.readFileSync(dataPath, "utf-8"));
    &#125; catch (e) &#123;&#125;
    // hash is consistent, no need to re-bundle
    if (prevData && prevData.hash === data.hash) &#123;
      log("Hash is consistent. Skipping. Use --force to override.");
      return prevData;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用esbuild解析整个项目，获取本次需要进行<strong>预构建的依赖</strong>和<strong>解析出问题的依赖</strong>，分别赋值给<code>deps</code>和<code>missing</code>,其主要执行过程在函数<code>scanImports</code>中（这部分的代码实现过程梳理放在本部分最后）。</li>
</ol>
<pre><code class="copyable">  let deps: Record<string, string>, missing: Record<string, string>;
  if (!newDeps) &#123;
    (&#123; deps, missing &#125; = await scanImports(config));
  &#125; else &#123;
    deps = newDeps;
    missing = &#123;&#125;;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>正式预构建前的一系列的处理
<ol>
<li>如果<code>missing</code>有值，则报错,就是我们在控制台看到的<code>The following dependencies are imported but could not be resolved....  Are they installed</code></li>
<li>把配置项<code>config.optimizeDeps?.include</code>里的依赖加入到<code>deps</code>中,如果处理失败的话也会在控制台报错</li>
<li>如果<code>deps</code>为空的话，说明不需要预构建，更新预构建内容的hash值后直接<code>return</code></li>
<li>执行到这说明本次需要进行预构建，在控制台提示本次预构建的依赖,如下图所示</li>
</ol>
</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc320098901141548e2ef47be32a755a~tplv-k3u1fbpfcp-watermark.image" alt="screenshot-20210815-121549.png" loading="lazy" referrerpolicy="no-referrer">
4. 进一步处理<code>deps</code>得到<code>flatIdDeps</code>，主要是因为默认esbuild打包的话对于依赖的分析、映射的处理可能比较麻烦,这里主要做了两方面的工作</p>
<blockquote>
<ol>
<li>扁平化目录结构。举个例子，引入<code>lib-flexible/flexible</code>,而预构建的依赖为<code>lib-flexible_flexible.js</code></li>
</ol>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57e9f8e7c82044e6b8bc75023f2f85fe~tplv-k3u1fbpfcp-watermark.image" alt="carbon.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<ol start="2">
<li>在插件中，把入口文件当作虚拟文件(这一步应该是esbuild插件的需要，不是特别理解)</li>
</ol>
</blockquote>
<pre><code class="copyable">// esbuild generates nested directory output with lowest common ancestor base
 // this is unpredictable and makes it difficult to analyze entry / output
 // mapping. So what we do here is:
 // 1. flatten all ids to eliminate slash
 // 2. in the plugin, read the entry ourselves as virtual files to retain the
 //    path.
 const flatIdDeps: Record<string, string> = &#123;&#125;;
 const idToExports: Record<string, ExportsData> = &#123;&#125;;
 const flatIdToExports: Record<string, ExportsData> = &#123;&#125;;

 await init;
 for (const id in deps) &#123;
   const flatId = flattenId(id);
   flatIdDeps[flatId] = deps[id];
   const entryContent = fs.readFileSync(deps[id], "utf-8");
   const exportsData = parse(entryContent) as ExportsData;
   for (const &#123; ss, se &#125; of exportsData[0]) &#123;
     const exp = entryContent.slice(ss, se);
     if (/export\s+\*\s+from/.test(exp)) &#123;
       exportsData.hasReExports = true;
     &#125;
   &#125;
   idToExports[id] = exportsData;
   flatIdToExports[flatId] = exportsData;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>使用esbuild对<code>deps</code>每个依赖进行构建并默认输出到<code>node_modules/.vite</code>中</li>
</ol>
<pre><code class="copyable"> const result = await build(&#123;
   entryPoints: Object.keys(flatIdDeps),
   bundle: true,
   format: "esm",
   external: config.optimizeDeps?.exclude,
   logLevel: "error",
   splitting: true,
   sourcemap: true,
   outdir: cacheDir,
   treeShaking: "ignore-annotations",
   metafile: true,
   define,
   plugins: [
     ...plugins,
     esbuildDepPlugin(flatIdDeps, flatIdToExports, config),
   ],
   ...esbuildOptions,
 &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>把此次预构建的信息更新并写入文件<code>node_modules/.vite/_metadata.json</code>,完成预构建！</li>
</ol>
<pre><code class="copyable">for (const id in deps) &#123;
    const entry = deps[id];
    data.optimized[id] = &#123;
      file: normalizePath(path.resolve(cacheDir, flattenId(id) + ".js")),
      src: entry,
      needsInterop: needsInterop(
        id,
        idToExports[id],
        meta.outputs,
        cacheDirOutputPath
      ),
    &#125;;
  &#125;

  writeFile(dataPath, JSON.stringify(data, null, 2));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2"><code>scanImports</code></h3>
<p><code>”具体哪些依赖是需要预构建的？“</code>是函数<code>scanImports</code>处理的，在<code>src/node/optimizer/scan.ts</code>中，其过程比较简单，大概分为两步：</p>
<blockquote>
<ol>
<li>找到入口文件（一般是<code>index.html</code>）</li>
<li>使用esbuild进行一次打包，打包过程中就找到了<code>deps</code>和<code>missing</code>,最后返回<code>deps</code>和<code>missing</code></li>
</ol>
</blockquote>
<pre><code class="copyable">// step 1
 let entries: string[] = []
 ...
 entries = await globEntries('**/*.html', config)
 ...
 
// step 2
const plugin = esbuildScanPlugin(config, container, deps, missing, entries)

const &#123; plugins = [], ...esbuildOptions &#125; =
    config.optimizeDeps?.esbuildOptions ?? &#123;&#125;
  await Promise.all(
    entries.map((entry) =>
      build(&#123;
        write: false,
        entryPoints: [entry],
        bundle: true,
        format: 'esm',
        logLevel: 'error',
        plugins: [...plugins, plugin],
        ...esbuildOptions
      &#125;)
    )
  )
  
return &#123;
    deps,
    missing
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>由上可以看出，<code>deps</code>和<code>missing</code>是在esbuild插件<code>esbuildScanPlugin</code>中得到的，那么这个插件是怎么做的呢？</p>
<h3 data-id="heading-3"><code>esbuildScanPlugin</code></h3>
<p>还是在<code>src/node/optimizer/scan.ts</code>中，该插件主要做了以下两件事：</p>
<ol>
<li>处理导入模块（依赖），在<code>build.onResolve</code>中，具体：</li>
</ol>
<blockquote>
<ol>
<li>设置<code>external</code>属性(external代表该模块是否需要打包)</li>
<li>判断是否应该加入<code>deps</code>或者<code>missing</code>,代码如下：</li>
</ol>
</blockquote>
<pre><code class="copyable">...
export const OPTIMIZABLE_ENTRY_RE = /\.(?:m?js|ts)$/
...
const resolved = await resolve(id, importer)
if (resolved) &#123;
    if (shouldExternalizeDep(resolved, id)) &#123;
      return externalUnlessEntry(&#123; path: id &#125;)
    &#125;
    if (resolved.includes('node_modules') || include?.includes(id)) &#123;
      // dependency or forced included, externalize and stop crawling
      if (OPTIMIZABLE_ENTRY_RE.test(resolved)) &#123;
        depImports[id] = resolved
      &#125;
      return externalUnlessEntry(&#123; path: id &#125;)
    &#125; else &#123;
      // linked package, keep crawling
      return &#123;
        path: path.resolve(resolved)
      &#125;
    &#125;
&#125; else &#123;
    missing[id] = normalizePath(importer)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由上可知模块（依赖）是否放在<code>deps、missing</code>里、放的话放在哪一个都是由函数<code>resolve</code>决定的，从代码中可以看到<code>resolve</code>的执行逻辑如下:</p>
<blockquote>
<ol>
<li>执行rollup的hook <code>resolveId()</code>,</li>
<li>执行vite的插件pluginContainer <code>resolveId()</code></li>
<li>最后是这里的<code>resolve()</code></li>
</ol>
</blockquote>
<p>由于我对于这一段的处理逻辑不是很清楚，这里只能简单的理解为：</p>
<blockquote>
<ol>
<li><code>resolve</code>失败的话就会放到<code>missing</code></li>
<li><code>resolve</code>里包含<code>node_modules</code>(我理解为放在<code>node_modules</code>目录下)或者在vite的配置项<code>include</code>里且是<code>OPTIMIZABLE_ENTRY_RE</code>的会直接放进<code>deps</code>等待打包，不再进一步向下crawling。</li>
</ol>
</blockquote>
<p>这里就把预构建需要的<code>deps</code>和<code>missing</code>收集到了。</p>
<ol start="2">
<li>处理文件内容，在<code>build.onLoad</code>中，具体：</li>
</ol>
<blockquote>
<ol>
<li>针对<code>.html .vue svelte</code>这类有 js 逻辑的文件，需要把其中的js部分抽离出来，使用<code>import 、export</code>语法包裹并返回</li>
<li>针对不同的文件(js、ts、jsx...)，加载不同的 loader 解析</li>
</ol>
</blockquote>
<h2 data-id="heading-4">预构建的结果</h2>
<p>预构建的结果都放在了<code>node_modules/.vite/</code>中，一般如下图所示，包括两方面的信息：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef42742aec2a4761ab9407bb0981db79~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li><code>_metadata.json</code>,是本次预构建产生的一些“版本”和依赖包的信息，如下图所示：</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58853028be964607848d240ae6341915~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li><code>xx.js, xxx.js.map</code>各个依赖包的打包结果</li>
</ol>
<h2 data-id="heading-5">END</h2>
<p>预构建部分的代码实现大概就是这样，文章同步放在了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwkstudy%2Fdoc%2Ftree%2Fmaster%2Fvite" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wkstudy/doc/tree/master/vite" ref="nofollow noopener noreferrer">vite源码阅读</a>中，关于vite源码相关的学习都会记录在这里，欢迎大家讨论交流，感谢各位🙏</p></div>  
</div>
            