
---
title: 'Promise的实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1270'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 23:33:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=1270'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span> (<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
resolve(<span class="hljs-string">'success'</span>);
reject(<span class="hljs-string">'fail'</span>);
&#125;)
p.then(<span class="hljs-function"><span class="hljs-params">data</span>=></span>&#123;&#125;,<span class="hljs-function"><span class="hljs-params">fail</span>=></span>&#123;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据上述Promise的基本使用，分析：</p>
<ul>
<li>Promise是一个构造函数</li>
<li>Promise接收一个立即执行的函数，且这个函数有两个参数，分别为resolve和reject</li>
<li>Promise有3中状态pending、fulfilled、rejected</li>
<li>resolve函数是将状态由pending改为fulfilled，reject函数是将状态由pending 改为rejected,且状态一旦变为fulfilled或者rejected就不能再更改状态了</li>
<li>then方法接收两个函数参数，成功执行第一个，失败执行第二个，且要将成功(resolve)、失败(reject)的参数传入相应的函数中</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'PENDING'</span>;
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'FULFILLED'</span>;
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'REJECTED'</span>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">myPromise</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">execute</span>)</span>&#123;
    execute(<span class="hljs-built_in">this</span>.resolve,<span class="hljs-built_in">this</span>.reject)
  &#125;
  status = PENDING;
  successParams = <span class="hljs-literal">undefined</span>;
  failParams = <span class="hljs-literal">undefined</span>;
  resolve = <span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status !== PENDING) <span class="hljs-keyword">return</span>;
    <span class="hljs-built_in">this</span>.status = FULFILLED;
    <span class="hljs-built_in">this</span>.successParams = value;
  &#125;
  reject = <span class="hljs-function">(<span class="hljs-params">error</span>)=></span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status !== PENDING) <span class="hljs-keyword">return</span>;
    <span class="hljs-built_in">this</span>.status = REJECTED;
    <span class="hljs-built_in">this</span>.failParams = error;
  &#125;
  then = <span class="hljs-function">(<span class="hljs-params">successCallback,failCallback</span>)=></span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === FULFILLED)&#123;
      successCallback(<span class="hljs-built_in">this</span>.successParams)
    &#125;
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === REJECTED)&#123;
      failCallback(<span class="hljs-built_in">this</span>.failParams)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>如果Promise立即执行函数中有一个异步的方法，那么then函数没法立即执行，见下面：</strong></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> myPromise(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    resolve(<span class="hljs-string">'sucess'</span>);
  &#125;,<span class="hljs-number">2000</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决方法:将then函数的两个方法存储起来，等resolve或者reject之后再执行</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">myPromise</span></span>&#123;
  ...
  successCallback = <span class="hljs-literal">undefined</span>;
  failCallback = <span class="hljs-literal">undefined</span>;
  resolve = <span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    ...
    <span class="hljs-built_in">this</span>.successCallback && <span class="hljs-built_in">this</span>.successCallback(value);
  &#125;
  reject = <span class="hljs-function">(<span class="hljs-params">error</span>)=></span>&#123;
    ...
    <span class="hljs-built_in">this</span>.failCallback && <span class="hljs-built_in">this</span>.failCallback(error)
  &#125;
  then = <span class="hljs-function">(<span class="hljs-params">successCallback,failCallback</span>)=></span>&#123;
    ...
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === PENDING)&#123;
      <span class="hljs-built_in">this</span>.successCallback = successCallback;
      <span class="hljs-built_in">this</span>.failCallback = failCallback;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Promise 还可以同时调用多个then方法，如:</strong></p>
<pre><code class="hljs language-jsx copyable" lang="jsx">p.then(<span class="hljs-function"><span class="hljs-params">data</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
  <span class="hljs-built_in">console</span>.log(data)
&#125;,<span class="hljs-function"><span class="hljs-params">error</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(error)
&#125;)

p.then(<span class="hljs-function"><span class="hljs-params">data</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)
  <span class="hljs-built_in">console</span>.log(data)
&#125;,<span class="hljs-function"><span class="hljs-params">error</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(error)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>思路：(如果Promise立即执行函数中是同步不需要改变，如果是异步需要改变)</p>
<p>将then中的两个函数用数组存储起来，等到resolve、reject后依次执行</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">myPromise</span></span>&#123;
  ...
  successCallback = [];
  failCallback = [];
  resolve = <span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
   ...
    <span class="hljs-comment">//this.successCallback && this.successCallback(value);</span>
    <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.successCallback.length) <span class="hljs-built_in">this</span>.successCallback.shift()(value)
  &#125;
  reject = <span class="hljs-function">(<span class="hljs-params">error</span>)=></span>&#123;
    ...
    <span class="hljs-comment">// this.failCallback && this.failCallback(error)</span>
    <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.failCallback.length) <span class="hljs-built_in">this</span>.failCallback.shift()(error)
  &#125;
  then = <span class="hljs-function">(<span class="hljs-params">successCallback,failCallback</span>)=></span>&#123;
    ...
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === PENDING)&#123;
      <span class="hljs-built_in">this</span>.successCallback.push(successCallback);
      <span class="hljs-built_in">this</span>.failCallback.push(failCallback);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Promise链式调用</strong></p>
<pre><code class="hljs language-jsx copyable" lang="jsx">p.then(<span class="hljs-function"><span class="hljs-params">data</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(data)
  <span class="hljs-keyword">return</span> <span class="hljs-number">100</span>
&#125;).then(<span class="hljs-function"><span class="hljs-params">data1</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">111</span>)
  <span class="hljs-built_in">console</span>.log(data1)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同步思路:</p>
<ul>
<li>then返回的要是一个Promise对象，这样才能继续调用then</li>
<li>上一个then的返回值给下一个then使用</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">myPromise</span></span>&#123;
...
  then = <span class="hljs-function">(<span class="hljs-params">successCallback,failCallback</span>)=></span>&#123;
    <span class="hljs-keyword">let</span> p2 = <span class="hljs-keyword">new</span> myPromise(<span class="hljs-function">(<span class="hljs-params">resolve</span>)=></span>&#123;
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === FULFILLED)&#123;
        <span class="hljs-keyword">let</span> x = successCallback(<span class="hljs-built_in">this</span>.successParams);
        resolve(x)
      &#125;
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === REJECTED)&#123;
        failCallback(<span class="hljs-built_in">this</span>.failParams)
      &#125;
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === PENDING)&#123;
        <span class="hljs-built_in">this</span>.successCallback.push(successCallback);
        <span class="hljs-built_in">this</span>.failCallback.push(failCallback);
      &#125;
    &#125;)
    <span class="hljs-keyword">return</span> p2;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Promise then第一个函数返回有可能是普通参数，也有可能是Promise对象(同步)</strong></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testPromise</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    resolve(<span class="hljs-number">2</span>)
  &#125;)
&#125;
p.then(<span class="hljs-function"><span class="hljs-params">data</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(data)
  <span class="hljs-keyword">return</span> testPromise()
&#125;).then(<span class="hljs-function"><span class="hljs-params">data1</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">111</span>)
  <span class="hljs-built_in">console</span>.log(data1)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>思路：</p>
<ul>
<li>如果返回的是普通参数，直接返回给下一个then使用</li>
<li>如果返回的是一个Promise对象，将成功的参数返回给下一个then的第一个函数使用，失败的参数返回给第二个函数使用</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span></span>&#123;
  ...
  then = <span class="hljs-function">(<span class="hljs-params">successCallback,failCallback</span>)=></span>&#123;
    <span class="hljs-keyword">let</span> p2 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === FULFILLED)&#123;
        <span class="hljs-keyword">let</span> x = successCallback(<span class="hljs-built_in">this</span>.successParams);
        promiseResolve(x,resolve,reject)
      &#125;
     ...
    &#125;)
    <span class="hljs-keyword">return</span> p2;
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promiseResolve</span>(<span class="hljs-params">x,resolve,reject</span>)</span>&#123;
  <span class="hljs-keyword">if</span>(x <span class="hljs-keyword">instanceof</span> MyPromise)&#123;
    x.then(resolve,reject)
  &#125;<span class="hljs-keyword">else</span>&#123;
    resolve(x)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Promise then(第一个函数) 不能返回当前的这个Promise对象：</strong></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">let</span> p1 = p.then(<span class="hljs-function"><span class="hljs-params">data</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(data)
  <span class="hljs-keyword">return</span> p1
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>思路:比对then返回的Promise和当前的promise对象，如果一样就抛错</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span></span>&#123;
  ...
  then = <span class="hljs-function">(<span class="hljs-params">successCallback,failCallback</span>)=></span>&#123;
    <span class="hljs-keyword">let</span> p2 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === FULFILLED)&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
          <span class="hljs-keyword">let</span> x = successCallback(<span class="hljs-built_in">this</span>.successParams);
          promiseResolve(p2,x,resolve,reject)
        &#125;,<span class="hljs-number">0</span>);
      &#125;
      ...
    &#125;)
    <span class="hljs-keyword">return</span> p2;
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promiseResolve</span>(<span class="hljs-params">p,x,resolve,reject</span>)</span>&#123;
  <span class="hljs-keyword">if</span>(p === x)&#123;
    <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'error'</span>))
  &#125;
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遇到两个坑，1.必须加setTimeout，否则拿不到当前的Promise对象p2和then返回的当前Promise对象；2.在使用的时候，不能then去链式调用，这样两个Promise就不一样，没法比较了，见下面</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">错误的写法:
 p.then(<span class="hljs-function"><span class="hljs-params">data</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(data)
  <span class="hljs-keyword">return</span> p1
&#125;).then(<span class="hljs-function"><span class="hljs-params">data1</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">111</span>)
&#125;,<span class="hljs-function"><span class="hljs-params">reason</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(reason)
&#125;)

正确的写法:
<span class="hljs-keyword">let</span> p1 = p.then(<span class="hljs-function"><span class="hljs-params">data</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(data)
  <span class="hljs-keyword">return</span> p1
&#125;)
p1.then(<span class="hljs-function"><span class="hljs-params">data1</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">111</span>)
&#125;,<span class="hljs-function"><span class="hljs-params">reason</span>=></span>&#123;
  <span class="hljs-built_in">console</span>.log(reason)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>捕获Promise中的错误</strong></p>
<p>思路:promise中的错误来源</p>
<ul>
<li>Promise立即执行函数</li>
<li>then中的两个函数</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">execute</span>)</span>&#123;
    <span class="hljs-keyword">try</span> &#123;
      execute(<span class="hljs-built_in">this</span>.resolve,<span class="hljs-built_in">this</span>.reject)
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-built_in">this</span>.reject(error)
    &#125;
  &#125;
  ...
  resolve = <span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    ...
    <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.successCallback.length) <span class="hljs-built_in">this</span>.successCallback.shift()()
  &#125;
  reject = <span class="hljs-function">(<span class="hljs-params">error</span>)=></span>&#123;
    ...
    <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.failCallback.length) <span class="hljs-built_in">this</span>.failCallback.shift()()
  &#125;
  then = <span class="hljs-function">(<span class="hljs-params">successCallback,failCallback</span>)=></span>&#123;
    <span class="hljs-keyword">let</span> p2 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === FULFILLED)&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = successCallback(<span class="hljs-built_in">this</span>.successParams);
            promiseResolve(p2,x,resolve,reject)
          &#125; <span class="hljs-keyword">catch</span> (error) &#123;
            reject(error)
          &#125;
        &#125;,<span class="hljs-number">0</span>);
      &#125;
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === REJECTED)&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = failCallback(<span class="hljs-built_in">this</span>.failParams);
            promiseResolve(p2,x,resolve,reject)
          &#125; <span class="hljs-keyword">catch</span> (error) &#123;
            reject(error)
          &#125;
        &#125;,<span class="hljs-number">0</span>);
      &#125;
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === PENDING)&#123;
        <span class="hljs-built_in">this</span>.successCallback.push(<span class="hljs-function">()=></span>&#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">let</span> x = successCallback(<span class="hljs-built_in">this</span>.successParams);
              promiseResolve(p2,x,resolve,reject)
            &#125; <span class="hljs-keyword">catch</span> (error) &#123;
              reject(error)
            &#125;
          &#125;,<span class="hljs-number">0</span>);
        &#125;);
        <span class="hljs-built_in">this</span>.failCallback.push(<span class="hljs-function">()=></span>&#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">let</span> x = failCallback(<span class="hljs-built_in">this</span>.failParams);
              promiseResolve(p2,x,resolve,reject)
            &#125; <span class="hljs-keyword">catch</span> (error) &#123;
              reject(error)
            &#125;
          &#125;,<span class="hljs-number">0</span>);
        &#125;);
      &#125;
    &#125;)
    <span class="hljs-keyword">return</span> p2;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：异步方法是在resolve/reject执行后，才执行下一个相应的then函数,</p>
<p><strong>Promise还有一种调用方法.then中是空的</strong></p>
<pre><code class="hljs language-jsx copyable" lang="jsx">p.then().then().then(<span class="hljs-function"><span class="hljs-params">value</span>=></span><span class="hljs-built_in">console</span>.log(value))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>思路：在then中没有函数的时候，补齐函数(下面是源码)</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'PENDING'</span>;
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'FULFILLED'</span>;
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'REJECTED'</span>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">execute</span>)</span>&#123;
    <span class="hljs-keyword">try</span> &#123;
      execute(<span class="hljs-built_in">this</span>.resolve,<span class="hljs-built_in">this</span>.reject)
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-built_in">this</span>.reject(error)
    &#125;
  &#125;
  status = PENDING;
  successParams = <span class="hljs-literal">undefined</span>;
  failParams = <span class="hljs-literal">undefined</span>;
  successCallback = [];
  failCallback = [];
  resolve = <span class="hljs-function">(<span class="hljs-params">value</span>)=></span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status !== PENDING) <span class="hljs-keyword">return</span>;
    <span class="hljs-built_in">this</span>.status = FULFILLED;
    <span class="hljs-built_in">this</span>.successParams = value;
    <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.successCallback.length) <span class="hljs-built_in">this</span>.successCallback.shift()()
  &#125;
  reject = <span class="hljs-function">(<span class="hljs-params">error</span>)=></span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status !== PENDING) <span class="hljs-keyword">return</span>;
    <span class="hljs-built_in">this</span>.status = REJECTED;
    <span class="hljs-built_in">this</span>.failParams = error;
    <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.failCallback.length) <span class="hljs-built_in">this</span>.failCallback.shift()()
  &#125;
  then = <span class="hljs-function">(<span class="hljs-params">successCallback,failCallback</span>)=></span>&#123;
    successCallback = successCallback ? successCallback : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value;
    failCallback = failCallback ? failCallback : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value;
    <span class="hljs-keyword">let</span> p2 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === FULFILLED)&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = successCallback(<span class="hljs-built_in">this</span>.successParams);
            promiseResolve(p2,x,resolve,reject)
          &#125; <span class="hljs-keyword">catch</span> (error) &#123;
            reject(error)
          &#125;
        &#125;,<span class="hljs-number">0</span>);
      &#125;
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === REJECTED)&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = failCallback(<span class="hljs-built_in">this</span>.failParams);
            promiseResolve(p2,x,resolve,reject)
          &#125; <span class="hljs-keyword">catch</span> (error) &#123;
            reject(error)
          &#125;
        &#125;,<span class="hljs-number">0</span>);
      &#125;
      <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === PENDING)&#123;
        <span class="hljs-built_in">this</span>.successCallback.push(<span class="hljs-function">()=></span>&#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">let</span> x = successCallback(<span class="hljs-built_in">this</span>.successParams);
              promiseResolve(p2,x,resolve,reject)
            &#125; <span class="hljs-keyword">catch</span> (error) &#123;
              reject(error)
            &#125;
          &#125;,<span class="hljs-number">0</span>);
        &#125;);
        <span class="hljs-built_in">this</span>.failCallback.push(<span class="hljs-function">()=></span>&#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">let</span> x = failCallback(<span class="hljs-built_in">this</span>.failParams);
              promiseResolve(p2,x,resolve,reject)
            &#125; <span class="hljs-keyword">catch</span> (error) &#123;
              reject(error)
            &#125;
          &#125;,<span class="hljs-number">0</span>);
        &#125;);
      &#125;
    &#125;)
    <span class="hljs-keyword">return</span> p2;
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promiseResolve</span>(<span class="hljs-params">p,x,resolve,reject</span>)</span>&#123;
  <span class="hljs-keyword">if</span>(p === x)&#123;
    <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'error'</span>))
  &#125;
  <span class="hljs-keyword">if</span>(x <span class="hljs-keyword">instanceof</span> MyPromise)&#123;
    x.then(resolve,reject)
  &#125;<span class="hljs-keyword">else</span>&#123;
    resolve(x)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果有错误或者不严谨的地方，请务必给予指正，十分感谢。</p></div>  
</div>
            