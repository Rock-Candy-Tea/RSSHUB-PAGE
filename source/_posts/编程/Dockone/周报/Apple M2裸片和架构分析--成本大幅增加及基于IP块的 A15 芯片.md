
---
title: 'Apple M2裸片和架构分析--成本大幅增加及基于IP块的 A15 芯片'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8ba3c972-8372-453a-9a89-0dc8e7c2ad8b_1024x572.jpeg'
author: Dockone
comments: false
date: 2022-06-26 08:10:36
thumbnail: 'https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8ba3c972-8372-453a-9a89-0dc8e7c2ad8b_1024x572.jpeg'
---

<div>   
<br>Apple 在 WWDC 上宣布了他们新的拥有 200 亿晶体管的 M2 SoC。 不幸的是，它在 CPU 等某些领域的性能提升非常小。 苹果这次提升主要是在 GPU 和视频编辑方面。 考虑到这款新 M2 带来的原始成本增加以及 M1 推出以来已经将近 2 年的事实，整体性能提升非常令人失望。 和我们之前在 A16 上报道的一样，由于成本问题，<a href="https://semianalysis.substack.com/p/as-moores-law-slows-apple-is-forced?s=w">Apple 被迫将 SoC 选择分散到 Pro iPhone 型号上的 A16 和普通 iPhone 型号上的 A15</a>。<br>
<br>今天，我们将讨论与 M2 架构和 Apple 未来设计相关的细节，包括在 WWDC 上未讨论的 M2 Pro/Max 和 M3。 我们还将对 Apple 在 Locuza 的帮助下发布的 M2 图像芯片面积（die area）进行分析。 如果您喜欢听而不是阅读，<a href="https://www.youtube.com/watch?v=r1OBUIwS_Dc">我们制作了一个 YouTube 视频</a>。<br>
<br><img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8ba3c972-8372-453a-9a89-0dc8e7c2ad8b_1024x572.jpeg" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>很奇怪，我们看到一些专家谈论这是 M1.5 或 M1+。 这都是胡说八道。 除了一些偏差之外，M1 通常与 Apple A14 基于相同的 IP 块。 M2，代号为Staten，一般与代号为Ellis的A15基于相同的IP块。 这些代号基于纽约一些最著名的岛屿，这应该暗示了这些架构的密切相关性。 鉴于与 M1 存在近 2 年的差距，在性能提升方面，许多令人失望的原因是发电量增长疲软。 许多人对 M2 的期望更高。<br>
<br>我们之前<a href="https://semianalysis.com/apple-cpu-gains-grind-to-a-halt-and-the-future-looks-dim-as-the-cpu-engineer-exodus-to-nuvia-and-rivos-impact-starts-to-bleed-in/">讨论过这个问题</a>，但是放缓的很大原因是来自苹果公司，它流失了许多优秀的工程师到其他公司，比如 <a href="https://semianalysis.com/apple-cpu-gains-grind-to-a-halt-and-the-future-looks-dim-as-the-cpu-engineer-exodus-to-nuvia-and-rivos-impact-starts-to-bleed-in/">Nuvia 和 Rivos</a> 等公司。 最近几年，这种流失并没有停止，这种原因简单来说是苹果的工作文化不是最好的以及其他公司，即谷歌、微软、亚马逊和 Meta 等大公司，在福利待遇方面给付的更多。 最后，还有大量非金钱动机的工程师外流，他们认为他们已经成功地完成了将苹果从英特尔芯片转移到自家芯片上。 这些工程师离开去从事他们认为其他更有趣的项目，无论是在大企业还是传统公司。<br>
<br>这些偏离最终在 A15 和 M2 以及即将推出的 A16 中达到顶峰，最终带来了不温不火的 CPU 增益。 我们听说 A16 将不会使用基于 Armv9 的下一代内核，如果苹果是第一个实施 Armv8 的，这真是令人难过。 我们听说下一代 Armv9 内核只会出现在 M3 中，这将是苹果在台积电 N3 节点上的第一款产品。 Apple 已经设计并流片出了 M2 Pro 和 M2 Max，它们仍然基于 N5 和 A15 基础 IP。<br>
<br><img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F69502024-a55e-4ceb-bbd4-0cf1193153d8_1024x421.jpeg" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>让我们深入裸片（die shot）了解一下。 Apple 展示了 M1 和 M2 的未标记图像。 这表明 M2 为 141.7mm2，但我们认为 Apple 修改了芯片图像。 这不是苹果第一次这么做了。 Apple 之前在 <a href="https://twitter.com/dylan522p/status/1450286632729518089?s=20&t=rK10G4Q9PcTSeERJYRIRww">M1 Max 上做了同样的事情</a>，他们隐藏了 M1 Ultra 中使用的 die-to-die 连接。 他们还改变了尺寸大小。<br>
<br><img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F21795c5c-b04c-43ab-87e4-1f26da858693_1024x331.png" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>苹果提供的图片似乎与实际的 M2 不相称。 SRAM 单元和 PHY在不同芯片上应该是一样的，我们可以基于这个来辨别，然后看到 M2 似乎比它实际的要小。 Apple 推出的 M2 比 A15 具有更高的晶体管密度，这个看上去也不一致。 由于专用于高密度 SRAM 单元的总面积较小，而专用于 IO 和其他逻辑的总面积较大，因此它的密度将较低。 出于这个原因，Locuza 缩放了 M2 晶粒（die）。 这种缩放带来了与 Apple 在 M1 和 A15 上相同的 SRAM 单元和相同的 PHY。 Apple 展现的图片意味着在晶粒尺寸缩放后存在大约 3% 的错误窗口。 尽管有误差线，但数字仍按测量值显示。<br>
<br>接下来我们看一下Apple怎么增加晶粒尺寸的。<br>
<br><img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5c08fac1-c4bf-4d5e-aebb-b598b87afdc9_1024x479.jpeg" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>首先让我们从 Apple 的 P-Core 开始。 它基于 A15 中出现的 Apple Avalanche 核心，仅仅存在一些细微差别。 这遵循了 M1 Pro 和 M1 Max 拥有一个修改后的Firestorm，它通过实现一个更大的 PA 来处理更大的内存大小。 基于 M 核心也有一些修改，这用于在 MacOS 上必须要支持的可变页大小。<br>
<br><img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1b16a058-cf31-4482-995c-089932dd9d42_1024x123.png" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>核心本身比 M1 大 21%，比 A15 大 7%。 与 M1 和 A15 相比，每一代增长最大的地方就是共享缓存 L2 ，它已经从 12MB 增长到 16MB。 AMX 单元在 A15 和 M1 上看起来也一样。 共享逻辑平面也明显更大，这表明内核与 L2 高速缓存和 SLC 之间存在更多带宽。 总体而言，Apple 在 P-Core 上花费了更大空间 5.2mm2，但它们的性能提升主要来自时钟速度。 <a href="https://www.anandtech.com/show/16983/the-apple-a15-soc-performance-review-faster-more-efficient/2">正如评论中所记录的那样</a>，IPC 的增长非常小。<br>
<br>一个非常有趣的变化是，A15 和 M2 中 Avalanche 核心的 ROB 与 M1 和 A14 中 Firestorm 核心相比显得更小。 这一点特别有趣，因为为了获得业界最宽、最高的 IPC 内核，苹果拥有业界最大的 ROB。<br>
<br><img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8a4f288b-769a-4098-9e3a-ec09f7acbfcf_838x404.jpeg" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>从 CPU 的角度来看，E-Core 是从 A14 到 A15 的主要变化单元，这里也是如此。 在缩放 Apple 提供的裸片后，A15 和 M2 的 E-Core 看起来几乎相同，这很好的表明，缩放是准确的。 Apple 对 Mac 芯片的 E-Core 进行了较少或没有修改，因为他们对 P-Core 上的这些更改进行了一些调整和不同的物理设计。<br>
<br><img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F45b9996e-e0fb-42a2-97c0-b72ce6dcf59f_1024x165.png" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>关于 E-Core，这里没有太多要说的，因为它与经过<a href="https://www.anandtech.com/show/16983/the-apple-a15-soc-performance-review-faster-more-efficient/2">广泛测试的 A15</a> 非常相同。 整个 E-Core 复合体经过几代的发展也才大了 1mm2，而整个 CPU 复合体则大了 6.2mm2。<br>
<br><img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4c373ad0-2ac1-4219-832a-75e037481764_1024x301.jpeg" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>缩放后的 GPU 与 128 ALU 的 M1 相比，每个内核的大小也几乎相同。 这很有趣，因为它是 M1 与 A14 不同之处之一。 尽管它们在同一代，但架构发生了变化。 相比于A SoC，苹果会优先在 X SoC 上做出改变。 例如，A6 和 A6X 在多年前就有不同的 GPU 架构。 鉴于 M 系列 SoC 只是 X 系列的更名。 这一代GPU核心本身似乎没有变化，但共享逻辑和杂项更大，因此在一些固定功能方面可能会有变化。 主要变化是在核心数量上， Apple 将其提升到 10 核 GPU 。单从 GPU 时钟速度来看，它从 1.27 GHz 上升到 1.406 GHz。<br>
<br><img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fca212b72-2bc4-4b66-bf15-4c6670ff69dd_1022x164.png" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>新的 GPU 总共增加了近 7 mm2。 尽管 Apple 表示在最高性能水平时功耗略有上升，但带来的性能提升还是很值得的。 在相同的功率水平下，由于更好的内存以及一个整体更宽/更慢的设计，Apple 仍然获得了不错的性能提升。 我们在这里也包括了 NPU 和 SLC 数据。 NPU 的数据有点奇怪，所以我们将跳过这些数据。 SLC 是有趣的地方。<br>
<br><img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3358b9e8-3339-45fc-874c-a12c2e650cb9_1022x272.jpeg" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>每个 2MB 数据阵列在 M1、A15 和缩放后的 M2 裸片上的大小通常相同，这是有意义的并证明了基于相同 PHY 大小进行缩放是合理的。 从第 1 代到第 2 代 N5 工艺节点没有缩小 SRAM 。 尽管如此，SLC 大小在 M2 上还是有所增长，这可能是为了给各种 IP 块（例如更大的 GPU）带来更多的带宽。<br>
<br><img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6272bad-2379-4e5e-b728-e3558b77affd_1024x208.jpeg" alt="请输入图片名称" referrerpolicy="no-referrer"><br>
<br>最后一个要对比的 IP 块是内存控制器 + PHY。 苹果在这里大幅增加了面积以支持 LPDDR5 6400。上图展示的是 1 个单元，当然内存控制器是多通道的。 专用于 128 位 LP5 总线的总面积约为 14mm2，而带有 128 位 LP4X 的 M1 为 8.1mm2，带有 64 位 LP4X 的 A15 为 4.3mm2。 从成本这个关键角度来看，LPDDR5 6400 比 LPDDR4X 4266 贵得多。<br>
<br>这也是 Apple 在今年即将推出的 iPhone 上拆分 A15 A16 阵容的重要组成部分。 我们之前在<a href="https://semianalysis.substack.com/p/as-moores-law-slows-apple-is-forced?s=w">这里</a>做了预测。 总体而言，苹果必须在 M2 上应对类似的问题，这就是为什么他们将基于 M1 的机型保留在低端市场。 晶圆价格的小幅上涨、更大的芯片从 118.91mm2 到 155.25mm2 以及更昂贵的内存的组合是造成这种情况的主要原因。<br>
<br>最后一个我们没有评估的 IP 块是更大的媒体引擎，用于增强媒体功能。 Apple 的 M 系列是迄今为止最适合专业创作人士的芯片。 这是毋庸置疑的。 如果你使用 Adobe 套件，M 系列芯片是最好的。<br>
<br>原文链接：<a href="https://semianalysis.substack.com/p/apple-m2-die-shot-and-architecture?s=r">Apple M2 Die Shot and Architecture Analysis – Big Cost Increase And A15 Based IP</a>（翻译：王欢）
                                
                                                              
</div>
            