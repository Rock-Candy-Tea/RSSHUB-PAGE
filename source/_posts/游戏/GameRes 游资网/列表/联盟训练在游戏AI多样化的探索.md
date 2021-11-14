
---
title: '联盟训练在游戏AI多样化的探索'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202110/21/110955rrx6m6qq0xbvuv00.jpg'
author: GameRes 游资网
comments: false
date: Thu, 21 Oct 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202110/21/110955rrx6m6qq0xbvuv00.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2517111">
<strong><font color="#de5650">导语</font></strong><br><br>
在深度强化学习中，联盟训练通过引入主智能体的“陪练”，发现主智能体策略的缺点，帮助其得到更快的提升。本文通过对模型特征和模型池多样性的建模，并基于此提升联盟模型池的多样性，引导克制主智能体的多种策略并提升主智能体的强度；同时，模型池的多样性也可以作为训练目标，为游戏AI的线上应用提供更多选择。<br><br><strong><font color="#de5650">一、 背景介绍</font></strong><br><br>
随着DeepMind、OpenAI等AI实验室在《星际2》[1]、《Dota 2》[2] 视频游戏智能体研究上的突破，深度强化学习在近几年得到了广泛的关注。如何在玩家数据有限或缺失的条件下，训练出接近或超过真人顶尖水平玩家能力的AI，是当前深度强化学习的研究热点之一。在实际训练场景中，我们很难为智能体搭建一个复杂的环境来一步到位学习到人类顶尖水平的模型，这样对人力和计算资源会提出更高的要求。针对这个问题，人们提出了自对弈[3]（self-play）训练框架（如图1），如同“左右互搏术”一样，使AI在不断和自己以及历史模型对战中学习到更优的策略。<br><br><div align="center">
<img id="aimg_1016378" aid="1016378" zoomfile="https://di.gameres.com/attachment/forum/202110/21/110955rrx6m6qq0xbvuv00.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/110955rrx6m6qq0xbvuv00.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/110955rrx6m6qq0xbvuv00.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">[ 图1.自对弈（self-play）示意图 ]</font></font></div>
<br>
自对弈方式能产生复杂环境或复杂的对抗形式，来不断进化智能体的能力。但正所谓“天下武功，唯快不破”，即使再高的竞技水平，都有可能会被攻破。比如击败曾经TI8 Dota2世界冠军OG的OpenAI Five[2]，在线上和玩家对战的时候，尽管最终AI胜率到达了99%，有一小部分玩家抓住了OpenAI Five的弱点，利用了AI不善于应对分路推进和隐身单位的弱点[4]，连续战胜了AI[5]，如下图所示：<br><br><div align="center">
<img id="aimg_1016379" aid="1016379" zoomfile="https://di.gameres.com/attachment/forum/202110/21/110956s3vfzc1cce944c9r.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/110956s3vfzc1cce944c9r.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/110956s3vfzc1cce944c9r.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">[ 图2.OpenAI Five Arena AI失败对局 ]</font></font></div>
<br>
使用当前主流深度强化学习方法训练的模型，一旦产生，它的参数已经固定；从另外一个角度来说，也就是行为模式、打法基本都是固定的：在某个特定游戏场景下，智能体往往会收敛至一个"局部最优"策略。这个现象导致了人们可以根据历史对战，发现和总结AI的战术打法，并根据此来利用AI的弱点进行针对性对战。由于在自对弈训练过程中，会受到对手模型池丰富度的影响，很难覆盖到所有打法风格，那么就有可能在训练中很少出现上面提到的分路推进、隐身英雄针对敌方阵容弱点的训练场景。而目前的技术很难支持固定的AI模型在失败对局中继续学习，并弥补这些弱点。为了应对这种情况，我们就需要构建一个具备更加丰富的训练环境，使智能体充分应对随时变化的对手策略，并做出更加合理的决策。DeepMind在《星际2》智能体[1]中，首先提出联盟的训练方式：AlphaStar League。为了训练最终打榜的智能体（这里称之为"主智能体"），AlphaStar League中不仅仅是需要主智能体击败当前存在的对手，并希望能及时找到主智能体的瑕疵，来帮助主智能体发现自己的缺点，从而得到更快的提升。AlphaStar League通过不同对手建模和采样的方式，来引导主智能体的对手策略多样性，目的是增加主智能体的整体强度。在实际博弈场景中，可能存在多种打法风格会同时克制主智能体（如速推会被对线优势、防守强力的打法克制），也有不同战术体系的循环克制（如带线克制团战、Gank克制带线、团战克制Gank），基于此，我们也需要关注产生具有不同打法风格的模型池，并且进一步强化主智能体的鲁棒性。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1016380" aid="1016380" zoomfile="https://di.gameres.com/attachment/forum/202110/21/110959p6iwo47wcu6uo78m.gif" data-original="https://di.gameres.com/attachment/forum/202110/21/110959p6iwo47wcu6uo78m.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/110959p6iwo47wcu6uo78m.gif" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">[ 图3. 赛博朋克游戏场景 ]</font></font></div>
<br>
在实际游戏AI应用中，"多样性"不仅仅是作为模型生产的一个手段，同时也可以作为目的：不同线上玩家的对于AI的需求也是多样的。比如，打法偏向保守的玩家会希望AI对手不会特别激进，喜欢Gank击杀的玩家更希望AI队友可以配合自己完成Gank行为。又比如对于NPC AI，目前游戏内置NPC，很多都是固定的模版，或者固定的对话，比如上图在《赛博朋克2077》中，玩家在车堆中扔了个手雷，所有NPC都整齐的从车里下来，蹲地抱头[6]，影响了游戏体验。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1016381" aid="1016381" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111002a601hxh9s817sgi8.gif" data-original="https://di.gameres.com/attachment/forum/202110/21/111002a601hxh9s817sgi8.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111002a601hxh9s817sgi8.gif" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">[ 图4. 游戏捏脸，图片来自[7] ]</font></font></div>
<br>
为了增强游戏内AI的多样性和个性化，如上图所示，如同游戏中"捏脸"[7]应用一样，如果我们在训练时控制智能体的不同演化方向，并且根据玩家画像或玩家需求，或根据玩家和其他AI之间的交互行为，定制匹配和玩家进行游戏的个性化AI模型，对于提升玩家游戏体验是非常有价值的。<br><br>
本文从联盟训练出发，探索可行的游戏AI多样性度量、生产和利用方案，将从以下几点展开进行具体介绍：<br><br>
1.联盟训练介绍<br><br>
2.模型风格和模型池多样性度量<br><br>
3.联盟训练在AI多样化中的探索<br><br><strong><font color="#de5650">二、联盟训练介绍</font></strong><br><br><strong>2.1 联盟训练</strong><br><br>
联盟（League）训练的概念由DeepMind在AlphaStar中被提出并得到应用，它是在虚拟自我博弈（Fictitious Self-Play，简称FSP）基础上引入了一组不同功能的智能体，称之为"联盟"。实际上，"联盟"训练方式在竞技体育中已经得到了应用，比如，在国家队乒乓球训练中，都会选取一部分非核心球员，或具有特殊打法的球员，或者模仿国外某种对手的打法风格，作为陪练来锻炼主力队员适应各种打法的能力[8]。这些陪练队员可能在国际比赛中并不能够战胜所有的对手取得冠军，但是对于帮助主力队员及时发现自己的弱点并且进行打法上的调整和优化，是十分必要的。<br><br><div align="center">
<img id="aimg_1016382" aid="1016382" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111005atpbvd0f6dxfdx7g.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111005atpbvd0f6dxfdx7g.jpg" width="582" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111005atpbvd0f6dxfdx7g.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">[ 图5. AlphaStar League ]</font></font></div>
<br>
如上图所示，AlphaStar使用了一个全自动的联盟训练框架，联盟一共包含三类智能体，分别是Main Agent、Main Exploiter和League Exploiter，从名字上来看，可以分别理解为是主力选手、开发主力选手弱点的陪练和开发整个联盟选手弱点的陪练，在AlphaStar中，使用了不同的对手采样方式，来训练这三类智能体：<br><br>
Main Agent：Main Agent主要使用了PFSP（Prioritized Fictitious Self-Play）方法，在每一轮次训练开始前，通过当前智能体和联盟的模型池进行评估对战，根据胜率战胜P[A战胜B]，从联盟历史模型池中增加更加匹配的对手的概率
<img id="aimg_1016383" aid="1016383" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111008ezsnd1hhas1drnzv.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111008ezsnd1hhas1drnzv.jpg" width="105" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111008ezsnd1hhas1drnzv.jpg" referrerpolicy="no-referrer">
，作为下一轮次训练的对手模型分布集合，其中
<img id="aimg_1016384" aid="1016384" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111011sfe4zka6jnek400n.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111011sfe4zka6jnek400n.jpg" width="124" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111011sfe4zka6jnek400n.jpg" referrerpolicy="no-referrer">
是权重函数，使用
<img id="aimg_1016385" aid="1016385" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111014q6dyn0wgnqq6gzz0.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111014q6dyn0wgnqq6gzz0.jpg" width="133" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111014q6dyn0wgnqq6gzz0.jpg" referrerpolicy="no-referrer">
时较难对手采样概率会更高，或使用
<img id="aimg_1016386" aid="1016386" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111017bfd8zdqqq21decdq.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111017bfd8zdqqq21decdq.jpg" width="130" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111017bfd8zdqqq21decdq.jpg" referrerpolicy="no-referrer">
时会倾向于选择更匹配的对手（胜率接近50%） ；在AlphaStar中，Main Agent使用了混合策略的形式采样对手模型，其中35%概率使用传统Self-Play自对弈方式按照一定概率分布选择Main Agent历史模型，50%使用PFSP方法从联盟模型池中进行采样，另外15%从已经淘汰的历史对手中进行随机挑选（即Main Agent对战这些智能体胜率已经达到100%）。<br><br>
Main Exploiter：Main Exploiter训练时主要对战当前版本Main Agent，目的是发现Main Agent策略的弱点，产生的模型作为Main Agent的对手加入至其训练对手中。<br><br>
League Exploiter：使用PFSP方法从整个联盟模型池中选择对手和对手概率分布，目的是发现整个联盟策略的弱点，产生的模型也作为Main Agent的对手加入至其训练流程中。<br><br>
AlphaStar联盟首先使用监督学习方式，利用人类玩家数据进行三类智能体的模型进行初始化，然后同时开始训练。对于每一个智能体，会进行一个"训练轮次"的迭代，即在开始训练时都会进行初始化，根据当前模型的对应策略，选择智能体的加载模型，以及对手模型分布；在到达训练轮次的结束条件（通常是高于一定训练胜率或超过一定训练步长）后结束这一轮次，并进行下一轮次的迭代。为了提升模型池的丰富程度，发现模型池中没有探索到的"盲区"，对于Main Exploiter和League Exploiter，都会以一定概率从人类样本训练得到的监督学习模型初始化，进行下一轮训练；而Main Agent不需要进行重新初始化。<br><br><div align="center">
<img id="aimg_1016387" aid="1016387" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111020qseysim1xj1dgxmd.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111020qseysim1xj1dgxmd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111020qseysim1xj1dgxmd.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">[ 图6. AlphaStar训练各阶段模型强度变化 ]</font></font></div>
<br>
如上图所示，引入了联盟训练的方式，AlphaStar模型在能力上得到了进一步的提升，达到了职业玩家的水平。<br><br>
联盟训练近几年在业界得到了应用和优化，TEG Robtics X和AI平台部提出了TStarBot-X训练结构[9]，对联盟中的Exploiter进行优化改造，如仅使用胜负奖励和策略蒸馏的方式来训练某个特定策略智能体的Specific Exploiter、从历史版本模型中探索发现最新Main Agent弱点的Evolutionary Exploiter等。在启元世界星际2打败职业玩家的联盟训练[10]中，同时也使用了多个主智能体，并通过Agent Branching方式来增加联盟的策略多样性。<br><br><strong>2.2 基于Avatar分布式强化学习平台的联盟训练框架</strong><br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1016388" aid="1016388" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111023f5qv5vttuzq7qoto.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111023f5qv5vttuzq7qoto.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111023f5qv5vttuzq7qoto.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">[ 图7. 基于Avatar平台的联盟训练框架 ]</font></font></div>
<br>
我们基于 Avatar分布式强化学习平台 搭建了一套全自动联盟训练框架，如图7所示。联盟中每一个智能体使用Avatar分布式框架和游戏环境交互和训练、评估。联盟是基于群体的训练方式，必然存在信息共享、中央控制的需求，因此在此基础上我们使用了一个中央协调器"Coordinator"来管理每一个训练或评估任务的参数。联盟框架包括Coordinator和Worker两个主要模块：<br><br>
Coordinator：联盟的中央协调器，主要负责任务及其参数的分配、联盟模型池的管理、训练和评估数据的管理，它主要包含以下几个部分：<br><br>
Coordinator：联盟的中央协调器，主要负责任务及其参数的分配、联盟模型池的管理、训练和评估数据的管理，它主要包含以下几个部分：<br><br>
共享模型池：管理和维护联盟的所有智能体持续产生的模型，这些模型参数固定，每一个模型都会标示它所属的Worker、模型ID、各项评估指标等信息；<br><br>
训练和评估数据管理：提供不同智能体对应训练任务、评估任务和模型天梯的查询接口；<br><br>
模型匹配策略：基于智能体的匹配策略、模型池和训练评估结果数据，对当前请求新任务的训练Worker匹配训练模型、对手模型和分布以及训练各组件的参数。<br><br>
Worker：管理并监控联盟中每个智能体在Avatar强化学习平台上的训练或评估任务，主要包括：<br><br>
训练Worker：接收到Coordinator训练任务后，进行训练任务的自动执行，包括启动、停止、更新并监控当前的训练任务，每一训练轮次结束后，会通知Coordinator添加模型并请求下一轮次的训练任务；<br><br>
评估Worker：接收到Coordinator待评估的对战模型列表后，进行评估任务的自动执行，包括启动、停止和监控当前评估任务，评估任务结束后，会通知Coordinator并进行下一批次的对战模型评估。<br><br>
在联盟中，每一个训练Worker都对应训练一个单独的智能体（如Main Exploiter）。开始训练时，会向Coordinator请求训练任务，Coordinator接收到请求后，会根据当前Worker的匹配策略和参数，模型池中模型的采样比例、采样规则等，计算出当前任务的各项参数，返回给Worker，Worker启动并完成当前分配的任务，上报给Coordinator，并继续下一轮的任务请求；同时随着模型池的数量增长，Coordinator会不断产生新的待评估模型，评估Worker在每一次评估任务完成后，会继续请求新生成的评估列表，进行评估和数据上报。<br><br>
联盟框架实质上是训练和评估任务分配和调度的平台，目前也支持了其他常见形式的自动化训练方式，如自对弈、PBT（Population-based Training）和自定义的混合策略，引导出满足不同应用场景需求的智能体。第四章中我们也会继续介绍联盟训练框架在AI多样性中的尝试。<br><br><strong><font color="#de5650">三、模型风格和多样性建模</font></strong><br><br>
为了引导多样化AI模型，首先要对"多样性"的概念进行定义。对于多人玩家PvP游戏而言，不同类型的阵容搭配可以算做多样性，不同打法风格也算是多样性。本文主要分析个体（如玩家、模型）的打法风格来度量模型池的多样性，而阵容搭配的多样性暂时不在本文的讨论范围内。<br><br>
从模型角度来出发，首先就需要提取模型的特征，通常使用1D的特征向量进行表示，基于这个向量，可以使用统计方法度量模型池中模型之间的距离，以及整个模型池的空间大小。如何提取有效可靠的策略特征，并且度量整个模型池的多样性，是本章需要讨论和解决的两大问题。<br><br><strong>3.1 模型特征提取</strong><br><br>
这里定义模型的特征为模型策略 θi 的表征，写作ϕ(θi)，其中
<img id="aimg_1016389" aid="1016389" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111026ojjglv501n6kj909.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111026ojjglv501n6kj909.jpg" width="76" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111026ojjglv501n6kj909.jpg" referrerpolicy="no-referrer">
为特征提取模块。简单来说，就是将模型的策略映射为一个长度为
<img id="aimg_1016390" aid="1016390" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111029wmm4344mew84ij9o.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111029wmm4344mew84ij9o.jpg" width="12" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111029wmm4344mew84ij9o.jpg" referrerpolicy="no-referrer">
的向量。<br><br><strong>无监督方法</strong><br><br>
提取游戏的智能体AI模型的特征有很多方法，首先想到的就是拿比赛结算信息，如比赛结束时游戏时间、胜负、金钱、装备信息作为模型的特征，这些数据能部分反应智能体AI的一些偏好，但这些数据往往无法捕捉游戏局内细节，很难还原AI在游戏内的具体策略，比如是更加激进还是偏向防守。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1016391" aid="1016391" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111032wyaamanbeznsjit6.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111032wyaamanbeznsjit6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111032wyaamanbeznsjit6.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">[ 图8. AI局内特征可视化 ]</font></font></div>
<br>
为了捕捉局内细节变化，较多方法使用局内动作或状态进行特征降维分析和差异比较，如DeepMind FTW Agent[11]对模型进行可视化时将局内状态特征采用t-SNE Embedding方法，来观察局内状态的转变，从而分析比较模型的打法风格。根据此也可以做特征降维、pooling等方法将局内特征聚合成模型特征。<br><br><strong>监督学习方法</strong><br><br><div align="center">
<img id="aimg_1016392" aid="1016392" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111035ps6dssjdnsjdccgd.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111035ps6dssjdnsjdccgd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111035ps6dssjdnsjdccgd.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">[ 图9. 通过监督学习方法预测模型语义特征 ]</font></font></div>
<br>
通过状态或者结算信息来表示模型特征的方法缺少一定的可解释性，而在一些游戏Bot AI的应用中，我们更希望能对智能体某方面行为能力进行刻画，比如模型特点属于激进或是保守，偏向个人发育还是团队利益，根据不同的应用场合，来选择使用不同的模型。一种比较通用的做法是手动给不同的模型或玩家打上标签，然后使用监督学习的方式训练一个预测网络，预测每个模型各维度的特点。这种方式依赖于标注的数据量和准确度，并且会产生一定的标注成本。<br><br><strong>基于难度评估方法</strong><br><br><div align="center">
<img id="aimg_1016393" aid="1016393" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111038r79n5ec7l4sn5y5c.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111038r79n5ec7l4sn5y5c.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111038r79n5ec7l4sn5y5c.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">[ 图10. 通过难度评估方法评估模型打法强度 ]</font></font></div>
<br>
在零和游戏中，能力的强弱是相对的，没办法通过"场均击杀10次"这样的数据来判断某个玩家或者模型在击杀能力上是强是弱。如何度量玩家或模型的能力，首先想到的根据特定指标的平均值进行评价，如胜率、击杀数、伤害值。但是由于游戏的匹配机制，玩家通常是和相同水平段位的其他玩家进行匹配，随着环境的不断变化，这些指标的参考意义就不是特别大。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1016394" aid="1016394" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111039b8vmbxubuffxfmzv.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111039b8vmbxubuffxfmzv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111039b8vmbxubuffxfmzv.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">[ 图11. “战斗强度”模型天梯 ]</font></font></div>
<br>
在业界比较常用的是Elo[12]或TrueSkill[13]等级分，来度量玩家的能力值。比赛完成时会根据己方等级分、对手等级分以及胜、负、平的关系，对己方和对手的等级分进行更新；同样道理，等级分也可以用来定义某个方面的能力强度。例如比较"击杀能力"，需要定义在"击杀能力"标准下的"胜、负、平"关系，如"我方击杀数-敌方击杀数>5"算作获胜，"我方击杀数-敌方击杀数<-5"算作失败，其他情况为平，那么对局后也可以更新对应"击杀能力"的等级分。最终得到的是具有语义性质的分数集合，并且建立模型天梯，不同等级分的高低，代表了该模型在这个打法风格维度上的强弱。<br><br><div align="center">
<img id="aimg_1016395" aid="1016395" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111040loze48s811go11re.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111040loze48s811go11re.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111040loze48s811go11re.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">[ 图12. CSGO能力分解，来自知乎[14] ]</font></font></div>
<br>
不同的游戏环境可以通过不同维度的能力，来刻画某个玩家或者模型的能力特征。如射击类游戏CSGO[14]，如图12所示，我们可以通过枪法、配合能力、残局能力、道具使用时机等不同维度数据来分析各种能力的强弱，同时也可以较为准确分析出模型或玩家的问题和漏洞出现在哪儿。<br><br>
综合考虑，基于难度评估方式能更直接反映模型当前各个维度的强弱，便于后续在训练中对模型行为进行刻画和理解，也可以在线上应用中准确挑选不同风格的AI模型，因此在下文中我们使用各维度的难度评估结果作为模型的特征表示。<br><br><strong>3.2 模型池多样性度量</strong><br><br>
模型池是模型的集合，代表了模型的群体，度量模型池的多样性，也就是整个群体的丰富程度。深度强化学习模型池的多样性度量也成为学术界近几年的研究方向之一，如[15][16]。那么如何量化模型池的多样性呢？首先就是要定义两个模型的特征向量
<img id="aimg_1016396" aid="1016396" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111040y596ytqzzmt5575m.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111040y596ytqzzmt5575m.jpg" width="19" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111040y596ytqzzmt5575m.jpg" referrerpolicy="no-referrer">
和
<img id="aimg_1016397" aid="1016397" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111040m7u1070sd2hjc60d.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111040m7u1070sd2hjc60d.jpg" width="20" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111040m7u1070sd2hjc60d.jpg" referrerpolicy="no-referrer">
之间的相似性。我们考虑核函数
<img id="aimg_1016398" aid="1016398" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111040v1j6osbrr0cozzrx.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111040v1j6osbrr0cozzrx.jpg" width="11" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111040v1j6osbrr0cozzrx.jpg" referrerpolicy="no-referrer">
，其中对于任意的
<img id="aimg_1016399" aid="1016399" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111041a7bpcc7c1m8c3dbp.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111041a7bpcc7c1m8c3dbp.jpg" width="19" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111041a7bpcc7c1m8c3dbp.jpg" referrerpolicy="no-referrer">
,
<img id="aimg_1016400" aid="1016400" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111041s47c2e3qxzq2vyq3.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111041s47c2e3qxzq2vyq3.jpg" width="20" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111041s47c2e3qxzq2vyq3.jpg" referrerpolicy="no-referrer">
都有
<img id="aimg_1016401" aid="1016401" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111041pzxtdkdollcx94cl.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111041pzxtdkdollcx94cl.jpg" width="94" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111041pzxtdkdollcx94cl.jpg" referrerpolicy="no-referrer">
。一种常用的核函数是平方指数（Squared Exponential）核：<br><br><div align="center">
<img id="aimg_1016402" aid="1016402" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111041zb7y76nya07cwscc.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111041zb7y76nya07cwscc.jpg" width="219" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111041zb7y76nya07cwscc.jpg" referrerpolicy="no-referrer">
</div>
<br>
根据上述公式，模型特征之间的距离越小，这两个向量之间就越相似，也就是两个模型越相似。<br><br><strong>模型池多样性度量</strong><br><br>
特征间相似度的度量仅仅是度量两个模型之间相似性，模型池作为一个群体，可能存在成百上千的模型，我们更需要通过一个指标描述整个群体的丰富程度。直观上来说，模型池的策略之间相似度越低，那么整个模型池的多样性也就越高。我们用一个定义在模型池集合的相似度度量矩阵上的函数f(K)∈R，其中K是相似度矩阵，比如使用平方指数核进行模型两两之间相似度的计算：
<img id="aimg_1016403" aid="1016403" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111041hb6k06ziqm60a0c0.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111041hb6k06ziqm60a0c0.jpg" width="186" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111041hb6k06ziqm60a0c0.jpg" referrerpolicy="no-referrer">
，输出是度量模型池多样性的一个标量，那么什么函数可以满足多样性的要求呢？<br><br>
一个比较合适的选择是矩阵 K的行列式[17] det(K)，矩阵可以看作是一组向量的集合，而矩阵的行列式的几何意义，就是各个向量张成的平行多面体的体积S：<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1016404" aid="1016404" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111042btqrrmgdkligzz8i.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111042btqrrmgdkligzz8i.jpg" width="252" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111042btqrrmgdkligzz8i.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">[ 图13. 行列式几何解释 ]</font></font></div>
<br>
也就是说，向量之间越不相似，它们之间的夹角就会越大，所张成的多面体的体积也就会越大，矩阵的行列式也就越大，所对应的模型集合的多样性也就越高。<br><br>
参考论文[15]，给定模型池策略特征集合 Θ=&#123;θ1,θ2,...,θM&#125;，通过平方指数核矩阵可以定义整个种群多样性：
<img id="aimg_1016405" aid="1016405" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111042o5dyhd5xnd53nd7d.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111042o5dyhd5xnd53nd7d.jpg" width="126" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111042o5dyhd5xnd53nd7d.jpg" referrerpolicy="no-referrer">
。<br><br>
这个多样性的定义，使用了行列式点过程[18]方法（Determinantal Point Processes，DPP），DPP方法最早在热力学中提出，在2018年被应用到提升推荐系统的多样性上[19]，取得了不错的效果，其中推荐给用户的列表就是选择最大后验概率（Maximum a posteriori，MAP）时的商品子集。同样地，模型池的多样性度量，也可以通过选取最大化多样性的模型子集的多样性来表示：<br><br><div align="center">
<img id="aimg_1016406" aid="1016406" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111045ma7b7sgemo54zat5.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111045ma7b7sgemo54zat5.jpg" width="207" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111045ma7b7sgemo54zat5.jpg" referrerpolicy="no-referrer">
</div>
<br>
明确了模型的特征表示和模型池的多样性的定义，本文在下一章节会探索AI模型多样性在联盟训练中的作用。<br><br><strong><font color="#de5650">四、联盟训练在AI多样化的探索</font></strong><br><br>
上文曾经提到，多样性不仅仅是训练的手段，也是目的。本章通过联盟训练的方式，尝试引导产生不同打法风格的模型，与此同时，利用这些模型，进一步发现主智能体的策略"盲区"，提升主智能体的能力。<br><br><strong>4.1 训练目标</strong><br><br>
根据联盟的设定，联盟中智能体训练的目标主要分为以下几类：<br><br>
对于Main Agent，不断提升模型能力；<br><br>
对于Main Exploiter，目标是探索克制Main Agent的打法风格，从而提升对战Main Agent的胜率，并且丰富模型池的多样性；<br><br>
对于League Exploiter，目标是提升对战联盟模型池的整体胜率，并且丰富模型池的多样性。<br><br>
我们将根据上述目标转换为每类智能体选择的最佳策略：<br><br><div align="center">
<img id="aimg_1016407" aid="1016407" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111048s22ttad2h8hchaaa.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111048s22ttad2h8hchaaa.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111048s22ttad2h8hchaaa.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1016408" aid="1016408" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111051q33bz0jj36wd550e.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111051q33bz0jj36wd550e.jpg" width="495" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111051q33bz0jj36wd550e.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1016409" aid="1016409" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111054lxsl1l9uxctzz5gw.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111054lxsl1l9uxctzz5gw.jpg" width="501" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111054lxsl1l9uxctzz5gw.jpg" referrerpolicy="no-referrer">
</div>
<br>
其中 Elo(π) 表示策略 π 的Elo等级分，表示该策略的整体强弱；Win(π,Πpool) 表示策略对战某个特定模型池模型的胜率情况，Div(Θ∪θ(π)) 表示模型池 Θ 加入当前策略π 后的多样性。通过修改目标函数，也可以为每一个Exploiter智能体选择特定的策略优化方向（比如偏向激进、分路推进策略），并且使用不同的初始化模型、奖励配置进行引导训练，以引导出特定打法风格的智能体。<br><br><strong>4.2 使用PBT（Population-Based Training）方法进行联盟多样化训练</strong><br><br>
强化学习的训练目标时寻找一个策略，从而最大化期望累计奖励
<img id="aimg_1016410" aid="1016410" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111057tcyi8g01kbqgbiid.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111057tcyi8g01kbqgbiid.jpg" width="94" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111057tcyi8g01kbqgbiid.jpg" referrerpolicy="no-referrer">
。由于视频游戏环境的复杂性，使用稀疏的结果奖励会导致学习效率非常低，因此通常会根据每个时间t的游戏信号或事件ρt，设置相对稠密的奖励信号 rt=w(ρt) ，来引导智能体更快进行学习。在训练过程中，每个智能体会根据当前的匹配策略，选择对手并且使用强化学习算法最大期望累计奖励。但是奖励并不代表智能体的最终训练结果和表现，也不会对群体的多样性产生影响，那么我们就需要通过群体优化的方式，来使得每种类型的智能体朝着目标方向进行演化。<br><br>
在使用强化学习对个体进行训练的基础上，我们引入了“元优化”（Meta-optimization）[11] 的思想，对不同智能体群进行分别优化，从而达到我们期望的目标：<br><br><div align="center">
<img id="aimg_1016411" aid="1016411" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111100j3cjmcy3qcj2dcld.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111100j3cjmcy3qcj2dcld.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111100j3cjmcy3qcj2dcld.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">[ 图14. 基于群体的联盟训练方法 ]</font></font></div>
<br>
这里我们使用了PBT[20]（Population-based Training）方法来训练联盟中的各智能体，来实现多目标优化问题，它分为“探索”和“利用”2个步骤：<br><br>
探索：每一轮训练，每个智能体会对不同的参数组合进行“探索”，在本文中参数主要关注不同的奖励配置，探索有几种形式：或基于上一轮最佳训练模型的奖励配置进行随机扰动，或从某个给定随机种子奖励配置进行初始化，同时并行启动N组实验，称为“Trial”。<br><br>
利用：根据4.1的不同智能体优化目标的定义，每一轮训练结束后，我们对相同智能体训练任务的N个Trial进行分别评估，并根据优化目标计算归一化得分。我们会“利用”得分最高的模型和参数配置，作为最优模型和配置，进行下一轮任务的迭代，据此不断演化出更容易达到特定智能体目标的参数配置。<br><br><strong>4.3 实验结果</strong><br><br>
下面从联盟的强度、演化过程以及多样性角度，来分析联盟训练与AI多样化之间的影响。<br><br><strong>主智能体强度</strong><br><br><div align="center">
<img id="aimg_1016412" aid="1016412" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111103gnrj01hqerijnxsg.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111103gnrj01hqerijnxsg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111103gnrj01hqerijnxsg.jpg" referrerpolicy="no-referrer">
</div>
<br>
首先看主智能体强度，如上表所示。相比于游戏内置最高等级AI（行为树实现），使用深度强化学习和自对弈（self-play）训练方式对Elo分提升超过1100分。在此基础上，联盟训练通过Exploiter发现主智能体的策略弱点，进一步提升其强度；使用Population-based方法，以目的为导向，演化出更加适合主智能体的奖励配置和对手打法，其Elo分已经达到1362分，并依旧在缓慢提升。<br><br><strong>联盟智能体</strong><br><br><div align="center">
<img id="aimg_1016413" aid="1016413" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111106t6693zmx5xb34amj.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111106t6693zmx5xb34amj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111106t6693zmx5xb34amj.jpg" referrerpolicy="no-referrer">
</div>
<br>
联盟中不同的智能体由于优化目标不同，达到的模型强度也是不同的。相比联盟中的其他智能体，Main Agent以最终强度为优化目标，演化出的智能体达到了最高的等级分；League Exploiter训练对手是联盟模型池中的所有模型，也具有一定强度；而Main Exploiter训练的目标就是为了克制Main Agent，本身模型强度并不会达到较高水平：这个结论和我们的认知也是比较一致的。<br><br><strong>奖励演化趋势</strong><br><br><div align="center">
<img id="aimg_1016414" aid="1016414" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111109ciuz9fa6earefgip.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111109ciuz9fa6earefgip.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111109ciuz9fa6earefgip.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">[ 图15. 联盟的各智能体奖励演化过程 ]</font></font></div>
<br>
由于训练目标的差异，不同智能体参数的演化方向是存在区别的。如图15所示，主智能体以最终结果为导向，Result相关的奖励权重随着训练进程不断提升；而其他Exploiter的奖励配置的演化也呈现出不同方向，可以初步看出，不同目的导向的智能体，它们的最优奖励是有所区别的。<br><br><strong>模型池多样性分析</strong><br><br><div align="center">
<img id="aimg_1016415" aid="1016415" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111112b4v4poi1pphvjh29.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111112b4v4poi1pphvjh29.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111112b4v4poi1pphvjh29.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">[ 图16. 模型池雷达图随训练轮次的变化 ]</font></font></div>
<br>
随着训练的进行，模型池的多样性也在不断提升。我们将模型策略分成10个维度进行表示，分别为模型整体强度、战斗强度、对线强度等，如上图所示，可以看到，由于初始化模型相同，刚开始训练时（第1轮），所有模型的分布都比较接近；随着训练迭代的进行，不同智能体朝着不同的方向进行演化，每个模型的雷达图的差异也开始逐渐增大。<br><br><strong><font color="#de5650">五、总结和展望</font></strong><br><br>
本文在AlphaStar League基础上，探索了模型池多样化的评估和训练方法，同时模型池的多样性也提升了主策略的强度。基于联盟和AI多样性训练的方式，本文仅做了初步的尝试和验证，行为策略的多样性是游戏之所以吸引不同玩家的一个原因之一，因此对于游戏内AI模型的多样性和联盟训练，我们还会持续进行研究，同时从技术和应用角度，也存在很多问题需要优化和解决：<br><br>
从技术角度上来说，可以在更高效、更具针对性引导多样性的方向做进一步探索和研究，比如：<br><br>
如何在保证种群不断丰富的前提下，将计算量限制在一定可控范围内，比如是否可以使用贝叶斯优化方法对PBT方法探索空间的减少[21]；<br><br>
如何使用少量训练模型，同时产生多种打法风格，比如使用分层的泛化模型，可以针对不同的奖励配置进行引导训练；<br><br>
如何根据玩家数据或特征，作为群体进化中的一系列“种子”，进行联盟训练，从而使联盟中的模型策略更接近玩家。<br><br><div align="center">
<img id="aimg_1016416" aid="1016416" zoomfile="https://di.gameres.com/attachment/forum/202110/21/111116fu06pk8u0t4u0ihh.jpg" data-original="https://di.gameres.com/attachment/forum/202110/21/111116fu06pk8u0t4u0ihh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/21/111116fu06pk8u0t4u0ihh.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">[ 图17. AI多样化和个性化在游戏中的应用 ]</font></font></div>
<br>
从应用角度上来说，无论是Bot AI还是NPC AI，我们都不希望他们是一成不变的。每个AI可以有不同的性格、特点，同时AI也能够和玩家、AI互相之间进行一些交互，来驱动AI不断改变自己的行为、认知和生活方式[22]。我们暂不追求《西部世界》或者《失控玩家》中的NPC具有独立的想法，但可以首先和环境、玩家建立友好的互动关系，并且会根据玩家的不同喜好做出不同的对策，提供给玩家更加真实的体验。如图17所示，这也需要我们去生产多样性的AI模型或模型池，而且可以根据玩家或周围AI互动的结果，动态调整AI的行为模式，来符合玩家所想要得到的体验。<br><br><font size="2"><font color="#808080">脚注</font></font><br><font size="2"><font color="#808080"><br></font></font><br><font size="2"><font color="#808080">[1]https://deepmind.com/blog/article/AlphaStar-Grandmaster-level-in-StarCraft-II-using-multi-agent-reinforcement-learning AlphaStar: Grandmaster level in StarCraft II using multi-agent reinforcement learning</font></font><br><font size="2"><font color="#808080">[2]https://openai.com/five/ OpenAI Five</font></font><br><font size="2"><font color="#808080">[3]https://openai.com/blog/competitive-self-play/ Competitive Self-Play</font></font><br><font size="2"><font color="#808080">[4]https://www.sohu.com/a/310018113_354973 AI Dota2虽完虐人类却弱点频现 | OpenAI Five亲测报告</font></font><br><font size="2"><font color="#808080">[5]https://zhuanlan.zhihu.com/p/63306194 碾压Dota2世界冠军的AI，被一小撮人持续干翻了</font></font><br><font size="2"><font color="#808080">[6]https://3g.163.com/dy/article_cambrian/FU4F329T05491OUS.html 赛博朋克2077--遍地是BUG，处处是妥协</font></font><br><font size="2"><font color="#808080">[7]https://cloud.tencent.com/developer/article/1805866 游戏“捏脸”需要高手教程？用这个AI模型，一张肖像照就能快速生成</font></font><br><font size="2"><font color="#808080">[8]https://www.zhihu.com/question/29910983 知乎：乒乓球国家队陪练都是什么水平？</font></font><br><font size="2"><font color="#808080">[9]https://arxiv.org/pdf/2011.13729.pdf TStarBot-X: An Open-Sourced and Comprehensive Study for Efficient League Training in StarCraft II Full Game</font></font><br><font size="2"><font color="#808080">[10]https://arxiv.org/pdf/2012.13169.pdf SCC: an Efficient Deep RL Agent Mastering the Game of StarCraft II</font></font><br><font size="2"><font color="#808080">[11]https://deepmind.com/blog/article/capture-the-flag-science Capture the Flag: the emergence of complex cooperative agents</font></font><br><font size="2"><font color="#808080">[12]https://en.wikipedia.org/wiki/Elo_rating_system Wiki: Elo</font></font><br><font size="2"><font color="#808080">[13]https://en.wikipedia.org/wiki/TrueSkill Wiki: TrueSkill</font></font><br><font size="2"><font color="#808080">[14]https://zhuanlan.zhihu.com/p/362806149 【CSGO】如何分析游戏数据</font></font><br><font size="2"><font color="#808080">[15]https://arxiv.org/pdf/2002.00632.pdf Effective Diversity in Population Based Reinforcement Learning</font></font><br><font size="2"><font color="#808080">[16]https://arxiv.org/pdf/2103.07927.pdf Modelling Behavioural Diversity for Learning in Open-Ended Games</font></font><br><font size="2"><font color="#808080">[17]https://zh.wikipedia.org/wiki/%E8%A1%8C%E5%88%97%E5%BC%8F Wiki：行列式</font></font><br><font size="2"><font color="#808080">[18]https://arxiv.org/pdf/1207.6083.pdf Determinantal point processes for machine learning</font></font><br><font size="2"><font color="#808080">[19]https://zhuanlan.zhihu.com/p/95607668 行列式点过程DPP在推荐系统中的应用</font></font><br><font size="2"><font color="#808080">[20]https://arxiv.org/pdf/1711.09846.pdf Population Based Training of Neural Networks</font></font><br><font size="2"><font color="#808080">[21]https://proceedings.neurips.cc//paper/2020/file/c7af0926b294e47e52e46cfebe173f20-Paper.pdf Provably Efficient Online Hyperparameter Optimization with Population-Based Bandits</font></font><br><font size="2"><font color="#808080">[22]http://www.coreesports.net/13845.html rct studio联合创始人陈雨恒：如何让NPC成为有血有肉的“虚拟人”</font></font><br><br><font size="2"><font color="#808080"></font></font><br><font size="2"><font color="#808080">来源：腾讯游戏学堂</font></font><br><font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/Sfwk1Afbn05Jphqg6YNZRg</font></font><br><br>
</td></tr></tbody></table>


  
</div>
            