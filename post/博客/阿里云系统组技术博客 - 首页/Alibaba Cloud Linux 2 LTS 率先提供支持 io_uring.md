
---
title: 'Alibaba Cloud Linux 2 LTS 率先提供支持 io_uring'
categories: 
    - 博客
    - 阿里云系统组技术博客 - 首页
author: 阿里云系统组技术博客 - 首页
comments: false
date: Sun, 31 May 2020 16:00:00 GMT
thumbnail: 'https://kernel.taobao.org//2020/06/io_uring-in-Alibaba-Cloud-Linux-2-LTS/io_uring_diag.png'
---

<div>   
<h1 id="概述">概述</h1> <p>Alibaba Cloud Linux 2 是阿里云操作系统团队基于开源 Linux 4.19 LTS 版本打造的一款针对云应用场景的下一代 Linux OS 发行版。在首次推出一年后，阿里云操作系统团队对外正式发布了Alibaba Cloud Linux 2 LTS 版本。LTS 版本的发布是一个重要的里程碑，标志着阿里云操作系统团队将为 Alibaba Cloud Linux 2 提供长期技术支持、稳定的更新和更好的服务，为 Alibaba Cloud Linux 2 的客户提供更多保障。</p> <p>Alibaba Cloud Linux 2 LTS 版本，其中一个重要的特性更新是提供了对 io_uring 的支持。io_uring 是由 block 维护者 Jens Axboe 开发的新型异步 IO 框架。io_uring 在 2019 年 1 月初提出，到 2019 年 3 月初合并到 Linux 内核主线，仅用短短的 2 个月时间就合入了 Linux v5.1，充分表明了社区对该框架的积极态度。当前社区发展非常火热，很多主流应用都开始提供对 io_uring 的支持，如 Node.js，Nginx，PostgreSQL，RocksDB，QEMU，spdk，等等。</p> <p>Alibaba Cloud Linux 2 LTS 版本的 io_uring 功能同步自 Linux 内核主线 v5.4，测试过程中发现的稳定性和性能问题已得到修复，相关补丁也已被接收合入到社区上游，并持续对其进行维护和支持。</p> <h1 id="linux-io-发展史">Linux IO 发展史</h1> <p>Linux 中有很多方式来执行文件 IO 操作。最初的 IO 系统调用需要追溯到 read(2) 和write(2)，后来发展为增加 offset 参数的 pread(2) 和 pwrite(2)，以及基于 vector 的版本 preadv(2) 和 pwritev(2)，再扩展成允许修改 flags 的版本 preadv2(2) 和 pwritev2(2)。这些系统调用看上去多种多样，但有一个共同的特性就是同步，即系统调用需要在数据读取完成或写入完成才返回。应某些应用场景的诉求，异步 IO 接口应势而生。POSIX 对应的接口为 aio_read(3)和 aio_write(3)，但由于性能不好实际使用很少。</p> <p>目前异步 IO 使用最多的是 Linux Native 异步 IO，即我们通常称的 aio。不幸的是，其同样有着诸多约束：</p> <ul> <li>最大的限制无疑是仅支持 direct io。而 O_DIRECT 存在 bypass 缓存和 size 对齐等限制，直接影响了 aio 在很多场景的使用。而针对 buffered io，其表现为同步。</li> <li>即使满足了所有异步 IO 的约束，有时候还是可能会被阻塞。例如，等待元数据 IO，或者等待 request 的分配等。</li> <li>存在额外的拷贝开销，每个 IO 提交需要拷贝 64+8 字节，每个 IO 完成需要拷贝 32 字节，这 104 字节的拷贝在大量小 IO 的场景下影响很可观。同时，需要非常小心地使用完成事件以避免丢事件。IO 需要至少 2 个系统调用（submit + wait-for-completion)，这在 spectre/meltdown 开启的前提下性能下降非常严重。</li> </ul> <h1 id="io_uring-原理介绍">io_uring 原理介绍</h1> <p>为了从根本上解决当前 aio 存在的问题和约束，io_uring 全新从零开始设计的异步 IO 框架。其设计的主要目标如下：</p> <ul> <li>简单易用，方便应用集成。</li> <li>可扩展，不仅仅为 block IO 使用，同样可以用于网络/非 block IO。</li> <li>特性丰富，满足所有应用，如 buffered io。</li> <li>高效，尤其是针对大部分场景的 512 字节或 4K IO。</li> <li>可伸缩，满足峰值场景的性能需要。</li> </ul> <p>io_uring 为了避免在提交和完成事件中的内存拷贝，设计了一对共享的 ring buffer 用于应用和内核之间的通信。其中，针对提交队列（SQ），应用是 IO 提交的生产者（producer），内核是消费者（consumer）；反过来，针对完成队列（CQ），内核是完成事件的生产者，应用是消费者。 <img src="https://kernel.taobao.org//2020/06/io_uring-in-Alibaba-Cloud-Linux-2-LTS/io_uring_diag.png" alt="image.png" referrerpolicy="no-referrer"></p> <h2 id="io_uring-系统调用">io_uring 系统调用</h2> <p>io_uring 一共提供了 3 个系统调用：io_uring_setup()，io_uring_enter()，以及io_uring_register()，位于 fs/io_uring.c。</p> <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cm">/**
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
</code></pre></div></div> <p>Alibaba Cloud Linux 2 LTS 版本支持的异步操作如下：</p> <ul> <li>IORING_OP_NOP 仅产生一个完成事件，除此之外没有任何操作。</li> <li>IORING_OP_READV / IORING_OP_WRITEV 提交 readv() / writev() 操作，大多数场景最核心的操作。</li> <li>IORING_OP_READ_FIXED / IORING_OP_WRITE_FIXED 使用已注册的 buffer 来提交 IO 操作，由于这些 buffer 已经完成映射，可以降低系统调用的开销。</li> <li>IORING_OP_FSYNC 下发 fsync() 调用。</li> <li>IORING_OP_POLL_ADD / IORING_OP_POLL_REMOVE 使用 IORING_OP_POLL_ADD 可对一组文件描述符 (file descriptors) 执行 poll() 操作；可以使用 IORING_OP_POLL_REMOVE 显式地取消 poll()。这种方式可以用来异步地监控一组文件描述符。</li> <li>IORING_OP_SYNC_FILE_RANGE 执行 sync_file_range() 调用，是对 fsync() 的一个增强。</li> <li>IORING_OP_SENDMSG / IORING_OP_RECVMSG 在 sendmsg() 和 recvmsg() 基础上，提供异步收发网络包功能。</li> <li>IORING_OP_TIMEOUT 用户态程序等待 IO 完成事件时，可以通过 IORING_OP_TIMEOUT 设置一个超时时间，类似 io_getevents(2) 的 timeout 机制。</li> </ul> <h2 id="io_uring-用户态库-liburing">io_uring 用户态库 liburing</h2> <p>为了简化使用，原作者 Jens 开发了一套 liburing 库，用户无需了解诸多 io_uring 细节便可以使用起来，如无需关心 memory barrier，以及 ring buffer 的管理等。相关接口在头文件 /usr/include/liburing.h 中定义。 Alibaba Cloud Linux 2 LTS 提供了 liburing 和 liburing-devel 包供用户安装。</p> <div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code>sodo yum <span class="nb">install </span>liburing liburing-devel
</code></pre></div></div> <p>基于 liburing 的一个简单的示例如下：</p> <div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cp">#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdio.h>
#include <liburing.h>
</span>
<span class="cp">#define ENTRIES4
</span>
<span class="kt">int</span> <span class="nf">main</span><span class="p">(</span><span class="kt">int</span> <span class="n">argc</span><span class="p">,</span> <span class="kt">char</span> <span class="o">*</span><span class="n">argv</span><span class="p">[])</span>
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
<span class="k">while</span> <span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="p">&#123;</span>
<span class="n">io_uring_peek_cqe</span><span class="p">(</span><span class="o">&</span><span class="n">ring</span><span class="p">,</span> <span class="o">&</span><span class="n">cqe</span><span class="p">);</span>
<span class="k">if</span> <span class="p">(</span><span class="o">!</span><span class="n">cqe</span><span class="p">)</span> <span class="p">&#123;</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"Not completed, waiting...</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="n">usleep</span><span class="p">(</span><span class="mi">1</span><span class="p">);</span>
<span class="p">&#125;</span> <span class="k">else</span> <span class="p">&#123;</span>
<span class="n">printf</span><span class="p">(</span><span class="s">"Completed</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="k">break</span><span class="p">;</span>
<span class="p">&#125;</span>
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
</code></pre></div></div> <p>更多的示例可参考： https://github.com/axboe/liburing/tree/master/examples/ https://github.com/axboe/liburing/tree/master/test</p> <h2 id="使用-fio-io_uring-测试性能">使用 fio io_uring 测试性能</h2> <p>Alibaba Cloud Linux 2 LTS 版本在 experimental 源中提供支持 io_uring 的 fio-3.17，用户可通过 ioengine=io_uring 使用 fio io_uring 进行性能测试。</p> <div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nb">sudo </span>yum <span class="nb">install</span> <span class="nt">-y</span> alinux-release-experimentals
<span class="nb">sudo </span>yum <span class="nb">install</span> <span class="nt">-y</span> fio-3.17
</code></pre></div></div> <p>fio 示例：</p> <div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code>fio <span class="nt">-name</span><span class="o">=</span>fiotest <span class="nt">-filename</span><span class="o">=</span>/mnt/vdd/testfile <span class="nt">-iodepth</span><span class="o">=</span>128 <span class="nt">-thread</span> <span class="nt">-rw</span><span class="o">=</span>randread <span class="nt">-ioengine</span><span class="o">=</span>io_uring <span class="nt">-sqthread_poll</span><span class="o">=</span>1 <span class="nt">-direct</span><span class="o">=</span>1 <span class="nt">-bs</span><span class="o">=</span>4k <span class="nt">-size</span><span class="o">=</span>10G <span class="nt">-numjobs</span><span class="o">=</span>1 <span class="nt">-runtime</span><span class="o">=</span>600 <span class="nt">-group_reporting</span>
</code></pre></div></div> <h1 id="io_uring-高级特性">io_uring 高级特性</h1> <h2 id="fixed-files-and-buffers">Fixed Files and Buffers</h2> <p>IORING_REGISTER_FILES / IORING_UNREGISTER_FILES，通过 io_uring_register() 系统调用提前注册一组 file，缓解每次 IO 操作因 fget() / fput() 带来的开销。 IORING_REGISTER_BUFFERS / IORING_UNREGISTER_BUFFERS，通过 io_uring_register() 系统调用注册一组固定的 IO buffers，当应用重用这些 IO buffers 时，只需要 map / unmap 一次即可，而不是每次 IO 都要去做，减少get_user_pages() / put_page() 带来的开销。</p> <h2 id="polled-io">Polled IO</h2> <p>IORING_SETUP_IOPOLL，与非 polling 模式等待硬件中断唤醒不同，内核将采用 polling 模式不断轮询硬件以确认 IO 请求是否已经完成，这在追求低延时和高 IOPS 的应用场景非常有用。</p> <h2 id="kernel-side-polling">Kernel Side Polling</h2> <p>IORING_SETUP_SQPOLL，当前应用更新 SQ ring 并填充一个新的 sqe，内核线程 sqthread 会自动完成提交，这样应用无需每次调用 io_uring_enter() 系统调用来提交 IO。应用可通过 IORING_SETUP_SQ_AFF 和 sq_thread_cpu 绑定特定的 CPU。 同时，为了节省无 IO 场景的 CPU 开销，该内核线程会在一段时间空闲后自动睡眠。应用在下发新的 IO 时，通过 IORING_ENTER_SQ_WAKEUP 唤醒该内核线程，该操作在 liburing 中都已封装完成。</p> <h1 id="io_uring-性能评测">io_uring 性能评测</h1> <h2 id="alibaba-cloud-linux-2-lts-评测">Alibaba Cloud Linux 2 LTS 评测</h2> <p>我们基于 Alibaba Cloud Linux 2 LTS 的 fio 测试评估数据如下：</p> <blockquote> <p>测试环境：ecs.i2.2xlarge，8 vCPU 64 GiB，I2 本地存储 1788 GiB。</p> </blockquote> <ul> <li> <p>4k 顺序读 <img src="https://kernel.taobao.org//2020/06/io_uring-in-Alibaba-Cloud-Linux-2-LTS/seq_read.png" alt="image.png" referrerpolicy="no-referrer"></p> </li> <li> <p>4k 顺序写 <img src="https://kernel.taobao.org//2020/06/io_uring-in-Alibaba-Cloud-Linux-2-LTS/seq_write.png" alt="image.png" referrerpolicy="no-referrer"></p> </li> <li> <p>4k 随机读 <img src="https://kernel.taobao.org//2020/06/io_uring-in-Alibaba-Cloud-Linux-2-LTS/rand_read.png" alt="image.png" referrerpolicy="no-referrer"></p> </li> <li> <p>4k 随机写 <img src="https://kernel.taobao.org//2020/06/io_uring-in-Alibaba-Cloud-Linux-2-LTS/rand_write.png" alt="image.png" referrerpolicy="no-referrer"></p> </li> </ul> <p>从上述测试数据可以看出：</p> <ul> <li>默认模式下，略微提升。</li> <li>开启 sqthread_poll 后，顺序读写提升很明显，达到 160% ~ 170%；随机读写提升 30% ~ 150%。</li> </ul> <h2 id="社区性能数据">社区性能数据</h2> <p>原作者 Jens 在 PATCHSET v5 中有分别对比 io_uring vs libaio，io_uring vs spdk 的 4k 随机读数据： https://lore.kernel.org/linux-block/20190116175003.17880-1-axboe@kernel.dk/</p> <p>测试结果如下：</p> <ul> <li>非 polling 模式，io_uring 相比 libaio 有略微提升。</li> <li>在 polling 模式下，io_uring 与 spdk 接近，甚至在 queue depth 较高时性能更好，完胜 libaio。</li> </ul> <h1 id="社区工作">社区工作</h1> <p>阿里云操作系统团队在 backport io_uring 特性到 Alibaba Cloud Linux 2 的过程中，进一步加固 io_uring 的稳定性，同时优化性能，相关工作以补丁的形式回馈到社区。</p> <h2 id="bugfix">BugFix</h2> <ul> <li>io_uring: fix __io_iopoll_check deadlock in io_sq_thread</li> <li>io_uring: fix poll_list race for SETUP_IOPOLL|SETUP_SQPOLL</li> <li>io_uring: restore req->work when canceling poll request</li> <li>io_uring: only restore req->work for req that needs do completion</li> <li>io_uring: use cond_resched() in io_ring_ctx_wait_and_kill()</li> <li>io_uring: fix mismatched finish_wait() calls in io_uring_cancel_files()</li> <li>io_uring: handle -EFAULT properly in io_uring_setup()</li> <li>io_uring: reset -EBUSY error when io sq thread is waken up</li> </ul> <h2 id="性能优化">性能优化</h2> <ul> <li>engines/io_uring: delete fio_option_is_set() calls when submitting sqes<br> fio io_uring 提交 IO 性能提升 30%。</li> <li>__io_uring_get_cqe: eliminate unnecessary io_uring_enter() syscalls<br> 在某些场景下，减少 50% 的 io_uring_enter() 系统调用开销。</li> <li>ext4: start to support iopoll method</li> <li>io_uring: io_uring_enter(2) don’t poll while SETUP_IOPOLL|SETUP_SQPOLL enabled<br> 能带来 13% 的性能提升，同时减少 20% 的 CPU 开销。</li> </ul> <h2 id="代码优化和特性重构">代码优化和特性重构</h2> <ul> <li>io_uring: cleanup io_alloc_async_ctx()</li> <li>io_uring: refactor file register/unregister/update handling & io_uring: initialize fixed_file_data lock<br> 重构 file register/unregister/update 特性，能更好地处理大量文件场景。</li> <li>io_uring: do not always copy iovec in io_req_map_rw()</li> </ul>   
</div>
            