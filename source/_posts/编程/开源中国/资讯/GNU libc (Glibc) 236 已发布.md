
---
title: 'GNU libc (Glibc) 2.36 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6119'
author: 开源中国
comments: false
date: Thu, 04 Aug 2022 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6119'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0"> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <p style="margin-left:0; margin-right:0">Glibc 是提供系统调用和基本函数的标准 C 语言库，目前 2.36 版本已经发布，主要内容如下：</p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>添加了对 DT_RELR 相对重定位格式的支持，一个新的 ELF 动态标签。</li> 
    <li>在 Linux 上添加 pidfd_open、pidfd_getfd 和 pidfd_send_signal 函数。pidfd 功能提供了对进程的访问，同时避免了传统 Unix 系统上的 PID 重用问题。</li> 
    <li>在 Linux 上增加了 process_madvise 函数。它具有与 madvise 相同的功能，但会更改 pidfd 标识的目标进程。</li> 
    <li>在 Linux 上增加了 process_mrelease 函数。它允许调用者释放垂死进程的内存。</li> 
    <li>添加了“no-aaaa”DNS 存根解析器选项。可使用它来抑制存根解析器进行的 AAAA 查询，包括由基于 NSS 的接口（如 getaddrinfo）触发的 AAAA 查找。</li> 
    <li>在 Linux 上添加 fsopen、fsmount、move_mount、fsconfig、fspick、open_tre 和 mount_setattr。它们是新的 Linux 内核挂载 API 的一部分，允许应用程序更灵活地配置和操作文件系统挂载。</li> 
    <li>localedef 现在接受以 UTF-8 编码的语言环境定义文件。以前，不在 ASCII 范围内的输入字节会导致不可预测的输出。</li> 
    <li>添加了函数 arc4random、arc4random_buf 和 arc4random_uniform ，产生更高质量的随机性。</li> 
    <li>添加了对在 Linux 上运行 LoongArch 的支持，至少需要 binutils 2.38、GCC 12 和 Linux 5.19。</li> 
   </ul> 
   <p style="margin-left:0; margin-right:0">更多内容可查看更新邮件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourceware.org%2Fpipermail%2Flibc-alpha%2F2022-August%2F141193.html" target="_blank">https://sourceware.org/pipermail/libc-alpha/2022-August/141193.html</a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            