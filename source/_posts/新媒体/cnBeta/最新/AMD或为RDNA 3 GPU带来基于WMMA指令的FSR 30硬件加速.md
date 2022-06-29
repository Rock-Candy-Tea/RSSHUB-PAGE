
---
title: 'AMD或为RDNA 3 GPU带来基于WMMA指令的FSR 3.0硬件加速'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0629/158b7061fcce86d.jpg'
author: cnBeta
comments: false
date: Wed, 29 Jun 2022 07:24:12 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0629/158b7061fcce86d.jpg'
---

<div>   
与采用机器学习（ML）硬件的英伟达 DLSS 方案相比，AMD 的 FSR 1.0 和 FSR 2.0 开源技术无需任何硬件辅助。然而近日有爆料称 —— <strong>得益于“Wave Matrix-Multiply-Accumulate”指令，AMD RDNA 3“GFX11”GPU 或升级基于硬件加速的 FSR 3.0 技术。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0629/158b7061fcce86d.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0629/158b7061fcce86d.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p>AMD 在 FSR 方面的工作很是出色，不仅提供了媲美 NVIDIA 的视觉质量，还做到了更加开源。但若红队决定在 FSR 3.0 中引入硬件加速，我们也有望迎来更高的性能和视觉质量。</p><p><img src="https://static.cnbetacdn.com/article/2022/0629/726fd2cadc456a6.png" alt="0-1.png" referrerpolicy="no-referrer"></p><p>@0x22h 在 Twitter 上指出，其在 LLVM 存储库中发现了一项新的提交，可知 AMD 为“GFX11”GPU 硬件引入了“波矩阵多累加”（简称 WMMA）指令。</p><p><img src="https://static.cnbetacdn.com/article/2022/0629/09bca8d4dc04664.jpg" alt="0-2.jpg" referrerpolicy="no-referrer"></p><p>GFX11 属于 RNDA 3 GPU 系列的代号，并且分为面向消费市场的 Radeon RX 7000 游戏显卡、以及面向工作站的 Radeon Pro 专业显卡。</p><p><a href="https://static.cnbetacdn.com/article/2022/0629/68efda65e1670f4.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0629/68efda65e1670f4.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>与英伟达 Tensor Core 所使用的矩阵乘法 / 深度学习操作类似，AMD WMMA 指令也在硬件层面加以融合，以帮助实现更好的机器学习 / DNN 操作。</p><p>虽然尚未披露更多细节，但 LLVM 最近更新可能暗示了 RDNA 3 GPU 将迎来主要图形管道的重大改进。</p><p><a href="https://static.cnbetacdn.com/article/2022/0629/6f77edd1295fc95.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0629/6f77edd1295fc95.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p><a href="https://wccftech.com/amd-fsr-3-0-gfx11-rdna-3-gpus-hardware-acceleration-wmma-instructions/" target="_self">WCCFTech</a> 指出：过去一年时间里，FSR 采用率已是其竞争对手的 2 倍。其中有 113+ 款游戏在一年内添加了对 FiedlityFX Super Resolution 的支持，另有 180+ 游戏在 3.4 年内获得了支持。</p><p>此外通过向 PC 和<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a> <a data-link="1" href="https://microsoft.pvxt.net/e4yLO" target="_blank">Xbox</a> 主机开放 FSR，这项开源技术的未来前景正变得愈加光明。不过在 RTX 40 系列 Ada Lovelace GPU 上市后，DLSS 3.0 也势必与 FSR 3.0 展开更激烈的竞争。</p>   
</div>
            