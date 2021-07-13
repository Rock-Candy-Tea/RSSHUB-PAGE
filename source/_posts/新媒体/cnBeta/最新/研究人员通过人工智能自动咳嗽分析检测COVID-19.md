
---
title: '研究人员通过人工智能自动咳嗽分析检测COVID-19'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0713/a8c9c5ac8b2c8c4.gif'
author: cnBeta
comments: false
date: Mon, 12 Jul 2021 23:56:03 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0713/a8c9c5ac8b2c8c4.gif'
---

<div>   
据外媒报道，COVID-19危机已经考验了全世界的医疗系统。获得针对COVID-19的疫苗已使情况日趋稳定。然而，人们不得不继续进行大规模人群新冠病毒核酸检测筛查，以发现阳性病例，从而打破可能的病毒传播链。因此，科学家必须研究新的技术，以减少诊断检测的时间和成本，从而以方便、有效和经济的方式大规模地进行检测。在Interspeech 2021国际大会的框架内，<strong>一个研究小组向利用声学诊断COVID-19（DiCOVA）挑战赛的咳嗽声轨提交了该系统。</strong>与他们的贡献有关的文章已被接受加入Interspeech科学计划。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0713/a8c9c5ac8b2c8c4.gif" alt="ezgif-1-f551b7b79404.gif" referrerpolicy="no-referrer"></p><p style="text-align: left;">这项研究由UPF视听系统工程校友、奥格斯堡大学（德国）研究员Adrià Mallol和Helena Cuesta领导，Emilia Gómez（欧盟委员会联合研究中心）参与，他们都是UPF信息和通信技术系（DTIC）音乐技术研究小组（MTG）的成员，以及奥格斯堡大学和伦敦帝国学院（英国）的研究员Björn Schuller。</p><p style="text-align: left;">以前基于人工智能的系统已被证明在检测咳嗽和打喷嚏以及识别呼吸道异常方面是有效的。人工智能还被用于精神健康领域，以识别抑郁症或创伤后应激障碍的患者。继数字健康方面的进展之后。“受这些研究的启发，并基于COVID-19引起的呼吸系统疾病，我们为自己设定了一个挑战，即调查人工智能技术是否能够通过自动咳嗽分析来检测与该病毒有关的疾病，”研究小组的成员Helena Cuesta解释说。</p><p style="text-align: left;">咳嗽信号在COVID-19检测呈阳性的患者中有所改变</p><p style="text-align: left;">在这篇论文中，作者研究了两种不同的神经网络架构，但有一个共同的结构：第一个区块处理输入的频谱图并提取一组嵌入式特征，第二个区块根据这些特征是对应于COVID-19检测阳性的病人还是健康病人进行分类。</p><p style="text-align: left;">"我们的模型使用频谱图，即音频信号的时间频率表示作为输入。"</p><p style="text-align:center"><a href="https://n.sinaimg.cn/tech/crawl/88/w1080h608/20201222/e452-kfnaptu9024468.jpg" target="_blank"><img src="https://n.sinaimg.cn/tech/crawl/88/w1080h608/20201222/e452-kfnaptu9024468.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">第一步是对输入数据进行预处理。一般来说，数据库的录音包含各种咳嗽，由沉默分开（我们咳嗽时的典型模式）。“为了只保留录音中包含相关信息的部分，即咳嗽，我们使用基于信号能量的声音活动检测器（SAD），” Cuesta解释说。在过滤了这些数据后，下一步是提取特征并随后对其进行分割。“我们的模型使用频谱图，即音频信号的时频表示法作为输入。”她补充说：“首先，我们计算数据库中每个录音的频谱图，然后将其分割成每个一秒钟的片段。”</p><p style="text-align: left;">患者的性别很重要</p><p style="text-align: left;">该项目一个有趣的贡献是研究不同版本的神经网络，以调查患者的性别是否是分析咳嗽时的一个考虑因素。“直觉上，当我们接触这项工作时，我们的一个假设是，男性和女性的咳嗽应该有不同的特征，因为他们的声道在大小和形状上有所不同，”作者评论说。</p><p style="text-align: left;">从频谱的角度来看，男性和女性产生的咳嗽不一定相等</p><p style="text-align: left;">从他们的工作所进行的实验来看，最显著的一个方面是，在作者评估的大多数情况下，包含患者性别信息的模型在预测中获得了更好的结果，这证实了一个假设，即从频谱的角度来看，男性产生的咳嗽和女性产生的咳嗽不一定相等。</p><p style="text-align: left;">咳嗽音轨 - DiCOVA挑战赛</p><p style="text-align: left;">DiCOVA挑战赛的组织者为参赛者提供了一个数据库（Coswara数据集），其中包含1040段1至15秒的人们咳嗽的音频记录。与录音一起，这个数据库提供了与每个录音相关的一系列元数据：COVID-19的阳性/阴性，个人的性别和国籍。“基于这些数据，我们已经开发并评估了两个不同的神经网络，利用一秒钟的音频，预测COVID-19的阳性或阴性，”作者指出。</p><p style="text-align: left;">尽管这项工作只是通过自动咳嗽分析检测COVID-19的第一种方法，但作者提出的实验提供了一些线索，可以在这项研究的下一步中进行跟踪。我们仍需了解咳嗽信号在COVID-19阳性患者中是如何改变的。因此，可以提取特征并设计特定的神经网络以提高模型的质量。</p>   
</div>
            