
---
title: '循序渐进实现Promise'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=436'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 22:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=436'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>实现promise要在熟练使用的基础上完成，首先要明确几点</p>
<ol>
<li>promise是一个类</li>
<li>promise有三种状态：<strong>成功（fulfilled）、失败（rejected）、等待（pending）</strong>
<ol>
<li>pending -> fulfilled / rejected</li>
<li>状态一旦确定就不可以再改变</li>
</ol>
</li>
<li>resolve和reject函数是用来改变状态的
<ol>
<li>resolve: fulfilled</li>
<li>reject: rejected</li>
</ol>
</li>
<li>调用then方式传入两个参数，第一个参数为状态fulfilled时的回调函数，第二个参数为状态为rejected时的回调函数</li>
</ol>
<h3 data-id="heading-0">第一版 - 基础核心原理的实现</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'pending'</span>
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'fufilled'</span>
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'rejected'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">exector</span>)</span> &#123;
    exector(<span class="hljs-built_in">this</span>.reslove, <span class="hljs-built_in">this</span>.reject)
  &#125;
  
  status = PENDING <span class="hljs-comment">// promise状态</span>
  value = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 成功时的值 then方法需要返回</span>
  error = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 失败时的值 then方法需要返回</span>
  
  <span class="hljs-comment">// 成功时的函数</span>
  reslove = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-comment">// 修改promise状态</span>
    <span class="hljs-built_in">this</span>.status = FULFILLED
    <span class="hljs-built_in">this</span>.value = value
  &#125;
  <span class="hljs-comment">// 失败时的函数</span>
  reject = <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-comment">// 修改promise状态</span>
    <span class="hljs-built_in">this</span>.status = REJECTED
    <span class="hljs-built_in">this</span>.error = error
  &#125;
  
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">successCallback, failCallback</span>)</span> &#123;
    <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.status) &#123;
            <span class="hljs-keyword">case</span> FULFILLED:
                successCallback(<span class="hljs-built_in">this</span>.value)
                <span class="hljs-keyword">break</span>
            <span class="hljs-keyword">case</span> REJECTED:
                failCallback(<span class="hljs-built_in">this</span>.error)
                <span class="hljs-keyword">break</span>
                
        &#125;
  &#125;
&#125;
<span class="hljs-comment">// test</span>
<span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
    reslove(<span class="hljs-string">'reslove'</span>)
&#125;)
  
promise.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(value) <span class="hljs-comment">// reslove</span>
&#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(error)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的代码，我们成功实现了对promise基础原理。调用promise.then方法可以成功打印出‘reslove’。但是，在then方法的实现中我们并没有对PENDING状态做处理。也就是说，假如我们进行异步操作，当前的promise是无法处理的。比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span> &#123;
    reslove(<span class="hljs-string">'reslove'</span>)
  &#125;,<span class="hljs-number">2000</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">第二版 - 处理异步情况</h3>
<p>那么异步情况如何处理呢？以上面setTimeout为例，reslove是在2秒后执行，在调用then方法2秒内当前promise的状态仍然为PENDING。
两步解决：</p>
<ol>
<li>PENDING状态时，对成功or失败回调作暂存</li>
<li>在reslove/reject 函数中判断是否有回调函数，有则执行</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'pending'</span>
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'fufilled'</span>
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'rejected'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">exector</span>)</span> &#123;
    exector(<span class="hljs-built_in">this</span>.reslove, <span class="hljs-built_in">this</span>.reject)
  &#125;
  
  status = PENDING <span class="hljs-comment">// promise状态</span>
  value = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 成功时的值 then方法需要返回</span>
  error = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 失败时的值 then方法需要返回</span>
    successCallback = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 成功回调</span>
    failCallback = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 失败回调</span>
  <span class="hljs-comment">// 成功时的函数</span>
  reslove = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-comment">// 修改promise状态</span>
    <span class="hljs-built_in">this</span>.status = FULFILLED
    <span class="hljs-built_in">this</span>.value = value
    <span class="hljs-built_in">this</span>.successCallback && <span class="hljs-built_in">this</span>.successCallback(<span class="hljs-built_in">this</span>.value)
  &#125;
  <span class="hljs-comment">// 失败时的函数</span>
  reject = <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-comment">// 修改promise状态</span>
    <span class="hljs-built_in">this</span>.status = REJECTED
    <span class="hljs-built_in">this</span>.error = error
    <span class="hljs-built_in">this</span>.failCallback && <span class="hljs-built_in">this</span>.failCallback(<span class="hljs-built_in">this</span>.error)
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">successCallback, failCallback</span>)</span> &#123;
    <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.status) &#123;
            <span class="hljs-keyword">case</span> FULFILLED:
                successCallback(<span class="hljs-built_in">this</span>.value)
                <span class="hljs-keyword">break</span>
            <span class="hljs-keyword">case</span> REJECTED:
                failCallBack(<span class="hljs-built_in">this</span>.error)
                <span class="hljs-keyword">break</span>
      <span class="hljs-comment">// 异步情况处理</span>
      <span class="hljs-keyword">case</span> PENDING:
        <span class="hljs-built_in">this</span>.successCallback = successCallback
        <span class="hljs-built_in">this</span>.failCallback = failCallback
                <span class="hljs-keyword">break</span>
        &#125;
  &#125;
&#125;
<span class="hljs-comment">// test</span>
<span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span> &#123;
        reslove(<span class="hljs-string">'reslove'</span>)
    &#125;, <span class="hljs-number">2000</span>)    
&#125;)
  
promise.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(value) <span class="hljs-comment">// 2秒后： reslove</span>
&#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(error)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现第二版后，问题又来了。我们平时使用promise时同一个promise下的then方法是可以多次调用的。我们将测试代码改为</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// test</span>
<span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span> &#123;
    reslove(<span class="hljs-string">'reslove'</span>)
  &#125;, <span class="hljs-number">2000</span>)  
&#125;)
promise.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第一次调用then: '</span>, value)
&#125;)
promise.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第二次调用then: '</span>, value)
&#125;)
<span class="hljs-comment">// 第二次调用then reslove</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发现代码只执行了最后一次then方法，打印“第二次调用then: reslove”。这显然是与我们的预期不相符的</p>
<h3 data-id="heading-2">第三版 - 多次调用</h3>
<p>要实现多次调用，我们需要做的是： 以数组形式暂存多个callback，并且在reslove/reject的时候依次调用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'pending'</span>
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'fufilled'</span>
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'rejected'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">exector</span>)</span> &#123;
    exector(<span class="hljs-built_in">this</span>.reslove, <span class="hljs-built_in">this</span>.reject)
  &#125;
  status = PENDING <span class="hljs-comment">// promise状态</span>
  value = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 成功时的值 then方法需要返回</span>
  error = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 失败时的值 then方法需要返回</span>
  <span class="hljs-comment">// 数组暂存</span>
  successCallback = [] <span class="hljs-comment">// 成功回调</span>
  failCallback = [] <span class="hljs-comment">// 失败回调</span>
  <span class="hljs-comment">// 成功时的函数</span>
  reslove = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-comment">// 修改promise状态</span>
    <span class="hljs-built_in">this</span>.status = FULFILLED
    <span class="hljs-built_in">this</span>.value = value
    <span class="hljs-comment">// 依次调用</span>
    <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.successCallback.length) <span class="hljs-built_in">this</span>.successCallback.shift()(<span class="hljs-built_in">this</span>.value)
  &#125;
  <span class="hljs-comment">// 失败时的函数</span>
  reject = <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-comment">// 修改promise状态</span>
    <span class="hljs-built_in">this</span>.status = REJECTED
    <span class="hljs-built_in">this</span>.error = error
    <span class="hljs-comment">// 依次调用</span>
    <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.failCallback.length) <span class="hljs-built_in">this</span>.failCallback.shift()(<span class="hljs-built_in">this</span>.error)
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">successCallback, failCallback</span>)</span> &#123;
    <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.status) &#123;
      <span class="hljs-keyword">case</span> FULFILLED:
        successCallback(<span class="hljs-built_in">this</span>.value)
        <span class="hljs-keyword">break</span>
      <span class="hljs-keyword">case</span> REJECTED:
        failCallBack(<span class="hljs-built_in">this</span>.error)
        <span class="hljs-keyword">break</span>
        <span class="hljs-comment">// 异步情况处理</span>
      <span class="hljs-keyword">case</span> PENDING:
        <span class="hljs-built_in">this</span>.successCallback.push(successCallback)
        <span class="hljs-built_in">this</span>.failCallback.push(failCallback)
        <span class="hljs-keyword">break</span>
    &#125;
  &#125;
&#125;
<span class="hljs-comment">// test</span>
<span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span> &#123;
    reslove(<span class="hljs-string">'reslove'</span>)
  &#125;, <span class="hljs-number">2000</span>)  
&#125;)
promise.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第一次调用then: '</span>, value)
&#125;)
promise.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第二次调用then: '</span>, value)
&#125;)
promise.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第三次调用then: '</span>, value)
&#125;)
<span class="hljs-comment">// 第一次调用then: reslove</span>
<span class="hljs-comment">// 第二次调用then: reslove</span>
<span class="hljs-comment">// 第三次调用then: reslove   </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了多次调用外，promise还支持链式调用。并且后面then方法的回调函数拿到的值是上一个then方法的回调函数的返回值。</p>
<h3 data-id="heading-3">第四版 - 链式调用</h3>
<p>这里值得注意的是，我们需要判断上一个then的返回值是什么类型。如果是普通的值，可以直接调用reslove方法。如果是promise对象，则需要根据promise对象返回的结果来决定调用reslove或者reject。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'pending'</span>
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'fufilled'</span>
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'rejected'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">exector</span>)</span> &#123;
    exector(<span class="hljs-built_in">this</span>.reslove, <span class="hljs-built_in">this</span>.reject)
  &#125;
  status = PENDING <span class="hljs-comment">// promise状态</span>
  value = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 成功时的值 then方法需要返回</span>
  error = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 失败时的值 then方法需要返回</span>
  successCallback = [] <span class="hljs-comment">// 成功回调</span>
  failCallback = [] <span class="hljs-comment">// 失败回调</span>
  <span class="hljs-comment">// 成功时的函数</span>
  reslove = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-comment">// 修改promise状态</span>
    <span class="hljs-built_in">this</span>.status = FULFILLED
    <span class="hljs-built_in">this</span>.value = value
    <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.successCallback.length) <span class="hljs-built_in">this</span>.successCallback.shift()(<span class="hljs-built_in">this</span>.value)
  &#125;
  <span class="hljs-comment">// 失败时的函数</span>
  reject = <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-comment">// 修改promise状态</span>
    <span class="hljs-built_in">this</span>.status = REJECTED
    <span class="hljs-built_in">this</span>.error = error
    <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.failCallback.length) <span class="hljs-built_in">this</span>.failCallback.shift()(<span class="hljs-built_in">this</span>.error)
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">successCallback, failCallback</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
      <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.status) &#123;
        <span class="hljs-keyword">case</span> FULFILLED:
          reslovePromise(successCallback(<span class="hljs-built_in">this</span>.value), reslove, reject)  
          <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> REJECTED:
          failCallBack(<span class="hljs-built_in">this</span>.error)
          <span class="hljs-keyword">break</span>
          <span class="hljs-comment">// 异步情况处理</span>
        <span class="hljs-keyword">case</span> PENDING:
          <span class="hljs-built_in">this</span>.successCallback.push(successCallback)
          <span class="hljs-built_in">this</span>.failCallback.push(failCallback)
          <span class="hljs-keyword">break</span>
      &#125;
    &#125;)  
  &#125;
&#125;
<span class="hljs-comment">// 通用方法 - 解析promise对象 (PENDING、 FULFILLED、REJECTED都会用到)</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reslovePromise</span>(<span class="hljs-params">x, reslove, reject</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (x <span class="hljs-keyword">instanceof</span> MyPromise) &#123;
    x.then(reslove, reject)
  &#125; <span class="hljs-keyword">else</span> &#123;
    reslove(x)
  &#125;
&#125;
<span class="hljs-comment">// test</span>
<span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
  reslove(<span class="hljs-string">'reslove'</span>)    
&#125;)
promise.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第一次调用then: '</span>, value)
  <span class="hljs-keyword">return</span> <span class="hljs-string">'reslove2'</span>
&#125;).then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第二次调用then: '</span>, value)
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
    reslove(<span class="hljs-string">'reslove3'</span>)
  &#125;)
&#125;).then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第三次调用then: '</span>, value)
&#125;)
<span class="hljs-comment">// 第一次调用then:  reslove</span>
<span class="hljs-comment">// 第二次调用then:  reslove2</span>
<span class="hljs-comment">// 第三次调用then:  reslove3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到第四版，我们的MyPromise实现了promise的基本功能。但从代码可以看出，我们并未对MyPromise做任何错误处理，这并不是一段健壮的代码该有的样子。那么接下来，我们就对MyPromise做一些代码优化及错误处理。</p>
<h3 data-id="heading-4">第五版 - 代码优化及错误处理</h3>
<p>错误处理想到了两方面。一是在reslove方法执行报错时，将状态改为REJECTED,执行reject方法。二是识别promise返回自对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'pending'</span>
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'fufilled'</span>
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'rejected'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">exector</span>)</span> &#123;
        <span class="hljs-keyword">try</span> &#123;
            exector(<span class="hljs-built_in">this</span>.reslove, <span class="hljs-built_in">this</span>.reject)
        &#125; <span class="hljs-keyword">catch</span>(e) &#123;
            <span class="hljs-built_in">this</span>.reject(e)
        &#125;
    &#125;

    status = PENDING <span class="hljs-comment">// promise状态</span>
    value = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 成功时的值 then方法需要返回</span>
    error = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 失败时的值 then方法需要返回</span>
    successCallback = [] <span class="hljs-comment">// 成功回调</span>
    failCallback = [] <span class="hljs-comment">// 失败回调</span>
    <span class="hljs-comment">// 成功时的函数</span>
    reslove = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        <span class="hljs-comment">// 修改promise状态</span>
        <span class="hljs-built_in">this</span>.status = FULFILLED
        <span class="hljs-built_in">this</span>.value = value
        <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.successCallback.length) <span class="hljs-built_in">this</span>.successCallback.shift()()
    &#125;
    <span class="hljs-comment">// 失败时的函数</span>
    reject = <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
        <span class="hljs-comment">// 修改promise状态</span>
        <span class="hljs-built_in">this</span>.status = REJECTED
        <span class="hljs-built_in">this</span>.error = error
        <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.failCallback.length) <span class="hljs-built_in">this</span>.failCallback.shift()()
    &#125;
    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">successCallback, failCallback</span>)</span> &#123;
        <span class="hljs-comment">// 将then方法的参数变为可选参数</span>
        successCallback = successCallback ? successCallback : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value
        failCallback = failCallback ? failCallback : <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;<span class="hljs-keyword">throw</span> error&#125;
        <span class="hljs-keyword">let</span> newPromise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
            <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.status) &#123;
                <span class="hljs-keyword">case</span> FULFILLED:
                    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span> &#123;
                        <span class="hljs-keyword">try</span> &#123;
                            reslovePromise(newPromise, successCallback(<span class="hljs-built_in">this</span>.value), reslove, reject)
                        &#125; <span class="hljs-keyword">catch</span>(e) &#123;
                            reject(e)
                        &#125;       
                    &#125;, <span class="hljs-number">0</span>)               
                    <span class="hljs-keyword">break</span>
                <span class="hljs-keyword">case</span> REJECTED:
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span> &#123;
                        <span class="hljs-keyword">try</span> &#123;
                            reslovePromise(newPromise, failCallback(<span class="hljs-built_in">this</span>.error), reslove, reject)
                        &#125; <span class="hljs-keyword">catch</span>(e) &#123;
                            reject(e)
                        &#125;       
                    &#125;, <span class="hljs-number">0</span>)
                    <span class="hljs-keyword">break</span>
                <span class="hljs-comment">// 异步情况处理</span>
                <span class="hljs-keyword">case</span> PENDING:
                    <span class="hljs-built_in">this</span>.successCallback.push(<span class="hljs-function">()=></span> &#123;
                        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span> &#123;
                            <span class="hljs-keyword">try</span> &#123;
                                reslovePromise(newPromise, successCallback(<span class="hljs-built_in">this</span>.value), reslove, reject)
                            &#125; <span class="hljs-keyword">catch</span>(e) &#123;
                                reject(e)
                            &#125;       
                        &#125;, <span class="hljs-number">0</span>)
                    &#125;)
                    <span class="hljs-built_in">this</span>.failCallback.push(<span class="hljs-function">()=></span> &#123;
                        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span> &#123;
                            <span class="hljs-keyword">try</span> &#123;
                                reslovePromise(newPromise, failCallback(<span class="hljs-built_in">this</span>.error), reslove, reject)
                            &#125; <span class="hljs-keyword">catch</span>(e) &#123;
                                reject(e)
                            &#125;       
                        &#125;, <span class="hljs-number">0</span>)
                    &#125;)
                    <span class="hljs-keyword">break</span>
            &#125;
        &#125;)
        <span class="hljs-keyword">return</span> newPromise   
    &#125;
&#125;
<span class="hljs-comment">// 通用方法 - 解析promose对象 (PENDING、 FULFILLED、REJECTED都会用到)</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reslovePromise</span>(<span class="hljs-params">newPromise ,x, reslove, reject</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (newPromise === x) &#123;
        <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'循环调用'</span>))
    &#125;
    <span class="hljs-keyword">if</span> (x <span class="hljs-keyword">instanceof</span> MyPromise) &#123;
        x.then(reslove, reject)
    &#125; <span class="hljs-keyword">else</span> &#123;
        reslove(x)
    &#125;
&#125;
<span class="hljs-comment">// test</span>
<span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">reslove, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span> &#123;
        reslove(<span class="hljs-string">'reslove'</span>)
    &#125;, <span class="hljs-number">2000</span>)

    <span class="hljs-comment">// reject('reject')</span>
&#125;)
promise.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第一次调用then reslove: '</span>, value)
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'then error'</span>)
&#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第一次调用then reject: '</span>, error)
&#125;).then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第二次调用then reslove: '</span>, value)
&#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第二次调用then reject: '</span>, error)
&#125;)
<span class="hljs-comment">// 第一次调用then reslove:  reslove</span>
<span class="hljs-comment">// 第二次调用then reject:  Error: then error</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            