
---
title: 'NVIDIA 4nm GPU性能首秀：最大4.5倍提升'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0909/cdf37ad2ea0a6de.jpg'
author: cnBeta
comments: false
date: Fri, 09 Sep 2022 12:20:22 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0909/cdf37ad2ea0a6de.jpg'
---

<div>   
北京时间9月9日，MLCommons社区发布了最新的MLPerf 2.1基准测试结果，新一轮基准测试拥有近5300个性能结果和2400个功耗测量结果，分别比上一轮提升了1.37倍和1.09倍，MLPerf的适用范围进一步扩大。<strong>阿里巴巴、华硕、Azure、壁仞科技、戴尔、富士通、技嘉、H3C、HPE、浪潮、Intel、Krai、联想、Moffett、Nettrix、Neural
Magic、NVIDIA、OctoML、高通、SAPEON 和 Supermicro 均是本轮测试的贡献者。</strong><br>
 <p>其中，NVIDIA表现依然亮眼，首次携H100参加MLPerf测试，并在所有工作负载中刷新世界纪录。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0909/cdf37ad2ea0a6de.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0909/cdf37ad2ea0a6de.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0909/cdf37ad2ea0a6de.jpg" referrerpolicy="no-referrer"></a></p><p><strong>H100打破世界记录，较A100性能提升4.5倍</strong></p><p>NVIDIA于今年3月份发布基于新架构NVIDIA Hopper的H100 GPU，与两年前推出的NVIDIA Ampere架构相比，实现了数量级的性能飞跃。</p><p>黄仁勋曾在 GTC 2022 上表示，20个H100 GPU便可以承托相当于全球互联网的流量，能够帮助客户推出先进的推荐系统及实时运行数据推理的大型语言模型。</p><p>令一众AI从业者期待的H100原本定于2022年第三季度正式发货，目前处于接受预定状态，用户的真实使用情况和H100的实际性能尚不可知，因此可以通过最新一轮的MLPerf测试得分提前感受H100的性能。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0909/3b425a829e8181b.png"><img data-original="https://static.cnbetacdn.com/article/2022/0909/3b425a829e8181b.png" src="https://static.cnbetacdn.com/thumb/article/2022/0909/3b425a829e8181b.png" referrerpolicy="no-referrer"></a></p><p>在本轮测试中，对比Intel Sapphire Rapids、Qualcomm Cloud AI 100、Biren BR104、SAPEON X220-enterprise，NVIDIA H100不仅提交了数据中心所有六个神经网络模型的测试成绩，且在单个服务器和离线场景中均展现出吞吐量和速度方面的领先优势。</p><p><strong>以NVIDIA  A100相比，H100在MLPerf模型规模最大且对性能要求最高的模型之一——用于自然语言处理的BERT模型中表现出4.5倍的性能提升，在其他五个模型中也都有1至3倍的性能提升。</strong></p><p>H100之所以能够在BERT模型上表现初出色，主要归功于其Transformer Engine。</p><p>其他同样提交了成绩的产品中，只有Biren BR104在离线场景中的ResNet50和BERT-Large模型下，相比NVIDIA A100有一倍多的性能提升，其他提交成绩的产品均未在性能上超越A100。</p><p>而在数据中心和边缘计算类别的场景中，A100 GPU的测试成绩依然不俗，得益于NVIDIA AI软件的不断改进，与2020年7月首次亮相MLPerf相比，A100 GPU实现了6倍的性能提升。</p><p><strong>追求AI通用性，测试成绩覆盖所有AI模型</strong></p><p>由于用户在实际应用中通常需要采用许多不同类型的神经网络协同工作，例如一个AI应用可能需要理解用户的语音请求、对图像进行分类、提出建议，然后以语音回应，每个步骤都需要用到不同的AI模型。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0909/f7af026e92f18b2.png"><img data-original="https://static.cnbetacdn.com/article/2022/0909/f7af026e92f18b2.png" src="https://static.cnbetacdn.com/thumb/article/2022/0909/f7af026e92f18b2.png" referrerpolicy="no-referrer"></a></p><p>正因如此，MLPerf基准测试涵盖了包括计算机视觉、自然语言处理、推荐系统、语音识别等流行的AI工作负载和场景，以便于确保用户获得可靠且部署灵活的性能。</p><p>这也意味着，提交的测试成绩覆盖的模型越多，成绩越好，其AI能力更加具备通用性。</p><p>在此轮测试中，NVIDIAAI依然是唯一能够在数据中心和边缘计算中运行所有MLPerf推理工作负载和场景的平台。</p><p>在数据中心方面，A100和H100都提交了六个模型测试成绩。</p><p>在边缘计算方面，NVIDIA Orin运行了所有MLPerf基准测试，且是所有低功耗系统级芯片中赢得测试最多的芯片。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0909/a494b075e95a2d9.png"><img data-original="https://static.cnbetacdn.com/article/2022/0909/a494b075e95a2d9.png" src="https://static.cnbetacdn.com/thumb/article/2022/0909/a494b075e95a2d9.png" referrerpolicy="no-referrer"></a></p><p>Orin是将NVIDIA Ampere架构GPU和Arm CPU内核集成到一块芯片中，主要用于机器人、自主机器、医疗机械和其他形式的边缘嵌入式计算。</p><p>目前，Orin已经被用在NVIDIA Jetson AGX Orin开发者套件以及机器人和自主系统生成模考，并支持完整的NVIDIA AI软件堆栈，包括自动驾驶汽车平台、医疗设备平台和机器人平台。</p><p>与4月在MLPerf上的首次亮相相比，Orin能效提高了50%，其运行速度和平均能效分别比上一代Jetson AGX Xavier 模块高出5倍和2倍。</p><p>追求通用型的NVIDIA AI 正在被业界广泛的机器学习生态系统支持。在这一轮基准测试中，有超过70 项提交结果在 NVIDIA 平台上运行。例如，Microsoft Azure 提交了在其云服务上运行NVIDIA AI 的结果。</p>   
</div>
            