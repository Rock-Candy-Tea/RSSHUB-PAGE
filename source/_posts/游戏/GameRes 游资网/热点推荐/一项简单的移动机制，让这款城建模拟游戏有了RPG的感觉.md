
---
title: '一项简单的移动机制，让这款城建模拟游戏有了RPG的感觉'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202109/03/091923zk7frzig2fjuguug.png'
author: GameRes 游资网
comments: false
date: Fri, 03 Sep 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202109/03/091923zk7frzig2fjuguug.png'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2512953">
编者按：《空中王国》(Airborne Kingdom)是一款城建模拟类游戏，由The Wandering Band开发。近日，这家工作室的联合创始人本·旺达(BenWander)在外媒Game Developer发表文章，分享了开发团队是怎样为该作设定独特的移动机制的。GamRes对文章的主要文章进行了编译整理。<br>
<br>
在《空中王国》中，玩家在云端建造和发展一座独特城市，并且能够让它飞跃广阔的景观。从一开始，我们就想让玩家建造令人向往的空中城堡，而在持续迭代的过程中，我们还决定让玩家能够直接控制城镇的移动。这项机制帮助我们为一个流行品类(模拟城建)带来了独特的微创新，同时在很大程度上改变了公司内部设计师的角色。<br>
<br>
<div align="center">
<img id="aimg_1005923" aid="1005923" zoomfile="https://di.gameres.com/attachment/forum/202109/03/091923zk7frzig2fjuguug.png" data-original="https://di.gameres.com/attachment/forum/202109/03/091923zk7frzig2fjuguug.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/03/091923zk7frzig2fjuguug.png" referrerpolicy="no-referrer">
</div><br>
笔者曾经在几家3A开发商工作多年，于2015年离开Visceral Games，随后独自开发了叙事冒险游戏《悬案疑云》(A Case ofDistrust)。2017年底Visceral被关闭，几位老同事和我取得联系，共同创办了The Wandering Band工作室。我们都曾参与打造热门大作(《龙腾世纪》《星球大战》《战地》等)，但直到开发《空中王国》期间，我们才第一次感受到对于项目拥有完全的创作自由，并且有足够的技能和资源来完成项目。<br>
<br>
从一开始，我们就很喜欢创作一款空中城建游戏的主意。这个品类吸引了许多玩家，而在云端创造王国的潜力同样诱人。然而，我们鼓捣的首个原型却平平无奇，与同类游戏相比没有让人眼前一亮的特色......<br>
<br>
为了让《空中王国》能够在众多城建类游戏中脱颖而出，我们尝试过许多机制，但直到添加“右击移动”(程序员弗雷德·加鲁最初将它描述为“像在一款RPG里那样移动”)机制时，我们才完全看到了这款游戏的潜力：玩家只需要点击游戏世界的某个位置，整座城市就会飞过去。<br>
<br>
<div align="center">
<img id="aimg_1005924" aid="1005924" zoomfile="https://di.gameres.com/attachment/forum/202109/03/091924o2g8jj8zps0pbyyw.png" data-original="https://di.gameres.com/attachment/forum/202109/03/091924o2g8jj8zps0pbyyw.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/03/091924o2g8jj8zps0pbyyw.png" referrerpolicy="no-referrer">
</div><br>
这种机制与游戏的其他部分完美融合。例如，当玩家想要收集资源时，不用将工人派往越来越远的地方，而是可以让城市距离资源收集点更近。如果玩家想要获取新的建造技术，那就必须四处探索、寻找。随着城市规模变大，它会需要更强的推进力......这些内在联系和谐自然，让我们感到惊讶。不过，这套移动系统也要求我们投入大量精力塑造游戏世界。<br>
<br>
起初，我们倾向于创造被大片无人区隔开的大块资源，但后来我们发现，玩家似乎对那些有节奏、可以反复体验的小任务更感兴趣。玩家朝着某个很远的地方飞去，在城市移动的过程中旋转镜头，寻找附近的资源并分配工人。之后玩家又可能会寻找距离更近的资源，并重新分配工人以提升效率。从某种意义上讲，这种玩法就像游戏内的一个微循环，节奏也让玩家觉得很舒适。<br>
<br>
为了放大那种感觉，在《空中王国》中，没有任何区域会无限期地为玩家提供所有资源。玩家可能会在某个地方找到大量隐藏的特定资源，但他们必须迅速移动......我们将整个游戏世界分为不同版块，并确保各个区域的资源量趋于平衡。我们还仔细调整了王国(城市)与资源点之间的最大距离——如果资源点距离王国太远，工人就会自动取消分配给他们的任务。<br>
<br>
<div align="center">
<img id="aimg_1005925" aid="1005925" zoomfile="https://di.gameres.com/attachment/forum/202109/03/091925uu7tupospn7n7kop.png" data-original="https://di.gameres.com/attachment/forum/202109/03/091925uu7tupospn7n7kop.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/03/091925uu7tupospn7n7kop.png" referrerpolicy="no-referrer">
</div><br>
在迭代开发的过程中，我们发现“探索感”变得越来越重要了。如果我们希望鼓励玩家探索，那就需要创造一个值得探索的世界，而这甚至改变了我们在公司内部的角色。扎克·姆巴赫(Zach Mumbach)最初担任制作人，但他后来将更多精力放在了关卡设计上，目标是鼓励玩家探索游戏世界的各个角落，并为玩家提供一些特别的奖励。<br>
<br>
直到项目接近收官阶段时，我们还在不断添加让玩家可以通过探索发现的东西，例如可以招募更多市民的定居点，可以被用来建造非凡建筑的古代文物，以及允许玩家根据个人喜好改变王国外观的染料、金属废墟等。我们添加了生物群落和昼夜系统，要求玩家在黑暗环境下，或者在峡谷间的浓密云层中寻找闪烁的光。另外，我们还为游戏编写了比原计划中更多的故事内容。<br>
<br>
从本质上讲，(空中城市的)移动机制让我们的游戏变得不再是一款纯粹的城建游戏，而是更靠近RPG。某些时候，我甚至觉得扎克和我在设计两款不同的游戏——我会更多地考虑城建游戏的经济和平衡性，而他则更像是在做一款开放世界冒险游戏。我们曾经做了个比喻：如果将王国比作某个游戏角色，那么各种新建筑和升级就像是对角色数值的提升......《空中王国》在叙事方面的改变也反映了这一点，其主线剧情的灵感更多地来源于《塞尔达传说》，而非《冰汽时代》。<br>
<br>
整个项目刚开始的时候，我们的想法相当保守，对设计故事情节、为游戏世界增添个性持保留态度。但如今回头来看，这些恰恰是我们所做的最佳决定，让我们能够融合不同品类，用富有新鲜感的内容来激发玩家兴趣。当然，《空中王国》也帮助我们赢得了很多荣誉，包括BAFTA游戏奖项提名和IGF荣誉提名等等。<br>
<br>
考虑到《空中王国》是一家新工作室推出的首款游戏，我对我们所做的工作感到无比自豪。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">原文：<a href="https://mp.weixin.qq.com/s/-M3MGVFth_GjuON4pcckvw" target="_blank">https://mp.weixin.qq.com/s/-M3MGVFth_GjuON4pcckvw</a></font></font><br>
<font size="2"><font color="#808080">原译文<a href="https://www.gamedeveloper.com/design/deep-dive-an-economy-of-discovery-behind-the-movement-of-airborne-kingdom" target="_blank">https://www.gamedeveloper.com/de ... of-airborne-kingdom</a></font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            