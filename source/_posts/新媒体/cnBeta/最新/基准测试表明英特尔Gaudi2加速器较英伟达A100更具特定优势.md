
---
title: '基准测试表明英特尔Gaudi2加速器较英伟达A100更具特定优势'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0628/d9e71c3b000c8c3.jpg'
author: cnBeta
comments: false
date: Tue, 05 Jul 2022 00:37:27 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0628/d9e71c3b000c8c3.jpg'
---

<div>   
<strong>在 2019 年以 20 亿美元收购了以色列 Habana Labs 后，英特尔推出了 Gaudi2 数据中心加速卡，并将之与面世已有两年的英伟达 A100 进行了对比。</strong>事实上，Habana 制造了两种专用加速器 —— 除了面向神经网络训练的 Gaudi2，还有主打推理任务的 Goya / Greco 。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0628/d9e71c3b000c8c3.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>虽然早在 5 月就发布，但 MLPerf 公共数据库直到上周才接收到它的基准测试成绩。</p><p>由其分享的图表可知，Gaudi2 系统的分数，被拿来和英伟达 / <a data-link="1" href="http://www.anrdoezrs.net/links/9019719/type/dlg/sid//https://www.dell.com/zh-cn/shop/deals" target="_blank">戴尔</a>的 A100 系统进行了横向比较。</p><p><img src="https://static.cnbetacdn.com/article/2022/0705/ec879b7c3acfb31.webp" alt="1.webp" referrerpolicy="no-referrer"></p><p>首先，ResNet-50 能够测试硬件在 AI 图像分类工作上的表现。可知 Habana 的 Gaudi2 系统只需 18 分钟就通过测试，而英伟达 A100 系统需要将近半个小时。</p><p>其次，Gaudi2 只用了 17 分钟来训练 BERT 模型，较 A100 系统快了大约一分钟。作为一个自然语言处理（NLP）模型，这项测试使用了来自维基百科的文章来训练。</p><p><img src="https://static.cnbetacdn.com/article/2022/0705/9f2bd995850c7bd.webp" alt="2.webp" referrerpolicy="no-referrer"></p><p>虽然所有测试平台都使用了八卡加速器 / GPU，但 Habana 系统搭配了双路 40 核的 Intel Xeon 8380 CPU，而英伟达系统则采用了双路 64 核的 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> EPYC 7742 CPU 。</p><p>规格方面，Gaudi2 具有 24 个张量处理（TPC）内核 + 并行运行的两部分矩阵乘法（MME）引擎。其支持包括 FP32、TF32、BF16、FP16 和 FP8 在内的广泛数据类型。</p><p><img src="https://static.cnbetacdn.com/article/2022/0628/895862e6130dd16.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>此外 Gaudi2 有一个专用于处理音视频输入的媒体引擎，集成 48MB 内部缓存 + 板载 96GB（6×16GB）HBM2e 高带宽内存，总带宽达到了 2.45 TB/s 。</p><p>连接方面，该加速器使用了 PCIe 4.0 x16 接口、辅以 24 个 100 Mbps RoCE2（RDMA over Converged Ethernet 2）端口。</p><p><img src="https://static.cnbetacdn.com/article/2022/0628/48830e3f6f4994a.jpg" alt="3.jpg" referrerpolicy="no-referrer"></p><p>需要指出的是，英伟达 A100 / H100 的功能要更加全面一些，Gaudi2 在某些特定任务上更具优势。</p><p>不过就算英伟达早在三个月前就发布了 H100 新品，Gaudi2 还是有望成为 A100 的一个有力竞争对手。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1286019.htm" target="_blank">英特尔开始推出Habana Labs Gaudi2 Linux驱动程序代码</a></p></div>   
</div>
            