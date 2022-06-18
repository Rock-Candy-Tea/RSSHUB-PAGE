
---
title: '天美F1技术策划：一个案例为你揭秘TD日常'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202206/10/091020t4ouua1m691aa4o3.png'
author: GameRes 游资网
comments: false
date: Fri, 10 Jun 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202206/10/091020t4ouua1m691aa4o3.png'
---

<div>   
<i><font color="#808080">本文首发“TiMi Club 天美俱乐部”微信公众号</font></i><br>
<br>
中国游戏行业发展至今，从专业到分工，正在经历哪些变化？天美联合腾讯游戏学堂，举办“游戏是门技术活儿：专业技能探秘”知乎圆桌活动，本文为圆桌议题“什么特质会让你立刻觉得一个技术策划很靠谱？”下的回答，希望对大家有所帮助。<br>
<br>
<font color="#808080"><strong>作者：菠萝王子</strong></font><br>
<font color="#808080"><strong>腾讯天美F1工作室高级技术策划</strong></font><br>
<br>
我目前在天美游戏 F1 工作室担任高级技术策划，工作内容主要对接摄像机特性以及 AI 特性里的游戏的技术设计以及实现工作。<br>
<br>
如何去做好一个靠谱的技术策划，我以一个工作中的小案例作为例子：<br>
<br>
当时游戏中已经做了一个敌兵对玩家所在的位置扔手雷的功能。但是在实际游戏体验中，由于手雷在飞行的过程中经常会撞到其他的静态障碍物，比如突出的建筑、栏杆等。由于碰撞，手雷常常最终落到一个对玩家没威胁的位置。<br>
<br>
最后大家在体验游戏的时候，常常感受不到敌兵投掷手雷这项功能，对玩家的战术威胁，也就失去了这个游戏设计点的初衷，即确保手雷能落到玩家身边，对玩家产生威胁。体验落空，战斗体验必然是不够好的。<br>
<br>
当我拿到这个需求的时候，其实首先是要作为策划去分析，这个问题的根源是什么？大家说体验不好的原因是什么？是敌兵扔手雷这个功能没意义吗？<br>
<br>
不是。而是敌人扔手雷的设计目的是为了让手雷能对玩家当前的位置产生威胁，使玩家主动改变当前位置（往往此时玩家会躲在一个比较安全的地方，比如掩体后），从而玩家会有可能再次出现在敌兵视野内，最终敌人能再次对玩家进行有效射击输出。<br>
<br>
<strong><font color="#de5650">这是作为技术策划，对于案例首先进行游戏设计层面的深度分析。</font></strong><br>
<br>
然后我们开始进行方案设计，方案设计的目的就是要优化这个现状，以达到游戏设计师的预想体验。<br>
<br>
那么预想体验是什么？回顾上面的分析，不难发现，预想体验就是敌兵在扔手雷的时候，手雷要尽可能有效地扔到玩家投掷时刻所在的位置身边。<br>
<br>
也就是说，敌兵投掷瞄准时需要预判手雷行进轨迹中的障碍物，调整角度，确保手雷能有效扔到玩家身边，而不是被路径中的各种静态障碍物给阻挡了。<br>
<br>
在完成设计分析以及预想体验归纳后，我开始进行这次优化的方案设计，在引擎中制作了如下功能演示：<br>
<br>
<div align="center">
<img aid="1042215" zoomfile="https://di.gameres.com/attachment/forum/202206/10/091020t4ouua1m691aa4o3.png" data-original="https://di.gameres.com/attachment/forum/202206/10/091020t4ouua1m691aa4o3.png" width="600" id="aimg_1042215" inpost="1" src="https://di.gameres.com/attachment/forum/202206/10/091020t4ouua1m691aa4o3.png" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1042216" zoomfile="https://di.gameres.com/attachment/forum/202206/10/091021p3wwmp7r3wx3w23z.png" data-original="https://di.gameres.com/attachment/forum/202206/10/091021p3wwmp7r3wx3w23z.png" width="600" id="aimg_1042216" inpost="1" src="https://di.gameres.com/attachment/forum/202206/10/091021p3wwmp7r3wx3w23z.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">上面的图中三角形是代表玩家，小方块代表敌兵</font></font></div><br>
从策划的角度上阐明了这个检测机制是如何展开的，敌兵（三角形）在投掷手雷的时候，会按照特定角度对玩家（小方块）当前位置进行轨迹线预判。<br>
<br>
在预判中，如果手雷中间被其他障碍物碰撞，则敌兵会主动调整抛射曲线角度，继续尝试另一条路径去向玩家扔手雷。<br>
<br>
只有当预判中出现了一条可以直接碰撞到玩家的路径，系统才会选择将这条路线作为最终的投掷路径。<br>
<br>
这个功能可以确保敌兵一旦扔出手雷，必定能有效命中玩家，以达到策划预期的设计效果，达成一次有意义的投掷。<br>
<br>
当然如果一直找不到合理有效的投掷路线，敌兵会主动取消投掷手雷，去进行其他更合理的行为。<br>
<br>
通过准确分析需求，清晰完整提出解决方案，也大幅度减少了程序功能制作迭代的时间。<br>
<br>
从程序的角度上来说，这个模块的逻辑实现清晰完整，程序直接可以一遍完成这个功能的开发。<br>
<br>
所以根据我个人以往的工作经验来看，在团队合作的过程中，作为技术策划，能站在策划的角度去分析问题的根源，以及合理地提出优化落地方案，并能以专业的技术作为傍身，把方案设计以技术或者原型的形式落地输出，让策划以及程序都能在方案中看到完整的呈现，是最容易得到团队其他成员的认同的，也是让团队认为你是一个靠谱的技术策划的根本所在。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：TiMi Club 天美俱乐部</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/ReYkxYQ0ywQirmdVb3YoeA</font></font><br>
<br>
  
</div>
            