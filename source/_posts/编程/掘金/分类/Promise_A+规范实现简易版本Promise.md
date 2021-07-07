
---
title: 'Promise_A+规范实现简易版本Promise'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3678'
author: 掘金
comments: false
date: Sat, 03 Jul 2021 23:22:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=3678'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>想优雅地进行异步操作，必须要熟识一个极其重要的概念 —— Promise。它是取代传统回调，实现同步链式写法的解决方案；是理解 generator、async/await 的关键</p>
<h3 data-id="heading-0">初见雏形</h3>
<p>在微信小程序开发过程中，我们使用 wx.request() 在微信小程序环境中发送一个网络请求。参考官方文档，具体用法如下：</p>
<pre><code class="hljs language-js copyable" lang="js">wx.request(&#123;
  <span class="hljs-attr">url</span>: <span class="hljs-string">'xxxx'</span>, <span class="hljs-comment">// 仅为示例，并非真实的接口地址</span>
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">x</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">y</span>: <span class="hljs-string">''</span>
  &#125;,
  <span class="hljs-attr">header</span>: &#123;
    <span class="hljs-string">'content-type'</span>: <span class="hljs-string">'application/json'</span> <span class="hljs-comment">// 默认值</span>
  &#125;,
  <span class="hljs-function"><span class="hljs-title">success</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(res.data)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置化的 API 风格和早期使用 jQuery 中 Ajax 方法的封装类似。这样的设计有一个小的问题，就是容易出现“回调地狱”问题。如果想先通过 ./userInfo 接口来获取登录用户信息数据，再从登录用户信息数据中，通过请求 <code>./$&#123;id&#125;/friendList</code> 接口来获取登录用户所有好友列表，就需要：</p>
<pre><code class="hljs language-js copyable" lang="js">wx.request(&#123;
  <span class="hljs-attr">url</span>: <span class="hljs-string">'./userInfo'</span>,
  <span class="hljs-function"><span class="hljs-title">success</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-keyword">const</span> id = res.data.id
    wx.request(&#123;
      <span class="hljs-attr">url</span>: <span class="hljs-string">`./<span class="hljs-subst">$&#123;id&#125;</span>/friendList`</span>,
      <span class="hljs-function"><span class="hljs-title">success</span>(<span class="hljs-params">res</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(res)
      &#125;
    &#125;)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这只是嵌套了一层回调而已，还够不成“地狱”场景，但是足以说明问题。</p>
<p>我们知道解决“回调地狱”问题的一个极佳方式就是 Promise，将微信小程序 wx.request() 方法进行 Promise 化：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> wxRequest = <span class="hljs-function">(<span class="hljs-params">url, data = &#123;&#125;, method = <span class="hljs-string">'GET'</span></span>) =></span> 
  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    wx.request(&#123;
      url,
      data,
      method,
      <span class="hljs-attr">header</span>: &#123;
        <span class="hljs-comment">//通用化 header 设置</span>
      &#125;,
      <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
        <span class="hljs-keyword">const</span> code = res.statusCode
        <span class="hljs-keyword">if</span> (code !== <span class="hljs-number">200</span>) &#123;
          reject(&#123; <span class="hljs-attr">error</span>: <span class="hljs-string">'request fail'</span>, code &#125;)
          <span class="hljs-keyword">return</span>
        &#125;
        resolve(res.data)
      &#125;,
      <span class="hljs-attr">fail</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
        reject(&#123; <span class="hljs-attr">error</span>: <span class="hljs-string">'request fail'</span>&#125;)
      &#125;,
    &#125;)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Promise 基本概念不再过多介绍。这是一个典型的 Promise 化案例，当然我们不仅可以对 wx.request() API 进行 Promise 化，更应该做的通用，能够 Promise 化更多类似（通过 success 和 fail 表征状态）的接口：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promisify = <span class="hljs-function"><span class="hljs-params">fn</span> =></span> <span class="hljs-function"><span class="hljs-params">args</span> =></span> 
  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    args.success = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">res</span>) </span>&#123;
      <span class="hljs-keyword">return</span> resolve(res)
    &#125;
    args.fail = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">res</span>) </span>&#123;
      <span class="hljs-keyword">return</span> reject(res)
    &#125;
  &#125;)

<span class="hljs-comment">// 使用 </span>
<span class="hljs-keyword">const</span> wxRequest = promisify(wx.request)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上例，可以知道：</p>
<blockquote>
<p>Promise 其实就是一个构造函数，我们使用这个构造函数创建一个 Promise 实例。该构造函数很简单，它只有一个参数，按照 Promise/A+ 规范的命名，把 Promise 构造函数的参数叫做 executor，executor 类型为函数。这个函数又“自动”具有 resolve、reject 两个方法作为参数。</p>
</blockquote>
<p>请仔细体会上述结论，那么可以通过结论，开始实现 Promise 的第一步：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">executor</span>) </span>&#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的 wx.request() 介绍中，实现了 Promise 化，因此对于嵌套回调场景，可以：</p>
<pre><code class="hljs language-js copyable" lang="js">wxRequest(<span class="hljs-string">'./userInfo'</span>)
  .then(
    <span class="hljs-function"><span class="hljs-params">data</span> =></span> wxRequest(<span class="hljs-string">`./<span class="hljs-subst">$&#123;data.id&#125;</span>/friendList`</span>),
    <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(error)
    &#125;
  )
  .then(
    <span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(data)
    &#125;,
    <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(error)
    &#125;
  )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过观察使用例子, 可以来剖析 Promise 的实质：</p>
<blockquote>
<p><strong>结论</strong>　Promise 构造函数返回一个 promise 对象实例，这个返回的 promise 对象具有一个 then 方法。then 方法中，调用者可以定义两个参数，分别是 onfulfilled 和 onrejected，它们都是函数类型。其中 onfulfilled 通过参数，可以获取 promise 对象 resolved 的值，onrejected 获得 promise 对象 rejected 的值。通过这个值，我们来处理异步完成后的逻辑。</p>
</blockquote>
<p>因此，继续实现 Promise：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">executor</span>) </span>&#123;

&#125;

<span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">onfulfilled, onrejected</span>) </span>&#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>继续复习 Promise 的知识，看例子来理解：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> promise1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  resolve(<span class="hljs-string">'data'</span>)
&#125;)

promise1.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
&#125;)

<span class="hljs-keyword">let</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  reject(<span class="hljs-string">'error'</span>)
&#125;)

promise2.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
&#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(error)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>结论</strong>　在使用 new 关键字调用 Promise 构造函数时，在合适的时机（往往是异步结束时），调用 executor 的参数 resolve 方法，并将 resolved 的值作为 resolve 函数参数执行，这个值便可以后续在 then 方法第一个函数参数（onfulfilled）中拿到；同理，在出现错误时，调用 executor 的参数 reject 方法，并将错误信息作为 reject 函数参数执行，这个错误信息可以在后续的 then 方法第二个函数参数（onrejected）中拿到。</p>
</blockquote>
<p>因此，在实现 Promise 时，应该有两个值，分别储存 resolved 的值，以及 rejected 的值（当然，因为 Promise 状态的唯一性，不可能同时出现 resolved 的值和 rejected 的值，因此也可以用一个变量来存储）；同时也需要存在一个状态，这个状态就是 promise 实例的状态（pending，fulfilled，rejected）；同时还要提供 resolve 方法以及 reject 方法，这两个方法需要作为 executor 的参数提供给开发者使用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">executor</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'pending'</span>
  <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>
  <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.value = value
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.reason = reason
  &#125;

  executor(resolve, reject)
&#125;


<span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">onfulfilled, onrejected</span>) </span>&#123;
  <span class="hljs-comment">// 健壮性处理</span>
  onfulfilled = <span class="hljs-keyword">typeof</span> onfulfilled === <span class="hljs-string">'function'</span> ? onfulfilled : <span class="hljs-function"><span class="hljs-params">data</span> =></span> data
  onrejected = <span class="hljs-keyword">typeof</span> onrejected === <span class="hljs-string">'function'</span> ? onrejected : <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;<span class="hljs-keyword">throw</span> error&#125;

  onfulfilled(<span class="hljs-built_in">this</span>.value)

  onrejected(<span class="hljs-built_in">this</span>.reason)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了保证 onfulfilled、onrejected 能够强健执行，我们为其设置了默认值</p>
<h3 data-id="heading-1">状态完善</h3>
<p>先来看一到题目，判断输出：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  resolve(<span class="hljs-string">'data'</span>)
  reject(<span class="hljs-string">'error'</span>)
&#125;)

promise.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
&#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(error)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>只会</strong>输出：data，因为我们知道 promise 实例状态只能从 pending 改变为 fulfilled，或者从 pending 改变为 rejected。状态一旦变更完毕，就不可再次变化或者逆转。也就是说：如果一旦变到 fulfilled，就不能再 rejected，一旦变到 rejected，就不能 fulfilled。</p>
<p>而我们的代码实现，显然无法满足这一特性。执行上一段代码时，将会输出 data 以及 error。</p>
<p>因此，需要对状态进行判断和完善：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">executor</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'pending'</span>
  <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>
  <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>

  <span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
      <span class="hljs-built_in">this</span>.value = value
      <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'fulfilled'</span>
    &#125;
  &#125;

  <span class="hljs-keyword">const</span> reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
      <span class="hljs-built_in">this</span>.reason = reason
      <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'rejected'</span>
    &#125;
  &#125;

  executor(resolve, reject)
&#125;

<span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">onfulfilled, onrejected</span>) </span>&#123;
  <span class="hljs-comment">// 健壮性处理</span>
  onfulfilled = <span class="hljs-keyword">typeof</span> onfulfilled === <span class="hljs-string">'function'</span> ? onfulfilled : <span class="hljs-function"><span class="hljs-params">data</span> =></span> data
  onrejected = <span class="hljs-keyword">typeof</span> onrejected === <span class="hljs-string">'function'</span> ? onrejected : <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;<span class="hljs-keyword">throw</span> error&#125;

  <span class="hljs-comment">// 只允许 promise 实例状态从 pending 改变为 fulfilled，或者从 pending 改变为 rejected。</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'fulfilled'</span>) &#123;
    onfulfilled(<span class="hljs-built_in">this</span>.value)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'rejected'</span>) &#123;
    onrejected(<span class="hljs-built_in">this</span>.reason)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看，在 resolve 和 reject 方法中，我们加入判断，只允许 promise 实例状态从 pending 改变为 fulfilled，或者从 pending 改变为 rejected。</p>
<h3 data-id="heading-2">异步完善</h3>
<p>到目前为止，实现还差了哪些内容呢？别急，再从示例代码分析：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-string">'data'</span>)
  &#125;, <span class="hljs-number">2000</span>)
&#125;)

promise.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正常来讲，上述代码会在 2 秒之后输出 data，但是目前实现的代码，并没有输入任何信息。这是为什么呢？</p>
<p>原因很简单，因为当前的实现逻辑全是同步的。在上面实例化一个 promise 的构造函数时，我们是在 setTimeout 逻辑里才调用 resolve，也就是说，2 秒之后才会调用 resolve 方法，也才会去更改 promise 实例状态。而结合目前实现，返回实现代码，then 方法中的 onfulfilled 执行是同步的，它在执行时 this.status 仍然为 pending，并没有做到“2 秒中之后再执行 onfulfilled”。</p>
<p>那该怎么办呢？应该在“合适”的时间才去调用 onfulfilled 方法，这个合适的时间就应该是开发者调用 resolve 的时刻，那么先在状态（status）为 pending 时，把开发者传进来的 onfulfilled 方法存起来，在 resolve 方法中再去执行即可：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">executor</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'pending'</span>
  <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>
  <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>
  <span class="hljs-built_in">this</span>.onFulfilledFunc = <span class="hljs-built_in">Function</span>.prototype
  <span class="hljs-built_in">this</span>.onRejectedFunc = <span class="hljs-built_in">Function</span>.prototype

  <span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
      <span class="hljs-built_in">this</span>.value = value
      <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'fulfilled'</span>

      <span class="hljs-built_in">this</span>.onFulfilledFunc(<span class="hljs-built_in">this</span>.value)
    &#125;

  &#125;

  <span class="hljs-keyword">const</span> reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
      <span class="hljs-built_in">this</span>.reason = reason
      <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'rejected'</span>

      <span class="hljs-built_in">this</span>.onRejectedFunc(<span class="hljs-built_in">this</span>.reason)
    &#125;
  &#125;

  executor(resolve, reject)
&#125;

<span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">onfulfilled, onrejected</span>) </span>&#123;
  onfulfilled = <span class="hljs-keyword">typeof</span> onfulfilled === <span class="hljs-string">'function'</span> ? onfulfilled : <span class="hljs-function"><span class="hljs-params">data</span> =></span> data
  onrejected = <span class="hljs-keyword">typeof</span> onrejected === <span class="hljs-string">'function'</span> ? onrejected : <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;<span class="hljs-keyword">throw</span> error&#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'fulfilled'</span>) &#123;
    onfulfilled(<span class="hljs-built_in">this</span>.value)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'rejected'</span>) &#123;
    onrejected(<span class="hljs-built_in">this</span>.reason)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
    <span class="hljs-built_in">this</span>.onFulfilledFunc = onfulfilled
    <span class="hljs-built_in">this</span>.onRejectedFunc = onrejected
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试一下，发现现在的实现也可以支持异步了！</p>
<p>同时，<strong>我们知道 Promise 是异步执行的：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
   resolve(<span class="hljs-string">'data'</span>)
&#125;)

promise.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正常的话，这里会<strong>按照顺序</strong>，输出 1 再输出 data。</p>
<p>而目前的实现，却没有考虑这种情况，先输出 data 再输出 1。因此，需要将 resolve 和 reject 的执行，放到任务队列中。这里姑且先放到 setTimeout 里，保证异步执行（这样的做法并不严谨，为了保证 Promise 属于 microtasks，很多 Promise 的实现库用了 MutationObserver 来模仿 nextTick）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (value <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) &#123;
    <span class="hljs-keyword">return</span> value.then(resolve, reject)
  &#125;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
      <span class="hljs-built_in">this</span>.value = value
      <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'fulfilled'</span>

      <span class="hljs-built_in">this</span>.onFulfilledFunc(<span class="hljs-built_in">this</span>.value)
    &#125;
  &#125;)
&#125;

<span class="hljs-keyword">const</span> reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
      <span class="hljs-built_in">this</span>.reason = reason
      <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'rejected'</span>

      <span class="hljs-built_in">this</span>.onRejectedFunc(<span class="hljs-built_in">this</span>.reason)
    &#125;
  &#125;)
&#125;

executor(resolve, reject)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一来，在执行到 executor(resolve, reject) 时，也能保证在 nextTick 中才去执行，不会阻塞同步任务。</p>
<p>同时在 resolve 方法中，加入了对 value 值是一个 Promise 实例的判断。看一下到目前为止的实现代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">executor</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'pending'</span>
  <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>
  <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>
  <span class="hljs-built_in">this</span>.onFulfilledFunc = <span class="hljs-built_in">Function</span>.prototype
  <span class="hljs-built_in">this</span>.onRejectedFunc = <span class="hljs-built_in">Function</span>.prototype

  <span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (value <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) &#123;
      <span class="hljs-keyword">return</span> value.then(resolve, reject)
    &#125;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.value = value
        <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'fulfilled'</span>

        <span class="hljs-built_in">this</span>.onFulfilledFunc(<span class="hljs-built_in">this</span>.value)
      &#125;
    &#125;)
  &#125;

  <span class="hljs-keyword">const</span> reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.reason = reason
        <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'rejected'</span>

        <span class="hljs-built_in">this</span>.onRejectedFunc(<span class="hljs-built_in">this</span>.reason)
      &#125;
    &#125;)
  &#125;

  executor(resolve, reject)
&#125;

<span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">onfulfilled, onrejected</span>) </span>&#123;
  onfulfilled = <span class="hljs-keyword">typeof</span> onfulfilled === <span class="hljs-string">'function'</span> ? onfulfilled : <span class="hljs-function"><span class="hljs-params">data</span> =></span> data
  onrejected = <span class="hljs-keyword">typeof</span> onrejected === <span class="hljs-string">'function'</span> ? onrejected : <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;<span class="hljs-keyword">throw</span> error&#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'fulfilled'</span>) &#123;
    onfulfilled(<span class="hljs-built_in">this</span>.value)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'rejected'</span>) &#123;
    onrejected(<span class="hljs-built_in">this</span>.reason)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
    <span class="hljs-built_in">this</span>.onFulfilledFunc = onfulfilled
    <span class="hljs-built_in">this</span>.onRejectedFunc = onrejected
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">细节完善</h3>
<p>到此为止，似乎目前的 Promise 实现越来越靠谱了，但是还有些细节需要完善。</p>
<p>比如当 promise 实例状态变更之前，添加多个 then 方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-string">'data'</span>)
  &#125;, <span class="hljs-number">2000</span>)
&#125;)

promise.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`1: <span class="hljs-subst">$&#123;data&#125;</span>`</span>)
&#125;)
promise.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`2: <span class="hljs-subst">$&#123;data&#125;</span>`</span>)
&#125;)


<span class="hljs-comment">// 应该输出 1:data 2:data</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而目前的实现，只会输出 2: data，这是因为第二个 then 方法中的 onFulfilledFunc 会覆盖第一个 then 方法中的 onFulfilledFunc。</p>
<p>这个问题也好解决，只需要将所有 then 方法中的 onFulfilledFunc 储存为一个数组 onFulfilledArray，在 resolve 时，依次执行即可。对于 onRejectedFunc 同理，改动后的实现为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">executor</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'pending'</span>
  <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>
  <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>
  <span class="hljs-built_in">this</span>.onFulfilledArray = [] <span class="hljs-comment">// modify</span>
  <span class="hljs-built_in">this</span>.onRejectedArray = [] <span class="hljs-comment">// modify</span>

  <span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (value <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) &#123;
      <span class="hljs-keyword">return</span> value.then(resolve, reject)
    &#125;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.value = value
        <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'fulfilled'</span>

        <span class="hljs-comment">// modify</span>
        <span class="hljs-built_in">this</span>.onFulfilledArray.forEach(<span class="hljs-function"><span class="hljs-params">func</span> =></span> &#123; 
          func(value)
        &#125;)
      &#125;
    &#125;)
  &#125;

  <span class="hljs-keyword">const</span> reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.reason = reason
        <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'rejected'</span>

        <span class="hljs-comment">// modify</span>
        <span class="hljs-built_in">this</span>.onRejectedArray.forEach(<span class="hljs-function"><span class="hljs-params">func</span> =></span> &#123;
          func(reason)
        &#125;)
      &#125;
    &#125;)
  &#125;

  <span class="hljs-comment">// 在构造函数中如果出错，将会自动触发 promise 实例状态为 rejected，我们用 try…catch 块对 executor 进行包裹</span>
  <span class="hljs-keyword">try</span> &#123;
    executor(resolve, reject)
  &#125; <span class="hljs-keyword">catch</span>(e) &#123;
    reject(e)
  &#125;
&#125;

<span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">onfulfilled, onrejected</span>) </span>&#123;
  onfulfilled = <span class="hljs-keyword">typeof</span> onfulfilled === <span class="hljs-string">'function'</span> ? onfulfilled : <span class="hljs-function"><span class="hljs-params">data</span> =></span> data
  onrejected = <span class="hljs-keyword">typeof</span> onrejected === <span class="hljs-string">'function'</span> ? onrejected : <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;<span class="hljs-keyword">throw</span> error&#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'fulfilled'</span>) &#123;
    onfulfilled(<span class="hljs-built_in">this</span>.value)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'rejected'</span>) &#123;
    onrejected(<span class="hljs-built_in">this</span>.reason)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
    <span class="hljs-built_in">this</span>.onFulfilledArray.push(onfulfilled)
    <span class="hljs-built_in">this</span>.onRejectedArray.push(onrejected)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">链式调用</h3>
<p>在完成了<code>Promise</code>的基础功能之后，看一道题目</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'Nordon'</span>)
  &#125;, <span class="hljs-number">2000</span>)
&#125;)

promise.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;data&#125;</span> next then`</span>
&#125;)
.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码执行后，将会在 2 秒后输出：Nordon，紧接着输出：Nordon next then。</p>
<p>可以看到，Promise 实例的 then 方法支持链式调用，输出 resolved 值后，如果在 then 方法体 onfulfilled 函数中同步显式返回新的值，将会在新 Promise 实例的 then 方法 onfulfilled 函数中输出新值。</p>
<p>如果在第一个 then 方法体 onfulfilled 函数中返回另一个 Promise 实例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'Nordon'</span>)
  &#125;, <span class="hljs-number">2000</span>)
&#125;)

promise.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        resolve(<span class="hljs-string">`<span class="hljs-subst">$&#123;data&#125;</span> next then`</span>)
    &#125;, <span class="hljs-number">4000</span>)
  &#125;)
&#125;)
.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将在 2 秒后输出：Nordon，紧接着再过 4 秒后（第 6 秒）输出：Nordon next then。</p>
<p>由此可知：</p>
<blockquote>
<p>一个 Promise 实例的 then 方法体 onfulfilled 函数和 onrejected 函数中，是支持再次返回一个 Promise 实例的，也支持返回一个非 Promise 实例的普通值；并且返回的这个 Promise 实例或者这个非 Promise 实例的普通值将会传给下一个 then 方法 onfulfilled 函数或者 onrejected 函数中，这样就支持链式调用了。</p>
</blockquote>
<p>该怎么实现这种行为呢？</p>
<p>首先来分析一下：为了能够支持 then 方法的链式调用，那么每一个 then 方法的 onfulfilled 函数和 onrejected 函数都应该返回一个 Promise 实例。</p>
<p>先实现返回一个非<code>Promise</code>对象的情况</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'Nordon'</span>)
  &#125;, <span class="hljs-number">2000</span>)
&#125;)

promise.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;data&#125;</span> next then`</span>
&#125;)
.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种 onfulfilled 函数返回一个普通值的场景，这里 onfulfilled 函数指的是：</p>
<pre><code class="hljs language-js copyable" lang="js">data => &#123;
  <span class="hljs-built_in">console</span>.log(data)
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;data&#125;</span> next then`</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在之前实现的 then 方法中，就可以创建一个新的 promise2 用以返回：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">onfulfilled, onrejected</span>) </span>&#123;
  onfulfilled = <span class="hljs-keyword">typeof</span> onfulfilled === <span class="hljs-string">'function'</span> ? onfulfilled : <span class="hljs-function"><span class="hljs-params">data</span> =></span> data
  onrejected = <span class="hljs-keyword">typeof</span> onrejected === <span class="hljs-string">'function'</span> ? onrejected : <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123; <span class="hljs-keyword">throw</span> error &#125;
  <span class="hljs-comment">// promise2 将作为 then 方法的返回值</span>
  <span class="hljs-keyword">let</span> promse2
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'fulfilled'</span>) &#123;
    <span class="hljs-keyword">return</span> promse2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-comment">// 这个新的 promse2 resolved 的值为 onfulfilled 的执行结果</span>
          <span class="hljs-keyword">let</span> result = onfulfilled(<span class="hljs-built_in">this</span>.value)
          resolve(result)
        &#125;
        <span class="hljs-keyword">catch</span>(e) &#123;
          reject(e)
        &#125;
      &#125;)
    &#125;)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'rejected'</span>) &#123;
    onrejected(<span class="hljs-built_in">this</span>.reason)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
    <span class="hljs-built_in">this</span>.onFulfilledArray.push(onfulfilled)
    <span class="hljs-built_in">this</span>.onRejectedArray.push(onrejected)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然别忘了 this.status === 'rejected' 状态和 this.status === 'pending' 状态也要加入相同的逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">onfulfilled, onrejected</span>) </span>&#123;
  <span class="hljs-comment">// promise2 将作为 then 方法的返回值</span>
  <span class="hljs-keyword">let</span> promise2
  
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'fulfilled'</span>) &#123;
    <span class="hljs-keyword">return</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-keyword">try</span> &#123;
                    <span class="hljs-comment">// 这个新的 promise2 resolved 的值为 onfulfilled 的执行结果</span>
                    <span class="hljs-keyword">let</span> result = onfulfilled(<span class="hljs-built_in">this</span>.value)
                    resolve(result)
                &#125;
                <span class="hljs-keyword">catch</span>(e) &#123;
                    reject(e)
                &#125;
            &#125;)
    &#125;)
  &#125;
  
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'rejected'</span>) &#123;
    <span class="hljs-keyword">return</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-keyword">try</span> &#123;
                    <span class="hljs-comment">// 这个新的 promise2 reject 的值为 onrejected 的执行结果</span>
                    <span class="hljs-keyword">let</span> result = onrejected(<span class="hljs-built_in">this</span>.value)
                    resolve(result)
                &#125;
                <span class="hljs-keyword">catch</span>(e) &#123;
                    reject(e)
                &#125;
            &#125;)
    &#125;)
  &#125;
  
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
    <span class="hljs-keyword">return</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">this</span>.onFulfilledArray.push(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">let</span> result = onfulfilled(<span class="hljs-built_in">this</span>.value)
          resolve(result)
        &#125;
        <span class="hljs-keyword">catch</span>(e) &#123;
          reject(e)
        &#125;
      &#125;)

      <span class="hljs-built_in">this</span>.onRejectedArray.push(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">let</span> result = onrejected(<span class="hljs-built_in">this</span>.reason)
          resolve(result)
        &#125;
        <span class="hljs-keyword">catch</span>(e) &#123;
          reject(e)
        &#125;
      &#125;)      
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里要重点理解 this.status === 'pending' 判断分支中的逻辑，这也最难理解的。先想想：当使用 Promise 实例，调用其 then 方法时，应该返回一个 Promise 实例，返回的就是 this.status === 'pending' 判断分支中返回的 promise2。那么这个 promise2 什么时候被 resolve 或者 reject 呢？应该是在异步结束，依次执行 onFulfilledArray 或者 onRejectedArray 数组中的函数时。</p>
<p>再思考，那么 onFulfilledArray 或者 onRejectedArray 数组中的函数应该做些什么呢？很明显，需要将 promise2 的状态切换，并 resolve onfulfilled 函数执行结果或者 reject onrejected 结果。</p>
<p>这也就是目前的改动，将 this.onFulfilledArray.push 的函数由：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.onFulfilledArray.push(onfulfilled)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改为：</p>
<pre><code class="hljs language-js copyable" lang="js">() => &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> result = onfulfilled(<span class="hljs-built_in">this</span>.value)
            resolve(result)
        &#125;
        <span class="hljs-keyword">catch</span>(e) &#123;
            reject(e)
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>的原因。 this. onRejectedArray.push 的函数的改动点同理。</p>
<p>继续来实现 then 方法显式返回一个 Promise 实例的情况。对应场景：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'Nordon'</span>)
  &#125;, <span class="hljs-number">2000</span>)
&#125;)

promise.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        resolve(<span class="hljs-string">`<span class="hljs-subst">$&#123;data&#125;</span> next then`</span>)
    &#125;, <span class="hljs-number">3000</span>)
  &#125;)
&#125;)
.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比第一种情况（ onfulfilled 函数和 onrejected 函数返回一个普通值的情况），实现这种 onfulfilled 函数和 onrejected 函数返回一个 Promise 实例也并不困难。但是我们需要小幅度重构一下代码，在上面实现的 let result = onfulfilled(this.value) 语句和 let result = onrejected(this.reason) 语句中，变量 result 由一个普通值会成为一个 Promise 实例。换句话说就是：变量 result 既可以是一个普通值，也可以是一个 Promise 实例，为此抽象出 resolvePromise 方法进行统一处理。改动已有实现为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> resolvePromise = <span class="hljs-function">(<span class="hljs-params">promise2, result, resolve, reject</span>) =></span> &#123; <span class="hljs-comment">// 待完善</span>

&#125;

<span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">onfulfilled, onrejected</span>) </span>&#123;
  <span class="hljs-comment">// promise2 将作为 then 方法的返回值</span>
  <span class="hljs-keyword">let</span> promise2
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'fulfilled'</span>) &#123;
    <span class="hljs-keyword">return</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-keyword">try</span> &#123;
                    <span class="hljs-comment">//这个新的 promise2 resolved 的值为 onfulfilled 的执行结果</span>
                    <span class="hljs-keyword">let</span> result = onfulfilled(<span class="hljs-built_in">this</span>.value)
                    resolvePromise(promise2, result, resolve, reject)
                &#125;
                <span class="hljs-keyword">catch</span>(e) &#123;
                    reject(e)
                &#125;
            &#125;)
    &#125;)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'rejected'</span>) &#123;
    <span class="hljs-keyword">return</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-keyword">try</span> &#123;
                    <span class="hljs-comment">//这个新的 promise2 reject 的值为 onrejected 的执行结果</span>
                    <span class="hljs-keyword">let</span> result = onrejected(<span class="hljs-built_in">this</span>.value)
                 resolvePromise(promise2, result, resolve, reject)
                &#125;
                <span class="hljs-keyword">catch</span>(e) &#123;
                    reject(e)
                &#125;
            &#125;)
    &#125;)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
    <span class="hljs-keyword">return</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">this</span>.onFulfilledArray.push(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">let</span> result = onfulfilled(value)
          resolvePromise(promise2, result, resolve, reject)
        &#125;
        <span class="hljs-keyword">catch</span>(e) &#123;
          reject(e)
        &#125;
      &#125;)

      <span class="hljs-built_in">this</span>.onRejectedArray.push(<span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">let</span> result = onrejected(reason)
          resolvePromise(promise2, result, resolve, reject)
        &#125;
        <span class="hljs-keyword">catch</span>(e) &#123;
          reject(e)
        &#125;
      &#125;)      
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在的任务就是完成 resolvePromise 函数，这个函数接受四个参数：</p>
<ul>
<li>promise2: 返回的 Promise 实例</li>
<li>result: onfulfilled 或者 onrejected 函数的返回值</li>
<li>resolve: promise2 的 resolve 方法</li>
<li>reject: promise2 的 reject 方法</li>
</ul>
<p>有了这些参数，就具备了抽象逻辑的必备条件。接下来就是动手实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> resolvePromise = <span class="hljs-function">(<span class="hljs-params">promise2, result, resolve, reject</span>) =></span> &#123;
  <span class="hljs-comment">// 当 result 和 promise2 相等时，也就是说 onfulfilled 返回 promise2 时，进行 reject</span>
  <span class="hljs-keyword">if</span> (result === promise2) &#123;
    reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'error due to circular reference'</span>))
  &#125;

  <span class="hljs-comment">// 是否已经执行过 onfulfilled 或者 onrejected</span>
  <span class="hljs-keyword">let</span> consumed = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">let</span> thenable

  <span class="hljs-keyword">if</span> (result <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) &#123;
    <span class="hljs-keyword">if</span> (result.status === <span class="hljs-string">'pending'</span>) &#123;
      result.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
        resolvePromise(promise2, data, resolve, reject)
      &#125;, reject)
    &#125; <span class="hljs-keyword">else</span> &#123;
      result.then(resolve, reject)
    &#125;
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-keyword">let</span> isComplexResult = <span class="hljs-function"><span class="hljs-params">target</span> =></span> (<span class="hljs-keyword">typeof</span> target === <span class="hljs-string">'function'</span> || <span class="hljs-keyword">typeof</span> target === <span class="hljs-string">'object'</span>) && (target !== <span class="hljs-literal">null</span>)

  <span class="hljs-comment">// 如果返回的是疑似 Promise 类型</span>
  <span class="hljs-keyword">if</span> (isComplexResult(result)) &#123;
    <span class="hljs-keyword">try</span> &#123;
      thenable = result.then
      <span class="hljs-comment">// 如果返回的是 Promise 类型，具有 then 方法</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> thenable === <span class="hljs-string">'function'</span>) &#123;
        thenable.call(result, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
          <span class="hljs-keyword">if</span> (consumed) &#123;
            <span class="hljs-keyword">return</span>
          &#125;
          consumed = <span class="hljs-literal">true</span>

          <span class="hljs-keyword">return</span> resolvePromise(promise2, data, resolve, reject)
        &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
          <span class="hljs-keyword">if</span> (consumed) &#123;
            <span class="hljs-keyword">return</span>
          &#125;
          consumed = <span class="hljs-literal">true</span>

          <span class="hljs-keyword">return</span> reject(error)
        &#125;)
      &#125;
      <span class="hljs-keyword">else</span> &#123;
        resolve(result)
      &#125;

    &#125; <span class="hljs-keyword">catch</span>(e) &#123;
      <span class="hljs-keyword">if</span> (consumed) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      consumed = <span class="hljs-literal">true</span>
      <span class="hljs-keyword">return</span> reject(e)
    &#125;
  &#125;
  <span class="hljs-keyword">else</span> &#123;
    resolve(result)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，对于 onfulfilled 函数返回的结果 result：如果 result 非 Promise 实例，非对象，非函数类型，是一个普通值的话（上述代码中 isComplexResult 函数进行判断），直接将 promise2 以该值 resolve 掉。</p>
<p>对于 onfulfilled 函数返回的结果 result：如果 result 含有 then 属性方法，称该属性方法为 thenable，说明 result 是一个 Promise 实例，执行该实例的 then 方法（既 thenable），此时的返回结果有可能又是一个 Promise 实例类型，也可能是一个普通值，因此还要递归调用 resolvePromise。</p>
<h3 data-id="heading-5">穿透实现</h3>
<p>看代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'Nordon'</span>)
  &#125;, <span class="hljs-number">2000</span>)
&#125;)


promise.then(<span class="hljs-literal">null</span>)
.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码将会在 2 秒后输出：Nordon。这就是 Promise 穿透现象：</p>
<blockquote>
<p>给 .then() 函数传递非函数值作为其参数时，实际上会被解析成 .then(null)，这时候的表现应该是：上一个 promise 对象的结果进行“穿透”，如果在后面链式调用仍存在第二个 .then() 函数时，将会获取被穿透下来的结果。</p>
</blockquote>
<p>那该如何实现 Promise 穿透呢？</p>
<p>其实很简单，并且我们已经做到了。想想在 then() 方法的实现中：我们已经对 onfulfilled 和 onrejected 函数加上判断：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">onfulfilled = <span class="hljs-built_in">Function</span>.prototype, onrejected = <span class="hljs-built_in">Function</span>.prototype</span>) </span>&#123;
  onfulfilled = <span class="hljs-keyword">typeof</span> onfulfilled === <span class="hljs-string">'function'</span> ? onfulfilled : <span class="hljs-function"><span class="hljs-params">data</span> =></span> data
  onrejected = <span class="hljs-keyword">typeof</span> onrejected === <span class="hljs-string">'function'</span> ? onrejected : <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123; <span class="hljs-keyword">throw</span> error &#125;

    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 onfulfilled 不是函数类型，则给一个默认值，该默认值是返回其参数的函数。onrejected 函数同理。这段逻辑，就是起到了实现“穿透”的作用。</p>
<h3 data-id="heading-6">其他方法&&静态方法</h3>
<h4 data-id="heading-7">catch 实现</h4>
<p>Promise.prototype.catch 可以进行异常捕获，它的典型用法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      reject(<span class="hljs-string">'Nordon error'</span>)
  &#125;, <span class="hljs-number">2000</span>)
&#125;)

promise1.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
&#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(error)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会在 2 秒后输出：Nordon error。</p>
<p>其实在这种场景下，它就相当于：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.catch = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">catchFunc</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>, catchFunc)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为.then() 方法的第二个参数也是进行异常捕获的，通过这个特性，可以比较简单地实现了 Promise.prototype.catch。</p>
<h4 data-id="heading-8">resolve 实现</h4>
<blockquote>
<p>Promise.resolve(value) 方法返回一个以给定值解析后的 Promise 实例对象。</p>
</blockquote>
<p>例子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'data'</span>).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先输出 1 再输出 data。</p>
<p>那么实现 Promise.resolve(value) 也很简单：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(value)
  &#125;)
&#125;

<span class="hljs-comment">// 其实 reject 同理</span>
<span class="hljs-built_in">Promise</span>.reject = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    reject(value)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">all 实现</h4>
<blockquote>
<p>Promise.all(iterable) 方法返回一个 Promise 实例，此实例在 iterable 参数内所有的 promise 都“完成（resolved）”或参数中不包含 promise 时回调完成（resolve）；如果参数中 promise 有一个失败（rejected），此实例回调失败（reject），失败原因的是第一个失败 promise 的结果。</p>
</blockquote>
<p>例子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'Nordon'</span>)
  &#125;, <span class="hljs-number">2000</span>)
&#125;)

<span class="hljs-keyword">const</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'WY'</span>)
  &#125;, <span class="hljs-number">2000</span>)
&#125;)

<span class="hljs-built_in">Promise</span>.all([promise1, promise2]).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将在 2 秒后输出：["Nordon", "WY"]。</p>
<p>实现思路:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.all = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">promiseArray</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(promiseArray)) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'The arguments should be an array!'</span>)
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">let</span> resultArray = []

      <span class="hljs-keyword">const</span> length = promiseArray.length

      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <length; i++) &#123;
        promiseArray[i].then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
          resultArray.push(data)

          <span class="hljs-keyword">if</span> (resultArray.length === length) &#123;
            resolve(resultArray)
          &#125;
        &#125;, reject)
      &#125;
    &#125;
    <span class="hljs-keyword">catch</span>(e) &#123;
      reject(e)
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先进行了对参数 promiseArray 的类型判断，对于非数组类型参数，进行抛错。Promise.all 会返回一个 Promise 实例，这个实例将会在 promiseArray 中的所有 Promise 实例 resolve 后进行 resolve，且 resolve 的值是一个数组，这个数组存有 promiseArray 中的所有 Promise 实例 resolve 的值。</p>
<p>整体思路依赖一个 for 循环对 promiseArray 进行遍历。同样按照这个思路，继续对 Promise.race 进行实现。</p>
<h4 data-id="heading-10">race 实现</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.race = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">promiseArray</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(promiseArray)) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'The arguments should be an array!'</span>)
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">const</span> length = promiseArray.length
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <length; i++) &#123;
        promiseArray[i].then(resolve, reject)
      &#125;
    &#125;
    <span class="hljs-keyword">catch</span>(e) &#123;
      reject(e)
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单分析一下，这里使用 for 循环同步执行 promiseArray 数组中的所有 promise 实例 then 方法，第一个 resolve 的实例直接会触发新 Promise（代码中新 new 出来的） 实例的 resolve 方法</p>
<h3 data-id="heading-11">完整代码</h3>
<p>截止目前本文已经对根据<a href="https://promisesaplus.com/" target="_blank" rel="nofollow noopener noreferrer">Promise/A+</a>的常用<code>API</code>实现了简单版本的<code>Promise</code></p>
<p>整体代码如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">executor</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'pending'</span>
  <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">null</span>
  <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">null</span>
  <span class="hljs-built_in">this</span>.onFulfilledArray = []
  <span class="hljs-built_in">this</span>.onRejectedArray = []

  <span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (value <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) &#123;
      <span class="hljs-keyword">return</span> value.then(resolve, reject)
    &#125;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.value = value
        <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'fulfilled'</span>

        <span class="hljs-built_in">this</span>.onFulfilledArray.forEach(<span class="hljs-function"><span class="hljs-params">func</span> =></span> &#123;
          func(value)
        &#125;)
      &#125;
    &#125;)
  &#125;

  <span class="hljs-keyword">const</span> reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.reason = reason
        <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'rejected'</span>

        <span class="hljs-built_in">this</span>.onRejectedArray.forEach(<span class="hljs-function"><span class="hljs-params">func</span> =></span> &#123;
          func(reason)
        &#125;)
      &#125;
    &#125;)
  &#125;


    <span class="hljs-keyword">try</span> &#123;
        executor(resolve, reject)
    &#125; <span class="hljs-keyword">catch</span>(e) &#123;
        reject(e)
    &#125;
&#125;

<span class="hljs-keyword">const</span> resolvePromise = <span class="hljs-function">(<span class="hljs-params">promise2, result, resolve, reject</span>) =></span> &#123;
  <span class="hljs-comment">// 当 result 和 promise2 相等时，也就是说 onfulfilled 返回 promise2 时，进行 reject</span>
  <span class="hljs-keyword">if</span> (result === promise2) &#123;
    <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'error due to circular reference'</span>))
  &#125;

  <span class="hljs-comment">// 是否已经执行过 onfulfilled 或者 onrejected</span>
  <span class="hljs-keyword">let</span> consumed = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">let</span> thenable

  <span class="hljs-keyword">if</span> (result <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) &#123;
    <span class="hljs-keyword">if</span> (result.status === <span class="hljs-string">'pending'</span>) &#123;
      result.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
        resolvePromise(promise2, data, resolve, reject)
      &#125;, reject)
    &#125; <span class="hljs-keyword">else</span> &#123;
      result.then(resolve, reject)
    &#125;
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-keyword">let</span> isComplexResult = <span class="hljs-function"><span class="hljs-params">target</span> =></span> (<span class="hljs-keyword">typeof</span> target === <span class="hljs-string">'function'</span> || <span class="hljs-keyword">typeof</span> target === <span class="hljs-string">'object'</span>) && (target !== <span class="hljs-literal">null</span>)
  <span class="hljs-comment">// 如果返回的是疑似 Promise 类型</span>
  <span class="hljs-keyword">if</span> (isComplexResult(result)) &#123;
    <span class="hljs-keyword">try</span> &#123;
      thenable = result.then
      <span class="hljs-comment">// 如果返回的是 Promise 类型，具有 then 方法</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> thenable === <span class="hljs-string">'function'</span>) &#123;
        thenable.call(result, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
          <span class="hljs-keyword">if</span> (consumed) &#123;
            <span class="hljs-keyword">return</span>
          &#125;
          consumed = <span class="hljs-literal">true</span>

          <span class="hljs-keyword">return</span> resolvePromise(promise2, data, resolve, reject)
        &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
          <span class="hljs-keyword">if</span> (consumed) &#123;
            <span class="hljs-keyword">return</span>
          &#125;
          consumed = <span class="hljs-literal">true</span>

          <span class="hljs-keyword">return</span> reject(error)
        &#125;)
      &#125;
      <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> resolve(result)
      &#125;

    &#125; <span class="hljs-keyword">catch</span>(e) &#123;
      <span class="hljs-keyword">if</span> (consumed) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      consumed = <span class="hljs-literal">true</span>
      <span class="hljs-keyword">return</span> reject(e)
    &#125;
  &#125;
  <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> resolve(result)
  &#125;
&#125;

<span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">onfulfilled, onrejected</span>) </span>&#123;
  onfulfilled = <span class="hljs-keyword">typeof</span> onfulfilled === <span class="hljs-string">'function'</span> ? onfulfilled : <span class="hljs-function"><span class="hljs-params">data</span> =></span> data
  onrejected = <span class="hljs-keyword">typeof</span> onrejected === <span class="hljs-string">'function'</span> ? onrejected : <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;<span class="hljs-keyword">throw</span> error&#125;

  <span class="hljs-comment">// promise2 将作为 then 方法的返回值</span>
  <span class="hljs-keyword">let</span> promise2

  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'fulfilled'</span>) &#123;
    <span class="hljs-keyword">return</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-comment">// 这个新的 promise2 resolved 的值为 onfulfilled 的执行结果</span>
          <span class="hljs-keyword">let</span> result = onfulfilled(<span class="hljs-built_in">this</span>.value)
          resolvePromise(promise2, result, resolve, reject)
        &#125;
        <span class="hljs-keyword">catch</span>(e) &#123;
          reject(e)
        &#125;
      &#125;)
    &#125;)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'rejected'</span>) &#123;
    <span class="hljs-keyword">return</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-comment">// 这个新的 promise2 reject 的值为 onrejected 的执行结果</span>
         <span class="hljs-keyword">let</span> result = onrejected(<span class="hljs-built_in">this</span>.reason)
         resolvePromise(promise2, result, resolve, reject)
        &#125;
        <span class="hljs-keyword">catch</span>(e) &#123;
          reject(e)
        &#125;
      &#125;)
    &#125;)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
    <span class="hljs-keyword">return</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">this</span>.onFulfilledArray.push(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">let</span> result = onfulfilled(value)
          resolvePromise(promise2, result, resolve, reject)
        &#125;
        <span class="hljs-keyword">catch</span>(e) &#123;
          <span class="hljs-keyword">return</span> reject(e)
        &#125;
      &#125;)

      <span class="hljs-built_in">this</span>.onRejectedArray.push(<span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">let</span> result = onrejected(reason)
          resolvePromise(promise2, result, resolve, reject)
        &#125;
        <span class="hljs-keyword">catch</span>(e) &#123;
          <span class="hljs-keyword">return</span> reject(e)
        &#125;
      &#125;)      
    &#125;)
  &#125;
&#125;

<span class="hljs-built_in">Promise</span>.prototype.catch = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">catchFunc</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>, catchFunc)
&#125;

<span class="hljs-built_in">Promise</span>.resolve = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    resolve(value)
  &#125;)
&#125;

<span class="hljs-built_in">Promise</span>.reject = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    reject(value)
  &#125;)
&#125;

<span class="hljs-built_in">Promise</span>.race = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">promiseArray</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(promiseArray)) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'The arguments should be an array!'</span>)
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">const</span> length = promiseArray.length
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <length; i++) &#123;
        promiseArray[i].then(resolve, reject)
      &#125;
    &#125;
    <span class="hljs-keyword">catch</span>(e) &#123;
      reject(e)
    &#125;
  &#125;)
&#125;

<span class="hljs-built_in">Promise</span>.all = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">promiseArray</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(promiseArray)) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'The arguments should be an array!'</span>)
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">let</span> resultArray = []

      <span class="hljs-keyword">const</span> length = promiseArray.length

      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <length; i++) &#123;
        promiseArray[i].then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
          resultArray.push(data)

          <span class="hljs-keyword">if</span> (resultArray.length === length) &#123;
            resolve(resultArray)
          &#125;
        &#125;, reject)
      &#125;
    &#125;
    <span class="hljs-keyword">catch</span>(e) &#123;
      reject(e)
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            