
---
title: 'Linux 5.17网络子系统方面的变化相当令人兴奋'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0110/4c274aebfa3eeb7.jpg'
author: cnBeta
comments: false
date: Mon, 10 Jan 2022 13:55:59 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0110/4c274aebfa3eeb7.jpg'
---

<div>   
正在开发的5.17内核的Linux网络子系统的更新是相当令人兴奋的，因为Linux在云中的大型服务器和企业网络设备上的运行以及小型物联网硬件上的Linux都是如此多产。新版不仅像往常一样有大量的硬件驱动行动，而且还有一些关键的性能/延迟优化。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0110/4c274aebfa3eeb7.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>在性能优化方面，AF_UNIX套接字有一个显著的延迟优化，同时优化了x86_64的csum_partial()函数，该函数通常用于计算TCP校验和。此外，TCP性能优化即在套接字锁释放后推迟释放SKB也非常令人关注。</p><p><img src="https://static.cnbetacdn.com/article/2022/0110/be4ca6f801b5394.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p><img src="https://static.cnbetacdn.com/article/2022/0110/5f9aece4081d601.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>Linux 5.17加入了许多<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>Wi-Fi设备的"ILLWIFI"驱动改进，包括新的Killer AX211 PCI ID、6GHz WiFi改进、支持OCE扫描、TAS支持以及更多。还加入了用于英特尔的WiFi驱动和其主动管理技术设备之间的接口。</p><p><img src="https://static.cnbetacdn.com/article/2022/0110/24a31f6cf19f506.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>新版对<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>方面也非常友好，尤其是对Yellow Carp的以太网支持，这让"Rembrandt"APU的处理器集成网络可以不经配置直接开始使用。此外还有对尚未发布的NVIDIA Spectrum-4网络ASIC的支持。</p><p>Linux 5.17的其他一些网络变化包括：新的BPF助手，支持内核加载器中的BPF重定位，为libbpf的v1.0版本做准备，在WiFi代码中通过在空时公平代码中使用粗略时间来节省一些CPU周期，支持Android AOSP蓝牙质量报告，多补丁TCP（MPTCP）增强，支持管理组件通过串行传输（MCTP），不同类型的网络卸载流程改进，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>方面加入的现在有XDP驱动程序支持，新的IWLMEI驱动程序。</p>   
</div>
            