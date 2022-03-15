
---
title: '苹果M1 Ultra为何能实现性能翻倍？背后真相揭开'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220315/df0ecc10-477e-4668-b66e-05d7f07edc3d.jpg'
author: 快科技（原驱动之家）
comments: false
date: Tue, 15 Mar 2022 18:42:58 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220315/df0ecc10-477e-4668-b66e-05d7f07edc3d.jpg'
---

<div>   
<p>在当下的半导体行业中，Chiplet(芯粒)设计已经成为行业主流，推动Chiplet发展的AMD获益良多。</p>
<p>苹果在3月9日的发布会上推出自研的M1 Ultra芯片，通过UltraFusion架构将两个M1 Max芯片拼在一起，使芯片的各项硬件指标翻倍，性能也得到大幅提升。</p>
<p style="text-align: center"><img alt="苹果M1 Ultra为何能实现性能翻倍？背后真相揭开" h="437" src="https://img1.mydrivers.com/img/20220315/df0ecc10-477e-4668-b66e-05d7f07edc3d.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>性能方面，<strong>苹果M1 Ultra支持128GB高带宽、低延迟的统一内存，<span style="color:#ff0000;">内建20个CPU核心、64个GPU核心和32核神经网络引擎</span></strong>，每秒可提供高达22万亿次运算，其GPU性能是苹果M1芯片的8倍，比最新的16核PC台式机高90%。</p>
<p style="text-align: center"><img alt="苹果M1 Ultra为何能实现性能翻倍？背后真相揭开" h="382" src="https://img1.mydrivers.com/img/20220315/b1d88818-f0cb-4d4d-87ab-12879ab75feb.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>早在2021年10月的M1 Max中使用了UltraFusion技术，但直到M1 Ultra发布会上才正式公开。</p>
<p>UltraFusion架构使用硅中介层(Silicon Interposer)和微型凸块(Micro-Bump)，将芯片连接信号超过10000个，提供2.5TB/s超高处理器间带宽和低延迟。</p>
<p>UltraFusion的互联带宽其他多芯片互连技术的4倍多，<strong>领先于由英特尔、AMD、ARM、台积电和三星等众多行业巨头组成的通用芯粒互连联盟(UCIe)。</strong></p>
<p style="text-align: center"><img alt="苹果M1 Ultra为何能实现性能翻倍？背后真相揭开" h="322" src="https://img1.mydrivers.com/img/20220315/26faa636-5d95-4135-9239-f8b8510ed3e7.png" style="border: black 1px solid" w="508" referrerpolicy="no-referrer"></p>
<p>根据苹果公司和台积电已发表的专利和论文，从2.5D/3D互连和技术层面解析UltraFusion封装架构。</p>
<p>最近几年，随着摩尔定律的逐渐放缓，新的“摩尔定律2.0”开始被芯片厂商接受，摩尔定律2.0的核心，就是封装技术，让芯片封装从传统的2.5D升级到3D，这新技术包括了英特尔Foveros、台积电的3D晶圆键合(wafer-on-wafer)等。</p>
<p style="text-align: center"><img alt="苹果M1 Ultra为何能实现性能翻倍？背后真相揭开" h="370" src="https://img1.mydrivers.com/img/20220315/c71e1d8f-4c8f-42a2-aacc-f2f151241a5a.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>从M1 Ultra发布的UltraFusion图示可以看到，苹果M1 Ultra应该是采用台积电基于第五代CoWoS Chiplet技术的互连架构。</p>
<p>Chip-on-Wafer-on-Substrate with Si interposer(CoWoS-S)是一种基于TSV的多芯片集成技术，广泛应用于高性能计算(HPC)和人工智能(AI)加速器领域。</p>
<p>随着CoWoS技术的进步，可制造的中介层(Interposer)面积稳步增加，全掩模版尺寸及户翻了一番，从大约830mm2提升至1700mm2，中介层面积的增加，会让封装后的芯片的面积加大。</p>
<p>台积电第5代CoWoS-S达到最多三个全光罩尺寸(大约2500mm2)的水平，通过双路光刻拼接方法，让硅中介层可容纳1200mm2的多个逻辑芯粒和八个HBM(高带宽内存)堆栈，芯粒与硅中介层的采用面对面(互连层与互连层对接)的连接方式。</p>
<p>在UltraFusion技术中，<span style="color:#ff0000;"><strong>通过CoWo-S5的裸片缝合(Die Stitching)技术，可将4个掩模版拼接来扩大中介层的面积。</strong></span></p>
<p><strong>这种方法可让4个掩模被同时曝光，并在单个芯片中生成四个缝合的“边缘”。苹果公司的专利还提到，UltraFusion技术的片间互连可以是单层金属、也可以是多层金属。</strong></p>
<p style="text-align: center"><img alt="苹果M1 Ultra为何能实现性能翻倍？背后真相揭开" h="369" src="https://img1.mydrivers.com/img/20220315/23f02e18-6ff9-4769-bffd-23e68ec1845a.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>UltraFusion不仅是简单的物理连接结构，封装架构中还有6项特别优化过的技术。</p>
<p>第一项就是在UltraFusion芯片中，加入新的低RC(电容x电阻=传输延迟)金属层，它能够在毫米互连尺度上提供更好的片间信号完整性。</p>
<p>与传统的多芯片模块(MCM)等封装解决方案相比，UltraFusion的中介层在逻辑芯粒之间或逻辑芯粒和存储器堆栈之间提供密集且短的金属互连。拥有片间完整性更好、能耗更低，同时还能以更高的频率运行。</p>
<p>第二项就是互连功耗控制，UltraFusion使用可关闭的缓冲器(Buffuer)，进行互连缓冲器的功耗控制，有效降低暂停的互连线的能耗。</p>
<p>第三项是优化高纵横比的硅通孔(TSV)，TSV是硅中介层技术中另一个非常关键部分。UltraFusion/CoWoS-S5通过使用重新设计的TSV，优化传输特性，以适合高速SerDes传输。</p>
<p>第四项集成在中介层的电容(iCAP)，UltraFusion在中介层集成深沟槽电容器(iCap)，提升芯片的电源完整性。集成在中介层的电容密度超过300nF/mm2，帮助各芯粒和信号互连享有更稳定的供电。</p>
<p>第五项新的热界面材料，UltraFusion通过集成在CoWoS-S5中，使用热导率>20W/K的新型非凝胶型热界面材料(TIM)，拥有100%的覆盖率，提高各个高算力芯粒的散热能力，提升整体散热性能，降低积热。</p>
<p>第六项通过Die-Stitching技术有效提升封装良率降低成本，UltraFusion仅将KGD(Known Good Die)进行键合，避免传统WoW(Wafer on Wafer)或CoW(Chip on Wafer)中失效的芯粒被封装的问题，提升封装后的良率，降低整体的平均成本。</p>
<p style="text-align: center"><img alt="苹果M1 Ultra为何能实现性能翻倍？背后真相揭开" h="224" src="https://img1.mydrivers.com/img/20220315/d97c00e2-4d5c-43dd-ac28-29394fa34c11.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>编辑点评：苹果的UltraFusion技术充分结合封装互连技术、半导体制造和电路设计技术，为整合面积更大、性能更高的算力芯片提供巨大的想象空间。同时，M1 Ultra的成功，会让传统的芯片制造商，感受到更大的压力。</p>
<p>作为未来半导体的发展方向，先进封装技术在最近几年已得到广泛的应用，同时获得大众的认可。特别是越来越多厂商加入到自研芯片的大军，如何提升Chiplet之间的互联、再到与HBM或DDR内存之间的带宽，也是延续摩尔定律的焦点。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220315/e0459e93092c4f459b0530c1995e8826.jpg" target="_blank"><img alt="苹果M1 Ultra为何能实现性能翻倍？背后真相揭开" h="318" src="https://img1.mydrivers.com/img/20220315/s_e0459e93092c4f459b0530c1995e8826.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：振亭</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/pingguom1.htm">苹果M1</a><a href="https://news.mydrivers.com/tag/m1_pro.htm">M1 Pro</a><a href="https://news.mydrivers.com/tag/m1_ultra.htm">M1 Ultra</a>  </p>
        
</div>
            