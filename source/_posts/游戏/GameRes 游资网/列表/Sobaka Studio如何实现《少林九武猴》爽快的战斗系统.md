
---
title: 'Sobaka Studio如何实现《少林九武猴》爽快的战斗系统'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202101/26/134832immgbm8amkmm98j8.jpg'
author: GameRes 游资网
comments: false
date: Tue, 26 Jan 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202101/26/134832immgbm8amkmm98j8.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2483355">
<i><font color="#808080">Sobaka Studio现任当家人Dmitry Kachkov出生于俄罗斯波罗的斯克。他从IT专业毕业并获得学位，曾参与开发各种游戏，包括《SmashCars》、《仓鼠球（HamsterBall）》PS3版和《Frontline Commando》。他曾为多家电子游戏公司工作，包括Creat Studio、Sperasoft和Glu Mobile。在2016年他成立了Sobaka Studio。这家开发商的第一个作品是清版射击游戏《救世主》。继首款作品成功之后，Dimitry Kachkov和他的团队又在2020年秋发售了武打片风格的清版动作游戏《少林九武猴》。</font></i><br>
<br>
大家好。我是Sobaka Studio的创始人Dmitry Kachkov。我们的小团队开发清版过关独立游戏已经有五年多了。这类游戏的游戏性往往与其战斗系统密不可分。你们中间很多人可能都已经注意到，在那些著名的清版过关游戏中，妙趣横生、千变万化、节奏明快的战斗往往比情节或环境更吸引玩家。<br>
<br>
我们的游戏《救世主（Redeemer）》和新近发售的《少林九武猴（9 Monkeys of Shaolin）》也是如此。我们的这两款游戏都被评论家称赞战斗系统出色。我将这种类型的战斗系统形容为“有嚼头”，我将尝试定义它的含义，并介绍我们是如何在我们的游戏中实现的。<br>
<br>
在《救世主》中，我们的硬汉僧侣Vasiliy经常需要用自己的双手把敌人扔到尽可能远的地方，而在《少林九武猴》中，主角用一根棍棒与大批敌人战斗，需要在游戏的技能发展系统中精进自己的战斗能力。<br>
<br>
这两款游戏中的这种饱和感和战斗的“嚼头”都是通过内部开发的连招攻击实现的。所以就来深入了解一下，我们是如何使用虚幻引擎做到这一点的。<br>
<br>
<div align="center"><span id="swf_CGG"></span></div><br>
<strong><font color="#de5650">连招攻击组件配置</font></strong><br>
<br>
一开始，“连招攻击”组件只是播放一个攻击/命中动画，但是在动画开始播放时，还有许多附加的条件、事件和触发器。这就是我们为了把战斗做得有嚼头而需要实现的各个部分。我们在这方面的开发已经进行了很长时间，现在它已经发展成一套很大的系统，而且由无数项附加设置决定。现在，我们只须调整一两个选项，就能把普通的动画播放变为一套复杂的动作序列。<br>
<br>
在我开始讲解内部功能之前，我们先来看看，怎样在UObject子类中设置每种连招攻击。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_956654" aid="956654" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134832immgbm8amkmm98j8.jpg" data-original="https://di.gameres.com/attachment/forum/202101/26/134832immgbm8amkmm98j8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134832immgbm8amkmm98j8.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">连招攻击调整的示例</font></font></div><br>
用来实现连招攻击的设置可以分为几类：<br>
<br>
<ul><li>动画：角色和武器动画。</li><li>设计：这些是游戏性设置，例如伤害、暴击率、流血伤害、格挡攻击的几率，等等。我们还保留了一系列攻击统计修改器，玩家会在游戏过程中逐步得到它们。</li><li>攻击：这些设置与攻击序列和动画相关：有效杀伤半径，负责命中追踪的骨骼名称，与敌人的距离（角色在多近的距离可以发动攻击，等等）。调整这些设置是动画师的工作。</li><li>充能打击：这用于强力打击设置（例如玩家长按攻击按钮来执行攻击时）。例如，这可以确定在充能时要播放什么特效，以及对于充能的打击要使用何种打击。</li><li>连招：如果玩家在攻击动画播放时连续按按钮，可以延续当前连招的攻击。</li><li>命中：这些设置定义攻击成功的情况下敌人受到的伤害多少，以及将要播放的受击动画。换句话说，这里是烟雾、火焰等效果的存储粒子设置，以及音频文件、敌人闪烁、摄像机晃动、冻结和描述敌人挨打后反应的蓝图?（硬直动画）的链接。以我们的游戏为例，它就是敌人倒地不起的一段时间，等等。<br>
</li></ul><br>
<strong><font color="#de5650">攻击动画</font></strong><br>
<br>
我们广泛使用了动画通知?（以下简称为通知）来调节和平衡游戏性，以及实现画面和声音变化。现在为初学者介绍一下基本的游戏性通知。游戏设计师和动画师都可以利用这种通知精心打磨优秀玩法的每一个细节。<br>
<br>
<div align="center">
<img id="aimg_956655" aid="956655" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134832hhotohutm65hufu0.jpg" data-original="https://di.gameres.com/attachment/forum/202101/26/134832hhotohutm65hufu0.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134832hhotohutm65hufu0.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">冲刺通知</font></strong><br>
<br>
在攻击时，玩家可以冲向敌人。这样就有了三个阶段：起始动画，向敌人的移动，以及打击。如果敌人离玩家很近，那么移动阶段就非常短，或者完全不存在（例如，玩家按下按钮时角色就会击中敌人）。如果对这个序列来说，敌人离得有点远，那我们就播放起始动画，暂停该动画，使玩家向敌人移动，取消暂停动画，然后播放击打动画。为了暂停和取消暂停动画，我们使用了通知，这使我们的动画师不必手动处理玩家与敌人的距离。<br>
<br>
考虑到这一点，我们将通知准确设置在动画应该暂停的时间，为了让玩家有机会先冲刺到能够到敌人的地方，这是必须的。我们准确计算了这些通知的时间点，使角色不会长时间停滞。尽管如此，为了保证效果，玩家还是必须停滞一下。在组件中实现冲刺的方式是对玩家的最大速度作基本的乘法，并强制朝冲刺目标点的方向（例如，朝向自动瞄准的目标）推过去。<br>
<br>
<strong><font color="#de5650">命中区域通知</font></strong><br>
<br>
在攻击动画的某个时间点，AOEAttackState状态会开启。AOE代表范围效果。这种状态会激活武器命中区域（有时候会放大很多）中近似的命中光线追踪计算，以判定敌人是否被击中。<br>
<br>
AOEAttackState不仅登记对敌人的命中，而且它本身也是一个独立的特殊StrikeHit动画通知。当通知被激活时，在玩家角色前方一定半径内的敌人就会被强制受到伤害。所有命中设置（例如AOE状态中的追踪和strikeHit活动期间的命中区域）都存储在当前连招攻击的蓝图中。设计师可以在该蓝图中精细调整不同打击的命中。<br>
<br>
<strong><font color="#de5650">切换到下一个攻击通知</font></strong><br>
<br>
在命中动画播放期间，可以显示一个ShortTick动画通知（瞬时命中）。当ShortTick通知被触发时，系统会检查当前攻击开始时攻击按钮是否被按下。如果被按下了，那么这次攻击后就会连接下一次攻击，这也是在连招攻击蓝图中配置的。换句话说，攻击的蓝图包含指向其他攻击蓝图的链接，而只有在ShortTick激活的那一刻攻击按钮被按下的情况下其他攻击蓝图才会被触发。请注意，为了精细调整连招的时机，可以多次设置ShortTick。<br>
<br>
<strong><font color="#de5650">取消通知</font></strong><br>
<br>
取消通知会结束攻击动画设置。这类通知设置在发生新事件时可以取消动画的情况。如果玩家按下移动按钮或者受到伤害，就可能触发此类事件。例如，如果超重击处于活动状态，较弱的敌人就无法通过自身的攻击将其打断。但是一旦活动阶段结束，玩家模型的漂亮动画即将完结，此时如果受到伤害，就会打断攻击的动画，转而播放受击动画。<br>
<br>
<strong><font color="#de5650">充能攻击通知</font></strong><br>
<br>
我们游戏中的大部分战斗招式都有“充能”版本（例如当玩家按住攻击按钮不放时，角色就会打出强力攻击，造成更多伤害）。虽然这款游戏的击打速度很快，而且也应该快速执行攻击，不过玩家可以将攻击按钮按住较长时间来执行“充能”攻击。因此，为了不让玩家处于被动的充能状态，我们设计了一条动画减速曲线，它会在玩家按住攻击按钮时激活。在这种情况下，动画的速度就会放慢，当积累了必要的能量时，就会出现特殊的视觉效果，此时命中会造成双倍伤害。<br>
<br>
<div align="center">
<img id="aimg_956656" aid="956656" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134833zxojdm3wnpjoijnv.jpg" data-original="https://di.gameres.com/attachment/forum/202101/26/134833zxojdm3wnpjoijnv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134833zxojdm3wnpjoijnv.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">其他通知</font></strong><br>
<br>
除了上述游戏性通知外，我们还有负责攻击的声音和画面部分的通知。有了它们，系统才是完整的。<br>
<br>
仅仅一次攻击就包含一系列声音效果，例如：武器击打声、玩家脚步声、攻击时的叫声、玩家攻击后的落地声，等等。我们游戏中的每个角色都有相同的人形骨骼，因此许多角色可以有相同的攻击动画。但是，不同的声音和效果设置可以大大改变玩家对一次攻击的感受。<br>
<br>
<strong><font color="#de5650">命中反应</font></strong><br>
<br>
如果检测到敌人被命中，那么就应该有一个反应来给玩家提供某些反馈。一般来说，反馈越强越好。但与此同时，这种反应必须是设计师能够管理的。<br>
<br>
<div align="center">
<img id="aimg_956657" aid="956657" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134834rjwedx21w62jyja1.jpg" data-original="https://di.gameres.com/attachment/forum/202101/26/134834rjwedx21w62jyja1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134834rjwedx21w62jyja1.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">每个连招攻击都包含描述命中时反应的蓝图。</font></font></div><br>
在下面的屏幕截图中，你可以看到敌人分为三种类型：轻型、中型和重型。因此我们可以给同一种命中设置不同的反应，供不同的敌人使用。<br>
<br>
<div align="center">
<img id="aimg_956658" aid="956658" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134837pcr3p8cjbymturlj.jpg" data-original="https://di.gameres.com/attachment/forum/202101/26/134837pcr3p8cjbymturlj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134837pcr3p8cjbymturlj.jpg" referrerpolicy="no-referrer">
</div><br>
这种办法并不能立竿见影地解决问题。最初，我们尝试在每个敌人的蓝图中设置命中与对该命中的反应之间的关联，但是在这种情况下，我们不得不枚举所有类型的攻击，这可能有数百种之多。这需要花很长时间设置，而且很容易出错。<br>
<br>
然后我们尝试设置敌人的命中反应的类，但是这反而又带来了一个问题：必须在每种命中反应中枚举许多敌人，另一方面，在创建新类时还不能忘记添加它们。<br>
<br>
为了简化创建此类链接的过程，我们将敌人分成四种：轻型、中型、重型和特殊类型。特殊类型的敌人使用特殊方法处理命中，而普通敌人根据自身类型选择一种动画及其设置。在这方面，反应动画可能不仅是持续时间不同，还可能在敌人动作的受阻和反击上有所不同。例如，重型敌人可以运行受击动画，但如果他决定攻击，还可以随时中断该动画。请参见下面的GIF。<br>
<br>
<div align="center">
<img id="aimg_956659" aid="956659" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134838ic27n5k8xd6aq0o7.gif" data-original="https://di.gameres.com/attachment/forum/202101/26/134838ic27n5k8xd6aq0o7.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134838ic27n5k8xd6aq0o7.gif" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_956660" aid="956660" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134840q0ll0c9c35swerls.gif" data-original="https://di.gameres.com/attachment/forum/202101/26/134840q0ll0c9c35swerls.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134840q0ll0c9c35swerls.gif" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_956661" aid="956661" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134842w9i9ui9qwdo8m9tr.gif" data-original="https://di.gameres.com/attachment/forum/202101/26/134842w9i9ui9qwdo8m9tr.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134842w9i9ui9qwdo8m9tr.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">华丽效果与反馈</font></strong><br>
<br>
有多种辅助效果可以帮助玩家得到更生动的印象。<br>
<br>
<div align="center">
<img id="aimg_956662" aid="956662" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134844imeffekoomavm2r1.gif" data-original="https://di.gameres.com/attachment/forum/202101/26/134844imeffekoomavm2r1.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134844imeffekoomavm2r1.gif" referrerpolicy="no-referrer">
</div><br>
<strong>摄像机晃动。</strong>我们可以给敌人的受击和玩家的受击分配摄像机晃动。在大多数情况下，这是玩家只能勉强察觉的晃动，但在我们认为玩家遭到很强力的打击时，这种效果也会变强。<br>
<br>
<strong>粒子效果。</strong>我们认为不同的效果很重要。除了命中效果（棍棒攻击、风吹和气功），我们还设置了多种击中敌人时的效果。在我们看来，给特别重要的打击分配不同的命中类型是值得的，例如在敌人仅仅受到伤害和敌人被一击毙命时就应该有所不同。为了让游戏看起来更华丽，我们往往会特意搞一些夸张的设置。<br>
<br>
<strong>微冻结。</strong>除了粒子效果和摄像机晃动，微冻结也是我们的战斗系统中一个非常重要的部分。实际上，它们被用于大量顶级动作游戏。微冻结就是角色和敌人的动画停止一小段时间。这可以给每次命中增加额外的质感。当然，每次命中本身都会精心计算这种效果的持续时间。当玩家杀死某个敌人时，这种效果的持续时间就比简单的命中要长，如果杀死的是一场战斗中的最后一个敌人，则会持续更长时间，仿佛我们给这场战斗画下了句号。<br>
<br>
<div align="center">
<img id="aimg_956663" aid="956663" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134846g66wbfwfo9p66uzu.jpg" data-original="https://di.gameres.com/attachment/forum/202101/26/134846g66wbfwfo9p66uzu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134846g66wbfwfo9p66uzu.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">《少林九武猴》中的新特色</font></strong><br>
<br>
为了突出《少林九武猴》的设计特色，我们对战斗系统应用了多项创新。<br>
<br>
<strong>武器动画：</strong>动画师使武器动画与角色的受击动画同步。<br>
<br>
<div align="center">
<img id="aimg_956664" aid="956664" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134847nwml4kzsaklcscy0.gif" data-original="https://di.gameres.com/attachment/forum/202101/26/134847nwml4kzsaklcscy0.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134847nwml4kzsaklcscy0.gif" referrerpolicy="no-referrer">
</div><br>
<strong>计算武器移动轨迹的击中追踪：</strong>在我们的游戏中，击中动画是非常快的，可能只持续数帧；与此同时，武器可能继续运动，甚至会穿过敌人。为了避免出现这种行为，我们计算了武器的运动路线，并将它分为几段。然后，我们在每一段都检查武器是否与敌人相交。<br>
<br>
<div align="center">
<img id="aimg_956665" aid="956665" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134850bfogtve7gyefbyqg.gif" data-original="https://di.gameres.com/attachment/forum/202101/26/134850bfogtve7gyefbyqg.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134850bfogtve7gyefbyqg.gif" referrerpolicy="no-referrer">
</div><br>
<strong>命中增强：</strong>攻击助力：因为攻击包含许多设置，而其中一些与基本的伤害处理有很大不同，我们有办法改进这些特性，并把对它们的控制权交给玩家。例如，我们有一个设置，它负责玩家的自动瞄准并计算玩家与敌人之间的距离来执行攻击。如果增大它的数值，就可以得到非常有趣的结果，甚至能够加强战斗的感觉。<br>
<br>
下面是一次基本踢击的样子。<br>
<br>
<div align="center">
<img id="aimg_956666" aid="956666" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134851o77qftvov2t72os8.gif" data-original="https://di.gameres.com/attachment/forum/202101/26/134851o77qftvov2t72os8.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134851o77qftvov2t72os8.gif" referrerpolicy="no-referrer">
</div><br>
这里是改进的踢击。<br>
<br>
<div align="center">
<img id="aimg_956667" aid="956667" zoomfile="https://di.gameres.com/attachment/forum/202101/26/134853dazj1s110tt8z86t.gif" data-original="https://di.gameres.com/attachment/forum/202101/26/134853dazj1s110tt8z86t.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202101/26/134853dazj1s110tt8z86t.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">总结</font></strong><br>
<br>
团队在攻击、攻击状态和敌人拓扑方面的工作，以及各种动画设置，为我们实现了我们想要开发的有嚼头的战斗。我希望这里介绍的经验对你和你的游戏有用。感谢你抽出时间阅读我们的博文。<br>
<br>
<i><font color="#808080">文中提及的相关链接</font></i><br>
<i><font color="#808080"><br>
</font></i><br>
<i><font color="#808080">[1] 蓝图</font></i><br>
<i><font color="#808080">https://docs.unrealengine.com/zh-CN/ProgrammingAndScripting/Blueprints/index.html</font></i><br>
<i><font color="#808080"><br>
</font></i><br>
<i><font color="#808080">[2] 动画通知</font></i><br>
<i><font color="#808080">https://docs.unrealengine.com/zh-CN/AnimatingObjects/SkeletalMeshAnimation/Sequences/Notifies/index.html</font></i><br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：虚幻引擎</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/PjgqUdACn8SJhux6bLy97A</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            