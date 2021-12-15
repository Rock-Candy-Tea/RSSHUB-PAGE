
---
title: '历史首次挖到钻石！网易AI在《我的世界》竞赛中夺冠'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211215/S49943b8a-d478-4522-97cd-40e301906e85.png'
author: 快科技（原驱动之家）
comments: false
date: Wed, 15 Dec 2021 15:55:07 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211215/S49943b8a-d478-4522-97cd-40e301906e85.png'
---

<div>   
<p>近日，在NeurIPS会议上举办的MineRL 2021 Diamond Competition落下帷幕，来自网易互娱AI Lab的Athena AI凭借高超的挖钻技巧，<strong>在以《我的世界》游戏为竞技环境的比赛中拿下Intro赛道的冠军以及Research赛道的亚军。</strong></p>
<p><span style="color:#ff0000;"><strong>这是AI第一次在《我的世界》中挖掘到钻石。</strong></span></p>
<p>该比赛由CMU, OpenAI, DeepMind, Microsoft Research等机构联合举办，是强化学习方向最负盛名的比赛之一。比赛自2019年起，每年在机器学习和计算神经科学领域顶级学术会议NeurIPS上举办，今年为第三届。</p>
<p>该比赛近年来吸引了包括腾讯AI Lab，华为诺亚方舟，启元，清华，北大，中科院，香港中文大学，南洋理工大学，斯坦福大学，美国西北大学、德国比勒费尔德大学在内的众多工业界和学术界的相关研究人员。</p>
<p>今年的比赛同样有来自海内外近60支队伍、超过400名研究人员同场竞技。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211215/49943b8a-d478-4522-97cd-40e301906e85.png" target="_blank"><img alt="历史首次挖到钻石！网易AI在《我的世界》竞赛中夺冠" h="314" src="https://img1.mydrivers.com/img/20211215/S49943b8a-d478-4522-97cd-40e301906e85.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>本届MineRL比赛划分为了Intro和Research两个赛道。</strong>与Research赛道注重高效地利用玩家数据，对训练数据表征、训练规模等方面进行了诸多的限制不同，Intro赛道更加贴近游戏AI开发中的真实场景，需要参赛者根据游戏特性设计针对性的算法，最大限度地提升AI的水平。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211215/29c90b69-995a-433a-8305-7653738460d0.png" target="_blank"><img alt="历史首次挖到钻石！网易AI在《我的世界》竞赛中夺冠" h="337" src="https://img1.mydrivers.com/img/20211215/S29c90b69-995a-433a-8305-7653738460d0.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>MineRL比赛要求参赛者在我的世界（MineCraft）游戏生存模式中，<span style="color:#ff0000;"><strong>训练出一个能够从零开始收集各种资源、制作工具最后挖到钻石的智能体。</strong></span></p>
<p>该任务的主要难点有：</p>
<p><strong>1、巨大的动作空间和状态空间：</strong></p>
<p>我的世界是一款3D开放世界游戏，智能体仅能依赖经过压缩处理的游戏画面以及背包中的部分物品数量信息来感知周围环境，能够执行的动作包括移动、攻击、视角调整、工具制作、装备切换、物品放置等所有玩家能够进行的操作，动作空间巨大。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211215/1b8ed610-878d-42fc-86a2-b864cfd26180.png" target="_blank"><img alt="历史首次挖到钻石！网易AI在《我的世界》竞赛中夺冠" h="350" src="https://img1.mydrivers.com/img/20211215/S1b8ed610-878d-42fc-86a2-b864cfd26180.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>2、复杂的工具链：</strong></p>
<p>我的世界中存在庞杂的资源系统和物品合成体系，即使是仅为了获取钻石也需要智能体学会按顺序收集并制作各种所需的资源和物品。</p>
<p>例如为了保证在挖到钻石前制作出铁镐，智能体必须学会在探索到地下深处时做好木棍、收集至少三块铁矿和一些燃料并在放置好的熔炉边烧制出所需的铁锭。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211215/aa8fe72e-ff7f-4404-94d9-c0ee6dcd8eb3.png" target="_blank"><img alt="历史首次挖到钻石！网易AI在《我的世界》竞赛中夺冠" h="244" src="https://img1.mydrivers.com/img/20211215/Saa8fe72e-ff7f-4404-94d9-c0ee6dcd8eb3.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>3、长期规划能力：</strong></p>
<p>在MineRL环境中智能体能够与环境进行至多18000次交互，这就要求智能体能够具备长期规划的能力。</p>
<p>例如智能体需要在游戏开始时就根据出生地周围环境，决定是否在收集完附近的木质资源后直接向地下探索矿物或是花费时间离开出生地寻找更多的木材以避免下矿后可能出现没有木头制作工具的尴尬。</p>
<p style="text-align: center"><img alt="历史首次挖到钻石！网易AI在《我的世界》竞赛中夺冠" h="290" src="https://img1.mydrivers.com/img/20211215/0db4bc46-0875-4d63-95cd-28bae9c4094a.gif" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p><strong>4、数据集有限且不完美</strong>：</p>
<p>主办方提供了可供AI学习的约200场人类玩家数据，数据集规模十分有限且并不是所有场次中的玩家最终都获得了钻石</p>
<p>在本次比赛中，在其他队伍更倾向于利用玩家数据集并使用层次化训练方法的氛围中，<strong>网易互娱AI Lab，另辟蹊径，采用端到端的纯强化学习方案，史无前例地训练出了能够从零开始获得钻石的Athena AI。</strong></p>
<p>Athena AI通过合理地约束有效动作，达到了对状态的搜索空间进行剪枝的目的，使得AI在不使用分层策略的情况下依然能够高效地在巨大的状态空间中进行探索和学习。</p>
<p>Athena AI的实现方案表明，即使是在多任务且任务之间有着复杂依赖关系的游戏场景内，单一的端到端模型的表现也是可以达到甚至超过精细设计的分层训练方式。</p>
<p>在最终Intro赛道的结果中，<strong>来自网易互娱AI Lab的队伍WinOrGoHome以645.55分夺得冠军，在100场游戏中累计21场都成功挖到了钻石，超越第二名的队伍近50%的分数。</strong></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211215/464a2abb-32b3-4750-bc78-6afa92b66fbd.png" target="_blank"><img alt="历史首次挖到钻石！网易AI在《我的世界》竞赛中夺冠" h="364" src="https://img1.mydrivers.com/img/20211215/S464a2abb-32b3-4750-bc78-6afa92b66fbd.png" style="border:black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>值得一提的是，作为智能AI系统，网易互娱AI Lab研发的Athena AI目前已经落地应用于网易互娱旗下的多款游戏。</p>
<p>网易互娱AI Lab成立于2017年，AI Lab所提供的人工智能服务包括计算机视觉、自然语言处理、语音信号处理、游戏AI多个方面。</p>
<p>目前技术已应用于网易互娱旗下多款热门游戏，如《梦幻西游》、《哈利波特：魔法觉醒》、《阴阳师》、《大话西游》、《荒野行动》、《明日之后》等等。</p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/wangyi.htm"><i>#</i>网易</a><a href="https://news.mydrivers.com/tag/wodeshijie.htm"><i>#</i>我的世界</a><a href="https://news.mydrivers.com/tag/guanjun.htm"><i>#</i>冠军</a></p>
<p class="url">
     
<span>责任编辑：随心</span>
</p>
        
</div>
            