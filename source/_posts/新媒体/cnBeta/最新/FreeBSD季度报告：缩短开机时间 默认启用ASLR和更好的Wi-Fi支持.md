
---
title: 'FreeBSD季度报告：缩短开机时间 默认启用ASLR和更好的Wi-Fi支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0311/b2acf8f902c4686.jpg'
author: cnBeta
comments: false
date: Fri, 11 Mar 2022 10:56:13 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0311/b2acf8f902c4686.jpg'
---

<div>   
<strong>除了今天发布FreeBSD
13.1-BETA1之外，FreeBSD项目还发布了2021年第四季度的状态报告，总结了过去一个季度中这个BSD操作系统所取得的所有开源活动。</strong>2021年第四季度对FreeBSD来说是一个非常繁忙的时期，在许多方面都取得了进展，包括：<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0311/b2acf8f902c4686.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>- 从11月起，通过FreeBSD HEAD中的代码，FreeBSD默认启用了地址空间布局随机化（ASLR），适用于FreeBSD上的所有64位可执行文件，包括PIE和非PIE（位置独立可执行文件）二进制文件。</p><p>- 正在进行的改善FreeBSD启动时间的工作，在Amazon EC2云上进行了测试。最新的工作使FreeBSD的启动时间从第四季度前的30秒减少到15秒左右，然后在第四季度末有望达到10秒左右。</p><p>- FreeBSD的Ports软件包集已经达到了46700个。</p><p>- FreeBSD 基金会对 AVX 错误进行了修正， 对 WireGuard 所需的加密技术进行了修改， 对 LLDB 调试器进行了改进， 并增加了新的系统调用 -- 包括 RSEQ、 MEMBARRIER 和 SHCED_GETCPU。</p><p>- 目前正在进行 FreeBSD 网站的改进工作。</p><p>- FreeBSD 将继续支持 LLVM 调试器 (LLDB)，并为其增加新的功能/支持。</p><p>- 通过利用<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>为Linux内核提供的代码，英特尔Wi-Fi驱动继续得到改进。现在已经支持英特尔AX210芯片组，并且正在对该驱动进行其他改进。</p><p>更多关于 FreeBSD Q4'2021 变化的细节请参见状态报告。</p>   
</div>
            