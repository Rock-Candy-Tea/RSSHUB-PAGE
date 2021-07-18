
---
title: '浅谈 JavaScript_callback() 回调函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4213'
author: 掘金
comments: false
date: Fri, 16 Jul 2021 20:32:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=4213'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在<strong>MDN</strong>的文档中，对**callback()**的定义为：</p>
<p><em>被作为实参传入另一函数，并在该外部函数内被调用，用以来完成某些任务的函数，称为回调函数。</em></p>
<p><em>A callback is a function that is passed as an argument to another function and is executed after its parent function has completed.</em></p>
<h3 data-id="heading-0">1. 理解回调函数</h3>
<p><strong>调用过程</strong>：函数a的参数为函数b，当函数a执行完之后再去执行b</p>
<blockquote>
<p>或许，可以通俗地认为：做完函数a的事情，再去做函数b的事情</p>
</blockquote>
<p>再<strong>打个比方</strong>：</p>
<p>你去上学，妈妈送你去上学并叮嘱你要记得将缴费单交给老师。</p>
<p>此时，函数a为妈妈送你上学，函数b为你将缴费单交给老师。也就是你要做完函数a，才会去执行函数b。</p>
<p><strong>提个疑问</strong>:</p>
<p>Q：为什么不直接把整个事情在函数a中写好，而是要通过一个参数进行回调呢？</p>
<p>A：如果你直接写进去，<code>function a()&#123;...;b();&#125;</code>，那就直接写死了，失去了变量的灵活性。当你要传入别的函数时，需要重新写一遍函数a。</p>
<h3 data-id="heading-1">2. 代码展示</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params">callback</span>) </span>&#123;      
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"parent函数a！"</span>);   
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"调用回调函数"</span>);   
   callback(); <span class="hljs-comment">// 调用回调函数</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"回调函数b"</span>); &#125;   

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">c</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"回调函数c"</span>); &#125;   
  
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123; a(b); a(c); &#125;

test();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3. 为什么需要回调</h3>
<p>JavaScript 在浏览器中运行，浏览器的主进程是<strong>单线程事件循环</strong>。如果我们尝试在单线程事件循环中，执行长时间运行的操作，则会阻止该过程。</p>
<p>JavaScript 是按从上到下的顺序运行代码。在有些情况下，<strong>必须在某些情况发生之后</strong>，代码才能运行，这就不是按顺序运行了。这是异步编程。</p>
<p>回调函数确保：函数在某个任务完成之前不运行，在任务完成之后立即运行。它帮助我们编写异步 JavaScript 代码，避免问题和错误。</p>
<p>在 JavaScript 里创建回调函数的方法是：将它作为参数传递给另一个函数，然后当某个任务完成之后，立即调用它。</p>
<h3 data-id="heading-3">4.  Javascript 回调地狱</h3>
<p>当多个异步函数一个接一个地执行时，会产生<strong>回调地狱</strong>。它也被称为<strong>厄运金字塔</strong>。</p>
<p>代码变得更加难以理解，以及难以维护和修改。这是由回调函数的嵌套而引发的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> p_client = <span class="hljs-keyword">new</span> Db(<span class="hljs-string">'integration_tests_20'</span>, <span class="hljs-keyword">new</span> Server(<span class="hljs-string">"127.0.0.1"</span>, <span class="hljs-number">27017</span>, &#123;&#125;), &#123;<span class="hljs-string">'pk'</span>:CustomPKFactory&#125;);
   p_client.open(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, p_client</span>) </span>&#123;
       p_client.dropDatabase(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, done</span>) </span>&#123;
           p_client.createCollection(<span class="hljs-string">'test_custom_key'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, collection</span>) </span>&#123;
               collection.insert(&#123;<span class="hljs-string">'a'</span>:<span class="hljs-number">1</span>&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, docs</span>) </span>&#123;
                   collection.find(&#123;<span class="hljs-string">'_id'</span>:<span class="hljs-keyword">new</span> ObjectID(<span class="hljs-string">"aaaaaaaaaaaa"</span>)&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, cursor</span>) </span>&#123;
                       cursor.toArray(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, items</span>) </span>&#123;
                           test.assertEquals(<span class="hljs-number">1</span>, items.length);
 
                           <span class="hljs-comment">// Let's close the db</span>
                           p_client.close();
                       &#125;);
                   &#125;);
               &#125;);
           &#125;);
       &#125;);
   &#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>↑ 就如上面的代码</p>
<h3 data-id="heading-4">5. 如何避免回调地狱？</h3>
<ol>
<li>使用promise</li>
<li>借助 async-await</li>
<li>使用 async.js 库</li>
</ol>
<blockquote>
<p>这里就不细讲了</p>
</blockquote>
<h3 data-id="heading-5">6. 优点和使用场景</h3>
<p><strong>用一句话概括：在直接调用函数A()时，把另一个函数B()作为参数，传入函数A()里面，以此来通过函数A()间接调用函数B()。</strong></p>
<p><strong>优点</strong></p>
<ul>
<li>
<p>DRY，避免重复代码</p>
</li>
<li>
<p>可以将通用的逻辑抽象</p>
</li>
<li>
<p>加强代码可维护性</p>
</li>
<li>
<p>加强代码可读性</p>
</li>
<li>
<p>分离专职的函数</p>
</li>
</ul>
<p><strong>使用场景</strong></p>
<ul>
<li>异步执行(例如读文件，发送HTTP请求)</li>
<li>事件监听和处理</li>
<li>设置超时和时间间隔的方法</li>
<li>通用化：代码简洁</li>
</ul>
<p>一篇关于callback()的好文：[<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000021942060" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000021942060" ref="nofollow noopener noreferrer">从零起步，真正理解Javascript回调函数</a>](<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000021942060" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000021942060" ref="nofollow noopener noreferrer">segmentfault.com/a/119000002…</a>)</p></div>  
</div>
            