
---
title: 'Spectre V1 SWAPGS缓解措施部分失效后重新上线 代码来自阿里巴巴工程师'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1205/6e36f5b00742431.jpg'
author: cnBeta
comments: false
date: Sun, 05 Dec 2021 13:25:26 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1205/6e36f5b00742431.jpg'
---

<div>   
今天晚些时候发布的Linux 5.16-rc4内核的"x86/紧急"变更集有一些Spectre
V1的修复，因为去年的内核提交导致其SWAPGS处理方面的部分混乱，这些修正也将可能被回传到相关的稳定版内核系列。<strong>在阿里巴巴工程师Lai
Jiangshan的帮助下，一些围绕Spectre V1 SWAPGS缓解的重要修正今天在主线内核中登陆。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1205/6e36f5b00742431.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>修正内容首先是对paranoid_entry路径中的内核条目SWAPGS的栅栏缺失的补丁。去年对主线内核的修改导致Spectre V1 SWAPGS缓解措施的退步，因为该路径中缺少栅栏。想了解补丁所有的细节可以访问这里：</p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?h=x86/urgent&id=1367afaa2ee90d1c956dfc224e199fcb3ff3f8cc" _src="https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?h=x86/urgent&id=1367afaa2ee90d1c956dfc224e199fcb3ff3f8cc" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?h=x86/urgent&id=1367afaa2ee90d1c956dfc224e199fcb3ff3f8cc</a><br></p><p>关于Linux内核的Spectre V1 SWAPGS缓解处理的更多背景信息在2019年的原始代码中概述，当时在CVE-2019-1125公开后，Spectre V1 SWAPGS缓解措施被合并了。</p><p>今天的拉动请求的一部分也是对使用正确的栅栏宏的这个修复。现在，正确的栅栏宏被用于确保尝试行为被阻止。</p><p>Lai Jiangshan今天的第三个补丁对SWAPGS路径上发现的潜在堆栈clobbering也有一个重要的Xen修复：</p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?h=x86/urgent&id=5c8f6a2e316efebb3ba93d8c1af258155dcf5632" _src="https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?h=x86/urgent&id=5c8f6a2e316efebb3ba93d8c1af258155dcf5632" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?h=x86/urgent&id=5c8f6a2e316efebb3ba93d8c1af258155dcf5632</a></p><p>SWAPGS栅栏问题和其他x86修复问题今天已经作为该请求的一部分被送入。Spectre V1 SWAPGS漏洞/缓解措施影响了Ivy Bridge和较新的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>CPU，Alder Lake仍然依赖SWAPGS/usercopy屏障。</p>   
</div>
            