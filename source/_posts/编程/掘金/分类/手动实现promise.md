
---
title: '手动实现promise'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8115'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 23:25:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=8115'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">1、基础版promise的实现</h4>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// 1.promise是一个类</span>
<span class="hljs-comment">// 2.当使用promise的时候 会传入一个执行器，此执行器是立即执行</span>
<span class="hljs-comment">// 3.当前executor 给了两个函数可以来描述当前promise的状态。promise中有三个状态 成功态  失败态 等待态</span>
<span class="hljs-comment">// 默认为等待态  如果调用resolve会走到成功态，如果调用reject 或者发生异常 会走失败态</span>
<span class="hljs-comment">// 4.每个promise实例都有一个then方法</span>
<span class="hljs-comment">// 5.promise 一旦状态变化后不能更改</span>
<span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'PENGING'</span>
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'FULFILLED'</span>
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'REJECTED'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.status = PENDING 
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 成功结果</span>
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 失败原因</span>
    <span class="hljs-keyword">const</span> resolve = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123; <span class="hljs-comment">// 只有在状态为pending的时候才能够修改状态</span>
        <span class="hljs-built_in">this</span>.status = FULFILLED
        <span class="hljs-built_in">this</span>.value = value
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> reject = <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123; <span class="hljs-comment">// 只有在状态为pending的时候才能够修改状态</span>
        <span class="hljs-built_in">this</span>.status = REJECTED
        <span class="hljs-built_in">this</span>.reason = reason
      &#125;
    &#125;
    <span class="hljs-keyword">try</span> &#123;
      executor(resolve,reject) <span class="hljs-comment">// promise 有两个参数 分别为成功的执行函数 和失败的执行函数</span>
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      reject(error) <span class="hljs-comment">// 针对执行器立即执行的时候抛出错误 </span>
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled,onRejected</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === FULFILLED)&#123; <span class="hljs-comment">// 执行成功回调</span>
      onFulfilled(<span class="hljs-built_in">this</span>.value)
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123; <span class="hljs-comment">// 执行失败回调</span>
      onRejected(<span class="hljs-built_in">this</span>.reason)
    &#125;
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-built_in">Promise</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2、promise的异步处理</h4>
<p>针对场景：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123; <span class="hljs-comment">// pending</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'ok'</span>)
  &#125;, <span class="hljs-number">1000</span>);
&#125;)

<span class="hljs-comment">// 当用户调用then方法的时候 此时promise可能为等待态， 先暂存起来，因为后续可能会调用resolve和reject， 等会再触发对应onFulfilled 或者 onRejected</span>
promise.then(<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123; <span class="hljs-comment">// then是异步的</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'success1'</span>,value)
&#125;,<span class="hljs-function">(<span class="hljs-params">reason</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'err'</span>,reason)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用发布订阅将回调函数暂存 最后执行</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'PENGING'</span>
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'FULFILLED'</span>
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'REJECTED'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.status = PENDING 
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 成功结果</span>
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 失败原因</span>
    <span class="hljs-built_in">this</span>.onResolvedCallbacks = [] <span class="hljs-comment">// 存储成功的回调函数</span>
    <span class="hljs-built_in">this</span>.onRejectedCallbacks = [] <span class="hljs-comment">// 存储失败的回调函数</span>
    <span class="hljs-keyword">const</span> resolve = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123; <span class="hljs-comment">// 只有在状态为pending的时候才能够修改状态</span>
        <span class="hljs-built_in">this</span>.status = FULFILLED
        <span class="hljs-built_in">this</span>.value = value
        <span class="hljs-comment">// 发布</span>
        <span class="hljs-built_in">this</span>.onResolvedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn())
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> reject = <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123; <span class="hljs-comment">// 只有在状态为pending的时候才能够修改状态</span>
        <span class="hljs-built_in">this</span>.status = REJECTED
        <span class="hljs-built_in">this</span>.reason = reason
        <span class="hljs-comment">// 发布</span>
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn())
      &#125;
    &#125;
    <span class="hljs-keyword">try</span> &#123;
      executor(resolve,reject) <span class="hljs-comment">// promise 有两个参数 分别为成功的执行函数 和失败的执行函数</span>
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      reject(error) <span class="hljs-comment">// 针对执行器立即执行的时候抛出错误 </span>
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled,onRejected</span>)</span> &#123;
    <span class="hljs-comment">// 订阅</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING)&#123; <span class="hljs-comment">// 在pending状态的时候收集成功回调/失败回调 利用切片编程(AOP)实现成功/失败回调函数的可扩展性</span>
      <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(<span class="hljs-function">()=></span> &#123;
        <span class="hljs-comment">// 此处可以增加自定义逻辑</span>
        onFulfilled(<span class="hljs-built_in">this</span>.value)
      &#125;)
      <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">()=></span> &#123;
        <span class="hljs-comment">// 此处可以增加自定义逻辑</span>
        onRejected(<span class="hljs-built_in">this</span>.reason)
      &#125;)
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === FULFILLED)&#123; <span class="hljs-comment">// 执行成功回调</span>
      onFulfilled(<span class="hljs-built_in">this</span>.value)
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123; <span class="hljs-comment">// 执行失败回调</span>
      onRejected(<span class="hljs-built_in">this</span>.reason)
    &#125;
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-built_in">Promise</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3、promise的链式调用</h4>
<p>当调用.then方法之后回返回一个新的promise</p>
<p>分析then方法的返回值</p>
<p>情况1： then中方法返回的是一个（普通值 不是promise）的情况, 会作为外层下一次then的成功结果</p>
<p>情况2： then中方法 执行出错 会走到外层下一次then的失败结果</p>
<p>清空3： 如果then中方法返回的是一个promise对象， 此时会根据promise的结果来处理是走成功还是失败 （传入的是成功或者失败的内容）</p>
<p>无论上一次then走是成功还是失败，只要返回的是普通值 都会执行下一次then的成功 如果返回一个失败的promise或者抛出异常，会走下一个then的失败</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 利用x的值来判断是调用promise2的resolve还是reject</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span> (<span class="hljs-params">promise2,x,resolve,reject</span>) </span>&#123;
  <span class="hljs-comment">// 第一种情况 如果返回的x和promise2相同 直接抛异常</span>
 <span class="hljs-keyword">if</span> (promise2 === x) &#123;
    <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'错误'</span>))
  &#125;
  <span class="hljs-comment">// 判断返回的是不是对象或者函数  只有返回的是对象或者函数才有可能是promise </span>
  <span class="hljs-keyword">if</span> ((<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'object'</span> && x !== <span class="hljs-literal">null</span>) || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-comment">// 兼容其他的promise 避免重复调用出现异常</span>
    <span class="hljs-keyword">let</span> called = <span class="hljs-literal">false</span>
    <span class="hljs-comment">// 通过.then方法判断是不是promise 由于.then的时候可能出现异常 </span>
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">let</span> then = x.then
      <span class="hljs-comment">// 如果then是一个函数 则认为是promise</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> then === <span class="hljs-string">'function'</span>) &#123;
        <span class="hljs-comment">// 此处不建议直接使用x.then 这样写同样会触发getter可能会发生异常</span>
        then.call(x,<span class="hljs-function">(<span class="hljs-params">y</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span> 
          called = <span class="hljs-literal">true</span>
          resolvePromise(promise2,x,resolve,reject) <span class="hljs-comment">// 一直解析到不是promise为止</span>
        &#125;, <span class="hljs-function">(<span class="hljs-params">r</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span> 
          called = <span class="hljs-literal">true</span>
          reject(r)
        &#125;)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// then不是函数 直接调用resolve</span>
        resolve(x)
      &#125;
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span> 
      called = <span class="hljs-literal">true</span>
      reject(error)
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 既不是对象也不是函数则为普通值 直接调用resolve</span>
    resolve(x)
  &#125;
&#125;
<span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'PENGING'</span>
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'FULFILLED'</span>
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'REJECTED'</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.status = PENDING 
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 成功结果</span>
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 失败原因</span>
    <span class="hljs-built_in">this</span>.onResolvedCallbacks = [] <span class="hljs-comment">// 存储成功的回调函数</span>
    <span class="hljs-built_in">this</span>.onRejectedCallbacks = [] <span class="hljs-comment">// 存储失败的回调函数</span>
    <span class="hljs-keyword">const</span> resolve = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123; <span class="hljs-comment">// 只有在状态为pending的时候才能够修改状态</span>
        <span class="hljs-built_in">this</span>.status = FULFILLED
        <span class="hljs-built_in">this</span>.value = value
        <span class="hljs-comment">// 发布</span>
        <span class="hljs-built_in">this</span>.onResolvedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn())
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> reject = <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123; <span class="hljs-comment">// 只有在状态为pending的时候才能够修改状态</span>
        <span class="hljs-built_in">this</span>.status = REJECTED
        <span class="hljs-built_in">this</span>.reason = reason
        <span class="hljs-comment">// 发布</span>
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn())
      &#125;
    &#125;
    <span class="hljs-keyword">try</span> &#123;
      executor(resolve,reject) <span class="hljs-comment">// promise 有两个参数 分别为成功的执行函数 和失败的执行函数</span>
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      reject(error) <span class="hljs-comment">// 针对执行器立即执行的时候抛出错误 </span>
    &#125;
  &#125;
  <span class="hljs-comment">// then参数是可选的</span>
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled,onRejected</span>)</span> &#123;
    onFulfilled = <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">'function'</span> ? onFulfilled : <span class="hljs-function"><span class="hljs-params">v</span> =></span> v
    onRejected = <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span> ? onRejected : <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123; <span class="hljs-keyword">throw</span> err &#125;
    <span class="hljs-comment">// 针对链式调用的处理 需要返回一个新的promise</span>
    <span class="hljs-keyword">let</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>) =></span> &#123;
      <span class="hljs-comment">// 将一下代码包裹在new Promise中 是因为需要拿到then方法的返回值 即 x</span>
        <span class="hljs-comment">// 订阅</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING)&#123; <span class="hljs-comment">// 在pending状态的时候收集成功回调/失败回调 利用切片编程(AOP)实现成功/失败回调函数的可扩展性</span>
        <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(<span class="hljs-function">()=></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123; <span class="hljs-comment">// 由于需要拿到promise2的值作为后续then方法的判断 同步执行会造成死循环 </span>
              <span class="hljs-comment">// 此处可以增加自定义逻辑</span>
          <span class="hljs-keyword">try</span> &#123; <span class="hljs-comment">// 针对then方法中 抛出异常处理 throw new Error()</span>
            <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value) <span class="hljs-comment">// x为成功回调的返回值</span>
            <span class="hljs-comment">// 此x 可能是一个promise， 如果是promise需要看一下这个promise是成功还是失败 .then ,如果成功则把成功的结果 调用promise2的resolve传递进去，如果失败则同理</span>
            <span class="hljs-comment">// x的值是决定调用promise2的成功还是失败 如果是promise则取它的状态 如果是普通值 则直接调用resolve</span>
            resolvePromise(promise2,x,resolve,reject)
          &#125; <span class="hljs-keyword">catch</span> (error) &#123; <span class="hljs-comment">// 如果then方法中抛出异常 直接走到下一个then的reject中</span>
            reject(error)
          &#125;
          &#125;, <span class="hljs-number">0</span>);
        &#125;)
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">()=></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 此处可以增加自定义逻辑</span>
            <span class="hljs-keyword">try</span> &#123; <span class="hljs-comment">// 针对then方法中 抛出异常处理 throw new Error()</span>
              <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.reason) <span class="hljs-comment">// x为失败回调的返回值</span>
              resolvePromise(promise2,x,resolve,reject)
            &#125; <span class="hljs-keyword">catch</span> (error) &#123; <span class="hljs-comment">// 如果then方法中抛出异常 直接走到下一个then的reject中</span>
              reject(error)
            &#125;
            &#125;, <span class="hljs-number">0</span>);
        &#125;)
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === FULFILLED)&#123; <span class="hljs-comment">// 执行成功回调</span>
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123; <span class="hljs-comment">// 针对then方法中 抛出异常处理 throw new Error()</span>
            <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value) <span class="hljs-comment">// x为成功回调的返回值</span>
            resolvePromise(promise2,x,resolve,reject)
          &#125; <span class="hljs-keyword">catch</span> (error) &#123; <span class="hljs-comment">// 如果then方法中抛出异常 直接走到下一个then的reject中</span>
            reject(error)
          &#125;
        &#125;, <span class="hljs-number">0</span>);
      &#125;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === REJECTED) &#123; <span class="hljs-comment">// 执行失败回调</span>
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123; <span class="hljs-comment">// 针对then方法中 抛出异常处理 throw new Error()</span>
            <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.reason) <span class="hljs-comment">// x为失败回调的返回值</span>
            resolvePromise(promise2,x,resolve,reject)
          &#125; <span class="hljs-keyword">catch</span> (error) &#123; <span class="hljs-comment">// 如果then方法中抛出异常 直接走到下一个then的reject中</span>
            reject(error)
          &#125;
        &#125;, <span class="hljs-number">0</span>);
      &#125;
    &#125;)
   
    <span class="hljs-keyword">return</span> promise2
    <span class="hljs-comment">// 此处不能直接return this this是当前的promise 返回的必须是一个新的promise 如果是当前的promise promise的状态是一旦改变便无法再次更改的</span>
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-built_in">Promise</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">测试promise</h5>
<p>安装测试插件
<code>npm install promises-aplus-tests -g</code></p>
<p>添加一下测试代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.deferred = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> dfd = &#123;&#125;;
    dfd.promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
        dfd.resolve= resolve;
        dfd.reject = reject;
    &#125;); 
    <span class="hljs-keyword">return</span> dfd;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>命令行执行命令<code>promises-aplus-tests xxx.js</code></p></div>  
</div>
            