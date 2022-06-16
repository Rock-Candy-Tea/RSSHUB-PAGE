
---
title: '微软和英特尔发布安全公告：Windows 10_11存在MMIO数据漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0616/eab5979564f6741.webp'
author: cnBeta
comments: false
date: Thu, 16 Jun 2022 08:42:36 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0616/eab5979564f6741.webp'
---

<div>   
在英特尔和微软今天发布的公告中，表示多款英特尔酷睿处理器存在一系列 CPU 漏洞。这些安全漏洞与 CPU 的内存映射 I/O（MMIO）有关，因此被统称为“MMIO陈旧数据漏洞”（MMIO Stale Data Vulnerabilities）。威胁者在成功利用一个有漏洞的系统后，可以读取被攻击系统上的特权信息。<br>
 <p style="text-align: left;">在其安全公告 <a href="https://msrc.microsoft.com/update-guide/vulnerability/ADV220002" target="_blank">ADV220002</a> 中，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>描述了潜在的攻击场景：</p><blockquote style="text-align: left;"><p style="text-align: left;">成功利用这些漏洞的攻击者可能会跨越信任边界读取特权数据。在共享资源环境中（如存在于一些云服务配置中），这些漏洞可能允许一个虚拟机不正当地访问另一个虚拟机的信息。在独立系统的非浏览场景中，攻击者需要事先访问系统，或者能够在目标系统上运行特制的应用程序来利用这些漏洞。</p></blockquote><p style="text-align: left;">这些漏洞被称为：</p><blockquote style="text-align: left;"><p style="text-align: left;">● <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21123" target="_blank">CVE-2022-21123</a> - 共享缓冲区数据读取(SBDR)</p><p style="text-align: left;">● <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21125" target="_blank">CVE-2022-21125</a> - 共享缓冲区数据采样(SBDS)</p><p style="text-align: left;">● <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21127" target="_blank">CVE-2022-21127</a> - 特殊寄存器缓冲区数据采样更新(SRBDS更新)</p><p style="text-align: left;">● <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21166" target="_blank">CVE-2022-21166</a> - 设备寄存器部分写入(DRPW)</p></blockquote><p style="text-align: left;">MMIO 使用处理器的物理内存地址空间来访问像内存组件一样响应的 I/O 设备。<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>在其安全公告 <a href="https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00615.html" target="_blank">INTEL-SA-00615</a> 中，更详细地描述了如何利用 CPU 非核心缓冲区数据来利用该漏洞。</p><blockquote style="text-align: left;"><p style="text-align: left;">处理器 MMIO 陈旧数据漏洞是一类内存映射的 I/O（MMIO）漏洞，可以暴露数据。当一个处理器内核读取或写入MMIO时，交易通常是通过不可缓存或写入组合的内存类型完成的，并通过非内核进行路由，非内核是CPU中的一段逻辑，由物理处理器内核共享，并提供一些通用服务。恶意行为者可能利用非核心缓冲区和映射寄存器来泄露同一物理核心内或跨核心的不同硬件线程的信息。</p><p style="text-align: left;">[......]这些漏洞涉及的操作导致陈旧的数据被直接读入架构、软件可见的状态或从缓冲区或寄存器采样。在一些攻击场景中，陈旧的数据可能已经存在于微架构的缓冲器中。在其他攻击场景中，恶意行为者或混乱的副代码可能从微架构位置（如填充缓冲区）传播数据。</p></blockquote><p style="text-align: left;">据微软称，以下<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>版本受到影响。</p><blockquote style="text-align: left;"><p style="text-align: left;">● Windows 11</p><p style="text-align: left;">● Windows 10</p><p style="text-align: left;">● Windows 8.1</p><p style="text-align: left;">● Windows Server 2022</p><p style="text-align: left;">● Windows Server 2019</p><p style="text-align: left;">● Windows Server 2016</p></blockquote><p>受影响的 CPU 列表以及它们各自的缓解措施如下图</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0616/eab5979564f6741.webp" alt="zfjrppf2.webp" referrerpolicy="no-referrer"></p>   
</div>
            