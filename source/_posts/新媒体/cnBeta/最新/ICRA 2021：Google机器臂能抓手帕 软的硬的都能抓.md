
---
title: 'ICRA 2021：Google机器臂能抓手帕 软的硬的都能抓'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0518/12850269eaa0b78.jpg'
author: cnBeta
comments: false
date: Tue, 18 May 2021 11:10:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0518/12850269eaa0b78.jpg'
---

<div>   
目前机器人相关研究主要是设计机械臂来抓住特定形状的物体，但是很少有抓住可变形状物体(deformable
objects)的相关研究。在变形物体操作中的一个难点是无法知道这个物体内部的参数，例如，对于一个刚性立方体，知道一个固定点相对于其中心的位置足以描述它在三维空间中的形状，但是对一个柔软的物体如丝绸来说，布面上的一个点可以在其他部分移动时保持固定。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/0518/12850269eaa0b78.jpg" referrerpolicy="no-referrer"></p><p>这使得感知算法难以描述织物的完整“状态”，特别是在遮挡的情况下。</p><p>此外，即使有一个被充分描述的可变形物体，其动力学也是复杂的。这使得在对可变形物体进行某种操作之后，很难预测其未来的状态，通常需要多步(multi-step)规划来达到目标状态。</p><p>在 ICRA 2021会议上，Google 发布了一个名为 deformaleravens 的开源模拟基准，对可变形物体操作的研究有极大促进作用。</p><p><img src="https://static.cnbetacdn.com/article/2021/0518/9fc635cf69b1f10.jpg" referrerpolicy="no-referrer"></p><p>论文中共设计了12个任务，包括操作电缆、织物和包，还包括一系列模型架构，用于操纵可变形物体，使其达到预期的目标状态。</p><p>这些模型架构也能够让机器人重新排列电线来达到目标状态，平滑地使非钢体如织物达到指定形状，或是将物品放入袋子中。</p><p>这是第一个包含特定任务的模拟器，在这个任务中机器人必须使用一个袋子来容纳其他物品，这对机器人学习更复杂的相对空间关系提出了关键的挑战。</p><p>DeformableRavens 基准数据集</p><p>Deformaleravens 扩展了之前Google对重排列对象(rearranging objects)的工作，包括一套12个模拟任务，覆盖一维、二维和三维可变形结构。每个任务都包含一个模拟的 UR5手臂和一个用于捏握的模拟夹钳，并与脚本演示器捆绑在一起，自动收集用于模仿学习的数据。任务随机化分布中项的起始状态，以测试不同对象配置的一般性。</p><p><img src="https://static.cnbetacdn.com/article/2021/0518/0f0d8bd7d977957.jpg" referrerpolicy="no-referrer"></p><p>UR5 是一款轻量级、可适应的协作式工业机器人，具有极高的灵活性，可处理中型应用程序。UR5e 的设计是为了无缝集成到广泛的应用程序。UR5e 也提供 OEM 机器人系统，并带有三向示教器（3-position teach pendant）。</p><p><img src="https://static.cnbetacdn.com/article/2021/0518/99f88dadfa94549.jpg" referrerpolicy="no-referrer"></p><p>为操作任务指定目标对于可变形物体尤其具有挑战性。考虑到它们复杂的动力学和高维配置空间，目标不能像一组刚性物体姿势那样容易确定，并且可能涉及复杂的相对空间关系，比如“将物品放入袋子”。</p><p>因此，除了通过分发脚本示范定义的任务之外，我们的基准还包含由目标映像指定的目标条件化任务。对于受目标限制的任务，给定的对象起始配置必须与一个单独的image配对，该映像显示相同对象的所需配置。这种特殊情况的成功取决于机器人是否能够使当前的配置足够接近目标图像中传达的配置。</p><p>Goal-Conditioned Transporter Networks 是一个为了补充模拟基准测试中的目标条件化任务，而将目标条件化集成到Google之前发布过的 Transporter Network 架构中，这是一个以行动为中心的模型架构，它通过重新排列深层特征来从视觉输入推断空间位移，很好地适用于刚性对象操作。</p><p>该体系结构以当前环境的图像和目标图像作为输入，计算这两个图像的深度视觉特征，然后利用元素乘法结合特征，对场景中的刚性和可变形物体进行相关处理。Transporter 网络结构的一个优点是它保留了视觉图像的空间结构，提供了归纳偏差，将基于图像的目标条件化为一个更简单的特征匹配问题，并利用卷积网络提高了学习效率。</p><p>一个涉及目标条件的实例任务如，为了将绿色块放入黄色袋子中，机器人需要学习空间特性，使其能够执行一系列多步骤的动作，以打开黄色袋子的顶部开口，然后将块放入其中。在它把方块放入黄色袋子之后，则成功结束。如果在目标图像中块被放在蓝色袋子中，则需要把块放在蓝色袋子中。</p><p><img src="https://static.cnbetacdn.com/article/2021/0518/e241bde763ab4cc.jpg" referrerpolicy="no-referrer"></p><p>结果表明，Goal-Conditioned Transporter Networks 使agent可以操纵变形结构到灵活指定的配置，而不需要测试时间的视觉锚目标位置。我们还通过在2D 和3D 变形体任务上进行测试，显著扩展了使用 Transporter Networks 操纵变形物体的先前成果。实验结果进一步表明，该方法比传统的基于地面真实位姿和顶点位置的方法具有更高的抽样效率。</p><p><img src="https://static.cnbetacdn.com/article/2021/0518/caab35a3e5fb372.jpg" referrerpolicy="no-referrer"></p><p>例如所学习的策略可以有效地模拟装袋任务，还提供目标图像以便机器人必须推断应该将物品放入哪个袋子。</p><p><img src="https://static.cnbetacdn.com/article/2021/0518/8699ad1b693e3bc.jpg" referrerpolicy="no-referrer"></p><p>未来这项工作还有几个可扩展的目标，例如减少观察到的失败模式。例如当机器人拉袋子向上，并导致抓着的东西掉下去时，就失败了。</p><p>另一种情况是，机器人将物品放置在包的不规则外表面，导致物品脱落。未来的算法改进可能允许动作以更高的频率运行，这样机器人可以实时作出反应来抵消这些可能的失败情况。</p><p><img src="https://static.cnbetacdn.com/article/2021/0518/85ca9ce73f8a9e9.jpg" referrerpolicy="no-referrer"></p><p>另一个发展领域是使用不需要专家演示的技术来训练基于 Transporter network 的可变形物体操作模型，比如基于实例的控制或基于模型的强化学习。</p>   
</div>
            