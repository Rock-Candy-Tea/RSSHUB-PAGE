
---
title: '英伟达希望通过Linux基金会的OPI项目来加速DPU的采用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0708/94e043106d2ec26.jpg'
author: cnBeta
comments: false
date: Fri, 08 Jul 2022 07:55:12 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0708/94e043106d2ec26.jpg'
---

<div>   
<strong>在收购 Mellanox 前，英伟达其实就已经酝酿过一种名叫“BlueField”的数据处理单元（以下简称 DPU）。</strong>据悉，DPU 允许加速器无需通过标准 x86 架构、即可立即访问网络。但在该公司于六年前披露相关细节后，期间它一直没有引发足够广泛的讨论。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0708/94e043106d2ec26.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（via <a href="https://wccftech.com/nvidia-accelerates-dpu-adoption-via-linux-foundation-project/" target="_self">WCCFTech</a>）</p><p>因相较于 PCIe 通道，CPU 其实更适合应用程序的管理，所以 BlueField 有望让该过程变得更加智能、同时减轻其它 PC 组件的工作负担。</p><p>最新消息是，即便当前只有少数公司在实际工作场所中使用 DPU，英伟达还是计划通过 Linux 基金会项目来推动并改进支持。</p><p><a href="https://static.cnbetacdn.com/article/2022/0708/b1e2ea3bad1c4b0.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0708/b1e2ea3bad1c4b0.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">JBOF 让直连 CPU 的所有初始化 PCIe 连接打通 NVMe 驱动器的数据传输</p><p><a href="https://www.storagereview.com/news/nvidia-accelerates-dpu-adoption-via-linux-foundation-project" target="_self">StorageReview</a> 指出：与常用的标准以太网 NIC 相比，DPU 的益处显而易见。其外观更像是一块微型计算板、拥有更强的处理性能，而不是单纯的“数据搬运工”。</p><p>此外 JBOF 可在不使用 x86 架构的情况下实现相同的操作，从而彰显了它的实用性和吸引力。系统使用两根 PCIe 3.0 排线，来连接一台或多台服务器的存储阵列。</p><p><img src="https://static.cnbetacdn.com/article/2022/0708/f5b0f11d3cfeb60.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（图 via StorageReview）</p><p>VAST Data 使用了英伟达当前基于 BlueField 设计的 DPU，其采用了高密度 1U 外形、可共享惊人的 675 TB 闪存存储。</p><p>另外 Fungible 打造了允许分解的 DPU 设计，StorageReview 能够访问其阵列，且 Fungible 最近表示打造了自家设计的 GPU 。</p><p>尴尬的是，由于需要大量软件才能与系统配合使用，这严重拖累了 BlueField DPU 的可访问性。</p><p>而要将相关产品部署到现有的系统，也没有想象中的那么轻松。最重要的是，标准存储企业正考虑转向更快速的设计和制造方法。</p><p><a href="https://static.cnbetacdn.com/article/2022/0708/ec2777ec737e44f.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0708/ec2777ec737e44f.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图 via StorageReview）</p><p>有鉴于此，英伟达正致力于通过成为 Linux 基金会的开放可编程基础设施项目（简称 OPI）的创始成员，来更好地推动 DPU 技术在市场上的普及。</p><p>这一举措可让 DPU 集成到更多系统中、易于访问且速度更快，且英伟达近期已在开源领域的更多 API 中启用 DOCA、以便广大开发者能够更快地采用。</p><p><img src="https://static.cnbetacdn.com/article/2022/0708/5f1bf4138df41ce.png" alt="5.png" referrerpolicy="no-referrer"></p><p>最后，该公司在 6 月 21 日的一篇<a href="https://blogs.nvidia.com/blog/2022/06/21/bluefield-doca-dpu-open-data-center/" target="_self">博客文章</a>中写道：“OPI 项目旨在创建一个由社区驱动、基于标准的开放生态系统，以借助 DPU 加速数据中心的网络和其它基础设施任务”。</p><p>至于 DOCA，其涵盖了驱动程序、库服务、文档、示例应用程序、管理工具等组件，旨在加速应用程序性能和简化开发工作。</p><p>它为使用加速驱动程序，或 DPDK、SPDK、Open vSwitch、Open SSL 的底层库编写的 BlueField 应用程序带来了更高的灵活性和可移植性。</p><p>英伟达将持续提供这方面的支持，且作为 OPI 的一部分，开发者们能够构建一个通用编程层，以支持诸多具有 DPU 加速功能的开放驱动程序和库。</p>   
</div>
            