
---
title: 'AMD 3D V-Cache技术开发多年 在Ryzen 9 5950X样品中首次出现'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0807/6dac7348aa36038.jpg'
author: cnBeta
comments: false
date: Sat, 07 Aug 2021 14:40:06 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0807/6dac7348aa36038.jpg'
---

<div>   
<strong>几个月前，AMD发布了关于他们的Ryzen CPU新技术的信息。AMD的3D V-Cache技术带来多达64MB的额外L3缓存，并将其堆叠在Ryzen CPU的顶部。</strong>3D缓存从一开始就被设计为可堆叠。这证明了AMD在这项技术上已经持续了工作几年。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0807/6dac7348aa36038.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0807/6dac7348aa36038.jpg" title alt="AMD-3D-V-Cache-Stack-Chiplet-Design-For-Next-Gen-Ryzen-Desktop-CPUs-Lisa-Su-CEO.jpg" referrerpolicy="no-referrer"></a></p><p>现在，来自TechInsights网站的Yuzo Fukuzaki提供了更多关于<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>缓存技术新进展的细节，Fukuzaki在Ryzen 9 5950X样品上发现了具体的连接点。样品上还有一个额外空间的说明，通过提供更多的铜质连接点，为3D V-Cache创造了无障碍环境。</p><p>堆叠安装过程利用了一种叫做"硅通孔"的技术，即TSV，它通过混合粘合将SRAM的第二层连接到芯片上。在TSV中使用铜而不是通常的焊料，可以实现热效率和更多的带宽。这取代了使用焊料将两个芯片相互连接的做法。</p><p><a href="https://static.cnbetacdn.com/article/2021/0807/0f8a9fd911f48e8.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0807/0f8a9fd911f48e8.jpg" title alt="1628095021605-740x594.jpg" referrerpolicy="no-referrer"></a></p><p>他还在LinkedIn关于这个问题的文章中指出：为了应对memory_wall问题，缓存内存的设计很重要，这是缓存密度在工艺节点上的趋势，逻辑上的3D内存集成可以有助于获得更高的性能。随着AMD开始实现Chiplet CPU整合，他们可以使用KGD（Known Good Die）来摆脱模具的低产量问题。在IRDS（International Roadmap Devices and Systems）中，这一创新预计将在2022年实现。</p><p>TechInsights以反向方式深入研究了3d V-Cache的连接方式，并提供了以下发现的结果：</p><p>TSV间距；17μm</p><p>KOZ尺寸；6.2 x 5.3μm</p><p>TSV数量粗略估计；大约23000个</p><p>TSV工艺位置；在M10-M11之间（共15种金属，从M0开始）</p><p>我们暂时只能猜测AMD计划在其未来的结构中使用3D V-Cache，例如在不久的将来发布的Zen 4架构。这项新技术使AMD处理器在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>技术之上有了一个有利的飞跃，由于我们看到CPU核心数量每年都在增加，因此L3缓存的大小变得越来越重要。</p><p><a href="https://static.cnbetacdn.com/article/2021/0807/fe49c4c4d7e44ef.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0807/fe49c4c4d7e44ef.png" title alt="AMD-3D-V-Cache-Stack-Chiplet-Design-For-Next-Gen-Ryzen-Desktop-CPUs.png" referrerpolicy="no-referrer"></a></p>   
</div>
            