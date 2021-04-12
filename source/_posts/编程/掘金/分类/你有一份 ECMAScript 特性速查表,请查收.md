
---
title: '你有一份 ECMAScript 特性速查表,请查收'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6746'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 22:37:53 GMT
thumbnail: 'https://picsum.photos/400/300?random=6746'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文以<strong>倒序</strong>的顺序并通过代码示例或简单的罗列展示<strong>所有 ECMAScript 版本</strong>提供的功能。 旨在为大家在编码时提供 ECMAScript 特性速查表</p>
<h2 data-id="heading-0">ES2021-ES12</h2>
<h3 data-id="heading-1">String.protype.replaceAll</h3>
<p>在 ES2021 之前，要替换掉一个字符串中的所有指定字符，我们可以这么做：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> str = <span class="hljs-string">"a+b+c+"</span>;
<span class="hljs-keyword">const</span> newStr = str.replace(<span class="hljs-regexp">/\+/g</span>, <span class="hljs-string">"🤣"</span>);
<span class="hljs-built_in">console</span>.log(newStr); <span class="hljs-comment">//a🤣b🤣c🤣</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES2021 则提出了 <code>replaceAll</code> 方法，并将其挂载在 String 的原型上，可以这么用：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> str = <span class="hljs-string">"a+b+c+"</span>;
<span class="hljs-keyword">const</span> newStr = str.replaceAll(<span class="hljs-string">"+"</span>, <span class="hljs-string">"🤣"</span>);
<span class="hljs-built_in">console</span>.log(newStr); <span class="hljs-comment">//a🤣b🤣c🤣</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">Promise.any</h3>
<p><code>Promise.any</code></p>
<ul>
<li>接收一个 Promise 可迭代对象，只要其中任意一个 promise 成功，就返回那个已经成功的 promise</li>
<li>如果所有的 promises 都失败/拒绝，就返回一个失败的 promise</li>
</ul>
<p><code>Promise.race</code> 的对比:</p>
<ul>
<li>只要任意一个 promise 的状态改变(不管成功 or 失败)，那么就返回那个 promise</li>
</ul>
<p><code>Promise.all()</code>的对比</p>
<ul>
<li>只要任意一个 promise 失败，则返回失败的 promise</li>
<li>当所有异步操作都成功后，才返回 promise,返回值组成一个数组</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> pErr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  reject(<span class="hljs-string">"总是失败"</span>);
&#125;);

<span class="hljs-keyword">const</span> pSlow = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">500</span>, <span class="hljs-string">"最终完成"</span>);
&#125;);

<span class="hljs-keyword">const</span> pFast = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">100</span>, <span class="hljs-string">"很快完成"</span>);
&#125;);

<span class="hljs-comment">// 使用 .then .catch</span>
<span class="hljs-built_in">Promise</span>.any([pErr, pSlow, pFast])
  .then(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
    <span class="hljs-comment">// 返回最先成功的一个promise ,即: pFast-"很快完成"</span>
    <span class="hljs-built_in">console</span>.log(value);
  &#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-comment">// 所有的 promise 都失败时触发</span>
  &#125;);

<span class="hljs-comment">// 使用 async-await</span>
<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-keyword">const</span> first = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.any(promises); <span class="hljs-comment">// 任何一个 promise 成功返回。</span>
  <span class="hljs-built_in">console</span>.log(first);
&#125; <span class="hljs-keyword">catch</span> (error) &#123;
  <span class="hljs-comment">// 所有的 promise 都失败了</span>
  <span class="hljs-built_in">console</span>.log(error);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">WeakRef</h3>
<p><code>WeakRef</code> 提案主要包含两个新功能：</p>
<ul>
<li>可以通过 <code>WeakRef</code> 类来给某个对象创建一个弱引用</li>
<li>可以通过 <code>FinalizationRegistry</code> 类，在某个对象被垃圾回收之后，执行一些自定义方法</li>
</ul>
<p>上述两个新功能可以同时使用，也可以单独使用，取决于你的需求。一个 <code>WeakRef</code> 对象包含一个对于某个对象的弱引用，被称为<em>目标</em>或<em>引用</em>。通过弱引用一个对象，可以让该对象在没有其它引用的情况下被垃圾回收机制回收。<code>WeakRef</code> 主要用来缓存和映射一些大型对象，当你希望某个对象在不被其它地方引用的情况下及时地被垃圾回收，那么你就可以使用它。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toogle</span>(<span class="hljs-params">element</span>) </span>&#123;
  <span class="hljs-keyword">const</span> weakElement = <span class="hljs-keyword">new</span> WeakRef(element);
  <span class="hljs-keyword">let</span> intervalId = <span class="hljs-literal">null</span>;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toggle</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> el = weakElement.deref();
    <span class="hljs-keyword">if</span> (!el) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">clearInterval</span>(intervalId);
    &#125;
    <span class="hljs-keyword">const</span> decoration = weakElement.style.textDecoration;
    <span class="hljs-keyword">const</span> style = decoration === <span class="hljs-string">"none"</span> ? <span class="hljs-string">"underline"</span> : <span class="hljs-string">"none"</span>;
    decoration = style;
  &#125;
  intervalId = <span class="hljs-built_in">setInterval</span>(toggle, <span class="hljs-number">1000</span>);
&#125;
<span class="hljs-keyword">const</span> element = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"link"</span>);
toogle(element);
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> element.remove(), <span class="hljs-number">10000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>FinalizationRegistry</code> 接收一个注册器回调函数，可以利用该注册器为指定对象注册一个事件监听器，当这个对象被垃圾回收之后，会触发监听的事件，具体步骤如下。首先，创建一个注册器：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> registry = <span class="hljs-keyword">new</span> FinalizationRegistry(<span class="hljs-function">(<span class="hljs-params">heldValue</span>) =></span> &#123;
  <span class="hljs-comment">// ....</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着注册一个指定对象，同时也可以给注册器回调传递一些参数：</p>
<pre><code class="hljs language-ts copyable" lang="ts">registry.register(theObject, <span class="hljs-string">"some value"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">逻辑赋值运算符</h3>
<p>详细信息参考<a href="https://tc39.es/proposal-logical-assignment/" target="_blank" rel="nofollow noopener noreferrer">ts39-proposal-logical-assignment</a></p>
<p>逻辑赋值运算符结合了逻辑运算符和赋值表达式。逻辑赋值运算符有两种：</p>
<ul>
<li>或等于（<code>||=</code>）</li>
<li>且等于（<code>&&=</code>）</li>
<li><code>??=</code></li>
</ul>
<h3 data-id="heading-5"><code>||=</code></h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> giveKey = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"somekey"</span>;
&#125;;
<span class="hljs-keyword">let</span> userDetails = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"chika"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">5</span>, <span class="hljs-attr">room</span>: <span class="hljs-number">10</span>, <span class="hljs-attr">key</span>: <span class="hljs-string">""</span> &#125;;
userDetails.key ||= giveKey();
<span class="hljs-built_in">console</span>.log(userDetails.key);

<span class="hljs-comment">//output : somekey</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">&&=</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> deleteKey = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">" "</span>;
&#125;;
<span class="hljs-keyword">let</span> userDetails = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"chika"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">5</span>, <span class="hljs-attr">room</span>: <span class="hljs-number">10</span>, <span class="hljs-attr">key</span>: <span class="hljs-string">"990000"</span> &#125;;
userDetails.key &&= deleteKey();
<span class="hljs-built_in">console</span>.log(userDetails.key);

<span class="hljs-comment">//output : ""</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">??= 空赋值运算符</h3>
<p><code>??=</code> 也被称为空赋值运算符，与上面的非空运算符相关。看看它们之间的联系：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">var</span> x = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">var</span> y = <span class="hljs-number">5</span>;
<span class="hljs-built_in">console</span>.log((x ??= y)); <span class="hljs-comment">// => 5</span>
<span class="hljs-built_in">console</span>.log((x = x ?? y)); <span class="hljs-comment">// => 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>仅当值为 <code>null</code> 或 <code>undefined</code> 时，此赋值运算符才会赋值。上面的例子强调了这个运算符本质上是空赋值的语法糖（类似的语法糖：<code>a = a + b</code> 可写成 <code>a += b</code> ）。接下来，让我们看看这个运算符与默认参数（默认参数是 ES6 引入的新语法，仅当函数参数为 <code>undefined</code> 时，给它设置一个默认值）的区别：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">gameSettingsWithNullish</span>(<span class="hljs-params">options</span>) </span>&#123;
  options.gameSpeed ??= <span class="hljs-number">1</span>;
  options.gameDiff ??= <span class="hljs-string">"easy"</span>;
  <span class="hljs-keyword">return</span> options;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">gameSettingsWithDefaultParams</span>(<span class="hljs-params">gameSpeed = <span class="hljs-number">1</span>, gameDiff = <span class="hljs-string">"easy"</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123; gameSpeed, gameDiff &#125;;
&#125;
gameSettingsWithNullish(&#123; <span class="hljs-attr">gameSpeed</span>: <span class="hljs-literal">null</span>, <span class="hljs-attr">gameDiff</span>: <span class="hljs-literal">null</span> &#125;); <span class="hljs-comment">// => &#123;gameSpeed: 1, gameDiff: 'easy'&#125;</span>
gameSettingsWithDefaultParams(<span class="hljs-literal">undefined</span>, <span class="hljs-literal">null</span>); <span class="hljs-comment">// => &#123;gameSpeed: null, gameDiff: null&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述函数处理空值的方式有一个值得注意的区别。默认参数将用空参数（这里的空参数，只能是 <code>undefined</code>）覆盖默认值，空赋值运算符将不会。默认参数和空赋值都不会覆盖未定义的值。<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Logical_nullish_assignment" target="_blank" rel="nofollow noopener noreferrer">MDN 官方文档</a></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> getKey = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"somekey"</span>;
&#125;;
<span class="hljs-keyword">let</span> userDetails = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"chika"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">5</span>, <span class="hljs-attr">room</span>: <span class="hljs-number">10</span> &#125;;
userDetails.key ??= getKey();
<span class="hljs-built_in">console</span>.log(userDetails.key);

<span class="hljs-comment">//output : "somekey"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">数字分隔符</h3>
<p>通过这个功能，我们利用 <code>\_，U+005F</code> 分隔符来将数字分组，提高数字的可读性：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-number">1_000_000_000</span>; <span class="hljs-comment">// 十亿</span>
<span class="hljs-number">101_475_938.38</span>; <span class="hljs-comment">// 亿万</span>

<span class="hljs-keyword">const</span> amount = <span class="hljs-number">12345_00</span>; <span class="hljs-comment">// 12,345</span>
<span class="hljs-keyword">const</span> amount = <span class="hljs-number">123_4500</span>; <span class="hljs-comment">// 123.45 (保留 4 位小数)</span>
<span class="hljs-keyword">const</span> amount = <span class="hljs-number">1_234_500</span>; <span class="hljs-comment">// 1,234,500</span>

<span class="hljs-number">0.000_001</span>; <span class="hljs-comment">// 百万分之一</span>
<span class="hljs-number">1e10_000</span>; <span class="hljs-comment">// 10^10000</span>

<span class="hljs-comment">//</span>
<span class="hljs-keyword">const</span> binary_literals = <span class="hljs-number">0b1010_0001_1000_0101</span>;
<span class="hljs-keyword">const</span> hex_literals = <span class="hljs-number">0xa0_b0_c0</span>;
<span class="hljs-comment">//</span>
<span class="hljs-keyword">const</span> bigInt_literals = <span class="hljs-number">1_000_000_000_000n</span>;
<span class="hljs-comment">//</span>
<span class="hljs-keyword">const</span> octal_literal = <span class="hljs-number">0o1234_5670</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-9">ES2020-ES11</h2>
<p>ES2020 是与 2020 年相对应的 ECMAScript 版本</p>
<h3 data-id="heading-10">String.protype.matchAll</h3>
<p><code>matchAll()</code>方法返回一个正则表达式在当前字符串的所有匹配</p>
<p>不过，它返回的是一个遍历器（Iterator），而不是数组。遍历器转为数组是非常简单的，使用<code>...</code>运算符和 <code>Array.from()</code>方法就可以了。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> <span class="hljs-built_in">string</span> = <span class="hljs-string">"test1test2test3"</span>;
<span class="hljs-keyword">const</span> regex = <span class="hljs-regexp">/t(e)(st(\d?))/g</span>;

<span class="hljs-keyword">const</span> newdata = <span class="hljs-built_in">string</span>.matchAll(regex);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> match <span class="hljs-keyword">of</span> newdata) &#123;
  <span class="hljs-built_in">console</span>.log(match);
&#125;
<span class="hljs-comment">// ["test1", "e", "st1", "1", index: 0, input: "test1test2test3"]</span>
<span class="hljs-comment">// ["test2", "e", "st2", "2", index: 5, input: "test1test2test3"]</span>
<span class="hljs-comment">// ["test3", "e", "st3", "3", index: 10, input: "test1test2test3"]</span>

<span class="hljs-comment">// 转为数组的方法一</span>
[...newdata];

<span class="hljs-comment">// 转为数组的方法二</span>
<span class="hljs-built_in">Array</span>.from(newdata);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>详细内容参考<a href="https://es6.ruanyifeng.com/#docs/regex#String-prototype-matchAll" target="_blank" rel="nofollow noopener noreferrer">ES 入门-matchAll</a></p>
<h3 data-id="heading-11">Dynamic import</h3>
<p><code>import(specifier)</code>函数，支持动态加载模块, <code>import</code> 函数的参数 <code>specifier</code>，指定所要加载的模块的位置。<code>import</code> 命令能够接受什么参数，<code>import()</code>函数就能接受什么参数，两者区别主要是后者为动态加载。</p>
<p><code>import()</code>返回一个 Promise 对象</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> someVariable = <span class="hljs-string">"user"</span>;

<span class="hljs-keyword">import</span>(<span class="hljs-string">`./some-modules/<span class="hljs-subst">$&#123;someVariable&#125;</span>.js`</span>)
  .then(<span class="hljs-function">(<span class="hljs-params"><span class="hljs-built_in">module</span></span>) =></span> &#123;
    <span class="hljs-comment">// 业务逻辑</span>
    <span class="hljs-built_in">module</span>.loadPageInto(main);
  &#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-comment">// 加载失败</span>
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>详细内容参考<a href="https://es6.ruanyifeng.com/#docs/module#import" target="_blank" rel="nofollow noopener noreferrer">ES 入门-import</a></p>
<h3 data-id="heading-12">Promise.allSettled</h3>
<p><code>Promise.allSettled()</code>方法接受一组 Promise 实例作为参数，包装成一个新的 Promise 实例。只有等到所有这些参数实例都返回结果，不管是<code>fulfilled</code>还是<code>rejected</code>，包装实例才会结束</p>
<p>有时候，我们不关心异步请求的结果，只关心所有的请求有没有结束。这时，<code>Promise.allSettled()</code>方法就很有用</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> promises = [fetch(<span class="hljs-string">"index.html"</span>), fetch(<span class="hljs-string">"https://does-not-exist/"</span>)];
<span class="hljs-keyword">const</span> results = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.allSettled(promises);

<span class="hljs-comment">// 过滤出成功的请求</span>
<span class="hljs-keyword">const</span> successfulPromises = results.filter(<span class="hljs-function">(<span class="hljs-params">p</span>) =></span> p.status === <span class="hljs-string">"fulfilled"</span>);

<span class="hljs-comment">// 过滤出失败的请求，并输出原因</span>
<span class="hljs-keyword">const</span> errors = results
  .filter(<span class="hljs-function">(<span class="hljs-params">p</span>) =></span> p.status === <span class="hljs-string">"rejected"</span>)
  .map(<span class="hljs-function">(<span class="hljs-params">p</span>) =></span> p.reason);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">globalThis</h3>
<p>ES2020 之前获取不同环境的<code>this</code>需要如下封装</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> getGlobalThis = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 在 webworker 或 service worker 中</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> self !== <span class="hljs-string">"undefined"</span>) <span class="hljs-keyword">return</span> self;

  <span class="hljs-comment">// 在浏览器中</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span> !== <span class="hljs-string">"undefined"</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">window</span>;

  <span class="hljs-comment">// 在 Node.js 中</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">global</span> !== <span class="hljs-string">"undefined"</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">global</span>;

  <span class="hljs-comment">// 独立的 JavaScript shell</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span> !== <span class="hljs-string">"undefined"</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;

  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"Unable to locate global object"</span>);
&#125;;
<span class="hljs-keyword">const</span> theGlobalThis = getGlobalThis();

<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> theGlobalThis.setTimeout !== <span class="hljs-string">"function"</span>) &#123;
  <span class="hljs-comment">// 此环境中没有 setTimeout 方法！</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，<code>globalThis</code> 提供了一个标准的方式来获取不同环境下的全局 <code>this </code> 对象（也就是全局对象自身）</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> globalThis.setTimeout !== <span class="hljs-string">"function"</span>) &#123;
  <span class="hljs-comment">// 此环境中没有 setTimeout 方法！</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>详细内容参考<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/globalThis" target="_blank" rel="nofollow noopener noreferrer">MDN-globalThis</a></p>
<h3 data-id="heading-14">空位合并操作符（Nullish coalescing Operator）</h3>
<p>在 JS 中，<code>??</code> 运算符被称为非空运算符。如果第一个参数不是 <code>null/undefined</code>（这里只有两个假值，但是 JS 中假值包含：未定义 <code>undefined</code>、空对象 <code>null</code>、数值 <code>0</code>、空数字 <code>NaN</code>、布尔 <code>false</code>，空字符串<code>''</code>，不要搞混了），将返回第一个参数，否则返回第二个参数。比如，</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-literal">null</span> ?? <span class="hljs-number">5</span>; <span class="hljs-comment">// => 5</span>
<span class="hljs-number">3</span> ?? <span class="hljs-number">5</span>; <span class="hljs-comment">// => 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给变量设置默认值时，以前常用 <code>||</code>逻辑或运算符，例如，</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> prevMoney = <span class="hljs-number">1</span>;
<span class="hljs-keyword">const</span> currMoney = <span class="hljs-number">0</span>;
<span class="hljs-keyword">const</span> noAccount = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">const</span> futureMoney = -<span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">moneyAmount</span>(<span class="hljs-params">money</span>) </span>&#123;
  <span class="hljs-keyword">return</span> money || <span class="hljs-string">`账户未开通`</span>;
&#125;
<span class="hljs-built_in">console</span>.log(moneyAmount(prevMoney)); <span class="hljs-comment">// => 1</span>
<span class="hljs-built_in">console</span>.log(moneyAmount(currMoney)); <span class="hljs-comment">// => 账户未开通</span>
<span class="hljs-built_in">console</span>.log(moneyAmount(noAccount)); <span class="hljs-comment">// => 账户未开通</span>
<span class="hljs-built_in">console</span>.log(moneyAmount(futureMoney)); <span class="hljs-comment">// => -1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们创建了函数 <code>moneyAmount</code>，它返回当前用户余额。我们使用 <code>||</code> 运算符来识别没有帐户的用户。然而，当用户没有帐户时，这意味着什么？将无账户视为空而不是 0 更为准确，因为银行账户可能没有（或负）货币。在上面的例子中，<code>||</code> 运算符将 0 视为一个虚假值，不应该包括用户有 0 美元的帐户。让我们使用<code>??</code> 非空运算符来解决这个问题：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> currMoney = <span class="hljs-number">0</span>;
<span class="hljs-keyword">const</span> noAccount = <span class="hljs-literal">null</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">moneyAmount</span>(<span class="hljs-params">money</span>) </span>&#123;
  <span class="hljs-keyword">return</span> money ?? <span class="hljs-string">`账户未开通`</span>;
&#125;
moneyAmount(currMoney); <span class="hljs-comment">// => 0</span>
moneyAmount(noAccount); <span class="hljs-comment">// => `账户未开通`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>概括地说 <code>??</code> 运算符允许我们在忽略错误值（如 0 和空字符串）的同时指定默认值。</p>
<h3 data-id="heading-15">可选链操作符（Optional Chaining）</h3>
<p><code>?.</code> 也叫链判断运算符。它允许开发人员读取深度嵌套在对象链中的属性值，而不必验证每个引用。当引用为空时，表达式停止计算并返回 <code>undefined</code>。比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">var</span> travelPlans = &#123;
  <span class="hljs-attr">destination</span>: <span class="hljs-string">"DC"</span>,
  <span class="hljs-attr">monday</span>: &#123;
    <span class="hljs-attr">location</span>: <span class="hljs-string">"National Mall"</span>,
    <span class="hljs-attr">budget</span>: <span class="hljs-number">200</span>,
  &#125;,
&#125;;
<span class="hljs-built_in">console</span>.log(travelPlans.tuesday?.location); <span class="hljs-comment">// => undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，把我们刚刚学到的结合起来</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addPlansWhenUndefined</span>(<span class="hljs-params">plans, location, budget</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (plans.tuesday?.location == <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-keyword">var</span> newPlans = &#123;
      plans,
      <span class="hljs-attr">tuesday</span>: &#123;
        <span class="hljs-attr">location</span>: location ?? <span class="hljs-string">"公园"</span>,
        <span class="hljs-attr">budget</span>: budget ?? <span class="hljs-number">200</span>,
      &#125;,
    &#125;;
  &#125; <span class="hljs-keyword">else</span> &#123;
    newPlans ??= plans; <span class="hljs-comment">// 只有 newPlans 是 undefined 时，才覆盖</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"已安排计划"</span>);
  &#125;
  <span class="hljs-keyword">return</span> newPlans;
&#125;
<span class="hljs-comment">// 对象 travelPlans 的初始值，来自上面一个例子</span>
<span class="hljs-keyword">var</span> newPlans = addPlansWhenUndefined(travelPlans, <span class="hljs-string">"Ford 剧院"</span>, <span class="hljs-literal">null</span>);
<span class="hljs-built_in">console</span>.log(newPlans);
<span class="hljs-comment">// => &#123; plans:</span>
<span class="hljs-comment">// &#123; destination: 'DC',</span>
<span class="hljs-comment">// monday: &#123; location: '国家购物中心', budget: 200 &#125; &#125;,</span>
<span class="hljs-comment">// tuesday: &#123; location: 'Ford 剧院', budget: 200 &#125; &#125;</span>
newPlans = addPlansWhenUndefined(newPlans, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>);
<span class="hljs-comment">// logs => 已安排计划</span>
<span class="hljs-comment">// returns => newPlans object</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子包含了我们到目前为止所学的所有运算符。现在我们已经创建了一个函数，该函数将计划添加到当前没有嵌套属性的对象 <code>tuesday.location</code> 中。我们还使用了非空运算符来提供默认值。此函数将错误地接受像“0”这样的值作为有效参数。这意味着 <code>budget</code> 可以设置为零，没有任何错误。</p>
<h3 data-id="heading-16">BigInt primitive type</h3>
<p>旧版本的 JS 标准最大的整数只能是<code>253 - 1</code>， 现在使用<code>BigInt</code> 用来表示整数，没有位数的限制，任何位数的整数都可以精确表示。 这是 ECMAScript 的又一种数据类型。</p>
<p>可以用在一个整数字面量后面加 n 的方式定义一个 BigInt ，如：10n，或者调用函数 BigInt()。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> theBiggestInt = <span class="hljs-number">9007199254740991n</span>;

<span class="hljs-keyword">const</span> alsoHuge = BigInt(<span class="hljs-number">9007199254740991</span>);
<span class="hljs-comment">// ↪ 9007199254740991n</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><a href="https://es6.ruanyifeng.com/#docs/number#BigInt-%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B" target="_blank" rel="nofollow noopener noreferrer">ES 入门-BigInt</a></li>
</ul>
<hr>
<h2 data-id="heading-17">ES2019-ES10</h2>
<h3 data-id="heading-18">Array#&#123;flat,flatMap&#125;</h3>
<p>数组的成员有时还是数组，<code>Array.prototype.flat()</code>用于将嵌套的数组“拉平”，变成一维的数组。该方法返回一个新数组，对原数据没有影响。</p>
<pre><code class="hljs language-ts copyable" lang="ts">[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, [<span class="hljs-number">3</span>, <span class="hljs-number">4</span>]].flat();
<span class="hljs-comment">// [1, 2, 3, 4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>flatMap()</code>只能展开一层数组。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 相当于 [[[2]], [[4]], [[6]], [[8]]].flat()</span>
[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>].flatMap(<span class="hljs-function">(<span class="hljs-params">x</span>) =></span> [[x * <span class="hljs-number">2</span>]]);
<span class="hljs-comment">// [[2], [4], [6], [8]]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>详细内容参考<a href="https://es6.ruanyifeng.com/#docs/array#%E6%95%B0%E7%BB%84%E5%AE%9E%E4%BE%8B%E7%9A%84-flat%EF%BC%8CflatMap" target="_blank" rel="nofollow noopener noreferrer">ES 入门-flat</a></p>
<h3 data-id="heading-19">Object.fromEntries</h3>
<p><code>Object.fromEntries()</code>方法是<code>Object.entries()</code>的逆操作，用于将一个键值对数组转为对象。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">Object</span>.fromEntries([
  [<span class="hljs-string">"foo"</span>, <span class="hljs-string">"bar"</span>],
  [<span class="hljs-string">"baz"</span>, <span class="hljs-number">42</span>],
]);
<span class="hljs-comment">// &#123; foo: "bar", baz: 42 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该方法的主要目的，是将键值对的数据结构还原为对象，因此特别适合将 Map 结构转为对象。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 例一</span>
<span class="hljs-keyword">const</span> entries = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([
  [<span class="hljs-string">"foo"</span>, <span class="hljs-string">"bar"</span>],
  [<span class="hljs-string">"baz"</span>, <span class="hljs-number">42</span>],
]);

<span class="hljs-built_in">Object</span>.fromEntries(entries);
<span class="hljs-comment">// &#123; foo: "bar", baz: 42 &#125;</span>

<span class="hljs-comment">// 例二</span>
<span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>().set(<span class="hljs-string">"foo"</span>, <span class="hljs-literal">true</span>).set(<span class="hljs-string">"bar"</span>, <span class="hljs-literal">false</span>);
<span class="hljs-built_in">Object</span>.fromEntries(map);
<span class="hljs-comment">// &#123; foo: true, bar: false &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">String#&#123;trimStart,trimEnd&#125;</h3>
<p>ES2019 对字符串实例新增了<code>trimStart()</code>和<code>trimEnd()</code>这两个方法。它们的行为与<code>trim()</code>一致，<code>trimStart()</code>消除字符串头部的空格，<code>trimEnd()</code>消除尾部的空格。它们返回的都是新字符串，不会修改原始字符串。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> s = <span class="hljs-string">"  abc  "</span>;

s.trim(); <span class="hljs-comment">// "abc"</span>
s.trimStart(); <span class="hljs-comment">// "abc  "</span>
s.trimEnd(); <span class="hljs-comment">// "  abc"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">Symbol#description</h3>
<p>ES2019 提供了一个实例属性<code>description</code>，直接返回 Symbol 的描述。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 创建 Symbol 的时候，可以添加一个描述。</span>
<span class="hljs-keyword">const</span> sym = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"foo"</span>);

sym.description; <span class="hljs-comment">// "foo"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>sym</code> 的描述就是字符串 <code>foo</code>。</p>
<h3 data-id="heading-22">try &#123; &#125; catch &#123;&#125; // optional binding</h3>
<p>旧版本的<code>try / catch</code>语句中的<code>catch</code>子句需要一个变量。 现在可以不加了</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 旧版本</span>
<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-built_in">console</span>.log(a);
&#125; <span class="hljs-keyword">catch</span> (error) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"报错了"</span>);
&#125;

<span class="hljs-comment">// ES2019-SE10</span>
<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-built_in">console</span>.log(a);
&#125; <span class="hljs-keyword">catch</span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"报错了"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">U+2028 和 U+2029</h3>
<p>在 ES2019 之前的版本中，不接受不转义的</p>
<ul>
<li>行分隔符<code>U + 2028</code></li>
<li>段落分隔符<code>U + 2029</code></li>
</ul>
<p>ES2019 允许 JavaScript 字符串直接输入 U+2028（行分隔符）和 U+2029（段分隔符）。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/*
ES2019之前，下面的代码会报错

ES2019 下面代码不会报错。
*/</span>
<span class="hljs-keyword">const</span> PS = <span class="hljs-built_in">eval</span>(<span class="hljs-string">"'\u2029'"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://es6.ruanyifeng.com/#docs/string#%E7%9B%B4%E6%8E%A5%E8%BE%93%E5%85%A5-U-2028-%E5%92%8C-U-2029" target="_blank" rel="nofollow noopener noreferrer">ES 入门-U+2028 和 U+2029</a></p>
<h3 data-id="heading-24">JSON-stringify-的改造</h3>
<p>为了确保返回的是合法的 UTF-8 字符，ES2019 改变了 <code>JSON.stringify()</code>的行为。如果遇到 <code>0xD800</code> 到 <code>0xDFFF</code> 之间的单个码点，或者不存在的配对形式，它会返回转义字符串，留给应用自己决定下一步的处理。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-string">"\u&#123;D834&#125;"</span>); <span class="hljs-comment">// ""\\uD834""</span>
<span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-string">"\uDF06\uD834"</span>); <span class="hljs-comment">// ""\\udf06\\ud834""</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://es6.ruanyifeng.com/#docs/string#JSON-stringify-%E7%9A%84%E6%94%B9%E9%80%A0" target="_blank" rel="nofollow noopener noreferrer">ES 入门-JSON-stringify-的改造</a></p>
<h3 data-id="heading-25">Array.prototype.sort() 的稳定排序</h3>
<p>早先的 ECMAScript 没有规定，<code>Array.prototype.sort()</code>的默认排序算法是否稳定，留给浏览器自己决定，这导致某些实现是不稳定的。<strong>ES2019</strong> 明确规定，<code>Array.prototype.sort()</code>的默认排序算法必须稳定。这个规定已经做到了，现在 JavaScript 各个主要实现的默认排序算法都是稳定的。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> arr = [<span class="hljs-string">"peach"</span>, <span class="hljs-string">"straw"</span>, <span class="hljs-string">"apple"</span>, <span class="hljs-string">"spork"</span>];

<span class="hljs-keyword">const</span> stableSorting = <span class="hljs-function">(<span class="hljs-params">s1, s2</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (s1[<span class="hljs-number">0</span>] < s2[<span class="hljs-number">0</span>]) <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
&#125;;

arr.sort(stableSorting);
<span class="hljs-comment">// ["apple", "peach", "straw", "spork"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://es6.ruanyifeng.com/#docs/array#Array-prototype-sort-%E7%9A%84%E6%8E%92%E5%BA%8F%E7%A8%B3%E5%AE%9A%E6%80%A7" target="_blank" rel="nofollow noopener noreferrer">ES 入门-排序稳定性</a></p>
<h3 data-id="heading-26">revised Function#toString</h3>
<p>ES2019 对函数实例的 <code>toString()</code>方法做出了修改。</p>
<p><code>toString()</code>方法返回函数代码本身，以前会省略注释和空格。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> /* <span class="hljs-title">foo</span> <span class="hljs-title">comment</span> */ <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

<span class="hljs-comment">// 老版本</span>
foo.toString();
<span class="hljs-comment">// function foo() &#123;&#125;</span>

<span class="hljs-comment">// 新版</span>
foo.toString();
<span class="hljs-comment">// "function /* foo comment */ foo () &#123;&#125;"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-27">ES2018-ES9</h2>
<h3 data-id="heading-28">解除模板字面量限制(Lifting template literal restriction).</h3>
<p>ES2018 放松了对标签模板里面的字符串转义的限制。如果遇到不合法的字符串转义，就返回<code>undefined</code>，而不是报错，并且从<code>raw</code>属性上面可以得到原始字符串。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tag</span>(<span class="hljs-params">strs</span>) </span>&#123;
  strs[<span class="hljs-number">0</span>] === <span class="hljs-literal">undefined</span>
  strs.raw[<span class="hljs-number">0</span>] === <span class="hljs-string">"\\unicode and \\u&#123;55&#125;"</span>;
&#125;
tag<span class="hljs-string">`\unicode and \u&#123;55&#125;`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，模板字符串原本是应该报错的，但是由于放松了对字符串转义的限制，所以不报错了，JavaScript 引擎将第一个字符设置为<code>undefined</code>，但是<code>raw</code>属性依然可以得到原始字符串，因此<code>tag</code>函数还是可以对原字符串进行处理。</p>
<ul>
<li><a href="https://es6.ruanyifeng.com/#docs/string#%E6%A8%A1%E6%9D%BF%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E9%99%90%E5%88%B6" target="_blank" rel="nofollow noopener noreferrer">ES 入门-模板字符串的限制</a></li>
<li><a href="https://es6.ruanyifeng.com/#docs/string-methods#String-raw" target="_blank" rel="nofollow noopener noreferrer">ES 入门-row</a></li>
<li><a href="https://es6.ruanyifeng.com/#docs/regex#u-%E4%BF%AE%E9%A5%B0%E7%AC%A6" target="_blank" rel="nofollow noopener noreferrer">ES 入门-修饰符：u</a></li>
</ul>
<h3 data-id="heading-29">正则之 s 修饰符：dotAll 模式-(s (dotAll) flag for regular expressions).</h3>
<p>ES2018 引入 <code>s </code>修饰符，使得<code>.</code>可以匹配任意单个字符。</p>
<pre><code class="hljs language-ts copyable" lang="ts">/foo.bar/s.test(<span class="hljs-string">"foo\nbar"</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这被称为<code>dotAll</code>模式，即点（dot）代表一切字符。所以，正则表达式还引入了一个<code>dotAll</code>属性，返回一个布尔值，表示该正则表达式是否处在<code>dotAll</code>模式。</p>
<p><a href="https://es6.ruanyifeng.com/#docs/regex#s-%E4%BF%AE%E9%A5%B0%E7%AC%A6%EF%BC%9AdotAll-%E6%A8%A1%E5%BC%8F" target="_blank" rel="nofollow noopener noreferrer">ES 入门-修饰符：dotAll 模式</a></p>
<h3 data-id="heading-30">正则之具名组匹配(RegExp named capture groups)</h3>
<p>ES2018 引入了具名组匹配（Named Capture Groups），允许为每一个组匹配指定一个名字，既便于阅读代码，又便于引用。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> RE_DATE = <span class="hljs-regexp">/(?<year>\d&#123;4&#125;)-(?<month>\d&#123;2&#125;)-(?<day>\d&#123;2&#125;)/</span>;

<span class="hljs-keyword">const</span> matchObj = RE_DATE.exec(<span class="hljs-string">"1999-12-31"</span>);
<span class="hljs-keyword">const</span> year = matchObj.groups.year; <span class="hljs-comment">// "1999"</span>
<span class="hljs-keyword">const</span> month = matchObj.groups.month; <span class="hljs-comment">// "12"</span>
<span class="hljs-keyword">const</span> day = matchObj.groups.day; <span class="hljs-comment">// "31"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://es6.ruanyifeng.com/#docs/regex#%E5%85%B7%E5%90%8D%E7%BB%84%E5%8C%B9%E9%85%8D" target="_blank" rel="nofollow noopener noreferrer">ES 入门-修饰符：具名组匹配</a></p>
<h3 data-id="heading-31">Rest/Spread Properties.</h3>
<p>ES6 为数组引入了扩展运算符的写法，</p>
<p>在 ES2018 中，为对象也引入了此写法</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">a</span>: <span class="hljs-string">"a"</span>, <span class="hljs-attr">b</span>: <span class="hljs-string">"b"</span>, <span class="hljs-attr">c</span>: <span class="hljs-string">"c"</span>, <span class="hljs-attr">d</span>: <span class="hljs-string">"d"</span>, <span class="hljs-attr">e</span>: <span class="hljs-string">"e"</span> &#125;;

<span class="hljs-comment">// 对象结构</span>
<span class="hljs-keyword">const</span> &#123; a, b, c, ...rest &#125; = obj;

<span class="hljs-comment">// 组成新对象</span>
<span class="hljs-keyword">const</span> newObj = &#123; a, ...rest &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">正则之后行断言(RegExp Lookbehind Assertions.)</h3>
<p>ES2018 引入后行断言</p>
<p>“后行断言”指: <code>x</code>只有不在<code>y</code>后面才匹配，必须写成<code>/(?<!y)x/</code>。比如，只匹配不在美元符号后面的数字，要写成<code>/(?<!\$)\d+/</code>。</p>
<pre><code class="hljs language-ts copyable" lang="ts">/(?<=\$)\d+<span class="hljs-regexp">/.exec('Benjamin Franklin is on the $100 bill')  /</span><span class="hljs-regexp">/ ["100"]
/</span>(?<!\$)\d+<span class="hljs-regexp">/.exec('it’s is worth about €90')                /</span><span class="hljs-regexp">/ ["90"]
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>使用后行断言进行字符串替换。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> RE_DOLLAR_PREFIX = <span class="hljs-regexp">/(?<=\$)foo/g</span>;
<span class="hljs-string">"$foo %foo foo"</span>.replace(RE_DOLLAR_PREFIX, <span class="hljs-string">"bar"</span>);
<span class="hljs-comment">// '$bar %foo foo'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://es6.ruanyifeng.com/#docs/regex#%E5%90%8E%E8%A1%8C%E6%96%AD%E8%A8%80" target="_blank" rel="nofollow noopener noreferrer">ES 入门-后行断言</a></p>
<h3 data-id="heading-33">Unicode 属性类(RegExp Unicode Property Escapes)</h3>
<p>ES2018 引入了一种新的类的写法<code>\p&#123;...&#125;</code>和<code>\P&#123;...&#125;</code>，允许正则表达式匹配符合 Unicode 某种属性的所有字符。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> regexGreekSymbol = <span class="hljs-regexp">/\p&#123;Script=Greek&#125;/u</span>;
regexGreekSymbol.test(<span class="hljs-string">"π"</span>); <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 匹配所有空格</span>
<span class="hljs-keyword">const</span> reg = <span class="hljs-regexp">/\p&#123;White_Space&#125;/</span>;

<span class="hljs-comment">// 匹配所有的箭头字符</span>
<span class="hljs-keyword">const</span> regexArrows = <span class="hljs-regexp">/^\p&#123;Block=Arrows&#125;+$/u</span>;
regexArrows.test(<span class="hljs-string">"←↑→↓↔↕↖↗↘↙⇏⇐⇑⇒⇓⇔⇕⇖⇗⇘⇙⇧⇩"</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://es6.ruanyifeng.com/#docs/regex#Unicode-%E5%B1%9E%E6%80%A7%E7%B1%BB" target="_blank" rel="nofollow noopener noreferrer">ES 入门-Unicode 属性类</a></p>
<h3 data-id="heading-34">Promise.prototype.finally.</h3>
<p><code>finally()</code>方法用于指定不管 Promise 对象最后状态如何，都会执行的操作。该方法是 ES2018 引入标准的。</p>
<pre><code class="hljs language-ts copyable" lang="ts">promise
.then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;···&#125;)
.catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;···&#125;)
.finally(<span class="hljs-function">() =></span> &#123;···&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，不管 promise 最后的状态，在执行完<code>then</code>或<code>catch</code>指定的回调函数以后，都会执行<code>finally</code>方法指定的回调函数。</p>
<p><a href="https://es6.ruanyifeng.com/#docs/promise#Promise-prototype-finally" target="_blank" rel="nofollow noopener noreferrer">ES 入门-finally</a></p>
<h3 data-id="heading-35">按顺序完成异步操作(Asynchronous Iteration)</h3>
<p>实际开发中，经常遇到一组异步操作，需要按照顺序完成。比如，依次远程读取一组 URL，然后按照读取的顺序输出结果。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">logInOrder</span>(<span class="hljs-params">urls</span>) </span>&#123;
  <span class="hljs-comment">// 并发读取远程URL</span>
  <span class="hljs-keyword">const</span> textPromises = urls.map(<span class="hljs-keyword">async</span> (url) => &#123;
    <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> fetch(url);
    <span class="hljs-keyword">return</span> response.text();
  &#125;);

  <span class="hljs-comment">// 按次序输出</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> textPromise <span class="hljs-keyword">of</span> textPromises) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">await</span> textPromise);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getData</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> promises = [fetch(<span class="hljs-string">"url1"</span>), fetch(<span class="hljs-string">"url2"</span>), fetch(<span class="hljs-string">"url3"</span>), fetch(<span class="hljs-string">"url4"</span>)];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> promises) &#123;
    <span class="hljs-comment">// 打印出promise</span>
    <span class="hljs-built_in">console</span>.log(item);
  &#125;

  <span class="hljs-keyword">for</span> <span class="hljs-keyword">await</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> promises) &#123;
    <span class="hljs-comment">// 打印出请求的结果</span>
    <span class="hljs-built_in">console</span>.log(item);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://es6.ruanyifeng.com/#docs/async#%E5%AE%9E%E4%BE%8B%EF%BC%9A%E6%8C%89%E9%A1%BA%E5%BA%8F%E5%AE%8C%E6%88%90%E5%BC%82%E6%AD%A5%E6%93%8D%E4%BD%9C" target="_blank" rel="nofollow noopener noreferrer">ES 入门-顺序异步操作</a></p>
<hr>
<h2 data-id="heading-36">ES2017-ES8</h2>
<h3 data-id="heading-37">Object.values/Object.entries</h3>
<p><code>Object.values</code> 方法返回一个数组，成员是参数对象自身的（不含继承的）所有可遍历（enumerable）属性的键值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">foo</span>: <span class="hljs-string">"bar"</span>, <span class="hljs-attr">baz</span>: <span class="hljs-number">42</span> &#125;;
<span class="hljs-built_in">Object</span>.values(obj);
<span class="hljs-comment">// ["bar", 42]</span>

<span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-number">100</span>: <span class="hljs-string">"a"</span>, <span class="hljs-number">2</span>: <span class="hljs-string">"b"</span>, <span class="hljs-number">7</span>: <span class="hljs-string">"c"</span> &#125;;
<span class="hljs-built_in">Object</span>.values(obj);
<span class="hljs-comment">// ["b", "c", "a"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Object.entries</code>方法返回一个数组，成员是参数对象自身的（不含继承的）所有可遍历（enumerable）属性的键值对数组。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">foo</span>: <span class="hljs-string">"bar"</span>, <span class="hljs-attr">baz</span>: <span class="hljs-number">42</span> &#125;;
<span class="hljs-built_in">Object</span>.entries(obj);
<span class="hljs-comment">// [ ["foo", "bar"], ["baz", 42] ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Object.entries</code> 的基本用途是遍历对象的属性。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> obj = &#123; <span class="hljs-attr">one</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">two</span>: <span class="hljs-number">2</span> &#125;;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [k, v] <span class="hljs-keyword">of</span> <span class="hljs-built_in">Object</span>.entries(obj)) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(k)&#125;</span>: <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(v)&#125;</span>`</span>);
&#125;
<span class="hljs-comment">// "one": 1</span>
<span class="hljs-comment">// "two": 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Object.entries</code> 方法的另一个用处是，将对象转为真正的 Map 结构。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">foo</span>: <span class="hljs-string">"bar"</span>, <span class="hljs-attr">baz</span>: <span class="hljs-number">42</span> &#125;;
<span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(<span class="hljs-built_in">Object</span>.entries(obj));
map; <span class="hljs-comment">// Map &#123; foo: "bar", baz: 42 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-38">String padding</h3>
<p>ES2017 引入了字符串补全长度的功能。如果某个字符串不够指定长度，会在头部或尾部补全。<code>padStart()</code>用于头部补全，<code>padEnd()</code>用于尾部补全。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-string">"x"</span>.padStart(<span class="hljs-number">5</span>, <span class="hljs-string">"ab"</span>); <span class="hljs-comment">// 'ababx'</span>
<span class="hljs-string">"x"</span>.padStart(<span class="hljs-number">4</span>, <span class="hljs-string">"ab"</span>); <span class="hljs-comment">// 'abax'</span>

<span class="hljs-string">"x"</span>.padEnd(<span class="hljs-number">5</span>, <span class="hljs-string">"ab"</span>); <span class="hljs-comment">// 'xabab'</span>
<span class="hljs-string">"x"</span>.padEnd(<span class="hljs-number">4</span>, <span class="hljs-string">"ab"</span>); <span class="hljs-comment">// 'xaba'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>padStart()的常见用途是为数值补全指定位数。下面代码生成 10 位的数值字符串。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-string">"1"</span>.padStart(<span class="hljs-number">10</span>, <span class="hljs-string">"0"</span>); <span class="hljs-comment">// "0000000001"</span>
<span class="hljs-string">"12"</span>.padStart(<span class="hljs-number">10</span>, <span class="hljs-string">"0"</span>); <span class="hljs-comment">// "0000000012"</span>
<span class="hljs-string">"123456"</span>.padStart(<span class="hljs-number">10</span>, <span class="hljs-string">"0"</span>); <span class="hljs-comment">// "0000123456"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个用途是提示字符串格式。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-string">"12"</span>.padStart(<span class="hljs-number">10</span>, <span class="hljs-string">"YYYY-MM-DD"</span>); <span class="hljs-comment">// "YYYY-MM-12"</span>
<span class="hljs-string">"09-12"</span>.padStart(<span class="hljs-number">10</span>, <span class="hljs-string">"YYYY-MM-DD"</span>); <span class="hljs-comment">// "YYYY-09-12"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-39">Object.getOwnPropertyDescriptors</h3>
<p>ES2017 引入了 <code>Object.getOwnPropertyDescriptors()</code>方法，返回指定对象所有自身属性（非继承属性）的<strong>描述对象</strong>。</p>
<ul>
<li><code>value</code> — 属性实际的值</li>
<li><code>writable</code> — 属性的值是否可以被修改</li>
<li><code>get</code> — 获取函数，在读取属性时调用</li>
<li><code>set</code> — 设置函数，在写入属性时调用</li>
<li><code>configurable</code> — 属性是否可以通过 delete 删除并重新定义，是否可以修改它的特 性，以及是否可以把它改为访问器属性</li>
<li><code>enumerable</code> — 属性是否可以通过 for-in 循环返回</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> obj = &#123;
  <span class="hljs-attr">foo</span>: <span class="hljs-number">123</span>,
  <span class="hljs-keyword">get</span> <span class="hljs-title">bar</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">"abc"</span>;
  &#125;,
&#125;;

<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptors(obj);
<span class="hljs-comment">// &#123; foo:</span>
<span class="hljs-comment">//    &#123; value: 123,</span>
<span class="hljs-comment">//      writable: true,</span>
<span class="hljs-comment">//      enumerable: true,</span>
<span class="hljs-comment">//      configurable: true &#125;,</span>
<span class="hljs-comment">//   bar:</span>
<span class="hljs-comment">//    &#123; get: [Function: get bar],</span>
<span class="hljs-comment">//      set: undefined,</span>
<span class="hljs-comment">//      enumerable: true,</span>
<span class="hljs-comment">//      configurable: true &#125; &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该方法的引入目的，主要是为了解决 <code>Object.assign()</code>无法正确拷贝 <code>get</code> 属性和 <code>set</code> 属性的问题。</p>
<p><code>Object.getOwnPropertyDescriptors()</code>方法的另一个用处，是配合 <code>Object.create()</code>方法，将对象属性克隆到一个新对象。这属于浅拷贝。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> shallowClone = <span class="hljs-function">(<span class="hljs-params">obj</span>) =></span>
  <span class="hljs-built_in">Object</span>.create(
    <span class="hljs-built_in">Object</span>.getPrototypeOf(obj),
    <span class="hljs-built_in">Object</span>.getOwnPropertyDescriptors(obj),
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/object-methods#Object-getOwnPropertyDescriptors" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-getOwnPropertyDescriptors</a></p>
<h3 data-id="heading-40">函数参数的尾逗号</h3>
<p>ES2017 允许函数的最后一个参数有尾逗号（trailing comma）。</p>
<p>此前，函数定义和调用时，都不允许最后一个参数后面出现逗号。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx">function clownsEverywhere(param1, param2,) &#123;
  /* ... */
&#125;

clownsEverywhere("foo", "bar",);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/function#%E5%87%BD%E6%95%B0%E5%8F%82%E6%95%B0%E7%9A%84%E5%B0%BE%E9%80%97%E5%8F%B7" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-函数参数的尾逗号</a></p>
<h3 data-id="heading-41">异步函数(Async functions)</h3>
<p>ES2017 标准引入了 <code>async</code> 函数，使得异步操作变得更加方便。</p>
<p><code>async</code> 函数是什么？一句话，它就是 <code>Generator</code> 函数的语法糖。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fakeRequest</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">"请求成功"</span>);
    &#125;, <span class="hljs-number">2000</span>);
  &#125;);
&#125;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getData</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"start"</span>);
  <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> fakeRequest();
  <span class="hljs-built_in">console</span>.log(res);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"end"</span>);
&#125;
getData();
<span class="hljs-comment">/*
1.start
2.请求成功
3.end
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-42">使用 Atomics 共享内存</h3>
<p><code>Atomics</code> 对象提供了一组静态方法对 <code>SharedArrayBuffer</code> 和 <code>ArrayBuffer</code> 对象进行原子操作。</p>
<p>更多详细内容参考<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Atomics" target="_blank" rel="nofollow noopener noreferrer">MDN-Atomics</a></p>
<hr>
<h2 data-id="heading-43">ES2016-ES7</h2>
<h3 data-id="heading-44">Array.prototype.includes</h3>
<p><code>Array.prototype.includes</code>方法返回一个布尔值，表示某个数组是否包含给定的值，与字符串的<code>includes</code>方法类似。</p>
<pre><code class="hljs language-ts copyable" lang="ts">[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
  .includes(<span class="hljs-number">2</span>) <span class="hljs-comment">// true</span>
  [(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>)].includes(<span class="hljs-number">4</span>) <span class="hljs-comment">// false</span>
  [(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-literal">NaN</span>)].includes(<span class="hljs-literal">NaN</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-45">求幂运算符(Exponentiation operator)</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 2的平方</span>
<span class="hljs-number">2</span> ** <span class="hljs-number">2</span>; <span class="hljs-comment">// 4</span>
<span class="hljs-comment">// 2的三次方</span>
<span class="hljs-number">2</span> ** <span class="hljs-number">3</span>; <span class="hljs-comment">// 8</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/number#%E6%8C%87%E6%95%B0%E8%BF%90%E7%AE%97%E7%AC%A6" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-指数运算符</a></p>
<hr>
<h2 data-id="heading-46">ES2015-ES6</h2>
<p>推荐阮一峰大佬的<a href="https://es6.ruanyifeng.com/" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程</a>,中文文档没有比他更详细的了</p>
<h3 data-id="heading-47">箭头函数(arrows)</h3>
<p>箭头函数是使用<code>=></code>语法的函数简写。与一般函数不同的是</p>
<ol>
<li>函数体内的<code>this</code>对象，就是定义时所在的对象，而不是使用时所在的对象。</li>
</ol>
<ul>
<li>this 对象的指向是可变的，但是在箭头函数中，它是固定的。</li>
</ul>
<ol start="2">
<li>不可以当作构造函数，也就是说，不可以使用<code>new</code>命令，否则会抛出一个错误。</li>
<li>不可以使用<code>arguments</code>对象，该对象在函数体内不存在。如果要用，可以用 <code>rest</code> 参数代替。</li>
<li>不可以使用<code>yield</code>命令，因此箭头函数不能用作 Generator 函数。</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">var</span> f = <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> v;

<span class="hljs-comment">// 等同于</span>
<span class="hljs-keyword">var</span> f = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">v</span>) </span>&#123;
  <span class="hljs-keyword">return</span> v;
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"id:"</span>, <span class="hljs-built_in">this</span>.id);
  &#125;, <span class="hljs-number">100</span>);
&#125;

<span class="hljs-keyword">var</span> id = <span class="hljs-number">21</span>;
<span class="hljs-comment">// 箭头函数导致this总是指向函数定义生效时所在的对象（&#123;id: 42&#125;），所以打印出来的是42</span>
foo.call(&#123; <span class="hljs-attr">id</span>: <span class="hljs-number">42</span> &#125;);
<span class="hljs-comment">// id: 42</span>

<span class="hljs-comment">// 对象不构成单独的作用域,使得this指向全局对象</span>
globalThis.s = <span class="hljs-number">21</span>;
<span class="hljs-keyword">const</span> obj = &#123;
  <span class="hljs-attr">s</span>: <span class="hljs-number">42</span>,
  <span class="hljs-attr">m</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.s),
&#125;;

obj.m(); <span class="hljs-comment">// 21</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/#docs/function#%E7%AE%AD%E5%A4%B4%E5%87%BD%E6%95%B0" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-箭头函数</a></p>
<h3 data-id="heading-48">类(Class)</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// ES5</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Point</span>(<span class="hljs-params">x, y</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.x = x;
  <span class="hljs-built_in">this</span>.y = y;
&#125;

Point.prototype.toString = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"("</span> + <span class="hljs-built_in">this</span>.x + <span class="hljs-string">", "</span> + <span class="hljs-built_in">this</span>.y + <span class="hljs-string">")"</span>;
&#125;;

<span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> Point(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);

<span class="hljs-comment">// ES6</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Point</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x, y</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.x = x;
    <span class="hljs-built_in">this</span>.y = y;
  &#125;

  <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">"("</span> + <span class="hljs-built_in">this</span>.x + <span class="hljs-string">", "</span> + <span class="hljs-built_in">this</span>.y + <span class="hljs-string">")"</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/#docs/class" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-Class</a></p>
<h3 data-id="heading-49">对象的扩展(enhanced object literals)</h3>
<h3 data-id="heading-50">对象的属性的简洁表示法</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> foo = <span class="hljs-string">"bar"</span>;
<span class="hljs-keyword">const</span> method = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello!"</span>;
&#125;;

<span class="hljs-keyword">const</span> filed = <span class="hljs-string">"name"</span>;

<span class="hljs-keyword">const</span> baz = &#123;
  foo,
  method,
  [filed]: <span class="hljs-string">"小王"</span>,
&#125;;

<span class="hljs-comment">// 等同于</span>
<span class="hljs-keyword">const</span> baz = &#123;
  <span class="hljs-attr">foo</span>: foo,
  <span class="hljs-attr">method</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello!"</span>;
  &#125;,
  <span class="hljs-attr">name</span>: <span class="hljs-string">"小王"</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/#docs/object#%E5%B1%9E%E6%80%A7%E7%9A%84%E7%AE%80%E6%B4%81%E8%A1%A8%E7%A4%BA%E6%B3%95" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-对象扩展</a></p>
<h3 data-id="heading-51">模板字符串</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 字符串中嵌入变量</span>
<span class="hljs-keyword">let</span> name = <span class="hljs-string">"Bob"</span>,
  time = <span class="hljs-string">"today"</span>;
<span class="hljs-string">`Hello <span class="hljs-subst">$&#123;name&#125;</span>, how are you <span class="hljs-subst">$&#123;time&#125;</span>?`</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/#docs/string#%E6%A8%A1%E6%9D%BF%E5%AD%97%E7%AC%A6%E4%B8%B2" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-字符串模板</a></p>
<h3 data-id="heading-52">数组解构+扩展运算符</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">var</span> [a] = [];

a === <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// true</span>

<span class="hljs-keyword">var</span> [a = <span class="hljs-number">1</span>] = [];
a === <span class="hljs-number">1</span>; <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/#docs/array#%E6%89%A9%E5%B1%95%E8%BF%90%E7%AE%97%E7%AC%A6" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-数组的扩展运算符</a></p>
<h3 data-id="heading-53">函数默认参数+剩余参数+扩展运算符</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//如果没有传递y 或者y===undefined ，则y=12</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">x, y = <span class="hljs-number">12</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> x + y;
&#125;
f(<span class="hljs-number">3</span>) == <span class="hljs-number">15</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">x, ...y</span>) </span>&#123;
  <span class="hljs-comment">// y 是一个数组</span>
  <span class="hljs-keyword">return</span> x * y.length;
&#125;
f(<span class="hljs-number">3</span>, <span class="hljs-string">"hello"</span>, <span class="hljs-literal">true</span>) == <span class="hljs-number">6</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">x, y, z</span>) </span>&#123;
  <span class="hljs-keyword">return</span> x + y + z;
&#125;
<span class="hljs-comment">// Pass each elem of array as argument</span>
f(...[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]) == <span class="hljs-number">6</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/#docs/function#%E4%B8%8E%E8%A7%A3%E6%9E%84%E8%B5%8B%E5%80%BC%E9%BB%98%E8%AE%A4%E5%80%BC%E7%BB%93%E5%90%88%E4%BD%BF%E7%94%A8" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-函数默认参数</a></p>
<h3 data-id="heading-54">块级作用域变量</h3>
<p>随着 ES6 中引入 <code>let/const</code> 关键字，JS 才具有函数作用域和全局作用域，现在 JS 也可以有块级作用域了。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
  &#123;
    <span class="hljs-keyword">let</span> x;
    &#123;
      <span class="hljs-comment">// 正常，因为在一个新的块级作用域中</span>
      <span class="hljs-keyword">const</span> x = <span class="hljs-string">"sneaky"</span>;
      <span class="hljs-comment">// const 定义的是常量无法被修改，因此会报错</span>
      x = <span class="hljs-string">"foo"</span>;
    &#125;
    <span class="hljs-comment">// 在块级作用域中已声明x,因此会报错</span>
    <span class="hljs-keyword">let</span> x = <span class="hljs-string">"inner"</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/#docs/let" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-unicode</a></p>
<h3 data-id="heading-55">遍历/迭代器+for..of(iterators + for..of)</h3>
<p>一个数据结构只要部署了 <code>Symbol.iterator</code> 属性，就被视为具有 iterator 接口，就可以用 <code>for...of</code> 循环遍历它的成员。也就是说，<code>for...of</code> 循环内部调用的是数据结构的 <code>Symbol.iterator</code> 方法。</p>
<p><code>for ... of</code>是<code>for ... in</code>和<code>forEach()</code>的替代方法，它循环访问可迭代的数据结构，如数组，映射，集合和字符串。</p>
<p>JavaScript 原有的 <code>for...in</code> 循环，只能获得对象的键名，不能直接获取键值。ES6 提供 <code>for...of</code> 循环，允许遍历获得键值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">"a"</span>, <span class="hljs-string">"b"</span>, <span class="hljs-string">"c"</span>, <span class="hljs-string">"d"</span>];

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> a <span class="hljs-keyword">in</span> arr) &#123;
  <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 0 1 2 3</span>
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> a <span class="hljs-keyword">of</span> arr) &#123;
  <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// a b c d</span>
&#125;

<span class="hljs-keyword">const</span> str = <span class="hljs-string">"helloworld"</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> a <span class="hljs-keyword">of</span> str) &#123;
  <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// h e l l o w o r l d</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/iterator" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-iterators</a></p>
<h3 data-id="heading-56">生成器(generators)</h3>
<p>Generators 使用<code>function *</code>和<code>yield</code>简化了迭代器的创建。 声明为<code>function *</code>的函数一个遍历器对象，也就是说，Generator 函数是一个遍历器对象生成函数。返回的遍历器对象，可以依次遍历 Generator 函数内部的每一个状态。</p>
<p>生成器是迭代器的子类型，因此具有<code>next</code>和<code>throw</code>方法。</p>
<p><code>yield</code>表达式是暂停执行的标记，而<code>next</code>方法可以恢复执行</p>
<p>注意：ES7 出现后,推荐使用<code>await</code>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">4</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">5</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-number">6</span>;
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> v <span class="hljs-keyword">of</span> foo()) &#123;
  <span class="hljs-built_in">console</span>.log(v);
&#125;
<span class="hljs-comment">// 1 2 3 4 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是一个利用 Generator 函数和<code>for...of</code>循环，实现斐波那契数列的例子。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">var</span> fibonacci = &#123;
  [<span class="hljs-built_in">Symbol</span>.iterator]: <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> [prev, curr] = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>];
    <span class="hljs-keyword">for</span> (;;) &#123;
      <span class="hljs-keyword">yield</span> curr;
      [prev, curr] = [curr, prev + curr];
    &#125;
  &#125;,
&#125;;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> n <span class="hljs-keyword">of</span> fibonacci) &#123;
  <span class="hljs-comment">//</span>
  <span class="hljs-keyword">if</span> (n > <span class="hljs-number">1000</span>) <span class="hljs-keyword">break</span>;
  <span class="hljs-built_in">console</span>.log(n);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面代码可见，使用<code>for...of</code>语句时不需要使用<code>next</code>方法。</p>
<p>利用<code>for...of</code>循环，可以写出遍历任意对象（object）的方法。原生的 JavaScript 对象没有迭代器接口，无法使用<code>for...of</code>循环，通过 Generator 函数为它加上这个接口，就可以用了。</p>
<p>生成器(Generator) 实质上继承了迭代器(Iterator)</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Generator <span class="hljs-keyword">extends</span> Iterator &#123;
  next(value?: <span class="hljs-built_in">any</span>): IteratorResult;
  <span class="hljs-keyword">throw</span>(exception: <span class="hljs-built_in">any</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/generator" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-iterators</a></p>
<h3 data-id="heading-57">Unicode</h3>
<p>ES6 增强了 Unicode 的功能,包括</p>
<ul>
<li>支持字符的 Unicode 表示法</li>
</ul>
<p>举例来说，“中”的 Unicode 码点是 <code>U+4e2d</code>，你可以直接在字符串里面输入这个汉字，也可以输入它的转义形式<code>\u4e2d</code>，两者是等价的。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-string">"中"</span> === <span class="hljs-string">"\u4e2d"</span>; <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用<code>/u</code>匹配码点的正则表达式</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// new RegExp behaviour, opt-in ‘u’</span>
<span class="hljs-string">"𠮷"</span>.match(<span class="hljs-regexp">/./u</span>)[<span class="hljs-number">0</span>].length == <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>获取 32 位的 UTF-16 字符的码点-<code>codePointAt</code></li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-string">"𠮷"</span>.codePointAt(<span class="hljs-number">0</span>) == <span class="hljs-number">0x20bb7</span>;

<span class="hljs-keyword">let</span> s = <span class="hljs-string">"𠮷a"</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> ch <span class="hljs-keyword">of</span> s) &#123;
  <span class="hljs-built_in">console</span>.log(ch.codePointAt(<span class="hljs-number">0</span>).toString(<span class="hljs-number">16</span>));
&#125;
<span class="hljs-comment">// 20bb7</span>
<span class="hljs-comment">// 61</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/#docs/string#%E5%AD%97%E7%AC%A6%E7%9A%84-Unicode-%E8%A1%A8%E7%A4%BA%E6%B3%95" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-unicode</a></p>
<h3 data-id="heading-58">模块化(modules)</h3>
<p>ES6 在语言标准的层面上，实现了模块功能，而且实现得相当简单，完全可以取代 CommonJS 和 AMD 规范，成为浏览器和服务器通用的模块解决方案。</p>
<p>使用 <code>export default</code> 或 <code>export</code> 进行导出</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// math.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> pi = <span class="hljs-number">3.141593</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">x, y</span>) </span>&#123;
  <span class="hljs-keyword">return</span> x + y;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>import</code> 进行导入</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// app.js</span>
<span class="hljs-keyword">import</span> sum, &#123; pi &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./math"</span>;

alert(<span class="hljs-string">"2π = "</span> + sum(pi, pi));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/module" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-module</a></p>
<h3 data-id="heading-59">模块加载器规则(module loaders)</h3>
<p>模块加载器支持:</p>
<ul>
<li>异步加载</li>
<li>代码是在模块作用域之中运行，而不是在全局作用域运行。模块内部的顶层变量，外部不可见。</li>
<li>模块之中，顶层的 <code>this</code> 关键字返回 undefined，而不是指向 <code>window</code>。也就是说，在模块顶层使用 <code>this</code> 关键字，是无意义的</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//index.js</span>
<span class="hljs-keyword">const</span> x = <span class="hljs-number">1</span>;

<span class="hljs-built_in">console</span>.log(x === <span class="hljs-built_in">window</span>.x); <span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span> === <span class="hljs-literal">undefined</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用顶层的 this 等于 undefined 这个语法点，可以侦测当前代码是否在 ES6 模块之中。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> isNotModuleScript = <span class="hljs-built_in">this</span> !== <span class="hljs-literal">undefined</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/module-loader" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-module-loader</a></p>
<p><code>import</code> and <code>export</code></p>
<h3 data-id="heading-60">Map + Set + Weakmap + Weakset</h3>
<p>ES6 提供了新的数据结构 <code>Set</code>。它类似于数组，但是成员的值都是唯一的，没有重复的值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// Sets</span>
<span class="hljs-keyword">var</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
s.add(<span class="hljs-string">"hello"</span>).add(<span class="hljs-string">"goodbye"</span>).add(<span class="hljs-string">"hello"</span>);
s.size === <span class="hljs-number">2</span>;
s.has(<span class="hljs-string">"hello"</span>) === <span class="hljs-literal">true</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES6 提供了 <code>Map</code> 数据结构。它类似于对象，也是键值对的集合，但是“键”的范围不限于字符串，各种类型的值（包括对象）都可以当作键。也就是说，Object 结构提供了“字符串—值”的对应，<code>Map</code> 结构提供了“值—值”的对应，是一种更完善的 Hash 结构实现。如果你需要“键值对”的数据结构，<code>Map</code> 比 Object 更合适。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// Maps</span>
<span class="hljs-keyword">var</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
m.set(<span class="hljs-string">"hello"</span>, <span class="hljs-number">42</span>);
m.set(s, <span class="hljs-number">34</span>);
m.get(s) == <span class="hljs-number">34</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>WeakMap</code> 结构与 <code>Map</code> 结构类似，也是用于生成键值对的集合。</p>
<p><code>WeakMap</code> 与 <code>Map</code> 的区别有两点。</p>
<ol>
<li>WeakMap 只接受对象作为键名（null 除外），不接受其他类型的值作为键名。</li>
<li>WeakMap 的键名所指向的对象，不计入垃圾回收机制。</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// Weak Maps</span>
<span class="hljs-keyword">var</span> wm = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();
wm.set(s, &#123; <span class="hljs-attr">extra</span>: <span class="hljs-number">42</span> &#125;);
wm.size === <span class="hljs-literal">undefined</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>WeakSet</code> 结构与 <code>Set</code> 类似，也是不重复的值的集合。但是，它与 <code>Set</code> 有两个区别。</p>
<ol>
<li>WeakSet 的成员只能是对象，而不能是其他类型的值。</li>
<li>WeakSet 中的对象都是弱引用</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// Weak Sets</span>
<span class="hljs-keyword">var</span> ws = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakSet</span>();
ws.add(&#123; <span class="hljs-attr">data</span>: <span class="hljs-number">42</span> &#125;);
<span class="hljs-comment">// Because the added object has no other references, it will not be held in the set</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/set-map" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-Set 和 Map</a></p>
<h3 data-id="heading-61">代理(proxies)</h3>
<p><code>Proxy</code> 用于修改某些操作的默认行为，等同于在语言层面做出修改。 可以用于操作拦截，日志记录/分析等。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 代理一个普通对象</span>
<span class="hljs-keyword">var</span> target = &#123;&#125;;
<span class="hljs-keyword">var</span> handler = &#123;
  <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">receiver, name</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`Hello, <span class="hljs-subst">$&#123;name&#125;</span>!`</span>;
  &#125;,
&#125;;

<span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);

<span class="hljs-comment">// true</span>
p.world === <span class="hljs-string">"Hello, world!"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是 <code>Proxy</code> 所有可以代理的"元操作"</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">var</span> handler =
&#123;
  <span class="hljs-attr">get</span>:...,
  <span class="hljs-attr">set</span>:...,
  <span class="hljs-attr">has</span>:...,
  <span class="hljs-attr">deleteProperty</span>:...,
  <span class="hljs-attr">apply</span>:...,
  <span class="hljs-attr">construct</span>:...,
  <span class="hljs-attr">getOwnPropertyDescriptor</span>:...,
  <span class="hljs-attr">defineProperty</span>:...,
  <span class="hljs-attr">getPrototypeOf</span>:...,
  <span class="hljs-attr">setPrototypeOf</span>:...,
  <span class="hljs-attr">enumerate</span>:...,
  <span class="hljs-attr">ownKeys</span>:...,
  <span class="hljs-attr">preventExtensions</span>:...,
  <span class="hljs-attr">isExtensible</span>:...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/get" target="_blank" rel="nofollow noopener noreferrer">MDN-handler.get()</a></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 代理一个函数对象</span>
<span class="hljs-keyword">var</span> target = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"I am the target"</span>;
&#125;;
<span class="hljs-keyword">var</span> handler = &#123;
  <span class="hljs-attr">apply</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">receiver, ...args</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">"I am the proxy"</span>;
  &#125;,
&#125;;

<span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, handler);
<span class="hljs-comment">//true</span>
p() === <span class="hljs-string">"I am the proxy"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/proxy" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-proxy</a></p>
<h3 data-id="heading-62">symbols</h3>
<p>ES6 引入了一种新的原始数据类型 <code>Symbol</code>，表示独一无二的值</p>
<p><code>Symbol</code> 值通过 Symbol 函数生成。这就是说，对象的属性名现在可以有两种类型，一种是原来就有的字符串，另一种就是新增的 <code>Symbol</code> 类型。凡是属性名属于 <code>Symbol</code> 类型，就都是独一无二的，可以保证不会与其他属性名产生冲突。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">var</span> MyClass = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">//</span>
  <span class="hljs-keyword">var</span> key = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"key"</span>);

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MyClass</span>(<span class="hljs-params">privateData</span>) </span>&#123;
    <span class="hljs-built_in">this</span>[key] = privateData;
  &#125;

  MyClass.prototype = &#123;
    <span class="hljs-attr">doStuff</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">this</span>[key];
    &#125;,
  &#125;;

  <span class="hljs-keyword">return</span> MyClass;
&#125;)();

<span class="hljs-keyword">var</span> c = <span class="hljs-keyword">new</span> MyClass(<span class="hljs-string">"hello"</span>);
<span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(c[<span class="hljs-string">"key"</span>] === <span class="hljs-literal">undefined</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建 <code>Symbol</code> 的时候，可以添加一个描述。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> sym = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"foo"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>sym</code> 的描述就是字符串 <code>foo</code>。</p>
<p><code>Symbol</code> 作为属性名，遍历对象的时候，该属性不会出现在 <code>for...in</code>、<code>for...of</code> 循环中，也不会被<code> Object.keys()</code>、<code>Object.getOwnPropertyNames()</code>、<code>JSON.stringify()</code>返回。</p>
<p>但是，它也不是私有属性，有一个 <code>Object.getOwnPropertySymbols()</code>方法，可以获取指定对象的所有 <code>Symbol</code> 属性名。该方法返回一个数组，成员是当前对象的所有用作属性名的 <code>Symbol</code> 值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> obj = &#123;&#125;;
<span class="hljs-keyword">let</span> a = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"a"</span>);
<span class="hljs-keyword">let</span> b = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"b"</span>);

obj[a] = <span class="hljs-string">"Hello"</span>;
obj[b] = <span class="hljs-string">"World"</span>;

<span class="hljs-keyword">const</span> objectSymbols = <span class="hljs-built_in">Object</span>.getOwnPropertySymbols(obj);

objectSymbols;
<span class="hljs-comment">// [Symbol(a), Symbol(b)]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/symbol" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-symbol</a></p>
<h3 data-id="heading-63">期约(promises)</h3>
<p><code>Promise</code> 是一个用于异步编程的库,里面保存着某个未来才会结束的事件（通常是一个异步操作）的结果。 许多现有的 JavaScript 库已经使用了 <code>Promise</code>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timeout</span>(<span class="hljs-params">duration = <span class="hljs-number">0</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(resolve, duration);
  &#125;);
&#125;

<span class="hljs-keyword">var</span> p = timeout(<span class="hljs-number">1000</span>)
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> timeout(<span class="hljs-number">2000</span>);
  &#125;)
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"hmm"</span>);
  &#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all([timeout(<span class="hljs-number">100</span>), timeout(<span class="hljs-number">200</span>)]);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/promise" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-promise</a></p>
<h3 data-id="heading-64">math + number + string + array + object APIs</h3>
<p>添加了许多类型的扩展方法,包括:<code>Math</code> ,<code>Array</code> ,<code>String</code> ,<code>Object</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">Number</span>.EPSILON;
<span class="hljs-built_in">Number</span>.isInteger(<span class="hljs-literal">Infinity</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Number</span>.isNaN(<span class="hljs-string">"NaN"</span>); <span class="hljs-comment">// false</span>

<span class="hljs-built_in">Math</span>.acosh(<span class="hljs-number">3</span>); <span class="hljs-comment">// 1.762747174039086</span>
<span class="hljs-built_in">Math</span>.hypot(<span class="hljs-number">3</span>, <span class="hljs-number">4</span>); <span class="hljs-comment">// 5</span>
<span class="hljs-built_in">Math</span>.imul(<span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">2</span>, <span class="hljs-number">32</span>) - <span class="hljs-number">1</span>, <span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">2</span>, <span class="hljs-number">32</span>) - <span class="hljs-number">2</span>); <span class="hljs-comment">// 2</span>

<span class="hljs-string">"abcde"</span>.includes(<span class="hljs-string">"cd"</span>); <span class="hljs-comment">// true</span>
<span class="hljs-string">"abc"</span>.repeat(<span class="hljs-number">3</span>); <span class="hljs-comment">// "abcabcabc"</span>

<span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">"*"</span>)); <span class="hljs-comment">// Returns a real Array</span>
<span class="hljs-built_in">Array</span>.of(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>) <span class="hljs-comment">// Similar to new Array(...), but without special one-arg behavior</span>
  [(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)].fill(<span class="hljs-number">7</span>, <span class="hljs-number">1</span>) <span class="hljs-comment">// [0,7,7]</span>
  [(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>)].find(<span class="hljs-function">(<span class="hljs-params">x</span>) =></span> x == <span class="hljs-number">3</span>) <span class="hljs-comment">// 3</span>
  [(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>)].findIndex(<span class="hljs-function">(<span class="hljs-params">x</span>) =></span> x == <span class="hljs-number">2</span>) <span class="hljs-comment">// 1</span>
  [(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>)].copyWithin(<span class="hljs-number">3</span>, <span class="hljs-number">0</span>) <span class="hljs-comment">// [1, 2, 3, 1, 2]</span>
  [(<span class="hljs-string">"a"</span>, <span class="hljs-string">"b"</span>, <span class="hljs-string">"c"</span>)].entries() <span class="hljs-comment">// iterator [0, "a"], [1,"b"], [2,"c"]</span>
  [(<span class="hljs-string">"a"</span>, <span class="hljs-string">"b"</span>, <span class="hljs-string">"c"</span>)].keys() <span class="hljs-comment">// iterator 0, 1, 2</span>
  [(<span class="hljs-string">"a"</span>, <span class="hljs-string">"b"</span>, <span class="hljs-string">"c"</span>)].values(); <span class="hljs-comment">// iterator "a", "b", "c"</span>

<span class="hljs-built_in">Object</span>.assign(Point, &#123; <span class="hljs-attr">origin</span>: <span class="hljs-keyword">new</span> Point(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>) &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考 ES 入门教程:</p>
<ul>
<li><a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/number" target="_blank" rel="nofollow noopener noreferrer">Number</a></li>
<li><a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/number#Math-%E5%AF%B9%E8%B1%A1%E7%9A%84%E6%89%A9%E5%B1%95" target="_blank" rel="nofollow noopener noreferrer">Math</a>,</li>
<li><a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/array#Array-from" target="_blank" rel="nofollow noopener noreferrer">Array.from</a></li>
<li><a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/array#Array-of" target="_blank" rel="nofollow noopener noreferrer">Array.of</a></li>
<li><a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/array#%E6%95%B0%E7%BB%84%E5%AE%9E%E4%BE%8B%E7%9A%84-copyWithin" target="_blank" rel="nofollow noopener noreferrer">Array.prototype.copyWithin</a></li>
<li><a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/object-methods#Object-assign" target="_blank" rel="nofollow noopener noreferrer">Object.assign</a></li>
</ul>
<h3 data-id="heading-65">二进制和八进制(binary and octal literals)</h3>
<p>两种新的数字表示形式。</p>
<ul>
<li>二进制: 0b 开头</li>
<li>八进制: 0o 开头</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-number">0b111110111</span> === <span class="hljs-number">503</span>; <span class="hljs-comment">// true</span>
<span class="hljs-number">0o767</span> === <span class="hljs-number">503</span>; <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-66">reflect api</h3>
<p>reflect API 公开对象上的运行时级别的<strong>元操作</strong>。</p>
<p>最重要的目的是配合 <code>Proxy</code> 使用，执行原生行为</p>
<p>让<code>Object</code>操作都变成函数行为。某些<code>Object</code>操作是命令式，比如<code>name in obj</code>和<code>delete obj[name]</code>，而<code>Reflect.has(obj, name)</code>和<code>Reflect.deleteProperty(obj, name)</code>让它们变成了函数行为。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 老写法</span>
<span class="hljs-string">"assign"</span> <span class="hljs-keyword">in</span> <span class="hljs-built_in">Object</span>; <span class="hljs-comment">// true</span>

<span class="hljs-comment">// 新写法</span>
<span class="hljs-built_in">Reflect</span>.has(<span class="hljs-built_in">Object</span>, <span class="hljs-string">"assign"</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/reflect" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-reflect</a></p>
<h3 data-id="heading-67">尾调用(tail calls)</h3>
<ul>
<li>尾调用:某个函数的最后一步是返回并调用另一个函数</li>
<li>尾递归:函数调用自身，称为递归。如果尾调用自身，就称为尾递归。</li>
<li><a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/function#%E5%B0%BE%E8%B0%83%E7%94%A8%E4%BC%98%E5%8C%96" target="_blank" rel="nofollow noopener noreferrer">尾调用优化</a></li>
</ul>
<p>注意，目前只有 Safari 浏览器支持尾调用优化，Chrome 和 Firefox 都不支持。这里就不深入研究了 😁</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">factorial</span>(<span class="hljs-params">n, acc = <span class="hljs-number">1</span></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (n <= <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> acc;
  <span class="hljs-keyword">return</span> factorial(n - <span class="hljs-number">1</span>, n * acc);
&#125;

<span class="hljs-comment">// 大多数浏览器中都会出现 堆栈溢出 的错误,</span>
<span class="hljs-comment">// 但是在 ES6的Safari中是安全的</span>
factorial(<span class="hljs-number">100000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多详细内容参考<a href="https://es6.ruanyifeng.com/?search=of&x=12&y=11#docs/function#%E4%BB%80%E4%B9%88%E6%98%AF%E5%B0%BE%E8%B0%83%E7%94%A8%EF%BC%9F" target="_blank" rel="nofollow noopener noreferrer">ES 入门教程-尾调用</a></p>
<h3 data-id="heading-68">通过 Intl API 对字符串，数字和日期进行国际化</h3>
<p><code>Intl</code> 对象是 ECMAScript 国际化 API 的命名空间，它提供对语言敏感的字符串比较、支持数字格式化以及日期和时间的格式化。</p>
<h3 data-id="heading-69">Intl.Collator 对象</h3>
<p>collator 这个单词意思是排序器。<code>Intl.Collator</code> 对象是排序器的构造函数，可以支持对语言敏感的字符串比较。</p>
<ul>
<li>中文排序</li>
</ul>
<p>如果我们希望我们的中文按照首字母拼音排序，该怎么处理？</p>
<p>此时，可以使用中文简体的 BCF 47 语言标记字符串 <code>zh</code> 进行排序，代码如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">var</span> arrUsername = [
  <span class="hljs-string">"陈坤"</span>,
  <span class="hljs-string">"邓超"</span>,
  <span class="hljs-string">"杜淳"</span>,
  <span class="hljs-string">"冯绍峰"</span>,
  <span class="hljs-string">"韩庚"</span>,
  <span class="hljs-string">"胡歌"</span>,
  <span class="hljs-string">"黄晓明"</span>,
  <span class="hljs-string">"贾乃亮"</span>,
  <span class="hljs-string">"李晨"</span>,
  <span class="hljs-string">"李易峰"</span>,
  <span class="hljs-string">"鹿晗"</span>,
  <span class="hljs-string">"井柏然"</span>,
  <span class="hljs-string">"刘烨"</span>,
  <span class="hljs-string">"陆毅"</span>,
  <span class="hljs-string">"孙红雷"</span>,
];

arrUsername.sort(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Intl</span>.Collator(<span class="hljs-string">"zh"</span>).compare);
<span class="hljs-comment">// 结果是：["陈坤", "邓超", "杜淳", "冯绍峰", "韩庚", "胡歌", "黄晓明", "贾乃亮", "井柏然", "李晨", "李易峰", "刘烨", "陆毅", "鹿晗", "孙红雷"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Intl API</code>详细可以参考这篇文章<a href="https://www.zhangxinxu.com/wordpress/2019/09/js-intl-zh/" target="_blank" rel="nofollow noopener noreferrer">JS Intl 对象完整简介及在中文中的应用</a></p>
<hr>
<h2 data-id="heading-70">ES2011-ES5</h2>
<p>相信大家已经对 ES5 都了然于胸，因此只做简单罗列，就不举例说明了</p>
<h3 data-id="heading-71">'USE STRICT'</h3>
<p>JS 的早期版本允许使用未声明的变量。 但是当使用 es5“严格使用”功能时，会报告错误</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// index.js</span>
<span class="hljs-meta">"use strict"</span>;

<span class="hljs-comment">// 报错:a is not defined</span>
a = <span class="hljs-number">22</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-72">Array</h3>
<h4 data-id="heading-73">Array.isArray</h4>
<h4 data-id="heading-74">Array.forEach</h4>
<h4 data-id="heading-75">Array.map</h4>
<h4 data-id="heading-76">Array.filter</h4>
<h4 data-id="heading-77">Array.reduce</h4>
<h4 data-id="heading-78">Array.reduceRight</h4>
<h4 data-id="heading-79">Array.every</h4>
<h4 data-id="heading-80">Array.some</h4>
<h4 data-id="heading-81">Array.indexOf</h4>
<h4 data-id="heading-82">Array.lastIndexOf</h4>
<h3 data-id="heading-83">JSON</h3>
<h4 data-id="heading-84">JSON.parse</h4>
<h4 data-id="heading-85">JSON.stringify</h4>
<h3 data-id="heading-86">DATE</h3>
<h4 data-id="heading-87">Date.now()</h4>
<h4 data-id="heading-88">Date.now().valueOf()</h4>
<h3 data-id="heading-89">Object.defineProperty()</h3>
<hr>
<h2 data-id="heading-90">参考文档</h2>
<ol>
<li><a href="https://github.com/lukehoban/es6features" target="_blank" rel="nofollow noopener noreferrer">ECMAScript 6 Features</a></li>
<li><a href="http://es6-features.org/#Constants" target="_blank" rel="nofollow noopener noreferrer">es6-features.org</a></li>
<li><a href="https://dev.to/carlillo/es2021-features-with-simple-examples-27d3" target="_blank" rel="nofollow noopener noreferrer">ES2021 Features with simple examples</a></li>
<li><a href="https://mp.weixin.qq.com/s/vZDunjbCnNqwDOaiflZlBw" target="_blank" rel="nofollow noopener noreferrer">4 个强大 JavaScript 运算符</a></li>
<li><a href="https://mp.weixin.qq.com/s/MghF85KhDPBSdaE1GXWjQg" target="_blank" rel="nofollow noopener noreferrer">ES6 核心特性</a></li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            