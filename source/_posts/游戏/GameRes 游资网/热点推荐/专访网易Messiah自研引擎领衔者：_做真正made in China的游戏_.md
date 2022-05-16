
---
title: '专访网易Messiah自研引擎领衔者：_做真正made in China的游戏_'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202205/13/142840yammymssmlh4fphw.jpg'
author: GameRes 游资网
comments: false
date: Fri, 13 May 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202205/13/142840yammymssmlh4fphw.jpg'
---

<div>   
<font size="2"><font color="#808080">本文转载自“网易游戏互娱校园招聘”</font></font><br>
<br>
近期，游戏引擎或将成为“下一个时代全世界最重要的底层工具之一”、“大国科技竞争另外一个关键技术”的说法一直保持着比较高的热度，有人摇旗高呼“务必要抓住这个技术突破口”，也有人沮丧发言，认定“中国无自研引擎”，或“中国自研引擎实力太弱”。<br>
<br>
本篇专访邀请到网易Messiah自研引擎领衔者&网易互娱首席游戏软件设计专家赵钰琨，希望通过对几个核心命题的讨论与交流，尝试对“自研游戏引擎”这回事做初步探讨：<br>
<br>
既然市面上已经有好几款相对比较成熟的、大家觉得“好用”的商用引擎了，网易为什么要“吃力不讨好”再去做自研游戏引擎？<br>
<br>
数十年如一日地“吃力不讨好”，意义在哪里？<br>
<br>
网易的自研引擎目前是怎么样的技术水平？未来何去何从？<br>
<br>
<div align="center">
<img aid="1039520" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142840yammymssmlh4fphw.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142840yammymssmlh4fphw.jpg" width="600" id="aimg_1039520" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142840yammymssmlh4fphw.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">2020年，网易自研引擎Messiah推出世界游戏业领先的全平台动态全局光方案，并已获得专利</font></font></div><br>
以下是经过整理的采访内容：<br>
<br>
<strong><font color="#de5650">一、研发综合实力的强横，与巨大的技术沉淀</font></strong><br>
<br>
<strong>您有看到过最近讨论度还挺高的“游戏引擎或将成为‘下一个时代全世界最重要的底层工具之一’、‘大国科技竞争另外一个关键技术’”的说法吗？</strong><br>
<br>
<strong>赵钰琨：</strong>有看到过。从我自身的经历和经验来看，游戏引擎不单只是代表了我们单纯做游戏产品的工业化实力，更重要的是，游戏工业是整个影视工业和互联网服务业结合的结晶，影视工业代表了离线计算的品质，互联网服务代表了即时计算，要在实时的苛刻条件下提供无限接近于影视高质量的视觉听觉综合体验、还是交互式的，这样对技术的要求是非常高标准的。<br>
<br>
<strong>能创造和研发出游戏引擎，代表着研发综合实力的强横，也同时意味着有巨大的技术沉淀。</strong><br>
<br>
往近说工业化4.0有很多需要实时模拟仿真进行虚拟化深度学习的游戏引擎运用场合，比如自动驾驶技术用虚拟世界进行学习，可以在游戏引擎中同时模拟上百万量车的自动驾驶状况，而AI在这个情境下进行学习效率更高，还不需要真实的汽车和道路。往远处说，扎克伯格曾经推崇一本科幻小说《安德的游戏》，内容讲的是未来人类用游戏训练青少年控制和外星人战斗的飞船，最终打败虫族的故事，虽然听起来很中二，但未来用AI或者游戏模拟进行战斗及国防研发的可能性巨大。而游戏引擎的研发提供了这种基础工业的可能性和预先的技术储备，是必不可少的。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1039521" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142840ie8b8vbf6qhlse6v.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142840ie8b8vbf6qhlse6v.jpg" width="600" id="aimg_1039521" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142840ie8b8vbf6qhlse6v.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">（图片：网络）</font></font></div><br>
所以围绕着游戏引擎研发所需要的图形、物理、网络、AI、软件硬件等一切技术，以及这些技术能无缝相容在一个框架内进行合作、融为一体，这种技术沉淀对未来科技竞争是非常关键的。<br>
<br>
这些技术是核心，是命脉，不能寄望于别人、不能买、不能借、不能依托于开源或者授权，更不能被别人卡脖子，要牢牢掌握在我们自己的手里，要能彻底地为我们自己所用，以发挥这些技术最大的威力。<br>
<br>
<strong>坚持要做自研，这种想法是因为什么契机产生的呢？</strong><br>
<br>
<strong>赵钰琨：</strong>我最早在学习编程的时候其实有这样的一个感觉，前面有很多非常聪明的、非常伟大的计算机科学家，他们发明了各种算法、写出了各种很牛的软件。刚开始学习做离线渲染的时候，我接触到了比如Ed Catmull发明的Stochastic Sampling算法，以及他在Pixar研发的PhotoRealistic RenderMan这个渲染器，他们写得非常棒。当时我问了自己一个问题：大家都是人，为什么别人能写出来我们写不出来？我很强烈地觉得不服气，既然人家可以做得那么好，我们也是可以写出（优秀的软件）来的。所以我整个大学阶段都在做一件事，就是尝试写一个能和RenderMan一较高下的离线渲染器。<br>
<br>
<div align="center">
<img aid="1039522" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142840sudur97jj6e9d5r6.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142840sudur97jj6e9d5r6.jpg" width="600" id="aimg_1039522" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142840sudur97jj6e9d5r6.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">（RenderMan渲染效果图 ｜ 图片：网络）</font></font></div><br>
后来我到了网易游戏，我开始接触游戏引擎。在立项做这个自研引擎的时候，我们的想法就是，人家3A游戏能做到跨平台的、全平台的、顶级的引擎，我们也都可以做到；人家能够做到实时的、全局光实时的动态全局光，我们也都能做到；而且我们要做得更好、在更短的时间内做得比他们好。<br>
<br>
<div align="center">
<img aid="1039523" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142841bliro6k6anor8k03.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142841bliro6k6anor8k03.jpg" width="600" id="aimg_1039523" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142841bliro6k6anor8k03.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1039524" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142841kfhpl444zhlzhp4k.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142841kfhpl444zhlzhp4k.jpg" width="600" id="aimg_1039524" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142841kfhpl444zhlzhp4k.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1039525" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142841jvpzotox523vnziu.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142841jvpzotox523vnziu.jpg" width="600" id="aimg_1039525" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142841jvpzotox523vnziu.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>简单来说就是有点“不认输”。</strong><br>
<br>
<strong>赵钰琨：</strong>对，是这个意思没有错。我自己实际上也是一直在贯彻这个观点，去推动网易的技术发展。在这个开发的过程里面我觉得比较有意思的是，我们不断地去挑战，不断地去努力，希望可以和那些已经站在顶尖的人们站在一起。<br>
<br>
我们从用一个非常简陋的demo在饭桌上用iPad mini 2给丁老板演示、直到现在能够支持上十数款产品在研发运营、乃至有《暗黑破坏神：不朽》这样的世界顶级的、史诗级的项目采用的自研引擎，我一直贯彻Messiah每一行代码都是我们自己写出来的，每一个功能都是我们亲手制作研发打磨出来的。我们的这种不服气、不认输贯穿了整个研发过程的始终。<br>
<br>
<div align="center">
<img aid="1039526" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142841sa9abj9jv9b9agsv.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142841sa9abj9jv9b9agsv.jpg" width="600" id="aimg_1039526" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142841sa9abj9jv9b9agsv.jpg" referrerpolicy="no-referrer">
</div><br>
我希望同学们能加入到我们这样的一个企业，在这样的一种研发氛围里面，也能做出自己的东西，通过自己的能力去敢挑战世界顶尖水平。<br>
<br>
世界顶尖不是说要挂在嘴巴上，而是要做出来。<br>
<br>
就网易自身而言，包括我们之前的《一梦江湖》《荒野行动》《王牌竞速》，以及现在已经即将全球上线的《暗黑破坏神：不朽》，都已经能够和世界顶尖的产品站在一起，依靠的也是我们自己一个字符一个字符敲出来的代码。<br>
<br>
<div align="center">
<img aid="1039527" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142842itk9laa993ae9bqd.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142842itk9laa993ae9bqd.jpg" width="600" id="aimg_1039527" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142842itk9laa993ae9bqd.jpg" referrerpolicy="no-referrer">
</div><br>
大概在2017年开始，我们陆陆续续有非常多的机会和各种世界顶尖研发团队进行交流，甚至还有机会和业界传奇游戏历史销量前三制作人、第一个提出Deferred Shading的大牛、第一个提出Cascade Shadow Map的大牛这样站在游戏世界之巅的人进行对话，我自己感触良多。<br>
<br>
跟他们交流，给他们看到我们的技术，获得他们的尊重、认可和赞许，他们还主动邀请我们进行更多更深入的沟通，甚至还有顶尖国外的制作人三番四次地想获得使用我们引擎的授权来进行新游戏的研发，我深切地感受到我们的技术真的开始摸到了世界顶尖水平。<br>
<br>
<div align="center">
<img aid="1039528" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142843il99hvhggzavhfdh.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142843il99hvhggzavhfdh.jpg" width="464" id="aimg_1039528" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142843il99hvhggzavhfdh.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1039529" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142843kugncl0g05ct1f15.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142843kugncl0g05ct1f15.jpg" width="462" id="aimg_1039529" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142843kugncl0g05ct1f15.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">新时代的3D手游引擎Messiah带来《一梦江湖》丰富而自由的捏脸3.0时代</font></font></div><br>
<strong><font color="#de5650">二、“如果自己不革自己的命，别人就会来革你的命”</font></strong><br>
<br>
<strong>听说Messiah每半年就要做一次大的系统重构，其中会涉及到不小的工作量吧？</strong><br>
<br>
<strong>赵钰琨：</strong>自2014年以来，至今Messiah经历了8年的持续研发迭代，成为一个横跨移动、桌面、主机的全平台次世代游戏引擎，至2022年完成了8款大型产品的研发工作。目前正在研发的产品达数十款，涵盖MMO、FPS、TPS、ARPG、赛车、体育竞技等多个游戏品类，引擎支持iOS、macOS、安卓、PC、Linux、PS4/PS5、Switch、XBox等几乎所有的游戏平台。<br>
<br>
架构与效率一直贯穿于整个引擎开发工作，我们相信良好的架构能提供足够高的执行效率以及良好的扩展伸缩性。<strong>我们深信——“如果自己不革自己的命，别人就会来革你的命”，所以我们一直贯彻一个开发规则，每半年左右必须全面更新一个大型子系统框架，架构是引擎发展的命根子。</strong><br>
<br>
<div align="center">
<img aid="1039530" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142844epukjaajy10d4gkv.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142844epukjaajy10d4gkv.jpg" width="600" id="aimg_1039530" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142844epukjaajy10d4gkv.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>那这几年里，Messiah大概都经历过哪些迭代变化呢？</strong><br>
<br>
<strong>赵钰琨：</strong>大概2007年，在我最早刚刚开始构思和设计Messiah雏形的时候，PC业界正开始面对摩尔定律的“失效”，即芯片频率的提升遇到瓶颈，Intel开始向多核心CPU发展，在超线程技术加持下并行计算日益提上议程。<br>
<br>
我在刚刚加入网易的时候有幸参与了当时的一个XBox 360开发课程，其中一个很有趣的点就是360的CPU在安排计算指令的时候需要“凑”一对儿一对儿的指令，以加大并行度，否则单条计算指令会降低PowerPC芯片的效率。这个是我之前没接触过的领域，让我大开眼界，也给了我灵感。后来我看到x86平台也开始有这样的趋势，我深刻的感受到多核心计算一定是未来的重中之重，于是我理想中的游戏引擎的样子，应该是一个天生并行的架构，应该是一个像现实世界一样多线程的架构，而不是传统游戏引擎——顺序逐一更新计算——的架构。<br>
<br>
<strong>为什么是多线程？</strong><br>
<br>
<strong>赵钰琨：</strong>Messiah刚研发的时候是2013年左右，当时是移动游戏刚刚开始爆红的时候，所有人都开始关注移动游戏，所以大家都觉得要针对当时的移动芯片进行开发，要根据当时的移动平台来设计。但是我断定移动平台必将走过PC平台的每一步，将会复刻PC平台的发展，包括CPU和GPU，他们将在很短的时间内变得一模一样。所以我坚持Messiah的移动平台版本也需要做多线程，多核心优化。在我们多线程刚出来的时候，不少人嘲讽，说我们不懂移动平台，说Messiah的多线程架构一定会死得很难看。后来恰恰相反，更短时间内更高效率的计算、以及多核心分摊计算成本反而能降低核心频率从而降低功耗，Messiah在移动平台上出色的效率及功耗控制赢得了很多项目的良好口碑。<br>
<br>
<div align="center">
<img aid="1039531" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142846qh9ri896stfphrz8.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142846qh9ri896stfphrz8.jpg" width="600" id="aimg_1039531" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142846qh9ri896stfphrz8.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《一梦江湖》： 网易Messiah引擎大胆尝试只在主机与PC端游用到的渲染技术</font></font></div><br>
在2017年我们成功推出了《天下手游》和《楚留香》（后更名为《一梦江湖》）以后，Messiah的架构迭代并没有停止，我认为我们需要更进一步的推动架构发展，需要为5年甚至10年以后的产品打基础做准备，于是我们又进一步的重构了整个多线程体系；2018年我们在支持了《荒野行动》这种可以做到无限大世界的游戏架构以后，重构了整个渲染管线，引入了Frame Graph系统——比Unreal引入这套系统提早了两年；2020年我们又再次大规模重构了多线程渲染系统，在PC上效率提高了10倍；2021年我们推出了Frame Graph 2.0；2022年我们迭代了多线程架构专门优化了大小核心调度，等等等等。<br>
<br>
<strong>技术难度上，挑战大吗？</strong><br>
<br>
<strong>赵钰琨：</strong>这些不断一次又一次的近乎全面的重写，非常困难，也很痛苦。指出别人的不足、纠正别人的错误是很容易的，很轻松的；推翻曾经的自己、否定曾经的自我是最困难，也是最痛苦的。但是我们就在这些一次又一次的自我否定中，伴随着引擎技术的成长，我们引擎研发人员的知识、技术、经验、得到了一次又一次的提高和升华。不断的挑战和战胜自己，是世界上最有意思的事情。现在我觉得战胜别人没什么值得高兴，战胜自己才是最值得高兴。<br>
<br>
而在实际的重构工作中最最最痛苦的就是历史遗留问题，但是我们一直坚持务必解决历史遗留问题，不做任何妥协，一定要妥善处理。至今我们所有的产品都能顺利的升级到引擎的最新版本，包括最早采用Messiah引擎的《天下手游》。而且我们承诺绝不放弃任何一款产品，都一直支持他们的升级。给产品灌注生命力也是维持引擎成长的最大动力。若是产品不再升级引擎了，就证明引擎失去了和产品同步发展的优势。<br>
<br>
<strong>团队内部怎么看待这样的架构迭代？</strong><br>
<br>
赵钰琨：其实刚刚有提到，我期待的工作状态，绝不是一个自己认为“还可以”的状态，当然，这也是很多做技术的同学都天然会有的追求。如果你选择程序员作为你的终身职业，然后进入到这个行业，以及进入到网易这样的一家以自主研发为主的公司，我认为每一个同学更需要关注自己的一些能力，比如说学习能力。学习是非常重要的，它会贯穿你的整个职业生涯。我们不只是需要学习像学校里面的一些理论知识，更重要的是要学习怎么样去做一个产品，怎么样去让一项技术落地，然后怎么样去接触新的东西，<strong>因为技术本身就是不断在更新和迭代的。</strong>然后去把这些技术运用到我们的产品上面去产生具体的价值，然后让所有人去享受到、玩到这些技术。<br>
<br>
<div align="center">
<img aid="1039532" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142847t3m643fld4dyw465.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142847t3m643fld4dyw465.jpg" width="600" id="aimg_1039532" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142847t3m643fld4dyw465.jpg" referrerpolicy="no-referrer">
</div><br>
同时在研发Messiah的过程里，我体会到最大的感悟并不是单纯的技术，而是研发引擎这个过程，最重要的，并不是仅仅产出一个产品、一堆代码，最重要的是这个研发过程培养了一个团队、一系列技术专家、沉淀下来了一个良好的技术研发环境氛围。<br>
<br>
随着引擎研发成长的人，是网易游戏引擎团队中最大的硕果，人比代码重要、比产品重要，有人才有这些可能性，代码自己不会成长，人会；代码不会自己变强，人会；代码不会自己进化，人只要给与足够的空间和机遇，给养分，给时间，给试错的机会，给动力，给回报，成长的空间是没有止境的。我们研发引擎一开始的初衷是为了解决技术短缺，后来逐步的变成解决人才短缺，再后来变成了我们培养了一个正向循环，一方面引擎的研发环境促进人成长、变强，另一方面人才变强了又促进迭代原有的引擎技术，让引擎变得更先进。<br>
<br>
<div align="center">
<img aid="1039533" zoomfile="https://di.gameres.com/attachment/forum/202205/13/142847lmvp9dizg1madpvc.jpg" data-original="https://di.gameres.com/attachment/forum/202205/13/142847lmvp9dizg1madpvc.jpg" width="600" id="aimg_1039533" inpost="1" src="https://di.gameres.com/attachment/forum/202205/13/142847lmvp9dizg1madpvc.jpg" referrerpolicy="no-referrer">
</div><br>
所以团队内部能达成这个迭代的共识，大家都明白迭代是引擎的成长过程，也是自己的成长过程。不断的推翻和重建，让代码更强大、让技术更先进、也让自己进步。不是一日复一日的重复劳动，而是不断推翻残旧的自我。当然我们也经历了一个过程，一开始痛苦、烦躁，明明做好了的东西，还要再来一次，然后慢慢接受，也主动去思考哪里做得不够、再推翻、再重构——变得更好。<br>
<br>
<strong><font color="#de5650">三、做真正made in China的中国游戏</font></strong><br>
<br>
<strong>你自己会怎么定位Messiah这款引擎？</strong><br>
<br>
<strong>赵钰琨：</strong>可以说，Messiah是网易在技术突破上第一次野心勃勃的巨大尝试，也是国内软件研发历史上一个巨大复杂软件成功研发的里程碑。<br>
<br>
游戏引擎的复杂度、耦合度、广度、深度，都决定了它是除了操作系统以外，其中一种最复杂的软件。其对执行效率有极端苛刻的要求，对前沿技术的落地注重、对产品直接支持面向用户、同时也承接整个产业的工业化，同时面对用户和生产者，既要运行时效率非凡也要生产时易用耐用。一方面既要达到宣传片里的顶级画面、也要在伸缩性上考虑极广泛的用户设备宽度。我认为这是极其苛刻的研发指标，仅亚于带图形用户界面的操作系统。<br>
<br>
这是第一次网易从零开始规划一个面向十年甚至二十年后的引擎。在规划的时候就提出需要从最底层开始解决根本性技术难题，并且贯彻始终，一直没有偏差的执行研发战略的引擎研发项目。我们在第一行代码写下来的时候就坚持跨平台、原生多线程、并发执行、支持尽可能多的图形API和操作系统、向主机看齐向移动兼容，务求一次研发所有平台都能跑起来一模一样。这种理念现在看起来是理所当然，而我最早构思Messiah的时候是2007年，成立项目的时候是2014年，当时这是大逆不道的破天荒的想法。很幸运我们坚持并一路走下来了，而且能做得到。今年是2022年，8年过去了这个规划看起来还刚刚能满足目前的需求，证明我们8年前的想象力也仅仅足够支撑至今，所以接下来我们需要更大胆、更具有想象力的规划，去憧憬下一个8年后的未来。<br>
<br>
同时Messiah也是一个非常极端的敏捷软件开发的产物，在研发的同时就开始供应给在研项目，相互促进。我们坚持精兵简政策略，坚持只采用极少量的顶尖研发人员、进行极高的迭代效率、以及非常迅速的响应，在很短的时间内支持了大量项目的开发、上线、运营。依靠的是相信技术、相信科学，一切问题用技术手段解决，尽量不留技术空白，历史问题当下解决。快速开发，快速迭代，快速验证，天下武功，唯快不破。<br>
<br>
<strong>在你看来，Messiah和市面上的商业引擎最大的区别体现在哪里呢？</strong><br>
<br>
<strong>赵钰琨：</strong>们和商业引擎是有非常大的不同的，首要的便是，自研引擎专注对内，所以我们很偏执地追求执行效率，只有执行效率和能耗指标远高于商业引擎，才能抵御体量庞大的商业引擎。俗话说船小好掉头，我们在采纳新的技术架构上、以及适应新的硬件上，响应速度远超商业引擎。在一些核心问题的修改上，我们的决策速度也远比商业引擎快、准、狠，所以Messiah最大的特点是，执行快、响应快、变化快。<br>
<br>
当然，虽然Messiah研发即将走进第九个年头，已经从一个简陋的demo飞速成长为有能力支撑世界级品质、全平台发行的大型游戏开发的成熟自研引擎，但我们也承认，Messiah至今依然有大量的不足，我们每天仍然面对很多反馈、很多珍贵的制作需求。我们团队中的每一个成员都正在努力改进，努力进步，<strong>希望有一天，属于我们自己的引擎能够矗立在世界游戏技术之巅，大家能用上世界最顶尖的技术——我们自己开发出来的技术。</strong><br>
<br>
  
</div>
            