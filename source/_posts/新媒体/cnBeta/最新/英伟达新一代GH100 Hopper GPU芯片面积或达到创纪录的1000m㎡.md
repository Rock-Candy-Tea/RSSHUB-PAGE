
---
title: '英伟达新一代GH100 Hopper GPU芯片面积或达到创纪录的1000m㎡'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0129/3931efd3bc430bd.png'
author: cnBeta
comments: false
date: Sat, 29 Jan 2022 06:41:37 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0129/3931efd3bc430bd.png'
---

<div>   
近日，英伟达被曝在代号为“Hopper”的新一代 GPU 的商标申请上遭到了 Dish Network 的反对，但这并不妨碍该公司旗舰芯片的迭代开发。<strong>@Kopite7Kimi 刚刚在一条推文中指出，传说中的 GH100 GPU，或具有不少于 1000 m㎡ 的占地面积。</strong>作为参考，绿厂当前在售的 Ampere GA100 GPU，尺寸也仅为 826 m㎡ 。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0129/3931efd3bc430bd.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">推特截图</p><p>若传闻属实，那 Hopper GH100 将成为英伟达史上最大的单 GPU 设计，且支持 HBM2e 高带宽缓存与其它先进的连接特性。</p><p>然而这还没完，考虑到 Hopper 将引入对多芯片模块化（MCM）方案的 GPU，我们大可期待在单个基板上融合的两颗 GH100 GPU —— 仅裸片面积就超过了 2000 m㎡ 。</p><p><img src="https://static.cnbetacdn.com/article/2022/0129/79b6fe7669e81fb.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">商标申请争议</p><p>据悉，Hopper GPU 将采用台积电 5nm 工艺制造，两两结合就是总计 288 组 SM 单元。至于每组 SM 所包含的核心数量，目前暂不得而知。</p><p>如果按照每组 64 个 CUDA 单元来计算，那我们将看到 18432 个核心 —— 规格凶猛到“满血版”Ampere GA 100 GPU 的 2.25 倍。</p><p>此外英伟达可以让 Hopper GPU 用上更多的 FP64、FP16 和 Tensor 内核，这也是要与<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> Ponte Vecchio（预计规格为 1:1 FP64）拼刺刀的一个重要先决条件。</p><p>最终配置很可能在每颗 GPU 模块上启用 144 组 SM 单元中的 134 个（单芯的可能性仍然存在）。</p><p>但若不使用 GPU Sparsity，该功能或很难达到与 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Instinct MI200 相同的 FP32 / FP64 性能水平。</p><p><img src="https://static.cnbetacdn.com/article/2022/0129/467a5e6553efa71.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">有关 GH100 单双芯的讨论仍在持续</p><p>即便如此，英伟达仍可能藏了一款秘密武器，那就是让 Hopper GPU 基于 COPA 方案来实现。</p><p>该公司曾谈到两款基于下一代架构的 Domain-Specialized COPA-GPU，且分别面向高性能计算（HPC）和深度学习（DL）细分市场。</p><p>HPC 衍生版本通常会选用标准解决方案，包含 MCM GPU 设计与各自的 HBM / MC + HBM（IO）小芯片。</p><p>相比之下，DL 衍生版本则要有趣得多，比如在 GPU 模块互连的完全独立的裸片上拥有巨大的缓存。</p>   
</div>
            