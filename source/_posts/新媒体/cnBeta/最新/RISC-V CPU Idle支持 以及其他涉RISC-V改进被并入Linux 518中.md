
---
title: 'RISC-V CPU Idle支持 以及其他涉RISC-V改进被并入Linux 5.18中'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0208/a6162d7a29ebca6.webp'
author: cnBeta
comments: false
date: Sun, 03 Apr 2022 04:06:59 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0208/a6162d7a29ebca6.webp'
---

<div>   
上周，Linux 5.18的主要RISC-V拉动带来了Sv57五级页表支持、改进的PolarFire
SoC支持、优化的MEMMOVE代码、对可重启序列的支持等等。<strong>最值得关注的是第二批RISC-V功能更新在本周发出，现在已经完成主线合并，使Linux
5.18内核更适合这种开放的处理器ISA。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0208/a6162d7a29ebca6.webp" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/0208/a6162d7a29ebca6.webp" referrerpolicy="no-referrer"></a></p><p>如上所述，RISC-V功能的重大变化已在上周被合并，但作为CPU架构更新的第二部分，足够多的额外（和测试）材料也已准备好。</p><p>首先是RISC-V CPU Idle支持使用较新的SBI（超级管理员二进制接口）扩展。RISC-V CPU Idle驱动是受Arm的PSCI CPU Idle驱动设计的"启发"。<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://wdc.jd.com/" target="_blank">西部数据</a>为这个新驱动程序的开发做出了主要贡献，该驱动程序用于处理处理器内核的空闲状态，以提高节约能源的能力。</p><p>RISC-V现在还支持CURRENT_STACK_POINTER内核选项，用于围绕强化用户拷贝代码进行额外的堆栈调试。此外，RISC-V的默认配置文件现在选择默认启用"CONFIG_PROFILING"。这是为了在不同的平台上利用可行的RISC-V PMU驱动，以帮助进行性能分析和其他内核分析功能。内核本次更新其余的工作主要是清理/修复。</p><p>关于Linux 5.18的这些最新RISC-V变化的更多细节，请看这个拉动请求：</p><p><a href="https://lore.kernel.org/lkml/mhng-e0c01ab7-020f-4264-91da-0852f7e89534@palmer-mbp2014/" _src="https://lore.kernel.org/lkml/mhng-e0c01ab7-020f-4264-91da-0852f7e89534@palmer-mbp2014/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="1a7772747d377f2a792a2b7b782d372a282a7c372e282c2e37232b7e7b372a222f287c2d7f22232f292e5a6a7b76777f683777786a282a2b2e">[email protected]</span>/</a><br></p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1228995.htm" target="_blank">Linux 5.17增加了对RISC-V sv48的支持 能够使设备识别更多的内存</a></p><p><a href="https://www.cnbeta.com/articles/tech/1248233.htm" target="_blank">RISC-V巨头SiFive完成1.75亿美元F轮融资 公司估值超25亿美元</a></p><p><a href="https://www.cnbeta.com/articles/tech/1248845.htm" target="_blank">禁完x86禁Arm RISC-V或成俄罗斯唯一选择</a></p></div>   
</div>
            