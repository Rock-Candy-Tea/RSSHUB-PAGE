
---
title: 'FreeBSD 13.1-RC6 发布，因修复遗留错误导致延期'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6934'
author: 开源中国
comments: false
date: Sat, 07 May 2022 07:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6934'
---

<div>   
<div class="content">
                                                                                            <p>FreeBSD 13.1 原本计划在上个月发布<a href="https://www.oschina.net/news/192837/freebsd-13-1-rc4-released">最后一个 RC 版本</a>后，本月初推出正式版。然而挥之不去的错误让这个最新的 BSD 操作系统更新产生了额外的候选版本。</p> 
<p>上周发布了 FreeBSD 13.1-RC5，原因是需要修复使用 ZFS+GELI 时的引导失败、符号链接周围的 pkg 问题、更正 libcxxrt 中的 ABI 以及其他问题。预计这将是最后一个候选版本。<br> <br> 现在发布的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.freebsd.org%2Farchives%2Ffreebsd-stable%2F2022-May%2F000762.html" target="_blank">FreeBSD 13.1-RC6</a> 则是作为另一个额外的候选版本，解决了 XHCI 驱动程序在某些情况下无法连接设备的问题。该显著问题已得到修复，并且还将 OpenSSL 升级到 1.1.1o。<br> <br> 鉴于此次更新只有一个值得注意的修复，因此 FreeBSD 13.1-RC6 也许将成为最后一个 RC，然后大约在一周内发布 FreeBSD 13.1 正式版。</p> 
<p><span style="background-color:#ffffff; color:#121212">虽然不是像 FreeBSD 14 这样的大版本更新，但 FreeBSD 13.1 在 64 位架构上默认启用了位置无关的可执行文件 (PIE) 支持、增加用于自动解密 ZFS 数据集的新“zfskeys”服务脚本、引入 NVMe 仿真 Bhyve 管理程序、chroot 现在支持非特权操作、各种 POWER 和 RISC-V 改进、改进 </span>big endian 支持<span style="background-color:#ffffff; color:#121212">、对 HiFive Unmatched RISC-V 开发板的支持、针对上游 OpenZFS 文件系统支持的更新以及许多其他设备驱动程序改进。</span></p>
                                        </div>
                                      
</div>
            