
---
title: '研究人员警告基于SATA天线的气隙系统攻击方法'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0719/ce63fe33d76eb4d.jpg'
author: cnBeta
comments: false
date: Tue, 19 Jul 2022 06:56:11 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0719/ce63fe33d76eb4d.jpg'
---

<div>   
<strong>以色列内盖夫本古里安大学软件和信息系统工程系的安全研究人员，刚刚披露了他们新发现的一种网络攻击技术。</strong>从“SATAn”的命名来看，可知其与计算机上常见的 SATA 存储接口有关。具体说来是，这是一种从气隙系统中窃取信息和数据的方法。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0719/ce63fe33d76eb4d.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0719/ce63fe33d76eb4d.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>所谓“气隙系统”，特指部署于任何网络的独立实体设备。然而有研究发现，在 6 GHz 频段附近、通过 SATA 数据线进行的无线传输相当有效。</p><blockquote><p>研究团队指出，尽管气隙 PC 没有无线连接，但其演示已表明攻击者能够利用 SATA 数据线来传输 6 GHz 频段的无线电信号。</p><p>串行 SATA 是在当前计算机中被广泛使用的总线接口，用于连接主机总线上的大容量存储设备 —— 比如 HDD / <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a> 和光驱等。</p><p>但也正是这种接口的普及性，使得针对各种 IT 环境和计算机系统的攻击也相当有效。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0719/35440a681ebaeaf.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>实验表明，SATA 3.0（6 Gbps）线缆会在各种频段发射电磁波 —— 包括 1 GHz、2.5 GHz、3.9 GHz 和 +6 GHz 。</p><p>然而与无线传输的最大相关性跨越，就出现在 5.9995 到 5.9996 GHz 之间 —— 隐蔽通道背后的想法，就是当 SATA 数据线当做可控制电磁辐射的天线。</p><p>结果表明，攻击者可使用 SATA 电缆将少量敏感信息，从高度安全的气隙计算机上无线传输至附近的接收器。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=366566135&autoplay=false&disablePlaylist=true" width="720" height="480" frameborder="0"></iframe></p><p style="text-align: center;">SATAn Air-Gap Exfiltration Attack via Radio Signals From SATA Cables（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMzY2NTY2MTM1LnNodG1s.html" target="_self">via</a>）</p><p>更糟糕的是，额外测试表明，在产生更强的信号方面，SATA 上的读取动作、比写入操作更为有效（平均强 3 dB）。</p><p>这也使得整体攻击更变更加容易得逞，毕竟写入通常需要获取更多的权限 —— 比如应用程序通常会开放读取其配置文件数据，但在写入上有所限制。</p><p><img src="https://static.cnbetacdn.com/article/2022/0719/e91539bf7b98435.jpg" alt="3.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://arxiv.org/abs/2207.07413" target="_self">Arxiv</a> | <a href="https://arxiv.org/pdf/2207.07413.pdf" target="_self">PDF</a>）</p><p>尽管如预期那样，SATA / 磁盘活动会导致 SATAn 隐蔽信道的效率变低。尤其在涉及密集的磁盘活动时，相关工作也会受到 CPU 和 I/O 限制。</p><p>不过最让人担心的，还是这项攻击在虚拟机上同样可行，只是效果会大打折扣。可知与主机生成的信号相比，虚拟机中的信号质量平均降低了 5 dB 。</p>   
</div>
            