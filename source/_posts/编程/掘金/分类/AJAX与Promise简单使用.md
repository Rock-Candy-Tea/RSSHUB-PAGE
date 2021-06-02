
---
title: 'AJAX与Promise简单使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5442'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 04:10:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=5442'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">AJAX</h1>
<h2 data-id="heading-1">1. 介绍</h2>
<p>AJAX，是 Asynchronous JavaScript And XML，意思是利用JavaScript执行异步网络请求，对页面进行局部更新，而不需要重载页面。</p>
<p>AJAX是浏览器的功能，利用浏览器在window上增加的XMLHttpRequest函数，利用该函数构造出一个对象，使用该对象进行请求发送与响应接受。</p>
<h2 data-id="heading-2">2. 使用</h2>
<ol>
<li>创建一个<code>XMLHttpRequest</code>对象</li>
<li>调用对象的<code>open</code>方法启用。</li>
<li>监听对象的 <code>onreadystatechange</code> 事件（或者是<code>onload</code>和<code>onerror</code>事件），处理函数对返回的数据进行处理。</li>
<li>调用对象的<code>send</code>方法发送请求。</li>
</ol>
<p>完整版：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> request = <span class="hljs-keyword">new</span> XMLHttpRequest()
request.open(<span class="hljs-string">'GET'</span>,<span class="hljs-string">'/xxx'</span>)
request.onreadystateChange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">
    <span class="hljs-keyword">if</span>(request.readyState === <span class="hljs-number">4</span>)&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求完成'</span>)
        <span class="hljs-keyword">if</span>(request.responese.status >= <span class="hljs-number">200</span> && request.response.status < <span class="hljs-number">300</span>)&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求成功'</span>)
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求失败'</span>)
        &#125;
    &#125;
</span>)
<span class="hljs-title">request</span>.<span class="hljs-title">send</span>(<span class="hljs-params"></span>)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>简略版：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> request = <span class="hljs-keyword">new</span> XMLHttpRequest()
request.open(<span class="hljs-string">'GET'</span>,<span class="hljs-string">'/xxx'</span>)
request.onload = <span class="hljs-function">()=></span>&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求成功'</span>)
request.send()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">3. onreadystatechange</h2>



































<table><thead><tr><th>值</th><th>状态</th><th>描述</th></tr></thead><tbody><tr><td>0</td><td>UNSENT</td><td>代理被创建，但尚未调用 open() 方法。</td></tr><tr><td>1</td><td>OPENED</td><td>open() 方法已经被调用。</td></tr><tr><td>2</td><td>HEADERS_RECEIVED</td><td>send() 方法已经被调用，并且头部和状态已经可获得。</td></tr><tr><td>3</td><td>LOADING</td><td>下载中； responseText 属性已经包含部分数据。</td></tr><tr><td>4</td><td>DONE</td><td>下载操作已完成。</td></tr></tbody></table>
<p>创建 -> 打开 -> 发送 -> 接收 -> 完成</p>
<p>每一次state的改变都会触发readystatechange事件，但我们一般只关心state为4的阶段，此阶段数据接收已完成，可来进行数据处理。onload函数也会在请求完成后即state为4的时候调用。</p>
<p><strong>终止请求</strong></p>
<p>使用XHR对象的<strong>abort</strong>方法会终止该请求，state会被重置为0。</p>
<h1 data-id="heading-4">Promise</h1>
<h2 data-id="heading-5">1. 介绍</h2>
<p>Promise是在ES6中确定的对异步及回调处理的规范实现。</p>
<p>一个 Promise 必然处于以下几种状态之一：</p>
<ul>
<li>待定（pending）: 初始状态，既没有被兑现，也没有被拒绝。</li>
<li>已兑现（fulfilled）: 意味着操作成功完成。</li>
<li>已拒绝（rejected）: 意味着操作失败。</li>
</ul>
<h2 data-id="heading-6">2. 使用Promise封装ajax</h2>
<p>关键：<code>return new Promise((resolve, reject)=>&#123;...&#125;)</code> 用以返回一个Promise对象。</p>
<pre><code class="hljs language-js copyable" lang="js">ajax = <span class="hljs-function">(<span class="hljs-params">method, url</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>)=></span>&#123; <span class="hljs-comment">//关键，用以返回一个Promise对象</span>
        <span class="hljs-keyword">var</span> request = <span class="hljs-keyword">new</span> XMLHttpRequest() 
        request.open(method, url)
        request.onreadystateChange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">
            <span class="hljs-keyword">if</span>(request.readyState === <span class="hljs-number">4</span>)&#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求完成'</span>)
                <span class="hljs-keyword">if</span>(request.responese.status === <span class="hljs-number">200</span>)&#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求成功'</span>)
                    resolve.call(<span class="hljs-literal">null</span>, request.response) <span class="hljs-regexp">//</span>成功则调用resolve
                &#125;<span class="hljs-keyword">else</span>&#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求失败'</span>)
                    reject.call(<span class="hljs-literal">null</span>, request) <span class="hljs-regexp">//</span>失败则调用reject
                &#125;
            &#125;
        </span>)
        <span class="hljs-title">request</span>.<span class="hljs-title">send</span>(<span class="hljs-params"></span>)
    &#125;)
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">3. then / catch / finally 函数</h2>
<p>一个Promise对象具有then函数，then函数接受两个函数，第一个函数当 Promise 变成接受状态（fulfilled）时被调用，第二个函数当 Promise 变成拒绝状态（rejected）时被调用。</p>
<p>catch 接收一个函数，在Promise被reject的时候执行，除非该函数抛出错误或返回一个失败的Promise，否则返回的Promise一直是resolved。实质上catch(failureCallback) 是 then(null, failureCallback) 的缩略形式。</p>
<p>finally接收一个回调函数，在promise结束时，无论结果是fulfilled或者是rejected，都会执行指定该回调函数。这避免了同样的语句需要在then()和catch()中各写一次的情况。</p>
<p>以调用上面封装的ajax函数为例</p>
<pre><code class="hljs language-js copyable" lang="js">ajax(<span class="hljs-string">'GET'</span>,<span class="hljs-string">'/user'</span>)
.then(
    <span class="hljs-function"><span class="hljs-params">res</span>=></span> <span class="hljs-built_in">console</span>.log(res),
    <span class="hljs-function"><span class="hljs-params">request</span> =></span> <span class="hljs-built_in">console</span>.log(request)
)
.catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))
.finally( <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'结束'</span>) )
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">4. all / race / any 函数</h2>
<ul>
<li>
<p>对比小结：</p>
<ul>
<li>都接受一个可迭代对象</li>
<li>all：全resolve才resolve，任何一个reject则reject</li>
<li>race：任何一个resolve或reject，则返回其状态</li>
<li>any：任何一个resolve，则成功。全为reject，则reject。</li>
</ul>
</li>
<li>
<p><strong>Promise.all(iterable)</strong></p>
<p>返回一个 Promise 实例，此实例在 iterable 参数内所有的 promise 都“完成（resolved）”或参数中不包含 promise 时回调完成（resolve）；如果参数中 promise 有一个失败（rejected），此实例回调失败（reject），失败原因的是第一个失败 promise 的结果。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise1 = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">3</span>);
<span class="hljs-keyword">const</span> promise2 = <span class="hljs-number">42</span>;
<span class="hljs-keyword">const</span> promise3 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">100</span>, <span class="hljs-string">'foo'</span>);
&#125;);

<span class="hljs-built_in">Promise</span>.all([promise1, promise2, promise3]).then(<span class="hljs-function">(<span class="hljs-params">values</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(values);
&#125;);
<span class="hljs-comment">// expected output: Array [3, 42, "foo"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>Promise.race(iterable)</strong></p>
<p>当iterable参数里的任意一个子promise被成功或失败后，父promise马上也会用子promise的成功返回值或失败详情作为参数调用父promise绑定的相应句柄，并返回该promise对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promise1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">500</span>, <span class="hljs-string">'one'</span>);
&#125;);

<span class="hljs-keyword">const</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">100</span>, <span class="hljs-string">'two'</span>);
&#125;);

<span class="hljs-built_in">Promise</span>.race([promise1, promise2]).then(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(value);
  <span class="hljs-comment">// Both resolve, but promise2 is faster</span>
&#125;);
<span class="hljs-comment">// expected output: "two"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>Promise.any(iterable)</strong></p>
<p>接收一个Promise对象的集合，当其中的一个 promise 成功，就返回那个成功的promise的值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> pErr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  reject(<span class="hljs-string">"总是失败"</span>);
&#125;);

<span class="hljs-keyword">const</span> pSlow = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">500</span>, <span class="hljs-string">"最终完成"</span>);
&#125;);

<span class="hljs-keyword">const</span> pFast = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">100</span>, <span class="hljs-string">"很快完成"</span>);
&#125;);

<span class="hljs-built_in">Promise</span>.any([pErr, pSlow, pFast]).then(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(value);
  <span class="hljs-comment">// pFast fulfils first</span>
&#125;)
<span class="hljs-comment">// 期望输出: "很快完成"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h1 data-id="heading-9">async / await</h1>
<ol>
<li>介绍</li>
</ol>
<blockquote>
<pre><code class="copyable">async和await关键字让我们可以用一种更简洁的方式写出基于Promise的异步行为，而无需刻意地链式调用promise。
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p>async声明一个函数为异步执行的，await则是等待一个异步方法执行完成。</p>
<p>async函数一定会返回一个promise对象。如果一个async函数的返回值看起来不是promise，那么它将会被隐式地包装在一个promise中。</p>
<p>await后面的代码可近似认为是在promise的then的回调的，多个await相当于链式调用多个then。</p>
<p>使用async / await，则无需使用promise.then传递回调函数。在await之后的代码会等待结束后继续执行，错误处理使用try...catch..</p>
<p>以下代码实现的功能等价：</p>
<ul>
<li>使用Promise</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">ajax(<span class="hljs-string">'GET'</span>,<span class="hljs-string">'user'</span>).then(<span class="hljs-function">(<span class="hljs-params">res</span>)=></span><span class="hljs-built_in">console</span>.log(res), <span class="hljs-function">(<span class="hljs-params">err</span>)=></span><span class="hljs-built_in">console</span>.log(err))
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用async / await</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">xxx</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">try</span>&#123;
        <span class="hljs-keyword">let</span> result = <span class="hljs-keyword">await</span> ajax(<span class="hljs-string">'GET'</span>,<span class="hljs-string">'user'</span>)
        <span class="hljs-built_in">console</span>.log(result)
    &#125;<span class="hljs-keyword">catch</span>(err)&#123;
        <span class="hljs-built_in">console</span>.log(error)
    &#125;
&#125;
xxx()
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            