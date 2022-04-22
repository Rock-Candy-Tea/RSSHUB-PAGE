
---
title: '莉莉丝游戏引擎渲染专家凯丁：从MMO到独立游戏，再到引擎技术'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202204/18/093626g61qt85cs651qiuu.png'
author: GameRes 游资网
comments: false
date: Mon, 18 Apr 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202204/18/093626g61qt85cs651qiuu.png'
---

<div>   
<div align="center">
<img aid="1036673" zoomfile="https://di.gameres.com/attachment/forum/202204/18/093626g61qt85cs651qiuu.png" data-original="https://di.gameres.com/attachment/forum/202204/18/093626g61qt85cs651qiuu.png" width="600" id="aimg_1036673" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/093626g61qt85cs651qiuu.png" referrerpolicy="no-referrer">
</div><br>
<i><font color="#808080">本文出自“莉莉丝游戏”公众号</font></i><br>
<br>
凯丁，自2010年起加入腾讯北极光工作室，担任《天涯明月刀》的客户端开发及引擎开发工作，后从北极光离开，并于2017年回到腾讯，加入NExT工作室，开始独立游戏《只只大冒险》的孵化和制作。《只只大冒险》上线后获得了IndieCade Europe 2019年观众选择奖、Indie Prize Asia 2019年最佳游戏设计以及IGF（独立游戏节）提名等众多独立游戏奖项。<br>
<br>
凯丁于2020年加入莉莉丝，担任在研项目渲染组组长一职。<br>
<br>
<strong><font color="#de5650">一、从MMO到独立游戏</font></strong><br>
<br>
<strong>了解到你从毕业起就进入游戏行业了，还记得第一份工作么？</strong><br>
<br>
当然。因为我本身就比较喜欢玩游戏和做游戏，大学毕业之后第一份工作首先加入了腾讯北极光工作室，有幸和一帮从育碧出来的骨灰级的游戏业内人士共事，参与制作了《天涯明月刀》。刚进去时做了很多天刀内的轻功、寻路等 GPP （Gameplay Programming，游戏性编程）相关的东西。由于我大学时期就在维护一个自研引擎，对游戏引擎有比较强的执念，所以又转去做引擎开发相关的工作了。<br>
<br>
现在很多同学想转引擎，但不一定有这么顺利了。<br>
<br>
我觉得当时转引擎不一定是一个很好的决定，不过确实在引擎团队学到了很多东西。其实只要在游戏开发这块足够深入，必定会触达引擎的底层，而引擎也不光只有渲染。<br>
<br>
<strong>但你后来还是选择离开这个团队，是因为什么？</strong><br>
<br>
当时换工作没有想得特别清楚吧，主要由于一些个人不成熟的原因选择了离开，之后加入新公司又发现和预期相差比较大。好在之后一个偶然的机会，《龙之谷》的团队正在搞优化相关的内容，有些内存问题没搞定。他们在线上找到我，希望我帮忙看看内存的问题是否可以优化。之后我给了一些优化建议，于是他们邀请我一起做龙之谷项目。最后封闭开发了三四个月，顺利把项目推上线，这段一开始不太符合预期的工作经历有了不错的结果。<br>
<br>
从这之后我就开始思考我对游戏的态度和追求的问题。以前我确实是一个比较执着于技术的人，后面发现，我做游戏的原始驱动力并不是因为我喜欢游戏引擎，而是我喜欢游戏本身。正好腾讯NExT那个时候在搞独立游戏，对我来说比较有吸引力，就又回到腾讯，加入了NExT工作室。<br>
<br>
<strong>所以你是因为独立游戏制作的机会再次回到腾讯的吗？</strong><br>
<br>
是的。还有个原因是当时招了很多纽约大学毕业的人，可以认识不一样的人，觉得还蛮有意思。他们肯定有在设计方面比较独特的地方。之后确实遇到了一个小朋友，跟他一起合作孵化出一个非常有意思的东西，就是《只只大冒险》的原型。<br>
<br>
当时NEXT内部有类似于Game Jam的比赛，有了想法之后我和那个小朋友合作，把想法用一个礼拜的时间做成Demo。基本玩法和机制确认后，差不多花了两三天时间，做了一个完整的关卡出来。<br>
<br>
<strong>两三天，落地能力听上去很强啊！</strong><br>
<br>
两三天能落地，是在技术验证过的基础上才可以做到的。<br>
<br>
最开始我们想做一个攀爬类的游戏，类似于《人类一败涂地》。然后我们去研究这个游戏，以及类似的独立游戏，发现有一些很好玩的技术点。比如《人类一败涂地》里的人物是软绵绵、很颓废的感觉，这个人物的表现并不是靠动画驱动，而是基于物理去驱动。有了这个前置的技术验证，才有后面的关卡快速落地。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1036674" zoomfile="https://di.gameres.com/attachment/forum/202204/18/093627paqzckshetkhpeh3.gif" data-original="https://di.gameres.com/attachment/forum/202204/18/093627paqzckshetkhpeh3.gif" width="320" id="aimg_1036674" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/093627paqzckshetkhpeh3.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《人类一败涂地》游戏画面</font></font></div><br>
<strong>所以这个idea是怎样变成《只只大冒险》的？</strong><br>
<br>
本身做物理游戏，所有的物理参数都非常考验设计师或者做Gameplay的人调手感的能力。我们也研究了其他类似的游戏，比如《Gang Beasts（萌萌小人大乱斗）》等，他们是用程序化的方式去生成动画，我们一直在尝试做类似的动画系统。之后基于这个动画系统衍生出来的玩法，做了一个类似于跳台的游戏。直到这个时候，我们的游戏角色也还是人形，有两个胳膊两个腿的那种。最后是跟一个纽大的哥们在脑暴的时候，突然之间灵光一闪，打算把手砍掉不要了，不做人型。这样设计控制起来很简单，两个摇杆就能操作，而且几乎能做任何人型生物能做的事，跟传统游戏很不一样。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1036675" zoomfile="https://di.gameres.com/attachment/forum/202204/18/093627b2u44j4h4bsuo6z9.gif" data-original="https://di.gameres.com/attachment/forum/202204/18/093627b2u44j4h4bsuo6z9.gif" width="320" id="aimg_1036675" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/093627b2u44j4h4bsuo6z9.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《只只大冒险》游戏画面</font></font></div><br>
<strong>项目正式开始制作后你主要负责什么工作内容？</strong><br>
<br>
前期主要是设计层面的工作，玩法，以及一些技术方案，就是基于物理的动画技术方案。中后期主要是程序为主了，负责一些性能框架Pipeline（管线）等，同时也包括跟美术和策划配合，怎么更好地让他们工作。<br>
<br>
<strong><font color="#de5650">二、独立游戏之美</font></strong><br>
<br>
<strong>对你来说独立游戏的魅力在哪里？</strong><br>
<br>
大部分商业游戏可能只能拓展技术边界，但独立游戏可以拓展游戏设计边界。首先独立游戏可以把控更多，而不是单纯的在某条工业化的管线下面拧螺丝。同时，独立游戏是思维的碰撞，跟他们一起工作，会了解他们的思维方式是怎样的，可以学到很多。另外，最适合做独立游戏的是T型人才，T型人才是指这个人在游戏开发的绝大部分领域都比较熟悉，且有一块领域特别地深。<br>
<br>
<strong>这段独立游戏的工作经历中有没有让你觉得特别难忘的事情？</strong><br>
<br>
整体来说都比较难忘，因为在这之前做得都是商业项目。制作《只只大冒险》之后，我感受到独立游戏和商业游戏的制作思路差异比较大——独立游戏完全是靠创意驱动，而非商业驱动。通常商业游戏制作是玩法品类+剧情内容，剧情内容是非常重要的一环，玩法可能是成熟固定的。所以《只只大冒险》的制作思路完全是反的，需要优先想好玩法机制，故事和剧情内容则没有那么重要。这点可以参考任天堂的游戏，几乎没有一点剧情上的概念，完全是纯粹的玩法，且玩法是很有意思的。<br>
<br>
<div align="center">
<img aid="1036676" zoomfile="https://di.gameres.com/attachment/forum/202204/18/093627enlyfqktj0mctrqv.png" data-original="https://di.gameres.com/attachment/forum/202204/18/093627enlyfqktj0mctrqv.png" width="590" id="aimg_1036676" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/093627enlyfqktj0mctrqv.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《只只大冒险》Tap Tap评分</font></font></div><br>
<strong>这种不同游戏在开发思路上的差异，具体在工作中是怎样体现的？</strong><br>
<br>
我觉得独立游戏的团队需要更能快速验证，这一点非常重要，不能有需求就接，按部就班地按照这个需求一步步做下去。独立游戏需要能快速地验证这个游戏到底好不好玩。当然，独立游戏开发也分阶段，我们的游戏真正开始铺量也就三四个月，前面那段时间基本上在做原型验证，思考该做什么样的关卡。<br>
<br>
<strong><font color="#de5650">三、一件很特别的事儿</font></strong><br>
<br>
<strong>是什么契机让你加入莉莉丝的？</strong><br>
<br>
当时做完《只只大冒险》，整个NExT的方向开始逐渐偏离独立游戏，我就开始看外面的机会了。我选项目有一个非常重要的因素，就是看这个团队是不是在做一件很特别的事。我对自己职业方向的选择和定位是——要么完全把关做独立游戏，要么就是这个项目组在做一件很特别的事，当初NExT的独立游戏项目就是这样吸引到我的。如今莉莉丝也一样，因为我所在的项目很特别。<br>
<br>
差不多2020年终的时候，我对莉莉丝还在了解阶段，但我一看就觉得这是个很有前景的方向。当时有好几个团队都在做类似的项目，最后选择莉莉丝是因为我在这中间挑选了个人觉得相对靠谱和优秀的团队。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1036677" zoomfile="https://di.gameres.com/attachment/forum/202204/18/093630oy30lqgk03y2snqy.png" data-original="https://di.gameres.com/attachment/forum/202204/18/093630oy30lqgk03y2snqy.png" width="600" id="aimg_1036677" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/093630oy30lqgk03y2snqy.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">所在游戏内灯光渲染截图</font></font></div><br>
<strong>你目前主要负责什么工作内容？</strong><br>
<br>
主要负责渲染。我刚加入莉莉丝时，整个项目渲染的能力严重不足，美术生产流程也有问题。很多东西不是数据驱动，流程不够自动化，需要美术理解的东西过多。所以我们团队在这一年建立起一套相对完善且有前瞻性的渲染管线，而且这个管线未来会对内开放给公司所有项目。另外，美术基于Lowpoly（低多边形，一种复古未来派风格设计）制作的生产流程也有比较大的问题，当美术要升级迭代时，就要对所有数据进行一次升级，这非常不合理。<br>
<br>
<strong>这是当时你刚加入时遇到的比较大的问题吗？</strong><br>
<br>
对，当时进组后第一件事就是升级美术的Lowpoly流程。当然，之后由于我们整体的渲染风格变化，这个流程被替换成更工业化的流程，不过依然无缝嵌在这个流程里。<br>
<br>
对我来说，跟美术、策划友好地合作是一件非常重要的事情，程序上做很多事情其实是为了避免美术或者策划出错。用一个可能不太好听的比喻——我们工作的出发点首先要默认他们会出错，所以一定要从程序上避免他们出错，这样可以最大程度地做到效率提升。<br>
<br>
<strong>你加入项目后通过拉通整个渲染管线，使得游戏整个品质有了较大的提升。能不能谈谈具体做了一些什么迭代，才有现在的呈现效果？</strong><br>
<br>
这个管线就是LitRenderPipeline（缩写LitRP,L代表 lilith , lighting），整合了很多特性的同时也考虑了兼容性，比如多光源、高质量阴影。同时我们放弃使用Lightmap（一种离线烘培到贴图的静态全局光照技术），转而使用更合适项目的Volumtric GI（一种基于球谐的全局光照技术）系统，用于提高全局光照效果，又能方便美术，甚至玩家使用。<br>
<br>
<div align="center">
<img aid="1036678" zoomfile="https://di.gameres.com/attachment/forum/202204/18/093632gyvdzyiy06f4zzvd.png" data-original="https://di.gameres.com/attachment/forum/202204/18/093632gyvdzyiy06f4zzvd.png" width="600" id="aimg_1036678" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/093632gyvdzyiy06f4zzvd.png" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1036679" zoomfile="https://di.gameres.com/attachment/forum/202204/18/093634g9j66zvvclqzcb95.png" data-original="https://di.gameres.com/attachment/forum/202204/18/093634g9j66zvvclqzcb95.png" width="600" id="aimg_1036679" inpost="1" src="https://di.gameres.com/attachment/forum/202204/18/093634g9j66zvvclqzcb95.png" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">光照效果优化前后对比图</font></font></div><br>
<strong>这个事情对你来说挑战大么？</strong><br>
<br>
整体难度不是很大，主要是要耐心地一步步推进，这其中最难的可能是做Pipeline要考虑很多兼容性。比如说之前做独立游戏，只考虑 PC 或者主机，做起来就很容易，但手游的硬件和 PC 不太一样。而且现阶段项目面向东南亚多一点，所以用户机型比较差。最开始搞LitRP时候要解决的重要问题之一是多光源。多光源的方案也是尽可能适配到OpenGL 3.0的机型。基本上海外的机器能跑起来，可能慢一点，但不至于不支持。<br>
<br>
<strong>目前你所在的项目已经开启了海外买量测试，对你来说现阶段还存在什么问题么？</strong><br>
<br>
现在渲染最大问题，主要是后续资源的统一性。对于我们这样的产品来说，资源统一非常重要。我们选用技术的时候，基本上是考虑和这个项目的合适程度，而不是去堆高级的技术。技术只有合不合适，没有所谓的高不高级。比如说Lightmap，GI方案里肯定是Lightmap效果最好。但对我们项目，尤其在之后要面向玩家这类非专业开发者的时候，Lightmap的烘培时间过长，要求其对技术的理解要比较深入，所以最后选择了Volumetric GI的方案。我们明年可能会在项目中落地的GPU Driven（一种可以通过在GPU端处理裁剪，发起绘制命令等特性来大幅减少CPU端的Drawcall数量，从而提升整体效率的技术）也是基于上面的观点， 考虑到玩家可能会往场景里面塞很多的mesh ，没办法做很好的优化，而GPU Driven能很好的解决这个问题。<br>
<br>
<strong><font color="#de5650">四、是游戏开发者，更是热爱者</font></strong><br>
<br>
<strong>听说你特别喜欢玩游戏。</strong><br>
<br>
我是“任豚”（任天堂游戏粉丝），特别喜欢任天堂的游戏，马里奥系列应该是我最喜欢的，还有《塞尔达传说：梅祖拉的面具》N64那版也特别喜欢。总的来说我比较偏爱玩法、机制比较巧妙的游戏。现在反而对3A游戏兴趣不大，不是说3A游戏品质不够好，只是在我看来有些叙事或者场面做的很宏大很漂亮的游戏，我会想为什么不干脆直接拍电影？玩起来有点累。<br>
<br>
我打游戏的历史也比较长，从GBA（GAME BOY ADVANCE，是任天堂公司于2001年3月21日发售的第二代便携式游戏机）时期就爱上了游戏，那时候手机还是黑白的，突然看到一个有彩色画面的机器，画面还特别棒，就被吸引了。<br>
<br>
<strong>聊下来我发现你对自己的定位其实并不是一名技术人员，而是游戏制作人，可以这么说吗？</strong><br>
<br>
可以这么说。我认为光追求技术没用，技术最终也要有一个落地的地方。我自己首先非常热爱游戏，同时也喜欢钻研技术，但技术最终要在游戏里落地的话不能只钻研技术，其他方面也要懂。所以我对组员的要求是要 T 要 P 还要 A（技术、策划、美术）。别人提过来的需求，最好自己先过一遍，不能拿起来就做。<br>
<br>
我认为优秀的技术人员也是一个很好的产品经理。首先有些技术人员可能本身就面向用户，比如有些做Gameplay很棒的程序员，最后的路径是成为制作人。即便有些技术岗位不直接面向用户，而是面向组内，那么组内的成员也一样是你的用户。所以产品意识是衡量一个技术人员综合能力非常重要的一环。<br>
<br>
<strong>感觉你的项目经历都挺顺利的，有没有什么对你来说真正很困难的事情？</strong><br>
<br>
对我来说真正困难的，可能是学会如何与不同的人交流，如何去主动推动项目，如何转变自己对引擎的执念，如何让团队作战而不是单兵作战。这些都是在观念发生变化，合作对象发生变化，职位发生变化时会遇到的困难，对我来说这些困难比实实在在遇到技术问题要难处理许多。<br>
<br>
<strong>你平时会做哪些个人提升？</strong><br>
<br>
游戏设计方面我会看一些推特上各种独立游戏的设计，会多接触一些游戏， Steam上的独立游戏基本都会玩。引擎方面会看看GDC（Game Developers Conference，游戏开发者大会）的视频以及一些论文。<br>
<br>
其实我之前还维护了一个小小的玩具引擎，从大学开始就一直在做，完全是自己开发。早期没有什么引擎可以参考，尤其是开源的。当时开源引擎好像只有Ogre（一种游戏制作引擎），我就参考着它是怎么做的，然后往里面加一些自己的东西。工作后发现之前写的东西还比较青涩，很多设计理念很落后，又持续做了改进。<br>
<br>
<strong>怎么会想到要自己去做一个引擎的？</strong><br>
<br>
我和编程的缘分其实开始的挺早的，初中机缘巧合，在老师的推荐下去了一个程序竞赛，那时候就开始接触编程。加上我也挺喜欢玩游戏，当时就觉得游戏好神奇，它能把那些画面变成我能操控着去动的。之后高中我开始萌生要做游戏的想法，进大学后顺理成章选了计算机专业。那时候就给自己定好了方向——我以后一定要做游戏！所以我做引擎也是为了做游戏，当时还用这个小引擎做了个小游戏上线。<br>
<br>
<strong>最后，对各位想做引擎，做技术的游戏热爱者们，有没有什么想说的话？</strong><br>
<br>
我觉得入行前得问一下自己——到底是想做游戏还是想做技术？做游戏和做技术给的建议是不同的方向。整体来说，新人做Gameplay也是有好处的，不要一开始就奔着去搞引擎、搞渲染，尤其是喜欢游戏的人。<br>
<br>
我给自己画了个圈，这个圈是游戏领域的知识圈，如果我想做游戏，就必须把这个知识圈给扩大，而技术是我的出发点。以技术为原点，慢慢的发现我还得了解更多的技术，还得了解美术想的是什么，还得了解策划，这些层面的知识都要去一一去扩宽。不过最重要的还是得知道自己的目标是什么，想做牛逼的技术还是牛逼的游戏产品。知道自己喜欢什么，想追求什么，真正热爱的是什么，才能少走弯路。<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：莉莉丝游戏</font></font><br>
<br>
  
</div>
            