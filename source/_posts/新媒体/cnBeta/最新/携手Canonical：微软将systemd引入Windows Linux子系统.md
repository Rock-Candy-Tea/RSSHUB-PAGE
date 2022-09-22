
---
title: '携手Canonical：微软将systemd引入Windows Linux子系统'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0922/b8124283b852d23.jpg'
author: cnBeta
comments: false
date: Thu, 22 Sep 2022 02:56:52 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0922/b8124283b852d23.jpg'
---

<div>   
通过与 Canonical 深度合作，<strong>微软今日宣布了 Windows Linux 子系统的一项功能更新 —— WSL2 现可在兼容的 Linux 发行版中运行 systemd 来管理服务。</strong>依赖 systemd 使用、或想要借此来轻松管理应用程序的 Windows 10 / 11 用户，将能够在本次更新后更轻松地于 WSL 环境下体验。<br>
<p><a href="https://static.cnbetacdn.com/article/2022/0922/b8124283b852d23.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0922/b8124283b852d23.jpg" alt="0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（来自：Microsoft Developer）</p><p><strong>微软在公告中解释称：</strong></p><blockquote><p>● 想要支持 systemd，需要对 WSL 的架构加以修改。由于 systemd 需要 PID 1，因此在 Linux 发行版中启动的 WSL init 进程将成为 systemd 的子进程。</p><p>● 其次，WSL init 进程负责为 Linux 和 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 组件之间的通信提供基础设施，因此更改此层次结构需要重新考虑使用 WSL init 进程所做的一些假设。</p><p>● 还有其它必要的修改，以确保正常关闭（clean shutdown）系统、并与 WSLg 兼容。</p><p>● 同样重要的是，通过这些更改，systemd 服务将不会让您的 WSL 实例保持活动状态。</p><p>● 不过相关 WSL 实例，仍可将像之前那样保持活动状态（<a href="https://devblogs.microsoft.com/commandline/systemd-support-is-now-available-in-wsl/" target="_self">详情请戳</a>）。</p></blockquote><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=385290853&autoplay=false&disablePlaylist=true" width="720" height="480" frameborder="0"></iframe></p><p style="text-align: center;">WSL Partnering with Canonical to support systemd（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMzg1MjkwODUzLnNodG1s.html" target="_self">via</a>）</p><p>鉴于这番变动会更改 WSL 在启动时的行为方式，官方建议大家能够谨慎地将之应用于现有的 WSL 发行版。</p><p><img src="https://static.cnbetacdn.com/article/2022/0922/be291d1079c6201.webp" alt="2.webp" referrerpolicy="no-referrer"></p><p>通过有选择性地启用 systemd、并积极向微软提交监测反馈，以便开发团队能够深入调查、并为将来的默认设置奠定基础。</p><p><img src="https://static.cnbetacdn.com/article/2022/0922/04a45f647813fff.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>最后，想要在 WSL 环境中体验 systemd 的用户，可移步至 Ubuntu 博客（<a href="https://ubuntu.com//blog/ubuntu-wsl-enable-systemd" target="_self">传送门</a>）以了解如何正确启用。</p>   
</div>
            