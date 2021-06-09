
---
title: '假如易立竞问你如何判断 JavaScript 中的数据类型？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2813cd17e4f34736905226f44b4cf074~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 07:30:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2813cd17e4f34736905226f44b4cf074~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p><strong>美味值：🌟🌟🌟🌟🌟</strong></p>
<p><strong>口味：芥末虾仁球</strong></p>
<p>为了和易老师对线，我们先来简单复习下。</p>
<p>JavaScript 的数据类型包括原始类型和对象类型：</p>
<ul>
<li>原始类型：Null、Undefined、Number、String、Boolean、Symbol、BigInt</li>
<li>对象类型：Object</li>
</ul>
<p>我们习惯把对象称为引用类型，当然还有很多特殊的引用类型，比如 Function、Array、RegExp、Math、Date、Error、Set、Map、各种定型数组 TypedArray 等。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2813cd17e4f34736905226f44b4cf074~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>原始类型值保存在栈中，对象类型值保存在堆中，在栈中保留了对象的引用地址，当 JavaScript 访问数据的时候，通过栈中的引用访问。</p>
<p>在 JavaScript 中，原始类型的赋值会完整复制变量值，而对象(引用)类型的赋值是复制引用地址。</p>
<h2 data-id="heading-0">再来两道常考面试题练练手</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'前端食堂'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">2</span>
&#125;
<span class="hljs-keyword">let</span> b = a
<span class="hljs-built_in">console</span>.log(a.name)
b.name = <span class="hljs-string">'童欧巴'</span>
<span class="hljs-built_in">console</span>.log(a.name)
<span class="hljs-built_in">console</span>.log(b.name)

<span class="hljs-comment">// 前端食堂</span>
<span class="hljs-comment">// 童欧巴</span>
<span class="hljs-comment">// 童欧巴</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一题 So Easy，闭着眼睛也能答对。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'前端食堂'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">2</span>
&#125;
<span class="hljs-keyword">const</span> expand = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">b</span>) </span>&#123;
    b.age = <span class="hljs-number">18</span>
    b = &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'童欧巴'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">25</span>
    &#125;
    <span class="hljs-keyword">return</span> b
&#125;
<span class="hljs-keyword">let</span> c = expand(a)
<span class="hljs-built_in">console</span>.log(c.age)
<span class="hljs-built_in">console</span>.log(a.age)
<span class="hljs-built_in">console</span>.log(a)

<span class="hljs-comment">// 25</span>
<span class="hljs-comment">// 18</span>
<span class="hljs-comment">// &#123;name: "前端食堂", age: 18&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这道题可能有些同学会答错，我们来一起分析一下：</p>
<p>expand 函数传进来的参数 b，其实传递的是对象在堆中的内存地址值，通过调用 b.age = 18 可以改变 a 对象的 age 属性。</p>
<p>但是 return 又把 b 变成了另一个内存地址，将 <code>&#123;name: "童欧巴", age: 25&#125;</code> 存入，导致最后返回 a 的值就变成了 <code>&#123;name: "童欧巴", age: 25&#125;</code></p>
<h2 data-id="heading-1">接下来让我们以热烈的掌声，欢迎易老师闪亮登场！</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24d4defd3fad433a898d426fae32dc2b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我会问你一些问题，你随时可以喝水。</p>
</blockquote>
<blockquote>
<p>JavaScript 中检测数据类型的方法有哪些你知道吗？</p>
</blockquote>
<ul>
<li>typeof</li>
<li>instanceof</li>
<li>constructor</li>
<li>Object.prototype.toString.call()</li>
</ul>
<blockquote>
<p>那 typeof 用起来怎么样呢？</p>
</blockquote>
<h2 data-id="heading-2">1.typeof</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">typeof</span> <span class="hljs-string">'a'</span> <span class="hljs-comment">// 'string'</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-number">1</span>   <span class="hljs-comment">// 'number' </span>
<span class="hljs-keyword">typeof</span> <span class="hljs-literal">true</span> <span class="hljs-comment">// 'boolean'</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 'undefined'</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'a'</span>) <span class="hljs-comment">// 'symbol'</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-number">1n</span> <span class="hljs-comment">// 'bigint'</span>

<span class="hljs-keyword">typeof</span> <span class="hljs-literal">null</span> <span class="hljs-comment">// 'object'</span>

<span class="hljs-keyword">typeof</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125; <span class="hljs-comment">// 'function'</span>
<span class="hljs-keyword">typeof</span> [] <span class="hljs-comment">// 'object'</span>
<span class="hljs-keyword">typeof</span> &#123;&#125; <span class="hljs-comment">// 'object'</span>
<span class="hljs-keyword">typeof</span> /a/ <span class="hljs-comment">// 'object'</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() <span class="hljs-comment">// 'object'</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>() <span class="hljs-comment">// 'object'</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>() <span class="hljs-comment">// 'object'</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>() <span class="hljs-comment">// 'object'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>两条结论：</strong></p>
<ol>
<li>typeof 可以判断除了 null 以外的原始类型。</li>
<li>typeof 只能判断对象类型中的 Function，其他判断不出来，都为 object。</li>
</ol>
<blockquote>
<p>为什么 typeof null 的值是 object？</p>
</blockquote>
<p>typeof 检测 null 时返回 object，是最初 JavaScript 语言的一个 Bug，为了兼容老代码一直保留至今。</p>
<p>如果想了解更多，请戳下面链接。</p>
<ul>
<li><a href="https://www.zhihu.com/question/21691758" target="_blank" rel="nofollow noopener noreferrer">链接</a></li>
</ul>
<h3 data-id="heading-3">Tips</h3>
<p>这里不得不提一下 NaN，毕竟我们都知道它戏比较多。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">typeof</span> <span class="hljs-literal">NaN</span> <span class="hljs-comment">// number</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>F**k NaN!</p>
<blockquote>
<p>instanceof 能判断出哪些类型你知道吗？</p>
</blockquote>
<h2 data-id="heading-4">2.instanceof</h2>
<p>检测构造函数的 prototype 属性是否出现在某个实例对象的原型链上。</p>
<p>也就是使用 <code>a instanceof B</code> 判断的是：a 是否为 B 的实例，即 a 的原型链上是否存在 B 的构造函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Number</span>) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">1</span>) <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Number</span>) <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> arr = []
<span class="hljs-built_in">console</span>.log(arr <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(arr <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> Fn = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'构造函数'</span>
&#125;
Fn.prototype = <span class="hljs-built_in">Object</span>.create(<span class="hljs-built_in">Array</span>.prototype)
<span class="hljs-keyword">let</span> a = <span class="hljs-keyword">new</span> Fn()
<span class="hljs-built_in">console</span>.log(a <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>两条结论：</strong></p>
<ol>
<li><code>instanceof</code> 可以准确判断对象(引用)类型，但是不能准确检测原始类型。</li>
<li>由于我们可以随意修改原型的指向导致检测结果不准确，所以这种方法是不安全的。</li>
</ol>
<blockquote>
<p>如果我就想用 instanceof 检测原始类型，你能满足我的需求吗？</p>
</blockquote>
<p>好，满足。</p>
<p>虽然 <code>instanceof</code> 不能检测原始类型，但是有一种方法可以让其用于检测原始类型。</p>
<p><code>Symbol.hasInstance</code> 允许我们自定义 <code>instanceof</code> 的行为。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PrimitiveNumber</span> </span>&#123;
  <span class="hljs-keyword">static</span> [<span class="hljs-built_in">Symbol</span>.hasInstance] = <span class="hljs-function"><span class="hljs-params">x</span>  =></span> <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'number'</span>;
&#125;
<span class="hljs-number">123</span> <span class="hljs-keyword">instanceof</span> PrimitiveNumber; <span class="hljs-comment">// true</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PrimitiveString</span> </span>&#123;
  <span class="hljs-keyword">static</span> [<span class="hljs-built_in">Symbol</span>.hasInstance] = <span class="hljs-function"><span class="hljs-params">x</span> =></span> <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'string'</span>;
&#125;
<span class="hljs-string">'abc'</span> <span class="hljs-keyword">instanceof</span> PrimitiveString; <span class="hljs-comment">// true</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PrimitiveBoolean</span> </span>&#123;
  <span class="hljs-keyword">static</span> [<span class="hljs-built_in">Symbol</span>.hasInstance] = <span class="hljs-function"><span class="hljs-params">x</span> =></span> <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'boolean'</span>;
&#125;
<span class="hljs-literal">false</span> <span class="hljs-keyword">instanceof</span> PrimitiveBoolean; <span class="hljs-comment">// true</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PrimitiveSymbol</span> </span>&#123;
  <span class="hljs-keyword">static</span> [<span class="hljs-built_in">Symbol</span>.hasInstance] = <span class="hljs-function"><span class="hljs-params">x</span> =></span> <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'symbol'</span>;
&#125;
<span class="hljs-built_in">Symbol</span>.iterator <span class="hljs-keyword">instanceof</span> PrimitiveSymbol; <span class="hljs-comment">// true</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PrimitiveNull</span> </span>&#123;
  <span class="hljs-keyword">static</span> [<span class="hljs-built_in">Symbol</span>.hasInstance] = <span class="hljs-function"><span class="hljs-params">x</span> =></span> x === <span class="hljs-literal">null</span>;
&#125;
<span class="hljs-literal">null</span> <span class="hljs-keyword">instanceof</span> PrimitiveNull; <span class="hljs-comment">// true</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PrimitiveUndefined</span> </span>&#123;
  <span class="hljs-keyword">static</span> [<span class="hljs-built_in">Symbol</span>.hasInstance] = <span class="hljs-function"><span class="hljs-params">x</span> =></span> x === <span class="hljs-literal">undefined</span>;
&#125;
<span class="hljs-literal">undefined</span> <span class="hljs-keyword">instanceof</span> PrimitiveUndefined; <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码来源下面链接。</p>
<ul>
<li><a href="https://www.30secondsofcode.org/blog/s/javascript-primitive-instanceof" target="_blank" rel="nofollow noopener noreferrer">有没有一种方法可以将instanceof用于原始JavaScript值？</a></li>
</ul>
<blockquote>
<p>既然你对 instanceof 这么了解了，能给我现场手写一个吗？</p>
</blockquote>
<h3 data-id="heading-5">手写 instanceof</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> myInstanceof = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">left, right</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> left !== <span class="hljs-string">'object'</span> || left === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    <span class="hljs-keyword">let</span> proto = <span class="hljs-built_in">Reflect</span>.getPrototypeOf(left)
    <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
        <span class="hljs-keyword">if</span> (proto === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        <span class="hljs-keyword">if</span> (proto === right.prototype) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        proto = <span class="hljs-built_in">Reflect</span>.getPrototypeOf(proto)
    &#125;
&#125;

<span class="hljs-keyword">const</span> arr = []
<span class="hljs-built_in">console</span>.log(myInstanceof(arr, <span class="hljs-built_in">Array</span>)) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(myInstanceof(arr, <span class="hljs-built_in">Object</span>)) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(myInstanceof(arr, <span class="hljs-built_in">RegExp</span>)) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要理解 instanceof 的工作原理，就必须理解原型链，对 JavaScript 原型链掌握的不够深刻的同学可以戳下面链接学习。</p>
<ul>
<li><a href="https://github.com/mqyqingfeng/Blog/issues/2" target="_blank" rel="nofollow noopener noreferrer">JavaScript深入之从原型到原型链</a></li>
<li><a href="https://yanhaijing.com/javascript/2021/03/13/javascript-prototype-chain/" target="_blank" rel="nofollow noopener noreferrer">如何回答面试中的JavaScript原型链问题</a></li>
</ul>
<blockquote>
<p>constructor 怎么样，好用吗？</p>
</blockquote>
<h2 data-id="heading-6">3.constructor</h2>
<p>对于数值直接量，直接使用 constructor 是会报错的，这个错误来自于浮点数的字面量解析过程，而不是 "." 作为存取运算符的处理过程。</p>
<p>在 JS 中，浮点数的小数位是可以为空的，因此 1. 和 1.0 会解析成相同的浮点数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 所以需要加上一个小括号，小括号运算符能够把数值转换为对象</span>
(<span class="hljs-number">1</span>).constructor <span class="hljs-comment">// ƒ Number() &#123; [native code] &#125;</span>
<span class="hljs-comment">// 或者</span>
<span class="hljs-number">1.</span>.constructor <span class="hljs-comment">// ƒ Number() &#123; [native code] &#125;</span>

<span class="hljs-keyword">const</span> a = <span class="hljs-string">'前端食堂'</span>
<span class="hljs-built_in">console</span>.log(a.constructor) <span class="hljs-comment">// ƒ String() &#123; [native code] &#125;</span>
<span class="hljs-built_in">console</span>.log(a.constructor === <span class="hljs-built_in">String</span>) <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> b = <span class="hljs-number">5</span>
<span class="hljs-built_in">console</span>.log(b.constructor) <span class="hljs-comment">// ƒ Number() &#123; [native code] &#125;</span>
<span class="hljs-built_in">console</span>.log(b.constructor === <span class="hljs-built_in">Number</span>) <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> c = <span class="hljs-literal">true</span>
<span class="hljs-built_in">console</span>.log(c.constructor) <span class="hljs-comment">// ƒ Boolean() &#123; [native code] &#125;</span>
<span class="hljs-built_in">console</span>.log(c.constructor === <span class="hljs-built_in">Boolean</span>) <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> d = []
<span class="hljs-built_in">console</span>.log(d.constructor) <span class="hljs-comment">// ƒ Array() &#123; [native code] &#125;</span>
<span class="hljs-built_in">console</span>.log(d.constructor === <span class="hljs-built_in">Array</span>) <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> e = &#123;&#125;
<span class="hljs-built_in">console</span>.log(e.constructor) <span class="hljs-comment">// ƒ Object() &#123; [native code] &#125;</span>
<span class="hljs-built_in">console</span>.log(e.constructor === <span class="hljs-built_in">Object</span>) <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> f = <span class="hljs-function">() =></span> <span class="hljs-number">1</span>
<span class="hljs-built_in">console</span>.log(f.constructor) <span class="hljs-comment">// ƒ Function() &#123; [native code] &#125;</span>
<span class="hljs-built_in">console</span>.log(f.constructor === <span class="hljs-built_in">Function</span>) <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> g = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'1'</span>)
<span class="hljs-built_in">console</span>.log(g.constructor) <span class="hljs-comment">// ƒ Symbol() &#123; [native code] &#125;</span>
<span class="hljs-built_in">console</span>.log(g.constructor === <span class="hljs-built_in">Symbol</span>) <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> h = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
<span class="hljs-built_in">console</span>.log(h.constructor) <span class="hljs-comment">// ƒ Date() &#123; [native code] &#125;</span>
<span class="hljs-built_in">console</span>.log(h.constructor === <span class="hljs-built_in">Date</span>) <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> i = <span class="hljs-number">11n</span>
<span class="hljs-built_in">console</span>.log(i.constructor) <span class="hljs-comment">// ƒ BigInt() &#123; [native code] &#125;</span>
<span class="hljs-built_in">console</span>.log(i.constructor === <span class="hljs-built_in">BigInt</span>) <span class="hljs-comment">// true</span>

<span class="hljs-keyword">const</span> j = <span class="hljs-regexp">/a/</span>
<span class="hljs-built_in">console</span>.log(j.constructor) <span class="hljs-comment">// ƒ RegExp() &#123; [native code] &#125;</span>
<span class="hljs-built_in">console</span>.log(j.constructor === <span class="hljs-built_in">RegExp</span>) <span class="hljs-comment">// true</span>


<span class="hljs-built_in">String</span>.prototype.constructor = <span class="hljs-string">'aaa'</span>
<span class="hljs-built_in">console</span>.log(a.constructor === <span class="hljs-built_in">String</span>) <span class="hljs-comment">// false</span>

<span class="hljs-keyword">const</span> k = <span class="hljs-literal">null</span>
<span class="hljs-built_in">console</span>.log(k.constructor) <span class="hljs-comment">// Cannot read property 'constructor' of null</span>

<span class="hljs-keyword">const</span> l = <span class="hljs-literal">undefined</span>
<span class="hljs-built_in">console</span>.log(l.constructor) <span class="hljs-comment">// Cannot read property 'constructor' of undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两条结论：</p>
<ol>
<li>除了 null 和 undefined，<code>constructor</code> 可以正确检测出原始类型和对象(引用)类型。</li>
<li>由于我们可以随意修改 <code>constructor</code> 导致检测结果不准确，所以这种方法是不安全的。</li>
</ol>
<blockquote>
<p>还剩下 Object.prototype.toString 了，它就无懈可击了吗？</p>
</blockquote>
<h2 data-id="heading-7">4.Object.prototype.toString</h2>
<p>toString() 方法返回一个表示该对象的字符串，我们可以改变它的 this 指向，将 this 指向要检测的值，即可返回当前检测值的信息。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.prototype.toString(&#123;&#125;) <span class="hljs-comment">// '[object Object]'</span>

<span class="hljs-built_in">Object</span>.prototype.toString.call(&#123;&#125;) <span class="hljs-comment">// '[object Object]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-string">'a'</span>) <span class="hljs-comment">// '[object String]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-number">1</span>) <span class="hljs-comment">// '[object Number]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">true</span>) <span class="hljs-comment">// '[object Boolean]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">null</span>) <span class="hljs-comment">// '[object Null]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">undefined</span>) <span class="hljs-comment">// '[object Undefined]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'a'</span>)) <span class="hljs-comment">// '[object Symbol]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-number">11n</span>) <span class="hljs-comment">// '[object BigInt]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-regexp">/a/</span>) <span class="hljs-comment">// '[object RegExp]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()) <span class="hljs-comment">// '[object Date]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call([<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>]) <span class="hljs-comment">// '[object Array]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;) <span class="hljs-comment">// '[object Function]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>()) <span class="hljs-comment">// '[object Error]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()) <span class="hljs-comment">// '[object Set]'</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()) <span class="hljs-comment">// '[object Map]'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>你能封装一个检测数据类型的通用方法吗？</p>
</blockquote>
<h2 data-id="heading-8">封装检测数据类型的通用方法</h2>
<p>封装方法的时候注意大小写。</p>
<p>方案有很多种，这里简单提供两个思路。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> getType = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">obj</span>) </span>&#123;
    <span class="hljs-keyword">let</span> type = <span class="hljs-keyword">typeof</span> obj
    <span class="hljs-keyword">if</span> (type !== <span class="hljs-string">'object'</span>) &#123;
        <span class="hljs-keyword">return</span> type
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.toString.call(obj).replace(<span class="hljs-regexp">/^\[object (\S+)\]$/</span>, <span class="hljs-string">'$1'</span>).toLowerCase()
&#125;

getType(&#123;&#125;) <span class="hljs-comment">// object</span>
getType(<span class="hljs-string">'a'</span>) <span class="hljs-comment">// string</span>
getType(<span class="hljs-number">1</span>) <span class="hljs-comment">// number</span>
getType(<span class="hljs-literal">true</span>) <span class="hljs-comment">// boolean</span>
getType(<span class="hljs-literal">null</span>) <span class="hljs-comment">// null</span>
getType(<span class="hljs-literal">undefined</span>) <span class="hljs-comment">// undefined</span>
getType(<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'a'</span>)) <span class="hljs-comment">// symbol</span>
getType(<span class="hljs-number">11n</span>) <span class="hljs-comment">// bigint</span>
getType(<span class="hljs-regexp">/a/</span>) <span class="hljs-comment">// regexp</span>
getType(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()) <span class="hljs-comment">// date</span>
getType([<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>]) <span class="hljs-comment">// array</span>
getType(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125;) <span class="hljs-comment">// function</span>
getType(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>()) <span class="hljs-comment">// error</span>
getType(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()) <span class="hljs-comment">// map</span>
getType(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()) <span class="hljs-comment">// set</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，换个姿势，这样也可以实现。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-string">'1'</span>).slice(<span class="hljs-number">8</span>, -<span class="hljs-number">1</span>).toLowerCase()
<span class="hljs-comment">// 'string'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>聊到这，基本上就是满分答案了。</p>
<p>如果你觉得哪里有遗漏，欢迎在评论区补充。</p>
<p>最后一个易老师的问题留给大家：</p>
<blockquote>
<p>你，喜欢 JavaScript 吗？</p>
</blockquote>
<h2 data-id="heading-9">❤️爱心三连击</h2>
<p>1.如果你觉得食堂酒菜还合胃口，就点个赞支持下吧，你的<strong>赞</strong>是我最大的动力。</p>
<p>2.关注公众号<code>前端食堂，吃好每一顿饭！</code></p>
<p>3.点赞、评论、转发 === 催更！</p></div>  
</div>
            