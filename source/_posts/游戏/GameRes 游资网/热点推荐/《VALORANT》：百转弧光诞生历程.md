
---
title: '《VALORANT》：百转弧光诞生历程'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202109/17/100523zew6h6welib1850u.jpg'
author: GameRes 游资网
comments: false
date: Fri, 17 Sep 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202109/17/100523zew6h6welib1850u.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2514884">
大家好，我是《VALORANT》内容支援团队的程序员Brandon Wang。今天，我要和武器设计师Chris Stone一起带各位看看新武器造型「百转弧光」的开发过程，以及程序和设计师如何携手合作，为玩家带来令人印象深刻的精彩内容。<br><br>
百转弧光是一个全新挑战。我们已成功推出了至尊龙焰和紫金狂潮等造型，但对於那些喜欢奇巧的武器造型，却又同时喜欢独特几何与一些精细视觉特效的玩家，我们却还没有做过类似的设计尝试。在有了概念图後，内容支援团队便进行测试，看玩家是否喜欢此设计——幸好他们很爱！或许是因为这种奇形怪状的抽象造型不同於一般FPS游戏常见的设计吧。给大家看看吧：<br><br><div align="center">
<img id="aimg_1009287" aid="1009287" zoomfile="https://di.gameres.com/attachment/forum/202109/17/100523zew6h6welib1850u.jpg" data-original="https://di.gameres.com/attachment/forum/202109/17/100523zew6h6welib1850u.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/17/100523zew6h6welib1850u.jpg" referrerpolicy="no-referrer">
</div>
<br>
要让那些球体「活过来」本身就是个特殊的挑战，因为单靠视觉特效并不能达到我们想追求的深度。如果球体只是单纯发光，那测试时获得热烈回响的概念幻想就会直接破灭。<br><br>
因此，内容支援团队和内容设计团队携手合作，让概念设计得以化为现实。在工程师的帮助下，我们的设计师测试了超棒的游戏内着色器，不只创造了百转弧光球体着色器，还有各位在《VALORANT》看到的其他着色器。<br><br><strong><font color="#de5650">当美术遇上程勋</font></strong><br><br>
在《VALORANT》开发早期，我（Brandon）为了改良着色器（游戏图像背後的程式）和协助设计师实现美术风格，进行了许多基础工作。<br><br>
当我们确立美术风格，且游戏效能在GPU方面表现良好时，我便跳出来协助其他有特殊需求的团队，发挥我的专业：转译与材料工程。<br><br><div align="center">
<img id="aimg_1009288" aid="1009288" zoomfile="https://di.gameres.com/attachment/forum/202109/17/100524q2lbkbnlffkzlfzi.gif" data-original="https://di.gameres.com/attachment/forum/202109/17/100524q2lbkbnlffkzlfzi.gif" width="350" inpost="1" src="https://di.gameres.com/attachment/forum/202109/17/100524q2lbkbnlffkzlfzi.gif" referrerpolicy="no-referrer">
</div>
<br>
其中一个我参与开发的素材就是圣祈的灵球。我们想为圣祈设计一个类似宝石的能量来源，所以我用视差制作了一个原型，让灵球看起来有一个会在内部流动、漂浮的浑沌核心。<br><br><div align="center">
<img id="aimg_1009289" aid="1009289" zoomfile="https://di.gameres.com/attachment/forum/202109/17/100524wjfecpz7zm373fqx.gif" data-original="https://di.gameres.com/attachment/forum/202109/17/100524wjfecpz7zm373fqx.gif" width="342" inpost="1" src="https://di.gameres.com/attachment/forum/202109/17/100524wjfecpz7zm373fqx.gif" referrerpolicy="no-referrer"><font size="2"><font color="#708090"> 
<img id="aimg_1009297" aid="1009297" zoomfile="https://di.gameres.com/attachment/forum/202109/17/100713km6c85lsulzo888y.gif" data-original="https://di.gameres.com/attachment/forum/202109/17/100713km6c85lsulzo888y.gif" width="250" inpost="1" src="https://di.gameres.com/attachment/forum/202109/17/100713km6c85lsulzo888y.gif" referrerpolicy="no-referrer"></font></font>
</div>
<div align="center"><font size="2"><font color="#708090">（左：我的原型；右：完成版）</font></font></div>
<br>
视觉特效设计师以原型及其原理为基础，调整了外观，再加上自己的设计，就完成了各位在游戏内看到的最终版本。<br><br>
我特别在武器造型加入了一点有趣的技术。棱镜、雪崩和百变星云原本都是在基本款武器模组上进行的测试和原型，目的是为了看看像圣祈灵球的特殊效果能不能也做出让人眼睛为之一亮的武器造型。<br><br>
但仅仅如此并不足以产生有趣的效果——我们必须做出让设计师能够调整的造型，因此我们在棱镜上使用了色彩梯度来调整效果和颜色。<br><br>
雪崩起初是各种不同效果的大杂烩，目的是制造出像喜马拉雅盐灯那样的粉红色造型（这灵感来自於《VALORANT》公关经理桌上的摆饰灯）。结果看起来不太对，但设计师发现了蓝色版本，便以此为方向，发展成玩家现在看到的造型。<br><br><div align="center">
<img id="aimg_1009290" aid="1009290" zoomfile="https://di.gameres.com/attachment/forum/202109/17/100524dw07uwuu73y0u7y7.png" data-original="https://di.gameres.com/attachment/forum/202109/17/100524dw07uwuu73y0u7y7.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/17/100524dw07uwuu73y0u7y7.png" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1009291" aid="1009291" zoomfile="https://di.gameres.com/attachment/forum/202109/17/100525mr3d31d444yo6yry.png" data-original="https://di.gameres.com/attachment/forum/202109/17/100525mr3d31d444yo6yry.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/17/100525mr3d31d444yo6yry.png" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1009292" aid="1009292" zoomfile="https://di.gameres.com/attachment/forum/202109/17/100526sx9yybddxwi2xcil.jpg" data-original="https://di.gameres.com/attachment/forum/202109/17/100526sx9yybddxwi2xcil.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/17/100526sx9yybddxwi2xcil.jpg" referrerpolicy="no-referrer">
</div>
<br>
百变星云最初的概念只是「异界之门」，但我们在工程方面费了不少功夫，才将纹理材质减少到就算使用低配电脑进行游戏，最低效能仍可以负担的程度（这些限制是为了让玩家在使用华丽造型时，游戏也能快速运行）。<br><br>
我们最後利用立方体展开图的一面，拿来进行水平铺设以求毫无缝隙，最後加上「细节」纹理。不幸的是，有些玩家看了这个版本会头晕，而我们不希望有任何键盘惨遭荼毒。所以我们的设计师进一步推展幻想，调整效果以避免玩家晕眩恶心的状况。之後我们又请《VALORANT》开发团队中容易在生活中跟游戏中头晕的人员，来帮我们进行了多几轮的游戏测试。<br><br><div align="center">
<img id="aimg_1009293" aid="1009293" zoomfile="https://di.gameres.com/attachment/forum/202109/17/100526ebrn8nrhkme4bp0q.jpg" data-original="https://di.gameres.com/attachment/forum/202109/17/100526ebrn8nrhkme4bp0q.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/17/100526ebrn8nrhkme4bp0q.jpg" referrerpolicy="no-referrer">
</div>
<br>
这些工程原型距离能生产的造型还很遥远，因此所有原型都成为了设计师制作造型时能选择的工具。棱镜、雪崩和百变星云直接构成了各自造型的主要部分，但百转弧光则结合了圣祈灵球背後的技术，才得以形成完整的造型。说到圣祈的灵球，我记——等等，别拿走我的键盘，那是我自己组装的，是我的键——<br><br><strong><font color="#de5650">——程序与美术的邂逅</font></strong><br><br>
嘿，我是Chris，该我上场了。噢，这键盘真赞，这个手感……<br><br>
上面提到的原版圣祈着色器很棒，这是无庸置疑的，但并不符合原始设计对百转弧光球体的幻想。我联络了Bwang（就是Brandon），请他稍微说明圣祈着色器的背後原理。在他解释着色器网路在游戏引擎的设置方式之後，我这边就能进行一些微调，以更符合我们对武器造型的设计目标。<br><br>
调整过後，我开始使用以节点为架构的材质制作软体「Substance Designer」，研究更能符合概念球体造型的新材质，同时也注意效能和着色器的限制（好让游戏能快速运行）。<br><br>
以下摘录创造新材质的过程。最後，我们以圣祈灵球为发想，创造了更抽象的元素，以符合百转弧光的设计幻想。<br><br><div align="center">
<img id="aimg_1009294" aid="1009294" zoomfile="https://di.gameres.com/attachment/forum/202109/17/100528il8s7u1sh21e8umm.gif" data-original="https://di.gameres.com/attachment/forum/202109/17/100528il8s7u1sh21e8umm.gif" width="500" inpost="1" src="https://di.gameres.com/attachment/forum/202109/17/100528il8s7u1sh21e8umm.gif" referrerpolicy="no-referrer">
</div>
<br>
另外，再来快速提一下我们和内容支援团队的另一项合作成果：棱镜造型使用的自订着色器。经过Bwang的几次解说後，我们成功新增了可以调整球体色彩变幻效果的自订控制。<br><br>
给大家看看吧：<br><br><div align="center">
<img id="aimg_1009295" aid="1009295" zoomfile="https://di.gameres.com/attachment/forum/202109/17/100528ibep579z9r6g6jnf.jpg" data-original="https://di.gameres.com/attachment/forum/202109/17/100528ibep579z9r6g6jnf.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/17/100528ibep579z9r6g6jnf.jpg" referrerpolicy="no-referrer">
</div>
<br><strong>敬请期待未来的合作内容</strong><br><br>
以上只是几个例子，说明内容设计团队和内容支援团队如何密切合作、开发全新着色器，让《VALORANT》的玩家能使用各种独特造型。<br><br><div align="center">
<img id="aimg_1009296" aid="1009296" zoomfile="https://di.gameres.com/attachment/forum/202109/17/100528kncdcoorlcmdzota.jpg" data-original="https://di.gameres.com/attachment/forum/202109/17/100528kncdcoorlcmdzota.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/17/100528kncdcoorlcmdzota.jpg" referrerpolicy="no-referrer">
</div>
<br>
由於我们还有其他例行任务，不是所有造型都会经历此过程，但我们总是很期待能为大家制作出新的着色器。希望这能展现跨团队合作的力量，以及双方为同一件事投入心力时，能产生多麽棒的结果。<br><br>
当我们试着思考什麽会激发玩家的兴趣时，就有了共同的目标。设计师和工程师合作无间，也会持续发现新的工作模式！<br><br><font size="2"><font color="#708090">来源：拳头游戏</font></font><br><font size="2"><font color="#708090">地址：https://playvalorant.com/zh-tw/news/dev/b-i-zhu-n-huguang-muhou-yuanxun-shejishi-g-ngcheng-shi-y-jishu-jie-mi/</font></font><br><br>
</td></tr></tbody></table>


  
</div>
            