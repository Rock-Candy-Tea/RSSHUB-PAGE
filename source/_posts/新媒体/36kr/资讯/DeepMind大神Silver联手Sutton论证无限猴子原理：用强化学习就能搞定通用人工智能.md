
---
title: 'DeepMind大神Silver联手Sutton论证无限猴子原理：用强化学习就能搞定通用人工智能'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210611/v2_e5e6c96131154007aa812db2c2f665ed_img_000'
author: 36kr
comments: false
date: Fri, 11 Jun 2021 07:03:27 GMT
thumbnail: 'https://img.36krcdn.com/20210611/v2_e5e6c96131154007aa812db2c2f665ed_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/UaC5kqfvwsm6Cm1GV1OVlg">“新智元”（ID:AI_era）</a>，编辑：Emil 好困，36氪经授权发布。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_e5e6c96131154007aa812db2c2f665ed_img_000" data-img-size-val="1080,540" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>来源：sciencedirect</p> 
<blockquote> 
 <p>【导读】DeepMind最近研究了一下大自然，于是决定把「达尔文主义」应用在AI上面。首先给AI设定一个奖励，等AI学会如何把奖励做到最大化，它就是个出色的人工智能代理了。</p> 
</blockquote> 
<p>人工智能发展了这么久，终于产生了包括卷积，注意力，全连接等各种机制。</p> 
<p>有趣的是，最近的研究反而搞起了「这些机制我们都不需要」的创新。</p> 
<p>例如苹果发表的一篇论文表示Transformer不需要注意力机制。</p> 
<p>在这个方面，DeepMind也不甘落后，发表文章称「Reward is Enough」，其他都不需要。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_3aa188f7295940b58caf7839ce6fea19_img_000" data-img-size-val="900,140" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>https://www.sciencedirect.com/science/article/pii/S0004370221000862</p> 
<p>人工智能现在已经能够在有限的环境中有效地解决特定的问题，但它们还没有发展出在人类和动物身上看到的那种普遍的「智能」。</p> 
<p>DeepMind认为「智能」不是从制定和解决复杂问题中产生，而是通过坚持一个简单但强大的原则：奖励最大化。</p> 
<p>值得注意的是，发表这篇文章的是DeepMind强化学习领域的两位大神：David Silver（下图右）以及Richard Sutton（下图左）。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_ee04098afd6549938513a9a28874af72_img_000" data-img-size-val="1080,546" referrerpolicy="no-referrer"></p> 
<p>David Silver 是 DeepMind 首席科学家、伦敦大学学院计算机科学系教授，他是 AlphaGo 的设计研发主导<a class="project-link" data-id="3969467" data-name="人物" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969467" target="_blank">人物</a>。</p> 
<p>而Richard Sutton 是阿尔伯塔大学计算机系教授、DeepMind 杰出科学家，他被认为是现代计算的强化学习创立者之一。</p> 
<h2 label="一级标题" style>奖励最大化就能实现AGI？</h2> 
<p>通常认为，组合多个人工智能模块就可以产生更高的智能系统。例如，把独立的计算机视觉、语音处理、NLP和运动控制模块之间进行协调，从而去解决需要多种技能的复杂问题。</p> 
<p>而DeepMind的研究表示，你们搞这些自上而下的都是歪门邪道，奖励机制才是自然界中产生如此丰富的智能的原因：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>不同形式的智能源于不同环境中不同奖励信号的最大化。例如蝙蝠的回声定位或黑猩猩的工具使用等。</p></li> 
</ul> 
<ul class=" list-paddingleft-2"> 
 <li><p>这些能力的产生也都将服务于一个单一的目标，也就是在动物所处的环境中获得最大化的回报。</p></li> 
</ul> 
<p><img src="https://img.36krcdn.com/20210611/v2_16f288d9aa2a4cb08b2127391608b122_img_000" data-img-size-val="1080,589" referrerpolicy="no-referrer"></p> 
<p>例如，一只想要「活着」的松鼠，那么饥饿最小化这个奖励机制就可以认为是 「活着 」的一个子目标。</p> 
<p>于是，这只松鼠就产生了感知和运动的技能，从而帮助它在有食物的时候找到并收集坚果。</p> 
<p>但只能找到食物的松鼠在食物变少时就会饿死。因此又产生了计划和记忆的能力，这样松鼠就可以把坚果藏起来，等到冬天的时候再去找到这些坚果。同时，松鼠还需要产生关于社会的知识，从而避免其他动物去偷藏起来的坚果。</p> 
<p>论文表示，奖励最大化是足以驱动自然界的生物和强化学习代理产生「智能」的，包括知识、学习、感知、社会智能、语言、概括和模仿。</p> 
<p>因此，人工智能通过奖励最大化的强化学习之后，就可以成为今后在人工智能方面通用的解决方案。</p> 
<p>然而，这个例子依然没有解释为什么同样是最大化奖励，人类就能写出「人工智能」，而这只松鼠就不行？</p> 
<h2 label="一级标题" style>奖励最大化的强化学习方法</h2> 
<p>强化学习是AI算法的一个特殊分支，这套方法由三个关键要素组成：环境、代理以及奖励机制。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_64d450b9355c4c0da4cc5b3fa20a1dc0_img_000" data-img-size-val="738,274" referrerpolicy="no-referrer"></p> 
<p>在执行操作的过程中，代理会依据操作过程对于目标的影响程度来决定奖励或者惩罚，同时改变自己和环境状态。</p> 
<p>许多的强化学习产生的问题在于代理对于环境缺乏初始的认知，从而导致开始时的随机操作。根据反馈，代理学会调整其行为，并制定最大化奖励的策略。</p> 
<p>在论文中，DeepMind 的研究人员建议将强化学习作为主要算法，它可以通过学习在自然界中的奖励最大化方法，并最终带来通用人工智能。</p> 
<p>作者在论文中说，「如果一个代理能够连续调整它的行为来提升奖励，那么任何在这种环境下的重复性能力都可以通过代理这样的行为产生出来。」</p> 
<p>一个好的强化学习代理可以通过这样的方法学习感知、语言、社交能力等等。</p> 
<p>在论文中，研究人员提供了几个例子，展示了强化学习代理如何能够在游戏和机器人环境中学习一般技能。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_8354715ad6ba439ebedf492b23215bb6_img_000" data-img-size-val="800,450" referrerpolicy="no-referrer"></p> 
<p>不过研究人员同时强调，一些基本问题仍然有待解决，比如他们对于强化学习的样本执行效率缺乏理论依据。</p> 
<p>众所周知，强化学习需要给机器「喂」大量的数据，假如让电脑通过机器学习的方法来学会一个电脑游戏，它们可能需要几百年来学习……</p> 
<p>并且如何在更多的领域来创造一个强化学习系统对于研究者来说也是一个挑战，因为任何环境中微小的变化都需要对模型进行全面重新训练。</p> 
<p>同时，奖励最大化的学习机制是一个未解决的问题，仍然是强化学习中有待进一步研究的核心问题。</p> 
<h2 label="一级标题" style>奖励最大化的优点和缺点</h2> 
<p>加州大学圣地亚哥分校的神经科学家、哲学家和名誉教授帕特里夏·丘奇兰 (Patricia Churchland) 将论文中的想法描述为「非常仔细和有见地的解决方案」。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_fc778ed2c2fb4971badaa519d3de835b_img_000" data-img-size-val="1080,655" referrerpolicy="no-referrer"></p> 
<p>同时，丘奇兰也指出论文中关于社会决策讨论中可能存在的缺陷。DeepMind的研究人员专注于在社交过程中的个人收益。</p> 
<p>而丘奇兰在自己最近写的书中谈到，对于哺乳动物和鸟类而言，个体之间的亲情关系往往会对社会决策产生重大影响，比如动物会为了保护孩子而将自己置于危险中而不顾。</p> 
<p>当然，丘奇兰补充到，自己的观点对于论文中的假设并没有冲突，只是一个有益的补充。</p> 
<p>而数据科学家Herbert Roitblat 则对于这篇论文的立场提出了挑战，他认为通过简单的学习机制和试错经验足以培养机器智能的说法有些站不住脚。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_f5e4921ca04d41e8b35d37e037143eb9_img_000" data-img-size-val="1080,1620" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Herbert Roitblat 也是通用AI领域的专家</p> 
<p>如果没有时间限制，那么试错学习的方法可能可行，但是这个方法就像是无限猴子定理，即让一只猴子在打字机上随机按键，当按键时间达到无穷，它必然会打出任何给定的文字。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_248b9d1c667448308977e56d1c7511e3_img_000" data-img-size-val="320,180" referrerpolicy="no-referrer"></p> 
<p>「建立了模型和表述方式之后，优化或强化就可以指导其进化，但这并不意味着强化就足够了，」Roitblat 说。</p> 
<p>同样，Roitblat 补充说，该论文没有对如何定义强化学习的奖励、操作和其他元素提出任何建议。</p> 
<p>「强化学习的前提是代理有一组有限的潜在操作方式，同时奖励标准和价值函数也需要提前指定。换句话说，通用人工智能的问题恰恰是强化学习的先决条件。</p> 
<p>所以如果机器学习都能够简化成为最大化某种评估参数的形式，那么强化学习肯定是有意义的，但是它仍然缺乏说服力。」</p> 
<h2 label="一级标题" style>通用人工智能迎来新曙光？</h2> 
<p>DeepMind的研究人员在探讨通用人工智能的实现路径：即通过自下而上，而不是由人类先制定好顶层规划和结构的方法来实现特定的目标。</p> 
<p>通用人工智能指的是通用人工智能是一些人工智能研究的主要目标，也是科幻小说和未来研究中的共<a class="project-link" data-id="63783" data-name="同话" data-logo="https://img.36krcdn.com/20200729/v2_b44abdb43d36461883348c691c69f1bf_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/63783" target="_blank">同话</a>题。一些研究人员将通用人工智能称为强AI（strong AI）或者完全AI（full AI），或称机器具有执行通用智能行为（general intelligent action）的能力。与弱AI（weak AI）相比，强AI可以尝试执行全方位的人类认知能力。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_59c2ac2b144d40e892b9b4216f0cd293_img_000" data-img-size-val="500,205" referrerpolicy="no-referrer"></p> 
<p>关于人工智能的智力水平，与乔布斯共同创建苹果公司的天才沃兹尼亚克曾经提出一个咖啡测试：</p> 
<p>即让一台机器进入普通的美国家庭并弄清楚如何制作咖啡：找到咖啡机，找到咖啡，加水，找到杯子，然后通过按下适当的按钮来冲泡咖啡。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_934ad127ec5642528c0980839b108d45_img_000" data-img-size-val="1000,600" referrerpolicy="no-referrer"></p> 
<p>在当前AI发展的水平下，一台机器人能够做到制作咖啡并非难事：通过工程师的顶层设计，让它的感知系统学会分辨咖啡、咖啡机等物品，同时让决策和执行系统来实现制作咖啡的一系列操作。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_34923f3820fa4a5f8c7334132f7f972c_img_000" data-img-size-val="800,600" referrerpolicy="no-referrer"></p> 
<p>但是难点在于如何让一台「一无所知」的机器人自己在环境中学会制作咖啡。依据DeepMind研究人员的论文，通过为AI设立一个制作咖啡的目标，并设定好相应的奖励机制，通过不断的试错这台机器终将领悟制作咖啡的真谛。</p> 
<p>如果目标设定得好，它可能还会帮你做出一杯口味纯正的猫屎咖啡。</p> 
<p>此篇文章如今在reddit上也引发了爱好者们的热烈讨论。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_3e24f994bb8a4562987d8bfb1a5a668e_img_000" data-img-size-val="1080,274" referrerpolicy="no-referrer"></p> 
<p>「恐怕这些学者是在<a class="project-link" data-id="42698" data-name="象牙塔" data-logo="https://img.36krcdn.com/20200729/v2_987ef1fc9d7742bf8672a020063ae1aa_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/42698" target="_blank">象牙塔</a>里待的时间太久了，过度自信到了自恋的程度。」</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_3d66a2f704b74f18ba9b6df830d49fb2_img_000" data-img-size-val="1080,191" referrerpolicy="no-referrer"></p> 
<p>「假设我有无限资源和时间，成功地创造出来了AGI，那我会从这个过程中学到什么？这还是科学吗？」</p> 
<p>根据达尔文的自然选择理论，生物进化大概需要4亿年的时间，但是至今也没人能解释清楚6亿年前寒武纪地球上为什么会突然多了那么多新物种。</p> 
<p><img src="https://img.36krcdn.com/20210611/v2_5811a18e43894b14972b118c9cc2d5fc_img_000" data-img-size-val="900,504" referrerpolicy="no-referrer"></p> 
<p>或许在自然界中的进化，也远非我们想象中的那么简单。</p> 
<p>参考资料：</p> 
<p>https://venturebeat.com/2021/06/09/deepmind-says-reinforcement-learning-is-enough-to-reach-general-ai/</p> 
<p>https://www.reddit.com/r/MachineLearning/comments/nplhy3/r_reward_is_enough_david_silver_richard_sutton/</p>  
</div>
            