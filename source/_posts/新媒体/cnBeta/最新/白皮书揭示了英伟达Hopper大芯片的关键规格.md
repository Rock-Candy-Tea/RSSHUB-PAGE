
---
title: '白皮书揭示了英伟达Hopper大芯片的关键规格'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0504/00be79779caf4ac.jpg'
author: cnBeta
comments: false
date: Wed, 04 May 2022 08:46:46 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0504/00be79779caf4ac.jpg'
---

<div>   
<strong>为英伟达下一代 H100 加速卡提供支撑的 GH100 芯片，纸面规格已经让人感到十分惊讶。不过周末曝光的白皮书，又让我们对其有了更深入的了解。</strong>据悉，绿厂正在积极利用台积电的 N4（4nm 级 EUV）先进工艺来构建 Hopper GPU，而 H100 大芯片更是被六个 HBM3 高带宽显存堆栈给环绕着。<br>
<p><a href="https://static.cnbetacdn.com/article/2022/0504/00be79779caf4ac.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0504/00be79779caf4ac.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图 via <a href="https://www.computerbase.de/2022-05/nvidia-hoppher-gh100-whitepaper/" target="_self">ComputerBase.de</a>）</p><p><a href="https://www.techpowerup.com/294503/nvidia-hopper-whitepaper-reveals-key-specs-of-monstrous-compute-processor" target="_self">TechPowerUp</a> 指出：GH100 计算芯片拥有 800 亿个庞大的晶体管数量，较 GA100 增加近 50% 。</p><p><img src="https://static.cnbetacdn.com/article/2022/0504/ea8c22610f0ff2e.png" alt="2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">Hopper GPU 的流处理器设计</p><p>有趣的是，在 4nm EUV 工艺的加持下，GH100 的芯片面积却只有 814 m㎡，小于基于 7nm DUV（台积电 N7 工艺）节点制造的 GA100（826 m㎡）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0504/594f8ff47ffba40.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">Ampere GPU 的流处理器设计</p><p>由图可知，英伟达 GH100 的组件层次结构与上一代类似，主要数学运算部分被布置到了 144 组流处理器（SM）上。</p><p>GH100 拥有 18432 个 FP32（单精度）/ 9216 个 FP64 （双精度）CUDA 核心，辅以 576 个第四代 Tensor 核心，此外硅片上其中一组 GPC 具有光栅图形单元。</p><p><a href="https://static.cnbetacdn.com/article/2022/0504/8ba3c8b0d04d251.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0504/8ba3c8b0d04d251.png" alt="4.png" referrerpolicy="no-referrer"></a></p><p>鉴于 GH100 具有 6144-bit 的 HBM3 显存位宽，英伟达或为其标配 80GB VRAM，预计带宽可超 3 TB/s（且有 ECC 加持）。</p><p>主机接口也迎来了重大升级，且 SXM 外形的 PCB 板上配备了最新一代 NVLink 界面（具有 900 GB/s 的带宽）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0504/a737b94f6dd091e.png" alt="5.png" referrerpolicy="no-referrer"></p><p>AIC 插卡版本则是采用了 PCIe 5.0 x16（128 GB/s）接口，且两者都引入了资源池（resource-pooling）功能。</p><p>最后，英伟达正在用更高的功耗来压榨更多的性能 —— 可知 H100 的典型功率值为 700W，而 A100 仅为 400W 。</p><p><a href="https://static.cnbetacdn.com/article/2022/0504/0fa0d5164503756.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0504/0fa0d5164503756.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a></p><p>不过 H100 并非满血 SKU，即使高密度的 SXM 外形版本，也只启用了 144 组 SM 单元中的 132 个 。</p><p>PCIe 插卡版本更是仅启用了 114 个 SM 单元，且两者的最高时钟速率都是 1.80 GHz 。</p>   
</div>
            