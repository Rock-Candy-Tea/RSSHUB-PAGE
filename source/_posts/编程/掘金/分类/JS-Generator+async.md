
---
title: 'JS-Generator+async'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4634'
author: 掘金
comments: false
date: Thu, 13 May 2021 23:00:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=4634'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">什么是Generator</h1>
<p><code>Generator</code> 函数是 ES6 提供的一种异步编程解决方案，语法行为与传统函数完全不同。<br>
<code>Generator</code> 函数有多种理解角度。语法上，首先可以把它理解成，Generator 函数是一个状态机，封装了多个内部状态。<br>
形式上，<code>Generator</code> 函数是一个普通函数，但是有两个特征。一是，<code>function</code>关键字与函数名之间有一个星号；二是，函数体内部使用<code>yield</code>表达式，定义不同的内部状态（<code>yield</code>在英语里的意思就是“产出”）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">helloWorldGenerator</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'hello'</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">'world'</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-string">'ending'</span>;
&#125;

<span class="hljs-keyword">var</span> hw = helloWorldGenerator();
hw.next()
<span class="hljs-comment">// &#123; value: 'hello', done: false &#125;</span>

hw.next()
<span class="hljs-comment">// &#123; value: 'world', done: false &#125;</span>

hw.next()
<span class="hljs-comment">// &#123; value: 'ending', done: true &#125;</span>

hw.next()
<span class="hljs-comment">// &#123; value: undefined, done: true &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>这里需要补充一下遍历器对象（Iterator Object）</code></p>
<h2 data-id="heading-1">Iterator</h2>
<p><code>Iterator</code> 的遍历过程是这样的。</p>
<p>（1）创建一个指针对象，指向当前数据结构的起始位置。也就是说，遍历器对象本质上，就是一个指针对象。</p>
<p>（2）第一次调用指针对象的<code>next</code>方法，可以将指针指向数据结构的第一个成员。</p>
<p>（3）第二次调用指针对象的<code>next</code>方法，指针就指向数据结构的第二个成员。</p>
<p>（4）不断调用指针对象的<code>next</code>方法，直到它指向数据结构的结束位置。<br>
<code>next</code>方法返回一个对象，表示当前数据成员的信息。这个对象具有<code>value</code>和<code>done</code>两个属性，<code>value</code>属性返回当前位置的成员，<code>done</code>属性是一个布尔值，表示遍历是否结束，即是否还有必要再一次调用<code>next</code>方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeIterator</span>(<span class="hljs-params">array</span>) </span>&#123;
  <span class="hljs-keyword">var</span> nextIndex = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">next</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> nextIndex < array.length ?
        &#123;<span class="hljs-attr">value</span>: array[nextIndex++]&#125; :
        &#123;<span class="hljs-attr">done</span>: <span class="hljs-literal">true</span>&#125;;
    &#125;
  &#125;;
&#125;;
<span class="hljs-keyword">var</span> it = makeIterator([<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>]);
it.next() <span class="hljs-comment">// &#123; value: "a", done: false &#125;</span>
it.next() <span class="hljs-comment">// &#123; value: "b", done: false &#125;</span>
it.next() <span class="hljs-comment">// &#123; value: undefined, done: true &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES6 的有些数据结构原生具备 <code>Iterator</code> 接口（比如数组），即不用任何处理，就可以被<code>for...of</code>循环遍历。原因在于，这些数据结构原生部署了<code>Symbol.iterator</code>属性，另外一些数据结构没有（比如对象）。凡是部署了<code>Symbol.iterator</code>属性的数据结构，就称为部署了遍历器接口。调用这个接口，就会返回一个遍历器对象。<br>
原生具备 Iterator 接口的数据结构如下：</p>
<ul>
<li>Array</li>
<li>Map</li>
<li>Set</li>
<li>String</li>
<li>TypedArray</li>
<li>函数的 arguments 对象</li>
<li>NodeList 对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>];
<span class="hljs-keyword">let</span> iter = arr[<span class="hljs-built_in">Symbol</span>.iterator]();

iter.next() <span class="hljs-comment">// &#123; value: 'a', done: false &#125;</span>
iter.next() <span class="hljs-comment">// &#123; value: 'b', done: false &#125;</span>
iter.next() <span class="hljs-comment">// &#123; value: 'c', done: false &#125;</span>
iter.next() <span class="hljs-comment">// &#123; value: undefined, done: true &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">next 方法的参数</h2>
<p>yield表达式本身没有返回值，或者说总是返回undefined。next方法可以带一个参数，该参数就会被当作上一个yield表达式的返回值。<br>
<code>yield表达式如果用在另一个表达式之中，必须放在圆括号里面;yield表达式用作函数参数或放在赋值表达式的右边，可以不加括号。</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">foo</span>(<span class="hljs-params">x</span>) </span>&#123;
  <span class="hljs-keyword">var</span> y = <span class="hljs-number">2</span> * (<span class="hljs-keyword">yield</span> (x + <span class="hljs-number">1</span>));
  <span class="hljs-keyword">var</span> z = <span class="hljs-keyword">yield</span> (y / <span class="hljs-number">3</span>);
  <span class="hljs-keyword">return</span> (x + y + z);
&#125;

<span class="hljs-keyword">var</span> a = foo(<span class="hljs-number">5</span>);
a.next() <span class="hljs-comment">// Object&#123;value:6, done:false&#125;</span>
a.next() <span class="hljs-comment">// Object&#123;value:NaN, done:false&#125;</span>
a.next() <span class="hljs-comment">// Object&#123;value:NaN, done:true&#125;</span>

<span class="hljs-keyword">var</span> b = foo(<span class="hljs-number">5</span>);                                 <span class="hljs-comment">// 带参 x=5</span>
b.next() <span class="hljs-comment">// &#123; value:6, done:false &#125;             // yield (x + 1) x+1 = 5+1</span>
b.next(<span class="hljs-number">12</span>) <span class="hljs-comment">// &#123; value:8, done:false &#125;           // 带参 （yield (x + 1)）= 12</span>
b.next(<span class="hljs-number">13</span>) <span class="hljs-comment">// &#123; value:42, done:true &#125;           // 带参 （yield (y / 3)）= 13</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">for...of 循环</h2>
<p>下面代码使用for...of循环，依次显示 5 个yield表达式的值。这里需要注意，一旦next方法的返回对象的done属性为true，for...of循环就会中止，且不包含该返回对象，所以上面代码的return语句返回的6，不包括在for...of循环之中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
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
<h3 data-id="heading-4">注意：</h3>
<p><code>next()</code>是对应<code>yield</code>后面表达式的，如果在<code>for...of</code>后在使用已经没有对应的yield了，所以会<code>&#123; value: undefined, done: true &#125;</code>，但是先<code>next()</code>再<code>for...of</code>就只会根据剩余<code>yield</code>做显示</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>, [[<span class="hljs-number">2</span>, <span class="hljs-number">3</span>], <span class="hljs-number">4</span>], [<span class="hljs-number">5</span>, <span class="hljs-number">6</span>]];

<span class="hljs-keyword">var</span> flat = <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params">a</span>) </span>&#123;
  <span class="hljs-keyword">var</span> length = a.length;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
    <span class="hljs-keyword">var</span> item = a[i];
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> item !== <span class="hljs-string">'number'</span>) &#123;
      <span class="hljs-keyword">yield</span>* flat(item);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">yield</span> item;
    &#125;
  &#125;
&#125;;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> f <span class="hljs-keyword">of</span> flat(arr)) &#123;
  <span class="hljs-built_in">console</span>.log(f);
&#125;;
<span class="hljs-comment">// 1 2 3 4 5 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">next()在for...of后</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arrs = flat(arr);
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> f <span class="hljs-keyword">of</span> arrs) &#123;
  <span class="hljs-built_in">console</span>.log(f);
&#125;; 
<span class="hljs-built_in">console</span>.log(arrs.next());
<span class="hljs-comment">// 1 2 3 4 5 6 &#123; value: undefined, done: true &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">next()在for...of前</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arrs = flat(arr);
<span class="hljs-built_in">console</span>.log(arrs.next());
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> f <span class="hljs-keyword">of</span> arrs) &#123;
  <span class="hljs-built_in">console</span>.log(f);
&#125;; 
<span class="hljs-comment">// &#123; value:1, done: false &#125; 2 3 4 5 6 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">斐波那契数列</h2>
<p>斐波那契数列（Fibonacci sequence），又称黄金分割数列，因数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……在数学上，斐波那契数列以如下被以递推的方法定义：F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2，n ∈ N*）</p>
<h3 data-id="heading-8">数组</h3>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">list</span>(<span class="hljs-params">max</span>)</span>&#123;
 <span class="hljs-keyword">let</span> arr = [];
 <span class="hljs-keyword">let</span> a = <span class="hljs-number">0</span>;
 <span class="hljs-keyword">let</span> b = <span class="hljs-number">1</span>;
 <span class="hljs-keyword">while</span>(arr.length<max)&#123;
 arr.push(a);
 [a,b] = [b,a+b];
 &#125; 
 <span class="hljs-keyword">return</span> arr;
 &#125;
 <span class="hljs-built_in">console</span>.log(list(<span class="hljs-number">5</span>));<span class="hljs-comment">// [0,1,1,2,3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">generator函数</h3>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">list</span>(<span class="hljs-params">max</span>)</span>&#123;
<span class="hljs-keyword">let</span> a = <span class="hljs-number">0</span>;
<span class="hljs-keyword">let</span> b = <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> n = <span class="hljs-number">0</span>;
<span class="hljs-keyword">while</span>(n<max)&#123;
  <span class="hljs-keyword">yield</span> a;
  [a,b] = [b,a+b];
  n++;
&#125;;
<span class="hljs-keyword">return</span>;
  &#125;;
  <span class="hljs-keyword">var</span> arr = list(<span class="hljs-number">5</span>);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> arr) &#123;
  <span class="hljs-built_in">console</span>.log(item);
  &#125;
<span class="hljs-comment">// 0 1 1 2 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">思考</h2>
<blockquote>
<p>Generator函数好在哪里？回归本质：函数是 ES6 提供的一种异步编程解决方案。
由斐波那契数列为例，普通构造函数跟Generator函数都能实现业务，但是区别在于：普通函数返回的>是数组；Generator函数是从上而下一步一步执行的用next()方法就会很明显。</p>
</blockquote>
<h3 data-id="heading-11">异步是什么</h3>
<p>异步的概念就是一步一步去执行，上一个事件执行完成了，下一个事件才会执行，可以对比一下if条件，异步的判断条件就是上一个事件是否执行完成。</p>
<h3 data-id="heading-12">异步编程的实现：回调函数</h3>
<p>JavaScript 语言对异步编程的实现，就是回调函数。所谓回调函数，就是把任务的第二段单独写在一个函数里面，等到重新执行这个任务的时候，就直接调用这个函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
fs.readFile(<span class="hljs-string">'./zf.js'</span>, <span class="hljs-string">'utf-8'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err, data</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'data'</span>,data);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>readFile</code>函数的第三个参数，就是回调函数，也就是任务的第二段。等到操作系统返回了<code>./zf.js</code>这个文件以后，回调函数才会执行。</p>
<blockquote>
<p>一个有趣的问题是，为什么 Node 约定，回调函数的第一个参数，必须是错误对象err（如果没有错误，该参数就是null）？</p>
</blockquote>
<blockquote>
<p>原因是执行分成两段，第一段执行完以后，任务所在的上下文环境就已经结束了。在这以后抛出的错误，原来的上下文环境已经无法捕捉，只能当作参数，传入第二段。</p>
</blockquote>
<h3 data-id="heading-13">回调函数的强耦合问题</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
fs.readFile(fileA, <span class="hljs-string">'utf-8'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err, data</span>) </span>&#123;
    fs.readFile(fileB, <span class="hljs-string">'utf-8'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err, data</span>) </span>&#123;
        <span class="hljs-comment">//...</span>
    &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以读取多个文件为例，只要有一个操作需要修改，它的上层回调函数和下层回调函数，可能都要跟着修改。这种情况就称为"回调函数地狱"（callback hell）。</p>
<blockquote>
<p>Promise 对象就是为了解决这个问题而提出的。它不是新的语法功能，而是一种新的写法，允许将回调函数的嵌套，改成链式调用。</p>
</blockquote>
<p><code>fs-readfile-promise</code>模块，它的作用就是返回一个 <code>Promise</code> 版本的<code>readFile</code>函数。<code>Promise</code> 提供<code>then</code>方法加载回调函数，<code>catch</code>方法捕捉执行过程中抛出的错误。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> readFile = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs-readfile-promise'</span>);

readFile(fileA)
.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(data.toString());
&#125;)
.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> readFile(fileB);
&#125;)
.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(data.toString());
&#125;)
.catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(err);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">Promise的最大问题</h3>
<p>Promise 的最大问题是代码冗余，原来的任务被 Promise 包装了一下，不管什么操作，一眼看去都是一堆then，原来的语义变得很不清楚。</p>
<blockquote>
<p>多余执行的冗余：如在某段程序的函数中，出现的语句，在对返回的参数没有任何的影响，但是又执行了多次，是为多余执行，此冗余是对CPU的消耗，应该杜绝该种冗余，应该注释掉。</p>
</blockquote>
<blockquote>
<p>代码数量的冗余：代码中太多的注释，或者一些没有使用到的变量，函数而存在程序中，这种冗余会让代码的可读性降低</p>
</blockquote>
<h3 data-id="heading-15">Generator函数的出现</h3>
<blockquote>
<p>ES6 提供的一种异步编程解决方案，语法行为与传统函数完全不同</p>
</blockquote>
<h4 data-id="heading-16">协程</h4>
<p>传统的编程语言，早有异步编程的解决方案（其实是多任务的解决方案）。其中有一种叫做"协程"（coroutine），意思是多个线程互相协作，完成异步任务。</p>
<p>协程有点像函数，又有点像线程。它的运行流程大致如下。</p>
<ul>
<li>第一步，协程A开始执行。</li>
<li>第二步，协程A执行到一半，进入暂停，执行权转移到协程B。</li>
<li>第三步，（一段时间后）协程B交还执行权。</li>
<li>第四步，协程A恢复执行。</li>
</ul>
<p>上面流程的协程A，就是异步任务，因为它分成两段（或多段）执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">asyncJob</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// ...其他代码</span>
  <span class="hljs-keyword">var</span> f = <span class="hljs-keyword">yield</span> readFile(fileA);
  <span class="hljs-comment">// ...其他代码</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的函数<code>asyncJob</code>是一个协程，它的奥妙就在其中的<code>yield</code>命令。它表示执行到此处，执行权将交给其他协程。也就是说，<code>yield</code>命令是异步两个阶段的分界线。</p>
<p>协程遇到<code>yield</code>命令就暂停，等到执行权返回，再从暂停的地方继续往后执行。它的最大优点，就是代码的写法非常像同步操作，如果去除<code>yield</code>命令，简直一模一样。</p>
<h4 data-id="heading-17">Generator 函数的数据交换和错误处理</h4>
<p><code>Generator</code> 函数可以暂停执行和恢复执行，这是它能封装异步任务的根本原因。除此之外，它还有两个特性，使它可以作为异步编程的完整解决方案：函数体内外的数据交换和错误处理机制。</p>
<p><code>next</code>返回值的<code>value</code> 属性，是 <code>Generator</code> 函数向外输出数据；next方法还可以接受参数，向 <code>Generator</code> 函数体内输入数据。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gen</span>(<span class="hljs-params">x</span>)</span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">yield</span>;
  &#125; <span class="hljs-keyword">catch</span> (e)&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'内部捕获'</span>,e);
  &#125;
&#125;

<span class="hljs-keyword">var</span> g = gen(<span class="hljs-number">1</span>);

g.next()
<span class="hljs-keyword">try</span> &#123;
  g.throw(<span class="hljs-string">'a'</span>);
  g.throw(<span class="hljs-string">'b'</span>);
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'外部捕获'</span>, e);
&#125;
<span class="hljs-comment">// 内部捕获 a</span>
<span class="hljs-comment">// 外部捕获 b</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码，<code>Generator</code> 函数体外，使用指针对象的<code>throw</code>方法抛出的错误，可以被函数体内的<code>try...catch</code>代码块捕获。这意味着，出错的代码与处理错误的代码，实现了时间和空间上的分离，这对于异步编程无疑是很重要的。</p>
<h4 data-id="heading-18">Generator的自动管理</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span>(<span class="hljs-params">fn</span>) </span>&#123;
  <span class="hljs-keyword">var</span> gen = fn();
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params">data</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'自动循环'</span>,data)
    <span class="hljs-keyword">var</span> result = gen.next(data);
<span class="hljs-built_in">console</span>.log(result.value)
    <span class="hljs-keyword">if</span> (result.done) <span class="hljs-keyword">return</span>;
    next(result.value)
  &#125;;
  next();
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">f</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
<span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
<span class="hljs-keyword">return</span> <span class="hljs-number">3</span>;
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'同步执行开始'</span>);
run(f);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行结束'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-19">async...await</h1>
<blockquote>
<p>ES2017 标准引入了 async 函数，使得异步操作变得更加方便。<br>
async 函数是什么？一句话，它就是 Generator 函数的语法糖。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">f</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">yield</span> <span class="hljs-number">1</span>;
<span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
<span class="hljs-keyword">return</span> <span class="hljs-number">3</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">await</span> <span class="hljs-number">1</span>;
<span class="hljs-keyword">await</span> <span class="hljs-number">2</span>;
        <span class="hljs-keyword">await</span> <span class="hljs-number">3</span>;
&#125;;
f();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>async</code>函数就是将 <code>Generator</code> 函数的星号<code>（*）</code>替换成<code>async</code>，将<code>yield</code>替换成<code>await</code>，仅此而已。</p>
<blockquote>
<p>async函数对 Generator 函数的改进，体现在以下四点:</p>
<ol>
<li>内置执行器</li>
<li>更好的语义</li>
<li>更广的适用性</li>
<li>返回值是 Promise</li>
</ol>
</blockquote>
<p>（1）内置执行器。<br>
<code>Generator</code> 函数的执行必须靠执行器(自动管理模式的封装)，而<code>async</code>函数自带执行器。也就是说，<code>async</code>函数的执行，与普通函数一模一样，只要一行。</p>
<p>（2）更好的语义。<br>
<code>async</code>和<code>await</code>，比起星号和<code>yield</code>，语义更清楚了。<code>async</code>表示函数里有异步操作，<code>await</code>表示紧跟在后面的表达式需要等待结果。</p>
<p>（3）更广的适用性。<br>
<code>async</code>函数的<code>await</code>命令后面，可以是 <code>Promise </code>对象和原始类型的值（数值、字符串和布尔值，但这时会自动转成立即 <code>resolved</code> 的 <code>Promise</code> 对象）。</p>
<p>（4）返回值是 Promise。
async函数的返回值是 <code>Promise</code> 对象，这比 <code>Generator </code>函数的返回值是 <code>Iterator</code> 对象方便多了。你可以用<code>then</code>方法指定下一步的操作。</p>
<p>进一步说，<code>async</code>函数完全可以看作多个异步操作，包装成的一个 <code>Promise</code> 对象，而<code>await</code>命令就是内部<code>then</code>命令的语法糖。</p>
<h2 data-id="heading-20">系统检验</h2>
<h3 data-id="heading-21">一</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">async1</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async1 start'</span>);
    <span class="hljs-keyword">await</span> async2();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async1 end'</span>);
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">async2</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async2'</span>);
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script start'</span>);
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout'</span>);
&#125;, <span class="hljs-number">0</span>)
async1();
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise1'</span>);
    resolve();
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise2'</span>);
&#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script end'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">二</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> num = <span class="hljs-number">10</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async:'</span>+<span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async-set'</span>+ ++num),<span class="hljs-number">0</span>)
num++;
res(num);
num++
&#125;));
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async2:'</span>+num)
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>,++num)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'2'</span>,num++)
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'set1'</span>+num),<span class="hljs-number">0</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'c1:'</span>+num)
foo()
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'c2:'</span>+num)
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'set2:'</span>+num),<span class="hljs-number">0</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">参见</h2>
<h6 data-id="heading-24">1.<a href="https://es6.ruanyifeng.com/#docs/generator" target="_blank" rel="nofollow noopener noreferrer"> 阮一峰-es6入门</a></h6></div>  
</div>
            