
---
title: '《二之国：交错世界》如何挑战MMORPG手游的极限'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202207/19/084942n5ld09zqj35lfafy.jpg'
author: GameRes 游资网
comments: false
date: Tue, 19 Jul 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202207/19/084942n5ld09zqj35lfafy.jpg'
---

<div>   
<i><font color="#808080">以下文章来源于虚幻引擎 ，作者Jimmy Thang</font></i><br>
<br>
由Netmarble与Level-5合作开发的《二之国：交错世界》是一款挑战手游极限的MMORPG游戏。它业界领先的图像以著名动画公司吉卜力工作室的美术作品为基础，迷人的角色设计和汇聚着各种生物群落的多元化环境使它独具特色，再加上一流的游戏动画，最终创造出了一种观赏顶级动漫般的体验。<br>
<br>
我们采访了Netmarble团队，了解他们如何完成这些惊人的成就。他们详细阐述了Sequencer、动画蓝图、材质编辑器、实时代码编写等虚幻引擎工具如何助力游戏开发。团队还分享了他们关于故事型MMORPG体验的设计想法，深入探讨了为游戏实现流畅网络代码的方法。<br>
<br>
<strong><font color="#de5650">能否向不熟悉《二之国：交错世界》的玩家们介绍一下这款游戏？</font></strong><br>
<br>
<strong>创意总监Yong Tack Oh：</strong>《二之国：交错世界》以Level-5和吉卜力工作室联合推出的《二之国》游戏系列为基础。这是一款MMORPG游戏，众多玩家可以进入奇幻而美丽的《二之国》世界展开冒险。不仅如此，他们还能在游戏内外创造难忘的体验。<br>
<br>
<strong><font color="#de5650">团队在制作这个项目时受到了哪些作品的影响？</font></strong><br>
<br>
<strong>Oh：</strong>吉卜力工作室精彩的动画电影受到了娱乐行业中几乎所有业内人士的认可。作为游戏开发者，能够在吉卜力工作室艺术瑰宝的基础上制作游戏，对我们来说是一项巨大的荣誉。除此之外，在项目制作过程中，与Level-5间的积极合作也让我们激动不已。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046627" zoomfile="https://di.gameres.com/attachment/forum/202207/19/084942n5ld09zqj35lfafy.jpg" data-original="https://di.gameres.com/attachment/forum/202207/19/084942n5ld09zqj35lfafy.jpg" width="600" id="aimg_1046627" inpost="1" src="https://di.gameres.com/attachment/forum/202207/19/084942n5ld09zqj35lfafy.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图片由Netmarble提供</font></font></div><br>
<strong><font color="#de5650">这款游戏完美利用了吉卜力工作室备受赞誉的美术风格，创造出了迄今为止公认最漂亮的一款手游。能否谈谈你们在游戏视觉方面所做的出色工作？</font></strong><br>
<br>
<strong>美术总监Nam Ho Choi：</strong>我们的目标是描绘一个温暖、多彩的美丽世界，置身其中的玩家可以尽情期待激动人心的事情发生。我们还重点为角色创造了动态面部表情和独特个性，让他们传达出一种动漫的感觉。为了实现这一目标，我们不仅仅是将这个项目当成一款游戏，更是将它看作一部动画电影，在整个项目中，从设定到角色，我们的重点都是表达出生动性。<br>
<br>
<strong>高级角色概念美术师Hwan Kwon：</strong>对视觉画面的完善本身就属于创作过程的一环。我们各个领域的专家都在竭力设计、渲染、修改和创造我们想象中的场景。在定稿之前，我们会反思这是否是我们能交付的最好工作。这是一项艰苦的工作，但我相信，我们的努力带来了不错的成果。<br>
<br>
<strong><font color="#de5650">凭借富有表现力的动作和流畅的剧情画面，《交错世界》的动画堪称一部世界顶级的动漫。能否谈谈这方面的工作？</font></strong><br>
<br>
<strong>高级动画美术师Ki Beom Lee：</strong>为了让角色清楚地表达情绪，我们将与角色个性相符的面部表情构建到了姿势资产中，并在剧情画面和对话中使用，以确保质量稳定。<br>
<br>
在制作剧情画面时，我们使用了虚幻引擎的Sequencer和动画蓝图。在这些工具的基础上，我们还使用了游戏内动画序列以及骨骼控制点等其他工具，编辑各种基本资源。这有助于我们集中精力为剧情画面制作专门的动画。<br>
<br>
<strong>视频制作经理Kyo Jin Lee：</strong>为了提高各种次级动画（动态动画、拖尾等）的质量，我们会使用骨骼控制节点纠正制作过程中出现的动画间断。此外，它也可以用来为其他各种对象添加丰富的次级动画。<br>
<br>
我们试着通过检查策划团队提供的关键点，强化故事剧情画面的效果。我们将已完成场景的感觉纳入考虑范围，通过恰当的构图剪裁和引发情感共鸣的布景创造出了适合故事的场景。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046628" zoomfile="https://di.gameres.com/attachment/forum/202207/19/084942r0mgbytsjsqylmtn.jpg" data-original="https://di.gameres.com/attachment/forum/202207/19/084942r0mgbytsjsqylmtn.jpg" width="600" id="aimg_1046628" inpost="1" src="https://di.gameres.com/attachment/forum/202207/19/084942r0mgbytsjsqylmtn.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图片由Netmarble提供</font></font></div><br>
<strong><font color="#de5650">从宁静的草原到白雪覆盖的田野，精致多样的地形是游戏的一大特色。团队是如何为游戏设计各种环境的？</font></strong><br>
<br>
<strong>高级游戏概念设计师Myung Sin Koo：</strong>MMORPG手游的本质导致展示地形规模成了一件难事。为了解决这个问题，我们将接景或视点空间与游戏空间分开来了。这样一来，我们不再关注小型资产的质量，而是将焦点放在了环境元素、关卡和更广阔领域的轮廓线上。<br>
<br>
我们能够使用虚幻引擎提供的各种光照效果和雾化效果构建丰富多彩的环境，我们还试着为每块地域设置不同的光源主色，突出显示不同的地点。我们花了大量精力平衡饱和度和亮度，避免使玩家感到不适应。<br>
<br>
我们可以在虚幻引擎中实时观察这些细致的任务，使这个过程更加直观和高效。<br>
<br>
<strong><font color="#de5650">《交错世界》凭借有趣而直观的玩法广受好评。能否谈谈这方面的设计理念？</font></strong><br>
<br>
<strong>Oh：</strong>MMORPG游戏在设计上通常会优先考虑玩家在共同游玩时的有趣体验——这不利于故事元素塑造世界。<br>
<br>
尽管《二之国：交错世界》是以MMORPG的形式开发的，但我们仍希望像传统JRPG游戏那样，讲述一个完整的故事。<br>
<br>
虽然最近大多数MMORPG游戏会鼓励玩家建立竞争型社会关系，但我们的系统和内容将促进玩家合作。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046629" zoomfile="https://di.gameres.com/attachment/forum/202207/19/084943jlrr4g840lgbi404.jpg" data-original="https://di.gameres.com/attachment/forum/202207/19/084943jlrr4g840lgbi404.jpg" width="600" id="aimg_1046629" inpost="1" src="https://di.gameres.com/attachment/forum/202207/19/084943jlrr4g840lgbi404.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图片由Netmarble提供</font></font></div><br>
<strong><font color="#de5650">能否详细介绍一下游戏战斗系统的设计方法？</font></strong><br>
<br>
<strong>Oh：</strong>我们在开发战斗系统时，最关注的是打击感。由于MMORPG游戏必须接收服务器上的决策结果，然后在客户端上表现出来，所以在信息交换时，不可避免地存在时间差。为了在这种环境中创造准确的动作战斗，我们使用了我们在之前作品中开发的各种技术。此外，我们还采用了非针对性战斗模式，提供类似于砍杀游戏的畅快感。<br>
<br>
<strong><font color="#de5650">《二之国：交错世界》作为该系列的新作，允许玩家选择自己的职业，如巫师、流氓和技师等。能否谈谈你们是如何设计它们的？</font></strong><br>
<br>
<strong>Oh：</strong>在设计《二之国：交错世界》的五种职业时，我们借鉴了《二之国：亡灵之国》的主角为参考。我们希望每位角色都有独特的外貌和个性。《二之国：交错世界》中更具挑战性的地方是，职业并没有特定的责任（如充当肉盾或奶妈）。这是因为，我们不希望那些被《二之国：交错世界》画面所吸引的休闲玩家由于选择的职业与自己的游戏风格不相符而感到失落。<br>
<br>
我们特别关注的一点是，要让玩家作为行动的代理人沉浸在游戏中，而不是充当一名观察者。例如，在玩这款游戏的时候，你会发现主要角色的对话非常有限。如果主要角色的言行违背了玩家意愿，玩家的角色就会转变为观察者，妨碍游戏的沉浸感。<br>
<br>
然而，主要角色台词说得太少，将严重限制前面强调的JRPG故事的发展。为了解决这个问题，我们需要有人代表玩家引导故事，于是，迷人的角色库乌就此诞生。我们本可以做出妥协，跳过这方面，但我们没有选择这样做。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046630" zoomfile="https://di.gameres.com/attachment/forum/202207/19/084943fe24psp22bfenctf.jpg" data-original="https://di.gameres.com/attachment/forum/202207/19/084943fe24psp22bfenctf.jpg" width="600" id="aimg_1046630" inpost="1" src="https://di.gameres.com/attachment/forum/202207/19/084943fe24psp22bfenctf.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图片由Netmarble提供</font></font></div><br>
<strong><font color="#de5650">除了各种职业外，《交错世界》还提供了强大的角色定制选项，允许玩家调整身高、服装、发型，甚至是单只眼睛的颜色。能否谈谈这方面工作？</font></strong><br>
<br>
<strong>高级3D建模经理Kyung Hwan Han：</strong>我们通过调整皮肤绑定所使用骨骼的比例，实现了对体型的定制。此外，我们还增加了各种头发资产，为玩家提供更多选择。虹膜和服装的颜色可以改变，特定的UV部分可以被染成单色。各种纹理遮罩贴图中也添加了可染色材质，这样就能够使用预先确定的调色板颜色为它们染色了。<br>
<br>
<strong><font color="#de5650">虚幻引擎为什么适合用于制作这款游戏？</font></strong><br>
<br>
<strong>首席客户端程序员Tae Woo Kim：</strong>《二之国》的渲染使用了传统的卡通着色器。此外，它所呈现的感觉依赖于吉卜力风格的暖调视觉画面。<br>
<br>
虚幻引擎的材质编辑器工具非常强大，具有直观的用户界面，能够让我们快速迭代，并更快地实现当前视觉目标。<br>
<br>
我们也只见过这一个引擎有能力创造聚集着数百名角色的大规模战场。<br>
<br>
即使不修改引擎，使用这些工具也可以显著改善性能。由于它还提供了完整的源代码，任何人都可以准确了解这些优化的原理，并快速应用它们。<br>
<br>
使用虚幻引擎还将带来许多其他优势，例如便利的多平台支持、强大的UDN支持，以及插件功能。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046631" zoomfile="https://di.gameres.com/attachment/forum/202207/19/084943pddj17mbb7f7choj.jpg" data-original="https://di.gameres.com/attachment/forum/202207/19/084943pddj17mbb7f7choj.jpg" width="600" id="aimg_1046631" inpost="1" src="https://di.gameres.com/attachment/forum/202207/19/084943pddj17mbb7f7choj.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图片由Netmarble提供</font></font></div><br>
<strong><font color="#de5650">团队有什么非常喜欢的虚幻引擎工具或功能吗？</font></strong><br>
<br>
<strong>首席客户端程序员Tae Woo Kim：</strong>蓝图编辑器、Sequencer、Persona、行为树、材质编辑器和Unreal Insights，这些都是非常易用的工具。<br>
<br>
每款工具都具有预览功能，这大大加快了开发过程。<br>
<br>
此外，还有许多非常有用的调试工具。其中，蓝图调试、碰撞分析器和可视记录器对我们产生了巨大的帮助。<br>
<br>
通过插件、命令行或编辑器工具控件，我们可以轻松地为每款游戏扩展出特定功能。例如，我们就为“熟悉的冒险”创建了带有编辑工具的插件。<br>
<br>
感谢实时代码编写功能，快速迭代成为了可能。在修改代码后能够对其进行检查，大幅提高了工作效率。<br>
<br>
<strong><font color="#de5650">考虑到Netmarble曾在《天堂2：革命》中使用过虚幻引擎，那次经验对于《二之国：交错世界》的开发是否存在帮助作用？</font></strong><br>
<br>
<strong>Tae Woo Kim：</strong>我们几乎熟悉虚幻引擎的所有工具，因为《天堂2：革命》中也使用了虚幻引擎。<br>
<br>
我们只是将引擎升级到了较新的版本，获取Epic Games后来增加的额外功能。<br>
<br>
《二之国：交错世界》建立在我们从《天堂2：革命》中所学到的经验之上，通过回顾如何实现那款游戏中的功能，我们节省了不少时间。这允许我们集中精力快速扩展和改进《二之国》的功能。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1046632" zoomfile="https://di.gameres.com/attachment/forum/202207/19/084943sp6zecpzrfwwm1hf.jpg" data-original="https://di.gameres.com/attachment/forum/202207/19/084943sp6zecpzrfwwm1hf.jpg" width="600" id="aimg_1046632" inpost="1" src="https://di.gameres.com/attachment/forum/202207/19/084943sp6zecpzrfwwm1hf.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">图片由Netmarble提供</font></font></div><br>
<strong><font color="#de5650">《二之国：交错世界》运行得如此流畅，能否谈谈你们是如何针对移动平台优化游戏的？</font></strong><br>
<br>
<strong>Tae Woo Kim：</strong>除了基本的优化技术外，我们还大量使用了虚幻引擎提供的重要性管理器和URO（更新速度优化）功能。<br>
<br>
重要性管理器用于确定每个对象的重要性，帮助我们决定要采取的合适行动。关键的优化领域包括：<br>
<br>
<ul><li>忽略不必要的Tick</li><li>展示由视野和距离产生的细节差异</li><li>忽略在视野外产生的某些动画和粒子</li><li>即时更改视野外的某些材质，不进行存储</li><li>将小地图对象分组</li><li>通过缓存避免频繁地生成/销毁Actor</li><li>通过缓存检查和检验文件</li><li>避免创建重复的大纲组件，仅按需创建<br>
</li></ul><br>
<strong><font color="#de5650">《二之国：交错世界》因其流畅的网络代码而受到好评。能否深入谈谈团队的实现方法？</font></strong><br>
<br>
<strong>首席服务器程序员Hyun Koo Kim：</strong><br>
<br>
<strong>1. 即使是在服务器上，也应该使用虚幻引擎的寻径模块。</strong><br>
<br>
<ul><li>当NPC移动时，如果客户端和服务器间的寻径逻辑不同，移动就可能存在偏差。</li><li>要解决这个问题，服务器也必须导入并使用虚幻引擎的寻径模块。<br>
</li></ul><br>
<strong>2. 使用自适应同步控制管理器，它将根据用户数量调整移动同步周期。</strong><br>
<br>
<ul><li>最初，由于担心出现性能问题，我们逐帧收集和发送移动数据包。</li><li>然后，在开发过程中，我们思考了如何在PVP期间加快移动的同步速度。</li><li>我们最终想到一个解决方案：当用户很少时，立即发送数据包，因为这不会影响性能。当用户较多时，先收集数据包，然后再发送，避免产生性能问题。<br>
</li></ul><br>
<strong>3. 在公共世界/实例世界的过渡中使用对象保留系统。</strong><br>
<br>
<ul><li>如果公共世界中的NPC也会在实例世界中使用，那就不得不重新创建之前的对象。这导致生成过渡太过粗糙。</li><li>为了解决这个问题，服务器提供了回收信息，客户端将根据这些信息回收对象，确保过渡平稳。<br>
</li></ul><br>
<strong>4. 专门为出站数据包设立线程池。</strong><br>
<br>
<ul><li>在MMORPG游戏中，许多用户会聚集至一个空间，这是由它的本质决定的。这种情况会导致服务器要向许多用户广播移动和战斗的同步数据包。</li><li>换句话说，从服务器的角度来看，接收量太少，但传输量太大。为了解决这个问题，我们创建了一个仅用于发送行为的线程池，为大量数据包的发送提供支持。<br>
</li></ul><br>
<strong>5. 使用预判定技能系统</strong><br>
<br>
<ul><li>手游网络不稳定，受网络延迟的影响很大。</li><li>开发期间，我们没有在PC环境中遇到过这个问题。然而，当我们在移动环境中进行测试时，我们发现战斗系统感觉不尽如人意。</li><li>为了解决这个问题，服务器会在技能发动时就预判定伤害，并将结果数据包发送给客户端。然后，客户端会在打击帧中反映结果。<br>
</li></ul><br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：虚幻引擎</font></font><br>
  
</div>
            