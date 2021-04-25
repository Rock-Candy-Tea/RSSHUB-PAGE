
---
title: 'JavaScript 中如何实现大文件并行下载？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/105d45a0431c4d9d86310758bf83ffcc~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 15:52:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/105d45a0431c4d9d86310758bf83ffcc~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在 <a href="https://mp.weixin.qq.com/s/yWOPoef9ixuSBWApZQhjIg" target="_blank" rel="nofollow noopener noreferrer">JavaScript 中如何实现并发控制？</a> 这篇文章中，阿宝哥详细分析了 <a href="https://github.com/rxaviers/async-pool" target="_blank" rel="nofollow noopener noreferrer">async-pool</a> 这个库如何利用 <code>Promise.all</code> 和 <code>Promise.race</code> 函数实现异步任务的并发控制。本文阿宝哥将介绍如何利用 <a href="https://github.com/rxaviers/async-pool" target="_blank" rel="nofollow noopener noreferrer">async-pool</a> 这个库提供的 <code>asyncPool </code> 函数来实现大文件的并行下载。</p>
<p>相信有些小伙伴已经了解大文件上传的解决方案，在上传大文件时，为了提高上传的效率，我们一般会使用 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Blob/slice" target="_blank" rel="nofollow noopener noreferrer">Blob.slice</a> 方法对大文件按照指定的大小进行切割，然后在开启多线程进行分块上传，等所有分块都成功上传后，再通知服务端进行分块合并。</p>
<p>那么对大文件下载来说，我们能否采用类似的思想呢？在服务端支持 <code>Range</code> 请求首部的条件下，我们也是可以实现多线程分块下载的功能，具体如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/105d45a0431c4d9d86310758bf83ffcc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>看完上图相信你对大文件下载的方案，已经有了一定的了解。接下来，我们先来介绍 HTTP 范围请求。</p>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 11 篇 Vue 3 进阶系列教程。</p>
</blockquote>
<h3 data-id="heading-0">一、HTTP 范围请求</h3>
<p>HTTP 协议范围请求允许服务器只发送 HTTP 消息的一部分到客户端。范围请求在传送大的媒体文件，或者与文件下载的断点续传功能搭配使用时非常有用。如果在响应中存在 <code>Accept-Ranges</code> 首部（并且它的值不为 “none”），那么表示该服务器支持范围请求。</p>
<p>在一个 Range 首部中，可以一次性请求多个部分，服务器会以 multipart 文件的形式将其返回。如果服务器返回的是范围响应，需要使用 <strong>206 Partial Content</strong> 状态码。假如所请求的范围不合法，那么服务器会返回  <strong>416 Range Not Satisfiable</strong> 状态码，表示客户端错误。服务器允许忽略  Range  首部，从而返回整个文件，状态码用 200 。</p>
<h4 data-id="heading-1">1.1 Range 语法</h4>
<pre><code class="copyable">Range: <unit>=<range-start>-
Range: <unit>=<range-start>-<range-end>
Range: <unit>=<range-start>-<range-end>, <range-start>-<range-end>
Range: <unit>=<range-start>-<range-end>, <range-start>-<range-end>, <range-start>-<range-end>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>unit</code>：范围请求所采用的单位，通常是字节（bytes）。</li>
<li><code><range-start></code>：一个整数，表示在特定单位下，范围的起始值。</li>
<li><code><range-end></code>：一个整数，表示在特定单位下，范围的结束值。<strong>这个值是可选的，如果不存在，表示此范围一直延伸到文档结束。</strong></li>
</ul>
<p>了解完 <code>Range</code> 语法之后，我们来看一下实际的使用示例：</p>
<h5 data-id="heading-2">1.1.1 单一范围</h5>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> curl http://i.imgur.com/z4d4kWk.jpg -i -H <span class="hljs-string">"Range: bytes=0-1023"</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">1.1.2 多重范围</h5>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> curl http://www.example.com -i -H <span class="hljs-string">"Range: bytes=0-50, 100-150"</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，HTTP 范围请求的相关知识就先介绍到这里，下面我们步入正题开始介绍如何实现大文件下载。</p>
<h3 data-id="heading-4">二、如何实现大文件下载</h3>
<p>为了让大家能够更好地理解后面的内容，我们先来看一下整体的流程图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0061dc3394644725a61a2414a3690c8b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>了解完大文件下载的流程之后，我们先来定义上述流程中涉及的一些辅助函数。</p>
<h4 data-id="heading-5">2.1 定义辅助函数</h4>
<h5 data-id="heading-6">2.1.1 定义 getContentLength 函数</h5>
<p>顾名思义 <code>getContentLength</code> 函数，用于获取文件的长度。在该函数中，我们通过发送 <code>HEAD</code> 请求，然后从响应头中读取 <code>Content-Length</code> 的信息，进而获取当前 <code>url</code> 对应文件的内容长度。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getContentLength</span>(<span class="hljs-params">url</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
    xhr.open(<span class="hljs-string">"HEAD"</span>, url);
    xhr.send();
    xhr.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      resolve(
        ~~xhr.getResponseHeader(<span class="hljs-string">"Content-Length"</span>) 
      );
    &#125;;
    xhr.onerror = reject;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">2.1.2 定义 asyncPool 函数</h5>
<p>在 <a href="https://mp.weixin.qq.com/s/yWOPoef9ixuSBWApZQhjIg" target="_blank" rel="nofollow noopener noreferrer">JavaScript 中如何实现并发控制？</a> 这篇文章中，我们介绍了 <code>asyncPool</code> 函数，它用于实现异步任务的并发控制。该函数接收 3 个参数：</p>
<ul>
<li><code>poolLimit</code>（数字类型）：表示限制的并发数；</li>
<li><code>array</code>（数组类型）：表示任务数组；</li>
<li><code>iteratorFn</code>（函数类型）：表示迭代函数，用于实现对每个任务项进行处理，该函数会返回一个 Promise 对象或异步函数。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncPool</span>(<span class="hljs-params">poolLimit, array, iteratorFn</span>) </span>&#123;
  <span class="hljs-keyword">const</span> ret = []; <span class="hljs-comment">// 存储所有的异步任务</span>
  <span class="hljs-keyword">const</span> executing = []; <span class="hljs-comment">// 存储正在执行的异步任务</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> array) &#123;
    <span class="hljs-comment">// 调用iteratorFn函数创建异步任务</span>
    <span class="hljs-keyword">const</span> p = <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> iteratorFn(item, array));
    ret.push(p); <span class="hljs-comment">// 保存新的异步任务</span>

    <span class="hljs-comment">// 当poolLimit值小于或等于总任务个数时，进行并发控制</span>
    <span class="hljs-keyword">if</span> (poolLimit <= array.length) &#123;
      <span class="hljs-comment">// 当任务完成后，从正在执行的任务数组中移除已完成的任务</span>
      <span class="hljs-keyword">const</span> e = p.then(<span class="hljs-function">() =></span> executing.splice(executing.indexOf(e), <span class="hljs-number">1</span>));
      executing.push(e); <span class="hljs-comment">// 保存正在执行的异步任务</span>
      <span class="hljs-keyword">if</span> (executing.length >= poolLimit) &#123;
        <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.race(executing); <span class="hljs-comment">// 等待较快的任务执行完成</span>
      &#125;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all(ret);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">2.1.3 定义 getBinaryContent 函数</h5>
<p><code>getBinaryContent</code> 函数用于根据传入的参数发起范围请求，从而下载指定范围内的文件数据块：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getBinaryContent</span>(<span class="hljs-params">url, start, end, i</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
      xhr.open(<span class="hljs-string">"GET"</span>, url, <span class="hljs-literal">true</span>);
      xhr.setRequestHeader(<span class="hljs-string">"range"</span>, <span class="hljs-string">`bytes=<span class="hljs-subst">$&#123;start&#125;</span>-<span class="hljs-subst">$&#123;end&#125;</span>`</span>); <span class="hljs-comment">// 请求头上设置范围请求信息</span>
      xhr.responseType = <span class="hljs-string">"arraybuffer"</span>; <span class="hljs-comment">// 设置返回的类型为arraybuffer</span>
      xhr.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        resolve(&#123;
          <span class="hljs-attr">index</span>: i, <span class="hljs-comment">// 文件块的索引</span>
          <span class="hljs-attr">buffer</span>: xhr.response, <span class="hljs-comment">// 范围请求对应的数据</span>
        &#125;);
      &#125;;
      xhr.send();
    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
      reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(err));
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是 <strong><code>ArrayBuffer</code></strong> 对象用来表示通用的、固定长度的原始二进制数据缓冲区。<strong>我们不能直接操作 <code>ArrayBuffer</code> 的内容，而是要通过类型数组对象或 DataView 对象来操作，它们会将缓冲区中的数据表示为特定的格式，并通过这些格式来读写缓冲区的内容</strong>。</p>
<h5 data-id="heading-9">2.1.4 定义 concatenate 函数</h5>
<p>由于不能直接操作 <strong><code>ArrayBuffer</code></strong> 对象，所以我们需要先把 <code>ArrayBuffer</code> 对象转换为 <code>Uint8Array</code> 对象，然后在执行合并操作。以下定义的 <code>concatenate</code> 函数就是为了合并已下载的文件数据块，具体代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">concatenate</span>(<span class="hljs-params">arrays</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!arrays.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
  <span class="hljs-keyword">let</span> totalLength = arrays.reduce(<span class="hljs-function">(<span class="hljs-params">acc, value</span>) =></span> acc + value.length, <span class="hljs-number">0</span>);
  <span class="hljs-keyword">let</span> result = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(totalLength);
  <span class="hljs-keyword">let</span> length = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> array <span class="hljs-keyword">of</span> arrays) &#123;
    result.set(array, length);
    length += array.length;
  &#125;
  <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">2.1.5 定义 saveAs 函数</h5>
<p><code>saveAs</code> 函数用于实现客户端文件保存的功能，这里只是一个简单的实现。在实际项目中，你可以考虑直接使用 <a href="https://github.com/eligrey/FileSaver.js" target="_blank" rel="nofollow noopener noreferrer">FileSaver.js </a>。如果你对  <a href="https://github.com/eligrey/FileSaver.js" target="_blank" rel="nofollow noopener noreferrer">FileSaver.js </a> 的工作原理感兴趣的话，可以阅读 <a href="https://mp.weixin.qq.com/s/oW0izYKgMC2eZdM459gmgQ" target="_blank" rel="nofollow noopener noreferrer">聊一聊 15.5K 的 FileSaver，是如何工作的？</a> 这篇文章。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">saveAs</span>(<span class="hljs-params">&#123; name, buffers, mime = <span class="hljs-string">"application/octet-stream"</span> &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> blob = <span class="hljs-keyword">new</span> Blob([buffers], &#123; <span class="hljs-attr">type</span>: mime &#125;);
  <span class="hljs-keyword">const</span> blobUrl = URL.createObjectURL(blob);
  <span class="hljs-keyword">const</span> a = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"a"</span>);
  a.download = name || <span class="hljs-built_in">Math</span>.random();
  a.href = blobUrl;
  a.click();
  URL.revokeObjectURL(blob);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>saveAs</code> 函数中，我们使用了 Blob 和 Object URL。其中 Object URL 是一种伪协议，允许 Blob 和 File 对象用作图像，下载二进制数据链接等的 URL 源。在浏览器中，我们使用 <code>URL.createObjectURL</code> 方法来创建 Object URL，该方法接收一个 <code>Blob</code> 对象，并为其创建一个唯一的 URL，其形式为 <code>blob:<origin>/<uuid></code>，对应的示例如下：</p>
<pre><code class="copyable">blob:https://example.org/40a5fb5a-d56d-4a33-b4e2-0acf6a8e5f641
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器内部为每个通过 <code>URL.createObjectURL</code> 生成的 URL 存储了一个 URL → Blob 映射。因此，此类 URL 较短，但可以访问 <code>Blob</code>。生成的 URL 仅在当前文档打开的状态下才有效。好了，Object URL 的相关内容就先介绍到这里，如果你进一步了解 Blob 和 Object URL 的话，可以阅读 <a href="https://mp.weixin.qq.com/s/lQKTCS_QB0E62SK9oXD4LA" target="_blank" rel="nofollow noopener noreferrer">你不知道的 Blob</a> 这篇文章。</p>
<h5 data-id="heading-11">2.1.6 定义 download 函数</h5>
<p><code>download</code> 函数用于实现下载操作，它支持 3 个参数：</p>
<ul>
<li><code>url</code>（字符串类型）：预下载资源的地址；</li>
<li><code>chunkSize</code>（数字类型）：分块的大小，单位为字节；</li>
<li><code>poolLimit</code>（数字类型）：表示限制的并发数。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">download</span>(<span class="hljs-params">&#123; url, chunkSize, poolLimit = <span class="hljs-number">1</span> &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> contentLength = <span class="hljs-keyword">await</span> getContentLength(url);
  <span class="hljs-keyword">const</span> chunks = <span class="hljs-keyword">typeof</span> chunkSize === <span class="hljs-string">"number"</span> ? <span class="hljs-built_in">Math</span>.ceil(contentLength / chunkSize) : <span class="hljs-number">1</span>;
  <span class="hljs-keyword">const</span> results = <span class="hljs-keyword">await</span> asyncPool(
    poolLimit,
    [...new <span class="hljs-built_in">Array</span>(chunks).keys()],
    <span class="hljs-function">(<span class="hljs-params">i</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> start = i * chunkSize;
      <span class="hljs-keyword">let</span> end = i + <span class="hljs-number">1</span> == chunks ? contentLength - <span class="hljs-number">1</span> : (i + <span class="hljs-number">1</span>) * chunkSize - <span class="hljs-number">1</span>;
      <span class="hljs-keyword">return</span> getBinaryContent(url, start, end, i);
    &#125;
  );
  <span class="hljs-keyword">const</span> sortedBuffers = results
    .map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(item.buffer));
  <span class="hljs-keyword">return</span> concatenate(sortedBuffers);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">2.2 大文件下载使用示例</h4>
<p>基于前面定义的辅助函数，我们就可以轻松地实现大文件并行下载，具体代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">multiThreadedDownload</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> url = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#fileUrl"</span>).value;
  <span class="hljs-keyword">if</span> (!url || !<span class="hljs-regexp">/https?/</span>.test(url)) <span class="hljs-keyword">return</span>;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"多线程下载开始: "</span> + +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>());
  download(&#123;
    url,
    <span class="hljs-attr">chunkSize</span>: <span class="hljs-number">0.1</span> * <span class="hljs-number">1024</span> * <span class="hljs-number">1024</span>,
    <span class="hljs-attr">poolLimit</span>: <span class="hljs-number">6</span>,
  &#125;).then(<span class="hljs-function">(<span class="hljs-params">buffers</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"多线程下载结束: "</span> + +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>());
    saveAs(&#123; buffers, <span class="hljs-attr">name</span>: <span class="hljs-string">"我的压缩包"</span>, <span class="hljs-attr">mime</span>: <span class="hljs-string">"application/zip"</span> &#125;);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于完整的示例代码内容比较多，阿宝哥就不放具体的代码了。感兴趣的小伙伴，可以访问以下地址浏览示例代码。</p>
<blockquote>
<p>完整的示例代码：<a href="https://gist.github.com/semlinker/837211c039e6311e1e7629e5ee5f0a42" target="_blank" rel="nofollow noopener noreferrer">gist.github.com/semlinker/8…</a></p>
</blockquote>
<p>这里我们来看一下大文件下载示例的运行结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ddb8be931e14feea5120399303b47c1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">三、总结</h3>
<p>本文介绍了在 JavaScript 中如何利用 <a href="https://github.com/rxaviers/async-pool" target="_blank" rel="nofollow noopener noreferrer">async-pool</a> 这个库提供的 <code>asyncPool </code> 函数，来实现大文件的并行下载。除了介绍 <code>asyncPool </code> 函数之外，阿宝哥还介绍了如何通过 HEAD 请求获取文件大小、如何发起 HTTP 范围请求及在客户端如何保存文件等相关知识。其实利用 <code>asyncPool </code> 函数不仅可以实现大文件的并行下载，而且还可以实现大文件的并行上传，感兴趣的小伙伴可以自行尝试一下。</p>
<blockquote>
<p>关注「全栈修仙之路」阅读阿宝哥原创的 4 本免费电子书（累计下载 3万+）及 11 篇 Vue 3 进阶系列教程。<strong>想一起学习 TS/Vue 3.0 的小伙伴可以添加阿宝哥微信 —— semlinker</strong>。</p>
</blockquote>
<h3 data-id="heading-14">四、参考资源</h3>
<ul>
<li><a href="https://mp.weixin.qq.com/s/lQKTCS_QB0E62SK9oXD4LA" target="_blank" rel="nofollow noopener noreferrer">你不知道的 Blob</a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer" target="_blank" rel="nofollow noopener noreferrer">MDN - ArrayBuffer</a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Range_requests" target="_blank" rel="nofollow noopener noreferrer">MDN - HTTP请求范围</a></li>
<li><a href="https://mp.weixin.qq.com/s/yWOPoef9ixuSBWApZQhjIg" target="_blank" rel="nofollow noopener noreferrer">JavaScript 中如何实现并发控制？</a></li>
</ul></div>  
</div>
            