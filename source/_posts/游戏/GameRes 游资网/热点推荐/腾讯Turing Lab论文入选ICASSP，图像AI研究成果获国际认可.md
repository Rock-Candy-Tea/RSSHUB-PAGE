
---
title: '腾讯Turing Lab论文入选ICASSP，图像AI研究成果获国际认可'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://www.gameres.com/undefined'
author: GameRes 游资网
comments: false
date: Mon, 06 Jun 2022 00:00:00 GMT
thumbnail: 'https://www.gameres.com/undefined'
---

<div>   
近日，全球顶级信号处理技术会议 ICASSP 2022 公布了论文入选名单。由王君乐博士带领的腾讯Turing Lab实验室论文——《针对手机游戏的主观与客观视频质量评价》（Subjective and Objective Quality Assessment of Mobile Gaming Video）、《引入用户共识学习的美学质量预测》（Considering User Agreement in Learning to Predict the Aesthetic Quality）被大会接收。<br>
<br>
ICASSP?(International Conference on Acoustics, Speech, and Signal Processing)是国际声学、语音和信号处理会议。是由IEEE主办的全世界最大的、也是最全面的信号处理及其应用方面的顶级学术会议，具有权威、广泛的学界及工业界影响力。历届ICASSP会议都备受AI领域研究学者的热议和关注。<br>
<br>
<div align="center">
<img aid="1041850" zoomfile="https://di.gameres.com/attachment/forum/202206/06/114427ebchphyyy93wv6vy.jpeg" data-original="https://di.gameres.com/attachment/forum/202206/06/114427ebchphyyy93wv6vy.jpeg" width="600" id="aimg_1041850" inpost="1" src="https://www.gameres.com/undefined" referrerpolicy="no-referrer">
</div><br>
此次，腾讯Turing Lab实验室在国际舞台全方位展示了腾讯在视频质量评价、图像质量评价方面的实力。<br>
<br>
以下为腾讯Turing Lab实验室入选论文概述：<br>
<br>
<strong><font color="#de5650">01.针对手机游戏的主观与客观视频质量评价</font></strong><br>
<br>
Subjective and Objective Quality Assessment of Mobile Gaming Video<br>
<br>
近年来，手机游戏在整个游戏市场中占据的份额已超50%，手游相关内容也成为社交媒体平台上短视频的重要组成部分。同时，基于视频流的云游戏也逐渐吸引了越来越多的用户。随着这些游戏相关的视频流媒体技术和服务的蓬勃发展，用户对游戏的质量体验(QoE, Quality of Experience)提出了更高的要求。只有对这个视频链路及内容表现进行更加严格的质量把控，才可以为用户带来更佳的游戏体验。<br>
<br>
画质作为质量体验QoE的重要维度之一，如何正确地预测人眼感知的画质在很长一段时间内一直是学术界及工业界研究的重点及热点。然而，目前大量的已有研究主要聚焦在传统的视频内容上，包括PGC内容、UGC内容、以及面向线上会议和共享屏幕等场景的特定内容等。当这些画质评价方法直接应用在游戏视频时，性能表现一般。<br>
<br>
因此，在本篇论文中，我们针对手机游戏在云游戏场景下的画质问题，进行了主观实验及客观算法模型研发的相关工作。我们先从腾讯先锋云游戏平台上选择17款手机游戏中，并针对不同场景收集了共150段源视频，之后使用多种编码器和编码参数构造出1293段视频。我们基于ITU相关标准进行严格的主观实验，从而得到了全新的针对手机游戏的视频质量评价数据集TGV dataset（Tencent Gaming Video dataset）。<br>
<br>
<div align="center">
<img aid="1041845" zoomfile="https://di.gameres.com/attachment/forum/202206/06/114426tao3fglzzegaf36d.jpg" data-original="https://di.gameres.com/attachment/forum/202206/06/114426tao3fglzzegaf36d.jpg" width="600" id="aimg_1041845" inpost="1" src="https://di.gameres.com/attachment/forum/202206/06/114426tao3fglzzegaf36d.jpg" referrerpolicy="no-referrer">
</div><br>
在这篇论文中，我们提出质量评价模型ERAQUE(Efficient hard-RAnk QUality Estimator)。结合新提出的困难样本排序损失（Hard Pairwise Ranking Loss， Fig1），该模型在训练过程中可以更加针对相似的样本对，从而学习到更细粒度的失真信息，进一步提升模型的性能。在提出的TGV数据集上，我们进行了模型训练和对比试验，实验结果表明ERAQUE模型相比业界其他质量评价模型表现出了更好的性能。<br>
<br>
<div align="center">
<img aid="1041846" zoomfile="https://di.gameres.com/attachment/forum/202206/06/114426sz6rgbfubz770d1u.jpg" data-original="https://di.gameres.com/attachment/forum/202206/06/114426sz6rgbfubz770d1u.jpg" width="600" id="aimg_1041846" inpost="1" src="https://di.gameres.com/attachment/forum/202206/06/114426sz6rgbfubz770d1u.jpg" referrerpolicy="no-referrer">
</div><br>
最后，为了让模型以在端侧更高效地推理，我们使用知识蒸馏的方案（Fig.2）对ERAQUE模型进行压缩和加速，最终实现ERAQUE模型的轻量化部署，实验结果表明ERAQUE模型配合提出的蒸馏策略可以使模型在复杂度和性能之间实现高度权衡。<br>
<br>
<strong><font color="#de5650">02. 引入用户共识学习的美学质量预测</font></strong><br>
<br>
Considering User Agreement in Learning to Predict the Aesthetic Quality<br>
<br>
近年来，针对图像的视觉美感评价技术在许多应用场景中发挥着重要作用，包括图像的自动化编辑、图像生成、以及在内容推荐领域等。因此，图像美学评价成为了学术界及工业界热门的研究课题。<br>
<br>
与传统的图像质量评价问题不同，由于人在进行美学评价时会引入更多high-level的评价维度，如情感、画面布局、色彩搭配与协调性等，这也使得美学评价相比针对失真进行的传统图像质量评价，具有更高的主观性与不确定性(见Figure 1)。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1041847" zoomfile="https://di.gameres.com/attachment/forum/202206/06/114426ky5fqy6080k8yqkb.jpg" data-original="https://di.gameres.com/attachment/forum/202206/06/114426ky5fqy6080k8yqkb.jpg" width="600" id="aimg_1041847" inpost="1" src="https://di.gameres.com/attachment/forum/202206/06/114426ky5fqy6080k8yqkb.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Figure 1：在这两幅图中，评测人员对于A图的美感评分具有更高的不确定性（标准差σ=1.36），而对于B图，评测人员对于美感的评分则趋于一致（标准差σ=0.59）</font></font></div><br>
在这篇论文中，我们提出了改良了的多任务attention网络（见Figure 2及Figure 3），可以对输入图像的美学MOS分数，以及代表了该分数不一致性的标准差进行端到端的预测。在损失函数方面，我们同时也提出了全新的针对的置信区间排序损失（confidence interval ranking loss）,用于促使模型在训练过程中更多地关注具有更高美学不确定性的图像对，从而学习到更具有区分性地特征，以及与观测者不确定性更相关的特征。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1041848" zoomfile="https://di.gameres.com/attachment/forum/202206/06/114426m8pmfexth5k7tf8t.jpg" data-original="https://di.gameres.com/attachment/forum/202206/06/114426m8pmfexth5k7tf8t.jpg" width="600" id="aimg_1041848" inpost="1" src="https://di.gameres.com/attachment/forum/202206/06/114426m8pmfexth5k7tf8t.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Figure 2: 文章所提出模型的总体架构</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1041849" zoomfile="https://di.gameres.com/attachment/forum/202206/06/114426cmzmmijkdmh5p7t2.jpg" data-original="https://di.gameres.com/attachment/forum/202206/06/114426cmzmmijkdmh5p7t2.jpg" width="600" id="aimg_1041849" inpost="1" src="https://di.gameres.com/attachment/forum/202206/06/114426cmzmmijkdmh5p7t2.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Figure 3: 文章所提出的LMLSP模块</font></font></div><br>
在这个工作中，我们通过大量的实验证明了我们所提出多任务学习美学模型不但在游戏图像的美学预测中具有巨大优势，同时对于传统的自然内容图像美学预测任务，也达到了很好的效果。<br>
<br>
<strong><font color="#de5650">产学研结合，落地业务，反哺技术</font></strong><br>
<br>
在业务层面，以上AI技术均已应用到腾讯先锋云游戏平台，腾讯先锋云游戏通过Turing Lab画质评价、多媒体视频质量评价、内容生成及虚实互动等能力，致力于全方位的提升云游戏画质表现，打造云游戏极致的用户体验。<br>
<br>
除了在C端业务的落地之外，在面向产业互联网层面，Turing Lab的视频质量评价技术也已经通过“腾讯WeTest质量云平台“对外开放，行业用户可以通过体验Demo快速体验了解到该技术。<br>
<br>
除此之外，在AI应用上的探索，腾讯WeTest官网近期全新上线了AI服务专区，并同步推出视频画质评价/游戏内容安全解决方案等产品能力。未来，腾讯WeTest将持续在科研领域深耕，并致力于将AI技术前沿研究与测试场景进行融合，用技术驱动测试乃至质量保障行业的发展，并以开放态度，对外输出优秀的技术能力，助力行业的发展。<br>
<br>
<strong><font color="#de5650">王君乐博士简介</font></strong><br>
<br>
腾讯专家研究员，Turning Lab负责人<br>
<br>
拥有10余年计算机视觉、多媒体、机器学习领域研究经验，在人体姿态估计与重建、图像质量评价、计算摄影学、沉浸式多媒体等领域有较深的了解及实战经验，并在这些领域带领团队进行探索与落地的工作。曾主导腾讯CenseoQoE画质评价方案的建设与社区开源，主导腾讯先锋云游戏云端虚实互动技术的研发。此外，在包括CVPR、NeurIPS、TIP、TMM等顶级会议及期刊上发表多篇论文，并为多个会议及期刊担任审稿人及组织者。<br>
<br>
  
</div>
            