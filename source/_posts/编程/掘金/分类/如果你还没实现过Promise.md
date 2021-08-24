
---
title: '如果你还没实现过Promise'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8756'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 01:03:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=8756'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">前言</h2>
<p>手写<code>Promise</code>，老生常谈的话题，但是实际使用时，难免还是会踩坑，今天就来一步步实现它，摸摸它到底是何方神圣。如果你还没有手写过 Promise，或者你想温习下 Promise 的实现，获取你可以看看这边文章。</p>
<p>接下来就是一步步实现一个符合 <strong>PromiseA+</strong> 规范的Promise的过程。</p>
<p>喏，这里：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpromisesaplus.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://promisesaplus.com/" ref="nofollow noopener noreferrer">PromiseA+</a></p>
<h2 data-id="heading-1">V0：基本实现</h2>
<p><strong>Promise状态</strong>：<code>pending</code>(等待)、<code>fulfilled</code>(成功)、<code>rejected</code>(失败)</p>
<h3 data-id="heading-2">Promise的雏形</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'pending'</span> <span class="hljs-comment">// 状态</span>
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 成功的结果</span>
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 失败的原因</span>

    <span class="hljs-keyword">let</span> resolve = <span class="hljs-function">() =></span> &#123;&#125;
    <span class="hljs-keyword">let</span> reject = <span class="hljs-function">() =></span> &#123;&#125;

    executor(resolve, reject)
  &#125;

  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">executor 容错</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 传入的执行函数可能会抛出错误</span>
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// 将resolve和reject给使用者</span>
      executor(resolve, reject)
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-comment">// error注入reject</span>
      reject(e)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">resolve 和 reject 方法</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 定义resolve</span>
    <span class="hljs-keyword">let</span> resolve = <span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
      <span class="hljs-comment">// 只能从pending变为fulfilled或者rejected状态</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'fulfilled'</span>
        <span class="hljs-built_in">this</span>.value = data
      &#125;
    &#125;
    <span class="hljs-comment">// 定义reject</span>
    <span class="hljs-keyword">let</span> reject = <span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
      <span class="hljs-comment">// 只能从pending变为fulfilled或者rejected状态</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'rejected'</span>
        <span class="hljs-built_in">this</span>.reason = data
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">then 方法</h3>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// 定义then方法，将fulfilled或者rejected的结果传入onFulfilled或者onRejected中</span>
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'fulfilled'</span>) &#123;
      onFulfilled(<span class="hljs-built_in">this</span>.value)
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'rejected'</span>) &#123;
      onRejected(<span class="hljs-built_in">this</span>.reason)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么，一个简单的实现就完成啦。</p>
<p><strong>小测试：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> resolve(<span class="hljs-number">1</span>))
p.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res)) <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子可以正常输出结果，但是，如果Promise内部是异步的呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> q = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-number">2</span>)
  &#125;, <span class="hljs-number">0</span>)
&#125;)
q.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res)) <span class="hljs-comment">// 并没有输出</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于异步延迟，调用then方法时，状态还是 pending，无法调用onFulfilled或者onRejected，那么我们需要对异步的情况做相应的处理。</p>
<h2 data-id="heading-6">V1：加入异步处理</h2>
<p><strong>怎么处理异步情况？</strong></p>
<p>针对上面的分析，调用then方法时还是 pending 状态，那么此时应该将回调函数存起来，等到状态改变（fulfilled / rejected）时再取出来调用。考虑到可能存在多个回调函数，我们使用数组存储回调函数，形成回调队列。</p>
<h3 data-id="heading-7">1. 定义两个数组作为回调队列</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.onResolvedCallbacks = [] <span class="hljs-comment">// 存放成功的回调</span>
<span class="hljs-built_in">this</span>.onRejectedCallbacks = [] <span class="hljs-comment">// 存放失败的回调</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2. then 方法中处理 pending 状态下的回调函数</h3>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'fulfilled'</span>) &#123;
      onFulfilled(<span class="hljs-built_in">this</span>.value)
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'rejected'</span>) &#123;
      onRejected(<span class="hljs-built_in">this</span>.reason)
    &#125;
    <span class="hljs-comment">// 新增：当 Promise还是等待状态，存储回调函数</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
      <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(onFulfilled)
      <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(onRejected)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3. 调用回调队列的函数</h3>
<p><strong>什么时候调用回调队列？</strong></p>
<p>由于 resolve 或者 reject 时是在异步队列里，我们在 then 中已经存储了相应的回调函数，那么当状态改变时，即在 resolve 或者 reject 发生时，就可以将回调函数取出来依次调用。</p>
<p>修改下constructor 方法：</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> resolve = <span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'fulfilled'</span>
        <span class="hljs-built_in">this</span>.value = data
        <span class="hljs-comment">// 状态改变后取出回调队列的函数依次调用</span>
        <span class="hljs-built_in">this</span>.onResolvedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb(<span class="hljs-built_in">this</span>.value))
      &#125;
    &#125;
    <span class="hljs-keyword">let</span> reject = <span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.status = <span class="hljs-string">'rejected'</span>
        <span class="hljs-built_in">this</span>.reason = data
        <span class="hljs-comment">// 状态改变后取出回调队列的函数依次调用</span>
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb(<span class="hljs-built_in">this</span>.reason))
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在存储回调函数时，value 或者 reason还没有值，等到状态改变时才拿到值，因此依次调用回调队列的函数时将相应的 value 或者 reason 传入。</p>
<p><strong>测试一下加入异步是否可以正常输出</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> q = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    resolve(<span class="hljs-number">2</span>)
  &#125;, <span class="hljs-number">0</span>)
&#125;)
q.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res)) <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>异步处理，完成。</p>
<p>就这？但是，别忘了还有 Promise 的<strong>链式调用</strong>呢！</p>
<h2 data-id="heading-10">V2：实现链式调用</h2>
<p>基于前面的实现是没法实现链式调用的。</p>
<pre><code class="hljs language-js copyable" lang="js">q.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res)
  <span class="hljs-keyword">return</span> <span class="hljs-number">3</span>
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res)) <span class="hljs-comment">// Uncaught TypeError: Cannot read property 'then' of undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>别忘了Promises/A+规范要求：then 方法返回新的 Promise。</p>
<p>接下来完善 then 方法</p>
<h3 data-id="heading-11">规范化then 参数：onFulfilled 和 onRejected</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// onFulfilled 和 onRejected 为函数</span>
    <span class="hljs-comment">// onFulfilled 不是函数时包装成函数，返回传入的值</span>
    onFulfilled =
      <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">'function'</span> ? onFulfilled : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value
    <span class="hljs-comment">// onRejected 不是函数时，需要抛出错误，否则会在后面的链式调用被resolve捕获</span>
    onRejected =
      <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span> ? onRejected : <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;<span class="hljs-keyword">throw</span> error&#125;    
      
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">then 方法返回新的 Promise，并加入 try...catch</h3>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-comment">// onFulfilled 和 onRejected 为函数</span>
    <span class="hljs-comment">// onFulfilled 不是函数时包装成函数，返回传入的值</span>
    onFulfilled =
      <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">'function'</span> ? onFulfilled : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value
    <span class="hljs-comment">// onRejected 不是函数时需要抛出错误，否则会在后面的链式调用被resolve捕获！！！</span>
    onRejected =
      <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span>
        ? onRejected
        : <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
            <span class="hljs-keyword">throw</span> error
          &#125;

    <span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'fulfilled'</span>) &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value)
          resolve(x)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          reject(e)
        &#125;
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'rejected'</span>) &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.reason)
          resolve(x)
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          reject(e)
        &#125;
      &#125;
      <span class="hljs-comment">// 当 Promise还是等待状态，存储回调函数</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value)
            resolve(x)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;)
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.reason)
            resolve(x)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;)
      &#125;
    &#125;)
    <span class="hljs-keyword">return</span> promise
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这下再执行链式调用就不报错了</p>
<pre><code class="hljs language-js copyable" lang="js">q.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res)
  <span class="hljs-keyword">return</span> <span class="hljs-number">3</span>
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res)) <span class="hljs-comment">// 一次输出 2 3</span>

q.then()then().then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res)) <span class="hljs-comment">// 2, 依次传递，因此输出2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里，基本就实现了支持链式调用的Promise了。</p>
<p>但是，但是，但是，是的，又双叒但是了，onFulfilled 和 onRejected 里面我们可以返回任何值，原始数据类型、引用类型、甚至是Promise！基于上面的实现，还不足以处理所有的返回值。不信你看：</p>
<pre><code class="hljs language-js copyable" lang="js">q.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res)
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> resolve(<span class="hljs-number">3</span>))
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res)) <span class="hljs-comment">// 依次输出 2 MyPromise</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是实际上，Promise 针对 onFulfilled 和 onRejected 里面返回 Promise 时，是会步步往里走，直到拿到一个里面的值的。也就是说，他实际上会输出 2 3。</p>
<p>这就迎来了下一版本。</p>
<p>我们将 then 中的 resolve 的逻辑抽取出来，用完善版的 <strong>resolvePromise</strong> 代替。</p>
<h2 data-id="heading-13">V3：引入 resolvePromise 方法</h2>
<p><strong>我们希望这个函数处理什么呢？</strong></p>
<ul>
<li>处理 onFulfilled 和 onRejected 的返回值 x，onFulfilled 时需要 resolve，onRejected 时需要 reject</li>
<li>循环引用：当 then 的返回值 promise 与 x 是同一引用时，抛出TypeError错误（2.3.1）</li>
</ul>
<h3 data-id="heading-14">resolvePromise需要的参数</h3>
<p>基于上面的分析，这个函数长这样</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 处理then里面onFulfilled或onRejected的返回值
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> </span>promise then方法返回的Promise对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>x onFulfilled或onRejected的返回值
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Function&#125;</span> </span>resolve Promise构造函数的resolve方法
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Function&#125;</span> </span>reject Promise构造函数的reject方法
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">promise, x, resolve, reject</span>) </span>&#123;
  <span class="hljs-comment">// </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">循环引用时抛出 TypeError 错误</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (promise === x) &#123;
    <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Promise循环引用啦'</span>))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">处理返回值</h3>
<p>大概如此：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// 返回值x 为 Promise（2.3.2）</span>
  <span class="hljs-comment">// 这一节其实可以省略，因为在下面对then的处理中已经包含了</span>
  <span class="hljs-comment">// if (x instanceof Promise) &#123;&#125;</span>

  <span class="hljs-comment">// 返回值x是对象或者函数（2.3.3）包含x为Promise的情况（2.3.2）</span>
  <span class="hljs-keyword">if</span> (x !== <span class="hljs-literal">null</span> && (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'object'</span> || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'function'</span>)) &#123;
    <span class="hljs-comment">// try...catch 防止then出现异常</span>
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">let</span> then = x.then <span class="hljs-comment">// （2.3.3.1）</span>
      /
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      reject(e) <span class="hljs-comment">// (2.3.3.2)(2.3.3.3.4.2)</span>
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 返回值x只是一个普通值（2.3.4）</span>
    resolve(x)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，处理下返回值的复杂场景</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// 返回值x 为 Promise（2.3.2）</span>
  <span class="hljs-comment">// 这一节其实可以省略，因为在下面对then的处理中已经包含了</span>
  <span class="hljs-comment">// if (x instanceof Promise) &#123;&#125;</span>

  <span class="hljs-keyword">let</span> called = <span class="hljs-literal">false</span> <span class="hljs-comment">// 是否 resolve 或者 reject了</span>
  <span class="hljs-comment">// 返回值x是对象或者函数（2.3.3）包含x为Promise的情况（2.3.2）</span>
  <span class="hljs-keyword">if</span> (x !== <span class="hljs-literal">null</span> && (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'object'</span> || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'function'</span>)) &#123;
    <span class="hljs-comment">// try...catch 防止then出现异常</span>
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">let</span> then = x.then <span class="hljs-comment">// （2.3.3.1）</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> then === <span class="hljs-string">'function'</span>) &#123;
        <span class="hljs-comment">//  返回值x有then且then是一个函数，则调用它，并将this指向x（2.3.3.3）</span>
        then.call(
          x,
          <span class="hljs-function"><span class="hljs-params">y</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span> <span class="hljs-comment">// 已经 resolve 或者 reject了， 则忽略(2.3.3.3.3)</span>
            called = <span class="hljs-literal">true</span>
            <span class="hljs-comment">// y有可能还是一个Promise，递归处理</span>
            resolvePromise(promise, y, resolve, reject)
          &#125;,
          <span class="hljs-function"><span class="hljs-params">r</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span> <span class="hljs-comment">// 已经 resolve 或者 reject了， 则忽略(2.3.3.3.3)</span>
            called = <span class="hljs-literal">true</span>
            reject(r)
          &#125;
        )
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 只是一个普通对象或者普通函数，则直接resolve</span>
        resolve(x)
      &#125;
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span> <span class="hljs-comment">// 已经 resolve 或者 reject了， 则忽略(2.3.3.3.4.1)</span>
      called = <span class="hljs-literal">true</span>
      reject(e) <span class="hljs-comment">// (2.3.3.2)(2.3.3.3.4.2)</span>
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 返回值x只是一个普通值（2.3.4）</span>
    resolve(x)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">V4: 给then中所有的返回加上异步延迟（标准版）</h2>
<p>这里使用setTimeout模拟延迟</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
    
    <span class="hljs-keyword">let</span> promise
    promise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'fulfilled'</span>) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value)
            resolvePromise(promise, x, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;, <span class="hljs-number">0</span>)
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'rejected'</span>) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.reason)
            resolvePromise(promise, x, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e)
          &#125;
        &#125;, <span class="hljs-number">0</span>)
      &#125;
      <span class="hljs-comment">// 当 Promise还是等待状态，存储回调函数</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value)
              resolvePromise(promise, x, resolve, reject)
            &#125; <span class="hljs-keyword">catch</span> (e) &#123;
              reject(e)
            &#125;
          &#125;, <span class="hljs-number">0</span>)
        &#125;)
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.reason)
              resolvePromise(promise, x, resolve, reject)
            &#125; <span class="hljs-keyword">catch</span> (e) &#123;
              reject(e)
            &#125;
          &#125;, <span class="hljs-number">0</span>)
        &#125;)
      &#125;
    &#125;)
    <span class="hljs-keyword">return</span> promise
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>标准版实现：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMiKiMiKi-Lin%2Ffront-end-notes%2Fblob%2Fworking%2FHandwriting%2FPromise.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MiKiMiKi-Lin/front-end-notes/blob/working/Handwriting/Promise.js" ref="nofollow noopener noreferrer">MyPromise</a></p>
<h2 data-id="heading-18">测试是否符合PromiseA+规范</h2>
<p>使用 <code>promises-aplus-tests</code> 这个库，测试你的Promise是否符合PromiseA+</p>
<pre><code class="copyable">yarn add promises-aplus-tests
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试前，需要在你的Promise结尾加上:</p>
<pre><code class="hljs language-js copyable" lang="js">MyPromise.defer = MyPromise.deferred = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> defer = &#123;&#125;
  defer.promise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    defer.resolve = resolve
    defer.reject = reject
  &#125;)
  <span class="hljs-keyword">return</span> defer
&#125;
<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-built_in">module</span>.exports = MyPromise
&#125; <span class="hljs-keyword">catch</span> (e) &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面就可以测试了</p>
<pre><code class="copyable">npx promises-aplus-tests Promise.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于上面的实现，可以看到一连串绿勾勾，最后看到 <code>872 passing (17s)</code>，通过了测试。</p>
<h2 data-id="heading-19">V5: 加上周边方法（现代完整版）</h2>
<p>其实基于V4已经够用了，也通过了测试。但是使用Promise时，我们是可以直接使用<code>Promise.resolve</code>、<code>Promise、reject</code>等方法的，V5即在V4的基础上，补充了<code>resolve、reject、catch、finally、all、race、allSettled</code>等的实现。这里称之为 “现代完整版”。</p>
<p>现代完整版实现：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMiKiMiKi-Lin%2Ffront-end-notes%2Fblob%2Fworking%2FHandwriting%2FPromise_Pro.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MiKiMiKi-Lin/front-end-notes/blob/working/Handwriting/Promise_Pro.js" ref="nofollow noopener noreferrer">Promise_pro</a></p>
<h2 data-id="heading-20">Q & A</h2>
<p><strong>1. 为何又谈论这个被谈烂的话题？</strong></p>
<p>时常回顾和温习，是非天资聪颖者最后的倔强。若同样有助于你，万分荣幸。</p>
<p><strong>2. 为什么给then中所有的返回加上延迟要使用setTimeout？</strong></p>
<p>首先，Promise 本身是同步的，其 then 和 catch 方法是异步的， 这里使用 setTimeout 模拟异步，是符合Promise A+规范的，也通过了测试，当然你也可以使用其它方法，如 <strong>MutationObserver</strong>。</p>
<p>虽然在 Eventloop 中setTimeout 属于宏任务，而实际上，Promise 的 then和 catch 是属于微任务队列，该实现与实际是有些许差异的，但这并影响我们通过手写一个符合 Promise A+ 规范的 Promise 去理解它的原理。</p>
<h2 data-id="heading-21">参考</h2>
<p>感谢大佬铺路，助我前行</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpromisesaplus.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://promisesaplus.com/" ref="nofollow noopener noreferrer">PromiseA+</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F21834559" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/21834559" ref="nofollow noopener noreferrer">史上最易读懂的 Promise/A+ 完全实现</a></li>
<li><a href="https://juejin.cn/post/6997968693414084644#" target="_blank" title="https://juejin.cn/post/6997968693414084644#">Promise之你看得懂的Promise</a></li>
</ul></div>  
</div>
            