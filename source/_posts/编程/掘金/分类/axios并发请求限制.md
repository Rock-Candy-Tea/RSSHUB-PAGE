
---
title: 'axios并发请求限制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2016'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 20:41:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=2016'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">限制axios并发请求（TypeScript)</h3>
<p>假设有一种场景，用户需要同时上传1000张图片，每张图片都需要单独发送post请求，但是浏览器或服务器会对并发请求数进行限制，如果前端一次发送的请求超出限制可能会报错。所以需要对前端并发请求数进行限制。</p>
<p>这里把异步任务封装成Promise。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/** <span class="hljs-doctag">@format </span>*/</span>

<span class="hljs-comment">/**
 * 封装axios并发请求数
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LimitPromise</span> </span>&#123;
  <span class="hljs-keyword">private</span> _max: <span class="hljs-built_in">number</span>;
  <span class="hljs-keyword">private</span> _count: <span class="hljs-built_in">number</span>;
  <span class="hljs-keyword">private</span> _taskQueue: <span class="hljs-built_in">any</span>[];

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">max: <span class="hljs-built_in">number</span></span>)</span> &#123;
    <span class="hljs-comment">// 异步任务“并发”上限</span>
    <span class="hljs-built_in">this</span>._max = max || <span class="hljs-number">6</span>;
    <span class="hljs-comment">// 当前正在执行的任务数量</span>
    <span class="hljs-built_in">this</span>._count = <span class="hljs-number">0</span>;
    <span class="hljs-comment">// 等待执行的任务队列</span>
    <span class="hljs-built_in">this</span>._taskQueue = [];
  &#125;

  <span class="hljs-comment">/**
   * 调用器，将异步任务函数和它的参数传入
   * <span class="hljs-doctag">@param </span>caller 异步任务函数，它必须是async函数或者返回Promise的函数
   * <span class="hljs-doctag">@param </span>args 异步任务函数的参数列表
   * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Promise<unknown>&#125;</span> </span>返回一个Promise
   */</span>
  <span class="hljs-function"><span class="hljs-title">call</span>(<span class="hljs-params">caller: (...arg: <span class="hljs-built_in">any</span>[]) => <span class="hljs-built_in">any</span></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> task = <span class="hljs-built_in">this</span>._createTask(caller, resolve, reject);
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._count >= <span class="hljs-built_in">this</span>._max) &#123;
        <span class="hljs-built_in">this</span>._taskQueue.push(task);
      &#125; <span class="hljs-keyword">else</span> &#123;
        task();
      &#125;
    &#125;);
  &#125;

  <span class="hljs-comment">/**
   * 创建一个任务
   * <span class="hljs-doctag">@param </span>caller 实际执行的函数
   * <span class="hljs-doctag">@param </span>args 执行函数的参数
   * <span class="hljs-doctag">@param <span class="hljs-variable">resolve</span></span>
   * <span class="hljs-doctag">@param <span class="hljs-variable">reject</span></span>
   * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Function&#125;</span> </span>返回一个任务函数
   * <span class="hljs-doctag">@private</span>
   */</span>
  <span class="hljs-function"><span class="hljs-title">_createTask</span>(<span class="hljs-params">
    caller: (...arg: <span class="hljs-built_in">any</span>[]) => <span class="hljs-built_in">any</span>,
    resolve: (value: <span class="hljs-built_in">any</span> | PromiseLike<<span class="hljs-built_in">any</span>>) => <span class="hljs-built_in">void</span>,
    reject: (reason?: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">void</span>
  </span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 实际上是在这里调用了异步任务，并将异步任务的返回（resolve和reject）抛给了上层</span>
      caller()
        .then(resolve)
        .catch(reject)
        .finally(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-comment">// 任务队列的消费区，利用Promise的finally方法，在异步任务结束后，取出下一个任务执行</span>
          <span class="hljs-built_in">this</span>._count--;
          <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._taskQueue.length) &#123;
            <span class="hljs-keyword">const</span> task = <span class="hljs-built_in">this</span>._taskQueue.shift();
            task();
          &#125;
        &#125;);
      <span class="hljs-built_in">this</span>._count++;
    &#125;;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在另一个文件使用封装的LimitPromise 类封装post方法：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> LimitPromise <span class="hljs-keyword">from</span> <span class="hljs-string">'./limitReq'</span>;
<span class="hljs-keyword">import</span> axios, &#123; AxiosRequestConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;

<span class="hljs-keyword">const</span> limtReq = <span class="hljs-keyword">new</span> LimitPromise(<span class="hljs-number">6</span>);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> limitPost = <span class="hljs-function">(<span class="hljs-params">
  url: <span class="hljs-built_in">string</span>,
  data?: <span class="hljs-built_in">any</span>,
  config?: AxiosRequestConfig,
  resolve?: (value: <span class="hljs-built_in">any</span> | PromiseLike<<span class="hljs-built_in">any</span>>) => <span class="hljs-built_in">void</span>,
  reject?: (reason?: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">void</span>
</span>) =></span>
  limtReq
    .call(<span class="hljs-function">() =></span> axios.post(url, data, config))
    .then(resolve)
    .catch(reject);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来直接将原来的axios.post请求改为limitPost即可。</p></div>  
</div>
            