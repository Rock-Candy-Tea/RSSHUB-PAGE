
---
title: '改进后的Zstd压缩算法被并入Linux 5.16 迎来性能大提升'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202111/619079058e9f092d5f7070a6_1024.jpg'
author: ZAKER
comments: false
date: Sat, 13 Nov 2021 18:57:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202111/619079058e9f092d5f7070a6_1024.jpg'
---

<div>   
<p>Zstd 被普遍用于 Linux 内核的各个领域用于数据压缩，从与 Btrfs 一样的透明文件系统压缩到允许内核模块用 Zstandard 算法进行压缩，但已经存在于内核中的代码已经过时多年了。<strong>而在 Linux 5.16 中，Zstd 的内核实现被提升到了最新标准，并提供了更好的性能。</strong></p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202111/619079058e9f092d5f7070a6_1024.jpg" data-height="226" data-width="234" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202111/619079058e9f092d5f7070a6_1024.jpg" referrerpolicy="no-referrer"></div></div>周六晚上为 Linux 5.16 合并的是 Linux 内核的 Zstd 代码，它经过了全面的修改。修订后的代码在 Zstd 的基础上加入了新内核风格封装的 API，这也有利于今后更容易更新，并可以自动生成 / 衍生出上游的 Zstd 源代码。<p></p><p>现有的 Zstd 内核代码已经有四年的历史了，在这段时间里，Zstd 的上游已经有了许多错误的修正和性能的优化。使用 Linux 5.16 的新代码，Btrfs Zstd 的解压速度可以提高 15%，SquasFS Zstd 的解压速度也可以提高 15%，F2FS Zstd 的解压速度可以提高 20%，zRAM 的解压速度可以提高 30%，内核 Zstd 图像的解压速度可以提高 35%，不仅如此，还有其他的优点。</p><p>在不久的将来，Zstd 还会有更多的性能优化，但想达到这个里程碑，首先需要将大修后的代码合并到主线上。Zstd 1.5.1 应该很快就会到来，以更好地统一繁杂的事务并提供最新的改进。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            