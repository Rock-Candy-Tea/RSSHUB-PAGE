
---
title: 'JS-async 和 await'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4453'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 20:48:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=4453'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">概述</h2>
<p><strong>async/await 是 promise 的语法糖</strong>，友情链接：<a href="https://juejin.cn/post/6981721700031266852" target="_blank" title="https://juejin.cn/post/6981721700031266852">Promise</a>，每次我们使用 await, 解释器都创建一个 promise 对象，然后把剩下的 async 函数中的操作放到 then 回调函数中。也就是说，除了await后面紧跟着的相当于Promise内部的代码外，async后的代码都相当于Promise.then中的代码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> () => &#123;
  a = a + <span class="hljs-number">1</span>;
  <span class="hljs-keyword">await</span> fn();
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'2'</span>, a) ;&#125;
  <span class="hljs-comment">// =======相当于======> </span>
  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">()=></span>&#123;
     fn()
     &#125;).then(<span class="hljs-function">()=></span>&#123;
       a = a + <span class="hljs-number">1</span>;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'2'</span>, a);
       &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>async/await</strong> 相比直接使用Promise来说：</p>
<p><strong>优势</strong>在于处理 then 的调用链，能够更清晰准确的写出代码。</p>
<p><strong>缺点</strong>在于滥用 await可能会导致性能问题，因为await会阻塞代码，也许之后的异步代码并不依赖于前者，但仍然需要等待前者完成，导致代码失去了并发性。</p>
<p>非主要：1.在没有await的情况下执行async函数，它会立即执行，返回一个Promise对象，并且，绝不会阻塞后面的语句。2.在await内部实现了generators，generators会保留await之前堆栈中的东西</p>
<h2 data-id="heading-1">示例</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">0</span>
<span class="hljs-keyword">var</span> b = <span class="hljs-keyword">async</span> () => &#123;
  a = a + <span class="hljs-keyword">await</span> <span class="hljs-number">10</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'2'</span>, a) <span class="hljs-comment">// -> '2' 10</span>
  a = (<span class="hljs-keyword">await</span> <span class="hljs-number">10</span>) + a
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'3'</span>, a) <span class="hljs-comment">// -> '3' 20</span>
&#125;
b()
a++
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>, a) <span class="hljs-comment">// -> '1' 1</span>
输出：<span class="hljs-number">1</span> <span class="hljs-number">1</span> <span class="hljs-number">2</span> <span class="hljs-number">10</span> <span class="hljs-number">3</span> <span class="hljs-number">20</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于以上代码你可能会有疑惑，这里可以先看下<a href="https://juejin.cn/post/6983868300140740615" target="_blank" title="https://juejin.cn/post/6983868300140740615">Eventloop的相关说明</a>，说明下原理</p>
<p>首先函数 b 先执行，在执行到 await 10 之前变量 a 还是 0，因为在 await 内部实现了 generators ，generators 会保留堆栈中东西，所以这时候 a = 0 被保存了下来
因为 await 是异步操作，遇到await就会立即返回一个pending状态的Promise对象，暂时返回执行代码的控制权，使得函数外的代码得以继续执行，所以会先执行 console.log('1', a)
这时候同步代码执行完毕，开始执行异步代码，将保存下来的值拿出来使用，这时候 a = 10
然后后面就是常规执行代码了</p></div>  
</div>
            