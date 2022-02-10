
---
title: 'LoongArch处理器架构支持开始在LLVM中提供'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0210/db2a02140be54cb.jpg'
author: cnBeta
comments: false
date: Thu, 10 Feb 2022 11:08:54 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0210/db2a02140be54cb.jpg'
---

<div>   
<strong>今天早上，LLVM 15.0的开发树上出现了对中国的LoongArch
CPU架构的初始补丁。LoongArch是中科龙芯的新CPU架构，该公司长期为中国国内PC市场生产各种MIPS64芯片，他们在Linux下运行表现良好。</strong>LoongArch以MIPS64为基础，加入了RISC-V的一些概念，是中国在不依赖其他技术来源的情况下自主推动CPU制造业发展的努力的代表。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0210/db2a02140be54cb.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>Loongson 3 5000系列是第一个支持这种ISA的硬件。就目前初步的硬件和软件支持而言，LoongArch的性能在这一点上并不引人注目。在最近几个月里，已经有很多工作在针对LoongArch的编译器工具链和Linux内核提供支持，即使在某些方面意味着只是复制现有的MIPS64代码。</p><p>今天取得的里程碑是在开源的LLVM编译器堆栈中实现了初步的LoongArch ISA支持。最初的补丁已经被合并，但似乎仍是一项正在进行的工作，特别是在代码生成方面。Loongson的工程师们正在为LoongArch编译器的支持而努力，这与他们为GCC所做的工作相似。</p><p>大多数开源项目已经接受了对LoongArch的支持，而我们将在长期内看到这种CPU架构的可行性（和性能），以及它能与x86_64、Arm、RISC-V等竞争的程度，以及这种ISA最终是否能在中国以外的地区得到明显的应用。</p><p><strong>了解更多：</strong></p><p><a href="https://github.com/llvm/llvm-project/search?q=LoongArch&type=commits" _src="https://github.com/llvm/llvm-project/search?q=LoongArch&type=commits" target="_blank">https://github.com/llvm/llvm-project/search?q=LoongArch&type=commits</a><br></p>   
</div>
            