
---
title: 'javascript之作用域与this指向'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7553'
author: 掘金
comments: false
date: Fri, 02 Apr 2021 18:17:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=7553'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近一周一直在思考一个问题，javascript的作用域(scope)究竟是什么？我们到底该如何去定义它呢？为此查阅了很多文章，特地去买了《你不知道的javascript》阅读学习了一番，有所收获。</p>
<blockquote>
<p>作用域</p>
</blockquote>
<p>针对作用域是什么这个问题，结合了相关的资料，笔者主观的将作用域定义为：</p>
<p>从狭义的角度来讲，javascript作用域可以理解为变量，对象和函数的可访问范围。换句话说，作用域决定了代码中变量，对象以及函数的可访问性，作用域是一个独立的地盘，使得变量不会外泄。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">outFun</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;
&#125;
outFun(); 
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// uncaught ReferenceError: a is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从广义的角度来讲，作用域是一套规则，用于确定在何处以及如何查找变量(标识符)。如果查找的目的是对变量进行赋值，那么就会使用LHS查询(赋值操作的目标是谁)；如果目的是获取变量的值，就会使用RHS查询(谁是赋值操作的源头)。javascript引擎首先会在代码执行前对其进行编译，在这个过程中，像var a = 2这样的声明会被分解成两个独立的步骤：</p>
<ol>
<li>首先，var a在其作用域中声明新变量，这是在代码执行前进行的。</li>
<li>接下来，a = 2会查询(LHS查询)变量a并对其进行赋值。</li>
</ol>
<p>LHS和RHS查询都会在当前执行作用域中开始，如果有需要就会向上一级作用域继续查找目标标识符，直到抵达全局作用域。但RHS和LHS的不同在于，不成功的RHS引用会导致抛出ReferenceError异常，不成功的LHS引用在非严格模式下会自动隐式的创建一个全局变量，改变量使用LHS引用的目标作为标识符，在严格模式下才会抛出ReferenceError异常。</p>
<blockquote>
<p>词法作用域</p>
</blockquote>
<p>词法作用域是指作用域由书写代码时函数或变量声明的位置来决定的，编译的词法分析阶段基本知道全部标识符在哪里以及是如何声明的。javascript采用的就是词法作用域，也称为静态作用域。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> value = <span class="hljs-number">1</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(value);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> value = <span class="hljs-number">2</span>;
    foo();
&#125;

bar(); <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>javascript中有两个机制可以“欺骗”词法作用域：eval(...)和with。eval()可以对一段包含一个或多个声明的代码直接执行，就好像代码是写在那个位置一样，并借此对所处的词法作用域进行修改。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">str, a</span>) </span>&#123;
  <span class="hljs-built_in">eval</span>(str);
  <span class="hljs-built_in">console</span>.log(a, b);
&#125;
<span class="hljs-keyword">var</span> b = <span class="hljs-number">2</span>;
foo(<span class="hljs-string">"var b = 3;"</span>, <span class="hljs-number">1</span>); <span class="hljs-comment">// 1, 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>with本质上是通过将一个对象的引用当作作用域来处理，将对象的属性当作作用域中的标识符来处理，从而创建了一个新的词法作用域。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-title">with</span>(<span class="hljs-params">obj</span>)</span> &#123;
    a = <span class="hljs-number">2</span>;
  &#125;
&#125;

<span class="hljs-keyword">var</span> o1 = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">3</span>
&#125;;

<span class="hljs-keyword">var</span> o2 = &#123;
  <span class="hljs-attr">b</span>: <span class="hljs-number">3</span>
&#125;;

foo(o1);
<span class="hljs-built_in">console</span>.log(o1.a); <span class="hljs-comment">// 2</span>

foo(o2);
<span class="hljs-built_in">console</span>.log(o2.a); <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以注意到一个奇怪的现象，实际上a = 2的赋值操作创建了一个全局的变量a。这是因为尽管with块可以将一个对象处理为词法作用域，但是这个块的内部正常的var声明并不会被限制在这个快的作用域中，而是被添加到with所处的函数作用域中，在执行foo(o2)时，由于a = 2是LSH引用，在obj的词法作用域、foo(...)的作用域和全局作用域都没找到a标识符，因此a = 2执行时，自动创建了一个全局变量。</p>
<blockquote>
<p>全局作用域与局部作用域</p>
</blockquote>
<p>javascript的作用域分为全局作用域和局部作用域，局部作用域包含函数作用域与块级作用域。</p>
<p>全局作用域贯穿整个javascript文档，在任何地方都能访问到的对象拥有全局作用域。一般来说最外层函数和在最外层函数外面定义的变量、未声明直接赋值的变量以及所有window对象的属性拥有全局作用域。</p>
<p>局部作用域是指变量只能在函数或代码块的内部被访问。函数作用域是最常见的作用域单元，我们在任意代码片段外部添加包装函数，都可以将内部的变量和函数“隐藏起来”，外部作用域无法访问包装函数的任何内容。</p>
<p>但函数不是唯一的作用域单元，块作用域指的是变量和函数不仅可以属于所处的作用域，也可以属于某个代码块，通常指&#123;...&#125;内部，ES6新增let和const关键字，所声明的变量属于块作用域，在指定块的作用域外无法被访问。</p>
<p>let/const声明的变量不会被提升到当前代码块的顶部，即不存在变量提升。实际上在let/const定义的变量首先会创建到TDZ，在初始化之前引用会直接报错。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(a);
  <span class="hljs-keyword">let</span> a;
&#125;
test(); <span class="hljs-comment">// Uncaught ReferenceError: Cannot access 'a' before initialization</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test1</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(b);
  <span class="hljs-keyword">const</span> b = <span class="hljs-number">2</span>;
&#125;
test1(); <span class="hljs-comment">// Uncaught ReferenceError: Cannot access 'b' before initialization</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test2</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">let</span> a;
  <span class="hljs-built_in">console</span>.log(a);
&#125;
test2(); <span class="hljs-comment">// undefined</span>

<span class="hljs-built_in">console</span>.log(c);
<span class="hljs-keyword">let</span> c; <span class="hljs-comment">// Uncaught ReferenceError: c is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上，块作用域还有其他的方式，上述提到的with关键字便是块作用域的一个例子，try/catch结构的catch分句也是具有块作用域的，其中声明的变量仅在catch内部有效。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">try</span>&#123;
  <span class="hljs-literal">undefined</span>(); <span class="hljs-comment">// 执行一个非法操作来抛出一个异常</span>
&#125;
<span class="hljs-keyword">catch</span>(err) &#123;
  <span class="hljs-built_in">console</span>.log(err); <span class="hljs-comment">// 能够正常执行 undefined is not a function</span>
&#125;

<span class="hljs-built_in">console</span>.log(err); <span class="hljs-comment">// Uncaught ReferenceError: err is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>执行上下文</p>
</blockquote>
<p>执行上下文(execution context)是评估和执行javascript代码的环境的抽象概念。每当javascript代码在运行的时候，它都是在执行上下文中运行的。我们可以将它理解为一个object，ES5中的执行上下文包括this绑定、词法环境组件(LexicalEnvironment component)和变量环境组件(VariableEnvironment component)。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ExcutionContext = &#123;
  ThisBinding = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">this</span> <span class="hljs-attr">value</span>></span>,
  LexicalEnvironment = &#123;...&#125;,
  VariableEnvironment = &#123;...&#125;,
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>This Binding</p>
<ul>
<li>全局执行上下文中，this的值指向window对象，而在nodejs中指向这个文件的module对象。</li>
<li>函数执行上下文中，this的值取决于函数的调用方式，后续将会介绍。</li>
</ul>
<p>词法环境（Lexical Environment）</p>
<p>词法环境包括两个部分：</p>
<ol>
<li>环境记录：存储变量和函数声明的实际位置</li>
<li>对外部环境的引用：可以访问其外部环境</li>
</ol>
<p>词法环境有两种类型</p>
<ol>
<li>全局环境：是一个没有外部环境的词法环境。其外部引用为null，拥有一个全局对象window及其关联的方法和属性以及任何用户自定义的全局变量</li>
<li>函数环境：用户在函数中定义的变量被存储在环境记录中，包括了arguments对象。对外部环境的引用为全局环境或包含内部函数的外部函数环境。</li>
</ol>
<p>变量环境（Variable Environment）</p>
<p>变量环境也是一个词法环境，ES6中，词法环境和变量环境的区别在于前者用于存储函数声明和let/const声明的变量，后者仅用于存储var声明的变量。</p>
<p>执行栈，也就是其他语言所说的“调用栈”，是一种拥有LIFO(后进先出)数据结构的栈，用来存储代码运行时创建的所有执行上下文。每当引擎遇到一个函数调用，就会为该函数创建一个新的执行上下文并压入执行栈的顶部，由于javascript引擎是单线程的，它会执行那些执行上下文位于栈顶的函数，当函数执行结束后执行上下文从栈中弹出，开始执行栈中的下一个上下文。</p>
<p>javascript属于解释型语言，它的执行可以分为编译阶段和执行阶段，作用域和执行上下文最大的区别在于：作用域在定义时就确定了，并不会改变，即javascript在编译阶段便会确定作用域规则；执行上下文在运行时确定，随时可能改变。同一个作用域下，不同的调用会产生不同的执行上下文环境，继而产生不同的变量的值。</p>
<blockquote>
<p>作用域链</p>
</blockquote>
<p>前面说过，作用域是根据标识符查找变量的一套规则，当一个块或函数嵌套在另一个块或函数中时，就发生了作用域嵌套，这样就形成了作用域链，引擎会根据作用域链来查找变量，从当前的执行作用域开始查找，如果找不到，就向上一级继续查找，直到最外层的全局作用域。</p>
<blockquote>
<p>闭包</p>
</blockquote>
<p>针对闭包的定义，是指有权访问另一个函数作用域中的变量的函数。《你不知道的javascript》中定义闭包：当函数可以记住并访问所在的词法作用域时，就产生了闭包，即使函数是在当前词法作用域之外执行。由此可见，闭包发生的对象是函数，而产生闭包的条件是对外部词法环境的访问。闭包的示例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a);
  &#125;
  
  <span class="hljs-keyword">return</span> bar;
&#125;

<span class="hljs-keyword">var</span> baz = foo();

baz(); <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i <= <span class="hljs-number">5</span>; i++) &#123;
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timer</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(i);
  &#125;,i*<span class="hljs-number">1000</span>)
&#125; 
<span class="hljs-comment">// 会打印6次6</span>

<span class="hljs-comment">// 利用let创建块作用域，timer函数访问块作用域中的i,产生闭包</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <= <span class="hljs-number">5</span>; i++) &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timer</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(i)
  &#125;,i*<span class="hljs-number">1000</span>);
&#125;
<span class="hljs-comment">// 0</span>
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// 3</span>
<span class="hljs-comment">// 4</span>
<span class="hljs-comment">// 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-0">利用闭包实现斐波那契数列</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fibonache</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> fn1 = <span class="hljs-number">1</span>;
  <span class="hljs-keyword">let</span> fn2 = <span class="hljs-number">1</span>;
  <span class="hljs-keyword">let</span> current;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    current = fn1;
    fn1 = fn2;
    fn2 = current + fn2;
    <span class="hljs-keyword">return</span> current;
  &#125;
&#125;
<span class="hljs-keyword">const</span> f = fibonache();
<span class="hljs-built_in">console</span>.log(f()); <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(f()); <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(f()); <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(f()); <span class="hljs-comment">// 3</span>
<span class="hljs-built_in">console</span>.log(f()); <span class="hljs-comment">// 5</span>
<span class="hljs-built_in">console</span>.log(f()); <span class="hljs-comment">// 8</span>
<span class="hljs-built_in">console</span>.log(f()); <span class="hljs-comment">// 13</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-1">利用闭包实现函数缓存</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> memorize = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn</span>) </span>&#123;
  <span class="hljs-keyword">const</span> cache = &#123;&#125;;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) </span>&#123;
    <span class="hljs-keyword">const</span> _args = <span class="hljs-built_in">JSON</span>.stringify(args);
    <span class="hljs-keyword">return</span> cache[_args] || (cache[_args] = fn.apply(fn, args));
  &#125;
&#125;

<span class="hljs-keyword">const</span> add = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">a</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'call 1 time'</span>);
  <span class="hljs-keyword">return</span> a + <span class="hljs-number">1</span>;
&#125;

<span class="hljs-keyword">const</span> adder = memorize(add);

<span class="hljs-built_in">console</span>.log(adder(<span class="hljs-number">1</span>)); 
<span class="hljs-built_in">console</span>.log(adder(<span class="hljs-number">1</span>));
<span class="hljs-built_in">console</span>.log(adder(<span class="hljs-number">2</span>));

<span class="hljs-comment">// call 1 time</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// call 1 time</span>
<span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>this指向</p>
</blockquote>
<p>javascript中的this指向问题是其特别重要的知识点，我们需要深入理解并掌握。判断一个运行中函数的this绑定，就需要找到这个函数的直接调用位置，调用位置决定了this的绑定对象。javascript中有四种this绑定规则：默认绑定、隐式绑定、显示绑定和new绑定。</p>
<p>默认绑定</p>
<p>默认绑定作用于独立函数直接调用的情况下，此时this指向全局对象，但严格模式下this指向undefined。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;

<span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;

foo(); <span class="hljs-comment">// 2</span>

<span class="hljs-comment">// 严格模式</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-meta">  "use strict"</span>;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a)
&#125;

<span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>;

foo(); <span class="hljs-comment">// TypeError: Cannot read property 'a' of undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>隐式绑定</p>
<p>如果函数的调用位置有上下文对象，或者函数被某个对象拥有或包含，那么this绑定符合隐式绑定的规则，谁调用它指向谁。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;

<span class="hljs-keyword">var</span> a = <span class="hljs-number">42</span>;

<span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">foo</span>: foo
&#125;;

obj.foo(); <span class="hljs-comment">// 2 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>foo函数调用时有上下文对象，隐式绑定规则会将函数调用中的this绑定到这个上下文对象，即obj调用的foo，故this指向obj，因此函数中的this.a = obj.a。对象属性引用链中只有最顶层会影响调用位置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;

<span class="hljs-keyword">var</span> obj2 = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">42</span>,
    <span class="hljs-attr">foo</span>: foo
&#125;

<span class="hljs-keyword">var</span> obj1 = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">obj2</span>: obj2
&#125;

obj1.obj2.foo(); <span class="hljs-comment">// 42</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>隐式绑定需要特别注意的一个问题是，它会存在隐式丢失的现象，即被隐式绑定的函数会丢失绑定对象，应用默认绑定，从而将this绑定到全局对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;

<span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">foo</span>: foo
&#125;;

<span class="hljs-keyword">var</span> bar = obj.foo;
<span class="hljs-keyword">var</span> a = <span class="hljs-number">42</span>;
bar(); <span class="hljs-comment">// 42</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上例中，虽然bar是obj.foo的一个引用，但实际上bar引用的是foo函数本身，相当于foo函数的一个别名，故bar() = foo()，因此此时bar()相当于直接调用foo()函数，此时将应用默认绑定，this指向全局变量</p>
<p>显示绑定</p>
<p>之前介绍Function对象时已经提过，javascript的所有函数都是Function对象，他们都具有实例方法call()和apply()。这两个方法的第一个参数都是一个对象，函数调用call()或apply()会将函数执行时的this绑定到这个对象上。因为我们可以直接指定this的绑定对象，因此将之称之为显示绑定规则。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;

<span class="hljs-keyword">var</span> a = <span class="hljs-number">42</span>;

<span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">2</span>
&#125;

foo.call(obj); <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>new绑定</p>
<p>javascript中构造函数可以通过new操作符来被调用并实例化一个对象，它们不属于某个类，只是被new操作符调用的普通函数。在使用new调用函数时，会自动执行下面的步骤：</p>
<ol>
<li>创建一个新对象</li>
<li>将构造函数的作用域赋值给新对象（this指向了这个新对象）</li>
<li>执行构造函数的代码（为这个新对象添加属性）</li>
<li>返回该对象</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">a</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.a = a;
&#125;

<span class="hljs-keyword">var</span> a = <span class="hljs-number">42</span>;

<span class="hljs-keyword">var</span> bar = <span class="hljs-keyword">new</span> foo(<span class="hljs-number">2</span>);

<span class="hljs-built_in">console</span>.log(bar.a); <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// js实现new</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myNew</span>(<span class="hljs-params">fn</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// 创建一个新对象，并将其隐式原型指向构造函数的原型</span>
    <span class="hljs-keyword">let</span> obj = &#123;
      <span class="hljs-attr">__proto__</span>: fn.prototype
    &#125;;
    <span class="hljs-comment">// this指向新对象，并执行构造函数的代码</span>
    fn.call(obj, ...arguments);
    <span class="hljs-comment">// 返回新对象</span>
    <span class="hljs-keyword">return</span> obj;
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-built_in">this</span>.age = age;
&#125;

<span class="hljs-keyword">let</span> obj = myNew(Person)(<span class="hljs-string">'zhang'</span>, <span class="hljs-number">18</span>);

<span class="hljs-built_in">console</span>.log(obj); <span class="hljs-comment">// &#123;name: 'zhang', age: 18&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，this绑定的优先级为：new > 显式 > 隐式 > 默认</p>
<blockquote>
<p>箭头函数</p>
</blockquote>
<p>ES6中，箭头函数是其中最有趣的新增特性，也是前端面试环节的一个高频考点，它的语法比一般的函数更加简洁，所以也是我们日常开发中经常使用的。箭头函数是一种使用箭头(=>)定义函数的新语法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> reflect = <span class="hljs-function"><span class="hljs-params">value</span> =></span> value;

<span class="hljs-comment">// 实际相当于：</span>
<span class="hljs-keyword">let</span> reflect = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-keyword">return</span> value;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>箭头函数与普通函数的主要区别有：</p>
<p>1.箭头函数本身没有this，箭头函数的this指向其代码外层所在的词法作用域（父作用域）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">foo</span>: <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
  &#125;
&#125;

obj.foo(); <span class="hljs-comment">// window 此时this指向父作用域，而在js中，只有创建函数才能开辟一块作用域,obj只是对象，故此时的父级作用域：window</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.箭头函数没有arguments对象，取而代之用rest参数...代替arguments对象，来访问箭头函数的参数列表</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 普通函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">a</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>);
&#125;

foo(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>); <span class="hljs-comment">// [1, 2, 3, 4, callee: ƒ, Symbol(Symbol.iterator): ƒ]</span>

<span class="hljs-comment">// 箭头函数</span>

<span class="hljs-keyword">let</span> foo = <span class="hljs-function">(<span class="hljs-params">b</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>);
&#125;

foo(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>); <span class="hljs-comment">// ReferenceError: arguments is not defined</span>

<span class="hljs-comment">// rest参数...</span>
<span class="hljs-keyword">let</span> foo = <span class="hljs-function">(<span class="hljs-params">...c</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(c);
&#125;

foo(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>); <span class="hljs-comment">// [1,2,3,4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.不能通过new关键字调用，箭头函数没有[[Construct]]方法，所以箭头函数不能被用作构造函数。其实从上面的内容可以知道，new关键字的其中步骤是将函数中的this指向新对象，而箭头函数本身是没有this的，因此也可以看出其不能被new关键字调用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> Person = <span class="hljs-function">(<span class="hljs-params">name, age</span>) =></span> &#123;
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-built_in">this</span>.age = age;
&#125;

<span class="hljs-keyword">let</span> obj = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'zhang'</span>, <span class="hljs-number">18</span>); <span class="hljs-comment">// TypeError: Person is not a constructor</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.箭头函数没有原型，由于不可以通过new关键字调用箭头函数，因此没有构建原型的需求，所以箭头函数不存在prototype这个属性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 箭头函数</span>
<span class="hljs-keyword">let</span> foo = <span class="hljs-function">() =></span> &#123;&#125;;
<span class="hljs-built_in">console</span>.log(foo.prototype); <span class="hljs-comment">// undefined</span>

<span class="hljs-comment">// 普通函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;&#125;;
<span class="hljs-built_in">console</span>.log(foo.prototype); <span class="hljs-comment">// &#123;constructor: ƒ&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.不可以通过call|apply|bind改变箭头函数的this指向，箭头函数的内部this值在定义时已经确定了，在函数的生命周期内始终保持一致。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span>;
<span class="hljs-keyword">let</span> foo = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;

foo();               <span class="hljs-comment">// 10</span>
foo.call(&#123;<span class="hljs-attr">a</span>: <span class="hljs-number">20</span>&#125;);   <span class="hljs-comment">// 10</span>
foo.apply(&#123;<span class="hljs-attr">a</span>: <span class="hljs-number">20</span>&#125;);  <span class="hljs-comment">// 10</span>
foo.bind(&#123;<span class="hljs-attr">a</span>: <span class="hljs-number">20</span>&#125;)(); <span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            