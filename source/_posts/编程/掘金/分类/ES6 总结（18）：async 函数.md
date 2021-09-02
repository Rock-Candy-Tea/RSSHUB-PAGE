
---
title: 'ES6 总结（18）：async 函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1496'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 22:27:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=1496'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、含义</h2>
<p>ES2017 标准引入了 <code>async</code> 函数，使得异步操作变得更加方便。</p>
<p><code>async</code> 函数是什么？一句话，它就是 <code>Generator</code> 函数的语法糖。</p>
<p>前文有一个 <code>Generator</code> 函数，依次读取两个文件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);

<span class="hljs-keyword">const</span> readFile = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fileName</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    fs.readFile(fileName, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error, data</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (error) <span class="hljs-keyword">return</span> reject(error);
      resolve(data);
    &#125;);
  &#125;);
&#125;;

<span class="hljs-keyword">const</span> gen = <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> f1 = <span class="hljs-keyword">yield</span> readFile(<span class="hljs-string">'/etc/fstab'</span>);
  <span class="hljs-keyword">const</span> f2 = <span class="hljs-keyword">yield</span> readFile(<span class="hljs-string">'/etc/shells'</span>);
  <span class="hljs-built_in">console</span>.log(f1.toString());
  <span class="hljs-built_in">console</span>.log(f2.toString());
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的函数 <code>gen</code> 可以写成 <code>async</code> 函数，就是下面这样。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> asyncReadFile = <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> f1 = <span class="hljs-keyword">await</span> readFile(<span class="hljs-string">'/etc/fstab'</span>);
  <span class="hljs-keyword">const</span> f2 = <span class="hljs-keyword">await</span> readFile(<span class="hljs-string">'/etc/shells'</span>);
  <span class="hljs-built_in">console</span>.log(f1.toString());
  <span class="hljs-built_in">console</span>.log(f2.toString());
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一比较就会发现，<code>async</code> 函数就是将 <code>Generator</code> 函数的星号（<code>*</code>）替换成 <code>async</code>，将 <code>yield</code> 替换成 <code>await</code>，仅此而已。</p>
<p><code>async</code> 函数对 <code>Generator</code> 函数的改进，体现在以下四点。</p>
<p>（1）内置执行器。</p>
<p><code>Generator</code> 函数的执行必须靠执行器，所以才有了 <code>co</code> 模块，而 <code>async</code> 函数自带执行器。也就是说，<code>async</code> 函数的执行，与普通函数一模一样，只要一行。</p>
<pre><code class="hljs language-js copyable" lang="js">asyncReadFile();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码调用了 <code>asyncReadFile</code> 函数，然后它就会自动执行，输出最后结果。这完全不像 <code>Generator</code> 函数，需要调用 <code>next</code> 方法，或者用 <code>co</code> 模块，才能真正执行，得到最后结果。</p>
<p>（2）更好的语义。</p>
<p><code>async</code> 和 <code>await</code>，比起星号和 <code>yield</code>，语义更清楚了。<code>async</code> 表示函数里有异步操作，<code>await</code> 表示紧跟在后面的表达式需要等待结果。</p>
<p>（3）更广的适用性。</p>
<p><code>co</code> 模块约定，<code>yield</code> 命令后面只能是 <code>Thunk</code> 函数或 <code>Promise</code> 对象，而 <code>async</code> 函数的 <code>await</code> 命令后面，可以是 <code>Promise</code> 对象和原始类型的值（数值、字符串和布尔值，但这时会自动转成立即 <code>resolved</code> 的 <code>Promise</code> 对象）。</p>
<p>（4）返回值是 Promise。</p>
<p><code>async</code> 函数的返回值是 <code>Promise</code> 对象，这比 <code>Generator</code> 函数的返回值是 Iterator 对象方便多了。你可以用 <code>then</code> 方法指定下一步的操作。</p>
<p>进一步说，<code>async</code> 函数完全可以看作多个异步操作，包装成的一个 <code>Promise</code> 对象，而 <code>await</code> 命令就是内部 <code>then</code> 命令的语法糖。</p>
<h2 data-id="heading-1">二、基本用法</h2>
<p><code>async</code> 函数返回一个 <code>Promise</code> 对象，可以使用 <code>then</code> 方法添加回调函数。当函数执行的时候，一旦遇到 <code>await</code> 就会先返回，等到异步操作完成，再接着执行函数体内后面的语句。</p>
<p>下面是一个例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getStockPriceByName</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">const</span> symbol = <span class="hljs-keyword">await</span> getStockSymbol(name);
  <span class="hljs-keyword">const</span> stockPrice = <span class="hljs-keyword">await</span> getStockPrice(symbol);
  <span class="hljs-keyword">return</span> stockPrice;
&#125;

getStockPriceByName(<span class="hljs-string">'goog'</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">result</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(result);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码是一个获取股票报价的函数，函数前面的 <code>async</code> 关键字，表明该函数内部有异步操作。调用该函数时，会立即返回一个 <code>Promise</code> 对象。</p>
<p>下面是另一个例子，指定多少毫秒后输出一个值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timeout</span>(<span class="hljs-params">ms</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(resolve, ms);
  &#125;);
&#125;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncPrint</span>(<span class="hljs-params">value, ms</span>) </span>&#123;
  <span class="hljs-keyword">await</span> timeout(ms);
  <span class="hljs-built_in">console</span>.log(value);
&#125;

asyncPrint(<span class="hljs-string">'hello world'</span>, <span class="hljs-number">50</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码指定 <code>50</code> 毫秒以后，输出 <code>hello world</code>。</p>
<p>由于 <code>async</code> 函数返回的是 <code>Promise</code> 对象，可以作为 <code>await</code> 命令的参数。所以，上面的例子也可以写成下面的形式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timeout</span>(<span class="hljs-params">ms</span>) </span>&#123;
  <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(resolve, ms);
  &#125;);
&#125;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncPrint</span>(<span class="hljs-params">value, ms</span>) </span>&#123;
  <span class="hljs-keyword">await</span> timeout(ms);
  <span class="hljs-built_in">console</span>.log(value);
&#125;

asyncPrint(<span class="hljs-string">'hello world'</span>, <span class="hljs-number">50</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>async 函数有多种使用形式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 函数声明</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

<span class="hljs-comment">// 函数表达式</span>
<span class="hljs-keyword">const</span> foo = <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;;

<span class="hljs-comment">// 对象的方法</span>
<span class="hljs-keyword">let</span> obj = &#123; <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span> &#123;&#125; &#125;;
obj.foo().then(...)

<span class="hljs-comment">// Class 的方法</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Storage</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.cachePromise = caches.open(<span class="hljs-string">'avatars'</span>);
  &#125;

  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getAvatar</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-keyword">const</span> cache = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.cachePromise;
    <span class="hljs-keyword">return</span> cache.match(<span class="hljs-string">`/avatars/<span class="hljs-subst">$&#123;name&#125;</span>.jpg`</span>);
  &#125;
&#125;

<span class="hljs-keyword">const</span> storage = <span class="hljs-keyword">new</span> Storage();
storage.getAvatar(<span class="hljs-string">'jake'</span>).then(…);

<span class="hljs-comment">// 箭头函数</span>
<span class="hljs-keyword">const</span> foo = <span class="hljs-keyword">async</span> () => &#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">三、语法</h2>
<p><code>async</code> 函数的语法规则总体上比较简单，难点是错误处理机制。</p>
<h3 data-id="heading-3">1. 返回 Promise 对象</h3>
<p><code>async</code> 函数返回一个 <code>Promise</code> 对象。</p>
<p><code>async</code> 函数内部 <code>return</code> 语句返回的值，会成为 <code>then</code> 方法回调函数的参数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">'hello world'</span>;
&#125;

f().then(<span class="hljs-function"><span class="hljs-params">v</span> =></span> <span class="hljs-built_in">console</span>.log(v))
<span class="hljs-comment">// "hello world"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，函数f内部 <code>return</code> 命令返回的值，会被 <code>then</code> 方法回调函数接收到。</p>
<p><code>async</code> 函数内部抛出错误，会导致返回的 <code>Promise</code> 对象变为 <code>reject</code> 状态。抛出的错误对象会被 <code>catch</code> 方法回调函数接收到。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'出错了'</span>);
&#125;

f().then(
  <span class="hljs-function"><span class="hljs-params">v</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'resolve'</span>, v),
  <span class="hljs-function"><span class="hljs-params">e</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'reject'</span>, e)
)
<span class="hljs-comment">//reject Error: 出错了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2. Promise 对象的状态变化</h3>
<p><code>async</code> 函数返回的 <code>Promise</code> 对象，必须等到内部所有 <code>await</code> 命令后面的 <code>Promise</code> 对象执行完，才会发生状态改变，除非遇到 <code>return</code> 语句或者抛出错误。也就是说，只有 <code>async</code> 函数内部的异步操作执行完，才会执行 <code>then</code> 方法指定的回调函数。</p>
<p>下面是一个例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTitle</span>(<span class="hljs-params">url</span>) </span>&#123;
  <span class="hljs-keyword">let</span> response = <span class="hljs-keyword">await</span> fetch(url);
  <span class="hljs-keyword">let</span> html = <span class="hljs-keyword">await</span> response.text();
  <span class="hljs-keyword">return</span> html.match(<span class="hljs-regexp">/<title>([\s\S]+)<\/title>/i</span>)[<span class="hljs-number">1</span>];
&#125;
getTitle(<span class="hljs-string">'https://tc39.github.io/ecma262/'</span>).then(<span class="hljs-built_in">console</span>.log)
<span class="hljs-comment">// "ECMAScript 2017 Language Specification"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，函数 <code>getTitle</code> 内部有三个操作：抓取网页、取出文本、匹配页面标题。只有这三个操作全部完成，才会执行 <code>then</code> 方法里面的 <code>console.log</code>。</p>
<h3 data-id="heading-5">3. await 命令</h3>
<p>正常情况下，<code>await</code> 命令后面是一个 <code>Promise</code> 对象，返回该对象的结果。如果不是 <code>Promise</code> 对象，就直接返回对应的值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 等同于</span>
  <span class="hljs-comment">// return 123;</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> <span class="hljs-number">123</span>;
&#125;

f().then(<span class="hljs-function"><span class="hljs-params">v</span> =></span> <span class="hljs-built_in">console</span>.log(v))
<span class="hljs-comment">// 123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>await</code> 命令的参数是数值 <code>123</code>，这时等同于 <code>return 123</code>。</p>
<p>另一种情况是，<code>await</code> 命令后面是一个 <code>thenable</code> 对象（即定义了 <code>then</code> 方法的对象），那么 <code>await</code> 会将其等同于 <code>Promise</code> 对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Sleep</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">timeout</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.timeout = timeout;
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">resolve, reject</span>)</span> &#123;
    <span class="hljs-keyword">const</span> startTime = <span class="hljs-built_in">Date</span>.now();
    <span class="hljs-built_in">setTimeout</span>(
      <span class="hljs-function">() =></span> resolve(<span class="hljs-built_in">Date</span>.now() - startTime),
      <span class="hljs-built_in">this</span>.timeout
    );
  &#125;
&#125;

(<span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">const</span> sleepTime = <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> Sleep(<span class="hljs-number">1000</span>);
  <span class="hljs-built_in">console</span>.log(sleepTime);
&#125;)();
<span class="hljs-comment">// 1000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>await</code> 命令后面是一个 <code>Sleep</code> 对象的实例。这个实例不是 <code>Promise</code> 对象，但是因为定义了 <code>then</code> 方法，<code>await</code> 会将其视为 <code>Promise</code> 处理。</p>
<p>这个例子还演示了如何实现休眠效果。JavaScript 一直没有休眠的语法，但是借助 <code>await</code> 命令就可以让程序停顿指定的时间。下面给出了一个简化的 <code>sleep</code> 实现。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sleep</span>(<span class="hljs-params">interval</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(resolve, interval);
  &#125;)
&#125;

<span class="hljs-comment">// 用法</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">one2FiveInAsync</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">5</span>; i++) &#123;
    <span class="hljs-built_in">console</span>.log(i);
    <span class="hljs-keyword">await</span> sleep(<span class="hljs-number">1000</span>);
  &#125;
&#125;

one2FiveInAsync();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>await</code> 命令后面的 <code>Promise</code> 对象如果变为 <code>reject</code> 状态，则 <code>reject</code> 的参数会被 <code>catch</code> 方法的回调函数接收到。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'出错了'</span>);
&#125;

f()
.then(<span class="hljs-function"><span class="hljs-params">v</span> =></span> <span class="hljs-built_in">console</span>.log(v))
.catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> <span class="hljs-built_in">console</span>.log(e))
<span class="hljs-comment">// 出错了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，上面代码中，<code>await</code> 语句前面没有 <code>return</code>，但是 <code>reject</code> 方法的参数依然传入了 <code>catch</code> 方法的回调函数。这里如果在 <code>await</code> 前面加上 <code>return</code>，效果是一样的。</p>
<p>任何一个 <code>await</code> 语句后面的 <code>Promise</code> 对象变为 <code>reject</code> 状态，那么整个 <code>async</code> 函数都会中断执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'出错了'</span>);
  <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'hello world'</span>); <span class="hljs-comment">// 不会执行</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，第二个 <code>await</code> 语句是不会执行的，因为第一个 <code>await</code> 语句状态变成了 <code>reject</code>。</p>
<p>有时，我们希望即使前一个异步操作失败，也不要中断后面的异步操作。这时可以将第一个 <code>await</code> 放在 <code>try...catch</code> 结构里面，这样不管这个异步操作是否成功，第二个 <code>await</code> 都会执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'出错了'</span>);
  &#125; <span class="hljs-keyword">catch</span>(e) &#123;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'hello world'</span>);
&#125;

f()
.then(<span class="hljs-function"><span class="hljs-params">v</span> =></span> <span class="hljs-built_in">console</span>.log(v))
<span class="hljs-comment">// hello world</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一种方法是 <code>await</code> 后面的 <code>Promise</code> 对象再跟一个 <code>catch</code> 方法，处理前面可能出现的错误。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'出错了'</span>)
    .catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> <span class="hljs-built_in">console</span>.log(e));
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'hello world'</span>);
&#125;

f()
.then(<span class="hljs-function"><span class="hljs-params">v</span> =></span> <span class="hljs-built_in">console</span>.log(v))
<span class="hljs-comment">// 出错了</span>
<span class="hljs-comment">// hello world</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">4. 错误处理</h3>
<p>如果 <code>await</code> 后面的异步操作出错，那么等同于 <code>async</code> 函数返回的 <code>Promise</code> 对象被 <code>reject</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'出错了'</span>);
  &#125;);
&#125;

f()
.then(<span class="hljs-function"><span class="hljs-params">v</span> =></span> <span class="hljs-built_in">console</span>.log(v))
.catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> <span class="hljs-built_in">console</span>.log(e))
<span class="hljs-comment">// Error：出错了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>async</code> 函数 <code>f</code> 执行后，<code>await</code> 后面的 <code>Promise</code> 对象会抛出一个错误对象，导致 <code>catch</code> 方法的回调函数被调用，它的参数就是抛出的错误对象。具体的执行机制，可以参考后文的“<code>async</code> 函数的实现原理”。</p>
<p>防止出错的方法，也是将其放在try...catch代码块之中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'出错了'</span>);
    &#125;);
  &#125; <span class="hljs-keyword">catch</span>(e) &#123;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span>(<span class="hljs-string">'hello world'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果有多个 <code>await</code> 命令，可以统一放在 <code>try...catch</code> 结构中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">const</span> val1 = <span class="hljs-keyword">await</span> firstStep();
    <span class="hljs-keyword">const</span> val2 = <span class="hljs-keyword">await</span> secondStep(val1);
    <span class="hljs-keyword">const</span> val3 = <span class="hljs-keyword">await</span> thirdStep(val1, val2);

    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Final: '</span>, val3);
  &#125;
  <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-built_in">console</span>.error(err);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面的例子使用 <code>try...catch</code> 结构，实现多次重复尝试。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> superagent = <span class="hljs-built_in">require</span>(<span class="hljs-string">'superagent'</span>);
<span class="hljs-keyword">const</span> NUM_RETRIES = <span class="hljs-number">3</span>;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> i;
  <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < NUM_RETRIES; ++i) &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">await</span> superagent.get(<span class="hljs-string">'http://google.com/this-throws-an-error'</span>);
      <span class="hljs-keyword">break</span>;
    &#125; <span class="hljs-keyword">catch</span>(err) &#123;&#125;
  &#125;
  <span class="hljs-built_in">console</span>.log(i); <span class="hljs-comment">// 3</span>
&#125;

test();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，如果 <code>await</code> 操作成功，就会使用 <code>break</code> 语句退出循环；如果失败，会被 <code>catch</code> 语句捕捉，然后进入下一轮循环。</p>
<h3 data-id="heading-7">5. 使用注意点</h3>
<p>第一点，前面已经说过，<code>await</code> 命令后面的 <code>Promise</code> 对象，运行结果可能是 <code>rejected</code>，所以最好把 <code>await</code> 命令放在 <code>try...catch</code> 代码块中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myFunction</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">await</span> somethingThatReturnsAPromise();
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-built_in">console</span>.log(err);
  &#125;
&#125;

<span class="hljs-comment">// 另一种写法</span>

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myFunction</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">await</span> somethingThatReturnsAPromise()
  .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(err);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二点，多个 <code>await</code> 命令后面的异步操作，如果不存在继发关系，最好让它们同时触发。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> foo = <span class="hljs-keyword">await</span> getFoo();
<span class="hljs-keyword">let</span> bar = <span class="hljs-keyword">await</span> getBar();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>getFoo</code> 和 <code>getBar</code> 是两个独立的异步操作（即互不依赖），被写成继发关系。这样比较耗时，因为只有 <code>getFoo</code> 完成以后，才会执行 <code>getBar</code>，完全可以让它们同时触发。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 写法一</span>
<span class="hljs-keyword">let</span> [foo, bar] = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all([getFoo(), getBar()]);

<span class="hljs-comment">// 写法二</span>
<span class="hljs-keyword">let</span> fooPromise = getFoo();
<span class="hljs-keyword">let</span> barPromise = getBar();
<span class="hljs-keyword">let</span> foo = <span class="hljs-keyword">await</span> fooPromise;
<span class="hljs-keyword">let</span> bar = <span class="hljs-keyword">await</span> barPromise;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面两种写法，<code>getFoo</code> 和 <code>getBar</code> 都是同时触发，这样就会缩短程序的执行时间。</p>
<p>第三点，<code>await</code> 命令只能用在 <code>async</code> 函数之中，如果用在普通函数，就会报错。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dbFuc</span>(<span class="hljs-params">db</span>) </span>&#123;
  <span class="hljs-keyword">let</span> docs = [&#123;&#125;, &#123;&#125;, &#123;&#125;];

  <span class="hljs-comment">// 报错</span>
  docs.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">doc</span>) </span>&#123;
    <span class="hljs-keyword">await</span> db.post(doc);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码会报错，因为 <code>await</code> 用在普通函数之中了。但是，如果将 <code>forEach</code> 方法的参数改成 <code>async</code> 函数，也有问题。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dbFuc</span>(<span class="hljs-params">db</span>) </span>&#123; <span class="hljs-comment">//这里不需要 async</span>
  <span class="hljs-keyword">let</span> docs = [&#123;&#125;, &#123;&#125;, &#123;&#125;];

  <span class="hljs-comment">// 可能得到错误结果</span>
  docs.forEach(<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">doc</span>) </span>&#123;
    <span class="hljs-keyword">await</span> db.post(doc);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码可能不会正常工作，原因是这时三个 <code>db.post</code> 操作将是并发执行，也就是同时执行，而不是继发执行。正确的写法是采用 <code>for</code> 循环。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dbFuc</span>(<span class="hljs-params">db</span>) </span>&#123;
  <span class="hljs-keyword">let</span> docs = [&#123;&#125;, &#123;&#125;, &#123;&#125;];

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> doc <span class="hljs-keyword">of</span> docs) &#123;
    <span class="hljs-keyword">await</span> db.post(doc);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一种方法是使用数组的reduce方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dbFuc</span>(<span class="hljs-params">db</span>) </span>&#123;
  <span class="hljs-keyword">let</span> docs = [&#123;&#125;, &#123;&#125;, &#123;&#125;];

  <span class="hljs-keyword">await</span> docs.reduce(<span class="hljs-keyword">async</span> (_, doc) => &#123;
    <span class="hljs-keyword">await</span> _;
    <span class="hljs-keyword">await</span> db.post(doc);
  &#125;, <span class="hljs-literal">undefined</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面例子中，<code>reduce</code> 方法的第一个参数是 <code>async </code>函数，导致该函数的第一个参数是前一步操作返回的 <code>Promise</code> 对象，所以必须使用 <code>await</code> 等待它操作结束。另外，<code>reduce</code> 方法返回的是 <code>docs</code> 数组最后一个成员的 <code>async</code> 函数的执行结果，也是一个 <code>Promise</code> 对象，导致在它前面也必须加上 <code>await</code>。</p>
<p>如果确实希望多个请求并发执行，可以使用 <code>Promise.all</code> 方法。当三个请求都会 <code>resolved</code> 时，下面两种写法效果相同。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dbFuc</span>(<span class="hljs-params">db</span>) </span>&#123;
  <span class="hljs-keyword">let</span> docs = [&#123;&#125;, &#123;&#125;, &#123;&#125;];
  <span class="hljs-keyword">let</span> promises = docs.map(<span class="hljs-function">(<span class="hljs-params">doc</span>) =></span> db.post(doc));

  <span class="hljs-keyword">let</span> results = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all(promises);
  <span class="hljs-built_in">console</span>.log(results);
&#125;

<span class="hljs-comment">// 或者使用下面的写法</span>

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dbFuc</span>(<span class="hljs-params">db</span>) </span>&#123;
  <span class="hljs-keyword">let</span> docs = [&#123;&#125;, &#123;&#125;, &#123;&#125;];
  <span class="hljs-keyword">let</span> promises = docs.map(<span class="hljs-function">(<span class="hljs-params">doc</span>) =></span> db.post(doc));

  <span class="hljs-keyword">let</span> results = [];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> promise <span class="hljs-keyword">of</span> promises) &#123;
    results.push(<span class="hljs-keyword">await</span> promise);
  &#125;
  <span class="hljs-built_in">console</span>.log(results);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第四点，<code>async</code> 函数可以保留运行堆栈。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = <span class="hljs-function">() =></span> &#123;
  b().then(<span class="hljs-function">() =></span> c());
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，函数 <code>a</code> 内部运行了一个异步任务 <code>b()</code>。当 <code>b()</code> 运行的时候，函数 <code>a()</code> 不会中断，而是继续执行。等到 <code>b()</code> 运行结束，可能 <code>a()</code> 早就运行结束了，<code>b()</code> 所在的上下文环境已经消失了。如果 <code>b()</code> 或 <code>c()</code> 报错，错误堆栈将不包括 <code>a()</code>。</p>
<p>现在将这个例子改成 <code>async</code> 函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">await</span> b();
  c();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>b()</code> 运行的时候，<code>a()</code> 是暂停执行，上下文环境都保存着。一旦 <code>b()</code> 或 <code>c()</code> 报错，错误堆栈将包括 <code>a()</code>。</p>
<h2 data-id="heading-8">四、async 函数的实现原理</h2>
<p><code>async</code> 函数的实现原理，就是将 <code>Generator</code> 函数和自动执行器，包装在一个函数里。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">args</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-comment">// 等同于</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">args</span>) </span>&#123;
  <span class="hljs-keyword">return</span> spawn(<span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// ...</span>
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有的 <code>async</code> 函数都可以写成上面的第二种形式，其中的 <code>spawn</code> 函数就是自动执行器。</p>
<p>下面给出 <code>spawn</code> 函数的实现，基本就是前文自动执行器的翻版。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">spawn</span>(<span class="hljs-params">genF</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-keyword">const</span> gen = genF();
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">step</span>(<span class="hljs-params">nextF</span>) </span>&#123;
      <span class="hljs-keyword">let</span> next;
      <span class="hljs-keyword">try</span> &#123;
        next = nextF();
      &#125; <span class="hljs-keyword">catch</span>(e) &#123;
        <span class="hljs-keyword">return</span> reject(e);
      &#125;
      <span class="hljs-keyword">if</span>(next.done) &#123;
        <span class="hljs-keyword">return</span> resolve(next.value);
      &#125;
      <span class="hljs-built_in">Promise</span>.resolve(next.value).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">v</span>) </span>&#123;
        step(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> gen.next(v); &#125;);
      &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
        step(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> gen.throw(e); &#125;);
      &#125;);
    &#125;
    step(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> gen.next(<span class="hljs-literal">undefined</span>); &#125;);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">五、与其他异步处理方法的比较</h2>
<p>我们通过一个例子，来看 <code>async</code> 函数与 <code>Promise</code>、<code>Generator</code> 函数的比较。</p>
<p>假定某个 DOM 元素上面，部署了一系列的动画，前一个动画结束，才能开始后一个。如果当中有一个动画出错，就不再往下执行，返回上一个成功执行的动画的返回值。</p>
<p>首先是 <code>Promise</code> 的写法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">chainAnimationsPromise</span>(<span class="hljs-params">elem, animations</span>) </span>&#123;

  <span class="hljs-comment">// 变量ret用来保存上一个动画的返回值</span>
  <span class="hljs-keyword">let</span> ret = <span class="hljs-literal">null</span>;

  <span class="hljs-comment">// 新建一个空的Promise</span>
  <span class="hljs-keyword">let</span> p = <span class="hljs-built_in">Promise</span>.resolve();

  <span class="hljs-comment">// 使用then方法，添加所有动画</span>
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> anim <span class="hljs-keyword">of</span> animations) &#123;
    p = p.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val</span>) </span>&#123;
      ret = val;
      <span class="hljs-keyword">return</span> anim(elem);
    &#125;);
  &#125;

  <span class="hljs-comment">// 返回一个部署了错误捕捉机制的Promise</span>
  <span class="hljs-keyword">return</span> p.catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-comment">/* 忽略错误，继续执行 */</span>
  &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> ret;
  &#125;);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然 <code>Promise</code> 的写法比回调函数的写法大大改进，但是一眼看上去，代码完全都是 <code>Promise</code> 的 API（<code>then</code>、<code>catch</code> 等等），操作本身的语义反而不容易看出来。</p>
<p>接着是 <code>Generator</code> 函数的写法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">chainAnimationsGenerator</span>(<span class="hljs-params">elem, animations</span>) </span>&#123;

  <span class="hljs-keyword">return</span> spawn(<span class="hljs-function"><span class="hljs-keyword">function</span>*(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> ret = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> anim <span class="hljs-keyword">of</span> animations) &#123;
        ret = <span class="hljs-keyword">yield</span> anim(elem);
      &#125;
    &#125; <span class="hljs-keyword">catch</span>(e) &#123;
      <span class="hljs-comment">/* 忽略错误，继续执行 */</span>
    &#125;
    <span class="hljs-keyword">return</span> ret;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码使用 <code>Generator</code> 函数遍历了每个动画，语义比 <code>Promise</code> 写法更清晰，用户定义的操作全部都出现在 <code>spawn</code> 函数的内部。这个写法的问题在于，必须有一个任务运行器，自动执行 <code>Generator</code> 函数，上面代码的 <code>spawn</code> 函数就是自动执行器，它返回一个 <code>Promise</code> 对象，而且必须保证 <code>yield</code> 语句后面的表达式，必须返回一个 <code>Promise</code>。</p>
<p>最后是 <code>async</code> 函数的写法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">chainAnimationsAsync</span>(<span class="hljs-params">elem, animations</span>) </span>&#123;
  <span class="hljs-keyword">let</span> ret = <span class="hljs-literal">null</span>;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> anim <span class="hljs-keyword">of</span> animations) &#123;
      ret = <span class="hljs-keyword">await</span> anim(elem);
    &#125;
  &#125; <span class="hljs-keyword">catch</span>(e) &#123;
    <span class="hljs-comment">/* 忽略错误，继续执行 */</span>
  &#125;
  <span class="hljs-keyword">return</span> ret;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到 <code>Async</code> 函数的实现最简洁，最符合语义，几乎没有语义不相关的代码。它将 <code>Generator</code> 写法中的自动执行器，改在语言层面提供，不暴露给用户，因此代码量最少。如果使用 <code>Generator</code> 写法，自动执行器需要用户自己提供。</p>
<h2 data-id="heading-10">六、实例：按顺序完成异步操作</h2>
<p>实际开发中，经常遇到一组异步操作，需要按照顺序完成。比如，依次远程读取一组 URL，然后按照读取的顺序输出结果。</p>
<p>Promise 的写法如下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">logInOrder</span>(<span class="hljs-params">urls</span>) </span>&#123;
  <span class="hljs-comment">// 远程读取所有URL</span>
  <span class="hljs-keyword">const</span> textPromises = urls.map(<span class="hljs-function"><span class="hljs-params">url</span> =></span> &#123;
    <span class="hljs-keyword">return</span> fetch(url).then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> response.text());
  &#125;);

  <span class="hljs-comment">// 按次序输出</span>
  textPromises.reduce(<span class="hljs-function">(<span class="hljs-params">chain, textPromise</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> chain.then(<span class="hljs-function">() =></span> textPromise)
      .then(<span class="hljs-function"><span class="hljs-params">text</span> =></span> <span class="hljs-built_in">console</span>.log(text));
  &#125;, <span class="hljs-built_in">Promise</span>.resolve());
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码使用 <code>fetch</code> 方法，同时远程读取一组 URL。每个 <code>fetch</code> 操作都返回一个 <code>Promise</code> 对象，放入 <code>textPromises</code> 数组。然后，<code>reduce</code> 方法依次处理每个 <code>Promise</code> 对象，然后使用 <code>then</code>，将所有 <code>Promise</code> 对象连起来，因此就可以依次输出结果。</p>
<p>这种写法不太直观，可读性比较差。下面是 <code>async</code> 函数实现。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">logInOrder</span>(<span class="hljs-params">urls</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> url <span class="hljs-keyword">of</span> urls) &#123;
    <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> fetch(url);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">await</span> response.text());
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码确实大大简化，问题是所有远程操作都是继发。只有前一个 URL 返回结果，才会去读取下一个 URL，这样做效率很差，非常浪费时间。我们需要的是并发发出远程请求。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">logInOrder</span>(<span class="hljs-params">urls</span>) </span>&#123;
  <span class="hljs-comment">// 并发读取远程URL</span>
  <span class="hljs-keyword">const</span> textPromises = urls.map(<span class="hljs-keyword">async</span> url => &#123;
    <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> fetch(url);
    <span class="hljs-keyword">return</span> response.text();
  &#125;);

  <span class="hljs-comment">// 按次序输出</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> textPromise <span class="hljs-keyword">of</span> textPromises) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">await</span> textPromise);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，虽然 <code>map</code> 方法的参数是 <code>async</code> 函数，但它是并发执行的，因为只有 <code>async</code> 函数内部是继发执行，外部不受影响。后面的 <code>for..of</code> 循环内部使用了 <code>await</code>，因此实现了按顺序输出。</p>
<h2 data-id="heading-11">七、顶层 await</h2>
<p>根据语法规格，<code>await</code> 命令只能出现在 <code>async</code> 函数内部，否则都会报错。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 报错</span>
<span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> fetch(<span class="hljs-string">'https://api.example.com'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>await</code> 命令独立使用，没有放在 <code>async</code> 函数里面，就会报错。</p>
<p>目前，有一个语法提案，允许在模块的顶层独立使用 <code>await</code> 命令，使得上面那行代码不会报错了。这个提案的目的，是借用 <code>await</code> 解决模块异步加载的问题。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// awaiting.js</span>
<span class="hljs-keyword">let</span> output;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> dynamic = <span class="hljs-keyword">await</span> <span class="hljs-keyword">import</span>(someMission);
  <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> fetch(url);
  output = someProcess(dynamic.default, data);
&#125;
main();
<span class="hljs-keyword">export</span> &#123; output &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，模块 awaiting.js 的输出值 <code>output</code>，取决于异步操作。我们把异步操作包装在一个 <code>async</code> 函数里面，然后调用这个函数，只有等里面的异步操作都执行，变量 <code>output</code> 才会有值，否则就返回 <code>undefined</code>。</p>
<p>上面的代码也可以写成立即执行函数的形式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// awaiting.js</span>
<span class="hljs-keyword">let</span> output;
(<span class="hljs-keyword">async</span> function1 <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">const</span> dynamic = <span class="hljs-keyword">await</span> <span class="hljs-keyword">import</span>(someMission);
  <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> fetch(url);
  output = someProcess(dynamic.default, data);
&#125;)();
<span class="hljs-keyword">export</span> &#123; output &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是加载这个模块的写法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// usage.js</span>
<span class="hljs-keyword">import</span> &#123; output &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./awaiting.js"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">outputPlusValue</span>(<span class="hljs-params">value</span>) </span>&#123; <span class="hljs-keyword">return</span> output + value &#125;

<span class="hljs-built_in">console</span>.log(outputPlusValue(<span class="hljs-number">100</span>));
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(outputPlusValue(<span class="hljs-number">100</span>), <span class="hljs-number">1000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>outputPlusValue()</code> 的执行结果，完全取决于执行的时间。如果 awaiting.js 里面的异步操作没执行完，加载进来的 <code>output</code> 的值就是 <code>undefined</code>。</p>
<p>目前的解决方法，就是让原始模块输出一个 <code>Promise</code> 对象，从这个 <code>Promise</code> 对象判断异步操作有没有结束。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// awaiting.js</span>
<span class="hljs-keyword">let</span> output;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> dynamic = <span class="hljs-keyword">await</span> <span class="hljs-keyword">import</span>(someMission);
  <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> fetch(url);
  output = someProcess(dynamic.default, data);
&#125;)();
<span class="hljs-keyword">export</span> &#123; output &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，awaiting.js 除了输出 <code>output</code>，还默认输出一个 <code>Promise</code> 对象（<code>async</code> 函数立即执行后，返回一个 <code>Promise</code> 对象），从这个对象判断异步操作是否结束。</p>
<p>下面是加载这个模块的新的写法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// usage.js</span>
<span class="hljs-keyword">import</span> promise, &#123; output &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./awaiting.js"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">outputPlusValue</span>(<span class="hljs-params">value</span>) </span>&#123; <span class="hljs-keyword">return</span> output + value &#125;

promise.then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(outputPlusValue(<span class="hljs-number">100</span>));
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(outputPlusValue(<span class="hljs-number">100</span>), <span class="hljs-number">1000</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，将 awaiting.js 对象的输出，放在 <code>promise.then()</code> 里面，这样就能保证异步操作完成以后，才去读取 <code>output</code>。</p>
<p>这种写法比较麻烦，等于要求模块的使用者遵守一个额外的使用协议，按照特殊的方法使用这个模块。一旦你忘了要用 <code>Promise</code> 加载，只使用正常的加载方法，依赖这个模块的代码就可能出错。而且，如果上面的 usage.js 又有对外的输出，等于这个依赖链的所有模块都要使用 <code>Promise</code> 加载。</p>
<p>顶层的 <code>await</code> 命令，就是为了解决这个问题。它保证只有异步操作完成，模块才会输出值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// awaiting.js</span>
<span class="hljs-keyword">const</span> dynamic = <span class="hljs-keyword">import</span>(someMission);
<span class="hljs-keyword">const</span> data = fetch(url);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> output = someProcess((<span class="hljs-keyword">await</span> dynamic).default, <span class="hljs-keyword">await</span> data);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，两个异步操作在输出的时候，都加上了 <code>await</code> 命令。只有等到异步操作完成，这个模块才会输出值。</p>
<p>加载这个模块的写法如下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// usage.js</span>
<span class="hljs-keyword">import</span> &#123; output &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./awaiting.js"</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">outputPlusValue</span>(<span class="hljs-params">value</span>) </span>&#123; <span class="hljs-keyword">return</span> output + value &#125;

<span class="hljs-built_in">console</span>.log(outputPlusValue(<span class="hljs-number">100</span>));
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(outputPlusValue(<span class="hljs-number">100</span>), <span class="hljs-number">1000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的写法，与普通的模块加载完全一样。也就是说，模块的使用者完全不用关心，依赖模块的内部有没有异步操作，正常加载即可。</p>
<p>这时，模块的加载会等待依赖模块（上例是 awaiting.js）的异步操作完成，才执行后面的代码，有点像暂停在那里。所以，它总是会得到正确的 <code>output</code>，不会因为加载时机的不同，而得到不一样的值。</p>
<p>注意，顶层 <code>await</code> 只能用在 ES6 模块，不能用在 CommonJS 模块。这是因为 CommonJS 模块的 <code>require()</code> 是同步加载，如果有顶层 <code>await</code>，就没法处理加载了。</p>
<p>下面是顶层 <code>await</code> 的一些使用场景。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// import() 方法加载</span>
<span class="hljs-keyword">const</span> strings = <span class="hljs-keyword">await</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">`/i18n/<span class="hljs-subst">$&#123;navigator.language&#125;</span>`</span>);

<span class="hljs-comment">// 数据库操作</span>
<span class="hljs-keyword">const</span> connection = <span class="hljs-keyword">await</span> dbConnector();

<span class="hljs-comment">// 依赖回滚</span>
<span class="hljs-keyword">let</span> jQuery;
<span class="hljs-keyword">try</span> &#123;
  jQuery = <span class="hljs-keyword">await</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'https://cdn-a.com/jQuery'</span>);
&#125; <span class="hljs-keyword">catch</span> &#123;
  jQuery = <span class="hljs-keyword">await</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'https://cdn-b.com/jQuery'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，如果加载多个包含顶层 <code>await</code> 命令的模块，加载命令是同步执行的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// x.js</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"X1"</span>);
<span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">r</span> =></span> <span class="hljs-built_in">setTimeout</span>(r, <span class="hljs-number">1000</span>));
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"X2"</span>);

<span class="hljs-comment">// y.js</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Y"</span>);

<span class="hljs-comment">// z.js</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"./x.js"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"./y.js"</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Z"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码有三个模块，最后的 z.js 加载 x.js 和 y.js，打印结果是 <code>X1</code>、<code>Y</code>、<code>X2</code>、<code>Z</code>。这说明，z.js 并没有等待 x.js 加载完成，再去加载 y.js。</p>
<p>顶层的 <code>await</code> 命令有点像，交出代码的执行权给其他的模块加载，等异步操作完成后，再拿回执行权，继续向下执行。</p></div>  
</div>
            