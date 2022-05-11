
---
title: 'AMD RNDA 3系列GFX11 GPU迎来首个Mesa代码合并'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0428/23933c53deb1880.webp'
author: cnBeta
comments: false
date: Wed, 11 May 2022 07:17:38 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0428/23933c53deb1880.webp'
---

<div>   
Phoronix 指出：<strong>近日一些著名的开源 AMD Radeon 图形驱动程序代码，被合并到了下个季度的 Mesa 22.2 版本项目中。</strong>作为 GFX10 的继任者，GFX11 显然特指基于 AMD RDNA 3 的下一代图形显示 IP 块。而更老的 GFX 9 / 10，则分别指代 Vega / CDNA 和 RDNA / RDNA 2 。<br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0428/23933c53deb1880.webp" referrerpolicy="no-referrer"></p><p>AMD 最近证实，其正在将工作重心转移到新一代 Radeon RX 7000 系列显卡产品线上。</p><p>而过去一周半的时间里，该公司已向 Mesa 提交了多项针对 GFX11 系列 和 AMDGPU Linux 内核 DRM 开源驱动程序的补丁。</p><p>通过将这批重要的开源 Radeon 图形驱动程序代码引入 Mesa 22.2，表明 AMD 正积极为 2022 年 3 季度的初始 RDNA 3“GFX11”GPU 支持做准备。</p><p>此外该公司还计划添加对另外几个 IP 块的支持，比如早前披露的为 LLVM 15.0 添加 GFX11 相关编码（该版本定于 4 个月后发布）。</p><p><a href="https://static.cnbetacdn.com/article/2022/0511/7b730f766629482.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0511/7b730f766629482.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">截图（来自：<a href="https://www.phoronix.com/scan.php?page=news_item&px=Mesa-22.2-GFX11-RDNA3-Lands" target="_self">Phoronix</a>）</p><p>虽然硬件仍处于开发阶段，但 AMD 仍在努力添加更多 RDNA 3 GFX11 特性，比如 Mesa 支持就提到了对 RadeonSI Gallium3D OpenGL 驱动程序的高度重视。</p><p>而最近在 Mesa 22.2 版本中添加的 RADV 驱动程序，又被视作与 Red Hat 和 Google Valve 等团体联手开发的非官方驱动程序。</p><p>使用 RADV 支持的开发者们，肯定希望加入 GFXll 和 RDNA3 的 Linux 支持补丁，从而为即将推出的新硬件找到必要的 ACO 编译器后端方案。</p><p><img src="https://static.cnbetacdn.com/article/2022/0511/b621bbf9bac667a.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：<a href="https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/16328" target="_self">FreeDesktop.org</a>）</p><p>新版 Mesa 对 AMD 图形硬件的另一项重要支持，就是全新的 VCN4 视频加速编解码器补丁（可与 Gallium3D 视频加速状态跟踪器配合使用）。</p><p>目前仍缺席的，就是<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> Arc Alchemist GPU 中已引入的 AV1 硬件加速支持。如果爆料靠谱的话，AMD 应该也会很快完善相关代码补丁。</p><p>最后，过去 24 小时内，合并工作队列已经提交了次要的 RADV 重构代码，以允许使用 Radeon Vulkan 驱动程序对相关任务进行着色。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1265991.htm" target="_blank">AMD RDNA 3补丁揭示Radeon RX 7000系列显卡支持AV1编码</a></p></div>   
</div>
            