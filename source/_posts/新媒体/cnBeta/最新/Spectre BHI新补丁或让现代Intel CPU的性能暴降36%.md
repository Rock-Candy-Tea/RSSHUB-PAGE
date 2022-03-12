
---
title: 'Spectre BHI新补丁或让现代Intel CPU的性能暴降36%'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0312/f9e6924a1b36e67.jpg'
author: cnBeta
comments: false
date: Sat, 12 Mar 2022 01:32:44 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0312/f9e6924a1b36e67.jpg'
---

<div>   
来自阿姆斯特丹的 VUSec 系统系统与网络安全研究团队，刚刚披露了与臭名昭著的 Spectre v2 新漏洞有关的更多细节。<strong>据悉，该漏洞同时影响 Intel 与 ARM 处理器，但 AMD CPU 幸运逃过一劫。</strong>通常情况下，攻击者会通过 CPU 的分支预测来利用“幽灵”（Spectre）漏洞，但新威胁还可利用分支历史缓冲区（BHB）来绕过增强型间接分支限制推测（EIBRS）的硬件缓解措施。<br>
  <p><a href="https://static.cnbetacdn.com/article/2022/0312/f9e6924a1b36e67.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0312/f9e6924a1b36e67.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">视频截图（来自：<a href="https://www.vusec.net/projects/bhi-spectre-bhb/" target="_self">VUSec</a>）</p><p>ARM 平台上的 CSV2 硬件缓解措施，也同样面临可利用 BHB 绕过的问题，因而研究人员将新威胁称作 Spectre-BHB 或分支历史注入（简称 BHI）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0312/f90a08f541daa25.png" alt="2.png" referrerpolicy="no-referrer"></p><p>针对 x86 处理器的 Linux 安全补丁，已于同日发布、并被添加到了 Linux 5.17 主线内核中。</p><p><img src="https://static.cnbetacdn.com/article/2022/0312/c2499d5e339ed6e.gif" alt="3.gif" referrerpolicy="no-referrer"></p><p>为了解 Spectre 新补丁对处理器性能的影响，Phoronix 特地在多款 Intel CPU 上展开了一系列基准测试。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=332378809&autoplay=false&disablePlaylist=true" width="640" height="480" frameborder="0"></iframe></p><p style="text-align: center;">BHI exploit leaking root entry in _etc_shadow（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMzMyMzc4ODA5LnNodG1s.html" target="_self">via</a>）</p><p>首先是最新的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> 12 带 Alder Lake-S 酷睿 i9-12900K 平台，在测量 Sockperf 吞吐量时、该 CPU 的性能损失竟然高达 26.7% 。而在其它基准测试项目中，Spectre-BHB 补丁亦会造成 2~14.5% 的性能损失。</p><p><a href="https://static.cnbetacdn.com/article/2022/0312/14cff3f43b6ba42.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0312/14cff3f43b6ba42.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">i9-12900K 性能折损（图自：<a href="https://www.phoronix.com/scan.php?page=article&item=spectre-bhi-retpoline" target="_self">Phoronix</a>）</p><p>其次，Phoronix 在英特尔 11 代 Tiger Lake 酷睿 i7-1185G7 移动处理器平台上展开了测试，结果发现不打补丁的性能优势竟高达 35.6%（另一项测试为 34.1%）。</p><p><a href="https://static.cnbetacdn.com/article/2022/0312/51992a2e83c800c.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0312/51992a2e83c800c.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">i7-1185G7 性能变化（图自：Phoronix）</p><p>其它情况下，i7-1185G7 在补丁前后的性能损失在 2~26.1% 之间。不过让人费解的是，个别项目竟然还可在部署补丁后，获得了 2.2% 的性能增益。</p>   
</div>
            