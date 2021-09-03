
---
title: '10个必须了解的Linux系统进程'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210831/9330ab9fee7905b8bd56a41f00e683f9.png'
author: Dockone
comments: false
date: 2021-09-03 09:07:42
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210831/9330ab9fee7905b8bd56a41f00e683f9.png'
---

<div>   
<br>当我们习惯性的执行ps命令后会看到很多“奇奇怪怪”的进程，而这些进程大部门都是系统的内核进程。很多同学对之了解的甚少，因此今天就为大家整理一篇入门级的系统进程介绍，希望能够帮助大家对操作系统进程的理解。<br>
<br>在日常运维工作中，经常会看到一些奇怪的系统进程占用资源比较高。而且总是会听到业务线同学询问“xxx这个是啥进程啊？咋开启了这么多？”<br>
<br>而这些系统级的内核进程都是会用中括号括起来的，它们会执行一些系统的辅助功能（如将缓存写入磁盘），无括号的进程都是用户们执行的进程（如PHP、Nginx等）。<br>
<br>如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210831/9330ab9fee7905b8bd56a41f00e683f9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210831/9330ab9fee7905b8bd56a41f00e683f9.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
下面就为大家普及10个比较常见的系统进程：<br>
<h4>kswapd0</h4>系统每过一定时间就会唤醒kswapd，看看内存是否紧张，如果不紧张，则睡眠，在kswapd中，有2个阀值，pages_hige和pages_low，当空闲内存页的数量低于pages_low的时候，kswapd进程就会扫描内存并且每次释放出32个free pages，直到free page的数量到达pages_high。<br>
<h4>kjournald</h4>journal：记录所有文件系统上的元数据改变，最慢的一种模式。<br>
<br>ordered：默认使用的模式,只记录文件系统改变的元数据，并在改变之前记录日志。<br>
<br>writeback：最快的一种模式,同样只记录修改过的元数据，依赖标准文件系统写进程将数据写到硬盘<br>
<h4>pdflush</h4>pdflush用于将内存中的内容和文件系统进行同步。<br>
<br><blockquote><br>比如说：当一个文件在内存中进行修改，pdflush负责将它写回硬盘。每当内存中的垃圾页（dirty page）超过10%的时候，pdflush就会将这些页面备份回硬盘。这个比率是可调节的，通过/etc/sysctl.conf中的 vm.dirty_background_ratio项默认值为10也可以。</blockquote><h4>kthreadd</h4>这种内核线程只有一个，它的作用是管理调度其它的内核线程。<br>
<br><blockquote><br>它在内核初始化的时候被创建，会循环运行一个叫做kthreadd的函数，该函数的作用是运行kthread_create_list全局链表中维护的kthread。可以调用kthread_create创建一个kthread，它会被加入到kthread_create_list链表中，同时kthread_create会weak up kthreadd_task。kthreadd在执行kthread会调用老的接口——kernel_thread运行一个名叫“kthread”的内核线程去运行创建的kthread，被执行过的kthread会从kthread_create_list链表中删除，并且kthreadd会不断调用scheduler 让出CPU。这个线程不能关闭。</blockquote><h4>migration</h4>这种内核线程共有32个，从migration/0到migration/31，每个处理器核对应一个migration内核线程，主要作用是作为相应CPU核的迁移进程，用来执行进程迁移操作，内核中的函数是migration_thread()。<br>
<br><blockquote><br>属于2.6内核的负载平衡系统，该进程在系统启动时自动加载（每个CPU一个），并将自己设为SCHED_FIFO的实时进程，然后检查runqueue::migration_queue中是否有请求等待处理，如果没有，就在TASK_INTERRUPTIBLE中休眠，直至被唤醒后再次检查。migration_thread() 仅仅是一个CPU绑定以及CPU电源管理等功能的一个接口。这个线程是调度系统的重要组成部分。</blockquote><h4>watchdog</h4>这种内核线程共有32个，从watchdog/0到watchdog/31，每个处理器核对应一个watchdog内核线程，watchdog用于监视系统的运行，在系统出现故障时自动重新启动系统，包括一个内核watchdog module和一个用户空间的watchdog程序。<br>
<br><blockquote><br>在Linux内核下，watchdog的基本工作原理是：当watchdog启动后（即/dev/watchdog设备被打开后），如果在某一设定的时间间隔（1分钟）内/dev/watchdog没有被执行写操作, 硬件watchdog电路或软件定时器就会重新启动系统，每次写操作会导致重新设定定时器。</blockquote><h4>events</h4>这种内核线程共有32个，从events/0到events/31，每个处理器核对应一个 events内核线程。用来处理内核事件很多软硬件事件（比如断电，文件变更）被转换为events，并分发给对相应事件感兴趣的线程进行响应。<br>
<h4>kblockd</h4>这种内核线程共有32个，从kblockd/0到kblockd/31，每个处理器核对应一个kblockd内核线程。用于管理系统的块设备，它会周期地激活系统内的块设备驱动。如果拥有块设备，那么这些线程就不能被去掉。<br>
<h4>aio</h4>这种内核线程共有32个，从aio/0到aio/31，每个处理器核对应一个aio内核线程，代替用户进程管理I/O，用以支持用户态的AIO（异步I/O），不应该被关闭。<br>
<h4>rpciod</h4>这种内核线程共有32个，从rpciod/0到rpciod/31，每个处理器核对应一个rpciod内核线程，主要作用是作为远过程调用服务的守护进程，用于从客户端启动I/O服务，通常启动NFS服务时要用到它。<br>
<h4>总结</h4>进程是操作系统上非常重要的概念，所有系统上面跑的数据都会以进程的类型存在。在Linux系统当中：触发任何一个事件时，系统都会将它定义成为一个进程，所以，进程是Linux程序的唯一的实现方式。<br>
<br>原文链接：<a href="https://juejin.cn/post/6998328836169400351" rel="nofollow" target="_blank">https://juejin.cn/post/6998328836169400351</a>，作者：Honest1y
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            