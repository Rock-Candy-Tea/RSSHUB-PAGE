
---
title: 'SSD 充当 HDD 缓存的技术，为什么没有被广泛运用？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://picx.zhimg.com/v2-bac9887ebb075156c30a391d37e393f2_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2022-09-08 00:54:34
thumbnail: 'https://picx.zhimg.com/v2-bac9887ebb075156c30a391d37e393f2_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">




<div class="question">


<div class="answer">

<strong>
<img class="avatar" src="https://picx.zhimg.com/v2-bac9887ebb075156c30a391d37e393f2_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">木头龙，</span><span class="bio">开了个新专栏，收录些老回答</span>
<a href="https://www.zhihu.com/question/40417425/answer/2660967883" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p><strong>很简单，普及速度赶不上 SSD 价格下降的速度。</strong></p>
<p>首先要说的是 SSD 给 HDD 当缓存其实是很有效的。以现代文件系统的数据组织结构，小容量闪存对于提升机械硬盘的随机文件访问速度的确是非常有帮助的。原理在于大部分文件系统是树型结构，要访问一个具体文件的物理存储位置，往往需要七八次甚至十数次的单线程单队列 4K 随机访问。因为机械硬盘的机械结构，定位到一个具体扇区平均需要 10ms 甚至更长时间的延迟，导致访问一个文件需要 0.1 秒甚至更多。而闪存因为是全电子操作，这个定位延迟可以缩短到数十μs 甚至数μs，几百倍的性能提升。如果把文件系统结构相关的元数据(Metadata)存储在闪存上作为机械硬盘的缓存，访问一个文件只需要定位一次，也可以获得十多倍的性能提升。更详细的解释，可以参看我之前写过的文章：</p>
<p><a class="internal" href="https://zhuanlan.zhihu.com/p/93032287">为什么说固态硬盘的 4K 性能很重要？</a></p>
<p>比较普及的用闪存作为机械硬盘缓存的技术，我认为应该是 2007 年 Windows Vista 推出时的 ReadyBoost。不过 ReadyBoost 用的闪存设备是 U 盘，一方面当时只有 USB 2.0（USB 3.0 在 2008 年才发布，支持 USB 3.0 的 Sandy Bridge 平台 2011 年才上市），持续写入速度还没硬盘快；另一方面 ReadyBoost 要求的 4K 随机读取 2.5 MB/s，十多年能符合这个要求的 U 盘可不便宜。所以 ReadyBoost 从来没有真正普及过。</p>
<p>而支持 USB 3.0 的 Sandy Bridge 平台上市时，Z68 就支持 Smart Respones Technology(SRT，智能响应技术)。但 Z68 主板的高昂价格对 SRT 普及造成了障碍；到了 Ivy Bridge 平台也只是下放到次高端的 H77 主板，直到 Haswell 平台最主流的 B85 才支持 SRT，此时已经是 2013 年了。</p>
<p>然鹅 SSD 的 NAND 闪存，2010 年三星开始量产 TLC 闪存，2013 年上市了 TLC 的 840 evo，2014 年上市了 3D V-NAND 的 850 系列。TLC 和 3D V-NAND 这两个技术大幅降低了 SSD 的成本，TLC + 3D V-NAND 的 850 evo 在 2015 年上市，240~256 GB 型号价格迅速降低到主流价位（500~600），二线品牌甚至有不到 400 的。例如太平洋电脑 2015 年底的一份入门级 SSD 评测中<sup>[1]</sup>，参测产品型号及参考价格如下：</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-27d315ca0851942b6b1e6edf1ed72220_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>256G SSD 成为主流后，主流电脑用户就没必要采用 SSD 缓存技术了——一般用户系统 + 应用程序也就占 100G 不到的存储空间，加上一些经常访问的常用文件也就占 200 不到。需要更大固态容量的大型软件、游戏用户，上 480~512G 的型号价格大概在 800~1200，也并非无法接受。机械硬盘就用来存储一些很少访问的冷数据如备份文件、归档项目文件等，或者占用存储空间大但又不太需要性能（尤其是随机访问性能）的多媒体文件，例如音乐、视频、照片等。</p>
<p><strong>SRT 的不足</strong></p>
<p>除了因为 SSD 价格快速下降外，Intel 的 SRT 未能普及还有几个 SRT 本身的原因。</p>
<p>首先是缓存的容量。SRT 只能支持最大 64GB 的缓存分区，主流用户应该是足够的，但对于需要数 TB 存储空间的用户来说，可能不太足够。一旦缓存容量不足，需要频繁替换缓存数据的话，加速效果会很差。</p>
<p>其次是启用 SRT 的步骤过于呆板。启用 SRT 需要在 Windows 环境下使用 Intel RST（Rapid Storage Technology，快速存储技术，不要和 SRT 混淆）的客户端操作，并且要求 SSD 上没有任何分区。</p>
<p>所以如果新装机，SSD 容量在 120G 以上，为了不浪费 SSD 的容量和性能，想把系统和应用安装到剩余的 SSD 空间会很麻烦。用户需要：</p>
<ol>
<li>在机械硬盘上安装 Windows；</li>
<li>安装 RST，在 RST 界面中启用 SRT，用固态给机械硬盘加速；</li>
<li>在 SSD 的剩余空间中建立分区，安装 Windows；</li>
<li>在 SSD 上的 Windows 中安装 RST；</li>
<li>删除 HDD 上的 Windows（可选）。</li>
</ol>
<p>一旦 SRT 出现错误，需要停止并重新启用的话就更麻烦了——你需要先备份 SSD 上系统盘中的数据，清除所有 SSD 上的分区，然后重复上述操作…</p>
<p>从 Skylake 开始，Intel 开始主推傲腾加速方案，SRT 在后续平台上相当于被废掉了。和 SSD 方案相比，傲腾虽然性能更好，也无需 TRIM 和 GC 加速效果更好，但因为介质成本高，接受程度就更差了。</p>
<p>最后就是，SSD 给 HDD 缓存在一些同时需要大容量存储空间和读写性能的场景中其实很常见。例如高端 NAS、混合磁盘阵列等。如果是电脑需要类似的混合存储，可以考虑 Windows 自带的存储空间建立分层存储池。</p>
<p><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//support.microsoft.com/zh-cn/windows/%25E5%25AD%2598%25E5%2582%25A8%25E7%25A9%25BA%25E9%2597%25B4-windows-b6c8b540-b8d8-fb8a-e7ab-4a75ba11f9f2%23WindowsVersion%3DWindows_" target="_blank" rel="nofollow noreferrer">存储空间 Windows</a></p>
<p>能接受 200 块钱的软件许可费用话，个人推荐使用 PrimoCache，使用上灵活很多，可以用 SSD 上的一个分区来加速机械硬盘、加速机械硬盘上的多个分区或者多块机械硬盘；也支持用内存给 SSD 加速；可以选择多种写入策略。</p>
<p><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//www.romexsoftware.com/zh-cn/primo-cache/index.html" target="_blank" rel="nofollow noreferrer">PrimoCache - 加速各种存储设备的缓存软件</a></p>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/40417425">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            