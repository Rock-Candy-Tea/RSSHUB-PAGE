
---
title: '计网 - 网络 I_O 模型：BIO、NIO 和 AIO 有什么区别？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce38e53072244eef8d760fe9bb938112~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 20:03:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce38e53072244eef8d760fe9bb938112~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">文章目录</h3>
<ul>
<li><a href="https://juejin.cn/post/6984999052542738439#Pre_6" target="_blank" title="#Pre_6">Pre</a></li>
<li><a href="https://juejin.cn/post/6984999052542738439#IO__24" target="_blank" title="#IO__24">I/O 的编程模型</a></li>
<li><a href="https://juejin.cn/post/6984999052542738439#_112" target="_blank" title="#_112">数据的传输和转化成本</a></li>
<li><a href="https://juejin.cn/post/6984999052542738439#_133" target="_blank" title="#_133">数据结构运用</a></li>
<li>
<ul>
<li><a href="https://juejin.cn/post/6984999052542738439#_139" target="_blank" title="#_139">缓冲区</a></li>
<li><a href="https://juejin.cn/post/6984999052542738439#IO__159" target="_blank" title="#IO__159">I/O 多路复用模型</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/6984999052542738439#_186" target="_blank" title="#_186">总结</a></li>
<li><a href="https://juejin.cn/post/6984999052542738439#QA_199" target="_blank" title="#QA_199">QA</a></li>
<li>
<ul>
<li><a href="https://juejin.cn/post/6984999052542738439#BIONIO__AIO__201" target="_blank" title="#BIONIO__AIO__201">BIO、NIO 和 AIO 有什么区别？</a></li>
<li><a href="https://juejin.cn/post/6984999052542738439#IO__211" target="_blank" title="#IO__211">I/O 多路复用用协程和用线程的区别？</a></li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce38e53072244eef8d760fe9bb938112~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h1 data-id="heading-1"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>Pre</h1>
<p>我们在处理网络问题时，经常是处理 I/O 问题——输入和输出。看上去很复杂，但说白了就是如何把网卡收到的数据给到指定的程序，然后程序如何将数据拷贝到网卡。</p>
<p>在处理 I/O 的时候，要结合具体的场景来思考程序怎么写。从程序的 API 设计上，我们经常会看到 3 类设计：BIO、NIO 和 AIO 。</p>
<p>从本质上说，讨论 BIO、NIO、AIO 的区别，其实就是在讨论 I/O 的模型，我们可以从下面 3 个方面来思考 。</p>
<ul>
<li>编程模型：合理设计 API，让程序写得更舒服。</li>
<li>数据的传输和转化成本：比如减少数据拷贝次数，合理压缩数据等。</li>
<li>高效的数据结构：利用好缓冲区、红黑树等</li>
</ul>
<hr>
<h1 data-id="heading-2"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>I/O 的编程模型</h1>
<p>我们先从编程模型上讨论下 BIO、NIO 和 AIO 的区别。</p>
<p>BIO（Blocking I/O，阻塞 I/O），API 的设计会阻塞程序调用。比如：</p>
<pre><code class="hljs language-bash copyable" lang="bash">byte a = readKey()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假设readKey方法从键盘读取一个按键，如果是非阻塞 I/O 的设计，readKey不会阻塞当前的线程。你可能会问：那如果用户没有按键怎么办？在阻塞 I/O 的设计中，如果用户没有按键线程会阻塞等待用户按键，在非阻塞 I/O 的设计中，线程不会阻塞，没有按键会返回一个空值，比如 null。</p>
<p>最后我们说说 AIO（Asynchronous I/O， 异步 I/O），API 的设计会多创造一条时间线。比如</p>
<pre><code class="hljs language-bash copyable" lang="bash">func callBackFunction(byte keyCode) &#123;

  // 处理按键

&#125;

readKey( callBackFunction )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在异步 I/O 中，readKey方法会直接返回，但是没有结果。结果需要一个回调函数callBackFunction去接收。从这个角度看，其实有两条时间线。第一条是程序的主干时间线，readKey的执行到readKey下文的程序都在这条主干时间线中。而callBackFunction的执行会在用户按键时触发，也就是时间不确定，因此callBackFunction中的程序是另一条时间线也是基于这种原因产生的，我们称作异步，异步描述的就是这种时间线上无法同步的现象，你不知道callbackFunction何时会执行。</p>
<p>但是我们通常说某某语言提供了异步 I/O，不仅仅是说提供上面程序这种写法，上面的写法会产生一个叫作回调地狱的问题，本质是异步程序的时间线错乱，导致维护成本较高。</p>
<pre><code class="hljs language-java copyable" lang="java">request(<span class="hljs-string">"/order/123"</span>, (data1) -> &#123;

  <span class="hljs-comment">//..</span>

  request(<span class="hljs-string">"/product/456"</span>, (data2) -> &#123;

    <span class="hljs-comment">// ..</span>

    request(<span class="hljs-string">"/sku/789"</span>, (data3) -> &#123;

      <span class="hljs-comment">//...</span>

    &#125;)

  &#125;)

&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如上面这段程序（称作回调地狱）维护成本较高，因此通常提供异步 API 编程模型时，我们会提供一种将异步转化为同步程序的语法。比如下面这段伪代码：</p>
<pre><code class="hljs language-java copyable" lang="java">Future future1 = request(<span class="hljs-string">"/order/123"</span>)

Future future2 = request(<span class="hljs-string">"/product/456"</span>)

Future future3 = request(<span class="hljs-string">"/sku/789"</span>)

<span class="hljs-comment">// ...</span>

<span class="hljs-comment">// ...</span>

order = future1.get()

product = future2.get()

sku = future3.get()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>request 函数是一次网络调用，请求订单 ID=123 的订单数据。本身 request 函数不会阻塞，会马上执行完成，而网络调用是一次异步请求，调用不会在request("/order/123")下一行结束，而是会在未来的某个时间结束。因此，我们用一个 Future 对象封装这个异步操作。future.get()是一个阻塞操作，会阻塞直到网络调用返回。</p>
<p>在request和future.get之间，我们还可以进行很多别的操作，比如发送更多的请求。 像 Future 这样能够将异步操作再同步回主时间线的操作，我们称作异步转同步，也叫作异步编程。</p>
<hr>
<h1 data-id="heading-3"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>数据的传输和转化成本</h1>
<p>上面我们从编程的模型上对 I/O 进行了思考，接下来我们从内部实现分析下 BIO、NIO 和 AIO。无论是哪种 I/O 模型，都要将数据从网卡拷贝到用户程序（接收），或者将数据从用户程序传输到网卡（发送）。</p>
<p>另一方面，有的数据需要编码解码，比如 JSON 格式的数据。还有的数据需要压缩和解压。数据从网卡到内核再到用户程序是 2 次传输。注意，将数据从内存中的一个区域拷贝到另一个区域，这是一个 CPU 密集型操作。数据的拷贝归根结底要一个字节一个字节去做。</p>
<p>从网卡到内核空间的这步操作，可以用 DMA（Direct Memory Access）技术控制。DMA 是一种小型设备，用 DMA 拷贝数据可以不使用 CPU，从而节省计算资源。遗憾的是，通常我们写程序的时候，不能直接控制 DMA，因此 DMA 仅仅用于设备传输数据到内存中。</p>
<p>不过，从内核到用户空间这次拷贝，可以用内存映射技术，将内核空间的数据映射到用户空间。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f7cec627a8947b99d21e5d60fec356b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h1 data-id="heading-4"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>数据结构运用</h1>
<p>在处理网络 I/O 问题的时候，还有一个重点问题要注意，就是数据结构的运用。</p>
<h2 data-id="heading-5"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>缓冲区</h2>
<p>缓冲区是一种在处理 I/O 问题中常用的数据结构，</p>
<ul>
<li>一方面<strong>缓冲区起到缓冲作用</strong>，在瞬时 I/O 量较大的时候，利用排队机制进行处理。</li>
<li>另一方面，<strong>缓冲区起到一个批处理的作用</strong>，比如 1000 次 I/O 请求进入缓冲区，可以合并成 50 次 I/O 请求，那么整体性能就会上一个档次。</li>
</ul>
<p>举个例子，比如你有 1000 个订单要写入 MySQL，如果这个时候你可以将这 1000 次请求合并成 50 次，那么磁盘写入次数将大大减少。同理，假设有 10000 次网络请求，如果可以合并发送，会减少 TCP 协议握手时间，可以最大程度地复用连接；另一方面，如果这些请求都较小，还可以粘包复用 TCP 段。在处理 Web 网站的时候，经常会碰到将多个 HTTP 请求合并成一个发送，从而减少整体网络开销的情况。</p>
<p>除了上述两方面原因，<strong>缓冲区还可以减少实际对内存的诉求</strong>。数据在网卡到内核，内核到用户空间的过程中，建议都要使用缓冲区。当收到的某个请求较大的时候，抽象成流，然后使用缓冲区可以减少对内存的使用压力。这是因为使用了缓冲区和流，就不需要真的准备和请求数据大小一致的内存空间了。可以将缓冲区大小规模的数据分成多次处理完，实际的内存开销是缓冲区的大小</p>
<hr>
<h2 data-id="heading-6"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>I/O 多路复用模型</h2>
<p>在运用数据结构的时候，还要思考 I/O 的多路复用用什么模型。</p>
<p>假设你在处理一个高并发的网站，每秒有大量的请求打到你的服务器上，你用多少个线程去处理 I/O 呢？对于没有需要压缩解压的场景，处理 I/O 的主要开销还是数据的拷贝。那么一个 CPU 核心每秒可以完成多少次数据拷贝呢？</p>
<p>拷贝，其实就是将内存中的数据从一个地址拷贝到另一个地址。再加上有 <strong>DMA，内存映射</strong>等技术，拷贝是非常快的。不考虑 DMA 和内存映射，一个 3GHz 主频的 CPU 每秒可以拷贝的数据也是百兆级别的。当然，速度还受限于内存本身的速度。<strong>因此总的来说，I/O 并不需要很大的计算资源</strong>。通常我们在处理高并发的时候，也不需要大量的线程去进行 I/O 处理。</p>
<p>对于多数应用来说，处理 I/O 的成本小于处理业务的成本。处理高并发的业务，可能需要大量的计算资源。每笔业务也可能会需要更多的 I/O，比如远程的 RPC 调用等。</p>
<p><strong>因此我们在处理高并发的时候，一种常见的 I/O 多路复用模式就是由少量的线程处理大量的网络接收、发送工作。然后再由更多的线程，通常是一个线程池处理具体的业务工作</strong>。</p>
<p>在这样一个模式下，有一个核心问题需要解决，就是当操作系统内核监测到一次 I/O 操作发生，它如何具体地通知到哪个线程调用哪段程序呢？</p>
<p>这时，<strong>一种高效的模型会要求我们将线程、线程监听的事件类型，以及响应的程序注册到内核</strong>。具体来说，比如某个客户端发送消息到服务器的时候，我们需要尽快知道哪个线程关心这条消息（处理这个数据）。例如 <strong>epoll 就是这样的模型，内部是红黑树。我们可以具体地看到文件描述符构成了一棵红黑树，而红黑树的节点上挂着文件描述符对应的线程、线程监听事件类型以及相应程序</strong>。</p>
<hr>
<p>讲了这么多，和 BIO、AIO、NIO 有什么关系？这里有两个联系。</p>
<p><strong>首先是无论哪种编程模型都需要使用缓冲区，也就是说 BIO、AIO、NIO 都需要缓冲区</strong>，因此关系很大。在我们使用任何编程模型的时候，如果内部没有使用缓冲区，那么一定要在外部增加缓冲区。<strong>另一个联系是类似 epoll 这种注册+消息推送的方式，可以帮助我们节省大量定位具体线程以及事件类型的时间。这是一个通用技巧，并不是独有某种 I/O 模型才可以使用</strong>。</p>
<p>不过从能力上分析，使用类似 epoll 这种模型，确实没有必要让处理 I/O 的线程阻塞，因为操作系统会将需要响应的事件源源不断地推送给处理的线程，因此可以考虑不让处理线程阻塞（比如用 NIO）</p>
<hr>
<h1 data-id="heading-7"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>总结</h1>
<p>从 3 个方面讨论了 I/O 模型。</p>
<ul>
<li>第一个是<strong>编程模型</strong>，阻塞、非阻塞、异步 3 者 API 的设计会有比较大的差异。通常情况下我们说的异步编程是异步转同步。异步转同步最大的价值，就是提升代码的可读性。可读，就意味着维护成本的下降以及扩展性的提升。</li>
<li>第二个在设计系统的 I/O 时，另一件需要考虑的就是<strong>数据传输以及转化的成本</strong>。传输主要是拷贝，比如可以使用内存映射来减少数据的传输。但是这里要注意一点，内存映射使用的内存是内核空间的缓冲区，因此千万不要忘记回收。因为这一部分内存往往不在我们所使用的语言提供的内存回收机制的管控范围之内。</li>
<li>最后是关于<strong>数据结构</strong>的运用，针对不同的场景使用不同的缓冲区，以及选择不同的消息通知机制，也是处理高并发的一个核心问题。</li>
</ul>
<p>从上面几个角度去看 I/O 的模型，你会发现，编程模型是编程模型、数据的传输是数据的传输、消息的通知是消息的通知，它们是不同的模块，完全可以解耦，也可以根据自己不同的业务特性进行选择。虽然在一个完整的系统设计中，往往提出的是一套完整的解决方案 ，但实际上我们还是应该将它们分开去思考，这样可以产生更好的设计思路。</p>
<hr>
<h1 data-id="heading-8"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>QA</h1>
<h2 data-id="heading-9"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>BIO、NIO 和 AIO 有什么区别？</h2>
<p>总的来说，这三者是三个 I/O 的编程模型。BIO 接口设计会直接导致当前线程阻塞。NIO 的设计不会触发当前线程的阻塞。AIO 为 I/O 提供了异步能力，也就是将 I/O 的响应程序放到一个独立的时间线上去执行。但是通常 AIO 的提供者还会提供异步编程模型，就是实现一种对异步计算封装的数据结构，并且提供将异步计算同步回主线的能力。</p>
<p>通常情况下，这 3 种 API 都会伴随 I/O 多路复用。<strong>如果底层用红黑树管理注册的文件描述符和事件，可以在很小的开销内由内核将 I/O 消息发送给指定的线程</strong>。另外，还可以用 <strong>DMA，内存映射等方式优化 I/O</strong>。</p>
<hr>
<h2 data-id="heading-10"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>I/O 多路复用用协程和用线程的区别？</h2>
<p>线程是执行程序的最小单位。I/O 多路复用时，会用单个线程处理大量的 I/O。还有一种执行程序的模型，叫协作程，协程是轻量级的线程。操作系统将执行资源分配给了线程，然后再调度线程运行。如果要实现协程，就要利用分配给线程的执行资源，在这之上再创建更小的执行单位。协程不归操作系统调度，协程共享线程的执行资源。</p>
<p>而 I/O 多路复用的意义，是减少线程间的切换成本。因此从设计上，只要是用单个线程处理大量 I/O 工作，线程和协程是一样的，并无区别。如果是单线程处理大量 I/O，使用协程也是依托协程对应线程执行能力。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c4ae765a1c549e387543eb4e9aa800c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            