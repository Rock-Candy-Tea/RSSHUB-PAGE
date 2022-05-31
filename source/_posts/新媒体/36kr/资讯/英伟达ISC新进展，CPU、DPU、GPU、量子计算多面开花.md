
---
title: '英伟达ISC新进展，CPU、DPU、GPU、量子计算多面开花'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9629'
author: 36kr
comments: false
date: Tue, 31 May 2022 03:08:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=9629'
---

<div>   
<p>在刚刚过去的ISC 2022（国际超级计算机大会）大会上，分别介绍了公司在CPU、DPU、GPU产品上的进展，及量子计算方面的努力。</p> 
<p>在CPU产品上，英伟达介绍了其NVIDIA HGXTM平台中的Gr<a class="project-link" data-id="1744024544877447" data-name="ace" data-logo="https://img.36krcdn.com/20220517/v2_7f3368f3935c45cfae94727c1a418ebd_img_000" data-refer-type="1" href="https://36kr.com/project/1744024544877447" target="_blank">ace</a>和Grace Hopper的发展情况，公布相关设计，制造商可以根据这些设计所提供的蓝图，构建出最高性能，且内存带宽和能效两倍于当今领先的数据中心CPU的系统。</p> 
<p>其Grace CPU超级芯片是将两块Grace CPU裸片通过NVIDIA NVLink®-C2C互连技术连接，提供144个高性能CPU核心和 1 TB/s的内存带宽，能支持PCIe Gen5协议、ConnectX<a target="_blank" rel="noopener noreferrer nofollow" href="https://www.nvidia.com/en-us/networking/infiniband-adapters/">®</a>-7智能网卡和BlueField<a target="_blank" rel="noopener noreferrer nofollow" href="https://www.bing.com/search?q=nvidia+bluefield+3&cvid=bcf22594ee2f4e848ad40d1e538372fc&aqs=edge.5.0j69i57j0l7.3667j0j4&FORM=ANAB01&PC=ACTS">®-3</a> DPU，保障HPC及AI工作的负载安全。</p> 
<p>Grace Hopper超级芯片则是将其中一个CPU芯片替换成H100 GPU芯片，并通过NVLink-C2C技术连接，满足满足HPC和超大规模AI应用需求。</p> 
<p>英伟达超大规模和HPC副总裁Ian Buck表示，超级计算已进入到超大规模AI时代。英伟达正与OEM合作伙伴一道助力研究者攻克此前无法解决的巨大挑战。为气候科学、能源研究、太空探索、数字生物学到量子计算等领域，提供运算平台基础。</p> 
<p>在会上，英伟达宣布，源讯、戴尔科技，技嘉科技、慧与、浪潮、联想和超微等多家计算机制造商正在采用全新NVIDIA Grace™超级芯片打造新一代服务器，为超大规模时代的AI和HPC工作负载提速。</p> 
<p>此外，洛斯阿拉莫斯国家实验室（LANL）和瑞士国家计算中心的新系统Alps都将采用NVIDIA Grace CPU技术。</p> 
<p><strong>在DPU这个英伟达引领的产品上，较多合作伙伴正在探索DPU产品的作用。</strong></p> 
<p>洛斯阿拉莫斯国家实验室（LANL）的杰出高级科学家Steve Poole正与 NVIDIA 进行一项为期多年的广泛合作，希望将计算多物理应用的性能提高 30 倍。基于DPU 赋能存储系统，加速闪存盒（ABoF，如下图所示）将固态存储与 DPU 和 InfiniBand 加速器相结合，可为 Linux 文件系统的关键性能部分提供加速。它的性能高达同类存储系统的 30 倍，并将成为 LANL 基础架构中的关键组件</p> 
<p>德克萨斯高级计算中心（TACC）近期也开始在 Dell PowerEdge 服务器中采用 BlueField-2。它将在 InfiniBand 网络上使用 DPU ，使其 Lonestar6 系统成为云原生超级计算的开发平台。</p> 
<p>俄亥俄州立大学的研究人员，还展示了 DPU 如何将一个 HPC 热门编程模型的运行速度提高 21%。他们通过卸载消息传递接口（MPI）的关键部分，加速了 P3DFFT ，这是一个用于众多大规模 HPC 仿真的数学库。</p> 
<p>除CPU+GPU的联合产品以外，<strong>在ISC上，英伟达还公布了公司在量子计算方面的进展。</strong></p> 
<p>NVIDIA 在2021 GTC上宣布了cuQuantum软件开发套件，到此时，已有数十家量子组织开始使用 NVIDIA cuQuantum 软件开发套件，在 GPU 上加速其量子电路模拟。</p> 
<p>其cuQuantum 可以运用于主要量子软件框架，如Google 的 qsim、IBM 的 Qiskit Aer、Xanadu 的 PennyLane 和 Classiq 的Quantum Algorithm Design 平台，实现用户直接访问GPU 加速，无需进行编码。</p> 
<p>而英伟达到下一步计划是，向混合系统发展，实现量子计算机和经典计算机协同工作，使系统级量子处理器（即 QPU）成为功能强大的新型加速器。</p> 
<p>英伟达希望在GPU 和 QPU之间建立快速、低延迟的连接，由GPU 负责电路优化、校正和纠错一类传统工作，以缩短GPU执行时间。目前，降低经典计算机和量子计算机之间的通信延迟，仍是混合量子作业面临的主要瓶颈。</p>  
</div>
            