
---
title: 'Hot Chips 34：摆脱x86束缚 英伟达详解Grace服务器CPU设计'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0825/05ee4c7c8db6d67.jpg'
author: cnBeta
comments: false
date: Thu, 25 Aug 2022 02:44:15 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0825/05ee4c7c8db6d67.jpg'
---

<div>   
<strong>在 Hot Chips 大会期间，英伟达详细介绍了该公司的 Grace CPU 设计。</strong>作为一种经典意义上的中央处理器，其旨在取代英特尔至强（Xeon）/ AMD 霄龙（EPYC）竞品，以在预先构建的高性能计算（HPC）服务器中扮演串行处理的角色 —— 因为每台服务器的六张 GPU 加速卡需要通过 CPU 进行互连。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0825/05ee4c7c8db6d67.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0825/05ee4c7c8db6d67.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（via <a href="https://wccftech.com/nvidia-grace-cpu-detailed-72-arm-v9-0-cores-117-mb-l3-cache-68-pcie-gen-5-lanes-tsmc-4n-process-500w-tdp/" target="_self">WCCFTech</a>）</p><p>据悉，该公司不仅研究了 CPU 层面的 I/O 与机器架构的瓶颈，还意识到了其计算服务器需要专门为这样的应用场景而定制中央处理器。</p><blockquote><p>得益于针对 NVIDIA API 的高度架构优化，Grace CPU 就此应运而生。</p><p>作为该公司首款服务器 CPU 产品，其效用可与 Intel / <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 竞品一较高下。</p></blockquote><p>作为一款单芯片，其采用了台积电 N4（4nm EUV）工艺制造，且英伟达将带有一两颗 Grace CPU + 一颗 H100 的板子称作 Superchip 或 Grace Hopper 超级芯片。</p><blockquote><p>可知每个Grace CPU 包含了一个 900 GB/s 的交换结构，以及一个带宽达到 PCIe 5.0 x16 七倍的 Coherent Interface 接口。</p><p>后者也是将相伴的 H100 或节点上相邻的超级芯片、与一致的内存访问连接起来的关键。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0825/cbd5ce7715226c0.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0825/cbd5ce7715226c0.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>Grace CPU 的串行处理能力，由 72 核心的 ARM v9 64-bit CPU 提供，而一枚超级芯片则包含了 144 个核心。</p><blockquote><p>主内存采用了 LPDDR5x 接口（支持 ECC），每个‘插槽’的带宽高达 1 TB/s —— 媲美超过 24 个通道的 DDR5 方案。</p><p>此外具有 68 条 PCIe 5.0 扮演了关键的串行 IO 接口角色，其主要被用于连接 NVMe 存储设备，且芯片的标称峰值 TDP 功耗达到了 500W 。</p></blockquote><p>随着 Grace CPU 的亮相，英伟达展示了该公司为企业和 HPC 应用场景设计大型多核处理器方面的强大工程实力。<a href="https://www.techpowerup.com/298095/nvidia-grace-cpu-specs-remind-us-why-intel-never-shared-x86-with-the-green-team" target="_self">TechPowerUp</a> 指出：</p><blockquote><p>鉴于 ARM 已大幅缩小与 x86-64 平台的性能、效率和 IPC 表现差距，我们也不难理解绿厂为何没能拿到蓝厂的 x86 许可，原本它有望交付出与<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>相媲<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://mideajiadian.jd.com/" target="_blank">美的</a>企业级处理器。</p><p>即便如此，英伟达的 DGX 计算节点、以及后续的更多预构建工作站 / 服务器（涵盖众多应用场景），势必将逐渐摆脱传统 x86 CPU、并用 Grace 及其继任者取而代之。</p></blockquote><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1275649.htm" target="_blank">NVIDIA推出用于HPC和AI场景的Grace和Grace Hopper超算芯片</a></p><p><a href="https://www.cnbeta.com/articles/tech/1308339.htm" target="_blank">NVIDIA Grace处理器详情公布：功耗500W、性能不及Zen2</a></p></div>   
</div>
            