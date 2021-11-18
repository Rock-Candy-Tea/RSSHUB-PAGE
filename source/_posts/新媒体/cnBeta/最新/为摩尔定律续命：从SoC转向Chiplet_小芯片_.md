
---
title: '为摩尔定律续命：从SoC转向Chiplet_小芯片_'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1118/12edbd553cdd509.jpg'
author: cnBeta
comments: false
date: Thu, 18 Nov 2021 06:08:42 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1118/12edbd553cdd509.jpg'
---

<div>   
以英特尔前CEO戈登摩尔命名的摩尔定律，是指集成电路中的晶体管数量每两年翻一番。55年来，半导体行业一直用摩尔定律来制定路线图和研发目标。为延续摩尔定律、实现芯片小型化，55年间新技术不断涌现。<br>
 <p>但从历史上看，晶圆的光掩模限制了单个芯片的最大尺寸，芯片制造商和设计人员不得不用多个芯片来完成提供的功能。很多情况下，甚至是多个芯片提供相同的功能，就像是处理器的内核和内存模块那样。</p><p>之前一直在用的SoC（片上系统）技术可以组合不同的模块，模块之间通信速度更快的同时，功耗更低、密度更高，而且成本更低。但近年来，先进制造节点的成本增加，削弱了SoC技术在成本上的优势。</p><p>在最新的台积电2021开放创新平台活动上，Alchip Technologies研发副总裁James Huang表示Chiplet“小芯片”和先进的封装技术，可以提供比单个SoC更有竞争力的成本结构，同时保持接近的性能和功耗。</p><p>其引用了两项对小芯片/封装发展至关重要的技术：一项是台积电的 3DFabric 和CoWos组合技术，另一项是Alchip的APLink die-to-die (D2D) I/0技术。</p><p>Chiplet“小芯片”技术，顾名思义，就是用多个小芯片封装在一起，用die-to-die内部互联技术，组成异构System in Packages（ SiPs）芯片。而更小的芯片单体，可以提高每片晶圆的利用率，从而降低成本。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1118/12edbd553cdd509.jpg" referrerpolicy="no-referrer"></p><p>但为了维持摩尔定律，Chiplet“小芯片”技术还需要提供与SoC技术接近的性能，需要AIchip的APLink D2D I/0技术支撑多个小芯片之间的高速数据流。</p><p>APlink 1.0使用的是台积电的12nm工艺，速度是1Gbps；APlink 2.0用的是7nm工艺，速度是4Gbps；正在测试的APLink 3.0已经有16Gbps的速度。</p><p>根据路线图，即将推出的APLink 4.0会采用 3nm D2D工艺。APlink 4.0 IP 将支持北/南、东/西方向和对称式PHY对齐，以尽量减少D2D线长，其互连拓扑的I/O总线会用标准的内核电压，PHY宏的速度将达到12Tbps，每条DQ的速度达到16Gbps，且只有5纳秒延迟 。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1118/eccdbdd0c03f216.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">图源EETimes</p><p>Chiplet“小芯片”技术涉及封装、EDA、芯片架构设计等多个领域，也有机会重构半导体产业链。但最后落地的关键是商业模式，Chiplet“小芯片”还需要点时间来证明自己。</p><br>   
</div>
            