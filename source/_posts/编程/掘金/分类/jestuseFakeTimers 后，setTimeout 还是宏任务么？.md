
---
title: 'jest.useFakeTimers 后，setTimeout 还是宏任务么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6998'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 06:17:34 GMT
thumbnail: 'https://picsum.photos/400/300?random=6998'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>开篇先提一个问题：<code>jest.useFakeTimers</code> 后，<code>setTimeout</code> 还是宏任务么？</p>
<h1 data-id="heading-0">业务场景</h1>
<p>业务上有一个需求，需要对若干主机进行连通性测试来选择一个响应时长最短的作为最优节点，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">"axios"</span>;

<span class="hljs-comment">/**
 * 获取一组主机地址中响应时长最短的节点
 *
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Array<string>&#125;</span> </span>hosts 主机域名加端口号数组
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Promise<string>&#125;</span> </span>响应时长最短的节点地址
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getFatestHost</span>(<span class="hljs-params">hosts</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    hosts.forEach(<span class="hljs-function">(<span class="hljs-params">host</span>) =></span> axios.get(<span class="hljs-string">`http://<span class="hljs-subst">$&#123;host&#125;</span>/api/v1/ping`</span>).then(<span class="hljs-function">() =></span> resolve(host)));
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">单元测试</h1>
<p>可以看到，代码并不复杂。接下来就是，对这样一项功能如何去做单元测试呢？我们可以劫持 <code>axios.get</code> 方法，然后通过 <code>setTimeout</code> 方法来模拟不同时长的响应，并基于预设的响应时长对 <code>getFastestHost</code> 的返回结果做断言。我们设定第一次 axios 请求耗时 20ms，第二次请求耗时 10ms，期望返回结果是耗时 10ms 的主机地址，整体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; getFatestHost &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./index.js"</span>;
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">"axios"</span>;

test(<span class="hljs-string">"test getFatestHost"</span>, <span class="hljs-function">() =></span> &#123;
  jest
    .spyOn(axios, <span class="hljs-string">"get"</span>)
    .mockReturnValueOnce(
      <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          resolve(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">200</span> &#125;);
        &#125;, <span class="hljs-number">20</span>);
      &#125;)
    )
    .mockReturnValueOnce(
      <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          resolve(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">200</span> &#125;);
        &#125;, <span class="hljs-number">10</span>);
      &#125;)
    );
  <span class="hljs-keyword">const</span> hostsArr = [<span class="hljs-string">"192.168.0.1:80"</span>, <span class="hljs-string">"192.168.0.2:80"</span>];
  <span class="hljs-keyword">return</span> expect(getFatestHost(hostsArr)).resolves.toBe(hostsArr[<span class="hljs-number">1</span>]);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里代码的执行逻辑如下：</p>
<ol>
<li>执行所有的同步代码，依次发送 axios ping 请求，该请求实际被 jest 的 mock 函数劫持，并产生两个 setTimeout 宏任务</li>
<li>10 ms 后第一个宏任务触发，并在宏任务执行过程中产生两个 promise.then 微任务</li>
<li>宏任务执行完成，resolve axios.get 微任务，然后 resolve getFatestHost 的 Promise 返回</li>
<li>返回 host 结果，测试结束。</li>
</ol>
<p>这一过程由于两个 setTimeout 都是宏任务，所以即使中间没有 10ms 的时间间隔，也会在执行完 10ms setTimeout 所建立的一系列微任务之后才会执行 20ms 的宏任务，这就使得测试用例结果和预期是一致的。</p>
<p>单元测试用例是跑通了，但是却不是最理想的解决方案，因为 <code>setTimeout</code> 的引入使得我们的测试变得低效。不过 jest 为我们提供了控制时间流转的办法，比如 <code>jest.runAllTimers()</code> 就可以让我们将时间快进以迅速完成所有的计时器，更准确来说，是完成所有的宏任务和微任务。</p>
<blockquote>
<p>Exhausts both the macro-task queue (i.e., all tasks queued by setTimeout(), setInterval(), and setImmediate()) and the micro-task queue (usually interfaced in node via process.nextTick).</p>
</blockquote>
<p>基于此我们来对单元测试用例进行一次改造：</p>
<pre><code class="hljs language-diff copyable" lang="diff">import &#123; getFatestHost &#125; from "./index.js";
import axios from "axios";

test("test getFatestHost", () => &#123;
<span class="hljs-addition">+ jest.useFakeTimers();</span>
  jest
    .spyOn(axios, "get")
    .mockReturnValueOnce(
      new Promise((resolve) => &#123;
        setTimeout(() => &#123;
          resolve(&#123; status: 200 &#125;);
        &#125;, 20);
      &#125;)
    )
    .mockReturnValueOnce(
      new Promise((resolve) => &#123;
        setTimeout(() => &#123;
          resolve(&#123; status: 200 &#125;);
        &#125;, 10);
      &#125;)
    );
<span class="hljs-addition">+ jest.runAllTimers();</span>
  const hostsArr = ["192.168.0.1:80", "192.168.0.2:80"];
  return expect(getFatestHost(hostsArr)).resolves.toBe(hostsArr[1]);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果这一次测试用例却失败了，看起来代码逻辑似乎没什么问题，仅仅是用 jest 对 setTimeout 进行了加速，就导致了不同的返回结果。</p>
<pre><code class="copyable">Expected: "192.168.0.2:80"
Received: "192.168.0.1:80"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们添加上打印信息来探究一下代码执行的顺序：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.spec.js</span>
test(<span class="hljs-string">"test getFatestHost"</span>, <span class="hljs-function">() =></span> &#123;
  jest.useFakeTimers();

  jest
    .spyOn(axios, <span class="hljs-string">"get"</span>)
    .mockReturnValueOnce(
      <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Promise1.created"</span>);
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"setTimeout 20ms "</span>);  <span class="hljs-comment">// 2</span>
          resolve(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">200</span>, <span class="hljs-attr">data</span>: <span class="hljs-string">"setTimeout 20ms"</span> &#125;);
        &#125;, <span class="hljs-number">20</span>);
      &#125;)
    )
    .mockReturnValueOnce(
      <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Promise2.created"</span>);
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"setTimeout 10ms "</span>);  <span class="hljs-comment">// 1</span>
          resolve(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">200</span>, <span class="hljs-attr">data</span>: <span class="hljs-string">"setTimeout 10ms"</span> &#125;);
        &#125;, <span class="hljs-number">10</span>);
      &#125;)
    );
  
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"before jest.RunAllTimers"</span>);
  jest.runAllTimers();
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"after jest.RunAllTimers"</span>);
  
  <span class="hljs-keyword">const</span> hostsArr = [<span class="hljs-string">"192.168.0.1:80"</span>, <span class="hljs-string">"192.168.0.2:80"</span>];
  <span class="hljs-keyword">return</span> expect(getFatestHost(hostsArr)).resolves.toBe(hostsArr[<span class="hljs-number">1</span>]);
&#125;);

<span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getFatestHost</span>(<span class="hljs-params">hosts</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    hosts.forEach(<span class="hljs-function">(<span class="hljs-params">host</span>) =></span>
      axios.get(<span class="hljs-string">`http://<span class="hljs-subst">$&#123;host&#125;</span>/api/v1/ping`</span>).then(<span class="hljs-function">(<span class="hljs-params">&#123; data &#125;</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;host&#125;</span> ping resolved: `</span>, data);  <span class="hljs-comment">// 3、4</span>
        resolve(host);
      &#125;)
    );
  &#125;);
&#125;

<span class="hljs-comment">// 打印顺序：</span>
<span class="hljs-comment">// Promise1.created</span>
<span class="hljs-comment">// Promise2.created</span>
<span class="hljs-comment">// before jest.RunAllTimers</span>
<span class="hljs-comment">// setTimeout 10ms</span>
<span class="hljs-comment">// setTimeout 20ms</span>
<span class="hljs-comment">// after jest.RunAllTimers</span>
<span class="hljs-comment">// 192.168.0.1:80 ping resolved：setTimeout 20ms</span>
<span class="hljs-comment">// 192.168.0.2:80 ping resolved：setTimeout 10ms</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里就发现了很多细节：</p>
<ol>
<li><code>Promise.created</code> 先于 <code>jest.RunAllTimers</code>，说明 <code>jest.mock</code> 在创建的时候就立即执行了回调函数，而不是在回调函数触发的时候才执行。</li>
<li><code>setTimeout</code> 函数在 <code>jestRunAllTimers</code> 的时候全部打印出来了，说明 <code>jest.useFakerTimers</code> 把 <code>setTimeout</code> 从异步的宏任务执行变成了同步执行，而 <code>setTimeout</code> 的延迟时间只是决定了同步代码执行的顺序。</li>
<li>调用 <code>getFatestHost</code> 的时候，<code>setTimeout</code> 以及执行完了，axios.get 会立即返回一个 resolved 的 promise，所以这个时候 promise.then 的执行顺序就只取决于 Promise 的创建时间，而不是 resolve 的时间了。</li>
</ol>
<p>这样就完整的解释了测试用例失败的奇怪原因。</p>
<p>说到这里我们先来简单复习一下事件循环：</p>
<p>js 执行完同步代码之后，会先查看微任务队列，并依次执行到队列为空，然后再取出一个宏任务进行执行，执行过程中如果产生了新的微任务，那么会在宏任务执行完之后继续执行微任务直到微任务队列为空，如此循环往复。</p>
<p>对于本文所涉及到的，需要了解：<code>setTimeout</code> 是宏任务，而 <code>Promise.then</code> 是微任务。</p>
<h1 data-id="heading-2">解决方案</h1>
<p>接下来回到正题，我们应该如何改造测试用例使得能够正确的测试业务代码呢？这里有两个思路：</p>
<p>第一个思路：还原真实场景，快进到第一个 setTimeout，模拟一个请求响应而另外一个请求尚未响应的情景，这里 jest 为我们提供了 advanceTimersToNextTimer 方法用于实现只快进到下一个 timer，代码改造如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; getFatestHost &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./index.js"</span>;
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">"axios"</span>;

test(<span class="hljs-string">"test getFatestHost"</span>, <span class="hljs-function">() =></span> &#123;
  jest.useFakeTimers();  
jest
    .spyOn(axios, <span class="hljs-string">"get"</span>)
    .mockReturnValueOnce(
      <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          resolve(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">200</span> &#125;);
        &#125;, <span class="hljs-number">20</span>);
      &#125;)
    )
    .mockReturnValueOnce(
      <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> 
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          resolve(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">200</span> &#125;);
        &#125;, <span class="hljs-number">10</span>);
      &#125;)
    );

  jest.advanceTimersToNextTimer();
  <span class="hljs-keyword">const</span> hostsArr = [<span class="hljs-string">"192.168.0.1:80"</span>, <span class="hljs-string">"192.168.0.2:80"</span>];
  <span class="hljs-keyword">return</span> expect(getFatestHost(hostsArr)).resolves.toBe(hostsArr[<span class="hljs-number">1</span>]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二个思路：同时完成两个请求的模拟响应，但是这里要注意避免同步代码先于业务代码执行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; getFatestHost &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./index.js"</span>;
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">"axios"</span>;

test(<span class="hljs-string">"test getFatestHost"</span>, <span class="hljs-function">() =></span> &#123;
  jest.useFakeTimers();  
jest
    .spyOn(axios, <span class="hljs-string">"get"</span>)
    .mockReturnValueOnce(
      <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          resolve(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">200</span> &#125;);
        &#125;, <span class="hljs-number">20</span>);
      &#125;)
    )
    .mockReturnValueOnce(
      <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> 
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          resolve(&#123; <span class="hljs-attr">status</span>: <span class="hljs-number">200</span> &#125;);
        &#125;, <span class="hljs-number">10</span>);
      &#125;)
    );

  <span class="hljs-keyword">const</span> hostsArr = [<span class="hljs-string">"192.168.0.1:80"</span>, <span class="hljs-string">"192.168.0.2:80"</span>];
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    getFatestHost(hostsArr).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
      expect(res).toBe(hostsArr[<span class="hljs-number">1</span>]);
      resolve();
    &#125;);
    jest.runAllTimers();
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的情况之所以复杂，主要在于：</p>
<ol>
<li>在同一个测试用例里同时混杂了微任务、宏任务的执行逻辑，需要对 event loop 有深刻的认知才能捋清楚代码的执行顺序。</li>
<li><strong>jest 中将 setTimeout 从宏任务变成了同步代码</strong>，仅仅是发现这一点就花费了挺大精力</li>
<li><strong>jest mock 回调函数的执行时间是创建时而不是触发时</strong>，这一点也与正常的逻辑思维有所偏差</li>
</ol></div>  
</div>
            