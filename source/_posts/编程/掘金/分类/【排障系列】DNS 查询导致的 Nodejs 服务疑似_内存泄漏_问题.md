
---
title: '【排障系列】DNS 查询导致的 Nodejs 服务疑似_内存泄漏_问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99d1c80bf52e42669b8979a573499b5f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 02 May 2021 03:08:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99d1c80bf52e42669b8979a573499b5f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1、OOM 报警：内存泄漏？</h2>
<p>某天下午，线上的服务监控发出报警：在同一个服务下，部署的众多容器中，某一个容器出现 OOM 问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99d1c80bf52e42669b8979a573499b5f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图是容器维度的资源使用率监控图。可以看到红色的内存使用率曲线，逐步升高将近到 100% 后又迅速降至 0%。这是因为触发 OOM 后容器自动重启。而在重启后，容器的的内存使用率仍在缓慢上升。</p>
<p>该容器分配的资源为 1 核 1G，其容器内只运行一个 Nodejs 进程。运行的 Nodejs 进程在某段时间的监控曲线如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c6c5174682a4a66aea8d050fa7216fd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，堆内存使用率也是逐步攀升，CPU 使用率则较为稳定。其与容器维度的监控表现一致。从容器与 Nodejs 进程的曲线上来看，非常像是 Nodejs 服务内存泄漏的问题。</p>
<h2 data-id="heading-1">2、使用堆内存快照，排查堆内存问题</h2>
<p>既然是内存问题，我很快想到要通过堆内存快照（Heap Snapshot）来排查。该服务使用了快手内部自研的 KNode 运行时来部署服务，因此可以在线上按需实时地打出堆快照，并在线查看：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d92675ff1e848e1bd6682690d70ff02~tplv-k3u1fbpfcp-watermark.image" alt="堆快照" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Heapsnaphost 中各项的含义以及如何查看，如果不了解可以看 <a href="https://developer.chrome.com/docs/devtools/memory-problems/memory-101/" target="_blank" rel="nofollow noopener noreferrer">Chrome Devtools 的说明文档</a>。</p>
</blockquote>
<p>不过可能是由于堆快照是一个切面数据，同时，打印这张快照时堆内存使用率也不是太高（大概为 20%），所以在初步看了堆快照后，问题线索不太直接。遇到这个问题，还有一个好办法，就是做两个时间点的快照 Diff。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5b98b438f7f421b8591ebc1cfdaf0e8~tplv-k3u1fbpfcp-watermark.image" alt="堆快照 Diff" loading="lazy" referrerpolicy="no-referrer"></p>
<p>v8 会给每个堆内存对象分配一个 ID。因此可以在 Heap 使用率较低和较高两个时间点，分别打印对应的堆快照，通过这个关联 ID，就可以对比出这段时间内新增和回收释放的堆内存对象。而 Chrome Devtools 本身也支持堆快照的 comparison 展示。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e0568b454684df8bef302856257ffb7~tplv-k3u1fbpfcp-watermark.image" alt="堆快照 Diff 结果展示" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图展示了在堆内存从 20% 涨到 50% 后新申请而没有被 GC 的对象（Object Allocated）。结合之前的堆快照（切面数据）和上面的 comparison 数据（Diff 数据），可以发现，红框中的这两类对象非常突出。也就是 <code>GetAddrInfoReqWrap</code> 与 <code>Socket</code>。</p>
<p><code>Socket</code> 和网络连接相关，属于比较广的范围。因为我将目光放在了 <code>GetAdrrInfoReqWrap</code> 上。基于之前对 Nodejs 的了解，我知道这是和 DNS 查询相关的 JS 层 wrapper 对象。当然，如果大家不知道这个对象，也可以通过<a href="https://github.com/nodejs/node/blob/v14.16.1/lib/dns.js#L141" target="_blank" rel="nofollow noopener noreferrer">查阅 Nodejs 源码</a>来了解到它的功能。展开堆快照中的对象，看下具体信息：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a05384fc910640f88f929520d7e961e2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从快照中对象的具体信息看，其 hostname 比较分散，所以感觉是和容器内整个 DNS 查询有关。</p>
<h2 data-id="heading-2">3、从其他 Nodejs 监控项，来看这个问题</h2>
<p>如果是 DNS 查询的问题，肯定也会间接影响到 HTTP 相关的监控项。而情况也确实如此。从 Nodejs 进程发起的 HTTP 请求的监控来看，有问题的容器，每分钟能完成的请求数只有 3 次（如下图）：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4803eb8b5de84c9b97871fc26739be4d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而同一个服务下的正常容器内，每个 Nodejs 进程每分钟可以正常发送超过 150 个 HTTP 请求（如下图）：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b78858af3062404f9ddb11da354d6968~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时，异常容器中的 Nodejs 发送完成一个 HTTP 请求的平均耗时超过了 800 秒（>13分钟）。而正常情况下内网服务之间的 HTTP 请求耗时一般都在几十毫秒，慢的也不太会超过几百毫秒。</p>
<p>此外，如果查看 Nodejs 的 Active Handle 的数量，也是处于一个持续上涨的状态。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cac8e6090fdb4556a0614ab92026e299~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里的 Active Handle 是指 <a href="http://docs.libuv.org/en/v1.x/design.html#handles-and-requests" target="_blank" rel="nofollow noopener noreferrer">libuv 中的 Handle</a>，与其类似的还有一个叫 Request 的概念。它是 libuv 中的抽象概念，用来指代 libuv 中某项操作的对象，例如定时器、设备 IO 等。Nodejs 进程中的 Active Handle 数量持续上涨往往是有问题的，它说明 Nodejs 要处理的东西“积压”地越来越多。</p>
<p>因此，基本怀疑就是 DNS 查询的问题导致请求积压，从而导致了该故障。</p>
<h2 data-id="heading-3">4、故障确定与修复</h2>
<p>通过上面的分析，基本可以确定和 DNS 查询脱不了干系。因为在服务部署的众多容器中，只有这一个有 OOM 问题，所以我分别登进一个健康容器和这个问题容器，执行以下 JS 代码来确认 DNS 查询情况（本文隐去了实际域名）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.time(<span class="hljs-string">'dns'</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">'dns'</span>).lookup(<span class="hljs-string">'xxx.xxxx.xxx'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'dns'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要提一下。Nodejs 封装了两类 DNS 查询的方法，一类就是上面用到的 <code>dns.lookup()</code>；另一个就是 <code>dns.resolve()</code> 和 <code>dns.resolve*()</code>。这里之所以在测试代码中使用 <code>dns.lookup()</code> 方法，是因为使用 Nodejs 中内置 http 模块的 <code>http.request()</code> 请求时，默认使用的就是该方法，而不是 <code>dns.resolve()</code>。</p>
<p>项目使用了 axios，而其在 <a href="https://github.com/axios/axios/blob/v0.21.1/lib/defaults.js#L18-L24" target="_blank" rel="nofollow noopener noreferrer">Nodejs 环境</a>下<a href="https://github.com/axios/axios/blob/v0.21.1/lib/adapters/http.js#L7" target="_blank" rel="nofollow noopener noreferrer">使用的是 <code>http.request()</code></a> 方法来发起 HTTP 请求。<code>http.request()</code> 会调用 net 模块中的 <a href="https://github.com/nodejs/node/blob/v14.16.1/lib/_http_client.js#L321" target="_blank" rel="nofollow noopener noreferrer"><code>createConnection</code> 方法</a>来建立连接。net 模块创建连接时，<a href="https://github.com/nodejs/node/blob/v14.16.1/lib/net.js#L1039" target="_blank" rel="nofollow noopener noreferrer">默认的 lookup 方法</a>就是 <code>dns.lookup()</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">lookupAndConnect</span>(<span class="hljs-params">self, options</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">const</span> lookup = options.lookup || dns.lookup;
  defaultTriggerAsyncIdScope(self[async_id_symbol], <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    lookup(host, dnsopts, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">emitLookup</span>(<span class="hljs-params">err, ip, addressType</span>) </span>&#123;
      self.emit(<span class="hljs-string">'lookup'</span>, err, ip, addressType, host);
      <span class="hljs-comment">// ...</span>
    &#125;);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，lookup 方法是<a href="https://nodejs.org/dist/latest-v14.x/docs/api/http.html#http_http_request_url_options_callback" target="_blank" rel="nofollow noopener noreferrer">可以设置</a>的，例如可以传入 <code>dns.resolve()</code> 或者自定义的方法。下图就是 Nodejs 官方文档中的说明截图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1a3c7cf1ebd41a4a62d3b1cd469a8df~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>回到该故障。测试代码运行后，正常容器（下图左）的 DNS 查询耗时为 33 毫秒；故障容器的耗时为 5000 毫秒，差异极大。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b0dcee98fbe4d98832cb124a037e028~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么是什么导致的耗时差异呢？</p>
<p><code>dns.lookup()</code> 方法会使用系统的 <a href="https://nodejs.org/dist/latest-v14.x/docs/api/dns.html#dns_dns_lookup_hostname_options_callback" target="_blank" rel="nofollow noopener noreferrer"><code>/etc/resolv.conf</code> 配置文件</a>。该文件中会设置 nameserver 的地址、超时时间、重试次数、rotate 策略等。通过对比正常容器和故障容器，发现了配置差异：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eaa3bed9fcaa48b98b2ad5b14542ea8f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>故障容器中（上图右）有个 nameserver 配置为了 <code>10.62.38.17</code>（正常容器是 <code>10.6.6.6</code>）。而 <code>10.62.38.17</code> 这个 nameserver 之前出现了问题，已经被替换掉了。但是在基础平台批量刷配置的操作中，故障容器所属的宿主机可能遗漏或者失败了。定位到具体原因后，联系了司内的容器化部署/运营平台的同学，修复该配置后后故障就解决了。</p>
<h2 data-id="heading-4">5、总结</h2>
<p>这个问题曲折的点在于：其监控表象初看像是内存泄漏，而一般来说内存泄漏都是代码 bug 导致的。但这个故障其实并非如此，实际是宿主机 DNS nameserver 的配置问题。</p>
<p>原因大致就是，由于 Nodejs 中 DNS 查询耗时过长导致了请求堆积，上游服务与 Nodejs 建立的连接也不会释放。所以在整个请求的生命周期中「持有」的对象未被释放，堆内存中对象不断增多，从而看起来像是「内存泄漏」。</p>
<hr>
<h2 data-id="heading-5">加餐：聊聊 Nodejs 中 DNS 查询与请求堆积</h2>
<p>上面还是只一个粗略的分析和定位。在这一节会尝试能更深入一些，将故障现象和 Nodejs 实现细节联系起来。</p>
<p>关于 Nodejs 中 DNS 查询故障导致的服务不响应的问题，之前已经有文章阐述了类似的问题：</p>
<blockquote>
<ul>
<li><a href="https://acemood.github.io/2020/05/02/node%E4%B8%AD%E8%AF%B7%E6%B1%82%E8%B6%85%E6%97%B6%E7%9A%84%E4%B8%80%E4%BA%9B%E5%9D%91/" target="_blank" rel="nofollow noopener noreferrer">node中请求超时的一些坑</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/138584520" target="_blank" rel="nofollow noopener noreferrer">NodeJS 中 DNS 查询的坑 & DNS cache 分析</a></li>
</ul>
</blockquote>
<p>下面再尝试简单解释一下。</p>
<p>使用 http 模块的 <code>http.request()</code> 方法默认会使用 <code>dns.lookup()</code> 作为 DNS 查询的方法（这个在上中文也已经提到了）。而 <code>dns.lookup()</code> 通过 binding 会调用到 <a href="https://github.com/nodejs/node/blob/v14.16.1/src/cares_wrap.cc#L1987-L1991" target="_blank" rel="nofollow noopener noreferrer"><code>GetAddrInfo()</code> 函数</a>：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">GetAddrInfo</span><span class="hljs-params">(<span class="hljs-keyword">const</span> FunctionCallbackInfo<Value>& args)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">int</span> err = req_wrap-><span class="hljs-built_in">Dispatch</span>(uv_getaddrinfo,
                               AfterGetAddrInfo,
                               *hostname,
                               <span class="hljs-literal">nullptr</span>,
                               &hints);
  <span class="hljs-keyword">if</span> (err == <span class="hljs-number">0</span>)
    <span class="hljs-comment">// Release ownership of the pointer allowing the ownership to be transferred</span>
    <span class="hljs-built_in">USE</span>(req_wrap.<span class="hljs-built_in">release</span>());

  args.<span class="hljs-built_in">GetReturnValue</span>().<span class="hljs-built_in">Set</span>(err);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中最重要的调用的就是 <code>uv_getaddrinfo()</code>，它会将 <a href="https://github.com/nodejs/node/blob/v14.16.1/deps/uv/src/unix/getaddrinfo.c#L209-L213" target="_blank" rel="nofollow noopener noreferrer"><code>uv__getaddrinfo_work</code> 提交到线程池的工作任务中</a>：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-built_in">uv__work_submit</span>(loop,
                &req->work_req,
                UV__WORK_SLOW_IO,
                uv__getaddrinfo_work,
                uv__getaddrinfo_done);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 <code>uv__getaddrinfo_work()</code> 中就会使用 <a href="https://github.com/nodejs/node/blob/v14.16.1/deps/uv/src/unix/getaddrinfo.c#L101-L108" target="_blank" rel="nofollow noopener noreferrer"><code>getaddrinfo</code> 函数</a>来做 DNS 查询：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">uv__getaddrinfo_work</span><span class="hljs-params">(struct uv__work* w)</span> </span>&#123;
  <span class="hljs-keyword">uv_getaddrinfo_t</span>* req;
  <span class="hljs-keyword">int</span> err;

  req = <span class="hljs-built_in">container_of</span>(w, <span class="hljs-keyword">uv_getaddrinfo_t</span>, work_req);
  err = <span class="hljs-built_in">getaddrinfo</span>(req->hostname, req->service, req->hints, &req->addrinfo);
  req->retcode = <span class="hljs-built_in">uv__getaddrinfo_translate_error</span>(err);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么为什么会涉及到线程池概念呢？因为调用 <code>getaddrinfo()</code> 函数是一个同步调用，所以 <a href="https://docs.libuv.org/en/latest/threadpool.html" target="_blank" rel="nofollow noopener noreferrer">libuv 会通过线程池</a>来实现 Nodejs 所需的异步 IO。线程池默认大小为 4，可以通过 <a href="https://github.com/nodejs/node/blob/v14.16.1/deps/uv/src/threadpool.c#L194" target="_blank" rel="nofollow noopener noreferrer"><code>UV_THREADPOOL_SIZE</code> 这个环境变量</a>来配置，在 Nodejs v14 中最大是 1024。</p>
<p>回到故障场景：</p>
<p>从正常进程的监控数据看到，每分钟 Nodejs 进程发起的请求大致为 150 个，也就是 1 秒 2.5 个。而在故障容器中，请求在 DNS 查询阶段就要耗时 5s。即使不考虑其他耗时也要 5s 才能发完一个请求。4 个线程平均下来，也就是 1 秒最多能处理 0.8 个请求。显然，2.5 要远大于 0.8，处理能力和请求数量严重不匹配。所以服务运行时间越长，积压的请求数、连接数就越多。</p>
<p>到这里，还有几个问题可以再说明下：</p>
<h3 data-id="heading-6">关于超时</h3>
<p>对于 HTTP 请求，我们一般会设置超时时间。但是 Nodejs 发起的请求可能不会触发到超时，由此使得上游服务到 Nodejs 的连接不会及时断开。这是在使用 axios 时可能出现的问题。</p>
<p>因为 axios 会基于 <a href="https://github.com/axios/axios/blob/v0.21.1/lib/adapters/http.js#L278" target="_blank" rel="nofollow noopener noreferrer"><code>requset.setTimeout</code></a> 来设置超时。之前的<a href="https://acemood.github.io/2020/05/02/node%E4%B8%AD%E8%AF%B7%E6%B1%82%E8%B6%85%E6%97%B6%E7%9A%84%E4%B8%80%E4%BA%9B%E5%9D%91/" target="_blank" rel="nofollow noopener noreferrer">文章</a>也分析过，它是不包含 DNS 查询时间的。从 <a href="https://nodejs.org/dist/latest-v14.x/docs/api/http.html#http_request_settimeout_timeout_callback" target="_blank" rel="nofollow noopener noreferrer">Nodejs 官网文档</a>中也能大致看出这个意思。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec69787ec0b3438d885809550036143a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">关于 DNS cache</h3>
<p>Nodejs 本身不做 DNS 查询结果的缓存（一些讨论也认为 cache 放在 userland 可能会合理些）。所以如果 <code>getaddrinfo()</code> 本身也没有 DNS cache（开启 nscd 似乎可以），Nodejs 就会在每次使用域名做 http 请求时，都会去请求 DNS nameserver。上文故障中的情况便是如此。</p>
<p>当然，你也可以通过使用类似像 <a href="https://www.npmjs.com/package/dnscache" target="_blank" rel="nofollow noopener noreferrer">dnscache</a> 这类包来做 monkey patch，在 JS 层为 DNS 查询添加缓存；或者通过在 axios 中添加拦截器，实现缓存。不过使用缓存一定要注意处理缓存过期的问题，可以使用 DNS server 返回的 TTL。不过有时这个值也不太可靠，可能会需要基于业务场景设置一个尽量小的值。总之使用缓存一定要谨慎！</p>
<h3 data-id="heading-8">关于 <code>dns.resolve()</code>/<code>dns.resolve*()</code></h3>
<p>从文章之前的章节可以知道，<code>dns.resolve()</code>/<code>dns.resolve*()</code> 与 <code>dns.lookup()</code> 的实现并不相同。它们是基于 <a href="https://github.com/c-ares/c-ares" target="_blank" rel="nofollow noopener noreferrer">c-ares</a> 实现的。</p>
<blockquote>
<p>This is c-ares, an asynchronous resolver library. It is intended for applications which need to perform DNS queries without blocking, or need to perform multiple DNS queries in parallel.</p>
</blockquote>
<p><code>http.request()</code> 是支持通过在 options 中传入 lookup 配置来覆盖默认的 <code>dns.lookup</code> 的。但是需要注意 <code>dns.resolve()</code> 和 <code>dns.lookup</code> 存在的<a href="https://nodejs.org/dist/latest-v14.x/docs/api/dns.html#dns_dns_resolve_dns_resolve_and_dns_reverse" target="_blank" rel="nofollow noopener noreferrer">可能区别</a>。</p>
<p>此外，它们只是不用再使用线程池，如果遇到像文中的故障，DNS 查询的耗时一样会很高，同样会有类似问题。</p>
<p>完。</p>
<blockquote>
<p>往期【排障系列】文章：</p>
<ul>
<li><a href="https://juejin.cn/post/6957344500310081544" target="_blank">npm script 执行”丢失“ root 权限的问题</a></li>
<li><a href="https://juejin.cn/post/6949823818097492005" target="_blank">记一次 Node gRPC 静态生成文件引发的问题</a></li>
</ul>
</blockquote></div>  
</div>
            