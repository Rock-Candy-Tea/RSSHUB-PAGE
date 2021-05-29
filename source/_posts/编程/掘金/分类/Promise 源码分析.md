
---
title: 'Promise 源码分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1811'
author: 掘金
comments: false
date: Fri, 28 May 2021 03:41:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=1811'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1、引入Promise</h3>
<ul>
<li>字面意义"承诺"，将来的某个时间进行兑现</li>
<li>主要解决地域回调问题</li>
<li>Promise是异步的一种解决方案</li>
<li>Promise是一个构造函数，有属性和方法；通过new实例化使用</li>
</ul>
<h3 data-id="heading-1">2、Promise相关特点</h3>
<blockquote>
<p><strong>Promise - ( 兑现承诺 )</strong></p>
<ul>
<li>要么成功要不失败，只能有一个结果</li>
</ul>
</blockquote>
<blockquote>
<p><strong>excutor - ( 执行器函数 )</strong></p>
<ul>
<li>
<p>当 new Promise(excutor) 的时候，excutor函数自动执行；( <code>同步执行</code> )</p>
</li>
<li>
<p>excutor函数有两个参数：resolve - 成功的回调函数 和 reject - 失败的回调函数</p>
</li>
</ul>
</blockquote>
<blockquote>
<p><strong>then - ( 链式调用 )</strong></p>
<ul>
<li>
<p><code>then是异步调用的：</code> 内部是利用微任务 或 宏任务处理</p>
</li>
<li>
<p><code>每次调用then都返回一个新的Promise对象</code>（继续下次链式调用）</p>
</li>
<li>
<p>then(call1,call2)方法里两个回调函数，即成功的回调和失败回调</p>
</li>
<li>
<p>then(call1,call2)本次执行call2方法，如果继续调用then方法</p>
<ul>
<li>本次call2执行结果为"成功"，下次then就执行call1</li>
<li>本次call2执行结果为"失败"，下次then就执行call2</li>
</ul>
</li>
<li>
<p><code>穿透作用：</code>如果上个then函数没，没有对应函数的处理，就会在下一个then的回调对应执行</p>
<ul>
<li>let promise = new Promise((resolve, reject) => &#123; resolve("new Promise") &#125;);</li>
<li>promise.then()</li>
<li>.then((value) => &#123;
<ul>
<li>console.log("---", value); //new Promise</li>
</ul>
</li>
<li>&#125;, (reason) => &#123;
<ul>
<li>console.log("---", reason);</li>
</ul>
</li>
<li>&#125;)</li>
</ul>
</li>
</ul>
</blockquote>
<blockquote>
<p><strong>catch - ( 链式调用 )</strong></p>
<ul>
<li>
<p>内部的执行原理：then(null,callBacks)</p>
</li>
<li>
<p>不影响继续调用 then 方法</p>
</li>
<li>
<p>会受到前面then方法的第二个回调函数<code>拦截</code></p>
</li>
</ul>
</blockquote>
<h3 data-id="heading-2">3、源码解析</h3>
<h5 data-id="heading-3">步骤分析</h5>
<ul>
<li>1、new MyPromise() 时自动触发executor函数（同步执行）</li>
<li>2、调用then方法时，收集成功或失败函数（前提executor内异步执行）</li>
<li>3、手动调用resolve或reject时，异步循环执行上一步收集的函数</li>
<li>4、对上一步每次函数的执行结果放到resolvePromise函数中做处理</li>
</ul>
<h5 data-id="heading-4">源码实现</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">"PENDING"</span>,
  FULFILLED = <span class="hljs-string">"FULFILLED"</span>,
  REJECTED = <span class="hljs-string">"REJECTED"</span>;


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
  <span class="hljs-comment">//executor</span>
  <span class="hljs-comment">///1、自执行函数，new MyPromise时立刻执行</span>
  <span class="hljs-comment">///2、包含两个参数：resolve和reject函数</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;

    <span class="hljs-built_in">this</span>.status = PENDING;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>;
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span>;

    <span class="hljs-comment">// 分别盛放所有的成功或失败的回调函数</span>
    <span class="hljs-built_in">this</span>.onFulfilledCallbacks = [];
    <span class="hljs-built_in">this</span>.onRejectedCallbacks = [];

    <span class="hljs-comment">// 不放到原型上：resolve和reject</span>
    <span class="hljs-comment">// 由于每次new的时候都需要创建自己的resolve和reject方法</span>
    <span class="hljs-keyword">const</span> resolve = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status == PENDING) &#123;<span class="hljs-comment">//状态只能被修改一次</span>
        <span class="hljs-built_in">this</span>.value = value;
        <span class="hljs-built_in">this</span>.status = FULFILLED;

        <span class="hljs-comment">//发布：迭代执行成功函数</span>
        <span class="hljs-built_in">this</span>.onFulfilledCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn());
      &#125;
    &#125;
    <span class="hljs-keyword">const</span> reject = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status == PENDING) &#123;<span class="hljs-comment">//状态只能被修改一次</span>
        <span class="hljs-built_in">this</span>.reason = value;
        <span class="hljs-built_in">this</span>.status = REJECTED;

        <span class="hljs-comment">//发布：迭代执行失败函数</span>
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn());
      &#125;
    &#125;

    <span class="hljs-comment">// 实例化时：executor函数内异常捕获处理 - 例如：throw new Error()</span>
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// executor：此方法同步执行</span>
      executor(resolve, reject);
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      reject(error)
    &#125;
  &#125;

  <span class="hljs-comment">// 每个then都返回一个新的promie对象，进行链式调用</span>
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;

    <span class="hljs-comment">// 解决穿透问题：如果onFulfilled或onRejected为空，默认给一个函数</span>
    <span class="hljs-comment">// 例如：promise2.then().then().then((resolve,reject)=>&#123;...&#125;)</span>
    onFulfilled = <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">"function"</span> ? onFulfilled : <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> value;
    onRejected = <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">"function"</span> ? onRejected : <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123; <span class="hljs-keyword">throw</span> reason &#125;;

    <span class="hljs-comment">// 创建一个promise对象作为返回值</span>
    <span class="hljs-keyword">let</span> promise2 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;

      <span class="hljs-comment">// 以下代码使用setTimeout包裹：</span>
      <span class="hljs-comment">/// 1、使用setTimeout（宏任务）的处理方式，确保可以取到当前promise2的对象</span>
      <span class="hljs-comment">/// 2、源码中用的是微任务的处理方式</span>
      <span class="hljs-comment">/// 3、保障了多次then的链式调用，等待上次执行结束后才能执行下次（ 事件循环机制 ）</span>

      <span class="hljs-comment">// 下列代码res的值作为resolve和reject返回值</span>
      <span class="hljs-comment">/// 1、可能为普通值</span>
      <span class="hljs-comment">/// 2、可能为primise对象</span>
      <span class="hljs-comment">/// 3、使用resolvePromise方法进行处理</span>

      <span class="hljs-comment">// 同步代码执行executor时，且状态为FULFILLED</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status == FULFILLED) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-comment">// 处理结果中抛出异常的情况，如：throw new Error()</span>
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> res = onFulfilled(<span class="hljs-built_in">this</span>.value)
            <span class="hljs-comment">// 处理返回值的函数</span>
            resolvePromise(promise2, res, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (error) &#123;
            reject(error);
          &#125;
        &#125;, <span class="hljs-number">0</span>);<span class="hljs-comment">//具体延迟执行的时间>=4ms;</span>
      &#125;

      <span class="hljs-comment">// 同步代码执行executor时，且状态为REJECTED</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status == REJECTED) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> res = onRejected(<span class="hljs-built_in">this</span>.reason)
            resolvePromise(promise2, res, resolve, reject)
          &#125; <span class="hljs-keyword">catch</span> (error) &#123;
            reject(error);
          &#125;
        &#125;, <span class="hljs-number">0</span>);
      &#125;

      <span class="hljs-comment">// 异步代码执行executor时：收集所有的成功或失败的回调函数</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.status == PENDING) &#123;
        <span class="hljs-comment">// 订阅：收集成功函数</span>
        <span class="hljs-built_in">this</span>.onFulfilledCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">let</span> res = onFulfilled(<span class="hljs-built_in">this</span>.value)
              resolvePromise(promise2, res, resolve, reject)
            &#125; <span class="hljs-keyword">catch</span> (error) &#123;
              reject(error);
            &#125;
          &#125;, <span class="hljs-number">0</span>);
        &#125;)
        <span class="hljs-comment">// 订阅：收集失败函数</span>
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">let</span> res = onRejected(<span class="hljs-built_in">this</span>.reason)
              resolvePromise(promise2, res, resolve, reject)
            &#125; <span class="hljs-keyword">catch</span> (error) &#123;
              reject(error);
            &#125;
          &#125;, <span class="hljs-number">0</span>);
        &#125;)
      &#125;
    &#125;)

    <span class="hljs-keyword">return</span> promise2;
  &#125;

  <span class="hljs-keyword">catch</span>(errorCallback) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>, errorCallback)
  &#125;

  <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      resolve(value);
    &#125;)
  &#125;

  <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      reject(reason);
    &#125;)
  &#125;

  <span class="hljs-comment">//所有实例执行成功才算成功</span>
  <span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">promiseArray</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(promiseArray)) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">" The arguments should be an array!"</span>)
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> resultArray = [];
        <span class="hljs-keyword">const</span> length = promiseArray.length;

        <span class="hljs-comment">// 有一个实例失败直会接执行reject方法；</span>
        <span class="hljs-comment">//否则等待所有实例执行完执行resolve方法</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
          promiseArray[i].then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
            resultArray.push(data);
            <span class="hljs-keyword">if</span> (resultArray.length === length) &#123;
              resolve(resultArray)
            &#125;
          &#125;, reject)
        &#125;
      &#125;
      <span class="hljs-keyword">catch</span> (e) &#123;
        reject(e)
      &#125;
    &#125;)
  &#125;

  <span class="hljs-comment">// 返回第一个改变状态的结果，无论成功的还是失败的</span>
  <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promiseArray</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(promiseArray)) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">" The arguments should be an array!"</span>)
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> length = promiseArray.length;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
          promiseArray[i].then(resolve, reject);
        &#125;
      &#125;
      <span class="hljs-keyword">catch</span> (e) &#123;
        reject(e)
      &#125;
    &#125;)
  &#125;
&#125;

<span class="hljs-comment">// 处理then中成功函数或失败函数的返回值</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">promise2, res, resolve, reject</span>) </span>&#123;

  <span class="hljs-comment">// 如果promise2等于res，抛出异常</span>
  <span class="hljs-comment">// 例如：let promise1 = promise.then((value) => &#123; return promise1; &#125;)</span>
  <span class="hljs-keyword">if</span> (promise2 == res) &#123;
    <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Changing cycle detected for promise #<MyPromise>'</span>))
  &#125;

  <span class="hljs-comment">// 如果res是一个object或function时</span>
  <span class="hljs-keyword">if</span> ((<span class="hljs-keyword">typeof</span> res === <span class="hljs-string">"object"</span> && res !== <span class="hljs-literal">null</span>) || (<span class="hljs-keyword">typeof</span> res === <span class="hljs-string">"function"</span>)) &#123;
    <span class="hljs-comment">//保证res.then取值的时候出现异常</span>
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">let</span> then = res.then;<span class="hljs-comment">//判断是否为 promise 对象</span>

      <span class="hljs-comment">//判断回调函数是否被多次调用过：例如 - resolve();resolve();连续多次调用</span>
      <span class="hljs-keyword">let</span> called = <span class="hljs-literal">false</span>;

      <span class="hljs-comment">//为promise对象</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> then === <span class="hljs-string">"function"</span>) &#123;
        then.call(res, <span class="hljs-function">(<span class="hljs-params">y</span>) =></span> &#123;
          <span class="hljs-comment">// 避免重复调用</span>
          <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;
          called = <span class="hljs-literal">true</span>;
          <span class="hljs-comment">// 如果Y为Promise对象，递归调用</span>
          <span class="hljs-comment">// 如果Y为普通值，相当于下次直接调用 - resolve()</span>
          resolvePromise(promise2, y, resolve, reject)
        &#125;, <span class="hljs-function">(<span class="hljs-params">r</span>) =></span> &#123;
          <span class="hljs-comment">// 避免重复调用</span>
          <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;
          called = <span class="hljs-literal">true</span>;
          reject(r)
        &#125;)
      &#125;
      <span class="hljs-keyword">else</span> &#123;
        resolve(res);
      &#125;
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-comment">// 避免重复调用</span>
      <span class="hljs-keyword">if</span> (called) <span class="hljs-keyword">return</span>;
      called = <span class="hljs-literal">true</span>;
      reject(error)
    &#125;
  &#125;
  <span class="hljs-comment">//res为普通值</span>
  <span class="hljs-keyword">else</span> &#123;
    resolve(res);
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = MyPromise;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            