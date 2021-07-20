
---
title: '关于this指向的极简解析，搞懂80%以上的指向问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9044'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 22:59:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=9044'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在刚入门开始学 <code>this</code> 的时候，我自己对 <code>this</code> 的指向是非常迷惑的，感觉总是抓不到重点。同时，对 <code>this</code> 指向的系统分析对于小白来说也很难搞懂。</p>
<p>在经过一段时间的总结后，大概弄明白了不同情况下 <code>this</code> 的指向，这里就来给大家总结一波，尽量用通俗简单的语言讲明白 <code>this</code> 的指向情况。</p>
<h1 data-id="heading-0">前置知识</h1>
<h2 data-id="heading-1">this 是什么？</h2>
<p>普遍概念：JavaScript 的关键字，当前环境执行上下文对象的属性。</p>
<p>能读懂的概念：<code>this</code> 就是你 <code>call</code> 一个函数时，传入的第一个参数。<strong>也可以理解成 <code>this</code> 就是 <code>call</code> 的第一个参数。</strong></p>
<h2 data-id="heading-2">函数调用的3种形式</h2>
<pre><code class="hljs language-js copyable" lang="js">f(p1, p2); <span class="hljs-comment">//等价于 function.call(undefined, p1, p2) </span>

obj.child.method(p1, p2);<span class="hljs-comment">// 等价于obj.child.method.call(obj.child, p1, p2) </span>

f.call(context, p1, p2); <span class="hljs-comment">// 这种调用形式，才是完整的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>this</code> 就是以上代码中的 <code>context</code> ，就是 <code>call</code> 一个函数时候传的 <code>context</code> 。</p>
<h2 data-id="heading-3"><code>this</code>指向的几种情况</h2>
<p>在分析以下几种情况的时候，可以结合 <code>fn.call()</code> ，就会得出答案，不需要刻意去记忆。</p>
<h3 data-id="heading-4">第一种：<code>f(p1, p2)</code></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>) &#125; 
f()

<span class="hljs-comment">//在此代码中，f() === f.call()</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上实例中，打印出来的结果为 <code>window</code>。为什么呢？因为浏览器规定：</p>
<blockquote>
<p>如果你传的 context 是 null 或 undefined，那么 window 对象就是默认的 context（严格模式下默认 context 是 undefined）</p>
</blockquote>
<p>如果想改变这里 this 的值，可以使用如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js">f.call(obj) <span class="hljs-comment">// 里面的this变成了obj</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">第二种：<code>obj.child.method(p1,p2)</code></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123; <span class="hljs-attr">foo</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>) &#125; &#125; 
obj.foo()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将 <code>obj.foo()</code> 转换为 <code>obj.foo.call(obj)</code> ，这里的 <code>this</code> 即为 <code>obj</code>。</p>
<h3 data-id="heading-6">第三种：包含<code>[]</code></h3>
<p><code>arr[0]()</code>这里面的 <code>this</code> 又是什么呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span> (<span class="hljs-params"></span>)</span>&#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>) &#125; 
<span class="hljs-keyword">var</span> arr = [fn, fn2] 
arr[<span class="hljs-number">0</span>]()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以把 <code>arr[0]</code> 假想成 <code>arr.0()</code> ，这个形式和前面提到的 <code>obj.child.method(p1,p2)</code> 类似，可以直接转换了。<code>arr[0]() - arr.0() - arr.0.call(arr)</code>，易得 <code>this === arr</code>。</p>
<h3 data-id="heading-7">第四种：箭头函数没有 <code>this</code></h3>
<p>箭头函数里并没有 <code>this</code>，如果你在箭头函数里看到 <code>this</code>，你直接把它当作箭头函数外面的 <code>this</code> 即可。外面的 <code>this</code> 是什么，箭头函数里面的 <code>this</code> 就还是什么，因为箭头函数本身不支持 <code>this</code>。</p>
<h3 data-id="heading-8">第五种：<code>EventHandler</code></h3>
<p>在添加事件监听时，也会遇到需要获取 <code>this</code> 的情况：</p>
<pre><code class="hljs language-js copyable" lang="js">button.addEventListener(<span class="hljs-string">'click'</span> ,<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handler</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过前面的 <code>call</code> 方法不能直接判断 <code>this</code> 是什么，我们需要找到 <code>handler</code> 调用时的代码。查找 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FEventTarget%2FaddEventListener%23the_value_of_this_within_the_handler" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/EventTarget/addEventListener#the_value_of_this_within_the_handler" ref="nofollow noopener noreferrer">MDN 文档</a>，可以看到这样一段描述：</p>
<blockquote>
<p>当使用 <code>addEventListener()</code> 为一个元素注册事件的时候，句柄里的 this 值是该元素的引用。其与传递给句柄的 event 参数的 <code>currentTarget 属性的值一样。</code></p>
</blockquote>
<p>转换成可以理解的代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">handler.call(event.currentTarget, event) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以得出其中的 this 就是 <code>event.currentTarget</code> 。</p>
<h2 data-id="heading-9">常见面试题解析</h2>
<p>通过以上方法，我们可以确定大部分情况下的 this 指向，这里放几道经典的面试题，来给大家巩固一下。</p>
<h3 data-id="heading-10">第一题</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = &#123;
  <span class="hljs-attr">name</span>:<span class="hljs-string">"里面的name"</span>,
  <span class="hljs-attr">sayName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"this.name = "</span> + <span class="hljs-built_in">this</span>.name)
  &#125;
&#125;

<span class="hljs-keyword">var</span> name = <span class="hljs-string">"外面的name"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayName</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">var</span> sss = a.sayName;
  sss(); 
  <span class="hljs-comment">// this.name = ??? </span>
  <span class="hljs-comment">// 解析：改成call调用的形式，sss.call(undefined)没有传参，this就是window，因此window.name = 外面的name</span>
  a.sayName(); 
  <span class="hljs-comment">//this.name = ???</span>
  <span class="hljs-comment">// 解析：a.sayName.call(a)，this就是a，this = 里面的name</span>
  (a.sayName)(); 
  <span class="hljs-comment">//this.name = ???</span>
  <span class="hljs-comment">// 解析：js中加不加括号效果都一样，因此相当于(a.sayName).call(a)，this=a，可得this=里面的name</span>
  (b = a.sayName)(); 
  <span class="hljs-comment">//this.name = ???</span>
  <span class="hljs-comment">//解析：括号和上面的效果一样，也就是此题可以转换成b.call(undefined)，那么this=window，window.name=外面的name</span>
&#125;
sayName();
<span class="hljs-comment">// 解析：sayName.call()，this就是window，window.name = 外面的name</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">第二题</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> length = <span class="hljs-number">10</span>; 
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.length)
&#125; 

<span class="hljs-keyword">var</span> obj = &#123; 
    <span class="hljs-attr">length</span>: <span class="hljs-number">5</span>, 
    <span class="hljs-attr">method</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn</span>)</span>&#123; 
    fn() <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>](); 
        &#125; 
&#125;; 

obj.method(fn, <span class="hljs-number">1</span>)

<span class="hljs-comment">// 提问：输出结果是什么？</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用代码转换方法解析题目如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> length = <span class="hljs-number">10</span>; 
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.length)
&#125; 

<span class="hljs-keyword">var</span> obj = &#123; 
    <span class="hljs-attr">length</span>: <span class="hljs-number">5</span>, 
    <span class="hljs-attr">method</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn</span>)</span>&#123; 
        fn() <span class="hljs-comment">//fn.call(undefined)，this = window，window.length = 10 </span>
        <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>](); <span class="hljs-comment">//arguments.0.call(arguments)，this=arguments，也就是[fn, 1]，两个数的数组，结果为2 </span>
            &#125; 
        &#125;; 
        
obj.method(fn, <span class="hljs-number">1</span>) 
<span class="hljs-comment">// obj.method.call(obj, fn, 1)，this = obj </span>
<span class="hljs-comment">// 结合window.length和[fn, 1]，可得本次输出结果为10、2</span>

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            