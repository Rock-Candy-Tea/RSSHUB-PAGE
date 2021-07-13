
---
title: '腾讯天美分享：如何独立制作游戏demo？'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202107/01/093331veyk6yruu336mf6f.jpg'
author: GameRes 游资网
comments: false
date: Thu, 01 Jul 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202107/01/093331veyk6yruu336mf6f.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2502743">
<i><font color="#808080">本文首发“腾讯天美工作室群”知乎号</font></i><br>
<i><font color="#808080">https://www.zhihu.com/question/30768958/answer/1952778209</font></i><br>
<br>
DEMO，全称是demonstration，意为“演示，示范”，而游戏DEMO简单来说就是一个游戏的示范版本，其目的是在开发时间与工作量可控的情况下，做出一款游戏的可玩雏形，验证玩法或预期体验是否有足够吸引力。<br>
<br>
如果尝试自己制作一款游戏DEMO，有两方面的好处：<br>
<br>
对自己，能在实践中学到更多游戏开发的知识，了解游戏的构成，比如角色、动作、关卡设计等；<br>
<br>
对项目，也可以在一两周内就输出可视化雏形，向领导或团队演示讲解自己的想法和概念。<br>
<br>
对于希望开发游戏的入门者来说，独自制作3D游戏DEMO将会是一个庞大艰深的工程，而受独立开发者青睐的2D像素游戏要相对切实可行，比如横版过关游戏。<br>
<br>
我们邀请了来自天美的Dino为大家分享他制作横版动作游戏Demo的经验，希望对大家有所帮助。<br>
<br>
<i><font color="#808080">*本文仅出于个人学习和经验分享的目的，以部分网络素材为例，为大家图文演示游戏DEMO的制作方法。</font></i><br>
<i><font color="#808080">*在实际生活中，不论是否以商业盈利为目的发布自制的游戏，都不可以使用他人拥有版权的素材。</font></i><br>
<br>
从行走逻辑上区分，横版动作游戏一般分为单线横版、纵深横版。从玩法上区分，还可以细分为格斗、射击、动作等。<br>
<br>
如今，横版射击和格斗游戏都略有些没落，而横版动作却仍颇受欢迎，也将是我们接下来将讨论的重点。<br>
<br>
<div align="center">
<img id="aimg_989200" aid="989200" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093331veyk6yruu336mf6f.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093331veyk6yruu336mf6f.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093331veyk6yruu336mf6f.jpg" referrerpolicy="no-referrer">
</div><br>
工欲善其事必先利其器。针对横版过关游戏，市面上有哪些现成的游戏开发软件可以选择？<br>
<br>
<div align="center">
<img id="aimg_989201" aid="989201" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093331abh0shw84p8pb1sw.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093331abh0shw84p8pb1sw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093331abh0shw84p8pb1sw.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_989202" aid="989202" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093332g3hszjrggyoe2rr2.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093332g3hszjrggyoe2rr2.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093332g3hszjrggyoe2rr2.jpg" referrerpolicy="no-referrer">
</div><br>
2DFM：全称是“2D格斗游戏制作工具2nd”。它是由日本OUTBACK制作、EB发行的一款2D格斗游戏制作工具。<br>
<br>
利用这款软件玩家可以独立制作出属于自己的PC格斗游戏——台湾FK小组制作的《超级COSPLAY大战final02版》。本人制作的《东东不死传说》都是用2DFM开发完成的。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_989203" aid="989203" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093332ve4hmr4laewhh2qf.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093332ve4hmr4laewhh2qf.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093332ve4hmr4laewhh2qf.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《东东不死传说》</font></font></div><br>
AGM：全称为ActionGameMaker，同样由日本EB发行。<br>
<br>
拥有ACT，ARPG，STG等组件，使用这些组件就能制作出相应的PC、XBOX360、PS3游戏，并且组件可以混合使用，例如可以做出地图上是ARPG，迷宫里是STG的游戏。可以说非常强悍。<br>
<br>
<div align="center">
<img id="aimg_989204" aid="989204" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093332bo2mm22qz5kqxz0q.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093332bo2mm22qz5kqxz0q.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093332bo2mm22qz5kqxz0q.jpg" referrerpolicy="no-referrer">
</div><br>
OPENBOR：横版过关游戏开发软件。BOR软件的原名是《Beats of Rage 》，名字有向SEGA的MD游戏《Streets of Rage》致敬的意思。<br>
<br>
开发者开源发布后改名为OPENBOR。它可以输出PC、安卓、PSP、XBOX等平台版本。下图是本人曾制作的横版DEMO。<br>
<br>
<div align="center">
<img id="aimg_989205" aid="989205" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093332t1xe8xs2fbws8ppa.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093332t1xe8xs2fbws8ppa.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093332t1xe8xs2fbws8ppa.jpg" referrerpolicy="no-referrer">
</div><br>
三者的适用面大致如下，而OPENBOR相对更适合横版动作游戏：<br>
<br>
<div align="center">
<img id="aimg_989206" aid="989206" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093333crpzjtmh3opoh1mg.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093333crpzjtmh3opoh1mg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093333crpzjtmh3opoh1mg.jpg" referrerpolicy="no-referrer">
</div><br>
接下来，让我们试试用OPEN BOR来制作一款横版动作游戏DEMO ——<br>
<br>
<div align="center">
<img id="aimg_989207" aid="989207" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093333f13wiii535uv1i35.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093333f13wiii535uv1i35.jpg" width="484" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093333f13wiii535uv1i35.jpg" referrerpolicy="no-referrer">
</div><br>
首先，我们先要了解一下动作游戏的构成。<br>
<br>
通常来说，一款横版动作游戏，包含了哪些元素？<br>
<br>
《恐龙世纪》的第一关可以拆解如下：<br>
<br>
<div align="center">
<img id="aimg_989208" aid="989208" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093333d31r8pjgc3zb3jpr.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093333d31r8pjgc3zb3jpr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093333d31r8pjgc3zb3jpr.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_989209" aid="989209" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093333ehmfxpzlxuh9e2gl.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093333ehmfxpzlxuh9e2gl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093333ehmfxpzlxuh9e2gl.jpg" referrerpolicy="no-referrer">
</div><br>
所谓的关卡，其实就是一群角色在一个房间里打架的过程：<br>
<br>
<div align="center">
<img id="aimg_989210" aid="989210" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093334jcfiqqqhbrbb5xvh.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093334jcfiqqqhbrbb5xvh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093334jcfiqqqhbrbb5xvh.jpg" referrerpolicy="no-referrer">
</div><br>
关卡的核心体验其实大同小异，这是另外一群角色在另外一个房间打架的过程。<br>
<br>
<div align="center">
<img id="aimg_989211" aid="989211" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093334jiusk7ksirty1zpt.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093334jiusk7ksirty1zpt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093334jiusk7ksirty1zpt.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_989212" aid="989212" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093334ix99poioygsjj9dw.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093334ix99poioygsjj9dw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093334ix99poioygsjj9dw.jpg" referrerpolicy="no-referrer">
</div><br>
说白了，这个就是一款动作游戏的基础框架：房间、人、打架。<br>
<br>
<div align="center">
<img id="aimg_989213" aid="989213" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093334izdxfdb40czdxq04.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093334izdxfdb40czdxq04.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093334izdxfdb40czdxq04.jpg" referrerpolicy="no-referrer">
</div><br>
那么我们可以针对这个房间，分解出一款横版动作游戏DEMO需要用到的素材：<br>
<br>
<strong>1.角色素材</strong><br>
<strong>2.场景素材</strong><br>
<strong>3.UI素材</strong><br>
<strong>4.音频素材</strong><br>
<br>
<div align="center">
<img id="aimg_989214" aid="989214" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093335ubq94yy1nnksbvhh.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093335ubq94yy1nnksbvhh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093335ubq94yy1nnksbvhh.jpg" referrerpolicy="no-referrer">
</div><br>
OPENBOR这款软件没有操作界面，纯文件夹操作。并且资源全部为熟悉的GIF、WAV等资源。可以从网上下载到OPENBOR的最新版本，容量只有几M。<br>
<br>
<div align="center">
<img id="aimg_989215" aid="989215" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093335ol7rr5g51gtgi450.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093335ol7rr5g51gtgi450.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093335ol7rr5g51gtgi450.jpg" referrerpolicy="no-referrer">
</div><br>
角色素材分为：主角、杂兵、特效。<br>
<br>
<div align="center">
<img id="aimg_989216" aid="989216" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093335ytghdtrft4zd45bt.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093335ytghdtrft4zd45bt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093335ytghdtrft4zd45bt.jpg" referrerpolicy="no-referrer">
</div><br>
出于演示目的，我使用了部分网络素材，希望大家有时间有条件还是尽量自己画。<br>
<br>
网络资源随意混搭会出现比例失调的情况。因此一定要规划好尺寸。<br>
<br>
<div align="center">
<img id="aimg_989217" aid="989217" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093336qqke3kajhupp3pp9.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093336qqke3kajhupp3pp9.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093336qqke3kajhupp3pp9.jpg" referrerpolicy="no-referrer">
</div><br>
角色资源整理好以后，放到Chars里面的次级文件夹里，以本人这个DEMO为例：\data\chars\mukui文件夹里。<br>
<br>
<div align="center">
<img id="aimg_989218" aid="989218" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093336az8861uvdbhhuvtu.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093336az8861uvdbhhuvtu.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093336az8861uvdbhhuvtu.jpg" referrerpolicy="no-referrer">
</div><br>
场景素材：同理。要么自己画，要么先用网络资源。<br>
<br>
<div align="center">
<img id="aimg_989219" aid="989219" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093336oaszsc2z2jthfxfm.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093336oaszsc2z2jthfxfm.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093336oaszsc2z2jthfxfm.jpg" referrerpolicy="no-referrer">
</div><br>
场景资源的透视关系也是很重要的。经过对比发现最常用的角度一般是30度或者45度。60度比较少见了。<br>
<br>
<div align="center">
<img id="aimg_989220" aid="989220" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093336eathcta2uoecl5et.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093336eathcta2uoecl5et.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093336eathcta2uoecl5et.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_989221" aid="989221" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093337jiui989jijefj1oh.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093337jiui989jijefj1oh.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093337jiui989jijefj1oh.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_989222" aid="989222" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093337cxyx8xfji5zvdbi3.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093337cxyx8xfji5zvdbi3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093337cxyx8xfji5zvdbi3.jpg" referrerpolicy="no-referrer">
</div><br>
场景资源整理好以后，放到Bgs里面的次级文件夹里，以本人这个DEMO为例：\data\bgs\city文件夹里。<br>
<br>
<div align="center">
<img id="aimg_989223" aid="989223" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093337aijdckzlwq394uqi.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093337aijdckzlwq394uqi.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093337aijdckzlwq394uqi.jpg" referrerpolicy="no-referrer">
</div><br>
UI素材：一般分为战斗UI和主菜单UI。OPENBOR自带了一套战斗UI资源，因此这个步骤可以缓一缓。等DEMO打磨得非常精美的时候，再替换成自己的UI也不迟。<br>
<br>
<div align="center">
<img id="aimg_989224" aid="989224" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093338c6cjxtjp0gphsqbw.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093338c6cjxtjp0gphsqbw.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093338c6cjxtjp0gphsqbw.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_989225" aid="989225" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093338k2vu8k8a2gua2ung.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093338k2vu8k8a2gua2ung.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093338k2vu8k8a2gua2ung.jpg" referrerpolicy="no-referrer">
</div><br>
音频素材：一般包含了背景音乐、音效。整理好以后，放到\data\music文件夹里。<br>
<br>
<div align="center">
<img id="aimg_989226" aid="989226" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093338zbp8xtpniu27o2o7.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093338zbp8xtpniu27o2o7.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093338zbp8xtpniu27o2o7.jpg" referrerpolicy="no-referrer">
</div><br>
音频可暂时使用部分网络资源，也可以用OPENBOR自带的资源。背景音乐OPENBOR采用的是BOR或OGG格式。<br>
<br>
音效：OPENBOR采用的是WAV格式。可以用GoldWave这个软件来切割。<br>
<br>
<div align="center">
<img id="aimg_989227" aid="989227" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093338idmsdl62njolsg2s.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093338idmsdl62njolsg2s.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093338idmsdl62njolsg2s.jpg" referrerpolicy="no-referrer">
</div><br>
音效：音频整理好以后，放到\data\sounds文件夹里。<br>
<br>
<div align="center">
<img id="aimg_989228" aid="989228" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093339pzee7bsbbb1e6dss.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093339pzee7bsbbb1e6dss.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093339pzee7bsbbb1e6dss.jpg" referrerpolicy="no-referrer">
</div><br>
通常一款横版动作游戏包含的模块：<br>
<br>
<strong>1.角色编辑器</strong><br>
<strong>2.AI编辑器</strong><br>
<strong>3.场景编辑器</strong><br>
<strong>4.关卡编辑器</strong><br>
<br>
有些软件会把这几个模块都放置到同一个面板。例如2D格斗软件2DFM就是同一个页面。但从程序开发角度来说，这些模块都是独立模块。每一个模块的开发周期可能1周-数月。<br>
<br>
<div align="center">
<img id="aimg_989229" aid="989229" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093339dem4du6uu3uuun30.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093339dem4du6uu3uuun30.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093339dem4du6uu3uuun30.jpg" referrerpolicy="no-referrer">
</div><br>
OPENBOR的编辑采用纯TXT文本操作。用户可以很容易找到各个模块的位置。资源准备就绪，我们就开始来编辑关卡了。OPENBOR的角色编辑是这个样子的。<br>
<br>
<div align="center">
<img id="aimg_989230" aid="989230" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093339hllnyx2yt70y7qql.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093339hllnyx2yt70y7qql.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093339hllnyx2yt70y7qql.jpg" referrerpolicy="no-referrer">
</div><br>
打开\data\chars\mukui下的角色TXT文本，可以看到很多可配参数——<br>
<br>
<div align="center">
<img id="aimg_989231" aid="989231" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093340daapk2pp2kaqpkpk.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093340daapk2pp2kaqpkpk.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093340daapk2pp2kaqpkpk.jpg" referrerpolicy="no-referrer">
</div><br>
开发者只需要按照OPENBOR的标准ID字符来配置这些参数即可。由于功能繁多，有兴趣的同学可以自行阅读OPENBOR的开发说明文档。例如这是主角的普通直拳的一个配置——<br>
<br>
<div align="center">
<img id="aimg_989232" aid="989232" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093340uwcwc081oz1upfuq.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093340uwcwc081oz1upfuq.jpg" width="490" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093340uwcwc081oz1upfuq.jpg" referrerpolicy="no-referrer">
</div><br>
简单的说，就是主角以不同的速度来播放了446-450整套序列帧图。并且在448号图的时候触发了攻击框。<br>
<br>
大家有没有发现，这套编辑方法本质上就是GIF动画的编辑逻辑，只不过在合适的帧数里加入了攻击判断。<br>
<br>
角色编辑小诀窍1：打击感的由来<br>
<br>
一套完整的打击感包括了以下几个基础因素：<br>
<br>
<strong>1.音效</strong><br>
<strong>2.光效</strong><br>
<strong>3.打中人的瞬间，双方的抖动帧数</strong><br>
<br>
<div align="center">
<img id="aimg_989233" aid="989233" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093341lz3w5iknn33qwc30.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093341lz3w5iknn33qwc30.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093341lz3w5iknn33qwc30.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_989234" aid="989234" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093341ewkuh1dagt49mhwd.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093341ewkuh1dagt49mhwd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093341ewkuh1dagt49mhwd.jpg" referrerpolicy="no-referrer">
</div><br>
经过研究发现，不同的动作游戏其顿帧的时间不同。似乎动作游戏的顿帧时长都偏低呢，比格斗游戏还短。分析其原因，就是因为动作游戏频繁攻击，如果顿帧时间太长很容易视觉疲劳。<br>
<br>
<div align="center">
<img id="aimg_989235" aid="989235" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093341mcqpcpprcvcvac9c.gif" data-original="https://di.gameres.com/attachment/forum/202107/01/093341mcqpcpprcvcvac9c.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093341mcqpcpprcvcvac9c.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">正常顿帧演示</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_989236" aid="989236" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093342x0j4jzfrr3ydyfvv.gif" data-original="https://di.gameres.com/attachment/forum/202107/01/093342x0j4jzfrr3ydyfvv.gif" width="320" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093342x0j4jzfrr3ydyfvv.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">不正常顿帧演示</font></font></div><br>
通常来讲，顿帧越长就意味着那一拳越带劲，打击感爆满。但是当一款游戏，所有攻击的顿帧都很长的时候，会显得非常无趣。就好比黑客帝国里整部电影都是子弹时间，或者某个宴席里所有菜都是烤乳猪。用户会非常腻烦……<br>
<br>
<div align="center">
<img id="aimg_989237" aid="989237" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093342vv3pmeyswftthver.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093342vv3pmeyswftthver.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093342vv3pmeyswftthver.jpg" referrerpolicy="no-referrer">
</div><br>
因此建议大部分攻击，其顿帧都维持在6-12之间的某个数，部分超必杀或者必杀技的收尾一击时，可以把数值配大。这个顿帧的应用，不仅可以用在2D项目上，其实3D项目也是共通的……<br>
<br>
<strong>角色编辑小诀窍2：判定框的绘制。</strong><br>
<br>
判定框分为受击框、攻击框、碰撞框。下图是受击框的一个范例。猜猜看哪种绘制方法是正确的，哪种是错误的？<br>
<br>
下图左边是正确的绘制，不随主角呼吸而晃动。右边是错误的绘制，过于强调跟随身体，会严重影响高玩的攻击判断。<br>
<br>
<div align="center">
<img id="aimg_989238" aid="989238" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093342cn3atcdld3ad0t5c.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093342cn3atcdld3ad0t5c.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093342cn3atcdld3ad0t5c.jpg" referrerpolicy="no-referrer">
</div><br>
格斗之王的受击框，在体形上相差不会很大。下蹲和跳跃姿态的时候甚至简化了一个框。<br>
<br>
<div align="center">
<img id="aimg_989239" aid="989239" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093343gxzc29vl9wczr0lr.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093343gxzc29vl9wczr0lr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093343gxzc29vl9wczr0lr.jpg" referrerpolicy="no-referrer">
</div><br>
街头霸王4的判定框也采用类似做法，一切从简。以打击感的稳定为目标。<br>
<br>
<div align="center">
<img id="aimg_989240" aid="989240" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093343vcqpaq0qqmqv2k1w.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093343vcqpaq0qqmqv2k1w.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093343vcqpaq0qqmqv2k1w.jpg" referrerpolicy="no-referrer">
</div><br>
判定框的绘制肯定也不需要随角色胳膊的晃动来变化，没必要每张都画。如果某个动作，其身体摆动幅度不大，那么其受击框应该尽量只绘制一套。（OPENBOR的逻辑是某一个指令会通吃下面所有脚本行，除非遇到了下一个同样的指令。）<br>
<br>
<div align="center">
<img id="aimg_989241" aid="989241" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093343rz647gx40x4g074i.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093343rz647gx40x4g074i.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093343rz647gx40x4g074i.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>角色编辑小诀窍3：动画帧数的调配。</strong><br>
<br>
角色的动作是由图片组成的，每一张图片的停留时间将决定了动画的快慢与否，流畅与否。<br>
<br>
通常一个动作包含了“发招，攻击，收招三”个阶段。也有些玩家习惯称之为“前摇、攻击、后摇”。<br>
<br>
<div align="center">
<img id="aimg_989242" aid="989242" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093344vkvfnvbybpsk6zj0.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093344vkvfnvbybpsk6zj0.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093344vkvfnvbybpsk6zj0.jpg" referrerpolicy="no-referrer">
</div><br>
制作统一的受击图，可以节约编辑工作。要知道SNK公司是做了十几年的格斗游戏，在手感这一块是顶尖的代表。因此虚心学习SNK公司的动画帧数数据是非常有必要的。<br>
<br>
<div align="center">
<img id="aimg_989243" aid="989243" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093344vm6r9w9mz393p80p.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093344vm6r9w9mz393p80p.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093344vm6r9w9mz393p80p.jpg" referrerpolicy="no-referrer">
</div><br>
下图是拳皇98的帧数表，可以适当参考。<br>
<br>
<div align="center">
<img id="aimg_989244" aid="989244" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093344c78sqabaq1ch1fj1.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093344c78sqabaq1ch1fj1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093344c78sqabaq1ch1fj1.jpg" referrerpolicy="no-referrer">
</div><br>
那么我们这个角色的第一拳，参数就参考一下金家潘，先这么设置吧。<br>
<br>
<div align="center">
<img id="aimg_989245" aid="989245" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093345u0qmltoqy904haao.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093345u0qmltoqy904haao.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093345u0qmltoqy904haao.jpg" referrerpolicy="no-referrer">
</div><br>
这里并非叫大家照着金家藩的手感来制作这个角色，而是通过一种低学习成本来尽早学会编辑角色。事实上当游戏完成后，自己完全可以微调各种参数。如果要自己去原创尝试，数值该怎么填？8、9、10？10、20、30？对于一个没有动作游戏编辑经验的策划来说，凭感觉去调整参数。说不定会适得其反，效果越调越差。<br>
<br>
特效和音效方面，OPENBOR默认播放的是flash.txt和flash.wav，图像资源位置在\data\chars\misc。<br>
<br>
<div align="center">
<img id="aimg_989246" aid="989246" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093345nf6f3fjdpj76rl6z.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093345nf6f3fjdpj76rl6z.jpg" width="489" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093345nf6f3fjdpj76rl6z.jpg" referrerpolicy="no-referrer">
</div><br>
当需要在某个特定的招式弃用特殊的特效和音效时。则在相应的attack里面配置新的特效。<br>
<br>
<div align="center">
<img id="aimg_989247" aid="989247" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093345nrygtszg8krg0tgm.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093345nrygtszg8krg0tgm.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093345nrygtszg8krg0tgm.jpg" referrerpolicy="no-referrer">
</div><br>
关卡方面，打开\data\levels下的关卡TXT文本，可以看到很多可配参数。<br>
<br>
<div align="center">
<img id="aimg_989248" aid="989248" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093345prsgrrg105qursss.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093345prsgrrg105qursss.jpg" width="485" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093345prsgrrg105qursss.jpg" referrerpolicy="no-referrer">
</div><br>
基本就就是列出了关卡所需的背景音乐、前后景需要的场景资源，下雨的特效、以及电话亭物件、敌兵的摆放坐标。<br>
<br>
关卡的清版逻辑很简单，有一个wait的字符，表示当前字符以前的敌兵必须全部杀死，才可以解开锁定的区域。<br>
<br>
时间关系，笔者不再罗列出所有脚本的功能用途。不过OPENBOR这款开源软件比较好的地方在于：所有功能都是用类似脚本的方式写入，网上可以很轻松的找到DEMO范例用来学习。<br>
<br>
我们来回顾一下一款动作游戏的DEMO，它是由哪些东西构成的。<br>
<br>
<div align="center">
<img id="aimg_989249" aid="989249" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093346gxomyqo5zykh653x.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093346gxomyqo5zykh653x.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093346gxomyqo5zykh653x.jpg" referrerpolicy="no-referrer">
</div><br>
积少成多，小关卡可以组成大关卡，大关卡可以组成大章节。<br>
<br>
<div align="center">
<img id="aimg_989250" aid="989250" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093346gvgs69zpxmlf9lub.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093346gvgs69zpxmlf9lub.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093346gvgs69zpxmlf9lub.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_989251" aid="989251" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093346g5yvbm45ovcy5pvy.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093346g5yvbm45ovcy5pvy.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093346g5yvbm45ovcy5pvy.jpg" referrerpolicy="no-referrer">
</div><br>
关卡就像是一枚螺丝钉，它的最终服务对象是游戏的各大核心系统。<br>
<br>
<div align="center">
<img id="aimg_989252" aid="989252" zoomfile="https://di.gameres.com/attachment/forum/202107/01/093346z57xe79pftepn54f.jpg" data-original="https://di.gameres.com/attachment/forum/202107/01/093346z57xe79pftepn54f.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/01/093346z57xe79pftepn54f.jpg" referrerpolicy="no-referrer">
</div><br>
制作DEMO的过程中，大家将学到哪些功能是必须的，哪些是可有可无的。<br>
<br>
当这些知识运用到我们工作中时，就会大大地节约策划、美术、程序之间的沟通成本。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">原文：https://www.zhihu.com/question/30768958/answer/1952778209</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            