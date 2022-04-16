
---
title: '华为工程师为Linux AArch64开发UEFI镜像内存支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0416/bc90f73dbdc9011.jpg'
author: cnBeta
comments: false
date: Sat, 16 Apr 2022 10:56:22 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0416/bc90f73dbdc9011.jpg'
---

<div>   
自2015年以来，Linux内核已经支持x86/x86_64的UEFI镜像内存功能，而现在华为正在努力为AArch64添加该功能。UEFI允许设置基于地址范围的部分内存镜像，这在UEFI
2.5规范中就已经开始了。这种UEFI内存镜像可以用于服务器的冗余/可靠性目的。<br>
 <p>符合UEFI规范的AArch64硬件也可以支持它，但直到现在还没有在AArch64/ARM64上设置Linux内核支持。</p><p>华为工程师Wupeng Ma周四发出了最新的补丁，实现了对AArch64硬件的这种Linux镜像内存支持。根据平台的设置，服务器通常可以提供完整的镜像（为镜像保留50%）或部分镜像，通常为10~20%，如果低于/高于4GB还可以手动选择，甚至由操作系统决定镜像的内存地址范围。</p><p><img src="https://static.cnbetacdn.com/article/2022/0416/bc90f73dbdc9011.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>那些对Arm 64位Linux服务器的镜像内存支持感兴趣的人可以在Linux内核邮件列表中找到当前的补丁系列：</p><p><a href="https://lore.kernel.org/lkml/20220414101314.1250667-1-mawupeng1@huawei.com/" _src="https://lore.kernel.org/lkml/20220414101314.1250667-1-mawupeng1@huawei.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="0537353737353134313435343634312b343730353333322834286864727075606b6234456d706472606c2b666a68">[email protected]</span>/</a><br></p>   
</div>
            