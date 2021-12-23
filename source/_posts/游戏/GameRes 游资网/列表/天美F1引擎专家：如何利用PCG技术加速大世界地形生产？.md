
---
title: '天美F1引擎专家：如何利用PCG技术加速大世界地形生产？'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202112/10/094719i1btprhm4mccmbb1.jpg'
author: GameRes 游资网
comments: false
date: Fri, 10 Dec 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202112/10/094719i1btprhm4mccmbb1.jpg'
---

<div>   
以下文章来源于TiMi Club 天美俱乐部 ，作者腾讯天美工作室群<br>
<br>
导语：天美十三周年，天美联合知乎游戏，举办“游戏未来十三问”主题圆桌，邀请游戏从业者、玩家和广大朋友们，一同探讨和展望游戏的未来。本文为圆桌议题“2021年，游戏行业有哪些能提升开发效率的“黑科技”，前景如何？”下的回答，希望对大家有所帮助。<br>
<br>
答者：潜龙旭，天美 F1 工作室技术中台引擎程序团队负责人<br>
<br>
不知不觉在游戏开发行业已过十年，从刚入行的技术小白，到现在依然什么都不懂的技术搬砖工，见证了一个时代的游戏技术变革。我本人先后做过游戏开发 SDK，端游 MMO，休闲手游，重度手游，大世界手游，大世界端游等各品类产品，现在是天美 F1 工作室技术中台引擎程序团队负责人。<br>
<br>
游戏行业发展很快，玩家对游戏的要求越来越高，游戏对技术的要求也越来越高，开发量也越来越大。我现在所在的天美 F1 工作室正在开发 AAA 级全平台的大世界游戏，这是一件非常具有挑战的事情。<br>
<br>
本人作为游戏引擎程序，深知技术更新之快，需要不断的学习才能接受这个挑战。所幸我们已经提前在多个方向积累了对标国际 AAA 大厂的技术能力，并且还在全球招募了不少具有 AAA 项目研发背景的各方面人才。通过不断的夯实技术基础，我们有能力也有信心接受新的挑战。在我们储备的技术中，PCG 的技术是目前大世界游戏必不可少的一种技术，现在做一些简单介绍。<br>
<br>
PCG（Procedural Content Generation,过程化内容生成）技术是最近比较热的提升游戏生产效率的一类技术。它是什么意思呢？<br>
<br>
网络百科给出的答案：过程生成（英语：Procedural Generation）是计算机科学中一种使计算机自动制造一类数据的算法。在计算机图形学中，它也被称为随机生成，常用于制作材质贴图和三维模型资源，并在电子游戏领域中用于自动制造大量游戏内容。过程化生成有着减小文件体积、扩大内容量、增强游戏随机性等优点。<br>
<br>
我个人的理解：如果在游戏中应用，简单说，过程化内容生成就是利用算法来自动生成游戏内容。原有的游戏内容需要美术和策划花费大量的精力制作，过程化的方式可以大大降低人工成本，除了可以节省一些重复的人工劳动之外，甚至可以自动创作出一些新的设计内容。试想如果有一个程序可以自动生产游戏，那是多么有意思的一件事情，也许那天到来，游戏开发者都下岗了。<br>
<br>
地形是大世界的基础，大世界没有地形，就没有玩家可立足之地。大世界有多大，地形就有多大，如果能用 PCG 技术加速大世界地形生产，就可以大大减少美术和策划的人力消耗。<br>
<br>
这里有两个难点，一：如何生成真实自然的地形？真实世界的地形并不是一些杂乱无章的形状，他是自然的造化，往往具有赏心悦目的美感。利用算法来生成具有美感的地形是我们面临的第一大挑战。二：大世界巨大，内容繁杂，涉及制作人员众多，如何让制作人员高效的协作是我们面临的第二大挑战。<br>
<br>
今天简单谈一谈如何利用 PCG 技术加速大世界游戏里的地形生产的一些基本思路。<br>
<br>
<strong><font color="#de5650">1. 传统的地形工作流</font></strong><br>
<br>
传统的地形工作流，大家应该很熟悉，美术先找到一些参考的高度图，导入到游戏引擎编辑器中，随后根据自己的需求，通过地形编辑工具来编辑地形。比如 UE 的地形编辑器提供了各种各样的刷子来给美术去手刷和雕刻地形。显而易见，这种方式对美术来说工作量是巨大的。<br>
<br>
<strong><font color="#de5650">2. 过程化地形</font></strong><br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024202" aid="1024202" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094719i1btprhm4mccmbb1.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094719i1btprhm4mccmbb1.jpg" width="199" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094719i1btprhm4mccmbb1.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">一些可用的地形噪声</font></font></div><br>
过程化地形可以利用算法自动地生成地形。常用的有随机噪声地形，这类方法是一类构造式的算法，通过设计一些噪声函数来随机生成地形高度信息，比如常见的 Perlin Noise，Worley Noise，Voronoi Noise，Flow Noise等等。<br>
<br>
另外还有一类是侵蚀算法。通常真实世界的地形，是大自然常年累月对地形进行影响的结果。这类算法会通过对侵蚀过程进行数学建模，然后仿真得到一个拟真的自然的地形效果。比如热侵蚀，水力侵蚀等 ......<br>
<br>
我们来看几个过程化地形的例子。比如如何用噪声表达丘陵地形？就像图中连绵起伏的小山包。其实很简单，我们对噪声函数取一个绝对值就好了，这时噪声的形状会发生一个凸起达到表达丘陵的效果。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024203" aid="1024203" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094720cil55ku5laaxl5j5.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094720cil55ku5laaxl5j5.jpg" width="532" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094720cil55ku5laaxl5j5.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">无人深空中的丘陵地形</font></font></div><br>
<div align="center">
<img id="aimg_1024204" aid="1024204" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094720yoy65z68ontonttz.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094720yoy65z68ontonttz.jpg" width="189" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094720yoy65z68ontonttz.jpg" referrerpolicy="no-referrer">
</div><br>
那如何利用噪声表达山脊线呢？很多大的山脉会有一条条山脊线，就像图中的阿尔卑斯山。我们可以把噪声先取绝对值再取反，翻转后抬高。<br>
<br>
可以观察到在波形相交的地方形成了一个尖点，图里的是二维的情况，如果在三维中就会形成一条条局部最高点的线，这样就可以模拟这种山脊的形状。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024205" aid="1024205" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094720k70iq31yib83m1j6.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094720k70iq31yib83m1j6.jpg" width="475" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094720k70iq31yib83m1j6.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">阿尔卑斯山脉</font></font></div><br>
<div align="center">
<img id="aimg_1024206" aid="1024206" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094720ph3k6czbsshs2kuu.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094720ph3k6czbsshs2kuu.jpg" width="293" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094720ph3k6czbsshs2kuu.jpg" referrerpolicy="no-referrer">
</div><br>
那如何用噪声表达河流呢？我们可以通过域扭曲的方法来做。这种方法很简单，就是对噪声函数的定义域做一次变换，比如这里的例子，简单的对变量做一个位置的偏移，经过多次的位置扭曲，形成一些很特别的效果。可以看到图中高度数据的变化过程，最后形成像河流一样的效果。<br>
<br>
<div align="center">
<img id="aimg_1024207" aid="1024207" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094720tpzvdnjdy7cpuane.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094720tpzvdnjdy7cpuane.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094720tpzvdnjdy7cpuane.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1024208" aid="1024208" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094721r8vy7ksw8cx3yxsx.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094721r8vy7ksw8cx3yxsx.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094721r8vy7ksw8cx3yxsx.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_1024209" aid="1024209" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094722n6w22jrfmwzbxofo.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094722n6w22jrfmwzbxofo.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094722n6w22jrfmwzbxofo.jpg" referrerpolicy="no-referrer">
</div><br>
刚才的讲的几个例子都是一些简单有效的噪声表达地形的方法。但真实的地形其实有一些特别的地方，比如自相似性。什么意思呢？<br>
<br>
我们从不同层次的视角去观察真实地形的时候，会有一些相似的特征。大到山脉，小到山体，更小的山上的每个石头都在起伏。也就是说如果用噪声表达这个特点，需要噪声在多个尺度具有自相似性。<br>
<br>
<div align="center">
<img id="aimg_1024210" aid="1024210" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094722k9tr9494k59rag29.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094722k9tr9494k59rag29.jpg" width="405" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094722k9tr9494k59rag29.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">山脉</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024211" aid="1024211" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094722fc6vjej9q9luwztq.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094722fc6vjej9q9luwztq.jpg" width="403" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094722fc6vjej9q9luwztq.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">山体</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024212" aid="1024212" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094722qfver284ma2qaf4f.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094722qfver284ma2qaf4f.jpg" width="396" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094722qfver284ma2qaf4f.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">山石</font></font></div><br>
为了实现这个效果，我们其实可以直接把多层噪声叠加起来实现。每一层噪声有自己的频率和振幅，叠加在一起就会形成这种具有分形效果的地形。为了更好的控制分形的效果，我们可以调整每层噪声之间的关系：关系有两种，一种是每层频率之间的变化率，另一种是每层振幅之间的变化率。<br>
<br>
特别的，如果每层振幅的变化跟频率的变化互为导数，这种多层噪声叫做粉红噪声。更特别的，如果变化率是 2 的幂次，我们把这种噪声的每层成为一个倍频（Octave），那这种噪声每层频率翻倍，振幅就减半。一般来说，Octave 小于 8 就够用了，太大了计算量增加，效果不会有大的增幅。<br>
<br>
这里是我们常见的分层 Perlin 噪声的效果，在 Octave 为 8 的情况下。可以看到这个分层地形，在大的高度变化上是一个低频的变化，在小的尺度上会有一些高频的变化。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024213" aid="1024213" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094722mxkr7lzrtl3p83pd.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094722mxkr7lzrtl3p83pd.jpg" width="414" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094722mxkr7lzrtl3p83pd.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Layered Perlin Noise</font></font></div><br>
纯过程化地形做的比较好的游戏，有《无人深空》，Minecraft。《无人深空》的地形是做的很不错的，有很多关于噪声的技巧应用，做出来一些挺不错的风格化的效果。<br>
<br>
<div align="center">
<img id="aimg_1024214" aid="1024214" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094723zgrmgwgueewugqtw.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094723zgrmgwgueewugqtw.jpg" width="410" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094723zgrmgwgueewugqtw.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《无人深空》</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024215" aid="1024215" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094723xk0vkn4oaorrs3ve.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094723xk0vkn4oaorrs3ve.jpg" width="450" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094723xk0vkn4oaorrs3ve.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">《我的世界》</font></font></div><br>
现在总结一下纯过程化地形的特点：<br>
<br>
<ul><li>基于随机的算法；</li><li>技术性是比较强的，美术不易理解；</li><li>容易重复；</li><li>可控性比较差，美术难以调效果<br>
</li></ul><br>
<br>
<strong><font color="#de5650">3. 美术主导的过程化地形生成</font></strong><br>
<br>
既然纯过程化地形生成有这么多问题，那大世界地形制作又想利用过程化技术来提升效率，怎么办？由于游戏场景的最终效果其实是美术来把控的，其实整个场景很复杂，不仅仅只有地形存在，涉及到的东西很多都需要美术来把关，所以我们需要的是美术主导的过程化生成。<br>
<br>
这种工作流需要更多的考量用户友好性，美术使用的工具是交互要人性化，要足够易用的。还需要有良好的艺术性表达性，美术可以很方便的做艺术设计。过程化技术在其中的作用主要是用来提升工作效率，并不像纯粹的过程化地形生成，一键生成地形，美术很难参与其中。<br>
<br>
这样的一个工作流，它的主体成员可以是一个比较小的团队组成，由 TA 和引擎工具根据美术需求设计开发地形工具，工具开发完后，美术使用工具设计地形。<br>
<br>
具体来说美术主导的过程化地形工作流分为以下三个阶段：<br>
<br>
1：原始地形生成，这个阶段 LA 和 TA 一起配合，利用一些过程化地形工具，比如 UE4 Landmass，Houdini，World Machine，World Creator，Gaea 之类的，根据世界的结构生成一份原始地形。<br>
<br>
2：过程化工具地形加工，这个阶段美术会在原始地形的基础上进行场景制作，会添加场景的其他层，比如河流，道路，岩石等等，这些场景元素的制作在过程化管线中对应一个个的过程化工具，这些工具可能会对地形产生影响。<br>
<br>
3：人工编辑，所有的过程化工具对地形作用完毕后，如果美术还不满意效果，这时需要进行人工调整，调整后形成最终的地形效果。<br>
<br>
<strong>3.1 原始地形生成</strong><br>
<br>
我们先看原始地形生成，这个阶段的思路是，整个造型过程是从初模到高模，高度图数据从低分辨率到高分辨率的一个过程，然后对真实地形来说侵蚀是很重要的一步。<br>
<br>
以 Houdini 来举例，大概有图例画的这些步骤。整个过程可以完全在 Houdini 内部做，也可以通过自定义的 Houdini Engine 在引擎中制作。完全在 Houdini 里做，对TA来说比较方便，在引擎编辑器内做的话，美术会比较方便。各有优缺点。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024216" aid="1024216" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094723du8aupbaq8opxbcl.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094723du8aupbaq8opxbcl.jpg" width="554" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094723du8aupbaq8opxbcl.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Houdini 地形工作流</font></font></div><br>
具体的，我们来看下这个流程。首先是 Massing，可以通过手绘，投射几何体或者直接导入高度数据进行一个最粗糙的造型，接下来，为了获得更自然的效果，我们对粗模进行一些细节的扰动，这个过程可以通过应用一些噪声来实现，还可以通过在特定区域添加一些障碍物。<br>
<br>
Seeding 后的地形有了一些细节，更自然，也有利于后面的侵蚀效果。再就是裂片，一般真实的山体会被河流或地壳运动切割开来，我们可以通过侵蚀算法加大侵蚀力度来获取这种切割效果。最后我们可以从高度这个层次进行 Remapping，对不同区域进行反复的造型。比如我们在第一遍的时候对地图的平原区域进行造型，第二遍对高原区域进行造型。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024217" aid="1024217" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094724hjau3o212a3baujc.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094724hjau3o212a3baujc.jpg" width="554" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094724hjau3o212a3baujc.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">地形粗模过程</font></font></div><br>
粗模造型在低精度下进行，迭代效率是比较快的，大的造型设计尽量在粗模阶段进行。粗模完成后对地形精度进行上采样，更高的精度可以拥有更多的细节，之后继续进行 Shaping，再之后就是侵蚀了。<br>
<br>
为了获得比较好的侵蚀效果，可以在侵蚀前再进行一次扰动。侵蚀是个比较耗时的操作，要比较快的迭代效果需要 TA 对此很熟悉。如果不满意效果，可以反复的造型和侵蚀，得到最终的原始地形效果。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024218" aid="1024218" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094724xy48v4fcrav9aai9.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094724xy48v4fcrav9aai9.jpg" width="554" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094724xy48v4fcrav9aai9.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">地形高模过程</font></font></div><br>
<strong>3.2 过程化工具地形加工</strong><br>
<br>
原始地形有了后，就进入到了过程化工具地形加工阶段。一般 PCG 的工具管线会按不同的工具种类进行分层，比如按照湖泊，河流，道路，栅栏，植被这样的层次进行划分。<br>
<br>
这里需要注意的是，每个工具之间具有依赖关系，前个工具的输出数据对后个工具会产生影响，比如我先用河流工具生成了一条河流，接着在河流经过的一个区域又用道路工具生成了一条路，那道路工具就需要考虑河流工具。比如我们可以通过输出 Mask 来标记河流的区域，这样道路工具就知道这里有一条河了。<br>
<br>
一般来说，这样的工具顺序需要事先规定好，做好流程的设计。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024219" aid="1024219" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094724j3kfq4ngkzh59kfq.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094724j3kfq4ngkzh59kfq.jpg" width="339" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094724j3kfq4ngkzh59kfq.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">过程化工具流程图</font></font></div><br>
这些过程化的工具都可能对地形产生影响，包括高度和材质，那关于地形的变化，这里有个隐藏的含义是后个工具是在上个工具影响后的地形上进行操作的，比如刚才提到的道路工具在河流之后，那河流工具本身会对地形进行形变，道路工具此时地形的输入就是河流工具对地形形变后的结果。<br>
<br>
当然有些工具可能对地形不会有形变作用，比如栅栏工具一般不会对地形有影响。所以在这个工作流中，我们需要把每层地形的变化都存储下来，如果没有这些中间结果，后面的工具便没有了地形的输入。<br>
<br>
<strong>3.3 人工编辑</strong><br>
<br>
既然过程化解决不了所有问题，那接下来进入到人工编辑阶段。问题又来了，哪些阶段需要进行地形的人工编辑呢？<br>
<br>
先回顾一下过程化工具的地形流程，如图，是一个链式的结构，可以看到我们可以在每个工具之间都可以进行人工编辑，比如河流工具对地形影响后，美术不满意，可以进行编辑调整，在调整后的地形基础上，再使用道路工具铺设道路，道路工具又会对地形进行影响，之后美术又可以继续在此基础上进行地形效果的调整。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024220" aid="1024220" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094725q9gib1pqqqgi77gz.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094725q9gib1pqqqgi77gz.jpg" width="545" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094725q9gib1pqqqgi77gz.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">过程化工具地形流程图</font></font></div><br>
有了这样的流程，就存在地形的修改如何存储的问题？<br>
<br>
为了实现非破坏性编辑，每层地形的修改都需要存储，推荐不要把修改数据存储到编辑器场景中，而是存到外部文件，这样对 Houdini 比较友好。<br>
<br>
另外一个值得思考的问题是人工修改的这部分数据是存储差异还是直接覆盖？存储差异直观上来看，有个优点，前阶段的工具地形输出有变化的时候，人工修改的数据可能可以继承，比如由于某些原因，道路工具把路整体抬高了，由于存储的是差异值，之前对一些局部的人工修改就可以复用。<br>
<br>
缺点是，可复用的数据的合理性其实是很模糊的，很多时候差异数据不可用，这种数据应用后出错了也不易发觉。采用覆盖的方式，优缺点是显而易见的，直接覆盖不会出错，但一旦前面的层对地形有修改，后续的每一层的手工修改就全部报废了，后续每一层都需要修改。<br>
<br>
基于正确性第一的原则，推荐使用覆盖而非差异的方式。人工修改一般只是修改局部，覆盖的方式就需要存两种数据，一种是标记哪些区域修改了的 Mask 信息，一种是需要覆盖的高度图信息。<br>
<br>
这样我们就有了一套完备的地形工作流程，但给美术实际使用时仍然遇到了不少问题。<br>
<br>
第一个是可手动编辑的阶段过多，大世界一般都会有十几层甚至几十层，工作流可调整的地方太多，其中的逻辑美术不易理解，第二个可控性差，之前也提到，前面层的修改会影响后面，导致频繁修改，非常容易出错，第三个最直接的就是美术反馈操作太繁琐，不好用。<br>
<br>
<div align="center">
<img id="aimg_1024221" aid="1024221" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094725rodmhhb7s7xgmoaq.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094725rodmhhb7s7xgmoaq.jpg" width="418" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094725rodmhhb7s7xgmoaq.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">过程化工具人工修改流程</font></font></div><br>
重新考量了下，这个流程虽说比较完整，但很多阶段其实没必要，由于过程化工具对地形影响频繁，整个阶段可以不需要人工修改地形，所以最终人工修改可以在整个过程化之前和之后进行，这样就可以简化为 4 个大的地形阶段。<br>
<br>
<ul type="1" class="litype_1"><li>原始地形：采用 Houdini，world Machine 输出。</li><li>人工修改 1：美术可以在引擎编辑器中对原始地形进行调整。</li><li>过程化工具地形阶段：合并为一个大的阶段，中间不允许人工调整。</li><li>人工修改 2：对最终地形进行人工调整。<br>
</li></ul><br>
整个过程可以循环重复迭代。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024222" aid="1024222" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094725tj9s1a1ke0ossa3y.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094725tj9s1a1ke0ossa3y.jpg" width="348" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094725tj9s1a1ke0ossa3y.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">过程化地形工作流</font></font></div><br>
<strong>3.4 一些经验小结</strong><br>
<br>
<font color="#de5650">① 可控性很重要</font><br>
<br>
完全的随机地形生成不可用<br>
<br>
美术导向，而非技术导向<br>
<br>
<font color="#de5650">② 非破坏性编辑</font><br>
<br>
原始地形不可丢<br>
<br>
可反复快速迭代<br>
<br>
<font color="#de5650">③ 数据存储</font><br>
<br>
便于导入导出<br>
<br>
使用覆盖，不要使用差异<br>
<br>
<font color="#de5650">④ 依赖关系</font><br>
<br>
后阶段依赖前阶段地形<br>
<br>
杜绝循环依赖<br>
<br>
编辑前及时锁定，避免冲突<br>
<br>
编辑前及时更新，避免错误修改<br>
<br>
<font color="#de5650">⑤ 不要过度依赖过程化</font><br>
<br>
<font color="#de5650">⑥ 锁定</font><br>
<br>
阶段越前，越需要更早确定<br>
<br>
地形修改工作量非常大<br>
<br>
<strong><font color="#de5650">4. PCG 技术的前景</font></strong><br>
<br>
PCG 技术不仅仅用来生成地形，还可以用于生成大世界环境中的方方面面，比如植被，道路，河流，湖泊，海洋，街区，建筑等等。<br>
<br>
如果把这些问题在实际项目中全部解决，生成符合美术需求的资产，那制作大世界游戏的成本会大大降低。当然并不是说美术没有事情可以做了，而是美术可以专注于艺术创作，去除不需要关心的重复劳动。这样 PCG 技术可以起到加快设计和验证效果的迭代速度。<br>
<br>
另外 PCG 技术还可以和机器学习等其他技术融合，来辅助美术设计，这类技术通过对已有的资产库数据进行学习，自动生成一些新的数字资产，美术再进行一些挑战，这样可以加快创作速度。<br>
<br>
PCG 技术甚至可以在一定程度上开放给玩家，用于制作 UGC 内容，玩家可以像游戏制作者一样创造游戏世界。整个 PCG 技术的应用前景空间巨大。<br>
<br>
目前天美 F1 技术中台除了在 PCG 管线上有不错的积累，其他 AAA 游戏技术我们也取得了一些成绩。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_1024223" aid="1024223" zoomfile="https://di.gameres.com/attachment/forum/202112/10/094726qcdfl5t1i8tlfjlp.jpg" data-original="https://di.gameres.com/attachment/forum/202112/10/094726qcdfl5t1i8tlfjlp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202112/10/094726qcdfl5t1i8tlfjlp.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">F1 技术积累图</font></font></div><br>
引擎技术、美术等方面，目前我们已经储备并在不断优化验证的方向包括：<br>
<br>
<ul><li>对标顶级 AAA 公司的，支持 AAA 品质开放大世界的 PCG 工业化游戏内容生产管线</li><li>次世代主机级渲染技术及美术制作工艺</li><li>GTA 级的大都市模拟游戏 AI 技术</li><li>超拟真载具物理仿真技术</li><li>基于光学动捕和 MotionMatching 的角色动画技术及制作管线</li><li>基于 FACS 系统的写实面部表情绑定和动画管线</li><li>基于 AI 学习的人物动画生产技术</li><li>...<br>
</li></ul><br>
最后欢迎大家加入 F1 工作室，和天美共同成长，做成国产 AAA 大作，实现个人技术突破。<br>
<br>
<font size="2"><font color="#808080">来源：腾讯天美工作室群</font></font><br>
<br>
  
</div>
            