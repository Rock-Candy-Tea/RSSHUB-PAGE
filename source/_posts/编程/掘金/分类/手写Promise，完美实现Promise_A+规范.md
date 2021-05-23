
---
title: '手写Promise，完美实现Promise_A+规范'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12e1263bb1574099aa425aa33a7118c9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 23 May 2021 02:40:19 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12e1263bb1574099aa425aa33a7118c9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>写这篇的文章的原因是在公司内部的前端小组里面分享了一下关于Promise的实现。感觉内容还不错，所以在这里分享给大家。源码文件会放到<a href="https://github.com/ZHONG-heart/study/tree/master/packages/promise/example" target="_blank" rel="nofollow noopener noreferrer">Github</a>上面，感兴趣的同学可以去查看源码。</p>
</blockquote>
<h2 data-id="heading-0">什么是Promise</h2>
<p><code>Promise</code>的核心思想是<code>Promise</code>表示异步操作的结果。一个<code>Promise</code>处于以下三种状态之一：</p>
<ul>
<li><code>pending</code> - <code>Promise</code> 的初始化状态</li>
<li><code>fulfilled</code> - 表示 <code>Promise</code> 成功操作的状态</li>
<li><code>rejected</code> - 表示 <code>Promise</code> 错误操作的状态</li>
</ul>
<p><code>Promise</code> 的内部状态改变如图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12e1263bb1574099aa425aa33a7118c9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">Promise的出现解决了什么问题</h2>
<ul>
<li>1.嵌套地狱的问题</li>
</ul>
<p>在<code>Promise</code>没有出现之前，我们会看到很多类似的代码。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)

fs.readFile(<span class="hljs-string">'./data.txt'</span>,<span class="hljs-string">'utf8'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err,data</span>)</span>&#123;
  fs.readFile(data, <span class="hljs-string">'utf8'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err,data</span>)</span>&#123;
    fs.readFile(data,<span class="hljs-string">'utf8'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err,data</span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(data);
    &#125;)
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Promise</code>出现之后，就可以采用链式调用的形式来写。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)

<span class="hljs-keyword">const</span> readFile = <span class="hljs-function">(<span class="hljs-params">filename</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    fs.readFile(filename, <span class="hljs-string">'utf8'</span>, <span class="hljs-function">(<span class="hljs-params">err, data</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (err) reject(err);
      resolve(data);
    &#125;)
  &#125;)
&#125;

readFile(<span class="hljs-string">'./data.txt'</span>).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> readFile(data) 
&#125;).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> readFile(data)  
&#125;).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用了<code>Promise</code>之后代码风格变得优雅了很多，写法上也更加直观。</p>
<ul>
<li>2.处理多个异步请求并发</li>
</ul>
<p><code>Promise.all</code>的出现让我们可以更加方便的处理多个任务完成时在进行处理的逻辑。</p>
<h2 data-id="heading-2">根据 <a href="https://promisesaplus.com/" target="_blank" rel="nofollow noopener noreferrer">Promise/A+</a> 规范实现 <code>Promise</code></h2>
<h3 data-id="heading-3">基本功能实现</h3>
<p>1.在动手写代码之前先了解一下需要实现哪些功能。</p>
<ul>
<li><code>Promise constructor</code></li>
</ul>
<blockquote>
<p><code>new Promise</code> 时，构造函数需要传入一个<code>executor()</code> 执行器，<code>executor</code>函数会立即执行，并且它支持传入两个参数，分别是 <code>resolve</code> 和 <code>reject</code>。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span><<span class="hljs-title">T</span>> </span>&#123;
   <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor: (resolve: (value: T ) => <span class="hljs-built_in">void</span>, reject: >(reason?: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">void</span>) => <span class="hljs-built_in">void</span></span>)</span>&#123;
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<ul>
<li><code>Promise</code> 状态 「Promise/A+ 2.1」</li>
</ul>
<blockquote>
<p><code>Promise</code> 必须处于以下三种状态之一：</p>
<p><code>pending</code>（等待中），可以转换为 <code>fulfilled</code>（完成）或 <code>rejected</code>（拒绝）。</p>
<p>当状态从 <code>pending</code> 切换到 <code>fulfilled</code> 时，该状态不得再过渡到其它状态，并且必须具有一个值，该值不能更改。</p>
<p>当状态从 <code>pending</code> 切换到 <code>rejected</code> 时，该状态不得再过渡到其它状态，并且必须有一个失败的原因，不能更改。</p>
</blockquote>
<ul>
<li><code>Promise then</code> 方法 「Promise/A+ 2.2」</li>
</ul>
<blockquote>
<p><code>Promise</code> 必须有一个 <code>then</code> 方法，<code>then</code> 接收两个参数，分别是成功时的回调 <code>onFulfilled</code>, 和失败时的回调 <code>onRejected</code>。</p>
<p><code>onFulfilled</code> 和 <code>onRejected</code> 是可选的参数，并且如果传入的 <code>onFulfilled</code> 和 <code>onRejected</code> 不是函数的话，则必须将其忽略。</p>
<p>如果 <code>onfulfilled</code> 是一个函数。则它必须在 <code>Promise</code> 的状态变成 <code>fulfilled</code>（完成）时才能调用，<code>Promise</code> 的值是传进它的第一个参数。并且它只能被调用一次。</p>
<p>如果 <code>onRejected</code> 是一个函数，则它必须在 <code>Promise</code> 的状态为 rejected（失败）时调用，并把失败的原因传入它的第一个参数。只能被调用一次。</p>
</blockquote>
<p>既然知道了需要实现那些功能，那就来动手操作一下，代码如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 使用枚举定义Promise的状态</span>
<span class="hljs-built_in">enum</span> PROMISE_STATUS &#123;
    PENDING,
    FULFILLED,
    REJECTED
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_Promise</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-comment">// 保存当前状态</span>
    <span class="hljs-keyword">private</span> status = PROMISE_STATUS.PENDING
    <span class="hljs-comment">// 保存resolve的值，或者reject的原因</span>
    <span class="hljs-keyword">private</span> value: T
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor: (resolve: (value: T) => <span class="hljs-built_in">void</span>, reject: (reason: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">void</span>) => <span class="hljs-built_in">void</span></span>)</span> &#123;
        executor(<span class="hljs-built_in">this</span>._resolve, <span class="hljs-built_in">this</span>._reject)
    &#125;
    
    <span class="hljs-comment">// 根据规范完成简易功能的then方法</span>
    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onfulfilled: (value: T) => <span class="hljs-built_in">any</span>, onrejected: (value: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span></span>)</span> &#123;
        <span class="hljs-comment">// 2.2.1</span>
        onfulfilled = <span class="hljs-keyword">typeof</span> onfulfilled === <span class="hljs-string">'function'</span> ? onfulfilled : <span class="hljs-literal">null</span>;
        onrejected = <span class="hljs-keyword">typeof</span> onrejected === <span class="hljs-string">'function'</span> ? onrejected : <span class="hljs-literal">null</span>;

        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PROMISE_STATUS.FULFILLED) &#123;
            <span class="hljs-comment">// 状态为fulfilled时调用成功的回调函数</span>
            onfulfilled(<span class="hljs-built_in">this</span>.value)
        &#125;

        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PROMISE_STATUS.REJECTED) &#123;
            <span class="hljs-comment">// 状态为rejected时调用失败的回调函数</span>
            onrejected(<span class="hljs-built_in">this</span>.value)
        &#125;

    &#125;
    
    <span class="hljs-comment">// 传入executor方法的第一个参数，调用此方法就是成功</span>
    <span class="hljs-keyword">private</span> _resolve = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (value === <span class="hljs-built_in">this</span>) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'A promise cannot be resolved with itself.'</span>);
        &#125;
        <span class="hljs-comment">// 只有是pending状态才可以更新状态，防止二次调用</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PROMISE_STATUS.PENDING) <span class="hljs-keyword">return</span>;
        <span class="hljs-built_in">this</span>.status = PROMISE_STATUS.FULFILLED;
        <span class="hljs-built_in">this</span>.value = value;
    &#125;
    
    <span class="hljs-comment">// 传入executor方法的第二个参数，调用此方法就是失败</span>
    <span class="hljs-keyword">private</span> _reject = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
        <span class="hljs-comment">// 只有是pending状态才可以更新状态，防止二次调用</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PROMISE_STATUS.PENDING) <span class="hljs-keyword">return</span>;
        <span class="hljs-built_in">this</span>.status = PROMISE_STATUS.REJECTED;
        <span class="hljs-built_in">this</span>.value = value
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码写完了我们测试一下功能：</p>
<pre><code class="copyable">const p1 = new _Promise((resolve, reject) => &#123;
  resolve(2)
&#125;)

p1.then(res => &#123;
  console.log(res, 'then ok1')
&#125;)

const p2 = new _Promise((resolve, reject) => &#123;
  setTimeout(() => &#123;
    resolve(2)
  &#125;, 1000);
&#125;)

p2.then(res => &#123;
  console.log(res, 'then ok2')
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台会打印出：</p>
<pre><code class="copyable">2 "then ok1"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不错，现在已经是稍见雏形。</p>
<h3 data-id="heading-4">支持异步操作</h3>
<p>我们已经实现了一个入门级的 <code>Promise</code>,但是细心的同学应该已经发现了，<code>then ok2</code> 这个值没有打印出来。</p>
<p>导致这个问题出现的原因是什么呢？原来是我们在执行then函数的时候，由于是异步操作，状态一直处于pending的状态，传进来的回调函数没有触发执行。</p>
<p>知道了问题就好解决了。只需要把传进来的回调函数存储起来。在调用resolve或reject方法的时候执行就可以了，我们优化一下代码：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-built_in">enum</span> PROMISE_STATUS &#123;
    PENDING,
    FULFILLED,
    REJECTED
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_Promise</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-keyword">private</span> status = PROMISE_STATUS.PENDING
    <span class="hljs-keyword">private</span> value: T
    <span class="hljs-comment">// 保存then方法传入的回调函数</span>
    <span class="hljs-keyword">private</span> callbacks = []
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor: (resolve: (value: T) => <span class="hljs-built_in">void</span>, reject: (reason: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">void</span>) => <span class="hljs-built_in">void</span></span>)</span> &#123;
        executor(<span class="hljs-built_in">this</span>._resolve, <span class="hljs-built_in">this</span>._reject)
    &#125;

    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onfulfilled: (value: T) => <span class="hljs-built_in">any</span>, onrejected: (value: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span></span>)</span> &#123;
        <span class="hljs-comment">// 2.2.1</span>
        onfulfilled = <span class="hljs-keyword">typeof</span> onfulfilled === <span class="hljs-string">'function'</span> ? onfulfilled : <span class="hljs-literal">null</span>;
        onrejected = <span class="hljs-keyword">typeof</span> onrejected === <span class="hljs-string">'function'</span> ? onrejected : <span class="hljs-literal">null</span>;

        <span class="hljs-comment">// 把then方法传入的回调函数整合一下</span>
        <span class="hljs-keyword">const</span> handle = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PROMISE_STATUS.FULFILLED) &#123;
                onfulfilled && onfulfilled(<span class="hljs-built_in">this</span>.value)
            &#125;

            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PROMISE_STATUS.REJECTED) &#123;
                onrejected && onrejected(<span class="hljs-built_in">this</span>.value)
            &#125;
        &#125;

        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PROMISE_STATUS.PENDING) &#123;
            <span class="hljs-comment">// 当状态是pending时，把回调函数保存进callback里面</span>
            <span class="hljs-built_in">this</span>.callbacks.push(handle)
        &#125;

        handle()
    &#125;

    <span class="hljs-keyword">private</span> _resolve = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (value === <span class="hljs-built_in">this</span>) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'A promise cannot be resolved with itself.'</span>);
        &#125;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PROMISE_STATUS.PENDING) <span class="hljs-keyword">return</span>;
        <span class="hljs-built_in">this</span>.status = PROMISE_STATUS.FULFILLED;
        <span class="hljs-built_in">this</span>.value = value;
        <span class="hljs-comment">// 遍历执行回调</span>
        <span class="hljs-built_in">this</span>.callbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn())
    &#125;

    <span class="hljs-keyword">private</span> _reject = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PROMISE_STATUS.PENDING) <span class="hljs-keyword">return</span>;
        <span class="hljs-built_in">this</span>.status = PROMISE_STATUS.REJECTED;
        <span class="hljs-built_in">this</span>.value = value
        <span class="hljs-comment">// 遍历执行回调</span>
        <span class="hljs-built_in">this</span>.callbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn())
    &#125;


&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在来测试一下上面的代码：</p>
<pre><code class="copyable">const p2 = new _Promise((resolve, reject) => &#123;
  setTimeout(() => &#123;
    resolve(2)
  &#125;, 1000);
&#125;)

p2.then(res => &#123;
  console.log(res, 'then ok2')
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在等待1s后，控制台会打印出：</p>
<pre><code class="copyable">2 "then ok2"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前已经可以支持异步操作了。现在的你已经是江湖中的高手了。</p>
<h3 data-id="heading-5">then 方法的链式调用</h3>
<p>在文章一开头介绍Promise时，提到了链式调用的概念<code>.then().then()</code>，现在就要实现这个至关重要的功能，在开始前先看一下<code>Promise/A+</code>的规范</p>
<blockquote>
<p><code>then</code>必须返回一个Promise 「Promise/A+ 2.2.7」</p>
<p><code>promise2 = promise1.then(onFulfilled, onRejected);</code></p>
<p>如果一个 <code>onFulfilled</code> 或 <code>onRejected</code> 返回一个值 <code>x</code> ,则运行 <code>Promise Resolution Procedure</code> (会在下面实现这个方法)。</p>
<p>如果任何一个 <code>onFulfilled </code>或 <code>onRejected</code> 引发异常 <code>e</code> 则 <code>promise2</code> 必须以 <code>e</code> 为其理由 <code>reject</code> (拒绝).</p>
<p>如果 <code>onFulfilled</code> 不是函数且<code>promise1</code>状态已经<code>fuifilled</code>（完成），则 <code>promise2</code> 必须使用与相同的值来实现 <code>promise1</code>。</p>
<p>如果<code>onRejected</code>不是函数而 <code>promise1</code> 状态为<code>rejected</code>（拒绝），则 <code>promise2</code> 必须以与相同的理由将其拒绝 <code>promise1</code>。</p>
<h3 data-id="heading-6">Promise Resolution Procedure 实现</h3>
<p>首先该方法的使用方式类似于下面这种形式
<code>resolvePromise(promise,x,...)</code></p>
<p>如果 <code>promise</code> 和 <code>x</code> 引用相同的对象，promise 则应该以TypeError为理由拒绝。「Promise/A+ 2.3.1」</p>
<p>如果 <code>x</code> 是一个 <code>promise</code> ，则应该采用它原本的状态返回。「Promise/A+ 2.3.2」</p>
<p>否则，判断 <code>x</code> 如果是对象或者是函数。则执行以下操作，先声明 <code>let then = x.then</code> ,如果出现异常结果 <code>e</code> ,则以 <code>e</code> 作为 <code>promise</code> reject（拒绝）的原因。如果 <code>then</code> 是个函数，则用 <code>call</code> 执行 <code>then</code> ，把 <code>this</code> 指向为 <code>x</code> ，第一个参数用 <code>resolvePromise</code> 调用，第二个用 <code>rejectPromise</code> 调用「Promise/A+ 2.3.3」</p>
<p>如果 <code>x</code> 不是对象或者方法，则使用 <code>x</code> 的值 <code>resolve</code> 完成 「Promise/A+ 2.3.4」</p>
</blockquote>
<p>只是通过文字不太容易理解，我们来看一下代码的实现：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-built_in">enum</span> PROMISE_STATUS &#123;
    PENDING,
    FULFILLED,
    REJECTED
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_Promise</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-keyword">private</span> status = PROMISE_STATUS.PENDING
    <span class="hljs-keyword">private</span> value: T
    <span class="hljs-keyword">private</span> callbacks = []
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor: (resolve: (value: T) => <span class="hljs-built_in">void</span>, reject: (reason: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">void</span>) => <span class="hljs-built_in">void</span></span>)</span> &#123;
        executor(<span class="hljs-built_in">this</span>._resolve, <span class="hljs-built_in">this</span>._reject)
    &#125;

    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onfulfilled: (value: T) => <span class="hljs-built_in">any</span>, onrejected: (value: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span></span>)</span> &#123;
        <span class="hljs-comment">// 2.2.1</span>
        onfulfilled = <span class="hljs-keyword">typeof</span> onfulfilled === <span class="hljs-string">'function'</span> ? onfulfilled : <span class="hljs-literal">null</span>;
        onrejected = <span class="hljs-keyword">typeof</span> onrejected === <span class="hljs-string">'function'</span> ? onrejected : <span class="hljs-literal">null</span>;

        <span class="hljs-keyword">const</span> nextPromise = <span class="hljs-keyword">new</span> _Promise(<span class="hljs-function">(<span class="hljs-params">nextResolve, nextReject</span>) =></span> &#123;
            <span class="hljs-keyword">const</span> handle = <span class="hljs-function">() =></span> &#123;
                <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PROMISE_STATUS.FULFILLED) &#123;
                    <span class="hljs-keyword">const</span> x = (onfulfilled && onfulfilled(<span class="hljs-built_in">this</span>.value))
                    <span class="hljs-built_in">this</span>._resolvePromise(nextPromise, x, nextResolve, nextReject)
                &#125;

                <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PROMISE_STATUS.REJECTED) &#123;
                    <span class="hljs-keyword">if</span> (onrejected) &#123;
                        <span class="hljs-keyword">const</span> x = onrejected(<span class="hljs-built_in">this</span>.value)
                        <span class="hljs-built_in">this</span>._resolvePromise(nextPromise, x, nextResolve, nextReject)
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        nextReject(<span class="hljs-built_in">this</span>.value)
                    &#125;
                &#125;

            &#125;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PROMISE_STATUS.PENDING) &#123;
                <span class="hljs-built_in">this</span>.callbacks.push(handle)
            &#125; <span class="hljs-keyword">else</span> &#123;
                handle()
            &#125;

        &#125;);
        <span class="hljs-keyword">return</span> nextPromise

    &#125;

    <span class="hljs-keyword">private</span> _resolve = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (value === <span class="hljs-built_in">this</span>) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'A promise cannot be resolved with itself.'</span>);
        &#125;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PROMISE_STATUS.PENDING) <span class="hljs-keyword">return</span>;
        <span class="hljs-built_in">this</span>.status = PROMISE_STATUS.FULFILLED;
        <span class="hljs-built_in">this</span>.value = value;
        <span class="hljs-built_in">this</span>.callbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn())
    &#125;

    <span class="hljs-keyword">private</span> _reject = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status !== PROMISE_STATUS.PENDING) <span class="hljs-keyword">return</span>;
        <span class="hljs-built_in">this</span>.status = PROMISE_STATUS.REJECTED;
        <span class="hljs-built_in">this</span>.value = value
        <span class="hljs-built_in">this</span>.callbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn())
    &#125;

    <span class="hljs-keyword">private</span> _resolvePromise = <T><span class="hljs-function">(<span class="hljs-params">nextPromise: _Promise<T>, x: <span class="hljs-built_in">any</span>, resolve, reject</span>) =></span> &#123;

        <span class="hljs-comment">// 2.3.1 nextPromise 不能和 x 相等</span>
        <span class="hljs-keyword">if</span> (nextPromise === x) &#123;
            <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'The promise and the return value are the same'</span>));
        &#125;

        <span class="hljs-comment">// 2.3.2 如果 x 是 Promise 返回 x 的状态和值</span>
        <span class="hljs-keyword">if</span> (x <span class="hljs-keyword">instanceof</span> _Promise) &#123;
            x.then(resolve, reject)
        &#125;

        <span class="hljs-comment">// 2.3.3 如果 x 是对象或者函数执行 if 里面的逻辑</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'object'</span> || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'function'</span>) &#123;
            <span class="hljs-keyword">if</span> (x === <span class="hljs-literal">null</span>) &#123;
                <span class="hljs-keyword">return</span> resolve(x);
            &#125;

            <span class="hljs-comment">// 2.3.3.1</span>
            <span class="hljs-keyword">let</span> then;
            <span class="hljs-keyword">try</span> &#123;
                then = x.then;
            &#125; <span class="hljs-keyword">catch</span> (error) &#123;
                <span class="hljs-keyword">return</span> reject(error);
            &#125;

            <span class="hljs-comment">// 2.3.3.3</span>
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> then === <span class="hljs-string">'function'</span>) &#123;
                <span class="hljs-comment">// 声明called 在调用过一次resolve或者reject之后，修改为true，保证只能调用一次</span>
                <span class="hljs-keyword">let</span> called = <span class="hljs-literal">false</span>; 
                <span class="hljs-keyword">try</span> &#123;
                    then.call(x, <span class="hljs-function"><span class="hljs-params">y</span> =></span> &#123;
                        <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>; <span class="hljs-comment">// 2.3.3.3.4.1</span>
                        called = <span class="hljs-literal">true</span>;
                        <span class="hljs-comment">// 递归解析的过程（因为可能 promise 中还有 promise）</span>
                        <span class="hljs-built_in">this</span>._resolvePromise(nextPromise, y, resolve, reject) 
                    &#125;, <span class="hljs-function"><span class="hljs-params">r</span> =></span> &#123;
                        <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>; <span class="hljs-comment">// 2.3.3.3.4.1</span>
                        called = <span class="hljs-literal">true</span>;
                        reject(r)
                    &#125;)
                &#125; <span class="hljs-keyword">catch</span> (e) &#123;
                    <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>; <span class="hljs-comment">// 2.3.3.3.4.1</span>
                    <span class="hljs-comment">// 2.3.3.3.4</span>
                    reject(e)
                &#125;
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">// 2.3.3.4</span>
                resolve(x)
            &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 2.3.4</span>
            resolve(x);
        &#125;

    &#125;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前已经实现可以链式调用的功能了，我们来测试一下：</p>
<pre><code class="copyable">const p3 = new _Promise((resolve, reject) => &#123;
    setTimeout(() => &#123;
        resolve(3)
    &#125;, 1000);
&#125;)

p3.then(res => &#123;
  console.log(res, 'then ok3')
  return '链式调用'
&#125;).then(res => &#123;
  console.log(res)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等待1s之后，控制台会打印出：</p>
<pre><code class="copyable">3 "then ok3"
"链式调用"
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">支持微任务</h3>
<p>有没有同学想到还缺少了一个尤为重要的功能，那就是微任务。我们应该如何实现和内置 <code>Promise</code> 一样的微任务流程呢?</p>
<p>在 <code>Web Api</code> 里面有这样一个方法 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/MutationObserver" target="_blank" rel="nofollow noopener noreferrer">MutationObserver</a>。我们可以基于它实现微任务的功能。并且也已经有相关的库给我们封装好了这个方法，它就是 <a href="https://github.com/kriskowal/asap" target="_blank" rel="nofollow noopener noreferrer">asap</a>。只要把需要以微任务执行的函数传入即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">asap(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// ...</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实在 <code>Web Api</code> 里面还有这样一个方法 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/WindowOrWorkerGlobalScope/queueMicrotask" target="_blank" rel="nofollow noopener noreferrer">queueMicrotask</a> 可以直接使用。使用方式也是把要以微任务执行的函数传入进去即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">self.queueMicrotask(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 函数的内容</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>queueMicrotask</code> 唯一的缺点就是兼容性不太好，在生产环境中建议还是使用 <code>asap</code> 这个库来实现微任务。</p>
<p>把之前写好的 <code>Promise then</code> 方法稍微做一下调整：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onfulfilled: (value: T) => <span class="hljs-built_in">any</span>, onrejected: (value: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span></span>)</span> &#123;
        <span class="hljs-comment">// 2.2.1</span>
        onfulfilled = <span class="hljs-keyword">typeof</span> onfulfilled === <span class="hljs-string">'function'</span> ? onfulfilled : <span class="hljs-literal">null</span>;
        onrejected = <span class="hljs-keyword">typeof</span> onrejected === <span class="hljs-string">'function'</span> ? onrejected : <span class="hljs-literal">null</span>;

        <span class="hljs-keyword">const</span> nextPromise = <span class="hljs-keyword">new</span> _Promise(<span class="hljs-function">(<span class="hljs-params">nextResolve, nextReject</span>) =></span> &#123;
            <span class="hljs-keyword">const</span> _handle = <span class="hljs-function">() =></span> &#123;
                <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PROMISE_STATUS.FULFILLED) &#123;
                    <span class="hljs-keyword">const</span> x = (onfulfilled && onfulfilled(<span class="hljs-built_in">this</span>.value))
                    <span class="hljs-built_in">this</span>._resolvePromise(nextPromise, x, nextResolve, nextReject)
                &#125;

                <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PROMISE_STATUS.REJECTED) &#123;
                    <span class="hljs-keyword">if</span> (onrejected) &#123;
                        <span class="hljs-keyword">const</span> x = onrejected(<span class="hljs-built_in">this</span>.value)
                        <span class="hljs-built_in">this</span>._resolvePromise(nextPromise, x, nextResolve, nextReject)
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        nextReject(<span class="hljs-built_in">this</span>.value)
                    &#125;
                &#125;

            &#125;
            <span class="hljs-keyword">const</span> handle = <span class="hljs-function">() =></span> &#123;
                <span class="hljs-comment">// 支持微任务</span>
                queueMicrotask(_handle)
            &#125;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status === PROMISE_STATUS.PENDING) &#123;
                <span class="hljs-built_in">this</span>.callbacks.push(handle)
            &#125; <span class="hljs-keyword">else</span> &#123;
                handle()
            &#125;

        &#125;);
        <span class="hljs-keyword">return</span> nextPromise

    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在完美支持微任务，和内置 <code>Promises</code> 事件执行顺序一致。我们来测试一下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'first'</span>)
<span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> _Promise(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'second'</span>)
  resolve(<span class="hljs-string">'third'</span>)
&#125;)
p1.then(<span class="hljs-built_in">console</span>.log)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'fourth'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到控制台打印的结果为：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">first
second
fourth
third
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里，我们已经把Promise最关键的功能完成了：<code>支持异步操作</code>，<code>then支持链式调用</code>，<code>支持微任务</code>。</p>
<h2 data-id="heading-8">测试完成的 Promise 是否符合规范</h2>
<p>1.下载Promise/A+规范提供了一个专门的测试脚本 <code>promises-aplus-tests</code></p>
<pre><code class="copyable">yarn add promises-aplus-tests -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.在我们的代码中加入以下代码：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">(_Promise <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>).deferred = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> dfd = &#123;&#125; <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>;
    dfd.promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        dfd.resolve = resolve;
        dfd.reject = reject;
    &#125;);
    <span class="hljs-keyword">return</span> dfd;
&#125;

<span class="hljs-built_in">module</span>.exports = _Promise;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.修改 <code>package.json</code> 文件增加以下内容（<code>./dist/promise/index.js</code>是需要测试的文件路径）：</p>
<pre><code class="copyable">&#123;
  "scripts": &#123;
    "test": "promises-aplus-tests ./dist/promise/index.js"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.执行 <code>yarn test</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c7d0bd7cb65407a8b3806d8b77c0b04~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到872个测试用例全部通过。</p>
<h2 data-id="heading-9"><code>Promise</code> 的其它 <code>API</code> 实现</h2>
<p>到目前为止，上述代码已经完整的按照 Promise/A+ 规范实现了，但还有一些内置Api没有实现。下面就把这些内置的方法来实现：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_Promise</span> </span>&#123;

    <span class="hljs-keyword">catch</span>(onrejected) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>, onrejected)
    &#125;

    <span class="hljs-function"><span class="hljs-title">finally</span>(<span class="hljs-params">cb</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(
            <span class="hljs-function"><span class="hljs-params">value</span> =></span> _Promise.resolve(cb()).then(<span class="hljs-function">() =></span> value),
            <span class="hljs-function"><span class="hljs-params">reason</span> =></span> _Promise.resolve(cb()).then(<span class="hljs-function">() =></span> &#123; <span class="hljs-keyword">throw</span> reason &#125;)
        );
    &#125;

    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (value <span class="hljs-keyword">instanceof</span> _Promise) &#123;
            <span class="hljs-keyword">return</span> value;
        &#125;

        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> _Promise(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
            resolve(value);
        &#125;);
    &#125;

    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> _Promise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            reject(reason);
        &#125;);
    &#125;

    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promises</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> _Promise(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
            <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(promises)) &#123;
                <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Promise.race accepts an array'</span>));
            &#125;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>, len = promises.length; i < len; i++) &#123;
                _Promise.resolve(promises[i]).then(resolve, reject);
            &#125;
        &#125;);

    &#125;

    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">promises</span>)</span> &#123;
        <span class="hljs-keyword">let</span> result = [];
        <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;

        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> _Promise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">const</span> processValue = <span class="hljs-function">(<span class="hljs-params">index, value</span>) =></span> &#123;
                result[index] = value;
                i++;
                <span class="hljs-keyword">if</span> (i == promises.length) &#123;
                    resolve(result);
                &#125;;
            &#125;;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; index < promises.length; index++) &#123;
                promises[index].then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
                    processValue(index, value);
                &#125;, reject);
            &#125;;
        &#125;);
    &#125;

    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">allSettled</span>(<span class="hljs-params">promises</span>)</span> &#123;
        <span class="hljs-keyword">let</span> result = []
        <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> _Promise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">const</span> processValue = <span class="hljs-function">(<span class="hljs-params">index, value, status: <span class="hljs-string">'fulfilled'</span> | <span class="hljs-string">'rejected'</span></span>) =></span> &#123;
                result[index] = &#123; status, value &#125;
                i++;
                <span class="hljs-keyword">if</span> (i == promises.length) &#123;
                    resolve(result);
                &#125;;
            &#125;;


            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; index < promises.length; index++) &#123;
                promises[index].then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
                    processValue(index, value, <span class="hljs-string">'fulfilled'</span>)
                &#125;, <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
                    processValue(index, value, <span class="hljs-string">'rejected'</span>)
                &#125;);
            &#125;;
        &#125;)
    &#125;
    
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">如何实现 <code>async</code> 和 <code>await</code></h2>
<p>我们完成了 <code>Promise</code> 的实现。但是大家有没有想过 <code>async</code> 和 <code>await</code> 这个 <code>Promise</code> 的语法糖如何实现呢？</p>
<p>这里我们就要借助 <code>Generator</code> 函数来实现这个功能，废话少说，直接上代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> gp1 = <span class="hljs-keyword">new</span> _Promise(<span class="hljs-function"><span class="hljs-params">r</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        r(<span class="hljs-number">1</span>)
    &#125;, <span class="hljs-number">1000</span>);
&#125;)

<span class="hljs-keyword">let</span> gp2 = <span class="hljs-keyword">new</span> _Promise(<span class="hljs-function"><span class="hljs-params">r</span> =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        r(<span class="hljs-number">2</span>)
    &#125;, <span class="hljs-number">1000</span>);
&#125;)

<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">gen</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> a = <span class="hljs-keyword">yield</span> gp1
    <span class="hljs-keyword">let</span> b = <span class="hljs-keyword">yield</span> gp2
    <span class="hljs-keyword">return</span> b + a
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span>(<span class="hljs-params">gen</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> _Promise(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
        g = gen()
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params">v</span>) </span>&#123;
          ret = g.next(v)
          <span class="hljs-keyword">if</span> (ret.done) <span class="hljs-keyword">return</span> resolve(ret.value);
          _Promise.resolve(ret.value).then(next)
        &#125;
        next()
    &#125;)
&#125;

run(gen).then(<span class="hljs-built_in">console</span>.log)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台里面会打印出结果为：<code>3</code></p>
<p>如果对这个 <code>run</code> 函数感兴趣，推荐去看下这个 <a href="https://github.com/tj/co" target="_blank" rel="nofollow noopener noreferrer">co</a> 库实现,代码写的非常简洁，只有一百行左右，值的一看。</p>
<h2 data-id="heading-11">总结</h2>
<p>用了近半天的时间才把这篇文章给写出来。其中的源码文件已经放到 <a href="https://github.com/ZHONG-heart/study/tree/master/packages/promise/example" target="_blank" rel="nofollow noopener noreferrer">Github</a> 上面。不想手敲一遍的同学可以直接拉下来代码执行查看结果。如果你有不同的意见或想法也欢迎留言。</p>
<p>相关资源链接</p>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/MutationObserver" target="_blank" rel="nofollow noopener noreferrer">MutationObserver</a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/WindowOrWorkerGlobalScope/queueMicrotask" target="_blank" rel="nofollow noopener noreferrer">queueMicrotask</a></li>
<li><a href="https://github.com/kriskowal/asap" target="_blank" rel="nofollow noopener noreferrer">asap</a></li>
<li><a href="https://github.com/tj/co" target="_blank" rel="nofollow noopener noreferrer">co</a></li>
</ul></div>  
</div>
            