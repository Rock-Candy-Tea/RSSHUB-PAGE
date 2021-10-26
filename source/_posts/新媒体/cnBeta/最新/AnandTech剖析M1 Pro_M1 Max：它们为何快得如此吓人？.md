
---
title: 'AnandTech剖析M1 Pro_M1 Max：它们为何快得如此吓人？'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/10/a6298bb8205751b.jpg'
author: cnBeta
comments: false
date: Tue, 26 Oct 2021 06:45:48 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/10/a6298bb8205751b.jpg'
---

<div>   
2021 年新款 MacBook Pro 已经陆续发货，从媒体和消费者的初期反馈来看都是积极的。苹果的 M1 Pro 和 M1 Max 在性能上已经超出大部分采用 Intel 和 AMD 的笔记本，也超越了某些桌面级 CPU，在部分测试中甚至接近服务器级配置。<strong>那么 M1 Pro/M1 Max 为何会这么强？</strong><br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/10/a6298bb8205751b.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/10/a6298bb8205751b.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;"><strong>性能核心</strong></p><p style="text-align: left;">AnandTech 在其评论中解释说，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>在 M1 Max 和 M1 Pro 上都保持了与 M1 类似的 CPU 设计。但是，虽然 CPU 可能是相同的，但它具有八个 Firestorm 性能核心和两个 Icestorm 效率核心。CPU 核心的峰值为 3228 MHz，但频率根据参与的核心数量而变化。</p><p style="text-align: left;"><strong>内存带宽和接口</strong></p><p style="text-align: left;">MacBook Pro 性能提升的另一个突破口是内存带宽和接口。这两款芯片的一个大特点是内存带宽和接口大大增加--M1 Pro 采用 256 位 LPDDR5 内存，速度为 6400MT/s，对应 204GB/s 带宽。这明显高于 M1 的 68 GB/s，也普遍高于仍然依赖 128 位接口的竞争者笔记本平台。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1026/7faccb6ab739571.gif" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/1026/7faccb6ab739571.gif" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">M1 Max 的表现更加优秀。苹果还在内存接口上增加了一倍[不仅仅是 GPU 核心的数量]，使用了高达 512 位宽的 LPDDR5 内存子系统--在SoC中闻所未闻，在历史上的独立 GPU 设计中也是罕见的。这给芯片带来了 408GB/s 的巨大带宽--这一带宽如何被芯片上的各种 IP 块所使用，是我们今天要调查的事情之一。</p><p style="text-align: left;"><strong>GPU 升级</strong></p><p style="text-align: left;">AnandTech 评论到，M1 Max 和 M1 Pro MacBook Pro 笔记本电脑的另一个明显升级体现在 GPU 方面。该媒体评论道：“从来没有任何 PC 处理器在出厂时将如此强大的 GPU 集成到主 SoC 中”。</p><p style="text-align:center"><a href="https://x0.ifengimg.com/ucms/2021_44/DE27B6247018392E09F2F1FF7220D36F302B9604_size1379_w432_h240.gif" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/1026/a10750006a2f880.gif" referrerpolicy="no-referrer"></a></p><p style="text-align: left;"><strong>显存升级对 GPU 性能有重要作用：</strong></p><p style="text-align: left;">M1 Max 有一个 512 位的接口，是原来 M1 的 128 位接口的 4 倍。可以肯定的是，以这种方式扩大 LPDDR 的规模一直是可能的，但至少在消费类 SoC 领域，这是以前从未做过的。有了这么宽的接口，苹果能够给 M1 Max 提供 400GB/s（技术上是 409.6GB/s）的内存带宽，这与英伟达最快的笔记本 SKU 上的带宽量相当。</p><p style="text-align: left;">评论中提到，游戏仍然是 MacBook Pro 的一个薄弱点。但不是因为 GPU 不能处理它。更多的是 macOS 上的可用性问题，这使 MacBook Pro 的游戏玩家处于不利地位。</p><p style="text-align: left;"><strong>小结</strong></p><p style="text-align: left;">AnandTech 的观点是非常明确的。M1 Pro 和 M1 Max 不同于目前业界的任何产品。</p><p style="text-align: left;">M1 Pro 和 M1 Max 完全改变了叙述方式--这些设计感觉是真正的 SoC，在制作时考虑到了资深用户，苹果在所有矢量上都提高了性能指标。我们预计会有很大的性能跃升，但我们没有想到新芯片能够实现的一些巨大的增长。</p><p style="text-align: left;">在内存方面，苹果已经将其内存子系统扩展到前所未有的尺寸，这使得 M1 Pro 和 Max 能够实现在笔记本电脑芯片中根本没有出现过的性能数字。这里的芯片不仅能够超越任何竞争对手的笔记本电脑设计，而且还能与最好的台式机系统竞争，你必须拿出服务器级别的硬件来超越 M1 Max--这一般来说是很荒谬的。</p><p style="text-align: left;">2021 年的 MacBook Pro 型号实现了“依赖 GPU 加速的内容创作和生产力工作负载的巨大性能飞跃”。这将吸引那些需要新芯片所能提供的那种先进性的专业人士。</p><p style="text-align: left;">看来苹果公司了解典型的 MacBook Pro 强大的用户，并围绕 Mac 的使用情况设计了芯片，使其大放异彩。原始性能、独特的加速以及纯粹的功率效率的结合，是你现在在任何其他平台上都找不到的，可能使新的 MacBook Pro 不仅是最好的笔记本电脑，而且是最适合这项任务的设备</p>    
</div>
            