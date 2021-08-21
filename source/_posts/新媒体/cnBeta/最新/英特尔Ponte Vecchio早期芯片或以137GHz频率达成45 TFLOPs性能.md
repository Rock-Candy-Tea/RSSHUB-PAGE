
---
title: '英特尔Ponte Vecchio早期芯片或以1.37GHz频率达成45 TFLOPs性能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0821/98f50295ad2f1ce.jpg'
author: cnBeta
comments: false
date: Sat, 21 Aug 2021 04:24:43 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0821/98f50295ad2f1ce.jpg'
---

<div>   
<strong>2021 架构日活动期间，英特尔披露了 Xe HPC“Ponte Vecchio”加速卡的诸多技术细节，并且分享了基于 A0 原型的一些初步性能数据。</strong>通过简单的数学计算，TechPowerUp 推测原型卡的运行频率在 1.37GHz 左右。但在 Sapphire Rapids 至强处理器平台上，单个 Ponte Vecchio OAM（双堆栈 MCM）还是实现了至少 45 TFLOPs 的 FP32 吞吐量。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0821/98f50295ad2f1ce.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0821/98f50295ad2f1ce.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图 via <a href="https://www.techpowerup.com/285783/intel-ponte-vecchio-early-silicon-puts-out-45-tflops-fp32-at-1-37-ghz-already-beats-nvidia-a100-and-amd-mi100" target="_self">TechPowerUp</a>）</p><p>如此耀眼的成绩，已经超越了英伟达 Ampere A100 Tensor Core 40GB 竞品所宣传的 19.5 TFLOPs，此外 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Instinct MI100 计算卡也仅提供了 23.1 TFLOPs 的 FP32 性能。</p><p><img src="https://static.cnbetacdn.com/article/2021/0821/eaffc893d1dca0f.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>“A0”版本应该是首批从代工厂流片回来的 Ponte Vecchio 原型，且<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>内部应该正在通过严格的 NDA 协议，来下发给 ISV 与行业合作伙伴。</p><p><a href="https://static.cnbetacdn.com/article/2021/0821/414b2871019a500.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0821/414b2871019a500.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p>通常情况下，芯片制造商只会将时钟速率明显低于最终性能的原型交付给 ISV，以便其充分测试相关功能和开发特定的软件。</p><p><a href="https://static.cnbetacdn.com/article/2021/0821/d6d5647ae63df15.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0821/d6d5647ae63df15.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a></p><p>参考英特尔在演示文稿中提到的数据，OAM 封装的每时钟周期 FP32 吞吐量为 32768 ops，且单个封装中的两个堆栈相当于 128 个 Xe 核心。</p><p><a href="https://static.cnbetacdn.com/article/2021/0821/05d45b79b06275b.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0821/05d45b79b06275b.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a></p><p>每个 Xe HPC 的核心矢量引擎，可在单个时钟周期内提供 256 次 FP32 操作，那样单封装（双堆栈）的总和为 32468 FP32 ops/clock，约等于 1373MHz 。</p><p><a href="https://static.cnbetacdn.com/article/2021/0821/8f3e77a43627792.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0821/8f3e77a43627792.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a></p><p>不过随着后续的生产迭代，我们有望看到更高的始终速率、以及吞吐量的线性扩展。不过考虑到芯片的庞大尺寸和功率消耗（传闻为 600W），最终运行频率卡在 1.37GHz 也不是不可能。</p><p><img src="https://static.cnbetacdn.com/article/2021/0821/a272253adcbc617.jpg" alt="7.jpg" referrerpolicy="no-referrer"></p><p>在用功耗换性能的情况下，英特尔甚至会要求厂商为 OAM 搭配高性能的水冷散热方案。至于其能否在 HPC 市场获得充分的认可，仍有待时间去检验。</p><p><img src="https://static.cnbetacdn.com/article/2021/0821/3137bc80f1b1bf6.jpg" alt="8.jpg" referrerpolicy="no-referrer"></p>   
</div>
            