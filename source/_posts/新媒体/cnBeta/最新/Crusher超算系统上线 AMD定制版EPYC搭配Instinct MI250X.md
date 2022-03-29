
---
title: 'Crusher超算系统上线 AMD定制版EPYC搭配Instinct MI250X'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0329/fc20510ea93778d.jpg'
author: cnBeta
comments: false
date: Tue, 29 Mar 2022 05:43:14 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0329/fc20510ea93778d.jpg'
---

<div>   
美国能源部（DOE）橡树岭国家实验室（ORNL）正打造一台ExaFLOP级的超级计算机Frontier，这是价值6亿美元的项目。在Frontier正式运行之前，将由Crusher暂时代替，作为测试平台。<strong>据TomsHardware</strong><a href="https://www.tomshardware.com/news/from-opteron-to-milan-crusher-supercomputer-comes-online-with-amd-cpus-and-gpus" target="_blank"><strong>报道</strong></a><strong>，近日Crusher超级计算机已上线。</strong><br>
 <p style="text-align:center"><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0329/fc20510ea93778d.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0329/fc20510ea93778d.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0329/fc20510ea93778d.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">Crusher与Frontier采用了相同的架构和组件，每个HPE Cray EX节点包括了一个<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>的64核EPYC“Trento”7A53处理器，512GB的DDR4内存，以及四块Instinct MI250X计算卡。Crusher共有192个节点，分别装入到两个机柜中，其中一个有128个节点，另外一个有64个节点，不过总的占用空间仅为以往Cray XK7 Titan超级计算机的十分之一，但提供了更高的运算性能。Cray XK7 Titan曾是世界上最快的超级计算机之一，搭载了AMD Opteron处理器和英伟达Tesla计算卡，在2012年到2019年之间为数百项科学研究服务。</p><p style="text-align: left;">Crusher和Frontier搭载的EPYC“Trento”7A53处理器是一款定制芯片，AMD没有透露太多的细节，只知道是代号Milan的Zen 3架构的衍生产品，传闻其I/O 芯片采用了Infinity Fabric 3.0来实现与GPU一致的内存接口。每块EPYC“Trento”7A53处理器会被划分为四个NUMA区域，每个NUMA区域与一块Instinct MI250X计算卡（每块两个GCD）相连。</p><p style="text-align: left;">CPU到GPU之间通过Infinity Fabric以36+36GB/s的接口带宽连接，CPU到GPU之间288GB/s的总带宽分布在节点中的八个GCD里。Crusher的每个节点通过四个HPE Slingshot 200GBps以太网NIC（25GB/s）连接，提供800Gbps（100 GB/s）的节点带宽。</p><p style="text-align: left;">Frontier超算系统在2021年已经交付，不过仍在进行集成和测试，具体运行的时间表仍未确定。Frontier超算系统是美国第一台ExaFLOP级的超级计算机，美国能源部预计会在2023年1月向研究人员开放。</p>   
</div>
            