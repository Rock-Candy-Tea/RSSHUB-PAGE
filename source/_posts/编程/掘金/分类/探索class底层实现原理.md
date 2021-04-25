
---
title: '探索class底层实现原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1078'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 22:23:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=1078'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>ECMAScript6</code> 实现了 <a href="https://tc39.es/ecma262/#sec-class-definitions" target="_blank" rel="nofollow noopener noreferrer"><code>class</code></a> ，实际上它是一个语法糖，但是它的出现能使 <code>JS</code> 编码更清晰，更接近 <code>面向对象编程</code>。</p>
<h2 data-id="heading-0">实现原理</h2>
<p>首先我们来看 <code>ES6</code> 中 <code>class</code> 的实现和 <code>ES5</code> 构造函数的实现，两者相比较不难看出 <code>constructor</code> 其实就是构造方法，指向 <code>ES5</code> 的构造函数，那么 <code>class</code> 本身指向的是构造函数，换言之底层依旧是构造函数。</p>
<h3 data-id="heading-1">ES6</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.age = age;
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"run"</span>);
  &#125;
  <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"hello!"</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">ES5</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-built_in">this</span>.age = age;
&#125;

Person.prototype.say = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"hello!"</span>);
&#125;;

Person.run = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"run"</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">babel 编译分析</h3>
<p>通过 <code>babel</code> 编译器将 <code>ES6</code> 代码 转换成 <code>ES5</code> 代码之后（代码转换可以试用 <a href="https://babeljs.io/repl#?browsers=defaults%2C%20not%20ie%2011%2C%20not%20ie_mob%2011&build=&builtIns=entry&corejs=3.6&spec=false&loose=false&code_lz=MYGwhgzhAEAKCmAnCB7AdtA3gKGnvw6EALogK7DEqIAUaYAtvADTRgDm8AlFrvgJDEAFgEsIAOnpNoAXmhT4Abj75og0RI7xZbTstUBfPiugkwxEcGjk0NHjlUEiKEPHEgU7GgCIb3riZGqhBgAJ52vKr8hGioru6ePkLwIB4AhP6B2EbYQA&debug=false&forceAllTransforms=true&shippedProposals=false&circleciRepo=&evaluate=true&fileSize=false&timeTravel=false&sourceType=script&lineWrap=true&presets=env&prettier=true&targets=&version=7.13.17&externalPlugins=" target="_blank" rel="nofollow noopener noreferrer">babel 官方在线工具</a>），可得到这两个关键函数 <code>_defineProperties</code> 和 <code>_createClass</code>，现在我们来一一解析说明。</p>
<pre><code class="hljs language-js copyable" lang="js">...
<span class="hljs-keyword">var</span> Person = <span class="hljs-comment">/*#__PURE__*/</span> (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-meta">  "use strict"</span>;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name, age</span>) </span>&#123;
    _classCallCheck(<span class="hljs-built_in">this</span>, Person);

    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.age = age;
  &#125;

  _createClass(
    Person,
    [
      &#123;
        <span class="hljs-attr">key</span>: <span class="hljs-string">"say"</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"hello!"</span>);
        &#125;,
      &#125;,
    ],
    [
      &#123;
        <span class="hljs-attr">key</span>: <span class="hljs-string">"run"</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span>(<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"run"</span>);
        &#125;,
      &#125;,
    ]
  );

  <span class="hljs-keyword">return</span> Person;
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">_createClass</h4>
<p><code>_createClass</code> 函数主要用于配置构造函数或构造函数原型上的公有函数和静态方法，并返回构造函数本身。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_createClass</span>(<span class="hljs-params">Constructor, protoProps, staticProps</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (protoProps) _defineProperties(Constructor.prototype, protoProps);
  <span class="hljs-keyword">if</span> (staticProps) _defineProperties(Constructor, staticProps);
  <span class="hljs-keyword">return</span> Constructor;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">_defineProperties</h4>
<p><code>_defineProperties</code> 函数主要用于声明公有函数和静态方法的描述符，并将其挂载到当前的构造函数或构造函数原型。它接收两个参数 <code>target</code>（） 和 <code>props</code>。</p>
<ul>
<li><code>target</code> 指向当前的构造函数或构造函数原型</li>
<li><code>props</code> 数组类型，指向公有函数和静态方法</li>
</ul>
<p>在遍历数组时，我们可以看到 <code>enumerable</code> 默认是 <code>false</code>，也就是说 <code>class</code> 类上的内部属性默认是不可枚举的，不能使用 <code>Object.keys</code> 遍历，具体如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.keys(Person.prototype); <span class="hljs-comment">// []</span>
<span class="hljs-built_in">Object</span>.keys(Person); <span class="hljs-comment">// []</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时在遍历的时候还会判断当前描述符是否存在 <code>value</code> 值，如果存在就设置可写属性 <code>writable</code> 为 <code>true</code>，反之就使用 <code>get</code> 和 <code>set</code> 属性。在遍历的末尾，通过 <code>Object.defineProperty</code> 将描述符配置到当前的构造函数或构造函数原型上，至此就是 <code>class</code> 的基本实现了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_defineProperties</span>(<span class="hljs-params">target, props</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < props.length; i++) &#123;
    <span class="hljs-keyword">var</span> descriptor = props[i];
    descriptor.enumerable = descriptor.enumerable || <span class="hljs-literal">false</span>;
    descriptor.configurable = <span class="hljs-literal">true</span>;
    <span class="hljs-keyword">if</span> (<span class="hljs-string">"value"</span> <span class="hljs-keyword">in</span> descriptor) descriptor.writable = <span class="hljs-literal">true</span>;
    <span class="hljs-built_in">Object</span>.defineProperty(target, descriptor.key, descriptor);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">构造函数的区别</h2>
<h3 data-id="heading-7">暂时性死区</h3>
<p><code>class</code> 不会声明提升，存在 <code>暂时性死区</code>，构造函数的本质是函数，函数声明会有提升作用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 👌</span>
&#123;
  <span class="hljs-keyword">const</span> foo = <span class="hljs-keyword">new</span> Foo();
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Foo</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
&#125;

<span class="hljs-comment">// error</span>
&#123;
  <span class="hljs-keyword">const</span> foo = <span class="hljs-keyword">new</span> Foo(); <span class="hljs-comment">// Cannot access 'Foo' before initialization</span>
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">严格模式</h3>
<p><code>class</code> 声明内部默认会启用 <code>严格模式</code>，构造函数默认 <code>非严格模式</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 👌</span>
&#123;
  <span class="hljs-keyword">const</span> foo = <span class="hljs-keyword">new</span> Foo();
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Foo</span>(<span class="hljs-params"></span>) </span>&#123;
    size = <span class="hljs-number">20</span>;
  &#125;
&#125;

<span class="hljs-comment">// error</span>
&#123;
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
      size = <span class="hljs-number">20</span>; <span class="hljs-comment">//  size is not defined</span>
    &#125;
  &#125;
  <span class="hljs-keyword">const</span> foo = <span class="hljs-keyword">new</span> Foo();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">内部方法不可枚举</h3>
<p><code>class</code> 的所有方法（包括 <code>静态方法</code>、<code>实例方法</code>）都 <code>不可枚举</code>，上文的 <code>_defineProperties</code> 函数方法实现中有提到，具体可参照上文，构造函数可枚举所有方法。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Foo</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

  Foo.print = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;;
  Foo.prototype.format = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;;

  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.keys(Foo)); <span class="hljs-comment">//  [ "print" ]</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.keys(Foo.prototype)); <span class="hljs-comment">//  [ "format" ]</span>
&#125;

&#123;
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;

    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">print</span>(<span class="hljs-params"></span>)</span> &#123;&#125;

    <span class="hljs-function"><span class="hljs-title">format</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  &#125;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.keys(Foo)); <span class="hljs-comment">//  []</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.keys(Foo.prototype)); <span class="hljs-comment">//  []</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">原型对象 prototype</h3>
<p><code>class</code> 的所有方法（包括 <code>静态方法</code>、<code>实例方法</code>）都没有原型对象 <code>prototype</code>，因此也没有 <code>[[construct]]</code>，不能通过 <code>new</code> 来调用，构造函数则支持 <code>new</code> 调用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 👌</span>
&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Foo</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
  Foo.prototype.format = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;;

  <span class="hljs-keyword">const</span> foo = <span class="hljs-keyword">new</span> Foo();
  <span class="hljs-keyword">const</span> fooFormat = <span class="hljs-keyword">new</span> foo.format();
&#125;

<span class="hljs-comment">// error</span>
&#123;
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">print</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
    <span class="hljs-function"><span class="hljs-title">format</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  &#125;

  <span class="hljs-keyword">const</span> foo = <span class="hljs-keyword">new</span> Foo();
  <span class="hljs-keyword">const</span> fooFormat = <span class="hljs-keyword">new</span> foo.format(); <span class="hljs-comment">// foo.format is not a constructor</span>
  <span class="hljs-keyword">const</span> fooPrint = <span class="hljs-keyword">new</span> foo.print(); <span class="hljs-comment">// foo.print is not a constructor</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">new 调用</h3>
<p><code>class</code> 必须使用 <code>new</code> 调用，构造函数的本质是函数，支持直接调用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 👌</span>
&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Foo</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

  <span class="hljs-keyword">const</span> foo = Foo();
&#125;

<span class="hljs-comment">// error</span>
&#123;
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;&#125;

  <span class="hljs-keyword">const</span> foo = Foo(); <span class="hljs-comment">//  Class constructor Foo cannot be invoked without 'new'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">类名重写</h3>
<p><code>class</code> 内部无法重写类名，构造函数可任意更改。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 👌</span>
&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Foo</span>(<span class="hljs-params"></span>) </span>&#123;
    Foo = <span class="hljs-string">"yo"</span>;
  &#125;
  <span class="hljs-keyword">const</span> foo = <span class="hljs-keyword">new</span> Foo();
&#125;

<span class="hljs-comment">// error</span>
&#123;
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// Foo = 'yo' // TypeError: Assignment to constant variable</span>
    &#125;
  &#125;

  <span class="hljs-keyword">const</span> foo = <span class="hljs-keyword">new</span> Foo();
  Foo = <span class="hljs-string">"yo"</span>; <span class="hljs-comment">// 👌</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            