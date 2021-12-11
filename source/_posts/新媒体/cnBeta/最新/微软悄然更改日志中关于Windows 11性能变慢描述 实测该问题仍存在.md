
---
title: '微软悄然更改日志中关于Windows 11性能变慢描述 实测该问题仍存在'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1211/6258e5588a3f2f1.jpg'
author: cnBeta
comments: false
date: Sat, 11 Dec 2021 00:49:39 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1211/6258e5588a3f2f1.jpg'
---

<div>   
微软悄然更新了 Windows 11 Build 22000.348（KB5007262）累积更新的日志，<strong>现在引入了“NVME、SSD、hard disk”等术语，而之前更新日志提到的是“NTFS”。</strong><br>
 <p style="text-align: left;">日志的更改可能和近期多家媒体报道 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 系统中的 NVMe <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a> 速度变慢影响有关。但是遗憾的是，目前无法确定微软是何时进行修改，因为微软并未在 KB5007262 日志中提及任何更新日期。</p><p style="text-align: left;">此前的更新日志写道</p><blockquote style="text-align: left;"><p style="text-align: left;">修复了当你启用更新序列号（USN）日志时影响 NTFS 的问题。NTFS 每次执行写操作时都会执行不必要的操作，这影响了 I/O 性能。</p></blockquote><p style="text-align: left;">而现在更新的日志写道</p><blockquote style="text-align: left;"><p style="text-align: left;">修复了一个问题，即每次发生写操作时执行不必要的操作，会影响 Windows 11 上所有磁盘（NVMe、SSD、硬盘）的性能。这个问题只在启用 NTFS USN日 志时发生。注意，USN 日志总是在 C：磁盘上启用。</p></blockquote><p style="text-align: left;">微软可能在术语上做了这个改变，也许是为了让读者更容易理解它已经解决了这个问题，因为大多数人可能更熟悉NVMe或SSD这些词，而不是NTFS。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1211/6258e5588a3f2f1.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1211/6258e5588a3f2f1.jpg" alt="6vb0i9i8.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">然而，与微软的说法相反，科技媒体 NeoWin 在 WD SN520 测试了推荐版本 22000.348，但问题依然存在。尽管这个问题有可能在其他系统上得到解决。虽然AS SSD没有产生任何显著的效果，但CrystalDiskMark似乎显示，与Windows 10相比，随机写入量下降了很多。</p>   
</div>
            