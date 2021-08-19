
---
title: 'webpack的watch模式下因 loader 缓存导致的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05fde2d33e4c4656af9aa75b1fd32fab~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 01:24:56 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05fde2d33e4c4656af9aa75b1fd32fab~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05fde2d33e4c4656af9aa75b1fd32fab~tplv-k3u1fbpfcp-watermark.image" alt="webpack_logo.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">问题概述</h3>
<p>一个简单的场景，需要记录项目中使用到的的页面或者组件资源，其中一个方法是将逻辑写在loader中，这样资源经过loader编译的时候可以统计到。但是在watch模式下会产生一个问题，修改完其中一个文件后，这个文件重新走loader，其他没有修改的文件不会再走loader，导致本次编译后统计的资源丢失。</p>
<h3 data-id="heading-1">场景复现</h3>
<blockquote>
<p>demo地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkotori2000%2Fwebpack-watch-loader-cache" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/kotori2000/webpack-watch-loader-cache" ref="nofollow noopener noreferrer">github.com/kotori2000/…</a></p>
</blockquote>
<p>例如 demo 中的部分 webpack 配置，使用了自定义的 TestWebpackPlugin 和 _babel-loader。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> TestWebpackPlugin()
  ],
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
        use: [<span class="hljs-string">'_babel-loader'</span>]
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外配置了loader的解析路径，能访问到自定义的loader</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">resolveLoader: &#123;
  <span class="hljs-attr">modules</span>: [<span class="hljs-string">'node_modules'</span>, path.resolve(__dirname, <span class="hljs-string">'loaders'</span>)]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv4.webpack.docschina.org%2Fapi%2Fcompiler-hooks%2F%23thiscompilation" target="_blank" rel="nofollow noopener noreferrer" title="https://v4.webpack.docschina.org/api/compiler-hooks/#thiscompilation" ref="nofollow noopener noreferrer">thisCompilation</a>钩子中先初始化compilation._testObj_对象；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// plugins/TestWebpackPlugin.js</span>
<span class="hljs-keyword">let</span> testObj
<span class="hljs-keyword">if</span> (!compilation.__testObj__) &#123;
  testObj = compilation.__testObj__ = &#123;
    <span class="hljs-attr">modulesMap</span>: &#123;&#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后 loader 阶段执行 _babel-loader.js 逻辑，将上阶段初始化的modulesMap赋值给常量，loader 解析的路径加到modulesMap 对象中，loader 依次处理三个文件;</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// loaders/_babel-loader.js</span>
<span class="hljs-keyword">const</span> testObj = <span class="hljs-built_in">this</span>._compilation.__testObj__
  
<span class="hljs-keyword">if</span> (!testObj) &#123;
  <span class="hljs-keyword">return</span> source
&#125;

<span class="hljs-keyword">const</span> modulesMap = testObj.modulesMap
<span class="hljs-keyword">if</span> (!modulesMap[<span class="hljs-built_in">this</span>.resourcePath]) &#123;
  modulesMap[<span class="hljs-built_in">this</span>.resourcePath] = <span class="hljs-built_in">this</span>.resourcePath
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>this.resourcePath资源文件的路径。</p>
</blockquote>
<p>处理完后会进入到 emit 钩子(这个时候已经 modulesMap 已经有了三个值)：键值都是对应的文件路径</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e261730a92644bb9a413215463b161a2~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候改变文件内容触发下一次编译（我这里修改b.js文件）：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/599aee59dd824a6aa4e91a2f12e01ef3~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer">
=>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02af0bc50b0a421486c92a5de0c85e70~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>只有修改的文件会再次经过_babel-loader.js的处理，再看此时modulesMap：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0e47a698c934fdf8f7eb4d0551f00bc~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>只收集到修改过的b.js的路径。</p>
<h3 data-id="heading-2">问题造成原因</h3>
<p>loader默认是开启缓存功能的，而每次触发编译的过程中，都会生成一个 compilation 对象，实际上 compilation 对象是每单独一次编译的流程和数据中心，从编译开始、文件输出到最后的日志输出，都关联在 compilation 上。而控制是否需要编译（是否走缓存）的代码在webpack/lib/Compilation.js的addModule方法中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack/lib/Compilation.js的addModule</span>
<span class="hljs-function"><span class="hljs-title">addModule</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, cacheGroup</span>)</span> &#123;
    <span class="hljs-keyword">const</span> identifier = <span class="hljs-built_in">module</span>.identifier();
    <span class="hljs-keyword">const</span> alreadyAddedModule = <span class="hljs-built_in">this</span>._modules.get(identifier);
    <span class="hljs-keyword">if</span> (alreadyAddedModule) &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">module</span>: alreadyAddedModule,
        <span class="hljs-attr">issuer</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">build</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">dependencies</span>: <span class="hljs-literal">false</span>
      &#125;;
    &#125;
    <span class="hljs-keyword">const</span> cacheName = (cacheGroup || <span class="hljs-string">"m"</span>) + identifier;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.cache && <span class="hljs-built_in">this</span>.cache[cacheName]) &#123;
      <span class="hljs-keyword">const</span> cacheModule = <span class="hljs-built_in">this</span>.cache[cacheName];
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> cacheModule.updateCacheModule === <span class="hljs-string">"function"</span>) &#123;
        cacheModule.updateCacheModule(<span class="hljs-built_in">module</span>);
      &#125;
      <span class="hljs-keyword">let</span> rebuild = <span class="hljs-literal">true</span>;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.fileTimestamps && <span class="hljs-built_in">this</span>.contextTimestamps) &#123;
        rebuild = cacheModule.needRebuild(
          <span class="hljs-built_in">this</span>.fileTimestamps,
          <span class="hljs-built_in">this</span>.contextTimestamps
        );
      &#125;
      <span class="hljs-keyword">if</span> (!rebuild) &#123;
        cacheModule.disconnect();
        <span class="hljs-built_in">this</span>._modules.set(identifier, cacheModule);
        <span class="hljs-built_in">this</span>.modules.push(cacheModule);
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> err <span class="hljs-keyword">of</span> cacheModule.errors) &#123;
          <span class="hljs-built_in">this</span>.errors.push(err);
        &#125;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> err <span class="hljs-keyword">of</span> cacheModule.warnings) &#123;
          <span class="hljs-built_in">this</span>.warnings.push(err);
        &#125;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">module</span>: cacheModule,
          <span class="hljs-attr">issuer</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">build</span>: <span class="hljs-literal">false</span>,
          <span class="hljs-attr">dependencies</span>: <span class="hljs-literal">true</span>
        &#125;;
      &#125;
      cacheModule.unbuild();
      <span class="hljs-built_in">module</span> = cacheModule;
    &#125;
    <span class="hljs-built_in">this</span>._modules.set(identifier, <span class="hljs-built_in">module</span>);
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.cache) &#123;
      <span class="hljs-built_in">this</span>.cache[cacheName] = <span class="hljs-built_in">module</span>;
    &#125;
    <span class="hljs-built_in">this</span>.modules.push(<span class="hljs-built_in">module</span>);
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">module</span>: <span class="hljs-built_in">module</span>,
      <span class="hljs-attr">issuer</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">build</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">dependencies</span>: <span class="hljs-literal">true</span>
    &#125;;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有一个needrebuild 判断是否需要重新编译（this.fileTimestamps 、this.contextTimestamps：首次或前一次编译存储的文件最后变更记录）。</p>
<h3 data-id="heading-3">解决办法：</h3>
<h5 data-id="heading-4">（1）强制让loader中不使用缓存,简单粗暴</h5>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22c33e11388d4872833654d39f9ce4e5~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样不管怎么修改所有的js文件都会经过_babel-laoder再次进行编译。
再次场景复现进行断点调试，能看到只修改b.js文件后index.js,a.js和b.js也都再次经过_babel-laoder的处理。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c3ce5e71b7f49b48edb2131e2640592~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">（2）重写 addModule 方法</h4>
<p>在 _babel-laoder 中用 this._module.buildInfo 保存编译过的文件（各个模块各自保存编译过的标记，当走缓存时能在plugin中读取到该标记），TestWebpackPlugin中重写 addModule 方法，保留原有逻辑判断的同时加入判断需要走缓存时（不需要重新编译的时候），手动加入缓存文件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">const</span> buildInfo = <span class="hljs-built_in">this</span>._module.buildInfo
buildInfo.modulesMap = buildInfo.modulesMap || &#123;&#125;
buildInfo.modulesMap[<span class="hljs-built_in">this</span>.resourcePath] = testObj.modulesMap[<span class="hljs-built_in">this</span>.resourcePath] = <span class="hljs-built_in">this</span>.resourcePath

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>this._module一种 hack 写法。用于访问当前加载的 Module 对象。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> rawAddModule = compilation.addModule
      compilation.addModule = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> addModuleResult = rawAddModule.apply(compilation, args)
        <span class="hljs-keyword">if</span> (!addModuleResult.build && addModuleResult.issuer) &#123;
          <span class="hljs-keyword">const</span> buildInfo = addModuleResult.module.buildInfo
          <span class="hljs-keyword">if</span> (buildInfo.modulesMap) &#123;
            <span class="hljs-built_in">Object</span>.assign(testObj.modulesMap, buildInfo.modulesMap)
          &#125;
        &#125;
        <span class="hljs-keyword">return</span> addModuleResult
      &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样再进行断点调试，首次处理三个文件依次经过处理，能看到buildInfo将处理过的文件路径进行了缓存（我这里文件路径过长所以没能展示出具体文件名，依次是index.js、a.js、b.js）：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/355738367a5141aeaf17621af3b6e6e0~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当修改b.js文件后，index.js和a.js文件因为走缓存会经过这步逻辑将module中保存的标记取出。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb2690d3f4214537a9cb83954c15b773~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f0c222add3747dab5bb15a128cfdd96~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而b.js则还是经过_babel-loader.js的处理最后到emit钩子中成功输出所有模块：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf3fc9e6f8a5454e98998d740f2d6edf~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">总结</h3>
<p>只是在这个 demo 场景下，loader 中还加入了其他的处理逻辑，比如收集 modulesMap 等，所以才导致的失效。
根据实际情况，如果收集 modulesMap 的过程与新增或删除依赖无关，其实可以把modulesMap直接挂载到 compiler 对象上，也能避免这种情况。</p></div>  
</div>
            