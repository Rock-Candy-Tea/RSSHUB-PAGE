
---
title: 'MMORPG技能管线设计经验总结'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202208/11/090339utvlns8cvt1ny6y6.png'
author: GameRes 游资网
comments: false
date: Thu, 11 Aug 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202208/11/090339utvlns8cvt1ny6y6.png'
---

<div>   
<i><font color="#808080">以下文章来源于腾讯游戏学堂 ，作者Console</font></i><br>
<br>
表现丰富、机制多变的技能作为MMORPG游戏战斗体验的核心组成部分，是吸引玩家的一大亮点，本文总结了笔者在MMORPG技能系统设计上的一些经验，供大家参考。<br>
<br>
<strong><font color="#de5650">一、设计思路</font></strong><br>
<br>
早期的MMORPG手游中，技能的表现相对简单，因此技能流程被分为几个固定的阶段（如准备阶段、攻击阶段、受击阶段），可以实现成一个简单的由服务器消息驱动的状态机，策划只需要配置一下切换状态的条件和不同状态的表现（特效、动画、音效等）。这种方式实现比较简单，但由于流程固化，对于实现机制复杂的技能时，往往需要进行编码实现，效率不高。因此一个好的技能系统应该是由数据驱动的，能让策划能自由组合配置。<br>
<br>
当前数据驱动的技能系统的有以下几个例子：<br>
<br>
<strong>1.1 Dota2技能系统</strong><br>
<br>
Dota2技能系统定义了Event、Action、Modifier等技能行为，由策划配置Key-Value的Json或Lua来自由组合，游戏运行时会将策划配置的文件解析成技能树。这种实现可以通过Key进行复用，但是当策划定义的Key数量过多时，学习成本将会比较高，而且技能流是文本型，不易于理解技能流程。<br>
<br>
<strong>1.2 守望先锋技能系统</strong><br>
<br>
守望先锋使用暴雪的脚本系统Statescript来实现技能系统。Statescript是一个可视化的脚本语言；每一个脚本都是一组互相连接的节点（node）形成的图（graph），代表了一段游戏逻辑的实现。当一个脚本运行时，它会创建一个运行时对象，这里称之为脚本实例（instance），每一个实例都被一个实体（entity）所拥有。实体上的脚本实例可以被动态地添加和删除，同一个实体上可以同时运行同一个脚本的多个实例。<br>
<br>
<div align="center">
<img aid="1049491" zoomfile="https://di.gameres.com/attachment/forum/202208/11/090339utvlns8cvt1ny6y6.png" data-original="https://di.gameres.com/attachment/forum/202208/11/090339utvlns8cvt1ny6y6.png" width="600" id="aimg_1049491" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/090339utvlns8cvt1ny6y6.png" referrerpolicy="no-referrer">
</div><br>
如上图所示，Statescript节点包括入口（Entry）、条件（Condition）、动作（Aciton）、状态（State），由程序员来实现这些具体的Action或State，然后策划就可以使用Statescript来自由组合自己想要的技能。<br>
<br>
可以看出Statescript其实并不是单独为了技能实现的，而是一个通用的脚本系统，只要提供的节点类型足够多的话，策划可以用来实现很多逻辑。这对于策划对各种节点的熟悉程度和编程能力有一定的要求。<br>
<br>
<strong>1.3 UE4 Gameplay Ability System</strong><br>
<br>
UE4 GAS是官方提供的依赖UE4 Gameplay框架的一个技能系统。基本构成如下：<br>
<br>
<ul><li><strong>Ability SystemComponent：</strong>技能运行时组件，控制技能的运行和相关属性的改变；</li><li><strong>Ability：</strong>技能，通过蓝图配置技能实例，包含较完整的技能逻辑，运行时可以动态地添加给角色的技能系统，或从技能系统中删除；</li><li><strong>Attribute和AttributeSet，属性和属性集。</strong>Attribute代表角色的某种属性，如血量、能量等，属性集表示一组属性的集合；</li><li><strong>Tags，标签，</strong>代表了某种状态。通过不同的Tag来表示角色当前的状态，如燃烧、虚弱等，类似角色身上的Buff；</li><li><strong>Gameplay Effect，技能效果，</strong>表示对某些Attribute和Tag的修改，例如一个火球术造成的GE可以是造成血量减50，同时将角色变成燃烧状态；</li><li><strong>Ability Tast，技能任务</strong>，表示技能过程中要执行的一个逻辑，例如播放动作等。<br>
</li></ul><br>
<div align="center">
<img aid="1049492" zoomfile="https://di.gameres.com/attachment/forum/202208/11/090340y2so712isbhd2nqb.png" data-original="https://di.gameres.com/attachment/forum/202208/11/090340y2so712isbhd2nqb.png" width="600" id="aimg_1049492" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/090340y2so712isbhd2nqb.png" referrerpolicy="no-referrer">
</div><br>
GAS系统也可以通过实现特定的Task和Effect，然后由策划自由组合，由于蓝图编辑器的可视化，可以清晰地看出技能的流程。<br>
<br>
<strong>1.4 MMORPG技能系统的特点</strong><br>
<br>
以上列举了三种优秀的数据驱动的技能系统的实现方案，通过对技能基础组成部分的抽象来实现技能流程的原子化，并基于此提供了自由组合、数据驱动的能力，大大提高了策划开发新技能的效率和自由度。上述三个技能方案来源于MOBA和射击游戏，这类游戏技能成长性相对简单。但是对于MMORPG游戏而言，技能数值的成长性也是技能系统的重要组成部分，因此在数据驱动、自由组合的设计原则上，技能成长数值的配置的便捷性也需要考虑进去。<br>
<br>
<strong><font color="#de5650">二、MMORPG技能系统分析</font></strong><br>
<br>
明确了数据驱动的设计思路后，首先需要分析下技能数据的组成。对于成长性的技能数值，例如不同等级伤害不同，我们可以继续按照数值策划的习惯，将它们保留在Excel里。而对于相同的技能，不管多少级，技能的流程和机制是一样的，这一部分我们就可以参考上述例子，将技能流程进行抽象，并交给策划自由组合搭配。<br>
<br>
<strong>2.1 技能流程抽象</strong><br>
<br>
一般MMORPG游戏的技能可以定义为通过特定的规则修改技能选点/目标后，执行技能表现并结算技能效果，流程可以总结如下：<br>
<br>
<div align="center">
<img aid="1049493" zoomfile="https://di.gameres.com/attachment/forum/202208/11/090340elfssm9j00mj1duf.png" data-original="https://di.gameres.com/attachment/forum/202208/11/090340elfssm9j00mj1duf.png" width="600" id="aimg_1049493" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/090340elfssm9j00mj1duf.png" referrerpolicy="no-referrer">
</div><br>
以一个常见的火球术为例，代入到上述流程图，技能过程可以描述为玩家释放技能时，首先检测目标是否在射程范围内，如果在范围内，且未被打断，则开始播放施法动画并朝目标发射火球，火球命中目标后，进行伤害结算，并播放目标的受击表现。<br>
<br>
将技能流程进一步抽象，可以得到三种类型的流程节点：<br>
<br>
规则类型：例如选目标规则、结算规则、条件判断等<br>
<br>
流程类型：分支流程、并行流程、循环流程等<br>
<br>
表现类型：动作、音效、特效等<br>
<br>
类似第一部分的三个例子，可以由开发实现不同Action或Task，交由策划自由组合，即可实现技能流程的数据驱动。但是这里如何确定抽象粒度呢？对于程序来说，将这些节点全部原子化的话，是最简单的，类似UE的GAS的设计思路，可以设计很多的Task，例如播放蒙太奇、播放特效等，搭配上很多的Effect，那功能就足够强大足够灵活。这样带来的一个问题就是，当节点实现的功能足够细的情况下，对于大致相同的技能流程，会出现“一千个读者心中有一千个哈姆雷特”的情况（如果大家的项目使用过UE蓝图进行开发，就能大致理解），也就是不同的策划完全能组合出看起来完全不同的流程图，这样既不方便学习，也不方便调试。因此我们尝试从业务层上进行抽象，抽象的原则是理解直观，学习门槛低，且类型可收敛。<br>
<br>
回到上面的流程图，我们和策划一起梳理了我们已经上线的一个MMORPG项目现存的几百个技能，从业务侧总结出了这样的一组节点：<br>
<br>
<div align="center">
<img aid="1049494" zoomfile="https://di.gameres.com/attachment/forum/202208/11/090340e8r5xv84xkq8vx8q.png" data-original="https://di.gameres.com/attachment/forum/202208/11/090340e8r5xv84xkq8vx8q.png" width="600" id="aimg_1049494" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/090340e8r5xv84xkq8vx8q.png" referrerpolicy="no-referrer">
</div><br>
我们将节点分为入口、同步、流程控制和表现等几个类型。开始节点里的配置内容主要是技能的一些释放条件；请求节点比较特殊，里面配置的是选点/选目标逻辑和结算效果，主控客户端会计算选点/选目标结果，同步后服务端会进行校验和结算，然后广播结算结果；流程控制节点里配置的是判断技能流程走向的条件；表现节点里配置动画、特效等表现数据。<br>
<br>
这一类策划易于理解的业务节点实际上是由一系列的原子化功能的组合，例如在动作节点里，除了动画配置外，还会有特效、音效、震屏等表现的配置。这样抽象的话，不仅可以收敛类型，还可以保证对于相同机制的技能，不同策划配置出来的流程图基本一致，开发调试的时候也易于理解这个技能的整体流程（对于如何确定抽象粒度，其实每个项目组都有各自的取舍，这里并没有一个通用的标准，只是看是否适合当前项目）。例如一个火球术就可以表现为：<br>
<br>
<div align="center">
<img aid="1049495" zoomfile="https://di.gameres.com/attachment/forum/202208/11/090341c5ljleh6l6qof1lo.png" data-original="https://di.gameres.com/attachment/forum/202208/11/090341c5ljleh6l6qof1lo.png" width="600" id="aimg_1049495" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/090341c5ljleh6l6qof1lo.png" referrerpolicy="no-referrer">
</div><br>
第一个请求节点通知服务端技能开始了，主控端开始预表现，服务端校验目标合法性并广播，收到消息的客户端执行后续动作和弹道表现，主控端弹道终点会再次通知服务端，服务端结算并广播结算结果。<br>
<br>
至此我们可以确定一个技能数据分为技能表里的成长性数值数据加上技能蓝图数据，技能表里一个技能可以索引一个技能蓝图配置（多对一，例如不同等级的火球术索引同一个技能蓝图）。对于抽象出来的节点，我们使用protobuf定义，并保存成Json文件，运行时通过技能ID索引到对应的技能蓝图来构造一棵树，并根据服务器同步的动态数据来Tick这棵树的执行。除了配置好的静态数据之外，技能运行时过程中会产生目标、选点等动态数据。我们的请求节点客户端侧的主要工作是同步这些发生变化的动态数据（这里称为技能上下文），客户端在每个请求节点收到服务端广播的上下文变更后，后续的表现节点就会基于新的上下文进行表现。<br>
<br>
<strong>2.2 技能运行时设计</strong><br>
<br>
技能运行时我们采用了类似GAS的设计，核心是角色身上挂载的技能组件。技能组件负责维护技能实例，并管理技能实例的生命周期。<br>
<br>
<div align="center">
<img aid="1049496" zoomfile="https://di.gameres.com/attachment/forum/202208/11/090341ipqq75gaubnr2q15.png" data-original="https://di.gameres.com/attachment/forum/202208/11/090341ipqq75gaubnr2q15.png" width="600" id="aimg_1049496" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/090341ipqq75gaubnr2q15.png" referrerpolicy="no-referrer">
</div><br>
技能运行时针对上述抽象出来的每个技能流程节点，实现了一个对应的运行时SkillAction。这些Action的创建由服务器同步的技能上下文来驱动创建。前一节简单介绍了上下文的概念，它包含了经过服务器验证的动态数据，如新选点、新目标、结算效果等。客户端收到一个新的上下文后，会创建一个Action组，每个Action组维护该上下文后续表现节点的运行。一个技能如果有多个请求同步节点的话，会创建多段上下文，每个上下文驱动它后续节点的运行。<br>
<br>
<div align="center">
<img aid="1049497" zoomfile="https://di.gameres.com/attachment/forum/202208/11/090341uuil77zaa8udz3ao.png" data-original="https://di.gameres.com/attachment/forum/202208/11/090341uuil77zaa8udz3ao.png" width="600" id="aimg_1049497" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/090341uuil77zaa8udz3ao.png" referrerpolicy="no-referrer">
</div><br>
技能的同步发生于技能流程的请求节点处，一般需要同步的原因是动态数据的变更。例如一个弹射技能，在多个目标间弹射时会发生多次目标变更，这就需要多次同步。同步方式是主控端发起并预表现，服务器校验并广播，主控端收到经校验的数据后会进行修正，模拟客户端收到广播包后进行后续表现。<br>
<br>
为了主控客户端的体验，技能开始后，会预测下一次同步时间，并在下次同步点之前发送同步包，保证收到服务器回包时刚好执行到同步点可以无缝执行后续逻辑。弱网环境下走到同步点未收到同步包的情况下，会预表现动画、特效等，收到回包后会对预表现进行修正：若服务器同步数据和当前一致，则继续当前表现；若不一致，例如预表现的位移和服务器下发的不同，在阈值范围内，根据时间戳向新位置加速插值表现，超过阈值的话则直接拉到新位置，防止和服务器位置差距过大。这个预发包的方式是在客户端实现了个技能中间层，主要功能是转发上下行的技能包，并预测下一个同步时间。<br>
<br>
<div align="center">
<img aid="1049498" zoomfile="https://di.gameres.com/attachment/forum/202208/11/090341nstyyon5z8ensprr.png" data-original="https://di.gameres.com/attachment/forum/202208/11/090341nstyyon5z8ensprr.png" width="600" id="aimg_1049498" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/090341nstyyon5z8ensprr.png" referrerpolicy="no-referrer">
</div><br>
技能的结算部分被抽象成效果，效果ID表示效果的功能（如修改属性、增删Buff等），一个效果里可以配置参数、条件、概率等，且可以被技能、Buff等多个数值系统复用。<br>
<br>
<strong><font color="#de5650">三、工具链支持</font></strong><br>
<br>
确定了技能数据和运行时结构后，就需要提供配套的工具链支持：一个方便易用的技能编辑器。对于不同的使用者，对编辑器的要求是不一样的：<br>
<br>
对于策划/美术：编辑器需要易于配置，即改即用，因此我们需要提供一个易于上手和使用的配置界面，且需要热更新功能；<br>
<br>
对于开发：针对技能系统出现的bug，需要能迅速定位问题，因此我们需要提供运行时流程可视化和网络消息日志功能。<br>
<br>
<strong>3.1 技能编辑器介绍</strong><br>
<br>
<div align="center">
<img aid="1049499" zoomfile="https://di.gameres.com/attachment/forum/202208/11/090341kitu1i0evhk0qqz9.png" data-original="https://di.gameres.com/attachment/forum/202208/11/090341kitu1i0evhk0qqz9.png" width="600" id="aimg_1049499" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/090341kitu1i0evhk0qqz9.png" referrerpolicy="no-referrer">
</div><br>
我们项目经历过换引擎的过程，在Unity上，我们开发了基于GraphView节点编辑器的技能配置界面，转到UE4后，使用蓝图的底层框架UEdGraph将这个配置界面移植了过来，如上图所示。这个编辑器左边展示了技能的基础信息，上面是技能关联的Excel表格信息预览，中间是节点配置界面，右侧是选中某个节点后的详情配置面板。<br>
<br>
策划在可以选择基于一个已有的技能模板或者新建一个技能蓝图，进行技能流程的配置。当策划只想预览技这个技能的动画、特效等客户端表现时，可以使用离线预览模式，直接在编辑器中看技能的表现效果。<br>
<br>
如果策划想看游戏中的实时表现，也可以在PIE运行模式下登录到服务器，修改完成后将当前技能配置热更新到服务器，同时替换当前游戏内存，并装配到主角或者目标，然后就可以实时地预览游戏内效果，不仅包含了技能表现，也包含了结算等数值结果。同时打开技能编辑器的调试信息开关，还可以绘制出技能结算的碰撞检测范围和技能位移路径，将选点、结算范围、路径等数据可视化，让策划一眼看出技能配置是否符合预期。<br>
<br>
另外，我们还提供了技能流程的可视化能力，当绑定到施法角色时，技能运行过程中会高亮当前正在执行的技能节点，同时将客户端和服务端通信的网络消息日志打印出来，可以帮助开发快速定位技能bug。<br>
<br>
<div align="center">
<img aid="1049500" zoomfile="https://di.gameres.com/attachment/forum/202208/11/090342l8zdy38hym1h1vey.png" data-original="https://di.gameres.com/attachment/forum/202208/11/090342l8zdy38hym1h1vey.png" width="600" id="aimg_1049500" inpost="1" src="https://di.gameres.com/attachment/forum/202208/11/090342l8zdy38hym1h1vey.png" referrerpolicy="no-referrer">
</div><br>
<strong>3.2 工具开发总结</strong><br>
<br>
工具开发对于提高效率的帮助是巨大的。对于一个设计好的数据驱动的系统，虽然新功能的开发可以完全交给策划去配置验证，但是如果配置完的数据需要重新启动加载，重新走登录流程看效果，那么调试的成本会非常高。方便快捷的热更新功能和游戏内可视化能力，对于技能系统这样的实时模块而言重要性不言而喻。在新项目中应用的这一套技能制作管线，对比我们项目组已上线的一款MMORPG手游中传统的技能制作方式，效率有了数量级的提升。<br>
<br>
<strong><font color="#de5650">总结</font></strong><br>
<br>
本文是我近两年开发MMORPG游戏战斗系统的一个总结，网上已经有很多技能系统设计的分享，我也将自己的心得体会记录一下，抛砖引玉，希望能给大家一个参考。随着游戏越来越重度化，我也认识到游戏内容（例如本文着重描述的技能）制作管线的重要性，因为一个好的制作管线将大幅提高内容的产出效率。对于Gameplay程序员而言，如何将策划的需求抽象成一个数据驱动的系统，并配套开发相应的制作管线，将成为一种核心能力。<br>
<br>
<font size="2"><font color="#808080"><strong>参考资料：</strong></font></font><br>
<font size="2"><font color="#808080">1. 《守望先锋》网络脚本化的武器和技能系统：https://www.lfzxb.top/ow-gdc-weapon-and-skillsystem/</font></font><br>
<font size="2"><font color="#808080">2. 虚幻四Gameplay Ability System学习资料：https://zhuanlan.zhihu.com/p/368201577</font></font><br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：腾讯游戏学堂</font></font><br>
<br>
  
</div>
            