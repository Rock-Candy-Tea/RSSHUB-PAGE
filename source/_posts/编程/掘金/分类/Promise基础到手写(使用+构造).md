
---
title: 'Promise基础到手写(使用+构造)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59da1a45f64842648816fcb833f1ced0~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 09 Apr 2021 04:21:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59da1a45f64842648816fcb833f1ced0~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Promise简介</h2>
<p>Promise 最早出现是为了解决编程中的异步行为导致的回调地狱。在没有 Promise 之前，对于函数的异步行为，一般采用回调函数的方式，在一个函数调用结束触发回调函数，这样会导致多层级的回调函数，难以维护。
Promise 有两个参数，一个成功回调，一个失败回调，所以在 Promise 外部，可以准确的获得成功和失败的时机，并且 Promise 支持链式调用，这样可以方便的进行多次调用，但是永远都是单层级，便于维护。</p>
<h2 data-id="heading-1">两种异步行为对比</h2>
<p>回调地狱方式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> sayhello = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name, callback</span>) </span>&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(name);
    callback();
  &#125;, <span class="hljs-number">1000</span>);
&#125;
sayhello(<span class="hljs-string">"first"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  sayhello(<span class="hljs-string">"second"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    sayhello(<span class="hljs-string">"third"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"end"</span>);
    &#125;);
  &#125;);
&#125;);
<span class="hljs-comment">//输出： first second third  end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Promise 写法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> sayHello = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"first"</span>);
    resolve();
  &#125;, <span class="hljs-number">1000</span>);
&#125;);
sayHello
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"second"</span>);
  &#125;)
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"third"</span>);
  &#125;)
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"end"</span>);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以发现 Promise 不管有多少次逻辑处理，每一次只有一层，清晰可见，不像回调一样，层层嵌套，难以理清。</p>
<h2 data-id="heading-2">Promise 基础</h2>
<p>Promise 实例</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(
  <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123; <span class="hljs-comment">// executor（执行者）</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    resolve(<span class="hljs-string">"done"</span>),<span class="hljs-number">1000</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们只需要 new Promise即可创建一个 Promise，创建即立刻调用其中的执行者。
executor 接受两个参数：resolve 和 reject 。这些是JavaScript 引擎预定义的，不要我们创建，我们只需要在我们想要告知的状态中调用对应的方法即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  resolve(<span class="hljs-string">"done"</span>);

  reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"…"</span>)); <span class="hljs-comment">// 被忽略</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> resolve(<span class="hljs-string">"…"</span>)); <span class="hljs-comment">// 被忽略</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>这儿只能有一个结果或一个 error</strong>
executor 只能调用一个 <code>resolve</code> 或一个 <code>reject</code>。任何状态的更改都是最终的。
所有其他的再对 <code>resolve</code> 和 <code>reject</code> 的调用都会被忽略
并且，<code>resolve/reject</code> 只需要一个参数（或不包含任何参数），并且将忽略额外的参数</p>
<p>那么我们会疑问，我们费这么大工夫，在 Promise 内部做这么多操作，最后使他产生一个状态是为了什么，他失败与否和我们之前的回调地狱有什么关系？</p>
<pre><code class="copyable">state 和 result 都是内部的
Promise 对象的 state 和 result 属性都是内部的。
我们无法直接访问它们。但我们可以对它们使用 .then/.catch/.finally 方法。
我们在下面对这些方法进行了描述。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们使用 Promise 生产了一个成功或者失败的结果，可以通过使用 <code>.then</code>、<code>.catch</code> 和 <code>.finally</code> 方法为消费函数进行结果接收。</p>
<h3 data-id="heading-3">then</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> resolve(<span class="hljs-string">"done!"</span>), <span class="hljs-number">1000</span>);
&#125;);

<span class="hljs-comment">// resolve 运行 .then 中的第一个函数</span>
promise.then(
  <span class="hljs-function"><span class="hljs-params">result</span> =></span> alert(result), <span class="hljs-comment">// 1 秒后显示 "done!"</span>
  <span class="hljs-function"><span class="hljs-params">error</span> =></span> alert(error) <span class="hljs-comment">// 不运行</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.then</code> 的第一个参数是一个函数，该函数将在 promise resolved 后运行并接收结果。
<code>.then</code> 的第二个参数也是一个函数，该函数将在 promise rejected 后运行并接收 error。
如果我们只对成功完成的情况感兴趣，那么我们可以只为 <code>.then</code> 提供一个函数参数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> resolve(<span class="hljs-string">"done!"</span>), <span class="hljs-number">1000</span>);
&#125;);

promise.then(alert); <span class="hljs-comment">// 1 秒后显示 "done!"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.catch(f)</code> 调用是 <code>.then(null, f)</code> 的完全的模拟，它只是一个简写形式。简单说，catch就是一个接收错误结果的方法。
<strong>我们可以对 settled 的 promise 附加处理程序</strong>
如果 promise 为 pending 状态，<code>.then/catch/finally</code> 处理程序（handler）将等待它。否则，如果 promise 已经是 settled 状态，它们就会运行
自测案例
写一个 3s 后弹窗的 Promise</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">delay</span>(<span class="hljs-params">ms</span>) </span>&#123;
  <span class="hljs-comment">// 你的代码</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-function"><span class="hljs-title">Promise</span>(<span class="hljs-params">resolve,reject</span>)</span>&#123;
  <span class="hljs-built_in">setTimeout</span>(resolve,<span class="hljs-number">3000</span>)
  &#125;
 &#125;

delay(<span class="hljs-number">3000</span>).then(<span class="hljs-function">() =></span> alert(<span class="hljs-string">'runs after 3 seconds'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">catch</h3>
<p>如果只要失败回调，那么只需要将 then 的第一个参数设置为null，
也可以使用 catch ，这里面可以接受 reject 的结果</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"Whoops!"</span>)), <span class="hljs-number">1000</span>);
&#125;);

<span class="hljs-comment">// .catch(f) 与 promise.then(null, f) 一样</span>
promise.catch(alert); <span class="hljs-comment">// 1 秒后显示 "Error: Whoops!"</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">finally</h3>
<p>无论结果如何，最后都会执行这里面的函数。
<code>**finally()**</code> 方法返回一个<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise" target="_blank" rel="nofollow noopener noreferrer"><code>Promise</code></a>。在promise结束时，无论结果是fulfilled或者是rejected，都会执行指定的回调函数。这为在<code>Promise</code>是否成功完成后都需要执行的代码提供了一种方式。
这避免了同样的语句需要在<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/then" target="_blank" rel="nofollow noopener noreferrer"><code>then()</code></a>和<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch" target="_blank" rel="nofollow noopener noreferrer"><code>catch()</code></a>中各写一次的情况。</p>
<h2 data-id="heading-6">构建 Promise</h2>
<p>在我了解完 Promise 后，我对如何实现他非常感兴趣，于是我试着自己来构建一个 Promise。
首先我们要分析一下我们的需求，我们要得到什么，要实现哪些功能，确定目标。</p>
<ol>
<li>我们要实现一个名叫 Promise 的类。</li>
<li>类里我们要实现一个 resolve 成功通知。</li>
<li>类里我们要实现一个 reject失败通知。</li>
<li>executor 立刻执行。</li>
<li>我们还要实现一个可以拿到结果的 then。</li>
<li>一个捕获错误的 catch。</li>
<li>一个不管结果的 finally。</li>
</ol>
<p><img alt="Promise.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59da1a45f64842648816fcb833f1ced0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
我们按照上图，分为两个大步骤，开始进行实现我们自己的 Promise。</p>
<p>首先构造 Promise 类。</p>
<ol>
<li>初始化阶段，我们考虑到 Promise 一共有三种状态，两个结果。所以我们要初始化状态和结果。</li>
<li>然后我们发送成功和失败的信息时，要改变状态，并且保存结果。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> executor !== <span class="hljs-string">"function"</span>) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"参数不合法"</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.status = <span class="hljs-string">"pending"</span>;
      <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>;
      <span class="hljs-built_in">this</span>.error = <span class="hljs-literal">undefined</span>;
      <span class="hljs-comment">//自动运行Promise中的函数</span>
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">//将resolve和reject函数给使用者</span>
        executor(resolve, reject);
      &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        <span class="hljs-comment">//如果在函数中抛出异常则将它注入reject中</span>
        reject(e);
      &#125;
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-comment">//成功触发</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">"pending"</span>) &#123;
      <span class="hljs-built_in">this</span>.status = <span class="hljs-string">"fulfilled"</span>;
      <span class="hljs-built_in">this</span>.value = data;
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">data</span>)</span> &#123;
    <span class="hljs-comment">//失败触发</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">"pending"</span>) &#123;
      <span class="hljs-built_in">this</span>.status = <span class="hljs-string">"rejected"</span>;
      <span class="hljs-built_in">this</span>.error = data;
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  <span class="hljs-keyword">catch</span>() &#123;&#125;
  <span class="hljs-function"><span class="hljs-title">finally</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们实现了上述几个目标，接下来我们要实现接受结果信息的方法。</p>
<ol>
<li>then 接受两个参数，第一个将在 promise resolved 后运行并接收 value 。第二个将在 promise reject 后运行并接收 error。</li>
<li>catch 只接受一个函数，promise reject 后运行并接收 error。</li>
<li>finally 无论结果如何都会执行。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> executor !== <span class="hljs-string">"function"</span>) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"参数不合法"</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.status = <span class="hljs-string">"pending"</span>;
      <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>;
      <span class="hljs-built_in">this</span>.error = <span class="hljs-literal">undefined</span>;
      <span class="hljs-comment">//自动运行Promise中的函数</span>
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">//将resolve和reject函数给使用者</span>
        executor(<span class="hljs-built_in">this</span>.resolve, <span class="hljs-built_in">this</span>.reject);
      &#125; <span class="hljs-keyword">catch</span> (e) &#123;
        <span class="hljs-comment">//如果在函数中抛出异常则将它注入reject中</span>
        <span class="hljs-built_in">this</span>.reject(e);
      &#125;
    &#125;
  &#125;
  resolve = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-comment">//成功触发</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">"pending"</span>) &#123;
      <span class="hljs-built_in">this</span>.status = <span class="hljs-string">"fulfilled"</span>;
      <span class="hljs-built_in">this</span>.value = data;
    &#125;
  &#125;;
  reject = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-comment">//失败触发</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">"pending"</span>) &#123;
      <span class="hljs-built_in">this</span>.status = <span class="hljs-string">"rejected"</span>;
      <span class="hljs-built_in">this</span>.error = data;
    &#125;
  &#125;;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">"fulfilled"</span>) &#123;
      onFulfilled(<span class="hljs-built_in">this</span>.value);
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">"rejected"</span>) &#123;
      onRejected(<span class="hljs-built_in">this</span>.error);
    &#125;
  &#125;
  <span class="hljs-keyword">catch</span>(onRejected) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">"rejected"</span>) &#123;
      onRejected(<span class="hljs-built_in">this</span>.error);
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">finally</span>(<span class="hljs-params">onFinally</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== <span class="hljs-string">"pending"</span>) &#123;
      onFinally();
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们就完成了一个简易版的 Promise。
我们来将文件引入测试一下，看看结果如何。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><!DOCTYPE html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./index.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        resolve(<span class="hljs-string">"coolFish!"</span>);
      &#125;);
      promise.then(
        <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"成功"</span> + data);
        &#125;,
        <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"失败"</span> + data);
        &#125;
      );
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span></span>


<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果和 Promise 一样，可以实现成功和失败的不同操作，接下来我们要开始扩展它的功能，从可支持链式调用开始。</p>
<h3 data-id="heading-7">Promise.then</h3>
<p>首先我们明确 promise.then（onFulfilled, onRejected ） 做的事情</p>
<ol>
<li>入参判断，处理 onFulfilled 或者 onRejected 不是函数的情况。</li>
<li>创建并且返回一个 promise 实例。</li>
<li>将 onFulfilled 和 onRejected 添加到事件队列（根据 promise 的状态来决定如何处理）。</li>
<li>状态为 fulfilled 执行 onFulfilled 。</li>
<li>状态为 rejected 则执行 onRejected。</li>
<li>如果没有做出决议，则添加进事件队列。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-comment">//创建并返回一个Promise实例</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> wrapOnFulfilled = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"wrapOnFulfilled"</span>);
            <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value);
            resolve(x);
          &#125; <span class="hljs-keyword">catch</span> (error) &#123;
            reject(error);
          &#125;
        &#125;, <span class="hljs-number">0</span>);
      &#125;;
      <span class="hljs-keyword">let</span> wrapOnRejected = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"wrapOnRejected"</span>);
            <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.error);
            resolve(x);
          &#125; <span class="hljs-keyword">catch</span> (error) &#123;
            reject(error);
          &#125;
        &#125;, <span class="hljs-number">0</span>);
      &#125;;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">"fulfilled"</span>) &#123;
        wrapOnFulfilled();
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">"rejected"</span>) &#123;
        wrapOnRejected();
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">this</span>.onFulfilledCallbacks.push(wrapOnFulfilled);
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(wrapOnRejected);
      &#125;
    &#125;);
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Promise.all</h3>
<p>首先我们先明确目标
<code>Promise.all</code> 接受一个 promise 数组作为参数（从技术上讲，它可以是任何可迭代的，但通常是一个数组）并返回一个新的 promise。
当所有给定的 promise 都被 settled 时，新的 promise 才会 resolve，并且其结果数组将成为新的 promise 的结果。
我们来看一张流程图，然后我们按照流程图来实现我们的代码</p>
<p><img alt="PromiseAll.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d320b3b145974d859754010ee0cdad7b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">promises</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-comment">// 如果Promise.all接收到的是一个空数组([])，它会立即决议。</span>
      <span class="hljs-keyword">if</span> (!promises.length) &#123;
        resolve([]);
      &#125;
      <span class="hljs-keyword">let</span> result = [];
      <span class="hljs-keyword">let</span> resolvedPro = <span class="hljs-number">0</span>;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>, length = promises.length; index < length; index++) &#123;
        <span class="hljs-built_in">Promise</span>.resolve(promises[index]).then(
          <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
            <span class="hljs-comment">// 注意，这里要用index赋值，而不是push。因为要保持返回值和接收到的promise的位置一致性。</span>
            result[index] = data;
            <span class="hljs-keyword">if</span> (++resolvedPro === length) &#123;
              resolve(result);
            &#125;
          &#125;,
          <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
            reject(error);
          &#125;
        );
      &#125;
    &#125;);
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">Promise.race</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 需要注意的是，如果Promise.race接收到的是一个空数组([])，则会一直挂起，而不是立即决议。</span>
<span class="hljs-built_in">Promise</span>.race = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">promises</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    promises.forEach(<span class="hljs-function">(<span class="hljs-params">promise</span>) =></span> &#123;
      <span class="hljs-built_in">Promise</span>.resolve(promise).then(resolve, reject);
    &#125;);
  &#125;);
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Promise.allSettled</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Promise.allSettled 返回一个在所有给定的promise都已经fulfilled或rejected后的promise，</span>
<span class="hljs-comment">// 并带有一个对象数组，每个对象表示对应的promise结果。</span>
<span class="hljs-built_in">Promise</span>.allSettled = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">promises</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (!promises.length) &#123;
      resolve([]);
    &#125;

    <span class="hljs-keyword">let</span> result = [];
    <span class="hljs-keyword">let</span> resolvedPro = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>, length = promises.length; index < length; index++) &#123;
      <span class="hljs-built_in">Promise</span>.resolve(promises[index])
        .then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
          <span class="hljs-comment">// 注意，这里要用index赋值，而不是push。因为要保持返回值和接收到的promise的位置一致性。</span>
          result[index] = &#123;
            <span class="hljs-attr">status</span>: FULFILLED_STATE,
            <span class="hljs-attr">value</span>: data,
          &#125;;
          <span class="hljs-keyword">if</span> (++resolvedPro === length) &#123;
            resolve(result);
          &#125;
        &#125;)
        .catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
          result[index] = &#123;
            <span class="hljs-attr">status</span>: REJECTED_STATE,
            <span class="hljs-attr">reason</span>: error,
          &#125;;
          <span class="hljs-keyword">if</span> (++resolvedPro === length) &#123;
            resolve(result);
          &#125;
        &#125;);
    &#125;
  &#125;);
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            