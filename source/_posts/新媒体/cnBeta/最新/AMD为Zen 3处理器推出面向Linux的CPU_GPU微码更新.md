
---
title: 'AMD为Zen 3处理器推出面向Linux的CPU_GPU微码更新'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0219/dffabaeb5211da6.png'
author: cnBeta
comments: false
date: Sat, 19 Feb 2022 10:51:06 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0219/dffabaeb5211da6.png'
---

<div>   
<strong>AMD开源团队最近在git.kernel.org网站的Linux固件树上发布了Family 19h/Zen 3
CPU微码更新，描述为"用于Linux内核的固件blobs库"。</strong>固件更新在linux-firmware.git树下，主要针对在Linux中操作的AMD
Zen 3 CPU用户。<br>
<p><strong><a href="https://static.cnbetacdn.com/article/2022/0219/dffabaeb5211da6.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0219/dffabaeb5211da6.png" title alt="]O@Y~KPFE~NR6Y&#125;SS9OT(9T.png" referrerpolicy="no-referrer"></a></strong></p><p><strong>访问获取：</strong></p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/?id=3c60818505d8b27e8716717d202a3068cf757ca5" _src="https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/?id=3c60818505d8b27e8716717d202a3068cf757ca5" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/?id=3c60818505d8b27e8716717d202a3068cf757ca5</a><br></p><p>官方没有为最新的固件升级发布更新日志，但对于AMD来说，这似乎一贯的做法。Family 19h的最后一次微码更新是在去年11月。在没有公布对固件进行了哪些修改的情况下，自然我们也不能够确定AMD是否完成了错误补丁或安全修复。</p><p>相比之下，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>在向Linux发布新的CPU微码时披露的信息比AMD多得多。他们在提供更新同时会提供受影响的产品清单和详细的更新日志。</p><p>AMD最近还更新了搭配Linux下Radeon软件21.50驱动程序的AMDGPU固件和微码文件。</p><p><strong>访问获取：</strong></p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/" _src="https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/</a><br></p><p>同样没有提供任何优化或自上次更新以来的变化细节，但在新驱动程序的发布页面上出现的唯一亮点是这样一句话：提供对 Ubuntu 20.04.4 HWE 的支持，随后补充说提供了面向Vulkan 1.3和CentOS的兼容性。</p><p>Vulkan 1.3是最新的图形和计算API，可以提高图形运算效率，并提供对GPU的跨平台访问。Vulkan是目前唯一的现代GPU API开放标准，使开发者能够编写可移植的应用程序到多个平台。AMD提醒用户确保在他们的系统上禁用RADV驱动，并安装Vulkan SDK 1.2.1298或更高版本。你可以在以下网站找到最新的Vulkan 1.3 SDK更新：<a href="https://vulkan.lunarg.com/sdk/home" _src="https://vulkan.lunarg.com/sdk/home" target="_blank">https://vulkan.lunarg.com/sdk/home</a>。</p>   
</div>
            