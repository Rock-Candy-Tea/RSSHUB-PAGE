
---
title: 'JS的 3种类型判断 和 原型链 原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6673'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 16:25:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=6673'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><hr>
<h1 data-id="heading-0">typeof 原理</h1>
<h2 data-id="heading-1">typeof 概念</h2>
<p>对于JS中的<code>typeof</code>，一般会用来判断一个变量的类型，他返回的是一个类型的字符串，它可以分辨出8种数据类型：</p>
<p><strong><code>boolean</code></strong>， <strong><code>string</code></strong>， <strong><code>number</code></strong>， <strong><code>undefined</code></strong>， <strong><code>object</code></strong>， <strong><code>function</code></strong>， <strong><code>symbol</code></strong> ，<strong><code>bigint</code></strong></p>
<p><strong><code>Symbol</code></strong> 是ES6中引入的一种<code>原始数据</code>类型，表示独一无二的值。<strong><code>BigInt</code></strong>（大整数）是 ES2020 引入的一种新的数据类型，用来解决 JavaScript中数字只能到 53 个二进制位（JavaScript 所有数字都保存成 64 位浮点数，大于这个范围的整数，无法精确表示的问题。(在平常的开发中，数据的id 一般用 string 表示的原因)。为了与 <strong><code>Number</code></strong> 类型区别，<strong><code>BigInt</code></strong> 类型的数据必须添加后缀 <strong><code>n</code></strong> 。 <strong><code>1234</code></strong> 为普通整数，<strong><code>1234n</code></strong> 为 <strong><code>BigInt</code></strong> 。</p>
<h2 data-id="heading-2">typeof 底层原理</h2>
<p><strong>不同的变量在底层储存的时候，都会表示为二进制，在 JS 中这个二进制的前（低）三位储存其类型信息。（在二进制中是从右往左数的3位）</strong></p>
<p>用 <strong><code>typeof</code></strong> 判断变量类型就是判断这个变量表示的二进制的前三位。</p>
<pre><code class="hljs language-js copyable" lang="js">- <span class="hljs-number">000</span> : 对象
- <span class="hljs-number">010</span> : 浮点数
- <span class="hljs-number">100</span> : 字符串
- <span class="hljs-number">110</span> : 布尔
- <span class="hljs-number">1</span>   : 整数
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 <strong><code>undefined</code></strong> 和 <strong><code>null</code></strong> 来说，情况会有所不同：</p>
<p><strong><code>null</code></strong> 的二进制表示全为 <strong>0</strong> ， 所以前三位也就都是 <strong>0</strong> ，所以会被当做 <strong>对象</strong> 看待，<strong><code>typeof</code></strong> 判断会返回 <strong><code>"object"</code></strong></p>
<p><strong><code>undefined</code></strong> 是用 <strong>-2^30</strong>  整数来表示，所以会被单独看待，<strong><code>typeof</code></strong> 判断会返回 <strong><code>"undefined"</code></strong></p>
<p>对于 <strong><code>Array</code></strong> 这样的类型也会被看成是 <strong>对象</strong>，因为他们的前三位也是 <strong><code>000</code></strong></p>
<p><strong><code>Array: 1000100010001000</code></strong></p>
<h2 data-id="heading-3">代码实测</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;&#125;
<span class="hljs-keyword">let</span> arr = []
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-keyword">let</span> ins_func = <span class="hljs-keyword">new</span> fn();
<span class="hljs-keyword">let</span> ins_obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
<span class="hljs-keyword">let</span> ins_arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>();
<span class="hljs-keyword">const</span> symbol = <span class="hljs-built_in">Symbol</span>(<span class="hljs-number">40</span>);


<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> a)           <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-string">"b"</span>)         <span class="hljs-comment">// string</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-number">1</span>)           <span class="hljs-comment">// number</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-literal">true</span>)        <span class="hljs-comment">// boolean</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-literal">null</span>)        <span class="hljs-comment">// object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-literal">undefined</span>)   <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Object</span>)      <span class="hljs-comment">// function</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Array</span>)       <span class="hljs-comment">// function</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Function</span>)    <span class="hljs-comment">// function</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Date</span>)        <span class="hljs-comment">// function</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>)    <span class="hljs-comment">// object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span>)    <span class="hljs-comment">// function</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> obj)         <span class="hljs-comment">// object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> arr)         <span class="hljs-comment">// object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> fn)          <span class="hljs-comment">// function</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> ins_func)    <span class="hljs-comment">// object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> ins_obj)     <span class="hljs-comment">// object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> ins_arr)     <span class="hljs-comment">// object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> symbol)    <span class="hljs-comment">// symbol</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> <span class="hljs-number">123n</span>)      <span class="hljs-comment">// bigint</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">instanceof 原理</h1>
<p>要理解 <strong><code>instanceof</code></strong> 的底层原理，必须先理解 <strong>原型链</strong> 的基本概念。</p>
<h2 data-id="heading-5">原型链</h2>
<p>首先，<strong><code>构造函数</code></strong> ，<strong><code>原型对象</code></strong> ，和 <strong><code>实例</code></strong> 的关系是：</p>
<p>1. 每个 <strong><code>构造函数</code></strong> 都有一个 <strong><code>原型对象</code></strong></p>
<p>2. <strong><code>原型对象</code></strong> 中包含一个指向 <strong><code>构造函数</code></strong> 的 <strong><code>指针</code></strong></p>
<p>3. <strong><code>实例</code></strong> 中包含一个指向 <strong><code>原型对象</code></strong> 的 <strong><code>指针</code></strong></p>
<p>当一个 <strong><code>类型A</code></strong> 的 <strong><code>原型对象</code></strong> 等于另一个 <strong><code>类型B</code></strong> 的 <strong><code>实例</code></strong> 的时候，<strong><code>类型A</code></strong> 的 <strong><code>原型对象</code></strong> 中就会包含一个指向另一个 <strong><code>类型B</code></strong> 的 <strong><code>原型对象</code></strong> 的 <strong><code>指针</code></strong>， 然后我们又让另一个 <strong><code>类型B</code></strong> 的 <strong><code>原型对象</code></strong> 等于 在另一个 <strong><code>类型C</code></strong> 的 <strong><code>实例</code></strong> 的时候，<strong><code>类型B</code></strong> 的 <strong><code>实例</code></strong> 中又包含了一个指向 <strong><code>类型C</code></strong> 的 <strong><code>实例</code></strong> 的 <strong><code>指针</code></strong> ， 这样层层递进，就构成了实例和原型对象的链条，这就是<strong>原型链的基本概念</strong>。</p>
<h2 data-id="heading-6">代码实测</h2>
<h3 data-id="heading-7">构造函数，原型对象，和 实例 之间的关系</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.a = <span class="hljs-number">1</span>;
&#125;
fn.prototype.b = <span class="hljs-number">2</span>;
<span class="hljs-keyword">let</span> instance = <span class="hljs-keyword">new</span> fn();

<span class="hljs-comment">// 每个构造函数都有一个原型对象</span>
<span class="hljs-built_in">console</span>.log(fn.prototype)                                     <span class="hljs-comment">// &#123;b: 2,constructor: ƒ fn()&#125;</span>

<span class="hljs-comment">// 每个原型对象都有一个指向构造函数的指针</span>
<span class="hljs-built_in">console</span>.log(fn.prototype.constructor === fn)                  <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 每个实例都有一个指向原型对象的指针</span>
<span class="hljs-built_in">console</span>.log(instance.__proto__ === fn.prototype)              <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 根据原型链的查找机制，Object.prototype 是原型链的顶端</span>
<span class="hljs-built_in">console</span>.log(instance.__proto__.__proto__ === <span class="hljs-built_in">Object</span>.prototype)<span class="hljs-comment">// true</span>

<span class="hljs-comment">// Object.prototype 的 __proto__ 属性值为 null</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.__proto__ === <span class="hljs-literal">null</span>)              <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">原型链 的查找顺序</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义A B C 三个构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-built_in">this</span>.a = <span class="hljs-number">1</span>;&#125;
A.prototype.b = <span class="hljs-number">2</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">B</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-built_in">this</span>.c = <span class="hljs-number">3</span>;&#125;
B.prototype.d = <span class="hljs-number">4</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">C</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-built_in">this</span>.e = <span class="hljs-number">5</span>;&#125;
C.prototype.f = <span class="hljs-number">6</span>;

<span class="hljs-comment">// 构造原型链</span>
<span class="hljs-comment">// 让 B 的原型 等于 C 的 实例</span>
<span class="hljs-comment">// 让 A 的 原型 等于 B 的 实例</span>
<span class="hljs-comment">// 注意：要从后往前构造原型链</span>
B.prototype = <span class="hljs-keyword">new</span> C();
A.prototype = <span class="hljs-keyword">new</span> B();

<span class="hljs-comment">// 创建一个 A 的 实例</span>
<span class="hljs-keyword">let</span> ins_A = <span class="hljs-keyword">new</span> A();

<span class="hljs-comment">// 可以访问到 实例A 的 构造函数中的属性</span>
<span class="hljs-comment">// 但访问不到 实例A 的 原型对象中的属性</span>
<span class="hljs-comment">// 因为 A 的 原型对象 已经等于或者说变成了 B 的实例</span>
<span class="hljs-built_in">console</span>.log(ins_A.a);   <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(ins_A.b);   <span class="hljs-comment">// undefined</span>

<span class="hljs-comment">// 可以访问到 B 的构造函数中的属性</span>
<span class="hljs-comment">// 因为 A 的 原型对象 已经等于了 B 的 实例，</span>
<span class="hljs-comment">// 所以 按照原型链的查找顺序：</span>
<span class="hljs-comment">// 先在 A 的 构造函数中查找，再到 A 的 原型对象中查找，</span>
<span class="hljs-comment">// 因为 A 的 原型对象 已经等于了 B 的 实例， </span>
<span class="hljs-comment">// 所以会到 B 的 构造函数中查找</span>
<span class="hljs-comment">// 访问不到 B 的 原型对象中的属性</span>
<span class="hljs-comment">// 因为 B 的 原型对象 已经等于或者说变成了 C 的实例</span>
<span class="hljs-built_in">console</span>.log(ins_A.c);   <span class="hljs-comment">// 3</span>
<span class="hljs-built_in">console</span>.log(ins_A.d);   <span class="hljs-comment">// undefined</span>

<span class="hljs-comment">// 同理，先查找A的构造函数，再查找A的原型对象，也就是 B 的实例，</span>
<span class="hljs-comment">// 当还没有查找到，会去 B 的 原型对象中查找，也就是 C 的 实例，</span>
<span class="hljs-comment">// C 的 构造函数中没有找到，会去 C 的 原型对象中查找</span>
<span class="hljs-built_in">console</span>.log(ins_A.e);   <span class="hljs-comment">// 5 </span>
<span class="hljs-built_in">console</span>.log(ins_A.f);   <span class="hljs-comment">// 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">instanceof 底层原理</h2>
<p><strong><code>instanceof</code></strong> 一般用来判断一个<strong>对象</strong>的具体类型，也就是一个用 <strong><code>typeof</code></strong> 判断出类型为 <strong><code>"object"</code></strong> 的变量具体属于哪种数据类型。</p>
<p>通俗来讲， <strong><code>instanceof</code></strong> 用来判断一个对象是否是一个构造函数的实例。</p>
<p><strong><code>A instanceof B</code></strong></p>
<p><strong><code>instanceof</code></strong> 判断的是 右边的prototype 是否在左边的原型链上，也就是：</p>
<p><strong><code>instanceof</code></strong> 在查找过程中会<strong>遍历</strong>左边变量 <strong><code>A</code></strong> 的原型链，直到找到右边变量 <strong><code>B</code></strong> 的 <strong><code>prototype</code></strong> ，如果查找失败会返回 <strong><code>false</code></strong></p>
<p><strong>注意：</strong> 对于 <strong><code>null</code></strong> 的判断 不能使用 <strong><code>instanceof</code></strong>，会报错</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Uncaught TypeError: Right-hand side of 'instanceof' is not an object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">null</span> <span class="hljs-keyword">instanceof</span> <span class="hljs-literal">null</span>)       
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">代码实测</h2>
<h3 data-id="heading-11">实例测试</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义A B C 三个构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-built_in">this</span>.a = <span class="hljs-number">1</span>;&#125;
A.prototype.b = <span class="hljs-number">2</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">B</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-built_in">this</span>.c = <span class="hljs-number">3</span>;&#125;
B.prototype.d = <span class="hljs-number">4</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">C</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-built_in">this</span>.e = <span class="hljs-number">5</span>;&#125;
C.prototype.f = <span class="hljs-number">6</span>;

<span class="hljs-comment">// 构造原型链</span>
<span class="hljs-comment">// 让 B 的原型 等于 C 的 实例</span>
<span class="hljs-comment">// 让 A 的 原型 等于 B 的 实例</span>
<span class="hljs-comment">// 注意：要从后往前构造原型链</span>
B.prototype = <span class="hljs-keyword">new</span> C();
A.prototype = <span class="hljs-keyword">new</span> B();

<span class="hljs-comment">// 创建一个 A 的 实例</span>
<span class="hljs-keyword">let</span> ins_A = <span class="hljs-keyword">new</span> A();

<span class="hljs-built_in">console</span>.log(ins_A.a);   <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(ins_A.b);   <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(ins_A.c);   <span class="hljs-comment">// 3</span>
<span class="hljs-built_in">console</span>.log(ins_A.d);   <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(ins_A.e);   <span class="hljs-comment">// 5 </span>
<span class="hljs-built_in">console</span>.log(ins_A.f);   <span class="hljs-comment">// 6</span>


<span class="hljs-comment">// instanceof 判断的是右边的prototype是否在左边的原型链上</span>
<span class="hljs-built_in">console</span>.log(ins_A <span class="hljs-keyword">instanceof</span> A)         <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(ins_A <span class="hljs-keyword">instanceof</span> B)         <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(ins_A <span class="hljs-keyword">instanceof</span> C)         <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(ins_A <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)    <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">其他测试</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [];
<span class="hljs-keyword">let</span> obj = &#123;&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-keyword">let</span> ins_fn = <span class="hljs-keyword">new</span> fn();

<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">null</span> <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)     <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span> <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)   <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Function</span> <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span> <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)    <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)      <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(arr <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)      <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(fn <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)       <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(ins_fn <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>);  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(ins_fn <span class="hljs-keyword">instanceof</span> fn);      <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(arr <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>);      <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">实现一个 <strong><code>instanceof</code></strong></h3>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">instanceof2</span>(<span class="hljs-params">left, right</span>) </span>&#123;
    <span class="hljs-keyword">let</span> rightPrototype  = right.prototype;
    <span class="hljs-keyword">let</span> leftProto = left.__proto__;
    <span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>) &#123;
        <span class="hljs-keyword">if</span>(leftProto === <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
        &#125;
        <span class="hljs-keyword">if</span>(leftProto === rightPrototype) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
        &#125;
        leftProto = leftProto.__proto__;
    &#125;
&#125;


<span class="hljs-comment">/*测试*/</span>

<span class="hljs-comment">// 定义A B C 三个构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-built_in">this</span>.a = <span class="hljs-number">1</span>;&#125;
A.prototype.b = <span class="hljs-number">2</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">B</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-built_in">this</span>.c = <span class="hljs-number">3</span>;&#125;
B.prototype.d = <span class="hljs-number">4</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">C</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-built_in">this</span>.e = <span class="hljs-number">5</span>;&#125;
C.prototype.f = <span class="hljs-number">6</span>;

B.prototype = <span class="hljs-keyword">new</span> C();
A.prototype = <span class="hljs-keyword">new</span> B();

<span class="hljs-comment">// 创建一个 A 的 实例</span>
<span class="hljs-keyword">let</span> ins_A = <span class="hljs-keyword">new</span> A();
<span class="hljs-comment">// instanceof 判断的是右边的prototype是否在左边的原型链上</span>
<span class="hljs-built_in">console</span>.log(ins_A <span class="hljs-keyword">instanceof</span> A)         <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(ins_A <span class="hljs-keyword">instanceof</span> B)         <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(ins_A <span class="hljs-keyword">instanceof</span> C)         <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(ins_A <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>)    <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(ins_A <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>)     <span class="hljs-comment">// false</span>


<span class="hljs-comment">// 自己实现的instanceof2</span>
<span class="hljs-built_in">console</span>.log(instanceof2(ins_A, A))      <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(instanceof2(ins_A, B))      <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(instanceof2(ins_A, C))      <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(instanceof2(ins_A, <span class="hljs-built_in">Object</span>)) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(instanceof2(ins_A, <span class="hljs-built_in">Array</span>))  <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">Object.prototype.toString.call() 原理</h1>
<p><strong><code>Object.prototype.toString.call()</code></strong> 用于判断某个对象值属于哪种内置类型</p>
<h2 data-id="heading-15">Object.prototype.toString() 调用</h2>
<p>每个对象都有一个 <strong><code>toString()</code></strong> 方法，他返回一个 <strong><code>[object type]</code></strong> 形式的字符串， <strong><code>type</code></strong> 代表这个对象的类型。</p>
<p>但是很多自定义对象可能会覆盖掉这个 <strong><code>toString()</code></strong> 方法，比如</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> A = &#123;&#125;;
<span class="hljs-keyword">let</span>  B = &#123;
    <span class="hljs-attr">toString</span>: <span class="hljs-function">() =></span> &#123;<span class="hljs-keyword">return</span> <span class="hljs-string">"hello"</span>;&#125;
&#125;
<span class="hljs-built_in">console</span>.log(A.toString());  <span class="hljs-comment">// "[object Object]"</span>
<span class="hljs-built_in">console</span>.log(B.toString());  <span class="hljs-comment">// "hello"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以为了检测出一个对象的类型，就要使用原本的 <strong><code>Object.prototype</code></strong> 上的 <strong><code>Object.prototype.toString()</code></strong> 方法，为了让每个对象都能调用这个方法，就要使用</p>
<p><strong><code>Object.prototype.toString.call()</code></strong></p>
<h2 data-id="heading-16">Object.prototype.toString() 原理</h2>
<p>对于 <strong><code>Object.prototype.toString.call()</code></strong> ：</p>
<p>1. 如果参数为 <strong><code>null</code></strong> 或者 <strong><code>undefined</code></strong> ，直接返回结果。</p>
<p>2. 如果参数不为 <strong><code>null</code></strong> 或者 <strong><code>undefined</code></strong> ，现将参数转换为对象再做判断。</p>
<p>3. 如果该参数转换成的对象有 <strong><code>[Symbol.toStringTag]</code></strong> 属性值，那么将该属性值作为 <strong><code>tag</code></strong> ；如果没有，就使用这些类型的对象拥有的自己的特定的内部属性作为 <strong><code>tag</code></strong>（比如 <strong><code>Boolean</code></strong> 对象就有 <strong><code>[[BooleanData]]</code></strong> 插槽，值为原始的 <strong><code>Boolean</code></strong> 值；<strong><code>Number</code></strong> 对象有  <strong><code>[[NumberData]]</code></strong> 插槽，值为原始的 <strong><code>Number</code></strong> 值）。最后返回 <strong><code>"[object " + tag + "]"</code></strong> 形式的字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// [Symbol.toStringTag] 属性值需要是一个字符串，否则会被忽略。</span>
<span class="hljs-keyword">let</span> o1 = &#123; [<span class="hljs-built_in">Symbol</span>.toStringTag]: <span class="hljs-string">"A"</span> &#125;;
<span class="hljs-keyword">let</span> o2 = &#123; [<span class="hljs-built_in">Symbol</span>.toStringTag]: <span class="hljs-literal">null</span> &#125;;

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(o1));    <span class="hljs-comment">// [object A]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(o2));    <span class="hljs-comment">// [object Object]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">代码实测</h2>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">true</span>))       <span class="hljs-comment">// [object Boolean]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-string">"a"</span>))        <span class="hljs-comment">// [object String]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-number">1</span>))          <span class="hljs-comment">// [object Number]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(&#123;<span class="hljs-attr">b</span>:<span class="hljs-number">2</span>&#125;))      <span class="hljs-comment">// [object Object]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>]))      <span class="hljs-comment">// [object Array]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-function">() =></span> &#123;&#125;))   <span class="hljs-comment">// [object Function]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-built_in">Symbol</span>(<span class="hljs-number">1</span>)))  <span class="hljs-comment">// [object Symbol]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-number">123n</span>))       <span class="hljs-comment">// [object Bigint]</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()))  <span class="hljs-comment">// [object Set]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()))  <span class="hljs-comment">// [object Map]</span>

<span class="hljs-keyword">let</span>  A = &#123;
    <span class="hljs-attr">toString</span>: <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"hello"</span>;
    &#125;
&#125;
<span class="hljs-built_in">console</span>.log(A.toString())                               <span class="hljs-comment">// hello</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(A))          <span class="hljs-comment">// [object Object]</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            