
---
title: 'RT-Thread v4.1.0 Beta 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-08c1ef6b64a4818ae710b3476155ae6b1f6.png'
author: 开源中国
comments: false
date: Sat, 05 Feb 2022 07:50:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-08c1ef6b64a4818ae710b3476155ae6b1f6.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://oscimg.oschina.net/oscnet/up-08c1ef6b64a4818ae710b3476155ae6b1f6.png" referrerpolicy="no-referrer"></p> 
<h2><span>前言</span></h2> 
<p style="color:#1a1a1a; margin-left:0; margin-right:0; text-align:justify"><span>虽然距离上次发布v4.0.5的更新才刚刚过去一个月的时间，但是经过我们紧锣密鼓的准备，我们终于在农历新年第一天为大家带来了全新的 v4.1.0 Beta 版本。这是一个<strong>体验尝鲜版并非4.1.0正式发布版</strong>，包含一些重大的更新，目前处于公测阶段，欢迎大家下载体验。预计收集完反馈之后稳定的版本 <strong>v4.1.0 将会在今年3月下旬正式发布</strong>。</span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>下载地址：</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><strong><span>gitee: </span></strong></p> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/rtthread/rt-thread/repository/archive/v4.1.0-beta"><span>https://gitee.com/rtthread/rt-thread/repository/archive/v4.1.0-beta</span></a><span> （国内用户推荐）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong><span>github: </span></strong></p> <p style="margin-left:0; margin-right:0"><span style="background-color:transparent; color:#0366d6">https://github.com/RT-Thread/rt-thread/archive/refs/tags/v4.1.0-beta.zip</span></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>更新日志</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>更完善的 POSIX 支持（PSE51 以及 其他常用的POSIX API 支持）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>更完善的跨多编译器平台的支持</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>更加稳定精简的系统内核</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>更完善的CPP11支持（gcc、armclang 双平台支持）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>更完善的64位架构支持</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>更完善的驱动框架（PM、sensor、sdio、cputime、usb）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>更多的原厂BSP（瑞萨、新唐、先楫、沁恒、小华半导体、东软载波...）</span></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>详细日志</span></h3> 
<p style="color:#1a1a1a; margin-left:0; margin-right:0; text-align:start"><span style="background-color:transparent; color:#0366d6">https://github.com/RT-Thread/rt-thread/releases/tag/v4.1.0-beta</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>迁移指南</span></h2> 
<p style="color:#1a1a1a; margin-left:0; margin-right:0; text-align:start"><span>在 RT-Thread 的 v4.1.0 版本及后续的版本，移除了 dfs_poll.h, dfs_posix.h, dfs_select.h三个之前常用的头文件。并且移除了 RT_USING_LIBC，RT_USING_POSIX 两个范围较大的宏。</span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>修改原因</span></h3> 
<p style="color:#1a1a1a; margin-left:0; margin-right:0; text-align:start"><span>该项改动的原因，是因为我们推动了 POSIX 编程接口标准化工作，方便 POSIX（例如类UNIX） 程序向 RT-Thread 迁移而无需大规模改动头文件。因此我们移除了dfs_poll.h, dfs_posix.h, dfs_select.h 这些被大量使用但带有 RT-Thread 特点的头文件；移除了模糊且开启范围过大的宏开关 RT_USING_POSIX 和 RT_USING_LIBC；细化了裁剪宏开关，使得裁剪更加精细化，在丰富功能的同时，不会导致代码体积的膨胀。用户可根据自己实际需求，精细化配置POSIX相关的功能。</span></p> 
<p style="color:#1a1a1a; margin-left:0; margin-right:0; text-align:start"><span><strong>产生的问题</strong><br> 由于历史原因，在部分软件包中，仍然有对RT_USING_LIBC，RT_USING_POSIX, dfs_poll.h, dfs_posix.h, dfs_select.h 的使用，在 RT-Thread 的 v4.1.0 版本及后续的版本中可能会出现编译失败的问题。</span></p> 
<p style="color:#1a1a1a; margin-left:0; margin-right:0; text-align:start"><strong>如果发现类似问题，请到社区论坛发帖报告，我们将及时处理</strong></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>解决方案</span></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">若代码中仍有 RT_USING_LIBC 与 RT_USING_POSIX 来判断添加某些头文件，则需要将这两个宏删除并细化：</p> </li> 
</ul> 
<pre style="margin-left:0; margin-right:0"><code><span style="color:#ae87fa"> 1</span>RT_USING_POSIX_FS
<span style="color:#ae87fa"> 2</span>    RT_USING_POSIX_DEVIO     --->Enable devices as file descriptors
<span style="color:#ae87fa"> 3</span>    RT_USING_POSIX_STDIO     --->Enable standard I/O devices, e.g. STDOUT_FILENO
<span style="color:#ae87fa"> 4</span>    RT_USING_POSIX_POLL      --->Enable I/<span style="color:#f82375">O Multiplexing <span style="color:#a5da2d">poll</span><span style="color:#ff9823">()</span> <poll.h>
<span style="color:#ae87fa"> 5</span>    RT_USING_POSIX_SELECT    --->Enable I/O Multiplexing <span style="color:#a5da2d">select</span><span style="color:#ff9823">()</span> <sys/select.h>
<span style="color:#ae87fa"> 6</span>    RT_USING_POSIX_TERMIOS   --->Enable Terminal I/O <termios.h>
<span style="color:#ae87fa"> 7</span>    RT_USING_POSIX_AIO       --->Enable Asynchronous I/O 
<span style="color:#ae87fa"> 8</span>    RT_USING_POSIX_MMAN      --->Enable Memory-Mapped I/O <sys/mman.h>
<span style="color:#ae87fa"> 9</span>RT_USING_POSIX_DELAY
<span style="color:#ae87fa">10</span>RT_USING_POSIX_CLOCK
<span style="color:#ae87fa">11</span>RT_USING_POSIX_TIMER
<span style="color:#ae87fa">12</span>RT_USING_PTHREADS
<span style="color:#ae87fa">13</span></span></code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">若代码中有 #include <dfs_posix.h>，按照代码中，对接口的需要，视情况分别引用 dfs_file.h,unistd.h,stdio.h,sys/stat.h, sys/statfs.h。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">若代码中有 #include <dfs_select.h> 修改为引用 sys/select.h</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">若代码中有 #include <dfs_poll.h> 修改为引用 poll.h</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>需要特殊注意的头文件</span></h3> 
<p style="color:#1a1a1a; margin-left:0; margin-right:0; text-align:start"><span>为保证跨不同编译器、不同工具链的兼容性，建议用户应用层代码：</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>使用 <sys/time.h> 代替 <time.h></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>使用 <sys/errno.h> 代替 <errno.h></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>使用 <sys/signal.h> 代替 <signal.h></span></p> </li> 
</ul> 
<h2 style="margin-left:.875em; margin-right:0; text-align:center"><span>欢迎小伙伴至论坛评论区留言！</span></h2> 
<h2 style="margin-left:0; margin-right:0; text-align:center"><span>欢迎大家多多贡献代码（PR）</span></h2> 
<p style="color:#1a1a1a; margin-left:0; margin-right:0; text-align:center"><span>如何给RT-Thread贡献代码这里有视频教程</span></p> 
<p style="color:#1a1a1a; margin-left:0; margin-right:0; text-align:center"><span style="background-color:transparent; color:#0366d6">https://www.bilibili.com/video/BV1gr4y1w7yX</span></p>
                                        </div>
                                      
</div>
            