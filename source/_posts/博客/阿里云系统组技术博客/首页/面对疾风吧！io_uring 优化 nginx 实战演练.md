
---
title: '面对疾风吧！io_uring 优化 nginx 实战演练'
categories: 
 - 博客
 - 阿里云系统组技术博客
 - 首页
headimg: 'https://kernel.taobao.org//2020/09/IO_uring_Optimization_for_Nginx/1.png'
author: 阿里云系统组技术博客
comments: false
date: Sun, 27 Sep 2020 00:00:00 GMT
thumbnail: 'https://kernel.taobao.org//2020/09/IO_uring_Optimization_for_Nginx/1.png'
---

<div>   
<h2 id="引言">引言</h2> <p>io_uring是Linux内核在v5.1引入的一套异步IO接口，随着其迅速发展，现在的io_uring已经远远超过了纯IO的范畴。从Linux v5.3版本开始，io_uring陆续添加了网络编程相关的API，对用户提供sendmsg、recvmsg、accept、connect等接口的异步支持，将io_uring的生态范围扩大到了网络领域。</p> <p>另外从Linux v5.7开始，io_uring对这些异步接口提供FAST POLL机制，用户无需再使用像select、event poll等多路复用机制来监听文件句柄，只要把读写请求直接丢到io_uring的submit queue中并提交，当文件句柄不可读写时，内核会主动添加poll handler，当文件句柄可读写时主动调用poll handler再次下发读写请求，从而减少系统调用次数提高性能。</p> <p>上一篇我们初探了 io_uring 用于网络的编程模型以及 echo server benchmark 下的性能表现，这篇文章我们将基于通用应用 nginx 实战。</p> <h2 id="nginx-io_uring-代码优化">Nginx io_uring 代码优化</h2> <p>Nginx是一款轻量级的Web服务器、反向代理服务器，由于它的内存占用少，启动极快，高并发能力强，在互联网项目中广泛应用。</p> <p><img src="https://kernel.taobao.org//2020/09/IO_uring_Optimization_for_Nginx/1.png" alt="img" referrerpolicy="no-referrer"></p> <p>从架构上看，Nginx由一个master和多个worker进程组成，多个worker之间不需要加锁，独立处理与client的连接和网络请求。worker是一个单线程大循环，这与上一篇“你认为 io_uring 只适用于存储 IO？大错特错！”文章中描述的 echo server 模型基本一致。</p> <h2 id="基于event-poll的编程模型">基于event poll的编程模型</h2> <p>event poll是Nginx在Linux下的默认事件模型。</p> <p><img src="https://kernel.taobao.org//2020/09/IO_uring_Optimization_for_Nginx/2.png" alt="img" referrerpolicy="no-referrer"></p> <p>event poll事件模型把listen fd以及新建连接的sock fd都注册进event poll中，当这些fd上有数据可读时，等待在epoll_wait()的worker进程会被唤醒，调用相应的回调函数进行处理，这里的recv、writev请求都为同步请求。</p> <h2 id="基于io_uring的编程模型">基于io_uring的编程模型</h2> <p>前面提到，io_uring的FAST POLL机制允许数据在未ready的情况下就直接下发，不需要再把普通连接的fd注册进event poll。另外这里的读写请求通过io_uring异步下发，处理流程大致如下：</p> <p><img src="https://kernel.taobao.org//2020/09/IO_uring_Optimization_for_Nginx/3.png" alt="img" referrerpolicy="no-referrer"></p> <p>事实上，accept()也可以采取FAFST POLL机制，无需等待listen_fd数据可读就直接下发，以减少系统调用次数。但在调试过程中发现这样accept()失败概率大大增加，而每次失败的accept()都会带来一次无效的sock内存申请和释放，这个开销较大，因此依然采用类似event poll的方式来侦听listen fd。后续针对这块可以做一些优化。</p> <h2 id="测试结果">测试结果</h2> <h3 id="测试环境">测试环境</h3> <ul> <li>测试机器 <ul> <li>CPU: Intel(R) Xeon(R) CPU E5-2682 v4 @ 2.50GHz 64逻辑核</li> <li>server cmdline添加：mitigation=on</li> </ul> </li> <li>nginx配置</li> </ul> <div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>user root;
http &#123;
    access_log  off;
    server &#123;
        access_log  off; // 关闭access log，否则会写日志，影响测试
        location / &#123;
            return 200;  // 不读本地文件，直接返回200
        &#125;
    &#125;
&#125;
</code></pre></div></div> <ul> <li> <p>benchmark 使用轻量级HTTP性能测试工具wrk进行压测。</p> </li> <li> <p>测试命令</p> <div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>长连接 wrk -c $connection -t $thread -d 120 $url
短连接 wrk -c $connection -t $thread -H "Connection: Close" -d 120 $url
</code></pre></div> </div> </li> </ul> <h3 id="测试结果-1">测试结果</h3> <h4 id="长连接">长连接</h4> <ul> <li>connection=1000，thread=200, 测试server上不同worker数目性能。</li> </ul> <p><img src="https://kernel.taobao.org//2020/09/IO_uring_Optimization_for_Nginx/4.png" alt referrerpolicy="no-referrer"></p> <p>worker数目在8以下时，QPS有20%左右的提升。随着worker数目增大，CPU不成为瓶颈，收益逐渐降低。</p> <ul> <li>server单worker，测试client端不同连接数性能(thread取默认数2）。</li> </ul> <p><img src="https://kernel.taobao.org//2020/09/IO_uring_Optimization_for_Nginx/5.png" alt referrerpolicy="no-referrer"> <img src="https://kernel.taobao.org//2020/09/IO_uring_Optimization_for_Nginx/6.png" alt referrerpolicy="no-referrer"></p> <p>可以看到单worker情况下，500个连接以上，QPS有20%以上的提升。从系统调用数目上看，io uring的系统调用数基本上在event poll的1/10以内。</p> <h4 id="短连接">短连接</h4> <ul> <li>connection=1000，thread=200, 测试server上不同worker数目性能。</li> </ul> <p><img src="https://kernel.taobao.org//2020/09/IO_uring_Optimization_for_Nginx/7.png" alt referrerpolicy="no-referrer"></p> <p>短连接场景，io uring相对于event poll非但没有提升，甚至在某些场景下有5%~10%的性能下降。究其原因，除了io uring框架本身带来的开销以外，还可能跟io uring编程模式下请求批量下发而带来的延迟有关。</p> <h2 id="总结及下一步工作">总结及下一步工作</h2> <p>从笔者目前的测试来看，io_uring在网络编程方面的优化更适合长连接场景，在长连接场景下最高有20%多的提升。短连接场景还有待优化，主要考虑以下两方面：</p> <ul> <li>io uring本身框架开销的优化，当然这个优化对长连接同样适用。</li> <li>针对短连接的优化，如针对accept()请求，先检查是否有数据可读，避免无效内存申请释放；多个accept()一起下发等。</li> </ul> <p>nginx 和 echo server 等优化实践相关内容（包含源代码），我们都已经在 OpenAnolis 社区高性能存储 SIG 开源（openanolis.org）。也欢迎大家积极参与讨论和贡献，一起探索 io_uring 的高性能之路。</p>   
</div>
            