
---
title: 'Linux 5.15迎来性能改进 支持Btrfs RAID退化等新功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0901/08935dc5f2c89dd.png'
author: cnBeta
comments: false
date: Wed, 01 Sep 2021 02:20:47 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0901/08935dc5f2c89dd.png'
---

<div>   
David Sterba 在本周一的 Linux 内核邮件公告中称：<strong>Btrft 文件系统的更新，现已登陆 Linux 5.15 主线，其中包含了一些激动人心的新功能和改进。</strong>今年夏天，开发团队一直忙于为 Linux 5.15 准备一系列相当活跃的变更，且最终于今日将其合并到了 Linux 5.15 Git 中。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0901/08935dc5f2c89dd.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://lore.kernel.org/lkml/cover.1630327914.git.dsterba@suse.com/" target="_self">LKML</a>）</p><p>主要变化如下：</p><blockquote><p>● 支持 FS-VERITY 内核层，允许对只读文件进行透明的完整性和真实性保护。此前该功能已适用于 EXT4 和 F2FS，现也适用于 Btrfs 文件系统。</p><p>● 支持 IDMAPPED 挂载，且允许公开不同所有权的相同文件或目录，设计用例涵盖了从容器到 systemd-home 。该功能在 Linux 5.12 中首次亮相，但当时仅适用于 FAT 和 EXT4 文件系统。</p><p>● Btrfs 迎来对 RAID0 和 RAID10 模式的‘退化’（Degenerated）支持，在本机 Btrfs RAID 生成模式下，其分别可在 1 / 2 个设备上运行，而不需要 2 / 4 个设备。在保留配置文件类型的同时，其有助于用户从阵列中转换或移除设备。</p><p>● 预读代码变更，支持全发送加速，实测可带来 11% 的性能提升。</p><p>● 支持批量延迟，以加快诸多文件的创建速度。</p><p>● 支持 Fsync/tree-log 加速，示例工作负载的吞吐量和运行时间均有 2% 的改进。重命名的锁定争用也较低，吞吐量提升 4%，且将延迟降低了 30% 。</p><p>● 继续开展子页面支持、实验性支持带 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_110018%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">4K</a> 扇区的 64K 页系统的写入。</p><p>● 改进刷新逻辑，以及其它常规的修复和底层增强。</p></blockquote>   
</div>
            