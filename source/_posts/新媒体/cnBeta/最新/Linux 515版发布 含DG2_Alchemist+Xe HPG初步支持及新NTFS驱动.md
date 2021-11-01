
---
title: 'Linux 5.15版发布 含DG2_Alchemist+Xe HPG初步支持及新NTFS驱动'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1101/ebd090184187fc1.webp'
author: cnBeta
comments: false
date: Sun, 31 Oct 2021 23:41:40 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1101/ebd090184187fc1.webp'
---

<div>   
Linus Torvalds在万圣节假期并没有休息，而是按期发布了Linux
5.15，也没有如之前传闻的那样将内核稳定版的发布再推迟一周。Linux
5.15有许多突出的变化，<strong>包括引入DAMON，来自Paragon的新NTFS文件系统驱动程序，Xe
HPG和DG2/Alchemist的首批支持代码，面向AMD Zen 3 APU的温度监控支持，以及更多。</strong><br>
 <p><strong><img src="https://static.cnbetacdn.com/article/2021/1101/ebd090184187fc1.webp" title alt="linux515lts-scaled.webp" referrerpolicy="no-referrer"></strong></p><p><strong>内核邮件列表中刊出了Linus Torvalds发布的简短的5.15版本公告：</strong></p><p><a href="https://lore.kernel.org/lkml/CAHk-=wjfbfQobW2jygMvgfJXKmzZNB=UTzBrFs2vTEzVpBXA4Q@mail.gmail.com/T/#u" _src="https://lore.kernel.org/lkml/CAHk-=wjfbfQobW2jygMvgfJXKmzZNB=UTzBrFs2vTEzVpBXA4Q@mail.gmail.com/T/#u" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="ffbcbeb794d2c28895999d99ae909da8cd958698b2899899b5a7b49285a5b1bdc2aaab85bd8db98ccd89abba85a98fbda7becbaebf929e9693d198929e9693d19c">[email protected]</span>om/T/#u</a><br></p><p><strong>您可以在这里参看Linux 5.15功能列表，以更全面地了解这个周期的令人兴奋的变化：</strong></p><p>处理器</p><p>- <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> PDTDMA驱动在开发了两年后被合并，以利于AMD EPYC服务器处理器。</p><p>- 为RISC-V扩展了堆栈随机化，并为RISC-V连接了其他功能。</p><p>- 在TCC驱动中支持Alder Lake。</p><p>- 一个重要的AMD笔记本电脑暂停/恢复修复，惠及各种型号。</p><p>- KVM现在默认为新的x86 TDP MMU，并增加了AMD SVM 5级分页。</p><p>- AMD Zen 3 APU温度监控支持终于完成。</p><p>- Yellow Carp APU温度监控支持。</p><p>- 合并了AMD SB-RMI驱动，以利于服务器的使用情况，如基于Linux的OpenBMC软件栈。</p><p>- 优化了AMD CPU的C3入口处理。</p><p>- 一些IRQ内核代码的改进，使Intel 486时代的硬件受益。</p><p>- 一个AVX2优化的SM4密码实现。</p><p>图形</p><p>- 许多新的RDNA2 PCI ID指向一个可能的RDNA2显卡更新。</p><p>- AMD Cyan Skillfish图形支持。</p><p>- 对<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>XeHP和DG2/Alchemist独立图形的初步支持。</p><p>- 移除英特尔Gen10 / Cannon Lake图形支持。</p><p>- 在DRM/KMS驱动中还有许多其他图形改进。</p><p>存储/文件系统。</p><p>- 合并了新的NTFS驱动，这是对现有NTFS驱动的一大改进。这个新驱动程序是由Paragon软件公司创建的"NTFS3"驱动程序。</p><p>- <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://samsung.jd.com/" target="_blank">三星</a>的KSMBD被合并为内核内SMB3文件服务器。</p><p>- OverlayFS 具有更好的性能，并复制了更多的属性。</p><p>- FUSE 现在允许挂载一个活动设备。</p><p>- 对 F2FS 进行了性能优化。</p><p>- 通过 NFS 客户端代码在多个 NIC 上共享连接。</p><p>- 针对 EXT4 的新优化。</p><p>- 对 XFS 的大量改进。</p><p>- 对Btrfs的降级RAID模式支持和性能改进。</p><p>- Btrfs支持IDMAPPED挂载和Btrfs FS-VERITY支持。</p><p>- Linux 5.15 I/O可以达到每核~3.5M IOPS。</p><p>- 应 systemd 开发者要求，支持全局县/磁盘事件的序列号。</p><p>- 删除了 LightNVM 子系统。</p><p>- 修复了 Linux 的软盘驱动代码。</p><p>- 其他块子系统的改动。</p><p>Linux Kernel 5.15版本的发布也意味着Linux内核现在开始进入非常令人兴奋的合并窗口。</p>   
</div>
            