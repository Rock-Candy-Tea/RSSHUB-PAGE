
---
title: '并行编程OpenMP在ARMv8架构上的应用'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b71d62fa51ae45bcbdc05384ba305804~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 19:20:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b71d62fa51ae45bcbdc05384ba305804~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.OpenMP简介</h2>
<p>OpenMP是一种用于共享内存并行系统的多线程程序设计方案，支持的编程语言包括C、C++和Fortran。OpenMP提供了对并行算法的高层抽象描述，特别适合在多核CPU机器上的并行程序设计。编译器根据程序中添加的pragma指令，自动将程序并行处理，使用OpenMP降低了并行编程的难度和复杂度。当编译器不支持OpenMP时，程序会退化成普通（串行）程序。程序中已有的OpenMP指令不会影响程序的正常编译运行。</p>
<p>OpenMP采用fork-join的执行模式。开始的时候只存在一个主线程，当需要进行并行计算的时候，派生出若干个分支线程来执行并行任务。当并行代码执行完成之后，分支线程会合，并把控制流程交给单独的主线程。</p>
<p>一个典型的fork-join执行模型的示意图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b71d62fa51ae45bcbdc05384ba305804~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">2.开发测试环境</h2>
<p>出于对ARM多核处理器的研究，使用OpenMP模型对一款8核CPU进行简单的测试。由于现在没有开发板实物，所以我就用QEMU模拟了一个8核contex-a72、内存512M的CPU，怎么使用QEMU模拟我会在下一篇文章中讲诉。</p>
<p>准备：</p>
<ul>
<li>Ubuntu18.04操作系统（不是虚拟机）</li>
<li>搭建好的QEMU环境</li>
<li>使用apt-get下载交叉编译器aarch64-linux-gnu-</li>
</ul>
<h2 data-id="heading-2">3.编写OpenMP测试程序</h2>
<p>OpenMP遍译制导指令以#pragma omp 开始，后边跟具体的功能指令，格式如：#pragma omp 指令[子句[,子句] …]。常用的功能指令如下：</p>
<ul>
<li>parallel：用在一个结构块之前，表示这段代码将被多个线程并行执行；</li>
<li>for：用于for循环语句之前，表示将循环计算任务分配到多个线程中并行执行，以实现任务分担，必须由编程人员自己保证每次循环之间无数据相关性；</li>
<li>parallel for：parallel和for指令的结合，也是用在for循环语句之前，表示for循环体的代码将被多个线程并行执行，它同时具有并行域的产生和任务分担两个功能；</li>
<li>sections：用在可被并行执行的代码段之前，用于实现多个结构块语句的任务分担，可并行执行的代码段各自用section指令标出（注意区分sections和section）；</li>
<li>parallel sections：parallel和sections两个语句的结合，类似于parallel for；</li>
<li>single：用在并行域内，表示一段只被单个线程执行的代码；</li>
<li>critical：用在一段代码临界区之前，保证每次只有一个OpenMP线程进入；</li>
<li>flush：保证各个OpenMP线程的数据影像的一致性；</li>
<li>barrier：用于并行域内代码的线程同步，线程执行到barrier时要停下等待，直到所有线程都执行到barrier时才继续往下执行；</li>
<li>atomic：用于指定一个数据操作需要原子性地完成；</li>
<li>master：用于指定一段代码由主线程执行；</li>
<li>threadprivate：用于指定一个或多个变量是线程专用，后面会解释线程专有和私有的区别。</li>
</ul>
<p>还有一些经常用到的API函数</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/271f99c2d3f148f6a3c1f772ea643807~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.编写测试代码OpenMPTest.c</strong></p>
<pre><code class="copyable">#include<stdio.h>  
#include"omp.h"  
void main()  
&#123;  
#pragma omp parallel for num_threads(8)  
    for (int i = 0; i < 8; i++)  
    &#123;  
        printf("OpenMP Test, 线程编号为: %d\n", omp_get_thread_num());  
    &#125;  
    return 0;
&#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.交叉编译OpenMPTest.c</strong></p>
<pre><code class="copyable">aarch-linux-gnu-gcc OpenMPTest.c -o OpenMPTest
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.可执行文件OpenMPTest挂载到QEMU中Linux文件系统中</strong></p>
<pre><code class="copyable">mount -o loop /home/xt/rootfs.ext3 /home/xt/tmpfs/
cp dhry.elf /home/xt/tmpfs/
umount /home/xt/tmpfs/
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.执行QEMU启动代码</strong></p>
<pre><code class="copyable">qemu-system-aarch64 \
        -machine virt \
        -cpu cortex-a72 \
        -nographic \
        -m 512 \
        -smp 8 \
        -kernel /home/xt/linux-5.12.9/arch/arm64/boot/Image \
        -initrd /home/xt/rootfs.ext3 \
        -append "root=/dev/ram0 rdinit=/linuxrc console=ttyAMA0"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果如下图所示：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0069a8e88a8a4a409ff83d9cf1a11830~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2019-11-15 105600.jpg" loading="lazy" referrerpolicy="no-referrer">
<strong>5.在模拟地ARM环境中执行已经挂载地可执行文件，./xxx</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06830ab030ef4dbc892d6aef3efb3a38~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行完成！！！！！！！！！！！！！！！！！！</p>
<h2 data-id="heading-3">参考</h2>
<p><a href="https://link.juejin.cn/?target=url" target="_blank" title="url" ref="nofollow noopener noreferrer">blog.csdn.net/u011808673/…</a>
<a href="https://link.juejin.cn/?target=url" target="_blank" title="url" ref="nofollow noopener noreferrer">www.pianshen.com/article/346…</a>
<a href="https://link.juejin.cn/?target=url" target="_blank" title="url" ref="nofollow noopener noreferrer">blog.csdn.net/Tronlong/ar…</a></p></div>  
</div>
            