
---
title: '构建硬核战斗与无缝随机关卡：《生死轮回》的设计与Gameplay技术实现'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202112/08/101634a1kcb0as1ask80ka.jpg'
author: GameRes 游资网
comments: false
date: Wed, 08 Dec 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202112/08/101634a1kcb0as1ask80ka.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2519830">
在今年“Unreal Open Day虚幻引擎技术开放日”（12月2日-3日）大会上，eBrain Studio负责人李伟围绕《生死轮回》和战斗系统和随机地图系统，从开发设计到实现，展开了分享演讲。<br><br><strong>以下是整理后的演讲实录：</strong><br><br>
我叫李伟，是eBrain Studio的负责人。我和我的小伙伴在基于虚幻引擎4开发一款Cyberpunk题材的横版动作Roguelite游戏，叫做《生死轮回》。这是一款故事驱动，以战斗，机关和解谜为游戏性核心的作品，不久面向PC和Console发布。<br><br><div align="center">
<img id="aimg_1023887" aid="1023887" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101634a1kcb0as1ask80ka.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101634a1kcb0as1ask80ka.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101634a1kcb0as1ask80ka.jpg" referrerpolicy="no-referrer">
</div>
<br>
在这款游戏的开发过程中，我担任制作人的角色。主要负责编剧，设计和gameplay编程方面的工作。在此之前，我是orap games的ceo和制作人，以相同的职责基于UDK和虚幻引擎3分别负责了《将死之日》和《忍者龟ol》的开发。<br><br>
今天我要讲的主题，包含两个部分，围绕《生死轮回》的“战斗系统”和“随机地图系统”展开讨论。针对这两个系统，探讨我们是怎么从设计到实现，遇到和解决问题，以及完成和最终打磨与扩展的。<br><br><strong><font color="#de5650">一、战斗系统</font></strong><br><br>
作为一款动作游戏，“战斗系统”的良好呈现是游戏品质的关键。然而“战斗系统” 是一个很泛的主题，因为围绕战斗系统的模块太多，边界时常又是那么模糊。所有内容详细介绍规模太大，逐一涉及不现实，这里我摘取“近战武器”和“受击者反馈”两个核心版块的内容进行陈述。<br><br>
我会采用思考设计，系统罗列，然后逐个详细的探讨他们的技术实现的方式展开。<br><br><strong>近战武器设计 1：技术目标</strong><br><br>
《生死轮回》的基础游戏性是玩家可以使用多样的近战武器与敌人战斗。为了丰富游戏体验和促进战斗追求,我们设计了超过30种特性迥异的近战武器。可以看到武士刀，大锤，长棍，拳头等近战武器。<br><br><div align="center">
<img id="aimg_1023888" aid="1023888" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101635w04s40kkbsblbdkz.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101635w04s40kkbsblbdkz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101635w04s40kkbsblbdkz.jpg" referrerpolicy="no-referrer">
</div>
<br>
如何实现武器的基础伤害功能，拉开不同武器的感受差异是我们的技术实现目标。基于该目标，我们进行分析，达成以上需要我们实现什么功能特性。<br><br><strong>近战武器设计 2：特性分析</strong><br><br>
我们从近战武器的自身特征着手分析：<br><br>
（1）武器形状：每一种武器有其大小不一的形状。我们需要精确的反应其挥舞时候的检测结果。可以让设计师根据武器的外形调整攻击检测范围。<br><br>
（2）目标角色反馈：击中各角色反馈表现不同。如人类会飙血，机器人会蹦出火花。敌人的死亡效果也有所不同，如我们想追求硬核和真实，钝器杀死的敌人会呈现布娃娃效果,利器可以将敌人的肢体切断。<br><br><div align="center">
<img id="aimg_1023889" aid="1023889" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101635ufjojjouevjezlke.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101635ufjojjouevjezlke.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101635ufjojjouevjezlke.jpg" referrerpolicy="no-referrer">
</div>
<br>
（3）表面材质反馈：除了击中角色。我们想像《黑暗之魂》一样，呈现足够的细节，武器打到墙壁上，可以溅起火花。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023890" aid="1023890" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101636ql35krkmx0lrm2gx.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101636ql35krkmx0lrm2gx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101636ql35krkmx0lrm2gx.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">黑暗之魂击中墙壁</font></font></div>
<br>
（4）利器和钝器：利器和钝器的击打感受不同，毫无疑问武士刀和棒球棍在击中目标时的顿感是不同的。前者类似切瓜，后者在击中目标的时刻能感受到阻力。<br><br><div align="center">
<img id="aimg_1023891" aid="1023891" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101637h507nm4ngnggy5ns.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101637h507nm4ngnggy5ns.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101637h507nm4ngnggy5ns.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">武士刀和棒球棍的击中</font></font></div>
<br><strong>近战武器框架</strong><br><br>
带着以上的思考和疑问，我们谈谈近战武器系统每一个环节的具体技术实现。<br><br>
《生死轮回》的Gameplay功能多是以C++实现，牵扯到可视化配置的时候，开放给Blueprints子类。<br><br><div align="center">
<img id="aimg_1023892" aid="1023892" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101637zj6ssssyfs6iridm.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101637zj6ssssyfs6iridm.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101637zj6ssssyfs6iridm.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">武器类C++代码</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023893" aid="1023893" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101637tc99qzzz96y09iqi.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101637tc99qzzz96y09iqi.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101637tc99qzzz96y09iqi.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">武器类蓝图代码</font></font></div>
<br>
这样的好处是，C++可以方便高效的实现算法和功能。Blueprints可以进行强大的可视化定制及直观的调用逻辑。武器系统的实现便是采用这种方式。对于武器类，他的父类继承自AActor。<br><br>
我们在C++中创建SkeletalMeshComponent组件，这样在代码中就可以方便的访问到该组件，实现其线性检测等伤害功能算法。<br><br>
在蓝图中设置武器模型及其物理，以供设计师定制击中粒子反馈，插槽及各项参数。为该武器的SkeletalMesh创建插槽，骨骼插槽可以用来指定每一把武器的检测起始和结束范围。<br><br><div align="center">
<img id="aimg_1023894" aid="1023894" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101638g7q00uizmrjqqz6h.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101638g7q00uizmrjqqz6h.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101638g7q00uizmrjqqz6h.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">刀类近战武器插槽</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023895" aid="1023895" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101638u7glj3l3lppzhawj.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101638u7glj3l3lppzhawj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101638u7glj3l3lppzhawj.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">棍类近战武器插槽</font></font></div>
<br>
下面我们谈谈，近战武器攻击检测的逻辑。<br><br><strong>近战武器检测实现 1：线性检测</strong><br><br>
近战武器挥舞的时候，即是不断的从插槽的一个端点朝目标端点，发出射线，检测扫描碰到物件的过程。<br><br>
实现武器对目标的检测：虚幻引擎4提供了大量特性多样的线性检测API，可以在两点之间发出射线，根据效率和需要的不同返回扫过的物件信息。例如我们使用了该线性检测函数，并对其进行定制封装，<br><br>
bool SweepMultiByChannel(TArray& OutHits, const FVector& Start, const FVector& End, const FQuat& Rot, ECollisionChannel TraceChannel, const FCollisionShape& CollisionShape, const FCollisionQueryParams& Params = FCollisionQueryParams:<img src="https://www.gameres.com/static/image/smiley/default/biggrin.gif" smilieid="3" border="0" alt referrerpolicy="no-referrer">efaultQueryParam, const FCollisionResponseParams& ResponseParam = FCollisionResponseParams::DefaultResponseParam) const;<br><br><div align="center">
<img id="aimg_1023896" aid="1023896" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101639ilejqe9zil6n4ly6.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101639ilejqe9zil6n4ly6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101639ilejqe9zil6n4ly6.jpg" referrerpolicy="no-referrer">
</div>
<br>
简单看看该函数，在该函数的执行结果中，我们可以返回几个重要的参数：<br><br>
- 数组结构TArray& OutHits会返回一系列扫描到的物件信息。这里有一些可以让我们获取更多细节的参数，我们后面会展开讲。<br><br>
- 这里的const FVector& Start, const FVector& End可以传入武器插槽起始和结束位置。<br><br>
这两个参数可以提供给我们刚才提到的需求分析中，最核心的的信息。OutHits可以帮助我们基于这些信息设置击中的反馈粒子，声音等。Start和End两个向量可以让我们的设计师将建立的插槽位置信息传入，设定线性检测的范围。<br><br>
虚幻引擎4提供了大量的可视化Debug工具，如果想看到这条射线的检测，可以借用DrawDebugline函数查看。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023897" aid="1023897" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101640ewk4zppi9ipp4444.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101640ewk4zppi9ipp4444.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101640ewk4zppi9ipp4444.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">玩家开启Debug的线性检测效果</font></font></div>
<br><strong>近战武器检测实现2：由角色驱动的检测通知</strong><br><br>
毫无疑问，角色在挥舞武器时进行的检测是最为自然的逻辑。线性检测本身比较耗费性能，根据使用者的攻击动画的执行情况，控制其开启和关闭。如下我们自定义了攻击检测的通知节点，在攻击动画播放时调用代码，进而控制武器的检测开始TraceStart和结束TraceEnd。<br><br><div align="center">
<img id="aimg_1023898" aid="1023898" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101640bn3sit9g9pgperrs.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101640bn3sit9g9pgperrs.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101640bn3sit9g9pgperrs.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1023899" aid="1023899" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101640cbivsbb5wstba7lz.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101640cbivsbb5wstba7lz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101640cbivsbb5wstba7lz.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">玩家的攻击动画AnimNotify通知</font></font></div>
<br>
当检测开始之时，在此期间将会不断地trace。因为该trace既可以写在Tick之内逐帧执行，也可以自定义一个Timer，让其按照一定高频的间隙进行检测。频率越高检测越准确，但是耗能。频率越低检测不准确，但是省性能，这里可以自行取舍。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023900" aid="1023900" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101641f2begb9mp2bhl2my.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101641f2begb9mp2bhl2my.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101641f2begb9mp2bhl2my.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">玩家的Debug线稀疏情况</font></font></div>
<br><div align="center">
<img id="aimg_1023901" aid="1023901" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101641up1zmh33rgz927g3.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101641up1zmh33rgz927g3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101641up1zmh33rgz927g3.jpg" referrerpolicy="no-referrer">
</div>
<br>
理论上来说，我们只需要在返回结果队列中，判断出Trace的是敌人，对其扣血即可，便实现了检测伤害。这里我们让该武器调用ApplyPointDamage传递伤害给受击目标，受击目标自身进行实际的处理细节。<br><br><div align="center">
<img id="aimg_1023902" aid="1023902" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101641umq46jys7deym3t6.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101641umq46jys7deym3t6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101641umq46jys7deym3t6.jpg" referrerpolicy="no-referrer">
</div>
<br>
然而，如果你这样做的话，会产生一个严重的错误。你可能会发现，一次武器挥舞，敌人有可能会承受很多次伤害，直至死亡。这就引入了受击者队列的话题。<br><br><strong>近战武器检测实现 3：受击者队列</strong><br><br>
因为在上面我们提到，Trace是在Tick中不断执行的，同一个敌人可能会在Trace过程中被多次检测到，其会不断受到伤害。我们只想在一次武器挥舞的过程中，让同一个敌人一次承受一击伤害。正确的做法是，我们需要建立一个队列来提出这一次TraceStart到TraceEnd的目标，对加入的目标进行排重。<br><br>
这里需要澄清一次挥舞和同一条攻击动画有多次攻击的区别，如果你想在一条动画中执行两次伤害，就再调用一次TraceStart和TraceEnd。<br><br><div align="center">
<img id="aimg_1023903" aid="1023903" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101641lfdln8x5xylel2cx.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101641lfdln8x5xylel2cx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101641lfdln8x5xylel2cx.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">AnimNotify中有多次TraceStart和End</font></font></div>
<br>
为什么会有两次或多次的情况，比如下面的长矛旋转攻击。我们想让这条动画中长矛每转半圈产生一次伤害。这样我们可以让动画师按照自己的想法制作一条完整的动画，又可以让设计师根据自己的需要设置伤害规律。<br><br><div align="center">
<img id="aimg_1023904" aid="1023904" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101642i1ih1sjv11vcnfz1.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101642i1ih1sjv11vcnfz1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101642i1ih1sjv11vcnfz1.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">使用长矛时在Montage的旋转动画</font></font></div>
<br><strong>近战武器击中反馈实现 1: 击中目标</strong><br><br>
FHitResult hitResult;<br><br>
HitResult含有丰富的击中目标信息，如获取Actor，即是击中的目标。<br><br><div align="center">
<img id="aimg_1023905" aid="1023905" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101642au8r1pxunpdenhlu.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101642au8r1pxunpdenhlu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101642au8r1pxunpdenhlu.jpg" referrerpolicy="no-referrer">
</div>
<br>
在上面的代码中，我们可以看到，如何判断一个敌人被击中并对其处理。<br><br>
IsInHurtList就是我刚才谈到的，在这次TraceStart和TraceEnd我们将同一个扫到的目标判断一次，进行排重。IsIgnoreByTeamID用来避免友军伤害，毕竟我们不想让敌人之间互相击中。<br><br><strong>近战武器击中反馈实现2：飞溅的血液和清脆的金属</strong><br><br>
我们也可以访问到hitResult.impactpoint获取击中位置，在这里播放粒子效果，例如设置飙血。和击中声音的位置。精确的反应出武器打到目标的点。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023906" aid="1023906" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101643hg8850ngk5ggbb9n.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101643hg8850ngk5ggbb9n.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101643hg8850ngk5ggbb9n.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">击中目标的血迹</font></font></div>
<br>
除此之外，HitResult也可以为我们返回物理材质。物理材质定义了材质表面的属性，据此设置对应的反馈效果。如我们击中了水泥地板，可以返回烟尘。木头的话即是木屑。我们可以在武器中详细的设置击打不同物理材质，的反馈效果。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023907" aid="1023907" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101643mszddesdd8w5xxxw.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101643mszddesdd8w5xxxw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101643mszddesdd8w5xxxw.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">使用武士刀打击地面火星</font></font></div>
<br><div align="center">
<img id="aimg_1023908" aid="1023908" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101643ywy33rhdyqwm3q3c.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101643ywy33rhdyqwm3q3c.jpg" width="566" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101643ywy33rhdyqwm3q3c.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1023909" aid="1023909" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101644np9spiyfpy5o2e5f.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101644np9spiyfpy5o2e5f.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101644np9spiyfpy5o2e5f.jpg" referrerpolicy="no-referrer">
</div>
<br>
我们实现的子弹击中目标也会根据物理材质，判断击中粒子。类似的，角色在移动时，脚步对地面进行线性检测，也会判断物理材质，反馈出对应的声音。<br><br><strong>近战武器击中反馈实现3：摄像机震动</strong><br><br>
谈谈摄像机摇晃和手柄震动。虚幻引擎4 为我们封装了大量实用的功能，我们的玩家角色的Controller继承自PlayerController，在该类中，为开发者们提供了摄像机震动的功能。<br><br>
我们只需要在代码中，挥舞武器和击中敌人的位置进行调用。再将对应的CameraShake变量在C++中暴露给蓝图，这样设计师便可以根据攻击感受调节对应武器击中震动效果。让不同的武器有所差异。<br><br><div align="center">
<img id="aimg_1023910" aid="1023910" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101644khorn3orjddb19zr.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101644khorn3orjddb19zr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101644khorn3orjddb19zr.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023911" aid="1023911" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101645jiwci4mwr2w0smk4.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101645jiwci4mwr2w0smk4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101645jiwci4mwr2w0smk4.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">武器击中目标后的摄像机震动效果</font></font></div>
<br>
我们不仅仅给击中目标添加了摄像机震动，设计师还可以根据每一把武器的挥舞起始对摄像机的震动情况进行定制。<br><br><div align="center">
<img id="aimg_1023912" aid="1023912" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101646b6lu4g5uuu66e9lg.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101646b6lu4g5uuu66e9lg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101646b6lu4g5uuu66e9lg.jpg" referrerpolicy="no-referrer">
</div>
<br>
手柄的震动反馈与此类似，我们在C++定义了摄像机震动的引用，这样设计师可以在蓝图中进行定制。使得每一种武器有其独有的质感表现。<br><br>
为了拉开不同武器击中差异感受，我们引入了击停的功能。<br><br><strong>近战武器击中反馈实现4：击打顿感</strong><br><br>
上面我们提到，我们想让利器如武士刀和钝器棒球棍，击中敌人后的顿感反馈不同。该怎么实现顿感呢？理论上来说，即是在击中敌人那一刻，让系统稍作停顿。我们观察一下Capcom的街霸：<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023913" aid="1023913" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101646oh5p2copopbl5lpp.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101646oh5p2copopbl5lpp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101646oh5p2copopbl5lpp.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">街霸5</font></font></div>
<br>
虚幻引擎4的强大功能库，再次给了我们帮助，在GameplayStatics.h头文件中，封装了下面的函数。该函数可以设置整个游戏世界的时间播放速率。<br><br><div align="center">
<img id="aimg_1023914" aid="1023914" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101646uu8gyhv88304vm8x.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101646uu8gyhv88304vm8x.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101646uu8gyhv88304vm8x.jpg" referrerpolicy="no-referrer">
</div>
<br>
我们在击中目标时，使其停滞，根据每一把武器设置停滞时间。同样的将这些参数暴露给设计师，他们可以根据每一把武器,设置击中敌人的停顿速率，以及持续时长。让不同的武器击中感受有所差异。通过肉眼可以看出下面的武士刀和大锤的击中感受有所差异。<br><br><div align="center">
<img id="aimg_1023915" aid="1023915" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101648j8kkk7uttsnnp2k3.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101648j8kkk7uttsnnp2k3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101648j8kkk7uttsnnp2k3.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1023916" aid="1023916" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101648recqtizm0mxcpx5c.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101648recqtizm0mxcpx5c.jpg" width="535" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101648recqtizm0mxcpx5c.jpg" referrerpolicy="no-referrer">
</div>
<br>
在代码中的执行过程是这样的，武器线性检测击中敌人的那一刻，系统速率放慢。很短的时间后，再恢复正常。根据不同武器的特性，例如利器和钝器的放慢速率和停滞时长有所不同即可。<br><br><strong><font color="#de5650">二、受击者反馈</font></strong><br><br><strong>受击者特性分析：动画，推力和溅血</strong><br><br>
由上面我们看到，为了呈现近战武器击中目标的反馈效果，我们为武器赋予了很多特征。一个巴掌拍不响，我们还需要为受击者作出对应的反馈。我们想通过3个方面呈现受击者的被击效果：第1条是给受击目标一定的推力，就像下面这样。<br><br><div align="center">
<img id="aimg_1023917" aid="1023917" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101648ep8tfkpfrthmdtn8.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101648ep8tfkpfrthmdtn8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101648ep8tfkpfrthmdtn8.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">《空洞骑士》战斗，推动敌人</font></font></div>
<br>
可以看到，《空洞骑士》中对敌人造成推力，使得攻击极有力量。一方面，推力可以增强玩家的输出力量反馈，这对于横版游戏来说简直天作之和。<br><br>
另一方面，我们在制作主角的攻击动画时，可以让其在招式中垫步。玩家不断的往前推进，敌人受击后往后退，两者亦步亦趋的状态感受很不错。打人就是要爽，这样就会有压着打人的感觉。<br><br>
第2条是受击动画。敌人在受到攻击时执行受击动画是最自然和直接的刺激反馈。第3条是受击者身体和地面周边墙壁溅射的血迹。毫无疑问，这可以增加细节感受。细节是我们想追求的。后面可以看到，我们为了呈现细节，实现了多少有趣的功能特性。<br><br>
下来，我讲讲推力是怎么实现的。<br><br><strong>受击者反馈1：推力</strong><br><br>
我们实现了角色基类ABaseCharacter，继承自ACharacter。我们的玩家角色和敌人都继承自ABaseCharacter。ABaseCharacter实现了角色和敌人的共有特性及功能。例如，基础的伤害处理逻辑。<br><br><div align="center">
<img id="aimg_1023918" aid="1023918" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101649ohiae3hcyrcyirry.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101649ohiae3hcyrcyirry.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101649ohiae3hcyrcyirry.jpg" referrerpolicy="no-referrer">
</div>
<br>
我们实现了一个角色在一段时间内，获取受击推力的系统。该系统可以让角色获取一个传入的方向位移及力量，并且持续一段时间。实现的原理是这样的，我们让角色受击时，开启一个Timer，在一段间隙内。执行获取的速度。<br><br><div align="center">
<img id="aimg_1023919" aid="1023919" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101649jkdb9bite8bxc39p.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101649jkdb9bite8bxc39p.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101649jkdb9bite8bxc39p.jpg" referrerpolicy="no-referrer">
</div>
<br>
在上面提到的ACharacter中，MovementComponent掌管着角色的运动，其中Velocity可以定制我们想让该角色保持的速度。<br><br><div align="center">
<img id="aimg_1023920" aid="1023920" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101649fbjj8laz29ava2zs.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101649fbjj8laz29ava2zs.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101649fbjj8laz29ava2zs.jpg" referrerpolicy="no-referrer">
</div>
<br>
在近战武器击中敌人时，我们调用该功能即可。由于每一种武器有不同的重量感，例如武士刀和大锤，对敌人的击中力量不同。我们同样开放给了设计师，可以为每一种武器设定推力的权重。<br><br>
同时，相同武器在不同招式下的发力大小是不同的，我们按照一定的数据结构，管理了攻击者对应每一个招式的数据，传入给该武器，例如其推力。由于敌人的重量感不同，每一种敌人有被推的权重参数，共同决定了受击后所呈现的推力。<br><br><strong>受击者反馈2：受击动画反应</strong><br><br>
我们将受击动画划分为3类，轻受击，重受击和被击飞。前面我们看到了，武器基于该函数传入给敌人伤害信息。<br><br><div align="center">
<img id="aimg_1023921" aid="1023921" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101650e8zbsz1t7uyufbpy.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101650e8zbsz1t7uyufbpy.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101650e8zbsz1t7uyufbpy.jpg" referrerpolicy="no-referrer">
</div>
<br>
其中我们扩展了DamageType，可以决定这次攻击受击者应该呈现怎样的反应。<br><br><div align="center">
<img id="aimg_1023922" aid="1023922" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101650cw9uuh2bazshfao5.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101650cw9uuh2bazshfao5.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101650cw9uuh2bazshfao5.jpg" referrerpolicy="no-referrer">
</div>
<br>
受击角色根据自己的伤害类型及当前的状态执行对应的受击动画逻辑。<br><br><div align="center">
<img id="aimg_1023923" aid="1023923" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101650v4fue1hymc5e5qzm.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101650v4fue1hymc5e5qzm.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101650v4fue1hymc5e5qzm.jpg" referrerpolicy="no-referrer">
</div>
<br>
受击动画的道理非常简单，仅是执行其对应Montage即可。<br><br><div align="center">
<img id="aimg_1023924" aid="1023924" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101650bm3vimzexq3u9cm2.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101650bm3vimzexq3u9cm2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101650bm3vimzexq3u9cm2.jpg" referrerpolicy="no-referrer">
</div>
<br>
在上面的代码中，我们看到使用了Timer来检测该动画是否已经执行完毕。这可以帮助我们追踪受击动画结束事件。<br><br>
值得一提的是，武器对目标造成什么样的击打反映是由攻击者决定，例如下面的敌人拿着农具，通过数据结构的配置。让其最后一招可以将玩家击飞。<br><br><div align="center">
<img id="aimg_1023925" aid="1023925" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101651uerdii6fdqv2qsbz.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101651uerdii6fdqv2qsbz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101651uerdii6fdqv2qsbz.jpg" referrerpolicy="no-referrer">
</div>
<br>
同样的，玩家也可以使用该武器，根据自己的动画招式，配置对应的击打效果。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023926" aid="1023926" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101651n6elrz58o59jo5y8.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101651n6elrz58o59jo5y8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101651n6elrz58o59jo5y8.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">玩家使用铁锹</font></font></div>
<br><strong>受击者反馈3：击飞</strong><br><br>
与执行受击动画不同的是，被击飞实现起来比较繁琐。那么怎么实现角色被击飞呢？为此我们拆分了击飞这一过程的逻辑，构建了一个状态机。<br><br><div align="center">
<img id="aimg_1023927" aid="1023927" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101652zcifhyhp8ph0ic33.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101652zcifhyhp8ph0ic33.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101652zcifhyhp8ph0ic33.jpg" referrerpolicy="no-referrer">
</div>
<br>
对Montage进行拆分管理。状态大致分为：起飞，飞行（循环），落地，爬起。在这里，飞行这一过程是循环执行的，因为我们不知道玩家和敌人是否飞出了平台，导致其还在空中便执行了落地动画，这样会显得很诡异。这个状态机根据时间,动画的执行状态,动画中的事件通知AnimNotify以及线性检测来进行管理。<br><br>
首先，让敌人执行被击飞动画。这时，我们按照一定的飞行速度给其推力，方向分别为向后和向下。向下的原因是，敌人可能会飞出斜坡，这样他会始终是一种贴地状况。我们让其飞行过程一直对地面进行线性检测，防止其在过高的地方执行坠落动画，并且朝其飞行的方向执行线性检测，查看是否有撞到墙壁。<br><br>
如果满足了飞行时间，或者撞到了飞行方向的墙壁，将会执行下落动画。在下落动画中，身体着地的那一刻，关闭其飞行方向的推力。待该条动画执行完毕后，执行其站起即可。<br><br><strong>受击者反馈4：溅血等细节</strong><br><br>
为了使战斗呈现的更有细节，我们想让敌人受击的时候，其身体的伤痕加重，并且血液会溅在四周的墙壁与地面上。<br><br>
实现过程如下：<br><br>
我在角色的受伤C++函数中，开放了留给TA同学BP事件接口。他根据该接口，调用自己实现的生成溅血贴花BP函数，以及为敌人的材质制作血迹效果，随着伤害的增多，调用材质实例的参数，血迹将会加重。<br><br><div align="center">
<img id="aimg_1023928" aid="1023928" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101652x3o7s8nnzs7s9qs1.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101652x3o7s8nnzs7s9qs1.jpg" width="568" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101652x3o7s8nnzs7s9qs1.jpg" referrerpolicy="no-referrer">
</div>
<br>
额外细节：利器击中角色时，武器尾迹可以拉出细长的血丝。<br><br><div align="center">
<img id="aimg_1023929" aid="1023929" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101652jopahnaohhpypyyq.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101652jopahnaohhpypyyq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101652jopahnaohhpypyyq.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023930" aid="1023930" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101653ghk6x6xera6khx22.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101653ghk6x6xera6khx22.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101653ghk6x6xera6khx22.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">剑类武器拖拽的血丝</font></font></div>
<br><strong>角色死亡特性分析：死亡效果呈现</strong><br><br>
玩家与敌人战斗，成功杀死对方是需要获得极大满足感的。无数的精彩动作片告诉我们，敌人的死亡效果会放大这种喜悦。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023931" aid="1023931" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101653hdzzzvlin1uxu1ud.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101653hdzzzvlin1uxu1ud.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101653hdzzzvlin1uxu1ud.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">碟中谍甩飞敌人</font></font></div>
<br>
我们不想制作很多死亡动画，还要根据死亡情景来匹配该播放哪段动画。如判定其是在空中死亡还是地面。这着实在太费神。布娃娃的死亡效果可以满足我们所需，让我们免去制作死亡动画，也省去操心以上各种情景的判断。最重要的是，物理效果也太有趣了。那么布娃娃效果怎么实现呢？<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023932" aid="1023932" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101653s4cytrc8rtt8ct70.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101653s4cytrc8rtt8ct70.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101653s4cytrc8rtt8ct70.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">布娃娃死亡</font></font></div>
<br><strong>角色死亡实现1：布娃娃效果</strong><br><br>
- 为角色绑定好布娃娃效果。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023933" aid="1023933" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101653stzs72o2xvsotvpa.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101653stzs72o2xvsotvpa.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101653stzs72o2xvsotvpa.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">布娃娃</font></font></div>
<br>
- 在敌人死亡时，激活该角色SkeletalMeshComponent的物理模拟。<br><br>
在我们游戏中，当该物理被激活时，我为其赋予了一定的冲力。这样敌人将有一种被揍飞的效果。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023934" aid="1023934" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101654vlpzxt5ttl58ft5a.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101654vlpzxt5ttl58ft5a.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101654vlpzxt5ttl58ft5a.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">敌人死亡</font></font></div>
<br><div align="center">
<img id="aimg_1023935" aid="1023935" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101654vqiugy8ss4a7w9uc.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101654vqiugy8ss4a7w9uc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101654vqiugy8ss4a7w9uc.jpg" referrerpolicy="no-referrer">
</div>
<br>
物理引擎的使用可以让游戏自然，有趣，不可预测。<br><br><strong>角色死亡实现 2: 断肢</strong><br><br>
下来这一部分可能会令一些听众感到不适，我希望听这一部分主题的听众都年满18岁。《生死轮回》中有种类繁多的武器。玩家和敌人会遭受钝器击伤，利器刺伤砍伤，爆炸等情况。<br><br>
我们引入了断肢系统来呈现多样性。再次提到DamageType类。我们自定义了各种断肢形式，可以确切的切掉左手，右腿，脑袋。或者随机断裂一件肢体，也有可能根据爆炸随机断几处。也有可能让整个角色四分五裂。<br><br><div align="center">
<img id="aimg_1023936" aid="1023936" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101655pyvomvvuhrbobryj.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101655pyvomvvuhrbobryj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101655pyvomvvuhrbobryj.jpg" referrerpolicy="no-referrer">
</div>
<br>
建立了一种数据结构，定义攻击者的招式参数，在武器检测的时候传给武器伤害类型。受击者会在死亡时根据自己承受的伤害类型，呈现对应的肢体断裂效果。例如玩家在使用武士刀执行下面的回身砍时，将会对敌人进行斩首。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023937" aid="1023937" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101655ak47oy6446do64so.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101655ak47oy6446do64so.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101655ak47oy6446do64so.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">对敌人斩首效果</font></font></div>
<br>
那么断肢系统是怎么实现的呢？有两种思路：<br><br>
既然我们在上面实现了角色在死亡时执行布娃娃效果。自然而然的，我们会考虑布娃娃的骨骼连接处是否可以解除骨骼绑定，呈现断裂。<br><br>
这里我就不卖关子了。我们并没有使用该方法，而是采用了另一种思路，实现起来更简单。<br><br><strong>断肢实现1：隐藏断掉的肢体</strong><br><br>
虚幻引擎4的SkeletalMeshComponent类提供了HideBoneByName函数，该函数可以隐藏对应的骨骼。<br><br>
例如我们传入角色的脑袋骨骼，其脑袋便会消失。这其实已经解决了问题的一半。<br><br><div align="center">
<img id="aimg_1023938" aid="1023938" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101655vc1gv8jehh8hee11.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101655vc1gv8jehh8hee11.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101655vc1gv8jehh8hee11.jpg" referrerpolicy="no-referrer">
</div>
<br><strong>断肢实现2：生成有物理效果的肢体</strong><br><br>
我们再生成一个有很好的物理效果的飞出去的脑袋好了。<br><br>
我们创建了一个叫做BDropActor.cpp的类，专门用于模拟飞出去的有物理效果的物件。<br><br>
Actor中包含SkeletalMeshComponent组件，生成的时候便会激活自己的物理效果。除了在这里用到的断肢，还有游戏中玩家扔出去的弹夹，喝完的血瓶。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023939" aid="1023939" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101656xudtupnmodd09o4p.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101656xudtupnmodd09o4p.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101656xudtupnmodd09o4p.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">断肢，弹夹再编辑器中的模拟</font></font></div>
<br><strong>断肢实现3：优化断裂飞翔肢体的反馈效果</strong><br><br>
SkeletalMeshComponent绑定了PhysicsAsset，设置正确的碰撞可以接受碰撞事件。我们让这些物件碰撞到物体表面的时候便可以播放声音和粒子特效。<br><br>
在C++中，我们绑定并实现该SkeletalMeshComponent的OnComponentHit的事件，该函数会在Mesh与物体碰撞时执行响应。<br><br>
需要注意的是，因为OnComponentHit随着物理会高频的撞击，如果我们只是粗暴的在撞击的时候播放声音和粒子，将会发现物理效果是非常不可控的。哪怕是轻微的撞击都会播放粒子和声音，这样会持续的嘈杂不堪。<br><br>
为此我们应该写一些约束条件：一方面控制播放间隙。另一方面，可以根据撞击的速度，缩放其撞击的音量。<br><br><div align="center">
<img id="aimg_1023940" aid="1023940" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101657rjl7sxwfq6x6jrlj.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101657rjl7sxwfq6x6jrlj.jpg" width="475" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101657rjl7sxwfq6x6jrlj.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1023941" aid="1023941" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101657jjmym6tthd553d0d.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101657jjmym6tthd553d0d.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101657jjmym6tthd553d0d.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1023942" aid="1023942" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101657q3ja95az99c89t4w.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101657q3ja95az99c89t4w.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101657q3ja95az99c89t4w.jpg" referrerpolicy="no-referrer">
</div>
<br>
如此，反馈将极具细节。例如，坠落撞击的速度达到一定的阈值才会溅起尘土，撞击的快慢和声音的大小匹配。<br><br>
这样的算法我们也应用在布料中，玩家在穿过布料的时候，如果速度够快，布料撞击的声音也会越大。<br><br><div align="center">
<img id="aimg_1023943" aid="1023943" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101657p3qqtk3ehza7zvu7.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101657p3qqtk3ehza7zvu7.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101657p3qqtk3ehza7zvu7.jpg" referrerpolicy="no-referrer">
</div>
<br>
我们也采用这种方式，让敌人死亡的时候丢掉自己手中的武器，武器撞击会产生对应的粒子特效。玩家丢掉的弹夹同样。<br><br><div align="center">
<img id="aimg_1023944" aid="1023944" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101657cj5vmsmds4zvjdx5.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101657cj5vmsmds4zvjdx5.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101657cj5vmsmds4zvjdx5.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">玩家丢掉弹夹，敌人的武器飞出去</font></font></div>
<br>
在断肢肢体的碰撞事件中，我们生成贴花来影响环境溅血。例如飞出去的脑袋，在撞击天花板的时候可以溅起血迹贴花。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023945" aid="1023945" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101658k1ltxo8h1lbbd8lh.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101658k1ltxo8h1lbbd8lh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101658k1ltxo8h1lbbd8lh.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">对敌人斩首效果</font></font></div>
<br><strong>断肢实现4：断肢效果呈现</strong><br><br>
我们预设了角色各部分的肢体的断裂模型，良好的组织和匹配各个肢体，便可以实现丰富的断裂种类。无论是单个确定的部位，还是随机几个，亦或是下面的手雷可以将敌人炸的四分五裂。都是可能的。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023946" aid="1023946" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101700hiza2f5dkzajahdc.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101700hiza2f5dkzajahdc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101700hiza2f5dkzajahdc.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">手雷将敌人炸的四分五裂</font></font></div>
<br><strong>近战系统总结：</strong><br><br>
有了细节，构建了大量的参数对系统良好的配置。是构成近战系统呈现品质的基础。在我们的游戏中，玩家和敌人都使用相同的武器。但是针对玩家和敌人，我们也会根据系统进行一些区分。下面想讲一讲我们是怎么实现无缝随机地图的。<br><br><strong><font color="#de5650">三、无缝Roguelite地图</font></strong><br><br><strong>随机地图概述</strong><br><br>
《生死轮回》一共有7个大关卡，每个关卡在每次进入时都会与上次不同,整个过程无缝连续，具有如同线性游戏的连贯游戏体验。在分享我们的实现技术之前，我想先分析一些传统随机地图的实现方案。这些方法的研究对我们自己的架构和实现,有很高的参考价值与启发。<br><br><strong>实现方案参考1：Procedural 动态生成</strong><br><br>
制作大批量的随机房间，对其分类，如这里是战斗房间，补给房间，走廊，还是呈现剧情的地方。定义好出口和入口，按照预设的算法规则，在关卡初始化的时候。动态的将这些地图的出口和入口进行连接生成。可能在生成之后还要避免地图重叠，进行重新计算。<br><br>
《死亡细胞》这款出色的横版动作roguelite游戏和不少俯视角地牢类型的游戏，便是采用以下方案实现的：<br><br><div align="center">
<img id="aimg_1023947" aid="1023947" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101700bjllz2iqssz2ps2e.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101700bjllz2iqssz2ps2e.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101700bjllz2iqssz2ps2e.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">死亡细胞拓扑结构</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023948" aid="1023948" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101701vsk89jkqqkk34zts.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101701vsk89jkqqkk34zts.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101701vsk89jkqqkk34zts.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">死亡细胞</font></font></div>
<br>
该方法有众多优点，但也有其不足。我们来看看：<br><br><strong>优点：</strong><br><br>
+ 无缝连续，生成后的关卡浑然一体。<br><br>
+ 随机度高，算法生成的房间即便连开发者都无法预测，每次感受焕然一新。大大提升重复可玩性。<br><br><strong>缺点：</strong><br><br>
- 地图边界处理，无论是对于设计，如何处理好地图的美术边界，还是其连接逻辑都是非常复杂的。没有采用很好的风格化处理，将会出现严重的房间感和割裂感。<br><br>
- 管理复杂，对房间的制作规范严谨，如出口与入口，房间的分类等。<br><br>
- 控制弱，不好掌控流程，房间的良好分类要求高。对叙事呈现难度高。加载卸载面临的情况可能复杂不好预测。<br><br>
- Debug难度高，随着房间迭代量增加，算法生成的地图千变万化，可能会出现一些无法预料之事。难以捕捉到。<br><br>
实现方案参考2：房间过渡式动态生成<br><br>
制作好大量的房间，玩家每次离开一个房间，按照一定的拓扑规则，黑屏加载下一个，卸载当前。采用这种技术实现方式的Rogulite游戏不在少数，如《哈迪斯》，《以撒的结合》。然而这种实现方案的优缺点都比较明显。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023949" aid="1023949" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101702i64x812so5662454.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101702i64x812so5662454.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101702i64x812so5662454.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">哈迪斯</font></font></div>
<br><strong>优点:</strong><br><br>
+ 技术难度低，采用Procedural面临的地图无缝拼接这种复杂的美术边界处理，及其连接技术挑战，都不再是问题。<br><br>
+ 性能要求低，每次只需要加载玩家舞台范围内的场景。<br><br>
+ 管理简单，房间的制作规范，出口和入口都不需要很繁琐的管理成本。<br><br><strong>缺点:</strong><br><br>
- 无法无缝，一个房间黑屏进入下一个房间，给人极大的割裂感。<br><br>
- 过场动画，对于播放过场动画的房间，玩家每次进来十分繁琐的加载和卸载。<br><br><strong>随机地图设计1：方案探索</strong><br><br>
我们想给玩家带来无缝流畅的游戏体验，因此没有采用类似《哈迪斯》的架构。但是，我们也并没有直接采用《死亡细胞》式的Procedural方案，原因有二：<br><br>
1.《生死轮回》是一款故事驱动的动作游戏，游戏内置有超过80分钟的实时过场动画，以及许多特殊事件。我们需要对关卡总流程有如同线性游戏般的掌控力。<br><br>
2. 在实现了Procedural式的动态生成关卡后，我们感觉到关卡的每一个区域有极强的房间感，无法满足我们对于衔接处的美术掌控。<br><br><strong>随机地图设计2：关卡拆分成区域</strong><br><br>
我们按照线性游戏的制作思路开发了一个完整的关卡。然后对其按区域划分。让每一个区域有满足整体及周边风格的迭代。<br><br>
在对区域进行多次美术迭代之后，我们不禁思考，是否也能对每一个美术区域的逻辑，进行多次迭代，以丰富关卡体验。<br><br><strong>随机地图设计3：区域由“美术”和“逻辑构成”</strong><br><br>
每一个迭代的区域由其“美术”和“逻辑”组合而成，这构成了该区域的独特游戏体验。<br><br>
“区域美术”意味着玩家目之所及的环境，以及环境构成的游玩路线。对于一般的线性游戏，关卡设计师预制了确定的游戏流程，玩家每次的体验一致。例如，进入这个关卡所见到的相同敌人及其布局。<br><br>
“区域逻辑”意味着玩家来到一个固定风貌场景的区域，所经历的游戏逻辑事件，如敌人的生成逻辑，事件脚本，和关卡，谜题等。<br><br><strong>关卡体验= 关卡美术+关卡逻辑</strong><br><br>
这里要说明的是，由于关卡美术决定了游玩路线，因此只能在其基础上进行逻辑迭代，而无法反过来。<br><br>
那么游戏体验的变化是怎样的呢？举一个例子：《生化危机4》中采用了一种动态难度机制，当玩家来到教堂的地方，这里原本只站着几个近战寺僧。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023950" aid="1023950" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101702oc1dpjzyckjeyrc5.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101702oc1dpjzyckjeyrc5.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101702oc1dpjzyckjeyrc5.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">生化危机4 的普通近战敌人</font></font></div>
<br>
但是如果之前的表现良好，身上的补给物充足。这里的敌人数目就会发生变化，近战敌人后面又补充了几个弩兵。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023951" aid="1023951" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101703hxt1w1vy1wa0gtx9.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101703hxt1w1vy1wa0gtx9.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101703hxt1w1vy1wa0gtx9.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">生化危机4 的弩枪敌人</font></font></div>
<br>
而采用逻辑分离的方式，我们不仅可以定制：1.敌人布置：这里的敌人布置不一样。如数量，站位和类型。2.动态难度：随着玩家能力的提升，这里的挑战难度和其能力匹配。3.玩法改变：这次可能是战斗，下次可能是解谜。<br><br><strong>关卡结构1：关卡区域拆分</strong><br><br>
每个主关卡，由自己，和按照区域划分的包含在其中的大量的迭代子关卡构成。<br><br>
借助虚幻引擎4的关卡管理器，我们能方便的对一个完成的线性关卡按区域进行划分。然后对各个区域按照创建子关卡的形式进行迭代。<br><br><div align="center">
<img id="aimg_1023952" aid="1023952" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101703ijjnxz0s0exrs4sv.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101703ijjnxz0s0exrs4sv.jpg" width="433" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101703ijjnxz0s0exrs4sv.jpg" referrerpolicy="no-referrer">
</div>
<br>
例如，从上面的地图中我们看到，A区域有3个美术关卡迭代A_1,A_2,A_3。我们看到，仅是对A_1的美术关卡，我们对其制作了3个逻辑关卡。<br><br>
最终，A区域的3个美术关卡及其每3个逻辑关卡，可组合呈现9种游戏体验。<br><br><strong>关卡结构2：主关卡构成</strong><br><br>
可以看到，在一个主关卡的列表中，包含了所有默认不加载和不可见的迭代子关卡。<br><br>
我们利用主关卡的LevelBP来进行一些全局事件的管理，例如控制玩家的死亡事件处理，全局随机下雨和雾的控制等。主关卡自己主要还包含了一些天空球，全局的天光/方向光，后期，LightmassImportanceVolume和路径体积等全局物件。<br><br>
那么每个区域的随机加载过程是怎么实现及运作的呢？<br><br><div align="center">
<img id="aimg_1023953" aid="1023953" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101703k0fxxkj5b0a05vl0.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101703k0fxxkj5b0a05vl0.jpg" width="553" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101703k0fxxkj5b0a05vl0.jpg" referrerpolicy="no-referrer">
</div>
<br><strong>随机区域实现1：随机加载管理器</strong><br><br>
我们实现了一个叫做BRoomArrow的管理器。像前面实现的近战武器和枪支一样，我们在C++中实现了其基础逻辑，为其创建BP子类，方便关卡设计师对其配置。<br><br><div align="center">
<img id="aimg_1023954" aid="1023954" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101704r3h8hllw3lv6cve0.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101704r3h8hllw3lv6cve0.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101704r3h8hllw3lv6cve0.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">RoomArrow C++截图</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1023955" aid="1023955" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101705f11ikj1blbwi4w1k.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101705f11ikj1blbwi4w1k.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101705f11ikj1blbwi4w1k.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">RoomArrow BP截图</font></font></div>
<br>
每个管理器对应每个区域的管理，他们放置在场景中。其自身会按照一定的逻辑规则加载该区域的随机子关卡。一个区域可以加载哪些随机关卡由关卡设计师预制。<br><br><div align="center">
<img id="aimg_1023956" aid="1023956" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101705p1iury64ig44ekck.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101705p1iury64ig44ekck.jpg" width="408" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101705p1iury64ig44ekck.jpg" referrerpolicy="no-referrer">
</div>
<br><strong>随机区域实现 2：地图的加载过程</strong><br><br>
在关卡初始化的过程中，按照区域ID，每一个RoomArrow会先加载该区域的“美术子关卡”。“美术子关卡”加载完毕之后，根据其前缀名字匹配一个随机的“逻辑子关卡”。<br><br>
名字匹配的过程是这样的，如该地图的美术关卡为A_1_Btl_R，其将会在A_1_Btl_R_L1~A_1_Btl_R_L3中随机寻找一个。每一个管理器加载完毕之后会设定其状态。我们在主关卡的Level BP中检测所有关卡是否加载完毕，以设置Loading条，和让玩家按下任意键进入游戏。这样就完成了随机关卡的序列化加载。<br><br><strong>随机区域实现 3：关卡的加载和卸载</strong><br><br>
我们同时让每个管理器肩负着各个区域的加载和卸载功能，以平衡性能。我们在该管理器中新建了BoxComponent，其碰撞事件检测玩家是否跑到区域内，以便设置该区域的可见或隐藏，加载或卸载。<br><br><div align="center">
<img id="aimg_1023957" aid="1023957" zoomfile="https://di.gameres.com/attachment/forum/202112/08/101705any7s4k4e2wxz47y.jpg" data-original="https://di.gameres.com/attachment/forum/202112/08/101705any7s4k4e2wxz47y.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/08/101705any7s4k4e2wxz47y.jpg" referrerpolicy="no-referrer">
</div>
<br><strong>随机区域实现 4：总结</strong><br><br>
这样，我们按照一定的设计思路，完成了满足我们游戏的无缝Rogulite地图实现。概括来说，即是：<br><br>
1.将关卡按区域划分。<br><br>
2.关卡美术与关卡逻辑分离。<br><br>
3.创建管理器控制每个区域的随机动态加载，关卡设计师预制每个区域的随机内容。<br><br>
4.加载卸载体积，平衡性能。<br><br><strong><font color="#de5650">四、设计，技术与游戏性</font></strong><br><br>
最后谈一谈在《生死轮回》的开发中，围绕设计，技术与游戏性实现方面的几点心得。<br><br>
设计，技术实现和乐趣：大多时候设计产生了需求，推动我们去展开技术实现。但技术在实现的过程中，也会激发我们产生有趣的想法，扩展设计。技术激发出的设计，如同童年时期，捣鼓玩具时产生的纯粹的，最本质的游戏性乐趣。这种探索出的设计，往往更加独特有趣。<br><br>
规模，细节和品质：一个可以掌控的体量做到极致，比一味做大而空泛无聊的游戏作品有价值的多。<br><br>
那一刀的品质：我们实现了那么多功能，暴露了那么多参数给设计师。实现了那么多粒子特效，向外包反馈了那么多次音效修改意见。制作了精致的角色和高品质的攻击和受击动画。最后用一个庞大精美的世界呈现了游戏舞台。而玩家在砍下敌人的第一刀之时，便能得出这款游戏值不值得玩的结论。<br><br>
单个和整个：将每一个模块高品质的实现，再极好的交汇在一起构成系统，是一件极富挑战之事。是否运转的良好实在考验团队的设计，技术，耐心和运气。<br><br>
我的分享就到这里，谢谢大家。<br><br><font size="2"><font color="#808080"></font></font><br><br>
</td></tr></tbody></table>


  
</div>
            