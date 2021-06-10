
---
title: 'Linux Kernel 5.14将移除已淘汰的RAW驱动'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0610/c4031a3a9f995a3.jpg'
author: cnBeta
comments: false
date: Thu, 10 Jun 2021 03:29:26 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0610/c4031a3a9f995a3.jpg'
---

<div>   
Linux 中的 RAW 驱动（RAW_DRIVER）主要用于提供对块设备的直接 I/O 访问，不过即将推出的 Linux Kernel 5.14 内核中将移除该驱动。该驱动原本计划在 2000 年年中的时候就要废弃，而且在更早的时候就已经被阻止使用了。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0610/c4031a3a9f995a3.jpg" alt="4thomk30.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">RAW 驱动允许 Linux 内核直接向块设备提供无缓冲的 I/O，但是它已经有十多年没有被使用了，因为在打开块设备时使用 O_DIRECT 标志可以实现同样的行为。原始模式下的块设备是通过/dev/raw/暴露的。虽然O_DIRECT一直是首选的方法，但一些传统的工作负载没有得到维护/无法直接使用 O_DIRECT方法，导致 RAW 驱动到现在才被淘汰。</p><p style="text-align: left;">现在，过去一周排队进入 char-misc-next 终于删除了 RAW 驱动。在这一点上，任何影响都应该是相当小的，而且是一个惊喜，但只是更多的旧内核残渣最终被移除，以专注于现代接口。</p>   
</div>
            