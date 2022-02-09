
---
title: 'Mesa的_TURNIP_Vulkan开源驱动已为高通Adreno提供加速支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0209/a70de88416c1844.webp'
author: cnBeta
comments: false
date: Wed, 09 Feb 2022 06:53:38 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0209/a70de88416c1844.webp'
---

<div>   
<strong>上周末召开的 FOSDEM 2022 线上活动中，Mesa 的“TURNIP”Vulkan 开源驱动为高通 Adreno 图形提供加速支持。</strong>TURNIP 最初是一个 Vulkan 驱动项目，与用于 Adreno 图形“Freedreno”反向工程 Gallium3D 驱动相似（大部分是同一个开发者），现在正逐渐走向成熟。<br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0209/a70de88416c1844.webp" alt="kncjpbbu.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">Igalia 的 Hyunjun Ko 介绍了 TURNIP 在过去一年取得的进展。许多 Vulkan 扩展是通过这个反向工程的开源高通 Vulkan 驱动实现的。除了添加了许多突出的扩展，还有一些重要的修正，最终使 TURNIP 成为符合 Adreno 618 类 GPU 的 Vulkan 1.1 驱动程序。</p><p style="text-align: left;">通过和 FEX-Emu、Box86 搭配使用，这个 Mesa Vulkan 驱动自去年开始可以运行 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 游戏，这要感谢 DXVK/VKD3D 在 Vulkan 上映射 Direct3D，然后 FEX/Box86 处理 x86/x86_64 到 Arm 的转换。</p>   
</div>
            