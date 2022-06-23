
---
title: 'Linux 5.20将支持XFS的异步缓冲写入和IO_uring以获得性能提升'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0623/340c52262a51ec7.jpg'
author: cnBeta
comments: false
date: Wed, 22 Jun 2022 23:56:50 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0623/340c52262a51ec7.jpg'
---

<div>   
Jens Axboe为Linux
5.20开发周期的功能列表做了补充，当使用IO_uring时，对XFS的异步缓冲写入的支持可以带来一些明显的性能优势。在下一个内核版本中引入的代码可以在使用XFS和IO_uring时实现异步缓冲写入。领导这项工作的Meta公司的Stefan
Roesch解释说：<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0623/340c52262a51ec7.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>"这个补丁系列增加了对同时使用XFS和IO-uring时的异步缓冲写入的支持。目前io-uring只支持慢速路径下的缓冲写入，通过在io工作进程中处理它们。有了这个补丁系列，现在可以支持快速路径中的缓冲写入。为了能够使用快速路径，所需的页面必须在页面缓存中，xfs中所需要的锁可以被立即授予，并且不需要从磁盘上读取额外的块。"</p><p><img src="https://static.cnbetacdn.com/article/2022/0623/9dc78cf06cd8b92.png" title alt="图片.png" referrerpolicy="no-referrer"><br></p><p>顺序写入的性能结果明显提升：从77k到209k IOPS，从314MB/s到854MB/s宽，9600ns到120ns延迟。这些使用XFS的IO_uring数字也使它现在领先于使用XFS的libaio的性能。</p><p>更多细节请看此系列补丁：</p><p><a href="https://lore.kernel.org/io-uring/20220616212221.2024518-1-shr@fb.com/" _src="https://lore.kernel.org/io-uring/20220616212221.2024518-1-shr@fb.com/" target="_blank">https://lore.kernel.org/io-uring/<span class="__cf_email__" data-cfemail="8ab8bab8b8babcbbbcb8bbb8b8b8bba4b8bab8bebfbbb2a7bba7f9e2f8caece8a4e9e5e7">[email protected]</span>/</a><br></p><p>IO_uring和块子系统的维护者Jens Axboe也分享了对其他文件系统的支持，Btrfs预计将成为下一个候选。</p>   
</div>
            