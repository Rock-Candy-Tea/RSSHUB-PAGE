
---
title: 'Linux 5.16 网络子系统大范围升级 多个新适配器驱动加入'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1102/5fb59868ee87361.jpeg'
author: cnBeta
comments: false
date: Tue, 02 Nov 2021 10:31:53 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1102/5fb59868ee87361.jpeg'
---

<div>   
<strong>Linux在数据中心中占主导地位，因此每个内核升级周期的网络子系统变化仍然相当活跃。Linux
5.16也不例外，周一最新与网络相关的更新加入了大量的驱动和新规范的支持。</strong>一个较新硬件的驱动是Realtek RTW89
Wi-Fi驱动，用于支持Realtek 8852AE 802.11ax适配器和未来的型号。<br>
 <p>另一个新网络驱动程序是用于ASIX AX88796C硬件的x88796c。同时，高通QCA8k驱动增加了对QCA8328的支持，以及对现有网络驱动的其他较小的支持补充。</p><p><img src="https://static.cnbetacdn.com/article/2021/1102/5fb59868ee87361.jpeg" title alt="wp-upload.jpeg" referrerpolicy="no-referrer"></p><p>英特尔的100G以太网驱动代码为TC/OvS flow API增加了eswitch offload，支持应用设备队列，其中Rx/Tx队列可以分配给应用线程，以及其他改进。</p><p>联发科MT7921 Wi-Fi驱动程序增加了对6GHz Wi-Fi的支持、主动状态电源管理（ASPM）和其他改进。</p><p><img src="https://static.cnbetacdn.com/article/2021/1102/2c4f47f69da928c.webp" title alt="mobile01-564e4080fd29fff3a197dc33075857d3.jpg.webp" referrerpolicy="no-referrer"></p><p>蓝牙代码方面，新版本合并的驱动对蓝牙链接质量和音频/编解码器支持有了一些改进，蓝牙驱动支持现在也出现在联发科MT7922和MT7921 SoC上。</p><p>Google的vNIC"GVE"驱动增加了对巨量帧、Rx页面重用和其他改进的支持。</p><p>BPF代码有了一些改进，包括安全方面的改变，现在默认不允许无特权的BPF。</p><p>核心网络代码增加了管理邻近条目的概念，这些条目由控制平面添加，并由内核解析，用于XDP和BPF等加速路径。其他变化包括对多路径TCP（MPTCP）的持续改进、基于RFC7450规范的自动组播隧道（AMT）驱动程序的引入，以及其他改进。</p><p><strong>关于Linux 5.16的许多网络变化的更多细节，请见此拉动请求：</strong></p><p><a href="https://lore.kernel.org/lkml/20211102054237.3307077-1-kuba@kernel.org/" _src="https://lore.kernel.org/lkml/20211102054237.3307077-1-kuba@kernel.org/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="1c2e2c2e2d2d2d2c2e2c29282e2f2b322f2f2c2b2c2b2b312d3177697e7d5c77796e72797032736e7b">[email protected]</span>/</a><br></p>   
</div>
            