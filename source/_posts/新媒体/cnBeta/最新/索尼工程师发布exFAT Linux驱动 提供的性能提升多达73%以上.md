
---
title: '索尼工程师发布exFAT Linux驱动 提供的性能提升多达73%以上'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0415/2483775e58d686f.jpg'
author: cnBeta
comments: false
date: Fri, 15 Apr 2022 10:06:41 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0415/2483775e58d686f.jpg'
---

<div>   
Linux内核的exFAT文件系统驱动继续以新的功能、修复和性能改进而很好地成熟起来。值得一提的是，最新的Linux exFAT驱动改进是一个来自索尼工程师的重大性能改进。<br>
 <p>当exFAT文件系统以"dirsync"模式挂载时，这一改进减少了集群归零时的块请求。这种改进的块请求带来了极大的性能提升。</p><p>索尼工程师Yuezhang Mo在一个带有SD卡存储的Arm测试平台上进行了一轮测试，结果表明新的驱动带来了73%甚至更高的性能，exFAT文件是<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>操作系统的用户中非常常用的一种。</p><p><img src="https://static.cnbetacdn.com/article/2022/0415/2483775e58d686f.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>简单的测试案例是创建许多目录，在256KB集群大小的极端情况下，时间改进从11分22秒下降到只有1分39秒。在exFAT的6<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_110018%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">4K</a>B集群大小下，创建1000个目录的时间从3分34秒下降到56秒。</p><p>该补丁本周被列为Linux exFAT文件系统驱动程序开发分支的一部分，本次性能改进也应该在今年夏天登陆Linux 5.19内核。</p><p><strong>了解更多：</strong></p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/linkinjeon/exfat.git/commit/?h=dev&id=1d404b899e322a3fed5d7af243d83bb9e71b1b78" _src="https://git.kernel.org/pub/scm/linux/kernel/git/linkinjeon/exfat.git/commit/?h=dev&id=1d404b899e322a3fed5d7af243d83bb9e71b1b78" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/linkinjeon/exfat.git/commit/?h=dev&id=1d404b899e322a3fed5d7af243d83bb9e71b1b78</a><br></p>   
</div>
            