
---
title: 'JavaScript异步发展历史'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/undefined'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 22:41:24 GMT
thumbnail: 'https://juejin.cn/post/undefined'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>"小和山的菜鸟们"，为前端开发者提供技术相关资讯以及系列基础文章。为更好的用户体验，请您移至我们官网小和山的菜鸟们 (<a href="https://xhs-rookies.com/" target="_blank" rel="nofollow noopener noreferrer">xhs-rookies.com/</a>) 进行学习，及时获取最新文章。</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>在 MDN 的 JavaScript 系列中我们已经学习了 callback、promise、generator、async/await。而在这一篇文章中，作者将以实际样例阐述异步发展历史，介绍每种实现方式的优势与不足，以期帮助读者熟悉历史进程并把握异步发展的脉络。 <img alt="异步发展历史" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">异步</h2>
<p>几十年前的导航网站，清爽又简单，没有什么特别的功能，只是单纯的展示，现成的网页在服务器上静静躺着，高效毫无压力，让人很喜欢。</p>
<p>几十年后的今天，静态页面远不能满足用户的需求，网站变得复杂起来，用户交互越来越频繁，从而产生大量复杂的内部交互，为了解决这种复杂，出现了各种系统“模式”，从而很容易的在外部获取数据，并实时展示给用户。</p>
<p>获取外部数据实际上就是“网络调用”，这个时候“<a href="https://developer.mozilla.org/en-US/docs/Glossary/Asynchronous" target="_blank" rel="nofollow noopener noreferrer">异步</a>”这个词汇出现了。</p>
<blockquote>
<p><a href="https://developer.mozilla.org/en-US/docs/Glossary/Asynchronous" target="_blank" rel="nofollow noopener noreferrer">异步</a>指两个或两个以上的对象或事件不同时存在或发生（或多个相关事物的发生无需等待其前一事物的完成）</p>
</blockquote>
<p><img src="https://img-blog.csdnimg.cn/2021011621291494.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzMzY0ODA2,size_16,color_FFFFFF,t_70" alt="image-20210116210456133" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">异步 callbacks</h2>
<blockquote>
<p><a href="https://developer.mozilla.org/zh-CN/docs/learn/JavaScript/%E5%BC%82%E6%AD%A5/%E7%AE%80%E4%BB%8B" target="_blank" rel="nofollow noopener noreferrer">异步 callbacks</a>其实就是函数，只不过是作为参数传递给那些在后台执行的其他函数。当那些后台运行的代码结束，就调用 callbacks 函数，通知你工作已经完成，或者其他有趣的事情发生了。</p>
</blockquote>
<p><strong>场景</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> readFile = <span class="hljs-function">(<span class="hljs-params">path, callBack</span>) =></span> &#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    callBack(path)
  &#125;, <span class="hljs-number">1000</span>)
&#125;

readFile(<span class="hljs-string">'first'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'first readFile success'</span>)
  readFile(<span class="hljs-string">'second'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'second readFile success'</span>)
    readFile(<span class="hljs-string">'third'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'third readFile success'</span>)
      readFile(<span class="hljs-string">'fourth'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'fourth readFile success'</span>)
        readFile(<span class="hljs-string">'fifth'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'fifth readFile success'</span>)
        &#125;)
      &#125;)
    &#125;)
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>优点：</strong></p>
<ul>
<li>解决了同步问题（即解决了一个任务时间长时，后面的任务排队，耗时太久，使程序的执行变慢问题）</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li>回调地狱(多层级嵌套)，会导致逻辑混乱，耦合性高，改动一处就会导致全部变动，嵌套多时，错误处理复杂</li>
<li>不能使用 try...catch 来抓取错误</li>
<li>不能 return</li>
<li>可读性差</li>
</ul>
<hr>
<h2 data-id="heading-3">Promise</h2>
<blockquote>
<p>一个<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise" target="_blank" rel="nofollow noopener noreferrer">Promise</a>对象代表一个在这个 promise 被创建出来时不一定已知的值。它让您能够把异步操作最终的成功返回值或者失败原因和相应的处理程序关联起来。 这样使得异步方法可以像同步方法那样返回值：异步方法并不会立即返回最终的值，而是会返回一个 promise，以便在未来某个时候把值交给使用者。</p>
</blockquote>
<p><strong>场景</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> readFile = <span class="hljs-function">(<span class="hljs-params">path</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (!path) &#123;
        reject(<span class="hljs-string">'error!!!'</span>)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.log(path + <span class="hljs-string">' readFile success'</span>)
        resolve()
      &#125;
    &#125;, <span class="hljs-number">1000</span>)
  &#125;)
&#125;

readFile(<span class="hljs-string">'first'</span>)
  .then(<span class="hljs-function">() =></span> readFile(<span class="hljs-string">'second'</span>))
  .then(<span class="hljs-function">() =></span> readFile(<span class="hljs-string">'third'</span>))
  .then(<span class="hljs-function">() =></span> readFile(<span class="hljs-string">'fourth'</span>))
  .then(<span class="hljs-function">() =></span> readFile(<span class="hljs-string">'fifth'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>优点：</strong></p>
<ul>
<li>状态改变后，就不会再变，任何时候都可以得到这个结果</li>
<li>可以将异步操作以同步操作的流程表达出来，避免了层层嵌套的回调函数</li>
<li>一定程度上解决了回调地狱的可读性问题</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li>无法取消 promise</li>
<li>当处于 pending 状态时，无法得知目前进展到哪一个阶段</li>
<li>代码冗余，有一堆任务时也会使语义不清晰</li>
</ul>
<hr>
<h2 data-id="heading-4">Generator</h2>
<blockquote>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Generator" target="_blank" rel="nofollow noopener noreferrer">Generator</a>函数是 ES6 中提供的一种<strong>异步编程解决方案</strong>。语法上，首先可以把它理解成，<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Generator" target="_blank" rel="nofollow noopener noreferrer">Generator</a>函数是一个<strong>状态机</strong>，封装了多个内部状态，需要使用<strong>next()函数</strong>来继续执行下面的代码。</p>
</blockquote>
<p><strong>特征</strong></p>
<ul>
<li>function 与函数名之间带有(*)</li>
<li>函数体内部使用 yield 表达式，函数执行遇到 yield 就返回</li>
</ul>
<p><strong>场景</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> readFile = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name, ms</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(name + <span class="hljs-string">'读完了'</span>)
      resolve()
    &#125;, ms)
  &#125;)
&#125;

<span class="hljs-keyword">var</span> gen = <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'指定generator'</span>)
  <span class="hljs-keyword">yield</span> readFile(<span class="hljs-string">'first'</span>, <span class="hljs-number">1000</span>)
  <span class="hljs-keyword">yield</span> readFile(<span class="hljs-string">'second'</span>, <span class="hljs-number">2000</span>)
  <span class="hljs-keyword">yield</span> readFile(<span class="hljs-string">'third'</span>, <span class="hljs-number">3000</span>)
  <span class="hljs-keyword">yield</span> readFile(<span class="hljs-string">'forth'</span>, <span class="hljs-number">4000</span>)
  <span class="hljs-keyword">yield</span> readFile(<span class="hljs-string">'fifth'</span>, <span class="hljs-number">5000</span>)
  <span class="hljs-keyword">return</span> <span class="hljs-string">'完成了'</span>
&#125;
<span class="hljs-keyword">var</span> g = gen()
<span class="hljs-keyword">var</span> result = g.next()
result.value
  .then(<span class="hljs-function">() =></span> &#123;
    g.next()
  &#125;)
  .then(<span class="hljs-function">() =></span> &#123;
    g.next()
  &#125;)
  .then(<span class="hljs-function">() =></span> &#123;
    g.next()
  &#125;)
  .then(<span class="hljs-function">() =></span> &#123;
    g.next()
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>优点：</strong></p>
<ul>
<li>可以控制函数的执行，可以配合 co 函数库使用</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li>流程管理却不方便（即何时执行第一阶段、何时执行第二阶段）</li>
</ul>
<hr>
<h2 data-id="heading-5">async 和 await</h2>
<blockquote>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/async_function" target="_blank" rel="nofollow noopener noreferrer">async functions</a> 和 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/await" target="_blank" rel="nofollow noopener noreferrer">await</a> 关键字是最近添加到 JavaScript 语言里面的。它们是 ECMAScript 2017 JavaScript 版的一部分（参见<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/ECMAScript_7_support_in_Mozilla" target="_blank" rel="nofollow noopener noreferrer">ECMAScript Next support in Mozilla</a>）。简单来说，它们是基于 promises 的语法糖，使异步代码更易于编写和阅读。通过使用它们，异步代码看起来更像是老式同步代码，因此它们非常值得学习。</p>
</blockquote>
<p><img src="https://img-blog.csdnimg.cn/20210116212853823.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzMzY0ODA2,size_16,color_FFFFFF,t_70" alt="image-20210116211018846" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>场景 1</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> readFile = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name, ms</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(name + <span class="hljs-string">'读完了'</span>)
      resolve()
    &#125;, ms)
  &#125;)
&#125;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useAsyncAwait</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">await</span> readFile(<span class="hljs-string">'first'</span>, <span class="hljs-number">1000</span>)
  <span class="hljs-keyword">await</span> readFile(<span class="hljs-string">'second'</span>, <span class="hljs-number">2000</span>)
  <span class="hljs-keyword">await</span> readFile(<span class="hljs-string">'third'</span>, <span class="hljs-number">3000</span>)
  <span class="hljs-keyword">await</span> readFile(<span class="hljs-string">'forth'</span>, <span class="hljs-number">4000</span>)
  <span class="hljs-keyword">await</span> readFile(<span class="hljs-string">'fifth'</span>, <span class="hljs-number">5000</span>)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async文件阅读完毕'</span>)
&#125;
useAsyncAwait()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>优点</strong></p>
<ul>
<li>
<p>内置执行器。意味着不需要像 generator 一样调用 next 函数或 co 模块</p>
</li>
<li>
<p>更广的适用性。async 和 await 后面跟的都是 promise 函数，原始数据类型会被转为 promise</p>
</li>
<li>
<p>语义更清晰、简洁</p>
<p><strong>缺点</strong></p>
</li>
<li>
<p>大量的 await 代码会阻塞（程序并不会等在原地，而是继续<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/EventLoop" target="_blank" rel="nofollow noopener noreferrer">事件循环</a>，等到响应后继续往下走）程序运行，每个 await 都会等待前一个完成</p>
</li>
</ul>
<p><strong>场景 2</strong> 场景 1 中的代码，其实 second，third 的伪请求其实并不依赖于 first，second 的结果，但它们必须等待前一个的完成才能继续，而我们想要的是它们同时进行，所以正确的操作应该是这样的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useAsyncAwait</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> first = readFile(<span class="hljs-string">'first'</span>, <span class="hljs-number">1000</span>)
  <span class="hljs-keyword">const</span> second = readFile(<span class="hljs-string">'second'</span>, <span class="hljs-number">2000</span>)
  <span class="hljs-keyword">const</span> third = readFile(<span class="hljs-string">'third'</span>, <span class="hljs-number">3000</span>)
  <span class="hljs-keyword">const</span> forth = readFile(<span class="hljs-string">'forth'</span>, <span class="hljs-number">4000</span>)
  <span class="hljs-keyword">const</span> fifth = readFile(<span class="hljs-string">'fifth'</span>, <span class="hljs-number">5000</span>)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async文件阅读完毕'</span>)

  <span class="hljs-keyword">await</span> first
  <span class="hljs-keyword">await</span> second
  <span class="hljs-keyword">await</span> third
  <span class="hljs-keyword">await</span> forth
  <span class="hljs-keyword">await</span> fifth
&#125;
useAsyncAwait()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里，我们将三个 promise 对象存储在变量中，这样可以同时启动它们关联的进程。</p>
<h2 data-id="heading-6">总结</h2>
<p>在这篇文章中，我们已经介绍了 JavaScript 异步发展史中 --- callback、promise、generator、async/await 的使用方式、优点与缺点。</p>






























<table><thead><tr><th align="center">发展史</th><th align="center">优点</th><th align="center">缺点</th></tr></thead><tbody><tr><td align="center">callback</td><td align="center">解决了同步问题</td><td align="center">回调地狱、可读性差、无法 try / catch 、无法 return</td></tr><tr><td align="center">promise</td><td align="center">一定程度上解决了回调地狱的可读性</td><td align="center">无法取消、任务多时，同样存在语义不清晰</td></tr><tr><td align="center">generator</td><td align="center">可以控制函数的执行，可以配合 co 函数库使用</td><td align="center">流程管理却不方便（即何时执行第一阶段、何时执行第二阶段</td></tr><tr><td align="center">async/await</td><td align="center">语义更清晰、简洁，内置执行器</td><td align="center">认知不清晰可能会造成大量 await 阻塞（程序并不会等在原地，而是继续<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/EventLoop" target="_blank" rel="nofollow noopener noreferrer">事件循环</a>，等到响应后继续往下走）情况</td></tr></tbody></table>
<p>而在现有的异步解决方案中，async/await 是使用人数最多的，它带给我们最大的好处即同步代码的风格，语义简洁、清晰。</p>
<h2 data-id="heading-7">相关文章</h2>
<ul>
<li><a href="https://developer.mozilla.org/zh-CN/docs/learn/JavaScript/%E5%BC%82%E6%AD%A5" target="_blank" rel="nofollow noopener noreferrer">MDN-异步 JavaScript</a></li>
<li><a href="https://www.ruanyifeng.com/blog/2012/12/asynchronous%EF%BC%BFjavascript.html" target="_blank" rel="nofollow noopener noreferrer">阮一峰-JavaScript 异步编程的 4 种方法</a></li>
<li><a href="https://segmentfault.com/a/1190000019254694" target="_blank" rel="nofollow noopener noreferrer">掘金-细说 JavaScript 异步的发展历程</a></li>
<li><a href="https://juejin.cn/post/6844903620043866126" target="_blank">掘金-async/await 的优点、陷阱以及如何使用</a></li>
<li><a href="https://www.williamife.com/2018/12/05/JS%E5%BC%82%E6%AD%A5%E5%8F%91%E5%B1%95%E6%B5%81%E7%A8%8B/" target="_blank" rel="nofollow noopener noreferrer">JS 异步发展流程</a></li>
</ul></div>  
</div>
            