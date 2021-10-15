
---
title: 'AMD终于在Linux 5.16版本中为较新的硬件默认启用了PSR'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1015/e9af35ac49c5f85.jpg'
author: cnBeta
comments: false
date: Fri, 15 Oct 2021 10:00:58 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1015/e9af35ac49c5f85.jpg'
---

<div>   
随着Linux
5.15内核即将完工，直接渲染驱动程序维护者的工作重点正在从针对下一周期（5.16）的新功能工作转移到错误修复上。<strong>AMD本周发出了一份AMDGPU
Linux 5.16素材的拉动请求，主要是提供错误修复，但一个值得注意的补充是最终为较新的GPU默认启用PSR。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1015/e9af35ac49c5f85.jpg" title alt="refresh.jpg" referrerpolicy="no-referrer"></p><p>在前几周，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>GPU向DRM-Next提出的Linux 5.16拉动请求带来了DisplayPort 2.0首次启用、Cyan Skillfish显示支持、USB4 DisplayPort隧道和其他变化。</p><p>本周为5.16合并窗口向DRM-Next提出的拉动请求包括围绕Cyan Skillfish Navi 1x APU支持的更多修复，IP发现枚举修复，显示器问题修复，Aldebaran的RAS修复，Raven Ridge的IOMMU修复，以及其他修复。</p><p>这个拉动请求中隐藏的一个补丁带来了一些令人兴奋的地方，即在较新的DCN硬件上默认启用PSR。是的，面板自我刷新终于在较新的硬件上被默认启用。尽管在这个时候，较新的硬件所支持的是带有DCN 3.1的Yellow Carp（Rembrandt）。带有DCN-3.1之前的硬件的GPU目前保持PSR关闭。</p><p>面板自刷新是一项省电功能，当显示屏/显示器内容是静态的时候，能够关闭额外的电路。虽然PSR是一个行业标准，但对于<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>硬件和各种笔记本显示面板来说，它也被证明是古怪的。由于一些桌面合成器不能正确地翻页和扫描出与他们的PSR处理方式有关的问题，AMD将他们的PSR支持被禁用到现在。现在，AMD更好地处理了合成器，因此认为默认情况下启用面板自刷新是安全的。但由于可能出现错误/退步，至少现在AMD没有为现有硬件启用PSR，只是为DCN 3.1和更新的显示硬件默认设置。</p><p>我们将在一段时间后看到他们是否决定为现有的AMD硬件打开PSR。</p><p>这个最新的AMDGPU/AMDKFD拉动请求到DRM-Next的补丁列表可以在这里找到：</p><p><a href="https://lists.freedesktop.org/archives/amd-gfx/2021-October/070204.html" _src="https://lists.freedesktop.org/archives/amd-gfx/2021-October/070204.html" target="_blank">https://lists.freedesktop.org/archives/amd-gfx/2021-October/070204.html</a><br></p>   
</div>
            