
---
title: '下一代异步 IO io_uring 技术解密'
categories: 
 - 博客
 - 阿里云系统组技术博客
 - 首页
headimg: 'https://kernel.taobao.org//2020/08/Introduction_to_IO_uring/1.png'
author: 阿里云系统组技术博客
comments: false
date: Sun, 02 Aug 2020 00:00:00 GMT
thumbnail: 'https://kernel.taobao.org//2020/08/Introduction_to_IO_uring/1.png'
---

<div>   
<h2 id="概述">概述</h2> <p>Alibaba Cloud Linux 2 是阿里云操作系统团队基于开源 Linux 4.19 LTS 版本打造的一款针对云应用场景的下一代 Linux OS 发行版。在首次推出一年后，阿里云操作系统团队对外正式发布了Alibaba Cloud Linux 2 LTS 版本。LTS 版本的发布是一个重要的里程碑，标志着阿里云操作系统团队将为 Alibaba Cloud Linux 2 提供长期技术支持、稳定的更新和更好的服务，为 Alibaba Cloud Linux 2 的客户提供更多保障。</p> <p>上一篇我们在 Alibaba Cloud Linux 2 上对比测试了 io_uring 与 libaio 以及 SPDK，可以看到 io_uring 带来的性能提升非常明显。这篇文章我们详细分析下 io_uring 的原理，以及我们在 io_uring 社区所做的工作。</p> <h2 id="io_uring-原理介绍">io_uring 原理介绍</h2> <p>为了从根本上解决当前 Linux aio 存在的问题和约束，io_uring 从零开始全新设计的了异步 IO 框架。其设计的主要目标如下：</p> <ul> <li>简单易用，方便应用集成。</li> <li>可扩展，不仅仅为 block IO 使用，同样可以用于网络 IO。</li> <li>特性丰富，满足所有应用，如 buffer io。</li> <li>高效，尤其是针对大部分场景的 512 字节或 4K IO。</li> <li>可伸缩，满足峰值场景的性能需要。</li> </ul> <p>io_uring 为了避免在提交和完成事件中的内存拷贝，设计了一对共享的 ring buffer 用于应用和内核之间的通信。其中，针对提交队列（SQ），应用是 IO 提交的生产者（producer），内核是消费者（consumer）；反过来，针对完成队列（CQ），内核是完成事件的生产者，应用是消费者。</p> <p><img src="https://kernel.taobao.org//2020/08/Introduction_to_IO_uring/1.png" alt="img" referrerpolicy="no-referrer"></p> <p>共享环的设计主要带来以下 3 个好处：</p> <ul> <li>提交、完成请求时节省应用和内核之间的内存拷贝；</li> <li>使用 SQPOLL 高级特性时，应用程序无需调用系统调用；</li> <li>无锁操作，用 memory ordering 实现同步。</li> </ul> <h3 id="io_uring-系统调用">io_uring 系统调用</h3> <p>io_uring 一共提供了 3 个系统调用：io_uring_setup()，io_uring_enter()，以及io_uring_register()，位于 fs/io_uring.c。</p> <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cm">/**
 * io_uring_setup - setup a context for performing asynchronous I/O
 */</span>
<span class="kt">int</span> <span class="n">io_uring_setup</span><span class="p">(</span><span class="n">u32</span> <span class="n">entries</span><span class="p">,</span> <span class="k">struct</span> <span class="n">io_uring_params</span> <span class="o">*</span><span class="n">p</span><span class="p">);</span>
<span class="cm">/**
 * io_uring_enter - initiate and/or complete asynchronous I/O
 */</span>
<span class="kt">int</span> <span class="n">io_uring_enter</span><span class="p">(</span><span class="kt">int</span> <span class="n">fd</span><span class="p">,</span> <span class="kt">unsigned</span> <span class="kt">int</span> <span class="n">to_submit</span><span class="p">,</span> <span class="kt">unsigned</span> <span class="kt">int</span> <span class="n">min_complete</span><span class="p">,</span>
                   <span class="kt">unsigned</span> <span class="kt">int</span> <span class="n">flags</span><span class="p">,</span> <span class="n">sigset_t</span> <span class="o">*</span><span class="n">sig</span><span class="p">)</span>
 
<span class="cm">/**
 * io_uring_register - register files or user buffers for asynchronous I/O
 */</span>
<span class="kt">int</span> <span class="n">io_uring_register</span><span class="p">(</span><span class="kt">int</span> <span class="n">fd</span><span class="p">,</span> <span class="kt">unsigned</span> <span class="kt">int</span> <span class="n">opcode</span><span class="p">,</span> <span class="kt">void</span> <span class="o">*</span><span class="n">arg</span><span class="p">,</span>
                      <span class="kt">unsigned</span> <span class="kt">int</span> <span class="n">nr_args</span><span class="p">)</span>
</code></pre></div></div> <p>Alibaba Cloud Linux 2 LTS 版本支持的异步操作如下，更多的特性支持持续完善中。</p> <ul> <li> <p>IORING_OP_NOP 仅产生一个完成事件，除此之外没有任何操作。</p> </li> <li> <p>IORING_OP_READV / IORING_OP_WRITEV 提交 readv() / writev() 操作，大多数场景最核心的操作。</p> </li> <li> <p>IORING_OP_READ_FIXED / IORING_OP_WRITE_FIXED 使用已注册的 buffer 来提交 IO 操作，由于这些 buffer 已经完成映射，可以降低系统调用的开销。</p> </li> <li> <p>IORING_OP_FSYNC 下发 fsync() 调用。</p> </li> <li> <p>IORING_OP_POLL_ADD / IORING_OP_POLL_REMOVE 使用 IORING_OP_POLL_ADD 可对一组文件描述符 (file descriptors) 执行 poll() 操作；可以使用 IORING_OP_POLL_REMOVE 显式地取消 poll()。这种方式可以用来异步地监控一组文件描述符。</p> </li> <li> <p>IORING_OP_SYNC_FILE_RANGE 执行 sync_file_range() 调用，是对 fsync() 的一个增强。</p> </li> <li> <p>IORING_OP_SENDMSG / IORING_OP_RECVMSG 在 sendmsg() 和 recvmsg() 基础上，提供异步收发网络包功能。</p> </li> <li> <p>IORING_OP_TIMEOUT 用户态程序等待 IO 完成事件时，可以通过 IORING_OP_TIMEOUT 设置一个超时时间，类似 io_getevents(2) 的 timeout 机制。</p> </li> </ul> <h3 id="io_uring-用户态库-liburing">io_uring 用户态库 liburing</h3> <p>为了简化使用，原作者 Jens 开发了一套 liburing 库，用户无需了解诸多 io_uring 细节便可以使用起来，如无需关心 memory barrier，以及 ring buffer 的管理等。相关接口在头文件 /usr/include/liburing.h 中定义。</p> <p>Alibaba Cloud Linux 2 LTS 提供了 liburing 和 liburing-devel 包供用户安装。</p> <div class="language-sh highlighter-rouge"><div class="highlight"><pre class="highlight"><code>sodo yum <span class="nb">install </span>liburing liburing-devel
</code></pre></div></div> <p>基于 liburing 的一个 helloworld 示例如下：</p> <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cp">#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdio.h>
#include <liburing.h>
#define ENTRIES     4
</span><span class="kt">int</span> <span class="nf">main</span><span class="p">(</span><span class="kt">int</span> <span class="n">argc</span><span class="p">,</span> <span class="kt">char</span> <span class="o">*</span><span class="n">argv</span><span class="p">[])</span>
<span class="p">&#123;</span>
    <span class="k">struct</span> <span class="n">io_uring</span> <span class="n">ring</span><span class="p">;</span>
    <span class="k">struct</span> <span class="n">io_uring_sqe</span> <span class="o">*</span><span class="n">sqe</span><span class="p">;</span>
    <span class="k">struct</span> <span class="n">io_uring_cqe</span> <span class="o">*</span><span class="n">cqe</span><span class="p">;</span>
    <span class="k">struct</span> <span class="n">iovec</span> <span class="n">iov</span> <span class="o">=</span> <span class="p">&#123;</span>
        <span class="p">.</span><span class="n">iov_base</span> <span class="o">=</span> <span class="s">"Hello World"</span><span class="p">,</span>
        <span class="p">.</span><span class="n">iov_len</span> <span class="o">=</span> <span class="n">strlen</span><span class="p">(</span><span class="s">"Hello World"</span><span class="p">),</span>
    <span class="p">&#125;;</span>
    <span class="kt">int</span> <span class="n">fd</span><span class="p">,</span> <span class="n">ret</span><span class="p">;</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">argc</span> <span class="o">!=</span> <span class="mi">2</span><span class="p">)</span> <span class="p">&#123;</span>
        <span class="n">printf</span><span class="p">(</span><span class="s">"%s: <testfile></span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">argv</span><span class="p">[</span><span class="mi">0</span><span class="p">]);</span>
        <span class="k">return</span> <span class="mi">1</span><span class="p">;</span>
    <span class="p">&#125;</span>
    <span class="cm">/* setup io_uring and do mmap */</span>
    <span class="n">ret</span> <span class="o">=</span> <span class="n">io_uring_queue_init</span><span class="p">(</span><span class="n">ENTRIES</span><span class="p">,</span> <span class="o">&</span><span class="n">ring</span><span class="p">,</span> <span class="mi">0</span><span class="p">);</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">ret</span> <span class="o"><</span> <span class="mi">0</span><span class="p">)</span> <span class="p">&#123;</span>
        <span class="n">printf</span><span class="p">(</span><span class="s">"io_uring_queue_init: %s</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">strerror</span><span class="p">(</span><span class="o">-</span><span class="n">ret</span><span class="p">));</span>
        <span class="k">return</span> <span class="mi">1</span><span class="p">;</span>
    <span class="p">&#125;</span>
    <span class="n">fd</span> <span class="o">=</span> <span class="n">open</span><span class="p">(</span><span class="s">"testfile"</span><span class="p">,</span> <span class="n">O_WRONLY</span> <span class="o">|</span> <span class="n">O_CREAT</span><span class="p">);</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">fd</span> <span class="o"><</span> <span class="mi">0</span><span class="p">)</span> <span class="p">&#123;</span>
        <span class="n">printf</span><span class="p">(</span><span class="s">"open failed</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
        <span class="n">ret</span> <span class="o">=</span> <span class="mi">1</span><span class="p">;</span>
        <span class="k">goto</span> <span class="n">exit</span><span class="p">;</span>
    <span class="p">&#125;</span>
    <span class="cm">/* get an sqe and fill in a WRITEV operation */</span>
    <span class="n">sqe</span> <span class="o">=</span> <span class="n">io_uring_get_sqe</span><span class="p">(</span><span class="o">&</span><span class="n">ring</span><span class="p">);</span>
    <span class="k">if</span> <span class="p">(</span><span class="o">!</span><span class="n">sqe</span><span class="p">)</span> <span class="p">&#123;</span>
        <span class="n">printf</span><span class="p">(</span><span class="s">"io_uring_get_sqe failed</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
        <span class="n">ret</span> <span class="o">=</span> <span class="mi">1</span><span class="p">;</span>
        <span class="k">goto</span> <span class="n">out</span><span class="p">;</span>
    <span class="p">&#125;</span>
    <span class="n">io_uring_prep_writev</span><span class="p">(</span><span class="n">sqe</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="o">&</span><span class="n">iov</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">);</span>
    <span class="cm">/* tell the kernel we have an sqe ready for consumption */</span>
    <span class="n">ret</span> <span class="o">=</span> <span class="n">io_uring_submit</span><span class="p">(</span><span class="o">&</span><span class="n">ring</span><span class="p">);</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">ret</span> <span class="o"><</span> <span class="mi">0</span><span class="p">)</span> <span class="p">&#123;</span>
        <span class="n">printf</span><span class="p">(</span><span class="s">"io_uring_submit: %s</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">strerror</span><span class="p">(</span><span class="o">-</span><span class="n">ret</span><span class="p">));</span>
        <span class="k">goto</span> <span class="n">out</span><span class="p">;</span>
    <span class="p">&#125;</span>
    <span class="cm">/* wait for the sqe to complete */</span>
    <span class="n">ret</span> <span class="o">=</span> <span class="n">io_uring_wait_cqe</span><span class="p">(</span><span class="o">&</span><span class="n">ring</span><span class="p">,</span> <span class="o">&</span><span class="n">cqe</span><span class="p">);</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">ret</span> <span class="o"><</span> <span class="mi">0</span><span class="p">)</span> <span class="p">&#123;</span>
        <span class="n">printf</span><span class="p">(</span><span class="s">"io_uring_wait_cqe: %s</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span> <span class="n">strerror</span><span class="p">(</span><span class="o">-</span><span class="n">ret</span><span class="p">));</span>
        <span class="k">goto</span> <span class="n">out</span><span class="p">;</span>
    <span class="p">&#125;</span>
    <span class="cm">/* read and process cqe event */</span>
    <span class="n">io_uring_cqe_seen</span><span class="p">(</span><span class="o">&</span><span class="n">ring</span><span class="p">,</span> <span class="n">cqe</span><span class="p">);</span>
<span class="nl">out:</span>
    <span class="n">close</span><span class="p">(</span><span class="n">fd</span><span class="p">);</span>
<span class="nl">exit:</span>
    <span class="cm">/* tear down */</span>
    <span class="n">io_uring_queue_exit</span><span class="p">(</span><span class="o">&</span><span class="n">ring</span><span class="p">);</span>
    <span class="k">return</span> <span class="n">ret</span><span class="p">;</span>
<span class="p">&#125;</span>
</code></pre></div></div> <p>更多的示例可参考：</p> <p><a href="https://github.com/axboe/liburing/tree/master/examples/">https://github.com/axboe/liburing/tree/master/examples/</a> <a href="https://github.com/axboe/liburing/tree/master/test">https://github.com/axboe/liburing/tree/master/test</a></p> <h2 id="io_uring-高级特性">io_uring 高级特性</h2> <h3 id="polled-io">Polled IO</h3> <p>IORING_SETUP_IOPOLL，与非 polling 模式等待硬件中断唤醒不同，内核将采用 polling 模式不断轮询硬件以确认 IO 请求是否已经完成，这在追求低延时和高 IOPS 的应用场景非常有用。</p> <h3 id="kernel-side-polling">Kernel Side Polling</h3> <p>IORING_SETUP_SQPOLL，当前应用更新 SQ ring 并填充一个新的 sqe，内核线程 sqthread 会自动完成提交，这样应用无需每次调用 io_uring_enter() 系统调用来提交 IO。应用可通过 IORING_SETUP_SQ_AFF 和 sq_thread_cpu 绑定特定的 CPU。 同时，为了节省无 IO 场景的 CPU 开销，该内核线程会在一段时间空闲后自动睡眠。应用在下发新的 IO 时，通过 IORING_ENTER_SQ_WAKEUP 唤醒该内核线程，该操作在 liburing 中都已封装完成。</p> <h3 id="fixed-files">Fixed Files</h3> <p>IORING_REGISTER_FILES / IORING_REGISTER_FILES_UPDATE / IORING_UNREGISTER_FILES，通过 io_uring_register() 系统调用提前注册一组 file，缓解每次 IO 操作因 fget() / fput() 带来的开销。</p> <h3 id="fixed-buffers">Fixed Buffers</h3> <p>IORING_REGISTER_BUFFERS / IORING_UNREGISTER_BUFFERS，通过 io_uring_register() 系统调用注册一组固定的 IO buffers，当应用重用这些 IO buffers 时，只需要 map / unmap 一次即可，而不是每次 IO 都要去做，减少get_user_pages() / put_page() 带来的开销。</p> <h3 id="linked-sqe">Linked SQE</h3> <p>IOSQE_IO_LINK，建立 sqe 序列之间的关联，这在诸如 copy 之类的操作中非常有用。使用 linked sqe 后，copy 操作的写请求链接在读请求之后，应用程序无需等待读请求数据返回后再下发写请求，而是共享了同一个 buffer，避免了上下文切换的开销。</p> <h2 id="社区工作">社区工作</h2> <p>阿里云操作系统团队在 backport io_uring 特性到 Alibaba Cloud Linux 2 的过程中，进一步优化性能，并加固 io_uring 的稳定性，相关工作以补丁的形式回馈到社区。</p> <h3 id="性能优化">性能优化</h3> <ul> <li> <p>engines/io_uring: delete fio_option_is_set() calls when submitting sqes fio io_uring 提交 IO 性能提升 30%。</p> </li> <li> <p>__io_uring_get_cqe: eliminate unnecessary io_uring_enter() syscalls 在某些场景下，减少 50% 的 io_uring_enter() 系统调用开销。</p> </li> <li> <p>ext4: start to support iopoll method</p> </li> <li> <p>io_uring: io_uring_enter(2) don’t poll while SETUP_IOPOLL|SETUP_SQPOLL enabled 能带来 13% 的性能提升，同时减少 20% 的 CPU 开销。</p> </li> </ul> <h3 id="代码优化和特性重构">代码优化和特性重构</h3> <ul> <li>io_uring: cleanup io_alloc_async_ctx()</li> <li>io_uring: refactor file register/unregister/update handling 重构 file register/unregister/update 特性，能更好地处理大量文件场景。</li> <li>io_uring: do not always copy iovec in io_req_map_rw()</li> <li>io_uring: avoid whole io_wq_work copy for requests completed inline</li> <li>io_uring: avoid unnecessary io_wq_work copy for fast poll feature</li> <li>e697deed834d io_uring: check file O_NONBLOCK state for accept</li> </ul> <h3 id="bugfix">BugFix</h3> <ul> <li>io_uring: fix __io_iopoll_check deadlock in io_sq_thread</li> <li>io_uring: fix poll_list race for SETUP_IOPOLL|SETUP_SQPOLL</li> <li>io_uring: restore req->work when canceling poll request</li> <li>io_uring: only restore req->work for req that needs do completion</li> <li>io_uring: use cond_resched() in io_ring_ctx_wait_and_kill()</li> <li>io_uring: fix mismatched finish_wait() calls in io_uring_cancel_files()</li> <li>io_uring: handle -EFAULT properly in io_uring_setup()</li> <li>io_uring: reset -EBUSY error when io sq thread is waken up</li> <li>io_uring: don’t submit sqes when ctx->refs is dying</li> <li>io_uring: fix io_kiocb.flags modification race in IOPOLL mode</li> <li>io_uring: don’t fail links for EAGAIN error in IOPOLL mode</li> <li>io_uring: add memory barrier to synchronize io_kiocb’s result and iopoll_completed</li> <li>io_uring: fix possible race condition against REQ_F_NEED_CLEANUP</li> </ul>   
</div>
            