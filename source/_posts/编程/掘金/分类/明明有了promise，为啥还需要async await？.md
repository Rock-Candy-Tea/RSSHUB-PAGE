
---
title: '明明有了promise，为啥还需要async await？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bb6238602aa437e808055124ed3bd9d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 10 May 2021 18:37:34 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bb6238602aa437e808055124ed3bd9d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>为了让还没听说过这个特性的小伙伴们有一个大致了解，以下是一些关于该特性的简要介绍：</p>
<blockquote>
<p>async/await是一种编写异步代码的新方法。在这之前编写异步代码使用的是回调函数和promise。<br>
async/await实际是建立在promise之上的。因此你不能把它和回调函数搭配使用。<br>
async/await可以使异步代码在形式上更接近于同步代码。这就是它最大的价值。<br></p>
</blockquote>
<h3 data-id="heading-0">语法<br></h3>
<p>假设有一个getJSON方法，它返回一个promise，该promise会被resolve为一个JSON对象。我们想要调用该方法，输出得到的JSON对象，最后返回"done"。</p>
<p>以下是使用promise的实现方式：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> makeRequest = <span class="hljs-function">() =></span>
  getJSON()
    .then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(data)
      <span class="hljs-keyword">return</span> <span class="hljs-string">"done"</span>
    &#125;)
makeRequest()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用async/await则是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> makeRequest = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">await</span> getJSON())
  <span class="hljs-keyword">return</span> <span class="hljs-string">"done"</span>
&#125;

makeRequest()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用async/await时有以下几个区别：</p>
<p>在定义函数时我们使用了async关键字。await关键字只能在使用async定义的函数的内部使用。所有async函数都会返回一个promise，该promise最终resolve的值就是你在函数中return的内容。<br>
由于第一点中的原因，你不能在顶级作用域中await一个函数。因为顶级作用域不是一个async方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// this will not work in top level</span>
<span class="hljs-comment">// await makeRequest()</span>
    
<span class="hljs-comment">// this will work</span>
makeRequest().then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
  <span class="hljs-comment">// do something</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>await getJSON()意味着直到getJSON()返回的promise在resolve之后，console.log才会执行并输出resolove的值。</p>
<h2 data-id="heading-1">为何使用async/await编写出来的代码更好呢？</h2>
<h3 data-id="heading-2">1. 简洁</h3>
<p>看看我们节省了多少代码吧。即使是在这么一个简单的例子中，我们也节省了可观的代码。我们不需要为.then编写一个匿名函数来处理返回结果，也不需要创建一个data变量来保存我们实际用不到的值。我们还避免了代码嵌套。这些小优点会在真实项目中变得更加明显。</p>
<h3 data-id="heading-3">2. 错误处理</h3>
<p>async/await终于使得用同一种构造(古老而好用的try/catch) 处理同步和异步错误成为可能。在下面这段使用promise的代码中，try/catch不能捕获JSON.parse抛出的异常，因为该操作是在promise中进行的。要处理JSON.parse抛出的异常，你需要在promise上调用.catch并重复一遍异常处理的逻辑。通常在生产环境中异常处理逻辑都远比console.log要复杂，因此这会导致大量的冗余代码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> makeRequest = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">try</span> &#123;
    getJSON()
      .then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
        <span class="hljs-comment">// this parse may fail</span>
        <span class="hljs-keyword">const</span> data = <span class="hljs-built_in">JSON</span>.parse(result)
        <span class="hljs-built_in">console</span>.log(data)
      &#125;)
      <span class="hljs-comment">// uncomment this block to handle asynchronous errors</span>
      <span class="hljs-comment">// .catch((err) => &#123;</span>
      <span class="hljs-comment">//   console.log(err)</span>
      <span class="hljs-comment">// &#125;)</span>
    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
        <span class="hljs-built_in">console</span>.log(err)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在看看使用了async/await的情况，catch代码块现在可以捕获JSON.parse抛出的异常了：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> makeRequest = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// this parse may fail</span>
    <span class="hljs-keyword">const</span> data = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-keyword">await</span> getJSON())
    <span class="hljs-built_in">console</span>.log(data)
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-built_in">console</span>.log(err)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3. 条件分支</h3>
<p>假设有如下逻辑的代码。请求数据，然后根据返回数据中的某些内容决定是直接返回这些数据还是继续请求更多数据：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> makeRequest = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> getJSON()
    .then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (data.needsAnotherRequest) &#123;
        <span class="hljs-keyword">return</span> makeAnotherRequest(data)
          .then(<span class="hljs-function"><span class="hljs-params">moreData</span> =></span> &#123;
            <span class="hljs-built_in">console</span>.log(moreData)
            <span class="hljs-keyword">return</span> moreData
          &#125;)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.log(data)
        <span class="hljs-keyword">return</span> data
      &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只是阅读这些代码已经够让你头疼的了。一不小心你就会迷失在这些嵌套(6层)，空格，返回语句中。</p>
<p>在使用async/await改写后，这段代码的可读性大大提高了：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> makeRequest = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> getJSON()
  <span class="hljs-keyword">if</span> (data.needsAnotherRequest) &#123;
    <span class="hljs-keyword">const</span> moreData = <span class="hljs-keyword">await</span> makeAnotherRequest(data);
    <span class="hljs-built_in">console</span>.log(moreData)
    <span class="hljs-keyword">return</span> moreData
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(data)
    <span class="hljs-keyword">return</span> data    
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">4. 中间值</h3>
<p>你可能会遇到这种情况，请求promise1，使用它的返回值请求promise2，最后使用这两个promise的值请求promise3。对应的代码看起来是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> makeRequest = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> promise1()
    .then(<span class="hljs-function"><span class="hljs-params">value1</span> =></span> &#123;
      <span class="hljs-comment">// do something</span>
      <span class="hljs-keyword">return</span> promise2(value1)
        .then(<span class="hljs-function"><span class="hljs-params">value2</span> =></span> &#123;
          <span class="hljs-comment">// do something          </span>
          <span class="hljs-keyword">return</span> promise3(value1, value2)
        &#125;)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果promise3没有用到value1，那么我们就可以把这几个promise改成嵌套的模式。如果你不喜欢这种编码方式，你也可以把value1和value2封装在一个Promsie.all调用中以避免深层次的嵌套：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> makeRequest = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> promise1()
    .then(<span class="hljs-function"><span class="hljs-params">value1</span> =></span> &#123;
      <span class="hljs-comment">// do something</span>
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all([value1, promise2(value1)])
    &#125;)
    .then(<span class="hljs-function">(<span class="hljs-params">[value1, value2]</span>) =></span> &#123;
      <span class="hljs-comment">// do something          </span>
      <span class="hljs-keyword">return</span> promise3(value1, value2)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方式为了保证可读性而牺牲了语义。除了避免嵌套的promise，没有其它理由要把value1和value2放到一个数组里。</p>
<p>同样的逻辑如果换用async/await编写就会非常简单，直观。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> makeRequest = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">const</span> value1 = <span class="hljs-keyword">await</span> promise1()
  <span class="hljs-keyword">const</span> value2 = <span class="hljs-keyword">await</span> promise2(value1)
  <span class="hljs-keyword">return</span> promise3(value1, value2)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">5. 异常堆栈</h3>
<p>假设有一段串行调用多个promise的代码，在promise串中的某一点抛出了异常：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> makeRequest = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> callAPromise()
    .then(<span class="hljs-function">() =></span> callAPromise())
    .then(<span class="hljs-function">() =></span> callAPromise())
    .then(<span class="hljs-function">() =></span> callAPromise())
    .then(<span class="hljs-function">() =></span> callAPromise())
    .then(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"oops"</span>);
    &#125;)
&#125;

makeRequest()
  .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
    <span class="hljs-comment">// output</span>
    <span class="hljs-comment">// Error: oops at callAPromise.then.then.then.then.then (index.js:8:13)</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从promise串返回的异常堆栈中没有包含关于异常是从哪一个环节抛出的信息。更糟糕的是，它还会误导你，它包含的唯一的函数名是callAPromise，然而该函数与此异常并无关系。（这种情况下文件名和行号还是有参考价值的）。</p>
<p>然而，在使用了async/await的代码中，异常堆栈指向了正确的函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> makeRequest = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">await</span> callAPromise()
  <span class="hljs-keyword">await</span> callAPromise()
  <span class="hljs-keyword">await</span> callAPromise()
  <span class="hljs-keyword">await</span> callAPromise()
  <span class="hljs-keyword">await</span> callAPromise()
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"oops"</span>);
&#125;

makeRequest()
  .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
    <span class="hljs-comment">// output</span>
    <span class="hljs-comment">// Error: oops at makeRequest (index.js:7:9)</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这带来的好处在本地开发环境中可能并不明显，但当你想要在生产环境的服务器上获取有意义的异常信息时，这会非常有用。在这种情况下，知道异常来自makeRequest而不是一连串的then调用会有意义的多。</p>
<h3 data-id="heading-7">6. 调试</h3>
<p>最后压轴的一点，使用async/await最大的优势在于它很容易被调试。由于以下两个原因，调试promise一直以来都是很痛苦的。</p>
<p>你不能在一个返回表达式的箭头函数中设置断点（因为没有代码块）</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bb6238602aa437e808055124ed3bd9d~tplv-k3u1fbpfcp-watermark.image" alt="9e73f12c-1d33-11e7-8c5b-98a885b03a49.png" loading="lazy" referrerpolicy="no-referrer">
如果你在一个.then代码块中使用调试器的步进(step-over)功能，调试器并不会进入后续的.then代码块，因为调试器只能跟踪同步代码的『每一步』。</p>
<p>通过使用async/await，你不必再使用箭头函数。你可以对await语句执行步进操作，就好像他们都是普通的同步调用一样。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b4e86514f324f3390eecf37f5fd6c43~tplv-k3u1fbpfcp-watermark.image" alt="d26b3a8a-1d33-11e7-885b-f020ab4999cc.png" loading="lazy" referrerpolicy="no-referrer">
结论
async/await是过去几年中JavaScript引入的最具革命性的特性之一。它使你意识到promise在语法上的糟糕之处，并提供了一种简单，直接的替代方案。</p>
<p><a href="https://loveky.github.io/2017/04/09/translte-6-reasons-why-javascripts-async-await-blows-promises-away/" target="_blank" rel="nofollow noopener noreferrer">参考文章</a></p></div>  
</div>
            