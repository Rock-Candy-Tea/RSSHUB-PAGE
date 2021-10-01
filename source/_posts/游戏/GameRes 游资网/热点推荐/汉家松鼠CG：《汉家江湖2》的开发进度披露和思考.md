
---
title: '汉家松鼠CG：《汉家江湖2》的开发进度披露和思考'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202109/22/094048xz77a0t8dtotaqy7.jpg'
author: GameRes 游资网
comments: false
date: Wed, 22 Sep 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202109/22/094048xz77a0t8dtotaqy7.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2515144">
<div align="center">
<img id="aimg_1009970" aid="1009970" zoomfile="https://di.gameres.com/attachment/forum/202109/22/094048xz77a0t8dtotaqy7.jpg" data-original="https://di.gameres.com/attachment/forum/202109/22/094048xz77a0t8dtotaqy7.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/094048xz77a0t8dtotaqy7.jpg" referrerpolicy="no-referrer">
</div>
<br>
大家好，我是汉家松鼠工作室的CG，这是一篇游戏开发进度披露。<br><br>
“汉家江湖”是一款我们工作室在2017年发布的武侠手机游戏，承蒙玩家老爷们的抬爱，目前还在运营中。在2019年，我们内部立项了“汉家江湖2”这个项目，但时至今日，除了最早的几个图片和视频，我们没有跟玩家沟通过更多项目的进展，今天想和大家来聊一聊项目的情况以及我们的思考。<br><br><strong><font color="#de5650">最初的想法</font></strong><br><br>
汉家江湖是一款2D游戏，在制作武侠动作、光影特效，以及拓展各种玩法展现来看，我们在运营中遇到了不少问题。主要是制作新的场景代价大、角色换装/动作等难以复用导致资源开销较大等等，这让我们萌生了使用3D来制作的想法。<br><br>
汉家江湖的侠客制作流程本来采用的是“3渲2”，也就是先制作3D模型，然后渲染成2D序列帧，最后压制成图集并入到游戏内资源。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1009971" aid="1009971" zoomfile="https://di.gameres.com/attachment/forum/202109/22/094048asrf2nr297s2r78w.jpg" data-original="https://di.gameres.com/attachment/forum/202109/22/094048asrf2nr297s2r78w.jpg" width="321" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/094048asrf2nr297s2r78w.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">汉家江湖角色2D序列帧示例</font></font></div>
<br>
所以我们本来就制作了一些侠客的3D模型，虽然这些3D模型可能很多时候只是为了渲染出2D效果，所以在制作时并没有把每一个细节3D化完善，甚至有一些细节是先套用动作，渲染出序列帧后，然后由美术人员手绘补充上去的。<br><br>
于是我们开始制作了一些DEMO，最初放出来的图片和视频也是基于一些既有素材，然后添加美术元素做的一些概念实现。<br><br><div align="center">
<img id="aimg_1009972" aid="1009972" zoomfile="https://di.gameres.com/attachment/forum/202109/22/094048mimfsm0mwdf5sov7.jpg" data-original="https://di.gameres.com/attachment/forum/202109/22/094048mimfsm0mwdf5sov7.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/094048mimfsm0mwdf5sov7.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">“汉家江湖2” 早期DEMO场景</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1009973" aid="1009973" zoomfile="https://di.gameres.com/attachment/forum/202109/22/094049nuk4krlrmcwmz8sw.jpg" data-original="https://di.gameres.com/attachment/forum/202109/22/094049nuk4krlrmcwmz8sw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/094049nuk4krlrmcwmz8sw.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">“汉家江湖2”早期DEMO场景</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1009974" aid="1009974" zoomfile="https://di.gameres.com/attachment/forum/202109/22/094049vjrrjopsbpo8kvoo.jpg" data-original="https://di.gameres.com/attachment/forum/202109/22/094049vjrrjopsbpo8kvoo.jpg" width="593" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/094049vjrrjopsbpo8kvoo.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">“汉家江湖2”早期DEMO战斗</font></font></div>
<br>
此时汉2项目其实进展非常顺利，似乎按照这个节奏开发，一年之内出试玩版指日可待。然而事实是我们想多了……<br><br><strong><font color="#de5650">步大扯蛋之典范</font></strong><br><br>
当时我们确实心比较野，内部同时有4个游戏在开发，分别是《汉家江湖》、《部落与弯刀》、《老江湖（后来改名模拟江湖）》和《汉家江湖2》。原本计划的《部落与弯刀》和《老江湖》都是一个快速项目，但由于内部需求不断升级，大家对项目的期待也不断提高，所以到这里我们人员已经非常严重的吃紧了。<br><br>
再加上《汉家江湖》更新1.2版本我们遇到了一个重大的滑铁卢……也是步子迈太大扯着蛋的典范，所以内部的研发压力非常大。<br><br>
于是我们做了一个决定：由于其他项目的开发进度远高于《汉2》，所以先中止《汉2》的开发，将人员并入到原有这些项目去，先把原来的项目都“搞定”了，再集中精力回来做《汉2》。<br><br><div align="center">
<img id="aimg_1009975" aid="1009975" zoomfile="https://di.gameres.com/attachment/forum/202109/22/094049a81q1q2mq1wmp741.jpg" data-original="https://di.gameres.com/attachment/forum/202109/22/094049a81q1q2mq1wmp741.jpg" width="595" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/094049a81q1q2mq1wmp741.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">部落与弯刀，一款开放世界沙盒游戏</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1009976" aid="1009976" zoomfile="https://di.gameres.com/attachment/forum/202109/22/094049zi2azig3ckhkzi2h.jpg" data-original="https://di.gameres.com/attachment/forum/202109/22/094049zi2azig3ckhkzi2h.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/094049zi2azig3ckhkzi2h.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">模拟江湖，一款市井武侠模拟经营游戏</font></font></div>
<br>
然后就是时间很长的开发了……《部落与弯刀》和《模拟江湖》的开发难度和工作量都不断在螺旋中增长，时至今日我们也没有交出满意的答案。当然，两个游戏我们都还在不断的开发和改进，《部落与弯刀的》Steam正式版应该会比较快和大家见面，手机版和Switch版本也会在明年发布。《模拟江湖》的重做版本也进行了第一轮测试，目前也快和大家第二轮测试见面了。<br><br><strong><font color="#de5650">重启项目</font></strong><br><br>
时间来到2020年，在《部落与弯刀》Steam EA版本发布以后，我们慎重考虑之下重启了《汉2》的开发探索。<br><br>
此时我们回过头去看当年的DEMO，已经发现当时的设计理念还是过于保守和落伍，美术概念也距离当今一线手游有不少差距。再加上汉家江湖在不断的更新中世界观进行迭代，已经不适合再用原来的思路去整个重制一个“3D版”。所以此时的重启“汉2”我们已经没有继续打算再用“汉家江湖”的名字，而是希望重新规划一个世界观，去讲一个新的、非那么传统经典武侠的故事，于是我们继续做了很多探索。<br><br>
那么原来已经在项目上落地的一些探索和积累，我们在慎重考虑后决定给现有线上的《汉家江湖》来整一个大的，在保持汉家江湖既有风格的情况下，做一个美术和玩法的升级，伴随着开放到60级的版本，带来一个新的2.0资料片。<br><br>
所以我们将项目一拆为2，一部分技术将并入到汉家江湖线上的运行版本，所有玩家都可以直接平滑过渡来体验这个升级。另一部分我们内部正在逐步加速孕育一个新的网络游戏，目前名字还没想好，内部代号为DBGRPG2022，可以透露的是：这将是一个多平台网络游戏、武侠题材。以及从名称上能够大致确定玩法和我们期待的上线发布时间。<br><br><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1009977" aid="1009977" zoomfile="https://di.gameres.com/attachment/forum/202109/22/094050wp8ddz6l3s33eepb.jpg" data-original="https://di.gameres.com/attachment/forum/202109/22/094050wp8ddz6l3s33eepb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/094050wp8ddz6l3s33eepb.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">版本拆分示意图</font></font></div>
<br><strong><font color="#de5650">新的开始</font></strong><br><br>
关注我们的小伙伴可能会知道，我们目前工作室已经在成都开始办公。未来将会以成都为主，逐步搬迁位于深圳的团队。<br><br>
在世界观上，“DBGRPG2022”（以下简称DR22）不会完全沿用汉家江湖，但一些人物会有机会在游戏中出场。游戏仍将是一个偏叙事向的RPG，并且拥有各种单机/联机玩法，发布平台为手机/PC。目前还处于研发早期阶段，将会是一个完全不同于汉家松鼠既往作品完成度的作品，我们非常欢迎优秀的小伙伴加入！<br><br>
如果顺利的话，本作将于最早明年年底左右和大家见面。<br><br><div align="center">
<img id="aimg_1009978" aid="1009978" zoomfile="https://di.gameres.com/attachment/forum/202109/22/094050oklku2ikl3m4b468.jpg" data-original="https://di.gameres.com/attachment/forum/202109/22/094050oklku2ikl3m4b468.jpg" width="596" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/094050oklku2ikl3m4b468.jpg" referrerpolicy="no-referrer">
</div>
<div align="center"><font size="2"><font color="#808080">概念剧情（DR22开发中DEMO）</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1009979" aid="1009979" zoomfile="https://di.gameres.com/attachment/forum/202109/22/094050jcccc84e4vbg55i6.jpg" data-original="https://di.gameres.com/attachment/forum/202109/22/094050jcccc84e4vbg55i6.jpg" width="583" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/094050jcccc84e4vbg55i6.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">概念剧情（DR22开发中DEMO）</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1009980" aid="1009980" zoomfile="https://di.gameres.com/attachment/forum/202109/22/094050tjejh1qkhncd6kld.jpg" data-original="https://di.gameres.com/attachment/forum/202109/22/094050tjejh1qkhncd6kld.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/094050tjejh1qkhncd6kld.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">概念场景（DR22开发中DEMO）</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1009981" aid="1009981" zoomfile="https://di.gameres.com/attachment/forum/202109/22/094051zwq7qwbo2ttit0vr.jpg" data-original="https://di.gameres.com/attachment/forum/202109/22/094051zwq7qwbo2ttit0vr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/094051zwq7qwbo2ttit0vr.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">真机运行画面-耶律红（DR22开发中DEMO）</font></font></div>
<div align="center"><font size="2"><font color="#808080"><br></font></font></div>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1009982" aid="1009982" zoomfile="https://di.gameres.com/attachment/forum/202109/22/094051pwu4w599c98ibsze.jpg" data-original="https://di.gameres.com/attachment/forum/202109/22/094051pwu4w599c98ibsze.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/22/094051pwu4w599c98ibsze.jpg" referrerpolicy="no-referrer"></font></font></div>
<div align="center"><font size="2"><font color="#808080">真机运行画面-椿岁（DR22开发中DEMO）</font></font></div>
<br>
最后是日常广告时间，我们的招人信息！<br><br>
在招岗位:<br><br>
http://www.hanjiasongshu.com/jobs.html<br><br><font size="2"><font color="#808080"></font></font><br><font size="2"><font color="#808080">来源：汉家松鼠 </font></font><br>
</td></tr></tbody></table>


  
</div>
            