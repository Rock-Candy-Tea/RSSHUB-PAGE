
---
title: '前端猛男带你走进nodejs系列（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62cd94d69af949c3b4390eee841bab35~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 18:01:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62cd94d69af949c3b4390eee841bab35~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a name="user-content-ah3x0" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h1 data-id="heading-0">一、nodejs之events模块</h1>
<p><a name="user-content-uwXmE" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-1">1、事件驱动模型</h2>
<p>Nodejs 使用了一个事件驱动、非阻塞 IO 的模型（有兴趣的同学可以回去看一下系列一），events模块是事件驱动的核心模块。很多内置模块都继承了events.EventEmitter。自己无需手动实现这种设计模式，直接继承EventEmitter即可。代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; EventEmitter &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"events"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyEmitter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">EventEmitter</span> </span>&#123;&#125;

<span class="hljs-keyword">const</span> ins = <span class="hljs-keyword">new</span> MyEmitter();
ins.on(<span class="hljs-string">"test"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"emit test event"</span>);
&#125;);
ins.emit(<span class="hljs-string">"test"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-QFBM6" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-2">2、API全解</h2>
<p><a name="user-content-zUnge" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-3">（1）API解释</h3>
<p>在events模块中，需要一个哈希表来存储监听事件和对应回调函数的，形式大概如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  事件A: [回调函数<span class="hljs-number">1</span>，回调函数<span class="hljs-number">2</span>，回调函数<span class="hljs-number">3</span>],
  事件B: 回调函数<span class="hljs-number">1</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">所有的API都是围绕这个哈希表来进行增删查改
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>emitter.addListener(eventName, listener)：对应事件增加一个回调函数</li>
<li>emitter.on(eventName, listener)：同1，别名</li>
<li>emitter.once(eventName, listener)：同1，在事件被多次触发下只执行一次</li>
<li>emitter.prependListener(eventName, listener)：同1，添加在监听器数组开头</li>
<li>emitter.prependOnceListener(eventName, listener)：同1，添加在监听器数组开头 && 单次监听器</li>
<li>emitter.removeListener(eventName, listener)：移除指定的事件中的某个监听器</li>
<li>emitter.removeAllListeners([eventName])：移除全部监听器或者指定的事件的监听器</li>
<li>emitter.emit(eventName[, ...args])：按照监听器注册的顺序，同步地调用对应事件的监听器，并提供传入的参数</li>
<li>emitter.eventNames()：获得哈希表中所有的键值(包括Symbol)</li>
<li>emitter.listenerCount(eventName)：获得哈希表中对应键值的监听器数量</li>
<li>emitter.listeners(eventName)：获得对应键的监听器数组的副本</li>
<li>emitter.rawListeners(eventName)：同上，只不过不会对once处理过后的监听器还原</li>
<li>emitter.setMaxListeners(n)：设置当前实例监听器最大限制数的值</li>
<li>emitter.getMaxListeners()：返回当前实例监听器最大限制数的值</li>
<li>EventEmitter.defaultMaxListeners：它是每个实例的监听器最大限制数的默认值，修改它会影响所有实例</li>
</ul>
<p><a name="user-content-y1cql" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-4">（2）events的错误处理</h3>
<p>下面先看一个例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> ins = <span class="hljs-keyword">new</span> MyEmitter();
ins.on(<span class="hljs-string">"error"</span>, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"error msg is"</span>, error.message);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">注册error事件后，我原本的理解是，所有事件回掉逻辑中的错误都会在 EventEmitter 内部被捕获，并且在内部触发 error 事件。也就是说下面代码，会打印："error msg is a is not defined"。
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">ins.on(<span class="hljs-string">"test"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(a);
&#125;);
ins.emit(<span class="hljs-string">"test"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而，错误并没有捕获，直接抛出了异常。由此可见，EventEmitter 在执行内部逻辑的时候，并没有try-catch。<br>如果按照正常想法，不想每一次都在外面套一层try-catch，那应该怎么做呢？我的做法是在 EventEmitter 原型链上新增一个safeEmit函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">EventEmitter.prototype.safeEmit = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">name, ...args</span>) </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.emit(name, ...args);
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.emit(<span class="hljs-string">"error"</span>, error);
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-hO9pB" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-5">（3）监听器队列顺序处理</h3>
<p>对于同一个事件，触发它的时候，函数的执行顺序就是函数绑定时候的顺序。官方库提供了emitter.prependListener()和 emitter.prependOnceListener() 两个接口，可以让新的监听器直接添加到队列头部。<br>但是如果想让新的监听器放入任何监听器队列的任何位置呢？在原型链上封装了 insertListener 方法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; EventEmitter &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"events"</span>);

EventEmitter.prototype.insertListener = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">
    name,
    index,
    callback,
    once = <span class="hljs-literal">false</span>
</span>) </span>&#123;
    <span class="hljs-comment">// 如果是once监听器，其数据结构是 &#123;listener: Function&#125;</span>
    <span class="hljs-comment">// 正常监听器，直接是 Function</span>
    <span class="hljs-keyword">const</span> listeners = ins.rawListeners(name);
    <span class="hljs-keyword">const</span> that = <span class="hljs-built_in">this</span>;
    <span class="hljs-comment">// 下标不合法</span>
    <span class="hljs-keyword">if</span> (index > listeners.length || index < <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;
    <span class="hljs-comment">// 绑定监听器数量已达上限</span>
    <span class="hljs-keyword">if</span> (listeners.length >= <span class="hljs-built_in">this</span>.getMaxListeners()) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;
    listeners.splice(index, <span class="hljs-number">0</span>, once ? &#123; <span class="hljs-attr">listener</span>: callback &#125; : callback);
    <span class="hljs-built_in">this</span>.removeAllListeners(name);
    listeners.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> item === <span class="hljs-string">"function"</span>) &#123;
            that.on(name, item);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">const</span> &#123; listener &#125; = item;
            that.once(name, listener);
        &#125;
    &#125;);
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;;

<span class="hljs-keyword">const</span> ins = <span class="hljs-keyword">new</span> EventEmitter();
ins.on(<span class="hljs-string">"test"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"test 1"</span>);
&#125;);
ins.on(<span class="hljs-string">"test"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"test 2"</span>);
&#125;);

<span class="hljs-comment">// 监听器队列中插入新的监听器，一个是once类型，一个不是once类型</span>
ins.insertListener(
    <span class="hljs-string">"test"</span>,
    <span class="hljs-number">0</span>,
    <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"once test insert"</span>);
    &#125;,
    <span class="hljs-literal">true</span>
);
ins.insertListener(<span class="hljs-string">"test"</span>, <span class="hljs-number">1</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"test insert"</span>);
&#125;);

ins.emit(<span class="hljs-string">'test'</span>);
ins.emit(<span class="hljs-string">'test'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终输出结果为：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">once test insert
test insert
test <span class="hljs-number">1</span>
test <span class="hljs-number">2</span>
test insert
test <span class="hljs-number">1</span>
test <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面还有一个有趣的问题：在一个事件监听器中监听同一个事件会死循环吗？</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; EventEmitter &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"events"</span>);
<span class="hljs-keyword">const</span> test = <span class="hljs-keyword">new</span> EventEmitter();
test.on(<span class="hljs-string">'repeat'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">repeatFn</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'123'</span>)
    test.on(<span class="hljs-string">'repeat'</span>, repeatFn);
&#125;)
test.emit(<span class="hljs-string">'repeat'</span>);
test.emit(<span class="hljs-string">'repeat'</span>);
test.emit(<span class="hljs-string">'repeat'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果为：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-number">123</span>
<span class="hljs-number">123</span>
<span class="hljs-number">123</span>
<span class="hljs-number">123</span>
<span class="hljs-number">123</span>
<span class="hljs-number">123</span>
<span class="hljs-number">123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从结果来看，在一个事件监听器中监听同一个事件不会死循环，但是随着emit的次数增加，该事件下对应的listener越来越多，触发同一个函数的次数也越来越多，所以应该尽量避免不必要的重复回调。
<a name="user-content-RE20n" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-6">（4）调整最大listeners</h3>
<p>默认情况下针对单一事件的最大listener数量是10，如果超过10个的话listener还是会执行，只是控制台会有警告信息，告警信息里面已经提示了操作建议，可以通过调用emitter.setMaxListeners()来调整最大listener的限制</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; EventEmitter &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"events"</span>);
<span class="hljs-keyword">const</span> test = <span class="hljs-keyword">new</span> EventEmitter();
<span class="hljs-built_in">console</span>.log(test.getMaxListeners()); <span class="hljs-comment">// 获取当前事件的最大listeners数量，默认值为10</span>

test.on(<span class="hljs-string">'repeat'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">repeatFn</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'123'</span>)
    test.on(<span class="hljs-string">'repeat'</span>, repeatFn);
&#125;)
test.setMaxListeners(<span class="hljs-number">5</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'afterChange'</span>, test.getMaxListeners()
)
test.emit(<span class="hljs-string">'repeat'</span>);
test.emit(<span class="hljs-string">'repeat'</span>);
test.emit(<span class="hljs-string">'repeat'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">上面的打印结果为：
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">beforeChange:  <span class="hljs-number">10</span>
<span class="hljs-attr">afterChange</span>:  <span class="hljs-number">5</span>
<span class="hljs-number">123</span>
<span class="hljs-number">123</span>
<span class="hljs-number">123</span>
<span class="hljs-number">123</span>
<span class="hljs-number">123</span>
<span class="hljs-number">123</span>
<span class="hljs-number">123</span>
(node:<span class="hljs-number">48024</span>) MaxListenersExceededWarning: Possible EventEmitter memory leak detected. <span class="hljs-number">6</span> repeat listeners added to [EventEmitter]. Use emitter.setMaxListeners() to increase limit
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">上面的警告信息的粒度不够，并不能告诉我们是哪里的代码出了问题，可以通过process.on('warning')来获得更具体的信息（emitter、event、eventCount）
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">MaxListenersExceededWarning: Possible EventEmitter memory leak detected. <span class="hljs-number">6</span> repeat listeners added to [EventEmitter]. Use emitter.setMaxListeners() to increase limit
    at _addListener (events.js:<span class="hljs-number">385</span>:<span class="hljs-number">17</span>)
    at EventEmitter.addListener (events.js:<span class="hljs-number">401</span>:<span class="hljs-number">10</span>)
    at EventEmitter.repeatFn (C:\Users\XJY\Desktop\test\nodejs\events\events.js:<span class="hljs-number">30</span>:<span class="hljs-number">10</span>)
    at EventEmitter.emit (events.js:<span class="hljs-number">322</span>:<span class="hljs-number">22</span>)
    at <span class="hljs-built_in">Object</span>.<anonymous> (C:\Users\XJY\Desktop\test\nodejs\events\events.js:<span class="hljs-number">36</span>:<span class="hljs-number">6</span>)
    at Module._compile (internal/modules/cjs/loader.js:<span class="hljs-number">1156</span>:<span class="hljs-number">30</span>)
    at <span class="hljs-built_in">Object</span>.Module._extensions..js (internal/modules/cjs/loader.js:<span class="hljs-number">1176</span>:<span class="hljs-number">10</span>)
    at Module.load (internal/modules/cjs/loader.js:<span class="hljs-number">1000</span>:<span class="hljs-number">32</span>)
    at <span class="hljs-built_in">Function</span>.Module._load (internal/modules/cjs/loader.js:<span class="hljs-number">899</span>:<span class="hljs-number">14</span>)
    at <span class="hljs-built_in">Function</span>.executeUserEntryPoint [<span class="hljs-keyword">as</span> runMain] (internal/modules/run_main.js:<span class="hljs-number">74</span>:<span class="hljs-number">12</span>) &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'MaxListenersExceededWarning'</span>,
  <span class="hljs-attr">emitter</span>: EventEmitter &#123;
    <span class="hljs-attr">_events</span>: [<span class="hljs-built_in">Object</span>: <span class="hljs-literal">null</span> prototype] &#123; <span class="hljs-attr">repeat</span>: [<span class="hljs-built_in">Array</span>] &#125;,
    <span class="hljs-attr">_eventsCount</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">_maxListeners</span>: <span class="hljs-number">5</span>,
    [<span class="hljs-built_in">Symbol</span>(kCapture)]: <span class="hljs-literal">false</span>
  &#125;,
  <span class="hljs-attr">type</span>: <span class="hljs-string">'repeat'</span>,
  <span class="hljs-attr">count</span>: <span class="hljs-number">6</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-n5q8b" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h1 data-id="heading-7">二、nodejs之process模块</h1>
<p>在开始这个模块的介绍时，我们需要了解一下并发和并行、进程和线程的知识
<a name="user-content-VkTly" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-8">1、并发和并行</h2>
<p><a name="user-content-tW4jR" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-9">（1）并发</h3>
<p>并发(concurrency)：指在同一时刻只能有一条指令执行，但多个进程指令被快速的轮换执行，使得在宏观上具有多个进程同时执行的效果，但在微观上并不是同时执行的，只是把时间分成若干段，使多个进程快速交替的执行。如下图所示：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62cd94d69af949c3b4390eee841bab35~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-k1rHX" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-10">（2）并行</h3>
<p>并行(parallel)：指在同一时刻，有多条指令在多个处理器上同时执行。所以无论从微观还是从宏观来看，二者都是一起执行的。如下图所示：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/424e97f64d6c42e5972ded42bbae8bfc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-ZQgcW" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-11">（3）并发和并发在不同处理器系统</h3>
<p>并行在多处理器系统中存在，而并发可以在单处理器和多处理器系统中都存在。<br>并发能够在单处理器系统中存在是因为并发是并行的假象，并行要求程序能够同时执行多个操作，而并发只是要求程序假装同时执行多个操作（每个小时间片执行一个操作，多个操作快速切换执行）。<br>当有多个线程在操作时，如果系统只有一个 CPU，则它根本不可能真正同时进行一个以上的线程，它只能把 CPU 运行时间划分成若干个时间段，再将时间段分配给各个线程执行，在一个时间段的线程代码运行时,其它线程处于挂起状态.这种方式我们称之为并发（Concurrent）。<br>当系统有一个以上 CPU 时，则线程的操作有可能非并发。当一个 CPU 执行一个线程时，另一个 CPU 可以执行另一个线程，两个线程互不抢占 CPU 资源，可以同时进行，这种方式我们称之为并行（Parallel）。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/408616d90697450f9bfba2a4f13a0a0c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-PJhGV" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-12">2、进程和线程</h2>
<p>早期在单核 CPU 的系统中，为了实现多任务的运行，引入了进程的概念，不同的程序运行在数据与指令相互隔离的进程中，通过时间片轮转调度执行，由于 CPU 时间片切换与执行很快，所以看上去像是在同一时间运行了多个程序。<br>由于进程切换时需要保存相关硬件现场、进程控制块等信息，所以系统开销较大。为了进一步提高系统吞吐率，在同一进程执行时更充分的利用 CPU 资源，引入了线程的概念。线程是操作系统调度执行的最小单位，它们依附于进程中，共享同一进程中的资源，基本不拥有或者只拥有少量系统资源，切换开销极小。
<a name="user-content-vwuWw" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-13">（1）进程</h3>
<p>进程（Process）是计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统结构的基础，进程是线程的容器。<br>我们启动一个服务、运行一个实例，就是开一个服务进程，例如 Java 里的 JVM 本身就是一个进程，Node.js 里通过 node app.js 开启一个服务进程，多进程就是进程的复制（fork），fork 出来的每个进程都拥有自己的独立空间地址、数据栈，一个进程无法访问另外一个进程里定义的变量、数据结构，只有建立了 IPC 通信，进程之间才可数据共享。<br>下面以一个简单的例子来说明一下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);

http.createServer().listen(<span class="hljs-number">3000</span>, <span class="hljs-function">() =></span> &#123;
    process.title = <span class="hljs-string">'自定义进程名称'</span> <span class="hljs-comment">// 进程进行命名</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`process.pid: `</span>, process.pid); 
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">在node index.js后，可以在任务管理器（windows）看到该进程的一些信息，证明该进程正在运行中<br />![](https://cdn.nlark.com/yuque/0/2021/png/581334/1625623677066-2319b71e-4b2b-45d2-a352-424a125f6947.png#clientId=uc4f9fb11-bf2e-4&from=paste&id=u4cd2fd35&margin=%5Bobject%20Object%5D&originHeight=325&originWidth=863&originalType=url&ratio=1&status=done&style=stroke&taskId=u10843aaf-8eb3-4e02-b3c8-58271d25905)<br />![](https://cdn.nlark.com/yuque/0/2021/png/581334/1625623683704-e07eca72-95a1-4e69-ab07-ca62fe539c41.png#clientId=uc4f9fb11-bf2e-4&from=paste&id=u4e6a1865&margin=%5Bobject%20Object%5D&originHeight=151&originWidth=451&originalType=url&ratio=1&status=done&style=stroke&taskId=ub44c3bcb-a45d-4a71-9e45-63d49cb40fa)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-YxAr6" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-14">（2）线程</h3>
<p>线程是操作系统能够进行运算调度的最小单位，首先我们要清楚线程是隶属于进程的，被包含于进程之中。一个线程只能隶属于一个进程，但是一个进程是可以拥有多个线程的。<br>同一块代码，可以根据系统CPU核心数启动多个进程，每个进程都有属于自己的独立运行空间，进程之间是不相互影响的。同一进程中的多条线程将共享该进程中的全部系统资源，如虚拟地址空间，文件描述符和信号处理等。但同一进程中的多个线程有各自的调用栈（call stack），自己的寄存器环境（register context），自己的线程本地存储（thread-local storage)，线程又有单线程和多线程之分，具有代表性的 JavaScript、Java 语言。
<a name="user-content-rgfvX" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-15">a、单线程</h4>
<p>单线程就是一个进程只开一个线程，想象一下一个痴情的少年，对一个妹子一心一意用情专一。<br>Javascript 就是属于单线程，程序顺序执行，可以想象一下队列，前面一个执行完之后，后面才可以执行，当你在使用单线程语言编码时切勿有过多耗时的同步操作，否则线程会造成阻塞，导致后续响应无法处理。你如果采用 Javascript 进行编码，尽可能的使用异步操作。<br>下面是一个同步阻塞的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// compute.js</span>
<span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);
<span class="hljs-keyword">const</span> [url, port] = [<span class="hljs-string">'127.0.0.1'</span>, <span class="hljs-number">3000</span>];

<span class="hljs-keyword">const</span> computation = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>;
    <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'计算开始'</span>);
    <span class="hljs-built_in">console</span>.time(<span class="hljs-string">'计算耗时'</span>);

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">1e10</span>; i++) &#123;
        sum += i
    &#125;;

    <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'计算结束'</span>);
    <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'计算耗时'</span>);
    <span class="hljs-keyword">return</span> sum;
&#125;;

<span class="hljs-keyword">const</span> server = http.createServer(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-keyword">if</span>(req.url == <span class="hljs-string">'/compute'</span>)&#123;
        <span class="hljs-keyword">const</span> sum = computation();

        res.end(<span class="hljs-string">`Sum is <span class="hljs-subst">$&#123;sum&#125;</span>`</span>);
    &#125;

    res.end(<span class="hljs-string">`ok`</span>);
&#125;);

server.listen(port, url, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`server started at http://<span class="hljs-subst">$&#123;url&#125;</span>:<span class="hljs-subst">$&#123;port&#125;</span>`</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">浏览器执行 http://127.0.0.1:3000/compute ，大约每次需要 11496.275ms，也就意味下次用户请求需要等待 11496.275ms：<br />![](https://cdn.nlark.com/yuque/0/2021/png/581334/1625623865789-3b6fa476-167d-40f0-9d07-86e0eeddf761.png#clientId=uc4f9fb11-bf2e-4&from=paste&id=u647357a9&margin=%5Bobject%20Object%5D&originHeight=102&originWidth=614&originalType=url&ratio=1&status=done&style=none&taskId=u7a38f6b4-d956-43ea-b9cf-aba638a0b30)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-l7QYz" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-16">b、多线程</h4>
<p>多线程就是没有一个进程只开一个线程的限制，好比一个风流少年除了爱慕自己班的某个妹子，还在想着隔壁班的漂亮妹子。Java 就是多线程编程语言的一种，可以有效避免代码阻塞导致的后续请求无法处理。<br>对于多线程的说明 Java 是一个很好的例子，看以下代码示例</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestApplication</span> </span>&#123;
    Integer count = <span class="hljs-number">0</span>;

    <span class="hljs-meta">@GetMapping("/test")</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Integer <span class="hljs-title">Test</span><span class="hljs-params">()</span> </span>&#123;
        count += <span class="hljs-number">1</span>;
        <span class="hljs-keyword">return</span> count;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        SpringApplication.run(TestApplication.class, args);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">运行结果，每次执行都会修改count值，所以，多线程中任何一个变量都可以被任何一个线程所修改。<br />我现在对上述代码做下修改将 count 定义在 test 方法里
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestApplication</span> </span>&#123;
    <span class="hljs-meta">@GetMapping("/test")</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Integer <span class="hljs-title">Test</span><span class="hljs-params">()</span> </span>&#123;
        Integer count = <span class="hljs-number">0</span>; <span class="hljs-comment">// 改变定义位置</span>
        count += <span class="hljs-number">1</span>;
        <span class="hljs-keyword">return</span> count;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        SpringApplication.run(TestApplication.class, args);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">运行结果每次都是 1，因为每个线程都拥有了自己的执行栈
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-q6o5Z" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-17">c、nodejs是单线程吗？</h4>
<p>Node 严格意义讲并非只有一个线程，通常说的 “Node 是单线程” 其实是指 JS 的执行主线程只有一个。<br>我们以一个简单的例子来看一下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>).createServer(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  res.writeHead(<span class="hljs-number">200</span>);
  res.end(<span class="hljs-string">'Hello World'</span>);
&#125;).listen(<span class="hljs-number">8000</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'process id'</span>, process.pid);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">终端打印结果如下：<br />![](https://cdn.nlark.com/yuque/0/2021/png/581334/1625624150014-999a12e6-f9ef-4f73-ba5c-52f7ca95776d.png#clientId=uc4f9fb11-bf2e-4&from=paste&id=u5bcb9547&margin=%5Bobject%20Object%5D&originHeight=101&originWidth=512&originalType=url&ratio=1&status=done&style=none&taskId=ua0ab1bf3-af46-45d1-9159-1e2df6c495e)<br />这样我们根据pid可以在任务管理器（windows）找到对应的进程和线程数<br />![](https://cdn.nlark.com/yuque/0/2021/png/581334/1625624176480-51c12d1c-8d18-4873-9aed-0fdf5b7b2591.png#clientId=uc4f9fb11-bf2e-4&from=paste&id=uffc851fd&margin=%5Bobject%20Object%5D&originHeight=133&originWidth=781&originalType=url&ratio=1&status=done&style=stroke&taskId=u76385d92-5437-4bc2-b8f3-f3f15eb1b17)<br />上图可以证实node进程中的线程并不是只有一个，事实上一个node进程通常包含以下线程：
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>1 个 Javascript 执行主线程</li>
<li>1 个 watchdog 监控线程用于处理调试信息</li>
<li>1 个 v8 task scheduler 线程用于调度任务优先级，加速延迟敏感任务执行</li>
<li>4 个 v8 线程，主要用来执行代码调优与 GC 等后台任务</li>
<li>用于异步 I/O 的 libuv 线程池</li>
</ul>
<p>如果执行程序中不包含 I/O 操作如文件读写等，则默认线程池大小为 0，否则 Node 会初始化大小为 4 的异步 I/O 线程池，当然我们也可以通过process.env.UV_THREADPOOL_SIZE 自己设定线程池大小，需要注意的是在 Node 中网络 I/O 并不占用线程池。<br>下图为node的进程结构图：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cf5b3b3f04e4cc0bec54deb52b2e6ee~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>既然 JS 执行线程只有一个，那么 Node 为什么还能支持较高的并发（异步调用函数）？<br>1、从上文异步 I/O 我们也能获得一些思路，Node 进程中通过 libuv 实现了一个事件循环机制（uv_event_loop），当执行主线程发生阻塞事件，如 I/O 操作时，主线程会将耗时的操作放入事件队列中，然后继续执行后续程序。<br>2、uv_event_loop 尝试从 libuv 的线程池（uv_thread_pool）中取出一个空闲线程去执行队列中的操作，执行完毕获得结果后，通知主线程，主线程执行相关回调，并且将线程实例归还给线程池。通过此模式循环往复，来保证非阻塞 I/O，以及主线程的高效执行。<br>相关流程可参照下图：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eecbf3a5068046f6b14c8b1650c39185~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-RYER0" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-18">d、线程池</h4>
<p>1、线程池是预先创建好的吗？<br>线程池中的线程是按需创建的，在上面的例子中加入文件读取的代码段：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);

http.createServer(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  fs.readFile(<span class="hljs-string">'./compute.js'</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (err) &#123;
      <span class="hljs-built_in">console</span>.log(err);
      process.exit();
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Date</span>.now(), <span class="hljs-string">'Read File I/O'</span>);
    &#125;
  &#125;);
  res.writeHead(<span class="hljs-number">200</span>);
  res.end(<span class="hljs-string">'Hello World'</span>);
&#125;).listen(<span class="hljs-number">8000</span>);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'process id'</span>, process.pid);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">在没进行访问前，node的线程数为8，一旦访问8000端口，线程数就会变为12，如下图所示，这说明了大小为4的线程池被创建<br />![](https://cdn.nlark.com/yuque/0/2021/png/581334/1625625853322-e30f08ce-f242-4d9a-b9a2-023eb93e6666.png#clientId=uc4f9fb11-bf2e-4&from=paste&id=ua86aa6c2&margin=%5Bobject%20Object%5D&originHeight=113&originWidth=607&originalType=url&ratio=1&status=done&style=stroke&taskId=u34e175fe-9a34-4120-ab08-002eef5acbe)<br />![](https://cdn.nlark.com/yuque/0/2021/png/581334/1625625862637-f2f7ec73-7518-4bf2-8274-17222805b6db.png#clientId=uc4f9fb11-bf2e-4&from=paste&id=u9578faea&margin=%5Bobject%20Object%5D&originHeight=79&originWidth=741&originalType=url&ratio=1&status=done&style=stroke&taskId=u54854e60-0851-4d0a-8579-462ba521040)<br />​
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、异步I/O都要占用线程池吗？<br>并不是，网络IO不会占用线程池。无论多少次访问都不会创建线程，代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);

http.createServer(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  http.get(<span class="hljs-string">'https://www.baidu.com/'</span>);
  res.end(<span class="hljs-string">'hello'</span>);
&#125;).listen(<span class="hljs-number">8000</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'server is listening: '</span> + <span class="hljs-number">8000</span>);
&#125;);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'process id'</span>, process.pid);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9297c2b4f98847a4975280e9591ac7eb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>3、文件I/O一定会占用线程池吗？<br>并不是，*Sync会阻塞主线程所以不会占用线程池，另外fs.FSWatcher也不会占用线程池。<br>​</p>
<p>4、线程池只能用于异步IO？<br>并不是，除了一些IO密集操作外，Node.js对一些CPU密集的操作也会放到线程池里面执行(Crypto、Zlib模块)<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbb07454f7d4403c8b9bf051b0fda85d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-sKQ8U" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-19">3、process的相关API</h2>
<p>Node.js 中的进程 Process 是一个全局对象，无需 require 直接使用，给我们提供了当前进程中的相关信息，官方文档提供了详细的说明，下面罗列一些常用的变量、方法和事件。</p>
<ul>
<li>process.env：环境变量，例如通过 process.env.NODE_ENV 获取不同环境项目配置信息</li>
<li>process.nextTick：这个在系列（2）中详细介绍过，有兴趣的小伙伴可以回去看一下，这主要是运用在事件循环中</li>
<li>process.pid：获取当前进程id</li>
<li>process.ppid：当前进程对应的父进程</li>
<li>process.cwd()：获取当前进程工作目录</li>
<li>process.platform：获取当前进程运行的操作系统平台</li>
<li>process.title：指定进程名称，有的时候需要给进程指定一个名称</li>
</ul>
<p><a name="user-content-ZjD0K" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-20">（1）process事件</h3>
<p><a name="user-content-Ey7NH" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-21">a、beforeExit</h4>
<p>当 Node.js 清空其事件循环并且没有额外的工作要安排时，则会触发 'beforeExit' 事件。 通常情况下，Node.js 进程会在没有工作调度时退出，但是注册在 'beforeExit' 事件上的监听器可以进行异步调用，从而导致 Node.js 进程继续。<br>对于导致显式终止的条件，例如调用 process.exit() 或未捕获的异常，则不会触发 'beforeExit' 事件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">process.on(<span class="hljs-string">'beforeExit'</span>, <span class="hljs-function">(<span class="hljs-params">code</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Process beforeExit event with code: '</span>, code);
&#125;);

process.on(<span class="hljs-string">'exit'</span>, <span class="hljs-function">(<span class="hljs-params">code</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Process exit event with code: '</span>, code);
&#125;);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'This message is displayed first.'</span>);

<span class="hljs-comment">// 打印:</span>
<span class="hljs-comment">// This message is displayed first.</span>
<span class="hljs-comment">// Process beforeExit event with code: 0</span>
<span class="hljs-comment">// Process exit event with code: 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-DCYgF" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-22">b、disconnect</h4>
<p>如果 Node.js 进程是通过 IPC 通道衍生的（参考子进程和集群文档），则在 IPC 通道关闭时将触发 'disconnect' 事件。
<a name="user-content-iZi2M" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-23">c、exit</h4>
<p>当 Node.js 进程由于以下任一原因即将退出时，则会触发 'exit' 事件：</p>
<ul>
<li>process.exit() 方法被显式调用；</li>
<li>Node.js 事件循环不再需要执行任何额外的工作。</li>
</ul>
<p>此时没有办法阻止事件循环的退出，一旦所有 'exit' 监听器都运行完毕，则 Node.js 进程将终止<br>监听器函数必须只执行同步操作。 Node.js 进程将在调用 'exit' 事件监听器后立即退出，从而导致任何仍在事件循环中排队的额外工作被放弃。 例如，在以下示例中，永远不会发生超时：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">process.on(<span class="hljs-string">'exit'</span>, <span class="hljs-function">(<span class="hljs-params">code</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'This will not run'</span>);
  &#125;, <span class="hljs-number">0</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-zCQOO" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-24">d、mesage</h4>
<p>如果 Node.js 进程是通过 IPC 通道衍生的（参考子进程和集群文档），则每当子进程收到父进程使用 childprocess.send() 发送的消息时，就会触发 'message' 事件
<a name="user-content-cREkq" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h4 data-id="heading-25">e、异常事件监听</h4>
<p>nodejs使用rejectionHandled、uncaughtException、uncaughtExceptionMonitor、unhandledRejection、warning等事件来监听异常情况，有兴趣的小伙伴可以根据官网例子尝试一下<br></p>
<p><a name="user-content-ZOClD" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h1 data-id="heading-26">三、nodejs之child_process模块</h1>
<p><a name="user-content-VjAK5" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-27">1、为什么使用多进程</h2>
<p>上面说到，通过事件循环机制，Node 实现了在 I/O 密集型（I/O-Sensitive）场景下的高并发，但是如果代码中遇到 CPU 密集场景（CPU-Sensitive）的场景，那么主线程将长时间阻塞，无法处理额外的请求。为了应对 CPU-Sensitive 场景，以及充分发挥 CPU 多核性能，Node 提供了 child_process 模块进行子进程的创建、通信、销毁等等。<br>父进程与子进程之间是一种 master/worker 的工作模式。通常会阻塞的操作分发给 worker 来执行（查 db，读文件，进程耗时的计算等等），master 上尽量编写非阻塞的代码。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7da6c9770ec4918948277e92da791e6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-AsiTt" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-28">2、CPU密集型和IO密集型</h2>
<p>下面简单介绍一下上面提及的CPU密集型和IO密集型的概念
<a name="user-content-VBeoC" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-29">（1）CPU密集型（CPU-bound）</h3>
<p>CPU密集型也叫计算密集型，指的是系统的硬盘、内存性能相对CPU要好很多，此时，系统运作大部分的状况是CPU Loading 100%，CPU要读/写I/O(硬盘/内存)，I/O在很短的时间就可以完成，而CPU还有许多运算要处理，CPU Loading很高。<br>在多重程序系统中，大部份时间用来做计算、逻辑判断等CPU动作的程序称之CPU bound。例如一个计算圆周率至小数点一千位以下的程序，在执行的过程当中绝大部份时间用在三角函数和开根号的计算，便是属于CPU bound的程序。<br>CPU bound的程序一般而言CPU占用率相当高。这可能是因为任务本身不太需要访问I/O设备，也可能是因为程序是多线程实现因此屏蔽掉了等待I/O的时间。
<a name="user-content-ZssrM" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-30">（2）IO密集型（I/O bound）</h3>
<p>IO密集型指的是系统的CPU性能相对硬盘、内存要好很多，此时，系统运作，大部分的状况是CPU在等I/O (硬盘/内存) 的读/写操作，此时CPU Loading并不高。<br>I/O bound的程序一般在达到性能极限时，CPU占用率仍然较低。这可能是因为任务本身需要大量I/O操作，而pipeline做得不是很好，没有充分利用处理器能力。
<a name="user-content-Da1yz" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-31">（3）CPU密集型 vs IO密集型</h3>
<p>我们可以把任务分为计算密集型（CPU密集型）和IO密集型。</p>
<ul>
<li>计算密集型</li>
</ul>
<p>计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。<br>计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。</p>
<ul>
<li>IO密集型</li>
</ul>
<p>涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。<br>IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。
<a name="user-content-cOuez" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-32">3、child_process的相关API</h2>
<p>child_process提供了4个方法，用于新建子进程，这4个方法分别为spawn、execFile、exec和fork。所有的方法都是异步的，可以用一张图来描述这4个方法的区别。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57cddfca659546cf89a8a0b8a6837740~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>spawn ： 子进程中执行的是非node程序，提供一组参数后，执行的结果以流的形式返回。</li>
<li>execFile：子进程中执行的是非node程序，提供一组参数后，执行的结果以回调的形式返回。</li>
<li>exec：子进程执行的是非node程序，传入一串shell命令，执行后结果以回调的形式返回，与execFile，不同的是exec可以直接执行一串shell命令。</li>
<li>fork：子进程执行的是node程序，提供一组参数后，执行的结果以流的形式返回，与spawn不同，fork生成的子进程只能执行node应用。接下来的小节将具体的介绍这一些方法。</li>
</ul>
<p><a name="user-content-oSPwU" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-33">（1）execFile 和 exec</h3>
<p>这两者的相同点为：执行的是非node应用，且执行后的结果以回调函数的形式返回；<br>不同点为：exec是直接执行的一段shell命令，而execFile是执行的一个应用；<br>举例来说，echo是UNIX系统的一个自带命令，我们直接可以在命令行执行：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">echo hello world
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">结果，在命令行中会打印出hello world<br />通过exec来实现：
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> cp=<span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>);
cp.exec(<span class="hljs-string">'echo hello world'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err,stdout</span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(stdout);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">执行这段代码，结果会输出hello world。我们发现exec的第一个参数，跟shell命令完全相似。<br />通过execFile来实现：
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> cp=<span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>);
cp.execFile(<span class="hljs-string">'echo'</span>,[<span class="hljs-string">'hello'</span>,<span class="hljs-string">'world'</span>],<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err,stdout</span>)</span>&#123;
   <span class="hljs-built_in">console</span>.log(stdout);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在windows上运行这段代码，却告诉我们出了错误：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-built_in">Error</span>: spawn echo ENOENT
    at Process.ChildProcess._handle.onexit (internal/child_process.js:<span class="hljs-number">267</span>:<span class="hljs-number">19</span>)
    at onErrorNT (internal/child_process.js:<span class="hljs-number">469</span>:<span class="hljs-number">16</span>)
    at processTicksAndRejections (internal/process/task_queues.js:<span class="hljs-number">84</span>:<span class="hljs-number">21</span>) &#123;
  <span class="hljs-attr">errno</span>: <span class="hljs-string">'ENOENT'</span>,
  <span class="hljs-attr">code</span>: <span class="hljs-string">'ENOENT'</span>,
  <span class="hljs-attr">syscall</span>: <span class="hljs-string">'spawn echo'</span>,
  <span class="hljs-attr">path</span>: <span class="hljs-string">'echo'</span>,
  <span class="hljs-attr">spawnargs</span>: [ <span class="hljs-string">'hello'</span>, <span class="hljs-string">'world'</span> ],
  <span class="hljs-attr">cmd</span>: <span class="hljs-string">'echo hello world'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">这是因为在windows上执行时，execlFile和spawn都是脱离cmd.exe这一解释器去单独执行的，为此，我们可以根据操作系统设置shell：true以隐式调用cmd
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> childProcess = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>);
childProcess.execFile(<span class="hljs-string">'echo'</span>, [<span class="hljs-string">'hello'</span>, <span class="hljs-string">'world'</span>], &#123;
  <span class="hljs-attr">shell</span>: process.platform === <span class="hljs-string">'win32'</span>
&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err,stdout</span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(stdout);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，在命令行中会打印出hello world
<a name="user-content-Lq6c3" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-34">（2）spawn</h3>
<p>spawn同样是用于执行非node应用，且不能直接执行shell，与execFile相比，spawn执行应用后的结果并不是执行完成后，一次性的输出的，而是以流的形式输出。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">const</span> childProcess = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>);
<span class="hljs-keyword">const</span> newRead = childProcess.spawn(<span class="hljs-string">'type'</span>, [<span class="hljs-string">'..\\txt\\spawn.txt'</span>], &#123;
  <span class="hljs-attr">shell</span>: process.platform === <span class="hljs-string">'win32'</span>,
&#125;);

newRead.stdout.on(<span class="hljs-string">"data"</span>, <span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> str = result.toString(<span class="hljs-string">'utf-8'</span>);
  <span class="hljs-built_in">console</span>.log(str);
&#125;)

<span class="hljs-comment">// txt/spawn.txt</span>
<span class="hljs-comment">// 文件内容为：acdgetadgh</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">通过控制台可以看到，输出内容正是txt文件的内容
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-sZ19P" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-35">（3）fork</h3>
<p>在javascript中，在处理大量计算的任务方面，HTML里面通过web work来实现，使得任务脱离了主线程。在node中使用了一种内置于父进程和子进程之间的通信来处理该问题，降低了大数据运行的压力。node中提供了fork方法，通过fork方法在单独的进程中执行node程序，并且通过父子间的通信，子进程接受父进程的信息，并将执行后的结果返回给父进程。<br>使用fork方法，可以在父进程和子进程之间开放一个IPC通道，使得不同的node进程间可以进行消息通信。<br>在子进程中：通过process.on('message')和process.send()的机制来接收和发送消息。<br>在父进程中：通过child.on('message')和child.send()的机制来接收和发送消息</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// father.js</span>
<span class="hljs-keyword">const</span> &#123; fork &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>);
<span class="hljs-keyword">const</span> child = fork(<span class="hljs-string">'./fib.js'</span>); <span class="hljs-comment">// 创建子进程</span>
child.send(&#123; <span class="hljs-attr">num</span>: <span class="hljs-number">44</span> &#125;); <span class="hljs-comment">// 将任务执行数据通过信道发送给子进程</span>
child.on(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-params">message</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'receive from child process, calculate result: '</span>, message.data);
  child.kill();
&#125;);
child.on(<span class="hljs-string">'exit'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'child process exit'</span>);
&#125;);
<span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123; <span class="hljs-comment">// 主进程继续执行</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'continue excute javascript code'</span>, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getSeconds());
&#125;, <span class="hljs-number">1000</span>);


<span class="hljs-comment">// fib.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fib</span>(<span class="hljs-params">num</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (num === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
  <span class="hljs-keyword">if</span> (num === <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
  <span class="hljs-keyword">return</span> fib(num - <span class="hljs-number">2</span>) + fib(num - <span class="hljs-number">1</span>);
&#125;
process.on(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-params">msg</span> =></span> &#123; <span class="hljs-comment">// 获取主进程传递的计算数据</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'child pid'</span>, process.pid);
  <span class="hljs-keyword">const</span> &#123; num &#125; = msg;
  <span class="hljs-keyword">const</span> data = fib(num);
  process.send(&#123; data &#125;); <span class="hljs-comment">// 将计算结果发送主进程</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">最后的输出结果是：
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">child pid <span class="hljs-number">39974</span>
<span class="hljs-keyword">continue</span> excute javascript code <span class="hljs-number">41</span>
<span class="hljs-keyword">continue</span> excute javascript code <span class="hljs-number">42</span>
<span class="hljs-keyword">continue</span> excute javascript code <span class="hljs-number">43</span>
<span class="hljs-keyword">continue</span> excute javascript code <span class="hljs-number">44</span>
receive <span class="hljs-keyword">from</span> child process, calculate result:  <span class="hljs-number">1134903170</span>
child process exit
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-WYRTW" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-36">（4）同步执行的子进程</h3>
<p>exec、execFile、spawn和fork执行的子进程都是默认异步的，子进程的运行不会阻塞主进程。除此之外，child_process模块同样也提供了execFileSync、spawnSync和execSync来实现同步的方式执行子进程。
<a name="user-content-skd7a" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-37">（5）单进程 vs 多进程</h3>
<p>下面我们通过两次计算斐波那契数列某一项的数值来验算：</p>
<ul>
<li>单进程</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fib</span>(<span class="hljs-params">num</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (num === <span class="hljs-number">0</span> || num === <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> num;
  <span class="hljs-keyword">return</span> fib(num - <span class="hljs-number">2</span>) + fib(num - <span class="hljs-number">1</span>);
&#125;
<span class="hljs-keyword">const</span> startTime = <span class="hljs-built_in">Date</span>.now();
<span class="hljs-keyword">const</span> calcNumArr = [<span class="hljs-number">41</span>, <span class="hljs-number">42</span>, <span class="hljs-number">43</span>, <span class="hljs-number">44</span>, <span class="hljs-number">45</span>, <span class="hljs-number">46</span>];
<span class="hljs-keyword">const</span> totalcount = calcNumArr.length;
<span class="hljs-keyword">let</span> completedCount = <span class="hljs-number">0</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < totalcount; i++) &#123;
  <span class="hljs-keyword">const</span> result = fib(calcNumArr[i]);
  completedCount++;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`process: <span class="hljs-subst">$&#123;completedCount&#125;</span>/<span class="hljs-subst">$&#123;totalcount&#125;</span>, result is：<span class="hljs-subst">$&#123;result&#125;</span>`</span>);
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`访问完成：用时：<span class="hljs-subst">$&#123;<span class="hljs-built_in">Date</span>.now() - startTime&#125;</span>ms`</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后终端输出结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">process: <span class="hljs-number">1</span>/<span class="hljs-number">6</span>, result is：<span class="hljs-number">165580141</span>
<span class="hljs-attr">process</span>: <span class="hljs-number">2</span>/<span class="hljs-number">6</span>, result is：<span class="hljs-number">267914296</span>
<span class="hljs-attr">process</span>: <span class="hljs-number">3</span>/<span class="hljs-number">6</span>, result is：<span class="hljs-number">433494437</span>
<span class="hljs-attr">process</span>: <span class="hljs-number">4</span>/<span class="hljs-number">6</span>, result is：<span class="hljs-number">701408733</span>
<span class="hljs-attr">process</span>: <span class="hljs-number">5</span>/<span class="hljs-number">6</span>, result is：<span class="hljs-number">1134903170</span>
<span class="hljs-attr">process</span>: <span class="hljs-number">6</span>/<span class="hljs-number">6</span>, result is：<span class="hljs-number">1836311903</span>
访问完成：用时：60215ms
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>多进程</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//father.js</span>
<span class="hljs-keyword">const</span> &#123; fork &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>);
<span class="hljs-keyword">const</span> numCPUs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"os"</span>).cpus().length;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'cpu为'</span> + numCPUs + <span class="hljs-string">'核'</span>);
<span class="hljs-keyword">const</span> startTime = <span class="hljs-built_in">Date</span>.now();
<span class="hljs-keyword">const</span> fibNumArr = [<span class="hljs-number">41</span>, <span class="hljs-number">42</span>, <span class="hljs-number">43</span>, <span class="hljs-number">44</span>, <span class="hljs-number">45</span>, <span class="hljs-number">46</span>];
<span class="hljs-keyword">const</span> totalTask = fibNumArr.length;
<span class="hljs-keyword">let</span> completedTask = <span class="hljs-number">0</span>;
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < totalTask; i++) &#123;
  <span class="hljs-keyword">const</span> child = fork(<span class="hljs-string">'./child.js'</span>);
  child.send(&#123; <span class="hljs-attr">num</span>: fibNumArr[i] &#125;);
  child.on(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-params">message</span> =></span> &#123;
    completedTask++;
    child.kill();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'receive from child process, calculate result: '</span> + message + <span class="hljs-string">'\n'</span> + <span class="hljs-string">'process: '</span> + completedTask + <span class="hljs-string">'/'</span> + totalTask);
    <span class="hljs-keyword">if</span>(completedTask >= totalTask) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'访问完成，用时：'</span> + (<span class="hljs-built_in">Date</span>.now() - startTime) + <span class="hljs-string">'ms'</span>)
    &#125;
  &#125;)
&#125;


<span class="hljs-comment">//child.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fib</span>(<span class="hljs-params">num</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (num === <span class="hljs-number">0</span> || num === <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> num;
  <span class="hljs-keyword">return</span> fib(num - <span class="hljs-number">2</span>) + fib(num - <span class="hljs-number">1</span>);
&#125;
process.on(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-params">message</span> =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; num &#125; = message;
  <span class="hljs-keyword">const</span> result = fib(num);
  process.send(result);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后终端输出结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cpu为<span class="hljs-number">6</span>核
receive <span class="hljs-keyword">from</span> child process, calculate result: <span class="hljs-number">165580141</span>
<span class="hljs-attr">process</span>: <span class="hljs-number">1</span>/<span class="hljs-number">6</span>
receive <span class="hljs-keyword">from</span> child process, calculate result: <span class="hljs-number">267914296</span>
<span class="hljs-attr">process</span>: <span class="hljs-number">2</span>/<span class="hljs-number">6</span>
receive <span class="hljs-keyword">from</span> child process, calculate result: <span class="hljs-number">433494437</span>
<span class="hljs-attr">process</span>: <span class="hljs-number">3</span>/<span class="hljs-number">6</span>
receive <span class="hljs-keyword">from</span> child process, calculate result: <span class="hljs-number">701408733</span>
<span class="hljs-attr">process</span>: <span class="hljs-number">4</span>/<span class="hljs-number">6</span>
receive <span class="hljs-keyword">from</span> child process, calculate result: <span class="hljs-number">1134903170</span>
<span class="hljs-attr">process</span>: <span class="hljs-number">5</span>/<span class="hljs-number">6</span>
receive <span class="hljs-keyword">from</span> child process, calculate result: <span class="hljs-number">1836311903</span>
<span class="hljs-attr">process</span>: <span class="hljs-number">6</span>/<span class="hljs-number">6</span>
访问完成，用时：24861ms
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的比较可以看到多进程情况下，cpu完成计算的速度要快得多。</p>
<h1 data-id="heading-38">END</h1>
<p>欢迎大家踊跃投稿，提出建议帮助前端周刊做得更好。
投稿方式：直接分享文章的链接给周刊组成员 邮箱：<a href="https://link.juejin.cn/?target=mailto%3Aspyro426%40163.com" target="_blank" title="mailto:spyro426@163.com" ref="nofollow noopener noreferrer">spyro426@163.com</a>；</p>
<blockquote>
<p>关于我们：我们是晓教育集团大教学前端团队，是一个年轻的团队。我们支持了集团几乎所有的教学业务。现伴随着事业群的高速发展，团队也在迅速扩张，欢迎各位前端高手加入我们~</p>
</blockquote>
<p>我们希望你是：技术上基础扎实、某领域深入；学习上善于沉淀、持续学习；性格上乐观开朗、活泼外向。
如有兴趣加入我们，欢迎发送简历至邮箱：</p>
<blockquote>
<ul>
<li><a href="https://link.juejin.cn/?target=mailto%3Aspyro426%40163.com" target="_blank" title="mailto:spyro426@163.com" ref="nofollow noopener noreferrer">spyro426@163.com</a>;</li>
<li><a href="https://link.juejin.cn/?target=mailto%3Aliushan%40xiao100.com" target="_blank" title="mailto:liushan@xiao100.com" ref="nofollow noopener noreferrer">liushan@xiao100.com</a>;</li>
<li><a href="https://link.juejin.cn/?target=mailto%3Ayangshuijuan%40xiao100.com" target="_blank" title="mailto:yangshuijuan@xiao100.com" ref="nofollow noopener noreferrer">yangshuijuan@xiao100.com</a>;</li>
</ul>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87cc3cddda0a46bea8337867bc8667c8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            