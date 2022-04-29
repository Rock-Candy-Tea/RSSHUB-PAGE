
---
title: '台积电确认苹果 M1 Ultra 采用 InFO-LSI 封装，将两片 M1 Max 连接到一起'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/4/a693f0e7-47df-4441-9e01-518c430ad7e4.jpg@s_2,w_820,h_461'
author: IT 之家
comments: false
date: Thu, 28 Apr 2022 14:57:06 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/4/a693f0e7-47df-4441-9e01-518c430ad7e4.jpg@s_2,w_820,h_461'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D2056699" rel="nofollow">OC_Formula</a> 的线索投递！</div>
            <p data-vmark="bd7a"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 4 月 28 日消息，在 M1 Ultra 官方发布会上，苹果介绍其 Mac Studio 中的 M1 Ultra 时表示，这是最强大的定制 Apple Silicon，它使用 UltraFusion 芯片对芯片互连技术，从而实现了 2.5TB / s 的带宽。</p><p data-vmark="3582" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/4/a693f0e7-47df-4441-9e01-518c430ad7e4.jpg@s_2,w_820,h_461" w="1024" h="576" alt="图 2：台积电详细介绍了 Apple 的 M1 UltraFusion 互连" title="台积电确认苹果 M1 Ultra 采用 InFO-LSI 封装，将两片 M1 Max 连接到一起" srcset="https://img.ithome.com/newsuploadfiles/2022/4/a693f0e7-47df-4441-9e01-518c430ad7e4.jpg 2x" width="1024" height="461" referrerpolicy="no-referrer"></p><p data-vmark="11f5">从介绍来看，这涉及到两个 M1 Max 芯片协同工作的问题。台积电现已证实，苹果 M1 Ultra 芯片其实并未采用传统的 CoWoS-S 2.5D 封装生产，而是使用了本地的芯片互连 (LSI) 的集成 InFO（Integrated Fan-out）芯片。</p><p data-vmark="2f21">IT之家了解到，苹果最新的 M1 系列产品基于台积电 5nm 工艺技术，但之前有媒体称其通用采用了台积电 CoWoS-S（chip-on-wafer-on substrate with silicon interposer）封装工艺。当然，台积电在使用其 CoWoS 封装平台为网络 IC 和超大 AI 芯片等多种芯片解决方案供应商提供服务方面拥有丰富经验，而且台积电还一直在使用先进工艺和 InFO_PoP 技术制造 iPhone 芯片。</p><p data-vmark="c546">实际上有很多种可以将芯片组桥接进行相互通信，但台积电的 InFO_LI 可以降低成本。半导体封装工程专业人士 Tom Wassick 放出了一张台积电在 3D IC 和异构集成国际研讨会上呈现的 PPT，阐明了其封装方法，显示苹果这次使用了 InFO_LI 技术。</p><p data-vmark="b0b4" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/4/77a4a9ba-00b8-451a-853a-2459a26f6dce.png" w="615" h="93" title="台积电确认苹果 M1 Ultra 采用 InFO-LSI 封装，将两片 M1 Max 连接到一起" width="615" height="93" referrerpolicy="no-referrer"></p><p data-vmark="0261" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/4/8f756ac3-3f84-4e02-aa1b-23c2a2fd23cb.png" w="553" h="183" title="台积电确认苹果 M1 Ultra 采用 InFO-LSI 封装，将两片 M1 Max 连接到一起" width="553" height="183" referrerpolicy="no-referrer"></p><p data-vmark="c07e">总的来说，CoWoS-S 是一种非常不错的方法，但要比 InFO_LI 更贵。除了这一点之外，Apple 没必要选择 CoWoS-S，毕竟 M1 Ultra 只需要完成两个 M1 Max 芯片的相互通信，而所有其他组件，包括统一的 RAM、GPU 和其他组件都是芯片中的一部分，因此，除非 M1 Ultra 改用信新型多芯片设计和更快的内存（如 HBM），否则 InFO_LI 对 Apple 来说就是更好的选择。</p><p data-vmark="6875" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/4/96b12e3e-35c8-4fdd-aede-3447fd36da60.png" w="1440" h="750" title="台积电确认苹果 M1 Ultra 采用 InFO-LSI 封装，将两片 M1 Max 连接到一起" width="1440" height="427" referrerpolicy="no-referrer"></p><p data-vmark="2fe9">具体而言，InFO-LSI 技术需要将一个本地 LSI (silicon interconnection) 与一个重分布层 RDL (redistribution layer) 相关联。与 CoWoS-S 相比，InFO-LSI 的主要优势在于其较低的成本。</p><p data-vmark="4f89">CoWos-S 需要用到大量完全由硅制成的大型中介层，因此成本非常昂贵；但 InFO_LI 凑合着用了本地化的芯片互连技术，总的来说没什么太大影响。</p><p data-vmark="a28e">值得一提的是，彭博社 Mark Gurman 称，苹果新一代 Mac Pro 已经准备就绪，它将搭载一款更强的芯片，也就是 M1 Ultra 的“继任者”。据称，这款产品的代号为 J180，此前的信息暗示，这款产品将采用台积电的下一代 4nm 工艺量产，而不是目前的 5nm 工艺。</p><p data-vmark="49c6">有传言称，新的苹果芯片将具有两个 M1 Ultra  相结合（4 个 M1 Max）。Gurman 早些时候表示，这款工作站将采用定制的芯片，最多可支持 40 核 CPU 和 128 核 GPU，性能值得期待，定价同样美丽。</p>
          
</div>
            