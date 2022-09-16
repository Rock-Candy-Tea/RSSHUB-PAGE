
---
title: 'vue2源码解析（四）：依赖收集'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f3c1203b83f44d9adfb8a1442ca2049~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 15 Sep 2022 23:07:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f3c1203b83f44d9adfb8a1442ca2049~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第1篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
<p><code>你好呀，我是小九，很高兴见到你。</code>
<br></p>
<h3 data-id="heading-0">摘要</h3>
<p>vue2源码学习之路。</p>
<p>查看之前的文章</p>
<p><a href="https://juejin.cn/post/7136055256122654734" target="_blank" title="https://juejin.cn/post/7136055256122654734">vue2源码解析（一）：环境搭建</a></p>
<p><a href="https://juejin.cn/post/7137574093147013157" target="_blank" title="https://juejin.cn/post/7137574093147013157">vue2源码解析（二）：数据劫持</a></p>
<p><a href="https://juejin.cn/post/7139754899121635364" target="_blank" title="https://juejin.cn/post/7139754899121635364">vue2源码解析（三）：从html模板到真实dom呈现全过程分析</a></p>
<br>
<p>在上一篇文章中，实现了从html模板到真实dom渲染的过程，简单回顾一下。</p>
<p>首先进行模板编译，将模板编译成ast语法树，然后将ast生成render函数。</p>
<p>调用render函数生成虚拟dom，最后再将虚拟dom转换成真实的dom。</p>
<p>整个过程中，有两个关键的函数，一是<code>_render</code>函数用于创建虚拟dom，<code>_update</code>函数负责将虚拟dom转成真实dom。</p>
<br>
<p>如果数据发生变化，视图也要随之变化，就要重新进行渲染。</p>
<p>此时就需要重新调用<code>_render</code>和<code>_update</code>函数。</p>
<p>通过手动调用<code>_render</code>函数和<code>_update</code>函数能够实现更新视图的效果</p>
<pre><code class="hljs language-ini copyable" lang="ini"><div <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span> class=<span class="hljs-string">"test"</span> style=<span class="hljs-string">"color: red"</span>>
    <div <span class="hljs-attr">class</span>=<span class="hljs-string">"number"</span>>&#123;&#123;a&#125;&#125;</div>
    <div>name: &#123;&#123;obj.name&#125;&#125;</div>
    <div>age: &#123;&#123;obj.age&#125;&#125;</div>
</div>

const <span class="hljs-attr">app</span> = new Vue(&#123;
    el: "<span class="hljs-comment">#app",</span>
    data: &#123;
        a: 100,
        obj: &#123;
            name: "tom",
            age: 10,
        &#125;,
    &#125;,
&#125;)<span class="hljs-comment">;</span>

setTimeout(() => &#123;
    <span class="hljs-attr">app.a</span> = <span class="hljs-number">20</span><span class="hljs-comment">;</span>
    <span class="hljs-attr">app.obj.name</span> = <span class="hljs-string">"小张"</span><span class="hljs-comment">;</span>
    <span class="hljs-attr">app.obj.age</span> =<span class="hljs-number">12</span><span class="hljs-comment">;</span>
    app._update(app._render())
&#125;, 1000)<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f3c1203b83f44d9adfb8a1442ca2049~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但实际上，不可能每次更新都手动调用<code>_render</code>和<code>_update</code>函数。</p>
<p>此时就需要实现数据的依赖收集，数据变化自动更新视图。</p>
<p>接下来就介绍一下如何实现自动更新。</p>
<br>
<h3 data-id="heading-1">项目结构</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ac73ce827074c4faeb0ccb11edc9707~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<h3 data-id="heading-2">vue更新策略</h3>
<p>先来了解一下vue的更新策略。</p>
<p><strong>vue更新策略是以组件为单位的</strong>，每个组件都有一个watcher，这个watcher也叫做渲染watcher。</p>
<p>组件中的属性变化后，就会调用当前组件对应的watcher，重新进行渲染。</p>
<p>而<strong>watcher的本质就是将渲染的逻辑封装起来</strong>，也就是<code>_render</code>和<code>_update</code>函数。</p>
<br>
<p>这里顺便说一句，为什么vue要组件化，面试中可能会问到。</p>
<blockquote>
<p>为什么要组件化，组件化的好处是什么？</p>
<p>一是复用，二是方便维护，三是局部更新</p>
</blockquote>
<br>
<h3 data-id="heading-3">封装Watcher</h3>
<h4 data-id="heading-4">1.封装<code>_render</code>和<code>_update</code></h4>
<p>在之前的代码中，<code>_render</code>和<code>_update</code>在挂载函数<code>mountComponent</code>中调用。</p>
<p>为了能够自动更新数据，这里，使用Watcher对这两个函数进行包装。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">mountComponent</span>(<span class="hljs-params">vm, el</span>) &#123;
    <span class="hljs-keyword">const</span> <span class="hljs-title function_">updateComponent</span> = (<span class="hljs-params"></span>) => &#123;
        vm.<span class="hljs-title function_">_update</span>(vm.<span class="hljs-title function_">_render</span>());
    &#125;;
    <span class="hljs-keyword">new</span> <span class="hljs-title class_">Watcher</span>(vm, updateComponent, <span class="hljs-function">() =></span> &#123;&#125;, &#123;&#125;, <span class="hljs-literal">true</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p>此时就需要一个Watcher类。</p>
<p>创建文件，路径src-->observer-->watcher.js，创建一个Watcher类。</p>
<h4 data-id="heading-5">2. 基本参数</h4>
<p>一个页面可能有很多组件，每一个组件都有一个watcher，因此每个watcher都需要添加一个唯一标识。</p>
<p>Watcher接收几个参数</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7b074c70c07419eadc563761c1666cf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>vm</code>：当前vue实例</p>
<p><code>expOrFn</code>：表达式或函数</p>
<p><code>cb</code>：回调函数，用于更新的函数</p>
<p><code>options</code>：选项</p>
<p><code>isRenderWatcher</code>：是不是渲染watcher，只是起了一个名字。</p>
<p>如果expOrFn是一个函数，就把这个函数放到getter上。</p>
<p>创建一个get函数，get函数用来执行getter。</p>
<p>get会默认执行一次，让页面渲染。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; observer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"."</span>;
<span class="hljs-keyword">import</span> &#123; isFunction &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../shared/until"</span>;

<span class="hljs-comment">// 每个watcher都添加一个唯一值</span>
<span class="hljs-keyword">let</span> uid = <span class="hljs-number">0</span>;

<span class="hljs-keyword">class</span> <span class="hljs-title class_">Watcher</span> &#123;
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params">vm, expOrFn, cb, options, isRenderWatcher</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">id</span> = ++uid; 
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">vm</span> = vm;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">cb</span> = cb;
        <span class="hljs-keyword">if</span> (<span class="hljs-title function_">isFunction</span>(expOrFn)) &#123;
            <span class="hljs-variable language_">this</span>.<span class="hljs-property">getter</span> = expOrFn;
        &#125;      
        
        <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">get</span>();
    &#125;
    <span class="hljs-title function_">get</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">getter</span>();
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">Watcher</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h3 data-id="heading-6">封装Dep</h3>
<p>一个页面有可能有多个组件，每个组件都有自己的数据，每个组件对应一个watcher，因此要将组件的数据和watcher绑定在一起。</p>
<br>
<p>有些数据在页面中使用了，有些数据没有使用，所以需要知道模板中使用了哪些属性。</p>
<p><strong>可以给模板中使用的每一个属性，增加一个收集器dep，目的就是收集watcher。</strong></p>
<h4 data-id="heading-7">1. dep和watcher的对应关系</h4>
<p>一个组件对应一个watcher，一个组件中有多个属性，一个属性对应一个dep，所以可能存在多个dep对应一个watcher。</p>
<p>一个属性可以在多个组件中使用，一个属性对应多个组件，所以可能存在一个dep对应多个watcher。</p>
<p><strong>dep和watcher之间是多对多的关系。</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f6f920e76e74b458fc13862493e3a1d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">2. 创建Dep类</h4>
<p>创建文件，路径src-->observer-->dep.js</p>
<p>dep可能有很多个，所以和watcher一样，需要一个唯一标识。</p>
<pre><code class="hljs language-ini copyable" lang="ini">let <span class="hljs-attr">uid</span> = <span class="hljs-number">0</span><span class="hljs-comment">;</span>

class Dep &#123;
    constructor() &#123;
        <span class="hljs-attr">this.id</span> = uid++<span class="hljs-comment">;</span>
    &#125;
&#125;
<span class="hljs-attr">Dep.target</span> = null<span class="hljs-comment">;</span>

export default Dep<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p>vue源码中借鉴了js的单线程模型。</p>
<p><strong>在Dep类上有一个target属性，用于保存当前渲染的watcher，渲染哪个watcher，就保存哪个，渲染完成之后，就把当前的target清空。</strong></p>
<p>注意，target不需要定义在Dep原型上，不是给实例用的，只是相当于定义了一个全局变量。</p>
<h4 data-id="heading-9">3.给属性添加dep</h4>
<p>在之前的代码中，有一个<code>defineReactive</code>函数，这个函数用来实现数据响应式，也就是数据劫持。</p>
<p>本质上是使用<code>Object.defineProperty</code>给每一个属性添加get和set方法。</p>
<p>获取数据就调用get方法，修改数据就调用set方法。</p>
<br>
<p>因此，可以在这个函数中给每个属性添加一个收集器<code>dep</code>，用于收集watcher。</p>
<p><strong>使用get方法取值时，进行依赖收集，使用set方法修改时，进行依赖更新。</strong></p>
<p>简单来说，当页面取值时，说明这个值用来渲染了，此时可以把watcher和属性对应起来。</p>
<p>当页面更新时，就调用watcher封装起来的<code>_render</code>和<code>_update</code>函数，重新渲染。</p>
<pre><code class="hljs language-scss copyable" lang="scss">export function <span class="hljs-built_in">defineReactive</span>(data, key, value) &#123;
    <span class="hljs-built_in">observer</span>(value);

    <span class="hljs-comment">// 给每个属性都添加一个dep</span>
    let dep = new <span class="hljs-built_in">Dep</span>();

    <span class="hljs-selector-tag">Object</span><span class="hljs-selector-class">.defineProperty</span>(data, key, &#123;
        // 取值时依赖收集
        get() &#123;
            if (Dep.target) &#123;
                dep<span class="hljs-selector-class">.depend</span>();
            &#125;
            return value;
        &#125;,
        <span class="hljs-comment">// 修改时依赖更新</span>
        <span class="hljs-built_in">set</span>(newValue) &#123;
            if (newValue === value) return;
            <span class="hljs-built_in">observer</span>(newValue);
            value = newValue;
           
            dep<span class="hljs-selector-class">.notify</span>();
        &#125;,
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">4. watcher和dep建立双向记忆</h4>
<p>上面的代码，如果<code>Dep.target</code>变量中，说明当前有一个渲染的watcher，那么就让dep记住当前的watcher。</p>
<pre><code class="hljs language-scss copyable" lang="scss">if (Dep.target) &#123;
    dep<span class="hljs-selector-class">.depend</span>();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用set后，数据更新，页面重新渲染。</p>
<pre><code class="hljs language-ini copyable" lang="ini">dep.notify()<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，需要在合适的时候，将当前的wathcer保存到全局变量Dep.target上。</p>
<br>
<p>前面封装watcher类时，watcher中有一个get方法，本质是调用渲染函数。</p>
<p>所以，需要在渲染之前，将watcher保存在全局变量<code>Dep.target</code>上，渲染完成后将这个变量清空。</p>
<pre><code class="hljs language-scss copyable" lang="scss">class Watcher &#123;
    ...
    <span class="hljs-built_in">get</span>() &#123;
        <span class="hljs-comment">// 将当前的watcher放到全局变量上</span>
        <span class="hljs-comment">// this是当前watcher实例</span>
        <span class="hljs-built_in">pushTarget</span>(this);

        <span class="hljs-comment">// 首先调用一次，让页面渲染</span>
        this<span class="hljs-selector-class">.getter</span>();

        <span class="hljs-comment">// 视图渲染完成后，清空这个值</span>
        <span class="hljs-built_in">popTarget</span>();
    &#125;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在src-->observer-->dep.js 中添加<code>pushTarget</code>函数和<code>popTarget</code>函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">pushTarget</span>(<span class="hljs-params">watcher</span>) &#123;
    <span class="hljs-title class_">Dep</span>.<span class="hljs-property">target</span> = watcher;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">popTarget</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-title class_">Dep</span>.<span class="hljs-property">target</span> = <span class="hljs-literal">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p>难点来了，如何让dep和watcher记住对方？</p>
<p>源码中的思路是，在Dep和Watcher类中分别创建一个保存的函数，调用对方的函数，同时将自己的实例传进去，并借助<code>Dep.target</code>这个中间变量。</p>
<p>如图所示</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d3e18fd3e914324a44c4c051c409cea~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<p>Dep类中添加<code>addSub</code>方法用于添加watcher</p>
<pre><code class="hljs language-perl copyable" lang="perl">addSub(<span class="hljs-function"><span class="hljs-keyword">sub</span>) </span>&#123;
    this.subs.push(<span class="hljs-function"><span class="hljs-keyword">sub</span>)</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加<code>depend</code>方法让watcher也记住dep。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title function_">depend</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-title class_">Dep</span>.<span class="hljs-property">target</span>.<span class="hljs-title function_">addDep</span>(<span class="hljs-variable language_">this</span>); 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p>Watcher类中添加<code>addDep</code>方法，记住dep。</p>
<p>这里有一点需要注意，如果页面中对于一个属性，使用了多次，每次使用，都让当前的watcher保存一次这个属性的dep，就会出现重复。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f79d9b67b934b3cbc01e63c8677ebf6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因此，就需要对dep去重。</p>
<p>源码中使用的是<code>Set</code>，先判断dep是否存在，再决定是否保存dep。</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-keyword">constructor</span>&#123;
    <span class="hljs-keyword">this</span>.deps = [];
    <span class="hljs-keyword">this</span>.depIds = new Set();
&#125;

addDep(dep) &#123;
    <span class="hljs-keyword">const</span> id = dep.id;
    <span class="hljs-keyword">if</span> (!<span class="hljs-keyword">this</span>.depIds.has(id)) &#123;
        <span class="hljs-keyword">this</span>.deps.push(dep);
        <span class="hljs-keyword">this</span>.depIds.add(id);
        dep.addSub(<span class="hljs-keyword">this</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，watcher和dep建立双向记忆完成。</p>
<h4 data-id="heading-11">5, 重新渲染</h4>
<p><code>defineReactive</code>这个函数中，get时调用了<code>dep.depend()</code>记住watcher，set时调用了<code>dep.notify()</code>重新渲染。</p>
<p><code>dep.notify()</code>的逻辑就是遍历subs中保存的所有watcher，调用watcher中的渲染方法。</p>
<br>
<p>在Dep类中添加<code>notify</code>函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title function_">notify</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">subs</span>.<span class="hljs-title function_">forEach</span>(<span class="hljs-function">(<span class="hljs-params">watcher</span>) =></span> watcher.<span class="hljs-title function_">update</span>());
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Watcher类中添加<code>update</code>函数，调用自身的get方法，重新渲染。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title function_">update</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">get</span>();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h3 data-id="heading-12">测试</h3>
<p>还是刚才的代码，这次可以实现自动更新</p>
<pre><code class="hljs language-ini copyable" lang="ini"><div <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span> class=<span class="hljs-string">"test"</span> style=<span class="hljs-string">"color: red"</span>>
<div <span class="hljs-attr">class</span>=<span class="hljs-string">"number"</span>>&#123;&#123;a&#125;&#125;</div>
<div>name: &#123;&#123;obj.name&#125;&#125;</div>
<div>age: &#123;&#123;obj.age&#125;&#125;</div>
</div>

<script>
const <span class="hljs-attr">app</span> = new Vue(&#123;
    el: "<span class="hljs-comment">#app",</span>
    data: &#123;
        a: 100,
        obj: &#123;
            name: "小明",
            age: 10,
        &#125;,
    &#125;,
&#125;)<span class="hljs-comment">;</span>

setTimeout(() => &#123;
    <span class="hljs-attr">app.a</span> = <span class="hljs-number">20</span><span class="hljs-comment">;</span>
    <span class="hljs-attr">app.obj.name</span> = <span class="hljs-string">"自动更新的name"</span><span class="hljs-comment">;</span>
    <span class="hljs-attr">app.obj.age</span> = <span class="hljs-string">"自动更新的age"</span><span class="hljs-comment">;</span>
&#125;, 1000)<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b25c1903a5e942e2921ca8e57057a13a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1.gif" loading="lazy" referrerpolicy="no-referrer">
<br></p>
<h3 data-id="heading-13">总结</h3>
<p>每一个属性都有一个dep，每一个组件都有一个watcher，watcher和dep是多对多的关系。</p>
<p>当创建渲染watcher的时候，会把当前的渲染watcher放到Dep的target上，调用_render方法取值，就会执行到属性的get方法，将当前渲染的watcher保存到全局属性上，然后让dep保存watcher，同时也将dep保存到这个watcher上。</p>
<p><strong>每个属性有一个dep，属性就是被观察者，watcher就是观察者，属性变化了会通知观察者更新，这就是观察者模式。</strong></p>
<br>
<p>watcher和dep相互记忆的过程很绕，需要好好理解，希望我们一起加油。</p>
<br>
<p>完整代码，请移步gihub <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnines-start%2Fvue2-source" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nines-start/vue2-source" ref="nofollow noopener noreferrer">vue2-source</a></p>
<hr>
<p>文章就到这里，下次再见！</p></div>  
</div>
            