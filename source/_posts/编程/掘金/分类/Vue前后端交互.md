
---
title: 'Vue前后端交互'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1352'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 07:06:55 GMT
thumbnail: 'https://picsum.photos/400/300?random=1352'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. 前后端交互概述与URL地址格式</h1>
<h2 data-id="heading-1">1.1. 接口调用方式</h2>
<ul>
<li>原生ajax</li>
<li>基于jQuery的ajax</li>
<li>fetch</li>
<li>axios</li>
</ul>
<h2 data-id="heading-2">1.2. url 地址格式有哪些</h2>
<ul>
<li>传统的url</li>
<li>Restful形式的url</li>
</ul>
<h1 data-id="heading-3">2.  异步</h1>
<ul>
<li>JavaScript的执行环境是「单线程」</li>
<li>所谓单线程，是指JS引擎中负责解释和执行JavaScript代码的线程只有一个，也就是一次只能完成一项任务，这个任务执行完后才能执行下一个，它会「阻塞」其他任务。这个任务可称为主线程</li>
<li>异步模式可以一起执行<strong>多个任务</strong></li>
<li>JS中常见的异步调用
<ul>
<li>定时任何</li>
<li>ajax</li>
<li>事件函数</li>
</ul>
</li>
</ul>
<h1 data-id="heading-4">3. promise</h1>
<ul>
<li>
<p>主要解决异步深层嵌套的问题</p>
</li>
<li>
<p>promise 提供了简洁的API 使得异步操作更加容易</p>
</li>
<li>
<p>如何定义一个promise实例</p>
<ul>
<li>我们使用new来构建一个Promise Promise的构造函数接收一个参数，是函数，并且传入两个参数： resolve，reject， 分别表示异步操作执行成功后的回调函数和异步操作执行失败后的回调函数</li>
<li>Promise实例生成以后，可以用then方法指定resolved状态和reject状态的回调函数</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <script type=<span class="hljs-string">"text/javascript"</span>>
    <span class="hljs-comment">/*
     1. Promise基本使用
           我们使用new来构建一个Promise  Promise的构造函数接收一个参数，是函数，并且传入两个参数：           resolve，reject， 分别表示异步操作执行成功后的回调函数和异步操作执行失败后的回调函数
    */</span>
    <span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>)</span>&#123;
      <span class="hljs-comment">//2. 这里用于实现异步任务  setTimeout</span>
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> flag = <span class="hljs-literal">false</span>;
        <span class="hljs-keyword">if</span>(flag) &#123;
          <span class="hljs-comment">//3. 正常情况</span>
          resolve(<span class="hljs-string">'hello'</span>);
        &#125;<span class="hljs-keyword">else</span>&#123;
          <span class="hljs-comment">//4. 异常情况</span>
          reject(<span class="hljs-string">'出错了'</span>);
        &#125;
      &#125;, <span class="hljs-number">100</span>);
    &#125;);
    <span class="hljs-comment">//  5 Promise实例生成以后，可以用then方法指定resolved状态和reject状态的回调函数 </span>
    <span class="hljs-comment">//  在then方法中，你也可以直接return数据而不是Promise对象，在后面的then中就可以接收到数据了  </span>
    p.then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(data)
    &#125;,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">info</span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(info)
    &#125;);
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">3.1. 基于Promise发送Ajax请求</h2>
<ul>
<li>多个请求如何保证顺序
<ul>
<li>通过then 的形式保证顺序</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <script type=<span class="hljs-string">"text/javascript"</span>>
    <span class="hljs-comment">/*
      基于Promise发送Ajax请求
    */</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">queryData</span>(<span class="hljs-params">url</span>) </span>&#123;
     #   <span class="hljs-number">1.1</span> 创建一个<span class="hljs-built_in">Promise</span>实例
      <span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>)</span>&#123;
        <span class="hljs-keyword">var</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
        xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
          <span class="hljs-keyword">if</span>(xhr.readyState != <span class="hljs-number">4</span>) <span class="hljs-keyword">return</span>;
          <span class="hljs-keyword">if</span>(xhr.readyState == <span class="hljs-number">4</span> && xhr.status == <span class="hljs-number">200</span>) &#123;
            # <span class="hljs-number">1.2</span> 处理正常的情况
            resolve(xhr.responseText);
          &#125;<span class="hljs-keyword">else</span>&#123;
            # <span class="hljs-number">1.3</span> 处理异常情况
            reject(<span class="hljs-string">'服务器错误'</span>);
          &#125;
        &#125;;
        xhr.open(<span class="hljs-string">'get'</span>, url);
        xhr.send(<span class="hljs-literal">null</span>);
      &#125;);
      <span class="hljs-keyword">return</span> p;
    &#125;
    # 注意：  这里需要开启一个服务 
    # 在then方法中，你也可以直接<span class="hljs-keyword">return</span>数据而不是<span class="hljs-built_in">Promise</span>对象，在后面的then中就可以接收到数据了
    queryData(<span class="hljs-string">'http://localhost:3000/data'</span>)
      .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(data)
        #  <span class="hljs-number">1.4</span> 想要继续链式编程下去 需要 <span class="hljs-keyword">return</span>  
        <span class="hljs-keyword">return</span> queryData(<span class="hljs-string">'http://localhost:3000/data1'</span>);
      &#125;)
      .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(data);
        <span class="hljs-keyword">return</span> queryData(<span class="hljs-string">'http://localhost:3000/data2'</span>);
      &#125;)
      .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(data)
      &#125;);
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">3.2. Promise 基本API</h2>
<h3 data-id="heading-7">3.2.1. 实例方法</h3>
<h4 data-id="heading-8">3.2.1.1. .then()</h4>
<ul>
<li>得到异步任务正确的结果(then方法指定resolved状态和reject状态的回调函数</li>
</ul>
<p>)</p>
<ul>
<li>then返回值有几种
<ul>
<li>可以返回一个非promise对象</li>
<li>可以返回一个promise对象</li>
</ul>
</li>
</ul>
<h4 data-id="heading-9">3.2.1.2. .catch()</h4>
<ul>
<li>获取异常信息</li>
</ul>
<h4 data-id="heading-10">3.2.1.3. .finally()</h4>
<ul>
<li>成功与否都会执行（不是正式标准）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <script type=<span class="hljs-string">"text/javascript"</span>>
    <span class="hljs-comment">/*
      Promise常用API-实例方法
    */</span>
    <span class="hljs-comment">// console.dir(Promise);</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>)</span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
          <span class="hljs-comment">// resolve(123);</span>
          reject(<span class="hljs-string">'error'</span>);
        &#125;, <span class="hljs-number">100</span>);
      &#125;)
    &#125;
    <span class="hljs-comment">// foo()</span>
    <span class="hljs-comment">//   .then(function(data)&#123;</span>
    <span class="hljs-comment">//     console.log(data)</span>
    <span class="hljs-comment">//   &#125;)</span>
    <span class="hljs-comment">//   .catch(function(data)&#123;</span>
    <span class="hljs-comment">//     console.log(data)</span>
    <span class="hljs-comment">//   &#125;)</span>
    <span class="hljs-comment">//   .finally(function()&#123;</span>
    <span class="hljs-comment">//     console.log('finished')</span>
    <span class="hljs-comment">//   &#125;);</span>
    <span class="hljs-comment">// --------------------------</span>
    <span class="hljs-comment">// 两种写法是等效的</span>
    foo()
      .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
        # 得到异步任务正确的结果
        <span class="hljs-built_in">console</span>.log(data)
      &#125;,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
        # 获取异常信息
        <span class="hljs-built_in">console</span>.log(data)
      &#125;)
      # 成功与否都会执行（不是正式标准） 
      .finally(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'finished'</span>)
      &#125;);
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3.2.2.  静态方法</h3>
<h4 data-id="heading-12">3.2.2.1.  .all()</h4>
<ul>
<li><code>Promise.all</code>方法接受一个数组作参数，数组中的对象（p1、p2、p3）均为promise实例（如果不是一个promise，该项会被用<code>Promise.resolve</code>转换为一个promise)。它的状态由这三个promise实例决定</li>
</ul>
<h4 data-id="heading-13">3.2.2.2. .race()</h4>
<ul>
<li><code>Promise.race</code>方法同样接受一个数组作参数。当p1, p2, p3中有一个实例的状态发生改变（变为<code>fulfilled</code>或<code>rejected</code>），p的状态就跟着改变。并把第一个改变状态的promise的返回值，传给p的回调函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <script type=<span class="hljs-string">"text/javascript"</span>>
    <span class="hljs-comment">/*
      Promise常用API-对象方法
    */</span>
    <span class="hljs-comment">// console.dir(Promise)</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">queryData</span>(<span class="hljs-params">url</span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>)</span>&#123;
        <span class="hljs-keyword">var</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
        xhr.onreadystatechange = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
          <span class="hljs-keyword">if</span>(xhr.readyState != <span class="hljs-number">4</span>) <span class="hljs-keyword">return</span>;
          <span class="hljs-keyword">if</span>(xhr.readyState == <span class="hljs-number">4</span> && xhr.status == <span class="hljs-number">200</span>) &#123;
            <span class="hljs-comment">// 处理正常的情况</span>
            resolve(xhr.responseText);
          &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-comment">// 处理异常情况</span>
            reject(<span class="hljs-string">'服务器错误'</span>);
          &#125;
        &#125;;
        xhr.open(<span class="hljs-string">'get'</span>, url);
        xhr.send(<span class="hljs-literal">null</span>);
      &#125;);
    &#125;
    <span class="hljs-keyword">var</span> p1 = queryData(<span class="hljs-string">'http://localhost:3000/a1'</span>);
    <span class="hljs-keyword">var</span> p2 = queryData(<span class="hljs-string">'http://localhost:3000/a2'</span>);
    <span class="hljs-keyword">var</span> p3 = queryData(<span class="hljs-string">'http://localhost:3000/a3'</span>);
     <span class="hljs-built_in">Promise</span>.all([p1,p2,p3]).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">result</span>)</span>&#123;
       <span class="hljs-comment">//   all 中的参数  [p1,p2,p3]   和 返回的结果一 一对应["HELLO TOM", "HELLO JERRY", "HELLO SPIKE"]</span>
       <span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">//["HELLO TOM", "HELLO JERRY", "HELLO SPIKE"]</span>
     &#125;)
    <span class="hljs-built_in">Promise</span>.race([p1,p2,p3]).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">result</span>)</span>&#123;
      <span class="hljs-comment">// 由于p1执行较快，Promise的then()将获得结果'P1'。p2,p3仍在继续执行，但执行结果将被丢弃。</span>
      <span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">// "HELLO TOM"</span>
    &#125;)
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">4. fetch</h1>
<ul>
<li>Fetch API是新的ajax解决方案 Fetch会返回Promise</li>
<li><strong>fetch不是ajax的进一步封装，而是原生js，没有使用XMLHttpRequest对象</strong>。</li>
<li>fetch(url, options).then(）</li>
<li>fetch 就是 ajax + Promise. 使用的方式和 jquery 提供的 $.ajax() 差不多</li>
<li>fetch默认是get请求</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <script type=<span class="hljs-string">"text/javascript"</span>>
    <span class="hljs-comment">/*
      Fetch API 基本用法
        fetch(url).then()
        第一个参数请求的路径   Fetch会返回Promise   所以我们可以使用then 拿到请求成功的结果 
    */</span>
    fetch(<span class="hljs-string">'http://localhost:3000/fdata'</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
      <span class="hljs-comment">// text()方法属于fetchAPI的一部分，它返回一个Promise实例对象，用于获取后台返回的数据</span>
      <span class="hljs-keyword">return</span> data.text();
    &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
      <span class="hljs-comment">//   在这个then里面我们能拿到最终的数据  </span>
      <span class="hljs-built_in">console</span>.log(data);
    &#125;)
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">4.1. fetch API 中的 HTTP 请求</h2>
<ul>
<li>
<p>fetch(url, options).then(）</p>
</li>
<li>
<p>HTTP协议，它给我们提供了很多的方法，如POST，GET，DELETE，UPDATE，PATCH和PUT</p>
<ul>
<li>默认的是 GET 请求</li>
<li>需要在 options 对象中 指定对应的 method method:请求使用的方法</li>
<li>post 和 普通 请求的时候 需要在options 中 设置 请求头 headers 和 body</li>
</ul>
</li>
<li>
<p>Fetch中 get 和delete的传参</p>
<ul>
<li>fetch(url, options).then(）</li>
<li>GET参数传递 - 传统URL 通过url ？ 的形式传参</li>
<li>restful形式的URL 通过/ 的形式传递参数</li>
<li>DELETE请求方式参数传递 和 get一样</li>
</ul>
</li>
<li>
<p>Post和put如何传递参数</p>
<ul>
<li>需要在body 中传递参数</li>
<li>需要指定headers因为默认Content-Type不是application/x-www-form-urlencoded</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">   <script type=<span class="hljs-string">"text/javascript"</span>>
        <span class="hljs-comment">/*
              Fetch API 调用接口传递参数
        */</span>
       #<span class="hljs-number">1.1</span> GET参数传递 - 传统URL  通过url  ？ 的形式传参 
        fetch(<span class="hljs-string">'http://localhost:3000/books?id=123'</span>, &#123;
                # get 请求可以省略不写 默认的是GET 
                <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>
            &#125;)
            .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                # 它返回一个<span class="hljs-built_in">Promise</span>实例对象，用于获取后台返回的数据
                <span class="hljs-keyword">return</span> data.text();
            &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                # 在这个then里面我们能拿到最终的数据  
                <span class="hljs-built_in">console</span>.log(data)
            &#125;);
      #<span class="hljs-number">1.2</span>  GET参数传递  restful形式的URL  通过/ 的形式传递参数  即  id = <span class="hljs-number">456</span> 和id后台的配置有关   
        fetch(<span class="hljs-string">'http://localhost:3000/books/456'</span>, &#123;
                # get 请求可以省略不写 默认的是GET 
                <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>
            &#125;)
            .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                <span class="hljs-keyword">return</span> data.text();
            &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                <span class="hljs-built_in">console</span>.log(data)
            &#125;);
       #<span class="hljs-number">2.1</span>  DELETE请求方式参数传递      删除id  是  id=<span class="hljs-number">789</span>
        fetch(<span class="hljs-string">'http://localhost:3000/books/789'</span>, &#123;
                <span class="hljs-attr">method</span>: <span class="hljs-string">'delete'</span>
            &#125;)
            .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                <span class="hljs-keyword">return</span> data.text();
            &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                <span class="hljs-built_in">console</span>.log(data)
            &#125;);
       #<span class="hljs-number">3</span> POST请求传参
        fetch(<span class="hljs-string">'http://localhost:3000/books'</span>, &#123;
                <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
                # <span class="hljs-number">3.1</span>  传递数据 
                <span class="hljs-attr">body</span>: <span class="hljs-string">'uname=lisi&pwd=123'</span>,
                #  <span class="hljs-number">3.2</span>  设置请求头 
                <span class="hljs-attr">headers</span>: &#123;
                    <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/x-www-form-urlencoded'</span>
                &#125;
            &#125;)
            .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                <span class="hljs-keyword">return</span> data.text();
            &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                <span class="hljs-built_in">console</span>.log(data)
            &#125;);
       # POST请求传参
        fetch(<span class="hljs-string">'http://localhost:3000/books'</span>, &#123;
                <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
                <span class="hljs-attr">body</span>: <span class="hljs-built_in">JSON</span>.stringify(&#123;
                    <span class="hljs-attr">uname</span>: <span class="hljs-string">'张三'</span>,
                    <span class="hljs-attr">pwd</span>: <span class="hljs-string">'456'</span>
                &#125;),
                <span class="hljs-attr">headers</span>: &#123;
                    <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/json'</span>
                &#125;
            &#125;)
            .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                <span class="hljs-keyword">return</span> data.text();
            &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                <span class="hljs-built_in">console</span>.log(data)
            &#125;);
        # PUT请求传参     修改id 是 <span class="hljs-number">123</span> 的 
        fetch(<span class="hljs-string">'http://localhost:3000/books/123'</span>, &#123;
                <span class="hljs-attr">method</span>: <span class="hljs-string">'put'</span>,
                <span class="hljs-attr">body</span>: <span class="hljs-built_in">JSON</span>.stringify(&#123;
                    <span class="hljs-attr">uname</span>: <span class="hljs-string">'张三'</span>,
                    <span class="hljs-attr">pwd</span>: <span class="hljs-string">'789'</span>
                &#125;),
                <span class="hljs-attr">headers</span>: &#123;
                    <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/json'</span>
                &#125;
            &#125;)
            .then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                <span class="hljs-keyword">return</span> data.text();
            &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
                <span class="hljs-built_in">console</span>.log(data)
            &#125;);
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">4.2. fetchAPI 中 响应格式</h2>
<ul>
<li>用fetch来获取数据，如果响应正常返回，我们首先看到的是一个response对象，其中包括返回的一堆原始字节，这些字节需要在收到后，需要我们通过调用方法将其转换为相应格式的数据，比如<code>JSON</code>，<code>BLOB</code>或者<code>TEXT</code>等等</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">/*
      Fetch响应结果的数据格式
    */</span>
    fetch(<span class="hljs-string">'http://localhost:3000/json'</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
      <span class="hljs-comment">// return data.json();   //  将获取到的数据使用 json 转换对象</span>
      <span class="hljs-keyword">return</span> data.text(); <span class="hljs-comment">//  //  将获取到的数据 转换成字符串 </span>
    &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
      <span class="hljs-comment">// console.log(data.uname)</span>
      <span class="hljs-comment">// console.log(typeof data)</span>
      <span class="hljs-keyword">var</span> obj = <span class="hljs-built_in">JSON</span>.parse(data);
      <span class="hljs-built_in">console</span>.log(obj.uname,obj.age,obj.gender)
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-17">5. axios</h1>
<ul>
<li>基于promise用于浏览器和node.js的http客户端</li>
<li>支持浏览器和node.js</li>
<li>支持promise</li>
<li>能拦截请求和响应</li>
<li>自动转换JSON数据</li>
<li>能转换请求和响应数据</li>
</ul>
<h2 data-id="heading-18">5.1. axios基础用法</h2>
<ul>
<li>
<p>get和 delete请求传递参数</p>
<ul>
<li>通过传统的url 以 ? 的形式传递参数</li>
<li>restful 形式传递参数</li>
<li>通过params 形式传递参数</li>
</ul>
</li>
<li>
<p>post 和 put 请求传递参数</p>
<ul>
<li>通过选项传递参数</li>
<li>通过 URLSearchParams 传递参数</li>
</ul>
</li>
<li>
<p>响应结果主要属性</p>
<ul>
<li>data 实际响应回来的数据</li>
<li>headers 响应头</li>
<li>status响应状态码</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    # <span class="hljs-number">1.</span> 发送get 请求 
    axios.get(<span class="hljs-string">'http://localhost:3000/adata'</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">ret</span>)</span>&#123; 
      #  拿到 ret 是一个对象      所有的对象都存在 ret 的data 属性里面
      <span class="hljs-comment">// 注意data属性是固定的用法，用于获取后台的实际数据</span>
      <span class="hljs-comment">// console.log(ret.data)</span>
      <span class="hljs-built_in">console</span>.log(ret)
    &#125;)
    # <span class="hljs-number">2.</span>  get 请求传递参数
    # <span class="hljs-number">2.1</span>  通过传统的url  以 ? 的形式传递参数
    axios.get(<span class="hljs-string">'http://localhost:3000/axios?id=123'</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">ret</span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(ret.data)
    &#125;)
    # <span class="hljs-number">2.2</span>  restful 形式传递参数 
    axios.get(<span class="hljs-string">'http://localhost:3000/axios/123'</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">ret</span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(ret.data)
    &#125;)
    # <span class="hljs-number">2.3</span>  通过params  形式传递参数 
    axios.get(<span class="hljs-string">'http://localhost:3000/axios'</span>, &#123;
      <span class="hljs-attr">params</span>: &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">789</span>
      &#125;
    &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">ret</span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(ret.data)
    &#125;)
    #<span class="hljs-number">3</span> axios <span class="hljs-keyword">delete</span> 请求传参     传参的形式和 get 请求一样
    axios.delete(<span class="hljs-string">'http://localhost:3000/axios'</span>, &#123;
      <span class="hljs-attr">params</span>: &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">111</span>
      &#125;
    &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">ret</span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(ret.data)
    &#125;)
    # <span class="hljs-number">4</span>  axios 的 post 请求
    # <span class="hljs-number">4.1</span>  通过选项传递参数
    axios.post(<span class="hljs-string">'http://localhost:3000/axios'</span>, &#123;
      <span class="hljs-attr">uname</span>: <span class="hljs-string">'lisi'</span>,
      <span class="hljs-attr">pwd</span>: <span class="hljs-number">123</span>
    &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">ret</span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(ret.data)
    &#125;)
    # <span class="hljs-number">4.2</span>  通过 URLSearchParams  传递参数 
    <span class="hljs-keyword">var</span> params = <span class="hljs-keyword">new</span> URLSearchParams();
    params.append(<span class="hljs-string">'uname'</span>, <span class="hljs-string">'zhangsan'</span>);
    params.append(<span class="hljs-string">'pwd'</span>, <span class="hljs-string">'111'</span>);
    axios.post(<span class="hljs-string">'http://localhost:3000/axios'</span>, params).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">ret</span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(ret.data)
    &#125;)
    #<span class="hljs-number">5</span>  axios put 请求传参   和 post 请求一样 
    axios.put(<span class="hljs-string">'http://localhost:3000/axios/123'</span>, &#123;
      <span class="hljs-attr">uname</span>: <span class="hljs-string">'lisi'</span>,
      <span class="hljs-attr">pwd</span>: <span class="hljs-number">123</span>
    &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">ret</span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(ret.data)
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">5.2. axios 全局配置</h2>
<pre><code class="hljs language-js copyable" lang="js">#  配置公共的请求头 
axios.defaults.baseURL = <span class="hljs-string">'https://api.example.com'</span>;
#  配置 超时时间
axios.defaults.timeout = <span class="hljs-number">2500</span>;
#  配置公共的请求头
axios.defaults.headers.common[<span class="hljs-string">'Authorization'</span>] = AUTH_TOKEN;
# 配置公共的 post 的 Content-Type
axios.defaults.headers.post[<span class="hljs-string">'Content-Type'</span>] = <span class="hljs-string">'application/x-www-form-urlencoded'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">5.3. axios 拦截器</h2>
<ul>
<li>
<p>请求拦截器</p>
<ul>
<li>
<p>请求拦截器的作用是在请求发送前进行一些操作</p>
<ul>
<li>例如在每个请求体里加上token，统一做了处理如果以后要改也非常容易</li>
</ul>
</li>
</ul>
</li>
<li>
<p>响应拦截器</p>
<ul>
<li>
<p>响应拦截器的作用是在接收到响应后进行一些操作</p>
<ul>
<li>例如在服务器返回登录状态失效，需要重新登录的时候，跳转到登录页</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    # <span class="hljs-number">1.</span> 请求拦截器 
    axios.interceptors.request.use(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">config</span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(config.url)
      # <span class="hljs-number">1.1</span>  任何请求都会经过这一步   在发送请求之前做些什么   
      config.headers.mytoken = <span class="hljs-string">'nihao'</span>;
      # <span class="hljs-number">1.2</span>  这里一定要<span class="hljs-keyword">return</span>   否则配置不成功  
      <span class="hljs-keyword">return</span> config;
    &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>)</span>&#123;
       #<span class="hljs-number">1.3</span> 对请求错误做点什么    
      <span class="hljs-built_in">console</span>.log(err)
    &#125;)
    #<span class="hljs-number">2.</span> 响应拦截器 
    axios.interceptors.response.use(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">res</span>) </span>&#123;
      #<span class="hljs-number">2.1</span>  在接收响应做些什么  
      <span class="hljs-keyword">var</span> data = res.data;
      <span class="hljs-keyword">return</span> data;
    &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>)</span>&#123;
      #<span class="hljs-number">2.2</span> 对响应错误做点什么  
      <span class="hljs-built_in">console</span>.log(err)
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-21">6. async 和 await</h1>
<ul>
<li>
<p>async作为一个关键字放到函数前面</p>
<ul>
<li>任何一个<code>async</code>函数都会隐式返回一个<code>promise</code></li>
</ul>
</li>
<li>
<p><code>await</code>关键字只能在使用<code>async</code>定义的函数中使用</p>
<ul>
<li>await后面可以直接跟一个 Promise实例对象</li>
<li>await函数不能单独使用</li>
</ul>
</li>
<li>
<p><strong>async/await 让异步代码看起来、表现起来更像同步代码</strong></p>
</li>
<li>
<p>async和await好处</p>
<ul>
<li>async搭配await是ES7提出的，它的实现是基于Promise</li>
</ul>
</li>
<li>
<p>注意细节点</p>
<ul>
<li>await函数不能单独使用，而且async函数返回的是一个Promise对象，可以使用then函数添加回调函数。当函数执行的时候，一旦遇到await函数就会先返回一个Promise对象，等到异步操作完成，再去执行后面的语句</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    # <span class="hljs-number">1.</span>  <span class="hljs-keyword">async</span> 基础用法
    # <span class="hljs-number">1.1</span> <span class="hljs-keyword">async</span>作为一个关键字放到函数前面
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">queryData</span>(<span class="hljs-params"></span>) </span>&#123;
      # <span class="hljs-number">1.2</span> <span class="hljs-keyword">await</span>关键字只能在使用<span class="hljs-keyword">async</span>定义的函数中使用      <span class="hljs-keyword">await</span>后面可以直接跟一个 <span class="hljs-built_in">Promise</span>实例对象
      <span class="hljs-keyword">var</span> ret = <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>)</span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
          resolve(<span class="hljs-string">'nihao'</span>)
        &#125;,<span class="hljs-number">1000</span>);
      &#125;)
      <span class="hljs-comment">// console.log(ret.data)</span>
      <span class="hljs-keyword">return</span> ret;
    &#125;
    # <span class="hljs-number">1.3</span> 任何一个<span class="hljs-keyword">async</span>函数都会隐式返回一个promise   我们可以使用then 进行链式编程
    queryData().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(data)
    &#125;)
    #<span class="hljs-number">2.</span>  <span class="hljs-keyword">async</span>    函数处理多个异步函数
    axios.defaults.baseURL = <span class="hljs-string">'http://localhost:3000'</span>;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">queryData</span>(<span class="hljs-params"></span>) </span>&#123;
      # <span class="hljs-number">2.1</span>  添加<span class="hljs-keyword">await</span>之后 当前的<span class="hljs-keyword">await</span> 返回结果之后才会执行后面的代码   
      
      <span class="hljs-keyword">var</span> info = <span class="hljs-keyword">await</span> axios.get(<span class="hljs-string">'async1'</span>);
      #<span class="hljs-number">2.2</span>  让异步代码看起来、表现起来更像同步代码
      <span class="hljs-keyword">var</span> ret = <span class="hljs-keyword">await</span> axios.get(<span class="hljs-string">'async2?info='</span> + info.data);
      <span class="hljs-keyword">return</span> ret.data;
    &#125;
    queryData().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>)</span>&#123;
      <span class="hljs-built_in">console</span>.log(data)
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            