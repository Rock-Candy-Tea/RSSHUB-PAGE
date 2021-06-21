
---
title: 'JS训练营(二) _ JS异步的几种方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3853'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 19:24:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=3853'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第18天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>JavaScript 是一门基于对象的弱类型语言(大家没意见吧)，由于 V8 引擎没有锁机制，JS 的执行环境是单线程的，在日常业务中你不可避免地会遇到异步处理。下面将浅谈几种异步方式</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>JS的任务执行模式只有两种：同步、异步。在同步操作中，如果某个请求或者资源出现死锁或假死，都会造成GUI渲染阻塞，页面基本挂掉的情况，于是，有很多场景下须用到异步处理。同步操作，任务遵循队列顺序，异步操作，就相当于并线了，因此异步任务不具有阻塞效应。
在浏览器端，耗时长的操作都应该异步执行，避免阻塞，比如Ajax操作；做服务器端，异步 将是唯一的模式，因为如果运行同步执行，那么服务器性能将快速被吃掉，服务失去响应，下面将具体介绍几种异步处理方式。</p>
<h2 data-id="heading-1">1.回调函数</h2>
<p>回调函数是异步操作最原始的方法，简单来说就是执行一个操作A，操作A执行完毕之后会执行操作B，依次回调，并且后者依赖前者，条理清晰，缺点也很明显，回调嵌套很深会造成 回调地狱(Callback hell)。</p>
<pre><code class="hljs language-js copyable" lang="js">ajax(url, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 操作A</span>
  ajax(url1, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 操作B</span>
    ajax(url2, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 操作C</span>
    &#125;);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>回调函数的优点是简单、容易理解和实现，缺点是不利于代码的阅读和维护，各个部分之间高度耦合，使得程序结构混乱、流程难以追踪（尤其是多个回调函数嵌套的情况），而且每个任务只能指定一个回调函数。此外它不能使用 try catch 捕获错误，不能直接 return。</p>
<h2 data-id="heading-2">2.延时器 setTimeout</h2>
<p>延时器本身就是异步操作，它不取决于代码的执行顺序，取决于某个事件是否发生。</p>
<pre><code class="hljs language-js copyable" lang="js">fun1.on(<span class="hljs-string">'done'</span>, fun2);
<span class="hljs-comment">// 待fun1发生done事件，就执行fun2。</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// ...</span>
    fun1.trigger(<span class="hljs-string">'done'</span>);
  &#125;, <span class="hljs-number">1000</span>);
&#125;
<span class="hljs-comment">// fun1.trigger('done')表示，执行完成后，立即触发done事件，从而开始执行fun2。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优点：每个事件都可以指定若干个回调函数，可以"去耦合"，有利于实现模块化
缺点：整个程序都要变成事件驱动型，无法保障顺序，运行流程不清晰，不方便看出主流程</p>
<h2 data-id="heading-3">发布/订阅模式</h2>
<p>发布订阅模式，基于一个主题/事件通道，希望接收通知的对象（称为subscriber）通过自定义事件订阅主题，被激活事件的对象（称为publisher）通过发布主题事件的方式被通知。</p>
<p>简单来说：就和用户订阅微信公众号道理一样，公众号可以被若干用户同时订阅，当公众号有新增内容时候，只要发布就好了，用户就能接收到最新的内容。（不等同于 观察者模式）</p>
<p>举个栗子：</p>
<pre><code class="hljs language-js copyable" lang="js">jQuery.subscribe(<span class="hljs-string">'done'</span>, f2);
<span class="hljs-comment">// 操作一：f2向信号中心jQuery订阅done信号</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// ...</span>
    jQuery.publish(<span class="hljs-string">'done'</span>);
  &#125;, <span class="hljs-number">1000</span>);
&#125;
<span class="hljs-comment">// 操作二：f1执行完成后，向中心jQuery发布done信号，从而引发f2的执行。</span>
jQuery.unsubscribe(<span class="hljs-string">'done'</span>, f2);
<span class="hljs-comment">// 操作三：f2完成执行后，可以取消订阅（unsubscribe）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优点：观察者和订阅者之间没有依赖，松散耦合，改进代码管理和潜在的复用。</p>
<h4 data-id="heading-4">附上观察者模式实现代码（JavaScript 版）</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//观察者列表</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ObserverList</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.observerList = [];
&#125;
ObserverList.prototype.add = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.observerList.push(obj);
&#125;;
ObserverList.prototype.count = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.observerList.length;
&#125;;
ObserverList.prototype.get = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">index</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (index > -<span class="hljs-number">1</span> && index < <span class="hljs-built_in">this</span>.observerList.length) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.observerList[index];
  &#125;
&#125;;
ObserverList.prototype.indexOf = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">obj, startIndex</span>) </span>&#123;
  <span class="hljs-keyword">var</span> i = startIndex;
  <span class="hljs-keyword">while</span> (i < <span class="hljs-built_in">this</span>.observerList.length) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.observerList[i] === obj) &#123;
      <span class="hljs-keyword">return</span> i;
    &#125;
    i++;
  &#125;
  <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>;
&#125;;
ObserverList.prototype.removeAt = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">index</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.observerList.splice(index, <span class="hljs-number">1</span>);
&#125;;

<span class="hljs-comment">//目标</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Subject</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.observers = <span class="hljs-keyword">new</span> ObserverList();
&#125;
Subject.prototype.addObserver = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">observer</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.observers.add(observer);
&#125;;
Subject.prototype.removeObserver = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">observer</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.observers.removeAt(<span class="hljs-built_in">this</span>.observers.indexOf(observer, <span class="hljs-number">0</span>));
&#125;;
Subject.prototype.notify = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context</span>) </span>&#123;
  <span class="hljs-keyword">var</span> observerCount = <span class="hljs-built_in">this</span>.observers.count();
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < observerCount; i++) &#123;
    <span class="hljs-built_in">this</span>.observers.get(i).update(context);
  &#125;
&#125;;

<span class="hljs-comment">//观察者</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Observer</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.update = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// ...</span>
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">3.Promise</h2>
<p>ES6 的新特性之一
ES6 的新特性之一，Promise 本意是承诺，在程序中的意思就是承诺我过一段时间后会给你一个结果。这明显是异步操作。Promise 有三种状态：Pending(初始)、Fulfilled(成功)、Rejected(失败)，需要注意的是这个承诺一旦从等待状态变成为其他状态就永远不能更改状态了，比如说一旦状态变为 resolved ，就不能再次改变为 Fulfilled，具有唯一性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 上面栗子的改写</span>
ajax(url)
  .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res);
    <span class="hljs-keyword">return</span> ajax(url1);
  &#125;)
  .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res);
    <span class="hljs-keyword">return</span> ajax(url2);
  &#125;)
  .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> <span class="hljs-built_in">console</span>.log(res));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>promise 的链式调用</p>
<ul>
<li>1.每次调用返回的都是一个新的 Promise 实例(这就是 then 可用链式调用的原因)</li>
<li>2.如果 then 中返回的是一个结果的话会把这个结果传递下一次 then 中的成功回调</li>
<li>3.如果 then 中出现异常,会走下一个 then 的失败回调</li>
<li>4.在 then 中使用了 return，那么 return 的值会被 Promise.resolve() 包装(见例 1，2)</li>
<li>5.then 中可以不传递参数，如果不传递会透到下一个 then 中(见例 3)</li>
<li>6.catch 会捕获到没有捕获的异常</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">read</span>(<span class="hljs-params">url</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    fs.readFile(url, <span class="hljs-string">'utf8'</span>, <span class="hljs-function">(<span class="hljs-params">err, data</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (err) reject(err);
      resolve(data);
    &#125;);
  &#125;);
&#125;
read(<span class="hljs-string">'./name.txt'</span>)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(); <span class="hljs-comment">//then中出现异常,会走下一个then的失败回调</span>
  &#125;) <span class="hljs-comment">//由于下一个then没有失败回调，就会继续往下找，如果都没有，就会被catch捕获到</span>
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'data'</span>);
  &#125;)
  .then()
  .then(<span class="hljs-literal">null</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'then'</span>, err); <span class="hljs-comment">// then error</span>
  &#125;)
  .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error'</span>);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">4.Generators</h2>
<p>Generator 是 ES6 中新增的语法，和 Promise 一样，都可以用来异步编程</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 使用 * 表示这是一个 Generator 函数</span>
<span class="hljs-comment">// 内部可以通过 yield 暂停代码</span>
<span class="hljs-comment">// 通过调用 next 恢复执行</span>
<span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span> + <span class="hljs-number">2</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">2</span>;
  <span class="hljs-keyword">yield</span> <span class="hljs-number">3</span>;
&#125;
<span class="hljs-keyword">let</span> b = test();
<span class="hljs-built_in">console</span>.log(b.next()); <span class="hljs-comment">// > &#123; value: 2, done: false &#125;</span>
<span class="hljs-built_in">console</span>.log(b.next()); <span class="hljs-comment">// > &#123; value: 3, done: false &#125;</span>
<span class="hljs-built_in">console</span>.log(b.next()); <span class="hljs-comment">// > &#123; value: undefined, done: true &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从以上代码可以发现，加上 * 的函数执行后拥有了 next 函数，也就是说函数执行后返回了一个对象。每次调用 next 函数可以继续执行被暂停的代码。以下是Generator 函数的简单实现。</p>
<p>完整的栗子:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generator</span>(<span class="hljs-params">cb</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> object = &#123;
      <span class="hljs-attr">next</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">stop</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;,
    &#125;;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">next</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> ret = cb(object);
        <span class="hljs-keyword">if</span> (ret === <span class="hljs-literal">undefined</span>)
          <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">value</span>: <span class="hljs-literal">undefined</span>,
            <span class="hljs-attr">done</span>: <span class="hljs-literal">true</span>,
          &#125;;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">value</span>: ret,
          <span class="hljs-attr">done</span>: <span class="hljs-literal">false</span>,
        &#125;;
      &#125;,
    &#125;;
  &#125;)();
&#125;
<span class="hljs-comment">// 如果你使用 babel 编译后可以发现 test 函数变成了这样</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> a;
  <span class="hljs-keyword">return</span> generator(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_context</span>) </span>&#123;
    <span class="hljs-keyword">while</span> (<span class="hljs-number">1</span>) &#123;
      <span class="hljs-keyword">switch</span> ((_context.prev = _context.next)) &#123;
        <span class="hljs-comment">// 可以发现通过 yield 将代码分割成几块</span>
        <span class="hljs-comment">// 每次执行 next 函数就执行一块代码</span>
        <span class="hljs-comment">// 并且表明下次需要执行哪块代码</span>
        <span class="hljs-keyword">case</span> <span class="hljs-number">0</span>:
          a = <span class="hljs-number">1</span> + <span class="hljs-number">2</span>;
          _context.next = <span class="hljs-number">4</span>;
          <span class="hljs-keyword">return</span> <span class="hljs-number">2</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-number">4</span>:
          _context.next = <span class="hljs-number">6</span>;
          <span class="hljs-keyword">return</span> <span class="hljs-number">3</span>;
        <span class="hljs-comment">// 执行完毕</span>
        <span class="hljs-keyword">case</span> <span class="hljs-number">6</span>:
        <span class="hljs-keyword">case</span> <span class="hljs-string">'end'</span>:
          <span class="hljs-keyword">return</span> _context.stop();
      &#125;
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">5.async / await</h2>
<p>一个函数如果加上 async ，那么该函数就会返回一个 Promise,并且await 只能在 async 函数中使用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sleep</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'finish'</span>);
      resolve(<span class="hljs-string">'sleep'</span>);
    &#125;, <span class="hljs-number">2000</span>);
  &#125;);
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> value = <span class="hljs-keyword">await</span> sleep();
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'object'</span>);
&#125;
test();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码会先打印 finish 然后再打印 object 。因为 await 会等待 sleep 函数 resolve ，所以即使后面是同步代码，也不会先去执行同步代码再来执行异步代码。async 和 await 相比直接使用 Promise 来说，优势在于处理 then 的调用链，能够更清晰准确的写出代码。缺点在于滥用 await 可能会导致性能问题，因为 await 会阻塞代码，也许之后的异步代码并不依赖于前者，但仍然需要等待前者完成，导致代码失去了并发性。</p>
<p>在举个栗子:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">0</span>;
<span class="hljs-keyword">var</span> b = <span class="hljs-keyword">async</span> () => &#123;
  a = a + (<span class="hljs-keyword">await</span> <span class="hljs-number">10</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'2'</span>, a); <span class="hljs-comment">// -> '2' 10</span>
  <span class="hljs-comment">//首先函数 b 先执行，在执行到 await 10 之前变量 a 还是 0，因为在 await 内部实现了 generators ，generators 会保留堆栈中东西，所以这时候 a = 0 被保存了下来因为 await 是异步操作，所以会先执行 console.log('1', a)这时候同步代码执行完毕，开始执行异步代码，将保存下来的值拿出来使用，这时候 a = 10,然后后面就是常规执行代码了</span>
  a = (<span class="hljs-keyword">await</span> <span class="hljs-number">10</span>) + a;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'3'</span>, a); <span class="hljs-comment">// -> '3' 20</span>
&#125;;
b();
a++;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>, a); <span class="hljs-comment">// -> '1' 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并发请求</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">read</span>(<span class="hljs-params">file</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
    fs.readFile(file, <span class="hljs-string">'utf8'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err, data</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (err) reject(err);
      resolve(data);
    &#125;);
  &#125;);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">readAll</span>(<span class="hljs-params"></span>) </span>&#123;
  read1();
  read2(); <span class="hljs-comment">//这个函数同步执行</span>
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">read1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> r = <span class="hljs-keyword">await</span> read(<span class="hljs-string">'1.txt'</span>, <span class="hljs-string">'utf8'</span>);
  <span class="hljs-built_in">console</span>.log(r);
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">read2</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> r = <span class="hljs-keyword">await</span> read(<span class="hljs-string">'2.txt'</span>, <span class="hljs-string">'utf8'</span>);
  <span class="hljs-built_in">console</span>.log(r);
&#125;
readAll(); <span class="hljs-comment">// 2.txt 3.txt</span>
<span class="hljs-comment">// async/await目前算是比较好的方案</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">参考书籍</h2>
<p>JavaScript 高级程序设计</p>
<p>JavaScript 设计模式</p>
<p>InfoQ 前端面试指南</p></div>  
</div>
            