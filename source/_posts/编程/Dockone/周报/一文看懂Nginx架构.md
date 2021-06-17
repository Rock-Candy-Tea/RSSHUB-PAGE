
---
title: '一文看懂Nginx架构'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210611/8de4fd67cad60a51f679c4b57ee1f617.png'
author: Dockone
comments: false
date: 2021-06-17 11:06:27
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210611/8de4fd67cad60a51f679c4b57ee1f617.png'
---

<div>   
<br>【编者的话】最近使用了基于Nginx的OpenResty的框架，于是对Nginx相关内容进行了学习，现将一些理解撰写成文，和大家探讨。<br>
<h3>Nginx基础架构</h3>Nginx启动后以daemon形式在后台运行，后台进程包含一个master进程和多个worker进程。如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210611/8de4fd67cad60a51f679c4b57ee1f617.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210611/8de4fd67cad60a51f679c4b57ee1f617.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Nginx是由一个master管理进程，多个worker进程处理工作的多进程模型。基础架构设计，如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210611/6673fca20c75d70c73c4f322d707748b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210611/6673fca20c75d70c73c4f322d707748b.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Master负责管理worker进程，worker进程负责处理网络事件。<strong>整个框架被设计为一种依赖事件驱动、异步、非阻塞的模式</strong>。<br>
<br>如此设计的优点有：<br>
<ul><li>可以充分利用多核机器，增强并发处理能力。</li><li>多worker间可以实现负载均衡。</li><li>Master监控并统一管理worker行为。在worker异常后，可以主动拉起worker进程，从而提升了系统的可靠性。并且由Master进程控制服务运行中的程序升级、配置项修改等操作，从而增强了整体的动态可扩展与热更的能力。</li></ul><br>
<br><h3>Master进程</h3><h4>核心逻辑</h4>Master进程的主逻辑在ngx_master_process_cycle，核心关注源码：<br>
<pre class="prettyprint">ngx_master_process_cycle(ngx_cycle_t *cycle)<br>
&#123;<br>
...<br>
ngx_start_worker_processes(cycle, ccf->worker_processes,<br>
                                    NGX_PROCESS_RESPAWN);<br>
...<br>
<br>
<br>
for ( ;; ) &#123;<br>
    if (delay) &#123;...&#125;<br>
<br>
    ngx_log_debug0(NGX_LOG_DEBUG_EVENT, cycle->log, 0, "sigsuspend");<br>
    sigsuspend(&set);<br>
<br>
    ngx_time_update();<br>
<br>
    ngx_log_debug1(NGX_LOG_DEBUG_EVENT, cycle->log, 0,<br>
                         "wake up, sigio %i", sigio);<br>
<br>
    if (ngx_reap) &#123;<br>
        ngx_reap = 0;<br>
        ngx_log_debug0(NGX_LOG_DEBUG_EVENT, cycle->log, 0, "reap children");<br>
        live = ngx_reap_children(cycle);<br>
    &#125;<br>
<br>
    if (!live && (ngx_terminate || ngx_quit)) &#123;...&#125;<br>
<br>
    if (ngx_terminate) &#123;...&#125;<br>
<br>
    if (ngx_quit) &#123;...&#125;<br>
<br>
    if (ngx_reconfigure) &#123;...&#125;<br>
<br>
    if (ngx_restart) &#123;...&#125;<br>
<br>
    if (ngx_reopen) &#123;...&#125;<br>
<br>
    if (ngx_change_binary) &#123;...&#125;<br>
<br>
    if (ngx_noaccept) &#123;<br>
        ngx_noaccept = 0;<br>
        ngx_noaccepting = 1;<br>
        ngx_signal_worker_processes(cycle,<br>
<br>
ngx_signal_value(NGX_SHUTDOWN_SIGNAL));<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
由上述代码，可以理解，master进程主要用来管理worker进程，具体包括如下4个主要功能：<br>
<ul><li>接受来自外界的信号。其中master循环中的各项标志位就对应着各种信号，如：ngx_quit代表QUIT信号，表示优雅的关闭整个服务。</li><li>向各个worker进程发送信。比如ngx_noaccept代表WINCH信号，表示所有子进程不再接受处理新的连接，由master向所有的子进程发送QUIT信号量。</li><li>监控worker进程的运行状态。比如ngx_reap代表CHILD信号，表示有子进程意外结束，这时需要监控所有子进程的运行状态，主要由ngx_reap_children完成。</li><li>当woker进程退出后（异常情况下），会自动重新启动新的woker进程。主要也是在ngx_reap_children。</li></ul><br>
<br><h4>热更</h4><strong>1）热重载-配置热更</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210611/8a5a5a3a60dbae7c7b5dd81292657781.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210611/8a5a5a3a60dbae7c7b5dd81292657781.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Nginx热更配置时，可以保持运行中平滑更新配置，具体流程如下：<br>
<ul><li>更新nginx.conf配置文件，向master发送SIGHUP信号或执行nginx -s reload</li><li>Master进程使用新配置，启动新的worker进程</li><li>使用旧配置的worker进程，不再接受新的连接请求，并在完成已存在的连接后退出</li></ul><br>
<br><strong>2）热升级-程序热更</strong><br>
<br>Nginx热升级过程如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210611/192380465791d1be73e0934d6ca4cec1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210611/192380465791d1be73e0934d6ca4cec1.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>将旧Nginx文件换成新Nginx文件（注意备份）</li><li>向master进程发送USR2信号（平滑升级到新版本的Nginx程序）</li><li>master进程修改pid文件号，加后缀.oldbin</li><li>master进程用新Nginx文件启动新master进程，此时新老master/worker同时存在。</li><li>向老master发送WINCH信号，关闭旧worker进程，观察新worker进程工作情况。若升级成功，则向老master进程发送QUIT信号，关闭老master进程；若升级失败，则需要回滚，向老master发送HUP信号（重读配置文件），向新master发送QUIT信号，关闭新master及worker。</li></ul><br>
<br><h3>Worker进程</h3><h4>核心逻辑</h4>Worker进程的主逻辑在ngx_worker_process_cycle，核心关注源码：<br>
<pre class="prettyprint">ngx_worker_process_cycle(ngx_cycle_t *cycle, void *data)<br>
&#123;<br>
ngx_int_t worker = (intptr_t) data;<br>
<br>
<br>
ngx_process = NGX_PROCESS_WORKER;<br>
ngx_worker = worker;<br>
<br>
<br>
ngx_worker_process_init(cycle, worker);<br>
<br>
<br>
ngx_setproctitle("worker process");<br>
<br>
<br>
for ( ;; ) &#123;<br>
<br>
<br>
    if (ngx_exiting) &#123;...&#125;<br>
<br>
<br>
    ngx_log_debug0(NGX_LOG_DEBUG_EVENT, cycle->log, 0, "worker cycle");<br>
<br>
<br>
    ngx_process_events_and_timers(cycle);<br>
<br>
<br>
    if (ngx_terminate) &#123;...&#125;<br>
<br>
<br>
    if (ngx_quit) &#123;...&#125;<br>
<br>
<br>
    if (ngx_reopen) &#123;...&#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
由上述代码，可以理解，worker进程主要在处理网络事件，通过ngx_process_events_and_timers方法实现，其中事件主要包括：网络事件、定时器事件。<br>
<h4>事件驱动-epoll</h4>Worker进程在处理网络事件时，依靠epoll模型，来管理并发连接，实现了事件驱动、异步、非阻塞等特性。如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210611/0b958eef5c6892a805d7b22bc1bc532c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210611/0b958eef5c6892a805d7b22bc1bc532c.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
通常海量并发连接过程中，每一时刻（相对较短的一段时间），往往只需要处理一小部分有事件的连接即活跃连接。基于以上现象，epoll通过将连接管理与活跃连接管理进行分离，实现了高效、稳定的网络IO处理能力。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210611/723ed6e414619159d100f360a610f5be.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210611/723ed6e414619159d100f360a610f5be.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
其中，epoll利用红黑树高效的增删查效率来管理连接，利用一个双向链表来维护活跃连接。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210611/4c0085d235fbae9fa1424d01953d5f49.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210611/4c0085d235fbae9fa1424d01953d5f49.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>惊群</h4>由于worker都是由master进程fork产生，所以worker都会监听相同端口。这样多个子进程在accept建立连接时会发生争抢，带来著名的“惊群”问题。<br>
<br>Worker核心处理逻辑ngx_process_events_and_timers核心代码如下：<br>
<pre class="prettyprint">void ngx_process_events_and_timers(ngx_cycle_t *cycle)&#123;<br>
//这里面会对监听socket处理<br>
...<br>
<br>
if (ngx_accept_disabled > 0) &#123;<br>
        ngx_accept_disabled--;<br>
&#125; else &#123;<br>
    //获得锁则加入wait集合,<br>
    if (ngx_trylock_accept_mutex(cycle) == NGX_ERROR) &#123;<br>
        return;<br>
    &#125;<br>
    ...<br>
    //设置网络读写事件延迟处理标志，即在释放锁后处理<br>
    if (ngx_accept_mutex_held) &#123;<br>
        flags |= NGX_POST_EVENTS;<br>
    &#125;<br>
&#125;<br>
...<br>
//这里面epollwait等待网络事件<br>
//网络连接事件，放入ngx_posted_accept_events队列<br>
//网络读写事件，放入ngx_posted_events队列<br>
(void) ngx_process_events(cycle, timer, flags);<br>
...<br>
//先处理网络连接事件，只有获取到锁，这里才会有连接事件<br>
ngx_event_process_posted(cycle, &ngx_posted_accept_events);<br>
//释放锁，让其他进程也能够拿到<br>
if (ngx_accept_mutex_held) &#123;<br>
    ngx_shmtx_unlock(&ngx_accept_mutex);<br>
&#125;<br>
//处理网络读写事件<br>
ngx_event_process_posted(cycle, &ngx_posted_events);<br>
&#125; <br>
</pre><br>
由上述代码可知，Nginx解决惊群的方法：<br>
<ul><li>将连接事件与读写事件进行分离。连接事件存放为ngx_posted_accept_events，读写事件存放为ngx_posted_events。</li><li>设置ngx_accept_mutex锁，只有获得锁的进程，才可以处理连接事件。</li></ul><br>
<br><h4>负载均衡</h4>Worker间的负载关键在于各自接入了多少连接，其中接入连接抢锁的前置条件是ngx_accept_disabled > 0，所以ngx_accept_disabled就是负载均衡机制实现的关键阈值。<br>
<pre class="prettyprint">ngx_int_t             ngx_accept_disabled;<br>
ngx_accept_disabled = ngx_cycle->connection_n / 8 - ngx_cycle->free_connection_n;<br>
</pre><br>
因此，在Nginx启动时，ngx_accept_disabled的值就是一个负数，其值为连接总数的7/8。当该进程的连接数达到总连接数的7/8时，该进程就不会再处理新的连接了。<br>
<br>同时每次调用'ngx_process_events_and_timers'时，将ngx_accept_disabled减1，直到其值低于阈值时，才试图重新处理新的连接。<br>
<br>因此，nginx各worker子进程间的负载均衡仅在某个worker进程处理的连接数达到它最大处理总数的7/8时才会触发，其负载均衡并不是在任意条件都满足。如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210611/91f23299c6dad75e3b6dec4947d92ea5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210611/91f23299c6dad75e3b6dec4947d92ea5.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
其中'pid'为1211的进程为master进程，其余为worker进程。<br>
<h3>思考</h3><h4>为什么不采用多线程模型管理连接？</h4><ul><li>无状态服务，无需共享进程内存</li><li>采用独立的进程，可以让互相之间不会影响。一个进程异常崩溃，其他进程的服务不会中断，提升了架构的可靠性。</li><li>进程之间不共享资源，不需要加锁，所以省掉了锁带来的开销。</li></ul><br>
<br><h4>为什么不采用多线程处理逻辑业务？</h4><ul><li>进程数已经等于核心数，再新建线程处理任务，只会抢占现有进程，增加切换代价。</li><li>作为接入层，基本上都是数据转发业务，网络IO任务的等待耗时部分，已经被处理为非阻塞/全异步/事件驱动模式，在没有更多CPU的情况下，再利用多线程处理，意义不大。并且如果进程中有阻塞的处理逻辑，应该由各个业务进行解决，比如openResty中利用了Lua协程，对阻塞业务进行了优化。</li></ul><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/o_OlJJdUz-t7znqXvIXwqg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/o_OlJJdUz-t7znqXvIXwqg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            