
---
title: '3D缓存版AMD EPYC处理器实测：性能提升约12%'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220123/s_7031b13f6710443499c9ef2abd881bec.jpg'
author: 快科技（原驱动之家）
comments: false
date: Sun, 23 Jan 2022 15:27:58 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220123/s_7031b13f6710443499c9ef2abd881bec.jpg'
---

<div>   
<p>在Zen 4全面铺开之前，AMD对Zen 3产品做了局部改良，分别推出了基于Zen3+的锐龙6000 APU、3D缓存版的锐龙5000X3D以及3D缓存版EPYC（Milan-X）。</p>
<p>3D缓存版作为极具特色的产品，到底性能Buff加成如何呢？</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220123/7031b13f6710443499c9ef2abd881bec.jpg" target="_blank"><img alt="3D缓存版AMD EPYC处理器实测：性能提升约12%" h="338" src="https://img1.mydrivers.com/img/20220123/s_7031b13f6710443499c9ef2abd881bec.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>根据Chips and Cheese对AMD EPYC 7V73X的测试，在不需求大缓存的OpenSSL中，实际频率更低的3D缓存版，居然还慢了2%。</p>
<p>不过在Gem5编译、7-Zip压缩等场景中，则提升了5~7%不等。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20220123/00b4b871a7864441b17269099eebe6c0.png" target="_blank"><img alt="3D缓存版AMD EPYC处理器实测：性能提升约12%" h="360" src="https://img1.mydrivers.com/img/20220123/s_00b4b871a7864441b17269099eebe6c0.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>汇总并考虑虚拟化测试中的频率损失，<strong>Chips and Cheese最终得出了3D缓存版综合性能提升12.5%这样的结论</strong>，坦率来说这可是远远低于AMD官方给出的超50%成绩。当然，AMD的场景是Synopsys VCS上实测EDA RTL验证工作负载。</p>
<p>回到产品本身，Milan 7003系列原本最多内部八个小芯片，每个自带32MB三级缓存，合计为256MB。</p>
<p>Milan-X 7003X系列则在每个小芯片上额外堆叠了64MB三级缓存，合计512MB。如果再算上4MB一级缓存、32MB二级缓存，一颗64核心的霄龙，就拥有恐怖的804MB缓存，双路就是几乎1.6GB！</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220123/c6ecfab1c5614d4c8c894d62928828a1.png" target="_blank"><img alt="3D缓存版AMD EPYC处理器实测：性能提升约12%" h="360" src="https://img1.mydrivers.com/img/20220123/s_c6ecfab1c5614d4c8c894d62928828a1.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/amd.htm"><i>#</i>AMD</a><a href="https://news.mydrivers.com/tag/huancun.htm"><i>#</i>缓存</a><a href="https://news.mydrivers.com/tag/xiaolong.htm"><i>#</i>霄龙</a><a href="https://news.mydrivers.com/tag/zen_3.htm"><i>#</i>Zen 3</a></p>
<p class="url">
     
<span>责任编辑：万南</span>
</p>
        
</div>
            