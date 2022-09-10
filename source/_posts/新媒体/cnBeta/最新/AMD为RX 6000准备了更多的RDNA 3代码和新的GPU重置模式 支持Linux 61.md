
---
title: 'AMD为RX 6000准备了更多的RDNA 3代码和新的GPU重置模式 支持Linux 6.1'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0910/479e7392ac08385.png'
author: cnBeta
comments: false
date: Sat, 10 Sep 2022 07:23:31 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0910/479e7392ac08385.png'
---

<div>   
AMD在Linux 6.1合并窗口关闭前为DRM-Next增加了一个重要的AMDGPU内核图形驱动更新，准备了更多的RDNA 3代码和新的GPU重置模式。每周我们都会收到来自AMD开源工程师的更新，他们稳步开发对公司新技术的支持。<br>
 <p>本周，AMD准备了对RDNA 3图形和CDNA MI300图形加速卡的支持。AMD将在内核中添加一个新的代码块，以协助实现这一支持。</p><p>然而，这段代码可以给Linux 6.1带来多大的AMD的内核支持表现提升目前还不知道。</p><p><a href="https://static.cnbetacdn.com/article/2022/0910/479e7392ac08385.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0910/479e7392ac08385.png" title alt="AMD-RDNA-3-Navi-33-GPU-For-Next-Gen-Radeon-RX-Graphics-Cards-_1.png" referrerpolicy="no-referrer"></a></p><p>以下是AMD本周做出的改变的总结：</p><blockquote><p><strong>amd-drm-next-6.1-2022-09-08:</strong></p><p>amdgpu:</p><p>- RDNA2的Mode2重置</p><p>- 大量新的DC文档</p><p>- 增加关于不同asic系列的文档</p><p>- DSC改进</p><p>- Aldebaran的修复</p><p>- 一些拼写和语法方面的修正</p><p>- 对vangogh的GFXOFF统计支持</p><p>- DC框架大小的修复</p><p>- NBIO 7.7更新</p><p>- DCN 3.2版更新</p><p>- DCN 3.1.4版更新</p><p>- SMU 13.x更新</p><p>- 杂项错误修复</p><p>- 重写DC寄存器偏移处理</p><p>- GC 11.x版更新</p><p>- PSP 13.x的更新</p><p>- SDMA 6.x更新</p><p>- GMC 11.x更新</p><p>- SR-IOV更新</p><p>- PSP对TA卸载的修复</p><p>- 支持DSC直通车</p><p>- 杂项代码清理</p><p>amdkfd:</p><p>- 对某些GC 10.3 IP的ISA修复</p><p>- 杂项代码清理</p><p>radeon:</p><p>- 延迟工作释放的修复</p><p>- 对一些jiffies的计算使用time_after</p><p>drm:</p><p>- 支持DSC穿透式辅助功能</p></blockquote><p>AMD代码中的不确定性是该公司在逐个IP块的基础上激活的策略。该公司还没有完全透露他们在明年支持Linux即将到来的图形和加速方面有多接近。还有一个问题是，一旦新技术推出，公司是否会有相应的准备工作。</p><p>AMD还增加了"Mode2"复位支持，涵盖"Sienna Cichlid"RDNA 2架构和Radeon RX 6000图形。Mode2是一种替代的图形处理重置模式，计划用于多容器使用情况和其他需要短时间GPU重置的领域，而不影响显存，反过来也不会丢失数据。</p><p>最后，AMD包括Aldebaran系列的错误修复和补丁，显示流压缩（DSC）的增强，VanGogh APU GFXOFF统计支持，SR-IOV的更新，以及各种低级代码的修订。你可以在这里阅读完整的拉动请求，列出所有的信息和每个新添加到内核的附加信息，为明年Linux 6.1的发布做准备：</p><p><a href="https://lists.freedesktop.org/archives/dri-devel/2022-September/371214.html" _src="https://lists.freedesktop.org/archives/dri-devel/2022-September/371214.html" target="_blank">https://lists.freedesktop.org/archives/dri-devel/2022-September/371214.html</a><br></p>   
</div>
            