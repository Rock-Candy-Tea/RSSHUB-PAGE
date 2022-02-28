
---
title: '瑞士等离子体中心和DeepMind使用AI来控制等离子体 用于核聚变研究'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0228/1043ae00735cd18.jpg'
author: cnBeta
comments: false
date: Mon, 28 Feb 2022 00:27:40 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0228/1043ae00735cd18.jpg'
---

<div>   
瑞士洛桑联邦理工学院（EPFL）管理的瑞士等离子体中心（SPC）在等离子体物理学和等离子体控制方法方面拥有几十年的经验。DeepMind是一家在2014年被Google收购的科学发现公司，致力于 “解决智能问题，推动科学和人类发展”。<strong>他们共同开发了一种基于深度强化学习的新的等离子体磁控制方法，并在SPC的托卡马克研究设施TCV中首次将其应用于真实世界的等离子体。</strong>他们的研究刚刚发表在《<a href="https://www.nature.com/articles/s41586-021-04301-9" target="_self">自然</a>》杂志上。<br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2022/0228/1043ae00735cd18.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0228/1043ae00735cd18.jpg" alt="Plasma-Inside-TCV-Tokamak-777x437.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">托卡马克是用于进行核聚变研究的甜甜圈形状的设备，SPC是世界上少数几个拥有一个正在运行的研究中心之一。这些设备利用强大的磁场将等离子体限制在极高的温度下--数亿摄氏度，甚至比太阳核心还要热--以便在氢原子之间发生核聚变。核聚变释放的能量正在被研究用于发电。SPC的托卡马克装置的独特之处在于它允许各种等离子体配置，因此它被称为可变配置托卡马克（TCV）。这意味着科学家可以用它来研究限制和控制等离子体的新方法。一个等离子体的配置与它的形状和在设备中的位置有关。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0228/7ac1ccf876cb1c4.gif" alt="ezgif-5-17e3bf0ec8.gif" referrerpolicy="no-referrer"></p><p style="text-align: left;">托卡马克装置通过一系列磁线圈形成和维持等离子体，这些磁线圈的设置，特别是电压，必须得到仔细控制。否则，等离子体可能会与容器壁发生碰撞并恶化。为了防止这种情况发生，SPC的研究人员在TCV托卡马克中使用之前，首先在一个模拟器上测试他们的控制系统配置。“我们的模拟器是基于20多年的研究，并不断地更新，”SPC的科学家和该研究的共同作者Federico Felici说。“但即便如此，仍然需要长时间的计算来确定控制系统中每个变量的正确值。这就是我们与DeepMind的联合研究项目的意义所在。”</p><p style="text-align: left;">DeepMind的专家们开发了一种可以创建和维护特定等离子体配置的人工智能算法，并在SPC的模拟器上对其进行训练。这包括首先让该算法在模拟中尝试许多不同的控制策略，并收集经验。根据收集的经验，该算法产生了一个控制策略，以产生所要求的等离子体配置。这包括首先让该算法通过一些不同的设置运行，并分析每个设置所产生的等离子体配置。然后，该算法被要求以另一种方式工作--通过识别正确的设置来产生特定的等离子体配置。经过训练后，基于人工智能的系统能够创建并维持广泛的等离子体形状和高级配置，包括在容器中同时维持两个独立的等离子体。最后，研究小组在托卡马克上直接测试了他们的新系统，以了解它在真实世界条件下的表现。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2022/0228/e30a510a520590e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0228/e30a510a520590e.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">SPC与DeepMind的合作可以追溯到2018年，当时Felici在该公司伦敦总部的黑客马拉松大赛上第一次见到DeepMind的科学家。他在那里解释了他的研究小组的托卡马克磁控问题。“DeepMind立即对在核聚变等领域测试他们的人工智能技术的前景感兴趣，特别是在托卡马克这样的真实世界系统上，”Felici说。DeepMind的控制团队负责人、该研究的共同作者Martin Riedmiller补充说：“我们团队的任务是研究新一代的人工智能系统--闭环控制器--能够完全从头在复杂的动态环境中学习。在现实世界中控制核聚变等离子体提供了梦幻般的机会，尽管它极具挑战性和复杂性。”</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0228/8f2f579607bf7d8.gif" alt="ezgif-5-70310cd572.gif" referrerpolicy="no-referrer"></p><p style="text-align: left;">一次双赢的合作</p><p style="text-align: left;">在与Felici交谈后，DeepMind提出与SPC合作，为其托卡马克装置开发一个基于人工智能的控制系统。“我们立即同意了这个想法，因为我们看到了创新的巨大潜力，”SPC主任和该研究的共同作者Ambrogio Fasoli说。“所有与我们合作的DeepMind科学家都非常热情，对在控制系统中实施人工智能有很多了解。” Fasoli则对DeepMind在短时间内集中精力于某一项目所能做出的惊人之举印象深刻。</p><p style="text-align: left;">DeepMind也从这个联合研究项目中得到了很多，说明了采取多学科方法对双方的好处。DeepMind的高级研究工程师、该研究的共同作者Brendan Tracey说：“与SPC的合作推动了我们改进强化学习算法，并因此可以加速融合等离子体的研究。”</p><p style="text-align: left;">这个项目应该为EPFL寻求与外部组织的其他联合研发机会铺平道路。Fasoli说：“我们总是对创新的双赢合作持开放态度，在这种合作中我们可以分享想法和探索新的观点，从而加快技术发展的步伐。”</p>   
</div>
            