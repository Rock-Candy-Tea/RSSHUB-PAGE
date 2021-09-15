
---
title: '【枭·音频】感同声受——《暗影火炬城》PS5 HD震动制作'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202109/09/143223e9a8ctttkzgg0tim.jpg'
author: GameRes 游资网
comments: false
date: Thu, 09 Sep 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202109/09/143223e9a8ctttkzgg0tim.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2513850">
<div align="center">
<img id="aimg_1007465" aid="1007465" zoomfile="https://di.gameres.com/attachment/forum/202109/09/143223e9a8ctttkzgg0tim.jpg" data-original="https://di.gameres.com/attachment/forum/202109/09/143223e9a8ctttkzgg0tim.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/143223e9a8ctttkzgg0tim.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1007466" aid="1007466" zoomfile="https://di.gameres.com/attachment/forum/202109/09/143223b1qnt8uiubmwnhnu.jpg" data-original="https://di.gameres.com/attachment/forum/202109/09/143223b1qnt8uiubmwnhnu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/143223b1qnt8uiubmwnhnu.jpg" referrerpolicy="no-referrer">
</div><br>
记者：请问雷德文先生，参与《暗影火炬城》的动作演出是怎样的一种体验呢？<br>
<br>
雷德文：整体来说相当愉快，只有一开始出了点小问题。在拍摄初期我在根本感受不到铁拳是否命中，导致NG了许多次。<br>
<br>
雷德文：后来导演给了我使用铁拳的资格，演出效果一下子上升了好几个台阶。<br>
<br>
唯一的缺点就是和我对戏的群演，经常三天两头就要调换一批，磨合起来有点花时间。<br>
<br>
《暗影火炬城》是上海钛核网络（TiGames）开发的一款银河恶魔城动作游戏。在上一期，我们与各位分享了在《暗影火炬城》角色语音后期处理方面的浅显心得。本期，我们将向各位介绍点干货，《暗影火炬城》登录PS5平台后带来的崭新体验——手柄HD震动功能。<br>
<br>
在以前，手柄震动都是由程序一手控制。而如今时代变了，声音设计师翻身做主人，获得了调教手柄震动的大权！屏幕前的你如果是一位声音设计师，或是对PS5手柄HD震动好奇的玩家， 不妨跟着枭工作室一起坐上智慧直通车，开往HD震动制作小课堂的绿皮火车就要发车啦！<br>
<br>
<strong><font color="#de5650">一、知识小课堂——HD震动原理与实现</font></strong><br>
<br>
在PS4时代，手柄震动依靠两个电机来驱动，用电机的配重不同，来模拟不同振幅和频率的震动。它的缺点就是无法让震动快速启动和停止，中间会有迟滞感，从音频的角度来说就是Attack（启动）和Release（恢复）时间过长。<br>
<br>
<div align="center">
<img id="aimg_1007467" aid="1007467" zoomfile="https://di.gameres.com/attachment/forum/202109/09/143224j51110tb1t1611bd.jpg" data-original="https://di.gameres.com/attachment/forum/202109/09/143224j51110tb1t1611bd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/143224j51110tb1t1611bd.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">PS4手柄内部构造，配重不同的非线性马达</font></font></div><br>
相比之下，PS5手柄采用了Foster音圈马达（Voice Coil Actuator）驱动，可以做到急起、急停，且震动行程与频率可以精密控制。<br>
<br>
PS5手柄震动的原理与扬声器类似，依靠声音引发震动。由于音圈马达是扬声器的一种，因此在PS5手柄连接电脑后，会被系统视为音频输出设备，可以被音频软件驱动。这使得PS5手柄不仅能轻松模拟出各种细腻的震动效果，还可以播放音乐。<br>
<br>
<div align="center">
<img id="aimg_1007468" aid="1007468" zoomfile="https://di.gameres.com/attachment/forum/202109/09/143224oumchkmu05nukryf.jpg" data-original="https://di.gameres.com/attachment/forum/202109/09/143224oumchkmu05nukryf.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/143224oumchkmu05nukryf.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">PS5手柄内部构造，搭配了音圈马达提供震动</font></font></div><br>
<strong><font color="#de5650">二、揽活的金刚钻——施工的必备工具</font></strong><br>
<br>
一般情况下，直接将手柄与电脑连接是不能正常工作的。PS5手柄并未对PC做适配，只能在Steam这类提供了API适配的游戏平台使用。因此在电脑上进行HD震动设计，必须借助一些工具的帮助。<br>
<br>
为了让工作在正确的轨道上运行，我们要求在编辑的音频的同时，能感受到手柄映射的震动，这就得让DAW（音频工作站）的音频一同输出到耳机和PS5手柄。<br>
<br>
我们使用了两个虚拟音频跳线软件，用来搭建MAC和PC的工作环境。<br>
<br>
在PC平台，我们使用的是VB-Audio推出的的Virtual Audio Cable。<br>
<br>
<div align="center">
<img id="aimg_1007469" aid="1007469" zoomfile="https://di.gameres.com/attachment/forum/202109/09/143225eih1gqlz07p0wlac.jpg" data-original="https://di.gameres.com/attachment/forum/202109/09/143225eih1gqlz07p0wlac.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/143225eih1gqlz07p0wlac.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">辅助工具 VoiceMetter WIN，PC平台上可以免费使用的一款高质量音频软件 官方网站链接：https://vb-audio.com/Cable/index.html</font></font></div><br>
而对于Mac平台，我们使用了RogueAmoeba旗下的LoopBack。<br>
<br>
<div align="center">
<img id="aimg_1007470" aid="1007470" zoomfile="https://di.gameres.com/attachment/forum/202109/09/143225p5xeu7i67v2huegg.jpg" data-original="https://di.gameres.com/attachment/forum/202109/09/143225p5xeu7i67v2huegg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/143225p5xeu7i67v2huegg.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">辅助工具 LoopBack MAC，MAC平台上的一款音频软件，界面简洁易于使用 官方网站链接：https://www.rogueamoeba.com/loopback/</font></font></div><br>
以上两个工具都是为了实现虚拟跳线，将音频工作站的音频输出到耳机和手柄中。<br>
<br>
需要注意的是，PS手柄的输入通道有四个，我们实际使用的是通道3&4，这两个才是驱动HD震动的通道。<br>
<br>
<div align="center">
<img id="aimg_1007471" aid="1007471" zoomfile="https://di.gameres.com/attachment/forum/202109/09/143226u0wdwutu9hhg97zh.jpg" data-original="https://di.gameres.com/attachment/forum/202109/09/143226u0wdwutu9hhg97zh.jpg" width="279" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/143226u0wdwutu9hhg97zh.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">在LoopBack使用通道3&4，或者VM中选择MixDawn就能完成手柄和耳机的连接</font></font></div><br>
将工作站的音频输出通道改至虚拟跳线软件后，我们便可以开始HD震动音效的制作了！<br>
<br>
<strong><font color="#de5650">三、Show Time！——HD震动制作流程</font></strong><br>
<br>
在正式的教学开始前，我们需要了解PS5手柄HD震动制作三个要点：<br>
<br>
<ul><li><strong>频率限定</strong>，PS5手柄支持的最佳频率范围在40HZ～400HZ，超出频率范围后震感会急剧下降。</li><li><strong>频率清晰</strong>，由于支持的频率范围有限、线性马达的能效限制，震动样本的频率组成如果过于复杂，我们得到的震感就会浑浊，不清晰。</li><li><strong>解放音量</strong>，手柄震动的音圈并不是传统扬声器，它可承载的能量比音频系统中的相对音量要高得多，所以不需要顾虑这个问题。我们可以在正常音量标准下制作，在植入游戏中后，提升震动的输出音量。调整到合适的强度，输出音量提升2至3倍都没有问题。<br>
</li></ul><br>
将这三个要点牢记于心，现在让我们开始制作吧！<br>
<br>
<strong>“移花接木，用已有的声音素材高切加工</strong><br>
<br>
制作震动最直接的方式就是借助已有的音效，后期处理之后输出给手柄。<br>
<br>
例如：我们需要为玩家的武器命中添加震动，那我们可以直接使用命中音效，高切掉400HZ以上的频率，即可获得一个基础的震动文件。<br>
<br>
这样得到的震动效果可以接受，但比较粗犷还不够细腻，所以我们还需要根据命中类型，加入其他波形，丰富震动细节。<br>
<br>
这里是金属敲击石头碎裂的音效，为了震感清晰，我们先加入一点石头掉落的细节。在加上一个200HZ左右的正弦波，作为金属碰撞的余震。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1007472" aid="1007472" zoomfile="https://di.gameres.com/attachment/forum/202109/09/143226a1prypkk55ugeknr.jpg" data-original="https://di.gameres.com/attachment/forum/202109/09/143226a1prypkk55ugeknr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/143226a1prypkk55ugeknr.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">命中的震动样本结构</font></font></div><br>
实际工作中，并不是所有震动都需要单独设计。时间有限的话，直接高切输出也是可行的。方便在项目中快速预览，调整震动制作的优先级。<br>
<br>
<strong>“另起炉灶，根据音效特点类比定做</strong><br>
<br>
为了达到更高品质的HD震动效果，就需要根据游戏表现特别设计音效，这里我们以《暗影火炬城》主角雷德文的通讯仪PAD为例，展示震动波形的制作过程。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1007473" aid="1007473" zoomfile="https://di.gameres.com/attachment/forum/202109/09/143229s67ekbm6xbeqbrss.jpg" data-original="https://di.gameres.com/attachment/forum/202109/09/143229s67ekbm6xbeqbrss.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/143229s67ekbm6xbeqbrss.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《暗影火炬城》的pad界面</font></font></div><br>
通讯仪是一个上世纪年代感的电子仪器，它有三个表现重点：动画节奏，设备启动，复古风格。<br>
<br>
我们首先制作了一段低频正弦波和方波，用以模拟启动时的重量感。设备启动的部分，我们通过调整锯齿波的调值包络曲线实现复古感，FC时代的游戏音乐音效便是用它制作的。此时声音还缺少一些厚度，于是我们把叠加处理过频率的白噪音，做与前者同样的处理。<br>
<br>
在pad启动的收尾，我们使用300hz的正弦波表现pad启动中的零件碰撞，接着使用短促的白噪音补充整体细节。（200HZ以上的正弦波可以模拟清脆的振感）<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1007474" aid="1007474" zoomfile="https://di.gameres.com/attachment/forum/202109/09/143229dsrszuzk6k0hbl87.jpg" data-original="https://di.gameres.com/attachment/forum/202109/09/143229dsrszuzk6k0hbl87.jpg" width="474" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/143229dsrszuzk6k0hbl87.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Pad启动的震动样本结构</font></font></div><br>
手动制作震动样本时，我们多使用基础波形来调制合成震动，这样可以获得清晰，层次分明的震感。以下是们在工作中常用的插件，基本上都是音频工作站的基础套件。除此之外，还使用音乐合成器合成需要的效果，合成撞击、设备启动等震动。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1007475" aid="1007475" zoomfile="https://di.gameres.com/attachment/forum/202109/09/143230cfujfyu86y39ynn6.jpg" data-original="https://di.gameres.com/attachment/forum/202109/09/143230cfujfyu86y39ynn6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/143230cfujfyu86y39ynn6.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">我们在制作时使用了相当多的中间工具，但都是音频工作站的基础插件</font></font></div><br>
如果声音引擎支持，也可使用实时的音频合成器。在游戏中根据游戏参数的变化，合成震动的音频样本。例如驾驶载具、武器效果、环境效果等。<br>
<br>
<strong><font color="#de5650">四、张弛有度，震动设计不可雨露均沾</font></strong><br>
<br>
在设计《暗影火炬城》的震动时，我们是有所保留的。并非让每个声音都产生震动。《暗影火炬城》一款类银河恶魔城游戏，玩家关注的重点是战斗和地图探索，声音不应喧宾夺主。<br>
<br>
在音乐和绘画中领域中，都有留白的说法。同理在游戏中，若是玩家的手柄时刻都有反馈，长时间游玩难免会有审美疲劳，产生厌恶感。<br>
<br>
我们不需要让角色行动的每一步都给出反馈，对玩家来说很累，对设计师来说也是。大量的样本要花大量时间配置和调试，设计师面对这般海量的工作，怕是只有献祭头发这一个选择了。<br>
<br>
<div align="center">
<img id="aimg_1007476" aid="1007476" zoomfile="https://di.gameres.com/attachment/forum/202109/09/143231u8bb07k63all0nnl.jpg" data-original="https://di.gameres.com/attachment/forum/202109/09/143231u8bb07k63all0nnl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/143231u8bb07k63all0nnl.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《瑞奇与叮当—时空跳转》震动效果细节丰富，这背后是无数设计师的头发堆成的小山</font></font></div><br>
在《暗影火炬城》中，我们主要给角色的武器攻击、命中反馈、道具交互设计了震动反馈。那些繁琐的细节被我们一一放弃，只为让玩家能够更加专注的游玩。<br>
<br>
<strong><font color="#de5650">五、一点点私货，给PS5手柄玩家的尝鲜</font></strong><br>
<br>
为了能方便大家理解HD震动的应用，我们以《暗影火炬城》中的一段过场CG为例，为其添加了HD震动。有条件的朋友可以连接手柄播放，体验一番。<br>
<br>
<strong><font color="#de5650">总结</font></strong><br>
<br>
相较于以往的声音设计强调关注音画之间的关系，PS5HD震动功能的出现使音频工作者也能参与触觉的设计，为玩家提供更加丰富完整的游戏表达。受益于游戏主机次世代的来临，我们枭工作室得以为《暗影火炬城》设计细致的震动反馈，让玩家更沉浸地体验主角的冒险故事。<br>
<br>
虽然SONY官方早在2020年就已经提到本文探讨的内容，并且制作了一套专门的HD震动波形制作工具。但如此高级的工具并非人人都能接触到，因此我们希望借这篇文章分享给大家使用音频日常工具制作HD震动波形的方法。<br>
<br>
时代在进步，我们更要不断学习，砥砺前行。以上是枭工作室参与《暗影火炬城》HD震动工作的一些心得分享，希望与各位热爱游戏的同仁，一起发掘它的潜力。<br>
<br>
如果各位想要切实体验HD震动对游戏体验的提升，不妨在《暗影火炬城》中与铁拳兔一起感受“拳拳到肉”！点击阅读原文，直达PS平台购买链接。<br>
<br>
<font color="#808080">《暗影火炬城》PS5、PS4，购买链接：</font><br>
<font color="#808080">https://store.playstation.com/zh-hans-hk/product/HP6808-PPSA03970_00-FISTASIAPS5HK003/</font><br>
<font color="#808080"><br>
</font><br>
<font color="#808080">《暗影火炬城》steam预购链接：</font><br>
<font color="#808080">https://store.steampowered.com/app/1330470/_/</font><br>
<br>
<strong><font color="#de5650">相关阅读：</font></strong><br>
<br>
<a href="https://www.gameres.com/888923.html" target="_blank">【枭·音频】注入灵魂—《暗影火炬城》角色语音后期处理</a><br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：枭工作室</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/nRa2K6hbkmf9lCQCeemhIA</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            