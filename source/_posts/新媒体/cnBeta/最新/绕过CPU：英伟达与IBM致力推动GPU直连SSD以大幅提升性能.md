
---
title: '绕过CPU：英伟达与IBM致力推动GPU直连SSD以大幅提升性能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0317/fe9a33dc411292c.jpg'
author: cnBeta
comments: false
date: Thu, 17 Mar 2022 08:29:34 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0317/fe9a33dc411292c.jpg'
---

<div>   
<strong>通过与几所大学的合作，英伟达和 IBM 打造了一套新架构，致力于为 GPU 加速应用程序，提供对大量数据存储的快速“细粒度访问”。</strong>所谓的“大加速器内存”（Big Accelerator Memory）旨在扩展 GPU 显存容量、有效提升存储访问带宽，同时为 GPU 线程提供高级抽象层，以便轻松按需、细粒度地访问扩展内存层次中的海量数据结构。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0317/fe9a33dc411292c.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">以 CPU 为中心的传统模型示例</p><p>显然，这项技术将使人工智能、分析和机器学习训练等领域更加受益。而作为 BaM 团队中的重量级选手，英伟达将为创新项目倾注自身的广泛资源。</p><p>比如允许 NVIDIA GPU 直接获取数据，而无需依赖于 CPU 来执行虚拟地址转换、基于页面的按需数据加载、以及其它针对内存和外存的大量数据管理工作。</p><p>对于普通用户来说，我们只需看到 BaM 的两大优势。其一是基于软件管理的 GPU 缓存，数据存储和显卡之间的信息传输分配工作，都将交给 GPU 核心上的线程来管理。</p><p>通过使用 RDMA、PCI Express 接口、以及自定义的 Linux 内核驱动程序，BaM 可允许 GPU 直接打通 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a> 数据读写。</p><p><img src="https://static.cnbetacdn.com/article/2022/0317/2b0362a67aa16d1.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">BaM 模型示例</p><p>其次，通过打通 NVMe SSD 的数据通信请求，BaM 只会在特定数据不在软件管理的缓存区域时，才让 GPU 线程做好参考执行驱动程序命令的准备。</p><p>基于此，在图形处理器上运行繁重工作负载的算法，将能够通过针对特定数据的访问例程优化，从而实现针对重要信息的高效访问。</p><p>显然，以 CPU 为中心的策略，会导致过多的 CPU-GPU 同步开销（以及 I/O 流量放大），从而拖累了具有细粒度的数据相关访问模式 —— 比如图形与数据分析、推荐系统和图形神经网络等新兴应用程序的存储网络带宽效率。</p><p>为此，研究人员在 BaM 模型的 GPU 内存中，提供了一个基于高并发 NVMe 的提交 / 完成队列的用户级库，使得未从软件缓存中丢失的 GPU 线程，能够以高吞吐量的方式来高效访问存储。</p><p><img src="https://static.cnbetacdn.com/article/2022/0317/d156509c00d5b4f.jpg" alt="3.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">BaM 设计的逻辑视图</p><p>更棒的是，该方案在每次存储访问时的软件开销都极低，并且支持高度并发的线程。而在基于 BaM 设计 + 标准 GPU + NVMe SSD 的 Linux 原型测试平台上开展的相关实验，也交出了相当喜人的成绩。</p><p>作为当前基于 CPU 统管一切事务的传统解决方案的一个可行替代，研究表明存储访问可同时工作、消除了同步限制，并且 I/O 带宽效率的显著提升，也让应用程序的性能不可同日而语。</p><p>此外 NVIDIA 首席科学家、曾带领斯坦福大学计算机科学系的 Bill Dally 指出：得益于软件缓存，BaM 不依赖于虚拟内存地址转换，因而天生就免疫于 TLB 未命中等序列化事件。</p><p>最后，三方将开源 BaM 设计的新细节，以期更多企业能够投入到软硬件的优化、并自行创建类似的设计。有趣的是，将闪存放在 GPU 一旁的 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Radeon 固态显卡，也运用了类似的功能设计理念。</p>   
</div>
            