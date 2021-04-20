
---
title: '一步步实现一个Promise'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7538'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 11:39:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=7538'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1、前言</h2>
<p>本篇文章，默认你已经知道什么是 <strong>Promise</strong> ，然后我会带你一步步的实现一个简易的 Promise。将会以循序渐进的方式，分步骤实现。</p>
<p>本文章相关代码地址：<a href="https://github.com/layouwen/blog_demo_lpromise" target="_blank" rel="nofollow noopener noreferrer">github.com/layouwen/bl…</a></p>
<p>如果本文章对你有所帮助，请不要吝啬你的 <strong>Start</strong> 哦~</p>
<h2 data-id="heading-1">2、三种状态</h2>
<p><a href="https://github.com/Layouwen/blog_demo_lpromise/blob/master/%E4%B8%89%E7%A7%8D%E7%8A%B6%E6%80%81.html" target="_blank" rel="nofollow noopener noreferrer">此处代码，点击这里</a></p>
<p>Promise 它一共会有三种状态：</p>
<ol>
<li>pending</li>
<li>fulfilled</li>
<li>rejected</li>
</ol>
<p>下面我们自己实现一个类，默认为 <strong>pending</strong> 状态，通过调用 <strong>resolve</strong> 或者 <strong>reject</strong> 改变其状态</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'pending'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = <span class="hljs-literal">undefined</span>
    callbackFn(<span class="hljs-built_in">this</span>.#resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.#reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  #<span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = res
  &#125;
  #<span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'reject'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = err
  &#125;
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'pending'</span>))) <span class="hljs-comment">// pending 状态</span>
<span class="hljs-keyword">const</span> l1 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  resolve(<span class="hljs-string">'我调用了resolve'</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(l1) <span class="hljs-comment">// fulfilled 状态</span>
<span class="hljs-keyword">const</span> l2 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  reject(<span class="hljs-string">'我调用了reject'</span>)
&#125;)
<span class="hljs-built_in">console</span>.log(l2) <span class="hljs-comment">// rejected 状态</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3、实现 then 参数回调</h2>
<p><a href="https://github.com/Layouwen/blog_demo_lpromise/blob/master/%E5%AE%9E%E7%8E%B0then%E5%8F%82%E6%95%B0%E5%9B%9E%E8%B0%83.html" target="_blank" rel="nofollow noopener noreferrer">此处代码，点击这里</a></p>
<p>返回的 <strong>Promise</strong> ，可以通过使用 <strong>then</strong> 传递成功和失败的回调。</p>
<p>通过 then 接收了两个回调。实现了分别调用回调的内容。但是发现，他们两个都会执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'pending'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = <span class="hljs-literal">undefined</span>
    callbackFn(<span class="hljs-built_in">this</span>.#resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.#reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  #<span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = res
  &#125;
  #<span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'reject'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = err
  &#125;
  <span class="hljs-comment">/* new content start */</span>
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onResolve, onReject</span>)</span> &#123;
    onResolve()
    onReject()
  &#125;
  <span class="hljs-comment">/* new content end */</span>
&#125;
<span class="hljs-keyword">const</span> l1 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> resolve())
l1.then(
  <span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'res'</span>),
  <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'err'</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对执行时机进行调整。使其在调用 resolve 或 reject 才执行相关的回调</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'pending'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = <span class="hljs-literal">undefined</span>
    callbackFn(<span class="hljs-built_in">this</span>.#resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.#reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  #<span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = res
    <span class="hljs-comment">/* new content start */</span>
    <span class="hljs-built_in">this</span>.cbResolve() <span class="hljs-comment">// 报错</span>
    <span class="hljs-comment">/* new content end */</span>
  &#125;
  #<span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'reject'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = err
    <span class="hljs-comment">/* new content start */</span>
    <span class="hljs-built_in">this</span>.cbReject() <span class="hljs-comment">// 报错</span>
    <span class="hljs-comment">/* new content end */</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onResolve, onReject</span>)</span> &#123;
    <span class="hljs-comment">/* new content start */</span>
    <span class="hljs-built_in">this</span>.cbResolve = onResolve
    <span class="hljs-built_in">this</span>.cbReject = onReject
    <span class="hljs-comment">/* new content end */</span>
  &#125;
&#125;
<span class="hljs-keyword">const</span> l1 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> resolve())
l1.then(
  <span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'res'</span>),
  <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'err'</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改装后，发现 resolve 和 reject 的执行时间比 then 的回调要快。导致无法执行 then 中的回调。我们需要对 resolve 和 reject 中执行回调的部分进行 <strong>延迟执行</strong>。可以使用 setTimeout 进行延迟</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'pending'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = <span class="hljs-literal">undefined</span>
    callbackFn(<span class="hljs-built_in">this</span>.#resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.#reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  #<span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = res
    <span class="hljs-comment">/* new content start */</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.cbResolve())
    <span class="hljs-comment">/* new content end */</span>
  &#125;
  #<span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'reject'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = err
    <span class="hljs-comment">/* new content start */</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.cbReject())
    <span class="hljs-comment">/* new content end */</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onResolve, onReject</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.cbResolve = onResolve
    <span class="hljs-built_in">this</span>.cbReject = onReject
  &#125;
&#125;
<span class="hljs-keyword">const</span> l1 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> resolve())
l1.then(
  <span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'res'</span>),
  <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'err'</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>考虑到 微任务 和 宏任务。我们可以使用 MutationObserver 替代 setTimeout</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'pending'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = <span class="hljs-literal">undefined</span>
    callbackFn(<span class="hljs-built_in">this</span>.#resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.#reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  #<span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = res
    <span class="hljs-comment">/* new content start */</span>
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.cbResolve()
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
    <span class="hljs-comment">/* new content end */</span>
  &#125;
  #<span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'reject'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = err
    <span class="hljs-comment">/* new content start */</span>
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.cbReject()
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
    <span class="hljs-comment">/* new content end */</span>
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onResolve, onReject</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.cbResolve = onResolve
    <span class="hljs-built_in">this</span>.cbReject = onReject
  &#125;
&#125;
<span class="hljs-keyword">const</span> l1 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> resolve())
l1.then(
  <span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'res'</span>),
  <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'err'</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4、链式调用</h2>
<p><a href="https://github.com/Layouwen/blog_demo_lpromise/blob/master/%E9%93%BE%E5%BC%8F%E8%B0%83%E7%94%A8.html" target="_blank" rel="nofollow noopener noreferrer">此处代码，点击这里</a></p>
<p>在原本的 <strong>Promise</strong> 中。我们是可以使用 <strong>then</strong> 链式调用。意味着每个 <strong>then</strong> 都返回一个新的 <strong>Promise</strong>。</p>
<p>因为支持链式。所以我们之前的 <code>cbResolve</code> 和 <code>cbReject</code> 就不能单单保存一个回调。要改回一个数组，将每一个 <strong>then</strong> 中的回调。都保存到回调队列中。等待调用 <strong>resolve</strong> 或者 <strong>reject</strong> 后才执行所有回调函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'pending'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = <span class="hljs-literal">undefined</span>
    <span class="hljs-comment">/* new content start */</span>
    <span class="hljs-built_in">this</span>.cbResolveQueue = []
    <span class="hljs-built_in">this</span>.cbRejectQueue = []
    <span class="hljs-comment">/* new content end */</span>
    callbackFn(<span class="hljs-built_in">this</span>.#resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.#reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  #<span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = res
    <span class="hljs-comment">/* new content start */</span>
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbResolveQueue.shift())) &#123;
        cbFn && cbFn()
      &#125;
    &#125;
    <span class="hljs-comment">/* new content end */</span>
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  #<span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'reject'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = err
    <span class="hljs-comment">/* new content start */</span>
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbRejectQueue.shift())) &#123;
        cbFn && cbFn()
      &#125;
    &#125;
    <span class="hljs-comment">/* new content end */</span>
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onResolve, onReject</span>)</span> &#123;
    <span class="hljs-comment">/* new content start */</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> cbResolve = <span class="hljs-function">() =></span> &#123;
        onResolve && onResolve()
        resolve()
      &#125;
      <span class="hljs-built_in">this</span>.cbResolveQueue.push(cbResolve)
      <span class="hljs-keyword">const</span> cbReject = <span class="hljs-function">() =></span> &#123;
        onReject && onReject()
        reject()
      &#125;
      <span class="hljs-built_in">this</span>.cbRejectQueue.push(cbReject)
    &#125;)
    <span class="hljs-comment">/* new content end */</span>
  &#125;
&#125;
<span class="hljs-keyword">const</span> l1 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> resolve())
l1.then(
  <span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'res'</span>),
  <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'err'</span>)
).then(
  <span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'res'</span>),
  <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'err'</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们已经完成了链式调用，但是我们会发现，此时如果返回一个新的 <strong>Promise</strong> ，却无法获取 <strong>Promise</strong> 的结果。所以我们得加一些判断条件。我们也会发现，此时此刻我们无法接收到 <strong>res</strong> 或 <strong>err</strong> 的参数。所以我们也要完善一下参数传递问题。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'pending'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.cbResolveQueue = []
    <span class="hljs-built_in">this</span>.cbRejectQueue = []
    callbackFn(<span class="hljs-built_in">this</span>.#resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.#reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  #<span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = res
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbResolveQueue.shift())) &#123;
        <span class="hljs-comment">/* new content start */</span>
        cbFn && cbFn(res)
        <span class="hljs-comment">/* new content end */</span>
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  #<span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'reject'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = err
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbRejectQueue.shift())) &#123;
        <span class="hljs-comment">/* new content start */</span>
        cbFn && cbFn(err)
        <span class="hljs-comment">/* new content end */</span>
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onResolve, onReject</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-comment">/* new content start */</span>
      <span class="hljs-keyword">const</span> cbResolve = <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-keyword">const</span> resolveRes = onResolve && onResolve(res)
        <span class="hljs-keyword">if</span> (resolveRes <span class="hljs-keyword">instanceof</span> LPromise) &#123;
          resolveRes.then(resolve)
        &#125; <span class="hljs-keyword">else</span> &#123;
          resolve(res)
        &#125;
      &#125;
      <span class="hljs-comment">/* new content end */</span>
      <span class="hljs-built_in">this</span>.cbResolveQueue.push(cbResolve)
      <span class="hljs-comment">/* new content start */</span>
      <span class="hljs-keyword">const</span> cbReject = <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        onReject && onReject(err)
        reject(err)
      &#125;
      <span class="hljs-comment">/* new content end */</span>
      <span class="hljs-built_in">this</span>.cbRejectQueue.push(cbReject)
    &#125;)
  &#125;
&#125;
<span class="hljs-keyword">const</span> l1 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> resolve(<span class="hljs-string">'我是传入的 resolve 数据'</span>))
l1.then(
  <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第一个then的res'</span>, res)
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> resolve(<span class="hljs-string">'返回的Promise'</span>))
  &#125;,
  <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第一个then的err'</span>, err)
)
  .then(
    <span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第二个then的res'</span>, res),
    <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第二个then的err'</span>, err)
  )
  .then(
    <span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第三个then的res'</span>, res),
    <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第三个then的err'</span>, err)
  )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到现在我们已经实现了 <strong>then</strong> 的链式调用</p>
<h2 data-id="heading-4">5、实现 catch 方法</h2>
<p><a href="https://github.com/Layouwen/blog_demo_lpromise/blob/master/%E5%AE%9E%E7%8E%B0catch%E6%96%B9%E6%B3%95.html" target="_blank" rel="nofollow noopener noreferrer">此处代码，点击这里</a></p>
<p>在调用 <code>catch</code> 的时候自动在回调队列中添加一个错误回调函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'pending'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.cbResolveQueue = []
    <span class="hljs-built_in">this</span>.cbRejectQueue = []
    callbackFn(<span class="hljs-built_in">this</span>.#resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.#reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  #<span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = res
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbResolveQueue.shift())) &#123;
        cbFn && cbFn(res)
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  #<span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'reject'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = err
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbRejectQueue.shift())) &#123;
        cbFn && cbFn(err)
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onResolve, onReject</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> cbResolve = <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-keyword">const</span> resolveRes = onResolve && onResolve(res)
        <span class="hljs-keyword">if</span> (resolveRes <span class="hljs-keyword">instanceof</span> LPromise) &#123;
          resolveRes.then(resolve)
        &#125; <span class="hljs-keyword">else</span> &#123;
          resolve(res)
        &#125;
      &#125;
      <span class="hljs-built_in">this</span>.cbResolveQueue.push(cbResolve)
      <span class="hljs-keyword">const</span> cbReject = <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        onReject && onReject(err)
        reject(err)
      &#125;
      <span class="hljs-built_in">this</span>.cbRejectQueue.push(cbReject)
    &#125;)
  &#125;
  <span class="hljs-comment">/* new content start */</span>
  <span class="hljs-keyword">catch</span>(err) &#123;
    <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">undefined</span>, err)
  &#125;
  <span class="hljs-comment">/* new content end */</span>
&#125;
<span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> reject(<span class="hljs-string">'我是p1的错误信息'</span>))
p1.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res)).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">6、resolve 和 reject 静态方法</h2>
<p><a href="https://github.com/Layouwen/blog_demo_lpromise/blob/master/Resolve%E5%92%8CReject%E9%9D%99%E6%80%81%E6%96%B9%E6%B3%95.html" target="_blank" rel="nofollow noopener noreferrer">此处代码，点击这里</a></p>
<p>这两个静态方法比较简单。只需要返回一个固定状态的 <strong>Promise</strong> 即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'pending'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.cbResolveQueue = []
    <span class="hljs-built_in">this</span>.cbRejectQueue = []
    callbackFn(<span class="hljs-built_in">this</span>.#resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.#reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  #<span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = res
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbResolveQueue.shift())) &#123;
        cbFn && cbFn(res)
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  #<span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'reject'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = err
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbRejectQueue.shift())) &#123;
        cbFn && cbFn(err)
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onResolve, onReject</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> cbResolve = <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-keyword">const</span> resolveRes = onResolve && onResolve(res)
        <span class="hljs-keyword">if</span> (resolveRes <span class="hljs-keyword">instanceof</span> LPromise) &#123;
          resolveRes.then(resolve)
        &#125; <span class="hljs-keyword">else</span> &#123;
          resolve(res)
        &#125;
      &#125;
      <span class="hljs-built_in">this</span>.cbResolveQueue.push(cbResolve)
      <span class="hljs-keyword">const</span> cbReject = <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        onReject && onReject(err)
        reject(err)
      &#125;
      <span class="hljs-built_in">this</span>.cbRejectQueue.push(cbReject)
    &#125;)
  &#125;
  <span class="hljs-comment">/* new content start */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> resolve(res))
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params"><span class="hljs-literal">undefined</span>, reject</span>) =></span> reject(err))
  &#125;
  <span class="hljs-comment">/* new content end */</span>
&#125;
<span class="hljs-keyword">const</span> p1 = LPromise.resolve(<span class="hljs-string">'成功'</span>)
<span class="hljs-built_in">console</span>.log(p1)
<span class="hljs-keyword">const</span> p2 = LPromise.reject(<span class="hljs-string">'失败'</span>)
<span class="hljs-built_in">console</span>.log(p2)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">7、实现 finally 方法</h2>
<p><a href="https://github.com/Layouwen/blog_demo_lpromise/blob/master/%E5%AE%9E%E7%8E%B0finally%E6%96%B9%E6%B3%95.html" target="_blank" rel="nofollow noopener noreferrer">此处代码，点击这里</a></p>
<p>这个与 catch 类似的实现，只需要保证不管成功还是失败都执行里面的回调。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'pending'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.cbResolveQueue = []
    <span class="hljs-built_in">this</span>.cbRejectQueue = []
    callbackFn(<span class="hljs-built_in">this</span>.#resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.#reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  #<span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = res
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbResolveQueue.shift())) &#123;
        cbFn && cbFn(res)
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  #<span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'reject'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = err
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbRejectQueue.shift())) &#123;
        cbFn && cbFn(err)
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onResolve, onReject</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> cbResolve = <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-keyword">const</span> resolveRes = onResolve && onResolve(res)
        <span class="hljs-keyword">if</span> (resolveRes <span class="hljs-keyword">instanceof</span> LPromise) &#123;
          resolveRes.then(resolve)
        &#125; <span class="hljs-keyword">else</span> &#123;
          resolve(res)
        &#125;
      &#125;
      <span class="hljs-built_in">this</span>.cbResolveQueue.push(cbResolve)
      <span class="hljs-keyword">const</span> cbReject = <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        onReject && onReject(err)
        reject(err)
      &#125;
      <span class="hljs-built_in">this</span>.cbRejectQueue.push(cbReject)
    &#125;)
  &#125;
  <span class="hljs-keyword">catch</span>(err) &#123;
    <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">undefined</span>, err)
  &#125;
  <span class="hljs-comment">/* new content start */</span>
  <span class="hljs-function"><span class="hljs-title">finally</span>(<span class="hljs-params">callback</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.then(callback, callback)
  &#125;
  <span class="hljs-comment">/* new content end */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> resolve(res))
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params"><span class="hljs-literal">undefined</span>, reject</span>) =></span> reject(err))
  &#125;
&#125;
<span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> reject(<span class="hljs-string">'我是p1的错误信息'</span>))
p1.then(
  <span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(res),
  <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err)
).finally(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'finally'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">8、实现 race 方法</h2>
<p><a href="https://github.com/Layouwen/blog_demo_lpromise/blob/master/%E5%AE%9E%E7%8E%B0race%E6%96%B9%E6%B3%95.html" target="_blank" rel="nofollow noopener noreferrer">此处代码，点击这里</a></p>
<p><strong>race</strong> 就是返回最先执行成功的结果。不管是成功还是失败。这样我们只需要遍历该 <strong>Promise</strong> ，正常返回数据。谁先执行完成，谁先返回即可。注意要控制状态，防止返回多个结果。 <strong>race</strong> 只需要返回最快的一个结果。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'pending'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.cbResolveQueue = []
    <span class="hljs-built_in">this</span>.cbRejectQueue = []
    callbackFn(<span class="hljs-built_in">this</span>.#resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.#reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  #<span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = res
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbResolveQueue.shift())) &#123;
        cbFn && cbFn(res)
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  #<span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'reject'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = err
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbRejectQueue.shift())) &#123;
        cbFn && cbFn(err)
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onResolve, onReject</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> cbResolve = <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-keyword">const</span> resolveRes = onResolve && onResolve(res)
        <span class="hljs-keyword">if</span> (resolveRes <span class="hljs-keyword">instanceof</span> LPromise) &#123;
          resolveRes.then(resolve)
        &#125; <span class="hljs-keyword">else</span> &#123;
          resolve(res)
        &#125;
      &#125;
      <span class="hljs-built_in">this</span>.cbResolveQueue.push(cbResolve)
      <span class="hljs-keyword">const</span> cbReject = <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        onReject && onReject(err)
        reject(err)
      &#125;
      <span class="hljs-built_in">this</span>.cbRejectQueue.push(cbReject)
    &#125;)
  &#125;
  <span class="hljs-keyword">catch</span>(err) &#123;
    <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">undefined</span>, err)
  &#125;
  <span class="hljs-function"><span class="hljs-title">finally</span>(<span class="hljs-params">callback</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.then(callback, callback)
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> resolve(res))
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params"><span class="hljs-literal">undefined</span>, reject</span>) =></span> reject(err))
  &#125;
  <span class="hljs-comment">/* new content start */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promiseArr</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> isContinue = <span class="hljs-literal">true</span>
      promiseArr.forEach(<span class="hljs-function"><span class="hljs-params">promise</span> =></span> &#123;
        promise.then(
          <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (isContinue) &#123;
              isContinue = <span class="hljs-literal">false</span>
              resolve(res)
            &#125;
          &#125;,
          <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (isContinue) &#123;
              isContinue = <span class="hljs-literal">false</span>
              reject(err)
            &#125;
          &#125;
        )
      &#125;)
    &#125;)
  &#125;
  <span class="hljs-comment">/* new content end */</span>
&#125;
<span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> resolve(<span class="hljs-number">1</span>), <span class="hljs-number">200</span>))
<span class="hljs-keyword">const</span> p2 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> reject(<span class="hljs-number">2</span>), <span class="hljs-number">1000</span>))
<span class="hljs-keyword">const</span> p3 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> resolve(<span class="hljs-number">3</span>), <span class="hljs-number">3000</span>))
LPromise.race([p1, p2, p3]).then(
  <span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'res'</span>, res),
  <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'err'</span>, err)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">9、实现 all 方法</h2>
<p><a href="https://github.com/Layouwen/blog_demo_lpromise/blob/master/%E5%AE%9E%E7%8E%B0all%E6%96%B9%E6%B3%95.html" target="_blank" rel="nofollow noopener noreferrer">此处代码，点击这里</a></p>
<p><strong>all</strong> 方法当所有 <strong>Promise</strong> 都成功时返回所有结果的数组，否则返回第一个失败的结果。我们只需要遍历该 <strong>Promise</strong> 数组。定义个变量存放当前 <strong>res</strong> 的长度。如果长度等于数组的长度，我们就 <strong>resolve</strong> 出去。否则发现第一个失败的时候，直接 <strong>reject</strong>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'pending'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.cbResolveQueue = []
    <span class="hljs-built_in">this</span>.cbRejectQueue = []
    callbackFn(<span class="hljs-built_in">this</span>.#resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.#reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  #<span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = res
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbResolveQueue.shift())) &#123;
        cbFn && cbFn(res)
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  #<span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'reject'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = err
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbRejectQueue.shift())) &#123;
        cbFn && cbFn(err)
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onResolve, onReject</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> cbResolve = <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-keyword">const</span> resolveRes = onResolve && onResolve(res)
        <span class="hljs-keyword">if</span> (resolveRes <span class="hljs-keyword">instanceof</span> LPromise) &#123;
          resolveRes.then(resolve)
        &#125; <span class="hljs-keyword">else</span> &#123;
          resolve(res)
        &#125;
      &#125;
      <span class="hljs-built_in">this</span>.cbResolveQueue.push(cbResolve)
      <span class="hljs-keyword">const</span> cbReject = <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        onReject && onReject(err)
        reject(err)
      &#125;
      <span class="hljs-built_in">this</span>.cbRejectQueue.push(cbReject)
    &#125;)
  &#125;
  <span class="hljs-keyword">catch</span>(err) &#123;
    <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">undefined</span>, err)
  &#125;
  <span class="hljs-function"><span class="hljs-title">finally</span>(<span class="hljs-params">callback</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.then(callback, callback)
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> resolve(res))
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params"><span class="hljs-literal">undefined</span>, reject</span>) =></span> reject(err))
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promiseArr</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> isContinue = <span class="hljs-literal">true</span>
      promiseArr.forEach(<span class="hljs-function"><span class="hljs-params">promise</span> =></span> &#123;
        promise.then(
          <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (isContinue) &#123;
              isContinue = <span class="hljs-literal">false</span>
              resolve(res)
            &#125;
          &#125;,
          <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (isContinue) &#123;
              isContinue = <span class="hljs-literal">false</span>
              reject(err)
            &#125;
          &#125;
        )
      &#125;)
    &#125;)
  &#125;
  <span class="hljs-comment">/* new content start */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">promiseArr</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> resArr = []
      <span class="hljs-keyword">const</span> length = promiseArr.length
      promiseArr.forEach(<span class="hljs-function"><span class="hljs-params">p</span> =></span> &#123;
        p.then(
          <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            resArr.push(res)
            <span class="hljs-keyword">if</span> (resArr.length === length) &#123;
              resolve(resArr)
            &#125;
          &#125;,
          <span class="hljs-function"><span class="hljs-params">err</span> =></span> reject(err)
        )
      &#125;)
    &#125;)
  &#125;
  <span class="hljs-comment">/* new content end */</span>
&#125;
<span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> resolve(<span class="hljs-number">1</span>), <span class="hljs-number">200</span>))
<span class="hljs-keyword">const</span> p2 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> reject(<span class="hljs-number">2</span>), <span class="hljs-number">1000</span>))
<span class="hljs-keyword">const</span> p3 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> reject(<span class="hljs-number">3</span>), <span class="hljs-number">3000</span>))
LPromise.all([p1, p2, p3]).then(
  <span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'res'</span>, res),
  <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'err'</span>, err)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">10、实现 allSettled 方法</h2>
<p><a href="https://github.com/Layouwen/blog_demo_lpromise/blob/master/%E5%AE%9E%E7%8E%B0allSettled%E6%96%B9%E6%B3%95.html" target="_blank" rel="nofollow noopener noreferrer">此处代码，点击这里</a></p>
<p>该方法与 <strong>all</strong> 类似。只是这个方法不管成功或失败，只要该 <strong>Promise</strong> 数组执行完毕。就会返回所有结果。我们只需要判断执行过的 <strong>Promise</strong> 长度是否等于数组长度。当一致时就直接 <strong>resolve</strong>。并且每次执行的时候，将返回值以指定格式的对象保存到返回的 <strong>res</strong> 中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'pending'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = <span class="hljs-literal">undefined</span>
    <span class="hljs-built_in">this</span>.cbResolveQueue = []
    <span class="hljs-built_in">this</span>.cbRejectQueue = []
    callbackFn(<span class="hljs-built_in">this</span>.#resolve.bind(<span class="hljs-built_in">this</span>), <span class="hljs-built_in">this</span>.#reject.bind(<span class="hljs-built_in">this</span>))
  &#125;
  #<span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'fulfilled'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = res
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbResolveQueue.shift())) &#123;
        cbFn && cbFn(res)
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  #<span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseState]]'</span>] = <span class="hljs-string">'reject'</span>
    <span class="hljs-built_in">this</span>[<span class="hljs-string">'[[PromiseResult]]'</span>] = err
    <span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> cbFn
      <span class="hljs-keyword">while</span> ((cbFn = <span class="hljs-built_in">this</span>.cbRejectQueue.shift())) &#123;
        cbFn && cbFn(err)
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> ob = <span class="hljs-keyword">new</span> MutationObserver(run)
    ob.observe(<span class="hljs-built_in">document</span>.body, &#123; <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span> &#125;)
    <span class="hljs-built_in">document</span>.body.setAttribute(<span class="hljs-string">'lpromise'</span>, <span class="hljs-string">'layouwen'</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onResolve, onReject</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> cbResolve = <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-keyword">const</span> resolveRes = onResolve && onResolve(res)
        <span class="hljs-keyword">if</span> (resolveRes <span class="hljs-keyword">instanceof</span> LPromise) &#123;
          resolveRes.then(resolve)
        &#125; <span class="hljs-keyword">else</span> &#123;
          resolve(res)
        &#125;
      &#125;
      <span class="hljs-built_in">this</span>.cbResolveQueue.push(cbResolve)
      <span class="hljs-keyword">const</span> cbReject = <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        onReject && onReject(err)
        reject(err)
      &#125;
      <span class="hljs-built_in">this</span>.cbRejectQueue.push(cbReject)
    &#125;)
  &#125;
  <span class="hljs-keyword">catch</span>(err) &#123;
    <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">undefined</span>, err)
  &#125;
  <span class="hljs-function"><span class="hljs-title">finally</span>(<span class="hljs-params">callback</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.then(callback, callback)
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">res</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> resolve(res))
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">err</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params"><span class="hljs-literal">undefined</span>, reject</span>) =></span> reject(err))
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promiseArr</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> isContinue = <span class="hljs-literal">true</span>
      promiseArr.forEach(<span class="hljs-function"><span class="hljs-params">promise</span> =></span> &#123;
        promise.then(
          <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (isContinue) &#123;
              isContinue = <span class="hljs-literal">false</span>
              resolve(res)
            &#125;
          &#125;,
          <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (isContinue) &#123;
              isContinue = <span class="hljs-literal">false</span>
              reject(err)
            &#125;
          &#125;
        )
      &#125;)
    &#125;)
  &#125;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">promiseArr</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> resArr = []
      <span class="hljs-keyword">const</span> length = promiseArr.length
      promiseArr.forEach(<span class="hljs-function"><span class="hljs-params">p</span> =></span> &#123;
        p.then(
          <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            resArr.push(res)
            <span class="hljs-keyword">if</span> (resArr.length === length) &#123;
              resolve(resArr)
            &#125;
          &#125;,
          <span class="hljs-function"><span class="hljs-params">err</span> =></span> reject(err)
        )
      &#125;)
    &#125;)
  &#125;
  <span class="hljs-comment">/* new content start */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">allSettled</span>(<span class="hljs-params">promiseArr</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
      <span class="hljs-keyword">const</span> resArr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(promiseArr.length)
      <span class="hljs-keyword">let</span> num = <span class="hljs-number">0</span>
      promiseArr.forEach(<span class="hljs-function"><span class="hljs-params">p</span> =></span> &#123;
        <span class="hljs-keyword">let</span> obj = &#123;&#125;
        p.then(
          <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            obj.status = <span class="hljs-string">'fulfilled'</span>
            obj.value = res
            resArr[num] = obj
            num++
            <span class="hljs-keyword">if</span> (num === resArr.length) resolve(resArr)
          &#125;,
          <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            obj.status = <span class="hljs-string">'rejected'</span>
            obj.reason = err
            resArr[num] = obj
            num++
            <span class="hljs-keyword">if</span> (num === resArr.length) resolve(resArr)
          &#125;
        )
      &#125;)
    &#125;)
  &#125;
  <span class="hljs-comment">/* new content end */</span>
&#125;
<span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> resolve(<span class="hljs-number">1</span>), <span class="hljs-number">200</span>))
<span class="hljs-keyword">const</span> p2 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> reject(<span class="hljs-number">2</span>), <span class="hljs-number">1000</span>))
<span class="hljs-keyword">const</span> p3 = <span class="hljs-keyword">new</span> LPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> reject(<span class="hljs-number">3</span>), <span class="hljs-number">3000</span>))
LPromise.allSettled([p1, p2, p3]).then(
  <span class="hljs-function"><span class="hljs-params">res</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'res'</span>, res),
  <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'err'</span>, err)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">End</h2>
<p>本文章实现的 Promise 不够完善，只是大概把实现原理带大家过一遍。Promise 的源码不是由 js 写的，所以我们只能尽可能使用 js 模仿。欢淫各位大佬补充更完善的版本。</p>
<p>交流学习~</p>
<blockquote>
<p>微信：gdgzyw<br>
github: <a href="https://juejin.cn/post/www.github.com/layouwen">www.github.com/layouwen</a></p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            