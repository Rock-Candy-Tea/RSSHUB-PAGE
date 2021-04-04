
---
title: '简单实现一个esbuild插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3963'
author: 掘金
comments: false
date: Sat, 03 Apr 2021 21:46:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=3963'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>首发于naeco的<a href="http://www.naeco.top/2021/03/21/esbuild-plugin/" target="_blank" rel="nofollow noopener noreferrer">博客</a></p>
</blockquote>
<p>​<a href="https://esbuild.github.io/" target="_blank" rel="nofollow noopener noreferrer">esbuild</a>是由<code>Go</code>编写的构建打包工具，对标的是<code>webpack</code>、<code>rollup</code>和<code>parcel</code>等工具，在静态语言的加持下，<code>esbuild</code>的构建速度可以是传统<code>js</code>构建工具的10-100倍，就好像跑车和自行车的区别。相对于<code>webpack</code>等工具，<code>esbuild</code>相对比较纯粹，配置也很简单，换句话说，支持的功能还不是很全面，目前还不适合用于大型的项目工程。但由于性能上的优势，<code>vite</code>和<code>snowpack</code>等<code>esm</code>构建工具都采用了esbuild作为底层支持。</p>
<h3 data-id="heading-0">esbuild插件</h3>
<p>​<code>esbuild</code>之前被人所诟病的一点就是缺少插件的支持，很多功能都没办法实现，好在在<code>0.8.x</code>版本后，官方终于推出了插件的支持，目前依然是实验性的一个特性，不排除未来会对API作出改变。但这不影响我们开发插件，因为<code>esbuild</code>的插件API非常简单，即使会有变动，后续迁移的成本也不会非常高。</p>
<p>​<code>esbuild</code> 插件就是一个对象，里面有<code>name</code>和<code>setup</code>两个属性，<code>name</code>是插件的名称，<code>setup</code>是一个函数，构建的时候会执行，插件的逻辑也封装在其中。以下是一个简单的<code>esbuild</code>插件示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> envPlugin = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'env'</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">build</span>)</span> &#123;
     <span class="hljs-comment">// 文件解析时触发</span>
    <span class="hljs-comment">// 将插件作用域限定于env文件，并为其标识命名空间"env-ns"</span>
    build.onResolve(&#123; <span class="hljs-attr">filter</span>: <span class="hljs-regexp">/^env$/</span> &#125;, <span class="hljs-function"><span class="hljs-params">args</span> =></span> (&#123;
      <span class="hljs-attr">path</span>: args.path,
      <span class="hljs-attr">namespace</span>: <span class="hljs-string">'env-ns'</span>,
    &#125;))

    <span class="hljs-comment">// 加载文件时触发</span>
    <span class="hljs-comment">// 只有命名空间为"env-ns"的文件才会被处理</span>
    <span class="hljs-comment">// 将process.env对象反序列化为字符串并交由json-loader处理</span>
    build.onLoad(&#123; <span class="hljs-attr">filter</span>: <span class="hljs-regexp">/.*/</span>, namespace: <span class="hljs-string">'env-ns'</span> &#125;, <span class="hljs-function">() =></span> (&#123;
      <span class="hljs-attr">contents</span>: <span class="hljs-built_in">JSON</span>.stringify(process.env),
      <span class="hljs-attr">loader</span>: <span class="hljs-string">'json'</span>,
    &#125;))
  &#125;,
&#125;

<span class="hljs-built_in">require</span>(<span class="hljs-string">'esbuild'</span>).build(&#123;
  <span class="hljs-attr">entryPoints</span>: [<span class="hljs-string">'app.js'</span>],
  <span class="hljs-attr">bundle</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">outfile</span>: <span class="hljs-string">'out.js'</span>,
  <span class="hljs-comment">// 应用插件</span>
  <span class="hljs-attr">plugins</span>: [envPlugin],
&#125;).catch(<span class="hljs-function">() =></span> process.exit(<span class="hljs-number">1</span>))

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 应用了env插件后，构建时将会被替换成process.env对象</span>
<span class="hljs-keyword">import</span> &#123; PATH &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'env'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`PATH is <span class="hljs-subst">$&#123;PATH&#125;</span>`</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​可以看到，<code>esbuild</code>插件实现还是非常简单的，只需要在<code>setup</code>函数中注册两个钩子函数，然后再添加相对应的代码逻辑即可，关于<code>esbuild</code>插件API的介绍可以查询官方的<a href="https://esbuild.github.io/plugins/" target="_blank" rel="nofollow noopener noreferrer">文档</a>。</p>
<h3 data-id="heading-1">esbuild-plugin-replace实现</h3>
<p>​先把成品放出来，<a href="https://github.com/naecoo/esbuild-plugin-replace" target="_blank" rel="nofollow noopener noreferrer">esbuild-plugin-replace</a>, 欢迎提issue和pr，顺手点个star就更好了😎。<code>esbuild-plugin-replace</code>这个插件作用是在构建时替换代码里的字符，主要用于动态更新代码的一些变量，比如版本号，构建时间，构建的<code>git</code>信息等。</p>
<p>​由于代码数不多，只有62行，所以下面直接将全部代码贴上来:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">const</span> MagicString = <span class="hljs-built_in">require</span>(<span class="hljs-string">'magic-string'</span>);

<span class="hljs-comment">// 替换内容可以是函数或原始值，但统一封装成函数，方便处理</span>
<span class="hljs-keyword">const</span> toFunction = <span class="hljs-function">(<span class="hljs-params">functionOrValue</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> functionOrValue === <span class="hljs-string">'function'</span>) <span class="hljs-keyword">return</span> functionOrValue;
  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> functionOrValue;
&#125;

<span class="hljs-keyword">const</span> longest = <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> b.length - a.length;
<span class="hljs-comment">// 将配置中的替换选项和替换内容提取出来</span>
<span class="hljs-keyword">const</span> mapToFunctions = <span class="hljs-function">(<span class="hljs-params">options</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> values = options.values ? <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, options.values) : <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, options);
  <span class="hljs-keyword">delete</span> values.include;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.keys(values).reduce(<span class="hljs-function">(<span class="hljs-params">fns, key</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> functions = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, fns);
    functions[key] = toFunction(values[key]);
    <span class="hljs-keyword">return</span> functions;
  &#125;, &#123;&#125;);
&#125;

<span class="hljs-comment">// 生成esbuild的filter，其实就是一个正则表达式</span>
<span class="hljs-keyword">const</span> generateFilter = <span class="hljs-function">(<span class="hljs-params">options</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> filter = <span class="hljs-regexp">/.*/</span>;
  <span class="hljs-keyword">if</span> (options.include) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.prototype.toString.call(options.include) !== <span class="hljs-string">'[object RegExp]'</span>) &#123;
      <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">`Options.include must be a RegExp object, but gets an '<span class="hljs-subst">$&#123;<span class="hljs-keyword">typeof</span> options.include&#125;</span>' type.`</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
      filter = options.include
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> filter;
&#125;

<span class="hljs-comment">// 核心函数，匹配代码中的字符串，用配置中的替换内容去替换</span>
<span class="hljs-keyword">const</span> replaceCode = <span class="hljs-function">(<span class="hljs-params">code, id, pattern, functionValues</span>) =></span> &#123;
  <span class="hljs-comment">// 这里用了magic-string这个库，方便对字符串进行处理</span>
  <span class="hljs-keyword">const</span> magicString = <span class="hljs-keyword">new</span> MagicString(code);
  <span class="hljs-comment">// 正则匹配</span>
  <span class="hljs-keyword">while</span> ((match = pattern.exec(code))) &#123;
    <span class="hljs-comment">// 获取匹配中的字符的索引</span>
    <span class="hljs-keyword">const</span> start = match.index;
    <span class="hljs-keyword">const</span> end = start + match[<span class="hljs-number">0</span>].length;
    <span class="hljs-comment">// 获取要替换内容</span>
    <span class="hljs-keyword">const</span> replacement = <span class="hljs-built_in">String</span>(functionValues[match[<span class="hljs-number">1</span>]](id));
    <span class="hljs-comment">// 字符串替换</span>
    magicString.overwrite(start, end, replacement);
  &#125;
  <span class="hljs-comment">// 返回处理后的内容</span>
  <span class="hljs-keyword">return</span> magicString.toString();
&#125;

<span class="hljs-comment">// 插件工厂函数</span>
<span class="hljs-built_in">exports</span>.replace = <span class="hljs-function">(<span class="hljs-params">options = &#123;&#125;</span>) =></span> &#123;
  <span class="hljs-comment">// 根据include选项生成filter配置</span>
  <span class="hljs-keyword">const</span> filter = generateFilter(options);
  <span class="hljs-comment">// 得到要replace的key和value对象，注意对象是函数</span>
  <span class="hljs-keyword">const</span> functionValues = mapToFunctions(options);
  <span class="hljs-keyword">const</span> empty = <span class="hljs-built_in">Object</span>.keys(functionValues).length === <span class="hljs-number">0</span>;
  <span class="hljs-comment">// 获取对象的key，并进行排序和转义</span>
  <span class="hljs-keyword">const</span> keys = <span class="hljs-built_in">Object</span>.keys(functionValues).sort(longest).map(<span class="hljs-built_in">escape</span>);
  <span class="hljs-comment">// 将所有key构建成一个正则表达式，用于匹配源代码</span>
  <span class="hljs-keyword">const</span> pattern = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">`\\b(<span class="hljs-subst">$&#123;keys.join(<span class="hljs-string">'|'</span>)&#125;</span>)\\b`</span>, <span class="hljs-string">'g'</span>);
  <span class="hljs-comment">// 返回插件</span>
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'replace'</span>,
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">build</span>)</span> &#123;
      <span class="hljs-comment">// 注册onLoad钩子，解析文件时将会引入</span>
      build.onLoad(&#123; filter &#125;, <span class="hljs-keyword">async</span> (args) => &#123;
        <span class="hljs-comment">// 首先获取源代码内容</span>
        <span class="hljs-keyword">const</span> source = <span class="hljs-keyword">await</span> fs.promises.readFile(args.path, <span class="hljs-string">"utf8"</span>);
        <span class="hljs-comment">// 进行replace</span>
        <span class="hljs-keyword">const</span> contents = empty ? source : replaceCode(source, args.path, pattern, functionValues)
        <span class="hljs-comment">// 返回转化后代码字符串，供esbuild处理</span>
        <span class="hljs-keyword">return</span> &#123; contents &#125;;
      &#125;);
    &#125;
  &#125;;
&#125;
<span class="hljs-built_in">module</span>.exports = <span class="hljs-built_in">exports</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​简单总结一下, <code>esbuild-plugin-replace</code>的核心逻辑就是根据用户的配置项key生成一个正则表达式，然后去匹配源代码，然后再用配置项的内容替换掉命中的字符，这里字符串操作用了<a href="https://www.npmjs.com/package/magic-string" target="_blank" rel="nofollow noopener noreferrer">magic-string</a>这个库，非常好用，推荐一下。然后，这个插件用法也很简单：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; build &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'esbuild'</span>);
<span class="hljs-keyword">const</span> &#123; replace &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'esbuild-plugin-replace'</span>);

build(&#123;
  <span class="hljs-comment">// 其他构建选项...</span>
  <span class="hljs-attr">plugins</span>: [
    replace(&#123;
      <span class="hljs-string">'__author__'</span>: <span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-string">'naecoo'</span>),
      <span class="hljs-string">'__version__'</span>: <span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-string">'1.0.0'</span>)
    &#125;)
  ]  
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你的代码是这样:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> debugInfo = &#123;
  <span class="hljs-attr">author</span>: __author__,
  <span class="hljs-attr">version</span>: __version
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>构建后，将会变成：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> debugInfo = &#123;
  <span class="hljs-attr">author</span>: <span class="hljs-string">"naeco"</span>,
  <span class="hljs-attr">version</span>: <span class="hljs-string">"1.0.0"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">题外话</h3>
<p>​esbuild的插件书写相对来说还是比较简单的，但值得注意一点的是，在构建过程中，不要过度使用插件，特别是用<code>js</code>编写的插件，因为会严重影响构建的性能，如果一定要用，请尽可能配置filter，将插件的作用域范围降至最小。同时，由于<code>esbuild</code>出的时间不算太久，很多工具和生态都不是很完善，如果要引入<code>esbuild</code>，很可能要开发人员自己手写一部分的插件，希望这篇文章可以帮助到你，也希望大家可以积极参与<code>esbuild</code>的生态，贡献更多优秀的代码。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            