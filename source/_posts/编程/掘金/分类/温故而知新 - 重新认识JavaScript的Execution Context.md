
---
title: '温故而知新 - 重新认识JavaScript的Execution Context'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6914'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 02:25:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=6914'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>更新下相关知识，立足过往，拥抱未来。</p>
<h2 data-id="heading-0">概念</h2>
<p>直接看规范关于<code>ExecutionContext</code>的定义：</p>
<blockquote>
<p>An execution context is a specification device that is used to track the runtime evaluation of code by an ECMAScript implementation.</p>
</blockquote>
<p><code>ExecutionContext</code>为抽象概念，用来描述可执行代码的执行环境。可执行代码的运行，都是在<code>ExecutionContext</code>中。</p>
<h4 data-id="heading-1">管理方式<code>ExecutionContextStack</code></h4>
<p><code>Execution context Stack</code>为后进先出（LIFO）的栈结构。栈顶永远是<code>running execution context</code>。当控制从当前<code>execution context</code>对应可执行代码转移到另一段可执行代码时，相应的<code>execution context</code>将被创建，并压入栈顶，执行结束，对应的<code>execution context</code>从栈顶弹出。</p>
<h5 data-id="heading-2">思索：什么<code>ECMAScript</code>特性会使<code>Execution context stack</code>不遵循<code>LIFO</code>规则？</h5>
<p>规范里面提到：</p>
<blockquote>
<p>Transition of the running execution context status among execution contexts usually occurs in stack-like last-in/first-out manner. However, some ECMAScript features require non-LIFO transitions of the running execution context.</p>
</blockquote>
<p>然后在规范里面，并没有找到<code>some ECMAScript features</code>到底是什么特性。不过，第一反应，<code>Generator</code>算不算？在stackoverflow上，有这么一个讨论<a href="https://stackoverflow.com/questions/48365754/execution-context-stack-violation-of-the-lifo-order-using-generator-function?r=SearchResults#" target="_blank" rel="nofollow noopener noreferrer">Execution Context Stack. Violation of the LIFO order using Generator Function</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">gen</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-number">2</span>;
&#125;

<span class="hljs-keyword">let</span> g = gen();

<span class="hljs-built_in">console</span>.log(g.next().value);
<span class="hljs-built_in">console</span>.log(g.next().value);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用一个函数时，当前<code>execution context</code>暂停执行，被调用函数的<code>execution context</code>创建并压入栈顶，当函数返回时，函数<code>execution context</code>被销毁，暂停的<code>execution context</code>得以恢复执行。</p>
<p>现在，使用的是<code>Generator</code>，<code>Generator</code>函数的<code>execution context</code>在返回<code>yield</code>表达式的值之后仍然存在，并未销毁，只是暂停并移交出了控制权，可能在某些时候恢复执行。</p>
<p>究竟是不是呢？有待求证。</p>
<h3 data-id="heading-3">词法环境<code>Lexical Environments</code></h3>
<p>看规范的定义：</p>
<blockquote>
<p>A Lexical Environment is a specification type used to define the association of Identifiers to specific variables and functions based upon the lexical nesting structure of ECMAScript code.</p>
</blockquote>
<p>按规范来说，<code>Lexical Environment</code>定义了标识<code>identifiers</code>与<code>Variables</code>或<code>Functions</code>的映射。</p>
<h4 data-id="heading-4">组成 <code>Lexical Environment</code>包含两部分：</h4>
<ul>
<li><code>Environment Record</code></li>
</ul>
<p>记录被创建的标识<code>identifiers</code>与<code>Variables</code>或<code>Functions</code>的映射</p>





























<table><thead><tr><th>类型</th><th>简述</th></tr></thead><tbody><tr><td><a href="https://262.ecma-international.org/10.0/#sec-declarative-environment-records" target="_blank" rel="nofollow noopener noreferrer">Declarative Environment Records</a></td><td>记录 <code>var</code>、<code>const</code>、<code>let</code>、<code>class</code>、<code>import</code>、<code>function</code>等声明</td></tr><tr><td><a href="https://262.ecma-international.org/10.0/#sec-object-environment-records" target="_blank" rel="nofollow noopener noreferrer">Object Environment Records</a></td><td>与某对象绑定，记录该对象中<code>string identifier</code>的属性，非<code>string identifier</code>的属性不会被记录。<code>Object environment records</code>为<code>with</code>语句所创建</td></tr><tr><td><a href="https://262.ecma-international.org/10.0/#sec-function-environment-records" target="_blank" rel="nofollow noopener noreferrer">Function Environment Records</a></td><td><code>Declarative Environment Records</code>的一种，用于函数的顶层，如果为非箭头函数的情况，提供<code>this</code>的绑定，若还引用了 <code>super</code>则提供<code>super</code>方法的绑定</td></tr><tr><td><a href="https://262.ecma-international.org/10.0/#sec-global-environment-records" target="_blank" rel="nofollow noopener noreferrer">Global Environment Records</a></td><td>包含所有顶层声明及<code>global object</code>的属性，<code>Declarative Environment Records</code>与<code>Object Environment Records</code>的组合</td></tr><tr><td><a href="https://262.ecma-international.org/10.0/#sec-module-environment-records" target="_blank" rel="nofollow noopener noreferrer">Module Environment Records</a></td><td><code>Declarative Environment Records</code>的一种，用于<code>ES module</code>的顶层，除去常量和变量的声明，还包含不可变的<code>import</code>的绑定，该绑定提供了到另一<code>environment records</code>的间接访问</td></tr></tbody></table>
<ul>
<li>外部<code>Lexical Environment</code>的引用</li>
</ul>
<p>通过引用构成了嵌套结构，引用可能为<code>null</code></p>
<h4 data-id="heading-5">分类 <code>Lexical Environment</code>分三类：</h4>
<ul>
<li><code>Global Environment</code></li>
</ul>
<p>没有外部<code>Lexical Environment</code>的<code>Lexical Environment</code></p>
<ul>
<li><code>Module Environment</code></li>
</ul>
<p>包含了模块顶层的声明以及导入的声明，外部<code>Lexical Environment</code>为<code>Global Environment</code></p>
<ul>
<li><code>Function Environment</code></li>
</ul>
<p>对应于<code>JavaScript</code>中的函数，其会建立<code>this</code>的绑定以及必要的<code>super</code>方法的绑定</p>
<h3 data-id="heading-6">变量环境<code>Variable Environments</code></h3>
<p>在ES6前，声明变量都是通过<code>var</code>声明的，在ES6后有了<code>let</code>和<code>const</code>进行声明变量，为了兼容<code>var</code>，便用<code>Variable Environments</code>来存储<code>var</code>声明的变量。</p>
<p><code>Variable Environments</code>实质上仍为<code>Lexical Environments</code></p>
<h2 data-id="heading-7">机制</h2>
<p>具体可以参考规范<a href="https://262.ecma-international.org/10.0/" target="_blank" rel="nofollow noopener noreferrer">ECMAScript 2019 Language Specification</a>。相关的是在<a href="https://262.ecma-international.org/10.0/#sec-execution-contexts" target="_blank" rel="nofollow noopener noreferrer"><code>8.3 Execution Contexts</code></a>。</p>
<p>一篇很不错的文章参考<a href="https://blog.bitsrc.io/understanding-execution-context-and-execution-stack-in-javascript-1c9ea8642dd0" target="_blank" rel="nofollow noopener noreferrer"><code>Understanding Execution Context and Execution Stack in Javascript</code></a>， 该文章的中文翻译版<a href="https://juejin.cn/post/6844903682283143181#heading-8" target="_blank">中文版</a></p>
<p>参考里面的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">20</span>;
<span class="hljs-keyword">var</span> b = <span class="hljs-number">40</span>;
<span class="hljs-keyword">let</span> c = <span class="hljs-number">60</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">d, e</span>) </span>&#123;
    <span class="hljs-keyword">var</span> f = <span class="hljs-number">80</span>;
    
    <span class="hljs-keyword">return</span> d + e + f;
&#125;

c = foo(a, b);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建的<code>Execution Context</code>像这样：</p>
<pre><code class="hljs language-js copyable" lang="js">GlobalExecutionContext = &#123;
  <span class="hljs-attr">LexicalEnvironment</span>: &#123;
    <span class="hljs-attr">EnvironmentRecord</span>: &#123;
      <span class="hljs-attr">Type</span>: <span class="hljs-string">"Object"</span>,
      <span class="hljs-attr">c</span>: < uninitialized >,
      foo: < func >
    &#125;
    <span class="hljs-attr">outer</span>: <<span class="hljs-literal">null</span>>,
    ThisBinding: <Global Object>
  &#125;,
  VariableEnvironment: &#123;
    EnvironmentRecord: &#123;
      Type: "Object",
      // Identifier bindings go here
      a: undefined,
      b: undefined,
    &#125;
    outer: <null>, 
    ThisBinding: <Global Object>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在运行阶段，变量赋值已经完成。因此<code>GlobalExecutionContext</code>在执行阶段看起来就像是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js">GlobalExecutionContext = &#123;
  <span class="hljs-attr">LexicalEnvironment</span>: &#123;
    <span class="hljs-attr">EnvironmentRecord</span>: &#123;
      <span class="hljs-attr">Type</span>: <span class="hljs-string">"Object"</span>,
      <span class="hljs-attr">c</span>: <span class="hljs-number">60</span>,
      <span class="hljs-attr">foo</span>: < func >,
    &#125;
    <span class="hljs-attr">outer</span>: <<span class="hljs-literal">null</span>>,
    ThisBinding: <Global Object>
  &#125;,
  VariableEnvironment: &#123;
    EnvironmentRecord: &#123;
      Type: "Object",
      // Identifier bindings go here
      a: 20,
      b: 40,
    &#125;
    outer: <null>, 
    ThisBinding: <Global Object>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当遇到函数<code>foo(a, b)</code>的调用时，新的<code>FunctionExecutionContext</code>被创建并执行函数中的代码。在创建阶段像这样：</p>
<pre><code class="hljs language-js copyable" lang="js">FunctionExecutionContext = &#123;
  <span class="hljs-attr">LexicalEnvironment</span>: &#123;
    <span class="hljs-attr">EnvironmentRecord</span>: &#123;
      <span class="hljs-attr">Type</span>: <span class="hljs-string">"Declarative"</span>,
      <span class="hljs-attr">Arguments</span>: &#123;<span class="hljs-number">0</span>: <span class="hljs-number">20</span>, <span class="hljs-number">1</span>: <span class="hljs-number">40</span>, <span class="hljs-attr">length</span>: <span class="hljs-number">2</span>&#125;,
    &#125;,
    <span class="hljs-attr">outer</span>: <GlobalLexicalEnvironment>,
    ThisBinding: <Global Object or undefined>,
  &#125;,
  VariableEnvironment: &#123;
    EnvironmentRecord: &#123;
      Type: "Declarative",
      f: undefined
    &#125;,
    outer: <GlobalLexicalEnvironment>,
    ThisBinding: <Global Object or undefined>,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行完后，看起来像这样：</p>
<pre><code class="hljs language-js copyable" lang="js">FunctionExecutionContext = &#123;
  <span class="hljs-attr">LexicalEnvironment</span>: &#123;
    <span class="hljs-attr">EnvironmentRecord</span>: &#123;
      <span class="hljs-attr">Type</span>: <span class="hljs-string">"Declarative"</span>,
      <span class="hljs-attr">Arguments</span>: &#123;<span class="hljs-number">0</span>: <span class="hljs-number">20</span>, <span class="hljs-number">1</span>: <span class="hljs-number">40</span>, <span class="hljs-attr">length</span>: <span class="hljs-number">2</span>&#125;,
    &#125;,
    <span class="hljs-attr">outer</span>: <GlobalLexicalEnvironment>,
    ThisBinding: <Global Object or undefined>,
  &#125;,
  VariableEnvironment: &#123;
    EnvironmentRecord: &#123;
      Type: "Declarative",
      f: 80
    &#125;,
    outer: <GlobalLexicalEnvironment>,
    ThisBinding: <Global Object or undefined>,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在函数执行完成以后，返回值会被存储在<code>c</code>里。因此<code>GlobalExecutionContext</code>更新。在这之后，代码执行完成，程序运行终止。</p>
<h2 data-id="heading-8">总结</h2>
<p><code>ECMAScript</code>规范是年年都在更新，得与时俱进的加强学习，立足过往及当下，拥抱未来！</p>
<h2 data-id="heading-9">参考资料</h2>
<ol>
<li><a href="https://blog.huli.tw/2018/12/08/javascript-closure/" target="_blank" rel="nofollow noopener noreferrer">所有的函式都是閉包：談 JS 中的作用域與 Closure</a></li>
<li><a href="https://my.oschina.net/u/4347428/blog/4263452" target="_blank" rel="nofollow noopener noreferrer">JS夯实之执行上下文与词法环境</a></li>
<li><a href="https://blog.csdn.net/qq_35368183/article/details/103888311" target="_blank" rel="nofollow noopener noreferrer">结合 JavaScript 规范来谈谈 Execution Contexts 与 Lexical Environments</a></li>
<li><a href="https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch1.md" target="_blank" rel="nofollow noopener noreferrer">You-Dont-Know-JS 2nd-ed</a></li>
<li><a href="https://262.ecma-international.org/10.0/" target="_blank" rel="nofollow noopener noreferrer">ECMAScript 2019 Language Specification</a></li>
<li><a href="https://blog.bitsrc.io/understanding-execution-context-and-execution-stack-in-javascript-1c9ea8642dd0" target="_blank" rel="nofollow noopener noreferrer">Understanding Execution Context and Execution Stack in Javascript</a></li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            