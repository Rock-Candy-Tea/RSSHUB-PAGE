
---
title: 'webpack4流程分析2'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1eec92b9b56418dbc6ae3e295f557d9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 02:20:15 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1eec92b9b56418dbc6ae3e295f557d9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.Compiler</h2>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// 1. 执行run方法开始编译</span>
<span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-comment">// 开始编译 编译完成了执行onCompiled(stats)</span>
  <span class="hljs-built_in">this</span>.compiler(onCompiled)
&#125;
<span class="hljs-comment">// 编译</span>
<span class="hljs-function"><span class="hljs-title">compiler</span>(<span class="hljs-params">callback</span>)</span> &#123;
  <span class="hljs-comment">// 创建参数</span>
  <span class="hljs-comment">// const params = this.newCompilationParams();</span>
  <span class="hljs-keyword">const</span> params = &#123;
    <span class="hljs-comment">// 普通模块工厂</span>
    <span class="hljs-attr">normalModuleFactory</span>: <span class="hljs-built_in">this</span>.createNormalModuleFactory(),
    <span class="hljs-comment">// 上下文模块工厂</span>
    <span class="hljs-attr">contextModuleFactory</span>: <span class="hljs-built_in">this</span>.createContextModuleFactory(),
    <span class="hljs-comment">// 依赖的集合</span>
    <span class="hljs-attr">compilationDependencies</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(),
  &#125;
  <span class="hljs-comment">// 创建compilation对象  params中有普通模块工厂的</span>
  <span class="hljs-keyword">const</span> compilation = <span class="hljs-built_in">this</span>.newCompilation(params);
  <span class="hljs-comment">// 执行make构建 执行单入口插件中注册的钩子</span>
  <span class="hljs-built_in">this</span>.hooks.make(compilation, callback)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. SingleEntryPlugin</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// class SingleEntryPlugin 在webpack执行过程中会注册插件</span>
<span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    compiler.hooks.compilation.tap(
      <span class="hljs-string">"SingleEntryPlugin"</span>,
      <span class="hljs-function">(<span class="hljs-params">compilation, &#123; normalModuleFactory &#125;</span>) =></span> &#123;
        <span class="hljs-comment">// 给compilation的dependencyFactories属性添加属性</span>
        compilation.dependencyFactories.set(
          SingleEntryDependency,
          normalModuleFactory
        );
      &#125;
    );

    <span class="hljs-comment">// compiler中执行make的时候就会执行这个插件</span>
    compiler.hooks.make.tapAsync(
      <span class="hljs-string">"SingleEntryPlugin"</span>,
      <span class="hljs-function">(<span class="hljs-params">compilation, callback</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"SingleEntryPlugin 从此入口文件开始编译"</span>);
        <span class="hljs-comment">// entry是入口文件 name是代码块的名称 context上下文绝对路径</span>
        <span class="hljs-keyword">const</span> &#123; entry, name, context &#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-comment">// 给entry添加了一些属性</span>
        <span class="hljs-keyword">const</span> dep = SingleEntryPlugin.createDependency(entry, name);
        <span class="hljs-comment">// 编译入口文件和他的依赖 这里的dep简单看就是entry</span>
        <span class="hljs-comment">// &#123;loc: &#123;name: 'main'&#125;, module: null, request:'./src/index.js', single entry &#125;</span>
        compilation.addEntry(context, dep, name, callback);
      &#125;
    );
&#125;
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">createDependency</span>(<span class="hljs-params">entry, name</span>)</span> &#123;
    <span class="hljs-comment">// 继承ModuleDependency 继承Dependency</span>
    <span class="hljs-keyword">const</span> dep = <span class="hljs-keyword">new</span> SingleEntryDependency(entry);
    dep.loc = &#123; name &#125;;
    <span class="hljs-keyword">return</span> dep;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3.Compilation</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Compilation</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Tapable</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    <span class="hljs-comment">// 在SingleEntryPlugin的compilation钩子会给变量赋值 不同的文件会对应不同的模块工厂</span>
    <span class="hljs-built_in">this</span>.dependencyFactories = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
  &#125;
  <span class="hljs-comment">// 执行make之后会执行单入口插件的hook执行addEntry() 开始编译一个入口</span>
  <span class="hljs-function"><span class="hljs-title">addEntry</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 增加模块链</span>
    <span class="hljs-built_in">this</span>._addModuleChain(
      context,
      entry,
      <span class="hljs-function">(<span class="hljs-params"><span class="hljs-built_in">module</span></span>) =></span> <span class="hljs-built_in">this</span>.entries.push(<span class="hljs-built_in">module</span>),
      callback
    );
  &#125;
  <span class="hljs-function"><span class="hljs-title">_addModuleChain</span>(<span class="hljs-params">context, dependency, onModule, callback</span>)</span> &#123;
    <span class="hljs-comment">//dep = new new SingleEntryDependency() singleEntryDependency</span>
    <span class="hljs-keyword">const</span> Dep = dependency.constructor;
    <span class="hljs-comment">// 拿到普通模块工厂 normalModuleFactory</span>
    <span class="hljs-keyword">const</span> moduleFactory = <span class="hljs-built_in">this</span>.dependencyFactories.get(Dep);
    <span class="hljs-comment">// 调用create方法创建模块</span>
    moduleFactory.create(&#123;&#125;, <span class="hljs-function">(<span class="hljs-params">err, <span class="hljs-built_in">module</span></span>) =></span> &#123;
      <span class="hljs-comment">// 调用module的build方法开始构建</span>
      <span class="hljs-built_in">this</span>.buildModule(<span class="hljs-built_in">module</span>, <span class="hljs-literal">false</span>, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;&#125;);
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4. NormalModuleFactory</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 普通模块工厂 如何产生normalModule的</span>
<span class="hljs-comment">// 简单理解为 create() &#123;return new NormalModule()&#125;</span>
<span class="hljs-comment">// NormalModuleFactory只是做了一些其他的处理</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NormalModuleFactory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Tapable</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">context, resolverFactory, options</span>)</span> &#123;
    <span class="hljs-comment">// 注册factory钩子 触发返回一个function</span>
    <span class="hljs-built_in">this</span>.hooks.factory.tap(<span class="hljs-string">"NormalModuleFactory"</span>, <span class="hljs-function">() =></span> <span class="hljs-function">(<span class="hljs-params">result, callback</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> resolver = <span class="hljs-built_in">this</span>.hooks.resolver.call(<span class="hljs-literal">null</span>);
      <span class="hljs-comment">// 执行resolver处理loader相关的逻辑</span>
      resolver(result, <span class="hljs-function">(<span class="hljs-params">err, data</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.hooks.afterResolve.callAsync(data, <span class="hljs-function">(<span class="hljs-params">err, result</span>) =></span> &#123;
          <span class="hljs-comment">// 创建模块 NormalModule</span>
          <span class="hljs-keyword">let</span> createdModule = <span class="hljs-built_in">this</span>.hooks.createModule.call(result);
          <span class="hljs-comment">// 普通模块</span>
          <span class="hljs-keyword">if</span> (!createdModule) createdModule = <span class="hljs-keyword">new</span> NormalModule(result);
          createdModule = <span class="hljs-built_in">this</span>.hooks.module.call(createdModule, result);
          <span class="hljs-comment">// 我们的到的模块就普通模块 给create方法</span>
          <span class="hljs-keyword">return</span> callback(<span class="hljs-literal">null</span>, createdModule);
        &#125;);
      &#125;);
    &#125;);

    <span class="hljs-comment">// 注册resolver钩子 会处理一些loader 也会返回一个函数 给factory执行</span>
    <span class="hljs-built_in">this</span>.hooks.factory.tap(<span class="hljs-string">"NormalModuleFactory"</span>, <span class="hljs-function">() =></span> <span class="hljs-function">(<span class="hljs-params">result, callback</span>) =></span> &#123;
      <span class="hljs-comment">// loader的处理</span>
      callback(<span class="hljs-literal">null</span>, &#123;&#125;);
    &#125;);
  &#125;

  <span class="hljs-comment">// create方法 普通模块创建模块</span>
  <span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params">data, callback</span>)</span> &#123;
    <span class="hljs-comment">// 这些参数都会给 factory 执行 factory 的时候会创建 NormalModule 普通模块</span>
    <span class="hljs-keyword">const</span> dependencies = data.dependencies;
    <span class="hljs-keyword">const</span> context = data.context || <span class="hljs-built_in">this</span>.context;
    <span class="hljs-keyword">const</span> resolveOptions = data.resolveOptions || &#123;&#125;;
    <span class="hljs-keyword">const</span> request = dependencies[<span class="hljs-number">0</span>].request; <span class="hljs-comment">// './src/index.js'</span>
    <span class="hljs-keyword">const</span> contextInfo = data.contextInfo || &#123;&#125;;
    <span class="hljs-built_in">this</span>.hooks.beforeResolve.callAsync(&#123;&#125;, <span class="hljs-function">(<span class="hljs-params">err, result</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> factory = <span class="hljs-built_in">this</span>.hooks.factory.call(<span class="hljs-literal">null</span>);
      factory(result, <span class="hljs-function">(<span class="hljs-params">err, <span class="hljs-built_in">module</span></span>) =></span> &#123;
        <span class="hljs-comment">// 这里拿到的module就是factory中callback中的createdModule</span>
        <span class="hljs-comment">// 这个module也是执行create返回的module</span>
        <span class="hljs-comment">// 之后再调用module.build方法开始构建</span>
        callback(<span class="hljs-literal">null</span>, <span class="hljs-built_in">module</span>);
      &#125;);
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">5.demo</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 简化下上面的逻辑</span>

<span class="hljs-comment">// 在factory中会执行resolver方法 处理loader</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolver</span>(<span class="hljs-params">data, callback</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"resolve"</span>, data);
  callback(<span class="hljs-literal">null</span>, &#123;
    <span class="hljs-attr">context</span>: <span class="hljs-string">"context"</span>,
    <span class="hljs-attr">request</span>: <span class="hljs-string">"./src/index.js"</span>,
  &#125;);
&#125;

<span class="hljs-comment">// 注册的factory钩子 执行的时候会返回一个函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">factory</span>(<span class="hljs-params">result, callback</span>) </span>&#123;
  resolver(result, <span class="hljs-function">(<span class="hljs-params">err, data</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"resolver"</span>, data);
    createdModule = <span class="hljs-keyword">new</span> NormalModule(result);
    callback(<span class="hljs-literal">null</span>, createdModule);
  &#125;);
&#125;

<span class="hljs-comment">// 一些参数</span>
<span class="hljs-keyword">let</span> result = &#123;
  <span class="hljs-attr">contextInfo</span>: <span class="hljs-string">"contextInfo"</span>,
  <span class="hljs-attr">resolveOptions</span>: <span class="hljs-string">"resolveOptions"</span>,
  <span class="hljs-attr">context</span>: <span class="hljs-string">"context"</span>,
  <span class="hljs-attr">request</span>: <span class="hljs-string">"request"</span>,
  <span class="hljs-attr">dependencies</span>: <span class="hljs-string">"dependencies"</span>,
&#125;;

<span class="hljs-comment">// 在create中会执行factory方法</span>
factory(result, <span class="hljs-function">(<span class="hljs-params">err, <span class="hljs-built_in">module</span></span>) =></span> &#123;
  <span class="hljs-comment">// 这里就可以拿到NormalModule</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"factory"</span>, <span class="hljs-built_in">module</span>);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">6. NormalModule</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NormalModule</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Module</span> </span>&#123;
  <span class="hljs-comment">// 调用模块的build方法开始编译</span>
  <span class="hljs-function"><span class="hljs-title">build</span>(<span class="hljs-params">options, compilation, resolver, fs, callback</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.doBuild(options, compilation, resolver, fs, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"build"</span>);
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">7.总结</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1eec92b9b56418dbc6ae3e295f557d9~tplv-k3u1fbpfcp-watermark.image" alt="无标题-2021-06-09-1537.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">在compiler中执行compiler 
==> 创建params 普通模块工厂 normalModuleFactory
==> 创建compilation对象 里面有一个 dependencyFactories 来记录不同模块的工厂函数
    ==> 创建过程中会触发 <span class="hljs-built_in">this</span>.hooks.compilation.call(compilation, params)
    ==> 执行SingleEntryPlugin中对应的钩子 记录SingleEntryDependency: normalModuleFactory
==> 执行make ==> 执行SingleEntryPlugin中的钩子 
    ==> 处理entry包装为SingleEntryDependency ==> compilation.addEntry()
    => addEntry开始编译一个新的入口 
    ==> addModuleChain()增加模块链
        ==> 从dependencyFactories中找到普通模块工厂 
        ==> 调用moduleFactory.create()方法创建
        ==> create()执行factory 得到<span class="hljs-built_in">module</span> = <span class="hljs-keyword">new</span> NormalModule() 普通模块
        ==> 执行模块的build方法(NormalModule.build)开始构建模块
        ==> afterBuild 递归处理依赖
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            