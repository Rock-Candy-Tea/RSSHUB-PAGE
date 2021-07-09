
---
title: 'webpack4流程分析4'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64f42b921d924e0aa6c16aeb186e3366~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 02:21:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64f42b921d924e0aa6c16aeb186e3366~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">NormalModule</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 经过上面的分析 我们知道调用 NormalModule 的build方法是真正的开始</span>
<span class="hljs-comment">// NormalModule 继承 Module</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NormalModule</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Module</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">build</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// doBuild就是runLoaders过程 先不考虑loader的情况</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.doBuild(options, compilation, resolver, fs, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
      <span class="hljs-comment">// 使用acorn解析生成ast 然后遍历</span>
      <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">this</span>.parser.parse(
        <span class="hljs-comment">//  this._source = this.createSource()</span>
        <span class="hljs-comment">// return new OriginalSource(source, this.request);</span>
        <span class="hljs-built_in">this</span>._ast || <span class="hljs-built_in">this</span>._source.source(),
        &#123;&#125;,
        cb
      );
    &#125;);
  &#125;
&#125;
<span class="hljs-comment">// Module 继承 DependenciesBlock</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Module</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">DependenciesBlock</span> </span>&#123;&#125;
<span class="hljs-comment">//里面有个重要的方法</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DependenciesBlock</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.dependencies = [];
    <span class="hljs-built_in">this</span>.blocks = [];
    <span class="hljs-built_in">this</span>.variables = [];
  &#125;
  <span class="hljs-function"><span class="hljs-title">addDependency</span>(<span class="hljs-params">dependency</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.dependencies.push(dependency);
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">NormalModuleFactory</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在上一章 我们知道 NormalModule 是在 NormalModuleFactory 中执行factory的时候new的</span>
<span class="hljs-comment">// 在 resolver 的过程中返回了 new module 的参数 我们先看下参数</span>
<span class="hljs-comment">// 暂时先不考虑loader的过程 这个步骤找到了绝对路径</span>
callback(<span class="hljs-literal">null</span>, &#123;
    context,
    <span class="hljs-comment">// request, // request: loaders.map(),</span>
    <span class="hljs-attr">request</span>: path.posix.join(context, request), <span class="hljs-comment">// 绝对路径</span>
    <span class="hljs-attr">dependencies</span>: data.dependencies, <span class="hljs-comment">// 依赖 这个时候是 SingleEntryDependency</span>
    <span class="hljs-attr">userRequest</span>: path.posix.join(context, request), <span class="hljs-comment">// 绝对路径 暂时使用path</span>
    <span class="hljs-attr">rawRequest</span>: request, <span class="hljs-comment">// './src/index.js'</span>
    <span class="hljs-attr">loaders</span>: [],
    <span class="hljs-comment">// 这里暂时使用entry的绝对路径来替代 忽略loader的部分</span>
    <span class="hljs-attr">resource</span>: path.posix.join(context, request),
    <span class="hljs-comment">// matchResource,</span>
    <span class="hljs-comment">// resourceResolveData,</span>
    settings, <span class="hljs-comment">// &#123;type: 'javascript/auto'&#125;</span>
    <span class="hljs-attr">type</span>: settings.type,
    <span class="hljs-comment">// js解析器 JavascriptModulesPlugin插件</span>
    <span class="hljs-attr">parser</span>: <span class="hljs-built_in">this</span>.getParser(settings.type, settings.parser),
    <span class="hljs-comment">// 不同的模块使用不同的生成器 为模版生成提供api方法</span>
    <span class="hljs-attr">generator</span>: <span class="hljs-built_in">this</span>.getGenerator(settings.type, settings.generator),
    <span class="hljs-attr">resolveOptions</span>: data.resolveOptions,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">JavascriptModulesPlugin</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// parser 哪来的? 不同类型的文件我们会有不同的解析器</span>
<span class="hljs-comment">// 在执行webpack的过程中 会处理 WebpackOptionsApply</span>
<span class="hljs-keyword">new</span> JavascriptModulesPlugin().apply(compiler); <span class="hljs-comment">// js模块</span>
<span class="hljs-keyword">new</span> JsonModulesPlugin().apply(compiler); <span class="hljs-comment">// json模块</span>
... 其他模块对应的插件处理

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">JavascriptModulesPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    <span class="hljs-comment">// 在compiler的hooks上有很多 compilation 的钩子</span>
    <span class="hljs-comment">// 当创建 compilation 的时候 会触发对应的钩子 执行一些列的hook</span>
    compiler.hooks.compilation.tap(
      <span class="hljs-string">"JavascriptModulesPlugin"</span>,
      <span class="hljs-function">(<span class="hljs-params">compilation, &#123; normalModuleFactory &#125;</span>) =></span> &#123;
        normalModuleFactory.hooks.createParser
          .for(<span class="hljs-string">"javascript/auto"</span>) <span class="hljs-comment">// 针对不同的type会有不同的钩子</span>
          .tap(<span class="hljs-string">"JavascriptModulesPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">options</span>) =></span> &#123;
            <span class="hljs-comment">// js的解析器就是这里得到的</span>
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Parser(options, <span class="hljs-string">"auto"</span>);
          &#125;);
        <span class="hljs-comment">// 模版主要和生成代码相关逻辑之后分析</span>
        compilation.mainTemplate.hooks.modules.tap();
      &#125;
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Parser</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在上一篇的时候 我们直接跳过了parse的过程 现在简单看下 </span>
<span class="hljs-comment">// 我们在初始化compilation之后通过模块工厂创建模块就可以拿到这里的js解析器</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parser</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Tapable</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options, sourceType = <span class="hljs-string">"auto"</span></span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
    <span class="hljs-comment">// 一堆的hooks</span>
    <span class="hljs-built_in">this</span>.hooks = &#123;&#125;;
  &#125;
  <span class="hljs-comment">// 我们调用parser方法 source是经过loader-runner处理过的代码</span>
  <span class="hljs-comment">// 主要是分两步 一个是parse解析 一个是遍历(触发各种hooks)</span>
  <span class="hljs-function"><span class="hljs-title">parse</span>(<span class="hljs-params">source, initialState</span>)</span> &#123;
    <span class="hljs-comment">// 生成ast语法树</span>
    <span class="hljs-keyword">let</span> ast = Parser.parse(source, &#123; <span class="hljs-attr">sourceType</span>: <span class="hljs-string">"module"</span> &#125;);
    <span class="hljs-comment">// 和作用域相关的 例如函数作用域 块级作用域等 先不考虑</span>
    <span class="hljs-built_in">this</span>.scope = &#123;&#125;;
    <span class="hljs-keyword">const</span> state = (<span class="hljs-built_in">this</span>.state = initialState || &#123;&#125;);
    <span class="hljs-comment">// 对语法树进行分析 主要就是用 module 的 addDependency 方法增加一些依赖 还有模板的处理</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.hooks.program.call(ast, comments) === <span class="hljs-literal">undefined</span>) &#123;
      <span class="hljs-comment">// 针对不同的节点做不同的处理</span>
      <span class="hljs-built_in">this</span>.detectMode(ast.body);
      <span class="hljs-built_in">this</span>.prewalkStatements(ast.body);
      <span class="hljs-built_in">this</span>.blockPrewalkStatements(ast.body);
      <span class="hljs-built_in">this</span>.walkStatements(ast.body);
    &#125;
    <span class="hljs-keyword">return</span> state;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">HarmonyModulesPlugin</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack对不同的依赖模块会有不同的模版处理</span>
<span class="hljs-comment">// ES module最终会给 HarmonyModulesPlugin 里面的依赖来处理</span>
<span class="hljs-comment">// CommonJS Module 的会给 CommonJsPlugin 里面的依赖处理 对其他的模块也有处理</span>
<span class="hljs-comment">// 我们以Esmodule为例分析 其他的跳过</span>

<span class="hljs-comment">// 1. 这些hook是什么时候注册的</span>
还是和之前一样 我们在执行webpack的时候 会执行 WebpackOptionsApply 里面是做了很多事的
<span class="hljs-keyword">new</span> ConstPlugin().apply(compiler);
<span class="hljs-keyword">new</span> ImportPlugin(options.module).apply(compiler);
<span class="hljs-keyword">new</span> HarmonyModulesPlugin(options.module).apply(compiler);
<span class="hljs-keyword">new</span> APIPlugin().apply(compiler);
<span class="hljs-keyword">new</span> CommonJsPlugin(options.module).apply(compiler);

<span class="hljs-comment">// 2.HarmonyModulesPlugin主要做了些啥</span>
<span class="hljs-comment">// 引入一些列的 不同语法的依赖类型</span>
<span class="hljs-keyword">const</span> HarmonyInitDependency = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./HarmonyInitDependency"</span>);
...
<span class="hljs-comment">// 不同的语法在编译过程中挂载的hooks</span>
<span class="hljs-keyword">const</span> HarmonyDetectionParserPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./HarmonyDetectionParserPlugin"</span>);
<span class="hljs-keyword">const</span> HarmonyImportDependencyParserPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./HarmonyImportDependencyParserPlugin"</span>);
<span class="hljs-keyword">const</span> HarmonyExportDependencyParserPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./HarmonyExportDependencyParserPlugin"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HarmonyModulesPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    compiler.hooks.compilation.tap(
      <span class="hljs-string">"HarmonyModulesPlugin"</span>,
      <span class="hljs-function">(<span class="hljs-params">compilation, &#123; normalModuleFactory &#125;</span>) =></span> &#123;
        <span class="hljs-comment">// 设置工厂和模块</span>
        compilation.dependencyFactories.set(
          HarmonyImportSpecifierDependency,
          normalModuleFactory
        );
        compilation.dependencyTemplates.set(
          HarmonyImportSpecifierDependency,
          <span class="hljs-keyword">new</span> HarmonyImportSpecifierDependency.Template()
        );
        <span class="hljs-keyword">const</span> handler = <span class="hljs-function">(<span class="hljs-params">parser, parserOptions</span>) =></span> &#123;
           <span class="hljs-comment">// 判断 esmodule</span>
           <span class="hljs-keyword">new</span> HarmonyDetectionParserPlugin().apply(parser);
          <span class="hljs-comment">// 处理import</span>
          <span class="hljs-keyword">new</span> HarmonyImportDependencyParserPlugin(<span class="hljs-built_in">this</span>.options).apply(parser);
          <span class="hljs-comment">// 处理export</span>
          <span class="hljs-keyword">new</span> HarmonyExportDependencyParserPlugin(<span class="hljs-built_in">this</span>.options).apply(parser);
        &#125;;

        <span class="hljs-comment">// 注册parser钩子 创建新的 normalModule 时钩子会被执行</span>
        <span class="hljs-comment">// handler会初始化各种plugin 注册相关的hooks</span>
        normalModuleFactory.hooks.parser
          .for(<span class="hljs-string">"javascript/auto"</span>)
          .tap(<span class="hljs-string">"HarmonyModulesPlugin"</span>, handler);
      &#125;
    );
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">HarmonyDetectionParserPlugin</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HarmonyDetectionParserPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">parser</span>)</span> &#123;
    parser.hooks.program.tap(<span class="hljs-string">"HarmonyDetectionParserPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">ast</span>) =></span> &#123;
      <span class="hljs-comment">// const isHarmony 判断import export的声明</span>
      <span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> = parser.state.module;
      <span class="hljs-keyword">const</span> compatDep = <span class="hljs-keyword">new</span> HarmonyCompatibilityDependency(<span class="hljs-built_in">module</span>);
      <span class="hljs-comment">// 增加依赖</span>
      <span class="hljs-built_in">module</span>.addDependency(compatDep);
      <span class="hljs-keyword">const</span> initDep = <span class="hljs-keyword">new</span> HarmonyInitDependency(<span class="hljs-built_in">module</span>);
      <span class="hljs-built_in">module</span>.addDependency(initDep);
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">import export</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 我们些代码 es module 一般是 import 和 export 语法</span>
<span class="hljs-comment">// 但是也会有多种写法 对应ast不同的称谓  之后学习babel的时候在重要学习 这里先简单有点印象</span>
<span class="hljs-keyword">import</span> x1 <span class="hljs-keyword">from</span> <span class="hljs-string">'./xx'</span> 
<span class="hljs-keyword">import</span> &#123;x2&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./xx'</span> 
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> x3 <span class="hljs-keyword">from</span> <span class="hljs-string">'./xx'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64f42b921d924e0aa6c16aeb186e3366~tplv-k3u1fbpfcp-watermark.image" alt="WX20210617-092838@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// export也会有很多不同的写法 感觉平时主要是 默认导出和具名导出</span>
<span class="hljs-comment">// import中type是一样的 export的type是不一样的 之后在处理ast的时候要注意</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'name'</span>&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> a = <span class="hljs-string">'a'</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02564e6c9aae4b17ac8c9f1acfdad1b5~tplv-k3u1fbpfcp-watermark.image" alt="WX20210617-093225@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">HarmonyImportDependencyParserPlugin</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 主要用来处理import的</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HarmonyImportDependencyParserPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">parser</span>)</span> &#123;
    <span class="hljs-comment">// import的钩子</span>
    parser.hooks.import.tap(
      <span class="hljs-string">"HarmonyImportDependencyParserPlugin"</span>,
      <span class="hljs-function">(<span class="hljs-params">statement, source</span>) =></span> &#123;
        <span class="hljs-comment">// 根据条件增加依赖</span>
        parser.state.module.addDependency(clearDep);
        parser.state.module.addDependency(sideEffectDep);
      &#125;
    );
    parser.hooks.importSpecifier.tap()
    parser.hooks.expression()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">HarmonyExportDependencyParserPlugin</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 主要是用来处理export</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HarmonyExportDependencyParserPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">parser</span>)</span> &#123;
    <span class="hljs-comment">// export 在parse的过程中会触发各种的hook</span>
    parser.hooks.export.tap(
      <span class="hljs-string">"HarmonyExportDependencyParserPlugin"</span>,
      <span class="hljs-function">(<span class="hljs-params">statement</span>) =></span> &#123;
        <span class="hljs-comment">// new HarmonyExportHeaderDependency() 不同的依赖</span>
        parser.state.current.addDependency(dep);
      &#125;
    );
    parser.hooks.exportImport.tap();
    parser.hooks.exportExpression.tap();
    parser.hooks.exportSpecifier.tap();
    parser.hooks.exportImportSpecifier.tap();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">demo</h2>
<pre><code class="copyable">// index.js 我们些一个demo 先只考虑 es module的情况 不分析 commonjs规范
// 在 https://astexplorer.net/ 中查看ast的结构
import sync from "./sync";
console.log(sync);
import(/*webpackChunkName: 'async'*/ "./async").then((result) => &#123;
  console.log(result.default);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/034306c2b8e74c44b0c3c0236f6cf987~tplv-k3u1fbpfcp-watermark.image" alt="ast.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 我们得到的ast语法树 body 中有三个  我们会遍历处理这里面的节点</span>

<span class="hljs-keyword">const</span> obj = &#123;
  <span class="hljs-comment">// 第一个是import</span>
  <span class="hljs-string">"type"</span>: <span class="hljs-string">"ImportDeclaration"</span>,
  <span class="hljs-string">"specifiers"</span>: [
    &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-string">"ImportDefaultSpecifier"</span>,
      <span class="hljs-string">"local"</span>: &#123; <span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>, <span class="hljs-string">"name"</span>: <span class="hljs-string">"sync"</span>&#125;
    &#125;
  ],
  <span class="hljs-string">"source"</span>: &#123; <span class="hljs-string">"type"</span>: <span class="hljs-string">"Literal"</span>,  <span class="hljs-string">"value"</span>: <span class="hljs-string">"./sync"</span>,  <span class="hljs-string">"raw"</span>: <span class="hljs-string">"\"./sync\""</span>&#125;
&#125;,
<span class="hljs-comment">// 后面两个都是 表达式</span>
<span class="hljs-keyword">const</span> obj1 = &#123;
  <span class="hljs-string">"type"</span>: <span class="hljs-string">"ExpressionStatement"</span>,
  <span class="hljs-string">"expression"</span>: &#123;
    <span class="hljs-string">"type"</span>: <span class="hljs-string">"CallExpression"</span>,
    <span class="hljs-string">"callee"</span>: &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-string">"MemberExpression"</span>,
      <span class="hljs-string">"object"</span>: &#123;  <span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>,  <span class="hljs-string">"name"</span>: <span class="hljs-string">"console"</span>  &#125;,
      <span class="hljs-string">"property"</span>: &#123; <span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>,  <span class="hljs-string">"name"</span>: <span class="hljs-string">"log"</span>  &#125;,
    &#125;,
    <span class="hljs-string">"arguments"</span>: [
      &#123; <span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>,  <span class="hljs-string">"name"</span>: <span class="hljs-string">"sync"</span>  &#125;
    ]
  &#125;
&#125;

<span class="hljs-keyword">const</span> obj2 = &#123;
  <span class="hljs-string">"type"</span>: <span class="hljs-string">"ExpressionStatement"</span>,
  <span class="hljs-string">"expression"</span>: &#123;
  <span class="hljs-string">"type"</span>: <span class="hljs-string">"CallExpression"</span>,
  <span class="hljs-string">"callee"</span>: &#123;
    <span class="hljs-string">"type"</span>: <span class="hljs-string">"MemberExpression"</span>,
    <span class="hljs-string">"object"</span>: &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-string">"ImportExpression"</span>,
      <span class="hljs-string">"source"</span>: &#123; <span class="hljs-string">"type"</span>: <span class="hljs-string">"Literal"</span>,  <span class="hljs-string">"value"</span>: <span class="hljs-string">"./async"</span>,  <span class="hljs-string">"raw"</span>: <span class="hljs-string">"\"./async\""</span>  &#125;
    &#125;,
    <span class="hljs-string">"property"</span>: &#123;<span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>,  <span class="hljs-string">"name"</span>: <span class="hljs-string">"then"</span> &#125;,
  &#125;,
  <span class="hljs-string">"arguments"</span>: [
    &#123;
      <span class="hljs-string">"type"</span>: <span class="hljs-string">"ArrowFunctionExpression"</span>,
      <span class="hljs-string">"params"</span>: [  &#123; <span class="hljs-string">"type"</span>: <span class="hljs-string">"Identifier"</span>,  <span class="hljs-string">"name"</span>: <span class="hljs-string">"result"</span> &#125;  ],
      <span class="hljs-string">"body"</span>: &#123; <span class="hljs-string">"type"</span>: <span class="hljs-string">"BlockStatement"</span>,  <span class="hljs-string">"body"</span>: [  <span class="hljs-comment">/** console和上面一样的  */</span> ]
        &#125;
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">parse</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// parse的过程是直接使用了 Parser.parse 生成语法树</span>
<span class="hljs-comment">// 遍历的工具 babel有 @babel/traverse esprima 是有 estraverse acorn自己处理</span>
<span class="hljs-comment">// 上面的过程主要是经过5个步骤 我们一个一个来看</span>
<span class="hljs-built_in">this</span>.hooks.program.call(ast, comments)
<span class="hljs-built_in">this</span>.detectMode(ast.body);
<span class="hljs-built_in">this</span>.prewalkStatements(ast.body);
<span class="hljs-built_in">this</span>.blockPrewalkStatements(ast.body);
<span class="hljs-built_in">this</span>.walkStatements(ast.body);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">1.program</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// this.hooks.program.call(ast, comments)</span>
<span class="hljs-comment">// 会触发 HarmonyDetectionParserPlugin 中注册的钩子</span>
<span class="hljs-comment">// 根据条件给我们增加依赖</span>
HarmonyCompatibilityDependency
HarmonyInitDependency
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">2.detectMode</h3>
<pre><code class="copyable">// 这一步主要是处理 严格模式 scope 的逻辑跳过
if (isLiteral && statements[0].expression.value === "use strict") &#123;
    this.scope.isStrict = true;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">3.prewalkStatements</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// this.prewalkStatements(ast.body);</span>
<span class="hljs-comment">// 1. 遍历执行</span>
<span class="hljs-built_in">this</span>.prewalkStatement(statement);
<span class="hljs-comment">// 2. 根据不同的类型执行不同的分支 我们demo中的三个 type为 ImportDeclaration 和 ExpressionStatement</span>
<span class="hljs-comment">// prewalkStatement不处理 ExpressionStatement 的类型 主要还是在处理 import和export</span>
<span class="hljs-comment">// ast.body的第一个节点会进入</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">prewalkStatement</span>(<span class="hljs-params">statement</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (statement.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"ImportDeclaration"</span>:
      <span class="hljs-built_in">this</span>.prewalkImportDeclaration(statement);
      <span class="hljs-keyword">break</span>;
  &#125;
&#125;
<span class="hljs-comment">// 3.处理import prewalkImportDeclaration import 又会根据 specifiers 分不同的类型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">prewalkImportDeclaration</span>(<span class="hljs-params">statement</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> specifier <span class="hljs-keyword">of</span> statement.specifiers) &#123;
    <span class="hljs-keyword">const</span> name = specifier.local.name;
    <span class="hljs-keyword">switch</span> (specifier.type) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"ImportDefaultSpecifier"</span>:
        <span class="hljs-comment">// 不同的类型会触发不同的 hooks</span>
        <span class="hljs-built_in">this</span>.hooks.importSpecifier.call(statement, source, <span class="hljs-string">"default"</span>, name);
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"ImportSpecifier"</span>:
        <span class="hljs-built_in">this</span>.hooks.importSpecifier.call(
          statement,
          source,
          specifier.imported.name,
          name
        );
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"ImportNamespaceSpecifier"</span>:
        <span class="hljs-built_in">this</span>.hooks.importSpecifier.call(statement, source, <span class="hljs-literal">null</span>, name);
        <span class="hljs-keyword">break</span>;
    &#125;
  &#125;
&#125;
<span class="hljs-comment">// 4. 触发hooks执行 HarmonyImportDependencyParserPlugin 增加依赖</span>
<span class="hljs-keyword">const</span> clearDep = <span class="hljs-keyword">new</span> ConstDependency(<span class="hljs-string">""</span>, statement.range);
<span class="hljs-keyword">const</span> sideEffectDep = <span class="hljs-keyword">new</span> HarmonyImportSideEffectDependency()
parser.state.module.addDependency(clearDep);
parser.state.module.addDependency(sideEffectDep);

<span class="hljs-comment">// 5.又新增了两个依赖</span>
HarmonyCompatibilityDependency
HarmonyInitDependency 

ConstDependency 
HarmonyImportSideEffectDependency 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">4.blockPrewalkStatements</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// this.blockPrewalkStatements(ast.body);</span>
<span class="hljs-comment">// 1. 同理遍历执行 blockPrewalkStatement</span>
<span class="hljs-built_in">this</span>.blockPrewalkStatement(statement);
<span class="hljs-comment">// 2.判断statement的type类型 很明显我们的demo没有对应的分支流程</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">blockPrewalkStatement</span>(<span class="hljs-params">statement</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (statement.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"VariableDeclaration"</span>:
      <span class="hljs-built_in">this</span>.blockPrewalkVariableDeclaration(statement);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"ExportDefaultDeclaration"</span>:
      <span class="hljs-built_in">this</span>.blockPrewalkExportDefaultDeclaration(statement);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"ExportNamedDeclaration"</span>:
      <span class="hljs-built_in">this</span>.blockPrewalkExportNamedDeclaration(statement);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"ClassDeclaration"</span>:
      <span class="hljs-built_in">this</span>.blockPrewalkClassDeclaration(statement);
      <span class="hljs-keyword">break</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">5. walkStatements</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// this.walkStatements(ast.body);</span>
<span class="hljs-comment">// 1.还是遍历执行</span>
<span class="hljs-built_in">this</span>.walkStatement(statement);
<span class="hljs-comment">// 2. 也是判断type的不同类型</span>
<span class="hljs-comment">// 在我们的case中 body第一个节点不走这个分支 后面两个都是ExpressionStatement</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">walkStatement</span>(<span class="hljs-params">statement</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (statement.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"ExpressionStatement"</span>:
      <span class="hljs-built_in">this</span>.walkExpressionStatement(statement);
      <span class="hljs-keyword">break</span>;
  &#125;
&#125;
<span class="hljs-comment">// 3. walkExpressionStatement 其实是处理expression</span>
<span class="hljs-built_in">this</span>.walkExpression(statement.expression);
<span class="hljs-comment">// 4.回顾下ast的结构</span>
<span class="hljs-comment">// type callee arguments</span>
<span class="hljs-comment">// 5. 判断不同的类型 我们的demo都是CallExpression</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">walkExpression</span>(<span class="hljs-params">expression</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (expression.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"CallExpression"</span>:
      <span class="hljs-built_in">this</span>.walkCallExpression(expression);
      <span class="hljs-keyword">break</span>;
  &#125;
&#125;
<span class="hljs-comment">// 6. 执行 walkCallExpression</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">walkCallExpression</span>(<span class="hljs-params">expression</span>) </span>&#123;
  <span class="hljs-comment">// 判断expression.callee.type 的类型</span>
  <span class="hljs-keyword">if</span> (
    expression.callee.type === <span class="hljs-string">"MemberExpression"</span> &&
    expression.callee.object.type === <span class="hljs-string">"FunctionExpression"</span>
  ) &#123;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (expression.callee.type === <span class="hljs-string">"FunctionExpression"</span>) &#123;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (expression.callee.type === <span class="hljs-string">"Import"</span>) &#123;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 计算函数表达式</span>
    <span class="hljs-keyword">const</span> callee = <span class="hljs-built_in">this</span>.evaluateExpression(expression.callee);
    <span class="hljs-keyword">if</span> (callee.isIdentifier()) &#123;
      <span class="hljs-comment">// 判断是不是标识符</span>
      <span class="hljs-keyword">const</span> callHook = <span class="hljs-built_in">this</span>.hooks.call.get(callee.identifier);
      <span class="hljs-keyword">if</span> (callHook !== <span class="hljs-literal">undefined</span>) &#123;
        <span class="hljs-comment">// 执行callHook</span>
        <span class="hljs-keyword">let</span> result = callHook.call(expression);
      &#125;
      <span class="hljs-keyword">const</span> callAnyHook = <span class="hljs-built_in">this</span>.hooks.callAnyMember.get(identifier);
      <span class="hljs-keyword">if</span> (callAnyHook !== <span class="hljs-literal">undefined</span>) &#123;
        <span class="hljs-keyword">let</span> result = callAnyHook.call(expression);
      &#125;
    &#125;
    <span class="hljs-comment">// 处理callee和arguments</span>
    <span class="hljs-keyword">if</span> (expression.callee) <span class="hljs-built_in">this</span>.walkExpression(expression.callee);
    <span class="hljs-keyword">if</span> (expression.arguments) <span class="hljs-built_in">this</span>.walkExpressions(expression.arguments);
  &#125;
&#125;
<span class="hljs-comment">// 7.执行walkExpression(expression.callee)</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">walkExpression</span>(<span class="hljs-params">expression</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (expression.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"MemberExpression"</span>:
      <span class="hljs-built_in">this</span>.walkMemberExpression(expression);
      <span class="hljs-keyword">break</span>;
  &#125;
&#125;
<span class="hljs-comment">// 8. walkMemberExpression</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">walkMemberExpression</span>(<span class="hljs-params">expression</span>) </span>&#123;
  <span class="hljs-keyword">const</span> exprName = <span class="hljs-built_in">this</span>.getNameForExpression(expression);
  <span class="hljs-keyword">const</span> expressionHook = <span class="hljs-built_in">this</span>.hooks.expression.get(exprName.name);
  <span class="hljs-keyword">const</span> expressionAnyMemberHook = <span class="hljs-built_in">this</span>.hooks.expressionAnyMember.get();
  <span class="hljs-comment">// 深度遍历执行object</span>
  <span class="hljs-built_in">this</span>.walkExpression(expression.object);
&#125;
<span class="hljs-comment">// 9.我们的object中是Identifier</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">walkExpression</span>(<span class="hljs-params">expression</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (expression.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"Identifier"</span>:
      <span class="hljs-built_in">this</span>.walkIdentifier(expression);
      <span class="hljs-keyword">break</span>;
  &#125;
&#125;
<span class="hljs-comment">// 10. 我们执行walkIdentifier</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">walkIdentifier</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 会判断作用域</span>
  <span class="hljs-comment">// if (!this.scope.definitions.has(expression.name)) &#123; &#125;</span>
  <span class="hljs-keyword">const</span> hook = <span class="hljs-built_in">this</span>.hooks.expression.get(); <span class="hljs-comment">// 有就执行</span>
  <span class="hljs-keyword">const</span> result = hook.call(expression);
&#125;

<span class="hljs-comment">// 11.处理完callee我们就要处理arguments 是多个 需要遍历处理</span>
<span class="hljs-comment">// 增加了一个依赖 HarmonyImportSpecifierDependency</span>

<span class="hljs-comment">// 12. 处理完ast.body中第二个元素之后 需要处理第三个元素</span>
<span class="hljs-comment">// 在处理callee的时候 object的type为ImportExpression</span>
<span class="hljs-comment">// 在处理arguments时为 ArrowFunctionExpression</span>

<span class="hljs-comment">// 13.处理callee</span>
<span class="hljs-built_in">this</span>.walkExpression(expression.object);
<span class="hljs-built_in">this</span>.walkCallExpression(expression);
<span class="hljs-comment">// 14. type为ImportExpression</span>
<span class="hljs-function"><span class="hljs-title">walkCallExpression</span>(<span class="hljs-params">expression</span>)</span> &#123;
  <span class="hljs-comment">// type为import 执行对应的hooks 进入到 ImportParserPlugin 插件中</span>
  <span class="hljs-keyword">let</span> result = <span class="hljs-built_in">this</span>.hooks.importCall.call(expression);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">acorn</h2>
<pre><code class="copyable">// webpack的ast和我们在网站上生成的代码有一些差异
// 当webpack在使用acorn的时候 有一些默认的参数 
// ecmaVersion: 11, sourceType: "module", acorn的版本也有一定的差异
// 主要看第二个节点的callee部分结构如下
Node &#123;
  type: 'CallExpression',
  start: 47,
  end: 64,
  loc: SourceLocation &#123;
    start: Position &#123; line: 4, column: 0 &#125;,
    end: Position &#123; line: 4, column: 17 &#125;
  &#125;,
  range: [ 47, 64 ],
  callee: Node &#123;
    type: 'Import',
    start: 47,
    end: 53,
    loc: SourceLocation &#123; start: [Position], end: [Position] &#125;,
    range: [ 47, 53 ]
  &#125;,
  arguments: [
    Node &#123;
      type: 'Literal',
      start: 54,
      end: 63,
      loc: [SourceLocation],
      range: [Array],
      value: './async',
      raw: '"./async"'
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">ImportParserPlugin</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在webpackOptionsApply中  </span>
<span class="hljs-keyword">new</span> ImportPlugin(options.module).apply(compiler)
<span class="hljs-comment">// ImportPlugin中会引入</span>
<span class="hljs-keyword">const</span> ImportParserPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./ImportParserPlugin"</span>);
<span class="hljs-keyword">const</span> ImportDependency = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./ImportDependency"</span>);
<span class="hljs-comment">// 也是设置依赖和模版 然后执行handler</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ImportPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    compiler.hooks.compilation.tap(
      <span class="hljs-string">"ImportPlugin"</span>,
      <span class="hljs-function">(<span class="hljs-params">compilation, &#123; contextModuleFactory, normalModuleFactory &#125;</span>) =></span> &#123;
        compilation.dependencyFactories.set(
          ImportDependency,
          normalModuleFactory
        );
        compilation.dependencyTemplates.set(
          ImportDependency,
          <span class="hljs-keyword">new</span> ImportDependency.Template()
        );
        <span class="hljs-keyword">const</span> handler = <span class="hljs-function">(<span class="hljs-params">parser, parserOptions</span>) =></span> &#123;
          <span class="hljs-keyword">new</span> ImportParserPlugin(options).apply(parser);
        &#125;;
        <span class="hljs-comment">// 处理js</span>
        normalModuleFactory.hooks.parser
          .for(<span class="hljs-string">"javascript/auto"</span>)
          .tap(<span class="hljs-string">"ImportPlugin"</span>, handler);
      &#125;
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">ImportParserPlugin</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ImportParserPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">parser</span>)</span> &#123;
    parser.hooks.importCall.tap(<span class="hljs-string">"ImportParserPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">expr</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> depBlock = <span class="hljs-keyword">new</span> ImportDependenciesBlock();
      <span class="hljs-comment">// 增加block</span>
      parser.state.current.addBlock(depBlock);
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">dependencies</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 经过上面ast的处理 我们当前模块增加了5个依赖 对应不同的模板</span>
<span class="hljs-comment">// 这些依赖时做什么的 暂时还是不清楚的</span>
HarmonyCompatibilityDependency <span class="hljs-comment">// 用于定义 exports:__esModule</span>
HarmonyInitDependency  <span class="hljs-comment">// </span>

ConstDependency  <span class="hljs-comment">// clean操作 删除</span>
HarmonyImportSideEffectDependency  <span class="hljs-comment">// 模版</span>

HarmonyImportSpecifierDependency <span class="hljs-comment">// 模版</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">blocks</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// blocks属性 对应我们 动态import的模块</span>
<span class="hljs-comment">// ImportDependenciesBlock </span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            