
---
title: 'Node 模块解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f12377d10d8d4c608fd48a99507c701b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 02:27:32 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f12377d10d8d4c608fd48a99507c701b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">模块解析</h1>
<p>相关代码大致位于 <code>node/lib/internal/modules/cjs/loader.js</code></p>
<p>默认有 3 种 （v13 更新了第四种，还在实验），分别是 js，json，node。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">> <span class="hljs-built_in">require</span>(<span class="hljs-string">'module'</span>)._extensions
[<span class="hljs-built_in">Object</span>: <span class="hljs-literal">null</span> prototype] &#123;
  <span class="hljs-string">'.js'</span>: [<span class="hljs-built_in">Function</span> (anonymous)],
  <span class="hljs-string">'.json'</span>: [<span class="hljs-built_in">Function</span> (anonymous)],
  <span class="hljs-string">'.node'</span>: [<span class="hljs-built_in">Function</span> (anonymous)]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Node 在没有解析到后缀时，默认使用 CommonJS 模式，而非 JSON</strong> ，也是这里只涉及到的这种解析模式。（一直被各种配置文件的常用格式误导了。。）</p>
<p>具体步骤大致如下：</p>
<ol>
<li>
<p>查询对应文件的绝对路径</p>
</li>
<li>
<p>读取文件的类型</p>
</li>
<li>
<p>通过封装（套函数外壳）创建私有作用域。</p>
</li>
<li>
<p>通过 VM 读取，执行代码</p>
</li>
<li>
<p>完成加载后，对应绝对路径缓存代码</p>
</li>
</ol>
<h2 data-id="heading-1">关键模块</h2>
<p>Node 在模块解析上有两个关键全局模块，不需要加载来完成模块引用和解析的操作。</p>
<ul>
<li>
<p>Require</p>
</li>
<li>
<p>Module</p>
</li>
</ul>
<p>可以理解成这样， <code>require</code> 作为交互用的指令， <code>module</code> 作为全部引用模块的管理者。 依赖的引用就是通过两者的合作完成的。</p>
<h2 data-id="heading-2">加载顺序</h2>
<ol>
<li>
<p>优先使用内置模块，如果有同名的会优先使用内置模块（像 <code>require</code> 和 <code>module</code> ）。</p>
</li>
<li>
<p>查询缓存</p>
</li>
<li>
<p>查询路径</p>
<ol>
<li>
<p>查询文件</p>
</li>
<li>
<p>查询文件夹</p>
</li>
</ol>
</li>
<li>
<p>查询 <code>node_modules</code></p>
</li>
<li>
<p>报错</p>
</li>
</ol>
<p>第三部中的查询地址顺序可以通过打印 <code>module</code> 查看。 这是 Node
模块解析时查询 <code>node_modules</code> 的顺序和对应的路径。</p>
<pre><code class="hljs language-bash copyable" lang="bash">// console.log(module)
Module &#123;
    id: <span class="hljs-string">'.'</span>,
    path: <span class="hljs-string">'/Users/arius/Lib/node-test'</span>,
    exports: &#123;&#125;,
    parent: null,
    filename: <span class="hljs-string">'/Users/arius/Lib/node-test/modules.js'</span>,
    loaded: <span class="hljs-literal">false</span>,
    children: [],
    paths: [
      <span class="hljs-string">'/Users/arius/Lib/node-test/node_modules'</span>,
      <span class="hljs-string">'/Users/arius/Lib/node_modules'</span>,
      <span class="hljs-string">'/Users/arius/node_modules'</span>,
      <span class="hljs-string">'/Users/node_modules'</span>,
      <span class="hljs-string">'/node_modules'</span>
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">文件夹处理</h3>
<p>在对应路径找不到文件的时候，会在该路径查询文件夹。</p>
<p><code>Module._resolveFilename</code> 会判断是否是相对路径。</p>
<p>如果是 <code>.</code> 开头，就是相对路径，这个时候查询文件或者目录 <code>index</code> ;</p>
<p>如果不是 相对路径，则会查询 <code>node_modules</code> ，路径和顺序如上。</p>
<p>只有这个时候会触发 <code>package.json</code> 检索。</p>
<p>加载的 <code>package.json</code> 以 <code>&#123;key: path, value: configJSON&#125;</code> ， 的格式存到全局的 <code>packageJSONCache</code> 中。</p>
<p>查询的实现在 <code>lib/internal/modules/esm/resolve.js::packageMainResolve</code> 中</p>
<p>所以当文件不存在时，执行顺序如下：</p>
<ol>
<li>
<p>查询缓存</p>
</li>
<li>
<p>判读是否是相对路径</p>
<ol>
<li>
<p>如果是，查询路径下的 <code>index</code></p>
</li>
<li>
<p>如果否，遍历 <code>paths</code> 查询 <code>package.json</code> ，并缓存</p>
<ol>
<li>
<p>如果有，先查询是否有 <code>exports</code> (2020-04 的更新)</p>
</li>
<li>
<p>再查询是否有 <code>main</code></p>
</li>
<li>
<p>再查询该路径是否存在 <code>index</code></p>
</li>
</ol>
</li>
</ol>
</li>
<li>
<p>报错</p>
</li>
</ol>
<h2 data-id="heading-4">模块解析</h2>
<p>实现在 <code>lib/internal/modules/cjs/loader.js::Module._compile</code> 。</p>
<p>当查询到后缀为 <code>c?js</code> 或者默认处理时，走js解析。</p>
<p>可以把每个js文件简单理解成一个函数。</p>
<p>因为这个原因，每次引用最外层的代码会被执行，但只输出对应的 <code>module</code> 。</p>
<p>Node解释器就是执行这个函数的工具，将对应的参数传给它，保证执行的作用域。</p>
<pre><code class="hljs language-bash copyable" lang="bash">> node                                                   
Welcome to Node.js v14.9.0.
Type <span class="hljs-string">".help"</span> <span class="hljs-keyword">for</span> more information.
> require(<span class="hljs-string">'module'</span>).wrapper
Proxy [
  [
    <span class="hljs-string">'(function (exports, require, module, __filename, __dirname) &#123; '</span>,
    <span class="hljs-string">'\n&#125;);'</span>
  ],
  &#123; <span class="hljs-built_in">set</span>: [Function: <span class="hljs-built_in">set</span>], defineProperty: [Function: defineProperty] &#125;
]
> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">
  <span class="hljs-built_in">exports</span>, <span class="hljs-comment">// 当前模块 exports 的引用，和 module.exports 是一个东西</span>
  <span class="hljs-built_in">require</span>,<span class="hljs-comment">// 一般就是 Module.prototype.require 即 _Module.prototype.require._load</span>
  <span class="hljs-built_in">module</span>, <span class="hljs-comment">// 当前模块, 也是 this</span>
  __filename, <span class="hljs-comment">// 文件绝对路径</span>
  __dirname <span class="hljs-comment">// 文件相对路径</span>
</span>) </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过前后增加函数执行的外壳，和 <code>Module</code> 统一管理输入的文件访问参数，
生成一个匿名函数，抛给 VM 执行这串代码。</p>
<p>由于node使用函数方式来执行整个文件，所以可以直接打印看到整个模块的相关信息。</p>
<pre><code class="hljs language-bash copyable" lang="bash">// args.js
console.log(arguments)
// run it
node args.js  
[Arguments] &#123;
  <span class="hljs-string">'0'</span>: &#123;&#125;,
  <span class="hljs-string">'1'</span>: [Function: require] &#123;
    resolve: [Function: resolve] &#123; paths: [Function: paths] &#125;,
    main: Module &#123;
      id: <span class="hljs-string">'.'</span>,
      path: <span class="hljs-string">'/Users/arius/Lib/node-test/require-test'</span>,
      exports: &#123;&#125;,
      parent: null,
      filename: <span class="hljs-string">'/Users/arius/Lib/node-test/require-test/args.js'</span>,
      loaded: <span class="hljs-literal">false</span>,
      children: [],
      paths: [Array]
    &#125;,
    extensions: [Object: null prototype] &#123;
      <span class="hljs-string">'.js'</span>: [Function (anonymous)],
      <span class="hljs-string">'.json'</span>: [Function (anonymous)],
      <span class="hljs-string">'.node'</span>: [Function (anonymous)]
    &#125;,
    cache: [Object: null prototype] &#123;
      <span class="hljs-string">'/Users/arius/Lib/node-test/require-test/args.js'</span>: [Module]
    &#125;
  &#125;,
  <span class="hljs-string">'2'</span>: Module &#123;
    id: <span class="hljs-string">'.'</span>,
    path: <span class="hljs-string">'/Users/arius/Lib/node-test/require-test'</span>,
    exports: &#123;&#125;,
    parent: null,
    filename: <span class="hljs-string">'/Users/arius/Lib/node-test/require-test/args.js'</span>,
    loaded: <span class="hljs-literal">false</span>,
    children: [],
    paths: [
      <span class="hljs-string">'/Users/arius/Lib/node-test/require-test/node_modules'</span>,
      <span class="hljs-string">'/Users/arius/Lib/node-test/node_modules'</span>,
      <span class="hljs-string">'/Users/arius/Lib/node_modules'</span>,
      <span class="hljs-string">'/Users/arius/node_modules'</span>,
      <span class="hljs-string">'/Users/node_modules'</span>,
      <span class="hljs-string">'/node_modules'</span>
    ]
  &#125;,
  <span class="hljs-string">'3'</span>: <span class="hljs-string">'/Users/arius/Lib/node-test/require-test/args.js'</span>,
  <span class="hljs-string">'4'</span>: <span class="hljs-string">'/Users/arius/Lib/node-test/require-test'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为是引用的关系 <code>module.exports</code> 一般和 <code>exports</code> 指向同一个东西,
但需要注意，执行 <code>require</code> 导出永远的 <code>module</code> 是不会变的， <code>exports</code> 只是引用。
这也是为啥 <code>exports=xxx</code> 不会生效的原因。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">module</span>.<span class="hljs-keyword">exports</span> = &#123;
  a: <span class="hljs-string">'123'</span>, <span class="hljs-comment">// 最终依然是 123</span>
&#125;
<span class="hljs-keyword">exports</span>.a = <span class="hljs-string">'321'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">依赖循环</h2>
<p>而当 <code>require</code> 一个包或者文件的时候，执行（或者说依赖）的并不直接是这个包。
对应整个对象的 <code>module</code>， 会被缓存到全局对象 <code>Module._cache[filename]</code> 中。</p>
<p>假如执行 <code>a.js</code> 。</p>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-comment">// a.js</span>
<span class="hljs-keyword">const</span> b = <span class="hljs-keyword">require</span>(<span class="hljs-string">'./b'</span>)
console.log(b) <span class="hljs-comment">// 'b'</span>
module.exports = <span class="hljs-string">'a'</span>
<span class="hljs-comment">// b.js</span>
<span class="hljs-keyword">const</span> a = <span class="hljs-keyword">require</span>(<span class="hljs-string">'./a'</span>)
console.log(a) <span class="hljs-comment">// &#123;&#125;, Module._cache中 a依然是 空的 Module &#123;&#125; 对象</span>
module.exports = <span class="hljs-string">'b'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>依赖处理中， CJS 和 ES 运行顺序是一致的 (其中 <code>default</code> , 子模块都为 <code>undefined</code> )，不同的是 ES 可以动态替换引用。
只要引用是在加载完成之后被调用, 就不会有问题。
所以需要注意需要最外层执行的函数的顺序。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// a.js</span>
<span class="hljs-keyword">import</span> &#123; b &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../'</span>;
<span class="hljs-built_in">console</span>.log(b)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> a = <span class="hljs-string">'a'</span>
<span class="hljs-comment">// b.js</span>
<span class="hljs-keyword">import</span> &#123; a &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../'</span>;
<span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// undefined</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> callA = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// 'a'</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> b = <span class="hljs-string">'b'</span>
<span class="hljs-comment">// index</span>
<span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> <span class="hljs-string">'./a'</span>;
<span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> <span class="hljs-string">'./b'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是 <code>mjs</code> 的话，遇到循环依赖会报错，可能还没支持或者是新的规范。。</p>
<pre><code class="hljs language-bash copyable" lang="bash">ReferenceError: Cannot access <span class="hljs-string">'a'</span> before initialization
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么 <code>mjs</code> 是啥？</p>
<h1 data-id="heading-6">ECMAScript 模块</h1>
<p>官方实验 ES6 规范，以 <code>mjs</code> 后缀结尾。
<code>cjs</code> 和 <code>esm</code> 的主要的区别在于， <code>require</code> + <code>module.exports</code> 对应 <code>import</code> 和 <code>export</code> 。</p>
<pre><code class="hljs language-bash copyable" lang="bash">// 使用的时候会有一个 实验的 warning
(node:55066) ExperimentalWarning: The ESM module loader is experimental.
// 如果直接 import 调用对应不是 mjs 的模块
(node:54924) Warning: To load an ES module, <span class="hljs-built_in">set</span> <span class="hljs-string">"type"</span>: <span class="hljs-string">"module"</span> <span class="hljs-keyword">in</span> the package.json or use the .mjs extension.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Node 要求 esm 模块都使用 <code>.mjs</code> 后缀，且 <strong>默认启动严格模式</strong> 。</p>
<p>或者在 <code>package.json</code> 中制定为 <code>type</code> 为 <code>module</code> ，这样执行目录内 <code>js</code> 脚本都会解析成 ES6 模块。这个解析仅限于 <code>js</code> 后缀， 其他(非 <code>js</code> )使用 <code>cjs</code> 或者 <code>mjs</code> 后缀文件会使用对应的解析方式。</p>
<p>与 Babel 时混用处理的方式不同， <code>require</code> 不能加载 <code>mjs</code> , <code>mjs</code> 中不能使用 <code>require</code> 。</p>
<h2 data-id="heading-7">相互调用</h2>
<p><code>cjs</code> 调用 <code>mjs</code> 时，需要用异步。
异步调用可能是想继承 <code>esm</code> 动态引用的机制，但是目前还不允许循环依赖。
而 <code>require</code> 不支持 ES6 模块的一个原因是，它是同步加载，而 ES6 模块内部可以使用顶层 <code>await</code> 命令，导致无法被同步加载。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">await</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./my-app.mjs'</span>);
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 <code>mjs</code> 调用 <code>cjs</code> 的时候只能整体调用，无法解析，作 shaking 啥的。</p>
<h2 data-id="heading-8">支持多个模式</h2>
<p>如果是 esm 模式则需要给一个整体的接口 <code>export default</code> 。
如果是 CommonJS 模式则需要封装一层，拆分一个单独的文件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> cjsModule <span class="hljs-keyword">from</span> <span class="hljs-string">'../index.cjs'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> &#123;...&#125; = cjsModule;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者使用 <code>package.json</code> 的方式修改, 其中 <code>exports</code> 除了相对路径替换外，还可以挑选调用方式。
具体如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./index.js</span>
<span class="hljs-built_in">require</span>(<span class="hljs-string">'find-me'</span>);<span class="hljs-comment">// Found you</span>
<span class="hljs-comment">// ./index.mjs</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'find-me'</span>; <span class="hljs-comment">// Found me!</span>


<span class="hljs-comment">// ./node_modules/find-me/package.json</span>
&#123;
  <span class="hljs-string">"exports"</span>: &#123;
    <span class="hljs-string">"import"</span>: <span class="hljs-string">"./me.mjs"</span>
    <span class="hljs-string">"require"</span>: <span class="hljs-string">"./you.js"</span>
  &#125;
&#125;
<span class="hljs-comment">// ./node_modules/find-me/you.js</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Found you'</span>)
<span class="hljs-comment">// ./node_modules/find-me/me.mjs</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Found me!'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">FAQ</h1>
<h2 data-id="heading-10">1. Node 中的错误行数问题</h2>
<p>Node 本身并没有对错误函数做处理，一切错误处理都来自 VM，历史上 Node 上报堆栈失败的原因是那时候 Node 4 没有配置 <code>displayErrors</code> 参数。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f12377d10d8d4c608fd48a99507c701b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://github.com/nodejs/node/pull/4874" target="_blank" rel="nofollow noopener noreferrer">github.com/nodejs/node…</a></p>
<p><code>wrapper</code> 本身第一行没有换行，而且代码没有压缩，直接拼接，所以不会有行数问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c20acac498114512b9b3e96c6f05d670~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">Refers</h1>
<ul>
<li>
<p><a href="https://github.com/nodejs/node" target="_blank" rel="nofollow noopener noreferrer">Node repo ，调试构建有点慢</a></p>
</li>
<li>
<p><a href="http://nodejs.cn/api/esm.html#esm_modules_ecmascript_modules" target="_blank" rel="nofollow noopener noreferrer">Node mjs api 文档</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6866973719634542606#heading-18" target="_blank">深入Node.js的模块加载机制，手写require函数。很不错的文章</a></p>
</li>
<li>
<p><a href="https://www.freecodecamp.org/news/requiring-modules-in-node-js-everything-you-need-to-know-e7fbd119be8/" target="_blank" rel="nofollow noopener noreferrer">关于 require 你所要知道的东西 （英文）</a></p>
</li>
</ul></div>  
</div>
            