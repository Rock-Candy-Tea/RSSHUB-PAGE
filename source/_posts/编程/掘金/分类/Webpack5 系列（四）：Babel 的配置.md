
---
title: 'Webpack5 系列（四）：Babel 的配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7755'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 01:46:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=7755'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、前言</h1>
<p>上一篇讲到如何<a href="https://juejin.cn/post/6997009154351038494" target="_blank" title="https://juejin.cn/post/6997009154351038494">配置一个基本的开发环境</a>。
本篇将介绍对于项目中 JS 文件的处理。</p>
<h1 data-id="heading-1">二、babel-loader</h1>
<p>index.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 箭头函数</span>
<span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a + b;

<span class="hljs-comment">// Promise 对象</span>
<span class="hljs-keyword">const</span> promise1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>));
  &#125;, <span class="hljs-number">1000</span>);
&#125;);

<span class="hljs-keyword">const</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(add(<span class="hljs-number">3</span>, <span class="hljs-number">4</span>));
  &#125;, <span class="hljs-number">1000</span>);
&#125;);

<span class="hljs-keyword">const</span> promise3 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(add(<span class="hljs-number">5</span>, <span class="hljs-number">6</span>));
  &#125;, <span class="hljs-number">1000</span>);
&#125;);

<span class="hljs-built_in">Promise</span>.all([promise1, promise2, promise3]).then(<span class="hljs-function"><span class="hljs-params">values</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(values); <span class="hljs-comment">// [3, 7, 11]</span>
&#125;);

<span class="hljs-comment">// 实例方法：Array.prototype.includes()</span>
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>];
<span class="hljs-built_in">console</span>.log(arr.includes(<span class="hljs-number">3</span>)); <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> root = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>);
root.innerHTML = add(<span class="hljs-number">1</span>, <span class="hljs-number">3</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有一些版本的浏览器对于JS新的语法(例如 ES6+)的支持不好，这时就需要将新的语法转换成 ES5 标准的语法，让浏览器正常识别它们，保证程序的稳定运行。</p>
<p>为了实现这种转换，我们该怎么办呢？<strong>用 Babel</strong>，它会把新语法转换为旧语法。</p>
<h2 data-id="heading-2">1. 依赖安装</h2>
<p>安装：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install -D babel-loader @babel/core @babel/preset-env
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">2. Loader 配置</h2>
<p>webpack.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>: &#123;
  <span class="hljs-attr">rules</span>: [
    &#123;
      <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.m?js$/</span>,
      exclude: <span class="hljs-regexp">/node_modules/</span>,
      use: &#123;
        <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>
      &#125;
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 babel 的配置，我们一般放在 babel.config.json 中，在根目录中新建 babel.config.json。</p>
<h1 data-id="heading-4">三、Babel 的配置</h1>
<h2 data-id="heading-5">1. 一般情况下的 babel 配置</h2>
<p>babel.config.json</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"presets"</span>: [
    [<span class="hljs-string">"@babel/preset-env"</span>, &#123;
      <span class="hljs-attr">"useBuiltIns"</span>: <span class="hljs-string">"usage"</span>, <span class="hljs-comment">// 按需引入 corejs 中的模块 </span>
      <span class="hljs-attr">"corejs"</span>: <span class="hljs-number">3</span>, <span class="hljs-comment">// 核心 js 版本</span>
      <span class="hljs-attr">"targets"</span>: <span class="hljs-string">"> 0.25%, not dead"</span> <span class="hljs-comment">// 浏览器支持范围</span>
    &#125;]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还需要下载的依赖：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm i core-js@3 --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：</strong> 必须要配置 <strong>useBuiltIns</strong>，如果不配置，babel 将不会处理 Promise、Map、Set、Symbol 等全局对象；<strong>corejs</strong> 也要同时配置，2 的版本可以处理全局对象，但实例方法并不处理，所以这里用 3 的版本。</p>
<h2 data-id="heading-6">2. 最佳的 babel 配置</h2>
<p>如果在写一个库时，最好添加上插件 —— <strong>babel/plugin-transform-runtime</strong>，配置如下：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"presets"</span>: [
    [<span class="hljs-string">"@babel/preset-env"</span>, &#123;
      <span class="hljs-attr">"targets"</span>: <span class="hljs-string">"> 0.25%, not dead"</span>
    &#125;]
  ],
  <span class="hljs-attr">"plugins"</span>: [
    <span class="hljs-comment">// 不污染全局，在运行时加载</span>
    [<span class="hljs-string">"@babel/plugin-transform-runtime"</span>, &#123;
      <span class="hljs-attr">"corejs"</span>: <span class="hljs-number">3</span>
    &#125;]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还需要下载的依赖：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install --save-dev @babel/plugin-transform-runtime
npm install --save @babel/runtime
npm install --save @babel/runtime-corejs3
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">四、最后的备注</h2>
<p>Babel 版本更新后，很多内容已经发生变化，官方文档也是晦涩难读，而中文网上的文章很多都已经过时，好在我看到了一位大佬的文章，这才让我对 @babel/preset-env 和 @babel/plugin-transform-runtime 有了基本的认识。文章 link 放在文末，请自行阅读。</p>
<ol>
<li>@babel/preset-env just transforms code with <strong>syntax</strong>, if we don’t config <strong>useBuiltIns</strong>.</li>
<li>@babel/transform-runtime can provide re-use helpers, but <strong>don’t</strong> polyfill by default.</li>
<li>Most situation best config: use @babel/preset-env transforms syntax. use @babel/transform-runtime avoid duplicate code, and config corejs: 3 to polyfill.</li>
</ol>
<p>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zzuu666.com%2Farticles%2F9" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zzuu666.com/articles/9" ref="nofollow noopener noreferrer">www.zzuu666.com/articles/9</a></p></div>  
</div>
            