
---
title: 'Linux 5.14版GPU驱动更新发布 新增代码约30万行'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Thu, 01 Jul 2021 11:36:12 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
Linux 5.14的Direct Rendering Manager（内核图形/显示驱动）更新增加了近30万行的新代码（312187插入，22367删除）。巨大的代码量增长是由新增的AMD Radeon图形支持、新增的微软驱动和其他变化所带来的。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p>正如我们已经习惯的那样，L.O.C.计数的大幅增加主要是由于<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>GPU DRM驱动程序和所有相关头文件的新硬件支持。这些寄存器头文件是自动生成的，也真正提高了AMDGPU内核驱动的行数，该驱动已经是Linux内核源代码树中最大的驱动。Linux 5.14的新AMD Radeon硬件支持是<a href="https://www.phoronix.com/scan.php?page=news_item&px=AMDGPU-Yellow-Carp-5.14">Yellow Carp</a>与<a href="https://www.phoronix.com/scan.php?page=news_item&px=AMD-Beige-Goby-Linux-5.14">Beige Goby</a>.。</p><p>Linux 5.14的一个新驱动是来自<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>的Hyper-V显示驱动，但它的体积相对较小，这个周期的另一个新驱动是SimpleDRM驱动。</p><p>Linux 5.14的DRM拉动请求也带来了：</p><p>- Intel Alder Lake P的启用和XeLPD显示的启用。</p><p>- 在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>驱动中继续进行GuC/HuC的启用工作。</p><p>- 英特尔驱动程序适应于为独立GPU使用TTM内存管理，并为DG1独立显卡获得更多位的对齐。</p><p>- AMDGPU的热拔插处理现在应该处于良好状态。</p><p>- 对AMDGPU的16bpc显示支持。</p><p>- 对Aldebaran的初始SR-IOV支持，以及对该新CDNA加速器的其他更新。</p><p>- PCI Express ASPM省电支持被默认启用。</p><p>- 对带有Smart Shift的AMD笔记本电脑实现初步支持。</p><p>- AMDGPU限速降频状态报告。</p><p>- AMDGPU/AMDKFD异构内存管理共享虚拟内存（HMM SVM）支持。</p><p>- 对VMware VMWGFX虚拟驱动器的ARM64支持和初始SVGA3支持。</p><p><strong>Linux 5.14的DRM变化的完整列表可以通过此拉动请求来了解：</strong></p><p><a href="http://lkml.iu.edu/hypermail/linux/kernel/2107.0/00009.html" _src="http://lkml.iu.edu/hypermail/linux/kernel/2107.0/00009.html" target="_blank">http://lkml.iu.edu/hypermail/linux/kernel/2107.0/00009.html</a><br></p>   
</div>
            