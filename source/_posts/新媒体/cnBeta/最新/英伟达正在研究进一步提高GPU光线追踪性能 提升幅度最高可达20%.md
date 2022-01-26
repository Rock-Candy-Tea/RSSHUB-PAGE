
---
title: '英伟达正在研究进一步提高GPU光线追踪性能 提升幅度最高可达20%'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0126/a73fc42f2f7bd72.jpg'
author: cnBeta
comments: false
date: Wed, 26 Jan 2022 12:05:28 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0126/a73fc42f2f7bd72.jpg'
---

<div>   
英伟达的研究人员一直的探究如何进一步提高GPU的光线追踪性能，有网友发现了英伟达近期发表的一篇论文，里面将“GPU Subwarp Interleaving”视为提高光线追踪性能的技术，提升幅度最高可达20%。<br>
 <p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0126/a73fc42f2f7bd72.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0126/a73fc42f2f7bd72.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0126/a73fc42f2f7bd72.jpg" referrerpolicy="no-referrer"></a></p><p>要实现如此大的性能提升并不是简单的事情，需要对微架构进行调整，否则技术的运用就会受到限制。由于新技术依赖于架构扩展，所以基本可以排除掉现有的Turing和Ampere架构，预计最快也要在Ada Lovelace架构之后的一代产品中才有可能看到。随着光线追踪技术在图形领域的运用越来越广泛，英伟达将会从多个角度解决光线追踪带来的性能问题，以保持自己产品的竞争力，并在营销上加以宣传。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0126/660f0393a97fb84.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0126/660f0393a97fb84.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0126/660f0393a97fb84.jpg" referrerpolicy="no-referrer"></a></p><p>在论文中，讨论了目前英伟达GPU的设计方式对光线追踪性能的限制。目前GPU为了满足大规模并行计算的需要，使用的是SIMD的执行模式，若干相同运算的输入会被打包成一组并行执行，这个组就是GPU的最小执行单元，英伟达称为“warp”。GPU通过对warp的调动来隐藏停顿，不过在实时光线追踪运算中，可能会出现问题从而导致性能的损失，而“GPU Subwarp Interleaving”则是解决目前GPU困境的一个解决方案。</p><p>研究人员在经过改造的增强型Turing架构GPU上，使用具有光线追踪工作负载的应用程序套件，实现了性能的提升，平均为6.3%，最高可达20%。现有的GeForce显卡不可能通过驱动程序更新获得这样的效果，只能将这项新技术应用到未来的架构中。</p>   
</div>
            