
---
title: '前端打包路（1） - 基本原理&发展历史&webpack初介绍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7d4d058dff245c49af1629cf281348a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 02 Apr 2021 01:13:36 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7d4d058dff245c49af1629cf281348a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p><code>后记：由于webpack的知识体系太庞大了，而且webpack是一个很有深度的框架，所以我们拆分一下，这节课先来讲一下打包的基本原理和历史，后面会尽可能深的介绍：（2）原理（3）实战&webpack优化 (4) Tapable (5) tree-shaking (6) sourceMap (7) HMR</code></p>
<p>前端打包、构建、gulp、grunt、webpack、rollup、一堆名词，之前没有好好的系统性学习过，这次抽空系统的捋一捋。。。<br>
可以说随着node的出现，前端变得越来越复杂，因为js代码不再是只能运行在浏览器里面的弱鸡语言，随之带来的是同样在服务器上运行的能力。我认为带来最大的利好就是前端项目也可以“工程化”了，就像C一样，具备了：预处理、编译、汇编、链接的能力。当然javascript是一门解释型语言，所以就没有后面三步了，前端打包多少类似于预处理+模块化的过程。</p>
<h2 data-id="heading-1">理解前端模块化</h2>
<p>为啥要模块化：难道都写在main.js里面？如何复用？如何协同开发？<br>
但是js不像其他</p>
<h3 data-id="heading-2">作用域</h3>
<pre><code class="copyable">全局作用域、局部作用域 
全局: window, global
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./moduleA.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./moduleB.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./moduleC.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// moduleA.js</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// moduleB.js</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// moduleC.js</span>
<span class="hljs-keyword">var</span> b = a + <span class="hljs-number">1</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b = '</span>, b);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">结果:b = 3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然被覆盖了。怎么办呢？</p>
<h3 data-id="heading-3">命名空间</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//moduleA</span>
<span class="hljs-keyword">var</span> a = &#123;
  <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//moduleB</span>
<span class="hljs-keyword">var</span> b = &#123;
  <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//moduleC</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'moduleA的value'</span>, a.value);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'moduleB的value'</span>, b.value);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">结果：
moduleA的value <span class="hljs-number">1</span>
moduleB的value <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看上去解决了上面的问题，但是随之而来的问题：</p>
<pre><code class="hljs language-js copyable" lang="js">a.value = <span class="hljs-number">100</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样很容易就改变内部的一个变量了
所以我们需要利用作用域和闭包来改造一把</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">var</span> moduleA = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> name = <span class="hljs-string">'Nolan'</span>;

    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">myNameIs</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请叫我'</span>, name);
      &#125;,
    &#125;;
  &#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一个立即执行函数。</p>
<pre><code class="hljs language-js copyable" lang="js">moduleA.myNameIs();
<span class="hljs-comment">// 请叫我Nolan</span>

moduleA.name;
<span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显暴露了该暴露的、隐藏了该隐藏的。<br>
接下来我们再优化一下写法</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">window</span></span>) </span>&#123;
  <span class="hljs-keyword">var</span> name = <span class="hljs-string">'Nolan'</span>;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myNameIs</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请叫我'</span>, name);
  &#125;
  
  <span class="hljs-built_in">window</span>.moduleA = &#123; myNameIs &#125;;
&#125;)(<span class="hljs-built_in">window</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你撸过webpack打包后的代码，对比一下，是不是很像了？</p>
<h4 data-id="heading-4">总结一下</h4>
<p>所以我们看到一个技术是循序渐进出来的，想想手写一个js继承是不是也是一步一步解决问题，遇到新的问题，再解决问题，最终产生的。<br>
<strong>优点：</strong></p>
<ul>
<li>作用域封装</li>
<li>重用性</li>
<li>解除耦合</li>
</ul>
<h3 data-id="heading-5">模块化</h3>
<h4 data-id="heading-6">History</h4>
<ul>
<li>AMD</li>
<li>COMMONJS</li>
<li>ES6 MODULE</li>
</ul>
<h4 data-id="heading-7">AMD</h4>
<pre><code class="hljs language-js copyable" lang="js">define(<span class="hljs-string">'moduleName'</span>, [<span class="hljs-string">'lodash'</span>], <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">_</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a, b);
  &#125;;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如 requireJS
后来衍生出了 玉伯大神的成名作 sea.js(CMD)</p>
<h4 data-id="heading-8">COMMONJS</h4>
<p>2009年推出，主要为了规范服务端开发，并不是针对浏览器的规范。所以后来Nodejs也引用了此标准。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> moduleA = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./moduleA'</span>);

<span class="hljs-built_in">exports</span>.getSum = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(a + b);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与AMD相同，强调了引入的模块。</p>
<h4 data-id="heading-9">ES6 MODULE</h4>
<p>与COMMONS很像</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> moduleA <span class="hljs-keyword">from</span> <span class="hljs-string">'./moduleA'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getName</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">return</span> name;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>期间诞生了很多可以打包的工具：<br>
Gulp，Grunt是<em>自动化</em>构建工具，这里要强调<em>自动化</em>是因为他们不仅可以做打包，自动化是其核心目的。<br>
而webpack的出现可以说是专注于打包。</p>
<h2 data-id="heading-10">webpack</h2>
<h3 data-id="heading-11">先来看一个小例子</h3>
<p>首先我们先创建一个webpack-test的工程
下面包括 index.html、src/index.js和src/util.js。 npm安装 webpack以及webpack-cli工具<br>
目前使用的是4.x.x版本。v5对tree-shake进行了性能优化，所以构建出的结果会有所不同。后面我们会介绍tree-shake是什么。
index.html</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>My Webpack Test<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./src/index.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> num = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./util'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是一个小测试！'</span>, num);
&#125;

test();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>util.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">exports</span>.default = <span class="hljs-number">123</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来在根目录执行
<code>npx webpack 或者 ./node_module/.bin/webpack</code>
会生成dist/main.js的文件，打开文件我们看下结构</p>
<pre><code class="hljs language-js copyable" lang="js">! <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-keyword">var</span> t = &#123;&#125;;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">n</span>(<span class="hljs-params">r</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (t[r]) <span class="hljs-keyword">return</span> t[r].exports;
        <span class="hljs-keyword">var</span> o = t[r] = &#123;
            <span class="hljs-attr">i</span>: r,
            <span class="hljs-attr">l</span>: !<span class="hljs-number">1</span>,
            <span class="hljs-attr">exports</span>: &#123;&#125;
        &#125;;
        <span class="hljs-keyword">return</span> e[r].call(o.exports, o, o.exports, n), o.l = !<span class="hljs-number">0</span>, o.exports
    &#125;
    n.m = e, n.c = t, n.d = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e, t, r</span>) </span>&#123;
        n.o(e, t) || <span class="hljs-built_in">Object</span>.defineProperty(e, t, &#123;
            <span class="hljs-attr">enumerable</span>: !<span class="hljs-number">0</span>,
            <span class="hljs-attr">get</span>: r
        &#125;)
    &#125;, n.r = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
        <span class="hljs-string">"undefined"</span> != <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> && <span class="hljs-built_in">Symbol</span>.toStringTag && <span class="hljs-built_in">Object</span>.defineProperty(e, <span class="hljs-built_in">Symbol</span>.toStringTag, &#123;
            <span class="hljs-attr">value</span>: <span class="hljs-string">"Module"</span>
        &#125;), <span class="hljs-built_in">Object</span>.defineProperty(e, <span class="hljs-string">"__esModule"</span>, &#123;
            <span class="hljs-attr">value</span>: !<span class="hljs-number">0</span>
        &#125;)
    &#125;, n.t = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e, t</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-number">1</span> & t && (e = n(e)), <span class="hljs-number">8</span> & t) <span class="hljs-keyword">return</span> e;
        <span class="hljs-keyword">if</span> (<span class="hljs-number">4</span> & t && <span class="hljs-string">"object"</span> == <span class="hljs-keyword">typeof</span> e && e && e.__esModule) <span class="hljs-keyword">return</span> e;
        <span class="hljs-keyword">var</span> r = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
        <span class="hljs-keyword">if</span> (n.r(r), <span class="hljs-built_in">Object</span>.defineProperty(r, <span class="hljs-string">"default"</span>, &#123;
                <span class="hljs-attr">enumerable</span>: !<span class="hljs-number">0</span>,
                <span class="hljs-attr">value</span>: e
            &#125;), <span class="hljs-number">2</span> & t && <span class="hljs-string">"string"</span> != <span class="hljs-keyword">typeof</span> e)
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> o <span class="hljs-keyword">in</span> e) n.d(r, o, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">t</span>) </span>&#123;
                <span class="hljs-keyword">return</span> e[t]
            &#125;.bind(<span class="hljs-literal">null</span>, o));
        <span class="hljs-keyword">return</span> r
    &#125;, n.n = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
        <span class="hljs-keyword">var</span> t = e && e.__esModule ? <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> e.default
        &#125; : <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> e
        &#125;;
        <span class="hljs-keyword">return</span> n.d(t, <span class="hljs-string">"a"</span>, t), t
    &#125;, n.o = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e, t</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.hasOwnProperty.call(e, t)
    &#125;, n.p = <span class="hljs-string">""</span>, n(n.s = <span class="hljs-number">0</span>)
&#125;([<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e, t, n</span>) </span>&#123;
    <span class="hljs-keyword">const</span> r = n(<span class="hljs-number">1</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是一个小测试！"</span>, r)
&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e, t</span>) </span>&#123;
    t.default = <span class="hljs-number">123</span>
&#125;]);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>前面那一大坨我们先不管</p>
<p>简化就是<code>(function(module)&#123;&#125;)([index.js, util.js])</code></p>
<p>看看结构发现是不是就是一个立即执行函数！所以说，高大上的webpack也只不过是通过前面提到的立即执行函数来实现的。那前面那一大堆不是人写的代码是什么呢？为啥会变成这个鸟样？我们接下来先让代码变得可读一些。</p>
<p><code>webpack --help</code>可以看到<code>--mode</code>这样一个参数，<code>development</code>和<code>production</code>两个值。默认是<code>production</code>，我们在运行<code>npx webpack</code>的时候也可以看到这样的输出：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7d4d058dff245c49af1629cf281348a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>接下来我们执行一把看看吧~<code>npx webpack --mode=development</code></p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">modules</span>) </span>&#123; <span class="hljs-comment">// webpackBootstrap</span>
  <span class="hljs-comment">// 定义一个缓存</span>
  <span class="hljs-keyword">var</span> installedModules = &#123;&#125;;
  <span class="hljs-comment">// 可以称之为webpack运行在浏览器上的require方法，参数就是立即执行函数的参数中的key值</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">__webpack_require__</span>(<span class="hljs-params">moduleId</span>) </span>&#123;
    <span class="hljs-comment">// 有缓存就返回缓存中的数据</span>
    <span class="hljs-keyword">if</span>(installedModules[moduleId]) &#123;
      <span class="hljs-keyword">return</span> installedModules[moduleId].exports;
    &#125;
    <span class="hljs-comment">// 开开心心放入缓存，注意这里定义了exports对象</span>
    <span class="hljs-keyword">var</span> <span class="hljs-built_in">module</span> = installedModules[moduleId] = &#123;
      <span class="hljs-attr">i</span>: moduleId,
      <span class="hljs-attr">l</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">exports</span>: &#123;&#125;
    &#125;;
    <span class="hljs-comment">// 执行函数</span>
    <span class="hljs-comment">// 思考一下，我们在IDE里面疯狂无脑写着import/require/exports/export这些模块</span>
    <span class="hljs-comment">// 跑到浏览器上运行的时候，浏览器哪儿知道这些玩意儿是干蛋的，但是浏览器知道啥？</span>
    <span class="hljs-comment">// 知道对象、知道函数，所以我们把模块的导出存在了module.exports里面，module.exports在前面刚被初始化干干净净的被call</span>
    <span class="hljs-comment">// 再遇到require不怕了，其实就是__webpack_require__这个方法嘛</span>
    <span class="hljs-comment">// 所以require()的参数是模块的路径也就是立即执行函数参数中的key</span>
    <span class="hljs-comment">// 而exports的就是个对象</span>
    modules[moduleId].call(<span class="hljs-built_in">module</span>.exports, <span class="hljs-built_in">module</span>, <span class="hljs-built_in">module</span>.exports, __webpack_require__);
    <span class="hljs-comment">// 不重要</span>
    <span class="hljs-built_in">module</span>.l = <span class="hljs-literal">true</span>;
    <span class="hljs-comment">// require(一个文件路径), 这个文件exports的那些玩意儿</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">module</span>.exports;
  &#125;
  <span class="hljs-comment">// 为内置的require对象添加依赖模块</span>
  __webpack_require__.m = modules;
  <span class="hljs-comment">// 为内置的require对象添加缓存</span>
  __webpack_require__.c = installedModules;

  <span class="hljs-comment">// exports对象添加一个getter方法</span>
  __webpack_require__.d = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">exports</span>, name, getter</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(!__webpack_require__.o(<span class="hljs-built_in">exports</span>, name)) &#123;
      <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">exports</span>, name, &#123; <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">get</span>: getter &#125;);
    &#125;
  &#125;;
  <span class="hljs-comment">// 下面的例子中讲</span>
  __webpack_require__.r = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">exports</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> !== <span class="hljs-string">'undefined'</span> && <span class="hljs-built_in">Symbol</span>.toStringTag) &#123;
      <span class="hljs-comment">// Object.prototype.toString.call(exports)的时候返回的是Module</span>
      <span class="hljs-comment">// 感觉就是看上去好看</span>
      <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">exports</span>, <span class="hljs-built_in">Symbol</span>.toStringTag, &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'Module'</span> &#125;);
    &#125;
    <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">exports</span>, <span class="hljs-string">'__esModule'</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-literal">true</span> &#125;);
  &#125;;
  <span class="hljs-comment">// 说实话，我也不太清楚这个方法是干啥的</span>
  <span class="hljs-comment">// 但是我翻了下github上有人提问，解释是：“ESM CJS interop. import("commonjs") will use it.”</span>
  <span class="hljs-comment">// 地址粘贴在下方： https://github.com/webpack/webpack/issues/11024</span>
  __webpack_require__.t = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value, mode</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(mode & <span class="hljs-number">1</span>) value = __webpack_require__(value);
    <span class="hljs-keyword">if</span>(mode & <span class="hljs-number">8</span>) <span class="hljs-keyword">return</span> value;
    <span class="hljs-keyword">if</span>((mode & <span class="hljs-number">4</span>) && <span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'object'</span> && value && value.__esModule) <span class="hljs-keyword">return</span> value;
    <span class="hljs-keyword">var</span> ns = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
    __webpack_require__.r(ns);
    <span class="hljs-built_in">Object</span>.defineProperty(ns, <span class="hljs-string">'default'</span>, &#123; <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">value</span>: value &#125;);
    <span class="hljs-keyword">if</span>(mode & <span class="hljs-number">2</span> && <span class="hljs-keyword">typeof</span> value != <span class="hljs-string">'string'</span>) <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> value) __webpack_require__.d(ns, key, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">key</span>) </span>&#123; <span class="hljs-keyword">return</span> value[key]; &#125;.bind(<span class="hljs-literal">null</span>, key));
    <span class="hljs-keyword">return</span> ns;
  &#125;;
  <span class="hljs-comment">// 下面的例子中讲</span>
  __webpack_require__.n = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span></span>) </span>&#123;
    <span class="hljs-keyword">var</span> getter = <span class="hljs-built_in">module</span> && <span class="hljs-built_in">module</span>.__esModule ?
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getDefault</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">module</span>[<span class="hljs-string">'default'</span>]; &#125; :
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getModuleExports</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">module</span>; &#125;;
    __webpack_require__.d(getter, <span class="hljs-string">'a'</span>, getter);
    <span class="hljs-keyword">return</span> getter;
  &#125;;
  <span class="hljs-comment">// 包含属性否</span>
  __webpack_require__.o = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">object, property</span>) </span>&#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.hasOwnProperty.call(object, property); &#125;;
  <span class="hljs-comment">// 不重要</span>
  __webpack_require__.p = <span class="hljs-string">""</span>;
  <span class="hljs-comment">// require入口文件吧</span>
  <span class="hljs-keyword">return</span> __webpack_require__(__webpack_require__.s = <span class="hljs-string">"./src/index.js"</span>);
&#125;)(&#123;
  <span class="hljs-comment">// 入口方法</span>
  <span class="hljs-string">"./src/index.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, <span class="hljs-built_in">exports</span>, __webpack_require__</span>) </span>&#123;
    <span class="hljs-built_in">eval</span>(<span class="hljs-string">"const num = __webpack_require__(/*! ./util */ \"./src/util.js\");\n\nfunction test() &#123;\n  console.log('我是一个小测试！', num);\n&#125;\n\ntest();\n\n\n//# sourceURL=webpack:///./src/index.js?"</span>);
  &#125;),
  <span class="hljs-comment">// 被引入的方法</span>
  <span class="hljs-string">"./src/util.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, <span class="hljs-built_in">exports</span></span>) </span>&#123;
    <span class="hljs-built_in">eval</span>(<span class="hljs-string">"exports.default = 123;\n\n//# sourceURL=webpack:///./src/util.js?"</span>);
  &#125;)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这次变得好阅读一些了。我把函数的作用写在注释上。</p>
<p>那我们再尝试一个ES6 MODULE和CJS混用的<br>
我们修改一下index.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; num &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./util'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是一个小测试！'</span>, num);
&#125;

test();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有util.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">exports</span>.num = <span class="hljs-number">123</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让我们再次打包看下结果，重复的部分我们就不说了，主要集中在不同上
<code>__webpack_require__.n</code>和<code>__webpack_require__.r</code>还有eval里面</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">modules</span>) </span>&#123; <span class="hljs-comment">// webpackBootstrap</span>
  <span class="hljs-keyword">var</span> installedModules = &#123;&#125;;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">__webpack_require__</span>(<span class="hljs-params">moduleId</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (installedModules[moduleId]) &#123;
      <span class="hljs-keyword">return</span> installedModules[moduleId].exports;
    &#125;
    <span class="hljs-keyword">var</span> <span class="hljs-built_in">module</span> = installedModules[moduleId] = &#123;
      <span class="hljs-attr">i</span>: moduleId,
      <span class="hljs-attr">l</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">exports</span>: &#123;&#125;
    &#125;;
    modules[moduleId].call(<span class="hljs-built_in">module</span>.exports, <span class="hljs-built_in">module</span>, <span class="hljs-built_in">module</span>.exports, __webpack_require__);
    <span class="hljs-built_in">module</span>.l = <span class="hljs-literal">true</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">module</span>.exports;
  &#125;
  __webpack_require__.m = modules;
  __webpack_require__.c = installedModules;
  <span class="hljs-comment">// 说白了就是以后在调用exports.a的时候用我们传进来的getter，这个例子里面也就是getDefault</span>
  <span class="hljs-comment">// 如果你在index.js里面这么用的 import X from './util';</span>
  <span class="hljs-comment">// console.log(X)的话，其实就是.a的getter。打完收工。</span>
  __webpack_require__.d = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">exports</span>, name, getter</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!__webpack_require__.o(<span class="hljs-built_in">exports</span>, name)) &#123;
      <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">exports</span>, name, &#123;
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">get</span>: getter
      &#125;);
    &#125;
  &#125;;
  <span class="hljs-comment">// 这个Symbol.toStringTag理解为当我们Object.prototype.toString.call(exports)时，返回[object Module]类型</span>
  __webpack_require__.r = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">exports</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> !== <span class="hljs-string">'undefined'</span> && <span class="hljs-built_in">Symbol</span>.toStringTag) &#123;
      <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">exports</span>, <span class="hljs-built_in">Symbol</span>.toStringTag, &#123;
        <span class="hljs-attr">value</span>: <span class="hljs-string">'Module'</span>
      &#125;);
    &#125;
    <span class="hljs-comment">// 为exports对象加了一个属性，标明这个文件是ES6MODULE的哟~</span>
    <span class="hljs-comment">// 回到下面eval</span>
    <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">exports</span>, <span class="hljs-string">'__esModule'</span>, &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-literal">true</span>
    &#125;);
  &#125;;
  <span class="hljs-comment">// 传入的exports对象是不是ES6Module啊？</span>
  <span class="hljs-comment">// 如果是，我们是不是会export default X一个默认值，然后import X就完了</span>
  <span class="hljs-comment">// 在es6 module中我们export default X其实是这样一个操作 default = X;</span>
  <span class="hljs-comment">// 没错就是个赋值，所以我们这样是会报错的  export default const X;</span>
  <span class="hljs-comment">// 转化成default = const X绝逼有问题对吧</span>
  <span class="hljs-comment">// 所以这里我们就用getDefault方法默认帮你返回exports.default值了</span>
  <span class="hljs-comment">// .d方法其实就是重写getter方法。</span>
  <span class="hljs-comment">// 我们看下三个参数getter现在就是 getDefault()这个方法了，'a'是我们命名的一个参数名</span>
  <span class="hljs-comment">// 我们去.d方法里面瞅一眼</span>
  __webpack_require__.n = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">module</span></span>) </span>&#123;
    <span class="hljs-keyword">var</span> getter = <span class="hljs-built_in">module</span> && <span class="hljs-built_in">module</span>.__esModule ?
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getDefault</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">module</span>[<span class="hljs-string">'default'</span>];
      &#125; :
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getModuleExports</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">module</span>;
      &#125;;
    __webpack_require__.d(getter, <span class="hljs-string">'a'</span>, getter);
    <span class="hljs-keyword">return</span> getter;
  &#125;;
  __webpack_require__.o = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">object, property</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.hasOwnProperty.call(object, property);
  &#125;;
  __webpack_require__.p = <span class="hljs-string">""</span>;
  <span class="hljs-keyword">return</span> __webpack_require__(__webpack_require__.s = <span class="hljs-string">"./src/index.js"</span>);
&#125;)
(&#123;
  <span class="hljs-string">"./src/index.js"</span>:
    (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;
<span class="hljs-meta">      "use strict"</span>;
      <span class="hljs-comment">// 由于我们在index.js中使用了import所以，webpack贴心的在eval前面插入了一行代码调用了r方法</span>
      <span class="hljs-comment">// 我们去看看r干了啥</span>
      <span class="hljs-comment">// 回来了继续看下</span>
      <span class="hljs-comment">// 调用了__webpack_require__.n方法，传递的是import进来的文件中的exports对象</span>
      <span class="hljs-comment">// 所以我们要去瞅一眼import的文件是谁，没错是下面的./src/util.js</span>
      <span class="hljs-comment">// 这个文件没有用es6 module所以并没有像这个方法一样插入__webpack_require__.r方法</span>
      <span class="hljs-comment">// 所以他的exports对象上并没有一个叫__esModule的属性，我们继续</span>
      <span class="hljs-comment">// 去看下.n方法</span>
      <span class="hljs-built_in">eval</span>(<span class="hljs-string">"__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _util__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./util */ \"./src/util.js\");\n/* harmony import */ var _util__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_util__WEBPACK_IMPORTED_MODULE_0__);\n\n\nfunction test() &#123;\n  console.log('我是一个小测试！', _util__WEBPACK_IMPORTED_MODULE_0__[\"num\"]);\n&#125;\n\ntest();\n\n\n//# sourceURL=webpack:///./src/index.js?"</span>);
    &#125;),
  <span class="hljs-string">"./src/util.js"</span>: (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">module</span>, <span class="hljs-built_in">exports</span></span>) </span>&#123;
    <span class="hljs-built_in">eval</span>(<span class="hljs-string">"exports.num = 123;\n\n//# sourceURL=webpack:///./src/util.js?"</span>);
  &#125;)
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>完球了。。。这下清楚了吧~</p>
<p>聪明的你肯定知道webpack的按需加载，如果这时候让你去实现你会怎么做呢？有几种天然的分隔文件方式呢？多入口？<code>import()</code>?<code>import(/* prefetch 还有 preload*/)</code>了解下？文件分开了，根据分开的文件创建html<code><link as="script" src="...." rel="prefetch"></code>是不是就可以呢？</p>
<h3 data-id="heading-12">原理</h3>
<p>叽叽喳喳半天，通过上面的例子，其实我们已经知道了webpack的产物，我们也分析了打包后的产物，那么从原始文件到构建后的文件，这其中又经历了什么呢？</p>
<hr>
<p>未完待续</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            