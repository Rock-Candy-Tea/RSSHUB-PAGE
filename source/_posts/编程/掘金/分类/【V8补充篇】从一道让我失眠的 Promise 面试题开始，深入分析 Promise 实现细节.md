
---
title: '【V8补充篇】从一道让我失眠的 Promise 面试题开始，深入分析 Promise 实现细节'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d16b84f7e1aa4d878fb982c9931552f6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 19:50:40 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d16b84f7e1aa4d878fb982c9931552f6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>罪魁祸首还是先挂出来</strong> 👇</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">4</span>);
&#125;).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res)
&#125;)

<span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>);
&#125;).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>);
&#125;).then(<span class="hljs-function">() =></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">6</span>);
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接上篇 👉 <a href="https://juejin.cn/post/6945319439772434469" target="_blank">从一道让我失眠的 Promise 面试题开始，深入分析 Promise 实现细节</a></p>
<p>手写 Promise 完整代码 👉 <a href="https://github.com/T-Roc/my-promise" target="_blank" rel="nofollow noopener noreferrer">github:my-promise</a></p>
<h2 data-id="heading-0">问题回顾</h2>
<p>上篇我们通过从零手写 Promise 的方式，带着大家去深入了解了一下 Promise 的一些实现细节。</p>
<p>最后我们发现其实只需要创建一次微任务，就可以处理 then 方法内部 <code>return Promise.resolve(4)</code> 的问题，所以我们没有办法在手写 Promise 实现中去找到到合理的解释，只能通过一些概念进行了猜测。</p>
<p>没有真正窥探到原生 Promise 的内部实现逻辑，似乎让人感觉有点隔靴搔痒 🙈</p>
<p>虽然一次还是两次微任务对我们实际生产也没有什么实质影响，创建两次微任务的代码逻辑也可能会在后续的某次迭代中被改掉。</p>
<p>但是我们不能不面对新的疑问：</p>
<ul>
<li><strong>原生 Promise 是不是真的产生了两次微任务来处理 return Promise.resolve(4)？</strong></li>
<li><strong>Promise V8 源码中有没有关键信息可以解释这个现象？</strong></li>
</ul>
<p>本着刨根问题对精神，还是决定做一下 Promise V8 源码内容补充,也算是对 V8 源码学习的一次启蒙。</p>
<h2 data-id="heading-1">Promise V8 源码如何阅读？</h2>
<p>废话不多说，来开始看源码 👉 <a href="https://chromium.googlesource.com/v8/v8.git/+/refs/heads/9.0-lkgr/src/builtins/promise-then.tq" target="_blank" rel="nofollow noopener noreferrer">源码地址</a>，注释内容来自我们<a href="https://tc39.es/ecma262/#sec-promise.prototype.then" target="_blank" rel="nofollow noopener noreferrer">ECMAScript® 2022</a> 规范。</p>
<p>你可能会看的脑壳疼 😂 更糟糕的是 Promise 的实现逻辑是实际上分布在不同的代码块中的，直接吃生肉很容易消化不良。</p>
<p>所以这里先推荐两篇 Promise V8源码分析文章（PS：我尝过，是熟的）：</p>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/264944183" target="_blank" rel="nofollow noopener noreferrer">Promise V8 源码分析(一)</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/329201628" target="_blank" rel="nofollow noopener noreferrer">Promise V8 源码分析(二)</a></li>
</ul>
<p>在大致熟悉 Promise V8 源码的之后，我们再回到之前的问题 👇</p>
<h2 data-id="heading-2">原生 Promise 是不是真的产生了两次微任务？</h2>
<p>在 Promise V8 源码中通过 <a href="https://chromium.googlesource.com/v8/v8.git/+/refs/heads/9.0-lkgr/src/builtins/builtins-microtask-queue-gen.cc#115" target="_blank" rel="nofollow noopener noreferrer">RunSingleMicrotask</a> 运行一个微任务。如果想要了解微任务的创建情况，就可以通过在RunSingleMicrotask 打印调用信息来观察。</p>
<p>我们来看一下在运行那道面试题时，RunSingleMicrotask 中打印的信息，图片来自知乎@徐鹏跃</p>
<p><img alt="v2-20dd94a382c3d43928dac616eb895498_720w.jpg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d16b84f7e1aa4d878fb982c9931552f6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>用红框圈出的信息，就是那两次神秘的微任务，<strong>所以我们这里我们就可以确认，确实是创建了两次微任务</strong>。</p>
<h2 data-id="heading-3">Promise V8 源码中关键信息在哪里？</h2>
<p>实际上我们通过<a href="https://juejin.cn/post/6945319439772434469" target="_blank">上一篇</a>的分析，我们知道有一次微任务创建的位置是很清晰的。那就是在发现 onFufilled 回调函数执行结果是一个 Promise 的时候，它会调用一次 then 方法去处理这种情况，调用 then 方法那就必然会使用 queueMicrotask 创建一次微任务。</p>
<p>先看一下面试题中这个 Promise</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">4</span>);
&#125;).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再来回顾一下上一篇中是如何处理 return Promise.resolve(4) 的 👇</p>
<ol>
<li>Promise.resolve() 执行，修改 Promise 状态为 fulfilled;</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 更改成功后的状态</span>
resolve = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
  <span class="hljs-comment">// 只有状态是等待，才执行状态修改</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PENDING) &#123;
    <span class="hljs-comment">// 状态修改为成功</span>
    <span class="hljs-built_in">this</span>.status = FULFILLED;
    <span class="hljs-comment">// 保存成功之后的值</span>
    <span class="hljs-built_in">this</span>.value = value;
    <span class="hljs-comment">// resolve里面将所有成功的回调拿出来执行</span>
    <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.onFulfilledCallbacks.length) &#123;
      <span class="hljs-comment">// Array.shift() 取出数组第一个元素，然后（）调用，shift不是纯函数，取出后，数组将失去该元素，直到数组为空</span>
      <span class="hljs-built_in">this</span>.onFulfilledCallbacks.shift()(value)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>then 初始化的时候，在这之前 Promise.resolve() 已经修改状态为 fulfilled，所以这里会立即通过 queueMicrotask 创建微任务将 onFulfilled 回调函数送入微任务队列；</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// onFulfilled 回调函数</span>
onFulfilled = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">4</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建一个微任务等待 promise2 完成初始化</span>
queueMicrotask(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// 获取成功回调函数的执行结果</span>
    <span class="hljs-keyword">const</span> x = realOnFulfilled(<span class="hljs-built_in">this</span>.value);
    <span class="hljs-comment">// 传入 resolvePromise 集中处理</span>
    resolvePromise(promise2, x, resolve, reject);
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    reject(error)
  &#125; 
&#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在 then 全部初始化完成后，同步代码执行结束，开始执行微任务列表中排队的任务，onFulfilled 回调函数此时会被调用，onFulfilled 函数的执行结果 x 会传入 resolvePromise 方法进行处理，此时 x 为 Promise.resolve(4) ；</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 获取成功回调函数的执行结果</span>
<span class="hljs-keyword">const</span> x = realOnFulfilled(<span class="hljs-built_in">this</span>.value);
<span class="hljs-comment">// 传入 resolvePromise 集中处理</span>
resolvePromise(promise2, x, resolve, reject);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>判断返回值 x 的类型，如果 <code>typeof x === object</code> 或者 <code>typeof x === function</code> ，同时判断 <code>x.then</code> 存在，此时 x 为 Promise.resolve(4)，符合上面的条件，则调用 then 方法（<strong>这里就会创建一次微任务</strong>），得到结果 y 继续调用  resolvePromise 递归判断，这里 y = 4，即不为 Promise, 调用  <code>resolve(4)</code> ，注意这里的resolve 方法是外部 Promise 的，相当于将 Promise.resolve(4) 的执行状态与结果提供给外部的 Promise，完整代码是这样 👇</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">promise, x, resolve, reject</span>) </span>&#123;
  <span class="hljs-comment">// 如果相等了，说明return的是自己，抛出类型错误并返回</span>
  <span class="hljs-keyword">if</span> (promise === x) &#123;
    <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'The promise and the return value are the same'</span>));
  &#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'object'</span> || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-comment">// x 为 null 直接返回，走后面的逻辑会报错</span>
    <span class="hljs-keyword">if</span> (x === <span class="hljs-literal">null</span>) &#123;
      <span class="hljs-keyword">return</span> resolve(x);
    &#125;

    <span class="hljs-keyword">let</span> then;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// 把 x.then 赋值给 then </span>
      then = x.then;
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-comment">// 如果取 x.then 的值时抛出错误 error ，则以 error 为据因拒绝 promise</span>
      <span class="hljs-keyword">return</span> reject(error);
    &#125;

    <span class="hljs-comment">// 如果 then 是函数</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> then === <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-keyword">let</span> called = <span class="hljs-literal">false</span>;
      <span class="hljs-keyword">try</span> &#123;
        then.call(
          x, <span class="hljs-comment">// this 指向 x</span>
          <span class="hljs-comment">// 如果 resolvePromise 以值 y 为参数被调用，则运行 [[Resolve]](promise, y)</span>
          <span class="hljs-function"><span class="hljs-params">y</span> =></span> &#123;
            <span class="hljs-comment">// 如果 resolvePromise 和 rejectPromise 均被调用，</span>
            <span class="hljs-comment">// 或者被同一参数调用了多次，则优先采用首次调用并忽略剩下的调用</span>
            <span class="hljs-comment">// 实现这条需要前面加一个变量 called</span>
            <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;
            called = <span class="hljs-literal">true</span>;
            resolvePromise(promise, y, resolve, reject);
          &#125;,
          <span class="hljs-comment">// 如果 rejectPromise 以据因 r 为参数被调用，则以据因 r 拒绝 promise</span>
          <span class="hljs-function"><span class="hljs-params">r</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;
            called = <span class="hljs-literal">true</span>;
            reject(r);
          &#125;);
      &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        <span class="hljs-comment">// 如果调用 then 方法抛出了异常 error：</span>
        <span class="hljs-comment">// 如果 resolvePromise 或 rejectPromise 已经被调用，直接返回</span>
        <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;

        <span class="hljs-comment">// 否则以 error 为据因拒绝 promise</span>
        reject(error);
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 如果 then 不是函数，以 x 为参数执行 promise</span>
      resolve(x);
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 如果 x 不为对象或者函数，以 x 为参数执行 promise</span>
    resolve(x);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过对手写 Promise 回顾，我们知道在处理 Promise.resolve(4)的时候，调用了 then 方法，来修改状态并拿到 Promise 的结果，这里也就创建了一次微任务。回过来我们再看一下在原生 Promise 中是怎么处理的。</p>
<p>实际上在 Promise V8 源码中也有类似上面的 resolvePromise 的处理，在 <a href="https://chromium.googlesource.com/v8/v8.git/+/refs/heads/9.0-lkgr/src/builtins/promise-resolve.tq#88" target="_blank" rel="nofollow noopener noreferrer">ResolvePromise</a> 方法中 👇</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-comment">// https://tc39.es/ecma262/#sec-promise-resolve-functions</span>
<span class="hljs-function">transitioning builtin
<span class="hljs-title">ResolvePromise</span><span class="hljs-params">(implicit context: Context)</span><span class="hljs-params">(
    promise: JSPromise, resolution: JSAny)</span>: JSAny </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// 8. If Type(resolution) is not Object, then</span>
    <span class="hljs-comment">// 8.a Return FulfillPromise(promise, resolution).</span>
    
    <span class="hljs-comment">// 如果 resolution 是整数/字符串</span>
    <span class="hljs-keyword">if</span> (TaggedIsSmi(resolution)) &#123;      
      <span class="hljs-comment">// FulfillPromise 把 promise 状态变为 fulfilled 状态</span>
      <span class="hljs-keyword">return</span> FulfillPromise(promise, resolution);
    &#125;
    <span class="hljs-keyword">const</span> promisePrototype =
        *NativeContextSlot(ContextSlot::PROMISE_PROTOTYPE_INDEX);
        
    <span class="hljs-comment">// 判断 resolution 的类型是否为 Promise</span>
    <span class="hljs-keyword">if</span> (resolutionMap.prototype == promisePrototype) &#123;
      <span class="hljs-comment">// The &#123;resolution&#125; is a native Promise in this case.</span>
      then = *NativeContextSlot(ContextSlot::PROMISE_THEN_INDEX);
      <span class="hljs-comment">// Check that Torque load elimination works.</span>
      <span class="hljs-keyword">static_assert</span>(nativeContext == LoadNativeContext(context));
      <span class="hljs-keyword">goto</span> Enqueue;
    &#125;
  &#125; label Enqueue &#123;
    <span class="hljs-comment">// 13. Let job be NewPromiseResolveThenableJob(promise, resolution,</span>
    
    <span class="hljs-comment">// 代码逻辑与规范一致，把 NewPromiseResolveThenableJob 送入微任务队列</span>
    <span class="hljs-keyword">const</span> task = NewPromiseResolveThenableJobTask(
        promise, UnsafeCast<JSReceiver>(resolution),
        UnsafeCast<Callable>(then));
    <span class="hljs-comment">// 14. Perform HostEnqueuePromiseJob(job.[[Job]], job.[[Realm]]).</span>
    <span class="hljs-comment">// 15. Return undefined.</span>
    
    <span class="hljs-comment">// 插入 microtask 队列</span>
    <span class="hljs-keyword">return</span> EnqueueMicrotask(task.context, task);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <code>resolutionMap.prototype == promisePrototype</code> 判断是否为 Promise，发现 onFulfilled 执行结果是一个 Promise 的时候，会创建 NewPromiseResolveThenableJob 并插入 microtask 队列中。<strong>这里实际上就是与我们手写代码存在差异的地方，也是多出的一次微任务创建的位置</strong>。在 <a href="https://tc39.es/ecma262/#sec-newpromiseresolvethenablejob" target="_blank" rel="nofollow noopener noreferrer">ECMAScript® 2022</a> 中也有说明这一块的规范 👇</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/482bf665bebe441e939181652c6705cd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28a5b3b5807e42aa9ed4c2af5727d5b6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>接着，我们看一下 <a href="https://chromium.googlesource.com/v8/v8.git/+/refs/heads/9.0-lkgr/src/builtins/promise-jobs.tq#13" target="_blank" rel="nofollow noopener noreferrer">PromiseResolveThenableJob</a> 里面到底是做了什么 👇</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-comment">// https://tc39.es/ecma262/#sec-promiseresolvethenablejob</span>
<span class="hljs-function">transitioning builtin
<span class="hljs-title">PromiseResolveThenableJob</span><span class="hljs-params">(implicit context: Context)</span><span class="hljs-params">(
    promiseToResolve: JSPromise, thenable: JSReceiver, then: JSAny)</span>: JSAny </span>&#123;
  <span class="hljs-keyword">const</span> nativeContext = LoadNativeContext(context);
  <span class="hljs-keyword">const</span> promiseThen = *NativeContextSlot(ContextSlot::PROMISE_THEN_INDEX);
  <span class="hljs-keyword">const</span> thenableMap = thenable.<span class="hljs-built_in">map</span>;
  <span class="hljs-keyword">if</span> (TaggedEqual(then, promiseThen) && IsJSPromiseMap(thenableMap) &&
      !IsPromiseHookEnabledOrDebugIsActiveOrHasAsyncEventDelegate() &&
      IsPromiseSpeciesLookupChainIntact(nativeContext, thenableMap)) &#123;
      
    <span class="hljs-comment">// PerformPromiseThen 方法也是 JS Promise then 方法的底层调用</span>
    <span class="hljs-keyword">return</span> PerformPromiseThen(
        UnsafeCast<JSPromise>(thenable), UndefinedConstant(),
        UndefinedConstant(), promiseToResolve);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">const</span> funcs =
        CreatePromiseResolvingFunctions(promiseToResolve, False, nativeContext);
    <span class="hljs-keyword">const</span> resolve = funcs.resolve;
    <span class="hljs-keyword">const</span> reject = funcs.reject;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">return</span> Call(
          context, UnsafeCast<Callable>(then), thenable, resolve, reject);
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-keyword">return</span> Call(context, UnsafeCast<Callable>(reject), Undefined, e);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>PerformPromiseThen 方法实际上也是 Promise then 方法的底层核心方法，在 <a href="https://tc39.es/ecma262/#sec-newpromiseresolvethenablejob" target="_blank" rel="nofollow noopener noreferrer">ECMAScript® 2022</a> 中我们可以看到 👇</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6eb6e6143a8b41c39214bd08661611fc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们看一下 Promise then 的 源码 👇</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function">transitioning javascript builtin
<span class="hljs-title">PromisePrototypeThen</span><span class="hljs-params">(js-implicit context: NativeContext, receiver: JSAny)</span><span class="hljs-params">(
    onFulfilled: JSAny, onRejected: JSAny)</span>: JSAny </span>&#123;
  <span class="hljs-comment">// 1. Let promise be the this value.</span>
  <span class="hljs-comment">// 2. If IsPromise(promise) is false, throw a TypeError exception.</span>
  <span class="hljs-keyword">const</span> promise = Cast<JSPromise>(receiver) otherwise ThrowTypeError(
      MessageTemplate::kIncompatibleMethodReceiver, <span class="hljs-string">'Promise.prototype.then'</span>,
      receiver);

  <span class="hljs-comment">// 3. Let C be ? SpeciesConstructor(promise, %Promise%).</span>
  <span class="hljs-keyword">const</span> promiseFun = UnsafeCast<JSFunction>(
      context[NativeContextSlot::PROMISE_FUNCTION_INDEX]);

  <span class="hljs-comment">// 4. Let resultCapability be ? NewPromiseCapability(C).</span>
  let resultPromiseOrCapability: JSPromise|PromiseCapability;
  let resultPromise: JSAny;
  label AllocateAndInit &#123;
    <span class="hljs-keyword">const</span> resultJSPromise = NewJSPromise(promise);
    resultPromiseOrCapability = resultJSPromise;
    resultPromise = resultJSPromise;
  &#125;
  <span class="hljs-comment">// onFulfilled 和 onRejected 是 then 接收的两个参数</span>
  <span class="hljs-keyword">const</span> onFulfilled = CastOrDefault<Callable>(onFulfilled, Undefined);
  <span class="hljs-keyword">const</span> onRejected = CastOrDefault<Callable>(onRejected, Undefined);

  <span class="hljs-comment">// 5. Return PerformPromiseThen(promise, onFulfilled, onRejected,</span>
  <span class="hljs-comment">//    resultCapability).</span>
  <span class="hljs-comment">// 这里是上面 ECMAScript 截图中对应的第5点，Return PerformPromiseThen</span>
  PerformPromiseThenImpl(
      promise, onFulfilled, onRejected, resultPromiseOrCapability);
  <span class="hljs-comment">// 返回一个新的 Promise</span>
  <span class="hljs-keyword">return</span> resultPromise;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来看一下 PerformPromiseThen 的源码 👇</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-comment">// https://tc39.es/ecma262/#sec-performpromisethen</span>
<span class="hljs-function">transitioning builtin
<span class="hljs-title">PerformPromiseThen</span><span class="hljs-params">(implicit context: Context)</span><span class="hljs-params">(
    promise: JSPromise, onFulfilled: Callable|Undefined,
    onRejected: Callable|Undefined, resultPromise: JSPromise|Undefined)</span>: JSAny </span>&#123;
    
  <span class="hljs-comment">// 调用 PerformPromiseThenImpl 方法</span>
  PerformPromiseThenImpl(promise, onFulfilled, onRejected, resultPromise);
  <span class="hljs-keyword">return</span> resultPromise;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比一下，我们发现他们实际上都是调用了 PerformPromiseThenImpl 方法来处理核心逻辑的，我们再看一下 <a href="https://chromium.googlesource.com/v8/v8.git/+/refs/heads/9.0-lkgr/src/builtins/promise-abstract-operations.tq#409" target="_blank" rel="nofollow noopener noreferrer">PerformPromiseThenImpl</a>中做了什么 👇</p>
<pre><code class="hljs language-js copyable" lang="js">transitioning macro PerformPromiseThenImpl(implicit context: Context)(
    promise: JSPromise, <span class="hljs-attr">onFulfilled</span>: Callable|Undefined,
    <span class="hljs-attr">onRejected</span>: Callable|Undefined,
    <span class="hljs-attr">resultPromiseOrCapability</span>: JSPromise|PromiseCapability|Undefined): <span class="hljs-keyword">void</span> &#123;
  <span class="hljs-keyword">if</span> (promise.Status() == PromiseState::kPending) &#123;
    <span class="hljs-comment">// pending 状态的分支</span>
    <span class="hljs-comment">// The &#123;promise&#125; is still in "Pending" state, so we just record a new</span>
    <span class="hljs-comment">// PromiseReaction holding both the onFulfilled and onRejected callbacks.</span>
    <span class="hljs-comment">// Once the &#123;promise&#125; is resolved we decide on the concrete handler to</span>
    <span class="hljs-comment">// push onto the microtask queue.</span>
    <span class="hljs-keyword">const</span> handlerContext = ExtractHandlerContext(onFulfilled, onRejected);
    <span class="hljs-comment">// 拿到 Promise 的 reactions_or_result 字段</span>
    <span class="hljs-keyword">const</span> promiseReactions =
        UnsafeCast<(Zero | PromiseReaction)>(promise.reactions_or_result);
    <span class="hljs-comment">// 考虑一个 Promise 可能会有多个 then 的情况，reaction 是个链表</span>
    <span class="hljs-comment">// 存储 Promise then 中传入的回调函数</span>
    <span class="hljs-keyword">const</span> reaction = NewPromiseReaction(
        handlerContext, promiseReactions, resultPromiseOrCapability,
        onFulfilled, onRejected);
    <span class="hljs-comment">// reactions_or_result 可以存 Promise 的处理函数，也可以存</span>
    <span class="hljs-comment">// Promise 的最终结果，因为现在 Promise 处于 pending 状态，</span>
    <span class="hljs-comment">// 所以存的是处理函数 reaction</span>
    promise.reactions_or_result = reaction;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// fulfilled 和 rejected 状态的分支</span>
    <span class="hljs-keyword">const</span> reactionsOrResult = promise.reactions_or_result;
    <span class="hljs-keyword">let</span> microtask: PromiseReactionJobTask;
    <span class="hljs-keyword">let</span> handlerContext: Context;
    <span class="hljs-keyword">if</span> (promise.Status() == PromiseState::kFulfilled) &#123;
      handlerContext = ExtractHandlerContext(onFulfilled, onRejected);
      microtask = NewPromiseFulfillReactionJobTask(
          handlerContext, reactionsOrResult, onFulfilled,
          resultPromiseOrCapability);
    &#125; <span class="hljs-keyword">else</span>
      deferred &#123;
        assert(promise.Status() == PromiseState::kRejected);
        handlerContext = ExtractHandlerContext(onRejected, onFulfilled);
        microtask = NewPromiseRejectReactionJobTask(
            handlerContext, reactionsOrResult, onRejected,
            resultPromiseOrCapability);
        <span class="hljs-keyword">if</span> (!promise.HasHandler()) &#123;
          <span class="hljs-attr">runtime</span>::PromiseRevokeReject(promise);
        &#125;
      &#125;
    
    <span class="hljs-comment">// fulfilled 和 rejected 状态时，将 onRejected onFulfilled 放入微任务队列</span>
    <span class="hljs-comment">// 等待执行</span>
    EnqueueMicrotask(handlerContext, microtask);
  &#125;
  promise.SetHasHandler();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们再次看到了熟悉的 EnqueueMicrotask()，它的出现意味着又有新的微任务被创建，这个与我们手写 Promise 实现中的处理逻辑基本一致，也就是 then 调用时所创建的那次微任务。</p>
<p>所以这里我们总结一下<strong>原生 Promise 创建两次微任务的位置</strong>：</p>
<ol>
<li>发现 Promise.resolve(4) 的时候，创建 NewPromiseResolveThenableJob，并将其送入微任务队列（与手写有差异）；</li>
<li>处理 Promise.resolve(4) 的时候，调用 then 方法时，内部创建了微任务来处理回调函数（与手写类似）；</li>
</ol>
<h2 data-id="heading-4">写在最后</h2>
<p>首先特别感谢<a href="https://www.zhihu.com/people/kan-a-79" target="_blank" rel="nofollow noopener noreferrer">知乎@徐鹏跃</a> 在 Promise V8 源码解析这块提供的支持，为文章提供了很多关键信息。</p>
<p>另外关于这道面试题，我也创建了知乎问题，得到了很多非常棒的回答，也推荐大家去看看 <a href="https://www.zhihu.com/question/453677175" target="_blank" rel="nofollow noopener noreferrer">promise.then 中 return Promise.resolve 后，发生了什么？</a></p>
<p>参考资料：</p>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/264944183" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/264944183</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/329201628" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/329201628</a></li>
<li><a href="https://tc39.es/ecma262/" target="_blank" rel="nofollow noopener noreferrer">tc39.es/ecma262/</a></li>
<li><a href="https://chromium.googlesource.com/v8/v8.git/+/refs/heads/9.0-lkgr/src/" target="_blank" rel="nofollow noopener noreferrer">chromium.googlesource.com/v8/v8.git/+…</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            