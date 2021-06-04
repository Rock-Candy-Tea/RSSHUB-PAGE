
---
title: '谷歌自研芯片 替代上千万颗英特尔CPU'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210604/S7bfb8b3e-bf0a-4ac7-84eb-a43ed3e53a23.png'
author: 快科技（原驱动之家）
comments: false
date: Fri, 04 Jun 2021 19:33:06 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210604/S7bfb8b3e-bf0a-4ac7-84eb-a43ed3e53a23.png'
---

<div>   
<p>伴随着新兴应用的兴起以及数字化程度越来越高，已有的成熟处理器在性能、效率以及成本上的优势相较自研芯片的优势越来越小，因此借助成熟的第三方IP以及EDA工具和代工厂，科技巨头们纷纷开始自研芯片，其中最有代表性的就是谷歌TPU，除此之外，谷歌Argos VCU也值得关注。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210604/7bfb8b3e-bf0a-4ac7-84eb-a43ed3e53a23.png" target="_blank"><img alt="谷歌自研芯片 替代上千万颗英特尔CPU" h="265" src="https://img1.mydrivers.com/img/20210604/S7bfb8b3e-bf0a-4ac7-84eb-a43ed3e53a23.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>谷歌设计了自己的新处理器Argos 视频（转）编码单元 (VCU)，其目的只有一个：处理视频。高效的新芯片使这家技术巨头能够用自己的芯片替换数千万颗英特尔 CPU。 </p>
<p>多年来，英特尔内置于其CPU中的视频编解码引擎一直主导着市场，因为它们提供了领先的性能和功能，并且易于使用。但是定制的专用集成电路 (ASIC) 的性能往往优于通用硬件，因为它们仅针对一种工作负载而设计。因此，谷歌转而为YouTube的视频处理任务开发自己的专用硬件，并取得了很好的效果。 </p>
<p>不过，英特尔可能会利用其最新技术来赢回谷歌的专业视频处理业务。 </p>
<p><strong>谷歌为什么自研VCU？</strong></p>
<p>数据显示，用户每分钟向YouTube上传超过500小时的各种格式的视频内容。Google需要将该内容快速转码为多种分辨率（包括144p、240p、360p、480p、720p、1080p、1440p、2160p和4320p）和数据高效格式（例如，H.264、VP9 或 AV1），这需要强大的编码能力。  </p>
<p>过去，谷歌有两种转码/编码内容的选择。第一个选项是英特尔的视觉计算加速器(VCA)，它包含三个Xeon E3 CPU，内置Iris Pro P6300/P580 GT4e集成图形内核和先进的硬件编码器。第二种选择是使用软件编码和通用英特尔至强处理器。</p>
<p>谷歌认为，对于YouTube的工作负载来说，这两种选择都不够节能。视觉计算加速本身就相当耗电，而至强CPU的数量本质上要增加服务器的数量，这意味着额外的功率和数据中心占用空间。因此，谷歌决定采用自研的定制硬件。 </p>
<p>谷歌的第一代 Argos VCU 并没有完全取代英特尔的CPU，因为服务器仍然需要运行操作系统并管理存储驱动器和网络连接。在很大程度上，谷歌的Argos VCU就像一个总是需要一个CPU的GPU。 </p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210604/3827ff63-0d8d-4645-9a2b-cf76667be203.png" target="_blank"><img alt="谷歌自研芯片 替代上千万颗英特尔CPU" h="537" src="https://img1.mydrivers.com/img/20210604/S3827ff63-0d8d-4645-9a2b-cf76667be203.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>谷歌的VCU与GPU中的流处理器不同，它集成了10个H.264/VP9编码器引擎、几个解码器内核、4个LPDDR4-3200内存通道（具有 4x32 位接口）、1个PCIe接口、1个DMA引擎和1个用于调度目的的小型通用内核。</p>
<p>VCU除了自研的编码器/转码器外，大多数IP都从第三方获得许可，以降低开发成本。每个 VCU还配备了8GB的可用ECC LPDDR4内存。  </p>
<p>实际上，谷歌研发VCU的理念是将尽可能多的高性能编码器/转码器放入单个硅片中（同时保持节能），然后将VCU的数量与所需的服务器数量分别扩展。谷歌在一块板上放置两个 VCU，然后在每个双插槽英特尔至强服务器上安装10个卡，大大提高了每个机架的解码/转码性能。</p>
<p><strong>VCU加速替代CPU</strong></p>
<p>谷歌表示，与英特尔Skylake驱动的服务器系统相比，其基于VCU的设备在性能、TCO（总体拥有成本）、计算效率方面实现了7倍（H.264）和高达33倍（VP9）的提升。这样的提升带来的成本优势（VCU与英特尔的 CPU 相比），使得 VCU 成为视频巨头YouTube的更好选择。 </p>
<p style="text-align: center"><img alt="谷歌自研芯片 替代上千万颗英特尔CPU" h="385" src="https://img1.mydrivers.com/img/20210604/81269db0-7eb6-4146-b785-49c21801daa0.png" style="border: black 1px solid" w="598" referrerpolicy="no-referrer"><br>
CPU、GPU 和配备 VCU 的系统离线双通道单输出 (SOT) 吞吐量</p>
<p>从谷歌分享的性能数据看，很明显单个Argos VCU仅比H.264 中的2路Skylake 服务器CPU快。但是，由于可以在单个服务器中安装20个VCU，从效率的角度来看，VCU胜出。但对于要求更高的VP9编解码器，谷歌的VCU似乎比英特尔的双路至强快五倍，有令人印象深刻的效率优势。 </p>
<p>自从谷歌拥有Argos VCU，它用自己芯片取代了许多基于至强的YouTube服务器。很难估计谷歌实际更换了多少至强系统，但一些分析师认为，这家科技巨头本可以将3300-4000万个英特尔CPU换成 自己的 VCU，即使第二个数字被高估了，单位仍然是数百万个。  </p>
<p>由于谷歌的其他服务需要大量处理器，因此该公司从AMD或英特尔购买的CPU数量可能仍然非常高，并且不会很快减少，因为谷歌自己的数据中心级芯片的使用需要数年时间。</p>
<p>还值得注意的是，目前谷歌为了尝试使用创新的编码技术（例如，AV1），YouTube 需要使用通用CPU，因为Argos不支持新编码技术的编解码。此外，随着更高效的编解码器的出现，这些编解码器对计算能力的要求往往更高，谷歌将不得不继续使用 CPU 进行部署。</p>
<p>但具有讽刺意味的是，专用硬件的优势在未来只会越来越大。谷歌已经在开发支持AV1、H.264 和VP9编解码器的第二代VCU，因为它需要进一步提高其编码技术的效率。目前尚不清楚谷歌何时会部署新的VCU，但很明显该公司希望尽可能使用自己的处理器而不是通用处理器。 </p>
<p><strong>英特尔并未停滞不前</strong></p>
<p>不过，英特尔并没有停滞不前。该公司 基于DG1 Xe-LP的 四芯片SG1服务器卡可以解码多达28路4Kp60流以及同时转码多达12路。本质上讲，英特尔的SG1与谷歌的Argos VCU 所做的工作完全一样：将视频解码和转码性能与服务器数量分开，从而减少用于视频应用的数据中心所需的通用处理器数量。  </p>
<p>凭借即将推出的Xe-HP GPU，英特尔将同时提供10个高质量4Kp60流的转码。请记住，某些Xe-HP GPU将扩展到四个区块，并且每个系统可以安装一个以上的GPU，英特尔在领先的媒体解码和编码能力市场只会变得更加稳固。</p>
<p><strong>总结</strong></p>
<p>Google 已成功构建了出色的H.264和支持VP9的视频（转）编码单元 (VCU)，与英特尔现有的CPU相比，它可以在视频编码/转码工作负载方面提供显着更高的效率。此外，VCU 使 谷歌能够独立于服务器数量扩展其视频编码/转码性能。  </p>
<p>然而，英特尔已经拥有Xe-LP GPU和SG1卡，它们也提供了一些重要的视频解码和编码功能，因此英特尔仍将在具有繁重视频流工作负载的数据中心取得成功。此外，随着英特尔 Xe-HP GPU的出现，该公司有望巩固其在该市场的地位。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210604/99cdf8de10d14751971cd1dae8e310ee.jpg" target="_blank"><img alt="谷歌自研芯片 替代上千万颗英特尔CPU" h="354" src="https://img1.mydrivers.com/img/20210604/s_99cdf8de10d14751971cd1dae8e310ee.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/intel.htm"><i>#</i>Intel</a><a href="https://news.mydrivers.com/tag/guge.htm"><i>#</i>谷歌</a></p>
<p class="url">
     <span>原文链接：<a href="https://www.leiphone.com/category/chipdesign/s2FIAB3LQ0aiG4yS.html">雷锋网</a></span>
<span>责任编辑：万南</span>
</p>
        
</div>
            