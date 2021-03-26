
---
title: 'Promise对象'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9600'
author: 掘金
comments: false
date: Fri, 26 Mar 2021 01:55:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=9600'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. Promise的含义</h1>
<p><code>Promise</code> 是异步编程的一种解决方案，比传统的解决方案——回调函数和事件——更合理和更强大。它由社区最早提出和实现，<code>ES6</code> 将其写进了语言标准，统一了用法，原生提供了<code>Promise</code>对象。</p>
<p>所谓<code>Promise</code>，简单说就是一个容器，里面保存着某个未来才会结束的事件（通常是一个异步操作）的结果。从语法上说，<code>Promise</code> 是一个对象，从它可以获取异步操作的消息。<code>Promise</code> 提供统一的 <code>API</code>，各种异步操作都可以用同样的方法进行处理。</p>
<p><code>Promise</code>对象有以下两个特点。</p>
<p>(1) 对象的状态不受外界影响。 <code>Promise</code>对象代表一个异步操作，有三种状态：<code>pending</code>（进行中）、<code>fulfilled</code>（已成功）和<code>rejected</code>（已失败）。只有异步操作的结果，可以决定当前是哪一种状态，任何其他操作都无法改变这个状态。这也是<code>Promise</code>这个名字的由来，它的英语意思就是“承诺”，表示其他手段无法改变。</p>
<p>（2）一旦状态改变，就不会再变，任何时候都可以得到这个结果。<code>Promise</code>对象的状态改变，只有两种可能：从<code>pending</code>变为<code>fulfilled</code>和从<code>pending</code>变为<code>rejected</code>。只要这两种情况发生，状态就凝固了，不会再变了，会一直保持这个结果，这时就称为 <code>resolved</code>（已定型）。如果改变已经发生了，你再对<code>Promise</code>对象添加回调函数，也会立即得到这个结果。这与事件（<code>Event</code>）完全不同，事件的特点是，如果你错过了它，再去监听，是得不到结果的。</p>
<p>注意，为了行文方便，本章后面的<code>resolved</code>统一只指<code>fulfilled</code>状态，不包含<code>rejected</code>状态。</p>
<p>有了<code>Promise</code>对象，就可以将异步操作以同步操作的流程表达出来，避免了层层嵌套的回调函数(<code>回调地狱</code>)。此外，<code>Promise</code>对象提供统一的接口，使得控制异步操作更加容易。</p>
<p><code>Promise</code>也有一些缺点。首先，无法取消<code>Promise</code>，一旦新建它就会<code>立即执行</code>，无法中途取消。其次，如果不设置回调函数，<code>Promise</code>内部抛出的错误，不会反应到外部。第三，当处于<code>pending</code>状态时，无法得知目前进展到哪一个阶段（刚刚开始还是即将完成）。</p>
<p>如果某些事件不断地反复发生，一般来说，使用<a href="https://nodejs.org/api/stream.html" target="_blank" rel="nofollow noopener noreferrer"> Stream </a>模式是比部署<code>Promise</code>更好的选择。</p>
<h1 data-id="heading-1">2. 基本用法</h1>
<p>ES6 规定，<code>Promise</code>对象是一个<code>构造函数</code>，用来生成<code>Promise实例</code>。</p>
<p>下面代码创造了一个<code>Promise</code>实例。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-comment">//... some code</span>
    
    <span class="hljs-keyword">if</span> (<span class="hljs-comment">/* 异步操作成功 */</span>) &#123;
        resolve(value);
    &#125; <span class="hljs-keyword">else</span> &#123;
        reject(error);
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Promise</code>构造函数接受一个函数作为参数, 该函数称为<code>executor</code>函数，该函数的两个参数分别是<code>resolve</code>和<code>reject</code>。它们是两个函数，由JavaScript引擎提供，不用自己部署。</p>
<p><code>resolve</code>函数的作用是，将<code>Promise</code>对象的状态从“未完成”变成“成功”（即从pending变为resolved）,在异步操作成功时调用，并将异步操作的结果，作为参数传递出去；
<code>reject</code>函数的作用是，将<code>Promise</code>对象的状态从“未完成”变成“失败”（即从pending变为rejected），在异步操作失败时调用，并将异步操作报出的错误，作为参数传递出去。</p>
<p><code>Promise</code>实例生成以后，可以用<code>then</code>方法分别指定<code>resolved</code>状态和<code>rejected</code>状态的回调函数。</p>
<pre><code class="hljs language-js copyable" lang="js">promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-comment">//success</span>
&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-comment">//failure</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>then</code>方法可以接受两个回调函数作为参数。第一个回调函数是<code>Promise</code>对象的状态变为<code>resolved</code>时调用，第二个回调函数是<code>Promise</code>对象的状态变为<code>rejected</code>时调用。这两个函数都是可选的，不一定要提供。它们都接受<code>Promise</code>对象传出的值作为参数。</p>
<p>下面是一个<code>Promise</code>对象的简单例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//定时器的第三个参数'done',是给resolve函数传递的参数。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timeout</span>(<span class="hljs-params">ms</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(resolve, ms, <span class="hljs-string">'done'</span>);
    &#125;);
&#125;

timeout(<span class="hljs-number">100</span>).then(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(value);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>timeout</code>方法返回一个<code>Promise</code>实例，表示一段时间以后才会发生的结果。过了指定的时间(<code>ms</code>参数)以后，<code>Promise</code>实例的状态变为<code>resolved</code>，就会触发<code>then</code>方法绑定的回调函数。</p>
<p>Promise 新建后就会立即执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Promise'</span>);
    resolve();
&#125;);

promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'resolved'</span>);
&#125;);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hi!'</span>);

<span class="hljs-comment">//Promise</span>
<span class="hljs-comment">//Hi!</span>
<span class="hljs-comment">//resolved</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，Promise新建后立即执行，所以首先输出的是<code>Promise</code>。然后，<code>then</code>方法指定的回调函数，将在当前脚本所有同步任务执行完才会执行，所以<code>resolved</code>最后输出。</p>
<p>下面是异步加载图片的例子。</p>
<pre><code class="hljs language-js copyable" lang="js">fucntion <span class="hljs-function"><span class="hljs-title">loadImageAsync</span>(<span class="hljs-params">url</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
        <span class="hljs-keyword">const</span> image = <span class="hljs-keyword">new</span> Image();
        
        iamge.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            resolve(image);
        &#125;;
        
        image.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Could not load image at'</span> + url));
        &#125;;
        
        image.src = url;
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，使用<code>Promise</code>包装了一个图片加载的异步操作。如果加载成功，就调用<code>resolve</code>方法，否则就调用<code>reject</code>方法。</p>
<p>下面是一个用<code>Promise</code>对象实现的 Ajax 操作的例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> getJSON = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">url</span>)</span>&#123;
    <span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve,reject</span>)</span>&#123;
        <span class="hljs-keyword">const</span> handler = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
             <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.readyState !== <span class="hljs-number">4</span>) &#123;
                 <span class="hljs-keyword">return</span>;
             &#125;
             <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-number">200</span>) &#123;
                 resolve(<span class="hljs-built_in">this</span>.response);
             &#125; <span class="hljs-keyword">else</span> &#123;
                 reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-built_in">this</span>.statusText));
             &#125;
        &#125;;
        <span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> XMLHttpRequest();
        client.open(<span class="hljs-string">"GET"</span>,url);
        client.onreadystatechange = handler;
        client.responseType = <span class="hljs-string">"json"</span>;
        client.setRequestHeader(<span class="hljs-string">"Accept"</span>,<span class="hljs-string">"application/json"</span>);
        client.send();
  
    &#125;);
    <span class="hljs-keyword">return</span> promise;
&#125;;

getJSON(<span class="hljs-string">"/posts.json"</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">result</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Contents:'</span> + result);
&#125;,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'出错了'</span>,error);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>getJSON</code>是对XMLHttpRequest 对象的封装，用于发出一个针对JSON数据的 HTTP 请求，并且返回一个<code>Promise</code>对象。需要注意的是，在<code>getJSON</code>内部，<code>resolve</code>函数和<code>reject</code>函数调用时，都带有参数。</p>
<p>如果调用<code>resolve</code>函数和<code>reject</code>函数时带有参数，那么它们的参数会被传递给回调函数。<code>reject</code>函数的参数通常是<code>Error</code>对象的实例，表示抛出的错误；<code>resolve</code>函数的参数除了正常的值以外，还可能是另一个Promise实例，比如像下面这样。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-comment">//...</span>
&#125;);

<span class="hljs-keyword">const</span> p2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-comment">//...</span>
    resolve(p1);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>p1</code>和<code>p2</code>都是 <code>Promise</code> 的实例，但是<code>p2</code>的<code>resolve</code>方法将<code>p1</code>作为参数，即一个异步操作的结果是返回另一个异步操作。</p>
<p><code>注意</code>，这时<code>p1</code>的状态就会传递给<code>p2</code>，也就是说，<code>p1</code>的状态决定了<code>p2</code>的状态。如果<code>p1</code>的状态是<code>pending</code>，那么<code>p2</code>的回调函数就会等待<code>p1</code>的状态改变；如果<code>p1</code>的状态已经是<code>resolved</code>或者<code>rejected</code>，那么<code>p2</code>的回调函数将会立刻执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'fail'</span>)), <span class="hljs-number">3000</span>);
&#125;);

<span class="hljs-keyword">const</span> p2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    seTimeout(<span class="hljs-function">()=></span> resolve(p1), <span class="hljs-number">1000</span>);
&#125;);

p2
  .then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> <span class="hljs-built_in">console</span>.log(result))
  .catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> <span class="hljs-built_in">console</span>.log(error))
  
<span class="hljs-comment">// Error: fail</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>p1</code>是一个 <code>Promise</code>，3 秒之后变为<code>rejected</code>。<code>p2</code>的状态在 1 秒之后改变，<code>resolve</code>方法返回的是<code>p1</code>。由于<code>p2</code>返回的是另一个 <code>Promise</code>，导致<code>p2</code>自己的状态无效了，由<code>p1</code>的状态决定<code>p2</code>的状态。所以，后面的<code>then</code>语句都变成针对后者<code>（p1）</code>。又过了 2 秒，<code>p1</code>变为<code>rejected</code>，导致触发<code>catch</code>方法指定的回调函数。</p>
<p><code>注意</code>，调用<code>resolve</code>或<code>reject</code>并不会终结 <code>Promise</code> 的<code>参数函数</code>的执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(<span class="hljs-number">1</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
&#125;).then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(result);
&#125;);

<span class="hljs-comment">//2</span>
<span class="hljs-comment">//1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，调用<code>resolve(1)</code>以后，后面的<code>console.log(2)</code>还是会执行，并且会首先打印出来。这是因为立即 <code>resolved</code> 的 <code>Promise</code> 是在本轮事件循环的末尾执行，总是晚于本轮循环的同步任务。</p>
<p>一般来说，调用<code>resolve</code>或<code>reject</code>以后，<code>Promise</code> 的使命就完成了，后继操作应该放到<code>then</code>方法里面，而不应该直接写在<code>resolve</code>或<code>reject</code>的后面。所以，最好在它们前面加上<code>return</code>语句，这样就不会有意外。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> resolve(<span class="hljs-number">1</span>);
  <span class="hljs-comment">// 后面的语句不会执行</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">3. Promise.prototype.then()</h1>
<p>Promise 实例具有<code>then</code>方法，也就是说，<code>then</code>方法是定义在原型对象<code>Promise.prototype</code>上的。它的作用是为 Promise 实例添加状态改变时的回调函数。前面说过，<code>then</code>方法的第一个参数是<code>resolved</code>状态的回调函数，第二个参数是<code>rejected</code>状态的回调函数，它们都是可选的。</p>
<p><code>then</code>方法返回的是一个<code>新</code>的<code>Promise实例</code>（注意，不是原来那个Promise实例）。因此可以采用<code>链式</code>写法，即<code>then</code>方法后面再调用另一个<code>then</code>方法。</p>
<pre><code class="hljs language-js copyable" lang="js">getJSON(<span class="hljs-string">"/posts.json"</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">json</span>) </span>&#123;
    <span class="hljs-keyword">return</span> json.post;
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">post</span>) </span>&#123;
    <span class="hljs-comment">//...</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码使用<code>then</code>方法，依次指定了两个回调函数。第一个回调函数完成以后，会将返回结果作为参数，传入第二个回调函数。</p>
<p>采用链式的then，可以指定一组按照次序调用的回调函数。这时，前一个回调函数，有可能返回的还是一个Promise对象（即有异步操作），这时后一个回调函数，就会等待该Promise对象的状态发生变化，才会被调用。</p>
<pre><code class="hljs language-js copyable" lang="js">getJSON(<span class="hljs-string">"/post/1.json"</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">post</span>) </span>&#123;
  <span class="hljs-keyword">return</span> getJSON(post.commentURL);
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">comments</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"resolved: "</span>, comments);
&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"rejected: "</span>, err);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，第一个<code>then</code>方法指定的回调函数，返回的是另一个Promise对象。这时，第二个<code>then</code>方法指定的回调函数，就会等待这个新的Promise对象状态发生变化。如果变为<code>resolved</code>，就调用第一个回调函数，如果状态变为<code>rejected</code>，就调用第二个回调函数。</p>
<p>如果采用箭头函数，上面的代码可以写得更简洁。</p>
<pre><code class="hljs language-js copyable" lang="js">getJSON(<span class="hljs-string">"/post/1.json"</span>).then(
  <span class="hljs-function"><span class="hljs-params">post</span> =></span> getJSON(post.commentURL)
).then(
  <span class="hljs-function"><span class="hljs-params">comments</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"resolved: "</span>, comments),
  <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"rejected: "</span>, err)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">4. Promise.prototype.catch()</h1>
<p><code>Promise.prototype.catch()</code>方法是<code>.then(null, rejection)</code>或<code>.then(undefined, rejection)</code>的别名，用于指定发生错误时的回调函数。</p>
<pre><code class="hljs language-js copyable" lang="js">getJSON(<span class="hljs-string">'/posts.json'</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">posts</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-comment">// 处理 getJSON 和 前一个回调函数运行时发生的错误</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'发生错误！'</span>, error);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>getJSON()</code>方法返回一个 Promise 对象，如果该对象状态变为<code>resolved</code>，则会调用<code>then()</code>方法指定的回调函数；如果异步操作抛出错误，状态就会变为<code>rejected</code>，就会调用<code>catch()</code>方法指定的回调函数，处理这个错误。另外，<code>then()</code>方法指定的回调函数，如果运行中抛出错误，也会被<code>catch()</code>方法捕获。</p>
<pre><code class="hljs language-js copyable" lang="js">p.then(<span class="hljs-function">(<span class="hljs-params">val</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'fulfilled:'</span>, val))
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'rejected'</span>, err));

<span class="hljs-comment">// 等同于</span>
p.then(<span class="hljs-function">(<span class="hljs-params">val</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'fulfilled:'</span>, val))
  .then(<span class="hljs-literal">null</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"rejected:"</span>, err));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是一个例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'test'</span>);
&#125;);
promise.catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(error);
&#125;);
<span class="hljs-comment">// Error: test</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>promise</code>抛出一个错误，就被<code>catch()</code>方法指定的回调函数捕获。注意，上面的写法与下面两种写法是等价的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 写法一</span>
<span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'test'</span>);
  &#125; <span class="hljs-keyword">catch</span>(e) &#123;
    reject(e);
  &#125;
&#125;);
promise.catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(error);
&#125;);

<span class="hljs-comment">// 写法二</span>
<span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'test'</span>));
&#125;);
promise.catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(error);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比较上面两种写法，可以发现<code>reject()</code>方法的作用，等同于抛出错误。</p>
<p>如果 Promise 状态已经变成<code>resolved</code>，再抛出错误是无效的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  resolve(<span class="hljs-string">'ok'</span>);
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'test'</span>);
&#125;);
promise
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123; <span class="hljs-built_in">console</span>.log(value) &#125;)
  .catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123; <span class="hljs-built_in">console</span>.log(error) &#125;);
<span class="hljs-comment">// ok</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，Promise 在resolve语句后面，再抛出错误，不会被捕获，等于没有抛出。因为 Promise 的状态一旦改变，就永久保持该状态，不会再变了。</p>
<p>Promise 对象的错误具有“冒泡”性质，会一直向后传递，直到被捕获为止。也就是说，错误总是会被下一个catch语句捕获。</p>
<pre><code class="hljs language-js copyable" lang="js">getJSON(<span class="hljs-string">'/post/1.json'</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">post</span>) </span>&#123;
  <span class="hljs-keyword">return</span> getJSON(post.commentURL);
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">comments</span>) </span>&#123;
  <span class="hljs-comment">// some code</span>
&#125;).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-comment">// 处理前面三个Promise产生的错误</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，一共有三个 Promise 对象：一个由<code>getJSON()</code>产生，两个由<code>then()</code>产生。它们之中任何一个抛出的错误，都会被最后一个<code>catch()</code>捕获。</p>
<p>一般来说，不要在<code>then()</code>方法里面定义 <code>Reject</code> 状态的回调函数（即<code>then</code>的第二个参数），总是使用<code>catch</code>方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// bad</span>
promise
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-comment">// success</span>
  &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123;
    <span class="hljs-comment">// error</span>
  &#125;);

<span class="hljs-comment">// good</span>
promise
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123; <span class="hljs-comment">//cb</span>
    <span class="hljs-comment">// success</span>
  &#125;)
  .catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123;
    <span class="hljs-comment">// error</span>
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，第二种写法要好于第一种写法，理由是第二种写法可以捕获前面then方法执行中的错误，也更接近同步的写法（try/catch）。因此，建议总是使用catch()方法，而不使用then()方法的第二个参数。</p>
<p>跟传统的try/catch代码块不同的是，如果没有使用catch()方法指定错误处理的回调函数，Promise 对象抛出的错误不会传递到外层代码，即不会有任何反应。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> someAsyncThing = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-comment">// 下面一行会报错，因为x没有声明</span>
    resolve(x + <span class="hljs-number">2</span>);
  &#125;);
&#125;;

someAsyncThing().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'everything is great'</span>);
&#125;);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-number">123</span>) &#125;, <span class="hljs-number">2000</span>);
<span class="hljs-comment">// Uncaught (in promise) ReferenceError: x is not defined</span>
<span class="hljs-comment">// 123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，someAsyncThing()函数产生的 Promise 对象，内部有语法错误。浏览器运行到这一行，会打印出错误提示ReferenceError: x is not defined，但是不会退出进程、终止脚本执行，2 秒之后还是会输出123。这就是说，Promise 内部的错误不会影响到 Promise 外部的代码，通俗的说法就是“Promise 会吃掉错误”。</p>
<p>这个脚本放在服务器执行，退出码就是<code>0</code>（即表示执行成功）。不过，<code>Node.js</code> 有一个<code>unhandledRejection</code>事件，专门监听未捕获的<code>reject</code>错误，上面的脚本会触发这个事件的监听函数，可以在监听函数里面抛出错误。</p>
<pre><code class="hljs language-js copyable" lang="js">process.on(<span class="hljs-string">'unhandledRejection'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err, p</span>) </span>&#123;
  <span class="hljs-keyword">throw</span> err;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>unhandledRejection</code>事件的监听函数有两个参数，第一个是错误对象，第二个是报错的 Promise 实例，它可以用来了解发生错误的环境信息。</p>
<p>注意，<code>Node</code> 有计划在未来废除<code>unhandledRejection</code>事件。如果 Promise 内部有未捕获的错误，会直接终止进程，并且进程的退出码不为 <code>0</code>。</p>
<p>再看下面的例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
  resolve(<span class="hljs-string">'ok'</span>);
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'test'</span>) &#125;, <span class="hljs-number">0</span>)
&#125;);
promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123; <span class="hljs-built_in">console</span>.log(value) &#125;);
<span class="hljs-comment">// ok</span>
<span class="hljs-comment">// Uncaught Error: test</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，Promise 指定在下一轮“事件循环”再抛出错误。到了那个时候，Promise 的运行已经结束了，所以这个错误是在 Promise 函数体外抛出的，会冒泡到最外层，成了未捕获的错误。</p>
<p>一般总是建议，Promise 对象后面要跟<code>catch()</code>方法，这样可以处理 Promise 内部发生的错误。<code>catch()</code>方法返回的还是一个 Promise 对象，因此后面还可以接着调用<code>then()</code>方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> someAsyncThing = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-comment">// 下面一行会报错，因为x没有声明</span>
    resolve(x + <span class="hljs-number">2</span>);
  &#125;);
&#125;;

someAsyncThing()
.catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'oh no'</span>, error);
&#125;)
.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'carry on'</span>);
&#125;);
<span class="hljs-comment">// oh no [ReferenceError: x is not defined]</span>
<span class="hljs-comment">// carry on</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码运行完<code>catch()</code>方法指定的回调函数，会接着运行后面那个<code>then()</code>方法指定的回调函数。如果没有报错，则会跳过<code>catch()</code>方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve()
.catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'oh no'</span>, error);
&#125;)
.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'carry on'</span>);
&#125;);
<span class="hljs-comment">// carry on</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码因为没有报错，跳过了<code>catch()</code>方法，直接执行后面的<code>then()</code>方法。此时，要是<code>then()</code>方法里面报错，就与前面的<code>catch()</code>无关了。</p>
<p><code>catch()</code>方法之中，还能再抛出错误。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> someAsyncThing = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-comment">// 下面一行会报错，因为x没有声明</span>
    resolve(x + <span class="hljs-number">2</span>);
  &#125;);
&#125;;

someAsyncThing().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> someOtherAsyncThing();
&#125;).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'oh no'</span>, error);
  <span class="hljs-comment">// 下面一行会报错，因为 y 没有声明</span>
  y + <span class="hljs-number">2</span>;
&#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'carry on'</span>);
&#125;);
<span class="hljs-comment">// oh no [ReferenceError: x is not defined]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>catch()</code>方法抛出一个错误，因为后面没有别的<code>catch()</code>方法了，导致这个错误不会被捕获，也不会传递到外层。如果改写一下，结果就不一样了。</p>
<pre><code class="hljs language-js copyable" lang="js">someAsyncThing().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> someOtherAsyncThing();
&#125;).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'oh no'</span>, error);
  <span class="hljs-comment">// 下面一行会报错，因为y没有声明</span>
  y + <span class="hljs-number">2</span>;
&#125;).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'carry on'</span>, error);
&#125;);
<span class="hljs-comment">// oh no [ReferenceError: x is not defined]</span>
<span class="hljs-comment">// carry on [ReferenceError: y is not defined]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，第二个<code>catch()</code>方法用来捕获前一个<code>catch()</code>方法抛出的错误。</p>
<h1 data-id="heading-4">5. Promise.prototype.finally()</h1>
<p><code>finally()</code>方法用于指定不管 Promise 对象最后状态如何，都会执行的操作。该方法是 ES2018 引入标准的。</p>
<pre><code class="hljs language-js copyable" lang="js">promise
.then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;···&#125;)
.catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;···&#125;)
.finally(<span class="hljs-function">() =></span> &#123;···&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，不管promise最后的状态，在执行完<code>then</code>或<code>catch</code>指定的回调函数以后，都会执行<code>finally</code>方法指定的回调函数。</p>
<p>下面是一个例子，服务器使用 Promise 处理请求，然后使用<code>finally</code>方法关掉服务器。</p>
<pre><code class="hljs language-js copyable" lang="js">server.listen(port)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// ...</span>
  &#125;)
  .finally(server.stop);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>finally</code>方法的回调函数不接受任何参数，这意味着没有办法知道，前面的 Promise 状态到底是<code>fulfilled</code>还是<code>rejected</code>。这表明，<code>finally</code>方法里面的操作，应该是与状态无关的，不依赖于 Promise 的执行结果。</p>
<p><code>finally</code>本质上是<code>then</code>方法的特例。</p>
<pre><code class="hljs language-js copyable" lang="js">promise
.finally(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 语句</span>
&#125;);

<span class="hljs-comment">// 等同于</span>
promise
.then(
  <span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
    <span class="hljs-comment">// 语句</span>
    <span class="hljs-keyword">return</span> result;
  &#125;,
  <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-comment">// 语句</span>
    <span class="hljs-keyword">throw</span> error;
  &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，如果不使用<code>finally</code>方法，同样的语句需要为成功和失败两种情况各写一次。有了<code>finally</code>方法，则只需要写一次。</p>
<p>它的实现也很简单。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.finally = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">callback</span>) </span>&#123;
  <span class="hljs-keyword">let</span> P = <span class="hljs-built_in">this</span>.constructor;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(
    <span class="hljs-function"><span class="hljs-params">value</span>  =></span> P.resolve(callback()).then(<span class="hljs-function">() =></span> value),
    <span class="hljs-function"><span class="hljs-params">reason</span> =></span> P.resolve(callback()).then(<span class="hljs-function">() =></span> &#123; <span class="hljs-keyword">throw</span> reason &#125;)
  );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，不管前面的 Promise 是<code>fulfilled</code>还是<code>rejected</code>，都会执行回调函数<code>callback</code>。</p>
<p>从上面的实现还可以看到，<code>finally</code>方法总是会返回原来的值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// resolve 的值是 undefined</span>
<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">2</span>).then(<span class="hljs-function">() =></span> &#123;&#125;, <span class="hljs-function">() =></span> &#123;&#125;)

<span class="hljs-comment">// resolve 的值是 2</span>
<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">2</span>).finally(<span class="hljs-function">() =></span> &#123;&#125;)

<span class="hljs-comment">// reject 的值是 undefined</span>
<span class="hljs-built_in">Promise</span>.reject(<span class="hljs-number">3</span>).then(<span class="hljs-function">() =></span> &#123;&#125;, <span class="hljs-function">() =></span> &#123;&#125;)

<span class="hljs-comment">// reject 的值是 3</span>
<span class="hljs-built_in">Promise</span>.reject(<span class="hljs-number">3</span>).finally(<span class="hljs-function">() =></span> &#123;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">6. Promise.all()</h1>
<p><code>Promise.all()</code>方法用于将多个 Promise 实例，包装成一个新的 Promise 实例。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.all([p1, p2, p3]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>Promise.all()</code>方法接受一个数组作为参数，<code>p1</code>、<code>p2</code>、<code>p3</code>都是 Promise 实例，如果不是，就会先调用下面讲到的<code>Promise.resolve</code>方法，将参数转为 Promise 实例，再进一步处理。另外，<code>Promise.all()</code>方法的参数可以不是数组，但必须具有 Iterator 接口，且返回的每个成员都是 Promise 实例。</p>
<p><code>p</code>的状态由<code>p1</code>、<code>p2</code>、<code>p3</code>决定，分成两种情况。</p>
<p>（1）只有<code>p1</code>、<code>p2</code>、<code>p3</code>的状态都变成<code>fulfilled</code>，<code>p</code>的状态才会变成<code>fulfilled</code>，此时<code>p1</code>、<code>p2</code>、<code>p3</code>的返回值组成一个数组，传递给<code>p</code>的回调函数。</p>
<p>（2）只要<code>p1</code>、<code>p2</code>、<code>p3</code>之中有一个被<code>rejected</code>，<code>p</code>的状态就变成<code>rejected</code>，此时第一个被<code>reject</code>的实例的返回值，会传递给<code>p</code>的回调函数。</p>
<p>下面是一个具体的例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 生成一个Promise对象的数组</span>
<span class="hljs-keyword">const</span> promises = [<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">7</span>, <span class="hljs-number">11</span>, <span class="hljs-number">13</span>].map(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">id</span>) </span>&#123;
  <span class="hljs-keyword">return</span> getJSON(<span class="hljs-string">'/post/'</span> + id + <span class="hljs-string">".json"</span>);
&#125;);

<span class="hljs-built_in">Promise</span>.all(promises).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">posts</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">reason</span>)</span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>promises</code>是包含 6 个 Promise 实例的数组，只有这 6 个实例的状态都变成<code>fulfilled</code>，或者其中有一个变为<code>rejected</code>，才会调用<code>Promise.all</code>方法后面的回调函数。</p>
<p>下面是另一个例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> databasePromise = connectDatabase();

<span class="hljs-keyword">const</span> booksPromise = databasePromise
  .then(findAllBooks);

<span class="hljs-keyword">const</span> userPromise = databasePromise
  .then(getCurrentUser);

<span class="hljs-built_in">Promise</span>.all([
  booksPromise,
  userPromise
])
.then(<span class="hljs-function">(<span class="hljs-params">[books, user]</span>) =></span> pickTopRecommendations(books, user));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>booksPromise</code>和<code>userPromise</code>是两个异步操作，只有等到它们的结果都返回了，才会触发<code>pickTopRecommendations</code>这个回调函数。</p>
<p>注意，如果作为参数的 Promise 实例，自己定义了<code>catch</code>方法，那么它一旦被<code>rejected</code>，并不会触发<code>Promise.all()</code>的<code>catch</code>方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  resolve(<span class="hljs-string">'hello'</span>);
&#125;)
.then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> result)
.catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> e);

<span class="hljs-keyword">const</span> p2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'报错了'</span>);
&#125;)
.then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> result)
.catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> e);

<span class="hljs-built_in">Promise</span>.all([p1, p2])
.then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> <span class="hljs-built_in">console</span>.log(result))
.catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> <span class="hljs-built_in">console</span>.log(e));
<span class="hljs-comment">// ["hello", Error: 报错了]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>p1</code>会<code>resolved</code>，<code>p2</code>首先会<code>rejected</code>，但是<code>p2</code>有自己的<code>catch</code>方法，该方法返回的是一个新的 Promise 实例，<code>p2</code>指向的实际上是这个实例。该实例执行完<code>catch</code>方法后，也会变成<code>resolved</code>，导致<code>Promise.all()</code>方法参数里面的两个实例都会<code>resolved</code>，因此会调用<code>then</code>方法指定的回调函数，而不会调用<code>catch</code>方法指定的回调函数。</p>
<p>如果<code>p2</code>没有自己的<code>catch</code>方法，就会调用<code>Promise.all()</code>的<code>catch</code>方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  resolve(<span class="hljs-string">'hello'</span>);
&#125;)
.then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> result);

<span class="hljs-keyword">const</span> p2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'报错了'</span>);
&#125;)
.then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> result);

<span class="hljs-built_in">Promise</span>.all([p1, p2])
.then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> <span class="hljs-built_in">console</span>.log(result))
.catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> <span class="hljs-built_in">console</span>.log(e));
<span class="hljs-comment">// Error: 报错了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">7. Promise.race()</h1>
<p><code>Promise.race()</code>方法同样是将多个 Promise 实例，包装成一个新的 Promise 实例。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.race([p1, p2, p3]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，只要<code>p1</code>、<code>p2</code>、<code>p3</code>之中有一个实例<code>率先</code>改变状态，<code>p</code>的状态就跟着改变。那个<code>率先</code>改变的 Promise 实例的返回值，就传递给<code>p</code>的回调函数。</p>
<p><code>Promise.race()</code>方法的参数与<code>Promise.all()</code>方法一样，如果不是 Promise 实例，就会先调用下面讲到的<code>Promise.resolve()</code>方法，将参数转为 Promise 实例，再进一步处理。</p>
<p>下面是一个例子，如果指定时间内没有获得结果，就将 Promise 的状态变为<code>reject</code>，否则变为<code>resolve</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.race([
    fetch(<span class="hljs-string">'/resource-that-may-take-a-while'</span>),
    <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
         <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'request timeout'</span>)), <span class="hljs-number">5000</span>)
    &#125;)
]);

p
.then(<span class="hljs-built_in">console</span>.log)
.catch(<span class="hljs-built_in">console</span>.error);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，如果 5 秒之内<code>fetch</code>方法无法返回结果，变量<code>p</code>的状态就会变为<code>rejected</code>，从而触发<code>catch</code>方法指定的回调函数。</p>
<h1 data-id="heading-7">8. Promise.allSettled()</h1>
<p><code>Promise.allSettled()</code>方法接受一组 Promise 实例作为参数，包装成一个新的 Promise 实例。只有等到所有这些参数实例都返回结果，不管是<code>fulfilled</code>还是<code>rejected</code>，包装实例才会结束。该方法由 ES2020 引入。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promises = [
  fetch(<span class="hljs-string">'/api-1'</span>),
  fetch(<span class="hljs-string">'/api-2'</span>),
  fetch(<span class="hljs-string">'/api-3'</span>),
];

<span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.allSettled(promises);
removeLoadingIndicator();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码对服务器发出三个请求，等到三个请求都结束，不管请求成功还是失败，加载的滚动图标就会消失。</p>
<p>该方法返回的新的 Promise 实例，一旦结束，状态总是<code>fulfilled</code>，不会变成<code>rejected</code>。状态变成<code>fulfilled</code>后，Promise 的监听函数接收到的参数是一个数组，每个成员对应一个传入Promise.allSettled()的 Promise 实例。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> resolved = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">42</span>);
<span class="hljs-keyword">const</span> rejected = <span class="hljs-built_in">Promise</span>.reject(-<span class="hljs-number">1</span>);

<span class="hljs-keyword">const</span> allSettledPromise = <span class="hljs-built_in">Promise</span>.allSettled([resolved, rejected]);

allSettledPromise.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">results</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(results);
&#125;);
<span class="hljs-comment">// [</span>
<span class="hljs-comment">//    &#123; status: 'fulfilled', value: 42 &#125;,</span>
<span class="hljs-comment">//    &#123; status: 'rejected', reason: -1 &#125;</span>
<span class="hljs-comment">// ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，Promise.allSettled()的返回值allSettledPromise，状态只可能变成fulfilled。它的监听函数接收到的参数是数组results。该数组的每个成员都是一个对象，对应传入Promise.allSettled()的两个 Promise 实例。每个对象都有status属性，该属性的值只可能是字符串fulfilled或字符串rejected。fulfilled时，对象有value属性，rejected时有reason属性，对应两种状态的返回值。</p>
<p>下面是返回值用法的例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promises = [ fetch(<span class="hljs-string">'index.html'</span>), fetch(<span class="hljs-string">'https://does-not-exist/'</span>) ];
<span class="hljs-keyword">const</span> results = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.allSettled(promises);

<span class="hljs-comment">// 过滤出成功的请求</span>
<span class="hljs-keyword">const</span> successfulPromises = results.filter(<span class="hljs-function"><span class="hljs-params">p</span> =></span> p.status === <span class="hljs-string">'fulfilled'</span>);

<span class="hljs-comment">// 过滤出失败的请求，并输出原因</span>
<span class="hljs-keyword">const</span> errors = results
  .filter(<span class="hljs-function"><span class="hljs-params">p</span> =></span> p.status === <span class="hljs-string">'rejected'</span>)
  .map(<span class="hljs-function"><span class="hljs-params">p</span> =></span> p.reason);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有时候，我们不关心异步操作的结果，只关心这些操作有没有结束。这时，<code>Promise.allSettled()</code>方法就很有用。如果没有这个方法，想要确保所有操作都结束，就很麻烦。<code>Promise.all()</code>方法无法做到这一点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> urls = [ <span class="hljs-comment">/* ... */</span> ];
<span class="hljs-keyword">const</span> requests = urls.map(<span class="hljs-function"><span class="hljs-params">x</span> =></span> fetch(x));

<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all(requests);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'所有请求都成功。'</span>);
&#125; <span class="hljs-keyword">catch</span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'至少一个请求失败，其他请求可能还没结束。'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>Promise.all()</code>无法确定所有请求都结束。想要达到这个目的，写起来很麻烦，有了<code>Promise.allSettled()</code>，这就很容易了。</p>
<h1 data-id="heading-8">9. Promise.any()</h1>
<p>ES2021 引入了<code>Promise.any()</code>方法。该方法接受一组 Promise 实例作为参数，包装成一个新的 Promise 实例返回。只要参数实例有一个变成fulfilled状态，包装实例就会变成fulfilled状态；如果所有参数实例都变成rejected状态，包装实例就会变成rejected状态。</p>
<p>Promise.any()跟Promise.race()方法很像，只有一点不同，就是不会因为某个 Promise 变成<code>rejected</code>状态而结束。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promises = [
  fetch(<span class="hljs-string">'/endpoint-a'</span>).then(<span class="hljs-function">() =></span> <span class="hljs-string">'a'</span>),
  fetch(<span class="hljs-string">'/endpoint-b'</span>).then(<span class="hljs-function">() =></span> <span class="hljs-string">'b'</span>),
  fetch(<span class="hljs-string">'/endpoint-c'</span>).then(<span class="hljs-function">() =></span> <span class="hljs-string">'c'</span>),
];
<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-keyword">const</span> first = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.any(promises);
  <span class="hljs-built_in">console</span>.log(first);
&#125; <span class="hljs-keyword">catch</span> (error) &#123;
  <span class="hljs-built_in">console</span>.log(error);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>Promise.any()</code>方法的参数数组包含三个 Promise 操作。其中只要有一个变成<code>fulfilled</code>，<code>Promise.any()</code>返回的 Promise 对象就变成<code>fulfilled</code>。如果所有三个操作都变成<code>rejected</code>，那么<code>await</code>命令就会抛出错误。</p>
<p><code>Promise.any()</code>抛出的错误，不是一个一般的错误，而是一个 <code>AggregateError</code> 实例。它相当于一个数组，每个成员对应一个被<code>rejected</code>的操作所抛出的错误。下面是 <code>AggregateError</code> 的实现示例。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> AggregateError() <span class="hljs-keyword">extends</span> <span class="hljs-built_in">Array</span> -> AggregateError

<span class="hljs-keyword">const</span> err = <span class="hljs-keyword">new</span> AggregateError();
err.push(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"first error"</span>));
err.push(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"second error"</span>));
<span class="hljs-keyword">throw</span> err;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>捕捉错误时，如果不用<code>try...catch</code>结构和 <code>await</code> 命令，可以像下面这样写。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.any(promises).then(
  <span class="hljs-function">(<span class="hljs-params">first</span>) =></span> &#123;
    <span class="hljs-comment">// Any of the promises was fulfilled.</span>
  &#125;,
  <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
    <span class="hljs-comment">// All of the promises were rejected.</span>
  &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是一个例子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> resolved = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">42</span>);
<span class="hljs-keyword">var</span> rejected = <span class="hljs-built_in">Promise</span>.reject(-<span class="hljs-number">1</span>);
<span class="hljs-keyword">var</span> alsoRejected = <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-literal">Infinity</span>);

<span class="hljs-built_in">Promise</span>.any([resolved, rejected, alsoRejected]).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">result</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(result); <span class="hljs-comment">// 42</span>
&#125;);

<span class="hljs-built_in">Promise</span>.any([rejected, alsoRejected]).catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">results</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(results); <span class="hljs-comment">// [-1, Infinity]</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">10. Promise.resolve()</h1>
<p>有时需要将现有对象转为 Promise 对象，<code>Promise.resolve()</code>方法就起到这个作用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> jsPromise = <span class="hljs-built_in">Promise</span>.resolve($.ajax(<span class="hljs-string">'/whatever.json'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码将 jQuery 生成的<code>deferred</code>对象，转为一个新的 Promise 对象。</p>
<p><code>Promise.resolve()</code>等价于下面的写法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'foo'</span>)
<span class="hljs-comment">// 等价于</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> resolve(<span class="hljs-string">'foo'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Promise.resolve()</code>方法的参数分成四种情况。</p>
<h3 data-id="heading-10"><strong>（1）参数是一个 Promise 实例</strong></h3>
<p>如果参数是 Promise 实例，那么<code>Promise.resolve</code>将不做任何修改、原封不动地返回这个实例。</p>
<h3 data-id="heading-11"><strong>（2）参数是一个<code>thenable</code>对象</strong></h3>
<p><code>thenable</code>对象指的是<code>具有then</code>方法的对象，比如下面这个对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> thenable = &#123;
  <span class="hljs-attr">then</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
    resolve(<span class="hljs-number">42</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Promise.resolve()</code>方法会将这个对象转为 Promise 对象，然后就立即执行<code>thenable</code>对象的<code>then()</code>方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> thenable = &#123;
  <span class="hljs-attr">then</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
    resolve(<span class="hljs-number">42</span>);
  &#125;
&#125;;

<span class="hljs-keyword">let</span> p1 = <span class="hljs-built_in">Promise</span>.resolve(thenable);
p1.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(value);  <span class="hljs-comment">// 42</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>thenable</code>对象的<code>then()</code>方法执行后，对象<code>p1</code>的状态就变为<code>resolved</code>，从而立即执行最后那个<code>then()</code>方法指定的回调函数，输出42。</p>
<h3 data-id="heading-12">（3）参数不是具有<code>then()</code>方法的对象，或根本就不是对象</h3>
<p>如果参数是一个原始值，或者是一个不具有then()方法的对象，则Promise.resolve()方法返回一个新的 Promise 对象，状态为resolved。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'Hello'</span>);

p.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">s</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(s)
&#125;);
<span class="hljs-comment">// Hello</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码生成一个新的 Promise 对象的实例p。由于字符串Hello不属于异步操作（判断方法是字符串对象不具有 then 方法），返回 Promise 实例的状态从一生成就是resolved，所以回调函数会立即执行。Promise.resolve()方法的参数，会同时传给回调函数。</p>
<h3 data-id="heading-13">（4）不带有任何参数</h3>
<p>Promise.resolve()方法允许调用时不带参数，直接返回一个resolved状态的 Promise 对象。</p>
<p>所以，如果希望得到一个 Promise 对象，比较方便的方法就是直接调用Promise.resolve()方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.resolve();

p.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的变量p就是一个 Promise 对象。</p>
<p>需要注意的是，立即resolve()的 Promise 对象，是在本轮“事件循环”（event loop）的结束时执行，而不是在下一轮“事件循环”的开始时。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'three'</span>);
&#125;, <span class="hljs-number">0</span>);

<span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'two'</span>);
&#125;);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'one'</span>);

<span class="hljs-comment">// one</span>
<span class="hljs-comment">// two</span>
<span class="hljs-comment">// three</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，setTimeout(fn, 0)在下一轮“事件循环”开始时执行，Promise.resolve()在本轮“事件循环”结束时执行，console.log('one')则是立即执行，因此最先输出。</p>
<p>分析：
定时器是异步宏任务
then是异步微任务
log('one')是同步任务</p>
<p>先执行同步任务，然后是异步微任务，最后是异步宏任务。</p>
<h1 data-id="heading-14">11. Promise.reject()</h1>
<p>Promise.reject(reason)方法也会返回一个新的 Promise 实例，该实例的状态为rejected。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'出错了'</span>);
<span class="hljs-comment">// 等同于</span>
<span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> reject(<span class="hljs-string">'出错了'</span>))

p.then(<span class="hljs-literal">null</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">s</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(s)
&#125;);
<span class="hljs-comment">// 出错了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码生成一个 Promise 对象的实例p，状态为rejected，回调函数会立即执行。</p>
<p>Promise.reject()方法的参数，会原封不动地作为reject的理由，变成后续方法的参数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'出错了'</span>)
.catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(e === <span class="hljs-string">'出错了'</span>)
&#125;)
<span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，Promise.reject()方法的参数是一个字符串，后面catch()方法的参数e就是这个字符串。</p>
<h1 data-id="heading-15">12. 应用</h1>
<h2 data-id="heading-16">加载图片</h2>
<p>我们可以将图片的加载写成一个Promise，一旦加载完成，Promise的状态就发生变化。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> preloadImage = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">path</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    <span class="hljs-keyword">const</span> image = <span class="hljs-keyword">new</span> Image();
    image.onload  = resolve;
    image.onerror = reject;
    image.src = path;
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">Generator 函数与 Promise 的结合</h2>
<p>使用 Generator 函数管理流程，遇到异步操作的时候，通常返回一个Promise对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getFoo</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
        resolve(<span class="hljs-string">'foo'</span>);
    &#125;);
&#125;

<span class="hljs-keyword">const</span> g = <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> foo = <span class="hljs-keyword">yield</span> getFoo();
        <span class="hljs-built_in">console</span>.log(foo);
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        <span class="hljs-built_in">console</span>.log(error);
    &#125;
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span> (<span class="hljs-params">generator</span>) </span>&#123;
    <span class="hljs-keyword">const</span> it = generator();
    
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">go</span>(<span class="hljs-params">result</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (result.done) <span class="hljs-keyword">return</span> result.value;
         
        <span class="hljs-keyword">return</span> result.value.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve</span>) </span>&#123;
            <span class="hljs-keyword">return</span> go(it.next(value));
        &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
            <span class="hljs-keyword">return</span> go(it.throw(error));
        &#125;);
    &#125;
    
    go(it.next());
&#125;

run(g);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的 Generator 函数g之中，有一个异步操作getFoo，它返回的就是一个Promise对象。函数run用来处理这个Promise对象，并调用下一个next方法。</p>
<h1 data-id="heading-18">13. Promise.try()</h1>
<p>实际开发中，经常遇到一种情况：不知道或者不想区分，函数f是同步函数还是异步操作，但是想用 Promise 来处理它。因为这样就可以不管f是否包含异步操作，都用then方法指定下一步流程，用catch方法处理f抛出的错误。一般就会采用下面的写法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve().then(f)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的写法有一个缺点，就是如果<code>f</code>是同步函数，那么它会在本轮事件循环的末尾执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> f = <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'now'</span>);
<span class="hljs-built_in">Promise</span>.resolve().then(f);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'next'</span>);
<span class="hljs-comment">// next</span>
<span class="hljs-comment">// now</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，函数f是同步的，但是用 Promise 包装了以后，就变成异步执行了。</p>
<p>那么有没有一种方法，让同步函数同步执行，异步函数异步执行，并且让它们具有统一的 API 呢？回答是可以的，并且还有两种写法。</p>
<h2 data-id="heading-19">第一种写法是用async函数来写。</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> f = <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'now'</span>);
(<span class="hljs-keyword">async</span> () => f())();
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'next'</span>);
<span class="hljs-comment">// now</span>
<span class="hljs-comment">// next</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，第二行是一个立即执行的匿名函数，会立即执行里面的<code>async函数</code>，因此如果<code>f</code>是同步的，就会得到同步的结果；如果<code>f</code>是异步的，就可以用<code>then</code>指定下一步，就像下面的写法。</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-keyword">async</span> () => f())()
.then(...)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，<code>async () => f()</code>会吃掉<code>f()</code>抛出的错误。所以，如果想捕获错误，要使用<code>promise.catch</code>方法。</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-keyword">async</span> () => f())()
.then(...)
.catch(...)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">第二种写法是使用new Promise()。</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> f = <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'now'</span>);
(
  <span class="hljs-function">() =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(
    <span class="hljs-function"><span class="hljs-params">resolve</span> =></span> resolve(f())
  )
)();
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'next'</span>);
<span class="hljs-comment">// now</span>
<span class="hljs-comment">// next</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码也是使用立即执行的匿名函数，执行new Promise()。这种情况下，同步函数也是同步执行的。</p>
<p>鉴于这是一个很常见的需求，所以现在有一个<a href="https://github.com/ljharb/proposal-promise-try" target="_blank" rel="nofollow noopener noreferrer">提案</a>，提供Promise.try方法替代上面的写法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> f = <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'now'</span>);
<span class="hljs-built_in">Promise</span>.try(f);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'next'</span>);
<span class="hljs-comment">// now</span>
<span class="hljs-comment">// next</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>事实上，<code>Promise.try</code>存在已久，Promise 库<code>Bluebird</code>、<code>Q</code>和<code>when</code>，早就提供了这个方法。</p>
<p>由于<code>Promise.try</code>为所有操作提供了统一的处理机制，所以如果想用then方法管理流程，最好都用Promise.try包装一下。这样有<a href="http://cryto.net/~joepie91/blog/2016/05/11/what-is-promise-try-and-why-does-it-matter/" target="_blank" rel="nofollow noopener noreferrer">许多好处</a>，其中一点就是可以更好地管理异常。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getUsername</span>(<span class="hljs-params">userId</span>) </span>&#123;
  <span class="hljs-keyword">return</span> database.users.get(&#123;<span class="hljs-attr">id</span>: userId&#125;)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">user</span>) </span>&#123;
    <span class="hljs-keyword">return</span> user.name;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>database.users.get()</code>返回一个 Promise 对象，如果抛出异步错误，可以用<code>catch</code>方法捕获，就像下面这样写。</p>
<pre><code class="hljs language-js copyable" lang="js">database.users.get(&#123;<span class="hljs-attr">id</span>: userId&#125;)
.then(...)
.catch(...)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是<code>database.users.get()</code>可能还会抛出同步错误（比如数据库连接错误，具体要看实现方法），这时你就不得不用<code>try...catch</code>去捕获。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
  database.users.get(&#123;<span class="hljs-attr">id</span>: userId&#125;)
  .then(...)
  .catch(...)
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这样的写法就很笨拙了，这时就可以统一用<code>promise.catch()</code>捕获所有同步和异步的错误。</p>
<pre><code class="copyable">Promise.try(() => database.users.get(&#123;id: userId&#125;))
  .then(...)
  .catch(...)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>事实上，<code>Promise.try</code>就是模拟<code>try</code>代码块，就像<code>promise.catch</code>模拟的是<code>catch</code>代码块。</p>
<p>参考链接：
<a href="https://es6.ruanyifeng.com/#docs/promise#Promise-race" target="_blank" rel="nofollow noopener noreferrer">es6.ruanyifeng.com/#docs/promi…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            