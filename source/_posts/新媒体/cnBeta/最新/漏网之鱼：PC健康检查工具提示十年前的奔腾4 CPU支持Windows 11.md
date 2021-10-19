
---
title: '漏网之鱼：PC健康检查工具提示十年前的奔腾4 CPU支持Windows 11'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1019/7107d064e7a431b.jpg'
author: cnBeta
comments: false
date: Tue, 19 Oct 2021 03:19:47 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1019/7107d064e7a431b.jpg'
---

<div>   
经过持续数月的爆料和 Beta 测试，微软终于在 10 月 5 日放出了 Windows 11 操作系统的正式版本。感兴趣的朋友，可通过通过 Windows 更新、或手动下载 ISO 镜像的方式来部署。<strong>有趣的是，尽管微软指定了运行 Windows 11 操作系统的最低硬件要求，不少人还是通过媒体创建工具（或删改 .dll 文件）来强行安装。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1019/7107d064e7a431b.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1019/7107d064e7a431b.jpg" alt="Windows-11-Pentium-CPU.jpg" referrerpolicy="no-referrer"></a></p><p>然而更让我们没想到的是，Carlos S. M. Computers 竟然在一台十年前的 Intel 奔腾 4 CPU 平台上顺利运行了 Windows 11 Build 22000.258（正式版）。</p><p>显然，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>忘记了在 PC 健康检查工具中加入这款 CPU 的识别字符串（Intel Family 15 Model），才使之逃脱了最低 8 代 Intel / 二代 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 锐龙 CPU 的安装检测限制。</p><p><img src="https://static.cnbetacdn.com/article/2021/1019/b6b46874400c8c1.png" alt="P4 Win11.png" referrerpolicy="no-referrer"></p><p>由 Carlos 在油管上分享的视频描述可知，这套平台搭载了 2007 年发布的 P4 661 @ 3.6 GHz（Cedar Mill）单核处理器（支持超线程）。</p><p>辅以<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://asus.jd.com/" target="_blank">华硕</a> P5Q 主板（Intel P45 芯片组）、4GB DDR2 800 内存、英伟达 GT 710（2G D3）显卡、以及<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://mall.jd.com/index-1000098521.html" target="_blank">美光</a> Real<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a> C400 120G SATA 固态硬盘。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=296563484&autoplay=false&disablePlaylist=true" width="640" height="480" frameborder="0"></iframe></p><p style="text-align: center;">Windows 11 running on Intel Pentium 4（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMjk2NTYzNDg0LnNodG1s.html" target="_self">via</a>）</p><p>据某些已在其设备上测试过的网友所述，他们能够在绕过 TPM 2.0 和安全启动的强制性要求之后，顺利地在 P4 661 上安装 Windows 11、甚至接收到了 Build 22000.282 等累积更新。</p><p>至于其它被《PC Health Check》检查工具拦在门外的用户，亦可参考官方文档来创建一个名为“AllowUpgradesWithUnsupportedTPMOrCPU”的注册表值，以在不受支持的硬件上下载并安装 Windows 11 。</p><p>即便如此，微软并不承诺为这些设备提供后续的累积更新或任何技术支持。</p>   
</div>
            