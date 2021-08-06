
---
title: '研究人员详解AMD 3D V-Cache缓存设计'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0806/6460b41773ef3a6.jpg'
author: cnBeta
comments: false
date: Fri, 06 Aug 2021 09:12:43 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0806/6460b41773ef3a6.jpg'
---

<div>   
<strong>高级技术研究员 Yuzo Fukuzaki，刚刚为我们详细解释了 AMD 在台北电脑展（Computex 2021）主题演讲期间介绍的一项难以捉摸的新 CPU 技术。</strong>在该公司后续的讲解中，有将所谓的三维垂直缓存（3D V-Cache），描述为堆叠在 CCD（CPU 复杂核心模块）顶上的额外 64MB 末级缓存。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0806/6460b41773ef3a6.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0806/6460b41773ef3a6.jpg" referrerpolicy="no-referrer"></a></p><p>官方宣称 3D V-Cache 设计可将游戏性能平均提升 15%，甚至可与 Zen 3 架构升级所带来的改进相媲美。</p><p>主题演讲体验，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 还亮出了一款基于 AM4 插槽、Zen 3 CCD 架构、辅以 3D V-Cache 缓存部件设计的原型样品。</p><p>以 16 核心的处理器为例，3D V-Cache 可让其拥有 192 MB 的 L3 缓存。</p><p><a href="https://static.cnbetacdn.com/article/2021/0806/f3932d54535d344.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0806/f3932d54535d344.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（传送门：<a href="https://www.linkedin.com/posts/yuzo-fukuzaki-12408111_3dabrv-ryzen-amd-activity-6828725467298828288-Jz_3" target="_self">LinkedIn</a>）</p><p>Yuzo Fukuzaki 通过详细的理论，阐明了 3D V-Cache 在处理器缓存层次结构中的最合理位置。显然，它扩展了 CCD 的 L3 缓存，而不是作为接替 L3 的“L4”级缓存。</p><p>猜测 3D V-Cache 应该属于一种 SRAM 芯片，采用与 Zen 3 CCD 相同的 7nm 工艺制造，尺寸在 6×6 m㎡，通常位于具有 32MB L3 SRAM 的 CCD 区域上方。</p><p>Fukuzaki 预估 AMD 会为 3D V-Cache 芯片打出大约 23000 个硅通孔（TSV），单孔直径约 17 μm，可将 3D V-Cache 芯片与主 CCD 模块紧密连接到一起。</p><p>不过对于操作系统来说，缓存的相关层级设置仍是相当透明的（可视作每个 CCD 模组的 96MB L3 缓存）。</p>   
</div>
            