
---
title: 'RPG游戏社交系统设计思路分析'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202112/20/110526rovio8oy8nclo0ji.jpg'
author: GameRes 游资网
comments: false
date: Mon, 20 Dec 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202112/20/110526rovio8oy8nclo0ji.jpg'
---

<div>   
<div align="center">
<img id="aimg_1025267" aid="1025267" zoomfile="https://di.gameres.com/attachment/forum/202112/20/110526rovio8oy8nclo0ji.jpg" data-original="https://di.gameres.com/attachment/forum/202112/20/110526rovio8oy8nclo0ji.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/110526rovio8oy8nclo0ji.jpg" referrerpolicy="no-referrer">
</div><br>
<font color="#808080"><i>本文首发于知乎白衣，个人主页https://www.zhihu.com/people/fu-dian-jun，为某不知名大厂在职策划，欢迎各位同行及游戏爱好者前来交流。</i></font><br>
<br>
<strong><font color="#de5650">前言</font></strong><br>
<br>
首先明确一下，此处所说RPG游戏为MMORPG游戏，MMORPG由于其包罗万象的特点，堪称游戏设计的大基本功，而社交系统作为一个没有Gameplay属性的系统穿插其中，但对其他系统进行总结分析时，均能寻找到其草蛇灰线，并影响着游戏整体的生态、体验、留存多个维度。此文笔者谨以MMORPG新人策划的视角，对MMORPG游戏常见的社交系统其定位、意义以及未来发展进行分析，欢迎各位同行进行交流。<br>
<br>
<strong><font color="#de5650">为何需要社交</font></strong><br>
<br>
做好社交之前，需要理解一个很重要的内容内容，为什么玩家需要社交？其实游戏中对于人际关系的架构基本与现实世界相同，所以大部分传播学的理论在游戏中也同样适用。当然，游戏世界可能由于虚拟的关系，来的更接近于乌托邦。基于马斯洛需求层次，笔者总结出以下三点。<br>
<br>
<strong>认同感——吸引玩家留存</strong><br>
<br>
玩家在游戏过程中，需要得到其他的成员的认同，这个可能只是简单的一起组队打副本，抑或是简单的几句世界频道的交流。总之玩家在这个世界中的投入，需要得到来自其他玩家的反馈，从而让玩家产生意识，这不只是我的游戏，或者说我现在的行为存在更大的意义。<br>
<br>
<strong>归属感——创造群体</strong><br>
<br>
在传播学中，对群体有以下定义：不论何种群体，在传播活动中其成员都要受群体形成的规范的调节和制约，保持大致统一的行为目标和认知结构。也就是说，群体往往有着统一的目标：例如公会的统一建设的目标，例如SLG联盟中占领城池的目标。当玩家拥有了一个属于自己的群体时，才会有更大的概率得到认同，或者说展示自己，有一群志同道合的玩家来一起进行游戏。<br>
<br>
<div align="center">
<img id="aimg_1025268" aid="1025268" zoomfile="https://di.gameres.com/attachment/forum/202112/20/110527r4yx7a3747l7zz3e.png" data-original="https://di.gameres.com/attachment/forum/202112/20/110527r4yx7a3747l7zz3e.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/110527r4yx7a3747l7zz3e.png" referrerpolicy="no-referrer">
</div><br>
<strong>优越感——在玩家群体间进行对比</strong><br>
<br>
优越感指的是在游戏过程中玩家需要进行自我炫耀，可能是作为高手来带领菜鸟玩家，也可能是与仇家对战等，而高低之分需要通过对比产生。同样，这部分与社交行为中的“冲突”相近，属于较为负面的一种表达方式，但这也是游戏体验、玩家行为的一部分，正所谓有人的地方就有江湖，玩家有着在游戏中快意情仇的需求，自然就会需要通过社交来体验优越感。<br>
<br>
<div align="center">
<img id="aimg_1025269" aid="1025269" zoomfile="https://di.gameres.com/attachment/forum/202112/20/110527iojnfffzqnaldnie.png" data-original="https://di.gameres.com/attachment/forum/202112/20/110527iojnfffzqnaldnie.png" width="421" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/110527iojnfffzqnaldnie.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">如何创造社交</font></strong><br>
<br>
<strong>给予身份</strong><br>
<br>
一个人的社交关系网络往往是由自身不同的身份所带来的。举例我们常见的微信列表，可能存在爱人、父母、子女、老师、同学、同事等多位好友，而每一位好友我们往往通过一个身份来进行连线。这也同理可以应用于游戏之中，以较为经典的MMORPG剑网三进行举例，玩家在游戏中可能存在哪些身份？师徒、队友、门派弟子、阵营等等，每一种身份，均会对玩家所在的群体进行一个划分，而每一个新的场景均会存在新的社交的可能。笔者理解，这也类似于大学时期的公选课，大量的选项对应的是大量潜在的社交可能。<br>
<br>
<div align="center">
<img id="aimg_1025270" aid="1025270" zoomfile="https://di.gameres.com/attachment/forum/202112/20/110528g5g916996hr393b7.png" data-original="https://di.gameres.com/attachment/forum/202112/20/110528g5g916996hr393b7.png" width="532" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/110528g5g916996hr393b7.png" referrerpolicy="no-referrer">
</div><br>
<strong>个性表达</strong><br>
<br>
让玩家形象变得足够的生动鲜明。现在的部分游戏中存在加好友后可以赠送体力的设定，这个设定有多个作用：比如可以绑定用户，通过小恩小惠来留住玩家，比如简单的双向交互。但因为玩家加了好友的动机是互送体力，所以在其他场景中，类似选择进行组队任务时，可能依旧会选择通过世界频道来进行召集，这种相当于对玩家进行了无效化社交。所以在创造社交场景时，需要给予玩家更为鲜明的社交画像，如玩家通过副本结识其他玩家，需要向该玩家展示另一名玩家类似战力、装备等信息（这就是个性表达），方便用户建立对该用户的认知和标签。<br>
<br>
<div align="center">
<img id="aimg_1025271" aid="1025271" zoomfile="https://di.gameres.com/attachment/forum/202112/20/110528ddt54dawtclu4il8.png" data-original="https://di.gameres.com/attachment/forum/202112/20/110528ddt54dawtclu4il8.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/110528ddt54dawtclu4il8.png" referrerpolicy="no-referrer">
</div><br>
<strong>善用需求</strong><br>
<br>
通过建立不同的需求来推动玩家之间的社交。主要包括两个方面，一方面是来自于数值方面的驱动，类似于副本多人组队难度会下降，同时会产出更好的奖励。这就通过奖励驱动玩家选择组队；另一方面则是精神驱动，即玩家在游戏过程中本身就存在着社交的需求，只需要在合适的场景进行引导即可。<br>
<br>
<strong><font color="#de5650">常见的社交系统</font></strong><br>
<br>
此处通过社交软件常见的三种模式进行总结归类，下方具体介绍不同类型的社交系统<br>
<br>
<strong>私聊系统</strong><br>
<br>
聊天系统、竞技场、好友系统、情缘系统<br>
<br>
聊天系统作为游戏中最基础的系统而存在，相当于组成了玩家最为基础和重要的沟通手段。而往往与聊天系统进行搭配的则是好友系统，两者共同组成了基础的社交部分，类似于“简易QQ”。<br>
<br>
竞技系统、情缘系统则是小范围的社交系统，与之类似的还有固定队系统等，此类社交具有范围小、关系紧密、社交属性明显等特点，玩家受到玩法、情感等方面的限制，组成了具有较高门槛的社交群体，而这部分群体也是游戏所需要重点维护的关系。<br>
<br>
<div align="center">
<img id="aimg_1025272" aid="1025272" zoomfile="https://di.gameres.com/attachment/forum/202112/20/110530km4wgz4b6mjzdoum.png" data-original="https://di.gameres.com/attachment/forum/202112/20/110530km4wgz4b6mjzdoum.png" width="464" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/110530km4wgz4b6mjzdoum.png" referrerpolicy="no-referrer">
</div><br>
<strong>群聊系统</strong><br>
<br>
公会系统、副本系统<br>
<br>
群聊系统往往类似于现实中的社群，存在一定的目的，但已经属于较为外层的社交，例如副本，玩家间存在共同目的为打通副本，但这里面不可能每一个都很亲密，会存在亲疏之分。<br>
<br>
<strong>论坛系统</strong><br>
<br>
社交分享系统 、社区系统，此类往往属于较为边缘的内容，用于鼓励玩家分享自身的日常、分享对游戏的二次创作等内容，近年来演变为两种趋势，一种为与游戏内的社交高度结合，使其成为一个较为重要的信息渠道，类似哈利波特；另一种则移出游戏外，作为单独的用户UGC平台存在，类似米哈游的米游社。<br>
<br>
<div align="center">
<img id="aimg_1025273" aid="1025273" zoomfile="https://di.gameres.com/attachment/forum/202112/20/110531owzii0zjgw0ixqiw.png" data-original="https://di.gameres.com/attachment/forum/202112/20/110531owzii0zjgw0ixqiw.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/20/110531owzii0zjgw0ixqiw.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">总结</font></strong><br>
<br>
经过这两周的思考，个人对游戏中的社交有了以下方面的理解：<br>
<br>
1.社交作为人类归属需求中的一种主要行为，在游戏中也同样存在，哪怕是在目前游戏市场大量游戏选择弱化社交概念的情况下，社交依旧有其存在的意义。<br>
<br>
2.传统游戏社交模型能够带给玩家的冲击愈发重复，玩家们需要能够双向传递所带来的情感冲击，可以参考尼尔机械纪元E结局、死亡搁浅等。<br>
<br>
3.置后社交效果明显。部分游戏会选择在游戏前期鼓励玩家加好友，不得不组队通过任务等方式来强制进行社交，但玩家前期需要对游戏的玩法、剧情进行高强度的认知，而此时若想打造沉浸式体验，需要让玩家有一定理解后再进行社交。<br>
<br>
4.社交讲求顺其自然，尤其需要搞懂游戏类型与定位。之前见过一些强数值向的游戏想要进行不同层级玩家间的社交，即让大R和小R一起玩，但双方战力带来的悬殊差距自然是缺乏共同语言的，所有的社交设计，需要结合游戏核心玩法和用户画像来进行。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<br>
  
</div>
            