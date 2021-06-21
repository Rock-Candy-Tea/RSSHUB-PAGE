
---
title: '_译_理解Javascript中的执行上下文和执行栈'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1495'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 01:48:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=1495'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原文地址：<a href="https://blog.bitsrc.io/understanding-execution-context-and-execution-stack-in-javascript-1c9ea8642dd0" target="_blank" rel="nofollow noopener noreferrer">Understanding Execution Context and Execution Stack in Javascript</a></p>
<h1 data-id="heading-0">执行上下文</h1>
<p>执行上下文：执行上下文是评估和执行 JavaScript 代码的环境的抽象概念。JavaScript在运行时都是在执行上下文中运行。</p>
<h2 data-id="heading-1">执行上下文的类型</h2>
<p>JavaScript 中有三种执行上下文类型。</p>
<p><strong>全局执行上下文</strong> —— 这是默认或者说基础的上下文，任何不在函数内部的代码都在全局上下文中。它会执行两件事：创建一个全局的 window 对象（浏览器的情况下），并且设置 this 的值等于这个全局对象。一个程序中只会有一个全局执行上下文。</p>
<p><strong>函数执行上下文</strong> —— 每当一个函数被调用时, 都会为该函数创建一个新的上下文。每个函数都有它自己的执行上下文，不过是在函数被调用时创建的。函数上下文可以有任意多个。每当一个新的执行上下文被创建，它会按定义的顺序（将在后文讨论）执行一系列步骤。</p>
<p><strong>Eval 函数执行上下文</strong> — 执行在 eval 函数内部的代码也会有它属于自己的执行上下文，但由于 JavaScript 开发者并不经常使用 eval，所以在这里我不会讨论它。</p>
<h2 data-id="heading-2">怎么创建执行上下文？</h2>
<p>我们已经看过 JavaScript 怎样管理执行上下文了，现在让我们了解 JavaScript 引擎是怎样创建执行上下文的。</p>
<p>1)创建阶段和2)执行阶段。</p>
<h2 data-id="heading-3">1)创建阶段</h2>
<p>执行上下文是在创建阶段创建的。以下是在创建阶段发生的事情:</p>
<p>1.创建了词法环境组件<br>
1.创建了变量环境组件</p>
<p>所以执行上下文在概念上可以表示如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ExecutionContext = &#123;
  LexicalEnvironment = <ref. to LexicalEnvironment in memory>,
  VariableEnvironment = <ref. to VariableEnvironment in  memory>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">1.1 词法环境（Lexical Environment）</h3>
<p>官方ES6文档定义词法环境为：<br>
词法环境是一种规范类型，用于根据ECMAScript代码的词法嵌套结构定义标识符与特定变量和函数的关联。<br>
一个词汇环境由一个环境记录和一个可能为空的外部词汇环境引用组成。<br>
简单地说，词法环境是一个保存标识符-变量映射的结构。(这里的标识符是变量/函数的名称，变量是对实际对象[包括函数对象和数组对象]或原始值的引用)。
例如，考虑以下代码片段:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> a = <span class="hljs-number">20</span>;
<span class="hljs-keyword">var</span> b = <span class="hljs-number">40</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'bar'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以上面代码段的词法环境是这样的:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">lexicalEnvironment = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">20</span>,
  <span class="hljs-attr">b</span>: <span class="hljs-number">40</span>,
  <span class="hljs-attr">foo</span>: <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ref.</span> <span class="hljs-attr">to</span> <span class="hljs-attr">foo</span> <span class="hljs-attr">function</span>></span>
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>每个词汇环境有三个组成部分:<br>
1.环境记录<br>
2.外部环境的引用<br>
3.this绑定</p>
<p><strong>1.1.1 环境记录</strong><br>
<strong>环境记录</strong>是变量和函数声明存储在词法环境中的地方。</p>
<p>有两种类型的环境记录：</p>
<p>1.声明式环境记录(Declarative environment record)——存储<strong>变量和函数声明</strong>。函数代码的词法环境包含一个声明性环境记录。<br>
2.对象环境记录(Object environment record)——全局代码的词法环境包含一个客观(objective)环境记录。除了变量和函数声明之外，对象环境记录还存储了一个全局绑定对象（浏览器中的window对象）。对于每个绑定对象的属性（在浏览器的情况下，它包含浏览器提供给 window 对象的属性和方法），在记录中创建一个新条目。</p>
<p>注 —对于函数代码，环境记录还包含一个arguments对象，该对象包含传递给函数的索引和参数之间的映射以及传递给函数的参数的长度（数量）。例如，以下函数的参数对象如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">var</span> c = a + b;
&#125;
foo(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>);
<span class="hljs-comment">// argument object</span>
Arguments: &#123;<span class="hljs-number">0</span>: <span class="hljs-number">2</span>, <span class="hljs-number">1</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">length</span>: <span class="hljs-number">2</span>&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1.1.2 外部环境的引用</strong>
对外部环境的引用是指它能够接触到外部词汇环境。这意味着如果在当前词法环境中找不到变量，JavaScript引擎可以在外部环境中查找变量。</p>
<p><strong>1.1.2 this绑定</strong>
在此组件中，this的值是确定的或设置的。
在全局执行上下文中，this的值引用全局对象。(在浏览器中，这指的是window对象)。</p>
<p>在函数执行上下文中，this的值取决于如何调用函数。如果它被一个对象引用调用，那么this的值被设置为该对象，否则，this的值被设置为全局对象或未定义(严格模式)。例如:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'peter'</span>,
  <span class="hljs-attr">birthYear</span>: <span class="hljs-number">1994</span>,
  <span class="hljs-attr">calcAge</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2018</span> - <span class="hljs-built_in">this</span>.birthYear);
  &#125;
&#125;
person.calcAge(); 
<span class="hljs-comment">// 'this' refers to 'person', because 'calcAge' was called with //'person' object reference</span>
<span class="hljs-keyword">const</span> calculateAge = person.calcAge;
calculateAge();
<span class="hljs-comment">// 'this' refers to the global window object, because no object reference was given</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>抽象地说，词法环境在伪代码中是这样的:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 全局执行上下文</span>
GlobalExectionContext = &#123;
  <span class="hljs-attr">LexicalEnvironment</span>: &#123;     <span class="hljs-comment">//词法环境</span>
    <span class="hljs-attr">EnvironmentRecord</span>: &#123;    <span class="hljs-comment">//环境记录</span>
      <span class="hljs-attr">Type</span>: <span class="hljs-string">"Object"</span>,
      <span class="hljs-comment">// Identifier bindings go here</span>
    &#125;
    <span class="hljs-attr">outer</span>: <<span class="hljs-literal">null</span>>,    <span class="hljs-comment">//外部环境的引用</span>
    <span class="hljs-built_in">this</span>: <global object>   //this指向
  &#125;
&#125;

// 函数执行上下文
FunctionExectionContext = &#123;
  LexicalEnvironment: &#123;     //词法环境
    EnvironmentRecord: &#123;    //环境记录
      Type: "Declarative",
      // Identifier bindings go here
    &#125;
    outer: <Global or outer function environment reference>,   //外部环境的引用
    this: <depends on how function is called>   //this指向
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.变量环境</h3>
<p>它也是一个词法环境，它的EnvironmentRecord保存着VariableStatements在这个执行上下文中创建的绑定。</p>
<p>正如上面所写的，变量环境也是一个词汇环境，所以它具有词汇环境的所有属性和组件，如上所定义的。</p>
<p>在ES6中，词法环境组件和变量环境组件的一个区别是，前者用于存储函数声明和变量(let和const)绑定，而后者仅用于存储变量(var)绑定。</p>
<h2 data-id="heading-6">2)执行阶段</h2>
<p>在这个阶段，所有这些变量的赋值都完成了，代码最终被执行。<br>
让我们看一些例子来理解上面的概念:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> a = <span class="hljs-number">20</span>;
<span class="hljs-keyword">const</span> b = <span class="hljs-number">30</span>;
<span class="hljs-keyword">var</span> c;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">multiply</span>(<span class="hljs-params">e, f</span>) </span>&#123;
 <span class="hljs-keyword">var</span> g = <span class="hljs-number">20</span>;
 <span class="hljs-keyword">return</span> e * f * g;
&#125;
c = multiply(<span class="hljs-number">20</span>, <span class="hljs-number">30</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行上述代码时，JavaScript引擎会创建一个全局执行上下文来执行全局代码。所以在创建阶段，全局执行上下文看起来是这样的:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">GlobalExectionContext = &#123;
  <span class="hljs-attr">LexicalEnvironment</span>: &#123;
    <span class="hljs-attr">EnvironmentRecord</span>: &#123;
      <span class="hljs-attr">Type</span>: <span class="hljs-string">"Object"</span>,
      <span class="hljs-comment">// Identifier bindings go here</span>
      <span class="hljs-attr">a</span>: < uninitialized >,
      b: < uninitialized >,
      multiply: < func >
    &#125;
    <span class="hljs-attr">outer</span>: <<span class="hljs-literal">null</span>>,
    ThisBinding: <Global Object>
  &#125;,
  VariableEnvironment: &#123;
    EnvironmentRecord: &#123;
      Type: "Object",
      // Identifier bindings go here
      c: undefined,
    &#125;
    outer: <null>,
    ThisBinding: <Global Object>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在执行阶段，变量分配完成。所以全局执行上下文在执行阶段看起来是这样的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">GlobalExectionContext = &#123;
<span class="hljs-attr">LexicalEnvironment</span>: &#123;
    <span class="hljs-attr">EnvironmentRecord</span>: &#123;
      <span class="hljs-attr">Type</span>: <span class="hljs-string">"Object"</span>,
      <span class="hljs-comment">// Identifier bindings go here</span>
      <span class="hljs-attr">a</span>: <span class="hljs-number">20</span>,
      <span class="hljs-attr">b</span>: <span class="hljs-number">30</span>,
      <span class="hljs-attr">multiply</span>: < func >
    &#125;
    <span class="hljs-attr">outer</span>: <<span class="hljs-literal">null</span>>,
    ThisBinding: <Global Object>
  &#125;,
VariableEnvironment: &#123;
    EnvironmentRecord: &#123;
      Type: "Object",
      // Identifier bindings go here
      c: undefined,
    &#125;
    outer: <null>,
    ThisBinding: <Global Object>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当遇到对函数multiply(20,30)的调用时，将创建一个新的函数执行上下文来执行函数代码。所以在创建阶段，函数的执行上下文看起来是这样的:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">FunctionExectionContext = &#123;
<span class="hljs-attr">LexicalEnvironment</span>: &#123;
    <span class="hljs-attr">EnvironmentRecord</span>: &#123;
      <span class="hljs-attr">Type</span>: <span class="hljs-string">"Declarative"</span>,
      <span class="hljs-comment">// Identifier bindings go here</span>
      <span class="hljs-attr">Arguments</span>: &#123;<span class="hljs-number">0</span>: <span class="hljs-number">20</span>, <span class="hljs-number">1</span>: <span class="hljs-number">30</span>, <span class="hljs-attr">length</span>: <span class="hljs-number">2</span>&#125;,
    &#125;,
    <span class="hljs-attr">outer</span>: <GlobalLexicalEnvironment>,
    ThisBinding: <Global Object or undefined>,
  &#125;,
VariableEnvironment: &#123;
    EnvironmentRecord: &#123;
      Type: "Declarative",
      // Identifier bindings go here
      g: undefined
    &#125;,
    outer: <GlobalLexicalEnvironment>,
    ThisBinding: <Global Object or undefined>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在此之后，执行上下文将经历执行阶段，这意味着对函数内部变量的赋值已经完成。所以在执行阶段，函数的执行上下文看起来是这样的:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">FunctionExectionContext = &#123;
<span class="hljs-attr">LexicalEnvironment</span>: &#123;
    <span class="hljs-attr">EnvironmentRecord</span>: &#123;
      <span class="hljs-attr">Type</span>: <span class="hljs-string">"Declarative"</span>,
      <span class="hljs-comment">// Identifier bindings go here</span>
      <span class="hljs-attr">Arguments</span>: &#123;<span class="hljs-number">0</span>: <span class="hljs-number">20</span>, <span class="hljs-number">1</span>: <span class="hljs-number">30</span>, <span class="hljs-attr">length</span>: <span class="hljs-number">2</span>&#125;,
    &#125;,
    <span class="hljs-attr">outer</span>: <GlobalLexicalEnvironment>,
    ThisBinding: <Global Object or undefined>,
  &#125;,
VariableEnvironment: &#123;
    EnvironmentRecord: &#123;
      Type: "Declarative",
      // Identifier bindings go here
      g: 20
    &#125;,
    outer: <GlobalLexicalEnvironment>,
    ThisBinding: <Global Object or undefined>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数完成后，返回值存储在c. 所以全局词法环境被更新。之后，全局代码完成，程序结束。</p>
<p>注意——您可能已经注意到，在创建阶段，let和const定义的变量没有任何关联的值，但var定义的变量被设置为undefined 。<br>
这是因为，在创建阶段，代码会扫描变量和函数声明，而函数声明则完整地存储在环境中，变量最初设置为undefined （在情况下var）或保持未初始化（在情况下let 和const）。
这就是为什么您可以var 在声明之前访问已定义的变量（尽管undefined）但在声明之前访问let和const变量时会出现引用错误。
这就是我们所说的提升。</p>
<p>注意——在执行阶段，如果 JavaScript 引擎let在源代码中声明的实际位置找不到变量的值，那么它将分配给它的值undefined。</p>
<p>结论
所以我们已经讨论了 JavaScript 程序是如何在内部执行的。虽然你不需要学习所有这些概念才能成为一个了不起的 JavaScript 开发人员，但对上述概念有一个很好的理解将帮助你更容易、更深入地理解其他概念，如提升、作用域和闭包。</p></div>  
</div>
            