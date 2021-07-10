
---
title: 'webpack4流程分析3'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5656'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 02:20:55 GMT
thumbnail: 'https://picsum.photos/400/300?random=5656'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. NormalModule</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NormalModule</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Module</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">&#123; type, request, rawRequest, loaders, resource, parser, generator &#125;</span>)</span> &#123;
    <span class="hljs-comment">// 这些参数都是如何来的? 到NormalModuleFactory中查看</span>
    <span class="hljs-built_in">this</span>.type = type
    <span class="hljs-built_in">this</span>.request = request <span class="hljs-comment">// 经过loader处理过的 loaders.map()</span>
    <span class="hljs-built_in">this</span>.rawRequest = rawRequest
    <span class="hljs-built_in">this</span>.loaders = loaders <span class="hljs-comment">// loader</span>
    <span class="hljs-built_in">this</span>.resource = resource <span class="hljs-comment">// code</span>
    <span class="hljs-built_in">this</span>.parser = parser <span class="hljs-comment">// js解析器</span>
    <span class="hljs-built_in">this</span>.generator = generator <span class="hljs-comment">// 模版生成</span>
  &#125;
  <span class="hljs-comment">// 调用build方法开始构建</span>
  <span class="hljs-function"><span class="hljs-title">build</span>(<span class="hljs-params">options, compilation, resolver, fs, callback</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.doBuild(options, compilation, resolver, fs, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
      <span class="hljs-comment">// webpack中使用acorn 我们可以使用babel来模拟</span>
      <span class="hljs-comment">// 关注主流程 parser 过程比较复杂先跳过不分析</span>
      <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">this</span>.parser.parse(
        <span class="hljs-built_in">this</span>._ast || <span class="hljs-built_in">this</span>._source.source(),
        &#123;&#125;,
        cb
      );
      callback();
    &#125;);
  &#125;
  <span class="hljs-function"><span class="hljs-title">doBuild</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 处理loader 这里就是loader执行的时机 将code经过loader处理之后在给parse解析</span>
    <span class="hljs-comment">// runLoaders的流程也相对独立 跳过</span>
    runLoaders(&#123;&#125;, <span class="hljs-function">(<span class="hljs-params">err, result</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> callback();
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. NormalModuleFactory</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NormalModuleFactory</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">context, resolverFactory, options</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.resolverFactory = resolverFactory;
    <span class="hljs-built_in">this</span>.hooks.factory.tap(<span class="hljs-string">"NormalModuleFactory"</span>, <span class="hljs-function">() =></span> <span class="hljs-function">(<span class="hljs-params">result, callback</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> resolver = <span class="hljs-built_in">this</span>.hooks.resolver.call(<span class="hljs-literal">null</span>);
      resolver(result, <span class="hljs-function">(<span class="hljs-params">err, data</span>) =></span> &#123;
        <span class="hljs-comment">// 我们要清楚NormalModule中的参数就要分析resolver这个hook</span>
        <span class="hljs-keyword">let</span> createdModule = <span class="hljs-keyword">new</span> NormalModule(result);
      &#125;);
    &#125;);
    <span class="hljs-comment">// 这一步找文件和loader的绝对路径 使用的是增强的node中require找文件规则</span>
    <span class="hljs-built_in">this</span>.hooks.resolver.tap(<span class="hljs-string">"NormalModuleFactory"</span>, <span class="hljs-function">() =></span> <span class="hljs-function">(<span class="hljs-params">data, callback</span>) =></span> &#123;
      <span class="hljs-comment">// 参数就这里返回的 主要是返回loader和文件 module的绝对路径和一些其他的构建信息</span>
      <span class="hljs-comment">// 获取解析器 loader的解析器</span>
      <span class="hljs-keyword">const</span> loaderResolver = <span class="hljs-built_in">this</span>.getResolver(<span class="hljs-string">"loader"</span>);
      <span class="hljs-comment">// 文件和模块</span>
      <span class="hljs-keyword">const</span> normalResolver = <span class="hljs-built_in">this</span>.getResolver(<span class="hljs-string">"normal"</span>, data.resolveOptions);
      <span class="hljs-comment">// inline loader的解析</span>
      <span class="hljs-comment">// loader排序 在runLoaders中按照顺序执行post inline normal pre</span>
      callback(<span class="hljs-literal">null</span>, &#123;
        <span class="hljs-comment">// 返回数据给NormalModule</span>
        context,
        <span class="hljs-attr">request</span>: loaders.map(),
        <span class="hljs-attr">dependencies</span>: data.dependencies,
        userRequest,
        <span class="hljs-attr">rawRequest</span>: request,
        loaders,
        resoutce,
        <span class="hljs-attr">parser</span>: <span class="hljs-built_in">this</span>.getParser(<span class="hljs-string">"javascript/auto"</span>),
        <span class="hljs-attr">generator</span>: <span class="hljs-built_in">this</span>.getGenerator(<span class="hljs-string">"javascript/auto"</span>),
      &#125;);
    &#125;);
  &#125;
  <span class="hljs-comment">// create方法创建模块</span>
  <span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 执行factory 这部分的逻辑之前分析过了</span>
    <span class="hljs-keyword">const</span> factory = <span class="hljs-built_in">this</span>.hooks.factory.call(<span class="hljs-literal">null</span>);
    factory(result, <span class="hljs-function">(<span class="hljs-params">err, <span class="hljs-built_in">module</span></span>) =></span> &#123;
      callback(<span class="hljs-literal">null</span>, <span class="hljs-built_in">module</span>);
    &#125;);
  &#125;
  <span class="hljs-comment">// resolverFactory是compiler中</span>
  <span class="hljs-function"><span class="hljs-title">getResolver</span>(<span class="hljs-params">type, resolveOptions</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.resolverFactory.get(type, resolveOptions || &#123;&#125;);
  &#125;
  <span class="hljs-function"><span class="hljs-title">getParser</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.createParser(type, parserOptions);
  &#125;
  <span class="hljs-function"><span class="hljs-title">getGenerator</span>(<span class="hljs-params">type, generatorOptions</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.createGenerator(type, generatorOptions);
  &#125;
  
  <span class="hljs-function"><span class="hljs-title">createParser</span>(<span class="hljs-params">type, parserOptions</span>)</span> &#123;
    <span class="hljs-comment">// 针对不同的模块创建不同的解析器 这些钩子是哪里的</span>
    <span class="hljs-keyword">const</span> parser = <span class="hljs-built_in">this</span>.hooks.createParser.for(type).call(parserOptions);
    <span class="hljs-built_in">this</span>.hooks.parser.for(type).call(parser, parserOptions);
    <span class="hljs-keyword">return</span> parser;
  &#125;
  
  <span class="hljs-function"><span class="hljs-title">createGenerator</span>(<span class="hljs-params">type, generatorOptions</span>)</span> &#123;
    <span class="hljs-keyword">const</span> generator = <span class="hljs-built_in">this</span>.hooks.createGenerator
      .for(type)
      .call(generatorOptions);
    <span class="hljs-built_in">this</span>.hooks.generator.for(type).call(generator, generatorOptions);
    <span class="hljs-keyword">return</span> generator;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3.ResolverFactory</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在compiler中</span>
<span class="hljs-built_in">this</span>.resolverFactory = <span class="hljs-keyword">new</span> ResolverFactory();

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ResolverFactory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Tapable</span> </span>&#123;
   <span class="hljs-comment">// get方法获取不同的loader处理</span>
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">type, resolveOptions</span>)</span> &#123;
    <span class="hljs-keyword">const</span> newResolver = <span class="hljs-built_in">this</span>._create(type, resolveOptions);
    <span class="hljs-keyword">return</span> newResolver;
  &#125;
  <span class="hljs-function"><span class="hljs-title">_create</span>(<span class="hljs-params">type, resolveOptions</span>)</span> &#123;
    <span class="hljs-comment">// type对应 webpackOptionsApply 中 tap 的类型 normal loader</span>
    resolveOptions = <span class="hljs-built_in">this</span>.hooks.resolveOptions.for(type).call(resolveOptions);
    <span class="hljs-comment">// 创建解析器 enhanced-resolve 增强的路径解析包 </span>
    <span class="hljs-comment">// todo 不分析这里</span>
    <span class="hljs-keyword">const</span> resolver = Factory.createResolver(resolveOptions);
    <span class="hljs-keyword">return</span> resolver;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4.WebpackOptionsApply</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在执行webpack的时候会执行这个文件 之前我们 EntryOptionPlugin()就是这里挂载的 还有很多其他的</span>

<span class="hljs-comment">// js的解析器和模板生成的api都是JavascriptModulesPlugin中挂载的</span>
<span class="hljs-keyword">new</span> JavascriptModulesPlugin().apply(compiler); <span class="hljs-comment">// js模块</span>
<span class="hljs-comment">// new JsonModulesPlugin().apply(compiler); // json模块</span>

<span class="hljs-comment">// moduleIds</span>
<span class="hljs-comment">// chunkIds</span>

<span class="hljs-comment">// 为Factory.createResolver提供默认的参数配置  ResolverFactory中触发钩子</span>
<span class="hljs-comment">// compiler.resolverFactory.hooks.resolveOptions.for("normal").tap();</span>
<span class="hljs-comment">// compiler.resolverFactory.hooks.resolveOptions.for("loader").tap();</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">5. JavascriptModulesPlugin</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">JavascriptModulesPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    compiler.hooks.compilation.tap(
      <span class="hljs-string">"JavascriptModulesPlugin"</span>,
      <span class="hljs-function">(<span class="hljs-params">compilation, &#123; normalModuleFactory &#125;</span>) =></span> &#123;
        normalModuleFactory.hooks.createParser
          .for(<span class="hljs-string">"javascript/auto"</span>)
          .tap(<span class="hljs-string">"JavascriptModulesPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">options</span>) =></span> &#123;
            <span class="hljs-comment">// webpack中的Parser使用的acorn 这部分逻辑比较复杂 先跳过</span>
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Parser(options, <span class="hljs-string">"auto"</span>);
          &#125;);

        normalModuleFactory.hooks.createGenerator
          .for(<span class="hljs-string">"javascript/auto"</span>)
          .tap(<span class="hljs-string">"JavascriptModulesPlugin"</span>, <span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> JavascriptGenerator();
          &#125;);
      &#125;
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">6.Compilation</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Compilation</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Tapable</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">_addModuleChain</span>(<span class="hljs-params">context, dependency, onModule, callback</span>)</span> &#123;
    moduleFactory.create(&#123;&#125;, <span class="hljs-function">(<span class="hljs-params">err, <span class="hljs-built_in">module</span></span>) =></span> &#123;
      <span class="hljs-comment">// 如果有依赖项就要处理模块的依赖项</span>
      <span class="hljs-keyword">const</span> afterBuild = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// 处理模块的依赖 那么我们如何找到模块的依赖</span>
        <span class="hljs-comment">// 得到ast语法树遍历找到依赖收集</span>
        <span class="hljs-built_in">this</span>.processModuleDependencies(<span class="hljs-built_in">module</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> callback(<span class="hljs-literal">null</span>, <span class="hljs-built_in">module</span>));
      &#125;;
      <span class="hljs-comment">// 构建模块 调用module的build方法 就是 module.build(</span>
      <span class="hljs-built_in">this</span>.buildModule(<span class="hljs-built_in">module</span>, <span class="hljs-literal">false</span>, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
        afterBuild();
      &#125;);
    &#125;);
  &#125;
  <span class="hljs-comment">// webpack非常恶心的地方就是各种回调 搞死人</span>
  <span class="hljs-function"><span class="hljs-title">buildModule</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, optional, origin, dependencies, thisCallback</span>)</span> &#123;
    <span class="hljs-built_in">module</span>.build(&#123;&#125;, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> thisCallback();
    &#125;);
  &#125;
  <span class="hljs-comment">// 模块build之后会处理依赖 这些依赖是哪里来的? 生成ast之后分析 require和import得到</span>
  <span class="hljs-function"><span class="hljs-title">processModuleDependencies</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, callback</span>)</span> &#123;
    <span class="hljs-built_in">module</span>.dependencies.forEach(<span class="hljs-function">(<span class="hljs-params">item, callback</span>) =></span> &#123;
      <span class="hljs-comment">// 拿到对应的工厂</span>
      <span class="hljs-keyword">const</span> factory = item.factory;
      <span class="hljs-comment">// 工厂创建模块 然后build 递归处理</span>
      factory.crete(&#123;&#125;, <span class="hljs-function">(<span class="hljs-params">err, dependentModule</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.buildModule();
      &#125;);
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">7.总结</h2>
<pre><code class="copyable">在我们执行module.build的时候
    => runLoaders 会先处理loader
    => 然后会使用解析器生成ast做分析
    
我们本次主要是分析 module 中的一些参数
1. loader和文件的怎么找到的 我们使用了enhanced-resolve路径解析包找到资源的绝对路径
2. js parse哪来的? JavascriptModulesPlugin中会tap对应的钩子 而执行webpack函数的时候会apply()
3. 在 ModuleFactory 的 resolver 中我们会返回创建 module 的参数(最要是找路径和构建需要的一些参数)
4. 接下来我们就要分析parse的过程 生成ast 找到依赖项 递归处理

// 简述模块的打包流程
1. 找到模块和loader的绝对路径  normalFacroty 中的 resolver 流程
2. 读取内容经过loader的处理 得到 js 模块 Module中的 runLoaders过程
3. 将js通过parse得到ast语法树
4. 分析ast中的依赖项(require, import) 分析模块的依赖 
5. 递归编译
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            