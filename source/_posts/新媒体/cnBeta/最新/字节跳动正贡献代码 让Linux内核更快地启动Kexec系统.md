
---
title: '字节跳动正贡献代码 让Linux内核更快地启动Kexec系统'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0725/f3c6542c3f5d9ee.webp'
author: cnBeta
comments: false
date: Mon, 25 Jul 2022 11:44:10 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0725/f3c6542c3f5d9ee.webp'
---

<div>   
作为TikTok背后的中国公司，ByteDance（字节跳动）在过去几年中一直致力于许多Linux内核的优化，他们最近的工作是加快内核的Kexec重启。由于公司庞大的服务器群需要为TikTok和其他应用程序提供动力，他们必须尽其所能从其服务器的启动/重启时间中减少几毫秒，这就其对Linux优化的目的：最新的Kexec重启系列补丁。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0725/f3c6542c3f5d9ee.webp" title alt="image.webp" referrerpolicy="no-referrer"></p><p>像许多其他大型组织一样，ByteDance依靠Kexec重启来转移到新的内核，无论是出于安全、维护还是优化的原因。通过使用Kexec，他们避免了服务器POST'ing和其他任务的更长的停机时间。但是，即使使用Kexec来切换到一个新的内核，以避免硬件初始化和引导程序，仍然可能带来太长的停机时间。</p><p>通过今天的"faster kexec reboot"系列补丁，他们将削减的目标定在大约500毫秒，这些时间可以被优化掉，使从机器Kexec到启动内核功能的时间降低到只剩下15毫秒。</p><p>提出的优化措施包括在x86/x86_64上支持未压缩的内核，以加快启动过程，而不是作为一个压缩的内核镜像，避免在内核未压缩时进行内存拷贝，并重新使用崩溃的内核保留内存进行正常的kexec操作。这样做之后，仅仅在x86上启用未压缩的内核，就使其启动时间减少了150毫秒，但意味着内核镜像的大小从8.5M猛增到53M。</p><p>这个补丁系列触及了大约100行Linux内核代码，字节跳动方面现在希望在上游将Kexec重启时间缩短半秒左右。</p><p><strong>了解更多：</strong></p><p><a href="https://lore.kernel.org/lkml/20220725083904.56552-1-huangjie.albert@bytedance.com/" _src="https://lore.kernel.org/lkml/20220725083904.56552-1-huangjie.albert@bytedance.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="6d5f5d5f5f5d5a5f585d555e545d5943585b58585f405c4005180c030a070408430c010f081f192d0f141908090c030e08430e0200">[email protected]</span>/</a><br></p>   
</div>
            