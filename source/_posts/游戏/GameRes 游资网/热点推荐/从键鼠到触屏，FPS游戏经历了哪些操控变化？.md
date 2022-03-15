
---
title: '从键鼠到触屏，FPS游戏经历了哪些操控变化？'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202203/02/110752dvyeyz4yufur6366.jpg'
author: GameRes 游资网
comments: false
date: Wed, 02 Mar 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202203/02/110752dvyeyz4yufur6366.jpg'
---

<div>   
<strong>编者按</strong> 在笔者的个人项目经验里，FPS品类的项目经验占据了2/3。回想初中时代热衷在【CF】里面的守望之城对狙；工作后也有更多条件购买3A大作，光环、命运、…然后到多人对战的守望、APEX等等，我属于典型的【人菜枪马瘾大】，再到后来很荣幸有机会参与Marvel、APEX等游戏制作。所幸能得到很多资深策划、设计师的指点，过程中有许多零散的思考，借此浅谈一些在设计中遇到的问题和解决方法，篇幅有限无法涵盖所有，不足请见谅：）<br>
<br>
<strong>作者：阿泽</strong><br>
<font size="2">（本文内容由公众号“阿泽与设计”提供，转载请征得同意。文章仅为作者观点，不代表GWB立场）</font><br>
<br>
本系列打算分为几篇，本篇主要为大家分享“基础操控”相关的内容：<br>
<br>
*下方FPS泛指射击类，非标准第一人称<br>
<br>
#1 基础操控<br>
<br>
#2 枪械<br>
<br>
#3 战场信息篇<br>
<br>
#4 技能交互篇<br>
<br>
……<br>
<br>
<div align="center">
<img aid="1032350" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110752dvyeyz4yufur6366.jpg" data-original="https://di.gameres.com/attachment/forum/202203/02/110752dvyeyz4yufur6366.jpg" width="600" id="aimg_1032350" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110752dvyeyz4yufur6366.jpg" referrerpolicy="no-referrer">
</div><br>
在FPS游戏中，移动、瞄准、射击是最基础的操控体验。在传统PC端的FPS游戏中，操控体验通常是由键鼠两种硬件组成，键盘主要是负责控制移动操控（跑、跳、蹲、趴等行为）的【下半身】操作，鼠标为操控开火射击、转视角等【上半身】操作，左右手的精细分工帮助玩家的大脑有清晰的指令指示，宽敞的屏幕可以让玩家的视觉焦点就集中在屏幕的准心范围，命中敌人后的强视觉冲击的击杀反馈…这些基础的体验构成了射击游戏的乐趣。<br>
<br>
<div align="center">
<img aid="1032351" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110753hndyitinet9rokv0.png" data-original="https://di.gameres.com/attachment/forum/202203/02/110753hndyitinet9rokv0.png" width="600" id="aimg_1032351" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110753hndyitinet9rokv0.png" referrerpolicy="no-referrer">
</div><br>
XBOX、PS4的主机玩家则是通过体验高度集成化的硬件【手柄】来获取射击体验；玩家仅需要操控一个硬件设备即可完成所有游戏行为。相比于【键鼠】双手控制的分离，又受到环境因素限制（桌子高度、鼠标垫等等），双手握持的方式能够最大限度保持肢体的体验自由度，比如随意弯曲、垂放摆动；另外双手的【握持感】也能够让感官更加集中，感受十字键和L/R键按下回弹阻尼带来的【压力感】差异，利用肌肉记忆去完成射击体验。<br>
<br>
<div align="center">
<img aid="1032352" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110754txdq3ldq2p1dhpds.png" data-original="https://di.gameres.com/attachment/forum/202203/02/110754txdq3ldq2p1dhpds.png" width="600" id="aimg_1032352" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110754txdq3ldq2p1dhpds.png" referrerpolicy="no-referrer">
</div><br>
不同于红白机时代的生硬触感，在射击游戏中通常还会有配合被命中时马达震动带来的【震感】反馈，从视觉、听觉、触觉三方面带给玩家更好的沉浸感。但手柄玩 FPS 最具有争议的大概就是【辅助瞄准】功能，原因是手柄无法像鼠标一样快速进行定位瞄准，精度与准确度较差。因此系统会一定范围内把准心自动瞄准在敌人身上，这些成了许多玩家对玩 FPS 用手柄的【诟病】，但个人认为也绝不会达到自瞄或者开挂的程度。<br>
<br>
在移动设备快速普及的时代，用户可以更用直接的交互方式获得操控感，双手的拇指【搓屏幕】也成为大众习以为常的游戏体验。手游为游戏带来了更多的场景便利性和大量新增玩家，但移动端的操控问题也很明显：各式各样的虚拟摇杆和按钮，再加上双手手指的遮挡和覆盖，给玩家留下的屏幕区域仅剩三分之二大小，数量繁多的操作…部分手机为了满足游戏体验则在边缘增加类似手柄的按键，但拥有游戏手机的玩家始终是少数，如何为更多玩家优化操作体验是做FPS手游必须重点解决的问题。<br>
<br>
<div align="center"><font size="2">
<img aid="1032353" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110754b5l9bnnndj6q5llx.png" data-original="https://di.gameres.com/attachment/forum/202203/02/110754b5l9bnnndj6q5llx.png" width="600" id="aimg_1032353" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110754b5l9bnnndj6q5llx.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">手指带来的遮挡</font></div><br>
<div align="center">
<img aid="1032354" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110755xbb0gl0hmblp0bpz.jpg" data-original="https://di.gameres.com/attachment/forum/202203/02/110755xbb0gl0hmblp0bpz.jpg" width="600" id="aimg_1032354" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110755xbb0gl0hmblp0bpz.jpg" referrerpolicy="no-referrer">
</div><br>
早期移动端的考虑到玩家手指操作的灵活度，通常主要是以玩家双手握持手机时用拇指操作的方式为主（简称二指玩家），王者荣耀的成功也离不开对MOBA类游戏的功能和操作进行简化，2.5D的固定视角只需要通过移动和释放技能就可以完成，很好的兼顾了大部分普通人使用左右手指进行交互的操作习惯。<br>
<br>
<div align="center">
<img aid="1032355" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110755t0704xz4ctnhphhc.png" data-original="https://di.gameres.com/attachment/forum/202203/02/110755t0704xz4ctnhphhc.png" width="600" id="aimg_1032355" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110755t0704xz4ctnhphhc.png" referrerpolicy="no-referrer">
</div><br>
在FPS的手游，由于加入了自由操控视野的操作，玩家需要操控【视角】才能精准的射击到移动的敌人，然而【视角】是需要根据玩家自身状态去自主判断。不同于ACT等游戏类型的技能会【自动锁定】敌人的机制，FPS所依赖的是玩家在多次射击中所沉淀下来的肌肉记忆和反应，只有通过操控视角锁敌才能达成精准击杀目标，【对枪竞技】也是FPS的乐趣所在。因此在FPS类型中【转视角】就成为了又一个核心的操控功能。于是如何同时完成【移动】【转视角】【射击】就成为了二指玩家的体验痛点。<br>
<br>
<div align="center"><font size="2">
<img aid="1032356" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110756bmq2ddp3wdd1xq1m.png" data-original="https://di.gameres.com/attachment/forum/202203/02/110756bmq2ddp3wdd1xq1m.png" width="600" id="aimg_1032356" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110756bmq2ddp3wdd1xq1m.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">阿尔法机动都市</font></div><br>
为了满足玩家在3D环境中通过【二指】操作去获得较好的射击体验，目前大部分FPS手游的基础操作都会有一些设置选项，左手移动都是通用的移动操作，而右手则有更多的选择性：：单按钮开火、跟随转视角开火、全屏开火三种基础模式。<br>
<br>
<div align="center"><font size="2">
<img aid="1032357" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110757nppm7rfip1gpzbpr.jpg" data-original="https://di.gameres.com/attachment/forum/202203/02/110757nppm7rfip1gpzbpr.jpg" width="600" id="aimg_1032357" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110757nppm7rfip1gpzbpr.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">PUBGM-自定义键位</font></div><br>
即便有多个模式选择，但每个模式都有自己的局限性，比如【点击开火】时没办法转视角；或者【开火跟随转视角】时也会带来部分弹药浪费的问题；又比如有些FPS加入了【瞄准即自动开火】，但也只适合TTK短的游戏，对于有弹药限制，并且长时间收集物资且无法复活的模式则并不适合。<br>
<br>
<div align="center"><font size="2">
<img aid="1032358" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110758vn02yqynwezf7len.png" data-original="https://di.gameres.com/attachment/forum/202203/02/110758vn02yqynwezf7len.png" width="600" id="aimg_1032358" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110758vn02yqynwezf7len.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">CODM-自定义键位</font></div><br>
<div align="center">
<img aid="1032359" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110758k0884wz0c254clz5.jpg" data-original="https://di.gameres.com/attachment/forum/202203/02/110758k0884wz0c254clz5.jpg" width="600" id="aimg_1032359" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110758k0884wz0c254clz5.jpg" referrerpolicy="no-referrer">
</div><br>
在FPS手游就必须提到【自定义】系统。<br>
<br>
随着部分玩家的熟练度和操作能力提高，自定义则是满足他们需求的需求必备功能，越来越多的三四指/C 手（或更多）教学传播。这种操作方式其实是映射手柄一样的操作方式，左上/右上通常都会通过自定义去修改和放大某个按钮控件，并且选择用【食指】控制。<br>
<br>
<div align="center"><font size="2">
<img aid="1032360" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110759n1mm6a6bbspe36zp.png" data-original="https://di.gameres.com/attachment/forum/202203/02/110759n1mm6a6bbspe36zp.png" width="600" id="aimg_1032360" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110759n1mm6a6bbspe36zp.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">三四指布局与B站教学</font></div><br>
由于【食指】的灵活性相对较低，因此通常都是【开火】【跳跃】这类简单的点触行为。虽然【三四指方案】能一定程度解决二指的困境，但由于手指的习惯差异性，目前也缺乏较为通用的布局方案；对大部分玩家来说会依旧会有手指灵活度问题。但反观来看，许多玩家都视为这是一种进阶的操作，对于FPS 这类游戏而言，由于缺乏MMO养成的长线成长，从操作上作为FPS 的长线成长也不失为一种好的运营方式。<br>
<br>
<div align="center">
<img aid="1032361" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110759vuddisprjvusu9xx.jpg" data-original="https://di.gameres.com/attachment/forum/202203/02/110759vuddisprjvusu9xx.jpg" width="600" id="aimg_1032361" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110759vuddisprjvusu9xx.jpg" referrerpolicy="no-referrer">
</div><br>
面对局内几十个可操作的按钮和信息（以和平精英的HUD 布局为例），设计师是通过怎样的设计逻辑来放置这些按钮的位置呢？<br>
<br>
我认为可以有评估维度逻辑：操作热区—功能优先级—按钮位置<br>
<br>
由于屏幕的物理局限和手指的操作习惯等因素，无法让所有的功能都处于最好的手指点击位置。我认为按钮的位置是需要根据玩法本身的使用频率来进行决策，因此需要先对操作热区进行判断，例如通常可以考虑分为三个操作热区：<br>
<br>
<div align="center"><font size="2">
<img aid="1032362" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110759g9hoxxzmtmfhd2dd.png" data-original="https://di.gameres.com/attachment/forum/202203/02/110759g9hoxxzmtmfhd2dd.png" width="600" id="aimg_1032362" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110759g9hoxxzmtmfhd2dd.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">和平精英-自定义为例</font></div><br>
<strong>一级热区：定义为操作频率最高，</strong>也是手指交互成本最低的区域，这个区域通常都是基础移动、开火这类基础体验，会直接影响玩家是否可以完成一个基础的射击操控；<br>
<br>
<strong>二级热区：这个区域通常也是比较核心的操作区域，</strong>我们可以定义为是能够辅助玩家更好的完成射击操作；例如转视角、瞄准，场景互动开关等；<br>
<br>
<strong>三级热区：这个区域可以明显的感受到对于二指操作的玩家而言已经比较困难，这些区域的位置的按钮通常会放置与玩法、沟通、队伍互动相关的按钮，</strong>这类操作频率较低，并且可以大多数处于非战斗场景下使用，因此该区域的按钮尺寸也相对较小。<br>
<br>
在定义了基本的操作热区后，设计师可以根据机制/使用场景的需要，从功能体验的优先级维度进行一个基础排序，比如：移动>开火>转视角、跑跳蹲等等。<br>
<br>
许多 FPS 也会根据自己的战斗节奏和场景进行基础操作体验的优先级排序，或者针对不同的模式进行调整。例如在【PUBGM】的BR模式中，由于地图尺寸和玩法因素，玩家需要长时间搜集物资和跑图，整体游戏节奏的TTK 较长， 因此换弹的频率相对较低，因此换弹的位置和按钮尺寸可以相对校小。<br>
<br>
<div align="center">
<img aid="1032363" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110800lr2b52bfci6mdmmr.png" data-original="https://di.gameres.com/attachment/forum/202203/02/110800lr2b52bfci6mdmmr.png" width="600" id="aimg_1032363" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110800lr2b52bfci6mdmmr.png" referrerpolicy="no-referrer">
</div><br>
反观【CODM】主打的MR团队竞技模式，更多围绕在火力比拼、快速复活的战斗节奏，TTK相对较短，此时的【换弹按钮】频率会更多，其位置和尺寸也会更加紧凑和大一些，方便玩家以最小交互成本快速点击。<br>
<br>
<div align="center">
<img aid="1032364" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110801yz3qokbor2uow1d0.png" data-original="https://di.gameres.com/attachment/forum/202203/02/110801yz3qokbor2uow1d0.png" width="600" id="aimg_1032364" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110801yz3qokbor2uow1d0.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1032365" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110801p7futoon77l7opao.jpg" data-original="https://di.gameres.com/attachment/forum/202203/02/110801p7futoon77l7opao.jpg" width="600" id="aimg_1032365" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110801p7futoon77l7opao.jpg" referrerpolicy="no-referrer">
</div><br>
随着使用场景多样化也会有更多细分的操控设计，可以试想一个场景：当你在使用瞄准时突然在视野出现敌人，由于瞄准视野的狭窄和敌人的快速移动，导致你无法瞄准，没反应过来就直接over了，传统流程需要关闭【瞄准镜】才能脱离视野。因此有些FPS会加入【越肩视角】开火来确保有更充分的射击视野，同时也减少晃动带来的影响。<br>
<br>
<div align="center">
<img aid="1032366" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110802gdgfxpno62ktktke.png" data-original="https://di.gameres.com/attachment/forum/202203/02/110802gdgfxpno62ktktke.png" width="600" id="aimg_1032366" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110802gdgfxpno62ktktke.png" referrerpolicy="no-referrer">
</div><br>
许多FPS手游也会加入差异性体验设计，比如在角色操控方面，APEX手游还原PC 端的身法操作，实现了【滑铲跳】等进阶操作组合；【和平精英】内的蹦蹦车、摩托车等载具，这些载具操作沿用映射现实的操作认知，玩家也可以自定义选择【赛车手游】的操控方式；还有【CODM】在战场加入了直升机的载具操作，从原本的XY轴变成XYZ轴体验。<br>
<br>
<div align="center">
<img aid="1032367" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110803k2g3lw95fp32xll2.jpg" data-original="https://di.gameres.com/attachment/forum/202203/02/110803k2g3lw95fp32xll2.jpg" width="500" id="aimg_1032367" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110803k2g3lw95fp32xll2.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1032368" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110803cgkv89lvflsl11z2.jpg" data-original="https://di.gameres.com/attachment/forum/202203/02/110803cgkv89lvflsl11z2.jpg" width="600" id="aimg_1032368" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110803cgkv89lvflsl11z2.jpg" referrerpolicy="no-referrer">
</div><br>
不久前和同事讨论的时候也会有提到：现在手游的FPS的局内布局相似度很高。我觉得一个 FPS 的战斗布局可能受到几个因素的影响：<br>
<br>
<strong>1.大盘玩家的通用操作习惯</strong><br>
<br>
<strong>2.单局玩家的战斗节奏</strong><br>
<br>
<strong>3.玩法/机制差异性</strong><br>
<br>
相信经历过FPS设计的朋友在项目初期，甚至迭代期也在都会尝试过不同的布局方案，但最终在玩家测试的时候还是并没有得出比较好的反馈。但完全按照市面上的竞品放置就可以了吗？我觉得可能要遵循另一条基础原则：通用体验一致化，差异体验创新。<br>
<br>
<strong>通用体验：</strong><br>
<br>
指玩家最常使用的行为操控：跑跳蹲趴，这些基础操作位置对玩家来说已经形成惯性的肌肉，尽量用最通用的操作去满足；<br>
<br>
<strong>差异体验：</strong><br>
<br>
结合游戏本身的操作进行设计，例如守望中【技能】作为每个英雄的特点，才能建立起壁垒和操作特点。<br>
<br>
反过来看，可能我认为重点不在于设计出差异化方案，考虑的不仅仅只是UI或者UX体验的差异化，而是需要站在更高维度的思考方案能够帮到项目起到怎样的作用，这也是设计价值的体现。<br>
<br>
<div align="center">
<img aid="1032369" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110803c98q8qtupfzepd9q.png" data-original="https://di.gameres.com/attachment/forum/202203/02/110803c98q8qtupfzepd9q.png" width="600" id="aimg_1032369" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110803c98q8qtupfzepd9q.png" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1032370" zoomfile="https://di.gameres.com/attachment/forum/202203/02/110804j707z480v7v7nrne.jpg" data-original="https://di.gameres.com/attachment/forum/202203/02/110804j707z480v7v7nrne.jpg" width="600" id="aimg_1032370" inpost="1" src="https://di.gameres.com/attachment/forum/202203/02/110804j707z480v7v7nrne.jpg" referrerpolicy="no-referrer">
</div><br>
在设计FPS类游戏的前期，局内的基础操控是最经常会 battle ，也是最常见的反馈就是：<br>
<br>
<strong>1：XXX按钮太小，玩家会点不到</strong><br>
<br>
<strong>2：XXX按钮太大，这样又容易误操作</strong><br>
<br>
这两者本身在设计上就是矛盾，通常手指的点击热区大约为44pix（不同分辨率下有差异），比较容易把自己主观的使用场景去代入。即便是通过玩家测试，在样本量有限的情况下，玩家的机型、手指变量等因素都会对CE 结果会有不一样的变动，很难客观的完全还原真实情况，需要结合设计师的经验进行判断。因此我认为解决这个问题的可以考虑三种方法：<br>
<br>
1：根据已有竞品的尺寸和位置，结合自身的使用场景进行整理罗列，明确该体验的优先级以及使用频率，综合优缺点带来的正收益/负收益最后来作为评估按钮大小的依据，做到设计有理有据。<br>
<br>
2：较小的按钮在不影响其他操作的情况下【操作热区】放大，确保操作体验流畅。<br>
<br>
3：必要场景下进行取舍，运用简约的四原则：删除、隐藏、组织、转移。<br>
<br>
以上就是本次的浅谈，感谢阅读：）<br>
<br>
<font size="2"></font><br>
<font size="2">来源：腾讯GWB游戏无界</font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/8JGy-5igYsx_d60vxRMekQ</font><br>
<br>
<br>
  
</div>
            