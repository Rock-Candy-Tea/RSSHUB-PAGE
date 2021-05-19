
---
title: '一次搞懂-JavaScript模块化详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e763abe0a1df437380c98bbe85e65be5~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 17:52:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e763abe0a1df437380c98bbe85e65be5~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e763abe0a1df437380c98bbe85e65be5~tplv-k3u1fbpfcp-zoom-1.image" alt="JavaScript-模块 1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">模块化的意义</h2>
<p>将代码拆分成独立的块，然后再把这些块使用模块模式连接起来实现不同的功能。</p>
<p>就像小时候玩的拼图一样，不同的拼图组合在一起就可以拼成任意的形状。</p>
<p>这种模式的背后思想也很简单：<strong>把逻辑分块、各自封装，相互独立，同时自行决定引入执行那些外部模块以及暴露自身的那些模块。</strong></p>
<p>这个基本的思想是所有的 JavaScript 模块系统的基础。</p>
<p>文中代码案例地址：<a href="https://github.com/AnsonZnl/JS-Modules-Sample" target="_blank" rel="nofollow noopener noreferrer">github.com/AnsonZnl/JS…</a></p>
<h3 data-id="heading-1">模块化的好处</h3>
<ul>
<li>避免命名冲突(减少命名空间污染)</li>
<li>更好的分离, 按需加载</li>
<li>更高复用性</li>
<li>高可维护性</li>
</ul>
<h2 data-id="heading-2">JS 中常见的模块</h2>
<h3 data-id="heading-3">IIFE 模式：匿名函数自调用（闭包）</h3>
<p>主要应用在浏览器端。</p>
<p>利用闭包的原理创造一个独有的函数作用域来保存私有变量，达到模块化的效果。</p>
<p><strong>使用</strong></p>
<p>HTML</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"module.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="javascript">
  <span class="hljs-built_in">console</span>.log(myModule.get()); <span class="hljs-comment">// output-data(获取内部数据)</span>
  myModule.set(<span class="hljs-string">"new data"</span>); <span class="hljs-comment">// 设置内部数据</span>
  <span class="hljs-built_in">console</span>.log(myModule.data); <span class="hljs-comment">//output-undefined (不能访问模块内部数据)</span>
  myModule.data = <span class="hljs-string">"xxxx"</span>; <span class="hljs-comment">//不是修改的模块内部的data</span>
  <span class="hljs-built_in">console</span>.log(myModule.get()); <span class="hljs-comment">//output-new data 修改后的值</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JS</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// module.js文件</span>
(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">window</span></span>) </span>&#123;
  <span class="hljs-keyword">let</span> data = <span class="hljs-string">"data"</span>;
  <span class="hljs-comment">//获取数据</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> data;
  &#125;
  <span class="hljs-comment">// 修改数据</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">set</span>(<span class="hljs-params">val</span>) </span>&#123;
    data = val;
  &#125;
  <span class="hljs-comment">//暴露行为</span>
  <span class="hljs-built_in">window</span>.myModule = &#123;
    get,
    set,
  &#125;;
&#125;)(<span class="hljs-built_in">window</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">CommonJS</h3>
<p>主要应用在服务端，如果在浏览器端运行需要借助其他工具（Browserify）。</p>
<p><strong>暴露模块：</strong> <code>module.exports = value</code>或者<code>exports.xx = value</code>(exports 是一个导出的对象)</p>
<p><strong>引入模块：</strong> <code>require(xx)</code>，如果是第三方模块，xxx 为模块名，如果为自定义模块，xxx 为模块的文件路径。</p>
<p><strong>特点</strong></p>
<ul>
<li>所有代码都运行在模块作用域，不会污染全局作用域。</li>
<li>模块可以多次加载，但是只会在第一次加载时运行一次，然后运行结果就被缓存了，以后再加载，就直接读取缓存结果。要想让模块再次运行，必须清除缓存。</li>
<li>模块加载的顺序，按照其在代码中出现的顺序。</li>
</ul>
<p><strong>使用</strong>
在 Node 中 安装 uniq 函数。</p>
<pre><code class="hljs language-base copyable" lang="base">npm init
npm install uniq --save
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// module.js</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">3</span>];
<span class="hljs-built_in">module</span>.exports = &#123;
  arr,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// app.js</span>
<span class="hljs-keyword">let</span> module1 = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./module.js"</span>);
<span class="hljs-keyword">let</span> uniq = <span class="hljs-built_in">require</span>(<span class="hljs-string">"uniq"</span>);

<span class="hljs-built_in">console</span>.log(uniq(module1.arr)); <span class="hljs-comment">// [1,2,3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">AMD</h3>
<p>全称是 Asynchronous Module Definition - 异步模块定义</p>
<p>和 CommonJS 不同的是 AMD 采用非同步的方式来加载模块。</p>
<p><strong>基本语法</strong></p>
<p>定义暴露模块</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义没有依赖的模块</span>
define(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> 模块;
&#125;);
<span class="hljs-comment">// 定义有依赖的模块</span>
define([<span class="hljs-string">"module1"</span>, <span class="hljs-string">"module2"</span>], <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">m1, m2</span>) </span>&#123;
  <span class="hljs-keyword">return</span> 模块;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入使用模块</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">require</span>([<span class="hljs-string">"module1"</span>, <span class="hljs-string">"module2"</span>], <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">m1, m2</span>) </span>&#123;
  使用m1 和 m2;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用案例</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- index.html --></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-comment"><!-- 引入require.js并指定js主文件的入口 --></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>
    <span class="hljs-attr">data-main</span>=<span class="hljs-string">"main"</span>
    <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcdn.net/ajax/libs/require.js/2.3.6/require.js"</span>
  ></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main.js</span>
(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">require</span>([<span class="hljs-string">"module.js"</span>], <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span></span>) </span>&#123;
    <span class="hljs-keyword">let</span> currentUrl = <span class="hljs-built_in">module</span>.getUrl();
    alert(<span class="hljs-string">"当前页面的URl："</span> + currentUrl);
  &#125;);
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// module.js</span>
<span class="hljs-comment">// 定义模块</span>
define(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> url = <span class="hljs-built_in">window</span>.location.href;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getUrl</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> url.toUpperCase();
  &#125;
  <span class="hljs-comment">// 暴露模块</span>
  <span class="hljs-keyword">return</span> &#123;
    getUrl,
  &#125;;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多的使用方法请参考：<a href="https://requirejs.org/" target="_blank" rel="nofollow noopener noreferrer">requirejs.org/</a></p>
<h3 data-id="heading-6">CMD</h3>
<p>CMD---是 SeaJS 在推广过程中对模块定义的规范化产出，是一个同步模块定义，是 SeaJS 的一个标准，SeaJS 是 CMD 概念的一个实现，SeaJS 是淘宝团队提供的一个模块开发的 JS 框架。</p>
<p>什么时候用到什么时候引入，即用即返回，这是一个同步概念。</p>
<p><strong>特点：</strong> CMD 是 AMD 在基础上改进的一种规范，和 AMD 不同在于依赖模块的执行机制不同，CMD 是就近依赖，而 AMD 是前置依赖。</p>
<p><strong>环境：</strong> 浏览器环境</p>
<p><strong>语法：</strong></p>
<ul>
<li>导入：define(function(require, exports, module)&#123;&#125;)</li>
<li>导出：define(function()&#123;return '值'&#125;)</li>
</ul>
<p><strong>使用</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main.js</span>
define(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">require</span>, <span class="hljs-built_in">exports</span>, <span class="hljs-built_in">module</span></span>) </span>&#123;
  <span class="hljs-keyword">var</span> moduleA = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./module.js"</span>);
  alert(moduleA.a); <span class="hljs-comment">// 打印出：hello world</span>
&#125;);
<span class="hljs-comment">// module.js</span>
define(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">require</span>, <span class="hljs-built_in">exports</span>, <span class="hljs-built_in">module</span></span>) </span>&#123;
  <span class="hljs-built_in">exports</span>.a = <span class="hljs-string">"hello world"</span>;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>
    <span class="hljs-attr">data-main</span>=<span class="hljs-string">"main"</span>
    <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcdn.net/ajax/libs/require.js/2.3.6/require.js"</span>
  ></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Sea.js 用法请参考：<a href="https://seajs.github.io/seajs/docs/" target="_blank" rel="nofollow noopener noreferrer">seajs.github.io/seajs/docs/</a></p>
<h3 data-id="heading-7">UMD</h3>
<p>全称 Universal Module Definition 看名字就知道，特点是兼容 AMD 和 CommonJS 规范，而且兼容全局引入。</p>
<p><strong>环境：</strong> 服务器环境和浏览器端</p>
<p><strong>UMD 实现原理很简单：</strong></p>
<ul>
<li>先判断是否支持 AMD（define 是否存在），存在则使用 AMD 方式加载模块；</li>
<li>再判断是否支持 Node.js 模块格式（exports 是否存在），存在则使用 Node.js 模块格式；</li>
<li>前两个都不存在，则将模块公开到全局（window 或 global）</li>
</ul>
<p><strong>使用</strong></p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">root, factory</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> define === <span class="hljs-string">"function"</span> && define.amd) &#123;
    <span class="hljs-comment">//AMD</span>
    define([<span class="hljs-string">"jquery"</span>], factory);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">exports</span> === <span class="hljs-string">"object"</span>) &#123;
    <span class="hljs-comment">//Node, CommonJS之类的</span>
    <span class="hljs-built_in">module</span>.exports = factory(<span class="hljs-built_in">require</span>(<span class="hljs-string">"jquery"</span>));
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">//浏览器全局变量(root 即 window)</span>
    root.returnExports = factory(root.jQuery);
  &#125;
&#125;)(<span class="hljs-built_in">this</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">$</span>) </span>&#123;
  <span class="hljs-comment">//方法</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myFuncA</span>(<span class="hljs-params"></span>) </span>&#123;&#125; <span class="hljs-comment">// 私有方法，因为没有返回</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myFuncB</span>(<span class="hljs-params"></span>) </span>&#123;&#125; <span class="hljs-comment">// 公共方法，因为返回了</span>

  <span class="hljs-comment">//暴露公共方法</span>
  <span class="hljs-keyword">return</span> &#123;
    myFuncB,
  &#125;;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家平时引入的 jQuery 的 CND 就是 UMD 的，源码可以查看：<a href="https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.js" target="_blank" rel="nofollow noopener noreferrer">cdn.bootcdn.net/ajax/libs/j…</a></p>
<h3 data-id="heading-8">ES6 Module</h3>
<p>在 ES6 之前，模块化主要是社区在推动进行的，从而出现了 CommonJS 和 AMD 两个，前者用于服务器后者用于浏览器，ES6 模块的出现将完全替代 CommonJS 和 AMD 规范，成为浏览器和服务器通用的解决方案。</p>
<p>ES6 模块的设计思想是尽量的静态化，使得编译时就能确定模块的依赖关系，以及输入和输出的变量。CommonJS 和 AMD 模块，都只能在运行时确定这些东西。比如，CommonJS 模块就是对象，输入时必须查找对象属性。</p>
<p><strong>特点</strong> ：</p>
<ul>
<li>按需加载（编译时加载）</li>
<li>import 和 export 命令只能在模块的顶层，不能在代码块之中（如：if 语句中）,import()语句可以在代码块中实现异步动态按需动态加载</li>
</ul>
<p><strong>环境：</strong> 服务器环境和浏览器端</p>
<p><strong>语法：</strong></p>
<ul>
<li>导入：<code>import &#123;modules1,modules1,&#125; from '模块路径'</code></li>
<li>导出：<code>export</code>或者<code>export default</code></li>
<li>动态导入：<code>import('模块路径').then(..)</code>

</li>
</ul>
<p><strong>使用</strong></p>
<p>Node 中 先安装 Babel:</p>
<pre><code class="copyable">npm install --save-dev @babel/core @babel/cli @babel/preset-env @babel/node
npm install --save @babel/polyfill
# 然后运行
npx babel-node main.js
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// modules/double.js</span>
<span class="hljs-keyword">let</span> mes = <span class="hljs-string">"Hello Modules for double"</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;mes&#125;</span> - <span class="hljs-subst">$&#123;value * <span class="hljs-number">2</span>&#125;</span>`</span>;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  mes,
  sum,
&#125;;
<span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./modules/double"</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">module</span>.sum(<span class="hljs-number">10</span>)); <span class="hljs-comment">// Hello Modules for double - 20</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器中</p>
<p><strong>区别</strong></p>
<ul>
<li>
<p>和 CommonJS 的区别：</p>
<ul>
<li>CommonJS 模块输出的是一个值得拷贝，ES6 模块输出的是值的引用</li>
<li>CommonJS 模块是运行时加载，ES6 模块是编译时输出接口</li>
<li>CommonJS 模块的 require()是同步加载模块，ES6 模块的 import 命令是异步加载，有一个独立的模块依赖的解析阶段。</li>
</ul>
</li>
</ul>
<p><strong>缺点</strong>
浏览器和服务器目前的支持不是很好，现阶段使用需要借助一些工具（<a href="https://www.babeljs.cn/" target="_blank" rel="nofollow noopener noreferrer">Babel</a>）。</p>
<ul>
<li>浏览器支持：在新版本的浏览器（如 Chrome）中可以使用<code><script type="module" src="./foo.js"></script></code>写法</li>
<li>服务器支持（Node）有两种模式，分别是 ES6 模块和 CommonJS。
<ul>
<li>从 Node.js v13.2 开始，默认支持 ES6 模块，但是需要采用<code>.mjs</code>为后缀名、或者在<code>package.json</code>中修改<code>type</code>字段为<code>module</code>（推荐）</li>
<li>使用 CommonJS 的话需要以<code>.cjs</code>为后缀，也可以设置<code>package.json</code>中修改<code>type</code>字段为<code>commonjs</code>（推荐）。</li>
</ul>
</li>
</ul>
<p>最好不要两者混用。更多的使用方法可以参考：<a href="https://es6.ruanyifeng.com/#docs/module" target="_blank" rel="nofollow noopener noreferrer">es6.ruanyifeng.com/#docs/modul…</a></p>
<h2 data-id="heading-9">总结</h2>
<ul>
<li>CommonJS 规范主要用于服务端编程，加载模块是同步的，这并不适合在浏览器环境，因为同步意味着阻塞加载，浏览器资源是异步加载的，因此有了 AMD CMD 解决方案。</li>
<li>AMD 规范在浏览器环境中异步加载模块，而且可以并行加载多个模块。不过，AMD 规范开发成本高，代码的阅读和书写比较困难，模块定义方式的语义不顺畅。</li>
<li>CMD 规范与 AMD 规范很相似，都用于浏览器编程，依赖就近，延迟执行，可以很容易在 Node.js 中运行。不过，依赖 SPM 打包，模块的加载逻辑偏重</li>
<li><strong>ES6 在语言标准的层面上，实现了模块功能，而且实现得相当简单，完全可以取代 CommonJS 和 AMD 规范，成为浏览器和服务器通用的模块解决方案。</strong></li>
</ul>
<h2 data-id="heading-10">参考</h2>
<ul>
<li><a href="https://juejin.cn/post/6844903744518389768" target="_blank">前端模块化详解</a></li>
<li><a href="https://segmentfault.com/a/1190000012419990" target="_blank" rel="nofollow noopener noreferrer">JS 模块</a></li>
<li><a href="https://www.php.cn/js-tutorial-410584.html" target="_blank" rel="nofollow noopener noreferrer">javascript 中 UMD 规范介绍</a></li>
<li><a href="https://es6.ruanyifeng.com/#docs/module" target="_blank" rel="nofollow noopener noreferrer">ES6 Modules</a></li>
<li><a href="https://mp.weixin.qq.com/s/quoWsIAvLITT6jGWs3higg" target="_blank" rel="nofollow noopener noreferrer">一篇理解前端模块化：AMD、CMD、CommonJS、ES6</a></li>
</ul></div>  
</div>
            