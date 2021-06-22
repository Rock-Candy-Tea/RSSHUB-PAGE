
---
title: '英伟达：DPU 将让数据中心成为新计算单元'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/6/b9b40118-482b-4a67-aaee-d2adaf4b95eb.png'
author: IT 之家
comments: false
date: Tue, 22 Jun 2021 06:47:53 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/6/b9b40118-482b-4a67-aaee-d2adaf4b95eb.png'
---

<div>   
<p>6 月 22 日消息 去年的 GTC 2020 大会上，英伟达（NVIDIA）发布了一款全新的处理器 DPU（Data Processing Unit，数据处理单元），由新型的 DOCA（Data-Center-Infrastructure-On-A-Chip Architecture）软件架构提供支持。</p><p>据媒体报道，近 1 年来，DPU 成为业界追逐的话题，Marvell、Broadcom、VMware 等众多制造商已加入这一细分赛道。今年 4 月，英伟达发布了新一代 BlueField-3 DPU，以及 DOCA SDK 1.0。</p><p>在日前举办的媒体沟通会上，英伟达网络事业部亚太区市场开发高级总监宋庆春对媒体介绍，随着数据量越来越大，很多通信模型会制约系统性能，传统的冯・诺依曼架构无法解决由通信模型带来的网络拥塞问题，继续提升数据中心性能成为业界共同面对的挑战。</p><p>以数据为中心的新架构，可以解决这个问题。宋庆春介绍，这一架构意味着数据在哪里，计算就在那里。当数据在 GPU 上，计算就在 GPU 上；当数据在 CPU 上，计算就在 CPU 上；当数据在网络中传输的时候，计算就在网络中。“新架构可以解决网络传输中多打一通信造成的的性能瓶颈问题或丢包问题，可以使通信延时降低 10 倍以上。”</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/6/b9b40118-482b-4a67-aaee-d2adaf4b95eb.png" w="1116" h="667" title="英伟达：DPU 将让数据中心成为新计算单元" width="1116" height="490" referrerpolicy="no-referrer"></p><p>而 DPU 的出现，为以数据为中心的计算架构提供了创新思路。宋庆春介绍，之前在以 CPU 为主体的系统里，所有的操作都用 CPU 来做。以 OVS 操作为例，跑在 CPU 上，会消耗很多 CPU 的核，但运行 OVS 的效率非常低。如果将 OVS 放到 DPU 上运行，则可以实现 OVS 和 CPU 业务之间的隔离，降低 OVS 对于业务性能的影响。</p><p>目前英伟达已经推出了 BlueField-2 DPU，GTC 2021 上推出的新一代 BlueField-3 DPU，相比上代产品计算能力提升 5 倍、加密处理能力提升 4 倍、存储性能也提升了 3~4 倍，整体性能得到全面提升。据悉，BlueField-3 预计在明年上半年推向市场。</p><p>宋庆春指出，随着 DPU 的崛起，数据中心成为新的计算单元。这一定会掀起一波数据中心的变革，不管是从单芯片、还是大规模的超级计算机，都可以采用统一的架构，在单芯片上可以有计算、有存储、有通信，一个数据中心所需的各个单元都有了。而大规模数据中心也是一样的架构，有计算、存储、通信等各单元，实现了统一架构的计算单元。“到了 BlueField-4 以后，我们将 GPU 集成到 DPU，DPU 就会成为一个完整的芯片级数据中心。”</p><p>在本次媒体沟通会上，国内知名云服务商，UCloud 资深技术专家马彦青表示，选择 DPU，是因为遇到了网络的性能瓶颈，同时期望降低成本。英伟达的 DPU 可以实现 ASAP2 网络卸载、SNAP/Virtio 存储卸载、ARM 处理器编排管理、DPI 深度包检测与加密、IB/RDMA 加速数据传输等功能，同时提升网关带宽和数据安全的优势，受到 UCloud 的欢迎。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/6/9f100ec4-1625-47d2-8a70-8a7cb5f13f33.png" w="1083" h="523" title="英伟达：DPU 将让数据中心成为新计算单元" width="1083" height="396" referrerpolicy="no-referrer"></p><p>例如在存储方面，UCloud 过去采取传统方式，即使用本地盘来做存储，一旦出现数据丢失的状况，想恢复是一件非常困难的事情。利用 DPU 和 DOCA 重构 UCloud 的裸金属存储架构，系统盘和数据盘都采用 RSSD 云盘，实现了计算和存储的解耦，这带来的好处，一是用户可以免装机，分钟级交付；二是不需要定制机型，减少资源浪费；三是发生故障时因为采用了云盘，可以快速迁移，且数据端是三副本，保证数据的安全。</p><p>此外，DPU 对于 UCloud 的意义，还在于实现了一张卡来实现虚拟化和裸金属架构的统一在，这使得 UCloud 可以共用存储设备、网络设备、软件栈，甚至物理网络也可以做到统一。“这是 UCloud 三年前设计裸金属架构时制定的目标。”马彦青说表示。</p><p>宋庆春强调，DPU 生态系统已经得到操作系统、安全、存储、应用等产业链厂商的广泛支持。英伟达与 UCloud 在两年前开始合作时，那时还没有 DOCA，也没有系统的 DPU API 软件支持，但基于双方的共识，UCloud 开发团队付出了大量努力，在他们的云上实现了软件定义和硬件加速的高度协作，实践了 DPU 提升系统性能和安全的能力。“随着 DOCA 的逐步成熟，双方合作也会迈向新台阶。”</p>
          
</div>
            