
---
title: '微软谷歌脸书网飞Isovalent宣布联手成立eBPF基金会'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0813/d1303ffe06348b7.png'
author: cnBeta
comments: false
date: Fri, 13 Aug 2021 03:02:18 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0813/d1303ffe06348b7.png'
---

<div>   
作为基础设施领域最具影响力的技术之一，eBPF 已在过去几年迎来了爆发式的增长。为更好地帮助和支持基于 eBPF 的开源项目之间的协作，<strong>包括微软、谷歌、脸书、网飞、Isovalent 在内的多家企业于今日宣布 —— 其已在 Linux 基金会麾下成立了一个全新的 eBPF 基金会。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0813/d1303ffe06348b7.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0813/d1303ffe06348b7.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（来自：Isovalent <a href="https://isovalent.com/blog/post/2021-08-ebpf-foundation-announcement" target="_self">官网</a>）</p><p>Isovalent 首席技术官兼联合创始人、同时也是新成立的 eBPF 管理委员会主任的 Thomas Graf 在一篇博客文章中表示：</p><blockquote><p>今天，我们宣布在 Linux 基金会麾下成立一个全新的 eBPF 基金会。</p><p>我们团队中的许多人，从早期就参与了相关开发工作，伴随它一路走过，且迎来了一个了不起的里程碑。</p><p>我们对在该技术创建过程中发挥的关键作用感到非常自豪，并将通过在 Linux 内核中共同维护该技术、以及几个主要的 eBPF 项目，来积极参与 eBPF 的未来开发。</p></blockquote><p>回顾历史：</p><blockquote><p>从 2014 年的一项 Linux 内核功能开始，eBPF 开始了它的旅程，并在同年编写提交了一个 Kubernetes 。</p><p>我还记得在 Linux Plumbers 会议上首次讨论了将 eBPF 添加到 Linux 内核的提议。</p><p>随着热度的增长，我们中的一些人开始看到围绕 eBPF 的巨大潜力，并最终成立了一家完整的公司。</p></blockquote><p>顾名思义，eBPF 与 BPF 有着共同的起源。BPF 起源于 BSD 社区，而 eBPF 合并到 Linux 内核的条件之一，就是要求不在内核中维护另一种字节码语言。</p><p>所以 eBPF 能够运行经典的 BPF 程序，同时顺理成章了铸就了“扩展 BPF”这个名称。</p><p><a href="https://static.cnbetacdn.com/article/2021/0813/519574b740072dc.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0813/519574b740072dc.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>为何创建 eBPF？</p><blockquote><p>从历史上看，由于内核具有监督和控制整个系统的特权能力，操作系统一直是实现可观察性、安全性和网络功能的理想场所。</p><p>同时，操作系统内核由于其核心作用、以及对稳定性和安全性的高要求而难以演进。</p><p>因此，与在操作系统之外实现的功能相比，操作系统级别的创新率，通常都是较低的。</p><p>eBPF 从根本上改变了这一点，通过允许沙盒程序在操作系统中运行，eBPF 使开发人员能够创建在运行时向操作系统添加功能的 eBPF 程序。</p><p>然后操作系统保证安全性和执行效率，就像在即时 (JIT) 编译器和验证引擎的帮助下进行本地编译一样。</p><p>这催生了一波基于 eBPF 的项目，涵盖了广泛的用例，包括下一代网络、可观察性、以及安全功能。</p></blockquote><p>eBPF 的当前应用：</p><blockquote><p>eBPF 很快就进入了大型数据中心的基础设施软件层，比如 Facebook 发布了基于 eBPF 的负载均衡器 Katran，且多年来一直在为该公司的数据中心提供支持。</p><p>最近，Facebook 工程师还撰写了关于使用 eBPF 进行大规模加密的文章，此外 eBPF 的适用范围不仅于此。</p><p>比如 Capital One 和 Adobe 均于 2020 年的 eBPF 峰会上分享了他们是如何通过 Cilium 项目，来利用 eBPF 助推其云原生 Kubernetes 环境中的网络、安全性和可观察性需求的。</p><p>eBPF 甚至已经成熟到 Google 决定将其引入自家托管的 Kubernetes 产品（GKE 和 Anthos），作为新的网络、安全性和可观察性层的地步。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2021/0813/78b71a8b0f03175.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0813/78b71a8b0f03175.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p>为何创立 eBPF 基金会？</p><blockquote><p>近年来，基于 eBPF 的项目数量呈爆炸式增长，并且越来越多的项目宣布有意开始采用该技术。eBPF 正迅速成为基础设施软件领域最具影响力的技术之一。</p><p>因此，优化项目之间的协作并确保 eBPF 的核心得到良好维护、并为 eBPF 的光明未来配备清晰的路线图和愿景的需求，也在日渐提升。</p><p>这就是 eBPF 基金会的用武之地，同时我们成立了一个 eBPF 指导委员会，来把关 eBPF 的技术方向和愿景。</p><p>此外随着 eBPF 普及移植到 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 内核和其它平台的，eBPF 程序可的移植性和 eBPF 运行时要求等问题，也变得愈加重要且需要协调。</p></blockquote><p>下一步的发展规划？</p><blockquote><p>eBPF 将持续快速发展，你可在项目目录中找到一组不断扩展的列表。尽管 eBPF 已被广泛部署，但我们仍处于让它开启一大波创新浪潮的早期阶段。</p></blockquote><p>最后，如果你想了解有关 eBPF 的更多信息，还请考虑免费注册即将于 8 月 18 至 19 日举行的虚拟 eBPF 峰会。</p>   
</div>
            