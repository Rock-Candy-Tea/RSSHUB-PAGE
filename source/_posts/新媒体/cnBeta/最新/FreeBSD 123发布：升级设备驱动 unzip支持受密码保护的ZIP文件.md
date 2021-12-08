
---
title: 'FreeBSD 12.3发布：升级设备驱动 unzip支持受密码保护的ZIP文件'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1208/3d0363755456d74.webp'
author: cnBeta
comments: false
date: Wed, 08 Dec 2021 03:25:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1208/3d0363755456d74.webp'
---

<div>   
虽然 FreeBSD 13 是目前最新稳定版，<strong>但这个开源 BSD 系统今天为 N-1 系列发布了 FreeBSD 12.3 版本。</strong>FreeBSD 13.0 于今年 4 月份发布，而对于那些还没有迁移到新系列的用户来说，FreeBSD 12.3 是 FreeBSD 12 系列的最新和最好的版本。<br>
 <p style="text-align: left;">FreeBSD 12.3 对各种网络驱动进行了更新，对其采用的各种开源包进行了更新，对应用程序进行了更新改进，对内核错误进行了修复，以及其他大量的修正。</p><p style="text-align: left;">在内核设备驱动方面，一些值得一提的改进包括：Zen 3 / Ryzen 4000 APU / Renoir / Van Gogh 在 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>temp 中的温度监控，Zen 3 对 AMDSMN 的支持，对 Mikrotik 10G/25G 网络设备的支持，对 Intel Killer Wireless-AC 1550i 的支持，对<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://asus.jd.com/" target="_blank">华硕</a> WL-167G V3 的支持，以及对 Intel 100 Series / C230 Series AMT 的支持。</p><p style="text-align: left;">用户空间变化方面，值得一提的改进包括：Bhyve 修正了其 NVMe 模拟中的大 IO 处理，freebsd-update 更新了一个新的标志以支持 jails，fstyp 现在可以检测 exFAT 文件系统，growfs 现在可以在读写安装的文件系统上操作，unzip 现在支持密码保护的档案，等等。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1208/3d0363755456d74.webp" alt="ju1esyqt.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">FreeBSD 12.3 将受密码保护的 ZIP 文件处理带到了它的 unzip 工具中......(当然，p7zip 和替代品已经在 FreeBSD Ports 中作为一种替代手段来处理 FreeBSD 上受密码保护的 ZIP。)</p><p style="text-align: left;">FreeBSD 12.3 还引入了 bc 5.0, OpenSSL 1.1.1i, SQLite 3.35.5, Subversion 1.14.1 LTS 等。FreeBSD 12.3 的 Boot Loader 增加了对从内存盘启动的支持，对从没有功能的 ZFS 池启动的支持，以及对其他 ZFS 功能的支持。</p><p style="text-align: left;">关于FreeBSD 12.3变化的下载和更多信息请访问<a href="https://www.freebsd.org/releases/12.3R/announce/" target="_blank">FreeBSD.org</a>。</p>   
</div>
            