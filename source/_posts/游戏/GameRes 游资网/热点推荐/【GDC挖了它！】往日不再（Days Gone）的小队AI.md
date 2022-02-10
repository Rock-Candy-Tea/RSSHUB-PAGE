
---
title: '【GDC挖了它！】往日不再（Days Gone）的小队AI'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202202/07/111827b2z2sb6zt28k212v.jpg'
author: GameRes 游资网
comments: false
date: Mon, 07 Feb 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202202/07/111827b2z2sb6zt28k212v.jpg'
---

<div>   
<div align="center">
<img aid="1029919" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111827b2z2sb6zt28k212v.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111827b2z2sb6zt28k212v.jpg" width="600" id="aimg_1029919" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111827b2z2sb6zt28k212v.jpg" referrerpolicy="no-referrer">
</div><br>
<font size="2"><font color="#696969">作者：一袋甜蕉宋球长</font></font><br>
<font size="2"><font color="#696969">知乎主页：https://www.zhihu.com/people/jerrylovemeow/posts</font></font><br>
<br>
<font size="2"><font color="#696969">GDC年份：2021</font></font><br>
<font size="2"><font color="#696969">GDC原标题：AI Summit: Squad Coordination in 'Days Gone'</font></font><br>
<font size="2"><font color="#696969">GDC Vault链接：</font></font><br>
<font size="2"><font color="#696969">https://gdcvault.com/play/1027237/AI-Summit-Squad-Coordination-in</font></font><br>
<font size="2"><font color="#696969">主讲人：Tobias Karlsson</font></font><br>
<font size="2"><font color="#696969">所属：Sony Bend Studio</font></font><br>
<br>
<font color="#696969">摘要</font><br>
<br>
<font color="#696969">这个GDC演讲分享了Days Gone的人类势力小队AI运作机制，主要用于Days Gone中不同人类势力之间的交战，也可用于对抗玩家。这套机制考虑到了AI的站位分布、进攻角色、战斗阵地等问题，其核心概念包括战线、战斗区、信心值、战斗角色等。</font><br>
<font color="#696969"><br>
</font><br>
<font color="#696969">考虑到Days Gone的大世界末世生存游戏性质，这套机制其实更侧重于表演而非实用战斗，用来构建玩家对整个世界的理解，玩家在这套机制中更多是被作为观众来处理的。</font><br>
<font color="#696969"><br>
</font><br>
<font color="#696969">另外，这次分享的相关文章也已经在Game AI Pro发布了：</font><br>
<font color="#696969"><br>
</font><br>
<font color="#696969">http://www.gameaipro.com/GameAIProOnlineEdition2021/GameAIProOnlineEdition2021_Chapter12_Squad_Coordination_in_Days_Gone.pdf</font><br>
<font color="#696969"><br>
</font><br>
<strong><font color="#696969">以下是这个演讲的详细内容。</font></strong><br>
<font color="#696969"><br>
</font><br>
<font color="#696969">（注：非精译，所有内容均为个人理解和再阐释）</font><br>
<br>
<strong><font color="#de5650">小队AI设计意图</font></strong><br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">1.塑造一个更可信的世界</font></strong><br>
<br>
Days Gone中有各种各样的人类势力和丧尸（Freakers）。<br>
<br>
在大世界中人类势力和丧尸、玩家，以及人类之间会对抗并发生战斗。<br>
<br>
为了让发生在这个世界中的斗争更可信，需要设计能反映人类成员间合作战斗的小队AI。<br>
<br>
<div align="center">
<img aid="1029920" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111827lhqd3fffhmyzhmfg.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111827lhqd3fffhmyzhmfg.jpg" width="600" id="aimg_1029920" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111827lhqd3fffhmyzhmfg.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">2.更优雅地提升难度</font></strong><br>
<br>
合作无间的AI更难被击败。<br>
<br>
单纯提升AI的攻击伤害和命中率过于粗暴了。<br>
<br>
<strong><font color="#de5650">设计目标简单拆解</font></strong><br>
<br>
设计合作AI是困难的，设计在大世界中的合作AI更难。Days Gone最终拿出的是一套相对简洁的设计，解决以下问题：<br>
<br>
小队的目标/行为<br>
<br>
小队成员的角色和角色分配方式<br>
<br>
小队成员的站位<br>
<br>
战斗相关的时机把握<br>
<br>
<div align="center">
<img aid="1029921" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111828l8i5eqemneju68ux.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111828l8i5eqemneju68ux.jpg" width="600" id="aimg_1029921" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111828l8i5eqemneju68ux.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">核心概念</font></strong><br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">0.敌我分布</font></strong><br>
<br>
在Days Gone中，两个不同势力的人类小队，各成员在战斗中不是呈现敌我混杂犬牙交错的形态，而是泾渭分明各站一边。这样的设计是小队AI工作的前提。<br>
<br>
这样做的原因是要提高战场的可读性。Days Gone是一个掩体射击战斗游戏，敌我双方的交错会使得掩体频繁失效，AI需要不断调整战斗位置，攻击效率会变得极低。如下图所示。<br>
<br>
<div align="center"><font size="2">
<img aid="1029922" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111828m7zd0kqp4xdgzxpd.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111828m7zd0kqp4xdgzxpd.jpg" width="600" id="aimg_1029922" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111828m7zd0kqp4xdgzxpd.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">红蓝双方势力在交错站位对打时难以协调</font></div><br>
另外，这样的分布从外部看，很难搞清楚攻防双方的意图，例如是一边从上往下打还是另一边从左往右打。在两边势力着装差不多的情况下，外部的玩家甚至很难分清谁在打谁。<br>
<br>
<div align="center"><font size="2">
<img aid="1029923" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111829aejtma7q9ebfecz3.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111829aejtma7q9ebfecz3.jpg" width="600" id="aimg_1029923" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111829aejtma7q9ebfecz3.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">各方人类势力着装差不多，一旦打起来，视觉观感上差不多是这样</font></div><br>
因此，在小队之间战斗的时候，首先需要把战场上对立的双方区隔开来，达到类似如下图的效果。<br>
<br>
<div align="center"><font size="2">
<img aid="1029924" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111829l23zczcg5n5zinht.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111829l23zczcg5n5zinht.jpg" width="600" id="aimg_1029924" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111829l23zczcg5n5zinht.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">这样的分布使得对立的双方更加明确</font></div><br>
<strong><font color="#de5650">1.小队（Squad）</font></strong><br>
<br>
人类AI以小队的形式组织起来。小队有以下的特征：<br>
<br>
<strong>每个AI必有所属小队</strong><br>
<br>
所有AI都是通过小队来协调战斗的，因此每个AI都需要有所属小队。当AI生成的时候，就会自动为他创建小队（因此1人小队也是成立的）。<br>
<br>
<div align="center">
<img aid="1029925" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111829k4dfrdrotvotrz44.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111829k4dfrdrotvotrz44.jpg" width="600" id="aimg_1029925" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111829k4dfrdrotvotrz44.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>小队会自动合并</strong><br>
<br>
1人小队显然无法配合，因此Days Gone设计了小队自动合并机制。当两个小队靠的足够近的时候，将它们自动合并成一个小队。<br>
<br>
<div align="center"><font size="2">
<img aid="1029926" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111829p0c4bubn0dtzumr9.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111829p0c4bubn0dtzumr9.jpg" width="600" id="aimg_1029926" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111829p0c4bubn0dtzumr9.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">距离较远的时候是两个小队</font></div><br>
<div align="center"><font size="2">
<img aid="1029927" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111829bmfaos0iao1c1cie.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111829bmfaos0iao1c1cie.jpg" width="600" id="aimg_1029927" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111829bmfaos0iao1c1cie.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">由于中间两队成员靠近到了阈值距离，他们所属小队合并了</font></div><br>
因此，当AI出生的时候，由于其周围有同伙AI，就自动合并小队了，小队成员协作也就成为了可能。<br>
<br>
<strong>小队会自动拆分</strong><br>
<br>
相当于上一条的逆规则，距离远到一定程度的成员将被重新拆分组成新的小队。<br>
<br>
<div align="center">
<img aid="1029928" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111830lewwwwnwsjnowxzs.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111830lewwwwnwsjnowxzs.jpg" width="600" id="aimg_1029928" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111830lewwwwnwsjnowxzs.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">2.AI层级</font></strong><br>
<br>
Days Gone中小队是由独立的AI实体控制的，这个小队控制AI主要的作用是选择行为（Behavior）以及为小队个体AI分配角色（Role）。<br>
<br>
<div align="center">
<img aid="1029929" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111830t0bmiuxsvoo7i06o.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111830t0bmiuxsvoo7i06o.jpg" width="600" id="aimg_1029929" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111830t0bmiuxsvoo7i06o.jpg" referrerpolicy="no-referrer">
</div><br>
个体AI的行为总的来说分为三个层级：高优先级行为、角色行为、低优先级行为。当一个AI被小队分配了某个角色的时候，就会开始执行角色行为。这些角色包括类似冲锋、侧翼包抄、火力掩护、投弹手等类型。角色行为之间也是存在预设好的优先级的。因此整个个体AI就会按照预设好的行为优先级行动。<br>
<br>
Days Gone倾向于严格限制角色行为的边界，即当个体AI获得某个角色的时候，只会做与角色相符的行为。而一些通用的行为则全部放在角色外去处理。<br>
<br>
<div align="center"><font size="2">
<img aid="1029930" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111830vafdfssrrjn7frsb.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111830vafdfssrrjn7frsb.jpg" width="600" id="aimg_1029930" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111830vafdfssrrjn7frsb.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">角色和行为模式严格绑定</font></div><br>
举例说明个体AI的行为层级：当手榴弹被丢到个体AI身边的时候，个体AI会立刻做一个躲闪行为，这个躲闪行为就是一个高优先级行为，不属于角色本身的。而低优先级行为，则是保底行为，当AI没有任何角色的时候会进行的行为，一般不会跑到。<br>
<br>
【注】关于AI的行为层级，GDC一些分享也提到过，例如全境封锁的AI设计分享，可以在油管找到。这里个人推测小队管理器AI应该是不会管理高优先级行为的，但是会把高优先级行为作为自己分配角色的判断条件。例如躲避手榴弹这个行为应该是不需要经过小队管理器的，但是当一个AI在躲避手榴弹的时候，小队管理器可能就无法给他分配某个角色了。<br>
<br>
<strong><font color="#de5650">3.前线（Frontline）</font></strong><br>
<br>
前线是用来描述一组小队AI和他的敌人之间的位置关系的。<br>
<br>
<div align="center">
<img aid="1029931" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111830q24utininumzmgs6.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111830q24utininumzmgs6.jpg" width="600" id="aimg_1029931" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111830q24utininumzmgs6.jpg" referrerpolicy="no-referrer">
</div><br>
前线包含了4个子概念：<br>
<br>
<strong>战斗方向</strong><br>
<br>
选取自己小队的质心（这里简单地用了所有小队成员的平均位置）和敌人小队的质心，从己方到敌方的连线即为战斗方向。<br>
<br>
<div align="center">
<img aid="1029932" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111830af9uwna3anjxoax5.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111830af9uwna3anjxoax5.jpg" width="600" id="aimg_1029932" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111830af9uwna3anjxoax5.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>战场宽度</strong><br>
<br>
选取战场上敌方小队展开的宽度（即小队两个成员之间的最大宽度）作为战场宽度。<br>
<br>
<div align="center">
<img aid="1029933" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111831vpcz940zzfp059qs.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111831vpcz940zzfp059qs.jpg" width="600" id="aimg_1029933" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111831vpcz940zzfp059qs.jpg" referrerpolicy="no-referrer">
</div><br>
但是如果这个宽度小于我方小队所需最小宽度（即每两个成员之间保持最小间距排开），那么就会选取我方小队所需最小宽度作为战场宽度。<br>
<br>
<div align="center">
<img aid="1029934" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111831rmxddys24ysc4mmx.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111831rmxddys24ysc4mmx.jpg" width="600" id="aimg_1029934" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111831rmxddys24ysc4mmx.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>中立区</strong><br>
<br>
中立区是敌我双方任何成员都不能踏足的区域。中立区的形状取决于前线的模式。前线有近距离和远距离两种模式。在近距离模式中，中立区是从地方最接近本方小队的成员算起，一个固定宽度的矩形区域（长边为战场宽度）。<br>
<br>
<div align="center">
<img aid="1029935" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111831i3zf6coqcia3s4qm.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111831i3zf6coqcia3s4qm.jpg" width="600" id="aimg_1029935" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111831i3zf6coqcia3s4qm.jpg" referrerpolicy="no-referrer">
</div><br>
远距离模式下，敌我双方最接近的成员之间的区域皆为中立区，也就是说这个区域是动态变化的。<br>
<br>
<div align="center">
<img aid="1029936" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111832yos10hjaxe9qa961.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111832yos10hjaxe9qa961.jpg" width="600" id="aimg_1029936" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111832yos10hjaxe9qa961.jpg" referrerpolicy="no-referrer">
</div><br>
这个模式被用作实现一些特殊的需求，例如要求一个小队原地防守。如上图所示，由于本方和敌方之间的区域都是中立区，因此无论敌方是推进还是撤退，本方都不会进入中立区，因此表现上就是坚守阵地。<br>
<br>
<strong>敌方控制区</strong><br>
<br>
敌方控制区是包含所有敌人的矩形再向外扩张一个固定宽度的矩形区域。后方额外扩张的区域是小队AI做侧翼包抄（Flanking）行为时会用到的。<br>
<br>
<div align="center">
<img aid="1029937" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111833zxda6xkgiiketx27.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111833zxda6xkgiiketx27.jpg" width="600" id="aimg_1029937" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111833zxda6xkgiiketx27.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">4.AI排布</font></strong><br>
<br>
在排列小队成员的时候，会根据战场宽度和小队成员数量，给小队的每个AI成员划分站位区域。划分采用简单的平均分布法，有几个成员，就给这个区域分成几行，每行占一位。<br>
<br>
<div align="center"><font size="2">
<img aid="1029938" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111833vcavte172cv93tta.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111833vcavte172cv93tta.jpg" width="600" id="aimg_1029938" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111833vcavte172cv93tta.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">划分好站位区之后，处于不合理位置的AI将会移动到合理位置</font></div><br>
这样设置的原因是保证AI合理分散开来，互相之间不会阻挡射击路线（毕竟这是个射击游戏）。另外，由于战斗方向会随时间而改变，因此站位分布也会随着战斗方向改变而改变。<br>
<br>
<div align="center"><font size="2">
<img aid="1029939" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111833o77xurvx19dctvg1.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111833o77xurvx19dctvg1.jpg" width="600" id="aimg_1029939" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111833o77xurvx19dctvg1.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">当战斗方向偏转较大的时候，AI也相应要做出较大位移调整</font></div><br>
<strong><font color="#de5650">5.信心值</font></strong><br>
<br>
信心值用来描述AI个体对己方赢得对决的态度。<br>
<br>
<div align="center">
<img aid="1029940" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111833l0vbu8imqbyipu0j.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111833l0vbu8imqbyipu0j.jpg" width="600" id="aimg_1029940" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111833l0vbu8imqbyipu0j.jpg" referrerpolicy="no-referrer">
</div><br>
个人和小队都有信心值的概念。小队的信心值是所有成员信心值的平均。信心值对决策具有决定性作用。个体AI和群体AI中都有许多行为是通过信心值驱动的。<br>
<br>
<div align="center">
<img aid="1029941" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111834mmwsphf2wlw2gil2.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111834mmwsphf2wlw2gil2.jpg" width="600" id="aimg_1029941" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111834mmwsphf2wlw2gil2.jpg" referrerpolicy="no-referrer">
</div><br>
信心值并不使用具体的数值，而是划分了不同的档位，因为档位的变化较数值更容易被玩家感知到。信心值共划分为5档：<br>
<br>
奋勇<br>
<br>
自信<br>
<br>
中立<br>
<br>
焦虑<br>
<br>
惊惶<br>
<br>
<div align="center"><font size="2">
<img aid="1029942" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111834rribalskafsxkhi3.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111834rribalskafsxkhi3.jpg" width="600" id="aimg_1029942" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111834rribalskafsxkhi3.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">信心值的5个档位</font></div><br>
之前提到小队的信心值是成员信心值的平均，这里涉及到一个类似计算结果取整的问题。Days Gone的做法是向着Neutral这一档的方向进行取整。<br>
<br>
<strong><font color="#de5650">6.信心值的计算</font></strong><br>
<br>
信心值的计算比较复杂，是通过计算双方的实力值并进行对比之后得出来的。<br>
<br>
【注】这一部分个人的理解不是很透彻，可能会存在对演讲的误解，酌情观看。<br>
<br>
<div align="center">
<img aid="1029943" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111834uwwrsowofo5ow01w.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111834uwwrsowofo5ow01w.jpg" width="600" id="aimg_1029943" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111834uwwrsowofo5ow01w.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>计算范围</strong><br>
<br>
首先要明确的是，这里计算的是个体AI的信心值，但是个体AI需要权衡战场上敌我双方的实力，因此，个体AI会统计战场上己方小队、己方友好单位所有人的实力值的总和，以及自己感知到的所有敌方单位的实力值的总和，将两者对比，用以计算自己的信心值。这个计算方法的核心是我（己方）怎么看你（敌方），因此双方对对方实力的认知就能够作为重要的指标。<br>
<br>
<strong>实力值</strong><br>
<br>
每方实力值都是个体实力值的加总，但是这个实力值正如上面提到的，是取决于一方怎么认识另一方的。<br>
<br>
<div align="center"><font size="2">
<img aid="1029944" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111834ys80ff0uxjqqc00w.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111834ys80ff0uxjqqc00w.jpg" width="600" id="aimg_1029944" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111834ys80ff0uxjqqc00w.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">基础实力值矩阵</font></div><br>
当己方计算自己队伍的实力值的时候，取的实力值是自己认为自己的实力，以及自己认为自己友军的实力，将所有己方单位的实力值进行加总。而当己方计算敌方队伍的实力值的时候，也是取自己认为的敌方单位的实力值进行加总。一方认为另一方的实力是多少，可以用上面图的那个矩阵来表示。<strong>注意，这个矩阵的值只是基础值，后面计算还会受系数的影响。</strong><br>
<br>
演讲者举例，例如某些势力看起来很强大，别的势力单位都会觉得比自己强，就是下图这个情况，蓝色和紫色势力的单位都认为绿色势力的单位实力高于自己（分别是自己的1.4倍和1.6倍）。<br>
<br>
<div align="center">
<img aid="1029945" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111834v8ioa4l48yn3avra.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111834v8ioa4l48yn3avra.jpg" width="600" id="aimg_1029945" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111834v8ioa4l48yn3avra.jpg" referrerpolicy="no-referrer">
</div><br>
当然，也有可能有这样的情况，就是双方都认为对方比自己强。<br>
<br>
<div align="center">
<img aid="1029946" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111835jqsjvxqz4wja80et.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111835jqsjvxqz4wja80et.jpg" width="600" id="aimg_1029946" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111835jqsjvxqz4wja80et.jpg" referrerpolicy="no-referrer">
</div><br>
使用己方认为对方实力如何这样的计算方式，带来的好处是可以演变出势力之间的战斗策略。如果双方都认为对方更强，从而己方信心值降低，那么就会造成双方都打得比较保守的僵持局面。<br>
<br>
每个个体AI实力值的基础值由上面的关系矩阵图决定，同时受一些乘数的影响。这些乘数包括：<br>
<br>
<div align="center">
<img aid="1029947" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111835chcmomm8zn7fec4m.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111835chcmomm8zn7fec4m.jpg" width="600" id="aimg_1029947" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111835chcmomm8zn7fec4m.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>武器</strong>：最重要的乘数，取决于携带的武器类型<br>
<br>
<strong>护甲</strong>：是否拥有护甲<br>
<br>
<strong>生命</strong>：这里只有单位是否重伤两种情况，对应两个不同的乘数<br>
<br>
<strong>信心值</strong>：个体的信心值影响个体的实力值，从而累加起来会对小队的实力值产生影响。<br>
<br>
（【注意】这里演讲者提到，如果一个小队的个体AI进入了Panic的状态，那么他的小队应该会很快瓦解，为了强化这个效果，这个单位的实力值将不会加到己方小队，而是加到对方小队，相当于在计算的时候，己方的Panic单位实际上相当于敌方单位。）<br>
<br>
在计算实力值的时候，还会把敌方已死亡单位的实力值加到己方来，这样能够进一步强化己方杀伤敌人带来的优势。<br>
<br>
<div align="center">
<img aid="1029948" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111835sp3sn86183801ty1.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111835sp3sn86183801ty1.jpg" width="600" id="aimg_1029948" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111835sp3sn86183801ty1.jpg" referrerpolicy="no-referrer">
</div><br>
但是这个加成不是永久的，只会持续一段时间并且影响力在这期间递减。<br>
<br>
（【注】以上部分讲的是个体AI如何计算敌我双方的实力值，但是在计算出来之后如何通过双方实力值得出自己的信心值，具体的方式主讲人没有提到，应该是有个梯度阈值对应关系的）<br>
<br>
<strong><font color="#de5650">7.信心值驱动玩家行为</font></strong><br>
<br>
信心值系统在处理不同AI势力之间对抗的时候表现较好，但是在处理AI小队对抗玩家的时候，效果则没有那么理想。因此开发组做了一些设定，通过玩家行为来改变AI信心值，从而反过来影响玩家行为。<br>
<br>
<div align="center">
<img aid="1029949" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111835wgvc14ggdsgslxpz.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111835wgvc14ggdsgslxpz.jpg" width="600" id="aimg_1029949" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111835wgvc14ggdsgslxpz.jpg" referrerpolicy="no-referrer">
</div><br>
玩家的一些消极行为会增加AI的信心值：<br>
<br>
不移动<br>
<br>
躲进掩体<br>
<br>
受击<br>
<br>
<div align="center">
<img aid="1029950" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111835zsg152za5dwkttko.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111835zsg152za5dwkttko.jpg" width="600" id="aimg_1029950" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111835zsg152za5dwkttko.jpg" referrerpolicy="no-referrer">
</div><br>
AI信心值增加会更有侵略性，从而迫使玩家改变消极行为。<br>
<br>
相应地，玩家的积极进攻行为也会降低AI的信心值：<br>
<br>
侧翼包抄/突破掩体<br>
<br>
瞄准AI<br>
<br>
近战攻击<br>
<br>
<div align="center">
<img aid="1029951" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111836adu1u1p6z62obopl.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111836adu1u1p6z62obopl.jpg" width="600" id="aimg_1029951" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111836adu1u1p6z62obopl.jpg" referrerpolicy="no-referrer">
</div><br>
从而使得玩家积极进攻获得奖励。<br>
<br>
<strong><font color="#de5650">小队行为</font></strong><br>
<br>
在讲解了小队的前线和小队信心值的概念之后，主讲人拆解了Days Gone中的小队行为。<br>
<br>
<div align="center">
<img aid="1029952" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111836rsm9p6wh4tt54445.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111836rsm9p6wh4tt54445.jpg" width="600" id="aimg_1029952" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111836rsm9p6wh4tt54445.jpg" referrerpolicy="no-referrer">
</div><br>
在Days Gone中，小队AI会控制小队进行以下几种行为：<br>
<br>
整队<br>
<br>
常规战斗<br>
<br>
撤退<br>
<br>
推进<br>
<br>
<div align="center">
<img aid="1029953" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111836myx2lfrc1q1rm3y7.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111836myx2lfrc1q1rm3y7.jpg" width="600" id="aimg_1029953" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111836myx2lfrc1q1rm3y7.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">1.整队</font></strong><br>
<br>
当小队中至少有一个成员的位置不合适的时候，小队就会进行整队。<br>
<br>
<div align="center">
<img aid="1029954" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111836flykgyh071pz1u7z.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111836flykgyh071pz1u7z.jpg" width="600" id="aimg_1029954" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111836flykgyh071pz1u7z.jpg" referrerpolicy="no-referrer">
</div><br>
这里位置的不合适，可能的情况包含：成员在中立区、成员在敌人控制区、成员超过战场宽度、成员落后离大部队太远等。<br>
<br>
整队的流程，如下图所示：<br>
<br>
<div align="center">
<img aid="1029955" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111837vajfh7vt607j5j9a.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111837vajfh7vt607j5j9a.jpg" width="600" id="aimg_1029955" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111837vajfh7vt607j5j9a.jpg" referrerpolicy="no-referrer">
</div><br>
图中中间两个带有红色视锥的AI是位置正确的AI，其他AI会在整队开始之后朝箭头方向，也就是他们应该出现的位置移动。而对于两个位置正确的AI，他们会有两种情况：保持自己的位置，并且朝敌人攻击，维持住战场；或者当敌人距离自己太近导致自己处于危险境地的时候，会在掩体之间来回切换。<br>
<br>
整队结束之后，所有的AI都会处于合适的位置上。<br>
<br>
<div align="center">
<img aid="1029956" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111837amm0ns0l9lsl9m0l.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111837amm0ns0l9lsl9m0l.jpg" width="600" id="aimg_1029956" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111837amm0ns0l9lsl9m0l.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">2.常规战斗</font></strong><br>
<br>
常规战斗行为只会在小队信心值为中立的时候才会发生。<br>
<br>
<div align="center">
<img aid="1029957" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111837e2b52n9b2wx2lnxo.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111837e2b52n9b2wx2lnxo.jpg" width="600" id="aimg_1029957" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111837e2b52n9b2wx2lnxo.jpg" referrerpolicy="no-referrer">
</div><br>
常规战斗在视觉上能够清晰的呈现，靠的就是上面部分提到的设计：前线保证了争斗方向的可读性，中立区保证了战斗双方能够区隔开来。随着战斗的持续，前线会随着双方位置的变化而改变，从而始终保持比较好的队形。<br>
<br>
<strong><font color="#de5650">3.撤退</font></strong><br>
<br>
当小队信心值低的时候，就会开始撤退（【注】这里分享并没说是否只有到了惊惶的级别才会撤退）。<br>
<br>
<div align="center">
<img aid="1029958" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111837tsfkpf3oo4zrkbk1.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111837tsfkpf3oo4zrkbk1.jpg" width="600" id="aimg_1029958" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111837tsfkpf3oo4zrkbk1.jpg" referrerpolicy="no-referrer">
</div><br>
撤退的方向是前线的反方向。当撤退开始时，系统会先选择一半的成员撤退。选择时优先选择处于掩体中的，然后是距离前线最近的。当这一半成员开始撤退的时候，另一半成员会提供支援火力。每次撤退的成员只会后退一小段距离，随后另一半成员（这时他们处于前线较近位置）开始撤退而之前撤退的提供支援火力。如此往复循环，直到出现以下情况之一小队将停止撤退：<br>
<br>
小队被阻挡<br>
<br>
小队和敌方小队脱离接触（【注】这里没有说明怎么脱离接触，估计是区域or距离脱战）<br>
<br>
小队信心值恢复（【注】这里没有说明怎么恢复信心，估计可能类似玩家把对面人打死不少）<br>
<br>
<strong><font color="#de5650">4.推进</font></strong><br>
<br>
当AI小队信心值高的时候，就会尝试向敌方推进。<br>
<br>
<div align="center">
<img aid="1029959" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111837lunwqe93vc9cbe9q.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111837lunwqe93vc9cbe9q.jpg" width="600" id="aimg_1029959" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111837lunwqe93vc9cbe9q.jpg" referrerpolicy="no-referrer">
</div><br>
推进的第一步是尝试接近敌方，这个过程可以认为是撤退的反向操作，即一半向前推进，另一半提供支援火力，如此往复。直到整个小队靠近敌方到足够近的距离（【注】推测是中立区的设置值）。<br>
<br>
当双方距离足够近的时候，推进的小队会尝试去侧翼包抄。系统会选择处于最左侧或者最右侧的成员去执行包抄的任务。<br>
<br>
<div align="center">
<img aid="1029960" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111838zx74m4hpz43wxhnl.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111838zx74m4hpz43wxhnl.jpg" width="600" id="aimg_1029960" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111838zx74m4hpz43wxhnl.jpg" referrerpolicy="no-referrer">
</div><br>
执行包抄任务的小队成员会选择敌方侧翼区域的一个位置并移动过去。<br>
<br>
<div align="center">
<img aid="1029961" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111838xvgn9is1b787in77.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111838xvgn9is1b787in77.jpg" width="600" id="aimg_1029961" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111838xvgn9is1b787in77.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2">从这个区域的形状可以理解之前为什么敌人控制区在后方还留有额外的距离</font></div><br>
（【注】分享到这里就讲完了侧翼包抄这一趴了，但是更多的细节并没有说明，例如选点方案，选点后执行的行为之类）<br>
<br>
<strong><font color="#de5650">优化说明：如何稳定前线</font></strong><br>
<br>
在分享的下一部分，主讲人介绍了针对前线（Frontline）的一些优化细节。由于前线的方向两个小队质心的连线方向，而小队成员的任何移动都会改变整个小队的质心，因此如果不加处理，小队成员为了保持位置合理，就会处于不断的走位之中而不会攻击。为了解决这个问题，Days Gone中做了以下几个方面的优化。<br>
<br>
<strong><font color="#de5650">1.忽略部分兵种</font></strong><br>
<br>
一些兵种如果加入小队前线的计算表现会很奇怪，因此Days Gone选择忽视这些兵种，在计算前线方向的时候不考虑他们。<br>
<br>
<div align="center">
<img aid="1029962" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111838rwtkrdkrwdewrrh2.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111838rwtkrdkrwdewrrh2.jpg" width="600" id="aimg_1029962" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111838rwtkrdkrwdewrrh2.jpg" referrerpolicy="no-referrer">
</div><br>
首先是狙击手。在Days Gone中，狙击手被设定为在指定好的位置原地不动的兵种，因此和小队的距离可能非常远，如果参与前线计算，那么前线的位置将非常靠后，其他队员几乎无法向前移动，所以不参与前线的计算。<br>
<br>
其次是突击手（Rushers）。突击手是装备霰弹枪近距离作战的兵种，他们会突进到交战中立区甚至敌占区内，因此也不参与前线计算。另外，小队系统也不需要处理突击手突击到距离敌人过近位置的问题，而是通过高优先级行为打断的方式处理。<br>
<br>
<strong><font color="#de5650">2.掩体位置取代单位位置</font></strong><br>
<br>
Days Gone是以掩体战斗为人类AI战斗核心的游戏。人类AI战斗的区域基本都有掩体。<br>
<br>
<div align="center">
<img aid="1029963" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111838ko0bkl65brv5o4ek.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111838ko0bkl65brv5o4ek.jpg" width="600" id="aimg_1029963" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111838ko0bkl65brv5o4ek.jpg" referrerpolicy="no-referrer">
</div><br>
掩体在设置的时候标记了掩体的使用位置，但是AI在使用掩体的时候，并不是一直处在下图圆圈的位置上的。<br>
<br>
<div align="center">
<img aid="1029964" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111838sllifwsocxzxxsyy.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111838sllifwsocxzxxsyy.jpg" width="600" id="aimg_1029964" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111838sllifwsocxzxxsyy.jpg" referrerpolicy="no-referrer">
</div><br>
例如AI在换弹的时候会有个后撤步动作，为了防止抢穿模进掩体。另外如果掩体是高掩体，AI在射击的时候就需要向侧方移动2m左右走出掩体进行射击。<br>
<br>
<div align="center">
<img aid="1029965" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111839kmzj2i7m7ijzb8dx.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111839kmzj2i7m7ijzb8dx.jpg" width="600" id="aimg_1029965" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111839kmzj2i7m7ijzb8dx.jpg" referrerpolicy="no-referrer">
</div><br>
这些微小的移动如果都计入前线的计算就会给前线带来频繁的扰动，因此，只要AI在使用掩体，就用掩体的位置（图中虚线圆圈）而不是AI的位置来计算前线。<br>
<br>
<div align="center">
<img aid="1029966" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111839agepe4ixt2jbit21.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111839agepe4ixt2jbit21.jpg" width="600" id="aimg_1029966" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111839agepe4ixt2jbit21.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">3.取一段时间前线的平均位置</font></strong><br>
<br>
前线的位置并不是时刻更新的，也不是某个时间间隔Tick一次的，而是取一段时间内前线位置的平均值，从而达到平滑的效果。<br>
<br>
<div align="center">
<img aid="1029967" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111839frnrrtncqqprf8bf.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111839frnrrtncqqprf8bf.jpg" width="600" id="aimg_1029967" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111839frnrrtncqqprf8bf.jpg" referrerpolicy="no-referrer">
</div><br>
不过为了避免前线位置变化反应过慢的问题，Days Gone会把前线位置向变化较大的那个方向进行修正，并且当变化足够大的时候，前线将被立刻修正为变化之后的位置。<br>
<br>
<div align="center">
<img aid="1029968" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111839qyjggojnq06khjky.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111839qyjggojnq06khjky.jpg" width="600" id="aimg_1029968" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111839qyjggojnq06khjky.jpg" referrerpolicy="no-referrer">
</div><br>
这种变化很大的情况比如：当两队AI正在战斗，突然一大波其中一方的友军来了，那么就要立刻修正前线的位置了。<br>
<br>
<strong><font color="#de5650">4.特殊处理：包抄者（Flankers）</font></strong><br>
<br>
由于侧翼包抄者需要移动到敌方控制区的侧翼，如果包抄者会影响前线的计算，那么就会给前线带来较大的扰动，并且在前线发生变化之后，包抄者自身也就不再处于适合包抄的位置了。<br>
<br>
<div align="center">
<img aid="1029969" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111840ev7wycuczve7147y.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111840ev7wycuczve7147y.jpg" width="600" id="aimg_1029969" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111840ev7wycuczve7147y.jpg" referrerpolicy="no-referrer">
</div><br>
但是，如果包抄者完全不影响前线计算，那么当AI被指派成为包抄者的时候，剩下的小队成员重新计算的前线位置又和决定包抄者的时候大不相同，这也会导致包抄者失去合理位置。<br>
<br>
<div align="center">
<img aid="1029970" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111840qb89ss8boqi4b8bz.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111840qb89ss8boqi4b8bz.jpg" width="600" id="aimg_1029970" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111840qb89ss8boqi4b8bz.jpg" referrerpolicy="no-referrer">
</div><br>
因此，最终方案是：当AI成为包抄者的时候，会在原地留下一个虚拟的单位（并不存在，只指示其位置）用于代替包抄者参与计算前线。<br>
<br>
<div align="center">
<img aid="1029971" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111840exx16e80e5tusuv1.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111840exx16e80e5tusuv1.jpg" width="600" id="aimg_1029971" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111840exx16e80e5tusuv1.jpg" referrerpolicy="no-referrer">
</div><br>
当前线移动的足够远的时候，虚拟单位将被移除。<br>
<br>
<div align="center">
<img aid="1029972" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111840oaj3ck4mhjjc7qjm.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111840oaj3ck4mhjjc7qjm.jpg" width="600" id="aimg_1029972" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111840oaj3ck4mhjjc7qjm.jpg" referrerpolicy="no-referrer">
</div><br>
当包抄者重新归队时，或者包抄者不再是小队一员时（例如死亡），虚拟单位也会被移除。<br>
<br>
<div align="center">
<img aid="1029973" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111840kz656hpuu90hu6le.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111840kz656hpuu90hu6le.jpg" width="600" id="aimg_1029973" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111840kz656hpuu90hu6le.jpg" referrerpolicy="no-referrer">
</div><br>
而对于敌方的包抄者的处理则要复杂一些。这里需要明确的是，我方的前线和敌方的前线并不一定是同一条线，因为一方可能同时面对多个敌方小队，另外玩家也是一个影响因素。因此，站在我方的角度，要去判断敌方谁是包抄者，就需要首先确定敌方的小队质心，从而获得己方质心和敌方质心的连线，即前线。<br>
<br>
具体的方法是：我方小队系统首先去发现所有敌人，根据距离把他们分成一堆儿一堆儿的。<br>
<br>
<div align="center">
<img aid="1029974" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111841qns3whnns7s00o4x.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111841qns3whnns7s00o4x.jpg" width="600" id="aimg_1029974" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111841qns3whnns7s00o4x.jpg" referrerpolicy="no-referrer">
</div><br>
然后取其中最大的一堆，如下图中四个人的显然是最大的一堆。<br>
<br>
<div align="center">
<img aid="1029975" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111841kfx93qx5q9mxqif5.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111841kfx93qx5q9mxqif5.jpg" width="600" id="aimg_1029975" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111841kfx93qx5q9mxqif5.jpg" referrerpolicy="no-referrer">
</div><br>
之后把一些给定大小范围内的人堆再加进来（例如下图中所有的三人堆），并用这些所有的AI小队去计算一个暂时的前线方向。<br>
<br>
<div align="center">
<img aid="1029976" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111841jga15wxd6zmk16jk.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111841jga15wxd6zmk16jk.jpg" width="600" id="aimg_1029976" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111841jga15wxd6zmk16jk.jpg" referrerpolicy="no-referrer">
</div><br>
之后，将处于这个前线以内的所有之前没被计算进来的AI都加进来，得到最终的敌人群体的质心并计算最终的前线方向。<br>
<br>
<div align="center">
<img aid="1029977" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111841bnlltqk5mq19zqn8.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111841bnlltqk5mq19zqn8.jpg" width="600" id="aimg_1029977" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111841bnlltqk5mq19zqn8.jpg" referrerpolicy="no-referrer">
</div><br>
在如此计算之后，剩下的没有被计入的敌人，就被认为是包抄者。<br>
<br>
<div align="center">
<img aid="1029978" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111842gg38dq8bbcpsdqqa.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111842gg38dq8bbcpsdqqa.jpg" width="600" id="aimg_1029978" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111842gg38dq8bbcpsdqqa.jpg" referrerpolicy="no-referrer">
</div><br>
（【注】上面这部分分享，说明一个小队AI的控制器，是没有一个上一级的总控来告诉其整个战场的全局信息的。小队AI只能通过成员单位AI的感知系统来发现敌人的位置和数量，从而计算前线之类的数据，以及识别敌方的包抄者。但令我不解的是，如果所谓的Flanker是小队AI分配的角色，但是对方的小队AI控制器却并不知道这个信息，那么按照上面分享的做法，会不会出现识别的Flanker和真正的Flanker不一致的情况，为什么不直接把谁是Flanker这个信息同步给对方的小队AI呢？根据这个分享来看，这套小队AI系统是把战场的观赏性作为第一位的，那么个人认为有个桥梁把战场所有单位的位置身份信息都互通一下，双方明牌演对手戏似乎更方便一些。可以互通信息处理一些类似上面前线计算和识别Flanker的问题，但是战斗决策依然符合个体AI的感知系统，不让个体AI开天眼，这样似乎呼会更好？）<br>
<br>
在识别出敌方的包抄者之后，如果己方立刻做出反馈，那么包抄者就会失去包抄位置，从而使得这场演出没那么好看。Days Gone的做法是：给这个包抄者一定的时间，在这个时间之内允许包抄者的包抄行为，而在这个时间之后，将会把包抄者加入敌方前线的计算，从而导致整个战线的移动，包抄者自然就失去了包抄位置。<br>
<br>
<div align="center">
<img aid="1029979" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111842z54ttl5l6l5li5b5.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111842z54ttl5l6l5li5b5.jpg" width="600" id="aimg_1029979" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111842z54ttl5l6l5li5b5.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">5.特殊处理：对抗玩家</font></strong><br>
<br>
玩家的行为是不受小队AI这套演出系统约束的，并且玩家的速度远快于AI。如果小队要跟随玩家的移动频繁改变自己的位置，就无法攻击玩家。因此Days Gone的方案是：识别出玩家在疾跑状态的时候，由于玩家此时几乎无法攻击到AI，因此AI在此期间不会改变自己的位置，只会通过射击迫使玩家进入掩体或者选择近战。在玩家不再疾跑之后，AI才会利用间隙重新调整自己的位置。<br>
<br>
<div align="center">
<img aid="1029980" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111842q5h3xahk8d6x50jz.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111842q5h3xahk8d6x50jz.jpg" width="600" id="aimg_1029980" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111842q5h3xahk8d6x50jz.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">AI与环境：来自关卡设计师的指引</font></strong><br>
<br>
以上部分是关于小队AI独立运作机制的，在分享的最后一部分主讲人介绍了小队AI与大世界环境交互的一些方式。<br>
<br>
<div align="center">
<img aid="1029981" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111842aln4fj6yaa4l1f16.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111842aln4fj6yaa4l1f16.jpg" width="600" id="aimg_1029981" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111842aln4fj6yaa4l1f16.jpg" referrerpolicy="no-referrer">
</div><br>
小队AI与环境（主要指大世界的人文环境，例如据点之类的）的交互需要环境提供相关信息，这部分由关卡设计师辅助完成（【注】其实就是关卡设计师拉框打Tag）。关卡设计师标记了一些功能区域用来让小队AI产生自然的行为。这些区域包括：<br>
<br>
防卫据点（Defend Zones）<br>
<br>
宅基地（Home Area）<br>
<br>
要塞区（Fortification Zones）<br>
<br>
<div align="center">
<img aid="1029982" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111842fptvupt28igfp2uv.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111842fptvupt28igfp2uv.jpg" width="600" id="aimg_1029982" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111842fptvupt28igfp2uv.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">1.防卫据点（Defend Zones）</font></strong><br>
<br>
防卫据点是AI运营管理的一大片区域。每个小队都会绑定一个防卫据点，并且会指定一个约束力值。在属于同一个防卫据点的所有小队中，除了约束力值最大的小队，其他小队都被允许短暂离开防卫据点（例如要去追击），以保证小队的大世界表现更加生动。<br>
<br>
<div align="center">
<img aid="1029983" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111843yjj293d42w2r2q44.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111843yjj293d42w2r2q44.jpg" width="600" id="aimg_1029983" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111843yjj293d42w2r2q44.jpg" referrerpolicy="no-referrer">
</div><br>
为了防止小队AI离开据点就不回来，Days Gone这里再次使用了信心值系统。<br>
<br>
<div align="center">
<img aid="1029984" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111843eq0pk94zr9rx49kt.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111843eq0pk94zr9rx49kt.jpg" width="600" id="aimg_1029984" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111843eq0pk94zr9rx49kt.jpg" referrerpolicy="no-referrer">
</div><br>
信心值系统这里发挥着如下的功能：<br>
<br>
推动攻击：信心值表现为自信的小队是可以追击退出己方防卫据点的敌人的。在追出防卫据点的时候，AI小队会获得信心值增益保证其处于追击状态（【注】推测用Timer或定时Buff之类的实现）。<br>
<br>
适时撤退：当追击距离足够远的时候，AI小队的信心值会开始下降，直到降至中立的级别，AI会停止追击。随着信心值进一步下降，AI会开始朝着防卫据点撤退并最终退回据点。<br>
<br>
防止拉扯：当AI小队回到防卫据点之后，其信心值会缓慢回复，直到回到自信级别。缓慢回复而不是直接重置的原因是，如果直接重置，那么小队会立刻开始追击，从而表现为拉扯，这是设计者不想看到的。<br>
<br>
（【注】这部分提到了约束力值的概念，但并没有讲到被设定了不同约束力值的小队在进攻和撤退上会有什么不同，个人推测可能可以作为一个乘数作用于信心值的下降时间和恢复时间）<br>
<br>
<strong><font color="#de5650">2.宅基地（Home Area）</font></strong><br>
<br>
宅基地是AI锚定的一小片区域，可以和防卫据点搭配使用，也可以独立使用。从表现上看，宅基地可能是AI的基地、营地或者守卫的资源点之类的。<br>
<br>
<div align="center">
<img aid="1029985" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111843wtj399obalhhlj8b.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111843wtj399obalhhlj8b.jpg" width="600" id="aimg_1029985" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111843wtj399obalhhlj8b.jpg" referrerpolicy="no-referrer">
</div><br>
当小队AI和特定的宅基地绑定的时候，意味着以下几件事情：<br>
<br>
退无可退：小队撤退时永远会向着宅基地撤退，并且一旦到达宅基地，将不会进一步撤离<br>
<br>
绝对防卫：当敌人进入小队AI的宅基地时，即使小队AI的信心值处于中立，也会主动推进攻击<br>
<br>
关于小队AI的撤退方向，之前提到过，是交战前线的反方向。如下图：淡蓝色箭头是前线的反方向，下方绿色的范围是宅基地。<br>
<br>
<div align="center">
<img aid="1029986" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111843w8f8dv8guh46gu8u.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111843w8f8dv8guh46gu8u.jpg" width="600" id="aimg_1029986" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111843w8f8dv8guh46gu8u.jpg" referrerpolicy="no-referrer">
</div><br>
为了实现小队朝着宅基地撤退的效果，实际是在撤退时小队计算的队伍质心会有一个朝向宅基地的偏移，并且越接近宅基地，这个偏移量越大，最终宅基地的位置会完全替代小队的质心，从而实现撤退进宅基地的效果。另外，在撤退过程中还需要保证前线的旋转从未超过90度，从而保证表现合理。<br>
<br>
<div align="center">
<img aid="1029987" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111843pjdikhgkrfzukbew.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111843pjdikhgkrfzukbew.jpg" width="600" id="aimg_1029987" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111843pjdikhgkrfzukbew.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">3.要塞区（Fortification）</font></strong><br>
<br>
为了更加智能，AI需要能够在战斗中利用有利地形、扼守咽喉要道。关卡设计师为此设计了要塞区用于标记一些易于防守的位置。<br>
<br>
<div align="center">
<img aid="1029988" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111844lqf6qf7dahuf9dxd.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111844lqf6qf7dahuf9dxd.jpg" width="600" id="aimg_1029988" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111844lqf6qf7dahuf9dxd.jpg" referrerpolicy="no-referrer">
</div><br>
己方要塞区由两部分构成：<br>
<br>
攻击位置：当战斗开始的时候己方AI会占据这里并攻击<br>
<br>
攻击触发区：如果敌方进入此区域，己方AI就会前往攻击位置开始攻击，注意此区域形状为一个圆台（下图标记为俯视图）<br>
<br>
<div align="center">
<img aid="1029989" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111844axu11fx4snt1t4tb.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111844axu11fx4snt1t4tb.jpg" width="600" id="aimg_1029989" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111844axu11fx4snt1t4tb.jpg" referrerpolicy="no-referrer">
</div><br>
需要注意的是，这两块区域只需要有逻辑上的绑定关系，而不需要在空间上紧密连接，这样配置更加灵活，也更适配一些存在高低差的区域，使得战斗更合理。<br>
<br>
当敌方进入要塞的攻击触发区，要塞区就被激活，己方AI就会前往攻击位置进行要塞的防卫。<br>
<br>
<div align="center">
<img aid="1029990" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111844ea1r654h6a277h31.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111844ea1r654h6a277h31.jpg" width="600" id="aimg_1029990" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111844ea1r654h6a277h31.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">4.综合应用</font></strong><br>
<br>
将以上三种区域配置方式综合应用，可以配置出一个合理而有层次的大世界AI大本营据点。<br>
<br>
下图标记了AI吃饭睡觉的营地：<br>
<br>
<div align="center">
<img aid="1029991" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111844t2eufnnoo6bv1njj.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111844t2eufnnoo6bv1njj.jpg" width="600" id="aimg_1029991" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111844t2eufnnoo6bv1njj.jpg" referrerpolicy="no-referrer">
</div><br>
下图标记了大本营周围的环境和内部的掩体（可以看到这个大本营有上下两个入口）：<br>
<br>
<div align="center">
<img aid="1029992" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111845yf1t0zv7tht4hxyb.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111845yf1t0zv7tht4hxyb.jpg" width="600" id="aimg_1029992" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111845yf1t0zv7tht4hxyb.jpg" referrerpolicy="no-referrer">
</div><br>
下图是针对大本营设置的防卫据点和宅基地：<br>
<br>
<div align="center">
<img aid="1029993" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111845rsvsv6vv3z3hf1vz.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111845rsvsv6vv3z3hf1vz.jpg" width="600" id="aimg_1029993" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111845rsvsv6vv3z3hf1vz.jpg" referrerpolicy="no-referrer">
</div><br>
可以看出防卫据点区域划出的形状是外扩且不规则的（【注】推测使用Spline框画），目的是应对角落的敌人，并且让AI能够适当追击出去。而宅基地则正好设置在大本营中心AI的生活区域，表现合理。<br>
<br>
下图是关卡设计师划分的要塞区：<br>
<br>
<div align="center">
<img aid="1029994" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111845rq0xjgx00nttfuzx.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111845rq0xjgx00nttfuzx.jpg" width="600" id="aimg_1029994" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111845rq0xjgx00nttfuzx.jpg" referrerpolicy="no-referrer">
</div>下图模拟了敌人从下方入口进攻的情况：<br>
<br>
<div align="center">
<img aid="1029995" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111845km5fo575z7osoz59.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111845km5fo575z7osoz59.jpg" width="600" id="aimg_1029995" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111845km5fo575z7osoz59.jpg" referrerpolicy="no-referrer">
</div><br>
当敌人进入要塞区的攻击触发区，小队AI会前往攻击位置进行要塞保卫。能够前往攻击位置的AI数量是有限的，这与攻击位置的大小相关。（【注】这里分享提到，要塞区是可以绑定一些AI的，当要塞区被敌人激活的时候，绑定的AI就会前往攻击位置，据此推测要塞有绑定AI和攻击位置最大承载AI数量之类的配置项）<br>
<br>
在利用要塞区进行防守的时候，己方AI依然会遵循之前提到的前线攻击方向等规则进行攻击和掩体移动。<br>
<br>
下图显示了敌方突破要塞区的情况（【注】分享这里并没提到什么指标算突破要塞）：<br>
<br>
<div align="center">
<img aid="1029996" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111846uptc9aa9cg4zu1cz.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111846uptc9aa9cg4zu1cz.jpg" width="600" id="aimg_1029996" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111846uptc9aa9cg4zu1cz.jpg" referrerpolicy="no-referrer">
</div><br>
当敌方突破要塞区的时候，要塞区的AI将会退出要塞，并和其他AI合并成一个小队，并进行常规战斗。而当小队AI撤退到宅基地的时候，将退无可退，并在那里进行最后的负隅顽抗。<br>
<br>
<div align="center">
<img aid="1029997" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111846okwfq1yqhi1y090r.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111846okwfq1yqhi1y090r.jpg" width="600" id="aimg_1029997" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111846okwfq1yqhi1y090r.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">总结：系统的优缺点</font></strong><br>
<br>
最后一部分分享总结了小队AI系统的优缺点：<br>
<br>
<div align="center">
<img aid="1029998" zoomfile="https://di.gameres.com/attachment/forum/202202/07/111846biur2uppqkmbxqxx.jpg" data-original="https://di.gameres.com/attachment/forum/202202/07/111846biur2uppqkmbxqxx.jpg" width="600" id="aimg_1029998" inpost="1" src="https://di.gameres.com/attachment/forum/202202/07/111846biur2uppqkmbxqxx.jpg" referrerpolicy="no-referrer">
</div><br>
大部分情况下表现良好：但也有例外，由于“前线”是个二维向量，因此这个系统无法适用于类似螺旋楼梯这样的场景，不过Days Gone并不太存在这类战斗场景，因此可以忽略。<br>
<br>
不太适应复杂地形阻挡区域：例如在建筑物内外战斗的时候，由于“前线”这一概念无法识别在这类区域中AI应该去哪里比较合理，无法识别房间之间的连通性，因此Days Gone不得不针对建筑物内外战斗做了一些特殊的行为。（【注】未分享怎么实现的）<br>
<br>
不适应与丧尸/动物的对抗：因为这套系统本质是给远程持枪AI相互射击表演设计的，而丧尸和动物全是近战单位，当人类小队AI用这套体系摆好队形之后，其小队行为很快会因为敌人近战攻击而被高优先级行为打断。<br>
<br>
对玩家造成潜移默化的影响：玩家并不知道前线和控制区之类的设定，但是在实际游玩中，玩家会因为小队AI的阵型而本能地尊重“前线”的存在，配合出演，从而达到和AI之间互相对抗差不多的效果。<br>
<br>
<strong><font color="#de5650">个人点评：</font></strong><br>
<br>
适用范围特异化：从这个分享来看，这套小队AI系统是专门针对大世界TPS掩体射击这几个标签设计的，这是这个系统能够顺利运作的前提，对类似近战ARPG之类的游戏，如果想实现群体AI的效果，可能新战神的分享更合适一些。<br>
<br>
<font color="#696969">Evolving Combat in 'God of War' for a New Perspectiv（</font><br>
<font color="#696969"><br>
</font><br>
<font color="#696969">www.youtube.com/watch?v=hE5tWF-Ou2k）</font><br>
<br>
表演性大于实用性：“前线”“信心值”是这个系统的两大核心概念，这俩无不是为表演服务的，分享者也多次强调战斗要从外部看来足够有章法足够好看，因此这套系统有可能在实际实现中为了好看而做了额外工作，具体需不需要参考就要看项目自身了。<br>
<br>
底层信息尚不透明：看完分享之后个人依然存有一些疑惑，例如：个体AI的角色有哪些，AI的角色行为和高优先级行为是怎么运作的，这个大世界的不同势力对抗是怎么触发的，这个大世界是怎么加载的……这些内容的实现和小队AI的设计一定是耦合的，缺失这部分信息的话还是无法评估这个系统的泛用性。<br>
<br>
其他：Days Gone这个游戏我玩过几个小时就放弃了，个人对丧尸、机车、求生、据点式大世界这些元素都不感兴趣，这游戏整体素质尚可但并不惊艳，因此我对游戏的深度内容并不够了解，如果以上内容有错误，那就是我胡说的。<br>
<br>
<font size="2"></font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/N5mvprKbjyVPGdJuP_dW_A</font><br>
<br>
<br>
  
</div>
            