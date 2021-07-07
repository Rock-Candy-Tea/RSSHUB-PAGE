
---
title: '《蓝色协议BLUE PROTOCOL》如何做电影动画级别的卡通渲染？'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202106/28/100820ar0ai48lztzsk0ra.jpg'
author: GameRes 游资网
comments: false
date: Mon, 28 Jun 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202106/28/100820ar0ai48lztzsk0ra.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2502254">
相关阅读：<br>
<a href="https://www.gameres.com/876961.html" target="_blank">《蓝色协议BLUE PROTOCOL》技术分享解读</a><br>
<a href="https://www.gameres.com/867673.html" target="_blank">日式 MMORPG 《蓝色协议》试玩评测：仿佛亲自走入一部动画之中</a><br>
<br>
近两年扎堆冒头的开放世界游戏里，模仿塞尔达做卡通渲染风格的产品不在少数。<br>
<br>
在更重视技术侧的国内环境下，摆在这类产品面前的一道难题，是如何让卡渲与其他产品拉开视觉差异，形成自己的一套风格化表现。而对于概念设计先行的日厂来说，风格化打磨是他们更擅长的内容创作的一环。<br>
<br>
今天想分享的内容，是万代南梦宫Online与万代南梦宫Game Studio共同开发的PC动作网游《蓝色协议》，有关风格化卡渲的经验分享。该产品由UE4研发，主打全球市场和「一眼就看得出来是日产」的赛璐璐风格特征。<br>
<br>
<div align="center">
<img id="aimg_988260" aid="988260" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100820ar0ai48lztzsk0ra.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100820ar0ai48lztzsk0ra.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100820ar0ai48lztzsk0ra.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
2019年7月官方放出了第一则PV，尽管官方标语中没有提及开放世界，但初期放出的场景观感明显针对开放世界和超大地图而来，而且最后几秒钟的镜头FF味很足。去年初随第一次测试，游戏公开第二支PV，这次点出的主题更明确，冲突感也更强，充满了日系作品的中二味。<br>
<br>
而这款游戏最吸引我的部分，便是游戏流程当中的诸多日系动画固有的细节表现。并不是指传统的建模风格、人物设定，而是人物表情动作、镜头语言、剧情桥段等一整套的演出手法，比如从测试版中的这类张力十足的场景。<br>
<br>
<div align="center">
<img id="aimg_988261" aid="988261" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100820ajb4db6uyb4z9j0y.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100820ajb4db6uyb4z9j0y.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100820ajb4db6uyb4z9j0y.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988262" aid="988262" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100820o5y181yfprp515g9.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100820o5y181yfprp515g9.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100820o5y181yfprp515g9.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988263" aid="988263" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100821wdt0u550z6ldukuv.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100821wdt0u550z6ldukuv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100821wdt0u550z6ldukuv.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
有意思的是，最近业内朋友和葡萄君聊到，有产品看了这一分享后，经过一段时间学习和打磨，最后改头换面，突然有了味道。还有技术从业者看过后感叹：「只想抄书」。当然，葡萄君更希望这类技术分享能打开更多团队的思路，让大家摸索出自己实打实的特色，于是将这篇旧闻再翻出来分享给大家。<br>
<br>
<div align="center">
<img id="aimg_988264" aid="988264" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100821h7o07m5hg41ugfm9.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100821h7o07m5hg41ugfm9.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100821h7o07m5hg41ugfm9.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
以下内容为去年CEDEC开发者大会上《蓝色协议》制作组的专题演讲，由GAME Watch和Online Gamer等日媒首发，游戏葡萄根据多家日媒文章编译整理，内容稍有加工、整合与补充。<br>
<br>
<div align="center"><font color="#de5650"><strong>01</strong></font></div><br>
<div align="center"><font color="#de5650"><strong>「宛如剧场版动画电影的世界」</strong></font></div><br>
<br>
《蓝色协议》立项时，为了将其培养成万代南梦宫的一个新晋IP，制作组选择了全球化的战略方向。<br>
<br>
这意味着在面对国内外诸多竞品的时候，这款游戏的画面需要让人一眼就看出来这是出自日本团队之手，所以他们确立的核心方针，就是将赛璐璐动画表现手法钻研到极致，并以此推动整个项目的研发。<br>
<br>
用一句话来总结其核心概念设计，就是「壮丽不失精致的赛璐璐风游戏」。<br>
<br>
<div align="center"><font size="2"><font color="#708090">
<img id="aimg_988265" aid="988265" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100821x7uya0075r0a0yp5.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100821x7uya0075r0a0yp5.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100821x7uya0075r0a0yp5.jpg" referrerpolicy="no-referrer">
</font></font></div><br>
<div align="center"><font size="2"><font color="#708090">概念设计</font></font></div><br>
<br>
不过，赛璐璐这个概念能延伸出各种各样的表现形式，比如项目组成员自己的印象里，就偏向于「细节削减一些、比较笼统、但又不失精致的东西」。<br>
<br>
这类先入为主的观念，恰恰是他们在为《蓝色协议》做设计时最大的障碍，比如在制作资产（Assets）的时候，每个人的先入观都会影响到赛璐璐风格的具体表现。<br>
<br>
于是制作组进一步提炼概念，得到了一个关键词「宛如进入剧场版动画电影世界的作品」。这个概念原本仅在内部用来讨论，给不同成员做说明，如今干脆被用作《蓝色协议》的主题，放在了官网最显眼位置。<br>
<br>
<div align="center"><font size="2"><font color="#708090">
<img id="aimg_988266" aid="988266" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100821ayn02ze00imtm2wd.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100821ayn02ze00imtm2wd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100821ayn02ze00imtm2wd.jpg" referrerpolicy="no-referrer">
</font></font></div><br>
<div align="center"><font size="2"><font color="#708090">游戏实景（封测版）</font></font></div><br>
<br>
那么具体来说世界观怎么设定，又要怎么制作？<br>
<br>
确定了美术的方向以后，接下来要思考的就是世界观设定。最开始，团队里讨论要设定成科幻风的RPG网游，但经过不断的讨论，世界观的重心开始从科幻要素，渐渐移向剑与魔法、古代超文明的幻想世界。<br>
<br>
灵感来自于一个假设：「如果16世纪身穿甲胄的人类士兵，突然获得了先进的技术制作出了宇航服，会怎么样？」大家发现，原本不可能共存的组合拼在一起，说不定会很有趣，于是新的点子就这样一发不可收拾。<br>
<br>
<div align="center">
<img id="aimg_988267" aid="988267" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100822x3dglmbvmins7ang.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100822x3dglmbvmins7ang.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100822x3dglmbvmins7ang.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
于是他们又融入了19世纪和20世纪前后的军服和现代化装扮，人物设定则为经常身着大量工业制品进行生活。整体描绘成了一个介于幻想和科幻之间的世界。<br>
<br>
<div align="center">
<img id="aimg_988268" aid="988268" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100822kmjjrr0zw0ivlxmi.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100822kmjjrr0zw0ivlxmi.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100822kmjjrr0zw0ivlxmi.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
基本的世界观设定好了，但问题才刚刚开始，最核心的矛盾在于，赛璐璐表现手法和游戏偏自由的运镜非常矛盾。<br>
<br>
举个例子，在动画里，观众只能从作者设定好的角度去看这个世界，然而《蓝色协议》要做的是身处剧场版动画风世界中的体验，这意味着，当相机固定的时候，手绘风动画的还原度会提高，但要让每个角度看起来都不破坏这种动画氛围，实现起来会非常困难。<br>
<br>
说白了就是让玩家把脑袋钻进电视里，在动画的世界里面到处看。<br>
<br>
这并不是一件简单的事，在制作组看来，现实情况是「没有什么一劳永逸的操作，让赛璐璐表现手法与自由相机直接共存」，所以项目组的做法非常朴实无华，就是一步一个脚印地积累每个「有动画味的」细节。<br>
<br>
这类细节在游戏里很多，比如角色捏脸界面，整体设计就像动画的人设画面，玩家看上去的感觉，就像是在给动画做设定。<br>
<br>
<div align="center">
<img id="aimg_988269" aid="988269" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100822pwbr9m5f4619rr4k.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100822pwbr9m5f4619rr4k.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100822pwbr9m5f4619rr4k.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
还有可操作的角色，也会露出各种各样的表情，给玩家留下一个活灵活现的印象。<br>
<br>
<div align="center">
<img id="aimg_988270" aid="988270" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100822h0uk1dnvzk0ln306.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100822h0uk1dnvzk0ln306.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100822h0uk1dnvzk0ln306.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
还有攻击特效的不透明处理，以及画面边缘射入光线似的环境特效、滤镜等，都在强调动画式的观感。<br>
<br>
<div align="center"><font size="2"><font color="#708090">
<img id="aimg_988271" aid="988271" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100823f1rot000vzlxsz1t.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100823f1rot000vzlxsz1t.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100823f1rot000vzlxsz1t.jpg" referrerpolicy="no-referrer">
</font></font></div><br>
<div align="center"><font size="2"><font color="#708090">战斗特效</font></font></div><br>
<div align="center"><font size="2"><font color="#708090"><br>
</font></font></div><br>
<div align="center">
<img id="aimg_988272" aid="988272" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100823lam9lp66m7uggap0.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100823lam9lp66m7uggap0.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100823lam9lp66m7uggap0.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#708090">环境特效</font></font></div><br>
<div align="center"><font size="2"><font color="#708090"><br>
</font></font></div><br>
<div align="center">
<img id="aimg_988273" aid="988273" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100823nhasb9kxcansmdka.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100823nhasb9kxcansmdka.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100823nhasb9kxcansmdka.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#708090">环境滤镜</font></font></div><br>
<br>
只要是制作组感到来电的瞬间、要素，都是不能放过的细节。下面具体展开来说各个关键的部分。<br>
<div align="center"><strong><font color="#de5650"><br>
</font></strong></div><br>
<div align="center"><strong><font color="#de5650">02</font></strong></div><br>
<div align="center"><strong><font color="#de5650">动画风角色的表现手法</font></strong></div><br>
<br>
关于角色的表现手法，下面这张图是游戏中最终的角色外观成品图。<br>
<br>
<div align="center">
<img id="aimg_988274" aid="988274" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100823nzc19xwwb51b10nt.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100823nzc19xwwb51b10nt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100823nzc19xwwb51b10nt.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
首先看轮廓线。这款游戏的轮廓线采用了后处理绘制，在开发早期，游戏仅用轮廓模型来表现，但随着模型本身数据的削减，以及法线编辑成本降低的需要，逐渐转变为后处理绘制为主的模式。<br>
<br>
<div align="center">
<img id="aimg_988275" aid="988275" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100824nv2zj9hzw0f8iowh.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100824nv2zj9hzw0f8iowh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100824nv2zj9hzw0f8iowh.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
具体来说，首先利用相机读取的深度数据，对模型的轮廓描绘轮廓线，但是如红色箭头所示，处于模型内部的部分目前还无法绘制轮廓。<br>
<br>
<div align="center">
<img id="aimg_988276" aid="988276" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100824zelmzf665xgaemtt.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100824zelmzf665xgaemtt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100824zelmzf665xgaemtt.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
然后借助明亮度的差异进行内部描边，并且按照亮度差的大小，差异越大的地方描边的浓度越高。<br>
<br>
<div align="center">
<img id="aimg_988277" aid="988277" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100824pbibbjf0livlizvl.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100824pbibbjf0livlizvl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100824pbibbjf0livlizvl.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
然后借助明亮度的差异进行内部描边，并且按照亮度差的大小，差异越大的地方描边的浓度越高。<br>
<br>
<div align="center">
<img id="aimg_988278" aid="988278" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100824n7ia7qt9ei2l7w2l.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100824n7ia7qt9ei2l7w2l.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100824n7ia7qt9ei2l7w2l.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988279" aid="988279" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100825os3q8ys1ak8e83xq.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100825os3q8ys1ak8e83xq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100825os3q8ys1ak8e83xq.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
另外，轮廓模型运用了里侧模型向法线方向扩张的手法，同时利用工具计算相邻法线的平均值，来修复尖端分叉。<br>
<br>
<div align="center">
<img id="aimg_988280" aid="988280" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100825rewkoleowly8bk8l.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100825rewkoleowly8bk8l.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100825rewkoleowly8bk8l.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
以及轮廓模型不会用在模型整体上，只会在颚、口、耳等突出在模型之外的部分使用。早期制作组还试过用World Normal，但是对鼻梁等位置产生了多余的描边，所以面部关闭了这个功能。<br>
<br>
<div align="center">
<img id="aimg_988281" aid="988281" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100825b83dnth88ddnnttd.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100825b83dnth88ddnnttd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100825b83dnth88ddnnttd.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
下面是对下颚使用轮廓模型的例子，从正面看下颚的时候，也能依靠深度数据来给轮廓描边，但从侧面就会变得很难。<br>
<br>
<div align="center">
<img id="aimg_988282" aid="988282" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100825qb9vf9gftzfb6vfu.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100825qb9vf9gftzfb6vfu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100825qb9vf9gftzfb6vfu.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
而头发由于存在众多复杂的凹凸部分，所以也使用了轮廓模型，但对于一些过度绘制复杂内部法线的发型，需要用到Z Shift功能将它推回去的手法（<font color="#00bfff">蓝色箭头所示</font>）。<br>
<br>
<div align="center">
<img id="aimg_988283" aid="988283" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100826c8ohgnfooa33twws.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100826c8ohgnfooa33twws.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100826c8ohgnfooa33twws.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
关于着色，卡通着色边界选择了不适用渐变、强调边界区分的风格。为了提高角色与背景的融合度跟设置感，从地面到角色胸部会稍微用一点渐变着色。另外Normal map会因为dds压缩导致的像素噪点，对边界部分造成负面影响，所以在这里并没有使用该功能。<br>
<br>
<div align="center">
<img id="aimg_988284" aid="988284" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100826hxhoouisia2xc214.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100826hxhoouisia2xc214.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100826hxhoouisia2xc214.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
明暗平衡上，由于5:5在逆光的时候有可能导致所有着色都变成阴影色，角色看起来会很扁平，所以采用了偏亮的7:3方案。<br>
<br>
<div align="center">
<img id="aimg_988285" aid="988285" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100826b0avm6mh353mmv8m.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100826b0avm6mh353mmv8m.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100826b0avm6mh353mmv8m.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
针对扩散反射光的阴影颜色会自动生成，来降低工作量同时削减数据。但是，明亮度调低以后会让画面看起来浑浊，所以要么错开色相再调低亮度，要么尽量不调低饱和度。<br>
<br>
<div align="center">
<img id="aimg_988286" aid="988286" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100826ho8o4dcj81e6wncw.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100826ho8o4dcj81e6wncw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100826ho8o4dcj81e6wncw.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
总是出于阴影的部分就直接用贴图来表现，逆光的时候就调低保留细节。<br>
<br>
<div align="center">
<img id="aimg_988287" aid="988287" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100827c22icuku22gskwkk.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100827c22icuku22gskwkk.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100827c22icuku22gskwkk.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
类似下颚等部位，会调节顶点色的漫反射函数，让它尽量容易形成阴影色。<br>
<br>
<div align="center">
<img id="aimg_988288" aid="988288" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100827ww5r5p5e5qpcp51p.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100827ww5r5p5e5qpcp51p.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100827ww5r5p5e5qpcp51p.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
对于帽子、头盔等造成的阴影，则是用后处理来表现，先利用材质种类来辨别模型，然后在调用对应模型的遮罩，最后在模型下方错位后形成阴影。<br>
<br>
<div align="center">
<img id="aimg_988289" aid="988289" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100828c1b0qczj0l7kdq7x.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100828c1b0qczj0l7kdq7x.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100828c1b0qczj0l7kdq7x.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
逆光也用到了后处理，根据角色轮廓同等大小来绘制。来自地面的反射光则弱化后尽量控制光线射入，另外模型的闭塞部位，也会使用Occlusion Masks保证光线不会射入。<br>
<br>
<div align="center">
<img id="aimg_988290" aid="988290" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100828opm4ip0p2z0me0km.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100828opm4ip0p2z0me0km.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100828opm4ip0p2z0me0km.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
游戏中也会随时间变化，出现光源位于角色头顶的状况。这种情况下，即便调整模型法线，角色脸上也会出现多余的阴影。因此，皮肤的材质采用了光线入射角度减半的减轻措施。<br>
<br>
<div align="center">
<img id="aimg_988291" aid="988291" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100828tz18tokjzkw2b1k6.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100828tz18tokjzkw2b1k6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100828tz18tokjzkw2b1k6.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
可以看到角色身体和衣服都随模型形状产生阴影变化，但面部则是分阶段在变化。<br>
<br>
<div align="center">
<img id="aimg_988292" aid="988292" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100829o1zhamzdzaz5gt4x.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100829o1zhamzdzaz5gt4x.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100829o1zhamzdzaz5gt4x.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988293" aid="988293" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100829i4010y9dz0te6iw4.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100829i4010y9dz0te6iw4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100829i4010y9dz0te6iw4.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988294" aid="988294" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100829ko92oige1zoi1mox.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100829ko92oige1zoi1mox.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100829ko92oige1zoi1mox.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
关于头发的反射。在动画中，这是影响作品个性化的一大重点，《蓝色协议》的制作方向则是按照还原下面样图的大方向来推进的。<br>
<br>
<div align="center">
<img id="aimg_988295" aid="988295" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100830igf5pey5yhtuuo3o.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100830igf5pey5yhtuuo3o.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100830igf5pey5yhtuuo3o.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
距离相机近的时候，反射球会变小，但离相机越远，并非把发射求单纯变大，而是以类似叶子的形状，向两个顶点拉长。也就是贴图按照最大值来绘制，但让着色器的中心部位逐渐变小，要实际用上这个功能，需要解决几个问题。<br>
<br>
<div align="center">
<img id="aimg_988296" aid="988296" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100830wun3v3c118zg6s4i.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100830wun3v3c118zg6s4i.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100830wun3v3c118zg6s4i.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
一个问题是，展开头发均匀配置的UV，分给每个Mask的面积会变小，导致边界会出现像素感。但是这个问题无法靠增加分割面积来解决，所以针对反射部分采用新的UV。然后重新配置必要的步骤，再对贴图进行烘焙。另外，这里为了规避dds压缩的影响，采用了没有压缩的格式。<br>
<br>
<div align="center">
<img id="aimg_988297" aid="988297" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100830btttctrcch88287g.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100830btttctrcch88287g.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100830btttctrcch88287g.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988298" aid="988298" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100831zqg70rbe3bxaxq3e.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100831zqg70rbe3bxaxq3e.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100831zqg70rbe3bxaxq3e.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
另一个问题是，反射扩缩的判断该怎么进行。用到的方法是，在贴图输入的时候，对各个高光的重心进行判断，然后根据相隔的距离，来移动UV达到高光缩小的效果。所有数据都会通过贴图的各个通道来使用，R通道是原画像，G通道是距离重心的横坐标，B通道是距离重心的纵坐标，α通道是扩缩时为了不影响周围其他的东西，保管着各个高光点的ID。<br>
<br>
<div align="center">
<img id="aimg_988299" aid="988299" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100831t6aj209vsqqsa0vn.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100831t6aj209vsqqsa0vn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100831t6aj209vsqqsa0vn.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
下面是实际效果，反射边界没有噪点，拉远相机也能保留细节。<br>
<br>
<div align="center">
<img id="aimg_988300" aid="988300" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100831is8nshmqq4mrc1wb.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100831is8nshmqq4mrc1wb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100831is8nshmqq4mrc1wb.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
关于捏人。本作里男女性别分别可以选择三种体格，而且调整身高会调整等身的设置，另外丰满度会区分是否能调节的部位，并加上缓急的设定。<br>
<br>
<div align="center">
<img id="aimg_988301" aid="988301" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100831y8y3mk8fjkkbbn3o.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100831y8y3mk8fjkkbbn3o.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100831y8y3mk8fjkkbbn3o.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988302" aid="988302" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100832xzn7xjjzc6411m1j.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100832xzn7xjjzc6411m1j.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100832xzn7xjjzc6411m1j.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
头发除了单色，还可以选择渐变色，面部各个部位也可以选择颜色，往后还会上线更多关于瞳色、睫毛、装饰等功能，角色Pose等功能也可以供玩家更好地查看捏脸效果。<br>
<br>
<div align="center">
<img id="aimg_988303" aid="988303" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100832d77dzn3xrg8eiis8.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100832d77dzn3xrg8eiis8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100832d77dzn3xrg8eiis8.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988304" aid="988304" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100832aluu0wggzsfslndu.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100832aluu0wggzsfslndu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100832aluu0wggzsfslndu.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988305" aid="988305" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100833fzhsbs1z997shb1f.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100833fzhsbs1z997shb1f.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100833fzhsbs1z997shb1f.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988306" aid="988306" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100833s8n89qqq5q5dzkjj.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100833s8n89qqq5q5dzkjj.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100833s8n89qqq5q5dzkjj.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988307" aid="988307" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100833d1tyyjhl3la36f81.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100833d1tyyjhl3la36f81.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100833d1tyyjhl3la36f81.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
要实现这种如同动画设定画的界面，需要对多个坐标进行摄像，然后将数据作为2D贴图使用，并且在同一个画面内重合。<br>
<br>
<div align="center">
<img id="aimg_988308" aid="988308" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100834ahe8u2smn7hr8nh1.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100834ahe8u2smn7hr8nh1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100834ahe8u2smn7hr8nh1.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988309" aid="988309" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100834bku6ppy1urke6rvg.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100834bku6ppy1urke6rvg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100834bku6ppy1urke6rvg.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
另外换装方面，为了控制成本，只用了一套资产，影响换装的部位会通过顶点色来输入数据。具体来说，上衣袖子的长度会固定为四段，并且让互相干涉的部位隐藏不显示。但是单纯不显示无法应对胖瘦的区别，所以在连接部位加入细骨，保证模型之间不会互相影响。<br>
<br>
<div align="center">
<img id="aimg_988310" aid="988310" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100834a7rhifzsozao47er.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100834a7rhifzsozao47er.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100834a7rhifzsozao47er.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988311" aid="988311" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100834w6knac6vye84vb7k.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100834w6knac6vye84vb7k.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100834w6knac6vye84vb7k.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
关于表情，由于画面内需要表现多个角色，所以为了降低消耗采用了骨骼的方式。总共使用150根骨骼，来表现25个情感各异的表情，同时用到了口型和眼镜的不同组合。<br>
<br>
<div align="center">
<img id="aimg_988312" aid="988312" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100835xspu8u8y68by6dky.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100835xspu8u8y68by6dky.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100835xspu8u8y68by6dky.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988313" aid="988313" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100835tz85m8fdgx586xdd.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100835tz85m8fdgx586xdd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100835tz85m8fdgx586xdd.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center"><strong><font color="#de5650">03</font></strong></div><br>
<div align="center"><strong><font color="#de5650">适合动画风角色的特效</font></strong></div><br>
<br>
为了配合动画风格的表现手法，《蓝色协议》中使用了大量的不透明素材来制作特效，而这种选择与角色的亲和力更高。<br>
<br>
<div align="center">
<img id="aimg_988314" aid="988314" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100835qfvo7fv3me3o2f3d.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100835qfvo7fv3me3o2f3d.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100835qfvo7fv3me3o2f3d.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
但是，不透明素材由于其特性，在特效重合的时候会降低画面的辨识度。<br>
<br>
<div align="center">
<img id="aimg_988315" aid="988315" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100835ff8t8qxxzt8608q1.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100835ff8t8qxxzt8608q1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100835ff8t8qxxzt8608q1.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
这款游戏为了改善这个问题，采用了根据相机距离对特效进行消除的处理手法。当相机靠近到一定距离的时候，特效就不会表示，从而方式辨识度降低。<br>
<br>
<div align="center">
<img id="aimg_988316" aid="988316" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100835xakikbillul2adwu.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100835xakikbillul2adwu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100835xakikbillul2adwu.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
另外，一般在动画里用到的特效都会有固定的循环模式，但是游戏里用起来会给玩家留下单调的印象。<br>
<br>
<div align="center">
<img id="aimg_988317" aid="988317" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100836aggpb7shh4gjrsh4.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100836aggpb7shh4gjrsh4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100836aggpb7shh4gjrsh4.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
所以游戏采用了给贴图增加扭曲效果的Flow Map功能，以及给贴图明暗Mask增加消失效果的dissolve功能，来组合表现出随机感和动画的消失感。<br>
<br>
<div align="center">
<img id="aimg_988318" aid="988318" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100836ovnjr4p5zkynsirv.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100836ovnjr4p5zkynsirv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100836ovnjr4p5zkynsirv.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
除此之外，通过Fresnel功能对Particle Mesh进行区分作色，来保证从不同角度的相机，都能看到不同外观的特效。<br>
<br>
<div align="center">
<img id="aimg_988319" aid="988319" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100836auu6xmman5usham6.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100836auu6xmman5usham6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100836auu6xmman5usham6.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988320" aid="988320" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100836u0h9m5irshchixii.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100836u0h9m5irshchixii.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100836u0h9m5irshchixii.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
接下来，关于如何活用顶点移动材质功能。首先如下面几张图片，角色挥出的斩击动作，不论从哪个角度看，都表现得非常自然。<br>
<br>
<div align="center">
<img id="aimg_988321" aid="988321" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100837zuu4sz4nmyl5fyoo.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100837zuu4sz4nmyl5fyoo.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100837zuu4sz4nmyl5fyoo.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988322" aid="988322" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100837tuirwczll0mmkmqi.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100837tuirwczll0mmkmqi.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100837tuirwczll0mmkmqi.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988323" aid="988323" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100837uohhfnhhrm4hhhhq.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100837uohhfnhhrm4hhhhq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100837uohhfnhhrm4hhhhq.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
如果斩击动作只用2D形式来呈现，侧面看起来只会是一条线。但通过调用UE4材质编辑器中的世界位置函数，就可以实现编辑模型顶点的定点移动材质功能。在《蓝色协议》里，一部分特效采用了StaticMesh Morph Target功能，它能储存模型UV通道的顶点移动信息，在模型里生成两个Morph Target。<br>
<br>
比如准备3个没有拓扑变化的模型，用StaticMesh Morph Target写出后，就能变成可变形的模型。再将它通过Particle系统随机触发，套上雷电的贴图，就可以做出一套电击特效。<br>
<br>
<div align="center">
<img id="aimg_988324" aid="988324" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100838tvork6ru4odv55ld.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100838tvork6ru4odv55ld.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100838tvork6ru4odv55ld.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988325" aid="988325" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100838kgg7zvcvygfaxmvz.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100838kgg7zvcvygfaxmvz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100838kgg7zvcvygfaxmvz.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988326" aid="988326" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100838ogf8khbkhbvhqh8w.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100838ogf8khbkhbvhqh8w.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100838ogf8khbkhbvhqh8w.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center"><font size="2"><font color="#708090">
<img id="aimg_988327" aid="988327" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100838ctcnent80pf1ttq8.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100838ctcnent80pf1ttq8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100838ctcnent80pf1ttq8.jpg" referrerpolicy="no-referrer">
</font></font></div><br>
<div align="center"><font size="2"><font color="#708090">仅用一个mesh就能实现多种形态变化</font></font></div><br>
<br>
另外，如果斩击特效用平面来表现，在不同的角度可能会导致看不见。<br>
<br>
<div align="center">
<img id="aimg_988328" aid="988328" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100839ifshk4kkmwkfwb5k.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100839ifshk4kkmwkfwb5k.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100839ifshk4kkmwkfwb5k.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988329" aid="988329" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100839yvdetd6kcztev16d.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100839yvdetd6kcztev16d.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100839yvdetd6kcztev16d.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
这个问题可以通过StaticMesh Morph Target设置一个可被破坏的的面包圈状模型。<br>
<br>
<div align="center">
<img id="aimg_988330" aid="988330" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100839vh46iykp78juh4ju.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100839vh46iykp78juh4ju.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100839vh46iykp78juh4ju.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
然后根据斩击的动作将模型顶点设置为可顺着面包圈的轮廓被破坏，让斩击动作可以带动模型的变化。<br>
<br>
<div align="center">
<img id="aimg_988331" aid="988331" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100839dad6ytsej69iypat.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100839dad6ytsej69iypat.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100839dad6ytsej69iypat.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988332" aid="988332" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100840atomfjjz9olrd8ed.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100840atomfjjz9olrd8ed.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100840atomfjjz9olrd8ed.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
再根据相机的朝向设置模型可随之转动（将模型Y轴对相机的朝向幅度数值化）。<br>
<br>
<div align="center">
<img id="aimg_988333" aid="988333" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100840yrs6sjjfhdfms60z.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100840yrs6sjjfhdfms60z.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100840yrs6sjjfhdfms60z.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988334" aid="988334" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100840sseiiz1asasstszs.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100840sseiiz1asasstszs.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100840sseiiz1asasstszs.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
这样一来，就能呈现出追随视线移动的斩击特效。<br>
<br>
<div align="center">
<img id="aimg_988335" aid="988335" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100840iykists4383k3ttz.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100840iykists4383k3ttz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100840iykists4383k3ttz.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
关于后处理，《蓝色协议》的目标是还原出动画的摄影处理效果。<br>
<br>
动画摄影处理效果是动画制作中至关重要的、必不可少的一个环节，属于在制作工序的收尾环节，对整体色调进行调整、对画面进行Para渐变处理、对光源进行漏光处理等，施加多种特效处理的制作过程。<br>
<br>
<div align="center">
<img id="aimg_988336" aid="988336" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100841mi0qpofjyr1olipq.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100841mi0qpofjyr1olipq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100841mi0qpofjyr1olipq.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
注：Para，蜡纸（Paraffin）的简称，一种色彩叠加手法，用于表现阴影和环境反射光，在赛璐璐时代用蜡纸处理，所以日本动画制作领域沿用了这个简称。<br>
<br>
要还原剧场动画式表现手法，动画摄影处理就是绕不过的一个关口。可以看一下具体的效果对比：<br>
<br>
<div align="center">
<img id="aimg_988337" aid="988337" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100841iddlmtym88jv8ylw.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100841iddlmtym88jv8ylw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100841iddlmtym88jv8ylw.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988338" aid="988338" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100841afeiv3blemb6bbeb.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100841afeiv3blemb6bbeb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100841afeiv3blemb6bbeb.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
考虑到泛用性，《蓝色协议》中Para的动作关联了以太阳为基准的SunFlare特效。具体来说，通过蓝图将太阳的世界坐标输送给材质，再通过改变Screen Space UV，设定太阳位置从Screen Space坐标朝向画面中央，就能做到用贴图来还原出动画风天空光的Para特效。<br>
<br>
把这一后处理设定为正常的10倍数值，就能看到下图中更明显的效果。<br>
<br>
<div align="center">
<img id="aimg_988339" aid="988339" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100841bcgt5oouz3ouu3pu.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100841bcgt5oouz3ouu3pu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100841bcgt5oouz3ouu3pu.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
不过，这个效果不能常开，比如在洞窟内、建筑物内，就不需要表现这类突出光线来源的特效，所以制作组又设置了一套判断相机是否进入阴影的机制。通过材质处理这套判断机制后，就可以切换向阳和背阴时的特效表现。<br>
<br>
<div align="center">
<img id="aimg_988340" aid="988340" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100841hprr825loieq2eup.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100841hprr825loieq2eup.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100841hprr825loieq2eup.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
然而在瞬间切换光线效果的时候，会造成画面的光线闪烁，所以需要再加一个持续数秒的变化效果。<br>
<br>
<div align="center">
<img id="aimg_988341" aid="988341" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100841f0xcua6axvpaaukv.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100841f0xcua6axvpaaukv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100841f0xcua6axvpaaukv.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
此外，针对不同的时间带，后处理环节还准备了4中特效，通过overlap手法来使用。<br>
<br>
<div align="center">
<img id="aimg_988342" aid="988342" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100842lacdkd8akzt11exa.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100842lacdkd8akzt11exa.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100842lacdkd8akzt11exa.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center"><strong><font color="#de5650">04</font></strong></div><br>
<div align="center"><strong><font color="#de5650">动画风格的场景渲染</font></strong></div><br>
<br>
关于背景资产。尽管这些资产使用了基于物理的材质，但是没有采用写实渲染，而是更注重日式动画背景的味道。而采用动画风不等于要降低模型的精度，模型本身也要按照真实形状来雕刻。为了实现这个效果，制作组刻意对一些模型细节进行了剔除。<br>
<br>
<div align="center">
<img id="aimg_988343" aid="988343" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100842o330x132p380azzd.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100842o330x132p380azzd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100842o330x132p380azzd.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988344" aid="988344" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100842mrw3vd1dwkd4c2k2.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100842mrw3vd1dwkd4c2k2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100842mrw3vd1dwkd4c2k2.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988345" aid="988345" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100842xdhd4hq9y4dzd40v.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100842xdhd4hq9y4dzd40v.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100842xdhd4hq9y4dzd40v.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988346" aid="988346" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100843keeas6xxsenja96e.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100843keeas6xxsenja96e.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100843keeas6xxsenja96e.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
如果对贴图进行手绘处理，不仅费时，也会因为制作者的能力差异产生很大的质量波动。所以在制作贴图的时候，制作组放弃Photoshop转用Substance，提炼出动画背景画风格的视觉要素，在Substance中做成材质，从而快速地制作质量稳定的贴图。<br>
<br>
<div align="center">
<img id="aimg_988347" aid="988347" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100843g1qr4ne5e33e318r.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100843g1qr4ne5e33e318r.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100843g1qr4ne5e33e318r.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
以木桶为例：<br>
<br>
<div align="center">
<img id="aimg_988348" aid="988348" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100843demwme9mq1hmcqcl.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100843demwme9mq1hmcqcl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100843demwme9mq1hmcqcl.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
木块颜色对比度太高，更尖锐的绘制方法：<br>
<br>
<div align="center">
<img id="aimg_988349" aid="988349" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100843j5zdbbubdlbqurq8.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100843j5zdbbubdlbqurq8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100843j5zdbbubdlbqurq8.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
弱化对比度，调整锐度：<br>
<br>
<div align="center">
<img id="aimg_988350" aid="988350" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100844vi4qlzlkbllqrbrk.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100844vi4qlzlkbllqrbrk.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100844vi4qlzlkbllqrbrk.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
通用高斯模糊滤镜和通用马赛克滤镜处理后的最终效果：<br>
<br>
<div align="center">
<img id="aimg_988351" aid="988351" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100844t2y50iyhq55myt43.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100844t2y50iyhq55myt43.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100844t2y50iyhq55myt43.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
能看到，采用这类手法后，物件的边缘部分，会比写实效果更强调手绘感。<br>
<br>
<div align="center">
<img id="aimg_988352" aid="988352" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100844dqlulrnwd85m4uqq.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100844dqlulrnwd85m4uqq.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100844dqlulrnwd85m4uqq.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988353" aid="988353" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100844qlk3lvzk83v3k22z.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100844qlk3lvzk83v3k22z.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100844qlk3lvzk83v3k22z.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
关于草原材质的动画式表现手法。在参考了各式各样的动画作品之后，制作组的重心放在了三个关键点上：一是根据距离相机的远近减少草地贴图颜色的数据；二是对草原整体设置色斑效果；三是追加高光效果，来表现风吹过草原的反光感。<br>
<br>
<div align="center">
<img id="aimg_988354" aid="988354" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100845pergwolgxwgljxxu.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100845pergwolgxwgljxxu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100845pergwolgxwgljxxu.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
这是不满足这三个条件的草原效果：<br>
<br>
<div align="center">
<img id="aimg_988355" aid="988355" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100845pk6yer30klhcdjur.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100845pk6yer30klhcdjur.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100845pk6yer30klhcdjur.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
第一步设置和效果：<br>
<br>
<div align="center">
<img id="aimg_988356" aid="988356" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100845wtfnvzn2fnto3tqv.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100845wtfnvzn2fnto3tqv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100845wtfnvzn2fnto3tqv.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988357" aid="988357" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100845b9913w9j6ns939cn.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100845b9913w9j6ns939cn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100845b9913w9j6ns939cn.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
第二步设置和效果：<br>
<br>
<div align="center">
<img id="aimg_988358" aid="988358" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100846lte095xdjzfftl97.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100846lte095xdjzfftl97.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100846lte095xdjzfftl97.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988359" aid="988359" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100846s5swyy3gjq23icpg.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100846s5swyy3gjq23icpg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100846s5swyy3gjq23icpg.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
第三步的设置和最终效果：<br>
<br>
<div align="center">
<img id="aimg_988360" aid="988360" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100846o3mww5vvvt5fmmhc.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100846o3mww5vvvt5fmmhc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100846o3mww5vvvt5fmmhc.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988361" aid="988361" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100847i5r5pilkb99r7siz.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100847i5r5pilkb99r7siz.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100847i5r5pilkb99r7siz.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
除了前文提到的与SunFlare关联的后处理之外，还有很多为了实现动画表现而用到的后处理效果。第一个是SNN滤镜，它可以计算相邻像素点的信息，并计算出平均值，来呈现手绘风格的细节。<br>
<br>
<div align="center">
<img id="aimg_988362" aid="988362" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100847lg7a05zax0xa2992.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100847lg7a05zax0xa2992.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100847lg7a05zax0xa2992.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
具体可以对照下面几组开关前后的效果图。<br>
<br>
<div align="center">
<img id="aimg_988363" aid="988363" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100847hzgbbbbivywirzsr.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100847hzgbbbbivywirzsr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100847hzgbbbbivywirzsr.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988364" aid="988364" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100847osdaa96aac4dyew4.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100847osdaa96aac4dyew4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100847osdaa96aac4dyew4.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988365" aid="988365" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100847y35zre3n7mezc661.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100847y35zre3n7mezc661.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100847y35zre3n7mezc661.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988366" aid="988366" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100848hwolep3hur7z3jzr.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100848hwolep3hur7z3jzr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100848hwolep3hur7z3jzr.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988367" aid="988367" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100848cbfzy49u4yu00m0b.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100848cbfzy49u4yu00m0b.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100848cbfzy49u4yu00m0b.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
此外，阴影色采用了自定义功能来实现，该功能可以指定距离相机远和近的场所，并且可以在远近之间切换颜色状态，主要阴影的部分和阴影边缘部分上，阴影色的呈现率可以实现单独控制，以及阴影绘制方法的调整等。<br>
<br>
<div align="center">
<img id="aimg_988368" aid="988368" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100848ez5srym2q7q70ghi.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100848ez5srym2q7q70ghi.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100848ez5srym2q7q70ghi.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988369" aid="988369" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100848bsz9iqszs8lefexe.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100848bsz9iqszs8lefexe.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100848bsz9iqszs8lefexe.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
阴影色有无的对比，近景阴影的青色成分的呈现率偏低，远景阴影的绿色成分呈现率稍强：<br>
<br>
<div align="center">
<img id="aimg_988370" aid="988370" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100849qrnrc8tqm3rvdnmn.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100849qrnrc8tqm3rvdnmn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100849qrnrc8tqm3rvdnmn.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988371" aid="988371" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100849fadq6fqa2p8jad9h.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100849fadq6fqa2p8jad9h.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100849fadq6fqa2p8jad9h.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
最后，游戏也用到了体积雾、体积阴影等渲染手法。<br>
<br>
<div align="center">
<img id="aimg_988372" aid="988372" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100849e16r9899s6gfp9zr.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100849e16r9899s6gfp9zr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100849e16r9899s6gfp9zr.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988373" aid="988373" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100849vwqd2o23d5wwh7qw.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100849vwqd2o23d5wwh7qw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100849vwqd2o23d5wwh7qw.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988374" aid="988374" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100849wokib7kknukt5kzn.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100849wokib7kknukt5kzn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100849wokib7kknukt5kzn.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
以上就是《蓝色协议》制作组的分享内容了。<br>
<br>
总体来看，相比目前市面上的开放世界/大世界网络游戏，《蓝色协议》在制作手法上最大的不同，就是用赛璐璐式的美术风格为基准，在游戏内摸索动画电影式观感的卡渲制作手法。<br>
<br>
而这个制作思路，要求制作组以单点打磨的思路去积累和实现每一个有动画味的细节表现。这并不是一个高效的制作思路，但某种程度上讲，要在诸多竞争对手中脱颖而出，这个级别的付出也是必不可少的。<br>
<br>
文章最后放一组《蓝色协议》在去年4月份的CBT版本截图，UI也很舒服，不过是完全针对PC的设计：<br>
<br>
<div align="center">
<img id="aimg_988375" aid="988375" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100850j690ae4ia5k60f90.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100850j690ae4ia5k60f90.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100850j690ae4ia5k60f90.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988376" aid="988376" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100850w9j7zjbxzr6jmz2n.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100850w9j7zjbxzr6jmz2n.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100850w9j7zjbxzr6jmz2n.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988377" aid="988377" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100850lhlidip9sshprp9r.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100850lhlidip9sshprp9r.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100850lhlidip9sshprp9r.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988378" aid="988378" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100851j3etf3tg93tdyt4h.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100851j3etf3tg93tdyt4h.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100851j3etf3tg93tdyt4h.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988379" aid="988379" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100851w90q5nx9i0q6hf2t.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100851w90q5nx9i0q6hf2t.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100851w90q5nx9i0q6hf2t.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988380" aid="988380" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100851gnz28a2j9hh7xpa6.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100851gnz28a2j9hh7xpa6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100851gnz28a2j9hh7xpa6.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988381" aid="988381" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100852k090ut8qtttptqbb.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100852k090ut8qtttptqbb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100852k090ut8qtttptqbb.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988382" aid="988382" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100852ijve0nyg082rmmnf.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100852ijve0nyg082rmmnf.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100852ijve0nyg082rmmnf.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988383" aid="988383" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100852fx7kj7v5vw5luxkb.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100852fx7kj7v5vw5luxkb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100852fx7kj7v5vw5luxkb.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988384" aid="988384" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100852nbv3hwewb82zh8bp.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100852nbv3hwewb82zh8bp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100852nbv3hwewb82zh8bp.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988385" aid="988385" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100852sbkmi4beuznbbmb3.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100852sbkmi4beuznbbmb3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100852sbkmi4beuznbbmb3.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988386" aid="988386" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100853d656k0ergm2eyus2.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100853d656k0ergm2eyus2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100853d656k0ergm2eyus2.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988387" aid="988387" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100853vnquhfp885xsutuw.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100853vnquhfp885xsutuw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100853vnquhfp885xsutuw.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988388" aid="988388" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100853m8mzm8kii5j7mm7m.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100853m8mzm8kii5j7mm7m.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100853m8mzm8kii5j7mm7m.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988389" aid="988389" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100853c2639f3g9f83pgb9.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100853c2639f3g9f83pgb9.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100853c2639f3g9f83pgb9.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988390" aid="988390" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100854lvyy0h7hevyv13in.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100854lvyy0h7hevyv13in.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100854lvyy0h7hevyv13in.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988391" aid="988391" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100854q5206c6063kccd43.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100854q5206c6063kccd43.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100854q5206c6063kccd43.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988392" aid="988392" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100854ixc2mkzp77a4vxiv.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100854ixc2mkzp77a4vxiv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100854ixc2mkzp77a4vxiv.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988393" aid="988393" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100854o4cmpnd4693mk68z.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100854o4cmpnd4693mk68z.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100854o4cmpnd4693mk68z.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img id="aimg_988394" aid="988394" zoomfile="https://di.gameres.com/attachment/forum/202106/28/100855hmmmmnalb6dlgbj7.jpg" data-original="https://di.gameres.com/attachment/forum/202106/28/100855hmmmmnalb6dlgbj7.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202106/28/100855hmmmmnalb6dlgbj7.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
文章来源：<br>
<br>
<font size="2">https://game.watch.impress.co.jp/docs/news/1275034.html</font><br>
<br>
参考内容：<br>
<br>
<font size="2">https://www.onlinegamer.jp/news/202009040001/</font><br>
<font size="2">https://www.famitsu.com/news/202009/08205405.html</font><br>
<font size="2">https://cgworld.jp/feature/202011-cedec2020-bluep.html</font><br>
<font size="2">https://www.gamespark.jp/article/2020/05/07/98864.html</font><br>
<font size="2">https://game.watch.impress.co.jp/docs/kikaku/1250117.html</font><br>
<font size="2">https://www.onlinegamer.jp/news/202004290007/</font><br>
<br>
<font size="2"><font color="#708090">编译/依光流</font></font><br>
<br>
<font size="2"><font color="#708090">来源：游戏葡萄</font></font><br>
<font size="2"><font color="#708090">地址：<a href="https://mp.weixin.qq.com/s/UO30PlEZpzzLNSzMBhkpBQ" target="_blank">https://mp.weixin.qq.com/s/UO30PlEZpzzLNSzMBhkpBQ</a></font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            