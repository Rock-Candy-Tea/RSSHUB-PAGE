
---
title: '里程碑式Google TPU v4重磅发布！ 单个Pod性能是世界第一超算的两倍'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202105/60a52afa8e9f0955777b8d09_1024.jpg'
author: ZAKER
comments: false
date: Wed, 19 May 2021 15:15:26 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202105/60a52afa8e9f0955777b8d09_1024.jpg'
---

<div>   
<p>Google I/O 开发者大会去年因为疫情而取消，今年采取线上形式强势回归。在没有开发者在场的 Google 园区内，Google CEO 桑达尔 · 皮查伊（Sundar Pichai）宣布推出多项全新技术，除了能够帮助用户实现 " 空间瞬移 " 的全息视频聊天技术 Project Starling 让人耳目一新，还有最新一代 AI 芯片 TPU v4。</p><p><strong>" 这是我们在 Google 上部署的最快的系统，对我们来说是一个具有历史意义的里程碑。" 皮查伊这样介绍到。</strong></p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202105/60a52afa8e9f0955777b8d09_1024.jpg" data-height="299" data-width="626" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202105/60a52afa8e9f0955777b8d09_1024.jpg" referrerpolicy="no-referrer"></div></div><strong>最强 TPU，速度提升 2 倍，性能提升 10 倍</strong><p></p><p>Google 官方介绍，在相同的 64 芯片规模下，不考虑软件带来的改善，TPU v4 相较于上一代 TPU v3 性能平均提升 2.7 倍。</p><p>在实际应用中，TPU v4 主要与 Pod 相连发挥作用，每一个 TPU v4 Pod 中有 4096 个 TPU v4 单芯片，得益于其独特的互连技术，能够将数百个独立的处理器转变为一个系统，互连带宽在规模上是其他任何网络技术的 10 倍，每一个 TPU v4 Pod 就能达到 1 exaFlOP 级的算力，实现每秒 10 的 18 次方浮点运算。这甚至是全球最快的超级计算机 " 富岳 " 的两倍性能。</p><p><strong>" 如果现在有 1 千万人同时使用笔记本电脑，所有这些计算机累加的计算能力，刚好就能够达到 1 exaFLOP 的算力。而之前要达到 1 exaFLOP，可能需要专门定制一个超级计算机。" 皮查伊如是说。</strong></p><p>今年的 MLPerf 结果表明，GoogleTPU v4 的实力不容小觑，在使用 ImageNet 数据集的图像分类训练测试（准确度至少 75.90%），256 个 TPU v4 在 1.82 分钟内完成了这一任务，这几乎与 768 个 Nvidia A100 图形卡、192 个 AMD Epyc 7742 内核（1.06 分钟）、512 个华为 AI 优化的 Ascend910 芯片以及 128 个 Intel Xeon Platinum 8168 内核（1.56 分钟）组合在一起的速度一样快。</p><p>当负责在大型维基百科语料库上训练基于 Transform 的阅读理解 BERT 模型时，TPU v4 的得分也很高。使用 256 个 TPU v4 进行训练需要 1.82 分钟，比使用 4096 TPU v3 进行训练所需的 0.39 分钟要慢 1 分多钟。同时，如果想要使用 Nvidia 的硬件达到 0.81 分钟的训练时间，需要 2048 张 A100 卡和 512 个 AMD Epyc 7742 CPU 内核。</p><p>Google 同样在 I/O 大会上展示了能够用到 TPU v4 的具体 AI 实例，包括能够同时处理网页、图像等多种数据的 MUM 模型（Multitask Unified Model，多任务统一模型）和专为对话打造的 LaMDA 都是能够用到 TPU v4 的场景模型，前者比阅读理解模型 BERT 强 1000 倍，适合赋能搜索引擎帮助用户更加高效地得到自己想要的信息，后者则可以与人类进行不间断的对话交流。</p><p>这一并不向外出售的 TPU，很快将在被部署在 Google 的数据中心，且 90% 左右的 TPU v4 Pod 都将使用绿的能源。<strong>另外，Google 也表示，将在今年晚些时候开放给 Google Cloud 的客户。</strong></p><p><strong>Google 自研 TPU，五年更新四代</strong></p><p>Google 最早于 2016 年宣布首款内部定制的 AI 芯片，区别于训练和部署 AI 模型的最常见的组合架构，即 CPU 和 GPU 组合，第一代 TPU 在那场世界著名的人机围棋大战助力 AlphaGo 打败李世石 " 一战成名 "，宣告并不是只有 GPU 才能做训练和推理。</p><p>Google 第一代 TPU 采用 28nm 工艺制程，功耗大约 40w，仅适用于深度学习推理，除了 AlphaGo，也用在 Google 搜索、翻译等机器学习模型中。</p><p>2017 年 5 月，Google 发布了能够实现机器学习模型训练和推理的 TPU v2，达到 180TFLOPs 浮点运算能力，同时内存带宽也得以提升，比同期推出的 CPU AI 工作负载提升 30 倍，比 GPU AI 工作负载提升 15 倍，被基于 4 块 TPU v2 的 AlphaGo 击败的世界围棋冠军柯洁最直观地感受了这一切。</p><p>2018 年 5 月，Google 又发布第三代 TPU，性能是上一代 TPU 的两倍，实现 420TFLOPs 浮点运算，以及 128GB 的高带宽内存。</p><p>按照一年一次迭代更新的节奏，Google 理应在 2019 年推出第四代 TPU，不过这一年的 I/O 大会上，Google 推出的是第二代和第三代 TPU Pod，可以配置超过 1000 颗 TPU，大大缩短了在进行复杂的模型训练时所需耗费的时间。</p><p><strong>在 AI 芯片发展史上，无论是从片上内存上，还是从可编程能力来看，Google TPU 都是不可多得的技术创新，打破 GPU 的 " 垄断 " 地位，且打开云端 AI 芯片的新竞争格局。</strong></p><p>发展五年的 Google TPU 在今天依然保持着强劲的竞争力，未来的世界是什么样的？Google TPU 已经告诉了我们一小部分答案。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            