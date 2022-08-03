
---
title: 'Linux 6.0网络子系统将迎来性能优化 并为Wi-Fi 7做早期准备'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png'
author: cnBeta
comments: false
date: Wed, 03 Aug 2022 13:12:42 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png'
---

<div>   
随着Linux 5.19内核的推出，一些令人兴奋的网络改进虽知道来，如big-TCP支持、基于光的网络的PureLiFi驱动、用于低功耗IoT硬件的“WFX”WiFi 驱动支持以及更多。现在，随着正在开发的Linux 6.0（也就是5.20版），还有很多工作要做。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/0404/d2285039c95da55.png" referrerpolicy="no-referrer"></a></p><p>Linux 6.0网络子系统的更新包括性能优化和调整、网络侧的IO_uring zero-copy发送、(e)BPF增强、围绕未来的内核版本中的Wi-Fi 7支持的早期步骤以及更多。</p><p>下面是Linux 6.0中网络功能更新的一些关键亮点：</p><p>- 网络端对IO_uring zero-copy发送的支持。</p><p>- 为Wi-Fi 7多链路操作（MLO）做准备。</p><p>- Unix套接字的每个网络命名空间查询表，以产生更好的可扩展性和降低抢占压力。</p><p>- TLS 1.3接收路径的一个重大性能改进。</p><p>- 各种eBPF改进和优化，BPF程序现在支持可休眠的uprobes，libbpf中的枚举文本表示法，更好的循环性能，新的基于eBPF的LSM类型，类型匹配支持，以及其他新特性。</p><p>- 对网络核心的前向内存分配进行了重构，以更好地处理来自许多开放插座的内存压力。</p><p>- 为Rensesas RZ/N1 ASPSW、Microchip LAN937x、Aquantia AQR113C提供新的以太网驱动程序。</p><p>- <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>ICE网络驱动程序增加了改进的vLAN卸载和PPPoE卸载支持。</p><p>- XDP重定向支持<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>用于Azure的MANA vNIC驱动程序。</p><p>本轮网络补丁的完整列表见此拉动请求：</p><p><a href="https://lore.kernel.org/lkml/20220803101438.24327-1-pabeni@redhat.com/" _src="https://lore.kernel.org/lkml/20220803101438.24327-1-pabeni@redhat.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="99aba9ababa9a1a9aaa8a9a8adaaa1b7abadaaabaeb4a8b4e9f8fbfcf7f0d9ebfcfdf1f8edb7faf6f4">[email protected]</span>/</a><br></p><p>这些补丁增加了约94000行新代码，同时删除了一些现有的64000行。</p>   
</div>
            