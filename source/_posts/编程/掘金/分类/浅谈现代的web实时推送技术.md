
---
title: '浅谈现代的web实时推送技术'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9740'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 07:59:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=9740'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 8 天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<hr>
<h3 data-id="heading-0">Server-Sent Event (SSE)</h3>
<p>SSE 客户端发送一个请求，建立连接后不会关闭连接。当有新数据时，服务端将消息推送到客户端。</p>
<h4 data-id="heading-1">特点</h4>
<ul>
<li>数据流式传输：SSE 发送一个类似音频流和视频流、下载文件的二进制流的数据流。</li>
<li>连接保持：与正常的 HTTP 请求一样。服务端连续不断的发送，客户端不会关闭连接</li>
<li>重连机制：如果连接断开，浏览器会尝试重新连接。</li>
<li>关闭连接：如果连接被关闭，客户端可以被告知使用 HTTP 204 无内容响应代码停止重新连接。</li>
</ul>
<h4 data-id="heading-2">优势</h4>
<p>SSE 不是新协议，已有的基础设施无需改造。用任何习惯的后端语言和框架都可以继续使用。</p>
<p>SSE 可以直接使用已有的验证和代理服务。</p>
<h4 data-id="heading-3">劣势</h4>
<p>只能单向接收数据。</p>
<h4 data-id="heading-4">兼容性</h4>
<p>IE 原生不支持，任何版本的 IE 都不支持。原因是 IE 的 XMLHttpRequest 对象不支持获取部分的响应内容。</p>
<p>但幸运的是，有一个 <a href="https://github.com/remy/polyfills/blob/master/EventSource.js" target="_blank" rel="nofollow noopener noreferrer">EventSource.js polyfill</a> 可以支持到 IE10。</p>
<p>如果完全不支持，请求接口时，将会回退到 GET 请求，只响应一次。</p>
<h4 data-id="heading-5">使用方法</h4>
<p>在客户端创建一个 EventSource 对象。对象指定接收事件的 URI。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> eventSource = <span class="hljs-keyword">new</span> EventSource(<span class="hljs-string">`myexample/sse`</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果创建对象的脚本和接口不同源，需要指定 options 对象，比如</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> eventSource = <span class="hljs-keyword">new</span> EventSource(<span class="hljs-string">"//otherorigin/sse"</span>, &#123; <span class="hljs-attr">withCredentials</span>: <span class="hljs-literal">true</span> &#125; );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 <code>EventSource</code> 初始化成功后，可以创建对应的监听函数接收服务端消息</p>
<pre><code class="hljs language-js copyable" lang="js">eventSource.onmessage = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(event.data);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了对全部信息的监听之外，你还可以监听指定事件类别的消息。事件类别在服务端推送数据时指定。</p>
<p>在客户端就可以</p>
<pre><code class="hljs language-js copyable" lang="js">evtSource.addEventListener(<span class="hljs-string">"ping"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(event.data) <span class="hljs-comment">//'ping' data</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你不想接收信息，可以关闭数据源：</p>
<pre><code class="hljs language-js copyable" lang="js">eventSource.close();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">参考文章</h4>
<p><a href="https://www.cnblogs.com/leftJS/p/11041410.html" target="_blank" rel="nofollow noopener noreferrer">SSE</a></p>
<h3 data-id="heading-7">WebSocket</h3>
<p>WebSocket 是一种全新的协议，它将 TCP 的 Socket（套接字）应用在了 webpage 上，从而使通信双方建立起一个保持在活动状态连接通道。</p>
<h4 data-id="heading-8">特点</h4>
<ul>
<li>需要<a href="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Protocol_upgrade_mechanism" target="_blank" rel="nofollow noopener noreferrer">升级到新协议</a>。协议升级是 HTTP 1.1 提供的内容。但如果你使用现有的库，升级问题不用担心</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> webSocket = <span class="hljs-keyword">new</span> WebSocket(<span class="hljs-string">"ws://destination.server.ext"</span>, <span class="hljs-string">"optionalProtocol"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>全双工。客户端和服务端可以互相传递消息，互相发布订阅消息。</li>
</ul>
<h4 data-id="heading-9">兼容性</h4>
<p>IE11 支持。毕竟是新协议，不受历史包袱影响，IE 也支持协议升级。</p>
<h4 data-id="heading-10">使用方法</h4>
<p>创建连接</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Create WebSocket connection</span>
<span class="hljs-comment">// 创建一个 WebSocket 连接</span>
<span class="hljs-keyword">const</span> socket = <span class="hljs-keyword">new</span> WebSocket(<span class="hljs-string">'ws://localhost:8080'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通道创建成功事件监听</p>
<pre><code class="hljs language-js copyable" lang="js">socket.onopen = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"WebSocket is open now."</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>错误监听</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Listen for possible errors</span>
<span class="hljs-comment">// 监听可能发生的错误</span>
socket.addEventListener(<span class="hljs-string">'error'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'WebSocket error: '</span>, event);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>消息发送</p>
<pre><code class="hljs language-js copyable" lang="js">socket.send(<span class="hljs-string">"Hello server!"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>消息监听</p>
<pre><code class="hljs language-js copyable" lang="js">socket.onmessage = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.debug(<span class="hljs-string">"WebSocket message received:"</span>, event);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            