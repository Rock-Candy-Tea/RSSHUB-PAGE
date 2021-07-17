
---
title: '基于 esbuild 的 universal bundler 设计'
categories: 
 - 编程
 - 掘金
 - 单个收藏夹
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b3fac78d9b14495919307f184b1daf9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 16 Mar 2021 03:54:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b3fac78d9b14495919307f184b1daf9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>由于 Lynx(公司自研跨端框架)编译工具和传统Web编译工具链有较大的差别（如不支持动态 style 和动态 script 基本告别了 bundleless 和 code splitting，模块系统基于 json 而非 js，没有浏览器环境)，且有在 Web 端实时编译(搭建系统)、web 端动态编译(WebIDE)，服务端实时编译(服务端编译下发）、和多版本切换等需求，因此我们需要开发一个即支持在本地也支持在浏览器工作且可以根据业务灵活定制开发的 bundler，即 universal bundler，在开发 universal bundler 的过程中也碰到了一些问题，最后我们基于 esbuild 开发了全新的 universal bundler，解决了我们碰到的大部分问题。</p>
<h2 data-id="heading-1">什么是bundler</h2>
<p>bundler的工作就是将一系列通过模块方式组织的代码将其打包成一个或多个文件，我们常见的bundler包括webpack、rollup、esbuild等。
这里的模块组织形式大部分指的是基于js的模块系统，但也不排除其他方式组织的模块系统(如wasm、小程序的json的usingComponents，css和html的import等），其生成文件也可能不仅仅是一个文件如（code spliting生成的多个js文件，或者生成不同的js、css、html文件等）。
大部分的bundler的核心工作原理都比较类似，但是其会偏重某些功能，如</p>
<ul>
<li>webpack :强调对web开发的支持，尤其是内置了HMR的支持，插件系统比较强大，对各种模块系统兼容性最佳(amd,cjs,umd,esm等，兼容性好的有点过分了，这实际上有利有弊,导致面向webpack编程），有丰富的生态，缺点是产物不够干净，产物不支持生成esm格式， 插件开发上手较难，不太适合库的开发。</li>
<li>rollup: 强调对库开发的支持，基于ESM模块系统，对tree shaking有着良好的支持，产物非常干净，支持多种输出格式，适合做库的开发，插件api比较友好，缺点是对cjs支持需要依赖插件，且支持效果不佳需要较多的hack，不支持HMR，做应用开发时需要依赖各种插件。</li>
<li>esbuild: 强调性能，内置了对css、图片、react、typescript等内置支持，编译速度特别快（是webpack和rollup速度的100倍+),缺点是目前插件系统较为简单，生态不如webpack和rollup成熟。</li>
</ul>
<h2 data-id="heading-2">bundler如何工作</h2>
<p>bundler的实现和大部分的编译器的实现非常类似，也是采用三段式设计，我们可以对比一下</p>
<ul>
<li>llvm: 将各个语言通过编译器前端编译到LLVM IR，然后基于LLVM IR做各种优化，然后基于优化后的LLVM IR根据不同处理器架构生成不同的cpu指令集代码。</li>
<li>bundler: 将各个模块先编译为module graph，然后基于module graph做tree shaking && code spliting &&minify等优化，最后将优化后的module graph根据指定的format生成不同格式的js代码。</li>
</ul>
<h4 data-id="heading-3">LLVM和bundler的对比</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2F6GJWJP" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/6GJWJP" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b3fac78d9b14495919307f184b1daf9~tplv-k3u1fbpfcp-zoom-1.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer">GJWJP</a>
这也使得传统的LLVM的很多编译优化策略实际上也可在bundler中进行，esbuild就是将这一做法推广到极致的例子。
因为rollup的功能和架构较为精简，我们以rollup为例看看一个bundler的是如何工作的。
rollup的bundle过程分为两步rollup和generate，分别对应了bundler前端和bundler后端两个过程。</p>
<ul>
<li>src/main.js</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">
<span class="hljs-keyword">import</span> lib <span class="hljs-keyword">from</span> <span class="hljs-string">'./lib'</span>;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'lib:'</span>, lib);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>src/lib.js</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> answer = <span class="hljs-number">42</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> answer;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先通过生成module graph</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> rollup = <span class="hljs-built_in">require</span>(<span class="hljs-string">'rollup'</span>);
<span class="hljs-keyword">const</span> util = <span class="hljs-built_in">require</span>(<span class="hljs-string">'util'</span>);
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> bundle = <span class="hljs-keyword">await</span> rollup.rollup(&#123;
    <span class="hljs-attr">input</span>: [<span class="hljs-string">'./src/index.js'</span>],
  &#125;);
  <span class="hljs-built_in">console</span>.log(util.inspect(bundle.cache.modules, &#123; <span class="hljs-attr">colors</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">depth</span>: <span class="hljs-literal">null</span> &#125;));
&#125;
main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出内容如下</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">[
&#123;
  <span class="hljs-attr">code</span>: <span class="hljs-string">'const answer = 42;\nexport default answer;\n'</span>,
  <span class="hljs-attr">ast</span>: xxx,
  <span class="hljs-attr">depenencies</span>: [],
  <span class="hljs-attr">id</span>: <span class="hljs-string">'Users/admin/github/neo/examples/rollup-demo/src/lib.js'</span>
  ...
&#125;,
&#123;
  <span class="hljs-attr">ast</span>: xxx,
  <span class="hljs-attr">code</span>: <span class="hljs-string">'import lib from '</span>./lib<span class="hljs-string">';\n\nconsole.log('</span>lib:<span class="hljs-string">', lib);\n'</span>,
  <span class="hljs-attr">dependencies</span>: [ <span class="hljs-string">'/Users/admin/github/neo/examples/rollup-demo/src/lib.js'</span> ]
  <span class="hljs-attr">id</span>: <span class="hljs-string">'/Users/admin/github/neo/examples/rollup-demo/src/index.js'</span>,
  ...
&#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们的生成产物里已经包含的各个模块解析后的ast结构，以及模块之间的依赖关系。
待构建完module graph,rollup就可以继续基于module graph根据用户的配置构建产物了。</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"> <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> bundle.generate(&#123;
    <span class="hljs-attr">format</span>: <span class="hljs-string">'cjs'</span>,
  &#125;);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'result:'</span>, result);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成内容如下</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-built_in">exports</span>: [],
      <span class="hljs-attr">facadeModuleId</span>: <span class="hljs-string">'/Users/admin/github/neo/examples/rollup-demo/src/index.js'</span>,
      <span class="hljs-attr">isDynamicEntry</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">isEntry</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">type</span>: <span class="hljs-string">'chunk'</span>,
      <span class="hljs-attr">code</span>: <span class="hljs-string">"'use strict';\n\nconst answer = 42;\n\nconsole.log('lib:', answer);\n"</span>,
      <span class="hljs-attr">dynamicImports</span>: [],
      <span class="hljs-attr">fileName</span>: <span class="hljs-string">'index.js'</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以一个基本的JavaScript的bundler流程并不复杂，但是其如果要真正的应用于生产环境，支持复杂多样的业务需求，就离不开其强大的插件系统。</p>
<h2 data-id="heading-4">插件系统</h2>
<p>大部分的bundler都提供了插件系统，以支持用户可以自己定制bundler的逻辑。如rollup的插件分为input插件和output插件，input插件对应的是根据输入生成Module Graph的过程，而output插件则对应的是根据Module Graph生成产物的过程。
我们这里主要讨论input插件，其是bundler插件系统的核心，我们这里以esbuild的插件系统为例，来看看我们可以利用插件系统来做什么。
input的核心流程就是生成依赖图，依赖图一个核心的作用就是确定每个模块的源码内容。input插件正提供了如何自定义模块加载源码的方式。
大部分的input 插件系统都提供了两个核心钩子</p>
<ul>
<li>onResolve(rollup 里叫resolveId, webpack里叫factory.hooks.resolver): 根据一个moduleid决定实际的的模块地址</li>
<li>onLoad（rollup里叫loadId，webpack里是loader)：根据模块地址加载模块内容)</li>
</ul>
<p>load这里esbuild和rollup与webpack处理有所差异，esbuild只提供了load这个hooks，你可以在load的hooks里做transform的工作，rollup额外提供了transform的hooks，和load的职能做了显示的区分（但并不阻碍你在load里做transform），而webpack则将transform的工作下放给了loader去完成。
这两个钩子的功能看似虽小，组合起来却能实现很丰富的功能。(插件文档这块，相比之下webpack的文档简直垃圾)
esbuild插件系统相比于rollup和webpack的插件系统，最出色的就是对于virtual module的支持。我们简单看几个例子来展示插件的作用。</p>
<h3 data-id="heading-5">loader</h3>
<p>大家使用webpack最常见的一个需求就是使用各种loader来处理非js的资源，如导入图片css等，我们看一下如何用esbuild的插件来实现一个简单的less-loader。</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> less = (): <span class="hljs-function"><span class="hljs-params">Plugin</span> =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'less'</span>,
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">build</span>)</span> &#123;
      build.onLoad(&#123; <span class="hljs-attr">filter</span>: <span class="hljs-regexp">/.less$/</span> &#125;, <span class="hljs-keyword">async</span> (args) => &#123;
        <span class="hljs-keyword">const</span> content = <span class="hljs-keyword">await</span> fs.promises.readFile(args.path);
        <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> render(content.toString());
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">contents</span>: result.css,
          <span class="hljs-attr">loader</span>: <span class="hljs-string">'css'</span>,
        &#125;;
      &#125;);
    &#125;,
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们只需要在onLoad里通过filter过滤我们想要处理的文件类型，然后读取文件内容并进行自定义的transform，然后将结果返回给esbuild内置的css loader处理即可。是不是十分简单
大部分的loader的功能都可以通过onLoad插件实现。</p>
<h4 data-id="heading-6">sourcemap && cache && error handle</h4>
<p>上面的例子比较简化，作为一个更加成熟的插件还需要考虑transform后sourcemap的映射和自定义缓存来减小load的重复开销以及错误处理，我们来通过svelte的例子来看如何处理sourcemap和cache和错误处理。</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">let</span> sveltePlugin = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'svelte'</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">build</span>)</span> &#123;
    <span class="hljs-keyword">let</span> svelte = <span class="hljs-built_in">require</span>(<span class="hljs-string">'svelte/compiler'</span>)
    <span class="hljs-keyword">let</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
    <span class="hljs-keyword">let</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
    <span class="hljs-keyword">let</span> cache = <span class="hljs-keyword">new</span> LRUCache(); <span class="hljs-comment">// 使用一个LRUcache来避免watch过程中内存一直上涨</span>
    build.onLoad(&#123; <span class="hljs-attr">filter</span>: <span class="hljs-regexp">/.svelte$/</span> &#125;, <span class="hljs-keyword">async</span> (args) => &#123;
      <span class="hljs-keyword">let</span> value = cache.get(args.path); <span class="hljs-comment">// 使用path作为key</span>
      <span class="hljs-keyword">let</span> input = <span class="hljs-keyword">await</span> fs.promises.readFile(args.path, <span class="hljs-string">'utf8'</span>);
      <span class="hljs-keyword">if</span>(value && value.input === input)&#123;
         <span class="hljs-keyword">return</span> value <span class="hljs-comment">// 缓存命中，跳过后续transform逻辑，节省性能</span>
      &#125;
      <span class="hljs-comment">// This converts a message in Svelte's format to esbuild's format</span>
      <span class="hljs-keyword">let</span> convertMessage = <span class="hljs-function">(<span class="hljs-params">&#123; message, start, end &#125;</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> location
        <span class="hljs-keyword">if</span> (start && end) &#123;
          <span class="hljs-keyword">let</span> lineText = source.split(<span class="hljs-regexp">/\r\n|\r|\n/g</span>)[start.line - <span class="hljs-number">1</span>]
          <span class="hljs-keyword">let</span> lineEnd = start.line === end.line ? end.column : lineText.length
          location = &#123;
            <span class="hljs-attr">file</span>: filename,
            <span class="hljs-attr">line</span>: start.line,
            <span class="hljs-attr">column</span>: start.column,
            <span class="hljs-attr">length</span>: lineEnd - start.column,
            lineText,
          &#125;
        &#125;
        <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">text</span>: message, location &#125;
      &#125;

      <span class="hljs-comment">// Load the file from the file system</span>
      <span class="hljs-keyword">let</span> source = <span class="hljs-keyword">await</span> fs.promises.readFile(args.path, <span class="hljs-string">'utf8'</span>)
      <span class="hljs-keyword">let</span> filename = path.relative(process.cwd(), args.path)

      <span class="hljs-comment">// Convert Svelte syntax to JavaScript</span>
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">let</span> &#123; js, warnings &#125; = svelte.compile(source, &#123; filename &#125;)
        <span class="hljs-keyword">let</span> contents = js.code + <span class="hljs-string">`//# sourceMappingURL=`</span> + js.map.toUrl() <span class="hljs-comment">// 返回sourcemap，esbuild会自动将整个链路的sourcemap进行merge</span>
        <span class="hljs-keyword">return</span> &#123; contents, <span class="hljs-attr">warnings</span>: warnings.map(convertMessage) &#125; <span class="hljs-comment">// 将warning和errors上报给esbuild，经esbuild再上报给业务方</span>
      &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">errors</span>: [convertMessage(e)] &#125;
      &#125;
    &#125;)
  &#125;
&#125;

<span class="hljs-built_in">require</span>(<span class="hljs-string">'esbuild'</span>).build(&#123;
  <span class="hljs-attr">entryPoints</span>: [<span class="hljs-string">'app.js'</span>],
  <span class="hljs-attr">bundle</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">outfile</span>: <span class="hljs-string">'out.js'</span>,
  <span class="hljs-attr">plugins</span>: [sveltePlugin],
&#125;).catch(<span class="hljs-function">() =></span> process.exit(<span class="hljs-number">1</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此我们实现了一个比较完整的svelte-loader的功能。</p>
<h3 data-id="heading-7">virtual module</h3>
<p>esbuild插件相比rollup插件一个比较大的改进就是对virtual module的支持,一般bundler需要处理两种形式的模块，一种是路径对应真是的磁盘里的文件路径，另一种路径并不对应真实的文件路径而是需要根据路径形式生成对应的内容即virtual module。
virtual module有着非常丰富的应用场景。</p>
<h4 data-id="heading-8">glob import</h4>
<p>举一个常见的场景，我们开发一个类似<a href="https://link.juejin.cn/?target=https%3A%2F%2Frollupjs.org%2Frepl%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rollupjs.org/repl/" ref="nofollow noopener noreferrer">rollupjs.org/repl/</a> 之类的repl的时候，通常需要将一些代码示例加载到memfs里，然后在浏览器上基于memfs进行构建，但是如果例子涉及的文件很多的话，一个个导入这些文件是很麻烦的，我们可以支持glob形式的导入。
examples/</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">examples
    index.html
    index.tsx
    index.css
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import examples from 'glob:./examples/**/*';
import &#123;vol&#125;  from 'memfs';
vol.fromJson(examples,'/'); //将本地的examples目录挂载到memfs
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类似的功能可以通过<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvitejs.dev%2Fguide%2Ffeatures.html%23glob-import" target="_blank" rel="nofollow noopener noreferrer" title="https://vitejs.dev/guide/features.html#glob-import" ref="nofollow noopener noreferrer">vite</a>或者babel-plugin-macro来实现，我们看看esbuild怎么实现。
实现上面的功能其实非常简单，我们只需要</p>
<ul>
<li>在onResolve里将自定义的path进行解析，然后将元数据通过pluginData和path传递给onLoad，并且自定义一个namespace(namespace的作用是防止正常的file load逻辑去加载返回的路径和给后续的load做filter的过滤）</li>
<li>在onLoad里通过namespace过滤拿到感兴趣的onResolve返回的元数据，根据元数据自定义加载生成数据的逻辑，然后将生成的内容交给esbuild的内置loader处理</li>
</ul>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> globReg = <span class="hljs-regexp">/^glob:/</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> pluginGlob = (): <span class="hljs-function"><span class="hljs-params">Plugin</span> =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'glob'</span>,
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">build</span>)</span> &#123;
      build.onResolve(&#123; <span class="hljs-attr">filter</span>: globReg &#125;, <span class="hljs-function">(<span class="hljs-params">args</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">path</span>: path.resolve(args.resolveDir, args.path.replace(globReg, <span class="hljs-string">''</span>)),
          <span class="hljs-attr">namespace</span>: <span class="hljs-string">'glob'</span>,
          <span class="hljs-attr">pluginData</span>: &#123;
            <span class="hljs-attr">resolveDir</span>: args.resolveDir,
          &#125;,
        &#125;;
      &#125;);
      build.onLoad(&#123; <span class="hljs-attr">filter</span>: <span class="hljs-regexp">/.*/</span>, namespace: <span class="hljs-string">'glob'</span> &#125;, <span class="hljs-keyword">async</span> (args) => &#123;
        <span class="hljs-keyword">const</span> matchPath: string[] = <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
          glob(
            args.path,
            &#123;
              <span class="hljs-attr">cwd</span>: args.pluginData.resolveDir,
            &#125;,
            <span class="hljs-function">(<span class="hljs-params">err, data</span>) =></span> &#123;
              <span class="hljs-keyword">if</span> (err) &#123;
                reject(err);
              &#125; <span class="hljs-keyword">else</span> &#123;
                resolve(data);
              &#125;
            &#125;
          );
        &#125;);
        <span class="hljs-keyword">const</span> result: Record<string, string> = &#123;&#125;;
        <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all(
          matchPath.map(<span class="hljs-keyword">async</span> (x) => &#123;
            <span class="hljs-keyword">const</span> contents = <span class="hljs-keyword">await</span> fs.promises.readFile(x);
            result[path.basename(x)] = contents.toString();
          &#125;)
        );
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">contents</span>: <span class="hljs-built_in">JSON</span>.stringify(result),
          <span class="hljs-attr">loader</span>: <span class="hljs-string">'json'</span>,
        &#125;;
      &#125;);
    &#125;,
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>esbuild基于filter和namespace的过滤是出于性能考虑的，这里的filter的正则是golang的正则，namespace是字符串，因此esbuild可以完全基于filter和namespace进行过滤而避免不必要的陷入到js的调用，最大程度减小golang call js的overhead，但是仍然可以filter设置为/.*/来完全陷入到js，在js里进行过滤，实际的陷入开销实际上还是能够接受的。</p>
</blockquote>
<p>virtual module不仅可以从磁盘里获取内容，也可以直接内存里计算内容，甚至可以把模块导入当函数调用。</p>
<h4 data-id="heading-9">memory virtual module</h4>
<p>这里的env模块，完全是根据环境变量计算出来的</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">let</span> envPlugin = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'env'</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">build</span>)</span> &#123;
    <span class="hljs-comment">// Intercept import paths called "env" so esbuild doesn't attempt</span>
    <span class="hljs-comment">// to map them to a file system location. Tag them with the "env-ns"</span>
    <span class="hljs-comment">// namespace to reserve them for this plugin.</span>
    build.onResolve(&#123; <span class="hljs-attr">filter</span>: <span class="hljs-regexp">/^env$/</span> &#125;, <span class="hljs-function"><span class="hljs-params">args</span> =></span> (&#123;
      <span class="hljs-attr">path</span>: args.path,
      <span class="hljs-attr">namespace</span>: <span class="hljs-string">'env-ns'</span>,
    &#125;))

    <span class="hljs-comment">// Load paths tagged with the "env-ns" namespace and behave as if</span>
    <span class="hljs-comment">// they point to a JSON file containing the environment variables.</span>
    build.onLoad(&#123; <span class="hljs-attr">filter</span>: <span class="hljs-regexp">/.*/</span>, namespace: <span class="hljs-string">'env-ns'</span> &#125;, <span class="hljs-function">() =></span> (&#123;
      <span class="hljs-attr">contents</span>: <span class="hljs-built_in">JSON</span>.stringify(process.env),
      <span class="hljs-attr">loader</span>: <span class="hljs-string">'json'</span>,
    &#125;))
  &#125;,
&#125;

<span class="hljs-comment">// </span>
<span class="hljs-keyword">import</span> &#123; NODE_ENV &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'env'</span> <span class="hljs-comment">// env为虚拟模块，</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">function virtual module</h4>
<p>把模块名当函数使用，完成编译时计算，甚至支持递归函数调用。</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"> build.onResolve(&#123; <span class="hljs-attr">filter</span>: <span class="hljs-regexp">/^fib((\d+))/</span> &#125;, <span class="hljs-function"><span class="hljs-params">args</span> =></span> &#123;
            <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">path</span>: args.path, <span class="hljs-attr">namespace</span>: <span class="hljs-string">'fib'</span> &#125;
   &#125;)
  build.onLoad(&#123; <span class="hljs-attr">filter</span>: <span class="hljs-regexp">/^fib((\d+))/</span>, namespace: <span class="hljs-string">'fib'</span> &#125;, <span class="hljs-function"><span class="hljs-params">args</span> =></span> &#123;
        <span class="hljs-keyword">let</span> match = <span class="hljs-regexp">/^fib((\d+))/</span>.exec(args.path), n = +match[<span class="hljs-number">1</span>]
        <span class="hljs-keyword">let</span> contents = n < <span class="hljs-number">2</span> ? <span class="hljs-string">`export default <span class="hljs-subst">$&#123;n&#125;</span>`</span> : <span class="hljs-string">`
              import n1 from 'fib(<span class="hljs-subst">$&#123;n - <span class="hljs-number">1</span>&#125;</span>) <span class="hljs-subst">$&#123;args.path&#125;</span>'
              import n2 from 'fib(<span class="hljs-subst">$&#123;n - <span class="hljs-number">2</span>&#125;</span>) <span class="hljs-subst">$&#123;args.path&#125;</span>'
              export default n1 + n2`</span>
         <span class="hljs-keyword">return</span> &#123; contents &#125;
  &#125;)
  <span class="hljs-comment">// 使用方式</span>
  <span class="hljs-keyword">import</span> fib5 <span class="hljs-keyword">from</span> <span class="hljs-string">'fib(5)'</span> <span class="hljs-comment">// 直接编译器获取fib5的结果，是不是有c++模板的味道</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">stream import</h4>
<p>不需要下载node_modules就可以进行npm run dev</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">import</span> &#123; Plugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'esbuild'</span>;
<span class="hljs-keyword">import</span> &#123; fetchPkg &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./http'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> UnpkgNamepsace = <span class="hljs-string">'unpkg'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> UnpkgHost = <span class="hljs-string">'https://unpkg.com/'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> pluginUnpkg = (): <span class="hljs-function"><span class="hljs-params">Plugin</span> =></span> &#123;
  <span class="hljs-keyword">const</span> cache: Record<string, &#123; <span class="hljs-attr">url</span>: string; content: string &#125;> = &#123;&#125;;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'unpkg'</span>,
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">build</span>)</span> &#123;
      build.onLoad(&#123; <span class="hljs-attr">namespace</span>: UnpkgNamepsace, <span class="hljs-attr">filter</span>: <span class="hljs-regexp">/.*/</span> &#125;, <span class="hljs-keyword">async</span> (args) => &#123;
        <span class="hljs-keyword">const</span> pathUrl = <span class="hljs-keyword">new</span> URL(args.path, args.pluginData.parentUrl).toString();
        <span class="hljs-keyword">let</span> value = cache[pathUrl];
        <span class="hljs-keyword">if</span> (!value) &#123;
          value = <span class="hljs-keyword">await</span> fetchPkg(pathUrl);
        &#125;
        cache[pathUrl] = value;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">contents</span>: value.content,
          <span class="hljs-attr">pluginData</span>: &#123;
            <span class="hljs-attr">parentUrl</span>: value.url,
          &#125;,
        &#125;;
      &#125;);
      build.onResolve(&#123; <span class="hljs-attr">namespace</span>: UnpkgNamepsace, <span class="hljs-attr">filter</span>: <span class="hljs-regexp">/.*/</span> &#125;, <span class="hljs-keyword">async</span> (args) => &#123;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">namespace</span>: UnpkgNamepsace,
          <span class="hljs-attr">path</span>: args.path,
          <span class="hljs-attr">pluginData</span>: args.pluginData,
        &#125;;
      &#125;);
    &#125;,
  &#125;;
&#125;;

<span class="hljs-comment">// 使用方式</span>
<span class="hljs-keyword">import</span> react <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>; <span class="hljs-comment">//会自动在编译器转换为 import react from 'https://unpkg.com/react'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面几个例子可以看出，esbuild的virtual module设计的非常灵活和强大，当我们使用virtual module时候，实际上我们的整个模块系统结构变成如下的样子
无法复制加载中的内容
针对不同的场景我们可以选择不同的namespace进行组合</p>
<ul>
<li>本地开发： 完全走本地file加载，即都走file namespace</li>
<li>本地开发免安装node_modules: 即类似deno和snowpack的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.snowpack.dev%2Fposts%2F2021-01-13-snowpack-3-0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.snowpack.dev/posts/2021-01-13-snowpack-3-0" ref="nofollow noopener noreferrer">streaming import</a>的场景，可以通过业务文件走file namespace,node_modules文件走unpkg namespace,比较适合超大型monorepo项目开发一个项目需要安装所有的node_modules过慢的场景。</li>
<li>web端实时编译场景(性能和网络问题)：即第三方库是固定的，业务代码可能变化，则本地file和node_modules都走memfs。</li>
<li>web端动态编译:即内网webide场景，此时第三方库和业务代码都不固定，则本地file走memfs，node_modules走unpkg动态拉取</li>
</ul>
<p>我们发现基于virtual module涉及的universal bundler非常灵活，能够灵活应对各种业务场景，而且各个场景之间的开销互不影响。</p>
<h2 data-id="heading-12">universal bundler</h2>
<p>大部分的bundler都是默认运行在浏览器上，所以构造一个universal bundler最大的难点还是在于让bundler运行在浏览器上。
区别于我们本地的bundler，浏览器上的bundler存在着诸多限制，我们下面看看如果将一个bundler移植到浏览器上需要处理哪些问题。</p>
<h3 data-id="heading-13">rollup</h3>
<p>首先我们需要选取一个合适的bundler来帮我们完成bundle的工作，rollup就是一个非常优秀的bundler，rollup有着很多非常优良的性质</p>
<ul>
<li>treeshaking支持非常好，也支持cjs的tree shaking</li>
<li>丰富的插件hooks，具有非常灵活定制的能力</li>
<li>支持运行在浏览器上</li>
<li>支持多种输出格式(esm,cjs,umd,systemjs)</li>
</ul>
<p>正式因为上述优良的特性，所以很多最新的bundler|bundleness工具都是基于rollup或者兼容rollup的插件体系，典型的就是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvitejs.dev%2Fguide%2Fapi-plugin.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vitejs.dev/guide/api-plugin.html" ref="nofollow noopener noreferrer">vite</a> 和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpreactjs%2Fwmr%2Fblob%2Fmain%2Fpackages%2Fwmr%2FREADME.md%23configuration-and-plugins" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/preactjs/wmr/blob/main/packages/wmr/README.md#configuration-and-plugins" ref="nofollow noopener noreferrer">wmr</a>, 不得不说给rollup写插件比起给webpack写插件要舒服很多。
我们早期的universal bundler实际上就是基于rollup开发的，但是使用rollup过程中碰到了不少问题，总结如下</p>
<h4 data-id="heading-14">对CommonJS的兼容问题</h4>
<p>但凡在实际的业务中使用rollup进行bundle的同学，绕不开的一个插件就是rollup-plugin-commonjs，因为rollup原生只支持ESM模块的bundle，因此如果实际业务中需要对commonjs进行bundle，第一步就是需要将CJS转换成ESM，不幸的是，Commonjs和ES Module的interop问题是个非常棘手的问题（搜一搜babel、rollup、typescript等工具下关于interop的issue <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsokra.github.io%2Finterop-test%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://sokra.github.io/interop-test/" ref="nofollow noopener noreferrer">sokra.github.io/interop-tes…</a> ，其两者语义上存在着天然的鸿沟，将ESM转换成Commonjs一般问题不太大（小心避开default导出问题），但是将CJS转换为ESM则存在着更多的问题。
rollup-plugin-commonjs虽然在cjs2esm上下了很多功夫，但是实际仍然有非常多的edge case,实际上rollup也正在重写该核心模块 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frollup%2Fplugins%2Fpull%2F658%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rollup/plugins/pull/658%E3%80%82" ref="nofollow noopener noreferrer">github.com/rollup/plug…</a> 一些典型的问题如下</p>
<h5 data-id="heading-15">循环引用问题</h5>
<p>由于commonjs的导出模块并非是live binding的，所以导致一旦出现了commonjs的循环引用，则将其转换成esm就会出问题</p>
<h5 data-id="heading-16">动态require的hoist问题</h5>
<p>同步的动态require几乎无法转换为esm，如果将其转换为top-level的import，根据import的语义，bundler需要将同步require的内容进行hoist，但是这与同步require相违背，因此动态require也很难处理</p>
<h5 data-id="heading-17">Hybrid CJS和ESM</h5>
<p>因为在一个模块里混用ESM和CJS的语义并没有一套标准的规范规定，虽然webpack支持在一个模块里混用CJS和ESM(downlevel to webpack runtime),但是rollup放弃了对该行为的支持（最新版可以条件开启，我没试过效果咋样）</p>
<h5 data-id="heading-18">性能问题</h5>
<p>正是因为cjs2esm的复杂性，导致该转换算法十分复杂，导致一旦业务里包含了很多cjs的模块，rollup其编译性能就会急剧下降，这在编译一些库的时候可能不是大问题，但是用于大型业务的开发，其编译速度难以接受。</p>
<h5 data-id="heading-19">浏览器上cjs转esm</h5>
<p>另一方面虽然rollup可以较为轻松的移植到到memfs上，但是rollup-plugin-commonjs是很难移植到web上的，所以我们早期基于rollup做web bundler只能借助于类似skypack之类的在线cjs2esm的服务来完成上述转换，但是大部分这类服务其后端都是通过rollup-plugin-commonjs来实现的，因此rollup原有的那些问题并没有摆脱，并且还有额外的网络开销，且难以处理非node_modules里cjs模块的处理。
幸运的是esbuild采取的是和rollup不同的方案，其对cjs的兼容采取了类似node的module wrapper,引入了一个非常小的运行时，来支持cjs(webpack实际上也是采用了运行时的方案来兼容cjs，但是他的runtime不够简洁。。。)。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a88b979d70834271895c918b4bd146b0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
其通过彻底放弃对cjs tree shaking的支持来更好的兼容cjs，并且同时可以在不引入插件的情况下，直接使得web bundler支持cjs。</p>
<h4 data-id="heading-20">virutual module的支持</h4>
<p>rollup的virtual module的支持比较hack,依赖路径前面拼上一个'\0'，对路径有入侵性，且对一些ffi的场景不太友好(c++ string把'\0'视为终结符)，当处理较为复杂的virtual module场景下，'\0'这种路径非常容易处理出问题。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b429d21be2d14afbbc0d3469beba9ed0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">filesystem</h3>
<p>本地的bundler都是访问的本地文件系统，但是在browser是不存在本地文件系统的，因此如何访问文件呢，一般可以通过将bundler实现为与具体的fs无关来实现,所有的文件访问通过可配置的fs来进行访问。<a href="https://link.juejin.cn/?target=https%3A%2F%2Frollupjs.org%2Frepl%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rollupjs.org/repl/" ref="nofollow noopener noreferrer">rollupjs.org/repl/</a> 即是采用此方式。因此我们只需要将模块的加载逻辑从fs里替换为浏览器上的memfs即可，onLoad这个hooks正可以用于替换文件的读取逻辑。</p>
<h3 data-id="heading-22">node module resolution</h3>
<p>当我们将文件访问切换到memfs时，一个接踵而至的问题就是如何获取一个require和import的id对应的实际路径格式,node里将一个id映射为一个真实文件地址的算法就是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fapi%2Fmodules.html%23modules_all_together" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/api/modules.html#modules_all_together" ref="nofollow noopener noreferrer">module resolution</a>, 该算法实现较为复杂需要考虑如下情况，详细算法见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftech.bytedance.net%2Farticles%2F6935059588156751880" target="_blank" rel="nofollow noopener noreferrer" title="https://tech.bytedance.net/articles/6935059588156751880" ref="nofollow noopener noreferrer">tech.bytedance.net/articles/69…</a></p>
<ul>
<li>file|index|目录三种情形</li>
<li>js、json、addon多文件后缀</li>
<li>esm和cjs loader区别</li>
<li>main field处理</li>
<li>conditional exports处理</li>
<li>exports subpath</li>
<li>NODE_PATH处理</li>
<li>递归向上查找</li>
<li>symlink的处理</li>
</ul>
<p>除了node module resolution本身的复杂，我们可能还需要考虑main module filed fallback、alias支持、ts等其他后缀支持等webpack额外支持但在社区比较流行的功能，yarn|pnpm|npm等包管理工具兼容等问题。自己从头实现这一套算法成本较大，且node 的module resolution算法一直在更新，webpack的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Fenhanced-resolve" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/enhanced-resolve" ref="nofollow noopener noreferrer">enhanced-resolve</a> 模块基本上实现了上述功能，并且支持自定义fs，可以很方便的将其移植到memfs上。</p>
<blockquote>
<p>我觉得这里node的算法着实有点over engineering而且效率低下（一堆fallback逻辑有不小的io开销），而且这也导致了万恶之源hoist盛行的主要原因，也许bare import配合import map，或者deno|golang这种显示路径更好一些。</p>
</blockquote>
<h3 data-id="heading-23">main field</h3>
<p>main field也是个较为复杂的问题，主要在于没有一套统一的规范，以及社区的库并不完全遵守规范，其主要涉及包的分发问题，除了main字段是nodejs官方支持的，module、browser、browser等字段各个bundler以及第三方社区库并未达成一致意见如</p>
<ul>
<li>cjs和esm，esnext和es5，node和browser，dev和prod的入口该怎么配置</li>
<li>module| main 里的代码应该是es5还是esnext的（决定了node_module里的代码是否需要走transformer）</li>
<li>module里的代码是应该指向browser的实现还是指向node的实现（决定了node bundler</li>
</ul>
<p>和browser bundler情况下main和module的优先级问题）</p>
<ul>
<li>node和browser差异的代码如何分发处理等等</li>
</ul>
<h3 data-id="heading-24">unpkg</h3>
<p>接下来我们就需要处理node_modules的模块了，此时有两种方式，一种是将node_modules全量挂载到memfs里,然后使用enhanced-resolve去memfs里加载对应的模块，另一种方式则是借助于unpkg，将node_modules的id转换为unpkg的请求。这两种方式都有其适用场景
第一种适合第三方模块数目比较固定（如果不固定，memfs必然无法承载无穷的node_modules模块），而且memfs的访问速度比网络请求访问要快的多，因此非常适合搭建系统的实现。
第二种则适用第三方模块数目不固定，对编译速度没有明显的实时要求，这种就比较适合类似codesandbox这种webide场景，业务可以自主的选择其想要的npm模块。</p>
<h3 data-id="heading-25">shim 与 polyfill</h3>
<p>web bundler碰到的另一个问题就是大部分的社区模块都是围绕node开发的，其会大量依赖node的原生api，但是浏览器上并不会支持这些api，因此直接将这些模块跑在浏览器上就会出问题。此时分为两种情况</p>
<ul>
<li>一种是这些模块依赖的实际就是些node的utily api例如utils、path等，这些模块实际上并不依赖node runtime,此时我们实际上是可以在浏览器上模拟这些api的，browserify实际上就是为了解决这种场景的，其提供了大量的node api在浏览器上的polyfill如path-browserify,stream-browserify等等，</li>
<li>另一种是浏览器和node的逻辑分开处理，虽然node的代码不需要在浏览器上执行，但是不期望node的实现一方面增大浏览器bundle包的体积和导致报错，此时我们需要node相关的模块进行external处理即可。</li>
</ul>
<blockquote>
<p>一个小技巧，大部分的bundler配置external可能会比较麻烦或者没办法修改bundler的配置，我们只需要将require包裹在eval里，大部分的bundler都会跳过require模块的打包。如eval('require')('os')</p>
</blockquote>
<h4 data-id="heading-26">polyfill与环境嗅探，矛与盾之争</h4>
<p>polyfill和环境嗅探是个争锋相对的功能，一方面polyfill尽可能抹平node和browser差异，另一方面环境嗅探想尽可能从差异里区分浏览器和node环境，如果同时用了这俩功能，就需要各种hack处理了</p>
<h3 data-id="heading-27">webassembly</h3>
<p>我们业务中依赖了c++的模块，在本地环境下可以将c++编译为静态库通过ffi进行调用，但是在浏览器上则需要将其编译为webassembly才能运行，但是大部分的wasm的大小都不小，esbuild的wasm有8M左右，我们自己的静态库编译出来的wasm也有3M左右，这对整体的包大小影响较大，因此可以借鉴code split的方案，将wasm进行拆分，将首次访问可能用到的代码拆为hot code,不太可能用到的拆为cold code, 这样就可以降低首次加载的包的体积。</p>
<h3 data-id="heading-28">我们可以在哪里使用esbuild</h3>
<p>esbuild有三个垂直的功能，既可以组合使用也可以完全独立使用</p>
<ul>
<li>minifier</li>
<li>transformer</li>
<li>bundler</li>
</ul>
<h4 data-id="heading-29">更高效的register和minify工具</h4>
<p>利用esbuild的transform功能，使用esbuild-register替换单元测试框架ts-node的register，大幅提升速度：见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Faelbore%2Fesbuild-jest" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/aelbore/esbuild-jest" ref="nofollow noopener noreferrer">github.com/aelbore/esb…</a> ,不过ts-node现在已经支持自定义register了，可以直接将register替换为esbuild-register即可，esbuild的minify性能也是远远超过terser（100倍以上）</p>
<h4 data-id="heading-30">更高效的prebundle工具</h4>
<p>在一些bundleness的场景，虽然不对业务代码进行bundle，但是为了一方面防止第三方库的waterfall和cjs的兼容问题，通常需要对第三方库进行prebundle，esbuild相比rollup是个更好的prebundle工具，实际上vite的最新版已经将prebundle功能从rollup替换为了esbuild。</p>
<h4 data-id="heading-31">更好的线上cjs2esm服务</h4>
<p>使用esbuild搭建esm cdn服务：esm.sh就是如此</p>
<h4 data-id="heading-32">node bundler</h4>
<p>相比于前端社区，node社区似乎很少使用bundle的方案，一方面是因为node服务里可能使用fs以及addon等对bundle不友好的操作，另一方面是大部分的bundler工具都是为了前端设计的，导致应用于node领域需要额外的配置。但是对node的应用或者服务进行bundle有着非常大的好处</p>
<ul>
<li>减小了使用方的node_modules体积和加快安装速度，相比将node应用的一堆依赖一起安装到业务的node_modules里，只安装bundle的代码大大减小了业务的安装体积和加快了安装速度，pnpm和yarn就是使用esbuild将所有依赖bundle实现零依赖的正面典型<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftwitter.com%2Fpnpmjs%2Fstatus%2F1353848140902903810%3Fs%3D21" target="_blank" rel="nofollow noopener noreferrer" title="https://twitter.com/pnpmjs/status/1353848140902903810?s=21" ref="nofollow noopener noreferrer">twitter.com/pnpmjs/stat…</a></li>
<li>提高了冷启动的速度，因为bundle后的代码一方面通过tree shaking减小了引起实际需要parse的js代码大小（js的parse开销在大型应用的冷启动速度上占据了不小的比重，尤其是对冷启动速度敏感的应用），另一方面避免了文件io，这两方面都同时大大减小了应用冷启动的速度，非常适合一些对冷启动敏感的场景，如serverless</li>
<li>避免上游的semver语义破坏，虽然semver是一套社区规范，但是这实际上对代码要求非常严格，当引入了较多的第三方库时，很难保证上游依赖不会破坏semver语义，因此bundle代码可以完全避免上游依赖出现bug导致应用出现bug，这对安全性要求极高的应用（如编译器）至关重要。</li>
</ul>
<p>因此笔者十分鼓励大家对node应用进行bundle，而esbuild对node的bundle提供了开箱即用的支持。</p>
<h4 data-id="heading-33">tsc transformer替代品</h4>
<p>tsc即使支持了增量编译，其性能也极其堪忧，我们可以通过esbuild来代替tsc来编译ts的代码。（esbuid不支持ts的type check也不准备支持），但是如果业务的dev阶段不强依赖type checker，完全可以dev阶段用esbuild替代tsc，如果对typechecker有强要求，可以关注swc,swc正在用rust重写tsc的type checker部分，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fswc-project%2Fswc%2Fissues%2F571" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/swc-project/swc/issues/571" ref="nofollow noopener noreferrer">github.com/swc-project…</a></p>
<h4 data-id="heading-34">monorepo与monotools</h4>
<p>esbuild是少有的对库开发和应用开发支持都比较良好的工具(webpack库支持不佳，rollup应用开发支持不佳)，这意味着你完全可以通过esbuild统一你项目的构建工具。
esbuild原生支持react的开发，bundle速度极其快，在没有做任何bundleness之类的优化的情况下，一次的完整的bundle只需要80ms（包含了react，monaco-editor，emotion，mobx等众多库的情况下）
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb93dcf6cecb47b4964834d1aef96cbd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
这带来了另一个好处就是你的monorepo里很方便的解决公共包的编译问题。你只需要将esbuild的main field配置为['source','module','main'],然后在你公共库里将source指向你的源码入口，esbuild会首先尝试去编译你公共库的源码，esbuild的编译速度是如此之快，根本不会因为公共库的编译影响你的整体bundle速度😁。我只能说TSC不太适合用来跑编译，too slow && too complex。</p>
<h2 data-id="heading-35">esbuild存在的一些问题</h2>
<h3 data-id="heading-36">调试麻烦</h3>
<p>esbuild的核心代码是用golang编写，用户使用的直接是编译出来的binary代码和一堆js的胶水代码，binary代码几乎没法断点调试(lldb|gdb调试），每次调试esbuild的代码，需要拉下代码重新编译调试，调试要求较高，难度较大</p>
<h3 data-id="heading-37">只支持target到es6</h3>
<p>esbuild的transformer目前只支持target到es6,对于dev阶段影响较小，但目前国内大部分都仍然需要考虑es5场景，因此并不能将esbuild的产物作为最终产物，通常需要配合babel | tsc | swc做es6到es5的转换</p>
<h3 data-id="heading-38">golang wasm的性能相比native有较大的损耗，且wasm包体积较大，</h3>
<p>目前golang编译出的wasm性能并不是很好（相比于native有3-5倍的性能衰减），并且go编译出来wasm包体积较大(8M+),不太适合一些对包体积敏感的场景</p>
<h2 data-id="heading-39">插件api较为精简</h2>
<p>相比于webpack和rollup庞大的插件api支持，esbuild仅支持了onLoad和onResolve两个插件钩子，虽然基于此能完成很多工作，但是仍然较为匮乏，如code spliting后的chunk的后处理都不支持</p>
<p><code>欢迎关注「 字节前端 ByteFE 」简历投递联系邮箱「 tech@bytedance.com 」</code></p></div>  
</div>
            