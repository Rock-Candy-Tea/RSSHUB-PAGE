
---
title: 'AMD Zen 3调度器模型最终被添加到LLVM_Clang中'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0316/fa38f64f19ef4a8.jpg'
author: cnBeta
comments: false
date: Mon, 03 May 2021 11:51:17 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0316/fa38f64f19ef4a8.jpg'
---

<div>   
<strong>虽然在最后一分钟AMD Zen 3 "znver3 "的改进被合并到最近发布的GCC 11当中，但最近首次亮相的LLVM 12.0在Zen
3的支持方面并不那么幸运。</strong>在LLVM 12中，有非常基本的支持，但更完整的支持预计要到今年秋天的LLVM 13中才能实现。<br>
<p><strong>访问<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Zen 3调度器模型：</strong></p><p><a href="https://github.com/llvm/llvm-project/commit/2b93c9c16c586c26d20a5166c6ffbd71bc85b2e6" _src="https://github.com/llvm/llvm-project/commit/2b93c9c16c586c26d20a5166c6ffbd71bc85b2e6" target="_blank">https://github.com/llvm/llvm-project/commit/2b93c9c16c586c26d20a5166c6ffbd71bc85b2e6</a><br></p><p><a href="https://static.cnbetacdn.com/article/2021/0316/fa38f64f19ef4a8.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0316/fa38f64f19ef4a8.jpg" referrerpolicy="no-referrer"></a> </p><p>最初的"-march=znver3"支持进入了LLVM 12，但是Zen 3调整的调度器模型依然维持在八字只有一撇的情况（最初的调度器模型更新已经在1月份发布供审查）。直到这个周末，Zen 3调度器模型才在LLVM Git中登陆，用于LLVM 13.0，该版本将在9月~10月以稳定版的形式出现，如果在LLVM 12.0.1版本中对其进行反向移植，则会在这之前出现。</p><p>从头开始建立的全新Zen 3调度器模型依靠LLVM的llvm-mca机器代码分析器来生成真实的指令，到目前为止，这个新的调度器模型只进行了有限的测试/基准测试，积极的一面是RawSpeed新模型对一些工作负载有所帮主。</p><p>本次提交增加了1.43万行的新代码，提供了当前的Zen 3模型。不过很遗憾的是，由于时间窗口没有赶上，无法实现在AMD EPYC 7003系列推出时有良好的开箱即用的编译器支持，更不用提最好的时机是在去年Ryzen 5000系列推出之前。<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>方面早在2018年就在GCC和LLVM/Clang中加入了Icelake-Server，并因其在发布前及时启用开源而受到好评。</p><p>LLVM 13.0应该在9月或10月的时间框架内发布（LLVM 13的发布日历尚未公布，但他们一年中的第二个版本通常发生在那时），所以我们会看到在这个下一个开源编译器发布之前，AMD还有哪些优化可能会成为现实。</p>   
</div>
            