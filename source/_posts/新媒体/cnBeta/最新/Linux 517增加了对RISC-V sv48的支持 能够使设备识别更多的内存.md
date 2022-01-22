
---
title: 'Linux 5.17增加了对RISC-V sv48的支持 能够使设备识别更多的内存'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0122/15c0e6b52e1c699.jpg'
author: cnBeta
comments: false
date: Sat, 22 Jan 2022 10:54:58 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0122/15c0e6b52e1c699.jpg'
---

<div>   
<strong>除了Linux 5.17带来了对低成本StarFive
RISC-V平台的支持和其他RISC-V的更新之外，周五还为这个免授权费用的处理器ISA带来了更多的变化。</strong>在Linux
5.17的这些最新RISC-V变化中，最引人注目的是提供sv48支持，RISC-V sv48指的是是允许48位虚拟地址空间支持。<br>
 <p>有了第四层分页表，RISC-V 64位内核现在可以寻址到128TB的虚拟地址空间，对应允许64TB的物理内存。当然，我们现在还没有看到任何高端的RISC-V服务器平台能够支持任何接近现有极限的东西 - 甚至都看不到任何高容量的RAM RISC-V服务器存在，但是这对RISC-V架构未来的发展来说显然是好事。</p><p>sv48在《RISC-V指令集手册》第二卷：特权架构m v1.10中的细节中有介绍：</p><p><a href="https://static.cnbetacdn.com/article/2022/0122/15c0e6b52e1c699.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0122/15c0e6b52e1c699.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></a></p><p>Linux 5.17可以在运行时自动检测对sv48的支持，并在非sv48硬件上回退到3级分页表支持，Linux开始sv48支持的补丁编写工作至少可以追溯到2020年，在被认为可以用于主线之前，已经经历了多轮代码审查。</p><p>Linux 5.17的sv48支持和其他最后的RISC-V补充工作会成为这次合并到Linux内核主线的一部分。</p>   
</div>
            