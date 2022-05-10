
---
title: 'AMD正在为Linux准备Zen 4 IBS扩展补丁'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0505/6c4083838890ba1.jpg'
author: cnBeta
comments: false
date: Tue, 10 May 2022 05:27:08 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0505/6c4083838890ba1.jpg'
---

<div>   
近日，AMD 提交了面向 Linux 预取子系统和实用程序的 IBS 补丁。<strong>该功能全称为“基于指令集的采样”（Instruction-Based Sampling），同时也是该公司 Zen 4 CPU 家族的首个官方补丁。</strong>Phoronix 指出，随着新补丁提交审查，意味着 Zen 4 处理器的 Linux 支持正在稳步推进。<br>
<p><a href="https://static.cnbetacdn.com/article/2022/0505/6c4083838890ba1.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0505/6c4083838890ba1.jpg" alt="0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图 via <a href="https://wccftech.com/amd-preps-zen-4-ibs-instruction-based-sampling-extensions-for-linux/" target="_self">WCCFTech</a>）</p><p>相关变化将在 Linux 开源操作系统的全新补丁和后续更新中得到很好的体现，且 Zen 4 将通过创建额外的数据源扩展、以及 L3 缓存未命中时的过滤功能，来增强 IBS 的使用体验。</p><p>Linux 内核邮件公告列表（<a href="https://lore.kernel.org/lkml/20220509044914.1473-1-ravi.bangoria@amd.com/" target="_self">LKML</a>）写道：</p><blockquote><p>● DataSrc 扩展为标记的加载 / 存储（load / store）操作提供了额外的数据源详情，且性能报告 / 脚本（perf report / script）原始转储（raw-dump）中也添加了对这些相关支持。</p><p>● 至于 L3 未命中过滤（miss filtering）的工作方式，则是通过在 IBS 计算器溢出上标记指令、并在其引发 L3 miss 时生成一个不可屏蔽中断（NMI）而实现的。</p><p>● 该操作会丢弃 L3 未命中的样本，并使用随机值重置计数器 —— 对于获取性能性能监测单元（fetch pmu）是 1-15 之间，操作性能监测单元（op pmu）则是 1-127 之间。</p><p>● 当用户只对此类样本感兴趣时，该过滤方法将有助于减少采样开销，比如将数据提供给分层内存系统中的页面迁移守护进程时。</p><p>● 此外通过新添加的 l3missonly 性能监测单元属性，得以让 IBS 驱动程序支持对 L3 未命中过滤功能的支持。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0510/0af9cfa09120ed0.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0510/0af9cfa09120ed0.png" referrerpolicy="no-referrer"></a></p><p>WCCFTech 补充道，新提交的选项也有利于逐步添加相关编译功能。通过将 perf 硬件采样结构反馈给编译器，以帮助设计基于配置文件优化的二进制文件。</p><p>对于企业客户来说，除了查看用于潜在分析优化和问题调试的利用率之外，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 的 Zen 4 IBS 补丁还是颇具吸引力的 —— 尽管在 Linux 新版功能和硬件性能计数器等功能开发上，竞争对手 Intel 还是要更加积极一些。</p>   
</div>
            