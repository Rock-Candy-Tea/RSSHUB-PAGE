
---
title: 'JS 基础 -- Iterator & Generator'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8021'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 23:40:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=8021'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Iterator 迭代器</h1>
<h2 data-id="heading-1">定义</h2>
<p>迭代器是一个特殊对象，每个迭代器都有一个 next() 方法，每次调用都返回一个结果对象；结果对象有两个属性：一个是 value 表示当前迭代返回的值，另一个是 done 表示迭代是否完成。</p>
<h3 data-id="heading-2">ES5 实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createIterator</span>(<span class="hljs-params">items</span>) </span>&#123;
  <span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>;

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">next</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">var</span> done = i >= items.length;
      <span class="hljs-keyword">var</span> value = done ? <span class="hljs-literal">undefined</span> : items[i++];

      <span class="hljs-keyword">return</span> &#123; value, done &#125;;
    &#125;
  &#125;;
&#125;

<span class="hljs-keyword">const</span> iterator = createIterator([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]);
iterator.next(); <span class="hljs-comment">// &#123;value: 1, done: false&#125;</span>
iterator.next(); <span class="hljs-comment">// &#123;value: 2, done: false&#125;</span>
iterator.next(); <span class="hljs-comment">// &#123;value: 3, done: false&#125;</span>
iterator.next(); <span class="hljs-comment">// &#123;value: undefined, done: true&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fjs-base-fn-g0uo3%3Ffile%3D%2Fsrc%2FES6%2Fiterator.js%3A0-210" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/js-base-fn-g0uo3?file=/src/ES6/iterator.js:0-210" ref="nofollow noopener noreferrer">js-base-fn</a></p>
<h1 data-id="heading-3">Generator 生成器</h1>
<h2 data-id="heading-4">定义</h2>
<p>生成器是返回迭代器的函数</p>
<h2 data-id="heading-5">使用</h2>
<p>ES6 支持通过 * 与 yield 关键字实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 声明</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">createItrator</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
<span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
<span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>;
&#125;

<span class="hljs-comment">// 表达式</span>
<span class="hljs-keyword">const</span> createIterator = <span class="hljs-function"><span class="hljs-keyword">function</span> *(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
<span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
<span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>;
&#125;

<span class="hljs-keyword">const</span> iterator = createIterator();
iterator.next(); <span class="hljs-comment">// &#123;value: 1, done: false&#125;</span>
iterator.next(); <span class="hljs-comment">// &#123;value: 2, done: false&#125;</span>
iterator.next(); <span class="hljs-comment">// &#123;value: 3, done: false&#125;</span>
iterator.next(); <span class="hljs-comment">// &#123;value: undefined, done: true&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>yield 通过它来指定调用迭代器的 next() 方法时的返回值及返回顺序。</li>
<li>每执行一条 yield 语句之后函数就会停止执行，直到再次调用迭代器的 next() 方法</li>
</ul>
<h3 data-id="heading-6">yield 的使用限制</h3>
<p>yield 只可以在生成器的内部使用，否则会会抛出错误，即便是生成器内部的函数里使用也是如此；</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">createIterator</span>(<span class="hljs-params">items</span>) </span>&#123;
items.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">yield</span> item + <span class="hljs-number">1</span>; <span class="hljs-comment">// 在内部函数中使用，导致语法错误</span>
&#125;)
&#125;
<span class="hljs-comment">// Uncaught SyntaxError: Unexpected identifier</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>yield 与 return 关键字一样，二者都不能穿透函数边界。</p>
<h3 data-id="heading-7">生成器对象的方法</h3>
<p>ES6 函数方法的简写</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> o = &#123;
*<span class="hljs-function"><span class="hljs-title">createIterator</span>(<span class="hljs-params">items</span>)</span> &#123;
items.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">yield</span> item + <span class="hljs-number">1</span>; <span class="hljs-comment">// 语法错误</span>
&#125;)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">可迭代对象和 for-of 循环</h2>
<p>可迭代对象具有 Symbol.iterator 属性，Symbol.iterator 通过指定的函数返回一个作用域附属对象的迭代器。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> num <span class="hljs-keyword">of</span> arr) &#123;
<span class="hljs-built_in">console</span>.log(num);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>for-of 循环代码通过调用 values 数组的 Symbol.iterator 方法来获取迭代器，随后迭代器的 next() 方法被多次调用，从其对象的 value 属性读取值并存储在变量 num 中</p>
<h3 data-id="heading-9">访问默认迭代器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> values = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">let</span> iterator = values[<span class="hljs-built_in">Symbol</span>.iterator]();

<span class="hljs-built_in">console</span>.log(iterator.next()); <span class="hljs-comment">// &#123;value: 1, done: false&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>判断是否为可迭代对象</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isIterable</span>(<span class="hljs-params">object</span>) </span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> object[<span class="hljs-built_in">Symbol</span>.iterator] === <span class="hljs-string">'function'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">创建可迭代对象</h3>
<p>默认情况下，开发者定义的对象都是不可迭代对象，但如果给 Symbol.iterator 属性添加一个生成器，则可以将其变为可迭代对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> collection  = &#123;
<span class="hljs-attr">items</span>: [],
*[<span class="hljs-built_in">Symbol</span>.iterator]() &#123;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.items) &#123;
<span class="hljs-keyword">yield</span> item;
&#125;
&#125;
&#125;

collection.item.push(<span class="hljs-number">1</span>);
collection.item.push(<span class="hljs-number">2</span>);
collection.item.push(<span class="hljs-number">3</span>);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> x <span class="hljs-keyword">of</span> collection) &#123;
<span class="hljs-built_in">console</span>.log(x);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            