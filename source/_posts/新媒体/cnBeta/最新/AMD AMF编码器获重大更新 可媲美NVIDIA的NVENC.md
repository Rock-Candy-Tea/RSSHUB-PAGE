
---
title: 'AMD AMF编码器获重大更新 可媲美NVIDIA的NVENC'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0708/f48dff77e36857c.webp'
author: cnBeta
comments: false
date: Fri, 08 Jul 2022 07:54:35 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0708/f48dff77e36857c.webp'
---

<div>   
在经历了十年的质量问题之后，AMD AMF 编码器的图像质量得到了大幅提升。在最新的 AMF Release 1.4.24 中引入了 B-frames 技术。在油管频道 EposVox 的测试中发现 AMD Radeon 显卡现在可以像 NVIDIA 的产品一样使用较低比特率的流媒体游戏。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0708/f48dff77e36857c.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">AMD 的编码技术在过去很多年来备受诟病，最早可以追溯到 Polaris GPU（AMD 400 系列）。与<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>的 QuickSync 编码器和 NVIDIA 的 NVENC 编码器相比，这种编码从未完全达到标准。随后NVIDIA 推出了采用 x264 编码的 RTX 20 系列 GPU 的第六代 NVENC 编码器，暂时领先于 AMD。</p><p style="text-align: left;">而这个困扰 AMD 十年之久的问题似乎终于得到了解决。油管频道 EposVox 在最新一期视频中，展示了 AMD 在低比特率流媒体性能表现，尤其是该公司最近的 Radeon RX 6000 系列 GPU 中仍然存在的 H.264 编解码器。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0708/49dfc744b3795cb.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">那么，AMD 是如何解决这个问题的呢？该公司将 B-frames 技术重新引入到 AMF 解码器中。该技术自公司最初的编码和解码引擎 VCE 以来一直缺失。 AMD 在发布带有 Raven Ridge APU 和 RDNA 1 GPU 的 VCN 引擎后放弃了这项技术。</p><p style="text-align: left;">Tom's Hardware 表示：“B-frames 技术允许 H.264 压缩算法从视频流中的过去和未来帧预测图像数据。它是一项可选功能，已被证明可以显着提高较低比特率的流的图像质量”。</p><p style="text-align: left;">Code Calamity 使用 VMAF 测量 AMF、NVENC 和 Intel QuickSync 之间的图像质量差异，并以 Big Buck Bunny 作为参考视频。在这个基准测试中，最高可能得分为 100 分。作为参考，NVENC 得分 96.13 分，英特尔 QuickSync 在本次测试中得分 96.37。根据 Code Calamity 的说法，AMD 的 AMF 编码器仅落后这两个编码器半个百分点，而之前（没有 B-Frames）AMD 的 AMF 落后了整整两分。</p><p style="text-align: left;">基准测试显示，AMD AMF 的图像质量更接近于 NVIDIA 当前的 NVENC 编码器。但是它虽然已经上线几个月了，没有流媒体平台提供任何当前支持，即使它已经可用了几个月。据推测，AMD 在实现其编码器 SDK 方面的开发人员支持历史一直很麻烦，这可以解释为什么它没有被纳入。</p>   
</div>
            