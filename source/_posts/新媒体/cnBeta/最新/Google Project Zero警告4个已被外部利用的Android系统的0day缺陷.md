
---
title: 'Google Project Zero警告4个已被外部利用的Android系统的0day缺陷'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0523/d5da25f37dd5690.png'
author: cnBeta
comments: false
date: Sun, 23 May 2021 03:36:23 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0523/d5da25f37dd5690.png'
---

<div>   
Google于月初公布了5月的Android安全性公告，修补约50个安全漏洞，<strong>不过，本周Google Project
Zero的安全研究人员Maddie
Stone周三（5/19）通过Twitter表示，Google已更新了该公告，特别注明有4个漏洞已经遭到外部利用。</strong><br>
<p>相关漏洞皆存在于GPU中，包含两个源自高通GPU的CVE-2021-1905与CVE-2021-1906，另外两个则是Arm Mali GPU中的CVE-2021-28663与CVE-2021-28664。</p><ul class=" list-paddingleft-2"><li><p>CVE-2021-1905：高通 - 由于对多个进程的内存映射处理不当，可能会出现 UAF。</p></li><li><p>CVE-2021-1906：高通 - 对失败时的地址取消注册处理不当，可能导致新的 GPU 地址分配失败。</p></li><li><p>CVE-2021-28663：ARM - Mali GPU 内核驱动程序允许对 GPU 显存进行不适当的操作。非特权用户可对 GPU 显存进行不当操作，以进入 "UAF" 情景，并可能获得 root 权限，并泄露信息。</p></li><li><p>CVE-2021-28664：ARM - Mali GPU 内核驱动程序将 CPU RO 页面提升为可写。非特权用户可以获得对只读内存的写入权限，并可能获得 root 权限，破坏内存和修改其他进程的内存。</p></li></ul><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/0523/d5da25f37dd5690.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>研究人员Maddie Stone表示说这4个漏洞已经被外部利用，更新的Android公告则相对保守，表示相关漏洞可能已受到有限的目标式攻击。</p><p>根据高通的说明，CVE-2021-1905属于释放后使用漏洞，源于Android无法妥善处理多程序内存映像；CVE-2021-1906则是在绘图未动作时检测到错误状况，因无法处理注销地址的错误，而造成新GPU位置分配的失败。</p><p>ARM方面则表示，CVE-2021-28663漏洞出现在其核心驱动程序允许于GPU内存的不当操作，未获特权的使用者可因此而进入释放后使用场景，进而取得最高权限，或造成信息揭露。CVE-2021-28664则可把CPU只读页面变成可写入，允许未获特权的用户写入只读存储器，并取得最高权限、破坏内存或是窜改其它程序的内存。</p><p>不管是Google、高通或ARM，皆未公布相关漏洞的被利用场景或黑客目前是否有攻击目的。</p>   
</div>
            