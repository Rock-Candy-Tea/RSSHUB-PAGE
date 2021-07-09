
---
title: '浏览器事件循环（event loop）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6240'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 01:31:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=6240'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Event Loop</p>
<blockquote>
<p>作用：js 是一门单线程语言，就造成了在执行中如果遇到比较耗时的程序就会一直等待，影响用户体验。所以有了event loop 来解决这个问题</p>
</blockquote>
<h5 data-id="heading-0">ES6 新增机制</h5>
<ul>
<li>macrotask（宏任务）: script 主代码块、setTimeout、setInterval、requestAnimationFrame、node 中的setimmediate 等。</li>
<li>microtask（微任务）: Promise.then catch finally、MutationObserver、node 中的process.nextTick 等。</li>
</ul>
<p><code>微任务跟在对应的宏任务后执行</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)
&#125;)
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>)
    resolve()
&#125;).then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">4</span>)
    
    <span class="hljs-built_in">Promise</span>.resolve()
    .then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-number">5</span>)
    &#125;)
    .then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-number">6</span>)
    &#125;)
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">7</span>)

<span class="hljs-comment">//结果</span>
<span class="hljs-number">1</span> <span class="hljs-number">3</span> <span class="hljs-number">7</span> <span class="hljs-number">4</span> <span class="hljs-number">5</span> <span class="hljs-number">6</span> <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>宏任务执行(javascript) <code>console.log(1)</code>
<ul>
<li>Macrotask Queue []</li>
<li>Microtask Queue []</li>
</ul>
<strong>console 1</strong></li>
<li>宏任务执行(setTimeout) 生成一个回调函数,排在<code>javascript</code>后边
<ul>
<li>Macrotask Queue [<code>javascript，setTimeout</code>]</li>
<li>Microtask Queue []</li>
</ul>
</li>
<li>微任务 Promise 同步执行 <code>console.log(3)</code> 并把 <code>.then</code> 放入到了微任务队列
<ul>
<li>Macrotask Queue [<code>javascript，setTimeout</code>]</li>
<li>Microtask Queue [<code>log(4).then(log(5)).then(log(6))</code>]</li>
</ul>
<strong>console 1 3</strong></li>
<li>同步执行 <code>console.log(7)</code>
<ul>
<li>Macrotask Queue [<code>javascript，setTimeout</code>]</li>
<li>Microtask Queue [<code>log(4).then(log(5)).then(log(6))</code>]</li>
</ul>
<strong>console 1 3 7</strong></li>
<li>先执行 <code>javascript</code> 的微任务 <code>console.log(4)</code> 并生成新的微任务 <code>.then</code>
<ul>
<li>Macrotask Queue [<code>javascript，setTimeout</code>]</li>
<li>Microtask Queue [<code>then(log(5)).then(log(6))</code>]</li>
</ul>
<strong>console 1 3 7 4</strong></li>
<li>执行 javascript 的微任务 <code>console.log(5)</code> 并生成新的微任务 <code>.then</code>
<ul>
<li>Macrotask Queue [<code>javascript，setTimeout</code>]</li>
<li>Microtask Queue [<code>.then(6)</code>]</li>
</ul>
<strong>console 1 3 7 4 5</strong></li>
<li>执行 javascript 的微任务 <code>console.log(6)</code>， <code>javascript</code>宏任务执行完毕，移除执行栈
<ul>
<li>Macrotask Queue [<code>javascript，setTimeout</code>]</li>
<li>Microtask Queue [<code>.then(6)</code>]</li>
</ul>
<strong>console 1 3 7 4 5 6</strong></li>
<li>执行下个宏任务 <code>setTimeout</code> ,<code>consol.log(2)</code>
<ul>
<li>Macrotask Queue [<code>setTimeout</code>]</li>
<li>Microtask Queue []</li>
</ul>
<strong>console 1 3 7 4 5 6 2</strong></li>
<li>执行完成。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"> 可以把浏览器理解成客栈，
 <span class="hljs-string">`相亲相爱一家人`</span>入住理解成一个宏任务，
 <span class="hljs-string">`家庭成员`</span>可能会有好多个微任务（比如先让你去拿个壶），并且执行中可能派生新的微任务（拿完之后还可能打壶水）
 并且执行中还有<span class="hljs-string">`幸福一家人`</span>入住
 但是你不可能打水的过程中分身去招待另一家，只能先让他进入队列
 当<span class="hljs-string">`相亲相爱一家人`</span>的微任务执行完之后，另一个宏任务开始执行
<span class="copy-code-btn">复制代码</span></code></pre>
<p>借鉴自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000016278115" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000016278115" ref="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></p></div>  
</div>
            