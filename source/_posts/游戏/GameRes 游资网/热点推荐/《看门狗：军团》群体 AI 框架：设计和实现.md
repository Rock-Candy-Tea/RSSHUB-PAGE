
---
title: '《看门狗：军团》群体 AI 框架：设计和实现'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202202/24/091559qcr3hylxxly3nr03.jpg'
author: GameRes 游资网
comments: false
date: Thu, 24 Feb 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202202/24/091559qcr3hylxxly3nr03.jpg'
---

<div>   
<div align="center">
<img aid="1031578" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091559qcr3hylxxly3nr03.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091559qcr3hylxxly3nr03.jpg" width="600" id="aimg_1031578" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091559qcr3hylxxly3nr03.jpg" referrerpolicy="no-referrer">
</div>作者：散漫的十七  本文首发知乎<br>
https://zhuanlan.zhihu.com/p/463560068<br>
<br>
<i><font color="#808080"><strong>GDC年份：</strong>2021</font></i><br>
<i><font color="#808080"><strong>GDC原标题：</strong>AI Summit: Branching Out: 'Watch Dogs Legion's' Architecture for Group AI Behaviours</font></i><br>
<i><font color="#808080"><strong>GDC Vault链接：</strong></font></i><br>
<i><font color="#808080">https://gdcvault.com/play/1027239/AI-Summit-Branching-Out-Watchgdcvault.com/play/1027239/AI-Summit-Branching-Out-Watch</font></i><br>
<i><font color="#808080"><strong>主讲人：</strong>Christopher Dragert, Ph.D., Patrick McKenna</font></i><br>
<i><font color="#808080"><strong>所属：</strong>Ubisoft Toronto, Ubisoft Toronto</font></i><br>
<br>
<strong><font color="#de5650">摘要</font></strong><br>
<br>
在《看门狗：军团》的开放世界中，世界基调的关键组成部分之一是让可信的 AI 执行逼真的行为。虽然可以调整单个个体的行为让其更加逼真，但多角色之间的交互可以提供更加丰富的体验。本次演讲将详细介绍 aLiVE群体AI系统，这是由Ubisoft Toronto开发的一种高度模块化的 AI 架构。该系统可以创建高度反应性（highly reactive）的群体行为，在《看门狗：军团》中用于制作 ID 检查、勒索、犯罪事件、人质救援、抗议团体和警察互动等等场景。当玩家与这些场景进行交互时，群体行为系统可以恰当地根据参与者的群体背景和身份定位，以真实有趣的方式做出反应。<br>
<br>
这个GDC分成前后两个部分，两位主讲人从设计和实现的角度分享了《看门狗：军团》中的开放世界群体AI框架，《看门狗：军团》中使用这套框架构建了绝大部分的NPC行为，通过调整预设可以构建出单个NPC乃至势力的行为模式以更好地为Gameplay服务，如体现NPC的能力，或构建Albion的各种随机发生的滥用职权的行为以塑造势力形象。<br>
<br>
以下是这个演讲的详细内容。<br>
<font color="#808080"><br>
</font><br>
<font color="#808080">（注：非精译，所有内容均为个人理解和再阐释）</font><br>
<font color="#808080">本文默认读者具有行为树、NPC行为逻辑、AI调试的基础知识，部分通用概念不再二次描述</font><br>
<br>
<strong><font color="#de5650">游戏玩法介绍</font></strong><br>
<br>
<div align="center">
<img aid="1031579" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091600i9ztv3uqiz1pv5pw.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091600i9ztv3uqiz1pv5pw.jpg" width="600" id="aimg_1031579" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091600i9ztv3uqiz1pv5pw.jpg" referrerpolicy="no-referrer">
</div><br>
扮演DedSec势力——一个黑客组织，目标是解放伦敦。<br>
<br>
在游戏过程中你可以招募任何你能见到的周围的伦敦市民。<br>
<br>
Play-as-Anyone，玩家可以招募他在开放世界中所见到的任何NPC，将其添加到自己的团队当中。<br>
<br>
<strong><font color="#de5650">设计需求</font></strong><br>
<br>
<div align="center">
<img aid="1031580" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091601bii5a8k5gka5huil.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091601bii5a8k5gka5huil.jpg" width="600" id="aimg_1031580" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091601bii5a8k5gka5huil.jpg" referrerpolicy="no-referrer">
</div><br>
从游戏玩法派生出了对AI的更高需求，玩家需要观察开放世界中NPC的行为，观察其是否有用某些能力。<br>
<br>
某些时候，游戏中会发生一些突发状况，可能来自开发者的设计，也可能是由于玩家做出了某些操作，此时，NPC也需要能够产生对应的反应，让玩家对其产生兴趣。<br>
<br>
因此，《看门狗：军团》对群体AI系统产生了如下几条设计需求：<br>
<br>
开放世界需要提供高光时刻来吸引玩家，从而促使玩家进行互动、对话、探索等行为<br>
<br>
"Hey, that guy just did something really cool, maybe I wanna add him to my team."<br>
<br>
NPC的互动需要经得起玩家的质疑——合理性<br>
<br>
NPC需要成为开放世界系统的一部分——整体性、实时性<br>
<br>
<strong><font color="#de5650">开放世界AI</font></strong><br>
<br>
<div align="center">
<img aid="1031581" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091601zmlfy31ym3wy05lg.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091601zmlfy31ym3wy05lg.jpg" width="600" id="aimg_1031581" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091601zmlfy31ym3wy05lg.jpg" referrerpolicy="no-referrer">
</div><br>
将目前开放世界的AI分为了三个层次，每一层行为的复杂程度和真实性逐步递增。最终是希望当NPC附近有任何事情发生时，NPC都会做出符合玩家心理预期的行为。<br>
<br>
等级1：只需要播放简单动画的路人 NPC<br>
<br>
作为背景板存在<br>
<br>
一般来讲不参与Gameplay，至多会做一些外表上的小细节<br>
<br>
等级2：播放“同步动画”（Synced Animation）的NPC——大部分“开放世界”游戏所处的阶段<br>
<br>
优点：可以表演交互和对话，能够更好地塑造NPC的形象<br>
<br>
缺点：进行交互的双方并不存在真正的关系，发生突发情况时表现就会变得十分不真实<br>
<br>
此处与下文中的同步动画个人理解为需要多个NPC同时播放的动画，即双人吵架、打架，或NPC之间发生的对话等等<br>
<br>
等级3：拥有群体行为的NPC<br>
<br>
Highly Realized<br>
<br>
符合“群体情境信息”（Group Context）——此处仅是为了统一名词便于表达，实际上context的含义在程序中描述的情况更加全面<br>
<br>
NPC自己的身份、职业<br>
<br>
NPC自己正在进行的行为<br>
<br>
同一场所其他NPC做出的行为<br>
<br>
...<br>
<br>
《看门狗：军团》能够通过群体行为系统构建出开放世界当中的所有行为，NPC可以遵循自己的身份，做出符合逻辑认知与世界观发展的行为。<br>
<br>
<div align="center">
<img aid="1031582" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091602vn107ai7odapa7dz.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091602vn107ai7odapa7dz.jpg" width="600" id="aimg_1031582" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091602vn107ai7odapa7dz.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">群体行为系统</font></strong><br>
<br>
<strong>1. 设计启发</strong><br>
<br>
在2014年的《细胞分裂：黑名单》中的全局脚本系统（Systemic Script）就已经有了当前的群体行为系统的雏形。<br>
<br>
<div align="center">
<img aid="1031583" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091602yi447zl744ylyr17.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091602yi447zl744ylyr17.jpg" width="600" id="aimg_1031583" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091602yi447zl744ylyr17.jpg" referrerpolicy="no-referrer">
</div><br>
关于全局脚本系统具体可以查看GDC：Modeling AI Perception and Awareness in Splinter Cell: Blacklist<br>
<br>
在全局脚本系统的设计过程中，主讲人总结了群体行为系统的设计准则(Philosophy)：<br>
<br>
<div align="center">
<img aid="1031584" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091602ye0xujgx7d7nrndu.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091602ye0xujgx7d7nrndu.jpg" width="600" id="aimg_1031584" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091602ye0xujgx7d7nrndu.jpg" referrerpolicy="no-referrer">
</div><br>
自底向上？<br>
<br>
依托于非群体管理的行为树或状态机上的节点，表现出类似的群体行为。但当出现突发事件时，难以做到状态的同步，且可能产生不可控的预期。<br>
<br>
自顶向下？<br>
<br>
使用群体管理脚本预设整个群体行为——灵活性不足，当面对开放世界中的大量事件时，无法对其进行反应<br>
<br>
Middle out<br>
<br>
可以通过NPC本身或管理系统本身产生某个行为，且动态的根据当前的情境信息与感知改变其行为，并将状态同步至群体行为管理器上。<br>
<br>
<strong>2. 组成元素</strong><br>
<br>
<div align="center">
<img aid="1031585" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091603westi5iqby4yxyq1.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091603westi5iqby4yxyq1.jpg" width="600" id="aimg_1031585" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091603westi5iqby4yxyq1.jpg" referrerpolicy="no-referrer">
</div><br>
这套群体行为系统由以下三部分组成：<br>
<br>
<strong>Actions</strong><br>
<br>
原始行为<br>
<br>
如播放动画，MoveTo，触发对话<br>
<br>
<strong>Behaviors</strong><br>
<br>
一系列Actions<br>
<br>
完成粒度较细的任务（Task），如ID检查中的扫描行为<br>
<br>
<strong>Strategies</strong><br>
<br>
一系列Behaviors<br>
<br>
完成高级目标，如整个ID检查<br>
<br>
（1）策略Strategies<br>
<br>
<div align="center">
<img aid="1031586" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091603h3bymm76pzyzrsvp.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091603h3bymm76pzyzrsvp.jpg" width="600" id="aimg_1031586" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091603h3bymm76pzyzrsvp.jpg" referrerpolicy="no-referrer">
</div><br>
一个完整的策略分为多个策略块<br>
<br>
策略块非循环性(Acyclically)地进行连接<br>
<br>
完成一个策略后就会去进行其他策略，策略的执行过程中也需要条件来进入下一个策略块<br>
<br>
每个策略块对应一个行为<br>
<br>
NPC们可以处于同一个策略块，也可以直接跳入某个策略块，如周围的警察NPC从巡逻行为直接参与到逮捕行为中<br>
<br>
当处于同一片区域时，NPC们可以进行同步，改变自己当前所处的策略块以完成群体行为<br>
<br>
（2）动作Actions<br>
<br>
<div align="center">
<img aid="1031587" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091603c1z12p88oo02qlzc.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091603c1z12p88oo02qlzc.jpg" width="600" id="aimg_1031587" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091603c1z12p88oo02qlzc.jpg" referrerpolicy="no-referrer">
</div><br>
全身动作Full-body Actions<br>
<br>
基本原则：NPC永远都在播放全身动作作为Idle<br>
<br>
如MoveTo，各种各样的全身动作等<br>
<br>
次要动画Secondary Actions<br>
<br>
某种层级更高的动作——可叠加的动画<br>
<br>
如进行对话、改变朝向、武器动画和设置AI状态（如表情等）等<br>
<br>
（3）行为结构体Behavior Structure<br>
<br>
<div align="center">
<img aid="1031588" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091604cb8k83g836iwz63l.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091604cb8k83g836iwz63l.jpg" width="600" id="aimg_1031588" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091604cb8k83g836iwz63l.jpg" referrerpolicy="no-referrer">
</div><br>
一次常规ID检查行为的图表，左侧为平民轨道，右侧为Albion轨道，共同配合完成了一次ID检查行为<br>
<br>
行为可以包含多个NPC的动作<br>
<br>
不同NPC有各自的行为轨道(Track)<br>
<br>
行为结构是一个有向无环图DAG（Directed Acyclic Graph）<br>
<br>
当联系(Connections) 与行为轨道发生交叉（如某个Action向自己之外的NPC发送通知）时进行同步<br>
<br>
在行为结构中引入了行为轨道和联系。行为轨道是基于对应的NPC的一系列行为；联系是NPC的动作之间的交互，可以发生在同一NPC的不同行为中，也可以在不同NPC之间进行跨轨道交互。只有某些行为会对其他轨道中的行为产生交互，如呼喊行为。<br>
<br>
（4）联系Connection<br>
<br>
<div align="center">
<img aid="1031589" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091604yngwwwroon30ifl6.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091604yngwwwroon30ifl6.jpg" width="600" id="aimg_1031589" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091604yngwwwroon30ifl6.jpg" referrerpolicy="no-referrer">
</div><br>
警察进行Connection：Play Bark后一个随机的间隔之后，平民才会进行移动<br>
<br>
通过联系启动轨道中的动作序列<br>
<br>
开始时OnStart、结束时OnEnd、特殊行为Action-Specific<br>
<br>
如呼喊行为所产生的联系（见图中黄色框体）在结束（OnEnd）时，平民NPC才会开始进行MoveTo动作<br>
<br>
当所有输入的联系上绑定的事件全部完成触发之后才会开始继续播放动作<br>
<br>
使用计时器对最终的行为表现Polish，包括正常行为可能需要的反应时间等<br>
<br>
个人理解Connection比较类似于Event，主讲人对其的描述也和UE4中常见的Event调用方式类似。触发全部的事件后再进行后续动作的播放可能是为了保证行为时间轴的正常推进，防止出现某些动画已经播放了，其他NPC又进行了某些和提前触发的动画不符合的行为，可能的实现方式是在全局管理器上做出某些限制。<br>
<br>
<strong>3. 各种注意事项</strong><br>
<br>
（1）连续性<br>
<br>
<div align="center">
<img aid="1031590" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091605e54h5kvvfn4x11fh.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091605e54h5kvvfn4x11fh.jpg" width="600" id="aimg_1031590" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091605e54h5kvvfn4x11fh.jpg" referrerpolicy="no-referrer">
</div><br>
不同的动作和行为之间需要保证整体的连续性，《看门狗：军团》通过动作容器(Container Action)进行管理。动作容器可以进行时机把控，并对上一个全身动作进行处理。<br>
<br>
当行为之间需要衔接时，通过动作容器处理上一个全身动作；当策略之间需要衔接时，通过前一个策略决定下一个策略，并保存所有的群体情境信息。<br>
<br>
（2）模块化<br>
<br>
<div align="center">
<img aid="1031551" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091250nqb0qcz0q7b1qzdt.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091250nqb0qcz0q7b1qzdt.jpg" width="600" id="aimg_1031551" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091250nqb0qcz0q7b1qzdt.jpg" referrerpolicy="no-referrer">
</div><br>
每个策略块实际上并不是指向某个特定的行为本身，而是指向一个行为种类 (Behavior Categories)<br>
<br>
每个行为种类存在一个默认的行为，在通常情况下，调用策略块实际上会调用对应的默认行为<br>
<br>
运行时可以指定地运行特殊行为，特殊行为存在特殊的先决条件(Precondition)，通过各种先决条件的配置的，AI可以根据游戏当前状态选择特殊行为<br>
<br>
某个NPC表现出来的特殊事件本质上都是通过预设的条件从而被设定好的，如某个带有格斗属性的NPC在被逮捕时，就会进行反击。<br>
<br>
可以通过NPC表现出来的行为反推其所拥有的能力<br>
<br>
特殊行为有着更高的优先级。当可以触发特殊事件时，群体行为系统会优先调用对应的特殊事件。<br>
<br>
（3）触发方式<br>
<br>
<div align="center">
<img aid="1031552" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091302m3fqyk4y68vc7kfa.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091302m3fqyk4y68vc7kfa.jpg" width="600" id="aimg_1031552" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091302m3fqyk4y68vc7kfa.jpg" referrerpolicy="no-referrer">
</div><br>
当分配策略时，会触发群体行为，主要有三种触发方式：<br>
<br>
在NPC出生点(Spawn Point)上配置策略<br>
<br>
群体行为管理器可以动态地改变世界中NPC的策略<br>
<br>
某个区域中存在两个NPC可以触发检查策略，就会为其分配检查策略并改变他们的行为，此部分的具体实现会在后半部分中详细描述<br>
<br>
使用任务(Mission)直接配置群体行为<br>
<br>
在任务区域对指定的任务NPC配置所需要的逻辑，可以在群体行为的框架下实现所需要的表现<br>
<br>
<strong>（4）动画中的注意事项</strong><br>
<br>
<div align="center">
<img aid="1031553" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091306d7waca4sjd6zjchl.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091306d7waca4sjd6zjchl.jpg" width="600" id="aimg_1031553" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091306d7waca4sjd6zjchl.jpg" referrerpolicy="no-referrer">
</div><br>
主讲人用《看门狗2》中的入侵隐私任务举例，总结了一些需要注意的点（部分要点不止运用在群体行为之中，如动画融合等）：<br>
<br>
<ul><li>对于特殊的事件配置不同的先决条件，允许玩家改变顺序完成任务，并根据玩家自己的行为看到不同的表现【注意】此句理解可能存在一些问题，酌情观看</li><li>设置大量的计时器优化表现</li><li>保证动画融合中不会滑步等错误表现</li><li>保证动画本身随时可以进行融合，可以通过对应的动画有相同的Idle动画来实现</li><li>保证动画融合不会出现跨状态融合，如持枪时不会强行播放非持枪的动画<br>
</li></ul><br>
<strong><font color="#de5650">上半场总结</font></strong><br>
<br>
上半场中更多地是从设计的角度，从整个群体行为系统的来龙去脉讲起，叙述了群体行为系统的组成部分，粗略地描述了一下调用的层级。上半场中讲述的内容很多是比较常识性的知识，更类似于科普。<br>
<br>
个人认为，下半场中的内容更加干货一些，可以直接了解到这套系统的配置方式、枚举类型、数据结构等等，并且描述了对应所需要的工具流，更偏向于实现。<br>
<br>
<strong><font color="#de5650">《看门狗：军团》中的群体行为</font></strong><br>
<br>
第二段的演讲由程序老哥分享，首先概括了群体行为系统最终达成的效果和遇到的挑战。<br>
<br>
<div align="center">
<img aid="1031554" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091314se8m4zrzwevo2whx.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091314se8m4zrzwevo2whx.jpg" width="600" id="aimg_1031554" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091314se8m4zrzwevo2whx.jpg" referrerpolicy="no-referrer">
</div><br>
《看门狗：军团》最终应用群体行为系统控制开放世界中的NPC，并强化了一部分NPC行为的有趣程度以吸引玩家的关注，更好地构筑Play-As-Anyone的游戏主题，此外，群体行为系统也提供了一部分的游戏性，如玩家的行为会影响NPC对其的态度等。<br>
<br>
开发群体行为系统遇到的挑战包括：<br>
<br>
<ul><li>高度交互性——可交互对象极多</li><li>一致性/连贯性——保证NPC做出的反应是合理的</li><li>鲁棒性——确保NPC即使在无输入的情况下也能够处理突发事件<br>
</li></ul><br>
最终的目标是保证群体行为在有大量输入的情况下也能产生逻辑自洽的表现。<br>
<br>
以上的挑战都可以在上半场分享中找到对应的需求以及情境<br>
<br>
下面将会分层次的介绍群体行为系统的组成部分：<br>
<br>
<strong><font color="#de5650">分支Branch</font></strong><br>
<br>
<div align="center">
<img aid="1031555" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091321fowdw6ioff6zllt5.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091321fowdw6ioff6zllt5.jpg" width="600" id="aimg_1031555" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091321fowdw6ioff6zllt5.jpg" referrerpolicy="no-referrer">
</div><br>
分支用来描述群体行为系统如何对外界刺激做出反应。每个策略存在多个分支，每个分支指定了一条规则，规则对应输入的事件。当对应事件发生时，将匹配分支中对应的规则，改变当前的行为。<br>
<br>
当前策略发生改变时，可用分支也会随之改变，不再响应原有分支中的事件。<br>
<br>
这样的设计允许策略设计者准确地指定某一个状态下会对哪些事件做出反馈。<br>
<br>
<strong><font color="#de5650">反应矩阵</font></strong><br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1031556" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091327p55sgn5gz55gghkv.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091327p55sgn5gz55gghkv.jpg" width="600" id="aimg_1031556" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091327p55sgn5gz55gghkv.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">现有的反应架构</font></font></div><br>
从上文不难发现，在开放世界这样充满了各种种类的可触发事件（在《看门狗：军团》中有近400种，包括了声音、天气、表情、动作、投掷物等等）的环境中，对每一种具体反应都设定对应的分支这样的工作量是不现实的。因此，单独的NPC对给定刺激的反应结果由反应矩阵（the Reaction Matrix）所定义。<br>
<br>
反应矩阵包含输入与输出两部分，输入包括刺激类型、AI种类、情境信息等，输出包括后续跳转的AI状态、需要播放的动画、需要进行的对话等等。<br>
<br>
反应矩阵的配置结构可以参考图片中的表格，左侧为所有的输入，包括当前行为、触发事件、事件的发送者与接收者等等，右侧为所有可能做出的行为，如NPC在行走时，附近存在Insult事件，且发送者不是敌人，目标不是自己的朋友的情况下，不可能触发到攻击行为。《看门狗：军团》中实际运用的反应矩阵可以达到1200行。<br>
<br>
反应矩阵的输入部分允许空值，这将匹配对应单元格所有类型的输入。反应矩阵最终的选择逻辑将会确保有最少的空值匹配，选中最具体的结果。<br>
<br>
关于反应矩阵的详细内容，可以翻阅GDC 2017：Helping It All Emerge: Managing Crowd AI in 'Watch Dogs 2'<br>
<br>
<strong><font color="#de5650">将反应矩阵的结果作为新的输入</font></strong><br>
<br>
<div align="center">
<img aid="1031557" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091334r8zfbvrqqoqmtv1t.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091334r8zfbvrqqoqmtv1t.jpg" width="600" id="aimg_1031557" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091334r8zfbvrqqoqmtv1t.jpg" referrerpolicy="no-referrer">
</div><br>
上文中的反应矩阵是作用于单独的NPC上的，当单独的NPC作为群体行为的成员时，仍然会使用反应矩阵评估其受到的刺激，但反应矩阵输出的结果将不会实际执行，而是作为一个中间值传递给群体行为系统的分支系统。<br>
<br>
分支中配置的输入与反应矩阵类似，但分支中配置的输入类型将会更少，且分支的输出将会指定群体行为该如何做出反应。<br>
<br>
即当NPC位于群体行为中时，NPC所做出的的反应将由NPC的反应矩阵与当前群体行为策略的分支共同决定，且分支将覆盖反应矩阵的结果。<br>
<br>
分支可以指定的行为包括：<br>
<br>
<ul><li>播放反应矩阵指定的行为</li><li>覆盖当前动画或指定下一个状态</li><li>无视发生的事件</li><li>进入新的策略<br>
</li></ul><br>
通过这些行为可以达成大多数的设计目的，如同步多个NPC的行为，做出特殊的应对等等。<br>
<br>
以上包括个人理解，可能与原文存在差异<br>
<br>
<strong><font color="#de5650">分支类型</font></strong><br>
<br>
<div align="center">
<img aid="1031558" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091334pyygy7fz7488y5ey.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091334pyygy7fz7488y5ey.jpg" width="600" id="aimg_1031558" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091334pyygy7fz7488y5ey.jpg" referrerpolicy="no-referrer">
</div><br>
可以配置如下的分支类型：<br>
<br>
<strong>无视Ignore</strong><br>
<br>
无视输入并继续当前策略，一般用于防止低优先级的事件打断当前高优先级的事件<br>
<br>
<strong>分支Branch&返回Return</strong><br>
<br>
可以理解为在当前策略的基础上额外进行一个行为后返回到原来的行为中<br>
<br>
如检查身份时，玩家过于靠近，NPC将会转向玩家并对其进行警告，然后继续之前的行为<br>
<br>
<strong>Hard Bail</strong><br>
<br>
终止当前策略，解除群体行为系统对NPC的控制，NPC将采取反应矩阵指定的行为<br>
<br>
通常用于爆炸、枪击等事件中<br>
<br>
<strong>Soft Bail</strong><br>
<br>
用于当前策略不再有效，会执行完毕当前分支中的行为后再结束当前策略<br>
<br>
不会突兀地结束，会执行当前分支中的行为（一般Soft Bail中的行为会设置为当前情境信息与事件对应的结束行为）<br>
<br>
<strong><font color="#de5650">分支的选择</font></strong><br>
<br>
<div align="center">
<img aid="1031559" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091335c640m6mfj72m93zv.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091335c640m6mfj72m93zv.jpg" width="600" id="aimg_1031559" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091335c640m6mfj72m93zv.jpg" referrerpolicy="no-referrer">
</div><br>
分支使用有序列表进行储存，并按顺序进行评估，优先匹配最先到达的分支。个人认为此处存在一定的配置规则，如提前定义某些情况的优先级，确定匹配空值的分支在列表中的顺序等<br>
<br>
优点：更容易定义规则之间的优先级<br>
<br>
缺点：即使分支中的输入类型已经简化过，粒度还是很细<br>
<br>
<strong><font color="#de5650">如何设置分支</font></strong><br>
<br>
<div align="center">
<img aid="1031560" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091336or4ph1ywrgbbiogm.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091336or4ph1ywrgbbiogm.jpg" width="600" id="aimg_1031560" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091336or4ph1ywrgbbiogm.jpg" referrerpolicy="no-referrer">
</div><br>
可以在策略级别定义分支，也可以在块级别定义分支。优先评估块内的分支，后续评估策略级的分支。<br>
<br>
参见上半场中策略部分，策略包含多个块<br>
<br>
此处举例说明了两种不同的定义方式的区别，并且讲述了Soft Bail的应用方式。<br>
<br>
当军官NPC正在逮捕一名平民时，当前处于逮捕策略内，执行扣押这个块的行为。当出现无人机时，需要确保NPC不会被群体行为系统束缚住，可以正确地执行被攻击时的应激反应，为了达成这个目的，一般会在策略级别配置Hard Bail分支，确保存在一个保底的被攻击行为。但对于某些情况，NPC直接停止一切操作（不会存储之前进行的行为）是不符合预期的，因此，可以使用更高优先级的块分支，配置Soft Bail，在退出当前策略之前，会将被逮捕的平民进行标记，这样在结束突发的攻击行为后，军官NPC还可以继续之前的逮捕行为。<br>
<br>
<strong><font color="#de5650">分支的存储与复用</font></strong><br>
<br>
<div align="center">
<img aid="1031561" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091340zqq342142sd124n2.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091340zqq342142sd124n2.jpg" width="600" id="aimg_1031561" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091340zqq342142sd124n2.jpg" referrerpolicy="no-referrer">
</div><br>
《看门狗：军团》开发结束时存在近200种不同的群体行为策略，不同的策略之间复用和共享了大量的分支逻辑。<br>
<br>
为了存储分支以便更好地复用与检验，建立了分支数据库。可以在分支数据库中创建可命名的对象，每个对象中存储一个分支规则的列表。围绕一些经常需要复用的特征管理这些对象，使其可以在任意策略中被复用。<br>
<br>
复用后的分支仍遵循从最具体到最不具体的先后顺序，被引入的数据库分支在执行顺序上弱于自定义分支<br>
<br>
个人理解即是在原有的单独定义的块级分支与策略级分支之上，添加了一个层：数据库级分支，块分支和策略级分支可以直接调用某些数据库分支，无需再重新配置。<br>
<br>
<div align="center">
<img aid="1031562" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091341y5bvpn4n90xb93xv.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091341y5bvpn4n90xb93xv.jpg" width="600" id="aimg_1031562" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091341y5bvpn4n90xb93xv.jpg" referrerpolicy="no-referrer">
</div><br>
此处举例说明数据库分支如何在群体行为中被复用。当出现破坏性黑客事件时，仍旧是先块分支后策略分支。首先执行块分支中的自定义部分，之后执行块中引用的数据库分支，接下来执行策略分支中的自定义部分，然后执行策略引用的数据库分支。<br>
<br>
<strong><font color="#de5650">分支的先决条件</font></strong><br>
<br>
<div align="center">
<img aid="1031563" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091347tlue2jelleulzuuc.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091347tlue2jelleulzuuc.jpg" width="600" id="aimg_1031563" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091347tlue2jelleulzuuc.jpg" referrerpolicy="no-referrer">
</div><br>
在运行时打开和关闭分支能够更好地调试群体行为，《看门狗：军团》使用了上半场群体行为系统中2(2)模块化中与其相同的方案，向分支中添加了先决条件(Precondition)，以增加当群体情境信息改变的粒度（increase the granularity of changes to the group context）。<br>
<br>
虽然先决条件的引入增加了设置单个分支的复杂度，但其可以让策略的设置得到简化，当某些必要性质的条件发生改变时，就无需再执行后面的策略，直接禁用部分分支。<br>
<br>
<strong><font color="#de5650">群体行为黑板</font></strong><br>
<br>
<div align="center">
<img aid="1031564" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091358bkr9aej63kb9q9xa.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091358bkr9aej63kb9q9xa.jpg" width="600" id="aimg_1031564" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091358bkr9aej63kb9q9xa.jpg" referrerpolicy="no-referrer">
</div><br>
上述的先决条件和群体情境信息都可以储存在黑板中。<br>
<br>
此处的黑板与我们熟知的AI中黑板的概念相同，以Key-Value的形式存储AI所需要的全部配置值。黑板值在运行时被更新，而AI系统可以监听黑板值的变化以选择对应的行为。<br>
<br>
<strong><font color="#de5650">实例演示</font></strong><br>
<br>
该视频片段举例说明了一个完整的群体行为是如何配置并工作的：<br>
<br>
<div align="center">
<img aid="1031565" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091403yz4np50lr5g5kgpi.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091403yz4np50lr5g5kgpi.jpg" width="600" id="aimg_1031565" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091403yz4np50lr5g5kgpi.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">此处为一段视频，可以去GDC官网查看</font></font></div><br>
军官NPC正在进行身份检查，玩家的目标是分散其注意力。为了完成这个行为，需要定义一个“被吸引注意力”的行为种类，并将其“平民逃跑”设置为默认行为，当玩家尝试吸引其注意力时就会触发这个行为。<br>
<br>
每个策略块实际上并不是指向某个特定的行为本身，而是指向一个行为种类 (Behavior Categories)<br>
<br>
每个行为种类存在一个默认的行为，在通常情况下，调用策略块实际上会调用对应的默认行为<br>
<br>
以上为上半场中模块化的部分内容<br>
<br>
这个默认行为按照顺序进行对应的动作，包括改变AI状态、播放动画、播放语音等等<br>
<br>
<div align="center">
<img aid="1031566" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091408tvw7nnynwwg6vrnr.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091408tvw7nnynwwg6vrnr.jpg" width="600" id="aimg_1031566" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091408tvw7nnynwwg6vrnr.jpg" referrerpolicy="no-referrer">
</div><br>
为了复用这个新创建的行为，需要创建一个新的分支数据库对象，并设置对应的规则以指向这个行为。示例中设置了三条规则：<br>
<br>
1.SoftBail至本次新定义新的行为种类<br>
<br>
2.无视针对平民的黑客行为——此处主讲人提到，玩家也会评估当前所有的活动分支，若某个行为对应的分支不会做出反应，则会禁用玩家对应行为的UI（如黑客UI）个人认为这里可以看做为一种判断当前UI是否展示的解决办法，既没有强制写死的禁用某个功能，又在游戏性和功能性里找到了平衡<br>
<br>
3.当平民已经被铐住时（先决条件达成），SoftBail至另外的结尾行为<br>
<br>
<div align="center">
<img aid="1031567" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091411pa82tn37yn7ei851.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091411pa82tn37yn7ei851.jpg" width="600" id="aimg_1031567" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091411pa82tn37yn7ei851.jpg" referrerpolicy="no-referrer">
</div><br>
下面介绍了三种不同的规则实际的配置与触发方式：<br>
<br>
<strong>规则1</strong><br>
<br>
<div align="center">
<img aid="1031568" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091413ffutuj8tzt8bzcta.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091413ffutuj8tzt8bzcta.jpg" width="600" id="aimg_1031568" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091413ffutuj8tzt8bzcta.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>触发事件：</strong><br>
<br>
OnBeingHacked当被骇入时<br>
<br>
<strong>先决条件：</strong><br>
<br>
事件接收者为军官NPC<br>
<br>
黑板值IsArrested为False（平民未被逮捕）<br>
<br>
<strong>结果：</strong><br>
<br>
SoftBail至上文定义的新行为种类中<br>
<br>
<strong>规则2</strong><br>
<br>
<div align="center">
<img aid="1031569" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091414j2iwo2voyysm8p88.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091414j2iwo2voyysm8p88.jpg" width="600" id="aimg_1031569" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091414j2iwo2voyysm8p88.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>触发事件：</strong><br>
<br>
OnBeingHacked当被骇入时<br>
<br>
<strong>先决条件：</strong><br>
<br>
事件接收者为平民NPC<br>
<br>
黑板值IsArrested的要求为空，即都可以匹配<br>
<br>
<strong>结果：</strong><br>
<br>
无视本次行为<br>
<br>
<strong>规则3</strong><br>
<br>
<div align="center">
<img aid="1031570" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091415is8s330r5k5pzwlg.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091415is8s330r5k5pzwlg.jpg" width="600" id="aimg_1031570" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091415is8s330r5k5pzwlg.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>触发事件：</strong><br>
<br>
OnBeingHacked当被骇入时<br>
<br>
<strong>先决条件：</strong><br>
<br>
黑板值IsArrested为True（平民已被逮捕）<br>
<br>
<strong>结果：</strong><br>
<br>
SoftBail至平民被逮捕的结尾行为中<br>
<br>
<strong><font color="#de5650">进阶操作</font></strong><br>
<br>
<div align="center">
<img aid="1031571" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091416acg28x2vc5bfzp81.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091416acg28x2vc5bfzp81.jpg" width="600" id="aimg_1031571" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091416acg28x2vc5bfzp81.jpg" referrerpolicy="no-referrer">
</div><br>
在《看门狗：军团》存在让NPC展示自己具有的能力的需求，为了让这个有打拳能力的NPC展示出不一样的行为，需要为他定义一个特殊的行为，并将其添加到之前已经建立好的行为种类中。<br>
<br>
<strong><font color="#de5650">近战击倒行为</font></strong><br>
<br>
<div align="center">
<img aid="1031572" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091417gdv7c7ffncsdpssd.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091417gdv7c7ffncsdpssd.jpg" width="600" id="aimg_1031572" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091417gdv7c7ffncsdpssd.jpg" referrerpolicy="no-referrer">
</div><br>
创建好这个行为后，为其定义特殊的先决条件：平民是否有近战能力（包括多种近战能力，平民NPC上不同的Tag都可以触发这个条件）<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1031573" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091419cnxi7wqfaxnriz9k.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091419cnxi7wqfaxnriz9k.jpg" width="600" id="aimg_1031573" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091419cnxi7wqfaxnriz9k.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">一段视频，可以去GDC官网查看</font></font></div><br>
<strong><font color="#de5650">工具流</font></strong><br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1031574" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091429j3j5yzrmb5sdbr34.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091429j3j5yzrmb5sdbr34.jpg" width="600" id="aimg_1031574" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091429j3j5yzrmb5sdbr34.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《看门狗：军团》的分析工具</font></font></div><br>
对这样的群体行为系统进行调试需要大量的工具和人力，且工具开发在整个游戏的开发过程中很难获得更多的资源。《看门狗：军团》的调试工具不够完善，但基础功能应该比较完整，包括录屏、逐帧跟踪、查看当前活动分支等。<br>
<br>
<strong><font color="#de5650">动捕相关与小贴士</font></strong><br>
<br>
<div align="center">
<img aid="1031575" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091433oen9ezq24ve5ie4w.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091433oen9ezq24ve5ie4w.jpg" width="600" id="aimg_1031575" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091433oen9ezq24ve5ie4w.jpg" referrerpolicy="no-referrer">
</div><br>
该部分讲述的内容主要是动捕中的注意事项，比较常规，包括提前做好准备、匹配对应的Pose、动捕现场需要有TA在场等等<br>
<br>
<div align="center">
<img aid="1031576" zoomfile="https://di.gameres.com/attachment/forum/202202/24/091440fdzd10o4rc4lb0wg.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/091440fdzd10o4rc4lb0wg.jpg" width="600" id="aimg_1031576" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/091440fdzd10o4rc4lb0wg.jpg" referrerpolicy="no-referrer">
</div><br>
增加工具与配置的易用性可以极大地增加效率与产出<br>
<br>
<div align="center">
<img aid="1031591" zoomfile="https://di.gameres.com/attachment/forum/202202/24/092104h3rhvh45rk6em439.jpg" data-original="https://di.gameres.com/attachment/forum/202202/24/092104h3rhvh45rk6em439.jpg" width="600" id="aimg_1031591" inpost="1" src="https://di.gameres.com/attachment/forum/202202/24/092104h3rhvh45rk6em439.jpg" referrerpolicy="no-referrer">
</div><br>
可行的话复用其他游戏（自家的）的动作，也可以使用已有资源和功能增加一些不错的小东西<br>
<br>
<strong><font color="#de5650">个人总结与碎碎念</font></strong><br>
<br>
这篇分享从落笔到完成用了一个月，其实远远用不到这么久，大概也就两天的量，但是断断续续一直也没有完成。第一次翻译这么长的东西，我高考都没翻译过这么长（。部分内容确实也是找不到更合适的词语进行翻译了，因此可能读起来翻译腔会很重，请多见谅。此外，下半场的翻译多少有点摆了，格式与英文原文没有上半场全面。<br>
<br>
分享的上半场主要是从设计角度，个人认为最重要的部分是组成元素与模块化两个部分，与下半场中相互对照，可以很清晰地梳理出整个系统的层次，并且分享了一部分配置相关的内容，相信可以根据这个思路在对应的游戏中复刻这套系统。<br>
<br>
<strong>适用范围窄</strong><br>
<br>
超大型开放世界单机游戏，如GTA等<br>
<br>
需要构建NPC的背景与人设的游戏<br>
<br>
不适用于战斗比重远大于探索比重的游戏<br>
<br>
<strong>配置量极大</strong><br>
<br>
想要达到分享中的效果，需要大量的配置<br>
<br>
《看门狗：军团》中的配置个人猜想有一部分是前作等游戏中的积累<br>
<br>
<strong>其他</strong><br>
<br>
感谢 一袋甜蕉宋球长 的文章，使用了文章中的链接布局，指路<br>
<br>
如有疏漏或翻译优化建议可以在评论区指出<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">原文：https://zhuanlan.zhihu.com/p/463560068</font></font><br>
<br>
  
</div>
            