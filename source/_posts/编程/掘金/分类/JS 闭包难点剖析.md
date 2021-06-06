
---
title: 'JS 闭包难点剖析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7288'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 06:53:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=7288'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">简介</h2>
<ol>
<li>JavaScript 中的作用域是什么意思?</li>
<li>闭包会在哪些场景中使用？</li>
<li>通过定时器循环输出自增的数字通过 JS 的代码如何实现？</li>
</ol>
<h2 data-id="heading-1">作用域基本介绍</h2>
<ul>
<li>JavaScript 的<strong>作用域</strong>通俗来讲，就是指变量能够被访问到的范围</li>
<li>在 JavaScript 中作用域中，ES5 之前只有<strong>全局作用域</strong>和<strong>函数作用域</strong>两种。</li>
<li>ES6 新增了块级作用域</li>
</ul>
<h3 data-id="heading-2">全局作用域</h3>
<p>在编程语言中，不论 Java 也好，JavaScript 也罢，变量一般都会分为<strong>全局变量</strong>和<strong>局部变量</strong>两种。</p>
<ul>
<li>那么变量定义在函数外部，代码最前面的一般情况下都是全局变量。</li>
<li>在 JavaScript 中，全局变量是挂载在 window 对象下的变量，所以在网页中的任何位置你都可以使用并且访问到这个全局变量</li>
<li>在 JavaScript 中所有没有经过定义，而直接被赋值的变量默认就是一个全局变量</li>
<li>现全局变量也是拥有全局的作用域，无论你在何处都可以使用它，在浏览器控制台输入 window.vName 的时候，就可以访问到 window 上所有全局变量。</li>
<li>全局变量的时候，会容易引起变量命名的冲突，所以在定义变量的时候应该注意作用域的问题。</li>
</ul>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-keyword">var</span> globalName = <span class="hljs-string">'global'</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getName</span>(<span class="hljs-params"></span>) </span>&#123; 
  <span class="hljs-built_in">console</span>.log(globalName) <span class="hljs-comment">// global</span>
  <span class="hljs-keyword">var</span> name = <span class="hljs-string">'inner'</span>
  <span class="hljs-built_in">console</span>.log(name) <span class="hljs-comment">// inner</span>
&#125; 
getName();
<span class="hljs-built_in">console</span>.log(name); <span class="hljs-comment">// </span>
<span class="hljs-built_in">console</span>.log(globalName); <span class="hljs-comment">//global</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setName</span>(<span class="hljs-params"></span>)</span>&#123; 
  vName = <span class="hljs-string">'setName'</span>;
&#125;
setName();
<span class="hljs-built_in">console</span>.log(vName); <span class="hljs-comment">// setName</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.vName) <span class="hljs-comment">// setName</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">函数作用域</h3>
<p>在 JavaScript 中，函数中定义的变量叫作函数变量，这个时候只能在函数内部才能访问到它，所以它的作用域也就是函数的内部，称为函数作用域</p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getName</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> name = <span class="hljs-string">'inner'</span>;
  <span class="hljs-built_in">console</span>.log(name); <span class="hljs-comment">//inner</span>
&#125;
getName();
<span class="hljs-built_in">console</span>.log(name);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了这个函数内部，其他地方都是不能访问到它的。同时，当这个函数被执行完之后，这个局部变量也相应会被销毁。所以你会看到在 getName 函数外面的 name 是访问不到的。</p>
<h3 data-id="heading-4">块级作用域</h3>
<ul>
<li>ES6 中新增了块级作用域，最直接的表现就是新增的 let 关键词</li>
<li>使用 let 关键词定义的变量只能在块级作用域中被访问，有“暂时性死区”的特点,也就是说这个变量在定义之前是不能被使用的</li>
<li>其实就是在 JS 编码过程中 <strong>if 语句及 for 语句后面 &#123;...&#125;</strong> 这里面所包括的，就是块级作用域。</li>
</ul>
<pre><code class="hljs language-TS copyable" lang="TS"><span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">//a is not defined</span>
<span class="hljs-keyword">if</span>(<span class="hljs-literal">true</span>)&#123;
  <span class="hljs-keyword">let</span> a = <span class="hljs-string">'123'</span>；
  <span class="hljs-built_in">console</span>.log(a)； <span class="hljs-comment">// 123</span>
&#125;
<span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">//a is not defined</span>
<span class="hljs-comment">// 变量 a 是在 if 语句&#123;...&#125; 中由 let 关键词进行定义的变量，所以它的作用域是 if 语句括号中的那部分</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">什么是闭包？</h2>
<p>先来看下红宝书上和 MDN 上给出的闭包的概念。</p>
<ul>
<li>红宝书闭包的定义：闭包是指有权<strong>访问另外一个函数作用域中的变量</strong>的函数。</li>
<li>MDN：一个<strong>函数和对其周围状态的引用捆绑在一起</strong>（或者说函数被引用包围），这样的组合就是闭包（closure）。也就是说，闭包让你可以在一个内层函数中访问到其外层函数的作用域。</li>
</ul>
<h3 data-id="heading-6">闭包的基本概念</h3>
<ul>
<li>通俗地讲解一下：闭包其实就是一个可以访问其他函数内部变量的函数。</li>
<li>即一个<strong>定义在函数内部的函数</strong>，或者直接说闭包是个内嵌函数也可以。</li>
</ul>
<p>通常情况下，函数内部变量是无法在外部访问的（即全局变量和局部变量的区别），因此使用闭包的作用，就具备实现了能在<strong>外部访问某个函数内部变量的功能</strong>，让这些内部变量的值始终可以保存在内存中。</p>
<pre><code class="hljs language-TS copyable" lang="TS"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun1</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(a);
    &#125;;
&#125;
fun1();
<span class="hljs-keyword">var</span> result = fun1();
result();  <span class="hljs-comment">// 1</span>

<span class="hljs-comment">// 可以很清楚地发现，a 变量作为一个 fun1 函数的内部变量，</span>
<span class="hljs-comment">//正常情况下作为函数内的局部变量，是无法被外部访问到的。但是通过闭包，我们最后还是可以拿到 a 变量的值。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">闭包产生的原因</h3>
<ul>
<li>我们需要明白作用域链的基本概念：当访问一个变量时，代码解释器会首先在当前的作用域查找，如果没找到，就去父级作用域去查找，直到找到该变量或者不存在父级作用域中，这样的链路就是作用域链。</li>
<li>需要注意的是，每一个子函数都会拷贝上级的作用域，形成一个作用域的链条</li>
</ul>
<pre><code class="hljs language-TS copyable" lang="TS"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun2</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">3</span>;
    <span class="hljs-built_in">console</span>.log(a);<span class="hljs-comment">//3</span>
  &#125;
&#125;
<span class="hljs-comment">// fun1 函数的作用域指向全局作用域（window）和它自己本身；</span>
<span class="hljs-comment">// fun2 函数的作用域指向全局作用域 （window）、fun1 和它本身；</span>
<span class="hljs-comment">// 而作用域是从最底层向上找，直到找到全局作用域 window 为止，如果全局还没有的话就会报错。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>即当前函数一般都会存在上层函数的作用域的引用，那么他们就形成了一条作用域链。</li>
</ul>
<h3 data-id="heading-8">闭包产生的本质就是</h3>
<ul>
<li><strong>当前环境中存在指向父级作用域的引用。</strong></li>
</ul>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun2</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a);  <span class="hljs-comment">// 2</span>
  &#125;
  <span class="hljs-keyword">return</span> fun2;
&#125;
<span class="hljs-keyword">var</span> result = fun1();
result();

<span class="hljs-comment">// 这里 result 会拿到父级作用域中的变量，输出 2。</span>
<span class="hljs-comment">// 因为在当前环境中，含有对 fun2 函数的引用，fun2 函数恰恰引用了 window、fun1 和 fun2 的作用域。</span>
<span class="hljs-comment">// 因此 fun2 函数是可以访问到 fun1 函数的作用域的变量。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那是不是只有返回函数才算是产生了闭包呢？</p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-keyword">var</span> fun3;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>
  fun3 = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a);
  &#125;
&#125;
fun1();
fun3();

<span class="hljs-comment">// 在给 fun3 函数赋值后，fun3 函数就拥有了 window、fun1 和 fun3 本身这几个作用域的访问权限；</span>
<span class="hljs-comment">// 然后还是从下往上查找，直到找到 fun1 的作用域中存在 a 这个变量；</span>
<span class="hljs-comment">// 因此输出的结果还是 2，最后产生了闭包，形式变了，本质没有改变。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此最后返回的不管是不是函数，也都不能说明没有产生闭包。</p>
<h2 data-id="heading-9">闭包的表现形式</h2>
<ul>
<li>我们来看看闭包的表现形式及应用场景到底有哪些呢？</li>
</ul>
<ol>
<li>返回一个函数，上面讲原因的时候已经说过，这里就不赘述了。</li>
<li>在定时器、事件监听、Ajax 请求、Web Workers 或者任何异步中，只要使用了回调函数，实际上就是在使用闭包。请看下面这段代码，这些都是平常开发中用到的形式。</li>
</ol>
<pre><code class="hljs language-TS copyable" lang="TS"><span class="hljs-comment">// 定时器</span>
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handler</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>);
&#125;，<span class="hljs-number">1000</span>);
<span class="hljs-comment">// 事件监听</span>
$(<span class="hljs-string">'#app'</span>).click(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Event Listener'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>作为函数参数传递的形式，比如下面的例子。</li>
</ol>
<pre><code class="hljs language-TS copyable" lang="TS"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">baz</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(a);
  &#125;
  bar(baz);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params">fn</span>)</span>&#123;
  <span class="hljs-comment">// 这就是闭包</span>
  fn();
&#125;
foo();  <span class="hljs-comment">// 输出2，而不是1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>IIFE（立即执行函数），创建了闭包，保存了全局作用域（window）和当前函数的作用域，因此可以输出全局的变量，如下所示。</li>
</ol>
<pre><code class="hljs language-TS copyable" lang="TS"><span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;
(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">IIFE</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(a);  <span class="hljs-comment">// 输出2</span>
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>IIFE 这个函数会稍微有些特殊，算是一种自执行匿名函数，这个匿名函数拥有独立的作用域。这不仅可以避免了外界访问此 IIFE 中的变量，而且又不会污染全局作用域，我们经常能在高级的 JavaScript 编程中看见此类函数。</li>
</ul>
<h2 data-id="heading-10">常见的开发应用场景</h2>
<ul>
<li>如何解决循环输出问题？</li>
</ul>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">5</span>; i ++)&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(i)
  &#125;, <span class="hljs-number">0</span>)
&#125;
<span class="hljs-comment">// 上面这段代码执行之后，从控制台执行的结果可以看出来，结果输出的是 5 个 6，那么一般面试官都会先问为什么都是 6？</span>
<span class="hljs-comment">// 我想让你实现输出 1、2、3、4、5 的话怎么办呢？</span>
<span class="hljs-comment">// 因此结合本讲所学的知识我们来思考一下，应该怎么给面试官一个满意的解释,可以围绕这两点来回答。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>setTimeout 为宏任务，由于 JS 中单线程 eventLoop 机制，在主线程同步任务执行完后才去执行宏任务，因此循环结束后 setTimeout 中的回调才依次执行。</li>
<li>因为 setTimeout 函数也是一种闭包，往上找它的父级作用域链就是 window，变量 i 为 window 上的全局变量，开始执行 setTimeout 之前变量 i 已经就是 6 了，因此最后输出的连续就都是 6。</li>
</ul>
<p>那么我们再来看看如何按顺序依次输出 1、2、3、4、5 呢？</p>
<h3 data-id="heading-11">利用 IIFE</h3>
<p>可以利用 IIFE（立即执行函数），当每次 for 循环时，把此时的变量 i 传递到定时器中，然后执行，改造之后的代码如下。</p>
<pre><code class="copyable">for(var i = 1;i <= 5;i++)&#123;
  (function(j)&#123;
    setTimeout(function timer()&#123;
      console.log(j)
    &#125;, 0)
  &#125;)(i)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">使用 ES6 中的 let</h3>
<p>ES6 中新增的 let 定义变量的方式，使得 ES6 之后 JS 发生革命性的变化，让 JS 有了块级作用域，代码的作用域以块级为单位进行执行。通过改造后的代码，可以实现上面想要的结果。</p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">5</span>; i++)&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(i);
  &#125;,<span class="hljs-number">0</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">定时器传入第三个参数</h3>
<p>setTimeout 作为经常使用的定时器，它是存在第三个参数的，日常工作中我们经常使用的一般是前两个，一个是回调函数，另外一个是时间，而第三个参数用得比较少。那么结合第三个参数，调整完之后的代码如下。</p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">1</span>;i<=<span class="hljs-number">5</span>;i++)&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">j</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(j)
  &#125;, <span class="hljs-number">0</span>, i)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从中可以看到，第三个参数的传递，可以改变 setTimeout 的执行逻辑，从而实现我们想要的结果，这也是一种解决循环输出问题的途径。</p>
<h2 data-id="heading-14">总结</h2>
<ul>
<li>
<p>到这里，本讲的内容就差不多结束了。这一讲我通过原理结合实践的方式，将闭包相关的知识点串起来剖析了一遍。你可以看到，其实闭包的知识整体上来说还是比较复杂的，它依赖一些相关的上游知识点。</p>
</li>
<li>
<p>另外，在日常的前端开发工作中，开发者往往会忽视对这部分知识的系统性学习，其实闭包的使用在日常的 JavaScript 编程中经常出现，使用的场景特别多而且复杂。由于闭包会使一些变量一直保存在内存中不会自动释放，所以如果大量使用的话就会消耗大量内存，从而影响网页性能。因此，你更应该深入理解闭包的原理，从而保证交付的代码性能更好。</p>
</li>
</ul></div>  
</div>
            