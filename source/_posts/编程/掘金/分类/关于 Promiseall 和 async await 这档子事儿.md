
---
title: '关于 Promise.all 和 async await 这档子事儿'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b40cd77ce7d47f686a45f24c1b01dbd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 01:41:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b40cd77ce7d47f686a45f24c1b01dbd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文章主要是对比两者之间使用<code>Promise</code>返回的异步函数的区别。</p>
<p>🌰 计算一下执行时间<br>
例子1：所有<code>异步函数</code>均为成功</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promise1</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span>=></span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            resolve()
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"promise1"</span>);
        &#125;,<span class="hljs-number">1000</span>)
    &#125;)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promise2</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span>=></span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            resolve();
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"promise2"</span>);
        &#125;,<span class="hljs-number">2000</span>)
    &#125;)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promise3</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span>=></span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            resolve();
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"promise3"</span>);
        &#125;,<span class="hljs-number">3000</span>)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例子2：
修改第一个<code>promise1</code>函数为失败。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promise1</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            reject(<span class="hljs-string">"error"</span>)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"promise1"</span>);
        &#125;,<span class="hljs-number">1000</span>)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">使用Promise.all</h2>
<p>如果我们使用 <code>Promise.all</code> 来执行 <code>例子1</code> 所有的异步函数，并计算时间</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.time(<span class="hljs-string">"test"</span>);
<span class="hljs-built_in">Promise</span>.all([promise1(),promise2(),promise3()]).then(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"promise.all执行完毕"</span>);
    <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">"test"</span>);
&#125;).catch(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"promise.all执行失败"</span>);
    <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">"test"</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们会得到如下的执行时间：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b40cd77ce7d47f686a45f24c1b01dbd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
omg，我的老天，这速度太快了。</p>
<p>可以看到<code>Promise.all</code> 会按顺序执行并且不会阻塞线程，而是等待所有异步执行完毕，结束整套执行。  并且会以执行的完成最慢的异步<code>promise3</code>函数作为结束。很明显这是一组全部执行并且正常回调的异步<code>Promise</code>函数。所以执行时间耗时 <code>3秒</code></p>
<p>接下来让我们看看这个 如果我们将第一个<code>promise1</code>函数修改为<code>reject</code>的回调，会如何执行呢？
代码见<code>例子2</code></p>
<p>我们会得到如下结果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9766b4eddf4746b3af1733a4b9f60524~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>Promise.all</code>这个小调皮居然直接执行自己自身的<code>catch</code>失败回调！然后执行了后续的异步函数,这是个感人的故事。。<br>
所以得出结论：<code>Promise.all</code> 如果遇到失败会立刻执行自身的<code>catch</code>回调并且不会中断后续异步函数的执行。</p>
<p>但是值得需要注意的是，<code>Promise.all</code>只会抛出<code>多个异步函数中第一个执行失败的信息</code> 也就是所有异步<code>Promise</code>函数中第一个<code>reject</code>!</p>
<h2 data-id="heading-1">使用async await</h2>
<p>有如下代码调用顺序执行 <code>例子1</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncTime</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.time(<span class="hljs-string">"aysncTime"</span>);
    <span class="hljs-keyword">await</span> promise1();
    <span class="hljs-keyword">await</span> promise2();
    <span class="hljs-keyword">await</span> promise3();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"async 执行完毕"</span>);
    <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">"aysncTime"</span>);
&#125;    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会得到如下结果:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bda425f949140bfa7ce3b38fbeb48d8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个时候<code>async</code>就向大家展示了 什么叫"姐就是女王,自信放光芒”，不出意外的阻塞了线程，并且同步按顺序执行并返回。<br>
同样是等待所有异步执行完毕，并结束。只不过和<code>Promise.all</code>不同的是会单一执行一个异步函数并等到当前异步函数执行到<code>resolve</code>再继续下一异步函数。执行时长是<code>按照依次执行完毕的时间累计而成</code> <code>6秒</code></p>
<p>同样的接下来让我们看看这个 如果我们将第一个<code>promise1</code>函数修改为<code>reject</code>的回调，会如何执行呢？见<code>例子2</code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10ce717f53d145088c71594671f07d57~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到<code>会直接中断掉不会进行后续的异步函数执行</code>，并且中断线程，不愧是女王就是有脾气！</p>
<p>需要注意的是如果需要代码保护继续执行的话，可以加入<code>try...catch</code>来进行异常捕捉！
如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncTime</span>(<span class="hljs-params"></span>)</span>&#123;
   <span class="hljs-built_in">console</span>.time(<span class="hljs-string">"aysncTime"</span>);
   <span class="hljs-keyword">try</span>&#123;
       <span class="hljs-keyword">await</span> promise1();
       <span class="hljs-keyword">await</span> promise2();
       <span class="hljs-keyword">await</span> promise3();
       <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"async 执行完毕"</span>);
       <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">"aysncTime"</span>);
   &#125;<span class="hljs-keyword">catch</span> (e) &#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"async 执行失败"</span>);
       <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">"aysncTime"</span>);
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以正确得到代码保护的结果。虽然会中断剩余异步函数的执行，但是保护了整个线程不会中断！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/595c1fc38241473cbacd606271c423c1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">总结</h2>
<h3 data-id="heading-3">Promise.all</h3>
<p>1.异步执行多个异步函数，虽然按顺序执行，但是由于异步回调时间不固定的情况下并不能保证执行顺序。<br>
2.不会阻塞线程，只会在合适的时机调用整体<code>resolve|reject</code>的回调函数。<br>
3.遇到执行回调中第一个失败。会立刻执行自身的<code>reject</code>的回调函数，并且只会抛出第一个失败<code>reject</code>,后续遇到<code>reject</code>均不执行。<br>
4.不会因为异步函数的失败，而中断后续所有的异步函数执行。<br>
5.由于是异步执行所有<code>异步函数</code>,可以更快的捕获异常问题。</p>
<h3 data-id="heading-4">async await</h3>
<p>1.同步执行异步代码，按顺序执行，并阻塞线程保证执行顺序。<br>
2.会阻塞线程。<br>
3.遇到执行回调中第一个失败，报错如果不加<code>try...catch</code>会直接中断<code>线程</code><br>
4.依次执行保证指定顺序调用异步函数。<br>
5.简洁的使用语法糖。</p>
<p>由此以上总结的特性，可以封装成两个执行异步函数的请求集，用于加载显示百分比进度。<br>
学习总结如有错误，欢迎指正！</p></div>  
</div>
            