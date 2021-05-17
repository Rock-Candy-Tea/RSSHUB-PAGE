
---
title: '🔍【攻破技术盲点】— 网络IO模型的分析（上）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cca111b19086486997075f5af89b9cdb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 20:04:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cca111b19086486997075f5af89b9cdb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Linux的网络IO模型</h1>
<blockquote>
<p><strong>网络IO的本质是socket的读写，socket在Linux中被抽象为流</strong>，<strong>IO可以理解为对流的操作。</strong></p>
</blockquote>
<h2 data-id="heading-1">IO的分类和范畴</h2>
<blockquote>
<p><strong>IO本身可以分为内存IO、网络IO和磁盘IO还有缓存IO等，一般讨论IO时更多是指后（网络IO和磁盘IO，因为这两个是最慢的哈哈），此处特别分析和说明网络IO</strong>。</p>
</blockquote>
<h2 data-id="heading-2">操作处理的分类</h2>
<h3 data-id="heading-3">阻塞/非阻塞</h3>
<blockquote>
<p><strong>针对函数/方法的实现方式而言，即数据就绪之前是立刻返回还是等待，即发起IO请求后是否会阻塞</strong>。</p>
</blockquote>
<h4 data-id="heading-4">阻塞IO机制</h4>
<blockquote>
<p><strong>阻塞IO情况下，当用户调用read后，用户线程会被阻塞，等内核数据准备好并且数据从内核缓冲区拷贝到用户态缓存区后read才会返回</strong>。可以看到是阻塞的<strong>两个部分</strong>。</p>
</blockquote>
<ul>
<li>
<p><strong>CPU把数据从磁盘读到内核缓冲区。</strong></p>
</li>
<li>
<p><strong>CPU把数据从内核缓冲区拷贝到用户缓冲区。</strong></p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cca111b19086486997075f5af89b9cdb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">非阻塞IO机制</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa420dfc49724d968d9dd9e667f9c4b7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>非阻塞IO发出read请求后发现数据没准备好，会继续往下执行，此时应用程序会不断轮询polling内核询问数据是否准备好，当数据没有准备好时，内核立即返回EWOULDBLOCK错误。</p>
</li>
<li>
<p>直到数据被拷贝到应用程序缓冲区，read请求才获取到结果。并且你要注意！<strong>这里最后一次 read 调用获取数据的过程，是一个同步的过程，是需要等待的过程</strong>。这里的同步指的是内核态的数据拷贝到用户程序的缓存区这个过程。</p>
</li>
</ul>
<h3 data-id="heading-6">同步/异步</h3>
<blockquote>
<p><strong>IO读操作指数据流经：网络 -> 内核缓冲区 -> 用户内存</strong></p>
</blockquote>
<ul>
<li>
<p><strong>同步和异步的主要区别在于数据从内核缓冲区 -> 用户内存这个过程需不需要用户进程等待</strong>。</p>
</li>
<li>
<p><strong>等待内核态准备数据结束之后，会自动回通知用户态的线程进行读取信息数据，此时之前用户态的线程不需要等待，可以去做其他操作。</strong></p>
</li>
</ul>
<blockquote>
<p><strong>对于一个网络IO，会涉及到两个系统对象，一个是调用这个IO的process（or thread）【用户态】，另一个就是系统内核（kernel）【内核态】</strong></p>
</blockquote>
<h4 data-id="heading-7">当一个用户态发生read操作发生时，它会经历两个阶段：</h4>
<ul>
<li>
<p><strong>第一阶段：用户态线程等待内核态的数据准备 (Waiting for the data to be ready)</strong>。</p>
</li>
<li>
<p><strong>第二阶段：用户态线程，将数据从内核拷贝到进程中 (Copying the data from the kernel to the process)。</strong></p>
<ul>
<li>
<p><strong>第一步：通常涉及等待网络上的数据分组到达，然后被复制到内核的某个缓冲区</strong>。</p>
</li>
<li>
<p><strong>第二步：把数据从内核缓冲区复制到（用户态）应用进程缓冲区。网络应用处理的是两大类问题：网络IO、数据计算。前者给应用带来的性能瓶颈更大。</strong></p>
</li>
</ul>
</li>
</ul>
<h4 data-id="heading-8">网络IO的模型大致有如下几种：</h4>
<ul>
<li>同步模型（synchronous IO）</li>
<li>阻塞IO模型（blocking IO）</li>
<li>非阻塞IO模型（non-blocking IO）</li>
<li>多路复用IO模型（multiplexing IO）</li>
<li>信号驱动IO模型（signal-driven IO）</li>
<li>异步IO（asynchronous IO）</li>
</ul>
<h2 data-id="heading-9">阻塞IO模型（blocking IO）</h2>
<p>在<strong>Linux</strong>中，默认情况下所有的<strong>socket</strong>都是<strong>blocking</strong>，一个典型的读操作流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1838b59343464048bd219960d16ce299~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当用户进程调用了<strong>recvfrom</strong>这个系统调用，如上所述，会有两个阶段</p>
<h3 data-id="heading-10">准备数据：</h3>
<ul>
<li>
<p>很多时候数据在一开始还没有到达，这个时候kernel就要等待足够的数据到来。而用户进程会一直阻塞。</p>
</li>
<li>
<p>当kernel等到数据准备好了，它会将数据从kernel中拷贝到用户内存，然后kernel返回，用户进程结束block状态，重新运行。</p>
</li>
</ul>
<blockquote>
<p>Blocking IO的特点就是IO执行的两个阶段都是block了的。</p>
</blockquote>
<h2 data-id="heading-11">非阻塞IO模型（non-blocking IO）[poll]</h2>
<p>在Linux中，可以通过设置<strong>socket使其变为non-blocking</strong>，其流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3dfc522a948d4ec6ad323405baabdb21~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><strong>当用户进程调用了recvfrom这个系统调用，如果kernel中的数据还没有准备好，那么用户进程不会block而是立刻返回一个error，即从用户的角度而言，不需要等待，马上得到一个结果。</strong></p>
</li>
<li>
<p><strong>从图中可以看出，用户进程在判断结果是一个error后，了解到数据还没有准备好，于是就不断重复上述操作直至kernel中的数据准备好，然后它马上将数据拷贝到了用户内存，然后返回。</strong></p>
</li>
</ul>
<h2 data-id="heading-12">多路复用IO模型（multiplexing IO）</h2>
<blockquote>
<p><strong>select/epoll/evpoll</strong>，也被称作是Event-Driven IO。好处是单个<strong>process</strong>可以同时处理多个网络连接的IO。</p>
</blockquote>
<ul>
<li>
<p><strong>基本原理可见下面的“IO复用技术”。也叫多路IO就绪通知。</strong></p>
</li>
<li>
<p><strong>这是一种进程预先告知内核的能力，让内核发现进程指定的一个或多个IO条件就绪了，就通知用户进程</strong>。</p>
</li>
<li>
<p><strong>使得一个进程能在一连串的事件上等待。</strong></p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/324301b37b1b490287bf148be1af6942~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><strong>这个流程和Blocking IO的流程其实并没有太多不同，事实上仅从图中看起来，由于需要进行两次系统调用，可能更差一些。但是，Select的优势在于它可以同时处理多个连接。</strong></p>
</li>
<li>
<p><strong>如果处理的连接数不是很高的话，使用“Select/Epoll 的 Web Server”不一定比使用“多线程 + BIO的Web Server”性能更好，反而延迟会更大。</strong></p>
</li>
</ul>
<blockquote>
<p><strong>Select/Epoll的优势并不是对于单个连接能处理得更快，而是在于能处理更多的连接。</strong></p>
</blockquote>
<blockquote>
<p><strong>在IO多路复用模型中，实际中，对于每一个socket，一般都设置成为non-blocking，但是，如上图所示，整个用户的process其实是一直被block的。只不过process是被select这个函数block，而不是被socket IO给block。</strong></p>
</blockquote>
<h2 data-id="heading-13">异步IO（asynchronous IO）</h2>
<blockquote>
<p>用户进程发起read操作之后，立刻就可以开始去做其它的事。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7b04fa2d3fa4ccbb4aa2dd3dc1dfda9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p><strong>从kernel的角度，当它受到一个asynchronous read之后，首先它会立刻返回，所以不会对用户进程产生任何block</strong>。</p>
</li>
<li>
<p><strong>kernel会等待数据准备完成，然后将数据拷贝到用户内存，当这一切都完成之后，kernel会给用户进程发送一个signal，告诉它read操作完成了</strong>。</p>
</li>
</ol>
<h3 data-id="heading-14">比较</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92c3b51dfba944f285bce56d8ece4f6b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">非阻塞和异步的区别</h3>
<blockquote>
<p>经过上面的介绍，会发现non-blocking IO和asynchronous IO的区别还是很明显的。</p>
</blockquote>
<ul>
<li>在non-blocking IO中，虽然进程大部分时间都不会被block，但是它仍然要求进程去主动的check，并且当数据准备完成以后，也需要进程主动的再次调用recvfrom来将数据拷贝到用户内存。</li>
<li>asynchronous IO则完全不同。它就像是用户进程将整个IO操作交给了他人（kernel）完成，然后他人做完后发信号通知。在此期间，用户进程不需要去检查IO操作的状态，也不需要主动的去拷贝数据。</li>
</ul>
<h1 data-id="heading-16">IO复用技术</h1>
<blockquote>
<p><strong>在IO编程过程中，当需要处理多个请求时，可以使用多线程和IO复的方式进行处理。</strong></p>
</blockquote>
<h2 data-id="heading-17">IO复用是什么？</h2>
<blockquote>
<p><strong>把多个IO的阻塞复用到一个select之类的阻塞上，从而使得系统在单线程的情况下同时支持处理多个请求</strong>。</p>
</blockquote>
<h3 data-id="heading-18">IO复用常见的应用场景：</h3>
<ul>
<li>服务器需要同时处理多个处于监听状态和多个连接状态的套接字；</li>
<li>服务器需要处理多种网络协议的套接字</li>
<li>IO复用的实现方式目前主要有select、poll和epoll/evpoll。</li>
</ul>
<h3 data-id="heading-19">select和poll的原理基本相同：</h3>
<ol>
<li>
<p><strong>注册待侦听的fd(这里的fd创建时最好使用非阻塞)</strong></p>
</li>
<li>
<p><strong>每次调用都去检查这些fd的状态，当有一个或者多个fd就绪的时候返回</strong></p>
</li>
<li>
<p><strong>返回结果中包括已就绪和未就绪的fd</strong></p>
</li>
</ol>
<h3 data-id="heading-20">select和poll与epoll机制的比较</h3>
<blockquote>
<p><strong>Linux网络编程过程中，相比于select/poll，epoll是有着更明显优势的一种选择</strong>。</p>
</blockquote>
<ul>
<li>
<p>支持一个进程打开的socket描述符不受限制（仅受限于操作系统的最大文件句柄数 unlimit）。</p>
<ul>
<li>
<p>Select的缺陷：一个进程所打开的FD受限，默认是2048；尽管数值可以更改，但同样可能导致网络效率下降；可以选择多进程的解决方案，但是进程的创建本身代价不小，而且进程间数据同步远比不上线程间同步的高效。</p>
</li>
<li>
<p>epoll所支持的FD上限是最大可以打开文件的数目：<strong>/proc/sys/fs/file-max</strong></p>
</li>
</ul>
</li>
</ul>
<p><strong>IO效率可能随着文件描述符数目的增加而线性下降。</strong></p>
<ul>
<li>
<p>epoll扫描系统的机制不同</p>
<ul>
<li>
<p><strong>select/poll是线性扫描FD的集合</strong>；</p>
</li>
<li>
<p><strong>epoll是根据FD上面的回调函数实现的，活跃的socket会主动去调用该回调函数</strong>，其它socket则不会，相当于市是一个AIO，只不过推动力在OS内核。</p>
</li>
</ul>
</li>
<li>
<p><strong>使用mmap加速内核与用户空间的消息传递，zero-copy的一种</strong>。</p>
</li>
<li>
<p><strong>epoll的API更加简单</strong>。</p>
</li>
<li>
<p>IO复用还有一个 水平触发 和 边缘触发 的概念：</p>
<ul>
<li>水平触发：当就绪的fd未被用户进程处理后，下一次查询依旧会返回，这是select和poll的触发方式。</li>
<li>边缘触发：无论就绪的fd是否被处理，下一次不再返回。理论上性能更高，但是实现相当复杂，并且任何意外的丢失事件都会造成请求处理错误。epoll默认使用水平触发，通过相应选项可以使用边缘触发。</li>
</ul>
</li>
</ul>
<h1 data-id="heading-21">IO模型的总结</h1>
<blockquote>
<p>最后，再举几个不是很恰当的例子来说明这四个IO Model，有A，B，C，D四个人在钓鱼：</p>
</blockquote>
<ul>
<li>
<p>A用的是最老式的鱼竿，所以呢，得一直守着，等到鱼上钩了再拉杆；（同步阻塞）</p>
</li>
<li>
<p>B的鱼竿有个功能，能够显示是否有鱼上钩，所以呢，B就和旁边的MM聊天，隔会再看看有没有鱼上钩，有的话就迅速拉杆；（非阻塞）</p>
</li>
<li>
<p>C用的鱼竿和B差不多，但他想了一个好办法，就是同时放好几根鱼竿，然后守在旁边，一旦有显示说鱼上钩了，它就将对应的鱼竿拉起来；（io多路复用机制）</p>
</li>
<li>
<p>D是个有钱人，干脆雇了一个人帮他钓鱼，一旦那个人把鱼钓上来了，就给D发个短信。（异步机制）</p>
</li>
</ul></div>  
</div>
            