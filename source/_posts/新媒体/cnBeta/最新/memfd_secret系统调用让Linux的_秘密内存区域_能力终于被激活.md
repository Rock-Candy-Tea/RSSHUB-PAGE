
---
title: 'memfd_secret系统调用让Linux的_秘密内存区域_能力终于被激活'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Tue, 13 Apr 2021 07:38:36 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
<strong>在一年多的打磨过程中，开发人员一直在实现Linux上创建秘密内存区域的能力，这意味着运用这一系统调用后，创建的“秘密内存区域”只有各自的进程才能访问，而不会映射给其他进程或内核页表。</strong>现在，这个
"memfd_secret"系统调用终于在Linux-Next中实现，而且看起来可以合并到内核主线了。<br>
<p>memfd_secret系统调用是在Linux上创建“秘密内存区域”的新接口，用于用户空间的OpenSSL等用例，尤其是可以用于存储私钥，从而减少私钥在系统内存中暴露的可能性，且没有任何其他硬件加密方法的支持。</p><p>但是为了确保这个memfd_secret功能不被滥用，除非在启动时通过一个特殊的选项，否则这个在系统中创建秘密内存区域的功能默认是被禁用的。秘密内存功能和memfd_secret系统调用被隐藏在 "secretmem_enable"选项后面，至少目前是这样。</p><p>关于memfd_secret系统调用的新消息是，它已经在周一通过Andrew Morton的代码进入了linux-next.git。鉴于此，我们有可能在即将到来的 Linux 5.13 周期中看到这个新的秘密内存区域系统调用会出现，至少这个功能也正在向主线靠近。</p><p><strong>关于系统调用和 "秘密 "内存区域的更多细节可以通过这个页面找到：</strong></p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/commit/?id=72101855fb9a2b3cd72c051791609a217c4a6281" _src="https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/commit/?id=72101855fb9a2b3cd72c051791609a217c4a6281" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/commit/?id=72101855fb9a2b3cd72c051791609a217c4a6281</a></p><p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a> </p>   
</div>
            