
---
title: 'rollup源码之plugin编写指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c33f6f9b5f3415cbad05acadf1c09ad~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 21 May 2021 01:21:00 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c33f6f9b5f3415cbad05acadf1c09ad~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>rollup作为一款轻量的打包编译工具，在我们日常的工具库开发中使用非常广泛，但是对于它的插件编写，从目前来看官网上对于插件的介绍几乎都是英文，学习起来也不是很友好, 例子也相对较少，所以整理一篇文章来学习也是不错的。除此之外，作为使用最广泛的webpack，它的插件编写也比较简单和清晰的，那它和rollup中的插件使用又有什么区别呢。下面将借助流程图 并搭配一些rollup源码来讲解。</p>
<h2 data-id="heading-1">插件执行</h2>
<p>我们知道<code>wepback</code>执行插件是借助了<code>tapable</code>用于同步串行、并行，异步串行并行等方式来执行插件，那rollup其实自己实现一套简易的类似<code>tapable</code>的功能。大家可以定位到源码中<code>src/utils/PluginDriver.ts</code>文件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PluginDriver</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">hookFirst</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">hookFirstSync</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">hookParallel</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">hookReduceArg0</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">hookReduceArg0Sync</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">hookReduceValue</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">hookReduceValueSync</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">hookSeqSync</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面分别介绍这些方法，都有什么作用，相信大家都通过方法名看出了具体作用了~</p>
<ul>
<li>
<p><strong>hookFirst</strong>: 异步串行，出现第一个返回值不为空的插件，就停止执行,类似<code>tapable</code>的<code>AsyncSeriesBailHook</code></p>
</li>
<li>
<p><strong>hookFirstSync</strong>: 同步串行，出现第一个返回值不为空的插件，就停止执行，类似<code>tapable</code>的<code>SyncBailHook</code></p>
</li>
<li>
<p><strong>hookParallel</strong>： 异步并行 Promise.all，类似<code>tapable</code>的<code>AsyncParallelHook</code></p>
</li>
<li>
<p><strong>hookReduceArg0</strong>: 异步串行，把上一个hook的返回值作为下一个hook的参数，如果返回为空就停止执行，并返回最后的值, 类似<code>tapable</code>的<code>AsyncSeriesWaterfallHook</code></p>
</li>
<li>
<p><strong>hookReduceArg0Sync</strong>：同步串行，把上一个hook的返回值作为下一个hook的参数，如果返回为空就停止执行，并返回最后的值, 类似<code>tapable</code>的<code>SyncWaterfallHook</code></p>
</li>
<li>
<p><strong>hookReduceValue</strong>: 异步串行，传入一个初始值value，上一个hook处理好value后的返回值作为下一个hook的参数</p>
</li>
<li>
<p><strong>hookReduceValueSync</strong>: 同步串行，传入一个初始值value，上一个hook处理好value后的返回值作为下一个hook的参数</p>
</li>
<li>
<p><strong>hookSeq</strong>: 异步串行，忽略返回值，类似<code>tapable</code>的<code>SyncHook</code></p>
</li>
<li>
<p><strong>hookSeqSync</strong>: 同步串行，忽略返回值类似<code>tapable</code>的<code>AsyncSeriesHook</code></p>
</li>
</ul>
<p>通过上面的介绍，大家听过大概知道了rollup的插件是如何执行的。</p>
<h2 data-id="heading-2">示例</h2>
<p>我们先从一段代码开始</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> rollup = <span class="hljs-built_in">require</span>(<span class="hljs-string">'rollup'</span>);
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> inputOptions = &#123;
  <span class="hljs-attr">input</span>: <span class="hljs-string">'./src/app.js'</span>
&#125;
<span class="hljs-keyword">const</span> outputOptions = &#123;
  <span class="hljs-attr">file</span>: <span class="hljs-string">'bundle.js'</span>,
  <span class="hljs-attr">format</span>: <span class="hljs-string">'cjs'</span>
&#125;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">build</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 第一步</span>
  <span class="hljs-keyword">const</span> bundle = <span class="hljs-keyword">await</span> rollup.rollup(inputOptions);
  
  <span class="hljs-comment">// 第二步</span>
  <span class="hljs-keyword">const</span> &#123; code, map &#125; = <span class="hljs-keyword">await</span> bundle.generate(outputOptions);
  
  <span class="hljs-comment">// 第三步</span>
  <span class="hljs-keyword">await</span> bundle.write(outputOptions);
&#125;

build();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">1. build阶段</h2>
<h3 data-id="heading-4">options Hook</h3>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
开始 --> 
获取inputOptions -->
获取插件数组 --> |异步串行|a(options Hook) -->
经过插件处理后的inputOptions -->
合并inputOptions和defaultInputOptions

style a fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
</code></pre>
<blockquote>
<p>注意：options hook会被异步串行执行</p>
</blockquote>
<p><strong>插件示例</strong></p>
<p>参数：inputOptions</p>
<p>上下文：</p>
<ul>
<li>meta: &#123; rollupVersion, watchMode &#125;</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'options hook'</span>,
    <span class="hljs-function"><span class="hljs-title">options</span>(<span class="hljs-params">inputOptions</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.meta.rollupVersion) <span class="hljs-comment">// 获取rollup版本信息</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.meta.watchMode)     <span class="hljs-comment">// 获取watchMode</span>
        inputOptions.input = <span class="hljs-string">'./src/index.js'</span>; <span class="hljs-comment">// 修改入口文件路径</span>
        <span class="hljs-keyword">return</span> inputOptions
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">buildStart Hook</h3>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TB
a(new Graph) --> b
subgraph Graph初始化
b(new PathTracker) --> c(new PluginDriver) --> d(new GlobalScope) --> e(new ModuleLoader)
end
e --> |hookParallel 异步并行|f(buildStart Hook) --> g(graph.build)

style f fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
</code></pre>
<p>可以看到在要执行<code>graph.build</code>之前，除了创建一些重要对象之外，还执行了<code>buildStart Hook</code></p>
<pre><code class="hljs language-js copyable" lang="js">graph.pluginDriver.hookParallel(<span class="hljs-string">'buildStart'</span>, [inputOptions])
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>插件示例</strong></p>
<p>参数：<code>inputOptions</code></p>
<blockquote>
<p>注意这里的inputOptions是经过合并处理过后的</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'buildStart'</span>,
  <span class="hljs-function"><span class="hljs-title">buildStart</span>(<span class="hljs-params">inputOptions</span>)</span> &#123;
    <span class="hljs-comment">// 可通过引用类型 直接修改</span>
    inputOptions.xx = xx
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">resolveId Hook</h3>
<p>下面进入解析入口文件路径阶段</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
a(graph.build) -->
normalizeEntryModules -->
|规范入口配置|loadEntryModule -->
|开始加载入口模块|resolveId -->
|hookFirst 异步串行可中断| b(resolveId Hook) -->
返回处理后的路径resolveIdResult

style b fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
</code></pre>
<p>经过rollup内部的路径处理和<code>resolveId Hook</code>的处理，我们拿到了完整的入口文件路径。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> pluginResult = <span class="hljs-keyword">await</span> pluginDriver.hookFirst(
    <span class="hljs-string">'resolveId'</span>,
    [source, importer, &#123; <span class="hljs-attr">custom</span>: customOptions &#125;],
    <span class="hljs-literal">null</span>,
    skip
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>插件示例</strong></p>
<p>参数：</p>
<ul>
<li>id 文件路径</li>
<li>importer 可指定当前解析目录</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 乞丐版的alias插件</span>
<span class="hljs-comment">// 第一种写法</span>
&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'resolveId'</span>,
  <span class="hljs-function"><span class="hljs-title">resolveId</span>(<span class="hljs-params">id</span>)</span> &#123;
    <span class="hljs-keyword">const</span> fullPath = id.replace(<span class="hljs-string">'@'</span>, path.resolve(__dirname, <span class="hljs-string">'src'</span>));
    <span class="hljs-keyword">return</span> id.includes(<span class="hljs-string">'.js'</span>) ? fullPath : fullPath + <span class="hljs-string">'.js'</span>
  &#125;
&#125;

<span class="hljs-comment">// 第二种</span>
&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'resolveId'</span>,
  <span class="hljs-function"><span class="hljs-title">resolveId</span>(<span class="hljs-params">id</span>)</span> &#123;
    <span class="hljs-keyword">const</span> fullPath = id.replace(<span class="hljs-string">'@'</span>, path.resolve(__dirname, <span class="hljs-string">'src'</span>));
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">id</span>: id.includes(<span class="hljs-string">'.js'</span>) ? fullPath : fullPath + <span class="hljs-string">'.js'</span>,
      <span class="hljs-attr">meta</span>: xxx, <span class="hljs-comment">// 模块meta信息</span>
      <span class="hljs-attr">moduleSideEffects</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 设置当前模块是否有副作用</span>
      <span class="hljs-attr">syntheticNamedExports</span>: xxx <span class="hljs-comment">// 默认为false,用法可参考 https://rollupjs.org/guide/en/#synthetic-named-exports</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>resolveId Hook</code>也是比较常用的hook，需要注意的是，如果有插件返回了值，那么后续所有插件的<code>resolveId</code>都不会被执行。</p>
<h3 data-id="heading-7">load Hook</h3>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
resolveIdResult --> a(addDefaultsToResolvedId统一结果为对象)

subgraph fetchModule
a --> b
b(new Module) --> |hookFirst 异步串行可中断|c
subgraph addModuleSource
c(load Hook)
end
c --> d(获取到经过load hook处理的代码source)
end


style c fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
</code></pre>
<p>拿到上一个<code>resolveId hook</code>处理的路径后，就要进入读取入口文件的步骤了，这一步rollup给了我们很大权力，我们可以任意修改文件内容。但是要注意，每个文件只会被一个插件的<code>load Hook</code>处理，因为它是以<code>hookFirst</code>来执行的。另外，如果你没有返回值，rollup会自动读取文件。</p>
<p><strong>插件示例</strong></p>
<p>参数：</p>
<ul>
<li>id 文件完整路径</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在所有文件前面添加注释</span>
<span class="hljs-comment">// 写法1</span>
&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'load'</span>,
  <span class="hljs-function"><span class="hljs-title">load</span>(<span class="hljs-params">id</span>)</span> &#123;
    <span class="hljs-comment">// 读取文件内容</span>
    <span class="hljs-keyword">const</span> content = fs.readFileSync(id);
    <span class="hljs-keyword">return</span> <span class="hljs-string">'/*这是一段注释*/'</span> + content.toString()
  &#125;
&#125;
<span class="hljs-comment">// 写法2</span>
&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'load'</span>,
  <span class="hljs-function"><span class="hljs-title">load</span>(<span class="hljs-params">id</span>)</span> &#123;
    <span class="hljs-comment">// 读取文件内容</span>
    <span class="hljs-keyword">const</span> content = fs.readFileSync(id);
    
    <span class="hljs-comment">// 也可以对代码进行转换 生成等操作</span>
    transform(content) 
    generate()
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">code</span>: <span class="hljs-string">'/*这是一段注释*/'</span> + content.toString()
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">transform Hook</h3>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
source --> |hookReduceArg0 异步串行|a(transform Hook) -->
b(ast,map,code)

style a fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
</code></pre>
<p>关于这个Hook想必大家都猜到了，可以对代码进行转换。关于这块的代码示例简单介绍就可以了~，大家自行发挥~。</p>
<p><strong>插件示例</strong></p>
<p>参数</p>
<ul>
<li>code</li>
<li>id</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 写法1</span>
&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'transform'</span>,
  <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params">code, id</span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        code,
        map,
        ast
    &#125;
  &#125;
&#125;
<span class="hljs-comment">//写法2</span>
&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'transform'</span>,
  <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params">code, id</span>)</span> &#123;
    <span class="hljs-keyword">return</span> code
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来就进入<code>AST</code>的创建阶段了</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
a(transform Hook) --> b&#123;是否返回ast&#125;
b --> |是|d(使用transofrm Hook返回的ast)
b --> |否|e(使用默认编译工具acorn)
d --> f(ast)
e --> f(ast)
f --> 创建ast上下文 -->
g(new ModuleScope) -->
h(new NamespaceVariable) -->
i(创建根ast节点new Program) -->
递归整个ast树并创建每个节点

</code></pre>
<p>上面的步骤其实递归了整个ast树，并为每个类型节点都创建了对应的<code>节点类</code>，对于它内部做了什么，本文不做讨论。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c33f6f9b5f3415cbad05acadf1c09ad~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">moduleParsed Hook</h3>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
addModuleSource --> |hookParallel 异步并行|a(moduleParsed Hook)

style a fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
</code></pre>
<p>在解析完模块后，我们能通过这个hook来获取模块的信息</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.pluginDriver.hookParallel(<span class="hljs-string">'moduleParsed'</span>, [<span class="hljs-built_in">module</span>.info]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>插件示例</strong></p>
<p>参数</p>
<ul>
<li>module.info 模块信息</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">id</span>: string, <span class="hljs-comment">// 模块路径</span>
  <span class="hljs-attr">code</span>: string | <span class="hljs-literal">null</span>, <span class="hljs-comment">// 模块代码</span>
  <span class="hljs-attr">ast</span>: ESTree.Program, <span class="hljs-comment">// 模块ast</span>
  <span class="hljs-attr">isEntry</span>: boolean, <span class="hljs-comment">// 是否是入口模块</span>
  <span class="hljs-attr">isExternal</span>: boolean, <span class="hljs-comment">// 是否是外部模块</span>
  <span class="hljs-attr">importedIds</span>: string[], <span class="hljs-comment">// 被此模块导入的所有模块id</span>
  <span class="hljs-attr">importers</span>: string[], <span class="hljs-comment">// 有哪些模块id 导入了该模块</span>
  <span class="hljs-attr">dynamicallyImportedIds</span>: string[], <span class="hljs-comment">// 通过import(xx)导入的所有模块id</span>
  <span class="hljs-attr">dynamicImporters</span>: string[], <span class="hljs-comment">// 有哪些模块通过import(xx)导入此模块</span>
  <span class="hljs-attr">implicitlyLoadedAfterOneOf</span>: string[], <span class="hljs-comment">// emitChunk会用到</span>
  <span class="hljs-attr">implicitlyLoadedBefore</span>: string[],  <span class="hljs-comment">// emitChunk会用到</span>
  <span class="hljs-attr">hasModuleSideEffects</span>: boolean | <span class="hljs-string">"no-treeshake"</span> <span class="hljs-comment">// 模块是否有副作用</span>
  <span class="hljs-attr">meta</span>: &#123;[plugin: string]: any&#125; <span class="hljs-comment">// 模块元信息</span>
  <span class="hljs-attr">syntheticNamedExports</span>: boolean | string <span class="hljs-comment">// https://rollupjs.org/guide/en/#synthetic-named-exports</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'moduleParsed'</span>,
  <span class="hljs-function"><span class="hljs-title">moduleParsed</span>(<span class="hljs-params">info</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(info);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取到模块信息之后，<code>rollup</code>将会根据模块的依赖树递归，重复以上的步骤，过程如下</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
a(moduleParsed Hook) --> b

subgraph fetch依赖模块
b(循环模块sources) --> c&#123;resolveIds是否解析过该source&#125;
c --> |否|d(resolveId)
c --> |是|g
d --> |hookFirst 异步串行可中断|f(resolveId Hook)
f --> g(resolveIdResult)
end
g --> 递归执行fetchModule
style a fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
style f fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
</code></pre>
<h2 data-id="heading-10">2.generate阶段</h2>
<blockquote>
<p>时间原因，流程图后续补充</p>
</blockquote>
<h3 data-id="heading-11">renderStart、banner、footer、intro、outro Hook</h3>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
bundle(new Bundle) -->
设置要输出的assets模块 --> |hookParallel|a(renderStart Hook)
a --> chunk
subgraph 生成Chunk对象
chunk(new Chunk) --> link(link dependencies)
end
link --> b(createAddons)
subgraph Promise.all
b --> |hookReduceValue|c(banner Hook)
b --> |hookReduceValue|d(footer Hook)
b --> |hookReduceValue|e(intro Hook)
b --> |hookReduceValue|f(outro Hook)
end

style a fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
</code></pre>
<p><strong>插件示例</strong></p>
<ul>
<li>
<p><strong>renderStart</strong></p>
<p>参数：inputOptions, outputOptions</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'renderStart'</span>,
    <span class="hljs-function"><span class="hljs-title">renderStart</span>(<span class="hljs-params">inputOptions, outputOptions</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(outputOptions);
      <span class="hljs-built_in">console</span>.log(inputOptions);
    &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>banner、footer、intro、outro Hook</strong></p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> outputOptions = &#123;
    <span class="hljs-attr">banner</span>: <span class="hljs-string">'banner'</span>,
    <span class="hljs-attr">footer</span>: <span class="hljs-string">'footer'</span>,
    <span class="hljs-attr">intro</span>: <span class="hljs-function">() =></span> <span class="hljs-string">'intro'</span>,
    <span class="hljs-attr">outro</span>: <span class="hljs-string">'outro'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在创建完chunk后，就会进入chunk的优化渲染阶段了，做的事情其实也比较简单，就是调用了所有ast节点的<code>render</code>方法，然后会把<code>included</code>为false的节点代码删除，也就是我们常说的<code>tree shaking</code>。</p>
<h3 data-id="heading-12">renderDynamicImport</h3>
<p><strong>插件示例</strong></p>
<p>参数：</p>
<pre><code class="copyable">&#123;
    customResolution: string | null
    format: string, // cjs/es等
    moduleId: string,  // import的模块路径
    targetModuleId: string | null // 被import的模块路径
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// plugin</span>
<span class="hljs-keyword">const</span> plugin = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'dynamic-import-polyfill'</span>,
  <span class="hljs-function"><span class="hljs-title">renderDynamicImport</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">left</span>: <span class="hljs-string">'dynamicImportPolyfill('</span>,
      <span class="hljs-attr">right</span>: <span class="hljs-string">', import.meta.url)'</span>
    &#125;
  &#125;
&#125;;

<span class="hljs-comment">// input</span>
<span class="hljs-keyword">import</span>(<span class="hljs-string">'./lib.js'</span>);

<span class="hljs-comment">// output</span>
dynamicImportPolyfill(<span class="hljs-string">'./lib.js'</span>, <span class="hljs-keyword">import</span>.meta.url);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">augmentChunkHash</h3>
<p><strong>插件示例</strong></p>
<p>参数：chunkInfo</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">code</span>: string,
  <span class="hljs-attr">dynamicImports</span>: string[],
  <span class="hljs-attr">exports</span>: string[],
  <span class="hljs-attr">facadeModuleId</span>: string | <span class="hljs-literal">null</span>,
  <span class="hljs-attr">fileName</span>: string,
  <span class="hljs-attr">implicitlyLoadedBefore</span>: string[],
  <span class="hljs-attr">imports</span>: string[],
  <span class="hljs-attr">importedBindings</span>: &#123;[imported: string]: string[]&#125;,
  <span class="hljs-attr">isDynamicEntry</span>: boolean,
  <span class="hljs-attr">isEntry</span>: boolean,
  <span class="hljs-attr">isImplicitEntry</span>: boolean,
  <span class="hljs-attr">map</span>: SourceMap | <span class="hljs-literal">null</span>,
  <span class="hljs-attr">modules</span>: &#123;  <span class="hljs-comment">// chunk所包含的模块</span>
    [id: string]: &#123;
      <span class="hljs-attr">renderedExports</span>: string[],
      <span class="hljs-attr">removedExports</span>: string[],
      <span class="hljs-attr">renderedLength</span>: number,
      <span class="hljs-attr">originalLength</span>: number,
      <span class="hljs-attr">code</span>: string | <span class="hljs-literal">null</span>
    &#125;,
  &#125;,
  <span class="hljs-attr">name</span>: string,
  <span class="hljs-attr">referencedFiles</span>: string[],
  <span class="hljs-attr">type</span>: <span class="hljs-string">'chunk'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'augmentChunkHash'</span>,
    <span class="hljs-function"><span class="hljs-title">augmentChunkHash</span>(<span class="hljs-params">chunkInfo</span>)</span> &#123;
      <span class="hljs-keyword">if</span>(chunkInfo.name === <span class="hljs-string">'foo'</span>) &#123;
        <span class="hljs-comment">// 生成唯一值以更新chunkName</span>
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Date</span>.now().toString();
      &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">resolveImportMeta</h3>
<p>参数：</p>
<ul>
<li>property <code>meta.xxx</code></li>
<li>模块和chunk id
<pre><code class="hljs language-js copyable" lang="js">&#123;
    chunkId,
    moduleId,
    format
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// a.js</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">import</span>.meta.testKey)

<span class="hljs-comment">// rollup.config.js</span>
&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'resolveImportMeta'</span>
    <span class="hljs-function"><span class="hljs-title">resolveImportMeta</span>(<span class="hljs-params">property, &#123;moduleId&#125;</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (property === <span class="hljs-string">'testKey'</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`new URL('<span class="hljs-subst">$&#123;path.relative(process.cwd(), moduleId)&#125;</span>', document.baseURI).href`</span>;
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">resolveFileUrl</h3>
<p><strong>插件示例</strong></p>
<p>参数：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    chunkId,
    fileName,
    format,
    moduleId,
    referenceId,
    relativePath
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'resolveFileUrl'</span>,
  <span class="hljs-function"><span class="hljs-title">resolveFileUrl</span>(<span class="hljs-params">&#123;fileName&#125;</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`new URL('<span class="hljs-subst">$&#123;fileName&#125;</span>', document.baseURI).href`</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">renderChunk</h3>
<p><strong>插件示例</strong></p>
<p>参数：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    code,  <span class="hljs-comment">// chunk代码</span>
    chunk,  <span class="hljs-comment">// chunk的一些信息</span>
    options  <span class="hljs-comment">// outputOptions</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 写法1</span>
&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'renderChunk'</span>,
  <span class="hljs-function"><span class="hljs-title">renderChunk</span>(<span class="hljs-params">&#123; code &#125;</span>)</span> &#123;
    <span class="hljs-comment">// change cdoe</span>
    <span class="hljs-keyword">return</span> &#123;
        code,
        map
    &#125;
  &#125;
&#125;

<span class="hljs-comment">// 写法2</span>
&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'renderChunk'</span>,
  <span class="hljs-function"><span class="hljs-title">renderChunk</span>(<span class="hljs-params">&#123; code &#125;</span>)</span> &#123;
    <span class="hljs-comment">// change cdoe</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">'/*注释*/'</span> + code
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">generateBundle</h3>
<p><strong>插件示例</strong></p>
<p>参数：</p>
<ul>
<li>outputOptions</li>
<li>ChunkInfo or AssetInfo
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// AssetInfo</span>
<span class="hljs-attr">moduleId</span>: &#123;
  <span class="hljs-attr">fileName</span>: string,
  name?: string,
  <span class="hljs-attr">source</span>: string | <span class="hljs-built_in">Uint8Array</span>,
  <span class="hljs-attr">type</span>: <span class="hljs-string">'asset'</span>,
&#125;

<span class="hljs-comment">// ChunkInfo</span>
<span class="hljs-attr">moduleId</span>: &#123;
  <span class="hljs-attr">code</span>: string,
  <span class="hljs-attr">dynamicImports</span>: string[],
  <span class="hljs-attr">exports</span>: string[],
  <span class="hljs-attr">facadeModuleId</span>: string | <span class="hljs-literal">null</span>,
  <span class="hljs-attr">fileName</span>: string,
  <span class="hljs-attr">implicitlyLoadedBefore</span>: string[],
  <span class="hljs-attr">imports</span>: string[],
  <span class="hljs-attr">importedBindings</span>: &#123;[imported: string]: string[]&#125;,
  <span class="hljs-attr">isDynamicEntry</span>: boolean,
  <span class="hljs-attr">isEntry</span>: boolean,
  <span class="hljs-attr">isImplicitEntry</span>: boolean,
  <span class="hljs-attr">map</span>: SourceMap | <span class="hljs-literal">null</span>,
  <span class="hljs-attr">modules</span>: &#123;
    [id: string]: &#123;
      <span class="hljs-attr">renderedExports</span>: string[],
      <span class="hljs-attr">removedExports</span>: string[],
      <span class="hljs-attr">renderedLength</span>: number,
      <span class="hljs-attr">originalLength</span>: number,
      <span class="hljs-attr">code</span>: string | <span class="hljs-literal">null</span>
    &#125;,
  &#125;,
  <span class="hljs-attr">name</span>: string,
  <span class="hljs-attr">referencedFiles</span>: string[],
  <span class="hljs-attr">type</span>: <span class="hljs-string">'chunk'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'generateBundle'</span>,
  <span class="hljs-function"><span class="hljs-title">generateBundle</span>(<span class="hljs-params">options, info</span>)</span> &#123;
    <span class="hljs-keyword">delete</span> info[<span class="hljs-string">'app.js'</span>]  <span class="hljs-comment">// 直接删除app.js chunk最后不会生成</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">writeBundle</h3>
<p>与<code>generateBundle</code>相似， 但是此时chunk已经生成，无法修改</p>
<h2 data-id="heading-19">插件上下文</h2>
<p>在rollup中每个插件都有自己的插件上下文，他具体又有什么用呢举个例子</p>
<pre><code class="hljs language-js copyable" lang="js">private runHookSync<H <span class="hljs-keyword">extends</span> SyncPluginHooks>(
        <span class="hljs-keyword">const</span> plugin = <span class="hljs-built_in">this</span>.plugins[pluginIndex];
        <span class="hljs-keyword">const</span> hook = plugin[hookName];
        <span class="hljs-keyword">if</span> (!hook) <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span> <span class="hljs-keyword">as</span> any;
        <span class="hljs-keyword">let</span> context = <span class="hljs-built_in">this</span>.pluginContexts[pluginIndex];
        <span class="hljs-keyword">if</span> (hookContext) &#123;
            context = hookContext(context, plugin);
        &#125;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> hook !== <span class="hljs-string">'function'</span>) &#123;
                <span class="hljs-keyword">return</span> throwInvalidHookError(hookName, plugin.name);
            &#125;
            <span class="hljs-comment">// 关键看这里通过apply将插件的this指向了context</span>
            <span class="hljs-keyword">return</span> (hook <span class="hljs-keyword">as</span> <span class="hljs-built_in">Function</span>).apply(context, args);
        &#125; <span class="hljs-keyword">catch</span> (err) &#123;
            <span class="hljs-keyword">return</span> throwPluginError(err, plugin.name, &#123; <span class="hljs-attr">hook</span>: hookName &#125;);
        &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至于<code>context</code>是什么，大家可以定位到<code>src/utils/PluginContext.ts</code>文件中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> context: PluginContext = &#123;
    <span class="hljs-function"><span class="hljs-title">addWatchFile</span>(<span class="hljs-params">id</span>)</span> &#123;&#125;,
    <span class="hljs-attr">cache</span>: cacheInstance,
    <span class="hljs-attr">emitAsset</span>: getDeprecatedContextHandler(...),
    <span class="hljs-attr">emitChunk</span>: getDeprecatedContextHandler(...),
    <span class="hljs-attr">emitFile</span>: fileEmitter.emitFile,
    error(err)
    <span class="hljs-attr">getAssetFileName</span>: getDeprecatedContextHandler(...),
    <span class="hljs-attr">getChunkFileName</span>: getDeprecatedContextHandler(),
    <span class="hljs-attr">getFileName</span>: fileEmitter.getFileName,
    <span class="hljs-attr">getModuleIds</span>: <span class="hljs-function">() =></span> graph.modulesById.keys(),
    <span class="hljs-attr">getModuleInfo</span>: graph.getModuleInfo,
    <span class="hljs-attr">getWatchFiles</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">Object</span>.keys(graph.watchFiles),
    <span class="hljs-attr">isExternal</span>: getDeprecatedContextHandler(...),
    <span class="hljs-attr">meta</span>: &#123;
        rollupVersion,
        <span class="hljs-attr">watchMode</span>: graph.watchMode
    &#125;,
    <span class="hljs-keyword">get</span> <span class="hljs-title">moduleIds</span>() &#123;
        <span class="hljs-keyword">const</span> moduleIds = graph.modulesById.keys();
        <span class="hljs-keyword">return</span> wrappedModuleIds();
    &#125;,
    <span class="hljs-attr">parse</span>: graph.contextParse,
    <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">source, importer, &#123; custom, skipSelf &#125; = BLANK</span>)</span> &#123;
        <span class="hljs-keyword">return</span> graph.moduleLoader.resolveId(source, importer, custom, skipSelf ? pidx : <span class="hljs-literal">null</span>);
    &#125;,
    <span class="hljs-attr">resolveId</span>: getDeprecatedContextHandler(...),
    <span class="hljs-attr">setAssetSource</span>: fileEmitter.setAssetSource,
    <span class="hljs-function"><span class="hljs-title">warn</span>(<span class="hljs-params">warning</span>)</span> &#123;&#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说我们可以在插件中直接通过<code>this.xxx</code>来调用上面的方法。他们都可以在各个hook中进行调用。下面进行介绍</p>
<h3 data-id="heading-20">addWatchFile</h3>
<p>用于动态添加对文件的监听，可以在<code>buildStart</code>、<code>load</code>、<code>resolveId</code>和<code>transform</code>中使用</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'addWatchFile'</span>,
  <span class="hljs-function"><span class="hljs-title">load</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 监听a.js文件的变化</span>
    <span class="hljs-built_in">this</span>.addWatchFile(<span class="hljs-string">'a.js'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">emitFile</h3>
<p><a href="https://rollupjs.org/guide/en/#thisemitfileemittedfile-emittedchunk--emittedasset--string" target="_blank" rel="nofollow noopener noreferrer">文档地址</a></p>
<p>发射一个文件到最后的打包中，并且会返回一个<code>referenceId</code>,支持两种对象传参</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'chunk'</span>,
  <span class="hljs-attr">id</span>: string,
  name?: string,
  fileName?: string,
  implicitlyLoadedAfterOneOf?: string[],
  importer?: string,
  preserveSignature?: <span class="hljs-string">'strict'</span> | <span class="hljs-string">'allow-extension'</span> | <span class="hljs-string">'exports-only'</span> | <span class="hljs-literal">false</span>,
&#125;

<span class="hljs-comment">// EmittedAsset</span>
&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'asset'</span>,
  name?: string,
  fileName?: string,
  source?: string | <span class="hljs-built_in">Uint8Array</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">error</h3>
<p>参数：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'error'</span>,
  <span class="hljs-function"><span class="hljs-title">load</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 抛出错误并显示 几行几列</span>
    <span class="hljs-built_in">this</span>.error(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'error message'</span>), &#123; <span class="hljs-attr">column</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">line</span>: <span class="hljs-number">1</span> &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">getCombinedSourcemap</h3>
<p>用于获取sourceMap，并且只能在<code>transform hook</code>中使用</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'getCombinedSourcemap'</span>,
  <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 获取sourceMap</span>
    <span class="hljs-built_in">this</span>.getCombinedSourcemap()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">getFileName</h3>
<p>获取通过<code>this.emitFile</code>文件发出的块或资源的文件名。文件名将相对于<code>outputOptions.dir</code>。</p>
<h3 data-id="heading-25">getModuleIds</h3>
<p>获取所有模块完整路径,需要注意的是，它返回的是个迭代器</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'getModuleIds'</span>,
  <span class="hljs-function"><span class="hljs-title">renderStart</span>(<span class="hljs-params">outputOptions</span>)</span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> id <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.getModuleIds()) &#123;
        <span class="hljs-comment">// get id</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">getModuleInfo</h3>
<p>获取模块info, 例如可以搭配<code>getModuleIds</code>使用</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'getModuleInfo'</span>,
  <span class="hljs-function"><span class="hljs-title">renderStart</span>(<span class="hljs-params">outputOptions</span>)</span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> id <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.getModuleIds()) &#123;
        <span class="hljs-keyword">const</span> moduleInfo = <span class="hljs-built_in">this</span>.getModuleInfo(id)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">getWatchFiles</h3>
<p>获取所有被监听变化的文件路径id, 包括通过<code>addWatchFile</code>添加的文件</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'getWatchFiles'</span>,
  <span class="hljs-function"><span class="hljs-title">renderStart</span>(<span class="hljs-params">outputOptions</span>)</span> &#123;
    <span class="hljs-keyword">const</span> watchIds = <span class="hljs-built_in">this</span>.getWatchFiles()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">parse</h3>
<p>用于编译代码，并返回ast</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'parse'</span>,
  <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params">code</span>)</span> &#123;
      <span class="hljs-keyword">const</span> ast = <span class="hljs-built_in">this</span>.parse(code)
      <span class="hljs-comment">// transform ast</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">resolve</h3>
<p>用于解析传入参数的完整路径,以及其他参数，它会经过所有的<code>resolveId hook</code>处理</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'parse'</span>,
  <span class="hljs-function"><span class="hljs-title">buildStart</span>(<span class="hljs-params">code</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.resolve(
        id, <span class="hljs-comment">// 要解析的文件路径</span>
        importer, <span class="hljs-comment">// 基于哪个目录解析</span>
        &#123;
            <span class="hljs-attr">skipSelf</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 是否跳过resolveId Hook</span>
            <span class="hljs-attr">custom</span>: &#123;&#125; <span class="hljs-comment">// 用户自定义参数，会传给每个resolveId Hook</span>
        &#125;
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">setAssetSource</h3>
<p>设置assets资源的代码，例如我们通过<code>this.emitFile</code>发射一个文件，返回了referanceId，可以通过这个id修改资源代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.setAssetSource(referenceId: string, <span class="hljs-attr">source</span>: string | <span class="hljs-built_in">Uint8Array</span>) => <span class="hljs-keyword">void</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            