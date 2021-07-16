
---
title: '一天之内，两大AI预测蛋白结构算法开源，分别登上Nature、Science'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210716/v2_3b9067c1516a46a8a5e02f361be151c2_img_000'
author: 36kr
comments: false
date: Fri, 16 Jul 2021 12:29:18 GMT
thumbnail: 'https://img.36krcdn.com/20210716/v2_3b9067c1516a46a8a5e02f361be151c2_img_000'
---

<div>   
<blockquote> 
 <p>这是科学激动人心的新一步。</p> 
</blockquote> 
<p>使用 DNA 序列预测蛋白质形状的 AphaFold2，终于开源了。 </p> 
<p>众所周知，蛋白质是生命活动的基本组件，它们可以单独存在，也会协同工作。为了发挥作用，这些长链氨基酸扭曲、折叠并交织成复杂的形状，这些形状可能很难，甚至根本不可能破译。 </p> 
<p>科学家们一直在梦想通过基因序列简单地预测蛋白质形状——如果能够成功，这将开启一个洞察生命运作机理的新世界。然而近五十年来，人们的进展缓慢。 </p> 
<p>7 月 15 日，《自然》杂志一篇论文被接收的消息引发了人们的关注，<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>旗下人工智能公司 DeepMind 在研究《Highly accurate protein structure prediction with AlphaFold》中宣布，人们首次发现了一种通过计算来预测蛋白质结构的方法。即使在不知道相似结构的情况下，AI 也可以在原子层面上精确预测蛋白质结构。也就是说，之前备受关注的 AlphaFold2 终于开源了。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210716/v2_3b9067c1516a46a8a5e02f361be151c2_img_000" referrerpolicy="no-referrer"></p> 
<p>无独有偶，作为相当热门的研究领域，Science 同样在今天发表了一篇论文，介绍并开源了一个可媲美 AlphaFold2 的新工具 RoseTTAFold。 </p> 
<p>所以说，赛马了，感兴趣的同学可以自由选择。 </p> 
<h2 label="一级标题" style><strong>AlphaFold2 开源，原子精度预测蛋白质结构</strong></h2> 
<p>2020 年 12 月的国际蛋白质结构预测竞赛 CASP ，一项重磅成果引发了科技界所有人的关注：由 DeepMind 开发的 AlphaFold 2 击败一众选手，在准确性方面达到比肩人类实验结果，被认为是蛋白质折叠问题的解决方案。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210716/v2_15321582c4924eb99c02199cc8d81427_img_000" referrerpolicy="no-referrer"></p> 
<p>在两年一次的 CASP 竞赛中，各组争先预测蛋白质的 3D 结构。2020，AlphaFold 击败了所有其他小组，并在准确性方面与实验结果相匹配。它能以就计算机方法而言前所未有的准确度根据蛋白质的氨基酸序列预测其三维结构。 </p> 
<p>这破解了出现五十年之久的蛋白质分子折叠问题，同时证明了 AI 对于科学发现，尤其是基础科学研究的影响。 </p> 
<p>科学家们纷纷表示，这项突破极具意义。Alphafold 的突破性研究成果将帮助科研人员弄清引发某些疾病的机制，并为设计药物、农作物增产，以及可降解塑料的「超级酶」研发铺平道路。 </p> 
<p>因此，这段时间以来，科研圈也在等待 AlphaFold 2 的技术细节。 </p> 
<p>不久之前，Demis Hassabis 就曾在 Twitter 上表示 DeepMind 将开源 AlphaFold2，如今终于兑现承诺。 </p> 
<p>7 月 15 日，Demis Hassabis、John Jumper 等人在 Nature 杂志上发表了文章《Highly accurate protein structure prediction with AlphaFold》，描述并开源了 AlphaFold2，它预测的蛋白质结构能达到原子水平的准确度。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210716/v2_b48886426bd0434097650b4f00506693_img_000" referrerpolicy="no-referrer"></p> 
<p>链接：https://www.nature.com/articles/s41586-021-03819-2</p> 
<p>开源地址：https://github.com/deepmind/alphafold</p> 
<p>在文章中，DeepMind 表示 AlphaFold 可以周期性的以原子精度预测蛋白质结构。在技术上，AlphaFold 利用多序列对齐，进行深度学习算法的设计，还结合了关于蛋白质结构的物理和生物学知识提升效果。 </p> 
<p>作为通讯作者之一，Demis Hassabis 在一段声明中写到，「去年在 CASP14 大会上我们揭晓了一个可以将蛋白质 3D 结构预测精确到原子水平的全新 AlphaFold 系统，此后我们承诺会分享我们的方法，并为科学共同体提供广泛、免费的获取途径。今天我们迈出了承诺的第一步，在《自然》期刊上分享 AlphaFold 的开源代码，并发表了系统的完整方法论，详尽细致说明 AlphaFold 是如何做到精确预测蛋白质 3D 结构的。作为一家致力于推动科学进步的公司，我们期待看到我们的方法将为科学界启发出什么其他新的研究方法，也期待很快能和大家分享更多我们的新进展。」 </p> 
<p>AlphaFlod 首次参加 CASP 就在 98 名参赛者中名列榜首，准确地从 43 种蛋白质中预测出了 25 种蛋白质的结构。而同组比赛中获得第二名的参赛者仅准确预测出了 3 种。AlphaFold 专注于从头开始建模目标形状，且并不使用先前已经解析的蛋白质作为模板。在大多数情况下，AlphaFold 的准确性与实验相媲美，大大优于其他方法。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210716/v2_60639fecb6c24ce7a0ceaf1b40bb91b6_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图 1：AlphaFold 产出高准确度的架构。 </p> 
<p> AlphaFold 网络直接预测给定蛋白质的所有重原子的三维坐标，使用基本氨基酸序列和同源序列的对齐序列作为输入 (如图 1e）。 </p> 
<p>AlphaFold 网络由两个主要部分组成。首先，网络的主干通过一个称为 Evoformer 的新神经网络块的重复层来处理输入，产生一个 Nseq × Nres 阵列 (Nseq: 序列数，Nres: 残差数) ，它表示一个处理过的 MSA 和一个表示剩余对的 Nres × Nres 阵列。Evoformer 块包含许多新颖的基于注意力和非基于注意力的成分，它的关键创新是与 MSA 交换信息的新机制，并能直接推理空间和进化关系的配对表征。 </p> 
<p>网络的主干之后是结构模块（Structure Module），该模块以蛋白质的每个残基的旋转和平移的形式引入了显式的 3-D 结构。这些表征在微不足道的状态下初始化，所有旋转设置为同一性（identity），所有位置设置为原点，但能够快速开发和完善具有精确原子细节的高度准确的蛋白质结构。这部分网络的关键创新包括打破链原子结构，允许同时局部细化结构的所有部分，一个新的「equivariant transformer」允许网络隐式地推理未表示的侧链原子，以及损失项可对残基方向的正确性赋予重要权重。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210716/v2_3ca587994ac548a1904e21b8ac9d16c7_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图 3：架构细节 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210716/v2_bd906da459054056806ec56f2cfad6f6_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图 4：解释神经网络 </p> 
<p>更多细节大家可以查看 Nature 原文与 DeepMind 提供的补充材料。 </p> 
<p>最后提一句，也不知是何原因，该论文未经编辑就出版了（5 月接收、7 月发表），难道是知道今天 Science 也将发表论文介绍一个可与 AlphaFold2 相匹配的研究？也就是下面这一篇。 </p> 
<h2 label="一级标题" style><strong>华盛顿大学等开发媲美 AlphaFold2 的新工具 RoseTTAFold</strong></h2> 
<p>DeepMind 在 2020 年的 CASP14 会议上展示了其在该领域的显著成果 AlphaFold2，当时该技术在预测蛋白质方面取得了排名第一的准确率。 </p> 
<p>华盛顿大学医学院蛋白质设计研究所（Institute for Protein Design）的研究者们很大程度上重现了 DeepMind 在蛋白质预测任务上的表现，他们联合哈佛大学、德克萨斯大学西南医学中心、剑桥大学、劳伦斯伯克利国家实验室等机构研发出了一款 <strong>基于深度学习的蛋白质预测新工具 RoseTTAFold，在预测蛋白质结构上取得了媲美 AlphaFold2 的超高准确率，而且速度更快、所需要的计算机处理能力也较低</strong> 。 </p> 
<p>这项研究已经在 Science 上发表。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210716/v2_07a9488c77574221b363065cbe7c8856_img_000" referrerpolicy="no-referrer"></p> 
<p>论文链接：https://science.sciencemag.org/content/early/2021/07/14/science.abj8754 </p> 
<p>华盛顿大学医学院团队也向社区开源了该工具，来自世界各地的科学家都可以使用它来构建蛋白质模型，加速自己的研究。在上传至 GitHub 后不久，该工具就已被 140 多个独立研究团队下载。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210716/v2_11fa196b17b74e019e320012a77f6349_img_000" referrerpolicy="no-referrer"></p> 
<p>项目地址 https://github.com/RosettaCommons/RoseTTAFold </p> 
<p>具体地，在这项研究中，华盛顿大学医学院生物化学系教授、蛋白质设计研究所所长 David Baker 领导的计算生物学家团队开发了一款叫做「RoseTTAFold」的软件工具，该工具利用深度学习技术，根据有限信息准确、快速地预测蛋白质结构，原本这一工作需要数年的实验室研究。 </p> 
<p>从结构上来看，RoseTTAFold 是一个 <strong>三轨（three-track）神经网络</strong> ，意味着它可以兼顾蛋白质序列的模式、氨基酸如何相互作用以及蛋白质可能的三维结构。在这种结构中，一维、二维、三维信息来回流动，使得网络能够集中推理蛋白质的化学部分与它的折叠结构。 </p> 
<p>下图 A 为具有 1D、2D 和 3D 注意力轨迹（attention track）的 RoseTTAFold 架构；B 为 CASP14 目标上蛋白质预测方法的平均 TM-score；C 为 CAMEO 中介（medium）和硬（hard）目标的盲基准测试结果。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210716/v2_dbe9f5df2ba244e7beaeb435e8c9327f_img_000" referrerpolicy="no-referrer"></p> 
<p>RoseTTAFold 方法的准确率<a class="project-link" data-id="81186" data-name="比目" data-logo="https://img.36krcdn.com/20200729/v2_2de30d2f5ca04d2e88544916251d2bc1_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/81186" target="_blank">比目</a>前可用的方法高得多，因而研究者想要测试 <strong>是否可以利用它解决以前未解决且具有挑战性的 MR 问题</strong> ，并改进临界个案的解决方案。四个最近的晶体数据集，包括牛属甘氨酸 N - 酰基转移酶（GLYAT）、细菌氧化还原酶以及细菌表面层蛋白（SLP）（下图 A）和来自真菌平革菌属金孢子菌属的分泌蛋白（下图 B），基于 PDB 蛋白质数据库中可用的模型无法利用 MR 解决，因此研究者使用 RoseTTAFold 模型进行了重新分析： </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210716/v2_4fbfaf05f3e24e26a015e1ae9c7403da_img_000" referrerpolicy="no-referrer"></p> 
<p>另一方面，RoseTTAFold 能够利用一台游戏计算机在短短 10 分钟内计算出蛋白质结构。研究者使用 RoseTTAFold 计算出<a class="project-link" data-id="4260438" data-name="了数" data-logo="https://img.36krcdn.com/20210422/v2_8e636ec7be434dd5bf7deebc8bed2b62_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/4260438" target="_blank">了数</a>百种新的蛋白质结构，其中包括许多人类基因组中认知甚少的蛋白质。此外，他们还生成了与人类健康直接相关的一些蛋白质结构，包括与有问题的脂质代谢、炎症和癌细胞生长相关的蛋白质。他们还表明，RoseTTAFold 可以用于建立复杂生物的模型，所需时间只是以前所需时间的一小部分。 </p> 
<p>下图为使用 RoseTTAFold 的蛋白质预测流程。其中，A 和 B 是从序列信息中预测大肠杆菌蛋白复合物的结构；C 表示由 RoseTTAFold 生成的 IL-12R/IL-12 复合结构符合以前发表的低温电子显微镜（cryo-EM）密度（EMD-21645）。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20210716/v2_1e69997eba7b4992af942afac5edbdaa_img_000" referrerpolicy="no-referrer"></p> 
<p>论文一作、华盛顿大学博士后研究员 Minkyung Baek 表示：「我们希望这个新工具将造福整个研究领域。」 </p> 
<p>参考链接： </p> 
<p>https://newsroom.uw.edu/news/accurate-protein-structure-prediction-now-accessible-all </p> 
<p>https://www.nature.com/articles/s41586-021-03819-2</p> 
<p>今天两大团队同时发布蛋白质预测成果，其中DeepMind如约公布了AlphaFold2的详细信息，另一团队的RoseTTaFold也基于同样的思想，取得了接近AlphaFold2的效果。 </p> 
<p>芝加哥丰田技术研究所的许锦波教授在接受外媒采访时表示，基于这些成果，业界可以展开更多的探索，尤其是复杂蛋白质结构的预测。</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号 <a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650821352&idx=1&sn=db286cbf8ede52d65be736e07332f00d&chksm=84e59696b3921f80991aea99766d3d2cfa780c1340a939a5484afdc6f5d8e0b5d4e1028f2478&scene=27#wechat_redirect">“机器之心”（ID：almosthuman2014）</a>，作者：Synced，36氪经授权发布。</p>  
</div>
            