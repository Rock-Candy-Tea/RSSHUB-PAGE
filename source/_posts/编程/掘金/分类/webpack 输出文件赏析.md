
---
title: 'webpack 输出文件赏析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1095'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 19:37:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=1095'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>序：</strong></p>
<p>5月份的时候我的好朋友（@杨鹏）看了 github 上的博客年少时的孤芳自赏，特意跑来夸奖一番。他期待我更新，我回复到6月会更一篇。但是我的整个 6 月都在忙（懒）着一个项目的重构，导致只要有点时间就去 B 站消遣去了（这事得怪up主小约翰可汗）。确实好久不写了，杨鹏的夸赞当勉励，也当是督促。我大概是第一个写技术博客还要写序的人，这一篇给杨鹏，祝好！</p>
<p>本篇内容略长，建议收藏精读；用 webpack 有几年了，也听了很多面试官问看过 webpack 打包输出的内容么。近来在重看 webpack 代码，愈发感叹 webpack 设计之精妙，感叹之余决定写上一篇标题用"赏析" 而不用解析，足见其妙；水平有限，不喜轻喷，如果有错误，请各位大佬指出，不胜感激！</p>
<h2 data-id="heading-0">1. demo 代码</h2>
<blockquote>
<p>本篇所用 webpack 为 v4.x 版本</p>
</blockquote>
<ul>
<li>webpack.config.js</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">bundle</span>: <span class="hljs-string">'./src/a.js'</span>
  &#125;,
  <span class="hljs-attr">devtool</span>: <span class="hljs-string">'none'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: __dirname + <span class="hljs-string">'/dist'</span>,
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].[chunkhash:4].js'</span>,
    <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">'[name].[chunkhash:8].js'</span>
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> HtmlWebpackPlugin()],
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@babel/env'</span>]
            &#125;
          &#125;
        ]
      &#125;
    ]
  &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>入口 a.js</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; add &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./b'</span>;
<span class="hljs-keyword">import</span>(<span class="hljs-string">'./c.js'</span>).then(<span class="hljs-function"><span class="hljs-params">m</span> =></span> m.minus(<span class="hljs-number">2</span>, <span class="hljs-number">1</span>));

<span class="hljs-keyword">const</span> A_NUM = <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> r = add(<span class="hljs-number">3</span>, <span class="hljs-number">2</span> + A_NUM);

<span class="hljs-built_in">console</span>.log(r);

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>模块 b.js</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> SOME_VAR = <span class="hljs-string">'SOME_VAR'</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>模块 c.js</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span>(<span class="hljs-string">'./b.js'</span>).then(<span class="hljs-function"><span class="hljs-params">m</span> =></span> m.add(<span class="hljs-number">200</span>, <span class="hljs-number">100</span>));

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">minus</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a - b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>模块 d.js</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> L = <span class="hljs-string">'Aragaki Yui'</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">times</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a * b
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. 打包输出文件</h2>
<p>注意打包的模式是开发模式，不要混淆代码，我们还要读这些代码，输出文件如下</p>
<ul>
<li>0.a619de3d.js (下称 chunk)</li>
<li>bundle.b05e.js (下称 bundle)</li>
<li>index.html</li>
</ul>
<h2 data-id="heading-2">3. 删除空注释</h2>
<p>这一步是降低心理难度的重要手段，很多人都是被这一大堆的注释劝退的；所以把类似下面的注释都替换成空，没错，用你的IDE，Cmd + R；暂时移除以下注释：bundle
和 chunk 的处理相同。</p>
<ul>
<li>bundle 里面的空注释，示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/******/</span>
 
<span class="hljs-comment">/***/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>模块前的注释，示例</li>
</ul>
<p>个注释是用来提示模块导出了那些内容，暂时忽略</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/*!******************!*\
  !*** ./src/a.js ***!
  \******************/</span>
<span class="hljs-comment">/*! no exports provided */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4. bundle （bundle.b05e.js）结构</h2>
<h3 data-id="heading-4">4.1 整体结构</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">modules</span>) </span>&#123; 
  <span class="hljs-comment">// webpack runtime 代码</span>
&#125;)(&#123;
  <span class="hljs-comment">// 这个是模块对象，下称为 modules， 注意提到 modules 就要想到这个对象！！！！</span>
  <span class="hljs-comment">// key 是模块的路径，注意，如果同一个模块使用了不同 loader，webpack 会认为这是两个模块，这个差别会体现在 key 上，key 包含了使用的 loader(如有)</span>
  <span class="hljs-comment">// value 就是被 webpack 包装处理过后的模块</span>
  <span class="hljs-string">"./src/a.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;&#125;),
  <span class="hljs-string">"./src/b.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;&#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的代码块可以看出来，这个结构就是一个自执行函数（IIFE），它定义形参 modules，接收实参为一个对象，这个对象中 key 是模块路径，value 则是被 webpack 包装后的模块；</p>
<p>看具体的代码前，先要了解一个概念———— runtime；我们来看下中文官方文档的定义：
<code> runtime，.....主要是指：在浏览器运行过程中，webpack 用来连接模块化应用程序所需的所有代码。它包含：在模块交互时，连接模块所需的加载和解析逻辑。包括：已经加载到浏览器中的连接模块逻辑，以及尚未加载模块的延迟加载逻辑。</code></p>
<p>简言之，就是 webpack 用来处理连接、加载、执行 webpack 模块的代码；这些就是 bundle 中自执行函数的主要内容，这一段信息量有点大，我们还是由外入内的介绍一下这些变量、方法、以及方法上的属性的大致作用；</p>
<h3 data-id="heading-5">4.2 runtime 概览</h3>
<p>1、  webpackJsonpCallback 方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">modules</span>) </span>&#123; <span class="hljs-comment">// webpack 启动代码</span>
    <span class="hljs-comment">// 这个 webpackJsonpCallback 是通过 JSONP 加载那些按需加载(import(some-file.js).then(...))的 chunk 时的 JSONP 的回调 callback；</span>
    <span class="hljs-comment">// JSONP 就是创建一个 script 标签去加载 js 文件，而 JOSNOP callback 就是加载回来以后要做的事情</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">webpackJsonpCallback</span>(<span class="hljs-params">data</span>) </span>&#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、 installedModules</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 模块缓存，已经安装过的模块们，如果已经加安装过了就缓存在这个对象中，下次再访问这个模块走缓存就可以了</span>
<span class="hljs-comment">// 下面的 __webpack_require__ 就是用来安装模块的</span>
<span class="hljs-keyword">var</span> installedModules = &#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、 installedChunks</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 这个已经安装过的 chunks，这个就有点复杂了；后面会细说加载异步 chunk 的过程；</span>
<span class="hljs-comment">// installedChunks 这个对象以 key-value 的形式保存已经安装的 chunk，key 是 chunk id，关于 value 有以下几种情况：</span>
<span class="hljs-comment">// value = undefined，表示该 chunk 未被加载过</span>
<span class="hljs-comment">// value = 0，chunk 已经加载完毕</span>
<span class="hljs-comment">// value = <Array> [Promise resolveFn, Promise rejectFn, Promise] 表示 chunk 正在加载中，关于为啥搞成这个数组结构后面的加载异步chunk 会细说</span>
<span class="hljs-comment">// value = null 表示 chunk preload 或者 prefetch </span>
    <span class="hljs-keyword">var</span> installedChunks = &#123;
            <span class="hljs-string">"bundle"</span>: <span class="hljs-number">0</span>
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、 jsonpScriptSrc 方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 为 script 标签 src 属性拼接 __webpack_require_.p，这个 p 属性就是 webpack.config.js 中 output.publicPath </span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jsonpScriptSrc</span>(<span class="hljs-params">chunkId</span>) </span>&#123;
<span class="hljs-keyword">return</span> __webpack_require__.p + <span class="hljs-string">""</span> + (&#123;&#125;[chunkId]||chunkId) + <span class="hljs-string">"."</span> + &#123;<span class="hljs-string">"0"</span>:<span class="hljs-string">"a619de3d"</span>&#125;[chunkId] + <span class="hljs-string">".js"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5、  _<em>webpack_require_</em> 方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack 运行时的主要方法，其作用创建并缓存 module 对象()后，执行这个 module 中的代码；</span>
<span class="hljs-comment">// 创建 module 是啥意思嘞？就是 __webpack_require__ 中的 &#123; i: moduleId, l: false, exports: &#123;&#125; &#125; 对象</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">__webpack_require__</span>(<span class="hljs-params">moduleId</span>) </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6、 __webpack_require__.e 静态属性</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 用于加载额外 chunk 的函数，比如按需加载的 chunk，这个里面就会有创建 script 标签然后去加载代码的具体逻辑，后面细说</span>
__webpack_require__.e = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">requireEnsure</span>(<span class="hljs-params">chunkId</span>) </span>&#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7、  __webpack_require__.m 静态属性</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 暴露这个 runtime 接收到的 modules 对象（这个自执行函数接收到参数对象，看上面 4.1 ）</span>
__webpack_require__.m = modules;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>8、 __webpack_require__.c 静态属性</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 暴露缓存的已经安装的模块们</span>
__webpack_require__.c = installedModules;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>9、 __webpack_require__.d 静态方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 在模块对象(module 上面__webpack_require__ 中创建的 module 对象，下同)的 exports 对象上增加属性，</span>
<span class="hljs-comment">// 以 getter 的形式定义导出（就是实现你代码中的通过 export 导出一个变量/常量/函数等）</span>
__webpack_require__.d = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">exports</span>, name, getter</span>) </span>&#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>10、 __webpack_require__.r 静态方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 在模块对象(module) 增加 __esModule 属性，用于标识这个模块是个 ES6 模块</span>
__webpack_require__.r = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">exports</span></span>) </span>&#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>11、 __webpack_require__.t 静态方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 这个 t 先忽略掉，暂时用不到</span>
__webpack_require__.t = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value, mode</span>) </span>&#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>12、 __webpack_require__.n 静态方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 得到 getDefaultExport 方法，抹平 ES6 的模块和非 ES6 模块的默认导出</span>
__webpack_require__.n = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span></span>) </span>&#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>13、 __webpack_require__.o 静态方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 调用 hasOwnProperty 判断对象是否有某一属性</span>
__webpack_require__.o = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">object, property</span>) </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.hasOwnProperty.call(object, property); &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>14、 __webpack_require__.p 静态属性</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 这个就是 webpack.config.js 中 output.publicPath，上面 jsonpScriptSrc 方法就是拼接的这个值</span>
__webpack_require__.p = <span class="hljs-string">""</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>15、 __webpack_require__.oe 静态方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 错误处理，忽略</span>
__webpack_require__.oe = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123; <span class="hljs-built_in">console</span>.error(err); <span class="hljs-keyword">throw</span> err; &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>16、 JSONP 初始化</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// JSONP 初始化，这是个精彩的部分，后面讲异步 chunk 加载的时候细说，但是先来看看这几步骤都在干啥</span>
<span class="hljs-keyword">var</span> jsonpArray = <span class="hljs-built_in">window</span>[<span class="hljs-string">"webpackJsonp"</span>] = <span class="hljs-built_in">window</span>[<span class="hljs-string">"webpackJsonp"</span>] || []; <span class="hljs-comment">// 初始化 window[webpackJsonp] 对象</span>
<span class="hljs-keyword">var</span> oldJsonpFunction = jsonpArray.push.bind(jsonpArray); <span class="hljs-comment">// 暂存数组 push 方法，这个 push 就是 Array.prototype.push</span>
jsonpArray.push = webpackJsonpCallback; <span class="hljs-comment">// 重写 jsonpArray.push 方法（注意，这么重写不会改写数组原型）</span>
jsonpArray = jsonpArray.slice(); <span class="hljs-comment">// 赋值 jsonpArrray，这个复制不带 push 方法！</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < jsonpArray.length; i++) webpackJsonpCallback(jsonpArray[i]); <span class="hljs-comment">// 若chunk先于 bundle 这个入口加载，这个 jsonpArray 里面就不是空的，此时，遍历并调用 webpackJsonpCallback，相当于手动触发 jsonp callback</span>
<span class="hljs-keyword">var</span> parentJsonpFunction = oldJsonpFunction; <span class="hljs-comment">// 旧 push 暂存于 parentJsonpFunciton</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>17、 __webpack_require__() 加载入口启动应用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 加载入口 module 并返回 webpack_require__ 执行后的 exports 对象</span>
<span class="hljs-comment">// 从这里算是真正的开始跑我们开发的模块了</span>
    <span class="hljs-keyword">return</span> __webpack_require__(__webpack_require__.s = <span class="hljs-string">"./src/a.js"</span>);
&#125;)
<span class="hljs-comment">/************************************************************************/</span>
(&#123;
<span class="hljs-comment">// 这就是 webpack runtime 的自执行函数接收到 modules 对象：提到 modules 请联想到这个对象</span>
    <span class="hljs-string">"./src/a.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;&#125;),
    <span class="hljs-string">"./src/b.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;&#125;)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">4.3 __webpack_require__ 方法</h3>
<p>前面的删除注释、把函数体里面的代码删除，都是在剔除支线剧情，让我们更多注意力放在我想表达的重点上，你可以更好的跟着作者的写作思路，如果你还在读，你会发现我已经由外入内了，从整个 js 文件到 webpack runtime 概览，从这个小的主题我就要进入到一个方法的代码块。</p>
<p>我们来重复一下 _<em>webpack_require_</em> 方法的作用：接收指定 moduleId 作为参数，创建并缓存 module 对象，加载并执行 moduleId 代码，是 webpack runtime 的重要部分；</p>
<p>在上面 webpack runtime 概览的最后发现，在 runtime 的最后调用了 __webpack_require__(<strong>webpack_require</strong>.s = './src/a.js')；接下来看看方法里面发生了什么：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">__webpack_require__</span> (<span class="hljs-params">moduleId</span>) </span>&#123;

    <span class="hljs-comment">// 查看缓存，如果缓存中有了即返回缓存即可：installedModules 在上面 4.2 runtime 概览（2）</span>
    <span class="hljs-keyword">if</span> (installedModules[moduleId]) &#123;
      <span class="hljs-keyword">return</span> installedModules[moduleId].exports
    &#125;

    <span class="hljs-comment">// 创建并缓存 module 对象，后面被赋值的这个对象称为  module 对象</span>
    <span class="hljs-keyword">var</span> <span class="hljs-built_in">module</span> = installedModules[moduleId] = &#123;
      <span class="hljs-attr">i</span>: moduleId,
      <span class="hljs-attr">l</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">exports</span>: &#123;&#125;
    &#125;

    <span class="hljs-comment">// 执行 module 中的代码：</span>
    <span class="hljs-comment">// modules 就是 webpack runtime 这个自执行函数接收到的模块对象，</span>
    <span class="hljs-comment">// moduleId 是什么？从上面 runtime 最后调用 __webpack_require__ 的时候可以发现接收的参数即 moduleId，即 ./src/a.js，这就是说 moduleId 可以认为是个路径</span>
    <span class="hljs-comment">// call 则把模块中的 this 修改成 module.exports 并执行，执行时传入参数：module, module.exports, __webpack_require__ （有没有 node.js 中 CMD 的感觉了）</span>
    modules[moduleId].call(<span class="hljs-built_in">module</span>.exports, <span class="hljs-built_in">module</span>, <span class="hljs-built_in">module</span>.exports, __webpack_require__)

    <span class="hljs-comment">// 标记 module 已经加载过，l 我猜猜是 loaded 的缩写</span>
    <span class="hljs-built_in">module</span>.l = <span class="hljs-literal">true</span>

    <span class="hljs-comment">// 把 module 的 exports 导出</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">module</span>.exports
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们看看 modules[moduleId] 即 modules["./src/a.js"] 里面是什么：</p>
<ul>
<li>modules</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1. webpack runtime 接收到的 modules 就是这个样子：</span>
<span class="hljs-keyword">var</span> modules = (&#123;
    <span class="hljs-string">"./src/a.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;
<span class="hljs-meta">      "use strict"</span>;
      __webpack_require__.r(__webpack_exports__);
      <span class="hljs-comment">/* harmony import */</span> <span class="hljs-keyword">var</span> _b__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(<span class="hljs-comment">/*! ./b */</span> <span class="hljs-string">"./src/b.js"</span>);
  
      __webpack_require__.e(<span class="hljs-comment">/*! import() */</span> <span class="hljs-number">0</span>)
        .then(__webpack_require__.bind(<span class="hljs-literal">null</span>, <span class="hljs-comment">/*! ./c.js */</span> <span class="hljs-string">"./src/c.js"</span>))
        .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">m</span>) </span>&#123;<span class="hljs-keyword">return</span> m.minus(<span class="hljs-number">2</span>, <span class="hljs-number">1</span>);&#125;);
      <span class="hljs-keyword">var</span> A_NUM = <span class="hljs-number">1</span>;
      <span class="hljs-keyword">var</span> r = <span class="hljs-built_in">Object</span>(_b__WEBPACK_IMPORTED_MODULE_0__[<span class="hljs-string">"add"</span>])(<span class="hljs-number">3</span>, <span class="hljs-number">2</span> + A_NUM);
      <span class="hljs-built_in">console</span>.log(r);
    &#125;),
    <span class="hljs-string">"./src/b.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;&#125;)
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>取 ./src/a.js</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 2. modules[moduleId] </span>
<span class="hljs-comment">// 从上面可以看出 modules[./src/a.js] 得到的一个函数 </span>

<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack__require__</span>) </span>&#123;
<span class="hljs-meta">    "use strict"</span>;
    __webpack_require__.r(__webpack_exports__); <span class="hljs-comment">// 利用上面的 __webpack_require\__.r 方法将该模块的 exports 对象上增加 __esModule 属性，定性为 ES6 module 对象</span>
    <span class="hljs-comment">/* harmony import */</span> <span class="hljs-keyword">var</span> _b__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(<span class="hljs-comment">/*! ./b */</span> <span class="hljs-string">"./src/b.js"</span>); <span class="hljs-comment">// 实现 import &#123; add &#125; from './b';</span>
    
    <span class="hljs-comment">// 实现 import('b.js').then(m => m.minus(2, 1);</span>
    __webpack_require__.e(<span class="hljs-comment">/*! import() */</span> <span class="hljs-number">0</span>) 
        .then(__webpack_require__.bind(<span class="hljs-literal">null</span>, <span class="hljs-comment">/*! ./c.js */</span> <span class="hljs-string">"./src/c.js"</span>))
        .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">m</span>) </span>&#123;<span class="hljs-keyword">return</span> m.minus(<span class="hljs-number">2</span>, <span class="hljs-number">1</span>);&#125;);
    <span class="hljs-keyword">var</span> A_NUM = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">var</span> r = <span class="hljs-built_in">Object</span>(_b__WEBPACK_IMPORTED_MODULE_0__[<span class="hljs-string">"add"</span>])(<span class="hljs-number">3</span>, <span class="hljs-number">2</span> + A_NUM);
    <span class="hljs-built_in">console</span>.log(r);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>和 src/a.js 源码对比一下</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; add &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./b'</span>;
<span class="hljs-keyword">import</span>(<span class="hljs-string">'./c.js'</span>).then(<span class="hljs-function"><span class="hljs-params">m</span> =></span> m.minus(<span class="hljs-number">2</span>, <span class="hljs-number">1</span>));

<span class="hljs-keyword">const</span> A_NUM = <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> r = add(<span class="hljs-number">3</span>, <span class="hljs-number">2</span> + A_NUM);

<span class="hljs-built_in">console</span>.log(r);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以轻松发现 webpack 都对代码做了些什么：</p>
<p>1）给模块包了一层函数 function (module, __webpack_exports_<em>, __webpack_require_</em>) &#123;&#125;；这么做则是为了实现模块化，用闭包做隔离， webpack 自己实现了一个 CommonJS 规范；</p>
<p>2）利用上面的 __webpack_require__.r 方法将该模块的 exports 对象上增加 __esModule 属性，定性为 ES6 module 对象；看看 .r 方法（上面 4.2 runtime 概览（10））：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">__webpack_require__.r = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">exports</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> !== <span class="hljs-string">'undefined'</span> && <span class="hljs-built_in">Symbol</span>.toStringTag) &#123;
      <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">exports</span>, <span class="hljs-built_in">Symbol</span>.toStringTag, &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'Module'</span> &#125;)
    &#125;
    <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">exports</span>, <span class="hljs-string">'__esModule'</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-literal">true</span> &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3）实现 <code>import &#123; add &#125; from './b'</code>; 导入 b 模块上的 add 方法，我们发现 <code>import</code> 关键字被 <code>__webpack_require__</code> 实现了，我们发现源码中的 add() 调用被处理成了<code> _b__WEBPACK_IMPORTED_MODULE_0__['add']</code>，这说明 add 这个方法被放到了 <code>_b__WEBPACK_IMPORTED_MODULE_0__</code> 对象上，那么这里思考一下，b 模块的导出怎么去了这个对象上的呢？</p>
<p>4）实现 <code>import('c.js').then(m => m.minus(2, 1)</code>; import(c.js) 变成了 <code>__webpack_require\__.e(/*! import() */ 0)</code>，而且增加了一个 <code>then(__webpack_require\__.bind(null, 'c.js''))</code> 这又是在搞什么呢？这个后面揭晓；</p>
<p>5）调用得到的 add 方法，忽略</p>
<p>6）log 输出，忽略</p>
<ul>
<li>我们看看 webpack 处理后的 b.js 的样子：</li>
</ul>
<p>b.js 同样在 modules 中，如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// moduels</span>
<span class="hljs-keyword">var</span> modules = (&#123;
    <span class="hljs-string">"./src/a.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;&#125;),
    <span class="hljs-string">"./src/b.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;
<span class="hljs-meta">      "use strict"</span>;
      __webpack_require__.r(__webpack_exports__);
      <span class="hljs-comment">/* harmony export (binding) */</span> __webpack_require__.d(__webpack_exports__, <span class="hljs-string">"SOME_VAR"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> SOME_VAR; &#125;);
      <span class="hljs-comment">/* harmony export (binding) */</span> __webpack_require__.d(__webpack_exports__, <span class="hljs-string">"add"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> add; &#125;);
      <span class="hljs-keyword">var</span> SOME_VAR = <span class="hljs-string">'SOME_VAR'</span>;
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
        <span class="hljs-keyword">return</span> a + b;
      &#125;
    &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比一下 b.js 的源码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> SOME_VAR = <span class="hljs-string">'SOME_VAR'</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以轻易看出 webpack 对 b.js 做了些什么：</p>
<p>1）<code>__webpack_require\__.r</code> 标识该模块是一个 ES6 的模块；</p>
<p>2）实现 <code>export const SOME_VAR = 'SOME_VAR'</code> ；我们发现 webpack 是通过 __webpack_require__.d 实现的 export 关键字，即导出，接着我们看 .d 方法（4.2 runtime 概览（9））；d 方法就是通过在 module.exports 对象（_<em>webpack_require_</em> 创建的）配置 getter 实现 export；这么做的好处在哪里？这种 export 一个变量（包括函数），好处是这个 getter 访问的都是原来模块作用域中的变量，自动连接到模块的作用域，若此设计不可谓不机智；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">__webpack_require__.d = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">exports</span>, name, getter</span>) </span>&#123;
    <span class="hljs-comment">// __webpack_require__.o 是 hasOwnProperty 方法，判断是否有私有属性的</span>
    <span class="hljs-keyword">if</span> (!__webpack_require__.o(<span class="hljs-built_in">exports</span>, name)) &#123;
      <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">exports</span>, name, &#123; <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">get</span>: getter &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>简单回顾一下，webpack 怎么让代码跑起来的？</li>
</ul>
<p>1）webpack 有自己的runtime，其中的 _<em>webpack_require_</em> 可以创建、缓存 module，然后加载并运行 module。在 runtime 的末尾传入入口模块的路径并执行 _<em>webpack_require_</em> 方法；</p>
<p>2）webpack 的 runtime 接受到了一个 modules 对象，其中 key 是模块路径，value 则是被 webpack 处理过的函数，这个函数就是模块主体；</p>
<p>3）webpack 通过 __webpack_require_<em>.r 定义 ES6 模块，通多 __webpack_require_</em>.d 方法实现 export，通过 _<em>webpack_require_</em> 实现 import 等措施实现了一个 CommonJS 规范的模块系统；</p>
<h2 data-id="heading-7">5. 非入口 chunk 的加载</h2>
<h3 data-id="heading-8">5.1 细说 <strong>webpack_require</strong>.e 方法</h3>
<p>就说说 webpack 是如何加载非入口 chunk，非入口 chunk 的加载需要 __webpack_require__.e 方法。在前面的 demo 中，a.js 源码中通过 import(c.js) 语法实现按需加载，被按需加载的模块会以一个单独的 chunk 生成一个文件 ———— 0.a619de3d.js；在看这个 chunk 之前，我们先看看 a.js 又是如何实现的 import() 语法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> modules = &#123;
    <span class="hljs-string">"./src/a.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;
        <span class="hljs-comment">// ... </span>
        <span class="hljs-comment">// 这里就是实现的 import(c.js).then((m) => ....)</span>
        __webpack_require__.e(<span class="hljs-comment">/*! import() */</span> <span class="hljs-number">0</span>)
          .then(__webpack_require__.bind(<span class="hljs-literal">null</span>, <span class="hljs-comment">/*! ./c.js */</span> <span class="hljs-string">"./src/c.js"</span>))
          .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">m</span>) </span>&#123;
            <span class="hljs-keyword">return</span> m.minus(<span class="hljs-number">2</span>, <span class="hljs-number">1</span>);
          &#125;);
    &#125;),
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码可以看出，<code>__webpack_require_<em>.e(/*! import() */ 0).then(__webpack_require_</em>.bind(null, /*! ./c.js */ "./src/c.js"))</code> 实现的 <code> import(c.js)</code>；接下来就该看看 e 方法的真实面目：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">__webpack_require__.e = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">requireEnsure</span>(<span class="hljs-params">chunkId</span>) </span>&#123;
    <span class="hljs-comment">// 1. 参数 chunkId: 用于加载的 chunk 的 chunkId，从上面调用该方法中可以看出要的加载 c.js 的对应的 chunkId 是 0，这个 chunkId 是 webpack 生成的，这里不需要关心；细心的朋友发现 chunk 文件除了 chunkId 0 后面还有 hash，这个 hash 哪里来的呢？这个后面下面揭晓</span>

    <span class="hljs-comment">// 2. promise 队列，可以加载多个 chunk；</span>
    <span class="hljs-keyword">var</span> promises = [];
    
    <span class="hljs-comment">// 3. 尝试从已经安装过的 chunk 中取用参数 chunkId，这个 installedChunks 的作用在上文 4.2 runtime 概览（3）</span>
    <span class="hljs-keyword">var</span> installedChunkData = installedChunks[chunkId];
    <span class="hljs-keyword">if</span>(installedChunkData !== <span class="hljs-number">0</span>) &#123; <span class="hljs-comment">// 这里判断非0，因为 0 表示已经安装过了</span>
        <span class="hljs-comment">// 如果从 installedChunks 中取到的 installedChunkData 是个 promise 则说明正在加载这个 chunk；</span>
        <span class="hljs-keyword">if</span>(installedChunkData) &#123;
           <span class="hljs-comment">// 这里有个精巧的设计，回到上面 4.2 runtime 概览（3）中关于 installedChunk 的 value 的详述中，</span>
            <span class="hljs-comment">// 只有一种情况不是 falsy 的值，其他的value如 0，undefined、null 都是 falsy，</span>
            <span class="hljs-comment">// 所以这里他敢判断 if(installedChunData) 而不用做细致判断</span>
            <span class="hljs-comment">// 就一个字，绝</span>
            promises.push(installedChunkData[<span class="hljs-number">2</span>]);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// else 说明这里就说明都是些 falsy 的值，说明该去乖乖的加载这个 chunkId 对应的 chunk 文件</span>

            <span class="hljs-comment">// 这里就要回达 4.2 runtime 概览（3）中为啥 installedChunks 的 value 有一种情况是一个数组:</span>
            <span class="hljs-comment">// [Promise resolveFn, Promise, rejectFn, promise] </span>
            <span class="hljs-comment">// 就是从 这个 __webpack_require__.e 方法的这里创建的，就在下面的这几行代码</span>
            <span class="hljs-keyword">var</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
                installedChunkData = installedChunks[chunkId] = [resolve, reject]; <span class="hljs-comment">//就是这里给数组中加上 resolve, reject~~~</span>
            &#125;); 
            promises.push(installedChunkData[<span class="hljs-number">2</span>] = promise); <span class="hljs-comment">// 这里给数组加上 promise 对象</span>
    
            <span class="hljs-comment">// 所谓 JSONP 就是新建个 script 标签去加载这个 chunkId 对应的文件（你是不是想说：就这？。。。jq 直呼内行）</span>
            <span class="hljs-keyword">var</span> script = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'script'</span>);
            <span class="hljs-keyword">var</span> onScriptComplete;
    
            script.charset = <span class="hljs-string">'utf-8'</span>;
            script.timeout = <span class="hljs-number">120</span>;
            <span class="hljs-keyword">if</span> (__webpack_require__.nc) &#123;
                script.setAttribute(<span class="hljs-string">"nonce"</span>, __webpack_require__.nc);
            &#125;

            <span class="hljs-comment">// 给 script src 属性赋值，浏览器就会去发起一个 get 请求去加载 src 对应的资源；</span>
            <span class="hljs-comment">// 还记得这个方法开头我们说只有 chunkId 0，还有 hash 来着，hash 从哪儿来？这里就是在 jsonpScriptSrc 方法里面拼接的；</span>
            script.src = jsonpScriptSrc(chunkId);
    
            <span class="hljs-comment">// create error before stack unwound to get useful stacktrace later</span>
            <span class="hljs-keyword">var</span> error = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>();
            onScriptComplete = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
                <span class="hljs-comment">// avoid mem leaks in IE.</span>
                script.onerror = script.onload = <span class="hljs-literal">null</span>;
                <span class="hljs-built_in">clearTimeout</span>(timeout);
                <span class="hljs-keyword">var</span> chunk = installedChunks[chunkId];
                <span class="hljs-keyword">if</span>(chunk !== <span class="hljs-number">0</span>) &#123;
                    <span class="hljs-keyword">if</span>(chunk) &#123;
                        <span class="hljs-keyword">var</span> errorType = event && (event.type === <span class="hljs-string">'load'</span> ? <span class="hljs-string">'missing'</span> : event.type);
                        <span class="hljs-keyword">var</span> realSrc = event && event.target && event.target.src;
                        error.message = <span class="hljs-string">'Loading chunk '</span> + chunkId + <span class="hljs-string">' failed.\n('</span> + errorType + <span class="hljs-string">': '</span> + realSrc + <span class="hljs-string">')'</span>;
                        error.name = <span class="hljs-string">'ChunkLoadError'</span>;
                        error.type = errorType;
                        error.request = realSrc;
                        chunk[<span class="hljs-number">1</span>](error);
                    &#125;
                    installedChunks[chunkId] = <span class="hljs-literal">undefined</span>;
                &#125;
            &#125;;
            <span class="hljs-comment">// 人肉处理超时， 120s 后手动超时</span>
            <span class="hljs-keyword">var</span> timeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                onScriptComplete(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'timeout'</span>, <span class="hljs-attr">target</span>: script &#125;);
            &#125;, <span class="hljs-number">120000</span>);
            script.onerror = script.onload = onScriptComplete;

            <span class="hljs-comment">// 把 script 标签插入到 dom 中 </span>
            <span class="hljs-built_in">document</span>.head.appendChild(script);
        &#125;
    &#125;
 
    <span class="hljs-comment">// 调用 Promise.all() 等所有被加载的 chunk 都完成了才会 resolve</span>
    <span class="hljs-comment">// 最后返回的是一个 promise</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all(promises);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结一下上面这段异步按需加载模块的操作：
1）首先源码中 import(c.js).then 被 webpack 处理成了 <code>__webpack_require__.e(chunkId).then(__webpack_require__.bind(null, c.js))</code>
2）__webpack_require__.e 则会通过 JSONP 加载对应的 chunk 并执行，返回加载 chunk 时创建的 promise 对象；
3）上面 1）中的 then 的回调 <code>__webpack_require\__.bind(null, c.js)</code> 接着执行，这个回调的作用其实就是调用 <code>__webpack_require\__</code> 去加载 c.js；
4）接着上面的从 chunk 加载按需加载的 <code>c.js</code>，紧接着再次调用 then 方法，这个 then 方法中的回调才会真正调用 c.js 中的方法，到这里被按需加载的 c.js 中的方法完成调用；</p>
<p>你以为到这里就结束了是么，怎（我）么（也）可（想）能（阿）？</p>
<p>我们来思考一个问题：<code>__webpack_require__</code> 是从 <code>modules</code> 对象或者 <code>installedModules</code> 缓存中获取模块的，那么这个 <code>chunk</code> 代码做了什么，<code>runtime</code> 又做了什么，才使得 <code>then(__webpack_require__.bind(null, c.js))</code> 取到预期的方法呢？</p>
<p>这个问题的答案要着眼于两方面：</p>
<ol>
<li>chunk 里面的代码；</li>
<li>runtime 中 JSONP 处理；</li>
</ol>
<h3 data-id="heading-9">5.2 chunk 概览及 JSONP</h3>
<p>1、chunk 中的代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1. 确保 window[webpackJsonp] 这个数组的存在，如果没有就赋值一个，有的话就取用</span>
(<span class="hljs-built_in">window</span>[<span class="hljs-string">"webpackJsonp"</span>] = <span class="hljs-built_in">window</span>[<span class="hljs-string">"webpackJsonp"</span>] || []).push([[<span class="hljs-number">0</span>],&#123;
  <span class="hljs-string">"./src/c.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;
<span class="hljs-meta">      "use strict"</span>;
      __webpack_require__.r(__webpack_exports__);
      <span class="hljs-comment">/* harmony export (binding) */</span> __webpack_require__.d(__webpack_exports__, <span class="hljs-string">"minus"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> minus; &#125;);
      <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-comment">/*! import() */</span>).then(__webpack_require__.bind(<span class="hljs-literal">null</span>, <span class="hljs-comment">/*! ./b.js */</span> <span class="hljs-string">"./src/b.js"</span>)).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">m</span>) </span>&#123;
        <span class="hljs-keyword">return</span> m.add(<span class="hljs-number">200</span>, <span class="hljs-number">100</span>);
      &#125;);
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">minus</span>(<span class="hljs-params">a, b</span>) </span>&#123;
        <span class="hljs-keyword">return</span> a - b;
      &#125;
  &#125;)
&#125;]);
<span class="hljs-comment">// 2. 接着就是向 window[webpackJsonp] 这个数组中 push 了一项，这里需要重点关注一下这个数组的 push 方法和被 push 的数据结构：</span>
<span class="hljs-comment">// 2.1 这个 push 方法不一定是数组原生的 push 方法（Array.prototype.push），这一点在后面的 runtime 处详述；</span>
<span class="hljs-comment">// 2.2 这个数组项是个数组，数组第一项又是个数组 [0], 第二项是个对象，对象的结构和 modules 相同，key 是资源路径，value 是个webpack 包装函数：</span>
<span class="hljs-comment">// 所以 window[webpackJsonp] 的大致结构：[[[0], &#123; ./src/c.js: (function(module, __....) &#123;&#125;) &#125;]]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、runtime 中的 JSONP 处理</p>
<p>在上面 <code>4.2 runtime 概览（16）</code> 这个小标题，说到了 JSONP 初始化，看看这段代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">modules</span>) </span>&#123;
    <span class="hljs-comment">// ... webpack runtime 代码</span>
    <span class="hljs-keyword">var</span> jsonpArray = <span class="hljs-built_in">window</span>[<span class="hljs-string">"webpackJsonp"</span>] = <span class="hljs-built_in">window</span>[<span class="hljs-string">"webpackJsonp"</span>] || []; <span class="hljs-comment">// 初始化 window[webpackJsonp]，如果没有就初始化</span>
    <span class="hljs-keyword">var</span> oldJsonpFunction = jsonpArray.push.bind(jsonpArray); <span class="hljs-comment">// 暂存数组 push 方法，这个 push 就是 Array.prototype.push</span>
    jsonpArray.push = webpackJsonpCallback; <span class="hljs-comment">// 重写 jsonpArray.push 方法（注意，这么重写不会改写数组原型）</span>
    jsonpArray = jsonpArray.slice(); <span class="hljs-comment">// 赋值 jsonpArrray，这个复制不带 push 方法！</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < jsonpArray.length; i++) webpackJsonpCallback(jsonpArray[i]); <span class="hljs-comment">// 本例子中，执行到这里时，jsonpArray 中是空的，所以这个 for 循环暂时不执行；若chunk先于 bundle 这个入口加载，这个 jsonpArray 里面就不是空的，此时，遍历并调用 webpackJsonpCallback，相当于手动触发 jsonp callback；</span>
    <span class="hljs-keyword">var</span> parentJsonpFunction = oldJsonpFunction; <span class="hljs-comment">// 旧 push 暂存于 parentJsonpFunciton</span>
    <span class="hljs-comment">// ... other runtime processing</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有必要强调一点，在本文对应的 demo 中，runtime 所在的入口 bundle 的执行顺序是先于后面按需加载的 chunk 的。所以执行过这段代码后，<code>window[webpackJsonp]</code> 已经初始化，同时 <code>jsonpArray</code> 的 <code>push</code> 方法被改写成了 <code>webpackJsonpCallback</code> 方法；</p>
<p>所以，等到后面 chunk 被加载回来后，执行 chunk 代码：<code>(window["webpackJsonp"] = window["webpackJsonp"] || []).push([[0],&#123;..</code> 时，执行的这个 push 其实是 <code>webpackJsonpCallback</code> 方法。</p>
<p>你一定在想，为什么会有这个操作？对于我这个搬砖的人来说，只能说：绝！</p>
<p>其实他改写 push 是配合着下面的 for 循环用的，目的在于不管是入口 bundle 先下载还是 chunk 先加载，都能让代码得到正确的执行。先加载 bundle，就是咱们上面一直说的情况，这个不多说，chunk 的 push 方法就是 webpackJsonpCallback 方法，调用 push 就是调用 webpackJsonpCallback。</p>
<p>如果先加载 chunk(例如某些预加载之类的技术下)，此时 chunk 中的代码先执行了，这个时候 chunk 会初始化 <code>window[webpackJsonp]</code> 这个数组，而 push 方法就是原生的数组方法 push，很朴素的把数组项添加到 <code>window[webpackJsonp]</code> 数组中，chunk 的使命暂时完成了；接下就等 bundle 加载并执行 runtime 了，等到执行到上面的 runtime 的时候，<code>window[webpackJsonp]</code> 数组已经被初始化，所以后面对 jsonpArray 的 for 循环就可以工作了，这个时候，对 <code>window[webpackJsonp]</code> 中的每一项调用一次 <code>webpackJsonpCallback</code>；</p>
<p>这就保证了，不管 chunk 何时加载，都能让代码以预期的方式工作。绝，连城诀！接下来看看这个 webpackJsonpCallback 做了些什么吧：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">webpackJsonpCallback</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-comment">// 1. 这个 data 就是上面说 chunk 代码的时 push 的数组项，结构类似：[[[0], &#123; ./src/c.js: (function(module, __....) &#123;&#125;) &#125;]]</span>
    <span class="hljs-keyword">var</span> chunkIds = data[<span class="hljs-number">0</span>]; <span class="hljs-comment">// chunkIds 就是上面的 [0] </span>
    <span class="hljs-keyword">var</span> moreModules = data[<span class="hljs-number">1</span>]; <span class="hljs-comment">// moreModules 就是上面的 &#123; ./src/c.js: (fun....) &#125; 这个对象</span>

    <span class="hljs-comment">// 2. 遍历 chunkIds，如果在 installedChunks 是个非 falsy 的值，说明这个 chunkId 对应的 chunk 正在加载了，</span>
    <span class="hljs-comment">// 把它的 resolve push 到 resolves 这个数组（注意：installedChunks 中若 chunkId 所对应 chunk 正在加载，其value [Promise resolveFn, Promise rejectFn, promsie ]）</span>
    <span class="hljs-comment">// 把 installedChunks[chunkId] 的值修改为 0，标识该 chunk 已经被加载过！</span>
    <span class="hljs-keyword">var</span> moduleId, chunkId, i = <span class="hljs-number">0</span>, resolves = [];
    <span class="hljs-keyword">for</span>(;i < chunkIds.length; i++) &#123;
        chunkId = chunkIds[i];
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Object</span>.prototype.hasOwnProperty.call(installedChunks, chunkId) && installedChunks[chunkId]) &#123;
            resolves.push(installedChunks[chunkId][<span class="hljs-number">0</span>]);
        &#125;
        installedChunks[chunkId] = <span class="hljs-number">0</span>;
    &#125;

    <span class="hljs-comment">// 这里回答：runtime 做了啥，才能让 chunk 代码里面的 module 可以被 runtime 中的 __webpack_require__ 获取到 的问题：</span>
    <span class="hljs-comment">// 是因为在这里会把 chunk 中所携带的 module 整合到 webpack runtime 接收到 modules 对象中，在下一个事件循环中 __webpack_require__ 从 modules 中取自然就可以取到了</span>
    <span class="hljs-keyword">for</span>(moduleId <span class="hljs-keyword">in</span> moreModules) &#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Object</span>.prototype.hasOwnProperty.call(moreModules, moduleId)) &#123;
            modules[moduleId] = moreModules[moduleId];
        &#125;
    &#125;
    
    <span class="hljs-comment">// 3. 这一步就是用来保证 bundle 先执行的时候，由于 runtime 执行，</span>
    <span class="hljs-comment">// 数组 push 被改写成 webpackJsonpCallback 后，chunk 加载后，能够正常的把 chunk 相关信息添加到 window[webpackJsonp] 这个数组中</span>
    <span class="hljs-keyword">if</span>(parentJsonpFunction) parentJsonpFunction(data);

    <span class="hljs-comment">// 4. resolves 中存放的都是加载 chunk时 __webpack_require__.e 方法创建的特殊数组项：</span>
    <span class="hljs-comment">// （形如[Promise resolve, Promise reject, promise]）的第 0 项，即 resolve，</span>
    <span class="hljs-comment">// 它决定了 __webpack_require__.e 方法最后 return 出去的 Promise.all(promise) 的 promise 对象是否 resolve，</span>
    <span class="hljs-comment">// 进而决定了编译后的 a.js 模块中：  __wepack_require__.e(0).then(__webpack_require__.bind(c.js)).then(...) 的执行</span>
    <span class="hljs-comment">// 如果 resolves 不为空，则清空这个队列，使得 __webpack_require__.e 方法最后 return 出去的 Promise.all(promise) promise 得以 resolve </span>
    <span class="hljs-keyword">while</span>(resolves.length) &#123;
        resolves.shift()();
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">6. splitChunks 之后的输出文件</h2>
<h3 data-id="heading-11">6.1 修改项目代码</h3>
<ul>
<li>修改 webpack.config.js 追加 splitChunk 配置(optimization.splitChunks)：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">m1</span>: <span class="hljs-string">'./src/m1.js'</span>,
    <span class="hljs-attr">m2</span>: <span class="hljs-string">'./src/m2.js'</span>
  &#125;,
  <span class="hljs-attr">devtool</span>: <span class="hljs-string">'none'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: __dirname + <span class="hljs-string">'/dist'</span>,
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].[chunkhash:4].js'</span>,
    <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">'[name].[chunkhash:8].js'</span>
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> HtmlWebpackPlugin()],
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@babel/env'</span>]
            &#125;
          &#125;
        ]
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">splitChunks</span>: &#123;
      <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>,
      <span class="hljs-attr">minSize</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">maxSize</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">minChunks</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">automaticNameDelimiter</span>: <span class="hljs-string">'~'</span>,
      <span class="hljs-attr">cacheGroups</span>: &#123;
        <span class="hljs-attr">default</span>: &#123;
          <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>,
          <span class="hljs-attr">minChunks</span>: <span class="hljs-number">2</span>,
          <span class="hljs-attr">priority</span>: -<span class="hljs-number">10</span>
        &#125;
      &#125;
    &#125;,
    <span class="hljs-comment">// runtimeChunk: &#123; name: 'runtime' &#125;</span>
  &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在 src 下追加两个文件m1.js 、m2.js，作为多入口:</li>
</ul>
<p>1、 m1.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; times &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./d'</span>;
<span class="hljs-built_in">console</span>.log(times(<span class="hljs-number">10</span>, <span class="hljs-number">4</span>));

<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、 m2.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; times &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./d'</span>;
<span class="hljs-built_in">console</span>.log(times(<span class="hljs-number">2</span>, <span class="hljs-number">12</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">6.2 打包输出文件</h3>
<p>这两个入口都依赖了 <code>d.js</code> 这个模块，这个模块将会被拆成一个单独的 chunk —— <code>dd~m1~m2.a7ba197d.js</code>；下列就是修改配置后的文件输出：</p>
<ol>
<li>index.html</li>
<li>m1.33c1.js</li>
<li>m2.50e9.js</li>
<li>dd<del>m1</del>m2.a7ba197d.js</li>
</ol>
<p>我们使用的 html-webpack-plugin，它会帮我你把 js 按顺序插入到 html 文件里；这里需要先看下 index.html 代码，关注一下这些 js 被引入的顺序；</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>Webpack App<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"dd~m1~m2.a7ba197d.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"m1.33c1.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"m2.50e9.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显的看出这个公共的 chunk 被最先引入，代码执行的时候也是先去加载并执行它；这和我们前面的例子略有区别，主要体现在：</p>
<ol>
<li>
<p>chunk 被优先引入，而入口 bundle 被后置；</p>
</li>
<li>
<p>在新生成的 bundle m1.xxx.js 和 m2.xxx.js 的 runtime 的最后不再返回 <code>__webpack_require__(入口)</code>，而是返回了 <code>checkDeferredModules([m1.33c1.js, dd~m1....js])</code>；</p>
</li>
<li>
<p>runtime 新增 <code>checkDeferredModules</code> 方法，同时 webpackJsonpCallback 中也作出了相应的调整，在末尾增加了两行代码：</p>
</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">deferredModules.push.apply(deferredModules, executeModules || []);
<span class="hljs-keyword">return</span> checkDeferredModules();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">6.3 执行过程分析</h3>
<p>1、首先加载并执行 <code>dd~m1~m2.a7ba197d.js</code> 文件，代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-built_in">window</span>[<span class="hljs-string">"webpackJsonp"</span>] = <span class="hljs-built_in">window</span>[<span class="hljs-string">"webpackJsonp"</span>] || []).push([[<span class="hljs-string">"dd~m1~m2"</span>],&#123;
  <span class="hljs-string">"./src/d.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;
<span class="hljs-meta">      "use strict"</span>;
      __webpack_require__.r(__webpack_exports__);
      <span class="hljs-comment">/* harmony export (binding) */</span> __webpack_require__.d(__webpack_exports__, <span class="hljs-string">"L"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> L; &#125;);
      <span class="hljs-comment">/* harmony export (binding) */</span> __webpack_require__.d(__webpack_exports__, <span class="hljs-string">"times"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> times; &#125;);
      <span class="hljs-keyword">var</span> L = <span class="hljs-string">'Aragaki Yui'</span>;
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">times</span>(<span class="hljs-params">a, b</span>) </span>&#123;
        <span class="hljs-keyword">return</span> a * b;
      &#125;
  &#125;)
&#125;]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分析发现，这个 chunk 和前面例子中按需加载的 chunk 没有特别大的差别，仍然是通过向 <code>window[webpackJsonp]</code> 中添加数组项；值得强调的是，这里因为 chunk 先于入口加载并执行，所以这个 <code>window[webpackJsonp]</code> 是在 chunk 中初始化，同时这个 <code>push</code> 方法也是数组原生的 <code>push</code> 方法；</p>
<p>2、加载入口文件 <code>m1.33c1.js</code> ，代码如下：</p>
<p>我们简化了这个入口文件，把注释和与前面未进行 splitChunks 相同的方法和变量删除掉，我们聚焦于不同点：</p>
<ul>
<li>变量 deferredModules</li>
<li>webpackJsonpCallback 方法</li>
<li>checkDeferredModules 方法</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">modules</span>) </span>&#123; <span class="hljs-comment">// webpackBootstrap</span>
<span class="hljs-comment">// install a JSONP callback for chunk loading</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">webpackJsonpCallback</span>(<span class="hljs-params">data</span>) </span>&#123;
<span class="hljs-comment">// ... 同前 webpackJsonpCallback 逻辑，略去</span>
        <span class="hljs-keyword">var</span> executeModules = data[<span class="hljs-number">2</span>];

<span class="hljs-comment">// 这一行代码目前还没看出啥作用，看起来是这个 webpackJsonpCallback 被调用时，比如 window[webpackJsonp].push 或者 </span>
        <span class="hljs-comment">// webpackJsonpCallback(jsonpArray[i]) 的时候可以传入一个 defferedModule 项；</span>
        <span class="hljs-comment">// webpack 的原文注释字面意思是"从已经加载过 chunk 中把 entry modules 加入到 deferredModules"</span>
deferredModules.push.apply(deferredModules, executeModules || []);

<span class="hljs-comment">// webpackJsonpCallback 是加载 chunk 后执行的，意在每次加载 chunk 后都 check 一下 defrredModules 中的依赖们是否加载完了，加载完了就调用入口 module 执行；</span>
        <span class="hljs-comment">// 这样有个好处就是不管加载入口还是先加载依赖，最后的代码执行顺序都能得正确执行；</span>
<span class="hljs-keyword">return</span> checkDeferredModules();
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkDeferredModules</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 方法作用：</span>
        <span class="hljs-comment">// deferredModules 中的每一项都是一个数组形如：[入口 chunk1, 依赖chunk2, 依赖 chunk3...]</span>
        <span class="hljs-comment">// checkDeferredModules 的作用就是检查 defferredModules 中的每一项，的依赖部分（从第二项开始）是否都已经安装完成（installedChunks[chunkIed] === 0）</span>
        <span class="hljs-comment">// 如果都安装完成了，则调用数组项的入口 chunk</span>


        <span class="hljs-comment">// 变量 result，用于接收入口 chunk 执行后的结果，最后返回它</span>
<span class="hljs-keyword">var</span> result;

        <span class="hljs-comment">// 遍历 deferredModules，这个 deferredModules 可以有很多项，所以需要遍历一下</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < deferredModules.length; i++) &#123;
<span class="hljs-keyword">var</span> deferredModule = deferredModules[i]; <span class="hljs-comment">// defferredModule 形如： [入口 chunk1, 依赖chunk2, 依赖 chunk3...]</span>
<span class="hljs-keyword">var</span> fulfilled = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 标识符，标识所有的依赖 chunk 都已经被安装</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> j = <span class="hljs-number">1</span>; j < deferredModule.length; j++) &#123;
<span class="hljs-keyword">var</span> depId = deferredModule[j];
<span class="hljs-keyword">if</span>(installedChunks[depId] !== <span class="hljs-number">0</span>) fulfilled = <span class="hljs-literal">false</span>; <span class="hljs-comment">// installedChunks 中对应这一项的值不为 0 说明没有安装完，安装完这个值就是 0 了，关于 installedChunks 在上文 4.2 runtime 概览（3、installedChunks）</span>
&#125;
<span class="hljs-comment">// 经历了上面的 for 循环，如果 fulfilled 还是 true 说明所有的依赖 chunk 都已经加载完成了，就可以执行入口 chunk 了</span>
<span class="hljs-keyword">if</span>(fulfilled) &#123;
                <span class="hljs-comment">// 此时从 deferredModules（注意有 s，不是 deferredMdoule） 中删除掉这一项，因为这一项已经 check 过了，</span>
                <span class="hljs-comment">// 下面一行代码立刻就会执行这一项的入口，所以 checkDeferredModules 对它的工作已经完成了；</span>
                <span class="hljs-comment">// 如果不删会怎样？后面只要有新的入口，比如 m2.js，添加到 defferedModules 数组就会触发重新 check，如果不删除就会让已经执行过 chunk 再执行一遍，相当于同一段逻辑执行两次；</span>
deferredModules.splice(i--, <span class="hljs-number">1</span>);
                <span class="hljs-comment">// __webpack_require__ 调用入口模块，并将其返回结果赋值给 result </span>
result = __webpack_require__(__webpack_require__.s = deferredModule[<span class="hljs-number">0</span>]);
&#125;
&#125;
        <span class="hljs-comment">// 开开心心拿着入口 module 返回结果返回</span>
<span class="hljs-keyword">return</span> result;
&#125;

    <span class="hljs-comment">// 这个变量时因为 slitChunks 多出来的，这个变量是一个数组，其第一项表示要加载的 module，从第二项开始后面的都是第一项依赖的模块；</span>
    <span class="hljs-comment">// 从这个例子上来说，第一项是入口 chunk（例如本例中的 m1.xxx.js），后面的是入口依赖的 chunk（如 dd~m1~m2.....js） </span>
    <span class="hljs-comment">// 现在这个数组是空的，什么时候里面才会值呢？在 runtime 结尾处，会把入口 ./src/m1.js 和 依赖的 dd~m1~m2 push 进去；</span>
    <span class="hljs-keyword">var</span> deferredModules = [];

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">__webpack_require__</span>(<span class="hljs-params">moduleId</span>) </span>&#123; <span class="hljs-comment">/* 同前 __webpack_require__ 略去 */</span> &#125;
    
<span class="hljs-comment">// JSONP 初始化.....</span>
<span class="hljs-keyword">var</span> jsonpArray = <span class="hljs-built_in">window</span>[<span class="hljs-string">"webpackJsonp"</span>] = <span class="hljs-built_in">window</span>[<span class="hljs-string">"webpackJsonp"</span>] || [];
<span class="hljs-keyword">var</span> oldJsonpFunction = jsonpArray.push.bind(jsonpArray);
jsonpArray.push = webpackJsonpCallback;
jsonpArray = jsonpArray.slice();
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < jsonpArray.length; i++) webpackJsonpCallback(jsonpArray[i]);
<span class="hljs-keyword">var</span> parentJsonpFunction = oldJsonpFunction;

<span class="hljs-comment">// 这里！把入口 ./src/m1.js 和 依赖的 chunk pushu 到 deferredModules 中；</span>
    <span class="hljs-comment">// 紧接着调用 checkDeferredModules 方法，接着去这个方法里面看看这个方法都发生了啥</span>
deferredModules.push([<span class="hljs-string">"./src/m1.js"</span>,<span class="hljs-string">"dd~m1~m2"</span>]);
<span class="hljs-keyword">return</span> checkDeferredModules();
&#125;)
<span class="hljs-comment">/************************************************************************/</span>
(&#123;
  <span class="hljs-comment">// 这个对象也是 modules </span>
  <span class="hljs-string">"./src/m1.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;
<span class="hljs-meta">    "use strict"</span>;
    __webpack_require__.r(__webpack_exports__);
    <span class="hljs-comment">/* harmony import */</span> <span class="hljs-keyword">var</span> _d__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(<span class="hljs-comment">/*! ./d */</span> <span class="hljs-string">"./src/d.js"</span>);
    
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>(_d__WEBPACK_IMPORTED_MODULE_0__[<span class="hljs-string">"times"</span>])(<span class="hljs-number">10</span>, <span class="hljs-number">4</span>));
  &#125;)

&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个入口 m2.js 同理，在此不再赘述。</p>
<ul>
<li>TIPS: 关于先加载 chunk 还是先加载入口，可以去 <code>index.html</code> 中调整一下 chunk 和 入口的 script 标签顺序，就可以发先控制台的输出仍然是正常的；</li>
</ul>
<h2 data-id="heading-14">7. 总结</h2>
<p>本篇详述了 webpack 打包输出文件，又赏析了他设计的精妙：</p>
<p>1）巧妙实现 CMD 规范 <code>__webpack_require__</code>，<code>__webpack_require__.d</code>，shim 浏览器的模块系统；</p>
<p>2）通过 runtime 的 改写 <code>push</code> 方法 并结合 for 循环调用 webpackJsonpCallback 实现无论入口和chunk的顺序如何，最后代码都能顺利执行</p>
<p>3）webpack 实现细节的精妙，比如 installedChunked 的数据结构的设计，只有一种正在加载的是数组，其余都是 falsy 值；</p>
<p>4）本篇篇幅有点长，建议阅读 2-3 遍；</p>
<p>5）码字不容易，看完了，点个赞呗</p></div>  
</div>
            