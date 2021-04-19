
---
title: 'PromiseA+ 规范'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3047'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 18:07:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=3047'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">术语</h2>
<ol>
<li>promise 是一个有then方法的对象或者是函数，行为遵循本规范。</li>
<li>thenable 是一个有then方法的对象或者是函数。</li>
<li>value 是 promise 状态成功时的值，也就是 resolve 的参数, 包括各种数据类型, 也包括 undefined/thenable 或者是 promise。</li>
<li>reason 是 promise 状态失败时的值, 也就是 reject 的参数, 表示拒绝的原因</li>
<li>exception 是一个使用 throw 抛出的异常值。</li>
</ol>
<h2 data-id="heading-1">定义</h2>
<p>Promise 表示一个异步操作的最终结果，与之进行交互的方式主要是 then 方法，该方法注册了两个回调函数，用于接收 promise 的终值或本 promise 不能执行的原因。</p>
<p>简单来说：Promise 是一个拥有 then 方法的对象或者函数。</p>
<h2 data-id="heading-2">状态</h2>
<ol>
<li>等待态（Pending）：初始状态，可改变。</li>
<li>执行态（Fulfilled）：最终态，不可变，必须拥有一个 value 值。</li>
<li>拒绝态（Rejected）：最终态，不可变，必须拥有一个 reason 值。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 状态流转：</span>
pending --> resolve(value) --> fulfilled;
pending --> reject(reason) --> rejected;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">then</h2>
<h3 data-id="heading-4">promise 必须提供一个 then 方法以访问其当前值、种植和据因</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 参数要求：必须是函数类型，如果不是，则被忽略。</span>
<span class="hljs-comment">// 这两个参数应该是 微任务。这里用queueMicrotask来实现微任务的调用</span>
<span class="hljs-built_in">Promise</span>.then(onFulfilled,onRejected);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>onFulfilled 特性：</li>
</ul>
<ol>
<li>只能被调用一次；</li>
<li>在 promise 变成 fulfilled 前不可被调用；</li>
<li>当 promise 执行结束后必须被调用，第一个参数是 promise 的终值。</li>
</ol>
<ul>
<li>onRejected 特性：</li>
</ul>
<ol>
<li>只能被调用一次；</li>
<li>在 promise 变成 rejected 之前不用管被调用；</li>
<li>当 promise 执行结束后必须被调用，第一个参数是 promise 的终值。</li>
</ol>
<h3 data-id="heading-5">then 方法可以被调用多次</h3>
<ol>
<li>promise状态变成 fulfilled 后，所有的 onFulfilled 回调都需要按照then的顺序执行, 也就是按照注册顺序执行(所以在实现的时候需要一个数组来存放多个onFulfilled的回调)</li>
<li>promise状态变成 rejected 后，所有的 onRejected 回调都需要按照then的顺序执行, 也就是按照注册顺序执行(所以在实现的时候需要一个数组来存放多个onRejected的回调)</li>
</ol>
<h3 data-id="heading-6">then 应该返回一个 promise</h3>
<pre><code class="hljs language-js copyable" lang="js">promise2 = promise1.then(onFulfilled,onRejected);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>onFulfilled 或 onRejected 执行的结果为x, 调用 resolvePromise；</li>
<li>如果 onFulfilled 或者 onRejected 执行时抛出异常e, promise2需要被reject；</li>
<li>如果 onFulfilled 不是一个函数, promise2 以promise1的value 触发fulfilled；</li>
<li>如果 onRejected 不是一个函数, promise2 以promise1的reason 触发rejected；</li>
</ol>
<h4 data-id="heading-7">resolvePromise</h4>
<pre><code class="hljs language-js copyable" lang="js">resolvePromise(newPromise,x,resolve,reject)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果 promise2 和 x 相等，那么 reject TypeError;</li>
<li>如果 x 是一个 promsie:</li>
</ul>
<ol>
<li>如果 x 是pending态，那么 promise 必须要在 pending，直到 x 变成 fulfilled or rejected;</li>
<li>如果 x 被 fulfilled,<code>fulfill promise with the same value</code></li>
<li>如果 x 被 rejected,<code>reject promise with the same reason</code></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">x.then(<span class="hljs-function">(<span class="hljs-params">y</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.resolvePromise(newPromise, y, resolve, reject);
&#125;, reject);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果 x 是一个 object or function</li>
</ul>
<p><code>let then = x.then</code></p>
<ol>
<li>如果 x.then 这步出错，那么 <code>reject promise with e as the reason</code></li>
<li>如果 then 不是一个function，那么 <code>fulfill promise with x</code></li>
<li>如果 then 是一个函数，<code>，then.call(x, resolvePromiseFn, rejectPromise)</code></li>
</ol>
<p>3.1. resolvePromiseFn 的 入参是 y, 执行 <code>resolvePromise(promise2, y, resolve, reject)</code>;<br>
3.2. rejectPromise 的 入参是 r, <code>reject promise with r</code>;<br>
3.3. 如果 resolvePromise 和 rejectPromise 都调用了，那么第一个调用优先，后面的调用忽略；<br>
3.4. 如果调用then抛出异常e ，如果 resolvePromise 或 rejectPromise 已经被调用，那么忽略则，<code>reject promise with e as the reason</code>。</p>
<blockquote>
<p>参考链接：
<a href="http://malcolmyu.github.io/malnote/2015/06/12/Promises-A-Plus/" target="_blank" rel="nofollow noopener noreferrer">PromiseA+规范</a></p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            