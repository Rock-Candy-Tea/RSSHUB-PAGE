
---
title: 'webpack打包原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3891'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 00:48:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=3891'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>webpack是一个<code>打包模块的机制</code>，只是把依赖的模块转化成可以代表这些包的静态文件。并不是什么commonjs或者amd之类的模块化规范。webpack就是识别你的 入口文件,识别你的模块依赖，来打包你的代码。至于你的代码使用的是commonjs还是amd或者es6的import,webpack都会对其进行分析,来获取代码的依赖。<code>webpack做的就是分析代码、转换代码、编译代码、输出代码。</code>webpack本身是一个node的模块，所以<code>webpack.config.js</code>是以commonjs形式书写的(node中的模块化是commonjs规范的)</p>
<p>webpack中每个模块有一个唯一的id，是从0开始递增的。整个打包后的<code>bundle.js</code>是一个匿名函数自执行。参数则为一个数组。数组的每一项都为个function。function的内容则为每个模块的内容，并<code>按照require的顺序</code>排列。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>:<span class="hljs-string">'./a.js'</span>,
  <span class="hljs-attr">output</span>:&#123;
    <span class="hljs-attr">filename</span>:<span class="hljs-string">'bundle.js'</span>
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// a.js</span>
<span class="hljs-keyword">var</span> b = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./b.js'</span>);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span>);

b.b1();
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// b.js</span>
<span class="hljs-built_in">exports</span>.b1 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b1'</span>)
&#125;;

<span class="hljs-built_in">exports</span>.b2 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b2'</span>)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// bundle.js</span>
(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">modules</span>) </span>&#123; <span class="hljs-comment">// webpackBootstrap</span>
   <span class="hljs-comment">// The module cache</span>
   <span class="hljs-keyword">var</span> installedModules = &#123;&#125;;

   <span class="hljs-comment">// The require function</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">__webpack_require__</span>(<span class="hljs-params">moduleId</span>) </span>&#123;
       <span class="hljs-comment">// Check if module is in cache</span>
       <span class="hljs-keyword">if</span>(installedModules[moduleId])
           <span class="hljs-keyword">return</span> installedModules[moduleId].exports;
       <span class="hljs-comment">// Create a new module (and put it into the cache)</span>
       <span class="hljs-keyword">var</span> <span class="hljs-built_in">module</span> = installedModules[moduleId] = &#123;
          <span class="hljs-attr">exports</span>: &#123;&#125;,
          <span class="hljs-attr">id</span>: moduleId,
          <span class="hljs-attr">loaded</span>: <span class="hljs-literal">false</span>
       &#125;;

     <span class="hljs-comment">// Execute the module function</span>
      modules[moduleId].call(<span class="hljs-built_in">module</span>.exports, <span class="hljs-built_in">module</span>, <span class="hljs-built_in">module</span>.exports,__webpack_require__);

      <span class="hljs-comment">// Flag the module as loaded</span>
     <span class="hljs-built_in">module</span>.loaded = <span class="hljs-literal">true</span>;

      <span class="hljs-comment">// Return the exports of the module</span>
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">module</span>.exports;
   &#125;


  <span class="hljs-comment">// expose the modules object (__webpack_modules__)</span>
   __webpack_require__.m = modules;

   <span class="hljs-comment">// expose the module cache</span>
  __webpack_require__.c = installedModules;

  <span class="hljs-comment">// __webpack_public_path__</span>
   __webpack_require__.p = <span class="hljs-string">""</span>;
   <span class="hljs-comment">// Load entry module and return exports</span>
  <span class="hljs-keyword">return</span> __webpack_require__(<span class="hljs-number">0</span>);
 &#125;)
 
([
<span class="hljs-comment">/* 0 */</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, <span class="hljs-built_in">exports</span>, __webpack_require__</span>) </span>&#123;
    <span class="hljs-keyword">var</span> b = __webpack_require__(<span class="hljs-number">1</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span>);
    b.b1();
&#125;,

<span class="hljs-comment">/* 1 */</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, <span class="hljs-built_in">exports</span></span>) </span>&#123;

    <span class="hljs-built_in">exports</span>.b1 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b1'</span>)
    &#125;;

    <span class="hljs-built_in">exports</span>.b2 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b2'</span>)
    &#125;;

 &#125;
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到<code>_webpack_require</code>是模块加载函数，接收模块id（webpack中<code>每个模块都会有一个独一无二的id</code>，其实也就是在IIFE传参数组中的索引值（0，1，2.....）<br>
a依赖b，所以在a中调用webpack加载模块的函数</p>
<p>webpack为什么能把任何形式的资源都视作模块呢？因为<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.jianshu.com%3Ft%3Dhttp%253A%252F%252Fwebpack.github.io%252Fdocs%252Fshimming-modules.html" target="_blank" rel="nofollow noopener noreferrer" title="https://link.jianshu.com?t=http%3A%2F%2Fwebpack.github.io%2Fdocs%2Fshimming-modules.html" ref="nofollow noopener noreferrer">loader机制</a>。不同的资源采用不同的loader进行转换。CMD、AMD 、import、css 、等都有相应的loader去进行转换。那为什么我们平时写的es6的模块机制，不用增加import的loader呢。因为我们使用了babel把import转换成了require。并且<strong>Webpack 2 将增加对 ES6 模块的原生支持并且混用 ES6、AMD 和 CommonJS 模块</strong>。这意味着 Webpack 现在可以识别 import 和 export 了，不需要先把它们转换成 CommonJS 模块的格式：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.jianshu.com%3Ft%3Dhttps%253A%252F%252Fgithub.com%252Fcssmagic%252Fblog%252Fissues%252F58" target="_blank" rel="nofollow noopener noreferrer" title="https://link.jianshu.com?t=https%3A%2F%2Fgithub.com%2Fcssmagic%2Fblog%2Fissues%2F58" ref="nofollow noopener noreferrer">Webpack 2 有哪些新东西</a>webpack对于es模块的实现，也是基于自己实现的<strong>webpack_require</strong> 和<strong>webpack_exports</strong> ，装换成类似于commonjs的形式。es6 module是静态的依赖,所以在运行前进行代码转换,这里的实现是将所有导出项作为一个对象的属性,在入口文件执行时,去递归的加载模块。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fe8ec61954748" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/e8ec61954748" ref="nofollow noopener noreferrer">webpack2是如何对实现es6 modules的</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.jianshu.com%2F%3Ft%3Dhttps%253A%252F%252Fsegmentfault.com%252Fa%252F1190000010955254" target="_blank" rel="nofollow noopener noreferrer" title="https://link.jianshu.com/?t=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000010955254" ref="nofollow noopener noreferrer">webpack模块化原理-ES module</a></p>
<h4 data-id="heading-0">如何实现一个简单的webpack</h4>
<ol>
<li>读取文件分析模块依赖</li>
<li>对模块进行解析执行(深度遍历)</li>
<li>针对不同的模块使用相应的loader</li>
<li>编译模块，生成抽象语法树AST。</li>
<li>循环遍历AST树，拼接输出js。<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.jianshu.com%3Ft%3Dhttps%253A%252F%252Flihuanghe.github.io%252F2016%252F05%252F30%252Fwebpack-source-analyse.html" target="_blank" rel="nofollow noopener noreferrer" title="https://link.jianshu.com?t=https%3A%2F%2Flihuanghe.github.io%2F2016%2F05%2F30%2Fwebpack-source-analyse.html" ref="nofollow noopener noreferrer">webpack 源码解析</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.jianshu.com%3Ft%3Dhttp%253A%252F%252Ftaobaofed.org%252Fblog%252F2016%252F09%252F09%252Fwebpack-flow%252F" target="_blank" rel="nofollow noopener noreferrer" title="https://link.jianshu.com?t=http%3A%2F%2Ftaobaofed.org%2Fblog%2F2016%2F09%2F09%2Fwebpack-flow%2F" ref="nofollow noopener noreferrer">细说 webpack 之流程篇</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.jianshu.com%3Ft%3Dhttps%253A%252F%252Fgithub.com%252Fyoungwind%252Fblog%252Fissues%252F99" target="_blank" rel="nofollow noopener noreferrer" title="https://link.jianshu.com?t=https%3A%2F%2Fgithub.com%2Fyoungwind%2Fblog%2Fissues%2F99" ref="nofollow noopener noreferrer">如何实现一个简单的webpack</a></li>
</ol>
<h4 data-id="heading-1">loader原理</h4>
<p>在解析对于文件，会自动去调用响应的loader<strong>loader 本质上是一个函数，输入参数是一个字符串，输出参数也是一个字符串。当然，输出的参数会被当成是 JS 代码，从而被 esprima 解析成 AST，触发进一步的依赖解析。</strong> webpack会按照从右到左的顺序执行loader。<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.jianshu.com%3Ft%3Dhttps%253A%252F%252Fgithub.com%252Fchemdemo%252Fchemdemo.github.io%252Fissues%252F13" target="_blank" rel="nofollow noopener noreferrer" title="https://link.jianshu.com?t=https%3A%2F%2Fgithub.com%2Fchemdemo%2Fchemdemo.github.io%2Fissues%2F13" ref="nofollow noopener noreferrer">Webpack——令人困惑的地方</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2Fconfig%2F%23%25E5%2585%25A8%25E5%25B1%2580-cli-%25E9%2585%258D%25E7%25BD%25AE" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/config/#%E5%85%A8%E5%B1%80-cli-%E9%85%8D%E7%BD%AE" ref="nofollow noopener noreferrer">cli.vuejs.org/zh/config/#…</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fu014440483%2Farticle%2Fdetails%2F87267160" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/u014440483/article/details/87267160" ref="nofollow noopener noreferrer">blog.csdn.net/u014440483/…</a></p></div>  
</div>
            