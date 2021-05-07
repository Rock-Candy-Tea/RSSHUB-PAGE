
---
title: '你不知道的webpack静态文件生成过程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56704d8e45774ee2b4e007e2d175b204~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 06 May 2021 23:38:38 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56704d8e45774ee2b4e007e2d175b204~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>作者：崔静</p>
</blockquote>
<p>本文需要你对webpack有一定的了解，如果你比较感兴趣，可以参考我们之前的webpack源码解析系列：<a href="https://juejin.cn/post/6844903726981840904" target="_blank">webpack系列-总览</a>。</p>
<h4 data-id="heading-0">一些概念说明</h4>
<p>Compilation 初始化的时候会初始化下面几个变量：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.mainTemplate = <span class="hljs-keyword">new</span> MainTemplate(...)
<span class="hljs-built_in">this</span>.chunkTemplate = <span class="hljs-keyword">new</span> ChunkTemplate(...)
<span class="hljs-built_in">this</span>.runtimeTemplate = <span class="hljs-keyword">new</span> RuntimeTemplate
<span class="hljs-built_in">this</span>.moduleTemplates = &#123;
   <span class="hljs-attr">javascript</span>: <span class="hljs-keyword">new</span> ModuleTemplate(<span class="hljs-built_in">this</span>.runtimeTemplate, <span class="hljs-string">"javascript"</span>),
   <span class="hljs-attr">webassembly</span>: <span class="hljs-keyword">new</span> ModuleTemplate(<span class="hljs-built_in">this</span>.runtimeTemplate, <span class="hljs-string">"webassembly"</span>)
&#125;
<span class="hljs-built_in">this</span>.hotUpdateChunkTemplate <span class="hljs-comment">// 暂时不关注</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>mainTemplate:  用来生成执行主流程的代码，里面包含了 webpack 的启动代码等等。
chunkTemplate: 得到的最终代码则会通过 JsonP 的方式来加载。</p>
<p>下面的例子：
我们有一个入口文件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> &#123; Vue &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">new</span> Vue(...)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的文件打包后生成一个 app.js ，一个 chunk-vendor.js。</p>
<p>app.js 结构如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">modules</span>) </span>&#123; <span class="hljs-comment">// webpackBootstrap</span>
   <span class="hljs-comment">// webpack 的启动函数</span>
   <span class="hljs-comment">// webpack 内置的方法</span>
 &#125;)&#123;&#123;
   <span class="hljs-attr">moduleId</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, <span class="hljs-built_in">exports</span>, __webpack_require__</span>) </span>&#123;
      <span class="hljs-comment">// 我们写的 js 代码都在各个 module 中</span>
   &#125;,
   <span class="hljs-comment">// ...</span>
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>chunk-vendors.js 结构如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-built_in">window</span>[<span class="hljs-string">"webpackJsonp"</span>] = <span class="hljs-built_in">window</span>[<span class="hljs-string">"webpackJsonp"</span>] || []).push([[<span class="hljs-string">"chunk-vendors"</span>],&#123;
   <span class="hljs-attr">moduleId</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, <span class="hljs-built_in">exports</span>, __webpack_require__</span>) </span>&#123;
     <span class="hljs-comment">// ...</span>
   &#125;,
   <span class="hljs-comment">// ...</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>app.js 里面包含了 webpack 的 bootstrap 代码，这个代码整体的框架就在 mainTemplate。</p>
<p>app.js 会通过 jonsP 的方式加载 chunk-vendor.js ，这个 js 代码的框架就放在 chunkTemplate 中。</p>
<p>app.js 和 chunk-vendors.js 中各个 module 的代码生成过程就在 ModuleTempalte 中。</p>
<h4 data-id="heading-1">代码生成主流程</h4>
<p>chunk 代码生成在 seal 阶段。从 <code>Compilation.createChunkAssets</code> 中开始。</p>
<p>主流程图如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56704d8e45774ee2b4e007e2d175b204~tplv-k3u1fbpfcp-watermark.image" alt="create-asset.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>**说明1：**在 JavascriptModulePlugin中会确定 render 函数。这个 render 函数后续在 createChunkAssets 中会调用。</p>
</blockquote>
<blockquote>
<p>**说明2：**这里 moduleTemplate 在 Compilation 一开始初始化会生成</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.moduleTemplates = &#123;
<span class="hljs-attr">javascript</span>: <span class="hljs-keyword">new</span> ModuleTemplate(<span class="hljs-built_in">this</span>.runtimeTemplate, <span class="hljs-string">"javascript"</span>),
<span class="hljs-attr">webassembly</span>: <span class="hljs-keyword">new</span> ModuleTemplate(<span class="hljs-built_in">this</span>.runtimeTemplate, <span class="hljs-string">"webassembly"</span>)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于走到是 mainTemplate，在最开始获取 render 各种信息的函数中 <code>renderManifest</code> 为触发 <code>JavascriptModulesPlugin</code> 中注册的函数，而这个里面确定了 module 所使用的模板为 <code>moduleTemplates.javascript</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">compilation.mainTemplate.hooks.renderManifest.tap(
  <span class="hljs-string">"JavascriptModulesPlugin"</span>,
  <span class="hljs-function">(<span class="hljs-params">result, options</span>) =></span> &#123;
    <span class="hljs-comment">//...</span>
    result.push(&#123;
      <span class="hljs-attr">render</span>: <span class="hljs-function">() =></span>
      compilation.mainTemplate.render(
        hash,
        chunk,
        moduleTemplates.javascript,
        dependencyTemplates
      ),
      <span class="hljs-comment">//...</span>
    &#125;);
    <span class="hljs-keyword">return</span> result;
  &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>说明3：</strong> module-source 的过程见最后附加内容</p>
</blockquote>
<p>首先确定当前结构是使用 mainTemplate 还是走 chunkTemplate。这两个 Tempalte 中会有自己的 render 流程。我们以 mainTempalte 为例，看 render 的流程。</p>
<p>render 主流程中会生成主结构的代码，也就是前面我们 app.js demo 生成的代码框架部分。然后生成各个 moulde 的代码。这个流程由 ModuleTemplate 中的函数完成。</p>
<p>在 module 生成的时候，会调用 <code>hook.content, hook.module, hook.render, hook.package</code>这几个 hook。在每一个 hook 得到结果之后，传入到下一个 hook 中。<code>hook.module</code> 这个 hook 执行完后，会得到 module 的代码。然后在 <code>hook.render</code> 中，将这些代码包裹成一个函数。如果我们在 <code>webpack.config.js</code> 中配置了 <code>output.pathinfo=true</code> (<a href="https://webpack.js.org/configuration/output/#outputpathinfo" target="_blank" rel="nofollow noopener noreferrer">配置说明</a>)，那么在 <code>hook.package</code>这里就会给最终生成的代码添加一些路径和 tree-shaking 相关的注释，可以方便我们阅读代码。</p>
<p>得到所有的 module 代码之后，将它们包裹成数组或者对象。</p>
<h4 data-id="heading-2">修改代码</h4>
<ul>
<li>利用上面文件生成的 hook, 在某个 module 中添加额外内容</li>
</ul>
<p>BannerPlugin 是在 chunk 文件开头添加额外的内容。如果我们仅仅是希望在某个 module 中添加内容如何做呢？回顾一下上面代码生成的流程图，module 代码生成有几个关键的 hook 例如 <code>hook.content,hook.module,hook.render</code>。可以在这几个 hook 中注册函数来进行修改。一个简单的 demo 如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; ConcatSource &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-sources"</span>);
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AddExternalPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-comment">// plugin 初始化。这里处理一些参数格式化等</span>
    <span class="hljs-built_in">this</span>.content = options.content <span class="hljs-comment">// 获取要添加的内容</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    <span class="hljs-keyword">const</span> content = <span class="hljs-built_in">this</span>.content
    compiler.hooks.compilation.tap(<span class="hljs-string">'AddExternal'</span>, <span class="hljs-function"><span class="hljs-params">compilation</span> =></span> &#123;
      compilation.moduleTemplates.javascript.hooks.render.tap(<span class="hljs-string">'AddExternal'</span>, <span class="hljs-function">(<span class="hljs-params">
        moduleSource,
        <span class="hljs-built_in">module</span> </span>) =></span> &#123;
          <span class="hljs-comment">// 这里会传入 module 参数，我们可以配置，指定在某一 module 中执行下面的逻辑</span>
          <span class="hljs-comment">// ConcatSource 意味着最后处理的时候，我们 add 到里面的代码，会直接拼接。</span>
          <span class="hljs-keyword">const</span> source = <span class="hljs-keyword">new</span> ConcatSource()
          <span class="hljs-comment">// 在最开始插入我们要添加的内容</span>
          source.add(content)
          <span class="hljs-comment">// 插入源码</span>
          source.add(moduleSource)
          <span class="hljs-comment">// 返回新的源码</span>
          <span class="hljs-keyword">return</span> source
      &#125;)
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在 chunk 执行代码外再包裹一层额外的逻辑。</li>
</ul>
<p>我们曾经配置过 umd 的模式，或者 <code>output.library</code> 参数。配置了这俩内容之后，最后生成的代码结构就和最开始 app.js demo 中的结果不一样了。以 <code>output.library='someLibName'</code> 为例，会变成下面这样</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> someLibName =
(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">modules</span>)</span>&#123;
<span class="hljs-comment">// webpackBootstrap</span>
&#125;)([
<span class="hljs-comment">//... 各个module</span>
])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个的实现，就是在上面 <code>hooks.renderWithEntry</code> 环节对 mainTemplate 生成的代码进行了修改。</p>
<p>如果我们在某些情况下，想额外包裹一些自己的逻辑。可以就在这里处理。给一个简单的 demo</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; ConcatSource &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-sources"</span>);
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyWrapPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
  &#125;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    <span class="hljs-keyword">const</span> onRenderWithEntry = <span class="hljs-function">(<span class="hljs-params">source, chunk, hash</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> newSource = <span class="hljs-keyword">new</span> ConcatSource()
      newSource.add(<span class="hljs-string">`var myLib =`</span>)
      newSource.add(source)
      newSource.add(<span class="hljs-string">`\nconsole.log(myLib)`</span>)
      <span class="hljs-keyword">return</span> newSource
    &#125;
    compiler.hooks.compilation.tap(<span class="hljs-string">'MyWrapPlugin'</span>, <span class="hljs-function"><span class="hljs-params">compilation</span> =></span> &#123;
      <span class="hljs-keyword">const</span> &#123; mainTemplate &#125; = compilation
      mainTemplate.hooks.renderWithEntry.tap(
        <span class="hljs-string">"MyWrapPlugin"</span>,
        onRenderWithEntry
      )
      <span class="hljs-comment">// 如果我们支持一些变量的配置化，那么就需要把我们配置的信息写入 hash 中。否则，当我们修改配置的时候，会发现 hash 值不会变化。</span>
      <span class="hljs-comment">// mainTemplate.hooks.hash.tap("SetVarMainTemplatePlugin", hash => &#123;</span>
      <span class="hljs-comment">// hash.update()</span>
      <span class="hljs-comment">// &#125;);</span>
    &#125;)
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = MyWrapPlugin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack编译后结果</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> myLib =<span class="hljs-comment">/******/</span> (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">modules</span>) </span>&#123;
<span class="hljs-comment">//... webpack bootstrap 代码</span>
<span class="hljs-comment">/******/</span>  <span class="hljs-keyword">return</span> __webpack_require__(__webpack_require__.s = <span class="hljs-number">0</span>);
<span class="hljs-comment">/******/</span> &#125;)
<span class="hljs-comment">/************************************************************************/</span>
<span class="hljs-comment">/******/</span> ([
<span class="hljs-comment">/* 0 */</span>
<span class="hljs-comment">/***/</span> (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, <span class="hljs-built_in">exports</span></span>) </span>&#123;
<span class="hljs-comment">// ...</span>
<span class="hljs-comment">/***/</span> &#125;)
<span class="hljs-comment">/******/</span> ])
<span class="hljs-built_in">console</span>.log(myLib);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>BannerPlugin</li>
</ul>
<p>类似内置的 BannerPlugin。在上面 chunk 文件生成之后，也就是<code>createChunkAssets</code>执行完成之后，对整体的 chunk 文件内容进行修改。例如 bannerPlugin 是在 <code>optimizaChunkAssets</code> hook 中</p>
<p>在这个 hook 里面可以拿到一个参数 <code>chunks</code> 所有的 chunk，然后在这里可以添加额外的内容。</p>
<h4 data-id="heading-3">chunkAssets 后文件内容修改</h4>
<p>createChunkAssets 执行过后，其他的 hook 中可可以拿到文件内容，进行修改。</p>
<ul>
<li>
<p>sourcemap 的影响，afterOptimizeChunkAssets 这个 hook 之后，webpack 生成了 sourcemap。如果在这个之后进行代码的修改，例如 optimizeAssets 或者更后面的 emit hook 中，会发现 sourcemap 不对了。像下面的例子</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">compiler.hooks.compilation.tap(<span class="hljs-string">'AddExternal'</span>, <span class="hljs-function"><span class="hljs-params">compilation</span> =></span> &#123;
  compilation.hooks.optimizeAssets.tap(<span class="hljs-string">'AddExternal'</span>, <span class="hljs-function"><span class="hljs-params">assets</span> =></span> &#123;
    <span class="hljs-keyword">let</span> main = assets[<span class="hljs-string">"main.js"</span>]
    main = main.children.unshift(<span class="hljs-string">'//test\n//test\n'</span>)
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>对 hash 的影响。当上面 chunk 代码生成结束后，其实 hash 也就随着生成了。在hash生成完之后的 hook 中对代码的修改，比如增加点啥，不会影响到 hash 的结果。例如上面修改 chunk 代码的例子。假如我们的 plugin 进行了升级，修改的内容变了，但是生成的 hash 并不会随着改变。所以需要在 hash 生成相关的 hook 中，把 plugin 的内容写入 hash 中。</p>
</li>
</ul>
<h3 data-id="heading-4">module-source 生成</h3>
<p>module-source 的过程中会对 parser 阶段生成的各个 dependency 进行处理，根据 dependency.Template 实现对我们缩写的源码的转换。这里我们结合最开始 parser 来一起看 module-source。以下面 demo 为例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> &#123; test &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./b.js'</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">some</span>(<span class="hljs-params"></span>) </span>&#123;
  test()
&#125;
some()

<span class="hljs-comment">// b.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b2'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.js parser 中转成的 AST:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dcdf51e70384cdfa8426cc1b4155902~tplv-k3u1fbpfcp-watermark.image" alt="ast.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对 ast 进行 parser ，这个过程中，会经历</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.hooks.program.call(ast, comments) === <span class="hljs-literal">undefined</span>) &#123;
  <span class="hljs-built_in">this</span>.detectMode(ast.body);
  <span class="hljs-built_in">this</span>.prewalkStatements(ast.body);
  <span class="hljs-built_in">this</span>.blockPrewalkStatements(ast.body);
  <span class="hljs-built_in">this</span>.walkStatements(ast.body);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>program</p>
<p>检测有没有用到 import/export ，会增加 HarmonyCompatibilityDependency, HarmonyInitDependency(作用后面介绍)</p>
</li>
<li>
<p>detectMode</p>
<p>检测最开始是否有 <code>use strict</code> 和 <code>use asm</code>，为了保证我们代码编译之后开头写的 use strict 仍然在最开始</p>
</li>
<li>
<p>prewalkStatements</p>
<p>遍历当前作用域下所有的变量定义。这个过程中<code>import &#123; test &#125; from './b.js'</code> 中 test 也是在当前作用域下的，所以 import 在这里会被处理(过程见 javascript-parser)。针对这句 import 会额外被添加<code>ConstDependency</code>和<code>HarmonyImportSideEffectDependency</code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44163c7221814602b570eb7de2753b68~tplv-k3u1fbpfcp-watermark.image" alt="ast-prewalk.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>blockPrewalk</p>
<p>处理当前作用域下 let/const（在 prewalk 的时候只会处理var），class 名，export 和 export default</p>
</li>
<li>
<p>walkStatements</p>
<p>开始深入每一个节点进行处理。这里会找到代码中所有使用 <code>test</code> 的地方，然后添加 <code>HarmonyImportSpecifierDependency</code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5d67852e92140f291857d3a26c0ef18~tplv-k3u1fbpfcp-watermark.image" alt="ast-walk.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>经理过这些之后，对于上面的 demo 就会加入</p>
<blockquote>
<p>HarmonyCompatibilityDependency</p>
<p>HarmonyInitDependency</p>
<p>ConstDependency</p>
<p>HarmonyImportSideEffectDependency</p>
<p>HarmonyImportSpecifierDependency</p>
</blockquote>
<p>这些 dependency 分成两大类：</p>
<ul>
<li>
<p>moduleDependency: 有对应的 denpendencyFactory，在 processModuleDependencies 过程中会对这个 dependency 进行处理，得到对应的 module</p>
<p><code>HarmonyImportSideEffectDependency  --> NormalModuleFactory</code></p>
<p><code>HarmonyImportSpecifierDependency  --> NormalModuleFactory</code></p>
<p>两个指向的是同一个 module(./b.js)，所以会被去重。然后 webpack 沿着 dependency ，处理 b.js... 直到将所有的 moduleDependency 处理完</p>
</li>
<li>
<p>仅文件生成的时候，用来生成代码</p>
</li>
</ul>
<h4 data-id="heading-5">module.source</h4>
<p>首先拿到源码代码，然后处理各个 dependency</p>
<ul>
<li>
<p>HarmonyCompatibilityDependency</p>
<p>在开始插入 <code>__webpack_require__.r(__webpack_exports__);</code>，标识这是一个 esModule</p>
</li>
<li>
<p>HarmonyInitDependency</p>
<p>遍历所有的 dependency, 负责生成 <code>import &#123;test&#125; from './b.js'</code> 对应的引入 './b.js' 模块的代码</p>
<p><code>/* harmony import */ var _b_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(0);</code></p>
</li>
<li>
<p>ConstDependency</p>
<p>在 HarmonyInitDependency 阶段中，已经插入了 <code>import</code> 语句对应的内容，所以源码中的 <code>import &#123;test&#125; from './b.js'</code>需要删除掉。ConstDependency 的作用就是把这句替换成空，即删除</p>
</li>
<li>
<p>HarmonyImportSideEffectDependency</p>
</li>
</ul>
<p>作用阶段在 HarmonyInitDependency 过程中</p>
<ul>
<li>
<p>HarmonyImportSpecifierDependency</p>
<p>代码中 <code>test()</code> 所生成的依赖。作用就是替换代码中的 <code>test</code></p>
<ul>
<li>
<p>获取到 './b.js' 模块对应的变量名 <code>_b_js__WEBPACK_IMPORTED_MODULE_0__</code></p>
</li>
<li>
<p>获取 test 对应到 b.js 中的属性名(因为经过 webpack 编译，为了简化代码，我们在 b.js 中的 export test，可能会被转为 export a = test)</p>
<p><code>Object(_b_js__WEBPACK_IMPORTED_MODULE_0__[/* test */ "a"])</code></p>
<blockquote>
<p>如果是被调用的话，会走一个逻辑??</p>
<pre><code class="copyable">if (isCall) &#123;
if (callContext === false && asiSafe) &#123;
return `(0,$&#123;access&#125;)`;
&#125; else if (callContext === false) &#123;
return `Object($&#123;access&#125;)`;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
</li>
<li>
<p>然后替换代码中 test</p>
</li>
</ul>
</li>
</ul>
<p>经过所有的 dependency 之后：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2a0b3bbcf344ff1a0ef05668b3496da~tplv-k3u1fbpfcp-watermark.image" alt="before-after-code.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>了解了这个过程之后，如果我们需要对源代码中进行一些简单的修改，可以利用 parser 阶段的各个 hook 来实现。在这里修改有一个好处，不用担心搞坏 sourcemap 和 影响 hash 的生成。</p>
<ul>
<li>parser 中插入代码的 demo</li>
</ul>
<p>例如，我们使用某个插件的时候，需要下面的写法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> MainFunction <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.js'</span>
<span class="hljs-keyword">import</span> &#123; test &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./b.js'</span>
MainFunction.use(test)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际中利用 webpack 插件，在检测到有 test 引入时候，自动插入</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> MainFunction <span class="hljs-keyword">from</span> <span class="hljs-string">'./a.js'</span>
MainFunction.use(test)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现的关键，就是上面提到的 <code>HarmonyImportSideEffectDependency</code>,  <code>HarmonyImportSpecifierDependency</code> 和 <code>ConstDependency</code></p>
<p>代码如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> ConstDependency = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack/lib/dependencies/ConstDependency"</span>);
<span class="hljs-keyword">const</span> HarmonyImportSideEffectDependency = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack/lib/dependencies/HarmonyImportSideEffectDependency"</span>)
<span class="hljs-keyword">const</span> HarmonyImportSpecifierDependency = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack/lib/dependencies/HarmonyImportSpecifierDependency"</span>)
<span class="hljs-keyword">const</span> NullFactory = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack/lib/NullFactory"</span>);

<span class="hljs-comment">// 要引入的 a.js 的路径。这个路径后面会经过 webpack 的 resolve</span>
<span class="hljs-keyword">const</span> externalJSPath = <span class="hljs-string">`<span class="hljs-subst">$&#123;path.join(__dirname, <span class="hljs-string">'./a.js'</span>)&#125;</span>`</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ProvidePlugin</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
&#125;
<span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
compiler.hooks.compilation.tap(
<span class="hljs-string">"InjectPlugin"</span>,
<span class="hljs-function">(<span class="hljs-params">compilation, &#123; normalModuleFactory &#125;</span>) =></span> &#123;
<span class="hljs-keyword">const</span> handler = <span class="hljs-function">(<span class="hljs-params">parser, parserOptions</span>) =></span> &#123;
          <span class="hljs-comment">// 在 parser 处理 import 语句的时候</span>
          parser.hooks.import.tap(<span class="hljs-string">'InjectPlugin'</span>, <span class="hljs-function">(<span class="hljs-params">statement, source</span>) =></span> &#123;
            parser.state.lastHarmonyImportOrder = (parser.state.lastHarmonyImportOrder || <span class="hljs-number">0</span>) + <span class="hljs-number">1</span>;
            <span class="hljs-comment">// 新建一个 './a.js' 的依赖</span>
            <span class="hljs-keyword">const</span> sideEffectDep = <span class="hljs-keyword">new</span> HarmonyImportSideEffectDependency(
              externalJSPath,
              parser.state.module,
              parser.state.lastHarmonyImportOrder,
              parser.state.harmonyParserScope
            );
            <span class="hljs-comment">// 为 dependency 设置一个位置。这里设置为和 import &#123; test &#125; from './b.js' 相同的位置，在代码进行插入的时候会插入到改句所在的地方。</span>
            sideEffectDep.loc = &#123;
              <span class="hljs-attr">start</span>: statement.start,
              <span class="hljs-attr">end</span>: statement.end
            &#125;
            <span class="hljs-comment">// 设置一下 renames，标识代码中 mainFunction 是从外部引入的</span>
            parser.scope.renames.set(<span class="hljs-string">'mainFunction'</span>, <span class="hljs-string">"imported var"</span>);
            <span class="hljs-comment">// 把这个依赖加入到 module 的依赖中</span>
            parser.state.module.addDependency(sideEffectDep);
            
            <span class="hljs-comment">// -------------处理插入 mainFunction.use(test)------------</span>
            <span class="hljs-keyword">if</span> (!parser.state.harmonySpecifier) &#123;
              parser.state.harmonySpecifier = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
            &#125;
            parser.state.harmonySpecifier.set(<span class="hljs-string">'mainFunction'</span>, &#123;
              <span class="hljs-attr">source</span>: externalJSPath,
              <span class="hljs-attr">id</span>: <span class="hljs-string">'default'</span>,
              <span class="hljs-attr">sourceOrder</span>: parser.state.lastHarmonyImportOrder
            &#125;)
            <span class="hljs-comment">// 针对 mainFunction.use 中的 mainFunction</span>
            <span class="hljs-keyword">const</span> mainFunction = <span class="hljs-keyword">new</span> HarmonyImportSpecifierDependency(
              externalJSPath,
              parser.state.module,
              -<span class="hljs-number">1</span>,
              parser.state.harmonyParserScope,
              <span class="hljs-string">'default'</span>,
              <span class="hljs-string">'mainFunction'</span>,
              [-<span class="hljs-number">1</span>, -<span class="hljs-number">1</span>], <span class="hljs-comment">// 插入到代码最开始</span>
              <span class="hljs-literal">false</span>
            )
            parser.state.module.addDependency(mainFunction)
            
            <span class="hljs-comment">// 插入代码片段 .use(</span>
            <span class="hljs-keyword">const</span> constDep1 = <span class="hljs-keyword">new</span> ConstDependency(
              <span class="hljs-string">'.use('</span>,
              -<span class="hljs-number">1</span>,
              <span class="hljs-literal">true</span>
            )
            parser.state.module.addDependency(constDep1)
            
            <span class="hljs-comment">// 插入代码片段 test</span>
            <span class="hljs-keyword">const</span> useArgument = <span class="hljs-keyword">new</span> HarmonyImportSpecifierDependency(
              source,
              parser.state.module,
              -<span class="hljs-number">1</span>,
              parser.state.harmonyParserScope,
              <span class="hljs-string">'test'</span>,
              <span class="hljs-string">'test'</span>,
              [-<span class="hljs-number">1</span>, -<span class="hljs-number">1</span>],
              <span class="hljs-literal">false</span>
            )
            parser.state.module.addDependency(useArgument)
            
            <span class="hljs-comment">// 插入代码片段 )</span>
            <span class="hljs-keyword">const</span> constDep2 = <span class="hljs-keyword">new</span> ConstDependency(
              <span class="hljs-string">')\n'</span>,
              -<span class="hljs-number">1</span>,
              <span class="hljs-literal">true</span>
            )
            parser.state.module.addDependency(constDep2)
          &#125;);
        &#125;
normalModuleFactory.hooks.parser
.for(<span class="hljs-string">"javascript/auto"</span>)
.tap(<span class="hljs-string">"ProvidePlugin"</span>, handler);
normalModuleFactory.hooks.parser
.for(<span class="hljs-string">"javascript/dynamic"</span>)
.tap(<span class="hljs-string">"ProvidePlugin"</span>, handler);
&#125;
);
&#125;
&#125;
<span class="hljs-built_in">module</span>.exports = ProvidePlugin;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成的代码如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* 1 */</span>
<span class="hljs-comment">/***/</span> (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;
<span class="hljs-meta">
"use strict"</span>;
<span class="hljs-keyword">const</span> mainFunction = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'mainFunction'</span>)
&#125;

mainFunction.use = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'load something'</span>)
&#125;
<span class="hljs-comment">/* harmony default export */</span> __webpack_exports__[<span class="hljs-string">"a"</span>] = (mainFunction);

<span class="hljs-comment">/***/</span> &#125;),
<span class="hljs-comment">/* 2 */</span>
<span class="hljs-comment">/***/</span> (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;
<span class="hljs-meta">
"use strict"</span>;
__webpack_require__.r(__webpack_exports__);
<span class="hljs-comment">/* harmony import */</span> <span class="hljs-keyword">var</span> _Users_didi_Documents_learn_webpack_4_demo_banner_demo_a_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(<span class="hljs-number">1</span>);
<span class="hljs-comment">/* harmony import */</span> <span class="hljs-keyword">var</span> _b_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(<span class="hljs-number">0</span>);
_Users_didi_Documents_learn_webpack_4_demo_banner_demo_a_js__WEBPACK_IMPORTED_MODULE_0__[<span class="hljs-comment">/* default */</span> <span class="hljs-string">"a"</span>].use(_b_js__WEBPACK_IMPORTED_MODULE_1__[<span class="hljs-comment">/* test */</span> <span class="hljs-string">"a"</span>])

<span class="hljs-built_in">Object</span>(_b_js__WEBPACK_IMPORTED_MODULE_1__[<span class="hljs-comment">/* test */</span> <span class="hljs-string">"a"</span>])()

<span class="hljs-comment">/***/</span> &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>DefinePlugin</p>
<p><a href="https://webpack.js.org/plugins/define-plugin/#usage" target="_blank" rel="nofollow noopener noreferrer">DefinePlugin 介绍</a></p>
<p>可以使用这个插件在编译阶段对一些常量进行替换的时候，例如:</p>
<ul>
<li>常用到的 js 代码中根据<code>process.env.NODE_ENV</code>的值，区分不同 dev 环境 和 production 环境。从而实现在不同环境下走不同的分支逻辑。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> DefinePlugin(&#123;
  <span class="hljs-string">'process.env.NODE_ENV'</span>: <span class="hljs-built_in">JSON</span>.stringify(process.env.NODE_ENV)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>可以配置 api URL</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> DefinePlugin(&#123;
  <span class="hljs-attr">API_DOMAIN</span>: process.env.NODE_ENV === <span class="hljs-string">'dev'</span> ? <span class="hljs-string">'"//10.96.95.200"'</span> : <span class="hljs-string">'"//api.didi.cn"'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现 dev 和 production 下 api 请求域名的切换。</p>
</li>
</ul>
<p>简单介绍一些原理：一个最简单的例子</p>
<pre><code class="copyable">new DefinePlugin(&#123;
  'TEST': "'test'"
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中使用 <code>const a = TEST</code>, 在 parser 的时候遍历到 = 号右边的时候，会触发表达式解析的钩子</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// key 是 TEST</span>
parser.hooks.expression.for(key).tap(<span class="hljs-string">"DefinePlugin"</span>, <span class="hljs-function"><span class="hljs-params">expr</span> =></span> &#123;
  <span class="hljs-keyword">const</span> strCode = toCode(code, parser); <span class="hljs-comment">// 结果为我们设置的 'test'</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/__webpack_require__/</span>.test(strCode)) &#123;
    <span class="hljs-comment">// 如果用到了 __webpack_require__ ，生成的 ConstantDependency 中 requireWebpackRequire=true</span>
    <span class="hljs-comment">// 在后期生成代码，用 function(module, exports)&#123;&#125; 将代码包裹起来的时候，参数里面会有 __webpack_require__，即 function(module, exports, __webpack_require__)&#123;&#125; </span>
    <span class="hljs-keyword">return</span> ParserHelpers.toConstantDependencyWithWebpackRequire(
      parser,
      strCode
    )(expr);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// ParserHelpers.toConstantDependency 会生成一个 ConstDependency，并且添加到当前的 module 中</span>
    <span class="hljs-comment">// ConstDependency.expression = "'test'"，位置就是我们代码中 TEST 对应的位置</span>
    <span class="hljs-keyword">return</span> ParserHelpers.toConstantDependency(
      parser,
      strCode
    )(expr);
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前面说过，ConstDependency 会对源码对应内容进行替换。所以在后面代码生成阶段执行下面的操作</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ConstDependency.Template = <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ConstDependencyTemplate</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">dep, source</span>)</span> &#123;
    <span class="hljs-comment">// 如果 range 是一个数字，则为插入；如果是一个区间，则为替换</span>
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> dep.range === <span class="hljs-string">"number"</span>) &#123;
source.insert(dep.range, dep.expression);
<span class="hljs-keyword">return</span>;
&#125;
<span class="hljs-comment">// 把源码中对应的地方替换成了 dep.expression，即 "test" </span>
source.replace(dep.range[<span class="hljs-number">0</span>], dep.range[<span class="hljs-number">1</span>] - <span class="hljs-number">1</span>, dep.expression);
&#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样便实现了，对源码中 TEST 的替换。</p>
</li>
</ul>
<h3 data-id="heading-6">总结</h3>
<p>相信通过上边详细的过程分析以及对应的一些demo的实践，对于webpack是如何生成静态文件的整个过程都已经了解了。希望在未来里，你遇到类似的场景，且现有的生态插件不能满足需求的时候，是可以自己动手搞定。</p>
<p>我们想要深入了解一个细节的最大动力就是来自于我们的需求，在我们开源的小程序框架<a href="https://github.com/didi/mpx" target="_blank" rel="nofollow noopener noreferrer">mpx</a>中就有很多很多上述静态文件生成的大量应用。如果你感兴趣，欢迎大家去了解、去使用、去共建。</p>
<p>额外的，<a href="https://juejin.cn/team/6943816493473726472" target="_blank">滴滴前端技术团队的团队号</a>也已经上线，我们也同步了一定的<a href="https://juejin.cn/team/6943816493473726472/hire" target="_blank">招聘信息</a>，我们也会持续增加更多职位，有兴趣的同学可以一起聊聊。</p></div>  
</div>
            