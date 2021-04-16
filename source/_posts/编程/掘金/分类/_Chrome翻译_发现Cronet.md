
---
title: '_Chrome翻译_发现Cronet'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9806a9e293b34d03acf4a1ed6627ace3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 18:14:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9806a9e293b34d03acf4a1ed6627ace3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>原文地址：<a href="https://medium.com/@cchiappini/discover-cronet-4c7b4812407" target="_blank" rel="nofollow noopener noreferrer">medium.com/@cchiappini…</a></p>
<p>原文作者：<a href="https://medium.com/@cchiappini" target="_blank" rel="nofollow noopener noreferrer">medium.com/@cchiappini</a></p>
<p>发布时间：2016年8月22日-5分钟阅读</p>
</blockquote>
<p>Cronet是一个用于Android和iOS应用的网络库。Cronet是作为库打包的Chromium网络栈：这意味着Chrome浏览器每天都在使用这个栈。</p>
<p>采用Cronet可以通过降低延迟和增加吞吐量来提高应用的网络性能。</p>
<p>本文介绍了Cronet库及其使用方法。你可以在<a href="https://github.com/GoogleChrome/cronet-sample" target="_blank" rel="nofollow noopener noreferrer">这里</a>找到一个如何使用Cronet的例子。这个示例展示了如何使用Cronet加载一堆图片，存储在谷歌云上。</p>
<h1 data-id="heading-0">今天的网络</h1>
<p>看起来每个人都在使用OkHttp的一些变体。你可以通过Android框架，直接使用OkHttp，或者Volley（配置为使用框架或OkHttp）。</p>
<p>框架版本的API，HttpUrlConnection，提供了一个在单线程上运行的同步API。</p>
<p>OkHttp提供了异步API、流和HTTP/2。</p>
<p><a href="https://developer.android.com/training/volley/index.html" target="_blank" rel="nofollow noopener noreferrer">Volley</a>提供了请求优先级、多并发网络请求和请求取消。Volley在解析过程中会在内存中保留响应，所以对于小的HTTP请求来说，它的处理能力更强。</p>
<p>而Cronet API则允许异步请求。</p>
<h1 data-id="heading-1">Chromium网络栈</h1>
<p><a href="https://www.chromium.org/developers/design-documents/network-stack" target="_blank" rel="nofollow noopener noreferrer">Chromium网络协议栈</a>提供了几个优势来改善页面加载时间。</p>
<p>每次主机建立连接时，都要进行各种活动，比如DNS解析和握手。Chromium协议栈使用<a href="https://insouciant.org/tech/connection-management-in-chromium/" target="_blank" rel="nofollow noopener noreferrer">Socket Late Binding机制</a>来解决这个问题。</p>
<p>现代页面需要大量的资源，而<a href="https://insouciant.org/tech/resource-prioritization-in-chromium/" target="_blank" rel="nofollow noopener noreferrer">资源优先级</a>是浏览器的一个难题。Chromium协议栈使用了资源优先级，所有的请求都会以优先级标记发送给服务器，让服务器按照适当的优先级顺序进行响应。</p>
<p>Chromium还提供了一个<a href="https://www.chromium.org/developers/design-documents/network-stack/disk-cache" target="_blank" rel="nofollow noopener noreferrer">磁盘缓存</a>来缓存网络资源。</p>
<h1 data-id="heading-2">其他Cronet功能</h1>
<p>在读写数据时，Cronet使用<a href="https://blogs.oracle.com/slc/entry/javanio_vs_javaio" target="_blank" rel="nofollow noopener noreferrer">JAVA NIO ByteBuffers</a>，为I/O功能提供了更好的性能。</p>
<p>作为Chromium网络栈，Cronet也允许设置请求的优先级。参见优先级部分的代码示例。</p>
<h1 data-id="heading-3">支持HTTP/2和QUIC</h1>
<p>使用Cronet的优势之一是支持HTTP/2和QUIC。如果您熟悉这两个协议，可以随意跳过下面的章节，转到使用方法。</p>
<h1 data-id="heading-4">HTTP/2</h1>
<p>HTTP/2通过进化标准，解决了目前HTTP的许多弊端。相对于其前身，HTTP/2。</p>
<ul>
<li>是二进制的，而不是文本的</li>
<li>是完全多路复用的，而不是有序的和阻塞的：这允许使用一个连接做并行请求</li>
<li>使用头压缩来减少开销</li>
<li>允许服务器主动将响应 "推送 "到客户端缓存中。</li>
</ul>
<h1 data-id="heading-5">QUIC</h1>
<p><a href="https://www.chromium.org/quic" target="_blank" rel="nofollow noopener noreferrer">QUIC协议</a>(Quick UDP Internet Connections)是谷歌在2012年宣布的，旨在用UDP代替TCP取代HTTP/2。</p>
<p>QUIC允许以更低的延迟创建连接，是一个没有线头阻塞的多路复用协议。这意味着它解决了数据包丢失的问题，只阻断单个数据流，而不是所有的数据流。</p>
<p>桌面和 Android Chrome 浏览器上的所有主要 Google 网站以及许多 Android 应用程序都使用了 QUIC。</p>
<p>性能测试报告显示，网页加载时间快了5%，网页搜索速度快了1秒，达到99%。YouTube是使用QUIC的地方之一，它报告说，通过减少30%的重音（视频暂停）数量，提高了体验质量。</p>
<h1 data-id="heading-6">使用情况</h1>
<h2 data-id="heading-7">CronetEngine</h2>
<p>第一步是实例化一个CronetEngine，你可以在<a href="https://github.com/GoogleChrome/cronet-sample/blob/master/android/app/src/main/java/com/google/samples/cronet_sample/ViewAdapter.java" target="_blank" rel="nofollow noopener noreferrer">ViewAdapter.java</a>中找到。通常情况下，你只需要一个CronetEngine实例，所以在示例中，它是一个静态变量，由方法getCronetEngine(Context context)创建。</p>
<p>当创建CronetEngine时，通过CronetEngine.Builder，有各种配置选项。</p>
<ol>
<li>控制缓存（选一个）</li>
</ol>
<ul>
<li>通过使用100KB的内存缓存。</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java">engineBuilder.enableHttpCache(CronetEngine.Builder.HTTP_CACHE_IN_MEMORY, <span class="hljs-number">100</span> * <span class="hljs-number">1024</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者通过使用1MB的磁盘缓存。</p>
<pre><code class="hljs language-java copyable" lang="java">engineBuilder.setStoragePath(storagePathString);
engineBuilder.enableHttpCache(CronetEngine.Builder.HttpCache.DISK,
 <span class="hljs-number">1024</span> * <span class="hljs-number">1024</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用以下方法启用HTTP2</li>
</ol>
<pre><code class="hljs language-java copyable" lang="java"> engineBuilder.enableHttp2(<span class="hljs-keyword">true</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>使用以下方法启用QUIC</li>
</ol>
<pre><code class="hljs language-java copyable" lang="java">engineBuilder.enableQuic(<span class="hljs-keyword">true</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>如果你知道服务器正在使用QUIC，你可以通过使用</li>
</ol>
<pre><code class="copyable">engineBuilder.addQuicHint(...)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>事实上，在收到第一个响应之前，Cronet并不知道服务器说的是QUIC，一开始也不会尝试使用它。使用addQuicHint(...)方法，就不需要发现服务器是否支持QUIC。此外，通过使用</p>
<pre><code class="copyable">cronetBuilder.setStoragePath(...)
cronetBuilder.enableHttpCache(CronetEngine.Builder.HTTP_CACHE_DISK_NO_HTTP, 1024 * 1024)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些信息将在不同的会话中被持久化，并从第一次请求开始使用。使用磁盘缓存也会持久化服务器的加密信息，对于QUIC 0-rtt会话的建立，事实上0-rtt使用了之前协商好的会话中的QUIC服务器信息。</p>
<h2 data-id="heading-8">UrlRequest</h2>
<p>在Android上，Cronet提供了自己的Java异步API。从ViewAdapter类中可以看到，首先你需要扩展UrlRequest.Callback来处理请求生命周期内的事件。</p>
<p>你有4个不同的回调方法，一旦请求完全和部分完成，就会被执行者调用。</p>
<pre><code class="hljs language-java copyable" lang="java">onRedirectReceived(...)
onResponseStarted(...)
onReadCompleted(...)
onSucceeded(...)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一旦你实现了请求回调，你就可以通过使用UrlRequestBuilder进行请求，它将结合URL、回调、执行器和Cronet引擎。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// Create an executor to execute the request</span>
Executor executor = Executors.newSingleThreadExecutor();
UrlRequest.Callback callback = <span class="hljs-keyword">new</span> SimpleUrlRequestCallback(holder.imageViewCronet);
UrlRequest.Builder builder = <span class="hljs-keyword">new</span> UrlRequest
.Builder(ImageRepository.getImage(position), callback, executor, cronetEngine);
<span class="hljs-comment">// Start the request</span>
builder.build().start();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">优先级</h2>
<p>一个请求可以有5种类型的<a href="https://chromium.googlesource.com/chromium/src/+/lkgr/components/cronet/android/api/src/org/chromium/net/UrlRequest.java" target="_blank" rel="nofollow noopener noreferrer">优先级</a>。</p>
<ul>
<li>REQUEST_PRIORITY_IDLE.</li>
<li>REQUEST_PRIORITY_LOWEST(最低级)</li>
<li>REQUEST_PRIORITY_LOW(优先级低)</li>
<li>REQUEST_PRIORITY_MEDIUM(优先级)</li>
<li>REQUEST_PRIORITY_HIGHEST(最高优先级)</li>
</ul>
<p>你可以通过使用builder的setPriority方法来设置Request的优先级。</p>
<pre><code class="hljs language-java copyable" lang="java">builder.setPriority(UrlRequest.Builder.REQUEST_PRIORITY_HIGHEST);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">HTTPURLConnection</h2>
<p>如果你依赖于java.net.HttpURLConnection API，你可以通过使用Cronet实现。</p>
<pre><code class="hljs language-java copyable" lang="java">HttpURLConnection connection = (HttpURLConnection)engine.openConnection(url);
URL.setURLStreamHandlerFactory(engine.createURLStreamHandlerFactory());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请注意，Cronet的HttpURLConnection实现在系统实现方面有一些限制。例如，它没有使用系统默认的HTTP缓存。考虑到要将async非阻塞API转换为同步阻塞API，Async API的性能可能比HttpURLConnection更强。</p>
<h1 data-id="heading-11">调试</h1>
<p>您可以使用 NetLog 来获取更多有关 Cronet 如何处理网络请求的信息。
为了做到这一点，您需要通过调用 CronetEngine.startNetLogToFile 和 CronetEngine.stopNetLog 来检测代码以启动和停止 NetLog。请看一下<a href="https://github.com/GoogleChrome/cronet-sample" target="_blank" rel="nofollow noopener noreferrer">示例</a>中名为startNetLog()的方法，.NetLog()是一个很好的例子。</p>
<p>可以通过使用Chrome浏览器导航到chrome://net-internals#import 来读取日志文件。</p>
<p>这就是NetLog的样子。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9806a9e293b34d03acf4a1ed6627ace3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>请注意，开启NetLog跟踪会影响网络性能。</p>
<h1 data-id="heading-12">资料库</h1>
<p>正如<a href="https://github.com/GoogleChrome/cronet-sample/blob/master/README.md" target="_blank" rel="nofollow noopener noreferrer">README</a>文件上所描述的那样，今天获取最新版本的库是一个手动过程。
根据架构不同，库的大小在3-5MB之间。</p>
<h1 data-id="heading-13">结束语</h1>
<p>Cronet是一个开源库，可以在Android和IOS上进行HTTP、HTTP/2和QUIC调用。今天就在你的应用上试试，以提高你的应用网络性能。</p>
<h1 data-id="heading-14">来源</h1>
<p><a href="https://www.chromium.org/developers/design-documents/network-stack" target="_blank" rel="nofollow noopener noreferrer">www.chromium.org/developers/…</a></p>
<p><a href="https://www.chromium.org/developers/design-documents/network-stack/network-stack-use-in-chromium" target="_blank" rel="nofollow noopener noreferrer">www.chromium.org/developers/…</a></p>
<hr>
<p>通过www.DeepL.com/Translator（免费版）翻译</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            