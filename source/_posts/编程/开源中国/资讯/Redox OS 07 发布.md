
---
title: 'Redox OS 0.7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4355'
author: 开源中国
comments: false
date: Sat, 30 Apr 2022 07:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4355'
---

<div>   
<div class="content">
                                                                                            <p>Redox 是一个用编程语言 Rust 编写的类似 Unix 的微内核操作系统，它的重点是安全、稳定和性能。Redox 的灵感来自先前的内核和操作系统，如 SeL4、MINIX、Plan 9 和 BSD。它与 GNU 和 BSD 类似，但用一种内存安全的语言编写，是在 MIT 许可下发布的开源软件。</p> 
<p>Redox OS 0.7 正式发布，更新内容如下：</p> 
<ul> 
 <li>引导程序：引导程序被完全重写，因此 BIOS 和 UEFI 版本都共享大部分相同的代码，并且都主要用 Rust 编写。这使得硬件支持大大改善，并允许 RedoxFS 得到改进。</li> 
 <li>Kernel：内核中加入了一些修复和新功能，并删除了一些代码。硬件支持得到改善，性能也得到提高。 
  <ul> 
   <li>初步增加了对 aarch64 的支持</li> 
   <li>所有的路径现在都被要求是 UTF-8 的，并且内核强制执行这个要求</li> 
   <li>CPU 特定的变量使用 GS 寄存器，由此带来了各种改进</li> 
   <li>所有的物理内存都被映射了，递归分页已经被移除</li> 
   <li>ACPI AML 代码被转移到 acpid，一个新的用户空间守护程序。</li> 
   <li>重写了内联汇编，以便在未来的编译器中保持稳定</li> 
   <li>Initfs 被移到了一个新的文件中，这极大地改善了封装。</li> 
   <li>许多内核问题已被修复</li> 
  </ul> </li> 
 <li>redoxfs：RedoxFS 被重写为写时复制文件系统，具有事务性更新和元数据和数据的签名。这种设计大大增加了 RedoxFS 的可靠性。此外，还增加了透明加密功能，如果有硬件加速的话使用 AES。引导程序现在使用与操作系统相同的驱动代码，这使得引导程序可以解锁文件系统，允许内核和 initfs 被文件系统加密和散列</li> 
 <li>relibc：Relibc 有不断的各种变化，使更多的软件得到了移植，同时也修复了许多 C 程序和库中的问题</li> 
 <li>rust：现在有了一个可以在 Redox 操作系统上运行的 rustc 版本。后续还有一些工作要做，以提高性能并确保 cargo 可以从 Redox OS 内部运行在 Redox OS 项目上</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redox-os.org%2Fnews%2Frelease-0.7.0%2F" target="_blank">https://www.redox-os.org/news/release-0.7.0/</a></p>
                                        </div>
                                      
</div>
            