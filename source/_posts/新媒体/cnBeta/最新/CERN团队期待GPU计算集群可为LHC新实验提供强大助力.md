
---
title: 'CERN团队期待GPU计算集群可为LHC新实验提供强大助力'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0208/6c8f718336a4a97.jpg'
author: cnBeta
comments: false
date: Tue, 08 Feb 2022 12:54:10 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0208/6c8f718336a4a97.jpg'
---

<div>   
对于传统计算机架构来说，想要每秒分析多达 10 亿次质子碰撞、或数万次极其复杂的铅碰撞，显然并非易事。随着大型强子对撞机（LHC）Run 3 数据处理需求的飙升，<strong>欧洲核子研究中心（CERN）也正通过四个大型实验项目，来探索通过 GPU 改善其计算基础设施的方法。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0208/6c8f718336a4a97.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0208/6c8f718336a4a97.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图自：CERN）</p><p><strong>据悉，LHC 实验的最新升级，即将于 2023 年投入使用。</strong></p><blockquote><p>考虑到传统中央处理器（CPU）难以应付新的计算挑战，目前正有四个大型项目在尝试采用 GPU 并行计算方案。</p><p>图上图所示，某 Run 3 候选 HLT 节点装配了双路 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Milan 64 核 CPU + 两张英伟达 Tesla T4 GPU 。</p></blockquote><p>GPU 在图像处理等应用场景下具有极高的效率，最初只是为了加速计算机 3D 图形渲染而打造。</p><blockquote><p>但在过去的几年里，LHC 实验、全球 LHC 计算网格（WLCG）和 CERN openlab 就已展开过这方面的研究尝试。</p><p>而在高能物理应用中加大 GPU 的计算投入，不仅能够提升 CERN 计算基础设施的质量和规模，还有助于提升系统的整体能效。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0208/bb97a3dd318b9ad.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0208/bb97a3dd318b9ad.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">铅-铅碰撞的 2 ms 可视化呈现（图自：ALICE TPC / CERN）</p><p><strong>CERN IT 部门负责人 Enrica Porcari 表示：</strong></p><blockquote><p>LHC 雄心勃勃的升级计划，带来了一系列令人兴奋的计算挑战。好消息是，GPU 能够在机器学习（DL）方面提供有力的支撑，帮助研究人员解决许多问题。</p><p>自 2020 年以来，CERN IT 部门提供了对数据中心 GPU 平台的访问权限，其已被证明在一系列应用中很受欢迎。</p><p>更重要的是，CERN openlab 正通过与工业界的合作研发项目，对将 GPU 用于机器学习一事展开郑重深入的调查。</p><p>与此同时，CERN 的科学计算协作小组，目前正努力帮助移植和优化实验中的关键代码。</p></blockquote><p>多年前，ALICE 项目就率先在其“高级触发在线计算机农场”（HLT）中使用了 GPU，但也是迄今唯一大规模运用 GPU 的实验。</p><blockquote><p>而新升级的 ALICE 探测器拥有超过 120 亿个连续读取的电子传感器元件，每秒可生成超过 3.5 TB 的数据流。即使经过一级数据处理，数据流量仍高达 600 GB/s 。</p><p>这些数据会被放到具有 250 个节点的 HPC 农场展开在线分析，每个节点包含 8 路 GPU + 32 核 CPU 。</p><p>大多数情况下，可将单个粒子检测器信号组装成粒子轨迹的软件（事件重建）工作，现均已适应了在 GPU 上并行工作。</p></blockquote><p>从 2022 年开始，LHCb 实验将处理 4 TB/s 的数据流，并对每秒筛选出的最有趣的 10 GB/s LHC 碰撞数据展开物理分析。</p><p>其独特方法是不卸载工作，而是分析 GPU 上每秒 3000 万个粒子束交叉点。自 2018 年以来，随着 CPU 处理的改进，LHCb 的探测器重建能效也提升了将近 20 倍。</p><p>目前研究人员正期待着使用 2022 年的首批新系统调试数据，并在此基础上让升级后的 LHCb 探测器得以发挥其完整的物理潜力。</p>   
</div>
            