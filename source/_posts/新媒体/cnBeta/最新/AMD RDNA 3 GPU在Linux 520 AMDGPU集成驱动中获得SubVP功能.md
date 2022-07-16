
---
title: 'AMD RDNA 3 GPU在Linux 5.20 AMDGPU集成驱动中获得SubVP功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0716/716b3afdaa1f1a9.png'
author: cnBeta
comments: false
date: Sat, 16 Jul 2022 13:39:38 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0716/716b3afdaa1f1a9.png'
---

<div>   
据报道，AMD将发布AMDGPU和AMDKFD驱动的最后一个功能更新计划到DRM-Next for Linux 5.20，为RDNA
3的发布做准备。合并窗口将在本月晚些时候开放，AMD等公司和最近报道的英特尔在内核支持上增加的功能正在敲定，为这两个科技巨头新一代的图形硬件做准备。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0716/716b3afdaa1f1a9.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0716/716b3afdaa1f1a9.png" title alt="2022-06-10_4-20-55.png" referrerpolicy="no-referrer"></a></p><p>AMD正在准备下一代RDNA 3架构和AMD基于CDNA的加速器，也被称为AMD Instinct，当该公司今年晚些时候开始推出最新的计算机组件时，对其新硬件的启用是在"逐块基础上"完成的。目前的开发状态不像以前的Linux驱动补丁那样明显。</p><p>AMD没有报告他们是否完成了对Linux 5.20内核支持的更新，但预计他们已经非常接近完成，因为AMD Radeon RX 7000 GPU将在未来几个月内首次亮相。然而，假设AMD在产品推出后，他们的RDNA 3更新与Linux 5.20的整合还没有确定。在这种情况下，开源用户将不得不依赖第三方的解决方案，直到该公司能够完全敲定进程中的集成。</p><p>今天，最后的DRM-Next功能拉动显示了更多的AMDGPU Linux驱动集成，就在AMD可以将之前的代码和修复添加到Linux 5.20内核中。由AMD添加到内核的更新包含：</p><blockquote><p>显示核心Next（DCN）v3.2块</p><p>支持DCN 3.1.4</p><p>SMU13更新</p><p>对GFX11（RDNA 3）图形和SDMA 6块的软复位处理</p></blockquote><p>对GFX11的软复位处理支持"对于确保当前补丁的任何停滞或问题至关重要。"SubVP"是一个新的显示核心（DC）组件，允许子视口功能。该元件是一个新的DCN 3.2硬件功能，但目前还不知道SubVP功能的全部能力将是什么。</p><p>AMD的最新拉动还增加了"DC SubVP支持"。在Linux AMD的拉动更新中，还整合了DisplayPort多流传输（DP MST）、许多音频补丁，并在最近的APU上修改了GART大小，增加了Scatter和Gather显示支持。最后，AMD还整合了VanGogh系列APU的GFXOFF状态的查询，增强了缓冲区对象域的固定，以及一些AMDKFD的修改。</p><p>有兴趣的读者可以可以查看官方内核页面上的拉动请求，在此阅读更多关于目前为Linux 5.20准备的AMDGPU和AMDKFD改动：</p><p><a href="https://lore.kernel.org/dri-devel/20220714214716.8203-1-alexander.deucher@amd.com/" _src="https://lore.kernel.org/dri-devel/20220714214716.8203-1-alexander.deucher@amd.com/" target="_blank">https://lore.kernel.org/dri-devel/<span class="__cf_email__" data-cfemail="be8c8e8c8c8e898f8a8c8f8a898f8890868c8e8d938f93dfd2dbc6dfd0dadbcc90dadbcbddd6dbccfedfd3da90ddd1d3">[email protected]</span>/</a><br></p>   
</div>
            