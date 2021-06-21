
---
title: 'Cesium是如何实现多线程的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5509'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 19:24:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=5509'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><p>这是我参与更文挑战的第9天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>。</p>
<h3 data-id="heading-0">Web Worker</h3>
<h4 data-id="heading-1">背景</h4>
<p>众所周知，JavaScript是单线程模型，所有的任务只能在同一条线程上进行完成，前边的任务未完成则后续任务只能等待，所以在H中引入了Web Worker，为JavaScript创建一个多线程的环境，将部分任务提供给它在后台运行，前台后台同时运行。</p>
<p>Web Worker是后台运行的JavaScript，它独立于其他脚本且不会影响页面的性能。引入Web Worker的好处是一些计算密集型或高延迟的任务，被 Web Worker 线程所处理，主线程就会很流畅，不会被阻塞或拖慢，而此时 Web Worker 在后台运行。但是这也正是 Web Worker 比较耗费资源的原因。</p>
<h4 data-id="heading-2">浏览器支持及使用</h4>
<p>除了IE外所有主流浏览器均支持Web Worker。</p>
<p>可在创建Worker之前检测是否支持</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span>(Worker)!==<span class="hljs-string">"undefined"</span>) &#123;
    <span class="hljs-comment">// 支持.....</span>
&#125;
<span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 不支持..</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Web Worker在一个独立的线程中运行，所以代码需要放在一个单独的文件中。加载时如果存在指定文件，浏览器会在文件下载完毕后执行，生成新的Worker线程，如果加载文件失败不会有任何提示。</p>
<p>创建Worker后利用<code>postMessage()</code>启动</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> worker = <span class="hljs-keyword">new</span> Worker(<span class="hljs-string">'worker.js'</span>);
<span class="hljs-keyword">var</span> info = <span class="hljs-string">'start worker!'</span>
worker.postMessage(info);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在Worker中使用<code>onmessge</code>事件接收主线程的消息来实现一些操作。</p>
<pre><code class="hljs language-js copyable" lang="js">onmessage = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-keyword">var</span> data = e.data
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样的，从Worker发消息到主线程也采用同样方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Receive the message from the main thread</span>
onmessage = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-keyword">var</span> info = e.data;
    <span class="hljs-keyword">var</span> result = info + <span class="hljs-string">' get'</span>;
    postMessage(result);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>可以使用<code>addEventListener</code>来替换<code>onmessage</code></p>
</blockquote>
<p>停止Worker有两种方法，在主线程中调用<code>worker.terminate()</code>或在内部调用<code>self.close()</code>均可。在任务结束后一定要停止，因为Worker会一直在后台运行耗费资源，不应该过度使用。</p>
<h4 data-id="heading-3">注意事项</h4>
<ul>
<li>主线程与Worker之间传递的消息不是共享的，因为系统将消息对象传递给Worker后会将其序列化，在另一端再取消序列化。大部分浏览器通过JSON的编码解码实现。</li>
<li>Worker的self和this都是Worker的全局作用域。</li>
<li>Worker无法处理DOM，无法使用window对象、document对象等。</li>
<li>Worker可以生成子Worker,但需要注意：子Worker必须和父线程处在相同origin中，其中的URI应相对于父Worker位置解析。</li>
</ul>
<h3 data-id="heading-4">Cesium的异步＋多线程</h3>
<p>Cesium中涉及到大量三维球计算和大数据量交互，比如三角网，参数化Geometry等，都是在Worker中实现的，参数的传递以及不同类型对应的不同算法。</p>
<p>Cesium源码中<code>Source\Core\TaskProcessor.js</code>内为Cesium封装的Worker。我们简单来看一下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">TaskProcessor</span>(<span class="hljs-params">workerPath, maximumActiveTasks</span>) </span>&#123;
    <span class="hljs-built_in">this</span>._workerPath = <span class="hljs-keyword">new</span> Uri(workerPath).isAbsolute()
        ? workerPath
    : TaskProcessor._workerModulePrefix + workerPath;
    <span class="hljs-built_in">this</span>._maximumActiveTasks = defaultValue(
        maximumActiveTasks,
        <span class="hljs-built_in">Number</span>.POSITIVE_INFINITY
    );
    <span class="hljs-built_in">this</span>._activeTasks = <span class="hljs-number">0</span>;
    <span class="hljs-built_in">this</span>._deferreds = &#123;&#125;;
    <span class="hljs-built_in">this</span>._nextID = <span class="hljs-number">0</span>;
&#125;


TaskProcessor.prototype.scheduleTask = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">
parameters,
 transferableObjects
</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!defined(<span class="hljs-built_in">this</span>._worker)) &#123;
        <span class="hljs-built_in">this</span>._worker = createWorker(<span class="hljs-built_in">this</span>);
    &#125;

    <span class="hljs-comment">// ……</span>


    <span class="hljs-keyword">return</span> when(canTransferArrayBuffer(), <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">canTransferArrayBuffer</span>) </span>&#123;
        <span class="hljs-comment">// ……</span>

        <span class="hljs-keyword">return</span> deferred.promise;
    &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们使用时只需要创建一个TaskProcessor，指定类型，然后调用scheduleTask，接收对应具体参数，然后返回一个Promise对象，我们可以异步的获取的对应结果。</p>
<p>使用方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> taskProcessor = <span class="hljs-keyword">new</span> Cesium.TaskProcessor(<span class="hljs-string">'myWorkerPath'</span>);
<span class="hljs-keyword">var</span> promise = taskProcessor.scheduleTask(&#123;
    <span class="hljs-attr">someParameter</span> : <span class="hljs-literal">true</span>,
    <span class="hljs-attr">another</span> : <span class="hljs-string">'hello'</span>
&#125;);
<span class="hljs-keyword">if</span> (!Cesium.defined(promise)) &#123;
    <span class="hljs-comment">// too many active tasks - try again later</span>
&#125; <span class="hljs-keyword">else</span> &#123;
    Cesium.when(promise, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">result</span>) </span>&#123;
        <span class="hljs-comment">// use the result of the task</span>
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            