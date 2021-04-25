
---
title: '使用 AbortController 取消 Fetch 请求和事件监听'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c851e03976fd4332a9b71536935b49b1~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 18:38:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c851e03976fd4332a9b71536935b49b1~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>AbortController 是一个控制器对象，你可以通过 new 构造函数的形式返回一个 AbortSignal 对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> controller = <span class="hljs-keyword">new</span> AbortController();
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>它有一个方法 <code>abort()</code>，用于触发 <code>abort</code> 事件</li>
<li>和单个属性 <code>signal</code>，可以在该属性上设置 <code>abort</code> 事件监听</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">controller.signal.onabort = <span class="hljs-function">() =></span> &#123;&#125;;

controller.signal.addEventListener(<span class="hljs-string">"abort"</span>, <span class="hljs-function">() =></span> &#123;&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 <code>controller.abort()</code> 被调用时：</p>
<ul>
<li><code>controller.signal</code> 就会触发 <code>abort</code> 事件</li>
<li><code>controller.signal.aborted</code> 属性从 <code>false</code> 变为 <code>true</code></li>
</ul>
<p>了解前置知识后，看一下实际应用的场景。</p>
<h2 data-id="heading-1">取消 Fetch 请求</h2>
<p>在没有 Fetch API 之前，一般通过 <code>XMLHttpRequest</code> 来实现数据更新，当我们发出请求后想临时取消，可以调用 <code>XMLHttpRequest.abort()</code> 方法来终止该请求。</p>
<p>有了 AbortController，同样可以实现取消 Fetch 请求。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> controller = <span class="hljs-keyword">new</span> AbortController();
<span class="hljs-keyword">const</span> signal = controller.signal;

fetch(<span class="hljs-string">"/"</span>, &#123; signal &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(err); <span class="hljs-comment">// DOMException: The user aborted a request.</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"aborted:"</span>, signal.aborted); <span class="hljs-comment">// aborted: true</span>
&#125;);

controller.abort();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c851e03976fd4332a9b71536935b49b1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">移除事件监听</h2>
<p>以往，我们通过 <code>EventTarget.addEventListener()</code> 来为一个 DOM、document 或 window 添加事件监听。</p>
<p>它的函数签名如下：</p>
<pre><code class="hljs language-js copyable" lang="js">target.addEventListener(type, listener);
target.addEventListener(type, listener, options);
target.addEventListener(type, listener, useCapture);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>options 是一个可选参数对象，它包含了以下属性来决定事件触发的行为：</p>
<ul>
<li><code>capture: boolean</code>，如果是 true，表示 listener 会在指定 type 事件类型的 <strong>捕获</strong> 阶段触发。false 则为 <strong>冒泡</strong> 阶段</li>
<li><code>once: boolean</code>，表示 listener 在添加之后最多只调用一次。如果是 true， listener 会在其被调用之后自动移除</li>
<li><code>passive: boolean</code>，设置为 true 时，表示 listener 永远不会调用 preventDefault()，用于优化页面的滚动性能</li>
</ul>
<p>当不再需要事件监听时，调用 <code>EventTarget.removeEventListener()</code> 来移除事件监听，但要保证 <strong>参数和添加监听时是一致的</strong>，即 <code>type</code> 事件类型必须是同一字符串，<code>listener</code> 回调函数必须是同一个函数引用，<code>options</code> 对象必须属性相同。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> btn = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">"button"</span>)[<span class="hljs-number">0</span>];

btn.addEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"button clicked"</span>), &#123;
  <span class="hljs-attr">capture</span>: <span class="hljs-literal">true</span>,
&#125;);

<span class="hljs-comment">// Doesn't work, because has different callback functions</span>
btn.removeEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"button clicked"</span>), &#123;
  <span class="hljs-attr">capture</span>: <span class="hljs-literal">true</span>,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Chrome 88 发布时，添加了一个 <a href="https://www.chromestatus.com/feature/5658622220566528" target="_blank" rel="nofollow noopener noreferrer">AbortSignal in addEventListener</a> 的新特性，它允许 AbortController 实例的 <code>signal</code> 属性传入 <code>addEventListener()</code> 的 options 对象，一旦调用实例的 <code>abort()</code> 方法，就会移除对应的事件监听。</p>
<p>这意味着开发者摆脱了调用 <code>removeEventListener()</code> 时繁琐的参数困境，只需使用 <code>abort()</code> 方法，既减少了代码量，又一目了然。</p>
<p>下面的代码实现了 "click once" 的效果，实测（Chrome 90）运行成功。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> controller = <span class="hljs-keyword">new</span> AbortController();
<span class="hljs-keyword">const</span> signal = controller.signal;
<span class="hljs-keyword">const</span> btn = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">"button"</span>)[<span class="hljs-number">0</span>];

<span class="hljs-keyword">const</span> handle = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"button clicked"</span>);
  controller.abort();
&#125;;

btn.addEventListener(<span class="hljs-string">"click"</span>, handle, &#123;
  <span class="hljs-attr">capture</span>: <span class="hljs-literal">true</span>,
  signal,
&#125;);

<span class="hljs-comment">// equals to</span>
<span class="hljs-comment">// btn.addEventListener("click", handle, &#123; once: true &#125;);</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">其他应用场景</h2>
<h3 data-id="heading-4">取消定时器 - 初级版：</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timeout</span>(<span class="hljs-params">duration, signal</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> handle = <span class="hljs-built_in">setTimeout</span>(resolve, duration);
    signal.onabort = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">clearTimeout</span>(handle);
      reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"The timeout was aborted"</span>));
    &#125;;
  &#125;);
&#125;

<span class="hljs-keyword">const</span> controller = <span class="hljs-keyword">new</span> AbortController();

timeout(<span class="hljs-number">10000</span>, controller.signal).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err));

controller.abort();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">取消定时器 - 高级版：</h3>
<blockquote>
<p>需要 Node.js v16 的支持</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; <span class="hljs-built_in">setTimeout</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"timers/promises"</span>;

<span class="hljs-keyword">const</span> ac = <span class="hljs-keyword">new</span> AbortController();
<span class="hljs-keyword">const</span> signal = ac.signal;

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-number">1000</span>, <span class="hljs-string">"foobar"</span>, &#123; signal &#125;)
  .then(<span class="hljs-built_in">console</span>.log)
  .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (err.name === <span class="hljs-string">"AbortError"</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"The timeout was aborted"</span>);
  &#125;);

ac.abort();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Reference</h2>
<ul>
<li>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener" target="_blank" rel="nofollow noopener noreferrer">MDN - EventTarget.addEventListener()</a></p>
</li>
<li>
<p><a href="https://css-tricks.com/using-abortcontroller-as-an-alternative-for-removing-event-listeners/" target="_blank" rel="nofollow noopener noreferrer">CSS - TRICKS - Using AbortController as an Alternative for Removing Event Listeners</a></p>
</li>
<li>
<p><a href="https://dom.spec.whatwg.org/#interface-abortcontroller" target="_blank" rel="nofollow noopener noreferrer">WHATWG living standard - AbortController</a></p>
</li>
<li>
<p><a href="https://nodejs.org/api/timers.html#timers_cancelling_timers" target="_blank" rel="nofollow noopener noreferrer">nodejs - Cancelling timers</a></p>
</li>
</ul></div>  
</div>
            