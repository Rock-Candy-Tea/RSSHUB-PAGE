
---
title: '3D缓存版AMD EPYC处理器实测：性能提升约12%'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0123/4888e28d2d22c21.jpg'
author: cnBeta
comments: false
date: Sun, 23 Jan 2022 08:33:26 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0123/4888e28d2d22c21.jpg'
---

<div>   
在Zen 4全面铺开之前，AMD对Zen 3产品做了局部改良，分别推出了基于Zen3+的锐龙6000 APU、3D缓存版的锐龙5000X3D以及3D缓存版EPYC（Milan-X）。3D缓存版作为极具特色的产品，到底性能Buff加成如何呢？<br>
 <p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0123/4888e28d2d22c21.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0123/4888e28d2d22c21.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0123/4888e28d2d22c21.jpg" referrerpolicy="no-referrer"></a></p><p>根据Chips and Cheese对<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> EPYC 7V73X的测试，在不需求大缓存的OpenSSL中，实际频率更低的3D缓存版，居然还慢了2%。</p><p>不过在Gem5编译、7-Zip压缩等场景中，则提升了5~7%不等。</p><p><img src="https://static.cnbetacdn.com/article/2022/0123/97e77b6246c9c1a.png" referrerpolicy="no-referrer"></p><p>汇总并考虑虚拟化测试中的频率损失，<strong>Chips and Cheese最终得出了3D缓存版综合性能提升12.5%这样的结论</strong>，坦率来说这可是远远低于AMD官方给出的超50%成绩。当然，AMD的场景是Synopsys VCS上实测EDA RTL验证工作负载。</p><p>回到产品本身，Milan 7003系列原本最多内部八个小芯片，每个自带32MB三级缓存，合计为256MB。</p><p>Milan-X 7003X系列则在每个小芯片上额外堆叠了64MB三级缓存，合计512MB。如果再算上4MB一级缓存、32MB二级缓存，一颗64核心的霄龙，就拥有恐怖的804MB缓存，双路就是几乎1.6GB！</p><p><img src="https://static.cnbetacdn.com/article/2022/0123/55952566899b5ec.png" referrerpolicy="no-referrer"></p>   
</div>
            