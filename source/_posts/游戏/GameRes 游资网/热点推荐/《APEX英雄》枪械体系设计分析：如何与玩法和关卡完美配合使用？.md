
---
title: '《APEX英雄》枪械体系设计分析：如何与玩法和关卡完美配合使用？'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202110/15/093835xggkkp23cdgkde2p.jpg'
author: GameRes 游资网
comments: false
date: Fri, 15 Oct 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202110/15/093835xggkkp23cdgkde2p.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2516704">
<div align="center">
<img id="aimg_1014778" aid="1014778" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093835xggkkp23cdgkde2p.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093835xggkkp23cdgkde2p.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093835xggkkp23cdgkde2p.jpg" referrerpolicy="no-referrer">
</div>
<br><font color="#808080">本文首发知乎：</font><br><font color="#808080">https://zhuanlan.zhihu.com/p/419270915</font><br><br>
更多阅读内容：<a href="https://www.gameres.com/890205.html" target="_blank">APEX关卡设计分析，它是如何做到横空出世依旧保持热度至今？</a><br><br><strong><font color="#de5650">一、前言</font></strong><br><br>
在网上搜索《APEX英雄》的枪械系统设计时，发现鲜有从设计师角度出发的文章。<br><br>
笔者作为一名关卡设计师，在经历了数百小时的游戏体验后，想要尝试尽量从游戏设计师的角度分析一下《APEX英雄》的枪械体系设计，从感性认识发展到理性认识。<br><br>
由于笔者并不是专业的枪械设计师，分析的有错误或者分析的不够深刻的地方，还望大家能多多指出我的错误，一起学习成长~<br><br>
如果看完觉得有收获的话，别忘点个赞哦~，你们的赞赏是我分享的最大动力。<br><br><strong><font color="#de5650">二、什么是枪械体系</font></strong><br><br>
枪械体系其实就是所有枪械中分为几个类型？每种类型的特点是什么？同种类型的枪械之间如何拉开差异？<br><br>
如上三个问题的答案汇总起来，就是枪械体系。<br><br>
举个栗子，《APEX英雄》中有霰弹枪、狙击枪。霰弹枪的主要特点是适合近距离爆发极高，适合打贴身战斗，距离远了以霰弹枪的扩散，远距离无法造成什么伤害。而狙击枪的主要特点是射程远，单发伤害高，适合攻击远距离目标，但是在贴身战斗中，由于狙击枪的射速慢且机动性差，所以不适合贴身战斗，这是枪械类型分类与每种类型枪械的特点。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014779" aid="1014779" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093835apdxxcfxy9qixqp2.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093835apdxxcfxy9qixqp2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093835apdxxcfxy9qixqp2.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">霰弹枪“和平捍卫者”和狙击枪“哨兵”</font></font></div>
<br>
在狙击枪类型中，比较哨兵与长弓的特点，哨兵单发伤害高但射速慢，适合爆头秒杀敌人。而长弓的单发伤害低于哨兵，但射速更快，持续输出能力更强，这就是同种枪械类型中不同武器的差异化。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014780" aid="1014780" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093836caw55ojogqqnagaj.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093836caw55ojogqqnagaj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093836caw55ojogqqnagaj.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">狙击枪“长弓”</font></font></div>
<br><strong><font color="#de5650">三、建立枪械体系的目的</font></strong><br><br><strong>从玩家角度来看：</strong><br><br><ul><li>完善的枪械体系可以让玩家在根据自己的使用目的来选取枪械时更加明确<br>
</li></ul>
<br>
比如我这局想采用远程劝架的方式来进行战斗，那么我就一定会带一把神射手或狙击枪。<br><br><strong>从设计师角度来看：</strong><br><br><ul><li>在设计新枪时有枪械体系作为框架，除非要制作一把全新类型的武器，否则新枪是无法脱离现有的枪械体系的，设计师可以更方便的对枪械做定位。<br>
</li></ul>
<br>
比如我想设计一把适合中远距离交战的武器，那么这把武器定位基本上就是神射手武器。神射手武器中已经有G7、30-30、三重击、波塞克弓了，新的神射手武器就需要和这些武器拉开差距。<br><br><ul><li>当体系中有枪械超模或者过于下水道时，完善的枪械体系可以让设计师方便的定位问题的根源所在，以便优化枪械。<br>
</li></ul>
<br>
比如第八赛季中的敖犬因其过高的近距离爆发而超模。于是玩家纷纷调侃说，在这个游戏里，你不拿敖犬，你就会被拿敖犬的敌人给杀死。后面制作组大砍了一刀敖犬的爆发伤害，才大幅改善了这一情况。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014781" aid="1014781" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093837gl6q366u6al6qxon.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093837gl6q366u6al6qxon.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093837gl6q366u6al6qxon.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">霰弹枪“敖犬”</font></font></div>
<br><strong><font color="#de5650">四、 建立枪械分类的思路分析</font></strong><br><br>
《APEX英雄》枪械体系分为几种枪械？每种枪械的特点是什么？怎么样突出每种枪械类型的特点？这些问题的答案将在本节为您解答。<br><br>
首先枪械一定是在关卡内使用的，所以枪械分类的建立一定离不开《APEX英雄》的关卡特点。<br><br>
《APEX英雄》中地图的尺寸是2km*2km，这就意味着游戏的交战距离范围至少是0m-数百米。而枪械种类之间最主要的区别就是适用距离的区别，这一点是显而易见的，于是《APEX英雄》中的枪械体系以距离划分的枪械类型如下。<br><br><strong>4.1 枪械类型强度得分表（以交战距离区间划分）：</strong><br><br><div align="center">
<img id="aimg_1014782" aid="1014782" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093837id6lczk2ph28k3zh.png" data-original="https://di.gameres.com/attachment/forum/202110/15/093837id6lczk2ph28k3zh.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093837id6lczk2ph28k3zh.png" referrerpolicy="no-referrer">
</div>
<br><strong>说明：</strong><br><br><ul>
<li>这里的距离和强度得分仅为我个人感受</li>
<li>由于拿不到《APEX英雄》官方的交战距离的后台统计数据，所以我对这些距离的得分并没有做根据每个区间的交战占比（0-10m的交战和80m以上的交战占比肯定是不一样的）做加权处理</li>
<li>总分高不代表武器类型就强，只代表武器的泛用性。霰弹枪虽然得分低，但是由于《APEX英雄》的近距离交战占比非常高，所以霰弹枪也是非常重要的一类武器类型<br>
</li>
</ul>
<br><strong>4.2 枪械类型适用距离的影响因素</strong><br><br><font color="#de5650">1）可用倍镜</font><br><br>
枪械的可用倍镜是影响枪械适用距离最大的因素，因为如果你看都看不见，就别提打他了（笑<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014783" aid="1014783" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093837ww5caclfptu5aa4a.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093837ww5caclfptu5aa4a.jpg" width="294" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093837ww5caclfptu5aa4a.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">各种枪械可用的倍镜表</font></font></div>
<br><strong>还有一些特殊倍镜：</strong><br><br><ul>
<li>金色单倍镜适用于霰弹枪、手枪、冲锋枪，目的之一是为了进一步加强这三种近战枪械的近战能力</li>
<li>同理金色4-10倍镜仅适用于狙击枪，目的之一也是为了进一步加强狙击枪的远程能力<br>
</li>
</ul>
<br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014784" aid="1014784" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093837scptozo0cga0o08g.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093837scptozo0cga0o08g.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093837scptozo0cga0o08g.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">金色单倍镜和金色4-10倍镜子</font></font></div>
<br><font color="#de5650">2）开镜移动惩罚</font><br><br>
在《APEX英雄》中，玩家使用不同类型的枪械开镜移动时，会有不同的移速惩罚。<br><br>
在近距离交战中，开镜移速是非常重要的属性，开镜移速慢的枪在对战开镜移速快的枪时，会被当靶子打，敌人在你面前快速移动，而你在敌人的视角里却移动的非常慢。<br><br>
游戏的启动项输入“+cl_showpos 1”即可在左上角开启角色移速显示。<br><br>
枪械开镜移速惩罚表如下（持枪腰射状态下所有的武器都是173.5的速度）：<br><br><div align="center">
<img id="aimg_1014785" aid="1014785" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093838ikevuxspk9xu99xt.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093838ikevuxspk9xu99xt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093838ikevuxspk9xu99xt.jpg" referrerpolicy="no-referrer">
</div>
<br>
从表中的数据可以看出，强调近距离作战的手枪、霰弹枪、冲锋枪的开镜移速惩罚远小于其他类型的枪械，而强调远距离作战的狙击枪，开镜惩罚是最大的。<br><br><font color="#de5650">3）腰射扩散与腰射准度</font><br><br>
在10m以内的贴身战中，一般都会用腰射进行对战，因为开镜会降低移速。在这个距离内，腰射的准度就很大程度决定了这种类型的武器近战强不强。<br><br>
下面的图片是我在靶场中静止不动只射击不控枪得到的各类型枪械的扩散图，霰弹枪比较特殊，放到后面说。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014786" aid="1014786" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093838cmix24xvuf7rv2mx.png" data-original="https://di.gameres.com/attachment/forum/202110/15/093838cmix24xvuf7rv2mx.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093838cmix24xvuf7rv2mx.png" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">手枪的扩散，图中为小帮手</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014787" aid="1014787" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093838hndud6q7522u7b22.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093838hndud6q7522u7b22.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093838hndud6q7522u7b22.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">冲锋枪的扩散，图中为R99</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014788" aid="1014788" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093838yotuoot1z23h3i96.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093838yotuoot1z23h3i96.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093838yotuoot1z23h3i96.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">突击步枪的扩散，图中为平行步枪</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014789" aid="1014789" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093839izr212kdlvd1v2jv.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093839izr212kdlvd1v2jv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093839izr212kdlvd1v2jv.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">神射手武器的扩散，图中为G7侦察枪</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1014790" aid="1014790" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093840hqmbzuvg9prj968y.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093840hqmbzuvg9prj968y.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093840hqmbzuvg9prj968y.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">狙击枪的扩散，图中为长弓</font></font></div>
<br>
由于大图非常占篇幅，所以我就每种武器放一张图啦，大家感兴趣可以自己去靶场测试。<br><br>
由上面的图片可以看出，手枪、冲锋枪的扩散是远小于其他类型的武器的（霰弹枪除外）。<br><br>
而霰弹枪在10m内腰射就是指哪打哪，所以腰射扩散和腰射准度是枪械近距离强弱的关键影响因素之一。<br><br><font color="#de5650">4）子弹飞行速度</font><br><br>
子弹飞行速度在远距离交战中十分重要，子弹飞行速度越快，需要的预瞄距离也就越近，预瞄的难度就越低，且子弹飞行速度快的枪就算双方同时开枪也可以先命中对方。<br><br>
枪械的子弹飞行速度表如下图所示：<br><br><div align="center">
<img id="aimg_1014791" aid="1014791" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093840laasa0asp8dj6kex.png" data-original="https://di.gameres.com/attachment/forum/202110/15/093840laasa0asp8dj6kex.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093840laasa0asp8dj6kex.png" referrerpolicy="no-referrer">
</div>
<br>
看表中的数据可以发现，越是适用交战距离越远的枪械，子弹飞行速度就越快。可以得出的结论是，子弹飞行速度也是枪械分类的重要影响因素。<br><br><font color="#de5650">5）子弹下坠</font><br><br>
子弹下坠的大小会决定远距离射击时需要抬枪的幅度，子弹下坠的越小，需要的抬枪幅度就越小，就越容易操控。<br><br>
子弹下坠的大小比较难量化，在此只列出我的测试结果，感兴趣的同学可以自己测试。<br><br><strong>测试结果：</strong><br><br>
霰弹枪≈冲锋枪≈手枪>突击步枪≈机枪≈神射手武器>狙击枪<br><br>
由测试结果来看，下坠幅度分为三个档次，最大的是强调近战的武器，中间的是强调中距离作战的武器，下坠最小的是强调远距离的狙击枪。<br><br><font color="#de5650">6）DPS</font><br><br>
近距离交战比较看DPS，因为近距离的子弹的命中率更高。<br><br>
远距离对枪比较看单发伤害，因为远距离子弹的命中率更低，单发高伤害的枪命中时的收益更大。<br><br><strong>以下是各枪械类型：</strong><br><br><div align="center">
<img id="aimg_1014792" aid="1014792" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093840bban2cub2bddbu80.png" data-original="https://di.gameres.com/attachment/forum/202110/15/093840bban2cub2bddbu80.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093840bban2cub2bddbu80.png" referrerpolicy="no-referrer">
</div>
<br>
从表中数据可以看出：<br><br><ul><li>中近距离枪械的DPS大于远距离枪械的DPS<br>
</li></ul>
<br>
从表中数据也可发现几个奇怪的数据：<br><br><strong>i）为什么手枪是强调近距离交战的，为什么DPS这么低？</strong><br><br>
因为《APEX英雄》作为战术竞技射击游戏，枪械是有发育过程的，而手枪一般是定位为前期落地武器（小帮手大佬除外）<br><br><strong>ii）为什么霰弹枪近战那么强，DPS数据上却不高？</strong><br><br>
因为霰弹枪的强势之处在于单发高伤害带来的高斩杀能力以及在掩体后的小身位peek能力<br><br><font color="#de5650">7）单发伤害</font><br><br>
单发伤害的作用已经在第五点中说明了，在此只列数据：<br><br><div align="center">
<img id="aimg_1014793" aid="1014793" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093840j8447rz9j01d2d27.png" data-original="https://di.gameres.com/attachment/forum/202110/15/093840j8447rz9j01d2d27.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093840j8447rz9j01d2d27.png" referrerpolicy="no-referrer">
</div>
<br><font color="#de5650">8）爆头倍率</font><br><br>
爆头倍率跟单发伤害是直接挂钩的，爆头倍率这一影响因素可以视为单发伤害的延伸。<br><br>
以下是爆头倍率数据：<br><br><div align="center">
<img id="aimg_1014794" aid="1014794" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093841eg79nnsw62579e0m.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093841eg79nnsw62579e0m.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093841eg79nnsw62579e0m.jpg" referrerpolicy="no-referrer">
</div>
<br>
从以下的数据很容易得出结论，越是适用于远距离的枪，爆头倍率越高，因为远距离武器就是要的单发高伤害。最强的远程武器是克莱伯，一枪头可以带走满血红甲敌人。<br><br>
冲锋枪还有一个隐藏的属性，就是36m之外是无法进行爆头的，这也是拉开冲锋枪与更远程的武器类型差距的一个设定吧。<br><br><strong><font color="#de5650">五、同种枪械类型中的细分思路分析</font></strong><br><br>
同种枪械类型的武器，需要突出每把武器的特点，以避免两把武器出现定位几乎重叠的情况，以尽量让每把武器都有其最适合的使用环境，这样才能尽可能的避免一招鲜吃遍天的情况，以丰富玩家的选择。<br><br><strong>5.1 可操控性</strong><br><br>
可操控性主要受后坐力影响，这一属性主要是为了满足不同熟练度玩家而划分的。<br><br>
新手需要可操控性好的武器以方便上手熟悉游戏，但可操控性好的武器一般收益比较低，高手则需要更难操控的武器以体现其技术，并且增加其收益。<br><br>
例如进空投前转换者冲锋枪和R99相比，转换者冲锋枪DPS低但好操控，适合新手，而R99后坐力大但DPS高，适合高手。<br><br><strong>5.2 容错率</strong><br><br>
容错率跟可操控性异曲同工，风险和收益永远都是成正比的。<br><br>
R99只要一开始定位没定准，因为射速快，一梭子马上就打完了，基本上全马<br><br>
而电能冲锋枪因为射速相对更慢，一开始定位没定准还能拉回来。<br><br><strong>5.3 特殊配件</strong><br><br>
丰富的特殊配件是一个非常有意思的设计点，这也是《APEX英雄》的科幻世界观带来的好处，为一把武器增加一个特殊配件槽，很容易就和其他武器的定位拉开了差距<br><br><strong>配件的分类</strong><br><br><font color="#de5650">1）用于提高武器上限</font><br><br>
涡轮增压器是其中的典型，涡轮增压器能哈沃克的前摇变短，让专注轻机枪达到最高射速的时间变短，以增加其威力<br><br>
类似的配件还有穿颅器，神射手节拍等<br><br><font color="#de5650">2）用于增加武器适用环境</font><br><br><ul>
<li>粉碎帽加强了30-30、波塞克弓的近战能力，以填补其中远距离的弱势表现</li>
<li>铁砧接收器让R301、平行步枪的中远程对枪能力更强</li>
<li>束流器让三重击变成三重喷，和平捍卫者变成和平狙，非常的有趣（笑<br>
</li>
</ul>
<br>
类似的还有锤击点、扼流器、快速拔枪等等<br><br>
其实有些配件也是加的比较无奈，30-30出场就成了一把下水道武器，重生组又不想单纯的调高伤害数值，所以为弥补它弱势的远程能力，而加强了其近战能力<br><br><strong>5.4 子弹体系</strong><br><br>
《APEX英雄》的子弹类型分为霰弹枪弹药、轻型弹药、重型弹药、能量弹药、弓箭、狙击枪弹药<br><br><div align="center">
<img id="aimg_1014795" aid="1014795" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093841z1w97791sycrdz5r.png" data-original="https://di.gameres.com/attachment/forum/202110/15/093841z1w97791sycrdz5r.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093841z1w97791sycrdz5r.png" referrerpolicy="no-referrer">
</div>
<br>
在同一种枪械类型中将枪械定位时，需要考虑各种子弹的特点，来决定使用什么弹药。<br><br>
霰弹枪子弹和狙击枪子弹可以不用管，因为霰弹枪和狙击枪一定会使用霰弹枪子弹和狙击枪子弹。<br><br>
弓箭比较特殊，也可以先不管。<br><br><ul type="1" class="litype_1">
<li>以单发伤害从小到大排序：轻型<重型≈能量</li>
<li>以子弹射速从慢到快排序：重型≈能量<轻型</li>
<li>以子弹飞行速度从慢到快：重型<轻型<能量</li>
<li>以子弹下坠从大到小来排序：重型<轻型<能量<br>
</li>
</ul>
<br><ul>
<li>比如在设计一把新的突击步枪时</li>
<li>如果想设计一把单发伤害高，子弹飞行速度快的武器，那就用能量弹药</li>
<li>如果想设计一把单发伤害低的武器，射速快的武器，那就用轻型弹药</li>
<li>如果想设计一把子弹飞行速度快的武器，下坠小的武器，那就用能量弹药<br>
</li>
</ul>
<br><strong>5.5 将第4节的部分参数进一步细化</strong><br><br>
将第4节的部分参数进一步细化并与第5节的前4点内容结合，来定位同类型的不同枪械。<br><br>
接下来我将举两个栗子说明来说明这一点。<br><br><strong>5.6 以冲锋枪类型为例</strong><br><br>
以冲锋枪类型的细分为例，来剖析重生组给枪械定位的思路<br><br>
冲锋枪共有4把，转换者冲锋枪（进空投前）、猎兽冲锋枪、电能冲锋枪、R99冲锋枪<br><br><div align="center">
<img id="aimg_1014796" aid="1014796" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093841n2omoqma1675x76m.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093841n2omoqma1675x76m.jpg" width="517" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093841n2omoqma1675x76m.jpg" referrerpolicy="no-referrer">
</div>
<br><strong>转换者冲锋枪的特点：</strong><br><br>
因为射速慢，而且后坐力不大，为转换者带来了最低的操控难度，但是同时DPS（160）也较低，主要是给新手或者是发育的前期使用<br><br><strong>猎兽冲锋枪：</strong><br><br>
五连发的射击模式，超高的腰射精准度，为猎兽带来了冲锋枪中最强的近战爆发能力，甚至可以不输喷子，五连发的射击手感也与其余三把全自动武器有很大差距<br><br><strong>电能冲锋枪：</strong><br><br>
全自动冲锋枪中排名第二的射速，射速不快，DPS（180）也不错，并且后坐力较小，所以使其可操控性好，容错率高。并且电能系武器的特点是子弹飞行速度快，使得电能冲锋枪是冲锋枪中适用距离最远的枪，奥林匹斯就很适合用电能而不适合用R99，因为奥林匹斯比较空旷，交战距离比较远。<br><br><strong>R99：</strong><br><br>
射速最快，后坐力最大，DPS（198）最高，高风险高收益，是一把给高手准备的枪。<br><br><strong>5.7 以狙击枪类型为例</strong><br><br>
狙击枪共有四把，分别是哨兵、长弓、充能步枪、克莱伯<br><br><div align="center">
<img id="aimg_1014797" aid="1014797" zoomfile="https://di.gameres.com/attachment/forum/202110/15/093842cuu85ud9c8icn98c.jpg" data-original="https://di.gameres.com/attachment/forum/202110/15/093842cuu85ud9c8icn98c.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/15/093842cuu85ud9c8icn98c.jpg" referrerpolicy="no-referrer">
</div>
<br><strong>哨兵：</strong>瞬间伤害超高（88），充能后爆头能一枪秒杀满血的白头白甲敌人，不过由于是拉栓狙，持续输出能力不如长弓<br><br><strong>长弓：</strong>除空投狙外瞬间伤害第二高的武器（60），由于是连狙，长弓的持续输出能力强于哨兵<br><br><strong>充能步枪：</strong>即时命中的激光伤害让其成为打的最远的狙击枪，不过即使命中的代价就是持续输出能力不如长弓，且子弹消耗奇快。<br><br><strong>克莱伯：</strong>最强狙击枪，永远不可能出空投的武器，具有全游戏唯一的爆头TTK为0的武器，这把狙的特点就不用我多说了吧。就是子弹有点少，不过这也是为了让空投武器不过于OP的限制咯<br><br><strong><font color="#de5650">结语</font></strong><br><br>
至此笔者对于《APEX英雄》的枪械体系分析就暂时告一段落啦，之后笔者会继续实践学习，完善这篇文章，诸君共勉！<br><br><font color="#808080">参考资料</font><br><br>
数据来源：https://apexlegends.fandom.com/wiki/Weapon#Other_weapons<br><br><font size="2"><font color="#808080"></font></font><br><font size="2"><font color="#808080">原文：https://zhuanlan.zhihu.com/p/419270915</font></font><br>
</td></tr></tbody></table>


  
</div>
            