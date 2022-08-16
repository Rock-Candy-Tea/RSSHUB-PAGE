
---
title: 'Linux 6.0-rc1 发布，Linus _也可以称之为 5.20 版本_'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=117'
author: 开源中国
comments: false
date: Tue, 16 Aug 2022 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=117'
---

<div>   
<div class="content">
                                                                                            <p>Linux 6.0 的第一个候选版本已发布，Linux 6.0 内核将在两个月内稳定下来。</p> 
<p>Linux 6.0 带来了超百万行代码，这些代码主要来源于 AMD GPU 和英特尔 Habana Labs Gaudi2 支持代码。下面是该版本一些重要的变更：</p> 
<ul> 
 <li><a href="https://www.oschina.net/news/205845/linux-char-misc-merge">合并大量 char/misc 代码，提供 Gaudi2 支持</a></li> 
 <li><a href="https://www.oschina.net/news/206435/f2fs-for-linux-6-0">引入 F2FS 低内存模式，用性能减少内存占用</a> </li> 
 <li><a href="https://www.oschina.net/news/206334/linux-6-0-loongarch">为 LoongArch 架构启用 PCI 和其他功能支持</a></li> 
 <li><a href="https://www.oschina.net/news/206091/linux-6-0-efi">为 Arm64 添加 UEFI 镜像内存和 ACPI PRM 支持</a></li> 
 <li><a href="https://www.oschina.net/news/205959/linux-6-0-media">将其 H.265/HEVC 用户空间 API 提升到稳定状态</a></li> 
 <li>大量英特尔 DG2/Alchemist 和 AMD RDNA3 图形改进</li> 
</ul> 
<p>但一些期待已久的内容，比如 Rust For Linux 的正式补丁尚未合并，增强性能的 MGLRU 工作也没有在这个版本中出现……也许会在 Linux 6.1 中合并。Linus Torvalds 还注意到最近出现的一些 Linux 内核崩溃，这些崩溃似乎是因为 VirtIO 合并，并且已经在解决中。</p> 
<p>有关该版本的详细改动，可在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flore.kernel.org%2Flkml%2FCAHk-%3DwgRFjPHV-Y_eKP9wQMLFDgG%2BdEUHiv5wC17OQHsG5z7BA%40mail.gmail.com%2FT%2F%23u" target="_blank">Linux 6.0-rc1 公告</a>中查看。</p> 
<p>有意思的是，Linus 在发布公告中认真地解释了采用 Linux 6.0 版本号的原因，还提到了中国开发者对“5.20 ”版本号的建议：</p> 
<blockquote> 
 <p>尽管主要版本号发生了变化，但这个版本并没有一些革新性的内容。“分层”编号系统的唯一原因是让版本号更容易记住和区分。这就是为什么每次在次版本号达到 20 左右时，我更喜欢增加主版本号，并重置次版本号的数字。</p> 
 <p>在我决定把这个内核称为 6.0之后，一些中国的开发者指出“5.20”是更好的版本号。如果你愿意把它叫做“Linux 5.20”，也可以继续这么叫。因为内核版本号真的完全是虚构的，没有任何内在的意义。</p> 
</blockquote> 
<p>最近几周 Linux 内核邮件的讨论一直在交替使用 5.20 和 6.0 两个版本号，直到 Linus 最终决定采用 6.0 。</p>
                                        </div>
                                      
</div>
            