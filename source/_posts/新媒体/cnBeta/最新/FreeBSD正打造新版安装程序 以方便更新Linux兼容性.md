
---
title: 'FreeBSD正打造新版安装程序 以方便更新Linux兼容性'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0726/7f0315aee53f41e.jpg'
author: cnBeta
comments: false
date: Mon, 26 Jul 2021 03:07:36 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0726/7f0315aee53f41e.jpg'
---

<div>   
<strong>在 2021 年 2 季度报告中，FreeBSD 团队详细介绍了他们从 4 到 6 月内的各项开发活动。</strong>可知在这个忙碌的季度，他们推出了 FreeBSD 13.0，并在诸多大型开发工作中取得了相应的进展。<br>
<p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/0726/7f0315aee53f41e.jpg" referrerpolicy="no-referrer"></p><p>（1）为新版 FreeBSD 安装程序引入了“粗略的概念验证”，其旨在成功取代当前的 bsdinstall 。</p><blockquote><p>这款实验性质的安装程序，采用了基于 Web 的安装界面，意味其能够通过浏览器轻松运行。除了在要安装 FreeBSD 的本地机器上安装运行，也可在远程系统上开启。</p><p>与当前的安装程序相比，Web 安装器拥有更加简洁和易于使用的现代用户界面。同时得益于更加模块化的设计，脚本化 / 自动化安装也更加轻松。</p></blockquote><p>（2）FreeBSD 基金会促进了 Bhyve 中的 VirtIO 1.0 现代支持、VMM 中的 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> PCI 直通修复、UFS 错误修复、基于 ptrace(PT_COREDMP) 的按需内核转储、以及通用内核调试等改进。</p><p>（3）正参考 Linux 5.7 内核的图形驱动程序状态，更新其 drm-kmod 图形驱动程序代码，以支持更新的 AMD Radeon 和 Intel 图形硬件。</p><p>（4）针对 FreeBSD 的 Linux 兼容层，带来了各项改进，以便在 FreeBSD 上运行 Linux 二进制文件。</p><p>（5）FreeBSD 工程团队发布了 FreeBSD 13.0-RELEASE 。</p><p>（6）Ports 现拥有超过 44200 个可用端口 / 包。</p><p>（7）致力于在 FreeBSD 上为 OpenGL 的中立调度层使用 libglvnd (GLVND)，以在处理不同的驱动程序堆栈时（比如 Mesa / NVIDIA）获得与在 Linux 上类似的益处。</p><p>（8）作为 FreeBSD 驱动的桌面操作系统，helloSystem 项目进展顺利。即将发布新版本，并向着下一个版本迈进。</p><p>感兴趣的朋友，可移步至 FreeBSD 官网（<a href="https://www.freebsd.org/news/newsflash/#2021-07-24:1" target="_self">传送门</a>），以获取更多细节。</p>   
</div>
            