
---
title: '了解NodeJs中的多线程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0721547a789d452ca44f222c3b658751~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 23:10:15 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0721547a789d452ca44f222c3b658751~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第<code>5</code>天，活动详情查看：<strong><a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">Worker Threads</h2>
<p>node中的多线程是在node版本v10.5.0引入的一个的一个新特性，在很长一段时间内<code>Worker Thread</code>都是实验性质的，到目前为止，node稳定的版本已经到了14.17.4，这个特性已经变成<strong>稳定可用</strong>了。</p>
<h3 data-id="heading-1">worker_thread是什么</h3>
<p>先来来看看官网的描述</p>
<pre><code class="copyable">The `worker_threads` module enables the use of threads that
execute JavaScript in parallel.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>意思就是：<code>worker_thread</code>模块允许使用线程来<strong>并行</strong>执行JavaScript。</p>
<p>我们以前Javascript都是单线程然后利用一个事件循环队列(<code>event loop</code>)不断监听<code>执行栈</code>是否有函数进入。对于worker_thread，其实可以理解为一个<code>event loop</code>中有多个javascript工作线程，创建一个线程相当于创建一个新的js执行环境。多线程的运行如下图</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0721547a789d452ca44f222c3b658751~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">与child_process的区别</h3>
<p><code>child_process</code>是可以创建一个新的node进程，<code>worker_thread</code>与它的最大区别就是：<strong>worker_thread可以共享内存</strong>，公共的数据可以在线程之间公用，而child_process只能通过JSON去传递数据。</p>
<p>还有就是：因为线程是在一个进程内的，创建一个线程的<strong>开销</strong>会比创建一个进程要<strong>小</strong></p>
<h3 data-id="heading-3">worker_thread的适用范围</h3>
<p><code>worker_thread</code>在<strong>CPU密集型的JS操作</strong>中非常有用，但是在IO密集型操作中性能不会有太多的改善，反而Node自带的一步IO操作会比工作线程更有用。</p>
<h2 data-id="heading-4">使用worker_thread</h2>
<p>介绍完worker_thread的概念，现在来介绍一下他的用法</p>
<h3 data-id="heading-5">创建工作线程</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; isMainThread, Worker, parentPort &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'worker_threads'</span>);

<span class="hljs-keyword">if</span> (isMainThread) &#123;
  createChildThread();
&#125; <span class="hljs-keyword">else</span> &#123;
  parentPort.on(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'parent thread listen:'</span>, msg);
  &#125;)
  parentPort.postMessage(<span class="hljs-string">'hello child thread'</span>)
  
&#125;

<span class="hljs-comment">// 创建线程方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createChildThread</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> worker = <span class="hljs-keyword">new</span> Worker(__filename)
  worker.on(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'child thread listen:'</span>, val);
    worker.postMessage(<span class="hljs-string">'hello parent thread'</span>);
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码在<strong>主线程</strong>的时候调用创建工作线程的方法，创建一个工作线程并且新增一个，而创建工作线程后调用主线程的端口向工作线程发送消息，工作线程接受到消息后再向主线程回应。大概的流程图如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9de637732d9e490bacde8c1ee5919f68~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行后返回</p>
<p>创建线程前
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d74d14094c94dc6a962fdaa35e1cc88~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建线程后，线程数量+1
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ff4d25fab214e03aad66df31536a412~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43f42225ce9c4bd49917896821af218b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">线程间通信</h2>
<p>上文提到，<code>worker_threads</code>可以通过<code>ArrayBuffer</code>或<code>SharedArrayBuffer</code>共享内存。接下来看一下，它在代码中是如何实现的.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; isMainThread, Worker, parentPort &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'worker_threads'</span>);

<span class="hljs-keyword">if</span> (isMainThread) &#123;
  createChildThread();
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 创建一个长度为4byte的SharedArrayBuffer</span>
  <span class="hljs-keyword">const</span> shareBuf = <span class="hljs-keyword">new</span> SharedArrayBuffer(<span class="hljs-number">4</span>);
  <span class="hljs-comment">// 创建一个8位无符号整型数组</span>
  <span class="hljs-keyword">const</span> bufInt = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(shareBuf);
  parentPort.on(<span class="hljs-string">'message'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'parent thread listen:'</span>, bufInt);
  &#125;);
  <span class="hljs-comment">// 发送共享内存创建的整型</span>
  parentPort.postMessage(&#123; bufInt &#125;);
&#125;

<span class="hljs-comment">// 创建线程方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createChildThread</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> worker = <span class="hljs-keyword">new</span> Worker(__filename);
  worker.on(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">&#123; bufInt &#125;</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'child thread listen:'</span>, bufInt);
    bufInt[<span class="hljs-number">0</span>] = <span class="hljs-number">11</span>;
    worker.postMessage(<span class="hljs-string">'finished'</span>);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行后返回，可以看到在子线程创建一个<code>SharedArrayBuffer</code>，用主线程广播的一个数据，在子线程中接收后赋值，因为是线程间共享的Buffer，所以主线程这边也可以看到在子线程中修改的数据。<br>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58653d9b171841b6a75547e1f8c05919~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图所示，使用<code>SharedArrayBuffer</code>创建的值会分配到共享内存中，所有线程都可以共用这块内存。<br>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5c4febc17c04102b948c7330a434248~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">线程间通信</h3>
<p>我们已经学会<strong>创建线程</strong>和<strong>使用共享内存</strong>了，从上面代码可以看到，线程都是从主线程中发送消息，然后子线程向主线程回复消息，没有办法让两个子线程直接直接通信，如果我想让两个子线程<strong>直接通信</strong>，那就需要用到<code>MessageChannel</code>这个类了，<code>MessageChannel</code>的具体用法可以点击<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMessageChannel" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel" ref="nofollow noopener noreferrer">这里</a>。现在就来实现一下子线程之间的直接通信。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123;
  isMainThread,
  Worker,
  parentPort,
  MessageChannel,
  threadId,
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'worker_threads'</span>);

<span class="hljs-keyword">if</span> (isMainThread) &#123;
  createChildThread();
&#125; <span class="hljs-keyword">else</span> &#123;
  parentPort.on(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">&#123; port &#125;</span>) =></span> &#123;
    <span class="hljs-comment">// 主线程接收到端口后配置通信端口方法</span>
    port.on(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`port<span class="hljs-subst">$&#123;threadId&#125;</span> listen:`</span>, msg);
    &#125;);
    port.postMessage(<span class="hljs-string">`hello, im thread <span class="hljs-subst">$&#123;threadId&#125;</span>`</span>);
  &#125;);
  parentPort.postMessage(<span class="hljs-string">'hello'</span>);
&#125;

<span class="hljs-comment">// 创建线程方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createChildThread</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; port1, port2 &#125; = <span class="hljs-keyword">new</span> MessageChannel(); <span class="hljs-comment">// 创建一个MessageChannel</span>
  <span class="hljs-keyword">const</span> worker1 = <span class="hljs-keyword">new</span> Worker(__filename); <span class="hljs-comment">// 创建子线程1</span>
  <span class="hljs-keyword">const</span> worker2 = <span class="hljs-keyword">new</span> Worker(__filename); <span class="hljs-comment">// 创建子线程2</span>
  worker2.postMessage(&#123; <span class="hljs-attr">port</span>: port1 &#125;, [port1]); <span class="hljs-comment">// 向主线程发送Channel的端口1</span>
  worker1.postMessage(&#123; <span class="hljs-attr">port</span>: port2 &#125;, [port2]); <span class="hljs-comment">// 向主线程发送Channel的端口1</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行代码后返回
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/939c747217804f82b241d743e82ceb97~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从代码实现可以看到，最终建立子线程直接通信的步骤还是在<strong>主线程的message事件中</strong>。建立通信的流程图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/185044e925fa480a8ac397de3506ee83~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">实战</h2>
<p>了解完线程的概念和用法，现在来实战一下：比如在数组中有100万条数据需要md5加密，对比一下使用工作线程和不使用工作线程的实现速度怎么样</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123;
  isMainThread,
  Worker,
  parentPort,
  threadId,
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'worker_threads'</span>);
<span class="hljs-keyword">const</span> &#123; createHash &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'crypto'</span>);

<span class="hljs-keyword">const</span> ARR_NUM = <span class="hljs-number">1000000</span>; <span class="hljs-comment">// 数组长度</span>
<span class="hljs-keyword">const</span> WORKER_NUM = <span class="hljs-number">1</span>; <span class="hljs-comment">// 线程数</span>
<span class="hljs-keyword">const</span> size = <span class="hljs-built_in">Math</span>.ceil(ARR_NUM / WORKER_NUM); <span class="hljs-comment">// 每个线程需要处理的数据量</span>

<span class="hljs-keyword">if</span> (isMainThread) &#123;
  createChildThread();
&#125; <span class="hljs-keyword">else</span> &#123;
  parentPort.on(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">&#123; status, index, startTime &#125;</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (index === WORKER_NUM) &#123;
      <span class="hljs-keyword">const</span> usedTime = <span class="hljs-built_in">Date</span>.now() - startTime;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`finish bussiness time: <span class="hljs-subst">$&#123;usedTime&#125;</span>ms`</span>);
      process.exit(threadId);
    &#125;
  &#125;);
  <span class="hljs-keyword">const</span> data = addHasCode(threadId, size, (threadId - <span class="hljs-number">1</span>) * size);
  <span class="hljs-comment">// 完成后</span>
  parentPort.postMessage(&#123;
    <span class="hljs-attr">business</span>: <span class="hljs-string">'finish work'</span>,
    data,
  &#125;);
&#125;

<span class="hljs-comment">// 创建线程方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createChildThread</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> finishNumBuf = <span class="hljs-keyword">new</span> SharedArrayBuffer(<span class="hljs-number">4</span>);
  <span class="hljs-keyword">let</span> finishNum = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(finishNumBuf);
  <span class="hljs-keyword">const</span> startTime = <span class="hljs-built_in">Date</span>.now();
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> x = <span class="hljs-number">0</span>; x < WORKER_NUM; x++) &#123;
    <span class="hljs-keyword">const</span> worker = <span class="hljs-keyword">new</span> Worker(__filename, &#123;&#125;);
    worker.on(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">&#123; business, data &#125;</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (business === <span class="hljs-string">'finish work'</span>) &#123;
        finishNum[<span class="hljs-number">0</span>]++;
        worker.postMessage(&#123;
          <span class="hljs-attr">status</span>: <span class="hljs-string">`finish worker <span class="hljs-subst">$&#123;x&#125;</span>`</span>,
          <span class="hljs-attr">index</span>: finishNum[<span class="hljs-number">0</span>],
          <span class="hljs-attr">startTime</span>: startTime,
          data,
        &#125;);
      &#125;
    &#125;);
  &#125;

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;WORKER_NUM&#125;</span> thread start working`</span>);
&#125;

<span class="hljs-comment">// 加密方法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addHasCode</span>(<span class="hljs-params">index, size, limit</span>) </span>&#123;
  <span class="hljs-keyword">const</span> result = [];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> x = limit, num = index * size; x < num; x++) &#123;
    result.push(createHash(<span class="hljs-string">'md5'</span>).update(<span class="hljs-string">'hello world'</span>).digest(<span class="hljs-string">'base64'</span>));
  &#125;
  <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>1</code>个线程计算，平均需要<code>2700ms</code>左右
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/270bd6ff5f924724ac077b3570c569b6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用<code>5</code>个线程计算，平均需要<code>2000ms</code>左右
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c7bb6b4fcd84b76ad179f76439f4da7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用<code>20</code>个线程计算，平均需要<code>2500ms</code>左右
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48bbca5d205047c88c37c04b791ebf33~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用<code>60</code>个线程计算，平均需要<code>3800ms</code>左右
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51505ec57d9e4bc5a0d0d9806e38a6a5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可见，<strong>线程不是越多越好</strong>，过多的线程可能会增加过多的系统开销，速度也不如单线程时候运行。</p>
<h2 data-id="heading-9">小结</h2>
<p>本文介绍了nodeJs中的<code>worker_threads</code>的概念，去多进程的区别，和它的优点。<br>
介绍了<code>worker_threads</code>是如何使用，共享内存，还有子线程之间的通信。<br>
最后用一个测试子进程的效率的例子说明<code>worker_threads</code>对比单线程运行。</p>
<p>若文章中有不严谨或出错的地方请在评论区域指出~</p>
<h2 data-id="heading-10">参考</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fdist%2Flatest-v14.x%2Fdocs%2Fapi%2Fworker_threads.html%23" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/dist/latest-v14.x/docs/api/worker_threads.html#" ref="nofollow noopener noreferrer">Worker Theread</a></li>
</ul></div>  
</div>
            