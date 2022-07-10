
---
title: 'DeepNash AI 在军棋里对人类高玩的胜率84%'
categories: 
 - 图片
 - 煎蛋
 - 首页
headimg: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2018/09/7b50a4e1e7245c57fc5e29a982c96792.jpg!custom'
author: 煎蛋
comments: false
date: Sun, 10 Jul 2022 07:24:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2018/09/7b50a4e1e7245c57fc5e29a982c96792.jpg!custom'
---

<div>   
<blockquote><p>军棋和围棋象棋不一样，是信息不透明的游戏</p></blockquote><img src="https://cors.zfour.workers.dev/?http://img.jandan.net/news/2018/09/7b50a4e1e7245c57fc5e29a982c96792.jpg!custom" referrerpolicy="no-referrer"><p>军棋和围棋、象棋存在本质上的不同。军棋是一种信息不完全公开的博弈游戏。</p>
<p>西洋陆军棋Stratego和国内留下的陆军棋有微小的差别：棋子更多且没有快速通行的铁路。</p>
<p>最近几年，Stratego 一直被认为是人工智能最有前途的热点之一。 游戏有两个主要挑战。</p>
<p>1) Stratego 博弈树中有 10535 个潜在状态。 </p>
<p>2)本游戏中的每位玩家必须在游戏开始时考虑 1066 种可能的部署。由于游戏结构的各种复杂配置，人工智能研究社区在这方面取得的进展微乎其微。</p>
<p>AI领域的领航者DeepMind提出了 DeepNash——一种无需人类演示、以无模型(model-free)从零开始在不完美信息游戏 Stratego 中学习的Stratego自我博弈的智能体。DeepNask击败了以往的SOTA AI，并在最复杂的变体Stratego Classic中达到了专家级人类玩家的水平。</p>
<p>正则化纳什动力学 (R-NaD) 是一种有原则的、无模型的强化学习技术，是 DeepNash 的主要支柱。DeepNash通过将R-NaD与深度神经网络架构集成来实现ε-Nash平衡。纳什均衡确保即使面对最坏情况的对手，代理也能表现良好。</p>
<p>DeepNash 包含三个部分：基本训练组件 R-NaD、微调学习策略和测试时后处理。 R-NaD 取决于三个重要阶段：奖励转换、动态和更新。此外，DeepNash的R-NaD学习方法建立在收敛的正则化概念之上。</p>
<p>DeepNash 网络由四个头组成，每个头都是躯干的较小版本，并添加了最终层以及残差块和跳过连接。第一个 DeepNash 头将价值函数生成为标量，但其他三个头通过在游戏和部署期间开发概率分布来编码代理的策略。</p>
<p>DeepNash的动态阶段分为两部分。第一部分通过使v-trace 器适应两人不完全信息的情况来估计价值函数。第二阶段，利用基于 v-trace 估计器的状态动作值估计，通过神经复制器动力学 (NeuRD) 优化来学习策略。在训练期间通过对动作概率应用额外的阈值和离散化来进行微调。</p>
<p>DeepNash 在 2022 年 4 月上旬与顶级人类玩家进行了为期两周的测试，50 场排名赛，其中 DeepNash 获胜率为 42%。因此，它相当于 2022 年 Classic Stratego 挑战排名中的 1799 分，这使 DeepNash 在所有 Gravon Stratego 玩家中排名第三。历史上Classic Stratego 的评分为 1778，使 DeepNash 在所有 Gravon Stratego 玩家中排名第三。</p>
<p>在 Gravon 平台上，DeepNash 对抗其他 AI 的最低胜率为 97%，对抗人类专家玩家的总体胜率为 84%。 DeepNash 可以为强化学习方法开辟新的机会，以解决超出现有最先进AI能力范围的现实世界里(有天文数字状态空间)的不完全信息的多智能体问题。</p>
<p>论文：<a href="https://arxiv.org/pdf/2206.15378.pdf">https://arxiv.org/pdf/2206.15378.pdf</a></p>
<blockquote class="wp-embedded-content" data-secret="zwl2NyxkwQ"><p><a href="https://www.marktechpost.com/2022/07/09/deepmind-ai-researchers-introduce-deepnash-an-autonomous-agent-trained-with-model-free-multiagent-reinforcement-learning-that-learns-to-play-the-game-of-stratego-at-expert-level/">Deepmind AI Researchers Introduce ‘DeepNash’, An Autonomous Agent Trained With Model-Free Multiagent Reinforcement Learning That Learns To Play The Game Of Stratego At Expert Level</a></p></blockquote>
<p><iframe title="“Deepmind AI Researchers Introduce ‘DeepNash’, An Autonomous Agent Trained With Model-Free Multiagent Reinforcement Learning That Learns To Play The Game Of Stratego At Expert Level” — MarkTechPost" class="wp-embedded-content" sandbox="allow-scripts" security="restricted" style="position: absolute; clip: rect(1px, 1px, 1px, 1px);" src="https://www.marktechpost.com/2022/07/09/deepmind-ai-researchers-introduce-deepnash-an-autonomous-agent-trained-with-model-free-multiagent-reinforcement-learning-that-learns-to-play-the-game-of-stratego-at-expert-level/embed/#?secret=zPALuDYdbn#?secret=zwl2NyxkwQ" data-secret="zwl2NyxkwQ" width="500" height="282" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe></p>  
</div>
            