
---
title: '_译_使用Promise'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4446'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 19:02:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=4446'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557?utm_campaign=30day&utm_medium=Ccenter&utm_source=20210528" target="_blank">更文挑战</a></p>
<blockquote>
<p>本文翻译自 <a href="https://developers.google.com/web/ilt/pwa/working-with-promises?hl=en" target="_blank" rel="nofollow noopener noreferrer">《Working with Promises》</a></p>
</blockquote>
<h2 data-id="heading-0">介绍</h2>
<p><code>Promise</code>的出现，提供了一种更好的方式来处理JavaScript中的异步代码。在此之前，已经有一些第三方库实现了类似功能，例如：</p>
<p><a href="https://github.com/kriskowal/q" target="_blank" rel="nofollow noopener noreferrer">Q</a> <br>
<a href="https://github.com/cujojs/when" target="_blank" rel="nofollow noopener noreferrer">when</a><br>
<a href="https://docs.microsoft.com/en-us/previous-versions/windows/apps/br211867(v=win.10)?redirectedfrom=MSDN" target="_blank" rel="nofollow noopener noreferrer">WinJS</a><br>
<a href="https://github.com/tildeio/rsvp.js" target="_blank" rel="nofollow noopener noreferrer">RSVP.js</a></p>
<p>上面这些<code>Promise</code>库，和<code>ES2015 JavaScript</code>规范（即ES6）也都支持了<code>Promise</code>。</p>
<p>有关支持<code>Promise</code>的浏览器列表，可以参考： <a href="https://caniuse.com/promises" target="_blank" rel="nofollow noopener noreferrer">Can I Use</a></p>
<h2 data-id="heading-1">为什么要使用Promise</h2>
<p>在JavaScript中，异步操作是很常见的，它可以用来请求网络资源或访问本地磁盘，和Web Worker、Service Worker通信，以及使用定时器等。</p>
<p>大多数情况下，当这些操作处理完成后，都是通过回调函数或事件来进行通信的。在简单网页的时代，这些方法可以运行得比较好，但是在一些大型的应用里效果就会不尽如人意。</p>
<h3 data-id="heading-2">旧方法： 使用事件</h3>
<p>使用事件来报告异步结果，有很多明显的缺点：</p>
<ul>
<li>需要把代码放在各个事件处理器里，导致代码太过分散；</li>
<li>在定义处理函数和接收事件之间，可能会出现临界状态导致紊乱；</li>
<li>为了维持同步，常常需要定义一个类或者全局变量来维护状态。</li>
</ul>
<p>这些问题使得异步处理变得复杂，不信可以随便找一个<code>XMLHttpRequest</code>的代码看看。</p>
<h3 data-id="heading-3">旧方法： 使用回调</h3>
<p>另一个办法就是使用回调了，具有代表性的是使用一个匿名函数。看起来就像下面这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isUserTooYoung</span>(<span class="hljs-params">id, callback</span>) </span>&#123;
  openDatabase(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">db</span>) </span>&#123;
    getCollection(db, <span class="hljs-string">'users'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">col</span>) </span>&#123;
      find(col, &#123;<span class="hljs-string">'id'</span>: id&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">result</span>) </span>&#123;
        result.filter(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">user</span>) </span>&#123;
          callback(user.age < cutoffAge);
        &#125;);
      &#125;);
    &#125;);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种回调的方式也有两个问题：</p>
<ul>
<li>阅读理解复杂：使用的回调越多，嵌套就越深，代码就越不容易理解和分析；</li>
<li>错误处理复杂：例如，其中一个函数接收到了非法参数，会怎么样？</li>
</ul>
<h3 data-id="heading-4">使用Promise</h3>
<p><code>Promise</code>提供了一种标准化的方式去管理异步操作，以及处理异常。以刚才的代码为例，使用<code>Promise</code>可以更加简单：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isUserTooYoung</span>(<span class="hljs-params">id</span>) </span>&#123;
  <span class="hljs-keyword">return</span> openDatabase() <span class="hljs-comment">// returns a promise</span>
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">db</span>) </span>&#123;<span class="hljs-keyword">return</span> getCollection(db, <span class="hljs-string">'users'</span>);&#125;)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">col</span>) </span>&#123;<span class="hljs-keyword">return</span> find(col, &#123;<span class="hljs-string">'id'</span>: id&#125;);&#125;)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">user</span>) </span>&#123;<span class="hljs-keyword">return</span> user.age < cutoffAge;&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以把<code>Promise</code>理解为一个等待异步操作结束的对象，然后依次调用下一个函数。我们可以通过调用<code>.then()</code>方法来传入下一个函数。当异步函数结束时，它的结果会传给<code>Promise</code>，然后<code>Promise</code>再传给下一个函数（作为参数）。</p>
<p>注意可能有很多次<code>.then()</code>的调用，每一次调用都会等待上一个<code>Promise</code>结束，再执行下一个函数，有必要的话再把结果返回给<code>Promise</code>。这样我们就可以无痛地链接同步和异步调用了。它极大地简化了我们的代码，所以现在大多数新的规范都会从异步方法中返回<code>Promise</code>。</p>
<h2 data-id="heading-5">Promise 术语</h2>
<p>在使用<code>Promise</code>时，我们常常会接触到和回调或者其他异步操作相关的术语。</p>
<p>在下面的例子中，我们需要把一个设置图片地址的异步任务转换成<code>Promise</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadImage</span>(<span class="hljs-params">url</span>) </span>&#123;
  <span class="hljs-comment">// wrap image loading in a promise</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-comment">// A new promise is "pending"</span>
    <span class="hljs-keyword">var</span> image = <span class="hljs-keyword">new</span> Image();
    image.src = url;
    image.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// Resolving a promise changes its state to "fulfilled"</span>
      <span class="hljs-comment">// unless you resolve it with a rejected promise</span>
      resolve(image);
    &#125;;
    image.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// Rejecting a promise changes its state to "rejected"</span>
      reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Could not load image at '</span> + url));
    &#125;;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Promise</code>有以下几种状态：</p>
<ul>
<li>进行中(<code>Pending</code>) - 异步操作还在进行中，<code>Promise</code>的结果还没有出来</li>
<li>已完成(<code>Fulfilled</code>) - 异步操作已经结束，<code>Promise</code>获得了一个返回的值</li>
<li>已终止(<code>Rejected</code>) - 异步操作失败，<code>Promise</code>无法完成，同时会返回一个失败的原因</li>
</ul>
<p>除此之外还有另一个名词：<code>settled</code>，它指的是已执行的<code>Promise</code>，要么已成功(<code>Fulfilled</code>)，要么已失败(<code>Rejected</code>)。</p>
<h2 data-id="heading-6">如何使用promise</h2>
<h3 data-id="heading-7">写一个简单的promise</h3>
<p>我们通过一个典型片段，来学习如何创建一个<code>Promise</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-comment">// 做一些事情，异步操作等等</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-comment">/* 符合预期的结果 */</span>) &#123;
    resolve(<span class="hljs-string">"Stuff worked!"</span>);
  &#125;
  <span class="hljs-keyword">else</span> &#123;
    reject(<span class="hljs-built_in">Error</span>(<span class="hljs-string">"It broke"</span>));
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Promise</code>构造函数接收一个参数——包含两个参数的回调函数：resolve 和 reject。我们可以在回调函数中做各种事情，比如异步操作，如果一切正常就调用 resolve，否则调用 reject。</p>
<p>通过 reject 来处理错误的方式，有点像在普通 JavaScript 中常用的 throw 方法，但不是必须的。reject 出来的<code>Error</code>对象最大的好处是，能捕获跟踪堆栈，在调试的时候很有用。</p>
<p>创建好<code>Promise</code>后，我们来看一下如何使用它：</p>
<pre><code class="hljs language-js copyable" lang="js">promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">result</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Success!"</span>, result); <span class="hljs-comment">// "Stuff worked!"</span>
&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Failed!"</span>, err); <span class="hljs-comment">// Error: "It broke"</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.then()</code>方法包含两个参数，一个是成功的回调，一个是失败的回调。二者都是可选的，你可以只添加其中一个。
更常见的方式是通过<code>.then()</code>来处理成功结果，用<code>.catch()</code>来处理错误。</p>
<pre><code class="hljs language-js copyable" lang="js">promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">result</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Success!"</span>, result);
&#125;).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Failed!"</span>, error);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.catch()</code>方法也很简单，相等于在 then 方法中只传失败的回调——<code>then(undefined, func)</code>，不过可读性更强。<strong>需要注意上面两个例子执行的方式是不同的。</strong> 后者相当于：</p>
<pre><code class="hljs language-js copyable" lang="js">promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">response</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Success!"</span>, response);
&#125;).then(<span class="hljs-literal">undefined</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Failed!"</span>, error);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它们的差别很微妙，但很有用。在<code>Promise</code>中如果出现错误需要 reject，当前<code>then()</code>方法中没有 reject 回调的话，它会依次到下一个<code>then()</code>方法中去寻找（或者在<code>catch()</code>中去寻找，因为它俩等效）。</p>
<p>上面第一个例子用的是<code>then(func1, func2)</code>，func1 和 func2 二者只会被调用一个，不存在同时调用的情况。
但是在第二个例子<code>then(func1).then(undefined, func2)</code>，和第三个例子<code>then(func1).catch(func2)</code>中，如果 func1 出现了错误需要 reject ，fun2 也会被调用，因为它们是执行链上的两个独立的步骤。</p>
<h3 data-id="heading-8">Promise链：then 和 catch</h3>
<p>在一个<code>Promise</code>上，我们可以添加多个<code>then()</code>和<code>catch()</code>来形成一个<code>Promise</code>链。在<code>Promise</code>链中，前一个函数返回的结果就成为了下一个函数接收的参数。</p>
<h4 data-id="heading-9">Then</h4>
<p><code>then()</code>方法接收函数参数来处理<code>Promise</code>的返回结果。当一个<code>Promise</code>成功返回，<code>.then()</code>会提取它返回的值（即<code>Promise</code>中 resolve 的值），然后执行回调函数，并且把这个返回值包装在一个新的<code>Promise</code>中。</p>
<p>可以把<code>then()</code>理解为<code>try/catch</code>块中<code>try</code>的部分。</p>
<p>记住我们之前的例子里，连续调用多个操作。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isUserTooYoung</span>(<span class="hljs-params">id</span>) </span>&#123;
  <span class="hljs-keyword">return</span> openDatabase() <span class="hljs-comment">// returns a promise</span>
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">db</span>) </span>&#123;<span class="hljs-keyword">return</span> getCollection(db, <span class="hljs-string">'users'</span>);&#125;)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">col</span>) </span>&#123;<span class="hljs-keyword">return</span> find(col, &#123;<span class="hljs-string">'id'</span>: id&#125;);&#125;)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">user</span>) </span>&#123;<span class="hljs-keyword">return</span> user.age < cutoffAge;&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个<code>Promise</code>中返回的值，会通过<code>then()</code>方法来传递。<code>then()</code>方法又会继续返回，可以返回一个<code>Promise</code>继续传递下去，也可以返回一个值，这个值就成为了后面函数的参数。通过<code>then()</code>，你可以链接任意数量的操作。</p>
<h4 data-id="heading-10">Catch</h4>
<p><code>Promise</code> 还提供了简单的错误处理机制，当一个<code>Promise</code>被 reject（或者抛出异常），它就会直接跳到第一个<code>catch()</code>的地方调用函数。</p>
<p>可以把catch前面的那些调用链看成被包裹在隐形的<code>try&#123;&#125;</code>方法中了。</p>
<p>在下面的例子里，我们通过<code>loadImage()</code>加载一张图片，然后用<code>then()</code>执行一系列转换操作。如果某个地方报错了（包括原始<code>Promise</code>以及后续任何步骤），它会直接跳转到<code>catch()</code>语句。</p>
<p>只有最后一段<code>then()</code>语句会把图片加入DOM，在那之前，我们都返回同样的图片，以便传递给下一个<code>then()</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processImage</span>(<span class="hljs-params">imageName, domNode</span>) </span>&#123;
  <span class="hljs-comment">// returns an image for the next step. The function called in</span>
  <span class="hljs-comment">// the return statement must also return the image.</span>
  <span class="hljs-comment">// The same is true in each step below.</span>
  <span class="hljs-keyword">return</span> loadImage(imageName)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">image</span>) </span>&#123;
    <span class="hljs-comment">// returns an image for the next step.</span>
    <span class="hljs-keyword">return</span> scaleToFit(<span class="hljs-number">150</span>, <span class="hljs-number">225</span>, image);
  &#125;)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">image</span>) </span>&#123;
    <span class="hljs-comment">// returns the image for the next step.</span>
    <span class="hljs-keyword">return</span> watermark(<span class="hljs-string">'Google Chrome'</span>, image);
  &#125;)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">image</span>) </span>&#123;
    <span class="hljs-comment">// Attach the image to the DOM after all processing has been completed.</span>
    <span class="hljs-comment">// This step does not need to return in the function or here in the</span>
    <span class="hljs-comment">// .then() because we are not passing anything on</span>
    showImage(image);
  &#125;)
  .catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'We had a problem in running processImage'</span>, error);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在一个<code>Promise</code>链里，我们还可以通过 catch 方法去做一些恢复处理。例如，下面的代码里，如果在<code>loadImage</code>和<code>scaleToFit</code>阶段出了问题，我们就在 catch 方法中提供一个应急图片，继续传入后面的then方法中执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processImage</span>(<span class="hljs-params">imageName, domNode</span>) </span>&#123;
  <span class="hljs-keyword">return</span> loadImage(imageName)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">image</span>) </span>&#123;
    <span class="hljs-keyword">return</span> scaleToFit(<span class="hljs-number">150</span>, <span class="hljs-number">225</span>, image);
  &#125;)
  .catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Error in loadImage() or scaleToFit()'</span>, error);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Using fallback image'</span>);
    <span class="hljs-keyword">return</span> fallbackImage();
  &#125;)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">image</span>) </span>&#123;
    <span class="hljs-keyword">return</span> watermark(<span class="hljs-string">'Google Chrome'</span>, image);
  &#125;)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">image</span>) </span>&#123;
    showImage(image);
  &#125;)
  .catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'We had a problem with watermark() or showImage()'</span>, error);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意： Promise链在执行完<code>catch()</code>语句后仍然会继续往下执行，直到执行完最后一个<code>then()</code>或者<code>catch()</code>才停止。</p>
<h3 data-id="heading-11">同步操作</h3>
<p>在<code>Promise</code>执行的函数里，并不是都需要返回一个<code>Promise</code>。如果函数是同步的，可以直接执行，就没必要返回一个<code>Promise</code>。</p>
<p>下面的<code>scaleToFit</code>函数是图片处理链路上的一部分，它没有返回一个<code>Promise</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">scaleToFit</span>(<span class="hljs-params">width, height, image</span>) </span>&#123;
  image.width = width;
  image.height = height;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Scaling image to '</span> + width + <span class="hljs-string">' x '</span> + height);
  <span class="hljs-keyword">return</span> image;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，这个函数需要把传入的图片返回，让图片可以继续在下一个函数中传递。</p>
<h3 data-id="heading-12">Promise.all</h3>
<p>很多时候我们需要等一系列异步操作都成功完成之后，再执行某些动作。<code>Promise.all</code>会返回一个<code>Promise</code>，如果所有传入的<code>Promise</code>都完成了，就执行 resolve ；如果任何一个传入的<code>Promise</code>失败了，就执行 reject，同时会返回对应的错误原因。这对我们需要确保一组异步动作的完成后再进行下一步的情况非常有用。</p>
<p>在下面的例子里，<code>promise1</code> 和<code>promise2</code> 都返回<code>Promise</code>。我们希望在它们俩都加载完成后再继续。我们把两个<code>Promise</code>都传入到<code>Promise.all</code>中，如果任何一个请求失败了，<code>Promise.all</code>就会 reject 出错的<code>Promise</code>。如果两个请求都成功，<code>Promise.all</code>就会以数组形式 resolve 两个<code>Promise</code>的返回值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> promise1 = getJSON(<span class="hljs-string">'/users.json'</span>);
<span class="hljs-keyword">var</span> promise2 = getJSON(<span class="hljs-string">'/articles.json'</span>);
<span class="hljs-built_in">Promise</span>.all([promise1, promise2]) <span class="hljs-comment">// Array of promises to complete</span>
.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">results</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'all data has loaded'</span>);
&#125;)
.catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'one or more requests have failed: '</span> + error);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意： 即使其中一个<code>Promise</code> reject，导致整个<code>Promise.all</code> reject，剩下的<code>Promise</code>仍然会继续执行，只是不会通过<code>Promise.all</code>返回而已。</p>
<h3 data-id="heading-13">Promise.race</h3>
<p>另一个会被用到使用的方法是<code>Promise.race</code>，<code>Promise.race</code>同样接收一个<code>Promise</code>列表，然后当有一个<code>Promise</code>率先执行完成后，<code>Promise.race</code>也执行完成。如果最快的这个<code>Promise</code> resolve了，<code>Promise.race</code>就resolve相应的值，如果这个<code>Promise</code> reject了，<code>Promise.race</code>也以相应的原因 reject。</p>
<p>下面的代码展示了<code>Promise.race</code>的使用例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.race([promise1, promise2])
.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(value);
&#125;)
.catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">reason</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(reason);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果其中一个<code>Promise</code>先 resolve 了，就立即执行 then 代码块里的内容，并且把 resolve 的值记录下来。</p>
<p>如果其中一个<code>Promise</code>先 reject 了，就立即执行 catch 里面的内容，并且把原因记录下来。</p>
<p>顾名思义，<code>Promise.race</code>就是让<code>Promise</code>竞赛，谁先返回就用谁，这个看起来很吸引人，但也容易忽略一些问题，比如下面的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> promise1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-comment">// something that fails</span>
&#125;);
<span class="hljs-keyword">var</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-comment">// something that succeeds</span>
&#125;);
<span class="hljs-built_in">Promise</span>.race([promise1, promise2])
.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-comment">// Use whatever returns fastest</span>
&#125;)
.catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">reason</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(reason);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>乍一看，这段代码似乎在让两个<code>Promise</code>比赛，一个 reject，另一个 resolve，然后看谁第一个返回就用谁。但是，如果其中一个<code>Promise</code> reject了，<code>Promise.race</code>会立即 reject，即使另一个<code>Promise</code>很快就可以 resolve 了也没用。</p>
<p>因此，如果<code>promise1</code>在<code>promise2</code>之前 reject，即使<code>promise2</code>马上就会 resolve，<code>Promise.race</code>也会立刻 reject。<code>Promise.race</code>本身不能保证会返回第一个 resolve 的<code>Promise</code>。</p>
<p>另一种有意思的用法是下面这种：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> promise1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-comment">// get a resource from the Cache</span>
&#125;);
<span class="hljs-keyword">var</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-comment">// Fetch a resource from the network</span>
&#125;);
<span class="hljs-built_in">Promise</span>.race([promise1, promise2])
.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resource</span>) </span>&#123;
  <span class="hljs-comment">// Use the fastest returned resource</span>
&#125;)
.catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">reason</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(reason);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子看上去是想让网络资源和缓存资源去竞争，哪个先返回就用哪个。但是，<code>Cache API</code> 和 <code>Fetch API</code>都可能返回一个不是我们想要的结果（fetch在404的情况下也会返回，caches在拿不到资源的时候也可能返回错误的资源）。在这个例子里，如果缓存里的资源不可用，但由于它通常返回得更快，<code>Promise.race</code>就会用它返回的错误结果去解析，并且忽略掉可能马上就获取到的网络资源。</p>
<p>有关<a href="https://web.dev/offline-cookbook/#cache-and-network-race" target="_blank" rel="nofollow noopener noreferrer">Cache & network race</a>的部分，请参阅<a href="https://web.dev/offline-cookbook/" target="_blank" rel="nofollow noopener noreferrer">Offline Cookbook</a>。</p></div>  
</div>
            