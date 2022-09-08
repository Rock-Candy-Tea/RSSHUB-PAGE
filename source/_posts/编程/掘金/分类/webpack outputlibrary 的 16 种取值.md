
---
title: 'webpack output.library 的 16 种取值'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1609'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 04:54:34 GMT
thumbnail: 'https://picsum.photos/400/300?random=1609'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划一期挑战——瓜分10万奖池，这是我的第1篇文章，<a href="https://juejin.cn/post/7138637426922094605?utm_source=xitongxiaoxi&utm_medium=push&utm_campaign=jinshijihua01" target="_blank" title="https://juejin.cn/post/7138637426922094605?utm_source=xitongxiaoxi&utm_medium=push&utm_campaign=jinshijihua01">点击查看活动详情</a>。</p>
<p>在项目开发中使用 webpack 打包前端代码，对 output.library 配置项总是不求甚解，只知道将代码打包成 npm 库的时候要配置它。这段时间又要开发组件库，借助这次机会对 output.library 求甚解。</p>
<p>配置过 output.library 的同学应该也配置过 output.libraryTarget，在开发库的时候总是一起配置它们。由于在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Fconfiguration%2Foutput%2F%23outputlibrarytarget" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/configuration/output/#outputlibrarytarget" ref="nofollow noopener noreferrer">webpack文档</a>中推荐使用 output.library.type 代替 output.libraryTarget，所以本文只介绍 output.library。</p>
<blockquote>
<p>本文 webpack 的版本是 5.74.0。</p>
</blockquote>
<h2 data-id="heading-0">前置准备</h2>
<p>入口代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack 的配置如下，后续我们只关注 library 字段。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./index.js'</span>,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">"none"</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'main.js'</span>,
    <span class="hljs-comment">// library: 'MyLibrary',</span>
    <span class="hljs-attr">path</span>: path.<span class="hljs-title function_">resolve</span>(__dirname, <span class="hljs-string">'dist'</span>),
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包输出的文件中，除了包含 index.js 中的源码，还包含 webpack 运行时，代码如下，后续将不再介绍它。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> __webpack_require__ = &#123;&#125;;
<span class="hljs-comment">// 将 definition 中的属性添加到 exports 上</span>
__webpack_require__.<span class="hljs-property">d</span> = <span class="hljs-function">(<span class="hljs-params"><span class="hljs-built_in">exports</span>, definition</span>) =></span> &#123;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> definition) &#123;
    <span class="hljs-keyword">if</span>(__webpack_require__.<span class="hljs-title function_">o</span>(definition, key) && !__webpack_require__.<span class="hljs-title function_">o</span>(<span class="hljs-built_in">exports</span>, key)) &#123;
            <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(<span class="hljs-built_in">exports</span>, key, &#123; <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">get</span>: definition[key] &#125;);
         &#125;
&#125;
&#125;;
<span class="hljs-comment">// 判断 obj 上是否有 prop</span>
__webpack_require__.<span class="hljs-property">o</span> = <span class="hljs-function">(<span class="hljs-params">obj, prop</span>) =></span> (<span class="hljs-title class_">Object</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">hasOwnProperty</span>.<span class="hljs-title function_">call</span>(obj, prop))

<span class="hljs-comment">// 在 exports 上定义 __esModule 属性</span>
__webpack_require__.<span class="hljs-property">r</span> = <span class="hljs-function">(<span class="hljs-params"><span class="hljs-built_in">exports</span></span>) =></span> &#123;
<span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> <span class="hljs-title class_">Symbol</span> !== <span class="hljs-string">'undefined'</span> && <span class="hljs-title class_">Symbol</span>.<span class="hljs-property">toStringTag</span>) &#123;
        <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(<span class="hljs-built_in">exports</span>, <span class="hljs-title class_">Symbol</span>.<span class="hljs-property">toStringTag</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'Module'</span> &#125;);
&#125;
<span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(<span class="hljs-built_in">exports</span>, <span class="hljs-string">'__esModule'</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-literal">true</span> &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FQxQstar%2Fwebpack.library" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/QxQstar/webpack.library" ref="nofollow noopener noreferrer">点这里</a>得到文本的代码。</p>
<h2 data-id="heading-1">不配置 library</h2>
<p>在介绍 library 各配置项的作用前，先看一下不配置 library 时的打包结果。如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 自执行函数</span>
(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
    __webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);  
    __webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
       <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* export default binding */</span> __WEBPACK_DEFAULT_EXPORT__)
    &#125;); 
    <span class="hljs-comment">// 打包入口导出的函数 </span>
    <span class="hljs-keyword">function</span> <span class="hljs-title function_">__WEBPACK_DEFAULT_EXPORT__</span>(<span class="hljs-params">a, b</span>) &#123;
        <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
    &#125;    
&#125;)()
;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上述代码可以看出，不配置 library 时，<code>__WEBPACK_DEFAULT_EXPORT__</code> 函数没有被公开，在库外部的任何位置都访问不到它。</p>
<p>下面将介绍配置 library 时的各种情况，library 可接受的数据类型是 <code>string | string[] | object</code>。<code>string</code> 是 <code>object</code> 类型的简写形式，当值为 <code>object</code> 类型时，object 中能包含的属性有 name、type、export、auxiliaryComment 和 umdNamedDefine。本文将重点放在 type 字段上，它决定如何公开当前库，取值基本固定，name 字段可以是任何字符串，它用来指定库的名称。</p>
<h2 data-id="heading-2">library.type = var(默认值)</h2>
<p>将 library 的值改成 <code>&#123;type: 'var', name: 'MyLibrary'&#125;</code>, 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> <span class="hljs-title class_">MyLibrary</span>;
(<span class="hljs-function">() =></span> &#123; 
<span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
__webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
__webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
   <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
&#125;);
<span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
&#125;

<span class="hljs-title class_">MyLibrary</span> = __webpack_exports__;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上述代码可以看出，通过<code>MyLibrary</code>能访问到<code>add</code>函数，当不能保证<code>MyLibrary</code>在全局变量上。</p>
<h2 data-id="heading-3">library.type = window</h2>
<p>将 library 的值改成 <code>&#123;type: 'window', name: 'MyLibrary'&#125;</code>, 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
__webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
 __webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
   <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
 &#125;);
<span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
&#125;

<span class="hljs-variable language_">window</span>.<span class="hljs-property">MyLibrary</span> = __webpack_exports__;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上述代码可以看出，通过<code>window.MyLibrary</code>能访问到<code>add</code>函数。</p>
<h2 data-id="heading-4">library.type = module</h2>
<p>将 library 的值改成 <code>&#123;type: 'module'&#125;</code>, 此时还要 experiments.outputModule 设置为 true , 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
__webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
__webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
 <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
&#125;);
<span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
&#125;

<span class="hljs-keyword">var</span> __webpack_exports__default = __webpack_exports__[<span class="hljs-string">"default"</span>];
<span class="hljs-keyword">export</span> &#123; __webpack_exports__default <span class="hljs-keyword">as</span> <span class="hljs-keyword">default</span> &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时不存在闭包，并且能用 es modules 将库导入。</p>
<h2 data-id="heading-5">library.type = this</h2>
<p>将 library 的值改成 <code>&#123;type: 'this', name: 'MyLibrary'&#125;</code>, 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
__webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
__webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
  <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
&#125;);
<span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
&#125;

<span class="hljs-variable language_">this</span>.<span class="hljs-property">MyLibrary</span> = __webpack_exports__;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时通过 this.MyLibrary 能访问到 add 函数</p>
<h2 data-id="heading-6">library.type = self</h2>
<p>将 library 的值改成 <code>&#123;type: 'self', name: 'MyLibrary'&#125;</code>, 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
__webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
__webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
  <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
&#125;);
<span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
&#125;

self.<span class="hljs-property">MyLibrary</span> = __webpack_exports__;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时通过 self.MyLibrary 可访问到 add 函数，在浏览器环境的全局上下文中 self 等于 window</p>
<h2 data-id="heading-7">library.type = global</h2>
<p>将 library 的值改成 <code>&#123;type: 'global', name: 'MyLibrary'&#125;</code>，此时 MyLibrary 会被分配到全局对象，全局对象会根据<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Fconfiguration%2Ftarget%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/configuration/target/" ref="nofollow noopener noreferrer">target</a>值的不同而不同，全部对象可能的值是 self、global 或 globalThis。当 target 的值为 web（默认值），代码结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
__webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
__webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
  <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
&#125;);
<span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
&#125;

self.<span class="hljs-property">MyLibrary</span> = __webpack_exports__;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时的打包结果与 library.type = self 结果一样。</p>
<h2 data-id="heading-8">library.type = commonjs</h2>
<p>将 library 的值改成 <code>&#123;type: 'commonjs', name: 'MyLibrary'&#125;</code>, 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
__webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
__webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
 <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
&#125;);
<span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
&#125;

<span class="hljs-built_in">exports</span>.<span class="hljs-property">MyLibrary</span> = __webpack_exports__;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>顾名思义，如果公开的库要在 CommonJS 环境中使用，那么将 library.type 设置成 commonjs，此时 MyLibrary 分配给了 exports</p>
<h2 data-id="heading-9">library.type = commonjs2</h2>
<p>将 library 的值改成 <code>&#123;type: 'commonjs2', name: 'MyLibrary'&#125;</code>, 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
__webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
__webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
  <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
&#125;);
<span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
&#125;

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span>.<span class="hljs-property">MyLibrary</span> = __webpack_exports__;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时 MyLibrary 分配给了 module.exports，如果公开的库要在 Node.js 环境中运行，推荐将 library.type 设置为 commonjs2。commonjs 和 commonjs2 很像，但它们有一些不同，简单的说 CommonJs 规范只定义了 exports ，但是 module.exports 被 node.js 和一些其他实现 CommonJs 规范的模块系统所使用，commonjs 表示纯 CommonJs，commonjs2 在 CommonJs 的基础上增加了 module.exports。</p>
<h2 data-id="heading-10">library.type = commonjs-static</h2>
<p>将 library 的值改成 <code>&#123;type: 'commonjs-module'&#125;</code>，注意此时没有设置 name 属性, 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
__webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
__webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
 <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
&#125;);
<span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
&#125;

<span class="hljs-built_in">exports</span>[<span class="hljs-string">"default"</span>] = __webpack_exports__[<span class="hljs-string">"default"</span>];
<span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(<span class="hljs-built_in">exports</span>, <span class="hljs-string">"__esModule"</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-literal">true</span> &#125;);
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 CommonJS 模块中使用库</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> add = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./dist/main.js'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 ESM 模块中使用库</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> add <span class="hljs-keyword">from</span> <span class="hljs-string">'./dist/main.js'</span>; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当源代码是用 ESM 编写的，但你的库要同时兼容 CJS 和 ESM 时，library.type = commonjs-static将很有用。</p>
<h2 data-id="heading-11">library.type = amd</h2>
<p>将 library 的值改成 <code>&#123;type: 'amd', name: 'MyLibrary'&#125;</code>, 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title function_">define</span>(<span class="hljs-string">"MyLibrary"</span>, [], <span class="hljs-function">() =></span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-comment">/******/</span> (<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
    __webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
    __webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
    <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
    &#125;);
    <span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
        <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
    &#125;

    <span class="hljs-keyword">return</span> __webpack_exports__;
    &#125;)()
    ;
&#125;);;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当你的库要在 amd 模块中使用时，将 library.type 设置成 amd</p>
<h2 data-id="heading-12">library.type = umd</h2>
<p>将 library 的值改成 <code>&#123;type: 'umd', name: 'MyLibrary'&#125;</code>, 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-keyword">function</span> <span class="hljs-title function_">webpackUniversalModuleDefinition</span>(<span class="hljs-params">root, factory</span>) &#123;
<span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">exports</span> === <span class="hljs-string">'object'</span> && <span class="hljs-keyword">typeof</span> <span class="hljs-variable language_">module</span> === <span class="hljs-string">'object'</span>)  <span class="hljs-comment">// commonjs2</span>
<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = <span class="hljs-title function_">factory</span>();
<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> define === <span class="hljs-string">'function'</span> && define.<span class="hljs-property">amd</span>) <span class="hljs-comment">// amd</span>
<span class="hljs-title function_">define</span>([], factory);
<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">exports</span> === <span class="hljs-string">'object'</span>) <span class="hljs-comment">// commonjs</span>
<span class="hljs-built_in">exports</span>[<span class="hljs-string">"MyLibrary"</span>] = <span class="hljs-title function_">factory</span>();
<span class="hljs-keyword">else</span> <span class="hljs-comment">// 全局变量</span>
root[<span class="hljs-string">"MyLibrary"</span>] = <span class="hljs-title function_">factory</span>();
&#125;)(self, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-comment">/******/</span> (<span class="hljs-function">() =></span> &#123; <span class="hljs-comment">// webpackBootstrap</span>
        <span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
        __webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
        __webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
            <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
        &#125;);
        <span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
            <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
        &#125;

        <span class="hljs-keyword">return</span> __webpack_exports__;
    &#125;)()
    ;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时你的库能用 Commonjs、AMD 和全局变量引入，在开发库时将 library.type 设置成 umd 很常见。</p>
<h2 data-id="heading-13">library.type = assign</h2>
<p>将 library 的值改成 <code>&#123;type: 'assign', name: 'MyLibrary'&#125;</code>, 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function">() =></span> &#123;

<span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
<span class="hljs-comment">// This entry need to be wrapped in an IIFE because it need to be in strict mode.</span>
(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-string">"use strict"</span>;
    __webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
    __webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
      <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
    &#125;);
    <span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
        <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
    &#125;
&#125;)();

<span class="hljs-title class_">MyLibrary</span> = __webpack_exports__;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这将生成一个隐含的全局变量 MyLibrary，通过 MyLibrary 能访问 add 函数，它有可能覆盖一个现有值，因此要小心使用。</p>
<h2 data-id="heading-14">library.type = assign-properties</h2>
<p>将 library 的值改成 <code>&#123;type: 'assign-properties', name: 'MyLibrary'&#125;</code>, 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
    <span class="hljs-comment">// This entry need to be wrapped in an IIFE because it need to be in strict mode.</span>
    (<span class="hljs-function">() =></span> &#123;
    <span class="hljs-string">"use strict"</span>;
    __webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
    __webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
      <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
    &#125;);
    <span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
        <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
    &#125;
    
    &#125;)();
    
    <span class="hljs-keyword">var</span> __webpack_export_target__ = (<span class="hljs-title class_">MyLibrary</span> = <span class="hljs-keyword">typeof</span> <span class="hljs-title class_">MyLibrary</span> === <span class="hljs-string">"undefined"</span> ? &#123;&#125; : <span class="hljs-title class_">MyLibrary</span>);
    <span class="hljs-comment">// 将 __webpack_exports__ 上的属性转移到 __webpack_export_target__ 上。</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i <span class="hljs-keyword">in</span> __webpack_exports__) __webpack_export_target__[i] = __webpack_exports__[i];
    <span class="hljs-keyword">if</span>(__webpack_exports__.<span class="hljs-property">__esModule</span>) <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(__webpack_export_target__, <span class="hljs-string">"__esModule"</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-literal">true</span> &#125;);
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它与 assign 类似，但更安全，如果 MyLibrary 存在，那么它将重用 MyLibrary，而非覆盖。</p>
<h2 data-id="heading-15">library.type = jsonp</h2>
<p>将 library 的值改成 <code>&#123;type: 'jsonp', name: 'MyLibrary'&#125;</code>, 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title class_">MyLibrary</span>((<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
    __webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
    __webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
    <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
    &#125;);
    <span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
        <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
    &#125;

    <span class="hljs-keyword">return</span> __webpack_exports__;
&#125;)()
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时入口的源码在 jsonp 的包裹器中，这种情况要确保 MyLibrary 函数存在。</p>
<h2 data-id="heading-16">library.type = system</h2>
<p>将 library 的值改成 <code>&#123;type: 'system', name: 'MyLibrary'&#125;</code>, 打包结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title class_">System</span>.<span class="hljs-title function_">register</span>(<span class="hljs-string">"MyLibrary"</span>, [], <span class="hljs-keyword">function</span>(<span class="hljs-params">__WEBPACK_DYNAMIC_EXPORT__, __system_context__</span>) &#123;
<span class="hljs-keyword">return</span> &#123;
<span class="hljs-attr">execute</span>: <span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) &#123;
<span class="hljs-title function_">__WEBPACK_DYNAMIC_EXPORT__</span>(
        (<span class="hljs-function">() =></span> &#123; 
            <span class="hljs-keyword">var</span> __webpack_exports__ = &#123;&#125;;
            __webpack_require__.<span class="hljs-title function_">r</span>(__webpack_exports__);
            __webpack_require__.<span class="hljs-title function_">d</span>(__webpack_exports__, &#123;
            <span class="hljs-string">"default"</span>: <span class="hljs-function">() =></span> (<span class="hljs-comment">/* binding */</span> add)
            &#125;);
            <span class="hljs-keyword">function</span> <span class="hljs-title function_">add</span>(<span class="hljs-params">a, b</span>) &#123;
                <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(a + b)
            &#125;

            <span class="hljs-keyword">return</span> __webpack_exports__;
        &#125;)()
      );
    &#125;
&#125;;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将你的库公开为一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsystemjs%2Fsystemjs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/systemjs/systemjs" ref="nofollow noopener noreferrer">System</a> 模块。</p>
<h2 data-id="heading-17">总结</h2>
<p>当你的库导出的内容需要在另外的地方（通常是另一个项目）访问，那么你应该给 webpack 配置 library 字段，library 究竟要配置成什么值，这取决于你希望你的库怎么被引入。</p></div>  
</div>
            