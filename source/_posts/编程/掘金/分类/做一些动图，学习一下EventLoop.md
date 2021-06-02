
---
title: '做一些动图，学习一下EventLoop'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/536eeb3dad9b407a8a7368d6b44fc341~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 19:10:06 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/536eeb3dad9b407a8a7368d6b44fc341~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;color:rgba(46,36,36,.87);overflow-x:hidden&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;margin-bottom:5px;font-size:30px;font-weight:500&#125;.markdown-body h1:before&#123;content:"#";margin-right:10px;color:#1976d2&#125;.markdown-body h2&#123;font-size:28px;font-weight:400;border-left:5px solid #454545;margin-top:20px;padding-left:10px;transition:all .3s ease-in-out&#125;.markdown-body h2:hover&#123;border-color:#1976d2&#125;.markdown-body h3&#123;font-size:24px;font-weight:400;margin-top:15px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:20px;font-weight:500&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body h2:first-letter,.markdown-body h3:first-letter,.markdown-body p:first-letter&#123;text-transform:capitalize&#125;.markdown-body em&#123;text-emphasis:dot;text-emphasis-position:under&#125;.markdown-body img&#123;display:block;margin:0 auto!important;max-width:100%;border-radius:2px;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#ddd,#999,#ddd);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;font-weight:900;word-break:break-word;border-radius:2px;overflow-x:auto;font-size:.87em;padding:.065em .4em;background-color:#fbe5e1;color:#c0341d&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:0 4px&#125;.markdown-body pre>code&#123;font-weight:400;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#027fff;transition:all .3s ease-in-out;padding-bottom:4px;border-bottom:2px solid transparent&#125;.markdown-body a:after&#123;content:"";display:inline-block;width:18px;height:18px;margin-left:4px;vertical-align:middle;background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMiIgaGVpZ2h0PSIyMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiMwMjdGRkYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTkuODE1IDYuNDQ4bDEuOTM2LTEuOTM2YzEuMzM3LTEuMzM2IDMuNTgtMS4yNTkgNS4wMTMuMTczIDEuNDMyIDEuNDMyIDEuNTEgMy42NzYuMTczIDUuMDEzbC0xLjQ1MiAxLjQ1Mi0uOTY4Ljk2OGMtMS4zMzcgMS4zMzYtMy41ODEgMS4yNTktNS4wMTMtLjE3MyIvPjxwYXRoIGQ9Ik0xMS4yNjcgMTUuMzY3bC0xLjkzNiAxLjkzNmMtMS4zMzYgMS4zMzctMy41OCAxLjI2LTUuMDEyLS4xNzMtMS40MzItMS40MzItMS41MS0zLjY3Ni0uMTczLTUuMDEybDEuNDUyLTEuNDUyLjk2OC0uOTY4YzEuMzM2LTEuMzM3IDMuNTgtMS4yNiA1LjAxMi4xNzMiLz48L2c+PC9zdmc+);background-size:cover;background-repeat:no-repeat&#125;.markdown-body a:hover&#123;border-color:#027fff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body a.footnote-backref:after,.markdown-body a.footnote-ref:after,.markdown-body sup a:after&#123;display:none!important&#125;.markdown-body table&#123;margin:0 auto 10px;font-size:12px;width:auto;max-width:100%;overflow:auto;border:2px solid #c6c6c6&#125;.markdown-body table img&#123;box-shadow:none!important&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body del&#123;color:rgba(0,0,0,.6)&#125;.markdown-body blockquote&#123;position:relative;color:#666;padding:5px 23px 1px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:hsla(0,0%,78.4%,.12);transition:all .2s ease-in-out&#125;.markdown-body blockquote:hover&#123;border-color:#1976d2&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;font-size:24px;font-weight:800;line-height:24px;color:#cbcbcb;opacity:.6&#125;.markdown-body blockquote:before&#123;content:"“";top:4px;left:6px&#125;.markdown-body blockquote:after&#123;content:"”";right:8px;bottom:-8px&#125;.markdown-body blockquote>p,.markdown-body blockquote blockquote&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #1976d2;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary:hover::-webkit-details-marker&#123;color:#1976d2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第1天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>。</p>
<p>最近在学习<code>Vue</code>源码，刚好学到虚拟DOM的异步更新，这里就涉及到<code>JavaScript</code>中的事件循环<code>Event Loop</code>。之前对这个概念还是比较模糊，大概知道是什么，但一直没有深入学习。刚好借此机会，回过头来学习一下<code>Event Loop</code>。</p>
<h1 data-id="heading-0">JavaScript是单线程的语言</h1>
<p>事件循环<code>Event Loop</code>，这是目前浏览器和<code>NodeJS</code>处理<code>JavaScript</code>代码的一种机制，而这种机制存在的背后，就有因为<code>JavaScript</code>是一门<strong>单线程</strong>的语言。</p>
<p>单线程和多线程最简单的区别就是：单线程同一个时间只能做一件事情，而多线程同一个时间能做多件事情。</p>
<p>而<code>JavaScript</code>之所谓设计为单线程语言，主要是因为它作为浏览器脚本语言，主要的用途就是与用户互动，操作<code>Dom</code>节点。</p>
<p>而在这个情景设定下，假设<code>JavaScript</code>同时有两个进程，一个是操作A节点，一个是删除A节点，这时候浏览器就不知道要以哪个线程为准了。</p>
<p>因此为了避免这类型的问题，<code>JavaScript</code>从一开始就属于单线程语言。</p>
<h2 data-id="heading-1">调用栈 Call Stack</h2>
<p>在<code>JavaScript</code>运行的时候，主线程会形成一个栈，这个栈主要是解释器用来最终函数执行流的一种机制。通常这个栈被称为调用栈<code>Call Stack</code>，或者执行栈（<code>Execution Context Stack</code>）。</p>
<p>调用栈，顾名思义是具有LIFO（后进先出，Last in First Out）的结构。调用栈内存放的是代码执行期间的所有执行上下文。</p>
<ul>
<li>每调用一个函数，解释器就会把该函数的执行上下文添加到调用栈并开始执行；</li>
<li>正在调用栈中执行的函数，如果还调用了其他函数，那么新函数也会被添加到调用栈，并立即执行；</li>
<li>当前函数执行完毕后，解释器会将其执行上下文清除调用栈，继续执行剩余执行上下文中的剩余代码；</li>
<li>但分配的调用栈空间被占满，会引发”堆栈溢出“的报错。</li>
</ul>
<p>现在用个小案例来演示一下调用栈。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span>);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b'</span>);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">c</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'c'</span>);
    a();
    b();
&#125;

c();

<span class="hljs-comment">/**
* 输出结果：c a b
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行这段代码的时候，首先调用的是函数<code>c()</code>。因此<code>function c()&#123;&#125;</code>的执行上下文就会被放入调用栈中。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/536eeb3dad9b407a8a7368d6b44fc341~tplv-k3u1fbpfcp-watermark.image" alt="call_stack_1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后开始执行函数<code>c</code>，执行的第一个语句是<code>console.log('c')</code>。</p>
<p>因此解释器也会将其放入调用栈中。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ba9a90a86764cd2bd89ea5d4fbf1267~tplv-k3u1fbpfcp-watermark.image" alt="call_stack_2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当<code>console.log('c')</code>方法执行完后，控制台打印了<code>'c'</code>，调用栈就会将其移除。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87d57cfc86d145269c5ddd448c2e94d4~tplv-k3u1fbpfcp-watermark.image" alt="call_stack_3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着就是执行<code>a()</code>函数。</p>
<p>解释器就将<code>function a() &#123;&#125;</code>的执行上下文放入调用栈中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91d45a91e7754d94a2773f80057f37fe~tplv-k3u1fbpfcp-watermark.image" alt="call_stack_4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>紧接着就执行<code>a()</code>中的语句——<code>console.log('a')</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dac105f219444da0bd053edd2a85b2b6~tplv-k3u1fbpfcp-watermark.image" alt="call_stack_5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当函数<code>a</code>执行结束后，调用栈就将执行上下文移除。</p>
<p>然后接着执行<code>c()</code>函数剩下的语句，也就是执行<code>b()</code>函数，因此它的执行上下文就加入调用栈中。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c4801b80d914722aa808b116b53a888~tplv-k3u1fbpfcp-watermark.image" alt="call_stack_6.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>紧接着就执行<code>b()</code>中的语句——<code>console.log('b')</code>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13c11b0b95aa42c5a9ef94edc5008358~tplv-k3u1fbpfcp-watermark.image" alt="call_stack_7.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>b()</code>执行完后，调用栈就将其移出。</p>
<p>这时<code>c()</code>也执行结束了，调用栈也将其移出栈。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d529cd9b0a3435681763466f634c8e1~tplv-k3u1fbpfcp-watermark.image" alt="call_stack_8.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候，我们这段语句就执行结束了。</p>
<h1 data-id="heading-2">任务队列</h1>
<p>上面的案例简单的介绍了关于<code>JavaScript</code>单线程的执行方式。</p>
<p>但这其中会存在一些问题，就是如果当一个语句也需要执行很长时间的话，比如请求数据、定时器、读取文件等等，后面的语句就得一直等着前面的语句执行结束后才会开始执行。</p>
<p>显而易见，这是不可取的。</p>
<h2 data-id="heading-3">同步任务和异步任务</h2>
<p>因此，<code>JavaScript</code>将所有执行任务分为了同步任务和异步任务。</p>
<p>其实我们每个任务都是在做两件事情，就是<strong>发起调用</strong>和<strong>得到结果</strong>。</p>
<p>而同步任务和异步任务最主要的差别就是，同步任务发起调用后，很快就可以得到结果，而异步任务是无法立即得到结果，比如请求接口，每个接口都会有一定的响应时间，根据网速、服务器等等因素决定，再比如定时器，它需要固定时间后才会返回结果。</p>
<p>因此，对于同步任务和异步任务的执行机制也不同。</p>
<p>同步任务的执行，其实就是跟前面那个案例一样，按照代码顺序和调用顺序，支持进入调用栈中并执行，执行结束后就移除调用栈。</p>
<p>而异步任务的执行，首先它依旧会进入调用栈中，然后发起调用，然后解释器会将其<strong>响应回调任务</strong>放入一个<strong>任务队列</strong>，紧接着调用栈会将这个任务移除。当主线程清空后，即所有同步任务结束后，解释器会读取任务队列，并依次将<strong>已完成的异步任务</strong>加入调用栈中并执行。</p>
<p>这里有个重点，就是异步任务不是直接进入任务队列的。</p>
<p>这里举一个简单的例子。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);

fetch(<span class="hljs-string">'https://jsonplaceholder.typicode.com/todos/1'</span>)
    .then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> response.json())
    .then(<span class="hljs-function"><span class="hljs-params">json</span> =></span> <span class="hljs-built_in">console</span>.log(json))

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很显然，<code>fetch()</code>就是一个异步任务。</p>
<p>但执行到<code>console.log(2)</code>之前，其实<code>fetch()</code>已经被调用且发起请求了，但是还未响应数据。而响应数据和处理数据的函数<code>then()</code>此时已经在<strong>任务队列</strong>中，等候<code>console.log(2)</code>执行结束后，所以同步任务清空后，再进入调用栈执行响应动作。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b36396fc5924451c8e73169a1885a505~tplv-k3u1fbpfcp-watermark.image" alt="async.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">宏任务和微任务</h2>
<p>前面聊到同步任务和异步任务的时候，提及到了<strong>任务队列</strong>。</p>
<p>在任务队列中，其实还分为<strong>宏任务队列（Task Queue）<strong>和</strong>微任务队列（Microtask Queue）</strong>，对应的里面存放的就是<strong>宏任务</strong>和<strong>微任务</strong>。</p>
<p>首先，宏任务和微任务都是异步任务。</p>
<p>而宏任务和微任务的区别，就是它们执行的顺序，这也是为什么要区分宏任务和微任务。</p>
<p>在同步任务中，任务的执行都是按照代码顺序执行的，而异步任务的执行也是需要按顺序的，队列的属性就是<strong>先进先出（FIFO，First in First Out）</strong>，因此异步任务会按照进入队列的顺序依次执行。</p>
<p>但在一些场景下，如果只按照进入队列的顺序依次执行的话，也会出问题。比如队列先进入一个一小时的定时器，接着再进入一个请求接口函数，而如果根据进入队列的顺序执行的话，请求接口函数可能需要一个小时后才会响应数据。</p>
<h4 data-id="heading-5">宏任务</h4>



































<table><thead><tr><th></th><th>浏览器</th><th>Node</th></tr></thead><tbody><tr><td>I/O</td><td>✅</td><td>✅</td></tr><tr><td>setTimeout</td><td>✅</td><td>✅</td></tr><tr><td>setInterval</td><td>✅</td><td>✅</td></tr><tr><td>setImmediate</td><td>❌</td><td>✅</td></tr><tr><td>requestAnimationFrame</td><td>✅</td><td>❌</td></tr></tbody></table>
<h4 data-id="heading-6">微任务</h4>

























<table><thead><tr><th></th><th>浏览器</th><th>Node</th></tr></thead><tbody><tr><td>process.nextTick</td><td>❌</td><td>✅</td></tr><tr><td>MutationObserver</td><td>✅</td><td>❌</td></tr><tr><td>Promise.then catch finally</td><td>✅</td><td>✅</td></tr></tbody></table>
<h1 data-id="heading-7">事件循环 Event Loop</h1>
<p>其实宏任务队列和微任务队列的执行，就是事件循环的一部分了，所以放在这里一起说。</p>
<p>事件循环的具体流程如下：</p>
<ol>
<li>从宏任务队列中，按照<strong>入队顺序</strong>，找到已经<strong>可以执行的宏任务</strong>，放入调用栈，开始执行；</li>
<li>执行完<strong>该宏任务</strong>下所有同步任务后，即调用栈清空后，该宏任务被推出宏任务队列，然后微任务队列开始按照入队顺序，依次执行其中的微任务，<strong>直至微任务队列清空为止</strong>；</li>
<li>当微任务队列清空后，一个事件循环结束；</li>
<li>接着从宏任务队列中，找到下一个已经可以执行的宏任务，开始第二个事件循环，直至宏任务队列清空为止。</li>
</ol>
<p>这里有几个重点：</p>
<ul>
<li>当我们第一次执行的时候，解释器会将整体代码<code>script</code>放入宏任务队列中，因此事件循环是从第一个宏任务开始的；</li>
<li>找宏任务的时候，按照入队的顺序，找到已经可以执行的宏任务。可以执行的宏任务，比如请求接口任务，已经接收到接口数据请求了，比如定时器已经到时可以执行了。如果按顺序排到的任务还不可执行的话，解释器会找到下一个宏任务的。之所以这样设计，是因为假如你的代码先写了<code>setTimeout(fn1,10000)</code>，后写了<code>setTimeout(fn2,1000)</code>，如果按照入队顺序，<code>fn1</code>一定在<code>fn2</code>先被执行，但当时间还没到10000ms的时候，<code>fn1</code>还不可执行，则解释器应该跳过<code>fn1</code>去执行<code>fn2</code>，否则的话<code>fn2</code>会等到11000ms才被执行。</li>
<li>如果在执行微任务的过程中，产生新的微任务添加到微任务队列中，也需要一起清空；微任务队列没清空之前，是不会执行下一个宏任务的。</li>
</ul>
<p>接下来，通过一个常见的面试题例子来模拟一下事件循环。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">"a"</span>);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"b"</span>);
&#125;, <span class="hljs-number">0</span>);

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"c"</span>);
    resolve();
&#125;)
    .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"d"</span>);
    &#125;)
    .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"e"</span>);
    &#125;);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"f"</span>);

<span class="hljs-comment">/**
* 输出结果：a c f d e b
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，当代码执行的时候，整体代码<code>script</code>被推入宏任务队列中，并开始执行该宏任务。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63e0812fe4fb443ba65ab26d5de95f44~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照代码顺序，首先执行<code>console.log("a")</code>。</p>
<p>该函数上下文被推入调用栈，执行完后，即移除调用栈。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c753d28cb8374f5f9d13569cf3934347~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来执行<code>setTimeout()</code>，该函数上下文也进入调用栈中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c80331146b64fd1bcfe070ccf080fc2~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为<code>setTimeout</code>是一个宏任务，因此将其<code>callback</code>函数推入宏任务队列中，然后该函数就被移除调用栈，继续往下执行。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/847d9b53ab974f78b810235f38448d90~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>紧接着是<code>Promise</code>语句，先将其放入调用栈，然后接着往下执行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/532fa46bfa654e17a5e494c94b377977~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行<code>console.log("c")</code>和<code>resolve()</code>，这里就不多说了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9265e6b57c2a42ebacf7d50d673cb4de~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_6.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着来到<code>new Promise().then()</code>方法，这是一个微任务，因此将其推入微任务队列中。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de71bda0eeb64a2690cef27a9c687011~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_7.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时<code>new Promise</code>语句已经执行结束了，就被移除调用栈。</p>
<p>接着做执行<code>console.log('f')</code>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1af0dff172334d37914a4ca4c9c1ce07~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_8.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候，<code>script</code>宏任务已经执行结束了，因此被推出宏任务队列。</p>
<p>紧接着开始清空微任务队列了。首先执行的是<code>Promise then</code>，因此它被推入调用栈中。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/039d9e6974c245b58f40b0baaf9fb36b~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_9.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后开始执行其中的<code>console.log("d")</code>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/414a340f94454d4e8c18b81bc759382b~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_10.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行结束后，检测到后面还有一个<code>then()</code>函数，因此将其推入微任务队列中。</p>
<p>此时第一个<code>then()</code>函数已经执行结束了，就会移除调用栈和微任务队列。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e15c103346f1434d87136abf91c5123c~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_11.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时微任务队列还没被清空，因此继续执行下一个微任务。</p>
<p>执行过程跟前面差不多，就不多说了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07ea9badd02d4e3986091cc212aae6d4~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_12.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时微任务队列已经清空了，第一个事件循环已经结束了。</p>
<p>接下来执行下一个宏任务，即<code>setTimeout callback</code>。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d061a0487bbe4b36a0230a90a9d35b82~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_13.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行结束后，它也被移除宏任务队列和调用栈。</p>
<p>这时候微任务队列里面没有任务，因此第二个事件循环也结束了。</p>
<p>宏任务也被清空了，因此这段代码已经执行结束了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3785ff320d644deb4476e81f3825be2~tplv-k3u1fbpfcp-watermark.image" alt="task_queque_14.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-8">await</h1>
<p>ECMAScript2017中添加了<code>async functions</code>和<code>await</code>。</p>
<p><code>async</code>关键字是将一个同步函数变成一个异步函数，并将返回值变为<code>promise</code>。</p>
<p>而<code>await</code>可以放在任何异步的、基于<code>promise</code>的函数之前。在执行过程中，它会暂停代码在该行上，直到<code>promise</code>完成，然后返回结果值。而在暂停的同时，其他正在等待执行的代码就有机会执行了。</p>
<p>下面通过一个例子来体验一下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">async1</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"a"</span>);
    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> async2();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"b"</span>);
&#125;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">async2</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"c"</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-number">2</span>;
&#125;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"d"</span>);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"e"</span>);
&#125;, <span class="hljs-number">0</span>);

async1().then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"f"</span>)
&#125;)

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"g"</span>);
    resolve();
&#125;).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"h"</span>);
&#125;);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"i"</span>);

<span class="hljs-comment">/**
* 输出结果：d a c g i b h f e 
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，开始执行前，将整体代码<code>script</code>放入宏任务队列中，并开始执行。</p>
<p>第一个执行的是<code>console.log("d")</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d6c329638ec409ba5f11e6fd3d29c36~tplv-k3u1fbpfcp-watermark.image" alt="async_await_1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>紧接着是<code>setTimeout</code>，将其回调放入宏任务中，然后继续执行。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f1f04859bfb442198a52b1d9902c918~tplv-k3u1fbpfcp-watermark.image" alt="async_await_2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>紧接着是调用<code>async1()</code>函数，因此将其函数上下文放置到调用栈。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/225d46f2cc5e4452883c01623768745e~tplv-k3u1fbpfcp-watermark.image" alt="async_await_3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后开始执行<code>async1</code>中的<code>console.log("a")</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6abde34a5244282a0ac63006c4e0501~tplv-k3u1fbpfcp-watermark.image" alt="async_await_4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来就是<code>await</code>关键字语句。</p>
<p><code>await</code>后面调用的是<code>async2</code>函数，因此我们将其放入调用栈。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/293e3d885e044c4ea345e5e24e4177a3~tplv-k3u1fbpfcp-watermark.image" alt="async_await_5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后开始执行<code>async2</code>中的<code>console.log("c")</code>，并<code>return</code>一个值。</p>
<p>执行完成后，<code>async2</code>就被移出调用栈。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f2810e9d4d34119a1e93a08f5b03761~tplv-k3u1fbpfcp-watermark.image" alt="async_await_6.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候，<code>await</code>会阻塞<code>async2</code>的返回值，先跳出<code>async1</code>进行往下执行。</p>
<p>需要注意的是，现在<code>async1</code>中的<code>res</code>变量，还是<code>undefined</code>，没有赋值。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0283181a9fff49159069afdc414c16d7~tplv-k3u1fbpfcp-watermark.image" alt="async_await_7.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>紧接着是执行<code>new Promise</code>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb63b3737a464753ba59e92b01d5f209~tplv-k3u1fbpfcp-watermark.image" alt="async_await_8.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行<code>console.log("i")</code>。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a319d8c9c5154d0f8d508154db114178~tplv-k3u1fbpfcp-watermark.image" alt="async_await_9.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时，<code>async1</code>外面的同步任务都执行完成了，因此就重新回到前面阻塞的位置，进行往下执行。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a202e7f34c50443f8901d31a45e60449~tplv-k3u1fbpfcp-watermark.image" alt="async_await_10.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时<code>res</code>成功赋值了<code>async2</code>的结果值，然后往下执行<code>console.log("b")</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d359c31825bc4e4ea5c8ab4f46e69567~tplv-k3u1fbpfcp-watermark.image" alt="async_await_11.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候<code>async1</code>才算是执行结束，紧接着再将其调用的<code>then()</code>函数放入微任务队列中。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f4b126608fc4547874af93a42533bac~tplv-k3u1fbpfcp-watermark.image" alt="async_await_12.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时<code>script</code>宏任务已经全部执行完了，开始准备清空微任务队列了。</p>
<p>第一个被执行的微任务队列是<code>promise then</code>，也就是将执行其中的<code>console.log("h")</code>语句。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06091de35b924bee886429fcc017b995~tplv-k3u1fbpfcp-watermark.image" alt="async_await_13.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行完<code>Promise then</code>微任务后，紧接着开始执行<code>async1</code>的<code>promise then</code>微任务。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81c010740652497897471c3237ee6580~tplv-k3u1fbpfcp-watermark.image" alt="async_await_14.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候微任务队列已经清空了，即开始执行下一个宏任务。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82eed4406c724eb78b38daea49b5b697~tplv-k3u1fbpfcp-watermark.image" alt="async_await_15.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">页面渲染</h1>
<p>最后来讲将事件循环中的页面更新渲染，这也是<code>Vue</code>中异步更新的逻辑所在。</p>
<p>每次当一次事件循环结束后，即一个宏任务执行完成后以及微任务队列被清空后，浏览器就会进行一次页面更新渲染。</p>
<p>通常我们浏览器页面刷新频率是60fps，也就是意味着120ms要刷新一次，因此我们也要尽量保证一次事件循环控制在120ms之内，这也是我们需要做代码性能优化的一个原因。</p>
<p>接下来还是通过一个案例来看一下。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Event Loop<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"demo"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./src/render1.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./src/render2.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// render1</span>
<span class="hljs-keyword">const</span> demoEl = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'demo'</span>);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span>);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    alert(<span class="hljs-string">'渲染完成！'</span>)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b'</span>);
&#125;,<span class="hljs-number">0</span>)

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'c'</span>);
    resolve()
&#125;).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'d'</span>);
    alert(<span class="hljs-string">'开始渲染！'</span>)
&#125;)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'e'</span>);
demoEl.innerText = <span class="hljs-string">'Hello World!'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// render2</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'f'</span>);

demoEl.innerText = <span class="hljs-string">'Hi World!'</span>;
alert(<span class="hljs-string">'第二次渲染！'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据<code>HTML</code>的执行顺序，第一个被执行的<code>JavaScript</code>代码是<code>render1.js</code>，因此解释器将其推入宏任务队列，并开始执行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5feea5835373440582ccb2a63aef1abe~tplv-k3u1fbpfcp-watermark.image" alt="render_1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第一个被执行的是<code>console.log("a")</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cffb8442d2d481b8c78fec5b748e2a2~tplv-k3u1fbpfcp-watermark.image" alt="render_2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其次是<code>setTimeout</code>，并将其回调加入宏任务队列中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5446c61f921849c7ba934160adcfab51~tplv-k3u1fbpfcp-watermark.image" alt="render_3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>紧接着执行<code>new Promise</code>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce18a8c48c1249f79be3e892f1bf21d0~tplv-k3u1fbpfcp-watermark.image" alt="render_4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同样，将其<code>then()</code>推入微任务队列中去。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/306b21e3e50e4156a47119fec8a52082~tplv-k3u1fbpfcp-watermark.image" alt="render_5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>紧接着执行<code>console.log("e")</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2190021a82a04f5c8311ebde4f288a61~tplv-k3u1fbpfcp-watermark.image" alt="render_6.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后，修改DOM节点的文本内容，但是这时候页面还不会更新渲染。</p>
<p>这时候<code>script</code>宏任务也执行结束了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d82b272153ff4c049ad630160a3969df~tplv-k3u1fbpfcp-watermark.image" alt="render_7.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>紧接着，开始清空微任务队列，执行<code>Promise then</code>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9182947f295e436a8509e5fe6ee646a3~tplv-k3u1fbpfcp-watermark.image" alt="render_8.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候，<code>alert</code>一个通知，而这个语句结束后，则微任务队列清空，代表第一个事件循环结束，即将要开始渲染页面了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d917f9014de43f7b014ec5060749b6f~tplv-k3u1fbpfcp-watermark.image" alt="render_9.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当点击关闭<code>alert</code>后，事件循环结束，页面也开始渲染。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3c77f7ff3be423c80f88185e5d98995~tplv-k3u1fbpfcp-watermark.image" alt="render_10.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>渲染结束后，就开始执行下一个宏任务，即<code>setTimeout callback</code>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/734b05f4724e49c4bcfc62777fc2caf2~tplv-k3u1fbpfcp-watermark.image" alt="render_11.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>紧接着执行<code>console.log("b")</code>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6db3b70b11634fb7b1d4d87376a729d5~tplv-k3u1fbpfcp-watermark.image" alt="render_12.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候宏任务队列已清空了，但是<code>html</code>文件还没执行结束，因此进入<code>render2.js</code>继续执行。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62aa89b72a97404b8ab3972464753f85~tplv-k3u1fbpfcp-watermark.image" alt="render_13.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先执行<code>console.log('f')</code>。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ca3d1b9bd0a41c5813fe3fbe6d146d1~tplv-k3u1fbpfcp-watermark.image" alt="render_14.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>紧接着，再次修改节点的文本信息，此时依旧不会更新页面渲染。</p>
<p>接着执行<code>alert</code>语句，当关闭<code>alert</code>通知后，该宏任务结束，微任务队列也为空，因此该事件循环也结束了，这时候就开始第二次页面更新。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a20d047d08e4ac0a1d031473adea88f~tplv-k3u1fbpfcp-watermark.image" alt="render_15.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但如果将所有<code>JavaScript</code>代码使用内嵌方式的话，浏览器会先把两个<code>script</code>丢到宏任务队列中去，因此执行的顺序也会不一样，这里就不一一推导了。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Event Loop<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"demo"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">const</span> demoEl = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'demo'</span>);

        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a'</span>);

        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            alert(<span class="hljs-string">'渲染完成！'</span>)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'b'</span>);
        &#125;,<span class="hljs-number">0</span>)

        <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'c'</span>);
            resolve()
        &#125;).then(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'d'</span>);
            alert(<span class="hljs-string">'开始渲染！'</span>)
        &#125;)

        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'e'</span>);
        demoEl.innerText = <span class="hljs-string">'Hello World!'</span>;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'f'</span>);

        demoEl.innerText = <span class="hljs-string">'Hi World!'</span>;
        alert(<span class="hljs-string">'第二次渲染！'</span>);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">输出：a c e d "开始渲染" f "第二次渲染" b "渲染结束"
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            