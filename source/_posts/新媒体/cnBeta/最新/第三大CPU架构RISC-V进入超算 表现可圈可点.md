
---
title: '第三大CPU架构RISC-V进入超算 表现可圈可点'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0610/95a5e09e4969294.png'
author: cnBeta
comments: false
date: Fri, 10 Jun 2022 13:05:38 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0610/95a5e09e4969294.png'
---

<div>   
一个欧洲大学生团队组装出第一台能够平衡功耗和性能的 RISC-V 超级计算机。更重要的是，它展示了 RISC-V
在高性能计算方面的巨大潜力，为欧洲摆脱对美国芯片技术的依赖提供了机会。“Monte
Cimone”集群不会很快用于处理大规模的天气模拟等，因为它只是一台实验机器。<br>
 <p>这台设备由博洛尼亚大学和意大利最大的超级计算中心 CINECA 的人员构建，六节点集群设计，旨在展示除浮点能力之外的各种 HPC 性能元素。</p><p>它使用 SiFive 的 Freedom U740 片上系统RISC-V 的电源模块，这个2020 年推出的 SoC 有五个 64 位 RISC-V CPU 内核——四个 U7 应用程序内核和一个 S7 系统管理内核——2MB 二级缓存、千兆以太网以及各种外围设备和硬件控制器。</p><p>它可以运行在大约 1.4GHz频率，以下是 Monte Cimone 的组件以及速度：</p><p>六台双板服务器，外形尺寸为 4.44 厘米 (1U) 高、42.5 厘米宽、40 厘米深。每块板都遵循行业标准 Mini-ITX 外形尺寸（每 170 毫米 170 毫米）；</p><p>每块主板配备一个 SiFive Freedom U740 SoC 和 16GB 的 64 位 DDR 内存，运行速度为 1866s MT/s，以及一个运行速度为 7.8 GB/s 的 PCIe Gen 3 x8 总线、一个千兆以太网端口和 USB 3.2 Gen 1 接口；</p><p>每个节点都有一个 M.2 M-key 扩展槽，由操作系统使用的 1TB NVME 2280 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a> 占用。每块板上都插有一张 microSD 卡，用于 UEFI 启动；</p><p>每个节点内部集成了两个 250 W 电源，以支持硬件和未来的 PCIe 加速器和扩展板。</p><p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20220610/547ed6b7-de3f-4df7-8a6b-1426b25ce6ea.png" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0610/95a5e09e4969294.png"><img data-original="https://static.cnbetacdn.com/article/2022/0610/95a5e09e4969294.png" src="https://static.cnbetacdn.com/thumb/article/2022/0610/95a5e09e4969294.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">每个节点的俯视图，显示了两个 SiFive Freedom SoC 板</p><p>Freedom SoC 主板本质上是 SiFive 的 HiFive Unmatched 主板。正如大多数超级计算机使用的那样，六个计算节点中的两个配备了 Infiniband 主机通道适配器 (HCA)。目标是部署 56GB/s Infiniband 以允许 RDMA 实现 I/O 性能。</p><p>这对于一个年轻的架构来说是雄心勃勃的，而且并非没有一些小问题。</p><p>“供应商目前仅支持 PCIe Gen 3 通道，”集群团队写道。“第一个实验结果表明，内核能够识别设备驱动程序并挂载内核模块来管理 Mellanox OFED 堆栈。由于尚未确定软件堆栈和内核驱动程序的不兼容性，我们无法使用 HCA 的所有 RDMA 功能。</p><p>尽管如此，我们还是成功地在两个板之间以及一个板和一个 HPC 服务器之间运行了 IB ping 测试，表明完全支持 Infiniband 是可行的。</p><p>”事实证明，HPC 软件堆栈比人们想象的要容易。“我们在 Monte Cimone 上移植了在生产环境中运行 HPC 工作负载所需的所有基本服务，即 NFS、LDAP 和 SLURM 作业调度程序。将所有必要的软件包移植到 RISC-V 相对简单。</p><p>该集群最终将成为这将为进一步测试 RISC-V 平台本身及其与其他架构良好配合的能力铺平道路，这是一个重要元素因为至少在未来几年内我们不太可能看到百亿亿级的 RISC-V 系统。</p><p>现在，就连<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>也在关注RISC-V的未来。</p>   
</div>
            