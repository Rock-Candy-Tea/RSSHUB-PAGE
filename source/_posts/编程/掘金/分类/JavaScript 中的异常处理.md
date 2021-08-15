
---
title: 'JavaScript 中的异常处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4019'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 07:58:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=4019'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与8月更文挑战的第14天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
</blockquote>
<p><strong>错误是编程过程的一部分</strong>。编写程序的过程难免会出现一些错误，通过这些产生的错误，我们可以学会如何避免遇到这样的情况，以及如何在下次做的更好。</p>
<p>在 JavaScript 中，当代码语句紧密耦合并产生错误时，继续使用剩余的代码语句是没有意义的。相反，我们试图尽可能优雅地从错误中恢复过来。JavaScript 解释器在出现此类错误时检查<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FControl_flow_and_error_handling" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling" ref="nofollow noopener noreferrer">异常处理</a>代码，如果没有异常处理程序，程序将返回导致错误的任何函数。</p>
<p>对<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FGlossary%2FCall_stack" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Glossary/Call_stack" ref="nofollow noopener noreferrer">调用堆栈</a>上的每个函数重复此操作，直到找到异常处理程序或到达顶层函数，从而导致程序以错误终止，导致程序的崩溃。</p>
<p>一般来说，有两种处理方式：</p>
<ul>
<li><strong>抛出异常</strong> — 如果在运行时发生的问题无法得到有意义的处理，最好抛出它</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">openFile</span>(<span class="hljs-params">fileName</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!exists(fileName)) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'找不到文件 '</span> + fileName) <span class="hljs-comment">// (1)</span>
  &#125;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>捕获异常</strong> — 抛出的异常在运行时更有意义的地方被捕获和处理</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
  openFile(<span class="hljs-string">'../test.js'</span>)
&#125; <span class="hljs-keyword">catch</span>(e) &#123;
  <span class="hljs-comment">// 优雅地处理抛出的期望</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让我们更详细地了解这些操作。</p>
<h2 data-id="heading-0">抛出异常</h2>
<p>您可能会看到类似 <code>ReferenceError: specs is not defined</code> 这样的情况。这表示通过 <code>throw</code> 语句引发的异常。</p>
<h3 data-id="heading-1">语法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">throw</span> «value»
​
<span class="hljs-comment">// 不要这样做</span>
<span class="hljs-keyword">if</span> (somethingBadHappened) &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-string">'Something bad happened'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对可以作为异常抛出的数据类型没有限制，但 JavaScript 具有特殊的内置异常类型。其中之一是 <code>Error</code>，正如您在前面的示例中所看到的。这些内置的异常类型为我们提供了比异常消息更多的细节。</p>
<h3 data-id="heading-2">Error</h3>
<p><code>Error</code> 类型用于表示一般异常。这种类型的异常最常用于实现用户定义的异常。它有两个内置属性可供使用。</p>
<ul>
<li><code>message</code> — 作为参数传递给 <strong><code>Error</code></strong> 构造函数的内容。例如，<code>new Error('This is an error message')</code>。您可以通过 <code>message</code> 属性访问消息。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> myError = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Error!!!'</span>)
​
<span class="hljs-built_in">console</span>.log(myError.message) <span class="hljs-comment">// Error!!!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>stack</code> — 该属性返回导致错误的文件的历史记录（调用堆栈）。堆栈顶部还包括 <code>message</code>，后面是实际堆栈，从最新/隔离的错误点开始，到最外部负责的文件。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Error</span>: <span class="hljs-built_in">Error</span>!!!
    at <anonymous>:<span class="hljs-number">1</span>:<span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong>：<code>new Error('...')</code> 在抛出之前不会执行任何操作，即 <code>throw new Error('error msg')</code>  将在 JavaScript 中创建一个 <code>Error</code> 实例，并停止脚本的执行，除非您对 <code>Error</code> 错误执行某些操作，例如捕获它。</p>
<h2 data-id="heading-3">捕捉异常</h2>
<p>现在我们知道了什么是异常以及如何抛出它们，让我们讨论一下如何通过捕获它们来阻止它们破坏我们的程序。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ftry...catch" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch" ref="nofollow noopener noreferrer"><code>try-catch-finally</code></a> 是处理异常的最简单方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
  <span class="hljs-comment">// 要运行的代码</span>
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
  <span class="hljs-comment">// 发生异常时要运行的代码</span>
&#125;
  
[ <span class="hljs-comment">// 可选</span>
  <span class="hljs-keyword">finally</span> &#123;
    <span class="hljs-comment">// 无论发生异常都始终执行的代码</span>
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>try</code> 子句中，我们添加了可能产生异常的代码。如果发生异常，则执行 <code>catch</code> 子句。</p>
<p>有时，无论代码是否产生异常，都需要执行代码，这时我们可以使用可选块 <code>finally</code>。</p>
<p>即使 <code>try</code> 或 <code>catch</code> 子句执行 <code>return</code> 语句，<code>finally</code> 块也将执行。例如，以下函数返回 <code>'Execute finally'</code>，因为 <code>finally</code> 子句是最后执行的内容。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125; <span class="hljs-keyword">finally</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Execute finally'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在无法事先检查代码正确性的地方使用 <code>try-catch</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> user = <span class="hljs-string">'&#123;"name": "D.O", "age": 18&#125;'</span>
<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-comment">// 代码运行</span>
  <span class="hljs-built_in">JSON</span>.parse(params)
  <span class="hljs-comment">// 在出现错误的情况下，其余的代码将永远无法运行</span>
  <span class="hljs-built_in">console</span>.log(params)
&#125; <span class="hljs-keyword">catch</span> (err) &#123;
  <span class="hljs-comment">// 在异常情况下运行的代码</span>
  <span class="hljs-built_in">console</span>.log(err.message) <span class="hljs-comment">// params is not defined</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所示，在执行代码之前，不可能检查 <code>JSON.parse</code> 以获得 <code>stringify</code> 对象或字符串。</p>
<blockquote>
<p><strong>注意</strong>：您可以捕获程序产生的异常和运行时异常，但无法捕获 JavaScript 语法错误。</p>
</blockquote>
<p><code>try-catch-finally</code> 只能捕获同步错误。如果我们尝试将其用于异步代码，那么在异步代码完成其执行之前，<code>try-catch-finally</code> 可能已经执行了。</p>
<h2 data-id="heading-4">如何处理异步代码块中的异常</h2>
<h3 data-id="heading-5">回调函数</h3>
<p>使用回调函数（不推荐），我们通常会收到两个如下所示的参数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">code, (err, result) => &#123;
  <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">return</span> <span class="hljs-built_in">console</span>.error(err)
  <span class="hljs-built_in">console</span>.log(result)
&#125;</span>)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到有两个参数：<code>err</code> 和 <code>result</code>。如果有错误，<code>err</code> 参数将等于该错误，我们可以抛出该错误来进行异常处理。</p>
<p>在 <code>if (err)</code> 块中返回某些内容或将其他指令包装在 <code>else</code> 块中都很重要。否则，您可能会遇到另一个错误。例如，当您尝试访问 <code>result.data</code> 时，<code>result</code> 可能未定义。</p>
<h3 data-id="heading-6">Promises</h3>
<p>使用 <code>promises</code> 的 <code>then</code> 或者 <code>catch</code>，我们可以通过将错误处理程序传递给 <code>then</code> 方法或使用 <code>catch</code> 子句来处理错误。</p>
<pre><code class="hljs language-js copyable" lang="js">promise.then(onFulfilled, onRejected)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以使用 <code>.catch(onRejected)</code> 而不是 <code>.then(null, onRejected)</code> 添加错误处理程序，其工作方式相同。</p>
<p>让我们看一个 <code>.catch</code> 拒绝 <code>Promise</code> 的例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'1'</span>)
  .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res) <span class="hljs-comment">// 1</span>
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'go wrong'</span>) <span class="hljs-comment">// 抛出异常</span>
&#125;)
.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res) <span class="hljs-comment">// 不会被执行</span>
&#125;)
.catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123; 
  <span class="hljs-built_in">console</span>.error(err) <span class="hljs-comment">// 捕获并处理异常 ——> Error: go wrong</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">使用 <code>async/await</code> 和 <code>try-catch</code></h3>
<p>使用 <code>async</code>/<code>await</code> 和 <code>try-catch-finally</code>，处理异常是轻而易举的事。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">func</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">await</span> nonExistentFunction()
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-built_in">console</span>.error(err) <span class="hljs-comment">// ReferenceError: nonExistentFunction is not defined </span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">如何处理未捕获的异常</h2>
<p>现在我们已经很好地理解了如何在同步和异步代码块中执行异常处理，让我们回答本文最后一个待解决的问题 ：<strong>我们如何处理未捕获的异常？</strong></p>
<h3 data-id="heading-9">在浏览器中</h3>
<p>我们可以使用 <code>window.onerror()</code> 方法来处理未捕获的异常。每当运行时发生错误时，该方法会在 <code>window</code> 对象上触发 <code>error</code> 事件。</p>
<p><code>onerror()</code> 的另一个实用模式是使用它来显示一条消息，以防在站点中加载图片时出现错误。</p>
<p><code>onerror()</code> 的另一个实用做法是：当站点中的图片或视频等数据加载出错时，可以用该方法触发某些操作。例如，提供一张加载出错时的图片，或显示一条消息。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"logo.png"</span> <span class="hljs-attr">onerror</span>=<span class="hljs-string">"alert('Error loading picture.')"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">在 Node.js 中</h3>
<p><code>EventEmitter</code> 模块派生的 <code>process</code> 对象可以订阅事件 <code>uncaughtException</code>。</p>
<pre><code class="hljs language-js copyable" lang="js">process.on(<span class="hljs-string">'uncaughtException'</span>, <span class="hljs-function">() =></span> &#123;&#125;)<span class="hljs-string">`
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以传递一个回调来处理异常。如果我们尝试捕获这个未捕获的异常，进程将不会终止，因此我们必须手动完成。</p>
<p><code>uncaughtException</code> 仅适用于同步代码。对于异步代码，还有另一个称为 <code>unhandledRejection</code> 的事件。</p>
<pre><code class="hljs language-js copyable" lang="js">process.on(<span class="hljs-string">'unhandledRejection'</span>, <span class="hljs-function">() =></span> &#123;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>决不要尝试为基本 <code>Error</code> 类型实现 “捕获所有” 处理程序。这将混淆所发生的一切，并损害代码的可维护性和可扩展性。</p>
<h2 data-id="heading-11">关键要点</h2>
<ul>
<li><code>throw</code> 语句用于生成用户定义的异常。在运行时，当 <code>throw</code> 遇到语句时，当前函数的执行将停止，控制权将传递给 <code>catch</code> 调用堆栈中的第一个子句。如果没有 <code>catch</code> 子句，程序将终止</li>
<li>JavaScript 有一些内置的异常类型，最值得注意的是 <code>Error</code>，它返回 <strong>Error</strong> 中的两个重要属性：<code>stack</code> 和 <code>message</code>。</li>
<li><code>try</code> 子句将包含可能产生异常的代码，<code>catch</code> 子句会在发生异常时执行。</li>
<li>对于异步代码，最好使用 <code>async/await</code> 配合 <code>try-catch</code> 语句。</li>
<li>可以捕获未处理的异常，这可以防止应用程序崩溃。</li>
</ul>
<p>不要觉得麻烦，异常处理可以帮助您提高代码的可维护性、可扩展性和可读性。</p></div>  
</div>
            