
---
title: 'let、const和块级作用域'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2505'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 23:41:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=2505'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">let、const和块级作用域</h2>
<h3 data-id="heading-1">let</h3>
<blockquote>
<p>ES6 新增了let命令，用来声明变量。</p>
<p>所声明的变量，只在let命令所在的代码块内有效。</p>
</blockquote>
<h4 data-id="heading-2">不存在变量提升</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// undefined</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="hljs-built_in">console</span>.log(b) <span class="hljs-comment">// Uncaught ReferenceError: b is not defined</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>var</code>命令会发生“变量提升”的现象，即在声明变量之前，这个变量可以使用但是值为<code>undefined</code>。</p>
<p>而<code>let</code>声明的变量，在声明语句之前使用就会报<code>ReferenceError</code>。</p>
<p>（但也并不是说这个变量就不存在，请看下一节暂时性死区。）</p>
<h4 data-id="heading-3">暂时性死区</h4>
<p>我们来看一个例子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="hljs-keyword">if</span>(<span class="hljs-literal">true</span>)&#123;
    <span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// Uncaught ReferenceError: Cannot access 'a' before initialization</span>
    <span class="hljs-keyword">let</span> a = <span class="hljs-number">2</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没有let声明语句，打印结果自然是1，但是有了let声明语句，在let所在的代码块中且在let语句之前使用a，就会报<code>ReferenceError</code>。</p>
<blockquote>
<p>ES6 明确规定，如果区块中存在let和const命令，这个区块对这些命令声明的变量，从一开始就形成了封闭作用域。凡是在声明之前就使用这些变量，就会报错。</p>
<p>这在语法上，称为“暂时性死区”（temporal dead zone，简称 TDZ）。</p>
</blockquote>
<p>由于暂时性死区的存在，导致<code>typeof</code>命令不再安全：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> a) <span class="hljs-comment">// "undefined"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通常情况下，我们使用<code>typeof</code>命令去判断一个未定义的变量，得到的结果是<code>"undefined"</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> a) <span class="hljs-comment">// Uncaught ReferenceError: a is not defined</span>
<span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于暂时性死区的存在，会直接报错。</p>
<blockquote>
<p>暂时性死区的本质就是，只要一进入当前作用域，所要使用的变量就已经存在了，但是不可获取。</p>
</blockquote>
<blockquote>
<p>ES6 规定暂时性死区和let、const语句不出现变量提升，主要是为了减少运行时错误，防止在变量声明前就使用这个变量，从而导致意料之外的行为。
这样的错误在 ES5 是很常见的，现在有了这种规定，避免此类错误就很容易了。</p>
</blockquote>
<h4 data-id="heading-4">不允许重复声明</h4>
<p><code>let</code>命令不能重复声明已经声明过的变量，无论这个变量是不是用<code>let</code>声明的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;
<span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// "undefined"</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> b = <span class="hljs-number">2</span>; <span class="hljs-comment">// Uncaught SyntaxError: Identifier 'b' has already been declared</span>
<span class="hljs-keyword">var</span> c = <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> c = <span class="hljs-number">2</span>; <span class="hljs-comment">// Uncaught SyntaxError: Identifier 'c' has already been declared</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">不会绑定全局对象</h4>
<p>let 声明的变量不会绑定要全局对象上，即便他是在全局作用域中声明的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.a) <span class="hljs-comment">// 1</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-number">2</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.b) <span class="hljs-comment">// "undefined"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">const</h3>
<blockquote>
<p><code>const</code>声明一个只读的常量。一旦声明，常量的值就不能改变。</p>
<p>这意味着，<code>const</code>一旦声明变量，就必须立即初始化，不能留到以后赋值。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a <span class="hljs-comment">// Uncaught SyntaxError: Missing initializer in const declaration</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类似于<code>let</code>，<code>const</code>只在声明所在的块级作用域内有效，不存在变量提升，存在暂时性死区，不可重复声明，不会绑定全局对象。</p>
<h3 data-id="heading-7">块级作用域</h3>
<h4 data-id="heading-8">为什么需要块级作用域？</h4>
<p>ES5 只有全局作用域和函数作用域，没有块级作用域，这就导致会出现下面这样的问题：</p>
<ul>
<li>由于变量提升，函数作用域内部的变量覆盖全局作用域的变量</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun</span>(<span class="hljs-params"></span>)</span>&#123;
   <span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// "undefined"</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-literal">false</span>)&#123;
        <span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;
    &#125;
&#125;
fun()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>循环计数作用的临时变量泄露到全局</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [];
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">5</span>; i++)&#123;
    arr[i]=i;
&#125;
<span class="hljs-built_in">console</span>.log(i) <span class="hljs-comment">// 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">ES6 块级作用域</h4>
<p>回忆一下：<code>let</code>声明的变量，只在let命令所在的代码块内有效。</p>
<p>也就是说，<code>let</code>的出现：</p>
<blockquote>
<p>实际上为 JavaScript 新增了块级作用域。</p>
</blockquote>
<p>上面的例子用let改写：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun</span>(<span class="hljs-params"></span>)</span>&#123;
   <span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// 1</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-literal">false</span>)&#123;
        <span class="hljs-keyword">let</span> a = <span class="hljs-number">2</span>;
    &#125;
&#125;
fun()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>if(false)</code>语句生成了一个新的块级作用域，即便条件为<code>false</code>不执行，外面的块级作用域可以跟她声明相同的变量：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun</span>(<span class="hljs-params"></span>)</span>&#123;
   <span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// 1</span>
    <span class="hljs-keyword">if</span>(<span class="hljs-literal">false</span>)&#123;
        <span class="hljs-keyword">let</span> a = <span class="hljs-number">2</span>;
    &#125;
&#125;
fun()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个例子可以通过let防止变量泄露：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [];
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">5</span>; i++)&#123;
    arr[i]=i;
&#125;
<span class="hljs-built_in">console</span>.log(i) <span class="hljs-comment">// Uncaught ReferenceError: i is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">块级作用域与函数声明</h4>
<blockquote>
<p>ES5 规定，函数只能在顶层作用域和函数作用域之中声明，不能在块级作用域声明。</p>
<p>但是，浏览器没有遵守这个规定，为了兼容以前的旧代码，还是支持在块级作用域之中声明函数。</p>
</blockquote>
<blockquote>
<p>ES6 引入了块级作用域，明确允许在块级作用域之中声明函数。
ES6 规定，块级作用域之中，函数声明语句的行为类似于let，在块级作用域之外不可引用。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am outside!'</span>); &#125;

(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-literal">false</span>) &#123;
    <span class="hljs-comment">// 重复声明一次函数f</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am inside!'</span>); &#125;
  &#125;

  f();
&#125;());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在ES5中，由于函数提升，上述例子会输出'I am inside!'。</p>
<p>而在ES6中，会报错:</p>
<blockquote>
<p>如果改变了块级作用域内声明的函数的处理规则，显然会对老代码产生很大影响。
为了减轻因此产生的不兼容问题，ES6 在附录 B里面规定，浏览器的实现可以不遵守上面的规定，有自己的行为方式。</p>
<ul>
<li>允许在块级作用域内声明函数。</li>
<li>函数声明类似于var，即会提升到全局作用域或函数作用域的头部。</li>
<li>同时，函数声明还会提升到所在的块级作用域的头部。</li>
</ul>
<p>考虑到环境导致的行为差异太大，应该避免在块级作用域内声明函数。如果确实需要，也应该写成函数表达式，而不是函数声明语句。</p>
</blockquote>
<hr>
<p>ES6 的块级作用域必须有大括号：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-literal">true</span>) <span class="hljs-keyword">let</span> x = <span class="hljs-number">1</span>; <span class="hljs-comment">// Uncaught SyntaxError: Lexical declaration cannot appear in a single-statement context</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没有大括号不存在块级作用域，而let只能出现在当前作用域的顶层，故报错。</p>
<p>函数声明相同：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-literal">true</span>) <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>非严格模式下不会报错，严格模式下报错：”Uncaught SyntaxError: In strict mode code, functions can only be declared at top level or inside a block.“</p>
<h3 data-id="heading-11">参考</h3>
<p><a href="https://es6.ruanyifeng.com/#docs/let" target="_blank" rel="nofollow noopener noreferrer">ECMAScript 6入门</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            