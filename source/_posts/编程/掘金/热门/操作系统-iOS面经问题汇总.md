
---
title: '操作系统-iOS面经问题汇总'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=2159'
author: 掘金
comments: false
date: Tue, 16 Mar 2021 06:38:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=2159'
---

<div>   
<div class="markdown-body"><style>.markdown-body .octicon&#123;display:inline-block;fill:currentColor;vertical-align:text-bottom&#125;.markdown-body .anchor&#123;float:left;line-height:1;margin-left:-20px;padding-right:4px&#125;.markdown-body .anchor:focus&#123;outline:none&#125;.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link&#123;color:#1b1f23;vertical-align:middle;visibility:hidden&#125;.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor&#123;text-decoration:none&#125;.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link&#123;visibility:visible&#125;.markdown-body h1:hover .anchor .octicon-link:before,.markdown-body h2:hover .anchor .octicon-link:before,.markdown-body h3:hover .anchor .octicon-link:before,.markdown-body h4:hover .anchor .octicon-link:before,.markdown-body h5:hover .anchor .octicon-link:before,.markdown-body h6:hover .anchor .octicon-link:before&#123;width:16px;height:16px;content:" ";display:inline-block;background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' aria-hidden='true'%3E%3Cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z'/%3E%3C/svg%3E")&#125;.markdown-body&#123;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#24292e;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size:16px;line-height:1.5;word-wrap:break-word&#125;.markdown-body details&#123;display:block&#125;.markdown-body summary&#123;display:list-item&#125;.markdown-body a&#123;background-color:initial&#125;.markdown-body a:active,.markdown-body a:hover&#123;outline-width:0&#125;.markdown-body strong&#123;font-weight:inherit;font-weight:bolder&#125;.markdown-body h1&#123;margin:.67em 0&#125;.markdown-body img&#123;border-style:none&#125;.markdown-body code,.markdown-body kbd,.markdown-body pre&#123;font-family:monospace,monospace;font-size:1em&#125;.markdown-body hr&#123;box-sizing:initial;overflow:visible&#125;.markdown-body input&#123;font:inherit;margin:0;overflow:visible&#125;.markdown-body [type=checkbox]&#123;box-sizing:border-box;padding:0&#125;.markdown-body *&#123;box-sizing:border-box&#125;.markdown-body input&#123;font-family:inherit;font-size:inherit;line-height:inherit&#125;.markdown-body a&#123;color:#0366d6;text-decoration:none&#125;.markdown-body a:hover&#123;text-decoration:underline&#125;.markdown-body strong&#123;font-weight:600&#125;.markdown-body hr&#123;height:0;margin:15px 0;overflow:hidden;background:transparent;border-bottom:1px solid #dfe2e5&#125;.markdown-body hr:after,.markdown-body hr:before&#123;display:table;content:""&#125;.markdown-body hr:after&#123;clear:both&#125;.markdown-body table&#123;border-spacing:0;border-collapse:collapse&#125;.markdown-body td,.markdown-body th&#123;padding:0&#125;.markdown-body details summary&#123;cursor:pointer&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:0;margin-bottom:0&#125;.markdown-body h1&#123;font-size:32px&#125;.markdown-body h1,.markdown-body h2&#123;font-weight:600&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3,.markdown-body h4&#123;font-weight:600&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5,.markdown-body h6&#123;font-weight:600&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body p&#123;margin-top:0;margin-bottom:10px&#125;.markdown-body blockquote&#123;margin:0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:0;margin-top:0;margin-bottom:0&#125;.markdown-body ol ol,.markdown-body ul ol&#123;list-style-type:lower-roman&#125;.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol&#123;list-style-type:lower-alpha&#125;.markdown-body dd&#123;margin-left:0&#125;.markdown-body code,.markdown-body pre&#123;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px&#125;.markdown-body pre&#123;margin-top:0;margin-bottom:0&#125;.markdown-body input::-webkit-inner-spin-button,.markdown-body input::-webkit-outer-spin-button&#123;margin:0;-webkit-appearance:none;appearance:none&#125;.markdown-body :checked+.radio-label&#123;position:relative;z-index:1;border-color:#0366d6&#125;.markdown-body .border&#123;border:1px solid #e1e4e8!important&#125;.markdown-body .border-0&#123;border:0!important&#125;.markdown-body .border-bottom&#123;border-bottom:1px solid #e1e4e8!important&#125;.markdown-body .rounded-1&#123;border-radius:3px!important&#125;.markdown-body .bg-white&#123;background-color:#fff!important&#125;.markdown-body .bg-gray-light&#123;background-color:#fafbfc!important&#125;.markdown-body .text-gray-light&#123;color:#6a737d!important&#125;.markdown-body .pl-3,.markdown-body .px-3&#123;padding-left:16px!important&#125;.markdown-body .px-3&#123;padding-right:16px!important&#125;.markdown-body .f6&#123;font-size:12px!important&#125;.markdown-body .lh-condensed&#123;line-height:1.25!important&#125;.markdown-body .text-bold&#123;font-weight:600!important&#125;.markdown-body .pl-c&#123;color:#6a737d&#125;.markdown-body .pl-c1,.markdown-body .pl-s .pl-v&#123;color:#005cc5&#125;.markdown-body .pl-e,.markdown-body .pl-en&#123;color:#6f42c1&#125;.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi&#123;color:#24292e&#125;.markdown-body .pl-ent&#123;color:#22863a&#125;.markdown-body .pl-k&#123;color:#d73a49&#125;.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre&#123;color:#032f62&#125;.markdown-body .pl-smw,.markdown-body .pl-v&#123;color:#e36209&#125;.markdown-body .pl-bu&#123;color:#b31d28&#125;.markdown-body .pl-ii&#123;color:#fafbfc;background-color:#b31d28&#125;.markdown-body .pl-c2&#123;color:#fafbfc;background-color:#d73a49&#125;.markdown-body .pl-c2:before&#123;content:"^M"&#125;.markdown-body .pl-sr .pl-cce&#123;font-weight:700;color:#22863a&#125;.markdown-body .pl-ml&#123;color:#735c0f&#125;.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms&#123;font-weight:700;color:#005cc5&#125;.markdown-body .pl-mi&#123;font-style:italic;color:#24292e&#125;.markdown-body .pl-mb&#123;font-weight:700;color:#24292e&#125;.markdown-body .pl-md&#123;color:#b31d28;background-color:#ffeef0&#125;.markdown-body .pl-mi1&#123;color:#22863a;background-color:#f0fff4&#125;.markdown-body .pl-mc&#123;color:#e36209;background-color:#ffebda&#125;.markdown-body .pl-mi2&#123;color:#f6f8fa;background-color:#005cc5&#125;.markdown-body .pl-mdr&#123;font-weight:700;color:#6f42c1&#125;.markdown-body .pl-ba&#123;color:#586069&#125;.markdown-body .pl-sg&#123;color:#959da5&#125;.markdown-body .pl-corl&#123;text-decoration:underline;color:#032f62&#125;.markdown-body .mb-0&#123;margin-bottom:0!important&#125;.markdown-body .my-2&#123;margin-bottom:8px!important;margin-top:8px!important&#125;.markdown-body .pl-0&#123;padding-left:0!important&#125;.markdown-body .py-0&#123;padding-top:0!important;padding-bottom:0!important&#125;.markdown-body .pl-1&#123;padding-left:4px!important&#125;.markdown-body .pl-2&#123;padding-left:8px!important&#125;.markdown-body .py-2&#123;padding-top:8px!important;padding-bottom:8px!important&#125;.markdown-body .pl-3&#123;padding-left:16px!important&#125;.markdown-body .pl-4&#123;padding-left:24px!important&#125;.markdown-body .pl-5&#123;padding-left:32px!important&#125;.markdown-body .pl-6&#123;padding-left:40px!important&#125;.markdown-body .pl-7&#123;padding-left:48px!important&#125;.markdown-body .pl-8&#123;padding-left:64px!important&#125;.markdown-body .pl-9&#123;padding-left:80px!important&#125;.markdown-body .pl-10&#123;padding-left:96px!important&#125;.markdown-body .pl-11&#123;padding-left:112px!important&#125;.markdown-body .pl-12&#123;padding-left:128px!important&#125;.markdown-body hr&#123;border-bottom-color:#eee&#125;.markdown-body kbd&#123;display:inline-block;padding:3px 5px;font:11px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;line-height:10px;color:#444d56;vertical-align:middle;background-color:#fafbfc;border:1px solid #d1d5da;border-radius:3px;box-shadow:inset 0 -1px 0 #d1d5da&#125;.markdown-body:after,.markdown-body:before&#123;display:table;content:""&#125;.markdown-body:after&#123;clear:both&#125;.markdown-body>:first-child&#123;margin-top:0!important&#125;.markdown-body>:last-child&#123;margin-bottom:0!important&#125;.markdown-body a:not([href])&#123;color:inherit;text-decoration:none&#125;.markdown-body blockquote,.markdown-body details,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul&#123;margin-top:0;margin-bottom:16px&#125;.markdown-body hr&#123;height:.25em;padding:0;margin:24px 0;background-color:#e1e4e8;border:0&#125;.markdown-body blockquote&#123;padding:0 1em;color:#6a737d;border-left:.25em solid #dfe2e5&#125;.markdown-body blockquote>:first-child&#123;margin-top:0&#125;.markdown-body blockquote>:last-child&#123;margin-bottom:0&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:24px;margin-bottom:16px;font-weight:600;line-height:1.25&#125;.markdown-body h1&#123;font-size:2em&#125;.markdown-body h1,.markdown-body h2&#123;padding-bottom:.3em;border-bottom:1px solid #eaecef&#125;.markdown-body h2&#123;font-size:1.5em&#125;.markdown-body h3&#123;font-size:1.25em&#125;.markdown-body h4&#123;font-size:1em&#125;.markdown-body h5&#123;font-size:.875em&#125;.markdown-body h6&#123;font-size:.85em;color:#6a737d&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:0;margin-bottom:0&#125;.markdown-body li&#123;word-wrap:break-all&#125;.markdown-body li>p&#123;margin-top:16px&#125;.markdown-body li+li&#123;margin-top:.25em&#125;.markdown-body dl&#123;padding:0&#125;.markdown-body dl dt&#123;padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:600&#125;.markdown-body dl dd&#123;padding:0 16px;margin-bottom:16px&#125;.markdown-body table&#123;display:block;width:100%;overflow:auto&#125;.markdown-body table th&#123;font-weight:600&#125;.markdown-body table td,.markdown-body table th&#123;padding:6px 13px;border:1px solid #dfe2e5&#125;.markdown-body table tr&#123;background-color:#fff;border-top:1px solid #c6cbd1&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body img&#123;max-width:100%;box-sizing:initial;background-color:#fff&#125;.markdown-body img[align=right]&#123;padding-left:20px&#125;.markdown-body img[align=left]&#123;padding-right:20px&#125;.markdown-body code&#123;padding:.2em .4em;margin:0;font-size:85%;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body pre&#123;word-wrap:normal&#125;.markdown-body pre>code&#123;padding:0;margin:0;font-size:100%;word-break:normal;white-space:pre;background:transparent;border:0&#125;.markdown-body .highlight&#123;margin-bottom:16px&#125;.markdown-body .highlight pre&#123;margin-bottom:0;word-break:normal&#125;.markdown-body .highlight pre,.markdown-body pre&#123;padding:16px;overflow:auto;font-size:85%;line-height:1.45;background-color:#f6f8fa;border-radius:3px&#125;.markdown-body pre code&#123;display:inline;max-width:auto;padding:0;margin:0;overflow:visible;line-height:inherit;word-wrap:normal;background-color:initial;border:0&#125;.markdown-body .commit-tease-sha&#123;display:inline-block;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:90%;color:#444d56&#125;.markdown-body .full-commit .btn-outline:not(:disabled):hover&#123;color:#005cc5;border-color:#005cc5&#125;.markdown-body .blob-wrapper&#123;overflow-x:auto;overflow-y:hidden&#125;.markdown-body .blob-wrapper-embedded&#123;max-height:240px;overflow-y:auto&#125;.markdown-body .blob-num&#123;width:1%;min-width:50px;padding-right:10px;padding-left:10px;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;line-height:20px;color:rgba(27,31,35,.3);text-align:right;white-space:nowrap;vertical-align:top;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none&#125;.markdown-body .blob-num:hover&#123;color:rgba(27,31,35,.6)&#125;.markdown-body .blob-num:before&#123;content:attr(data-line-number)&#125;.markdown-body .blob-code&#123;position:relative;padding-right:10px;padding-left:10px;line-height:20px;vertical-align:top&#125;.markdown-body .blob-code-inner&#123;overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:#24292e;word-wrap:normal;white-space:pre&#125;.markdown-body .pl-token.active,.markdown-body .pl-token:hover&#123;cursor:pointer;background:#ffea7f&#125;.markdown-body .tab-size[data-tab-size="1"]&#123;-moz-tab-size:1;tab-size:1&#125;.markdown-body .tab-size[data-tab-size="2"]&#123;-moz-tab-size:2;tab-size:2&#125;.markdown-body .tab-size[data-tab-size="3"]&#123;-moz-tab-size:3;tab-size:3&#125;.markdown-body .tab-size[data-tab-size="4"]&#123;-moz-tab-size:4;tab-size:4&#125;.markdown-body .tab-size[data-tab-size="5"]&#123;-moz-tab-size:5;tab-size:5&#125;.markdown-body .tab-size[data-tab-size="6"]&#123;-moz-tab-size:6;tab-size:6&#125;.markdown-body .tab-size[data-tab-size="7"]&#123;-moz-tab-size:7;tab-size:7&#125;.markdown-body .tab-size[data-tab-size="8"]&#123;-moz-tab-size:8;tab-size:8&#125;.markdown-body .tab-size[data-tab-size="9"]&#123;-moz-tab-size:9;tab-size:9&#125;.markdown-body .tab-size[data-tab-size="10"]&#123;-moz-tab-size:10;tab-size:10&#125;.markdown-body .tab-size[data-tab-size="11"]&#123;-moz-tab-size:11;tab-size:11&#125;.markdown-body .tab-size[data-tab-size="12"]&#123;-moz-tab-size:12;tab-size:12&#125;.markdown-body .task-list-item&#123;list-style-type:none&#125;.markdown-body .task-list-item+.task-list-item&#123;margin-top:3px&#125;.markdown-body .task-list-item input&#123;margin:0 .2em .25em -1.6em;vertical-align:middle&#125;</style><h2 data-id="heading-0">1.什么是操作系统？</h2>
<ol>
<li>操作系统（OS）是管理计算机硬件与软件资源的程序，是计算机的基石。</li>
<li>操作系统本质上是运行在计算机的软件程序，其他应用程序都需要通过操作系统来调用系统的资源，如内存、CPU、GPU、磁盘；</li>
<li>操作系统的存在屏蔽了硬件和硬件层面的复杂性；</li>
<li>操作系统的内核（Kernel）是操作系统的核心部分，它负责系统的内存、硬件、文件系统、应用程序的管理。</li>
</ol>
<h2 data-id="heading-1">2.讲一讲用户态和系统态</h2>
<ul>
<li>根据进程访问资源的特点可以分为用户态的系统态
<ol>
<li>用户态：用户态运行的进程可以访问用户程序的数据；</li>
<li>系统态：几乎可以访问任意的计算机资源，不受限制</li>
</ol>
</li>
<li>我们运行的程序基本上都在用户态运行，如果需要调用系统级别的子功能（如文件管理，进程控制，内存管理等）则需要切换到系统态，进行系统调用。通过系统调用，向操作系统提出请求，由其代为完成。</li>
</ul>
<h2 data-id="heading-2">3.讲一讲系统调用</h2>
<ul>
<li>系统调用按照功能可以分为以下几类：
<ol>
<li>设备管理：设备的请求或释放，如视频电话启动摄像头；</li>
<li>文件管理：文件的修改、创建、删除等；</li>
<li>进程控制：进程的创建、撤销、阻塞、唤醒等；</li>
<li>进程通信：完成进程间的消息或信号传递；</li>
<li>内存管理：内存分配（malloc 函数）、回收（free）、地址转换（将逻辑地址转化为物理地址等）</li>
</ol>
</li>
</ul>
<h2 data-id="heading-3">4.进程和线程的区别和联系？</h2>
<ul>
<li>联系
<ul>
<li>进程是资源分配的基本单位，线程是独立调度的基本单位;一个进程中可以有多个线程，它们共享进程资源；</li>
</ul>
</li>
<li>区别
<ul>
<li>拥有资源：</li>
</ul>
<blockquote>
<p>进程是资源分配的基本单位，但是线程不拥有资源，线程可以访问隶属进程的资源。</p>
</blockquote>
<ul>
<li>调度：</li>
</ul>
<blockquote>
<p>线程是独立调度的基本单位，在同一进程中，线程的切换不会引起进程切换；从一个进程的线程切换到另一个进程的线程时，会引起进程的切换。</p>
</blockquote>
<ul>
<li>系统开销</li>
</ul>
<blockquote>
<p>进程的开销更大，线程的开销小。</p>
</blockquote>
<ul>
<li>通信</li>
</ul>
<blockquote>
<p>线程间可以通过直接读写同一进程中的数据进行通信，但进程间的通信需要借助IPC。</p>
</blockquote>
</li>
</ul>
<h2 data-id="heading-4">5.进程和线程的切换哪个带来的资源消耗大？为什么线程的消耗比较小？</h2>
<p>由于创建或撤销进程时，系统都要为之分配或回收资源，如内存空间、I/O设备等，所付出的开销远大于创建或撤销线程时的开销。类似地，在进行进程切换时，涉及当前进程CPU的保存及新调度进程CPU环境的设置，而线程切换时只需保存和设置少量寄存器内容，开销很小。最主要的一个区别在于进程切换涉及虚拟地址空间的切换而线程不会。因为每个进程都有自己的虚拟地址空间，而线程是共享所在进程的虚拟地址空间的，因此同一个进程中的线程进行线程切换时不涉及虚拟地址空间的转换。</p>
<p>说法2:CPU上下文切换就是把前一个任务的 CPU 上下文（也就是 CPU 寄存器和程序计数器）保存起来，然后加载新任务的上下文到这些寄存器和程序计数器，来运行新任务。一次系统调用的过程，其实是发生了两次 CPU 上下文切换。（用户态代码-系统态代码-用户态代码）。系统调用过程中，并不会涉及到虚拟内存等进程用户态的资源。进程上下文切换就比系统调用时多了一步：在保存内核态资源之前，需要把用户态资源（虚拟内存、栈等）保存下来；而由于同一进程的线程共享堆和方法区，因此同一进程的线程切换时，只需要切换线程的私有数据即可，而不同进程的线程切换过程就跟进程上下文切换是一样的。</p>
<h2 data-id="heading-5">6.线程共享哪些内存空间？</h2>
<p>一个进程中的所有线程共享该进程的地址空间，但它们有各自独立的（私有的）栈(stack)；同一进程内的线程共享本进程的资源如虚拟内存、描述符等，但是进程之间的资源是独立的。</p>
<h2 data-id="heading-6">7.进程和线程各自分配了哪些资源？</h2>
<ul>
<li>进程
内存空间、I/O设备、cpu、信号处理函数、打开的文件描述符等；</li>
<li>线程
有独立的调用栈/本地变量/寄存器上下文</li>
</ul>
<h2 data-id="heading-7">8.讲一下各种锁</h2>
<ul>
<li>
<h3 data-id="heading-8">互斥锁</h3>
定义：互斥锁是一种用于多线程编程，防止两条线程同时对同一公共资源（例如全局变量）进行读写的机制，该目的是通过将代码切成一个个临界区而达成。
<ul>
<li>NSLock</li>
<li>pthread_mutex</li>
<li>@synchronized</li>
</ul>
</li>
<li>
<h3 data-id="heading-9">自旋锁</h3>
定义：在自旋锁中，线程会反复检查变量是否可用。由于线程这个过程中一直保持执行，所以是一种忙等待。一旦获取了自旋锁，线程就会一直保持该锁，直到显示释放自旋锁。自旋锁避免了进程上下文的调度开销，因此对于线程只会阻塞很短时间的场合是有效的。对于iOS属性的修饰符atomic，自己带一把自旋锁。
<ul>
<li>OSSpinLock</li>
<li>atomic</li>
</ul>
</li>
<li>
<h3 data-id="heading-10">条件锁</h3>
定义：条件锁就是条件变量，当进程的某些资源要求不满足时就进入休眠，即锁住了；当资源被分配到满足条件时条件锁打开，进程继续运行。
<ul>
<li>NSCondition</li>
<li>NSConditionLock</li>
</ul>
</li>
<li>
<h3 data-id="heading-11">递归锁</h3>
定义：递归锁就是同一个线程可以加锁N次而不会引发死锁，递归锁是特殊的互斥锁，即是带有递归性质的互斥锁；
<ul>
<li>pthread_mutex(recursive)</li>
<li>NSRecursiveLock</li>
<li>@synchronized</li>
</ul>
</li>
<li>
<h3 data-id="heading-12">读写锁</h3>
读写锁实际是一种特殊的自旋锁。将对共享资源的访问分成读者和写者，读者只对共享资源进行读访问，写者则需要对共享资源进行写操作。这种锁相对于自旋锁能提高并发性。</li>
<li>
<h3 data-id="heading-13">更高级的同步机制——信号量</h3>
互斥锁可以说是semaphore取值仅在(0/1)之间的特例。信号量可以有更大的取值空间，通过限制同一资源的最多访问数来实现更加复杂的同步，而不单单是线程间的互斥。</li>
</ul>
<h2 data-id="heading-14">9.死锁的各种问题</h2>
<h3 data-id="heading-15">死锁的必要条件</h3>
<ul>
<li>互斥</li>
</ul>
<blockquote>
<p>每个资源要么已经分配给了某个进程，要么就是可用的</p>
</blockquote>
<ul>
<li>占有和等待</li>
</ul>
<blockquote>
<p>已经得到了某个资源的进程可以再请求新的资源</p>
</blockquote>
<ul>
<li>不可抢占</li>
</ul>
<blockquote>
<p>已经分配给某个进程的资源不可被强制性抢占，它只能被占有它的进程显式的释放</p>
</blockquote>
<ul>
<li>环路等待</li>
</ul>
<blockquote>
<p>有两个或两个以上的进程组成一条环路，该环路中每一个进程都在等待下一个进程占有的资源</p>
</blockquote>
<h3 data-id="heading-16">处理方法</h3>
<ul>
<li>鸵鸟策略（忽略死锁，不处理）</li>
<li>死锁检测与死锁恢复（不试图阻止死锁，而是当检测到死锁发生时，采取措施进行恢复）
<ul>
<li>通过抢占恢复</li>
<li>利用回滚恢复</li>
<li>通过杀死进程恢复</li>
</ul>
</li>
<li>死锁预防(在程序运行之前预防发生死锁)
<ul>
<li>破坏互斥条件
<ul>
<li>例如假脱机打印机技术允许若干个进程同时输出，唯一真正请求物理打印机的进程是打印机守护进程。</li>
</ul>
</li>
<li>破坏占有和等待条件
<ul>
<li>一种实现方式是规定所有进程在开始执行前请求所需要的全部资源。</li>
</ul>
</li>
<li>破坏不可抢占条件</li>
<li>破坏环路等待
<ul>
<li>给资源统一编号，进程只能按编号顺序来请求资源。</li>
</ul>
</li>
</ul>
</li>
<li>死锁避免(在程序运行时避免发生死锁)
<ul>
<li>安全状态和银行家算法</li>
</ul>
</li>
</ul>
<h2 data-id="heading-17">10.谈一谈同步和异步</h2>
<p>同步方式指的是添加任务后阻塞当前线程直到任务被加入队列并且执行结束；
异步方式指的是加入任务队列后，不必等待任务执行，函数立即返回</p>
<p>同步与异步只与线程有关，和队列无关，不要混淆；队列的串行和并行与同步、异步并无关联；
同步与异步是准备抛任务的线程 与 执行任务线程的关系；抛任务的线程是否等待这个任务执行完成，若等待就是同步，不等待就是发起了异步。</p>
<p>如何深入理解同步异步只与线程有关而和队列无关？</p>
<p>举个例子：主线程往串行队列异步抛100个任务，这100个任务是在串行队列里串行执行的，但主线程在抛完之后就不关心任务执行的怎么样了。串行是这100个任务的串行，和主线程没关系。</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-built_in">dispatch_queue_t</span> queue = dispatch_queue_create(<span class="hljs-string">"serial"</span>,null);
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">100</span>; i ++ )&#123;
    <span class="hljs-built_in">dispatch_async</span>(queue, ^&#123;
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"current:%d"</span>, i);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此处感谢@Fater7的精彩讲解。</p>
<h2 data-id="heading-18">11.两个线程同时访问i并使之++一万次，i的结果</h2>
<p>答：不可预期，具体要看线程如何调度。</p>
<ul>
<li>
<h3 data-id="heading-19">多线程下执行的顺序不可预测</h3>
<ul>
<li>编译器优化会重排代码</li>
<li>cpu会乱序执行指令</li>
<li>不要对执行顺序妄下假设</li>
</ul>
</li>
</ul>
<h2 data-id="heading-20">12.手写一个线程安全的单例模式</h2>
<p>双重校验锁模式</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-class"><span class="hljs-keyword">@implementation</span> <span class="hljs-title">Singleton</span></span>

+ (<span class="hljs-keyword">instancetype</span>)sharedInstance&#123;
<span class="hljs-keyword">static</span> Singleton * sharedInstance = <span class="hljs-literal">nil</span>;
      <span class="hljs-keyword">if</span>(!sharedInstance)&#123;
      <span class="hljs-keyword">@synchronized</span>(<span class="hljs-keyword">self</span>)&#123;
        <span class="hljs-keyword">if</span>(!sharedInstance)&#123;
          sharedInstance = [[Singleton alloc] init];
        &#125;
      &#125;
   &#125;
    <span class="hljs-comment">//NSLog(@"currentTime:%@", [NSDate date]);</span>
    <span class="hljs-keyword">if</span>(sharedInstance)&#123;
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"address：%@"</span>,[sharedInstance description]);
    &#125;
  <span class="hljs-keyword">return</span> sharedInstance;
&#125;

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>dispatch_once</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-class"><span class="hljs-keyword">@implementation</span> <span class="hljs-title">Singleton</span></span>
+(<span class="hljs-keyword">instancetype</span>)sharedInstance&#123;
    <span class="hljs-keyword">static</span> Singleton *sharedInstance = <span class="hljs-literal">nil</span>;
    <span class="hljs-keyword">static</span> <span class="hljs-built_in">dispatch_once_t</span> onceToken;
    <span class="hljs-built_in">dispatch_once</span>(&onceToken, ^&#123;
        sharedInstance = [[Singleton alloc] init];
    &#125;);
    <span class="hljs-keyword">if</span>(sharedInstance)&#123;
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"address: %@"</span>, [sharedInstance description]);
    &#125;
    <span class="hljs-keyword">return</span> sharedInstance;
&#125;
<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">13.并发和并行</h2>
<p>并发和并行并不是互斥的概念。
与并发执行对应的是顺序执行；
与并行相对应的是串行；
并发是两个队列交替使用一台咖啡机，并行是两个队列同时使用两台咖啡机；
并发和并行都可以是很多个线程，就看这些线程能不能同时被（多个）cpu执行；如果可以就说明是并行；而并发是多个线程被（一个）cpu轮流执行；</p>
<h2 data-id="heading-22">14.进程之间如何通信？</h2>
<p>常见的通信方法有管道、信号、消息队列、信号量、共享内存、套接字；</p>
<ul>
<li>管道：本质上是一块缓冲区，父进程通过fork子进程来共享管道，进行通信。管道是半双工单向通信，因此在通信前就要确定数据流向：即关闭父子进程各自一端不用的读写。如果一方是读数据就关闭写的描述符。</li>
<li>信号量：信号量是一个计数器，用于多进程共享数据的访问，通常用来实现进程间的同步，避免资源竞争</li>
<li>共享内存：多个进程访问同一块内存空间，这样进程之间可以及时看到对方对内存空间中的数据更新，通常需要使用互斥锁、信号量等同步操作来完成</li>
<li>套接字（socket）：主要用于客户端和服务器进程之间的网络通信；套接字是支持tcp/ip网络通信的基本操作单元，可以看作是不同主机进程之间双向通信的端点，是通信双方的一种约定；</li>
</ul>
<h2 data-id="heading-23">15.线程之间如何同步？</h2>
<ul>
<li>互斥资源（互斥量）：拥有互斥对象的线程才能访问公共资源，比如synchronized关键词和各种锁都是使用这个机制。</li>
<li>信号量：它允许多个线程访问同一资源，控制资源的最大线程访问数；
<ul>
<li>dispatch_semaphore</li>
</ul>
</li>
<li>时间：Wait/Notify，通过通知操作来保持线程同步。
<ul>
<li>dispatch_group_notify</li>
<li>dispatch_group_wait</li>
</ul>
</li>
</ul>
<h2 data-id="heading-24">16.讲一讲进程切换调度的算法</h2>
<ol>
<li>先到先服务（FCFS)：从就绪队列中选择最先进入的进程，为其分配资源；</li>
<li>短作业优先：选择估计运行时间最短的进程；</li>
<li>时间片轮转：为每个进程分配固定的运行时间段；</li>
<li>优先级调度：根据进程优先级进行分配，如果优先级相同使用FCFS进行调度；</li>
<li>多级反馈队列：既能使高优先级任务得到响应，又能让短作业迅速完成，Unix采用这种调度算法。</li>
</ol>
<h2 data-id="heading-25">17. 讲一讲内存管理机制和内存管理方法</h2>
<blockquote>
<p>内存管理主要分为连续分配管理和离散分配管理。离散分配管理又分为页式管理、段式管理和段页式管理。</p>
</blockquote>
<ol>
<li>页式管理：将主存分为大小固定的相等的页，用页表来管理；</li>
<li>段式管理：根据用户需求，为每段定义逻辑信息，根据段来分配内存，用段表管理；</li>
<li>段页式管理：结合段式和页式的优点，先分为段，每段再分为页。</li>
</ol>
<p>段式和页式的共同点：都是离散存储，为了提高内存利用率，减少碎片；
区别：分页式由系统完成，分段式由用户根据需求划分。一个指令可能会跨页但不会跨段，页式有内碎片而段式没有。</p>
<h2 data-id="heading-26">18.讲一讲快表和多级页表</h2>
<ol>
<li>快表提高了内存的时间性能，提高了虚拟地址到物理地址的转换速度，是一种高速的缓存，正常情况分页下需要访问两次主存，而使用快表命中的情况下只需要访问一次高速内存，一次主存即可。日常系统开发redis缓存就是借鉴了这一思想；</li>
<li>多级页表提高了内存的空间性能，通过使用多级页表映射的方式来替代把所有页表都放在内存中。</li>
</ol>
<h2 data-id="heading-27">19.什么是虚拟内存？</h2>
<p>比如某些软件运行时占用的内存要远远超出电脑本身的内存，这是通过虚拟内存来实现的。虚拟内存定义了一个连续的虚拟内存地址空间，把内存扩展到硬盘空间上（内存到外存）</p>
<h2 data-id="heading-28">20.说一说虚拟内存的局部性原理</h2>
<p>局部性原理是虚拟内存技术的基础，它允许程序部分装入内存即可运行。</p>
<ol>
<li>时间局部性：一条指令被执行或者一个数据被访问，那么不久之后这个指令或数据会再次被执行或访问；</li>
<li>空间局部性：一个存储单元被访问，则不久之后其附近的存储单元也将被访问，通过预存机制来实现高速缓存；</li>
</ol>
<h2 data-id="heading-29">21.虚拟内存的实现技术有哪些？讲一讲常见的页面置换算法。</h2>
<ul>
<li>虚拟内存的实现建立在内存离散分配管理方式的基础上，在其基础上增加了请求调页/段和页面/分段置换的功能。请求分页、请求分段、请求段页式存储管理，其原理是在开始前仅装入部分程序，当运行时发现访问的页/段不在时，再启动缺页中断，如果内存足够，则直接加入内存，不够则进行页面置换。</li>
<li>页面置换实际上就是一种淘汰页面的机制
<ol>
<li>先进先出（FIFO）：淘汰最先进入的页面</li>
<li>最近最久未使用（LRU）：记录每个页面上次被访问到现在的时间，淘汰最长的。LRU算法可以通过哈希链表（LinkedHashMap）数据结构来实现。</li>
<li>最少使用（LFU）：淘汰最少使用；</li>
<li>最佳（OPT）：根据未来的使用情况，以最低缺页率进行淘汰，不可实现的算法。</li>
</ol>
</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            