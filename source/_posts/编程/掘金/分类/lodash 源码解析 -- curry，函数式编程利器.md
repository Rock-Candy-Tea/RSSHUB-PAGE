
---
title: 'lodash 源码解析 -- curry，函数式编程利器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7691b057bd8492b81f5fb5ccc4014cb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 28 Mar 2021 01:54:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7691b057bd8492b81f5fb5ccc4014cb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>柯里化是函数式编程中不可或缺的一环，这个函数使得接受多参数的函数可以通过不影响结果的方式使其成为接受单参数的函数及其序列，根据这个特点可以合成出很多类似功能的函数，甚至是以自定义的顺序运行代码，达到复用代码的目的</p>
<p>lodash 中的 <code>curry</code> 函数因为处理了很多边界情况，这里有些我也不是很清楚。因此这次我只会分析基础的 <code>curry</code> 相关的代码，其余的部分不会详细说明，有一些不足欢迎在评论里补充</p>
<h1 data-id="heading-1">思路分析</h1>
<h3 data-id="heading-2">1. 流程图</h3>
<p><img alt="About curry.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7691b057bd8492b81f5fb5ccc4014cb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2. 简易的 <code>curry</code> 函数</h3>
<p>这里贴一个自己实现的简易的 <code>curry</code> 函数，以便理清思路。可以看到柯里化最主要的部分就是对函数进行包裹，在这个包裹内把参数存储起来，等到参数的数量足够再执行</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curry</span>(<span class="hljs-params">func, ...args1</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrapper</span> (<span class="hljs-params">...args2</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (args1.length + args2.length >= func.length) &#123;
            <span class="hljs-keyword">return</span> func.apply(<span class="hljs-literal">null</span>, [...args1, ...args2])
        &#125;
        <span class="hljs-keyword">return</span> curry(func, ...args1, ...args2)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">源码分析</h1>
<h3 data-id="heading-5">1. curry</h3>
<h5 data-id="heading-6">1. 传入参数</h5>
<ul>
<li><code>func</code> 函数</li>
<li><code>arity</code> 传入函数的参数</li>
<li><code>guard</code> 可以让 <code>curry</code> 成为可迭代的函数，用于 <code>_.map</code> 类似的函数</li>
</ul>
<h5 data-id="heading-7">2. 源码分析</h5>
<p><code>curry</code> 上的 <code>placeholder</code> 传入到 <code>result</code> 上，让 <code>result</code> 也可以使用 <code>placeholder</code>。这里的 <code>placehoder</code>  是 lodash 在外部手动设置的，可以通过传入 lodash 本身的变量，即 <code>_</code> 作为占位符</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curry</span>(<span class="hljs-params">func, arity, guard</span>) </span>&#123;
  arity = guard ? <span class="hljs-literal">undefined</span> : arity;
  <span class="hljs-keyword">var</span> result = createWrap(func, WRAP_CURRY_FLAG, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, arity);
  result.placeholder = curry.placeholder;
  <span class="hljs-keyword">return</span> result;
&#125;

<span class="hljs-comment">//...</span>
arrayEach([<span class="hljs-string">'bind'</span>, <span class="hljs-string">'bindKey'</span>, <span class="hljs-string">'curry'</span>, <span class="hljs-string">'curryRight'</span>, <span class="hljs-string">'partial'</span>, <span class="hljs-string">'partialRight'</span>], <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">methodName</span>) </span>&#123;
  lodash[methodName].placeholder = lodash;
&#125;);
<span class="hljs-comment">//...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2. createWrap</h3>
<h5 data-id="heading-9">1. 传入参数</h5>
<ul>
<li><code>func</code> 传入的被柯里化的函数</li>
<li><code>bitmask</code> 标志位</li>
<li><code>thisArg</code> 传递 <code>this</code> 指向</li>
<li><code>partials</code> 已经包含的参数</li>
<li><code>holders</code> 占位符</li>
<li><code>argPos</code> 参数的位置，<code>re-arg</code> 函数会用到</li>
<li><code>ary</code> 参数接收的数量，<code>ary</code> 函数会用到</li>
<li><code>arity</code> 后传入的参数</li>
</ul>
<h5 data-id="heading-10">2. 源码分析</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createWrap</span>(<span class="hljs-params">func, bitmask, thisArg, partials, holders, argPos, ary, arity</span>) </span>&#123;
  <span class="hljs-keyword">var</span> isBindKey = bitmask & WRAP_BIND_KEY_FLAG;
  <span class="hljs-keyword">if</span> (!isBindKey && <span class="hljs-keyword">typeof</span> func != <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(FUNC_ERROR_TEXT);
  &#125;
  <span class="hljs-keyword">var</span> length = partials ? partials.length : <span class="hljs-number">0</span>;
  <span class="hljs-keyword">if</span> (!length) &#123;
    bitmask &= ~(WRAP_PARTIAL_FLAG | WRAP_PARTIAL_RIGHT_FLAG);
    partials = holders = <span class="hljs-literal">undefined</span>;
  &#125;
  ary = ary === <span class="hljs-literal">undefined</span> ? ary : nativeMax(toInteger(ary), <span class="hljs-number">0</span>);
  arity = arity === <span class="hljs-literal">undefined</span> ? arity : toInteger(arity);
  length -= holders ? holders.length : <span class="hljs-number">0</span>;
  <span class="hljs-keyword">if</span> (bitmask & WRAP_PARTIAL_RIGHT_FLAG) &#123;
    <span class="hljs-keyword">var</span> partialsRight = partials,
        holdersRight = holders;
    partials = holders = <span class="hljs-literal">undefined</span>;
  &#125;
  <span class="hljs-keyword">var</span> data = isBindKey ? <span class="hljs-literal">undefined</span> : getData(func);
  <span class="hljs-keyword">var</span> newData = [
    func, bitmask, thisArg, partials, holders, partialsRight, holdersRight,
    argPos, ary, arity
  ];
  <span class="hljs-keyword">if</span> (data) &#123;
    mergeData(newData, data);
  &#125;
  func = newData[<span class="hljs-number">0</span>];
  bitmask = newData[<span class="hljs-number">1</span>];
  thisArg = newData[<span class="hljs-number">2</span>];
  partials = newData[<span class="hljs-number">3</span>];
  holders = newData[<span class="hljs-number">4</span>];
  arity = newData[<span class="hljs-number">9</span>] = newData[<span class="hljs-number">9</span>] === <span class="hljs-literal">undefined</span>
    ? (isBindKey ? <span class="hljs-number">0</span> : func.length)
  : nativeMax(newData[<span class="hljs-number">9</span>] - length, <span class="hljs-number">0</span>);
  <span class="hljs-keyword">if</span> (!arity && bitmask & (WRAP_CURRY_FLAG | WRAP_CURRY_RIGHT_FLAG)) &#123;
    bitmask &= ~(WRAP_CURRY_FLAG | WRAP_CURRY_RIGHT_FLAG);
  &#125;
  <span class="hljs-keyword">if</span> (!bitmask || bitmask == WRAP_BIND_FLAG) &#123;
    <span class="hljs-keyword">var</span> result = createBind(func, bitmask, thisArg);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (bitmask == WRAP_CURRY_FLAG || bitmask == WRAP_CURRY_RIGHT_FLAG) &#123;
    result = createCurry(func, bitmask, arity);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> ((bitmask == WRAP_PARTIAL_FLAG || bitmask == (WRAP_BIND_FLAG | WRAP_PARTIAL_FLAG)) && !holders.length) &#123;
    result = createPartial(func, bitmask, thisArg, partials);
  &#125; <span class="hljs-keyword">else</span> &#123;
    result = createHybrid.apply(<span class="hljs-literal">undefined</span>, newData);
  &#125;
  <span class="hljs-keyword">var</span> setter = data ? baseSetData : setData;
  <span class="hljs-keyword">return</span> setWrapToString(setter(result, newData), func, bitmask);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>检测 <code>createWrap</code> 是否是用于 <code>bind</code> 绑定函数</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">var</span> isBindKey = bitmask & WRAP_BIND_KEY_FLAG;
  <span class="hljs-keyword">if</span> (!isBindKey && <span class="hljs-keyword">typeof</span> func != <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(FUNC_ERROR_TEXT);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>partials</code> 为 <code>undefined</code>，<code>length</code> 置为 <code>0</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> length = partials ? partials.length : <span class="hljs-number">0</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 <code>length</code> 为 <code>0</code>，把 <code>partial</code> 和 <code>partialRight</code> 功能也关闭，同时 <code>holders</code> 和 <code>partials</code> 置为 <code>0</code>，<code>ary</code>、<code>arity</code> 和传入时保持一致</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (!length) &#123;
  bitmask &= ~(WRAP_PARTIAL_FLAG | WRAP_PARTIAL_RIGHT_FLAG);
  partials = holders = <span class="hljs-literal">undefined</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ary</code> 不变，<code>arity</code>  不变，<code>length</code> 置为 <code>0</code>（根据 <code>holders</code> 占位符的数量决定）</p>
<pre><code class="hljs language-js copyable" lang="js">ary = ary === <span class="hljs-literal">undefined</span> ? ary : nativeMax(toInteger(ary), <span class="hljs-number">0</span>);
arity = arity === <span class="hljs-literal">undefined</span> ? arity : toInteger(arity);
length -= holders ? holders.length : <span class="hljs-number">0</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>检测 是否使用 <code>partial</code> 的功能</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (bitmask & WRAP_PARTIAL_RIGHT_FLAG) &#123;
  <span class="hljs-keyword">var</span> partialsRight = partials,
      holdersRight = holders;
  partials = holders = <span class="hljs-literal">undefined</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>data</code> 置为 弱引用 <code>metaMap</code> 取 <code>func</code> 的 <code>value</code> 值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> data = isBindKey ? <span class="hljs-literal">undefined</span> : getData(func);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化 <code>newData</code>，<code>newData</code> 包含了被柯里化的函数，标志位，this 指针，绑定的参数，占位符，绑定的右起的参数，右起的占位符</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> newData = [
  func, bitmask, thisArg, partials, holders, partialsRight, holdersRight,
  argPos, ary, arity
];
<span class="hljs-keyword">if</span> (data) &#123;
  mergeData(newData, data);
&#125;
func = newData[<span class="hljs-number">0</span>];
bitmask = newData[<span class="hljs-number">1</span>];
thisArg = newData[<span class="hljs-number">2</span>];
partials = newData[<span class="hljs-number">3</span>];
holders = newData[<span class="hljs-number">4</span>];
arity = newData[<span class="hljs-number">9</span>] = newData[<span class="hljs-number">9</span>] === <span class="hljs-literal">undefined</span>
  ? (isBindKey ? <span class="hljs-number">0</span> : func.length)
: nativeMax(newData[<span class="hljs-number">9</span>] - length, <span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据 <code>bitmask</code> 使用对应的功能，这里使用的是 <code>WRAP_CURRY_FLAG</code></p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">if</span> (!arity && bitmask & (WRAP_CURRY_FLAG | WRAP_CURRY_RIGHT_FLAG)) &#123;
    bitmask &= ~(WRAP_CURRY_FLAG | WRAP_CURRY_RIGHT_FLAG);
  &#125;
  <span class="hljs-keyword">if</span> (!bitmask || bitmask == WRAP_BIND_FLAG) &#123;
    <span class="hljs-keyword">var</span> result = createBind(func, bitmask, thisArg);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (bitmask == WRAP_CURRY_FLAG || bitmask == WRAP_CURRY_RIGHT_FLAG) &#123;
    result = createCurry(func, bitmask, arity);
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> ((bitmask == WRAP_PARTIAL_FLAG || bitmask == (WRAP_BIND_FLAG | WRAP_PARTIAL_FLAG)) && !holders.length) &#123;
    result = createPartial(func, bitmask, thisArg, partials);
  &#125; <span class="hljs-keyword">else</span> &#123;
    result = createHybrid.apply(<span class="hljs-literal">undefined</span>, newData);
  &#125;
  <span class="hljs-keyword">var</span> setter = data ? baseSetData : setData;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置 <code>toString</code> 方法，对返回的函数的 <code>toString</code> 方法进行设置，设置为返回 原函数的 <code>+</code> 带有 <code>/* [wrapped with _.curry] */</code> 标识的字符串</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">return</span> setWrapToString(setter(result, newData), func, bitmask);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3. creatCurry</h3>
<h5 data-id="heading-12">1. 传入参数</h5>
<ul>
<li><code>func</code> 传入的被柯里化的函数</li>
<li><code>bitmask</code> 标志位</li>
<li><code>arity</code> 传入给 <code>createCurry</code> 的需要绑定的参数</li>
</ul>
<h5 data-id="heading-13">2. 源码分析</h5>
<p>过滤 <code>placeholder</code>，同时返回柯里化的函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createCurry</span>(<span class="hljs-params">func, bitmask, arity</span>) </span>&#123;
  <span class="hljs-keyword">var</span> Ctor = createCtor(func);
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrapper</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> length = <span class="hljs-built_in">arguments</span>.length,
        args = <span class="hljs-built_in">Array</span>(length),
        index = length,
        placeholder = getHolder(wrapper);
    <span class="hljs-keyword">while</span> (index--) &#123;
      args[index] = <span class="hljs-built_in">arguments</span>[index];
    &#125;
    <span class="hljs-keyword">var</span> holders = (length < <span class="hljs-number">3</span> && args[<span class="hljs-number">0</span>] !== placeholder && args[length - <span class="hljs-number">1</span>] !== placeholder)
    ? []
    : replaceHolders(args, placeholder);
    length -= holders.length;
    <span class="hljs-keyword">if</span> (length < arity) &#123;
      <span class="hljs-keyword">return</span> createRecurry(
        func, bitmask, createHybrid, wrapper.placeholder, <span class="hljs-literal">undefined</span>,
        args, holders, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, arity - length);
    &#125;
    <span class="hljs-keyword">var</span> fn = (<span class="hljs-built_in">this</span> && <span class="hljs-built_in">this</span> !== root && <span class="hljs-built_in">this</span> <span class="hljs-keyword">instanceof</span> wrapper) ? Ctor : func;
    <span class="hljs-keyword">return</span> apply(fn, <span class="hljs-built_in">this</span>, args);
  &#125;
  <span class="hljs-keyword">return</span> wrapper;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提取 <code>func</code> 作为构造函数，如果柯里化的是构造函数，也可以保证其正常接收参数并返回</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">var</span> Ctor = createCtor(func);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化，获取 <code>placeholder</code>，这里的 <code>placeholder</code> 可以是 lodash 默认的，也可以是在 <code>wrapper</code> 上设置的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> length = <span class="hljs-built_in">arguments</span>.length,
    args = <span class="hljs-built_in">Array</span>(length),
    index = length,
    placeholder = getHolder(wrapper);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果传入参数小于函数参数 <code>arity</code>，调用 <code>createRecurry</code>，返回新的函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (length < arity) &#123;
  <span class="hljs-keyword">return</span> createRecurry(
    func, bitmask, createHybrid, wrapper.placeholder, <span class="hljs-literal">undefined</span>,
    args, holders, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>, arity - length);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数大于等于 <code>arity</code> ，传入参数返回函数调用结果，这里检测是否是构造函数，只要参数足够，柯里化的函数也可以作为构造函数使用，如果不是构造函数就正常返回调用值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fn = (<span class="hljs-built_in">this</span> && <span class="hljs-built_in">this</span> !== root && <span class="hljs-built_in">this</span> <span class="hljs-keyword">instanceof</span> wrapper) ? Ctor : func;
    <span class="hljs-keyword">return</span> apply(fn, <span class="hljs-built_in">this</span>, args);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">4. createRecurry</h3>
<h5 data-id="heading-15">1. 传入参数</h5>
<p>类似 <code>creatCurry</code></p>
<h5 data-id="heading-16">2. 源码分析</h5>
<p><code>wrapper</code> 函数会调用 <code>createRecurry</code> 最终处理绑定的参数和 懒加载 等情况，然后交给 <code>createHybrid</code> 返回新函数或是返回结果</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRecurry</span>(<span class="hljs-params">func, bitmask, wrapFunc, placeholder, thisArg, partials, holders, argPos, ary, arity</span>) </span>&#123;
  <span class="hljs-comment">// 根据 bitmask 和 isCurry 标志位，设置 holders 、 partials 等参数</span>
  <span class="hljs-keyword">var</span> isCurry = bitmask & WRAP_CURRY_FLAG,
      newHolders = isCurry ? holders : <span class="hljs-literal">undefined</span>,
      newHoldersRight = isCurry ? <span class="hljs-literal">undefined</span> : holders,
      newPartials = isCurry ? partials : <span class="hljs-literal">undefined</span>,
      newPartialsRight = isCurry ? <span class="hljs-literal">undefined</span> : partials;
  bitmask |= (isCurry ? WRAP_PARTIAL_FLAG : WRAP_PARTIAL_RIGHT_FLAG);
  bitmask &= ~(isCurry ? WRAP_PARTIAL_RIGHT_FLAG : WRAP_PARTIAL_FLAG);
  <span class="hljs-comment">// 清除 bind 标志位</span>
  <span class="hljs-keyword">if</span> (!(bitmask & WRAP_CURRY_BOUND_FLAG)) &#123;
    bitmask &= ~(WRAP_BIND_FLAG | WRAP_BIND_KEY_FLAG);
  &#125;
  <span class="hljs-keyword">var</span> newData = [
    func, bitmask, thisArg, newPartials, newHolders, newPartialsRight,
    newHoldersRight, argPos, ary, arity
  ];
    <span class="hljs-comment">// 调用 createHybird，借用这个函数的能力返回一个新函数</span>
  <span class="hljs-keyword">var</span> result = wrapFunc.apply(<span class="hljs-literal">undefined</span>, newData);
  <span class="hljs-keyword">if</span> (isLaziable(func)) &#123;
    setData(result, newData);
  &#125;
  <span class="hljs-comment">// 设置 placeholder</span>
  result.placeholder = placeholder;
  <span class="hljs-comment">// 同样的，将 toString 设置为返回 原函数的 + 带有 /* [wrapped with _.curry] */ 标识的字符串</span>
  <span class="hljs-keyword">return</span> setWrapToString(result, func, bitmask);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">5. createHybrid</h3>
<h5 data-id="heading-18">1. 传入参数</h5>
<p>类似 <code>createCurry</code></p>
<h5 data-id="heading-19">2. 源码分析</h5>
<p>主要作用就是返回 <code>wrapper</code> ，类似于 <code>createCurry</code>，返回一个 <code>wrapper</code> 函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createHybrid</span>(<span class="hljs-params">func, bitmask, thisArg, partials, holders, partialsRight, holdersRight, argPos, ary, arity</span>) </span>&#123;
  
  <span class="hljs-keyword">var</span> isAry = bitmask & WRAP_ARY_FLAG,
      isBind = bitmask & WRAP_BIND_FLAG,
      isBindKey = bitmask & WRAP_BIND_KEY_FLAG,
      isCurried = bitmask & (WRAP_CURRY_FLAG | WRAP_CURRY_RIGHT_FLAG),
      isFlip = bitmask & WRAP_FLIP_FLAG,
      Ctor = isBindKey ? <span class="hljs-literal">undefined</span> : createCtor(func);
    
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrapper</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> length = <span class="hljs-built_in">arguments</span>.length,
        args = <span class="hljs-built_in">Array</span>(length),
        index = length;
    <span class="hljs-keyword">while</span> (index--) &#123;
      args[index] = <span class="hljs-built_in">arguments</span>[index];
    &#125;
    <span class="hljs-keyword">if</span> (isCurried) &#123;
      <span class="hljs-keyword">var</span> placeholder = getHolder(wrapper),
          holdersCount = countHolders(args, placeholder);
    &#125;
    <span class="hljs-keyword">if</span> (partials) &#123;
      args = composeArgs(args, partials, holders, isCurried);
    &#125;
    <span class="hljs-keyword">if</span> (partialsRight) &#123;
      args = composeArgsRight(args, partialsRight, holdersRight, isCurried);
    &#125;
    length -= holdersCount;
    <span class="hljs-keyword">if</span> (isCurried && length < arity) &#123;
      <span class="hljs-keyword">var</span> newHolders = replaceHolders(args, placeholder);
      <span class="hljs-keyword">return</span> createRecurry(
        func, bitmask, createHybrid, wrapper.placeholder, thisArg,
        args, newHolders, argPos, ary, arity - length
      );
    &#125;
    <span class="hljs-keyword">var</span> thisBinding = isBind ? thisArg : <span class="hljs-built_in">this</span>,
        fn = isBindKey ? thisBinding[func] : func;
    length = args.length;
    <span class="hljs-keyword">if</span> (argPos) &#123;
      args = reorder(args, argPos);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isFlip && length > <span class="hljs-number">1</span>) &#123;
      args.reverse();
    &#125;
    <span class="hljs-keyword">if</span> (isAry && ary < length) &#123;
      args.length = ary;
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span> && <span class="hljs-built_in">this</span> !== root && <span class="hljs-built_in">this</span> <span class="hljs-keyword">instanceof</span> wrapper) &#123;
      fn = Ctor || createCtor(fn);
    &#125;
    <span class="hljs-keyword">return</span> fn.apply(thisBinding, args);
  &#125;
  <span class="hljs-keyword">return</span> wrapper;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 <code>wrapper</code> 其实类似上面的 <code>createCurry</code>，增加了绑定之前参数的代码</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrapper</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> length = <span class="hljs-built_in">arguments</span>.length,
        args = <span class="hljs-built_in">Array</span>(length),
        index = length;
    <span class="hljs-keyword">while</span> (index--) &#123;
      args[index] = <span class="hljs-built_in">arguments</span>[index];
    &#125;
    <span class="hljs-keyword">if</span> (isCurried) &#123;
      <span class="hljs-keyword">var</span> placeholder = getHolder(wrapper),
          holdersCount = countHolders(args, placeholder);
    &#125;
    <span class="hljs-keyword">if</span> (partials) &#123;
      args = composeArgs(args, partials, holders, isCurried);
    &#125;
    <span class="hljs-keyword">if</span> (partialsRight) &#123;
      args = composeArgsRight(args, partialsRight, holdersRight, isCurried);
    &#125;
    length -= holdersCount;
    <span class="hljs-keyword">if</span> (isCurried && length < arity) &#123;
      <span class="hljs-keyword">var</span> newHolders = replaceHolders(args, placeholder);
      <span class="hljs-keyword">return</span> createRecurry(
        func, bitmask, createHybrid, wrapper.placeholder, thisArg,
        args, newHolders, argPos, ary, arity - length
      );
    &#125;
    <span class="hljs-keyword">var</span> thisBinding = isBind ? thisArg : <span class="hljs-built_in">this</span>,
        fn = isBindKey ? thisBinding[func] : func;
    length = args.length;
    <span class="hljs-comment">//......</span>
    
    <span class="hljs-keyword">if</span> (isAry && ary < length) &#123;
      args.length = ary;
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span> && <span class="hljs-built_in">this</span> !== root && <span class="hljs-built_in">this</span> <span class="hljs-keyword">instanceof</span> wrapper) &#123;
      fn = Ctor || createCtor(fn);
    &#125;
    <span class="hljs-keyword">return</span> fn.apply(thisBinding, args);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-20">应用场景</h1>
<p><code>curry</code> 函数可以包裹现有的函数，用于复用函数，比如一个 add 函数，可以通过柯里化的方式包裹，形成了新的函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> add =_.curry(add)
<span class="hljs-keyword">let</span> add10 = add(<span class="hljs-number">10</span>)
<span class="hljs-keyword">let</span> add100 = add(<span class="hljs-number">100</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-21">总结</h1>
<p>柯里化的实现，用到了 JS 的闭包特性，存储了传入的参数，闭包通常指的是自带执行环境的函数。</p>
<p>柯里化虽然提升了代码的复用率，但也有问题，比如对执行逻辑的复杂化，比如在内存中产生了很多闭包</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            