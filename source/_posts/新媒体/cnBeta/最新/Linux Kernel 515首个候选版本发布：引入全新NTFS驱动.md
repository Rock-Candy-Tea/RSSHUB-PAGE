
---
title: 'Linux Kernel 5.15首个候选版本发布：引入全新NTFS驱动'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0904/42a0d81ffed89f0.jpg'
author: cnBeta
comments: false
date: Mon, 13 Sep 2021 02:12:47 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0904/42a0d81ffed89f0.jpg'
---

<div>   
<strong>在为期两周的窗口合并器结束之后，Linux Kernel 5.15 首个候选版本于今天发布。</strong>新分支对内核进行了诸多修改，其中包括将 Paragon NTFS3 作为新的 NTFS 文件系统驱动程序，KSMBD 作为内核内的 SMB3 文件服务器，在上下文切换时选择进入 L1d 缓存刷新等等。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/thumb/article/2021/0904/42a0d81ffed89f0.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0904/42a0d81ffed89f0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">Linux Kernel 5.15 还继续对<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a> M1 进行优化，引入很多针对 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 的改进，以及对<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> DG2/Alchemist 和 XeHP 独立图形的初步支持，以及许多其他新硬件的支持。</p><p style="text-align: left;">Linus Torvalds 在公告中对 Linux 5.15-rc1 写道：</p><blockquote style="text-align: left;"><p style="text-align: left;">所以 5.15 并不是一个特别大的版本，至少在提交的数量上来看是这样的。只有 1 万多个非合并提交，这实际上是我们在 5.x 系列中最小的 RC1。我们通常会在 12-14 万的提交量范围内徘徊。也就是说，计算提交量并不一定是最好的衡量标准，这一次可能尤其如此。</p><p style="text-align: left;">我们有一些新的子系统，其中 NTFSv3 和 ksmbd 最值得关注。因此，当你以“改变的行数”为基础看统计数字时，5.15-rc1 最终看起来更加中庸了。它仍然不像是一个特别大的合并窗口，但也不是最小的窗口。</p></blockquote>   
</div>
            