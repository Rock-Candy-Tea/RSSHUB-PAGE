
---
title: 'JS处理并行请求的四种方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9258'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 01:39:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=9258'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">需求</h3>
<p>两个异步请求同时发出，两个请求都返回时再做处理</p>
<h3 data-id="heading-1">实现</h3>
<p>这里的方法仅提供思路，只做请求成功处理</p>
<h5 data-id="heading-2">方法一</h5>
<p>使用Promise.all</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> startTime = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">time</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(time)
    &#125;, time)
  &#125;)
&#125;
<span class="hljs-keyword">let</span> request1 = request(<span class="hljs-number">3000</span>)
<span class="hljs-keyword">let</span> request2 = request(<span class="hljs-number">2000</span>)
<span class="hljs-built_in">Promise</span>.all([request1, request2]).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() - startTime)<span class="hljs-comment">// [ 3000, 2000 ] 3001</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">方法二</h5>
<p>自定义状态，在回调中判断返回状态，待2个请求都有返回值时再做处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> startTime = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">time</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(time)
    &#125;, time)
  &#125;)
&#125;
<span class="hljs-keyword">let</span> state = [<span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>]
<span class="hljs-keyword">let</span> request1 = request(<span class="hljs-number">3000</span>)
<span class="hljs-keyword">let</span> request2 = request(<span class="hljs-number">2000</span>)
request1.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  state[<span class="hljs-number">0</span>] = res
  process()
&#125;)
request2.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  state[<span class="hljs-number">1</span>] = res
  process()
&#125;)
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">process</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (state[<span class="hljs-number">0</span>] && state[<span class="hljs-number">1</span>]) &#123;
    <span class="hljs-built_in">console</span>.log(state, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() - startTime) <span class="hljs-comment">// [ 3000, 2000 ] 3001</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">方法三</h5>
<p><strong>generator，yield</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> startTime = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ajax</span>(<span class="hljs-params">time, cb</span>) </span>&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> cb(time), time)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">time</span>) </span>&#123;
  ajax(time, <span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    it.next(data);
  &#125;)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> request1 = request(<span class="hljs-number">3000</span>);
  <span class="hljs-keyword">let</span> request2 = request(<span class="hljs-number">2000</span>);
  <span class="hljs-keyword">let</span> res1 = <span class="hljs-keyword">yield</span> request1
  <span class="hljs-keyword">let</span> res2 = <span class="hljs-keyword">yield</span> request2
  <span class="hljs-built_in">console</span>.log(res1, res2, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() - startTime) <span class="hljs-comment">// 2000 3000 3001</span>
&#125;
<span class="hljs-keyword">let</span> it = main();
it.next();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个地方有点问题，<code>因为request2耗时较短，会先返回，</code>也就是先执行it.next(2000)，<code>导致res1获得了request2的返回值</code>
若使用co函数，则不会存在这个问题，因为co是在promise.then函数中才执行it.next()，相当于it.next()是链式调用</p>
<p><strong>generator使用co函数</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> co = <span class="hljs-built_in">require</span>(<span class="hljs-string">'co'</span>)
<span class="hljs-keyword">const</span> startTime = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span> (<span class="hljs-params">time</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(time)
    &#125;, time)
  &#125;)
&#125;
co(<span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> request1 = request(<span class="hljs-number">3000</span>);
  <span class="hljs-keyword">let</span> request2 = request(<span class="hljs-number">2000</span>);
  <span class="hljs-keyword">let</span> res1 = <span class="hljs-keyword">yield</span> request1
  <span class="hljs-keyword">let</span> res2 = <span class="hljs-keyword">yield</span> request2
  <span class="hljs-built_in">console</span>.log(res1, res2, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() - startTime) <span class="hljs-comment">// 3000 2000 3001</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了co函数，就不需要生成it和执行next方法了；
co的原理其实也简单，就是递归执行next，直到done为true；
如果next返回的value是Promise，则在then函数中执行next，若不是Promise，直接执行next函数
下面是co函数的简版手写实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">co</span>(<span class="hljs-params">func</span>) </span>&#123;
  <span class="hljs-keyword">let</span> it = func()
  <span class="hljs-keyword">let</span> t = it.next()
  next()
  
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (t.done) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">if</span> (t.value <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) &#123;
      t.value.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        t = it.next(res)
        next()
      &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123;
      t = it.next(t.value)
      next()
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">方法四</h5>
<p>有了generator，很容易想到async/await，毕竟async/await就是由generator实现的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// setTimeout模拟异步请求，time为请求耗时</span>
<span class="hljs-keyword">const</span> startTime = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span> (<span class="hljs-params">time</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(time)
    &#125;, time)
  &#125;)
&#125;
(<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> request1 = request(<span class="hljs-number">3000</span>)
  <span class="hljs-keyword">let</span> request2 = request(<span class="hljs-number">2000</span>)
  <span class="hljs-keyword">let</span> res1 = <span class="hljs-keyword">await</span> request1
  <span class="hljs-built_in">console</span>.log(res1, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() - startTime)<span class="hljs-comment">// 3000 3001</span>
  <span class="hljs-keyword">let</span> res2 = <span class="hljs-keyword">await</span> request2
  <span class="hljs-built_in">console</span>.log(res2, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() - startTime) <span class="hljs-comment">// 2000 3005</span>
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            