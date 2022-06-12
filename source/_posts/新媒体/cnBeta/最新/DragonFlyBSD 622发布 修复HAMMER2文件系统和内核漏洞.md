
---
title: 'DragonFlyBSD 6.2.2发布 修复HAMMER2文件系统和内核漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/06/ef018324dfed3fb.png'
author: cnBeta
comments: false
date: Sat, 11 Jun 2022 23:51:18 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/06/ef018324dfed3fb.png'
---

<div>   
DragonFlyBSD 6.2最早在2022年一月份推出，包括AMDGPU Linux内核驱动移植，HAMMER2改进，NVMM管理程序移植，以及其他改进。本周末发布的是DragonFlyBSD 6.2.2，在稳定代码库的基础上进行了各种错误修复。<br>
 <p>6.2系列对带有NVMM的type-2管理程序的硬件支持，加入<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>gpu驱动，远程安装HAMMER2卷的试验性能力，以及其他许多变化。</p><p>DragonFlyBSD 6.2.2主要是对BSD操作系统默认使用的HAMMER2原始文件系统进行了修复。HAMMER2的修复范围包括解决可能出现的死机问题，被删除的文件在文件系统中卸载前依然迟滞的错误。</p><p>DragonFlyBSD 6.2.2还解决了TMPFS中可能出现的readdir()竞争问题，并有多种不同的内核修复。另外还有更新的时区数据作为维护性更新。</p><p><a href="https://static.cnbetacdn.com/article/2022/06/ef018324dfed3fb.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/06/ef018324dfed3fb.png" referrerpolicy="no-referrer"></a></p><p><strong>有关DragonFlyBSD的相关介绍：</strong><br></p><p>DragonFly与其他BSD派生的系统和Linux属于同一类操作系统，它与其他BSD操作系统共享祖先代码。DragonFly为BSD基础提供了另一种可能，使其向完全不同于FreeBSD、NetBSD和OpenBSD系列的方向发展。</p><p>DragonFly包含了许多有用的功能，使其区别于其他同类的操作系统。</p><p>最突出的是HAMMER，一种现代高性能文件系统，内置镜像和历史访问功能。</p><p>虚拟内核提供了将一个完整的内核作为用户进程运行的能力，以达到管理资源或加速内核开发和调试的目的。</p><p>DragonFlyBSD内核为SMP使用了几种同步和锁定机制。自从项目开始以来，大部分的工作都是在这个领域进行的。它故意简化某些锁的类别，使更多的子系统不容易出现死锁，以及使用专门为SMP设计的算法重写几乎所有的原始代码库，这些都带来了一个非常稳定的，高性能的内核，能够有效地使用所有的CPU，内存和I/O资源的投入。</p><p>DragonFlyBSD在内核中几乎没有瓶颈或锁的争夺。几乎所有的操作都能在任何数量的cpu上并发运行。多年来，VFS支持基础设施（namecache，vnode cache），用户支持基础设施（uid，gid，进程组，会话），进程和线程基础设施，存储子系统，网络，用户和内核内存分配和管理，进程fork，exec和exit/teardown，时间保持，以及内核设计的所有其他方面都是以极端SMP性能为目标重写的。</p><p>DragonFly利用交换空间来缓存文件系统数据和元数据，从而独特地利用了价格低廉的固体存储设备（<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a>）的广泛存在。这一功能通常被称为"交换缓存"，只需很小的硬件投资，就可以大大提升服务器和工作站的工作负荷。</p><p>DragonFly存储栈包括强大的、本地编写的AHCI和NVME驱动，通过DEVFS的稳定设备名称，以及用于可靠卷管理和加密的Device Mapper的部分实现。</p><p>其他一些对系统管理员特别有用的功能有：一个高性能和可扩展的TMPFS实现，一个极其高效的NULLFS，不需要目录或文件节点的内部复制，原生编写的DNTPD（ntp客户端）使用全线拦截和标准偏差求和来保持高度精确的时间，以及DMA，旨在为不需要postfix或sendmail等更广泛的邮件服务的系统操作员提供低开销邮件服务。</p><p>DragonFly利用dports系统提供了数以千计的源代码和二进制形式的应用程序。这些功能和更多的功能结合在一起，使DragonFly成为一个现代的、有用的、友好的和熟悉的类UNIX操作系统。</p><p><a href="https://static.cnbetacdn.com/article/2022/06/3c868c9a5b224cf.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/06/3c868c9a5b224cf.png" referrerpolicy="no-referrer"></a></p><p>构成DragonFlyBSD 6.2.2的20多个稳定版错误修正列表可以在提交列表中找到：</p><p><a href="https://lists.dragonflybsd.org/pipermail/commits/2022-June/820953.html" _src="https://lists.dragonflybsd.org/pipermail/commits/2022-June/820953.html" target="_blank">https://lists.dragonflybsd.org/pipermail/commits/2022-June/820953.html</a><br></p><p>这个DragonFlyBSD稳定版可以从DragonFlyBSD.org下载：</p><p><a href="https://www.dragonflybsd.org/" _src="https://www.dragonflybsd.org/" target="_blank">https://www.dragonflybsd.org/</a></p>   
</div>
            