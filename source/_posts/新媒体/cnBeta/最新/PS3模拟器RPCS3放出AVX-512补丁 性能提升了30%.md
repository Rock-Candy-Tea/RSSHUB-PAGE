
---
title: 'PS3模拟器RPCS3放出AVX-512补丁 性能提升了30%'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0622/f5498e4c71d3e95.jpg'
author: cnBeta
comments: false
date: Wed, 22 Jun 2022 14:30:20 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0622/f5498e4c71d3e95.jpg'
---

<div>   
AVX-512在传统的消费级PC领域作用并不是很大，Intel在11代酷睿处理器短暂地加入AVX-512指令集后，又在12代酷睿上禁用了这一指令集，但这指令集对于PlayStation
3模拟器来说还是很有用的，RPCS3模拟器的开发者Whatcookie最近发布了一个补丁，它利用AVX-512指令让模拟器的性能提升了30%之多。<br>
 <p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0622/f5498e4c71d3e95.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0622/f5498e4c71d3e95.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0622/f5498e4c71d3e95.jpg" referrerpolicy="no-referrer"></a></p><p>到目前为止，AVX-512指令对于传统的PC游戏是没太大作用的，但对于PS3模拟器来说，支持AVX-512的CPU所具备的大型文件寄存器、数据级并行性和LLVM编译器是相当有用的，因为你需要模拟Cell处理器时就需要这些东西，LVVM编译器会自动选择可能的最佳代码路径，AVX-512还添加了新的掩码寄存器，可以选择与EVEX编码指令一起使用。</p><p>索尼的PS3用的是IBM的Cell处理器，该CPU拥有一个Power内核和八个协处理器，采用顺序执行和128位SIMD的专有指令集架构，因为通用性问题后续就没有游戏主机厂采用这种架构的处理器了，它多核多线程和数据级并行性的特性非常适合高性能计算领域，也适合编码、加密等工作，甚至是游戏领域，但想利用好的话学习成本很高，对于游戏厂商来说还得考虑多平台兼容的问题，这也是为什么索尼和<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>现在的主机都采用x86架构CPU的原因。</p><p>其实现在用Core i9-12900K使用RPCS3模拟器即使不用AVX-512也能达到每秒120帧以上，听上去这AVX-512补丁可有可无，但目前支持AVX-512的处理器性能大多都比Core i9-12900K低，对于它们来说性能提升30%效果还是相当明显的，而且未来<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>的锐龙7000处理器也会加入对AVX-512指令的支持。</p>   
</div>
            