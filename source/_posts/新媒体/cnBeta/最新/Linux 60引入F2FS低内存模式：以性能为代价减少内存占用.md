
---
title: 'Linux 6.0引入F2FS低内存模式：以性能为代价减少内存占用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0813/0751846d9f9eff7.webp'
author: cnBeta
comments: false
date: Sat, 13 Aug 2022 00:26:26 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0813/0751846d9f9eff7.webp'
---

<div>   
Flash Friendly File-System (F2FS) 对于闪存设备，尤其是固态硬盘和移动硬盘来说，依然是强大的文件系统选项。<strong>在 Linux 6.0 中，此文件系统驱动程序还有更多改进，引入了包括低内存模式在内的一些新功能。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0813/0751846d9f9eff7.webp" alt="u054fu43.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">低内存模式在低端 Android <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>以及内存容量不充裕的设备上，能够调整文件系统行为以减少内存占用。但是作为牺牲的是，F2FS 会影响运行性能。带有 Linux 6.0 的 F2FS 在其原子写入操作、前台垃圾收集时间、修复等方面也有所改进。</p><p style="text-align: left;">F2FS 维护者 Jaegeuk Kim 将这个周期的工作总结为：</p><p style="text-align: left;">在这个周期中，我们主要修复了一些不恰当地操纵每个文件压缩标志的极端情况。而且，我们发现 f2fs 在设置区域容量时错误地计算了一个部分中的有效块，因此，通过额外的 sysfs 条目来修复它以便于检查它。最后，这个系列包括几个关于新的原子写入支持的补丁，例如几个错误修复和重新添加我们在之前版本中错误删除的 atomic_write_abort 支持。</p>   
</div>
            