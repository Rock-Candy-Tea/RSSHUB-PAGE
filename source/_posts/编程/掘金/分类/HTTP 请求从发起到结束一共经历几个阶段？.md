
---
title: 'HTTP 请求从发起到结束一共经历几个阶段？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d097bc7ee394243bed7a196a0e9ec14~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 05:31:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d097bc7ee394243bed7a196a0e9ec14~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：</strong> <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a> ​ <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a name="user-content-YruGG" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-0">序言</h2>
<p>这是浏览器专题的第三天，前面我们有讲《<a href="https://juejin.cn/post/6992231633373888543" target="_blank" title="https://juejin.cn/post/6992231633373888543">Chrome 中的多进程架构</a> 》 和 《 <a href="https://juejin.cn/post/6992602955396415496" target="_blank" title="https://juejin.cn/post/6992602955396415496">数据传输(IP/UDP/TCP)</a> 》，有了这些基础，我们今天来学习一下HTTP协议相关的知识。</p>
<p>HTTP 协议，建立在 TCP 连接基础之上的。HTTP 是一种允许浏览器向服务器获取资源的协议，是 Web 的基础，通常由浏览器发起请求，用来获取不同类型的文件，例如 HTML 文件、CSS 文件、JavaScript 文件、图片、视频等。此外，HTTP 也是浏览器使用最广的协议。 <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a name="user-content-AJHd6" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-1">HTTP请求发起流程</h2>
<p>当我们在浏览器上访问一个网址时，浏览器会向目标资源服务器发送资源请求，期间会经过一系列严谨的操作，保证请求的安全与稳定，接下来我们就一步步的详细了解。 <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a name="user-content-iI9Ob" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-2">1. 构建请求</h3>
<p>在发送请求前，需要构建<strong>请求行</strong>信息，该信息声明了<strong>请求方式</strong>，<strong>请求文件</strong>，和<strong>请求协议</strong>。构建完毕后，浏览器准备发起网络请求。</p>
<pre><code class="copyable">//请求行示例
GET /index.html HTTP1.1
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a name="user-content-vOjON" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-3">2. 查找缓存</h3>
<p>在发起网络之前，浏览器会根据请求行，查找<strong>浏览器缓存</strong>中是否存在该请求的缓存文件，如果有则从<strong>缓存中直接取</strong>，将资源返回，并且<strong>结束此次请求</strong>，这样做有以下好处：</p>
<ol>
<li>缓解服务器压力，提升性能。</li>
<li>对于网站来说，缓存是实现快速资源加载的重要部分。 <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a name="user-content-cra5R" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></li>
</ol>
<h3 data-id="heading-4">3. 准备IP地址和端口</h3>
<p>我们前面了解到，互联网数据传输是使用 TCP 和 IP 实现的，HTTP 则是作为应用层协议，用于封装请求的文本信息，也就是说<strong>HTTP的内容是通过TCP的传输数据阶段来实现的。</strong> 所以我们可以知道：</p>
<ol>
<li>HTTP网络请求的第一步是和服务器简历 TCP 连接。</li>
<li>建立 TCP 连接的第一步就需要准备 IP 地址和端口号。</li>
<li>我们通过 URL 地址可以获取 IP 和端口信息。</li>
<li>由于 IP 是一串数字非常难记，所以为了方便记忆有了 <strong>DNS ，</strong> 也就是域名，他和 IP 是一个映射关系，只需要输入 DNS 他会转换成对应的 IP 。</li>
</ol>
<p>小结:
所以浏览器请求第一步会请求 DNS 返回域名对应的 IP,当然浏览器还提供了 DNS 数据缓冲服务，如果如果某个域名已经解析过了，那么浏览器会缓存解析的结果，以供下次查询时直接使用，这样也会减少一次网络请求。拿到 IP 之后，接下来就需要获取端口号了。通常情况下，如果 URL 没有特别指明端口号，那么 HTTP 协议默认是 80 端口。 <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a name="user-content-E989K" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-5">4. 等待TCP队列</h3>
<p>由于 Chrome 的 TCP 连接机制（同一个域名同时最多只能建立6个TCP连接），所以当请求超过6个时，超出的请求会进入排队等待状态，直到进行中的请求完成。当然，如果当前请求数量少于 6，会直接进入下一步，建立 TCP 连接。 <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a name="user-content-Ffqzb" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-6">5. 建立 TCP 连接</h3>
<p>排队结束后，通过3次握手建立 TCP 连接。《 <a href="https://juejin.cn/post/6992602955396415496" target="_blank" title="https://juejin.cn/post/6992602955396415496">数据传输(IP/UDP/TCP)</a> 》该文章有详细介绍 TCP 的连接方式。 <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a name="user-content-fno0T" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-7">6. 发送 HTTP 请求</h3>
<p>一旦建立了 TCP 连接，浏览器就可以和服务器进行通信，而 HTTP 中的数据正是这个通信过程中传输的，我们看一个 HTTP 请求报文。 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d097bc7ee394243bed7a196a0e9ec14~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"> 首先浏览器会向服务器发送请求行，它包括了请求方法、请求 URI（Uniform Resource Identifier）和 HTTP 版本协议。 发送请求行，就是告诉服务器浏览器需要什么资源，最常用的请求方法是 Get。比如，直接在浏览器地址栏键入极客时间的域名（time.geekbang.org），这就是告诉服务器要 Get 它的首页资源。 另外一个常用的请求方法是 POST，它用于发送一些数据给服务器，比如登录一个网站，就需要通过 POST 方法把用户信息发送给服务器。如果使用 POST 方法，那么浏览器还要准备数据给服务器，这里准备的数据是通过请求体来发送。 在浏览器发送请求行命令之后，还要以请求头形式发送其他一些信息，把浏览器的一些基础信息告诉服务器。比如包含了浏览器所使用的操作系统、浏览器内核等信息，以及当前请求的域名信息、浏览器端的 Cookie 信息，等等。 <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a name="user-content-tK3T3" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-8">服务端处理 HTTP 请求流程</h2>
<p><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a name="user-content-OgJHY" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-9">1. 返回请求</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0789f7a6eda460b9f5b60eb6c40f335~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"> 首先服务器会返回响应行，包括协议版本和状态码。但并不是所有的请求都可以被服务器处理的，那么一些无法处理或者处理出错的信息，怎么办呢？服务器会通过请求行的状态码来告诉浏览器它的处理结。</p>
<ol>
<li>
<p>最常用的状态码是 200，表示处理成功，如果没有找到页面，则会返回 404。</p>
</li>
<li>
<p>随后，正如浏览器会随同请求发送请求头一样，服务器也会随同响应向浏览器发送响应头。响应头包含了服务器自身的一些信息，比如服务器生成返回数据的时间、返回的数据类型（JSON、HTML、流媒体等类型），以及服务器要在客户端保存的 Cookie 等信息。</p>
</li>
<li>
<p>发送完响应头后，服务器就可以继续发送响应体的数据，通常，响应体就包含了 HTML 的实际内容。 <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a name="user-content-LfZzB" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
</li>
</ol>
<h3 data-id="heading-10">2. 断开连接</h3>
<p>通常情况下，一旦服务器向客户端返回了请求数据，它就要关闭 TCP 连接。不过如果浏览器或者服务器在其头信息中加入了：</p>
<pre><code class="copyable">Connection:Keep-Alive 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么 TCP 连接在发送后将仍然保持打开状态，这样浏览器就可以继续通过同一个 TCP 连接发送请求。保持 TCP 连接可以省去下次请求时需要建立连接的时间，提升资源加载速度。比如，一个 Web 页面中内嵌的图片就都来自同一个 Web 站点，如果初始化了一个持久连接，你就可以复用该连接，以请求其他资源，而不需要重新再建立新的 TCP 连接。 <a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a name="user-content-ULAy5" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p></div>  
</div>
            