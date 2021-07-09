
---
title: '定时器_ Linux 中的 epoll'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82ceaa4ea2d2402ead3db3c71fbc7f61~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 08:26:30 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82ceaa4ea2d2402ead3db3c71fbc7f61~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>在看 Node http 模块文档的时候， 才留意到 <code>server.timeout</code> 这个属性， 本想简单介绍一下， 但是在梳理过后发现关于 <code>timeout</code> 有庞大的内容支撑： <code>server.timout -> node core timers -> uv timers -> linux msleep/hrtimer -> clocksource -> tsc -> cmos rtc -> clock cycle</code>， 所以拆分成几部分大致做下介绍， 期望定时器系列结束之后， noder 能够大致明白: <code>clock cycle</code> 是如何驱动 linux 的 <code>msleep/hrtimer</code>； linux 的 timers 与 uv timers 的关系； node timers 与 uv timers的关系。</p>
</blockquote>
<p>在<a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer">Libuv中的timer</a>中大胆猜测了epoll是通过linux中<code>低精度定时器</code>实现的，不幸的是只猜对了一半。关于epoll在timer中的应用需要关注两个地方: <code>同步阻塞</code>和<code>定时触发</code>，其中定时触发是通过linux的高精度定时器实现的(其实linux只要支持高精度定时器，最终所有的定时器都是高精度定时器，只不过低精度定时器是通过高精度定时器模拟出来的)。</p>
<h2 data-id="heading-0">定时器</h2>
<p>在整个学习定时器阅读源码的过程中，个人一直非常关注的地方就是<code>触发源</code>，什么触发了代码的执行。触发源的本质有两种: <code>硬件触发</code>，<code>软件触发</code>。</p>
<p>软件触发</p>
<pre><code class="copyable">while(true) &#123;
const now = getTimeFromTimeKeeper();
if (now === '双11') &#123;
emitEventInvokeActions();// 触发源
&#125;
schedule()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>硬件触发</p>
<p>硬件触发通过发送<code>中断信号</code>，告知CPU执行指定的中断程序，在中断程序中判断是否到达指定时间，比软件触发的代价更低。关于<code>硬件启动注册及切换</code>的过程，可以通过<code>/var/log/dmesg</code>查看</p>
<pre><code class="copyable">#$ cat dmesg|grep -i -E "hz|clock|time|tsc|rtc|apic|hpet"
...
[    1.792655] kernel: clocksource: Switched to clocksource tsc
...
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">epoll 定时触发</h2>
<p>现代计算机中无论高精度还是低精度都是通过硬件中断的方式来实现定时的，所以关于epoll 定时触发没有什么神秘可言。</p>
<p>通过linux源码中<code>epoll-wait</code>的系统调用<code>SYSCALL_DEFINE4(epoll_wait,..., int timeout)</code>死盯<code>timeout</code>参数一步步追踪可以发现:</p>
<pre><code class="copyable">static int ep_poll(struct eventpoll *ep, struct epoll_event __user *events,
   int maxevents, long timeout)
&#123;
...
struct timespec64 end_time = ep_set_mstimeout(timeout);
*to = timespec64_to_ktime(end_time); // 转成 纳秒精度
schedule_hrtimeout_range(to, slack, HRTIMER_MODE_ABS); // 后面触发工作就是定时器的任务了
...
__set_current_state(TASK_INTERRUPTIBLE);// 可中断的睡眠状态
...
__set_current_state(TASK_RUNNING);// 可运行状态。未必正在使用CPU，也许是在等待调度
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定时器的基本原理比较简单，但是由上可知，定时器是异步触发的，那epoll是如何做到同步阻塞的呢？</p>
<h2 data-id="heading-2">epoll 同步阻塞</h2>
<p>Libuv中定时器严重依赖于epoll的<code>同步阻塞</code>功能，触发问题通过高精度定时器来解决了，那同步问题如何解决--<code>进程调度</code>(操作系统原理)？</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82ceaa4ea2d2402ead3db3c71fbc7f61~tplv-k3u1fbpfcp-watermark.image" alt="process.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有上面代码可知在ep_poll方法中，主动调用<code>__set_current_state</code>方法，使进程进入<code>TASK_INTERRUPTIBLE</code>状态，退出CPU调度，进入<code>等待执行状态</code>，该状态可以被<code>中断唤醒</code>，而等待的中断就是我们设置的定时器产生的。</p>
<h2 data-id="heading-3">epoll 姗姗来迟</h2>
<p>epoll 这么香，为什么在2.6内核版本的时候才开始引入？</p>
<p>作为大前端开发人员，咱对linux发展史不熟悉，但是咱对react熟悉呀。回顾下react发展史，component+stackReconcile -> fiberReconcile+hook -> concurrencyReconcile+hook。 concurrencyReconcile+hook这么香，尤其是hook，那为什么一开始没有引入到react中？ 如果。。。</p>
<p>历史没有如果，软件是是演化而来的，而不是设计出来的。每个时代的产物都与当时的时代背景紧密相关，而不能在一个新的时代去思考旧时代的为什么。时代在发展，人也在进步，活在当下。</p>
<p>关注我的微信公众号，欢迎留言讨论，我会尽可能回复，感谢您的阅读。</p></div>  
</div>
            