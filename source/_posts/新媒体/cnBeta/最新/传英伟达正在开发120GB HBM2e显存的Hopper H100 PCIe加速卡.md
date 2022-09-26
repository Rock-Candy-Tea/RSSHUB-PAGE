
---
title: '传英伟达正在开发120GB HBM2e显存的Hopper H100 PCIe加速卡'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0926/9c107b3596f98d3.jpg'
author: cnBeta
comments: false
date: Mon, 26 Sep 2022 08:09:37 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0926/9c107b3596f98d3.jpg'
---

<div>   
近日有消息称，英伟达正在开发一款 Hopper H100 PCIe 加速卡，特点是具有高达 120GB 的 HBM2e 显存。<strong>截至目前，该公司已经发布了两个版本的 Hopper H100 GPU，分别是 SXM5 和 PCIe 板型。</strong>虽然两款 SKU 都配备了 80GB VRAM，但前者用上了全新的 HBM3 标准、而后者仍为 HBM2e 。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0926/9c107b3596f98d3.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0926/9c107b3596f98d3.jpg" referrerpolicy="no-referrer"></a></p><p>最新消息是，据 s-ss.cc 爆料，英伟达可能正在开发全新的 PCIe 扩展卡版本的 Hopper H100 GPU —— 但它并未配备 80GB HBM2e VRAM、而是增加到了 120GB 。</p><blockquote><p>消息称这张新卡配备了六个 HBM2e 堆栈、拥有 6144-bit 总线位宽 @ 120GB VRAM、辅以 SXM5 同款 GH100 GPU 。</p><p>总计 16896 个 CUDA 核心、带宽超 3 TB/s、单精度性能 30 TFLOPS —— 与 SXM5 版本相当。</p></blockquote><p>照此规格，英伟达 Hopper GH100 GPU 拥有 144 组 SM 流处理器 / 8 个 GPC —— 每组 GPC 包含 9 个 TPC，每 TPC 由 2 组 SM 单元组成。</p><p>每组 SM 单元最多由 128 个 FP32 单元，那样满血版应该是 18432 个 CUDA 核心。</p><p><a href="https://static.cnbetacdn.com/article/2022/0926/a131bd4943cc1d1.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0926/a131bd4943cc1d1.jpg" referrerpolicy="no-referrer"></a></p><p>GH100 GPU 完整规格参考：</p><blockquote><p>● 每颗 GPU 拥有 8 GPC、72 TPCs（9 TPC / GPC）、2 SM / TPC、144 SM 单元</p><p>● 每组 SM 单元拥有 128 个 FP32 CUDA 核心，每颗 GPU 拥有 18432 个 FP32 CUDA 核心。</p><p>● 每组 SM 单元拥有 4 个第四代张量核心，每颗 GPU 拥有完整 576 个 Tensor Cores 。</p><p>● 6 组 HBM3 或 HBM2e 显存堆栈，辅以 12 个 @ 512-bit 显存控制器。</p><p>● 配备 60 MB 二级缓存</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0926/4b3fefce4d6207d.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0926/4b3fefce4d6207d.png" alt="NVIDIA-Hopper-H100-GPU.png" referrerpolicy="no-referrer"></a></p><p>以下是 SXM5 外形的 NVIDIA H100 GPU 规格：</p><blockquote><p>● 每颗 GPU 拥有 8 GPC / 66 TPC、2  SM / TPC、132 SM 单元</p><p>● 每组 SM 单元拥有 128 个 FP32 CUDA 核心，每颗 GPU 拥有 16896 个 FP32 CUDA 核心。</p><p>● 每组 SM 单元拥有 4 个第四代张量核心，每颗 GPU 拥有 528 个 Tensor Cores 。</p><p>● 5 组 @ 80GB HBM3 显存堆栈，辅以 10 个 @ 512-bit 显存控制器。</p><p>● 配备 50MB 二级缓存</p><p>● 支持第四代 NVLink 和 PCIe 5.0</p></blockquote><p>目前尚不清楚英伟达正在搞测试原型，还是酝酿推出 Hopper H100 GPU 的未来迭代。</p><p>不过该公司最近在 GTC 2022 大会上表示，Hopper GPU 现已全面投产，预计首批产品会在下月到来。</p>   
</div>
            