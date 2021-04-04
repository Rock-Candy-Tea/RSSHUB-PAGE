
---
title: '温故而知新 - 重新认识JavaScript的Hoisting'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9387'
author: 掘金
comments: false
date: Sat, 03 Apr 2021 00:59:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=9387'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>为JavaScript里面的概念，温故而知新。</p>
<h3 data-id="heading-0">概念：Hositing是什么</h3>
<p>在JavaScript中，如果试图使用尚未声明的变量，会出现<code>ReferenceError</code>错误。毕竟变量都没有声明，JavaScript也就找不到这变量。加上变量的声明，可正常运行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(a);
<span class="hljs-comment">// Uncaught ReferenceError: a is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a;
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>考虑下如果是这样书写：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// undefined</span>
<span class="hljs-keyword">var</span> a;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直觉上，程序是自上向下逐行执行的。使用尚未声明的变量<strong>a</strong>，按理应该出现<code>ReferenceError</code>错误，而实际上却输出了<code>undefined</code>。这种现象，就是<a href="https://developer.mozilla.org/en-US/docs/Glossary/Hoisting" target="_blank" rel="nofollow noopener noreferrer"><strong>Hoisting</strong></a>。<code>var a</code>由于某种原因被"<em>移动</em>"到最上面了。可以理解为如下形式：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a;
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要<strong>注意</strong>：</p>
<ol>
<li>
<p>实际上声明在代码里的位置是不会变的。</p>
</li>
<li>
<p>hoisting只是针对声明，赋值并不会。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// undefined</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">2015</span>;

<span class="hljs-comment">// 理解为如下形式</span>
<span class="hljs-keyword">var</span> a;
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// undefined</span>
a = <span class="hljs-number">2015</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里<code>var a = 2015</code>理解上可分成两个步骤：<code>var a</code>和<code>a = 2015</code>。</p>
</li>
<li>
<p>函数表达式不会<code>hoisting</code>。</p>
<pre><code class="hljs language-js copyable" lang="js">fn(); <span class="hljs-comment">// TypeError: fn is not a function</span>
<span class="hljs-keyword">var</span> fn = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;

<span class="hljs-comment">// 理解为如下形式</span>
<span class="hljs-keyword">var</span> fn;
fn();
fn = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里<code>fn()</code>对<code>undefined</code>值进行函数调用导致非法操作，因此抛出<code>TypeError</code>错误。</p>
</li>
<li>
<p>函数声明和变量声明，都会<code>hoisting</code>，需要注意的是，函数会优先<code>hoisting</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(fn);
<span class="hljs-keyword">var</span> fn;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

<span class="hljs-comment">// 理解为如下形式</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-keyword">var</span> fn; <span class="hljs-comment">// 重复声明，会被忽略</span>
<span class="hljs-built_in">console</span>.log(fn);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>对于有参数的函数：</p>
<pre><code class="hljs language-js copyable" lang="js">fn(<span class="hljs-number">2016</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">a</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 2016</span>
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">2015</span>;
&#125;

<span class="hljs-comment">// 理解为如下形式</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">a</span>) </span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">2016</span>; <span class="hljs-comment">// 这里对应传参，值为函数调用时候传进来的值</span>
    <span class="hljs-keyword">var</span> a; <span class="hljs-comment">// 重复声明，会被忽略</span>
    <span class="hljs-built_in">console</span>.log(a);
    a = <span class="hljs-number">2015</span>;
&#125;
fn(<span class="hljs-number">2016</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结一下，可以理解<code>Hoisting</code>是处理所有声明的过程。需要注意<strong>赋值及函数表达式不会hoisting</strong>。</p>
<h3 data-id="heading-1">意义：为什么需要Hoisting</h3>
<p>可以处理函数互相调用的场景：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params">n</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (n > <span class="hljs-number">0</span>) fn2(n);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn2</span>(<span class="hljs-params">n</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(n);
    fn1(n - <span class="hljs-number">1</span>);
&#125;

fn1(<span class="hljs-number">6</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按逐行执行的观念来看，必然存在先后顺序，像<code>fn1</code>与<code>fn2</code>之间的相互调用，如果没有<code>hoisting</code>的话，是无法正常运行的。</p>
<h3 data-id="heading-2">规范：Hoisting的运行规则</h3>
<p>具体可以参考规范<a href="https://262.ecma-international.org/10.0/" target="_blank" rel="nofollow noopener noreferrer">ECMAScript 2019 Language Specification</a>。与Hoisting相关的，是在<a href="https://262.ecma-international.org/10.0/#sec-execution-contexts" target="_blank" rel="nofollow noopener noreferrer"><code>8.3 Execution Contexts</code></a>。</p>
<p>一篇很不错的文章参考<a href="https://blog.bitsrc.io/understanding-execution-context-and-execution-stack-in-javascript-1c9ea8642dd0" target="_blank" rel="nofollow noopener noreferrer"><code>Understanding Execution Context and Execution Stack in Javascript</code></a></p>
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
<pre><code class="hljs language-js copyable" lang="js">GlobalExectionContext = &#123;
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
<p>在运行阶段，变量赋值已经完成。因此<code>GlobalExectionContext</code>在执行阶段看起来就像是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js">GlobalExectionContext = &#123;
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
<p>当遇到函数<code>foo(a, b)</code>的调用时，新的<code>FunctionExectionContext</code>被创建并执行函数中的代码。在创建阶段像这样：</p>
<pre><code class="hljs language-js copyable" lang="js">FunctionExectionContext = &#123;
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
<pre><code class="hljs language-js copyable" lang="js">FunctionExectionContext = &#123;
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
<p>在函数执行完成以后，返回值会被存储在<code>c</code>里。因此<code>GlobalExectionContext</code>更新。在这之后，代码执行完成，程序运行终止。</p>
<h3 data-id="heading-3">细节：var、let、const在hoisting上的差异</h3>
<p>回顾<code>规范：Hoisting的运行规则</code>，可以注意到在创建阶段，不管是用<code>let</code>、<code>const</code>或<code>var</code>，都会进行<code>hoisting</code>。而差别在于：使用<code>let</code>和<code>const</code>进行声明的时候，设置为<code>uninitialized</code>(未初始化状态)，而<code>var</code>会设置为<code>undefined</code>。所以在<code>let</code>或<code>const</code>声明的变量之前访问时，会抛出<code>ReferenceError: Cannot access 'c' before initialization</code>错误。对应的名词为<code>Temporal Dead Zone</code>(暂时性死区)。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">demo1</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(c); <span class="hljs-comment">// c 的 TDZ 开始</span>
    <span class="hljs-keyword">let</span> c = <span class="hljs-number">10</span>; <span class="hljs-comment">// c 的 TDZ 结束</span>
&#125;
demo1();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">demo2</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'begin'</span>); <span class="hljs-comment">// c 的 TDZ 开始</span>
    <span class="hljs-keyword">let</span> c; <span class="hljs-comment">// c 的 TDZ 结束</span>
    <span class="hljs-built_in">console</span>.log(c);
    c = <span class="hljs-number">10</span>;
    <span class="hljs-built_in">console</span>.log(c);
&#125;
demo2();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">总结</h3>
<p>果真是温故而知新，发现自己懂得其实好少。鞭策自己，后续对<code>this</code>、<code>prototype</code>、<code>closures</code>及<code>scope</code>等，进行温故。</p>
<h4 data-id="heading-5">参考资料</h4>
<ol>
<li><a href="https://blog.huli.tw/2018/11/10/javascript-hoisting-and-tdz/" target="_blank" rel="nofollow noopener noreferrer">我知道你懂 hoisting，可是你了解到多深？</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Hoisting" target="_blank" rel="nofollow noopener noreferrer">MDN: Hoisting</a></li>
<li><a href="https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch1.md" target="_blank" rel="nofollow noopener noreferrer">You-Dont-Know-JS 2nd-ed</a></li>
<li><a href="https://262.ecma-international.org/10.0/" target="_blank" rel="nofollow noopener noreferrer">ECMAScript 2019 Language Specification</a></li>
<li><a href="https://blog.bitsrc.io/understanding-execution-context-and-execution-stack-in-javascript-1c9ea8642dd0" target="_blank" rel="nofollow noopener noreferrer">Understanding Execution Context and Execution Stack in Javascript</a></li>
<li>JavaScript高级程序设计</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            