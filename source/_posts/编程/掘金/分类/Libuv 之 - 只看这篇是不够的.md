
---
title: 'Libuv 之 - 只看这篇是不够的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbf2e15497e74b2c888df6b881ca8a28~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 30 Mar 2021 22:34:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbf2e15497e74b2c888df6b881ca8a28~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>图片来源：<a href="https://github.com/libuv/libuv" target="_blank" rel="nofollow noopener noreferrer">libuv</a></p>
</blockquote>
<blockquote>
<p>本文作者：<a href="https://github.com/hsiaosiyuan0" target="_blank" rel="nofollow noopener noreferrer">肖思元</a></p>
</blockquote>
<p>对 Node.js 的学习，无论如何都绕不开 Libuv。本文选择沿着 Libuv 的 Linux 实现的脉络对其内部一探究竟</p>
<h2 data-id="heading-0">为什么是 Linux</h2>
<blockquote>
<p>As an asynchronous event-driven JavaScript runtime, Node.js is designed to build <strong>scalable network applications</strong></p>
<p><a href="https://nodejs.org/en/about/#about-node-js" target="_blank" rel="nofollow noopener noreferrer">About Node.js</a></p>
</blockquote>
<p>Node.js 作为前端同学探索服务端业务的利器，自身是立志可以构建一个具有伸缩性的网络应用程序。目前的服务端环境主要还是 Linux，对于另一个主要的服务端环境 Unix，则在 API 上和 Linux 具有很高相似性，所以选择 Linux 作为起始点，说不定可以有双倍收获和双倍快乐</p>
<h2 data-id="heading-1">Libuv 与 Linux</h2>
<p>下面是 libuv 官网的架构图：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbf2e15497e74b2c888df6b881ca8a28~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>单以 Linux 平台来看，libuv 主要工作可以简单划为两部分：</p>
<ul>
<li>围绕 epoll，处理那些被 epoll 支持的 IO 操作</li>
<li>线程池（Thread pool），处理那些不被 epoll 支持的 IO 操作</li>
</ul>
<h2 data-id="heading-2">epoll 简介</h2>
<p>为了追本溯源，我们将从 epoll 开始</p>
<p>简单来说，epoll 是由 Linux 内核提供的一个系统调用（system call），我们的应用程序可以通过它：</p>
<ul>
<li>告诉系统帮助我们同时监控多个文件描述符</li>
<li>当这其中的一个或者多个文件描述符的 I/O 可操作状态改变时，我们的应用程序会接收到来自系统的事件提示（event notification）</li>
</ul>
<h3 data-id="heading-3">事件循环</h3>
<p>我们通过一小段伪代码来演示使用 epoll 时的核心步骤：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-comment">// 创建 epoll 实例</span>
<span class="hljs-keyword">int</span> epfd = epoll_create(MAX_EVENTS);
<span class="hljs-comment">// 向 epoll 实例中添加需要监听的文件描述符，这里是 `listen_sock`</span>
epoll_ctl_add(epfd, listen_sock, EPOLLIN | EPOLLOUT | EPOLLET);

<span class="hljs-keyword">while</span>(<span class="hljs-number">1</span>) &#123;
  <span class="hljs-comment">// 等待来自 epoll 的通知，通知会在其中的文件描述符状态改变时</span>
  <span class="hljs-comment">// 由系统通知应用。通知的形式如下：</span>
  <span class="hljs-comment">//</span>
  <span class="hljs-comment">// epoll_wait 调用不会立即返回，系统会在其中的文件描述符状态发生</span>
  <span class="hljs-comment">// 变化时返回</span>
  <span class="hljs-comment">//</span>
  <span class="hljs-comment">// epoll_wait 调用返回后：</span>
  <span class="hljs-comment">// nfds 表示发生变化的文件描述符数量</span>
  <span class="hljs-comment">// events 会保存当前的事件，它的数量就是 nfds</span>
  <span class="hljs-keyword">int</span> nfds = epoll_wait(epfd, events, MAX_EVENTS, <span class="hljs-number">-1</span>);

  <span class="hljs-comment">// 遍历 events，对事件作出符合应用预期的响应</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < nfds; i++) &#123;
    <span class="hljs-comment">// consume events[i]</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>完整例子见 <a href="https://github.com/going-merry0/epoll-echo-server" target="_blank" rel="nofollow noopener noreferrer">epoll-echo-server</a></p>
</blockquote>
<p>上面的代码中已经包含了注释，可以大致概括为下图：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5cccedcdb9c42359658fbb8e5c0c779~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>所以处于 libuv 底层的 epoll 也是有「事件循环」的概念，可见事件循环并不是 libuv 独创</p>
<p>提到 epoll，不得不提它的两种触发模式：水平触发（Level-triggered）、边缘触发（Edge-triggered）。不得不提是因为它们关系到 epoll 的事件触发机制，加上名字取得又有些晦涩</p>
<h3 data-id="heading-4">水平触发</h3>
<p>这两个术语都源自电子学领域，我们从它们的原始含义开始理解</p>
<p>首先是水平触发：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a06ee2e190c84bee87bc153313fa8b68~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p><a href="https://electricalbaba.com/edge-triggering-and-level-triggering/" target="_blank" rel="nofollow noopener noreferrer">Electrical Concepts</a></p>
</blockquote>
<p>上图是表示电压变化的时序图，VH 表示电压的峰值，VL 表示电话的谷值。水平触发的含义是，随着时间的变化，只要电压处于峰值，系统就会激活对应的电路（触发）</p>
<h3 data-id="heading-5">边缘触发</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9ab9b9d570a41a2afadb077fc9eee96~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p><a href="https://electricalbaba.com/edge-triggering-and-level-triggering/" target="_blank" rel="nofollow noopener noreferrer">Electrical Concepts</a></p>
</blockquote>
<p>上图依然是表示电压变化的时序图，不过激活电路（触发）的条件是电压的<strong>改变</strong>，即电压由 VH -> VL、VL -> VH 的状态变化，在图中通过<strong>边</strong>来表示这个变化，即 Rising edge 和 Falling edge，所以称为 Edge-triggered 即边缘触发</p>
<p>我们可以大致理解它们的形式与差别，继续结合下面的 epoll 中的表现进行理解</p>
<h3 data-id="heading-6">在 epoll 中</h3>
<p>回到 epoll 中，水平触发和边缘触发作为原始含义的衍生，当然还是具有类似电子学领域中的含义</p>
<p>我们通过一个例子来理解，比如我们有一个 fd（File descriptor） 表示刚建立的客户端连接，随后客户端给我们发送了 5 bytes 的内容，</p>
<p>如果是水平触发：</p>
<ul>
<li>我们的应用会被系统唤醒，因为 fd 此时状态变为了可读</li>
<li>我们从系统的缓冲区中读取 1 byte 的内容，并做了一些业务操作</li>
<li>进入到新的一次事件循环，等待系统下一次唤醒</li>
<li>系统继续唤醒我们的应用，因为缓冲区还有未读取的 4 bytes 内容</li>
</ul>
<p>如果是边缘触发：</p>
<ul>
<li>我们的应用会被系统唤醒，因为 fd 此时状态变为了可读</li>
<li>我们从系统的缓冲区中读取 1 byte 的内容，并做了一些业务操作</li>
<li>进入到新的一次事件循环，等待系统下一次唤醒</li>
<li>此时系统并不会唤醒我们的应用，直到下一次客户端发送了一些内容，比如发送了 2 bytes（因为直到下一次客户端发送了请求之前，fd 的状态并没有改变，所以在边缘触发下系统不会唤醒应用）</li>
<li>系统唤醒我们的应用，此时缓冲区有 6 bytes = (4 + 2) bytes</li>
</ul>
<p>我们很难将水平触发、边缘触发的字面意思与上面的行为联系起来，好在我们已经预先了解过它们在电子学领域的含义</p>
<p>水平触发，因为已经是可读状态，所以它会一直触发，直到我们读完缓冲区，且系统缓冲区没有新的客户端发送的内容；边缘触发对应的是<strong>状态的变化</strong>，每次有新的客户端发送内容，都会设置可读状态，因此只会在这个时机触发</p>
<p>水平触发是 epoll 默认的触发模式，并且 libuv 中使用的也是水平触发。在了解了水平触发和边缘触发的区别后，我们其实就可以猜测 libuv 使用水平触发而不是边缘触发背后的考量：</p>
<p>如果是边缘触发，在 epoll 的客观能力上，我们不被要求一次读取完缓冲区的内容（可以等到下一次客户端发送内容时继续读取）。但是实际业务中，客户端此时很可能在等待我们的响应（可以结合 HTTP 协议理解），而我们还在等待客户端的下一次写入，因此会陷入死锁的逻辑。由此一来，一次读取完缓冲区的内容几乎就成了边缘触发模式下的必选方式，这就不可避免的造成其他回调的等待时间变长，让 CPU 时间分配在各个回调之间显得不够均匀</p>
<h3 data-id="heading-7">局限性</h3>
<p>epoll 并不能够作用在所有的 IO 操作上，比如文件的读写操作，就无法享受到 epoll 的便利性</p>
<p>所以 libuv 的工作可以大致概括为：</p>
<ul>
<li>将各种操作系统上的类似 epoll 的系统调用（比如 Unix 上的 kqueue 和 Windows 上的 IOCP）抽象出统一的 API（内部 API）</li>
<li>对于可以利用系统调用的 IO 操作，优先使用统一后的 API</li>
<li>对于不支持或者支持度不够的 IO 操作，使用线程池（Thread pool）的方式模拟出异步 API</li>
<li>最后，将上面的细节封装在内部，对外提供统一的 API</li>
</ul>
<h2 data-id="heading-8">回到 libuv</h2>
<p>回到 libuv，我们将以 event-loop 为主要脉络，结合上文提到的 epoll，以及下面将会介绍到的线程池，继续 libuv 在 Linux 上的实现细节一探究竟</p>
<h3 data-id="heading-9">event-loop</h3>
<p>我们将结合源码来回顾一下 event-loop 基本概念</p>
<p>下面这幅图也取自 libuv 官网，它描述了 event-loop 内部的工作：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7fd6575cdc64bf88839cb8bd5502cfa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>引用自 <a href="http://docs.libuv.org/en/v1.x/design.html" target="_blank" rel="nofollow noopener noreferrer">libuv - Design overview</a></p>
</blockquote>
<p>单看流程图可能太抽象，下面是对应的 libuv 内部的实现 <a href="https://github.com/libuv/libuv/blob/v1.x/src/unix/core.c#L365" target="_blank" rel="nofollow noopener noreferrer">完整内容</a>：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_run</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, uv_run_mode mode)</span> </span>&#123;
  <span class="hljs-keyword">int</span> timeout;
  <span class="hljs-keyword">int</span> r;
  <span class="hljs-keyword">int</span> ran_pending;

  r = uv__loop_alive(loop);
  <span class="hljs-keyword">if</span> (!r) uv__update_time(loop);

  <span class="hljs-comment">// 是循环，没错了</span>
  <span class="hljs-keyword">while</span> (r != <span class="hljs-number">0</span> && loop->stop_flag == <span class="hljs-number">0</span>) &#123;
    uv__update_time(loop);
    <span class="hljs-comment">// 处理 timer 队列</span>
    uv__run_timers(loop);
    <span class="hljs-comment">// 处理 pending 队列</span>
    ran_pending = uv__run_pending(loop);
    <span class="hljs-comment">// 处理 idle 队列</span>
    uv__run_idle(loop);
    <span class="hljs-comment">// 处理 prepare 队列</span>
    uv__run_prepare(loop);

    <span class="hljs-comment">// 执行 io_poll</span>
    uv__io_poll(loop, timeout);
    uv__metrics_update_idle_time(loop);

    <span class="hljs-comment">// 执行 check 队列</span>
    uv__run_check(loop);
    <span class="hljs-comment">// 执行 closing 队列</span>
    uv__run_closing_handles(loop);

    r = uv__loop_alive(loop);
    <span class="hljs-keyword">if</span> (mode == UV_RUN_ONCE || mode == UV_RUN_NOWAIT) <span class="hljs-keyword">break</span>;
  &#125;

  <span class="hljs-keyword">return</span> r;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之所以各种形式的回调（比如 <code>setTimeout</code>）在优先级上会有差别，就在于它们使用的是不同的队列，而不同的队列在每次事件循环的迭代中的执行顺序不同</p>
<h3 data-id="heading-10">Handle 和 Request</h3>
<p>按照官网的描述，它们是对 event-loop 中执行的操作的抽象，前者表示需要长期存在的操作，后者表示短暂的操作。单看文字描述可能不太好理解，我们看一下它们的使用方式有何不同</p>
<p>对于 Handle 表示的长期存在的操作来说，它们的 API 具有类似下面的形式：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-comment">// IO 操作</span>
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_poll_init_socket</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, <span class="hljs-keyword">uv_poll_t</span>* handle, <span class="hljs-keyword">uv_os_sock_t</span> socket)</span></span>;
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_poll_start</span><span class="hljs-params">(<span class="hljs-keyword">uv_poll_t</span>* handle, <span class="hljs-keyword">int</span> events, uv_poll_cb cb)</span></span>;
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_poll_stop</span><span class="hljs-params">(<span class="hljs-keyword">uv_poll_t</span>* poll)</span></span>;

<span class="hljs-comment">// timer</span>
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_timer_init</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, <span class="hljs-keyword">uv_timer_t</span>* handle)</span></span>;
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_timer_start</span><span class="hljs-params">(<span class="hljs-keyword">uv_timer_t</span>* handle, uv_timer_cb cb, <span class="hljs-keyword">uint64_t</span> timeout, <span class="hljs-keyword">uint64_t</span> repeat)</span></span>;
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_timer_stop</span><span class="hljs-params">(<span class="hljs-keyword">uv_timer_t</span>* handle)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大致都有这三个步骤（并不是全部）：<code>初始化 -> 开始 -> 停止</code>。很好理解吧，因为是长期存在的操作，它开始了就会持续被处理，所以需要安排一个「停止」的 API</p>
<p>而对于 Request 表示的短暂操作来说，比如域名解析操作：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_getaddrinfo</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, <span class="hljs-keyword">uv_getaddrinfo_t</span>* req, uv_getaddrinfo_cb getaddrinfo_cb, <span class="hljs-comment">/* ... */</span>)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>域名解析操作的交互形式是，我们提交需要解析的地址，方法会返回解析的结果（这样的感觉似乎有点 HTTP 1.0 请求的样子），所以按「请求 - Request」来命名这样的操作的原因就变得有画面感了</p>
<p>不过 Handle 和 Request 两者不是互斥的概念，Handle 内部实现可能也用到了 Request。因为一些宏观来看的长期操作，在每个时间切片内是可以看成是 Request 的，比如我们处理一个请求，可以看成是一个 Handle，而在当次的请求中，我们很可能会做一些读取和写入的操作，这些操作就可以看成是 Request</p>
<h3 data-id="heading-11">timer</h3>
<p>我们通过 timer 开放出来的 API 为线索，来分析它的内部实现：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_timer_init</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, <span class="hljs-keyword">uv_timer_t</span>* handle)</span></span>;
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_timer_start</span><span class="hljs-params">(<span class="hljs-keyword">uv_timer_t</span>* handle, uv_timer_cb cb, <span class="hljs-keyword">uint64_t</span> timeout, <span class="hljs-keyword">uint64_t</span> repeat)</span></span>;
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_timer_stop</span><span class="hljs-params">(<span class="hljs-keyword">uv_timer_t</span>* handle)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>uv_timer_init</code> 没有什么特殊的地方，只是初始化一下 <code>handle</code> 的状态，并将其添加到 <code>loop->handle_queue</code> 中</p>
<p><code>uv_timer_start</code> 内部做了这些工作：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_timer_start</span><span class="hljs-params">(<span class="hljs-keyword">uv_timer_t</span>* handle,
                   uv_timer_cb cb,
                   <span class="hljs-keyword">uint64_t</span> timeout,
                   <span class="hljs-keyword">uint64_t</span> repeat)</span> </span>&#123;
  <span class="hljs-keyword">uint64_t</span> clamped_timeout;

  <span class="hljs-comment">// loop->time 表示 loop 当前的时间。loop 每次迭代开始时，会用当次时间更新该值</span>
  <span class="hljs-comment">// clamped_timeout 就是该 timer 未来超时的时间点，这里直接计算好，这样未来就不需要</span>
  <span class="hljs-comment">// 计算了，直接从 timers 中取符合条件的即可</span>
  <span class="hljs-keyword">if</span> (clamped_timeout < timeout)
    clamped_timeout = (<span class="hljs-keyword">uint64_t</span>) <span class="hljs-number">-1</span>;

  handle->timer_cb = cb;
  handle->timeout = clamped_timeout;
  handle->repeat = repeat;

  <span class="hljs-comment">// 除了预先计算好的 clamped_timeout 以外，未来当 clamped_timeout 相同时，使用这里的</span>
  <span class="hljs-comment">// 自增 start_id 作为比较条件来觉得 handle 的执行先后顺序</span>
  handle->start_id = handle->loop->timer_counter++;

  <span class="hljs-comment">// 将 handle 插入到 timer_heap 中，这里的 heap 是 binary min heap，所以根节点就是</span>
  <span class="hljs-comment">// clamped_timeout 值（或者 start_id）最小的 handle</span>
  heap_insert(timer_heap(handle->loop),
              (struct heap_node*) &handle->heap_node,
              timer_less_than);
  <span class="hljs-comment">// 设置 handle 的开始状态</span>
  uv__handle_start(handle);

  <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>uv_timer_stop</code> 内部做了这些工作：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_timer_stop</span><span class="hljs-params">(<span class="hljs-keyword">uv_timer_t</span>* handle)</span> </span>&#123;
  <span class="hljs-keyword">if</span> (!uv__is_active(handle))
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;

  <span class="hljs-comment">// 将 handle 移出 timer_heap，和 heap_insert 操作一样，除了移出之外</span>
  <span class="hljs-comment">// 还会维护 timer_heap 以保障其始终是 binary min heap</span>
  heap_remove(timer_heap(handle->loop),
              (struct heap_node*) &handle->heap_node,
              timer_less_than);
  <span class="hljs-comment">// 设置 handle 的状态为停止</span>
  uv__handle_stop(handle);

  <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到目前为止，我们已经知道所谓的 <code>start</code> 和 <code>stop</code> 其实可以粗略地概括为，往属性 <code>loop->timer_heap</code> 中插入或者移出 handle，并且这个属性使用一个名为 binary min heap 的数据结构</p>
<p>然后我们再回顾上文的 <code>uv_run</code>：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_run</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, uv_run_mode mode)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">while</span> (r != <span class="hljs-number">0</span> && loop->stop_flag == <span class="hljs-number">0</span>) &#123;
    <span class="hljs-comment">// ...</span>
    uv__update_time(loop);
    uv__run_timers(loop);
    <span class="hljs-comment">// ...</span>
  &#125;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>uv__update_time</code> 我们已经见过了，作用就是在循环开头阶段、使用当前时间设置属性 <code>loop->time</code></p>
<p>我们只需要最后看一下 <code>uv__run_timers</code> 的内容，就可以串联整个流程：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">uv__run_timers</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop)</span> </span>&#123;
  <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">heap_node</span>* <span class="hljs-title">heap_node</span>;</span>
  <span class="hljs-keyword">uv_timer_t</span>* handle;

  <span class="hljs-keyword">for</span> (;;) &#123;
    <span class="hljs-comment">// 取根节点，该值保证始终是所有待执行的 handle</span>
    <span class="hljs-comment">// 中，最先超时的那一个</span>
    heap_node = heap_min(timer_heap(loop));
    <span class="hljs-keyword">if</span> (heap_node == <span class="hljs-literal">NULL</span>)
      <span class="hljs-keyword">break</span>;

    handle = container_of(heap_node, <span class="hljs-keyword">uv_timer_t</span>, heap_node);
    <span class="hljs-keyword">if</span> (handle->timeout > loop->time)
      <span class="hljs-keyword">break</span>;

    <span class="hljs-comment">// 停止、移出 handle、顺便维护 timer_heap</span>
    uv_timer_stop(handle);
    <span class="hljs-comment">// 如果是需要 repeat 的 handle，则重新加入到 timer_heap 中</span>
    <span class="hljs-comment">// 会在下一次事件循环中、由本方法继续执行</span>
    uv_timer_again(handle);
    <span class="hljs-comment">// 执行超时 handle 其对应的回调</span>
    handle->timer_cb(handle);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上，就是 timer 在 Libuv 中的大致实现方式</p>
<h4 data-id="heading-12">min heap</h4>
<p>后面我们会看到，除了 timer 之外的 handle 都存放在名为 queue 的数据结构中，而存放 timer handle 的数据结构则为 min heap。那么我们就来看看这样的差别选择有何深意</p>
<p>所谓 min heap 其实是（如需更全面的介绍，可以参考 <a href="https://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/" target="_blank" rel="nofollow noopener noreferrer">Binary Tree</a>）：</p>
<ul>
<li>complete binary tree</li>
<li>根节点为真个 tree 中最小的节点</li>
</ul>
<p>先看 binary tree（二元树的定义是）：</p>
<ul>
<li>所有节点都只有最多两个子节点</li>
</ul>
<p>进一步看 complete binary tree 的定义则是：</p>
<ul>
<li>除了最后一层以外，其余层中的每个节点<strong>都有两个</strong>子节点</li>
<li>最后一层的摆布逻辑是，从左往右依次摆放（尽量填满左边）</li>
</ul>
<p>下面是几个例子：</p>
<pre><code class="copyable">complete binary tree 的例子：

               18
            /      \
         15         30
        /  \        /  \
      40    50    100   40
     /  \   /
    8   7  9

下面不是 complete binary tree，因为最后一层没有优先放满左边

               18
             /    \
          40       30
                   /  \
                 100   40

min heap 的例子，根节点是最小值、父节点始终小于其子节点：

               18
             /    \
           40       30
         /  \
      100   40
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 libuv 中对 timer handle 所需的操作是：</p>
<ul>
<li>添加和移除 timer handle</li>
<li>快速拿到 <code>clamped_timeout</code> 最小的 timer handle</li>
</ul>
<p>而 min heap 兼顾了上面的需求：</p>
<ul>
<li>相对数组而言，具有更高的插入和移除的效率</li>
<li>相对链表而言，具有更高的效率来维护极值（这里是最小值）</li>
</ul>
<p>heap 的实现在文件是 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/heap-inl.h" target="_blank" rel="nofollow noopener noreferrer">heap-inl.h</a>，我加入了一些注释，有兴趣的同学可以继续一探究竟</p>
<h3 data-id="heading-13">pending</h3>
<p>上面，我们已经了解了每次事件循环迭代中、处于第一顺位的 timer 的处理，接下来我们来看处在第二顺位的 pending 队列的处理：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">int</span> <span class="hljs-title">uv__run_pending</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop)</span> </span>&#123;
  QUEUE* q;
  QUEUE pq;
  <span class="hljs-keyword">uv__io_t</span>* w;

  <span class="hljs-keyword">if</span> (QUEUE_EMPTY(&loop->pending_queue))
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;

  QUEUE_MOVE(&loop->pending_queue, &pq);

  <span class="hljs-comment">// 不断从队列中弹出元素进行操作</span>
  <span class="hljs-keyword">while</span> (!QUEUE_EMPTY(&pq)) &#123;
    q = QUEUE_HEAD(&pq);
    QUEUE_REMOVE(q);
    QUEUE_INIT(q);
    w = QUEUE_DATA(q, <span class="hljs-keyword">uv__io_t</span>, pending_queue);
    w->cb(loop, w, POLLOUT);
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从源码来看，仅仅是从队列 <code>loop->pending_queue</code> 中不断弹出元素然后执行，并且弹出的元素是 <code>uv__io_t</code> 结构体的属性，从名字来看大致应该是 IO 相关的操作</p>
<p>另外，对 <code>loop->pending_queue</code> 进行插入操作的只有函数 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/unix/core.c#L951" target="_blank" rel="nofollow noopener noreferrer">uv__io_feed</a>，该函数的被调用点基本是执行一些 IO 相关的收尾工作</p>
<h4 data-id="heading-14">queue</h4>
<p>和上文出现的 min heap 一样，queue 也是主要用到的数据结构，所以我们在第一次见到它的时候、顺便介绍一下</p>
<p>min heap 的实现相对更深一些，所以提供了基于源码的注释 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/heap-inl.h" target="_blank" rel="nofollow noopener noreferrer">heap-inl.h</a> 让感兴趣的读者深入了解一下，而 queue 则相对就简单一些，加上源码中随处会出现操作 queue 的宏，了解这些宏到底做了什么、会让阅读源码时更加安心</p>
<p>接下来我们就一起看看 queue 和一些常用的操作它的宏，首先是起始状态：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a32814f95404a06af641aaeaa66c87e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>queue 在 libuv 中被设计成一个环形结构，所以起始状态就是 <code>next</code> 和 <code>prev</code> 都指向自身</p>
<p>接下来我们来看一下往 queue 插入一个新的元素是怎样的形式：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ee1dcd7e82d4f94a48e2939f5b490c4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上图分两部分，上半部分是已有的 queue、h 表示其当前的 head，q 是待插入的元素。下半部分是插入后的结果，图中的红色表示 <code>prev</code> 的通路，紫色表示 <code>next</code> 的通路，顺着通路我们可以发现它们始终是一个环形结构</p>
<p>上图演示的 <code>QUEUE_INSERT_TAIL</code> 顾名思义是插入到队尾，而因为是环形结构，我们需要修改头、尾、待插入元素三者的引用关系</p>
<p>再看一下移除某个元素的形式：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3b4b14d7ccd4abd9afa293cf0bd9402~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>移除某个元素就比较简单了，就是将该元素的 <code>prev</code> 和 <code>next</code> 连接起来即可，这样连接后，就跳过了该元素，使得该元素呈现出被移除的状态（无法在通路中访问到）</p>
<p>继续看下连接两个队列的操作：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee7d2a3a512649da8462406d53234be1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>看上去貌似很复杂，其实就是把两个环先解开，然后首尾相连成为一个新的环即可。这里通过意识流的作图方式，使用 <code>1</code> 和 <code>2</code> 标注了代码和连接动作的对应关系</p>
<p>最后看一下将队列一分为二的操作：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24eee287045f4f6590c7563906b5d31e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上图同样通过意识流的作图方式，使用 <code>1</code> 和 <code>2</code> 标注了代码和连接动作的对应关系；将原本以 <code>h</code> 开头的 queue，在 <code>q</code> 处剪开，<code>h</code> 和 <code>q</code> 之前的元素相连接成为一个新的 queue；<code>n</code> 作为另一个 queue 的开头，连接 <code>q</code> 和断开前的队列的末尾，构成另一个 queue</p>
<p>上面演示了一些具有有代表性的 queue 操作，感兴趣的同学可以继续查看 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/queue.h" target="_blank" rel="nofollow noopener noreferrer">queue.h</a> 来一探究竟</p>
<h3 data-id="heading-15">idle，check，prepare</h3>
<p>大家或许会奇怪，为什么没有按照它们在事件循环中的顺序进行介绍，而且还把它们三个放在了一起</p>
<p>如果大家在源码中搜索 <code>uv__run_idle</code> 或者 <code>uv__run_check</code> 会更加奇怪，因为我们只能找到它们的声明，甚至找不到它们的定义</p>
<p>其实它们都是在 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/unix/loop-watcher.c" target="_blank" rel="nofollow noopener noreferrer">loop-watcher.c</a> 中通过宏生成的，因为它们的操作都是一样的 - 从各自的队列中取出 handle 然后执行即可</p>
<p>需要说明的是，大家不要被 idle 的名字迷惑了，它并不是事件循环闲置的时候才会执行的队列，而是在每次时间循环迭代中，都会执行的，完全没有 idle 之意</p>
<p>不过要说完全没有 idle 之意似乎也不是特别合适，比如 idle 和 prepare 队列在内部实现上，无非是先后执行的队列而已：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_run</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, uv_run_mode mode)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">while</span> (r != <span class="hljs-number">0</span> && loop->stop_flag == <span class="hljs-number">0</span>) &#123;
    <span class="hljs-comment">// ...</span>
    uv__run_idle(loop);
    uv__run_prepare(loop);
    uv__io_poll(loop, timeout);
    <span class="hljs-comment">// ...</span>
  &#125;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么现在有一个 handle，我们希望它在 <code>uv__io_poll</code> 之前执行，是添加到 idle 还是 prepare 队列中呢？</p>
<p>我觉得 prepare 是取「为了下面的 <code>uv__io_poll</code> 做准备」之意，所以如果是为了 io_poll 做准备的 handle，那么可以添加到 prepare 队列中，其余则可以添加到 idle 之中。同样的设定我觉得也适用于 check，它运行在 io_poll 之后，可以让用户做一些检验 IO 执行结果的工作，让任务队列更加语义化</p>
<h3 data-id="heading-16">io poll</h3>
<p>对于 io_poll 我们还是从事件循环开始分析</p>
<h4 data-id="heading-17">从事件循环开始</h4>
<p>下面是上文已经介绍过的事件循环的片段：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_run</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, uv_run_mode mode)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">while</span> (r != <span class="hljs-number">0</span> && loop->stop_flag == <span class="hljs-number">0</span>) &#123;
    <span class="hljs-comment">// ...</span>
    timeout = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">if</span> ((mode == UV_RUN_ONCE && !ran_pending) || mode == UV_RUN_DEFAULT)
      timeout = uv_backend_timeout(loop);

    uv__io_poll(loop, timeout);
    <span class="hljs-comment">// ...</span>
  &#125;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码计算了一个 <code>timeout</code> 用于调用 <code>uv__io_poll(loop, timeout)</code></p>
<h4 data-id="heading-18">的确是 epoll</h4>
<p><code>uv__io_poll</code> 定义在 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/unix/linux-core.c#L191" target="_blank" rel="nofollow noopener noreferrer">linux-core.c</a> 中，虽然这是一个包含注释在内接近 300 行的函数，但想必大家也发现了，其中的核心逻辑就是开头演示的 epoll 的用法：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">uv__io_poll</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, <span class="hljs-keyword">int</span> timeout)</span> </span>&#123;
  <span class="hljs-keyword">while</span> (!QUEUE_EMPTY(&loop->watcher_queue)) &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-comment">// `loop->backend_fd` 是使用 `epoll_create` 创建的 epoll 实例</span>
    epoll_ctl(loop->backend_fd, op, w->fd, &e)
    <span class="hljs-comment">// ...</span>
  &#125;

  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">for</span> (;;) &#123;
  <span class="hljs-comment">// ...</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-comment">/* ... */</span>) &#123;
      <span class="hljs-comment">// ...</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// ...</span>
      <span class="hljs-comment">// `epoll_wait` 和 `epoll_pwait` 只有细微的差别，所以这里只考虑前者</span>
      nfds = epoll_wait(loop->backend_fd,
                        events,
                        ARRAY_SIZE(events),
                        timeout);
      <span class="hljs-comment">// ...</span>
    &#125;
  &#125;
  <span class="hljs-comment">// ...</span>

  <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < nfds; i++) &#123;
    <span class="hljs-comment">// ...</span>
    w = loop->watchers[fd];
    <span class="hljs-comment">// ...</span>
    w->cb(loop, w, pe->events);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">timeout</h4>
<p><code>epoll_wait</code> 的 <code>timeout</code> 参数的含义是：</p>
<ul>
<li>如果是 <code>-1</code> 表示一直等到有事件产生</li>
<li>如果是 <code>0</code> 则立即返回，包含调用时产生的事件</li>
<li>如果是其余整数，则以 <code>milliseconds</code> 为单位，规约到未来某个系统时间片内</li>
</ul>
<p>结合上面这些，我们看下 <code>uv_backend_timeout</code> 是如何计算 <code>timeout</code> 的：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_backend_timeout</span><span class="hljs-params">(<span class="hljs-keyword">const</span> <span class="hljs-keyword">uv_loop_t</span>* loop)</span> </span>&#123;
  <span class="hljs-comment">// 时间循环被外部停止了，所以让 `uv__io_poll` 理解返回</span>
  <span class="hljs-comment">// 以便尽快结束事件循环</span>
  <span class="hljs-keyword">if</span> (loop->stop_flag != <span class="hljs-number">0</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;

  <span class="hljs-comment">// 没有待处理的 handle 和 request，则也不需要等待了，同样让 `uv__io_poll`</span>
  <span class="hljs-comment">// 尽快返回</span>
  <span class="hljs-keyword">if</span> (!uv__has_active_handles(loop) && !uv__has_active_reqs(loop))
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;

  <span class="hljs-comment">// idle 队列不为空，也要求 `uv__io_poll` 尽快返回，这样尽快进入下一个时间循环</span>
  <span class="hljs-comment">// 否则会导致 idle 产生过高的延迟</span>
  <span class="hljs-keyword">if</span> (!QUEUE_EMPTY(&loop->idle_handles))
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;

  <span class="hljs-comment">// 和上一步目的一样，不过这里是换成了 pending 队列</span>
  <span class="hljs-keyword">if</span> (!QUEUE_EMPTY(&loop->pending_queue))
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;

  <span class="hljs-comment">// 和上一步目的一样，不过这里换成，待关闭的 handles，都是为了避免目标队列产生</span>
  <span class="hljs-comment">// 过高的延迟</span>
  <span class="hljs-keyword">if</span> (loop->closing_handles)
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;

  <span class="hljs-keyword">return</span> uv__next_timeout(loop);
&#125;

<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv__next_timeout</span><span class="hljs-params">(<span class="hljs-keyword">const</span> <span class="hljs-keyword">uv_loop_t</span>* loop)</span> </span>&#123;
  <span class="hljs-keyword">const</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">heap_node</span>* <span class="hljs-title">heap_node</span>;</span>
  <span class="hljs-keyword">const</span> <span class="hljs-keyword">uv_timer_t</span>* handle;
  <span class="hljs-keyword">uint64_t</span> diff;

  heap_node = heap_min(timer_heap(loop));
  <span class="hljs-comment">// 如果没有 timer 待处理，则可以放心的 block 住，等待事件到达</span>
  <span class="hljs-keyword">if</span> (heap_node == <span class="hljs-literal">NULL</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-number">-1</span>; <span class="hljs-comment">/* block indefinitely */</span>

  handle = container_of(heap_node, <span class="hljs-keyword">uv_timer_t</span>, heap_node);
  <span class="hljs-comment">// 有 timer，且 timer 已经到了要被执行的时间内，则需让 `uv__io_poll`</span>
  <span class="hljs-comment">// 尽快返回，以在下一个事件循环迭代内处理超时的 timer</span>
  <span class="hljs-keyword">if</span> (handle->timeout <= loop->time)
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;

  <span class="hljs-comment">// 没有 timer 超时，用最小超时间减去、当前的循环时间的差值，作为超时时间</span>
  <span class="hljs-comment">// 因为在为了这个差值时间内是没有 timer 超时的，所以可以放心 block 以等待</span>
  <span class="hljs-comment">// epoll 事件</span>
  diff = handle->timeout - loop->time;
  <span class="hljs-keyword">if</span> (diff > INT_MAX)
    diff = INT_MAX;

  <span class="hljs-keyword">return</span> (<span class="hljs-keyword">int</span>) diff;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的 <code>uv__next_timeout</code> 实现主要分为三部分：</p>
<ul>
<li>只有在没有 timer 待处理的时候，才会是 <code>-1</code>，结合本节开头对 <code>epoll_wait</code> 的 <code>timeout</code> 参数的解释，<code>-1</code> 会让后续的 <code>uv__io_poll</code> 进入 block 状态、完全等待事件的到达</li>
<li>当有 timer，且有超时的 timer <code>handle->timeout <= loop->time</code>，则返回 <code>0</code>，这样 <code>uv__io_poll</code> 不会 block 住事件循环，目的是为了快速进入下一次事件循环、以执行超时的 timer</li>
<li>当有 timer，不过都没有超时，则计算最小超时时间 <code>diff</code> 来作为 <code>uv__io_poll</code> 的阻塞时间</li>
</ul>
<p>不知道大家发现没有，timeout 的计算，其核心指导思想就是要尽可能的让 CPU 时间能够在事件循环的多次迭代的、多个不同任务队列的执行、中尽可能的分配均匀，避免某个类型的任务产生很高的延迟</p>
<h4 data-id="heading-20">小栗子</h4>
<p>了解了 io_poll 队列是如何执行之后，我们通过一个 echo server 的小栗子，来对 io_poll 有个整体的认识：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-keyword">uv_loop_t</span> *loop;

<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">echo_write</span><span class="hljs-params">(<span class="hljs-keyword">uv_write_t</span> *req, <span class="hljs-keyword">int</span> status)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 一些无所谓有，但有所谓无的收尾工作</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">echo_read</span><span class="hljs-params">(<span class="hljs-keyword">uv_stream_t</span> *client, <span class="hljs-keyword">ssize_t</span> nread, <span class="hljs-keyword">uv_buf_t</span> buf)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 创建一个写入请求（上文已经介绍过 Request 和 Handle 的区别），</span>
  <span class="hljs-comment">// 将读取的客户端内容写回给客户端，写入完成后进入回调 `echo_write`</span>
  <span class="hljs-keyword">uv_write_t</span> *write_req = (<span class="hljs-keyword">uv_write_t</span>*)<span class="hljs-built_in">malloc</span>(<span class="hljs-keyword">sizeof</span>(<span class="hljs-keyword">uv_write_t</span>));
  uv_write(write_req, client, &buf, <span class="hljs-number">1</span>, echo_write);
&#125;

<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">on_new_connection</span><span class="hljs-params">(<span class="hljs-keyword">uv_stream_t</span> *server, <span class="hljs-keyword">int</span> status)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 创建 client 实例并关联到事件循环</span>
  <span class="hljs-keyword">uv_tcp_t</span> *client = (<span class="hljs-keyword">uv_tcp_t</span>*) <span class="hljs-built_in">malloc</span>(<span class="hljs-keyword">sizeof</span>(<span class="hljs-keyword">uv_tcp_t</span>));
  uv_tcp_init(loop, client);
  <span class="hljs-comment">// 与建立客户端连接，并读取客户端输入，读取完成后进入 `echo_read` 回调</span>
  <span class="hljs-keyword">if</span> (uv_accept(server, (<span class="hljs-keyword">uv_stream_t</span>*) client) == <span class="hljs-number">0</span>) &#123;
    uv_read_start((<span class="hljs-keyword">uv_stream_t</span>*) client, alloc_buffer, echo_read);
  &#125;
  <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">()</span> </span>&#123;
  <span class="hljs-comment">// 创建事件循环</span>
  loop = uv_default_loop();

  <span class="hljs-comment">// 创建 server 实例并关联事件循环</span>
  <span class="hljs-keyword">uv_tcp_t</span> server;
  uv_tcp_init(loop, &server);
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 绑定 server 到某个端口，并接受请求</span>
  uv_tcp_bind(&server, uv_ip4_addr(<span class="hljs-string">"0.0.0.0"</span>, <span class="hljs-number">7000</span>));
  <span class="hljs-comment">// 新的客户端请求到达后，会进去到 `on_new_connection` 回调</span>
  uv_listen((<span class="hljs-keyword">uv_stream_t</span>*) &server, <span class="hljs-number">128</span>, on_new_connection);
  <span class="hljs-comment">// ...</span>

  <span class="hljs-comment">// 启动事件循环</span>
  <span class="hljs-keyword">return</span> uv_run(loop, UV_RUN_DEFAULT);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">Thead pool</h3>
<p>到目前为止，我们已经确认过 io_poll 内部实现确实是使用的 epoll。在本文的开头，我们也提到 epoll 目前并不能处理所有的 IO 操作，对于那些 epoll 不支持的 IO 操作，libuv 统一使用其内部的线程池来模拟出异步 IO。接下来我们看看线程池的大致工作形式</p>
<h4 data-id="heading-22">创建</h4>
<p>因为我们已经知道读写文件的操作是无法使用 epoll 的，那么就顺着这个线索，通过 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/unix/fs.c#L1891" target="_blank" rel="nofollow noopener noreferrer">uv_fs_read</a> 的内部实现，找到 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/threadpool.c#L256" target="_blank" rel="nofollow noopener noreferrer">uv__work_submit</a> 方法，发现是在其中初始化的线程池：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">uv__work_submit</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop,
                     struct uv__work* w,
                     <span class="hljs-keyword">enum</span> uv__work_kind kind,
                     <span class="hljs-keyword">void</span> (*work)(struct uv__work* w),
                     <span class="hljs-keyword">void</span> (*done)(struct uv__work* w, <span class="hljs-keyword">int</span> status))</span> </span>&#123;
  uv_once(&once, init_once);
  <span class="hljs-comment">// ...</span>
  post(&w->wq, kind);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以线程池的创建、是一个延迟创建的单例。<code>init_once</code> 内部会调用 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/threadpool.c#L188" target="_blank" rel="nofollow noopener noreferrer">init_threads</a> 来完成线程池初始化工作：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-keyword">static</span> <span class="hljs-keyword">uv_thread_t</span> default_threads[<span class="hljs-number">4</span>];

<span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">init_threads</span><span class="hljs-params">(<span class="hljs-keyword">void</span>)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  nthreads = ARRAY_SIZE(default_threads);
  val = getenv(<span class="hljs-string">"UV_THREADPOOL_SIZE"</span>);
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < nthreads; i++)
    <span class="hljs-keyword">if</span> (uv_thread_create(threads + i, worker, &sem))
      <span class="hljs-built_in">abort</span>();
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的实现，我们知道默认的线程池中线程的数量是 <code>4</code>，并且可以通过 <code>UV_THREADPOOL_SIZE</code> 环境变量重新指定该数值</p>
<p>除了对线程池进行单例延迟创建，<code>uv__work_submit</code> 当然还是会提交任务的，这部分工作是由 <code>post(&w->wq, kind)</code> 完成的，我们来看下 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/threadpool.c#L142:13" target="_blank" rel="nofollow noopener noreferrer">post</a> 方法的实现细节：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">post</span><span class="hljs-params">(QUEUE* q, <span class="hljs-keyword">enum</span> uv__work_kind kind)</span> </span>&#123;
  uv_mutex_lock(&mutex);
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 将任务插入到 `wq` 这个线程共享的队列中</span>
  QUEUE_INSERT_TAIL(&wq, q);
  <span class="hljs-comment">// 如果有空闲线程，则通知它们开始工作</span>
  <span class="hljs-keyword">if</span> (idle_threads > <span class="hljs-number">0</span>)
    uv_cond_signal(&cond);
  uv_mutex_unlock(&mutex);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以发现对于提交任务，其实就是将任务插入到线程共享队列 <code>wq</code>，并且有空闲线程时才会通知它们工作。那么，如果此时没有空闲线程的话，是不是任务就被忽略了呢？答案是否，因为工作线程会在完成当前工作后，主动检查 <code>wq</code> 队列是否还有待完成的工作，有的话会继续完成，没有的话，则进入睡眠，等待下次被唤醒（后面会继续介绍这部分细节）</p>
<h4 data-id="heading-23">任务如何调度</h4>
<p>上面在创建线程的时候 <code>uv_thread_create(threads + i, worker, &sem)</code> 中的 <code>worker</code> 就是线程执行的内容，我们来看下 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/threadpool.c#L57" target="_blank" rel="nofollow noopener noreferrer">worker</a> 的大致内容：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-comment">// 线程池的 wq，提交的任务都先链到其中</span>
<span class="hljs-keyword">static</span> QUEUE wq;

<span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">worker</span><span class="hljs-params">(<span class="hljs-keyword">void</span>* arg)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// `idle_threads` 和 `run_slow_work_message` 这些是线程共享的，所以要加个锁</span>
  uv_mutex_lock(&mutex);
  <span class="hljs-keyword">for</span> (;;) &#123;
    <span class="hljs-comment">// 这里的条件判断，可以大致看成是「没有任务」为 true</span>
    <span class="hljs-keyword">while</span> (QUEUE_EMPTY(&wq) ||
           (QUEUE_HEAD(&wq) == &run_slow_work_message &&
            QUEUE_NEXT(&run_slow_work_message) == &wq &&
            slow_io_work_running >= slow_work_thread_threshold())) &#123;
      <span class="hljs-comment">// 轮转到当前进程时因为没有任务，则无事可做</span>
      <span class="hljs-comment">// 空闲线程数 +1</span>
      idle_threads += <span class="hljs-number">1</span>;
      
      <span class="hljs-comment">// `uv_cond_wait` 内部是使用 `pthread_cond_wait` 调用后会：</span>
      <span class="hljs-comment">// - 让线程进入等待状态，等待条件变量 `cond` 发生变更</span>
      <span class="hljs-comment">// - 对 `mutex` 解锁</span>
      <span class="hljs-comment">//</span>
      <span class="hljs-comment">// 此后，其他线程中均可使用 `uv_cond_signal` 内部是 `pthread_cond_signal` </span>
      <span class="hljs-comment">// 来广播一个条件变量 `cond` 变更的事件，操作系统内部会随机唤醒一个等待 `cond` </span>
      <span class="hljs-comment">// 变更的线程，并在被唤醒线程的 uv_cond_wait 调用返回之前，对之前传入的 `mutex` </span>
      <span class="hljs-comment">// 参数上锁</span>
      <span class="hljs-comment">//</span>
      <span class="hljs-comment">// 因此循环跳出（有任务）后，`mutex` 一定是上锁的</span>
      uv_cond_wait(&cond, &mutex);
      idle_threads -= <span class="hljs-number">1</span>;
    &#125;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-comment">// 因为上锁了，所以放心进行队列的弹出操作</span>
    q = QUEUE_HEAD(&wq);
    QUEUE_REMOVE(q);
    <span class="hljs-comment">// ...</span>
    <span class="hljs-comment">// 因为已经完成了弹出，可以解锁，让其他线程可以继续操作队列</span>
    uv_mutex_unlock(&mutex);

    <span class="hljs-comment">// 利用 c 结构体的小特性，做字段偏移，拿到 `q` 所属的 `uv__work` 实例</span>
    w = QUEUE_DATA(q, struct uv__work, wq);
    w->work(w);

    <span class="hljs-comment">// 下面要操作 `w->loop->wq` 所以要上锁</span>
    uv_mutex_lock(&w->loop->wq_mutex);
    w->work = <span class="hljs-literal">NULL</span>; 

    <span class="hljs-comment">// 需要看仔细，和开头部分线程池中的 wq 区别开</span>
    QUEUE_INSERT_TAIL(&w->loop->wq, &w->wq);

    <span class="hljs-comment">// 唤醒主线程的事件循环</span>
    uv_async_send(&w->loop->wq_async);
    uv_mutex_unlock(&w->loop->wq_mutex);

    <span class="hljs-comment">// 这一步上锁是必须的，因为下次迭代的开头又需要</span>
    <span class="hljs-comment">// 操作共享内存，不过不必担心死锁，因为它和下一次迭代</span>
    <span class="hljs-comment">// 中的 `uv_cond_wait` 解锁操作是对应的</span>
    uv_mutex_lock(&mutex);
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们保留了相对重要的内容，并加以注释。可以大致地概括为：</p>
<ul>
<li>对于线程池中的线程，会通过 <code>uv_cond_wait</code> 来等待被唤醒</li>
<li>线程被唤醒后就从 <code>wq</code> 中主动找一个任务做，完成任务就唤醒主线程，因为回调需要在主线程被执行</li>
<li>随后就进入下一次迭代，如果有任务，就继续完成，直至没有任务时，通过 <code>uv_cond_wait</code> 再次进入睡眠状态</li>
<li>唤醒是通过在另外的线程中使用 <code>uv_cond_signal</code> 来通知操作系统做调度</li>
<li>线程池是一个可伸缩的设计，当一个任务都没有时，线程会都进入睡眠状态，当任务逐渐增多时，会由活动的线程尝试唤醒睡眠中的线程</li>
</ul>
<h4 data-id="heading-24">唤醒主线程</h4>
<p>当线程池完成任务后，需要通知主线程执行对应的回调。通知的方式很有意思，我们先来看下事件循环初始化操作 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/unix/loop.c#L30" target="_blank" rel="nofollow noopener noreferrer">uv_loop_init</a>：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_loop_init</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 初始化 min heap 和各种队列，用于存放各式的 handles</span>
  heap_init((struct heap*) &loop->timer_heap);
  QUEUE_INIT(&loop->wq);
  QUEUE_INIT(&loop->idle_handles);
  QUEUE_INIT(&loop->async_handles);
  QUEUE_INIT(&loop->check_handles);
  QUEUE_INIT(&loop->prepare_handles);
  QUEUE_INIT(&loop->handle_queue);

  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 调用 `epoll_create` 创建 epoll 实例</span>
  err = uv__platform_loop_init(loop);
  <span class="hljs-keyword">if</span> (err)
    <span class="hljs-keyword">goto</span> fail_platform_init;

  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 用于线程池通知的初始化</span>
  err = uv_async_init(loop, &loop->wq_async, uv__work_done);
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码中 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/unix/async.c#L45" target="_blank" rel="nofollow noopener noreferrer">uv_async_init</a> 是用于初始化线程池通知相关的工作，下面是它的函数签名：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_async_init</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, <span class="hljs-keyword">uv_async_t</span>* handle, uv_async_cb async_cb)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以第三个实参 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/threadpool.c#L295" target="_blank" rel="nofollow noopener noreferrer">uv__work_done</a> 其实是一个回调函数，我们可以看下它的内容：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">uv__work_done</span><span class="hljs-params">(<span class="hljs-keyword">uv_async_t</span>* handle)</span> </span>&#123;
  <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">uv__work</span>* <span class="hljs-title">w</span>;</span>
  <span class="hljs-keyword">uv_loop_t</span>* loop;
  QUEUE* q;
  QUEUE wq;
  <span class="hljs-keyword">int</span> err;

  loop = container_of(handle, <span class="hljs-keyword">uv_loop_t</span>, wq_async);
  uv_mutex_lock(&loop->wq_mutex);
  <span class="hljs-comment">// 将目前的 `loop->wq` 全部移动到局部变量 `wq` 中，</span>
  <span class="hljs-comment">//</span>
  <span class="hljs-comment">// `loop->wq` 中的内容是在上文 worker 中任务完成后使用</span>
  <span class="hljs-comment">// `QUEUE_INSERT_TAIL(&w->loop->wq, &w->wq)` 添加的</span>
  <span class="hljs-comment">//</span>
  <span class="hljs-comment">// 这样尽快释放锁，让其他任务可尽快接入</span>
  QUEUE_MOVE(&loop->wq, &wq);
  uv_mutex_unlock(&loop->wq_mutex);

  <span class="hljs-comment">// 遍历 `wq` 执行其中每个任务的完成回调</span>
  <span class="hljs-keyword">while</span> (!QUEUE_EMPTY(&wq)) &#123;
    q = QUEUE_HEAD(&wq);
    QUEUE_REMOVE(q);

    w = container_of(q, struct uv__work, wq);
    err = (w->work == uv__cancelled) ? UV_ECANCELED : <span class="hljs-number">0</span>;
    w->done(w, err);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>知道了 <code>uv__work_done</code> 就是负责执行任务完成回调的工作后，继续看一下 <code>uv_async_init</code> 的内容，看看其内部是如何使用 <code>uv__work_done</code> 的：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">uv_async_init</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, <span class="hljs-keyword">uv_async_t</span>* handle, uv_async_cb async_cb)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 待调查</span>
  err = uv__async_start(loop);
  <span class="hljs-comment">// ...</span>

  <span class="hljs-comment">// 创建了一个 async handle</span>
  uv__handle_init(loop, (<span class="hljs-keyword">uv_handle_t</span>*)handle, UV_ASYNC);
  <span class="hljs-comment">// 在目前的脉络中 `async_cb` 就是 `uv__work_done` 了</span>
  handle->async_cb = async_cb;
  handle->pending = <span class="hljs-number">0</span>;

  <span class="hljs-comment">// 把 async handle 加入到队列 `loop->async_handles` 中</span>
  QUEUE_INSERT_TAIL(&loop->async_handles, &handle-><span class="hljs-built_in">queue</span>);
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们继续看一下之前待调查的 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/unix/async.c#L202" target="_blank" rel="nofollow noopener noreferrer">uv__async_start</a> 的内容：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">int</span> <span class="hljs-title">uv__async_start</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// `eventfd` 可以创建一个 epoll 内部维护的 fd，该 fd 可以和其他真实的 fd（比如 socket fd）一样</span>
  <span class="hljs-comment">// 添加到 epoll 实例中，可以监听它的可读事件，也可以对其进行写入操作，因此就用户代码就可以借助这个</span>
  <span class="hljs-comment">// 看似虚拟的 fd 来实现的事件订阅了</span>
  err = eventfd(<span class="hljs-number">0</span>, EFD_CLOEXEC | EFD_NONBLOCK);
  <span class="hljs-keyword">if</span> (err < <span class="hljs-number">0</span>)
    <span class="hljs-keyword">return</span> UV__ERR(errno);

  pipefd[<span class="hljs-number">0</span>] = err;
  pipefd[<span class="hljs-number">1</span>] = <span class="hljs-number">-1</span>;
  <span class="hljs-comment">// ...</span>

  uv__io_init(&loop->async_io_watcher, uv__async_io, pipefd[<span class="hljs-number">0</span>]);
  uv__io_start(loop, &loop->async_io_watcher, POLLIN);
  loop->async_wfd = pipefd[<span class="hljs-number">1</span>];

  <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们知道 epoll 是支持 socket fd 的，对于支持的 fd，epoll 的事件调度将非常的高效。而对于不支持的 IO 操作，libuv 则使用 <code>eventfd</code> 创建一个虚拟的 fd，继续利用 fd 的事件调度功能</p>
<p>我们继续看下上面出现的 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/unix/core.c#L882" target="_blank" rel="nofollow noopener noreferrer">uv__io_start</a> 的细节，来确认一下事件订阅的步骤：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">uv__io_start</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, <span class="hljs-keyword">uv__io_t</span>* w, <span class="hljs-keyword">unsigned</span> <span class="hljs-keyword">int</span> events)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>

  <span class="hljs-comment">// 大家可以翻到上面 `uv__io_poll` 的部分，会发现其中有遍历 `loop->watcher_queue`</span>
  <span class="hljs-comment">// 将其中的 fd 都加入到 epoll 实例中，以订阅它们的事件的动作</span>
  <span class="hljs-keyword">if</span> (QUEUE_EMPTY(&w->watcher_queue))
    QUEUE_INSERT_TAIL(&loop->watcher_queue, &w->watcher_queue);

  <span class="hljs-comment">// 将 fd 和对应的任务关联的操作，同样可以翻看上面的 `uv__io_poll`，当接收到事件</span>
  <span class="hljs-comment">// 通知后，会有从 `loop->watchers` 中根据 fd 取出任务并执行其完成回调的动作</span>
  <span class="hljs-comment">// 另外，根据 fd 确保 watcher 不会被重复添加</span>
  <span class="hljs-keyword">if</span> (loop->watchers[w->fd] == <span class="hljs-literal">NULL</span>) &#123;
    loop->watchers[w->fd] = w;
    loop->nfds++;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>确认了事件订阅步骤以后，我们来看下事件回调的内容。上面的形参 <code>w</code> 在我们目前的脉络中，对应的实参是 <code>loop->async_io_watcher</code>，而它是通过 <code>uv__io_init(&loop->async_io_watcher, uv__async_io, pipefd[0])</code> 初始化的，我们看一下 <code>uv__io_init</code> 的函数签名：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">uv__io_init</span><span class="hljs-params">(<span class="hljs-keyword">uv__io_t</span>* w, uv__io_cb cb, <span class="hljs-keyword">int</span> fd)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/unix/async.c#L122" target="_blank" rel="nofollow noopener noreferrer">uv__async_io</a> 是接收到虚拟 fd 事件的回调函数，继续看下它的内容：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">uv__async_io</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop, <span class="hljs-keyword">uv__io_t</span>* w, <span class="hljs-keyword">unsigned</span> <span class="hljs-keyword">int</span> events)</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 确保 `w` 必定是 `loop->async_io_watcher`</span>
  assert(w == &loop->async_io_watcher);

  <span class="hljs-keyword">for</span> (;;) &#123;
    <span class="hljs-comment">// 从中读一些内容，`w->fd` 就是上面使用 `eventfd` 创建的虚拟 fd</span>
    <span class="hljs-comment">// 不出意外的话，通知那端的方式、一定是往这个 fd 里面写入一些内容，我们可以后面继续确认</span>
    <span class="hljs-comment">// 从中读取一些内容的目的是避免缓冲区被通知所用的不含实际意义的字节占满</span>
    r = read(w->fd, buf, <span class="hljs-keyword">sizeof</span>(buf));
    <span class="hljs-comment">// ...</span>
  &#125;

  <span class="hljs-comment">// 执行 `loop->async_handles` 队列，任务实际的回调</span>
  QUEUE_MOVE(&loop->async_handles, &<span class="hljs-built_in">queue</span>);
  <span class="hljs-keyword">while</span> (!QUEUE_EMPTY(&<span class="hljs-built_in">queue</span>)) &#123;
    q = QUEUE_HEAD(&<span class="hljs-built_in">queue</span>);
    h = QUEUE_DATA(q, <span class="hljs-keyword">uv_async_t</span>, <span class="hljs-built_in">queue</span>);

    QUEUE_REMOVE(q);
    QUEUE_INSERT_TAIL(&loop->async_handles, q);

    <span class="hljs-comment">// ...</span>
    h->async_cb(h);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们已经知道了事件的订阅，以及事件响应的方式</p>
<p>接着继续确认一下事件通知是如何在线程池中触发的。<a href="http://docs.libuv.org/en/v1.x/async.html?highlight=uv_async_send#c.uv_async_send" target="_blank" rel="nofollow noopener noreferrer">uv_async_send</a> 是唤醒主线程的开放 API，它其实是调用的内部 API <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/unix/async.c#L168" target="_blank" rel="nofollow noopener noreferrer">uv__async_send</a>：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">uv__async_send</span><span class="hljs-params">(<span class="hljs-keyword">uv_loop_t</span>* loop)</span> </span>&#123;
  <span class="hljs-keyword">const</span> <span class="hljs-keyword">void</span>* buf;
  <span class="hljs-keyword">ssize_t</span> len;
  <span class="hljs-keyword">int</span> fd;
 
  <span class="hljs-comment">// ...</span>
  fd = loop->async_io_watcher.fd; 

  <span class="hljs-keyword">do</span>
    <span class="hljs-comment">// 果然事件通知这一端就是往 `eventfd` 创建的虚拟 fd 写入数据</span>
    <span class="hljs-comment">// 剩下的就是交给 epoll 高效的事件调度机制唤醒事件订阅方就可以了</span>
    r = write(fd, buf, len);
  <span class="hljs-keyword">while</span> (r == <span class="hljs-number">-1</span> && errno == EINTR);

  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们最后通过一副意识流的图，对上面的线程池的流程进行小结：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5cf5947fc5a45378b1ec794390990dd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上图中我们的任务是在 <code>uv__run_idle(loop);</code> 执行的回调中通过 <code>uv__work_submit</code> 完成的，但是实际上，对于使用事件循环的应用而言，整个应用的时间片都划分在了各个不同的队列回调中，所以实际上、从其余的队列中提交任务也是可能的</p>
<h3 data-id="heading-25">closing</h3>
<p>我们开头已经介绍过，只有 Handle 才配备了关闭的 API，因为 Request 是一个短暂任务。Handle 的关闭需要使用 <a href="https://github.com/going-merry0/libuv/blob/feature/learn/src/unix/core.c#L108" target="_blank" rel="nofollow noopener noreferrer">uv_close</a>：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">uv_close</span><span class="hljs-params">(<span class="hljs-keyword">uv_handle_t</span>* handle, uv_close_cb close_cb)</span> </span>&#123;
  assert(!uv__is_closing(handle));

  handle->flags |= UV_HANDLE_CLOSING;
  handle->close_cb = close_cb;

  <span class="hljs-keyword">switch</span> (handle->type) &#123;
  <span class="hljs-comment">// 根据不同的 handle 类型，执行各自的资源回收工作</span>
  <span class="hljs-keyword">case</span> UV_NAMED_PIPE:
    uv__pipe_close((<span class="hljs-keyword">uv_pipe_t</span>*)handle);
    <span class="hljs-keyword">break</span>;

  <span class="hljs-keyword">case</span> UV_TTY:
    uv__stream_close((<span class="hljs-keyword">uv_stream_t</span>*)handle);
    <span class="hljs-keyword">break</span>;

  <span class="hljs-keyword">case</span> UV_TCP:
    uv__tcp_close((<span class="hljs-keyword">uv_tcp_t</span>*)handle);
    <span class="hljs-keyword">break</span>;
  <span class="hljs-comment">// ...</span>

  <span class="hljs-keyword">default</span>:
    assert(<span class="hljs-number">0</span>);
  &#125;
  
  <span class="hljs-comment">// 添加到 `loop->closing_handles`</span>
  uv__make_close_pending(handle);
&#125;

<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">uv__make_close_pending</span><span class="hljs-params">(<span class="hljs-keyword">uv_handle_t</span>* handle)</span> </span>&#123;
  assert(handle->flags & UV_HANDLE_CLOSING);
  assert(!(handle->flags & UV_HANDLE_CLOSED));
  handle->next_closing = handle->loop->closing_handles;
  handle->loop->closing_handles = handle;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用 <code>uv_close</code> 关闭 Handle 后，libuv 会先释放 Handle 占用的资源（比如关闭 fd），随后通过调用 <code>uv__make_close_pending</code> 把 handle 连接到 <code>closing_handles</code> 队列中，该队列会在事件循环中被 <code>uv__run_closing_handles(loop)</code> 调用所执行</p>
<p>使用了事件循环后，业务代码的执行时机都在回调中，由于 <code>closing_handles</code> 是最后一个被执行的队列，所以在其余队列的回调中、那些执行 <code>uv_close</code> 时传递的回调，都会在当次迭代中被执行</p>
<h2 data-id="heading-26">小结</h2>
<p>本文沿着 Libuv 的 Linux 实现的脉络对其内部实现进行了简单的探索、尝试解开 libuv 的神秘面纱。很显然，只看这篇是不够的，但愿有幸可以作为想深入了解 libuv 的起始读物。后续我们会结合 Node.js 来探究它们内部是如何衔接的</p>
<blockquote>
<p>本文发布自 <a href="https://github.com/x-orpheus" target="_blank" rel="nofollow noopener noreferrer">网易云音乐大前端团队</a>，文章未经授权禁止任何形式的转载。我们常年招收前端、iOS、Android，如果你准备换工作，又恰好喜欢云音乐，那就加入我们 grp.music-fe (at) corp.netease.com！</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            