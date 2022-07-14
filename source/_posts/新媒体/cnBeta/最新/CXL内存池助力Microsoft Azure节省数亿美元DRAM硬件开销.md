
---
title: 'CXL内存池助力Microsoft Azure节省数亿美元DRAM硬件开销'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0714/3d4304644800471.jpg'
author: cnBeta
comments: false
date: Thu, 14 Jul 2022 00:44:31 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0714/3d4304644800471.jpg'
---

<div>   
<strong>微软、Google、亚马逊等云计算巨头，都在以各种“实例”（Instance）和按需付费的方式，向广大客户提供其云端硬件资源。</strong>不过通常情况下，这些实例都会受到特定的 CPU 和内存配置的约束 —— 意味着客户智能从预设的几个选项中进行挑选、而无法进一步细分配置。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0714/3d4304644800471.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0714/3d4304644800471.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图 via <a href="https://semianalysis.substack.com/p/cxl-enables-microsoft-azure-to-cut" target="_self">SemiAnalisis</a>）</p><p>比如每多一个虚拟的 CPU 核心，就会往上添加 2GB 的内存。且在实例开启的过程中，预先分配的 CPU 与内存资源也被单个客户锁定，而无法在全局环境中动态调节。</p><p>长期以来，超大规模企业一直在努力思考如何缓和这方面的资源浪费 —— 毕竟许多示例没有充分利用其 DRAM，导致整个数据中心的使用效率低下。</p><blockquote><p>以 Microsoft Azure 为例，其测量结果表明 —— 近半虚拟机从未使用超过 50% 的预分配内存资源，这样的浪费是相当惊人的。</p><p>随着 CPU 资源的触顶，剩余的内存资源无法物尽其用，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>将这种状态称作内存搁浅（Memory Stranding）。</p><p>更让人感到震惊的是，多达 25% 的 DRAM 在任何特定时刻都可能被搁置。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0714/ab8a8e770f9d3d6.jpg" alt="3.jpg" referrerpolicy="no-referrer"></p><p>为了大幅改善这种情况，Microsoft Azure 想到了所谓的“内存池”（Memory Pooling）概念。</p><p>旨在允许 CPU 访问其所需的尽可能多的内存、而不占用或搁置不需要那么多 DRAM 资源的虚拟机。</p><blockquote><p>好消息是，全新的 CXL 缓存一致性协议，已经得到了各大主流硬件提供商的产品支持。</p><p>通过采用 CXL 硬件，微软等数据中心运营商有望大幅降低其 DRAM 成本。</p><p>假如最终得到 9~10% 的整体 DRAM 优化，大型云服务器提供商可轻松介绍数亿美元的内存硬件开销。</p></blockquote><p>此外微软估计，使用 CXL 和内存池技术，将使数据中心的服务器成本降低 4-5% —— 毕竟仅 DRAM 组件就占比超过了 50% 。</p><p><a href="https://static.cnbetacdn.com/article/2022/0714/efc3710369cd510.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0714/efc3710369cd510.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a></p><p>性能方面，Microsoft Azure 团队对一些使用本地 DRAM / 内存池的配置进行了基准测试，不过性能损失 / 最佳效果还是取决于具体的应用程序。</p><blockquote><p>一方面，Memory Pooling 会导致额外的 67-87 ns 延迟，导致某些应用程序的速度变得更慢。</p><p>另一方面，20% 左右的应用程序并未受到内存池的性能拖累，但有 23% 的应用程序性能损失不到 5% 。</p><p>此外 25% 的应用程序减速超 20%，12% 的应用程序减速超 30% 。</p></blockquote><p>需要指出的是，这只是微软在首批 CXL 硬件上展开的早期测试。展望下一代硬件和新的 CXL 协议规范，Memory Pooling 还有望带来更好的体验。</p>   
</div>
            