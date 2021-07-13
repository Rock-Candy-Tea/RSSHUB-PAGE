
---
title: '轻松入门前端【3】—— Promise'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cd7b42d60c8451586ddd65f61f6251b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 21:59:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cd7b42d60c8451586ddd65f61f6251b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Promise</h2>
<h3 data-id="heading-1">特性</h3>
<h4 data-id="heading-2">创建实例</h4>
<p>一：使用构造函数创建，该方式接受一个回调函数，其中会传进去 <code>resolve</code> 和 <code>reject</code> 方法</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  resolve(<span class="hljs-string">'data'</span>)
&#125;)

promise.then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)                         <span class="hljs-comment">// data，后打印</span>
&#125;)

<span class="hljs-built_in">console</span>.log(promise <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>)     <span class="hljs-comment">// true，先打印</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>该方法的好处是灵活，可以控制创建 promise 实例时做的额外操作，但是代码比较累赘</p>
<p>代码执行构造函数时是同步的，只有开始链式调用的时候才是异步</p>
</blockquote>
<p>二：使用静态方法 <code>Promise.resolve()</code> 或 <code>Promise.reject()</code> 创建</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> promise = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'data'</span>)
promise.then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)       <span class="hljs-comment">// data</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>Promise.resolve()</code> 是 <code>new Promise((resolve) => &#123; resolve() &#125;)</code> 的语法糖，功能完全一样，reject 方法同理</p>
<p>Promise 的链式调用过程中，每一次链式调用链式方法（如 <code>resolve</code>、<code>reject</code>、<code>then</code> 、<code>catch</code>、<code>finally</code>）返回的都是一个全新的 promise 实例，因此该方法自然也可以当成创建 promise 使用</p>
</blockquote>
<p>声明实例是是同步操作，只有开始链式调用才会产生异步任务</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
  resolve(<span class="hljs-string">'promise'</span>)
&#125;)

<span class="hljs-keyword">const</span> promiseTask = promise.then(<span class="hljs-function">() =></span> <span class="hljs-string">'promiseTask'</span>)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'同步任务开始.....'</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise:'</span>)
<span class="hljs-built_in">console</span>.log(promise)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promiseTask:'</span>)
<span class="hljs-built_in">console</span>.log(promiseTask)

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'异步任务开始.....'</span>)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise:'</span>)
  <span class="hljs-built_in">console</span>.log(promise)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promiseTask:'</span>)
  <span class="hljs-built_in">console</span>.log(promiseTask)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cd7b42d60c8451586ddd65f61f6251b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h4 data-id="heading-3">状态变更</h4>
<p>Promise 有三种状态：</p>
<ul>
<li>Pending：进行中</li>
<li>Resolved：已完成（该状态也称为 <code>fulfilled</code>）</li>
<li>Rejected：已失败</li>
</ul>
<p>其中状态更改只有两种：</p>
<ul>
<li>Pending → Resolved</li>
<li>Pending → Rejected</li>
</ul>
<blockquote>
<p>一个 promise 的状态从 pengding 进到另一任意状态时，该 promise 的状态就会一直停留在该状态，无法被更改</p>
<p>链式调用中如果没有发生错误，则都是 <code>pending → resolved</code> 的状态转变</p>
</blockquote>
<hr>
<h4 data-id="heading-4">异步阻塞</h4>
<p>在 promise 的链式调用中，会等待上一个 promise 的状态置为非 <code>pending</code> 才会开始执行下一个，这里需要注意的是，阻塞只对 promise 有效，无法直接作用于其他异步函数</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-built_in">Promise</span>.resolve()
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行了setTimeout方法'</span>)
    &#125;)
  &#125;)
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'任务完成'</span>)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c200365f800408da9de7262bb7d13de~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如果想阻塞这些任务需要用 promise 进行封装</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-built_in">Promise</span>.resolve()
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行了setTimeout方法'</span>)
        resolve()
      &#125;)
    &#125;)
  &#125;)
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'任务完成'</span>)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ba7f75e0b0e4211b791757e87fcd2f4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h4 data-id="heading-5">数据传递</h4>
<p>promise 的数据传递只能由下一个链式调用接受上一个数据，无法跨级传递数据</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'A'</span>)
  .then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data)<span class="hljs-comment">// A</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">'B'</span>
  &#125;)
  .then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data)<span class="hljs-comment">// B</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>then 的回调方法中使用的是 <code>return</code> 传递结果，而 Promise 使用 <code>resolve</code> 传递结果，这是因为编译器会将 then 中 return 的值解析为 <code>return Promise.resolve(...)</code>，相当于返回了一个新的 promise 实例</p>
</blockquote>
<hr>
<h4 data-id="heading-6">错误处理</h4>
<p>promise 使用 <code>reject</code> 和 <code>catch</code> 捕获错误</p>
<blockquote>
<p>reject 方法返回的是一个失败状态的 promise，用于抛出错误</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> promise =  <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    reject(<span class="hljs-string">'出大事儿啦!!!'</span>)
  &#125;)
&#125;)

<span class="hljs-built_in">console</span>.log(promise)

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(promise)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/288e79b6686742a7bc03b972d0cb5257~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>catch 方法返回的是一个成功状态的 promise，用于处理错误</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> promise =  <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'出大事儿啦！！！'</span>)
&#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err)
    <span class="hljs-keyword">return</span> <span class="hljs-string">'错误信息'</span>
  &#125;)

<span class="hljs-built_in">console</span>.log(promise)

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(promise)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d22813283604a97ae8b6b8e988ef836~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>关联关系：</p>
<ul>
<li>上一个 promise 置为 reject 状态后，其数据会被传入下个 then 方法的第二个回调函数，如果没有进行该回调函数的声明，则数据会被之后的 catch 方法捕获</li>
<li>如果是网络原因造成的错误，则错误只能由 catch 捕获</li>
</ul>
<blockquote>
<p>所以一般直接用 catch 方法就完事儿了</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> promise =  <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'出大事儿啦!!!'</span>)
  .then(
    <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;<span class="hljs-built_in">console</span>.log(data)&#125;,      <span class="hljs-comment">// 无数据打印</span>
    <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;<span class="hljs-built_in">console</span>.log(err)&#125;         <span class="hljs-comment">// 出大事儿啦!!!</span>
  )
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> promise =  <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'出大事儿啦!!!'</span>)
  .then(
    <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;&#125;,      
    <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;&#125;                
  )
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err)                    <span class="hljs-comment">// 无数据打印，因为错误已经在之前被捕获到了</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>处理顺序：如果其中一个 promise 置为了失败状态，则在错误捕获前的 promise 任务不会被执行</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// > 3、4任务不会被执行，使用then的第二个回调函数的方式捕获错误同样功能</span>
<span class="hljs-built_in">Promise</span>.resolve()
  .then(<span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行第1个任务'</span>)&#125;)
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行第2个任务'</span>)
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'出大事儿啦!!!'</span>)
  &#125;)
  .then(<span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行第3个任务'</span>)&#125;)
  .then(<span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行第4个任务'</span>)&#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行第5个任务'</span>)
    <span class="hljs-built_in">console</span>.log(err)
  &#125;)
  .then(<span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行第6个任务'</span>)&#125;)
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da3e54a667fb4202be4a4a0f1ad9889a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如果存在多个错误，则捕获 <code>出现错误 → 捕获</code> 过程中最开始的错误</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'出大事儿啦!!!'</span>)
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'又出大事儿啦!!!'</span>)
  &#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err)                      <span class="hljs-comment">// 出大事儿啦!!!</span>
  &#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err)                      <span class="hljs-comment">// 无数据打印</span>
  &#125;)
  .then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'又又出大事儿啦!!!'</span>)
  &#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err)                      <span class="hljs-comment">// 又又出大事儿啦!!!</span>
  &#125;)
  
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-7">Promise方法</h3>
<h4 data-id="heading-8">链式调用</h4>
<p><strong>promise.then (callback?, errorCallback?)</strong></p>
<ul>
<li>功能：链式调用下一个任务</li>
<li>参数：
<ul>
<li><code>callback?: function(data)</code>：
<ul>
<li>data：上一个 promise 成功时传递的数据</li>
</ul>
</li>
<li><code>errorCallback?: function(error)</code>：
<ul>
<li>error： <code>出现错误 → 捕获</code> 过程中最开始的错误</li>
</ul>
</li>
</ul>
</li>
<li>返回值：<code>Promise</code>：返回一个新的 promise</li>
</ul>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">'传递的数据'</span>)
  .then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data)       <span class="hljs-comment">// 传递的数据</span>
  &#125;)
  .then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data)       <span class="hljs-comment">// undefined，因为上一个promise没有值传递</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>promise.catch (callback?)</strong></p>
<ul>
<li>功能：捕获链式任务过程中的错误</li>
<li>参数：
<ul>
<li><code>callback?: function(error)</code>：
<ul>
<li>error： <code>出现错误 → 捕获</code> 过程中最开始的错误</li>
</ul>
</li>
</ul>
</li>
<li>返回值：<code>Promise</code>：返回一个新的 promise</li>
</ul>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'出大事儿啦!!!'</span>)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err)      <span class="hljs-comment">// 出大事儿啦!!!</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>promise.finally (callback?)</strong></p>
<ul>
<li>功能：无论任务链是否有报错，都会执行该方法</li>
<li>参数：
<ul>
<li><code>callback?: function()</code>：执行内容</li>
</ul>
</li>
<li>返回值：<code>Promise</code>：返回一个新的 promise</li>
</ul>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  resolve()
&#125;)
  .then(<span class="hljs-function">() =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    reject()
  &#125;))
  .finally(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'任务完毕'</span>)       <span class="hljs-comment">// 任务完毕</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h4 data-id="heading-9">并行处理</h4>
<p><strong>Promise.all (promiseTasks)</strong></p>
<ul>
<li>功能：并行处理多个 promise 任务，只有全部的 promise 都成功了返回的 promise 才会成功，否则失败
<ul>
<li>成功时，将各 promise 传递的数据按照任务声明顺序存在一个数组中，传递给下一个 promise</li>
<li>失败时，将首个失败的 promise 错误信息传递给下一个 promise</li>
</ul>
</li>
<li>参数：
<ul>
<li><code>promiseTasks: Array<Promise></code>：promise 任务集</li>
</ul>
</li>
<li>返回值：<code>Promise</code>：返回一个新的 promise，传递包含所有成功任务数据数组，或首个失败任务信息</li>
</ul>
<blockquote>
<p>每个 promise 在并行处理的过程中是独立的，因此不会因为某个 promise 失败了而影响到其他的 promise，它只影响并行函数的结果</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// > 顺序打印 1 5 10，说明是并行处理任务</span>
<span class="hljs-keyword">const</span> delay = <span class="hljs-function">(<span class="hljs-params">time, callback</span>) =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    callback()
    resolve(time)
  &#125;, time)
&#125;)

<span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Promise</span>.all([
  delay(<span class="hljs-number">10</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>)&#125;),
  delay(<span class="hljs-number">1</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)&#125;),
  delay(<span class="hljs-number">5</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>)&#125;),
])

result.then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)       <span class="hljs-comment">// [ 10, 1, 5 ]</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>Promise.all </code> 在任务成功时会阻塞所有任务，直到所有任务都成功了才会继续往下链式调用，但是如果有任意任务失败了，立即会跳出该方法往下链式调用（不会影响 <code>Promise.all</code> 内部 promise 任务集的继续执行）</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// > 顺序打印 出大事啦!!! 1 5 10，说明 Promise.all 失败时立即退出链式调用下一个任务</span>
<span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Promise</span>.all([
  delay(<span class="hljs-number">10</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>)&#125;),
  delay(<span class="hljs-number">1</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)&#125;),
  <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'出大事啦!!!'</span>),
  delay(<span class="hljs-number">5</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>)&#125;),
  <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'又出大事啦!!!'</span>),
])

result.then(
  <span class="hljs-function">() =></span> &#123;&#125;,
  <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;<span class="hljs-built_in">console</span>.log(err)&#125;       <span class="hljs-comment">// 出大事啦!!!</span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>Promise.race (promiseTasks)</strong></p>
<ul>
<li>功能：并行处理多个 promise 任务，只要其中一个 promise 非 pengding 状态则立即跳出该方法往下链式调用（其他仍在执行的任务不会被中断，继续执行）</li>
<li>参数：
<ul>
<li><code>promiseTasks: Array<Promise></code>：promise 任务集</li>
</ul>
</li>
<li>返回值：<code>Promise</code>：返回一个新的 promise，传递首个成功或失败任务的数据</li>
</ul>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// > 顺序打印 1 5 10</span>
<span class="hljs-keyword">const</span> delay = <span class="hljs-function">(<span class="hljs-params">time, callback</span>) =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    callback()
    resolve(time)
  &#125;, time)
&#125;)

<span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Promise</span>.race([
  delay(<span class="hljs-number">10</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>)&#125;),
  delay(<span class="hljs-number">1</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)&#125;),
  delay(<span class="hljs-number">5</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>)&#125;),
])

result.then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)       <span class="hljs-comment">// 1</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>Promise.allSettled (promiseTasks)</strong></p>
<ul>
<li>功能：并行处理多个 promise 任务，只有全部的 promise 都为非 penging 状态时才会继续往下链式调用</li>
<li>参数：
<ul>
<li><code>promiseTasks: Array<Promise></code>：promise 任务集</li>
</ul>
</li>
<li>返回值：<code>Promise</code>：返回一个新的 promise，传递所有 promise 的任务信息</li>
</ul>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// > 顺序打印 1 5 10</span>
<span class="hljs-keyword">const</span> delay = <span class="hljs-function">(<span class="hljs-params">time, callback</span>) =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    callback()
    resolve(time)
  &#125;, time)
&#125;)

<span class="hljs-keyword">const</span> result = <span class="hljs-built_in">Promise</span>.allSettled([
  delay(<span class="hljs-number">10</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">10</span>)&#125;),
  delay(<span class="hljs-number">1</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)&#125;),
  <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'出大事啦!!!'</span>),
  delay(<span class="hljs-number">5</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>)&#125;),
  <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'又出大事啦!!!'</span>),
])

result.then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data)       
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57ece8582e8d45f9a5bdce90927ccbc3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-10">使用技巧</h3>
<h4 data-id="heading-11">延时函数</h4>
<p>使用 promise 制作一个延时函数可以放在 promise 任务链或 async 函数中来阻塞异步操作</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 顺序打印 1 2 3</span>
<span class="hljs-keyword">const</span> delay = <span class="hljs-function">(<span class="hljs-params">time, callback</span>) =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    callback()
    resolve()
  &#125;, time)
&#125;)

<span class="hljs-keyword">const</span> fn = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
  <span class="hljs-keyword">await</span> delay(<span class="hljs-number">50</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)&#125;)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>)
&#125;

fn()
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h4 data-id="heading-12">超时处理</h4>
<p>通过 <code>Promise.race</code> 的特性可以制作一个超时处理函数，往往用在网络请求超时中</p>
<blockquote>
<p>原生 promise 无法直接取消或中断进行中的任务，最多只能通过报错来阻止数据的传递</p>
</blockquote>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 顺序打印 1 2 3</span>
<span class="hljs-keyword">const</span> delay = <span class="hljs-function">(<span class="hljs-params">time, callback</span>) =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    callback()
    resolve()
  &#125;, time)
&#125;)

<span class="hljs-built_in">Promise</span>.race([
  delay(<span class="hljs-number">500</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求结束'</span>)&#125;),      <span class="hljs-comment">// 模拟请求需要500ms</span>
  delay(<span class="hljs-number">300</span>, <span class="hljs-function">() =></span> &#123;<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请求超时'</span>)&#125;)
])
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            