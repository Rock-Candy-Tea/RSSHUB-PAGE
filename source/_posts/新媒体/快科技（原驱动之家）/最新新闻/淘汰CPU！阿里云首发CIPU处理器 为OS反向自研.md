
---
title: '淘汰CPU！阿里云首发CIPU处理器 为OS反向自研'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220613/S8ce67359-704c-4d8c-bdc3-8c2795a1010a.jpg'
author: 快科技（原驱动之家）
comments: false
date: Mon, 13 Jun 2022 12:05:31 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220613/S8ce67359-704c-4d8c-bdc3-8c2795a1010a.jpg'
---

<div>   
<p>阿里硬件研发，又有大动作。</p>
<p>刚刚，阿里云正式对外发布全新处理器：CIPU。</p>
<p><strong><span style="color:#ff0000;">不仅架构全自研，还号称要“替代CPU成为新一代云计算核心硬件”！</span></strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220613/8ce67359-704c-4d8c-bdc3-8c2795a1010a.jpg" target="_blank"><img alt="淘汰CPU！阿里云首发CIPU处理器 为OS反向自研" h="433" src="https://img1.mydrivers.com/img/20220613/S8ce67359-704c-4d8c-bdc3-8c2795a1010a.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>云计算搞了这么些年，CPU在数据中心可一直还是牢牢占据“C位”。</p>
<p>就在去年，阿里还花大力气推出了5nm的服务器CPU倚天710。</p>
<p>这怎么就突然要打破传统了呢？</p>
<p>CIPU，这个比CPU多了一个I的新面孔，究竟什么来头？</p>
<p><strong>CIPU究竟是什么？</strong></p>
<p>CIPU全称Cloud Infrastructure Process Units，意为<strong>云基础设施处理器。</strong></p>
<p>从名字上就能看出，这是一颗云端处理器，专门用于连接服务器内硬件和云上虚拟化资源。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220613/1dc4a677-53c0-4dff-bf59-7b5ee509950a.png" target="_blank"><img alt="淘汰CPU！阿里云首发CIPU处理器 为OS反向自研" h="398" src="https://img1.mydrivers.com/img/20220613/S1dc4a677-53c0-4dff-bf59-7b5ee509950a.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
△CIPU架构图</p>
<p>据阿里云介绍，之所以用CIPU取代以CPU为核心的架构，就是为了更好地“压榨”服务器硬件、获取更多虚拟化资源，并让已有的资源用起来更顺手。</p>
<p><strong>软件上，CIPU接入飞天云操作系统，更高效地完成虚拟化资源编排调度的工作；</strong></p>
<p><strong>硬件上，飞天操作系统通过CIPU能快速云化管理数据中心物理设备，并对网络和存储硬件进行加速，这样一来不仅不会再浪费CPU的算力，还能增强网络和存储性能。</strong></p>
<p>从功能来说，它拥有四大特性：</p>
<p>云原生最佳载体，即每个裸金属系统能运行2000个容器，并用沙箱容器技术为容器提供更安全的隔离，链路启动速度在50ms以内；</p>
<p>芯片直接实现IO引擎，其中存储I/O操作每秒可进行300万次，网络I/O最高每秒5000万个分组数据包，存储长尾时延降低50%；</p>
<p>芯片级安全加固，即能高速卸载加密后的数据，将芯片级硬件的不可篡改性映射到软件上；</p>
<p>增强型融合网络，即在RDMA技术加持下，网络延迟最低达到5微秒，带宽最高能达到200GB。</p>
<p><strong>从性能来说，它又给计算、存储和网络三类资源带来了不少提升。</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220613/f7bece17-b811-4aff-836d-4cc5bee56ed4.png" target="_blank"><img alt="淘汰CPU！阿里云首发CIPU处理器 为OS反向自研" h="382" src="https://img1.mydrivers.com/img/20220613/Sf7bece17-b811-4aff-836d-4cc5bee56ed4.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>计算上，CIPU能快速接入不同类型资源的神龙云服务器，单容器虚拟化消耗减少50%，启动速度快350%。以运行部分数据库和服务器为例，Nginx性能就提升了89%，Redis提升68%，MySQL提升60%，此外对于AI和大数据场景也有提升。</p>
<p>存储上，CIPU能对存算分离架构的块存储接入进行硬件加速，存储时延最低达到30微秒，带宽最高200Gbps，支持云上多计算节点NVME共享访问云盘块存储，Oracle RAC、SAP Hana等高可用数据库无缝上云。</p>
<p>网络上，CIPU对高带宽物理网络进行了硬件加速，基础带宽达到200GB，并采用自研的RDMA-Solar协议，网络时延降低至16us，相较自建物理机的集群吞吐量提升30%、业务高峰期延迟下降90%。</p>
<p><strong>有意思的是，阿里云这款CIPU处理器，其实已经在内部打磨好几年了。</strong></p>
<p>它最初的“灵感”，来自于阿里云内部一个叫做神龙卡的设备。</p>
<p>神龙卡诞生于2017年，从功能上来讲有点类似于AWS发布的一款名叫Nitro的平台（集成了虚拟机监视器、带外管理等功能），甚至比AWS发布的时间更早一点。</p>
<p>经过了好几轮迭代后，神龙卡逐渐加入了编排调度、硬件加速等更多能力，最终诞生了CIPU的雏形，随后也在继续完善这一款产品。</p>
<p>一方面，据阿里云智能云架构总监黄瑞瑞介绍，在这几年里，CIPU已经承受过像“双十一”这种体量的性能&压力“测试”了。</p>
<p>另一方面，有不少阿里云的客户，也或多或少已经使用过基于CIPU的云计算服务。虽然客户可能对底层硬件层没有直接的感知，但阿里云的网络、存储等性能，这几年确实在不断上升，例如，不久前阿里云就成为国内唯一获评全球十大计算机网络研究机构的中国企业。</p>
<p>如今来看，CIPU的出现确实再次打破了云计算的“瓶颈”，将整体性能提升了一大部分。</p>
<p>不过，要说推翻CPU在云数据中心里“C位”的想法，倒也不是阿里一家有之。</p>
<p>在市面上相似概念的产品里，CIPU相比IPU、DPU来说，又究竟有什么不同？</p>
<p><strong>为什么是CIPU？</strong></p>
<p>要说清楚这件事儿，还是得从云计算技术的发展历程说起。</p>
<p>过去十几年来云计算技术的发展，可以大体分为两个阶段。</p>
<p>第一阶段，在分布式技术的推动之下，互联网企业开始将业务从大型机向分布式系统迁移，打下了分布式架构的底座。</p>
<p>第二阶段，资源池化技术出现。这一技术通过计算存储分离的架构，实现了对资源的统一调度编排，使得弹性计算成为可能。</p>
<p>对于用户而言，这也就意味着云计算可靠性和可用性的极大提升。</p>
<p>在这两个阶段，计算体系架构都是以CPU为核心的。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220613/66ee42b6-69cf-474d-8f28-7607b1585692.png" target="_blank"><img alt="淘汰CPU！阿里云首发CIPU处理器 为OS反向自研" h="396" src="https://img1.mydrivers.com/img/20220613/S66ee42b6-69cf-474d-8f28-7607b1585692.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>但当云计算发展到今天，以大数据应用为代表的数据密集型场景越来越多，这种以CPU为中心的架构便开始暴露短板：</p>
<p>首先，以CPU为中心的架构会导致计算和网络传输之间的时延较大。</p>
<p>其次，大数据应用增多，导致数据中心内部数据迁移量增大，以CPU为中心的架构无法提供高带宽。</p>
<p>再者，以阿里云为例，其在全球27个国家和地区、84个可用区管理着上百万台服务器。但以CPU为中心的架构很难解决这种超大规模基础设施的复杂管理问题。</p>
<p>如此一来，解决之道也就指向了一个方向：<strong>打破以CPU为中心的传统云计算体系架构，定义新一代云计算基础技术。</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220613/bba30401-4fe0-4361-a7f5-cc21874cf3c7.png" target="_blank"><img alt="淘汰CPU！阿里云首发CIPU处理器 为OS反向自研" h="333" src="https://img1.mydrivers.com/img/20220613/Sbba30401-4fe0-4361-a7f5-cc21874cf3c7.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>而这也正是如今各大厂商所追逐的最新技术热点。</p>
<p>比如英伟达的DPU（Data Processing Units），2020年10月一经发布，便在业界引发热议。</p>
<p>顾名思义，DPU侧重解决的是数据迁移带宽的问题。作为集成加速平台，DPU能够从CPU上卸载关键的网络、存储和安全任务，降低CPU的开销。</p>
<p>老黄当时表示：</p>
<p>数据中心已成为新型计算单元，而DPU是其重要的组成部分。CPU、GPU和DPU的结合，可构成完全可编程的单一AI计算单元，提供前所未有的安全性和算力。</p>
<p>而英特尔也紧随其后，提出了“IPU”（Infrastructure Processing Units）的概念。</p>
<p><strong>相比于DPU，IPU更强调虚拟化云化能力，通过网络虚拟化、存储虚拟化、网络存储管理以及安全等功能，加速网络基础设施，释放CPU核来提高应用程序性能。</strong></p>
<p>尽管在概念上有些许区分，但无论是DPU还是IPU，都是想通过软件定义+硬件加速的方式，替代CPU成为数据中心的核心硬件。</p>
<p>由此也可以看出，阿里云此番推出的CIPU，更像是IPU和DPU的综合体，既能云化虚拟化管控数据中心，又能解决数据迁移带宽的问题。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220613/eefd69b8-aefe-4b3c-948a-4faa6c5bdf26.png" target="_blank"><img alt="淘汰CPU！阿里云首发CIPU处理器 为OS反向自研" h="193" src="https://img1.mydrivers.com/img/20220613/Seefd69b8-aefe-4b3c-948a-4faa6c5bdf26.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>而更大的区别在于，阿里云本身就是一家云厂商，还是有飞天云操作系统的那一种。</p>
<p>这就意味着，与英伟达、英特尔这样的硬件厂商不同，阿里云对于云计算技术发展各个阶段所面临的问题，有更为切身的体会。</p>
<p>前文提到，CIPU是一颗专门为飞天系统设计的处理器。也就是说，它从设计之初，就是贴合云计算行业痛点、结合飞天系统特点去做的。</p>
<p>这样的软硬一体化，一方面，既能通过硬件提供高性能，又能通过软件提供灵活性。</p>
<p>另一方面，从一开始就避免了适配性的问题，能通过1+1＞2的方式，做到更强的性能、更低的价格、更高的稳定性。</p>
<p><strong>自主研发的云计算</strong></p>
<p>如此看来，最先享受到这波技术发展红利的，就是云上用户们——</p>
<p>云计算能做到更高的性价比了。</p>
<p>而作为CIPU背后的云厂商，阿里云此番技术发布，也扣上了云计算技术国产化在新阶段的重要一环。</p>
<p>以阿里云自身为例：</p>
<p>2009年，阿里云自研云计算操作系统飞天诞生。双11、12306春运购票等大家津津乐道的极限并发场景，都跑在这个系统之上。</p>
<p>2017年，为了解决服务器虚拟化性能损耗的问题，阿里云自主研发了神龙架构（就是上文提到的神龙卡），通过把虚拟化转移到专用硬件中进行加速，实现了性能“0损耗”。</p>
<p>在云存储技术方面，阿里云自研的盘古分布式存储系统，推动了面向数据中心ZNSSSD国际标准的发展。与西部数据（WD）共同提出的NVMe2.0，是目前云计算业内最为先进的软硬一体深度融合的分布式存储系统。</p>
<p>去年，阿里云还发布了首款CPU倚天710，刷新了Arm服务器芯片性能纪录。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220613/d9af9457-0399-414e-99e6-d9f5b88e4213.png" target="_blank"><img alt="淘汰CPU！阿里云首发CIPU处理器 为OS反向自研" h="426" src="https://img1.mydrivers.com/img/20220613/Sd9af9457-0399-414e-99e6-d9f5b88e4213.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>……</p>
<p>从网络到存储，从软件到硬件，通过13年的技术积累、自主研发，阿里云作为国内云厂商的代表，正在世界云计算的舞台上发出越来越高的声量。</p>
<p>而CIPU的推出，则意味着这种在技术自主化方面的努力，或许已更进一步：</p>
<p>尝试打破海外云厂商、硬件厂商定义的传统发展路线，走出一条自己的新路。</p>
<p>每当技术发展到一个更新换代的新阶段，围绕话语权的竞争往往精彩不断，影响更甚于科技圈本身。</p>
<p>5G如是，云技术亦如是。</p>
<p>好戏或许才刚刚开场。</p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：上方文Q</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/aliyun.htm">阿里云</a><a href="https://news.mydrivers.com/tag/alibaba.htm">阿里巴巴</a><a href="https://news.mydrivers.com/tag/cpuchuliqi.htm">CPU处理器</a>  </p>
        
</div>
            