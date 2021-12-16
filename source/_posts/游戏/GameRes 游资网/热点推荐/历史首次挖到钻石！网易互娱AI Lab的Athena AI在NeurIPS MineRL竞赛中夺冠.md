
---
title: '历史首次挖到钻石！网易互娱AI Lab的Athena AI在NeurIPS MineRL竞赛中夺冠'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202112/10/174946y96gm6wic26qw6r6.png'
author: GameRes 游资网
comments: false
date: Fri, 10 Dec 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202112/10/174946y96gm6wic26qw6r6.png'
---

<div>   
近日，在NeurIPS会议上举办的MineRL 2021 Diamond Competition落下帷幕，来自网易互娱AI Lab的Athena AI凭借高超的挖钻技巧，在以《我的世界》游戏为竞技环境的比赛中拿下Intro赛道的冠军以及Research赛道的亚军。这是AI第一次在《我的世界》中挖掘到钻石。该比赛由CMU, OpenAI, DeepMind, Microsoft Research等机构联合举办，是强化学习方向最负盛名的比赛之一。比赛自2019年起，每年在机器学习和计算神经科学领域顶级学术会议NeurIPS上举办，今年为第三届。该比赛近年来吸引了包括腾讯AI Lab，华为诺亚方舟，启元，清华，北大，中科院，香港中文大学，南洋理工大学，斯坦福大学，美国西北大学、德国比勒费尔德大学在内的众多工业界和学术界的相关研究人员。今年的比赛同样有来自海内外近60支队伍、超过400名研究人员同场竞技。<br>
<br>
<div align="center">
<img id="aimg_1024400" aid="1024400" zoomfile="https://di.gameres.com/attachment/forum/202112/10/174946y96gm6wic26qw6r6.png" data-original="https://di.gameres.com/attachment/forum/202112/10/174946y96gm6wic26qw6r6.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/174946y96gm6wic26qw6r6.png" referrerpolicy="no-referrer">
</div><br>
本届MineRL比赛划分为了Intro和Research两个赛道。与Research赛道注重高效地利用玩家数据，对训练数据表征、训练规模等方面进行了诸多的限制不同，Intro赛道更加贴近游戏AI开发中的真实场景，需要参赛者根据游戏特性设计针对性的算法，最大限度地提升AI的水平。<br>
<br>
<div align="center">
<img id="aimg_1024401" aid="1024401" zoomfile="https://di.gameres.com/attachment/forum/202112/10/174947zmi7pp7uz768762i.png" data-original="https://di.gameres.com/attachment/forum/202112/10/174947zmi7pp7uz768762i.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/174947zmi7pp7uz768762i.png" referrerpolicy="no-referrer">
</div><br>
MineRL比赛要求参赛者在我的世界（MineCraft）游戏生存模式中，训练出一个能够从零开始收集各种资源、制作工具最后挖到钻石的智能体。该任务的主要难点有：<br>
<br>
1.巨大的动作空间和状态空间： 我的世界是一款3D开放世界游戏，智能体仅能依赖经过压缩处理的游戏画面以及背包中的部分物品数量信息来感知周围环境，能够执行的动作包括移动、攻击、视角调整、工具制作、装备切换、物品放置等所有玩家能够进行的操作，动作空间巨大。<br>
<br>
<div align="center">
<img id="aimg_1024402" aid="1024402" zoomfile="https://di.gameres.com/attachment/forum/202112/10/174947jujhikauxdeek2ib.png" data-original="https://di.gameres.com/attachment/forum/202112/10/174947jujhikauxdeek2ib.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/174947jujhikauxdeek2ib.png" referrerpolicy="no-referrer">
</div><br>
2.复杂的工具链：我的世界中存在庞杂的资源系统和物品合成体系，即使是仅为了获取钻石也需要智能体学会按顺序收集并制作各种所需的资源和物品。例如为了保证在挖到钻石前制作出铁镐，智能体必须学会在探索到地下深处时做好木棍、收集至少三块铁矿和一些燃料并在放置好的熔炉边烧制出所需的铁锭。<br>
<br>
<div align="center">
<img id="aimg_1024403" aid="1024403" zoomfile="https://di.gameres.com/attachment/forum/202112/10/174950n1hvbhe1huausao5.png" data-original="https://di.gameres.com/attachment/forum/202112/10/174950n1hvbhe1huausao5.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/174950n1hvbhe1huausao5.png" referrerpolicy="no-referrer">
</div><br>
3.长期规划能力：在MineRL环境中智能体能够与环境进行至多18000次交互，这就要求智能体能够具备长期规划的能力。例如智能体需要在游戏开始时就根据出生地周围环境，决定是否在收集完附近的木质资源后直接向地下探索矿物或是花费时间离开出生地寻找更多的木材以避免下矿后可能出现没有木头制作工具的尴尬。<br>
<br>
<div align="center">
<img id="aimg_1024405" aid="1024405" zoomfile="https://di.gameres.com/attachment/forum/202112/10/175043kdx0k0wkdqdo2v09.gif" data-original="https://di.gameres.com/attachment/forum/202112/10/175043kdx0k0wkdqdo2v09.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/175043kdx0k0wkdqdo2v09.gif" referrerpolicy="no-referrer">
</div><br>
4.数据集有限且不完美：主办方提供了可供AI学习的约200场人类玩家数据，数据集规模十分有限且并不是所有场次中的玩家最终都获得了钻石<br>
<br>
在本次比赛中，在其他队伍更倾向于利用玩家数据集并使用层次化训练方法的氛围中，网易互娱AI Lab不破不立，另辟蹊径，在面对如此复杂的问题时，大胆放弃依赖主办方提供的人类数据，没有采用分层强化学习等被认为是解决该问题的一些关键技术，而采用端到端的纯强化学习方案，在自研的分布式强化学习框架中结合了自身在游戏AI领域积累的丰富工程实践经验，史无前例地训练出了能够从零开始获得钻石的Athena AI。Athena AI通过合理地约束有效动作，达到了对状态的搜索空间进行剪枝的目的，使得AI在不使用分层策略的情况下依然能够高效地在巨大的状态空间中进行探索和学习。Athena AI的实现方案表明，即使是在多任务且任务之间有着复杂依赖关系的游戏场景内，单一的端到端模型的表现也是可以达到甚至超过精细设计的分层训练方式。在最终Intro赛道的结果中，来自网易互娱AI Lab的队伍WinOrGoHome以645.55分夺得冠军，在100场游戏中累计21场都成功挖到了钻石，超越第二名的队伍近50%的分数。<br>
<br>
<div align="center">
<img id="aimg_1024404" aid="1024404" zoomfile="https://di.gameres.com/attachment/forum/202112/10/174952yyq505gximtbfyye.png" data-original="https://di.gameres.com/attachment/forum/202112/10/174952yyq505gximtbfyye.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/174952yyq505gximtbfyye.png" referrerpolicy="no-referrer">
</div><br>
值得一提的是，作为智能AI系统，网易互娱AI Lab研发的Athena AI目前已经落地应用于网易互娱旗下的多款游戏，从竞技对战到平衡性测试，涵盖了多种类型的游戏，产生了巨大的技术价值。<br>
<br>
网易互娱AI Lab成立于2017年，隶属于网易互动娱乐事业群，是游戏行业领先的人工智能实验室。AI Lab所提供的人工智能服务包括计算机视觉、自然语言处理、语音信号处理、游戏AI多个方面。目前技术已应用于网易互娱旗下多款热门游戏，如《梦幻西游》、《哈利波特：魔法觉醒》、《阴阳师》、《大话西游》、《荒野行动》、《明日之后》等等。<br>
<br>
  
</div>
            