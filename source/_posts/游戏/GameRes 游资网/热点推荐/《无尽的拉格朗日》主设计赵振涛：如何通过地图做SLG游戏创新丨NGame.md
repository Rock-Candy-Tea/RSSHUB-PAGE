
---
title: '《无尽的拉格朗日》主设计赵振涛：如何通过地图做SLG游戏创新丨N.Game'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202205/12/094838vsrsdbts0s0sztn7.jpg'
author: GameRes 游资网
comments: false
date: Thu, 12 May 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202205/12/094838vsrsdbts0s0sztn7.jpg'
---

<div>   
2022N.GAME网易游戏开发者峰会于「4月18日-4月21日」举办，本届峰会围绕全新主题“未来已来 The Future is Now”，共设置创意趋势场、技术驱动场、艺术打磨场以及价值探索场四个场次，邀请了20位海内外重磅嘉宾共享行业研发经验、前沿研究成果和未来发展趋势。<br>
<br>
本篇干货来自创意趋势场的嘉宾赵振涛，他是网易游戏交互设计专家，也是《无尽的拉格朗日》的主设计。<br>
<br>
<div align="center">
<img aid="1039196" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094838vsrsdbts0s0sztn7.jpg" data-original="https://di.gameres.com/attachment/forum/202205/12/094838vsrsdbts0s0sztn7.jpg" width="600" id="aimg_1039196" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094838vsrsdbts0s0sztn7.jpg" referrerpolicy="no-referrer">
</div><font color="#808080"><i>嘉宾分享实录</i></font><br>
<font color="#808080"><i>（有部分删减与调整）</i></font><br>
<br>
大家好，我是网易游戏的交互设计师——赵振涛，今天和大家聊一聊数字地图学在SLG游戏中的应用。<br>
<br>
自从六年前《率土之滨》上线后，SLG市场就逐渐出现了一个新的品类：率土LIKE。近年来，该品类涌现出了一大批优秀的作品，给用户带来丰富体验的同时，新的SLG项目想要获得成功也变得越来越难。<br>
<br>
<div align="center">
<img aid="1039197" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094839issgdtsrsbbq5ts5.png" data-original="https://di.gameres.com/attachment/forum/202205/12/094839issgdtsrsbbq5ts5.png" width="567" id="aimg_1039197" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094839issgdtsrsbbq5ts5.png" referrerpolicy="no-referrer">
</div><br>
在这样的背景下，2021年中，《无尽的拉格朗日》上线了。如果要用一个词来形容，我想或许可以称之为“创新的挑战者”。但创新的过程中，也碰到了很多问题。<br>
<br>
<strong><font color="#de5650">无极地图的核心是什么？</font></strong><br>
<br>
当时，项目主打的核心创新点之一是无极缩放地图，与市场的主流形式不同，<strong>无极缩放地图的沙盘和高层战略地图是融为一体的</strong>，这一点能给游戏体验带来大幅的提升。<br>
<br>
在项目研发中期，需求的大量更迭使地图看起来缺乏整体性的规划，部分层级的信息过载和信息缺失是比较常见的问题。<br>
<br>
当时，制作人很敏锐地看到了这个问题。于是，尽管知道这件事情非常艰难，但我们还是开始了对地图的研究和探索。<br>
<br>
那时，我们陷入了一个反思，无极地图的核心到底是什么？<br>
<br>
带着这个问题，我们开始了求索之路——去图书馆查阅信息学和地图统计学的文献资料。那些学科资源真的称得上是宝藏！就这样，这个循环过程大概持续了有半个月。<br>
<br>
有一天打车回家，我无意间发现了一个规律：定位目标地点时，地图总是会下探至底层地图，而预览路程时，则会提高至高层地图。即不同的需求对应了不同的地图层级，且是规律性的。<br>
<br>
第二天上班，我就做出了下面这张图。这个金字塔模型完整演绎了用户在无极缩放地图中的体验目标，其中的道理和打车是非常相似的。<br>
<br>
<div align="center">
<img aid="1039198" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094839szvz1039cp3mt8v9.png" data-original="https://di.gameres.com/attachment/forum/202205/12/094839szvz1039cp3mt8v9.png" width="538" id="aimg_1039198" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094839szvz1039cp3mt8v9.png" referrerpolicy="no-referrer">
</div><br>
在地图的低层级，用户目标往往是和具体的信息、行动有关，比如我家在哪个小区？在哪一栋楼？而在地图的高层级，用户则更加关注宽泛的概括信息，比如新家到公司有多少条路可以供我选择？哪些路正在堵车？堵的程度怎么样？<br>
<br>
所以，我们通过这个金字塔推导出了每一个地图层级的层级需求，进而确定了各个层级的设计表现，这样最核心的问题就迎刃而解了。<br>
<br>
那么，SLG地图模型和打车软件又有哪些不同呢？打车的需求路径是以单线需求为主的，比如搜索目的地、查看路径、打车前往。<br>
<br>
而SLG呢？SLG需求路径的核心，是多人参与的阶段性需求（探索、扩张、开发、消灭等）为主的战略模型。简单来讲，就是战略模型设计决定了战略地图的设计，可以理解为战略模型才是“爸爸”。<br>
<br>
<div align="center">
<img aid="1039199" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094839n6fcac3z1n3vrt5p.png" data-original="https://di.gameres.com/attachment/forum/202205/12/094839n6fcac3z1n3vrt5p.png" width="600" id="aimg_1039199" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094839n6fcac3z1n3vrt5p.png" referrerpolicy="no-referrer">
</div><br>
实际上它的全貌应该如下图。这张图解释了SLG战略地图、战略模型、用户体验三者之间的关系：战略地图是用户打开战略模型体验的钥匙。<br>
<br>
<div align="center">
<img aid="1039200" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094840ybjog6kkbwyoapkk.png" data-original="https://di.gameres.com/attachment/forum/202205/12/094840ybjog6kkbwyoapkk.png" width="593" id="aimg_1039200" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094840ybjog6kkbwyoapkk.png" referrerpolicy="no-referrer">
</div><br>
之前我们碰到的困难，或许正是因为没有重视用户体验路径这一关键的一环。<br>
<br>
<strong><font color="#de5650">应用上述逻辑后地图的改观</font></strong><br>
<br>
我们设定了宏伟的蓝图后，讨论地图的上限时，往往忽略了一个问题：下限是什么？用户在实际体验中，真正在意的下限到底是什么？是他们达成任务目标的速度。<br>
<br>
比如，需要在地图上找出哪些地方有更宝贵的资源时，下面这两张地图带来的体验将是完全不同的。衡量这一体验的重要标准就是达成目标的速度。<br>
<br>
<div align="center">
<img aid="1039201" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094840a1ej7and6qa1uha1.png" data-original="https://di.gameres.com/attachment/forum/202205/12/094840a1ej7and6qa1uha1.png" width="600" id="aimg_1039201" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094840a1ej7and6qa1uha1.png" referrerpolicy="no-referrer">
</div><br>
我们做过测试，后者几乎只用了前者十分之一的时间，这是两个完全不同的概念。<br>
<br>
<div align="center">
<img aid="1039202" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094840y3x0twuhl0jjmo4l.png" data-original="https://di.gameres.com/attachment/forum/202205/12/094840y3x0twuhl0jjmo4l.png" width="574" id="aimg_1039202" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094840y3x0twuhl0jjmo4l.png" referrerpolicy="no-referrer">
</div><br>
同样的，在决策战术时，哪张地图可以更快地识别单位呢？答案很明显，是后者。后者把不符合这一需求的信息进行了过滤和删减，并把支持这一需求的信息进行了视觉上的加强，得到的结果显而易见。<br>
<br>
<div align="center">
<img aid="1039203" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094840knc44hgnzkgygpkr.jpg" data-original="https://di.gameres.com/attachment/forum/202205/12/094840knc44hgnzkgygpkr.jpg" width="600" id="aimg_1039203" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094840knc44hgnzkgygpkr.jpg" referrerpolicy="no-referrer">
</div><br>
在更高层级的地图层级中，地图需求已经变更为了广义的概括信息，当指挥决策时，你一定需要这些更加全局的信息来判断局势，这时候，你并不需要知道哪里有更宝贵的资源，所以这些资源都会被过滤掉。<br>
<br>
当我们把视角拉得更大时，所展现的信息应该更加宏观，所有的信息形态都应该致力于这一目标。这里引出了一个有趣的概念：<strong>同一个信息，在不同的地图层级中，其视觉形态是在不断发生变化的。</strong><br>
<br>
这其中的根本原因就在于，信息是要服从于地图层级目标。简单来讲，就是个人要服从于集体，这样，在完成层级目标的同时，地图还能保持高度的整体性。<br>
<br>
最后，在进行整体局势判断时，单位信息或趋势信息已经不再重要，判断与周围的局势关系时，你只需要关心周围最重要的事物。<br>
<br>
但，这并不是全部。<br>
<br>
我们整合了《地图学科》《信息学科》《统计学科》等等相关资料，结合无极数字地图信息层级体验理论，对SLG数字战略地图设计理论产出了全新的论述成果——《数字地图学》。<br>
<br>
<div align="center">
<img aid="1039204" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094841hmwgdi88z8x88l72.png" data-original="https://di.gameres.com/attachment/forum/202205/12/094841hmwgdi88z8x88l72.png" width="567" id="aimg_1039204" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094841hmwgdi88z8x88l72.png" referrerpolicy="no-referrer">
</div><br>
该成果将全面支持其他相似项目，带来更多的应用价值。<br>
<br>
<div align="center">
<img aid="1039205" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094841dryvowl1ro1odi18.png" data-original="https://di.gameres.com/attachment/forum/202205/12/094841dryvowl1ro1odi18.png" width="567" id="aimg_1039205" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094841dryvowl1ro1odi18.png" referrerpolicy="no-referrer">
</div><br>
下列图是我们迭代之后的效果。<br>
<br>
<div align="center">
<img aid="1039206" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094841w42iilglwllu2a4w.png" data-original="https://di.gameres.com/attachment/forum/202205/12/094841w42iilglwllu2a4w.png" width="567" id="aimg_1039206" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094841w42iilglwllu2a4w.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">地图设计的核心决策逻辑</font></strong><br>
<br>
最后，想和大家聊一聊地图设计的核心决策逻辑。<br>
<br>
先看一件很有趣的事情：地图设计中我们会将点元素、线元素、面元素以及环境元素进行了分层设计并且重新组合。<br>
<br>
为什么要这么做？地图设计是一个非常庞大而且复杂的工程，如何降低错误率是整个生产环节中最重要的事情之一，而分层设计是可以降低设计逻辑复杂度的有效方法。<br>
<br>
<div align="center">
<img aid="1039207" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094841j556j5nlmolqysj8.png" data-original="https://di.gameres.com/attachment/forum/202205/12/094841j556j5nlmolqysj8.png" width="544" id="aimg_1039207" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094841j556j5nlmolqysj8.png" referrerpolicy="no-referrer">
</div><br>
还有很多这样的例子：我们在不断实践中逐渐摸索出一套把这些方法标准化的生产流程，将整体阶段分为了需求阶段、策略阶段、和感官阶段，而生产阶段分为地编设计、需求重要度量化环评、点线面分层设计测试和地图合成视觉调整。<br>
<br>
<div align="center">
<img aid="1039208" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094841v1z9om2yppy81z2y.png" data-original="https://di.gameres.com/attachment/forum/202205/12/094841v1z9om2yppy81z2y.png" width="600" id="aimg_1039208" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094841v1z9om2yppy81z2y.png" referrerpolicy="no-referrer">
</div><br>
每一个阶段都有严格的检验标准，环环相扣，保证每一个层级的决策都密而不疏。<br>
<br>
<strong><font color="#de5650">未来的地图</font></strong><br>
<br>
在人类文明历史的长河中，地图的身影一直伴随着文明的延续与发展。可以说，地图是人类古老文明的传输工具，也是打开未来世界的钥匙。<br>
<br>
从最古老的山海经地图，到科技发展带来的卫星遥感地图，再到数字化地图高度应用的今天，我们的生活似乎都离不开地图。<br>
<br>
<div align="center">
<img aid="1039209" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094842d4o5dt0u4zjd7a7j.png" data-original="https://di.gameres.com/attachment/forum/202205/12/094842d4o5dt0u4zjd7a7j.png" width="600" id="aimg_1039209" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094842d4o5dt0u4zjd7a7j.png" referrerpolicy="no-referrer">
</div><br>
但是，即使是今天，我们在复杂场景（比如大型的多层商场）使用地图时仍然有进步的空间，这说明地图的进化还未达到完美的状态，二维数字地图已经满足不了我们对生活的需求。<br>
<br>
那么，在未来，我们的地图能否表达出更加全面的信息呢？<br>
<br>
随着数字地图的不断发展，地图将有可能不再是单一割裂存在的工具，而是承载了完整时空信息概念的统一体。这带给我们无限的想象：未来的地图和世界是不是可以融为一体呢？<br>
<br>
<strong>未来的地图中，可以看到非常宏观的信息，同时也可以看到非常微观的具体信息，并且可以看到动态的时间信息和空间信息的组合体。</strong><br>
<br>
最近元宇宙的概念非常火，大家有没有想象过，在未来元宇宙的空间里，地图将扮演一个怎样的角色？大家不妨畅想一下。我相信，随着科技的不断进步，一个更好的能承载完整时空信息概念的统一体，很快就会呈现在我们面前。<br>
<br>
<strong><font color="#de5650">结语</font></strong><br>
<br>
最后的最后，我想分享一点自己的小感悟。<br>
<br>
依稀记得第一次看到那张“不拼搏，枉少年”的网易校招海报时，我还是一个酷爱游戏的懵懂少年，很庆幸现在的我也成为了一名游戏开发者。<br>
<br>
从小到大，一直有人问我：为什么那么喜欢玩游戏？当我在艾泽拉斯广袤的世界里探索时，只有我懂是为什么。<br>
<br>
<div align="center">
<img aid="1039210" zoomfile="https://di.gameres.com/attachment/forum/202205/12/094842gy5x56b60tb0o5yg.png" data-original="https://di.gameres.com/attachment/forum/202205/12/094842gy5x56b60tb0o5yg.png" width="600" id="aimg_1039210" inpost="1" src="https://di.gameres.com/attachment/forum/202205/12/094842gy5x56b60tb0o5yg.png" referrerpolicy="no-referrer">
</div><br>
而直到今天，我都相信，无论是游戏还是现实，无论多么困难的事情，只要有一颗勇于探索的心，就一定能找到打开世界的那一粒“沙子”。谢谢大家！<br>
<br>
  
</div>
            