
---
title: '改进后的Zstd压缩算法被并入Linux 5.16 迎来性能大提升'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1114/5ac992426c33587.jpg'
author: cnBeta
comments: false
date: Sun, 14 Nov 2021 01:23:35 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1114/5ac992426c33587.jpg'
---

<div>   
Zstd被普遍用于Linux内核的各个领域用于数据压缩，从与Btrfs一样的透明文件系统压缩到允许内核模块用Zstandard算法进行压缩，但已经存在于内核中的代码已经过时多年了。<strong>而在Linux
5.16中，Zstd的内核实现被提升到了最新标准，并提供了更好的性能。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1114/5ac992426c33587.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>周六晚上为Linux 5.16合并的是Linux内核的Zstd代码，它经过了全面的修改。修订后的代码在Zstd的基础上加入了新内核风格封装的API，这也有利于今后更容易更新，并可以自动生成/衍生出上游的Zstd源代码。</p><p>现有的Zstd内核代码已经有四年的历史了，在这段时间里，Zstd的上游已经有了许多错误的修正和性能的优化。使用Linux 5.16的新代码，Btrfs Zstd的解压速度可以提高15%，SquasFS Zstd的解压速度也可以提高15%，F2FS Zstd的解压速度可以提高20%，zRAM的解压速度可以提高30%，内核Zstd图像的解压速度可以提高35%，不仅如此，还有其他的优点。</p><p>在不久的将来，Zstd还会有更多的性能优化，但想达到这个里程碑，首先需要将大修后的代码合并到主线上。Zstd 1.5.1应该很快就会到来，以更好地统一繁杂的事务并提供最新的改进。</p><p>关于这个大更新的更多细节，对于任何在内核中依赖Zstd压缩/解压的人来说，可以看这个Git合并的所有细节：</p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=c8c109546a19613d323a319d0c921cb1f317e629" _src="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=c8c109546a19613d323a319d0c921cb1f317e629" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=c8c109546a19613d323a319d0c921cb1f317e629</a><br></p><p>这个拉动请求是几天前提交的，但Linus Torvalds指出，鉴于它的影响，他希望推迟合并，以便有更多时间亲自审查代码。</p><p>如果你对Zstd的CPU性能基准感兴趣，请参阅OpenBenchmarking.org的网页，了解许多不同处理器的综合排名：</p><p><a href="https://openbenchmarking.org/test/pts/compress-zstd#results" _src="https://openbenchmarking.org/test/pts/compress-zstd#results" target="_blank">https://openbenchmarking.org/test/pts/compress-zstd#results</a><br></p>   
</div>
            