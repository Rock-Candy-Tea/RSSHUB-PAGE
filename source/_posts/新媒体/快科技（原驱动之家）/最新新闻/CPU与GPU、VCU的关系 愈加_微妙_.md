
---
title: 'CPU与GPU、VCU的关系 愈加_微妙_'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210608/Sfa4e0814-a1fe-4a1f-8fab-91b9ce185a36.png'
author: 快科技（原驱动之家）
comments: false
date: Tue, 08 Jun 2021 20:33:39 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210608/Sfa4e0814-a1fe-4a1f-8fab-91b9ce185a36.png'
---

<div>   
<p>一个GPU总需要一个CPU，但CPU的选择已经不再单一，GPU的功能也不再“简单”，曾经稳固的关系，不再是单纯的合作。</p>
<p>四月份，英伟达发布了采用Arm架构的首款数据中心CPU Grace引发广泛关注。本月，外媒Tomshardware报道，像CPU一样总需要一个CPU的谷歌自研视频编解码处理单元Argos VCU，预计可以替换3000-4000万个英特尔CPU。</p>
<p>依赖CPU的GPU和VCU为什么会有替代CPU的势头？芯片巨头与互联网巨头间的竞合关系，是如何加深的？</p>
<p><strong>CPU市场的双重变化</strong></p>
<p>回答CPU与其它依赖CPU处理器关系变化之前，不妨先了解CPU市场本身的变化。在很长一段时间，由于CPU的性能已经足够满足包括PC在内的各种应用需求，再加上内存和带宽成为CPU性能提升的瓶颈。CPU王者英特尔在提升CPU性能动力不足，以及先进制程工艺进展不如预期的情况下，连续多代CPU性能提升幅度不大，被称作“挤牙膏”。</p>
<p>英特尔在领先位置缓慢前进的几年间，AMD凭借Zen架构的迅速迭代以及台积电先进制造工艺的加持，性能迅速接近甚至超越英特尔酷睿和至强CPU的性能。“AMD Yes”表达了消费者对于AMD产品迅速提升的认可。</p>
<p>英特尔和AMD的x86 CPU是PC时代的标志，然而在性能提升陷入瓶颈，以及先进半导体制程提升难度越来越大的背景下，两家最具代表性的CPU公司表现相差甚远，并且开始在市场份额上有所体现。</p>
<p>依旧有领先优势的英特尔感受到了老对手带来的竞争压力，因此无论是产品性能提升还是市场策略都更加积极。然而，英特尔在服务器CPU市场除了要面临同为x86阵营AMD的竞争，Arm阵营的公司也来势汹汹。</p>
<p><strong>Ampere董事长兼首席执行官Renee James说：“我们知道未来将与过去不同，因为软件环境变了，不再是关于PC和PC服务器的业务，而是围绕云和云边缘。现在，需要另一种不同的微处理器。”</strong></p>
<p>Ampere基于Arm Neoverse N1内核，推出了80核的Altra CPU和128核Altra Max CPU，持续刷新服务器CPU核心数的纪录，突出与x86 CPU相比更高的核数以及在云原生市场的优势。</p>
<p>同样是强调差异化优势，英伟达的Grace主要是面向数据密集型HPC和AI应用。英伟达首席执行官黄仁勋称基于Grace的系统与英伟达GPU紧密结合，性能将比目前最先进的NVIDIA DGX系统（在x86 CPU上运行）高出10倍。</p>
<p>无论是Ampere还是英伟达，其差异化高性能CPU的基础都是Arm。而Arm也在今年三月推出了面向未来十年的新一代架构Armv9，Arm希望将其架构在智能终端的成功扩展到高性能计算市场，包括边缘、云端及5G等。基于Armv9架构的Neoverse N2正是Arm向高性能市场拓展的关键产品。</p>
<p><strong>整体看来，已经在PC和服务器CPU市场大获成功的x86阵营正开始一场激烈的竞争。此时，面向云计算、AI的Arm架构CPU迅速发展，要在新兴市场分一杯羹。未来，RISC-V CPU会以怎样的方式参与到CPU市场的竞争，也让人充满期待。</strong></p>
<p><strong>异构时代，定制CPU优势突显</strong></p>
<p>CPU市场发生双重变化的一个关键因素是市场需求，在市场的驱动下，CPU的价值也更多体现在异构系统中。英伟达在今年四月发布Grace CPU的时候，也同时将其数据中心产品路线图升级为GPU+CPU+DPU的三类芯片，逐年飞跃，一个架构的策略。在这个新的策略中，GPU和DPU性能的充分发挥依旧需要有CPU强大的性能，也就是说，CPU计算和控制的基础和核心作用没有改变。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210608/fa4e0814-a1fe-4a1f-8fab-91b9ce185a36.png" target="_blank"><img alt="CPU与GPU、VCU的关系 愈加“微妙”" h="412" src="https://img1.mydrivers.com/img/20210608/Sfa4e0814-a1fe-4a1f-8fab-91b9ce185a36.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>变的是新兴应用对于算力的大幅快速增长，异构系统的性能是更重要的关注点。“目前市场上每年交付的3000万台数据中心服务器中，有1/3用于运行软件定义的数据中心堆栈，其负载的增长速度远远快于摩尔定律。除非我们找到加速的办法，否则用于运行应用的算力将会越来越少。”黄仁勋说，“新时代的计算机需要新的芯片、新的系统架构、新的网络、新的软件和工具。”</p>
<p>这也是英伟达推出DPU，并且将DPU归入其数据中心产品路线图的原因。“现代超大规模云技术推动数据中心从基础上走向了新的架构, 利用一种专门针对数据中心基础架构软件而设计的新型处理器, 来卸载和加速由虚拟化、网络、存储、安全和其它云原生AI服务产生的巨大计算负荷。BlueField DPU正是为此而生。”黄仁勋此前表示。</p>
<p><strong>异构组合才能更好满足未来市场的需求，这也已经是业界共识，从英特尔拥有CPU+GPU+FPGA+AI加速器的完整芯片组合，到英伟达宣布收购Arm，再到AMD宣布收购赛灵思，芯片巨头们都希望通过不同类型的芯片组合满足云计算、AI等计算更加密集应用的需求。</strong></p>
<p>在这种变化中，CPU的选择也会更加多样。Computex 21上，黄仁勋在回答雷锋网等提问时表示：“未来的世界非常多样，当然也会有不同的CPU，包括x86架构和Arm架构，大型CPU和小型CPU，面向边缘、数据中心、超算等CPU，我们的策略是在我们服务的市场，选择最合适的CPU，我们会继续支持x86 CPU。”</p>
<p>面向特定的市场，并非所有CPU都合适。因此在不同的市场需要不同的CPU，比如在笔记本电脑市场，英特尔的x86 CPU是不错的选择，在DGX系统中，AMD的CPU表现非常好。在5G基站中，基于Arm的Marvell CPU是一个理想选择。在云计算市场，Ampere的CPU性能出色。英伟达的CPU为的是解决AI推荐系统和自然语言理解这样大型AI模型的计算挑战。</p>
<p><strong>“我相信未来既需要通用CPU，也需要定制CPU。支持Arm和x86对我们来说都是很好的战略。”黄仁勋表示。</strong></p>
<p><strong>CPU与GPU、VCU更加微妙的竞合关系</strong></p>
<p>既有自研的Arm CPU，也支持x86 CPU，让英伟达与CPU巨头间的竞合关系中竞争的成分更高。在PC时代，芯片巨头间的竞争，是CPU公司或者GPU公司之间的竞争，CPU与GPU公司以合作为主旋律。</p>
<p>迈入AI时代，英伟达凭借其GPU硬件加上通用的软件，成为了AI芯片公司的代表，在AI市场成为了英特尔强大的竞争对手。<strong>面向市场空间巨大的云计算和5G市场，英伟达的GPU依旧离不开英特尔和AMD的CPU，但同时英伟达会更加注重Arm架构CPU的开发，芯片巨头间的竞合关系进一步加深。</strong></p>
<p><strong>这种关系变化更明显的转变在芯片巨头与互联网巨头之间。</strong>比如文章开头提到的谷歌Argos VCU，多年来谷歌都使用英特尔CPU中的视频编解码引擎，但随着视频内容越来越多，以及分辨率越来越高，谷歌需要性能更强但是功耗和成本更低的芯片。</p>
<p>定制的专用芯片性能往往会比通用芯片更强，通过自研核心功能加上集成第三方IP，能在规模应用中实现优势。谷歌表示，与英特尔Skylake驱动的服务器系统相比，其基于VCU的设备在性能、TCO（总体拥有成本）、计算效率方面实现了7倍（H.264）和高达33倍（VP9）的提升。</p>
<p>CPU、GPU 和配备 VCU 的系统离线双通道单输出 (SOT) 吞吐量</p>
<p>除了VPU，谷歌也已经通过自研的TPU减少了购买CPU和GPU。<strong>谷歌与芯片巨头们的关系，不再单纯是紧密的合作伙伴，在特定市场也成为了竞争对手。</strong></p>
<p><strong>对于这种转变，英特尔公司副总裁兼中国区总经理王锐此前对雷锋网(公众号：雷锋网)表示，“竞争对手可以在某一参数或者是在制程上缩短与我们的差距。但要打造整个架构，在计算和AI的各个方面都要能够赶超英特尔，不是那么容易的事情。”</strong></p>
<p>这是芯片巨头应对技术、市场变化的自信和底气，当然，芯片巨头们也需要更多地考虑与自研芯片的互联网巨头们的关系。</p>
<p><strong>不要忽略，无论是芯片巨头们之间的竞争，还是芯片巨头与互联网巨头们之间关系的变化，本质上除了市场和应用变化的驱动，还有成熟的芯片产业链，包括成熟的设计工具、IP、代工厂和封装，很大程度降低了GPU公司设计CPU，以及互联网巨头设计定制芯片的门槛。</strong></p>
<p>芯片行业的门槛还在进一步降低，这还会带来怎样的变化？</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210608/e13118a5ce004140a12cc629d754c164.jpg" target="_blank"><img alt="CPU与GPU、VCU的关系 愈加“微妙”" h="354" src="https://img1.mydrivers.com/img/20210608/s_e13118a5ce004140a12cc629d754c164.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/cpuchuliqi.htm"><i>#</i>CPU处理器</a><a href="https://news.mydrivers.com/tag/xianka.htm"><i>#</i>显卡</a></p>
<p class="url">
     <span>原文链接：<a href="https://www.leiphone.com/category/chipdesign/YGCUXJYnAc2XMP2c.html">雷锋网</a></span>
<span>责任编辑：万南</span>
</p>
        
</div>
            