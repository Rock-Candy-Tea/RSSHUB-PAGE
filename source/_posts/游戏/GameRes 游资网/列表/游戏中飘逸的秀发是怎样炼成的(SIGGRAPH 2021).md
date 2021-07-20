
---
title: '游戏中飘逸的秀发是怎样炼成的(SIGGRAPH 2021)'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202105/25/095106t98c850tdnd0kdvd.jpg'
author: GameRes 游资网
comments: false
date: Tue, 25 May 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202105/25/095106t98c850tdnd0kdvd.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2498017">
<div class="quote"><blockquote>物质点方法最近在模拟多材料及其大规模耦合方面展现出了非常好的效果。然而，在包含碎片的场景中，MPM比传统的拉格朗日方法表现出更多的耗散性和数值粘度。我们提出一种积分方法，该方法可以在每个时间步校正粒子的位置。与传统的积分器相比，我们的方法有效地降低了模拟中速度的平滑和非物理粘度。相关文章已被计算机图形学顶级会议SIGGRAPH收录。</blockquote></div><br>
最近，元宇宙(Metaverse)的概念引起了许多人的关注，人们希望能够创造一个虚拟的世界，并且在其中拥有现实世界般丰富的生活体验。然而，使用计算机还原真实世界是一件非常困难的事情。许多我们习以为常的现象，在微观上是非常复杂的。海滩上行驶的越野汽车扬起满天沙尘；车窗中探出头的女孩被风吹散了头发；海浪拍打在礁石上，溅起细密的浪花。想要在计算机中重现这样的场景，往往需要用超大量的粒子和元素来描述这些运动的物体：飞舞的沙子、飘散的发丝和飞溅的水珠，并且需要正确地处理它们之间的碰撞和相互作用，才能得到令人满意的视觉效果。<br>
<br>
<div align="center">
<img id="aimg_980562" aid="980562" zoomfile="https://di.gameres.com/attachment/forum/202105/25/095106t98c850tdnd0kdvd.jpg" data-original="https://di.gameres.com/attachment/forum/202105/25/095106t98c850tdnd0kdvd.jpg" width="554" inpost="1" src="https://di.gameres.com/attachment/forum/202105/25/095106t98c850tdnd0kdvd.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">[ 图一：真实世界现象背后都有复杂的物理作用 ]</font></font></div><br>
在物理模拟中，物质通常用粒子或网格来表示。如图二所示，物质点法（Material Point Method，MPM）是一种综合了两种方式优点的方法，通过粒子和网格的混合，使得方法对于大规模的物理模拟有着更高的计算效率和更好的可并行性。如果单一的采用粒子或网格来表示物质，就需要对周围的粒子或网格进行额外的计算。而物质点法可以在网格上求解方程，以驱使粒子移动和形变，从而模拟出粒子的运动。以低耗算力来达到丰富的视觉效果。<br>
<br>
<div align="center">
<img id="aimg_980563" aid="980563" zoomfile="https://di.gameres.com/attachment/forum/202105/25/095106axz5mbfyd6gx9ghq.jpg" data-original="https://di.gameres.com/attachment/forum/202105/25/095106axz5mbfyd6gx9ghq.jpg" width="554" inpost="1" src="https://di.gameres.com/attachment/forum/202105/25/095106axz5mbfyd6gx9ghq.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">[ 图二：物质点法的计算过程 (Stomakhin et al. 2013) ]</font></font></div><br>
物质点法为了实现在粒子和网格之间进行物理量的传输和转换，就需要对粒子的速度和位置进行时序上的积分。现有的积分器普遍有着数值粘性过大的缺点：当一个场景中的粒子不断分离和散开时，现有积分器会使得物体的运动显得过于粘稠。我们在基于物质点法搭建头发模拟器的时候，注意到了这个问题：发丝之间仿佛打上了发蜡，聚集成簇，难以实现我们想要的飘逸的效果，就像图三中展示的这样。<br>
<br>
<div align="center">
<img id="aimg_980564" aid="980564" zoomfile="https://di.gameres.com/attachment/forum/202105/25/095107cjz5856587bso87e.jpg" data-original="https://di.gameres.com/attachment/forum/202105/25/095107cjz5856587bso87e.jpg" width="554" inpost="1" src="https://di.gameres.com/attachment/forum/202105/25/095107cjz5856587bso87e.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">[ 图三：基于传统积分器实现的头发模拟效果 ]</font></font></div><br>
让我们试着想象一下。若是在没有粘性的情况下，两个粒子要想分离，可以直接按照“路程=速度x时间”来计算任意时间两个粒子移动的相对距离。然而，当我们使用物质点法（MPM），加入背景网格进行模拟时，便会产生两个问题：<br>
<br>
<ul><li>首先，物质点法假定了物质是连续的。这样的假设禁止一块材料与附近的其他材料自由分离。在材料不分离的状态下，连续性假设能够正确处理材料内部的应力。然而，这个假设并不适用于材料分离的时候，由于这一前提下材料不具备独立的运动状态，所以很难分离。</li><li>其次，由于物质点法下信息反复在网格和粒子之间传递。不同方向的粒子被映射到同一个网格节点上，他们的速度就被“混合”了起来。相反的速度相互抵消，粒子的动能也就减小了。只要两个粒子无法逃逸出这个他们同时作用的区域，每过一段时间，总动能就会损失一点，以至于最后粒子的运动趋于停滞。<br>
</li></ul><br>
<div align="center">
<img id="aimg_980565" aid="980565" zoomfile="https://di.gameres.com/attachment/forum/202105/25/095107qv8rh3v3ekui58uh.jpg" data-original="https://di.gameres.com/attachment/forum/202105/25/095107qv8rh3v3ekui58uh.jpg" width="554" inpost="1" src="https://di.gameres.com/attachment/forum/202105/25/095107qv8rh3v3ekui58uh.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">[ 图四：不同积分器实现的粒子分离效果对比 ]</font></font></div><br>
解决物质点法积分器带来的运动粘稠这个问题，就是我们这项研究的动机。<br>
<br>
要想看得更远，就需要站在巨人的肩膀上。回顾前人的工作，最早的网格和粒子混合计算积分器来自于一种被称为粒子胞元法(Particle-in-Cell, PIC)的方法。在我们的简化模型中可以看到，使用粒子胞元法的粒子几乎在模拟刚开始时就丧失了他们的动能。为了克服这种方法带来的严重的数值粘性，隐式粒子流体法（Fluid-Implicit-Particle，FLIP)应运而生。它在速度积分时保留了上一步的粒子速度，这种速度所带有的信息通常比背景网格平均后分配的信息要丰富许多，我们称之为高频亚网格信息。在2003年以后，上述两种方法成为了视觉特效与影视工业中进行河流、海洋等液体模拟的标准积分器工具。然而，隐式粒子流体法（FLIP）在我们的简化模型中依然带有明显的粘稠现象。2015年，研究人员在原有粒子胞元法的基础上，增加了切速度场的成分，创造了仿射粒子胞元法（Affine Particle-in-Cell，APIC)。在我们的简化模型测试中，使用仿射粒子胞元法（APIC）模拟的粒子的确能实现分离，但由于线性动量部分被网格进行了平均，分离的过程异常“艰难”。我们将这种现象称为“位置陷阱”。如图五所示，两个本来应该分离的粒子，由于在进行粒子向网格上的映射时，网格格点上的速度被平均了，导致映射回粒子上时，实际产生的速度方向和真实有比较大的差异，所以分离效果比较差。<br>
<br>
<div align="center">
<img id="aimg_980566" aid="980566" zoomfile="https://di.gameres.com/attachment/forum/202105/25/095107q4090k6n0630f9n4.jpg" data-original="https://di.gameres.com/attachment/forum/202105/25/095107q4090k6n0630f9n4.jpg" width="554" inpost="1" src="https://di.gameres.com/attachment/forum/202105/25/095107q4090k6n0630f9n4.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">[ 图五：基于FLIP进行计算出现的“位置陷阱”现象 ]</font></font></div><br>
如何避免粒子落入这个“位置陷阱”成为我们需要解决的首要问题。受到隐式粒子流体法（FLIP）的启发，它通过速度积分时保留的高频亚网格信息来实现丰富的速度信息，我们想到是否可以将高频亚网格信息也引入位置积分来解除这个“陷阱”。为了保持材料的连续性，在粒子不分离的状态下，我们依然可以使用隐式粒子流体法（FLIP）进行求解，而当粒子面临分离的时候，我们则将高频亚网格信息引入位置积分来避免“位置陷阱”的出现。<br>
<br>
在本项研究中，我们将这个自研的新型积分器方法命名为可分离隐式粒子流体法（Separable FLIP，SFLIP)。这个新方法的特点是，在材料分离的时刻使用一部分粒子自身速度（而不仅仅是网格节点速度）来对位置进行积分，从而在连续性假设不再成立的时候减轻粒子-网格转移过程中的数值粘度。如图六所示，在网格信息重新传递回粒子的时候，考虑粒子自身的速度进行积分，两个粒子顺利分离，与图五相比有了明显的改进。<br>
<br>
<div align="center">
<img id="aimg_980567" aid="980567" zoomfile="https://di.gameres.com/attachment/forum/202105/25/095107bkgg0gld5gfgfaae.jpg" data-original="https://di.gameres.com/attachment/forum/202105/25/095107bkgg0gld5gfgfaae.jpg" width="554" inpost="1" src="https://di.gameres.com/attachment/forum/202105/25/095107bkgg0gld5gfgfaae.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">[ 图六：基于SFLIP解决“位置陷阱”问题 ]</font></font></div><br>
此外，我们也注意到，仿射粒子胞元法（APIC）和隐式粒子流体法（FLIP）之间的简单组合仿射粒子流体法（AFLIP）可以以低分辨率保留相对复杂的动态结构。所以，我们将可分离隐式粒子流体法（SFLIP）的概念也扩展到了仿射粒子流体法（AFLIP），从而让粒子更容易分离，我们将这种新颖的方案称为仿射可分离粒子流体法（ASFLIP）。<br>
<br>
<div align="center">
<img id="aimg_980568" aid="980568" zoomfile="https://di.gameres.com/attachment/forum/202105/25/095108slz6x66swwknus6b.jpg" data-original="https://di.gameres.com/attachment/forum/202105/25/095108slz6x66swwknus6b.jpg" width="554" inpost="1" src="https://di.gameres.com/attachment/forum/202105/25/095108slz6x66swwknus6b.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">[ 图七：不同积分器实现的头发模拟效果对比 ]</font></font></div><br>
基于上述的SFLIP和ASFLIP方法，我们可以有效的改善头发模拟中的粘连问题，从而实现了更为飘逸更为顺滑的头发模拟，为虚拟角色的提供了更好更真实的表现能力。<br>
<br>
作为总结，本研究的主要贡献在于对现有MPM积分器的调研和新积分器开发，其中包括：<br>
<br>
<ul type="1" class="litype_1"><li>重新审视MPM中常用的各种积分器的连续性假设和数值粘度。</li><li>提出了一种能更好地保留高频信息和动能的积分器，相比传统方法，它几乎没有额外的计算成本。</li><li>提出了一种更易于让粒子分离的积分器，并将其应用于FLIP和AFLIP，以打破分离的材料之间的连续性假设。<br>
</li></ul><br>
<i><font color="#808080">详细的资料和研究内容，请参考项目网站：http://yunfei.work/asflip/</font></i><br>
<br>
<strong>参考文献</strong><br>
<br>
<i><font color="#808080">Stomakhin, A., Schroeder, C., Chai, L., Teran, J., & Selle, A. (2013). A material point method for snow simulation. ACM Transactions on Graphics (TOG), 32(4), 1-10.</font></i><br>
<br>
<font size="2"><font color="#808080">作者/Yun (Raymond) Fei、Qi Guo、Rundong Wu、 Li Huang、Ming Gao 腾讯互动娱乐 研究员</font></font><br>
<font size="2"><font color="#808080">来源：腾讯游戏学院</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            