
---
title: 'JS异步编程(3)-Promise'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6645'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 18:35:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=6645'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">JS异步编程(3)-Promise</h1>
<p>这是我参与更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><code>Promise</code> 算是 <code>JavaScript</code> 异步编程演进过程中的里程碑级别的特性更新<br>
最早由社区提出和实现，直到 <code>ES6</code> 发布将其写进了标准，统一了用法，并原生提供了 <code>Promise</code> 对象</p>
<ul>
<li>通过 <code>then</code> 函数的链式调用方式，在形式上初步解决了<strong>回调地狱</strong>的问题</li>
<li>成为后续 <code>async/await</code>、<code>fetch</code> 等等API的基石</li>
</ul>
<h2 data-id="heading-1">Promise 特性</h2>
<ul>
<li>异步任务</li>
<li>值穿透</li>
<li><code>resolve/reject</code> 没有中断执行</li>
<li><code>catch</code> 和 <code>then rejectHandle</code> 的区别</li>
</ul>
<h3 data-id="heading-2">异步任务</h3>
<ul>
<li><code>new Promise</code> 是同步执行的</li>
<li><code>Promise</code> 的 <code>then</code> <code>catch</code> <code>finally</code> 才是异步执行的</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 下方代码输出顺序： 1 -> 3 -> 2 -> 4</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>)
    resolve(<span class="hljs-number">4</span>)
&#125;)
.then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">值穿透</h3>
<p><code>Promise</code> 的 <code>then</code> <code>catch</code> 的<strong>参数期望是函数</strong>，传入非函数则会发生<strong>值穿透</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">1</span>)
  .then(<span class="hljs-number">2</span>)
  .then(<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">3</span>))
  .then(<span class="hljs-built_in">console</span>.log) <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">resolve/reject 没有中断执行</h3>
<p><code>resolve/reject</code> 只是改变了 <code>Promise</code> 对象的状态，并没有中断当前的执行<br>
我们有时候会下意识的认为：<code>resolve/reject</code> 直接让程序进入了下一个阶段，其实并不是</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 下方代码输出顺序： 1 -> 3 -> 2</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
    resolve(<span class="hljs-number">2</span>)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>)
&#125;)
.then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">catch 和 then rejectHandle 的区别</h3>
<ul>
<li><code>catch</code> 可以捕获 <code>Promise resolve</code> 之前的 <code>throw Error</code> 错误</li>
<li><code>then rejectHandler</code> 不能捕获同级 <code>then resolveHandler</code> 中的错误</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    resolve(<span class="hljs-number">1</span>)
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'err'</span>) <span class="hljs-comment">// 不会进入 Promise catch</span>
&#125;)

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    resolve()
&#125;)
.then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'err'</span>)
&#125;, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 无法捕获同级 then rejectHandler 中的错误 err</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Promise 静态方法特性</h2>
<h3 data-id="heading-7">Promise.all</h3>
<p><code>Promise.all</code> 参数接收一个可迭代对象（一般是数组）并返回一个新的 <code>Promise</code> 对象
具体参考 MDN： <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/all" target="_blank" rel="nofollow noopener noreferrer">Promise.all()</a></p>
<ul>
<li>如果参数是空数组，进入 <code>then</code></li>
<li>如果参数数组不包含 <code>Promise</code> 对象，进入 then，例如 <code>Promise.all([1,2,3])</code></li>
<li>如果一个元素 <code>Promise reject</code>，会立刻进入 <code>Promise.all</code> 的 <code>catch</code>，但不会影响其他元素 Promise 的继续执行</li>
<li>如果想知道是哪一个失败了，可以在元素 <code>Promise</code> 的 <code>reject</code> 中标识</li>
</ul>
<p>如果数组元素 <code>Promise</code> 自己处理内部错误并重新返回一个 <code>resolve</code> 的 <code>Promise</code>，就不会因此导致进入 <code>Promise.all</code> 的 <code>catch</code></p>
<h3 data-id="heading-8">Promise.race</h3>
<p><code>Promise.race</code> 参数和 <code>Promise.all</code> 一样<br>
具体参考 MDN： <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/race" target="_blank" rel="nofollow noopener noreferrer">Promise.race()</a></p>
<ul>
<li>如果参数是空数组，<code>then</code> <code>catch</code> 都不执行</li>
<li>如果数组非空，根据第一个返回的元素 <code>Promise</code> 的 <code>resolve</code> <code>reject</code>，立刻对应进入 <code>Promise.race</code> 的 <code>then</code> <code>catch</code></li>
<li>无论第一个元素 <code>Promise</code> 的结果如何，不会影响其他元素 <code>Promise</code> 继续执行</li>
</ul>
<h3 data-id="heading-9">Promise.allSettled</h3>
<p><code>Promise.allSettled</code> 由 <code>ES11</code> 引入标准<br>
<code>Promise.allSettled</code> 会等待全部元素 <code>Promise</code> 完成后（无论 <code>resolve</code> 还是 <code>reject</code>），进入 <code>then</code></p>
<p>那什么情况下能进入 <code>Promise.allSettled</code> 的 <code>catch</code> 呢？<br>
在某个 <code>Promise</code> <code>throw Error</code> 的时候！</p>
<p>并且 <code>Promise.allSettled</code> 的 <code>catch</code> 会捕获每一个 <code>Promise</code> 中的错误，因此有可能执行多次<br>
（<code>Promise.all</code> 只会捕捉第一个 <code>reject</code> 的错误）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(<span class="hljs-number">1</span>)
  &#125;, <span class="hljs-number">100</span>)
&#125;);

<span class="hljs-keyword">const</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(<span class="hljs-number">2</span>)
  &#125;, <span class="hljs-number">200</span>)
&#125;);

<span class="hljs-built_in">Promise</span>.allSettled([promise1, promise2])
  .then(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'then'</span>, value)
  &#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-comment">// 100ms 后捕获 promise1 的错误，200ms 后捕获 promise2 的错误</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'catch'</span>, err)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Promise.any</h3>
<p><code>Promise.any</code> 由 <code>ES12</code> 引入标准</p>
<ul>
<li>如果元素 <code>Promise</code> 有一个 <code>resolve</code>，就进入 <code>Promise.any</code> 的 <code>then</code></li>
<li>如果元素 <code>Promise</code> 全部都 <code>reject</code>，就进入 <code>Promise.any</code> 的 <code>catch</code></li>
</ul>
<h2 data-id="heading-11">Promise/A+ 规范</h2>
<p>如上文所述，<code>Promise</code> 是 <code>ES6</code> 提供的标准原生对象<br>
当我们的代码需要编译成 <code>ES5</code> 或者以下版本的时候，需要引入 polyfill<br>
polyfill 中的 Promise 就是根据 Promise/A+ 规范编写的</p>
<p>详情参考：<a href="https://promisesaplus.com/#notes" target="_blank" rel="nofollow noopener noreferrer">Promise/A+ 规范</a></p>
<ul>
<li>一个 <code>Promise</code> 的当前状态必须为以下三种状态中的一种：等待态（<code>Pending</code>）、执行态（<code>Fulfilled</code>）和拒绝态（<code>Rejected</code>）
<ul>
<li>处于等待态时，<code>promise</code> 可以迁移至执行态或拒绝态</li>
<li>处于执行态时，<code>promise</code> 不能迁移至其他任何状态，必须拥有一个不可变的终值</li>
<li>处于拒绝态时，<code>promise</code> 不能迁移至其他任何状态，必须拥有一个不可变的据因</li>
</ul>
</li>
<li>必须实现 then 方法
<ul>
<li><code>then</code> 函数接受两个参数</li>
<li><code>then</code> 函数参数如果不是函数，则忽略该参数</li>
<li><code>then</code> 函数可以被一个 <code>promise</code> 多次调用</li>
<li>必须返回一个 <code>promise</code> 实例</li>
</ul>
</li>
</ul>
<h2 data-id="heading-12">写在最后</h2>
<p>总有人和我说 <code>Promise.all</code> 和 <code>Promise.race</code> 其中一个 <code>Promise</code> <code>reject</code> 会<strong>中断</strong>其他 <code>Promise</code> 的进行<br>
我查阅文档 + 写 <code>demo</code> 测试，都证明既<strong>不中断</strong>，也<strong>不等待</strong><br>
如有同样认为会<strong>中断</strong>的兄弟，希望在<strong>评论区</strong>给个 <code>demo</code></p></div>  
</div>
            