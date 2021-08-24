
---
title: '使用 better-queue 管理复杂的任务'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9356'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 10:01:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=9356'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>队列，在数据结构中是一种线性表，其特性为必须从一端插入，然后从另一端删除数据。但笔者今天重点不是如何实现该数据结构，我们可以看一看如何借助队列管理复杂的任务。</p>
<p>队列在实际开发中应用的场景非常广泛。因为在一个复杂的系统中，总是会有一些非常耗时的处理。在这种时候开发者不能要求系统提供实时处理、实时响应的能力。这时候我们就可以通过队列来解决此类问题。</p>
<p>开发者可以不停地往队列塞入数据，并为其生成唯一值（进行跟踪），同时根据当前系统的处理能力不断的从队列取出数据进行业务处理，以此来减轻在同一时间内进行大量复杂业务处理，以便增强系统的处理能力。</p>
<p>服务端通常可以借助队列来进行异步处理、系统解耦、数据同步以及流量削峰。</p>
<p>如果需求较为简单，开发者可以直接借助数组来进行处理。对于较为复杂的需求，可以使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdiamondio%2Fbetter-queue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/diamondio/better-queue" ref="nofollow noopener noreferrer">better-queue</a> 来解决问题。</p>
<p>better-queue 进一步扩展了队列，让其有很多好用的功能。诸如：</p>
<ul>
<li>并行化处理</li>
<li>持久(和可扩展)存储</li>
<li>批处理</li>
<li>优先队列</li>
<li>合并、过滤任务</li>
<li>任务统计</li>
</ul>
<h2 data-id="heading-0">使用方法</h2>
<p>让我们开始看一看 better-queue 如何使用。</p>
<h3 data-id="heading-1">代码风格</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> BetterQueue <span class="hljs-keyword">from</span> <span class="hljs-string">"better-queue"</span>;

<span class="hljs-comment">// 创建队列并且提供任务处理的回调函数</span>
<span class="hljs-comment">// 当调用回调意味该数据已经从队列中删除</span>
<span class="hljs-comment">// 然后从队列中取出下一条数据继续处理</span>
<span class="hljs-keyword">const</span> q = <span class="hljs-keyword">new</span> BetterQueue(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">input, cb</span>) </span>&#123;
  <span class="hljs-comment">// 从队列中取出数据并进行处理...</span>
  <span class="hljs-keyword">const</span> result = <span class="hljs-string">'xxxx'</span>
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// 如果成功则调用回调并且返回结果</span>
    cb(<span class="hljs-literal">null</span>, result);
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-comment">// 否则返回错误</span>
    cb(err)
  &#125;
&#125;)

q.push(<span class="hljs-number">1</span>)
q.push(&#123;<span class="hljs-attr">x</span>: <span class="hljs-number">1</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到，该库的代码风格还是采用了 Node 早期版本的回调风格，如果在执行期间发生了错误，会把错误作为回调的第一个参数传递到回调函数中。类似于：</p>
<pre><code class="hljs language-ts copyable" lang="ts">fs.readFile(filePath, <span class="hljs-function">(<span class="hljs-params">err, data</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (err) &#123;
    <span class="hljs-built_in">console</span>.log(err)
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">队列生成与使用</h3>
<p>首先我们可以构建存储结构和请求的数据结构 Job。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 任务数据</span>
<span class="hljs-keyword">interface</span> Job<T> &#123;
  <span class="hljs-comment">// 任务的唯一值，唯一确定当前任务</span>
  <span class="hljs-attr">id</span>: <span class="hljs-built_in">string</span>;
  <span class="hljs-comment">// 当前任务的状态：等待中，已成功，已失败  </span>
  status: <span class="hljs-string">'waiting'</span> | <span class="hljs-string">'succeeded'</span> | <span class="hljs-string">'failed'</span>;
  <span class="hljs-comment">// 任务的请求参数，可以是 id，也可以是其他数据</span>
  queryArgs?: <span class="hljs-built_in">any</span>;
  <span class="hljs-comment">// 任务的返回结果</span>
  result: T;
  <span class="hljs-comment">// 任务错误信息</span>
  err: <span class="hljs-built_in">Error</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后开发队列的回调函数以及新建任务队列:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 异步处理逻辑</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncProcess</span><<span class="hljs-title">T</span>>(<span class="hljs-params">job: Job<T>, cb: <span class="hljs-built_in">Function</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> req = job.queryArgs || job.id
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// await 异步请求处理，数据库访问，或者生成文件等耗时任务</span>
    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> query(<span class="hljs-string">'/xxx/xxx'</span>, req)
    cb(<span class="hljs-literal">null</span>, result)
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    <span class="hljs-comment">// 生成错误</span>
    cb(error)
  &#125;
&#125;

<span class="hljs-comment">// 创建队列</span>
<span class="hljs-keyword">const</span> betterQueue = <span class="hljs-keyword">new</span> BetterQueue(asyncProcess)

<span class="hljs-comment">// 对象存储，因为队列只会进行任务处理，并不包括数据的存储</span>
<span class="hljs-comment">// 也可以使用 map</span>
<span class="hljs-keyword">const</span> jobById = &#123;&#125;

<span class="hljs-comment">// 创建队列数据</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++) &#123;
  <span class="hljs-comment">// 建立 job</span>
  <span class="hljs-keyword">const</span> asyncJob: Job = &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;id&#125;</span>`</span>,
    <span class="hljs-attr">queryArgs</span>: &#123;&#125;,
    <span class="hljs-attr">status</span>: <span class="hljs-string">'waiting'</span>
  &#125;
  <span class="hljs-comment">// 存储 job,通过 id 追踪数据</span>
  jobById[asyncJob.id] = asyncJob

  betterQueue.push(asyncJob)
    <span class="hljs-comment">// 取出数据并且完成请求后调用 cb(null, result) 会进入这里</span>
    .on(<span class="hljs-string">'finish'</span>, <span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
      <span class="hljs-comment">// 修改任务状态，并存储任务结果</span>
      job.status = <span class="hljs-string">'succeeded'</span>
      job.result = result
    &#125;)
    <span class="hljs-comment">// 失败调用 cb(err) 会进入这里 </span>
    .on(<span class="hljs-string">'failed'</span>, <span class="hljs-function">(<span class="hljs-params">error: <span class="hljs-built_in">Error</span></span>) =></span> &#123;
      <span class="hljs-comment">// 修改任务状态，并存储错误信息</span>
      job.status = <span class="hljs-string">'failed'</span>
      job.err = error
    &#125;)
&#125;

<span class="hljs-comment">// 获取任务，如果队列没有处理，会返回 wait 状态</span>
<span class="hljs-comment">// 队列已经处理，会返回 succeeded 或者 failed</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getJob</span>(<span class="hljs-params">id: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> jobById[id]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在存储完任务之后，我们可以在前端或者服务端根据 id 来获取整个任务信息。</p>
<h3 data-id="heading-3">并发处理</h3>
<p>此时任务队列就会一个接一个进行业务处理，在上一个异步任务完成（成功或者失败）后进行下一个任务。但这样就太慢了。同时也没有发挥出系统应有的处理能力。这时候我们可以直接添加配置项 concurrent。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 创建队列</span>
<span class="hljs-keyword">const</span> betterQueue = <span class="hljs-keyword">new</span> BetterQueue(asyncProcess, &#123;
  <span class="hljs-attr">concurrent</span>: <span class="hljs-number">10</span>
&#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的话，系统可以依次且同时处理多条任务。大大减少了所有任务的处理时长。</p>
<h3 data-id="heading-4">任务状态</h3>
<p>我们还可以通过 getStats() 获取当前任务状态，这是 getStats 返回的信息：</p>
<pre><code class="hljs language-ts copyable" lang="ts"> <span class="hljs-keyword">interface</span> QueueStats &#123;
  <span class="hljs-attr">total</span>: <span class="hljs-built_in">number</span>; <span class="hljs-comment">// 处理的任务总数</span>
  average: <span class="hljs-built_in">number</span>; <span class="hljs-comment">// 平均处理时间</span>
  successRate: <span class="hljs-built_in">number</span>; <span class="hljs-comment">// 成功率，在 0 和 1 之间 </span>
  peak: <span class="hljs-built_in">number</span>; <span class="hljs-comment">// 大多数任务在任何给定时间点排队</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cb</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 获取当前队列的状态并打印完成数据对比。</span>
  <span class="hljs-comment">// 如: 1/10 2/10</span>
  <span class="hljs-keyword">const</span> stats = betterQueue.getStats()
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;stats.total&#125;</span>/10000`</span>)
&#125;

betterQueue.push(asyncJob)
  .on(<span class="hljs-string">'finish'</span>, <span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-comment">// 完成时候进行回调</span>
    cb()
  &#125;)
  .on(<span class="hljs-string">'failed'</span>, <span class="hljs-function">(<span class="hljs-params">error: <span class="hljs-built_in">Error</span></span>) =></span> &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-comment">// 完成时候进行回调</span>
    cb()
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候我们可以借助 getStats 向前端展示当前任务状态。</p>
<h3 data-id="heading-5">队列控制</h3>
<p>better-queue 提供了强大的队列控制能力。</p>
<p>我们可以通过任务 id 直接取消某一个任务。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 直接取消任务</span>
betterQueue.cancel(jobId)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还可以通过 cancelIfRunning 设置为 true 来控制之前队列中之前的任务取消。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 创建队列</span>
<span class="hljs-keyword">const</span> betterQueue = <span class="hljs-keyword">new</span> BetterQueue(asyncProcess, &#123;
  <span class="hljs-attr">cancelIfRunning</span>: <span class="hljs-literal">true</span>
&#125;)

betterQueue.push(&#123;<span class="hljs-attr">id</span>: <span class="hljs-string">'xxx'</span>&#125;);
<span class="hljs-comment">// 如果之前的 id 在队列中，取消前一个任务，执行后一个任务</span>
betterQueue.push(&#123;<span class="hljs-attr">id</span>: <span class="hljs-string">'xxx'</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以轻松控制队列暂停、恢复以及销毁。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 暂停队列运行</span>
betterQueue.pause()

<span class="hljs-comment">// 恢复队列运行</span>
betterQueue.resume()

<span class="hljs-comment">// 销毁队列，清理数据</span>
betterQueue.destroy()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，开发者也可以通过新建队列的回调函数中传出一个对象来自行控制。如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> betterQueue = <span class="hljs-keyword">new</span> BetterQueue(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">file: File, cb: <span class="hljs-built_in">Function</span></span>) </span>&#123;

  <span class="hljs-keyword">var</span> worker = someLongProcess(file);

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">cancel</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// 取消文件上传</span>
    &#125;,
    <span class="hljs-attr">pause</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// 暂停文件处理</span>
    &#125;,
    <span class="hljs-attr">resume</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// 恢复文件上传</span>
    &#125;
  &#125;
&#125;)
betterQueue.push(<span class="hljs-string">'/path/to/file.pdf'</span>)
betterQueue.pause()
betterQueue.resume()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">重试与超时</h3>
<p>对于异步任务来说，如果出现了执行失败，better-queue 也提供了重试机制。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> betterQueue = <span class="hljs-keyword">new</span> BetterQueue(asyncProcess, &#123;
  <span class="hljs-comment">// 当前任务失败了可以重新请求，最大为 10 次，超过 10 次宣告任务失败</span>
  <span class="hljs-attr">maxRetries</span>: <span class="hljs-number">10</span>,
  <span class="hljs-comment">// 重试等待时间 1s</span>
  <span class="hljs-attr">retryDelay</span>: <span class="hljs-number">1000</span>,
  <span class="hljs-comment">// 超时时间 5s，当前异步任务处理超过 5s 则认为任务失败</span>
  <span class="hljs-attr">maxTimeout</span>: <span class="hljs-number">5000</span>,
&#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">持久化</h3>
<p>当前任务队列存储到内存中，但在开发服务端时候，仅放入内存可能不是那么安全，我们可以通过传入 store 配置项来持久化队列数据。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 此时队列的插入和删除都会和数据库进行交互</span>
<span class="hljs-keyword">const</span> betterQueue = <span class="hljs-keyword">new</span> BetterQueue(asyncProcess, &#123;
  <span class="hljs-attr">store</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'sql'</span>,
    <span class="hljs-attr">dialect</span>: <span class="hljs-string">'sqlite'</span>,
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/path/to/sqlite/file'</span>
  &#125;
&#125;)

<span class="hljs-comment">// 或者使用 use</span>
betterQueue.use(&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'sql'</span>,
  <span class="hljs-attr">dialect</span>: <span class="hljs-string">'sqlite'</span>,
  <span class="hljs-attr">path</span>: <span class="hljs-string">'/path/to/sqlite/file'</span>
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>该库目前支持 SQLite 和 PostgreSQL，同时项目也提供了定制支持。</p>
<pre><code class="hljs language-ts copyable" lang="ts">betterQueue.use(&#123;
  <span class="hljs-attr">connect</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">cb</span>) </span>&#123;
    <span class="hljs-comment">// 连接你的数据库</span>
  &#125;,
  <span class="hljs-attr">getTask</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">taskId, cb</span>) </span>&#123;
    <span class="hljs-comment">// 查询任务</span>
  &#125;,
  <span class="hljs-attr">putTask</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">taskId, task, priority, cb</span>) </span>&#123;
    <span class="hljs-comment">// 保存任务同时携带优先级</span>
  &#125;,
  <span class="hljs-attr">takeFirstN</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">n, cb</span>) </span>&#123;
    <span class="hljs-comment">// 删除前 n 项（根据优先级和传入顺序排序）</span>
  &#125;,
  <span class="hljs-attr">takeLastN</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">n, cb</span>) </span>&#123;
    <span class="hljs-comment">// 删除后 n 项（根据优先级和传入顺序排序）</span>
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">先进后出</h3>
<p>better-queue 不仅仅提供了先进先出的逻辑，甚至提供了先进后出的逻辑，只需要在配置中添加 filo。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 创建队列</span>
<span class="hljs-keyword">const</span> betterQueue = <span class="hljs-keyword">new</span> BetterQueue(asyncProcess, &#123;
  <span class="hljs-attr">filo</span>: <span class="hljs-literal">true</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">任务过滤、合并以及调整优先级</h3>
<p>我们可以在业务处理中过滤某些任务，只需要添加 filter 函数。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> betterQueue = <span class="hljs-keyword">new</span> BetterQueue(asyncProcess, &#123;
  <span class="hljs-comment">// 在推送任务前执行过滤</span>
  <span class="hljs-attr">filter</span>: <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">job: Job, cb: <span class="hljs-built_in">Function</span></span>) </span>&#123;
    <span class="hljs-comment">// 在执行业务处理前预处理，验证数据，数据库查找等较为有用</span>
    <span class="hljs-comment">// 异步处理验证失败</span>
    <span class="hljs-keyword">if</span> (filterFail) &#123;
      cb(<span class="hljs-string">'not_allowed'</span>)
      <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-comment">// 为 job 前置处理</span>
    cb(<span class="hljs-literal">null</span>, job)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于有相同 id 的任务，better-queue 提供了合并函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> betterQueue = <span class="hljs-keyword">new</span> BetterQueue(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">task, cb</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"I have %d %ss."</span>, task.count, task.id);
  cb();
&#125;, &#123;
  <span class="hljs-attr">merge</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">oldTask, newTask, cb</span>) </span>&#123;
    oldTask.count += newTask.count;
    cb(<span class="hljs-literal">null</span>, oldTask);
  &#125;
&#125;)

betterQueue.push(&#123; <span class="hljs-attr">id</span>: <span class="hljs-string">'apple'</span>, <span class="hljs-attr">count</span>: <span class="hljs-number">2</span> &#125;)
betterQueue.push(&#123; <span class="hljs-attr">id</span>: <span class="hljs-string">'apple'</span>, <span class="hljs-attr">count</span>: <span class="hljs-number">1</span> &#125;)
betterQueue.push(&#123; <span class="hljs-attr">id</span>: <span class="hljs-string">'orange'</span>, <span class="hljs-attr">count</span>: <span class="hljs-number">1</span> &#125;)
betterQueue.push(&#123; <span class="hljs-attr">id</span>: <span class="hljs-string">'orange'</span>, <span class="hljs-attr">count</span>: <span class="hljs-number">1</span> &#125;)
 
<span class="hljs-comment">// 这时候会打印出 </span>
<span class="hljs-comment">// I have 3 apples.  </span>
<span class="hljs-comment">// I have 2 oranges.</span>

<span class="hljs-comment">// 而不是</span>

<span class="hljs-comment">// I have 1 apples.</span>
<span class="hljs-comment">// I have 1 oranges.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优先级对于队列也是非常重要的配置。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> betterQueue = <span class="hljs-keyword">new</span> BetterQueue(asyncProcess, &#123;
  <span class="hljs-comment">// 决定先处理那些任务</span>
  <span class="hljs-attr">priority</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">job: Job, cb: <span class="hljs-built_in">Function</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (job.queryArgs === <span class="hljs-string">'xxxxx'</span>) &#123;
      cb(<span class="hljs-literal">null</span>, <span class="hljs-number">10</span>)
      <span class="hljs-keyword">return</span>
    &#125; 
    <span class="hljs-keyword">if</span> (job.queryArgs === <span class="hljs-string">'xxx'</span>)&#123;
      cb(<span class="hljs-literal">null</span>, <span class="hljs-number">5</span>)
      <span class="hljs-keyword">return</span>
    &#125;
    cb(<span class="hljs-literal">null</span>, <span class="hljs-number">1</span>);
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">批处理与批处理前置</h3>
<p>批处理同样也可以增强系统处理能力。使用批处理不会立即处理任务，而是将多个任务合并为一个任务处理。</p>
<p>批处理不同于 concurrent，该配置是当前队列内存储的数据达到批处理配置后才会进行数据处理。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> betterQueue = <span class="hljs-keyword">new</span> BetterQueue<(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">batch, cb</span>) </span>&#123;
  <span class="hljs-comment">// batch 中是一个数组，最多为 3 个</span>
  <span class="hljs-comment">// [job1, job2, job3]</span>
  cb()
&#125;, &#123;
  <span class="hljs-comment">// 批处理大小</span>
  <span class="hljs-attr">batchSize</span>: <span class="hljs-number">3</span>,
  <span class="hljs-comment">// 5 秒内等待队列拥有 3 个项目，或者 3 秒内没有添加新的任务</span>
  <span class="hljs-comment">// 直接处理队列</span>
  <span class="hljs-attr">batchDelay</span>: <span class="hljs-number">5000</span>,
  <span class="hljs-attr">batchDelayTimeout</span>: <span class="hljs-number">3000</span>
&#125;)

<span class="hljs-comment">// 当前也会触发，不过要等 3 秒没有添加新任务</span>
<span class="hljs-comment">// 如开始时放入 1 条数据，等待 2.5 s 后放入第二条数据，则在 5s 后也会执行</span>
betterQueue.push(job1)
betterQueue.push(job2)

<span class="hljs-comment">// 在 1s 内推入第三条数据到队列中</span>
<span class="hljs-comment">// 队列数据达到 3 了，开始处理</span>
betterQueue.push(job3)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以通过添加前置条件判断是否执行下一个批处理。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> betterQueue = <span class="hljs-keyword">new</span> BetterQueue<(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">batch, cb</span>) </span>&#123;
  <span class="hljs-comment">// batch 中是一个数组，最多为 3 个</span>
  <span class="hljs-comment">// [job1, job2, job3]</span>
  cb()
&#125;, &#123;
  <span class="hljs-attr">precondition</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">cb</span>) </span>&#123;
    <span class="hljs-comment">// 当前是否是联网状态</span>
    isOnline(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err, ok</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (ok) &#123;
        <span class="hljs-comment">// 返回 true，进行下一次批处理</span>
        cb(<span class="hljs-literal">null</span>, <span class="hljs-literal">true</span>);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 继续执行直到为 true</span>
        cb(<span class="hljs-literal">null</span>, <span class="hljs-literal">false</span>);
      &#125;
    &#125;)
  &#125;,
  <span class="hljs-comment">// 每 10 秒执行一次 precondition 函数</span>
  <span class="hljs-attr">preconditionRetryTimeout</span>: <span class="hljs-number">10</span> * <span class="hljs-number">1000</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，better-queue 提供了更多的参数与配置，我们可以进一步学习，以便基于现有业务管理复杂的任务。让负责的任务变得更加可控。同时也可以提升系统处理业务的能力。</p>
<h2 data-id="heading-11">鼓励一下</h2>
<p>如果你觉得这篇文章不错，希望可以给与我一些鼓励，在我的 github 博客下帮忙 star 一下。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwsafight%2FpersonBlog" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wsafight/personBlog" ref="nofollow noopener noreferrer">博客地址</a></p>
<h2 data-id="heading-12">参考资料</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fbetter-queue" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/better-queue" ref="nofollow noopener noreferrer">better-queue</a></p>
<pre><code class="copyable"><span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            