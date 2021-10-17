
---
title: 'AMD Ryzen SME特性在Linux系统上造成启动失败和黑屏问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1017/81733635317f912.jpg'
author: cnBeta
comments: false
date: Sun, 17 Oct 2021 14:26:48 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1017/81733635317f912.jpg'
---

<div>   
<strong>AMD的安全内存加密（SME）功能被发现对某些Linux系统造成问题，因此，从现在开始，该功能将被默认禁用。这个问题是由Linux工程师Paul
Menzel在10月5日发现的。</strong>SME功能显然在某些AMD Raven Ridge系统上导致启动失败。<br>
 <p>这个问题最早是在Ryzen 3
2200G系统上检测到的，该处理器与<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">微星</a>B350M MORTAR主板配对时问题非常突出。</p><p>然而在其他启用SME的Ryzen电脑中也报告了黑屏问题，因此，这个问题可能也存在于其他基于Zen的处理器系列中。</p><p><a href="https://static.cnbetacdn.com/article/2021/1017/81733635317f912.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1017/81733635317f912.jpg" title alt="1634471795_amd_sme_sev.jpg" referrerpolicy="no-referrer"></a></p><p><strong>报错信息集中在:</strong></p><blockquote><p>AMD_MEM_ENCRYPT</p><p>AMD_MEM_ENCRYPT_ACTIVE_BY_DEFAULT<br></p></blockquote><p>它甚至在其他系统上导致黑屏，该问题已被报告给Debian错误跟踪系统。</p><p>SME功能允许对系统DRAM进行加密，以便保护其中的敏感数据免受黑客的攻击。但内核团队也已经发出提示，由于某些平台的缺陷，不要在Kconfig中默认启用AMD内存加密，导致启动失败。</p><p>了解更多：</p><p><a href="https://lore.kernel.org/lkml/YWvy9bSRaC+m1sV+@zn.tnic/T/#u" _src="https://lore.kernel.org/lkml/YWvy9bSRaC+m1sV+@zn.tnic/T/#u" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="4b121c3d32722918192a0860267a381d600b3125653f252228">[email protected]</span>/T/#u</a><br></p><p><a href="https://lists.freedesktop.org/archives/amd-gfx/2021-October/069868.html" _src="https://lists.freedesktop.org/archives/amd-gfx/2021-October/069868.html" target="_blank">https://lists.freedesktop.org/archives/amd-gfx/2021-October/069868.html</a> <br></p>   
</div>
            