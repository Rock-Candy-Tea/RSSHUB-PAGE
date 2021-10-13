
---
title: '轮到卡牌游戏了：研究人员利用蒙特卡洛树形搜索算法教AI玩指环王卡牌'
categories: 
 - 图片
 - 煎蛋
 - 首页
headimg: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/03/32b1db99c0db99b5be9fa93bc6757d95.jpg!custom'
author: 煎蛋
comments: false
date: Mon, 11 Oct 2021 15:58:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/03/32b1db99c0db99b5be9fa93bc6757d95.jpg!custom'
---

<div>   
<blockquote><p>为什么不是炉石</p></blockquote><img src="https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/03/32b1db99c0db99b5be9fa93bc6757d95.jpg!custom" referrerpolicy="no-referrer"><p>华沙理工大学的研究人员最近着手开发一种基于蒙特卡洛树形搜索(MCTS)算法的技术，可以让AI玩《指环王》的(LotR)经典卡牌游戏。游戏由Fantasy Flight Games于2011年发行。MCTS算法是一种通用的启发式决策方法，通过玩一系列被称为 "playout" 的随机游戏，可以优化特定游戏或场景中的搜索解决方案空间。研究人员在最近一篇预发表在arXiv上的论文中介绍了他们的MCTS技术。</p>
<p>"我们是纸牌游戏LotR的爱好者，但我们发现没有人工智能可以玩这个游戏。"进行这项研究的两位研究人员Bartosz Sawicki和Konrad Godlewski告诉TechXplore。"尽管如此，我们发现树状搜索方法可应用在类似的卡牌游戏中，如《旅法师》或《炉石传说》。"</p>
<p>能够玩好LotR卡牌游戏的算法，还不存在的主要原因是，这样的方法具有很大的挑战性。事实上，LotR是一个合作性的纸牌游戏，包含巨大的可能解的空间，复杂的逻辑结构和随机事件。这些特质使得游戏的规则和策略非常难以通过单纯算法实现。</p>
<p>"2016年的围棋比赛是人类选手有机会胜过人工智能的最后时刻。"Sawicki和Godlewski解释说。"我们论文的目的是为LotR游戏实现一个MCTS代理。"</p>
<p>LotR卡牌游戏很难与其他奇幻和冒险卡牌游戏相提并论，如《昆特牌》和《炉石传说》。事实上，与其他游戏相比，LotR被设计为单人或团队冒险RPG来玩，而非与其他玩家竞争。此外，游戏中的决策过程非常复杂，因为玩法包括几个阶段，其中大部分取决于前一个阶段的结果。</p>
<p>尽管有这些挑战，Sawicki和Godlewiski还是开发出一种基于MCTS的方法。然后，他们在一个游戏模拟器上进行了一系列测试，评估了他们开发的技术。</p>
<p>"我们的MCTS代理取得了明显高于专家玩家的胜率。此外，通过向扩展策略集和MCTS添加知识，我们能够进一步提高该模型的整体效率。”</p>
<p>Sawicki和Godlewski最近的工作证明，有可能成功地结合不同的人工智能和计算技术来创建能够玩复杂和合作的多阶段游戏的AI。尽管如此，该团队发现，使用MCTS来处理这些复杂的游戏也会有很大的局限性。</p>
<p>"主要问题是MCTS将游戏逻辑与人工智能算法合并，所以你在构建游戏树时必须知道合法的动作。"Sawicki和Godlewski解释说。"然而，对于具有显著分支因素的游戏树的调试是一场噩梦。有很多情况下，程序运行顺利，但胜率为零，我们不得不手动检查整个树。"</p>
<p>这项最新研究可能会激发其它工具的开发，让AI接管复杂的、战略性的和多阶段的游戏。在他们目前和未来的研究中，Sawicki和Godlewski还想探索在LotR游戏中训练的深度强化学习(RL)的潜力和性能。</p>
<p>"我们目前的工作重点是使用RL方法来进一步提高人工智能代理在游戏中的表现。在这种情况下，给定一个游戏状态，神经网络会返回一个由环境(即游戏模拟器)执行的动作。这很棘手，因为行动的数量在不同的状态下是不同的，而网络只能有固定数量的输出。到目前为止，我们的结果是有希望的，我们将在即将发表的文章中解释我们是如何取得这些结果的。" </p>
<p>https://techxplore.com/news/2021-10-monte-carlo-tree-algorithms-lord.html</p>  
</div>
            