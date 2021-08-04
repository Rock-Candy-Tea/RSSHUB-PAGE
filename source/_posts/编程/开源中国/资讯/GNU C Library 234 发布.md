
---
title: 'GNU C Library 2.34 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1667'
author: 开源中国
comments: false
date: Wed, 04 Aug 2021 06:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1667'
---

<div>   
<div class="content">
                                                                    
                                                        <p>GNU C Library 2.34 已发布，GNU C Library 被设计为可移植和高性能的 C 库。它遵循所有相关标准，包括 ISO C11和 POSIX.1-2017，也是已知的最完善的国际化接口之一，广泛应用于 GNU/Linux 系统以及其他使用 Linux 内核的系统。</p> 
<p><strong>部分更新内容</strong></p> 
<ul> 
 <li>所有以前在 libpthread、libdl、libutil 和 libanl 中实现的功能都被整合到 libc 库本身。官方仍然提供了这些 former libraries 的空静态存档，以便在应用程序向前推进时不至于出现太多破坏性的变化，只需要与 libc 链接。</li> 
 <li>在 32 位 x86 等配置上支持 64 位 time_t。目前，Time_t 在这类配置上仍默认为 32 位，但将来可能会改变。</li> 
 <li>在 Linux 上有一个新的 Glibc tunable，允许配置线程栈缓存的大小。</li> 
 <li>添加了_Fork 作为 async-signal-safe fork replacement。</li> 
 <li>在 Linux 上支持 close_range 函数，当在现代版本的 Linux 内核上运行时，可以有效地关闭一系列的文件描述符。</li> 
 <li>支持现代 CPU 功能（如 Arm SVE）的 dynamic sized register sets。</li> 
 <li>支持 ISO C2X function timespec_getres。</li> 
 <li>更多有用的 linker diagnostics。</li> 
 <li>以及一些安全修复和其他错误修复。</li> 
</ul> 
<p>详细内容可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourceware.org%2Fpipermail%2Flibc-alpha%2F2021-August%2F129718.html" target="_blank">更新公告</a>。  </p>
                                        </div>
                                      
</div>
            